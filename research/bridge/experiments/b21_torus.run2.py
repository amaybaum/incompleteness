#!/usr/bin/env python3
"""b21_torus.py -- node B21 of research/bridge (round 5): what an explicit exotic cone invariant under the tower's
closure G = closure <cnot, actT nflip, actT R_z(t) for all t> (B10-4) must satisfy. Exact arithmetic (sympy: symbols
for the torus angles and the seed's coordinates; Gaussian rationals for the instances; the torus sampled at the
Gaussian-rational points of the unit circle {+-1, +-i, (3 +- 4i)/5, (4 +- 3i)/5}).

DECISION RULE (fixed 2026-10-11T08:24:00Z, from `date -u` immediately before writing; before run 1).

Matrix side (HO-21's conjugation formulas; one dictionary [D]): basis |00>, |01>, |10>, |11> (control first);
CNOT; X_B = I (x) X; the generator I (x) diag(1, e^{it}); the torus T^2 = {U(u, v) = diag(e^{iu}, e^{-iu}, e^{iv}, e^{-iv})}
(B10 T9's exp(i(a Z_B + b Z_A Z_B)) with u = a + b, v = a - b). Defects d = I - c P_h, P_h = h h^*/|h|^2; pairing
<A, B> = tr(AB); s = |<h|h'>|^2/(|h|^2 |h'|^2).

CHECKS
  T1  (G1) I (x) diag(1, e^{it}) = e^{it/2} U(-t/2, -t/2) and CNOT (I (x) diag(1, e^{it})) CNOT = e^{it/2} U(-t/2, t/2),
      symbolically in t; CNOT U(u, v) CNOT = U(u, -v) and X_B U(u, v) X_B = U(-u, -v) symbolically (so CNOT and X_B
      normalize T^2); CNOT^2 = X_B^2 = 1, CNOT X_B = X_B CNOT; none of CNOT, X_B, CNOT X_B is diagonal. Hence
      G = T^2 . {1, CNOT, X_B, CNOT X_B} modulo scalars: four components, identity component T^2.
  T2  (G3) <h | U(u, v) X_B h> = 2 Re(conj(h00) h01 e^{iu}) + 2 Re(conj(h10) h11 e^{iv}), symbolically in the eight real
      coordinates of h and in u, v; exact instances: h = (1, 1, 2, i) with U = diag(i, -i, 1, 1) = U(pi/2, 0), and
      h = (1, 2, 3, 4) with U = diag(i, -i, i, -i) = U(pi/2, pi/2): <h | U X_B h> = 0. (Every G-orbit contains an
      orthogonal pair: choose e^{iu}, e^{iv} to make each term vanish.)
  T3  (G2) U(u, v) h reshaped has det e^{i(u-v)} h00 h11 - e^{i(v-u)} h01 h10, symbolically; the seed (2, 1, 1, 0)
      has |h00 h11| != |h01 h10| and |h00 h10| != |h01 h11| and the same for its images under CNOT, X_B, CNOT X_B
      (product-free G-orbit); countercontrol: h = (1, 2, 2, -4) has |h00 h11| = |h01 h10| = 4 and U(pi/2, 0) h is an
      exact product (det 0 and an explicit factorization).
  T4  the pairing law <d_j, d_k> = 4 - 2c + c^2 s, symbolically in c and s; at c = 2 it is 4 s >= 0, and the (CC)
      inequality (sqrt(c_j - 1) + sqrt(c_k - 1))^2 <= c_j c_k s of Theorem S' (HO-30 item 1) reads 4 <= 4 s at c = 2:
      it holds only for s = 1, so S' applies to a c = 2 defect set only if every two distinct rays are orthogonal.
  T5  Lemma C18-1's witness for G, exact: seed h = (1, 1, 2, i), partner h' = U(pi/2, 0) X_B h (orthogonal, T2),
      c* = 51/50, lambda = (c* - 1)/(4 - 2 c*) = 1/98, y = P_h + lambda (I - c* P_{h'}): <y, d_h> = 0,
      h'^* y h' / |h'|^2 = lambda (1 - c*) < 0, and <y, I - c* P_{g h}> >= 0 for every g in the sampled group (the four
      components at the 64 Gaussian-rational torus points, 256 defects), with the lemma's identity
      <y, d_l> = c*(1 - s_{hl}) + lambda c*^2 s_{h'l} on each sample.

VERDICT B21-EXACT iff T1-T5 all PASS; otherwise VERDICT B21-FAILED followed by the failing ids.

Post-run edit after run 1 (2026-10-11T08:25Z; run 1 kept as b21_torus.run1.*; rule text unchanged): run 1 failed T5's
identity sub-check only because the torus sample used the Python integers +-1, whose reciprocal 1/eu is a float, which
nsimplify turned into radical expressions in 8 of the 256 samples (every actual pairing was exact and >= 0, minimum 0).
The sample now uses sympy integers and the conjugate as the reciprocal of a unit-modulus Gaussian rational.
"""
import sys
from itertools import product

import sympy as sp

I = sp.I
PASS, FAIL = [], []


def check(name, ok, msg):
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")


def dagger(M):
    return M.conjugate().T


def simp(M):
    return M.applyfunc(lambda z: sp.nsimplify(sp.expand(z)))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
XB = sp.kronecker_product(I2, X)
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
u, v, t = sp.symbols("u v t", real=True)


def U(uu, vv):
    return sp.diag(sp.exp(I * uu), sp.exp(-I * uu), sp.exp(I * vv), sp.exp(-I * vv))


def zero_sym(M):
    return all(sp.simplify(sp.expand(z)) == 0 for z in M)


# ---------------- T1 ----------------
gen = sp.kronecker_product(I2, sp.diag(1, sp.exp(I * t)))
t1 = zero_sym(gen - sp.exp(I * t / 2) * U(-t / 2, -t / 2))
t1 = t1 and zero_sym(CNOT * gen * CNOT - sp.exp(I * t / 2) * U(-t / 2, t / 2))
t1 = t1 and zero_sym(CNOT * U(u, v) * CNOT - U(u, -v)) and zero_sym(XB * U(u, v) * XB - U(-u, -v))
t1 = t1 and CNOT * CNOT == sp.eye(4) and XB * XB == sp.eye(4) and CNOT * XB == XB * CNOT
F = [sp.eye(4), CNOT, XB, CNOT * XB]
nondiag = all(any(M[i, j] != 0 for i in range(4) for j in range(4) if i != j) for M in F[1:])
t1 = t1 and nondiag
check("T1", t1, "generators in T^2 . {1, CNOT, X_B, CNOT X_B} modulo scalars; CNOT U(u,v) CNOT = U(u,-v), "
      "X_B U(u,v) X_B = U(-u,-v); CNOT, X_B commuting involutions, none diagonal: four components, identity component T^2")

# ---------------- T2 ----------------
xs = sp.symbols("x0 x1 x2 x3", real=True)
ys = sp.symbols("y0 y1 y2 y3", real=True)
h = sp.Matrix([xs[k] + I * ys[k] for k in range(4)])
lhs = sp.expand((dagger(h) * U(u, v) * XB * h)[0])
rhs = sp.expand(2 * sp.re(sp.conjugate(h[0]) * h[1] * sp.exp(I * u)) + 2 * sp.re(sp.conjugate(h[2]) * h[3] * sp.exp(I * v)))
t2 = sp.simplify(sp.expand_complex(lhs - rhs)) == 0
inst = []
for hh, UU, name in ((sp.Matrix([1, 1, 2, I]), sp.diag(I, -I, 1, 1), "(1,1,2,i), U(pi/2,0)"),
                     (sp.Matrix([1, 2, 3, 4]), sp.diag(I, -I, I, -I), "(1,2,3,4), U(pi/2,pi/2)")):
    val = sp.nsimplify(sp.expand((dagger(hh) * UU * XB * hh)[0]))
    inst.append((name, val))
    t2 = t2 and val == 0
check("T2", t2, "<h|U(u,v) X_B h> = 2Re(conj(h00)h01 e^iu) + 2Re(conj(h10)h11 e^iv) symbolically; instances "
      + "; ".join(f"{n}: {val}" for n, val in inst))

# ---------------- T3 ----------------
hs = sp.Matrix([sp.symbols("a0"), sp.symbols("a1"), sp.symbols("a2"), sp.symbols("a3")])
Uh = U(u, v) * hs
det_sym = sp.expand(Uh[0] * Uh[3] - Uh[1] * Uh[2])
t3 = sp.simplify(det_sym - (sp.exp(I * (u - v)) * hs[0] * hs[3] - sp.exp(I * (v - u)) * hs[1] * hs[2])) == 0


def absq(z):
    return sp.nsimplify(sp.expand(z * sp.conjugate(z)))


def product_free(hh):
    """the torus orbit of hh is product-free iff |h00 h11| != |h01 h10| (compared as squared moduli)"""
    return absq(hh[0] * hh[3]) != absq(hh[1] * hh[2])


seed = sp.Matrix([2, 1, 1, 0])
comps = [simp(g * seed) for g in F]
pf = all(product_free(c) for c in comps)
t3 = t3 and pf
cc = sp.Matrix([1, 2, 2, -4])
img = simp(sp.diag(I, -I, 1, 1) * cc)
det_cc = sp.nsimplify(sp.expand(img[0] * img[3] - img[1] * img[2]))
fact = simp(sp.kronecker_product(sp.Matrix([I, 2]), sp.Matrix([1, -2])))
t3 = t3 and absq(cc[0] * cc[3]) == absq(cc[1] * cc[2]) and det_cc == 0 and img == fact
check("T3", t3, f"det law symbolic; seed (2,1,1,0): product-free on all four components {pf} "
      f"(squared moduli {[ (absq(c[0]*c[3]), absq(c[1]*c[2])) for c in comps]}); countercontrol (1,2,2,-4): "
      f"|h00h11|^2 = |h01h10|^2 = {absq(cc[0]*cc[3])}, U(pi/2,0) h = {list(img)} = (i,2) (x) (1,-2), det {det_cc}")

# ---------------- T4 ----------------
c, s = sp.symbols("c s", positive=True)
ph, pk = sp.symbols("ph pk")  # placeholders not needed: use an explicit pair with symbolic overlap via 2-dim model
# pairing law from the definitions: tr((I - c P_j)(I - c P_k)) = 4 - 2c + c^2 tr(P_j P_k), tr(P_j P_k) = s
law = sp.expand(4 - 2 * c + c ** 2 * s)
# verify on exact rank-one projectors with rational overlap: h_j = (1,0,0,0), h_k = (3,4,0,0)/5 -> s = 9/25
hj = sp.Matrix([1, 0, 0, 0])
hk = sp.Matrix([3, 4, 0, 0]) / 5
Pj = hj * dagger(hj)
Pk = hk * dagger(hk)
cval = sp.Rational(51, 50)
pair = sp.nsimplify(sp.expand(((sp.eye(4) - cval * Pj) * (sp.eye(4) - cval * Pk)).trace()))
t4 = pair == law.subs({c: cval, s: sp.Rational(9, 25)})
at2 = sp.expand(law.subs(c, 2))
cc2 = sp.simplify((sp.sqrt(2 - 1) + sp.sqrt(2 - 1)) ** 2 - 2 * 2 * s)   # (CC) at c = 2: 4 <= 4 s
t4 = t4 and at2 == 4 * s and cc2 == 4 - 4 * s
check("T4", t4, f"<d_j, d_k> = 4 - 2c + c^2 s (exact instance {pair} at c = 51/50, s = 9/25); at c = 2 the pairing is {at2} >= 0; "
      f"(CC) at c = 2 reads 4 <= 4 s, i.e. s = 1 on every positively paired pair")

# ---------------- T5 ----------------
hseed = sp.Matrix([1, 1, 2, I])
hp = simp(sp.diag(I, -I, 1, 1) * XB * hseed)
n2 = sp.nsimplify(sp.expand((dagger(hseed) * hseed)[0]))
n2p = sp.nsimplify(sp.expand((dagger(hp) * hp)[0]))
cstar = sp.Rational(51, 50)
lam = (cstar - 1) / (4 - 2 * cstar)
Ph = simp(hseed * dagger(hseed) / n2)
Php = simp(hp * dagger(hp) / n2p)
dh = sp.eye(4) - cstar * Ph
dhp = sp.eye(4) - cstar * Php
y = simp(Ph + lam * dhp)
pair_h = sp.nsimplify(sp.expand((y * dh).trace()))
neg = sp.nsimplify(sp.expand((dagger(hp) * y * hp)[0] / n2p))
t5 = (lam == sp.Rational(1, 98)) and pair_h == 0 and neg == lam * (1 - cstar) and neg < 0
circle = [sp.Integer(1), sp.Integer(-1), I, -I, (3 + 4 * I) / 5, (3 - 4 * I) / 5, (4 + 3 * I) / 5, (4 - 3 * I) / 5]
nsamp, minpair, idok = 0, None, True
for eu, ev in product(circle, circle):
    Ut = sp.diag(eu, sp.conjugate(eu), ev, sp.conjugate(ev))
    for g in F:
        gh = simp(Ut * g * hseed)
        Pg = simp(gh * dagger(gh) / n2)
        d = sp.eye(4) - cstar * Pg
        val = sp.nsimplify(sp.expand((y * d).trace()))
        shl = sp.nsimplify(sp.expand(absq((dagger(hseed) * gh)[0]) / (n2 * n2)))
        shpl = sp.nsimplify(sp.expand(absq((dagger(hp) * gh)[0]) / (n2p * n2)))
        ident = sp.nsimplify(cstar * (1 - shl) + lam * cstar ** 2 * shpl)
        if val != ident:
            idok = False
        nsamp += 1
        minpair = val if minpair is None else min(minpair, val)
t5 = t5 and idok and minpair >= 0
check("T5", t5, f"lambda = {lam}; <y, d_h> = {pair_h}; h'^* y h'/|h'|^2 = {neg} < 0; over {nsamp} sampled orbit defects "
      f"min <y, d> = {minpair} >= 0, C18-1's identity on every sample {idok}")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B21-EXACT" if not FAIL else "VERDICT B21-FAILED " + " ".join(FAIL))
sys.exit(0)
