"""Native read v15: one native tick from q10 at L+1 into the declared whole-V read.

Standard library only, exact integers, no assert statements. Every required
control raises ControlFailure; main() then prints VOID and exits with status 2.
Inputs are read as data from the retained native package and pinned by hash.
"""
import argparse
import ast
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import sys


class ControlFailure(Exception):
    pass


def need(ok, label):
    if not ok:
        raise ControlFailure(label)


T = 185
P = 12*840**185
S = P+T
R = S+68
L = R+9
Q9 = (0, S, 77)
Q10 = (0, S, 78)
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
STEP_NAMES = {(1, 0, 0): '+x', (-1, 0, 0): '-x', (0, 1, 0): '+y',
              (0, -1, 0): '-y', (0, 0, 1): '+z', (0, 0, -1): '-z'}
PINS = {
    'native_route_v13/result.json':
        '762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02',
    'native_route_v13/review/result.json':
        '73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e4',
    'native_decode_v14/result.json':
        '3172e7d013c09cdcdf638a7ace68e0eff98bb3cd0411e8666b76a8226ad59034',
    'branch_v10/local-controller/symmetric-result.json':
        'd8e7c1f5841192165beefb3fe35b069cc14cc93f2faa2bd68619aa7748b3db2f',
    'parallel_v3/history_control/SOURCE-GEOMETRY.json':
        '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d',
    'native_route_v13/checks.py':
        '8c1bbc37f47b6ff7ad7ee67d719f058067e2e15e9a6a967adfb78ef57d1ed856',
}
TABLE_SHA256 = 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'
FEWEST_LAW = (1, 5, 1, 4, 1, 5)


def h(v):
    a, b, d = (v >> 2) & 1, (v >> 1) & 1, v & 1
    return (b << 2) | (d << 1) | (a ^ (b & d))


def fields(v):
    return (v >> 2) & 1, (v >> 1) & 1, v & 1


def dist(p, q):
    return sum(abs(x-y) for x, y in zip(p, q))


def add(p, q, k=1):
    return tuple(x+k*y for x, y in zip(p, q))


def key_text(e):
    base = ('0', 'S', '77')
    parts = []
    for j in range(3):
        if e[j] == 0:
            parts.append(base[j])
        elif base[j] == '0':
            parts.append(('' if e[j] > 0 else '-')+'(L+2)')
        else:
            parts.append(base[j]+('+' if e[j] > 0 else '-')+'(L+2)')
    return '('+','.join(parts)+')'


# ---------------------------------------------------------------- K1 inputs

def load_inputs(root):
    data = {}
    for rel, digest in sorted(PINS.items()):
        raw = (root/rel).read_bytes()
        need(hashlib.sha256(raw).hexdigest() == digest, 'K1 input pin '+rel)
        text = raw.decode('utf-8')
        data[rel] = json.loads(text) if rel.endswith('.json') else text
    route = data['native_route_v13/result.json']
    table = route['q10_table_hex']
    need(len(table) == 4096, 'K1 q10 table length')
    need(hashlib.sha256(table.encode()).hexdigest() == TABLE_SHA256, 'K1 recomputed table digest')
    need(route['table_sha256'] == TABLE_SHA256, 'K1 recorded table digest')
    review = data['native_route_v13/review/result.json']['independent_native_table']['sha256']
    need(review == TABLE_SHA256, 'K1 review table digest')
    need(route['table_order'].startswith('x,u,mY,mR,a,b,Ecode,Ncode'), 'K1 table order')
    q9hex = data['branch_v10/local-controller/symmetric-result.json']['q9_table_hex']
    need(len(q9hex) == 32768, 'K1 old q9 table length')
    sources = data['parallel_v3/history_control/SOURCE-GEOMETRY.json']['sources']
    need(len(sources) == 1479, 'K1 inherited source inventory')
    return {'q10': [int(c, 16) for c in table], 'q9hex': q9hex,
            'sources': [tuple(row['position']) for row in sources],
            'v14': data['native_decode_v14/result.json'],
            'route_checks': data['native_route_v13/checks.py']}


def q10_index(x, u, my, mr, a, b, e, n):
    index = 0
    for value, size in zip((x, u, my, mr, a, b, e, n), (2, 2, 2, 2, 2, 2, 8, 8)):
        index = size*index+value
    return index


def old_q9(q9hex, x, u, my, mr, a, b):
    # Row order of the retained symmetric q9 table, with the fixed W,Q,C,G
    # payload codes 4,5,7 used by native_route_v13's own q9 control.
    index = 0
    for value, size in zip((x, u, my, mr, a, b, 4, 5, 7), (2, 2, 2, 2, 2, 2, 8, 8, 8)):
        index = size*index+value
    return int(q9hex[index], 16)


CONTEXTS = tuple(k for k in product((0, 1), repeat=5) if (k[3], k[4]) != (0, 1))


def law_codes(coeffs, k):
    u, my, mr, a, b = k
    feature = 1 | (u << 1) | (my << 2) | (mr << 3) | (a << 4) | (b << 5)
    bits = [bin(c & feature).count('1') % 2 for c in coeffs]
    return 4*bits[0]+2*bits[1]+bits[2], 4*bits[3]+2*bits[4]+bits[5]


# ------------------------------------------------------------- K2 key lemma

def small_ball(radius):
    for a in range(-radius, radius+1):
        for b in range(-radius+abs(a), radius-abs(a)+1):
            for d in range(-radius+abs(a)+abs(b), radius-abs(a)-abs(b)+1):
                yield a, b, d


def reaches(c, w, t):
    d = dist(c, w)
    return d <= t and (t-d) % 2 == 0


def dependency_keys(nmax):
    """Dependency sets propagated through the second-order rule itself.

    dep(t,p) is the set of initial cells (slice,pos), slice 0 current and -1
    previous, on which U_t(p) can depend: U_t(p) reads U_(t-2)(p) and the six
    U_(t-1) neighbors.
    """
    memo = {}

    def dep(t, p):
        if (t, p) in memo:
            return memo[t, p]
        if t == 0:
            out = frozenset({(0, p)})
        elif t == -1:
            out = frozenset({(-1, p)})
        else:
            acc = set(dep(t-2, p))
            for step in STEPS:
                acc |= dep(t-1, add(p, step))
            out = frozenset(acc)
        memo[t, p] = out
        return out
    origin = (0, 0, 0)
    shared = mismatches = tested = 0
    for n in range(1, nmax+1):
        own = dep(n-1, origin)
        nb = {e: dep(n, e) for e in STEPS}
        keys = set()
        for e in STEPS:
            rest = set(own)
            for f in STEPS:
                if f != e:
                    rest |= nb[f]
            keys |= nb[e]-rest
        need(keys == {(0, tuple((n+1)*v for v in e)) for e in STEPS} |
             {(-1, tuple(n*v for v in e)) for e in STEPS},
             'K2 propagated keys are the axial cells of both slices')
        for c in small_ball(n+2):
            if dist(c, origin) == n+1 and len([v for v in c if v]) > 1:
                shared += sum(1 for e in STEPS if (0, c) in nb[e]) >= 2
            for w, tt in [(origin, n-1)]+[(e, n) for e in STEPS]:
                s = dep(tt, w)
                tested += 1
                mismatches += ((0, c) in s) != reaches(c, w, tt)
                mismatches += ((-1, c) in s) != reaches_previous(c, w, tt)
    need(mismatches == 0, 'K2 propagated cones equal the cone formula')
    need(shared > 0, 'K2 propagated countercontrol: shared off-axis cell not found')
    return {'n_range': [1, nmax], 'cells_times_targets_compared': tested,
            'current_keys_axial_(n+1)e_previous_keys_axial_ne': True,
            'shared_offaxis_current_cells': shared}


def reaches_previous(c, w, t):
    d = dist(c, w)
    return d <= t-1 and (t-1-d) % 2 == 0


def key_lemma():
    origin = (0, 0, 0)
    shared_seen = 0
    for n in range(2, 8):
        keys = set()
        for c in small_ball(n+2):
            # A current-slice cell influences (t,w) only when dist<=t and
            # t-dist is even: the second-order rule preserves the parity
            # of t+x+y+z.
            if reaches(c, origin, n-1):
                continue
            reached = [e for e in STEPS if reaches(c, e, n)]
            if len(reached) == 1:
                keys.add(c)
            if len(reached) >= 2 and dist(c, origin) == n+1 and sum(1 for v in c if v) > 1:
                shared_seen += 1
        need(keys == {tuple((n+1)*v for v in e) for e in STEPS}, 'K2 keys are exactly the axial cells')
    need(shared_seen > 0, 'K2 countercontrol: shared off-axis cell not found')
    return {'lattice_sizes_n': [2, 7], 'keys_equal_six_axial_cells': True,
            'shared_offaxis_cells_seen': shared_seen}


# --------------------------------------------------- K3/K4 small native worlds

BACKGROUNDS = ('sha256', 'polynomial')


def background(kind, seed, t, p):
    if kind == 'sha256':
        return hashlib.sha256(repr((seed, t, p)).encode()).digest()[0] & 7
    x, y, z = p
    return ((5*x*x+3*y*y+7*z*z+x*y+2*y*z+11*t+13*seed+x+4*z)
            ^ (x*z+3*seed*t+y*seed+(x*y*z))) & 7


def packed_world(kind, n, seed, cells, previous_cells=None):
    """Bit-parallel native evaluation; cells maps a t=0 position to its lane values."""
    previous_cells = previous_cells or {}
    lanes = len(next(iter(list(cells.values())+list(previous_cells.values()))))
    full = (1 << lanes)-1
    planted = {p: tuple(sum(((vals[i] >> (2-k)) & 1) << i for i in range(lanes))
                        for k in range(3)) for p, vals in cells.items()}
    planted_previous = {p: tuple(sum(((vals[i] >> (2-k)) & 1) << i for i in range(lanes))
                                 for k in range(3)) for p, vals in previous_cells.items()}

    @lru_cache(None)
    def get(t, p):
        if t == 0 and p in planted:
            return planted[p]
        if t == -1 and p in planted_previous:
            return planted_previous[p]
        if t in (-1, 0):
            v = background(kind, seed, t, p)
            return tuple(full if (v >> (2-k)) & 1 else 0 for k in range(3))
        acc = [0, 0, 0]
        for step in STEPS:
            w = get(t-1, add(p, step))
            for k in range(3):
                acc[k] ^= w[k]
        a, b, d = acc
        old = get(t-2, p)
        return (old[0] ^ b, old[1] ^ d, old[2] ^ (a ^ (b & d)))

    def value(t, p):
        tr = get(t, p)
        return [sum(((tr[k] >> i) & 1) << (2-k) for k in range(3)) for i in range(lanes)]
    return value


def scalar_world(kind, n, seed, assignment, previous_assignment=None):
    previous_assignment = previous_assignment or {}

    @lru_cache(None)
    def get(t, p):
        if t == 0 and p in assignment:
            return assignment[p]
        if t == -1 and p in previous_assignment:
            return previous_assignment[p]
        if t in (-1, 0):
            return background(kind, seed, t, p)
        acc = 0
        for step in STEPS:
            acc ^= get(t-1, add(p, step))
        return get(t-2, p) ^ h(acc)
    return get


def native_key_controls():
    origin = (0, 0, 0)
    worlds = scalar_rows = previous_worlds = 0
    counter = {kind: [] for kind in BACKGROUNDS}
    for kind, n, seed in product(BACKGROUNDS, range(1, 5), (0, 3, 8)):
        for e in STEPS:
            key = tuple((n+1)*v for v in e)
            value = packed_world(kind, n, seed, {key: list(range(8))})
            V = value(n+1, origin)
            old = value(n-1, origin)
            nb = {w: value(n, w) for w in STEPS}
            need(len(set(V)) == 8, 'K3 V is a permutation of the key')
            need(len(set(old)) == 1, 'K3 old-local q9 independent of key')
            need(len(set(nb[e])) == 8, 'K3 own neighbor is a permutation of the key')
            need(all(len(set(nb[w])) == 1 for w in STEPS if w != e),
                 'K3 other neighbors independent of key')
            for lane in range(8):
                get = scalar_world(kind, n, seed, {key: lane})
                need(get(n+1, origin) == V[lane] and get(n-1, origin) == old[lane] and
                     all(get(n, w) == nb[w][lane] for w in STEPS),
                     'K3 scalar and packed evaluators agree')
                scalar_rows += 1
            worlds += 1
            # Previous-slice key n*e at t=-1.
            pkey = tuple(n*v for v in e)
            value = packed_world(kind, n, seed, {}, {pkey: list(range(8))})
            V = value(n+1, origin)
            need(len(set(V)) == 8, 'K3 V is a permutation of the previous-slice key')
            need(len(set(value(n-1, origin))) == 1, 'K3 old-local q9 independent of previous-slice key')
            need(len(set(value(n, e))) == 8, 'K3 own neighbor permutes the previous-slice key')
            need(all(len(set(value(n, w))) == 1 for w in STEPS if w != e),
                 'K3 other neighbors independent of previous-slice key')
            for lane in range(8):
                get = scalar_world(kind, n, seed, {}, {pkey: lane})
                need(get(n+1, origin) == V[lane], 'K3 scalar and packed evaluators agree (previous)')
                scalar_rows += 1
            previous_worlds += 1
        off = (-n, 0, -1)
        value = packed_world(kind, n, seed, {off: list(range(8))})
        changed = [w for w in STEPS if len(set(value(n, w))) > 1]
        get = scalar_world(kind, n, seed, {off: 5})
        need(all(get(n, w) == value(n, w)[5] for w in STEPS), 'K3 countercontrol evaluators agree')
        counter[kind].append(len(changed) >= 2)
    # The check 'other neighbors independent of key' must be shown to fail on
    # native data: the off-axis cell has to change two neighbors in at least
    # one world. Per-world counts are reported for both background families.
    need(any(counter['sha256']), 'K3 countercontrol: off-axis cell must change two neighbors')
    need(all(any(counter['sha256'][3*i:3*i+3]) for i in range(4)),
         'K3 countercontrol: off-axis cell must change two neighbors for every n')
    return {'worlds_two_backgrounds_n1_to_4_three_seeds_six_keys': worlds,
            'previous_slice_key_worlds': previous_worlds,
            'scalar_comparisons_all_8_lanes': scalar_rows,
            'offaxis_cell_changes_two_neighbors_worlds': {
                kind: '%d of %d' % (sum(v), len(v)) for kind, v in counter.items()}}


def detector_controls():
    origin = (0, 0, 0)
    rows = 0
    for kind, n, seed in product(BACKGROUNDS, range(1, 5), (0, 3, 8)):
        operand = (0, 0, n+1)
        key = (-(n+1), 0, 0)
        lanes = list(product(range(8), range(8)))
        value = packed_world(kind, n, seed, {operand: [o for o, k in lanes],
                                       key: [k for o, k in lanes]})
        V = value(n+1, origin)
        table = {lanes[i]: V[i] for i in range(64)}
        for kv in range(8):
            need(len({table[o, kv] for o in range(8)}) == 8,
                 'K4 positive: pinned key lets V separate operands')
            need(table[0, kv] != table[1, kv], 'K4 positive: total variation 1')
        laws = [Counter(table[o, kv] for kv in range(8)) for o in range(8)]
        need(all(law == laws[0] for law in laws), 'K4 null: uniform key gives equal V laws')
        need(laws[0] == Counter({v: 1 for v in range(8)}), 'K4 null: V uniform')
        rows += 64
    return {'detector_rows': rows, 'pinned_key_TV': 1, 'uniform_key_TV': 0}


# ----------------------------------------------------- stage G: actual scale

PORTS = [((0, T, 0), (0, -1, 0), T), ((0, 0, -8*T), (0, 0, -1), T),
         ((T, P, 0), (0, 1, 0), S), ((-T, P, 0), (0, 1, 0), S),
         ((4*T, P, 0), (0, 1, 0), S), ((0, S, 0), (0, 1, 0), S),
         ((12*R, 0, 0), (-1, 0, 0), R), ((48*L, 0, 0), (1, 0, 0), L)]
RECEIVERS = [p for p, _, _ in PORTS]+[(-48*L, 0, 0)]


def ready_balls():
    balls = [(p, dl) for p, _, dl in PORTS]
    balls += [((T, 0, 0), T), ((-T, 0, 0), T), ((4*T, 0, 0), T),
              ((0, S, -68), R), ((-12*R, 0, 0), R)]
    balls += [((0, S, 68+k), R+k) for k in range(10)]
    balls += [((-48*L, 0, 0), L)]
    need(len(balls) == 24, 'K5 inherited ready-ball count')
    return balls, balls+[(Q10, L+1)]


def safe_value(node, env):
    """Evaluate a literal geometry expression without executing any code."""
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return node.value
    if isinstance(node, ast.Name):
        need(node.id in env, 'K5 route geometry: unknown name '+node.id)
        return env[node.id]
    if isinstance(node, (ast.Tuple, ast.List)):
        items = [safe_value(x, env) for x in node.elts]
        return tuple(items) if isinstance(node, ast.Tuple) else items
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -safe_value(node.operand, env)
    if isinstance(node, ast.BinOp) and type(node.op) in (ast.Add, ast.Sub, ast.Mult):
        a, b = safe_value(node.left, env), safe_value(node.right, env)
        return a+b if isinstance(node.op, ast.Add) else a-b if isinstance(node.op, ast.Sub) else a*b
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and not node.keywords
            and node.func.id in ('list', 'zip', 'range')):
        args = [safe_value(x, env) for x in node.args]
        if node.func.id == 'range':
            need(len(args) == 1 and 0 <= args[0] <= 100, 'K5 route geometry: range bound')
            return list(range(args[0]))
        if node.func.id == 'zip':
            return list(zip(*args))
        return list(args[0])
    if isinstance(node, ast.ListComp) and len(node.generators) == 1:
        g = node.generators[0]
        need(isinstance(g.target, ast.Name) and not g.ifs, 'K5 route geometry: comprehension form')
        return [safe_value(node.elt, dict(env, **{g.target.id: v})) for v in safe_value(g.iter, env)]
    raise ControlFailure('K5 route geometry: unsupported expression')


def route_geometry(text):
    """Read native_route_v13's ready list, ports, deadlines and directions as data."""
    tree = ast.parse(text)
    function = [f for f in tree.body if isinstance(f, ast.FunctionDef) and f.name == 'geometry']
    need(len(function) == 1, 'K5 route geometry: one geometry() function')
    env = {'T': T, 'P': P, 'S': S, 'R': R, 'L': L}
    found = {}
    for stmt in function[0].body:
        if (isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name)
                and stmt.targets[0].id in ('target', 'deadline', 'ports', 'deadlines', 'ready', 'directions')):
            found[stmt.targets[0].id] = safe_value(stmt.value, env)
            env[stmt.targets[0].id] = found[stmt.targets[0].id]
        elif (isinstance(stmt, ast.AugAssign) and isinstance(stmt.target, ast.Name)
              and stmt.target.id == 'ready' and isinstance(stmt.op, ast.Add)):
            found['ready'] = found['ready']+safe_value(stmt.value, env)
            env['ready'] = found['ready']
    need(set(found) == {'target', 'deadline', 'ports', 'deadlines', 'ready', 'directions'},
         'K5 route geometry: all lists found')
    route_writes_closed(function[0])
    return found


TRACKED = ('target', 'deadline', 'ports', 'deadlines', 'ready', 'directions')


def target_names(node):
    if isinstance(node, ast.Name):
        return {node.id}
    if isinstance(node, (ast.Tuple, ast.List)):
        out = set()
        for x in node.elts:
            out |= target_names(x)
        return out
    if isinstance(node, ast.Starred):
        return target_names(node.value)
    if isinstance(node, (ast.Subscript, ast.Attribute)):
        return target_names(node.value)
    return set()


def route_writes_closed(function):
    """Refuse the listed write forms on a tracked name outside the top-level
    statements route_geometry reads: assignment, augmented assignment, direct
    aliases, loop or comprehension targets, deletion, walrus, method calls on
    a tracked name, parameters and scope declarations. Indirect writes (for
    example list.extend(ready, ...), a container alias or a lambda argument)
    are not detected; the hash pin of native_route_v13/checks.py is what
    guarantees that the list read is the list used."""
    read = set()
    for stmt in function.body:
        if (isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name)
                and stmt.targets[0].id in TRACKED):
            read.add(id(stmt))
        elif (isinstance(stmt, ast.AugAssign) and isinstance(stmt.target, ast.Name)
              and stmt.target.id == 'ready' and isinstance(stmt.op, ast.Add)):
            read.add(id(stmt))
    tracked = set(TRACKED)
    for node in ast.walk(function):
        written = set()
        if isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and id(node) not in read:
            for target in (node.targets if isinstance(node, ast.Assign) else [node.target]):
                written |= target_names(target)
            # An alias such as r = ready (or r = ready[0]) would let a later
            # write escape the name check.
            if node.value is not None and isinstance(node.value, (ast.Name, ast.Subscript, ast.Attribute)):
                written |= target_names(node.value)
        elif isinstance(node, (ast.For, ast.AsyncFor, ast.comprehension)):
            written |= target_names(node.target)
        elif isinstance(node, ast.NamedExpr):
            written |= target_names(node.target)
        elif isinstance(node, ast.Delete):
            for target in node.targets:
                written |= target_names(target)
        elif isinstance(node, ast.withitem) and node.optional_vars is not None:
            written |= target_names(node.optional_vars)
        elif isinstance(node, (ast.Global, ast.Nonlocal)):
            written |= set(node.names)
        elif isinstance(node, ast.arg):
            written.add(node.arg)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            written.add(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            written |= {(a.asname or a.name).split('.')[0] for a in node.names}
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            written |= target_names(node.func.value)
        need(not (written & tracked), 'K5 route geometry: tracked list written outside the read statements')


READER_COUNTERCONTROLS = (
    'if deadline:\n        ready += [((0,0,0),1)]',
    'ready.append(((0,0,0),1))',
    'ready.extend([((0,0,0),1)])',
    'ready.insert(0,((0,0,0),1))',
    'ports[0]=(0,0,0)',
    'deadlines += [1]',
    'for directions in [[]]: pass',
    'alias = ready',
)


def reader_countercontrols(text):
    """Mutated in-memory copies of the pinned file must each be refused."""
    anchor = '    ready += [((-48*L,0,0),L)]\n'
    need(text.count(anchor) == 1, 'K5 reader countercontrol anchor line')
    refused = 0
    for insert in READER_COUNTERCONTROLS:
        copy = text.replace(anchor, anchor+'    '+insert+'\n')
        try:
            route_geometry(copy)
        except ControlFailure as failure:
            refused += str(failure) == 'K5 route geometry: tracked list written outside the read statements'
    need(refused == len(READER_COUNTERCONTROLS), 'K5 reader countercontrol: mutated route copy accepted')
    return refused


def local_sources():
    return {'O': (0, 0, 0), 'W': (0, -76, 76), 'E': (0, -78, 78), 'N': (0, S, S+156),
            'Q': (0, S, S+136), 'C': (0, S, S+150), 'G': (0, S, S+152), 'J': (0, S, S+154),
            'Kplus': (1, S, S+153), 'Kminus': (-1, S, S+153),
            'selector_y': (0, 2*S, 0), 'selector_plus': (T, S+P, 0),
            'selector_minus': (-T, S+P, 0), 'F10_pin': (-(L+1), S, 78),
            'z_source': (-48*L, -L, 0),
            # junction_v4 selector controls and reset pulses: the fourth
            # selector and the opposite pulse (Q is the other pulse).
            'selector_4T': (4*T, S+P, 0), 'reset_opposite': (0, S, -S-136)}


def bank_index(cell):
    for i, (port, d, dl) in enumerate(PORTS):
        axis = next(j for j in range(3) if d[j])
        if any(cell[j] != port[j] for j in range(3) if j != axis):
            continue
        t = (cell[axis]-port[axis])*d[axis]
        if dl < t <= 2*L:
            return i, t-dl
    return None


def classify(cell, inventory, balls):
    for name, pos in local_sources().items():
        if cell == pos:
            return 'PINNED', 'source '+name
    if cell in inventory:
        return 'PINNED', 'inherited source'
    bank = bank_index(cell)
    if bank is not None:
        return 'BANK', 'port %d index deadline+%d' % bank
    for center, radius in balls:
        if dist(cell, center) <= radius:
            return 'PINNED', 'ready ball'
    return 'FREE', 'complement'


def shell_banks():
    out = []
    for i, (port, d, dl) in enumerate(PORTS):
        axis = next(j for j in range(3) if d[j])
        rest = sum(abs(port[j]-Q9[j]) for j in range(3) if j != axis)
        t0 = (Q9[axis]-port[axis])*d[axis]
        slack = L+2-rest
        if slack < 0:
            continue
        for t in range(max(dl+1, t0-slack), min(2*L, t0+slack)+1):
            cell = add(port, d, t)
            dd = dist(cell, Q9)
            need(dd <= L+2, 'K6 shell bank enumeration')
            active = (sum(cell)-sum(Q9)-(L+2)) % 2 == 0
            reach = [STEP_NAMES[e] for e in STEPS if dist(cell, add(Q9, e)) <= L+1]
            out.append({'port': i, 'index_over_deadline': t-dl,
                        'distance_to_q9_over_L': dd-L, 'active': active,
                        'q9_neighbors_reached_by_L+1': reach if active else []})
    return out


def receiver_info(cell):
    nearest = min(range(len(RECEIVERS)), key=lambda i: dist(cell, RECEIVERS[i]))
    distance = dist(cell, RECEIVERS[nearest])
    slack = distance-L
    text = ('L%+d' % slack) if abs(slack) < 10**6 else str(distance)
    return nearest, text, slack <= 2


def classify_previous(cell, balls):
    # Previous-slice readiness is the ball of radius one less about each
    # centre (native_route_v13/PLAN.md; native_v11 'smaller previous ready
    # regions'). Sources and bank coordinates are current-slice triples.
    for center, radius in balls:
        if dist(cell, center) <= radius-1:
            return 'PINNED', 'previous ready ball'
    return 'FREE', 'complement'


def geometry(inventory, route_text):
    inherited, balls = ready_balls()
    route = route_geometry(route_text)
    need([tuple(x) for x in route['ready']] == inherited,
         'K5 ready list equals native_route_v13 geometry()')
    refused_copies = reader_countercontrols(route_text)
    need(route['target'] == Q10 and route['deadline'] == L+1,
         'K5 q10 extension equals native_route_v13 geometry()')
    need(route['ports'] == [p for p, _, _ in PORTS] and route['deadlines'] == [dl for _, _, dl in PORTS]
         and route['directions'] == [d for _, d, _ in PORTS],
         'K5 ports, deadlines and bank directions equal native_route_v13 geometry()')
    inv = set(inventory)
    anchors = {
        'q10_axial': classify(add(Q10, (0, 0, 1), L+1), inv, balls),
        'E': classify((0, -78, 78), inv, balls),
        'N': classify((0, S, S+156), inv, balls),
        'F10_position': classify((-(L+1), S, 78), inv, balls),
        'F8_position': classify((-(L+1), S, 76), inv, balls),
        'port0_bank_T+2': classify((0, -2, 0), inv, balls),
        'q10_ready_interior': classify((0, S, 78+L), inv, balls),
        'selector_4T': classify((4*T, S+P, 0), inv, balls),
        'reset_opposite': classify((0, S, -S-136), inv, balls),
    }
    need(tuple(anchors['q10_axial']) == ('PINNED', 'source N'), 'K5 anchor q10 axial is source N')
    need(tuple(anchors['E']) == ('PINNED', 'source E') and tuple(anchors['N']) == ('PINNED', 'source N'),
         'K5 anchor E,N are their declared sources')
    need(tuple(anchors['F10_position']) == ('PINNED', 'source F10_pin'), 'K5 anchor F10 is its pin')
    need(tuple(anchors['selector_4T']) == ('PINNED', 'source selector_4T') and
         tuple(anchors['reset_opposite']) == ('PINNED', 'source reset_opposite'),
         'K5 anchor junction_v4 selector and reset pulse are declared sources')
    need(anchors['F8_position'][0] == 'FREE', 'K5 anchor F8 free')
    need(anchors['port0_bank_T+2'][0] == 'BANK', 'K5 anchor port-0 bank')
    need(tuple(anchors['q10_ready_interior']) == ('PINNED', 'ready ball'), 'K5 anchor q10 ready ball')
    need(receiver_info((0, -2, 0))[2], 'K5 anchor receiver reached by a port-0 bank cell')
    previous_anchors = {'previous_q9': classify_previous(Q9, balls),
                        'previous_N_position': classify_previous((0, S, S+156), balls)}
    need(tuple(previous_anchors['previous_q9']) == ('PINNED', 'previous ready ball'),
         'K5 anchor previous q9 pinned')
    need(tuple(previous_anchors['previous_N_position']) == ('FREE', 'complement'),
         'K5 anchor previous N position free')
    anchors.update(previous_anchors)
    need(receiver_info((-(L+1), S, 76))[1:] == ('L+77', False), 'K6 Native A f8 public slack 77')
    # K6: E and N avoid every inherited ready ball, as native_route_v13 checks.
    for pos in ((0, -78, 78), (0, S, S+156)):
        need(all(dist(pos, c) > r for c, r in inherited), 'K6 E,N avoid inherited ready balls')
    keys = []
    for e in STEPS:
        cell = add(Q9, e, L+2)
        w = add(Q9, e)
        need(dist(cell, w) == L+1 and dist(cell, Q9) == L+2, 'G key reaches own neighbor')
        need(all(dist(cell, add(Q9, f)) == L+3 for f in STEPS if f != e), 'G key private')
        status, reason = classify(cell, inv, balls)
        nearest, near_text, reached = receiver_info(cell)
        keys.append({'direction': STEP_NAMES[e], 'cell': key_text(e),
                     'ready_balls_containing': [i for i, (c, r) in enumerate(balls)
                                                if dist(cell, c) <= r],
                     'ready_margin': min(dist(cell, c)-r for c, r in balls),
                     'balls_at_ready_margin': [i for i, (c, r) in enumerate(balls)
                                               if dist(cell, c)-r == min(dist(cell, cc)-rr
                                                                         for cc, rr in balls)],
                     'status': status, 'reason': reason,
                     'nearest_receiver': nearest, 'nearest_receiver_distance': near_text,
                     'receiver_reached_by_L+2': reached,
                     'operand_cell': e == (0, 0, 1)})
    previous_keys = []
    for e in STEPS:
        cell = add(Q9, e, L+1)
        need(dist(cell, add(Q9, e)) == L and dist(cell, Q9) == L+1 and
             all(dist(cell, add(Q9, f)) == L+2 for f in STEPS if f != e), 'G previous key private')
        status, reason = classify_previous(cell, balls)
        nearest = min(range(len(RECEIVERS)), key=lambda i: dist(cell, RECEIVERS[i]))
        distance = dist(cell, RECEIVERS[nearest])
        previous_keys.append({
            'direction': STEP_NAMES[e], 'cell': key_text(e).replace('(L+2)', '(L+1)'),
            'status': status, 'reason': reason,
            'previous_ready_margin': min(dist(cell, c)-(r-1) for c, r in balls),
            'nearest_receiver': nearest,
            'nearest_receiver_distance': ('L%+d' % (distance-L)) if abs(distance-L) < 10**6 else str(distance),
            # A previous-slice cell influences (t,w) only if dist <= t-1.
            'receiver_reached_by_L+2': distance <= L+1,
            'operand_cell': e == (0, 0, 1)})
    f9 = add(Q9, (-1, 0, 0), L+2)
    need(min(dist(f9, p) for p, _, _ in PORTS)-L == 79, 'K6 Native A f9 public slack 79')
    banks = shell_banks()
    need(len(banks) == 8 and sum(1 for b in banks if b['active']) == 4, 'K6 shell bank count 8/4')
    need(all(b['distance_to_q9_over_L'] == 2 for b in banks if b['active']), 'K6 active banks at L+2')
    q10_ports = [(i, dist(Q10, p)) for i, (p, _, _) in enumerate(PORTS) if dist(Q10, p) < 10**6]
    return {'anchors': {k: list(v) for k, v in anchors.items()}, 'keys': keys,
            'previous_slice_keys': previous_keys,
            'ready_list_equals_native_route_v13_geometry': True,
            'route_reader_mutated_copies_refused': refused_copies,
            'largest_ready_radius_over_L': max(r for _, r in balls)-L,
            'local_sources_declared': len(local_sources()),
            'ready_ball_order': 'ports 0-7 with their deadlines; (T,0,0),(-T,0,0),(4T,0,0) radius T; '
                                '((0,S,-68),R); ((-12R,0,0),R); ((0,S,68+k),R+k) for k=0..9; '
                                '((-48L,0,0),L); B_(L+1)(q10)',
            'ports_within_10^6_of_q10': q10_ports,
            'shell_banks': banks, 'inherited_ready_balls': len(inherited),
            'inherited_sources': len(inv)}


# --------------------------------------------- table-level preserved results

def table_checks(data):
    q10, q9hex, v14 = data['q10'], data['q9hex'], data['v14']
    rows = 0
    for x, u, my, mr, a, b in product((0, 1), repeat=6):
        if (a, b) == (0, 1):
            continue
        s = x ^ u ^ a
        need(old_q9(q9hex, x, u, my, mr, a, b) == 4*0+2*s+(s ^ a ^ b), 'K6 old q9 is (0,s,s^a^b)')
        rows += 1
    need(rows == 48, 'K6 accepted old rows')
    counts = v14['readout_solution_counts']
    need(len(counts) == 254 and counts[240-1] == 1456, 'K6 v14 q10.A law count')
    entry = [r for r in v14['post_hoc_degree_one_readouts'] if r['readout_bits'] == 240]
    need(len(entry) == 1 and tuple(entry[0]['fewest_seed_law_field_coefficients_EA_EB_ED_NA_NB_ND'])
         == FEWEST_LAW, 'K6 v14 fewest-seed law')
    per_s = {0: set(), 1: set()}
    cancel = 0
    for k in CONTEXTS:
        u, my, mr, a, b = k
        e, n = law_codes(FEWEST_LAW, k)
        for x in (0, 1):
            s = x ^ u ^ a
            c = q10[q10_index(x, u, my, mr, a, b, e, n)]
            need(fields(c)[0] == s, 'K6 fewest law gives q10.A=s')
            p = old_q9(q9hex, x, u, my, mr, a, b)
            need(fields(c)[0] ^ fields(p)[2] == a ^ b, 'D1 q10.A XOR p.D is a XOR b')
            cancel += 1
            per_s[s].add(c)
    # Under a uniform FREE key, for every accepted row of this law and every
    # fixed residual of the other four neighbors, V ranges over all 8 codes.
    uniform_rows = 0
    for k in CONTEXTS:
        u, my, mr, a, b = k
        e, n = law_codes(FEWEST_LAW, k)
        for x in (0, 1):
            c = q10[q10_index(x, u, my, mr, a, b, e, n)]
            p = old_q9(q9hex, x, u, my, mr, a, b)
            for rest in range(8):
                Vs = Counter(p ^ h(c ^ m ^ rest) for m in range(8))
                need(Vs == Counter({v: 1 for v in range(8)}), 'G uniform key gives uniform V on table rows')
                uniform_rows += 1
    return {'accepted_old_q9_rows': rows, 'v14_q10A_law_count': 1456,
            'fewest_law_rows_q10A_equals_s': cancel,
            'fewest_law_q10A_xor_pD_equals_a_xor_b_rows': cancel,
            'fewest_law_distinct_q10_codes_s0_s1': [len(per_s[0]), len(per_s[1])],
            'uniform_key_table_rows_x_residuals': uniform_rows}


def read_algebra():
    for p in range(8):
        image = {p ^ h(sig) for sig in range(8)}
        need(len(image) == 8, 'D1 Sigma to V bijective given p')
        for sig in range(8):
            v = p ^ h(sig)
            pa, pb, pd = fields(p)
            sa, sb, sd = fields(sig)
            need(fields(v) == (pa ^ sb, pb ^ sd, pd ^ sa ^ (sb & sd)), 'D1 V field formulas')
    return {'V.A': 'p.A XOR Sigma.B', 'V.B': 'p.B XOR Sigma.D',
            'V.D': 'p.D XOR Sigma.A XOR Sigma.B*Sigma.D',
            'given_p_V_determines_whole_Sigma': True}


# ------------------------------------------------------------------- verdict

def plural(n, one, many):
    return '%d %s' % (n, one if n == 1 else many)


def key_list(keys):
    return ', '.join('%s key %s' % (k['direction'], k['cell']) for k in keys)


def verdict(geo):
    others = [k for k in geo['keys'] if not k['operand_cell']]
    clean = [k for k in others if k['status'] == 'FREE' and not k['receiver_reached_by_L+2']]
    public = [k for k in others if k['status'] == 'FREE' and k['receiver_reached_by_L+2']]
    banks = [k for k in others if k['status'] == 'BANK']
    previous = [k for k in geo['previous_slice_keys'] if not k['operand_cell'] and k['status'] == 'FREE']
    base = {'free_keys_unseen_by_public_records': [k['direction'] for k in clean],
            'free_keys_reaching_a_public_port_by_L+2': [k['direction'] for k in public],
            'bank_keys': [k['direction'] for k in banks],
            'free_previous_slice_keys': [k['direction'] for k in previous],
            'outcome_rule_uses': 'current-slice keys, as preregistered'}
    if not clean:
        base.update({'outcome': 'NOT_DECIDED_BY_THIS_PLAN',
                     'statement': 'No non-q10 current-slice key cell is a free complement variable '
                                  'unseen by the public records through L+2; delivery and leakage '
                                  'need the full native V kernel, which this plan does not compute.'})
        return base
    names = ', '.join('%s key %s (nearest public receiver at distance %s)'
                      % (k['direction'], k['cell'], k['nearest_receiver_distance']) for k in clean)
    text = (
        '%s of the 5 non-q10 current-slice key cells of q9 at L+2 %s free complement '
        'variables under the native_route_v13 contract that no permitted record through L+2 '
        'depends on: %s. For each such key and every fixed value of all other initial '
        'variables, V=U_(L+2)(q9) is a permutation of the key triple, while the old q9 record '
        'and every other permitted record through L+2 do not depend on it (nor does the private '
        'cell q10 at L+1). (i) No fixed readout of the whole V equals s for every complement '
        'value. (ii) If such a key is uniform given all other initial variables, V is uniform '
        'and independent of q10.A, s, the seeds and every other permitted record through L+2: '
        'under a uniform free key the read is harmless and carries no operand. (iii) Delivery '
        'through this read needs the %s known, by pinning (a preparation change) or by reading '
        'the q9 %s at L+1 (an access change).') % (
            len(clean), 'is a' if len(clean) == 1 else 'are', names,
            plural(len(clean), 'unseen free key', 'unseen free keys'),
            'neighbor' if len(clean) == 1 else 'neighbors')
    if public:
        text += (' The %s %s also free and %s a public port by L+2 (%s); %s must also be '
                 'determined, by pinning, by reading the q9 %s at L+1, or from the permitted port '
                 'record, which is not computed here. If an unseen free key is uniform, V is '
                 'independent of that port record by (ii); otherwise their joint law is not '
                 'computed.') % (
            key_list(public), 'is' if len(public) == 1 else 'are',
            'reaches' if len(public) == 1 else 'reach',
            ', '.join('port %d at distance %s' % (k['nearest_receiver'], k['nearest_receiver_distance'])
                      for k in public),
            'it' if len(public) == 1 else 'they',
            'neighbor' if len(public) == 1 else 'neighbors')
    if previous:
        text += (' The previous-slice %s %s also free; %s must also be determined in one of '
                 'these ways.') % (key_list(previous), 'is' if len(previous) == 1 else 'are',
                                   'it' if len(previous) == 1 else 'each')
    text += (' These are necessary conditions, not sufficient: shared complement cells also '
             'enter V. Neither change is adopted; the test stops there. The classification, and '
             'so the outcome, is conditional on the declared ready-cone, source and bank inventory '
             'shared with native_route_v13 being complete: no undeclared readiness, preparation or '
             'correlation, and no record in the lineage with a deadline beyond L%+d (the largest '
             'declared ready radius used). Part (ii) is conditional in addition on a uniform free '
             'key, which the inherited independent-uniform complement prior of junction_v4 '
             'supplies where that inherited prior is retained.') % geo['largest_ready_radius_over_L']
    base.update({'outcome': 'NEGATIVE_FOR_CONSTRUCTION', 'statement': text})
    return base


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=here.parent)
    args = parser.parse_args()
    try:
        data = load_inputs(args.source_root)
        controls = {'K2_key_lemma': key_lemma(),
                    'K2_dependency_propagation': dependency_keys(6),
                    'K3_native_key_permutation': native_key_controls(),
                    'K4_delivery_detector': detector_controls()}
        geo = geometry(data['sources'], data['route_checks'])
        table = table_checks(data)
        algebra = read_algebra()
    except ControlFailure as failure:
        print('VOID: %s' % failure)
        sys.exit(2)
    except Exception as failure:
        import traceback
        traceback.print_exc()
        print('VOID: unexpected %s' % type(failure).__name__)
        sys.exit(2)
    result = {
        'schema': 'oi.native-vread.v15',
        'base': 'bef79f6f3daec0b734a7d9c6a9423ed634852818',
        'inputs_sha256': PINS, 'q10_table_sha256': TABLE_SHA256,
        'permitted_reads_used': [
            'eight old public ports, full raw triples at every tick through L+2',
            'old whole-q9 terminal record at L',
            'Native A single whole-V read: whole q9 triple at L+2'],
        'candidate_stage': 'unchanged native update V=U_L(q9) XOR H(XOR of six q9 neighbors at L+1)',
        'controls': controls, 'geometry': geo, 'table': table,
        'diagnostic_read_algebra': algebra,
        'verdict': verdict(geo),
        'not_established': [
            'completeness of the declared ready-cone, source and bank inventory shared with '
            'native_route_v13 (no undeclared readiness, preparation or correlation; no record '
            'in the lineage with a deadline beyond L+1); the outcome is conditional on it',
            'privacy of the V read under a complement law in which no free key is uniform',
            'multi-tick stages, other reads, other layouts, readiness extensions',
            'previous-slice keys enter (iii) only; the outcome rule uses current-slice keys',
            'Native A geometry with its own pool; acceptance predicate; carrier law',
            'any access rule or preparation change; A1 or A2 reconstruction; OI generally'],
    }
    print(json.dumps(result, sort_keys=True, indent=1))


if __name__ == '__main__':
    main()
