"""EQ5-PREM q2 — the purity-factorization lemma behind "first-order independent preparation => full independent
preparation" (Part A, A1/A3): its exact ingredients, and countercontrols showing that purity and positivity are
load-bearing.  Research only; nothing here is adopted.

Usage:  python3 -I -B q2_purity.py <base>/verification/lean-mathlib/OIBridge

The lemma (written in RESULT §A1; this script checks its exact ingredients).  Let T be a normalized n-token table
(homogeneous indices 0..3 per token) that is nonnegative on every product g_1 (x) ... (x) g_n of effects of the 3-ball,
and whose single-token marginals x_1, ..., x_n are unit vectors.  Then T = hom x_1 (x) ... (x) hom x_n.
Proof route: for fixed effects on tokens 2..n, the token-1 conditional c_F(g) = T(g, F) is nonnegative on the effect cone
of the ball, the Lorentz cone Lor (EFF-1 lor_ehom, CD:930, and isEffectOn_affOf, CD:916), hence lies in Lor (self-dual);
c_F + c_{F'} telescopes to the marginal hom x_1, which spans an extreme ray of Lor when |x_1| = 1; so every c_F is a
multiple of hom x_1 and T factorizes in token 1; induct.  The two-token core of that step is checked below as
polynomial identities.

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription: the landed Lorentz cone `Lor v := 0 <= v 0 /\ sum_j v (j+1)^2 <= v 0^2` (CD:869) and the effect-cone
    lemmas lor_ehom (CD:930) and isEffectOn_affOf (CD:916) are present with these statements.
 L1 two-token core, T = hom z (x) hom y + C with C supported on indices a, b >= 1 (symbolic z, y, C, f), reduced modulo
    z.z = 1:  (i) T(g_z, u) = 0 for g_z = (1/2, -z/2); (ii) T(g_z, f) = -(1/2) z^T C fvec; (iii) the token-1 conditional
    c_f = (T(e_mu, f))_mu equals (f(y), z f(y) + C fvec); (iv) |cvec_f|^2 - c_f0^2 = 2 f(y) z^T C fvec + |C fvec|^2.
 L2 the extreme-ray identity used for |x| = 1: for a = (alpha, v) and b = (1 - alpha, x - v),
    (alpha^2 - |v|^2) + ((1 - alpha)^2 - |x - v|^2) = -2 (alpha (1 - alpha) - v.(x - v))  modulo x.x = 1 (symbolic).
 L3 the token-1 factorization step: for T = hom x (x) T' (symbolic 2-token T', 3 tokens in all) and product effects,
    T(g, f, f') = g(x) T'(f, f') (symbolic).
 L4 spanning: the homogenized vectors of the four rational unit vectors e_x, e_y, e_z, -e_z are linearly independent
    (exact determinant nonzero), so their four-fold products form a basis of W4 (Kronecker products of a basis).
 CC1 purity is load-bearing: T_cl = (hom z (x) hom z + hom(-z) (x) hom(-z))/2 satisfies T_cl(g, f) =
    (g(z) f(z) + g(-z) f(-z))/2 (symbolic, so it is nonnegative on product effects), its marginals are 0, and it differs
    from hom 0 (x) hom 0.
 CC2 positivity is load-bearing: T = hom z (x) hom z + (1/2) E_xx has the pure marginals z, z, and the explicit product
    effect g = (1, (3/5, 0, -4/5))/2, f = (1, (-1, 0, 0))/2 gives T(g, f) < 0 (exact).
 VERDICT Q2-PURITY-LEMMA-INGREDIENTS-EXACT iff K, L1-L4, CC1, CC2 all pass; otherwise VERDICT NOT RENDERED.
 LEADS (printed after the verdict; they certify nothing and do not affect it): for each STMC-respecting twist Psi of W4
    in the list, the A-table Psi(hom x_0 (x) ... (x) hom x_3) at an axis-aligned pure product has pure marginals and
    differs from the product, so the lemma predicts a negative product-effect value; an exact search over products of the
    seven axis effects {u, (1 +- e_i)/2} reports the minimum value and a witness.
 Exact arithmetic only (sympy rationals and symbols; Fractions in the search).  No timing in stdout.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

import sympy as sp

LEAN = sys.argv[1]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


R4 = range(4)
CD = read(os.path.join(LEAN, "CompositeDimension.lean")).split("\n")
k_ok = (CD[868].strip() == "def Lor (v : HVec d) : Prop := 0 ≤ v 0 ∧ ∑ j : Fin d, v j.succ ^ 2 ≤ v 0 ^ 2"
        and CD[929].strip().startswith("theorem lor_ehom {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) : Lor (ehom e)")
        and CD[915].strip().startswith("theorem isEffectOn_affOf {v : HVec d} (hv : Lor v) (hv0 : v 0 ≤ 1 / 2) :"))
check("K the Lorentz cone Lor (CD:869) and the effect-cone lemmas lor_ehom (CD:930), isEffectOn_affOf (CD:916) present",
      k_ok)

# ------------------------------------------------------------------ L1 two-token core
z = sp.symbols("z1:4")
y = sp.symbols("y1:4")
C = sp.Matrix(3, 3, lambda i, j: sp.Symbol("C%d%d" % (i + 1, j + 1)))
f0 = sp.Symbol("f0")
fv = sp.Matrix(sp.symbols("fx fy fz"))
zv = sp.Matrix(z)
yv = sp.Matrix(y)
hz = [1] + list(z)
hy = [1] + list(y)
T = [[hz[m] * hy[n] + (C[m - 1, n - 1] if m >= 1 and n >= 1 else 0) for n in R4] for m in R4]
NORM = z[0] ** 2 + z[1] ** 2 + z[2] ** 2 - 1


def red(e):
    """reduce a polynomial modulo z.z = 1 (substitute z3^2 = 1 - z1^2 - z2^2 repeatedly)"""
    e = sp.expand(e)
    return sp.expand(sp.rem(sp.Poly(e, z[2]), sp.Poly(NORM, z[2])).as_expr()) if e.has(z[2]) else e


def pair(g, f, T_):
    return sp.expand(sum(g[m] * f[n] * T_[m][n] for m in R4 for n in R4))


fhat = [f0] + list(fv)
u = [1, 0, 0, 0]
gz = [sp.Rational(1, 2)] + [-zi / 2 for zi in z]
fy = f0 + (fv.T * yv)[0]
i_ok = red(pair(gz, u, T)) == 0
ii_ok = red(pair(gz, fhat, T) + sp.Rational(1, 2) * ((zv.T * C * fv)[0])) == 0
cf = [pair([1 if k == mu else 0 for k in R4], fhat, T) for mu in R4]
iii_ok = (sp.expand(cf[0] - fy) == 0
          and all(sp.expand(cf[k + 1] - (z[k] * fy + (C * fv)[k])) == 0 for k in range(3)))
lhs = sum(cf[k + 1] ** 2 for k in range(3)) - cf[0] ** 2
rhs = 2 * fy * (zv.T * C * fv)[0] + sum(((C * fv)[k]) ** 2 for k in range(3))
iv_ok = red(lhs - rhs) == 0
check("L1 two-token core modulo z.z = 1: (i) T(g_z, u) = 0; (ii) T(g_z, f) = -(1/2) z^T C f; (iii) c_f = (f(y), z f(y) "
      "+ C f); (iv) |cvec_f|^2 - c_f0^2 = 2 f(y) z^T C f + |C f|^2 (symbolic)", i_ok and ii_ok and iii_ok and iv_ok,
      "(i) %s, (ii) %s, (iii) %s, (iv) %s" % (i_ok, ii_ok, iii_ok, iv_ok))

# ------------------------------------------------------------------ L2 extreme-ray identity
al = sp.Symbol("alpha")
v = sp.symbols("v1:4")
x = z                         # reuse z as the unit vector x
q1 = al ** 2 - sum(vi ** 2 for vi in v)
q2 = (1 - al) ** 2 - sum((x[i] - v[i]) ** 2 for i in range(3))
target = -2 * (al * (1 - al) - sum(v[i] * (x[i] - v[i]) for i in range(3)))
check("L2 extreme-ray identity: (alpha^2 - |v|^2) + ((1 - alpha)^2 - |x - v|^2) = -2(alpha(1 - alpha) - v.(x - v)) "
      "modulo x.x = 1 (symbolic)", red(q1 + q2 - target) == 0)

# ------------------------------------------------------------------ L3 factorization step
w = sp.symbols("w1:4")
Tp = [[sp.Symbol("P%d%d" % (b, c)) for c in R4] for b in R4]
hx = [1] + list(w)
T3 = {(a, b, c): hx[a] * Tp[b][c] for a in R4 for b in R4 for c in R4}
gs = [sp.Symbol("g%d" % k) for k in R4]
f1 = [sp.Symbol("p%d" % k) for k in R4]
f2 = [sp.Symbol("q%d" % k) for k in R4]
val3 = sp.expand(sum(gs[a] * f1[b] * f2[c] * T3[(a, b, c)] for a in R4 for b in R4 for c in R4))
gx = sum(gs[a] * hx[a] for a in R4)
tp = sum(f1[b] * f2[c] * Tp[b][c] for b in R4 for c in R4)
check("L3 factorization step: for T = hom x (x) T', T(g, f, f') = g(x) T'(f, f') (symbolic)",
      sp.expand(val3 - gx * tp) == 0)

# ------------------------------------------------------------------ L4 spanning
S = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, -1]]
d = sp.Matrix(S).det()
check("L4 the homogenized e_x, e_y, e_z, -e_z are linearly independent (det != 0); their four-fold products form a "
      "basis of W4", d != 0, "det = %s" % d)

# ------------------------------------------------------------------ CC1 purity load-bearing
zz = [0, 0, 1]
hz_ = [1, 0, 0, 1]
hmz = [1, 0, 0, -1]
Tcl = [[sp.Rational(1, 2) * (hz_[m] * hz_[n] + hmz[m] * hmz[n]) for n in R4] for m in R4]
gsym = sp.symbols("a0:4")
fsym = sp.symbols("b0:4")
gzv = sum(gsym[k] * hz_[k] for k in R4)
gmz = sum(gsym[k] * hmz[k] for k in R4)
fzv = sum(fsym[k] * hz_[k] for k in R4)
fmz = sum(fsym[k] * hmz[k] for k in R4)
cc1 = (sp.expand(pair(gsym, fsym, Tcl) - sp.Rational(1, 2) * (gzv * fzv + gmz * fmz)) == 0
       and all(Tcl[k][0] == 0 and Tcl[0][k] == 0 for k in (1, 2, 3)) and Tcl[3][3] != 0)
check("CC1 purity load-bearing: T_cl(g, f) = (g(z)f(z) + g(-z)f(-z))/2 (nonnegative on product effects), marginals 0, "
      "and T_cl != hom 0 (x) hom 0 (its zz entry is %s)" % Tcl[3][3], cc1)

# ------------------------------------------------------------------ CC2 positivity load-bearing
Tq = [[hz_[m] * hz_[n] for n in R4] for m in R4]
Tq[1][1] = Tq[1][1] + sp.Rational(1, 2)
g = [sp.Rational(1, 2), sp.Rational(3, 10), 0, sp.Rational(-2, 5)]
f = [sp.Rational(1, 2), sp.Rational(-1, 2), 0, 0]
val = pair(g, f, Tq)
pure_marg = [Tq[k][0] for k in R4] == [1, 0, 0, 1] and [Tq[0][k] for k in R4] == [1, 0, 0, 1]
lor_ok = all(h[0] >= 0 and sum(h[k] ** 2 for k in (1, 2, 3)) <= h[0] ** 2 and h[0] <= sp.Rational(1, 2) for h in (g, f))
check("CC2 positivity load-bearing: T = hom z (x) hom z + E_xx/2 has pure marginals (z, z); g = (1,(3/5,0,-4/5))/2 and "
      "f = (1,(-1,0,0))/2 are effects (Lor, head 1/2); T(g, f) < 0", pure_marg and lor_ok and val < 0, "T(g, f) = %s" % val)

check("F no float in the checked quantities", not any(isinstance(q, float) for q in (val, d)))

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- q2_purity: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q2-PURITY-LEMMA-INGREDIENTS-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")

# ================================================================== LEADS (certify nothing; outside the verdict)
I4 = list(itertools.product(R4, R4, R4, R4))
SG = [1, 1, -1, 1]


def psi_mf(Z):
    return {I: (SG[I[3]] * Z[I] if I[:3] != (0, 0, 0) else Z[I]) for I in I4}


def psi_4(Z):
    return {I: (-Z[I] if all(k != 0 for k in I) else Z[I]) for I in I4}


def psi_2(Z):
    return {I: (-Z[I] if (I[0] != 0 and I[1] != 0 and I[2] == 0 and I[3] == 0) else Z[I]) for I in I4}


def psi_half(Z):
    return {I: (Fr(1, 2) * Z[I] if sum(1 for k in I if k != 0) >= 2 else Z[I]) for I in I4}


TW = [("Psi_mf (e1's twist)", psi_mf), ("Psi_4 (sign of 4-body entries)", psi_4),
      ("Psi_2 (sign of 01 correlations)", psi_2), ("Psi_half (correlations halved)", psi_half)]
AX = [[Fr(1), Fr(0), Fr(0), Fr(0)]] + [[Fr(1, 2)] + [Fr(s, 2) if k == i else Fr(0) for k in range(3)]
                                        for i in range(3) for s in (1, -1)]
pure = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
H = {I: Fr(1) for I in I4}
for I in I4:
    p = Fr(1)
    for t in R4:
        p *= ([1] + pure[t])[I[t]]
    H[I] = p
for name, F in TW:
    Tt = F(H)
    single_ok = all(Tt[I] == H[I] for I in I4 if sum(1 for k in I if k != 0) <= 1)
    differs = any(Tt[I] != H[I] for I in I4)
    best = None
    for gi in itertools.product(range(7), repeat=4):
        gg = [AX[k] for k in gi]
        vv = sum(gg[0][a] * gg[1][b] * gg[2][c] * gg[3][dd] * Tt[(a, b, c, dd)] for a, b, c, dd in I4 if Tt[(a, b, c, dd)] != 0)
        if best is None or vv < best[0]:
            best = (vv, gi)
    print("LEAD %s: preserves single-token entries %s, differs from the product %s, minimum over axis effects %s at %s -> %s"
          % (name, single_ok, differs, best[0], best[1],
             "WITNESS-FOUND" if best[0] < 0 else "NO-WITNESS-IN-GRID"))
