"""Working with multiple datasets together"""

import anndata as ad
import numpy as np

from zytome.explorer import Dataset


def _rearrange_features_to_match_another(
    S: ad.AnnData, T: ad.AnnData
) -> tuple[ad.AnnData, np.ndarray]:
    """
    Rearrange features (variables) of AnnData S to match the features of T.

    Args:
        S: AnnData with shape (n_obs, n_vars).
        T: AnnData with shape (m_obs, t_vars).

    Returns:
        S_rearr: AnnData with vars in the same order as T.var_names.
        marks: boolean np.ndarray of shape (t_vars,), True if feature existed in S.
    """
    S_vars = S.var_names
    T_vars = T.var_names

    marks = np.isin(T_vars, S_vars)

    S_rearr = S[:, S_vars.intersection(T_vars)].copy()
    S_rearr = S_rearr[:, T_vars]  # reorder to match T exactly

    return S_rearr, marks


def rearrange_features_to_match_another(
    source_dataset: Dataset, reference_dataset: Dataset
) -> tuple[Dataset, np.ndarray]:
    """Re-arranges the features in source to match the order of the features in referece.
    Additionally a True-False n-dim vector is used to mark known(True) and unknown(False) data.
    """

    new_adata, marks = _rearrange_features_to_match_another(
        source_dataset.adata, reference_dataset.adata
    )
    return Dataset(new_adata, source_dataset, []), marks
