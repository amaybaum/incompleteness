"""Independent two-tick cone and conditional instrument-kernel review."""
import argparse
import ast
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


TR = tuple(product((0, 1), repeat=3))
ZERO = (0, 0, 0)
P = ZERO
Q8, Q10, M = (0, 0, -1), (0, 0, 1), (-1, 0, 0)
F8, F10, F9 = (-1, 0, -1), (-1, 0, 1), (-2, 0, 0)
DIR = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
WEIGHTS = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def xx(*values):
    out = [0, 0, 0]
    for v in values:
        for i in range(3):
            out[i] ^= v[i]
    return tuple(out)


def h(q):
    a, b, d = q
    return b, d, a ^ (b & d)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def rawcode(q):
    return 4*q[0]+2*q[1]+q[2]


def selected(old, q, t):
    return old[1], q[1], t[2], t[1]


def flag(old, q, t):
    s, y, r, z = selected(old, q, t)
    return int(q[0]+2*q[2]+4*t[0] < WEIGHTS[y ^ s, r ^ s])


def mu(s):
    return {(s, s ^ a, s ^ b, z): F(n, 20)
            for (a, b), n in WEIGHTS.items() if n for z in (0, 1)}


def submeasure(s, success):
    return {(s, s ^ a, s ^ b, z): F(n if success else 8-n, 64)
            for (a, b), n in WEIGHTS.items() for z in (0, 1)}


def tv(a, b):
    return sum((abs(a.get(k, F())-b.get(k, F())) for k in a.keys() | b.keys()), F())/2


def density_determinant(law):
    total = sum(law.values(), F())
    require(total > 0, 'nonzero density measure')
    x = sum(p*(1-2*j[0]) for j, p in law.items())/total
    y = sum(p*(1-2*j[1]) for j, p in law.items())/total
    z = sum(p*(1-2*j[3]) for j, p in law.items())/total
    # Explicit Hermitian matrix [[a,b-ic],[b+ic,d]], computed independently
    # from normalized populations. Its determinant is a*d-b*b-c*c.
    a, d, b, c = (1+z)/2, (1-z)/2, x/2, y/2
    return a*d-b*b-c*c, (x, y, z), (a, d)


def two_tick(initial):
    # Complete backward cone of (origin,t=2) and its six t=1 neighbors:
    # all relevant initial sites have L1 radius <=2. No off-axis dependency
    # is omitted. This differs from the author's sparse infinite-step engine.
    first = {}
    for p in DIR:
        first[p] = h(xx(*(initial.get(add(p, e), ZERO) for e in DIR)))
    second = xx(initial.get(P, ZERO), h(xx(*first.values())))
    return first, second


def scaled_native_controls(author_result):
    worlds = inverse_cases = pair_controls = 0
    base_rows = defaultdict(list)
    repaired_rows = defaultdict(list)
    for old, f8, f10, f9 in product(TR, repeat=4):
        initial = {P: old, F8: f8, F10: f10, F9: f9}
        first, raw = two_tick(initial)
        q, t, m = first[Q8], first[Q10], first[M]
        recovered = xx(raw, h(xx(*first.values())))
        require(recovered == old, 'seven-site inverse on actual native two-tick world')
        require(q == h(xx(old, f8)) and t == h(xx(old, f10)) and
                m == h(xx(old, f8, f10, f9)), 'independent source-to-neighbor response')
        require(all(first[p] == h(old) for p in ((1, 0, 0), (0, 1, 0), (0, -1, 0))),
                'all remaining current neighbor operands retained')
        repaired_rows[old].append((q, t, m, raw))
        if f9 == ZERO:
            polar = (f8[1] & f10[2]) ^ (f10[1] & f8[2])
            require(raw == xx(old, (0, polar, 0)), 'quadratic shared-source native finite difference')
            base_rows[old].append((q, t, m, raw))
        worlds += 1
        inverse_cases += 1
    negatives = []
    for old, rows in base_rows.items():
        triples = Counter(row[:3] for row in rows)
        actual = {j: F(n, 64) for j, n in triples.items()}
        product_reference = {j: F(1, 512) for j in product(TR, repeat=3)}
        require(tv(actual, product_reference) == F(7, 8), 'pairwise freshness misses triple law')
        for i, j in ((0, 1), (0, 2), (1, 2)):
            require(Counter((r[i], r[j]) for r in rows) == Counter(product(TR, repeat=2)),
                    'native pairwise independence')
            pair_controls += 1
        raw_law = {j: F(n, 64) for j, n in Counter(r[3] for r in rows).items()}
        require(raw_law == {old: F(5, 8), xx(old, (0, 1, 0)): F(3, 8)}, 'native base raw distribution')
        omitted = Counter(xx(old, h(xx(q, t, h(old)))) for q, t, m, raw in rows)
        omitted = {j: F(n, 64) for j, n in omitted.items()}
        require(omitted == {j: F(1, 8) for j in TR} and tv(raw_law, omitted) == F(3, 4),
                'omitting shared M changes actual native whole raw record')
        if old[0]:
            continue
        pooled = Counter()
        posteriors = defaultdict(Counter)
        for q, t, m, raw in rows:
            if flag(old, q, t):
                j = selected(old, q, t)
                pooled[j] += 1
                posteriors[raw][j] += 1
        require(sum(pooled.values()) == 20 and {j: F(n, 20) for j, n in pooled.items()} == mu(old[1]),
                'base still has correct pooled full post-X target')
        for raw, count in sorted(posteriors.items()):
            det, xyz, diagonal = density_determinant(count)
            require(det < 0, 'each base successful raw branch is nonpositive')
            negatives.append({'s': old[1], 'old_R': old[2], 'raw': rawcode(raw),
                              'mass_given_accept': str(F(sum(count.values()), 20)),
                              'determinant': str(det)})
    require(negatives == author_result['base_accepted_raw_nonpositive_branches'],
            'independent eight exact posterior density matrices agree')
    for old, rows in repaired_rows.items():
        require(Counter(row[:3] for row in rows) == Counter(product(TR, repeat=3)),
                'actual three-source small native triangular map')
        require(Counter((q, t, raw) for q, t, m, raw in rows) == Counter(product(TR, repeat=3)),
                'actual small native full pool/raw independence')
    return {'native_worlds': worlds, 'seven_site_inverse_cases': inverse_cases,
            'pairwise_controls': pair_controls, 'negative_raw_posteriors': negatives}


def conditional_joint_kernel():
    worlds = success_cells = failure_cells = zero_cells = posteriors = 0
    for old, complement in product(TR, repeat=2):
        law = Counter()
        triples = Counter()
        for q, t, m in product(TR, repeat=3):
            raw = xx(old, h(xx(q, t, m, complement)))
            recovered = xx(raw, h(xx(q, t, m, complement)))
            require(recovered == old, 'arbitrary-complement fixed phase comparison')
            triples[q, t, raw] += 1
            if not old[0]:
                law[flag(old, q, t), raw, selected(old, q, t)] += 1
            worlds += 1
        require(triples == Counter(product(TR, repeat=3)), 'conditional pool/raw bijection all fixed backgrounds')
        if old[0]:
            continue
        for raw in TR:
            accepted = {}
            for success in (0, 1):
                target = submeasure(old[1], success)
                for j, mass in target.items():
                    actual = F(law[success, raw, j], 512)
                    require(actual == mass/8, 'whole raw/abstract-flag/outgoing code kernel')
                    if success:
                        success_cells += bool(actual)
                        zero_cells += not actual
                        accepted[j] = actual
                    else:
                        failure_cells += bool(actual)
            require(sum(accepted.values()) == F(5, 128), 'per-whole-raw success mass')
            det, xyz, diagonal = density_determinant(accepted)
            require(det == 0 and xyz == (1-2*old[1], 0, 0) and min(diagonal) >= 0,
                    'positive pure X density on every whole raw posterior')
            # Retain the actual failed selected coordinates, not a qubit state.
            require(sum(F(law[0, raw, j], 512) for j in submeasure(old[1], 0)) == F(11, 128),
                    'failed measure stays physical and normalized')
            for old_flag in (0, 1):
                offered = sum(n for (a, v, j), n in law.items() if v == raw and old_flag and a)
                require(offered == (20 if old_flag else 0), 'old terminal failure cannot offer carrier')
            posteriors += 1
    return {'conditional_worlds': worlds, 'positive_whole_raw_posteriors': posteriors,
            'nonzero_success_code_cells': success_cells, 'nonzero_failure_code_cells': failure_cells,
            'zero_success_code_cells': zero_cells}


def flag_controls():
    proper = {(a, v): (F(5, 16) if a else F(11, 16))/8 for a in (0, 1) for v in range(8)}
    errors = []
    marginal = []
    for f in range(256):
        deterministic = {(int(f >> v & 1), v): F(1, 8) for v in range(8)}
        errors.append(tv(deterministic, proper))
        marginal.append(abs(F(f.bit_count(), 8)-F(5, 16)))
    require(min(errors) == F(5, 16) and min(marginal) == F(1, 16),
            'whole raw port cannot be relabelled as abstract A')
    for s in (0, 1):
        target = mu(s)
        fake = {(s, y, r, z): F(1, 8) for y, r, z in product((0, 1), repeat=3)}
        require(tv(fake, target) == F(2, 5), 'independent matched-rate flag leaves wrong whole selected carrier')
        intended, unrelated = {}, {}
        for v in TR:
            intended[0, v, None] = unrelated[0, v, None] = F(11, 128)
            for j in set(target) | set(fake):
                intended[1, v, j] = F(5, 128)*target.get(j, F())
                unrelated[1, v, j] = F(5, 128)*fake.get(j, F())
        require(tv(intended, unrelated) == F(1, 8), 'full offered carrier/flag/raw error')
        # Calibrated R is a retained target coordinate, not a new native read.
        actual_r = sum(p for j, p in fake.items() if j[2] == s)
        target_r = sum(p for j, p in target.items() if j[2] == s)
        require(actual_r == F(1, 2) and target_r == F(9, 10), 'terminal R detects fake flag')
        require(F(5, 16)*(target_r-actual_r) == F(1, 8), 'R attains full error')
        # Both have the same XYZ Bloch vector; R is a consequential extra test.
        require(density_determinant(fake)[1] == density_determinant(target)[1],
                'XYZ moments alone miss the forbidden joint calibration')
    return {'boolean_functions': 256, 'best_raw_flag_joint_tv': '5/16',
            'best_flag_marginal_error': '1/16', 'unrelated_flag_conditional_carrier_tv': '2/5',
            'unrelated_flag_full_offered_carrier_tv': '1/8'}


def native_b_data_adapter(author_root, pins):
    # Extract one literal string as data; no author code is imported/executed.
    tree = ast.parse((author_root/'checks.py').read_text())
    table = next(node.value.value for node in tree.body if isinstance(node, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == 'NATIVE_B_Q10_HEX' for t in node.targets))
    require(len(table) == 512 and hashlib.sha256(table.encode()).hexdigest() == pins['native_B_table_sha256'],
            'retained Native B table bytes')
    lookup = dict(zip(((x, u, my, mr, a, b, n)
                       for x, u, my, mr, a, b in product((0, 1), repeat=6) for n in range(8)),
                      (int(v, 16) for v in table)))
    for k in product((0, 1), repeat=6):
        require({lookup[*k, n] for n in range(8)} == set(range(8)), 'Native B whole-N permutation')
    witness = [lookup[0, 0, my, mr, 1, 0, 0] for my, mr in product((0, 1), repeat=2)]
    require(witness == [1, 3, 1, 3], 'Native B selected-only pad witness')
    sensitivity = sum(value != lookup[x, u, 0, 0, a, b, n]
                      for (x, u, my, mr, a, b, n), value in lookup.items())
    require(sensitivity == 144, 'Native B full table pad sensitivity')
    pairs = 0
    for my, mr in product((0, 1), repeat=2):
        for n in range(8):
            require(lookup[0, 0, my, mr, 1, 1, n] == lookup[1, 0, my, mr, 1, 1, n],
                    'Native B accepted current-port sign collision')
            require(lookup[0, 0, my, mr, 1, 1, n] == (4, 2, 1, 0, 3, 5, 6, 7)[n],
                    'Native B pinned sign-fibre permutation')
            pairs += 1
    return {'data_rows': len(lookup), 'N_permutations': 64, 'pad_witness': witness,
            'pad_sensitive_rows': sensitivity, 'opposite_sign_collisions': pairs,
            'earlier_public_record_equality_proved': False,
            'reviewer_was_Native_B_author': True}


def main():
    ap = argparse.ArgumentParser()
    default = Path(__file__).resolve().parent.parent
    if not (default/'PLAN.md').exists() or not (default/'PROVENANCE.json').exists():
        default = default/'composition_v5'
    ap.add_argument('--author-root', type=Path, default=default)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    pins = json.loads((here/'INPUT-HASHES.json').read_text())
    for path, expected in pins['author_files'].items():
        raw = (args.author_root/path).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == expected, 'immutable author file '+path)
        require(hashlib.sha1(('blob '+str(len(raw))+'\0').encode()+raw).hexdigest()
                == pins['github_blobs'][path], 'published GitHub blob '+path)
    author_result = json.loads((args.author_root/'result.json').read_text())
    native = scaled_native_controls(author_result)
    kernel = conditional_joint_kernel()
    controls = flag_controls()
    adapter = native_b_data_adapter(args.author_root, pins)
    result = {'schema': 'oi.native-coupling-composition-review.v5',
              'author_sha': pins['author_sha'], 'author_file_pins': len(pins['author_files']),
              'native_scaled_controls': native, 'conditional_F9_kernel': kernel,
              'flag_controls': controls, 'Native_B_data_adapter': adapter,
              'verdict': 'ACCEPT_SCOPED_JOINT_KERNEL',
              'actual_scale_geometry': 'inherited Native A source theorem; not re-proved here',
              'physical_acceptance_flag': 'not_constructed',
              'new_observer_access': 'not_adopted',
              'native_reusable_instrument': 'not_constructed'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
