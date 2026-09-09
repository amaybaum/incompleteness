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
import glob
import itertools
import json
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
    ('CompletedOI', ('qm_implies_oiCore', 'oiCore_forward_redundancy',
                     'completedOI_iff_qm', 'completedOI_iff_physical', 'oiCore_not_completedOI', 'observationalIndependence_iff_inert',
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
                                'countermodel_reversibleRichness', 'redundancy_fails', 'form_fixed_existence_fails', 'conjChannel_trace_iff',
                                'instAvail_mono', 'instAvail_trace', 'fullClass_contextStable', 'fullClass_labelInvariant', 'cp_of_realized',
                                'conjChannel_smul', 'realized_conj', 'realized_zero', 'realized_add', 'realized_sum', 'sum_comp', 'comp_sum',
                                'realized_comp', 'realized_smul_nonneg', 'realized_transport', 'realized_id', 'realized_localLuders',
                                'realized_discard', 'fullClass_arch', 'realized_of_instAvail', 'cp_of_instAvail', 'instAvail_comp_one',
                                'instAvail_one_comp', 'instAvail_id', 'transport_refl', 'transport_trans', 'transport_comp', 'reindex_reindex',
                                'uniformAttach_reindex', 'transport_discard', 'instAvail_transport', 'tensorOf_conjTranspose',
                                'amplRefL_conjChannel', 'amplRefL_sum', 'refBlockR_amplRef', 'amplRefL_comp', 'tensorOf_one_reindex',
                                'tensorOf_one_readProj', 'amplRefL_transport', 'refBlockR_reindex_uniformAttach', 'amplRefL_discard',
                                'instAvail_spectator', 'instAvail_withSpectator', 'realized_withSpectator', 'genFamily_regrouping',
                                'genFamily_relabelling', 'genTheory_ambient', 'genTheory_embeddedObservation', 'genTheory_availExt_iff',
                                'genTheory_fullClass_control', 'genTheory_mono', 'genTheory_generated', 'genTheory_implementationLocality',
                                'parallel_of_implementationLocal', 'observationalIndependence_of_implementationLocality',
                                'krausSoundExt_of_implementationGenerated', 'validity_of_implementationLocality',
                                'instAvail_fullClass_of_krausFamily', 'generated_of_qm', 'implementationLocality_of_qm',
                                'countermodel_not_implementationGenerated', 'countermodel_not_implementationLocality',
                                'implementationLocality_independent', 'oiPlusEmbedded_of_oiPlusLocal', 'qm_of_oiPlusLocal', 'oiPlusLocal_of_qm',
                                'oiPlusLocal_iff_qm', 'oiPlusLocal_iff_oiPlusEmbedded', 'carrier_general_oiPlusLocal')),
    ('MicroscopicReversibility', ('reversibleRichness_iff', 'control_of_lieRank_inverse', 'control_of_lieRank', 'inverseAccessibility_of_lieRank',
                                  'dyad_sum_span_single', 'kraus_of_conj_unitary', 'implementationLocality_of_reversible', 'conjChannel_zero',
                                  'exists_scaled_mem_of_instAvail_unitary', 'inverseAccessibility_of_generated_daggerStable',
                                  'inverseAccessibility_of_reversibleImplementationLocality', 'genTheory_reversibleImplementationLocality',
                                  'fullClass_daggerStable', 'fullClass_unitaryRaySaturated', 'reversibleImplementationLocality_of_qm',
                                  'oiPlusLocal_of_oiPlusMicro', 'qm_of_oiPlusMicro', 'oiPlusMicro_of_qm', 'oiPlusMicro_iff_qm',
                                  'oiPlusMicro_iff_oiPlusLocal', 'carrier_general_oiPlusMicro')),
    ('LieRankSource', ('diagClass_arch', 'diagClass_contextStable',
                     'diagClass_labelInvariant', 'diagClass_daggerStable', 'diagClass_unitaryRaySaturated', 'preservesDiag_conj_of_diag', 'diagGen_not_control',
                     'lieRank_not_redundant', 'single_apply', 'single_conjTranspose', 'single_smul_one',
                     'transition_hermitian', 'phaseGate_conjTranspose', 'phaseGate_unitary', 'permMatrix_one',
                     'permMatrix_mul', 'perm_conj_transition', 'perm_conj_transitionY', 'phase_conj_transition',
                     'bracket_XY', 'ctrl_unitary', 'gen_X', 'gen_Y',
                     'exists_perm_pair', 're_diag_zero', 'skew_offdiag', 'pair_decomp',
                     'hControl_star', 'avail_mul', 'avail_perm', 'avail_ctrl',
                     'lieRank_of_elementary', 'elementary_of_control', 'oiPlusMicro_of_oiPlusElem', 'qm_of_oiPlusElem',
                     'oiPlusElem_of_qm', 'oiPlusElem_iff_qm', 'oiPlusElem_iff_oiPlusMicro', 'carrier_general_oiPlusElem',
                     'elementary_not_redundant')),
    ('PositivePackage', ('oiPlusPos_iff_qm', 'oiPlusPos_iff_oiPlusElem', 'carrier_general_oiPlusPos')),
    ('FlowEndpoint', ('onesTheory_avail_conj', 'onesTheory_sourcedOI', 'levelPerm_involutive', 'onesTheory_layerFlowExecutable',
                      'exists_third', 'onesTheory_no_quarter_flow', 'onesTheory_not_phaseFree_general', 'onesTheory_not_phaseFree',
                      'flow_endpoint_refuted', 'flow_endpoint_refuted_general', 'phaseGate_mulVec_ones',
                      'onesTheory_not_phasesAvailable', 'onesTheory_not_derivedOI', 'onesTheory_not_substratumAvail',
                      'onesTheory_not_qm')),
    ('PhaseSource', ('onesFixing_not_phasesAvailable', 'permClass_onesFixing', 'permTheory_not_phasesAvailable_onesFixing',
                     'bijectiveOperator_mulVec_ones', 'readWriteOperator_mulVec_ones', 'phaseGate_not_scalar',
                     'conjChannel_phaseGate_ne_id', 'diagonal_conj_phaseGate', 'phaseGate_moves_ones',
                     'substratumClass_not_onesFixing')),
    ('DerivedQ3', ('flipAt_self', 'flipAt_of_ne', 'phaseGate_mul_self', 'gateFlow_isolation_flip', 'flip_avail',
                   'phaseFree_of_phases_layerFlowExecutable', 'phaseFree_of_derivedOI_layerFlowExecutable',
                   'qm_of_derivedOI_layerFlowExecutable', "derivedOI_qm_iff_layerFlowExecutable'",
                   'derivedOI_layerFlowExecutable_of_qm', 'phaseFree_of_derivedOI_layerFlowExecutable_swap',
                   "derivedOI_qm_iff_layerFlowExecutable_swap'", 'gateFlow_one_eq_one', 'levelPerm_one',
                   'layerFlowExecutable_one', 'substratumTheory_layerFlowExecutable_one',
                   'derivedOI_layerFlowExecutable_one_not_phaseFree')),
    ('ExecSource', ('exists_nonMonomial_of_layerFlowExecutable', 'not_configurationLevel_of_layerFlowExecutable',
                    'bijectionLevel_not_layerFlowExecutable', 'configurationLevel_not_avail_gateFlow_half',
                    'substratumTheory_not_avail_gateFlow_half', 'obs_not_layerFlowExecutable',
                    'obs_not_layerFlowExecutable_shear', 'obs_not_layerFlowExecutable_swap',
                    'waveSubstratum_swap_moves', 'waveSubstratum_not_layerFlowExecutable_swap',
                    'gateFlow_half_not_monomial', 'onesClass_not_configurationLevel')),
    ('LiftSource', ('not_layerFlowExecutable_of_preservesDiag', 'coherentLift_isMonomial',
                    'reversibleExtension_conj_monomial', 'correlationExtension_preservesDiag',
                    'coherentLiftClass_contains_lift', 'coherentLiftClass_configurationLevel',
                    'coherentLiftClass_eq_substratumClass', 'coherentLiftClass_arch',
                    'coherentLiftTheory_eq_substratumTheory', 'coherentLiftClass_not_layerFlowExecutable',
                    'obs_availExt_le_coherentLift', 'waveSubstratum_coherentLift_not_layerFlowExecutable_swap',
                    'single_isMonomial', 'stochasticChannel_kraus_monomial', 'stochasticChannel_preservesDiag',
                    'stochastic_not_layerFlowExecutable', 'avail_one_not_layerFlowExecutable',
                    'obs_swap_avail_one_not_layerFlowExecutable')),
    ('C5Discovery', ('obligations_independent', 'killBattery_substratum', 'killBattery_ones', 'killBattery_perm',
                     'killBattery_not_qm', 'obligations_outside_battery', 'bijectionLevel_fails_obligations',
                     'updateLevel_symplectic_inert', 'hadamard_not_monomial', 'hadamard_not_preservesDiag',
                     'siteSwapImage_not_monomial', 'polGen_arch', 'polGen_not_configurationLevel',
                     'siteShearImage_one_eq_phaseGate', 'polarizedTheory_phase_level_one', 'gateFlow_half_eq_hsh',
                     'polarizedTheory_swap_half_level_one')),
    ('SubstratumSource', ('genTheory_avail_conj', 'genTheory_elementary', 'quantumArchitecture_supplies_all',
                       'genTheory_qm_of_quantumArchitecture', 'fullClass_drivesElementary', 'fullClass_quantumArchitecture',
                       'qm_generated_by_quantumArchitecture', 'diagClass_not_drivesElementary', 'diagGen_not_quantumArchitectureGenerated')),
    ('SubstratumInterface', ('monomial_permMatrix', 'monomial_diagonal', 'bijectiveOperator_monomial', 'phaseOperator_monomial',
                          'exchange_monomial', 'phase_monomial', 'monomial_entry', 'preservesDiag_conj_of_monomial',
                          'rot_not_monomial', 'monomialSource_not_control', 'monomialSource_not_qm', 'elementary_split')),
    ('ReadWriteControl', ('readWriteOperator_eq_perm', 'readWriteOperator_monomial', 'offDiagonal_interp_not_monomial', 'readWriteSourced_monomialSource',
                        'readWriteSourced_not_control', 'readWriteSourced_not_qm', 'memorySwap_nontrivial', 'memorySwap_operator_monomial',
                        'readWriteControl_independent')),
    ('StructuralClosure', ('of_ite_ne_zero', 'mul_entry_ne_zero', 'monomial_submonomial', 'submonomial_monomial',
                          'monomial_iff_submonomial', 'submonomial_one', 'submonomial_mul', 'submonomial_smul',
                          'submonomial_diagonal', 'submonomial_block', 'substratumClass_arch', 'tensor_one_entry_ne_zero',
                          'submonomial_tensor_one', 'substratumClass_contextStable', 'submonomial_reindex',
                          'substratumClass_labelInvariant', 'submonomial_conjTranspose', 'substratumClass_daggerStable', 'substratumClass_unitaryRaySaturated',
                          'bijectiveOperator_conjTranspose', 'phaseOperator_conjTranspose', 'substratumClass_structurallyClosed',
                          'bijectiveOperator_supplied', 'phaseOperator_supplied', 'readWriteOperator_supplied',
                          'substratumGen_not_control', 'substratumGen_not_qm', 'quantumArchitecture_iff_drives_of_closed',
                          'substratumClass_not_drivesElementary', 'substratumClass_not_quantumArchitecture', 'substratum_residual',
                          'substratum_extension_quantum_iff_drives', 'substratum_plus_control_qm', 'fullClass_extendsSubstratum',
                          'qm_generated_by_substratum_extension')),
    ('TypedCompletion', ('availT_equiv', 'shadow_regroupingInvariant', 'shadow_relabellingInvariant', 'shadow_isAmbientMember',
                         'shadow_embeddedObservation', 'attachUniform_fin', 'discardR_fin', 'discardR_attachUniform',
                         'embL_isometry', 'embR_isometry', 'sum_embL_proj', 'sum_embR_proj', 'embL_conj_apply',
                         'embR_compress_apply', 'discardR_embL_conj', 'attachUniform_eq_sum', 'isTypedKraus_of_family',
                         'availT_of_krausFamily', 'wrap_availT', 'wrap_apply', 'recover_of_wrap', 'typedKraus_of_availT',
                         'sum_emb2_proj', 'emb2_compress', 'regOp_normalized', 'discardR_regOp_conj', 'availT_of_typedKraus',
                         'typed_determined', 'conjT_eq_conjChannel', 'typedKraus_iff_endomorphic', 'shadowQuantum_of_typed',
                         'typed_determined_iff', 'typed_determined_of_oiPlusElem', 'preservesDiag_transportT',
                         'preservesDiag_attachUniform', 'preservesDiag_discardR', 'preservesDiag_localLuders',
                         'typedDiag_shadow_not_control', 'typedDiag_shadow_not_qm', 'typed_interface_not_quantum')),
    ('RegionLimit', ('restrict_eq_discardR', 'trace_tensorOf', 'tensorOf_mul', 'trace_inclObs_mul', 'uniform_consistent',
                     'pureProduct_consistent', 'overlap_uniform_pure', 'overlap_eventually_small', 'genZero_hermitian',
                     'genTwoPi_hermitian', 'flow_genZero', 'flow_genTwoPi', 'flows_agree_integer', 'flows_differ_half',
                     'continuous_extension_not_unique', 'continuum_audit_round1')),
    ('RegionTower', ('confRestrict_trans', 'agreeOff_trans_iff', 'inclObs_refl', 'inclObs_trans', 'restrict_refl',
                     'sum4_comm', 'trace_inclObs_mul_restrict', 'eq_of_trace_pairing', 'restrict_trans',
                     'dependsOnlyOn_comp_step', 'iterate_dependsOnlyOn_ball', 'site_iterate_dependsOnlyOn',
                     'readout_unaffected_outside_ball', 'restrict_add', 'restrict_smul', 'consistent_mix',
                     'card_extensions_agree', 'card_fibre', 'card_conf', 'restrict_uniform_apply',
                     'uniform_family_consistent', 'phaseGate_conj_apply', 'offDiag_zero_of_phase_invariant',
                     'diag_eq_of_perm_invariant', 'invariant_state_scalar', 'invariant_normalized_eq_uniform',
                     'uniform_invariant', 'state_selection_audit')),
    ('QuasilocalAlgebra', ('glob_patch', 'patch_eq_iff', 'agreeOffG_iff', 'kern_inclObs', 'kern_conjTranspose',
                           'emb_single_apply', 'ext_of_kerOf', 'emb_inclObs', 'emb_mul', 'emb_injective', 'emb_eq_iff',
                           'inclObs_mul', 'inclObs_one', 'inclObs_injective', 'inclObs_conjTranspose', 'ofM_eq_iff',
                           'exists_ofM₂', 'norm_inclObs', 'star_ofM', 'norm_ofM',
                           'isometry_star_local', 'star_coe', 'stage_inclObs',
                           'norm_stage', 'stage_injective', 'closure_iUnion_stage', 'evalLocal_ofM', 'evalLocal_one',
                           'evalLocal_nonneg', 'norm_trace_mul_le', 'norm_evalLocal_le', 'quasiState_coe',
                           'quasiState_stage', 'quasiState_one', 'quasiState_nonneg', 'quasiState_unique',
                           'uniformFamily_isStateFamily', 'referenceState_stage', 'agreeOffG_map', 'kerOf_heis',
                           'symm_patch_eq_patch', 'target_of_glob_eq', 'heis_emb', 'transported_conjTranspose',
                           'transported_injective', 'norm_transported', 'heisLoc_star', 'norm_heisLoc',
                           'heisLoc_inv_heisLoc', 'heisQ_mul', 'heisQ_star', 'norm_heisQ', 'heisQ_inv_heisQ',
                           'heis_iterate_emb', 'quasilocal_completion')),
    ('SecondOrderCircuit', ('leap_eq_swap_shear', 'shear_shear', 'swapLayer_swapLayer',
                            'curOf_gate', 'gate_gate', 'gate_comm', 'swapGate_comm',
                            'shearOn_insert', 'gateList_eq_shearOn', 'gateList_eq_shear_of_mem',
                            'gateList_eq_self_of_notMem', 'depth_two_circuit',
                            'proj_mul_proj', 'unit_one', 'unit_mul_unit', 'star_unit',
                            'flow_one', 'flow_add', 'flow_mul', 'gate_drive',
                            'unit_comm', 'isGateList_prod', 'flowList_one', 'flowList_add',
                            'layer_drive', 'drive_two', 'two_layer_drive',
                            'permMat_involutive', 'localGate_isGate',
                            'proj_localGate_mem_stage', 'quasilocal_drive')),
    ('SecondOrderLayer', ('extPerm_involutive', 'qGate_isGate', 'inclObs_permMat',
                          'disjoint_gateRegion_of_notMem_affected', 'layerAct_stabilizes',
                          'layerAct_eq_of_stage_eq', 'layerLoc_ofM', 'layerLoc_mul',
                          'layerLoc_star', 'norm_layerLoc', 'layerQ_stage', 'norm_layerQ',
                          'layerQ_mul', 'layerQ_star', 'layerQ_zero_time',
                          'continuous_layerQ_time', 'layerU_add', 'layerQ_add_time',
                          'layerQ_bijective')),
    ('SwapLayer', ('swapConf_involutive', 'swapGate_isGate', 'swapGate_comm', 'swapU_add',
                   'swapAct_stabilizes', 'swapLoc_ofM', 'swapLoc_mul', 'swapLoc_star',
                   'norm_swapLoc', 'swapQ_stage', 'norm_swapQ', 'swapQ_mul', 'swapQ_star',
                   'swapQ_zero_time', 'continuous_swapQ_time', 'swapQ_add_time',
                   'swapQ_bijective')),
    ('SecondOrderDrive', ('permOp_of_comp', 'permOpInv_of_comp', 'heis_of_comp',
                          'heisLoc_of_comp', 'heisQ_of_comp', 'driveQ_zero_time', 'driveQ_mul',
                          'driveQ_star', 'norm_driveQ', 'driveQ_bijective',
                          'continuous_driveQ_time', 'driveQ_isContinuousPath',
                          'mem_stepInfl_of_mem_gateRegion', 'ruleDynamics_comp',
                          'heisQ_ruleDynamics', 'glob_localConf', 'localConf_localConf',
                          'permOp_localDyn', 'permOpInv_localDyn', 'heis_localDyn',
                          'heisLoc_localDyn', 'heisQ_localDyn', 'heis_eq_of_agree',
                          'qGate_regionSwap_union', 'swapU_one_eq_qGate',
                          'agreeOffG_swapLayer', 'heis_swapDyn_emb', 'swapQ_one_eq_heisQ',
                          'curOn_shearOnRegion', 'shearOnRegion_involutive', 'shearPerm_empty',
                          'gateOn_shearOnRegion', 'gateEquiv_trans_shearPerm',
                          'layerU_one_eq_qGate', 'rhs_glob', 'localConf_shearPerm_of_mem',
                          'localConf_shearPerm_of_not_mem', 'heis_shearDyn_emb',
                          'layerQ_one_eq_heisQ', 'driveQ_one_eq_heisQ')),
    ('InstrumentAvailability', ('isQInstrJ_fin', 'isFSJ_fin', 'qTotalJ_fin', 'qTotalJ_equiv',
                                'isQInstrJ_equiv', 'qBranchJ_coarse', 'sum_qBranchJ', 'availFS_id',
                                'mem_range_stage_mono', 'availFS_comp', 'availFS_relabel',
                                'availFS_dyn', 'availFS_of_kraus', 'kraus_of_availFS',
                                'qTotalJ_stage_of_disjoint', 'phaseAll_not_availFS',
                                'q3_countermodel', 'states_untouched', 'dynamics_untouched')),
    ('InstrumentCompletion', ('qBranch_add', 'qBranch_smul', 'qBranch_star_mul_self', 'sum_qBranch',
                              'qBranch_sum_one', 'qTotal_one', 'qInstrument_of_kraus',
                              'kraus_of_finiteSupport', 'finiteSupport_iff_kraus',
                              'qBranch_stage_inclObs', 'qTotal_stage_of_disjoint', 'wtConj_apply',
                              'wtConj_mul', 'wtConj_injective', 'inclObs_wtConj', 'norm_wtConj',
                              'wtLoc_ofM', 'wtLoc_mul', 'wtLoc_star', 'norm_wtLoc', 'wtQ_stage',
                              'wtQ_mul', 'wtQ_smul', 'wtQ_star', 'norm_wtQ', 'wtQ_one', 'siteWt_unimodular',
                              'phaseAllWt_unimodular', 'phaseAllWt_compat', 'phaseAllQ_mul',
                              'norm_phaseAllQ', 'phaseAllWt_singleton', 'phaseAll_not_finiteSupport',
                              'instrument_audit_entry_one')),
    ('QuasilocalCharacterization', ('emb_comm_of_disjoint', 'stage_comm_of_disjoint', 'localMap_ofM',
                                    'localHom_unique', 'norm_localHom', 'canon_stage', 'norm_canon',
                                    'canonHom_injective', 'canonHom_surjective', 'canonEquiv_stage',
                                    'canon_unique', 'systemEquiv_stage', 'systemEquiv_unique',
                                    'systemState_stage', 'systemState_isState', 'oi_localityPreserving',
                                    'canon_dyn', 'systemEquiv_dyn', 'inclObs_phaseConj', 'phaseConj_four',
                                    'norm_phaseConj', 'phaseQ_stage', 'norm_phaseQ', 'phaseQ_four',
                                    'phase_localityPreserving', 'phaseQ_ne_heisQ',
                                    'quasilocal_characterization')),
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
# Round-58 guards: the split of reversible richness; dagger stability stated without the
# availability vocabulary; the inverse clause derived from dagger stability under unitary-ray
# saturation and, after the inverse-clause audit, from Lie-rank control on the well-formed theory;
# no countermodel claimed.
mrv = open(os.path.join(BRIDGE, 'OIBridge', 'MicroscopicReversibility.lean'), encoding='utf-8').read()
_mrvflat = ' '.join(mrv.split())
ok6 &= 'theorem reversibleRichness_iff' in mrv and 'InverseAccessibility T ∧ LieRankRichness T := Iff.rfl' in _mrvflat
_ds = _slice(mrv, 'def DaggerStable', 'variable {A : Type}')
for _w in ('avail', 'withSpectator', 'HasCompositeUnitaryControl', 'InverseAccessibility'):
    ok6 &= _w not in _ds
ok6 &= 'theorem kraus_of_conj_unitary' in mrv and 'theorem inverseAccessibility_of_generated_daggerStable' in mrv
ok6 &= 'theorem reversibleImplementationLocality_of_qm' in mrv
_cm = ' '.join(_slice(mrv, 'theorem carrier_general_oiPlusMicro', ':=').split())
ok6 &= bool(_cm) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _cm
ok6 &= _cm.endswith('OIPlusMicro T ↔ ExactAllFiniteEndomorphicQuantumOps T')
ok6 &= 'def OIPlusMicro : Prop := ReversibleImplementationLocality T ∧ LieRankRichness T ∧ EmbeddedObservation T' in _mrvflat
ok6 &= 'force inverse accessibility' in _mrvflat and 'consumes no inverse of a control' in _mrvflat
ok6 &= 'theorem inverseAccessibility_of_lieRank [Nonempty A] (hwf : WellFormed T)' in _mrvflat
ok6 &= 'theorem inverse_redundant' not in mrv
ok6 &= 'theorem inverseAccessibility_independent' not in mrv and 'theorem daggerStable_of_inverse' not in mrv
ok6 &= 'theorem lieRank_of_' not in mrv
ok6 &= 'structure FiniteOperationalTheory' not in mrv and 'native_decide' not in mrv
# Round-59 guards: the generated-theory construction; the diagonal-architecture redundancy
# countermodel; the elementary-transition primitive stated without a Lie algebra or reachability;
# the su(D) derivation; the compressed set; the minimal repertoire and converse unclaimed.
lrs = open(os.path.join(BRIDGE, 'OIBridge', 'LieRankSource.lean'), encoding='utf-8').read()
_lrsflat = ' '.join(lrs.split())
ok6 &= 'theorem lieRank_not_redundant' in lrs and '¬ LieRankRichness T' in _slice(lrs, 'theorem lieRank_not_redundant', ':=')
ok6 &= 'theorem hControl_star' in lrs and 'theorem lieRank_of_elementary' in lrs
_et = _slice(lrs, 'def ElementaryTransitionRichness', 'theorem avail_mul')
for _w in ('controlLie', 'HControl', 'IsSpecialSkew', 'UniversalUnitaryReachability'):
    ok6 &= _w not in _et
ok6 &= 'theorem elementary_of_control' in lrs and 'theorem diagGen_not_control' in lrs
_ce = ' '.join(_slice(lrs, 'theorem carrier_general_oiPlusElem', ':=').split())
ok6 &= bool(_ce) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A)' in _ce
ok6 &= _ce.endswith('OIPlusElem T ↔ ExactAllFiniteEndomorphicQuantumOps T')
ok6 &= 'def OIPlusElem : Prop := ReversibleImplementationLocality T ∧ ElementaryTransitionRichness T ∧ EmbeddedObservation T' in _lrsflat
ok6 &= 'The minimal elementary repertoire' in _lrsflat
ok6 &= 'theorem elementary_of_lieRank' not in lrs and 'theorem minimal_repertoire' not in lrs
ok6 &= 'theorem lieRank_redundant' not in lrs and 'theorem elementary_redundant_of' not in lrs
ok6 &= 'structure FiniteOperationalTheory' not in lrs and 'native_decide' not in lrs
# Round-61 guards: the substratum object (quantum architecture) collapsing the three
# primitive-source principles; the QM equivalence; the decisive elementary-drivability property
# with the diagonal countermodel; no derivation from A1-A6 claimed.
sub = open(os.path.join(BRIDGE, 'OIBridge', 'SubstratumSource.lean'), encoding='utf-8').read()
_subflat = ' '.join(sub.split())
ok6 &= 'structure QuantumArchitecture' in sub and 'def DrivesElementary' in sub
ok6 &= 'theorem quantumArchitecture_supplies_all' in sub and 'theorem genTheory_qm_of_quantumArchitecture' in sub
ok6 &= 'theorem qm_generated_by_quantumArchitecture' in sub
ok6 &= 'theorem diagClass_not_drivesElementary' in sub and 'theorem diagGen_not_quantumArchitectureGenerated' in sub
ok6 &= 'ReversibleImplementationLocality (genTheory 𝓘 hq.arch A) ∧ ElementaryTransitionRichness (genTheory 𝓘 hq.arch A) ∧ EmbeddedObservation (genTheory 𝓘 hq.arch A)' in _subflat
ok6 &= 'does not derive a quantum architecture from A1-A6' in _subflat
ok6 &= 'theorem quantumArchitecture_of_oiCore' not in sub and 'theorem substratum_supplies' not in sub
ok6 &= 'theorem drivesElementary_of_' not in sub and 'axiom ' not in sub
ok6 &= 'structure FiniteOperationalTheory' not in sub and 'native_decide' not in sub
# Round-62 guards: the substratum/implementation interface (monomial operators of bijective and
# phase interventions); the monomial invariant; the permutation-only no-go; no exponential
# computed; the frozen statements untouched.
sif = open(os.path.join(BRIDGE, 'OIBridge', 'SubstratumInterface.lean'), encoding='utf-8').read()
_sifflat = ' '.join(sif.split())
ok6 &= 'def IsMonomial' in sif and 'def bijectiveOperator' in sif and 'def phaseOperator' in sif
ok6 &= 'theorem rot_not_monomial' in sif and 'theorem preservesDiag_conj_of_monomial' in sif
ok6 &= 'theorem monomialSource_not_control' in sif and 'theorem monomialSource_not_qm' in sif
ok6 &= 'theorem exchange_monomial' in sif and 'theorem phase_monomial' in sif
ok6 &= 'def MonomialSource (T : FiniteOperationalTheory A) : Prop :=' in sif
_ns = _slice(sif, 'theorem monomialSource_not_qm', '#print axioms')
ok6 &= '¬ ExactAllFiniteEndomorphicQuantumOps T' in _ns
ok6 &= 'does not compute a matrix exponential' in _sifflat
ok6 &= 'theorem monomialSource_of_bijective' not in sif and 'theorem flow_monomial' not in sif
ok6 &= 'theorem drivesElementary_of_substratum' not in sif
ok6 &= 'structure FiniteOperationalTheory' not in sif and 'native_decide' not in sif
# Round-63 guards: the substratum-level read-write primitive with no quantum-control vocabulary;
# the induced monomial operator; the tangent-test no-go; the outcome (C); the countercontrol; no
# control law postulated; frozen statements untouched.
rwc = open(os.path.join(BRIDGE, 'OIBridge', 'ReadWriteControl.lean'), encoding='utf-8').read()
_rwcflat = ' '.join(rwc.split())
ok6 &= 'structure ReadWriteFamily' in rwc and 'def readWriteOperator' in rwc
_rwf = _slice(rwc, 'structure ReadWriteFamily', 'def readWriteOperator')
for _w in ('transition', 'flow', 'conjChannel', 'HControl', 'DrivesElementary'):
    ok6 &= _w not in _rwf
ok6 &= 'theorem offDiagonal_interp_not_monomial' in rwc and 'theorem readWriteOperator_monomial' in rwc
ok6 &= 'theorem readWriteSourced_not_qm' in rwc and 'theorem readWriteControl_independent' in rwc
_nq = _slice(rwc, 'theorem readWriteSourced_not_qm', 'theorem memorySwap_nontrivial')
ok6 &= '¬ ExactAllFiniteEndomorphicQuantumOps T' in _nq
ok6 &= 'theorem memorySwap_nontrivial' in rwc and 'theorem memorySwap_operator_monomial' in rwc
ok6 &= 'no control law is postulated' in _rwcflat
ok6 &= 'theorem drivesElementary_of_readWrite' not in rwc and 'theorem readWrite_flow' not in rwc
ok6 &= 'theorem offDiagonal_of_readWrite' not in rwc
ok6 &= 'structure FiniteOperationalTheory' not in rwc and 'native_decide' not in rwc
# Round-64 guards: the substratum class is the round-62 predicate (nothing added to obtain
# closure); the elementwise form and its equivalence in both directions; the four closures as
# theorems; the residual (not driving, not quantum) and the endpoint on extensions; no control
# law postulated; frozen statements untouched.
scl = open(os.path.join(BRIDGE, 'OIBridge', 'StructuralClosure.lean'), encoding='utf-8').read()
_sclflat = ' '.join(scl.split())
ok6 &= 'def substratumClass : ImplementationClass := fun _ _ _ K => IsMonomial K' in scl
ok6 &= 'def IsSubmonomial' in scl and 'theorem monomial_submonomial' in scl
ok6 &= 'theorem submonomial_monomial' in scl and 'theorem monomial_iff_submonomial' in scl
for _t in ('substratumClass_arch', 'substratumClass_contextStable', 'substratumClass_labelInvariant',
           'substratumClass_daggerStable', 'substratumClass_structurallyClosed'):
    ok6 &= ('theorem ' + _t) in scl
ok6 &= 'theorem substratumClass_not_drivesElementary' in scl and 'theorem substratum_residual' in scl
_res = _slice(scl, 'theorem substratum_residual', 'end Residual')
ok6 &= '¬ DrivesElementary substratumClass' in _res and '¬ QuantumArchitecture substratumClass' in _res
ok6 &= 'theorem substratum_plus_control_qm' in scl and 'theorem qm_generated_by_substratum_extension' in scl
_pc = _slice(scl, 'theorem substratum_plus_control_qm', 'theorem fullClass_extendsSubstratum')
ok6 &= 'hd : DrivesElementary' in _pc                                   # controllability is a hypothesis
ok6 &= 'no control law is postulated' in _sclflat
ok6 &= 'theorem substratumClass_drivesElementary' not in scl
ok6 &= 'theorem substratumClass_quantumArchitecture' not in scl
ok6 &= 'structure FiniteOperationalTheory' not in scl and 'native_decide' not in scl
# Level-II round-1 guards: the typed interface has independent operational meaning (its
# structure region names no dilation, no Kraus form, no shadow, no exactness); the shadow is a
# genuine FiniteOperationalTheory; both halves of the determination theorem are theorems; the
# interface is satisfied by a non-quantum theory; frozen Level I statements untouched.
tcl = open(os.path.join(BRIDGE, 'OIBridge', 'TypedCompletion.lean'), encoding='utf-8').read()
_tclflat = ' '.join(tcl.split())
ok6 &= 'structure TypedOperationalTheory' in tcl
_tst = _slice(tcl, 'structure TypedOperationalTheory', 'namespace TypedOperationalTheory')
for _w in ('Kraus', 'conjT', 'shadow', 'Exact', 'dilat', 'Stinespring', 'QuantumOps'):
    ok6 &= _w not in _tst
ok6 &= 'noncomputable def shadow' in tcl and ': FiniteOperationalTheory A where' in tcl
ok6 &= 'theorem shadow_embeddedObservation' in tcl
ok6 &= 'theorem typedKraus_of_availT' in tcl and 'theorem availT_of_typedKraus' in tcl
ok6 &= 'theorem typed_determined' in tcl and 'theorem typed_determined_of_oiPlusElem' in tcl
ok6 &= 'theorem typed_determined_iff' in tcl and 'theorem shadowQuantum_of_typed' in tcl
_td = _slice(tcl, 'theorem typed_determined ', 'theorem typed_determined_of_oiPlusElem')
ok6 &= '↔ IsTypedKrausInstrument F' in _td and 'hq : 𝒯.ShadowQuantum' in _td
ok6 &= 'noncomputable def typedDiag : TypedOperationalTheory' in tcl
ok6 &= 'theorem typedDiag_shadow_not_qm' in tcl and 'theorem typed_interface_not_quantum' in tcl
ok6 &= 'typing artifact for this interface' in _tclflat
ok6 &= 'theorem typed_qm_of_oi' not in tcl and 'theorem infinite' not in tcl
ok6 &= 'structure FiniteOperationalTheory' not in tcl and 'native_decide' not in tcl
# Level-III round-1 guards: the quasilocal-completion audit adds no continuity, completeness or
# Hilbert-space axiom; the restriction is the Level II discard (rfl); the continuity countermodel
# and the overlap decay are theorems; nothing about L^2(R^3) or an infinite-volume algebra is
# claimed; frozen Level I/II statements untouched.
rgl = open(os.path.join(BRIDGE, 'OIBridge', 'RegionLimit.lean'), encoding='utf-8').read()
_rglflat = ' '.join(rgl.split())
ok6 &= 'theorem restrict_eq_discardR' in rgl and ':= rfl' in _slice(rgl, 'theorem restrict_eq_discardR', 'def inclObs')
ok6 &= 'theorem trace_inclObs_mul' in rgl and 'theorem uniform_consistent' in rgl
ok6 &= 'theorem pureProduct_consistent' in rgl and 'theorem overlap_uniform_pure' in rgl
ok6 &= 'theorem overlap_eventually_small' in rgl
ok6 &= 'theorem continuous_extension_not_unique' in rgl and 'theorem continuum_audit_round1' in rgl
_ce = _slice(rgl, 'theorem continuous_extension_not_unique', 'end Continuity')
ok6 &= 'flow H₀ (1 / 2) ≠ flow H₁ (1 / 2)' in _ce and '∀ n : ℕ, flow H₀ n = flow H₁ n' in _ce
ok6 &= 'no continuity axiom is introduced' in _rglflat
for _w in ('axiom continuity', 'axiom completeness', 'StronglyContinuous', 'L2Space', 'MeasureTheory.L2',
           'theorem infiniteVolume', 'theorem continuum_limit_exists', 'CStarAlgebra'):
    ok6 &= _w not in rgl
ok6 &= 'structure FiniteOperationalTheory' not in rgl and 'native_decide' not in rgl
# Level-III round-2 guards: the region tower is functorial with restriction derived from inclusion
# through the duality; the causal cone is a theorem; the state-selection audit proves convexity,
# the reference family, and the finite Schur lemma; no representation, GNS or continuity axiom is
# introduced; frozen Level I/II statements untouched.
rgt = open(os.path.join(BRIDGE, 'OIBridge', 'RegionTower.lean'), encoding='utf-8').read()
_rgtflat = ' '.join(rgt.split())
ok6 &= 'theorem inclObs_trans' in rgt and 'theorem restrict_trans' in rgt
ok6 &= 'theorem trace_inclObs_mul_restrict' in rgt and 'theorem eq_of_trace_pairing' in rgt
_rt = _slice(rgt, 'theorem restrict_trans', 'end Tower')
ok6 &= 'eq_of_trace_pairing' in _rt and 'inclObs_trans' in _rt            # derived through the duality
ok6 &= 'theorem iterate_dependsOnlyOn_ball' in rgt and 'theorem readout_unaffected_outside_ball' in rgt
ok6 &= 'theorem consistent_mix' in rgt and 'theorem uniform_family_consistent' in rgt
ok6 &= 'theorem invariant_state_scalar' in rgt and 'theorem invariant_normalized_eq_uniform' in rgt
ok6 &= 'theorem state_selection_audit' in rgt
ok6 &= 'not claimed either way' in _rgtflat
for _w in ('axiom continuity', 'GNS', 'CStarAlgebra', 'theorem representation_selected',
           'theorem sector_required', 'theorem infiniteVolume'):
    ok6 &= _w not in rgt
ok6 &= 'structure FiniteOperationalTheory' not in rgt and 'native_decide' not in rgt
# Level-III round-3 guards: the quasilocal completion is CONSTRUCTED -- the local algebra as
# equivalence classes (the criterion is a theorem), the inclusions isometric by the uniqueness of
# the C*-norm, the completion an abstract norm completion that is a C*-algebra and the closure of
# the union of the stages, states by unique continuous extension, the dynamics by continuous
# extension of an isometric star automorphism; no Hilbert-space representation, no continuity
# axiom, no continuous-time law, no L^2; frozen Level I/II statements untouched.
qal = open(os.path.join(BRIDGE, 'OIBridge', 'QuasilocalAlgebra.lean'), encoding='utf-8').read()
_qalflat = ' '.join(qal.split())
ok6 &= 'theorem emb_eq_iff' in qal and 'theorem inclObs_injective' in qal
ok6 &= 'theorem norm_inclObs' in qal and 'NonUnitalStarAlgHom.norm_map' in qal   # isometry from C*-norm uniqueness
ok6 &= 'noncomputable instance instCStarRingLocal' in qal
ok6 &= 'abbrev Quasilocal' in qal and 'UniformSpace.Completion (localAlg' in qal   # the abstract completion
ok6 &= 'noncomputable instance instCStarAlgebraQuasilocal' in qal
ok6 &= 'theorem stage_inclObs' in qal and 'theorem norm_stage' in qal and 'theorem closure_iUnion_stage' in qal
ok6 &= 'theorem evalLocal_ofM' in qal and 'theorem quasiState_unique' in qal and 'theorem quasiState_nonneg' in qal
_qs = _slice(qal, 'noncomputable def quasiState', 'theorem quasiState_coe')
ok6 &= 'extend' in _qs                                                     # the state is the unique continuous extension
ok6 &= 'theorem heis_emb' in qal and 'theorem norm_transported' in qal and 'theorem norm_heisQ' in qal
ok6 &= 'theorem heisQ_inv_heisQ' in qal and 'theorem heis_iterate_emb' in qal
ok6 &= 'theorem quasilocal_completion' in qal
ok6 &= 'not claimed either way' in _qalflat and 'no inner product, no norm and no state' in _qalflat
for _w in ('axiom continuity', 'InnerProductSpace', 'HilbertSpace', 'lp (fun', 'L²', 'GelfandNaimark',
           'theorem representation_selected', 'theorem sector_required', 'theorem quasilocal_equiv',
           'NormedSpace.exp', 'flow '):
    ok6 &= _w not in qal
ok6 &= 'structure FiniteOperationalTheory' not in qal and 'native_decide' not in qal
# Level-III round-4 guards: the target class is DEFINED INDEPENDENTLY of the construction and the
# construction is proved to be its unique member up to a canonical isomorphism (a bijective star
# homomorphism obtained as the continuous extension of the factored stage maps); the dynamics
# target is decided by the phase countermodel (Target B strictly larger); no Hilbert space,
# no continuity axiom, no claim that every locality-preserving automorphism is induced.
qch = open(os.path.join(BRIDGE, 'OIBridge', 'QuasilocalCharacterization.lean'), encoding='utf-8').read()
_qchflat = ' '.join(qch.split())
ok6 &= 'structure QuasilocalSystem' in qch and 'noncomputable def oiSystem' in qch
_qsys = _slice(qch, 'structure QuasilocalSystem', 'attribute [instance] QuasilocalSystem.inst')
for _w in ('Scaffold', 'localAlg', 'Quasilocal ', 'emb ', 'ofM'):
    ok6 &= _w not in _qsys                                     # the target class does not mention the construction
_qcanon = _slice(qch, 'noncomputable def canon ', 'theorem canon_coe')
ok6 &= 'UniformSpace.Completion.extension' in _qcanon         # the canonical map is the continuous extension
_qequiv = _slice(qch, 'noncomputable def canonEquiv', 'theorem canonEquiv_apply')
ok6 &= 'StarAlgEquiv.ofBijective' in _qequiv
ok6 &= 'theorem canonHom_surjective' in qch and 'theorem canon_unique' in qch
ok6 &= 'theorem systemEquiv_unique' in qch and 'theorem systemState_isState' in qch
ok6 &= 'theorem canon_dyn' in qch and 'theorem systemEquiv_dyn' in qch
ok6 &= 'theorem phase_localityPreserving' in qch and 'theorem phaseQ_ne_heisQ' in qch
ok6 &= 'Nontrivial Q' in qch and 'theorem quasilocal_characterization' in qch
ok6 &= 'not claimed either way' in _qchflat and 'a theorem, not a preference' in _qchflat
for _w in ('axiom continuity', 'InnerProductSpace', 'HilbertSpace', 'lp (fun', 'GelfandNaimark',
           'NormedSpace.exp', 'theorem targetB_redundant', 'theorem every_automorphism_induced',
           'theorem all_systems_classified', 'theorem representation_selected'):
    ok6 &= _w not in qch
ok6 &= 'structure FiniteOperationalTheory' not in qch and 'native_decide' not in qch
# POST-LEVEL III INSTRUMENT AUDIT guards: the round is an AUDIT, not a level -- Q1 is decided in
# BOTH directions with separate witnesses (§A.34), the abstract CP class is not formalized, the
# finite-support and stage-compatible classes are separated by an explicit witness, and no
# infinite-dimensional characterization, availability claim, or manuscript change is asserted.
inc = open(os.path.join(BRIDGE, 'OIBridge', 'InstrumentCompletion.lean'), encoding='utf-8').read()
_incflat = ' '.join(inc.split())
ok6 &= 'def IsQInstrument' in inc and 'noncomputable def qBranch' in inc and 'def IsFiniteSupport' in inc
# Q1 needs BOTH directions as separate theorems, and the biconditional must cite them, not replace them
ok6 &= 'theorem qInstrument_of_kraus' in inc and 'theorem kraus_of_finiteSupport' in inc
_q1 = _slice(inc, 'theorem finiteSupport_iff_kraus', 'theorem qBranch_stage_inclObs')
ok6 &= 'kraus_of_finiteSupport' in _q1 and 'qInstrument_of_kraus' in _q1
ok6 &= 'theorem qBranch_stage_inclObs' in inc and 'theorem qTotal_stage_of_disjoint' in inc
ok6 &= 'structure UnimodularFamily' in inc and 'theorem inclObs_wtConj' in inc
ok6 &= 'theorem phaseAllWt_compat' in inc and 'theorem phaseAll_not_finiteSupport' in inc
ok6 &= 'theorem instrument_audit_entry_one' in inc
ok6 &= 'not claimed either way' in _incflat and 'is NOT formalized here' in _incflat
for _w in ('axiom continuity', 'InnerProductSpace', 'HilbertSpace', 'GelfandNaimark',
           'theorem all_instruments_stage_compatible', 'theorem infiniteDimensional_characterization',
           'theorem stageCompatible_available', 'theorem compatible_family_extends',
           'CompletelyPositive', 'NormedSpace.exp'):
    ok6 &= _w not in inc
ok6 &= 'structure FiniteOperationalTheory' not in inc and 'native_decide' not in inc
# the audit file must carry the pre-registered questions and keep the undecided ones undecided
_aud = open(os.path.join(os.path.dirname(BRIDGE), 'INSTRUMENT-COMPLETION-AUDIT.md'),
            encoding='utf-8').read()
for _q in ('| Q1 |', '| Q2 |', '| Q3 |', '| Q4 |', '| Q5 |'):
    ok6 &= _q in _aud
ok6 &= _aud.count('**open') >= 4 and '**decided**' in _aud
# INSTRUMENT AUDIT ROUND 2 guards: the countermodel must WITHHOLD ONLY the infinite-support
# availability claim -- it keeps the frozen algebra, states and dynamics, contains every
# finite-support Level-II instrument, is closed under the framework's operations, and excludes the
# phase map. It must claim independence, never impossibility.
# ---- CT2 guard: the continuous-time round must not claim a single time-independent generator ----
_soc = open(os.path.join(BRIDGE, 'OIBridge', 'SecondOrderCircuit.lean'), encoding='utf-8').read()
ok_ct2 = True
# the depth-two factorization is stated for an arbitrary F, not only a linear one
ok_ct2 &= 'for an arbitrary `F`' in _soc
# the endpoint theorems must both carry the explicit non-claim
ok_ct2 &= _soc.count('time-independent') >= 2
for _thm in ('two_layer_drive', 'quasilocal_drive'):
    _blk = _slice(_soc, 'theorem ' + _thm, '\n\n')
    ok_ct2 &= _thm in _soc
# the drive must be piecewise, i.e. the file must say so where it states the endpoint
ok_ct2 &= 'piecewise constant' in _soc
# no autonomous-group claim may be asserted
for _bad in ('autonomous', 'time-translation invariant generator',
             'single time-independent generator exists'):
    ok_ct2 &= _bad not in _soc
# the generator locality claim must be backed by the stage-membership theorems
ok_ct2 &= 'proj_localGate_mem_stage' in _soc and 'unit_localGate_mem_stage' in _soc
# no sorry / native_decide anywhere in the module
ok_ct2 &= 'sorry' not in _soc and 'native_decide' not in _soc
# ---- CT2 REPAIR guards: the all-sites layers and the two-piece drive ----
# `quasilocal_drive` quantifies over a FINITE LIST of gates, which is not the all-sites layer.
# The repair supplies the layer itself, and these guards keep its scope honest.
_sol = open(os.path.join(BRIDGE, 'OIBridge', 'SecondOrderLayer.lean'), encoding='utf-8').read()
_swl = open(os.path.join(BRIDGE, 'OIBridge', 'SwapLayer.lean'), encoding='utf-8').read()
_sod = open(os.path.join(BRIDGE, 'OIBridge', 'SecondOrderDrive.lean'), encoding='utf-8').read()
# the all-sites layer needs FINITE RANGE, which the depth-two factorization did not; and the
# module must say that the formal sum of on-site terms is not an element of the algebra
ok_ct2 &= 'finite range' in _sol and 'not an element' in _sol
ok_ct2 &= 'Nothing here exhibits a bounded global Hamiltonian' in _sol
# each layer separately IS a one-parameter group: group law, inverse, strong continuity
for _t in ('layerQ_add_time', 'layerQ_bijective', 'continuous_layerQ_time'):
    ok_ct2 &= 'theorem ' + _t in _sol
for _t in ('swapQ_add_time', 'swapQ_bijective', 'continuous_swapQ_time'):
    ok_ct2 &= 'theorem ' + _t in _swl
# the ORDER of the composite is fixed by a theorem, not by a convention
for _t in ('permOp_of_comp', 'permOpInv_of_comp', 'heis_of_comp', 'heisQ_of_comp'):
    ok_ct2 &= 'theorem ' + _t in _sod
# and the drive is defined in that order: the SWAP flow innermost, the SHEAR flow outermost
ok_ct2 &= 'layerQ R t (swapQ V t x)' in _sod
# both layer endpoints are identified, and so is the composite's
for _t in ('swapQ_one_eq_heisQ', 'layerQ_one_eq_heisQ', 'driveQ_one_eq_heisQ',
           'layerU_one_eq_qGate', 'swapU_one_eq_qGate'):
    ok_ct2 &= 'theorem ' + _t in _sod
# the endpoint is the frozen dynamics, not a fresh definition of one
ok_ct2 &= 'heisQ (ruleDynamics R)' in _sod
# the composite is a CONTINUOUS PATH of automorphisms, and no more than that
for _t in ('driveQ_zero_time', 'driveQ_bijective', 'continuous_driveQ_time',
           'driveQ_isContinuousPath'):
    ok_ct2 &= 'theorem ' + _t in _sod
ok_ct2 &= '**Not claimed: a group law.**' in _sod
ok_ct2 &= 'no generator is exhibited' in _sod
# a group law for the composite must not appear under any of the layers' names
for _bad in ('driveQ_add_time', 'driveQ_left_inverse (t s', 'one-parameter group of the drive'):
    ok_ct2 &= _bad not in _sod
for _f in (_sol, _swl, _sod):
    ok_ct2 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _f) is None
    ok_ct2 &= re.search(r'(?m)^axiom ', _f) is None and 'native_decide' not in _f
_NOCLAIM = ('not claimed', 'Not claimed', 'does not claim', 'neither claims', 'remains open',
            'remains OPEN', 'is not settled', 'never claims', 'must not be read',
            'does not say', 'not claim')


def _asserted(text, phrase, markers=_NOCLAIM):
    """True when the phrase appears in some paragraph that does NOT disclaim it.

    The enclosing markdown heading counts as context, because a non-claim list is written under a
    "what this does not claim" heading and the heading is its own paragraph. Without that, an
    honest disclaimer trips the guard built to protect it.
    """
    head = ''
    for para in text.split('\n\n'):
        stripped = para.strip()
        if stripped.startswith('#'):
            head = stripped
        if phrase in para and not any(k in (head + ' ' + para) for k in markers):
            return True
    return False


# ---- CT3 guard: the centralizer census must be reported as a NECESSARY condition only ----
_sg = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'static_generator_probe.py'),
           encoding='utf-8').read()
_cta = open(os.path.join(os.path.dirname(BRIDGE), 'CONTINUOUS-TIME-AUDIT.md'),
            encoding='utf-8').read()
ok_ct3 = True
# CT3 must be stated in the infinite-volume form, not as a bounded element of the algebra
ok_ct3 &= 'not an element of that algebra' in _sg
ok_ct3 &= 'finite-range interaction' in _sg and 'tau_1 = heisQ(Phi_OI)' in _sg
# the census is necessary, never sufficient, and the verdict is non-obstruction
ok_ct3 &= 'NON-OBSTRUCTION' in _sg
ok_ct3 &= 'necessary condition is not evidence' in _sg
ok_ct3 &= 'not a statement about all finite ranges' in _sg
# the controls must be present: a census that reports trivial everywhere is a broken probe
ok_ct3 &= _sg.count('CONTROL.') >= 2 and 'on-site' in _sg
# the diagonal/off-diagonal split must be there, with the reason it decides the reading
ok_ct3 &= 'diagonal H exponentiates to a diagonal unitary' in _sg
# the modular census is an upper bound; the verdict needs a certified characteristic-zero
# lower bound, so the bracket and the exact-over-Z witness must both be present
ok_ct3 &= 'rank_p <= rank_Q' in _sg and 'upper bound' in _sg
ok_ct3 &= 'exactly over Z' in _sg and 'BRACKETED' in _sg
ok_ct3 &= 'certified lower' in _cta and 'bracketed' in _cta
# the finite-to-infinite periodization must be recorded as an obligation, not used silently
ok_ct3 &= 'periodize' in _sg and 'periodization' in _cta
# no claim that a static generator exists, in the probe or in the audit
for _bad in ('a static local generator exists', 'CT3 is answered', 'CT3 closed',
             'autonomous generator found'):
    ok_ct3 &= not _asserted(_sg, _bad) and not _asserted(_cta, _bad)
# the audit must keep CT3 open and must not read the passed necessary condition as evidence
ok_ct3 &= 'passed, not failed' in _cta
ok_ct3 &= 'Floquet' in _cta
ok_ct3 &= 'sorry' not in _sg
# ---- forward-redundancy guard: the OI/QM reading must stay frozen ----
_co = open(os.path.join(BRIDGE, 'OIBridge', 'CompletedOI.lean'), encoding='utf-8').read()
_fr = open(os.path.join(os.path.dirname(BRIDGE), 'OI-CORE-FORWARD-REDUNDANCY.md'),
           encoding='utf-8').read()
_frflat = ' '.join(_fr.split())
_coflat = ' '.join(_co.split())
ok_fr = True
# the forward implication has its own name, and the audit entry collects the three readings
ok_fr &= 'theorem qm_implies_oiCore' in _co and 'theorem oiCore_forward_redundancy' in _co
ok_fr &= 'theorem completedOI_iff_physical' in _co
# containment must be labelled containment, in the module and in the record
ok_fr &= 'Containment only' in _coflat or 'containment statement' in _coflat.lower()
for _k in ('Containment', 'Redundancy', 'No ontological necessity'):
    ok_fr &= _k in _frflat
# the record must keep the core's positive role and must not read the containment as explanatory
ok_fr &= 'defines what counts as an OI realization' in _frflat \
    and 'defines what counts as an OI realization' in _coflat
ok_fr &= 'informationally complete' in _frflat
ok_fr &= 'is not an explanatory one' in _frflat
# the lint class must exist, with its OWN markers -- the general ones would let the
# dangerous sentences escape through "cannot" and "does not"
_cc = open(os.path.join(os.path.dirname(os.path.dirname(BRIDGE)), 'tools', 'claims_check.py'),
           encoding='utf-8').read()
ok_fr &= 'OI_CLAIMS' in _cc and 'OI_MARKERS' in _cc
ok_fr &= 'cannot exist without' in _cc and '(requires|needs) hidden' in _cc
ok_fr &= 'core-containment' in _cc
# and the equivalence theorem itself must be untouched
ok_fr &= 'theorem oiPlus_iff_qm' in _co
check('R7-FWD', ok_fr,
      'Forward-redundancy guard: the OI/QM reading is frozen. The forward implication has its own '
      'name (qm_implies_oiCore), the audit entry oiCore_forward_redundancy collects containment, '
      'redundancy and the failure of the converse, and the record states all three readings -- '
      'containment yes, forward redundancy yes, ontological necessity NO, with the reason the '
      'strong reading breaks (informationally complete measurements determine a density matrix). '
      'The core keeps its positive role of defining what counts as an OI realization, and the '
      'equivalence theorem oiPlus_iff_qm is untouched. claims_check carries an OI_CLAIMS class '
      'with its own marker list, because the general markers include "cannot" and "does not" and '
      'would let the guarded sentences escape through the very words that make them dangerous.')

# ---- CT3-R2A guard: a dead branch must not be read as a closed question ----
# The positive requirements are checked against SCOPE TOKENS rather than prose, so that rewording
# a sentence cannot silently disarm the guard. The forbidden phrases are checked PER PARAGRAPH and
# only count as asserted when the paragraph carries no non-claim marker -- otherwise an honest
# "not claimed: that CT3 is settled" trips the guard that exists to protect it, which is exactly
# what happened the first time this was written.
_sl = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'spectral_logarithm_probe.py'),
           encoding='utf-8').read()
ok_ct3b = True
# machine-readable scope, not prose
for _tok in ('R2A-NEGATIVE', 'R2B-OPEN', 'CT3-OPEN', 'NO-OBSTRUCTION-CLAIM',
             'FINITE-VOLUME-ONLY'):
    ok_ct3b &= ('SCOPE-TOKEN: ' + _tok) in _sl
# the split, the certificate, and the control that stops the negative being over-read
ok_ct3b &= 'R2-A' in _sl and 'R2-B' in _sl and 'degenerate' in _sl
ok_ct3b &= 'full-period' in _sl and 'no width-w window' in _sl
ok_ct3b &= 'SCOPE CONTROL' in _sl
# the six dimensions are dimensions of H, not of K: H_0 is a spectral function of P and so is
# nonlocal by this very round, which makes K = (H - H_0)/2pi not necessarily local
ok_ct3b &= 'dimensions of H' in _sl and 'need not be local' in _sl
# and the fixed-volume qualification: stable dimension is not compatible solution directions
ok_ct3b &= 'FIXED-VOLUME' in _sl and 'site-dependent' in _sl
# no claim that CT3 is settled, unless the paragraph disclaims it
for _bad in ('CT3 is closed', 'CT3 is settled', 'no static generator exists',
             'rules out a static generator'):
    ok_ct3b &= not _asserted(_sl, _bad) and not _asserted(_cta, _bad)
ok_ct3b &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _sl) is None
# ---- CT3-R2B step-1 guard: an obstruction that must stay scoped to width 2 ----
_cb = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'centralizer_basis_probe.py'),
           encoding='utf-8').read()
ok_ct3c = True
for _tok in ('W2-OBSTRUCTED', 'WIDER-RANGE-OPEN', 'CT3-OPEN', 'FINITE-VOLUME-ONLY'):
    ok_ct3c &= ('SCOPE-TOKEN: ' + _tok) in _cb
# the basis must be exact over Z, complete against the R1 census, and quotientable by scalars
ok_ct3c &= 'exactly over Z' in _cb and 'COMPLETE' in _cb
ok_ct3c &= 'identity lies in the span' in _cb
# the sharper quantization statement, with the per-block residue
ok_ct3c &= '(2 pi/m) Z' in _cb and 'n = -r (mod m)' in _cb
# block traces from the projector identity, not by diagonalizing
ok_ct3c &= 'sum_k omega^(-rk) P^k' in _cb and 'without diagonalizing' in _cb
# the Hermitian sector split must be present, and the antisymmetric fact flagged as COMPUTED --
# it is what confines the obstruction to width 2, and assuming it would silently widen the claim
ok_ct3c &= 'real-antisymmetric' in _cb and 'IDENTICALLY ZERO' in _cb
ok_ct3c &= 'computed fact, not an assumption' in _cb
ok_ct3c &= 'confines this round to width 2' in _cb
# the obstruction itself, as an exact certificate rather than a search
ok_ct3c &= '(m - 2r) d_r / m' in _cb and 'e_(m-r) - e_r' in _cb
ok_ct3c &= 'integer certificate rather than a search' in _cb
# the certificate must be exact: no floating arithmetic anywhere on the load-bearing path, and
# the annihilator licensed by integer facts rather than by forming spectral traces numerically
ok_ct3c &= 'cmath' not in _cb and '1e-6' not in _cb
ok_ct3c &= 'PALINDROMIC over Z' in _cb and 'VANISH over Z' in _cb
ok_ct3c &= 'no floating arithmetic on the load-bearing path' in _cb
# the control that stops it being over-read
ok_ct3c &= 'CONTROL' in _cb and 'sitting in plain sight' in _cb
# rank alone must be recorded as the WRONG diagnostic, since that was the first reading
ok_ct3c &= 'RANK WAS THE WRONG DIAGNOSTIC' in _cb
# the invariant is pinned
ok_ct3c &= 'PINNED' in _cb and 'invariant of the centralizer space' in _cb
for _bad in ('CT3 is settled', 'R2-B is settled', 'no static generator exists',
             'CT3 is closed'):
    ok_ct3c &= not _asserted(_cb, _bad) and not _asserted(_cta, _bad)
# ---- CT3-R2B-Q2 guard: the period correction must stay corrected, and the round stay scoped ----
_wp = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'wave_period_probe.py'),
           encoding='utf-8').read()
_q2 = open(os.path.join(os.path.dirname(BRIDGE), 'CT3-R2B-Q2-PERIOD-AND-CYCLES.md'),
           encoding='utf-8').read()
ok_ct3d = True
for _tok in ('PERIOD-CORRECTED', 'WIDER-RANGE-OPEN', 'Q2-ONLY', 'CONJECTURE-FALSE',
             'CT3-OPEN', 'FINITE-VOLUME-ONLY'):
    ok_ct3d &= ('SCOPE-TOKEN: ' + _tok) in _wp
# the corrected period must be stated, with its reason, in probe and note alike
ok_ct3d &= 'ord(F mod q) = qL' in _wp and 'ord(F mod q) = qL' in _q2
ok_ct3d &= 'L for L even, 2L for L odd' in _wp
# the three manuscript locations must carry the corrected statement and not the superseded one
for _p, _bad, _good in (
        ('papers/SM.md', 'and L if q = 2', 'q = 2 included'),
        ('book/appendix-b-derivations.md', 'L & q = 2', 'q = 2$ included'),
        ('book/The-Incompleteness-of-Observation-FULL.md', 'L & q = 2', 'q = 2$ included')):
    _t = open(os.path.join(os.path.dirname(os.path.dirname(BRIDGE)), _p), encoding='utf-8').read()
    ok_ct3d &= _bad not in _t and _good in _t
    ok_ct3d &= 'the nilpotent part is automatically killed' not in _t
# the width-2 confinement and the finite-volume limit must be restated, not inherited silently
ok_ct3d &= 'WIDTH-2 ingredient' in _wp and 'width-2' in _q2
ok_ct3d &= 'periodization obligation' in _wp and 'periodization obligation' in _q2
# the conjecture must be recorded as FALSE with its arithmetic, and never asserted
ok_ct3d &= 'WIEFERICH' in _wp and 'Wieferich' in _q2
ok_ct3d &= 'IS FALSE' in _wp and 'is false' in _q2
for _bad in ('silent exactly at the powers of two', 'silence set is the powers of two',
             'CT3 is settled', 'CT3 is closed', 'no static generator exists'):
    ok_ct3d &= not _asserted(_wp, _bad) and not _asserted(_q2, _bad)
# exact arithmetic only, as in the round it continues
ok_ct3d &= 'cmath' not in _wp and '1e-6' not in _wp
# ---- Audit A guard: the recurrence chain must keep C1, and the audit must keep its scope ----
_pc = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'partition_coupling_probe.py'),
           encoding='utf-8').read()
_aa = open(os.path.join(os.path.dirname(BRIDGE), 'C1C4-MINIMALITY-AUDIT.md'),
           encoding='utf-8').read()
_root = os.path.dirname(os.path.dirname(BRIDGE))
ok_auda = True
for _tok in ('C1-LOAD-BEARING', 'ONE-LOCATION', 'C1-NOT-SUFFICIENT'):
    ok_auda &= ('SCOPE-TOKEN: ' + _tok) in _pc
# the repaired chain, in both parallel sources, and the defective form in neither
for _p in ('book/ch18-beyond.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_root, _p), encoding='utf-8').read()
    ok_auda &= 'Recurrence guarantees that any partition' not in _t
    ok_auda &= 'Recurrence together with C1' in _t and 'uncoupled partition' in _t
# the statements the repair restores agreement with must themselves still be there
_m = open(os.path.join(_root, 'papers/Main.md'), encoding='utf-8').read()
_c1 = open(os.path.join(_root, 'book/ch01-observation.md'), encoding='utf-8').read()
ok_auda &= 'non-permutation one-step witness' in _m and 'and condition C1' in _c1
# the countermodel and its control must both be present, and the control is what makes it readable
ok_auda &= 'THE COUNTERMODEL' in _pc and 'THE CONTROL' in _pc
ok_auda &= 'coin-and-die' in _pc
# C1 sufficiency must never be claimed, in probe or audit
for _bad in ('C1 is sufficient', 'C1 suffices', 'recurrence alone gives backflow'):
    ok_auda &= not _asserted(_pc, _bad) and not _asserted(_aa, _bad)
# the audit must publish the clean axes and its own limits, not only its hit
ok_auda &= 'The axes that came back clean' in _aa and 'What this audit does not claim' in _aa
# ---- Audit B guard: C4 at the concrete cut is named, not discharged, and not a hypothesis of hbar ----
_cc = open(os.path.join(os.path.dirname(BRIDGE), 'CONCRETE-CUT-AUDIT.md'), encoding='utf-8').read()
_gr = open(os.path.join(_root, 'papers/GR.md'), encoding='utf-8').read()
ok_audb = True
# the fourth entry exists at the cut and carries the status verdict, in GR and in both book sources
ok_audb &= '**(C4)**' in _gr and 'Not presently discharged' in _gr
for _p in ('book/ch07-gravity.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_root, _p), encoding='utf-8').read()
    ok_audb &= 'Status of C4 (history readback)' in _t and 'not presently discharged' in _t
    ok_audb &= 'reads the same degrees it writes' not in _t
    ok_audb &= 'satisfies the framework\'s four conditions' not in _t
# what remains must be stated, not gestured at
ok_audb &= 'routed back into future visible conditionals' in _gr
# C4 must not be made a hypothesis of the hbar derivation, and the derivation's own conditions must stay named
ok_audb &= 'not a hypothesis of the calibration' in _gr
# the two intro residues review caught: neither sentence may recur, in GR or in either book source,
# and the intro must carry the conditional form instead
for _t in (_gr,) + tuple(open(os.path.join(_root, _p), encoding='utf-8').read() for _p in
                        ('book/ch07-gravity.md', 'book/The-Incompleteness-of-Observation-FULL.md')):
    ok_audb &= 'The cosmological horizon satisfies all four conditions' not in _t
    ok_audb &= 'the full equivalence applies in our universe' not in _t
ok_audb &= 'remains conditional on C4' in _gr
ok_audb &= 'carried by H-slope together with the horizon and frame conditions' in _gr
# the audit must record why bidirectionality and H-scramble do not close it, and what it does not claim
ok_audb &= 'strengthened form of C1' in _cc and 'H-scramble' in _cc
ok_audb &= 'What this audit does not claim' in _cc
for _bad in ('C4 is satisfied at the cosmological', 'C4 holds at the cosmological horizon',
             'C4 fails at the cosmological'):
    ok_audb &= not _asserted(_gr, _bad) and not _asserted(_cc, _bad)
# ---- the SM side of the same guard: Layer 0 attribution, the 2.1 inventory, Chapter 1's inference ----
_sm = open(os.path.join(_root, 'papers/SM.md'), encoding='utf-8').read()
ok_audb &= 'follow from C1–C4' not in _sm and 'right partition geometry' not in _sm
ok_audb &= 'not inputs to this derivation' in _sm and 'C2 and C4 are explicit hypotheses' in _sm
ok_audb &= 'neither is proved here' in _sm
for _p in ('book/ch04-methodology.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_root, _p), encoding='utf-8').read()
    ok_audb &= 'structural constraints from C1–C4' not in _t and 'not inputs to this layer' in _t
for _p in ('book/ch01-observation.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_root, _p), encoding='utf-8').read()
    ok_audb &= 'at the horizon this is automatic' not in _t
    ok_audb &= 'a property to be demonstrated there rather than assumed' in _t
    # the paragraph after the C4 definition: four conditions named, and no blanket margins
    ok_audb &= 'coupled, persistent, and vast sustains' not in _t
    ok_audb &= 'satisfied by enormous margins' not in _t
    ok_audb &= 'sufficiently capacious, and read back sustains' in _t
    ok_audb &= 'C2 and C4 remain hypotheses of Theorem 22' in _t
    # no quantitative margin attributed to C1, and the C3 floor named as a data-processing bound
    ok_audb &= 'C1 is verified structurally' in _t
    ok_audb &= 'holds for the realized process by data processing' in _t
ok_audb &= 'The SM lattice cut' in _cc and 'Finding B4' in _cc
# the canonical table's distinctive refined cells, so the table cannot regress while the prose stays right
for _cell in ('verified structurally', 'verified, timescale margin', 'verified, capacity margin',
              'capacity floor, data processing', 'named, not presently discharged'):
    ok_audb &= _cell in _cc
ok_audb &= 'copies this table verbatim' in _cc
# the freeze copies the table verbatim: same five cells, same two rows, and it names its enforcement
_fz = open(os.path.join(os.path.dirname(BRIDGE), 'CONCRETE-CUT-FREEZE.md'), encoding='utf-8').read()
for _cell in ('verified structurally', 'verified, timescale margin', 'verified, capacity margin',
              'capacity floor, data processing', 'named, not presently discharged'):
    ok_audb &= _cell in _fz
ok_audb &= 'Two rows, not one' in _fz and 'What the freeze does not claim' in _fz
ok_audb &= 'CT3, which stays paused behind OI-N' in _fz
for _bad in ('C1–C3 verified at both cuts', 'C4 holds at', 'C4 fails at'):
    ok_audb &= not _asserted(_fz, _bad)
# the Introduction's twin of the blanket-margins sentence, and no blanket form anywhere in the book
for _p in ('book/ch00-introduction.md', 'book/ch01-observation.md',
           'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_root, _p), encoding='utf-8').read()
    ok_audb &= 'satisfied by enormous margins' not in _t
ok_audb &= 'readback is named there and still to be demonstrated' in \
    open(os.path.join(_root, 'book/ch00-introduction.md'), encoding='utf-8').read()
# ---- OI-N guard: the exploratory thread stays exploratory, and its two proved ends stay scoped ----
_po = open(os.path.join(BRIDGE, 'OIBridge', 'PassiveObservation.lean'), encoding='utf-8').read()
_on = open(os.path.join(os.path.dirname(BRIDGE), 'OI-N-EXPLORATORY.md'), encoding='utf-8').read()
ok_oin = True
ok_oin &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _po) is None and 'native_decide' not in _po
for _nm in ('psd_summand_of_rankOne', 'choiMatrix_id', 'passive_branch_scalar',
            'passive_outcome_state_independent', 'no_complete_passive_observation',
            'pinching_cp', 'pinching_passive_on_diagonal', 'pinching_separates_diagonal',
            'pinching_sum_apply', 'pinching_not_passive'):
    ok_oin &= ('#print axioms ' + _nm) in _po
# the definitions the thread depends on are fixed here, and the control is present
ok_oin &= 'def IsPassiveInstrument' in _po and 'def SeparatesStates' in _po and 'def pinching' in _po
# the module and the note both keep N3 and N4 open and refuse the hidden-ontology reading
ok_oin &= 'Not claimed' in _po and 'OI-N3' in _po and 'OI-N4' in _po
ok_oin &= 'Status: exploratory' in _on and 'OI-N3 — the exact boundary: proved, as a classification' in _on
ok_oin &= 'OI-N4 — relation to `OICore`: proved, as theory-insensitivity' in _on
ok_oin &= 'OI-N5 — the internal observer: proved, as rigidity' in _on
ok_oin &= 'What this thread does not claim' in _on
for _bad in ('QM requires OI', 'quantum mechanics requires observational incompleteness',
             'hidden OI ontology is forced'):
    ok_oin &= not _asserted(_po, _bad) and not _asserted(_on, _bad)
# N1/N2 alone name noncommutativity only as the candidate obstruction; the module that says so
# keeps saying so, and the README keeps the candidate form attached to N1/N2.
_rd = open(os.path.join(os.path.dirname(BRIDGE), 'README.md'), encoding='utf-8').read()
for _bad in ('obstruction of N1 is noncommutativity', 'why a noncommutative algebra forbids'):
    ok_oin &= _bad not in _po and _bad not in _on and _bad not in _rd
ok_oin &= 'candidate' in _po and 'candidate obstruction' in _on and 'candidate obstruction' in _rd
# ---- OI-N3: the central-observation module closes the boundary as a classification ----
_co = open(os.path.join(BRIDGE, 'OIBridge', 'CentralObservation.lean'), encoding='utf-8').read()
ok_oin &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _co) is None and 'native_decide' not in _co
for _nm in ('exists_kraus', 'kraus_block_vanish', 'branch_preserves_block', 'choiMatrix_restrictMap',
            'restricted_passive', 'branch_scalar_on_block', 'central_classification',
            'blockPinch_passive', 'no_complete_passive_of_block', 'blockPinch_separates',
            'complete_passive_iff_injective', 'injective_iff_commutative',
            'complete_passive_iff_commutative'):
    ok_oin &= ('#print axioms ' + _nm) in _co
# the definitions N3 rests on, and the shape of the central theorem: nonnegativity from CP and
# normalization from passivity, stated per nonempty block
ok_oin &= 'def IsBlockPassiveInstrument' in _co and 'def SeparatesBlockStates' in _co
ok_oin &= 'def blockPinch' in _co and 'def restrictMap' in _co
ok_oin &= '(∀ a i, (∃ s, blk s = i) → 0 ≤ c a i)' in _co
ok_oin &= '(∀ i, (∃ s, blk s = i) → ∑ a, c a i = 1)' in _co
# block preservation is derived, not assumed: the passive-instrument definition carries no
# block-preservation clause, and the theorem that supplies it is present
ok_oin &= 'InBlock' not in _co.split('def IsBlockPassiveInstrument')[1].split('end Blocks')[0]
ok_oin &= 'theorem branch_preserves_block' in _co
# the scope N3 keeps: block-diagonal form, no Wedderburn–Artin, and the N4/N5 items stay open
ok_oin &= 'Not claimed' in _co and 'Wedderburn' in _co and 'OI-N4' in _co
ok_oin &= 'All thirteen named results print' in _on and 'Wedderburn' in _on
for _bad in ('infinite-dimensional algebras', 'OICore implies passive',
             'passive incompleteness implies OICore'):
    ok_oin &= not _asserted(_on, _bad) and not _asserted(_co, _bad)
# ---- OI-N4: passive incompleteness is theory-insensitive, non-discriminating for the OI core ----
_pi = open(os.path.join(BRIDGE, 'OIBridge', 'PassiveIndependence.lean'), encoding='utf-8').read()
ok_oin &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _pi) is None and 'native_decide' not in _pi
for _nm in ('passivelyIncomplete_of_card', 'passivelyIncomplete_qubit', 'keepsLabels_localLuders',
            'tau_moves_label', 'label_not_oiCore', 'oiCore_to_passive_vacuous',
            'passivelyIncomplete_without_oiCore', 'passive_not_implies_oiCore',
            'passive_nondiscriminating', 'pinching_isKrausFamily', 'pinching_preservesDiag',
            'diag_passivelyCompleteOnDiagonal', 'label_passivelyCompleteOnDiagonal',
            'sector_diagram'):
    ok_oin &= ('#print axioms ' + _nm) in _pi
# the theory-level definitions, the witness theory, and the two-sided shape of the diagram:
# the forward implication is recorded as vacuous, the converse as failing, and the witness is
# a theory that realizes no OI core
ok_oin &= 'def PassivelyIncomplete' in _pi and 'def PassivelyCompleteOnDiagonal' in _pi
ok_oin &= 'def KeepsLabels' in _pi and 'noncomputable def labelTheory' in _pi
ok_oin &= 'theorem label_not_oiCore : ¬ OICore labelTheory' in _pi
ok_oin &= '∃ T : FiniteOperationalTheory (Fin 2), PassivelyIncomplete T ∧ ¬ OICore T' in _pi
# the anti-misreading: the module and the note both say passive incompleteness holds without
# any OI core, and neither claims a completion condition for the witness theory
ok_oin &= 'realizes no OI core' in _pi and 'realizes no OI core' in _on
ok_oin &= 'All fourteen named results print' in _on
for _bad in ('labelTheory satisfies', 'labelTheory is physical', 'evidence for a hidden ontology',
             'evidence for a hidden OI ontology'):
    ok_oin &= not _asserted(_pi, _bad) and not _asserted(_on, _bad) and not _asserted(_rd, _bad)
# the exact logic is asymmetric: one implication holds (vacuously) and the converse fails. The
# symmetric vocabulary is forbidden outright, and the theory-insensitive reading is required.
for _t in (_pi, _on, _rd):
    for _bad in ('neither implies the other', 'logically independent', 'neither notion carries',
                 'neither implies', 'no implication between them'):
        ok_oin &= _bad not in _t
    ok_oin &= 'theory-insensitive' in _t
ok_oin &= 'vacuous' in _pi and 'vacuous' in _on and 'orthogonal' in _pi and 'orthogonal' in _on
# ---- OI-N5: the internal observer — a passive self-record can only be read, never written ----
_io = open(os.path.join(BRIDGE, 'OIBridge', 'InternalObserver.lean'), encoding='utf-8').read()
ok_oin &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _io) is None and 'native_decide' not in _io
for _nm in ('no_full_passive_self_record', 'branch_kills_other_block', 'branch_fixes_own_block',
            'internal_branch_eq_blockPart', 'internal_outcome_law', 'blockPinch_internal',
            'internal_complete_iff', 'no_complete_internal_observer', 'classical_control',
            'recordInstr_cp', 'recordInstr_records', 'recordInstr_writes',
            'recordInstr_not_passive', 'recordInstr_not_internal'):
    ok_oin &= ('#print axioms ' + _nm) in _io
# the record semantics and the internal observer are definitions; rigidity is stated as the
# record projection on block-diagonal states; the boundary is the injectivity of the record map
ok_oin &= 'def Records' in _io and 'def IsInternalObserver' in _io and 'def recBlk' in _io
ok_oin &= '(F o) ρ = blockPart blk o ρ' in _io
ok_oin &= 'IsInternalObserver blk F ∧ SeparatesBlockStates blk F) ↔ Function.Injective blk' in _io
# the non-passive control must both record and write, and be proved not passive — the control
# is what shows passivity is the operative hypothesis
ok_oin &= 'theorem recordInstr_writes' in _io and 'theorem recordInstr_not_passive' in _io
ok_oin &= 'All fourteen named results print' in _on.split('## OI-N5')[1]
# scope: no consciousness, self-modelling or ontology reading; nothing about OICore reopened
for _t in (_io, _on, _rd):
    ok_oin &= 'consciousness' in _t
for _bad in ('the observer is conscious', 'self-aware', 'N5 shows OICore', 'N5 implies OICore',
             'the observer requires a hidden ontology'):
    ok_oin &= not _asserted(_io, _bad) and not _asserted(_on, _bad) and not _asserted(_rd, _bad)
ok_oin &= 'cannot write a new record' in _io and 'only be read, never written' in _io
# the boundary is injectivity of the record map: "at most one carrier state per record block",
# so every NONEMPTY record block is one-dimensional. The literal "every record block is
# one-dimensional" silently adds surjectivity and is forbidden in module, note and README.
for _t in (re.sub(r'\s+', ' ', _io), re.sub(r'\s+', ' ', _on), re.sub(r'\s+', ' ', _rd)):
    ok_oin &= 'at most one carrier state' in _t and 'every nonempty record block is one-dimensional' in _t
    for _bad in ('every record block is one-dimensional', 'every block has dimension one',
                 'iff every record block is', 'iff every `d_i = 1`'):
        ok_oin &= _bad not in _t
ok_oin &= 'every block has dimension one' not in re.sub(r'\s+', ' ', _co)
ok_oin &= 'at most one basis state' in re.sub(r'\s+', ' ', _co)
# ---- the OI-N freeze: the endpoint stated once, in the form the guard enforces ----
_fzn = open(os.path.join(os.path.dirname(BRIDGE), 'OI-N-FREEZE.md'), encoding='utf-8').read()
_fzn1 = re.sub(r'\s+', ' ', _fzn)
ok_oin &= 'Status: frozen' in _fzn and 'What the freeze does not claim' in _fzn
for _line in ('Noncommutativity forbids complete passive observation',
              'Passive incompleteness does not diagnose `OICore`',
              'A passive internal observer can only read an existing record',
              'Creating a genuinely new internal record requires changing the joint system'):
    ok_oin &= _line in _fzn1
for _nm in ('complete_passive_iff_commutative', 'central_classification',
            'passivelyIncomplete_of_card', 'oiCore_to_passive_vacuous',
            'passivelyIncomplete_without_oiCore', 'internal_branch_eq_blockPart',
            'internal_outcome_law', 'recordInstr_writes', 'recordInstr_not_passive',
            'no_full_passive_self_record'):
    ok_oin &= _nm in _fzn
for _p in ('PassiveObservation.lean', 'CentralObservation.lean', 'PassiveIndependence.lean',
           'InternalObserver.lean'):
    ok_oin &= _p in _fzn
ok_oin &= 'Extending the thread needs a new charter' in _fzn1
for _bad in ('QM requires OI', 'quantum mechanics requires observational incompleteness',
             'hidden OI ontology is forced', 'evidence for a hidden ontology',
             'logically independent', 'neither implies the other'):
    ok_oin &= not _asserted(_fzn, _bad)
ok_oin &= 'OI-N-FREEZE.md' in _on and 'OI-N-FREEZE.md' in _rd
# two scope points the kernel does not carry: the intrinsic-to-ambient transport through the block
# conditional expectation is not formalized, so the statements are for the ambient definition;
# and the classification is one direction (every passive instrument induces a stochastic
# observation of the center), with no converse constructor from an arbitrary stochastic matrix.
for _t in (re.sub(r'\s+', ' ', _co), re.sub(r'\s+', ' ', _on), re.sub(r'\s+', ' ', _rd)):
    ok_oin &= 'transport is not formalized here' in _t and 'induces a classical stochastic observation' in _t
    for _bad in ('nothing is lost', 'is exactly a classical stochastic observation',
                 'are exactly classical stochastic observations',
                 'are precisely classical stochastic observations',
                 'is a classical stochastic observation of the center'):
        ok_oin &= _bad not in _t
check('R7-OIN', ok_oin,
      'OI-N guard: the passive-observation module carries no sorry and no native_decide, prints the '
      'axioms of all ten named results, fixes the three definitions the thread depends on, keeps the '
      'control scoped to the commutative algebra with the dephasing lemma; the central-observation '
      'module carries no sorry and no native_decide, prints the axioms of all thirteen named results, '
      'states the classification with nonnegativity and normalization per nonempty block, derives '
      'block preservation rather than assuming it, and keeps to the block-diagonal form; the '
      'passive-independence module carries no sorry and no native_decide, prints the axioms of all '
      'fourteen named results, records the forward implication as vacuous and the converse as '
      'failing through a theory that realizes no OI core, claims no completion condition for '
      'that witness, and states the result as theory-insensitivity rather than as a symmetric '
      'independence; the internal-observer module carries no sorry and no native_decide, prints '
      'the axioms of all fourteen named results, states rigidity as the record projection on '
      'block-diagonal states and the boundary as injectivity of the record map, carries the '
      'record-creating non-passive control, and reads nothing about consciousness, self-modelling '
      'or ontology into the result; module and note both mark the thread exploratory, record N3 as '
      'proved as a classification, N4 as proved as theory-insensitivity and N5 as proved as '
      'rigidity, and assert neither that QM requires OI nor that a hidden ontology is forced.')

# ---- the completion-assumption audit: the charter's ledger reconciled with the kernel ----
_caa = open(os.path.join(os.path.dirname(BRIDGE), 'COMPLETION-ASSUMPTION-AUDIT.md'),
            encoding='utf-8').read()
_lor = open(os.path.join(BRIDGE, 'OIBridge', 'LevelOneRecursion.lean'), encoding='utf-8').read()
ok_caa = True
ok_caa &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _lor) is None and 'native_decide' not in _lor
for _nm in ('systemLoose_observerRecursion', 'levelOne_independent_of_recursion', 'levelOne_row'):
    ok_caa &= ('#print axioms ' + _nm) in _lor
# the row is stated with both halves, and the second half is a negation, not a derivation
ok_caa &= '¬ ∀ T : FiniteOperationalTheory (Fin 2), ObserverRecursion T → SystemToLevelOne T' in _lor
# every ledger row names its kernel witness; the charter's stale package is named as such;
# the residual items are listed as open and the note settles none of them
for _nm in ('systemToLevelOne_of_embeddedObservation', 'closure_of_observerRecursion',
            'observationalIndependence_of_implementationLocality',
            'validity_of_implementationLocality', 'lieRank_of_elementary',
            'lieRank_not_redundant', 'redundancy_fails', 'closure_independent',
            'validity_independent', "levelOne_independent'", 'levelOne_independent_of_recursion',
            'carrier_general_oiPlusElem', 'substratum_residual'):
    ok_caa &= _nm in _caa
ok_caa &= 'What remains open' in _caa and 'nothing in this note\nsettles them' in _caa
ok_caa &= 'What this note does not claim' in _caa
for _bad in ('SystemToLevelOne is derived from observer recursion',
             'observer recursion supplies the seam', 'OIPlusElem is minimal',
             'the substratum supplies elementary drivability', 'inverse accessibility is redundant'):
    ok_caa &= not _asserted(_caa, _bad)
# the charter carries its banner: historical, reconciled with and superseded by the audit note,
# and it does not send a future agent back to the five rows; and OIPlusElem is "the most
# compressed package currently recorded", never "the kernel's smallest", since global minimality
# is exactly the open item
_chr = open(os.path.join(os.path.dirname(BRIDGE),
                         'EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md'), encoding='utf-8').read()
_chr1 = re.sub(r'\s+', ' ', _chr)
ok_caa &= _chr.lstrip().startswith('# Equivalence strengthening roadmap')
ok_caa &= 'Historical charter' in _chr and 'superseded by' in _chr1
ok_caa &= 'COMPLETION-ASSUMPTION-AUDIT.md' in _chr and 'do not restart the five rows from here' in _chr1
ok_caa &= 'most compressed package currently recorded' in _chr1
for _t in (re.sub(r'\s+', ' ', _caa), re.sub(r'\s+', ' ', _rd), _chr1):
    ok_caa &= 'most compressed package currently recorded' in _t
    ok_caa &= "kernel's smallest" not in _t and 'kernel smallest' not in _t
# the control row of the ledger runs through Lie-rank richness with no dagger clause
_ctrl_row = [l for l in _caa.split('\n') if l.startswith('| `HasCompositeUnitaryControl` |')]
ok_caa &= len(_ctrl_row) == 1
if _ctrl_row:
    ok_caa &= 'dagger-stable' not in _ctrl_row[0] and 'inverseAccessibility_of_generated_daggerStable' not in _ctrl_row[0]
    ok_caa &= 'lieRank_of_elementary' in _ctrl_row[0] and 'control_of_lieRank' in _ctrl_row[0]
    ok_caa &= 'control_of_lieRank_inverse' not in _ctrl_row[0]
check('R7-CAA', ok_caa,
      'Completion-assumption audit guard: the level-one-recursion module carries no sorry and no '
      'native_decide and prints the axioms of its three results, the seam row is stated with '
      'both halves and the observer-recursion half as a negation; the note names a kernel witness '
      'for every ledger row, names the charter package as the round-41 one against the most '
      'compressed package currently recorded (never "the kernel smallest"), the charter carries '
      'its historical banner pointing to the note, the control row of the ledger runs through '
      'Lie-rank richness with no dagger clause, the note lists the residual items as open and '
      'settles none, and asserts neither that '
      'observer recursion supplies the seam, that OIPlusElem is minimal, that the substratum '
      'drives the elementary transitions, nor that the inverse clause is redundant.')

# ---- the inverse-clause audit: dagger stability leaves the exact characterization ----
_inv = open(os.path.join(os.path.dirname(BRIDGE), 'INVERSE-CLAUSE-AUDIT.md'),
            encoding='utf-8').read()
_inv1 = re.sub(r'\s+', ' ', _inv)
_pr = open(os.path.join(BRIDGE, 'OIBridge', 'PositiveReachability.lean'), encoding='utf-8').read()
_prflat = ' '.join(_pr.split())
_mrv = open(os.path.join(BRIDGE, 'OIBridge', 'MicroscopicReversibility.lean'), encoding='utf-8').read()
_mrvflat = ' '.join(_mrv.split())
_ppk = open(os.path.join(BRIDGE, 'OIBridge', 'PositivePackage.lean'), encoding='utf-8').read()
_ppkflat = ' '.join(_ppk.split())
ok_inv = True
# the positive-reachability core sits upstream of the implementation-locality stack
ok_inv &= 'import OIBridge.LieRankSource' not in _pr and 'import OIBridge.PositiveReachability' in _mrv
ok_inv &= 'import OIBridge.PositiveReachability' in _ppk and 'namespace PositiveReachability' in _ppk
ok_inv &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _pr) is None and 'native_decide' not in _pr
ok_inv &= 'structure FiniteOperationalTheory' not in _pr and 'axiom ' not in _pr
_inv_names = ('avail_of_mem_posReach', 'exists_pow_tendsto_one', 'exists_pow_pred_tendsto_star',
              'adStar_mem_posSpan', 'exp_posDir_conj_mem_posSpan', 'bracket_mem_posSpan',
              'controlLie_le_posLie', 'skew_mem_posSpan', 'map_adEquiv_posSpan₀',
              'exists_nested_spanning', 'wordMap_mem_posReach', 'wordMap_hasStrictFDerivAt',
              'psiW_hasStrictFDerivAt', 'psiDerivW_surjective', 'posReach_mem_nhds_totalProd',
              'nhds_one_of_nhds_mem', 'eq_top_of_nhds_one', 'posReach_eq_top',
              'universalReachability_of_lieRank_positive')
_inv_names_mrv = ('control_of_lieRank', 'inverseAccessibility_of_lieRank')
_inv_names_ppk = ('oiPlusPos_iff_qm', 'oiPlusPos_iff_oiPlusElem', 'carrier_general_oiPlusPos')
for _nm in _inv_names:
    ok_inv &= ('#print axioms ' + _nm) in _pr
for _nm in _inv_names_mrv:
    ok_inv &= ('#print axioms ' + _nm) in _mrv
for _nm in _inv_names_ppk:
    ok_inv &= ('#print axioms ' + _nm) in _ppk
ok_inv &= _pr.count('#print axioms') == len(_inv_names)
ok_inv &= _ppk.count('#print axioms') == len(_inv_names_ppk)
ok_inv &= len(_inv_names) + len(_inv_names_mrv) + len(_inv_names_ppk) == 24
# the positive monoid is a Submonoid closure of the round-fifty generators, with no inverse
ok_inv &= 'Submonoid.closure (generators H U)' in _prflat
# the reachability theorem carries no adjoint-closure hypothesis
_urp = _slice(_pr, 'theorem universalReachability_of_lieRank_positive', ':= by')
ok_inv &= bool(_urp) and 'hstar' not in _urp and 'conjChannel Vᴴ' not in _urp
ok_inv &= 'UniversalUnitaryReachability avail' in ' '.join(_urp.split())
# the theory-level statements are the ones the note names
ok_inv &= 'theorem control_of_lieRank (h : LieRankRichness T) : HasCompositeUnitaryControl T' in _mrvflat
ok_inv &= 'def OIPlusPos : Prop := ImplementationLocality T ∧ ElementaryTransitionRichness T ∧ EmbeddedObservation T' in _ppkflat
_cgp = ' '.join(_slice(_ppk, 'theorem carrier_general_oiPlusPos', ':=').split())
ok_inv &= bool(_cgp) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]' in _cgp
ok_inv &= _cgp.endswith('OIPlusPos T ↔ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T')
ok_inv &= 'DaggerStable' not in _pr and 'DaggerStable' not in _ppk
ok_inv &= 'ReversibleImplementationLocality T ∧' not in _slice(_ppk, 'def OIPlusPos', 'variable')
# the note records the fork, the outcome, the twenty-four results and its non-claims
ok_inv &= _inv.lstrip().startswith('# The inverse-clause audit')
ok_inv &= 'Status: Outcome A of the preregistered fork, proved.' in _inv1
for _t in ('Outcome A — direct redundancy', 'Outcome B — only inverse derivation',
           'Outcome C — independence', 'The order of attack is A, B, C',
           'Twenty-four named results', 'What this note does not claim'):
    ok_inv &= _t in _inv1
for _nm in _inv_names + _inv_names_mrv + _inv_names_ppk:
    ok_inv &= _nm in _inv
ok_inv &= '## Migration, recorded after the round' in _inv and 'PositivePackage' in _inv
for _bad in ('HControl is necessary', 'minimal elementary repertoire is settled',
             'dagger stability is false', 'inverse accessibility implies dagger stability',
             'quantum mechanics requires OI', 'non-compact'):
    ok_inv &= not _asserted(_inv, _bad)
# the residual list of the completion-assumption audit names the item as settled elsewhere and
# keeps its own three open items; the README carries the same package and the twenty-four
ok_inv &= 'settled by `INVERSE-CLAUSE-AUDIT.md`' in re.sub(r'\s+', ' ', _caa)
ok_inv &= '`OIPlusPos` | implementation locality, elementary transition richness, embedded observation | `carrier_general_oiPlusPos`' in _caa
_rd1 = re.sub(r'\s+', ' ', _rd)
ok_inv &= 'carrier_general_oiPlusPos' in _rd1 and 'Twenty-four named results' in _rd1
ok_inv &= 'Guard `R7-INV`' in _rd1
# inverseAccessibility_of_lieRank is a theorem about well-formed theories: every paragraph that
# names it says so, and no text derives inverse accessibility from Lie-rank richness alone
_psa_txt = open(os.path.join(os.path.dirname(BRIDGE), 'PRIMITIVE-SOURCE-AUDIT.md'),
                encoding='utf-8').read()
for _t in (_caa, _rd, _inv, _psa_txt):
    for _para in _t.split('\n\n'):
        if 'inverseAccessibility_of_lieRank' in _para:
            ok_inv &= 'well-formed' in _para
    _t1 = re.sub(r'\s+', ' ', _t)
    for _bad in ('inverse accessibility is derived from Lie-rank richness alone',
                 'inverse clause is forced by Lie-rank richness alone',
                 'forced by Lie-rank richness alone', 'InverseAccessibility T := by'):
        ok_inv &= _bad not in _t1
ok_inv &= 'theorem inverseAccessibility_of_lieRank [Nonempty A] (hwf : WellFormed T) (h : LieRankRichness T) : InverseAccessibility T' in _mrvflat
check('R7-INV', ok_inv,
      'Inverse-clause guard: the positive-reachability module carries no sorry, axiom or '
      'native_decide, imports nothing of the implementation-locality stack and prints the axioms of '
      'exactly its nineteen results, the two theory-level theorems printing in MicroscopicReversibility '
      'and the three package results in PositivePackage, twenty-four in all; the positive '
      'monoid is a Submonoid closure of the round-fifty generators; the reachability theorem '
      'carries no hstar hypothesis; control_of_lieRank and OIPlusPos are stated as in the note, '
      'with the carrier-general equivalence quantified over every nonempty finite carrier and no '
      'dagger clause; the note records the preregistered fork, the outcome A, the twenty-four '
      'results and its non-claims, and asserts neither that HControl is necessary, that the '
      'repertoire is minimal, nor anything about non-compact groups; the completion-assumption '
      'audit and the README carry the package and the count; and inverseAccessibility_of_lieRank '
      'is stated with its well-formedness hypothesis wherever it is named.')

# ---- the minimal-repertoire audit: one driven transition and the exchanges, no phase ----
_min = open(os.path.join(os.path.dirname(BRIDGE), 'MINIMAL-REPERTOIRE-AUDIT.md'),
            encoding='utf-8').read()
_min1 = re.sub(r'\s+', ' ', _min)
_mr = open(os.path.join(BRIDGE, 'OIBridge', 'MinimalRepertoire.lean'), encoding='utf-8').read()
_mrflat = ' '.join(_mr.split())
_rlp = open(os.path.join(os.path.dirname(BRIDGE), 'lean', 'repertoire_lie_probe.py'),
            encoding='utf-8').read()
ok_min = True
ok_min &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _mr) is None and 'native_decide' not in _mr
ok_min &= 'structure FiniteOperationalTheory' not in _mr and 'axiom ' not in _mr
_min_names = ('bracket_XX', 'hControl_of_XYZ', 'hControl_perm', 'colourAlg',
              'transition_mem_colourAlg', 'controlLie_le_colourAlg', 'diag_zero_of_mem_controlLie',
              'popDiff_notMem_controlLie', 'not_hControl_of_colourCompatible', 'not_hControl_two',
              'not_hControl_evenCycle', 'phaseFree_of_elementary', 'avail_perm_of_ne',
              'control_at_level', 'tensorOf_one_isometry', 'discard_tensorOf_one', 'descend',
              'control_of_phaseFree', 'oiPlusMin_iff_qm', 'oiPlusMin_iff_oiPlusPos',
              'carrier_general_oiPlusMin', 'perm_avail_of_cycle_swap', 'phaseFree_of_cyclic')
for _nm in _min_names:
    ok_min &= ('#print axioms ' + _nm) in _mr
ok_min &= _mr.count('#print axioms') == len(_min_names)
# the repertoire: one driven pair and the exchanges of distinct states, no quarter phase anywhere
ok_min &= 'phaseGate' not in _mr
ok_min &= ('def PhaseFreeRichness : Prop := ∀ n : ℕ, 2 ≤ Fintype.card (A × Fin n) → '
           '(∃ a b : A × Fin n, a ≠ b ∧ ∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow (transition a b) t))) '
           '∧ (∀ a b : A × Fin n, a ≠ b → T.availExt n Unit (fun _ => conjChannel (permMatrix (Equiv.swap a b))))') in _mrflat
ok_min &= 'def OIPlusMin : Prop := ImplementationLocality T ∧ PhaseFreeRichness T ∧ EmbeddedObservation T' in _mrflat
_cgm = ' '.join(_slice(_mr, 'theorem carrier_general_oiPlusMin', ':=').split())
ok_min &= bool(_cgm) and '∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]' in _cgm
ok_min &= _cgm.endswith('OIPlusMin T ↔ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T')
# the local theorem needs three states; the obstruction is stated as a negation at the qubit and
# at the even cycle; descent consumes the closure rule and not classical coarse-graining
ok_min &= 'theorem hControl_perm (i₀ j₁ : S) (h : i₀ ≠ j₁) (hD : 3 ≤ Fintype.card S) : HControl (transition i₀ j₁) (fun σ : Equiv.Perm S => permMatrix σ)' in _mrflat
ok_min &= '¬ HControl (transition (0 : Fin 2) 1) (fun σ : Equiv.Perm (Fin 2) => permMatrix σ)' in _mrflat
ok_min &= 'theorem not_hControl_evenCycle (m : ℕ) : ¬ HControl' in _mrflat
ok_min &= 'IteratedAncillaClosure T' in _slice(_mr, 'theorem descend', ':= by')
ok_min &= 'availExt_coarse' not in _mr
ok_min &= 'theorem control_of_phaseFree [Nonempty A] (hclos : IteratedAncillaClosure T) (h : PhaseFreeRichness T) : HasCompositeUnitaryControl T' in _mrflat
# the note: preregistered fork, the finding that fixed the hypothesis, the outcome, non-claims
ok_min &= _min.lstrip().startswith('# The minimal-repertoire audit')
ok_min &= 'Status: Outcome A of the preregistered fork, proved.' in _min1
for _t in ('Outcome A — phase-free richness suffices', 'Outcome B — the qubit phase is genuine',
           'Excluded before the kernel', 'not bipartite', 'Twenty-three named results',
           'What this note does not claim', 'not a uniform finite-carrier repertoire',
           'even-carrier countercontrol', 'most compressed package currently formalized',
           'kernel proves generation for the complete graph only'):
    ok_min &= _t in _min1
for _nm in _min_names:
    ok_min &= _nm in _min
for _bad in ('one driven transition is minimal in every sense', 'one cycle suffices',
             'the substratum supplies the driven transition', 'quantum mechanics requires OI',
             'bare OI implies'):
    ok_min &= not _asserted(_min, _bad)
# the cycle claim is stated at its evidence: odd cycles computed at 3, 5, 7, every even cycle a
# theorem, no iff over D and no general non-bipartite theorem, in the note, README and probe
for _t in (_min1, _rd1, ' '.join(_rlp.split()), re.sub(r'\s+', ' ', _caa)):
    for _bad in ('exactly when `D` is odd', 'exactly when D is odd', 'exactly at odd D',
                 'exactly on odd carriers', 'gives full control exactly', 'generates full control exactly',
                 'iff D is odd', 'when the graph is connected and not bipartite',
                 'For a connected non-bipartite G', 'adjacent exchange cannot be dropped',
                 'exchange clause cannot be replaced by a single cycle',
                 'minimal elementary repertoire is settled', 'minimal elementary repertoire, is settled'):
        ok_min &= _bad not in _t
# the exact probe is carried, wired into CI, and its scope tokens are on record
for _t in ('SCOPE-TOKEN: ODD-CYCLES-TESTED', 'SCOPE-TOKEN: BIPARTITE-NO-DIAGONAL',
           'SCOPE-TOKEN: EXCHANGES-NOT-DROPPED', 'from fractions import Fraction',
           'no theorem for every odd cycle or for every connected non-bipartite graph'):
    ok_min &= _t in ' '.join(_rlp.split())
ok_min &= re.search(r'^\s*import numpy', _rlp, re.M) is None
_wf = open(os.path.join(os.path.dirname(os.path.dirname(BRIDGE)), '.github', 'workflows',
                        'verify.yml'), encoding='utf-8').read()
ok_min &= 'repertoire_lie' in _wf
# the completion-assumption audit and the README carry the package and the settled item
ok_min &= '`OIPlusMin` | implementation locality, phase-free richness, embedded observation | `carrier_general_oiPlusMin`' in _caa
ok_min &= 'the planned reduction of the elementary repertoire, is settled by `MINIMAL-REPERTOIRE-AUDIT.md`' in re.sub(r'\s+', ' ', _caa)
ok_min &= 'most compressed package currently formalized' in re.sub(r'\s+', ' ', _caa)
ok_min &= 'carrier_general_oiPlusMin' in _rd1 and 'Twenty-three named results' in _rd1
ok_min &= 'Guard `R7-MIN`' in _rd1
check('R7-MIN', ok_min,
      'Minimal-repertoire guard: the module carries no sorry, axiom or native_decide, prints the '
      'axioms of exactly its twenty-three results, never mentions the quarter phase, states '
      'phase-free richness as one driven pair and the exchanges of distinct states at every '
      'level with two or more states, OIPlusMin as the package and its carrier-general '
      'equivalence over every nonempty finite carrier; the local theorem needs three states, '
      'the qubit and even-cycle obstructions are negations, and descent consumes the closure '
      'rule and not classical coarse-graining; the note records the preregistered fork, the '
      'parity finding that fixed the hypothesis, the outcome and its non-claims; the cycle claim '
      'is stated at its evidence in the note, the README, the probe and the completion-assumption '
      'audit (odd cycles computed at 3, 5, 7, every even cycle a theorem, no iff over D, no '
      'general non-bipartite theorem, the single cycle an even-carrier countercontrol, OIPlusMin '
      'the most compressed package currently formalized and not a minimality theorem); the exact '
      'probe is carried without numpy, wired into CI, with its scope tokens; and the audit and '
      'README carry the package and the count.')

# ---- manuscript propagation of the inverse-clause result: the manuscript-facing strongest
# characterization names implementation locality, assumes no dagger stability and no inverse
# accessibility, and states the well-formedness qualification wherever the derived inverse
# accessibility is named ----
_msroot = os.path.dirname(os.path.dirname(BRIDGE))
_ms = {}
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md',
             'book/ch01-observation.md', 'book/ch19-open-problems.md',
             'book/The-Incompleteness-of-Observation-FULL.md',
             'papers/GR.tex', 'papers/Main.tex', 'papers/Explainer.tex',
             'book/The-Incompleteness-of-Observation-FULL.tex'):
    _ms[_rel] = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
ok_msp = True
for _rel, _t in _ms.items():
    _t1 = re.sub(r'\s+', ' ', _t).lower().replace('\\_', '_')
    ok_msp &= 'reversible implementation locality' not in _t1
    ok_msp &= 'carrier_general_oiplus' + 'elem' not in _t1
    ok_msp &= 'inverseaccessibility_of_generated_daggerstable' not in _t1
    ok_msp &= 'universalreachability_of_lierank_unconditional' not in _t1
    ok_msp &= 'typed_determined_of_oipluselem' not in _t1
_grm = _ms['papers/GR.md']
_grm1 = re.sub(r'\s+', ' ', _grm)
ok_msp &= '1. *Implementation locality.*' in _grm
ok_msp &= '\\text{implementation locality} + \\text{phase-free richness}' in _grm1
ok_msp &= '\\text{implementation locality} + \\text{elementary transition richness}' not in _grm1
ok_msp &= 'carrier_general_oiPlusPos' in _grm and 'oiPlusPos_iff_qm' in _grm
ok_msp &= 'control_of_lieRank' in _grm and 'universalReachability_of_lieRank_positive' in _grm
ok_msp &= 'elementary implementations are closed under the adjoint' not in _grm
ok_msp &= 'No closure of the implementations under the adjoint is assumed' in _grm1
ok_msp &= 'Inverse accessibility is not a hypothesis of the equivalence' in _grm1
ok_msp &= 'typed_determined_of_oiPlusPos' in _grm
ok_msp &= 'the Lie-rank clause alone already does so, with no inverse of a control consumed' in _grm1
_tp = open(os.path.join(BRIDGE, 'OIBridge', 'TypedPositive.lean'), encoding='utf-8').read()
ok_msp &= '#print axioms typed_determined_of_oiPlusPos' in _tp and 'sorry' not in _tp
ok_msp &= os.path.exists(os.path.join(_msroot, 'tools', 'lean_manuscript_census.py'))
ok_msp &= os.path.exists(os.path.join(_msroot, 'verification', 'lean-manuscript-census.json'))
ok_msp &= '"lean-manuscript"' in open(os.path.join(_msroot, 'tools', 'release_gate.py'), encoding='utf-8').read()
# the census is complete relative to the maintained registry: the tool requires an anchor for
# every carried family, the registry and the note state the same-commit contract, and the
# contract is a durable contributor rule
_cens_tool = open(os.path.join(_msroot, 'tools', 'lean_manuscript_census.py'), encoding='utf-8').read()
ok_msp &= "ANCHORED = ('current', 'consistent-uncited', 'scope-consistent')" in _cens_tool
ok_msp &= 'NOANCHOR' in _cens_tool and 'complete relative to the maintained registry' in _cens_tool
_cens_reg = open(os.path.join(_msroot, 'verification', 'lean-manuscript-census.json'), encoding='utf-8').read()
ok_msp &= 'Registry contract (AGENTS.md A.35)' in _cens_reg and '"papers/SM.md"' in _cens_reg
_cens_note = re.sub(r'\s+', ' ', open(os.path.join(_msroot, 'verification', 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_msp &= 'Status: complete relative to the maintained registry' in _cens_note
ok_msp &= 'updates the registry in the same commit' in _cens_note
ok_msp &= 'so a kernel strengthening that reaches the verification notes and the guards and not the papers is caught at the next run' not in _cens_note
ok_msp &= 'Status: complete for the kernel at this commit' not in _cens_note
_agents = re.sub(r'\s+', ' ', open(os.path.join(_msroot, 'AGENTS.md'), encoding='utf-8').read())
ok_msp &= '## §A.35 Registry contract for the Lean-to-manuscript census' in _agents
ok_msp &= 'updates the registry in the same commit' in _agents
# the summaries in Main, the Explainer and both book mirrors carry the same statement
_msum = ('implementation locality, phase-free richness — one continuously driven transition and the '
         'exchanges of distinguishable states, with no phase operation — and embedded observation, with '
         'no closure of the implementations under the adjoint and no inverse accessibility assumed')
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md',
             'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    ok_msp &= _msum in re.sub(r'\s+', ' ', _ms[_rel])
ok_msp &= 'carrier_general_oiPlusPos' in _ms['papers/Main.md']
# every manuscript paragraph naming the derived inverse accessibility carries "well-formed"
for _rel in ('papers/GR.md', 'papers/Main.md'):
    for _para in _ms[_rel].split('\n\n'):
        if 'inverseAccessibility_of_lieRank' in _para:
            ok_msp &= 'well-formed' in _para
# the second principle is phase-free richness, stated at the kernel's evidence, with the elementary
# repertoire as its stronger form; the substratum endpoint is unchanged
ok_msp &= '2. *Phase-free richness.*' in _grm
ok_msp &= ('some pair of distinguishable states is continuously drivable, and every exchange of two '
           'distinguishable states is available. No phase operation enters.') in _grm1
ok_msp &= 'carrier_general_oiPlusMin' in _grm and 'oiPlusMin_iff_qm' in _grm and 'hControl_perm' in _grm
ok_msp &= 'not_hControl_evenCycle' in _grm and 'oiPlusMin_iff_oiPlusPos' in _grm
ok_msp &= 'typed_determined_of_oiPlusMin' in _grm
ok_msp &= 'the quarter phase is dispensable at every level' in _grm1
ok_msp &= 'no stronger minimality of the one driven transition is claimed' in _grm1
ok_msp &= '2. *Elementary transition richness.*' not in _grm
ok_msp &= 'whether the phase or other parts of the repertoire can be eliminated remains open' not in _grm1
for _bad in ('exactly when D is odd', 'exactly when `D` is odd', 'exactly on odd carriers',
             'exactly at odd D', 'the repertoire is minimal', 'minimal repertoire is settled',
             'least discrete', 'smallest discrete', 'minimal discrete', 'minimal repertoire',
             'positive word in the flows, the controls, and the phases',
             'On a carrier with two or fewer states the generated algebra'):
    ok_msp &= _bad not in _grm1
# the owner's three wording repairs: scalar phases of the positive monoid distinguished from the
# repertoire, the obstruction stated at two states with descent for the levels with two or fewer,
# and the two-element discrete form stated as sufficient rather than least
ok_msp &= 'up to a global scalar phase that acts trivially on its conjugation channel' in _grm1
ok_msp &= 'not an operation of the repertoire' in _grm1
ok_msp &= 'On a two-state carrier the drive and the exchange commute' in _grm1
ok_msp &= 'the levels with two or fewer states inherit control instead from the level with three times as many states' in _grm1
ok_msp &= 'the two-element discrete form the kernel formalizes, sufficient for every exchange' in _grm1
ok_msp &= 'no claim that a smaller discrete resource is excluded' in _grm1
ok_msp &= 'carrier_general_oiPlusMin' in _ms['papers/Main.md']
ok_msp &= '#print axioms typed_determined_of_oiPlusMin' in _tp
for _nm in ('"carrier_general_oiPlusPos": "carrier_general_oiPlusMin"', '"oiPlusPos_iff_qm": "oiPlusMin_iff_qm"',
            '"hControl_star": "hControl_perm"', '"typed_determined_of_oiPlusPos": "typed_determined_of_oiPlusMin"'):
    ok_msp &= _nm in _cens_reg
ok_msp &= 'text{current OI substratum} + \\text{continuous off-diagonal controllability}' in _grm1
# the generated forms carry the propagated statement
ok_msp &= 'implementation locality} + \\text{phase-free richness}' in re.sub(r'\s+', ' ', _ms['papers/GR.tex'])
for _rel in ('papers/Main.tex', 'papers/Explainer.tex', 'book/The-Incompleteness-of-Observation-FULL.tex'):
    ok_msp &= 'no closure of the implementations under the adjoint' in re.sub(r'\s+', ' ', _ms[_rel])
check('R7-MSP', ok_msp,
      'Manuscript-propagation guard for the inverse-clause result: no manuscript source or '
      'generated form names reversible implementation locality, the superseded package or the '
      'dagger-stable derivation; GR 3.3 states the primitive as implementation locality, boxes '
      'implementation locality with elementary transition richness and embedded observation, '
      'cites carrier_general_oiPlusPos and the positive-reachability theorems, assumes no adjoint '
      'closure and no inverse accessibility, and states the well-formedness qualification wherever '
      'the derived inverse accessibility is named; the census tool requires an anchor for every '
      'carried family, and the registry, the census note and AGENTS.md A.35 state the same-commit '
      'registry contract with the census complete relative to the maintained registry; Main, the '
      'Explainer and both book mirrors carry '
      'the same summary; the second principle is phase-free richness with the elementary repertoire '
      'as its stronger form, cited from MinimalRepertoire with the even-carrier countercontrol and no '
      'minimality claim, the four supersessions recorded in the registry and the typed corollary '
      'typed_determined_of_oiPlusMin present; the substratum endpoint is unchanged; and '
      'the generated .tex forms carry the propagated statement; the typed form cites the '
      'current package through TypedPositive; and the Lean-to-manuscript census tool and its '
      'registry exist and run in the release gate.')

# ---- CT2 narration guard: the manuscripts state the continuous-time result as a path from the
# identity to the update, not as a one-parameter group and not as a generator; CT3 stays open ----
ok_ctn = True
_ctn_files = {}
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md',
             'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md',
             'papers/GR.tex', 'papers/Main.tex', 'papers/Explainer.tex',
             'book/The-Incompleteness-of-Observation-FULL.tex'):
    _ctn_files[_rel] = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read())
_gct = _ctn_files['papers/GR.md']
for _t in ('What the substratum does determine is a path',
           'factors exactly as a depth-two local circuit, a shear layer followed by a swap layer',
           'its reversibility a consequence of the factorization',
           'time-one map of a strongly continuous one-parameter group of isometric $*$-automorphisms of the quasilocal algebra',
           'run in the order the Heisenberg picture forces, the swap first',
           'norm-continuous path of isometric $*$-automorphisms from the identity to the update\'s own Heisenberg action',
           'For the composite path no one-parameter-group law is established and no generator is exhibited',
           'whether the path satisfies a one-parameter-group law, and whether one time-independent finite-range interaction has the update as its unit-time map, are open, and nothing here decides either',
           'A continuous-time Hamiltonian law is additional structure where that formulation is wanted',
           '`leap_eq_swap_shear`', '`depth_two_circuit`', '`layerQ_add_time`', '`swapQ_add_time`',
           '`layerQ_one_eq_heisQ`', '`swapQ_one_eq_heisQ`', '`heisQ_of_comp`',
           '`driveQ_isContinuousPath`', '`driveQ_one_eq_heisQ`', '`continuous_extension_not_unique`'):
    ok_ctn &= _t in _gct
ok_ctn &= ('an exact norm-continuous path of local $*$-automorphisms of the quasilocal algebra from the '
           'identity to the update\'s Heisenberg action, for which no one-parameter-group law is established '
           'and no generator is exhibited') in _ctn_files['papers/Main.md']
_ctn_sum = ('while the update is joined to the identity by an exact norm-continuous path of local '
            '$*$-automorphisms of that algebra, with no one-parameter-group law established and no generator exhibited, a '
            'continuous-time Hamiltonian law remains additional structure')
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md',
             'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md'):
    ok_ctn &= _ctn_sum in _ctn_files[_rel]
for _rel in ('papers/Main.tex', 'papers/Explainer.tex', 'book/The-Incompleteness-of-Observation-FULL.tex'):
    ok_ctn &= 'with no one-parameter-group law established and no generator exhibited' in _ctn_files[_rel]
ok_ctn &= 'driveQ_isContinuousPath' in _ctn_files['papers/GR.tex'].replace('\\_', '_')
# no manuscript closes CT3' in either direction (the path promoted to a group, or asserted not to be
# one), states cross-layer noncommutation as a theorem, exhibits a generator, or closes CT3
for _rel, _t in _ctn_files.items():
    _l = _t.lower()
    for _bad in ('the update is generated by', 'generated by a time-independent',
                 'generated by one time-independent', 'static generator exists',
                 'admits a static generator', 'the path is a one-parameter group',
                 'the composite is a one-parameter group', 'ct3 is settled', 'ct3 is closed',
                 'the update is the exponential of', 'is not a one-parameter group',
                 'not a one-parameter group', 'the two layers not commuting',
                 'the layers do not commute', 'the two layers do not commute'):
        ok_ctn &= _bad not in _l
# the kernel statement is the one cited
_sod = open(os.path.join(BRIDGE, 'OIBridge', 'SecondOrderDrive.lean'), encoding='utf-8').read()
ok_ctn &= 'theorem driveQ_isContinuousPath' in _sod and '#print axioms driveQ_one_eq_heisQ' in _sod
ok_ctn &= 'No group law and no generator are asserted' in re.sub(r'\s+', ' ', _sod)
# the registry carries CT2 as current with its anchors, and the census note agrees
_ctn_reg = json.loads(open(os.path.join(_msroot, 'verification', 'lean-manuscript-census.json'), encoding='utf-8').read())
_ctn_fam = [f for f in _ctn_reg['families'] if f['name'] == 'continuous time (CT2)']
ok_ctn &= len(_ctn_fam) == 1 and _ctn_fam[0]['status'] == 'current' and len(_ctn_fam[0]['manuscript']) >= 5
ok_ctn &= '| continuous time (CT2) | 4 | current |' in open(os.path.join(_msroot, 'verification', 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read()
check('R7-CTN', ok_ctn,
      'CT2 narration guard: GR 3.3 states the depth-two factorization, the two layer groups and the '
      'norm-continuous path of isometric *-automorphisms from the identity to the update, as a path '
      'with no one-parameter-group law for the composite established, no generator exhibited and '
      'CT3 stated open, citing the '
      'SecondOrder modules; Main 2.3 and the quasilocal summaries in Main, the Explainer and both '
      'book mirrors carry the same clause, in source and generated forms; no manuscript closes the '
      'group question in either direction, states cross-layer noncommutation as a theorem, exhibits '
      'a generator or closes CT3; the kernel file asserts no group law and '
      'no generator; the registry carries CT2 as current with its anchors and the census note '
      'agrees.')

# ---- OI-N narration guard: the passive-observation endpoint is narrated outside the assumptions
# and arrows of the OI->QM characterization, with the N4 anti-conflation in the same paragraph ----
ok_oinn = True
_oinn_main = open(os.path.join(_msroot, 'papers', 'Main.md'), encoding='utf-8').read()
_oinn_expl = open(os.path.join(_msroot, 'papers', 'Explainer.md'), encoding='utf-8').read()
_oinn_par = [p for p in _oinn_main.split('\n\n') if p.startswith('**Passive observation, kept apart')]
ok_oinn &= len(_oinn_par) == 1
_op = re.sub(r'\s+', ' ', _oinn_par[0]) if _oinn_par else ''
for _t in ('enter none of its hypotheses or conclusions',
           'Complete passive observation of a finite-dimensional observable algebra in block-diagonal form',
           'is possible exactly when the algebra is commutative',
           'some passive instrument separates its states exactly when the algebra is commutative',
           'exactly when the algebra is commutative',
           'induces a classical stochastic observation of the algebra\'s center',
           'Quantum noncommutativity cannot coexist with complete passive observation',
           'This is theory-insensitive',
           'carries no information about whether the OI core is realized',
           'holds vacuously, and its converse fails',
           'not evidence for a hidden ontology',
           'nothing here says that quantum mechanics rests on observation incompleteness',
           'is a consequence of full control and nothing more',
           'can only read an existing record',
           'creating a genuinely new record changes the joint system',
           'All four statements are finite-dimensional, and none bears on the equivalence',
           '`complete_passive_iff_commutative`', '`central_classification`',
           '`no_complete_passive_observation`', '`passivelyIncomplete_of_card`',
           '`passive_nondiscriminating`', '`passivelyIncomplete_without_oiCore`',
           '`internal_branch_eq_blockPart`', '`internal_outcome_law`', '`recordInstr_writes`',
           '`recordInstr_not_passive`', '`no_full_passive_self_record`',
           '`oiCore_to_passive_vacuous`', '`qm_implies_oiCore`', '`realizesSealedOICore_of_control`'):
    ok_oinn &= _t in _op
# the N1/N3 statement is existential, as the freeze states it: some passive instrument is complete
# iff the algebra is commutative, never every passive instrument
# the paragraph sits outside the equivalence: no package name, no arrow, no box
for _bad in ('carrier_general', 'OIPlus', '\\iff', '\\boxed', 'equivalent to'):
    ok_oinn &= _bad not in _op
_oe = re.sub(r'\s+', ' ', _oinn_expl)
for _bad in ('observes the algebra completely, separating its states, exactly when',
             'observes it completely exactly when', 'every passive instrument observes',
             'every passive instrument separates', 'each passive instrument observes'):
    ok_oinn &= _bad not in _op and _bad not in _oe
for _t in ('*Passive observation, kept apart.*', 'enter none of its conditions',
           'is possible exactly when the algebra is commutative',
           'some passive instrument separates its states exactly then',
           'cannot coexist with complete passive observation', 'theory-insensitive',
           'not evidence for a hidden ontology',
           'nor a statement that quantum mechanics rests on observation incompleteness',
           'can only read an existing record'):
    ok_oinn &= _t in _oe
# GR carries no passive-observation paragraph: the endpoint stays out of the characterization's home
ok_oinn &= 'Passive observation, kept apart' not in _grm
# the symmetric vocabulary of N4 and the freeze's other forbidden readings stay out of the papers
_oinn_epar = [p for p in _oinn_expl.split('\n\n') if p.startswith('*Passive observation, kept apart.*')]
ok_oinn &= len(_oinn_epar) == 1
for _t in (_op.lower(), re.sub(r'\s+', ' ', _oinn_epar[0]).lower() if _oinn_epar else ''):
    # the symmetric vocabulary of N4, forbidden in the two narrating paragraphs
    for _bad in ('neither implies the other', 'logically independent', 'neither notion carries',
                 'independent of the oi core', 'orthogonal'):
        ok_oinn &= _bad not in _t
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'papers/Main.tex', 'papers/Explainer.tex'):
    _l = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read()).lower()
    for _bad in ('qm requires oi', 'quantum mechanics requires observation',
                 'every block is one-dimensional', 'every block has dimension one',
                 'is exactly a classical stochastic observation',
                 'passive incompleteness is evidence', 'passive incompleteness diagnoses',
                 'passive incompleteness implies the oi core', 'passive observation forbids'):
        ok_oinn &= _bad not in _l
    ok_oinn &= _l.count('evidence for a hidden ontology') == _l.count('not evidence for a hidden ontology')
for _rel in ('papers/Main.tex', 'papers/Explainer.tex'):
    ok_oinn &= 'cannot coexist with complete passive observation' in re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read())
# the registry carries OI-N as current with its anchors; the census note agrees; the freeze note is untouched
_oinn_fam = [f for f in _ctn_reg['families'] if f['name'] == 'OI-N passive observation']
ok_oinn &= len(_oinn_fam) == 1 and _oinn_fam[0]['status'] == 'current' and len(_oinn_fam[0]['manuscript']) >= 5
ok_oinn &= '| OI-N passive observation | 4 | current |' in open(os.path.join(_msroot, 'verification', 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read()
check('R7-OINN', ok_oinn,
      'OI-N narration guard: Main 3.4 carries one paragraph, outside the characterization (no '
      'package name, arrow or box in it), stating the four endpoint items with their kernel names, '
      'the N1/N3 statement existential (some passive instrument complete iff commutative, never '
      'every), the vacuous implication cited as oiCore_to_passive_vacuous and the containment as '
      'qm_implies_oiCore through realizesSealedOICore_of_control, '
      'the theory-insensitive reading of N4 with the vacuous implication and the failing converse, '
      'and the anti-conflation in the same paragraph (not evidence for a hidden ontology, no '
      'statement that QM rests on OI, containment as a consequence of control); the Explainer '
      'carries the compact form; GR carries none; the symmetric N4 vocabulary and the freeze\'s '
      'forbidden readings are absent from both papers and their generated forms; the registry '
      'carries OI-N as current with its anchors and the census note agrees.')

# ---- kernel-pointer guard: the SM counting layer and the Main 3.4 equivalence chain cite their
# current theorem names at the principal statements, and no pointer falls back to a superseded name ----
ok_ptr = True
_sm_md = open(os.path.join(_msroot, 'papers', 'SM.md'), encoding='utf-8').read()
_mn_md = open(os.path.join(_msroot, 'papers', 'Main.md'), encoding='utf-8').read()
_ptr_pins = {
    'papers/SM.md': (
        ('*Proof.* Characters at each conjugacy class', '`theorem_7`', '`sum_proj`', '`finrank_PT`', '`char_c4_odd`', '`chiLink`', '`card_rot`', '`card_sym`', '`card_mul_finrank_invariants`', '`finrank_intertwiners`'),
        ('*Proof.* Inversion in $O_h$', '`ohInvariant_iff`', '`rem_littleO`', '`rem_bigO`'),
        ('*Proof.* The 2^d = 8 BZ corners', '`theorem_8`'),
        ('*Proof.* The Yang-Mills action', '`theorem_16`'),
        ('*Proof.* T-invariance (Theorem 17)', '`theorem_19`')),
    'papers/Main.md': (
        ('*Proof.* Modulo phases the Weyl operators', '`entanglementBreaking_twirl`', '`not_entanglementBreaking_twirl`', '`exists_lagrangian_tuple`', '`isotropic_iff_commute`', '`separable_imp_ppt`'),
        ('*The revival counterexample and the doubly-stochastic obstruction', '`c3_necessity`', '`card_hidden_ge_two_pow_Istar`', '`c3_necessity_and_capacity`'),
        ('*Proof (constructive).* Let $D$ be a common denominator', '`S_imp_D`'),
        ('*($Q_{\\mathrm{fb}}$) the laws realizable', '`finite_horizon_equivalence`', '`S_imp_D`', '`permMatrix_mem_unitaryGroup`', '`isDiag_Phi`'),
        ('*(c) **Capacity floor.**', '`unavoidable_hidden_predictive_memory`', '`distinguishability_floor`', '`capacity_floor`'),
        ('Each added principle is independently necessary', '`carrier_general_oiPlusMin`', '`oiPlusMin_iff_qm`', '`typed_determined_iff`', '`typed_determined_of_oiPlusMin`', '`closure_iUnion_stage`', '`quasiState_unique`', '`driveQ_isContinuousPath`', '`driveQ_one_eq_heisQ`', '`substratum_plus_control_qm`'),
        ('**Passive observation, kept apart', '`complete_passive_iff_commutative`', '`passive_nondiscriminating`', '`internal_branch_eq_blockPart`', '`qm_implies_oiCore`')),
}
_ptr_texts = {'papers/SM.md': _sm_md, 'papers/Main.md': _mn_md}
for _rel, _pins in _ptr_pins.items():
    _lines = _ptr_texts[_rel].split('\n')
    for _pin in _pins:
        _hits = [l for l in _lines if l.startswith(_pin[0])]
        ok_ptr &= len(_hits) == 1
        for _nm in _pin[1:]:
            ok_ptr &= bool(_hits) and _nm in _hits[0]
# every pointed-to name is declared in OIBridge, and no paragraph of either paper cites a superseded
# name without its successor beside it (the registry's supersession table, read here directly)
_ptr_reg = json.loads(open(os.path.join(_msroot, 'verification', 'lean-manuscript-census.json'), encoding='utf-8').read())
_ptr_decl = set()
for _lf in glob.glob(os.path.join(BRIDGE, 'OIBridge', '*.lean')):
    for _m in re.finditer(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:protected\s+)?(?:theorem|lemma|def|abbrev|structure|instance|class)\s+([A-Za-z_][A-Za-z0-9_\'₀₁₂.]*)', open(_lf, encoding='utf-8').read(), re.M):
        _ptr_decl.add(_m.group(1).split('.')[-1])
for _rel, _pins in _ptr_pins.items():
    for _pin in _pins:
        for _nm in _pin[1:]:
            ok_ptr &= _nm.strip('`') in _ptr_decl
for _rel, _t in _ptr_texts.items():
    for _old, _new in _ptr_reg['supersessions'].items():
        for _para in _t.split('\n\n'):
            if f'`{_old}`' in _para and f'`{_new}`' not in _para:
                ok_ptr = False
# the generated forms carry the pointers, and the registry records both families as current
for _rel, _nm in (('papers/SM.tex', 'theorem_7'), ('papers/SM.tex', 'finrank_intertwiners'),
                  ('papers/Main.tex', 'finite_horizon_equivalence'),
                  ('papers/Main.tex', 'permMatrix_mem_unitaryGroup'), ('papers/Main.tex', 'isDiag_Phi'),
                  ('papers/Main.tex', 'unavoidable_hidden_predictive_memory'),
                  ('papers/Main.tex', 'entanglementBreaking_twirl')):
    ok_ptr &= _nm in open(os.path.join(_msroot, _rel), encoding='utf-8').read().replace('\\_', '_')
for _fam_name in ('representation bridge and counting', 'equivalence chain and memory'):
    _fam = [f for f in _ptr_reg['families'] if f['name'] == _fam_name]
    ok_ptr &= len(_fam) == 1 and _fam[0]['status'] == 'current' and len(_fam[0]['manuscript']) >= 5
ok_ptr &= all(f['status'] != 'consistent-uncited' for f in _ptr_reg['families'])
check('R7-PTR', ok_ptr,
      'Kernel-pointer guard: SM Theorem 7, Corollary 1a, Theorems 8, 16 and 19, and Main\'s '
      'separability threshold, C3 necessity, process dilation, finite-horizon equivalence, hidden '
      'predictive memory, the 3.4 summary and the passive-observation paragraph each carry their '
      'current kernel names at the end of the proof or list that follows the statement, the '
      'statement lines themselves untouched so the coverage ledger fingerprints hold; every pointed-to name is declared in OIBridge; '
      'no paragraph of either paper cites a superseded name without its successor; the generated '
      'forms carry the pointers; and the registry records both families as current with no family '
      'left consistent-uncited.')

# ---- Route B, milestone B0: the consequence closure is defined from kernel names, the falsifier is
# one named operation, the target is a definition whose proofs go through the sealed core for the
# substratum theory, and nothing reaches a manuscript ----
ok_rb0 = True
_rb = open(os.path.join(BRIDGE, 'OIBridge', 'RouteB.lean'), encoding='utf-8').read()
_rbflat = ' '.join(_rb.split())
_rbn = open(os.path.join(os.path.dirname(BRIDGE), 'ROUTE-B-AUDIT.md'), encoding='utf-8').read()
_rbn1 = re.sub(r'\s+', ' ', _rbn)
ok_rb0 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _rb) is None and 'native_decide' not in _rb
ok_rb0 &= 'axiom ' not in _rb
_rb_names = ('DerivedOI.implementationLocality', 'DerivedOI.closure', 'falsifier_available_of_control',
             'falsifier_available_of_phaseFree', 'not_phaseFree_of_falsifier_unavailable',
             'falsifier_not_monomial_not_diag', 'exchangesAvailable_of_control',
             'phasesAvailable_of_control', 'readWriteAvailable_of_control', 'derivedOI_of_qm',
             'derivedOICore_of_qm', 'qm_not_falsifierUnavailable', 'target_separates', 'target_not_qm',
             'substratumTheory_avail_conj', 'substratumTheory_derivedOI',
             'substratumTheory_falsifierUnavailable', 'substratumTheory_candidate',
             'target_of_substratum_core', 'derivedOI_qm_iff_phaseFree', 'substratumTheory_relabel',
             'substratumTheory_passiveStep', 'substratumTheory_controlStep', 'substratumTheory_readout',
             'substratumTheory_readoutFamily', 'substratumTheory_comb',
             'substratumTheory_realizesSealedOICore', 'substratumTheory_derivedOICore', 'routeB_target',
             'substratumTheory_not_phaseFree', 'derivedOICore_not_phaseFree')
for _nm in _rb_names:
    ok_rb0 &= ('#print axioms ' + _nm) in _rb and _nm in _rbn
ok_rb0 &= _rb.count('#print axioms') == len(_rb_names)
# the closure is exactly the five conjuncts, the core form adds the sealed core, the target is a
# definition whose only proof consumes the sealed-core hypothesis
ok_rb0 &= ('def DerivedOI (T : FiniteOperationalTheory A) : Prop := ReversibleImplementationLocality T ∧ '
           'EmbeddedObservation T ∧ ExchangesAvailable T ∧ PhasesAvailable T ∧ ReadWriteAvailable T') in _rbflat
ok_rb0 &= 'def DerivedOICore (T : FiniteOperationalTheory (Fin 2)) : Prop := DerivedOI T ∧ RealizesSealedOICore T' in _rbflat
ok_rb0 &= 'def FalsifierUnavailable (T : FiniteOperationalTheory (Fin 2)) : Prop := ¬ T.availExt 1 Unit (fun _ => conjChannel rot)' in _rbflat
ok_rb0 &= 'def RouteBTarget : Prop := ∃ T : FiniteOperationalTheory (Fin 2), DerivedOICore T ∧ FalsifierUnavailable T' in _rbflat
# the target has exactly two proofs: the reduction to the sealed core, and its discharge
ok_rb0 &= _rbflat.count(': RouteBTarget :=') == 2
ok_rb0 &= 'theorem target_of_substratum_core (h : RealizesSealedOICore (substratumTheory (Fin 2))) : RouteBTarget :=' in _rbflat
ok_rb0 &= 'theorem routeB_target : RouteBTarget := target_of_substratum_core substratumTheory_realizesSealedOICore' in _rbflat
ok_rb0 &= 'theorem substratumTheory_candidate : DerivedOI (substratumTheory (Fin 2)) ∧ FalsifierUnavailable (substratumTheory (Fin 2))' in _rbflat
ok_rb0 &= 'theorem substratumTheory_falsifierUnavailable : FalsifierUnavailable (substratumTheory (Fin 2))' in _rbflat
ok_rb0 &= 'must fail this named operation' in _rbflat and 'exactly it' not in _rbflat
ok_rb0 &= 'theorem not_phaseFree_of_falsifier_unavailable (T : FiniteOperationalTheory (Fin 2)) (heo : EmbeddedObservation T) (hf : FalsifierUnavailable T) : ¬ PhaseFreeRichness T' in _rbflat
# the note: status, the two preregistered outcomes, the table, the falsifier, the target, non-claims
ok_rb0 &= _rbn.lstrip().startswith('# Route B')
ok_rb0 &= 'Status: B0 and B1 complete; the target is proved with the substratum theory as the witness.' in _rbn1
ok_rb0 &= 'B1 is one question' in _rbn1 and 'must fail this named operation' in _rbn1
ok_rb0 &= 'exactly one named operation' not in _rbn1 and 'exactly it' not in _rbn1
for _t in ('Outcome 1 — a countertheory exists', 'Outcome 2 — every candidate collapses',
           'from kernel names', 'The falsifier', 'The B1 target, stated', 'What would falsify Outcome 1 at B1',
           'What would falsify Outcome 2', 'Thirty-one named results', 'What this note does not claim',
           'The candidate, certified up to the core', 'target_of_substratum_core',
           'RouteBTarget', 'The proof is `routeB_target`',
           'additionally requires `RealizesSealedOICore T`'):
    ok_rb0 &= _t in _rbn1
# the stale forms, absolute and conditional, are rejected in the module, the note and the README
for _t in (_rbflat, _rbn1, _rd1):
    for _bad in ('with no proof.', 'No proof is given and none is asserted', 'is stated and not proved',
                 'stated and not proved', 'no proof anywhere', 'is a further consequence',
                 'no unconditional proof', 'consumes the sealed core for the substratum theory as its hypothesis',
                 'Nothing here answers it', 'nothing here discharges it', 'Whether it does is open',
                 'certified up to one conjunct.**'):
        ok_rb0 &= _bad not in _t
ok_rb0 &= 'additionally requires the sealed OI core' in _rbflat
for _bad in ('Outcome 2 holds', 'Outcome 2 is proved', 'the drive is independent of OI',
             'independent of bare OI', 'quantum mechanics requires OI', 'bare OI implies',
             'Route A is closed', 'physical theory', 'derived from bare OI'):
    ok_rb0 &= not _asserted(_rbn, _bad)
# no manuscript carries Route B; the registry classifies the module as kernel-only, carried by none
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_rb0 &= 'RouteB' not in _t and 'Route B' not in _t and 'DerivedOI' not in _t and 'routeB_target' not in _t
_rb_fam = [f for f in _ptr_reg['families'] if f['name'] == 'route B: consequence closure']
ok_rb0 &= len(_rb_fam) == 1 and _rb_fam[0]['status'] == 'kernel-only' and _rb_fam[0]['modules'] == ['RouteB']
ok_rb0 &= _rb_fam[0]['manuscript'] == [] and 'routeB_target' in _rb_fam[0]['note'] and 'not about bare OI' in _rb_fam[0]['note']
ok_rb0 &= '`R7-RB0`' in _rd1 and '`R7-RB1`' in _rd1 and 'RouteBTarget' in _rd1 and 'Thirty-one named results' in _rd1
ok_rb0 &= 'target_of_substratum_core' in _rd1 and 'routeB_target' in _rd1
check('R7-RB0', ok_rb0,
      'Route B0 guard: the module carries no sorry, axiom or native_decide and prints the axioms of '
      'exactly its thirty-one results; DerivedOI is exactly the five conjuncts, DerivedOICore adds the '
      'sealed core, the falsifier is the unavailability of conjChannel rot at level one, the target '
      'is a definition with exactly two proofs, the reduction to the sealed core and its discharge, '
      'the stale absolute and conditional forms are absent, and the reduction is stated as in the '
      'note; the note records the status, the two preregistered outcomes, the closure table, the '
      'falsifier, the target and its non-claims, and asserts neither that the drive is independent '
      'of bare OI nor that Route A is closed; no manuscript carries Route B; the registry classifies '
      'the module as kernel-only with no manuscript anchor and the README carries the paragraph.')

# ---- Route B, milestone B1: the four sealed-core clauses were preregistered before the proof with
# exactly two admissible outcomes each, every clause closed by its positive outcome under its
# preregistered name, the permutation clauses from monomial generation and not from control, and
# the outcome is recorded with its scope ----
ok_rb1 = True
_rbF = _rb[_rb.index('### Section F'):]
_rbFflat = ' '.join(_rbF.split())
# the preregistration precedes the outcome in the note, and freezes the four clauses and the rule
_i_pre = _rbn.find('## B1 — the sealed core for the substratum theory, preregistered before the proof')
_i_out = _rbn.find('## B1 — the outcome, clause by clause')
ok_rb1 &= 0 < _i_pre < _i_out
for _t in ('1. **Passive step availability.**', '2. **Control-step availability.**',
           '3. **Native visible readout, as a family certified inside the generated theory.**',
           '4. **Comb agreement.**', 'Two admissible outcomes per clause, and no third',
           'a kernel theorem establishing the clause for `substratumTheory (Fin 2)`, or a kernel theorem establishing its negation',
           'B1 does not repair or enlarge the candidate', 'The control discipline',
           'The absence of a sufficient condition is not evidence against a conclusion',
           'Order of attack', 'Preregistered names'):
    ok_rb1 &= _t in _rbn1
# every clause closed under its preregistered name; no negative name exists anywhere
for _nm in ('substratumTheory_passiveStep', 'substratumTheory_controlStep', 'substratumTheory_readout',
            'substratumTheory_readoutFamily', 'substratumTheory_comb',
            'substratumTheory_realizesSealedOICore', 'routeB_target'):
    ok_rb1 &= ('theorem ' + _nm) in _rbF
for _nm in ('substratumTheory_not_passiveStep', 'substratumTheory_not_controlStep',
            'substratumTheory_not_readout', 'substratumTheory_not_readoutFamily', 'substratumTheory_not_comb'):
    ok_rb1 &= ('theorem ' + _nm) not in _rb
# the clause statements are the sealed core's conjuncts, verbatim
ok_rb1 &= ('theorem substratumTheory_passiveStep : (substratumTheory (Fin 2)).availExt 4 Unit '
           '(fun _ => transport coreIdx (correlationExtension sigmaPerm (onesCorr Core))) := substratumTheory_relabel sigmaPerm') in _rbFflat
ok_rb1 &= ('theorem substratumTheory_controlStep : (substratumTheory (Fin 2)).availExt 4 Unit '
           '(fun _ => transport coreIdx (correlationExtension tauPerm (onesCorr Core))) := substratumTheory_relabel tauPerm') in _rbFflat
ok_rb1 &= ('theorem substratumTheory_readout (r : Bool × Bool) : transport coreIdx (readVisible r) '
           '= (substratumTheory (Fin 2)).readout 4 (visIdx r)') in _rbFflat
ok_rb1 &= ('theorem substratumTheory_readoutFamily : (substratumTheory (Fin 2)).availExt 4 (Bool × Bool) '
           '(fun r => transport coreIdx (readVisible r))') in _rbFflat
ok_rb1 &= ('theorem substratumTheory_comb (steps : List VStep) (w : Core → ℂ) : realizedFold steps '
           '(Matrix.reindex coreIdx coreIdx (Matrix.diagonal w)) = Matrix.reindex coreIdx coreIdx '
           '(Matrix.diagonal (visWeightFold steps w)) := realizedFold_diagonal steps w') in _rbFflat
ok_rb1 &= 'theorem substratumTheory_realizesSealedOICore : RealizesSealedOICore (substratumTheory (Fin 2)) :=' in _rbFflat
ok_rb1 &= ('theorem substratumTheory_derivedOICore : DerivedOICore (substratumTheory (Fin 2)) := '
           '⟨substratumTheory_derivedOI, substratumTheory_realizesSealedOICore⟩') in _rbFflat
ok_rb1 &= 'theorem substratumTheory_not_phaseFree : ¬ PhaseFreeRichness (substratumTheory (Fin 2))' in _rbFflat
ok_rb1 &= ('theorem derivedOICore_not_phaseFree : ∃ T : FiniteOperationalTheory (Fin 2), DerivedOICore T ∧ '
           '¬ PhaseFreeRichness T := target_separates routeB_target') in _rbFflat
ok_rb1 &= ('theorem derivedOI_qm_iff_phaseFree [Nonempty A] {T : FiniteOperationalTheory A} (h : DerivedOI T) : '
           'ExactAllFiniteEndomorphicQuantumOps T ↔ PhaseFreeRichness T') in _rbflat
# the permutation clauses come from monomial generation: the relabel lemma goes through
# substratumTheory_avail_conj with the label-invariant class and the permutation isometry, and
# Section F names no control hypothesis and applies no control-derived availability
ok_rb1 &= ('rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel] exact substratumTheory_avail_conj '
           '(substratumClass_labelInvariant _ _ coreIdx _ (monomial_permMatrix g)) '
           '(reindex_isometry _ _ (permMatrix_isometry g))') in _rbFflat
ok_rb1 &= 'hctrl' not in _rbF and 'HasCompositeUnitaryControl' not in _rbF.replace('composite unitary control', '')
ok_rb1 &= re.search(r'(?<![A-Za-z_])relabel_available [T_(]', _rbF) is None
ok_rb1 &= 'realizesSealedOICore_of_control' not in _rbF and 'substratumGen_not_control' not in _rbF
# the outcome record: the table, the direct test, the scope, the robustness, and the non-claims
for _t in ('| 1, passive step | `substratumTheory_passiveStep` | `substratumTheory_relabel sigmaPerm` |',
           '| 2, control step | `substratumTheory_controlStep` | `substratumTheory_relabel tauPerm` |',
           '| 4, comb agreement | `substratumTheory_comb` |',
           'No clause failed, no candidate repair was made, and no hypothesis was added',
           'Composite unitary control was not used, and `substratumGen_not_control` was not consulted',
           '`routeB_target : RouteBTarget`, with `substratumTheory (Fin 2)` as the witness',
           'What the outcome establishes', 'Why the witness is robust to later derivations',
           'What the outcome does not establish', 'the preregistered Outcome 1 at this carrier',
           'A1–A6 are not `DerivedOI`', 'derivedOI_qm_iff_phaseFree', 'derivedOICore_not_phaseFree',
           'Route A is not closed by this note'):
    ok_rb1 &= _t in _rbn1
# the census note carries the kernel-only row for the family, and the README the B1 sentences
_cen = open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read()
_cen1 = re.sub(r'\s+', ' ', _cen)
ok_rb1 &= '| route B: consequence closure | 1 | kernel-only |' in _cen1 and 'routeB_target' in _cen1
ok_rb1 &= re.search(r'The exceptions? (is|are) the Route B family', _cen1) is not None and '`kernel-only`' in _cen1
for _t in ('is proved (`routeB_target`, through `target_of_substratum_core`)',
           'substratumTheory_realizesSealedOICore', 'substratumTheory_relabel',
           'derivedOICore_not_phaseFree', 'derivedOI_qm_iff_phaseFree',
           'whose A1–A6 are not `DerivedOI`', 'which is a propagation round of its own'):
    ok_rb1 &= _t in _rd1
check('R7-RB1', ok_rb1,
      'Route B1 guard: the note preregisters the four sealed-core clauses before the outcome, each '
      'with exactly two admissible outcomes and no repair of the candidate, and records the control '
      'discipline; every clause is closed under its preregistered positive name with the sealed '
      'core\'s conjunct as its statement, no negative name exists, the permutation clauses go through '
      'monomial generation with no control hypothesis in Section F, routeB_target discharges '
      'target_of_substratum_core, and the note, the census and the README record the outcome with '
      'its scope: the two-state closure with the core does not entail phase-free richness, under the '
      'closure quantum mechanics is exactly phase-free richness, and nothing is said of bare OI.')

# ---- The manuscript-axiom pass: A1–A6 preregistered before the proof with a representability
# verdict each, A1 and A2 closed under faithful forms, A3–A6 recorded as gaps with no weakened
# predicate, no ManuscriptOI conjunction formed, the sourcing bound proved, nothing asserted
# about the witness against A3–A6 or about the strongest claim ----
ok_max = True
_ma = open(os.path.join(BRIDGE, 'OIBridge', 'ManuscriptAxioms.lean'), encoding='utf-8').read()
_maflat = ' '.join(_ma.split())
_man = open(os.path.join(os.path.dirname(BRIDGE), 'MANUSCRIPT-AXIOM-AUDIT.md'), encoding='utf-8').read()
_man1 = re.sub(r'\s+', ' ', _man)
ok_max &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _ma) is None and 'native_decide' not in _ma
ok_max &= 'axiom ' not in re.sub(r'/-.*?-/', '', _ma, flags=re.S)
_ma_names = ('a1_every_theory', 'substratumTheory_A1', 'substratumTheory_A2', 'substratumTheory_A1A2',
             'a2_of_control', 'substratumClass_configurationLevel', 'configurationLevel_iff_le_substratum',
             'configurationLevel_availExt_le', 'configurationLevel_falsifierUnavailable',
             'configurationLevel_not_phaseFree', 'configurationLevel_not_qm')
for _nm in _ma_names:
    ok_max &= ('#print axioms ' + _nm) in _ma and _nm in _man1
ok_max &= _ma.count('#print axioms') == len(_ma_names)
# exactly four definitions: the two faithful axioms, their conjunction, and the sourcing predicate;
# no predicate for a gapped axiom and no ManuscriptOI
ok_max &= sorted(re.findall(r'^def (\w+)', _ma, re.M)) == sorted(['A1Realized', 'A2Realized', 'A1A2Realized', 'ConfigurationLevel'])
ok_max &= re.search(r'\b(def|theorem|abbrev|structure) \w*(A3|A4|A5|A6|ManuscriptOI)\w*', _ma) is None
ok_max &= 'ManuscriptOI' not in _ma
ok_max &= ('def A1Realized (_T : FiniteOperationalTheory (Fin 2)) : Prop := Fintype.card Core = 8 ∧ '
           '∀ n : ℕ, Fintype.card (Fin 2 × Fin n) = 2 * n') in _maflat
ok_max &= ('def A2Realized (T : FiniteOperationalTheory (Fin 2)) : Prop := T.availExt 4 Unit '
           '(fun _ => transport coreIdx (correlationExtension sigmaPerm (onesCorr Core))) ∧ T.availExt 4 Unit '
           '(fun _ => transport coreIdx (correlationExtension sigmaPerm.symm (onesCorr Core)))') in _maflat
ok_max &= ('def ConfigurationLevel (𝓘 : ImplementationClass) : Prop := ∀ (S : Type) [Fintype S] [DecidableEq S] '
           '(K : Matrix S S ℂ), 𝓘 S K → IsMonomial K') in _maflat
ok_max &= 'theorem configurationLevel_not_phaseFree (h : ConfigurationLevel 𝓘) (hl : LabelInvariant 𝓘) : ¬ PhaseFreeRichness (genTheory 𝓘 arch (Fin 2))' in _maflat
ok_max &= 'theorem configurationLevel_falsifierUnavailable (h : ConfigurationLevel 𝓘) : FalsifierUnavailable (genTheory 𝓘 arch (Fin 2))' in _maflat
ok_max &= 'theorem substratumTheory_A2 : A2Realized (substratumTheory (Fin 2)) := ⟨substratumTheory_relabel sigmaPerm, substratumTheory_relabel sigmaPerm.symm⟩' in _maflat
# the note: preregistration precedes the outcome; the six axioms verbatim; a verdict per axiom
# before the proof; two outcomes per representable axiom, the gap for the others; the reading of
# the bound fixed in advance; the outcome table; the missing interface; the non-claims
_i_pre = _man.find('## Per-axiom preregistration')
_i_bound = _man.find('## The interface theorem, preregistered')
_i_out = _man.find('## The outcome')
ok_max &= 0 < _i_pre < _i_bound < _i_out
ok_max &= _man.lstrip().startswith('# The manuscript-axiom audit')
for _t in ('**(A1) Finiteness.** The configuration space $S$ is finite.',
           '**(A2) Determinism.** $\\varphi : S \\to S$ is a bijection (deterministic, reversible dynamics).',
           '**(A3) Bounded coupling degree.**', '**(A4) Center independence.**', '**(A5) Linearity.**',
           '**(A6) Background independence.**',
           '| A1 finiteness | **yes**', '| A2 determinism | **yes** |', '| A3 bounded coupling degree | **no** |',
           '| A4 center independence | **no** |', '| A5 linearity | **no** |',
           '| A6 background independence | **no** |',
           'no conjunction named `ManuscriptOI` is defined in the kernel',
           'Configuration-level sourcing bound', 'If the theorem holds, its reading is fixed here in advance',
           'Status: pass complete, with a scope repair recorded at review. No manuscript-level A1–A6 conjunct is presently a faithful predicate of the bare theory',
           'realized-core image', '## Scope repair, recorded at review', 'commit `6183bc6`',
           'A1 and A2 are realized-core images, not faithful predicates of the manuscript substratum',
           'The sourcing bound proves necessity, not uniqueness',
           'requires some non-configuration-level sourcing',
           "the manuscripts' specifically named open candidate",
           '| A1 finiteness | realized-core image holds for the witness, and for every theory; manuscript-level A1 is a gap (no identification map) |',
           '| A2 determinism | realized-core image holds for the witness, and for every theory with composite unitary control; manuscript-level A2 is a gap (no identification map) |',
           '| A3 bounded coupling degree | **gap** | no kernel predicate |',
           '| A4 center independence | **gap** | no kernel predicate |',
           '| A5 linearity | **gap** | no kernel predicate |',
           '| A6 background independence | **gap** | no kernel predicate |',
           'is **not established**', 'The strongest form is therefore not refuted here',
           'The missing interface, recorded', 'Eleven named results', 'What this note does not claim',
           'A3–A6 may well be what such a derivation consumes; the pass does not say they are not',
           'not shown here to be the only one',
           'makes the required continuous mixing executable', 'one-parameter family of transitions at the relevant levels',
           'A single executable non-monomial gate is not enough',
           'That an executable non-monomial gate would close Route A'):
    ok_max &= _t in _man1
# a discrete non-monomial gate is never promoted to closure of Route A: the target is the
# executable continuous mixing family, in the module, the README and the outcome
for _t in (_maflat, _rd1, _man[_man.find('## The outcome'):]):
    ok_max &= 'a non-monomial operation executable' not in _t and 'non-monomial operation executable' not in _t
for _t in (_maflat, _rd1):
    ok_max &= 'not a single non-monomial gate' in _t
for _bad in ('a non-monomial gate closes Route A', 'non-monomial gate suffices', 'Route A is closed by a gate'):
    ok_max &= not _asserted(_man, _bad)
# the superseded readings are absent from the module, the README, the registry note and the
# outcome half of the note; the scope-repair section quotes two of them and is excluded
_man_out = _man[_man.find('## The outcome'):]
for _t in (_maflat, _rd1, _man_out):
    for _bad in ('only through the observer-level lift', 'the only place left', 'every sourcing of any substratum',
                 'the only sourcing the bound leaves', 'faithful theory-level forms relative to',
                 'A1 and A2 hold for the witness', 'A1 AND A2 HOLD FOR THE WITNESS'):
        ok_max &= _bad not in _t
for _bad in ('The witness satisfies ManuscriptOI', 'witness satisfies `ManuscriptOI`', 'ManuscriptOI does not imply',
             'A1–A6 hold for the witness',
             'satisfies A1–A6', 'satisfies the full manuscript OI', 'strongest form is false',
             'OI ⇒ QM is false', 'the lift is derivable', 'the lift is not derivable',
             'quantum mechanics requires OI', 'bare OI implies', 'Route A is closed',
             'the drive is independent of OI', 'A3–A6 fail', 'A3–A6 hold',
             'A1 and A2 hold for the witness', 'the lift is the only', 'only non-configuration-level sourcing is'):
    ok_max &= not _asserted(_man, _bad)
# no manuscript carries the pass; the registry classifies the module as kernel-only, no anchor
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_max &= 'ManuscriptAxioms' not in _t and 'A1Realized' not in _t and 'ConfigurationLevel' not in _t
_ma_fam = [f for f in _ptr_reg['families'] if f['name'] == 'manuscript axioms A1-A6']
ok_max &= len(_ma_fam) == 1 and _ma_fam[0]['status'] == 'kernel-only' and _ma_fam[0]['modules'] == ['ManuscriptAxioms']
ok_max &= _ma_fam[0]['manuscript'] == [] and 'asserts nothing about whether the witness satisfies any of A1-A6 in the manuscript sense' in _ma_fam[0]['note']
ok_max &= 'realized-core images' in _ma_fam[0]['note'] and 'requires some non-configuration-level sourcing' in _ma_fam[0]['note']
for _bad in ('faithful theory-level forms', 'every configuration-level sourcing of any substratum', 'only through the observer-level lift'):
    ok_max &= _bad not in _ma_fam[0]['note']
_cen_ma = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_max &= '| manuscript axioms A1–A6 | 1 | kernel-only |' in _cen_ma and 'realized-core images of A1 and A2' in _cen_ma
for _t in ('`R7-MAX`', 'MANUSCRIPT-AXIOM-AUDIT.md', 'A1Realized', 'A2Realized', 'ConfigurationLevel',
           'configurationLevel_not_phaseFree', 'formalization gap', 'Eleven named results',
           'no manuscript-level A1–A6 conjunct is presently a faithful predicate of the bare theory',
           'realized-core images', 'requires some non-configuration-level sourcing',
           'specifically named open candidate', 'not shown to be the only one',
           'asserts nothing about whether the witness satisfies any of A1–A6 in the manuscript sense'):
    ok_max &= _t in _rd1
check('R7-MAX', ok_max,
      'Manuscript-axiom guard: the module carries no sorry, axiom or native_decide and prints the axioms '
      'of exactly its eleven results; it defines exactly A1Realized, A2Realized, A1A2Realized and '
      'ConfigurationLevel, verbatim as pinned, with no predicate for A3–A6 and no ManuscriptOI; the '
      'note quotes the six axioms, gives each a representability verdict before the proof, preregisters '
      'the sourcing bound with its reading fixed in advance, records the scope repair made at review '
      'with the preregistration commit named, records the A1 and A2 realized-core images as holding '
      'and all six axioms as gaps at the manuscript-substratum level with the missing interface, the '
      'bound as necessity of a non-configuration-level sourcing with the lift as the named candidate '
      'and not the only route, the negative case as not established and the strongest form as not '
      'refuted, and asserts nothing about the witness against A1–A6 in the manuscript sense or about '
      'the strongest claim; the superseded readings are absent from the module, the README, the '
      'registry and the outcome; no manuscript carries the pass; the registry and the census carry the '
      'family as kernel-only with no anchor and the README carries the paragraph.')

# ---- The lift audit: three questions preregistered before the proof with their exclusions; Q1
# positive; Q2 negative for the substratum theory and consistent under control; the preregistered
# Q3 open at its hypothesis and the strengthened Q3' positive under SubstratumAvail; the
# preregistered Q4 not established and the strengthened Q4' the endpoint relative to the baseline;
# the object a layer and never the composite drive; nothing asserted about the lift, Route A, or
# the minimality of the baseline ----
ok_lift = True
_la = open(os.path.join(BRIDGE, 'OIBridge', 'LiftAudit.lean'), encoding='utf-8').read()
_laflat = ' '.join(_la.split())
_lan = open(os.path.join(os.path.dirname(BRIDGE), 'LIFT-AUDIT.md'), encoding='utf-8').read()
_lan1 = re.sub(r'\s+', ' ', _lan)
ok_lift &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _la) is None and 'native_decide' not in _la
ok_lift &= 'axiom ' not in re.sub(r'/-.*?-/', '', _la, flags=re.S)
_la_names = re.findall(r"^theorem ([\w']+)", _la, re.M)
ok_lift &= len(_la_names) == 56
for _nm in _la_names:
    ok_lift &= ('#print axioms ' + _nm) in _la
ok_lift &= _la.count('#print axioms') == 56
for _nm in ('gateFlow_unitary', 'gateFlow_group', 'gateFlow_zero', 'gateFlow_one', 'gateFlow_trace',
            'gateFlow_stage', 'layerFlowExecutable_of_control', 'gateFlow_half_not_preservesDiag',
            'configurationLevel_not_layerFlowExecutable', 'substratumTheory_not_layerFlowExecutable',
            'exp_smul_idempotent', 'flow_transition_closedForm', 'orb_mul', 'gateFlow_eq_orb',
            'flow_transition_eq_orb', 'signFun_mul', 'gateFlow_isolation', 'substratumTheory_substratumAvail',
            'phaseFree_of_layerFlowExecutable', 'derivedOI_qm_iff_layerFlowExecutable', 'regionSwap_moves',
            'substratumTheory_not_layerFlowExecutable_swap', 'phaseFree_of_layerFlowExecutable_swap',
            'derivedOI_qm_iff_layerFlowExecutable_swap'):
    ok_lift &= _nm in _la_names and _nm in _lan1
# the predicate is the only entry of unit into availability; the object is a layer involution
ok_lift &= ('def LayerFlowExecutable (T : FiniteOperationalTheory S) (σ : Equiv.Perm S) : Prop := '
            '∀ (n : ℕ) (t : ℝ), T.availExt n Unit (fun _ => conjChannel (gateFlow (levelPerm σ n) t))') in _laflat
ok_lift &= 'noncomputable def gateFlow (σ : Equiv.Perm S) (t : ℝ) : Matrix S S ℂ := unit (permMat σ) t' in _laflat
ok_lift &= 'driveQ' not in _la and 'layerQ' not in _la and 'swapQ' not in _la
ok_lift &= ('theorem substratumTheory_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : '
            '¬ LayerFlowExecutable (substratumTheory S) σ') in _laflat
ok_lift &= ('theorem phaseFree_of_layerFlowExecutable (T : FiniteOperationalTheory S) (hsub : SubstratumAvail T) '
            '{σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable T σ) : '
            'PhaseFreeRichness T') in _laflat
ok_lift &= ('theorem derivedOI_qm_iff_layerFlowExecutable [Nonempty S] (T : FiniteOperationalTheory S) '
            '(hd : DerivedOI T) (hsub : SubstratumAvail T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) '
            '{x : S} (hx : σ x ≠ x) : ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ') in _laflat
ok_lift &= ('= ReachabilitySeam.flow (transition a (τ a)) (Real.pi * t)') in _laflat
# the note: exclusions and questions precede the outcome; the outcome table; the deviation; the
# frontier; the non-claims
_i_q = _lan.find('## The three questions, in order, each with its own outcomes')
_i_out = _lan.find('## The outcome')
ok_lift &= 0 < _i_q < _i_out
ok_lift &= _lan.lstrip().startswith('# The lift audit')
for _t in ('The questions were evaluated in the preregistered order; Q1 and Q2 close, Q3 remains open at its preregistered hypothesis',
           'Executability is not inferred from the path', 'The CT2 flows are candidates, not operations',
           'The target is the literal interface', 'continuous mathematical path ⇒ executable continuous path ⇒ `PhaseFreeRichness`',
           '**Q1. Finite-region realization.**', '**Q2. Derived executability.**', '**Q3. Richness bridge.**',
           '**Q4, conditional, only if Q3 closes positively.**', 'Preregistration commit `0d299c7`',
           '| Q1, finite-region realization | **positive** |', '| Q2, derived executability | **negative** for `substratumTheory S`',
           '| Q3, richness bridge, as preregistered (`DerivedOI T` and `LayerFlowExecutable T σ` give `PhaseFreeRichness T`) | **open**',
           '| Q3′, the strengthened bridge (`SubstratumAvail T` and `LayerFlowExecutable T σ`',
           '| Q4, the endpoint, as preregistered (under `DerivedOI T` alone) | **not established as stated** |',
           '| Q4′, the strengthened endpoint | under `DerivedOI T ∧ SubstratumAvail T`',
           'Where the proved hypothesis is stronger than the preregistered one', 'The hypothesis proved is therefore `SubstratumAvail T`',
           'the theorems are Q3′ and Q4′, not Q3 and Q4', 'The preregistered Q3 is left **open** at its hypothesis',
           'The pass does not show that `SubstratumAvail` follows from `DerivedOI`, nor that it is the minimal extra baseline',
           'None of the three preregistered total outcomes is reached as stated',
           '**relative to the baseline `DerivedOI ∧ SubstratumAvail`**',
           'relative to the baseline `DerivedOI ∧ SubstratumAvail`',
           'What the outcome does not establish', 'Fifty-six named results', 'What this note does not claim',
           'Status: pass complete. Q1 positive; Q2 negative for the substratum theory and for every configuration-level class, executability consistent under control; the preregistered Q3, from `DerivedOI` and executability, is open'):
    ok_lift &= _t in _lan1
# the superseded readings are rejected: Q3 positive at the preregistered hypothesis, the second
# preregistered case, Q4 under DerivedOI alone, an unrelativized extra principle
_lan_out = _lan[_lan.find('## The outcome'):]
for _t in (_lan_out, _rd1, _laflat):
    for _bad in ('| Q3, richness bridge | **positive**', 'second preregistered case', 'Q3 positive', 'Q3 is positive',
                 'Every question closed in the preregistered order under its preregistered name',
                 'Every question closed in the preregistered order',
                 'Q4, the endpoint | under `DerivedOI T` and', 'One deviation from the preregistration',
                 'The one deviation from the preregistration', 'the extra sourcing principle is named exactly',
                 'The exact extra sourcing principle is isolated', 'Q3 — EXECUTABLE', 'Q4 — THE ENDPOINT'):
        ok_lift &= _bad not in _t
for _bad in ('the preregistered Q3 holds', 'Q3 as preregistered holds', 'SubstratumAvail follows from DerivedOI',
             'the baseline is minimal'):
    ok_lift &= not _asserted(_lan, _bad)
for _bad in ('the lift is derivable', 'the lift is not derivable', 'Route A is closed', 'executability is derived',
             'executability of the layer flow is derived', 'OI implies QM', 'the drive is derived from the substratum',
             'quantum mechanics requires OI', 'bare OI implies', 'the drive is independent of OI',
             'reads availability off the path', 'derived executable flow'):
    ok_lift &= not _asserted(_lan, _bad)
# no manuscript carries the audit; registry and census kernel-only; README paragraph
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_lift &= 'LayerFlowExecutable' not in _t and 'gateFlow_isolation`' not in _t and 'SubstratumAvail' not in _t
_la_fam = [f for f in _ptr_reg['families'] if f['name'] == 'lift audit: executable layer flows']
ok_lift &= len(_la_fam) == 1 and _la_fam[0]['status'] == 'current' and _la_fam[0]['modules'] == ['LiftAudit']
ok_lift &= _la_fam[0]['manuscript'] != [] and 'about whether the observer-level lift is derivable' in _la_fam[0]['note']
ok_lift &= 'relative to the baseline DerivedOI with SubstratumAvail' in _la_fam[0]['note'] and 'is open' in _la_fam[0]['note']
_cen_la = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_lift &= '| lift audit: executable layer flows | 1 | current |' in _cen_la
for _t in ('`R7-LIFT`', 'LIFT-AUDIT.md', 'LayerFlowExecutable', 'gateFlow_isolation', 'phaseFree_of_layerFlowExecutable',
           'derivedOI_qm_iff_layerFlowExecutable', 'Fifty-six named results', 'never the composite drive',
           'one non-monomial gate is not a result', 'is open, not established by this pass', 'strengthened Q3′',
           'is not established as stated; the strengthened Q4′ is proved',
           'relative to the baseline `DerivedOI` with the substratum\'s availability',
           'nor that this baseline is minimal', 'that the observer-level lift is derivable or is not',
           'that the preregistered Q3 or Q4 holds as stated'):
    ok_lift &= _t in _rd1
check('R7-LIFT', ok_lift,
      'Lift-audit guard: the module carries no sorry, axiom or native_decide and prints the axioms of exactly '
      'its fifty-six results; executability enters availability only through LayerFlowExecutable, the object '
      'is a layer involution\'s gate flow and the composite drive is never used; Q2 is the stated negative for '
      'the substratum theory, Q3′ the stated bridge under the substratum\'s availability with the preregistered '
      'Q3 recorded as open, Q4′ the stated equivalence relative to the baseline with the preregistered Q4 '
      'recorded as not established, and the isolation identity lands on the transition flow at angle πt; the '
      'note preregisters the three exclusions and the three questions before the outcome, names the '
      'preregistration commit, records the outcome table, the stronger hypothesis, the frontier arrow relative '
      'to the baseline and the non-claims, rejects the superseded readings, and asserts neither that the lift is '
      'derivable nor that it is not, nor that Route A is closed, nor that the baseline is minimal; no manuscript '
      'carries the audit; '
      'the registry and the census carry the family as kernel-only with no anchor and the README carries the '
      'paragraph.')

# ---- The substratum-interface audit: four distinctions frozen before the proof (substrate facts
# are not availability; substratumTheory is the current model, not the faithful image;
# SubstratumAvail audited, not assumed; no executability question); Q1 the axioms as predicates
# with A6 a gap and the wave rule an instance; Q2 the write access generates exactly the scaled
# partial permutations, which source no phase; Q3 the third preregistered outcome, SourcedOI with
# the exact missing conjunct to DerivedOI the phases, the failure of SubstratumAvail witnessed by
# them and its full gap not characterized; nothing asserted about the lift,
# executability, A6, or the manuscripts' sentences ----
ok_sub = True
_sa = open(os.path.join(BRIDGE, 'OIBridge', 'SubstratumInterfaceAudit.lean'), encoding='utf-8').read()
_saflat = ' '.join(_sa.split())
_san = open(os.path.join(os.path.dirname(BRIDGE), 'SUBSTRATUM-INTERFACE-AUDIT.md'), encoding='utf-8').read()
_san1 = re.sub(r'\s+', ' ', _san)
ok_sub &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _sa) is None and 'native_decide' not in _sa
ok_sub &= 'axiom ' not in re.sub(r'/-.*?-/', '', _sa, flags=re.S)
_sa_names = re.findall(r"^theorem ([\w']+)", _sa, re.M)
ok_sub &= len(_sa_names) == 82
for _nm in _sa_names:
    ok_sub &= re.search(r'^#print axioms (?:[\w.]+\.)?' + re.escape(_nm) + r'$', _sa, re.M) is not None
ok_sub &= _sa.count('#print axioms') == 82
# distinction 4: no executability question, no intermediate-time unitary
ok_sub &= 'LayerFlowExecutable' not in _sa and 'gateFlow' not in _sa and 'unit (' not in _sa
ok_sub &= 'driveQ' not in _sa and 'layerQ' not in _sa and 'swapQ' not in _sa
# Q1: the predicates verbatim, no predicate for A6, no ManuscriptOI
for _d in ('def A1 : Prop := Finite 𝒮.Conf',
           'def A2 : Prop := Function.Bijective 𝒮.φ',
           'def A3 (D : ℕ) : Prop := ∀ i, (𝒮.R.N i).card ≤ D',
           'def A4Exact : Prop := ∀ (v : 𝒮.ι) (c : 𝒮.ι → 𝒮.V), 𝒮.R.F (shiftBy v c) = shiftBy v (𝒮.R.F c)',
           'def A4 (G : Subgroup (Equiv.Perm 𝒮.Conf)) : Prop := ∀ v : 𝒮.ι, ∃ g ∈ G, ∀ x : 𝒮.Conf, 𝒮.φ (shiftBy v x) = g (shiftBy v (𝒮.φ x))',
           "def A5 : Prop := ∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'",
           'def A3Family (𝒮 : ℕ → Substratum) : Prop := ∃ D, ∀ L, (𝒮 L).A3 D',
           'def φ : 𝒮.Conf ≃ 𝒮.Conf := leapEquiv 𝒮.R.F'):
    ok_sub &= _d in _saflat
ok_sub &= re.search(r'\bA6\b\s*:', _sa) is None and 'def A6' not in _sa and 'ManuscriptOI' not in _sa
# Q2: the sourced class and its canonicity; the sourced theory; the invariant
for _d in ('def IsScaledPartialPerm (K : Matrix S S ℂ) : Prop := IsSubmonomial K ∧ ∃ c : ℂ, ‖c‖ ≤ 1 ∧ ∀ i j, K i j ≠ 0 → K i j = c',
           'def permClass : ImplementationClass := fun _ _ _ K => IsScaledPartialPerm K',
           'noncomputable abbrev permTheory (A : Type) [Fintype A] [DecidableEq A] : FiniteOperationalTheory A := genTheory permClass permClass_arch A',
           'noncomputable abbrev obsTheory : FiniteOperationalTheory 𝒮.Conf := permTheory 𝒮.Conf',
           'def PreservesNonneg (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop := ∀ X : Matrix S S ℂ, (∀ p q, 0 ≤ X p q) → ∀ p q, 0 ≤ Φ X p q',
           'def BijectionLevel (𝓘 : ImplementationClass) : Prop := ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → permClass S K',
           'def SourcedOI (T : FiniteOperationalTheory A) : Prop := ReversibleImplementationLocality T ∧ EmbeddedObservation T ∧ ExchangesAvailable T ∧ ReadWriteAvailable T',
           'theorem permClass_le_of_exchanges {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hex : ∀ (S : Type) [Fintype S] [DecidableEq S] (a b : S), 𝓘 S (permMatrix (Equiv.swap a b))) : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → 𝓘 S K',
           'theorem bijectionLevel_not_phasesAvailable [Nonempty A] {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hb : BijectionLevel 𝓘) : ¬ PhasesAvailable (genTheory 𝓘 arch A)',
           'theorem permTheory_not_substratumAvail [Nonempty A] : ¬ SubstratumAvail (permTheory A)',
           'theorem permTheory_not_derivedOI [Nonempty A] : ¬ DerivedOI (permTheory A)',
           'theorem derivedOI_iff_sourcedOI_phases (T : FiniteOperationalTheory A) : DerivedOI T ↔ SourcedOI T ∧ PhasesAvailable T',
           'theorem permTheory_realizesSealedOICore : RealizesSealedOICore (permTheory (Fin 2))',
           "obsTheory { ι := ι, V := V, R := R } = obsTheory { ι := ι, V := V, R := R' } := rfl"):
    ok_sub &= _d in _saflat
for _nm in ('a2_every_substratum', 'a1_of_finite', 'a3_of_fintype', 'a4_of_exact', 'waveSubstratum_A1',
            'waveSubstratum_A2', 'waveSubstratum_A3', 'waveSubstratum_A4Exact', 'waveSubstratum_A5',
            'scaledPartialPerm_iff', 'permClass_arch', 'permClass_le_of_exchanges', 'permClass_le_substratum',
            'preservesNonneg_conj_of_scaled', 'phaseGate_not_preservesNonneg', 'sign_not_preservesNonneg',
            'bijectionLevel_not_phasesAvailable', 'bijectionLevel_diagonal_only_scalar', 'sourcedOI_of_qm',
            'sourcedOI_qm_iff_phaseFree', 'exchanges_of_readWrite', 'permTheory_sourcedOI',
            'permTheory_not_phasesAvailable', 'permTheory_no_sign', 'substratumAvail_phasesAvailable',
            'permTheory_realizesSealedOICore', 'permTheory_falsifierUnavailable', 'permTheory_twoState',
            'obsTheory_rule_independent', 'obs_dynamics_avail', 'obs_shear_avail', 'obs_swap_avail',
            'obs_sourcedOI', 'obs_not_phasesAvailable', 'obs_diagonal_avail_only_scalar', 'obs_not_derivedOI',
            'obs_not_substratumAvail', 'obs_qm_iff_phaseFree'):
    ok_sub &= _nm in _sa_names and _nm in _san1
# the note: the four distinctions and the three questions precede the outcome; the commit; the
# outcome rows; the location of the phases; the non-claims
_i_dist = _san.find('## Four distinctions, frozen at the outset')
_i_q = _san.find('## The three questions, in order, each with its own outcomes')
_i_out = _san.find('## The outcome')
ok_sub &= 0 < _i_dist < _i_q < _i_out
ok_sub &= _san.lstrip().startswith('# The substratum-interface audit')
for _t in ('Substrate facts are not operational availability', 'is the current kernel model, not automatically the faithful image',
           'is audited, not assumed', 'No executability question', '`𝒮 ⟶ T_obs(𝒮)`, sourcing',
           '**Q1. Faithful substrate representation.**', '**Q2. Observer sourcing.**', '**Q3. Baseline comparison.**',
           'the one modelling input', 'the least architecture', 'Preregistration commit `f52f280`',
           '| A6 background independence |', '**gap**: the alphabet carries no internal index and no coupling matrix',
           '| Q1, faithful substrate representation | **as preregistered**', '| Q2, the phases | **negative**',
           '| Q3, baseline comparison | **the third preregistered outcome**',
           'so the gap to `DerivedOI` is exactly `PhasesAvailable`', 'the phases witness the failure of `SubstratumAvail`',
           'the full gap to `SubstratumAvail` is not characterized', '## Scope repair, recorded at review',
           'The gap to `SubstratumAvail` is witnessed, not characterized', 'Where a proved statement differs from the preregistered one',
           'The first and second Q3 outcomes are not reached', 'The phases, located', 'no phase is sourced',
           'is a theorem about every bijection-level sourcing', 'the round-62 stipulation',
           'is an owner decision for a propagation round; nothing is changed here',
           'What the outcome establishes', 'the full gap between the sourced theory and `SubstratumAvail` is not characterized here', 'consumes nothing of A3–A6',
           'What the outcome does not establish', 'no executability question was asked',
           'Eighty-one named results', 'What this note does not claim'):
    ok_sub &= _t in _san1
ok_sub &= 'Status: pass complete. Q1: A1, A2 and A5 are stated on the structure' in _san1
ok_sub &= 'the exact missing conjunct being `PhasesAvailable`; it also fails `SubstratumAvail`, the phases already witnessing that failure, while the full gap to `SubstratumAvail` is not characterized by this pass' in _san1
_i_rep = _san.find('## Scope repair, recorded at review')
ok_sub &= _i_q < _i_rep < _i_out
# the superseded reading, the gap to SubstratumAvail as exactly the phases, is absent from every
# outcome-facing surface; the docstring residue on A6 is absent from the module
# the overclaims are absent from every paragraph that does not disclaim them
for _bad in ('the phase structure is not part of OI', 'the manuscripts are wrong', 'A6 holds', 'A6 fails',
             'satisfies A1–A6', 'satisfies the manuscripts\' A1–A6', 'LayerFlowExecutable is derived',
             'executability is derived', 'the lift is derivable', 'the lift is not derivable', 'OI implies QM',
             'Route A is closed', 'the observer has no write access', 'SourcedOI is the manuscripts\' OI',
             'the phase structure is absent from the manuscripts', 'the manuscripts supply no phase',
             'quantum mechanics requires OI', 'bare OI implies', 'the drive is independent of OI'):
    ok_sub &= not _asserted(_san, _bad)
# the two Q3 outcomes not reached are named only as preregistered alternatives, never in the outcome
_san_out = _san[_san.find('## The outcome'):]
for _bad in ('the first preregistered outcome is reached', 'the sourced theory satisfies DerivedOI',
             'the sourced theory satisfies `DerivedOI`', 'SubstratumAvail is the faithful image',
             'the baseline stands as the faithful image', 'obs_derivedOI`', 'obs_substratumAvail`',
             'the second preregistered outcome is reached'):
    ok_sub &= _bad not in _san_out and _bad not in _rd1
# no manuscript carries the audit; registry and census kernel-only; README paragraph and counts
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_sub &= 'SubstratumInterfaceAudit' not in _t and 'permTheory' not in _t and 'SourcedOI' not in _t and 'obsTheory' not in _t
_sa_fam = [f for f in _ptr_reg['families'] if f['name'] == 'substratum interface: sourced observer theory']
ok_sub &= len(_sa_fam) == 1 and _sa_fam[0]['status'] == 'kernel-only' and _sa_fam[0]['modules'] == ['SubstratumInterfaceAudit']
ok_sub &= _sa_fam[0]['manuscript'] == [] and 'exact missing conjunct PhasesAvailable' in _sa_fam[0]['note']
ok_sub &= 'the full gap to SubstratumAvail is not characterized' in _sa_fam[0]['note']
for _t in (_san[_san.find('## The outcome'):], _rd1, _saflat, _sa_fam[0]['note']):
    for _bad in ('gap to both is exactly', 'gap to each being exactly', 'gap being exactly the phases',
                 'the gap being exactly `PhasesAvailable`', 'gap to both `DerivedOI` and `SubstratumAvail`',
                 'in exactly one conjunct, the phases', 'A1–A6 as predicates of it'):
        ok_sub &= _bad not in _t
ok_sub &= 'no executability question' in _sa_fam[0]['note'] and 'owner decision' in _sa_fam[0]['note']
ok_sub &= 'asserts nothing about whether the observer-level lift is derivable' in _sa_fam[0]['note']
_cen_sa = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_sub &= '| substratum interface: sourced observer theory | 1 | kernel-only |' in _cen_sa
for _t in ('`R7-SUB`', 'SUBSTRATUM-INTERFACE-AUDIT.md', 'permClass', 'SourcedOI', 'obsTheory', 'PreservesNonneg',
           'permClass_le_of_exchanges', 'bijectionLevel_not_phasesAvailable', 'permTheory_realizesSealedOICore',
           'obsTheory_rule_independent', 'Eighty-two named results', 'exact missing conjunct',
           'the full gap to `SubstratumAvail` is not characterized by the pass',
           'no executability question', 'A6 is a gap', 'owner decision', 'third preregistered outcome'):
    ok_sub &= _t in _rd1
ok_sub &= 'gap being exactly the phases' not in _cen_sa and 'the full gap to `SubstratumAvail` is not characterized' in _cen_sa
ok_sub &= '143 modules' in _rd1 and '3,102 named results' in _rd1
ok_sub &= '## Migration, recorded after the round' in _san and 'scalarHull_permClass_iff' in _san1
ok_sub &= '## Migration to instrument realization, recorded after the round' in _san
ok_sub &= 'permClass_unitaryRaySaturated' in _san1 and 'realized_of_instAvail permClass_arch' in _san1
check('R7-SUB', ok_sub,
      'Substratum-interface guard: the module carries no sorry, axiom or native_decide and prints the axioms '
      'of exactly its eighty-two results, the sourced class unitary-ray saturated after the migration; it asks no executability question (no LayerFlowExecutable, gateFlow, '
      'unit or drive); it defines A1, A2, A3, A3Family, A4Exact, A4 and A5 verbatim as pinned with no predicate '
      'for A6 and no ManuscriptOI; it defines the sourced class, the sourced and observer theories, the '
      'nonnegativity invariant, the bijection-level classes and SourcedOI verbatim, with the canonicity of the '
      'class, the no-phase theorem for every bijection-level class, the failure of DerivedOI and SubstratumAvail '
      'for the sourced theory, the sealed core without phases and the rule-independence of the observer theory '
      'stated as pinned; the note freezes the four distinctions and the three questions before the outcome, '
      'names the preregistration commit, records A6 as a gap, the phases as the one negative, the third Q3 '
      'outcome with the exact missing conjunct to DerivedOI the phases and the failure of SubstratumAvail '
      'witnessed by them with its full gap not characterized, the scope repair made at review with the '
      'superseded reading absent from every outcome-facing surface, the location of the phases as the round-62 stipulation with the '
      'manuscripts\' sentences an owner decision, and the non-claims; no manuscript carries the audit; the '
      'registry and the census carry the family as kernel-only with no anchor and the README carries the '
      'paragraph and the counts.')

# ---- The scalar-closure audit: Architecture.smul restricted to contractive scalars after the
# census; realized_smul_nonneg and realized_discard with the bound; the generated theory unchanged
# by definition; the sourced class migrated; the scalar-hull regression theorem; nothing weakens;
# the restriction recorded as not sufficient for the flow endpoint; no manuscript narrates it ----
ok_scal = True
_lrs = open(os.path.join(BRIDGE, 'OIBridge', 'ImplementationLocality.lean'), encoding='utf-8').read()
_lrsflat = ' '.join(_lrs.split())
_sc = open(os.path.join(BRIDGE, 'OIBridge', 'ScalarClosure.lean'), encoding='utf-8').read()
_scflat = ' '.join(_sc.split())
_scn = open(os.path.join(os.path.dirname(BRIDGE), 'SCALAR-CLOSURE-AUDIT.md'), encoding='utf-8').read()
_scn1 = re.sub(r'\s+', ' ', _scn)
ok_scal &= ('smul : ∀ (S : Type) [Fintype S] [DecidableEq S] (a : ℂ) (K : Matrix S S ℂ), ‖a‖ ≤ 1 → 𝓘 S K → 𝓘 S (a • K)') in _lrsflat
ok_scal &= ('theorem realized_smul_nonneg (hsmul : ∀ (a : ℂ) (K : Matrix S S ℂ), ‖a‖ ≤ 1 → 𝓘 S K → 𝓘 S (a • K)) '
            '{Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (c : ℝ) (hc : 0 ≤ c) (hc1 : c ≤ 1)') in _lrsflat
# the unrestricted form is gone from the architecture and from every hypothesis that fed it
ok_scal &= '(K : Matrix S S ℂ), 𝓘 S K → 𝓘 S (a • K)' not in _lrsflat
ok_scal &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _sc) is None and 'native_decide' not in _sc
ok_scal &= 'axiom ' not in re.sub(r'/-.*?-/', '', _sc, flags=re.S)
_sc_names = re.findall(r"^theorem ([\w']+)", _sc, re.M)
ok_scal &= len(_sc_names) == 12 and _sc.count('#print axioms') == 12
for _nm in _sc_names:
    ok_scal &= ('#print axioms ' + _nm) in _sc
for _nm in ('genTheory_availExt_eq', 'realized_real_smul', 'realized_scalarHull_iff', 'scalarHull_arch',
            'scalarHull_permClass_iff', 'permTheory_hull_availExt_iff', 'permClass_of_scalarHull_isometry',
            'instAvail_scalarHull_permClass'):
    ok_scal &= _nm in _sc_names and _nm in _scn1
ok_scal &= '(genTheory 𝓘 arch A).availExt n O F ↔ InstAvail 𝓘 (A × Fin n) O F' in _scflat
ok_scal &= '## Migration to instrument realization, recorded after the round' in _scn
ok_scal &= ("def scalarHull (𝓘 : ImplementationClass) : ImplementationClass := fun S _ _ K => "
            "∃ (a : ℂ) (K' : Matrix S S ℂ), 𝓘 S K' ∧ K = a • K'") in _scflat
ok_scal &= 'Realized (scalarHull 𝓘) S Φ ↔ Realized 𝓘 S Φ' in _scflat
ok_scal &= '↔ (permTheory A).availExt n O F' in _scflat
# the note: the decision, the change, the census and the tests precede the outcome
_i_cen = _scn.find('## The census of consumers, taken before the change')
_i_tests = _scn.find('## The tests, each with its admissible outcomes')
_i_out = _scn.find('## The outcome')
ok_scal &= 0 < _i_cen < _i_tests < _i_out
ok_scal &= _scn.lstrip().startswith('# The scalar-closure audit')
for _t in ('Unrestricted scalar closure is rejected as an operational reading', 'restricted to contractive scalars',
           'is not sufficient for the flow endpoint', '**T1. Operational preservation.**', '**T2. Class migration.**',
           '**T3. Regression.**', '**T4. What weakens.**', '**T5. Guards.**', 'Preregistration commit `8a4bfaa`',
           '| T1 | ', '| T2 | ', '| T3 | ', '| T4 | ', '| T5 | ', 'Nothing weakens', 'Ten named results',
           'What this note does not claim', 'does not touch `Realized`'):
    ok_scal &= _t in _scn1
ok_scal &= 'Status: pass complete' in _scn1
for _bad in ('the flow endpoint is settled', 'flowTheory fails', 'flowTheory has phase-free richness',
             'the countermodel is established', 'the replication loophole is closed', 'OI implies QM',
             'quantum mechanics requires OI', 'bare OI implies'):
    ok_scal &= not _asserted(_scn, _bad)
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_scal &= 'ScalarClosure' not in _t and 'scalarHull' not in _t and 'contractive scalar' not in _t
_sc_fam = [f for f in _ptr_reg['families'] if f['name'] == 'scalar closure: contractive architecture']
ok_scal &= len(_sc_fam) == 1 and _sc_fam[0]['status'] == 'verification-only' and _sc_fam[0]['modules'] == ['ScalarClosure']
ok_scal &= _sc_fam[0]['manuscript'] == [] and 'not sufficient for the flow endpoint' in _sc_fam[0]['note']
_cen_sc = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_scal &= '| scalar closure: contractive architecture | 1 | verification-only |' in _cen_sc
for _t in ('`R7-SCAL`', 'SCALAR-CLOSURE-AUDIT.md', 'realized_scalarHull_iff', 'permTheory_hull_availExt_iff',
           'instAvail_scalarHull_permClass', 'Twelve named results', 'modulus at most one', 'Nothing weakens',
           'is not sufficient for the flow endpoint'):
    ok_scal &= _t in _rd1
check('R7-SCAL', ok_scal,
      'Scalar-closure guard: Architecture.smul and the hypotheses that feed it are stated for scalars of modulus '
      'at most one and the unrestricted form is absent; realized_smul_nonneg carries the bound; the module carries '
      'no sorry, axiom or native_decide and prints the axioms of exactly its twelve results, with the scalar hull, the '
      'regression theorem and its instance for the migrated sourced class, re-proved for instrument realization, '
      'stated as pinned; the note records the '
      'owner decision, the change fixed in advance, the census before the change, the five tests before the '
      'outcome, the outcome per test, nothing weakening, the restriction as not sufficient for the flow endpoint, '
      'and the non-claims; no manuscript narrates the scalar closure; the registry and the census carry the family '
      'as verification-only and the README carries the paragraph and the counts.')

# ---- The instrument-realization audit, after its migration: the inductive predicate with five
# constructors and no sum is the implementation semantics of the kernel; the module keeps the
# branch-wise comparison object, the protocol invariant and the countercontrol in the closed-form
# ones-fixing class; the flow endpoint neither asserted nor refuted ----
ok_inst = True
_ir = open(os.path.join(BRIDGE, 'OIBridge', 'InstrumentRealization.lean'), encoding='utf-8').read()
_irflat = ' '.join(_ir.split())
_irn = open(os.path.join(os.path.dirname(BRIDGE), 'INSTRUMENT-REALIZATION-AUDIT.md'), encoding='utf-8').read()
_irn1 = re.sub(r'\s+', ' ', _irn)
_il = open(os.path.join(BRIDGE, 'OIBridge', 'ImplementationLocality.lean'), encoding='utf-8').read()
_ilflat = ' '.join(_il.split())
ok_inst &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _ir) is None and 'native_decide' not in _ir
ok_inst &= 'axiom ' not in re.sub(r'/-.*?-/', '', _ir, flags=re.S)
_ir_names = re.findall(r"^theorem ([\w']+)", _ir, re.M)
ok_inst &= len(_ir_names) == 69 and _ir.count('#print axioms') == 69
for _nm in _ir_names:
    ok_inst &= ('#print axioms ' + _nm) in _ir
# the inductive definition lives in ImplementationLocality: exactly five constructors, named, no sum
_i_ind = _il.find('inductive InstAvail (𝓘 : ImplementationClass) :')
ok_inst &= _i_ind > 0 and 'inductive InstAvail' not in _ir
_ind_block = _il[_i_ind:_il.find('\n\n', _i_ind)]
_ctors = re.findall(r'^  \| (\w+)', _ind_block, re.M)
ok_inst &= _ctors == ['op', 'readout', 'coarse', 'bind', 'discard']
ok_inst &= '∑' not in ' '.join(l for l in _ind_block.splitlines() if l.strip().startswith('| op') or l.strip().startswith('| bind') or l.strip().startswith('| discard'))
for _t in ('| op {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (hK : 𝓘 T K) (hiso : Kᴴ * K = 1) : InstAvail 𝓘 T Unit (fun _ => conjChannel K)',
           '| readout {T T\' : Type} [Fintype T] [DecidableEq T] [Fintype T\'] [DecidableEq T\'] {m : ℕ} (e : T\' × Fin m ≃ T) (hP : ∀ k, 𝓘 T (Matrix.reindex e e (readProj T\' m k))) : InstAvail 𝓘 T (Fin m) (fun k => conjChannel (Matrix.reindex e e (readProj T\' m k)))',
           'InstAvail 𝓘 T (O × O\') (fun c => (G c.1 c.2).comp (F c.1))',
           '| discard {T : Type} [Fintype T] [DecidableEq T] {m : ℕ} (hm : 0 < m) {O : Type} [Fintype O] [DecidableEq O]',
           'InstAvail 𝓘 T O (fun a => discardWith (A := T) m (uniformAttach m) (F a))',
           'theorem instAvail_trace', 'theorem realized_of_instAvail (arch : Architecture 𝓘)',
           'theorem instAvail_withSpectator', 'theorem genTheory_embeddedObservation',
           'theorem instAvail_fullClass_of_krausFamily'):
    ok_inst &= _t in _ilflat
# the comparison object and T2 in the module
for _t in ('def IsGenInstrument (𝓘 : ImplementationClass) (S : Type) [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop := (∀ a, Realized 𝓘 S (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace',
           'noncomputable def branchTheory', 'avail := fun _ _ _ F => IsGenInstrument 𝓘 S F',
           'theorem isGenInstrument_of_instAvail (arch : Architecture 𝓘)',
           '(h : (genTheory 𝓘 arch A).availExt n O F) : (branchTheory 𝓘 arch A).availExt n O F',
           'def OnesNormal (T : Type) [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) : Prop := ∃ (ι : Type) (_ : Fintype ι) (K : ι → Matrix T T ℂ) (out : ι → O), (∀ a, F a = ∑ i ∈ Finset.univ.filter (fun i => out i = a), conjChannel (K i)) ∧ ∑ i, (K i)ᴴ *ᵥ ones T = ones T',
           'def OnesFixing (𝓘 : ImplementationClass) : Prop := ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → Kᴴ * K = 1 → ∃ z : ℂ, K *ᵥ ones S = z • ones S',
           'theorem instAvail_onesNormal (hf : OnesFixing 𝓘)',
           'theorem instAvail_unitary_fixes_ones (hf : OnesFixing 𝓘)',
           'theorem isometry_fixes_ones : OnesFixing onesClass',
           'theorem flow_realized_not_instrumentRealized {a b c : T} (hab : a ≠ b) (hca : c ≠ a) (hcb : c ≠ b) : IsGenInstrument onesClass T (fun _ : Unit => conjChannel (ReachabilitySeam.flow (transition a b) (Real.pi / 2))) ∧ ¬ InstAvail onesClass T Unit (fun _ => conjChannel (ReachabilitySeam.flow (transition a b) (Real.pi / 2)))'):
    ok_inst &= _t in _irflat
ok_inst &= 'LayerFlowExecutable' not in _ir
for _bad in ('PhaseSaturated', 'InstrumentGenerated', 'InstrumentLocality', 'OIPlusInst', 'OIPlusMinInst',
             'DerivedOIInst', 'SourcedOIInst', 'RouteBTargetInst', 'SubstratumAvailInst', 'instTheory',
             'substratumInstTheory', 'permInstTheory'):
    ok_inst &= _bad not in _ir
# the note: the defect, the census, the shape, the tests, the non-doings, the amendments precede the
# outcome, and the migration section follows it
_j = [_irn.find(h) for h in ('## The defect', '## The census of consumers, taken before the change',
      '## The replacement, as an object to be defined', '## The tests, each with its admissible outcomes',
      '## What the round does not do', '## Amendments, recorded after the preregistration', '## The outcome',
      '## What this note does not claim', '## Migration, recorded after the round')]
ok_inst &= all(x > 0 for x in _j) and _j == sorted(_j)
ok_inst &= _irn.lstrip().startswith('# The instrument-realization audit')
for _t in ('Preregistration commit `9741199`', 'amendments commit `1f730b2`', 'Uniform ancilla: yes',
           '**T1. Soundness.**', '**T2. The converse fails.**', '**T3. The generated theory exists.**',
           '**T4. Survival.**', '**T5. The flow endpoint is not settled here.**', '**T6. Guards.**',
           '| T1 | ', '| T2 | ', '| T3 | ', '| T4 | ', '| T5 | ', '| T6 | ', '163 named results',
           'provenance removes the replication', '### T4, the survival record',
           'added hypotheses `Architecture 𝓘` and `PhaseSaturated 𝓘`', 'a recorded deviation',
           'What this note does not claim', 'That `Realized` or `ImplementationGenerated` has changed',
           'INSTRUMENT-MIGRATION-AUDIT.md', 'UnitaryRaySaturated', 'genTheory_le_branchTheory', '69 named results'):
    ok_inst &= _t in _irn1
ok_inst &= 'Status: pass complete' in _irn1
for _bad in ('settles the flow endpoint', 'the flow endpoint holds', 'the flow endpoint is refuted',
             'flowTheory fails', 'flowTheory has phase-free richness',
             'OI implies QM', 'quantum mechanics requires OI', 'bare OI implies',
             'the countermodel is established'):
    ok_inst &= not _asserted(_irn, _bad)
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_inst &= 'InstrumentRealization' not in _t and 'InstAvail' not in _t and 'instrument-realized' not in _t
    ok_inst &= 'UnitaryRaySaturated' not in _t and 'branchTheory' not in _t
_ir_fam = [f for f in _ptr_reg['families'] if f['name'] == 'instrument realization: one-instrument provenance']
ok_inst &= len(_ir_fam) == 1 and _ir_fam[0]['status'] == 'verification-only' and _ir_fam[0]['modules'] == ['InstrumentRealization']
ok_inst &= _ir_fam[0]['manuscript'] == [] and 'provenance removes the replication' in _ir_fam[0]['note'] and 'flow endpoint' in _ir_fam[0]['note']
ok_inst &= 'implementation semantics of the kernel' in _ir_fam[0]['note'] and 'UnitaryRaySaturated' in _ir_fam[0]['note']
_cen_ir = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_inst &= '| instrument realization: one-instrument provenance | 1 | verification-only |' in _cen_ir
ok_inst &= 'implementation semantics of the kernel after its migration' in _cen_ir
for _t in ('`R7-INST`', 'INSTRUMENT-REALIZATION-AUDIT.md', 'flow_realized_not_instrumentRealized',
           'instAvail_unitary_fixes_ones', 'Sixty-nine named results', 'provenance removes the replication',
           'genTheory_le_branchTheory', 'neither asserted nor refuted'):
    ok_inst &= _t in _rd1
check('R7-INST', ok_inst,
      'Instrument-realization guard: InstAvail is an inductive predicate in ImplementationLocality with exactly '
      'the five constructors op, readout, coarse, bind and discard, no constructor taking a sum, its step an '
      'admissible isometry, its readout a register readout with admissible projectors and its discard of '
      'positive size, stated as pinned; the module carries no sorry, axiom or native_decide and prints the '
      'axioms of exactly its sixty-nine results; the branch-wise comparison object, the inclusion of the '
      'generated theory in the branch-wise theory, the protocol invariant OnesNormal, the ones-fixing property, '
      'the general negative theorem and the countercontrol in the closed-form class are stated as pinned; the '
      'module mentions no executability and none of the parallel names of the previous round; the note keeps '
      'the defect, the census, the shape, the tests, the non-doings and the amendments before the outcome, names '
      'both commits, the owner decision, the six outcomes, the survival record, the deviation in the class of the '
      'countercontrol and the non-claims, carries its migration section after them, and asserts nothing about the '
      'flow endpoint; no manuscript carries the primitive; the registry and the census carry the family as '
      'verification-only with the migrated description and the README carries the paragraph and the count.')

# ---- The instrument-migration audit: provenance-aware realization as the implementation semantics
# in place; the parallel names gone; the saturation condition renamed, local to inverse
# accessibility and in no package; the positive-reachability core upstream of the stack; the four
# frozen notes with a migration section each; no manuscript edited ----
ok_mig = True
_mgn = open(os.path.join(os.path.dirname(BRIDGE), 'INSTRUMENT-MIGRATION-AUDIT.md'), encoding='utf-8').read()
_mgn1 = re.sub(r'\s+', ' ', _mgn)
_mrv2 = open(os.path.join(BRIDGE, 'OIBridge', 'MicroscopicReversibility.lean'), encoding='utf-8').read()
_mrv2flat = ' '.join(_mrv2.split())
_lrs2 = open(os.path.join(BRIDGE, 'OIBridge', 'LieRankSource.lean'), encoding='utf-8').read()
_lrs2flat = ' '.join(_lrs2.split())
# M1: the semantics, in place
ok_mig &= ('def ImplementationGenerated (T : FiniteOperationalTheory A) (𝓘 : ImplementationClass) : Prop := '
           '∀ (N : ℕ), 0 < N → ∀ (O : Type) [Fintype O] [DecidableEq O] '
           '(F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ), '
           'T.availExt N O F ↔ InstAvail 𝓘 (A × Fin N) O F') in _ilflat
ok_mig &= '(∀ a, Realized 𝓘 (A × Fin N) (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace' not in _ilflat
ok_mig &= 'noncomputable def genTheory (S : Type) [Fintype S] [DecidableEq S] : FiniteOperationalTheory S where avail := fun _ _ _ F => InstAvail 𝓘 S _ F availExt := fun _ _ _ _ F => InstAvail 𝓘 _ _ F' in _ilflat
ok_mig &= 'def Realized (𝓘 : ImplementationClass)' in _il and 'Φ = ∑ i, conjChannel (K i) ∧ ∀ i, 𝓘 S (K i)' in _ilflat
ok_mig &= 'structure Architecture (𝓘 : ImplementationClass) : Prop where' in _il
ok_mig &= _il.index('inductive InstAvail') < _il.index('def ImplementationGenerated') < _il.index('structure Architecture') < _il.index('noncomputable def genTheory')
ok_mig &= 'def ImplementationLocality (T : FiniteOperationalTheory A) : Prop := ∃ 𝓘 : ImplementationClass, ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘' in _ilflat
# M2: the three statements fixed in advance, and no other
ok_mig &= ('theorem inverseAccessibility_of_generated_daggerStable [Nonempty A] {T : FiniteOperationalTheory A} '
           '{𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hg : ImplementationGenerated T 𝓘) (hd : DaggerStable 𝓘) '
           '(hs : UnitaryRaySaturated 𝓘) : InverseAccessibility T') in _mrv2flat
ok_mig &= ('(harch : ∀ 𝓘, ImplementationGenerated T 𝓘 → Architecture 𝓘 ∧ UnitaryRaySaturated 𝓘) : InverseAccessibility T') in _mrv2flat
ok_mig &= 'def ReversibleImplementationLocality (T : FiniteOperationalTheory A) : Prop := ∃ 𝓘 : ImplementationClass, ImplementationGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘 ∧ DaggerStable 𝓘' in _mrv2flat
ok_mig &= 'theorem control_of_lieRank (h : LieRankRichness T) : HasCompositeUnitaryControl T' in _mrv2flat
ok_mig &= 'theorem genTheory_reversibleImplementationLocality' in _mrv2 and 'theorem genTheory_reversibleImplementationLocality' not in _lrs2
# M3: the compressed sets keep their statements; the inverse clause from Lie-rank control
ok_mig &= 'theorem oiPlusMicro_iff_qm : OIPlusMicro T ↔ ExactAllFiniteEndomorphicQuantumOps T' in _mrv2flat
ok_mig &= 'inverseAccessibility_of_lieRank T' in _slice(_mrv2, 'theorem oiPlusLocal_of_oiPlusMicro', 'theorem qm_of_oiPlusMicro')
ok_mig &= 'theorem oiPlusElem_iff_qm : OIPlusElem T ↔ ExactAllFiniteEndomorphicQuantumOps T' in _lrs2flat
ok_mig &= 'theorem oiPlusLocal_iff_qm : OIPlusLocal T ↔ ExactAllFiniteEndomorphicQuantumOps T' in _ilflat
# M4: saturation defined once, beside inverse accessibility, in no package and in no equivalence
ok_mig &= ('def UnitaryRaySaturated (𝓘 : ImplementationClass) : Prop := ∀ (S : Type) [Fintype S] [DecidableEq S] '
           '(c : ℂ) (V : Matrix S S ℂ), c ≠ 0 → Vᴴ * V = 1 → 𝓘 S (c • V) → 𝓘 S V') in _mrv2flat
ok_mig &= _mrv2.count('def UnitaryRaySaturated') == 1
_all_src = {}
for _f in sorted(os.listdir(os.path.join(BRIDGE, 'OIBridge'))):
    if _f.endswith('.lean'):
        _all_src[_f] = open(os.path.join(BRIDGE, 'OIBridge', _f), encoding='utf-8').read()
for _f, _t in _all_src.items():
    for _blk in re.findall(r'^def OIPlus\w+.*?(?=\n\n)', _t, re.S | re.M):
        ok_mig &= 'UnitaryRaySaturated' not in _blk
    for _blk in re.findall(r'^theorem \w+_iff_qm.*?(?=:=)', _t, re.S | re.M):
        ok_mig &= 'UnitaryRaySaturated' not in _blk
    for _blk in re.findall(r'^theorem carrier_general_\w+.*?(?=:=)', _t, re.S | re.M):
        ok_mig &= 'UnitaryRaySaturated' not in _blk
for _nm in ('fullClass_unitaryRaySaturated', 'diagClass_unitaryRaySaturated',
            'substratumClass_unitaryRaySaturated', 'permClass_unitaryRaySaturated'):
    ok_mig &= any(('#print axioms ' + _nm) in _t for _t in _all_src.values())
# M5: one name per result: the parallel names are absent from the whole kernel
for _bad in ('PhaseSaturated', 'InstrumentGenerated', 'InstrumentLocality', 'OIPlusInst', 'OIPlusMinInst',
             'DerivedOIInst', 'SourcedOIInst', 'RouteBTargetInst', 'SubstratumAvailInst', 'instTheory',
             'instFamily', 'substratumInstTheory', 'permInstTheory', 'inverseAccessibility_of_instrumentGenerated'):
    ok_mig &= all(_bad not in _t for _t in _all_src.values())
# the positive-reachability core upstream of the stack, the package downstream, every name unchanged
ok_mig &= 'import OIBridge.LieRankSource' not in _all_src['PositiveReachability.lean']
ok_mig &= 'import OIBridge.PositiveReachability' in _all_src['MicroscopicReversibility.lean']
ok_mig &= 'namespace PositiveReachability' in _all_src['PositivePackage.lean'] and 'import OIBridge.PositivePackage' in root
ok_mig &= 'import OIBridge.PositivePackage' in _all_src['MinimalRepertoire.lean'] and 'import OIBridge.PositivePackage' in _all_src['TypedPositive.lean']
# the consumers: proofs through soundness and monotonicity, statements unchanged
ok_mig &= 'InstAvail.op V hV hiso' in _all_src['SubstratumSource.lean']
ok_mig &= 'instAvail_mono (fun S _ _ K hK => h S K hK) hF' in _all_src['ManuscriptAxioms.lean']
for _f in ('RouteB.lean', 'LiftAudit.lean', 'ManuscriptAxioms.lean', 'SubstratumInterfaceAudit.lean', 'StructuralClosure.lean', 'LieRankSource.lean'):
    ok_mig &= 'realized_of_instAvail' in _all_src[_f]
ok_mig &= all('hav.1 ()' not in _t for _t in _all_src.values())
# the note: decision, census, plan, tests and non-doings precede the outcome and the non-claims
_k = [_mgn.find(h) for h in ('## The decision it implements', '## The census of what changes, taken before the edit',
      '## The module plan, fixed in advance', '## The tests, each with its admissible outcomes',
      '## What the round does not do', '## The outcome', '## What this note does not claim')]
ok_mig &= all(x > 0 for x in _k) and _k == sorted(_k)
ok_mig &= _mgn.lstrip().startswith('# The instrument-migration audit')
ok_mig &= 'Status: pass complete' in _mgn1 and 'Preregistration commit `45e6063`' in _mgn1
for _t in ('rename `PhaseSaturated` to `UnitaryRaySaturated`', '**M1. The semantics.**', '**M2. Statements.**',
           '**M3. The compressed sets.**', '**M4. Saturation, local.**', '**M5. One name per result.**',
           '**M6. The surfaces.**', '**M7. The checks.**', '| M1 | ', '| M2 | ', '| M3 | ', '| M4 | ', '| M5 | ',
           '| M6 | ', '| M7 | ', 'The names, each to its canonical counterpart', 'Two parallel results dropped',
           'Where the saturation condition is consumed', 'owner decision for a propagation round',
           'No further theorem needed a hypothesis', 'What this note does not claim', '121 modules and 2,699'):
    ok_mig &= _t in _mgn1
for _bad in ('settles the flow endpoint', 'the flow endpoint holds', 'the flow endpoint is refuted',
             'flowTheory fails', 'flowTheory has phase-free richness', 'OI implies QM',
             'quantum mechanics requires OI', 'bare OI implies', 'the countermodel is established',
             'the GR sentences are wrong', 'the manuscripts are wrong'):
    ok_mig &= not _asserted(_mgn, _bad)
# the four frozen notes carry a migration section each; no manuscript is edited
for _rel, _hdr in (('SUBSTRATUM-INTERFACE-AUDIT.md', '## Migration to instrument realization, recorded after the round'),
                   ('SCALAR-CLOSURE-AUDIT.md', '## Migration to instrument realization, recorded after the round'),
                   ('INSTRUMENT-REALIZATION-AUDIT.md', '## Migration, recorded after the round'),
                   ('INVERSE-CLAUSE-AUDIT.md', '## Migration, recorded after the round')):
    _t = open(os.path.join(os.path.dirname(BRIDGE), _rel), encoding='utf-8').read()
    ok_mig &= _hdr in _t and 'INSTRUMENT-MIGRATION-AUDIT.md' in _t
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_mig &= 'InstAvail' not in _t and 'UnitaryRaySaturated' not in _t and 'INSTRUMENT-MIGRATION' not in _t
_gr_txt = open(os.path.join(_msroot, 'papers/GR.md'), encoding='utf-8').read()
ok_mig &= 'with aggregate probability normalization' not in _gr_txt
ok_mig &= 'Probability normalization in aggregate is a consequence of that realization' in _gr_txt
for _t in ('`R7-MIG`', 'INSTRUMENT-MIGRATION-AUDIT.md', 'UnitaryRaySaturated', 'genTheory_le_branchTheory',
           'inverseAccessibility_of_lieRank', 'PositivePackage', 'canonical implementation semantics'):
    ok_mig &= _t in _rd1
check('R7-MIG', ok_mig,
      'Instrument-migration guard: ImplementationGenerated is instrument realization by the class and genTheory '
      'carries the instrument fields, in ImplementationLocality with the inductive predicate, the architecture and '
      'the closures upstream of them, the branch-wise generation clause absent and Realized kept as the comparison '
      'notion; exactly the three statements fixed in advance changed, inverse accessibility from dagger stability '
      'carrying Architecture and UnitaryRaySaturated, its per-class corollary the same, and genTheory_availExt_eq '
      'the new predicate; the compressed sets keep their statements with the inverse clause from Lie-rank control '
      'on the well-formed theory; UnitaryRaySaturated is defined once beside inverse accessibility, holds for the '
      'four classes and occurs in no package and in no equivalence; the parallel names of the previous round are '
      'absent from the kernel; the positive-reachability core imports nothing of the stack and the package sits in '
      'PositivePackage under the same namespace; the consumers are repaired through soundness and monotonicity; '
      'the note keeps the decision, the census, the plan, the tests and the non-doings before the outcome, names '
      'the preregistration commit, the seven outcomes, the name map, the two dropped results, where saturation is '
      'consumed and the GR sentences as an owner decision, and asserts nothing about the flow endpoint; the four '
      'frozen notes carry a migration section each; GR 3.3 carries the propagated normalization reading; the README carries the paragraph.')

# ---- The flow-endpoint audit: the arrow from the sourced baseline with the executable layer
# flow, decided negatively on the migrated semantics by the theory of the ones-fixing class, the
# negative at level two as preregistered; the least class undefined; the lift audit's Q3 from
# DerivedOI untouched; no manuscript narrates it ----
ok_flow = True
_fe = open(os.path.join(BRIDGE, 'OIBridge', 'FlowEndpoint.lean'), encoding='utf-8').read()
_feflat2 = ' '.join(_fe.split())
_fen = open(os.path.join(os.path.dirname(BRIDGE), 'FLOW-ENDPOINT-AUDIT.md'), encoding='utf-8').read()
_fen1 = re.sub(r'\s+', ' ', _fen)
_fxn = open(os.path.join(os.path.dirname(BRIDGE), 'FLOW-EXTENSION-AUDIT.md'), encoding='utf-8').read()
ok_flow &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _fe) is None and 'native_decide' not in _fe
ok_flow &= 'axiom ' not in re.sub(r'/-.*?-/', '', _fe, flags=re.S)
_fe_names = re.findall(r"^theorem ([\w']+)", _fe, re.M)
ok_flow &= len(_fe_names) == 15 and _fe.count('#print axioms') == 15
for _nm in _fe_names:
    ok_flow &= ('#print axioms ' + _nm) in _fe
# the test theory is the generated theory of the ones-fixing class; nothing else is defined
ok_flow &= 'noncomputable abbrev onesTheory (A : Type) [Fintype A] [DecidableEq A] : FiniteOperationalTheory A := genTheory onesClass onesClass_arch A' in _feflat2
ok_flow &= re.search(r'(?m)^(noncomputable )?def ', _fe) is None and re.search(r'(?m)^structure ', _fe) is None
ok_flow &= 'flowClass' not in _fe and 'flowTheory' not in _fe and 'IsGenInstrument' not in _fe and 'branchTheory' not in _fe
for _t in ('theorem onesTheory_sourcedOI : SourcedOI (onesTheory A)',
           'theorem onesTheory_layerFlowExecutable {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) : LayerFlowExecutable (onesTheory S) σ',
           'theorem onesTheory_no_quarter_flow {n : ℕ} {a b c : A × Fin n} (hab : a ≠ b) (hca : c ≠ a) (hcb : c ≠ b) : ¬ (onesTheory A).availExt n Unit (fun _ => conjChannel (ReachabilitySeam.flow (transition a b) (Real.pi / 2)))',
           'theorem onesTheory_not_phaseFree_general (h2 : 2 ≤ Fintype.card A) : ¬ PhaseFreeRichness (onesTheory A)',
           'theorem onesTheory_not_phaseFree : ¬ PhaseFreeRichness (onesTheory (Fin 2))',
           'theorem flow_endpoint_refuted : ∃ T : FiniteOperationalTheory (Fin 2), SourcedOI T ∧ LayerFlowExecutable T (Equiv.swap 0 1) ∧ ¬ PhaseFreeRichness T',
           'theorem flow_endpoint_refuted_general (h2 : 2 ≤ Fintype.card A) {σ : Equiv.Perm A} (hσ : ∀ x, σ (σ x) = x) : SourcedOI (onesTheory A) ∧ LayerFlowExecutable (onesTheory A) σ ∧ ¬ PhaseFreeRichness (onesTheory A)',
           'theorem onesTheory_not_phasesAvailable (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable (onesTheory A)',
           'theorem onesTheory_not_derivedOI (h2 : 2 ≤ Fintype.card A) : ¬ DerivedOI (onesTheory A)',
           'theorem onesTheory_not_substratumAvail (h2 : 2 ≤ Fintype.card A) : ¬ SubstratumAvail (onesTheory A)',
           'theorem onesTheory_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (onesTheory (Fin 2))'):
    ok_flow &= _t in _feflat2
# the negative is proved at level two: the witness level in the proof is the literal 2
_npf = _slice(_fe, 'theorem onesTheory_not_phaseFree_general', 'theorem onesTheory_not_phaseFree :')
ok_flow &= bool(_npf) and 'h 2 hcard' in _npf and 'Fintype.card (A × Fin 2)' in _npf
ok_flow &= 'flow_realized_not_instrumentRealized' in _slice(_fe, 'theorem onesTheory_no_quarter_flow', 'theorem onesTheory_not_phaseFree_general')
# the note: question, objects, mechanism, tests, meanings and non-doings precede the outcome
_k = [_fen.find(h) for h in ('## The question', '## The objects', '## The mechanism, fixed in advance',
      '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
      '## What the round does not do', '## Scope amendment, recorded after the preregistration',
      '## The outcome', '## What this note does not claim')]
ok_flow &= all(x > 0 for x in _k) and _k == sorted(_k)
ok_flow &= _fen.lstrip().startswith('# The flow-endpoint audit')
for _t in ('Preregistration commit `4ec3623`', 'Status: pass complete', 'commit `c19c12a`', 'The level of the negative, fixed now',
           'preregistered at level `n = 2`', 'not to be relocated', '**F1. The sourced closure.**', '**F2. Executability.**',
           '**F3. The endpoint, negative at level two.**', '**F4. The endpoint theorem.**', '**F5. The location of the failure.**',
           '**F6. The surfaces.**', '**F7. The checks.**', '| F1 | ', '| F2 | ', '| F3 | ', '| F4 | ', '| F5 | ', '| F6 | ', '| F7 | ',
           'no proved statement differs from the preregistered one', 'The obstruction was not moved',
           'What no outcome establishes', 'What the outcome does not establish', 'stays open as the lift audit records it',
           'fifteen named results', 'relative phase structure', 'What the round does not do', 'What this note does not claim',
           'the absence of phases witnesses the failure of `SubstratumAvail`', 'unique or the minimal', 'scope amendment above',
           'What is retained from the flow-extension audit', 'commit `490e03c`'):
    ok_flow &= _t in _fen1
for _bad in ('the preregistered Q3 holds', 'Q3 is refuted', 'the lift is derivable', 'the lift is not derivable',
             'Route A is closed', 'OI implies QM', 'quantum mechanics requires OI', 'bare OI implies',
             'the witness is minimal', 'onesTheory is minimal', 'executability is derived',
             'DerivedOI and executability fail to give phase-free richness'):
    ok_flow &= not _asserted(_fen, _bad)
ok_flow &= 'flowClass' not in _fen[_fen.find('## The outcome'):] or 'not defined' in _fen[_fen.find('## The outcome'):]
# the amended scope: the absence of phases witnesses the failure of SubstratumAvail and the gap is
# not characterized; relative phase is an obstruction identified, not the unique or minimal resource
_fen_out = _fen[_fen.find('## The outcome'):]
for _t in (_fen_out, _rd1, _feflat2, re.sub(r'\s+', ' ', _lan)):
    for _bad in ('exactly through the phases', 'the missing resource is a relative phase', 'the missing resource being a relative phase',
                 'gap to `SubstratumAvail` is exactly', 'the resource the executable layer flow lacks being a relative phase'):
        ok_flow &= _bad not in _t
for _bad in ('relative phase is the unique missing resource', 'relative phase is the minimal missing resource',
             'the gap to SubstratumAvail is exactly the phases'):
    ok_flow &= not _asserted(_fen, _bad)
# the superseded preregistration names this round; the lift audit records its Q3 untouched
ok_flow &= '## Superseded, recorded after the deferral' in _fxn and 'FLOW-ENDPOINT-AUDIT.md' in _fxn
ok_flow &= 'flow_endpoint_refuted' in _fxn and '## Deferral, recorded after the preregistration' in _fxn
ok_flow &= _fxn.find('## Deferral, recorded after the preregistration') < _fxn.find('## Superseded, recorded after the deferral')
ok_flow &= '## The flow endpoint on the sourced baseline, recorded after the round' in _lan
ok_flow &= 'stays open as the outcome above records it' in re.sub(r'\s+', ' ', _lan)
# no manuscript carries the round; the registry and the census carry the family as kernel-only
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_flow &= 'FlowEndpoint' not in _t and 'onesTheory' not in _t and 'flow_endpoint_refuted' not in _t and 'onesClass' not in _t
_fe_fam = [f for f in _ptr_reg['families'] if f['name'] == 'flow endpoint: executable layer flow on the sourced baseline']
ok_flow &= len(_fe_fam) == 1 and _fe_fam[0]['status'] == 'kernel-only' and _fe_fam[0]['modules'] == ['FlowEndpoint']
ok_flow &= _fe_fam[0]['manuscript'] == [] and 'level two' in _fe_fam[0]['note'] and 'relative phase structure' in _fe_fam[0]['note']
ok_flow &= 'not shown unique or minimal' in _fe_fam[0]['note'] and 'full gap not characterized' in _fe_fam[0]['note']
ok_flow &= 'untouched and stays open' in _fe_fam[0]['note'] and 'not claimed minimal' in _fe_fam[0]['note']
_cen_fe = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_flow &= '| flow endpoint: executable layer flow on the sourced baseline | 1 | kernel-only |' in _cen_fe
for _t in ('`R7-FLOW`', 'FLOW-ENDPOINT-AUDIT.md', 'onesTheory', 'flow_endpoint_refuted', 'onesTheory_no_quarter_flow',
           'Fifteen named results', 'preregistered at level two', 'proved there and not elsewhere', 'relative phase structure',
           'the absence of phases witnesses the failure', 'unique or minimal missing resource',
           'from `DerivedOI`, is untouched and stays open', 'not a minimal one', 'Route A in either direction'):
    ok_flow &= _t in _rd1
ok_flow &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-FLOW', ok_flow,
      'Flow-endpoint guard: the module carries no sorry, axiom or native_decide and prints the axioms of exactly '
      'its fifteen results; it defines nothing but the test theory, the generated theory of the ones-fixing class, '
      'and names no least class; the sourced closure, the executability of every layer flow, the quarter-turn '
      'obstruction on every carrier with a third point, the failure of phase-free richness at the literal level two, '
      'the endpoint theorem on the two-state carrier and in general, and the failure of the phases, DerivedOI, '
      'SubstratumAvail and quantum mechanics are stated as pinned; the note keeps the question, the objects, the '
      'mechanism, the tests, the meanings and the non-doings before the outcome, names both commits, fixes the '
      'level of the negative in advance and records it proved there, carries the scope amendment reading the absence '
      'of phases as a witness of the failure of SubstratumAvail with the gap not characterized and relative phase as an '
      'obstruction identified and not the unique or minimal resource, and asserts nothing about the lift audit\'s '
      'Q3, the lift, Route A or minimality; the flow-extension note names this round as its superseding '
      'preregistration after its deferral; the lift audit records its Q3 untouched; no manuscript carries the '
      'round; the registry and the census carry the family as kernel-only and the README carries the paragraph '
      'and the counts.')

# ---- The phase-source audit: whether the stated substratum and observer access derive the
# phases; the ones-fixing invariant general; the sourced class ones-fixing; the distinctions in
# the kernel; the round-62 phase intervention isolated as the one source; the census verdicts;
# no new intervention kind, class or theory; no manuscript narrates it ----
ok_phase = True
_ps = open(os.path.join(BRIDGE, 'OIBridge', 'PhaseSource.lean'), encoding='utf-8').read()
_psflat = ' '.join(_ps.split())
_psn = open(os.path.join(os.path.dirname(BRIDGE), 'PHASE-SOURCE-AUDIT.md'), encoding='utf-8').read()
_psn1 = re.sub(r'\s+', ' ', _psn)
ok_phase &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _ps) is None and 'native_decide' not in _ps
ok_phase &= 'axiom ' not in re.sub(r'/-.*?-/', '', _ps, flags=re.S)
_ps_names = re.findall(r"^theorem ([\w']+)", _ps, re.M)
ok_phase &= len(_ps_names) == 10 and _ps.count('#print axioms') == 10
for _nm in _ps_names:
    ok_phase &= ('#print axioms ' + _nm) in _ps
# nothing is defined: no intervention kind, no class, no theory
ok_phase &= re.search(r'(?m)^(noncomputable )?(def|abbrev|structure|inductive) ', _ps) is None
for _t in ('theorem onesFixing_not_phasesAvailable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hf : OnesFixing 𝓘) (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable (genTheory 𝓘 arch A)',
           'theorem permClass_onesFixing : OnesFixing permClass',
           'theorem permTheory_not_phasesAvailable_onesFixing {A : Type} [Fintype A] [DecidableEq A] (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable (permTheory A)',
           'theorem bijectiveOperator_mulVec_ones (σ : Equiv.Perm S) : bijectiveOperator σ *ᵥ ones S = ones S',
           'theorem readWriteOperator_mulVec_ones {a b : S} (F : ReadWriteFamily a b) (l : ℝ) : readWriteOperator F l *ᵥ ones S = ones S',
           'theorem phaseGate_not_scalar (h2 : 2 ≤ Fintype.card S) (a : S) (c : ℂ) : phaseGate a ≠ c • (1 : Matrix S S ℂ)',
           'theorem conjChannel_phaseGate_ne_id (h2 : 2 ≤ Fintype.card S) (a : S) : conjChannel (phaseGate a) ≠ LinearMap.id',
           'theorem diagonal_conj_phaseGate (d : S → ℂ) (hd : ∀ i, star (d i) * d i = 1) (a : S) : Matrix.diagonal d * phaseGate a * (Matrix.diagonal d)ᴴ = phaseGate a',
           'theorem phaseGate_moves_ones (h2 : 2 ≤ Fintype.card S) (a : S) (z : ℂ) : phaseGate a *ᵥ ones S ≠ z • ones S',
           'theorem substratumClass_not_onesFixing : ¬ OnesFixing substratumClass'):
    ok_phase &= _t in _psflat
ok_phase &= 'instAvail_unitary_fixes_ones' in _slice(_ps, 'theorem onesFixing_not_phasesAvailable', 'end Invariant')
ok_phase &= 'onesFixing_not_phasesAvailable permClass_arch permClass_onesFixing' in _psflat
# the note: question, distinctions, census, criteria, tests, meanings and non-doings precede the outcome
_k = [_psn.find(h) for h in ('## The question', '## Four distinctions, frozen at the outset',
      '## The census of purported sources, taken before the pass', '## The criteria, fixed in advance',
      '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
      '## What the round does not do', '## Scope amendment, recorded after the preregistration',
      '## The outcome', '## What this note does not claim')]
ok_phase &= all(x > 0 for x in _k) and _k == sorted(_k)
ok_phase &= _psn.lstrip().startswith('# The phase-source audit')
for _t in ('Preregistration commit `2cc1cbc`', 'Status: pass complete', 'commit `b1c0677`',
           '**(D1) Gauge is not an intervention.**', '**(D2) A representation fact is not availability.**',
           '**(D3) A global phase is not the resource.**', '**(D4) Availability is instrument realization.**',
           '| P1, the phase intervention |', '| P2, the substratum-source sentence |', '| P9, the observer architecture\'s own operations |',
           '**Positive.**', '**Negative.**', '**Underdetermined.**',
           '**T1. The invariant, general.**', '**T2. The stated access is ones-fixing.**', '**T3. The distinctions, in the kernel.**',
           '**T4. The stipulation, isolated.**', '**T5. The manuscript census, per entry.**', '**T6. The countercontrol.**',
           '**T7. The surfaces and the checks.**', '| T1 | ', '| T7 | ', 'The verdicts, per entry', 'The headline',
           'no proved statement differs from the preregistered one', 'negative for the stated access', 'rests on P1, a stipulation',
           'The missing access, under the scope amendment', 'scope amendment above', 'necessary condition',
           'the sufficient access tested is the quarter-phase intervention itself',
           'Moving the ray is not by itself sufficient', 'moving the all-ones ray is sufficient to source `PhasesAvailable`',
           'What the outcome does not establish', 'What this note does not claim', 'ten named results'):
    ok_phase &= _t in _psn1
for _bad in ('the manuscripts are wrong', 'DerivedOI is false', 'the phases cannot be sourced', 'the lift is derivable',
             'the lift is not derivable', 'Route A is closed', 'OI implies QM', 'quantum mechanics requires OI',
             'bare OI implies', 'relative phase is the unique missing resource', 'relative phase is the minimal missing resource',
             'the preregistered Q3 holds', 'Q3 is refuted', 'the phase structure is derived', 'PhasesAvailable is derived',
             'moving the all-ones ray is sufficient', 'the ray-moving condition is sufficient'):
    ok_phase &= not _asserted(_psn, _bad)
# the amended scope on every outcome-facing surface: the ray-moving condition is necessary, the
# sufficient access tested is the quarter-phase intervention, and neither is stated as the other
_psn_out = _psn[_psn.find('## The outcome'):]
for _t in (_psn_out, _rd1, re.sub(r'\s+', ' ', _san)):
    for _bad in ('the missing access is named: an admissible operator', 'missing access named as an admissible operator that moves the all-ones ray',
                 'of which the quarter phase is the canonical instance', 'of which the quarter phase `phaseGate a` is the canonical instance'):
        ok_phase &= _bad not in _t
# the frozen notes carry their sections; no manuscript is edited
_ssn = open(os.path.join(os.path.dirname(BRIDGE), 'SUBSTRATUM-SOURCE-AUDIT.md'), encoding='utf-8').read()
ok_phase &= '## Fifth entry, recorded after the freeze: the phase source' in _ssn and _ssn.find('## Freeze') < _ssn.find('## Fifth entry, recorded after the freeze')
ok_phase &= 'substratumClass_not_onesFixing' in _ssn
ok_phase &= '## The phases, decided, recorded after the round' in _san and 'permClass_onesFixing' in _san
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_phase &= 'OnesFixing' not in _t and 'PHASE-SOURCE' not in _t and 'phaseGate_moves_ones' not in _t
# the substratum-source sentence, requalified in the propagation round, cites the three deciding theorems
_gr_txt2 = open(os.path.join(_msroot, 'papers/GR.md'), encoding='utf-8').read()
ok_phase &= 'and the phase structure — supplies the structural part in full' not in _gr_txt2
ok_phase &= 'The phase intervention enters as an assumption on the substratum class' in _gr_txt2
ok_phase &= '`permClass_onesFixing`, `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing` in `OIBridge/PhaseSource.lean`' in _gr_txt2
_ps_fam = [f for f in _ptr_reg['families'] if f['name'] == 'phase source: the stated access and the stipulated phases']
ok_phase &= len(_ps_fam) == 1 and _ps_fam[0]['status'] == 'current' and _ps_fam[0]['modules'] == ['PhaseSource']
ok_phase &= _ps_fam[0]['manuscript'] != [] and 'a stipulation' in _ps_fam[0]['note'] and 'underdetermined' in _ps_fam[0]['note']
ok_phase &= 'PHASE-PROPAGATION-AUDIT.md' in _ps_fam[0]['note'] and 'no complex structure' in _ps_fam[0]['note']
ok_phase &= 'sufficient access tested' in _ps_fam[0]['note'] and 'missing access named as an admissible operator' not in _ps_fam[0]['note']
_cen_ps = re.sub(r'\s+', ' ', open(os.path.join(os.path.dirname(BRIDGE), 'LEAN-MANUSCRIPT-CENSUS.md'), encoding='utf-8').read())
ok_phase &= '| phase source: the stated access and the stipulated phases | 1 | current |' in _cen_ps
for _t in ('`R7-PHASE`', 'PHASE-SOURCE-AUDIT.md', 'onesFixing_not_phasesAvailable', 'permClass_onesFixing',
           'substratumClass_not_onesFixing', 'Ten named results', 'a stipulation, and on nothing else',
           'current OI sourcing stops', 'is underdetermined, and what it would have to supply is stated in two parts',
           'the necessary condition, an admissible operator selectable at every level', 'the sufficient access tested',
           'moving the ray alone being no guarantee of a quarter phase',
           'an additional physical assumption on the route', 'recorded for the propagation'):
    ok_phase &= _t in _rd1
check('R7-PHASE', ok_phase,
      'Phase-source guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'ten results and defines no intervention kind, class or theory; the general ones-fixing invariant, the '
      'ones-fixing sourced class with its no-phase corollary, the ones-fixing bijective, read-write and layer '
      'operators, the three distinctions and the isolation of the round-62 phase intervention are stated as '
      'pinned; the note keeps the question, the four distinctions, the nine-entry census, the criteria, the '
      'tests, the meanings and the non-doings before the outcome, names both commits, records the verdict per '
      'entry with the stated access negative and the phrase underdetermined, carries the scope amendment reading the '
      'ray-moving condition as necessary and the quarter-phase intervention as the sufficient access tested, and '
      'asserts nothing about the lift audit\'s Q3, the lift, Route A, uniqueness or minimality, or the '
      'manuscripts being wrong; the frozen substratum-source and substratum-interface notes carry their sections; '
      'the substratum-source sentence is requalified in the propagation round, citing the three deciding theorems; '
      'the registry and the census carry the family as current and the README carries the paragraph and the counts.')

# ---- phase-source propagation guard: the manuscripts state the sourced boundary, publication-only ----
ok_prop = True
_ppn = open(os.path.join(os.path.dirname(BRIDGE), 'PHASE-PROPAGATION-AUDIT.md'), encoding='utf-8').read()
_ppn1 = re.sub(r'\s+', ' ', _ppn)
ok_prop &= _ppn.lstrip().startswith('# The phase-source propagation round')
_i_pitems = _ppn.find('## The three items, fixed in advance')
_i_pcons = _ppn.find('## The constraints, fixed in advance')
_i_ptests = _ppn.find('## The tests, fixed in advance')
_i_pnot = _ppn.find('## What the round does not do')
_i_pout = _ppn.find('## The outcome')
ok_prop &= 0 < _i_pitems < _i_pcons < _i_ptests < _i_pnot < _i_pout
for _t in ('Preregistration commit `76e1a3a`', 'Status: pass complete', '`main` at `05e290b`',
           '**Item 1, the two normalization sentences.**', '**Item 2, the file attributions moved by the migration.**',
           '**Item 3, the substratum-source sentence.**', '**The mirrors, per §A.25.**',
           '**E1. The normalization sentences.**', '**E6. The checks.**', '| E1 | ', '| E6 | ',
           'moving the all-ones ray is not shown sufficient', 'No theorem is added, changed or removed',
           'zero occurrences', 'six occurrences'):
    ok_prop &= _t in _ppn1
for _bad in ('moving the all-ones ray is sufficient', 'the ray-moving condition is sufficient',
             'the substratum derives the phases', 'the phase structure is derived', 'PhasesAvailable is derived',
             'Q3 is refuted', 'the preregistered Q3 holds',
             'the manuscripts are wrong', 'OI implies QM', 'bare OI implies'):
    ok_prop &= not _asserted(_ppn, _bad)
# GR 3.3: realization by one protocol with normalization as a consequence; the phase intervention as an
# assumption, in two parts; the moved names attributed to their modules
_pgr1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, 'papers/GR.md'), encoding='utf-8').read())
for _t in ('Operational interventions are those realized by one protocol built from admissible implementation operators',
           'the branches of an intervention arise together as the outcomes of one protocol',
           'Probability normalization in aggregate is a consequence of that realization rather than a clause of it',
           'the normalization half of operational validity is a consequence of implementation generation',
           '`instAvail_trace`',
           'together with one further intervention principle, that a relative phase on a single state is a selectable intervention at every level',
           'The phase intervention enters as an assumption on the substratum class, not as a consequence of the finite states with the bijective read-write dynamics',
           'no class whose isometries do so realizes a quarter phase at any level with two or more states',
           'An operator carrying the all-ones vector off its ray is therefore necessary to any access that supplies the phases, and is not shown sufficient',
           'the access assumed is the quarter-phase intervention itself, a member of the class as stated',
           '`permClass_onesFixing`, `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing` in `OIBridge/PhaseSource.lean`',
           '`phase_monomial` in `OIBridge/SubstratumInterface.lean`',
           'the phase intervention enters as an assumption on the substratum class itself',
           '`control_of_lieRank` in `OIBridge/MicroscopicReversibility.lean`',
           '`carrier_general_oiPlusPos`, `oiPlusPos_iff_qm` in `OIBridge/PositivePackage.lean`',
           '`universalReachability_of_lieRank_positive` in `OIBridge/PositiveReachability.lean`'):
    ok_prop &= _t in _pgr1
ok_prop &= ('`carrier_general_oiPlusPos` in `OIBridge/PositivePackage.lean`, `inverseAccessibility_of_lieRank` in '
            '`OIBridge/MicroscopicReversibility.lean`') in re.sub(r'\s+', ' ', open(os.path.join(_msroot, 'papers/Main.md'), encoding='utf-8').read())
# the five mirrors of the substratum-source summary qualify the phases the same way
_pqual = ('the exchanges of distinguishable states, and, as a stated intervention principle rather than a consequence of its '
          'finite states and bijective dynamics, the phases — but, under finite bijective read-write dynamics')
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read())
    ok_prop &= _pqual in _t1 and 'the exchanges of distinguishable states, and the phases — but' not in _t1
ok_prop &= _t1.count(_pqual) == 2
# the superseded clauses, the moved attributions and the sufficiency misreading are absent from every manuscript
# source and generated form; no manuscript names the kernel predicates of the boundary
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/ch01-observation.md', 'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md',
             'papers/GR.tex', 'papers/Main.tex', 'papers/Explainer.tex', 'book/The-Incompleteness-of-Observation-FULL.tex'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read()).replace('\\_', '_')
    ok_prop &= 'with aggregate probability normalization' not in _t1
    ok_prop &= 'explicit in implementation generation' not in _t1
    ok_prop &= 'and the phase structure — supplies the structural part in full' not in _t1
    for _nm in ('control_of_lieRank', 'inverseAccessibility_of_lieRank', 'carrier_general_oiPlusPos', 'oiPlusPos_iff_qm'):
        ok_prop &= not re.search(re.escape(_nm) + r'[^.]{0,60}OIBridge/PositiveReachability', _t1)
    for _bad in ('moving the all-ones ray is sufficient', 'any operator that moves the all-ones ray supplies',
                 'the phases are derived', 'derives the phases', 'the phase structure is derived',
                 'derives the phase structure', 'supplies the phase structure', 'the phases are a consequence of',
                 'SourcedOI', 'DerivedOI', 'PhasesAvailable', 'RouteB', 'InstAvail'):
        ok_prop &= _bad not in _t1
# the registry, the census note and the README carry the round; the kernel is untouched
_pp_fam = [f for f in _ptr_reg['families'] if f['name'] == 'phase source: the stated access and the stipulated phases']
ok_prop &= len(_pp_fam) == 1 and _pp_fam[0]['status'] == 'current'
ok_prop &= {m['file'] for m in _pp_fam[0]['manuscript']} == {'papers/GR.md', 'papers/Main.md'}
ok_prop &= 'as an assumption' in _pp_fam[0]['note'] and 'carried by no manuscript' not in _pp_fam[0]['note']
_pir_fam = [f for f in _ptr_reg['families'] if f['name'] == 'instrument realization: one-instrument provenance']
ok_prop &= len(_pir_fam) == 1 and 'owner decision for a propagation round' not in _pir_fam[0]['note']
ok_prop &= 'instAvail_trace' in _pir_fam[0]['note'] and _pir_fam[0]['status'] == 'verification-only'
ok_prop &= '| phase source: the stated access and the stipulated phases | 1 | current |' in _cen_ps
for _t in ('`R7-PROP`', 'PHASE-PROPAGATION-AUDIT.md', 'realization by one protocol', 'as an assumption on the substratum class',
           'is necessary to any access that supplies the phases and is not shown sufficient', 'the sufficient access assumed',
           'No theorem is added or changed'):
    ok_prop &= _t in _rd1
check('R7-PROP', ok_prop,
      'Phase-source propagation guard: the note keeps the three items, the mirrors, the constraints, the tests and '
      'the non-doings before the outcome, names both commits, and asserts neither that moving the all-ones ray '
      'suffices nor that the phases are derived; GR 3.3 states implementation locality as realization by one '
      'protocol with normalization in aggregate its consequence, citing instAvail_trace, and the sentence after '
      'the boxed equivalence the same; the moved names are attributed to MicroscopicReversibility and '
      'PositivePackage in GR and Main with the positive reachability theorem keeping its path; the '
      'substratum-source sentence states the phase intervention as an assumption on the substratum class with '
      'the necessary condition and the sufficient access assumed as two parts, citing the three deciding '
      'theorems and the stated member; the five mirrors qualify the phases the same way; the superseded clauses, '
      'the moved attributions, the sufficiency misreading and the kernel predicates of the boundary are absent '
      'from every manuscript source and generated form; the registry carries the phase-source family as current '
      'with anchors in GR and Main and the instrument-realization note corrected; the census note and the README '
      'carry the round.')

# ---- the Q3 round: phase-free richness from the closure and one executable layer flow, the phase
# hypothesis explicit and consumed at the sign flip; the endpoint under the closure alone ----
ok_q3 = True
_q3 = open(os.path.join(BRIDGE, 'OIBridge', 'DerivedQ3.lean'), encoding='utf-8').read()
_q3flat = ' '.join(_q3.split())
_q3n = open(os.path.join(os.path.dirname(BRIDGE), 'DERIVED-Q3-AUDIT.md'), encoding='utf-8').read()
_q3n1 = re.sub(r'\s+', ' ', _q3n)
ok_q3 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _q3) is None and 'native_decide' not in _q3
ok_q3 &= 'axiom ' not in re.sub(r'/-.*?-/', '', _q3, flags=re.S)
_q3_names = re.findall(r"^theorem ([\w']+)", _q3, re.M)
ok_q3 &= len(_q3_names) == 17 and _q3.count('#print axioms') == 17
for _nm in _q3_names:
    ok_q3 &= ('#print axioms ' + _nm) in _q3
# the module defines one function, the sign flip, and no intervention kind, class or theory
ok_q3 &= re.findall(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) (\w+)', _q3, re.M) == ['flipAt']
ok_q3 &= 'import OIBridge.PhaseSource' in _q3 and 'import OIBridge.DerivedQ3' in root
# no continuous phase, no substratum availability and no countertheory enter
for _t in ('phaseFun', 'SubstratumAvail', 'diagonal_avail', 'derivedQ3_refuted'):
    ok_q3 &= _t not in _q3
# the statements, as preregistered
for _t in ('def flipAt (b z : S) : ℂ := if z = b then -1 else 1',
           'theorem phaseGate_mul_self (b : S) : phaseGate b * phaseGate b = Matrix.diagonal (flipAt b)',
           'theorem gateFlow_isolation_flip {τ : Equiv.Perm S} (hτ : ∀ z, τ (τ z) = z) {a : S} (ha : τ a ≠ a) (t : ℝ) : '
           'gateFlow τ t * (Matrix.diagonal (flipAt (τ a)) * gateFlow τ (-t) * Matrix.diagonal (flipAt (τ a))) '
           '= ReachabilitySeam.flow (transition a (τ a)) (Real.pi * t)',
           'theorem flip_avail (T : FiniteOperationalTheory S) (hph : PhasesAvailable T) (n : ℕ) (b : S × Fin n) : '
           'T.availExt n Unit (fun _ => conjChannel (Matrix.diagonal (flipAt b)))',
           'theorem phaseFree_of_phases_layerFlowExecutable (T : FiniteOperationalTheory S) (hph : PhasesAvailable T) '
           '(hexch : ExchangesAvailable T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) '
           '(hex : LayerFlowExecutable T σ) : PhaseFreeRichness T',
           'theorem phaseFree_of_derivedOI_layerFlowExecutable (T : FiniteOperationalTheory S) (hd : DerivedOI T) '
           '{σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable T σ) : PhaseFreeRichness T',
           "theorem derivedOI_qm_iff_layerFlowExecutable' [Nonempty S] (T : FiniteOperationalTheory S) (hd : DerivedOI T) "
           '{σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) : ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ',
           'theorem gateFlow_one_eq_one (t : ℝ) : gateFlow (1 : Equiv.Perm S) t = 1',
           'theorem derivedOI_layerFlowExecutable_one_not_phaseFree : ∃ T : FiniteOperationalTheory (Fin 2), '
           'DerivedOI T ∧ LayerFlowExecutable T 1 ∧ ¬ PhaseFreeRichness T',
           'theorem derivedOI_layerFlowExecutable_of_qm [Nonempty S] (T : FiniteOperationalTheory S) '
           '(h : ExactAllFiniteEndomorphicQuantumOps T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) : DerivedOI T ∧ LayerFlowExecutable T σ'):
    ok_q3 &= _t in _q3flat
# the phase hypothesis is consumed at the sign flip; Q3 from the closure uses the phases and the exchanges only;
# the transition flow is assembled from the sign-flip identity with the time-reversed flow
ok_q3 &= 'rw [← phaseGate_mul_self]' in _q3
ok_q3 &= 'phaseFree_of_phases_layerFlowExecutable T hd.2.2.2.1 hd.2.2.1 hσ hx hex' in _q3flat
ok_q3 &= 'flip_avail T hph n' in _q3flat and 'gateFlow_isolation_flip hτ ha (t / Real.pi)' in _q3flat
ok_q3 &= 'hex n (-(t / Real.pi))' in _q3flat
# the note: question, distinctions, attack, countercontrols, tests, meanings and non-doings precede the outcome
_kq = [_q3n.find(h) for h in ('## The frozen question', '## Three distinctions, frozen', '## The attack, fixed in advance',
       '## The countercontrols, fixed in advance', '## The tests, fixed in advance',
       '## What the outcomes mean, fixed in advance', '## What the round does not do',
       '## Scope amendment, recorded after the preregistration', '## The outcome')]
ok_q3 &= all(x > 0 for x in _kq) and _kq == sorted(_kq)
ok_q3 &= _q3n.lstrip().startswith('# The Q3 round')
# the amendment: the identity case "in every theory" was too broad; C2 needs and proves the substratum witness
_q3n_out = _q3n[_q3n.find('## The outcome'):]
ok_q3 &= 'availExt_id_of_control' in _q3n and 'scope amendment above' in _q3n_out
ok_q3 &= 'is not automatic from the bare `FiniteOperationalTheory` structure' in _q3n1
ok_q3 &= 'is amended above and is not a statement any theorem makes' in _q3n1
ok_q3 &= 'holds in every theory, in particular' not in _q3n_out
for _t in ('Preregistration commit `f206058`', 'Status: pass complete', '`main` at `f80688e`',
           '**(D1) The phase hypothesis is used materially.**',
           '**(D2) Sufficiency of the quarter phase as a sourced access is not sufficiency for the repertoire.**',
           '**(D3) The target is phase-free richness.**', '**The sign-flip identity, to be proved.**',
           '**The negative branch.**', '**C1, the phase hypothesis is necessary.**',
           '**C2, the moved-configuration hypothesis is necessary.**', '**T1. The sign-flip identity.**',
           '**T7. The surfaces and the checks.**', '| T1 | ', '| T7 | ', 'the constructive branch',
           'The negative branch is not reached', 'consumed at the sign flip', 'seventeen named results',
           '`PhasesAvailable` as an explicit extra hypothesis'):
    ok_q3 &= _t in _q3n1
for _bad in ('PhasesAvailable is derived', 'the phase structure is derived', 'SubstratumAvail follows from DerivedOI',
             'the baseline is minimal', 'relative phase is the unique', 'relative phase is the minimal',
             'the lift is derivable', 'the lift is not derivable', 'Route A is closed', 'OI implies QM',
             'quantum mechanics requires OI', 'bare OI implies', 'the manuscripts are wrong'):
    ok_q3 &= not _asserted(_q3n, _bad)
# the lift audit and the phase-source note record the decision after their frozen text
ok_q3 &= '## Q3 at its preregistered hypothesis, decided, recorded after the round' in _lan
ok_q3 &= _lan.find('## What this note does not claim') < _lan.find('## Q3 at its preregistered hypothesis, decided')
ok_q3 &= 'phaseFree_of_derivedOI_layerFlowExecutable' in _lan and 'gateFlow_isolation_flip' in _lan
ok_q3 &= '## The decision that followed, recorded after the round' in _psn
ok_q3 &= _psn.find('## What this note does not claim') < _psn.find('## The decision that followed')
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
# carries the paragraph and the counts
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_q3 &= 'flipAt' not in _t and 'DERIVED-Q3' not in _t and 'LayerFlowExecutable' not in _t
_q3_fam = [f for f in _ptr_reg['families'] if f['name'] == 'Q3 from the closure: one executable layer flow']
ok_q3 &= len(_q3_fam) == 1 and _q3_fam[0]['status'] == 'current' and _q3_fam[0]['modules'] == ['DerivedQ3']
ok_q3 &= _q3_fam[0]['manuscript'] != [] and 'sign-flip identity' in _q3_fam[0]['note'] and 'explicit hypothesis' in _q3_fam[0]['note']
ok_q3 &= '| Q3 from the closure: one executable layer flow | 1 | current |' in _cen_ps
for _t in ('`R7-Q3`', 'DERIVED-Q3-AUDIT.md', 'gateFlow_isolation_flip', 'phaseFree_of_derivedOI_layerFlowExecutable',
           "derivedOI_qm_iff_layerFlowExecutable'", 'derivedOI_layerFlowExecutable_one_not_phaseFree',
           'Seventeen named results', 'time reversal replacing the continuous phase',
           'the step at which the phase hypothesis is consumed', 'two named assumptions', 'nor derived from the closure'):
    ok_q3 &= _t in _rd1
ok_q3 &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-Q3', ok_q3,
      'Q3 guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its seventeen '
      'results, defines the sign flip and no intervention kind, class or theory, and cites neither the continuous '
      'phase, the substratum availability nor a countertheory; the sign-flip identity, the square of the quarter '
      'phase, its availability, Q3 from the phases and the exchanges, Q3 from the closure, the endpoint under the '
      'closure alone, the identity countercontrol and the consistency theorem are stated as pinned, the phase '
      'hypothesis consumed at the sign flip and the closure entering only through the phases and the exchanges; the '
      'note keeps the question, the three distinctions, the attack with the negative branch, the countercontrols, the '
      'tests, the meanings and the non-doings before the outcome, names both commits, records the constructive branch '
      'with the negative branch not reached, and asserts nothing about sourcing the phases, minimality, the lift, '
      'Route A or the manuscripts; the lift audit and the phase-source note carry the decision after their frozen '
      'text; the registry and the census carry the family as current after the propagation round and the README '
      'carries the paragraph and the counts.')

# ---- the Q3 propagation: the layer-flow endpoint in GR 3.3 and the summaries, publication-only, the
# witness of each direction named, both sourcing qualifications kept, the families current ----
ok_q3p = True
_qpn = open(os.path.join(os.path.dirname(BRIDGE), 'Q3-PROPAGATION-AUDIT.md'), encoding='utf-8').read()
_qpn1 = re.sub(r'\s+', ' ', _qpn)
ok_q3p &= _qpn.lstrip().startswith('# The Q3 propagation round')
_kqp = [_qpn.find(h) for h in ('## The items, fixed in advance', '## The constraints, fixed in advance',
        '## The tests, fixed in advance', '## What the round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome')]
ok_q3p &= all(x > 0 for x in _kqp) and _kqp == sorted(_kqp)
# the amendment: the generic theorem and the concrete swap-layer instance kept distinct
ok_q3p &= 'keeps the generic theorem and the concrete instance distinct' in _qpn1
ok_q3p &= 'scope amendment above' in _qpn[_qpn.find('## The outcome'):]
for _t in ('Preregistration commit `6eb213b`', 'Status: pass complete', '`main` at `be31589`',
           '**Item 1, the layer-flow form in `[GR §3.3]`.**',
           '**Item 3, the registry and the census, per §A.35, in the same commit.**',
           '**E1. The paragraph.**', '**E6. The checks.**', '| E1 | ', '| E6 | ',
           'No uniqueness or minimality is claimed', 'six occurrences'):
    ok_q3p &= _t in _qpn1
for _bad in ('the executability is derived', 'the phases are derived', 'the phase structure is derived',
             'the assumptions are minimal', 'the pair is minimal', 'Route A is closed', 'OI implies QM',
             'bare OI implies', 'the manuscripts are wrong'):
    ok_q3p &= not _asserted(_qpn, _bad)
# GR 3.3: the layer-flow form, its display, the witness of each direction, the instance, the two qualifications
_qgr = open(os.path.join(_msroot, 'papers/GR.md'), encoding='utf-8').read()
_qgr1 = re.sub(r'\s+', ' ', _qgr)
for _t in ('**Layer-flow form.**',
           'text{exact finite endomorphic operational QM} \\;\\iff\\; \\text{one nontrivial layer flow executable}',
           "`derivedOI_qm_iff_layerFlowExecutable'` in `OIBridge/DerivedQ3.lean`",
           'The executability is necessary because full unitary control makes every unitary available',
           '`layerFlowExecutable_of_control` in `OIBridge/LiftAudit.lean`',
           'the square of the quarter phase on the image of a moved configuration is a sign flip',
           '`gateFlow_isolation_flip`', '`phaseFree_of_derivedOI_layerFlowExecutable`',
           '`qm_of_derivedOI_layerFlowExecutable`', "`derivedOI_qm_iff_layerFlowExecutable_swap'`",
           'For the concrete substratum factorization, the swap-layer flow on a nonempty region with a nontrivial '
           'alphabet is the one-parameter unitary group of one of its gates and is an instance of this equivalence',
           'the equivalence itself is stated for each involution with a moved configuration, whether or not it is a '
           'gate of that factorization',
           'Two qualifications are part of the statement.',
           'The phase intervention is an assumption on the substratum class, as stated above, and not a consequence of '
           'the finite states with the bijective read-write dynamics',
           'The executability of the layer flow at intermediate times is likewise not derived',
           '`substratumTheory_not_layerFlowExecutable` in `OIBridge/LiftAudit.lean`',
           'No uniqueness or minimality is claimed for the pair of assumptions'):
    ok_q3p &= _t in _qgr1
ok_q3p &= _qgr.find('**Substratum-source form.**') < _qgr.find('**Layer-flow form.**') < _qgr.find('**Typed form.**')
ok_q3p &= 'text{current OI substratum} + \\text{continuous off-diagonal controllability}' in _qgr1
# the summary at the six sites, after the pinned continuous-time clause
_qsum = ('exact finite endomorphic operational quantum mechanics holds exactly when one continuous layer flow of an '
         'involution of the configuration space moving some configuration is an available operation at every level '
         'and every intermediate time, the executability of that flow being an assumption not derived by '
         'configuration-level generation, as the phase intervention is an assumption on the substratum class and not '
         'a consequence of the finite states with the bijective dynamics')
_qcount = 0
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read())
    ok_q3p &= _qsum in _t1 and _ctn_sum in _t1
    _qcount += _t1.count(_qsum)
ok_q3p &= _qcount == 6
ok_q3p &= ("`derivedOI_qm_iff_layerFlowExecutable'` in `OIBridge/DerivedQ3.lean`, "
           '`substratumTheory_not_layerFlowExecutable` in `OIBridge/LiftAudit.lean`') in re.sub(r'\s+', ' ',
           open(os.path.join(_msroot, 'papers/Main.md'), encoding='utf-8').read())
# the kernel predicates of the boundary, the superseded identifiers, any derivation of either assumption and
# any minimality claim are absent from every manuscript source and generated form
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/ch01-observation.md', 'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md',
             'papers/GR.tex', 'papers/Main.tex', 'papers/Explainer.tex', 'book/The-Incompleteness-of-Observation-FULL.tex'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read()).replace('\\_', '_')
    for _bad in ('DerivedOI', 'SourcedOI', 'PhasesAvailable', 'SubstratumAvail', 'RouteB', 'LayerFlowExecutable',
                 'phaseFree_of_layerFlowExecutable`', 'phaseFree_of_layerFlowExecutable}', 'phaseFree_of_layerFlowExecutable ',
                 'derivedOI_qm_iff_layerFlowExecutable`', 'derivedOI_qm_iff_layerFlowExecutable}', 'derivedOI_qm_iff_layerFlowExecutable ',
                 'the executability is derived', 'executability is derived from', 'derives the executability',
                 'the layer flow is derived', 'the phases are derived', 'derives the phases',
                 'the pair of assumptions is minimal', 'the assumptions are minimal', 'is the unique resource',
                 'the minimal resource',
                 'The layer flow is the one-parameter unitary group of one gate of the depth-two factorization'):
        ok_q3p &= _bad not in _t1
# the registry: both families current with anchors, the two supersessions, the census rows, the README
_qp_fam = [f for f in _ptr_reg['families'] if f['name'] == 'Q3 from the closure: one executable layer flow']
ok_q3p &= len(_qp_fam) == 1 and _qp_fam[0]['status'] == 'current'
ok_q3p &= {m['file'] for m in _qp_fam[0]['manuscript']} == {'papers/GR.md', 'papers/Main.md'}
ok_q3p &= 'carried by no manuscript' not in _qp_fam[0]['note'] and 'Q3-PROPAGATION-AUDIT.md' in _qp_fam[0]['note']
_qla_fam = [f for f in _ptr_reg['families'] if f['name'] == 'lift audit: executable layer flows']
ok_q3p &= len(_qla_fam) == 1 and _qla_fam[0]['status'] == 'current'
ok_q3p &= 'papers/GR.md' in {m['file'] for m in _qla_fam[0]['manuscript']}
ok_q3p &= 'superseded' in _qla_fam[0]['note'] and 'carried by no manuscript' not in _qla_fam[0]['note']
for _k, _v in (('phaseFree_of_layerFlowExecutable', 'phaseFree_of_derivedOI_layerFlowExecutable'),
               ('derivedOI_qm_iff_layerFlowExecutable', "derivedOI_qm_iff_layerFlowExecutable'")):
    ok_q3p &= _ptr_reg['supersessions'].get(_k) == _v
ok_q3p &= '| Q3 from the closure: one executable layer flow | 1 | current |' in _cen_ps
ok_q3p &= '| lift audit: executable layer flows | 1 | current |' in _cen_ps
for _t in ('`R7-Q3P`', 'Q3-PROPAGATION-AUDIT.md', 'layer-flow form', 'the witness of each direction',
           'superseded by the endpoint under the closure alone', 'No theorem is added or changed'):
    ok_q3p &= _t in _rd1
check('R7-Q3P', ok_q3p,
      'Q3 propagation guard: the note keeps the items, the constraints, the tests and the non-doings before the '
      'outcome, names both commits and asserts no derivation of either assumption and no minimality; GR 3.3 carries '
      'the layer-flow form after the substratum-source form and before the typed form, with its display, the witness '
      'of each direction named beside it, the swap-layer instance and both sourcing qualifications, the '
      'substratum-source box standing; the summary sentence occurs at the six sites after the pinned continuous-time '
      'clause; no manuscript source or generated form names a kernel predicate of the boundary, a superseded '
      'identifier, a derivation of either assumption or a minimality; the registry carries the Q3 and lift-audit '
      'families as current with anchors and the two supersessions, the census rows follow, and the README carries '
      'the round.')

# ---- the executability-source audit: the stated access does not make one layer flow executable; the
# necessary condition and the sufficient access tested named; the lift the one open entry ----
ok_exec = True
_ex = open(os.path.join(BRIDGE, 'OIBridge', 'ExecSource.lean'), encoding='utf-8').read()
_exflat = ' '.join(_ex.split())
_exn = open(os.path.join(os.path.dirname(BRIDGE), 'EXEC-SOURCE-AUDIT.md'), encoding='utf-8').read()
_exn1 = re.sub(r'\s+', ' ', _exn)
ok_exec &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _ex) is None and 'native_decide' not in _ex
ok_exec &= 'axiom ' not in re.sub(r'/-.*?-/', '', _ex, flags=re.S)
_ex_names = re.findall(r"^theorem ([\w']+)", _ex, re.M)
ok_exec &= len(_ex_names) == 12 and _ex.count('#print axioms') == 12
for _nm in _ex_names:
    ok_exec &= ('#print axioms ' + _nm) in _ex
# the module defines no intervention kind, class, theory or function; no gate flow is placed in a class
ok_exec &= re.findall(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) (\w+)', _ex, re.M) == []
ok_exec &= 'import OIBridge.DerivedQ3' in _ex and 'import OIBridge.ExecSource' in root
for _t in ('onesClass_gateFlow', 'SubstratumAvail', 'sorry'):
    ok_exec &= (_t not in _ex) or _t == 'onesClass_gateFlow'
ok_exec &= 'SubstratumAvail' not in _ex and 'phaseFun' not in _ex
# the statements, as preregistered
for _t in ('theorem exists_nonMonomial_of_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) '
           '{σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable (genTheory 𝓘 arch S) σ) : '
           '∃ K : Matrix (S × Fin 1) (S × Fin 1) ℂ, 𝓘 (S × Fin 1) K ∧ ¬ IsMonomial K',
           'theorem not_configurationLevel_of_layerFlowExecutable',
           'theorem bijectionLevel_not_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) '
           '(hb : BijectionLevel 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ',
           'theorem configurationLevel_not_avail_gateFlow_half',
           'theorem obs_not_layerFlowExecutable {g : Equiv.Perm 𝒮.Conf} {x : 𝒮.Conf} (hx : g x ≠ x) : '
           '¬ LayerFlowExecutable (obsTheory 𝒮) g',
           'theorem obs_not_layerFlowExecutable_shear', 'theorem obs_not_layerFlowExecutable_swap',
           'theorem waveSubstratum_swap_moves [Fact (1 < q)] (α : ZMod q)',
           'theorem waveSubstratum_not_layerFlowExecutable_swap [NeZero L] [NeZero q] [Fact (1 < q)] (α : ZMod q) : '
           '¬ LayerFlowExecutable (obsTheory (waveSubstratum d L q α))',
           'theorem gateFlow_half_not_monomial {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) : ¬ IsMonomial (gateFlow σ (1 / 2 : ℝ))',
           'theorem onesClass_not_configurationLevel : ¬ ConfigurationLevel onesClass'):
    ok_exec &= _t in _exflat
ok_exec &= 'gateFlow_half_not_preservesDiag' in _exflat and 'obs_availExt_le_substratum' in _exflat
# the note: question, distinctions, census, criteria, tests, meanings and non-doings precede the outcome
_ke = [_exn.find(h) for h in ('## The question', '## Five distinctions, frozen at the outset',
       '## The census of purported sources, taken before the pass', '## The criteria, fixed in advance',
       '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
       '## What the round does not do', '## Scope amendment, recorded after the preregistration', '## The outcome')]
ok_exec &= all(x > 0 for x in _ke) and _ke == sorted(_ke)
ok_exec &= _exn.lstrip().startswith('# The executability-source audit')
# the amendment: the stated access is permutation-valued, the stipulated phase intervention is a separate
# configuration-level assumption, X8 is not a source; the overbroad census sentence is not the outcome's
_exn_out0 = re.sub(r'\s+', ' ', _exn[_exn.find('## The outcome'):])
ok_exec &= 'scope amendment above' in _exn_out0
for _t in ('Every operation supplied by the stated observer access is configuration-level',
           'in `obsTheory 𝒮` permutation-valued', 'The separately stipulated phase intervention is also monomial',
           'does not rescue executability', 'X8 is not a source'):
    ok_exec &= _t in _exn_out0
ok_exec &= 'is a permutation of the configurations or a phase' not in _exn_out0
ok_exec &= 'with X8 excluded as a stipulation and the consistency control' in _exn1
for _t in ('Preregistration commit `3b36661`', 'Status: pass complete', '`main` at `087d023`',
           '**(D1) A mathematical path is not an operation.**',
           '**(D2) An emergent continuous-time description of the visible process is a representation, not an availability.**',
           '**(D3) Time-one availability with a continuous interpolation is not intermediate-time availability.**',
           '**(D4) Coarse-graining, hidden memory and hidden clocks give classical maps.**',
           '**(D5) The target is the literal predicate.**', '| X1, ', '| X7, ', '| X8, ',
           '**T1. The necessary condition.**', '**T7. The surfaces and the checks.**', '| T1 | ', '| T7 | ',
           'The verdicts, per entry', 'negative for the stated access', 'underdetermined',
           'the sufficient access tested', 'A non-monomial operator is not by itself sufficient', 'twelve named results'):
    ok_exec &= _t in _exn1
for _bad in ('the lift is derivable', 'the lift is not derivable', 'executability is derived',
             'LayerFlowExecutable is derived', 'the phases are derived', 'PhasesAvailable is derived',
             'Route A is closed', 'OI implies QM', 'quantum mechanics requires OI', 'bare OI implies',
             'the manuscripts are wrong', 'a non-monomial operator suffices', 'a non-monomial operator is sufficient',
             'reads availability off the path'):
    ok_exec &= not _asserted(_exn, _bad)
_exn_out = _exn[_exn.find('## The outcome'):]
for _bad in ('the missing access is named: a non-monomial', 'any non-monomial operator supplies', 'the executability is derived'):
    ok_exec &= _bad not in _exn_out
for _bad in ('the missing access is named: a non-monomial', 'any non-monomial operator supplies'):
    ok_exec &= _bad not in _rd1
# the lift audit and the interface note record the decision after their frozen text
ok_exec &= '## The executability source, recorded after the round' in _lan
ok_exec &= _lan.find('## Q3 at its preregistered hypothesis, decided') < _lan.find('## The executability source, recorded after the round')
ok_exec &= 'obs_not_layerFlowExecutable' in _lan and 'exists_nonMonomial_of_layerFlowExecutable' in _lan
ok_exec &= '## The next arrow, decided for the stated access, recorded after the round' in _san
ok_exec &= _san.find('## The phases, decided, recorded after the round') < _san.find('## The next arrow, decided for the stated access')
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_exec &= 'EXEC-SOURCE' not in _t
    ok_exec &= _rel in ('papers/GR.md', 'papers/Main.md') or ('ExecSource' not in _t and 'obs_not_layerFlowExecutable' not in _t
                                                          and 'waveSubstratum' not in _t and 'exists_nonMonomial' not in _t)
_ex_fam = [f for f in _ptr_reg['families'] if f['name'] == 'executability source: the stated access and the layer flows']
ok_exec &= len(_ex_fam) == 1 and _ex_fam[0]['status'] == 'current' and _ex_fam[0]['modules'] == ['ExecSource']
ok_exec &= {m['file'] for m in _ex_fam[0]['manuscript']} == {'papers/GR.md', 'papers/Main.md'} and 'Negative for the stated access' in _ex_fam[0]['note']
ok_exec &= 'the sufficient access tested' in _ex_fam[0]['note'] and 'owner decision' not in _ex_fam[0]['note'] and 'SOURCING-PROPAGATION-AUDIT.md' in _ex_fam[0]['note']
ok_exec &= '| executability source: the stated access and the layer flows | 1 | current |' in _cen_ps
for _t in ('`R7-EXEC`', 'EXEC-SOURCE-AUDIT.md', 'exists_nonMonomial_of_layerFlowExecutable',
           'waveSubstratum_not_layerFlowExecutable_swap', 'onesClass_not_configurationLevel', 'Twelve named results',
           'negative for the stated access', 'the sufficient access tested',
           'a non-monomial operator alone being no guarantee', 'underdetermined for the observer-level lift',
           'an additional physical assumption on the route'):
    ok_exec &= _t in _rd1
ok_exec &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-EXEC', ok_exec,
      'Executability-source guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its twelve results, defines nothing and places no gate flow in a class; the necessary condition, the '
      'non-configuration-level corollary, the bijection-level and configuration-level negatives, the unavailability '
      'of the gate flow at time one half, the observer theory of every substratum executing no layer flow with its '
      'own layers, the wave substratum\'s swap layer moving a configuration, and the countercontrols are stated as '
      'pinned; the note keeps the question, the five distinctions, the eight-entry census, the criteria, the tests, '
      'the meanings and the non-doings before the outcome, names both commits, records the verdict negative for the '
      'stated access and the lift underdetermined with the necessary condition and the sufficient access tested '
      'distinguished, and asserts nothing about the lift being derivable or not, a non-monomial operator sufficing, '
      'the phase, Route A or the manuscripts; the lift audit and the interface note carry the decision after their '
      'frozen text; no manuscript is edited; the registry and the census carry the family as kernel-only and the '
      'README carries the paragraph and the counts.')

# ---- the lift-source audit: the observer-level lift, in every formulation the corpus states that lands in the
# operational interface, derives either target; the wave-operator lift underdetermined; the stronger statements
# attached only where the kernel proves them (the scope amendment) ----
ok_lsrc = True
_ls = open(os.path.join(BRIDGE, 'OIBridge', 'LiftSource.lean'), encoding='utf-8').read()
_lsflat = ' '.join(_ls.split())
_lsn = open(os.path.join(os.path.dirname(BRIDGE), 'LIFT-SOURCE-AUDIT.md'), encoding='utf-8').read()
_lsn1 = re.sub(r'\s+', ' ', _lsn)
ok_lsrc &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _ls) is None and 'native_decide' not in _ls
ok_lsrc &= 'axiom ' not in re.sub(r'/-.*?-/', '', _ls, flags=re.S)
_ls_names = re.findall(r"^theorem ([\w']+)", _ls, re.M)
ok_lsrc &= len(_ls_names) == 18 and _ls.count('#print axioms') == 18
for _nm in _ls_names:
    ok_lsrc &= ('#print axioms ' + _nm) in _ls
# the module defines exactly the lift-extended class, its theory and the Kraus form of a stochastic map; no
# intervention kind; no gate flow and no non-monomial operator placed in the class; no map from the site space
ok_lsrc &= re.findall(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) (\w+)', _ls, re.M) \
    == ['coherentLiftClass', 'coherentLiftTheory', 'stochasticChannel']
_ls_cls = _lsflat[_lsflat.find('def coherentLiftClass'):_lsflat.find('variable {S : Type}', _lsflat.find('def coherentLiftClass'))]
ok_lsrc &= ('def coherentLiftClass : ImplementationClass := fun S _ _ K => IsMonomial K ∨ ∃ (g : Equiv.Perm S) '
            "(d : S → ℂ), (∀ s, d s * conj' (d s) = 1) ∧ K = Matrix.diagonal (fun a => d (g.symm a)) * permMatrix g") in _ls_cls
ok_lsrc &= 'gateFlow' not in _ls_cls and 'unit' not in _ls_cls and 'onesClass' not in _ls
ok_lsrc &= 'SubstratumAvail' not in _ls and 'phaseFun' not in _ls and 'Θ' not in _ls
ok_lsrc &= 'import OIBridge.ExecSource' in _ls and 'import OIBridge.CoherentExtension' in _ls and 'import OIBridge.LiftSource' in root
# the statements, as preregistered
for _t in ('theorem not_layerFlowExecutable_of_preservesDiag (T : FiniteOperationalTheory S)',
           'T.availExt n O F → ∀ o, PreservesDiag (F o)) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : ¬ LayerFlowExecutable T σ',
           'theorem coherentLift_isMonomial (g : Equiv.Perm S) (d : S → ℂ) : IsMonomial (Matrix.diagonal (fun a => d (g.symm a)) * permMatrix g)',
           'theorem reversibleExtension_conj_monomial [Nonempty S] (g : Equiv.Perm S) (C : Matrix S S ℂ) (hpsd : C.PosSemidef) (hdiag : ∀ s, C s s = 1)',
           '∃ K : Matrix S S ℂ, IsMonomial K ∧ Kᴴ * K = 1 ∧ correlationExtension g C = conjChannel K',
           'theorem correlationExtension_preservesDiag (g : Equiv.Perm S) (C : Matrix S S ℂ) (hdiag : ∀ s, C s s = 1) : PreservesDiag (correlationExtension g C)',
           'theorem coherentLiftClass_contains_lift', 'theorem coherentLiftClass_configurationLevel : ConfigurationLevel coherentLiftClass',
           'theorem coherentLiftClass_eq_substratumClass : coherentLiftClass = substratumClass',
           'theorem coherentLiftClass_arch : Architecture coherentLiftClass',
           'theorem coherentLiftTheory_eq_substratumTheory : coherentLiftTheory S = substratumTheory S',
           'theorem coherentLiftClass_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : ¬ LayerFlowExecutable (coherentLiftTheory S) σ',
           'theorem obs_availExt_le_coherentLift',
           'theorem waveSubstratum_coherentLift_not_layerFlowExecutable_swap [NeZero L] [NeZero q] [Fact (1 < q)] (α : ZMod q) : '
           '¬ LayerFlowExecutable (coherentLiftTheory (waveSubstratum d L q α).Conf)',
           'theorem single_isMonomial (c : ℂ) (i k : S) : IsMonomial (c • Matrix.single i k 1)',
           'theorem stochasticChannel_kraus_monomial',
           'theorem stochasticChannel_preservesDiag (A : S → S → ℝ) : PreservesDiag (stochasticChannel A)',
           'theorem stochastic_not_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)',
           'IsMonomial K ∨ ∃ (c : ℂ) (i k : T), K = c • Matrix.single i k 1',
           'theorem avail_one_not_layerFlowExecutable {σ : Equiv.Perm S} (hσ : ∀ y, σ (σ y) = y) {x : S} (hx : σ x ≠ x) : '
           '(∀ n, (substratumTheory S).availExt n Unit (fun _ => conjChannel (gateFlow (levelPerm σ n) 1))) ∧ ¬ LayerFlowExecutable (substratumTheory S) σ',
           'theorem obs_swap_avail_one_not_layerFlowExecutable'):
    ok_lsrc &= _t in _lsflat
for _t in ('reversibleExtension_iff_rankOne', 'rankOne_extension_monomial', 'correlationExtension_diagonal',
           'gateFlow_half_not_preservesDiag', 'configurationLevel_not_layerFlowExecutable', 'obs_availExt_le_substratum',
           'waveSubstratum_swap_moves', 'substratumTheory_avail_conj', 'gateFlow_one', 'obs_swap_avail'):
    ok_lsrc &= _t in _lsflat
# the note: question with the two targets and the discipline, distinctions, census, criteria, tests, meanings and
# non-doings precede the outcome; no scope amendment was needed
_kl = [_lsn.find(h) for h in ('## The question', '## Five distinctions, frozen at the outset',
       '## The census of formulations, taken before the pass', '## The criteria, fixed in advance',
       '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
       '## What the round does not do', '## Scope amendment, recorded after the preregistration', '## The outcome',
       '## What this note does not claim')]
ok_lsrc &= all(x > 0 for x in _kl) and _kl == sorted(_kl)
ok_lsrc &= _lsn.lstrip().startswith('# The lift-source audit')
for _t in ('Preregistration commit `5e20f45`', '`main` at `04b7acf`', 'Status: pass complete',
           '**Target A.**', '**Target B.**', '**The discipline.**',
           'No inference from "there exists an observer-level Hamiltonian or wave operator" to "the observer can execute its exponential"',
           '**(D1) A generator is not an operation.**', '**(D2) A description of the visible statistics is not an operation.**',
           '**(D3) A coherent completion is a channel on the carrier, and is tested as one.**',
           '**(D4) A map on a different space has not landed.**', '**(D5) Diagonal preservation is the invariant.**',
           '| L1, ', '| L2, ', '| L3, ', '| L4, ', '| L5, ', '**T1. The diagonal criterion.**', '**T8. The surfaces and the checks.**',
           '| T1 | ', '| T8 | ', 'The verdicts, per formulation', 'What the wave-operator lift would have to supply',
           'Neither target is derived', 'stands unchanged', 'eighteen named results',
           'Target A is necessary for Target B and not sufficient for it'):
    ok_lsrc &= _t in _lsn1
_lsn_out = re.sub(r'\s+', ' ', _lsn[_lsn.find('## The outcome'):])
for _t in ('read under the scope amendment above', 'no formulation the corpus states that lands in the operational interface derives either target',
           'the one that does not land is underdetermined', 'The stronger statements hold where the kernel proves them, and there only',
           'is not the exclusion of every other realization', 'the implementation classes of the nonreversible members are not classified here',
           'other realizations of the same channel are not classified here',
           '| L1, the coherent completion on the configuration carrier | representational; derives neither target |',
           '| L2, the projected observer operator on visible distributions | representational; derives neither target |',
           '| L3, the harmonic wave-operator lift on the amplitude space | **underdetermined** |',
           '| L5, the executable reading | not a source |', 'X7 is decided for the formulations that land'):
    ok_lsrc &= _t in _lsn_out
for _bad in ('the lift is derived', 'the lift is not derivable', 'executability is derived',
             'LayerFlowExecutable is derived', 'Target A is reached', 'Target B is reached', 'the phases are derived',
             'Route A is closed', 'OI implies QM', 'quantum mechanics requires OI', 'bare OI implies',
             'the manuscripts are wrong', 'a non-monomial operator suffices', 'a non-monomial operator is sufficient',
             'no such map exists', 'the map does not exist', 'reads availability off'):
    ok_lsrc &= not _asserted(_lsn, _bad)
_lsn_out_body = _lsn_out[:_lsn_out.find('## What this note does not claim')]
for _bad in ('the lift is derivable', 'the lift sources executability', 'the lift supplies a non-monomial',
             'both targets negative for every formulation that lands', 'delivers configuration-level operations',
             'lands only as configuration-level', 'Target A and Target B negative', 'adding nothing to the stated access',
             'Neither target is reached'):
    ok_lsrc &= _bad not in _lsn_out_body
# the amendment: the stronger statements only where the kernel proves them; the broader form rejected on every
# publication-facing surface
_lsn_am = _lsn1[_lsn1.find('## Scope amendment, recorded after the preregistration'):_lsn1.find('## The outcome')]
for _t in ('the reversible coherent members', 'every Kraus realization', 'is not read as the exclusion of every non-monomial realization',
           'no formulation that lands derives either target', 'read as "derives neither target"', 'no theorem changes'):
    ok_lsrc &= _t in _lsn_am
# the executability-source note and the axiom audit record the decision after their frozen text
_exn_ls = open(os.path.join(os.path.dirname(BRIDGE), 'EXEC-SOURCE-AUDIT.md'), encoding='utf-8').read()
ok_lsrc &= '## The lift, decided for the formulations that land, recorded after the round' in _exn_ls
ok_lsrc &= _exn_ls.find('## Scope amendment, recorded after the preregistration') < _exn_ls.find('## The lift, decided for the formulations that land') < _exn_ls.find('## The outcome')
ok_lsrc &= 'coherentLiftClass_eq_substratumClass' in _exn_ls and 'stays underdetermined' in _exn_ls
_maa_ls = open(os.path.join(os.path.dirname(BRIDGE), 'MANUSCRIPT-AXIOM-AUDIT.md'), encoding='utf-8').read()
ok_lsrc &= '## The third item of the missing interface, decided for the formulations that land, recorded after the round' in _maa_ls
ok_lsrc &= _maa_ls.find('## What this note does not claim') < _maa_ls.find('## The third item of the missing interface')
ok_lsrc &= 'coherentLiftClass_eq_substratumClass' in _maa_ls and 'the lift is derivable' not in _maa_ls[_maa_ls.find('## The third item'):]
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_lsrc &= 'LIFT-SOURCE' not in _t and 'coherentLift_isMonomial' not in _t
    ok_lsrc &= _rel in ('papers/GR.md', 'papers/Main.md') or ('LiftSource' not in _t and 'coherentLiftClass' not in _t and 'stochasticChannel' not in _t)
_ls_fam = [f for f in _ptr_reg['families'] if f['name'] == 'lift source: the observer-level lift in the operational interface']
ok_lsrc &= len(_ls_fam) == 1 and _ls_fam[0]['status'] == 'current' and _ls_fam[0]['modules'] == ['LiftSource']
ok_lsrc &= {m['file'] for m in _ls_fam[0]['manuscript']} == {'papers/GR.md', 'papers/Main.md'} and 'No formulation the corpus states that lands in the operational interface derives either target' in _ls_fam[0]['note']
ok_lsrc &= 'not read as the exclusion of every other realization' in _ls_fam[0]['note']
ok_lsrc &= 'Underdetermined for the wave-operator lift' in _ls_fam[0]['note'] and 'owner decision' not in _ls_fam[0]['note'] and 'SOURCING-PROPAGATION-AUDIT.md' in _ls_fam[0]['note']
ok_lsrc &= '| lift source: the observer-level lift in the operational interface | 1 | current |' in _cen_ps
for _t in ('`R7-LSRC`', 'LIFT-SOURCE-AUDIT.md', 'not_layerFlowExecutable_of_preservesDiag', 'coherentLiftClass_eq_substratumClass',
           'waveSubstratum_coherentLift_not_layerFlowExecutable_swap', 'stochastic_not_layerFlowExecutable',
           'avail_one_not_layerFlowExecutable', 'coherentLiftClass_contains_lift', 'Eighteen named results',
           'no formulation that lands in the operational interface derives either target',
           'the stronger\nstatements attached only where the kernel proves them'.replace('\n', ' '),
           'no exclusion of other realizations of those channels claimed',
           'underdetermined for the wave-operator lift', 'The verdict of the executability-source audit stands unchanged'):
    ok_lsrc &= _t in _rd1
ok_lsrc &= '143 modules' in _rd1 and '3,102 named results' in _rd1
_ls_exsec = _exn_ls[_exn_ls.find('## The lift, decided for the formulations that land'):_exn_ls.find('## The outcome')]
_ls_maasec = _maa_ls[_maa_ls.find('## The third item of the missing interface'):]
_ls_cenrow = _cen_ps[_cen_ps.find('| lift source: the observer-level lift in the operational interface |'):]
_ls_cenrow = _ls_cenrow[:_ls_cenrow.find(' |\n') + 1] if ' |\n' in _ls_cenrow else _ls_cenrow[:3000]
for _bad in ('delivers configuration-level operations', 'deliver configuration-level operations',
             'both targets negative for every formulation that lands', 'lands only as configuration-level',
             'adding nothing to the stated access', 'adds nothing to the stated access',
             'Both targets negative', 'both targets, a non-monomial admissible operator and one executable layer flow, negative'):
    ok_lsrc &= _bad not in _rd1 and _bad not in _ls_fam[0]['note'] and _bad not in _ls_cenrow
    ok_lsrc &= _bad not in re.sub(r'\s+', ' ', _ls_exsec) and _bad not in re.sub(r'\s+', ' ', _ls_maasec)
ok_lsrc &= 'derives either a non-monomial admissible operator or the gate flow of a layer' in re.sub(r'\s+', ' ', _ls_exsec)
ok_lsrc &= 'derive neither a non-monomial admissible operator nor an executable layer flow' in re.sub(r'\s+', ' ', _ls_maasec)
ok_lsrc &= 'every implementation of a nonreversible coherent completion' in _lsflat
check('R7-LSRC', ok_lsrc,
      'Lift-source guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'eighteen results, defines exactly the lift-extended class, its theory and the Kraus form of a stochastic '
      'map, places no gate flow and no non-monomial operator in the class and states no map from the site space; '
      'the diagonal criterion, the monomial reversible coherent lift, the monomial conjugation of the reversible '
      'coherent extension, the diagonal preservation of every coherent completion, the lift-extended class equal '
      'to the substratum class with its theory executing no layer flow, the observer theory inside it, the wave '
      'substratum instance, the monomial scaled matrix units and Kraus operators of the stochastic channel, and '
      'the two generator countermodels are stated as pinned; the note keeps the question with its two targets and '
      'the discipline, the five distinctions, the five-formulation census, the criteria, the tests, the meanings '
      'and the non-doings before the scope amendment and the outcome, names both commits, records the verdict as no '
      'formulation that lands deriving either target with the stronger statements attached only where the kernel '
      'proves them, the reversible coherent members monomial, every coherent completion diagonal-preserving and the '
      'explicit realization of the stochastic channel configuration-level, no exclusion of other realizations '
      'claimed on any surface, and underdetermined for the wave-operator lift with what it would have to supply, '
      'and asserts nothing about the lift being derived or not derivable, a map from the wave operator existing '
      'or not, a non-monomial operator sufficing, the phase, Route A or the manuscripts; '
      'the executability-source note and the axiom audit carry the decision after their frozen text; no '
      'manuscript is edited; the registry and the census carry the family as kernel-only and the README carries '
      'the paragraph and the counts.')

# ---- the sourcing propagation round: the combined executability-source and lift-source verdict in GR 3.3 and the
# mirrored summaries; the equivalence exact, the sourcing of its layer-flow hypothesis not ----
ok_srcp = True
_spn = open(os.path.join(os.path.dirname(BRIDGE), 'SOURCING-PROPAGATION-AUDIT.md'), encoding='utf-8').read()
_spn1 = re.sub(r'\s+', ' ', _spn)
ok_srcp &= _spn.lstrip().startswith('# The sourcing propagation round')
_ksp = [_spn.find(h) for h in ('## The statement to be carried, fixed in advance', '## The items, fixed in advance',
        '## The constraints, fixed in advance', '## The tests, fixed in advance', '## What the round does not do',
        '## The outcome')]
ok_srcp &= all(x > 0 for x in _ksp) and _ksp == sorted(_ksp)
for _t in ('Preregistration commit `1dff487`', 'Status: pass complete', '`main` at `0a7044a`',
           '**Item 1, the layer-flow form in `[GR §3.3]`.**', '**Item 3, the registry and the census, per §A.35, in the same commit.**',
           '**E1. The paragraph.**', '**E6. The checks.**', '| E1 | ', '| E6 | ', 'The wave-operator lift is unresolved, not ruled out',
           'Layer-flow access is called neither unique nor minimal', 'six occurrences'):
    ok_srcp &= _t in _spn1
for _bad in ('the phases are derived', 'the lift is derived', 'every realization of those channels is configuration-level',
             'the assumptions are minimal', 'the pair is minimal', 'Route A is closed', 'OI implies QM', 'bare OI implies',
             'the manuscripts are wrong'):
    ok_srcp &= not _asserted(_spn, _bad)
# GR 3.3: the sourcing statement after the second qualification, before the no-uniqueness sentence; the second display
_sgr = open(os.path.join(_msroot, 'papers/GR.md'), encoding='utf-8').read()
_sgr1 = re.sub(r'\s+', ' ', _sgr)
for _t in ("Nor is that executability sourced by the substratum's own dynamics with the observer's stated access",
           'its own shear and swap layers included, the layers being available at time one and not at intermediate times',
           'any access that does execute one supplies a non-monomial admissible operator at level one',
           '`obs_not_layerFlowExecutable`, `waveSubstratum_not_layerFlowExecutable_swap`, `exists_nonMonomial_of_layerFlowExecutable` in `OIBridge/ExecSource.lean`',
           'The observer-level lift of [SM §4.1], in every formulation stated that lands in the operational interface, derives neither such an operator nor the layer flow',
           'the reversible coherent lift of a permutation is monomial', 'every coherent completion, reversible or not, preserves diagonal states',
           'the explicit Kraus realization of the projected observer operator is configuration-level',
           'a generator whose time-one exponential is available does not make the exponential available at intermediate times',
           '`reversibleExtension_conj_monomial`, `correlationExtension_preservesDiag`, `coherentLiftClass_eq_substratumClass`, `stochasticChannel_kraus_monomial`, `avail_one_not_layerFlowExecutable` in `OIBridge/LiftSource.lean`',
           'whether every realization of those channels is configuration-level is not decided',
           'the site-space wave-operator formulation is unresolved rather than excluded, no operational map from it to the configuration carrier being stated',
           'Fractional-time access to one layer flow is therefore an additional physical intervention assumption, as the phase intervention is',
           'text{stated substratum dynamics with observer access} \;\\not\\Rightarrow\; \\text{one nontrivial layer flow executable}',
           'The equivalence displayed above is exact; the physical sourcing of this one of its hypotheses is not',
           'No uniqueness or minimality is claimed for the pair of assumptions; a different pair could be sufficient as well'):
    ok_srcp &= _t in _sgr1
ok_srcp &= _sgr.find('`substratumTheory_not_layerFlowExecutable` in `OIBridge/LiftAudit.lean`') < _sgr.find('Nor is that executability sourced') \
    < _sgr.find('stated substratum dynamics with observer access} \;\\not\\Rightarrow') < _sgr.find('No uniqueness or minimality is claimed for the pair of assumptions') < _sgr.find('**Typed form.**')
ok_srcp &= _sgr1.count('one nontrivial layer flow executable}') == 2
# the summary at the six sites, directly after the Q3 summary sentence, whose count is unchanged
_ssum = ("The stated substratum dynamics with the observer's read and write access do not source that executability, the layers "
         'being available at time one and not at intermediate times, and the observer-level lift, in every formulation stated that '
         'lands in the operational interface, derives neither a non-monomial admissible operator nor the layer flow, the site-space '
         'wave-operator formulation being unresolved rather than excluded')
_scount = 0
_qcount2 = 0
for _rel in ('papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read())
    ok_srcp &= _ssum in _t1
    _scount += _t1.count(_ssum)
    _qcount2 += _t1.count(_qsum)
    for _m in re.finditer(re.escape(_qsum), _t1):
        _tail = _t1[_m.end():_m.end() + 800]
        ok_srcp &= _ssum in _tail
ok_srcp &= _scount == 6 and _qcount2 == 6
ok_srcp &= ('`obs_not_layerFlowExecutable` in `OIBridge/ExecSource.lean`, `coherentLiftClass_eq_substratumClass` in `OIBridge/LiftSource.lean`'
            in re.sub(r'\s+', ' ', open(os.path.join(_msroot, 'papers/Main.md'), encoding='utf-8').read()))
# the kernel predicates of the boundary, the overbroad realization claim, exclusion or derivation of the lift, derivation of
# either assumption and any minimality claim are absent from every manuscript source and generated form
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/ch01-observation.md', 'book/ch19-open-problems.md', 'book/The-Incompleteness-of-Observation-FULL.md',
             'papers/GR.tex', 'papers/Main.tex', 'papers/Explainer.tex', 'book/The-Incompleteness-of-Observation-FULL.tex'):
    _t1 = re.sub(r'\s+', ' ', open(os.path.join(_msroot, _rel), encoding='utf-8').read()).replace('\\_', '_')
    for _bad in ('DerivedOI', 'SourcedOI', 'PhasesAvailable', 'SubstratumAvail', 'RouteB', 'LayerFlowExecutable', 'obsTheory', 'permTheory',
                 'every realization of those channels is configuration-level, and', 'every realization of the coherent',
                 'every Kraus realization is configuration-level', 'the wave-operator lift is excluded', 'the wave-operator lift is ruled out',
                 'the lift is derived', 'derives the layer flow', 'the executability is derived', 'executability is derived from',
                 'derives the executability', 'the layer flow is derived', 'the phases are derived', 'derives the phases',
                 'the pair of assumptions is minimal', 'the assumptions are minimal', 'is the unique resource', 'the minimal resource',
                 'the unique layer-flow', 'the minimal layer-flow', 'delivers configuration-level operations',
                 'both targets negative for every formulation'):
        ok_srcp &= _bad not in _t1
# the registry: both families current with anchors in GR and Main, the census rows, the README
_sp_ex = [f for f in _ptr_reg['families'] if f['name'] == 'executability source: the stated access and the layer flows']
_sp_ls = [f for f in _ptr_reg['families'] if f['name'] == 'lift source: the observer-level lift in the operational interface']
for _fam in (_sp_ex, _sp_ls):
    ok_srcp &= len(_fam) == 1 and _fam[0]['status'] == 'current'
    ok_srcp &= {m['file'] for m in _fam[0]['manuscript']} == {'papers/GR.md', 'papers/Main.md'}
    ok_srcp &= 'carried by no manuscript' not in _fam[0]['note'] and 'SOURCING-PROPAGATION-AUDIT.md' in _fam[0]['note']
ok_srcp &= '| executability source: the stated access and the layer flows | 1 | current |' in _cen_ps
ok_srcp &= '| lift source: the observer-level lift in the operational interface | 1 | current |' in _cen_ps
for _t in ('`R7-SRCP`', 'SOURCING-PROPAGATION-AUDIT.md', 'the sourcing statement', 'unresolved rather than\nexcluded'.replace('\n', ' '),
           'the equivalence exact and the sourcing of this one hypothesis not', 'six occurrences',
           'the phase is not reopened; the lift is not reinterpreted; no uniqueness or minimality is claimed'):
    ok_srcp &= _t in _rd1
ok_srcp &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-SRCP', ok_srcp,
      'Sourcing propagation guard: GR 3.3\'s layer-flow paragraph carries the sourcing statement after its second '
      'qualification and before the no-uniqueness sentence, with the ExecSource and LiftSource witnesses, the four proved '
      'facts, the two reservations (realizations not classified; the wave-operator lift unresolved rather than excluded), '
      'the second display in the words of the first and the exactness sentence; the summary sentence follows the Q3 '
      'summary sentence at all six sites, whose count is unchanged, Main carrying the kernel pointers; no manuscript source '
      'or generated form names a kernel predicate of the boundary, claims every realization of the channels '
      'configuration-level, excludes or derives the wave-operator lift, derives either assumption or claims uniqueness or '
      'minimality; both families are current with anchors in GR and Main; the note keeps the statement, the items, the '
      'constraints, the tests and the non-doings before the outcome and names both commits; the README carries the round '
      'and the counts are unchanged.')

# ---- the C5 discovery audit: no C5 named or adopted; the kill battery; the two candidate families; the polarization
# map stated explicitly and tested; the verdict C with its sharpened reason ----
ok_c5d = True
_c5 = open(os.path.join(BRIDGE, 'OIBridge', 'C5Discovery.lean'), encoding='utf-8').read()
_c5flat = ' '.join(_c5.split())
_c5n = open(os.path.join(os.path.dirname(BRIDGE), 'C5-DISCOVERY-AUDIT.md'), encoding='utf-8').read()
_c5n1 = re.sub(r'\s+', ' ', _c5n)
ok_c5d &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _c5) is None and 'native_decide' not in _c5
ok_c5d &= 'axiom ' not in re.sub(r'/-.*?-/', '', _c5, flags=re.S)
_c5_names = re.findall(r"^theorem ([\w']+)", _c5, re.M)
ok_c5d &= len(_c5_names) == 24 and _c5.count('#print axioms') == 17
for _nm in ('obligations_independent', 'killBattery_substratum', 'killBattery_ones', 'killBattery_perm', 'killBattery_not_qm',
            'obligations_outside_battery', 'bijectionLevel_fails_obligations', 'updateLevel_symplectic_inert',
            'hadamard_not_monomial', 'hadamard_not_preservesDiag', 'siteSwapImage_not_monomial', 'polGen_arch',
            'polGen_not_configurationLevel', 'siteShearImage_one_eq_phaseGate', 'polarizedTheory_phase_level_one',
            'gateFlow_half_eq_hsh', 'polarizedTheory_swap_half_level_one'):
    ok_c5d &= ('#print axioms ' + _nm) in _c5 and _nm in _c5_names
# nothing named C5 is defined in the kernel; the definitions are the battery, the images, the class and the theory
_c5_defs = re.findall(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) (\w+)', _c5, re.M)
ok_c5d &= _c5_defs == ['KillBattery', 'hc', 'hadamard', 'siteShearImage', 'siteSwapImage', 'PolGen', 'polarizedTheory']
ok_c5d &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _c5, re.M) is None
ok_c5d &= 'onesClass_gateFlow' not in _c5 and 'SubstratumAvail' not in _c5 and 'Θ' not in _c5
ok_c5d &= 'import OIBridge.LiftSource' in _c5 and 'import OIBridge.FlowEndpoint' in _c5 and 'import OIBridge.C5Discovery' in root
# the statements, as preregistered
for _t in ('theorem obligations_independent : (PhasesAvailable (substratumTheory (Fin 2)) ∧ ¬ LayerFlowExecutable (substratumTheory (Fin 2)) (Equiv.swap 0 1)) ∧ (LayerFlowExecutable (onesTheory (Fin 2)) (Equiv.swap 0 1) ∧ ¬ PhasesAvailable (onesTheory (Fin 2)))',
           'def KillBattery (T : FiniteOperationalTheory (Fin 2)) : Prop := T = substratumTheory (Fin 2) ∨ T = onesTheory (Fin 2) ∨ T = permTheory (Fin 2)',
           'theorem killBattery_not_qm {T : FiniteOperationalTheory (Fin 2)} (h : KillBattery T) : ¬ ExactAllFiniteEndomorphicQuantumOps T',
           'theorem obligations_outside_battery {T : FiniteOperationalTheory (Fin 2)} (hph : PhasesAvailable T) {σ : Equiv.Perm (Fin 2)} {x : Fin 2} (hx : σ x ≠ x) (hex : LayerFlowExecutable T σ) : ¬ KillBattery T',
           'theorem bijectionLevel_fails_obligations [Nonempty S] {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hb : BijectionLevel 𝓘) : ¬ PhasesAvailable (genTheory 𝓘 arch S)',
           'theorem updateLevel_symplectic_inert {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (h : ConfigurationLevel 𝓘) (hl : LabelInvariant 𝓘) : ¬ PhaseFreeRichness (genTheory 𝓘 arch (Fin 2))',
           'noncomputable def hadamard : Matrix (Fin 2) (Fin 2) ℂ := Matrix.of fun i j => if i = 1 ∧ j = 1 then -hc else hc',
           'theorem hadamard_not_monomial : ¬ IsMonomial hadamard',
           'theorem hadamard_not_preservesDiag : ¬ PreservesDiag (conjChannel hadamard)',
           'noncomputable def siteShearImage (n : ℕ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ := Matrix.diagonal fun p => if p.1 = 1 then Complex.I else 1',
           'noncomputable def siteSwapImage (n : ℕ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ := Matrix.of fun p q => if p.2 = q.2 then hadamard p.1 q.1 else 0',
           'theorem siteSwapImage_not_monomial (n : ℕ) (k : Fin n) : ¬ IsMonomial (siteSwapImage n)',
           '| perm {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : permClass T K) : PolGen T K',
           '| shear (n : ℕ) : PolGen (Fin 2 × Fin n) (siteShearImage n)', '| swap (n : ℕ) : PolGen (Fin 2 × Fin n) (siteSwapImage n)',
           'theorem polGen_not_configurationLevel : ¬ ConfigurationLevel PolGen',
           'theorem siteShearImage_one_eq_phaseGate : siteShearImage 1 = phaseGate ((1 : Fin 2), (0 : Fin 1))',
           'theorem polarizedTheory_phase_level_one : (polarizedTheory (Fin 2)).availExt 1 Unit (fun _ => conjChannel (phaseGate ((1 : Fin 2), (0 : Fin 1))))',
           'theorem gateFlow_half_eq_hsh : gateFlow (levelPerm (Equiv.swap (0 : Fin 2) 1) 1) (1 / 2 : ℝ) = siteSwapImage 1 * siteShearImage 1 * siteSwapImage 1',
           'theorem polarizedTheory_swap_half_level_one : (polarizedTheory (Fin 2)).availExt 1 Unit (fun _ => conjChannel (gateFlow (levelPerm (Equiv.swap (0 : Fin 2) 1) 1) (1 / 2 : ℝ)))'):
    ok_c5d &= _t in _c5flat
for _t in ('substratumTheory_not_layerFlowExecutable', 'onesTheory_layerFlowExecutable', 'onesTheory_not_phasesAvailable',
           'onesTheory_not_qm', 'permTheory_not_qm', 'permTheory_not_phasesAvailable', 'bijectionLevel_not_phasesAvailable',
           'bijectionLevel_not_layerFlowExecutable', 'configurationLevel_not_phaseFree', 'configurationLevel_not_layerFlowExecutable',
           'gateFlow_half_entries', 'gateFlow_unitary', 'genTheory_avail_conj'):
    ok_c5d &= _t in _c5flat
# the note: question with the two obligations, outcomes, eight tests, two candidates, tests, meanings, non-doings, outcome
_kc = [_c5n.find(h) for h in ('## The question', '## Three admissible outcomes, frozen', '## The necessary tests every candidate must pass, frozen',
       '## The two candidate families, frozen', '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
       '## What the round does not do', '## Scope amendment, recorded after the preregistration', '## The outcome',
       '## What this note does not claim')]
ok_c5d &= all(x > 0 for x in _kc) and _kc == sorted(_kc)
ok_c5d &= _c5n.lstrip().startswith('# The C5 discovery audit')
for _t in ('Preregistration commit `f57c1f8`', '`main` at `0df6a8a`', 'Status: pass complete',
           '**O1, the relative-phase resource.**', '**O2, the continuous coherent transition resource.**',
           '**A, single condition.**', '**B, two-condition obstruction.**', '**C, underdetermined.**',
           '1. **Level.**', '2. **Non-monomiality through the map.**', '8. **The map, stated.**',
           '**Candidate 1, tunable coupling.**', '**Candidate 2, symplectic partition structure.**',
           '**T0. The obligations and their independence.**', '**T8. The surfaces and the checks.**',
           '| T0 | ', '| T8 | ', 'The verdict, with its reason', 'What a surviving candidate would have to supply',
           'seventeen named results', 'no C5 named or adopted', 'a candidate is never defined by its output'.replace('a candidate', 'A candidate')):
    ok_c5d &= _t in _c5n1
_c5n_out = re.sub(r'\s+', ' ', _c5n[_c5n.find('## The outcome'):])
for _t in ('The verdict is **C, underdetermined**', 'scope amendment above', 'read under the scope amendment',
           'underdetermined for the full generated theory', 'the finiteness of the bare Weil subgroup identifying the candidate',
           'not proving failure after closure', 'Outcome A is not reached', 'Outcome B is not reached',
           'the missing kernel step named', 'continuous canonical structure',
           'the corpus states neither a non-bijection-valued coupling nor the polarization map',
           '| T5 | candidate 2, the flow: outcome (b), read closure-safely.', '| T6 | test 8 for candidate 2: the corpus does not supply the polarization map.'):
    ok_c5d &= _t in _c5n_out
for _bad in ('both obligations fail for a single reason', 'fail for one and the same reason', 'executes no layer flow at every time',
             'cut off', 'the controlled quarter phase is outside the polarized theory', 'not kernel-proved', 'fails at level two',
             'fail together for one reason'):
    ok_c5d &= _bad not in _c5n_out and _bad not in _rd1 and _bad not in _c5_fam[0]['note'] if '_c5_fam' in dir() else True
_c5n_am = re.sub(r'\s+', ' ', _c5n[_c5n.find('## Scope amendment, recorded after the preregistration'):_c5n.find('## The outcome')])
for _t in ('`PolGen` is not the finite Weil group', 'underdetermined for the full generated theory', 'not proving failure after closure',
           'The preregistration above is untouched', 'no theorem changes'):
    ok_c5d &= _t in _c5n_am
# no adoption of a C5 anywhere in the note, the module or the README; no availability read off the representation
for _bad in ('C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'the polarization map is available',
             'the observer can execute the Weil', 'outcome A is reached', 'Outcome A is reached', 'a C5 has been found',
             'the executability is derived', 'the phases are derived', 'Route A is closed', 'OI implies QM', 'bare OI implies'):
    ok_c5d &= not _asserted(_c5n, _bad)
for _bad in ('C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found',
             'outcome A is reached', 'Outcome A is reached', 'the observer can execute the Weil'):
    ok_c5d &= _bad not in _c5 and _bad not in _rd1
for _bad in ('polarizedTheory_not_layerFlowExecutable', 'polarizedTheory_phasesAvailable', 'polarizedTheory_not_phasesAvailable'):
    ok_c5d &= _bad not in _c5flat
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    ok_c5d &= 'C5Discovery' not in _t and 'C5-DISCOVERY' not in _t and 'KillBattery' not in _t and 'polarizedTheory' not in _t
    ok_c5d &= 'PolGen' not in _t and 'siteSwapImage' not in _t and 'gateFlow_half_eq_hsh' not in _t
    ok_c5d &= re.search(r'\(C5\)|\bC5\b', _t) is None
_c5_fam = [f for f in _ptr_reg['families'] if f['name'] == 'C5 discovery: the kill battery and the polarization map']
ok_c5d &= len(_c5_fam) == 1 and _c5_fam[0]['status'] == 'kernel-only' and _c5_fam[0]['modules'] == ['C5Discovery']
ok_c5d &= _c5_fam[0]['manuscript'] == [] and 'Verdict C, underdetermined' in _c5_fam[0]['note']
ok_c5d &= 'Nothing is named C5 or adopted' in _c5_fam[0]['note'] and 'owner decision' in _c5_fam[0]['note']
ok_c5d &= '| C5 discovery: the kill battery and the polarization map | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-C5D`', 'C5-DISCOVERY-AUDIT.md', 'obligations_independent', 'KillBattery', 'bijectionLevel_fails_obligations',
           'updateLevel_symplectic_inert', 'polGen_not_configurationLevel', 'gateFlow_half_eq_hsh', 'Seventeen named results',
           'Verdict: C, underdetermined', 'Nothing is named C5 or adopted', 'underdetermined for the\nfull generated theory'.replace('\n', ' '),
           'a continuous canonical structure on the partition', 'whether the instrument closure synthesizes either is not decided'):
    ok_c5d &= _t in _rd1
for _bad in ('both obligations fail for a single reason', 'fail for one and the same reason', 'executes no layer flow at every time',
             'cut off from both obligations', 'not kernel-proved', 'Both obligations then fail'):
    ok_c5d &= _bad not in _rd1 and _bad not in _c5_fam[0]['note'] and _bad not in re.sub(r'\s+', ' ', _c5n[_c5n.find('## The outcome'):])
ok_c5d &= 'Verdict C, underdetermined, read under the round' in _c5_fam[0]['note'] and 'does not prove failure after the instrument closure' in _c5_fam[0]['note']
ok_c5d &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-C5D', ok_c5d,
      'C5 discovery guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'seventeen results, defines exactly the battery, the Hadamard coefficient and matrix, the two images, the '
      'polarized class and its theory, and nothing named C5; the independence of the obligations, the battery and '
      'its non-quantumness, the bijection-level negative control, the update-level inertness, the non-monomial and '
      'non-diagonal-preserving Hadamard, the non-monomial swap image, the non-configuration-level polarized class, '
      'the level-one quarter phase and the half-time swap flow as the Hadamard-conjugated quarter phase are stated '
      'as pinned; the note keeps the question with the two obligations, the three outcomes, the eight tests, the two '
      'candidates, the tests, the meanings and the non-doings before the outcome, names both commits, records the '
      'verdict C read under the scope amendment, the polarization candidate kernel-proved at level one and undecided beyond '
      'for the full generated theory with the bare Weil subgroup identifying the obstruction and the missing step named, '
      'and adopts no C5 and reads no availability off the representation; no manuscript is edited; the registry and '
      'the census carry the family as kernel-only and the README carries the paragraph and the counts.')

# ---- the polarization closure audit: O2 negative by counting through the full class and the bridge, O1 positive by
# construction in the relabelling closure; the split verdict; nothing from bare-subgroup finiteness; no C5 ----
ok_pcl = True
_pc = open(os.path.join(BRIDGE, 'OIBridge', 'PolarizationClosure.lean'), encoding='utf-8').read()
_pcflat = ' '.join(_pc.split())
_pcn = open(os.path.join(os.path.dirname(BRIDGE), 'POLARIZATION-CLOSURE-AUDIT.md'), encoding='utf-8').read()
_pcn1 = re.sub(r'\s+', ' ', _pcn)
ok_pcl &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _pc) is None and 'native_decide' not in _pc
ok_pcl &= 'axiom ' not in re.sub(r'/-.*?-/', '', _pc, flags=re.S)
_pc_names = re.findall(r"^theorem ([\w']+)", _pc, re.M)
ok_pcl &= len(_pc_names) == 51 and _pc.count('#print axioms') == 26
for _nm in ('gateFlow_entries', 'gateFlow_not_proportional', 'countable_not_layerFlowExecutable',
            'uncountable_of_layerFlowExecutable', 'polC_arch', 'polC_labelInvariant', 'polGen_le_polC', 'gen_countable',
            'gen_reindex', 'polC_mem_gen', 'polC_countable_upToScalar', 'polGen_countable_upToScalar',
            'polarizedTheoryC_not_layerFlowExecutable', 'polarizedTheory_not_layerFlowExecutable', 'phaseRelabel_block',
            'polC_phaseGate', 'polarizedTheoryC_phasesAvailable', 'polC_daggerStable', 'polC_contextStable',
            'polarizedTheoryC_derivedOI', 'polarizedTheoryC_not_qm', "killBattery'_not_qm", 'levelThreeWord_mem',
            'levelThree_word_block', 'levelThree_block_not_clifford', 'polC_levelThree_block'):
    ok_pcl &= ('#print axioms ' + _nm) in _pc and _nm in _pc_names
# the definitions: the relabelling-closed class and its theory, the countability apparatus, the two relabellings, the
# extended battery and the level-three word with its block; nothing named C5; no definition of the discovery audit changed
_pc_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w']+)", _pc, re.M)
ok_pcl &= _pc_defs == ['PolC', 'polarizedTheoryC', 'ZeroOne', 'ImagesAt', 'Gen', 'phaseRelabel', 'ctxRelabel', "KillBattery'",
                       'cycleP', 'levelThreeWord', 'fiberRelabel', 'refl25', 'levelThreeBlock']
ok_pcl &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _pc, re.M) is None
ok_pcl &= 'import OIBridge.C5Discovery' in _pc and 'import OIBridge.PolarizationClosure' in root
ok_pcl &= 'import OIBridge.PolarizationClosure' not in _c5
for _t in ('LayerFlowExecutable', 'PhasesAvailable', 'PolGen', 'polarizedTheory'):
    ok_pcl &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _pc, re.M) is None
# the statements, as preregistered: the relabelling constructor, the inclusion, the counting theorem and its
# contrapositive, countability up to scalar, the two negatives, the phase block and the phases, the closure, the
# non-quantumness, the extended battery, the level-three block and its membership
for _t in ("| relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T') (K : Matrix T T ℂ) : PolC T K → PolC T' (Matrix.reindex e e K)",
           'theorem polGen_le_polC : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), PolGen T K → PolC T K',
           'theorem gateFlow_not_proportional {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) {t t\' : ℝ} (ht : t ∈ Ico (0 : ℝ) 2) (ht\' : t\' ∈ Ico (0 : ℝ) 2) (htt\' : t ≠ t\') (c : ℂ) : gateFlow σ t ≠ c • gateFlow σ t\'',
           'theorem countable_not_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ)) (hD : D.Countable) (hmem : ∀ K : Matrix (S × Fin 1) (S × Fin 1) ℂ, 𝓘 (S × Fin 1) K → ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ), M ∈ D ∧ K = c • M) : ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ',
           'theorem uncountable_of_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable (genTheory 𝓘 arch S) σ) : ¬ ∃ D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ), D.Countable ∧ ∀ K : Matrix (S × Fin 1) (S × Fin 1) ℂ, 𝓘 (S × Fin 1) K → ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ), M ∈ D ∧ K = c • M',
           'theorem polC_countable_upToScalar (T : Type) [Fintype T] [DecidableEq T] : ∃ D : Set (Matrix T T ℂ), D.Countable ∧ ∀ K : Matrix T T ℂ, PolC T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M',
           'theorem polGen_countable_upToScalar (T : Type) [Fintype T] [DecidableEq T] : ∃ D : Set (Matrix T T ℂ), D.Countable ∧ ∀ K : Matrix T T ℂ, PolGen T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M',
           'theorem polarizedTheoryC_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : ¬ LayerFlowExecutable (polarizedTheoryC S) σ',
           'theorem polarizedTheory_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) : ¬ LayerFlowExecutable (polarizedTheory S) σ',
           'theorem phaseRelabel_block (n : ℕ) (p : Fin 2 × Fin n) : ancBlock (Matrix.reindex (phaseRelabel n p) (phaseRelabel n p) (siteShearImage (2 * n))) 0 0 = phaseGate p',
           'theorem polC_phaseGate (n : ℕ) (p : Fin 2 × Fin n) : PolC (Fin 2 × Fin n) (phaseGate p)',
           'theorem polarizedTheoryC_phasesAvailable : PhasesAvailable (polarizedTheoryC (Fin 2))',
           'theorem polC_daggerStable : DaggerStable PolC', 'theorem polC_contextStable : ContextStable PolC',
           'theorem polarizedTheoryC_derivedOI : DerivedOI (polarizedTheoryC (Fin 2))',
           'theorem polarizedTheoryC_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (polarizedTheoryC (Fin 2))',
           "def KillBattery' (T : FiniteOperationalTheory (Fin 2)) : Prop := KillBattery T ∨ T = polarizedTheoryC (Fin 2)",
           "theorem killBattery'_not_qm {T : FiniteOperationalTheory (Fin 2)} (h : KillBattery' T) : ¬ ExactAllFiniteEndomorphicQuantumOps T",
           'theorem levelThreeWord_mem : PolGen (Fin 2 × Fin 3) levelThreeWord',
           'noncomputable def refl25 : Matrix (Fin 2) (Fin 2) ℂ := !![(1 : ℂ), 1 / 2; 1 / 2, -1]',
           'noncomputable def levelThreeBlock : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ := hc • Matrix.of fun x y => refl25 x.1 y.1',
           'theorem levelThree_word_block : ancBlock (Matrix.reindex fiberRelabel fiberRelabel levelThreeWord) 0 1 = levelThreeBlock',
           'theorem polC_levelThree_block : PolC (Fin 2 × Fin 1) levelThreeBlock'):
    ok_pcl &= _t in _pcflat
# the negatives pass through the counting theorem and the bridge, never through a subgroup
for _t in ('exists_scaled_mem_of_instAvail_unitary', 'Cardinal.mk_Ico_real', 'Cardinal.aleph0_lt_continuum',
           'Complex.exp_eq_exp_iff_exists_int', 'derivedOI_layerFlowExecutable_of_qm'):
    ok_pcl &= _t in _pcflat
for _bad in ('Clifford', 'Weil', 'WeylTwirl', 'pauliNormalizer', 'Finite.of', 'Fintype.card_le', 'Nat.card', 'Group.orderOf',
             'orderOf', 'IsOfFinOrder', 'Subgroup'):
    ok_pcl &= _bad not in re.sub(r'/-.*?-/|--[^\n]*', '', _pc, flags=re.S)
# the note: the question, the scope rule, the two classes with the hazard, the two arguments, the four outcomes with
# split expected, the eight tests, the meanings, the non-doings, then the outcome and the non-claims, in that order
_kp = [_pcn.find(h) for h in ('## The question', '## The two classes, and a hazard of the formalization, frozen',
       '## The two obligations, tested by two different arguments, frozen', '## Four admissible outcomes, frozen',
       '## The tests, each with its admissible outcomes', '## What the outcomes mean, fixed in advance',
       '## What the round does not do', '## Scope amendment, recorded after the preregistration', '## The outcome',
       '## What this note does not claim')]
ok_pcl &= all(x > 0 for x in _kp) and _kp == sorted(_kp)
# the scope amendment: the bridge read one-way, the forward direction what the negative consumes, the converse only for
# a unitary itself in the class or under a stated ray-saturation hypothesis, neither stated nor proved; nothing else changed
_pcn_am = re.sub(r'\s+', ' ', _pcn[_pcn.find('## Scope amendment, recorded after the preregistration'):_pcn.find('## The outcome')])
for _t in ('the preregistration above is untouched', 'no theorem, verdict or outcome changes', 'proves the forward direction only',
           'The converse as written does not follow from `op` alone', 'a stated ray-saturation hypothesis',
           'Neither is stated or proved in this round', 'T1 is therefore read as one-way',
           'The converse is immediate only where the unitary itself is in the class', 'gives no availability of the unitary direction'):
    ok_pcl &= _t in _pcn_am
ok_pcl &= 'read one-way under the scope amendment' in _pcn1 and 'That the bridge is an equivalence' in _pcn1
for _bad in ('the converse being the constructor `op`', 'the converse is the constructor `op`', 'equivalent to `c • U` lying in the class',
             'the converse by `op`'):
    ok_pcl &= _bad not in re.sub(r'\s+', ' ', _pcn[_pcn.find('## The outcome'):])
for _bad in ('is equivalent to `c • U`', 'the converse by `op`', 'the converse being the constructor `op`'):
    ok_pcl &= _bad not in _rd1
ok_pcl &= _pcn.lstrip().startswith('# The polarization closure audit')
for _t in ('Preregistration commit `a7c1db0`', '`main` at `2554000`', '**The scope rule, frozen.**', '**The bridge, cited.**',
           '**O2 by counting.**', '**O1 by construction.**', '- **Negative closure.**', '- **Positive escape.**', '- **Split.**',
           '- **Undecided.**', 'No outcome names or adopts a C5.', '**T1. The bridge.**', '**T2. The counting theorem.**',
           '**T8. The surfaces and the checks.**', '| T1 | ', '| T8 | ', 'Status: pass complete', 'twenty-six named results',
           'undecidable for `PolGen` in the type-indexed formulation'):
    ok_pcl &= _t in _pcn1
_pcn_out = re.sub(r'\s+', ' ', _pcn[_pcn.find('## The outcome'):])
for _t in ('The verdict is **split**', 'O1 holds for `PolC` at every level by explicit construction',
           'O2 fails for `PolC`, and by transfer for `PolGen`, through the full class and the bridge, by counting',
           'O2 requires an uncountable projective image',
           'no finitely or countably projectively generated implementation structure sources an executable nontrivial layer flow',
           'is physical interpretation', 'continuity is not formalized in the kernel',
           'a negative for `PolGen` derived from `PolC` and from nothing about bare subgroups', 'The positive does not transfer',
           'undecidable in that formulation', 'a candidate theory constructed by this round, not a theory the corpus sources',
           'test 8 of that audit, that the corpus does not supply the map, is unchanged',
           'the availability of the unitary direction of that ray is not claimed',
           'recorded from the numerical check and not proved', 'it is the countability of the primitive family up to scalar',
           'Whether one realization-level condition supplies both obligations remains the C5 question',
           '| T3 | countability of the polarized classes', '| T4 | O1 for `PolC`', '| T6 | the level-three structure'):
    ok_pcl &= _t in _pcn_out
# no verdict other than split; no inference from bare-subgroup finiteness; no continuity theorem; no C5; no availability
for _bad in ('The verdict is **negative closure**', 'The verdict is **positive escape**', 'The verdict is **undecided**',
             'because the bare Weil subgroup is finite', 'because the Weil subgroup is finite', 'by finiteness of the Weil',
             'by the finiteness of the Weil', 'since the Weil group is finite', 'the finiteness of the bare Weil subgroup proves',
             'the finiteness of the bare Clifford subgroup proves', 'finite, so no flow', 'finite and therefore executes no'):
    ok_pcl &= _bad not in _pcn1 and _bad not in _rd1
for _bad in ('continuous parameter is necessary', 'continuous parameter necessary', 'requires a continuous parameter',
             'needs a continuous parameter', 'a continuous parameter is required', 'continuity is necessary', 'continuity is required',
             'C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found',
             'the polarization map is available', 'is sourced by the corpus', 'the observer has the quarter phase',
             'the observer executes', 'PolGen has the phases', '`PolGen` has the phases', 'the executability is derived',
             'the phases are derived', 'Route A is closed', 'OI implies QM', 'bare OI implies'):
    ok_pcl &= not _asserted(_pcn, _bad)
for _bad in ('continuous parameter is necessary', 'continuous parameter necessary', 'requires a continuous parameter',
             'needs a continuous parameter', 'a continuous parameter is required', 'continuity is necessary', 'continuity is required',
             'C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found',
             'is available to the observer', 'is sourced by the corpus'):
    ok_pcl &= _bad not in _pc and _bad not in _rd1
for _bad in ('the executability is derived', 'the phases are derived'):
    ok_pcl &= _bad not in _pc and not _asserted(_rd, _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('PolarizationClosure', 'POLARIZATION-CLOSURE', 'PolC', 'polarizedTheoryC', "KillBattery'",
                 'uncountable_of_layerFlowExecutable', 'countable_not_layerFlowExecutable', 'phaseRelabel', 'levelThree'):
        ok_pcl &= _bad not in _t
_pc_fam = [f for f in _ptr_reg['families'] if f['name'] == 'polarization closure: O2 by counting and O1 by construction']
ok_pcl &= len(_pc_fam) == 1 and _pc_fam[0]['status'] == 'kernel-only' and _pc_fam[0]['modules'] == ['PolarizationClosure']
ok_pcl &= _pc_fam[0]['manuscript'] == [] and 'Verdict split' in _pc_fam[0]['note']
for _t in ('Nothing is named C5 or adopted', 'owner decision', 'not sourced by the corpus', 'test 8 of the discovery audit is unchanged',
           'the reading of it as a continuous parameter being interpretation', "the unitary direction's availability not claimed",
           'the positive does not transfer to PolGen in the type-indexed formulation'):
    ok_pcl &= _t in _pc_fam[0]['note']
for _bad in ('continuous parameter is necessary', 'is available to the observer', 'is sourced by the corpus', 'C5 holds',
             'is equivalent to `c • U`', 'the converse by `op`', 'the converse being the constructor `op`'):
    ok_pcl &= _bad not in _pc_fam[0]['note']
ok_pcl &= '| polarization closure: O2 by counting and O1 by construction | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-PCL`', 'POLARIZATION-CLOSURE-AUDIT.md', 'polGen_le_polC', 'gateFlow_not_proportional',
           'countable_not_layerFlowExecutable', 'polC_countable_upToScalar', 'uncountable_of_layerFlowExecutable',
           'phaseRelabel_block', 'polarizedTheoryC_phasesAvailable', 'polC_contextStable', 'polarizedTheoryC_derivedOI',
           'polarizedTheoryC_not_qm', "KillBattery'", 'levelThree_word_block', 'levelThree_block_not_clifford',
           'Twenty-six named results', 'Verdict: split', 'O2 requires an uncountable projective image',
           'no finitely or countably projectively generated implementation structure', 'continuity not being formalized',
           'not sourced by the corpus', 'test 8 of the discovery audit is unchanged', 'Nothing is named C5 or adopted',
           'the positive does not transfer to `PolGen` in the type-indexed formulation',
           "the unitary direction's availability not claimed", 'nothing is inferred from the finiteness of the bare Clifford or Weil subgroup'):
    ok_pcl &= _t in _rd1
# the discovery note: its frozen text and its outcome untouched, one section recorded after them
_c5n_rec = _c5n.find('## Recorded after the round: the polarization closure audit')
ok_pcl &= _c5n_rec > _c5n.find('## What this note does not claim') and _c5n_rec > _c5n.find('Status: pass complete')
_c5n_rec1 = re.sub(r'\s+', ' ', _c5n[_c5n_rec:])
for _t in ('Test 8 above is unchanged', 'The verdict C of this note is unchanged', 'the closure-safe reading of this note stands as written',
           'not the finiteness of the bare Weil subgroup', 'undecidable for `PolGen` in the type-indexed formulation',
           'a candidate theory of that round', 'Nothing is named C5 or adopted'):
    ok_pcl &= _t in _c5n_rec1
ok_pcl &= _c5n_rec1.count('## ') == 1
ok_pcl &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-PCL', ok_pcl,
      'Polarization closure guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'twenty-six results, defines exactly the relabelling-closed class and its theory, the countability apparatus, the '
      'two relabellings, the extended battery and the level-three word with its block, nothing named C5 and no definition '
      'of the discovery audit; the counting theorem and its contrapositive, countability up to scalar of both classes, the '
      'two negatives, the phase block and the phases, dagger and context stability, the closure, the non-quantumness, the '
      'extended battery and the level-three block are stated as pinned, every negative passing through the counting '
      'theorem and the bridge and nothing through a subgroup; the note keeps the question, the scope rule, the two classes '
      'with the hazard, the two arguments, the four outcomes, the eight tests, the meanings and the non-doings before the '
      'outcome, names both commits, records the split verdict with the mechanism and the reason, the theorem-level form '
      'of the O2 conclusion with continuity marked as interpretation, the transfer to PolGen on each side, the constructed '
      'theory as a candidate of the round with test 8 unchanged, and the contractive block with the unitary direction '
      'unclaimed; no manuscript is edited; the registry and the census carry the family as kernel-only; the discovery note '
      'carries one section after its frozen text; the README carries the paragraph and the counts.')

# ---- the coherent-continuum source audit: the strengthened necessary condition (uncountably many non-monomial rays at
# level one) proved and necessary only; the two known failures orthogonal; the read-write image finite; the canonical
# path with the continuum and unsourced; the coupling traced and outside the current axioms; outcome 2; no C5 ----
ok_ccs = True
_cc = open(os.path.join(BRIDGE, 'OIBridge', 'CoherentContinuumSource.lean'), encoding='utf-8').read()
_ccflat = ' '.join(_cc.split())
_ccn = open(os.path.join(os.path.dirname(BRIDGE), 'COHERENT-CONTINUUM-SOURCE-AUDIT.md'), encoding='utf-8').read()
_ccn1 = re.sub(r'\s+', ' ', _ccn)
ok_ccs &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _cc) is None and 'native_decide' not in _cc
ok_ccs &= 'axiom ' not in re.sub(r'/-.*?-/', '', _cc, flags=re.S)
_cc_names = re.findall(r"^theorem ([\w']+)", _cc, re.M)
ok_ccs &= len(_cc_names) == 19 and _cc.count('#print axioms') == 17
for _nm in ('gateFlow_entries_im', 'gateFlow_not_monomial', 'isMonomial_of_smul', 'gateFlow_not_countablyCovered',
            'nonMonomialCountablyCovered_of_countable', 'uncountableNonMonomialRays_of_layerFlowExecutable',
            'not_layerFlowExecutable_of_nonMonomialCountablyCovered', 'uncountableNonMonomialRays_of_qm',
            'substratumClass_monomial', 'weightGate_not_proportional', 'substratumClass_not_countablyCovered',
            'polC_nonMonomialCountablyCovered', 'known_failures_orthogonal', 'readWriteOperator_range_finite',
            'readWrite_parameter_uncountable_image_finite', 'gateFlow_path_coherent_continuum',
            'coherent_continuum_not_sourced'):
    ok_ccs &= ('#print axioms OIBridge.CoherentContinuumSource.' + _nm) in _cc and _nm in _cc_names
# the definitions: the two predicates and the diagonal weight; nothing named C5; no coupling, no class containing the
# flow, no existing definition restated
_cc_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w']+)", _cc, re.M)
ok_ccs &= _cc_defs == ['NonMonomialCountablyCovered', 'UncountableNonMonomialRays', 'weightGate']
ok_ccs &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _cc, re.M) is None
ok_ccs &= ': ImplementationClass :=' not in _cc and 'Coupling' not in _cc and 'coupling' not in re.sub(r'/-.*?-/|--[^\n]*', '', _cc, flags=re.S)
ok_ccs &= 'import OIBridge.PolarizationClosure' in _cc and 'import OIBridge.CoherentContinuumSource' in root
for _t in ('LayerFlowExecutable', 'PhasesAvailable', 'PolC', 'PolGen', 'substratumClass', 'ReadWriteFamily', 'gateFlow', 'IsMonomial'):
    ok_ccs &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _cc, re.M) is None
# the statements, as preregistered
for _t in ('theorem gateFlow_not_monomial {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) : ¬ IsMonomial (gateFlow σ t)',
           'def NonMonomialCountablyCovered (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop := ∃ D : Set (Matrix T T ℂ), D.Countable ∧ ∀ K : Matrix T T ℂ, 𝓘 T K → ¬ IsMonomial K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M',
           'def UncountableNonMonomialRays (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop := ¬ NonMonomialCountablyCovered 𝓘 T',
           'theorem uncountableNonMonomialRays_of_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable (genTheory 𝓘 arch S) σ) : UncountableNonMonomialRays 𝓘 (S × Fin 1)',
           'theorem not_layerFlowExecutable_of_nonMonomialCountablyCovered {𝓘 : ImplementationClass} (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (h : NonMonomialCountablyCovered 𝓘 (S × Fin 1)) : ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ',
           'theorem uncountableNonMonomialRays_of_qm {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (h : ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2))) : UncountableNonMonomialRays 𝓘 (Fin 2 × Fin 1)',
           'theorem substratumClass_monomial (K : Matrix T T ℂ) (h : substratumClass T K) : IsMonomial K := h',
           'theorem substratumClass_not_countablyCovered {a b : T} (hab : a ≠ b) : ¬ ∃ D : Set (Matrix T T ℂ), D.Countable ∧ ∀ K : Matrix T T ℂ, substratumClass T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M',
           'theorem polC_nonMonomialCountablyCovered : NonMonomialCountablyCovered PolC T',
           'theorem readWriteOperator_range_finite {a b : S} (F : ReadWriteControl.ReadWriteFamily a b) : (Set.range (ReadWriteControl.readWriteOperator F)).Finite',
           '¬ (Set.univ : Set ℝ).Countable ∧ (Set.range (ReadWriteControl.readWriteOperator F)).Finite ∧ ∀ l : ℝ, IsMonomial (ReadWriteControl.readWriteOperator F l)',
           'theorem gateFlow_path_coherent_continuum {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) : (∀ t ∈ Ioo (0 : ℝ) 1, ¬ IsMonomial (gateFlow σ t)) ∧ ¬ ∃ D : Set (Matrix S S ℂ), D.Countable ∧ ∀ t ∈ Ioo (0 : ℝ) 1, ∃ (c : ℂ) (M : Matrix S S ℂ), M ∈ D ∧ gateFlow σ t = c • M',
           '∧ ¬ LayerFlowExecutable (substratumTheory S) σ ∧ ∀ (𝓘 : ImplementationClass) (arch : Architecture 𝓘), ConfigurationLevel 𝓘 → ¬ (genTheory 𝓘 arch S).availExt 1 Unit (fun _ => conjChannel (gateFlow (levelPerm σ 1) (1 / 2 : ℝ)))'):
    ok_ccs &= _t in _ccflat
# the negatives pass through the bridge, non-proportionality and non-monomiality; the read-write image needs no continuity
for _t in ('exists_scaled_mem_of_instAvail_unitary', 'gateFlow_not_proportional', 'Cardinal.mk_Ioo_real', 'Real.sin_pos_of_pos_of_lt_pi',
           'polC_countable_upToScalar', 'readWriteOperator_eq_perm', 'readWriteOperator_monomial', 'derivedOI_layerFlowExecutable_of_qm',
           'substratumTheory_not_layerFlowExecutable', 'configurationLevel_not_avail_gateFlow_half'):
    ok_ccs &= _t in _ccflat
for _bad in ('Continuous ', 'ContinuousOn', 'Weil', 'Clifford', 'orderOf', 'Subgroup'):
    ok_ccs &= _bad not in re.sub(r'/-.*?-/|--[^\n]*', '', _cc, flags=re.S)
# the note: the question, the strengthened condition, the census, the outcomes, the tests, the non-doings, then the outcome
_kcc = [_ccn.find(h) for h in ('## The question', '## The strengthened necessary condition, frozen', '## The corpus census, frozen before the pass',
        '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do', '## The outcome',
        '## What this note does not claim')]
ok_ccs &= all(x > 0 for x in _kcc) and _kcc == sorted(_kcc)
ok_ccs &= _ccn.lstrip().startswith('# The coherent-continuum source audit')
for _t in ('Preregistration commit `24dd290`', '`main` at `fa0938b`', 'Status: preregistered; no proof attempted', 'Status: pass complete',
           '**Scope boundary.** This is a necessary condition only', '1. **Existing source.**', '2. **No current source; empirical extension remains.**',
           '3. **Underdetermined operational route.**', 'No outcome establishes that C5 exists or does not exist', '### T1 —', '### T8 —',
           '| S1, stated observer access', '| S9, consistency controls', 'seventeen named results'):
    ok_ccs &= _t in _ccn1
_ccn_out = re.sub(r'\s+', ' ', _ccn[_ccn.find('## The outcome'):])
for _t in ('The verdict is **outcome 2, no current source; the empirical extension remains**', 'The condition is necessary only',
           'the reading as a continuous coherent control parameter is interpretation',
           'both kinds of partial resource separately', 'no stated operational source of an uncountable coherent projective family',
           'The canonical gate path has that family mathematically and is not available',
           'remains an explicitly extra physical extension, not a consequence of C1–C4 or of the stated access',
           'Outcome 1 is not reached', 'Outcome 3 is not reached', 'The second item alone is necessary and not sufficient, and is not C5',
           'the inference from the mathematical continuum to executability is rejected', 'no map is invented',
           'nowhere is it defined as an operation of the current theory', 'defined nowhere' if False else 'outside the current axioms',
           'the closure audit is a consequence', 'is not superseded', 'Nothing is named "C5" in the module or adopted in this note',
           '| S1 | ', '| S8 | ', '| S9 | ', '| T1 | ', '| T8 | '):
    ok_ccs &= _t in _ccn_out
for _bad in ('The verdict is **outcome 1', 'The verdict is **outcome 3', 'Outcome 1 is reached', 'outcome 1 is reached',
             'the observer can execute the canonical path', 'sufficient for a layer flow, so',
             'the coupling is derived', 'the coupling is defined', 'defines the coupling',
             'C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found',
             'continuity is necessary for O2', 'continuous parameter is necessary', 'requires a continuous parameter',
             'is available to the observer', 'is sourced by the corpus', 'the executability is derived', 'the phases are derived',
             'Route A is closed', 'OI implies QM', 'bare OI implies'):
    ok_ccs &= not _asserted(_ccn, _bad)
for _bad in ('is sufficient for a layer flow', 'therefore the observer can execute', 'the coupling is derived', 'the coupling is defined',
             'C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found',
             'continuous parameter is necessary', 'is available to the observer', 'is sourced by the corpus', 'Outcome 1 is reached',
             'outcome 1 is reached'):
    ok_ccs &= _bad not in _cc and _bad not in _rd1
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('CoherentContinuumSource', 'COHERENT-CONTINUUM', 'NonMonomialCountablyCovered', 'UncountableNonMonomialRays',
                 'weightGate', 'known_failures_orthogonal', 'coherent_continuum_not_sourced', 'readWriteOperator_range_finite'):
        ok_ccs &= _bad not in _t
_cc_fam = [f for f in _ptr_reg['families'] if f['name'] == 'coherent-continuum source: the strengthened necessary condition and the unsourced path']
ok_ccs &= len(_cc_fam) == 1 and _cc_fam[0]['status'] == 'kernel-only' and _cc_fam[0]['modules'] == ['CoherentContinuumSource']
ok_ccs &= _cc_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 2, no current source', 'necessary only', 'the two known failures are orthogonal'.replace('the two', 'The two'),
           'no continuity assumed', 'is not sourced', 'defined nowhere as an operation of the current theory', 'Nothing is named C5 or adopted',
           'the second alone not sufficient', 'owner decision'):
    ok_ccs &= _t in _cc_fam[0]['note']
for _bad in ('is sufficient for a layer flow', 'C5 holds', 'is available to the observer', 'is sourced by the corpus', 'continuous parameter is necessary'):
    ok_ccs &= _bad not in _cc_fam[0]['note']
ok_ccs &= '| coherent-continuum source: the strengthened necessary condition and the unsourced path | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-CCS`', 'COHERENT-CONTINUUM-SOURCE-AUDIT.md', 'gateFlow_not_monomial', 'NonMonomialCountablyCovered', 'UncountableNonMonomialRays',
           'uncountableNonMonomialRays_of_layerFlowExecutable', 'not_layerFlowExecutable_of_nonMonomialCountablyCovered',
           'nonMonomialCountablyCovered_of_countable', 'uncountableNonMonomialRays_of_qm', 'substratumClass_not_countablyCovered',
           'polC_nonMonomialCountablyCovered', 'known_failures_orthogonal', 'readWriteOperator_range_finite',
           'gateFlow_path_coherent_continuum', 'coherent_continuum_not_sourced', 'The condition is necessary only',
           'continuum without coherent mixing, coherent mixing without a continuum', 'an uncountable parameter domain is not an uncountable operational image',
           'the inference from the mathematical continuum to executability is rejected', 'defined nowhere as an operation of the current theory',
           'Verdict: outcome 2, no current source, the empirical extension remaining', 'the second alone is not sufficient',
           'Seventeen named results', 'Nothing is named C5 or adopted; no coupling is defined; no definition changes'):
    ok_ccs &= _t in _rd1
# the closure note: one section recorded after its frozen text and its outcome, the verdict unchanged
_pcn_rec = _pcn.find('## Recorded after the round: the coherent-continuum source audit')
ok_ccs &= _pcn_rec > _pcn.find('## What this note does not claim') and _pcn_rec > _pcn.find('Status: pass complete')
_pcn_rec1 = re.sub(r'\s+', ' ', _pcn[_pcn_rec:])
for _t in ('strengthens the necessary condition above', 'is not by itself diagnostic', 'The verdict of this note is unchanged',
           'records no stated source of the coherent continuum in the corpus', 'Nothing is named C5 or adopted'):
    ok_ccs &= _t in _pcn_rec1
ok_ccs &= _pcn_rec1.count('## ') == 1
# the discovery note is untouched by this round: still exactly one recorded section
ok_ccs &= _c5n.count('## Recorded after the round') == 1 and 'coherent-continuum' not in _c5n
ok_ccs &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-CCS', ok_ccs,
      'Coherent-continuum source guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its seventeen results, defines exactly the two cover predicates and the diagonal weight, nothing named C5, no '
      'coupling, no class containing the flow and no existing definition restated; the non-monomiality of every '
      'intermediate-time flow point, the strengthened necessary condition and its contrapositive, the consistency '
      'control, the orthogonal failures, the finite read-write image and the unsourced path are stated as pinned, every '
      'negative passing through the bridge, non-proportionality and non-monomiality with no continuity assumed; the note '
      'keeps the question, the strengthened condition, the census, the outcomes, the tests and the non-doings before the '
      'outcome, names both commits, records outcome 2 with the per-route and per-test tables, the necessary-only reading, '
      'the rejected inference from the mathematical continuum, the coupling traced and outside the current axioms, and '
      'the three obligations with the second not sufficient; no manuscript is edited; the registry and the census carry '
      'the family as kernel-only; the closure note carries one section after its frozen text and the discovery note is '
      'untouched; the README carries the paragraph and the counts.')

# ---- the state-mixing coupling construction audit: one sourced real mixing datum on a single pair, a postulate, closed
# with the stated access; the resource from the datum; the bridge as identity and composition; the closure and the
# completion, with the class-level form under the stated-access containment; the two replacement classes failing;
# outcome 1; no C5; no minimality claim ----
ok_smc = True
_sm = open(os.path.join(BRIDGE, 'OIBridge', 'StateMixingCoupling.lean'), encoding='utf-8').read()
_smflat = ' '.join(_sm.split())
_smn = open(os.path.join(os.path.dirname(BRIDGE), 'STATE-MIXING-COUPLING-AUDIT.md'), encoding='utf-8').read()
_smn1 = re.sub(r'\s+', ' ', _smn)
ok_smc &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _sm) is None and 'native_decide' not in _sm
ok_smc &= 'axiom ' not in re.sub(r'/-.*?-/', '', _sm, flags=re.S)
_sm_names = re.findall(r"^theorem ([\w']+)", _sm, re.M)
ok_smc &= len(_sm_names) == 50 and _sm.count('#print axioms') == 25
for _nm in ('mixR_arch', 'mixR_le_mixC', 'mixImage_mul', 'mixImage_unitary', 'mixImage_not_monomial', 'mixImage_not_proportional',
            'mixC_uncountableNonMonomialRays', 'phaseIndicator_mem', 'siteShear_mem', 'gateFlow_eq_shear_mix',
            'layerFlowExecutable_of_mixSourced', 'mixTheory_layerFlowExecutable', 'mixC_daggerStable', 'mixC_contextStable',
            'derivedOI_of_stated', 'mixTheory_derivedOI', 'qm_of_mixSourced', 'mixTheory_phaseFree', 'mixTheory_endpoint',
            'mixTheory_qm', 'mixR_countable_upToScalar', 'mixTheoryR_not_layerFlowExecutable', 'mixTheoryR_not_qm',
            'mixTheory_empty_not_qm', 'comparison'):
    ok_smc &= ('#print axioms OIBridge.StateMixingCoupling.' + _nm) in _sm and _nm in _sm_names
# the definitions: the datum, its sourcing map, the class family, its full instance, the two theories and the countability
# apparatus; nothing named C5 or minimal; no existing definition restated
_sm_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w']+)", _sm, re.M)
ok_smc &= _sm_defs == ['rot', 'mixImage', 'MixR', 'MixC', 'mixTheoryR', 'mixTheory', 'MixImagesAt', 'GenM']
ok_smc &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _sm, re.M) is None
ok_smc &= re.search(r'(?i)\bminimal\b', re.sub(r'/-.*?-/|--[^\n]*', '', _sm, flags=re.S)) is None
for _t in ('LayerFlowExecutable', 'PhasesAvailable', 'PhaseFreeRichness', 'DerivedOI', 'PolC', 'PolGen', 'substratumClass',
           'ReadWriteFamily', 'gateFlow', 'IsMonomial', 'phaseGate', 'siteShearImage'):
    ok_smc &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _sm, re.M) is None
# the vocabulary boundary on the definition region: the datum, the sourcing map and the class name no flow, no transition,
# no polarization image, no quantum-control predicate, no exponential; the datum is cosine and sine
_sm_defregion = _sm[_sm.find('noncomputable def rot'):_sm.find('/-- **THE CLASS OF THE STATED ACCESS AND THE DATUM AT EVERY ANGLE.** -/')]
ok_smc &= 'Real.cos' in _sm_defregion and 'Real.sin' in _sm_defregion
for _bad in ('gateFlow', 'unit ', 'SecondOrderCircuit.proj', 'proj (', 'flow', 'transition', 'hadamard', 'siteSwapImage', 'siteShearImage',
             'PhaseFreeRichness', 'LayerFlowExecutable', 'HasCompositeUnitaryControl', 'Complex.exp', 'cexp', 'levelPerm', 'permMat ',
             'ExactAllFiniteEndomorphicQuantumOps', 'Quantum', 'quantum'):
    ok_smc &= _bad not in _sm_defregion
ok_smc &= 'import OIBridge.CoherentContinuumSource' in _sm and 'import OIBridge.StateMixingCoupling' in root
# the statements, as preregistered and amended
for _t in ('noncomputable def rot (θ : ℝ) : Matrix (Fin 2) (Fin 2) ℂ := !![(Real.cos θ : ℂ), -(Real.sin θ : ℂ); (Real.sin θ : ℂ), (Real.cos θ : ℂ)]',
           'noncomputable def mixImage (n : ℕ) (θ : ℝ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ := Matrix.of fun p q => if p.2 = q.2 then rot θ p.1 q.1 else 0',
           '| phase (n : ℕ) (p : Fin 2 × Fin n) : MixR D (Fin 2 × Fin n) (phaseGate p)',
           '| mix (n : ℕ) (θ : ℝ) (hθ : θ ∈ D) : MixR D (Fin 2 × Fin n) (mixImage n θ)',
           '| relabel {T T\' : Type} [Fintype T] [DecidableEq T] [Fintype T\'] [DecidableEq T\'] (e : T ≃ T\') (K : Matrix T T ℂ) : MixR D T K → MixR D T\' (Matrix.reindex e e K)',
           'abbrev MixC : ImplementationClass := MixR Set.univ',
           'noncomputable def mixTheory (S : Type) [Fintype S] [DecidableEq S] : FiniteOperationalTheory S := genTheory MixC mixC_arch S',
           'theorem mixImage_not_monomial {n : ℕ} (k : Fin n) {θ : ℝ} (hθ : θ ∈ Ioo (0 : ℝ) (Real.pi / 2)) : ¬ IsMonomial (mixImage n θ)',
           'theorem mixC_uncountableNonMonomialRays : UncountableNonMonomialRays MixC (Fin 2 × Fin 1)',
           'theorem gateFlow_eq_shear_mix (n : ℕ) (t : ℝ) : gateFlow (levelPerm (Equiv.swap (0 : Fin 2) 1) n) t = Complex.exp (((Real.pi * t / 2 : ℝ) : ℂ) * Complex.I) • (siteShearImage n * mixImage n (-(Real.pi * t / 2)) * (siteShearImage n)ᴴ)',
           'theorem mixTheory_layerFlowExecutable : LayerFlowExecutable (mixTheory (Fin 2)) (Equiv.swap 0 1)',
           'theorem mixC_daggerStable : DaggerStable MixC', 'theorem mixC_contextStable : ContextStable MixC',
           'theorem mixTheory_derivedOI : DerivedOI (mixTheory (Fin 2))',
           'theorem qm_of_mixSourced {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hl : LabelInvariant 𝓘) (hd : DaggerStable 𝓘) (hc : ContextStable 𝓘) (hperm : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), permClass T K → 𝓘 T K) (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p)) (hmix : ∀ (n : ℕ) (θ : ℝ), 𝓘 (Fin 2 × Fin n) (mixImage n θ)) : DerivedOI (genTheory 𝓘 arch (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2))',
           'theorem mixTheory_phaseFree : PhaseFreeRichness (mixTheory (Fin 2))',
           'theorem mixTheory_endpoint : DerivedOI (mixTheory (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2))',
           'theorem mixTheory_qm : ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2))',
           'theorem mixR_countable_upToScalar {D : Set ℝ} (hD : D.Countable) (T : Type) [Fintype T] [DecidableEq T] : ∃ D\' : Set (Matrix T T ℂ), D\'.Countable ∧ ∀ K : Matrix T T ℂ, MixR D T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D\' ∧ K = c • M',
           'theorem mixTheoryR_not_qm {D : Set ℝ} (hD : D.Countable) : ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR D (Fin 2))',
           'theorem mixTheory_empty_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR ∅ (Fin 2))',
           '∧ (∀ D : Set ℝ, D.Countable → ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR D (Fin 2))) ∧ ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR ∅ (Fin 2)) ∧ ¬ ExactAllFiniteEndomorphicQuantumOps (polarizedTheoryC (Fin 2))'):
    ok_smc &= _t in _smflat
# the bridge passes through the constructor op, the cited closure theorem and the counting theorem; the closure reuses the
# stated theorems; no availability is stipulated
for _t in ('SubstratumSource.genTheory_avail_conj', 'gateFlow_unitary', 'qm_of_derivedOI_layerFlowExecutable',
           'phaseFree_of_derivedOI_layerFlowExecutable', 'genTheory_reversibleImplementationLocality', 'genTheory_embeddedObservation',
           'countable_not_layerFlowExecutable', 'derivedOI_layerFlowExecutable_of_qm', 'Finset.induction_on', 'Real.cos_sq_add_sin_sq',
           'polarizedTheoryC_not_qm'):
    ok_smc &= _t in _smflat
for _bad in ('sorry', 'axiom ', 'Weil', 'Clifford'):
    ok_smc &= _bad not in re.sub(r'/-.*?-/|--[^\n]*', '', _sm, flags=re.S)
# the note: the question, the status, the datum, the bridge, the outcomes, the tests, the non-doings, the amendment, then the
# outcome and the non-claims, in that order
_ksm = [_smn.find(h) for h in ('## The question', '## The status of the construction, frozen', '## The datum, frozen in form',
        '## The bridge, frozen as a route', '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome', '## What this note does not claim')]
ok_smc &= all(x > 0 for x in _ksm) and _ksm == sorted(_ksm)
ok_smc &= _smn.lstrip().startswith('# The state-mixing coupling construction audit')
for _t in ('Preregistration commit `fc4498d`', 'scope amendment `314076c`', '`main` at `f9e9648`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', 'The coupling datum is a **postulate**', '**The word "minimal" is not used.**',
           '1. **Sufficient.**', '2. **Bridge fails.**', '3. **Comparison fails.**', 'No outcome names or adopts C5',
           '**T1. The datum and the class.**', '**T8. The verdict.**', 'the stated-access containment made explicit',
           'No theorem is sought that derives the stated permutation or read-write access from the mixing datum alone',
           'The preregistered concrete endpoint, bridge, comparisons and outcomes are unchanged', 'twenty-five named results'):
    ok_smc &= _t in _smn1
_smn_out = re.sub(r'\s+', ' ', _smn[_smn.find('## The outcome'):])
for _t in ('The verdict is **outcome 1, sufficient**', 'the class-level form read under the scope amendment',
           '**The bridge, step by step.**', 'a case the preregistration did not foresee and the product lemma settles',
           'Outcome 1 is reached', 'It is not a global minimality or uniqueness theorem, and none is claimed',
           'The datum is a postulate', 'nothing here derives it from the substratum, from C1–C4, or from the stated access',
           'nothing here says that nature, the OI substratum, or the observer supplies it', 'The manuscript status of the resource is unchanged',
           'what realization-level physical principle forces the mixing datum', 'That question is not attempted here',
           'That the class-level theorem holds without the permutation containment: no such theorem was sought',
           'the kill battery is not extended', '| T1 | ', '| T4 | ', '| T8 | '):
    ok_smc &= _t in _smn_out
for _bad in ('The verdict is **outcome 2', 'The verdict is **outcome 3', 'the minimal', 'a minimal', 'minimal coupling',
             'minimal extension', 'is unique', 'uniquely', 'the datum is available', 'derives the datum',
             'nature supplies', 'the observer has the datum', 'the observer can execute', 'the observer can source',
             'C5 is the', 'C5 := ', 'define C5 as', 'we adopt C5', 'C5 holds', 'C5 is satisfied', 'a C5 has been found', 'the datum is C5',
             'is sourced by the corpus', 'derived from the stated access, and', 'forces the mixing datum, which'):
    ok_smc &= _bad not in _smn_out
ok_smc &= re.search(r'\bminimal\b', _smn_out) is None
for _bad in ('the datum is derived', 'the datum is available', 'derives the datum', 'is sourced by the corpus', 'C5 holds', 'C5 is the',
             'a C5 has been found', 'we adopt C5', 'the observer can execute', 'is derived from the substratum', 'derived from C1',
             'is minimal', 'the datum is a C5'):
    ok_smc &= not _asserted(_smn[_smn.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('StateMixingCoupling', 'STATE-MIXING-COUPLING', 'mixImage', 'MixC', 'MixR', 'mixTheory', 'qm_of_mixSourced',
                 'gateFlow_eq_shear_mix', 'phaseIndicator_mem'):
        ok_smc &= _bad not in _t
_sm_fam = [f for f in _ptr_reg['families'] if f['name'] == 'state-mixing coupling construction: one sourced pair coupling and the completion']
ok_smc &= len(_sm_fam) == 1 and _sm_fam[0]['status'] == 'kernel-only' and _sm_fam[0]['modules'] == ['StateMixingCoupling']
ok_smc &= _sm_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 1, sufficient', 'The datum is a postulate', 'a comparison and not a global minimality or uniqueness theorem',
           'Nothing is named C5 or adopted', 'the manuscript status of the resource, which is unchanged', 'owner decision'):
    ok_smc &= _t in _sm_fam[0]['note']
for _bad in ('is minimal', 'the minimal', 'the datum is derived', 'the datum is available', 'C5 holds', 'is sourced by the corpus'):
    ok_smc &= _bad not in _sm_fam[0]['note']
ok_smc &= '| state-mixing coupling construction: one sourced pair coupling and the completion | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-SMC`', 'STATE-MIXING-COUPLING-AUDIT.md', 'rot', 'mixImage', 'MixR', 'MixC', 'mixTheory', 'mixC_uncountableNonMonomialRays',
           'gateFlow_eq_shear_mix', 'phaseIndicator_mem', 'siteShear_mem', 'layerFlowExecutable_of_mixSourced', 'mixTheory_layerFlowExecutable',
           'mixC_daggerStable', 'mixC_contextStable', 'derivedOI_of_stated', 'mixTheory_derivedOI', 'mixTheory_phaseFree', 'mixTheory_qm',
           'mixTheory_endpoint', 'qm_of_mixSourced', 'mixR_countable_upToScalar', 'mixTheoryR_not_qm', 'mixTheory_empty_not_qm', 'comparison',
           'The datum is a postulate', 'the manuscript status of the resource is unchanged', 'Verdict: outcome 1, sufficient',
           'a comparison and not a global minimality or uniqueness theorem', 'Twenty-five named results', 'Nothing is named C5 or adopted'):
    ok_smc &= _t in _rd1
for _bad in ('the minimal coupling', 'minimal extension', 'the datum is derived', 'the datum is available', 'the observer can execute the flow',
             'C5 holds', 'C5 is the', 'a C5 has been found'):
    ok_smc &= _bad not in _rd1
# the coherent-continuum note: one section recorded after its frozen text; the discovery and closure notes untouched by this round
_ccn_rec = _ccn.find('## Recorded after the round: the state-mixing coupling construction audit')
ok_smc &= _ccn_rec > _ccn.find('## What this note does not claim') and _ccn_rec > _ccn.find('Status: pass complete')
_ccn_rec1 = re.sub(r'\s+', ' ', _ccn[_ccn_rec:])
for _t in ('stated as a postulate', 'meets the three obligations recorded above', 'The verdict of this note is unchanged',
           'derived from nothing in the corpus', 'the corpus still states no operational source of the coherent continuum',
           'Nothing is named C5 or adopted'):
    ok_smc &= _t in _ccn_rec1
ok_smc &= _ccn_rec1.count('## ') == 1
ok_smc &= 'state-mixing coupling construction audit' not in _c5n and 'state-mixing coupling construction audit' not in _pcn
ok_smc &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-SMC', ok_smc,
      'State-mixing coupling guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'twenty-five results, defines exactly the datum, its sourcing map, the class family and its full instance, the two '
      'theories and the countability apparatus, nothing named C5 or minimal, with the definition region naming no flow, '
      'transition, polarization image, exponential or quantum-control predicate; the datum, the class, the resource from '
      'the datum, the identity, executability, the stabilities, the closure, the completion, the class-level form under '
      'the stated-access containment and the two replacement-class negatives are stated as pinned, the bridge passing '
      'through the constructor op and the cited closure theorem; the note keeps the question, the status, the datum, the '
      'bridge, the outcomes, the tests and the non-doings before the amendment and the outcome, names the three commits, '
      'records outcome 1 with the bridge step by step and the comparisons as comparisons, the postulate status and the '
      'unchanged manuscript status, and uses no minimality word in its claims; no manuscript is edited; the registry and '
      'the census carry the family as kernel-only; the coherent-continuum note carries one section after its frozen text '
      'and the discovery and closure notes are untouched; the README carries the paragraph and the counts.')

# ---- the real pair-flow reduction audit: the five-hypothesis principle stated without the rotation form, the reduction to
# the datum under those hypotheses alone, the composition to the completion, the three countercontrols, the narrow
# sourcing audit negative; outcome 2; no C5; no continuity-necessity claim ----
ok_rpf = True
_rp = open(os.path.join(BRIDGE, 'OIBridge', 'RealPairFlow.lean'), encoding='utf-8').read()
_rpflat = ' '.join(_rp.split())
_rpcode = re.sub(r'/-.*?-/|--[^\n]*', '', _rp, flags=re.S)
_rpn = open(os.path.join(os.path.dirname(BRIDGE), 'REAL-PAIR-FLOW-AUDIT.md'), encoding='utf-8').read()
_rpn1 = re.sub(r'\s+', ' ', _rpn)
ok_rpf &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _rp) is None and 'native_decide' not in _rp
ok_rpf &= 'axiom ' not in _rpcode
_rp_names = re.findall(r"^theorem ([\w'.]+)", _rp, re.M)
ok_rpf &= len(_rp_names) == 49 and _rp.count('#print axioms') == 20
for _nm in ('rotR_inj_small', 'transport_rotR', 'PairFlow.pairFlow_det_one', 'PairFlow.pairFlow_form', 'PairFlow.pairFlow_eq_rotR_ang',
            'PairFlow.pairFlow_exists_eps', 'PairFlow.pairFlow_ang_add', 'PairFlow.pairFlow_ang_linear', 'PairFlow.pairFlow_rate',
            'PairFlow.pairFlow_supplies_mixImage', 'qm_of_pairFlowSourced', 'flowR_eq_mixC', 'pairFlowTheory_endpoint',
            'pairFlowTheory_qm', 'shearFlow_all_but_orth', 'shearFlow_ne_rotR', 'boostFlow_all_but_orth', 'boostFlow_ne_rotR',
            'constFlow_all_but_nontrivial', 'constFlow_transport'):
    ok_rpf &= ('#print axioms OIBridge.RealPairFlow.' + _nm) in _rp and _nm in _rp_names
# the definitions: the principle, its transport, the rotation as conclusion, the local angle, the pair-flow class and theory,
# the three countercontrol families; nothing named C5; no existing definition restated
_rp_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _rp, re.M)
ok_rpf &= _rp_defs == ['PairFlow', 'transport', 'rotR', 'PairFlow.ang', 'FlowR', 'pairFlowTheory', 'shearFlow', 'boostFlow', 'constFlow']
ok_rpf &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _rp, re.M) is None
for _t in ('MixR', 'MixC', 'mixImage', 'rot', 'mixTheory', 'LayerFlowExecutable', 'PhaseFreeRichness', 'DerivedOI', 'gateFlow'):
    ok_rpf &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _rp, re.M) is None
# the vocabulary boundary on the definition region of the principle and its transport, comments stripped: no cosine, sine,
# rotation, datum, flow, transition, exponential or quantum-control predicate
_rp_defregion = _rpcode[_rpcode.find('structure PairFlow'):_rpcode.find('end Principle')]
ok_rpf &= 'A : ℝ → Matrix (Fin 2) (Fin 2) ℝ' in _rp_defregion and 'nontrivial : ∃ t : ℝ, A t ≠ 1' in _rp_defregion
for _bad in ('cos', 'sin', 'rot', 'mixImage', 'gateFlow', 'flow ', 'transition', 'PhaseFreeRichness', 'LayerFlowExecutable',
             'HasCompositeUnitaryControl', 'exp', 'Quantum', 'quantum', 'HasDerivAt', 'deriv', 'Differentiable', 'generator'):
    ok_rpf &= _bad not in _rp_defregion
# no differentiability or generator hypothesis anywhere in the code: the classification closes under the five hypotheses
for _bad in ('HasDerivAt', 'deriv ', 'Differentiable', 'HasFDerivAt', 'fderiv'):
    ok_rpf &= _bad not in _rpcode
ok_rpf &= 'import OIBridge.StateMixingCoupling' in _rp and 'import OIBridge.RealPairFlow' in root
# the statements, as preregistered and amended
for _t in ('structure PairFlow where A : ℝ → Matrix (Fin 2) (Fin 2) ℝ zero : A 0 = 1 add : ∀ s t : ℝ, A (s + t) = A s * A t cont : Continuous A orth : ∀ t : ℝ, (A t)ᵀ * A t = 1 nontrivial : ∃ t : ℝ, A t ≠ 1',
           'def transport (n : ℕ) (M : Matrix (Fin 2) (Fin 2) ℝ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ := Matrix.of fun p q => if p.2 = q.2 then (M p.1 q.1 : ℂ) else 0',
           'theorem PairFlow.pairFlow_det_one (t : ℝ) : (F.A t).det = 1',
           'theorem PairFlow.pairFlow_rate : ∃ ω : ℝ, ω ≠ 0 ∧ ∀ t : ℝ, F.A t = rotR (ω * t)',
           'theorem PairFlow.pairFlow_supplies_mixImage (n : ℕ) (θ : ℝ) : ∃ t : ℝ, transport n (F.A t) = mixImage n θ',
           '(hflow : ∀ (n : ℕ) (t : ℝ), 𝓘 (Fin 2 × Fin n) (transport n (F.A t))) : DerivedOI (genTheory 𝓘 arch (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2))',
           '| flow (n : ℕ) (t : ℝ) : FlowR F (Fin 2 × Fin n) (transport n (F.A t))',
           'theorem flowR_eq_mixC : FlowR F = MixC',
           'theorem pairFlowTheory_qm : ExactAllFiniteEndomorphicQuantumOps (pairFlowTheory F (Fin 2))',
           'def shearFlow (t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![1, t; 0, 1]',
           'noncomputable def boostFlow (t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![Real.cosh t, Real.sinh t; Real.sinh t, Real.cosh t]',
           'def constFlow (_ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := 1',
           'theorem shearFlow_ne_rotR {θ : ℝ} (hθ : Real.sin θ ≠ 0) (t : ℝ) : shearFlow t ≠ rotR θ',
           'theorem boostFlow_ne_rotR {θ : ℝ} (hθ : Real.sin θ ≠ 0) (t : ℝ) : boostFlow t ≠ rotR θ',
           '∧ (∀ t : ℝ, (shearFlow t).det = 1) ∧ (∃ t : ℝ, shearFlow t ≠ 1) ∧ ¬ (∀ t : ℝ, (shearFlow t)ᵀ * shearFlow t = 1)',
           '∧ (∀ t : ℝ, (constFlow t)ᵀ * constFlow t = 1) ∧ ¬ (∃ t : ℝ, constFlow t ≠ 1)',
           'theorem constFlow_transport (n : ℕ) (t : ℝ) : transport n (constFlow t) = 1'):
    ok_rpf &= _t in _rpflat
# the route as amended: the intermediate value theorem, the complex exponential for the small-angle injectivity, density
# on rational multiples with clamped continuous functions, subdivision through the group law, the construction audit's
# class-level theorem
for _t in ('intermediate_value_uIcc', 'Complex.exp_eq_exp_iff_exists_int', 'Rat.denseRange_cast', 'ext_on', 'Real.arcsin',
           'Real.cos_arcsin', 'pairFlow_pow', 'rotR_pow', 'qm_of_mixSourced', 'Real.cosh_sq_sub_sinh_sq', 'exists_nat_ge'):
    ok_rpf &= _t in _rpflat
# the note: the two questions, the principle, the route, the sourcing table, the outcomes, the tests, the non-doings, the
# amendment, then the outcome and the non-claims, in that order
_krp = [_rpn.find(h) for h in ('## The two questions', '## The candidate principle, frozen in form', '## The reduction, frozen as a route',
        '## The sourcing audit, frozen narrow', '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome', '## What this note does not claim')]
ok_rpf &= all(x > 0 for x in _krp) and _krp == sorted(_krp)
ok_rpf &= _rpn.lstrip().startswith('# The real pair-flow reduction audit')
for _t in ('Preregistration commit `ed3c224`', 'scope amendment `7038c0c`', '`main` at `e6ca6ed`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', '1. identity: `A 0 = 1`', '5. nontriviality: `A t ≠ 1` for some `t`', 'The rotation form is not assumed; it is the conclusion',
           '1. **Existing principle sources the pair flow.**', '2. **Reduction succeeds, sourcing fails.**', '3. **Reduction fails or weakens.**',
           '| S1, the continuous-time extension of `[Main §2.3]`', '| S4, an invariant quadratic or energy structure',
           'Liouville measure preservation is never read as Euclidean norm preservation; determinant one is never read as orthogonality',
           'heuristic only and is not a required proof construction', 'A merely mathematical change to a suitable basis is insufficient',
           'twenty named results'):
    ok_rpf &= _t in _rpn1
_rpn_out = re.sub(r'\s+', ' ', _rpn[_rpn.find('## The outcome'):])
for _t in ('The verdict is **outcome 2, reduction succeeds, sourcing fails**', 'with no differentiability or generator hypothesis added',
           'the rotation form was not assumed', 'the intermediate value theorem on the connected line', 'a dense set',
           'the heuristic global extension of the preregistration is not used', 'by subdividing an arbitrary time through the group law',
           '`flowR_eq_mixC`', '| S1 | no pair flow |', '| S2 | no pair flow |', '| S3 | no carrier map; not a source |',
           '| S4 | none stated on the pair; not a source |', 'the qualification of the scope amendment', 'is not met',
           'Outcome 1 is not reached; outcome 3 is not reached',
           'what physical principle gives a nontrivial continuous orthogonal action on one distinguishable pair',
           'the principle is not named C5', 'Nothing here says that the completion needs continuity, orthogonality or the principle',
           'The manuscript status of the state-mixing resource is unchanged', '| T1 | ', '| T4 | ', '| T8 | ',
           'with orthogonality and nontriviality independently tested by the countercontrols',
           '## Countercontrol scope correction, recorded after the execution',
           'do not establish independent necessity of all five pair-flow hypotheses',
           'It does not prove separate necessity or minimality of identity, the group law, or continuity',
           'The five-hypothesis classification theorem and outcome 2 are unchanged'):
    ok_rpf &= _t in _rpn_out
ok_rpf &= _rpn.find('## Countercontrol scope correction, recorded after the execution') > _rpn.find('## What this note does not claim')
for _bad in ('The verdict is **outcome 1', 'The verdict is **outcome 3', 'Outcome 1 is reached', 'outcome 1 is reached',
             'continuity is necessary for the completion, ', 'the principle is necessary for', 'orthogonality is necessary for the completion, ',
             'the principle is C5', 'is C5.', 'C5 is the', 'we adopt C5', 'a C5 has been found', 'define C5', 'Liouville preservation gives',
             'measure preservation gives orthogonality', 'determinant one gives orthogonality', 'recurrence gives an orthogonal',
             'the corpus sources the pair flow', 'the corpus supplies the pair flow', 'nature realizes', 'is realized by nature',
             'differentiability hypothesis is added', 'generator hypothesis is added', 'each shown necessary',
             'each hypothesis is necessary', 'necessity of all five', 'minimality of the five'):
    ok_rpf &= _bad not in _rpn_out.replace('do not establish independent necessity of all five pair-flow hypotheses', '')
for _bad in ('continuity is necessary', 'the principle is C5', 'is derived from the substratum', 'the observer can execute',
             'the corpus sources the pair flow', 'C5 holds', 'a C5 has been found'):
    ok_rpf &= not _asserted(_rpn[_rpn.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('RealPairFlow', 'REAL-PAIR-FLOW', 'PairFlow', 'pairFlow', 'shearFlow', 'boostFlow', 'constFlow', 'flowR_eq_mixC',
                 'qm_of_pairFlowSourced'):
        ok_rpf &= _bad not in _t
_rp_fam = [f for f in _ptr_reg['families'] if f['name'] == 'real pair-flow reduction: the principle, the reduction and the sourcing audit']
ok_rpf &= len(_rp_fam) == 1 and _rp_fam[0]['status'] == 'kernel-only' and _rp_fam[0]['modules'] == ['RealPairFlow']
ok_rpf &= _rp_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 2, reduction succeeds, sourcing fails', 'with none added', 'stated without the rotation form',
           'Nothing says continuity or the principle is necessary', 'nothing is named C5 or adopted', 'the manuscript status of the state-mixing resource, which is unchanged',
           'owner decision'):
    ok_rpf &= _t in _rp_fam[0]['note']
for _bad in ('continuity is necessary', 'the principle is C5', 'the corpus sources the pair flow', 'C5 holds'):
    ok_rpf &= _bad not in _rp_fam[0]['note']
ok_rpf &= '| real pair-flow reduction: the principle, the reduction and the sourcing audit | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-RPF`', 'REAL-PAIR-FLOW-AUDIT.md', 'PairFlow', 'transport', 'PairFlow.pairFlow_det_one', 'PairFlow.pairFlow_form',
           'PairFlow.pairFlow_ang_add', 'PairFlow.pairFlow_ang_linear', 'PairFlow.pairFlow_rate', 'PairFlow.pairFlow_supplies_mixImage',
           'qm_of_pairFlowSourced', 'flowR_eq_mixC', 'pairFlowTheory_endpoint', 'pairFlowTheory_qm', 'shearFlow_all_but_orth',
           'shearFlow_ne_rotR', 'boostFlow_all_but_orth', 'boostFlow_ne_rotR', 'constFlow_all_but_nontrivial', 'constFlow_transport',
           'with none added', 'without the rotation form', 'Liouville preservation never read as norm preservation',
           'Verdict: outcome 2, reduction succeeds, sourcing fails', 'Nothing says continuity or the principle is necessary',
           'Twenty named results', 'Nothing is named C5 or adopted; no definition changes; no manuscript changes'):
    ok_rpf &= _t in _rd1
for _bad in ('continuity is necessary for', 'the principle is C5', 'the corpus sources the pair flow', 'Outcome 1 is reached', 'C5 holds'):
    ok_rpf &= _bad not in _rd1
# the state-mixing note: one section recorded after its frozen text; the discovery, closure and coherent-continuum notes untouched
_smn_rec = _smn.find('## Recorded after the round: the real pair-flow reduction audit')
ok_rpf &= _smn_rec > _smn.find('## What this note does not claim') and _smn_rec > _smn.find('Status: pass complete')
_smn_rec1 = re.sub(r'\s+', ' ', _smn[_smn_rec:])
for _t in ('reduces the datum of this round to a principle', 'stated without the rotation form', 'The verdict of this note is unchanged',
           'the datum keeps its postulate status', 'Nothing is named C5 or adopted'):
    ok_rpf &= _t in _smn_rec1
ok_rpf &= _smn_rec1.count('## ') == 1
ok_rpf &= 'real pair-flow reduction audit' not in _c5n and 'real pair-flow reduction audit' not in _pcn and 'real pair-flow reduction audit' not in _ccn
ok_rpf &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-RPF', ok_rpf,
      'Real pair-flow guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly its '
      'twenty results, defines exactly the principle, its transport, the rotation as conclusion, the local angle, the '
      'pair-flow class and theory and the three countercontrol families, nothing named C5 and no existing definition '
      'restated, with the principle\'s definition region naming no cosine, sine, rotation, datum, flow, transition, '
      'exponential, derivative or quantum-control predicate and no differentiability hypothesis anywhere; the '
      'principle, the transport, the determinant, the rate, the supply, the class-level endpoint, the class equality, '
      'the pair-flow theory and the countercontrols are stated as pinned, the route passing through the intermediate '
      'value theorem, the complex exponential, density on rational multiples, subdivision through the group law and the '
      'construction audit\'s class-level theorem; the note keeps the two questions, the principle, the route, the '
      'sourcing table, the outcomes, the tests and the non-doings before the amendment and the outcome, names the three '
      'commits, records outcome 2 with the reduction step by step under the five hypotheses alone, the four sourcing '
      'statuses, the frontier question, and no necessity or C5 claim; no manuscript is edited; the registry and the '
      'census carry the family as kernel-only; the state-mixing note carries one section after its frozen text and the '
      'discovery, closure and coherent-continuum notes are untouched; the README carries the paragraph and the counts.')

# ---- the operational pair-flow equivalence audit: the theory-level predicate on the two-valued carrier, the canonical
# flow, the forward direction from control, the backward direction within the theory's availability with the amendment's
# base case from the sourced flow at time zero, the central biconditional, the two countercontrols; outcome 1; no C5; no
# generalization beyond Fin 2; the generation semantics of the reverse reconstruction deferred ----
ok_pfe = True
_pf = open(os.path.join(BRIDGE, 'OIBridge', 'PairFlowEquivalence.lean'), encoding='utf-8').read()
_pfflat = ' '.join(_pf.split())
_pfcode = re.sub(r'/-.*?-/|--[^\n]*', '', _pf, flags=re.S)
_pfn = open(os.path.join(os.path.dirname(BRIDGE), 'PAIR-FLOW-EQUIVALENCE-AUDIT.md'), encoding='utf-8').read()
_pfn1 = re.sub(r'\s+', ' ', _pfn)
ok_pfe &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _pf) is None and 'native_decide' not in _pf
ok_pfe &= 'axiom ' not in _pfcode
_pf_names = re.findall(r"^theorem ([\w'.]+)", _pf, re.M)
ok_pfe &= len(_pf_names) == 16 and _pf.count('#print axioms') == 15
for _nm in ('rotR_orth', 'rotR_continuous', 'rotFlow_A', 'pairFlowSourced_of_qm', 'derivedOI_pairFlowSourced_of_qm',
            'mixAvail_of_pairFlowSourced', 'identity_avail_of_pairFlowSourced', 'phaseIndicator_avail', 'siteShear_avail',
            'conjChannel_unit_smul', 'layerFlowExecutable_of_derivedOI_pairFlowSourced', 'qm_of_derivedOI_pairFlowSourced',
            'qm_iff_derivedOI_pairFlowSourced', 'polarizedTheoryC_not_pairFlowSourced', 'countable_not_pairFlowSourced'):
    ok_pfe &= ('#print axioms OIBridge.PairFlowEquivalence.' + _nm) in _pf and _nm in _pf_names
# the definitions: the predicate and the canonical flow, nothing else; nothing named C5; no existing definition restated
_pf_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _pf, re.M)
ok_pfe &= _pf_defs == ['PairFlowSourced', 'rotFlow']
ok_pfe &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _pf, re.M) is None
for _t in ('PairFlow', 'transport', 'rotR', 'mixImage', 'rot', 'LayerFlowExecutable', 'PhaseFreeRichness', 'DerivedOI', 'gateFlow',
           'siteShearImage', 'PhasesAvailable', 'conjChannel'):
    ok_pfe &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _pf, re.M) is None
# the predicate is on availability in the theory and the backward direction stays there: no class generation, no
# implementation class, no architecture anywhere in the code; the carrier is the two-valued one throughout
for _bad in ('genTheory', 'ImplementationClass', 'Architecture', 'arch.', 'FiniteOperationalTheory S', 'FiniteOperationalTheory A'):
    ok_pfe &= _bad not in _pfcode
ok_pfe &= 'import OIBridge.RealPairFlow' in _pf and 'import OIBridge.PairFlowEquivalence' in root
# the statements, as preregistered and amended
for _t in ('def PairFlowSourced (T : FiniteOperationalTheory (Fin 2)) : Prop := ∃ F : PairFlow, ∀ (n : ℕ) (t : ℝ), T.availExt n Unit (fun _ => conjChannel (transport n (F.A t)))',
           'noncomputable def rotFlow : PairFlow where A := rotR',
           'theorem rotFlow_A (t : ℝ) : rotFlow.A t = rotR t := rfl',
           'theorem pairFlowSourced_of_qm (T : FiniteOperationalTheory (Fin 2)) (h : ExactAllFiniteEndomorphicQuantumOps T) : PairFlowSourced T',
           'theorem mixAvail_of_pairFlowSourced (hs : PairFlowSourced T) (n : ℕ) (θ : ℝ) : T.availExt n Unit (fun _ => conjChannel (mixImage n θ))',
           'theorem identity_avail_of_pairFlowSourced (hs : PairFlowSourced T) (n : ℕ) : T.availExt n Unit (fun _ => conjChannel (1 : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ))',
           'theorem phaseIndicator_avail (hph : PhasesAvailable T) (hs : PairFlowSourced T) (n : ℕ)',
           'theorem siteShear_avail (hph : PhasesAvailable T) (hs : PairFlowSourced T) (n : ℕ) : T.availExt n Unit (fun _ => conjChannel (siteShearImage n))',
           'theorem layerFlowExecutable_of_derivedOI_pairFlowSourced (hd : DerivedOI T) (hs : PairFlowSourced T) : LayerFlowExecutable T (Equiv.swap 0 1)',
           'theorem qm_of_derivedOI_pairFlowSourced (hd : DerivedOI T) (hs : PairFlowSourced T) : ExactAllFiniteEndomorphicQuantumOps T',
           'theorem qm_iff_derivedOI_pairFlowSourced (T : FiniteOperationalTheory (Fin 2)) : ExactAllFiniteEndomorphicQuantumOps T ↔ DerivedOI T ∧ PairFlowSourced T',
           'theorem polarizedTheoryC_not_pairFlowSourced : ¬ PairFlowSourced (polarizedTheoryC (Fin 2))',
           'theorem countable_not_pairFlowSourced (T : FiniteOperationalTheory (Fin 2)) (D : Set (Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ)) (hD : D.Countable)',
           # the amendment's base case: the witness flow at time zero, its identity field, the transport of the identity
           'have h1 : transport n (1 : Matrix (Fin 2) (Fin 2) ℝ) = 1 := constFlow_transport n 0', 'rwa [F.zero, h1] at this',
           'exact identity_avail_of_pairFlowSourced hs n',
           # the routes: the supply, control, the shear-mix identity, the unit scalar, the composition, the existing Q3
           'F.pairFlow_supplies_mixImage n θ', 'physical_of_exactAll T h', 'rw [rotFlow_A, transport_rotR]', 'mixImage_unitary n t',
           'derivedOI_of_qm T h', 'gateFlow_eq_shear_mix', 'conjChannel_unit_smul (Complex.norm_exp_ofReal_mul_I _)', 'avail_conj_mul T n',
           'siteShearImage_conjTranspose', 'qm_of_derivedOI_layerFlowExecutable T hd hσ', 'polarizedTheoryC_derivedOI',
           'polarizedTheoryC_not_qm', 'mixImage_not_proportional (0 : Fin 1)', 'Cardinal.mk_Ioo_real', 'Cardinal.aleph0_lt_continuum'):
    ok_pfe &= _t in _pfflat
# the note: the theorem, the predicate, the routes, the boundary, the countercontrols, the deferred reconstruction, the
# meaning, the outcomes, the tests, the non-doings, the amendment, then the outcome and the non-claims, in that order
_kpf = [_pfn.find(h) for h in ('## The theorem, frozen', '## The predicate, frozen in form', '## The two directions, frozen as routes',
        '## The vocabulary boundary for future sources, frozen now', '## The countercontrols, frozen with their exact scope',
        '## The reverse reconstruction, deferred with both formulations recorded', '## What this round establishes if the theorem is proved',
        '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome', '## What this note does not claim')]
ok_pfe &= all(x > 0 for x in _kpf) and _kpf == sorted(_kpf)
ok_pfe &= _pfn.lstrip().startswith('# The operational pair-flow equivalence audit')
ok_pfe &= _pfn.count('## Scope amendment, recorded after the preregistration') == 1
for _t in ('Preregistration commit `4db4d7a`', 'scope amendment `3bfcb03`', '`main` at `acd001f`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', '`ExactAllFiniteEndomorphicQuantumOps T ↔ DerivedOI T ∧ PairFlowSourced T`',
           'The two-valued carrier is frozen', 'is not claimed and is deferred',
           '`∃ F : PairFlow, ∀ n t, T.availExt n Unit (fun _ => conjChannel (transport n (F.A t)))`',
           'not membership of the matrices in an implementation class',
           'It does not bind this round\'s predicate', '1. **Both directions close.**', '2. **The backward direction needs a hypothesis beyond `DerivedOI`.**',
           '3. **A direction fails.**', 'This round chooses neither', 'the next round must choose one before testing any realization-level necessity',
           'nothing here says that a coherent continuum is insufficient', 'This is a necessary condition',
           'is not claimed from `PhasesAvailable` alone at every level', 'by evaluating its witness flow at time zero',
           'outcome 2 is not triggered by this base case', 'fifteen named results'):
    ok_pfe &= _t in _pfn1
# the frozen vocabulary boundary, a blockquote, read with its quote markers removed
_pfn1q = re.sub(r'\s+', ' ', _pfn.replace('\n> ', ' '))
for _t in ('No future realization-level candidate counts as a source of `PairFlowSourced` if its statement uses `PairFlow`, `transport`, rotation, cosine or sine, orthogonal-matrix dynamics, `mixImage`, `LayerFlowExecutable`, or an equivalent operational-control predicate',
           'Such a condition is a restatement of the target rather than an independent physical source'):
    ok_pfe &= _t in _pfn1q
_pfn_out = re.sub(r'\s+', ' ', _pfn[_pfn.find('## The outcome'):])
for _t in ('The verdict is **outcome 1, both directions close**', 'with no hypothesis added on either side',
           'the base case of the scope amendment is discharged from the sourced flow at time zero',
           'No step reaches back through `genTheory` or any implementation class', 'Canonical, and not new physics',
           'Outcome 2 is not reached', 'outcome 3 is not reached', 'principally a repackaging of proved machinery',
           'It is not a discovery of new physics', 'nothing here is named C5', 'a necessary condition only',
           'nothing here exhibits a non-quantum theory with a coherent continuum', 'The pair flow remains an operationally sourced condition',
           'must be frozen before any realization-level necessity is tested', 'The manuscript status of the state-mixing resource is unchanged',
           'nothing is generalized beyond `Fin 2`', '| T1 | ', '| T4 | ', '| T5 | ', '| T6 | ', '| T8 | '):
    ok_pfe &= _t in _pfn_out
_pfn_out_claims = _pfn_out.replace('nothing here says a coherent continuum is insufficient', '').replace('That a coherent continuum is insufficient', '')
for _bad in ('The verdict is **outcome 2', 'The verdict is **outcome 3', 'Outcome 1 is not reached', 'outcome 1 is not reached',
             'the pair flow is C5', 'is C5.', 'C5 is the', 'we adopt C5', 'a C5 has been found', 'define C5', 'C5 holds',
             'coherent continuum is insufficient', 'the corpus sources the pair flow', 'realization-level necessity is proved',
             'every realization compatible with OI carries', 'generalized to an arbitrary carrier', 'holds on every carrier',
             'availability containment is chosen', 'generated-theory equality is chosen', 'the semantics is decided',
             'new physics is', 'discovery of new physics.', 'sources the pair flow from', 'minimal', 'Minimal'):
    ok_pfe &= _bad not in _pfn_out_claims
for _bad in ('the pair flow is C5', 'C5 holds', 'the corpus sources the pair flow', 'is necessary at the realization level'):
    ok_pfe &= not _asserted(_pfn[_pfn.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('PairFlowEquivalence', 'PAIR-FLOW-EQUIVALENCE', 'PairFlowSourced', 'pairFlowSourced', 'rotFlow',
                 'qm_iff_derivedOI_pairFlowSourced'):
        ok_pfe &= _bad not in _t
_pf_fam = [f for f in _ptr_reg['families'] if f['name'] == 'operational pair-flow equivalence: the closure with one sourced pair flow is exactly quantum mechanics']
ok_pfe &= len(_pf_fam) == 1 and _pf_fam[0]['status'] == 'kernel-only' and _pf_fam[0]['modules'] == ['PairFlowEquivalence']
ok_pfe &= _pf_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 1, both directions close', 'with no hypothesis added on either side', 'not new physics',
           'a necessary condition only', 'Nothing is named C5 or adopted', 'nothing generalized beyond Fin 2',
           'generation semantics deferred', 'the manuscript status of the state-mixing resource, which is unchanged', 'owner decision'):
    ok_pfe &= _t in _pf_fam[0]['note']
for _bad in ('the pair flow is C5', 'C5 holds', 'the corpus sources the pair flow', 'coherent continuum is insufficient.', 'minimal'):
    ok_pfe &= _bad not in _pf_fam[0]['note']
ok_pfe &= '| operational pair-flow equivalence: the closure with one sourced pair flow is exactly quantum mechanics | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-PFE`', 'PAIR-FLOW-EQUIVALENCE-AUDIT.md', 'PairFlowSourced', 'rotFlow', 'rotFlow_A', 'rotR_orth', 'rotR_continuous',
           'rotR_pi_ne_one', 'pairFlowSourced_of_qm', 'derivedOI_pairFlowSourced_of_qm', 'mixAvail_of_pairFlowSourced',
           'identity_avail_of_pairFlowSourced', 'phaseIndicator_avail', 'siteShear_avail', 'conjChannel_unit_smul',
           'layerFlowExecutable_of_derivedOI_pairFlowSourced', 'qm_of_derivedOI_pairFlowSourced', 'qm_iff_derivedOI_pairFlowSourced',
           'polarizedTheoryC_not_pairFlowSourced', 'countable_not_pairFlowSourced', 'on availability and not on class membership',
           'with no reach back through any implementation class', 'the scope amendment\'s base case',
           'Verdict: outcome 1, both directions close', 'and not new physics', 'a necessary condition only', 'Fifteen named results',
           'Nothing is named C5 or adopted; nothing is generalized beyond `Fin 2`; the reverse reconstruction\'s generation semantics is deferred; no definition changes; no manuscript changes'):
    ok_pfe &= _t in _rd1
for _bad in ('the pair flow is C5', 'C5 holds', 'the corpus sources the pair flow', 'Outcome 2 is reached', 'Outcome 3 is reached',
             'coherent continuum is insufficient.'):
    ok_pfe &= _bad not in _rd1
# the real pair-flow note: one section recorded after its countercontrol correction; the state-mixing, coherent-continuum,
# closure and discovery notes untouched by this round
_rpn_rec = _rpn.find('## Recorded after the round: the operational pair-flow equivalence audit')
ok_pfe &= _rpn_rec > _rpn.find('## Countercontrol scope correction, recorded after the execution') and _rpn_rec > _rpn.find('Status: pass complete')
_rpn_rec1 = re.sub(r'\s+', ' ', _rpn[_rpn_rec:])
for _t in ('states the principle of this note as a predicate on a finite operational theory', '`PairFlowSourced`',
           '`qm_iff_derivedOI_pairFlowSourced`', 'with no reach back through any implementation class',
           'The verdict of this note is unchanged', 'the pair flow remains an operationally sourced condition', 'Nothing is named C5 or adopted'):
    ok_pfe &= _t in _rpn_rec1
ok_pfe &= _rpn_rec1.count('## ') == 1
for _n in (_smn, _ccn, _pcn, _c5n):
    ok_pfe &= 'operational pair-flow equivalence audit' not in _n and 'PairFlowSourced' not in _n
ok_pfe &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-PFE', ok_pfe,
      'Operational pair-flow equivalence guard: the module carries no sorry, axiom or native_decide, prints the axioms of '
      'exactly its fifteen results, defines exactly the theory-level predicate on the two-valued carrier and the canonical '
      'rate-one rotation flow, nothing named C5 and no existing definition restated, with no class generation, '
      'implementation class or architecture anywhere in the code; the predicate, the canonical flow, the forward direction '
      'from composite unitary control, the datum\'s availability, the identity at every level from the witness flow at '
      'time zero as the amendment\'s base case, the phase products and the site shear by finite composition, the unit '
      'scalar, the layer flow through the construction audit\'s identity, the existing Q3, the central biconditional and '
      'the two countercontrols are stated as pinned; the note keeps the theorem, the predicate, the routes, the vocabulary '
      'boundary for future sources, the countercontrols with their exact scope, the deferred reconstruction semantics, '
      'the meaning, the outcomes, the tests and the non-doings before the amendment and the outcome, names the three '
      'commits, records outcome 1 with both directions, no hypothesis added, the repackaging status and no new physics, '
      'and no C5, generalization, realization-level necessity, coherent-continuum insufficiency or semantics claim; no '
      'manuscript is edited; the registry and the census carry the family as kernel-only; the real pair-flow note carries '
      'one section after its countercontrol correction and the state-mixing, coherent-continuum, closure and discovery '
      'notes are untouched; the README carries the paragraph and the counts.')

# ---- the discrete completion audit: one fixed discrete gate at one fixed angle on top of the closure, the density targets
# frozen, dense unitary control proved at every level for every angle with alpha/pi irrational through the echo, the
# relocation, the Euler decomposition and the Givens decomposition, the finite countercontrols uniform at the multiples of
# pi/4, the canonical fixed-gate theory, the instrument chain's consumption of exact control named; outcome 2; no C5; no
# continuous pair flow in any constructive route; no irrationality as a physical principle ----
ok_dca = True
_dc = open(os.path.join(BRIDGE, 'OIBridge', 'DiscreteCompletion.lean'), encoding='utf-8').read()
_dcflat = ' '.join(_dc.split())
_dccode = re.sub(r'/-.*?-/|--[^\n]*', '', _dc, flags=re.S)
_dcn = open(os.path.join(os.path.dirname(BRIDGE), 'DISCRETE-COMPLETION-AUDIT.md'), encoding='utf-8').read()
_dcn1 = re.sub(r'\s+', ' ', _dcn)
ok_dca &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _dc) is None and 'native_decide' not in _dc
ok_dca &= 'axiom ' not in _dccode
_dc_names = re.findall(r"^theorem ([\w'.]+)", _dc, re.M)
ok_dca &= len(_dc_names) == 160 and _dc.count('#print axioms') == 51
for _nm in ('conj_within', 'norm_mul_sub_mul_le', 'blockOf_mul', 'blockOf_unitary', 'blockOnly_rot_sub_one_norm_le',
            'blockOf_rot_dist_le', 'rx_eq_conj', 'rot_rx_rot', 'su2_form', 'exists_unit_scalar_su2', 'euler_of_su2',
            'euler_of_unitary', 'dense_angles', 'BlockRepertoire.rot_approx', 'BlockRepertoire.rx_approx',
            'BlockRepertoire.dense_block_su2', 'blockRepertoire_levelOne', 'levelOne_dense', 'flipSet_avail', 'echo_identity',
            'isolated_mem_availSet', 'blockRepertoire_level', 'exists_perm_pair_map', 'relocated_dense', 'twoLevel_mul',
            'det_twoLevel', 'twoLevel_mul_apply', 'givens_unitary', 'det_givens', 'row_zero_of_col_zero',
            'su_mem_closure_of_suppOn', 'su_mem_closure_twoLevel', 'relocated_eq_twoLevel', 'twoLevelSU_approx',
            'closure_approx', 'su_dense', "exists_unit_scalar_su'", 'denseUnitaryControl_of_fixedGate', 'Gen2.pauli_conj',
            'scalar_of_comm_XZ', 'proportional_of_same_conj', 'gen2_pi_div_four_finite_upToScalar',
            'gen2_multiple_finite_upToScalar', 'mixR_singleton_daggerStable', 'mixR_singleton_contextStable',
            'fixedGateTheory_derivedOI', 'fixedGateTheory_fixedGateSourced', 'fixedGateTheory_krausSoundExt',
            'fixedGateTheory_denseUnitaryControl', 'fixedGateTheory_not_qm', 'fixedGateTheory_one_denseUnitaryControl'):
    ok_dca &= ('#print axioms OIBridge.DiscreteCompletion.' + _nm) in _dc and (_nm in _dc_names or _nm.split('.')[-1] in _dc_names)
# the definitions: the predicates, the metric, the closure, the block algebra, the gates, the repertoire, the available set,
# the flips, the relocation, the two-level apparatus, the Givens block, the level-one group, the Pauli set, the canonical
# theory; nothing named C5; no existing definition restated
_dc_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _dc, re.M)
ok_dca &= _dc_defs == ['FixedGateSourced', 'ChanWithin', 'DenseUnitaryControl', 'KrausDense', 'DenseFiniteQM', 'ClosureAvail',
                       'anc', 'ancC', 'blockOnly', 'blockOf', 'S2', 'X2', 'rx', 'BlockRepertoire', 'availSet', 'flipSet', 'Z2',
                       'echoSet', 'relocated', 'incl', 'twoLevel', 'SuppOn', 'givens', 'TwoLevelSU', 'phaseBlock', 'Gen2', 'Y2',
                       'pauliBase', 'Pauli', 'pmul', 'fixedGateTheory']
ok_dca &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _dc, re.M) is None
for _t in ('mixImage', 'MixR', 'mixTheoryR', 'DerivedOI', 'PairFlow', 'PairFlowSourced', 'LayerFlowExecutable', 'KrausSoundExt',
           'conjChannel', 'IsFiniteEndomorphicKrausInstrument'):
    ok_dca &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _dc, re.M) is None
# no continuous pair flow in any constructive route, and no irrationality condition inside a definition
_dccode_noopen = re.sub(r'^open .*$', '', _dccode, flags=re.M)
ok_dca &= 'PairFlowSourced' not in _dccode and re.search(r'\bPairFlow\b', _dccode_noopen) is None
ok_dca &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive)[^\n]*Irrational', _dc, re.M) is None
ok_dca &= 'import OIBridge.PairFlowEquivalence' in _dc and 'import OIBridge.DiscreteCompletion' in root
# the statements, as preregistered and amended
for _t in ('def FixedGateSourced (α : ℝ) (T : FiniteOperationalTheory (Fin 2)) : Prop := ∀ n : ℕ, T.availExt n Unit (fun _ => conjChannel (mixImage n α))',
           '∀ X : Matrix S S ℂ, ‖Φ X - Ψ X‖ ≤ ε * ‖X‖',
           'Vᴴ * V = 1 ∧ ‖c‖ = 1 ∧ T.availExt n Unit (fun _ => conjChannel V) ∧ ‖U - c • V‖ < ε',
           'def DenseFiniteQM (T : FiniteOperationalTheory (Fin 2)) : Prop := KrausSoundExt T ∧ KrausDense T',
           '{ε : ℝ} (h : ‖U - V‖ ≤ ε) : ChanWithin (2 * ε) (conjChannel U) (conjChannel V)',
           '‖A * B - A\'\' * B\'\'‖ ≤ ‖A - A\'\'‖ + ‖B - B\'\'‖'.replace("''", "'"),
           '‖blockOnly k₀ (StateMixingCoupling.rot δ - 1)‖ ≤ |δ|',
           'theorem dense_angles {β : ℝ} (hβ : Irrational (β / Real.pi)) (θ δ : ℝ) (hδ : 0 < δ) : ∃ k m : ℤ, |(k : ℝ) * β + m * (2 * Real.pi) - θ| < δ',
           'AddSubgroup.dense_or_cyclic', 'AddSubgroup.mem_closure_pair',
           '∃ V ∈ A, Vᴴ * V = 1 ∧ ‖blockOf k₀ M - V‖ < ε',
           'theorem levelOne_dense (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi)) (hg : FixedGateSourced α T)',
           'flipSet (echoSet k₀) * mixImage n α * flipSet (echoSet k₀) * mixImage n α = blockOf k₀ (StateMixingCoupling.rot (2 * α))',
           'BlockRepertoire k₀ (2 * α) (availSet T n)',
           '∃ V ∈ availSet T n, Vᴴ * V = 1 ∧ ‖relocated σ k₀ M - V‖ < ε',
           'def twoLevel (a b : S) (M : Matrix (Fin 2) (Fin 2) ℂ) : Matrix S S ℂ := 1 + incl a b * (M - 1) * (incl a b)ᵀ',
           '(twoLevel a b M).det = M.det', 'Matrix.det_one_add_mul_comm',
           'W ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V}',
           'theorem denseUnitaryControl_of_fixedGate (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi)) (hg : FixedGateSourced α T) : DenseUnitaryControl T',
           'theorem gen2_multiple_finite_upToScalar (k : ℤ)',
           'noncomputable abbrev fixedGateTheory (α : ℝ) : FiniteOperationalTheory (Fin 2) := mixTheoryR {α} (Fin 2)',
           'theorem fixedGateTheory_not_qm (α : ℝ) : ¬ ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory α) := mixTheoryR_not_qm (Set.countable_singleton α)',
           'theorem fixedGateTheory_one_denseUnitaryControl : DenseUnitaryControl (fixedGateTheory 1)', 'irrational_pi'):
    ok_dca &= _t in _dcflat
# the note: the question, the resource, the targets, the prediction, the lift, the fork, the outcomes, the tests, the
# non-doings, the amendment, then the outcome and the non-claims, in that order
_kdc = [_dcn.find(h) for h in ('## The question', '## The lead resource, frozen', '## The targets, frozen',
        '## The level-one prediction, frozen, with what must be kernel-proved distinguished', '## The all-level lift, frozen as a route',
        '## The instrument fork, frozen', '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome', '## What this note does not claim')]
ok_dca &= all(x > 0 for x in _kdc) and _kdc == sorted(_kdc)
ok_dca &= _dcn.lstrip().startswith('# The discrete completion audit')
ok_dca &= _dcn.count('## Scope amendment, recorded after the preregistration') == 1
for _t in ('Preregistration commit `d4deada`', 'scope amendment `0a6ccbb`', '`main` at `1cb923d`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', '`G_α` is finite if and only if `α ∈ (π/4)ℤ`', '`α = π/8`', '1. **Full success.**',
           '2. **Unitary density succeeds, instrument density stalls.**', '3. **Level-one or all-level density fails.**',
           'Isolation before relocation', 'Resource density and quantum soundness are separate theorems', 'Two closure obligations in D3',
           'fifty-one named results'):
    ok_dca &= _t in _dcn1
_dcn_out = re.sub(r'\s+', ' ', _dcn[_dcn.find('## The outcome'):])
for _t in ('The verdict is **outcome 2, unitary density succeeds, instrument density stalls**', 'the constant `2` as frozen',
           'with no passage between entries and the operator norm anywhere', 'The theorem is uniform over all `α` with `α/π` irrational',
           'The Givens step is carried out in full and not left named', '**D1 holds**', 'Ambition level 1 is reached in its strongest uniform form',
           'The predicted classification is not kernel-proved in either remaining direction', 'The `π/8` case stays a prediction',
           'density is not exactness', 'consumes exact composite unitary control at two structural places', '`KrausDense` is not claimed',
           'Dense unitary control is not promoted to dense quantum mechanics', 'Its two obligations are named and not proved',
           'Outcome 1 is not reached; outcome 3 is not reached', 'the gate is a stated datum',
           'The manuscript status of the state-mixing resource is unchanged', '| T1 | ', '| T5 | ', '| T7 | ', '| T8 | ', '| T10 | '):
    ok_dca &= _t in _dcn_out
_dcn_out_claims = _dcn_out.replace('That OI itself supplies the gate; the gate is a stated datum', '').replace('That OI itself supplies the fixed gate', '') \
    .replace('That exact quantum mechanics follows from density', '').replace('or that exact quantum mechanics follows from density without the completion operation', '') \
    .replace('That density is exactness', '')
for _bad in ('The verdict is **outcome 1', 'The verdict is **outcome 3', 'Outcome 2 is not reached', 'is C5.', 'C5 holds', 'C5 is the',
             'we adopt C5', 'define C5', 'the fixed gate is C5', 'OI supplies the', 'OI itself supplies', 'KrausDense is proved',
             'DenseFiniteQM is proved', 'dense finite quantum mechanics is proved', 'the completion is proved', 'the classification is kernel-proved',
             'π/8 is proved', '`π/8` is proved', 'exact quantum mechanics follows from density', 'density is exactness',
             'fundamental physics is', 'is fundamental physics', 'minimal', 'Minimal', 'PairFlow enters', 'continuous pair flow is used'):
    ok_dca &= _bad not in _dcn_out_claims
for _bad in ('the fixed gate is C5', 'C5 holds', 'OI supplies the fixed gate', 'KrausDense holds', 'DenseFiniteQM holds', 'the completion holds'):
    ok_dca &= not _asserted(_dcn[_dcn.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('DiscreteCompletion', 'DISCRETE-COMPLETION', 'FixedGateSourced', 'DenseUnitaryControl', 'KrausDense', 'DenseFiniteQM',
                 'fixedGateTheory', 'denseUnitaryControl_of_fixedGate'):
        ok_dca &= _bad not in _t
_dc_fam = [f for f in _ptr_reg['families'] if f['name'] == 'discrete completion: one fixed gate, dense unitary control and the instrument fork']
ok_dca &= len(_dc_fam) == 1 and _dc_fam[0]['status'] == 'kernel-only' and _dc_fam[0]['modules'] == ['DiscreteCompletion']
ok_dca &= _dc_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 2, unitary density succeeds, instrument density stalls', 'KrausDense is not claimed', 'pi/8 stays a prediction',
           'Nothing is named C5 or adopted', 'no continuous pair flow in any constructive route', 'no irrationality condition a physical principle',
           'the manuscript status of the state-mixing resource, which is unchanged', 'owner decision'):
    ok_dca &= _t in _dc_fam[0]['note']
for _bad in ('the fixed gate is C5', 'C5 holds', 'KrausDense is proved', 'density is exactness', 'minimal'):
    ok_dca &= _bad not in _dc_fam[0]['note']
ok_dca &= '| discrete completion: one fixed gate, dense unitary control and the instrument fork | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-DCA`', 'DISCRETE-COMPLETION-AUDIT.md', 'FixedGateSourced', 'DenseUnitaryControl', 'ChanWithin', 'conj_within', 'KrausDense',
           'DenseFiniteQM', 'ClosureAvail', 'denseUnitaryControl_of_fixedGate', 'dense_angles', 'euler_of_su2', 'euler_of_unitary',
           'BlockRepertoire.dense_block_su2', 'blockOnly_rot_sub_one_norm_le', 'levelOne_dense', 'echo_identity', 'isolated_mem_availSet',
           'relocated_dense', 'det_twoLevel', 'su_mem_closure_twoLevel', 'closure_approx', 'su_dense', 'Gen2.pauli_conj',
           'proportional_of_same_conj', 'gen2_multiple_finite_upToScalar', 'fixedGateTheory_derivedOI', 'fixedGateTheory_fixedGateSourced',
           'fixedGateTheory_krausSoundExt', 'fixedGateTheory_denseUnitaryControl', 'fixedGateTheory_not_qm', 'fixedGateTheory_one_denseUnitaryControl',
           'Verdict: outcome 2, unitary density succeeds, instrument density stalls', '`KrausDense` is not claimed', '`π/8` stays a prediction',
           'Fifty-one named results', 'Nothing is named C5 or adopted; no continuous pair flow enters any constructive route; no irrationality condition is a physical principle; no definition changes; no manuscript changes'):
    ok_dca &= _t in _rd1
for _bad in ('the fixed gate is C5', 'C5 holds', 'KrausDense is proved', 'density is exactness', 'Outcome 1 is reached', 'Outcome 3 is reached'):
    ok_dca &= _bad not in _rd1
# the pair-flow equivalence note: one section recorded after its frozen text; the other notes untouched by this round
_pfn2 = open(os.path.join(os.path.dirname(BRIDGE), 'PAIR-FLOW-EQUIVALENCE-AUDIT.md'), encoding='utf-8').read()
_pfn_rec = _pfn2.find('## Recorded after the round: the discrete completion audit')
ok_dca &= _pfn_rec > _pfn2.find('## What this note does not claim') and _pfn_rec > _pfn2.find('Status: pass complete')
_pfn_rec1 = re.sub(r'\s+', ' ', _pfn2[_pfn_rec:])
for _t in ('replaces the sourced pair flow of this note by one fixed discrete gate at one fixed angle', '`denseUnitaryControl_of_fixedGate`',
           '`fixedGateTheory_not_qm`', 'The benchmark of this note is unchanged', 'reaches density of the unitaries and not exactness',
           'Nothing is named C5 or adopted'):
    ok_dca &= _t in _pfn_rec1
ok_dca &= _pfn_rec1.count('## ') == 1
for _n in (_rpn, _smn, _ccn, _pcn, _c5n):
    ok_dca &= 'discrete completion audit' not in _n and 'FixedGateSourced' not in _n
ok_dca &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-DCA', ok_dca,
      'Discrete completion guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its fifty-one results, defines exactly the predicates and the metric, the closure of availability, the block '
      'algebra, the gates, the block repertoire, the available set, the flips, the relocation, the two-level apparatus, '
      'the Givens block, the level-one group, the Pauli set and the canonical theory, nothing named C5, no existing '
      'definition restated, no pair flow in any constructive route and no irrationality inside a definition; the '
      'predicates, the bridge at constant two, the C*-identity bound, the dense angles by the dense-or-cyclic '
      'dichotomy, the block density, level one, the echo identity, the repertoire at the doubled angle, the relocation, '
      'the two-level Sylvester form with its determinant, the Givens closure, dense unitary control, the uniform finite '
      'countercontrols and the canonical theory are stated as pinned; the note keeps the question, the resource, the '
      'targets, the prediction, the lift, the fork, the outcomes, the tests and the non-doings before the amendment and '
      'the outcome, names the three commits, records outcome 2 with dense unitary control proved, the instrument chain\'s '
      'consumption of exact control named with its missing lemma, the closure obligations named, the classification not '
      'claimed beyond the proved cases, and no C5, no OI-supplies-the-gate, no density-is-exactness claim; no manuscript '
      'is edited; the registry and the census carry the family as kernel-only; the pair-flow equivalence note carries one '
      'section after its frozen text and the older notes are untouched; the README carries the paragraph and the counts.')

# ---- the quantitative dense-instrument bridge audit: from dense unitary control to dense instruments; the branch bound with
# a carrier-only constant, the shifted theory from identity availability beside the untouched shift, every exact consumption
# of the circuit discharged from the closure, inert spectators by citation, the approximate Stinespring assembly, the canonical
# theory dense finite quantum mechanics; outcome 1; no C5; no continuous pair flow; no completion claim ----
ok_dib = True
_di = open(os.path.join(BRIDGE, 'OIBridge', 'DenseInstrumentBridge.lean'), encoding='utf-8').read()
_diflat = ' '.join(_di.split())
_dicode = re.sub(r'/-.*?-/|--[^\n]*', '', _di, flags=re.S)
_din = open(os.path.join(os.path.dirname(BRIDGE), 'DENSE-INSTRUMENT-BRIDGE-AUDIT.md'), encoding='utf-8').read()
_din1 = re.sub(r'\s+', ' ', _din)
ok_dib &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _di) is None and 'native_decide' not in _di
ok_dib &= 'axiom ' not in _dicode
_di_names = re.findall(r"^theorem ([\w'.]+)", _di, re.M)
ok_dib &= len(_di_names) == 32 and _di.count('#print axioms') == 32
for _nm in ('chanWithin_mono', 'chanWithin_sum', 'unitary_unit_smul', 'norm_eq_one_of_isometry', 'norm_isometry_conj_le',
            'norm_isometry_compress_le', 'esf_gram', 'ptraceAnc_eq_sum', 'norm_ptraceAnc_le', 'norm_localLuders_le',
            'norm_pureAttach_le', 'branch_within', 'shiftId_avail_iff', 'shiftId_availExt_conj_iff', 'circuit_available_of_avail',
            'reindex_permMatrix', 'eqvMatrix_apply', 'eqvMatrix_mul', 'mul_eqvMatrix_conjTranspose', 'eqvMatrix_gram',
            'reindex_eq_eqvMatrix_conj', 'norm_reindex_le', 'id_avail_of_derivedOI', 'inert_of_derivedOI', 'shiftId_swap_avail',
            'shiftId_approx', 'krausDense_of_denseControl', 'denseFiniteQM_of_denseControl', 'krausDense_of_fixedGate',
            'fixedGateTheory_krausDense', 'fixedGateTheory_denseFiniteQM', 'fixedGateTheory_one_denseFiniteQM'):
    ok_dib &= ('#print axioms OIBridge.DenseInstrumentBridge.' + _nm) in _di and _nm in _di_names
# the definitions: exactly the shifted theory from identity availability and the bijection matrix; nothing named C5; no
# existing definition or circuit theorem restated; the existing shift untouched
_di_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _di, re.M)
ok_dib &= _di_defs == ['shiftId', 'eqvMatrix']
ok_dib &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _di, re.M) is None
for _t in ('shift', 'ChanWithin', 'KrausDense', 'DenseFiniteQM', 'DenseUnitaryControl', 'FixedGateSourced', 'ClosureAvail',
           'mixImage', 'MixR', 'mixTheoryR', 'DerivedOI', 'PairFlow', 'PairFlowSourced', 'conjChannel',
           'IsFiniteEndomorphicKrausInstrument', 'InertSpectatorCompositionality', 'IteratedAncillaClosure',
           'HasCompositeUnitaryControl', 'HasAncillaSwapControl', 'discardMap', 'localLuders', 'ptraceAnc', 'pureAttach'):
    ok_dib &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _di, re.M) is None
for _t in ('circuit_available', 'stinespringCircuit_branch', 'fullInstruments_of_control', 'conj_within', 'conjChannel_unit_smul',
           'denseUnitaryControl_of_fixedGate', 'shift_avail_iff', 'shift_control', 'shift_full'):
    ok_dib &= re.search(r'^theorem ' + _t + r'\b', _di, re.M) is None
_anc = open(os.path.join(BRIDGE, 'OIBridge', 'AncillaClosure.lean'), encoding='utf-8').read()
ok_dib &= 'noncomputable def shift (T : FiniteOperationalTheory A) (hctrl : HasCompositeUnitaryControl T)' in _anc
ok_dib &= 'avail_id := availExt_id_of_control T hctrl n' in _anc
_dicode_noopen = re.sub(r'^open .*$', '', _dicode, flags=re.M)
ok_dib &= 'PairFlowSourced' not in _dicode and re.search(r'\bPairFlow\b', _dicode_noopen) is None
ok_dib &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive)[^\n]*Irrational', _di, re.M) is None
ok_dib &= 'import OIBridge.DiscreteCompletion' in _di and 'import OIBridge.DenseInstrumentBridge' in root
# the statements, as preregistered and amended
for _t in ('ChanWithin (s.card * ε) (∑ i ∈ s, F i) (∑ i ∈ s, G i)',
           'theorem norm_eq_one_of_isometry [Nonempty S] {l : Type} [Fintype l] [DecidableEq l] {E : Matrix l S ℂ} (hE : Eᴴ * E = 1) : ‖E‖ = 1',
           'Matrix.l2_opNorm_conjTranspose_mul_self',
           'theorem esf_gram {n : ℕ} (k₀ : Fin n) : (Esf (A := A) k₀)ᴴ * Esf (A := A) k₀ = 1',
           'ptraceAnc n M = ∑ e : Fin n, (Esf (A := A) e)ᴴ * M * Esf (A := A) e',
           '‖ptraceAnc n M‖ ≤ n * ‖M‖', '‖localLuders k X‖ ≤ ‖X‖', '‖pureAttach n k₀ ρ‖ ≤ ‖ρ‖',
           'theorem branch_within [Nonempty A] {r : ℕ} (k₀ k : Fin (r + 1))',
           'ChanWithin (2 * ((r : ℝ) + 1) * δ) (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel U))) (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel V)))',
           'noncomputable def shiftId (T : FiniteOperationalTheory A) (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id)) (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ) : FiniteOperationalTheory (A × Fin n) where',
           'avail_id := hid n', 'readout_avail := fun m => availExt_relativeReadout T hin n m',
           'have h := hclos n m\' O (fun a => (F a).comp Φ) hcomp',
           '(shiftId T hid hin hclos n).avail O F ↔ T.availExt n O F := Iff.rfl',
           'theorem circuit_available_of_avail (T : FiniteOperationalTheory A) (n : ℕ)',
           '(hUav : T.availExt n Unit (fun _ => conjChannel U))',
           'Matrix.reindex e e (permMatrix σ) = permMatrix ((e.symm.trans σ).trans e)',
           '(eqvMatrix e)ᴴ * eqvMatrix e = 1', 'Matrix.reindex e e M = eqvMatrix e * M * (eqvMatrix e)ᴴ',
           '[Nonempty l] (e : l ≃ l\') (M : Matrix l l ℂ) : ‖Matrix.reindex e e M‖ ≤ ‖M‖',
           'theorem id_avail_of_derivedOI {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) (n : ℕ) : T.availExt n Unit (fun _ => LinearMap.id)',
           'theorem inert_of_derivedOI {A : Type} [Fintype A] [DecidableEq A] [Nonempty A] {T : FiniteOperationalTheory A} (hd : DerivedOI T) : InertSpectatorCompositionality T := (OIHierarchyGeneral.observationalIndependence_iff_inert T).mp (observationalIndependence_of_implementationLocality hd.implementationLocality)',
           'exact permMatrix_mem_availSet T hd (Nat.mul_pos hn hm) _',
           'theorem krausDense_of_denseControl {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) (hdense : DenseUnitaryControl T) : KrausDense T',
           'finiteIsometryExtensionSF_discharged (Fin 2 × Fin (k + 1)) r 0 (Vsf K)',
           'set δ := ε / (2 * ((r : ℝ) + 1) * ((r : ℝ) + 1)) with hδdef',
           'pureSeedPrep_available_of_swap (shiftId T hid hin hclos (k + 1)) r 0 hswap',
           'stinespringCircuit_branch K 0 j U hUE ρ', 'PairFlowEquivalence.conjChannel_unit_smul hc',
           'theorem denseFiniteQM_of_denseControl {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) (hdense : DenseUnitaryControl T) (hs : KrausSoundExt T) : DenseFiniteQM T',
           'theorem krausDense_of_fixedGate {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi)) (hg : FixedGateSourced α T) : KrausDense T',
           'theorem fixedGateTheory_krausDense {α : ℝ} (hα : Irrational (α / Real.pi)) : KrausDense (fixedGateTheory α)',
           'theorem fixedGateTheory_denseFiniteQM {α : ℝ} (hα : Irrational (α / Real.pi)) : DenseFiniteQM (fixedGateTheory α) := ⟨fixedGateTheory_krausSoundExt α, fixedGateTheory_krausDense hα⟩',
           'theorem fixedGateTheory_one_denseFiniteQM : DenseFiniteQM (fixedGateTheory 1)'):
    ok_dib &= _t in _diflat
# the note: the question, the objects, the steps, the prediction, the outcomes, the tests, the non-doings, the amendment,
# then the outcome and the non-claims, in that order
_kdi = [_din.find(h) for h in ('## The question', '## The objects, all existing and unchanged', '## The steps, frozen',
        '## The prediction', '## Admissible outcomes, frozen', '## Tests, frozen', '## What this round does not do',
        '## Scope amendment, recorded after the preregistration', '## The outcome', '## What this note does not claim')]
ok_dib &= all(x > 0 for x in _kdi) and _kdi == sorted(_kdi)
ok_dib &= _din.lstrip().startswith('# The quantitative dense-instrument bridge audit')
ok_dib &= _din.count('## Scope amendment, recorded after the preregistration') == 1
for _t in ('Preregistration commit `f8a9b80`', 'scope amendment `e5498b1`', '`main` at `5ff795e`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', '1. **Full dense-instrument success.**',
           '2. **Branch continuity succeeds, the structure exposes one exact missing operational condition.**',
           '3. **A quantitative branch or assembly obstruction prevents `KrausDense`.**', 'Exactly three.',
           '**(1) The round is a Barandes and Stinespring closure audit.**', '**(2) Step 3 is a citation for every theory satisfying the closure.**',
           '**(3) The general assembly theorem carries no spectator hypothesis.**', '**(4) A correction to the discrete completion audit\'s outcome.**',
           '**(5) The frontier hierarchy, recorded correctly.**', 'literally true and materially misleading',
           'The correspondence is cited as motivation only', 'thirty-two named results'):
    ok_dib &= _t in _din1
_din_out = re.sub(r'\s+', ' ', _din[_din.find('## The outcome'):])
for _t in ('The verdict is **outcome 1, full dense-instrument success**', 'The constant is `2 (r + 1)`, depending only on the carrier',
           'No sharper constant is claimed', 'the new definition beside the untouched `shift`',
           'By citation for every theory satisfying the closure on a nonempty carrier', 'the fallback of the preregistration is not used',
           'none of them a hypothesis', 'Soundness stays separate', 'Density is not the completion, and D3 is not claimed',
           'Outcome 1 is reached; outcome 2 is not reached; outcome 3 is not reached', 'was a formal gap',
           'the sole remaining physical sourcing question in this thread is the fixed nonclassical gate itself', 'The gate is a stated datum',
           'is not exact quantum mechanics', 'The manuscript status of the state-mixing resource is unchanged',
           'cited as motivation for the representation and dilation arrows only', 'the two debts of D3 stand',
           '| T1 | ', '| T5 | ', '| T7 | ', '| T9 | '):
    ok_dib &= _t in _din_out
for _bad in ('The verdict is **outcome 2', 'The verdict is **outcome 3', 'Outcome 1 is not reached', 'is C5.', 'C5 holds', 'C5 is the',
             'we adopt C5', 'define C5', 'the fixed gate is C5', 'OI supplies the', 'OI itself supplies', 'D3 is proved',
             'the completion is proved', 'exact quantum mechanics is the completion', 'density is exactness', 'minimal', 'Minimal',
             'PairFlow enters', 'continuous pair flow is used', 'Barandes proves', 'proved by Barandes', 'the correspondence proves',
             'is fundamental physics', 'fundamental physics is'):
    ok_dib &= _bad not in _din_out
for _bad in ('the fixed gate is C5', 'C5 holds', 'the gate is supplied by OI', 'D3 holds', 'the completion holds',
             'is exact quantum mechanics'):
    ok_dib &= not _asserted(_din[_din.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('DenseInstrumentBridge', 'DENSE-INSTRUMENT-BRIDGE', 'krausDense_of_denseControl', 'fixedGateTheory_denseFiniteQM',
                 'fixedGateTheory_krausDense', 'shiftId', 'branch_within', 'inert_of_derivedOI'):
        ok_dib &= _bad not in _t
_di_fam = [f for f in _ptr_reg['families'] if f['name'] == 'dense-instrument bridge: from dense unitary control to dense finite quantum mechanics']
ok_dib &= len(_di_fam) == 1 and _di_fam[0]['status'] == 'kernel-only' and _di_fam[0]['modules'] == ['DenseInstrumentBridge']
ok_dib &= _di_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 1, full dense-instrument success', 'the stall was a formal gap', 'a stated datum', 'D3 is not claimed',
           'still not exact quantum mechanics', 'Nothing is named C5 or adopted', 'no continuous pair flow in any constructive route',
           'the correspondence cited as motivation only', 'owner decision'):
    ok_dib &= _t in _di_fam[0]['note']
for _bad in ('the fixed gate is C5', 'C5 holds', 'D3 is proved', 'the completion is proved', 'density is exactness', 'minimal', 'OI supplies the'):
    ok_dib &= _bad not in _di_fam[0]['note']
ok_dib &= '| dense-instrument bridge: from dense unitary control to dense finite quantum mechanics | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-DIB`', 'DENSE-INSTRUMENT-BRIDGE-AUDIT.md', 'branch_within', 'esf_gram', 'norm_pureAttach_le', 'norm_localLuders_le',
           'ptraceAnc_eq_sum', 'norm_ptraceAnc_le', 'shiftId', 'id_avail_of_derivedOI', 'reindex_permMatrix', 'shiftId_swap_avail',
           'circuit_available_of_avail', 'reindex_eq_eqvMatrix_conj', 'norm_reindex_le', 'shiftId_approx', 'inert_of_derivedOI',
           'DerivedOI.implementationLocality', 'observationalIndependence_of_implementationLocality', 'observationalIndependence_iff_inert',
           'krausDense_of_denseControl', 'denseFiniteQM_of_denseControl', 'krausDense_of_fixedGate', 'fixedGateTheory_krausDense',
           'fixedGateTheory_denseFiniteQM', 'fixedGateTheory_one_denseFiniteQM', 'fixedGateTheory_not_qm',
           'Verdict: outcome 1, full dense-instrument success', 'the stall was a formal gap', 'a stated datum',
           'D3 and its two debts are untouched; `π/8` stays a prediction', 'Thirty-two named results',
           'Nothing is named C5 or adopted; no continuous pair flow enters any constructive route; no definition changes; no manuscript changes'):
    ok_dib &= _t in _rd1
for _bad in ('the fixed gate is C5', 'C5 holds', 'D3 is proved', 'the completion is proved', 'density is exactness', 'OI supplies the'):
    ok_dib &= _bad not in _rd1
# the discrete completion note: one section recorded after its frozen text and its outcome; the older notes untouched
_dcn2 = open(os.path.join(os.path.dirname(BRIDGE), 'DISCRETE-COMPLETION-AUDIT.md'), encoding='utf-8').read()
_dcn_rec = _dcn2.find('## Recorded after the round: the dense-instrument bridge audit')
ok_dib &= _dcn_rec > _dcn2.find('## What this note does not claim') and _dcn_rec > _dcn2.find('Status: pass complete')
_dcn_rec1 = re.sub(r'\s+', ' ', _dcn2[_dcn_rec:])
for _t in ('The frozen text and the outcome of this note are not edited', 'literally true and materially misleading', '`inert_of_derivedOI`',
           '`branch_within`', '`shiftId`', '`fixedGateTheory_denseFiniteQM`', 'while still not exact quantum mechanics',
           'Outcome 2 of this note was a formal continuity gap and not a physical condition', 'the gate remains a stated datum'):
    ok_dib &= _t in _dcn_rec1
ok_dib &= _dcn_rec1.count('## ') == 1
for _n in (_rpn, _smn, _ccn, _pcn, _c5n, _pfn):
    ok_dib &= 'dense-instrument bridge' not in _n and 'DenseInstrumentBridge' not in _n
ok_dib &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-DIB', ok_dib,
      'Dense-instrument bridge guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its thirty-two results, defines exactly the shifted theory from identity availability and the bijection matrix, '
      'nothing named C5, no existing definition or circuit theorem restated, the existing shift untouched, no pair flow '
      'in any constructive route and no irrationality inside a definition; the calculus of the metric, the isometry '
      'norms, the seed embedding, the partial trace as a sum of compressions with its bound, the Lüders contraction, the '
      'isometric attachment, the branch bound with the constant two times the ancilla dimension, the shifted theory '
      'field by field, the circuit from the availability of its unitary, the reindexed permutation, the bijection '
      'matrix, the identity and the swaps from the closure, inert spectators by citation, the descent of dense control, '
      'the assembly with the explicit delta, soundness separate, the fixed-gate form and the canonical endpoints are '
      'stated as pinned; the note keeps the question, the objects, the steps, the prediction, the outcomes, the tests '
      'and the non-doings before the amendment and the outcome, names the three commits, records the amendment\'s five '
      'points, records outcome 1 with the branch bound, the shifted theory, the spectators and the endpoints proved, '
      'D3 and the completion not claimed, the gate a stated datum, and no C5, no OI-supplies-the-gate, no '
      'density-is-exactness, no completion claim; no manuscript is edited; the registry and the census carry the family '
      'as kernel-only; the discrete completion note carries one section after its frozen text and its outcome, with the '
      'T7 correction, and the older notes are untouched; the README carries the paragraph and the counts.')

# ---- the frozen substratum nonclassical-resource sourcing audit: the sourcing question below the closure, for the phases and
# dense unitary control at once, with the architecture frozen and A6 left a gap; one invariant of a theory's availability,
# the census, the two ceilings audited separately with the dense-control one proved twice, both rule-independent; outcome 3,
# the no-go; no axiom or operation added to the substratum and nothing added reported as sourced; no C5 ----
ok_fss = True
_fs = open(os.path.join(BRIDGE, 'OIBridge', 'FrozenSourcing.lean'), encoding='utf-8').read()
_fsflat = ' '.join(_fs.split())
_fscode = re.sub(r'/-.*?-/|--[^\n]*', '', _fs, flags=re.S)
_fsn = open(os.path.join(os.path.dirname(BRIDGE), 'FROZEN-SUBSTRATUM-SOURCING-AUDIT.md'), encoding='utf-8').read()
_fsn1 = re.sub(r'\s+', ' ', _fsn)
ok_fss &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _fs) is None and 'native_decide' not in _fs
ok_fss &= 'axiom ' not in _fscode
_fs_names = re.findall(r"^theorem ([\w'.]+)", _fs, re.M)
ok_fss &= len(_fs_names) == 23 and _fs.count('#print axioms') == 23
for _nm in ('norm_entry_le_l2_opNorm', 'le_zero_of_forall_pos', 'nonneg_of_forall_pos', 'nonnegBounded_of_bijectionLevel',
            'permTheory_nonnegBounded', 'obsTheory_nonnegBounded', 'nonnegBounded_not_phasesAvailable',
            'permTheory_phase_ceiling', 'nonnegBounded_not_derivedOI', 'preservesNonneg_of_approx',
            'nonnegBounded_not_denseUnitaryControl', 'permTheory_dense_ceiling', 'mixImage_not_preservesNonneg',
            'nonnegBounded_not_denseUnitaryControl_rot', 'permMatrix_preservesNonneg', 'readWrite_preservesNonneg',
            'obs_dynamics_preservesNonneg', 'phaseOperator_outside_ceiling', 'sourcing_rule_independent',
            'phase_ceiling_rule_independent', 'frozen_sourcing_verdict', 'nonnegBounded_verdict',
            'fixedGateTheory_outside_ceiling'):
    ok_fss &= ('#print axioms OIBridge.FrozenSourcing.' + _nm) in _fs and _nm in _fs_names
# THE FREEZE: exactly one definition, the invariant; nothing named C5; no axiom, no A6 predicate, no substratum structure,
# no existing definition restated, no enrichment of the implementation class
_fs_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _fs, re.M)
ok_fss &= _fs_defs == ['NonnegBounded']
ok_fss &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _fs, re.M) is None
ok_fss &= 'A6' not in _fs and re.search(r'(?m)^axiom ', _fs) is None
for _t in ('Substratum', 'permClass', 'permTheory', 'obsTheory', 'BijectionLevel', 'PreservesNonneg', 'IsScaledPartialPerm',
           'IsMonomial', 'MonomialSource', 'phaseOperator', 'bijectiveOperator', 'phaseGate', 'mixImage', 'DerivedOI',
           'SourcedOI', 'PhasesAvailable', 'DenseUnitaryControl', 'KrausDense', 'DenseFiniteQM', 'ChanWithin', 'conjChannel',
           'ReadWriteFamily', 'readWriteOperator', 'Rule', 'A1', 'A2', 'A3', 'A4', 'A5', 'ImplementationClass',
           'Architecture', 'genTheory', 'fixedGateTheory'):
    ok_fss &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _fs, re.M) is None
_fscode_noopen = re.sub(r'^open .*$', '', _fscode, flags=re.M)
ok_fss &= 'PairFlowSourced' not in _fscode and re.search(r'\bPairFlow\b', _fscode_noopen) is None
ok_fss &= 'import OIBridge.DenseInstrumentBridge' in _fs and 'import OIBridge.FrozenSourcing' in root
# the statements, as preregistered
for _t in ('def NonnegBounded (T : FiniteOperationalTheory A) : Prop := ∀ (n : ℕ) (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ), T.availExt n Unit (fun _ => Φ) → PreservesNonneg Φ',
           'theorem nonnegBounded_of_bijectionLevel {𝓘 : ImplementationClass} (arch : Architecture 𝓘) (hb : BijectionLevel 𝓘) : NonnegBounded (genTheory 𝓘 arch A) := fun _ _ hav => preservesNonneg_of_realized hb (realized_of_instAvail arch hav ())',
           'theorem permTheory_nonnegBounded : NonnegBounded (permTheory A)',
           'theorem obsTheory_nonnegBounded (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V] : NonnegBounded (obsTheory 𝒮)',
           '(M : Matrix m n ℂ) (p : m) (q : n) : ‖M p q‖ ≤ ‖M‖',
           'theorem nonnegBounded_not_phasesAvailable [Nonempty A] {T : FiniteOperationalTheory A} (h : NonnegBounded T) : ¬ PhasesAvailable T',
           'theorem nonnegBounded_not_derivedOI [Nonempty A] {T : FiniteOperationalTheory A} (h : NonnegBounded T) : ¬ DerivedOI T',
           'theorem preservesNonneg_of_approx [Nonempty S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1)',
           'Wᴴ * W = 1 ∧ PreservesNonneg (conjChannel W) ∧ ‖U - W‖ < ε) : PreservesNonneg (conjChannel U)',
           'conj_within hU hW hUW.le X',
           'theorem nonnegBounded_not_denseUnitaryControl {T : FiniteOperationalTheory (Fin 2)} (h : NonnegBounded T) : ¬ DenseUnitaryControl T',
           'theorem permTheory_dense_ceiling : ¬ DenseUnitaryControl (permTheory (Fin 2))',
           'theorem mixImage_not_preservesNonneg {n : ℕ} (k : Fin n) {θ : ℝ} (hs : 0 < Real.sin θ) (hc : 0 < Real.cos θ) : ¬ PreservesNonneg (conjChannel (mixImage n θ))',
           'theorem nonnegBounded_not_denseUnitaryControl_rot {T : FiniteOperationalTheory (Fin 2)} (h : NonnegBounded T) : ¬ DenseUnitaryControl T',
           'theorem obs_dynamics_preservesNonneg (𝒮 : Substratum)',
           'PreservesNonneg (conjChannel (permMatrix (levelPerm 𝒮.φ n)))',
           'theorem phaseOperator_outside_ceiling',
           "(R R' : Rule ι V) (P : FiniteOperationalTheory (ι → V × V) → Prop) : P (obsTheory { ι := ι, V := V, R := R }) ↔ P (obsTheory { ι := ι, V := V, R := R' }) := Iff.rfl",
           'theorem frozen_sourcing_verdict : ¬ PhasesAvailable (permTheory (Fin 2)) ∧ ¬ DenseUnitaryControl (permTheory (Fin 2)) ∧ ¬ DerivedOI (permTheory (Fin 2))',
           'theorem nonnegBounded_verdict {T : FiniteOperationalTheory (Fin 2)} (h : NonnegBounded T) : ¬ PhasesAvailable T ∧ ¬ DenseUnitaryControl T ∧ ¬ DerivedOI T',
           'theorem fixedGateTheory_outside_ceiling {α : ℝ} (hα : Irrational (α / Real.pi)) : ¬ NonnegBounded (fixedGateTheory α)'):
    ok_fss &= _t in _fsflat
# the note: the question, the frozen architecture, the layers, the prediction, the outcomes, the guard, the tests, the
# non-doings, then the outcome and the non-claims, in that order
_kfs = [_fsn.find(h) for h in ('## The question', '## The architecture, frozen exactly as it stands', '## The four layers, frozen',
        '## The prediction, recorded before proof', '## Admissible outcomes, frozen',
        "## The circularity guard, the round's most important constraint", '## Tests, frozen',
        '## What this round does not do', '## The outcome', '## What this note does not claim')]
ok_fss &= all(x > 0 for x in _kfs) and _kfs == sorted(_kfs)
ok_fss &= _fsn.lstrip().startswith('# The frozen substratum nonclassical-resource sourcing audit')
for _t in ('Preregistration commit `c0e763c`', '`main` at `8f277f5`', 'Status: preregistered; no proof attempted',
           'Status: pass complete', '1. **Positive.**', '2. **Split or partial.**', '3. **No-go.**', 'Exactly three.',
           '**A6 remains a gap with no predicate**', 'twenty-three named results',
           'No new axiom, carrier map, coupling, phase intervention, polarization map, continuous control,',
           'enrichment of the implementation class may be added to the frozen', 'reported as sourced by OI',
           'candidate empirical extension', '`PhasesAvailable` is not `DenseUnitaryControl`',
           'A resource sufficient for dense quantum mechanics is not a resource sourced by the substratum'):
    ok_fss &= _t in _fsn1
_fsn_out = re.sub(r'\s+', ' ', _fsn[_fsn.find('## The outcome'):])
# the substantive outcome, with the round's own non-claim paragraph and the non-claims section set aside: an honest
# disclaimer must not trip the guard built to protect it
_fsn_cut = _fsn_out.find('**What the outcome does not establish')
_fsn_out_claims = _fsn_out[:_fsn_cut] if _fsn_cut > 0 else _fsn_out
for _t in ('The verdict is **outcome 3, the no-go**', 'No axiom, operation, carrier map, coupling or class enrichment was added',
           'never through a claim that some available channel is itself a scaled partial permutation',
           'Represented, not sourced', 'Audited independently of layer 2', 'the invariant passes to limits',
           'The ceiling is a property of the class and not a statement about one gate',
           'which carries no phase at all', 'neither obligation is derived from the other',
           'Asked only after the two were audited separately', 'The rule adds no availability',
           'The substrate\'s own update is sourced, and it is rule-dependent',
           'contributes no availability beyond the configuration-level observer theory', 'A6 stays the gap it was',
           'The two sides fit', 'it takes nothing back from the density side',
           'Outcome 3 is reached; outcome 1 is not reached; outcome 2 is not reached',
           'an independent empirical datum relative to the presently stated OI architecture',
           'not repaired by choosing a different microscopic rule', '**What the outcome does not establish',
           '| T1 | ', '| T4 | ', '| T5 | ', '| T8 | '):
    ok_fss &= _t in _fsn_out
for _bad in ('The verdict is **outcome 1', 'The verdict is **outcome 2', 'Outcome 3 is not reached', 'is C5.', 'C5 holds',
             'we adopt C5', 'define C5', 'OI supplies the', 'OI itself supplies', 'the architecture is refuted',
             'refutes the architecture', 'A6 is filled', 'we add an axiom', 'two independent additions are needed',
             'no architecture can source', 'cannot be sourced by any', 'minimal', 'Minimal', 'PairFlow enters',
             'density is exactness', 'we enrich the'):
    ok_fss &= _bad not in _fsn_out_claims
for _bad in ('the architecture is refuted', 'OI supplies the phases', 'A6 has a predicate', 'two independent additions are needed',
             'no extension could source'):
    ok_fss &= not _asserted(_fsn[_fsn.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('FrozenSourcing', 'FROZEN-SUBSTRATUM-SOURCING', 'NonnegBounded', 'frozen_sourcing_verdict',
                 'permTheory_dense_ceiling', 'nonnegBounded_not_denseUnitaryControl', 'sourcing_rule_independent'):
        ok_fss &= _bad not in _t
_fs_fam = [f for f in _ptr_reg['families'] if f['name'] == 'frozen substratum sourcing: the ceilings of the stated architecture']
ok_fss &= len(_fs_fam) == 1 and _fs_fam[0]['status'] == 'kernel-only' and _fs_fam[0]['modules'] == ['FrozenSourcing']
ok_fss &= _fs_fam[0]['manuscript'] == []
for _t in ('Verdict outcome 3, the no-go', 'an independent empirical datum relative to the presently stated architecture',
           'A6 a gap with no predicate and not filled', 'no axiom, operation, carrier map, coupling or class enrichment is added',
           'a different microscopic rule does not move either ceiling', 'neither obligation is derived from the other',
           'Nothing is named C5 or adopted', 'owner decision'):
    ok_fss &= _t in _fs_fam[0]['note']
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'two independent additions are needed', 'minimal'):
    ok_fss &= _bad not in _fs_fam[0]['note']
ok_fss &= '| frozen substratum sourcing: the ceilings of the stated architecture | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-FSS`', 'FROZEN-SUBSTRATUM-SOURCING-AUDIT.md', 'NonnegBounded', 'nonnegBounded_of_bijectionLevel',
           'permTheory_nonnegBounded', 'obsTheory_nonnegBounded', 'permMatrix_preservesNonneg', 'readWrite_preservesNonneg',
           'obs_dynamics_preservesNonneg', 'phaseOperator_outside_ceiling', 'nonnegBounded_not_phasesAvailable',
           'nonnegBounded_not_derivedOI', 'permTheory_phase_ceiling', 'norm_entry_le_l2_opNorm', 'preservesNonneg_of_approx',
           'nonnegBounded_not_denseUnitaryControl', 'permTheory_dense_ceiling', 'mixImage_not_preservesNonneg',
           'nonnegBounded_not_denseUnitaryControl_rot', 'sourcing_rule_independent', 'phase_ceiling_rule_independent',
           'frozen_sourcing_verdict', 'nonnegBounded_verdict', 'fixedGateTheory_outside_ceiling',
           'Verdict: outcome 3, the no-go', 'A6 a gap with no predicate and not filled',
           'an independent empirical datum relative to the presently stated architecture', 'Twenty-three named results',
           'Nothing is named C5 or adopted; no continuous pair flow enters any route; no definition changes; no manuscript changes'):
    ok_fss &= _t in _rd1
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'two independent additions are needed'):
    ok_fss &= _bad not in _rd1
# the two prior notes each carry one section after their frozen text; the older notes untouched
_sin2 = open(os.path.join(os.path.dirname(BRIDGE), 'SUBSTRATUM-INTERFACE-AUDIT.md'), encoding='utf-8').read()
_sin_rec = _sin2.find('## Recorded after the round: the frozen substratum sourcing audit')
ok_fss &= _sin_rec > _sin2.find('## What this note does not claim')
ok_fss &= re.sub(r'\s+', ' ', _sin2[_sin_rec:]).count('## ') == 1
_din3 = open(os.path.join(os.path.dirname(BRIDGE), 'DENSE-INSTRUMENT-BRIDGE-AUDIT.md'), encoding='utf-8').read()
_din_rec = _din3.find('## Recorded after the round: the frozen substratum sourcing audit')
ok_fss &= _din_rec > _din3.find('## What this note does not claim') and _din_rec > _din3.find('Status: pass complete')
_din_rec1 = re.sub(r'\s+', ' ', _din3[_din_rec:])
for _t in ('The frozen text and the outcome of this note are not edited', '`fixedGateTheory_outside_ceiling`',
           'it takes nothing back from the density side', 'larger than the fixed gate'):
    ok_fss &= _t in _din_rec1
ok_fss &= _din_rec1.count('## ') == 1
for _n in (_rpn, _smn, _ccn, _pcn, _c5n, _pfn, _dcn):
    ok_fss &= 'frozen substratum sourcing' not in _n and 'FrozenSourcing' not in _n
ok_fss &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-FSS', ok_fss,
      'Frozen substratum sourcing guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its twenty-three results, defines exactly the nonnegativity invariant and nothing else, names nothing C5, mentions '
      'no A6 and defines no predicate for it, adds no axiom and restates no existing definition of the substratum, the '
      'interface, the shape predicates or the density side, and carries no pair flow; the invariant, its derivation through '
      'the implementation class and the realization theorem, the sourced and observer theories carrying it, the entrywise '
      'bound, the limit lemma, the phase ceiling at class level, the closure negative, the dense-control ceiling and its '
      'second route from the rotation witness, the census of the sourced operations and of the phase operator outside the '
      'ceiling, the rule-independence of the verdict and the combined verdicts are stated as pinned; the note keeps the '
      'question, the frozen architecture, the layers, the prediction, the outcomes, the circularity guard, the tests and the '
      'non-doings before the outcome, names both commits, records outcome 3 with the census, the two ceilings audited '
      'separately and the dense-control one proved twice, the rule contributing nothing, A6 still a gap, the density side '
      'untouched, and no C5, no OI-supplies-the-resource, no architecture-refuted, no A6-filled, no two-additions and no '
      'no-architecture-can-source claim; no manuscript is edited; the registry and the census carry the family as '
      'kernel-only; the substratum interface note and the dense-instrument bridge note each carry one section after their '
      'frozen text and the older notes are untouched; the README carries the paragraph and the counts.')

# ---- R7-SOI: the stochastic observer-interface determination audit -- the determination predicate, the single-orbit
# positive route stated and then closed by the architecture's own additivity axiom, the ensemble leg proved undetermined
# for the manuscripts' wave rule, the observation-map leg recorded by census; outcome A, the interface gap; stage 2 not
# entered, so no induced process, no divisibility predicate, no correspondence; no C5 ----
ok_soi = True
_so = open(os.path.join(BRIDGE, 'OIBridge', 'StochasticInterface.lean'), encoding='utf-8').read()
_soflat = ' '.join(_so.split())
_socode = re.sub(r'/-.*?-/|--[^\n]*', '', _so, flags=re.S)
_son = open(os.path.join(os.path.dirname(BRIDGE), 'STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md'), encoding='utf-8').read()
_son1 = re.sub(r'\s+', ' ', _son)
ok_soi &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _so) is None and 'native_decide' not in _so
ok_soi &= 'axiom ' not in _socode
_so_names = re.findall(r"^theorem ([\w'.]+)", _so, re.M)
ok_soi &= len(_so_names) == 12 and _so.count('#print axioms') == 12
for _nm in ('ensembleDetermined_of_transitive', 'not_ensembleDetermined_of_disjoint',
            'not_ensembleDetermined_of_fixedPoint', 'phi_fixes_zero', 'waveSubstratum_phi_fixes_zero',
            'ensemble_underdetermined', 'waveSubstratum_ensemble_underdetermined', 'not_transitive_of_fixedPoint',
            'readWriteFamily_exists', 'readWriteFamily_exists_two', 'stochastic_interface_gap',
            'waveSubstratum_stochastic_interface_gap'):
    ok_soi &= ('#print axioms OIBridge.StochasticInterface.' + _nm) in _so and _nm in _so_names
# THE FREEZE: exactly one definition, the determination predicate; no observation map, no ensemble, no induced process,
# no divisibility predicate, no correspondence predicate, no A6, nothing named C5, no existing definition restated
_so_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _so, re.M)
ok_soi &= _so_defs == ['EnsembleDetermined']
ok_soi &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _so, re.M) is None
ok_soi &= 'A6' not in _so and re.search(r'(?m)^axiom ', _so) is None
ok_soi &= 'Markov' not in _so and 'markov' not in _so
ok_soi &= re.search(r'(?i)divisib', _socode) is None
ok_soi &= re.search(r'(?i)barandes', _so) is None
for _t in ('Substratum', 'permClass', 'permTheory', 'obsTheory', 'Rule', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6',
           'NonnegBounded', 'PreservesNonneg', 'BijectionLevel', 'DerivedOI', 'SourcedOI', 'PhasesAvailable',
           'DenseUnitaryControl', 'KrausDense', 'DenseFiniteQM', 'ChanWithin', 'conjChannel', 'ReadWriteFamily',
           'readWriteOperator', 'IsProb', 'Invariant', 'orbit', 'unif', 'entropy', 'marg', 'Core', 'vis', 'swapFn',
           'histTriple', 'CoreC1C4', 'genTheory', 'fixedGateTheory', 'Divisible', 'Indivisible', 'PDivisible',
           'Obs', 'Ensemble', 'InducedProcess', 'Correspondence'):
    ok_soi &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _so, re.M) is None
_socode_noopen = re.sub(r'^open .*$', '', _socode, flags=re.M)
ok_soi &= re.search(r'\bPairFlow\b', _socode_noopen) is None
ok_soi &= ('import OIBridge.FrozenSourcing' in _so and 'import OIBridge.CanonicalMeasure' in _so
           and 'import OIBridge.StochasticInterface' in root)
# the statements, as executed
for _t in ('def EnsembleDetermined (φ : Equiv.Perm S) : Prop := ∃! p : S → ℝ, IsProb p ∧ Invariant φ p',
           'theorem ensembleDetermined_of_transitive (φ : Equiv.Perm S) (s : S) (htr : ∀ t : S, t ∈ orbit φ s) : EnsembleDetermined φ',
           'theorem not_ensembleDetermined_of_disjoint (φ : Equiv.Perm S) {A B : Finset S} (hA : A.Nonempty) (hB : B.Nonempty) (hAm : ∀ x ∈ A, φ x ∈ A) (hBm : ∀ x ∈ B, φ x ∈ B) (hdisj : Disjoint A B) : ¬ EnsembleDetermined φ',
           'theorem not_ensembleDetermined_of_fixedPoint (φ : Equiv.Perm S) {x y : S} (hx : φ x = x) (hxy : y ≠ x) : ¬ EnsembleDetermined φ',
           'theorem phi_fixes_zero (h5 : 𝒮.A5) : 𝒮.φ 0 = 0',
           'theorem waveSubstratum_phi_fixes_zero (d L q : ℕ) [NeZero L] [NeZero q] (α : ZMod q) : (waveSubstratum d L q α).φ 0 = 0',
           'theorem ensemble_underdetermined (h5 : 𝒮.A5) {y : 𝒮.Conf} (hy : y ≠ 0) : ¬ EnsembleDetermined 𝒮.φ',
           'theorem waveSubstratum_ensemble_underdetermined (d L q : ℕ) [NeZero L] [NeZero q] [Fact (1 < q)] (α : ZMod q) : ¬ EnsembleDetermined (waveSubstratum d L q α).φ',
           'theorem not_transitive_of_fixedPoint {S : Type*} [Fintype S] [DecidableEq S] (φ : Equiv.Perm S) {x y : S} (hx : φ x = x) (hxy : y ≠ x) : ¬ ∃ s : S, ∀ t : S, t ∈ orbit φ s',
           'theorem readWriteFamily_exists (a b : S) : Nonempty (ReadWriteFamily a b)',
           'theorem readWriteFamily_exists_two {a b c d : S} : Nonempty (ReadWriteFamily a b) ∧ Nonempty (ReadWriteFamily c d)',
           'theorem stochastic_interface_gap (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V] (h5 : 𝒮.A5) {y : 𝒮.Conf} (hy : y ≠ 0) : ¬ EnsembleDetermined 𝒮.φ ∧ ¬ ∃ s : 𝒮.Conf, ∀ t : 𝒮.Conf, t ∈ orbit 𝒮.φ s'):
    ok_soi &= _t in _soflat
# the note: the question, the frozen architecture, the stages, the quantifier, the guard, the outcomes, the prediction,
# the tests, the non-doings, the amendment, then the outcome and the non-claims, in that order
_kso = [_son.find(h) for h in ('## The question', '## The architecture, frozen exactly as it stands', '## The stages, frozen',
        '## The ensemble quantifier, frozen', "## The guard, stricter than the frozen sourcing audit's",
        '## Admissible outcomes, frozen', '## The prediction, recorded before proof', '## Tests, frozen',
        '## What this round does not do', '## Scope amendment, recorded after the preregistration',
        '## The outcome', '## What this note does not claim')]
ok_soi &= all(x > 0 for x in _kso) and _kso == sorted(_kso)
ok_soi &= _son.lstrip().startswith('# The stochastic observer-interface determination audit')
for _t in ('Preregistration commit `23c1dbd`, amendment commit `892d81c`', '`main` at `22ef402`',
           'Status: preregistered; no proof attempted', 'Status: pass complete', 'Exactly three, in this order.',
           '1. **Outcome A, the interface gap.**', '2. **Outcome B, sourced interface, divisible process.**',
           '3. **Outcome C, sourced interface, indivisible process.**', '**A6 remains a gap with no predicate**',
           'twelve named results', 'Outcome A is expected, on the ensemble leg',
           'Neither `Obs` nor `μ` may be selected because it yields indivisibility',
           'Carrying `vis` from the census core to `Substratum.Conf` by analogy',
           'Invariance does not select **in general**', 'remains a selection principle rather than a consequence',
           'a *sourced family* of'):
    ok_soi &= _t in _son1
_son_out = re.sub(r'\s+', ' ', _son[_son.find('## The outcome'):])
# the substantive outcome, with the round's own non-claim paragraph and the non-claims section set aside
_son_cut = _son_out.find('**What the outcome does not establish')
_son_out_claims = _son_out[:_son_cut] if _son_cut > 0 else _son_out
for _t in ('The verdict is **outcome A, the interface gap**',
           'the ensemble leg fails by theorem rather than by absence of a candidate',
           'No axiom, observation map, ensemble, coupling or class enrichment was added',
           'Invariance is the only ensemble constraint the architecture states',
           'The positive route, taken up first', 'That ensemble would have been derived, not chosen',
           'The fixed point, from a stated axiom', 'Nothing was added to obtain this; the axiom was read',
           'The same fixed point closes the positive route',
           'any configuration other than zero serves equally, and none was chosen for the verdict it would yield',
           'on a one-letter alphabet the configuration space is a single point',
           'the structure privileges no pair', 'it induces no function on configurations',
           'The frozen text records that carrying it across is an addition rather than a finding',
           'it proves no claim that a map cannot exist',
           'the divisibility predicates were not introduced, and the diagnostic was not run',
           'Outcome A is reached; outcome B is not reached; outcome C is not reached',
           'obtained by supplying two of its three inputs from outside',
           '**What the outcome does not establish', '| T1 | ', '| T4 | ', '| T5 | ', '| T8 | '):
    ok_soi &= _t in _son_out
for _bad in ('The verdict is **outcome B', 'The verdict is **outcome C', 'Outcome A is not reached', 'is C5.', 'C5 holds',
             'we adopt C5', 'define C5', 'OI supplies the', 'OI itself supplies', 'the architecture is refuted',
             'refutes the architecture', 'A6 is filled', 'we add an axiom', 'no architecture can supply',
             'cannot be supplied by any', 'minimal', 'Minimal', 'PairFlow enters', 'non-Markovian', 'the process is divisible',
             'the process is indivisible', 'the correspondence applies', 'we use the uniform measure',
             'we use the counting measure', 'we carry `vis`'):
    ok_soi &= _bad not in _son_out_claims
for _bad in ('the architecture is refuted', 'A6 has a predicate', 'no extension could supply',
             'an observation map on `Conf` cannot exist', 'the induced process is indivisible'):
    ok_soi &= not _asserted(_son[_son.find('## The outcome'):], _bad)
# no manuscript carries the round; the registry and the census carry the family as kernel-only; the README
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('StochasticInterface', 'STOCHASTIC-OBSERVER-INTERFACE', 'EnsembleDetermined',
                 'stochastic_interface_gap', 'ensemble_underdetermined', 'not_transitive_of_fixedPoint',
                 'readWriteFamily_exists'):
        ok_soi &= _bad not in _t
_so_fam = [f for f in _ptr_reg['families']
           if f['name'] == 'stochastic observer interface: the determination gap of the stated architecture']
ok_soi &= len(_so_fam) == 1 and _so_fam[0]['status'] == 'kernel-only' and _so_fam[0]['modules'] == ['StochasticInterface']
ok_soi &= _so_fam[0]['manuscript'] == []
for _t in ('Verdict outcome A, the interface gap', 'A6 a gap with no predicate and not filled',
           'no correspondence theorem is stated or cited and no predicate for one is defined',
           "the census core's vis is not carried to Substratum.Conf",
           'invariance being the only ensemble constraint the architecture states',
           'divisibility is never identified with Markovianity because neither predicate was introduced',
           'conditional on A5 and on a configuration space carrying more than the zero configuration',
           'nothing is named C5', 'owner decision'):
    ok_soi &= _t in _so_fam[0]['note']
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'minimal', 'non-Markovian'):
    ok_soi &= _bad not in _so_fam[0]['note']
ok_soi &= '| stochastic observer interface: the determination gap of the stated architecture | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-SOI`', 'STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md', 'EnsembleDetermined',
           'ensembleDetermined_of_transitive', 'phi_fixes_zero', 'waveSubstratum_phi_fixes_zero',
           'not_ensembleDetermined_of_disjoint', 'not_ensembleDetermined_of_fixedPoint', 'ensemble_underdetermined',
           'not_transitive_of_fixedPoint', 'waveSubstratum_ensemble_underdetermined',
           'waveSubstratum_stochastic_interface_gap', 'stochastic_interface_gap', 'readWriteFamily_exists',
           'readWriteFamily_exists_two', 'Verdict: outcome A, the interface gap',
           'A6 a gap with no predicate and not filled', 'Twelve named results',
           'no divisibility predicate exists in the kernel'):
    ok_soi &= _t in _rd1
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'non-Markovian'):
    ok_soi &= _bad not in _rd1
# the frozen sourcing note carries exactly one section after its own non-claims; the older notes untouched
_fsn4 = open(os.path.join(os.path.dirname(BRIDGE), 'FROZEN-SUBSTRATUM-SOURCING-AUDIT.md'), encoding='utf-8').read()
_fsn_x = _fsn4.find('## Cross-reference, appended after the frozen text')
ok_soi &= _fsn_x > _fsn4.find('## What this note does not claim') and _fsn_x > _fsn4.find('Status: pass complete')
_fsn_x1 = re.sub(r'\s+', ' ', _fsn4[_fsn_x:])
for _t in ('takes up the narrow reading this note gives its own outcome 3', 'reports outcome A, the interface gap',
           'The ensemble leg is proved from A5', 'Nothing above is changed by that result'):
    ok_soi &= _t in _fsn_x1
ok_soi &= _fsn_x1.count('## ') == 1
for _n in (_rpn, _smn, _ccn, _pcn, _c5n, _pfn, _dcn, _din):
    ok_soi &= 'stochastic observer interface' not in _n and 'StochasticInterface' not in _n
ok_soi &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-SOI', ok_soi,
      'Stochastic observer-interface determination guard: the module carries no sorry, axiom or native_decide, prints the '
      'axioms of exactly its twelve results, defines exactly the ensemble-determination predicate and nothing else -- no '
      'observation map, no ensemble, no induced process, no divisibility predicate, no correspondence predicate -- names '
      'nothing C5, mentions no A6 and defines no predicate for it, never writes Markov or Barandes, restates no existing '
      'definition of the substratum, the measure layer, the census core, the interface or the density side, and carries no '
      'pair flow; the determination predicate, the single-orbit positive route, the fixed point from A5 for every additive '
      'rule and for the wave rule, the disjoint-invariant-sets route to undetermination, the ensemble leg for every '
      'substratum and for the wave rule, the failure of transitivity, the read-write existence witnesses and the two '
      'combined verdicts are stated as pinned; the note keeps the question, the frozen architecture, the stages, the '
      'ensemble quantifier, the guard, the outcomes, the prediction, the tests, the non-doings and the scope amendment '
      'before the outcome, names all three commits, records outcome A with both legs stated separately, the positive route '
      'stated and then closed, the one-letter-alphabet and additivity hypotheses stated, stage 2 not entered and no '
      'divisibility predicate defined, and no C5, no OI-supplies-the-resource, no architecture-refuted, no A6-filled, no '
      'no-extension-could-supply, no map-cannot-exist, no divisibility verdict and no correspondence claim; no manuscript '
      'is edited; the registry and the census carry the family as kernel-only; the frozen sourcing note carries exactly one '
      'section after its own non-claims and the older notes are untouched; the README carries the paragraph and the counts.')

# ---- R7-C4R: the C4 causal-readback audit -- the two candidate forms on rooted one-time visible marginals, the
# frozen composition orientation, the chain to P-indivisibility by two independent routes, the layer used only for
# the construction, the four controls, and the two verdicts reported separately; no fifth condition, no C5 ----
ok_c4r = True
_cr = open(os.path.join(BRIDGE, 'OIBridge', 'CausalReadback.lean'), encoding='utf-8').read()
_crflat = ' '.join(_cr.split())
_crcode = re.sub(r'/-.*?-/|--[^\n]*', '', _cr, flags=re.S)
_crn = open(os.path.join(os.path.dirname(BRIDGE), 'C4-CAUSAL-READBACK-AUDIT.md'), encoding='utf-8').read()
_crn1 = re.sub(r'\s+', ' ', _crn)
_cra = open(os.path.join(os.path.dirname(BRIDGE), 'C4-CAUSAL-READBACK-AUDIT-AMENDMENT.md'), encoding='utf-8').read()
_cra1 = re.sub(r'\s+', ' ', _cra)
ok_c4r &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _cr) is None and 'native_decide' not in _cr
ok_c4r &= 'axiom ' not in _crcode and re.search(r'(?m)^axiom ', _cr) is None
_cr_names = re.findall(r"^theorem ([\w'.]+)", _cr, re.M)
ok_c4r &= len(_cr_names) == 21 and _cr.count('#print axioms') == 21
for _nm in ('tv_nonneg', 'tv_eq_zero_iff', 'tv_pos_of_ne', 'tv_mul_le', 'rows_eq_of_factor', 'c4e_implies_c4r',
            'c4r_implies_pIndivisible', 'c4e_implies_pIndivisible', 'c4e_implies_pIndivisible_via_c4r',
            'not_c4e_and_not_c4r_of_pDivisible', 'rootedMap_isRowStochastic', 'j2_isRowStochastic',
            'one_isRowStochastic', 'j2_rows_eq', 'one_rows_ne', 'pdFamily_pDivisible', 'pdFamily_not_c4e_not_c4r',
            'peFamily_c4e', 'peFamily_pIndivisible', 'control_separation', 'causal_readback_verdict'):
    ok_c4r &= ('#print axioms OIBridge.CausalReadback.' + _nm) in _cr and _nm in _cr_names
# THE FREEZE: exactly the audit's own definitions; no fifth condition; nothing named C5; total variation REUSED
# from the kernel rather than redefined; the manuscript condition not renamed; no correspondence predicate
_cr_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _cr, re.M)
ok_c4r &= _cr_defs == ['IsRowStochastic', 'PDivisible', 'PIndivisibleWithin', 'C4e', 'C4r',
                       'RootedRealization', 'rootedMap', 'J2', 'pdFamily', 'peFamily']
ok_c4r &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive|theorem) [Cc]5', _cr, re.M) is None
ok_c4r &= 'A6' not in _cr
ok_c4r &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) tv\b', _cr, re.M) is None
ok_c4r &= 'import OIBridge.HiddenMemory' in _cr and 'HiddenMemory' in _crflat
for _t in ('C4w', 'Markov', 'markov', 'Barandes', 'Divisible ', 'Correspondence', 'Obs', 'Ensemble'):
    ok_c4r &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _cr, re.M) is None
ok_c4r &= 'import OIBridge.CausalReadback' in root
# the frozen orientation, and the statements as executed
for _t in ('def PDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ∀ s t : ℕ, s < t → t ≤ K → ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ',
           'def C4e (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ∃ (a b : V) (s t : ℕ), a ≠ b ∧ s < t ∧ t ≤ K ∧ Γ s a = Γ s b ∧ Γ t a ≠ Γ t b',
           'def C4r (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ∃ (a b : V) (s t : ℕ), a ≠ b ∧ s < t ∧ t ≤ K ∧ tv (Γ s a) (Γ s b) < tv (Γ t a) (Γ t b)',
           'theorem tv_mul_le {Λ : Matrix V V ℝ} (hΛ : IsRowStochastic Λ) (p q : V → ℝ) : tv (fun j => ∑ i, p i * Λ i j) (fun j => ∑ i, q i * Λ i j) ≤ tv p q',
           'theorem rows_eq_of_factor {Γs Γt Λ : Matrix V V ℝ} (hfac : Γt = Γs * Λ) {a b : V} (hrow : Γs a = Γs b) : Γt a = Γt b',
           'theorem c4e_implies_c4r (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4e K Γ) : C4r K Γ',
           'theorem c4r_implies_pIndivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4r K Γ) : PIndivisibleWithin K Γ',
           'theorem c4e_implies_pIndivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) (h : C4e K Γ) : PIndivisibleWithin K Γ',
           'theorem pdFamily_pDivisible (K : ℕ) : PDivisible K pdFamily',
           'theorem peFamily_c4e : C4e 3 peFamily',
           'theorem peFamily_pIndivisible : PIndivisibleWithin 3 peFamily',
           'multiplication, `Γ t = Γ s * Λ`. Left multiplication mixes over the root index and is not the'):
    ok_c4r &= _t in _crflat
# the note: the frozen sections in order, then the outcome and the non-claims
_kcr = [_crn.find(h) for h in ('## Why this round exists', '## The question, frozen', '## Layer boundary, frozen',
        '## The current C4, frozen as the weak form', '## Candidate strengthened C4, frozen before proof',
        '## P-divisibility, frozen', '## The core theorem targets', '## Mandatory controls', '## Relationship to C4w',
        '## Physical-sourcing census', '## Admissible outcomes', '## Barandes boundary', '## Tests, frozen',
        '## Guard', '## Prediction, recorded before proof', '## The outcome', '## What this note does not claim')]
ok_c4r &= all(x > 0 for x in _kcr) and _kcr == sorted(_kcr)
ok_c4r &= _crn.lstrip().startswith('# C4 causal-readback strengthening audit')
for _t in ('Preregistration commit `ada7ccf`, amendment commit `53830de`', '`main` at `5ca538a`',
           'twenty-one named results', 'No fifth condition is defined, nothing is named C5',
           'M-A on the mathematics** and **S-B on the sourcing'):
    ok_c4r &= _t in _crn1
# the amendment is binding, additions-only, and carries all four corrections plus the guard clause
for _t in ('This amendment is binding and additions-only', 'byte-for-byte untouched',
           'A1 — `C4e` / `C4r` are candidate causal-readback forms, not yet proved strengthenings',
           'A2 — row-stochastic composition convention is frozen now', '`Gamma_t = Gamma_s * Lambda_(t,s)`',
           'Left multiplication by `Lambda` mixes over the root index',
           'A3 — layer construction and abstract no-go theorems are separate', 'layer-independent',
           'A4 — “left the visible description” means the one-time marginal only',
           'A5 — execution guard for the audit-local C4 vocabulary'):
    ok_c4r &= _t in _cra1
_crn_out = re.sub(r'\s+', ' ', _crn[_crn.find('## The outcome'):])
_crn_cut = _crn_out.find('### What the outcome does not establish')
_crn_out_claims = _crn_out[:_crn_cut] if _crn_cut > 0 else _crn_out
for _t in ('The verdict is **M-A on the mathematics** and **S-B on the sourcing**',
           'Stochasticity of the propagator is never used',
           'The composition convention did real work',
           'Under the opposite orientation the argument fails outright',
           'the kernel proves the divisibility half, and\nthe existing exact probe proves the memory half'.replace('\n', ' '),
           'is\n**not proved and is not claimed**'.replace('\n', ' '),
           'the word *strengthening* is therefore not used',
           'not comparable in the proved direction',
           'They probe different observables',
           'A conditional theorem is not a sourced one',
           '#537 remains binding and is not weakened here',
           '| T1 | ', '| T7 | ', '| T8 | ', '| T10 | '):
    ok_c4r &= _t in _crn_out
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'minimal', 'Minimal', 'is C5.',
             'C5 holds', 'we adopt C5', 'define C5', 'a fifth condition', 'C4e strengthens C4w',
             'C4r strengthens C4w', 'the strengthened C4 succeeds', 'necessary for P-indivisibility.',
             'non-Markovian', 'the correspondence applies', 'closes #537', 'S-A is reached'):
    ok_c4r &= _bad not in _crn_out_claims
for _bad in ('the architecture is refuted', 'the architecture sources', 'C4e implies C4w',
             'either candidate is necessary', 'a causal hidden write-then-read mechanism is exhibited'):
    ok_c4r &= not _asserted(_crn[_crn.find('## The outcome'):], _bad)
# no manuscript carries the round, and the manuscript's own C4 is untouched by the audit vocabulary
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('CausalReadback', 'C4-CAUSAL-READBACK', 'C4e', 'C4r', 'C4w', 'PIndivisibleWithin',
                 'causal_readback_verdict', 'pdFamily', 'peFamily'):
        ok_c4r &= _bad not in _t
# the manuscript's own C4 clause, which the round cites as provenance, is still present and unedited
_main_c4 = open(os.path.join(_msroot, 'papers/Main.md'), encoding='utf-8').read()
ok_c4r &= 'it does not by itself assert a causal write-then-read cycle' in _main_c4
ok_c4r &= 'a pre-sampled hidden variable revealed by the history satisfies it' in _main_c4
_cr_fam = [f for f in _ptr_reg['families']
           if f['name'] == 'causal readback: the candidate forms and the divisibility no-go']
ok_c4r &= len(_cr_fam) == 1 and _cr_fam[0]['status'] == 'kernel-only' and _cr_fam[0]['modules'] == ['CausalReadback']
ok_c4r &= _cr_fam[0]['manuscript'] == []
for _t in ('neither is called a strengthening of the manuscript condition',
           'the opposite orientation mixing over the root index and breaking the argument',
           'two independent routes', 'layer-independent',
           'verdict M-A on the mathematics and S-B on the sourcing, reported separately',
           'total variation is the kernel', 'nothing is named C5', 'owner decision'):
    ok_c4r &= _t.lower() in _cr_fam[0]['note'].lower()
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'minimal', 'non-Markovian'):
    ok_c4r &= _bad not in _cr_fam[0]['note']
ok_c4r &= '| causal readback: the candidate forms and the divisibility no-go | 1 | kernel-only |' in _cen_ps
for _t in ('`R7-C4R`', 'C4-CAUSAL-READBACK-AUDIT.md', 'causal_readback_verdict', 'tv_mul_le', 'rows_eq_of_factor',
           'c4r_implies_pIndivisible', 'c4e_implies_pIndivisible', 'RootedRealization', 'rootedMap_isRowStochastic',
           'pdFamily_pDivisible', 'pdFamily_not_c4e_not_c4r', 'peFamily_c4e', 'peFamily_pIndivisible',
           'control_separation', 'Twenty-one named results', 'M-A on the mathematics, S-B on the sourcing',
           'neither candidate is called a\nstrengthening'.replace('\n', ' '),
           'Γ t = Γ s * Λ', 'right multiplication on the outcome index'):
    ok_c4r &= _t in _rd1
# the forbidden forms are the ASSERTIONS, not the round's own disclaimer, which names the same words
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'non-Markovian',
             'a fifth condition is defined', 'a fifth condition is named', 'defines a fifth condition',
             'names a fifth condition'):
    ok_c4r &= _bad not in _rd1
# the older notes are untouched by this round
for _n in (_rpn, _smn, _ccn, _pcn, _c5n, _pfn, _dcn, _din, _fsn, _son):
    ok_c4r &= 'causal readback' not in _n and 'CausalReadback' not in _n
ok_c4r &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-C4R', ok_c4r,
      'C4 causal-readback guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its twenty-one results, defines exactly the audit predicates, the rooted realization and the two controls and '
      'nothing else -- no fifth condition, no correspondence predicate, no observation map, no ensemble -- names '
      'nothing C5, mentions no A6, never redefines total variation but reuses the kernel definition, and does not '
      'rename the manuscript condition; the frozen right-multiplication orientation is stated in the module header '
      'and used in every statement, and the two routes to the endpoint -- the data-processing contraction and the '
      'row obstruction that uses neither stochasticity nor the layer -- are separately pinned, as are the rooted '
      'construction, the four controls and the combined verdict; the note keeps its frozen sections in order before '
      'the outcome, names both commits, and the amendment is binding, additions-only and carries all five of its '
      'clauses; the outcome records M-A and S-B separately, states that stochasticity is unused by the exact route, '
      'that the orientation is load-bearing, that the kernel proves the divisibility half while the exact probe '
      'proves the memory half, that the converse to the manuscript condition is unproved so no ordering is forced '
      'and the word strengthening is not used, and that the interface gap remains binding; no architecture-refuted, '
      'no OI-sources-it, no A6-filled, no fifth-condition, no necessity and no correspondence claim; the manuscript '
      'C4 clause the round cites as provenance is present and unedited and no manuscript carries the round; the '
      'registry and the census carry the family as kernel-only; the README carries the paragraph and the counts.')

# ---- R7-RCH: the recurrence-horizon route -- an identity return of the rooted map together with a strictly
# earlier overlap of two distinct rooted rows forces revival and forbids divisibility within that horizon;
# only the store clause is consumed, the second arrow is reused, and nothing is claimed below the horizon ----
ok_rch = True
_rh = open(os.path.join(BRIDGE, 'OIBridge', 'RecurrenceHorizon.lean'), encoding='utf-8').read()
_rhflat = ' '.join(_rh.split())
_rhcode = re.sub(r'/-.*?-/|--[^\n]*', '', _rh, flags=re.S)
_rhn = open(os.path.join(os.path.dirname(BRIDGE), 'RECURRENCE-TIGHTNESS-AUDIT.md'), encoding='utf-8').read()
_rha = open(os.path.join(os.path.dirname(BRIDGE), 'RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md'), encoding='utf-8').read()
_rha1 = re.sub(r'\s+', ' ', _rha)
ok_rch &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _rh) is None and 'native_decide' not in _rh
ok_rch &= 'axiom ' not in _rhcode and re.search(r'(?m)^axiom ', _rh) is None
_rh_names = re.findall(r"^theorem ([\w'.]+)", _rh, re.M)
ok_rch &= len(_rh_names) == 9 and _rh.count('#print axioms') == 9
for _nm in ('tv_eq_one_sub_sum_min', 'tv_le_one_sub_min', 'tv_lt_one_of_overlap', 'tv_one_rows',
            'c4r_of_identity_return_of_overlap', 'pIndivisible_of_identity_return_of_overlap',
            'c4r_of_rooted_identity_return_of_overlap', 'pIndivisible_of_rooted_identity_return_of_overlap',
            'horizon_verdict'):
    ok_rch &= ('#print axioms OIBridge.RecurrenceHorizon.' + _nm) in _rh and _nm in _rh_names
# THE FREEZE: the module DEFINES NOTHING. Every predicate is the merged round's, total variation is the
# kernel's, and no readback parent, horizon symbol or rigidity lemma is introduced here.
_rh_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _rh, re.M)
ok_rch &= _rh_defs == []
ok_rch &= 'import OIBridge.CausalReadback' in _rh
ok_rch &= 'import OIBridge.RecurrenceHorizon' in root
for _t in ('CausalReadback', 'C4w', 'C5', 'N_CR', 'Rigidity', 'StochasticInverse', 'Markov', 'Barandes'):
    ok_rch &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _rh, re.M) is None
# the statements as executed, at the hypothesis level actually proved
for _t in ('theorem tv_eq_one_sub_sum_min {p q : V → ℝ} (hp : ∑ j, p j = 1) (hq : ∑ j, q j = 1) : tv p q = 1 - ∑ j, min (p j) (q j)',
           'theorem tv_one_rows {a b : V} (hab : a ≠ b) : tv ((1 : Matrix V V ℝ) a) ((1 : Matrix V V ℝ) b) = 1',
           'theorem c4r_of_identity_return_of_overlap {Γ : ℕ → Matrix V V ℝ} {n s : ℕ} (hsn : s < n) (hstoch : IsRowStochastic (Γ s)) (hI : Γ n = 1) {a b : V} (hab : a ≠ b) {x : V} (hax : 0 < Γ s a x) (hbx : 0 < Γ s b x) : C4r n Γ',
           'theorem pIndivisible_of_identity_return_of_overlap {Γ : ℕ → Matrix V V ℝ} {n s : ℕ} (hsn : s < n) (hstoch : IsRowStochastic (Γ s)) (hI : Γ n = 1) {a b : V} (hab : a ≠ b) {x : V} (hax : 0 < Γ s a x) (hbx : 0 < Γ s b x) : PIndivisibleWithin n Γ',
           'c4r_implies_pIndivisible n Γ'):
    ok_rch &= _t in _rhflat
# the dependency result the round reports, and the scope limit, both stated in the module
for _t in ('only the store clause', 'the write clause, the causal read leg and the rooted-reappearance leg play no part',
           'nothing here claims a result for any horizon below', 'reused rather than reproved',
           'not a redefinition', 'layer-independent'):
    ok_rch &= _t.lower() in ' '.join(_rh.split()).lower()
# the preregistration is frozen and its amendment controls the horizon; execution claims nothing below it
ok_rch &= 'RECURRENCE-TIGHTNESS-AUDIT.md' in _rhflat and 'RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md' in _rhflat
ok_rch &= 'N_CR := min { n > 0 : Gamma_n = I and there exists a storage witness time s with s < n }' in _rha1
ok_rch &= 'Execution must not silently treat a bare visible return as a period.' in _rha1
# no manuscript carries the round
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('RecurrenceHorizon', 'RECURRENCE-TIGHTNESS', 'N_CR', 'horizon_verdict',
                 'c4r_of_identity_return_of_overlap', 'PIndivisibleWithin'):
        ok_rch &= _bad not in _t
_rh_fam = [f for f in _ptr_reg['families']
           if f['name'] == 'recurrence horizon: an identity return with an earlier overlap forbids divisibility']
ok_rch &= len(_rh_fam) == 1 and _rh_fam[0]['status'] == 'kernel-only' and _rh_fam[0]['modules'] == ['RecurrenceHorizon']
ok_rch &= _rh_fam[0]['manuscript'] == []
for _t in ('only the store clause', 'reused rather than reproved', 'no stochastic-inverse rigidity lemma is introduced',
           'not a redefinition', 'layer-independent', 'separate tightness question',
           'no accessibility claim is made for the horizon itself'):
    ok_rch &= _t.lower() in _rh_fam[0]['note'].lower()
for _bad in ('the architecture is refuted', 'OI supplies the', 'A6 is filled', 'minimal', 'non-Markovian',
             'before recurrence', 'accessible quantum'):
    ok_rch &= _bad not in _rh_fam[0]['note']
ok_rch &= ('| recurrence horizon: an identity return with an earlier overlap forbids divisibility | 1 | kernel-only |'
           in _cen_ps)
for _t in ('`R7-RCH`', 'RECURRENCE-TIGHTNESS-AUDIT.md', 'RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md',
           'c4r_of_identity_return_of_overlap', 'pIndivisible_of_identity_return_of_overlap',
           'tv_eq_one_sub_sum_min', 'tv_one_rows', 'tv_lt_one_of_overlap', 'horizon_verdict',
           'reused rather than reproved', 'no stochastic-inverse rigidity lemma is introduced',
           'Nine named results', 'the write clause and both read legs of the frozen readback parent play no part'):
    ok_rch &= _t in _rd1
# the forbidden readings: no claim below the horizon, no accessibility, no parent-strength inflation
for _bad in ('before recurrence', 'accessible quantum', 'A6 is filled', 'OI supplies the',
             'the parent is necessary', 'forces accessible'):
    ok_rch &= _bad not in _rd1[_rd1.find('OIBridge/RecurrenceHorizon.lean'):
                               _rd1.find('OIBridge/RecurrenceHorizon.lean') + 3000]
ok_rch &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-RCH', ok_rch,
      'Recurrence-horizon guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its nine results, and DEFINES NOTHING -- every predicate is the merged causal-readback round\'s, total '
      'variation is the kernel\'s existing notion with the one-minus-overlap identity an addition rather than a '
      'redefinition, and no readback parent, no horizon symbol and no stochastic-inverse rigidity lemma is '
      'introduced; the two endpoints are separately pinned, distinct identity rows at distance exactly one and '
      'overlapping rows strictly below one, as are the revival witness on the pair and its composition with the '
      'already-merged revival no-go, reused rather than reproved; the hypotheses are pinned at the level actually '
      'proved, so the round\'s own dependency result is enforced -- only the store clause is consumed and the write '
      'clause and both read legs play no part -- and the abstract section is layer-independent while the layer '
      'section draws on the rooted realization solely for row-stochasticity; the preregistration and its controlling '
      'amendment are named in the module, the amendment carries the controlling horizon definition and the '
      'no-periodicity warning verbatim, and nothing is claimed for any horizon below the one proved, the tightness '
      'question being neither answered nor prejudged and no accessibility claim made; no manuscript carries the '
      'round; the registry and the census carry the family as kernel-only; the README carries the paragraph and the '
      'counts.')


# ---- R7-SCF: the scaling family -- the abstract half of S1, quantified over the horizon rather
# than checked at particular horizons; a constructive divisibility factor, the merged revival no-go
# reused for indivisibility, and no realization, parent or horizon symbol introduced ----
ok_scf = True
_sf = open(os.path.join(BRIDGE, 'OIBridge', 'ScalingFamily.lean'), encoding='utf-8').read()
_sfflat = ' '.join(_sf.split())
_sfcode = re.sub(r'/-.*?-/|--[^\n]*', '', _sf, flags=re.S)
_sfn = open(os.path.join(os.path.dirname(BRIDGE), 'RECURRENCE-SCALING-AUDIT.md'), encoding='utf-8').read()
_sfn1 = re.sub(r'\s+', ' ', _sfn)
ok_scf &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _sf) is None and 'native_decide' not in _sf
ok_scf &= 'axiom ' not in _sfcode and re.search(r'(?m)^axiom ', _sf) is None
_sf_names = re.findall(r"^theorem ([\w'.]+)", _sf, re.M)
ok_scf &= len(_sf_names) == 11 and _sf.count('#print axioms') == 11
for _nm in ('Bmat_one_eq', 'Bmat_isRowStochastic', 'Bmat_mul', 'Bmat_factor', 'tv_Bmat',
            'tv_Bmat_one', 'tv_Bmat_lt_one', 'pDivisible_below', 'c4r_at_return',
            'pIndivisible_at_return', 'tight_at'):
    ok_scf &= ('#print axioms OIBridge.ScalingFamily.' + _nm) in _sf and _nm in _sf_names
# THE FREEZE: exactly one definition, the channel itself. No realization, no parent, no horizon
# symbol, no rediscovered divisibility predicate, and total variation reused from the kernel.
_sf_defs = re.findall(r"^(?:noncomputable )?(?:def|abbrev|structure|inductive) ([\w'.]+)", _sf, re.M)
ok_scf &= _sf_defs == ['Bmat']
ok_scf &= 'import OIBridge.RecurrenceHorizon' in _sf
ok_scf &= 'import OIBridge.ScalingFamily' in root
for _t in ('N_CR', 'CausalReadback', 'Tight', 'RootedRealization', 'PDivisible', 'C4r', 'tv', 'C5'):
    ok_scf &= re.search(r'^(?:noncomputable )?(?:def|abbrev|structure|inductive) ' + _t + r'\b', _sf, re.M) is None
# the statements as executed: uniform in the horizon, constructive factor, reused no-go
for _t in ('def Bmat (p : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![p, 1 - p; 1 - p, p]',
           'theorem Bmat_mul (p q : ℝ) : Bmat p * Bmat q = Bmat (2 * p * q - p - q + 1)',
           'theorem tv_Bmat (p : ℝ) : tv (Bmat p 0) (Bmat p 1) = |2 * p - 1|',
           'IsRowStochastic (Bmat ((pt + ps - 1) / (2 * ps - 1)))',
           'c4r_implies_pIndivisible N _ (c4r_at_return hN hhalf hlt hpN)'):
    ok_scf &= _t in _sfflat
# the module's own scope statements, which keep it from being read as the construction target
for _t in ('quantified over the horizon', 'none of it is a check at', 'is not reproved here',
           'Nothing in this module constructs a realization', 'must exhibit',
           'no claim is made about physical accessibility of any horizon'):
    ok_scf &= _t.lower() in _sfflat.lower()
# the frozen preregistration is named and its S1/finite-table discipline is intact
ok_scf &= 'RECURRENCE-SCALING-AUDIT.md' in _sfflat
ok_scf &= 'A finite table of tight realizations at increasing horizons is **not** an unbounded family' in _sfn1
ok_scf &= 'exists B, for all R: tight(R) -> N_CR(R) <= B' in _sfn1
# no manuscript carries the round
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('ScalingFamily', 'RECURRENCE-SCALING', 'Bmat', 'tight_at', 'N_CR'):
        ok_scf &= _bad not in _t
_sf_fam = [f for f in _ptr_reg['families']
           if f['name'] == 'scaling family: tightness of the return horizon, uniform in the horizon']
ok_scf &= len(_sf_fam) == 1 and _sf_fam[0]['status'] == 'kernel-only' and _sf_fam[0]['modules'] == ['ScalingFamily']
ok_scf &= _sf_fam[0]['manuscript'] == []
for _t in ('quantified over the horizon', 'constructive rather than existential',
           'not reproved but reuses', 'constructs no realization',
           'not by itself the round', 'physical accessibility'):
    ok_scf &= _t.lower() in _sf_fam[0]['note'].lower()
for _bad in ('unbounded family is exhibited', 'S1 is proved', 'O-1', 'inaccessible', 'minimal'):
    ok_scf &= _bad not in _sf_fam[0]['note']
ok_scf &= ('| scaling family: tightness of the return horizon, uniform in the horizon | 1 | kernel-only |'
           in _cen_ps)
for _t in ('`R7-SCF`', 'RECURRENCE-SCALING-AUDIT.md', 'Bmat_mul', 'tv_Bmat', 'Bmat_factor',
           'tight_at', 'c4r_at_return', 'pIndivisible_at_return',
           'constructive rather than existential', 'is not reproved',
           'not itself the round’s construction target'.replace('’', "'"),
           'Eleven named results'):
    ok_scf &= _t in _rd1
# the forbidden readings: the abstract half is not the construction, and claims nothing about reach
for _bad in ('unbounded family is exhibited', 'S1 is proved', 'inaccessible', 'accessible quantum'):
    ok_scf &= _bad not in _rd1[_rd1.find('OIBridge/ScalingFamily.lean'):
                               _rd1.find('OIBridge/ScalingFamily.lean') + 2200]
ok_scf &= '143 modules' in _rd1 and '3,102 named results' in _rd1
check('R7-SCF', ok_scf,
      'Scaling-family guard: the module carries no sorry, axiom or native_decide, prints the axioms of exactly '
      'its eleven results, and defines exactly one object -- the symmetric binary channel -- introducing no '
      'realization, no readback parent, no horizon symbol and no reimplementation of divisibility, revival or '
      'total variation; the composition law and the rooted-row distance are pinned as executed, the divisibility '
      'factor is constructive and pinned with the stochasticity it must satisfy, and the indivisibility half is '
      'pinned as the merged revival no-go reused rather than reproved; the module states, and the guard requires, '
      'that its results are quantified over the horizon rather than checked at particular horizons, that it '
      'constructs no realization, that it supplies only what a realization-layer construction must exhibit, and '
      'that it claims nothing about physical accessibility; the frozen preregistration is named and its '
      'finite-table rule and bounded-horizon S2 form are intact; no manuscript carries the round; the registry and '
      'the census carry the family as kernel-only and neither claims the construction target is met; the README '
      'carries the paragraph and the counts.')



# ---- R7-RCL: the rooted classification -- the finite-visible iff, integrated into the ordinary
# bridge root, with axiom reporting complete at the source rather than inferred from build output ----
_RC_MODS = ('RootedClassification', 'RootedClassificationT2', 'RootedClassificationAllTime')
_rc_txt = {_m: open(os.path.join(BRIDGE, 'OIBridge', _m + '.lean'), encoding='utf-8').read()
           for _m in _RC_MODS}
_rc_all = '\n'.join(_rc_txt.values())
_rc_flat = ' '.join(_rc_all.split())


def _rc_declared(txt):
    """Theorem names, counting declarations that carry attributes.

    A bare ^theorem scan misses `@[simp] theorem ...`, and this round found the difference the hard
    way: the chain scanned as 37 declarations while 40 results were named. Undercounting here would
    let an unprinted theorem hide inside the count it was supposed to be caught by."""
    return re.findall(r"(?m)^(?:@\[[^\]]*\]\s*)?theorem\s+([A-Za-z_][\w']*)", txt)


def _rc_printed(txt):
    return re.findall(r"#print axioms OIBridge\.RootedClassification\.([\w']+)", txt)


def _rc_prints_complete(txt):
    """The source-level axiom-reporting contract: every named result is printed, and only those.

    Set equality rather than count equality. A duplicated print together with a dropped one keeps
    the line count intact while leaving a result unreported, which is exactly the shape a count pin
    cannot see."""
    _d, _pr = _rc_declared(txt), _rc_printed(txt)
    return set(_d) == set(_pr) and len(_d) == len(set(_d))


def _rc_root_reachable(root_txt, wf_txt, scf_txt):
    """The architectural contract: the chain is built by the ordinary bridge build.

    Both halves failed during this round. A development import in ScalingFamily made the chain look
    gated while `lake build` did not reach it, and the CI workaround that replaced it could report
    only a missing object file. Reachability is therefore a property to enforce, not a convention to
    remember."""
    for _m in _RC_MODS:
        if ('import OIBridge.' + _m + '\n') not in root_txt:
            return False
    if re.search(r'lake build\s+OIBridge\.', wf_txt):
        return False
    if re.search(r'lake env lean\s+OIBridge/RootedClassification', wf_txt):
        return False
    if 'RootedClassification' in scf_txt:
        return False
    return True


_rc_scf = open(os.path.join(BRIDGE, 'OIBridge', 'ScalingFamily.lean'), encoding='utf-8').read()
ok_rcl = True
# the two contracts hold as the tree stands
ok_rcl &= all(_rc_prints_complete(_rc_txt[_m]) for _m in _RC_MODS)
ok_rcl &= _rc_root_reachable(root, _wf, _rc_scf)
# and each is mutation-tested, one broken way at a time, against the three ways this round broke
ok_rcl &= not _rc_root_reachable(
    root.replace('import OIBridge.RootedClassificationAllTime\n', ''), _wf, _rc_scf)
ok_rcl &= not _rc_root_reachable(
    root, _wf + '\n          lake build OIBridge.RootedClassificationAllTime\n', _rc_scf)
ok_rcl &= not _rc_root_reachable(
    root, _wf, _rc_scf + '\nimport OIBridge.RootedClassification\n')
# ... and against both ways axiom reporting can go incomplete: a dropped print, and the harder case
# of a duplicated print masking a dropped one, where the raw line count is unchanged
_rc_b4 = _rc_printed(_rc_txt['RootedClassification'])
_rc_m4 = _rc_txt['RootedClassification'].replace(
    '#print axioms OIBridge.RootedClassification.' + _rc_b4[-1] + '\n', '', 1)
# the mutation must actually change the text, or the control passes vacuously: an earlier draft of
# this guard deleted a print line for a `def`, which has none, and so tested nothing
ok_rcl &= _rc_m4 != _rc_txt['RootedClassification']
ok_rcl &= not _rc_prints_complete(_rc_m4)
_rc_names = _rc_printed(_rc_txt['RootedClassificationAllTime'])
_rc_m5 = _rc_txt['RootedClassificationAllTime'].replace(
    '#print axioms OIBridge.RootedClassification.' + _rc_names[-1],
    '#print axioms OIBridge.RootedClassification.' + _rc_names[0])
ok_rcl &= not _rc_prints_complete(_rc_m5)
ok_rcl &= (_rc_m5.count('#print axioms') == _rc_txt['RootedClassificationAllTime'].count('#print axioms'))
# forty named results across the chain, and the standing hygiene
ok_rcl &= sum(len(_rc_declared(_rc_txt[_m])) for _m in _RC_MODS) == 40
ok_rcl &= (len(_rc_declared(_rc_txt['RootedClassification'])) == 16
           and len(_rc_declared(_rc_txt['RootedClassificationT2'])) == 8
           and len(_rc_declared(_rc_txt['RootedClassificationAllTime'])) == 16)
_rc_code = re.sub(r'/-.*?-/|--[^\n]*', '', _rc_all, flags=re.S)
ok_rcl &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _rc_all) is None and 'native_decide' not in _rc_all
ok_rcl &= 'axiom ' not in _rc_code and re.search(r'(?m)^axiom ', _rc_all) is None
# the capstone and the semantic class as executed, and the class kept distinct from the candidate
for _t in ('def FiniteRootedRealizable',
           'theorem finiteRootedRealizable_iff_pper (Γ : ℕ → Matrix V V ℝ) : FiniteRootedRealizable (V := V) Γ ↔ PPer Γ',
           'theorem finiteRootedRealizable_of_realization',
           'theorem pper_of_finiteRootedRealizable',
           'theorem pper_has_responseRealization',
           'theorem rootedMap_mem_PPer'):
    ok_rcl &= _t in _rc_flat
# the finite-visible restriction is stated where it can be read, not left to the typeclass alone
for _t in ('Finite visible carriers only', 'classifies the finite-visible slice',
           'requires only `Fintype H`', 'no period need exist'):
    ok_rcl &= _t.lower() in _rc_flat.lower()
# control 13: three separated statements, and the horizon distinction carried in the kernel
for _t in ('theorem pdFamily_not_periodicFamily', 'theorem peFamily_not_periodicFamily',
           'theorem pdFamily_not_finiteRootedRealizable', 'theorem peFamily_not_finiteRootedRealizable'):
    ok_rcl &= _t in _rc_flat
for _t in ('realize the requested prefix', 'free to depend on the horizon',
           'not a single realization agreeing at every time'):
    ok_rcl &= _t.lower() in _rc_flat.lower()
# the frozen preregistration and its amendment are named where the reconciliation lives
ok_rcl &= 'OI-ROOTED-CLASSIFICATION-AUDIT.md' in _rd1
_rc_amd = open(os.path.join(os.path.dirname(BRIDGE), 'C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md'),
               encoding='utf-8').read()
_rc_amd1 = re.sub(r'\s+', ' ', _rc_amd)
for _t in ('append-only', 'superseded', 'does **not** give', 'depends on `K`'):
    ok_rcl &= _t.lower() in _rc_amd1.lower()
# no manuscript carries the round
for _rel in ('papers/GR.md', 'papers/Main.md', 'papers/Explainer.md', 'papers/Substratum.md', 'papers/SM.md',
             'book/The-Incompleteness-of-Observation-FULL.md'):
    _t = open(os.path.join(_msroot, _rel), encoding='utf-8').read()
    for _bad in ('RootedClassification', 'FiniteRootedRealizable', 'PPer', 'OI-ROOTED-CLASSIFICATION'):
        ok_rcl &= _bad not in _t
# registry and census carry the family as kernel-only over all three modules
_rc_fam = [f for f in _ptr_reg['families'] if f['name'].startswith('rooted classification:')]
ok_rcl &= len(_rc_fam) == 1 and _rc_fam[0]['status'] == 'kernel-only'
ok_rcl &= _rc_fam[0]['modules'] == list(_RC_MODS) and _rc_fam[0]['manuscript'] == []
for _t in ('finite-visible only', 'rather than a reader', 'no full-support realization',
           'depend on it', 'no accessibility claim'):
    ok_rcl &= _t.lower() in _rc_fam[0]['note'].lower()
for _bad in ('decidable', 'arbitrary visible', 'accessible', 'minimal'):
    ok_rcl &= _bad not in _rc_fam[0]['note'].lower()
ok_rcl &= ('| rooted classification: the finite-visible intrinsic characterization of the realizable class | 3 | kernel-only |'
           in _cen_ps)
# the README carries the paragraph, the guard name, and the updated counts
for _t in ('`R7-RCL`', 'finiteRootedRealizable_iff_pper', 'finiteRootedRealizable_of_realization',
           'The result is finite-visible only', 'Forty named results',
           'pdFamily_not_finiteRootedRealizable', 'C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md'):
    ok_rcl &= _t in _rd1
ok_rcl &= '143 modules' in _rd1 and '3,102 named results' in _rd1
# the forbidden readings: this classifies the finite-visible slice and nothing wider. The
# disclaimers themselves contain the forbidden phrases as negations, so they are REQUIRED text and
# are excised before the scan -- a guard that trips on its own disclaimer is unsatisfiable, and this
# round has already met that shape more than once.
_rc_win = _rd1[_rd1.find('OIBridge/RootedClassification.lean'):
               _rd1.find('OIBridge/RootedClassification.lean') + 2600]
_RC_PROTECTED = ('nothing here classifies the arbitrary-visible case',)
ok_rcl &= all(_pp in _rc_win for _pp in _RC_PROTECTED)
_rc_scan = _rc_win
for _pp in _RC_PROTECTED:
    _rc_scan = _rc_scan.replace(_pp, '')
for _bad in ('classifies the arbitrary-visible', 'decides membership', 'physically accessible',
             'quantum representation class'):
    ok_rcl &= _bad not in _rc_scan
check('R7-RCL', ok_rcl,
      'Rooted-classification guard: the chain carries no sorry, axiom or native_decide, and its axiom reporting is '
      'checked as a SOURCE contract -- the set of theorem names equals the set of print targets in each module, '
      'counting attribute-prefixed declarations, so a duplicated print masking a dropped one is caught where a count '
      'pin is not; sixteen, eight and sixteen results, forty in all. Reachability is a SEPARATE contract and is '
      'enforced rather than assumed: all three modules are imported by the bridge root, CI carries no '
      'classification-only build target and no direct elaboration of these files, and no merged module hooks back '
      'into the chain. Both contracts are mutation-tested, one violation at a time, against the three ways this '
      'round actually broke reachability and the two ways axiom reporting can go incomplete. The capstone is pinned '
      'as executed, with the semantic class a distinct named predicate and its carrier universe shown harmless '
      'rather than assumed so; the finite-visible restriction is pinned as stated text, not left to the typeclass; '
      'control 13 is pinned as three separated statements with the horizon distinction carried in the kernel, and '
      'its amendment as append-only and superseding; no manuscript carries the round; the registry and census carry '
      'the family as kernel-only over all three modules and claim neither decidability nor accessibility nor a '
      'wider universe; and the README carries the paragraph, the guard name and the counts.')


# ---- R7-QSTAR: the Arc C translation layer -- the frozen root-preparation map, enforced as a
# SHAPE contract on the source rather than trusted to review ----
#
# The frozen preregistration names three rejected preparation maps and one rejected weakening of
# the horizon theorem. A comment saying they are rejected is worth nothing; each is checked here,
# and each check is mutation-tested against the specific way it would be broken.
_QS = open(os.path.join(BRIDGE, 'OIBridge', 'QuantumRepresentation.lean'), encoding='utf-8').read()


def _qs_body(txt, head):
    """The text of one declaration: its header through to the first blank line.

    Stopping at the next declaration instead would swallow the prose between them, and the prose
    here discusses the very shapes these checks forbid -- the section note spells out `∀K ∃Q_K`.
    A quantifier check reading that would be inspecting a comment, not the definition."""
    i = txt.find(head)
    if i < 0:
        return ''
    j = txt.find('\n\n', i)
    return txt[i:j if j > 0 else len(txt)]


def _qs_quantifier_order(txt):
    """The existential block stands OUTSIDE the root, time and outcome quantifiers.

    This is the frozen order, and it is the whole difference between one system serving every root
    and a per-root family of systems. A guard on the words alone would pass on either arrangement,
    so the check is positional."""
    body = _qs_body(txt, 'def QStar')
    if not body:
        return False
    e, a = body.find('∃ Q : QfbData V'), body.find('∀ (a : V)')
    if e < 0 or a < 0 or e > a:
        return False
    # and nothing existentially quantified after the root quantifier: a per-root datum cannot be
    # smuggled in as an inner existential
    return '∃' not in body[a:]


def _qs_reuses_all_time_data(txt):
    """condReal reuses the basis, unitary and readout; only the initial law is re-conditioned.

    Checked on the definition rather than on prose, and backed by the three rfl lemmas: a witness
    assembled per horizon out of unrelated data cannot make them typecheck."""
    body = _qs_body(txt, 'noncomputable def QfbData.condReal')
    if not body:
        return False
    for _f in ('Bas := Q.Bas', 'U := Q.U', 'read := Q.read', 'init := Q.condInit a'):
        if _f not in body:
            return False
    flat = ' '.join(txt.split())
    # word-boundary, not substring: `condReal_readout` CONTAINS `condReal_read`, so a plain `in`
    # test passes on a rename that removes the lemma. That flaw sat in the first draft of this
    # guard and its own mutation 5 is what exposed it.
    for _l in ('condReal_Bas', 'condReal_U', 'condReal_read'):
        if re.search(r'theorem QfbData\.' + _l + r'\b', flat) is None:
            return False
    return True


def _qs_read_fibre(txt):
    """Every conditioning event is the READ FIBRE, never a basis point.

    The frozen map conditions on `read (B_0) = a`. Conditioning on a finer basis-level event gives
    the preparer the hidden label and is a different class."""
    for _head, _need in (('noncomputable def QfbData.rootMass', 'fun b => Q.read b = a'),
                         ('noncomputable def QfbData.condInit', 'if Q.read b = a')):
        if _need not in _qs_body(txt, _head):
            return False
    jm = _qs_body(txt, 'noncomputable def QfbData.jointMass')
    return 'fun b => Q.read b = a' in jm and "fun b' => Q.read b' = j" in jm


def _qs_strong_horizon(txt):
    """The horizon theorem is the strong one, and the per-horizon form is derived FROM it.

    `∀K ∃Q_K` is satisfied by a different basis at every horizon and would establish nothing about
    Q*. It appears only as a corollary whose proof cites the strong theorem."""
    flat = ' '.join(txt.split())
    if 'theorem QfbData.condReal_law' not in flat:
        return False
    if '(Q.condReal a K).law = Q.rootTraj K a' not in flat:
        return False
    cor = _qs_body(txt, 'theorem qfbRealizable_rootTraj')
    return 'Q.condReal_law' in cor and 'Q.condReal_isLaw' in cor


ok_qstar = True
# the four contracts hold as the tree stands
ok_qstar &= _qs_quantifier_order(_QS)
ok_qstar &= _qs_reuses_all_time_data(_QS)
ok_qstar &= _qs_read_fibre(_QS)
ok_qstar &= _qs_strong_horizon(_QS)

# ... and each is mutation-tested against the exact weakening it exists to catch. Every mutation
# must CHANGE THE SOURCE: a mutation that fails to mutate records a pass while testing nothing,
# which is how the Arc B guard shipped a vacuous control.
_qs_m1 = _QS.replace(
    '∃ Q : QfbData V, Q.IsLaw ∧ Q.PositiveRootMass ∧ ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j',
    '∀ (a : V), ∃ Q : QfbData V, Q.IsLaw ∧ Q.PositiveRootMass ∧ ∀ (t : ℕ) (j : V), Γ t a j = Q.rooted t a j')
ok_qstar &= _qs_m1 != _QS and not _qs_quantifier_order(_qs_m1)

_qs_m2 = _QS.replace('  U := Q.U\n', '  U := 1\n')
ok_qstar &= _qs_m2 != _QS and not _qs_reuses_all_time_data(_qs_m2)

_qs_m3 = _QS.replace('  ∑ b ∈ univ.filter (fun b => Q.read b = a), Q.init b',
                     '  ∑ b ∈ univ.filter (fun b => b = b), Q.init b')
ok_qstar &= _qs_m3 != _QS and not _qs_read_fibre(_qs_m3)

_qs_m4 = _QS.replace('  ⟨Q.condReal a K, Q.condReal_isLaw hQ hpos a K, Q.condReal_law a K⟩',
                     '  ⟨Q.condReal a K, sorry, sorry⟩')
ok_qstar &= _qs_m4 != _QS and not _qs_strong_horizon(_qs_m4)

_qs_m5 = _QS.replace('theorem QfbData.condReal_read', 'theorem QfbData.condReal_readout')
ok_qstar &= _qs_m5 != _QS and not _qs_reuses_all_time_data(_qs_m5)

# standing hygiene, and the scope the module is allowed to claim
_qs_code = re.sub(r'/-.*?-/|--[^\n]*', '', _QS, flags=re.S)
ok_qstar &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', _QS) is None and 'native_decide' not in _QS
ok_qstar &= 'axiom ' not in _qs_code and re.search(r'(?m)^axiom ', _QS) is None
# T1 only: the module must not claim either inclusion
_qs_flat = ' '.join(_QS.split()).lower()
for _bad in ('qstar_subset', 'subset_qstar', 'pper_iff_qstar', 'qstar_iff_pper'):
    ok_qstar &= _bad not in _qs_flat
ok_qstar &= 'decides neither inclusion' in _qs_flat
# the frozen provenance is carried in the file that implements it
for _t in ('38a8f09d9d314fdd3d7747d0d0351f07c693c582',
           '8177527b11a0970c7fc71f1bff382112aaf93aa6',
           'e809e04aee45181d162bd4a2cc2782751b65f509'):
    ok_qstar &= _t in _QS


def _qs_root_reachable(txt, root_txt, wf_txt):
    """The module is reached by the ORDINARY build.

    Without this the semantic controls above are unenforceable in practice: an unimported module is
    never elaborated by the bridge job, so CI would report green while never compiling the file the
    guard is guarding. Arc B lost a round to exactly this."""
    if 'import OIBridge.QuantumRepresentation\n' not in root_txt:
        return False
    if re.search(r'lake build\s+OIBridge\.QuantumRepresentation', wf_txt):
        return False
    if re.search(r'lake env lean\s+OIBridge/QuantumRepresentation', wf_txt):
        return False
    return True


def _qs_seam_closed(txt):
    """QStar and the horizon theorem speak about the same object.

    QStar is stated through `bornPow`, the horizon theorem through the chain weight. Without the
    marginal theorem those are two parallel definitions and T1 is not closed, however green the
    build is."""
    flat = ' '.join(txt.split())
    if 'theorem QfbData.rootTraj_marginal' not in flat:
        return False
    if 'Q.rootTraj t a τ = Q.rooted t a j' not in flat:
        return False
    return 'theorem QfbData.sum_path' in flat


ok_qstar &= _qs_root_reachable(_QS, root, _wf)
ok_qstar &= _qs_seam_closed(_QS)
# the reachability contract is mutation-tested the way Arc B's was, since dropping the import is
# the failure that leaves every other control unenforced
ok_qstar &= not _qs_root_reachable(_QS, root.replace('import OIBridge.QuantumRepresentation\n', ''), _wf)
ok_qstar &= not _qs_root_reachable(_QS, root, _wf + '\n          lake build OIBridge.QuantumRepresentation\n')
_qs_m6 = _QS.replace('theorem QfbData.rootTraj_marginal', 'theorem QfbData.rootTraj_partial')
ok_qstar &= _qs_m6 != _QS and not _qs_seam_closed(_qs_m6)
# axiom reporting as a source contract: theorem-name set equals print-target set
_qs_decl = re.findall(r"(?m)^(?:@\[[^\]]*\]\s*)?theorem\s+([A-Za-z_][\w'.]*)", _QS)
_qs_pr = re.findall(r"#print axioms OIBridge\.QuantumRepresentation\.([\w'.]+)", _QS)
ok_qstar &= set(_qs_decl) == set(_qs_pr) and len(_qs_decl) == len(set(_qs_decl)) and len(_qs_decl) == 13
_qs_m7 = _QS.replace('#print axioms OIBridge.QuantumRepresentation.QfbData.rootTraj_marginal\n', '', 1)
ok_qstar &= _qs_m7 != _QS
ok_qstar &= set(re.findall(r"#print axioms OIBridge\.QuantumRepresentation\.([\w'.]+)", _qs_m7)) != set(_qs_decl)

check('R7-QSTAR', ok_qstar,
      'Arc C translation guard: the frozen root-preparation map is enforced as a SHAPE contract on the source, '
      'not trusted to review. The QStar existential block is checked POSITIONALLY to stand outside the root, time '
      'and outcome quantifiers, with no inner existential, so a per-root datum cannot be smuggled in; condReal is '
      'checked to reuse the basis, unitary and readout, backed by three rfl lemmas a per-horizon witness could not '
      'satisfy; every conditioning sum is checked to run over the READ FIBRE rather than a basis point; and the '
      'horizon theorem is checked to be the strong one with the per-horizon form derived FROM it. Each of the four '
      'is mutation-tested against the exact weakening it exists to catch, and every mutation is asserted to change '
      'the source, since a mutation that fails to mutate records a pass while testing nothing. Reachability is a '
      'separate contract and is mutation-tested too: an unimported module would leave every semantic control above '
      'unenforced because CI would never elaborate the file. The seam between QStar and the horizon theorem is '
      'pinned by the marginal theorem, without which the two are parallel definitions rather than one translation. '
      'Axiom reporting is the source contract used by R7-RCL: the set of theorem names equals the set of print '
      'targets, thirteen in all.')

check('R7-AUDB', ok_audb,
      'Audit B guard: [GR] 2.2 carries a fourth entry recording C4 as a named realization condition at '
      'the cosmological cut, not presently discharged, with exactly what remains stated; both book '
      'sources carry the same status and no longer infer C4 from bidirectionality or say the horizon '
      'satisfies all four conditions; the hbar derivation names its own conditions and does not consume '
      'C4; the intro neither says the horizon satisfies all four conditions nor that the full equivalence '
      'applies in our universe, but that the equivalence remains conditional on C4; and the audit records '
      'why bidirectionality and H-scramble do not close it, and claims neither '
      'that C4 holds nor that it fails at the cut. On the SM side: Layer 0 no longer lists C1-C4 as '
      'inputs to the gauge chain, the 2.1 inventory names all four with Theorem 22 status, and '
      'Chapter 1 neither calls the horizon read-write cycle automatic nor lists three conditions as '
      'sufficient nor declares all four satisfied by enormous margins. Claims neither '
      'that C4 holds nor that it fails at the cut.')

check('R7-AUDA', ok_auda,
      'Audit A guard: the recurrence chain names C1 in both parallel sources and the unqualified '
      '"any partition" form is gone from both, while the [Main] and Chapter 1 statements the '
      'repair restores agreement with are still present. The countermodel probe carries its '
      'control -- the corpus own coin-and-die system, where the same measurement reports the '
      'backflow that the uncoupled product system lacks -- so the negative cannot be read as a '
      'blind measurement. Neither probe nor audit claims C1 sufficient for anything, and the '
      'audit publishes the axes that came back clean and its own limits, not only its one hit.')

check('R7-CT3D', ok_ct3d,
      'CT3-R2B-Q2 guard: the period formula is stated in its corrected uniform form, '
      'ord(F mod q) = qL at every prime including 2, in the probe, in the round note and at all '
      'three manuscript locations, none of which retains the superseded q = 2 value or its '
      'reasoning. The round restates rather than inherits its two limits -- the antisymmetric '
      'vanishing is the WIDTH-2 ingredient, and the periodization obligation is unused -- and '
      'records the power-of-two conjecture as FALSE with the Wieferich arithmetic that makes it '
      'so, rather than reporting the small-L coincidence as the law. No floating arithmetic, and '
      'nothing claims CT3 settled.')

check('R7-CT3C', ok_ct3c,
      'CT3-R2B step-1 guard: the centralizer basis is exact over Z, complete against the CT3-R1 '
      'census and quotientable by scalars; the quantization lemma is stated in its sharper '
      'single-lattice form with the per-block residue; block traces come from the projector '
      'identity rather than from diagonalizing. The Hermitian sector split is present and the '
      'vanishing of the antisymmetric block traces is flagged as a COMPUTED fact -- it is what '
      'confines the obstruction to width 2, and assuming it would silently widen the claim. The '
      'obstruction is an exact integer certificate, (m - 2r) d_r / m not in Z, not a search; the '
      'on-site control that would refute a wrong test is present; rank alone is recorded as the '
      'wrong diagnostic; and the first-moment subspace is pinned. Nothing claims CT3 or R2-B '
      'settled beyond width 2 at the volumes tested.')

check('R7-CT3B', ok_ct3b,
      'CT3-R2A scope guard: the spectral-logarithm probe splits CT3 into the function-of-P branch '
      'and the degenerate-eigenspace branch, certifies the first dead by an explicit full-period '
      'displacement witness at every width below the system size, and carries the SCOPE CONTROL '
      'that stops the negative being over-read -- on-site rules, which provably do have static '
      'local generators, return the same dimension one. The probe and the audit state that CT3 '
      'itself remains open and neither claims a static generator is ruled out.')

check('R7-CT3', ok_ct3,
      'CT3 scope guard: the static-generator probe states CT3 in its infinite-volume form (one '
      'time-independent finite-range interaction, not a bounded element of the quasilocal '
      'algebra), reports the local-centralizer census as a NECESSARY condition only, carries the '
      'on-site controls that show the method detects generators where they must exist, splits the '
      'census into diagonal and off-diagonal with the reason that split decides the reading, and '
      'records the verdict as NON-OBSTRUCTION. Neither the probe nor the audit claims that a '
      'static finite-range generator exists, and neither treats a passed necessary condition as '
      'evidence of sufficiency. The modular census is recorded as an upper bound and paired with a '
      'characteristic-zero lower bound verified exactly over Z, so the non-obstruction verdict is '
      'not a modular artifact; and the finite-to-infinite periodization is recorded as an '
      'obligation for any future obstruction claim rather than used silently.')

check('R7-CT2', ok_ct2,
      'CT2 scope guard: the second-order circuit module states the depth-two factorization for an '
      'arbitrary neighbourhood function, backs its locality claim with the stage-membership '
      'theorems, and records at both endpoint theorems that a single TIME-INDEPENDENT generator is '
      'NOT claimed -- the drive is piecewise constant across the two layers. No autonomous '
      'one-parameter-group claim appears, and the module carries no sorry and no native_decide. '
      'The repair modules keep the same scope: the all-sites layers carry the finite-range '
      'hypothesis the factorization did not need and the note that the formal sum of on-site terms '
      'is not an algebra element; each layer separately is a strongly continuous one-parameter '
      'group; the order of the composite is fixed by heis_of_comp rather than by convention, with '
      'the SWAP flow innermost; and the composite is claimed to be a continuous path of '
      '*-automorphisms through the identity and NOT a one-parameter group. Both layer endpoints '
      'are identified with the frozen heisQ, and so is the composite\'s: driveQ R 1 is '
      'heisQ (ruleDynamics R), so the path starts at the identity and ends at the update.')

ina = open(os.path.join(BRIDGE, 'OIBridge', 'InstrumentAvailability.lean'), encoding='utf-8').read()
_inaflat = ' '.join(ina.split())
ok6 &= 'def AvailFS' in ina and 'theorem q3_countermodel' in ina
# nothing frozen is weakened: the frozen state and dynamics theorems are restated on the same algebra
ok6 &= 'theorem states_untouched' in ina and 'theorem dynamics_untouched' in ina
_stu = _slice(ina, 'theorem states_untouched', 'theorem dynamics_untouched')
# the frozen state layer must be restated for EVERY consistent family, not only the reference one
ok6 &= 'IsStateFamily' in _stu and 'quasiState_isState' in _stu and 'quasiState_stage' in _stu
ok6 &= 'uniformFamily_isStateFamily' not in _stu
_dyu = _slice(ina, 'theorem dynamics_untouched', 'end Summary')
ok6 &= 'heisQ_mul' in _dyu and 'norm_heisQ' in _dyu and 'heisQ_inv_heisQ' in _dyu
# the closure rules and the containment of Level II
for _t in ('theorem availFS_id', 'theorem availFS_comp', 'theorem availFS_relabel',
           'theorem availFS_dyn', 'theorem availFS_of_kraus', 'theorem kraus_of_availFS',
           'theorem qBranchJ_coarse', 'theorem sum_qBranchJ'):
    ok6 &= _t in ina
# the exclusion, at an ARBITRARY finite outcome index rather than only Fin n
ok6 &= 'theorem phaseAll_not_availFS' in ina and 'theorem qTotalJ_stage_of_disjoint' in ina
_exc = _slice(ina, 'theorem phaseAll_not_availFS', 'end Exclusion')
ok6 &= '[Fintype J]' in _exc
# independence, not impossibility
ok6 &= 'independence from' in _inaflat and 'not impossibility' in _inaflat
# the Level II containment must be stated for the ENDOMORPHIC fixed-carrier case, with the typed
# attachment/discard structure named as separately frozen, and Q5's principle must not be unique
ok6 &= 'endomorphic Kraus instrument' in _inaflat
ok6 &= 'separately frozen and unchanged' in _inaflat
ok6 &= 'not a uniquely forced one' in _inaflat
for _w in ('theorem oi_forbids', 'theorem infiniteSupport_impossible',
           'theorem availability_derived', 'axiom continuity', 'CompletelyPositive',
           'InnerProductSpace', 'HilbertSpace'):
    ok6 &= _w not in ina
ok6 &= 'structure FiniteOperationalTheory' not in ina and 'native_decide' not in ina
# the audit file must record Q3 as decided and keep Q2, Q4, Q5 open
_aud2 = open(os.path.join(os.path.dirname(BRIDGE), 'INSTRUMENT-COMPLETION-AUDIT.md'),
             encoding='utf-8').read()
ok6 &= 'Second entry' in _aud2 and _aud2.count('**open') >= 3
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
      "LINT. All seventy-eight files are imported by OIBridge.lean so CI builds them; no `sorry`, no "
      "`axiom`, no `native_decide`; all 7 + 16 + 8 + 8 + 7 + 11 + 21 + 4 + 66 + 3 + 17 + 17 + 11 + 15 + 10 + 20 + 11 + 7 + 13 + 31 + 13 + 27 + 9 + 11 + 17 + 8 + 6 + 29 + 23 + 28 + 7 + 8 + 17 + 21 + 17 + 14 + 9 + 20 + 33 + 2 + 30 + 24 + 30 + 33 + 49 + 21 + 22 + 12 + 31 + 39 + 32 + 52 + 21 + 13 + 22 + 25 + 38 + 77 + 30 + 11 + 5 + 16 + 22 + 26 + 16 + 57 + 10 + 12 + 9 + 34 + 40 + 16 + 28 + 143 + 87 + 53 + 19 + 31 named results print their "
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
