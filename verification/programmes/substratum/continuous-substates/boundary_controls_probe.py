#!/usr/bin/env python3
"""SUBSTATE-1: finite-visible / infinite-internal-state countercontrols.

Exact cyclic finite prefixes of an invertible two-sided Bernoulli shift.
The proof for the infinite product system is in BOUNDARY-CONTROLS.md.
Not a native OI model.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

CHECKS = 0


def check(cond, msg):
    """Count a passed check; print the message and exit 1 on failure."""
    global CHECKS
    if not cond:
        print(f"FAIL {msg}")
        raise SystemExit(1)
    CHECKS += 1


def shift(bits):
    return bits[1:] + bits[:1]


def unshift(bits):
    return bits[-1:] + bits[:-1]


def t_d(bits, pointer):
    """D: (x,b) -> (left-shift(x), b)."""
    return shift(bits), pointer


def t_d_inv(bits, pointer):
    return unshift(bits), pointer


def t_r(bits, pointer):
    """R: (x,b) -> (left-shift(x), b xor x[0]), on a cyclic finite prefix."""
    return shift(bits), pointer ^ bits[0]


def t_r_inv(bits, pointer):
    oldbits = unshift(bits)
    return oldbits, pointer ^ oldbits[0]


def t_q(bits, pointer):
    """Q: (x,b) -> (x, b xor x[0]); an involution."""
    return bits, pointer ^ bits[0]


def states(q):
    for bits in product((0, 1), repeat=q):
        for pointer in (0, 1):
            yield bits, pointer


def visible_counts(step, q, n):
    """Counts of visible records (b_0,...,b_n) obtained by iterating step."""
    counts = Counter()
    for state in states(q):
        record = (state[1],)
        for _ in range(n):
            state = step(*state)
            record += (state[1],)
        counts[record] += 1
    return counts


def rooted_matrix(counts, time):
    out = []
    for a in (0, 1):
        denom = sum(n for word, n in counts.items() if word[0] == a)
        check(denom > 0, f"rooted matrix: no record starts with {a}")
        out.append(tuple(Fraction(
            sum(n for word, n in counts.items()
                if word[0] == a and word[time] == b), denom
        ) for b in (0, 1)))
    return tuple(out)


def rank2x2(m):
    if all(v == 0 for row in m for v in row):
        return 0
    return 1 if m[0][0] * m[1][1] - m[0][1] * m[1][0] == 0 else 2


IDENT = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
MIXED = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))


def main():
    horizons = 0
    for horizon in range(1, 10):
        q = horizon + 1
        for state in states(q):
            check(t_r_inv(*t_r(*state)) == state, f"R inverse, q={q}")
            check(t_r(*t_r_inv(*state)) == state, f"R inverse, q={q}")
            check(t_d_inv(*t_d(*state)) == state, f"D inverse, q={q}")
            check(t_d(*t_d_inv(*state)) == state, f"D inverse, q={q}")
        shifted = visible_counts(t_r, q, horizon)
        decoupled = visible_counts(t_d, q, horizon)
        check(len(shifted) == 2 ** (horizon + 1), f"R word count, n={horizon}")
        check(set(shifted.values()) == {2 ** (q - horizon)},
              f"R equiprobable words, n={horizon}")
        check(sum(shifted.values()) == 2 ** (q + 1), f"R total, n={horizon}")
        check(set(decoupled) == {(0,) * (horizon + 1), (1,) * (horizon + 1)},
              f"D constant words, n={horizon}")
        check(set(decoupled.values()) == {2 ** q}, f"D counts, n={horizon}")
        for t in range(1, horizon + 1):
            check(rooted_matrix(shifted, t) == MIXED,
                  f"R Gamma_{t}, n={horizon}")
            check(rooted_matrix(decoupled, t) == IDENT,
                  f"D Gamma_{t}, n={horizon}")
        horizons += 1
        print(f"PASS SHIFT-XOR horizon={horizon}, q={q}: "
              f"{2**(horizon+1)} equiprobable records, "
              f"H(record)={horizon+1} bits; decoupled=2 constant records")
    # The finite surrogate agrees with the unbounded stream for n <= q and
    # first differs at n = q+1; it returns exactly at 2q. The infinite stream
    # has P(b_{2q}=b_0)=1/2 instead (independent fresh increments).
    returns = 0
    for q in range(2, 9):
        for start in states(q):
            state = start
            for _ in range(2 * q):
                state = t_r(*state)
            check(state == start, f"T_R^(2q) identity, q={q}")
        returns += 1
        print(f"PASS FINITE-LONG-HORIZON q={q}: T^(2q)=identity")
    q = 5
    for state in states(q):
        check(t_q(*t_q(*state)) == state, f"Q involution, q={q}")
    toggle = visible_counts(t_q, q, 3)
    N = 2 ** (q + 1)
    check(toggle[(0, 0, 0, 0)] == toggle[(0, 1, 0, 1)] == N // 4, "Q words b0=0")
    check(toggle[(1, 1, 1, 1)] == toggle[(1, 0, 1, 0)] == N // 4, "Q words b0=1")
    check(len(toggle) == 4, "Q word count")
    gamma1 = rooted_matrix(toggle, 1)
    gamma2 = rooted_matrix(toggle, 2)
    check(gamma1 == MIXED, "Q Gamma_1")
    check(gamma2 == IDENT, "Q Gamma_2")
    check(rank2x2(gamma1) == 1, "Q rank Gamma_1 = 1")
    check(rank2x2(gamma2) == 2, "Q rank Gamma_2 = 2")
    print("PASS TOGGLE: rooted Gamma_1=[[1/2,1/2],[1/2,1/2]] (rank 1), "
          "Gamma_2=I (rank 2) => no Lambda with Gamma_2=Lambda Gamma_1; "
          "P-indivisible")
    print(f"PASS TOTAL: {CHECKS} checks; {horizons} shift-XOR/decoupled "
          f"horizons + {returns} long-horizon returns + 1 toggle case")


if __name__ == "__main__":
    main()
