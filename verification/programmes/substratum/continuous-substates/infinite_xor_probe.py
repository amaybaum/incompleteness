#!/usr/bin/env python3
"""Exact bounded regression for infinite-xor-counterexample.md; not an all-time proof."""
import itertools
import json
from fractions import Fraction as F


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def words(h):
    counts = {}
    for phase in range(3):
        blocks = (phase + h)//3 + 1
        for bits in itertools.product((0, 1), repeat=2*blocks):
            word = []
            for t in range(h+1):
                block, p = divmod(phase+t, 3)
                a, b = bits[2*block:2*block+2]
                word.append((a, b, a ^ b)[p])
            w = tuple(word)
            counts[w] = counts.get(w, F(0)) + F(1, 3*4**blocks)
    return counts


def main():
    for h in range(1, 8):
        law = words(h)
        require(sum(law.values(), F(0)) == 1, ("normalization", h))
        for t in range(1, h+1):
            for a, b in itertools.product((0, 1), repeat=2):
                joint = sum((p for w, p in law.items() if w[0] == a and w[t] == b), F(0))
                require(joint == F(1, 4), ("root pair", h, t, a, b))
    law = words(2)
    for w in itertools.product((0, 1), repeat=3):
        require(law[w] == (F(1, 6) if w[0] ^ w[1] ^ w[2] == 0 else F(1, 12)),
                ("triple", w))
    for a, b in itertools.product((0, 1), repeat=2):
        require(law[(a, b, a ^ b)]/F(1, 4) == F(2, 3), ("C4", a, b))
    print(json.dumps({"status": "PASS", "horizons": [1, 7],
                      "rooted_positive_time": "J2", "conditional_memory_gap": "1/6",
                      "scope": "finite regression; all-time paper proof separate"}, sort_keys=True))


if __name__ == "__main__":
    main()
