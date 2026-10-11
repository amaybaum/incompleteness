#!/usr/bin/env python3
"""b18_preflight.py -- node B18 of research/bridge (round 5): the correction item of HO-33 (finding F1). Exact
preflight of the design lemma `phaseFree_of_layerFlowExecutable_free` (lean/BridgeToken.lean, section B): the kernel's
isolation identity (LiftAudit.lean:660) for a fixed-point-free involution needs no phase at a general angle, because
the phase diagonal is then a unimodular scalar, which conjugation discards.

DECISION RULE (fixed 2026-10-11T07:43:14Z, from `date -u` immediately before writing; before run 1).

All matrices are rebuilt here from the kernel's definitions, read at L in this tree:
  permMat sigma x y = [sigma y = x]                                   (SecondOrderCircuit.lean:710)
  proj g = (1/2)(1 - g);  unit g t = 1 + (e^{i pi t} - 1) proj g       (SecondOrderCircuit.lean:352, :356)
  gateFlow tau t = unit (permMat tau) t                               (LiftAudit.lean:47)
  levelPerm sigma n (s, k) = (sigma s, k)                              (LiftAudit.lean:51)
  signFun tau e a z = -1 if tau z != z and not (z = a or z = tau a) and e z < e (tau z) else 1   (:582)
  phaseFun tau t z = 1 if tau z = z else e^{-i pi t}                   (:586)
  transition a b = E_ab + E_ba;  flow H s = exp(-i s H)                (LieRankSource.lean:199; ReachabilitySeam.lean:95)
Symbolic in t (sympy, exact); e is the lexicographic enumeration (the identity holds for every enumeration; one is
fixed here).

CHECKS
  P1  S = Fin 2, sigma the exchange, n = 1, 2, 3: tau = levelPerm sigma n moves every configuration and phaseFun tau t
      takes the single value e^{-i pi t}.
  P2  The isolation identity, symbolically in t, for n = 1, 2, 3 and a = (0, 0):
      diag(phaseFun) * G * (D * G * D) = flow (transition a (tau a)) (pi t),  G = gateFlow tau t, D = diag(signFun).
  P3  Its scalar-free form: G * D * G * D = e^{i pi t} * flow (transition a (tau a)) (pi t), symbolically, n = 1, 2, 3.
  P4  D has entries in {1, -1}, every entry's fourth power is 1 (the lattice invariant), and D^H D = 1.
  P5  Countercontrol (the fixed-point-free hypothesis is load-bearing): S = Fin 3, sigma the exchange of 0 and 1
      (2 fixed), n = 1: phaseFun takes two values, and G * D * G * D is not a scalar multiple of the transition flow
      (the (2, 2) entry forces the scalar 1 and the (0, 1) entry then differs for generic t; checked symbolically and at
      t = 1/2).
  P6  The pair carrier S = Fin 2 x Fin 2 with sigma_2 = id x exchange: fixed-point-free at levels n = 1, 2, and P2/P3
      hold at n = 1 (carrier of 8 configurations).

VERDICT B18-PREFLIGHT-OK iff P1-P6 all PASS; otherwise VERDICT B18-PREFLIGHT-FAILED followed by the failing ids.
"""
import sys
from itertools import product

import sympy as sp

I = sp.I
t = sp.symbols("t", real=True)
PASS, FAIL = [], []


def check(name, ok, msg):
    (PASS if ok else FAIL).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {msg}")


def zero_sym(M):
    return all(sp.simplify(sp.expand(sp.expand_complex(z).rewrite(sp.exp))) == 0 for z in M)


# ---------------- the kernel's definitions on an explicit configuration list ----------------
def perm_mat(conf, tau):
    idx = {c: i for i, c in enumerate(conf)}
    N = len(conf)
    M = sp.zeros(N, N)
    for y in conf:
        M[idx[tau(y)], idx[y]] = 1
    return M


def unit(g, tt):
    N = g.shape[0]
    return sp.eye(N) + (sp.exp(I * sp.pi * tt) - 1) * (sp.Rational(1, 2) * (sp.eye(N) - g))


def sign_diag(conf, tau, a):
    idx = {c: i for i, c in enumerate(conf)}
    vals = []
    for z in conf:
        moved = tau(z) != z
        chosen = (z == a) or (z == tau(a))
        lower = idx[z] < idx[tau(z)]
        vals.append(-1 if (moved and not chosen and lower) else 1)
    return sp.diag(*vals), vals


def phase_diag(conf, tau, tt):
    vals = [1 if tau(z) == z else sp.exp(-I * sp.pi * tt) for z in conf]
    return sp.diag(*vals), vals


def flow_transition(conf, a, b, s):
    """exp(-i s (E_ab + E_ba)) = 1 + (cos s - 1)(E_aa + E_bb) - i sin s (E_ab + E_ba), a != b."""
    idx = {c: i for i, c in enumerate(conf)}
    N = len(conf)
    M = sp.eye(N)
    ia, ib = idx[a], idx[b]
    M[ia, ia] = sp.cos(s)
    M[ib, ib] = sp.cos(s)
    M[ia, ib] = -I * sp.sin(s)
    M[ib, ia] = -I * sp.sin(s)
    return M


def level_conf(S, n):
    return [(s, k) for s in S for k in range(n)]


def run_identity(conf, tau, a):
    g = perm_mat(conf, tau)
    G = unit(g, t)
    D, dvals = sign_diag(conf, tau, a)
    P, pvals = phase_diag(conf, tau, t)
    F = flow_transition(conf, a, tau(a), sp.pi * t)
    lhs2 = P * G * (D * G * D)
    lhs3 = G * D * G * D
    return G, D, dvals, pvals, F, zero_sym(lhs2 - F), zero_sym(lhs3 - sp.exp(I * sp.pi * t) * F)


# ---------------- P1-P4: S = Fin 2, sigma the exchange ----------------
S2 = [0, 1]
sigma2 = lambda s: 1 - s
p1 = p2 = p3 = p4 = True
rep = []
for n in (1, 2, 3):
    conf = level_conf(S2, n)
    tau = lambda z, n=n: (sigma2(z[0]), z[1])
    a = (0, 0)
    moved_all = all(tau(z) != z for z in conf)
    G, D, dvals, pvals, F, ok2, ok3 = run_identity(conf, tau, a)
    pset = {sp.simplify(v) for v in pvals}
    p1 = p1 and moved_all and pset == {sp.exp(-I * sp.pi * t)}
    p2 = p2 and ok2
    p3 = p3 and ok3
    fourth = all(v ** 4 == 1 for v in dvals)
    unitary = sp.simplify(D.H * D - sp.eye(len(conf))) == sp.zeros(len(conf), len(conf))
    p4 = p4 and set(dvals) <= {1, -1} and fourth and unitary
    rep.append((n, moved_all, len(pset), ok2, ok3, dvals))
check("P1", p1, f"levels n = 1, 2, 3: every configuration moved {[r[1] for r in rep]}; phaseFun single value e^(-i pi t) "
      f"{[r[2] == 1 for r in rep]}")
check("P2", p2, f"isolation identity diag(phaseFun) G (D G D) = flow(transition a (tau a))(pi t), symbolic in t: "
      f"{[r[3] for r in rep]}")
check("P3", p3, f"scalar-free form G D G D = e^(i pi t) flow(...)(pi t), symbolic in t: {[r[4] for r in rep]}")
check("P4", p4, f"sign diagonals (n = 1, 2, 3): {[r[5] for r in rep]}; entries in {{1, -1}}, fourth powers 1, unitary")

# ---------------- P5: countercontrol with a fixed point ----------------
S3 = [0, 1, 2]
conf3 = level_conf(S3, 1)
tau3 = lambda z: ((1 - z[0]) if z[0] in (0, 1) else z[0], z[1])
a3 = (0, 0)
G3, D3, d3, pv3, F3, ok2_3, ok3_3 = run_identity(conf3, tau3, a3)
pset3 = {sp.simplify(v) for v in pv3}
M3 = G3 * D3 * G3 * D3
e22 = sp.simplify(M3[2, 2] - F3[2, 2])            # fixed point: both 1 -> the scalar would have to be 1
diff01 = sp.simplify((M3 - F3)[0, 1])
diff01_half = sp.simplify(diff01.subs(t, sp.Rational(1, 2)))
p5 = (len(pset3) == 2) and (e22 == 0) and (diff01 != 0) and (diff01_half != 0) and (not ok3_3) and ok2_3
check("P5", p5, f"S = Fin 3 with 2 fixed: phaseFun takes {len(pset3)} values; the kernel identity with the phase still "
      f"holds {ok2_3}; the scalar-free form fails {not ok3_3}: (2,2) difference {e22} forces scalar 1, (0,1) "
      f"difference {diff01} (at t = 1/2: {diff01_half})")

# ---------------- P6: the pair carrier with the exchange of the second token ----------------
S22 = [(x, y) for x in (0, 1) for y in (0, 1)]
sigma22 = lambda s: (s[0], 1 - s[1])
p6 = True
rep6 = []
for n in (1, 2):
    conf = level_conf(S22, n)
    tau = lambda z, n=n: (sigma22(z[0]), z[1])
    moved_all = all(tau(z) != z for z in conf)
    p6 = p6 and moved_all
    rep6.append((n, moved_all))
conf = level_conf(S22, 1)
tau = lambda z: (sigma22(z[0]), z[1])
G, D, dvals, pvals, F, ok2, ok3 = run_identity(conf, tau, ((0, 0), 0))
p6 = p6 and ok2 and ok3 and {sp.simplify(v) for v in pvals} == {sp.exp(-I * sp.pi * t)}
check("P6", p6, f"pair carrier, id x exchange: fixed-point-free at n = 1, 2 {[r[1] for r in rep6]}; at n = 1 (8 "
      f"configurations) the identity {ok2} and its scalar-free form {ok3}; sign diagonal {dvals}")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B18-PREFLIGHT-OK" if not FAIL else "VERDICT B18-PREFLIGHT-FAILED " + " ".join(FAIL))
sys.exit(0)
