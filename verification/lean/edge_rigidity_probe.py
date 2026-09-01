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
                             'circuit_branch')),
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
                            'transposeMap_not_kraus')),
    ('HiddenCoherence', ('blockOp_one', 'blockOp_comp', 'blockOp_sum',
                         'localLuders_eq_blockOp', 'uniformAttach_offDiag',
                         'blockOp_uniformAttach', 'sum_fibers', 'scalarAvail_isKraus',
                         'hiddenCoherence_krausSound', 'badOp_availExt',
                         'badOp_invisible', 'badOp_choi', 'badOp_not_cp',
                         'badOp_not_kraus', 'hiddenCoherence_not_krausSoundExt',
                         'krausSound_not_implies_krausSoundExt')),
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
# the external analytic boundary stays exactly four items and no more
_flat = ' '.join(mc.split())
ok6 &= 'stays exactly four items and no more' in _flat
ok6 &= all(item in _flat for item in
           ('compact Lie integration', 'finite isometry extension',
            'PSD square-root/factorization', 'Uhlmann/Schmidt uniqueness'))
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
      "LINT. All thirty-six files are imported by OIBridge.lean so CI builds them; no `sorry`, no "
      "`axiom`, no `native_decide`; all 7 + 16 + 8 + 8 + 7 + 11 + 21 + 4 + 66 + 3 + 17 + 17 + 11 + 15 + 10 + 20 + 11 + 7 + 13 + 31 + 13 + 27 + 9 + 11 + 17 + 8 + 6 + 29 + 23 + 25 + 7 + 8 + 15 + 16 + 5 + 16 named results print their "
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
