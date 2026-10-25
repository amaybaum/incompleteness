"""Native B q10 source-compatible seed injection; exact bit-packed native rule."""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


T = 185
P = 12*840**185
S = P+T
R = S+68
L = R+9
BASE = T+68
BUDGET = 20
ZERO = (0, 0, 0)
TR = tuple(product((0, 1), repeat=3))
UR = tuple((u, a, b, n) for u, a, b in product((0, 1), repeat=3) for n in range(8))
ROWS = tuple((x, u, my, mr, a, b, n)
             for x, u, my, mr, a, b in product((0, 1), repeat=6) for n in range(8))
UF = (1 << len(UR))-1
FULL = (1 << len(ROWS))-1
UINDEX = {r: i for i, r in enumerate(UR)}
RINDEX = {r: i for i, r in enumerate(ROWS)}
XM, UM, MY, MR = tuple(sum(r[j] << i for i, r in enumerate(ROWS)) for j in range(4))


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def xx(*qs):
    a = b = d = 0
    for q in qs:
        a ^= q[0]
        b ^= q[1]
        d ^= q[2]
    return a, b, d


def h(q):
    a, b, d = q
    return b, d, a ^ (b & d)


def hp(q, n):
    for _ in range(n % 12):
        q = h(q)
    return q


def lane(q, i):
    return tuple((w >> i) & 1 for w in q)


def code(q):
    return 4*q[0]+2*q[1]+q[2]


def dist(p, q):
    return sum(abs(x-y) for x, y in zip(p, q))


def ball(radius, center):
    for a in range(-radius, radius+1):
        for b in range(-radius+abs(a), radius-abs(a)+1):
            for d in range(-radius+abs(a)+abs(b), radius-abs(a)-abs(b)+1):
                yield center[0]+a, center[1]+b, center[2]+d


def odd(parts):
    total = 0
    for value in parts:
        if total & value:
            return False
        total |= value
    return True


def pack(function):
    return tuple(sum(function(*r)[j] << i for i, r in enumerate(UR)) for j in range(3))


SOURCES = {
    (0, 0, 0): pack(lambda u, a, b, n: (u, 0, 1)),
    (0, 0, -14): pack(lambda u, a, b, n: (u, 0, u)),
    (0, 0, -16): pack(lambda u, a, b, n: (u, 1 ^ u, 1)),
    (0, 0, -18): pack(lambda u, a, b, n: (u ^ b, a, u ^ a)),
    (1, 0, -17): pack(lambda u, a, b, n: (a ^ b, 0, a ^ b)),
    (-1, 0, -17): pack(lambda u, a, b, n: (a ^ b, a ^ b, a ^ b)),
    (0, 0, -20): pack(lambda u, a, b, n: TR[n]),
}


@lru_cache(None)
def direct_upper(t, x, y, z):
    if t < 0 or (t-x-y-z) % 2:
        return ZERO
    if min(abs(x-a)+abs(y-b)+abs(z-c) for a, b, c in SOURCES) > t:
        return ZERO
    if t == 0:
        return SOURCES.get((x, y, z), ZERO)
    ns = [direct_upper(t-1, x-1, y, z), direct_upper(t-1, x+1, y, z),
          direct_upper(t-1, x, abs(y-1), z), direct_upper(t-1, x, y+1, z),
          direct_upper(t-1, x, y, z-1), direct_upper(t-1, x, y, z+1)]
    return xx(direct_upper(t-2, x, y, z), h(xx(*ns)))


@lru_cache(None)
def upper_strip():
    values = {}

    def get(ell, x, y, n):
        y = abs(y)
        if ell < 0 or abs(x)+y > ell or (ell-abs(x)-y) % 2 or ell+abs(x)+y > BUDGET:
            return ZERO
        return values[ell, x, y][n]

    for ell in range(BUDGET+1):
        for x in range(-ell, ell+1):
            for y in range(ell-abs(x)+1):
                if (ell-abs(x)-y) % 2 or ell+abs(x)+y > BUDGET:
                    continue
                arr = [direct_upper(ell, x, y, 0)]
                values[ell, x, y] = arr
                for n in range(1, BASE+(BUDGET-ell)//2+1):
                    transverse = xx(*(get(ell-1, x+dx, y+dy, n)
                                      for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))))
                    arr.append(xx(get(ell-2, x, y, n),
                                  h(xx(arr[n-1], get(ell-2, x, y, n+1), transverse))))
    return values


@lru_cache(None)
def expand_upper(q):
    return tuple(sum(((w >> UINDEX[u, a, b, n]) & 1) << i
                     for i, (x, u, my, mr, a, b, n) in enumerate(ROWS)) for w in q)


@lru_cache(None)
def upper(t, pos):
    x, y, n = pos[0], abs(pos[1]), R-pos[2]
    ell = t-n
    if ell < 0 or abs(x)+y > ell or (ell-abs(x)-y) % 2:
        return ZERO
    need(ell+abs(x)+y <= BUDGET, 'signed upper strip coverage')
    return expand_upper(upper_strip()[ell, x, y][n-P])


@lru_cache(None)
def lower_levels(j):
    # Two lanes, x=0,1, with W=111 fixed.
    origin = (0, 2, 0)
    w = (3, 3, 3)
    first = h(xx(hp(origin, 75), hp(w, 75)))
    levels = [first]
    for ell in (1, 2):
        forcing = hp(w, 75+ell) if not (75 & ell) else ZERO
        levels.append(h(xx(levels[-1], forcing)))
    for k in range(1, j+1):
        forcing = hp(origin, k+75) if not (k & 75) else ZERO
        levels[0] = h(xx(levels[0], forcing))
        for ell in (1, 2):
            levels[ell] = h(xx(levels[ell], levels[ell-1]))
    return tuple(levels)


@lru_cache(None)
def direct_lower(t, x, y, z):
    if t < 0 or (t-x-y-z) % 2:
        return ZERO
    if min(abs(x)+abs(y)+abs(z), abs(x)+abs(y+76)+abs(z-76)) > t:
        return ZERO
    if t == 0:
        return (0, 2, 0) if (x, y, z) == (0, 0, 0) else (3, 3, 3) if (x, y, z) == (0, -76, 76) else ZERO
    ns = [direct_lower(t-1, abs(x-1), y, z), direct_lower(t-1, x+1, y, z),
          direct_lower(t-1, x, y-1, z), direct_lower(t-1, x, y+1, z),
          direct_lower(t-1, x, y, z-1), direct_lower(t-1, x, y, z+1)]
    return xx(direct_lower(t-2, x, y, z), h(xx(*ns)))


def expand_lower(q):
    return tuple(sum(((w >> x) & 1) << i
                     for i, (x, u, my, mr, a, b, n) in enumerate(ROWS)) for w in q)


CONTROLS = [((0, -S, -68), XM), ((0, S, -68), MY ^ MR),
            ((T, P, -68), MY), ((-T, P, -68), MR)]
ENTRIES = {(0, -9, 8): (176, 0), (0, -10, 9): (175, 1), (0, -11, 10): (174, 2)}


def base(t, pos):
    out = upper(t, pos)
    for source, bits in CONTROLS:
        ds = tuple(abs(x-y) for x, y in zip(source, pos))
        if sum(ds) <= t:
            need(sum(ds) == t, 'pre-R lower only at first front')
            if odd(ds):
                out = xx(out, hp((0, bits, 0), t))
    if t == R-1 and pos in ENTRIES:
        j, ell = ENTRIES[pos]
        expected = hp((0, XM, 0), t) if odd((0, S+pos[1], 68+pos[2])) else ZERO
        need(out == expected, 'entry has only isolated original-origin background')
        out = expand_lower(lower_levels(j)[ell])
    return out


def native_compute():
    end = (0, 0, 10)
    old = {pos: base(R-2, pos) for pos in ball(10, end)}
    now = {pos: base(R-1, pos) for pos in ball(11, end)}
    records = {}
    for tau in range(11):
        nxt = {}
        for pos in ball(10-tau, end):
            neighbors = [now[tuple(pos[j]+(sign if j == axis else 0) for j in range(3))]
                         for axis in range(3) for sign in (-1, 1)]
            nxt[pos] = xx(old[pos], h(xx(*neighbors)))
        records[tau] = nxt
        if tau == 0:
            need(nxt[0, 0, 0] == (XM, FULL, XM ^ UM), 'original qY preserved')
        if tau == 7:
            need(nxt[0, 0, 7] == (0, 0, XM ^ UM), 'q7 preserved')
        if tau == 8:
            need(nxt[0, 0, 8] == (0, XM ^ UM, 0), 'q8 preserved')
        old, now = now, nxt
    return now[end], records


def controller_audit(out, extended):
    family = []
    common = []
    joint = []
    targets = {key: [] for key in ('clean_A_xor_c', 'clean_B_xor_c', 'clean_D_xor_c',
                                  'clean_B_s', 'mixer', 'pair_BR')}
    coefficients = product(range(8) if extended else (0,), range(8), range(8))
    for B, C, V in coefficients:
        cells = {(s, c): set() for s, c in product((0, 1), repeat=2)}
        row_values = []
        for x, u, my, mr, a, b, c in product((0, 1), repeat=7):
            if (a, b) == (0, 1):
                continue
            s = x ^ u ^ a
            n = ((B if u ^ a else 0) ^ (C if a ^ b else 0) ^ (V if c else 0))
            got = lane(out, RINDEX[x, u, my, mr, a, b, n])
            cells[s, c].add(got)
            row_values.append((s, c, got))
        stable = all(len(v) == 1 for v in cells.values())
        injective_s = stable and all(cells[0, c] != cells[1, c] for c in (0, 1))
        fresh_effect = stable and any(cells[s, 0] != cells[s, 1] for s in (0, 1))
        joint_injective = stable and len(set(next(iter(v)) for v in cells.values())) == 4
        if injective_s:
            witness = {'B': B, 'C': C, 'V': V,
                       'codes_s0c0_s0c1_s1c0_s1c1': [code(next(iter(cells[s, c])))
                                                        for s, c in product((0, 1), repeat=2)],
                       'fresh_c_effect': fresh_effect, 'joint_injective': joint_injective}
            common.append(witness)
            if joint_injective:
                joint.append(witness)
        for name in targets:
            def wanted(s, c):
                return {'clean_A_xor_c': (s ^ c, 0, 0), 'clean_B_xor_c': (0, s ^ c, 0),
                        'clean_D_xor_c': (0, 0, s ^ c), 'clean_B_s': (0, s, 0),
                        'mixer': (c, s, c & s), 'pair_BR': (0, s, s ^ c)}[name]
            if all(got == wanted(s, c) for s, c, got in row_values):
                targets[name].append([B, C, V])
        family.append({'B': B, 'C': C, 'V': V,
                       'max_code_multiplicity_at_fixed_s_c': max(map(len, cells.values())),
                       'common_s_code': injective_s, 'joint_s_c_code': joint_injective})
    return {'candidate_count': len(family), 'common_s_codes': common,
            'joint_s_c_codes': joint, 'standard_targets': targets,
            'candidate_max_multiplicity_histogram':
            dict(sorted(Counter(r['max_code_multiplicity_at_fixed_s_c'] for r in family).items()))}


def pad_obstruction(out):
    count = 0
    for x, u, my, n in product((0, 1), (0, 1), (0, 1), range(8)):
        lo = lane(out, RINDEX[x, u, my, 0, 1, 0, n])
        hi = lane(out, RINDEX[x, u, my, 1, 1, 0, n])
        need(lo[1] ^ hi[1] == 1, 'accepted mask10 always reintroduces selector mR in B')
        count += 1
    return {'mR_toggle_pairs_mask10': count,
            'native_identity': 'q10.B(mR=1) XOR q10.B(mR=0)=1 when (a,b)=(1,0)',
            'example': {'x': 0, 'u': 0, 'a': 1, 'b': 0, 'Ncode': 0,
                        'q9': [0, 1, 0],
                        'q10_codes_for_pads_00_01_10_11':
                        [code(lane(out, RINDEX[0, 0, my, mr, 1, 0, 0]))
                         for my, mr in product((0, 1), repeat=2)]},
            'whole_earlier_public_records_equal_between_pad_variants': 'not established'}


def affine_solution(contexts, values):
    solutions = []
    for field in range(3):
        pivots = {}
        for k, value in zip(contexts, values):
            mask = 1+sum(v << (i+1) for i, v in enumerate(k))
            rhs = (value >> (2-field)) & 1
            while mask:
                pivot = mask.bit_length()-1
                if pivot in pivots:
                    prior, prior_rhs = pivots[pivot]
                    mask ^= prior
                    rhs ^= prior_rhs
                else:
                    pivots[pivot] = (mask, rhs)
                    break
            if not mask and rhs:
                return None
        solution = 0
        for pivot in sorted(pivots):
            mask, rhs = pivots[pivot]
            if rhs ^ ((mask & solution).bit_count() & 1):
                solution |= 1 << pivot
        need(all(((1+sum(v << (i+1) for i, v in enumerate(k))) & solution).bit_count() % 2
                 == (value >> (2-field)) & 1 for k, value in zip(contexts, values)),
             'affine source solution on every accepted known context')
        solutions.append(solution)
    return [sum(((solutions[j] >> i) & 1) << (2-j) for j in range(3)) for i in range(6)]


def pad_aware_single_source(out):
    contexts = [k for k in product((0, 1), repeat=5) if (k[3], k[4]) != (0, 1)]
    maps = []
    common = None
    sizes = []
    for u, my, mr, a, b in contexts:
        pairs = {}
        for n in range(8):
            pair = tuple(code(lane(out, RINDEX[s ^ u ^ a, u, my, mr, a, b, n]))
                         for s in (0, 1))
            if pair[0] != pair[1]:
                need(pair not in pairs, 'own-N permutation gives unique pair preimage')
                pairs[pair] = n
        maps.append(pairs)
        common = set(pairs) if common is None else common & set(pairs)
        sizes.append(len(common))
    survivors = []
    for pair in sorted(common):
        required = [pairs[pair] for pairs in maps]
        affine = affine_solution(contexts, required)
        survivors.append({'raw_code_pair_s0_s1': pair,
                          'source_N_codes_in_context_order': required,
                          'affine_coefficients_constant_u_mY_mR_a_b': affine})
    fresh_pairs = []
    for i, one in enumerate(survivors):
        for two in survivors[i+1:]:
            a = one['affine_coefficients_constant_u_mY_mR_a_b']
            b = two['affine_coefficients_constant_u_mY_mR_a_b']
            if a is not None and b is not None and a[1:] == b[1:]:
                fresh_pairs.append({'first_raw_pair': one['raw_code_pair_s0_s1'],
                                    'second_raw_pair': two['raw_code_pair_s0_s1'],
                                    'fresh_c_coefficient': a[0] ^ b[0]})
    incompatible = None
    for i in range(len(maps)):
        for j in range(i+1, len(maps)):
            if not (set(maps[i]) & set(maps[j])):
                incompatible = {'first_context_u_mY_mR_a_b': contexts[i],
                                'second_context_u_mY_mR_a_b': contexts[j],
                                'first_raw_pair_set': sorted(maps[i]),
                                'second_raw_pair_set': sorted(maps[j])}
                break
        if incompatible is not None:
            break
    # Mechanism check on every held-N unknown-sign pair. This algebraic
    # identity is extracted from the actual native table, not an isolated H.
    derivative_count = 0
    for u, my, mr, a, b, n in product((0, 1), (0, 1), (0, 1),
                                     (0, 1), (0, 1), range(8)):
        if (a, b) == (0, 1):
            continue
        zero = lane(out, RINDEX[u ^ a, u, my, mr, a, b, n])
        one = lane(out, RINDEX[1 ^ u ^ a, u, my, mr, a, b, n])
        need(zero[0] ^ one[0] == u, 'q10 A unknown-sign derivative is exactly old seed u')
        derivative_count += 1
    erased_pairs = 0
    branch_permutation = None
    for my, mr in product((0, 1), repeat=2):
        zero = [code(lane(out, RINDEX[1, 0, my, mr, 1, 1, n])) for n in range(8)]
        one = [code(lane(out, RINDEX[0, 0, my, mr, 1, 1, n])) for n in range(8)]
        need(zero == one, 'accepted u0 mask11 loses unknown sign at q10 for every N')
        need(len(set(zero)) == 8, 'new source still transported bijectively on erased-input branch')
        if branch_permutation is None:
            branch_permutation = zero
        need(zero == branch_permutation, 'erased-input branch also pad-independent')
        erased_pairs += 8
    return {'context_order': 'u,mY,mR,a,b lexicographic; only accepted00,10,11',
            'known_seed_contexts': len(contexts), 'pair_intersection_sizes_after_context': sizes,
            'common_raw_pairs': survivors, 'affine_fresh_c_pairs': fresh_pairs,
            'two_context_incompatibility_witness': incompatible,
            'unknown_s_A_derivative_pairs': derivative_count,
            'derivative_identity': 'q10.A(s=0,N) XOR q10.A(s=1,N)=u for every accepted known context and held N',
            'pointwise_X_loss_branch': {'u': 0, 'a': 1, 'b': 1,
                                       'unknown_s_pairs_checked_all_pads_N': erased_pairs,
                                       'q10_codes_N0_to_N7_for_either_s': branch_permutation,
                                       'previous_q9_s_retained': True,
                                       'q10_only_deterministic_X_decoder': 'impossible on all accepted worlds'},
            'verdict': 'common raw binary X code exists' if survivors
                       else 'no common raw binary X code for any pad-aware seed-only single N'}


def geometry(root):
    target = (0, S, 78)
    npos = (0, S, S+156)
    deadline = R+10
    need(dist(npos, target) == deadline, 'new source native first arrival')
    need(dist(npos, (0, S, 77)) == L+2, 'q9 not changed by new source')
    need(dist(npos, (0, S, 76)) == L+3, 'earlier q8 not changed by new source')
    geo = json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    need(len(geo) == 1479, 'old source inventory')
    need(all(dist(tuple(v['position']), target) >= deadline for v in geo),
         'new ready extension retains old compiled source geometry')
    need(all(tuple(v['position']) != npos for v in geo), 'new source overwrites no compiled coordinate')
    ports = [(0, T, 0), (0, 0, -8*T), (T, P, 0), (-T, P, 0),
             (4*T, P, 0), (0, S, 0), (12*R, 0, 0), (48*L, 0, 0)]
    deadlines = [T, T, S, S, S, S, R, L]
    ready = list(zip(ports, deadlines))
    ready += [((T, 0, 0), T), ((-T, 0, 0), T), ((4*T, 0, 0), T),
              ((0, S, -68), R), ((-12*R, 0, 0), R)]
    ready += [((0, S, 68+k), R+k) for k in range(10)]
    ready += [((-48*L, 0, 0), L)]
    need(all(dist(npos, center) > radius for center, radius in ready),
         'new N source outside all earlier ready prescriptions')
    directions = [(0, -1, 0), (0, 0, -1), (0, 1, 0), (0, 1, 0),
                  (0, 1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
    bank_pairs = 0
    min_slacks = []
    for p, d, start in zip(ports, directions, deadlines):
        axis = next(j for j in range(3) if d[j])
        times = {start+1, deadline}
        zero = (target[axis]-p[axis])*d[axis]
        if start+1 <= zero <= deadline:
            times.add(zero)
        gaps = []
        for t in times:
            source = tuple(v+t*w for v, w in zip(p, d))
            need(source != npos and dist(source, target) > deadline,
                 'entire original-time public bank excluded from new q10 ready pins')
            gaps.append(dist(source, target)-deadline)
            bank_pairs += 1
        min_slacks.append(min(gaps))
    f8 = (-(L+1), S, 76)
    f10 = (-(L+1), S, 78)
    need(dist(f8, target) == deadline+2, 'optional F8 resource remains outside')
    need(dist(f10, target) == deadline, 'optional F10 is replaced by boundary pin')
    need(all(dist(npos, p) > L for p in ports), 'new N cannot affect old public history through L')
    entries = []
    W = (0, -76, 76)
    for time, radius in ((R-2, 10), (R-1, 11)):
        for p in ball(radius, (0, 0, 10)):
            absolute = (p[0], S+p[1], 68+p[2])
            if dist(W, absolute) <= time:
                entries.append([time-R, list(p), dist(W, absolute)-time])
    expected = [[-1, [0, -11, 10], 0], [-1, [0, -10, 9], 0], [-1, [0, -9, 8], 0]]
    need(entries == expected, 'exact three-layer lower W cone entries')
    return {'source_inventory_rows': len(geo), 'prior_ready_regions_excluded_by_N': len(ready),
            'public_bank_breakpoint_cases': bank_pairs,
            'public_bank_minimum_positive_slack_P_coefficients':
            [{'P_coefficient': x//P, 'constant': x%P} for x in min_slacks],
            'W_entries': entries, 'F8_preserved': True, 'F10_uniform_factor_replaced': True,
            'N_does_not_change_old_public_record_through_L': True}


def main():
    ap = argparse.ArgumentParser()
    default = Path(__file__).resolve().parent.parent
    if not (default/'parallel_v3').exists():
        default = default/'checkpoint_v11'
    ap.add_argument('--source-root', type=Path, default=default)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    prov = json.loads((here/'PROVENANCE.json').read_text())
    for path, expected in prov['inputs'].items():
        need(hashlib.sha256((args.source_root/path).read_bytes()).hexdigest() == expected,
             'inherited bytes '+path)
    need(P % (12*840**BUDGET) == 0, 'actual signed upper period')
    need(P % (384*840**3) == 0, 'actual coupled three-layer lower period')
    data = upper_strip()
    upper_controls = 0
    for (ell, x, y), arr in data.items():
        for n in range(3):
            need(arr[n] == direct_upper(n+ell, x, y, n), 'direct full native upper cluster')
            upper_controls += len(UR)
    lower_controls = 0
    for j in range(9):
        for ell in range(3):
            need(lower_levels(j)[ell] == direct_lower(j+76+ell, 0, j, 76+ell),
                 'direct origin/W native three-layer first front')
            lower_controls += 2
    g = geometry(args.source_root)
    out, records = native_compute()
    prior = json.loads((args.source_root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    old_rows = 0
    for i, (x, u, my, mr, a, b, n) in enumerate(ROWS):
        index = 0
        for value, size in zip((x, u, my, mr, a, b, 4, 5, 7), (2, 2, 2, 2, 2, 2, 8, 8, 8)):
            index = size*index+value
        need(lane(records[9][0, 0, 9], i) == TR[int(prior[index], 16)],
             'all actual old q9 rows unchanged by initial extension and N')
        old_rows += 1
    # First-front permutation in the one new initial N triple, for each
    # actual old unknown/input/pad context. This is not an isolated H(q9) test.
    permutation_contexts = 0
    mask_dependence_rows = 0
    accepted_mask_dependence_rows = 0
    for row in product((0, 1), repeat=6):
        image = {lane(out, RINDEX[*row, n]) for n in range(8)}
        need(len(image) == 8, 'new axial source has nonvacuous full native response')
        permutation_contexts += 1
    for i, (x, u, my, mr, a, b, n) in enumerate(ROWS):
        if lane(out, i) != lane(out, RINDEX[x, u, 0, 0, a, b, n]):
            mask_dependence_rows += 1
            if (a, b) != (0, 1):
                accepted_mask_dependence_rows += 1
    first = controller_audit(out, False)
    extended = controller_audit(out, True) if not first['joint_s_c_codes'] else None
    pad = pad_obstruction(out)
    aware = pad_aware_single_source(out)
    result = {'schema': 'oi.native-outward-seed-controller.v12',
              'source_revision': prov['source_revision'],
              'checks': {'upper_direct_scalar_lanes': upper_controls,
                         'lower_direct_scalar_rows': lower_controls,
                         'q9_preserved_rows': old_rows,
                         'new_source_permutation_contexts': permutation_contexts,
                         'selector_pad_dependence_rows': mask_dependence_rows,
                         'accepted_selector_pad_dependence_rows': accepted_mask_dependence_rows,
                         'geometry': g},
              'q10_table_order': 'x,u,mY,mR,a,b,Ncode lexicographic; code=4A+2B+D',
              'q10_table_hex': ''.join(format(code(lane(out, i)), 'x') for i in range(len(ROWS))),
              'family64': first, 'family512': extended,
              'pad_obstruction': pad, 'pad_aware_single_N': aware,
              'verdict': {'joint_s_c_native_code': 'exists' if first['joint_s_c_codes'] or
                          (extended and extended['joint_s_c_codes']) else 'excluded_in_fixed_affine_family',
                          'native_predicate': 'not_constructed',
                          'single_q10_pointwise_X_transfer': 'excluded for any seed-only N in this fixed geometry',
                          'full_quantum_reset': 'not_constructed',
                          'initial_resource_contract': 'outward-ready extension and optional F10 factor replaced'}}
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
