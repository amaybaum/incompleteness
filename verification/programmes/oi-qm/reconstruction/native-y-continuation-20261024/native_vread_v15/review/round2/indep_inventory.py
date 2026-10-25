"""Reviewer's independent inventory of fixed initial regions, from primary declarations.

Built from the prose/code specifications of the lineage, not from native_vread_v15's or
native_route_v13's ready list:
  junction_v4 REPORT section 1 table (15 base current regions with stated centres/radii),
  outward/reset chain q_k=(0,S,68+k) with deadline R+k up to q9 at L (history_v9 'B_L(q8)'
  at its L=R+8, branch_v10/history_v11 '(0,S,77),L'),
  herald_v10 herald/Z cones (|x|=48L, radius L),
  history_v9/history_v11 eight ports with deadlines and bank rays (deadline, 2L],
  native_seed_v12 q10 extension B_(R+10)(q10),
  source families: 1479 inherited table; junction_v4 controls (four selectors, two reset pulses);
  lower front O, W, E; upper cluster Q,C,G,J,K+-,N; F10 pin; herald family and z source;
  remote program blocks (|x|>=12R, inside their remote balls).
Previous-slice ready radius = current radius - 1 (history_v9 'previous ready ball B_(L-1)(q8)').
Also a list-free structural bound: max declared deadline in the lineage.

Usage: python3 -I -B indep_inventory.py <SOURCE-GEOMETRY.json>
"""
import json
import sys

T = 185
P = 12*840**185
S = P+T
d = 68
R = S+d
L = R+9
Q9 = (0, S, 77)


def l1(p, q):
    return sum(abs(a-b) for a, b in zip(p, q))


def plus(p, e, k):
    return tuple(a+k*b for a, b in zip(p, e))


regions = []  # (name, centre, current radius)
orig = [(0, T, 0), (T, 0, 0), (-T, 0, 0), (4*T, 0, 0), (0, 0, -8*T)]
regions += [('junction original %d' % i, c, T) for i, c in enumerate(orig)]
regions += [('junction transported %d' % i, plus(c, (0, 1, 0), P), S) for i, c in enumerate(orig[:4])]
regions += [('Y collision', (0, S, d), R), ('R collision', (0, S, -d), R),
            ('q2', (0, S, d+2), R+2), ('q3', (0, S, d+3), R+3),
            ('remote herald', (12*R, 0, 0), R), ('remote Z', (-12*R, 0, 0), R)]
regions += [('outward q%d' % k, (0, S, d+k), R+k) for k in range(4, 10)]
regions += [('herald_v10 herald', (48*L, 0, 0), L), ('herald_v10 Z', (-48*L, 0, 0), L)]
regions += [('Native B q10 extension', (0, S, 78), R+10)]
PORTS = [((0, T, 0), (0, -1, 0), T), ((0, 0, -8*T), (0, 0, -1), T), ((T, P, 0), (0, 1, 0), S),
         ((-T, P, 0), (0, 1, 0), S), ((4*T, P, 0), (0, 1, 0), S), ((0, S, 0), (0, 1, 0), S),
         ((12*R, 0, 0), (-1, 0, 0), R), ((48*L, 0, 0), (1, 0, 0), L)]
regions += [('port %d ready' % i, p, dl) for i, (p, _, dl) in enumerate(PORTS)]
# port balls duplicate junction balls (0,T,0),(0,0,-8T),transported,(12R,0,0) and herald: harmless.

sources = {'O': (0, 0, 0), 'W': (0, -76, 76), 'E': (0, -78, 78),
           'Q': (0, S, S+136), 'C': (0, S, S+150), 'G': (0, S, S+152), 'J': (0, S, S+154),
           'K+': (1, S, S+153), 'K-': (-1, S, S+153), 'N': (0, S, S+156),
           'sel y': (0, 2*S, 0), 'sel +T': (T, P+S, 0), 'sel -T': (-T, P+S, 0), 'sel 4T': (4*T, P+S, 0),
           'reset pulse +': (0, S, S+2*d), 'reset pulse -': (0, S, -S-2*d),
           'F10 pin': (-(L+1), S, 78), 'z source': (-48*L, -L, 0)}
inherited = {tuple(r['position']) for r in json.load(open(sys.argv[1]))['sources']}


def on_bank(c):
    for i, (p, e, dl) in enumerate(PORTS):
        ax = [j for j in range(3) if e[j]][0]
        if all(c[j] == p[j] for j in range(3) if j != ax):
            t = (c[ax]-p[ax])*e[ax]
            if dl < t <= 2*L:
                return i
    return None


DIRS = {'+x': (1, 0, 0), '-x': (-1, 0, 0), '+y': (0, 1, 0), '-y': (0, -1, 0), '+z': (0, 0, 1), '-z': (0, 0, -1)}
out = {}
for slice_, k, shrink in (('current', L+2, 0), ('previous', L+1, 1)):
    for n, e in DIRS.items():
        c = plus(Q9, e, k)
        margins = sorted((l1(c, cc)-(r-shrink), name) for name, cc, r in regions)
        pinned = [name for m, name in margins if m <= 0]
        src = [name for name, p in sources.items() if p == c] + (['inherited'] if c in inherited else [])
        bank = on_bank(c) if slice_ == 'current' else None
        remote = abs(c[0]) >= 12*R-R  # remote blocks lie inside |x|>=11R
        herald_family = c[0] >= 47*L
        status = 'PINNED' if (pinned or src or remote or herald_family) else ('BANK' if bank is not None else 'FREE')
        mm = margins[0][0]
        out['%s %s' % (slice_, n)] = {'status': status, 'pinned_by': pinned[:3], 'sources': src, 'bank': bank,
                                      'min_margin': mm if abs(mm) < 10**6 else 'huge', 'nearest': margins[0][1]}
# List-free structural bound: a cell c can be pinned by a ready cone only around a declared
# record (target, deadline) with dist(c,target) <= deadline.  Largest declared deadline is
# L+1 (q10); every record with deadline >= L is listed here.
records = [('q9 terminal', Q9, L), ('q10', (0, S, 78), L+1), ('herald', (48*L, 0, 0), L), ('Z', (-48*L, 0, 0), L),
           ('q8 (Native A pool)', (0, S, 76), L+1)]
bound = {}
for n in ('-x', '+y', '-y'):
    c = plus(Q9, DIRS[n], L+2)
    bound[n] = min(l1(c, t)-dl for _, t, dl in records)
print(json.dumps({'regions': len(regions), 'keys': out, 'late_record_slack': bound}, indent=1))
