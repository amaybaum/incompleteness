"""Level 3A reference simulator: RECORD's exact window simulator (record_sim.py, sealed) plus the one new letter

    'c'  conditional flip of the visible pair, (u, v) -> (u XOR v, v); pair code p = u + 2v, so c = (0, 1, 3, 2).

Everything else (State, leap, pair_map, kappa_fn, PASSIVE, the letters o, m, i, f, s, p) is imported from the sealed
module unchanged. run3 is record_sim.run with the extra branch for 'c'.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'record'))
from record_sim import State, kappa_fn, PASSIVE, F_bits   # noqa: E402,F401

LEAPS = 'oimp'


def c_perm(q):
    """pair code q = u + 2v  ->  (u XOR v) + 2v"""
    return ((q & 1) ^ (q >> 1)) | (q & 2)


def run3(protocol, rule, kappa):
    """Joint record distribution of a protocol: (integer counts per record string, total mass)."""
    T = sum(1 for s in protocol if s in LEAPS)
    st = State()
    left = T
    for s in protocol:
        if s in 'om':
            st.pair_map(kappa_fn(kappa), record=(s == 'o'))
        elif s == 'p':
            st.pair_map(kappa_fn(PASSIVE), record=True)
        elif s == 'f':
            st.pair_map(lambda q: (q ^ 2, None), record=False)
        elif s == 's':
            st.pair_map(lambda q: (((q & 1) << 1) | (q >> 1), None), record=False)
        elif s == 'c':
            st.pair_map(lambda q: (c_perm(q), None), record=False)
        elif s != 'i':
            raise ValueError(s)
        if s in LEAPS:
            left -= 1
            st.leap(min(st.a + 1, left), rule)
    counts = [int(x) for x in st.P.sum(axis=0)]
    return counts, 4 ** st.mass_log4
