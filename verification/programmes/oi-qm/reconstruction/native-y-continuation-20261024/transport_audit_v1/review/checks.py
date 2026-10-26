"""Independent forward-cone and exact algebra review, no author module imports."""
import argparse
from functools import reduce
from itertools import product
from math import comb, lcm
from pathlib import Path
import hashlib
import json


ZERO = (0, 0, 0)
TR = tuple(product((0, 1), repeat=3))
DIR = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def h(q):
    a, b, d = q
    return b, d, a ^ (b & d)


def hinv(q):
    a, b, d = q
    return d ^ (a & b), a, b


def xx(*qs):
    return tuple(reduce(int.__xor__, (q[i] for q in qs), 0) for i in range(3))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def ball(r, c):
    for a in range(-r, r+1):
        for b in range(-r+abs(a), r-abs(a)+1):
            for d in range(-r+abs(a)+abs(b), r-abs(a)-abs(b)+1):
                yield add(c, (a, b, d))


def forward(current, previous, requests):
    """Forward evolution on a union of complete backward cones."""
    horizon = max(t for t, p in requests)
    domains = []
    for step in range(horizon+1):
        region = set()
        for t, p in requests:
            if t >= step:
                region.update(ball(t-step, p))
        domains.append(region)
    old = {p: previous(p) for p in domains[0]}
    now = {p: current(p) for p in domains[0]}
    answer = {(0, p): now[p] for t, p in requests if t == 0}
    for t in range(1, horizon+1):
        future = {p: xx(old[p], h(xx(*(now[add(p, e)] for e in DIR))))
                  for p in domains[t]}
        answer.update({(t, p): future[p] for rt, p in requests if rt == t})
        old, now = now, future
    return answer


def background(p, salt=0):
    x, y, z = p
    return TR[((5*x*x+3*y*z+11*z+salt) ^ (x*y+7*y*y+salt*z)) & 7]


def partitions(n, low=1):
    if not n:
        yield ()
    for k in range(low, n+1):
        for tail in partitions(n-k, k):
            yield (k,)+tail


def radius_one_census():
    # Independent closed formula: four outer symbols and one center.
    lookup = [TR.index(h(q)) for q in TR]
    table = []
    for raw in range(8**5):
        old_outer = [(raw >> (3*i)) & 7 for i in range(4)]
        new_outer = [lookup[v] for v in old_outer]
        outer_xor = reduce(int.__xor__, new_outer, 0)
        center = lookup[((raw >> 12) & 7) ^ outer_xor]
        output = sum(q << (3*i) for i, q in enumerate(new_outer)) | (center << 12)
        # Invert the closed formula with an independent table search.
        recovered_outer = [lookup.index(v) for v in new_outer]
        recovered_center = lookup.index(center) ^ outer_xor
        check(recovered_outer == old_outer and recovered_center == (raw >> 12),
              'radius-one closed inverse')
        table.append(output)
    check(len(set(table)) == 8**5, 'radius-one bijection')
    seen = set()
    sizes = []
    for start in range(len(table)):
        if start in seen:
            continue
        p, count = start, 0
        while p not in seen:
            seen.add(p)
            p = table[p]
            count += 1
        check(p == start, 'radius-one cycle')
        sizes.append(count)
    check(lcm(*sizes) == 720, 'exact radius-one order')
    return {'states': len(table), 'order': lcm(*sizes), 'cycles': len(sizes)}


def extrusion():
    rows = 0
    for radius, delay, salt in product(range(4), range(4), (1, 7)):
        horizon = radius+delay
        end = (0, delay, 0)
        shell = {p: background(p, salt) for p in ball(radius, ZERO)
                 if p[1] <= 0 and sum(abs(x) for x in p) == radius}
        pts = sorted(((x, z) for x in range(-radius, radius+1)
                      for z in range(-radius, radius+1)
                      if abs(x)+abs(z) <= radius),
                     key=lambda q: (-abs(q[0])-abs(q[1]), q))
        requests = [(radius-abs(x)-abs(z)+d, (x, d, z))
                    for d in range(delay+1) for x, z in pts]
        requests += [(t, end) for t in range(horizon)]
        raw = forward(lambda p: shell.get(p, ZERO) if dist(p, end) <= horizon
                      else background(p, 13),
                      lambda p: ZERO if dist(p, end) <= horizon-1
                      else background(p, 17), requests)
        front = {(x, z): raw[radius-abs(x)-abs(z), (x, 0, z)] for x, z in pts}
        for d in range(delay+1):
            for x, z in pts:
                check(raw[radius-abs(x)-abs(z)+d, (x, d, z)] == front[x, z],
                      'full native/staggered-front agreement')
                # Geometric dependency exclusion and complete cone embedding.
                t = radius-abs(x)-abs(z)+d
                check(dist((x, d, z), end)+t == horizon, 'complete causal cone inclusion')
                for source in shell:
                    check(dist(source, (x, d, z)) >= t, 'rear-shell first-front bound')
                rows += 1
            new = {}
            for p in pts:
                a, b = p
                outer = [new[q] for q in ((a+1, b), (a-1, b), (a, b+1), (a, b-1))
                         if q in new and abs(q[0])+abs(q[1]) == abs(a)+abs(b)+1]
                new[p] = h(xx(front[p], *outer))
                check(xx(hinv(new[p]), *outer) == front[p], 'triangular inverse per site')
            front = new
        check(all(raw[t, end] == ZERO for t in range(horizon)), 'blank receiver prefix')
    return rows


def dirty_axis():
    count = 0
    for direction, n, salt in product(DIR, range(1, 5), (0, 3)):
        source = tuple(-n*x for x in direction)
        outputs = []
        for value in TR:
            raw = forward(lambda p: value if p == source else background(p, salt),
                          lambda p: background(p, salt+11), [(n, ZERO)])
            outputs.append(raw[n, ZERO])
            count += 1
        check(len(set(outputs)) == 8, 'arbitrary-background own response')
    return count


def chronological_controls():
    scenarios = {
        'acyclic': (((1, 0, 0), (0, 1, 0)), ((1, 3, 0), (0, 4, 0))),
        'cycle': (((0, 0, 0), (1, 1, 0)), ((0, 3, 0), (-2, 1, 0)))
    }
    result = {}
    for name, (ports, sources) in scenarios.items():
        table = {}
        for a, b in product(TR, repeat=2):
            init = {sources[0]: a, sources[1]: b}
            raw = forward(lambda p: init.get(p, ZERO) if name == 'cycle'
                          else init.get(p, background(p, 5)),
                          lambda p: ZERO if name == 'cycle' else background(p, 9),
                          [(t, p) for t in range(4) for p in ports])
            pair = tuple(raw[3, p] for p in ports)
            table[a, b] = pair
            if name == 'cycle':
                expected = h(h(xx(h(a), h(b))))
                check(pair == (expected, expected), 'native cyclic collapse formula')
                check(all(raw[t, p] == ZERO for t in range(3) for p in ports),
                      'cyclic sources invisible before deadline')
        size = len(set(table.values()))
        if name == 'acyclic':
            check(size == 64, 'acyclic full product law')
        else:
            check(size == 8, 'cyclic joint law loses six bits to three')
            for b in TR:
                check(len({table[a, b][0] for a in TR}) == 8, 'cyclic own0 still bijective')
            for a in TR:
                check(len({table[a, b][1] for b in TR}) == 8, 'cyclic own1 still bijective')
        result[name] = size
    for q in TR:
        raw = forward(lambda p: q if p == (1, 1, 0) else ZERO,
                      lambda p: ZERO, [(2, ZERO)])
        check(raw[2, ZERO] == ZERO, 'multiple-shortest-path countercontrol')
    return result


def wings():
    words = steps = omissions = matrix_entries = 0
    for ell, salt in product(range(2, 7), range(3)):
        controls = [TR[(3*t*t+5*t+salt+1) & 7] for t in range(ell-1)] + [ZERO]
        coefficients = {}
        for wing in range(3):
            desired = [q[(wing-t) % 3] for t, q in enumerate(controls)]
            source = []
            for q in range(ell):
                source.append(desired[q] ^ reduce(int.__xor__,
                              (source[e] for e in range(q) if comb(q, e) & 1), 0))
                # Independent triangular solve versus the subset transform.
                expected = reduce(int.__xor__,
                                  (desired[e] for e in range(q+1) if e & ~q == 0), 0)
                check(source[q] == expected, 'Pascal triangular solve/subset inverse')
                matrix_entries += 1
            for q, bit in enumerate(source):
                p = ((ell-1-q, q+1, 0), (ell-1-q, -q-1, 0),
                     (ell-1-q, 0, q+1))[wing]
                coefficients[p] = tuple(bit if j == wing else 0 for j in range(3))
        raw = forward(lambda p: coefficients.get(p, ZERO), lambda p: ZERO,
                      [(t+1, (ell-1-t, 0, 0)) for t in range(ell)]+
                      [(t, ZERO) for t in range(ell)])
        state = ZERO
        for t, control in enumerate(controls):
            state = h(xx(state, control))
            check(raw[t+1, (ell-1-t, 0, 0)] == state, 'full native affine wing word')
            steps += 1
        check(all(raw[t, ZERO] == ZERO for t in range(ell)), 'wing blank prefix')
        truncated = {p: q for p, q in coefficients.items() if p[0] != 0}
        reduced = forward(lambda p: truncated.get(p, ZERO), lambda p: ZERO, [(ell, ZERO)])
        omissions += reduced[ell, ZERO] != state
        words += 1
    check(omissions > 0, 'terminal source row matters')
    return {'words': words, 'native_steps': steps, 'Pascal_entries': matrix_entries,
            'terminal_omission_failures': omissions}


def application_geometry(source_root):
    T = 185
    P = 12*840**185
    S = T+P
    rows = json.loads((source_root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    check(len(rows) == 1479, 'retained compiled source inventory')
    receivers = [((0, T, 0), {'input'}), ((T, 0, 0), {'input', 'Y'}),
                 ((-T, 0, 0), {'input', 'R'}), ((4*T, 0, 0), {'Z'})]
    compared = 0
    for receiver, owners in receivers:
        translated = add(receiver, (0, P, 0))
        for row in rows:
            p = tuple(row['position'])
            sigma = abs(p[0]-receiver[0])+abs(p[2]-receiver[2])-(p[1]-receiver[1])
            if row['owner'] in owners:
                check(p[1] <= receiver[1] and sigma == T,
                      'intended source on radius185 rear hemisphere')
                check(dist(p, translated) == S, 'actual shifted current boundary')
            else:
                check(sigma > T and dist(p, translated) > S,
                      'foreign source outside every forward enlarged cone')
            compared += 1
        check(dist(ZERO, translated) > S-1, 'old unknown previous input excluded')
        # All-index symbolic frontier inequalities: increasing s adds s to sigma.
        for f0 in ((0, 0, 0), (0, 0, -9*T)):
            p = add(f0, (0, -1, 0)) if f0 == ZERO else add(f0, (0, 0, -1))
            sigma = abs(p[0]-receiver[0])+abs(p[2]-receiver[2])-(p[1]-receiver[1])
            check(sigma > T, 'old public frontier outside relay cone')
    return {'source_receiver_comparisons': compared, 'receiver_count': len(receivers),
            'compiled_truth_semantics': 'separate retained application audit'}


def main():
    ap = argparse.ArgumentParser()
    default = Path(__file__).resolve().parent.parent
    if not (default/'PLAN.md').exists() or not (default/'PROVENANCE.json').exists():
        default = default/'transport_audit_v1'
    ap.add_argument('--author-root', type=Path, default=default)
    candidate = default.parent
    if not (candidate/'parallel_v3').exists():
        candidate = candidate/'checkpoint_v10'
    ap.add_argument('--source-root', type=Path, default=candidate)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    pins = json.loads((here/'INPUT-HASHES.json').read_text())
    for path, digest in pins['author_files'].items():
        check(hashlib.sha256((args.author_root/path).read_bytes()).hexdigest() == digest,
              'exact author bytes '+path)
    for path, digest in pins['inherited_files'].items():
        check(hashlib.sha256((args.source_root/path).read_bytes()).hexdigest() == digest,
              'inherited geometry bytes '+path)
    hp = [h(q) for q in TR]
    check(len(set(hp)) == 8 and all(hinv(h(q)) == q for q in TR), 'H permutation/inverse')
    for q in TR:
        now = q
        for _ in range(12):
            now = h(now)
        check(now == q, 'H exponent12')
    parts = list(partitions(8))
    check(len(parts) == 22 and all(840 % lcm(*p) == 0 for p in parts),
          'all eight-symbol permutation cycle types')
    P = 12*840**185
    check(all(P % (12*840**r) == 0 for r in (0, 18, 144, 176, 185)), 'exact exponent divisibility')
    check(P % (12*840**186) != 0, 'uncovered larger radius')
    result = {'schema': 'oi.native-transport-proof-review.v1',
              'author_sha': pins['author_sha'], 'author_files_checked': len(pins['author_files']),
              'eight_symbol_cycle_types': len(parts),
              'native_extrusion_front_values': extrusion(),
              'native_dirty_axis_value_comparisons': dirty_axis(),
              'radius_one': radius_one_census(),
              'chronological': chronological_controls(), 'wing': wings(),
              'radius185_application_geometry': application_geometry(args.source_root),
              'verdict': 'ACCEPT_SCOPED_PROOFS',
              'limitations': ['internal separate-author review', 'not external certification',
                              'no dirty-phase adapter', 'no quantum calibration derivation',
                              'radius185 source application remains separate dependency']}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
