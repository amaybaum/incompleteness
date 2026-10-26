#!/usr/bin/env python3
"""Exact finite controls for the operational-quotient candidate; stdlib only."""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


COUNTS = Counter()


def require(name, condition):
    if not condition:
        raise RuntimeError(name)
    COUNTS[name] += 1


LAMBDA = tuple(product((-1, 1), repeat=3))
INDEX = {v: i for i, v in enumerate(LAMBDA)}
U = (F(1, 8),) * 8


def moments(p):
    return tuple(sum((p[j] * LAMBDA[j][a] for j in range(8)), F(0))
                 for a in range(3))


def mass(p):
    return sum(p, F(0))


def scaled(p, c):
    return tuple(c * v for v in p)


def allowed_octahedron(p):
    return min(p) >= 0 and sum(map(abs, moments(p))) <= mass(p)


def allowed_ball(p):
    return min(p) >= 0 and sum(v * v for v in moments(p)) <= mass(p) ** 2


def eigen(a, s):
    return tuple(F(int(v[a] == s), 4) for v in LAMBDA)


def instrument(p, a, s, reset=True):
    if reset:
        weight = sum((p[j] for j in range(8) if LAMBDA[j][a] == s), F(0))
        return scaled(eigen(a, s), weight)
    return tuple(p[j] if LAMBDA[j][a] == s else F(0) for j in range(8))


def push(p, r):
    out = [F(0)] * 8
    for j, v in enumerate(LAMBDA):
        out[INDEX[tuple(sum(r[a][b] * v[b] for b in range(3))
                        for a in range(3))]] += p[j]
    return tuple(out)


# Complex numbers and matrices are represented over Q, never floats.
def c(real=0, imag=0):
    return (F(real), F(imag))


def ca(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cm(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cc(x):
    return (x[0], -x[1])


ZERO = c()
ONE = c(1)
IDENTITY = ((ONE, ZERO), (ZERO, ONE))
PAULI = (
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, c(0, -1)), (c(0, 1), ZERO)),
    ((ONE, ZERO), (ZERO, c(-1))),
)
H_RAW = ((ONE, ONE), (ONE, c(-1)))
S_MATRIX = ((ONE, ZERO), (ZERO, c(0, 1)))
ROT_RAW = ((c(2, -1), ZERO), (ZERO, c(2, 1)))


def madd(a, b):
    return tuple(tuple(ca(a[i][j], b[i][j]) for j in range(2)) for i in range(2))


def mscale(a, k):
    return tuple(tuple((k * z[0], k * z[1]) for z in row) for row in a)


def mmul(a, b):
    return tuple(tuple(ca(cm(a[i][0], b[0][j]), cm(a[i][1], b[1][j]))
                       for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple(cc(a[j][i]) for j in range(2)) for i in range(2))


def conjugate(a, u, norm=1):
    return mscale(mmul(mmul(u, a), adjoint(u)), F(1, norm))


def decode(p):
    x, y, z = moments(p)
    w = mass(p)
    return ((c((w + z) / 2), c(x / 2, -y / 2)),
            (c(x / 2, y / 2), c((w - z) / 2)))


def projector(a, s):
    return mscale(madd(IDENTITY, mscale(PAULI[a], s)), F(1, 2))


def quantum_instrument(rho, a, s):
    pr = projector(a, s)
    return mmul(mmul(pr, rho), pr)


def trace(a):
    return ca(a[0][0], a[1][1])


def determinant(a):
    x, y = cm(a[0][0], a[1][1]), cm(a[0][1], a[1][0])
    return (x[0] - y[0], x[1] - y[1])


def tv(p, q):
    return sum((abs(a - b) for a, b in zip(p, q)), F(0)) / 2


def multiply3(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
H3 = ((0, 0, 1), (0, -1, 0), (1, 0, 0))
S3 = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
R3 = ((F(3, 5), F(-4, 5), 0), (F(4, 5), F(3, 5), 0), (0, 0, 1))


def classical_gate(p, gate):
    return push(p, (I3, H3, S3)[gate])


def quantum_gate(rho, gate):
    return rho if gate == 0 else conjugate(rho, (H_RAW, S_MATRIX)[gate - 1],
                                         2 if gate == 1 else 1)


def row_rank(a):
    a = [list(map(F, row)) for row in a]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((k for k in range(rank, len(a)) if a[k][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        k = a[rank][col]
        a[rank] = [x / k for x in a[rank]]
        for r in range(len(a)):
            if r != rank:
                k = a[r][col]
                a[r] = [x - k * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def result():
    global COUNTS
    COUNTS = Counter()
    eigens = [eigen(a, s) for a in range(3) for s in (-1, 1)]
    xy = [tuple(F(int(v[0] * v[1] == s), 4) for v in LAMBDA)
          for s in (-1, 1)]
    parity = [tuple(F(int(v[0] * v[1] * v[2] == s), 4) for v in LAMBDA)
              for s in (-1, 1)]
    nus = [tuple(F(2, 3) * U[j] + F(int(j == k), 3) for j in range(8))
           for k in range(8)]
    preparations = eigens + [U] + xy + parity + nus
    for p in preparations:
        require("admissible_preparation", allowed_octahedron(p) and mass(p) == 1)
        require("decoded_density", determinant(decode(p))[0] >= 0)

    # Independent matrix projectors validate every outcome map, including zeros.
    for p in preparations:
        for a, s in product(range(3), (-1, 1)):
            post = instrument(p, a, s)
            require("projector_intertwining", decode(post) == quantum_instrument(decode(p), a, s))
            require("post_branch_invariant", allowed_octahedron(post))
        for g in (1, 2):
            require("matrix_gate_intertwining",
                    decode(classical_gate(p, g)) == quantum_gate(decode(p), g))

    group = {I3}
    pending = [I3]
    while pending:
        r = pending.pop()
        for gen in (H3, S3):
            q = multiply3(gen, r)
            if q not in group:
                group.add(q)
                pending.append(q)
    require("clifford_count", len(group) == 24)
    for r in group:
        for p in preparations:
            out = push(p, r)
            mean = tuple(sum(r[a][b] * moments(p)[b] for b in range(3))
                         for a in range(3))
            require("clifford_moment_map", moments(out) == mean)
            require("clifford_preparation_invariant", allowed_octahedron(out))

    # Hidden Fourier characters of degree >=2 span the moment kernel.
    for degrees in ((0, 1), (0, 2), (1, 2), (0, 1, 2)):
        v = tuple(F(1 if len([i for i in degrees if lam[i] == -1]) % 2 == 0 else -1)
                  for lam in LAMBDA)
        require("kernel_character", mass(v) == 0 and moments(v) == (0, 0, 0))
        for a, s in product(range(3), (-1, 1)):
            require("instrument_kernel_congruence", instrument(v, a, s) == (F(0),) * 8)
        for r in group:
            require("gate_kernel_congruence", moments(push(v, r)) == (0, 0, 0))

    # Full finite records, settings/flags/clocks included in branch keys.
    def policy(k, history):
        t = len(history)
        if k == 0:
            return 0, t % 3
        if k == 1:
            return 0, 0
        if k == 2:
            return 1 if not history or history[-1][-1] == 1 else 2, (t + sum(x[-1] == 1 for x in history)) % 3
        return 2 if t % 2 else 1, (2 + t + sum(x[-1] for x in history)) % 3

    for p in preparations:
        for k in range(4):
            branches = [((), p, decode(p))]
            for t in range(3):
                next_branches = []
                for history, hp, qp in branches:
                    g, a = policy(k, history)
                    hp, qp = classical_gate(hp, g), quantum_gate(qp, g)
                    for s in (-1, 1):
                        record = (t + 1, g, a, 1, s)
                        ho, qo = instrument(hp, a, s), quantum_instrument(qp, a, s)
                        require("adaptive_full_branch_law", decode(ho) == qo)
                        next_branches.append((history + (record,), ho, qo))
                branches = next_branches
            require("adaptive_total_mass", sum(mass(b[1]) for b in branches) == 1)
            require("adaptive_all_records_retained", len(branches) == 8)

    # Explicit globally invertible reset; source register is retained as workspace.
    def reset_label(a, s, seed):
        vals = [None] * 3
        vals[a] = s
        for bit, axis in enumerate(i for i in range(3) if i != a):
            vals[axis] = 1 if seed & (1 << bit) else -1
        return INDEX[tuple(vals)]

    for a in range(3):
        images = set()
        for src, blank, seed, rec in product(range(8), range(8), range(4), range(2)):
            s = LAMBDA[src][a]
            label = reset_label(a, s, seed)
            out = ((blank + label) % 8, src, seed, rec ^ int(s == -1))
            images.add(out)
            back = (out[1], (out[0] - reset_label(a, LAMBDA[out[1]][a], out[2])) % 8,
                    out[2], out[3] ^ int(LAMBDA[out[1]][a] == -1))
            require("dilation_inverse", back == (src, blank, seed, rec))
        require("dilation_bijection", len(images) == 512)
        for src in range(8):
            labels = [reset_label(a, LAMBDA[src][a], r) for r in range(4)]
            out = tuple(F(labels.count(j), 4) for j in range(8))
            require("dilation_ready_kernel", out == eigen(a, LAMBDA[src][a]))

    # The old pointwise invariant is not invariant under this new decoder.
    zminus = eigen(2, -1)
    hpost = push(zminus, H3)
    require("hadamard_negative_offdiagonal", decode(hpost)[0][1] == c(F(-1, 2)))
    require("hadamard_output_positive", determinant(decode(hpost)) == ZERO)

    # No-reset and access controls: identical moments can have different records.
    require("same_moments_xy_pair", decode(xy[0]) == decode(xy[1]))
    def no_reset_law(p):
        return tuple(mass(instrument(instrument(p, 0, s, False), 1, t, False))
                     for s, t in product((-1, 1), repeat=2))
    no_reset_tv = tv(no_reset_law(xy[0]), no_reset_law(xy[1]))
    require("no_reset_splits_quotient", no_reset_tv == 1)
    for p in xy:
        for s in (-1, 1):
            post = scaled(instrument(p, 0, s, False), 2)
            require("no_reset_post_nonpositive", determinant(decode(post)) == c(F(-1, 4)))

    old_workspace_tvs = []
    for a in range(3):
        records = []
        for p in xy:
            records.append(tuple(sum(p[j] for j, v in enumerate(LAMBDA)
                                     if (v[0], v[a]) == (s, w))
                                 for s, w in product((-1, 1), repeat=2)))
        old_workspace_tvs.append(tv(*records))
    require("old_workspace_joint_access", old_workspace_tvs == [0, 1, 0])
    for a, s, seed in product(range(3), (-1, 1), range(4)):
        p = tuple(F(int(j == reset_label(a, s, seed))) for j in range(8))
        require("fresh_seed_exposure_nonpositive", determinant(decode(p)) == c(F(-1, 2)))

    # Affine span and rational non-Clifford impossibility witness.
    require("admissible_fibre_span", row_rank(nus) == 8)
    rt = tuple(zip(*R3))
    require("rational_rotation_orthogonal", multiply3(R3, rt) == I3)
    for p in preparations:
        x, y, z = moments(p)
        target = tuple(sum(R3[a][b] * (x, y, z)[b] for b in range(3)) for a in range(3))
        dm = ((c((1 + target[2]) / 2), c(target[0] / 2, -target[1] / 2)),
              (c(target[0] / 2, target[1] / 2), c((1 - target[2]) / 2)))
        require("rational_rotation_matrix_control", dm == conjugate(decode(p), ROT_RAW, 5))
    vertex = (1, -1, 1)
    rotated_vertex = tuple(sum(R3[a][b] * vertex[b] for b in range(3)) for a in range(3))
    require("cube_escape", rotated_vertex[0] == F(7, 5))
    pplus, pminus = nus[INDEX[vertex]], nus[INDEX[tuple(-x for x in vertex)]]
    source_tv = tv(pplus, pminus)
    target_plus = (F(11, 15), F(4, 15))
    target_minus = tuple(reversed(target_plus))
    target_tv = tv(target_plus, target_minus)
    lower = (target_tv - source_tv) / 2
    require("pair_source_tv", source_tv == F(1, 3))
    require("pair_target_tv", target_tv == F(7, 15))
    require("pair_error_floor", lower == F(1, 15))
    # Independent exhaustive extreme response controls, no LP solver needed.
    maximal_tv = F(0)
    for mask in range(256):
        probs = [sum(p[j] for j in range(8) if mask & (1 << j)) for p in (pplus, pminus)]
        diff = abs(probs[0] - probs[1])
        maximal_tv = max(maximal_tv, diff)
        require("all_deterministic_response_contraction", diff <= source_tv)
    require("tight_source_tv", maximal_tv == source_tv)
    actual_plus = (F(2, 3), F(1, 3))
    actual_minus = tuple(reversed(actual_plus))
    require("tight_pair_error", max(tv(actual_plus, target_plus), tv(actual_minus, target_minus)) == lower)
    require("ball_codomain_does_not_remove_pair", allowed_ball(pplus) and allowed_ball(pminus))

    # State-coverage is a distinct issue from kernel availability.
    rstar = (F(3, 5), F(4, 5), F(0))
    require("missing_octahedron_state", sum(abs(x) for x in rstar) > 1 and sum(x*x for x in rstar) == 1)
    closest = tuple(F(2, 5) * eigens[1][j] + F(3, 5) * eigens[3][j] for j in range(8))
    require("closest_octahedron_preparation", allowed_octahedron(closest))
    coverage_gap = max(abs(x - y) / 2 for x, y in zip(rstar, moments(closest)))
    require("two_pauli_coverage_gap", coverage_gap == F(1, 10))
    # An enlarged supplied Bloch-ball prior removes state coverage, not the pair obstruction.
    product_prior = tuple(F(1, 8) * (1 + rstar[0]*v[0]) * (1 + rstar[1]*v[1]) * (1 + rstar[2]*v[2])
                          for v in LAMBDA)
    require("ball_prior_covers_missing_state", allowed_ball(product_prior) and moments(product_prior) == rstar)
    require("ball_prior_outside_octahedron", not allowed_octahedron(product_prior))

    return {
        "schema": "oi-operational-quotient-v3.1",
        "verdict": "PASS",
        "scope": "abstract eight-sign quotient with supplied preparation/access/reset contract",
        "preparations_checked": len(preparations),
        "hidden_states": 8,
        "clifford_rotations": len(group),
        "local_quantum_instrument_branches": len(preparations)*6,
        "adaptive_policies": 4,
        "adaptive_depth": 3,
        "adaptive_leaf_records": len(preparations)*4*8,
        "dilation_states_per_axis": 512,
        "hadamard_output_offdiagonal": "-1/2",
        "no_reset_two_read_tv": str(no_reset_tv),
        "public_X_plus_workspace_field_tv": list(map(str, old_workspace_tvs)),
        "exposed_fresh_seed_post_determinant": "-1/2",
        "fibre_preparation_linear_span_rank": 8,
        "nonclifford_rotated_cube_coordinate": str(rotated_vertex[0]),
        "source_pair_tv": str(source_tv),
        "target_rotated_X_pair_tv": str(target_tv),
        "fixed_representation_pair_error_floor": str(lower),
        "octahedron_two_Pauli_state_coverage_gap": str(coverage_gap),
        "checks": dict(sorted(COUNTS.items())),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    payload = json.dumps(result(), indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(payload)
    else:
        print(payload, end="")
