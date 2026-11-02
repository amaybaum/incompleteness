"""Explicit countermodel family (time-homogeneous, counting measure): maximal-period LFSR bijections.

V = GF(2), H = GF(2)^m, d = m+1. State z = (s_t, ..., s_{t+d-1}); phi shifts and appends
s_{t+d} = sum_i c_i s_{t+i} for a primitive feedback polynomial of degree d. Visible x = s_t.
Uniform prior on V x H. Verified exactly for m = 1..4 (L = 2^d - 1 = 3, 7, 15, 31):
  bijection; order L; Gamma_t = J/2 for 1 <= t <= L-1, Gamma_L = I;
  no gap at orders < m; a gap with delta = 1 at every order m..L-2 (window {0..L-1});
  P-divisible on {0..L-1} (exact LP, every pair), not P-divisible on {0..L} (C-rec).
"""
import importlib.util, sys, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

# s_{t+d} = sum_{i in taps} s_{t+i}  (primitive: x^2+x+1, x^3+x+1, x^4+x+1, x^5+x^2+1)
TAPS = {2: (0, 1), 3: (0, 1), 4: (0, 1), 5: (0, 2)}
green = True
for m in (1, 2, 3, 4):
    d = m + 1
    taps = TAPS[d]
    nV, nH = 2, 2 ** m
    N = nV * nH
    def enc(bits):  # bits[0] visible, bits[1:] hidden
        x = bits[0]; h = 0
        for i, b in enumerate(bits[1:]):
            h |= b << i
        return x * nH + h
    def dec(z):
        x, h = divmod(z, nH)
        return [x] + [(h >> i) & 1 for i in range(m)]
    perm = [0] * N
    for z in range(N):
        s = dec(z)
        new = sum(s[i] for i in taps) % 2
        perm[z] = enc(s[1:] + [new])
    bij = sorted(perm) == list(range(N))
    Lo = L.perm_order(perm)
    G = L.rooted_family(perm, nV, nH, Lo)
    J2 = [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]]
    I2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    rank_one = all(G[t] == J2 for t in range(1, Lo)) and G[Lo] == I2
    P = L.law_from_trajs(L.trajectories(perm, nV, nH, Lo))
    gaps = {k: L.gap_at(P, k, nV)[:2] for k in range(1, Lo - 1)}
    no_early = all(not gaps[k][0] for k in range(1, m))
    full_late = all(gaps[k][0] and gaps[k][1] == 1 for k in range(m, Lo - 1))
    div_ok, bad = L.p_divisible_window(G, Lo - 1, closed_form_check=True)
    indiv_L, badL = L.p_divisible_window(G, Lo)
    ok = bij and Lo == 2 ** d - 1 and rank_one and no_early and full_late and div_ok and not indiv_L
    green &= ok
    print(f'm={m}: |S|={N} bijection={bij} L={Lo} Gamma_t=J/2 (1<=t<L), Gamma_L=I: {rank_one}; '
          f'no gap below order {m}: {no_early}; delta=1 gap at every order {m}..{Lo-2}: {full_late}; '
          f'P-divisible on {{0..{Lo-1}}}: {div_ok}; P-divisible on {{0..{Lo}}}: {indiv_L} (first failing pair {badL}) -> {"OK" if ok else "FAIL"}')
    if m == 1:
        print('   m=1 permutation (index x*nH+h):', perm)
print('LFSR FAMILY', 'ALL VERIFIED' if green else 'FAILED')
