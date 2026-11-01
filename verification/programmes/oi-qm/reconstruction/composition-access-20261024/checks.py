#!/usr/bin/env python3
"""Small exact controls for REPORT.md; stdlib only, no native-lattice claim."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def add(d, k, v):
    d[k] += v


def tv(p, q):
    return sum((abs(p.get(k, 0) - q.get(k, 0))
                for k in p.keys() | q.keys()), F(0)) / 2


def marginal(p, f):
    d = defaultdict(F)
    for k, v in p.items():
        add(d, f(k), v)
    return dict(d)


def need(ok, name):
    if not ok:
        raise RuntimeError(name)


def native_toy(qg, a):
    # Independent direct implementation, with a private retained garbage bit.
    q, g = qg
    d = defaultdict(F)
    add(d, ((0, -1), (q, 1 - g)), F(1, 4))
    for seed in range(4):
        b = q if a == 0 else 1 - q if a == 1 else seed % 2
        g2 = g ^ q ^ (a % 2) ^ (seed // 2)
        add(d, ((1, b), (b, g2)), F(3, 16))
    return dict(d)


def reference_toy(q, a):
    if a == 0:
        return {((0, -1), q): F(1, 4), ((1, q), q): F(3, 4)}
    if a == 1:
        return {((0, -1), q): F(1, 4), ((1, 1-q), 1-q): F(3, 4)}
    return {((0, -1), q): F(1, 4), ((1, 0), 0): F(3, 8),
            ((1, 1), 1): F(3, 8)}


RECORDS = ((0, -1), (1, 0), (1, 1))


def execute(start, kernel, policy, decoder):
    state = {((), start): F(1)}
    for i in range(2):
        nxt = defaultdict(F)
        for (hist, x), p in state.items():
            a = policy[0] if i == 0 else policy[1 + RECORDS.index(hist[0])]
            for (r, xp), k in kernel(x, a).items():
                add(nxt, (hist + (r,), xp), p * k)
        state = dict(nxt)
    return marginal(state, lambda hx: (hx[0], decoder(hx[1])))


def report():
    # Local law and exhaustive finite policy sanity checks of the written proof.
    local_count = 0
    for q, g, a in product(range(2), range(2), range(3)):
        p = native_toy((q, g), a)
        need(sum(p.values()) == 1, "toy normalization")
        decoded = marginal(p, lambda rx: (rx[0], rx[1][0]))
        need(decoded == reference_toy(q, a), "local intertwining")
        local_count += 1
    policy_count = 0
    for policy in product(range(3), repeat=4):
        for q, g in product(range(2), repeat=2):
            p = execute((q, g), native_toy, policy, lambda x: x[0])
            r = execute(q, reference_toy, policy, lambda x: x)
            need(p == r, "adaptive full record and terminal carrier")
            policy_count += 1
    need(native_toy((0, 0), 0) != native_toy((0, 1), 0),
         "private fibers actually differ")

    independent = {(r, c): F(1, 4) for r, c in product(range(2), repeat=2)}
    copied = {(r, r): F(1, 2) for r in range(2)}
    need(marginal(independent, lambda x: x[0]) ==
         marginal(copied, lambda x: x[0]), "record marginal equal")
    need(marginal(independent, lambda x: x[1]) ==
         marginal(copied, lambda x: x[1]), "carrier marginal equal")
    need(tv(independent, copied) == F(1, 2), "joint marginal mutant detected")

    # Initially independent input/seed; a previous herald conditions on equality.
    prior = {(x, s): F(1, 4) for x, s in product(range(2), repeat=2)}
    need(prior == independent, "independent initial bank")
    post = {(x, s): p * 2 for (x, s), p in prior.items() if x == s}
    need(marginal(post, lambda xs: xs[1]) == {0: F(1, 2), 1: F(1, 2)},
         "seed remains fair conditional on herald")
    output = marginal(post, lambda xs: xs[0] ^ xs[1])
    need(tv(output, {0: F(1, 2), 1: F(1, 2)}) == F(1, 2),
         "hidden input correlation mutant detected")

    pairs = ((0, 0), (1, 0), (1, 1))
    def carrier(weights, y):
        return {(y ^ a, y, y ^ b, z): w / 2
                for (a, b), w in zip(pairs, weights) for z in range(2)}
    y_diagnostics = []
    for y in range(2):
        good = carrier((F(5, 10), F(3, 10), F(2, 10)), y)
        bad = carrier((F(5, 10), F(2, 10), F(3, 10)), y)
        need(marginal(good, lambda c: c[0]) == marginal(bad, lambda c: c[0]),
             "terminal X cannot see calibration swap")
        delta_r = tv(marginal(good, lambda c: c[2]), marginal(bad, lambda c: c[2]))
        need(delta_r == F(1, 10), "terminal R sees calibration swap")
        need(tv(good, bad) == F(1, 10), "full carrier sees calibration swap")
        y_diagnostics.append({"y": y, "terminal_x_tv": "0",
                              "terminal_r_tv": str(delta_r), "carrier_tv": "1/10"})

    # Matching success-conditioned laws does not match the whole experiment.
    ref_herald = {"success": F(1, 2), "failure": F(1, 2)}
    wrong_herald = {"success": F(3, 4), "failure": F(1, 4)}
    need(tv(ref_herald, wrong_herald) == F(1, 4), "failure mass mutant detected")

    # Accessing a private fiber distinguishes states identified by the decoder.
    need(tv({0: F(1)}, {1: F(1)}) == 1, "enlarged access separates private fibers")
    return {
        "schema": "oi-composition-access-controls-v1",
        "arithmetic": "exact rational, Python fractions.Fraction",
        "scope": "finite abstract instrument contract controls, not native lattice certification",
        "local_intertwining_cases": local_count,
        "depth_two_adaptive_policies": 81,
        "policy_initial_boundary_cases": policy_count,
        "private_fibers_differ_but_decoded_protocol_laws_match": True,
        "marginals_only_mutant_joint_tv": "1/2",
        "fresh_seed_after_herald_hidden_input_mutant_tv": "1/2",
        "failure_mass_mutant_tv": "1/4",
        "private_fiber_access_mutant_tv": "1",
        "post_y_calibration_controls": y_diagnostics,
        "controls_passed": True,
        "verdict": "HOLDS_WITHIN_ABSTRACT_FINITE_CONTROL_SCOPE"
    }


if __name__ == "__main__":
    result = report()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("RESULT.json")
    if path.exists():
        need(path.read_text() == encoded, "retained structured result mismatch")
    else:
        path.write_text(encoded)
    print(encoded, end="")
