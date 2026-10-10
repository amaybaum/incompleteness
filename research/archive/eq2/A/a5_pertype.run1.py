"""EQ2-A probe A5 -- the stricter per-type theorem, exact.  Research only; base bcbc516f.
Usage: python3 -I -B a5_pertype.py <CompositeDimension.lean> <K2Guard.lean>

Setting: n tokens of ONE type, pair composites in {Q, Tw} with native twist bits tau_ij (relative to the given
copy identification).  A per-token chart eps in {I, R}^n presents pair (i,j) iff [eps_i != eps_j] = tau_ij; a
type-uniform chart is eps constant.  (The SO(3) parts of a chart are automorphisms of Q and Tw and are dropped.)

DECISION RULE (fixed before the first run): verdict `A5-PERTYPE-EXACT` iff every check passes:
  E1  uniform charts never change a twist bit: chart2 e e maps the Bell table of Q to phiW and of Tw to idW, for
      e in {I, R}; per-token (I, R) and (R, I) exchange them              (exact)
  E2  enumeration, n = 3 and 4: a per-token chart presenting every pair exists iff tau is a coboundary
      (4 of 8; 8 of 64); a uniform chart exists iff tau = 0 (1 of 8; 1 of 64)
  E3  EX-symmetric assignments tau = c (constant): per-token chart iff c = 0 (n = 3, 4); the all-twisted
      assignment (c = 1) is S_n-symmetric and has no chart -- EX alone does not force presentability at n >= 3
  E4  the twin (n = 2, tau = 1) is per-token presentable, not uniformly presentable, and SWAP-invariant (EX holds)
  E5  parity rule (Theorem C, written) + uniform composition (tau = c) on a triangle forces c = 0:
      c = c XOR c has the unique solution c = 0 (checked by enumeration), so uniform composition + IE2 gives tau = 0
  E6  M_tw: the transposition (0 1) acting on symbolic generator tables permutes the three generator families
      (with swapW on the (0,1) family, which preserves Tw by E4), so the exchange's idle extension preserves the
      all-twisted hull -- "EX + IE2 for the exchange only" does not force tau = 0
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import Matrix  # noqa: E402

import eq2a_lib as L  # noqa: E402

cd_path, k2_path = sys.argv[1], sys.argv[2]
check = L.check
idW, _, _ = L.parse_k2guard_tables(k2_path)
phiW = L.parse_phiW(cd_path)
RY, ID = L.REFLY, L.ID3
Wsym = Matrix(4, 4, lambda m, n: sp.Symbol(f"w{m}{n}", real=True))


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


bell = {0: phiW, 1: L.actT(RY, phiW)}
check("E1 the Bell table of Tw is idW (= actT reflY phiW)", bell[1] == idW)
ok = True
for e in (ID, RY):
    ok = ok and L.chart2(e, e, bell[0]) == phiW and L.chart2(e, e, bell[1]) == idW
check("E1 uniform charts chart2 e e (e in {I, R}) send phiW -> phiW and idW -> idW: twist bits unchanged", ok)
check("E1 per-token (I,R) and (R,I) exchange phiW and idW",
      L.chart2(ID, RY, phiW) == idW and L.chart2(RY, ID, phiW) == idW and
      L.chart2(ID, RY, idW) == phiW and L.chart2(RY, ID, idW) == phiW)
check("E1 the global transpose chart2 R R fixes Q's and Tw's Bell tables and commutes with actT reflY (symbolic)",
      zero(L.chart2(RY, RY, L.actT(RY, Wsym)) - L.actT(RY, L.chart2(RY, RY, Wsym))))


def presentable(n, tau, uniform=False):
    pairs = list(itertools.combinations(range(n), 2))
    epss = [(c,) * n for c in (0, 1)] if uniform else itertools.product((0, 1), repeat=n)
    return any(all((eps[i] != eps[j]) == bool(tau[p]) for p, (i, j) in enumerate(pairs)) for eps in epss)


for n in (3, 4):
    pairs = list(itertools.combinations(range(n), 2))
    taus = list(itertools.product((0, 1), repeat=len(pairs)))
    cob = {tuple((eps[i] + eps[j]) % 2 for (i, j) in pairs) for eps in itertools.product((0, 1), repeat=n)}
    per = [t for t in taus if presentable(n, t)]
    uni = [t for t in taus if presentable(n, t, uniform=True)]
    check(f"E2 n = {n}: per-token chart exists iff tau is a coboundary ({len(per)} of {len(taus)})",
          set(per) == cob and len(per) == 2 ** (n - 1))
    check(f"E2 n = {n}: uniform chart exists iff tau = 0 ({len(uni)} of {len(taus)})",
          uni == [tuple([0] * len(pairs))])
    const = [tuple([c] * len(pairs)) for c in (0, 1)]
    check(f"E3 n = {n}: EX-symmetric tau = c has a per-token chart iff c = 0",
          presentable(n, const[0]) and not presentable(n, const[1]))
check("E4 the twin (n = 2, tau = 1): per-token presentable, not uniformly presentable",
      presentable(2, (1,)) and not presentable(2, (1,), uniform=True))
check("E4 the twin is SWAP-invariant: swapW . actT reflY = transposeW . actT reflY . swapW and transposeW fixes Q "
      "(symbolic; A1.13)", zero(L.swapW(L.actT(RY, Wsym)) - L.transposeW(L.actT(RY, L.swapW(Wsym)))))
check("E5 on a triangle, parity tau_02 = tau_01 XOR tau_12 with tau = c constant forces c = 0",
      [c for c in (0, 1) if c == (c ^ c)] == [0])
# E6: the copy transposition (0 1) applied to symbolic generators of M_tw.  Tables are permuted by
# T'[i0, i1, i2] = T[i1, i0, i2].  Type (0,1): sigma (x) z  ->  (swapW sigma) (x) z, and swapW sigma lies in Tw by the
# E4 identity; type (0,2): sigma on (0,2) (x) y  ->  sigma on (1,2) (x) y on copy 0 (same sigma); type (1,2) -> (0,2).
def gen3(sig, pair, z):
    i, j = pair
    k = [c for c in range(3) if c not in pair][0]
    hz = L.hom(z)
    return {idx: sig[idx[i], idx[j]] * hz[idx[k]] for idx in itertools.product(range(4), repeat=3)}


def perm01(T):
    return {(i0, i1, i2): T[(i1, i0, i2)] for (i0, i1, i2) in T}


def teq(A, B):
    return all(sp.expand(A[k] - B[k]) == 0 for k in A)


Ssym = L.actT(RY, Matrix(4, 4, lambda m, n: sp.Symbol(f"s{m}{n}", real=True)))   # a generic element of R_B(span Q)
zs = sp.symbols("z0:3", real=True)
check("E6 (0 1) maps sigma on (0,1) (x) z to (swapW sigma) on (0,1) (x) z (symbolic)",
      teq(perm01(gen3(Ssym, (0, 1), zs)), gen3(L.swapW(Ssym), (0, 1), zs)))
check("E6 (0 1) maps sigma on (0,2) (x) y to sigma on (1,2) (x) y and back (symbolic)",
      teq(perm01(gen3(Ssym, (0, 2), zs)), gen3(Ssym, (1, 2), zs)) and
      teq(perm01(gen3(Ssym, (1, 2), zs)), gen3(Ssym, (0, 2), zs)))
check("E6 swapW maps the twisted Bell table idW to itself and actT reflY (Q-element) into transposeW . actT reflY",
      L.swapW(idW) == idW)

ok = L.summary("a5_pertype")
print("VERDICT " + ("A5-PERTYPE-EXACT" if ok else "A5-NOT-RENDERED"))
sys.exit(0 if ok else 1)
