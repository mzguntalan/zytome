"""Working with multiple datasets together"""

from typing import Sequence
from typing import Tuple
from typing import Union

import anndata as ad
import numpy as np
import pandas as pd
from scipy import sparse

from zytome.explorer import Dataset


def _rearrange_features_to_match_another_adata(
    S: ad.AnnData,
    T: ad.AnnData,
    # T_column_names: Sequence[str],
    pad_missing: bool = True,  # if True, return full [n, t] with zeros for missing
) -> Tuple[Union[ad.AnnData, ad.AnnData], np.ndarray]:
    """
    Align S's variables to T_column_names.

    Returns:
      - If pad_missing=True: AnnData with X shape [n_obs(S), len(T_column_names)].
        Missing features are zero columns (sparse-safe).
      - If pad_missing=False: AnnData view with only the features that exist in S,
        ordered like T_column_names[marks].
      - marks: boolean array of length len(T_column_names); True if feature existed in S.
    """
    T_column_names = T.var_names
    T_vars = np.asarray(T_column_names)
    idx_in_S = S.var_names.get_indexer(T_vars)  # -1 where missing
    marks = idx_in_S >= 0

    s_idx = idx_in_S[marks]
    S_present = S[:, s_idx]  # view/subset; order follows T where present

    if not pad_missing:
        # Fix var_names to match the subset of T
        S_present = S_present.copy()
        S_present.var_names = T_vars[marks]
        return S_present, marks

    n = S.n_obs
    t = len(T_vars)
    pos_in_T = np.nonzero(marks)[0]

    if sparse.issparse(S.X):
        X_out = sparse.lil_matrix((n, t), dtype=S.X.dtype)
        X_out[:, pos_in_T] = S_present.X  # stays sparse
        X_out = X_out.tocsr()
    else:
        X_out = np.zeros((n, t), dtype=S.X.dtype)
        X_out[:, pos_in_T] = S_present.X

    S_rearr = ad.AnnData(
        X_out,
        obs=S.obs.copy(),
        var=pd.DataFrame(
            {
                "ensembl_id": T_vars,
                "feature_name": T.var["feature_name"],
                "feature_length": T.var["feature_length"],
            },
            index=T_vars,
        ),
        dtype=S.X.dtype,
    )
    S_rearr.obs_names = S.obs_names.copy()
    S_rearr.var_names = T_vars

    return S_rearr, marks


def rearrange_features_to_match_another(
    source_dataset: Dataset, reference_dataset: Dataset
) -> tuple[Dataset, np.ndarray]:
    """Re-arranges the features in source to match the order of the features in referece.
    Additionally a True-False n-dim vector is used to mark known(True) and unknown(False) data.
    """

    new_adata, marks = _rearrange_features_to_match_another_adata(
        source_dataset.adata, reference_dataset.adata
    )
    return Dataset(new_adata, source_dataset, []), marks
