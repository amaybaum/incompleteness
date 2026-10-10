"""EQ4-P probe p9 -- N4 candidate "purification" (pure = extreme ray): exact ingredients.  Research only.

Usage:  python3 -I -B p9_purification.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py (and sympy for small symbolic identities).

Support lemma (written, NOTES N4): if w is in BS* (three tokens) and tr_3 w = D/2 with D = |00><00| + |11><11|, then w
is supported on E = L (x) C^2, L = span{|00>, |11>}, and w restricted to E is PSD.  Proof: (a) |0>_1 (x) |1 phi>_23
is a product across 1|23, so <01 phi|w|01 phi> >= 0, and these sum to <01|tr_3 w|01> = 0 over a basis, so each
vanishes, for every phi; likewise |10 phi>.  (b) Block positivity across 2|13 (token-2 vector |1>) and across 1|23
(token-1 vector |0>) make the operators <1|_2 w |1>_2 and <0|_1 w |0>_1 PSD, so their rows through the zero diagonal
entries vanish; block positivity across 3|12 gives <01 chi|w|10 chi> = 0 for every chi, and polarization of the
sesquilinear form (phi, psi) -> <01 phi|w|10 psi> gives 0 for all phi, psi.  So every row and column through |01 .>,
|10 .> vanishes.  (c) For v = |00>|u> + |11>|w> in E, (|0>+|1>)_1 (x) (|0>|u> + |1>|w>)_23 = v + |01 w> + |10 u>, a
product across 1|23, so <v|w|v> >= 0.  Hence non-PSD elements cannot purify D/2 within one extra token.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P9-PURIFICATION-EXACT` iff all pass:
  K  transcription control.
  S  (S1) polarization identity B(x, y) = (1/4) sum_k i^(-k) B(x + i^k y, x + i^k y) for a symbolic sesquilinear form
     on C^2 (symbolic); (S2) the vector identity of step (c) (symbolic u, w); (S3) for psi = |00>|u> + |11>|w>:
     tr_3 |psi><psi| has entries |u|^2, |w|^2, <w|u> (symbolic) and Det(psi) = (u0 w1 - u1 w0)^2 (symbolic), so a
     rank-one purification of D/2 within one token (|u| = |w|, u orthogonal to w) is GHZ-class; (S4) instances: GHZ and
     omega_p = p GHZ + (1 - p)(D/2 (x) 1/2) for p = 1/2 have marginal D/2 and are supported on E and PSD there
     (exact); countercontrol: W3 (in BS*, marginal not proportional to D) has nonzero entries outside E.
  R  the residual case is not empty as a set of operators: omega_p (p = 1/2) is PSD, rank 4 on E, marginal D/2, not
     biseparable (tr(W3 omega_p) < 0), and NPT across the effective cut L|3 (its partial transpose on token 3 has a
     negative eigenvalue: exact vector check).
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p9_purification")
rng = random.Random(20261009 + 9)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])

# S1 polarization
m = sp.symbols("m0:8", real=True)
Mm = sp.Matrix(2, 2, lambda i, j: m[2 * (2 * i + j)] + sp.I * m[2 * (2 * i + j) + 1])
xs = sp.symbols("x0:4", real=True)
ys = sp.symbols("y0:4", real=True)
xv = sp.Matrix([xs[0] + sp.I * xs[1], xs[2] + sp.I * xs[3]])
yv = sp.Matrix([ys[0] + sp.I * ys[1], ys[2] + sp.I * ys[3]])
Bf = lambda a, b: (a.H * Mm * b)[0, 0]
pol = sum(sp.I ** (-k) * Bf(xv + sp.I ** k * yv, xv + sp.I ** k * yv) for k in range(4)) / 4
rep.check("S1 polarization: B(x, y) = (1/4) sum_k i^(-k) B(x + i^k y, x + i^k y) (symbolic)",
          sp.expand(pol - Bf(xv, yv)) == 0)
# S2 vector identity (order of tokens 1,2,3; index 4 t1 + 2 t2 + t3)
u = sp.symbols("u0:2")
w = sp.symbols("w0:2")
left = [0] * 8
a = [1, 1]
chi = [u[0], u[1], w[0], w[1]]          # |0>|u> + |1>|w> on tokens 2,3
for t1 in range(2):
    for k in range(4):
        left[4 * t1 + k] += a[t1] * chi[k]
v_E = [0] * 8
v_E[0], v_E[1], v_E[6], v_E[7] = u[0], u[1], w[0], w[1]           # |00u> + |11w>
extra = [0] * 8
extra[2], extra[3], extra[4], extra[5] = w[0], w[1], u[0], u[1]   # |01w> + |10u>
rep.check("S2 (|0>+|1>)(|0>|u> + |1>|w>) = |00u> + |11w> + |01w> + |10u> (symbolic)",
          all(sp.expand(left[i] - v_E[i] - extra[i]) == 0 for i in range(8)))
# S3 marginal and hyperdeterminant of psi = |00u> + |11w>
ur = sp.symbols("ur0:2", real=True)
ui = sp.symbols("ui0:2", real=True)
wr = sp.symbols("wr0:2", real=True)
wi = sp.symbols("wi0:2", real=True)
uu = [ur[k] + sp.I * ui[k] for k in range(2)]
ww = [wr[k] + sp.I * wi[k] for k in range(2)]
psi = sp.Matrix([uu[0], uu[1], 0, 0, 0, 0, ww[0], ww[1]])
rho = psi * psi.H
marg = sp.zeros(4, 4)
for r in range(8):
    for c in range(8):
        if (r & 1) == (c & 1):
            marg[r >> 1, c >> 1] += rho[r, c]
expect = sp.zeros(4, 4)
expect[0, 0] = sum(sp.expand(z * sp.conjugate(z)) for z in uu)
expect[3, 3] = sum(sp.expand(z * sp.conjugate(z)) for z in ww)
expect[0, 3] = sum(sp.expand(uu[k] * sp.conjugate(ww[k])) for k in range(2))
expect[3, 0] = sp.conjugate(expect[0, 3])
aa = lambda i, j, k: psi[4 * i + 2 * j + k]
Det = sp.expand(aa(0, 0, 0) ** 2 * aa(1, 1, 1) ** 2 + aa(0, 0, 1) ** 2 * aa(1, 1, 0) ** 2
                - 2 * aa(0, 0, 0) * aa(1, 1, 1) * aa(0, 0, 1) * aa(1, 1, 0))
# full Cayley formula specialised: only a000, a001, a110, a111 can be nonzero
rep.check("S3 tr_3|psi><psi| = |u|^2 |00><00| + |w|^2 |11><11| + (<w|u>|00><11| + h.c.) and Det(psi) = (u0 w1 - u1 w0)^2 "
          "(symbolic; the other Cayley terms vanish on psi)",
          (marg - expect).applyfunc(sp.expand).is_zero_matrix
          and sp.expand(Det - (uu[0] * ww[1] - uu[1] * ww[0]) ** 2) == 0
          and L.hyperdet([1, 2, 0, 0, 0, 0, 3, 5]) == L.G((1 * 5 - 2 * 3) ** 2))
# S4 instances
X3 = (0, 1, 2)
D = L.ket_op([1, 0, 0, 0], (0, 1)) + L.ket_op([0, 0, 0, 1], (0, 1))
GH = L.ghz(X3)
Ehalf = L.tensor(D.scale(Fr(1, 2)), L.identity((2,)).scale(Fr(1, 2)))
omega = GH.scale(Fr(1, 2)) + Ehalf.scale(Fr(1, 2))
Eidx = {0, 1, 6, 7}


def supported_on_E(Op_):
    return all(r in Eidx and c in Eidx for (r, c) in Op_.d)


def restrict_E(Op_):
    idx = sorted(Eidx)
    return L.op([[Op_.get(r, c) for c in idx] for r in idx], (90, 91))


ok_s4 = True
for Om in (GH, omega):
    ok_s4 &= L.ptrace(Om, (0, 1)) == D.scale(Fr(1, 2)) and supported_on_E(Om) and L.psd(restrict_E(Om))[0]
W3 = L.w3(X3)
ok_s4 &= not supported_on_E(W3)
rep.check("S4 GHZ and omega_1/2 have marginal D/2, are supported on E and PSD there; countercontrol: W3 has entries "
          "outside E", ok_s4)
# R residual case
psd_om, _ = L.psd(omega)
rank_ok = True
# rank on E: restrict and check the 4x4 matrix is nonsingular (exact determinant via elimination pivots)
RE = restrict_E(omega)
Md = [[RE.get(r, c) for c in range(4)] for r in range(4)]


def det4(M):
    M = [row[:] for row in M]
    n = len(M)
    det = L.ONE
    for i in range(n):
        piv = next((r for r in range(i, n) if not M[r][i].is_zero()), None)
        if piv is None:
            return L.ZERO
        if piv != i:
            M[i], M[piv] = M[piv], M[i]
            det = -det
        det = det * M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [M[r][j] - f * M[i][j] for j in range(n)]
    return det


rank4 = not det4(Md).is_zero()
fid = L.pair(W3, omega)
# NPT across L|3: PT on token 2 (the third token) and a negative direction: v = |00>|1> - |11>|0>  (indices 1, 6)
PTo = L.ptranspose(omega, [2])
vneg = [0] * 8
vneg[1], vneg[6] = 1, -1
val_neg = L.pair(PTo, L.ket_op(vneg, X3))
rep.check("R omega_1/2 is PSD, rank 4 on E, marginal D/2, not biseparable (tr(W3 omega) = %s < 0), NPT across L|3 "
          "(<v|PT_3(omega)|v> = %s < 0)" % (fid, val_neg),
          psd_om and rank4 and fid.re < 0 and val_neg.re < 0)

rep.verdict("P9-PURIFICATION-EXACT")
