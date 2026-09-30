"""Batch classification of exponent matrices: relaxed / strict census membership masks (exact int64), support."""
import numpy as np
from lib42 import STRUCTS, SMAT
KEYS = [(nm, 'row' if tr else 'col') for nm, tr, s in STRUCTS]
_AR = [SMAT[(nm, tr, True)] for nm, tr, s in STRUCTS]
_AS = [SMAT[(nm, tr, False)] for nm, tr, s in STRUCTS]
def member_masks(X):
    """X: (B, 256) int64. Returns (strict_mask, relaxed_mask) int arrays, bit k = in structure KEYS[k]."""
    ms = np.zeros(len(X), dtype=np.int64); mr = np.zeros(len(X), dtype=np.int64)
    for k in range(18):
        ms |= (~(X @ _AS[k].T).any(axis=1)).astype(np.int64) << k
        mr |= (~(X @ _AR[k].T).any(axis=1)).astype(np.int64) << k
    return ms, mr
