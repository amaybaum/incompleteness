#!/usr/bin/env python3
"""b13_preflight.py -- node B13 of research/bridge (round 3): exact preflight of every algebraic statement the design
module BridgeReach.lean relies on, under its conventions, before the dispatch.

DECISION RULE (fixed 2026-10-11T01:09:57Z, from `date -u` immediately before writing; before run 1).

Conventions (as in the module): a pair vector is psi(a, b), a the first token, listed (00, 01, 10, 11);
prodDet psi = psi00 psi11 - psi01 psi10; prodCross x y = x00 y11 + y00 x11 - x01 y10 - y01 x10;
kron2 a b = (a0 b0, a0 b1, a1 b0, a1 b1); CNOT psi (a, b) = psi(a, b xor a); conjV = entrywise conjugation;
bellV = (1, 0, 0, 1). Matrices act on column vectors in the order (00, 01, 10, 11).

CHECKS
  P1  prodDet(x + t y) - (prodDet x + prodCross x y * t + prodDet y * t^2) expands to 0 (x, y, t symbolic).
  P2  prodDet(kron2 a b) expands to 0 (a, b symbolic).
  P3  The three-root lemma's linear_combination certificates are polynomial identities:
        (t1 - t2)(b + c(t1 + t2)) = e1 - e2;  (t1 - t3)(b + c(t1 + t3)) = e1 - e3;  (t2 - t3) c = l1 - l2;
        b = l1 - (t1 + t2) c;  a = e1 - t1 b - t1^2 c   (e_k = a + b t_k + c t_k^2, l_k = b + c(t1 + t_{k+1})).
      Countercontrol: with t1 = t2 the system has the nonzero solution (a, b, c) = (t1 t3, -(t1 + t3), 1).
  P4  conjV(v + n w) = conjV v + n conjV w for natural n (v, w with real and imaginary parts symbolic, n = 0..5);
      countercontrol: for t = i it fails (conj(i) = -i).
  P5  prodDet bellV = 1; for psi = (1, 2, 3, 5): prodDet psi = -1 and prodDet(CNOT psi) = -7, with CNOT psi =
      (1, 2, 5, 3) computed from the matrix of (a, b) -> (a, b xor a); the module's map
      cnotV psi = ![![psi00, psi01], ![psi11, psi10]] agrees with that matrix on a symbolic vector.
  P6  The avoidance construction on actual instances: the family f_U(v) = prodDet(U v) for U in {1, CNOT, SWAP,
      H(x)1, S(x)H, CZ} and the antiunitary f(v) = prodDet(U conj v) for U in {1, CNOT}: running the module's
      induction (start v = 0 is replaced at each step by v + n w with n in 0..2|s|, w = U_j^* bellV, or conj of it
      for the antiunitary member) ends at a v with every f nonzero, exactly. Countercontrol: the zero matrix
      gives prodDet(0 v) = 0 for all v.
  P7  The coset conditions of ReachAnti: for kappa = K o conj with K = S(x)H, and h = CNOT, the map
      kappa h kappa^-1 equals the matrix K conj(h) K^*, and kappa^2 equals K conj(K), on a symbolic vector.

VERDICT B13-PREFLIGHT-OK iff P1-P7 all PASS; otherwise VERDICT B13-PREFLIGHT-FAILED followed by the failing ids.
"""
import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg=""):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


def pdet(v): return v[0] * v[3] - v[1] * v[2]
def pcross(x, y): return x[0] * y[3] + y[0] * x[3] - x[1] * y[2] - y[1] * x[2]


# P1
xs = sp.symbols("x0:4")
ys = sp.symbols("y0:4")
t = sp.symbols("t")
line = [xs[k] + t * ys[k] for k in range(4)]
p1 = sp.expand(pdet(line) - (pdet(xs) + pcross(xs, ys) * t + pdet(ys) * t ** 2)) == 0
check("P1", p1, f"prodDet expansion along a line: {p1}")

# P2
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")
kr = [a0 * b0, a0 * b1, a1 * b0, a1 * b1]
p2 = sp.expand(pdet(kr)) == 0
check("P2", p2, f"prodDet(kron2 a b) = 0: {p2}")

# P3
A, Bc, C, t1, t2, t3 = sp.symbols("A B C t1 t2 t3")
e = {k: A + Bc * tk + C * tk ** 2 for k, tk in ((1, t1), (2, t2), (3, t3))}
l1 = Bc + C * (t1 + t2)
l2 = Bc + C * (t1 + t3)
certs = [
    sp.expand((t1 - t2) * l1 - (e[1] - e[2])),
    sp.expand((t1 - t3) * l2 - (e[1] - e[3])),
    sp.expand((t2 - t3) * C - (l1 - l2)),
    sp.expand(Bc - (l1 - (t1 + t2) * C)),
    sp.expand(A - (e[1] - t1 * Bc - t1 ** 2 * C)),
]
cc = {A: t1 * t3, Bc: -(t1 + t3), C: 1}
counter = all(sp.expand(e[k].subs(cc).subs(t2, t1)) == 0 for k in (1, 2, 3))
check("P3", all(c == 0 for c in certs) and counter,
      f"five certificates are identities: {all(c == 0 for c in certs)}; countercontrol (t1 = t2 admits a nonzero "
      f"quadratic): {counter}")

# P4
vr = sp.symbols("vr0:4", real=True)
vi = sp.symbols("vi0:4", real=True)
wr = sp.symbols("wr0:4", real=True)
wi = sp.symbols("wi0:4", real=True)
v = [vr[k] + sp.I * vi[k] for k in range(4)]
w = [wr[k] + sp.I * wi[k] for k in range(4)]
ok4 = True
for n in range(6):
    ok4 &= all(sp.expand(sp.conjugate(v[k] + n * w[k]) - (sp.conjugate(v[k]) + n * sp.conjugate(w[k]))) == 0
               for k in range(4))
bad = any(sp.expand(sp.conjugate(v[k] + sp.I * w[k]) - (sp.conjugate(v[k]) + sp.I * sp.conjugate(w[k]))) != 0
          for k in range(4))
check("P4", ok4 and bad, f"conj fixes natural parameters n = 0..5: {ok4}; countercontrol t = i fails: {bad}")

# P5
idx = [(0, 0), (0, 1), (1, 0), (1, 1)]
CNOTm = sp.zeros(4, 4)
for c, (aa, bb) in enumerate(idx):
    r = idx.index((aa, bb ^ aa))
    CNOTm[r, c] = 1
bell = [1, 0, 0, 1]
psi = sp.Matrix([1, 2, 3, 5])
cpsi = CNOTm * psi
s = sp.symbols("s0:4")
cnotV = [s[0], s[1], s[3], s[2]]
agree = list(CNOTm * sp.Matrix(s)) == cnotV
ok5 = pdet(bell) == 1 and pdet(list(psi)) == -1 and list(cpsi) == [1, 2, 5, 3] and pdet(list(cpsi)) == -7 and agree
check("P5", ok5, f"prodDet bellV = {pdet(bell)}; prodDet psi = {pdet(list(psi))}; CNOT psi = {list(cpsi)}, "
      f"prodDet = {pdet(list(cpsi))}; cnotV agrees with the CNOT matrix: {agree}")

# P6
h = 1 / sp.sqrt(2)
Hm = sp.Matrix([[h, h], [h, -h]])
Sm = sp.Matrix([[1, 0], [0, sp.I]])
I2 = sp.eye(2)
def kron(P, Q): return sp.Matrix(sp.kronecker_product(P, Q))
SWAP = sp.zeros(4, 4)
for c, (aa, bb) in enumerate(idx):
    SWAP[idx.index((bb, aa)), c] = 1
CZ = sp.diag(1, 1, 1, -1)
fam = [("1", sp.eye(4), False), ("CNOT", CNOTm, False), ("SWAP", SWAP, False), ("H(x)1", kron(Hm, I2), False),
       ("S(x)H", kron(Sm, Hm), False), ("CZ", CZ, False), ("conj", sp.eye(4), True), ("CNOT conj", CNOTm, True)]
def fval(U, anti, vec):
    vv = sp.Matrix(vec).applyfunc(sp.conjugate) if anti else sp.Matrix(vec)
    return sp.nsimplify(sp.simplify(pdet(list(U * vv))))
bellM = sp.Matrix(bell)
cur = [0, 0, 0, 0]
steps = []
for j, (name, U, anti) in enumerate(fam):
    wv = U.H * bellM
    if anti:
        wv = wv.applyfunc(sp.conjugate)
    assert fval(U, anti, list(wv)) != 0
    done = fam[: j + 1]
    chosen = None
    for n in range(2 * len(done) + 1):
        cand = [sp.simplify(cur[k] + n * wv[k]) for k in range(4)]
        if all(fval(U2, an2, cand) != 0 for (_, U2, an2) in done):
            chosen = (n, cand)
            break
    if chosen is None:
        steps.append((name, None))
        break
    steps.append((name, chosen[0]))
    cur = chosen[1]
final_ok = all(n is not None for (_, n) in steps) and all(fval(U, an, cur) != 0 for (_, U, an) in fam)
zero_ctl = sp.expand(pdet(list(sp.zeros(4, 4) * sp.Matrix(s)))) == 0
check("P6", final_ok and zero_ctl,
      f"induction steps (member, n): {steps}; final v = {[sp.nsimplify(c) for c in cur]} avoids all "
      f"{len(fam)} members: {final_ok}; zero-matrix countercontrol: {zero_ctl}")

# P7
K = kron(Sm, Hm)
x = sp.Matrix(sp.symbols("z0:4"))
def kap(vec): return K * vec.applyfunc(sp.conjugate)
def kapinv(vec): return (K.H * vec).applyfunc(sp.conjugate)
inv_ok = sp.simplify(kap(kapinv(x)) - x) == sp.zeros(4, 1)
lhs = kap(CNOTm * kapinv(x))
rhs = K * CNOTm.applyfunc(sp.conjugate) * K.H * x
conj_ok = sp.simplify(lhs - rhs) == sp.zeros(4, 1)
sq_ok = sp.simplify(kap(kap(x)) - K * K.applyfunc(sp.conjugate) * x) == sp.zeros(4, 1)
check("P7", inv_ok and conj_ok and sq_ok,
      f"kappa^-1 = conj o K^*: {inv_ok}; kappa h kappa^-1 = K conj(h) K^*: {conj_ok}; kappa^2 = K conj(K): {sq_ok}")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B13-PREFLIGHT-OK" if not FAIL else "VERDICT B13-PREFLIGHT-FAILED " + " ".join(FAIL))
