#!/usr/bin/env python3
"""Setting-conditioned later access through H*=2L (later-access-preregistration.md).

Standard library only; exact int and Fraction arithmetic. Every check raises
CheckFailure or returns a status; no assert statement is used, so -O behaves
identically. Exit 0 with a token, 2 VOID, 3 output differs from the committed
expected JSON. The token is computed only after every control has passed.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE_ROOT = HERE.parents[1]/'oi-qm/reconstruction/native-y-continuation-20261024'
EXPECTED = HERE/'later-access-result.json'
SCHEMA = 'oi.native-later-access.v1'
PINS = {
    'native_vread_v15/checks.py':
        '93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824',
    'shared_v12/INTERFACE-CONTRACT.md':
        '1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633',
    'history_v11/REPORT.md':
        '413c9595a6def923ba62e1c0d34c12c0516997fe1c928e5438abaf6a990fdb81',
    'parallel_v3/history_control/SOURCE-GEOMETRY.json':
        '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d',
}
PARENT = ('native_random_setting_probe.py',
          '1609a902350de46aa051b771725eaf1bec611d0ce843ee5e005e2ee3dde0753b')
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
BOTTOM = 'BOTTOM'

# Code mutants of the preregistered mutant table (row number, catching checkpoints).
# Row 4 ("P2 weakened: >= for >, or record cells skipped") is run as both variants.
MUTANTS = {
    'drop-RBD': (1, ('CP-LEAK',)),
    'marginal-comparator': (2, ('CP-MARG',)),
    'pin-frontier': (3, ('CP-SUPPORT',)),
    'p2-ge': (4, ('CP-GEO-COUNTER',)),
    'p2-skip-records': (4, ('CP-GEO-COUNTER',)),
    'sampled-min': (5, ('CP-BREAKPOINT',)),
    'order-reversed-accepted': (6, ('CP-ORDER-COUNTER',)),
    'nonbijective-rule': (7, ('CP-RULE', 'CP-PERM-A')),
    'omit-terminal': (8, ('CP-BRANCH',)),
    'renormalize': (9, ('CP-BRANCH',)),
    'float': (10, ('CP-EXACT',)),
    'extra-read': (11, ('CP-READSET',)),
    'no-stop-domain-check': (12, ('CP-STOP-COUNTER',)),
    'search-fixed-background': (13, ('CP-SEARCH-COUNTER',)),
    'token-before-controls': (14, ('CP-GATE',)),
}
MUTANT = None


class CheckFailure(Exception):
    pass


def require(ok, label):
    if not ok:
        raise CheckFailure(label)


def dist(p, q):
    return sum(abs(x-y) for x, y in zip(p, q))


def add(p, q, k=1):
    return tuple(x+k*y for x, y in zip(p, q))


# ------------------------------------------------------------------ the rule

def rule_bits(a, b, d):
    """H(A,B,D)=(B,D,A XOR BD) on bits or on packed bit planes."""
    if MUTANT == 'nonbijective-rule':
        return b, d, b & d
    return b, d, a ^ (b & d)


def prime_bits(a, b, d):
    """The non-bijective countercontrol rule H'(A,B,D)=(B,D,BD)."""
    return b, d, b & d


def code_rule(bits):
    def h(code):
        x, y, z = bits((code >> 2) & 1, (code >> 1) & 1, code & 1)
        return 4*x+2*y+z
    return h


def h(code):
    return code_rule(rule_bits)(code)


def h_spec(code):
    a, b, d = (code >> 2) & 1, (code >> 1) & 1, code & 1
    return 4*b+2*d+(a ^ (b & d))


# --------------------------------------------------------- inputs (CP-PIN)

def load_inputs(root):
    digests = {}
    for rel, digest in sorted(PINS.items()):
        raw = (root/rel).read_bytes()
        got = hashlib.sha256(raw).hexdigest()
        require(got == digest, 'CP-PIN: input pin '+rel)
        digests[rel] = got
    raw = (HERE/PARENT[0]).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT[1], 'CP-PIN: parent probe pin')
    digests['continuous-substates/'+PARENT[0]] = PARENT[1]
    v = load_module('retained_preparation', root/'native_vread_v15/checks.py')
    par = load_module('accepted_parent', HERE/PARENT[0])
    sources = json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes())['sources']
    require(len(sources) == 1479, 'CP-PIN: 1479 compiled sources')
    inventory = sorted({tuple(s['position']) for s in sources})
    _, balls = v.ready_balls()
    exceptions = v.local_sources()
    require(len(balls) == 25 and len(exceptions) == 17, 'CP-PIN: 25 ready balls and 17 named exceptions')
    q = v.Q10
    rows = [('R', v.S+4, v.PORTS[5][0], v.add(v.PORTS[5][0], v.PORTS[5][1], v.S+4), 'BANK'),
            ('N', v.L+2, q, v.add(q, par.D[3], v.L+2), 'FREE')]
    for off in (2, 3, 4, 5):
        t = v.L+off
        rows += [('B%d:%d' % (off, i), t, v.add(q, par.D[i]),
                  v.add(v.add(q, par.D[i]), par.LAUNCH[i], t), 'FREE') for i in par.ORDER]
        if off >= 4:
            rows += [('W%d:%d' % (off, i), t, p, v.add(p, d, t), 'BANK')
                     for i, (p, d, _) in enumerate(v.PORTS)]
    require(len(rows) == 42 and len({r[3] for r in rows}) == 42, 'CP-PIN: 42 distinct eta cells')
    inv = set(inventory)
    kinds = [v.classify(r[3], inv, balls)[0] for r in rows]
    require(kinds == [r[4] for r in rows] and kinds.count('FREE') == 25 and kinds.count('BANK') == 17,
            'CP-PIN: eta classes 25 FREE and 17 BANK')
    return {'v': v, 'par': par, 'digests': digests, 'inventory': inventory, 'balls': balls,
            'exceptions': exceptions, 'eta': rows}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# -------------------------------------------------- piecewise-affine minimum

def candidates(origin, direction, cell, lo, hi):
    """Endpoints and every absolute-value breakpoint of t -> dist(origin+t*dir, cell)."""
    if MUTANT == 'sampled-min':
        return sorted({lo, hi} | {lo+(hi-lo)*k//10 for k in range(11)})
    out = {lo, hi}
    for k in range(3):
        if direction[k]:
            root = Fraction(cell[k]-origin[k], direction[k])
            for r in (root.numerator//root.denominator, -((-root.numerator)//root.denominator)):
                if lo <= r <= hi:
                    out.add(r)
    return sorted(out)


def breakpoints_only(origin, direction, cell, lo, hi):
    out = {lo, hi}
    for k in range(3):
        if direction[k]:
            r = (cell[k]-origin[k])*direction[k]
            if lo <= r <= hi:
                out.add(r)
    return sorted(out)


def gfun(origin, direction, cell, time, slope):
    return lambda t: dist(add(origin, direction, t), cell)+slope*t-time


def minimum(ray, cell, time, slope=0, cands=None):
    origin, direction, lo, hi = ray
    g = gfun(origin, direction, cell, time, slope)
    ts = cands if cands is not None else candidates(origin, direction, cell, lo, hi)
    best = min((g(t), t) for t in ts)
    return best[0], best[1], len(ts)


def first_below(ray, cell, time, slope, threshold):
    """Smallest integer t in the window with g(t) < threshold, exactly."""
    origin, direction, lo, hi = ray
    g = gfun(origin, direction, cell, time, slope)
    ts = breakpoints_only(origin, direction, cell, lo, hi)
    if g(ts[0]) < threshold:
        return ts[0]
    for a, b in zip(ts, ts[1:]):
        ga, gb = g(a), g(b)
        if gb < threshold:
            m = (gb-ga)//(b-a)
            return a+(ga-threshold)//(-m)+1
    return None


# ------------------------------------------------------------- geometry

class Geometry:
    def __init__(self, inp):
        v = self.v = inp['v']
        self.L, self.S, self.R, self.T = v.L, v.S, v.R, v.T
        self.H = 2*v.L
        self.lo = v.L+6
        self.ports = [(p, d) for p, d, _ in v.PORTS]
        self.rays = [(p, d, self.lo, self.H) for p, d in self.ports]
        L, S, R = v.L, v.S, v.R
        q = v.Q10
        self.footprint = [q]+[add(q, d) for d in STEPS]
        self.records = ([('R', self.ports[5][0], S+4), ('q9_record', v.Q9, L),
                         ('V_read', v.Q9, L+2), ('herald', self.ports[7][0], L)] +
                        [('flag_q%d' % k, (0, S, 68+k), R+k) for k in range(10)] +
                        [('port%d_precut' % j, p, L+3) for j, (p, _) in enumerate(self.ports)])
        labels = []
        for name, t in (('K0', L+3), ('K1', L+4), ('K2', L+5)):
            for n, site in enumerate(self.footprint):
                labels.append(('%s_cur_site%d' % (name, n), site, t))
                labels.append(('%s_prev_site%d' % (name, n), site, t-1))
        labels += [('dW1_port%d' % j, p, L+4) for j, (p, _) in enumerate(self.ports)]
        labels += [('dW2_port%d' % j, p, L+5) for j, (p, _) in enumerate(self.ports)]
        self.labels = labels
        self.eta = inp['eta']
        self.inventory = inp['inventory']
        self.exceptions = inp['exceptions']
        self.balls = inp['balls']

    def tick(self, t):
        for base, name in ((self.L, 'L'), (2*self.L, '2L'), (self.S, 'S'), (self.R, 'R')):
            if abs(t-base) <= 10**6:
                return name+('+%d' % (t-base) if t >= base else '-%d' % (base-t))
        return str(t)


def p1_check(geo, rays):
    """P1: unique straight own path of length t, and no other-port arrival before t."""
    least, where, evals, fails = None, None, 0, []
    for i, ray in enumerate(rays):
        origin, direction, lo, hi = ray
        axial = sum(1 for x in direction if x) == 1 and sum(abs(x) for x in direction) == 1
        own_ok = axial and origin == geo.ports[i][0]
        for t in breakpoints_only(origin, direction, origin, lo, hi):
            own_ok = own_ok and dist(add(origin, direction, t), origin) == t
            evals += 1
        if not own_ok:
            fails.append((lo, i, {'ray': i, 'tick': geo.tick(lo), 'kind': 'own path', '_t': lo}))
        for j, (pj, _) in enumerate(geo.ports):
            if j == i:
                continue
            m, t, n = minimum(ray, pj, 0, slope=-1)
            evals += n
            if least is None or m < least:
                least, where = m, {'ray': i, 'port': j, 'tick': geo.tick(t)}
            if m < 0:
                tb = first_below(ray, pj, 0, -1, 0)
                tb = t if tb is None else tb
                tp = dist(add(origin, direction, tb), pj)
                fails.append((tb, i, {'ray': i, 'tick': geo.tick(tb), 'kind': 'arrival at port %d' % j,
                                      'arrival_tick': geo.tick(tp), '_t': tb, '_tp': tp, '_j': j}))
    first = min(fails, key=lambda f: (f[0], f[1]))[2] if fails else None
    return first is None, {'min_other_port_distance_minus_t': least, 'argmin': where,
                           'evaluations': evals}, first


def p2_check(geo, rays):
    """P2: dist(f_i(t), cell) > time for every pre-cut record and every label."""
    entries = ([] if MUTANT == 'p2-skip-records' else [('record',)+e for e in geo.records]) + \
        [('label',)+e for e in geo.labels]
    least, where, evals, failing, first = None, None, 0, [], None
    for i, ray in enumerate(rays):
        for kind, name, cell, time in entries:
            m, t, n = minimum(ray, cell, time)
            evals += n
            if least is None or m < least:
                least, where = m, {'ray': i, 'entry': name, 'tick': geo.tick(t)}
            ok = (m >= 0) if MUTANT == 'p2-ge' else (m > 0)
            if not ok:
                tb = first_below(ray, cell, time, 0, 1)
                tb = t if tb is None else tb
                failing.append((kind, name))
                if first is None or (tb, i) < (first['_t'], first['ray']):
                    first = {'ray': i, 'tick': geo.tick(tb), 'cell': name, 'time': geo.tick(time),
                             '_t': tb}
    return first is None, {'min_distance_minus_time': least, 'argmin': where,
                           'entries': len(entries), 'evaluations': evals}, first, failing


def on_ray(ray, cell):
    origin, direction, lo, hi = ray
    k = next(j for j in range(3) if direction[j])
    if any(cell[j] != origin[j] for j in range(3) if j != k):
        return None
    t = (cell[k]-origin[k])*direction[k]
    return t if lo <= t <= hi else None


def p3_check(geo, rays):
    """P3: exact affine-ray intersection against eta, sources, exceptions, ready balls."""
    points = ([('eta:'+r[0], r[3]) for r in geo.eta] +
              [('source', p) for p in geo.inventory] +
              [('exception:'+n, p) for n, p in sorted(geo.exceptions.items())])
    hits, first, least, where = [], None, None, None
    for i, ray in enumerate(rays):
        for name, cell in points:
            t = on_ray(ray, cell)
            if t is not None:
                hits.append(name)
                if first is None or (t, i) < (first['_t'], first['ray']):
                    first = {'ray': i, 'tick': geo.tick(t), 'set': name, '_t': t}
        for b, (center, radius) in enumerate(geo.balls):
            m, t, _ = minimum(ray, center, radius)
            if least is None or m < least:
                least, where = m, {'ray': i, 'ball': b, 'tick': geo.tick(t)}
            if not m > 0:
                tb = first_below(ray, center, radius, 0, 1)
                tb = t if tb is None else tb
                hits.append('ball%d' % b)
                if first is None or (tb, i) < (first['_t'], first['ray']):
                    first = {'ray': i, 'tick': geo.tick(tb), 'set': 'ready ball %d' % b, '_t': tb}
    # beta's own cells are pairwise distinct (the H-prior exponent counts them once).
    distinct = True
    for i in range(len(rays)):
        for j in range(i+1, len(rays)):
            if rays_meet(rays[i], rays[j]):
                distinct = False
                hits.append('beta%d~beta%d' % (i, j))
    return not hits, {'point_cells': len(points), 'balls': len(geo.balls), 'intersections': len(hits),
                      'min_ball_distance_minus_radius': least, 'ball_argmin': where,
                      'beta_cells_pairwise_distinct': distinct}, first, hits


def rays_meet(a, b):
    (pa, da, la, ha), (pb, db, lb, hb) = a, b
    ka = next(j for j in range(3) if da[j])
    kb = next(j for j in range(3) if db[j])
    if ka == kb:
        if any(pa[j] != pb[j] for j in range(3) if j != ka):
            return False
        ia = sorted((pa[ka]+da[ka]*la, pa[ka]+da[ka]*ha))
        ib = sorted((pb[ka]+db[ka]*lb, pb[ka]+db[ka]*hb))
        return not (ia[1] < ib[0] or ib[1] < ia[0])
    if any(pa[j] != pb[j] for j in range(3) if j not in (ka, kb)):
        return False
    ta = (pb[ka]-pa[ka])*da[ka]
    tb = (pa[kb]-pb[kb])*db[kb]
    return la <= ta <= ha and lb <= tb <= hb


def equal_time_edges(geo, rays):
    edges = set()
    for i, ray in enumerate(rays):
        for j, (pj, _) in enumerate(geo.ports):
            if i != j and minimum(ray, pj, 0, slope=-1)[0] == 0:
                edges.add((i, j))
    return edges


def p4_check(edges, key):
    """P4: the equal-time cross-edges are exactly 2->5 and 3->5, consistent with the order."""
    if MUTANT == 'order-reversed-accepted':
        consistent = all(key(i) != key(j) for i, j in edges)
    else:
        consistent = all(key(i) < key(j) for i, j in edges)
    return edges == {(2, 5), (3, 5)} and consistent


def p5_check(geo):
    side = 256*geo.L+64*geo.T+1
    pts = [add(p, d, t) for p, d, lo, hi in geo.rays for t in (lo, hi)]
    pts += [p for p, _ in geo.ports]+[r[3] for r in geo.eta]+[r[2] for r in geo.eta]
    pts += geo.footprint+[c for _, c, _ in geo.records]+list(geo.inventory)
    pts += list(geo.exceptions.values())
    for center, radius in geo.balls:
        for k in range(3):
            for s in (-1, 1):
                p = list(center)
                p[k] += s*radius
                pts.append(tuple(p))
    spans = [max(p[k] for p in pts)-min(p[k] for p in pts) for k in range(3)]
    ok = 2*geo.H < side and all(2*s < side for s in spans)
    return ok, {'two_Hstar_lt_side': 2*geo.H < side,
                'every_span_lt_half_side': all(2*s < side for s in spans),
                'side_minus_two_Hstar': side-2*geo.H,
                'half_side_minus_max_span': Fraction(side, 2)-max(spans), 'points': len(pts)}


def p6a_check(bits):
    hh = code_rule(bits)
    return len({hh(c) for c in range(8)}) == 8


# ---------------------------------------------------- packed native worlds

def bgval(*key):
    return hashlib.sha256(repr(key).encode()).digest()[0] & 7


def to_planes(values):
    n = len(values)
    out = []
    for k in (2, 1, 0):
        bits = ''.join('1' if (values[i] >> k) & 1 else '0' for i in range(n-1, -1, -1))
        out.append(int(bits, 2))
    return tuple(out)


def from_planes(tr, n):
    a, b, d = (format(x, '0%db' % n)[::-1] for x in tr)
    return [4*(a[i] == '1')+2*(b[i] == '1')+(d[i] == '1') for i in range(n)]


def native_world(cur, bg, bits=None, actuator=None):
    """Second-order native rule U_t(p)=U_(t-2)(p) XOR H(XOR of six U_(t-1) neighbors)."""
    bits = bits or rule_bits

    @lru_cache(maxsize=None)
    def get(t, p):
        if t == 0 and p in cur:
            return cur[p]
        if t in (0, -1):
            return bg(t, p)
        a = b = d = 0
        for s in STEPS:
            w = get(t-1, (p[0]+s[0], p[1]+s[1], p[2]+s[2]))
            a ^= w[0]
            b ^= w[1]
            d ^= w[2]
        old = get(t-2, p)
        n = bits(a, b, d)
        out = (old[0] ^ n[0], old[1] ^ n[1], old[2] ^ n[2])
        if actuator is not None:
            out = actuator(t, p, out, get)
        return out
    return get


def const_bg(lanes, *key):
    full = (1 << lanes)-1

    def bg(t, p):
        v = bgval(*(key+(t, p)))
        return tuple(full if (v >> k) & 1 else 0 for k in (2, 1, 0))
    return bg


def block_bg(lanes, block, kind, seed):
    """Background depending on a per-block (setting, key) label: value(kind,seed,c,e,t,p)."""
    nblocks = lanes//block
    masks = [((1 << block)-1) << (block*j) for j in range(nblocks)]

    def value(c, e, t, p):
        if kind == 'sha256':
            return bgval('P6b', seed, c, e, t, p)
        x, y, z = p
        return ((5*x*x+3*y*y+7*z*z+x*y+11*t+13*seed+5*c+3*e+x*e) ^ (x*z+3*seed*t+y*c+e*z)) & 7

    def bg(t, p):
        planes = [0, 0, 0]
        for j in range(nblocks):
            v = value(j//8, j % 8, t, p)
            for k in range(3):
                if (v >> (2-k)) & 1:
                    planes[k] |= masks[j]
        return tuple(planes)
    return bg


def p6b_check(bits):
    """P6b: every first-front step permutes its own triple in setting- and key-dependent backgrounds."""
    worlds = perms = 0
    first = None
    for kind, n, seed in product(('sha256', 'polynomial'), (1, 2, 3, 4), (0, 3, 8)):
        for e in STEPS:
            lanes = 128   # (c, eta label, own bank value)
            cur = {add((0, 0, 0), e, n): to_planes([x & 7 for x in range(lanes)])}
            get = native_world(cur, block_bg(lanes, 8, kind, seed), bits)
            for j in range(1, n+1):
                vals = from_planes(get(j, add((0, 0, 0), e, n-j)), lanes)
                for blk in range(16):
                    perms += 1
                    if len(set(vals[8*blk:8*blk+8])) != 8 and first is None:
                        first = {'world': [kind, n, seed, list(e)], 'step': j, 'block': blk}
            for tt in range(1, n):
                vals = from_planes(get(tt, (0, 0, 0)), lanes)
                for blk in range(16):
                    if len(set(vals[8*blk:8*blk+8])) != 1 and first is None:
                        first = {'world': [kind, n, seed, list(e)], 'early_tick': tt, 'block': blk}
            worlds += 1
    # Same-tick co-arrival: a second bank triple whose front meets the own path at every step.
    for kind, n, seed in product(('sha256', 'polynomial'), (2, 3, 4), (0, 3, 8)):
        lanes = 1024   # (c, eta label, co-arriving triple, own bank value)
        cur = {(0, n, 0): to_planes([x & 7 for x in range(lanes)]),
               (1, n-1, 0): to_planes([(x >> 3) & 7 for x in range(lanes)])}
        get = native_world(cur, block_bg(lanes, 64, kind, seed), bits)
        for j in range(1, n+1):
            vals = from_planes(get(j, (0, n-j, 0)), lanes)
            for grp in range(128):
                perms += 1
                if len(set(vals[8*grp:8*grp+8])) != 8 and first is None:
                    first = {'world': ['co-arrival', kind, n, seed], 'step': j, 'group': grp}
        worlds += 1
    return first is None, {'worlds': worlds, 'diagonal_permutation_checks': perms}, first


# ------------------------------------------------- the small window world

TOY = {'s': (0, 7, 0), 'g': (0, 8, 0), 'k': (0, -7, 0), 'd': (2, 5, 0), 'b': (8, 0, 0)}
TOY_VARS = ('s', 'g', 'k', 'd', 'b')
PR, PW, PK, PT, ACT = (0, 5, 0), (4, 5, 0), (0, -5, 0), (5, 0, 0), (6, 0, 0)
TOY_OUT = {'R': (2, PR), 'Wp@3': (3, PR), 'Wq@2': (2, PW), 'K0@2': (2, PK),
           'Tail0@3': (3, PT), 'Tail0@4': (4, PT)}


def toy_eval(assigns, actuate, cvals=None):
    """Evaluate the native window for each assignment; c is R.A unless supplied exogenously."""
    n = len(assigns)
    cur = {TOY[v]: to_planes([a[v] for a in assigns]) for v in TOY_VARS}
    cplane = to_planes([4*c for c in cvals])[0] if cvals is not None else None

    def act(t, p, out, get):
        if actuate and t == 2 and p == ACT:
            ca = cplane if cplane is not None else get(2, PR)[0]
            return (out[0] ^ ca, out[1], out[2])
        return out
    get = native_world(cur, const_bg(n, 'toy'), actuator=act)
    vals = {name: from_planes(get(t, p), n) for name, (t, p) in TOY_OUT.items()}
    obs = []
    for i in range(n):
        r = vals['R'][i]
        o = {'R.A': r >> 2, 'R.B@2': (r >> 1) & 1, 'R.D@2': r & 1}
        o.update({name: vals[name][i] for name in TOY_OUT if name != 'R'})
        o['c'] = cvals[i] if cvals is not None else r >> 2
        obs.append(o)
    return obs


def toy_fixture(pins=None, equal=None, actuate=False):
    pins, equal = pins or {}, equal or {}
    free = [v for v in TOY_VARS if v not in pins and v not in equal]
    assigns = []
    for vals in product(range(8), repeat=len(free)):
        a = dict(zip(free, vals))
        a.update(pins)
        for v, w in equal.items():
            a[v] = a[w]
        assigns.append(a)
    mass = Fraction(1, 8**len(free))
    obs = toy_eval(assigns, actuate)
    lanes = []
    for a, o in zip(assigns, obs):
        o['eta'] = (a['s'], a['k'])
        o['Dp'] = (a['g'], a['d'])
        lanes.append((mass, o, a))
    return {'lanes': lanes, 'pins': pins, 'equal': equal, 'actuate': actuate}


# ------------------------------------------------------ comparator layer

def is_window(name):
    return name.startswith(('R.B', 'R.D', 'W', 'K', 'Tail'))


def window_x(obs, assign=None, extra=()):
    names = sorted(n for n in obs if is_window(n))
    if MUTANT == 'drop-RBD':
        names = [n for n in names if not n.startswith(('R.B', 'R.D'))]
    x = tuple((n, obs[n]) for n in names)
    return x+tuple(('X:'+v, assign[v]) for v in extra)


def k0_of(x):
    for name, val in x:
        if name[:2] == 'K0':
            return val
    raise KeyError('K0 coordinate')


def accessible(x):
    return tuple(p for p in x if not p[0].startswith('K'))


def measures(lanes, extra=(), view=window_x):
    tot = defaultdict(Fraction)
    for mass, obs, _ in lanes:
        tot[obs['c']] += mass
    mu = {0: defaultdict(Fraction), 1: defaultdict(Fraction)}
    for mass, obs, assign in lanes:
        mu[obs['c']][view(obs, assign, extra)] += mass/tot[obs['c']]
    return mu


def restrict(mu, k0):
    out = {x: m for x, m in mu.items() if k0_of(x) == k0}
    if MUTANT == 'renormalize':
        z = sum(out.values())
        out = {x: m/z for x, m in out.items()} if z else out
    return out


def push(mu, f):
    out = defaultdict(Fraction)
    for x, m in mu.items():
        out[f(x)] += m
    return out


def tv(mu, nu):
    s = sum((abs(mu.get(x, 0)-nu.get(x, 0)) for x in set(mu) | set(nu)), Fraction(0))/2
    return float(s) if MUTANT == 'float' else s


def marginal_tv(mu, nu):
    names = sorted({n for x in list(mu)+list(nu) for n, _ in x})
    best = Fraction(0)
    for name in names:
        f = (lambda x, name=name: dict(x).get(name))
        best = max(best, tv(push(mu, f), push(nu, f)))
    return best


def compare(mu, nu):
    """The joint comparator: TV over the complete tuple."""
    if MUTANT == 'marginal-comparator':
        return marginal_tv(mu, nu)
    return tv(mu, nu)


def k0_values(mu):
    return sorted({k0_of(x) for c in (0, 1) for x in mu[c]}, key=repr)


def tv_tables(mu):
    out = {}
    for k0 in k0_values(mu):
        a, b = restrict(mu[0], k0), restrict(mu[1], k0)
        out[k0] = (compare(a, b), compare(push(a, accessible), push(b, accessible)))
    return out


def hidden_only(tables):
    return any(w > 0 for w, _ in tables.values()) and all(a == 0 for _, a in tables.values())


def informativeness_small(lanes, tail_prefix='Tail'):
    """EMPTY iff Tail is independent of (eta, K labels) given D', computed exactly."""
    groups = defaultdict(list)
    for mass, obs, _ in lanes:
        groups[obs['Dp']].append((mass, obs))
    for rows in groups.values():
        joint, mt, me, tot = defaultdict(Fraction), defaultdict(Fraction), defaultdict(Fraction), Fraction(0)
        for mass, obs in rows:
            tail = tuple(obs[n] for n in sorted(obs) if n.startswith(tail_prefix))
            ek = (obs['eta'],)+tuple(obs[n] for n in sorted(obs) if n.startswith('K'))
            joint[tail, ek] += mass
            mt[tail] += mass
            me[ek] += mass
            tot += mass
        for t in mt:
            for e in me:
                if joint.get((t, e), 0)*tot != mt[t]*me[e]:
                    return 'INFORMATIVE'
    return 'EMPTY'


# ------------------------------------------------- bounded witness search

def bounded_search(label, coord, S, supports, joint, evaluate, cone=None):
    """Item 3: exact law of Y under each c, averaged over every variable of S, per k0."""
    rec = {'trigger': label, 'coordinate': coord, 'S': list(S), 'S_size': len(S)}
    if cone is not None and not set(cone) <= set(S):
        rec.update(derivation='not run', outcome='rejected: incomplete dependence set')
        return rec, False
    if len(S) > 6:
        rec.update(derivation='not run', outcome='outside bound')
        return rec, False
    masses = list(joint.values())
    if not (all(type(m) is Fraction and m >= 0 for m in masses) and sum(masses) == 1):
        rec.update(derivation='failed', outcome='no witness: derivation failed')
        return rec, False
    rec['derivation'] = 'derived from the fixture preparation law'
    names = sorted(supports)
    full = [dict(zip(names, vals)) for vals in product(*(supports[n] for n in names))]
    pairs = [(a, c) for a in full for c in (0, 1)]
    ys = evaluate(pairs)
    table = {}
    for (a, c), y in zip(pairs, ys):
        key = (tuple(a[v] for v in S), c)
        if table.setdefault(key, y) != y:
            rec['outcome'] = 'rejected: incomplete dependence set'
            return rec, False
    pc = defaultdict(Fraction)
    for (sigma, c, k0), m in joint.items():
        pc[c] += m
    fixed = None
    if MUTANT == 'search-fixed-background' and S:
        fixed = min(sig[-1] for (sig, c, k0), m in joint.items() if m > 0)
    law = {0: defaultdict(lambda: defaultdict(Fraction)), 1: defaultdict(lambda: defaultdict(Fraction))}
    for (sigma, c, k0), m in sorted(joint.items(), key=repr):
        if m == 0 or (fixed is not None and sigma[-1] != fixed):
            continue
        law[c][k0][table[sigma, c]] += m/pc[c]
    witness = None
    for k0 in sorted(set(law[0]) | set(law[1]), key=repr):
        a = {y: m for y, m in law[0][k0].items() if m}
        b = {y: m for y, m in law[1][k0].items() if m}
        if a != b:
            witness = {'k0': k0, 'law_c0': sorted(a.items()), 'law_c1': sorted(b.items())}
            break
    rec['outcome'] = 'witness' if witness else 'no witness: equal laws'
    if witness:
        rec['witness'] = witness
    return rec, witness is not None


def toy_search(fix, coord, S_override=None):
    t, p = TOY_OUT[coord]
    cone = [v for v in TOY_VARS if dist(TOY[v], p) <= t]
    S = cone if S_override is None else S_override
    joint = defaultdict(Fraction)
    for mass, obs, a in fix['lanes']:
        joint[tuple(a[v] for v in S), obs['c'], obs['K0@2']] += mass

    def evaluate(pairs):
        obs = toy_eval([a for a, _ in pairs], fix['actuate'], [c for _, c in pairs])
        return [o[coord] for o in obs]
    return bounded_search('fixture', coord, S, {v: range(8) for v in TOY_VARS}, dict(joint),
                          evaluate, cone=cone if S_override is None else None)


def ball_count(r):
    return 0 if r < 0 else (2*r+1)*(2*r*r+2*r+3)//3


def actual_search(geo, p1_first):
    """Item 3 at actual scale: |S| is the backward-cone variable count of each searched port."""
    rec = {'trigger': None, 'S_size': None, 'derivation': 'not run', 'outcome': 'not triggered'}
    if p1_first is None:
        return rec, False
    coords = [(p1_first['ray'], p1_first['_t'])]
    if '_tp' in p1_first:
        coords.append((p1_first['_j'], p1_first['_tp']))
    sizes = [ball_count(t)+ball_count(t-1) for _, t in coords]
    rec['trigger'] = {'ray': p1_first['ray'], 'tick': p1_first['tick'],
                      'searched': [{'port': i, 'tick': geo.tick(t)} for i, t in coords]}
    rec['S_size'] = [str(s) for s in sizes]
    if all(s > 6 for s in sizes):
        rec['outcome'] = 'outside bound: no witness'
        return rec, False
    rec['derivation'] = 'unavailable: no exact joint law of S with (c, K0) at actual scale'
    rec['outcome'] = 'no witness: derivation unavailable'
    return rec, False


# ----------------------------------------------------------------- controls

def control_rule(inp):
    v = inp['v']
    require(all(h(c) == v.h(c) == h_spec(c) for c in range(8)), 'CP-RULE: h differs from the pinned rule')
    require(len({h(c) for c in range(8)}) == 8 and any(h(c ^ 1) ^ h(c) != h(1) ^ h(0) for c in range(8)),
            'CP-RULE: pinned rule bijective and nonlinear')
    return {'codes_checked': 8, 'table': [h(c) for c in range(8)]}


def control_pos(fx):
    fix = fx['pos']
    tables = tv_tables(measures(fix['lanes']))
    best = max(a for _, a in tables.values())
    require(best > 0, 'CP-POS: supplied coupling not detected by the joint comparator')
    rec, found = toy_search(fix, 'Tail0@3')
    require(found, 'CP-POS: bounded search returned no witness on the supplied coupling')
    return {'max_TV_acc': best, 'search': rec}


def control_access(fx):
    fix = fx['access']
    la = tv_tables(measures(fix['lanes']))
    ext = tv_tables(measures(fix['lanes'], extra=('b',)))
    la_max = max(max(w, a) for w, a in la.values())
    ext_max = max(a for _, a in ext.values())
    require(la_max == 0, 'CP-ACCESS: LA alone shows a difference')
    require(ext_max > 0, 'CP-ACCESS: extra read of the own bank triple not detected')
    return {'LA_max_TV': la_max, 'extra_read_max_TV': ext_max}


def control_prior(fx):
    corr = fx['prior']
    lanes = corr['lanes']
    marg_s, marg_b = defaultdict(Fraction), defaultdict(Fraction)
    for m, o, a in lanes:
        marg_s[a['s']] += m
        marg_b[a['b']] += m
    fair = set(marg_s.values()) == {Fraction(1, 8)} == set(marg_b.values())
    tables = tv_tables(measures(lanes))
    best = max(w for w, _ in tables.values())
    other = tv_tables(measures(fx['prior-other']['lanes']))
    other_max = max(w for w, _ in other.values())
    require(fair, 'CP-PRIOR: correlated fixture marginals not fair')
    require(best > 0, 'CP-PRIOR: b5-correlated prior not detected at fixed k0')
    require(other_max == 0, 'CP-PRIOR: other-key correlation differs at fixed k0')
    return {'fair_marginals': fair, 'b5_correlated_max_TV_win': best, 'other_key_max_TV_win': other_max}


def abstract_lanes(rows):
    mass = Fraction(1, len(rows))
    return [(mass, o, {}) for o in rows]


def control_marg():
    rows = []
    for r, u, k in product(range(8), range(8), range(2)):
        c, rb = r >> 2, (r >> 1) & 1
        rows.append({'c': c, 'R.B@2': rb, 'R.D@2': r & 1, 'K0@2': k, 'Tail0@3': u,
                     'Tail1@3': u ^ (4*c) ^ (2*rb) ^ k})
    mu = measures(abstract_lanes(rows))
    joint = max(compare(restrict(mu[0], k), restrict(mu[1], k)) for k in (0, 1))
    marg = max(marginal_tv(restrict(mu[0], k), restrict(mu[1], k)) for k in (0, 1))
    require(marg == 0, 'CP-MARG: marginal comparator not blind (vacuous fixture)')
    require(joint > 0, 'CP-MARG: joint comparator missed a joint-only difference')
    return {'joint_TV': joint, 'marginal_TV': marg}


def control_leak():
    rows = []
    for r, u in product(range(8), range(8)):
        c = r >> 2
        rows.append({'c': c, 'R.B@2': (r >> 1) & 1, 'R.D@2': r & 1, 'K0@2': 0, 'Tail0@3': u,
                     'Tail1@3': u ^ (4*(c ^ (r & 1)))})
    lanes = abstract_lanes(rows)
    kept = compare(*(measures(lanes)[c] for c in (0, 1)))
    strip = (lambda o, a, e: tuple(p for p in window_x(o, a, e) if not p[0].startswith(('R.B', 'R.D'))))
    mu = measures(lanes, view=strip)
    dropped = compare(mu[0], mu[1])
    require(kept == 1 and dropped == 0, 'CP-LEAK: R.B/D leak not TV1 retained, TV0 dropped')
    return {'TV_with_RBD': kept, 'TV_without_RBD': dropped}


def control_null(fx):
    mu = measures(fx['null']['lanes'])
    same = compare(mu[0], dict(mu[0]))
    tables = tv_tables(mu)
    worst = max(max(w, a) for w, a in tables.values())
    rec, found = toy_search(fx['null'], 'Tail0@3')
    require(same == 0 and worst == 0, 'CP-NULL: identical laws give nonzero TV')
    require(not found, 'CP-NULL: search returned a witness on identical laws')
    return {'identical_TV': same, 'null_world_max_TV': worst, 'search': rec}


def counter_fixture_search(S):
    rows = []
    for s, d in product(range(8), range(8)):
        rows.append({'s': s, 'd': d})
    joint = defaultdict(Fraction)
    for a in rows:
        joint[tuple(a[v] for v in S), a['s'] >> 2, 0] += Fraction(1, 64)

    def evaluate(pairs):
        return [a['d'] ^ c for a, c in pairs]
    return bounded_search('fixture Y=c XOR d', 'Y', S, {'s': range(8), 'd': range(8)},
                          dict(joint), evaluate)


def control_search_counter():
    rec, found = counter_fixture_search(['d'])
    rec2, found2 = counter_fixture_search([])
    require(not found, 'CP-SEARCH-COUNTER: witness returned on Y=c XOR d')
    require(rec2['outcome'].startswith('rejected') and not found2,
            'CP-SEARCH-COUNTER: incomplete dependence set not rejected')
    return {'complete_S': rec, 'd_omitted': rec2}


SUPPORT_FRONTIERS = [(1, 7, 0), (0, 8, 0), (53, 0, 0), (54, 0, 0)]
SUPPORT_OUTPUTS = [(5, (1, 2, 0)), (5, (0, 3, 0)), (5, (48, 0, 0)), (6, (48, 0, 0))]


def frontier_rows(pin=None):
    rows = list(product(range(8), repeat=4))
    if MUTANT == 'pin-frontier':
        rows = [r[:3]+(0,) for r in rows]
    if pin is not None:
        rows = [r[:pin]+(0,)+r[pin+1:] for r in rows]
    return rows


def tail_support(rows, seed):
    n = len(rows)
    cur = {p: to_planes([r[j] for r in rows]) for j, p in enumerate(SUPPORT_FRONTIERS)}
    get = native_world(cur, const_bg(n, 'support', seed))
    outs = [from_planes(get(t, p), n) for t, p in SUPPORT_OUTPUTS]
    return len({tuple(o[i] for o in outs) for i in range(n)})


def control_support():
    out = {}
    for seed in (17, 41):
        full = tail_support(frontier_rows(), seed)
        pinned = tail_support(frontier_rows(pin=1), seed)
        require(full == 4096, 'CP-SUPPORT: four padded frontier triples do not give support 4096')
        require(pinned == 512 and pinned != 4096, 'CP-SUPPORT: pinning not detected as 4096 -> 512')
        out['background_%d' % seed] = {'support': full, 'pinned_support': pinned}
    return out


def control_hidden():
    rows = []
    for r, u, k in product(range(8), range(8), range(8)):
        c = r >> 2
        rows.append({'c': c, 'R.B@2': (r >> 1) & 1, 'R.D@2': r & 1, 'K0@2': k,
                     'K1@3': k ^ (4*c), 'Tail0@4': u})
    tables = tv_tables(measures(abstract_lanes(rows)))
    win = max(w for w, _ in tables.values())
    acc = max(a for _, a in tables.values())
    flag = hidden_only(tables)
    require(win > 0 and acc == 0 and flag, 'CP-HIDDEN: hidden-only case not reported')
    return {'max_TV_win': win, 'max_TV_acc': acc, 'hidden_only': flag}


def control_info(fx):
    empty = informativeness_small(fx['null']['lanes'])
    counter = informativeness_small(fx['prior-other']['lanes'])
    ctv = max(w for w, _ in tv_tables(measures(fx['prior-other']['lanes'])).values())
    require(empty == 'EMPTY', 'CP-INFO: independent uniform tail not EMPTY')
    require(counter == 'INFORMATIVE' and ctv == 0, 'CP-INFO: INFO-COUNTER not INFORMATIVE with TV 0')
    return {'INFO': empty, 'INFO_COUNTER': counter, 'INFO_COUNTER_TV': ctv}


def control_geo_counter(geo):
    L, S = geo.L, geo.S
    o5, d5 = geo.ports[5]
    cone = (add(o5, (0, -(L+6), L+84)), d5, geo.lo, geo.H)
    on_eta = (add(o5, (0, -4, 78)), d5, geo.lo, geo.H)
    q9ray = (add(o5, (3, -(L+6), 77)), d5, geo.lo, geo.H)
    ok_c, m_c, first_c, _ = p2_check(geo, [cone])
    ok_e2 = p2_check(geo, [on_eta])[0]
    ok_e3, _, first_e, hits_e = p3_check(geo, [on_eta])
    ok_q, _, first_q, failing_q = p2_check(geo, [q9ray])
    rec_hit = sorted({n for k, n in failing_q if k == 'record' and n in ('q9_record', 'V_read')})
    require(not ok_c and m_c['min_distance_minus_time'] == 0,
            'CP-GEO-COUNTER: exact-cone ray (dist == time) not rejected by P2')
    require(not ok_e3 and any(x.startswith('eta:') for x in hits_e),
            'CP-GEO-COUNTER: ray on an eta cell not rejected by P3')
    require(not ok_q and rec_hit, 'CP-GEO-COUNTER: ray reaching the q9/V record not rejected at the record')
    return {'exact_cone_min': m_c['min_distance_minus_time'], 'exact_cone_first': strip_private(first_c),
            'eta_ray_P2_fails': not ok_e2, 'eta_ray_first': strip_private(first_e),
            'q9_ray_records_hit': rec_hit, 'q9_ray_first': strip_private(first_q)}


def control_breakpoint():
    ray = ((0, 0, 0), (1, 0, 0), 1, 100)
    cell, time = (37, 0, 0), 2
    m, t, _ = minimum(ray, cell, time)
    grid = sorted({1, 100} | {1+99*k//10 for k in range(11)})
    sampled = min(gfun(ray[0], ray[1], cell, time, 0)(x) for x in grid)
    require(sampled > 0, 'CP-BREAKPOINT: fixture vacuous (sampling finds the minimum)')
    require(m == -2 and t == 37, 'CP-BREAKPOINT: breakpoint minimum not found')
    return {'breakpoint_min': m, 'breakpoint_tick': t, 'sampled_min': sampled}


def control_order_counter(edges):
    reversed_ok = p4_check(edges, lambda i: -i)
    require(not reversed_ok, 'CP-ORDER-COUNTER: reversed equal-time order accepted')
    return {'reversed_order_fails_P4': not reversed_ok}


def control_perm_counter():
    a = p6a_check(prime_bits)
    b = p6b_check(prime_bits)[0]
    require(not a and not b, "CP-PERM-COUNTER: non-bijective H' passes P6a or P6b")
    return {'P6a_fails': not a, 'P6b_fails': not b}


def la_read_set(geo):
    la = {('port', i, 'L+6..2L') for i in range(8)}
    precut = {('port', i, 'ticks<=L+5') for i in range(8)} | {('q9_whole', 'L'), ('V_whole', 'L+2')}
    return la, precut


def declared_reads(geo):
    la, precut = la_read_set(geo)
    reads = set(la) | set(precut)
    if MUTANT == 'extra-read':
        reads.add(('z_receiver', 'L+6..2L'))
    return reads


def access_changes(reads, geo):
    if MUTANT == 'extra-read':
        return set()
    la, precut = la_read_set(geo)
    return reads-la-precut


def control_readset(geo):
    la, precut = la_read_set(geo)
    reads = declared_reads(geo)
    extra = ('q10', 'L+6')
    flagged = access_changes(reads | {extra}, geo)
    require(reads == la | precut and not access_changes(reads, geo),
            'CP-READSET: declared read set differs from LA plus pre-cut records')
    require(flagged == {extra}, 'CP-READSET: an extra read field is not flagged as an access change')
    return {'declared_fields': len(reads), 'LA_fields': len(la), 'precut_fields': len(precut),
            'extra_read_flagged': sorted(flagged)}


def stop_domain_ok(domain, acc):
    if MUTANT == 'no-stop-domain-check':
        return True
    return set(domain) <= set(acc)


def run_stop(rule, x_acc, lane_inputs):
    _, domain, fn = rule
    pre = []
    while True:
        if fn(dict(pre), lane_inputs) or len(pre) == len(x_acc):
            return tuple(pre)
        pre.append(x_acc[len(pre)])


def control_stop(fx):
    checked = 0
    for name in ('pos',):
        lanes = fx[name]['lanes']
        require(len({m for m, _, _ in lanes}) == 1, 'CP-STOP: fixture lanes not equally weighted')
        xs = [window_x(o, a) for _, o, a in lanes]
        acc = sorted({n for n, _ in accessible(xs[0])}, key=lambda n: (int(n.split('@')[1]), n))
        order = {n: i for i, n in enumerate(acc)}

        def chron(x):
            return tuple(sorted(accessible(x), key=lambda p: order[p[0]]))
        chrons = [chron(x) for x in xs]
        k0s = [k0_of(x) for x in xs]
        count_c, lane_groups = defaultdict(int), defaultdict(int)
        for (_, o, _), xc, k0 in zip(lanes, chrons, k0s):
            count_c[o['c']] += 1
            lane_groups[o['c'], k0, xc] += 1
        rules = [('len%d' % m, tuple(acc), (lambda pre, inp, m=m: len(pre) >= m)) for m in range(len(acc)+1)]
        for nm in acc:
            for bit in range(3):
                rules.append(('%s bit%d' % (nm, bit), tuple(acc),
                              (lambda pre, inp, nm=nm, bit=bit: nm in pre and (pre[nm] >> bit) & 1 == 1)))
        mu = measures(lanes)
        ks = k0_values(mu)
        rest = {(c, k0): restrict(mu[c], k0) for c in (0, 1) for k0 in ks}
        full = {k0: compare(rest[0, k0], rest[1, k0]) for k0 in ks}
        rest_chron = {key: [(chron(x), m) for x, m in law.items()] for key, law in rest.items()}
        for rule in rules:
            require(stop_domain_ok(rule[1], acc), 'CP-STOP: valid rule rejected')
            memo, counts = {}, defaultdict(int)
            for (c, k0, xc), n in lane_groups.items():
                if xc not in memo:
                    memo[xc] = run_stop(rule, xc, {})
                counts[c, k0, memo[xc]] += n
            direct = defaultdict(dict)
            for (c, k0, r), n in counts.items():
                direct[c, k0][r] = Fraction(n, count_c[c])
            for k0 in ks:
                pushed = {}
                for c in (0, 1):
                    law = defaultdict(Fraction)
                    for xc, m in rest_chron[c, k0]:
                        law[memo[xc] if xc in memo else run_stop(rule, xc, {})] += m
                    pushed[c] = law
                require(all(direct[c, k0] == dict(pushed[c]) for c in (0, 1)),
                        'CP-STOP: stopped law is not the pushforward of the full-window law')
                require(compare(pushed[0], pushed[1]) <= full[k0], 'CP-STOP: stopped TV exceeds full-window TV')
                checked += 1
    require(max(full.values()) > 0, 'CP-STOP: fixture full-window TV is zero (vacuous)')
    return {'rule_k0_cases': checked, 'rules': len(rules), 'max_full_window_TV': max(full.values())}


def control_stop_counter(fx):
    called = []
    rule = ('reads R.A', ('R.A',), (lambda pre, inp: called.append(1) or inp.get('R.A') == 1))
    lanes = fx['null']['lanes']
    acc = sorted({n for n, _ in accessible(window_x(lanes[0][1], lanes[0][2]))})
    accepted = stop_domain_ok(rule[1], acc)
    if accepted:
        for m, o, a in lanes[:64]:
            run_stop(rule, accessible(window_x(o, a)), {'R.A': o['R.A']})
    require(not accepted and not called, 'CP-STOP-COUNTER: a stop rule reading R.A was evaluated')
    return {'rejected_before_evaluation': not accepted, 'evaluations': len(called)}


def branch_lanes():
    contexts = list(product((0, 1), repeat=6))
    lanes, masses = [], {}
    for i, ctx in enumerate(contexts):
        terminal = (ctx[4], ctx[5]) == (0, 1)
        if terminal and MUTANT == 'omit-terminal':
            continue
        m = Fraction(2*i+1, 4096)
        masses[i] = (m, terminal)
        for c in (0, 1):
            if terminal:
                for u in range(8):
                    lanes.append((m/16, {'c': c, 'K0@0': BOTTOM, 'Tail0@1': u, 'ctx': i}, {}))
            else:
                for k0, u in product(range(8), range(8)):
                    lanes.append((m/128, {'c': c, 'K0@0': k0, 'Tail0@1': u ^ k0, 'ctx': i}, {}))
    return lanes, masses


def control_branch():
    lanes, masses = branch_lanes()
    terminal = [i for i, (_, t) in masses.items() if t]
    require(len(masses) == 64 and len(terminal) == 16, 'CP-BRANCH: 48 continuing and 16 terminal contexts')
    mu = measures(lanes)
    tm = sum(masses[i][0] for i in terminal)
    cm = sum(m for m, t in masses.values() if not t)
    ok = True
    for c in (0, 1):
        bottom = sum(restrict(mu[c], BOTTOM).values())
        rest = sum(sum(restrict(mu[c], k).values()) for k in range(8))
        ok = ok and bottom == tm and rest == cm and bottom+rest == 1
    per_ctx = defaultdict(Fraction)
    for m, o, _ in lanes:
        if o['c'] == 0:
            per_ctx[o['ctx']] += 2*m
    ok = ok and all(per_ctx[i] == masses[i][0] for i in masses) and any(per_ctx[i] != 1 for i in masses)
    require(ok, 'CP-BRANCH: branch masses do not sum to the source-context masses')
    tables = tv_tables(mu)
    return {'contexts': len(masses), 'terminal_at_bottom': len(terminal),
            'bottom_mass': tm, 'continuing_mass': cm, 'TV_win_bottom': tables[BOTTOM][0]}


def control_precut(fx, geo):
    v = geo.v
    out = {}
    for name in ('null', 'pos'):
        lanes = fx[name]['lanes']
        view = (lambda o, a, e: tuple((n, o[n]) for n in ('R.B@2', 'R.D@2', 'K0@2', 'Wq@2', 'Wp@3')))
        mu = measures(lanes, view=view)
        out[name+'_precut_TV'] = tv(mu[0], mu[1])
    b5 = add(geo.ports[5][0], geo.ports[5][1], geo.S+4)
    k_slices = min(dist(b5, s) for s in geo.footprint)-(geo.L+3)
    incoming = [r[3] for r in geo.eta[1:14]]
    k_to_r = min(dist(k, geo.ports[5][0]) for k in incoming)-(geo.S+4)
    q9 = dist(b5, v.Q9)-(geo.L+2)
    require(all(x == 0 for x in out.values()), 'CP-PRECUT: pre-cut factor differs across c on the fixture')
    require(k_slices > 0 and k_to_r > 0 and q9 > 0, "CP-PRECUT: R's exclusion from K0 fails")
    out.update(b5_to_K0_slices_minus_tau=k_slices, incoming_keys_to_R_minus_S4=k_to_r,
               b5_to_q9_minus_L2=q9)
    return out


def walk_exact(obj, path='result'):
    if isinstance(obj, float):
        raise CheckFailure('CP-EXACT: float at '+path)
    if isinstance(obj, dict):
        for k, x in obj.items():
            walk_exact(x, path+'.'+str(k))
    elif isinstance(obj, (list, tuple)):
        for i, x in enumerate(obj):
            walk_exact(x, '%s[%d]' % (path, i))
    elif not (obj is None or isinstance(obj, (int, Fraction, str))):
        raise CheckFailure('CP-EXACT: non-exact type at '+path)


def strip_private(rec):
    if not isinstance(rec, dict):
        return rec
    return {k: v for k, v in rec.items() if not k.startswith('_')}


# --------------------------------------------------------------- the gate

class Gate:
    def __init__(self):
        self.open = False


def decide(gate, pre, geo):
    require(gate.open, 'CP-GATE: token requested before every control passed')
    holds = {k: pre[k]['holds'] for k in pre}
    rest = all(holds[k] for k in ('P2', 'P3', 'P4', 'P5', 'P6a', 'P6b'))
    if holds['P1'] and rest:
        zero = Fraction(0)
        tables = {BOTTOM: (zero, zero), 'every incoming-packet value': (zero, zero)}
        # Proof-derived, not measured: under P1-P6b and H-prior each tail
        # triple is a permutation of its own independent uniform bank triple.
        info = 'EMPTY'
        search, _ = actual_search(geo, None)
        return 'LA-EQUAL', tables, hidden_only(tables), info, search, None
    if not holds['P1'] and rest:
        first = pre['P1']['_first']
        search, found = actual_search(geo, first)
        if found:
            return 'LA-DIFFERENT', None, False, 'INFORMATIVE', search, None
        return 'LA-UNDETERMINED', None, 'UNKNOWN', 'UNKNOWN', search, ('P1', strip_private(first))
    failing = [k for k in ('P2', 'P3', 'P4', 'P5', 'P6a', 'P6b') if not holds[k]]
    search = {'trigger': None, 'S_size': None, 'derivation': 'not run',
              'outcome': 'not run: %s fails' % failing[0]}
    return 'LA-UNDETERMINED', None, 'UNKNOWN', 'UNKNOWN', search, \
        (failing[0], strip_private(pre[failing[0]].get('_first')))


def jsonable(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, set):
        return [jsonable(v) for v in sorted(x, key=repr)]
    return x


def execute(root):
    try:
        inp = load_inputs(root)
    except (OSError, ValueError, KeyError, AttributeError) as exc:
        raise CheckFailure('CP-PIN: input not loadable: %s' % type(exc).__name__)
    geo = Geometry(inp)
    gate = Gate()
    if MUTANT == 'token-before-controls':
        decide(gate, {}, geo)
    # Preconditions P1-P6b: measured exactly; a failure decides a token, not VOID.
    pre = {}
    ok, meas, first = p1_check(geo, geo.rays)
    pre['P1'] = {'checkpoint': 'CP-GEO-OWN', 'holds': ok, 'measured': meas,
                 'first_failure': strip_private(first), '_first': first}
    ok, meas, first, _ = p2_check(geo, geo.rays)
    pre['P2'] = {'checkpoint': 'CP-GEO-EXCL', 'holds': ok, 'measured': meas, 'first_failure': strip_private(first)}
    ok, meas, first, _ = p3_check(geo, geo.rays)
    pre['P3'] = {'checkpoint': 'CP-GEO-DISJ', 'holds': ok, 'measured': meas, 'first_failure': strip_private(first)}
    edges = equal_time_edges(geo, geo.rays)
    ok = p4_check(edges, lambda i: i)
    pre['P4'] = {'checkpoint': 'CP-ORDER', 'holds': ok, 'measured': {'equal_time_edges': sorted(edges)},
                 'first_failure': None if ok else {'edges': sorted(edges)}}
    ok, meas = p5_check(geo)
    pre['P5'] = {'checkpoint': 'CP-TORUS', 'holds': ok, 'measured': meas, 'first_failure': None}
    ok = p6a_check(rule_bits)
    pre['P6a'] = {'checkpoint': 'CP-PERM-A', 'holds': ok,
                  'measured': {'distinct_images': len({h(c) for c in range(8)})}, 'first_failure': None}
    ok, meas, first = p6b_check(rule_bits)
    pre['P6b'] = {'checkpoint': 'CP-PERM-B', 'holds': ok, 'measured': meas, 'first_failure': first}
    # Controls and countercontrols: any failure is VOID.
    fx = {'null': toy_fixture(), 'pos': toy_fixture(pins={'b': 5}, actuate=True),
          'access': toy_fixture(actuate=True), 'prior': toy_fixture(equal={'b': 's'}),
          'prior-other': toy_fixture(equal={'b': 'k'})}
    controls = [
        ('CP-RULE', lambda: control_rule(inp)),
        ('CP-POS', lambda: control_pos(fx)),
        ('CP-ACCESS', lambda: control_access(fx)),
        ('CP-PRIOR', lambda: control_prior(fx)),
        ('CP-MARG', control_marg),
        ('CP-LEAK', control_leak),
        ('CP-NULL', lambda: control_null(fx)),
        ('CP-SEARCH-COUNTER', control_search_counter),
        ('CP-SUPPORT', control_support),
        ('CP-HIDDEN', control_hidden),
        ('CP-INFO', lambda: control_info(fx)),
        ('CP-GEO-COUNTER', lambda: control_geo_counter(geo)),
        ('CP-BREAKPOINT', control_breakpoint),
        ('CP-ORDER-COUNTER', lambda: control_order_counter(edges)),
        ('CP-PERM-COUNTER', control_perm_counter),
        ('CP-READSET', lambda: control_readset(geo)),
        ('CP-STOP', lambda: control_stop(fx)),
        ('CP-STOP-COUNTER', lambda: control_stop_counter(fx)),
        ('CP-PRECUT', lambda: control_precut(fx, geo)),
        ('CP-BRANCH', control_branch),
    ]
    results, failed = {}, {}
    for name, fn in controls:
        try:
            results[name] = {'pass': True, 'measured': fn()}
        except Exception as exc:
            results[name] = {'pass': False, 'reason': str(exc) or type(exc).__name__}
            failed[name] = str(exc)
    fixture_searches = [results.get(n, {}).get('measured', {}) for n in ('CP-POS', 'CP-NULL')]
    keys = {'trigger', 'S_size', 'derivation', 'outcome'}
    srch = [s['search'] for s in fixture_searches if 'search' in s]
    if 'CP-SEARCH-COUNTER' in results and results['CP-SEARCH-COUNTER']['pass']:
        srch += list(results['CP-SEARCH-COUNTER']['measured'].values())
    if len(srch) == 4 and all(keys <= set(s) for s in srch):
        results['CP-SEARCH'] = {'pass': True, 'measured': {'fixture_records': len(srch)}}
    else:
        results['CP-SEARCH'] = {'pass': False, 'reason': 'CP-SEARCH: fixture search record incomplete'}
        failed['CP-SEARCH'] = results['CP-SEARCH']['reason']
    try:
        walk_exact({k: v for k, v in pre.items()}, 'preconditions')
        walk_exact(results, 'controls')
        results['CP-EXACT'] = {'pass': True, 'measured': {'floats_found': 0}}
    except CheckFailure as exc:
        results['CP-EXACT'] = {'pass': False, 'reason': str(exc)}
        failed['CP-EXACT'] = str(exc)
    failed_pre = sorted(pre[k]['checkpoint'] for k in pre if not pre[k]['holds'])
    if failed:
        return void(failed, failed_pre)
    gate.open = True
    token, tables, hidden, info, search, gap = decide(gate, pre, geo)
    require(keys <= set(search), 'CP-SEARCH: actual search record incomplete')
    results['CP-GATE'] = {'pass': True, 'measured': {'controls_passed_before_token': len(results)}}
    for k in pre:
        pre[k].pop('_first', None)
    result = {
        'schema': SCHEMA, 'status': 'TOKEN', 'token': token,
        'hidden_only': hidden, 'informativeness': info, 'named_gap': gap,
        'informativeness_basis': ('triangular proof: Pr(Tail=w | D\', eta) = 8^-(8(H*-L-5)) for every tail word w'
                                  if token == 'LA-EQUAL' else 'item 4 of the decision rule'),
        'TV_by_k0': None if tables is None else
        {str(k): {'TV_win': w, 'TV_acc': a} for k, (w, a) in tables.items()},
        'search': search, 'preconditions': pre, 'controls': results,
        'window': {'first_tick': 'L+6', 'Hstar': '2L', 'beta_triples': 8*(geo.H-geo.L-5),
                   'tail_ports': 8, 'k0_classes': 'incoming-packet values and BOTTOM (16 terminal contexts)',
                   'stop_policy_domain': 'A(X)-prefixes only'},
        'hypotheses': ['H-prior', 'H-inventory', 'H-access', 'H-rule', 'H-torus'],
        'pins': inp['digests'],
        'basis': 'exact geometry and controls; LA-EQUAL rests on the written chronological-triangular proof',
    }
    walk_exact(result)
    return 0, jsonable(result)


def void(failed, failed_pre):
    return 2, {'schema': SCHEMA, 'status': 'VOID', 'failed_controls': sorted(failed),
               'failed_preconditions': failed_pre, 'reasons': dict(sorted(failed.items()))}


def emit(code, result):
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    return code


def mutation_suite():
    report, ok_all = {}, True
    modes = (('normal', ['-I', '-B']), ('optimized', ['-I', '-O', '-B']))
    jobs = [(name, mode, flags) for name in MUTANTS for mode, flags in modes]
    done = {}
    for start in range(0, len(jobs), 4):
        procs = [(job, subprocess.Popen([sys.executable]+job[2]+[str(Path(__file__).resolve()),
                                         '--mutant', job[0]],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
                 for job in jobs[start:start+4]]
        for job, proc in procs:
            out, _ = proc.communicate()
            done[job[0], job[1]] = (proc.returncode, out)
    for name, (row, expect) in MUTANTS.items():
        entry = {'row': row, 'expected': list(expect)}
        for mode, _ in modes:
            rc, out = done[name, mode]
            try:
                data = json.loads(out)
            except ValueError:
                data = {}
            if not isinstance(data, dict):
                data = {}
            named = set(data.get('failed_controls', []))|set(data.get('failed_preconditions', []))
            caught = (rc == 2 and data.get('status') == 'VOID' and set(expect) <= named)
            entry[mode] = {'rc': rc, 'status': data.get('status'),
                           'failed': sorted(named), 'caught': caught}
            ok_all = ok_all and caught
        report[name] = entry
    print(json.dumps({'schema': SCHEMA+'.mutation-suite', 'mutants': report, 'all_caught': ok_all},
                     sort_keys=True, separators=(',', ':')))
    return 0 if ok_all else 1


def main():
    global MUTANT
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root', type=Path, default=SOURCE_ROOT)
    ap.add_argument('--expected', type=Path, default=EXPECTED)
    ap.add_argument('--mutant', choices=sorted(MUTANTS))
    ap.add_argument('--mutation-suite', action='store_true')
    ap.add_argument('--write-expected', action='store_true',
                    help='first execution only: write the expected JSON if absent')
    args = ap.parse_args()
    if args.mutation_suite:
        return mutation_suite()
    MUTANT = args.mutant
    try:
        code, result = execute(args.source_root)
    except Exception as exc:
        label = str(exc).split(':')[0] if str(exc).startswith('CP-') else 'INTERNAL-ERROR'
        return emit(*void({label: str(exc)}, []))
    if code != 0:
        return emit(code, result)
    text = json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n'
    if MUTANT is not None:
        sys.stdout.write(text)
        return 0
    if not args.expected.exists():
        if not args.write_expected:
            sys.stdout.write(text)
            return 3
        args.expected.write_text(text)
    elif args.expected.read_text() != text:
        sys.stdout.write(text)
        return 3
    sys.stdout.write(text)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
