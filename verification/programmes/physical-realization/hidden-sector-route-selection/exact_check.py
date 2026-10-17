#!/usr/bin/env python3
"""Exact design examples; no empirical data and no claimed native OI model."""
from fractions import Fraction as F
from itertools import permutations, product
import json

checks = 0


def require(condition, name):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(name)


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def push(p, f):
    out = [F(0)] * len(p)
    for i, j in enumerate(f):
        out[j] += p[i]
    return out


def project(p):
    return [p[0] + p[1], p[2] + p[3]]


def stochastic(m):
    return all(all(x >= 0 for x in row) and sum(row) == 1 for row in m)


def evolve(p, m):
    return [sum(p[i] * m[i][j] for i in range(len(p)))
            for j in range(len(p))]


def moment(p, degree):
    return sum(weight * x ** degree for weight, x in zip(p, (-1, 0, 1)))


for n in range(2, 5):
    u = [F(1, n)] * n
    for numerators in product(range(3), repeat=n):
        if not sum(numerators):
            continue
        p = [F(x, sum(numerators)) for x in numerators]
        for perm in permutations(range(n)):
            require(tv(push(p, perm), u) == tv(p, u), "permutation TV")

nonuniform = [F(1), F(0)]
require(tv(nonuniform, [F(1, 2)] * 2) > 0, "nonvacuous initial deviation")
stationary = [F(1, 2), F(0), F(1, 2)]
initial = [F(0), F(1, 2), F(1, 2)]
require(push(stationary, (0, 0, 2)) == stationary
        and tv(push(initial, (0, 0, 2)), stationary) < tv(initial, stationary),
        "nonbijection countercontrol")

cycle = (1, 2, 3, 0)
p = [F(1, 2), F(1, 2), F(0), F(0)]
fine, coarse = [], []
for _ in range(5):
    fine.append(tv(p, [F(1, 4)] * 4))
    coarse.append(tv(project(p), [F(1, 2)] * 2))
    p = push(p, cycle)
require(fine == [F(1, 2)] * 5, "constant fine deviation")
require(coarse == [F(1, 2), F(0), F(1, 2), F(0), F(1, 2)],
        "projected revival")
p0, p1 = [F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)]
require(project(p0) == project(p1), "equal input projections")
require(project(push(p0, cycle)) != project(push(p1, cycle)),
        "different output projections")

q = [F(1, 4), F(1, 2), F(1, 4)]
eps = F(1, 16)
rho = [q[0] + eps, q[1] - 2 * eps, q[2] + eps]
require(sum(rho) == 1 and min(rho) >= 0, "perturbation is probability law")
require(moment(rho, 1) == 0 and moment(rho, 3) == 0, "odd moments zero")
require(moment(rho, 2) == F(5, 8), "variance changed")
require(moment(rho, 2) / moment(q, 2) == F(5, 4), "response amplitude")

for retained in (F(1), F(1, 2), F(1, 4), F(0)):
    m = [[retained * F(i == j) + (1 - retained) * q[j]
          for j in range(3)] for i in range(3)]
    require(stochastic(m), "reset stochastic")
    require(evolve(q, m) == q, "reset reference invariant")
    expected = [q[i] + retained * (rho[i] - q[i]) for i in range(3)]
    require(evolve(rho, m) == expected, "reset eigenmode")
require(evolve(rho, [[F(i == j) for j in range(3)] for i in range(3)]) == rho,
        "identity does not relax")
require(not stochastic([[F(1), F(1), F(0)]] * 3), "invalid kernel rejected")
require([q[0], q[1], q[2]] == q and moment(q, 3) == 0,
        "zero perturbation null")

amplitude = F(1, 4)
exit_l1, exit_l2, variable_initial, continued = [], [], [], []
for ratio in (1, 2, 4, 8):
    exit_l1.append(amplitude / ratio)
    exit_l2.append(amplitude / ratio ** 2)
    variable_initial.append(F(ratio, 32) / ratio)
    continued.append((amplitude / ratio) * F(ratio, 16))
require(exit_l1 != exit_l2, "order-H rates do not fix exponent")
require(variable_initial == [F(1, 32)] * 4, "initial scale dependence cancels trend")
require(continued == [F(1, 64)] * 4, "common end cancels exit trend")

mutations = {
    "nonbijective permutation": tv(push([F(1, 2)] * 2, (0, 0)), [F(1, 2)] * 2) != 0,
    "no projected revival": coarse != [F(1, 2), F(0), F(0), F(0), F(0)],
    "wrong second moment": moment(rho, 2) != moment(q, 2),
    "forced third moment": moment(rho, 3) != eps,
    "unit exponent for both rates": exit_l2 != exit_l1,
    "frozen-exit formula after common-end relaxation": continued != exit_l1,
}
for name, rejected in mutations.items():
    require(rejected, name)

print(json.dumps({
    "controls": checks,
    "mutation_countercontrols_rejected": len(mutations),
    "fine_tv": [str(x) for x in fine],
    "projected_tv": [str(x) for x in coarse],
    "variance_ratio": str(moment(rho, 2) / moment(q, 2)),
    "third_moment": str(moment(rho, 3)),
    "exit_exponent_1": [str(x) for x in exit_l1],
    "exit_exponent_2": [str(x) for x in exit_l2],
    "common_end": [str(x) for x in continued],
    "verdict": "DESIGN_CHECKS_PASS; no empirical or native OI verdict",
}, sort_keys=True, indent=2))
