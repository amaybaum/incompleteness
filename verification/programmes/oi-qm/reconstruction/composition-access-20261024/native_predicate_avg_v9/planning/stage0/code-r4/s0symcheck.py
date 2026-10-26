"""Stage 0 control C0 (layer 1): symmetry group of v8's configuration space and the
counts and orbit counts of its record space, by direct canonicalization and by Burnside's
lemma. Configuration combinatorics only: no context, no closure, no law. Standard library,
exact integers. (r1 stage0-design/sym_check.py; design evidence for C0, not frozen code.)"""
from itertools import permutations, product


def ball(r):
    return [(x, y, z) for x in range(-r, r+1) for y in range(-(r-abs(x)), r-abs(x)+1)
            for z in range(-(r-abs(x)-abs(y)), r-abs(x)-abs(y)+1)]


def crystal(r):  # OEIS A001845, |l1 ball| in Z^3
    return (2*r+1)*(2*r*r+2*r+3)//3


OH = []
for perm in permutations(range(3)):
    for sg in product((1, -1), repeat=3):
        OH.append((perm, sg))


def act(g, c):
    perm, sg = g
    return tuple(sg[i]*c[perm[i]] for i in range(3))


Q9, Q8, Q10, M = (0, 0, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0)
OTHERS = ((1, 0, 0), (0, -1, 0), (0, 1, 0))
PORT = (0, 0, -3)
REG = set(ball(4))
PHI7 = {Q8, Q10, M, *OTHERS}


def stab(cond):
    return [g for g in OH if cond(g)]


geom_noport = stab(lambda g: {act(g, c) for c in REG} == REG and {act(g, c) for c in PHI7} == PHI7)
geom = stab(lambda g: g in geom_noport and act(g, PORT) == PORT)
labelled = stab(lambda g: g in geom and act(g, Q8) == Q8 and act(g, Q10) == Q10
                and {act(g, c) for c in (M, *OTHERS)} == {M, *OTHERS})
print('O_h order', len(OH))
print('masking geometry without port: order', len(geom_noport))
print('masking geometry with port (0,0,-3): order', len(geom))
print('labelled roles (q8, q10 fixed; m and others permuted): order', len(labelled))
assert all(len(ball(r)) == crystal(r) for r in range(12)), 'ball count vs A001845'
print('ball counts r=0..11 equal crystal-ball formula; |ball(4)|=%d |ball(8)|=%d' % (crystal(4), crystal(8)))

G = labelled
SITES = sorted(REG)
TIMES = range(-1, 24)
items = [(x, t) for x in SITES for t in TIMES]
print('items', len(items))
# Direct canonicalization of single items and unordered two-site pairs.
single_orbits = {min((act(g, x), t) for g in G) for x, t in items}
site_pairs = [(a, b) for i, a in enumerate(SITES) for b in SITES[i+1:]]
pair_orbits = set()
for a, b in site_pairs:
    imgs = [(act(g, a), act(g, b)) for g in G]
    for t1 in TIMES:
        for t2 in TIMES:
            pair_orbits.add(min(tuple(sorted(((ga, t1), (gb, t2)))) for ga, gb in imgs))
n_pairs = len(site_pairs)*len(TIMES)**2
print('records: singles', len(items), 'pairs', n_pairs)
# Burnside.
fix1 = sum(sum(1 for x in SITES if act(g, x) == x)*len(TIMES) for g in G)
fix2 = 0
for g in G:
    fixed_sites = [x for x in SITES if act(g, x) == x]
    nf = len(fixed_sites)
    fix2 += (nf*(nf-1)//2)*len(TIMES)**2           # both fixed
    swaps = sum(1 for x in SITES if act(g, x) != x and act(g, act(g, x)) == x)//2
    fix2 += swaps*len(TIMES)                          # swapped, equal times
assert fix1 % len(G) == 0 and fix2 % len(G) == 0
print('single orbits: direct', len(single_orbits), 'Burnside', fix1//len(G))
print('pair orbits:   direct', len(pair_orbits), 'Burnside', fix2//len(G))
assert len(single_orbits) == fix1//len(G) and len(pair_orbits) == fix2//len(G)
