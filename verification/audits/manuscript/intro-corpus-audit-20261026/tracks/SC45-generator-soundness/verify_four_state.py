#!/usr/bin/env python3
"""SC-45 exact coherent-channel and population controls (draft, no Lean claim).

Do not use Python assert for evidence: all checks and exit statuses remain active
under python3 -O. The results are finite rational arithmetic, not a proof of
the full all-partitions gauge classification.
"""
from fractions import Fraction as F
from itertools import permutations, product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def carrier(v, h):
    return tuple(product(range(v), range(h)))


def perm_from_order(states, order):
    return dict(zip(states, order))


def inverse(p, states):
    require(set(p) == set(states) and set(p.values()) == set(states),
            "permutation invalid")
    return {value: key for key, value in p.items()}


def conj(phi, p, states):
    inv = inverse(p, states)
    return {s: p[phi[inv[s]]] for s in states}


def power(phi, states, t):
    result = {s: s for s in states}
    for _ in range(t):
        result = {s: phi[result[s]] for s in states}
    return result


def coherent_channel(phi, v, h, t):
    """Phi_t(|a><b|)_(c,d), uniform hidden seed, exact rational."""
    states = carrier(v, h)
    step = power(phi, states, t)
    data = {}
    for a, b, c, d in product(range(v), repeat=4):
        matched = 0
        for k in range(h):
            left, right = step[(a, k)], step[(b, k)]
            if left[0] == c and right[0] == d and left[1] == right[1]:
                matched += 1
        data[(a, b, c, d)] = F(matched, h)
    return data


def populations(ch, v):
    return tuple(tuple(ch[(a, a, c, c)] for c in range(v))
                 for a in range(v))


def global_hidden(v, h, sigma):
    return {(a, k): (a, sigma[k]) for a, k in carrier(v, h)}


def fibre_hidden(v, h, sigma_by_v):
    return {(a, k): (a, sigma_by_v[a][k]) for a, k in carrier(v, h)}


def extended_channel(phi, v, h, psi, rho, t):
    """Explicit tensor dilation and trace, including off-diagonal ancilla rho."""
    n = len(psi)
    states = carrier(v, h)
    step = power(phi, states, t)
    dstep = {i: i for i in range(n)}
    for _ in range(t):
        dstep = {i: psi[dstep[i]] for i in range(n)}
    out = {}
    for a, b, c, d in product(range(v), repeat=4):
        x = F(0)
        for k, left_d, right_d in product(range(h), range(n), range(n)):
            left, right = step[(a, k)], step[(b, k)]
            if (left[0] == c and right[0] == d and
                left[1] == right[1] and dstep[left_d] == dstep[right_d]):
                x += rho[left_d][right_d] / h
        out[(a, b, c, d)] = x
    return out


def expect_failure(action, tag):
    try:
        action()
    except ValueError:
        return tag
    raise RuntimeError("MUTANT SURVIVED: " + tag)


def run():
    m = carrier(2, 2)
    phi = {s: (s[1], s[0]) for s in m}
    bad = {s: s for s in m}
    bad[(0, 0)], bad[(1, 0)] = bad[(1, 0)], bad[(0, 0)]
    changed = conj(phi, bad, m)
    first = coherent_channel(phi, 2, 2, 1)
    second = coherent_channel(changed, 2, 2, 1)
    half = F(1, 2)
    require(populations(first, 2) == ((half, half), (half, half)),
            "original population law")
    require(populations(second, 2) == ((F(1), F(0)), (F(0), F(1))),
            "transformed population law")
    require(first != second, "four-state coherent counterexample")

    preserving = violating = 0
    for order in permutations(m):
        q = perm_from_order(m, order)
        same = populations(coherent_channel(conj(phi, q, m), 2, 2, 1), 2) == populations(first, 2)
        preserving += int(same)
        violating += int(not same)
    require((preserving, violating) == (16, 8), "16/8 census mismatch")

    exhaustive = 0
    for v, h in ((2, 2), (2, 3), (3, 2)):
        states = carrier(v, h)
        for order in permutations(states):
            p = perm_from_order(states, order)
            original = [coherent_channel(p, v, h, t) for t in range(5)]
            for sigma in permutations(range(h)):
                transformed = conj(p, global_hidden(v, h, sigma), states)
                require(all(coherent_channel(transformed, v, h, t) == original[t]
                            for t in range(5)),
                        f"global hidden permutation coherence: {(v, h)}")
                exhaustive += 1
    require(exhaustive == 5808, "coherent hidden-only coverage count")
    # Fibre-specific permutation: population-positive but NOT coherent-positive.
    witness = None
    for order in permutations(m):
        p = perm_from_order(m, order)
        controlled = fibre_hidden(2, 2, ((0, 1), (1, 0)))
        cp = conj(p, controlled, m)
        if coherent_channel(cp, 2, 2, 1) != coherent_channel(p, 2, 2, 1):
            witness = (p, cp)
            break
    require(witness is not None, "fibre-dependent coherent countercontrol not found")
    require(all(populations(coherent_channel(witness[0], 2, 2, t), 2)
                == populations(coherent_channel(witness[1], 2, 2, t), 2)
                for t in range(5)), "fibre-dependent population invariance")

    rho = ((F(1, 2), F(1, 4)), (F(1, 4), F(1, 2)))
    require(sum(rho[i][i] for i in range(2)) == 1, "ancilla not normalized")
    dswap = {0: 1, 1: 0}
    enlargements = 0
    for order in list(permutations(carrier(2, 3)))[:160]:
        p = perm_from_order(carrier(2, 3), order)
        for t in range(4):
            require(extended_channel(p, 2, 3, dswap, rho, t) ==
                    coherent_channel(p, 2, 3, t), "decoupled coherent enlargement")
        enlargements += 1
    require(enlargements == 160, "enlargement coverage")

    def mutate_invalid():
        q = {s: (0, 0) for s in m}
        inverse(q, m)
    def mutate_counterexample():
        require(coherent_channel(phi, 2, 2, 1) !=
                coherent_channel(phi, 2, 2, 1), "must detect equality")
    def mutate_observed_matrix():
        require(populations(second, 2) == populations(first, 2), "wrong expected")
    def mutate_wrong_census():
        require((preserving, violating) == (15, 9), "must reject altered census")
    def mutate_controlled_hidden():
        require(coherent_channel(witness[0], 2, 2, 1) ==
                coherent_channel(witness[1], 2, 2, 1),
                "a fibre-dependent map is not coherent-invariant")
    def mutate_nondecoupled():
        # Explicitly evolve |a,h,d> -> |a XOR d,h,d>, uniform ancillary d.
        # This is a bijection, but the ancilla *couples* to the visible bit.
        original = {s: s for s in m}
        baseline = populations(coherent_channel(original, 2, 2, 1), 2)
        coupled = tuple(tuple(
            F(sum(int((a ^ d) == c) for d in range(2)), 2)
            for c in range(2))
            for a in range(2))
        require(coupled == baseline, "coupled ancilla cannot be ignored")
    mutants = [
        expect_failure(mutate_invalid, "invalid-bijection"),
        expect_failure(mutate_counterexample, "collapsed-counterexample"),
        expect_failure(mutate_observed_matrix, "wrong-population"),
        expect_failure(mutate_wrong_census, "changed-16-8"),
        expect_failure(mutate_controlled_hidden, "fibre-coherence"),
        expect_failure(mutate_nondecoupled, "coupled-ancilla"),
    ]
    require(len(mutants) == 6, "mutant coverage")
    return {
        "verdict": "PASS",
        "carrier_global_hidden_cases": exhaustive,
        "decoupled_coherent_cases": enlargements,
        "one_step_full_state_relabelling": {"preserving": preserving, "violating": violating},
        "fibre_dependent": "population invariant; coherent counterexample found",
        "killed_mutants": mutants,
        "scope": "finite exact controls; all-partitions equivalence not tested"
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, separators=(",", ":")))
