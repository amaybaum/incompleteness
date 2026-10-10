"""EQ2-C, C2(b): EQ-D T1 drivesElementary_of_qubit and T4 cardSplit_independence, refined against the kernel text
(ImplementationLocality, SubstratumSource, StructuralClosure, MinimalRepertoire, LieRankSource).

Kernel facts used (read at bcbc516f): DrivesElementary SS:77 has three clauses over EVERY carrier S and EVERY a, b
(including a = b): flow (transition a b) t, permMatrix (Equiv.swap a b), phaseGate a. transition LRS:199 =
single a b 1 + single b a 1 (so transition a a = 2 E_aa); phaseGate LRS:209 = diagonal (I at a); flow RS:95 =
exp((-t I) . H). ContextStable IL:359 adjoins 1_R on the FIRST factor; ancBlock AC:457 reads the ancilla in the SECOND
factor; Architecture IL:506 (one, mul, smul, proj, block).
Closed forms used below (written lemma, standard: T = E_ab + E_ba has T^2 = E_aa + E_bb =: P, T^3 = T):
  a != b:  flow (transition a b) t = 1 + (cos t - 1) P - i sin t T;   a = b: flow = 1 + (e^(-2it) - 1) E_aa.

DECISION RULE (fixed before the first run). Verdict "DRIVE-LIFT-REFINED" prints only if all pass:
  D0  T^2 = P and T^3 = T for transition a b (a != b), exactly, on Fin 2..5 (the basis of the closed form).
  D1  with D = tensorOf 1 ((phaseGate 0)^2) -- NO relabelling of D (EQ-D used reindex tau; tau = id suffices) --
      and M = reindex sigma (tensorOf 1 (flow X s)), sigma the involution (a,1) <-> (b,0) of R x Fin 2:
      M D M D = tensorOf (flow (transition a b) (2s)) 1, modulo cos^2 + sin^2 = 1, for every ordered a != b in
      R = Fin 2..5; its ancBlock (0,0) is flow (transition a b) (2s).
  D2  phases: reindex e (tensorOf 1 (phaseGate 0)) with e the involution (r,0) <-> (r,1), r != a, has ancBlock (0,0)
      = phaseGate a (R = Fin 1..5, every a).
  D3  a = b flows: the same relabelling applied to flow (transition 0 0) t on Fin 2 gives flow (transition a a) t.
  D4  swaps: phaseGate a * phaseGate b * flow (transition a b) (pi/2) = permMatrix (swap a b) for a != b; for a = b
      permMatrix (swap a a) = 1 (Equiv.swap_self, permMatrix_one' LRS:228, Architecture.one).
  D5  countercontrols: without D, M M is not the target (R = Fin 3); with sigma = id, M D M D = 1.
  D6  mutation self-test of the comparator: wrong angle and wrong pair are rejected.
  K1  T4 arithmetic: c * m = 2^j with m >= 1 forces c = 2^i (exhaustive, c * m <= 2^16); and c * 0 is never 2^j.
  K2  T4 witnesses: tensorOf 1_(Fin 3) (flow (transition 0 1) (pi/4)) on the 6-element carrier is not monomial (a column
      with two nonzero entries), so cardSplitClass is not ContextStable; flow (transition 0 1) (pi/4) on Fin 3 is not
      monomial, so cardSplitClass does not drive; conj of rot (x) 1_3 does not preserve the diagonal.
Exact (sympy rationals, I, sqrt(2); polynomial reduction modulo c^2 + s^2 - 1).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c_common import Checks  # noqa: E402
import sympy as sp  # noqa: E402

C = Checks("c2b_drive_lift")
I = sp.I
c, s = sp.symbols("c s", real=True)
u = sp.symbols("u")


def circ_zero(expr):
    ex = sp.expand(expr)
    if ex == 0:
        return True
    re_, im_ = sp.expand(sp.re(ex)), sp.expand(sp.im(ex))
    ok = True
    for part in (re_, im_):
        _, rem = sp.reduced(part, [s ** 2 + c ** 2 - 1], s, c)
        ok &= sp.expand(rem) == 0
    return ok


def mat_zero(M):
    return all(circ_zero(x) for x in M)


def E(n, i, j):
    M = sp.zeros(n, n)
    M[i, j] = 1
    return M


def transition(n, a, b):
    return E(n, a, b) + E(n, b, a)


def flow_closed(n, a, b, cs, sn):
    """closed form of flow (transition a b) t with cos t = cs, sin t = sn (a != b)"""
    P = E(n, a, a) + E(n, b, b)
    return sp.eye(n) + (cs - 1) * P - I * sn * transition(n, a, b)


def phaseGate(n, a):
    return sp.diag(*[(I if k == a else 1) for k in range(n)])


def tensorOf(X, Y):
    n, m = X.shape[0], Y.shape[0]
    return sp.Matrix(n * m, n * m, lambda p, q: X[p // m, q // m] * Y[p % m, q % m])


def reindex(perm, K):
    """Matrix.reindex e e K = K.submatrix e.symm e.symm; perm is an involution here, so e.symm = e"""
    n = K.shape[0]
    return sp.Matrix(n, n, lambda p, q: K[perm[p], perm[q]])


def ancBlock(K, m, f, e):
    n = K.shape[0] // m
    return sp.Matrix(n, n, lambda p, q: K[p * m + f, q * m + e])


def permMatrix(n, g):
    return sp.Matrix(n, n, lambda i, j: 1 if g[j] == i else 0)


# ----------------------------------------------------------------------------- D0

ok = True
for n in range(2, 6):
    for a in range(n):
        for b in range(n):
            if a != b:
                T = transition(n, a, b)
                P = E(n, a, a) + E(n, b, b)
                ok &= (T * T - P).is_zero_matrix and (T * T * T - T).is_zero_matrix
C.check("D0 T = transition a b (a != b): T^2 = E_aa + E_bb and T^3 = T on Fin 2..5 (basis of the closed form)", ok)

# ----------------------------------------------------------------------------- D1

F = flow_closed(2, 0, 1, c, s)                      # flow (transition 0 1) s on Fin 2
Z2 = phaseGate(2, 0) ** 2
ok = True
count = 0
for r in range(2, 6):
    for a in range(r):
        for b in range(r):
            if a == b:
                continue
            perm = list(range(2 * r))
            perm[2 * a + 1], perm[2 * b + 0] = 2 * b + 0, 2 * a + 1
            M = reindex(perm, tensorOf(sp.eye(r), F))
            D = tensorOf(sp.eye(r), Z2)
            target = tensorOf(flow_closed(r, a, b, c ** 2 - s ** 2, 2 * c * s), sp.eye(2))
            prodM = M * D * M * D
            ok &= mat_zero(prodM - target)
            ok &= mat_zero(ancBlock(prodM, 2, 0, 0) - flow_closed(r, a, b, c ** 2 - s ** 2, 2 * c * s))
            count += 1
C.check(f"D1 M D M D = tensorOf (flow (transition a b) (2s)) 1 with D = tensorOf 1 ((phaseGate 0)^2) unrelabelled, "
        f"and ancBlock 0 0 gives flow (transition a b) (2s): all {count} ordered pairs a != b in Fin 2..5", ok)

# ----------------------------------------------------------------------------- D2, D3

ok2, ok3 = True, True
for r in range(1, 6):
    for a in range(r):
        perm = list(range(2 * r))
        for q in range(r):
            if q != a:
                perm[2 * q], perm[2 * q + 1] = 2 * q + 1, 2 * q
        K = reindex(perm, tensorOf(sp.eye(r), phaseGate(2, 0)))
        ok2 &= (ancBlock(K, 2, 0, 0) - phaseGate(r, a)).is_zero_matrix
        K3 = reindex(perm, tensorOf(sp.eye(r), sp.diag(u, 1)))     # flow (transition 0 0) t = diag(e^(-2it), 1)
        ok3 &= (ancBlock(K3, 2, 0, 0) - sp.diag(*[(u if k == a else 1) for k in range(r)])).is_zero_matrix
C.check("D2 phases: relabel (r,0) <-> (r,1) for r != a, then ancBlock 0 0 of tensorOf 1 (phaseGate 0) is phaseGate a "
        "(every a in Fin 1..5)", ok2)
C.check("D3 a = b flows: the same relabelling turns diag(e^(-2it), 1) = flow (transition 0 0) t into "
        "diag(e^(-2it) at a) = flow (transition a a) t (every a in Fin 1..5)", ok3)

# ----------------------------------------------------------------------------- D4

ok = True
for n in range(2, 6):
    for a in range(n):
        for b in range(n):
            if a != b:
                g = list(range(n))
                g[a], g[b] = b, a
                lhs = phaseGate(n, a) * phaseGate(n, b) * flow_closed(n, a, b, 0, 1)
                ok &= (sp.expand(lhs - permMatrix(n, g))).is_zero_matrix
C.check("D4 swaps: phaseGate a * phaseGate b * flow (transition a b) (pi/2) = permMatrix (swap a b) for a != b "
        "(Fin 2..5); a = b: permMatrix (swap a a) = permMatrix 1 = 1", ok and
        permMatrix(3, [0, 1, 2]) == sp.eye(3))

# ----------------------------------------------------------------------------- D5 countercontrols

r, a, b = 3, 0, 1
perm = list(range(2 * r))
perm[2 * a + 1], perm[2 * b] = 2 * b, 2 * a + 1
M = reindex(perm, tensorOf(sp.eye(r), F))
D = tensorOf(sp.eye(r), Z2)
target = tensorOf(flow_closed(r, a, b, c ** 2 - s ** 2, 2 * c * s), sp.eye(2))
M0 = tensorOf(sp.eye(r), F)
C.check("D5 countercontrols: without D, M M is not the target (R = Fin 3); with sigma = id, M D M D = 1 (the relabelling "
        "is load-bearing)", not mat_zero(M * M - target) and mat_zero(M0 * D * M0 * D - sp.eye(2 * r)))

r, a, b = 4, 1, 3
perm = list(range(2 * r))
perm[2 * a + 1], perm[2 * b] = 2 * b, 2 * a + 1
M = reindex(perm, tensorOf(sp.eye(r), F))
D = tensorOf(sp.eye(r), Z2)
P4 = M * D * M * D
wrong_angle = tensorOf(flow_closed(r, a, b, c, s), sp.eye(2))
wrong_pair = tensorOf(flow_closed(r, a, 2, c ** 2 - s ** 2, 2 * c * s), sp.eye(2))
right = tensorOf(flow_closed(r, a, b, c ** 2 - s ** 2, 2 * c * s), sp.eye(2))
C.check("D6 mutation self-test of the comparator (R = Fin 4, a = 1, b = 3): the right target matches; the angle s in "
        "place of 2s and the pair (1, 2) in place of (1, 3) are rejected",
        mat_zero(P4 - right) and not mat_zero(P4 - wrong_angle) and not mat_zero(P4 - wrong_pair))

# ----------------------------------------------------------------------------- K1, K2: T4

pow2 = {2 ** j for j in range(0, 17)}
ok = all((c_ * m_ not in pow2) or (c_ in pow2) for c_ in range(0, 2 ** 16 + 1) for m_ in range(1, 2 ** 16 // max(c_, 1) + 1)
         if c_ * m_ <= 2 ** 16)
C.check("K1 c * m = 2^j with m >= 1 forces c = 2^i (exhaustive for c * m <= 2^16); with m = 0, c * 0 = 0 is never 2^j",
        ok and 0 not in pow2)
h = sp.sqrt(2) / 2
Fq = flow_closed(2, 0, 1, h, h)                    # flow (transition 0 1) (pi/4)
K6 = tensorOf(sp.eye(3), Fq)


def not_monomial(K):
    n = K.shape[0]
    return any(sum(1 for i in range(n) if sp.simplify(K[i, j]) != 0) >= 2 for j in range(n))


diag_in = sp.diag(1, 0, 0, 0, 0, 0)
rot = sp.Matrix([[h, -h], [h, h]])
Rc = tensorOf(rot, sp.eye(3))
out = Rc * diag_in * Rc.H
C.check("K2 cardSplit witnesses: tensorOf 1_(Fin 3) (flow X (pi/4)) on the 6-element carrier has a column with two nonzero "
        "entries (not monomial; not ContextStable); flow (transition 0 1) (pi/4) on Fin 3 is not monomial (does not "
        "drive); conj (rot (x) 1_3) sends a diagonal matrix to a non-diagonal one",
        not_monomial(K6) and not_monomial(flow_closed(3, 0, 1, h, h)) and
        any(sp.simplify(out[i, j]) != 0 for i in range(6) for j in range(6) if i != j))

sys.exit(C.finish("DRIVE-LIFT-REFINED: the Fin 2 data (phaseGate 0, flow of transition 0 0 and 0 1) with Architecture "
                  "(one, mul, block), ContextStable and LabelInvariant reach every clause of DrivesElementary, a = b "
                  "included; D needs no relabelling; cardSplitClass's witnesses are exact"))
