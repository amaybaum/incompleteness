#!/usr/bin/env python3
"""Independent controls for the frozen P24.5 candidate's boundary claims."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

checks = 0


def require(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)


def log2_integer(value):
    require(value > 0 and value & (value - 1) == 0, "exact power-of-two entropy term")
    return value.bit_length() - 1


def entropy(values):
    counts = Counter(values)
    total = sum(counts.values())
    return Fraction(log2_integer(total)) - sum(
        (Fraction(count, total) * log2_integer(count) for count in counts.values()), Fraction()
    )


def conditional_information(a, b, c):
    return entropy(list(zip(a, c))) + entropy(list(zip(b, c))) - entropy(c) - entropy(list(zip(a, b, c)))


registers = []
for m in range(1, 7):
    states = list(product(range(2), repeat=m + 1))
    past = [s[:m] for s in states]
    present = [s[m] for s in states]
    one_step = [s[0] for s in states]
    next_m = [s[:m] for s in states]
    future_period = [s for s in states]
    hidden_now = [s[:m] for s in states]
    identifying_record = [s for s in states]
    one = conditional_information(past, one_step, present)
    full = conditional_information(past, future_period, present)
    block = conditional_information(past, next_m, present)
    residual = entropy(list(zip(hidden_now, identifying_record))) - entropy(identifying_record)
    require(one == 1, "one-step conditional predictive information is one bit")
    require(full == block == m, "full future and next-m block information equal hidden capacity")
    require(residual == 0, "identified current hidden store has zero residual entropy")
    registers.append({"hidden_bits": m, "one_step_conditional_information_bits": int(one),
                      "full_future_conditional_information_bits": int(full),
                      "residual_hidden_entropy_bits": int(residual)})

# Test the product-carrier singleton equivalence separately from the prior
# controls, across all four-state dynamics, supports and short nonempty words.
states = list(product(range(2), repeat=2))
current_hidden_cases = 0
for p in permutations(range(4)):
    for support_bits in range(1, 16):
        support = [s for s in range(4) if support_bits >> s & 1]
        for length in range(1, 6):
            by_record = defaultdict(list)
            for initial in support:
                state = initial
                word = []
                for step in range(length):
                    word.append(states[state][0])
                    if step + 1 < length:
                        state = p[state]
                by_record[tuple(word)].append((initial, state))
            for fibre in by_record.values():
                initials = {s for s, _ in fibre}
                currents = {s for _, s in fibre}
                hidden = {states[s][1] for s in currents}
                require((len(initials) == 1) == (len(currents) == 1) == (len(hidden) == 1),
                        "nonempty retained record fixes visible coordinate and preserves singleton criterion")
                current_hidden_cases += 1

# Why k >= 1 must be explicit: identity dynamics and empty record leave two
# possible visible states but the same hidden coordinate.
empty_support = [(0, 0), (1, 0)]
require(len(empty_support) == 2 and len({h for _, h in empty_support}) == 1,
        "empty record does not give the product hidden singleton equivalence")

# A capacity shortfall forces one large fibre, not universal ambiguity.
compressed_record = [0, 0, 0, 1]
counts = Counter(compressed_record)
require(max(counts.values()) >= 2 and min(counts.values()) == 1,
        "pigeonhole collision coexists with a singleton fibre")

result = {"status": "PASS", "checks": checks,
          "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "registers": registers, "current_hidden_cases": current_hidden_cases,
          "scope": "Exact bounded controls only; not CI, kernel proof or a physical record-retention mechanism."}
print(json.dumps(result, indent=2, sort_keys=True))
