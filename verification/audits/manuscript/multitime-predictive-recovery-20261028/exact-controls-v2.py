#!/usr/bin/env python3
"""Exact, deterministic controls for multitime-recovery-proof-v2.md.

Scratch proof development only. No network, repository writes, heavy suites,
frozen-protocol execution, scientific status changes, or floating-point tests.
Run: python exact-controls-v2.py
All finite tests supplement, and do not replace, the proofs in the companion.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
import hashlib
import json
from pathlib import Path


def need(ok, name):
    if not ok:
        raise RuntimeError(name)


def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    return mat([[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)])


def sub(a, b):
    return mat([[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)])


def mul(a, b):
    return mat([[sum(a[i][k] * b[k][j] for k in range(len(b)))
                 for j in range(len(b[0]))] for i in range(len(a))])


def tr(a):
    return tuple(zip(*a))


def rank(a):
    if not a:
        return 0
    rows = [list(r) for r in a]
    pivot = 0
    for col in range(len(rows[0])):
        hit = next((i for i in range(pivot, len(rows)) if rows[i][col]), None)
        if hit is None:
            continue
        rows[pivot], rows[hit] = rows[hit], rows[pivot]
        z = rows[pivot][col]
        rows[pivot] = [v / z for v in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                z = rows[i][col]
                rows[i] = [x - z * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def inverse(a):
    n = len(a)
    rows = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for col in range(n):
        hit = next((i for i in range(col, n) if rows[i][col]), None)
        need(hit is not None, "inverse requested for singular matrix")
        rows[col], rows[hit] = rows[hit], rows[col]
        z = rows[col][col]
        rows[col] = [v / z for v in rows[col]]
        for i in range(n):
            if i != col:
                z = rows[i][col]
                rows[i] = [x - z * y for x, y in zip(rows[i], rows[col])]
    answer = mat([r[n:] for r in rows])
    need(mul(a, answer) == eye(n) == mul(answer, a), "inverse two-sided check")
    return answer


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def words(q, bound):
    for n in range(bound + 1):
        yield from product(range(q), repeat=n)


def word_operator(operators, word):
    answer = eye(len(operators[0]))
    for letter in word:
        answer = mul(operators[letter], answer)
    return answer


def probability(operators, initial, word):
    row = mat([[1] * len(initial)])
    return mul(row, mul(word_operator(operators, word), initial))[0][0]


def path_probability(operators, initial, word):
    # Independent summation over hidden trajectories, with no matrix products.
    n = len(initial)
    answer = F(0)
    for path in product(range(n), repeat=len(word) + 1):
        mass = initial[path[0]][0]
        for t, letter in enumerate(word):
            mass *= operators[letter][path[t + 1]][path[t]]
        answer += mass
    return answer


def minimality(operators, initial):
    n = len(initial)
    ws = list(words(len(operators), n - 1))
    reach = tr([tuple(r[0] for r in mul(word_operator(operators, w), initial)) for w in ws])
    observe = [mul(mat([[1] * n]), word_operator(operators, w))[0] for w in ws]
    return rank(reach), rank(observe)


def stochastic(operators, initial, strict=False):
    n = len(initial)
    summed = mat([[sum(a[i][j] for a in operators) for j in range(n)] for i in range(n)])
    need(all(sum(summed[i][j] for i in range(n)) == 1 for j in range(n)), "normalization")
    need(sum(row[0] for row in initial) == 1, "initial normalization")
    need(all(x >= 0 for row in initial for x in row), "initial positivity")
    need(all(x > 0 if strict else x >= 0 for a in operators for row in a for x in row),
         "operator positivity")


def basis_indices(vectors):
    indices, prior = [], 0
    for i in range(len(vectors)):
        current = rank([vectors[j] for j in indices + [i]])
        if current > prior:
            indices.append(i)
            prior = current
    return indices


def hankel_reconstruct(operators, initial):
    d = len(initial)
    candidates = list(words(len(operators), d - 1))
    reach_vectors = [tuple(row[0] for row in mul(word_operator(operators, w), initial))
                     for w in candidates]
    obs_vectors = [mul(mat([[1] * d]), word_operator(operators, u))[0] for u in candidates]
    prefixes = [candidates[i] for i in basis_indices(reach_vectors)]
    suffixes = [candidates[i] for i in basis_indices(obs_vectors)]
    need(len(prefixes) == d == len(suffixes), "Hankel bases exist")
    h = mat([[probability(operators, initial, w + u) for w in prefixes] for u in suffixes])
    hi = inverse(h)
    recovered = []
    for c in range(len(operators)):
        hc = mat([[probability(operators, initial, w + (c,) + u) for w in prefixes]
                  for u in suffixes])
        recovered.append(mul(hi, hc))
    initial_hat = mul(hi, mat([[probability(operators, initial, u)] for u in suffixes]))
    evaluation_hat = mat([[probability(operators, initial, w) for w in prefixes]])
    r = tr([tuple(row[0] for row in mul(word_operator(operators, w), initial))
            for w in prefixes])
    need(all(a == mul(inverse(r), mul(o, r)) for a, o in zip(recovered, operators)),
         "Hankel reconstruction orientation")
    for w in words(len(operators), 6):
        actual = mul(evaluation_hat, mul(word_operator(recovered, w), initial_hat))[0][0]
        need(actual == probability(operators, initial, w), "Hankel reconstruction word equality")
    longest = max(len(w) + 1 + len(u) for w in prefixes for u in suffixes)
    need(longest <= 2 * d - 1, "Hankel access bound")
    return {"prefixes": prefixes, "suffixes": suffixes,
            "maximum_word_length_used": longest, "hankel": h}


def positive_similarity_control():
    t = mat([[F(3, 5), F(2, 5)], [F(2, 5), F(3, 5)]])
    a0 = mat([[F(1, 4), F(1, 10)], [F(1, 10), F(1, 5)]])
    aa = [a0, sub(t, a0)]
    initial = mat([[F(2, 3)], [F(1, 3)]])
    s = mat([[1, F(1, 10)], [0, F(9, 10)]])
    si = inverse(s)
    bb = [mul(s, mul(a, si)) for a in aa]
    initial_b = mul(s, initial)
    for ops, init in [(aa, initial), (bb, initial_b)]:
        stochastic(ops, init, strict=True)
        need(minimality(ops, init) == (2, 2), "positive example minimality")
        for w in words(2, 6):
            need(probability(ops, init, w) == path_probability(ops, init, w),
                 "independent hidden-path check")
        for k in range(7):
            need(sum(probability(ops, init, w) for w in product(range(2), repeat=k)) == 1,
                 "word-law normalization")
    for w in words(2, 6):
        need(probability(aa, initial, w) == probability(bb, initial_b, w), "similar word laws")
    r = tr([tuple(row[0] for row in initial),
            tuple(row[0] for row in mul(a0, initial))])
    rp = tr([tuple(row[0] for row in initial_b),
             tuple(row[0] for row in mul(bb[0], initial_b))])
    recovered_s = mul(rp, inverse(r))
    need(recovered_s == s, "unique similarity recovered from reachable basis")
    need(mul(tr(s), s) != eye(2), "similarity is not orthogonal/unitary")
    need(any(x < 0 for row in si for x in row), "similarity inverse is not positive")
    need(any(sum(x != 0 for x in row) > 1 for row in s), "similarity is not monomial")
    need(mul(mat([[1, 1]]), s) == mat([[1, 1]]), "similarity preserves normalization")
    need(all(s != p for p in [eye(2), mat([[0, 1], [1, 0]])]), "no hidden-state permutation")
    return {"S": s, "inverse": si, "initial_A": initial, "initial_B": initial_b,
            "operators_A": aa, "operators_B": bb,
            "ranks": [2, 2], "words_and_paths_checked_through": 6,
            "reconstructed_similarity": recovered_s,
            "hankel": hankel_reconstruct(aa, initial)}


def nonminimal_controls():
    row = mat([[1, 1]])
    init_r = mat([[1], [0]])
    ta = mat([[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]])
    tb = mat([[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]])
    scale = lambda a: mat([[x / 2 for x in rr] for rr in a])
    no_obs = [[scale(ta), scale(ta)], [scale(tb), scale(tb)]]
    for ops in no_obs:
        stochastic(ops, init_r, strict=True)
        need(minimality(ops, init_r) == (2, 1), "lack-of-observability rank")
        need(all(mul(row, a) == mat([[F(1, 2), F(1, 2)]]) for a in ops),
             "all-word fair-law witness without observability")
    need(trace(no_obs[0][0]) != trace(no_obs[1][0]), "nonobservables are not similar")
    init_o = mat([[F(1, 2)], [F(1, 2)]])
    total = mat([[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]])
    a0 = mat([[F(3, 10), F(1, 5)], [F(2, 5), F(1, 10)]])
    b0 = mat([[F(7, 20), F(3, 20)], [F(1, 4), F(1, 4)]])
    no_reach = [[a0, sub(total, a0)], [b0, sub(total, b0)]]
    for ops in no_reach:
        stochastic(ops, init_o, strict=True)
        need(minimality(ops, init_o) == (1, 2), "lack-of-reachability rank")
        need(all(mul(a, init_o) == mat([[F(1, 4)], [F(1, 4)]]) for a in ops),
             "all-word fair-law witness without reachability")
    need(trace(a0) != trace(b0), "unreachables are not similar")
    for family, init in [(no_obs, init_r), (no_reach, init_o)]:
        for ops in family:
            for w in words(2, 6):
                need(probability(ops, init, w) == F(1, 2) ** len(w), "finite fair-law check")
    return {"without_observability_ranks": [2, 1],
            "without_observability_traces": [trace(x[0]) for x in no_obs],
            "without_reachability_ranks": [1, 2],
            "without_reachability_traces": [trace(x[0]) for x in no_reach]}


def sharp_length_control():
    def mixture(p, weights):
        ops = [mat([[p[0], 0], [0, p[1]]]),
               mat([[1 - p[0], 0], [0, 1 - p[1]]])]
        return ops, mat([[weights[0]], [weights[1]]])
    aa, a = mixture((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)))
    bb, b = mixture((F(1, 5), F(17, 24)), (F(25, 61), F(36, 61)))
    for ops, init in [(aa, a), (bb, b)]:
        stochastic(ops, init)
        need(minimality(ops, init) == (2, 2), "sharpness example minimality")
    for w in words(2, 2):
        need(probability(aa, a, w) == probability(bb, b, w), "match through length 2")
    pa, pb = probability(aa, a, (0, 0, 0)), probability(bb, b, (0, 0, 0))
    need(pa != pb and pa - pb == F(11, 1920), "d=2 distinguishing length 3")
    return {"minimal_dimension_each": 2, "matching_lengths": [0, 1, 2],
            "distinguishing_word": [0, 0, 0], "probabilities": [pa, pb],
            "difference": pa - pb}


def trajectory(p, readout, state, length):
    answer = []
    for _ in range(length):
        answer.append(readout[state])
        state = p[state]
    return tuple(answer)


def passive_laws(p, readout, prior, bound):
    laws = []
    for length in range(bound + 1):
        law = defaultdict(F)
        for state, mass in enumerate(prior):
            if mass:
                law[trajectory(p, readout, state, length)] += mass
        laws.append(dict(law))
    return laws


def reconstruct_native(laws, bound):
    if bound == 1:
        need(len(laws[1]) == 1, "one-state label")
        w = next(iter(laws[1]))
        return {w: w}, {w: laws[1][w]}, {w: w[0]}
    length = bound - 1
    states = set(laws[length])
    step, prior, readout = {}, {}, {}
    for w in states:
        extensions = [u for u in laws[length + 1] if u[:-1] == w]
        need(len(extensions) == 1, "deterministic block extension")
        target = extensions[0][1:]
        need(target in states, "block successor exists")
        step[w], prior[w], readout[w] = target, laws[length][w], w[0]
    need(set(step.values()) == states, "reconstructed quotient is a permutation")
    return step, prior, readout


def native_quotient_ray_control(step, mass, visible, length):
    # Work on the quotient, with one COMMON separating length for every word.
    # This is an algebraic retained-word construction, not a hidden-control API.
    states = sorted(step)
    n = len(states)
    position = {w: i for i, w in enumerate(states)}
    p = mat([[int(position[step[w]] == i) for w in states] for i in range(n)])
    operators = []
    for c in range(2):
        dx = mat([[int(i == j and visible[states[j]] == c)
                   for j in range(n)] for i in range(n)])
        operators.append(mul(p, dx))
    initial = mat([[mass[w]] for w in states])
    ones = mat([[1] * n])
    reached = set()
    for w in states:
        need(len(w) == length, "common separating word length")
        op = word_operator(operators, w)
        start = position[w]
        target = w
        for _ in range(length):
            target = step[target]
        end = position[target]
        effect = mat([[int(i == start) for i in range(n)]])
        ray = mat([[mass[w] * int(i == end)] for i in range(n)])
        need(mul(ones, op) == effect, "native singleton indicator effect")
        need(mul(op, initial) == ray, "native singleton retained-word ray")
        reached.add(end)
    need(reached == set(range(n)), "common-length rays cover all quotient coordinates")
    need(minimality(operators, initial) == (n, n), "native quotient linear minimality")
    # H[u,w] is the probability of chronological concatenation w then u.
    h = mat([[probability(operators, initial, w + u) for w in states]
             for u in states])
    need(rank(h) == n, "native exact Hankel-rank equals quotient-state count")


def quotient_control(p, readout, prior, bound):
    n = len(p)
    # Independent finite equivalence: follow each pair for n! steps. The
    # permutation order divides n!, so this checks full future equivalence.
    common_order = 1
    for k in range(2, n + 1):
        common_order *= k
    full_tails = [trajectory(p, readout, i, common_order) for i in range(n)]
    short_tails = [trajectory(p, readout, i, max(1, n - 1)) for i in range(n)]
    for i in range(n):
        for j in range(n):
            need((full_tails[i] == full_tails[j]) == (short_tails[i] == short_tails[j]),
                 "N-1 state-separation bound, including constant label")
            if full_tails[i] == full_tails[j]:
                need(full_tails[p[i]] == full_tails[p[j]], "quotient forward invariance")
                pi, pj = p.index(i), p.index(j)
                need(full_tails[pi] == full_tails[pj], "quotient backward invariance")
    laws = passive_laws(p, readout, prior, max(bound, 7))
    step, mass, visible = reconstruct_native(laws, bound)
    length = 1 if bound == 1 else bound - 1
    label = [trajectory(p, readout, i, length) for i in range(n)]
    native_quotient_ray_control(step, mass, visible, length)
    need(len(set(label)) == len(set(full_tails)), "blocks label exactly quotient states")
    for i in range(n):
        need(step[label[i]] == label[p[i]], "reconstruction conjugates quotient dynamics")
        need(visible[label[i]] == readout[i], "reconstruction preserves visible labels")
    for w in mass:
        need(mass[w] == sum(prior[i] for i in range(n) if label[i] == w), "pushed prior")
    for k in range(8):
        predicted = defaultdict(F)
        for w, weight in mass.items():
            state, out = w, []
            for _ in range(k):
                out.append(visible[state])
                state = step[state]
            predicted[tuple(out)] += weight
        need(dict(predicted) == laws[k], "predicted native word law")
    return len(mass)


def native_grid_control():
    n, count, constant, nonstationary = 4, 0, 0, 0
    hist = defaultdict(int)
    priors = [tuple(F(1, n) for _ in range(n)), tuple(F(i + 1, 10) for i in range(n))]
    for p in permutations(range(n)):
        for readout in product(range(2), repeat=n):
            for prior in priors:
                q = quotient_control(p, readout, prior, bound=n)
                hist[q] += 1
                constant += int(len(set(readout)) == 1)
                nonstationary += int(any(prior[p.index(j)] != prior[j] for j in range(n)))
                count += 1
    need(count == 768 and constant == 96 and nonstationary > 0, "grid coverage")
    for label in [0, 1]:
        need(quotient_control((0,), (label,), (F(1),), 1) == 1, "one-state edge case")
    return {"instances": count, "permutations": 24, "binary_readouts": 16,
            "full_support_priors": 2, "nonstationary_prior_instances": nonstationary,
            "constant_readout_instances": constant,
            "quotient_size_histogram": dict(hist), "B": 4,
            "word_lengths_for_reconstruction": [3, 4],
            "independent_prediction_checked_through": 7,
            "N_equals_1_instances": 2,
            "common_length_cone_and_Hankel_checks": count + 2}


def de_bruijn(k):
    a = [0] * (2 * k)
    result = []
    def visit(t, period):
        if t > k:
            if k % period == 0:
                result.extend(a[1:period + 1])
        else:
            a[t] = a[t - period]
            visit(t + 1, period)
            for j in range(a[t - period] + 1, 2):
                a[t] = j
                visit(t + 1, t)
    visit(1, 1)
    need(len(result) == 2 ** k, "de Bruijn cycle length")
    return tuple(result)


def missing_bound_control():
    records = []
    for k in [2, 3, 4]:
        small, large = de_bruijn(k), de_bruijn(k + 1)
        laws = []
        for readout in [small, large]:
            n = len(readout)
            p = tuple((i + 1) % n for i in range(n))
            prior = tuple(F(1, n) for _ in range(n))
            laws.append(passive_laws(p, readout, prior, k + 1))
            need(len(set(trajectory(p, readout, i, n - 1) for i in range(n))) == n,
                 "de Bruijn model future-observable")
        need(laws[0][:k + 1] == laws[1][:k + 1], "missing-bound finite agreement")
        need(laws[0][k + 1] != laws[1][k + 1], "missing-bound later divergence")
        for length in range(k + 1):
            need(set(laws[0][length].values()) == {F(1, 2 ** length)}, "uniform cylinders")
        records.append({"matching_max_length": k, "state_counts": [len(small), len(large)],
                        "first_distinguishing_length": k + 1})
    return {"full_support_and_stationary": True, "future_observable": True,
            "examples": records}


def cycle_lengths(p):
    seen, lengths = set(), []
    for state in range(len(p)):
        if state in seen:
            continue
        q, length = state, 0
        while q not in seen:
            seen.add(q)
            length += 1
            q = p[q]
        lengths.append(length)
    return sorted(lengths)


def hidden_fiber_control():
    states = [(v, h) for v in range(2) for h in range(3)]
    pa = tuple(states.index((1 - v, h)) for v, h in states)
    pb = tuple(states.index((1 - v, (h + 1) % 3)) for v, h in states)
    readout = tuple(v for v, h in states)
    prior = tuple(F(1, 6) for _ in states)
    need(passive_laws(pa, readout, prior, 12) == passive_laws(pb, readout, prior, 12),
         "hidden fibers agree on finite passive words")
    # Algebraic all-time witness: in both models visible v advances by v -> 1-v,
    # independently of h. Thus every word law is the same alternating mixture.
    need(all(readout[pa[i]] == 1 - readout[i] == readout[pb[i]] for i in range(6)),
         "all-time visible quotient witness")
    need(cycle_lengths(pa) == [2, 2, 2] and cycle_lengths(pb) == [6], "not conjugate as full permutations")
    return {"full_dynamics_cycle_types": [cycle_lengths(pa), cycle_lengths(pb)],
            "common_visible_quotient_size": 2,
            "scope": "fiber freedom only; decoupled ancilla moves may already identify these models"}


def absent_full_support_control():
    # A third state has no prior mass and sits forever at readout 1. Its prior-
    # supported two-state process is identical to the observable two-cycle.
    p = (1, 0, 2)
    readout = (0, 1, 1)
    prior = (F(1, 2), F(1, 2), F(0))
    a = passive_laws(p, readout, prior, 8)
    b = passive_laws((1, 0), (0, 1), (F(1, 2), F(1, 2)), 8)
    need(a == b, "invisible zero-mass native state")
    need(len(set(trajectory(p, readout, i, 2) for i in range(3))) == 3,
         "zero-mass model is future-observable on all states")
    return {"state_counts": [3, 2], "same_supported_process": True,
            "missing_hypothesis": "global full support"}


def main():
    controls = {
        "positive_nonphysical_similarity": positive_similarity_control(),
        "missing_minimality": nonminimal_controls(),
        "dimension_two_length_bound": sharp_length_control(),
        "native_full_support_grid": native_grid_control(),
        "native_missing_known_bound": missing_bound_control(),
        "native_hidden_fiber_freedom": hidden_fiber_control(),
        "native_missing_full_support": absent_full_support_control(),
    }
    result = {"status": "PASS", "arithmetic": "fractions.Fraction only",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "control_groups": controls,
              "scope": "bounded exact controls; universal claims rest on companion proofs"}
    print(json.dumps(result, indent=2, default=str, sort_keys=True))


if __name__ == "__main__":
    main()
