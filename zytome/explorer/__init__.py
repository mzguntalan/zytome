import os

import anndata as ad
import numpy as np
import requests

from zytome.portal._interfaces.dataset import DatasetInterface


def get_zytome_dir() -> str:
    """This is where the datasets are stored"""
    return os.getenv("Z_ZYTOME_DIR", "./.zytome")


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
