#!/usr/bin/env python3
"""Exact finite controls for global_form_proof_v1.txt; standard library only.

Exit 0 means only the explicitly enumerated finite assertions held. The
general group proofs and physical scope are in the separate proof note.
No floating point, external package, imported candidate code or assert.
"""
import itertools
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


FIELDS = (
    ("Q", 1, 1, 1),
    ("uR", 1, 0, 4),
    ("dR", 1, 0, -2),
    ("L", 0, 1, -3),
    ("eR", 0, 0, -6),
    ("H", 0, 1, 3),
)


def center_phases(a, b, k, modulus, fields=FIELDS):
    # omega^a, (-1)^b and z=exp(2 pi i k/modulus).
    require(modulus % 6 == 0, "phase grid must include Z3 and Z2")
    return tuple((r3 * a * (modulus // 3) +
                  r2 * b * (modulus // 2) + q * k) % modulus
                 for _, r3, r2, q in fields)


def center_control(modulus):
    actual = {(a, b, k)
              for a in range(3) for b in range(2) for k in range(modulus)
              if all(p == 0 for p in center_phases(a, b, k, modulus))}
    expected = {(j % 3, j % 2, j * (modulus // 6)) for j in range(6)}
    require(actual == expected, "SM common central kernel differs from Z6")
    single_extra = FIELDS + (("vectorlike_q1", 0, 0, 1),
                             ("vectorlike_qminus1", 0, 0, -1))
    extra_kernel = {(a, b, k)
                    for a in range(3) for b in range(2) for k in range(modulus)
                    if all(p == 0 for p in
                           center_phases(a, b, k, modulus, single_extra))}
    require(extra_kernel == {(0, 0, 0)}, "extra q=+-1 singlets did not remove kernel")
    require(any(center_phases(1, 0, 0, modulus)), "independent color center survived test")
    require(any(center_phases(0, 1, 0, modulus)), "independent weak center survived test")
    require(any(center_phases(0, 0, modulus // 6, modulus)),
            "independent abelian sixth root survived test")
    return {"phase_modulus": modulus,
            "elements_checked": 6 * modulus,
            "common_kernel": [list(x) for x in sorted(actual)],
            "extra_vectorlike_q1_pair_kernel_order": len(extra_kernel),
            "independent_center_negative_controls": True}


def parity(permutation):
    return sum(permutation[i] > permutation[j]
               for i in range(len(permutation))
               for j in range(i + 1, len(permutation))) % 2


def identity(n):
    return (tuple(range(n)), (0,) * n)


def scalar(n, phase, modulus):
    return (tuple(range(n)), (phase % modulus,) * n)


def scale(matrix, phase, modulus):
    permutation, phases = matrix
    return (permutation, tuple((x + phase) % modulus for x in phases))


def mul(left, right, modulus):
    # e_j maps to root^phase_j e_permutation[j]. Composition left after right.
    p, a = left
    q, b = right
    return (tuple(p[q[j]] for j in range(len(p))),
            tuple((b[j] + a[q[j]]) % modulus for j in range(len(p))))


def det_phase(matrix, modulus):
    p, phases = matrix
    require(modulus % 2 == 0, "determinant parity needs an even grid")
    return (sum(phases) + parity(p) * (modulus // 2)) % modulus


def tensor(left, right, modulus):
    p, a = left
    q, b = right
    n = len(q)
    return (tuple(p[i] * n + q[j] for i in range(len(p)) for j in range(n)),
            tuple((a[i] + b[j]) % modulus
                  for i in range(len(p)) for j in range(n)))


def monomials(n, modulus, phase_choices=None, determinant_one=False):
    choices = range(modulus) if phase_choices is None else phase_choices
    for p in itertools.permutations(range(n)):
        for phases in itertools.product(choices, repeat=n):
            matrix = (p, phases)
            if not determinant_one or det_phase(matrix, modulus) == 0:
                yield matrix


def rho_blocks(A, B, z, modulus):
    return (scale(tensor(A, B, modulus), z, modulus),
            scale(A, 4 * z, modulus),
            scale(A, -2 * z, modulus),
            scale(B, -3 * z, modulus),
            scalar(1, -6 * z, modulus),
            scale(B, 3 * z, modulus))


def noncentral_sm_control():
    # A finite monomial subgroup containing the full relevant Z6, not just its center.
    modulus = 6
    color = tuple(monomials(3, modulus, determinant_one=True))
    weak = tuple(monomials(2, modulus, determinant_one=True))
    units = tuple(identity(n) for n in (6, 3, 3, 2, 1, 2))
    actual = set()
    checked = 0
    for A, B, z in itertools.product(color, weak, range(modulus)):
        checked += 1
        if rho_blocks(A, B, z, modulus) == units:
            actual.add((A, B, z))
    expected = {(scalar(3, 2 * k, modulus), scalar(2, 3 * k, modulus), k)
                for k in range(6)}
    require(actual == expected, "full finite monomial kernel has noncentral extras")
    # Verify multiplication/order of the expected generator directly.
    gA, gB, gz = scalar(3, 2, 6), scalar(2, 3, 6), 1
    A, B, z = identity(3), identity(2), 0
    powers = set()
    for _ in range(6):
        powers.add((A, B, z))
        A, B, z = mul(A, gA, 6), mul(B, gB, 6), (z + gz) % 6
    require(powers == expected and (A, B, z) == (identity(3), identity(2), 0),
            "kernel is not generated by the proposed order-six element")
    return {"phase_modulus": 6, "color_group_order": len(color),
            "weak_group_order": len(weak), "elements_checked": checked,
            "kernel_order": len(actual), "noncentral_kernel_exclusion": True,
            "six_powers_are_distinct_and_close": True}


def F(C, D, t, modulus):
    a, b = det_phase(C, modulus), det_phase(D, modulus)
    return (scale(C, -2 * t + a - b, modulus),
            scale(D, 3 * t - 2 * a + b, modulus))


def g0_mul(left, right, modulus):
    C, D, t = left
    E, J, u = right
    return (mul(C, E, modulus), mul(D, J, modulus), (t + u) % modulus)


def coupled_center_control(modulus):
    actual = set()
    for c, d, t in itertools.product(range(modulus), repeat=3):
        # Independent direct integer evaluation of the two output block phases.
        if ((-2 * t + 4 * c - 2 * d) % modulus == 0 and
                (3 * t - 6 * c + 3 * d) % modulus == 0):
            actual.add((c, d, t))
    expected = {(c, d, (2 * c - d) % modulus)
                for c in range(modulus) for d in range(modulus)}
    require(actual == expected, "correlated central kernel differs from K")
    require(all((c, c, c) in actual for c in range(modulus)),
            "common phase not killed")
    require({t for t in range(modulus) if (0, 0, t) in actual} == {0},
            "singlet circle is not retained faithfully")
    return {"phase_modulus": modulus, "elements_checked": modulus ** 3,
            "kernel_order": len(actual), "expected_order": modulus ** 2,
            "common_phase_redundant": True, "singlet_axis_kernel_order": 1}


def noncentral_F_control():
    modulus = 12
    color = tuple(monomials(3, modulus, (0, modulus // 2)))
    weak = tuple(monomials(2, modulus, (0, modulus // 2)))
    actual = set()
    image = set()
    elements = tuple(itertools.product(color, weak, range(modulus)))
    identity_pair = (identity(3), identity(2))
    # Generators of the signed monomial groups and the singlet-axis root.
    generators = [((1, 0, 2), (0, 0, 0)),
                  ((0, 2, 1), (0, 0, 0))]
    g0_generators = [(x, identity(2), 0) for x in generators]
    for j in range(3):
        phases = tuple(6 if k == j else 0 for k in range(3))
        g0_generators.append(((tuple(range(3)), phases), identity(2), 0))
    g0_generators.append((identity(3), ((1, 0), (0, 0)), 0))
    for j in range(2):
        phases = tuple(6 if k == j else 0 for k in range(2))
        g0_generators.append((identity(3), ((0, 1), phases), 0))
    g0_generators.append((identity(3), identity(2), 1))
    homomorphism_pairs = 0
    for element in elements:
        C, D, t = element
        E, J = F(C, D, t, modulus)
        require((det_phase(E, modulus) + det_phase(J, modulus)) % modulus == 0,
                "F output left S(U3xU2)")
        image.add((E, J))
        if (E, J) == identity_pair:
            actual.add(element)
        # Verify F(xg)=F(x)F(g) for every x and every finite-group generator.
        for generator in g0_generators:
            FC, FD = F(*generator, modulus)
            require(F(*g0_mul(element, generator, modulus), modulus) ==
                    (mul(E, FC, modulus), mul(J, FD, modulus)),
                    "finite F homomorphism control failed")
            homomorphism_pairs += 1
    expected = {(scalar(3, c, modulus), scalar(2, d, modulus), (2 * c - d) % modulus)
                for c in (0, 6) for d in (0, 6)}
    require(actual == expected, "noncentral finite F kernel differs from K intersection")
    require(len(image) * len(actual) == len(elements), "finite first isomorphism count failed")
    # Every encountered target has the explicitly exhibited root-free right section.
    for E, J in image:
        delta = det_phase(E, modulus)
        section = (E, J, delta)
        require(F(*section, modulus) == (E, J), "F right section failed")
    return {"phase_modulus": modulus, "elements_checked": len(elements),
            "homomorphism_generator_pairs": homomorphism_pairs,
            "kernel_order": len(actual), "image_order": len(image),
            "noncentral_kernel_exclusion": True, "right_section_checked": True}


def descent_control():
    checked = 0
    for r3, r2, q in itertools.product(range(3), range(2), range(-12, 13)):
        residue = 2 * r3 + 3 * r2 + q
        for order in (1, 2, 3, 6):
            # Generator of the order-d subgroup is g^(6/d).
            phase_numerator = residue * (6 // order)
            actual = phase_numerator % 6 == 0
            expected = residue % order == 0
            require(actual == expected, "general descent congruence failed")
            checked += 1
    # Every listed field descends to every allowed subgroup quotient.
    residues = {name: 2 * r3 + 3 * r2 + q for name, r3, r2, q in FIELDS}
    require(all(value % 6 == 0 for value in residues.values()), "SM row failed descent")
    return {"triples_checked": 3 * 2 * 25,
            "subgroup_checks": checked,
            "subgroup_orders": [1, 2, 3, 6], "SM_residues": residues}


def main():
    result = {
        "schema": "oi-gauge-global-finite-controls-v1",
        "status": "finite_controls_hold",
        "arithmetic": "exact integers modulo stated root-of-unity orders",
        "SM_center_controls": [center_control(n) for n in (6, 60, 360)],
        "SM_noncentral_monomial_control": noncentral_sm_control(),
        "coupled_center_controls": [coupled_center_control(n) for n in (6, 12, 30)],
        "coupled_noncentral_monomial_control": noncentral_F_control(),
        "descent_control": descent_control(),
        "scope": "Finite controls only; the continuous group proof and unproved physical selection are separate.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
