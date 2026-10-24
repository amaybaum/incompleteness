"""Separate-engine finite-menu A2 review. No author code is imported."""
from fractions import Fraction as F
from itertools import product
from math import isqrt, lcm
from pathlib import Path
from collections import Counter
from bisect import bisect_right
import hashlib
import json
import argparse


def require(value, message):
    if not value:
        raise RuntimeError(message)


def inner(a, b):
    return sum((x*y for x, y in zip(a, b)), F())


def negative(a):
    return tuple(-x for x in a)


def apply(a, v):
    return tuple(inner(row, v) for row in a)


def compose(a, b):
    return tuple(tuple(sum(a[i][j]*b[j][k] for j in range(3))
                       for k in range(3)) for i in range(3))


IDENTITY = tuple(tuple(F(i == j) for j in range(3)) for i in range(3))
AXES = {'X': (F(1), F(0), F(0)), 'Y': (F(0), F(1), F(0)),
        'Z': (F(0), F(0), F(1)), 'a': (F(3, 5), F(4, 5), F(0))}
BASE = dict(AXES, p=(F(2, 3), F(-2, 3), F(1, 3)),
            q=(F(2, 3), F(-2, 3), F(-1, 3)))
RAYS = {name+suffix: tuple(sign*x for x in v)
        for name, v in BASE.items() for sign, suffix in ((1, '+'), (-1, '-'))}
DECLARED = {
    'H': ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
    'S': ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
    'R': ((F(3, 5), F(-4, 5), 0), (F(4, 5), F(3, 5), 0), (0, 0, 1)),
    'r': ((F(3, 5), F(4, 5), 0), (F(-4, 5), F(3, 5), 0), (0, 0, 1))}

# Complex arithmetic is represented by pairs. These unnormalized quantum
# matrices independently define the real rotations used by the verifier.
def plus(z, w):
    return z[0]+w[0], z[1]+w[1]


def times(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def conjugate(z):
    return z[0], -z[1]


def matmul(a, b):
    return tuple(tuple(plus(times(a[i][0], b[0][j]), times(a[i][1], b[1][j]))
                       for j in range(2)) for i in range(2))


def dagger(a):
    return tuple(tuple(conjugate(a[j][i]) for j in range(2)) for i in range(2))


def scaled(a, f):
    return tuple(tuple((f*z[0], f*z[1]) for z in row) for row in a)


def density(v, mass=F(1)):
    x, y, z = v
    return (
        (((mass+z)/2, F(0)), (x/2, -y/2)),
        ((x/2, y/2), ((mass-z)/2, F(0))))


def bloch(a):
    return 2*a[1][0][0], 2*a[1][0][1], a[0][0][0]-a[1][1][0]


def mass(a):
    return a[0][0][0]+a[1][1][0]


UNITS = {
    'H': ((((F(1), F(0)), (F(1), F(0))),
           ((F(1), F(0)), (F(-1), F(0)))), F(2)),
    'S': ((((F(1), F(0)), (F(0), F(0))),
           ((F(0), F(0)), (F(0), F(1)))), F(1)),
    'R': ((((F(2), F(-1)), (F(0), F(0))),
           ((F(0), F(0)), (F(2), F(1)))), F(5)),
    'r': ((((F(2), F(1)), (F(0), F(0))),
           ((F(0), F(0)), (F(2), F(-1)))), F(5))}


def quantum_rotate(a, name):
    u, factor = UNITS[name]
    return scaled(matmul(matmul(u, a), dagger(u)), 1/factor)


def quantum_measure(a, axis, sign):
    projector = density(tuple(sign*x for x in AXES[axis]))
    return matmul(matmul(projector, a), projector)


def quantum_generators():
    out = {}
    for name in UNITS:
        columns = [bloch(quantum_rotate(density(axis), name))
                   for axis in (AXES['X'], AXES['Y'], AXES['Z'])]
        matrix = tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
        require(matrix == DECLARED[name], 'quantum rotation convention')
        out[name] = matrix
    return out


ROTATIONS = quantum_generators()


def word_matrices(depth):
    out = [((), IDENTITY)]
    for n in range(1, depth+1):
        for labels in product(ROTATIONS, repeat=n):
            matrix = IDENTITY
            declared = IDENTITY
            for name in labels:
                matrix = compose(ROTATIONS[name], matrix)
                declared = compose(DECLARED[name], declared)
            require(matrix == declared, 'all-word independent rotation')
            require(compose(tuple(zip(*matrix)), matrix) == IDENTITY,
                    'orthogonal quantum word')
            out.append((labels, matrix))
    return out


def norm_interval(square):
    require(square >= 0, 'nonnegative norm square')
    denominator = 1 << 64
    numerator = isqrt((square.numerator << 128)//square.denominator)
    low = F(numerator, denominator)
    high = low if low*low == square else F(numerator+1, denominator)
    require(low*low <= square <= high*high, 'rational norm enclosure')
    return low, high


class FiniteSphere:
    def __init__(self, m, w=16, b=24):
        self.m, self.w, self.b, self.seeds = m, w, b, 1 << b
        self.points = []
        for fixed, side in product(range(3), (-1, 1)):
            others = [j for j in range(3) if j != fixed]
            for first, second in product(range(1-m, m, 2), repeat=2):
                point = [None]*3
                point[fixed] = side*m
                point[others[0]], point[others[1]] = first, second
                self.points.append(tuple(point))
        require(len(self.points) == 6*m*m == len(set(self.points)), 'entire alphabet')
        lookup = {point: i for i, point in enumerate(self.points)}
        self.opposite = [lookup[negative(point)] for point in self.points]
        self.inward = []
        for point in self.points:
            square = sum(c*c for c in point)
            length = isqrt(square)
            if length*length != square:
                length += 1
            require((length-1)**2 < square <= length**2, 'integer inward radius')
            self.inward.append(tuple(F(c, length) for c in point))
        self.distributions, self.weight_data, self.averages = {}, {}, {}
        for name, direction in RAYS.items():
            if name[-1] == '-':
                continue
            rational_weights = [max(F(0), inner(direction, point))*m**3 /
                                inner(point, point)**2 for point in self.points]
            integers = [int((1 << w)*value) for value in rational_weights]
            total = sum(integers)
            require(total > 0, 'nonempty weighted geometry')
            for value, integer in zip(rational_weights, integers):
                require(0 <= value-F(integer, 1 << w) < F(1, 1 << w),
                        'geometric floor enclosure')
            cumulative, previous = 0, 0
            counts = []
            for integer in integers:
                cumulative += integer
                edge = (self.seeds*cumulative)//total
                counts.append(edge-previous)
                previous = edge
            require(previous == self.seeds and min(counts) >= 0, 'CDF partition')
            tv = sum(abs(F(c, self.seeds)-F(i, total))
                     for c, i in zip(counts, integers))/2
            require(tv <= F(len(counts)-1, self.seeds), 'finite rounding TV')
            self.weight_data[name] = (rational_weights, integers, total, tv)
            self.distributions[name] = counts
            self.distributions[name[:-1]+'-'] = [counts[j] for j in self.opposite]
        for name, counts in self.distributions.items():
            require(sum(counts) == self.seeds, 'source normalization')
            self.averages[name] = tuple(sum(F(c, self.seeds)*v[j]
                                          for c, v in zip(counts, self.inward))
                                       for j in range(3))
        self.cache = {}

    def probability(self, name, rotation, axis):
        coefficients = tuple(sum(AXES[axis][i]*rotation[i][j] for i in range(3))
                             for j in range(3))
        key = name, coefficients
        if key not in self.cache:
            denominator = lcm(*(c.denominator for c in coefficients))
            integers = tuple(int(c*denominator) for c in coefficients)
            count = sum(c for c, point in zip(self.distributions[name], self.points)
                        if inner(integers, point) >= 0)
            self.cache[key] = F(count, self.seeds)
        return self.cache[key]

    def sampled(self, name, seed):
        require(0 <= seed < self.seeds, 'seed in bank block')
        if name[-1] == '-':
            return self.opposite[self.sampled(name[:-1]+'+', seed)]
        cumulative = 0
        for i, count in enumerate(self.distributions[name]):
            cumulative += count
            if seed < cumulative:
                return i
        raise RuntimeError('incomplete sampler')


def certify(m):
    grid = FiniteSphere(m)
    all_words = word_matrices(3)
    maximum_norm, maximum_error, kappa = F(), F(), F()
    positive_cases, read_cases, quantum_controls = 0, 0, 0
    chi_ray, kappa_witness = None, None
    for name, direction in RAYS.items():
        decoded = tuple(F(3, 2)*x for x in grid.averages[name])
        square = inner(decoded, decoded)
        require(square <= 1, 'fixed decoder ray positivity')
        maximum_norm = max(maximum_norm, square)
        difference = tuple(x-y for x, y in zip(decoded, direction))
        error = norm_interval(inner(difference, difference))[1]/2
        if error > maximum_error:
            maximum_error, chi_ray = error, name
        for labels, matrix in all_words:
            actual = apply(matrix, decoded)
            require(inner(actual, actual) == square, 'all ray word norms')
            positive_cases += 1
            quantum_state = density(direction)
            for label in labels:
                quantum_state = quantum_rotate(quantum_state, label)
            require(bloch(quantum_state) == apply(matrix, direction),
                    'all ray words versus direct quantum matrices')
            quantum_controls += 1
            if len(labels) == 3:
                continue
            for axis in AXES:
                p = grid.probability(name, matrix, axis)
                target = mass(quantum_measure(quantum_state, axis, 1))
                deviation = abs(p-target)
                if deviation > kappa:
                    kappa = deviation
                    kappa_witness = {'ray': name, 'word': labels, 'axis': axis,
                                     'source_plus': str(p), 'quantum_plus': str(target)}
                read_cases += 1
    cdf_digest = hashlib.sha256(json.dumps(
        {name: grid.distributions[name] for name in RAYS}, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()
    certificate = {'M': m, 'labels': len(grid.points), 'alpha': '3/2',
                   'maximum_decoded_norm_squared': str(maximum_norm),
                   'chi_upper': str(maximum_error), 'chi_ray': chi_ray,
                   'kappa': str(kappa), 'kappa_witness': kappa_witness,
                   'CQ_bound_upper': str(3*kappa+2*maximum_error),
                   'positive_cases': positive_cases, 'read_cases': read_cases,
                   'quantum_word_controls': quantum_controls,
                   'distinct_read_cases': len(grid.cache),
                   'cdf_count_vectors_sha256': cdf_digest,
                   'nonzero_floor_rounding_rays': sum(any(value != F(i, 1 << grid.w)
                                                         for value, i in zip(data[0], data[1]))
                                                     for data in grid.weight_data.values()),
                   'nonzero_CDF_rounding_rays': sum(data[3] > 0
                                                   for data in grid.weight_data.values())}
    return grid, certificate


def tv(a, b):
    return sum(abs(a.get(k, F())-b.get(k, F())) for k in set(a) | set(b))/2


def source_controls(grid):
    small = FiniteSphere(8, 10, 10)
    for name in ('X+', 'Z+', 'a+'):
        cumulative = []
        total = 0
        for c in small.distributions[name]:
            total += c
            cumulative.append(total)
        histogram = Counter()
        for seed in range(small.seeds):
            sample = small.sampled(name, seed)
            require(sample == bisect_right(cumulative, seed), 'independent binary sampler')
            require(small.sampled(name[:-1]+'-', seed) == small.opposite[sample],
                    'pointwise antipodal sample')
            histogram[sample] += 1
        require([histogram[i] for i in range(len(small.points))] == small.distributions[name],
                'every fair seed counted')
    first_plus = small.probability('Z+', IDENTITY, 'X')
    fresh, reuse = {}, Counter()
    for sign in (1, -1):
        probability = first_plus if sign == 1 else 1-first_plus
        post = 'X+' if sign == 1 else 'X-'
        second_plus = small.probability(post, IDENTITY, 'Z')
        for second in (1, -1):
            fresh[sign, second] = probability*(second_plus if second == 1 else 1-second_plus)
    for seed in range(small.seeds):
        point = small.points[small.sampled('Z+', seed)]
        first = 1 if point[0] >= 0 else -1
        second_point = small.points[small.sampled('X+' if first == 1 else 'X-', seed)]
        second = 1 if second_point[2] >= 0 else -1
        reuse[first, second] += F(1, small.seeds)
    reuse_gap = tv(fresh, reuse)
    require(reuse_gap > 0, 'reused seed is detected')
    adaptive, ignored = {}, {}
    for sign in (1, -1):
        p = first_plus if sign == 1 else 1-first_plus
        post = 'X+' if sign == 1 else 'X-'
        for second in (1, -1):
            axis = 'Z' if sign == 1 else 'a'
            p_adapt = small.probability(post, IDENTITY, axis)
            p_bad = small.probability(post, IDENTITY, 'Z')
            adaptive[sign, second] = p*(p_adapt if second == 1 else 1-p_adapt)
            ignored[sign, second] = p*(p_bad if second == 1 else 1-p_bad)
    adaptive_gap = tv(adaptive, ignored)
    require(adaptive_gap > 0 and 1-first_plus > 0, 'adaptive and bank mutants detected')
    mixtures = {}
    for axis in ('X', 'Z'):
        counts = [F(a+b, 2*grid.seeds) for a, b in
                  zip(grid.distributions[axis+'+'], grid.distributions[axis+'-'])]
        mixtures[axis] = dict(enumerate(counts))
        require(tuple(grid.averages[axis+'+'][j]+grid.averages[axis+'-'][j]
                      for j in range(3)) == (0, 0, 0), 'equal decoded input')
    private_gap = tv(mixtures['X'], mixtures['Z'])
    timing_gap = abs(sum(mixtures['X'][i]-mixtures['Z'][i]
                         for i, point in enumerate(grid.points)
                         if abs(point[0]) > abs(point[2])))
    require(private_gap > 0 and timing_gap > 0, 'access and timing leaks detected')
    negative_atoms = sum(c > 0 and F(9, 4)*inner(v, v) > 1
                         for c, v in zip(grid.distributions['Z+'], grid.inward))
    require(negative_atoms > 0, 'seed disclosure changes positive cone')
    return {'small_seed_exhaustion_cases': 3*small.seeds,
            'reused_seed_TV': str(reuse_gap), 'ignored_adaptive_TV': str(adaptive_gap),
            'insufficient_bank_failure': str(1-first_plus),
            'private_label_TV': str(private_gap), 'private_timing_gap': str(timing_gap),
            'negative_individual_seed_atoms': negative_atoms}


def action(policy, tick, outcomes):
    if policy in AXES:
        return 'read', policy
    if policy == 'rotations':
        return 'rotate', ('H', 'S', 'R')[tick]
    if policy == 'unitaries_then_read':
        return (('rotate', 'S'), ('rotate', 'H'), ('read', 'a'))[tick]
    if policy == 'adaptive':
        if tick == 0:
            return 'read', 'Z'
        if tick == 1:
            return ('read', 'a') if outcomes[0] == 1 else ('rotate', 'r')
        return 'read', 'X' if outcomes[-1] == 1 else 'Z'
    if policy == 'read_rotate_read':
        if tick == 0:
            return 'read', 'a'
        if tick == 1:
            return 'rotate', 'r' if outcomes[-1] == 1 else 'H'
        return 'read', 'X' if outcomes[0] == 1 else 'Z'
    if policy == 'stops':
        if tick == 0:
            return 'read', 'X'
        if outcomes[0] == 1:
            return 'stop', None
        return 'read', 'Z' if tick == 1 else 'a'
    raise RuntimeError('unknown policy')


def adaptive_control(grid, certificate):
    inputs = [[(F(1), name)] for name in RAYS]
    inputs += [[(F(1, 2), 'X+'), (F(1, 2), 'X-')],
               [(F(1, 2), 'Z+'), (F(1, 2), 'Z-')],
               [(F(2, 5), 'p+'), (F(3, 5), 'q+')],
               [(F(1, 3), 'a+'), (F(2, 3), 'Y-')]]
    policies = list(AXES)+['rotations', 'unitaries_then_read', 'adaptive',
                           'read_rotate_read', 'stops']
    counters = Counter()
    maximum_cq, maximum_tv = F(), F()
    bound = F(certificate['CQ_bound_upper'])
    for initial_terms, policy in product(inputs, policies):
        start = tuple(F(3, 2)*sum(weight*grid.averages[name][j]
                                 for weight, name in initial_terms) for j in range(3))
        branches = [(F(1), initial_terms, IDENTITY, density(start), (), (), False)]
        for tick in range(3):
            following = []
            for p, terms, rotation, rho, outcomes, record, stopped in branches:
                op, name = ('stop', None) if stopped else action(policy, tick, outcomes)
                if op == 'rotate':
                    following.append((p, terms, compose(ROTATIONS[name], rotation),
                                      quantum_rotate(rho, name), outcomes,
                                      record+((tick, op, name, 1),), False))
                    counters['nodes'] += 1
                elif op == 'stop':
                    following.append((p, terms, rotation, rho, outcomes,
                                      record+((tick, op, name, 1),), True))
                    counters['nodes'] += 1
                else:
                    plus_probability = sum(weight*grid.probability(ray, rotation, name)
                                           for weight, ray in terms)
                    for sign in (1, -1):
                        prob = plus_probability if sign == 1 else 1-plus_probability
                        target = quantum_measure(rho, name, sign)
                        reset = [(F(1), name+('+' if sign == 1 else '-'))]
                        following.append((p*prob, reset, IDENTITY, target,
                                          outcomes+(sign,), record+((tick, op, name, sign, 1),), False))
                        counters['nodes'] += 1
                        if p*prob == 0 or mass(target) == 0:
                            counters['zero_nodes'] += 1
            branches = following
        require(sum(b[0] for b in branches) == 1, 'source full record normalization')
        require(sum(mass(b[3]) for b in branches) == 1, 'quantum full record normalization')
        cq_upper, record_tv = F(), F()
        for p, terms, rotation, rho, outcomes, record, stopped in branches:
            require(len(record) == 3, 'complete tick metadata')
            mean = tuple(F(3, 2)*sum(weight*grid.averages[name][j]
                                    for weight, name in terms) for j in range(3))
            outgoing = apply(rotation, mean)
            require(inner(outgoing, outgoing) <= 1, 'actual output state positive')
            delta = tuple(p*v-w for v, w in zip(outgoing, bloch(rho)))
            norm_high = norm_interval(inner(delta, delta))[1]
            delta_mass = abs(p-mass(rho))
            cq_upper += max(delta_mass, norm_high)/2
            record_tv += delta_mass/2
        require(cq_upper <= bound, 'direct adaptive CQ control')
        counters['protocol_input_cases'] += 1
        counters['leaves'] += len(branches)
        maximum_cq, maximum_tv = max(maximum_cq, cq_upper), max(maximum_tv, record_tv)
    return {'counts': dict(counters), 'maximum_CQ_upper': str(maximum_cq),
            'maximum_record_TV': str(maximum_tv),
            'role': 'Independent bounded controls; all-policy coverage uses the envelope proof.'}


def verify_inputs(author_root):
    here = Path(__file__).resolve().parent
    pins = json.loads((here/'INPUT-HASHES.json').read_text())
    for name, item in pins['author_files'].items():
        content = (author_root/name).read_bytes()
        require(hashlib.sha256(content).hexdigest() == item['sha256'], 'author SHA256 '+name)
        require(hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
                == item['git_blob'], 'immutable Git blob '+name)
    return pins


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author-root', type=Path,
                        default=Path(__file__).resolve().parents[2]/'a2_efficiency_v6')
    options = parser.parse_args()
    pins = verify_inputs(options.author_root)
    measured = []
    grid = None
    for m in (8, 16):
        grid, certificate = certify(m)
        measured.append(certificate)
    author_result = json.loads((options.author_root/'result.json').read_text())
    for actual, recorded in zip(measured, author_result['attempts']):
        for ours, theirs in [('maximum_decoded_norm_squared', 'maximum_decoded_ray_norm_squared'),
                             ('chi_upper', 'chi_upper'), ('kappa', 'kappa'),
                             ('CQ_bound_upper', 'fixed_decoder_CQ_bound_upper'),
                             ('cdf_count_vectors_sha256', 'cdf_count_vectors_sha256')]:
            require(actual[ours] == recorded[theirs], 'independent envelope agreement '+ours)
    require(F(measured[0]['CQ_bound_upper']) > F(1, 10), 'M8 threshold failure')
    require(F(measured[1]['CQ_bound_upper']) ==
            F(17239332625914280559, 230584300921369395200) < F(1, 10), 'M16 executed certificate')
    resources = {'initial_fair_bits_excluding_mixture': 4*24,
                 'labels': 6*16**2, 'formal_words': sum(4**j for j in range(4)),
                 'word_label_upper': 6*16**2*sum(4**j for j in range(4)),
                 'CDF_table_bits_upper': 12*6*16**2*25,
                 'response_table_bits_upper': 4*6*16**2*sum(4**j for j in range(4)),
                 'retained_old_carrier_register_upper': 3,
                 'scope': 'Specified finite menus, total h=3; tables and workspace remain supplied.'}
    controls = source_controls(grid)
    protocols = adaptive_control(grid, measured[-1])
    result = {'schema': 'oi.a2-efficiency-v6.separate-review.v1',
              'author_commit': pins['author_commit'], 'envelopes': measured,
              'resources': resources, 'controls': controls, 'adaptive_controls': protocols,
              'verdict': 'ACCEPT_WITHIN_FINITE_MENU_HORIZON_SCOPE',
              'limits': ['No native availability or probability-selection derivation.',
                         'Finite controls do not replace the all-policy envelope proof.',
                         'Internal separate-agent review, not formal or external certification.']}
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
