#!/usr/bin/env python3
"""SUBSTATE-1: exact finite-word census for the 3-solenoid countercontrol.

The group automorphism is multiplication by 3 on the 3-solenoid.
Its first circle coordinate evolves by x -> 3x mod 1. Haar projection
onto that coordinate is Lebesgue-uniform. Read a bit at threshold 1/2.

This enumerates the *circle-factor* cylinder partitions exactly, using
integer arithmetic on a common endpoint grid. It does not simulate an
infinite carrier, prove its Haar projection theorem, or test OI's
gauge-coupled 3-D wave map.
"""
import itertools
import json
from fractions import Fraction


def require(condition, reason="control failed"):
    if not condition:
        raise AssertionError(reason)


def word_probabilities(h):
    """All (h+1)-bit cylinder probabilities, exact, without a Markov assumption."""
    n = 2 * (3 ** h)
    d = 2 * n  # midpoint sample of each exact atom [k/n,(k+1)/n)
    counts = {}
    for k in range(n):
        midpoint_num = 2 * k + 1
        word = tuple(int(2 * ((3 ** t * midpoint_num) % d) >= d)
                     for t in range(h + 1))
        counts[word] = counts.get(word, 0) + 1
    return {w: Fraction(c, n) for w, c in counts.items()}


def proposed_markov_probability(word):
    prob = Fraction(1, 2)
    for a, b in zip(word, word[1:]):
        prob *= Fraction(2, 3) if a == b else Fraction(1, 3)
    return prob


def matches_markov_law(words, transition):
    for word, actual in words.items():
        expected = Fraction(1, 2)
        for a, b in zip(word, word[1:]):
            expected *= transition[a][b]
        if actual != expected:
            return False
    return True


def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def matrix_power(A, n):
    P = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    for _ in range(n):
        P = multiply(P, A)
    return P


def rooted_matrix(words, h):
    return [[2 * sum((prob for word, prob in words.items()
                       if word[0] == a and word[-1] == b), Fraction(0))
             for b in range(2)] for a in range(2)]


def main():
    P = [[Fraction(2, 3), Fraction(1, 3)],
         [Fraction(1, 3), Fraction(2, 3)]]
    eye = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    controls = []
    matrices = {}
    for h in range(8):
        got = word_probabilities(h)
        expected_words = list(itertools.product((0, 1), repeat=h + 1))
        require(len(got) == len(expected_words), ("word count", h))
        require(sum(got.values(), Fraction(0)) == 1, ("normalization", h))
        for word in expected_words:
            require(got[word] == proposed_markov_probability(word), ("Markov", h, word))

        require(matches_markov_law(got, P), ("full-word comparator", h))
        rooted = rooted_matrix(got, h)
        m = 3 ** h
        predicted = [[Fraction(m + 1, 2 * m), Fraction(m - 1, 2 * m)],
                     [Fraction(m - 1, 2 * m), Fraction(m + 1, 2 * m)]]
        require(rooted == predicted == matrix_power(P, h), ("rooted semigroup", h))
        if h:
            require(rooted != eye, ("countercontrol: visible period", h))
        controls.append({"horizon": h, "words": len(got), "pass": True})
        matrices[str(h)] = [[str(x) for x in row] for row in rooted]

    # Independent low-order cylinder controls: these values were obtained
    # from partition lengths, not the generic Markov-product expression.
    w2 = word_probabilities(2)
    require(w2[(0, 0, 0)] == Fraction(2, 9))
    require(w2[(0, 0, 1)] == Fraction(1, 9))
    require(w2[(1, 0, 0)] == Fraction(1, 9))
    require(w2[(1, 0, 1)] == Fraction(1, 18))


    # Pairwise-independent XOR triples have uniform two-time marginals but
    # violate the uniform Markov word law. The full-word comparison must reject.
    xor_words = {w: Fraction(1, 4) if w[2] == (w[0] ^ w[1]) else Fraction(0)
                 for w in itertools.product((0, 1), repeat=3)}
    for i, j in ((0, 1), (0, 2), (1, 2)):
        require(all(sum((p for w, p in xor_words.items() if w[i] == a and w[j] == b),
                        Fraction(0)) == Fraction(1, 4)
                    for a, b in itertools.product((0, 1), repeat=2)),
                ("XOR pairwise uniformity", i, j))
    require(not matches_markov_law(xor_words, [[Fraction(1, 2)] * 2 for _ in range(2)]),
            "full-word comparator accepted the non-Markov XOR law")

    # Every verdict is printed only after the exact controls pass.
    print(json.dumps({
        "status": "PASS",
        "non_markov_xor_countercontrol": "REJECTED by full-word comparison",
        "controls": controls,
        "three_solenoid_group_automorphism": "x -> 3x; invertible on solenoid",
        "readout": "first circle coordinate, binary half-interval",
        "one_step_markov": [[str(x) for x in row] for row in P],
        "rooted_matrices": matrices,
        "result": "finite-time Markov and P-divisible, no exact visible identity return for t >= 1",
        "limits": "exact cylinder enumeration h <= 7; all-h proof is in solenoid-countercontrol.md"
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
