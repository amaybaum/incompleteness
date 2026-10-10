"""EQ5-PREM q4 — the pair-level premises (K1: IsNot, NativeGate, Entangling; K-infinity-Copy: one common NOT) hold for
every pair of the countermodels M_rho, M_tw and M_th, whose gates are (cnot, cnot, cnot, cnotTw).  For cnot these are
landed (CD:838, :1160, :1380); this script checks the cnotTw clauses exactly, by reduction to cnot.  Research only.

Usage:  python3 -I -B q4_pair_gates.py <base>/verification/lean-mathlib/OIBridge <eq5>/inputs

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription: sgn, pc, pt, nflip, reflY, z3, xplus, phiW, idW parsed from the base equal the hand transcriptions;
    the package defines cnotTw as actTEquiv reflY o cnot o actTEquiv reflY (FourCopyDefs :81-84).
 N1 N-CLASS form: cnotTw w = actC id (actT reflY (cnot (actC id (actT reflY w)))) (symbolic), with reflY orthogonal.
 N2 NativeGate (eball 3) z3 nflip cnotTw, exact parts: frame (the four corner products), relT and relC with nflip
    (symbolic); the positivity clauses reduce to cnot's landed ones through
    cnotTw (prodState x y) = actT reflY (cnot (prodState x (reflY y))) and cnotTw^-1 = cnotTw (symbolic), and
    pairVal a b (actT reflY w) = pairVal a (reflY-hom b) w (symbolic; reflY maps effects of the ball to effects).
 N3 Entangling: cnotTw (prodState xplus z3) = idW = actT reflY phiW (exact); actT reflY is a linear involution
    preserving maxCone and the normalization, so it carries the extreme joint state phiW (entangling_cnot, CD:1380) to an
    extreme joint state that is not a product (W).
 N4 K-infinity-Copy: the NOT used in every clause of every pair's gate is the same nflip (by N2 and the landed cnot
    clauses).
 VERDICT Q4-PAIR-GATES-EXACT iff K and N1-N4 pass; otherwise VERDICT NOT RENDERED.  Exact arithmetic only; no timing.
"""
import os
import re
import sys

import sympy as sp

LEAN = sys.argv[1]
INPUTS = sys.argv[2]
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
CD = read(os.path.join(LEAN, "CompositeDimension.lean"))
K2G = read(os.path.join(LEAN, "K2Guard.lean"))
DEFS = read(os.path.join(INPUTS, "FourCopyDefs.lean")).split("\n")


def pmap(name):
    blk = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|[^\n]*\n)+)", CD).group(1)
    return {(int(a), int(b)): int(c) for a, b, c in re.findall(r"(\d), (\d) => (\d)", blk)}


PC, PT = pmap("pc"), pmap("pt")
msg = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1", CD)
NEG = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))}
PC_H = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
        (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT_H = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
        (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}
nflip_t = re.search(r"def nflip[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", CD).group(1).replace(" ", "")
reflY_t = re.search(r"def reflY[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", K2G).group(1).replace(" ", "")
idw_lit = "def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]" in K2G
lits = ("def z3 : Fin 3 → ℝ := ![0, 0, 1]" in CD and "def xplus : Fin 3 → ℝ := ![1, 0, 0]" in CD
        and "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0" in CD)
defs_ok = (DEFS[80].strip() == "def cnotTw : W 3 ≃ₗ[ℝ] W 3 :="
           and DEFS[81].strip() == "actTEquiv reflY reflY_reflY ≪≫ₗ cnot ≪≫ₗ actTEquiv reflY reflY_reflY"
           and DEFS[83].strip() == "theorem cnotTw_apply (ω : W 3) : cnotTw ω = actT reflY (cnot (actT reflY ω)) := rfl")
check("K transcription: sgn, pc, pt, nflip, reflY, z3, xplus, phiW, idW; package cnotTw = actT reflY o cnot o actT reflY "
      "(FourCopyDefs :81-84)", PC == PC_H and PT == PT_H and NEG == {(1, 3), (2, 2)} and nflip_t == "1,-1,-1"
      and reflY_t == "1,-1,1" and idw_lit and lits and defs_ok)

HRY = [1, 1, -1, 1]
HNF = [1, 1, -1, -1]
HID = [1, 1, 1, 1]


def zero(e):
    return sp.expand(e) == 0


def teq(A, B):
    return all(zero(A[m][n] - B[m][n]) for m in R4 for n in R4)


def hom(x):
    return [sp.Integer(1)] + [sp.sympify(v) for v in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def cnot(w):
    return [[(-1 if (m, n) in NEG else 1) * w[PC[(m, n)]][PT[(m, n)]] for n in R4] for m in R4]


def actT(hs, w):
    return [[hs[n] * w[m][n] for n in R4] for m in R4]


def actC(hs, w):
    return [[hs[m] * w[m][n] for n in R4] for m in R4]


def cnotTw(w):
    return actT(HRY, cnot(actT(HRY, w)))


def pairVal(a, b, w):
    return sp.expand(sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4))


W = [[sp.Symbol("w%d%d" % (m, n)) for n in R4] for m in R4]
xs, ys = sp.symbols("x1:4"), sp.symbols("y1:4")
check("N1 N-CLASS form: cnotTw = actC id o actT reflY o cnot o actC id o actT reflY (symbolic); reflY = diag(1,-1,1) is "
      "orthogonal", teq(cnotTw(W), actC(HID, actT(HRY, cnot(actC(HID, actT(HRY, W)))))) and reflY_t == "1,-1,1")


def corner(a):
    return [0, 0, 1] if a == 0 else [0, 0, -1]


frame = all(teq(cnotTw(prodState(corner(a), corner(b))), prodState(corner(a), corner((a + b) % 2)))
            for a in (0, 1) for b in (0, 1))
relT = teq(actT(HNF, cnotTw(actT(HNF, W))), cnotTw(W))
relC = teq(actC(HNF, cnotTw(actC(HNF, W))), actT(HNF, cnotTw(W)))
red_pos = teq(cnotTw(prodState(xs, ys)), actT(HRY, cnot(prodState(xs, [ys[0], -ys[1], ys[2]]))))
invol = teq(cnotTw(cnotTw(W)), W)
a_s, b_s = sp.symbols("a0:4"), sp.symbols("b0:4")
pull = zero(pairVal(a_s, b_s, actT(HRY, W)) - pairVal(a_s, [b_s[0], b_s[1], -b_s[2], b_s[3]], W))
check("N2 NativeGate (eball 3) z3 nflip cnotTw: frame on the four corner products, relT, relC (symbolic); positivity "
      "reduces to cnot's: cnotTw(prodState x y) = actT reflY (cnot (prodState x (reflY y))), cnotTw involution, and the "
      "reflY pullback of product effects (symbolic)", frame and relT and relC and red_pos and invol and pull,
      "frame %s relT %s relC %s reduction %s involution %s pullback %s" % (frame, relT, relC, red_pos, invol, pull))
PHIW = [[sp.Integer([1, 1, -1, 1][i]) if i == j else sp.Integer(0) for j in R4] for i in R4]
IDW = [[sp.Integer(1) if i == j else sp.Integer(0) for j in R4] for i in R4]
check("N3 Entangling: cnotTw(prodState xplus z3) = idW = actT reflY phiW (exact)",
      teq(cnotTw(prodState([1, 0, 0], [0, 0, 1])), IDW) and teq(actT(HRY, PHIW), IDW))
check("N4 K-infinity-Copy: the same NOT nflip in the relations of cnot (landed cnot_relT, cnot_relC) and of cnotTw (N2)",
      relT and relC and "theorem cnot_relT (ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω := by" in CD
      and "theorem cnot_relC (ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω) := by" in CD)

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- q4_pair_gates: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q4-PAIR-GATES-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
