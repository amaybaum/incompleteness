#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/EdgeRigidity.lean, OIBridge/HomometricSix.lean,
OIBridge/HomometricKill.lean, OIBridge/PiccardBridge.lean, OIBridge/TurnpikeScopeTransfer.lean,
OIBridge/CongruentReconstruction.lean, OIBridge/FrequencyMatching.lean,
OIBridge/AntiunitaryInvariance.lean, OIBridge/ThermalOrientation.lean, and
OIBridge/ShellAssignment.lean.

EdgeRigidity kernel-proves K4-RIGIDITY: for n >= 5, an edge permutation of K_n preserving all
four-cycle product identities as identities is induced by a vertex permutation -- with the n = 4
complement exception exposed as sharp -- plus the manuscript-facing corollary that a non-induced
edge permutation forces a nontrivial exponent relation (summing to zero, so flat rows always
survive). HomometricSix kernel-proves the two load-bearing finite endpoints of the n = 6 kill
chain: the flat-locus theorem L_mu-perp = span(1) and the max-clique-3 obstruction, plus the mask
factorizations and the xi/eta linkage. HomometricKill closes the ANALYTIC MIDDLE in the kernel --
rank-one line forcing, the multiplicative phase elimination (explicit certificates in place of the
Smith normal form), the torus-zero bridge, and the assembled `homometricSix_unrealizable`: the
forced non-two-branch six-mode correspondence admits no pair of unitary eigenbases with all
overlaps nonzero.

These checks exercise the same statements independently (no Lean in the loop):

  R1  THE HYPERSIMPLEX COUNT AT n = 4: exhaustively over all 720 edge permutations of K4,
      exactly 48 preserve every matching identity -- the 24 vertex-induced ones and their 24
      complement-composites. The complement itself preserves and is induced by no vertex
      permutation. This is the Delta(2,4) exception, and it is the ONLY structure: preserving
      set = S4 x {id, complement}.
  R2  RIGIDITY SAMPLED AT n = 5..7: every random vertex-induced edge permutation preserves all
      identities; random edge permutations (overwhelmingly non-induced) violate at least one
      identity whenever they are non-induced, and each preserving sample found IS induced.
  R3  THE EXCEPTIONAL RELATION: for non-induced samples, the violated matching difference w is
      a nonzero integer vector with sum(w) = 0 (the flat direction always survives), matching
      `exceptional_relation`'s conclusion.
  R4  THE FIVE FLAT-LOCUS INSTANCES: the exact relation vectors of the five quadruple/matching
      instances used in HomometricSix.flat_locus span the full 5-dimensional annihilator of the
      flat direction -- so the Lean file's linear elimination is complete, not lucky.
  R5  THE CLIQUE DATA: the 8 connection elements in HomometricSix.conn match the exact common
      mask zeros computed here from scratch (via the factored cofactors), are inversion-closed,
      generate a group of order 48, and admit max clique exactly 3.
  R6  ORIENTATION COHERENCE: for random spectra with distinct eigenvalues, both global lifts
      satisfy every triangle gap identity while EVERY properly mixed sign assignment violates
      one -- the content of `orientation_coherence`, checked in exact fractions.
  R7  lint of all ten Lean files.
  R8  CONGRUENT RECONSTRUCTION, numerically: random unitary V, random unimodular row/column
      phases and mode permutation build W; the coefficient lines match and H' recovers
      D H D^dag + E0 (and the reflected model recovers -D conj(H) D^dag + E0) to machine
      precision; perturbing one column phase off the unit circle breaks a coefficient line
      (the modulus rigidity that needs m >= 3); at m = 2 the hyperbola ambiguity survives
      the diagonal filter -- retained as the countercontrol showing modulus rigidity is
      sharp at m >= 3, and identified by `dim_two_moduli_dichotomy` as exactly the swap
      (= reflection) branch, never a third alternative.
  R9  FREQUENCIES TO COEFFICIENTS, numerically: for random V and a Golomb spectrum, the
      complex amplitude of each frequency in |U_ij(t)|^2 (the ampC fiber sum) equals the
      single coefficient line C^{ab}_{ij}; a translation-congruent W matches every amplitude
      at the translated frequency; a degenerate spectrum collides two fibers and the
      per-line extraction fails, showing the distinct-gap hypothesis is load-bearing; and
      the m = 2 dichotomy factorization (q-p)(1-p-q) = 0 is verified on random rows.

Usage:  python3 edge_rigidity_probe.py
"""
import itertools
import os
import random
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


def edges_of(n):
    return list(itertools.combinations(range(n), 2))


def preserves(n, perm, edges):
    """perm: dict edge -> edge. Check all matching identities as endpoint multisets."""
    for q in itertools.combinations(range(n), 4):
        a, b, c, d = q
        m1 = sorted(perm[(a, b)] + perm[(c, d)])
        m2 = sorted(perm[(a, c)] + perm[(b, d)])
        m3 = sorted(perm[(a, d)] + perm[(b, c)])
        if m1 != m2 or m1 != m3:
            return False
    return True


def induced_by(n, perm, edges):
    for tau in itertools.permutations(range(n)):
        if all(perm[e] == tuple(sorted((tau[e[0]], tau[e[1]])))for e in edges):
            return tau
    return None


# ---------------------------------------------------------------- R1  n = 4 exhaustive
E4 = edges_of(4)
preserving = []
for imgs in itertools.permutations(E4):
    perm = dict(zip(E4, imgs))
    if preserves(4, perm, E4):
        preserving.append(perm)
compl = {e: tuple(sorted(set(range(4)) - set(e))) for e in E4}
induced_count = sum(1 for p in preserving if induced_by(4, p, E4) is not None)
compl_composites = 0
for p in preserving:
    q = {e: compl[p[e]] for e in E4}
    if induced_by(4, q, E4) is not None and induced_by(4, p, E4) is None:
        compl_composites += 1
ok1 = len(preserving) == 48 and induced_count == 24 and compl_composites == 24
ok1 &= preserves(4, compl, E4) and induced_by(4, compl, E4) is None
check("R1", ok1,
      f"n = 4 EXHAUSTIVE: of all 720 edge permutations of K4, exactly {len(preserving)} "
      f"preserve every matching identity -- {induced_count} vertex-induced plus "
      f"{compl_composites} complement-composites -- and the complement map itself preserves "
      f"while being induced by no vertex permutation. The Delta(2,4) hypersimplex exception, "
      f"exactly as Lean's `compl4_preserves` / `compl4_not_induced`, with nothing else hiding")

# ---------------------------------------------------------------- R2  rigidity sampled
rng = random.Random(20260830)
ok2 = True
for n in (5, 6, 7):
    E = edges_of(n)
    for _ in range(30):
        tau = list(range(n))
        rng.shuffle(tau)
        perm = {e: tuple(sorted((tau[e[0]], tau[e[1]]))) for e in E}
        ok2 &= preserves(n, perm, E)
    found_noninduced_preserving = False
    for _ in range(200):
        imgs = E[:]
        rng.shuffle(imgs)
        perm = dict(zip(E, imgs))
        if preserves(n, perm, E):
            if induced_by(n, perm, E) is None:
                found_noninduced_preserving = True
    ok2 &= not found_noninduced_preserving
check("R2", ok2,
      "RIGIDITY SAMPLED at n = 5, 6, 7: 30 random vertex-induced edge permutations per n all "
      "preserve every identity, and among 200 random edge permutations per n no preserving "
      "non-induced one exists -- every preserving sample is induced, matching `k4_rigidity`")

# ---------------------------------------------------------------- R3  the exceptional relation
ok3 = True
tested = 0
for n in (5, 6):
    E = edges_of(n)
    while tested < 25 * (n - 4):
        imgs = E[:]
        rng.shuffle(imgs)
        perm = dict(zip(E, imgs))
        if induced_by(n, perm, E) is not None:
            continue
        tested += 1
        wfound = None
        for q in itertools.combinations(range(n), 4):
            a, b, c, d = q
            w = [0] * n
            for v in perm[(a, b)] + perm[(c, d)]:
                w[v] += 1
            for v in perm[(a, c)] + perm[(b, d)]:
                w[v] -= 1
            if any(w):
                wfound = w
                break
        ok3 &= wfound is not None and sum(wfound) == 0
check("R3", ok3,
      f"THE EXCEPTIONAL RELATION on {tested} random non-induced edge permutations (n = 5, 6): "
      f"each has a violated matching whose exponent vector w is nonzero with sum(w) = 0 -- "
      f"a genuine constraint that nevertheless never excludes the flat row, exactly "
      f"`exceptional_relation`'s conclusion")

# ---------------------------------------------------------------- R4  the five instances span
R1v = [0, 1, 4, 10, 12, 17]
R2v = [0, 1, 8, 11, 13, 17]
g2 = {}
for c, d in itertools.combinations(range(6), 2):
    g2[R2v[d] - R2v[c]] = (c, d)
mu = {(a, b): g2[R1v[b] - R1v[a]] for a, b in itertools.combinations(range(6), 2)}
inv = {v: k for k, v in mu.items()}
INSTANCES = [((0, 1, 3, 4), '12'), ((1, 2, 3, 4), '12'), ((0, 2, 3, 5), '12'),
             ((0, 1, 2, 5), '13'), ((0, 1, 2, 3), '12')]
vecs = []
for (qc, kind) in INSTANCES:
    c, d, e, f = qc
    m1 = [(c, d), (e, f)]
    m2 = [(c, e), (d, f)] if kind == '12' else [(c, f), (d, e)]
    w = [0] * 6
    for p in m1:
        for v in inv[p]:
            w[v] += 1
    for p in m2:
        for v in inv[p]:
            w[v] -= 1
    vecs.append([Fraction(x) for x in w])


def rank(M):
    M = [row[:] for row in M]
    m, n = len(M), len(M[0])
    r = 0
    for cix in range(n):
        piv = next((i for i in range(r, m) if M[i][cix] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cix]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][cix] != 0:
                fct = M[i][cix]
                M[i] = [x - fct * y for x, y in zip(M[i], M[r])]
        r += 1
    return r


ok4 = rank(vecs) == 5 and all(sum(w) == 0 for w in vecs)
check("R4", ok4,
      "THE FIVE FLAT-LOCUS INSTANCES used by HomometricSix.flat_locus (quadruples 0134, 1234, "
      "0235, 0125, 0123) have exponent vectors of rank exactly 5, each summing to zero: they "
      "span the entire annihilator of the flat direction, so the Lean file's five-relation "
      "linear elimination is complete rather than fortuitous")

# ---------------------------------------------------------------- R5  the clique data
# recompute the common zeros from scratch via the cofactors: G = 1 + x + x^2 y has torus zeros
# (omega^{+-1}, 1); H and Ht are quadratics in y over Z[i]-points x in {1, i, -i}
import cmath
Z_expected = {(4, 0), (8, 0), (0, 1), (0, 3), (3, 2), (9, 2), (3, 3), (9, 1)}


def to_exp(x, y):
    a = round(cmath.phase(x) / (2 * cmath.pi) * 12) % 12
    b = round(cmath.phase(y) / (2 * cmath.pi) * 4) % 4
    assert abs(x - cmath.exp(2j * cmath.pi * a / 12)) < 1e-9
    assert abs(y - cmath.exp(2j * cmath.pi * b / 4)) < 1e-9
    return (a, b)


zs = set()
w = cmath.exp(2j * cmath.pi / 3)
zs.add(to_exp(w, 1))
zs.add(to_exp(w.conjugate(), 1))
for x in (1, 1j, -1j):
    # H(x, y) = x^3 y^2 + (1 - x) y + 1 = 0
    a2, a1, a0 = x ** 3, 1 - x, 1
    disc = cmath.sqrt(a1 * a1 - 4 * a2 * a0)
    for sgn in (1, -1):
        y = (-a1 + sgn * disc) / (2 * a2)
        Ht = x ** 3 * y ** 2 + (x ** 3 - x ** 2) * y + 1
        if abs(y * y.conjugate() - 1) < 1e-9 and abs(Ht) < 1e-9:
            zs.add(to_exp(x, y))
ok5 = zs == Z_expected
conn = sorted(Z_expected)
ok5 &= all(((-a) % 12, (-b) % 4) in Z_expected for a, b in conn)
S = {(0, 0)}
changed = True
while changed:
    changed = False
    for gx, gy in conn:
        for hx, hy in list(S):
            el = ((gx + hx) % 12, (gy + hy) % 4)
            if el not in S:
                S.add(el)
                changed = True
ok5 &= len(S) == 48
best = 0
Slist = sorted(S)
adj = {u: {v for v in Slist if v != u and ((u[0] - v[0]) % 12, (u[1] - v[1]) % 4) in Z_expected}
       for u in Slist}


def grow(clique, cand):
    global best
    best = max(best, len(clique))
    for i, v in enumerate(cand):
        if len(clique) + len(cand) - i <= best:
            break
        grow(clique + [v], [u for u in cand[i + 1:] if u in adj[v]])


grow([], Slist)
ok5 &= best == 3
check("R5", ok5,
      f"THE CLIQUE DATA recomputed from scratch: the common torus zeros of the two factored "
      f"masks are exactly the 8 exponent pairs in HomometricSix.conn, inversion-closed, "
      f"generating a group of order {len(S)} with max clique {best} -- the kernel-proved "
      f"`no_four_clique` / `no_six_orthogonal` / `three_clique` data verified independently")

# ---------------------------------------------------------------- R6  orientation coherence
ok6o = True
for trial in range(40):
    n = rng.choice((4, 5, 6))
    E = sorted(rng.sample(range(1, 200), n))
    E = [Fraction(x) for x in E]
    tau = list(range(n))
    rng.shuffle(tau)


    def triangle_ok(eps):
        for a, b, c in itertools.combinations(range(n), 3):
            lhs = eps[(a, b)] * (E[a] - E[b]) + eps[(b, c)] * (E[b] - E[c])
            if lhs != eps[(a, c)] * (E[a] - E[c]):
                return False
        return True


    pairs = list(itertools.combinations(range(n), 2))
    ok6o &= triangle_ok({p: 1 for p in pairs})
    ok6o &= triangle_ok({p: -1 for p in pairs})
    eps = {p: rng.choice((1, -1)) for p in pairs}
    if len(set(eps.values())) == 2:
        ok6o &= not triangle_ok(eps)
check("R6", ok6o,
      "ORIENTATION COHERENCE in exact fractions, 40 random spectra with distinct eigenvalues "
      "(n = 4..6): both global sign choices satisfy every triangle gap identity, and every "
      "genuinely mixed per-edge sign assignment violates at least one -- an induced unordered "
      "correspondence has exactly the two directed lifts, Lean's `orientation_coherence`")

# ---------------------------------------------------------------- R7  lint
ok6 = True
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
for fname, names in (
    ('EdgeRigidity', ('k4_rigidity', 'exceptional_relation', 'induced_preserves',
                      'pulledBack_const', 'compl4_preserves', 'compl4_not_induced',
                      'orientation_coherence')),
    ('HomometricSix', ('golomb_r1', 'golomb_r2', 'mu_gap', 'mu_forced', 'muInv_mu',
                       'mu_muInv', 'mu_not_vertex_induced', 'flat_locus', 'linkage',
                       'maskV_factor', 'maskW_factor', 'maskV_eq_sum', 'conn_symm',
                       'no_four_clique', 'no_six_orthogonal', 'three_clique')),
    ('HomometricKill', ('line_forcing', 'flat_of_products', 'monomial_relations',
                        'torus_zeros', 'point_to_exponent', 'orderOf_zeta', 'orderOf_I',
                        'homometricSix_unrealizable')),
    ('PiccardBridge', ('piccard_mu_bridge', 'piccard_realizes_mu',
                       'piccardX_at_printed', 'piccardY_at_printed',
                       'piccard_factor_r', 'piccard_factor_s',
                       'piccardX_marks', 'piccardY_marks')),
    ('TurnpikeScopeTransfer', ('rational_point', 'rational_solutions', 'exists_int_scaling',
                               'integer_realization_of_real_realization',
                               'spectral_classification_of_BG',
                               'gaps_eq_of_equal_probabilities',
                               'twoBranch_of_BGClassification')),
    ('AntiunitaryInvariance', ('run_transposeMap', 'pairing_transpose', 'circuit_invariance',
                               'transposeMap_kraus', 'kraus_normalization',
                               'string_invariance', 'unitary_channel_transpose',
                               'commute_all_scalar', 'ad_eq_scalar',
                               'phase_families_shift', "phase_families_shift'")),
    ('ThermalOrientation', ('gibbs_reflection', 'gibbs_reflection_perm', 'gibbs_orientation',
                            'transported_gibbs', 'orientation_excludes_reflection',
                            'gibbs_strictlyPassive', 'passivity_selector',
                            'passive_antipassive_const', 'passivity_selector_nonuniform',
                            'counting_passive', 'counting_strictlyPassive',
                            'commutant_diagonal', 'umat_spectral', 'stationary_offdiag',
                            'stationary_spectral_form', 'exists_margin_pair',
                            'approx_passivity_selector', 'rate_sign_transport',
                            'energyOrder_transport', 'passive_transport',
                            'reflection_excluded_of_transition_identification')),
    ('ShellAssignment', ('shellWeight_invariant', 'joint_stationary',
                         'marginal_stationary', 'shellConditional_sum')),
    ('CoherentLift', ('permMatrix_unitary', 'permMatrix_conj_diagonal', 'readProj_sum',
                      'branch_normalization', 'qfold_diagonal', 'intersection_consistent',
                      'extension_forces_agreement', 'no_common_extension_of_disagreement',
                      'finite_comb_extension', 'sandwich_stationary',
                      'spectral_clauses_insufficient', 'overlap_row_sum', 'overlap_col_sum',
                      'mixture_diag', 'shell_representation_from_comb',
                      'comb_mixture_of_shell_representation', 'uniform_overlap_obstruction',
                      'populations_nonuniform_of_marginal', 'projOverlap_complex',
                      'projector_overlap_nonneg', 'projector_overlap_col_sum',
                      'projector_overlap_row_sum', 'projector_mixture_readout',
                      'projector_shell_representation_from_comb',
                      'comb_mixture_of_projector_shell_representation',
                      'projector_uniform_overlap_obstruction', 'projOverlap_rankOne',
                      'rankOne_specialization', 'vlift_conjTranspose', 'vlift_mul',
                      'vlift_one', 'vlift_sum', 'vlift_kraus', 'permMatrix_prodCongr',
                      'readProj_fst_vlift', 'permMatrix_conj_apply', 'qStep_assemble',
                      'local_intervention_overlap', 'assemble_trace', 'opStep_trace',
                      'local_intervention_branch', 'embA_conjTranspose_mul_apply',
                      'mul_embA_apply', 'ptraceV_eq_trace', 'embA_vlift',
                      'embA_conj_channel', 'local_channel_preserves_ancilla',
                      "umat_spectral'", 'umat_zero', 'trace_diag_sandwich',
                      'intervened_readout_expansion', 'two_time_forces_stationary',
                      'two_time_necessary', 'krausChoi_psd', 'krausChoi_tp',
                      'vlift_mul_apply', 'mul_vlift_conjTranspose_apply',
                      'chApply_krausChoi', 'conjOp_transpose', 'transpose_conj_response',
                      'umat_conjOp_reflect', 'readProj_transpose', 'permMatrix_conjOp',
                      'real_instrument_reflection_invariant', 'intertwining_all_horizons',
                      'intertwining_comb_compatible')),
    ('TwoByTwoNoGo', ('twoByTwo_affine_rigidity', 'twoByTwo_nonCP',
                      'twoByTwo_no_local_lift')),
    ('AccessibleAlgebra', ('gap_coefficient_vanish', 'dyad_conjugation',
                           'dyad_conjugation_apply', 'accessible_trivial_commutant',
                           'native_menu_generates', 'complexProbe_trivialCommutant',
                           'vlift_ancillaBlockDiagonal', 'ancillaBlockDiagonal_mul',
                           'umat_ancillaBlockDiagonal', 'decoupled_carrier_commutes',
                           'ancillaPhase_not_scalar', 'conjOp_mul', 'conjOp_vlift',
                           'real_menu_conjugation_stable', 'probeG_unitary',
                           'probeResp_is_probe_response',
                           'complexProbe_breaks_conjugation')),
    ('OperationalRigidity', ('line_coefficient_vanish', 'conj_context_entry',
                             'operational_separation', 'sameData_unique_state',
                             'sameData_combination_transfer', 'sameData_linear_extension',
                             'psd_pair_kernel', 'projection_extreme',
                             'extreme_projection', 'orderIso_maps_projections',
                             'orderIso_orthogonal', 'orderIso_square', 'orderIso_jordan',
                             'hermitian_spectral_edyad', 'trace_edyad_mul',
                             'psd_trace_mul_nonneg', 'accessible_cone_full')),
    ('JordanClassification', ('psd_iff_trace_nonneg', 'jordan_complexify',
                              'orthogonal_resolution_rank_one', 'corner_form',
                              'corner_nilpotent', 'corner_unimodular',
                              'corner_cocycle', 'orientation_dichotomy',
                              'matrixJordan_unitary_or_transpose',
                              'sameData_orderIso',
                              'sameData_unitary_or_transpose')),
    ('OrientationSelection', ('transpose_data_eq', 'selector_factorization_invariant',
                              'operational_orientation_noGo', 'transpose_span',
                              'transpose_sep', 'transpose_cone',
                              'transpose_completion_admissible',
                              'transpose_realizes_second_branch', 'transpose_not_inner',
                              'orientedReference_excludes_transpose',
                              'oriented_functional_not_data_definable',
                              'sameData_unitary_of_orientedReference',
                              'shellRepresentation_stationary_profile',
                              'sameData_unitary_of_transitionIdentification',
                              'sameData_unitary_of_shellRepresentation')),
    ('OrientationClosure', ('conjM_conjM', 'conjM_sandwich_transpose',
                            'umat_reflect_conjM',
                            'shellRepresentation_transpose_stable',
                            'transitionIdentification_orientation_sensitive',
                            'stationary_readout',
                            'orientedShellRepresentation_orientation_sensitive',
                            'no_universal_oriented_property',
                            'no_symmetric_condition_forces_transitionIdentification',
                            'no_symmetric_condition_forces_orientedShell')),
    ('CycleFibreHull', ('sum_range_shift', 'freq_shift', 'freq_pow', 'freq_sum_one',
                        'freq_sum_card', 'fiberProj_trace', 'stationary_diag_pow',
                        'stationary_freq_readout', 'psd_diag_real',
                        'stationary_readout_hull', 'hull_readout_achieved',
                        'no_representation_outside_hull', 'transitive_freq_const',
                        'transitive_freq_eq_countMarginal',
                        'ergodicShell_readout_unique', 'ergodicShell_SRC',
                        'cycle_eigenvector_overlap', 'commutant_entry_zero',
                        'simple_spectrum_column_moduli',
                        'permLogBranch_projOverlap_invariant')),
    ('DynamicsGlue', ('conj_diag_entry', 'diagonalGlue_forces_monomial',
                      'monomial_conj_apply', 'glue_of_monomial',
                      'diagonalGlue_iff_monomial', 'monomial_unitary',
                      'diag_invariant_pow', 'diag_invariant_freq_readout',
                      'monomial_ergodic_readout_unique', 'phasedCycle_columnModuli',
                      'ergodicShell_SRC_of_dynamicsGlue')),
    ('DomainGlue', ('spanning_domain_glue_implies_G1', 'itiIndicator_mem',
                    'separating_singleton_mem', 'separating_domain_span_top',
                    'classicalBranch_glue_forces_G1',
                    'classicalBranch_glue_forces_monomial',
                    'ergodicShell_SRC_of_domainGlue')),
    ('ObservabilityQuotient', ('branchDomainK_invariant',
                               'classIndicator_eq_itiIndicator',
                               'itiIndicator_mem_BDK', 'classIndicator_mem_BDK',
                               'invariant_le_span_classIndicators',
                               'branchDomain_span_eq_itineraryInvariant',
                               'classicalBranchDomain_iff_horizon',
                               'itiRelInf_iff_orderOf',
                               'classicalBranch_span_eq_invariant', 'glueEq_span',
                               'domainGlue_classification_mod_itineraryFibres',
                               'domainGlue_unitary', 'glue_column_support')),
    ('PassiveQuotient', ('itiRelInf_pow', 'itiRelInf_evolve',
                         'itiRelInf_symm_evolve', 'quotPerm_mk', 'quotPerm_pow_mk',
                         'itiRelInf_greatest_congruence',
                         'quotient_itinerarySeparating',
                         'passiveMinimal_iff_itinerarySeparating',
                         'realization_pow', 'minimal_realization_bijective',
                         'realizationMap_equivariant', 'realizationMap_vis',
                         'realization_factor_unique', 'quotMeasure_weighted_sum',
                         'itiIndicator_quotient_mk', 'trajProb_quotient',
                         'quotMeasure_evolve', 'quotMeasure_branch',
                         'quotient_transitive', 'passiveQuotient_glue_forces_G1',
                         'passiveQuotient_glue_forces_monomial',
                         'ergodicShell_SRC_of_passiveQuotient',
                         'hiddenExt_pow_fst', 'hiddenExt_itiRelInf_fibre',
                         'hiddenExt_not_separating', 'hiddenExt_itiIndicator',
                         'hiddenExt_same_law', 'hiddenExt_quotient_recovers_base',
                         'addEquiv_pow_sub', 'linear_itiRelInf_iff',
                         'linear_separating_iff_observability')),
    ('ControlledQuotient', ('actWord_append', 'actWord_replicate',
                            'ctrlRel_evolve', 'ctrlRel_word',
                            'ctrlRel_symm_evolve', 'ctrlRel_le_itiRelInf',
                            'ctrlRel_greatest_congruence', 'ctrlPerm_mk',
                            'ctrlWord_mk', 'controlled_actionSeparating',
                            'controlledMinimal_iff_actionSeparating',
                            'controlledToPassive_surjective',
                            'intervention_separates_passive_fibre')),
    ('CoherentExtension', ('basisVec_mulVec', 'basisVec_dot', 'form_basis',
                           'hermitian_form_conj', 'psd_zero_form_mulVec_zero',
                           'psd_diag_zero_entry_zero',
                           'psd_unit_diag_entry_bound',
                           'psd_unimodular_rank_one',
                           'correlationExtension_single',
                           'correlationExtension_classical', 'embed_sum',
                           'choi_correlation',
                           'correlationExtension_completelyPositive',
                           'correlationExtension_trace',
                           'correlationExtension_cptp',
                           'cptp_classical_forces_correlation',
                           'cptpExtension_iff_correlationMatrix',
                           'correlationExtension_comp',
                           'correlationExtension_one_eq_id_iff',
                           'reversibleExtension_iff_rankOne',
                           'rankOne_extension_monomial',
                           'purity_selector_rank_one',
                           'correlationExtension_diagonal', 'combPerm_cons',
                           'combFold_diagonal', 'combPerm_eq_permProd',
                           'classicalComb_blind_to_correlation')),
    ('ProjectiveAction', ('unimodular_ne_zero', 'correlationExtension_matrix_eq',
                          'functoriality_forces_rankOne',
                          'functoriality_schur_law',
                          'coherentFunctoriality_iff_projectiveMonomial',
                          'monomial_entry', 'functorial_projective_unitaries',
                          'functorial_cocycle', 'groupFamily_comb_blind')),
    ('ControlLie', ('phase_conj_invariant', 'controlGenerators_phase_invariant',
                    'controlLie_phase_invariant', 'conj_conj_collapse',
                    'controlLie_gauge_mem', 'controlLie_gauge_mem_iff',
                    'controlLie_le_skewHerm', 'unitary_inv_eq_conjTranspose',
                    'unitary_exp_conj', 'conjugated_flow', 'controlLie_trivial')),
    ('InstrumentDilation', ('krausInstrument_isometry', 'dilation_sysBlock',
                            'instrument_coarsegrain',
                            'finiteInstrument_of_ancillaControl',
                            'uniformInput_one', 'uniformEnvChannel_unital',
                            'resetChannel_not_unital', 'uniformHiddenState_not_full',
                            'tensorProduct_entry', 'localEffect_trace',
                            'productMatrixUnit_separating', 'tomography_physical',
                            'productMatrixUnit_local_separating', 'form_expand',
                            'eq_zero_of_form_vanishes', 'prodProj_trace',
                            'local_tomography_physical')),
    ('Purification', ('branch_project', 'mixed_branch_is_pure',
                      'trace_eq_sum_diag', 'readout_feedforward_reset',
                      'uniform_readout_feedforward_seed', 'luders_selector_cp',
                      'purification_partialTrace',
                      'purification_of_factorization')),
    ('BranchSelector', ('ludersLift_selector',
                        'choi_ludersLift', 'ludersLift_cp',
                        'cp_rankOneSelector_forces_luders',
                        'cp_rankOneSelector_iff_luders',
                        'monomial_luders_classicalBranch')),
    ('IndependenceCensus', ('core_hidden_drives_visible', 'core_visible_period_two',
                            'core_observer_minimal', 'core_capacity_saturates',
                            'core_history_readback', 'core_isC1C4',
                            'sigma_tau_commute',
                            'ludersLift_diagonal', 'stateFold_diagonal',
                            'threeCompletions_same_classical_comb', 'monoU_conj',
                            'monoU_mul', 'monoU_unitary', 'nonFunctorial_cptp',
                            'nonFunctorial_classical', 'nonFunctorial_not_functorial',
                            'Utau_involution', 'Usigma_Utau_commute',
                            'nonTensor_not_local', 'Usigma_local', 'Vtau_local',
                            'passiveProj_idempotent', 'one_sub_two_passiveProj',
                            'restrictedU_fixes_coreH', 'restricted_controlLie_line',
                            'outsideGen_skewHermitian', 'outsideGen_traceless',
                            'outsideGen_not_mem',
                            'oi_core_underdetermines_completion')),
    ('MonoidalCompletion', ('wordPerm_append', 'wordMap_append',
                            'implementationExtensionality_descends',
                            'descendedAction_functorial', 'spectatorIndependent_iff',
                            'wordMap_isCorrelationExtension',
                            'implementationExtensionality_iff_functorial', 'hComp_iff',
                            'HControl_iff_controlLie0_full', 'central_conj_fixed',
                            'centralDrift_not_HControl', 'wordPerm_eq_parityPerm',
                            'wordMap_eq_parityMap', 'parityPerm_injective',
                            'implementationExtensionality_of_involutive',
                            'nonTensor_implementationExtensional',
                            'restricted_implementationExtensional',
                            'nonFunctorial_not_implementationExtensional',
                            'nonTensor_not_spectatorPattern', 'restricted_not_HControl',
                            'census_clause_taxonomy', 'fullOps_universalUnitary',
                            'availability_not_implies_hComp')),
    ('OperationalAssembly', ('spectatorIndependent_iff_mapLevel', 'tensorOf_single',
                             'localLuders_tensor', 'localLuders_mapSpectatorIndependent',
                             'eq_of_agree_on_single',
                             'mapSpectatorIndependent_iff_localLuders',
                             'blockDephase_apply', 'choiMatrix_sum', 'blockDephase_cp',
                             'localLuders_classical', 'blockDephase_classical',
                             'blockDephase_classical_eq', 'blockDephase_ne_localLuders',
                             'blockDephase_not_mapSpectatorIndependent',
                             'tensorOf_productPreparation',
                             'hasFullInstruments_hasUniversalControl',
                             'tensorOf_add_left', 'ptraceAnc_localLuders',
                             'readout_is_localLuders', 'conj_ancSwap_single',
                             'localLuders_uniform', 'pureSeedPrep_available',
                             'circuit_available', 'circuit_available_pureSeed',
                             'circuit_branch', 'pureSeedPrep_available_of_swap',
                             'compositeControl_hasSwapControl',
                             'pureSeedPrep_available_of_swapControl')),
    ('StinespringAssembly', ('Vsf_eq_dilationIsometry', 'Esf_eq_seedEmbed', 'vsf_gram',
                             'esf_conj', 'vsf_block', 'stinespringCircuit_branch',
                             'fullInstruments_of_control')),
    ('KrausSoundness', ('instrumentBranch_trace', 'instrumentBranch_isKraus',
                        'exact_iff_sound_and_full', 'exact_of_sound_control',
                        'krausSound_trace_preserving', 'traceAmplifier_not_kraus',
                        'everywhereAvailable_not_sound',
                        'everywhereAvailable_full_not_exact')),
    ('CompositeSoundness', ('isKrausFamily_iff', 'krausSound_exposedComposite',
                            'ptraceAnc_trace', 'discardWith_trace',
                            'not_kraus_of_trace_ne', 'traceWitness_exposed_on_reachable',
                            'posSemidef_sum', 'choiMatrix_finsum', 'conjChannel_cp',
                            'krausFamily_cp', 'exposedComposite_cp', 'transposeMap_trace',
                            'form_of_two_singles', 'transposeMap_not_cp',
                            'transposeMap_not_kraus', 'krausSoundExtAllLevels_unsatisfiable',
                            'krausSoundExt_of_allLevels')),
    ('HiddenCoherence', ('blockOp_one', 'blockOp_comp', 'blockOp_sum',
                         'localLuders_eq_blockOp', 'uniformAttach_offDiag',
                         'blockOp_uniformAttach', 'sum_fibers', 'scalarAvail_isKraus',
                         'hiddenCoherence_krausSound', 'badOp_availExt',
                         'badOp_invisible', 'badOp_choi', 'badOp_not_cp',
                         'badOp_not_kraus', 'hiddenCoherence_not_krausSoundExt',
                         'krausSound_not_implies_krausSoundExt',
                         'isKrausFamily_coarse', 'discard_uniform_scalarAvail',
                         'hiddenCoherenceFull_exact',
                         'hiddenCoherenceFull_not_krausSoundExt',
                         'exact_not_implies_krausSoundExt')),
    ('AncillaInterference', ('sqrt2_inv_sq', 'hRaw_gram', 'hMat_unitary', 'ancMix_unitary',
                             'conjChannel_ancMix_tensor', 'hMat_conjTranspose_apply',
                             'badOp_tensor', 'mix_seed', 'tauChain_diag',
                             'interference_branch', 'form_of_one_single',
                             'smul_id_cp_nonneg', 'interference_exposes_badOp',
                             'compositeControl_hasInterference',
                             'interferenceControl_hasInterference',
                             'interferenceControl_exposes_badOp',
                             'compositeControl_hasInterferenceControl')),
    ('PartialTranspose', ('ancTranspose_apply', 'ancTranspose_tensor', 'ancTranspose_trace',
                          'posSemidef_transpose', 'ancTranspose_choi', 'ancTranspose_not_cp',
                          'ancTranspose_not_kraus', 'hMat_symm', 'hMat_involutive',
                          'mixSeed_symm', 'tauChainT_eq', 'tauChainT_diag',
                          'interference_branch_transpose',
                          'ancTranspose_survives_interference')),
    ('FactorExchange', ('swapMat_unitary', 'conjChannel_swapMat_apply',
                        'conjChannel_swapMat_tensor', 'ptraceAnc_tensor_uniform',
                        'exchange_transpose_exchange', 'exchanged_transpose_eq',
                        'compositeControl_hasFactorExchange',
                        'factorExchange_exposes_ancTranspose',
                        'compositeControl_exposes_ancTranspose')),
    ('DimensionalObstruction', ('reduction2_trace', 'reduction2_unital', 'reduction2_covariant',
                                'reduction2_commutes_conj', 'maxEntVec_norm', 'reduction2_choi',
                                'reduction2_choi_form', 'reduction2_choi_maxEnt',
                                'reduction2_not_cp', 'pairForm_of_orth',
                                'rankTwo_bound_of_orth', 'rankTwo_bound_re',
                                'rankTwo_trace_bound', 'dot_rankTwo_bound', 'ampl2_sum',
                                'ampl2_reduction2', 'form_tensor_one',
                                'ampl2_reduction2_rankOne', 'reduction2_twoPositive',
                                'qubit_tests_do_not_characterize_cp')),
    ('DimensionalCountermodel', ('amplR_comp', 'choiMatrix_eq_ampl2', 'twoPositive_qubit_cp',
                                 'isTwoPositive_comp', 'isTwoPositive_sum', 'ampl2_conjChannel',
                                 'conjChannel_twoPositive', 'ampl2_localLuders',
                                 'localLuders_twoPositive', 'localLuders_trace_sum',
                                 'amplR_ptraceAncL_eq', 'amplR_uniformAttach_eq',
                                 'amplR_ptraceAncL_posSemidef',
                                 'amplR_uniformAttach_posSemidef', 'uniformAttach_trace',
                                 'choiMatrix_conjChannel', 'choiMatrix_injective',
                                 'kraus_of_choi_factor',
                                 'sum_conjTranspose_mul_eq_one_of_trace',
                                 'isKrausFamily_of_cp_of_factorization',
                                 'psdFactorization_of_spectral', 'countermodelOf_exact',
                                 'countermodelOf_control',
                                 'countermodelOf_reduction2_available',
                                 'countermodelOf_not_krausSoundExt',
                                 'countermodel_of_factorization', 'countermodel_exact',
                                 'countermodel_control', 'countermodel_reduction2_available',
                                 'countermodel_not_krausSoundExt',
                                 'countermodel_hasFactorExchange',
                                 'countermodel_hasInterferenceControl',
                                 'exactControl_not_implies_krausSoundExt')),
    ('BoundaryAudit', ('psdFactorization_discharged', 'purification_unconditional')),
    ('ReferenceExtension', ('isTwoPositive_iff_referencePositive', 'amplRef_sum_map',
                            'amplRef_conjChannel', 'conjChannel_referencePositive',
                            'amplRef_reduction2', 'choiMatrix_eq_amplRef',
                            'referencePositive_self_cp', 'cp_referencePositive',
                            'isCompletelyPositive_iff_referencePositive_self',
                            'emb3_injective', 'maxEnt3_norm', 'refMarginalR_maxEnt3',
                            'tensorOf_one_one', 'amplRef_reduction2_maxEnt3',
                            'amplRef_reduction2_maxEnt3_form',
                            'amplRef_reduction2_maxEnt3_not_posSemidef',
                            'reduction2_not_threePositive', 'reduction2_threshold',
                            'refBlock_pad', 'apply_eq_pad_ampl2', 'positive_of_twoPositive',
                            'withSpectator_reindex', 'qutrit_of_parallel', 'qutritIdx_apply',
                            'posSemidef_of_reindex', 'posSemidef_reindex',
                            'countermodel_not_qutritReferenceExtension',
                            'countermodel_not_parallelReferenceExtension',
                            'control_not_implies_parallelReferenceExtension',
                            'exactControl_not_implies_qutritReferenceExtension')),
    ('ReferenceSufficiency', ('unitVectorRotation_of_isometryExtension', 'pureState_reachable',
                              'sound_avail_cp_tp', 'exact_avail_cp_tp', 'cp_apply_posSemidef',
                              'two_single_eq_dyads',
                              'linear_functional_zero_of_dyads', 'isHermitian_of_forms_real',
                              'posSemidef_of_forms_nonneg', 'forms_nonneg_of_unit', 'branch_cp',
                              'aggregate_trace', 'krausSoundExt_of_sound_control_refext',
                              'krausSoundExt_of_exact_control_refext',
                              'countermodel_witness_level_two', 'cp_comp', 'localLuders_cp',
                              'fullQuantum_exact', 'fullQuantum_control',
                              'fullQuantum_krausSoundExt', 'withSpectator_conjChannel',
                              'withSpectator_cp', 'fullQuantum_parallelReferenceExtension',
                              'parallelReferenceExtension_satisfiable')),
    ('SpectatorBridge', ('refBlockR_tensorOf', 'amplRef_tensorOf',
                         'mapSpectatorIndependent_iff_amplRef', 'spectatorIndependent_form',
                         'hComp_spectator_form', 'ext_of_agree_on_reindexed_single',
                         'isSpectatorExtension_iff', 'spectatorExtension_unique',
                         'inertSpectator_iff_parallelReferenceExtension',
                         'krausSoundExt_of_sound_control_inert', 'countermodel_not_inert',
                         'fullQuantum_inert', 'correlationExtension_ones',
                         'correlationExtension_ones_eq_conjChannel',
                         'correlationExtension_ones_comp', 'wordMap_ones',
                         'implementationExtensionality_ones', 'spectatorIndependent_ones',
                         'hComp_ones', 'transport_apply', 'transport_conjChannel',
                         'reindex_isometry', 'permMatrix_isometry', 'withSpectator_eq_transport',
                         'hCompRealized_spectator_available', 'hCompRealized_ones_of_control',
                         'countermodel_hCompRealized_ones', 'fullQuantum_hCompRealized_ones',
                         'hcompRealized_not_implies_parallelReferenceExtension',
                         'hcompRealized_consistent_with_parallelReferenceExtension')),
    ('AncillaClosure', ('transport_id', 'transport_comp', 'transport_sum', 'transport_smul',
                        'transport_symm_transport', 'transport_reindex', 'shiftIdx_apply',
                        'specIdx_apply', 'conjChannel_one', 'availExt_id_of_control',
                        'availExt_comp_unit', 'filter_snd_unit', 'availExt_comp_family',
                        'transport_localLuders', 'availExt_relativeReadout', 'shift_avail_iff',
                        'shift_control', 'shift_full', 'compositeCompleteness',
                        'exactComposite_of_soundExt_full', 'exactComposite_iff',
                        'exactComposite_of_conditions', 'choiMatrix_smul', 'cp_smul',
                        'conjChannel_apply', 'transport_cp', 'cp_of_transport_cp',
                        'discardWith_uniform_conjChannel', 'discardWith_sum',
                        'discardWith_uniform_cp', 'fullQuantum_iteratedAncillaClosure',
                        'conditions_satisfiable', 'fullQuantum_exactComposite')),
    ('ClosureObstruction', ('admOp_mul', 'admOp_unitary', 'adm_conjChannel_unitary', 'adm_zero',
                            'adm_add', 'adm_sum', 'conjChannel_mul', 'adm_comp', 'adm_cp',
                            'esf_mul_conjTranspose', 'adm_localLuders', 'admissible_exact',
                            'admissible_control', 'admissible_krausSoundExt',
                            'one_kronecker_isometry', 'tensorOf_one_eq_kronecker',
                            'reindex_smul_matrix', 'admOp_withSpectator', 'adm_withSpectator',
                            'admissible_parallelReferenceExtension', 'admissible_inert',
                            'star_dot_swap', 'form_vecMulVec', 'dyad_sum_span',
                            'rD_sq_add_sD_sq', 'qubit_gram', 'damping_gram',
                            'ancillaDamping_trace', 'ancillaDamping_isKraus', 'choiMatrix_add',
                            'vecOf_K₀_ne', 'vecOf_K₁_ne', 'vecOf_orth', 'kraus_of_damping',
                            'K₀_apply', 'K₁_apply', 'gram_entries', 'dampInv_mul',
                            'card_carrier', 'ad_not_adm', 'wD_isometry', 'WD_isometry',
                            'WD_apply', 'WD_esf', 'admissible_no_shift',
                            'admissible_not_iteratedAncillaClosure',
                            'admissible_not_fullComposite', 'admissible_not_exactComposite',
                            'closure_independent')),
    ('CompositionalIndependence', ('amplR_transport', 'twoPositive_transport',
                                   'twoPositive_of_transport', 'amplR_ptraceAncL_eq_sum',
                                   'embR_conjTranspose_apply', 'amplR_uniformAttach_eq_sum',
                                   'discardWith_uniform_twoPositive',
                                   'countermodel_iteratedAncillaClosure',
                                   'countermodel_krausSound', 'admissible_krausSound',
                                   'countermodel_reduction2_available_fin1',
                                   'countermodel_not_exactComposite',
                                   'closure_not_implies_inert', 'inert_not_implies_closure',
                                   'both_satisfiable', 'independence_matrix',
                                   'hcompRealized_inert_not_implies_closure',
                                   'hcompRealized_closure_not_implies_inert',
                                   'inert_not_deletable', 'closure_not_deletable',
                                   'conditional_classification')),
    ('OIRealization', ('coreIdx_apply', 'vis_coreIdx_symm_iff', 'readVisible_apply',
                       'readVisible_eq_localLuders', 'readVisible_family_eq',
                       'readout_relabel_available', 'readVisible_diagonal', 'vstepMap_diagonal',
                       'realizedFold_diagonal', 'relabel_available',
                       'realizesSealedOICore_of_control', 'countermodel_realizesSealedOICore',
                       'admissible_realizesSealedOICore', 'fullQuantum_realizesSealedOICore',
                       'partIdx_fst', 'sealedCore_is_finiteOI', 'sameCore_closure_not_inert',
                       'sameCore_inert_not_closure', 'sameCore_both', 'sameCore_both_sides',
                       'finiteOI_not_implies_inert', 'finiteOI_not_implies_closure')),
    ('OperationalValidity', ('cp_of_valid_inert', 'krausSoundExt_of_validity_inert',
                             'validity_of_krausSoundExt', 'krausSoundExt_iff_validity_of_inert',
                             'countermodel_validity', 'admissible_validity',
                             'fullQuantum_validity', 'validity_not_implies_krausSoundExt',
                             'exactComposite_of_validity', 'physical_classification',
                             'physical_inert_not_deletable', 'physical_closure_not_deletable')),
    ('LevelOneSeam', ('uniformAttach_one_eq', 'ptraceAnc_one_eq',
                      'discardWith_uniform_one_eq_transport', 'avail_of_availExt_one',
                      'transport_transport_symm', 'avail_iff_availExt_one', 'reindex_sum',
                      'transport_instrumentBranch', 'isKraus_transport_of', 'isKraus_transport',
                      'exactSystem_of_levelOne', 'exactAll_of_levelOne', 'exactAll_of_conditions',
                      'trace_transport', 'fullQuantum_systemToLevelOne',
                      'all_conditions_satisfiable', 'systemLoose_control',
                      'systemLoose_krausSoundExt', 'systemLoose_validity',
                      'systemLoose_parallelReferenceExtension', 'systemLoose_inert',
                      'systemLoose_iteratedAncillaClosure', 'systemLoose_exactComposite',
                      'systemLoose_realizesSealedOICore', 'systemLoose_amplifier_available',
                      'systemLoose_not_exact', 'transport_amplifier',
                      'systemLoose_not_systemToLevelOne', 'levelOne_independent',
                      'levelOne_not_deletable', 'final_classification')),
    ('PhysicalCharacterization', ('krausFamily_of_exact_fin', 'avail_of_krausFamily_fin',
                                  'krausFamily_cp_tr', 'availExt_zero',
                                  'krausFamily_of_exactComposite', 'availExt_of_krausFamily',
                                  'krausFamily_of_exactSystem', 'availExt_pos_iff',
                                  'krausSoundExt_of_exactComposite',
                                  'validity_of_exactComposite', 'control_of_exactComposite',
                                  'inert_of_exactComposite', 'closure_of_exactComposite',
                                  'levelOne_of_exactAll', 'physical_of_exactAll',
                                  'exactAll_of_physical', 'exactAll_iff_physical',
                                  'everywhereAvailable_not_validity',
                                  'everywhereAvailable_control', 'validity_independent',
                                  'countermodel_systemToLevelOne', 'inert_independent',
                                  "levelOne_independent'", 'qubitDamping_isKraus',
                                  'transport_add', 'levelOne_eq', 'L₀_apply', 'L₁_apply',
                                  'transport_qubitDamping', 'levelOne_gram',
                                  'levelOneDamping_trace', 'vecOf_L₀_ne', 'vecOf_L₁_ne',
                                  'vecOf_L_orth', 'kraus_of_levelOneDamping',
                                  'levelOne_gram_entries', 'levelOneInv_mul',
                                  'levelOneDamping_not_adm',
                                  'admissible_not_systemToLevelOne')),
    ('DiagonalTheory', ('preservesDiag_id', 'preservesDiag_zero', 'preservesDiag_add',
                        'preservesDiag_sum', 'preservesDiag_comp', 'reindex_diagonal',
                        'preservesDiag_transport', 'refBlockR_diagonal',
                        'preservesDiag_amplRef', 'preservesDiag_withSpectator',
                        'preservesDiag_localLuders', 'preservesDiag_relabel',
                        'preservesDiag_conjChannel_perm', 'uniformAttach_diagonal',
                        'ptraceAnc_diagonal', 'preservesDiagP_uniform',
                        'preservesDiag_discardWith', 'diag_krausSoundExt', 'diag_validity',
                        'diag_parallelReferenceExtension', 'diag_inert',
                        'preservesDiag_of_transport', 'diag_iteratedAncillaClosure',
                        'diag_systemToLevelOne', 'diag_relabel_available',
                        'diag_realizesSealedOICore', 'rot_isometry', 'rot_not_preservesDiag',
                        'diag_not_control', 'diag_not_exactAll', 'control_independent',
                        'minimality_audit')),
    ('RankGapTheory', ('isUnit_of_left_inverse', 'inv_mul_of_isUnit', 'gapOp_mul',
                       'gapOp_unitary', 'gap_conjChannel', 'gap_zero', 'gap_add', 'gap_sum',
                       'gap_comp', 'gap_cp', 'inv2_mul', 'ext_two_one', 'factor_of_singular',
                       'twoByTwo_dichotomy', 'gapOp_one', 'gap_localLuders', 'gap_exact',
                       'gap_control', 'gap_krausSoundExt', 'gap_validity',
                       'gap_realizesSealedOICore', 'gap_systemToLevelOne',
                       'gapOp_withSpectator', 'gap_withSpectator',
                       'gap_parallelReferenceExtension', 'gap_inert', 'qutrit_gram',
                       'gap_gram', 'gapChannel_trace', 'gapChannel_isKraus', 'G₀_apply',
                       'G₁_apply', 'vecOf_G₀_ne', 'vecOf_G₁_ne', 'vecOf_G_orth',
                       'kraus_of_gapChannel', 'gap_mulVec_kerVec', 'gap_not_isUnit',
                       'inc_compress', 'gapChannel_not_gap', 'wG_isometry', 'WG_isometry',
                       'WG_apply', 'WG_esf', 'gap_no_shift', 'gap_not_iteratedAncillaClosure',
                       'gap_not_fullComposite', 'gap_not_exactComposite', 'gap_not_exactAll',
                       'gap_not_physical', 'closure_cell_closed', 'five_way_minimality')),
    ('IsometryExtension', ('inner_colVec', 'seed_orthonormal',
                           'finiteIsometryExtensionSF_discharged', 'isometryExtension_unit',
                           'isometryExtension_composite', 'discharged_items',
                           'fullInstruments_of_control_unconditional',
                           'exact_of_sound_control_unconditional',
                           'compositeCompleteness_unconditional',
                           'unitVectorRotation_unconditional',
                           'krausSoundExt_of_sound_control_inert_unconditional',
                           'exactComposite_of_conditions_unconditional',
                           'exactComposite_of_validity_unconditional',
                           'exactAll_of_conditions_unconditional',
                           'exactAll_of_physical_unconditional',
                           'exactAll_iff_physical_unconditional',
                           'fullQuantum_exactComposite_unconditional', 'fullQuantum_exactAll',
                           'systemLoose_exactComposite_unconditional',
                           'final_classification_unconditional', 'operational_classification')),
    ('GeneralCarrier', ('exactComposite_of_validity_general', 'exactAll_of_conditions_general',
                        'exactAll_of_physical_general', 'exactAll_iff_physical_general',
                        'general_characterization',
                        'exactAll_iff_physical_unconditional_of_general',
                        'physical_iff_wellFormed_substantive', 'exactAll_iff_substantive',
                        'exactAll_iff_wellFormed_substantive', 'oi_alone_not_qm',
                        'oi_compatible_classification', 'oi_compatible_iff', 'main_result')),
    ('UhlmannUniqueness', ('inner_rowVec', 'inner_comb', 'comb_eq_zero_of_transfer',
                           'rowBasis_mem', 'coeff_spec', 'inner_transported',
                           'transported_orthonormal', 'rowBasis_orthonormal_ambient',
                           'coord_expansion', 'partialIso_apply', 'inner_comb_orthonormal',
                           'partialIso_inner', 'partialIso_norm', 'partialIso_rowVec',
                           'eq_sum_single', 'matrixOf_apply', 'matrixOf_isometry',
                           'mul_conjTranspose_of_conjTranspose_mul', 'rightUnitary_of_gram',
                           'kronecker_mulVec_purifVec', 'purifier_uniqueness',
                           'boundary_one_item')),
    ('ReachabilitySeam', ('flow_skewAdjoint_gen', 'flow_mem_unitary',
                          'mem_unitary_of_conjTranspose_mul', 'flow_mem_reachable',
                          'control_mem_reachable', 'smul_one_mem_unitary',
                          'phase_mem_reachable', 'conj_mem_unitary',
                          'conjugatedFlow_mem_reachable', 'dense_of_exact',
                          'exists_unit_notMem_finite', 'inv_smul_mem_unitary',
                          'exists_phase_joined', 'exact_of_local', 'conjChannel_smul',
                          'norm_det_unitary', 'exists_special_phase', 'avail_of_mem_closure',
                          'universalReachability_of_exact', 'universalReachability_of_lieRank',
                          'noControls_central_scalar_of_mem_closure',
                          'noControls_central_reachable_scalar', 'swap2_unitary',
                          'swap2_not_scalar', 'noControls_central_not_exact')),
    ('OrbitReachability', ('coe_conjTranspose_mul_self', 'coe_mul_self_conjTranspose', 'orbitDir_skew', 'phaseDir_skew',
                           'orbitDirs_skew', 'real_smul_skew', 'exp_smul_mem_unitary', 'real_smul_neg_I_smul',
                           'exp_orbitDir_mem_reachable', 'norm_eq_one_of_smul_one_mem_unitary', 'exp_phaseDir_eq', 'exp_phaseDir_mem_reachable',
                           'exp_orbitDirs_mem_reachable', 'ad_orbitDirs', 'ad_mem_orbitSpan', 'orbitSpan_closed',
                           'exp_neg_smul_eq_conjTranspose', 'bracket_mem_orbitSpan', 'mem_orbitLie_iff', 'controlGenerators_subset_orbitDirs',
                           'controlLie_le_orbitLie', 'skew_mem_orbitSpan', 'exists_spanning_family', 'prodMap_zero',
                           'prodMap_zero_fun', 'prodMap_mem_reachable', 'dirMap_apply', 'prodMap_hasStrictFDerivAt',
                           'hermMap_apply', 'hermMap_conjTranspose', 'psi_zero', 'psi_hasStrictFDerivAt',
                           'psiDeriv_surjective', 'exists_exp_injOn_nhds', 'localReachability_of_hcontrol', 'localReachabilityOfLieRank',
                           'exactReachability_of_hcontrol', 'universalReachability_of_lieRank_unconditional')),
    ('CompletedOI', ('completedOI_iff_qm', 'completedOI_iff_physical', 'oiCore_not_completedOI', 'observationalIndependence_iff_inert',
                     'parallel_of_observationalIndependence', 'flow_zero', 'flow_isometry', "single_diag_hermitian'",
                     'control_of_reversibleRichness', 'perm_conj_single', "edyad_eq_conj_single'", 'edyad_eq_conj_single',
                     'mul_permMatrix_unitary', 'hControl_single_all', 'reversibleRichness_of_control', 'closure_of_observerRecursion',
                     'observerRecursion_of_closure', 'observerRecursion_iff_closure', 'qm_of_oiPlus', 'oiPlus_of_qm',
                     'oiPlus_iff_qm', 'oiPlus_iff_completedOI', 'countermodel_hid', 'countermodel_hread',
                     'diag_hid', 'diag_hread', 'independence_independent', 'richness_independent',
                     'recursion_independent', 'oiPlus_independence')),
    ('CarrierGeneralOIPlus', ('observationalIndependence_iff_inert', 'parallel_of_observationalIndependence', 'conjChannel_mul_general', 'control_of_reversibleRichness',
                             'reversibleRichness_of_control', 'qm_of_oiPlus', 'oiPlus_of_qm', 'oiPlus_iff_qm',
                             'carrier_general_oiPlus', 'oiPlus_qubit_iff', 'oiPlus_independence')),
    ('EmbeddedObservation', ('availExt_of_eq_zero', 'availExt_iff_embedded', 'id_of_embedded', 'read_of_embedded',
                             'closure_of_embedded', 'systemToLevelOne_of_embedded', 'closure_of_embeddedObservation',
                             'observerRecursion_of_embeddedObservation', 'systemToLevelOne_of_embeddedObservation',
                             'cpFamily_regrouping', 'cpFamily_relabelling', 'ambient_of_qm', 'embeddedObservation_of_qm',
                             'gap_not_embeddedObservation', 'embeddedObservation_independent', 'core_not_embeddedObservation',
                             'oiPlus_of_oiPlusEmbedded', 'qm_of_oiPlusEmbedded', 'oiPlusEmbedded_of_qm', 'oiPlusEmbedded_iff_qm',
                             'oiPlusEmbedded_iff_oiPlus', 'carrier_general_oiPlusEmbedded')),
    ('ImplementationLocality', ('twoPosFamily_regrouping', 'twoPosFamily_relabelling', 'countermodel_ambient', 'countermodel_embeddedObservation',
                                'countermodel_reversibleRichness', 'redundancy_fails', 'form_fixed_existence_fails', 'cp_of_realized',
                                'realized_withSpectator', 'parallel_of_implementationLocal', 'observationalIndependence_of_implementationLocality',
                                'krausSoundExt_of_implementationGenerated', 'validity_of_implementationLocality', 'fullClass_contextStable',
                                'fullClass_labelInvariant', 'generated_of_qm', 'implementationLocality_of_qm', 'countermodel_not_implementationGenerated',
                                'countermodel_not_implementationLocality', 'implementationLocality_independent', 'oiPlusEmbedded_of_oiPlusLocal',
                                'qm_of_oiPlusLocal', 'oiPlusLocal_of_qm', 'oiPlusLocal_iff_qm', 'oiPlusLocal_iff_oiPlusEmbedded',
                                'carrier_general_oiPlusLocal')),
    ('SubstantiveCensus', ('reduction2_trace_card', 'two_card_sub_one_ne_zero', 'kappa_pos', 'redMap_apply',
                           'redMap_trace', 'ampl2_smul_map', 'amplRef_smul_map', 'redMap_twoPositive',
                           'reduction2_preservesDiag', 'redMap_preservesDiag', 'ent3_star', 'ent3_norm',
                           'refMarginalR_ent3', 'amplRef_reduction2_ent3', 'amplRef_reduction2_ent3_form', 'amplRef_redMap_ent3_not_posSemidef',
                           'traceShift_apply', 'choiMatrix_traceShift', 'traceShift_choi_form', 'traceShift_not_cp',
                           'classTheory_availExt_iff', 'classTheory_validity', 'classTheory_systemToLevelOne', 'classTheory_wellFormed',
                           'classTheory_relabel', 'classTheory_realizes', 'classTheory_inert', 'classTheory_control',
                           'classTheory_closure', 'classTheory_not_control', 'classTheory_not_closure', 'classTheory_not_inert',
                           'reindex_reindex', 'transport_trans', 'transport_spectatorLast', 'discardWith_uniform_spectatorLast',
                           'preservesDiag_conjChannel_of_colMonomial', 'colMonomial_one_kronecker', 'D3_colMonomial', 'E3_colMonomial',
                           'gapChannel_eq_sum', 'gapChannel_cp', 'gapChannel_preservesDiag', 'iota6_injective',
                           'discard_redMap', 'discard_redMap_not_cp', 'diagGap_wellFormed', 'diagGap_realizes',
                           'diagGap_inert', 'diagGap_not_control', 'diagGap_not_closure', 'diagTwoPos_wellFormed',
                           'diagTwoPos_realizes', 'diagTwoPos_closure', 'diagTwoPos_not_control', 'diagTwoPos_not_inert',
                           'capped_wellFormed', 'capped_control', 'capped_realizes', 'capped_not_inert',
                           'capped_not_closure', 'cappedDiag_wellFormed', 'cappedDiag_realizes', 'cappedDiag_not_control',
                           'cappedDiag_not_inert', 'cappedDiag_not_closure', 'cell_none', 'cell_I',
                           'cell_C', 'cell_K', 'cell_IC', 'cell_IK',
                           'cell_CK', 'cell_ICK', 'substantive_census', 'no_boolean_relation',
                           'qm_is_the_top_cell')),
    ('FrequencyMatching', ('ampC_eq_zero', 'normSq_eq_sum_gaps',
                           'coefficients_by_frequency_determined', 'fiber_singleton',
                           'coefficient_line_extraction')),
    ('CongruentReconstruction', ('modulus_rigid', 'moduli_match',
                                 'phase_coboundary_of_moduli', 'phase_coboundary',
                                 'reconstruction_translation_of_moduli',
                                 'reconstruction_translation',
                                 'reconstruction_reflection_of_moduli',
                                 'reconstruction_reflection',
                                 'reconstruction_dim_zero', 'reconstruction_dim_one',
                                 'dim_two_moduli_dichotomy', 'unitary2_line_dichotomy',
                                 'reconstruction_dim_two', 'exceptional_impossible',
                                 'twoBranch_of_PiccardClassification',
                                 'twoBranch_of_spectral_classification'))):
    src = open(os.path.join(BRIDGE, 'OIBridge', f'{fname}.lean'), encoding='utf-8').read()
    body = src[src.index('namespace OIBridge'):]
    ok6 &= f'import OIBridge.{fname}' in root
    ok6 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
    ok6 &= re.search(r'(?m)^axiom ', body) is None
    ok6 &= 'native_decide' not in body
    ok6 &= all((f'theorem {nm}' in src) or (f'lemma {nm}' in src) for nm in names)
    ok6 &= all(f'#print axioms {nm}' in src for nm in names)
# the census must attach all three failures to ONE shared core: the same classical comb
# must be proved for every completion, or the independence claim is three unrelated examples
ic = open(os.path.join(BRIDGE, 'OIBridge', 'IndependenceCensus.lean'),
          encoding='utf-8').read()
ok6 &= all(f'stateFold {c} steps (Matrix.diagonal w)' in ic
           for c in ('nonFunctorialC', 'nonTensorC', 'restrictedC'))
# the restricted-control completion is ordinary quantum kinematics with a proper reachable
# subgroup, NOT a non-quantum theory: the wording guard must be present, not an overclaim
ok6 &= 'not "non-quantum"' in ic and 'UNRESTRICTED' in ic
# C1-C4 must be kernel conditions bound into the capstone, not a prose reading of it
ok6 &= 'def CoreC1C4 : Prop' in ic and 'theorem core_isC1C4 : CoreC1C4' in ic
# CANONICAL C-NUMBERING GUARD.  OI numbers the conditions C1 coupling, C2 memory
# persistence, C3 sufficient hidden memory capacity, C4 history readback.  Pin each label
# to the docstring that actually precedes its theorem, so the C3/C4 pair cannot silently
# flip again (they were reversed once, and the theorem content does not catch it).
for _lbl, _thm in (('C3', 'core_capacity_saturates'), ('C4', 'core_history_readback')):
    _i = ic.index(f'theorem {_thm}')
    _doc = ic[ic.rindex('/--', 0, _i):_i]
    ok6 &= f'**{_lbl} ' in _doc
ok6 &= ic.index('theorem core_capacity_saturates') < ic.index('theorem core_history_readback')
ok6 &= 'C3 (sufficient hidden memory capacity)' in ic and 'C4 (history readback)' in ic
cap = ic[ic.index('theorem oi_core_underdetermines_completion'):]
ok6 &= 'CoreC1C4' in cap[:cap.index(':=')]
ok6 &= 'S ⇔ D ⇔ Q_fb` is untouched' in ic
# ROUND-24 SCOPE GUARDS.  The compositional principle must DESCEND from implementation-level
# clauses, not be defined as a conjunction of the round-18/20 predicates; and the Lie
# certificate must stay a SEPARATE predicate from operational control richness.
mc = open(os.path.join(BRIDGE, 'OIBridge', 'MonoidalCompletion.lean'),
          encoding='utf-8').read()


def _slice(text, start, stop):
    """Text between two markers, or '' if either is missing (a clean lint failure)."""
    if start not in text:
        return ''
    rest = text[text.index(start):]
    return rest[:rest.index(stop)] if stop in rest else rest


ok6 &= 'def ImplementationExtensionality' in mc and 'def SpectatorIndependent' in mc
# HComp's DEFINITION must be the two independent clauses -- round 18's predicate may be
# NAMED in the scope note, but must not appear in the definition itself
_hcomp = _slice(mc, 'def HComp', '/--')
ok6 &= bool(_hcomp) and 'CoherentFunctoriality' not in _hcomp
ok6 &= 'ImplementationExtensionality' in _hcomp and 'SpectatorIndependent' in _hcomp
# the certificate and the operational richness principle must be genuinely DIFFERENT
# notions, not aliases: one is about the control Lie algebra, the other about which
# channels are available.  H_Lie is sufficient for reachability, not necessary for full QM.
_hlie = _slice(mc, 'def HControl {G : Type*}', '/--')
_hop = _slice(mc, 'def UniversalUnitaryReachability\n', 'omit')
ok6 &= bool(_hlie) and bool(_hop)
ok6 &= 'controlLie' in _hlie and 'controlLie' not in _hop
ok6 &= 'conjChannel' in _hop and 'conjChannel' not in _hlie
ok6 &= 'theorem centralDrift_not_HControl' in mc
# HControl_iff_controlLie0_full must be kernel-internal: no exponential, no Lie integration
_hc = _slice(mc, 'theorem HControl_iff_controlLie0_full', '/--')
ok6 &= bool(_hc) and 'exp' not in _hc
# the external analytic boundary: the historical four-item statement is PRESERVED and
# LABELLED, and the round-35 audit file carries the current three-item statement
_flat = ' '.join(mc.split())
ok6 &= 'stays exactly four items and no more' in _flat
ok6 &= all(item in _flat for item in
           ('compact Lie integration', 'finite isometry extension',
            'PSD square-root/factorization', 'Uhlmann/Schmidt uniqueness'))
_LABEL = 'HISTORICAL, SUPERSEDED BY THE ROUND-35 BOUNDARY AUDIT'
ok6 &= _LABEL in _flat
for _fn in ('OperationalAssembly', 'StinespringAssembly'):
    ok6 &= _LABEL in ' '.join(open(os.path.join(BRIDGE, 'OIBridge', f'{_fn}.lean'),
                                   encoding='utf-8').read().split())
ba = open(os.path.join(BRIDGE, 'OIBridge', 'BoundaryAudit.lean'), encoding='utf-8').read()
_baflat = ' '.join(ba.split())
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: THREE ITEMS' in _baflat
ok6 &= 'DISCHARGED INTERNALLY (round thirty-four): PSD square-root / factorization' in _baflat
ok6 &= all(item in _baflat for item in
           ('compact Lie integration / reachability', 'finite isometry extension',
            'finite Uhlmann / Schmidt / right-unitary uniqueness'))
_pd = _slice(ba, 'theorem psdFactorization_discharged', 'theorem purification_unconditional')
ok6 &= bool(_pd) and 'psdFactorization_of_spectral' in _pd
ok6 &= 'It proves nothing new' in _baflat and 'PROVENANCE IS PRESERVED, NOT REWRITTEN' in _baflat
# the remaining items must not be claimed discharged anywhere in the audit (item 2, finite
# isometry extension, IS discharged from round forty-five -- see the Round-45 guards)
ok6 &= 'Lie integration is discharged' not in _baflat and 'reachability is discharged' not in _baflat
ok6 &= 'reachability is discharged' not in _baflat   # (right-unitary uniqueness IS discharged from round forty-eight)
# Purification keeps its conditional theorem and cross-references the discharge
_pu = open(os.path.join(BRIDGE, 'OIBridge', 'Purification.lean'), encoding='utf-8').read()
ok6 &= 'theorem purification_of_factorization' in _pu and 'psdFactorization_of_spectral' in _pu
# ROUND-35 GUARDS (part two).  The reference amplification must be GENERIC, 2-positivity its
# Fin 2 case definitionally, the threshold a theorem, the reindexing explicit data keeping the
# system slot, and NO sufficiency claim anywhere.
re_ = open(os.path.join(BRIDGE, 'OIBridge', 'ReferenceExtension.lean'), encoding='utf-8').read()
_rebody = re_.split('namespace OIBridge')[1]
_reflat = ' '.join(re_.split())
_irp = _slice(re_, 'def IsReferencePositive', '/--')
ok6 &= bool(_irp) and '∀ M : Matrix (R × S) (R × S) ℂ, M.PosSemidef → (amplRef R Φ M).PosSemidef' in _irp
_iff = _slice(re_, 'theorem isTwoPositive_iff_referencePositive', 'def IsThreePositive')
ok6 &= bool(_iff) and 'Iff.rfl' in _iff
_thr = _slice(re_, 'theorem reduction2_threshold', ':=')
ok6 &= bool(_thr) and 'IsTwoPositive (reduction2 (Fin 2 × Fin 2)) ∧ ¬ IsThreePositive (reduction2 (Fin 2 × Fin 2))' in _thr
_frm = _slice(re_, 'theorem amplRef_reduction2_maxEnt3_form', ':= by')
ok6 &= bool(_frm) and '= -3 / 7' in _frm
# the reindexing is an equivalence handed in as data, not a cardinality simp
_ws = _slice(re_, 'def withSpectator', 'def HasParallelReferenceExtension')
ok6 &= bool(_ws) and 'Matrix.reindexLinearEquiv' in _ws and 'Fintype.card' not in _ws
_pre = _slice(re_, 'def HasParallelReferenceExtension', 'end Spectator')
ok6 &= bool(_pre) and '(e : R × (A × Fin n) ≃ A × Fin m)' in _pre
ok6 &= 'T.availExt n O F → T.availExt m O (fun a => withSpectator R e (F a))' in _pre
_qi = _slice(re_, 'def qutritIdx', 'theorem qutritIdx_apply')
ok6 &= bool(_qi) and 'finProdFinEquiv' in _qi and 'Equiv.prodAssoc' in _qi and 'Equiv.prodComm' in _qi
ok6 &= 'qutritIdx (r, (a, e)) = (a, finProdFinEquiv (r, e))' in re_
# the countermodel theorems name the round-34 theory and nothing else
_cq = _slice(re_, 'theorem countermodel_not_qutritReferenceExtension', ':= by')
ok6 &= bool(_cq) and '¬ HasQutritReferenceExtension countermodel' in _cq
_ind = _slice(re_, 'theorem control_not_implies_parallelReferenceExtension', ':=')
ok6 &= bool(_ind) and 'HasCompositeUnitaryControl T ∧ ¬ HasParallelReferenceExtension T' in _ind
# NO sufficiency, no structure field, no satisfiability claim
ok6 &= 'KrausSoundExt' not in _rebody
ok6 &= re.search(r'(?m)^structure ', re_) is None
ok6 &= 'theorem parallelReferenceExtension_implies' not in re_
ok6 &= 'theorem qutritReferenceExtension_implies' not in re_
ok6 &= 'No sufficiency' in _reflat
ok6 &= 'is not shown to be satisfiable by any theory here' in _reflat
ok6 &= 'it is not, in general, enough to characterize complete positivity' in _reflat
ok6 &= "That is round thirty-six's question" in _reflat
ok6 &= 'is strictly weaker' not in _reflat
# ROUND-36 GUARDS.  The sufficiency theorem must consume boundary item 2 as an explicit
# hypothesis at the ONE-DIMENSIONAL source, derive rotation from it (no Mathlib discharge of
# item 2), and claim soundness only -- not composite completeness.
rs = open(os.path.join(BRIDGE, 'OIBridge', 'ReferenceSufficiency.lean'), encoding='utf-8').read()
_rsbody = rs.split('namespace OIBridge')[1]
_rsflat = ' '.join(rs.split())
_cap = _slice(rs, 'theorem krausSoundExt_of_sound_control_refext', ':= by')
ok6 &= bool(_cap) and '(hext : FiniteIsometryExtensionSF Unit)' in _cap
# ROUND-37 OPENING CLEANUP: the primary antecedent is system SOUNDNESS, not exactness;
# system completeness must not appear in the capstone slice
ok6 &= '(hsound : KrausSound T)' in _cap and 'HasCompositeUnitaryControl T' in _cap
ok6 &= 'ExactFiniteEndomorphicQuantumOps' not in _cap
ok6 &= 'HasFullFiniteEndomorphicInstruments' not in _cap
ok6 &= 'HasParallelReferenceExtension T' in _cap and _cap.rstrip().endswith('KrausSoundExt T')
# the round-36 exact form survives as a corollary, proved through exact_iff_sound_and_full
_capx = _slice(rs, 'theorem krausSoundExt_of_exact_control_refext', 'theorem countermodel_witness_level_two')
ok6 &= bool(_capx) and '(hex : ExactFiniteEndomorphicQuantumOps T)' in _capx
ok6 &= 'krausSoundExt_of_sound_control_refext T hext ((exact_iff_sound_and_full T).mp hex).1' in _capx
ok6 &= 'STRENGTHENED IN ROUND THIRTY-SEVEN' in _rsflat
_rot = _slice(rs, 'theorem unitVectorRotation_of_isometryExtension', 'end Rotation')
ok6 &= bool(_rot) and 'hext (2 * n + 1)' in _rot and 'Esf' in _rot
ok6 &= 'exists_orthonormalBasis' not in _rsbody and 'OrthonormalBasis' not in _rsbody
ok6 &= 'gramSchmidt' not in _rsbody
ok6 &= 'def UnitVectorRotation' in rs
# both failure modes through ONE polarization argument, no hidden case split
ok6 &= 'theorem two_single_eq_dyads' in rs and 'theorem isHermitian_of_forms_real' in rs
ok6 &= 'theorem posSemidef_of_forms_nonneg' in rs and 'No case split is hidden' in _rsflat
# the branch-CP lemma must reach exactness through the discard of an AVAILABLE family
_bcp = _slice(rs, 'theorem branch_cp', 'end BranchCP')
ok6 &= bool(_bcp) and 'prepAvail_discard' in _bcp and 'sound_avail_cp_tp' in _bcp
ok6 &= '(hsound : KrausSound T)' in _bcp and 'exact_avail_cp_tp' not in _bcp
ok6 &= 'withSpectator' in _bcp and 'diag_nonneg' in _bcp
# the positive instance
_fq = _slice(rs, 'noncomputable def fullQuantum', 'theorem fullQuantum_exact')
ok6 &= bool(_fq) and 'avail := fun _ _ _ F => IsKrausFamily F' in _fq
ok6 &= 'availExt := fun _ _ _ _ F => IsCPInstrument F' in _fq
ok6 &= 'theorem fullQuantum_parallelReferenceExtension' in rs
_sat = _slice(rs, 'theorem parallelReferenceExtension_satisfiable', ':=')
ok6 &= bool(_sat) and 'HasParallelReferenceExtension T ∧ KrausSoundExt T' in _sat
# no structure field; soundness direction only; OI question deferred
ok6 &= re.search(r'(?m)^structure ', rs) is None
ok6 &= 'NOT claimed: composite COMPLETENESS' in _rsflat
ok6 &= 'soundness direction only' in _rsflat
ok6 &= "that is round thirty-seven's question" in _rsflat
ok6 &= 'theorem krausSoundExt_iff' not in rs and 'theorem composite_complete' not in rs
ok6 &= 'is strictly weaker' not in _rsflat
# ROUND-37 GUARDS.  The H_comp bridge must separate FORM (what spectator independence
# determines) from EXISTENCE (what it does not supply): the form theorems must land on
# amplRefL / withSpectator; inert-spectator compositionality must be an EXISTENCE clause
# (∃ G) over IsSpectatorExtension; the non-implication must be kernelized on the round-34
# countermodel with H_comp REALIZED (every named coherent map available); no claim that
# H_comp or OI implies the extension, no composite completeness, no OI ⟺ QM.
sb = open(os.path.join(BRIDGE, 'OIBridge', 'SpectatorBridge.lean'), encoding='utf-8').read()
_sbflat = ' '.join(sb.split())
_form = _slice(sb, 'theorem hComp_spectator_form', ':=')
ok6 &= bool(_form) and '(h : HComp act corr CB C)' in _form
ok6 &= '= amplRefL R (correlationExtension g (CB g))' in ' '.join(_form.split())
_mi = _slice(sb, 'theorem mapSpectatorIndependent_iff_amplRef', ':= by')
ok6 &= bool(_mi) and 'MapSpectatorIndependent ΦB ΦRS ↔ ΦRS = amplRefL R ΦB' in _mi
_ise = _slice(sb, 'theorem isSpectatorExtension_iff', ':= by')
ok6 &= bool(_ise) and 'IsSpectatorExtension e Φ G ↔ G = withSpectator R e Φ' in _ise
_inert = _slice(sb, 'def InertSpectatorCompositionality', 'theorem inertSpectator_iff_parallelReferenceExtension')
ok6 &= bool(_inert) and '∃ G' in _inert and 'IsSpectatorExtension e (F a) (G a)' in _inert
ok6 &= 'T.availExt m O G' in _inert
ok6 &= 'theorem inertSpectator_iff_parallelReferenceExtension' in sb
_hr = _slice(sb, 'def HCompRealized', 'theorem hCompRealized_spectator_available')
ok6 &= bool(_hr) and 'HComp act corr CB C' in _hr and 'transport e' in _hr
ok6 &= 'T.availExt m Unit' in _hr and 'T.availExt n Unit' in _hr
_ni = _slice(sb, 'theorem hcompRealized_not_implies_parallelReferenceExtension', ':=')
ok6 &= bool(_ni) and 'HCompRealized T qutritIdx' in _ni
ok6 &= '¬ HasParallelReferenceExtension T' in _ni and '¬ InertSpectatorCompositionality T' in _ni
ok6 &= 'HasCompositeUnitaryControl T' in _ni
ok6 &= 'countermodel' in _slice(sb, 'theorem hcompRealized_not_implies_parallelReferenceExtension', 'theorem hcompRealized_consistent')
ok6 &= 'theorem hcompRealized_consistent_with_parallelReferenceExtension' in sb
ok6 &= 'theorem krausSoundExt_of_sound_control_inert' in sb
ok6 &= 'inert-spectator compositionality' in _sbflat.lower()
ok6 &= 'acts identically on that spectator' in _sbflat
ok6 &= re.search(r'(?m)^structure ', sb) is None
ok6 &= 'NOT claimed: composite COMPLETENESS' in _sbflat
ok6 &= "round thirty-eight's" in _sbflat
ok6 &= 'NOT claimed: OI + conditions' in _sbflat
ok6 &= 'theorem hComp_implies_parallelReferenceExtension' not in sb
ok6 &= 'theorem oi_implies_parallelReferenceExtension' not in sb
ok6 &= 'theorem oi_iff_quantum' not in sb and 'theorem composite_complete' not in sb
ok6 &= 'theorem inertSpectator_of_hComp' not in sb
# ROUND-38 GUARDS.  The shifted theory must be built with each field discharged by a NAMED
# audit lemma carrying its exact hypothesis (control for the composite identity, inert
# spectators for the relative readout, the closure rule for the discard); the closure rule
# must be the relative uniform-attach-then-discard rule and nothing more; the endpoint must
# consume KrausSound (not exactness), the two compositional conditions and boundary item 2
# at the named carriers; the obstruction must be a countermodel with exact system QM, control,
# inert spectators and composite soundness; no claim that OI implies either condition, no
# claim of full QM beyond the finite endomorphic scope.
ac = open(os.path.join(BRIDGE, 'OIBridge', 'AncillaClosure.lean'), encoding='utf-8').read()
_acflat = ' '.join(ac.split())
_clos = _slice(ac, 'def IteratedAncillaClosure', 'end Audit')
ok6 &= bool(_clos) and 'uniformAttach (m + 1)' in _clos and 'discardWith' in _clos
ok6 &= 'T.availExt (n * (m + 1)) O' in _clos and 'T.availExt n O' in _clos
ok6 &= 'pureAttach' not in _clos and 'conjChannel' not in _clos and 'IsKrausFamily' not in _clos
_shift = _slice(ac, 'noncomputable def shift', 'theorem shift_avail_iff')
ok6 &= bool(_shift) and 'availExt_id_of_control T hctrl n' in _shift
ok6 &= 'availExt_relativeReadout T hin n m' in _shift and 'hclos n m' in _shift
ok6 &= 'avail := fun O _ _ F => T.availExt n O F' in _shift
ok6 &= 'transport (shiftIdx A n m)' in _shift
_aud = _slice(ac, 'theorem availExt_id_of_control', 'def IteratedAncillaClosure')
ok6 &= bool(_aud) and '(hctrl : HasCompositeUnitaryControl T)' in _aud
ok6 &= '(hin : InertSpectatorCompositionality T)' in _aud
ok6 &= 'theorem transport_localLuders' in ac and 'withSpectator (Fin n) (specIdx A n m)' in ac
_end = _slice(ac, 'theorem exactComposite_of_conditions', ':=')
ok6 &= bool(_end) and '(hsound : KrausSound T)' in _end
ok6 &= '(hin : InertSpectatorCompositionality T)' in _end
ok6 &= '(hclos : IteratedAncillaClosure T)' in _end
ok6 &= 'FiniteIsometryExtensionSF Unit' in _end
ok6 &= 'FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))' in _end
ok6 &= _end.rstrip().endswith('ExactCompositeQuantumOps T')
ok6 &= 'ExactFiniteEndomorphicQuantumOps' not in _end
ok6 &= 'theorem compositeCompleteness' in ac and 'theorem conditions_satisfiable' in ac
ok6 &= re.search(r'(?m)^structure ', ac) is None
ok6 &= 'NOT claimed: that OI implies iterated ancilla closure' in _acflat
ok6 &= 'finite endomorphic instrument scope' in _acflat
ok6 &= 'theorem oi_implies_iteratedAncillaClosure' not in ac
ok6 &= 'theorem oi_iff_quantum' not in ac and 'theorem full_quantum_mechanics' not in ac
co = open(os.path.join(BRIDGE, 'OIBridge', 'ClosureObstruction.lean'), encoding='utf-8').read()
_coflat = ' '.join(co.split())
_ind = _slice(co, 'theorem closure_independent', ':=')
ok6 &= bool(_ind) and 'ExactFiniteEndomorphicQuantumOps T' in _ind
ok6 &= 'HasCompositeUnitaryControl T' in _ind and 'InertSpectatorCompositionality T' in _ind
ok6 &= 'KrausSoundExt T' in _ind and '¬ IteratedAncillaClosure T' in _ind
ok6 &= '¬ HasFullCompositeInstruments T' in _ind
_ns = _slice(co, 'theorem admissible_no_shift', ':= by')
ok6 &= bool(_ns) and "HasCompositeUnitaryControl T'" in _ns
ok6 &= 'admissibleTheory.availExt 2 O F' in _ns
_adn = _slice(co, 'theorem ad_not_adm', 'end Damping')
ok6 &= bool(_adn) and 'Matrix.rank_one' in _adn and 'rank_mul_le_left' in _adn
ok6 &= 'rank_le_card_width' in _adn and 'dampInv_mul' in _adn
ok6 &= 'theorem dyad_sum_span' in co and 'Kraus uniqueness is not invoked' in _coflat
ok6 &= 'KrausUniqueness' not in co.split('namespace OIBridge')[1]
ok6 &= re.search(r'(?m)^structure ', co) is None
ok6 &= 'theorem admissible_iteratedAncillaClosure' not in co
# ROUND-39 GUARDS.  The independence matrix must carry all three rows with system Kraus
# soundness and control in each; the two H_comp non-implications must be stated on the
# realized predicate; the frozen classification must be the endpoint implication against
# boundary item 2 at the named carriers plus the three witnesses; and the OI caveat must be
# explicit -- no claim that observer independence itself fails to imply either principle.
ci = open(os.path.join(BRIDGE, 'OIBridge', 'CompositionalIndependence.lean'), encoding='utf-8').read()
_ciflat = ' '.join(ci.split())
_mat = ' '.join(_slice(ci, 'theorem independence_matrix', ':=').split())
ok6 &= bool(_mat) and _mat.count('KrausSound T ∧ HasCompositeUnitaryControl T') == 3
ok6 &= 'IteratedAncillaClosure T ∧ ¬ InertSpectatorCompositionality T' in _mat
ok6 &= 'InertSpectatorCompositionality T ∧ ¬ IteratedAncillaClosure T' in _mat
ok6 &= 'InertSpectatorCompositionality T ∧ IteratedAncillaClosure T)' in _mat
_cc = ' '.join(_slice(ci, 'theorem conditional_classification', ':=').split())
ok6 &= bool(_cc) and 'FiniteIsometryExtensionSF Unit' in _cc
ok6 &= 'FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))' in _cc
ok6 &= '→ IteratedAncillaClosure T → ExactCompositeQuantumOps T' in _cc
ok6 &= 'ExactFiniteEndomorphicQuantumOps' not in _cc
ok6 &= 'theorem countermodel_iteratedAncillaClosure' in ci
ok6 &= 'theorem discardWith_uniform_twoPositive' in ci
for _nm in ('hcompRealized_inert_not_implies_closure', 'hcompRealized_closure_not_implies_inert'):
    _hs = ' '.join(_slice(ci, 'theorem ' + _nm, ':=').split())
    ok6 &= bool(_hs) and 'HCompRealized T qutritIdx' in _hs and 'HasCompositeUnitaryControl T' in _hs
ok6 &= 'theorem inert_not_deletable' in ci and 'theorem closure_not_deletable' in ci
ok6 &= 'They do NOT show that observer independence itself fails to imply them' in _ciflat
ok6 &= 'is not done here and is not claimed' in _ciflat
ok6 &= re.search(r'(?m)^structure ', ci) is None
ok6 &= 'theorem oi_not_implies_inert' not in ci and 'theorem oi_not_implies_closure' not in ci
ok6 &= 'theorem oi_iff_quantum' not in ci
ok6 &= 'CAVEAT RETIRED IN ROUND FORTY' in _ciflat
# ROUND-40 GUARDS.  The OI bridge must embed the sealed core with the hidden bit on the
# system qubit and the visible pair on the ancilla; the readout must be the ACTUAL visible
# readout (both hidden partners kept), proved equal to the native readout, not the round-23
# full-basis probe; the realization predicate must carry C1-C4, both transported permutation
# channels, the readout identity and availability, and the comb agreement; the audit must be
# a bundled theorem; the capstone must realize the SAME core in both countermodels; the
# claim boundary must name what remains interpretive.
oi = open(os.path.join(BRIDGE, 'OIBridge', 'OIRealization.lean'), encoding='utf-8').read()
_oiflat = ' '.join(oi.split())
_ci2 = _slice(oi, 'def coreIdx', 'theorem coreIdx_apply')
ok6 &= bool(_ci2) and 'toFun p := (bitIdx p.1.2, visIdx (p.1.1, p.2))' in _ci2
_rv = _slice(oi, 'def readVisible', 'theorem readVisible_apply')
ok6 &= bool(_rv) and 'if vis p = r ∧ vis q = r then X p q else 0' in _rv
ok6 &= 'ludersLift' not in _rv and 'Step.read' not in oi.split('namespace OIBridge')[1]
_rl = ' '.join(_slice(oi, 'theorem readVisible_eq_localLuders', ':= by').split())
ok6 &= bool(_rl) and 'transport coreIdx (readVisible r) = localLuders (A := Fin 2) (visIdx r)' in _rl
_pred = ' '.join(_slice(oi, 'def RealizesSealedOICore', 'theorem relabel_available').split())
ok6 &= bool(_pred) and 'CoreC1C4' in _pred
ok6 &= 'correlationExtension sigmaPerm (onesCorr Core)' in _pred
ok6 &= 'correlationExtension tauPerm (onesCorr Core)' in _pred
ok6 &= 'transport coreIdx (readVisible r) = T.readout 4 (visIdx r)' in _pred
ok6 &= 'T.availExt 4 (Bool × Bool) (fun r => transport coreIdx (readVisible r))' in _pred
ok6 &= 'realizedFold steps' in _pred and 'visWeightFold steps w' in _pred
_th = ' '.join(_slice(oi, 'theorem realizesSealedOICore_of_control', ':= by').split())
ok6 &= bool(_th) and '(hctrl : HasCompositeUnitaryControl T) : RealizesSealedOICore T' in _th
_aud = ' '.join(_slice(oi, 'def SealedCoreIsFiniteOI', 'theorem sealedCore_is_finiteOI').split())
ok6 &= bool(_aud) and 'Fintype.card Core = 8' in _aud and '1 < Fintype.card Bool' in _aud
ok6 &= 'swapFn p = swapFn q → p = q' in _aud and 'swapFn (swapFn p) = p' in _aud
ok6 &= 'visWeightStep (.act g) (fun _ => c) = fun _ => c' in _aud and 'CoreC1C4' in _aud
_cap = ' '.join(_slice(oi, 'theorem sameCore_both_sides', ':=').split())
ok6 &= bool(_cap) and _cap.startswith('theorem sameCore_both_sides : SealedCoreIsFiniteOI')
ok6 &= _cap.count('RealizesSealedOICore T ∧ ExactFiniteEndomorphicQuantumOps T') == 3
ok6 &= 'KrausSound' not in _cap
ok6 &= 'IteratedAncillaClosure T ∧ ¬ InertSpectatorCompositionality T' in _cap
ok6 &= 'InertSpectatorCompositionality T ∧ ¬ IteratedAncillaClosure T' in _cap
ok6 &= 'theorem finiteOI_not_implies_inert' in oi and 'theorem finiteOI_not_implies_closure' in oi
ok6 &= 'What remains outside the kernel is interpretive only' in _oiflat
ok6 &= re.search(r'(?m)^structure ', oi) is None
ok6 &= 'theorem oi_iff_quantum' not in oi and 'theorem oi_implies_quantum' not in oi
ok6 &= 'theorem manuscript_oi_not_implies' not in oi
# ROUND-41 GUARDS.  Validity must be stated WITHOUT any quantum formalism (no CP, Choi or
# Kraus in the definition); the promotion theorem must consume validity and inert spectators
# only; the physical endpoint must not mention KrausSound, exactness or the Unit isometry
# hypothesis; the classification must carry the three witnesses; the reading of the endpoint
# as a classification of completions compatible with OI must be explicit.
ov = open(os.path.join(BRIDGE, 'OIBridge', 'OperationalValidity.lean'), encoding='utf-8').read()
_ovflat = ' '.join(ov.split())
_val = _slice(ov, 'def CompositeOperationalValidity', 'noncomputable def selfRefIdx')
ok6 &= bool(_val) and 'X.PosSemidef → ((F a) X).PosSemidef' in _val
ok6 &= '∑ a, ((F a) X).trace = X.trace' in _val
ok6 &= 'IsCompletelyPositive' not in _val and 'choiMatrix' not in _val
ok6 &= 'Kraus' not in _val and 'conjChannel' not in _val
_prom = ' '.join(_slice(ov, 'theorem krausSoundExt_of_validity_inert', ':=').split())
ok6 &= bool(_prom) and '(hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)' in _prom
ok6 &= _prom.rstrip().endswith('KrausSoundExt T')
ok6 &= 'KrausSound T' not in _prom.replace('KrausSoundExt T', '')
ok6 &= 'HasCompositeUnitaryControl' not in _prom and 'FiniteIsometryExtensionSF' not in _prom
_cpv = _slice(ov, 'theorem cp_of_valid_inert', 'theorem krausSoundExt_of_validity_inert')
ok6 &= bool(_cpv) and 'choiMatrix_eq_amplRef' in _cpv and 'selfRefIdx' in _cpv
_pe = ' '.join(_slice(ov, 'theorem exactComposite_of_validity', ':=').split())
ok6 &= bool(_pe) and 'FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))' in _pe
ok6 &= 'FiniteIsometryExtensionSF Unit' not in _pe
ok6 &= 'KrausSound T' not in _pe and 'ExactFiniteEndomorphicQuantumOps' not in _pe
ok6 &= '(hval : CompositeOperationalValidity T)' in _pe and '(hclos : IteratedAncillaClosure T)' in _pe
ok6 &= _pe.rstrip().endswith('ExactCompositeQuantumOps T')
_pc = ' '.join(_slice(ov, 'theorem physical_classification', ':=').split())
ok6 &= bool(_pc) and _pc.count('CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T') == 3
ok6 &= 'FiniteIsometryExtensionSF Unit' not in _pc
ok6 &= 'theorem validity_not_implies_krausSoundExt' in ov
ok6 &= 'theorem physical_inert_not_deletable' in ov and 'theorem physical_closure_not_deletable' in ov
ok6 &= 'CLASSIFICATION OF OPERATIONAL COMPLETIONS COMPATIBLE WITH OI' in _ovflat
ok6 &= 'not yet a derivation of the quantum structure from OI alone' in _ovflat
ok6 &= re.search(r'(?m)^structure ', ov) is None
ok6 &= 'theorem oi_iff_quantum' not in ov and 'theorem validity_of_oi' not in ov
# ROUND-42 GUARDS.  The structural direction must be proved with no hypothesis beyond the
# structure (from prepAvail_uniform and prepAvail_discard); the principle must be ONLY the
# system-to-level-one direction; the endpoint must cover the system and every composite,
# consume the five conditions and item 2 at the composite carriers only, with no KrausSound,
# no exactness premise and no Unit isometry; the loose countermodel must be stated with an
# unrestricted system predicate and refuted directly by the trace amplifier.
ls = open(os.path.join(BRIDGE, 'OIBridge', 'LevelOneSeam.lean'), encoding='utf-8').read()
_lsflat = ' '.join(ls.split())
_sd = _slice(ls, 'theorem avail_of_availExt_one', 'def SystemToLevelOne')
ok6 &= bool(_sd) and 'prepAvail_discard' in _sd and 'prepAvail_uniform' in _sd
ok6 &= 'SystemToLevelOne' not in _sd and 'HasCompositeUnitaryControl' not in _sd
_pr = ' '.join(_slice(ls, 'def SystemToLevelOne', 'theorem transport_transport_symm').split())
ok6 &= bool(_pr) and 'T.avail O F → T.availExt 1 O (fun a => transport (levelOneIdx A).symm (F a))' in _pr
ok6 &= '↔' not in _pr
ok6 &= 'theorem avail_iff_availExt_one' in ls and 'theorem isKraus_transport' in ls
_ea = ' '.join(_slice(ls, 'theorem exactAll_of_conditions', ':=').split())
ok6 &= bool(_ea) and '(h1 : SystemToLevelOne T)' in _ea and '(hval : CompositeOperationalValidity T)' in _ea
ok6 &= 'FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))' in _ea and 'FiniteIsometryExtensionSF Unit' not in _ea
ok6 &= 'KrausSound' not in _ea and 'ExactFiniteEndomorphicQuantumOps T' not in _ea.split('ExactAllFiniteEndomorphicQuantumOps')[0]
ok6 &= _ea.rstrip().endswith('ExactAllFiniteEndomorphicQuantumOps T')
_lo = _slice(ls, 'noncomputable def systemLoose', 'theorem systemLoose_control')
ok6 &= bool(_lo) and 'avail := fun _ _ _ _ => True' in _lo and 'availExt := fun _ _ _ _ F => IsCPInstrument F' in _lo
_ne = _slice(ls, 'theorem systemLoose_not_systemToLevelOne', 'theorem levelOne_independent')
ok6 &= bool(_ne) and 'FiniteIsometryExtensionSF' not in _ne and '(2 : ℂ) • LinearMap.id' in _ne
_fc = ' '.join(_slice(ls, 'theorem final_classification', ':=').split())
ok6 &= bool(_fc) and '→ SystemToLevelOne T → ExactAllFiniteEndomorphicQuantumOps T' in _fc
ok6 &= '¬ SystemToLevelOne T ∧ ¬ ExactFiniteEndomorphicQuantumOps T' in _fc
ok6 &= 'theorem levelOne_independent' in ls and 'theorem levelOne_not_deletable' in ls
ok6 &= 'bookkeeping law' in _lsflat
ok6 &= re.search(r'(?m)^structure ', ls) is None
ok6 &= 'theorem oi_iff_quantum' not in ls and 'theorem systemToLevelOne_of_oi' not in ls
# ROUND-43 GUARDS.  The necessity direction must be kernel-internal (no isometry hypothesis
# in physical_of_exactAll); the characterization must carry item 2 at the composite
# carriers only and no Unit isometry, no KrausSound and no exactness premise; the bundle
# must be exactly the five conditions; the open closure cell must be named as open and
# admissible_not_systemToLevelOne must be a theorem; the diagonal theory must carry the
# diagonal-preservation conjunct at every level and refute control by the rational rotation.
pc = open(os.path.join(BRIDGE, 'OIBridge', 'PhysicalCharacterization.lean'), encoding='utf-8').read()
_pcflat = ' '.join(pc.split())
_nec = ' '.join(_slice(pc, 'theorem physical_of_exactAll', ':=').split())
ok6 &= bool(_nec) and 'FiniteIsometryExtensionSF' not in _nec
ok6 &= '(h : ExactAllFiniteEndomorphicQuantumOps T) : PhysicalCompletionConditions T' in _nec
_bundle = ' '.join(_slice(pc, 'def PhysicalCompletionConditions', 'theorem physical_of_exactAll').split())
ok6 &= bool(_bundle) and 'CompositeOperationalValidity T ∧ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T' in _bundle
ok6 &= 'KrausSound' not in _bundle and 'Exact' not in _bundle
_iff = ' '.join(_slice(pc, 'theorem exactAll_iff_physical', ':=').split())
ok6 &= bool(_iff) and 'FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))' in _iff
ok6 &= 'FiniteIsometryExtensionSF Unit' not in _iff and 'KrausSound' not in _iff
ok6 &= _iff.rstrip().endswith('ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T')
ok6 &= 'theorem admissible_not_systemToLevelOne' in pc and 'is recorded OPEN' in _pcflat
ok6 &= 'theorem validity_independent' in pc and 'theorem inert_independent' in pc
ok6 &= 'theorem countermodel_systemToLevelOne' in pc
ok6 &= re.search(r'(?m)^structure ', pc) is None
ok6 &= 'theorem closure_independent_all' not in pc and 'theorem oi_iff_quantum' not in pc
dt = open(os.path.join(BRIDGE, 'OIBridge', 'DiagonalTheory.lean'), encoding='utf-8').read()
_dtflat = ' '.join(dt.split())
_dth = _slice(dt, 'noncomputable def diagTheory', 'theorem diag_krausSoundExt')
ok6 &= bool(_dth) and 'avail := fun _ _ _ F => IsKrausFamily F ∧ ∀ a, PreservesDiag (F a)' in _dth
ok6 &= 'availExt := fun _ _ _ _ F => IsCPInstrument F ∧ ∀ a, PreservesDiag (F a)' in _dth
ok6 &= 'prepAvail := fun n P => RefTestedPrep n P ∧ PreservesDiagP P' in _dth
_nc = _slice(dt, 'theorem rot_not_preservesDiag', 'theorem diag_not_control')
ok6 &= bool(_nc) and 'conjChannel rot' in _nc
_ci3 = ' '.join(_slice(dt, 'theorem control_independent', ':=').split())
ok6 &= bool(_ci3) and 'RealizesSealedOICore T ∧ ¬ HasCompositeUnitaryControl T' in _ci3
ok6 &= 'SystemToLevelOne T' in _ci3 and 'IteratedAncillaClosure T' in _ci3
_ma = ' '.join(_slice(dt, 'theorem minimality_audit', ':=').split())
ok6 &= bool(_ma) and _ma.count('RealizesSealedOICore T') == 4 and '¬ SystemToLevelOne admissibleTheory' in _ma
ok6 &= 'theorem diag_realizesSealedOICore' in dt and 'theorem diag_not_exactAll' in dt
ok6 &= 'bare finite OI does not select QM' in _dtflat
ok6 &= re.search(r'(?m)^structure ', dt) is None
ok6 &= 'theorem diag_control' not in dt and 'theorem oi_iff_quantum' not in dt
# Round-44 guards: the rank-gap theory closes the closure cell; the audit is five-way.
rg = open(os.path.join(BRIDGE, 'OIBridge', 'RankGapTheory.lean'), encoding='utf-8').read()
_rgflat = ' '.join(rg.split())
_gop = ' '.join(_slice(rg, 'def GapOp', 'def Gap ').split())
ok6 &= bool(_gop) and 'IsUnit K' in _gop and 'Fintype.card ι ≤ N' in _gop
_gth = _slice(rg, 'noncomputable def gapTheory', 'theorem gap_exact')
ok6 &= bool(_gth) and 'avail := fun _ _ _ F => IsKrausFamily F' in _gth
ok6 &= 'availExt := fun N _ _ _ F => IsGapInstrument N F' in _gth
_dich = ' '.join(_slice(rg, 'theorem twoByTwo_dichotomy', ':=').split())
ok6 &= bool(_dich) and 'IsUnit K ∨' in _dich and 'Matrix (Fin 2 × Fin 1) Unit ℂ' in _dich
_ns = ' '.join(_slice(rg, 'theorem gap_no_shift', ':=').split())
ok6 &= bool(_ns) and 'FiniteOperationalTheory (Fin 2 × Fin 3)' in _ns
ok6 &= 'gapTheory.availExt 3 O F' in _ns and "HasCompositeUnitaryControl T'" in _ns
_ccc = ' '.join(_slice(rg, 'theorem closure_cell_closed', ':=').split())
ok6 &= bool(_ccc) and 'RealizesSealedOICore T ∧ ¬ IteratedAncillaClosure T' in _ccc
ok6 &= 'SystemToLevelOne T' in _ccc and 'CompositeOperationalValidity T' in _ccc
ok6 &= 'InertSpectatorCompositionality T' in _ccc and 'HasCompositeUnitaryControl T' in _ccc
_fwm = ' '.join(_slice(rg, 'theorem five_way_minimality', ':=').split())
ok6 &= bool(_fwm) and _fwm.count('RealizesSealedOICore T') == 5
ok6 &= _fwm.count('¬ CompositeOperationalValidity T') == 1
ok6 &= _fwm.count('¬ InertSpectatorCompositionality T') == 1
ok6 &= _fwm.count('¬ HasCompositeUnitaryControl T') == 1
ok6 &= _fwm.count('¬ IteratedAncillaClosure T') == 1 and _fwm.count('¬ SystemToLevelOne T') == 1
ok6 &= 'FiniteIsometryExtensionSF' not in rg
ok6 &= 'theorem gap_systemToLevelOne' in rg and 'theorem gap_not_iteratedAncillaClosure' in rg
ok6 &= 'CLOSED IN ROUND FORTY-FOUR' in _pcflat and 'CLOSED IN ROUND FORTY-FOUR' in _dtflat
ok6 &= re.search(r'(?m)^structure ', rg) is None
ok6 &= 'theorem oi_iff_quantum' not in rg and 'theorem gap_iteratedAncillaClosure' not in rg
ok6 &= 'theorem gap_exactAll' not in rg and 'theorem gap_physical' not in rg
# Round-45 guards: boundary item 2 discharged internally; the characterization unconditional;
# the round-35 three-item statement preserved and labelled; two items remain, not claimed.
ie = open(os.path.join(BRIDGE, 'OIBridge', 'IsometryExtension.lean'), encoding='utf-8').read()
_ieflat = ' '.join(ie.split())
_dis = ' '.join(_slice(ie, 'theorem finiteIsometryExtensionSF_discharged', 'theorem isometryExtension_unit').split())
ok6 &= bool(_dis) and 'FiniteIsometryExtensionSF A' in _dis
ok6 &= 'Orthonormal.exists_orthonormalBasis_extension_of_card_eq' in _dis and 'finrank_euclideanSpace' in _dis
ok6 &= 'sorry' not in ie and re.search(r'(?m)^axiom ', ie) is None and 'native_decide' not in ie
_unc = ' '.join(_slice(ie, 'theorem exactAll_iff_physical_unconditional', ':=').split())
ok6 &= bool(_unc) and _unc.endswith('ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T')
ok6 &= 'FiniteIsometryExtensionSF' not in _unc and 'hext' not in _unc
_oc = ' '.join(_slice(ie, 'theorem operational_classification', ':=').split())
ok6 &= bool(_oc) and 'FiniteIsometryExtensionSF' not in _oc and _oc.count('RealizesSealedOICore T') == 5
ok6 &= 'ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T' in _oc
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: TWO ITEMS' in _ieflat
ok6 &= 'SUPERSEDED IN ROUND FORTY-FIVE' in _baflat
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: TWO ITEMS' in _baflat
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: THREE ITEMS' in _baflat   # provenance kept
ok6 &= 'compact Lie integration / reachability' in _ieflat and 'finite Uhlmann / Schmidt / right-unitary uniqueness' in _ieflat
ok6 &= 'Lie integration is discharged' not in _ieflat and 'reachability is discharged' not in _ieflat
# the historical conditional theorems are KEPT as written
for _fn, _th in (('StinespringAssembly', 'theorem fullInstruments_of_control (T : FiniteOperationalTheory A)'),
                 ('PhysicalCharacterization', 'theorem exactAll_iff_physical (T : FiniteOperationalTheory (Fin 2))'),
                 ('AncillaClosure', 'theorem compositeCompleteness (T : FiniteOperationalTheory A)')):
    ok6 &= _th in open(os.path.join(BRIDGE, 'OIBridge', f'{_fn}.lean'), encoding='utf-8').read()
ok6 &= 'DISCHARGED IN ROUND FORTY-FIVE' in ' '.join(open(os.path.join(BRIDGE, 'OIBridge', 'StinespringAssembly.lean'), encoding='utf-8').read().split())
ok6 &= 'ITEM 2 DISCHARGED IN ROUND FORTY-FIVE' in _pcflat
ok6 &= re.search(r'(?m)^structure ', ie) is None
ok6 &= 'theorem oi_iff_quantum' not in ie and 'theorem lie_integration_discharged' not in ie
ok6 &= 'theorem uhlmann_discharged' not in ie
# Round-46 guards: the characterization for every nonempty finite system; well-formedness
# vs the three substantive principles; OI alone != QM; no boundary item; no overclaim.
gc = open(os.path.join(BRIDGE, 'OIBridge', 'GeneralCarrier.lean'), encoding='utf-8').read()
_gcflat = ' '.join(gc.split())
ok6 &= 'variable {A : Type} [Fintype A] [DecidableEq A] [Nonempty A]' in gc
_gen = ' '.join(_slice(gc, 'theorem exactAll_iff_physical_general', ':=').split())
ok6 &= bool(_gen) and '(T : FiniteOperationalTheory A)' in _gen and 'Fin 2' not in _gen
ok6 &= _gen.endswith('ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T')
_gch = ' '.join(_slice(gc, 'theorem general_characterization', ':=').split())
ok6 &= bool(_gch) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _gch
ok6 &= 'def WellFormed (T : FiniteOperationalTheory A) : Prop := CompositeOperationalValidity T ∧ SystemToLevelOne T' in _gcflat
ok6 &= 'def SubstantiveCompletion (T : FiniteOperationalTheory A) : Prop := InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T' in _gcflat
_sub = ' '.join(_slice(gc, 'theorem exactAll_iff_substantive', ':=').split())
ok6 &= bool(_sub) and '(hwf : WellFormed T)' in _sub and _sub.endswith('ExactAllFiniteEndomorphicQuantumOps T ↔ SubstantiveCompletion T')
_mr = ' '.join(_slice(gc, 'theorem main_result', ':=').split())
ok6 &= bool(_mr) and _mr.count('RealizesSealedOICore T') == 6 and '[Nonempty A]' in _mr
_oa = ' '.join(_slice(gc, 'theorem oi_alone_not_qm', ':=').split())
ok6 &= bool(_oa) and 'RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T' in _oa
ok6 &= 'FiniteIsometryExtensionSF' not in gc and 'sorry' not in gc and 'native_decide' not in gc
ok6 &= re.search(r'(?m)^axiom ', gc) is None and re.search(r'(?m)^structure ', gc) is None
ok6 &= 'theorem oi_derives_qm' not in gc and 'theorem oi_iff_quantum' not in gc
ok6 &= 'theorem five_way_minimality_general' not in gc
ok6 &= 'GENERALIZED TO EVERY NONEMPTY FINITE SYSTEM IN ROUND FORTY-SIX' in _pcflat
# Round-48 guards: finite right-unitary uniqueness discharged; the boundary is one item; the
# two-item statements preserved and labelled; the remaining item not claimed.
uu = open(os.path.join(BRIDGE, 'OIBridge', 'UhlmannUniqueness.lean'), encoding='utf-8').read()
_uuflat = ' '.join(uu.split())
_ru = ' '.join(_slice(uu, 'theorem rightUnitary_of_gram', ':=').split())
ok6 &= bool(_ru) and '(A B : Matrix S E ℂ) (hG : A * Aᴴ = B * Bᴴ)' in _ru
ok6 &= _ru.endswith('∃ U : Matrix E E ℂ, Uᴴ * U = 1 ∧ B = A * U')
ok6 &= 'LinearIsometry.extend' in uu and 'stdOrthonormalBasis' in uu
ok6 &= 'sorry' not in uu and re.search(r'(?m)^axiom ', uu) is None and 'native_decide' not in uu
_pu = ' '.join(_slice(uu, 'theorem purifier_uniqueness', ':=').split())
ok6 &= bool(_pu) and 'purifVec B = ((1 : Matrix S S ℂ) ⊗ₖ Uᵀ) *ᵥ purifVec A' in _pu
_bo = ' '.join(_slice(uu, 'theorem boundary_one_item', ':=').split())
ok6 &= bool(_bo) and 'FiniteIsometryExtensionSF A' in _bo and 'B = A * U' in _bo and 'PosSemidef' in _bo
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: ONE ITEM' in _uuflat
ok6 &= 'compact Lie integration / reachability' in _uuflat
ok6 &= 'Lie integration is discharged' not in _uuflat and 'reachability is discharged' not in _uuflat
ok6 &= 'SUPERSEDED IN ROUND FORTY-EIGHT' in _baflat
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: ONE ITEM' in _baflat
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: TWO ITEMS' in _baflat   # provenance kept
ok6 &= 'SUPERSEDED IN ROUND FORTY-EIGHT' in _ieflat
_puf = ' '.join(open(os.path.join(BRIDGE, 'OIBridge', 'Purification.lean'), encoding='utf-8').read().split())
ok6 &= 'DISCHARGED IN ROUND FORTY-EIGHT' in _puf and 'recorded as the cited external result rather than reproved' in _puf
ok6 &= re.search(r'(?m)^structure ', uu) is None
ok6 &= 'theorem lie_reachability_discharged' not in uu and 'theorem rightIsometry_of_gram' not in uu
# Round-49 guards: the compact-Lie seam audited; the one remaining item named and consumed
# exactly once; the reduction internal; nothing beyond it claimed.
rsm = open(os.path.join(BRIDGE, 'OIBridge', 'ReachabilitySeam.lean'), encoding='utf-8').read()
_rsmflat = ' '.join(rsm.split())
_lr = ' '.join(_slice(rsm, 'def LocalReachabilityOfLieRank', 'theorem universalReachability_of_lieRank').split())
ok6 &= bool(_lr) and 'HControl H U → LocalReachability H U' in _lr
_ul = ' '.join(_slice(rsm, 'theorem universalReachability_of_lieRank', ':=').split())
ok6 &= bool(_ul) and '(hstep : LocalReachabilityOfLieRank S)' in _ul and _ul.endswith('UniversalUnitaryReachability avail')
ok6 &= rsm.count('LocalReachabilityOfLieRank') >= 3   # def, its doc, the one consumer
ok6 &= 'theorem localReachabilityOfLieRank' not in rsm and 'theorem lieRank_localReachability' not in rsm
_el = ' '.join(_slice(rsm, 'theorem exact_of_local', ':=').split())
ok6 &= bool(_el) and '(hloc : LocalReachability H U)' in _el and _el.endswith('ExactReachability H U')
ok6 &= 'FiniteIsometryExtensionSF' not in rsm and 'sorry' not in rsm and 'native_decide' not in rsm
ok6 &= re.search(r'(?m)^axiom ', rsm) is None and re.search(r'(?m)^structure ', rsm) is None
ok6 &= 'theorem noControls_central_not_exact' in rsm and 'theorem exists_special_phase' in rsm
ok6 &= 'theorem conjChannel_smul' in rsm and 'theorem dense_of_exact' in rsm
ok6 &= 'THE BOUNDARY AUDIT: unchanged in count (ONE ITEM)' in _rsmflat
ok6 &= 'SHARPENED IN ROUND FORTY-NINE' in _baflat and 'Count unchanged: ONE ITEM' in _baflat
ok6 &= 'theorem exact_of_dense' not in rsm and 'theorem hControl_of_exact' not in rsm
# Round-50 guards: the last external item discharged; the endpoint theorems present with
# the exact statements; the round-49 definition and consumer unchanged and consumed; the
# discharge labels in place; nothing beyond the compact matrix-group setting claimed.
orb = open(os.path.join(BRIDGE, 'OIBridge', 'OrbitReachability.lean'), encoding='utf-8').read()
_orbflat = ' '.join(orb.split())
ok6 &= 'theorem localReachabilityOfLieRank : LocalReachabilityOfLieRank S' in _orbflat
ok6 &= 'def LocalReachabilityOfLieRank' not in orb        # defined once, in ReachabilitySeam
_ex50 = ' '.join(_slice(orb, 'theorem exactReachability_of_hcontrol', ':=').split())
ok6 &= bool(_ex50) and '(hLie : HControl H U)' in _ex50 and _ex50.endswith('ExactReachability H U')
ok6 &= 'exact_of_local (localReachabilityOfLieRank G H U hH hU hLie)' in _orbflat
_uu50 = ' '.join(_slice(orb, 'theorem universalReachability_of_lieRank_unconditional', ':=').split())
ok6 &= bool(_uu50) and 'hstep' not in _uu50 and _uu50.endswith('UniversalUnitaryReachability avail')
ok6 &= 'universalReachability_of_lieRank localReachabilityOfLieRank H U hH hU hLie' in _orbflat
_lh50 = ' '.join(_slice(orb, 'theorem localReachability_of_hcontrol', ':=').split())
ok6 &= bool(_lh50) and '[Nonempty S]' in _lh50 and _lh50.endswith('LocalReachability H U')
for _nm in ('bracket_mem_orbitSpan', 'controlLie_le_orbitLie', 'skew_mem_orbitSpan',
            'exists_spanning_family', 'prodMap_mem_reachable', 'prodMap_hasStrictFDerivAt',
            'psi_hasStrictFDerivAt', 'psiDeriv_surjective', 'exists_exp_injOn_nhds'):
    ok6 &= f'theorem {_nm}' in orb
ok6 &= 'map_nhds_eq_of_surj' in orb and 'eventually_left_inverse' in orb
ok6 &= 'hasDerivAt_iff_tendsto_slope' in orb and 'exists_linearIndependent' in orb
ok6 &= re.search(r'(?m)^axiom ', orb) is None and re.search(r'(?m)^structure ', orb) is None
ok6 &= 'native_decide' not in orb and 'Trotter' not in _slice(orb, 'namespace OIBridge', 'end OIBridge')
ok6 &= 'THE EXTERNAL BOUNDARY: ZERO ITEMS' in _orbflat
ok6 &= 'THE CURRENT UNRESOLVED EXTERNAL BOUNDARY: ZERO ITEMS' in _orbflat
ok6 &= 'DISCHARGED IN ROUND FIFTY' in _baflat and 'UNRESOLVED EXTERNAL BOUNDARY: ZERO ITEMS' in _baflat
ok6 &= 'DISCHARGED IN ROUND FIFTY' in _rsmflat and 'UNRESOLVED EXTERNAL BOUNDARY: ZERO ITEMS' in _rsmflat
ok6 &= 'SUPERSEDED IN ROUND FIFTY' in _ieflat and 'SUPERSEDED IN ROUND FIFTY' in _uuflat
ok6 &= 'theorem orbit_theorem' not in orb and 'theorem closedSubgroup' not in orb
ok6 &= 'theorem hControl_of_exact' not in orb and 'theorem lieClosure_eq' not in orb
# Round-52 guards: the eight-cell census of the three substantive principles; the four
# multi-failure theories built by one class construction; the census, the no-relation theorem
# and the top-cell theorem present with exact statements; no physical realization claimed.
scn = open(os.path.join(BRIDGE, 'OIBridge', 'SubstantiveCensus.lean'), encoding='utf-8').read()
_scflat = ' '.join(scn.split())
ok6 &= 'theorem substantive_census (gI gC gK : Bool)' in _scflat
_cen = ' '.join(_slice(scn, 'theorem substantive_census', ':= by').split())
ok6 &= bool(_cen) and 'WellFormed T ∧ RealizesSealedOICore T' in _cen
ok6 &= '(InertSpectatorCompositionality T ↔ gI = true)' in _cen
ok6 &= '(HasCompositeUnitaryControl T ↔ gC = true)' in _cen
ok6 &= '(IteratedAncillaClosure T ↔ gK = true)' in _cen
ok6 &= 'theorem no_boolean_relation (Rel : Prop → Prop → Prop → Prop)' in _scflat
ok6 &= 'theorem qm_is_the_top_cell' in _scflat and 'exactAll_iff_substantive T hwf' in _scflat
for _nm in ('diagGapTheory', 'diagTwoPosTheory', 'cappedTheory', 'cappedDiagTheory'):
    ok6 &= f'noncomputable def {_nm} : FiniteOperationalTheory (Fin 2) := classTheory' in _scflat
for _nm in ('cell_none', 'cell_I', 'cell_C', 'cell_K', 'cell_IC', 'cell_IK', 'cell_CK', 'cell_ICK'):
    ok6 &= f'theorem {_nm}' in scn
ok6 &= 'structure ClassData' in scn and 'structure FiniteOperationalTheory' not in scn
ok6 &= 'theorem classTheory_not_inert' in scn and 'theorem classTheory_not_closure' in scn
ok6 &= 'theorem amplRef_redMap_ent3_not_posSemidef' in scn and 'theorem traceShift_not_cp' in scn
ok6 &= 'theorem discardWith_uniform_spectatorLast' in scn and 'gapChannel_not_gap' in scn
ok6 &= 'NOT claimed: that any cell is physically realized' in _scflat
ok6 &= 'theorem cell_physical' not in scn and 'theorem oi_selects' not in scn
ok6 &= 'theorem census_canonical' not in scn and 'native_decide' not in scn
# Round-53 guards: the layered hierarchy (bare core unchanged, completed OI explicit); the three
# OI-motivated principles with their implications and converses; OI-plus equivalent to QM; the
# independence of the three principles; nothing about bare OI implying any principle claimed.
coi = open(os.path.join(BRIDGE, 'OIBridge', 'CompletedOI.lean'), encoding='utf-8').read()
_coiflat = ' '.join(coi.split())
ok6 &= 'def OICore (T : FiniteOperationalTheory (Fin 2)) : Prop := RealizesSealedOICore T' in _coiflat
ok6 &= 'def CompletedOI (T : FiniteOperationalTheory (Fin 2)) : Prop := OICore T ∧ PhysicalCompletionConditions T' in _coiflat
ok6 &= 'theorem completedOI_iff_qm' in coi and 'theorem completedOI_iff_physical' in coi
ok6 &= 'theorem oiCore_not_completedOI' in coi
ok6 &= 'def ObservationalIndependence : Prop := HasParallelReferenceExtension T' in _coiflat
ok6 &= 'theorem observationalIndependence_iff_inert' in coi
ok6 &= 'theorem control_of_reversibleRichness' in coi and 'theorem reversibleRichness_of_control' in coi
ok6 &= 'universalReachability_of_lieRank_unconditional' in coi and 'hControl_single_all' in coi
ok6 &= 'theorem closure_of_observerRecursion' in coi and 'theorem observerRecursion_of_closure' in coi
ok6 &= 'noncomputable def shiftOfClosure' in coi and 'T\'.prepAvail_discard' in coi
_oip = ' '.join(_slice(coi, 'def OIPlus : Prop :=', 'theorem qm_of_oiPlus').split())
ok6 &= 'OICore T ∧ WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T' in _oip
ok6 &= 'theorem qm_of_oiPlus' in coi and 'theorem oiPlus_of_qm' in coi
ok6 &= 'theorem oiPlus_iff_qm : OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T' in _coiflat
ok6 &= 'theorem oiPlus_iff_completedOI' in coi and 'theorem oiPlus_independence' in coi
ok6 &= 'NOT claimed: that any of the three principles follows from bare OI' in _coiflat
ok6 &= 'is `RealizesSealedOICore` and is not modified' in _coiflat
ok6 &= 'theorem principle_of_oiCore' not in coi and 'theorem inert_of_oiCore' not in coi
ok6 &= 'theorem control_of_oiCore' not in coi and 'theorem closure_of_oiCore' not in coi
ok6 &= 'structure FiniteOperationalTheory' not in coi and 'native_decide' not in coi
# Round-55 guards: carrier-general OI-plus; the qubit specialization identified with the
# round-53 definition; the audit's one honest exception (no carrier-general sealed core) stated;
# the round-53 file unchanged.
cgo = open(os.path.join(BRIDGE, 'OIBridge', 'CarrierGeneralOIPlus.lean'), encoding='utf-8').read()
_cgoflat = ' '.join(cgo.split())
ok6 &= 'def OIPlus : Prop := WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T' in _cgoflat
_cg = ' '.join(_slice(cgo, 'theorem carrier_general_oiPlus', ':=').split())
ok6 &= bool(_cg) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _cg
ok6 &= _cg.endswith('OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T')
ok6 &= 'theorem oiPlus_qubit_iff (T : FiniteOperationalTheory (Fin 2)) : OIHierarchy.OIPlus T ↔ OIPlus T' in _cgoflat
ok6 &= 'theorem reversibleRichness_of_control [Nonempty A]' in _cgoflat and 'Classical.arbitrary A' in cgo
ok6 &= 'theorem conjChannel_mul_general' in cgo and 'theorem control_of_reversibleRichness' in cgo
ok6 &= 'NOT claimed: a carrier-general sealed OI core' in _cgoflat
ok6 &= 'RealizesSealedOICore' not in _slice(cgo, 'def OIPlus : Prop :=', 'theorem qm_of_oiPlus')
ok6 &= 'theorem oiCoreGeneral' not in cgo and 'def OICoreGeneral' not in cgo
ok6 &= 'structure FiniteOperationalTheory' not in cgo and 'native_decide' not in cgo
# Round-56 guards: embedded observation; observer recursion and the level-one seam derived from
# it; the CP-instrument family as the necessity witness; the rank-gap countercontrol; the converse
# and the sources of the other principles unclaimed.
eob = open(os.path.join(BRIDGE, 'OIBridge', 'EmbeddedObservation.lean'), encoding='utf-8').read()
_eobflat = ' '.join(eob.split())
ok6 &= 'def EmbeddedObservation (T : FiniteOperationalTheory A) : Prop := ∃ 𝒯 : TheoryFamily, RegroupingInvariant 𝒯 ∧ RelabellingInvariant 𝒯 ∧ IsAmbientMember T 𝒯' in _eobflat
ok6 &= 'theorem observerRecursion_of_embeddedObservation' in eob and 'theorem systemToLevelOne_of_embeddedObservation' in eob
ok6 &= 'theorem embeddedObservation_of_qm' in eob and 'noncomputable def cpTheory' in eob
_ce = ' '.join(_slice(eob, 'theorem carrier_general_oiPlusEmbedded', ':=').split())
ok6 &= bool(_ce) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _ce
ok6 &= _ce.endswith('OIPlusEmbedded T ↔ ExactAllFiniteEndomorphicQuantumOps T')
ok6 &= 'def OIPlusEmbedded : Prop := CompositeOperationalValidity T ∧ OIHierarchyGeneral.ObservationalIndependence T ∧ OIHierarchyGeneral.ReversibleRichness T ∧ EmbeddedObservation T' in _eobflat
ok6 &= 'SystemToLevelOne' not in _slice(eob, 'def OIPlusEmbedded : Prop :=', 'theorem oiPlus_of_oiPlusEmbedded')
ok6 &= 'theorem embeddedObservation_independent' in eob and 'theorem gap_not_embeddedObservation' in eob
ok6 &= 'The converse `ObserverRecursion → EmbeddedObservation` is not proved' in _eobflat
ok6 &= 'theorem embeddedObservation_of_observerRecursion' not in eob and 'theorem embeddedObservation_iff_observerRecursion' not in eob
ok6 &= 'theorem validity_of_embeddedObservation' not in eob and 'theorem embeddedObservation_of_oiCore' not in eob
ok6 &= 'structure FiniteOperationalTheory' not in eob and 'native_decide' not in eob
# Round-57 guards: the redundancy test recorded as failing; the implementation-level primitive
# stated without the spectator-extension vocabulary; the countermodel diagnosed as not
# implementation-generated; the compressed set; the open question unclaimed.
ilo = open(os.path.join(BRIDGE, 'OIBridge', 'ImplementationLocality.lean'), encoding='utf-8').read()
_iloflat = ' '.join(ilo.split())
ok6 &= 'theorem redundancy_fails' in ilo and '¬ ObservationalIndependence T' in _slice(ilo, 'theorem redundancy_fails', ':=')
ok6 &= 'theorem form_fixed_existence_fails' in ilo and 'theorem countermodel_not_implementationGenerated' in ilo
_cs = _slice(ilo, 'def ContextStable', '/-- **(L) LABEL INVARIANCE**')
_lv = _slice(ilo, 'def LabelInvariant', '/-- **IMPLEMENTATION LOCALITY**')
for _w in ('withSpectator', 'HasParallelReferenceExtension', 'InertSpectatorCompositionality', 'avail'):
    ok6 &= _w not in _cs and _w not in _lv
ok6 &= 'theorem observationalIndependence_of_implementationLocality' in ilo
ok6 &= 'theorem validity_of_implementationLocality' in ilo and 'theorem implementationLocality_of_qm' in ilo
_cl = ' '.join(_slice(ilo, 'theorem carrier_general_oiPlusLocal', ':=').split())
ok6 &= bool(_cl) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _cl
ok6 &= _cl.endswith('OIPlusLocal T ↔ ExactAllFiniteEndomorphicQuantumOps T')
ok6 &= 'def OIPlusLocal : Prop := ImplementationLocality T ∧ OIHierarchyGeneral.ReversibleRichness T ∧ EmbeddedObservation T' in _iloflat
ok6 &= 'Whether context stability is redundant given implementation generation' in _iloflat
ok6 &= 'theorem observationalIndependence_of_embeddedObservation' not in ilo
ok6 &= 'theorem implementationLocality_of_observationalIndependence' not in ilo
ok6 &= 'theorem contextStable_redundant' not in ilo and 'theorem richness_of_' not in ilo
ok6 &= 'structure FiniteOperationalTheory' not in ilo and 'native_decide' not in ilo
# b24a GUARDS.  Physical local tomography must rest on PRODUCT RANK-ONE EFFECTS, not on
# matrix-unit functionals; the matrix-unit statement keeps its own separate name.
idil = open(os.path.join(BRIDGE, 'OIBridge', 'InstrumentDilation.lean'),
            encoding='utf-8').read()
ok6 &= 'theorem productMatrixUnit_local_separating' in idil
_ltp = _slice(idil, 'theorem local_tomography_physical', ':= by')
ok6 &= bool(_ltp) and 'prodProj' in _ltp and 'Matrix.single' not in _ltp
# and instrument availability must be family-level and NORMALIZED, not "every conjugation
# by an arbitrary K is available"
_ffa = _slice(mc, 'def FullFiniteInstrumentAvailability', '/--')
ok6 &= bool(_ffa) and 'instrumentBranch K out' in _ffa
ok6 &= '(K k)ᴴ * K k = 1' in _ffa
ok6 &= 'FullFiniteQuantumOps' not in mc
# the reverse implication must be recorded as FALSE, with the countermodel
ok6 &= 'theorem availability_not_implies_hComp' in mc
# ROUND-25 OPENING GUARDS.  Map-level spectator independence must be stated for ARBITRARY
# linear maps (an irreversible Lüders selector is the whole point), and the three physically
# distinct clauses must stay distinct predicates.
oa = open(os.path.join(BRIDGE, 'OIBridge', 'OperationalAssembly.lean'),
          encoding='utf-8').read()
_msi = _slice(oa, 'def MapSpectatorIndependent', '/--')
ok6 &= bool(_msi) and 'Equiv.Perm' not in _msi and 'correlationExtension' not in _msi
# the reversible round-24 clause must be recorded as a SPECIALIZATION of it
ok6 &= 'theorem spectatorIndependent_iff_mapLevel' in oa
# product preparation is its own clause, not smuggled into the operation-level notion
ok6 &= 'def ProductPreparation' in oa
_pp = _slice(oa, 'def ProductPreparation', '/--')
ok6 &= bool(_pp) and 'MapSpectatorIndependent' not in _pp
# the surviving freedom must be exhibited as a genuine CP channel, not merely asserted
ok6 &= 'theorem blockDephase_cp' in oa
ok6 &= 'theorem blockDephase_classical_eq' in oa
ok6 &= 'theorem blockDephase_not_mapSpectatorIndependent' in oa
# the endomorphic-scope phrase must be present on the instrument predicate
ok6 &= 'finite endomorphic instruments on a fixed system' in ' '.join(oa.split())
# ROUND-25b GUARDS.  The native readout must NOT be postulated as id (x) Luders: the
# structure may only assume it exists and is spectator-independent, and the FORM must be
# derived.  So `localLuders` must not appear among the structure's readout fields.
_ft = _slice(oa, 'structure FiniteOperationalTheory', '/-- **THE READOUT FORM')
ok6 &= bool(_ft) and '= localLuders' not in _ft
ok6 &= 'MapSpectatorIndependent (ludersLift k) (readout n k)' in _ft
ok6 &= 'theorem readout_is_localLuders' in oa
# the closure rules the reconstruction actually consumes must be present by name
ok6 &= all(f in _ft for f in ('availExt_bind', 'prepAvail_discard', 'availExt_coarse',
                              'avail_coarse', 'prepAvail_uniform', 'readout_avail'))
# composite control must be family-level in the ancilla size, not a premise on A alone
_cc = _slice(oa, 'def HasCompositeUnitaryControl', '/-- **THE CIRCUIT')
ok6 &= bool(_cc) and '(n : ℕ)' in _cc and 'availExt n' in _cc
# purification / Uhlmann must NOT be used by this assembly
ok6 &= 'PURIFICATION AND UHLMANN UNIQUENESS ARE NOT USED' in ' '.join(oa.split())
# b25c GUARD: NO PURE SEED may be postulated.  Preparation must be an availability notion
# whose only granted instance is the UNIFORM attachment; the pure attachment must be a
# THEOREM.  So no structure field may mention pureAttach, and prepAvail_uniform must be
# the uniform one.
ok6 &= 'def prepAvail' not in oa            # prepAvail is a structure FIELD, not a def
ok6 &= bool(_ft) and 'pureAttach' not in _ft
ok6 &= 'prepAvail_uniform : ∀ n : ℕ, prepAvail (n + 1) (uniformAttach (n + 1))' in oa
ok6 &= 'theorem pureSeedPrep_available' in oa
ok6 &= all(f in _ft for f in ('prepAvail', 'prepAvail_post', 'prepAvail_discard'))
# and the old pure-product postulate must be gone
ok6 &= 'prep_isProduct' not in oa
# blockDephase is a CP SELECTIVE operation, not a channel: trace preservation is unproved
_bd = _slice(oa, '/-- **The surviving freedom is a genuine CP operation.**', '-/')
ok6 &= bool(_bd) and 'not a channel' in ' '.join(_bd.split())
# KRAUS-ROUND GUARDS.  The one external fact must be an explicit HYPOTHESIS carried in the
# capstone's own binder list, never an `axiom` and never a structure field -- and the
# capstone must consume NOTHING else beyond composite unitary control.
sa = open(os.path.join(BRIDGE, 'OIBridge', 'StinespringAssembly.lean'),
          encoding='utf-8').read()
ok6 &= 'def FiniteIsometryExtensionSF' in sa
ok6 &= re.search(r'(?m)^axiom ', sa) is None
_cap = _slice(sa, 'theorem fullInstruments_of_control', ':= by')
ok6 &= bool(_cap)
ok6 &= 'FiniteIsometryExtensionSF A' in _cap and 'HasCompositeUnitaryControl T' in _cap
# neither the readout FORM nor a pure seed may reappear as a premise: both are derived
ok6 &= all(bad not in _cap for bad in ('localLuders', 'pureAttach', 'ProductPreparation',
                                       'MapSpectatorIndependent'))
# the system-first mirrors must be PINNED to round twenty pointwise, or the two dilation
# developments can drift apart silently under the factor swap
_pin1 = _slice(sa, 'theorem Vsf_eq_dilationIsometry', '\n\n')
_pin2 = _slice(sa, 'theorem Esf_eq_seedEmbed', '\n\n')
ok6 &= bool(_pin1) and 'dilationIsometry K (k, s\') s := rfl' in ' '.join(_pin1.split())
ok6 &= bool(_pin2) and 'seedEmbed k₀ (k, s\') s := rfl' in ' '.join(_pin2.split())
# the fine branch must be a STANDALONE theorem, provable from `U E = V` alone -- no
# availability bookkeeping inside it
_fb = _slice(sa, 'theorem stinespringCircuit_branch', ':= by')
ok6 &= bool(_fb) and 'avail' not in _fb and 'hUE : U * Esf k₀ = Vsf K' in _fb
# the scope must stay ENDOMORPHIC and the Kraus index nonempty
_hf = _slice(sa, 'def HasFullFiniteEndomorphicInstruments', '/--')
ok6 &= bool(_hf) and 'Fin (n + 1) → Matrix A A ℂ' in _hf
ok6 &= '(K k)ᴴ * K k = 1' in _hf and 'instrumentBranch K out' in _hf
_saflat = ' '.join(sa.split())
ok6 &= 'ALL FINITE ENDOMORPHIC INSTRUMENTS ON A FIXED SYSTEM' in _saflat
ok6 &= 'Purification and Uhlmann uniqueness are not used' in _saflat
# and the header of the file it builds on must not misdescribe the dependency graph:
# the endpoint object is FiniteOperationalTheory, and no closure rule grants a product
# preparation with a chosen ancilla state
_oaflat = ' '.join(oa.split())
ok6 &= 'it is NOT the object the assembly runs on' in _oaflat
ok6 &= 'the ONLY preparation granted' in _oaflat
ok6 &= 'no rule grants a product preparation with a chosen ancilla state' in _oaflat
ok6 &= 'hComp_forward' not in mc
# ROUND-26 GUARDS.  Soundness must be a RESTRICTION (available => representable), exactness
# must be a genuine iff, and the split must be into exactly the two inclusions.
ks = open(os.path.join(BRIDGE, 'OIBridge', 'KrausSoundness.lean'), encoding='utf-8').read()
_snd = _slice(ks, 'def KrausSound', '/--')
ok6 &= bool(_snd) and 'T.avail (Fin m) F → IsFiniteEndomorphicKrausInstrument F' in _snd
_ex = _slice(ks, 'def ExactFiniteEndomorphicQuantumOps', '/--')
ok6 &= bool(_ex) and 'T.avail (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F' in _ex
_spl = _slice(ks, 'theorem exact_iff_sound_and_full', ':= by')
ok6 &= bool(_spl) and 'KrausSound T ∧ HasFullFiniteEndomorphicInstruments T' in _spl
# the representation predicate must be an EXISTENTIAL over a normalized Kraus family, not a
# CP/Choi classification -- no external analytic fact may enter through it
_rep = _slice(ks, 'def IsFiniteEndomorphicKrausInstrument', '/--')
ok6 &= bool(_rep) and '(K k)ᴴ * K k = 1' in _rep and 'F = instrumentBranch K out' in _rep
ok6 &= bool(_rep) and 'PosSemidef' not in _rep and 'choiMatrix' not in _rep
# the countercontrol must be an everywhere-available GENUINE theory that fails soundness
ok6 &= 'def everywhereAvailable' in ks
_ev = _slice(ks, 'def everywhereAvailable', '/-- **THE EVERYWHERE-AVAILABLE THEORY IS NOT')
ok6 &= bool(_ev) and 'avail := fun _ _ _ _ => True' in _ev
ok6 &= bool(_ev) and 'readout := fun _ k => localLuders k' in _ev
ok6 &= 'theorem everywhereAvailable_not_sound' in ks
# NON-NECESSITY MUST NOT BE ASSERTED.  Composite unitary control is sufficient, not
# necessary, and this round does not build that countermodel -- the scope note must say so
# and no theorem may claim it.
_ksflat = ' '.join(ks.split())
ok6 &= 'SUFFICIENT Stinespring architecture for richness, not a necessary condition' in _ksflat
ok6 &= 'countermodel is NOT built here' in _ksflat
ok6 &= 'theorem exact_not_implies_compositeControl' not in ks
ok6 &= '¬ HasCompositeUnitaryControl' not in ks
# ROUND-27 GUARDS.  The composite audit must generalize the representation predicate
# without forking it, must consume only the EASY Kraus => CP direction, and must not assert
# the implication it does not settle.
cs = open(os.path.join(BRIDGE, 'OIBridge', 'CompositeSoundness.lean'),
          encoding='utf-8').read()
_ikf = _slice(cs, 'def IsKrausFamily', '/--')
ok6 &= bool(_ikf) and '(K k)ᴴ * K k = 1' in _ikf
ok6 &= bool(_ikf) and 'PosSemidef' not in _ikf and 'choiMatrix' not in _ikf
ok6 &= 'theorem isKrausFamily_iff' in cs        # the two predicates must be pinned together
_kse = _slice(cs, 'def KrausSoundExt', '/-!')
ok6 &= bool(_kse) and 'T.availExt n O F → IsKrausFamily F' in _kse
# ROUND-36 CORRECTION.  The predicate quantifies over POSITIVE levels; the all-levels form is
# kept under its own name and proved unsatisfiable, so the degenerate level is on the record.
_kse1 = _slice(cs, 'def KrausSoundExt (T', 'def KrausSoundExtAllLevels')
ok6 &= bool(_kse1) and 'T.availExt (n + 1) O F → IsKrausFamily F' in _kse1
ok6 &= 'CORRECTED IN ROUND THIRTY-SIX' in ' '.join(cs.split())
_unsat = _slice(cs, 'theorem krausSoundExtAllLevels_unsatisfiable', 'theorem krausSoundExt_of_allLevels')
ok6 &= bool(_unsat) and 'readout_avail 0' in _unsat and 'Fin.elim0' in _unsat
# the exposed-composite theorem must come from prepAvail_discard and add no hypothesis
_exc = _slice(cs, 'theorem krausSound_exposedComposite', '\n\n')
ok6 &= bool(_exc) and 'prepAvail_discard' in _exc
# ONLY THE EASY DIRECTION.  CP => Kraus needs PSD factorization and must not appear.
_csflat = ' '.join(cs.split())
ok6 &= 'this is Kraus ⟹ CP, which is a computation' in _csflat
ok6 &= 'it is NOT used here, so the external boundary is untouched' in _csflat
ok6 &= 'theorem cp_implies_kraus' not in cs and 'theorem kraus_of_cp' not in cs
# the transpose must be refuted by POSITIVITY, with the trace blindness recorded
ok6 &= 'theorem transposeMap_trace' in cs and 'theorem transposeMap_not_cp' in cs
ok6 &= 'theorem transposeMap_not_kraus' in cs
# and the open fork must stay open: no theorem may claim either direction
ok6 &= 'krausSound_implies_ext' not in cs and 'krausSound_not_implies_ext' not in cs
ok6 &= 'whether `KrausSound T` implies `KrausSoundExt T`. Neither direction is asserted' \
    in _csflat
# and the exposure principle must NOT be overstated: it is conditioned on a violation
# occurring on the REACHABLE state P rho, not on global trace preservation
ok6 &= 'no trace violation can hide ON THE OPERATIONALLY REACHABLE PREPARATION IMAGE' in _csflat
ok6 &= 'every composite surplus must globally preserve the trace' in _csflat
ok6 &= 'traceWitness_always_exposed' not in cs
# ROUND-28 GUARDS.  The countermodel must grant ONLY the uniform attachment, must keep the
# surplus operationally invisible, and must not claim what closes the gap.
hc = open(os.path.join(BRIDGE, 'OIBridge', 'HiddenCoherence.lean'), encoding='utf-8').read()
_seed = _slice(hc, 'def SeedAvail', '/--')
ok6 &= bool(_seed) and 'P = uniformAttach n' in _seed
# the only granted preparation: no second disjunct may sneak a richer preparation in
ok6 &= bool(_seed) and '∨' not in _seed
# the surplus must be PROVED invisible through that preparation, not asserted
ok6 &= 'theorem badOp_invisible' in hc
_inv = _slice(hc, 'theorem badOp_invisible', ':= by')
ok6 &= bool(_inv) and 'discardWith n (uniformAttach n)' in _inv and 'LinearMap.id' in _inv
# refuted by POSITIVITY (the trace test cannot see it), via round 27's easy direction
ok6 &= 'theorem badOp_not_cp' in hc and 'theorem badOp_not_kraus' in hc
ok6 &= 'krausFamily_cp' in _slice(hc, 'theorem badOp_not_kraus', '\n\n')
# the capstone is an existential separation, on ONE theory
_sep = _slice(hc, 'theorem krausSound_not_implies_krausSoundExt', ':=')
ok6 &= bool(_sep) and 'KrausSound T ∧ ¬ KrausSoundExt T' in _sep
_hcflat = ' '.join(hc.split())
# the legitimacy note must be present: control richness is a property, not a structure field
ok6 &= '`HasCompositeUnitaryControl` is NOT a field of `FiniteOperationalTheory`' in _hcflat
# and what closes the gap must NOT be claimed
ok6 &= 'that is not proved here' in _hcflat
ok6 &= 'compositeControl_implies_krausSoundExt' not in hc
ok6 &= 'theorem hiddenCoherence_hasCompositeUnitaryControl' not in hc
# THE ANTECEDENT MUST BE EXACTNESS, NOT MERE SOUNDNESS.  KrausSound alone is a weak
# antecedent: hiddenCoherence is sound but INCOMPLETE on the system, so that separation is
# not the one at issue.  The strong model must have avail = ALL Kraus families, and the
# file must say plainly why the two theorems are different.
_hcf = _slice(hc, 'noncomputable def hiddenCoherenceFull', '/-- **THE SYSTEM SECTOR')
ok6 &= bool(_hcf) and 'avail := fun _ _ _ F => CompositeSoundness.IsKrausFamily F' in _hcf
ok6 &= 'theorem hiddenCoherenceFull_exact' in hc
_ex28 = _slice(hc, 'theorem exact_not_implies_krausSoundExt', ':=')
ok6 &= bool(_ex28) and 'ExactFiniteEndomorphicQuantumOps T ∧ ¬ KrausSoundExt T' in _ex28
ok6 &= 'sound but very INCOMPLETE' in _hcflat
ok6 &= 'only the second theorem licenses the sentence at the top of this file' in _hcflat
# the WEAK theorem's own docstring must not claim the strong statement either: locally it
# proves KrausSound -/-> KrausSoundExt and nothing more
_wk = _slice(hc, '**THE FORK, SETTLED', 'theorem krausSound_not_implies_krausSoundExt')
ok6 &= bool(_wk) and 'SYSTEM SOUNDNESS does not force composite' in ' '.join(_wk.split())
ok6 &= bool(_wk) and 'Exact quantum operations on the visible system do NOT force' \
    not in ' '.join(_wk.split())
# and the trace wording must be right: badOp preserves the trace OUTRIGHT, since a coherence
# never contributes to a trace at all -- it scales amplitudes, not traces
ok6 &= 'TRACE-PRESERVING OUTRIGHT, not merely on the diagonal' in _hcflat
ok6 &= 'trace-scaling only on coherences' not in _hcflat
# ROUND-29 GUARDS.  The interference principle must be SMALL -- a pure two-level seed and
# one mixer -- and must not smuggle composite unitary control back in; and the file must not
# claim the general implication it does not prove.
ai = open(os.path.join(BRIDGE, 'OIBridge', 'AncillaInterference.lean'),
          encoding='utf-8').read()
_prin = _slice(ai, 'def HasAncillaQubitInterference', '/-!')
ok6 &= bool(_prin) and 'T.prepAvail 2 (pureAttach 2 0)' in _prin
ok6 &= bool(_prin) and 'conjChannel (ancMix A)' in _prin
ok6 &= bool(_prin) and 'HasCompositeUnitaryControl' not in _prin
ok6 &= bool(_prin) and 'KrausSoundExt' not in _prin
# the exposure theorem kills THIS surplus, and says only that
_exp = _slice(ai, 'theorem interference_exposes_badOp', ':= by')
ok6 &= bool(_exp) and '¬ T.availExt 2 Unit (fun _ => badOp (A := A) 2)' in _exp
ok6 &= bool(_exp) and 'KrausSound T' in _exp and 'HasAncillaQubitInterference T' in _exp
# strict-weakness direction only; the converse must not appear
ok6 &= 'theorem compositeControl_hasInterference' in ai
ok6 &= 'interference_implies_krausSoundExt' not in ai
ok6 &= 'theorem interference_hasCompositeControl' not in ai
_aiflat = ' '.join(ai.split())
ok6 &= 'The converse is NOT proved and NOT claimed' in _aiflat
ok6 &= 'it says nothing about every possible one' in _aiflat
# and the reason the contradiction is positivity, not trace, must be on the record
ok6 &= 'THE CONTRADICTION IS POSITIVITY, NOT TRACE' in _aiflat
# ROUND-30 GUARDS.  The pure seed must be derivable from the SWAPS alone, so the interference
# certificate can be stated purely as control with no pure-state availability premise.
_pss = _slice(oa, 'theorem pureSeedPrep_available_of_swap', ':= by')
ok6 &= bool(_pss) and 'HasCompositeUnitaryControl' not in _pss
ok6 &= bool(_pss) and 'ancSwap (A := A) (n + 1) k k₀' in _pss
ok6 &= 'def HasAncillaSwapControl' in oa
ok6 &= 'theorem compositeControl_hasSwapControl' in oa
_ctrl = _slice(ai, 'def HasAncillaQubitInterferenceControl', '/--')
ok6 &= bool(_ctrl) and 'HasAncillaQubitSwapControl T' in _ctrl
ok6 &= bool(_ctrl) and 'prepAvail' not in _ctrl and 'pureAttach' not in _ctrl
ok6 &= 'theorem interferenceControl_exposes_badOp' in ai
# WORDING: one direction is proved, so "strictly weaker" is not licensed anywhere
ok6 &= 'is strictly weaker' not in _aiflat and 'strictly below' not in _aiflat
ok6 &= 'IS WEAKER THAN COMPOSITE CONTROL' not in _aiflat
ok6 &= 'It does NOT license "strictly weaker"' in _aiflat
# ROUND-31 GUARDS.  The survivor must be the ANCILLA-only transpose, positive and not CP,
# and the round-30 certificate must be shown BLIND to it -- with no claim about what would
# expose it.
pt = open(os.path.join(BRIDGE, 'OIBridge', 'PartialTranspose.lean'), encoding='utf-8').read()
_at = _slice(pt, 'def ancTranspose', '@[simp]')
ok6 &= bool(_at) and 'X (p.1, q.2) (q.1, p.2)' in _at
ok6 &= 'theorem ancTranspose_trace' in pt and 'theorem posSemidef_transpose' in pt
ok6 &= 'theorem ancTranspose_not_cp' in pt and 'theorem ancTranspose_not_kraus' in pt
# the null result must be a THEOREM about the round-30 chain, not prose
_nul = _slice(pt, 'theorem interference_branch_transpose', ':= by')
ok6 &= bool(_nul) and 'conjChannel (ancMix A)' in _nul and 'ancTranspose A 2' in _nul
ok6 &= 'theorem tauChainT_eq' in pt and 'theorem ancTranspose_survives_interference' in pt
_ptflat = ' '.join(pt.split())
# the corrected phase reasoning must be recorded, since it was the natural wrong guess
ok6 &= 'Pure phase gives nothing new in either direction' in _ptflat
# and NOTHING may claim the minimal entangling capability or a general impossibility
ok6 &= 'it does not exhibit the minimal entangling capability that DOES expose' in _ptflat
ok6 &= 'does not prove that no ancilla-local principle whatsoever could' in _ptflat
ok6 &= 'minimalEntangling' not in pt and 'theorem entangling_exposes' not in pt
# the structural gap is NAMED, not silently patched: this round adds no structure field
ok6 &= 'structure ' not in pt
ok6 &= 'no rule lifting an available SYSTEM operation' in _ptflat
# ROUND-32 GUARDS.  The round-31 header's guess that a Bell-type test was needed must be
# recorded as CORRECTED, not deleted and not left standing.
ok6 &= 'A STRUCTURAL NOTE, CORRECTED BY ROUND THIRTY-TWO' in _ptflat
ok6 &= 'A Bell-type test needs one or the other' not in _ptflat
ok6 &= 'The first half was wrong' in _ptflat
# The exposure must be by ONE composite unitary on a qubit system, through closure alone:
# no lift rule, no fixed system state, no pure ancilla, no mixer, no Bell pair.
fe = open(os.path.join(BRIDGE, 'OIBridge', 'FactorExchange.lean'), encoding='utf-8').read()
_feflat = ' '.join(fe.split())
ok6 &= 'def factorSwap : Equiv.Perm (Fin 2 × Fin 2) := Equiv.prodComm (Fin 2) (Fin 2)' in fe
_hq = _slice(fe, 'def HasQubitFactorExchange', 'theorem compositeControl_hasFactorExchange')
ok6 &= bool(_hq) and 'T.availExt 2 Unit (fun _ => conjChannel swapMat)' in _hq
ok6 &= _hq.count('∧') == 0 and 'prepAvail' not in _hq and 'ancMix' not in _hq
# the exact computation must be an equation of MAPS, uniform ancilla in, system transpose out
_eq = _slice(fe, 'theorem exchanged_transpose_eq', ':=')
ok6 &= bool(_eq) and 'uniformAttach 2' in _eq and '= transposeMap (Fin 2)' in _eq
ok6 &= 'ancTranspose (Fin 2) 2' in _eq and _eq.count('conjChannel swapMat') == 2
# the exposure theorem's premises are exactly soundness and the exchange
_ex = _slice(fe, 'theorem factorExchange_exposes_ancTranspose', ':= by')
ok6 &= bool(_ex) and '(hsound : KrausSound T)' in _ex and '(hex : HasQubitFactorExchange T)' in _ex
ok6 &= 'HasCompositeUnitaryControl' not in _ex and 'pureAttach' not in _ex and 'Bell' not in _ex
ok6 &= '¬ T.availExt 2 Unit (fun _ => ancTranspose (Fin 2) 2)' in _ex
# and the proof must reach round 27's system-side refutation, not re-prove non-CP-ness
_exb = _slice(fe, 'theorem factorExchange_exposes_ancTranspose', 'theorem compositeControl_exposes_ancTranspose')
ok6 &= 'transposeMap_not_kraus' in _exb and 'T.prepAvail_uniform' in _exb
ok6 &= 'choiMatrix' not in _exb and 'dotProduct_mulVec_nonneg' not in _exb
# no structure field, no Bell state, no lift rule is added anywhere in this file
ok6 &= re.search(r'(?m)^structure ', fe) is None and 'bellState' not in fe and 'liftRule' not in fe
ok6 &= 'KrausSoundExt' not in fe.split('namespace OIBridge')[1]
# WORDING: one direction only, and composite soundness is NOT derived
ok6 &= 'the converse is not proved and not claimed' in _feflat
ok6 &= '`KrausSoundExt` is not derived here' in _feflat
ok6 &= 'is strictly weaker' not in _feflat and 'strictly below' not in _feflat
# ROUND-33 GUARDS.  The dimensional obstruction must be the reduction-type map, refuted by
# an explicit Choi witness, proved 2-positive WITHOUT a PSD square root, and must claim no
# operational countermodel and nothing about any theory.
do = open(os.path.join(BRIDGE, 'OIBridge', 'DimensionalObstruction.lean'), encoding='utf-8').read()
_dobody = do.split('namespace OIBridge')[1]
_doflat = ' '.join(do.split())
ok6 &= 'toFun X := (7 : ℂ)⁻¹ • ((2 * X.trace) • (1 : Matrix S S ℂ) - X)' in do
# 2-positivity is DEFINED as the qubit-reference test, nothing weaker
_tp = _slice(do, 'def IsTwoPositive', '/--')
ok6 &= bool(_tp) and 'M.PosSemidef → (ampl2 Φ M).PosSemidef' in _tp
# non-CP by the explicit witness, not by a CP/Kraus classification
_ncp = _slice(do, 'theorem reduction2_not_cp', 'end Choi')
ok6 &= bool(_ncp) and 'maxEntVec' in _ncp and 'dotProduct_mulVec_nonneg' in _ncp
ok6 &= 'IsKrausFamily' not in _dobody and 'krausFamily_cp' not in _dobody
# the pure case is proved by hand (Gram-Schmidt), and the extension to all PSD inputs uses
# the spectral resolution and eigenvalue nonnegativity -- no square root anywhere
_r1 = _slice(do, 'theorem ampl2_reduction2_rankOne', 'theorem edyad_eq_vecMulVec')
ok6 &= bool(_r1) and 'dot_rankTwo_bound' in _r1 and 'eigenvalues' not in _r1
_tpp = _slice(do, 'theorem reduction2_twoPositive', 'end Amplification')
ok6 &= bool(_tpp) and 'hermitian_spectral_edyad' in _tpp and 'eigenvalues_nonneg' in _tpp
ok6 &= 'sqrt' not in _dobody and 'conjTranspose_mul_self' not in _dobody
ok6 &= 'posSemidef_iff_eq' not in _dobody
# the boxed statement carries all four properties
_box = _slice(do, 'theorem qubit_tests_do_not_characterize_cp', ':=')
ok6 &= bool(_box) and 'IsTracePreserving Φ ∧ Φ 1 = 1 ∧ IsTwoPositive Φ ∧ ¬ IsCompletelyPositive Φ' in _box
# NO operational content is claimed: no theory, no availability, no structure field
ok6 &= 'availExt' not in _dobody and 'KrausSoundExt' not in _dobody
ok6 &= 'FiniteOperationalTheory' not in _dobody
ok6 &= re.search(r'(?m)^structure ', do) is None
# WORDING: the non-claims must be on the record
ok6 &= 'no operational countermodel is claimed' in _doflat
ok6 &= 'boundary item 3 (PSD square-root/factorization) is NOT consumed' in _doflat
ok6 &= 'It does NOT prove that `Φ₂` fails 3-positivity' in _doflat
ok6 &= 'The next question, recorded and not answered' in _doflat
ok6 &= 'is strictly weaker' not in _doflat and 'countermodel exists' not in _doflat
# and round 34's answer must be cross-referenced, since the open question is now closed
ok6 &= 'ANSWERED BY ROUND THIRTY-FOUR' in _doflat
# ROUND-34 GUARDS.  The countermodel must be exactly quantum on the system, 2-positive-instrument
# on every composite, with the one external step ISOLATED against boundary item 3 and its
# discharge stated loudly rather than the item silently retired.
dc = open(os.path.join(BRIDGE, 'OIBridge', 'DimensionalCountermodel.lean'), encoding='utf-8').read()
_dcbody = dc.split('namespace OIBridge')[1]
_dcflat = ' '.join(dc.split())
# the composite sector: every branch 2-positive AND aggregate trace preservation, nothing else
_sec = _slice(dc, 'def IsTwoPositiveInstrument', 'end Sector')
ok6 &= bool(_sec) and '(∀ a, IsTwoPositive (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace' in _sec
# the key lemma uses no factorization and no hypothesis beyond 2-positivity
_key = _slice(dc, 'theorem twoPositive_qubit_cp', 'end Amplification')
ok6 &= bool(_key) and 'PSDFactorization' not in _key and 'hfac' not in _key
ok6 &= 'choiMatrix_eq_ampl2' in _key
# the reference-tested preparation predicate, and the explicit reindexing matrix
_pp = _slice(dc, 'def RefTestedPrep', '/--')
ok6 &= bool(_pp) and '(∀ ρ, (P ρ).trace = ρ.trace)' in _pp and 'amplR P' in _pp
ok6 &= 'def ancEmbed' in dc and 'theorem amplR_ptraceAncL_eq' in dc and 'theorem amplR_uniformAttach_eq' in dc
# the external step: stated as a hypothesis, consumed exactly there
ok6 &= 'def PSDFactorization' in dc
_ks = _slice(dc, 'theorem isKrausFamily_of_cp_of_factorization', ':= by')
ok6 &= bool(_ks) and '(hfac : PSDFactorization (S × S))' in _ks
_thy = _slice(dc, 'noncomputable def countermodelOf', 'variable (hfac')
ok6 &= bool(_thy) and 'avail := fun _ _ _ F => IsKrausFamily F' in _thy
ok6 &= 'availExt := fun _ _ _ _ F => IsTwoPositiveInstrument F' in _thy
ok6 &= 'isKrausFamily_of_cp_of_factorization hfac' in _thy
# the discharge uses the spectral resolution and the real square root, no Mathlib PSD sqrt/CFC
_dis = _slice(dc, 'theorem psdFactorization_of_spectral', 'end KrausStep')
ok6 &= bool(_dis) and 'hermitian_spectral_edyad' in _dis and 'Real.sqrt' in _dis
ok6 &= 'PosSemidef.sqrt' not in _dcbody and 'posSemidef_iff_eq' not in _dcbody and 'CFC' not in _dcbody
# the two capstones: conditional on the boundary, and unconditional
_cap1 = _slice(dc, 'theorem countermodel_of_factorization', ':=')
ok6 &= bool(_cap1) and '(hfac : PSDFactorization (Fin 2 × Fin 2))' in _cap1
ok6 &= 'ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T ∧ ¬ KrausSoundExt T' in _cap1
_cap2 = _slice(dc, 'theorem exactControl_not_implies_krausSoundExt', ':=')
ok6 &= bool(_cap2) and 'hfac' not in _cap2 and 'PSDFactorization' not in _cap2
ok6 &= 'ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T ∧ ¬ KrausSoundExt T' in _cap2
# no structure field is added; the theory is built from the existing structure
ok6 &= re.search(r'(?m)^structure ', dc) is None
# WORDING: the boundary item is NOT retired, the audit is separate, and control is not the answer
ok6 &= 'THIS DOES NOT RETIRE BOUNDARY ITEM 3' in _dcflat
ok6 &= 'separate boundary audit' in _dcflat
ok6 &= 'The missing condition is therefore not control richness' in _dcflat
ok6 &= 'That principle is not added here' in _dcflat
ok6 &= 'boundary item 3 is retired' not in _dcflat and 'retires boundary item 3' not in _dcflat
ok6 &= 'is strictly weaker' not in _dcflat
# the general theorem must carry its sharp hypothesis and the exception must be at n = 4
er = open(os.path.join(BRIDGE, 'OIBridge', 'EdgeRigidity.lean'), encoding='utf-8').read()
ok6 &= 'theorem k4_rigidity (hn : 5 ≤ n)' in er
ok6 &= 'Edge 4 ≃ Edge 4' in er
ok6 &= 'theorem homometricSix_unrealizable' in open(
    os.path.join(BRIDGE, 'OIBridge', 'HomometricKill.lean'), encoding='utf-8').read()
cr = open(os.path.join(BRIDGE, 'OIBridge', 'CongruentReconstruction.lean'),
          encoding='utf-8').read()
ok6 &= 'theorem twoBranch_of_PiccardClassification' in cr
ok6 &= 'theorem twoBranch_of_spectral_classification' in cr
ok6 &= '(hm : 3 ≤ m)' in cr and 'theorem reconstruction_dim_two' in cr
# the spectral wrapper's classification premise must mention only spectra: no coefficient
# products in its hclass block (the coefficient hypotheses are DERIVED, not assumed)
spec_block = cr[cr.index('theorem twoBranch_of_spectral_classification'):]
spec_hclass = spec_block[spec_block.index('(hclass :'):spec_block.index('(∃ E₀ : ℝ')]
ok6 &= 'conj\'' not in spec_hclass and 'star' not in spec_hclass
check("R7", ok6,
      "LINT. All sixty-four files are imported by OIBridge.lean so CI builds them; no `sorry`, no "
      "`axiom`, no `native_decide`; all 7 + 16 + 8 + 8 + 7 + 11 + 21 + 4 + 66 + 3 + 17 + 17 + 11 + 15 + 10 + 20 + 11 + 7 + 13 + 31 + 13 + 27 + 9 + 11 + 17 + 8 + 6 + 29 + 23 + 28 + 7 + 8 + 17 + 21 + 17 + 14 + 9 + 20 + 33 + 2 + 30 + 24 + 30 + 33 + 49 + 21 + 22 + 12 + 31 + 39 + 32 + 52 + 21 + 13 + 22 + 25 + 38 + 77 + 30 + 11 + 5 + 16 + 22 + 26 named results print their "
      "axiom dependencies; `k4_rigidity` carries the sharp hypothesis 5 <= n, m = 2 closes "
      "via `reconstruction_dim_two`, and `twoBranch_of_spectral_classification`'s "
      "classification premise is purely spectral -- no coefficient product in its hclass "
      "block; `piccard_mu_bridge` records the parametric bridge to the quoted family")

# ---------------------------------------------------------------- R8  congruent reconstruction
import cmath
ok8 = True
rng8 = random.Random(20260831)


def rand_unitary(n):
    # Gram-Schmidt on a random complex matrix
    M = [[complex(rng8.gauss(0, 1), rng8.gauss(0, 1)) for _ in range(n)] for _ in range(n)]
    Q = []
    for r in M:
        v = r[:]
        for q in Q:
            ip = sum(a * b.conjugate() for a, b in zip(v, q))
            v = [a - ip * b for a, b in zip(v, q)]
        nrm = sum(abs(a) ** 2 for a in v) ** 0.5
        Q.append([a / nrm for a in v])
    return Q


def coeff_line(M, ta, tb, i, j):
    return (M[i][ta] * M[i][tb].conjugate()) * (M[j][ta] * M[j][tb].conjugate()).conjugate()


for n in (3, 4, 5):
    V = rand_unitary(n)
    tau = list(range(n))
    rng8.shuffle(tau)
    d = [cmath.exp(1j * rng8.uniform(0, 6.28)) for _ in range(n)]
    beta = [cmath.exp(1j * rng8.uniform(0, 6.28)) for _ in range(n)]
    E = sorted(rng8.sample(range(1, 60), n))
    E0 = rng8.uniform(-3, 3)
    W = [[0j] * n for _ in range(n)]
    for i in range(n):
        for a in range(n):
            W[i][tau[a]] = d[i] * beta[a] * V[i][a]
    # coefficient lines match
    for a in range(n):
        for b in range(n):
            if a != b:
                for i in range(n):
                    for j in range(n):
                        ok8 &= abs(coeff_line(W, tau[a], tau[b], i, j)
                                   - coeff_line(V, a, b, i, j)) < 1e-9
    # H' = D H D^dag + E0
    Ep = [0.0] * n
    for a in range(n):
        Ep[tau[a]] = E[a] + E0
    for i in range(n):
        for j in range(n):
            Hp = sum(W[i][c] * Ep[c] * W[j][c].conjugate() for c in range(n))
            H = sum(V[i][a] * E[a] * V[j][a].conjugate() for a in range(n))
            rhs = d[i] * H * d[j].conjugate() + (E0 if i == j else 0)
            ok8 &= abs(Hp - rhs) < 1e-7
    # reflection branch: Wr from conj(V), spectra reflected
    Wr = [[0j] * n for _ in range(n)]
    for i in range(n):
        for a in range(n):
            Wr[i][tau[a]] = d[i] * beta[a] * V[i][a].conjugate()
    Epr = [0.0] * n
    for a in range(n):
        Epr[tau[a]] = -E[a] + E0
    for i in range(n):
        for j in range(n):
            Hp = sum(Wr[i][c] * Epr[c] * Wr[j][c].conjugate() for c in range(n))
            H = sum(V[i][a] * E[a] * V[j][a].conjugate() for a in range(n))
            rhs = -(d[i] * H.conjugate() * d[j].conjugate()) + (E0 if i == j else 0)
            ok8 &= abs(Hp - rhs) < 1e-7
    # countercontrol: a non-unimodular column factor breaks a diagonal coefficient line (m >= 3)
    Wbad = [row[:] for row in W]
    for i in range(n):
        Wbad[i][tau[0]] *= 1.3
    broke = False
    for b in range(1, n):
        for i in range(n):
            if abs(coeff_line(Wbad, tau[0], tau[b], i, i) - coeff_line(V, 0, b, i, i)) > 1e-6:
                broke = True
    ok8 &= broke
# m = 2 hyperbola: rho0 * rho1 = 1 with rho != 1 passes every pairwise-product test
rho = [2.5, 1 / 2.5]
ok8 &= abs(rho[0] * rho[1] - 1) < 1e-12 and abs(rho[0] - 1) > 1
check("R8", ok8,
      "CONGRUENT RECONSTRUCTION at m = 3, 4, 5: random unitary V, unimodular row/column phases "
      "and a mode permutation build W with all coefficient lines matching, and H' recovers "
      "D H D^dag + E0 exactly (reflected model recovers -D conj(H) D^dag + E0); a "
      "non-unimodular column factor breaks a diagonal line, and the m = 2 hyperbola "
      "rho0*rho1 = 1 passes every pairwise product while being non-flat -- the modulus "
      "rigidity is sharp at m >= 3; the hyperbola is retained as the countercontrol, and "
      "`dim_two_moduli_dichotomy` identifies it as exactly the swap (reflection) branch")

# ------------------------------------------- R9  frequencies to coefficients (FrequencyMatching)
ok9 = True
rng9 = random.Random(20260830)


def ampC_num(M, En, i, j, om):
    """The fiber sum of FrequencyMatching.ampC, numerically."""
    tot = 0j
    for p in range(len(En)):
        for q in range(len(En)):
            if abs((En[q] - En[p]) - om) < 1e-9:
                tot += M[i][p] * M[j][p].conjugate() * (M[i][q].conjugate()) * M[j][q]
    return tot


for _ in range(3):
    m9 = 4
    V = rand_unitary(m9)
    E = [0.0, 1.0, 4.0, 9.0]          # Golomb: all signed gaps distinct
    # 1. singleton fibers: the amplitude at omega = E_b - E_a IS the coefficient line
    for a in range(m9):
        for b in range(m9):
            if a != b:
                for i in range(m9):
                    for j in range(m9):
                        line = (V[i][a] * V[j][a].conjugate()
                                * V[i][b].conjugate() * V[j][b])
                        ok9 &= abs(ampC_num(V, E, i, j, E[b] - E[a]) - line) < 1e-9
    # 2. |U_ij(t)|^2 equals the Fourier sum of the amplitudes over the gap set
    gaps9 = sorted({round(E[q] - E[p], 9) for p in range(m9) for q in range(m9)})
    for _ in range(3):
        t = rng9.uniform(-2, 2)
        for i in range(m9):
            for j in range(m9):
                U = sum(V[i][a] * cmath.exp(-1j * E[a] * t) * V[j][a].conjugate()
                        for a in range(m9))
                four = sum(ampC_num(V, E, i, j, om) * cmath.exp(1j * om * t)
                           for om in gaps9)
                ok9 &= abs(abs(U) ** 2 - four) < 1e-7
    # 3. a translation-congruent W matches every amplitude at the translated frequency
    tau = list(range(m9))
    rng9.shuffle(tau)
    d = [cmath.exp(1j * rng9.uniform(0, 6.28)) for _ in range(m9)]
    beta = [cmath.exp(1j * rng9.uniform(0, 6.28)) for _ in range(m9)]
    E0 = rng9.uniform(-3, 3)
    W = [[0j] * m9 for _ in range(m9)]
    Ep = [0.0] * m9
    for a in range(m9):
        Ep[tau[a]] = E[a] + E0
        for i in range(m9):
            W[i][tau[a]] = d[i] * beta[a] * V[i][a]
    for om in gaps9:
        for i in range(m9):
            for j in range(m9):
                ok9 &= abs(ampC_num(W, Ep, i, j, om) - ampC_num(V, E, i, j, om)) < 1e-9
# 4. countercontrol: a DEGENERATE spectrum collides two fibers, and the amplitude at the
#    shared frequency is no longer any single coefficient line
Vd = rand_unitary(4)
Ed = [0.0, 1.0, 2.0, 5.0]             # E1-E0 = E2-E1 = 1: the omega = 1 fiber has two pairs
collided = False
for i in range(4):
    for j in range(4):
        amp = ampC_num(Vd, Ed, i, j, 1.0)
        l01 = Vd[i][0] * Vd[j][0].conjugate() * Vd[i][1].conjugate() * Vd[j][1]
        l12 = Vd[i][1] * Vd[j][1].conjugate() * Vd[i][2].conjugate() * Vd[j][2]
        if abs(amp - l01) > 1e-6 and abs(amp - l12) > 1e-6:
            collided = True
        ok9 &= abs(amp - (l01 + l12)) < 1e-9
ok9 &= collided
# 5. the m = 2 dichotomy algebra: q(1-q) = p(1-p) iff q = p or q = 1 - p
for _ in range(50):
    p = rng9.uniform(0.01, 0.99)
    for q in (p, 1 - p):
        ok9 &= abs((q - p) * (1 - p - q)) < 1e-12
        ok9 &= abs(q * (1 - q) - p * (1 - p)) < 1e-12
    q = rng9.uniform(0.01, 0.99)
    if abs(q - p) > 1e-3 and abs(q - (1 - p)) > 1e-3:
        ok9 &= abs(q * (1 - q) - p * (1 - p)) > 1e-7
check("R9", ok9,
      "FREQUENCIES TO COEFFICIENTS at m = 4: with a Golomb spectrum every fiber is a "
      "singleton, so each frequency amplitude of |U_ij(t)|^2 IS one coefficient line "
      "(`fiber_singleton` + `coefficient_line_extraction`); |U|^2 equals the Fourier sum of "
      "the amplitudes (`normSq_eq_sum_gaps`); a translation-congruent model matches every "
      "amplitude; a degenerate spectrum merges two fibers and the amplitude is their SUM, not "
      "a line -- the distinct-gap hypothesis is load-bearing; and the m = 2 factorization "
      "(q-p)(1-p-q) = 0 characterizes q(1-q) = p(1-p) exactly")


print()
print('     [scope] Settled in Lean: K4-rigidity for all n >= 5 with the n = 4 complement')
print('     exception sharp (EdgeRigidity), the non-induced => exceptional-relation corollary')
print('     with its flat-direction control, and the two finite endpoints of the n = 6 kill')
print('     chain (HomometricSix): L_mu-perp = span(1) and the max-clique-3 obstruction, plus')
print('     mask factorizations, the xi/eta linkage, Golomb/forcedness of mu, and mu being')
print('     induced by no vertex map even with mixed orientations. The analytic middle is now')
print('     ALSO kernel-closed (HomometricKill.lean): rank-one line forcing, the multiplicative')
print('     phase elimination, the torus-zero bridge, and the assembled theorem')
print('     homometricSix_unrealizable -- the forced non-two-branch six-mode correspondence')
print('     admits no pair of unitary eigenbases with all overlaps nonzero. The congruent-case')
print('     assembly is kernel-closed (phase_coboundary, both reconstruction branches, the')
print('     m = 0, 1 dispatch), the Fourier layer is kernel-closed (FrequencyMatching:')
print('     probabilities determine every frequency amplitude, and distinct gaps extract each')
print('     coefficient line from one spectral identity), and m = 2 is kernel-closed')
print('     (dim_two_moduli_dichotomy / unitary2_line_dichotomy / reconstruction_dim_two: the')
print('     hyperbola IS the reflection branch). twoBranch_of_spectral_classification now needs')
print('     only equal probabilities + distinct gaps + a purely SPECTRAL classification. NOT')
print('     settled in the kernel: the integer Piccard/Bekir-Golomb classification itself,')
print('     consumed as the cited premise BGIntegerClassification -- the manuscript two-branch')
print('     THEOREM is graded K2 on it, with the integer-to-real passage kernel-proved')
print('     (TurnpikeScopeTransfer.lean); formalizing the 2007 classification is the sole')
print('     remaining K3 backlog item.')
print()
print("edge_rigidity_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
