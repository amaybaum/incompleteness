"""Exact geometry and independent finite controls for the unprepared junction.
Standard library; no imports from the inherited dynamics or no-carry model.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
import json

ROOT = Path(__file__).resolve().parents[1]
T = 185
P = 12 * 840 ** T
S = T + P
D = 68
R = S + D
N = R + 3
s = (0, S - 1, D + 2)
f = (0, -D - 4, D + 2)
STEPS = tuple(tuple(sign if j == axis else 0 for j in range(3))
              for axis in range(3) for sign in (-1, 1))

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def add(v, w):
    return tuple(a + b for a, b in zip(v, w))

def dist(v, w):
    return sum(abs(a - b) for a, b in zip(v, w))

def h(v):
    a, b, d = v
    return b, d, a ^ (b & d)

def xor(*values):
    result = [0, 0, 0]
    for value in values:
        for j in range(3):
            result[j] ^= value[j]
    return tuple(result)

states = tuple(product((0, 1), repeat=3))
need(add(f, (0, N, 0)) == s, 'unique positive-y axial path')
need(dist(f, s) == N, 'terminal first-arrival time')
q_y = (0, S, D)
q2 = (0, S, D + 2)
q3 = (0, S, D + 3)
need(dist(f, q_y) == R + 6, 'qY exclusion')
need(dist(f, q2) == R + 4, 'q2 exclusion')
need(dist(f, q3) == R + 5, 'optional q3 extension exclusion')
ports = [(0, T, 0), (T, 0, 0), (-T, 0, 0), (4*T, 0, 0), (0, 0, -8*T)]
balls = [('original-' + str(i), q, T) for i, q in enumerate(ports)]
balls += [('transport-' + str(i), add(q, (0, P, 0)), S)
          for i, q in enumerate(ports[:4])]
balls += [('Y-collision', q_y, R), ('R-collision', (0, S, -D), R),
          ('q2', q2, R+2), ('q3-optional', q3, R+3),
          ('remote-herald', (12*R, 0, 0), R), ('remote-Z', (-12*R, 0, 0), R)]
need(len(balls) == 15, 'ready ball inventory')
for name, center, radius in balls:
    need(dist(f, center) > radius, 'free pivot was pinned by ' + name)
need(min(dist(f, q)-radius for _, q, radius in balls) == 2, 'minimum slack')
geometry = json.loads((ROOT / 'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())
need(len(geometry['sources']) == 1479, 'source count')
need(all(tuple(src['position']) != f for src in geometry['sources']), 'old source exception')
controls = [(0, 2*S, 0), (T, P+S, 0), (-T, P+S, 0), (4*T, P+S, 0),
            (0, S, S+2*D), (0, S, -S-2*D)]
need(f not in controls and f[0] < 12*R, 'new source exceptions')
print('J1: actual giant-integer geometry; pivot outside all15 ready balls and1479 original sources: PASS')

# At the final update only the -y neighbor can already depend on this pivot.
for e in STEPS:
    need(dist(f, add(s, e)) == (N-1 if e == (0, -1, 0) else N+1), 'last-neighbor distances')
need(dist(f, s) > N-2, 'old slice independent of pivot')
# An arbitrary full background supplies offsets a,b. No field is dropped.
for a, b in product(states, repeat=2):
    images = [xor(a, h(xor(m, b))) for m in states]
    need(len(set(images)) == 8, 'translated H must be a permutation')
print('J2: full native update has64 bijective offset maps; only one final neighbor carries the fresh pivot: PASS')

# Eight initial values of the pivot are evolved simultaneously in bit lanes.
ALL = 255
PIVOT = (240, 204, 170)
def scalar(v, lane):
    return tuple((field >> lane) & 1 for field in v)

def background(t, v, seed):
    a, b, c = v
    value = ((a*17+b*31+c*43+seed*59+t*71) ^
             ((a*a+3*b*b+5*c*c+7*seed+11*t) << 2)) & 7
    return tuple(ALL if value & (1 << (2-j)) else 0 for j in range(3))

def dynamics(seed):
    @lru_cache(None)
    def at(t, v):
        if t == 0 and v == (0, 0, 0):
            return PIVOT
        if t in (-1, 0):
            return background(t, v, seed)
        return xor(at(t-2, v), h(xor(*(at(t-1, add(v, e)) for e in STEPS))))
    return at

comparisons = 0
nontrivial_offsets = 0
for seed in range(3):
    at = dynamics(seed)
    for direction in STEPS:
        simple = PIVOT
        for k in range(1, 9):
            v = tuple(k*a for a in direction)
            old = at(k-2, v)
            others = xor(*(at(k-1, add(v, e)) for e in STEPS
                           if e != tuple(-a for a in direction)))
            need(all(field in (0, ALL) for field in old + others), 'off-path term depends on pivot')
            prior = at(k-1, tuple((k-1)*a for a in direction))
            actual = at(k, v)
            need(actual == xor(old, h(xor(prior, others))), 'complete recurrence')
            need(len({scalar(actual, lane) for lane in range(8)}) == 8, 'direct dense-background permutation')
            simple = h(simple)
            nontrivial_offsets += actual != simple
            comparisons += 1
need(nontrivial_offsets > 0, 'controls failed to distinguish omitted-background formula')
print('J3: %d direct 3-D dense-background first-arrival cases, all8 pivot values; omitted-background countercontrol: PASS' % comparisons)

# Distance alone is insufficient: two shortest paths cancel for an isolated pulse.
@lru_cache(None)
def isolated(t, v):
    if t < 0 or sum(map(abs, v)) > t:
        return (0, 0, 0)
    if t == 0:
        return PIVOT if v == (0, 0, 0) else (0, 0, 0)
    return xor(isolated(t-2, v), h(xor(*(isolated(t-1, add(v, e)) for e in STEPS))))
need(isolated(2, (1, 1, 0)) == (0, 0, 0), 'nonaxial countercontrol')
for x, y, a, b, d in product((0, 1), repeat=5):
    got = xor((0, 1^y, x), h((a, b, d)))
    need(got == (b, 1^y^d, x^a^(b&d)), 'sidecar junction identity')
print('J4: exact sidecar-plus-six-neighbor identity; nonaxial distance-only claim rejected: PASS')

# A blanket new cold ball conflicts with prior resources.
need(dist((0, -1, 0), s) == R+2, 'M1 captured')
need(dist((0, -2, 0), s) == R+3, 'M2 captured')
need(dist((0, 0, 0), s) == R+1, 'unknown old input captured by previous ball')
need((sum(s)+N) % 2 == 0, 'junction current-source parity')
need(sum((0, -2, 0)) % 2 == 0, 'M2 remains in active parity')
need(sum((0, -1, 0)) % 2 == 1, 'M1 opposite current parity')
need((sum((0, 0, 0))-1) % 2 == 1, 'old unknown opposite phase parity')
need(dist((0, -3, 0), s) == R+4, 'all further Mj outside')
print('J5: blanket ready extension captures old M1/M2 and unknown previous input; active-parity extension still captures M2: PASS')

# Proposed initial active-sector extension: six current-source exceptions.
# The formulas below also give the inequalities for every positive index.
for j in (1, 2, 3, D, P, R):
    need(dist((0, -j, 0), s)-N == j-2, 'old Mj slack')
    need(dist((0, 0, -9*T-j), s)-N == 9*T+j-2, 'old Nj slack')
for k in (1, 2, 3, D, P, R):
    for i, q in enumerate(ports[:4]):
        frontier = add(q, (0, P+S+k, 0))
        need(dist(frontier, s)-N == k+(3*T if i == 3 else 0), 'selector frontier slack')
inside = [src for src in geometry['sources'] if dist(tuple(src['position']), s) <= N]
need(len(inside) == 1 and inside[0]['position'] == [0, 0, 0], 'only old origin source inside')
need(dist(controls[0], s) == N and dist(controls[1], s) == N and dist(controls[2], s) == N, 'three selector exceptions on boundary')
need(dist(controls[3], s) == N+3*T, 'Z selector outside')
need(dist(controls[4], s) == N-4 and dist(controls[5], s) == N+2*D, 'upper/lower pulse distances')
need((S+1) & (D+2) == 2, 'isolated M2 no-carry obstruction')
need(64*R+64*T+1 > 2*N+1, 'local cone embeds in inherited odd torus')
print('J6: proposed initial active-sector cone preserves all reserved banks with M2 exception; isolated M2 front cancels, interaction law remains open: PASS')
print('SCOPE: the unchanged proposed junction has no deterministic raw operand or clean code for all allowed backgrounds. Uniform terminal marginal is not a joint-history law. A redesigned prepared junction remains open.')
