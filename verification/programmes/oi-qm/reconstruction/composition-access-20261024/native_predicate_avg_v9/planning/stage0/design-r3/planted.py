"""R3 design check (toys only): the planted family {q} plus all of q's near and far
axis tips as depth-0 quantities, for each convention (A: F and B types; G: F type,
placed outside a toy frame, and inside it as the vacuity contrast), depths 1-4,
against the correct rule and each rule mutant. Standard library."""
import sys
sys.path.insert(0, sys.argv[1])
from proto import Geometry, axes, add  # noqa: E402

D = 3
AX = axes(D)


def family(g, q):
    c, t = q
    d, ty = g.depth(q)
    near, far = g.slices(ty)
    fam = {q} | {(add(c, e, d), near) for e in AX}
    if d >= 1:
        fam |= {(add(c, e, d-1), far) for e in AX}
    return fam


def run(conv, eligible=None, centre=(0, 0, 0)):
    L = 4 if conv == 'A' else 0
    rules = {
        'correct': dict(far=True),
        'near-only L3': dict(far=False),
        'offaxis all': dict(offaxis='all'),
        'offaxis B-only': dict(offaxis='B'),
        'wrong far tip': dict(wrong_far=True),
        'symmetric radii': dict(symmetric=True),
        'swapped slices': dict(swap=True),
    }
    geos = {k: Geometry(D, L, eligible=eligible, **v) for k, v in rules.items()}
    gc = geos['correct']
    types = ('F', 'B') if conv == 'A' else ('F',)
    rows = []
    for ty in types:
        for d in range(1, 5):
            q = (centre, gc.L+d) if ty == 'F' else (centre, gc.E-d)
            fam = family(gc, q)
            out = {k: len(g.closure(set(), fam)) for k, g in geos.items()}
            rows.append((ty, d, len(fam), out))
    return rows


def show(title, rows):
    print(title)
    for ty, d, n, out in rows:
        print('  %s depth %d |family|=%2d  ' % (ty, d, n) + '  '.join('%s:%d' % (k, v) for k, v in out.items()))


show('Convention A (pair (3,4)), all tips eligible:', run('A'))
# Convention G: pair (-1, 0); toy frame = even cells |c|<=3 at slice 0 and odd |c|<=2 at slice -1.
R = 3


def in_frame(u):
    c, s = u
    n = sum(map(abs, c))
    return (s == 0 and n <= R and n % 2 == 0) or (s == -1 and n <= R-1 and n % 2 == 1)


show('Convention G, plant centred at (9,0,0), outside the toy frame (seed tips eligible):',
     run('G', eligible=lambda u: not in_frame(u), centre=(9, 0, 0)))
show('Convention G, plant centred at the origin, INSIDE the toy frame (vacuity contrast):',
     run('G', eligible=lambda u: not in_frame(u), centre=(0, 0, 0)))
