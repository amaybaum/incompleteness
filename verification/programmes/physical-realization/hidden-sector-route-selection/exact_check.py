#!/usr/bin/env python3
"""Exact design examples; no empirical data and no claimed native OI model.

Recipe: python3 -I -B exact_check.py | cmp - exact-output.json  (never -O).
A failed check prints its name to stderr and exits with status 1.
"""
from fractions import Fraction as F
from itertools import permutations, product
import json
import sys

checks = 0
families = {}
countercontrols = []


def require(condition, name, family="other"):
    global checks
    if not condition:
        print(f"CHECK FAILED: {name}", file=sys.stderr)
        sys.exit(1)
    checks += 1
    families[family] = families.get(family, 0) + 1


def reject(name, rejected):
    # A countercontrol runs a corrupted input through the predicate a positive check
    # uses; it passes only if that predicate rejects it.
    require(rejected, f"countercontrol accepted: {name}", "countercontrol")
    countercontrols.append(name)


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def push(p, f):
    out = [F(0)] * len(p)
    for i, j in enumerate(f):
        out[j] += p[i]
    return out


def project(p, cells=(0, 0, 1, 1)):
    out = [F(0)] * (max(cells) + 1)
    for i, c in enumerate(cells):
        out[c] += p[i]
    return out


def stochastic(m):
    return all(all(x >= 0 for x in row) and sum(row) == 1 for row in m)


def evolve(p, m):
    return [sum(p[i] * m[i][j] for i in range(len(p)))
            for j in range(len(p))]


def moment(p, degree, support=(-1, 0, 1)):
    return sum(weight * x ** degree for weight, x in zip(p, support))


def is_law(p):
    return sum(p) == 1 and min(p) >= 0


# 1. Total variation from a stationary reference is invariant under a bijection.
def tv_preserved(p, f, ref):
    return tv(push(p, f), ref) == tv(p, ref)


def cycle_constant_law(perm):
    # A stationary law, constant on each cycle; nonuniform unless perm is one cycle.
    weights = [None] * len(perm)
    for i in range(len(perm)):
        j = i
        while weights[j] is None:
            weights[j] = i + 1
            j = perm[j]
    return [F(w, sum(weights)) for w in weights]


for n in range(2, 5):
    u = [F(1, n)] * n
    for numerators in product(range(3), repeat=n):
        if not sum(numerators):
            continue
        p = [F(x, sum(numerators)) for x in numerators]
        for perm in permutations(range(n)):
            require(tv_preserved(p, perm, u), "permutation TV, uniform", "tv_uniform")
            pi = cycle_constant_law(perm)
            if len(set(pi)) > 1:
                require(push(pi, perm) == pi, "reference stationary", "tv_nonuniform")
                require(tv_preserved(p, perm, pi), "permutation TV, nonuniform",
                        "tv_nonuniform")

require(tv([F(1), F(0)], [F(1, 2)] * 2) > 0, "nonvacuous initial deviation")
stationary = [F(1, 2), F(0), F(1, 2)]
require(push(stationary, (0, 0, 2)) == stationary, "reference fixed by the nonbijection")
reject("nonbijective map", not tv_preserved([F(0), F(1, 2), F(1, 2)], (0, 0, 2),
                                            stationary))
reject("nonstationary reference", not tv_preserved([F(1), F(0)], (1, 0),
                                                   [F(3, 4), F(1, 4)]))


# 2. Four-cycle: constant fine deviation, recurrent projected deviation, no closure.
def series(f, cells, p, steps=5):
    k = max(cells) + 1
    fine, coarse = [], []
    for _ in range(steps):
        fine.append(tv(p, [F(1, len(p))] * len(p)))
        coarse.append(tv(project(p, cells), [F(1, k)] * k))
        p = push(p, f)
    return fine, coarse


def revives(coarse):
    return any(coarse[s] == 0 and coarse[t] > 0
               for s in range(len(coarse)) for t in range(s + 1, len(coarse)))


def closure_fails(f, cells):
    points = [[F(i == j) for j in range(len(f))] for i in range(len(f))]
    return any(project(a, cells) == project(b, cells)
               and project(push(a, f), cells) != project(push(b, f), cells)
               for a in points for b in points)


cycle, cells = (1, 2, 3, 0), (0, 0, 1, 1)
start = [F(1, 2), F(1, 2), F(0), F(0)]
fine, coarse = series(cycle, cells, start)
require(fine == [F(1, 2)] * 5, "constant fine deviation")
require(coarse == [F(1, 2), F(0), F(1, 2), F(0), F(1, 2)], "projected series")
require(revives(coarse), "projected revival")
require(closure_fails(cycle, cells), "no autonomous projected update")
reject("within-cell swaps do not revive", not revives(series((1, 0, 3, 2), cells, start)[1]))
reject("lumpable partition admits closure", not closure_fails(cycle, (0, 1, 0, 1)))

# 3. A symmetric perturbation changes the variance with zero odd moments.
q = [F(1, 4), F(1, 2), F(1, 4)]


def law(eps, q=q):
    return [q[0] + eps, q[1] - 2 * eps, q[2] + eps]


def variance_only(r, support=(-1, 0, 1)):
    return (is_law(r) and moment(r, 1, support) == 0 and moment(r, 3, support) == 0
            and moment(r, 2, support) != moment(q, 2))


eps = F(1, 16)
rho = law(eps)
require(variance_only(rho), "variance changed with zero odd moments")
require(moment(rho, 2) == F(5, 8), "variance value")
require(moment(rho, 2) / moment(q, 2) == F(5, 4), "response amplitude")
require(law(F(0)) == q and moment(q, 3) == 0, "zero perturbation null")
reject("zero perturbation", not variance_only(law(F(0))))
reject("asymmetric perturbation (odd moments)",
       not variance_only([q[0] + eps, q[1] - eps, q[2]]))
# On (-1, 0, 1) the mean and the third moment coincide, so each clause is exercised
# alone on a law supported on (-1, 0, 2).
reject("skewed zero-mean law (nonzero third moment)",
       not variance_only([F(1, 2), F(1, 4), F(1, 4)], (-1, 0, 2)))
reject("shifted law with zero third moment (nonzero mean)",
       not variance_only([F(4, 5), F(1, 10), F(1, 10)], (-1, 0, 2)))
reject("perturbation outside the law interval", not variance_only(law(F(1, 4) + F(1, 1000))))


# 4. Reset kernels: stochastic, reference-preserving, contracting.
def reset(retained):
    return [[retained * F(i == j) + (1 - retained) * q[j]
             for j in range(3)] for i in range(3)]


def contracts(p, m):
    return stochastic(m) and evolve(q, m) == q and tv(evolve(p, m), q) < tv(p, q)


for retained in (F(1, 2), F(1, 4), F(0)):
    m = reset(retained)
    require(contracts(rho, m), "reset contracts")
    expected = [q[i] + retained * (rho[i] - q[i]) for i in range(3)]
    require(evolve(rho, m) == expected, "reset eigenmode")
reject("identity kernel", not contracts(rho, reset(F(1))))
reject("nonstochastic kernel", not contracts(rho, [[F(1), F(1), F(0)]] * 3))

# 5. Exit rule, end rule and initial data, computed by evolving the laws.
# One step is Delta ln a = ln 2; with constant H, the mode k = 2^s k_i exits after s steps.
# Retained fraction 1/2 per step is lambda = 1; 1/4 per step is lambda = 2.
EXITS, END = (0, 1, 2, 3), 4


def run(p, retained, steps):
    for _ in range(steps):
        p = evolve(p, reset(retained))
        require(is_law(p), "evolved law is a probability law", "evolution")
    return p


def response(p):
    return moment(p, 2) / moment(q, 2) - 1


amplitude = 4 * eps  # xi - 1 at the onset
exit_l1 = [response(run(rho, F(1, 2), s)) for s in EXITS]
exit_l2 = [response(run(rho, F(1, 4), s)) for s in EXITS]
continued = [response(run(run(rho, F(1, 2), s), F(1, 2), END - s)) for s in EXITS]
initial = [law(F(2 ** s, 128)) for s in EXITS]  # xi - 1 = (k/k_i)/32 at the onset
variable_initial = [response(run(p, F(1, 2), s)) for p, s in zip(initial, EXITS)]
variable_initial_l2 = [response(run(p, F(1, 4), s)) for p, s in zip(initial, EXITS)]


def exit_formula(lam):
    return [amplitude / F(2 ** s) ** lam for s in EXITS]


def scale_independent(values):
    return len(set(values)) == 1


require(exit_l1 == exit_formula(1), "frozen exit, lambda = 1, matches (k_i/k)")
require(exit_l2 == exit_formula(2), "frozen exit, lambda = 2, matches (k_i/k)^2")
require(exit_l1 != exit_l2, "order-H rates do not fix the exponent")
require(continued == [amplitude / 2 ** END] * len(EXITS), "common end matches (a_i/a_end)")
require(scale_independent(continued), "common end cancels the exit trend")
require(scale_independent(variable_initial), "initial scale dependence cancels the trend")
reject("frozen exit is scale-independent", not scale_independent(exit_l1))
reject("unit exponent for the rate-2 history", exit_l2 != exit_formula(1))
reject("frozen-exit formula after common-end relaxation", continued != exit_formula(1))
reject("lambda = 1 initial data under the rate-2 history",
       not scale_independent(variable_initial_l2))

print(json.dumps({
    "controls": checks,
    "controls_by_family": families,
    "countercontrols_rejected": countercontrols,
    "fine_tv": [str(x) for x in fine],
    "projected_tv": [str(x) for x in coarse],
    "variance_ratio": str(moment(rho, 2) / moment(q, 2)),
    "third_moment": str(moment(rho, 3)),
    "exit_exponent_1": [str(x) for x in exit_l1],
    "exit_exponent_2": [str(x) for x in exit_l2],
    "common_end": [str(x) for x in continued],
    "scale_dependent_initial": [str(x) for x in variable_initial],
    "verdict": "DESIGN_CHECKS_PASS; no empirical or native OI verdict",
}, sort_keys=True, indent=2))
