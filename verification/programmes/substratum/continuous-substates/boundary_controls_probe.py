#!/usr/bin/env python3
"""SUBSTATE-1: finite-visible / infinite-internal-state countercontrols.

Exact cyclic finite prefixes of an invertible two-sided Bernoulli shift.
The proof for the infinite product system is in BOUNDARY-CONTROLS.md.
Not a native OI model or a test of the GR area law.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def shift_and_xor(bits, pointer):
    """(x,b) -> (left-shift(x), b xor x[0]), on a cyclic finite prefix."""
    return bits[1:] + bits[:1], pointer ^ bits[0]


def reverse_shift_and_xor(bits, pointer):
    oldbits = bits[-1:] + bits[:-1]
    return oldbits, pointer ^ oldbits[0]


def horizon_counts(q, n):
    counts = Counter()
    for bits in product((0, 1), repeat=q):
        for pointer in (0, 1):
            now, b = bits, pointer
            record = (b,)
            for _ in range(n):
                now, b = shift_and_xor(now, b)
                record += (b,)
            counts[record] += 1
    return counts


def decoupled_counts(q, n):
    counts = Counter()
    for bits in product((0, 1), repeat=q):
        for pointer in (0, 1):
            counts[(pointer,) * (n + 1)] += 1
    return counts


def fixed_hidden_toggle_counts(q, n):
    """(x,b) -> (x,b xor x[0]); x has q hidden bits."""
    counts = Counter()
    for bits in product((0, 1), repeat=q):
        for pointer in (0, 1):
            counts[tuple(pointer ^ (bits[0] if t % 2 else 0)
                         for t in range(n + 1))] += 1
    return counts



def rooted_matrix(counts, time):
    out = []
    for a in (0, 1):
        denom = sum(n for word, n in counts.items() if word[0] == a)
        assert denom
        out.append(tuple(Fraction(
            sum(n for word, n in counts.items()
                if word[0] == a and word[time] == b), denom
        ) for b in (0, 1)))
    return tuple(out)


def check():
    for horizon in range(1, 10):
        q = horizon + 1
        for bits in product((0, 1), repeat=q):
            for pointer in (0, 1):
                after = shift_and_xor(bits, pointer)
                assert reverse_shift_and_xor(*after) == (bits, pointer)
                assert shift_and_xor(*reverse_shift_and_xor(bits, pointer)) == (bits, pointer)
        shifted = horizon_counts(q, horizon)
        decoupled = decoupled_counts(q, horizon)
        assert len(shifted) == 2 ** (horizon + 1)
        assert set(shifted.values()) == {2 ** (q - horizon)}
        assert sum(shifted.values()) == 2 ** (q + 1)
        assert len(decoupled) == 2
        assert set(decoupled.values()) == {2 ** q}
        ident = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
        mixed = ((Fraction(1, 2), Fraction(1, 2)),
                 (Fraction(1, 2), Fraction(1, 2)))
        for t in range(1, horizon + 1):
            assert rooted_matrix(shifted, t) == mixed
            assert rooted_matrix(decoupled, t) == ident
        assert 2 ** (horizon + 1) * Fraction(1, 2 ** (horizon + 1)) == 1
        print(f"PASS SHIFT-XOR horizon={horizon}, q={q}: "
              f"{2**(horizon+1)} equiprobable records, "
              f"H(record)={horizon+1} bits; decoupled=2 constant records")
    # Finite reversible surrogate agrees with the unbounded stream for n < q,
    # but reveals its finite recurrence at 2q. The infinite stream has
    # P(b_{2q}=b_0)=1/2 instead (independent fresh increments).
    for q in range(2, 9):
        for bits in product((0, 1), repeat=q):
            for pointer in (0, 1):
                x, b = bits, pointer
                for _ in range(2 * q):
                    x, b = shift_and_xor(x, b)
                assert (x, b) == (bits, pointer)
        print(f"PASS FINITE-LONG-HORIZON q={q}: T^(2q)=identity")
    q = 5
    toggle = fixed_hidden_toggle_counts(q, 3)
    N = 2 ** (q + 1)
    assert toggle[(0, 0, 0, 0)] == toggle[(0, 1, 0, 1)] == N // 4
    assert toggle[(1, 1, 1, 1)] == toggle[(1, 0, 1, 0)] == N // 4
    assert len(toggle) == 4
    mixed = ((Fraction(1, 2), Fraction(1, 2)),
             (Fraction(1, 2), Fraction(1, 2)))
    ident = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    assert rooted_matrix(toggle, 1) == mixed
    assert rooted_matrix(toggle, 2) == ident
    print("PASS TOGGLE: rooted Gamma_1=[[1/2,1/2],[1/2,1/2]], "
          "Gamma_2=I; nonpermutation+identity return => P-indivisible")
    print("PASS TOTAL: 9 shift-XOR exact finite-prefix cases + 1 toggle case")


if __name__ == "__main__":
    check()
