"""RANK investigation: full-protocol rank (actions interleaved) versus passive rank, small horizons.

Lattice second-order rule on sites [-R, R], R = total protocol length (causal cone), uniform (u, v).
Steps: 'o' = read v_0 then leap; 'i' = leap; 'f' = flip v_0; 's' = swap (u_0, v_0) (local bijections).
Joint matrix J[(prep protocol, prep record), (effect protocol, effect record)] = integer counts.
rank(J) = rank of the conditional table (row scaling), = dim aff{prepVec} + 1 (theorem R0).
"""
import sys
from itertools import product
import numpy as np
sys.path.insert(0, '.')
from lattice_rank import rank_mod, rank_Q, P1, F   # noqa: E402


def run_all(protocol, R, rule):
    W = 2 * R + 1
    m = np.uint32((1 << W) - 1)
    c = np.uint32(R)
    one = np.uint32(1) << c
    idx = np.arange(1 << (2 * W), dtype=np.uint64)
    u = (idx & np.uint64((1 << W) - 1)).astype(np.uint32)
    v = (idx >> np.uint64(W)).astype(np.uint32)
    rec = np.zeros(len(u), dtype=np.int64)
    for st in protocol:
        if st == 'o':
            rec = (rec << 1) | ((v >> c) & np.uint32(1)).astype(np.int64)
            u, v = v, (F(v, m, rule) ^ u) & m
        elif st == 'i':
            u, v = v, (F(v, m, rule) ^ u) & m
        elif st == 'f':
            v = v ^ one
        elif st == 's':
            bu, bv = (u >> c) & np.uint32(1), (v >> c) & np.uint32(1)
            u = (u & ~one) | (bv << c)
            v = (v & ~one) | (bu << c)
    nobs = protocol.count('o')
    return np.bincount(rec, minlength=1 << nobs)


def protocol_matrix(L, alphabet, rule):
    prots = [p for l in range(L + 1) for p in product(alphabet, repeat=l)]
    R = 2 * L
    rows, cols, cache = [], [], {}
    for pp in prots:
        rows += [(pp, r) for r in range(1 << pp.count('o'))]
    for ep in prots:
        cols += [(ep, r) for r in range(1 << ep.count('o'))]
    J = []
    for pp in prots:
        k1 = pp.count('o')
        block = {}
        for ep in prots:
            k2 = ep.count('o')
            Rp = max(1, sum(1 for s_ in pp + ep if s_ in 'oi'))     # exact cone radius
            cnt = run_all(pp + ep, Rp, rule) * (1 << (2 * (2 * R + 1) - 2 * (2 * Rp + 1)))  # common denominator
            block[ep] = cnt.reshape(1 << k1, 1 << k2) if k1 + k2 > 0 else cnt.reshape(1, 1)
        for r in range(1 << k1):
            row = []
            for ep in prots:
                row += [int(x) for x in block[ep][r]]
            J.append(row)
    # drop zero-probability preparations
    J = [row for row in J if row[0] != 0]
    return J


if __name__ == '__main__':
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    for rule in ('linear', 'nonlinear'):
        for alph, name in ((('o',), 'passive'), (('o', 'i'), 'obs+idle'), (('o', 'i', 'f', 's'), 'full')):
            J = protocol_matrix(L, alph, rule)
            rk = rank_Q(J) if len(J) <= 120 else rank_mod(J, P1)
            print(f'PROTOCOL {rule} L={L} {name}: preparations={len(J)} rank={rk}', flush=True)
