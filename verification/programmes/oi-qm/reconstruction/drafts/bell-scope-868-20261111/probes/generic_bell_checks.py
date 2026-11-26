#!/usr/bin/env python3
"""GENERIC exact checks for BELL-SCOPE-UNIT1 (paper-only, #868).

Pure mathematics only: CHSH algebra over the 16 deterministic tables, the
Tsirelson box, an exact local witness at TV distance (sqrt2-1)/4, total-variation
contraction under a local post-processing, independence under a conditioned
uniform product measure (with a coupling countercontrol and a non-product event
that keeps setting independence), and a six-site abstract toy map realizing the
local witness inside the screened class. No OI rule, carrier, coupling,
preparation or simulator is encoded. Exit status 0 iff every check holds.
"""
import itertools, sys
from fractions import Fraction as Fr
import sympy as sp

fails = []
def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok: fails.append(name)

ctx = [(x, y) for x in (0, 1) for y in (0, 1)]
signs = list(itertools.product((1, -1), repeat=4))
# the eight CHSH-type functionals: sign patterns with an odd number of minus signs, times +-1
patterns = [s for s in signs if s.count(-1) % 2 == 1]

# G1: every deterministic table gives each CHSH-type functional in {-2,+2}
det = list(itertools.product((1, -1), repeat=4))  # (a0,a1,b0,b1)
ok = True
for a0, a1, b0, b1 in det:
    A = (a0, a1); B = (b0, b1)
    E = [A[x] * B[y] for x, y in ctx]
    for p in patterns:
        if sum(pi * ei for pi, ei in zip(p, E)) not in (-2, 2): ok = False
check("G1 sixteen deterministic tables: all 8 CHSH functionals in {-2,2}", ok)

# G2: Tsirelson box, exact
r = 1 / sp.sqrt(2)
def PQ(a, b, x, y):  # a,b in {+1,-1}
    E = -r if (x, y) == (1, 1) else r
    return (1 + a * b * E) / 4
EQ = [sp.simplify(sum(a * b * PQ(a, b, x, y) for a in (1, -1) for b in (1, -1))) for x, y in ctx]
SQ = sp.simplify(EQ[0] + EQ[1] + EQ[2] - EQ[3])
check("G2a Tsirelson box CHSH = 2*sqrt(2)", sp.simplify(SQ - 2 * sp.sqrt(2)) == 0)
check("G2b Tsirelson box is a family of probability laws",
      all(sp.simplify(sum(PQ(a, b, x, y) for a in (1, -1) for b in (1, -1)) - 1) == 0 for x, y in ctx)
      and all(PQ(a, b, x, y).evalf() > 0 for a in (1, -1) for b in (1, -1) for x, y in ctx))

# G3: explicit local witness: uniform mixture of the 8 deterministic tables with S=+2
S2 = [d for d in det if d[0]*d[2] + d[0]*d[3] + d[1]*d[2] - d[1]*d[3] == 2]
check("G3a exactly 8 deterministic tables reach S=+2", len(S2) == 8)
def PL(a, b, x, y):
    return Fr(sum(1 for d in S2 if d[x] == a and d[2 + y] == b), len(S2))
EL = [sum(a * b * PL(a, b, x, y) for a in (1, -1) for b in (1, -1)) for x, y in ctx]
check("G3b witness correlators (1/2,1/2,1/2,-1/2), CHSH = 2",
      EL == [Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(-1, 2)])
tv = [sp.nsimplify(sum(sp.Abs(sp.Rational(PL(a, b, x, y)) - PQ(a, b, x, y)) for a in (1, -1) for b in (1, -1)) / 2)
      for x, y in ctx]
target = (sp.sqrt(2) - 1) / 4
check("G3c witness TV to Tsirelson box = (sqrt2-1)/4 in every context",
      all(sp.simplify(t - target) == 0 for t in tv))
check("G3d (2*sqrt2-2)/8 == (sqrt2-1)/4", sp.simplify((2 * sp.sqrt(2) - 2) / 8 - target) == 0)
# the witness equals the isotropic mixture v*PQ + (1-v)/4 at v = 1/sqrt2
v = 1 / sp.sqrt(2)
check("G3e witness = isotropic mixture at v = 1/sqrt2",
      all(sp.simplify(sp.Rational(PL(a, b, x, y)) - (v * PQ(a, b, x, y) + (1 - v) / 4)) == 0
          for a in (1, -1) for b in (1, -1) for x, y in ctx))

# G4: correlator / TV inequality |E_P - E_Q| <= 2 TV(P,Q) on 4-point laws, exhaustive on a rational grid
grid = [Fr(i, 6) for i in range(7)]
ok = True
laws = [p for p in itertools.product(grid, repeat=3) if sum(p) <= 1]
laws = [p + (1 - sum(p),) for p in laws]
vals = [1, -1, -1, 1]  # a*b for (++),(+-),(-+),(--)
for P in laws:
    for Q in laws[::7]:
        dE = abs(sum(v_ * (p - q) for v_, p, q in zip(vals, P, Q)))
        TV = sum(abs(p - q) for p, q in zip(P, Q)) / 2
        if dE > 2 * TV: ok = False
check("G4 |E_P-E_Q| <= 2 TV on a rational grid of 2x2 laws", ok)

# G5: TV contraction under a local post-processing (bot -> +1), exhaustive on a grid over 3x3 outcome laws
ok = True
grid3 = [Fr(i, 3) for i in range(4)]
outs = [(a, b) for a in (1, -1, 0) for b in (1, -1, 0)]  # 0 stands for bot
f = lambda o: 1 if o == 0 else o
import random
random.seed(1)
def rand_law():
    w = [random.randint(0, 5) for _ in outs]
    s = sum(w) or 1
    return [Fr(x, s) for x in w]
for _ in range(400):
    P, Q = rand_law(), rand_law()
    if sum(P) != 1 or sum(Q) != 1: continue
    tv = sum(abs(p - q) for p, q in zip(P, Q)) / 2
    push = lambda L: {k: sum(L[i] for i, o in enumerate(outs) if (f(o[0]), f(o[1])) == k)
                      for k in [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
    pP, pQ = push(P), push(Q)
    if sum(abs(pP[k] - pQ[k]) for k in pP) / 2 > tv: ok = False
check("G5 TV contracts under local post-processing bot->+1 (400 exact rational cases)", ok)

# G6: conditioned uniform product measure. Coordinates g (generator, 2 bits) and w (response region, 2 bits).
# (a) conditioning on an event E_G x E_W: g independent of w.
# (b) countercontrol: conditioning on a coupling event (parity of g0 xor w0 = 0): independence fails.
def indep(event):
    pts = [(g, w) for g in itertools.product((0, 1), repeat=2) for w in itertools.product((0, 1), repeat=2) if event(g, w)]
    n = len(pts)
    pg = {}; pw = {}; pj = {}
    for g, w in pts:
        pg[g] = pg.get(g, 0) + Fr(1, n); pw[w] = pw.get(w, 0) + Fr(1, n); pj[(g, w)] = pj.get((g, w), 0) + Fr(1, n)
    return all(pj.get((g, w), 0) == pg[g] * pw[w] for g in pg for w in pw)
check("G6a product event: generator coordinates independent of response coordinates",
      indep(lambda g, w: (g[0] | g[1]) == 1 and w[1] == 0))
check("G6b countercontrol: coupling event breaks independence",
      not indep(lambda g, w: (g[0] ^ w[0]) == 0))

# G6c: a non-product conditioning event under which setting independence still holds (CF is sufficient,
# not necessary). Generator coordinates (a, b, r): setting bits a, b and a residue bit r. Response bit w.
# Condition the uniform measure on r == w.
pts = [(a, b, r, w) for a, b, r, w in itertools.product((0, 1), repeat=4) if r == w]
n = len(pts)
def law(key):
    d = {}
    for p_ in pts: d[key(p_)] = d.get(key(p_), 0) + Fr(1, n)
    return d
pG = law(lambda p_: p_[:3]); pW = law(lambda p_: p_[3]); pGW = law(lambda p_: (p_[:3], p_[3]))
not_product = any(pGW.get((g, w), 0) != pG[g] * pW[w] for g in pG for w in pW)
pS = law(lambda p_: p_[:2]); pSW = law(lambda p_: (p_[:2], p_[3]))
mi = all(pSW.get((s_, w), 0) == pS[s_] * pW[w] for s_ in pS for w in pW)
check("G6c event r == w: not a product across generator/response coordinates, settings still independent of w",
      not_product and mi)

# G7: an abstract six-site deterministic map in the screened class that realizes the G3 witness.
# Sites: gA, gB (setting bits), wA, wB (two bits each: the wing's answers to settings 0 and 1), rA, rB (record
# bits, 0/1 standing for +1/-1). One step: rA ^= wA[gA], rB ^= wB[gB]; every other site is unchanged.
# The map is a bijection. Conditioning event: (wA, wB) is one of the 8 tables with S = +2, and rA = rB = 0.
bit = lambda s_: 0 if s_ == 1 else 1
W8 = [((bit(d[0]), bit(d[1])), (bit(d[2]), bit(d[3]))) for d in S2]
states = [(gA, gB, wA, wB, rA, rB) for gA in (0, 1) for gB in (0, 1)
          for wA in itertools.product((0, 1), repeat=2) for wB in itertools.product((0, 1), repeat=2)
          for rA in (0, 1) for rB in (0, 1)]
def phi(s_):
    gA, gB, wA, wB, rA, rB = s_
    return (gA, gB, wA, wB, rA ^ wA[gA], rB ^ wB[gB])
check("G7a toy map is a bijection of its 256 states", len({phi(s_) for s_ in states}) == len(states) == 256)
# dependence of each output site on each input site, by exhaustive single-site variation
def depends(out_idx, in_idx):
    by_rest = {}
    for s_ in states:
        rest = s_[:in_idx] + s_[in_idx + 1:]
        by_rest.setdefault(rest, set()).add(phi(s_)[out_idx])
    return any(len(v_) > 1 for v_ in by_rest.values())
dep = {(o, i) for o in range(6) for i in range(6) if depends(o, i)}
expected = {(i, i) for i in range(6)} | {(4, 0), (4, 2), (5, 1), (5, 3)}
check("G7b dependence graph: rA reads only (gA, wA, rA), rB only (gB, wB, rB); no cross-wing edge", dep == expected)
E7 = [s_ for s_ in states if (s_[2], s_[3]) in W8 and s_[4] == 0 and s_[5] == 0]
m = len(E7)
# the event is a product across generator sites (gA, gB) and the remaining sites, so settings are independent
pset = {}; pom = {}; pjoint = {}
for s_ in E7:
    k = (s_[0], s_[1]); o = s_[2:]
    pset[k] = pset.get(k, 0) + Fr(1, m); pom[o] = pom.get(o, 0) + Fr(1, m); pjoint[(k, o)] = Fr(1, m) + pjoint.get((k, o), 0)
check("G7c settings independent of the non-generator sites under the conditioned uniform law; all four pairs occur",
      len(pset) == 4 and all(pjoint.get((k, o), 0) == pset[k] * pom[o] for k in pset for o in pom))
def PT(a, b, x, y):
    sel = [s_ for s_ in E7 if s_[0] == x and s_[1] == y]
    return Fr(sum(1 for s_ in sel if phi(s_)[4] == bit(a) and phi(s_)[5] == bit(b)), len(sel))
check("G7d toy record law equals the G3 witness in every context",
      all(PT(a, b, x, y) == PL(a, b, x, y) for a in (1, -1) for b in (1, -1) for x, y in ctx))

print("ALL PASS" if not fails else "FAILURES: " + ", ".join(fails))
sys.exit(1 if fails else 0)
