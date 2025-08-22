import os
from functools import partial
from typing import Callable
from typing import List
from typing import Optional

import anndata as ad
import numpy as np
import requests

from zytome.portal._interfaces.dataset import DatasetInterface
from zytome.portal._interfaces.dataset import Handler
from zytome.portal.gtex.base import GTExBulkInterface

Filter = Callable[[ad.AnnData], ad.AnnData]


class Dataset(DatasetInterface):
    def __init__(
        self, adata: ad.AnnData, dataset: DatasetInterface, filters: List[Filter]
    ):
        self._adata = adata
        self._dataset = dataset
        self._filters = filters
        self._raw = None
        self._raw_normalized_by_feature_length = None

    @property
    def short_name(self) -> str:
        return self._dataset.short_name

    @property
    def long_name(self) -> str:
        return self._dataset.long_name

    @property
    def tissues(self) -> list[str]:
        return self._dataset.tissues

    @property
    def diseases(self) -> list[str]:
        return self._dataset.diseases

    @property
    def assays(self) -> list[str]:
        return self._dataset.assays

    @property
    def organism(self) -> str:
        return self._dataset.organism

    @property
    def num_cells(self) -> int:
        return self._dataset.num_cells

    @property
    def download_link(self) -> str:
        return self._dataset.download_link

    @property
    def handler(self) -> Handler:
        return self._dataset.handler

    @property
    def adata(self) -> ad.AnnData:
        self._apply_filters()
        return self._adata

    def _apply_filters(self):
        adata = self._adata

        for filter_fn in self._filters:
            adata = filter_fn(adata)

        self._filters = []
        self._adata = adata

    @property
    def raw(self) -> np.ndarray:
        return self.adata.X.toarray()

    @property
    def raw_normalized_by_feature_length(self) -> np.ndarray:
        return self.raw / self.feature_lengths[None, :]

    @property
    def feature_lengths(self):
        return np.array(self.adata.var["feature_length"].values)

    @property
    def feature_names(self):
        return list(self.adata.var["feature_name"].index)

    @property
    def feature_name_name(self):
        """Returns the name of the index column of the feature name series. Example: 'ensembl_id'. This is useful in identifying gene name convetion"""
        return self.adata.var["feature_name"].index.name

    @property
    def feature_types(self):
        return self.adata.var["feature_type"]

    def filter(self, filter_fn: Filter) -> "Dataset":
        return Dataset(self._adata, self._dataset, self._filters + [filter_fn])


def load_data_from_portal(dataset: DatasetInterface):
    adata = read_raw_h5ad(dataset)
    adata.X = adata.raw.X  # converts X back to the raw
    return Dataset(adata, dataset, [])


def make_filter(
    assays: Optional[List[str]] = None,
    tissues: Optional[List[str]] = None,
    feature_types: Optional[List[str]] = None,
    max_cells: Optional[int] = None,
    rng: Optional[np.random.Generator] = None,
):

    return partial(
        filter_adata,
        assays=assays,
        tissues=tissues,
        feature_types=feature_types,
        max_cells=max_cells,
        rng=rng,
    )


def get_zytome_dir() -> str:
    """This is where the datasets are stored"""
    return os.getenv("Z_ZYTOME_DIR", "./.zytome")


def read_gct_gz(dataset: GTExBulkInterface) -> ad.AnnData:
    assert dataset.handler == "GTEx"
    dir_name = dataset.long_name
    short_name = "dataset"
    download_link_gct_gz = dataset.download_link
    metadata_link = dataset.metadata_link


def read_raw_h5ad(dataset: DatasetInterface) -> ad.AnnData:
    """
    This function reads the raw AnnData object for a given dataset.
    It first checks if the raw file exists locally. If not, it downloads
    it from the dataset's download link, saving it to a dataset-specific
    directory.  The directory structure is determined by the dataset's
    long name and the zytome directory obtained from `get_zytome_dir()`.
    Finally, it reads the AnnData object from the saved h5ad file.

    Parameters
    ----------
    dataset : DatasetInterface
        An object implementing the DatasetInterface, providing access to
        the dataset's long name and download link.

    Returns
    -------
    ad.AnnData
        The AnnData object read from the raw h5ad file.
    """
    dir_name = dataset.long_name
    short_name = "dataset"
    download_link = dataset.download_link

    base_dir = get_zytome_dir()
    dataset_dir = os.path.join(base_dir, dir_name)
    os.makedirs(dataset_dir, exist_ok=True)

    raw_path = os.path.join(dataset_dir, f"{short_name}_raw.h5ad")

    if not os.path.exists(raw_path):
        print(f"[INFO] Raw file not found, downloading from {download_link}...")
        response = requests.get(download_link, stream=True)
        response.raise_for_status()
        with open(raw_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[INFO] Saved raw data to {raw_path}")

    print(f"[INFO] Reading AnnData from {raw_path}")
    return ad.read_h5ad(raw_path)


def filter_adata(
    adata: ad.AnnData,
    *,
    assays: Optional[List[str]] = None,
    tissues: Optional[List[str]] = None,
    feature_types: Optional[List[str]] = None,
    max_cells: Optional[int] = None,
    rng: Optional[np.random.Generator] = None,
) -> ad.AnnData:
    """
    Filter AnnData object by cell-level metadata (assay, tissue),
    gene-level metadata (feature_type), and optionally cap the number
    of cells. Keeps .X sparse.

    Parameters
    ----------
    adata : AnnData
        Input AnnData object.
    assays : list[str], optional
        List of assay names to keep.
    tissues : list[str], optional
        List of tissue names to keep.
    feature_types : list[str], optional
        List of feature types to keep.
    max_cells : int, optional
        Maximum number of cells to retain after filtering.
    rng : np.random.Generator, optional
        NumPy random generator for sampling. If None, no shuffling,
        just take the first max_cells cells.

    Returns
    -------
    AnnData
        Filtered AnnData object.
    """
    mask_cells = np.ones(adata.n_obs, dtype=bool)
    mask_genes = np.ones(adata.n_vars, dtype=bool)

    if assays:
        mask_cells &= adata.obs["assay"].isin(assays)
    if tissues:
        mask_cells &= adata.obs["tissue"].isin(tissues)
    if feature_types:
        mask_genes &= adata.var["feature_type"].isin(feature_types)

    adata_filtered = adata[mask_cells, mask_genes]

    if max_cells is not None and adata_filtered.n_obs > max_cells:
        if rng is not None:
            selected_idx = rng.choice(
                adata_filtered.n_obs, size=max_cells, replace=False
            )
        else:
            selected_idx = np.arange(max_cells)
        adata_filtered = adata_filtered[selected_idx, :]

    return adata_filtered
