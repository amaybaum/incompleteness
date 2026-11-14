"""Reviewer probe P3 (QPHEN Phase 1 review). Exact; F_2 arithmetic, Fractions.

Checks QX4 A4.1 in the generic F_2 affine-symplectic class (no OI apparatus is
built): Leggett-Garg correlators for a Z-read with an independent uniform kick on
the conjugate slot (the 'SA-1(c) backaction' abstraction of A4.1), fixed affine
symplectic G between reads.

Run types (two reads each, as in QX4 §1):
  (1,2): read t1, G, read t2        -> C12
  (2,3): G, read t2, G, read t3     -> C23
  (1,3): read t1, G, G, read t3     -> C13
K3 forms: s1*C12 + s2*C23 + s3*C13 with s1*s2*s3 = -1; macrorealist NIM bound 1.

m = 1: the single encoded carrier (z, x)   -- A4.1's stated setting.
m = 2: carrier plus one further mode (w, v) -- scope extension, reported only.
Preparations: each slot known (0/1) or uniform; 'SA-1(c)' = every mode has exactly
one known slot (or a both-unknown environment mode); 'sharp' = all known.
"""
import itertools
from fractions import Fraction
import numpy as np

def sp_group(m):
    n = 2*m
    J = np.zeros((n, n), dtype=int)
    for k in range(m):
        J[2*k, 2*k+1] = J[2*k+1, 2*k] = 1
    out = []
    for bits in itertools.product((0, 1), repeat=n*n):
        M = np.array(bits, dtype=int).reshape(n, n)
        if np.array_equal((M.T @ J @ M) % 2, J):
            out.append(M)
    return out

def run_corr(M, c, prep, schedule, m):
    """prep: list of 2m entries in {0,1,'u'}. schedule: list of 'R' or 'G'.
    Returns exact correlator between the two read records."""
    n = 2*m
    unk = [i for i, p in enumerate(prep) if p == 'u']
    nreads = schedule.count('R')
    tot = 0; cnt = 0
    for bits in itertools.product((0, 1), repeat=len(unk) + nreads):
        st = np.array([0 if p == 'u' else p for p in prep], dtype=int)
        for i, b in zip(unk, bits[:len(unk)]):
            st[i] = b
        kicks = list(bits[len(unk):])
        rec = []
        for op in schedule:
            if op == 'G':
                st = (M @ st + c) % 2
            else:
                rec.append(st[0])              # record z of the carrier
                st[1] = (st[1] + kicks.pop()) % 2  # independent uniform kick on x
        tot += (-1) ** ((rec[0] + rec[1]) % 2)
        cnt += 1
    return Fraction(tot, cnt)

def scan(m, preps):
    G = sp_group(m)
    n = 2*m
    trans = [np.array(t, dtype=int) for t in itertools.product((0, 1), repeat=n)]
    forms = [s for s in itertools.product((1, -1), repeat=3) if s[0]*s[1]*s[2] == -1]
    best = None
    corr_vals = set()
    for M in G:
        for c in trans:
            for prep in preps:
                C12 = run_corr(M, c, prep, ['R', 'G', 'R'], m)
                C23 = run_corr(M, c, prep, ['G', 'R', 'G', 'R'], m)
                C13 = run_corr(M, c, prep, ['R', 'G', 'G', 'R'], m)
                corr_vals |= {C12, C23, C13}
                K = max(s[0]*C12 + s[1]*C23 + s[2]*C13 for s in forms)
                if best is None or K > best[0]:
                    best = (K, M.tolist(), c.tolist(), prep, (C12, C23, C13))
    return len(G), sorted(corr_vals), best

def preps_for(m, kind):
    halves = [(0, 'u'), (1, 'u'), ('u', 0), ('u', 1)]
    env = [('u', 'u')]
    sharp = [(a, b) for a in (0, 1) for b in (0, 1)]
    carrier = halves  # Z+-, X+- (SA-1(c), H-PREP)
    if m == 1:
        return [list(cp) for cp in carrier]
    other = {'sa1c': halves + env, 'sharp': sharp}[kind]
    return [list(cp) + list(op) for cp in carrier for op in other]

if __name__ == '__main__':
    # Control: QM single-qubit pi/3 rotation value 3/2 (QX4 A4.6), exact rationals
    from fractions import Fraction as F
    cos = {1: F(1, 2), 2: F(-1, 2)}
    print('control: QM R60 n_perp_z K3 =', 2*cos[1] - cos[2])
    nz2 = F(1, 3)
    C = lambda c: nz2 + (1 - nz2)*c
    print('control: QM R60 body-diagonal K3 =', 2*C(cos[1]) - C(cos[2]))
    c35, c35_2 = F(3, 5), 2*F(3, 5)**2 - 1
    print('control: QM arccos(3/5) n_perp_z K3 =', 2*c35 - c35_2)
    nG, vals, best = scan(1, preps_for(1, None))
    print(f'm=1: |Sp(2,2)|={nG}; correlator values {[str(v) for v in vals]}; max K3 = {best[0]}')
    nG, vals, best = scan(2, preps_for(2, 'sa1c'))
    print(f'm=2 SA-1(c)/env preps: |Sp(4,2)|={nG}; correlator values {[str(v) for v in vals]}; '
          f'max K3 = {best[0]}; witness {best[1:]}')
    nG, vals, best = scan(2, preps_for(2, 'sharp'))
    print(f'm=2 sharp second mode: correlator values {[str(v) for v in vals]}; '
          f'max K3 = {best[0]}; witness {best[1:]}')
