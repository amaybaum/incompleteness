#!/usr/bin/env python3
"""Exact bounded checks for the restricted SM-Theorem-3 converse.

Standard library only. This supports, but does not replace, the general proof.
Checks remain active under python -O; no floating point and no assert statements.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path

Matrix = dict[tuple[int, int], Q]


def matrix(rows: list[list[int | Q]]) -> Matrix:
    return {(i, j): Q(x) for i, row in enumerate(rows)
            for j, x in enumerate(row) if x}


def diagonal(xs: list[int | Q]) -> Matrix:
    return {(i, i): Q(x) for i, x in enumerate(xs) if x}


def add(*args: Matrix) -> Matrix:
    out: Matrix = {}
    for a in args:
        for k, v in a.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(c: int | Q, a: Matrix) -> Matrix:
    return {k: Q(c) * v for k, v in a.items() if c * v}


def mul(a: Matrix, b: Matrix) -> Matrix:
    brow: dict[int, list[tuple[int, Q]]] = {}
    for (i, j), v in b.items():
        brow.setdefault(i, []).append((j, v))
    out: Matrix = {}
    for (i, k), av in a.items():
        for j, bv in brow.get(k, []):
            out[i, j] = out.get((i, j), Q(0)) + av * bv
    return {k: v for k, v in out.items() if v}


def anti(a: Matrix, b: Matrix) -> Matrix:
    return add(mul(a, b), mul(b, a))


def require(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)


def onsite_case(d: Matrix, e: Matrix, c: Matrix, n: int) -> None:
    require(mul(e, e) == diagonal([1] * n), 'involution')
    require(not anti(d, e), 'baseline anticommutation')
    require(mul(c, e) == mul(e, c), 'perturbation commutation')
    observed = anti(add(d, c), e)
    require(observed == scale(2, mul(c, e)), 'operator identity')
    require((not observed) == (not c), 'operator converse')


def scalar_cases() -> int:
    e, identity = diagonal([1, -1]), diagonal([1, 1])
    count = 0
    for a, b, m, p in product((-1, 0, 1), repeat=4):
        d = matrix([[0, a], [b, 0]])
        c = add(scale(m, e), scale(p, identity))
        onsite_case(d, e, c, 2)
        require(anti(add(d, c), e) == add(scale(2*m, identity), scale(2*p, e)),
                'two-parameter identity')
        require((not anti(add(d, c), e)) == (m == 0 and p == 0),
                'two-parameter converse')
        count += 1
    for m, p in [(Q(1, 2), Q(-1, 3)), (Q(0), Q(0))]:
        d = matrix([[0, Q(1, 3)], [Q(-2, 5), 0]])
        c = add(scale(m, e), scale(p, identity))
        onsite_case(d, e, c, 2)
        require((not anti(add(d, c), e)) == (m == 0 and p == 0),
                'rational coefficient converse')
        count += 1
    return count


def commuting_block_cases() -> int:
    # An even-parity block can mix two components: C need not be scalar or diagonal.
    e = diagonal([1, 1, -1])
    d = matrix([[0, 0, 2], [0, 0, -3], [5, 7, 0]])
    count = 0
    for u, v, w, x, y in product((-1, 0, 1), repeat=5):
        c = matrix([[u, v, 0], [w, x, 0], [0, 0, y]])
        onsite_case(d, e, c, 3)
        count += 1
    return count


def lattice(axes: int, extent: int) -> tuple[Matrix, Matrix, Matrix, int]:
    sites = list(product(range(extent), repeat=axes))
    index = {x: i for i, x in enumerate(sites)}
    b: Matrix = {}
    second: Matrix = {}
    def bump(a: Matrix, i: int, j: int, v: int) -> None:
        a[i, j] = a.get((i, j), Q(0)) + v
    for i, x in enumerate(sites):
        for mu in range(axes):
            eta = (-1) ** sum(x[:mu])
            for direction in (-1, 1):
                y = list(x)
                y[mu] = (y[mu] + direction) % extent
                bump(b, i, index[tuple(y)], eta * direction)
                z = list(x)
                z[mu] = (z[mu] + 2 * direction) % extent
                bump(second, i, index[tuple(z)], 1)
            bump(second, i, i, -2)
    e = diagonal([(-1) ** sum(x) for x in sites])
    return ({k: v for k, v in b.items() if v}, e,
            {k: v for k, v in second.items() if v}, len(sites))


def lattice_cases() -> list[dict[str, int | str]]:
    records = []
    for axes in (1, 2, 3, 4):
        b, e, second, n = lattice(axes, 4)
        require(not anti(b, e), 'even-lattice chirality')
        require(all((i, i) not in b for i in range(n)), 'Dirac center-free')
        square = mul(b, b)
        require(square == second, 'independent second-difference construction')
        require(all(square.get((i, i), 0) == -2 * axes for i in range(n)),
                'squared operator nonzero center')
        records.append({'axes': axes, 'extent': 4, 'sites': n,
                        'diag_B_squared': -2 * axes, 'B_equals': '2D'})
    return records


def countercontrols() -> dict[str, bool]:
    out = {}
    e, identity = diagonal([1, -1]), diagonal([1, 1])
    x = matrix([[0, 1], [1, 0]])
    out['drop_C_commutes'] = bool(x) and not anti(x, e) and mul(x, e) != mul(e, x)
    out['drop_baseline_chirality'] = (bool(scale(-1, identity)) and
        not anti(add(identity, scale(-1, identity)), e) and bool(anti(identity, e)))
    out['drop_invertible_grading'] = bool(identity) and not anti(identity, {})
    two_i = anti(identity, identity)
    out['characteristic_two'] = bool(identity) and all(v.denominator == 1 and
                                                     v.numerator % 2 == 0
                                                     for v in two_i.values())
    out['single_parity_coefficient_cancellation'] = not add(identity, scale(-1, identity))
    # M=I and P=-epsilon are nonzero, commute with epsilon, but M epsilon + P=0.
    out['operator_coefficient_cancellation'] = (bool(identity) and bool(e) and
        not add(mul(identity, e), scale(-1, e)))
    for axes, extent in product((1, 2), (3, 5)):
        b, grading, _, _ = lattice(axes, extent)
        out[f'odd_periodic_boundary_d{axes}_L{extent}'] = bool(anti(b, grading))
    for name, ok in out.items():
        require(ok, 'countercontrol: ' + name)
    return out


def main() -> None:
    scalars = scalar_cases()
    blocks = commuting_block_cases()
    lattices = lattice_cases()
    controls = countercontrols()
    result = {
        'schema': 'sm-theorem3-restricted-converse-smoke-v1',
        'evidence_class': 'bounded exact rational computation; not a Lean certificate',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scalar_cases': scalars,
        'commuting_block_cases': blocks,
        'lattice_cases': lattices,
        'countercontrols': controls,
        'passed': all(controls.values()) and scalars == 83 and blocks == 243
                  and len(lattices) == 4,
    }
    require(bool(result['passed']), 'aggregate check')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
