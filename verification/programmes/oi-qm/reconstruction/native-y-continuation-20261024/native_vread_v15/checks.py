"""Native read v15: one native tick from q10 at L+1 into the declared whole-V read.

Standard library only, exact integers, no assert statements. Every required
control raises ControlFailure; main() then prints VOID and exits with status 2.
Inputs are read as data from the retained native package and pinned by hash.
"""
import argparse
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
        data[rel] = json.loads(raw.decode('utf-8'))
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
            'v14': data['native_decode_v14/result.json']}


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


def packed_world(kind, n, seed, cells):
    """Bit-parallel native evaluation; cells maps a t=0 position to its lane values."""
    lanes = len(next(iter(cells.values())))
    full = (1 << lanes)-1
    planted = {p: tuple(sum(((vals[i] >> (2-k)) & 1) << i for i in range(lanes))
                        for k in range(3)) for p, vals in cells.items()}

    @lru_cache(None)
    def get(t, p):
        if t == 0 and p in planted:
            return planted[p]
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


def scalar_world(kind, n, seed, assignment):
    @lru_cache(None)
    def get(t, p):
        if t == 0 and p in assignment:
            return assignment[p]
        if t in (-1, 0):
            return background(kind, seed, t, p)
        acc = 0
        for step in STEPS:
            acc ^= get(t-1, add(p, step))
        return get(t-2, p) ^ h(acc)
    return get


def native_key_controls():
    origin = (0, 0, 0)
    worlds = scalar_rows = 0
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
            for lane in (0, 3, 6):
                get = scalar_world(kind, n, seed, {key: lane})
                need(get(n+1, origin) == V[lane] and get(n-1, origin) == old[lane] and
                     all(get(n, w) == nb[w][lane] for w in STEPS),
                     'K3 scalar and packed evaluators agree')
                scalar_rows += 1
            worlds += 1
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
    return {'worlds_two_backgrounds_n1_to_4_three_seeds_six_keys': worlds,
            'scalar_comparisons': scalar_rows,
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


def local_sources():
    return {'O': (0, 0, 0), 'W': (0, -76, 76), 'E': (0, -78, 78), 'N': (0, S, S+156),
            'Q': (0, S, S+136), 'C': (0, S, S+150), 'G': (0, S, S+152), 'J': (0, S, S+154),
            'Kplus': (1, S, S+153), 'Kminus': (-1, S, S+153),
            'selector_y': (0, 2*S, 0), 'selector_plus': (T, S+P, 0),
            'selector_minus': (-T, S+P, 0), 'F10_pin': (-(L+1), S, 78),
            'z_source': (-48*L, -L, 0)}


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


def geometry(inventory):
    inherited, balls = ready_balls()
    inv = set(inventory)
    anchors = {
        'q10_axial': classify(add(Q10, (0, 0, 1), L+1), inv, balls),
        'E': classify((0, -78, 78), inv, balls),
        'N': classify((0, S, S+156), inv, balls),
        'F10_position': classify((-(L+1), S, 78), inv, balls),
        'F8_position': classify((-(L+1), S, 76), inv, balls),
        'port0_bank_T+2': classify((0, -2, 0), inv, balls),
        'q10_ready_interior': classify((0, S, 78+L), inv, balls),
    }
    need(anchors['q10_axial'][0] == 'PINNED', 'K5 anchor q10 axial pinned')
    need(anchors['E'][0] == 'PINNED' and anchors['N'][0] == 'PINNED', 'K5 anchor E,N pinned')
    need(anchors['F10_position'][0] == 'PINNED', 'K5 anchor F10 pinned')
    need(anchors['F8_position'][0] == 'FREE', 'K5 anchor F8 free')
    need(anchors['port0_bank_T+2'][0] == 'BANK', 'K5 anchor port-0 bank')
    need(tuple(anchors['q10_ready_interior']) == ('PINNED', 'ready ball'), 'K5 anchor q10 ready ball')
    need(receiver_info((0, -2, 0))[2], 'K5 anchor receiver reached by a port-0 bank cell')
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
                     'status': status, 'reason': reason,
                     'nearest_receiver': nearest, 'nearest_receiver_distance': near_text,
                     'receiver_reached_by_L+2': reached,
                     'operand_cell': e == (0, 0, 1)})
    f9 = add(Q9, (-1, 0, 0), L+2)
    need(min(dist(f9, p) for p, _, _ in PORTS)-L == 79, 'K6 Native A f9 public slack 79')
    banks = shell_banks()
    need(len(banks) == 8 and sum(1 for b in banks if b['active']) == 4, 'K6 shell bank count 8/4')
    need(all(b['distance_to_q9_over_L'] == 2 for b in banks if b['active']), 'K6 active banks at L+2')
    q10_ports = [(i, dist(Q10, p)) for i, (p, _, _) in enumerate(PORTS) if dist(Q10, p) < 10**6]
    return {'anchors': {k: list(v) for k, v in anchors.items()}, 'keys': keys,
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

def verdict(geo):
    others = [k for k in geo['keys'] if not k['operand_cell']]
    clean = [k for k in others if k['status'] == 'FREE' and not k['receiver_reached_by_L+2']]
    public = [k for k in others if k['status'] == 'FREE' and k['receiver_reached_by_L+2']]
    banks = [k for k in others if k['status'] == 'BANK']
    base = {'free_keys_unseen_by_public_records': [k['direction'] for k in clean],
            'free_keys_reaching_a_public_port_by_L+2': [k['direction'] for k in public],
            'bank_keys': [k['direction'] for k in banks]}
    if not clean:
        base.update({'outcome': 'NOT_DECIDED_BY_THIS_PLAN',
                     'statement': 'No non-q10 key cell is a free complement variable unseen by '
                                  'the public records through L+2; delivery and leakage need the '
                                  'full native V kernel, which this plan does not compute.'})
        return base
    names = ', '.join('%s key %s (nearest public receiver at distance %s)'
                      % (k['direction'], k['cell'], k['nearest_receiver_distance']) for k in clean)
    extra = ''
    if public:
        extra = (' The %s key %s is also a free complement variable but reaches public port %d '
                 'at distance %s, so it couples V to that port record; their joint law is not '
                 'computed here.') % (public[0]['direction'], public[0]['cell'],
                                      public[0]['nearest_receiver'],
                                      public[0]['nearest_receiver_distance'])
        if len(public) > 1:
            extra += ' %d further such keys exist.' % (len(public)-1)
    every = len(clean)+len(public)
    base.update({
        'outcome': 'NEGATIVE_FOR_CONSTRUCTION',
        'statement': (
            '%d of the 5 non-q10 key cells of q9 at L+2 are free complement variables under '
            'the native_route_v13 contract that no permitted record through L+2 depends on: '
            '%s. For each such key and every fixed value of all other initial variables, '
            'V=U_(L+2)(q9) is a permutation of the key triple, while the old q9 record, q10 at '
            'L+1 and every other permitted record through L+2 do not depend on it. (i) No '
            'nonconstant fixed readout of the whole V equals s for every complement value. '
            '(ii) If such a key is uniform given all other initial variables, V is uniform and '
            'independent of q10.A, s, the seeds and every other permitted record through L+2: '
            'the read is harmless and carries no operand. (iii) Delivery through this read '
            'needs at least these %d free key cells known (necessary, not sufficient: shared '
            'complement cells also enter V): pinning them (a preparation change) or reading '
            'their q9 neighbors at L+1 (an access change). Neither is adopted; the test stops '
            'there.%s') % (len(clean), names, every, extra)})
    return base


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=here.parent)
    args = parser.parse_args()
    try:
        data = load_inputs(args.source_root)
        controls = {'K2_key_lemma': key_lemma(),
                    'K3_native_key_permutation': native_key_controls(),
                    'K4_delivery_detector': detector_controls()}
        geo = geometry(data['sources'])
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
            'privacy of the V read under a complement law in which no free key is uniform',
            'multi-tick stages, other reads, other layouts, readiness extensions',
            'previous-slice key cells (not classified by this plan)',
            'Native A geometry with its own pool; acceptance predicate; carrier law',
            'any access rule or preparation change; A1 or A2 reconstruction; OI generally'],
    }
    print(json.dumps(result, sort_keys=True, indent=1))


if __name__ == '__main__':
    main()
