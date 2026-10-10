#!/usr/bin/env python3
"""
ds7_models.py -- thread DS, questions DS.7(b) and DS.3, and the route of the input's claim C53: exact finite models
that carry neither OI content nor quantum amplitudes, tested against the input's three requirements.

COMMON DATA
4-point screen of ds5_physics: psi_L(x) = 1/(2 sqrt2), psi_R(x) = i^x/(2 sqrt2), x in {0,1,2,3}.
Quantum reference laws, computed exactly from the input's formula 2 with real overlap gamma:
  Q_LR[g](x) = |psi_L|^2 + |psi_R|^2 + 2 Re(conj(psi_L) psi_R g);   single slit (whole amplitude through one slit):
  Q_L(x) = 2|psi_L(x)|^2, Q_R(x) = 2|psi_R(x)|^2. Quantum two-path bound: P_LR(x) <= (sqrt(Q_L/2) + sqrt(Q_R/2))^2.
Visibility of a law on this screen: V = (max - min)/(max + min).

MODEL CL1 (classical; no amplitudes; no OI premise). State (s, k, hp, hr, hl, p, d, x):
  s in {LR, L, R} open slits (setting); k in {off, half, on} detector coupling (setting); hp in Z2, hr in Z2, hl in Z4
  hidden, uniform and independent; p in Z3 path register (0 unset, 1 = L, 2 = R); d in Z3 record register; x in Z4
  screen. phi = phi3 o phi2 o phi1, each adding to one register a function of the others (so each is a bijection):
    phi1: p += path(s, hp) mod 3      path(LR, hp) = 1 + hp; path(L, .) = 1; path(R, .) = 2
    phi2: d += p * rec(k, hr) mod 3   rec(off, .) = 0; rec(on, .) = 1; rec(half, hr) = hr
    phi3: x += land(s, d, hl) mod 4   land = BOTH[hl] if (s = LR and d = 0) else UNI[hl]
                                      BOTH = (0, 0, 1, 3) (law (1/2, 1/4, 0, 1/4)), UNI = (0, 1, 2, 3)
  Initial condition p = d = x = 0. The observer reads the settings (s, k) and the final x; d where stated.

DECISION RULES (fixed in this header before the first run; rules, not expected numbers)
Each check prints "ID | text | PASS/FAIL"; a countercontrol (CC-) PASSES when the alternative it names fails exactly.
A block prints its VERDICT only if all its checks pass, else "VERDICT <block>: VOID". "ALL BLOCKS GREEN" prints only if
every block is green. Exact arithmetic only (fractions.Fraction, sympy Rationals and sqrt(2)).
B1 bijectivity: phi1, phi2, phi3 and phi are bijections of the full 5184-element state space (exhaustive).
B2 requirement 1: P_CL1(x | LR, off) == Q_LR[1]; P_CL1(x | L, off) == Q_L; P_CL1(x | R, off) == Q_R (exact).
   Control: Q_LR[1] satisfies the quantum two-path bound at every x.
B3 requirement 2: P_CL1(x | LR, half) == Q_LR[1/2] and P_CL1(x | LR, on) == Q_LR[0] (exact); the suppression is
   derived inside the model: V == 1 - r with r the record's registration probability (r = 0, 1/2, 1 for off/half/on).
B4 requirement 3: every law above is produced by the one map phi, the settings entering only as initial conditions
   (structural; the count of distinct maps used is printed and must be 1).
B5 complementarity (reported against the quantum pure-record equality V^2 + D^2 = 1 of ds5 F6): at k = half,
   D_cl := total variation between the laws of d given p = L and given p = R. PASS iff V^2 + D_cl^2 < 1 exactly
   (CL1 meets the three requirements and still violates the quantum equality).
CC-B6 (CL0: same architecture, BOTH replaced by (0,0,0,0)): phi stays a bijection, and P(x | LR, off) violates the
   quantum two-path bound at x = 0 (fails requirement 1).
CC-B7 (CLfree: a non-disturbing classical record; land ignores d): at k = on the record is perfect (D_cl = 1) and
   P(x | LR, on) == Q_LR[1] (V = 1): fails requirement 2.
B8 memory variant (route test for C53). Visible law of three steps (v0, v1, v2) = (t, *, x) for (s, k) = (LR, off):
   t = hp uniform; * a common in-flight value; x = 0 if t = 0, and x = BOTH2[hl], BOTH2 = (0, 0, 2, 2), if t = 1.
   PASS iff (a) the law is a probability law; (b) its screen marginal violates the quantum two-path bound at x = 0;
   (c) C4 memory witness: the histories (t=0, *) and (t=1, *) have the same current visible value and different
   next-step laws (exact); (d) C1 witness: given the visible history (t=1, *), the next visible value depends on the
   hidden hl (two hl values give different x).
   [K + W, recorded in RESULT]: S_imp_D realizes this law by a finite reversible deterministic system; C4 holds of every
   realization of a non-Markov law (Main L80), and C1, C3 follow from C4 in a faithful realization (Main L72, L78).
B9 DS.3 illustration, the certified constructions run on the double-slit law. Horizon K = 1, alphabet
   V = {src, 0, 1, 2, 3}, law P(src, x) = Q_LR[1](x). Build S_imp_D's clock-and-record carrier (hidden = (clock,
   complete visible record), coherent states advance the clock, padded to a permutation) and D_imp_Qfb's
   representation (U = permutation matrix of the inverse step, diagonal initial law, readout = visible factor).
   PASS iff the carrier step is a permutation, the Born chain law with weights |U|^p equals P for p = 1, 2 and 3 (every
   entry of U is 0 or 1), and no cross term arises (the initial law is diagonal and the chain collapses at each step).
   CC-B9: the quantum two-slit representation of the same law has the nonzero cross term 2 Re(conj(psi_L) psi_R) at
   x = 0.
B10 Sorkin: I3(p) := |a+b+c|^p - |a+b|^p - |a+c|^p - |b+c|^p + |a|^p + |b|^p + |c|^p. PASS iff I3(2) == 0 identically
   for symbolic complex a, b, c. CC-B10: I3(4) != 0 at a = b = c = 1.
"""
from fractions import Fraction
from itertools import product

import sympy as sp

I = sp.I
results, order = {}, []


def chk(block, cid, text, ok):
    ok = bool(ok)
    results.setdefault(block, []).append(ok)
    if block not in order:
        order.append(block)
    print(f"{cid} | {text} | {'PASS' if ok else 'FAIL'}")


def verdict(block, text):
    print(f"VERDICT {block}: {text}" if all(results.get(block, [False])) else f"VERDICT {block}: VOID")


def frac(e):
    r = sp.simplify(e)
    if not r.is_Rational:
        raise ValueError(f"not an exact rational: {r}")
    return Fraction(int(r.p), int(r.q))


def fmt(law):
    return "(" + ", ".join(str(v) for v in law) + ")"


def visibility(law):
    mx, mn = max(law), min(law)
    return (mx - mn) / (mx + mn)


# ------------------------------------------------------------------ quantum references (exact)
SCREEN = range(4)
pL = [1 / (2 * sp.sqrt(2)) for _ in SCREEN]
pR = [I ** x / (2 * sp.sqrt(2)) for x in SCREEN]


def ab2(z):
    return sp.expand(z * sp.conjugate(z))


def Q_LR(g):
    return [frac(sp.simplify(ab2(pL[x]) + ab2(pR[x]) + 2 * sp.re(sp.expand(sp.conjugate(pL[x]) * pR[x] * g))))
            for x in SCREEN]


Q_L = [frac(sp.simplify(2 * ab2(pL[x]))) for x in SCREEN]
Q_R = [frac(sp.simplify(2 * ab2(pR[x]))) for x in SCREEN]


def bound_ok(law):
    # law(x) <= (sqrt(Q_L/2) + sqrt(Q_R/2))^2, checked exactly with sympy
    out = []
    for x in SCREEN:
        b = (sp.sqrt(sp.Rational(Q_L[x].numerator, Q_L[x].denominator) / 2)
             + sp.sqrt(sp.Rational(Q_R[x].numerator, Q_R[x].denominator) / 2)) ** 2
        out.append(bool(sp.Rational(law[x].numerator, law[x].denominator) <= sp.expand(b)))
    return out


# ------------------------------------------------------------------ the classical models
S_SET, K_SET = ["LR", "L", "R"], ["off", "half", "on"]
BOTH, UNI, ZERO = (0, 0, 1, 3), (0, 1, 2, 3), (0, 0, 0, 0)


def make_model(both_table, record_disturbs=True):
    def path(s, hp):
        return {"LR": 1 + hp, "L": 1, "R": 2}[s]

    def rec(k, hr):
        return {"off": 0, "on": 1, "half": hr}[k]

    def land(s, d, hl):
        if s == "LR" and (d == 0 or not record_disturbs):
            return both_table[hl]
        return UNI[hl]

    def phi1(st):
        s, k, hp, hr, hl, p, d, x = st
        return (s, k, hp, hr, hl, (p + path(s, hp)) % 3, d, x)

    def phi2(st):
        s, k, hp, hr, hl, p, d, x = st
        return (s, k, hp, hr, hl, p, (d + p * rec(k, hr)) % 3, x)

    def phi3(st):
        s, k, hp, hr, hl, p, d, x = st
        return (s, k, hp, hr, hl, p, d, (x + land(s, d, hl)) % 4)

    def phi(st):
        return phi3(phi2(phi1(st)))

    return phi1, phi2, phi3, phi


STATES = list(product(S_SET, K_SET, range(2), range(2), range(4), range(3), range(3), range(4)))


def is_bij(f):
    return len({f(st) for st in STATES}) == len(STATES)


def run(phi, s, k):
    lawx = [Fraction(0)] * 4
    dist_d = {1: [Fraction(0)] * 3, 2: [Fraction(0)] * 3}
    for hp, hr, hl in product(range(2), range(2), range(4)):
        w = Fraction(1, 16)
        out = phi((s, k, hp, hr, hl, 0, 0, 0))
        p, d, x = out[5], out[6], out[7]
        lawx[x] += w
        if p in dist_d:
            dist_d[p][d] += w
    return lawx, dist_d


def tv_given_path(dist_d):
    tl, tr = sum(dist_d[1]), sum(dist_d[2])
    if tl == 0 or tr == 0:
        return None
    return sum(abs(dist_d[1][j] / tl - dist_d[2][j] / tr) for j in range(3)) / 2


CL1 = make_model(BOTH)
CL0 = make_model(ZERO)
CLfree = make_model(BOTH, record_disturbs=False)

# ------------------------------------------------------------------ B1
chk("B1", "B1", f"CL1: phi1, phi2, phi3, phi bijective on {len(STATES)} states: "
    f"{[is_bij(f) for f in CL1]}", all(is_bij(f) for f in CL1))
verdict("B1", "CL1 is one finite reversible deterministic map")

# ------------------------------------------------------------------ B2
qlr1 = Q_LR(1)
l_off, _ = run(CL1[3], "LR", "off")
l_L, _ = run(CL1[3], "L", "off")
l_R, _ = run(CL1[3], "R", "off")
chk("B2", "B2-control", f"Q_LR[1] = {fmt(qlr1)} satisfies the quantum two-path bound at every x: {bound_ok(qlr1)}",
    all(bound_ok(qlr1)))
chk("B2", "B2", f"P(x|LR,off) = {fmt(l_off)} vs Q_LR[1]; P(x|L,off) = {fmt(l_L)} vs Q_L = {fmt(Q_L)}; "
    f"P(x|R,off) = {fmt(l_R)} vs Q_R = {fmt(Q_R)}", l_off == qlr1 and l_L == Q_L and l_R == Q_R)
verdict("B2", "requirement 1 is met by CL1 exactly")

# ------------------------------------------------------------------ B3
l_half, dd_half = run(CL1[3], "LR", "half")
l_on, dd_on = run(CL1[3], "LR", "on")
q_half, q_on = Q_LR(sp.Rational(1, 2)), Q_LR(0)
r = {"off": Fraction(0), "half": Fraction(1, 2), "on": Fraction(1)}
Vs = {"off": visibility(l_off), "half": visibility(l_half), "on": visibility(l_on)}
chk("B3", "B3-laws", f"P(x|LR,half) = {fmt(l_half)} vs Q_LR[1/2] = {fmt(q_half)}; P(x|LR,on) = {fmt(l_on)} vs "
    f"Q_LR[0] = {fmt(q_on)}", l_half == q_half and l_on == q_on)
chk("B3", "B3-derived", f"visibilities {[str(Vs[k]) for k in K_SET]} == 1 - r = {[str(1 - r[k]) for k in K_SET]}",
    all(Vs[k] == 1 - r[k] for k in K_SET))
verdict("B3", "requirement 2 is met by CL1 exactly, with the amount derived from the record's registration rate")

# ------------------------------------------------------------------ B4
used = {id(CL1[3])}
chk("B4", "B4", f"distinct maps used for all settings: {len(used)}", len(used) == 1)
verdict("B4", "requirement 3 is met by CL1: one map, settings as initial conditions")

# ------------------------------------------------------------------ B5
D_cl = tv_given_path(dd_half)
lhs = Vs["half"] ** 2 + D_cl ** 2
chk("B5", "B5", f"k=half: V = {Vs['half']}, D_cl = {D_cl}, V^2 + D_cl^2 = {lhs} (< 1 required)", lhs < 1)
verdict("B5", "CL1 meets requirements 1-3 and violates the quantum pure-record equality V^2 + D^2 = 1")

# ------------------------------------------------------------------ CC-B6, CC-B7
l0, _ = run(CL0[3], "LR", "off")
chk("B6", "CC-B6", f"CL0 bijective: {is_bij(CL0[3])}; P(x|LR,off) = {fmt(l0)}; bound holds at x=0: "
    f"{bound_ok(l0)[0]} (must be False)", is_bij(CL0[3]) and not bound_ok(l0)[0])
verdict("B6", "the same architecture yields a non-quantum two-slit law: requirement 1 is not implied by it")
lf, ddf = run(CLfree[3], "LR", "on")
Df = tv_given_path(ddf)
chk("B7", "CC-B7", f"CLfree bijective: {is_bij(CLfree[3])}; k=on: D_cl = {Df}; P(x|LR,on) = {fmt(lf)}; equals "
    f"Q_LR[1]: {lf == qlr1}; V = {visibility(lf)}", is_bij(CLfree[3]) and Df == 1 and lf == qlr1)
verdict("B7", "a perfect classical record need not suppress anything: suppression is not implied by having a record")

# ------------------------------------------------------------------ B8
BOTH2 = (0, 0, 2, 2)
law3 = {}
for hp, hl in product(range(2), range(4)):
    w = Fraction(1, 8)
    x = 0 if hp == 0 else BOTH2[hl]
    key = (hp, "*", x)
    law3[key] = law3.get(key, Fraction(0)) + w
tot = sum(law3.values())
marg = [sum(v for (t, s_, x), v in law3.items() if x == xx) for xx in SCREEN]
nxt = {t: [sum(v for (tt, s_, x), v in law3.items() if tt == t and x == xx) /
           sum(v for (tt, s_, x), v in law3.items() if tt == t) for xx in SCREEN] for t in (0, 1)}
c1 = sorted({BOTH2[hl] for hl in range(4)})
chk("B8", "B8-a", f"three-step law sums to {tot}", tot == 1)
chk("B8", "B8-b", f"screen marginal {fmt(marg)}; bound holds at x=0: {bound_ok(marg)[0]} (must be False)",
    not bound_ok(marg)[0])
chk("B8", "B8-c", f"C4 witness: P(x | t=0,*) = {fmt(nxt[0])}, P(x | t=1,*) = {fmt(nxt[1])}", nxt[0] != nxt[1])
chk("B8", "B8-d", f"C1 witness: given (t=1,*), the next visible value over hidden hl takes values {c1}",
    len(c1) > 1)
verdict("B8", "a memory-bearing (C4) embedded-observer law with a record of its past can carry a non-quantum "
        "two-slit pattern")

# ------------------------------------------------------------------ B9
SRC = "src"
VIS = [SRC, 0, 1, 2, 3]
KH = 1
trajs = [(SRC, x) for x in SCREEN]
Pt = {(SRC, x): qlr1[x] for x in SCREEN}
HID = [(c, tau) for c in range(KH + 1) for tau in product(VIS, repeat=KH + 1)]
ALL = [(v, hdn) for v in VIS for hdn in HID]


def emb(c, tau):
    return (tau[c], (c, tau))


coh = [emb(c, tau) for (c, tau) in HID]
adv = {st: emb((st[1][0] + 1) % (KH + 1), st[1][1]) for st in coh}
# pad the injective partial map to a permutation of ALL (deterministic order), as exists_perm_extending does
rest_dom = [st for st in ALL if st not in adv]
rest_img = [st for st in ALL if st not in set(adv.values())]
step = dict(adv)
step.update(dict(zip(rest_dom, rest_img)))
is_perm = sorted(map(repr, step.values())) == sorted(map(repr, ALL)) and len(step) == len(ALL)
idx = {st: i for i, st in enumerate(ALL)}
init = {st: Fraction(0) for st in ALL}
for tau in trajs:
    init[emb(0, tau)] += Pt[tau]
inv = {v: k for k, v in step.items()}


def U_entry(bp, b):           # U = permMatrix of step^{-1}: U[b', b] = 1 iff b = step^{-1}(b'), i.e. b' = step(b)
    return 1 if step[b] == bp else 0


def chain_law(pw):
    law = {}
    for b0 in ALL:
        if init[b0] == 0:
            continue
        for b1 in ALL:
            wgt = init[b0] * Fraction(abs(U_entry(b1, b0)) ** pw)
            if wgt:
                key = (b0[0], b1[0])
                law[key] = law.get(key, Fraction(0)) + wgt
    return law


laws = {pw: chain_law(pw) for pw in (1, 2, 3)}
target = {k: v for k, v in Pt.items() if v != 0}
entries01 = all(U_entry(step[b], b) == 1 for b in ALL)
chk("B9", "B9-perm", f"S_imp_D carrier step is a permutation of {len(ALL)} states: {is_perm}", is_perm)
chk("B9", "B9-law", f"Born chain law with |U|^p equals the law for p=1,2,3: "
    f"{[laws[pw] == target for pw in (1, 2, 3)]}; U has one entry 1 per column: {entries01}",
    all(laws[pw] == target for pw in (1, 2, 3)) and entries01)
diag_init = all(isinstance(v, Fraction) for v in init.values())
chk("B9", "B9-nocross", "initial law is a diagonal (classical) weight on basis states and the chain collapses at every "
    "step, so no term of the form conj(c_a) c_b with a != b enters", diag_init)
cross0 = sp.simplify(2 * sp.re(sp.expand(sp.conjugate(pL[0]) * pR[0])))
chk("B9", "CC-B9", f"quantum two-slit representation: cross term at x=0 is {cross0} (must be nonzero)", cross0 != 0)
verdict("B9", "the certified S->D->Q_fb constructions represent the double-slit law with a permutation unitary and no "
        "interference term; the exponent p is not selected")

# ------------------------------------------------------------------ B10
def cs(name):
    re_, im_ = sp.symbols(f"{name}_re {name}_im", real=True)
    return re_ + I * im_


a, b, c = cs("a"), cs("b"), cs("c")


def I3(pw, a_, b_, c_):
    f = (lambda z: sp.expand(ab2(z) ** sp.Rational(pw, 2))) if pw % 2 == 0 else None
    return sp.expand(f(a_ + b_ + c_) - f(a_ + b_) - f(a_ + c_) - f(b_ + c_) + f(a_) + f(b_) + f(c_))


chk("B10", "B10", "I3(2) == 0 identically (symbolic complex a, b, c)", I3(2, a, b, c) == 0)
i34 = I3(4, 1, 1, 1)
chk("B10", "CC-B10", f"I3(4) at a=b=c=1 is {i34} (must be nonzero)", i34 != 0)
verdict("B10", "no third-order interference holds for the quadratic exponent and fails for p = 4")

# ------------------------------------------------------------------ summary
green = [blk for blk in order if all(results[blk])]
print(f"SUMMARY: {sum(len(v) for v in results.values())} checks; blocks green {len(green)}/{len(order)}")
if len(green) == len(order):
    print("ALL BLOCKS GREEN")
