#!/usr/bin/env python3
"""E1_build_part.py - assemble evidence/part-E1.json from the outputs of
E1_decls.py, E1_logreports.py (one per job log) and E1_crosscheck.py, the
audit's matrix.json, and the formal-coverage readings recorded below (each
reading was made against the source at eae01647 and is stated per declaration).

Usage:
    python3 -I E1_build_part.py --decls decls.json --matrix matrix.json \
        --rep17 rep-121598983127.json --repeae rep-121827872751.json \
        --rep02e rep-121840956899.json --cross crosscheck.json > part-E1.json
"""
import json
import sys

RUN17, JOB17 = '40330683786', '121598983127'
RUNEAE, JOBEAE = '40395660130', '121827872751'
RUN02E, JOB02E = '40399411290', '121840956899'
ALLOW = ['propext', 'Classical.choice', 'Quot.sound']

# FINDINGS ids (replacement texts, evidence lists, optional changes) per declaration.
FINDINGS = {
    'pIndivisible_of_rooted_identity_return_of_overlap': ['R-12'],
    'RootedRealization': ['R-12'],
    'routed_forces_indivisible_somewhere': ['R-13', 'OD-5'],
    'routedAtStorage_forces_indivisible_somewhere': ['R-13', 'OD-5', 'OD-15'],
    'RoutedReadback': ['R-13'],
    'card_hidden_ge_two_pow_Istar': ['R-22'],
    'c3_necessity': ['R-22'],
    'qStar_not_subset_finiteRootedRealizable': ['R-05'],
    'finiteRootedRealizable_iff_pper': ['R-09', 'O-6', 'OD-4'],
    'responseRealization': ['R-08'],
    'realizesSealedOICore_of_control': ['R-06', 'OD-2', 'OD-15'],
    'HasCompositeUnitaryControl': ['R-06'],
    'PhysicalCompletionConditions': ['R-06'],
    'permClass_onesFixing': ['R-06', 'OD-15'],
    'onesFixing_not_phasesAvailable': ['R-06', 'OD-15'],
    'substratumClass_not_onesFixing': ['R-06'],
    'substratumClass_not_drivesElementary': ['R-06'],
    'monomialSource_not_control': ['R-06', 'OD-15'],
    'readWriteSourced_not_control': ['R-06'],
    'readWriteSourced_not_qm': ['R-06'],
    'substratum_residual': ['R-06', 'OD-15'],
    'substratum_extension_quantum_iff_drives': ['R-06'],
    'substratum_plus_control_qm': ['R-06', 'OD-15'],
    'frozen_sourcing_verdict': ['R-06', 'OD-2'],
    'determinism_reversibility_selected_measure': ['O-5'],
    'continuous_extension_not_unique': ['O-14'],
    'exactAll_iff_physical_general': ['R-05'],
}

# Formal-coverage readings: (outcome, what the source states, how it matches, limits/modelling premises).
COV = {
    'finite_horizon_equivalence': ('pass',
        'For every K and every P : Traj V K -> R (V a Fintype with DecidableEq): (Stochastic P <-> RevRealizable P) and (RevRealizable P <-> QfbRealizable P) and (QfbRealizable P <-> Stochastic P). Only P is an argument; lines 466-468 are the proof term, each reverse arrow a composition of the three inclusions.',
        'Matches Theorem 1 (S_K = D_K = Q_K, each the set of all probability laws on C_V^{K+1}), "the reverse inclusions as their compositions" and "no construction enters as a hypothesis".',
        'Modelling premises: finite alphabets (Fintype V, finite Hid, finite basis); reversible dynamics = an Equiv of V x Hid; Q_K reads out in one fixed basis at every step. The kernel needs no |C_V| >= 2 (the Introduction\'s |C_V| >= 2 is narrower, harmless).'),
    'S_imp_D': ('pass',
        'Stochastic P -> RevRealizable P: an Equiv of V x Hid (Hid = clock x trajectory record, padded to a bijection) and an initial law on V x Hid that need not factor.',
        'Matches S_K subset D_K and the realization description at L56 (sampled trajectory with a clock in the hidden register; correlated initial law, as D_K at L43 allows).',
        'The independent-prior form is not stated in the kernel (Equivalence.lean:150-156 says so); the Introduction says it is proved on paper.'),
    'D_imp_Qfb': ('pass',
        'RevRealizable P -> QfbRealizable P with U = permMatrix of step^-1, init = the joint initial law on V x Hid (diagonal weights), read = Prod.fst.',
        'Matches D_K subset Q_K and the permutation-unitary representation read out in the configuration basis at every step (L58).',
        'Modelling premise: the unitary supplied is a permutation matrix (entries 0 and 1), as L66 states.'),
    'Qfb_imp_S': ('pass',
        'QfbRealizable P -> Stochastic P; normalisation from unitarity of U (QfbReal.sum_born) through the every-step Born chain.',
        'Matches Q_K subset S_K ("is the Born rule", L58).', ''),
    'permMatrix_mem_unitaryGroup': ('pass',
        'For phi : Equiv.Perm (V x H), phi.permMatrix C is in the unitary group.',
        'Supporting lemma of Theorem 1 as Appendix A states; used by D_imp_Qfb (Equivalence.lean:340).',
        'Its short name collides with another `#print axioms` target in the tree, so the gate\'s SILENT check cannot certify its report by name; the retained result and all three job logs carry its report at EquivalenceChain:392.'),
    'pushforward_identity': ('pass',
        'For a Realization R (step : V x H ~ V x H; a joint law w on Hist x V x H, nonnegative, total 1) and any p, x: nextLaw R p x = marg (post R p x) (nextVis R x), with nextVis x h = (step (x,h)).1.',
        'Matches Theorem 2(a) for a joint law of history, present and hidden state, as L80 restricts it.',
        'post and nextLaw divide by the history weight; for a zero-weight history both sides are the zero function (Lean division by zero), so the identity is vacuous there. The time-t identification with a realization run from time 0 is not formalized, as L80 states.'),
    'distinguishability_floor': ('pass',
        'tv (nextLaw R p x) (nextLaw R p\' x) <= tv (post R p x) (post R p\' x), tv = half the l1 distance.',
        'Matches Theorem 2(b) for histories p, p\' ending at x.', 'Same joint-law scope as (a).'),
    'capacity_floor': ('pass',
        '[Nonempty H]: memory R <= cmiBits w X_<t X_t H_t and cmiBits w X_<t X_t H_t <= logb 2 |H|, with cmi w a b c = I(a; c | b) (FiniteEntropy:352) in bits.',
        'Matches Theorem 2(c): M_t <= I(X_<t; H_t | X_t) <= log2 |C_H|. memory (HiddenMemory:138) is I(X_<t; X_{t+1} | X_t) with X_{t+1} defined from phi.',
        'Same joint-law scope.'),
    'unavoidable_hidden_predictive_memory': ('pass',
        'The conjunction of (a), (b) and (c) above for one Realization.', 'Matches Theorem 2 as bundled.', 'Same joint-law scope.'),
    'c3_necessity': ('partial',
        '[Nonempty H]: cmiBits w X_<t X_t (varFuture R L) <= logb 2 |H|, the visible future of finite length L read off (X_t, H_t).',
        'Supports L84 in the joint-law form of Theorem 2.',
        'L84 does not define I*; Main.md:492 defines I* = sup_t I(X_<t; X_>t | X_t). The kernel bounds finite-length futures, and card_hidden_ge_two_pow_Istar takes the maximum over a finite nonempty family; an infinite-future or infinite-family supremum is not stated (R-22).'),
    'card_hidden_ge_two_pow_Istar': ('partial',
        '[Nonempty H], F a nonempty Finset, R : i -> Realization Hist V H, L : i -> N: 2^(Istar) <= |H|, Istar = F.sup\' of cmiBits w X_<t X_t (varFuture (R i) (L i)).',
        'Supports "needs |C_H| >= 2^{I*} (machine-checked in the same form as Theorem 2)" for I* a maximum over finitely many joint laws and finite future lengths.',
        'Same limit as c3_necessity: the Introduction leaves I* undefined (R-22); for a finite-horizon law the supremum is a finite maximum and the forms agree.'),
    'isPermMatrix_of_stochastic_inverse': ('pass',
        'A, B in rowStochastic R n (n a Fintype), A * B = 1 or B * A = 1 -> exists sigma, A = sigma.permMatrix R.',
        'Matches L96: a finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix.',
        'No other module uses it: the kernel route from routed readback to indivisibility (PhysicalC4Discharge, PhysicalC4StorageReadback) goes through RecurrenceHorizon and does not invoke this lemma. L96 says "by the route of Theorem 3", which is accurate; "With this lemma" describes Main\'s written proof.'),
    'pIndivisible_of_rooted_identity_return_of_overlap': ('pass',
        'R : RootedRealization V H (an Equiv of V x H and one prior on H shared by every root), s < n, rootedMap R n = 1, a != b, 0 < rootedMap R s a x, 0 < rootedMap R s b x -> PIndivisibleWithin n (rootedMap R), i.e. not (forall s < t <= n, exists row-stochastic Lambda, Gamma t = Gamma s * Lambda).',
        'Matches Theorem 3 (L92) with the rooted definitions of L90 exactly; "fixed hidden prior" is RootedRealization.prior, "shared by every root" (CausalReadback:181).',
        'Reversibility is not used beyond making Gamma_s row-stochastic (RecurrenceHorizon section B docstring). Census family kernel-only (OD-4).'),
    'routed_forces_indivisible_somewhere': ('partial',
        'RoutedReadback K R -> exists n, PIndivisibleWithin n (rootedMap R).',
        'The conclusion matches "readback forces indivisibility somewhere in the recurrence cycle", proved by the route of Theorem 3.',
        'RoutedReadback\'s store clause is the seed-posterior spelling, which PhysicalC4Discharge.lean:27-29 records differs from the storage-time clause; L96\'s gloss ("a visible-history record written into the hidden state is read back later") matches PhysicalC4StorageReadback:256 instead (R-13). The proof extracts only the overlap clause (routedReadback_overlap, :88-92) plus finite recurrence (rootedMap_periodic); the write, store and read-effect clauses are not used, so the kernel shows indivisibility follows from a weaker hypothesis than readback.'),
    'routedAtStorage_forces_indivisible_somewhere': ('pass',
        'RoutedReadbackAtStorage K R -> exists n, PIndivisibleWithin n (rootedMap R).',
        'Its store clause is Law(H_s | X_s = x, X_0 = a), the storage-time reading, which matches L96\'s gloss (R-13, OD-5).',
        'As for the seed-posterior form, the proof uses only the overlap clause (routedReadbackAtStorage_overlap) plus finite recurrence. Census family kernel-only (OD-4).'),
    'gl2_strong_gauge_moves_relative_candidate': ('partial',
        'Exists Gamma : N -> Matrix (Fin 2) (Fin 2) R and U, U\', K : N -> Matrix (Fin 2 x Fin 2) ... with CoherentLift 0 Gamma U, CoherentLift 0 Gamma U\', every K t in the strong anchor stabilizer, U\' t = U t * K t, K t != K s for some t, s, and readback of |U 1 (U 0)^H|^2 != readback of |U\' 1 (U\' 0)^H|^2.',
        'Matches "two coherent lifts of one visible family ... can differ by a time-dependent right action invisible to the visible law and then have different relating evolutions" as an existence statement; the kernel shows even the visible readback of the relating candidate differs.',
        'CoherentLift (CoherentLiftGauge:124) is pointwise admissibility at every time (AdmissibleDilationAt, DilationChoice:134); it does not encode "compose exactly across times", and the GL2 docstring (:528-529) records that the cocycle condition is not used because it is vacuous, holding for every family. One explicit witness (|V| = 2, a period-two family, one time pair).'),
    'gl3_constant_gauge_preserves_relative': ('pass',
        'K unitary on V x A, any U : N -> Matrix: (U t * K) * (U s * K)^H = U t * (U s)^H.',
        'Matches "a constant deformation cancels from every relating evolution".', 'Necessity only, as the module states.'),
    'bridge_traj': ('pass',
        'U, U\' trivial-ancilla admissible dilations of the same slice G (pad, anchor (0,0)), M, N in permClass V: (realData (M * U * N)).rootTraj K a = (realData (M * U\' * N)).rootTraj K a for every K, a.',
        'Matches L126 ("same one-step visible matrix -> root-conditioned trajectory laws agree at every horizon"); the kernel adds permClass interventions on either side, which specialise to the stated case with M = N = 1.',
        ''),
    'rooted_eq_iff_slice_eq': ('pass',
        'For trivial-ancilla admissible dilations U of G and U\' of G\': (forall t a j, rooted families of realData U and realData U\' agree) <-> G = G\'.',
        'The forward direction matches L126 as cited ("forward direction").', ''),
    'realData_traj_stochastic': ('pass',
        '[Nonempty V], U unitary: for every K, a, (realData U).rootTraj K a is QfbRealizable and Stochastic.',
        'Matches "each such trajectory law is fixed-basis realizable and stochastic".', 'Needs V nonempty (uniform initial law 1/|V|).'),
    'realData': ('pass',
        'realData U: basis V, evolution U, initial law 1/|V| (uniform), readout id.',
        'Matches L126 ("uniform initial law and identity readout").', ''),
    'exactAll_iff_physical_general': ('pass',
        'A : Type, [Fintype A] [DecidableEq A] [Nonempty A] (section General): ExactAllFiniteEndomorphicQuantumOps T <-> PhysicalCompletionConditions T, proof term <physical_of_exactAll T, exactAll_of_physical_general T>.',
        'Matches Theorem 4 for every nonempty finite system, both directions with separate witnesses (section A.34). ExactAll = system exactness and exactness at every level k+1, each "available iff IsFiniteEndomorphicKrausInstrument" with sum K^H K = 1.',
        'Outcome sets are quantified as Fin m; relabelling to any finite outcome set follows from avail_coarse with a bijection. FiniteOperationalTheory (OperationalAssembly:594) is the premise structure: identity; coarse-graining on the system and every level; outcome-conditioned composition at every ancilla level; uniformly mixed ancilla preparation, post-composition; spectator-independent readout; ancilla discard. These match L114 clause by clause.'),
    'physical_of_exactAll': ('pass',
        '[Nonempty A] (section Necessity, PhysicalCharacterization:224): ExactAllFiniteEndomorphicQuantumOps T -> PhysicalCompletionConditions T.',
        'Matches the => direction (L118).', ''),
    'exactAll_of_physical_general': ('pass',
        '[Nonempty A]: PhysicalCompletionConditions T -> ExactAllFiniteEndomorphicQuantumOps T, via exactAll_of_levelOne, exactComposite_of_validity_general (krausSoundExt_of_validity_inert, compositeCompleteness_unconditional).',
        'Matches the <= direction (L118) and the route Appendix A names.', ''),
    'PhysicalCompletionConditions': ('pass',
        'CompositeOperationalValidity T and InertSpectatorCompositionality T and HasCompositeUnitaryControl T and IteratedAncillaClosure T and SystemToLevelOne T.',
        'Matches (i)-(v) at L114: (i) PSD-preserving branches with trace-summing outcomes at every ancilla level (OperationalValidity:88); (ii) SystemToLevelOne (LevelOneSeam:117); (iii) inert spectator (SpectatorBridge:223); (iv) every unitary at every level (OperationalAssembly:665); (v) uniform-ancilla attach-act-discard closure (AncillaClosure:247).',
        'Positivity in (i) is per-branch PSD preservation at every ancilla level, which is how L114 phrases it.'),
    'krausSoundExt_of_validity_inert': ('pass',
        '[Nonempty A]: CompositeOperationalValidity T -> InertSpectatorCompositionality T -> KrausSoundExt T.',
        'Supporting step of <= as Appendix A states.', ''),
    'compositeCompleteness_unconditional': ('pass',
        'HasCompositeUnitaryControl T -> InertSpectatorCompositionality T -> IteratedAncillaClosure T -> HasFullCompositeInstruments T; no isometry-extension hypothesis.',
        'Supporting step of <=, "premise discharged by finiteIsometryExtensionSF_discharged".', ''),
    'finiteIsometryExtensionSF_discharged': ('pass',
        'For every finite A with DecidableEq: FiniteIsometryExtensionSF A.', 'Discharges the premise as Appendix A states.', ''),
    'exactAll_of_levelOne': ('pass',
        'SystemToLevelOne T -> ExactCompositeQuantumOps T -> ExactAllFiniteEndomorphicQuantumOps T.', 'Supporting step of <=.', ''),
    'exactComposite_of_validity_general': ('pass',
        'Validity, inert spectators, composite control and iterated ancilla closure -> ExactCompositeQuantumOps T, for every nonempty finite A.',
        'Consumes krausSoundExt_of_validity_inert as the matrix states (I-339).', ''),
    'five_way_minimality': ('pass',
        'Five existentials over FiniteOperationalTheory (Fin 2): for each of the five conditions, a theory satisfying the other four and RealizesSealedOICore and failing that one.',
        'Matches L120: on the qubit, each condition is independent of the other four and of a fixed finite observation process satisfying (C1)-(C4).',
        'RealizesSealedOICore (OIRealization:234) fixes one sealed core (CoreC1C4, IndependenceCensus:187) on a 4-level ancilla; independence is relative to that one process, as "a fixed finite observation process" says.'),
    'oi_alone_not_qm': ('pass',
        'Exists T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T and not ExactAllFiniteEndomorphicQuantumOps T (witness diagTheory).',
        'Matches "a qubit theory that never creates coherence realizes the observation process and is not quantum": diagTheory\'s availability is Kraus/CP families preserving diagonal states (DiagonalTheory:246).', ''),
    'PDivisible': ('partial',
        'PDivisible K Gamma := forall s t, s < t -> t <= K -> exists Lambda, IsRowStochastic Lambda and Gamma t = Gamma s * Lambda.',
        'Matches the definition at L90 exactly.',
        'Locator: the matrix cites CausalReadback:52, which is the docstring; the def is at :54. Census family kernel-only.'),
    'tv_mul_le': ('pass',
        'Lambda row-stochastic: tv (p Lambda) (q Lambda) <= tv p q.',
        'Matches "a stochastic divisor contracts total variation" (L90) and the necessity direction at L94.', ''),
    'RootedRealization': ('pass',
        'structure: step : V x H ~ V x H; prior : H -> R, nonnegative, summing to 1, "shared by every root".',
        'Matches "a bijection ... with a fixed hidden prior" (L92) and R-12\'s "hidden prior independent of x_0".', ''),
    'Stochastic': ('pass', 'Stochastic P := (forall tau, 0 <= P tau) and sum P = 1.', 'Matches S_K (L42).', ''),
    'RevReal': ('pass', 'structure: finite Hid, step : (V x Hid) ~ (V x Hid), init : V x Hid -> R (IsLaw separately); law = pushforward along the visible trajectory.',
        'Matches D_K (L43) and the faithful-realization definition (L30), including the correlated initial law.', ''),
    'QfbReal': ('pass', 'structure: finite Bas, U : Matrix Bas Bas C, init : Bas -> R, read : Bas -> V; IsLaw = U unitary and init a probability law; law = marginal of the every-step Born chain.',
        'Matches Q_K (L44): fixed basis, initial state diagonal in it, Born readout at every step, record a fixed function of each outcome.', ''),
    'QfbReal.born': ('pass', 'born b b\' := ||U b\' b||^2.', 'Matches "p = |U|^2 is part of the definition of Q_K" (L66).', ''),
    'QfbReal.chain': ('pass', 'chain sigma := init (sigma 0) * prod_k born (sigma k) (sigma (k+1)).', 'Matches "measures at every step" (L60).', ''),
    'isDiag_Phi': ('partial', 'phi a permutation of V x H, mu : H -> C, rho diagonal: Phi phi mu t rho = Tr_H[U^t (rho (x) diag mu) U^-t] is diagonal.',
        'Matches I-128 (tracing out a permutation unitary from a diagonal hidden state preserves diagonal states).',
        'I-129 ("for them (2) implies CP-indivisibility") is Main\'s written theorem; the kernel covers only its diagonal-preservation premise. The Introduction does not call I-129 machine-checked.'),
    'cmi_nonneg': ('pass', '0 <= cmi w a b c for a probability law w.',
        'Supports I-324 negatively: FiniteEntropy.lean\'s 21 theorems (sum_mul_log_le ... cmi_le_log_card) contain no vanishing criterion (I = 0 iff conditional independence), and a tree-wide grep finds none, so "not machine-checked" is accurate.', ''),
    'Realization': ('pass', 'structure: step : V x H ~ V x H, w : Hist x V x H -> R, nonnegative, total 1.',
        'Supports I-324: nothing ties w to a realization run from time 0, so the time-t identification is outside the kernel, as L80 states.', ''),
    'memory': ('pass', 'memory R := cmiBits R.w varHist varNow (varNext R) = I(X_<t; X_{t+1} | X_t) in bits.', 'Matches M_t (L72).', ''),
    'rootedMap_periodic': ('partial', 'PeriodicFamily (fun t => rootedMap R t): exists M > 0 with Gamma (t + M) = Gamma t for every t.',
        'Supports I-009/I-120 (finite recurrence: some multiple of the period is an identity return).',
        'I-088 ("a finite bijection has finite order L ... one fixed realization has an L-periodic multi-time law") is about the multi-time law; the kernel states periodicity of the rooted one-time maps, a consequence used by the readback theorems. The multi-time periodicity is elementary but not this declaration.'),
    'responseRealization': ('partial', 'Given row-stochastic Gamma : N -> Matrix V V R and M: a RootedRealization on ResponseHidden V M with step responseStep and prior responsePrior Gamma.',
        'A rooted-family analogue of the independent-prior realization.',
        'Does not cover I-071 (finite-horizon multi-time laws with a prior independent of x_0); R-08 correctly adds no "machine-checked".'),
    'FiniteOperationalTheory': ('pass', 'structure (OperationalAssembly:594): avail, availExt; avail_id; avail_coarse; availExt_coarse; availExt_bind; prepAvail with prepAvail_uniform and prepAvail_post; readout, readout_avail, readout_local; prepAvail_discard.',
        'Matches I-137 (L114) clause by clause; the readout\'s form is derived (readout_is_localLuders), not postulated.', 'Outcome-conditioned composition is at ancilla levels (availExt_bind), as L114 says.'),
    'RoutedReadback': ('partial', 'exists a != b, 0 < w <= s < t <= K, x: a hidden seed separating the roots at w; overlap 0 < Gamma_s(a,x), Gamma_s(b,x); different rootedPosteriors at (s, x); different pushforwards at t; rootedMap R t a != rootedMap R t b.',
        'A formalization of a routed form of (C4).', 'rootedPosterior divides the root-conditioned weight of the initial hidden seed (the frozen spelling), not Law(H_s | X_s = x, X_0 = a); PhysicalC4Discharge.lean:27-29 records the discrepancy (R-13).'),
    'qStar_not_subset_finiteRootedRealizable': ('pass', 'not (forall Gamma : N -> Matrix (Fin 2) (Fin 2) R, QStar Gamma -> FiniteRootedRealizable Gamma).',
        'Supports the all-time scope remark (a nonperiodic quantum rooted family has no exact all-time realization by one fixed finite system) on Fin 2.',
        'Census family kernel-only; R-05 does not cite it.'),
    'finiteRootedRealizable_iff_pper': ('pass', 'FiniteRootedRealizable Gamma <-> PPer Gamma, PPer = Gamma 0 = 1, every Gamma t row-stochastic, and PeriodicFamily Gamma.',
        'Matches R-09\'s evidence sentence (realizable at every time by one finite reversible system exactly when row-stochastic, identity at the root, and periodic).',
        'Rooted (one-time) families only, not multi-time laws; census family kernel-only (OD-4).'),
    'readWriteSourced_not_control': ('pass', 'T on Fin 2 with ReadWriteSourced T (every available composite conjugation is a permutation matrix) -> not HasCompositeUnitaryControl T.',
        'Supports R-06 "on the qubit (iv) fails" for read-write sourcing.', 'Qubit only; modelling premise: the sourced conjugations are permutation matrices.'),
    'readWriteSourced_not_qm': ('pass', 'T on Fin 2 with ReadWriteSourced T -> not ExactAllFiniteEndomorphicQuantumOps T.', 'Supports I-258/I-281 (matrix) on the qubit.', 'Qubit only; FINDINGS does not cite it.'),
    'substratum_residual': ('pass', 'Architecture, ContextStable, LabelInvariant, DaggerStable of substratumClass (IsMonomial), and not DrivesElementary, not QuantumArchitecture, and genTheory substratumClass (Fin 2) not exact QM.',
        'Matches R-06 "structurally closed but drives no elementary transition, and its generated qubit theory is not quantum".',
        'substratumClass contains swaps and quarter phases (both monomial), so the failure of DrivesElementary is the continuous transition flows. Modelling premise: the substratum\'s supplied operators are exactly the monomials (round-62 interface).'),
    'substratum_extension_quantum_iff_drives': ('pass', 'ExtendsSubstratum I -> StructurallyClosed I -> (QuantumArchitecture I <-> DrivesElementary I).', 'Supports I-258/I-281 (matrix) and R-06\'s endpoint.', ''),
    'substratum_plus_control_qm': ('pass', '[Nonempty A] (A : Type, finite): ExtendsSubstratum I -> StructurallyClosed I -> DrivesElementary I -> ExactAllFiniteEndomorphicQuantumOps (genTheory I hc.arch A).',
        'Matches R-06 "adding continuous control of the elementary transitions, with the closure properties kept, yields exact finite operational QM on every nonempty finite carrier".',
        'DrivesElementary (SubstratumSource:77) is the transition flows at every real t, the swaps and the quarter phases; the phases come with the substratum class it extends ("with a phase intervention assumed"). The hypothesis StructurallyClosed is load-bearing, hence "with the closure properties kept".'),
    'substratumClass_not_drivesElementary': ('pass', 'not DrivesElementary substratumClass.', 'Supports R-06 "no continuously tunable state mixing".', ''),
    'realizesSealedOICore_of_control': ('pass', 'T on Fin 2, HasCompositeUnitaryControl T -> RealizesSealedOICore T.',
        'Matches R-06 L120 "Conversely, every qubit theory satisfying (iv) realizes that process".', 'Qubit only, as the text says.'),
    'HasCompositeUnitaryControl': ('pass', 'forall n, U on A x Fin n with U^H U = 1: availExt n Unit (conjChannel U).', 'Matches condition (iv) (L114) and R-06\'s use of it.', ''),
    'permClass_onesFixing': ('pass', 'OnesFixing permClass: every admissible isometry in the contractively scaled partial permutations fixes the all-ones vector up to a scalar.',
        'With onesFixing_not_phasesAvailable, supports R-06 "the substratum as stated ... supplies no quarter phase".',
        'Modelling premise: "the stated dynamics and access" is the class permClass; that the bijective interventions, read-write operators and gate flows lie in it is shown by separate lemmas (bijectiveOperator_mulVec_ones, readWriteOperator_mulVec_ones, gateFlow_mulVec_ones), the identification itself is a modelling choice.'),
    'onesFixing_not_phasesAvailable': ('pass', 'Architecture I, OnesFixing I, 2 <= |A| -> not PhasesAvailable (genTheory I arch A).',
        'Supports "supplies no quarter phase" on every carrier with at least two states.', 'PhasesAvailable is the quarter phase at every level; the text says "quarter phase", which is the exact form.'),
    'substratumClass_not_onesFixing': ('pass', 'not OnesFixing substratumClass (the quarter phase is monomial, unitary and moves the all-ones ray).',
        'Supports R-06\'s "with a phase intervention assumed": it isolates the phase as the one stipulated intervention that is not ones-fixing.',
        'FINDINGS lists it under "No phases from the stated access"; it does not itself show absence of phases, it shows the phase is the stipulated ingredient.'),
    'monomialSource_not_control': ('pass', 'T on Fin 2, MonomialSource T -> not HasCompositeUnitaryControl T.', 'Matches R-06 "on the qubit a theory of such operations fails (iv)".', 'Qubit only.'),
    'frozen_sourcing_verdict': ('pass', 'not PhasesAvailable (permTheory (Fin 2)) and not DenseUnitaryControl (permTheory (Fin 2)) and not DerivedOI (permTheory (Fin 2)).',
        'Supports the matrix links of I-258/I-281.', 'Census family kernel-only; FINDINGS deliberately does not cite it (OD-2).'),
    'determinism_reversibility_selected_measure': ('pass', 'For phi a permutation of a nonempty finite S: invariant laws supported on an orbit are uniform on it; the uniform law is invariant and has maximal entropy among invariant laws; two disjoint invariant sets give two distinct invariant laws.',
        'Supports O-5\'s "(machine-checked)" after "maximal-entropy default" (L38).', 'Optional change; needs a retained axiom report before Appendix A cites it (OD-15).'),
    'continuous_extension_not_unique': ('pass', 'Exist Hermitian H0, H1 on Fin 2 with unitary flows, equal at every integer time and different at t = 1/2.', 'Supports O-14.', 'Optional change.'),
}


def main():
    a = sys.argv
    arg = lambda k: a[a.index(k) + 1]
    decls = json.load(open(arg('--decls')))['declarations']
    matrix = json.load(open(arg('--matrix')))
    reps = {JOB17: json.load(open(arg('--rep17'))), JOBEAE: json.load(open(arg('--repeae'))),
            JOB02E: json.load(open(arg('--rep02e')))}
    cross = json.load(open(arg('--cross')))

    claims = {}
    for r in matrix['rows']:
        for l in r['chain']:
            if l['layer'] != 'kernel' or not l['source'].startswith('lean:'):
                continue
            parts = l['source'].split(':', 3)
            short = parts[3].split()[0].split('.')[-1]
            claims.setdefault(short, set()).add(r['id'])

    def key(d):
        return d['name'].split('.')[-1]

    items = []

    def add(**kw):
        kw['item'] = 'E1-%02d' % (len(items) + 1)
        items.append({k: kw[k] for k in ('item', 'type', 'what', 'claims', 'sources', 'check',
                                         'outcome', 'evidence_level', 'limits', 'notes', 'not_covered') if k in kw})

    appA = [d for d in decls if d['cited_in'] == 'AppA']
    all_claims_appA = sorted({c for d in appA for c in claims.get(key(d), set())} | {'I-053', 'I-311'})

    add(type='ci-receipt',
        what='The retained expected result papers/introduction_repro/results-121598983127.json (blob 61cfd6ea, sha256 0f200310...) is a faithful extraction of job 121598983127 ("Mathlib bridge", run 40330683786, push on main at 17b830bc): build success, release gate PASS with 22/22 steps, lean-axioms "6082 named result(s) reported", 0 failure markers, 14 modules complete with 286 reports, and each of the 28 Appendix A declarations reported once with exactly [propext, Classical.choice, Quot.sound].',
        claims=all_claims_appA,
        sources=['papers/introduction_repro/results-121598983127.json@4a260ca9', 'papers/introduction_repro/README.md@4a260ca9',
                 'run %s / job %s' % (RUN17, JOB17)],
        check='GitHub API: actions/jobs/121598983127 (MCP get_workflow_job) -> head_sha 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86, conclusion success, steps Build and Release gate success. Downloaded the job log read-only (gh api repos/amaybaum/incompleteness/actions/jobs/121598983127/logs): 43064 lines, sha256 bc2291bc57d9..., equal to the README\'s full-log digest; its first 38918 lines joined by newline hash to 1a83921fb967..., equal to source.served_sha256. E1_logreports.py re-extracted every report from the Build step and E1_crosscheck.py compared all 286 retained reports (name, line, axioms) and every module\'s #print-axioms line numbers (read from source at eae01647) with this log: no difference. Countercontrols (an axiom dropped from one retained report; one print line shifted) were each caught on exactly that module.',
        outcome='pass', evidence_level='certificate-checked',
        limits='The reports are lake replays of an earlier elaboration restored from the Actions cache (exact key hit); lake --rehash re-hashes the checked-out sources against the restored traces, so they belong to byte-identical sources and the same toolchain, but no fresh elaboration was observed. Log text is diagnostic (§A.44); the structured signals are the job and step conclusions and the gate\'s exit status.',
        notes='Cross-check verdict: %s.' % json.dumps({k: cross[k] for k in ('modules', 'reports', 'failures', 'countercontrol_axiom_drop_caught', 'countercontrol_print_shift_caught', 'holds')}))

    for run, job, sha, label in ((RUNEAE, JOBEAE, 'eae01647f50d9e2aa90957fbd6c59d8cf44e7681', 'eae01647'),
                                 (RUN02E, JOB02E, '02e73e5611c6f89ddbedb3b49968529748a0b33a', '02e73e56')):
        rp = reps[job]
        add(type='ci-receipt',
            what='Main push CI at %s: run %s (verify, push, attempt 1, conclusion success); job %s "Mathlib bridge" conclusion success with steps Build and Release gate success; gate 22/22 PASS including lean-axioms "6082 named result(s) reported, no sorr[yAx]..."; Build step: "%s", %d axiom reports, markers %s.' % (
                label, run, job, rp['build_success_line'], rp['total_reports_in_build'], json.dumps(rp['markers_build'])),
            claims=['I-053', 'I-311'],
            sources=['run %s / job %s' % (run, job)],
            check='MCP get_workflow_run %s (head_sha %s, conclusion success) and list_workflow_jobs (job %s and its step conclusions). Job log downloaded read-only through the REST endpoint; E1_logreports.py read the Build step (to the first "Build completed successfully") and the gate lines. Same Lean toolchain line (Lean 4.33.0, commit d8b18978) and Mathlib revision db584cd6 as the retained run.' % (run, sha, job),
            outcome='pass', evidence_level='certificate-checked',
            limits='Replayed build (cache hit), as for the retained run. The "error:" token appears 12 times in the whole log, all in the later round-specific mutation steps (KTOKEN-MAXCONE-1, KTRANS-SEP-2), none in Build or Release gate.',
            notes='Lean sources at %s are byte-identical to 17b830bc (E1-04).' % label)

    add(type='lean-certificate',
        what='The Lean sources the Introduction cites are identical at 17b830bc, eae01647, 4a260ca9 and 02e73e56, and so are the gate tools that check them.',
        claims=['I-053'],
        sources=['verification/lean-mathlib@eae01647', 'tools/lean_axiom_check.py@02e73e56', 'tools/release_gate.py@02e73e56', '.github/workflows/verify.yml@02e73e56'],
        check='git rev-parse <c>:verification/lean-mathlib -> 8624ba39ada1... and <c>:verification/lean -> 277d2822cca0... at all four commits; git diff --stat 17b830bc eae01647, eae01647 02e73e56 and 17b830bc 4a260ca9 -- verification/lean verification/lean-mathlib are empty; tools/lean_axiom_check.py (8dec29c7), tools/release_gate.py (317135fc) and verify.yml (d5d3840a) have the same blobs at 17b830bc, eae01647 and 02e73e56. 17b830bc is an ancestor of eae01647, which is an ancestor of 02e73e56.',
        outcome='pass', evidence_level='certificate-checked',
        limits='Identity of sources and checker, not a rebuild.', notes='')

    fs = decls and json.load(open(arg('--decls')))['forbidden_scan']
    add(type='lean-certificate',
        what='No declaration in verification/lean-mathlib is an axiom, opaque or unsafe constant, and no source uses sorry, admit, native_decide, implemented_by, extern or debug.skipKernelTC; the gate\'s axiom allow-list is exactly {propext, Classical.choice, Quot.sound}.',
        claims=['I-053', 'I-311'],
        sources=['verification/lean-mathlib@eae01647 (%d .lean files)' % fs['files'], 'tools/lean_axiom_check.py:47@02e73e56'],
        check='E1_decls.py scanned every .lean file with comments stripped for the forbidden-construct patterns: %s. tools/lean_axiom_check.py line 47: PERMITTED = {\'propext\', \'Classical.choice\', \'Quot.sound\'}; it fails on sorryAx anywhere, on a nonzero lake exit, on any axiom outside PERMITTED (native_decide shows as Lean.ofReduceBool) and on a declared `#print axioms` with no report. The build logs of all three runs have 0 occurrences of sorryAx, Lean.ofReduceBool and "declaration uses \'sorry\'".' % json.dumps({k: len(v) for k, v in fs['hits'].items()}),
        outcome='pass', evidence_level='certificate-checked',
        limits='The scan is textual over OIBridge; Mathlib\'s own sources were not scanned (the printed reports cover what each printed declaration uses, Mathlib included). The SILENT check matches by short name; 33 short names are printed more than once in the tree, and of the declarations audited here only permMatrix_mem_unitaryGroup collides (its report is present in all three logs and in the retained result).',
        notes='Modelling premises are recorded per declaration below; none of the premise structures states its theorem\'s conclusion.')

    # per-declaration lean-certificate items
    for d in decls:
        k = key(d)
        cl = sorted(claims.get(k, set())) + FINDINGS.get(d['name'], FINDINGS.get(k, []))
        src = 'lean:%s:%d:%s' % (d['module'], d['found_line'], d['name'])
        prints = [p['line'] for p in d.get('print_axioms', [])]
        if not prints:
            continue
        r17 = next(x for x in reps[JOB17]['declarations'] if x['name'] == d['name'] and x['module'] == d['module'])
        reae = next(x for x in reps[JOBEAE]['declarations'] if x['name'] == d['name'] and x['module'] == d['module'])
        r02 = next(x for x in reps[JOB02E]['declarations'] if x['name'] == d['name'] and x['module'] == d['module'])
        ok = all(x['within_allow_list'] and x['report_lines_match_prints'] and len(x['reports']) == 1 and x['reports'][0]['axioms'] == ALLOW
                 for x in (r17, reae, r02))
        retained = d.get('retained_report') or []
        in_ret = bool(retained)
        res_line = ('retained result: report at %s:%d %s' % (d['module'], retained[0]['line'], retained[0]['axioms'])) if in_ret else 'not in the retained result (its module is %s)' % ('retained but this print is not among the 28 Appendix A declarations' if d.get('retained_module') else 'outside the 14 retained modules')
        add(type='lean-certificate',
            what='%s (%s, kind %s, declared at %s:%d) is kernel-checked and its `#print axioms` report is exactly [propext, Classical.choice, Quot.sound] at 17b830bc, eae01647 and 02e73e56.' % (d['name'], d['full_name'], d['kind'], d['module'], d['found_line']),
            claims=cl,
            sources=[src, 'print %s:%s' % (d['module'], ','.join(map(str, prints)))] + (['papers/introduction_repro/results-121598983127.json@4a260ca9'] if in_ret else []) + ['job %s' % JOB17, 'job %s' % JOBEAE, 'job %s' % JOB02E],
            check='Name: E1_decls.py found the declaration header at %s:%d (cited line %d%s) in the source at eae01647; sources identical at 17b830bc (E1-04). Axioms: %s; E1_logreports.py found exactly one report per job log at the print line, %s. Kernel checking: job conclusions success with Build and Release gate success at each commit (E1-01..E1-03); the gate\'s lean-axioms step, whose contract fails on any missing or non-allow-listed report, passed. Dependencies: no axiom/opaque/sorry/native_decide anywhere in OIBridge (E1-05); the report covers transitive Mathlib dependencies.' % (
                d['module'], d['found_line'], d['cited_line'], '' if d['resolves_at_cited_line'] else ', offset %+d' % d['offset'], res_line,
                '; '.join('%s: %s' % (j, x['reports'][0]['axioms'] if x['reports'] else 'none') for j, x in ((JOB17, r17), (JOBEAE, reae), (JOB02E, r02)))),
            outcome='pass' if ok and d['resolves_at_cited_line'] else 'partial',
            evidence_level='certificate-checked',
            limits=('Retained expected result plus CI logs.' if in_ret else 'No retained expected result covers this declaration: the per-declaration axiom content is read from CI job-log text (diagnostic under §A.44); the structured certificate is the Release gate step conclusion together with lean_axiom_check\'s contract. Appendix A would need the retained result extended (OD-15) before citing it.') + ' Replayed build (no fresh elaboration observed).',
            notes='')

    # cmi_nonneg: compiled, no report
    d = next(x for x in decls if x['name'] == 'cmi_nonneg')
    add(type='lean-certificate',
        what='cmi_nonneg (OIBridge.FiniteEntropy.cmi_nonneg, FiniteEntropy:372) is kernel-checked as part of the module build; it has no `#print axioms` line.',
        claims=sorted(claims.get('cmi_nonneg', set())),
        sources=['lean:FiniteEntropy:372:cmi_nonneg', 'job %s' % JOBEAE],
        check='Header found at the cited line. Its module compiles in the successful Build step at each commit, with 0 sorry markers; its proof is cmi3_nonneg applied to marg_nonneg and sum_marg, and cmi3_nonneg\'s report (FiniteEntropy:484) is within the allow-list.',
        outcome='partial', evidence_level='traced-only',
        limits='No axiom report exists for this declaration itself; its axiom set is inferred from the tree-wide scan (E1-05) and the report of cmi3_nonneg, not printed. It supports I-324 only negatively (what is not formalized).',
        notes='')

    defs = [x for x in decls if not x.get('print_axioms') and x['name'] != 'cmi_nonneg']
    add(type='lean-certificate',
        what='The definitions and structures the matrix and FINDINGS cite resolve and are accepted by the kernel: %s.' % ', '.join('%s (%s:%d)' % (x['name'], x['module'], x['found_line']) for x in defs),
        claims=sorted({c for x in defs for c in claims.get(key(x), set())} | {c for x in defs for c in FINDINGS.get(x['name'], [])}),
        sources=['lean:%s:%d:%s' % (x['module'], x['found_line'], x['name']) for x in defs] + ['job %s' % JOBEAE, 'job %s' % JOB02E],
        check='E1_decls.py resolved each header (the matrix\'s CausalReadback:52 for PDivisible is its docstring; the def is at :54; all others at the cited line). Each module compiled in the successful Build step at each commit. A `#print axioms` report is not meaningful for a definition\'s content, which is what these citations rely on; their content is checked in the formal-coverage items.',
        outcome='pass', evidence_level='certificate-checked',
        limits='Kernel acceptance only; no axiom reports.', notes='')

    # Listed claims a partial coverage reading does not cover (E4 then grades the row's link to it traced-only).
    NOT_COVERED = {
        'isDiag_Phi': {'I-129': 'the kernel covers only the diagonal-preservation premise of the written theorem'},
        'rootedMap_periodic': {'I-088': 'the kernel states periodicity of the rooted one-time maps, not of the multi-time law'},
        'responseRealization': {'I-071': 'a rooted-family analogue; not the finite-horizon multi-time law with a prior independent of x_0'},
    }
    # formal coverage items, one per declaration
    for d in decls:
        k = key(d)
        cov = COV.get(d['name']) or COV.get(k)
        if cov is None:
            raise SystemExit('no coverage reading for %s' % d['name'])
        outcome, stmt, match, lim = cov
        cl = sorted(claims.get(k, set())) + FINDINGS.get(d['name'], FINDINGS.get(k, []))
        add(type='formal-coverage',
            what='%s: %s' % (d['name'], stmt),
            claims=cl,
            sources=['lean:%s:%d:%s' % (d['module'], d['found_line'], d['name']), 'papers/Introduction.md@4a260ca9'],
            check='Read the statement and its premise structures from the source at eae01647 (E1_decls.py output, then the definitions it uses) and compared it, clause by clause, with the Introduction claims listed (matrix.json rows and FINDINGS texts). ' + match,
            outcome=outcome,
            evidence_level='certificate-checked',
            limits=lim or 'None beyond the per-declaration certificate.',
            notes='Census family status at eae01647 is recorded in part-E1.md.',
            **({'not_covered': NOT_COVERED[d['name']]} if d['name'] in NOT_COVERED else {}))

    add(type='open-obligation',
        what='All three runs examined replayed the OIBridge build from the Actions cache, so no fresh elaboration of the cited declarations was observed; no retained expected result covers the declarations outside Appendix A; and the repository\'s `reproduce evidence` workflow cannot reproduce either as it stands.',
        claims=['I-053', 'R-06', 'R-09', 'R-12', 'R-13', 'OD-15'],
        sources=['.github/workflows/reproduce-evidence.yml@48b18ac5', 'verification/audits/evidence-retention/reproduce.py@48b18ac5', 'papers/introduction_repro/README.md@4a260ca9'],
        check='Read the workflow and reproduce.py at 48b18ac5: workflow_dispatch only; the bridge job runs reproduce.py --run RUN_ID, which looks up the manifest entry ci-RUN_ID, checks out its commit, runs lake exe cache get / lake --rehash build / release_gate.py from an empty .lake/build, extracts with the named extractor blob and compares with compare_result.py. The manifest at 48b18ac5 has no entry ci-40330683786; the archive (and this workflow) left main at 5c4e5087, an ancestor of 02e73e56, so neither is on main. The Introduction\'s README gives the same recipe for manual use.',
        outcome='partial', evidence_level='traced-only',
        limits='See part-E1.md for the proposed owner-authorized CI reproduction.',
        notes='')
    json.dump(items, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == '__main__':
    main()
