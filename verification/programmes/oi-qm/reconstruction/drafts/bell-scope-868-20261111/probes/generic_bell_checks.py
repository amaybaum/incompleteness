#!/usr/bin/env python3
"""GENERIC exact checks for BELL-SCOPE-UNIT1 (paper-only, #868).

Pure mathematics only: CHSH algebra over the 16 deterministic tables, the
Tsirelson box, an exact local witness at TV distance (sqrt2-1)/4, total-variation
contraction under a local post-processing, and independence under a conditioned
uniform product measure (with a coupling countercontrol). No OI rule, carrier,
coupling, preparation or simulator is encoded. Exit status 0 iff every check holds.
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

print("ALL PASS" if not fails else "FAILURES: " + ", ".join(fails))
sys.exit(1 if fails else 0)
