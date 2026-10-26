#!/usr/bin/env python3
# Generates matrix/part-B4.json for claims I-246..I-312 (B4 mapping agent).
import json, sys
S = '/tmp/claude-0/-home-user-incompleteness/57e93868-2ccb-5ebd-afb7-d31826198729/scratchpad'
D = S + '/icaudit/verification/audits/manuscript/intro-corpus-audit-20261026'
claims = json.load(open(D + '/inventory/claims.json'))
byid = {}
for c in claims:
    byid[c['id']] = c
    if c.get('direction'):
        for sc in c['direction']['sub_claims']:
            byid[sc['id']] = dict(sc, _parent=c)

E = '@eae01647'
I = '@4a260ca9'

def L(link, source, layer, hyps, status):
    return {'link': link, 'source': source, 'layer': layer, 'hypotheses': hyps, 'link_status': status}

def C(site, text, nature):
    return {'site': site, 'text': text, 'nature': nature}

# ---- shared links ---------------------------------------------------------------------------
T1_K = L('Theorem 1, S_K = D_K = Q_K at every finite horizon for every finite visible alphabet; the three biconditionals assembled from S_imp_D, D_imp_Qfb, Qfb_imp_S with no construction as hypothesis',
         'lean:Equivalence.lean:462:finite_horizon_equivalence', 'kernel', ['finite visible alphabet V (Fintype)', 'finite horizon K'], 'proved')
S_IMP_D = L('S_K ⊆ D_K: every stochastic finite-horizon law is the visible marginal of a finite reversible system (clock-and-record carrier)',
            'lean:Equivalence.lean:422:S_imp_D', 'kernel', ['finite V', 'finite K'], 'proved')
D_IMP_Q = L('D_K ⊆ Q_K: permutation unitary read out in the configuration basis',
            'lean:Equivalence.lean:294:D_imp_Qfb', 'kernel', ['finite V', 'finite K'], 'proved')
Q_IMP_S = L('Q_K ⊆ S_K: fixed-basis Born records are probability laws (chain normalisation)',
            'lean:Equivalence.lean:245:Qfb_imp_S', 'kernel', ['finite V', 'finite K'], 'proved')
T2_K = L('Theorem 2 (a)-(c): pushforward identity, TV floor, M_t <= I(X_<t;H_t|X_t) <= log2|C_H|, for a joint law of history, present and hidden state',
         'lean:HiddenMemory.lean:185:unavoidable_hidden_predictive_memory', 'kernel', ['joint law of (history, present, hidden state) with next visible = f_x(h)'], 'proved')
T2_ID = L("Identification of a realization's time-t law with the kernel's joint law (stated in Main §1.5 as 'a step not formalized')",
          'papers/Main.md:99' + E, 'paper-derivation', [], 'proved')
COR = L('Corollary: M_t>0 exactly when every faithful realization carries readout-relevant hidden memory at t (forward: pushforward identity in each realization; converse: in one realization from S_imp_D); CMI vanishing criterion not formalized',
        'papers/Main.md:99' + E, 'paper-derivation', ['standard CMI vanishing criterion [CT06]'], 'proved')
T4_FWD = L('Theorem 4 (⇒): exact finite operational QM on a nonempty finite carrier implies (i)–(v)',
           'lean:PhysicalCharacterization.lean:301:physical_of_exactAll', 'kernel', ['nonempty finite carrier'], 'proved')
T4_IFF = L('Theorem 4 assembled: ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T',
           'lean:GeneralCarrier.lean:100:exactAll_iff_physical_general', 'kernel', ['nonempty finite carrier'], 'proved')
FIVE = L('Five-way minimality on the qubit: for each of (i)–(v) a theory on Fin 2 realizing the sealed OI core, satisfying the other four, failing that one',
         'lean:RankGapTheory.lean:702:five_way_minimality', 'kernel', ['qubit carrier Fin 2', 'sealed C1–C4 OI core'], 'proved')
OINQ = L('OI alone is not QM: the diagonal-preserving theory realizes the sealed OI core and is not exact QM',
         'lean:GeneralCarrier.lean:160:oi_alone_not_qm', 'kernel', ['qubit carrier'], 'proved')
GR33_IND = L("GR §3.3: 'Each of the five is independent of the other four and of the observation process itself ... bare finite OI ⇏ QM'",
             'papers/GR.md:220' + E, 'paper-derivation', [], 'proved')
GL2 = L('GL2: two coherent lifts of the same visible family related by a time-dependent strong gauge have different relative candidates (existential witness, one visible pair, one anchor, frozen readback)',
        'lean:CoherentLiftGauge.lean:537:gl2_strong_gauge_moves_relative_candidate', 'kernel', ['qubit visible carrier', 'frozen readback convention', 'anchor 0'], 'proved')
P0_RM = L("ROADMAP P0: 'What additional structure determines the relative quantum evolution OI leaves free' — OPEN (acts 11–17 localize it; no selection principle adopted)",
          'verification/ROADMAP.md:63' + E, 'none', [], 'open')
SUBST_RES = L("Stated substratum class (bijections with the phase intervention stated) is structurally closed but does not drive elementary transitions; its generated theory on Fin 2 is not exact QM",
              'lean:StructuralClosure.lean:383:substratum_residual', 'kernel', ['phase intervention assumed on the substratum class'], 'proved')
RW_NOT = L('Read-write sourced theories (finite bijective read-write dynamics with the stated observer access) are not exact QM (monomial operators only)',
           'lean:ReadWriteControl.lean:174:readWriteSourced_not_qm', 'kernel', ['qubit carrier'], 'proved')
FROZEN = L("Frozen-sourcing verdict: the bijection-level (permutation) theory sources no phases, no dense unitary control, not DerivedOI; ROADMAP records the resource as INDEPENDENT ('does not say an extended architecture cannot source it')",
           'lean:FrozenSourcing.lean:318:frozen_sourcing_verdict', 'kernel', ['two-valued carrier', 'NonnegBounded (bijection-level) architecture'], 'proved')
EXT_IFF = L('A structurally closed extension of the substratum class is a quantum architecture iff it drives the elementary transitions; with it, exact finite operational QM on every nonempty finite carrier (substratum_plus_control_qm)',
            'lean:StructuralClosure.lean:408:substratum_extension_quantum_iff_drives', 'kernel', ['ExtendsSubstratum', 'StructurallyClosed'], 'proved')
GR_SUBST = L("GR §3.3 substratum-source form: 'the concrete substratum supplies every structural requirement of quantum mechanics but not continuous state-mixing controllability, and quantum mechanics is obtained exactly when that one physical resource is added'; the phase intervention is an assumption on the class",
             'papers/GR.md:260' + E, 'paper-derivation', ['phase intervention assumed'], 'proved')
GR_LAYER = L("GR §3.3 layer-flow form: stated substratum dynamics with observer access ⇏ one nontrivial layer flow executable; fractional-time access is an additional physical intervention assumption",
             'papers/GR.md:266' + E, 'kernel', ['phase intervention stated'], 'proved')
RM_INDEP = L("ROADMAP 'Settled negatively — INDEPENDENT': 'FrozenSourcing proves that the present configuration-level architecture cannot source DenseUnitaryControl ... an independent empirical datum relative to the present architecture ... does not say an extended architecture cannot source it'",
             'verification/ROADMAP.md:1538' + E, 'none', [], 'proved')
RM_F2 = L("ROADMAP P1 F2: a named extension of OI that sources the nonclassical resource, proved sufficient — OPEN ('the present architecture is settled negatively')",
          'verification/ROADMAP.md:69' + E, 'none', [], 'open')
GR_G3 = L("GR dependency ladder: G3, covariant field equations with conservation/Bianchi structure and the continuum limit, open; G4 (cosmological constant, dark sector, Page curve, MOND) conditional on G3",
          'papers/GR.md:12' + E, 'paper-derivation', [], 'open')
RM_G3 = L("ROADMAP P2 'Covariant matter→boundary coupling (the G3 map)' — OPEN",
          'verification/ROADMAP.md:75' + E, 'none', [], 'open')
GR_DESC = L("GR §6.2: 'Descriptive distinction established; dynamical decoupling conditional on G3' — two gravitational completions differing by ρ_C g_μν share the same substratum and transition law",
            'papers/GR.md:356' + E, 'paper-derivation', ['G3 open'], 'conditional')
GR_A8 = L('GR Thm A.8 (cycle typicality) conditional on H-scramble, full product space as a single shell',
          'papers/GR.md:817' + E, 'paper-derivation', ['H-scramble', 'whole configuration space a single energy shell'], 'conditional')
GR_A9 = L('GR Thm A.9 (cycle-averaged Page curve) conditional on A.8, hence on H-scramble, and on H-decouple',
          'papers/GR.md:845' + E, 'paper-derivation', ['H-scramble', 'H-decouple'], 'conditional')
GR_HSCR = L("GR: H-scramble fails for every bijection in the setting of Thm A.7's proof (definite configuration, aligned bipartition); 'H-scramble is not established here'",
            'papers/GR.md:835' + E, 'paper-derivation', [], 'open')
GR_HDEC = L("GR A.7 setup: H-decouple 'Timescale ordering does not supply it, and H-decouple is not established here'",
            'papers/GR.md:809' + E, 'paper-derivation', [], 'open')
GR_SHELL = L("GR 'Proper energy shells': Thm A.8 on a proper shell and the Page curve of A.9 on such a shell are open",
             'papers/GR.md:843' + E, 'paper-derivation', [], 'open')
GR_TRAJ = L("GR: entropy along a single trajectory 'is a different quantity, and whether it follows the same curve is open'",
            'papers/GR.md:853' + E, 'paper-derivation', [], 'open')
BHB_C1 = L('BHb C1/C6(a): permutation orbit of a configuration is a product basis state at every aligned bipartition (proof + exhaustive sweeps 24/40320/362880 permutations)',
           'verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:18' + E, 'exhaustive-computation', ['aligned bipartition', 'definite initial configuration'], 'proved')
BHA_A = L('BHa claim A: 1376 of 40320 bijections of {0,1}^3 give zero accessible advantage; 60 non-injective maps of {0,1}^2 recover exactly (exhaustive)',
          'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:18' + E, 'exhaustive-computation', ['finite toy classes'], 'proved')
BHA_C = L('BHa C1/C2 [PROVED]: bijectivity + complete endpoint access gives exact recovery; P_succ >= 1/|K| (written proofs + exhaustive checks)',
          'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:20' + E, 'paper-derivation', ['bijective dynamics'], 'proved')
MAIN_45 = L("Main §4.5: 'no memory-witness outcome therefore falsifies the ontology at present' ... 'No ontology-level memory falsifier is established until the completed model supplies the constraint'",
            'papers/Main.md:702' + E, 'paper-derivation', [], 'open')
RM_EMP = L("ROADMAP P2 'Direct empirical access to the hidden sector — proposed routes to a discriminating test' — OPEN",
           'verification/ROADMAP.md:76' + E, 'none', [], 'open')
OI_POSIT = L('OI as a physical hypothesis (representation choice, empirically motivated); Main posit ledger',
             'papers/Main.md:708' + E, 'conjecture', ['OI physical hypothesis'], 'conditional')

rows = {}
def row(cid, chain, req, ps, src, verdict, contra=None, fix=None, notes='', cond=None):
    c = byid[cid]
    if '_parent' in c:
        p = c['_parent']
        base = {'id': cid, 'section': p['section'], 'line': p['line'], 'text': p['text'],
                'status_as_stated': {'level': c['status_as_stated'], 'hypotheses': [], 'note': 'sub-claim ' + c['label'] + ': ' + c['claim']}}
    else:
        base = {'id': cid, 'section': c['section'], 'line': c['line'], 'text': c['text'],
                'status_as_stated': c['status_as_stated']}
    r = dict(base)
    r['chain'] = chain
    r['required_assumptions'] = req
    r['proof_status'] = ps
    if cond:
        r['conditional_on'] = cond
    r['strongest_verified_source'] = src
    r['verdict'] = verdict
    r['contradictions'] = contra or []
    r['proposed_fix'] = fix
    r['notes'] = notes
    rows[cid] = r

# ======================= §6.1 =================================================================
row('I-246',
    [OI_POSIT, Q_IMP_S, S_IMP_D,
     L('All-time scope: Q* (fixed-basis quantum rooted families, all times) is NOT contained in the class realizable by one fixed finite reversible system (Hadamard witness is nonperiodic); C_OI ⊆ Q* holds',
       'lean:QuantumRepresentationT2.lean:163:qStar_not_subset_finiteRootedRealizable', 'kernel', ['qubit visible carrier', 'rooted families, all times'], 'proved'),
     L("Main Remark (consolidation): 'the universal all-time form is settled negative ... a nonperiodic target admits no exact all-time realization by one fixed finite substratum'",
       'papers/Main.md:618' + E, 'paper-derivation', [], 'proved')],
    ['OI physical hypothesis', 'finite horizon', 'finite-dimensional unitary system, fixed basis, diagonal initial state'],
    'conditional', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'IMPRECISE',
    [C('verification/lean-manuscript-census.json (family "quantum representation: the all-time translation layer")' + E,
       'T2 is REFUTED: the Hadamard datum ... is a member of Q* whose induced rooted family is ... nonperiodic, so Q* is not contained in the OI-realizable class',
       'kernel-only all-time result, carried by no manuscript; it falsifies an unscoped reading of the sentence (one fixed finite system cannot record a non-permutation fixed-basis family at all times)')],
    "If the hypothesis holds, the fixed-basis statistics of quantum theory are, at every finite horizon, visible laws of an embedded observer",
    "Conditional on OI (stated). The identification holds per finite horizon (Theorem 1, Q_K ⊆ D_K, kernel). Under OI the observer is part of ONE fixed finite reversible system, whose rooted family is periodic (kernel rootedMap_periodic); the kernel proves fixed-basis families with non-permutation unitaries are not all-time realizable by any such system (qStar_not_subset_finiteRootedRealizable). The Introduction scopes Theorem 1 per horizon in §2.3 and §6.4, but this §6.1 sentence drops the horizon qualifier. Low severity.",
    cond=['OI physical hypothesis'])

row('I-247',
    [OI_POSIT, T2_K, T2_ID, COR],
    ['OI physical hypothesis', 'faithful realization', 'CMI vanishing criterion (not formalized)', "time-t identification (not formalized)"],
    'conditional', 'lean:HiddenMemory.lean:185:unavoidable_hidden_predictive_memory', 'FAITHFUL', [],
    None,
    "A law departs from Markov behaviour iff M_t>0 for some t; Theorem 2(c) and the Corollary place that memory in the hidden state of every faithful realization. Kernel parts plus two paper steps (time-t identification, CMI vanishing criterion); the sentence carries no status word, which §6.1 does not require. Conditional on OI as stated.",
    cond=['OI physical hypothesis'])

row('I-248',
    [T4_IFF, FIVE, OINQ, GR33_IND],
    ['nonempty finite carrier', 'qubit witnesses for non-implication'],
    'proved-kernel', 'lean:GeneralCarrier.lean:100:exactAll_iff_physical_general', 'FAITHFUL', [],
    None,
    "Theorem 4 (kernel, both directions) plus five_way_minimality/oi_alone_not_qm (kernel). Completeness note shared with I-258: for the stated substratum the corpus settles (iv) negatively (GR §3.3 substratum-source form), which this sentence does not need to state.")

row('I-249',
    [L("Main §3.3 Theorem (Bell ceiling for a screened local completion): deterministic, local setting operations, setting-independent pre-setting ensemble ⇒ |S_CHSH| <= 2",
       'papers/Main.md:360' + E, 'paper-derivation', ['determinism', 'pointwise causal cone', 'setting-independent pre-setting ensemble'], 'proved'),
     L('Bell/CHSH inequality', '[Bel64; CHSH69]', 'literature', [], 'proved'),
     L("Main §3.3: with globally coupled setting-dependent hidden dynamics the response-table construction realizes PR-box behaviour — the selector is causal locality, not representability",
       'papers/Main.md:356' + E, 'paper-derivation', [], 'proved')],
    ['determinism', 'locality (pointwise causal cone)', 'measurement independence'],
    'proved-paper', 'papers/Main.md:360' + E, 'FAITHFUL', [],
    None,
    "'Memory alone' is read as hidden memory within a local, measurement-independent deterministic completion; Main §3.3 shows that without locality the finite construction even realizes PR boxes, so the qualifier matters and the sentence is accurate in context (§3.5 states the hypotheses).")

row('I-250',
    [L("Main §3.3 / abstract: 'Reproducing them requires ontic parameter dependence ... or else setting-dependent ontic ensembles' (Bell ceiling contrapositive)",
       'papers/Main.md:22' + E, 'paper-derivation', ['determinism', 'measurement independence'], 'proved'),
     L('Bell ceiling theorem', 'papers/Main.md:360' + E, 'paper-derivation', ['setting-independent ensemble'], 'proved')],
    ['deterministic completion', 'measurement independence'],
    'proved-paper', 'papers/Main.md:360' + E, 'FAITHFUL', [],
    None,
    'For deterministic models parameter independence plus measurement independence is Bell locality; violating CHSH with MI kept requires parameter dependence. The framework\'s adoption of the ontic option is a choice (Book ch01 §1.7, Main §3.3), stated as such in §3.5.')

row('I-251',
    [L("Substratum §3.3 H-Bell: preparation-indexed graphs must (i) supply the ontic parameter dependence, (ii) preserve operational no-signalling, (iii) satisfy a metric/Ollivier–Ricci stability condition for the continuum-curvature step",
       'papers/Substratum.md:132' + E, 'conjecture', ['H-Bell'], 'open'),
     L("ROADMAP P1 'H-Bell — composite and Bell closure' — OPEN; H-Bell is downstream of a harder obligation (the hop-metric curvature route fails for the reference graph before any Bell edge is added)",
       'verification/ROADMAP.md:67' + E, 'none', [], 'open')],
    ['H-Bell'],
    'open', 'verification/ROADMAP.md:67' + E, 'FAITHFUL',
    [C('verification/ROADMAP.md:963' + E, 'And H-Bell is downstream of a harder obligation ... the hop-metric curvature route fails for the reference family before any Bell edge is added',
       'partial negative result on the continuum-limit leg not mentioned in the Introduction (completeness, low)')],
    None,
    'Open status agrees with Substratum, Main abstract and ROADMAP.')

# ======================= §6.2 =================================================================
MAIN_TITLE = C('papers/Main.md:2' + E, '### The Equivalence of Quantum Mechanics and Embedded Observation',
               "[Main]'s title asserts an equivalence of QM and embedded observation; Main itself scopes it ('the exact equivalence claim is at the finite observable-law level', Main:20; the phrase is defined at Main:758 as 'exact bidirectional equivalence of finite observable stochastic laws and their quantum representations'), and GR §3.3 proves bare finite OI ⇏ QM. The Introduction cites the title verbatim (line 261). Owner decision.")
row('I-252',
    [T1_K, OINQ, FIVE, GR33_IND],
    ['finite carriers'],
    'proved-kernel', 'lean:GeneralCarrier.lean:160:oi_alone_not_qm', 'FAITHFUL',
    [MAIN_TITLE,
     C('papers/Methodology.md:585' + E + '; papers/Structure.md:1416' + E, '[Main] ... "The Incompleteness of Observation: The Equivalence of Quantum Mechanics and Embedded Observation"', 'same title carried in companion reference lists'),
     C('book/appendix-c-objections.md:315' + E, '"The framework identifies QM with embedded observation, dissolves the cosmological constant problem ..." (objection voice; the response at :317 does not dispute the identification and says "the derivations are explicit and the proofs are complete")', 'book appendix C response leaves the identification standing and asserts complete proofs')],
    None,
    "Faithful as a disclaimer: Theorem 1 is a representation result and OI alone does not imply QM (kernel). The [Main] title is recorded as an owner finding (see part-B4.md).")

row('I-253', [T1_K], ['finite visible alphabet', 'finite horizon'], 'proved-kernel', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'FAITHFUL', [], None,
    "S_K is by definition every law on C_V^{K+1}; Theorem 1 (kernel) makes D_K and Q_K equal to it.")

row('I-254',
    [L("Main §3.4 / Intro §2.3: the supplied unitaries are permutations with 0/1 entries, so |U|^p gives the same table for every p>0; p=|U|^2 is part of Q_K's definition",
       'papers/Main.md:20' + E, 'exact-algebra', [], 'proved'),
     L('Born exponent not selected by the representation', '[Bar26, Thm 3.1]', 'literature', [], 'proved')],
    [], 'proved-paper', 'papers/Main.md:20' + E, 'FAITHFUL', [], None,
    "Immediate algebra. The origin of the exponent is open (§3.5; Main 'named as a frontier item').")

row('I-255', [T4_IFF, FIVE], ['nonempty finite carrier'], 'proved-kernel', 'lean:RankGapTheory.lean:702:five_way_minimality', 'FAITHFUL', [], None,
    'No unique operational theory is selected: each completion condition can fail while the OI core and the other four hold (kernel).')

row('I-256', [FIVE, OINQ, GR33_IND], ['qubit witnesses'], 'proved-kernel', 'lean:RankGapTheory.lean:702:five_way_minimality', 'FAITHFUL', [], None,
    "five_way_minimality covers all five cells (validity, inert spectators, control, iterated closure, system-to-level-one = Intro's (i),(iii),(iv),(v),(ii)). A qubit counter-model suffices for non-implication.")

row('I-257', [FIVE], ['qubit carrier Fin 2', 'sealed OI core'], 'proved-kernel', 'lean:RankGapTheory.lean:702:five_way_minimality', 'FAITHFUL', [], None,
    'Statement checked: five existentials over FiniteOperationalTheory (Fin 2), each with RealizesSealedOICore and exactly one condition failing.')

STATED_SUBSTRATUM_CONTRA = [
    C('papers/GR.md:260' + E, "the concrete substratum supplies every structural requirement of quantum mechanics but not continuous state-mixing controllability, and quantum mechanics is obtained exactly when that one physical resource is added",
      'corpus settles (iv) negatively for the stated substratum; the Introduction states the whole question as open'),
    C('verification/ROADMAP.md:1529' + E, '| Dense/nonclassical operational control from the presently stated architecture | INDEPENDENT |', 'recorded as settled negatively, not open'),
    C('papers/GR.md:228' + E, "The substantive physical question it isolates is whether the OI substratum supplies (iii)–(v)", "GR's framing sentence at the characterization, which the Introduction cites; GR's own later paragraphs (:260, :266) narrow it"),
    C('papers/Main.md:758' + E, "It is the remaining operational-lifting problem, not a defect in the exact stochastic–quantum equivalence proved here",
      'Main §5 frames the coherent/compositional residual as an open lifting problem without the INDEPENDENT verdict for the present architecture (corpus finding)')]
row('I-258',
    [GR33_IND, SUBST_RES, RW_NOT, FROZEN, GR_SUBST, GR_LAYER, EXT_IFF, RM_INDEP, RM_F2],
    ['stated substratum = finite bijective dynamics with the stated observer access (phase intervention assumed where stated)', 'finite carriers'],
    'proved-kernel', 'lean:StructuralClosure.lean:383:substratum_residual', 'UNDERCLAIM',
    STATED_SUBSTRATUM_CONTRA,
    "which of (iii)–(v) a physical substratum supplies is open, except that the stated substratum, with the observer's stated access, does not supply the continuous state-mixing control that (iv) requires [GR §3.3]",
    "The corpus has a kernel-checked negative result for the presently stated architecture: bijection-level (monomial) operations source no phases and no dense unitary control (frozen_sourcing_verdict, readWriteSourced_not_qm, substratum_residual), recorded INDEPENDENT in ROADMAP; with one continuous off-diagonal controllability resource (and the assumed phase intervention) the extension is exact finite operational QM (substratum_extension_quantum_iff_drives, substratum_plus_control_qm). What remains open is whether a physical substratum supplies that resource (ROADMAP F2). Calling the whole question 'open' understates a settled negative (§A.30/code-review rule: state negatives for the class ruled out). The same wording appears in the abstract and §3.2 (other ranges).")

row('I-259', [GL2, P0_RM], ['coherent lifts on a fixed carrier and anchor'], 'proved-kernel', 'lean:CoherentLiftGauge.lean:537:gl2_strong_gauge_moves_relative_candidate', 'FAITHFUL', [], None,
    'An existential witness suffices for "does not fix". ROADMAP P0 records the selection question as open.')

row('I-260', [S_IMP_D, L("Main §1.5: 'S ⇔ D, Markov laws included, so the existence of a realization does not distinguish non-Markovian laws'", 'papers/Main.md:99' + E, 'paper-derivation', [], 'proved')],
    ['finite horizon'], 'proved-kernel', 'lean:Equivalence.lean:422:S_imp_D', 'FAITHFUL', [], None, 'Every law, Markov or not, has a realization (kernel).')

row('I-261',
    [L("Main Remark (scope: P-indivisibility is not quantum non-Markovianity): Hadamard then identity is CP-divisible while its populations ½J → I are P-indivisible",
       'papers/Main.md:330' + E, 'exact-algebra', [], 'proved'),
     L('Main Remark (three notions, kept apart)', 'papers/Main.md:334' + E, 'paper-derivation', [], 'proved')],
    [], 'proved-paper', 'papers/Main.md:330' + E, 'FAITHFUL', [], None, 'Explicit counterexample computed in the remark.')

row('I-262',
    [L('Intro B.2 / Main: X_2 = X_0 ⊕ X_1 has every two-time matrix ½J (P-divisible) and I(X_0;X_2|X_1) = 1 bit', 'papers/Introduction.md:232' + I, 'exact-algebra', [], 'proved'),
     L('Same process up to relabelling', '[RHP14, Eq. (15)]', 'literature', [], 'proved')],
    [], 'proved-paper', 'papers/Introduction.md:232' + I, 'FAITHFUL', [], None, 'Counterexample in the Introduction itself (exact).')

BH_DISS = [C('book/ch18-beyond.md:146' + E, "The second dissolution: the black hole information paradox ... The apparent information loss in Hawking radiation is an artifact of the trace-out",
             "book voice calls the information paradox 'dissolved' and asserts the trace-out reading; the same paragraph says the Page curve is conditional (tone tension, corpus finding)")]
row('I-263', [GR_A9, GR_HSCR, GR_HDEC, GR_SHELL, GR_TRAJ], ['H-scramble', 'H-decouple', 'G3'], 'open', 'papers/GR.md:609' + E, 'FAITHFUL', BH_DISS, None,
    'GR §8.4(iii) and App. A state every leg of the Page result as conditional or open.')

row('I-264', [GR_A8, GR_A9, GR_HSCR, GR_HDEC, GR_SHELL, GR_TRAJ, GR_G3], ['H-scramble', 'H-decouple', 'full-product-space shell', 'G3'], 'open', 'papers/GR.md:845' + E, 'FAITHFUL',
    [C('papers/GR.md:609' + E, '(iii) The Page curve ... the Page value is recovered, as a cycle average, ... conditional also on the decoupling condition H-decouple', 'consistent: conditional result whose hypotheses are not established')], None,
    'GR states Theorems A.8–A.9 as conditional on H-scramble (which fails in the framework\'s own configuration setting) and H-decouple (not established).')

row('I-265',
    [BHA_A, BHA_C, BHB_C1,
     L("BHa item F: 'GR A.7 decoupling statement at 30 M_sun is contradicted; t_evap/τ_B^D ∈ [1.785e57, 1.786e65]' — an audit observation on GR's own timescale formulas, not a toy-model result",
       'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:30' + E, 'numerical', [], 'proved'),
     L("BHb C6(b)–(d): textual analyses of GR Thms A.8–A.9 (where the Page value enters; shell factorization CONDITIONAL with certified bounds; time average vs instantaneous value OPEN)",
       'verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:20' + E, 'paper-derivation', [], 'proved')],
    ['finite toy classes'], 'proved-paper', 'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:18' + E, 'IMPRECISE',
    [C('verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:3' + E, 'Status: exploratory research, unreviewed for adoption.', "BHa's own status line; the Introduction's reference entry says 'internally reviewed' (outside this range; a review/REVIEW.md exists)")],
    "the results of §5 reported from [BHa; BHb] are finite toy-model computations, each proved on paper or checked exhaustively at small size or by exact arithmetic, and analyses of the hypotheses of [GR App. A]",
    "The toy-model results cited in §5 (claim A counts, C1, C2, BHb C1/C6(a), the diagonal-shell value) are exhaustive or proved. But §5 also cites BHa item F (timescale arithmetic on GR's formulas, 'audit observation') and BHb C6(b)–(d) (textual analyses of GR's theorems), which are not toy models. BHb also carries NUMERICAL (double-precision) items (C3) that §5 does not use. Low severity.")

row('I-266', [L("§5 makes no claim that information reaches D; BHa C3 shows a single B–D coupling defeats recovery even with all of W read", 'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:22' + E, 'exhaustive-computation', [], 'proved')],
    [], 'open', 'papers/Introduction.md:175' + I, 'FAITHFUL', [], None, 'Scope disclaimer. Whether information reaches D is not established anywhere in the corpus (proof_status records that open state, not a defect).')

row('I-267',
    [L("GR Theorem A.7 (Effective pure state): on t ≪ τ_B^D the joint state of V and B is effectively pure, O(t/τ_B^D)",
       'papers/GR.md:811' + E, 'paper-derivation', ['t ≪ τ_B^D', 'boundary-only dependence (A.5 step (i))'], 'proved'),
     L("GR A.7 setup: 'Theorem A.7 is stated for t ≪ τ_B^D'; evaporation is longer than τ_B^D for black holes above ~10^11 kg; A.7 does not establish B∪R purity (H-decouple)",
       'papers/GR.md:809' + E, 'paper-derivation', [], 'proved'),
     L("BHa item F contradicts the A.7 decoupling statement at 30 M_sun (outside A.7's stated scope)",
       'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:30' + E, 'numerical', [], 'proved')],
    ['t ≪ τ_B^D'], 'proved-paper', 'papers/GR.md:811' + E, 'FAITHFUL', [], None,
    "ATTENTION RESOLVED: GR Thm A.7 is the 'Effective pure state' theorem (decoupling of D on t ≪ τ_B^D), distinct from the Page results A.8–A.9. The disclaimer is correctly aimed: BHa item F shows timescale ordering fails at astrophysical evaporation times, which is outside A.7's stated scope, so no claim is made that A.7 fails within it. Optional clarity: name what A.7 states.")

row('I-268', [GR_HDEC], [], 'open', 'papers/Introduction.md:175' + I, 'FAITHFUL', [], None, 'Scope disclaimer.')

row('I-269', [OI_POSIT, MAIN_45, RM_EMP,
              L("Main §4.5 theorem-level falsifiability: the characterization theorem is mathematical; what is falsifiable is the physical identification", 'papers/Main.md:704' + E, 'paper-derivation', [], 'proved')],
    ['OI physical hypothesis'], 'open', 'papers/Main.md:704' + E, 'FAITHFUL',
    [C('book/appendix-a-prediction-status.md:28' + E, "S — Structural prediction ... S-class predictions provide the framework's strongest evidence", 'corpus reports empirical comparisons of the SM/GR sectors (OI plus a specific substratum and named hypotheses); the Introduction neither uses nor reports them'),
     C('book/appendix-c-objections.md:317' + E, 'the derivations are explicit and the proofs are complete; the predictions match empirical data at substantial precision', 'book voice stronger than the Introduction and than GR (G3 open)')],
    None,
    "Faithful as a statement of what the paper claims. OWNER DECISION: the corpus's Appendix A empirical comparisons test conjunctions of OI with a specific substratum and named hypotheses, not OI as stated in §1.1; whether the Introduction should say so (and the abstract's 'Open are ... any test of the hypothesis') is a scope choice.")

row('I-270', [L('Card game on card inputs is a classical stochastic process; Book: "a card mechanism is a local classical toy"', 'book/ch01-observation.md:286' + E, 'paper-derivation', [], 'proved')],
    [], 'proved-paper', 'book/ch01-observation.md:286' + E, 'FAITHFUL', [], None, 'Scope disclaimer backed by B.3 and Book §1.11.')

row('I-271', [L('Card game: φ(h,b)=(b,h), uniform independent burn card; trajectory law is a classical stochastic process (exact enumeration)', 'papers/Introduction.md:251' + I, 'exhaustive-computation', [], 'proved')],
    [], 'proved-paper', 'papers/Introduction.md:251' + I, 'FAITHFUL', [], None, 'Definitional for a classical card model.')

row('I-272', [L('Unitary embedding with uniform diagonal burn card: one-step channel ρ ↦ tr(ρ) I/2, constant hence entanglement-breaking', 'papers/Main.md:286' + E, 'exact-algebra', ['uniform diagonal hidden state'], 'proved'),
              L('Constant channel is measure-and-prepare', 'papers/Introduction.md:251' + I, 'exact-algebra', [], 'proved')],
    ['uniform diagonal burn card'], 'proved-paper', 'papers/Main.md:286' + E, 'FAITHFUL', [], None, "Main Remark (failure of (C1)) computes the same swap channel.")

row('I-273', [L('Instrument ρ ↦ ¼σ_oρσ_o sums to tr(ρ)I/2 by Σ_o σ_oXσ_o = 2tr(X)I; conditioned channels σ_o·σ_o compose to the identity (checked here: Σ_o σ_o(¼σ_oρσ_o)σ_o = ρ)', 'papers/Introduction.md:253' + I, 'exact-algebra', ['uniform burn card'], 'proved'),
              L('Classical-memory definition', '[BBS24, Def. 1]', 'literature', [], 'proved')],
    ['uniform burn card'], 'proved-paper', 'papers/Introduction.md:253' + I, 'FAITHFUL', [], None, 'Algebra re-checked in this mapping.')

row('I-274', [L("Book §1.11: 'no arrangement of cards on a table violates a Bell inequality'", 'book/ch01-observation.md:286' + E, 'paper-derivation', [], 'proved'),
              L('A local classical model is a local hidden-variable model', '[Bel64; CHSH69]', 'literature', [], 'proved')],
    [], 'proved-paper', 'book/ch01-observation.md:286' + E, 'FAITHFUL', [], None, 'Immediate: a local classical card model is LHV.')

CC_DISS = [C('papers/GR.md:326' + E, '## 6. Dissolution of the Cosmological Constant Problem', "GR section heading asserts a dissolution; GR's text (:356) says the decoupling is conditional on G3 (heading-level tension)"),
           C('book/ch07-gravity.md:163' + E, '## 7.7 Dissolution of the cosmological constant problem', 'book heading; body (:167) says "proposes a dissolution ... conditional"'),
           C('book/ch18-beyond.md:142' + E, '**The first dissolution: the cosmological constant.**', 'book voice; qualified as conditional in the same paragraph'),
           C('book/appendix-c-objections.md:317' + E, 'the derivations are explicit and the proofs are complete', 'overstates relative to GR G3 open (corpus finding)')]
row('I-275', [GR_G3,
              L("GR §7.4: the vacuum-energy normalization ρ_Λ ~ H²/G is the Friedmann scale 'whose value is an input'", 'papers/GR.md:551' + E, 'paper-derivation', [], 'proved')],
    [], 'proved-paper', 'papers/GR.md:551' + E, 'FAITHFUL',
    [C('papers/GR.md:545' + E, '| Dark sector fraction | Ω_dark ≈ 95% | Ω_CDM + Ω_Λ ≈ 95% | consistent |', 'GR lists a predicted combined dark fraction; not a prediction of Ω_Λ alone, so no contradiction, but the reader may see one')],
    None, 'No corpus document predicts Λ or Ω_Λ; GR treats the value as an input.')

row('I-276', [GR_G3, GR_DESC, RM_G3], ['G3 open'], 'open', 'papers/GR.md:356' + E, 'FAITHFUL', CC_DISS, None,
    "Faithful. The 'Dissolution' headings in GR §6 and Book §7.7 are qualified as conditional in their bodies; recorded as corpus tone findings.")

row('I-277', [GR_DESC, GR_G3],
    ['G3 covariant field equations'], 'conditional', 'papers/GR.md:356' + E, 'IMPRECISE', [],
    "§4's proposal is conditional on the covariant field equations",
    "GR: 'Descriptive distinction established; dynamical decoupling conditional on G3'. §4 itself says the descriptive distinction (shift invariance of visible transition probabilities) holds unconditionally; only the gravitational proposal is conditional. 'All of §4 is conditional' is a slight overstatement of the conditionality. Low severity.",
    cond=['covariant field equations (G3)'])

row('I-278', [L("Deterministic systems analysed with quantum methods precede OI", '[tH14]', 'literature', [], 'proved')], [], 'proved-paper', '[tH14]', 'FAITHFUL', [], None,
    "Scope disclaimer (literature-backed). The rendered-out reference comment records [tH14] as read first-hand (abstract, Ch. 2 §2.1) and SUPPORTED; not re-read here.")

row('I-279', [L("'t Hooft's cellular-automaton interpretation", '[tH14]', 'literature', [], 'proved')], [], 'proved-paper', '[tH14]', 'FAITHFUL', [], None,
    "Attribution only; first-hand read recorded in verification/audits/manuscript/introductory-paper-20261025 (per the reference comment), not repeated here.")

row('I-280', [L('Self-description of the paper\'s content', 'papers/Introduction.md:179' + I, 'none', [], 'unsupported')],
    [], 'unsupported', 'papers/Introduction.md:28' + I, 'IMPRECISE', [],
    "What the paper states are the cited results, with their scopes and status.",
    "The paper also states a physical hypothesis (OI), a proposal (§4), finite computations (§5), open problems (§6.3) and its own examples (Appendix B, uncited). 'cited theorems' is narrower than the content. Low severity; the sentence is also self-description that §A.32 discourages in paper prose.")

# ======================= §6.3 =================================================================
row('I-281', [GR33_IND, SUBST_RES, RW_NOT, FROZEN, GR_SUBST, GR_LAYER, EXT_IFF, RM_INDEP, RM_F2],
    ['stated substratum with stated observer access', 'finite carriers'],
    'open', 'lean:StructuralClosure.lean:383:substratum_residual', 'UNDERCLAIM', STATED_SUBSTRATUM_CONTRA,
    "whether a physical substratum supplies the phase intervention and the continuous state-mixing control that the stated substratum lacks, with which exact finite operational quantum mechanics follows [GR §3.3]",
    "The decisive test survives, but the corpus has narrowed it: for the presently stated architecture (iv) is settled negatively (kernel; ROADMAP INDEPENDENT), and sufficiency of the one added resource is kernel-proved (substratum_plus_control_qm; layer-flow form derivedOI_qm_iff_layerFlowExecutable'). The open question is ROADMAP F2. The open item stays open; the wording omits the established negative and positive halves. Medium severity.",
    cond=None)

row('I-282',
    [L("GR §2.2 (C4): 'the present paper does not independently demonstrate that a visible-history record written into hidden boundary degrees is routed back ... within the accessible window'", 'papers/GR.md:52' + E, 'paper-derivation', [], 'open'),
     L("ROADMAP P1 'Physical C4 discharge at the cosmological and lattice cuts' — OPEN, residual exact per cut (RoutedReadback; LatticeCutReadback)", 'verification/ROADMAP.md:66' + E, 'kernel', [], 'open')],
    [], 'open', 'verification/ROADMAP.md:66' + E, 'FAITHFUL',
    [C('verification/ROADMAP.md:66' + E, 'Physical C4 discharge at the cosmological and lattice cuts ... OPEN', 'the lattice cut is also open; the Introduction names only the cosmological partition (completeness, low)')],
    None, 'Agrees with GR §2.2 and ROADMAP.')

row('I-283', [MAIN_45, RM_EMP,
              L("Appendix A F7 'Born rule transient violations (conditional prospect: ... form not derived)'", 'book/appendix-a-prediction-status.md:180' + E, 'conjecture', [], 'open')],
    [], 'open', 'papers/Main.md:702' + E, 'FAITHFUL', [], None,
    "No corpus item supplies an established discriminating experiment; F7 is explicitly a conditional prospect with no derived form.")

row('I-284', [MAIN_45], [], 'open', 'papers/Main.md:702' + E, 'FAITHFUL', [], None, "Main §4.5: 'none is established here'.")

row('I-285', [GR_G3, RM_G3], ['G3'], 'open', 'papers/GR.md:12' + E, 'FAITHFUL', CC_DISS[:2], None, 'Matches GR Level G3 and ROADMAP P2.')

row('I-286', [GR_HSCR, GR_HDEC, BHB_C1], ['H-scramble', 'H-decouple'], 'open', 'papers/GR.md:835' + E, 'FAITHFUL', [], None,
    "Open, with a partial negative already stated in §5: H-scramble fails in the definite-configuration aligned setting; GR: 'it requires an initial superposition of configurations or a bipartition not aligned with them, and which of these the substratum supplies is open'.")

row('I-287', [GR_SHELL, GR_TRAJ,
              L('BHb C6(c) CONDITIONAL / C6(d) OPEN proof obligation', 'verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:21' + E, 'paper-derivation', [], 'open')],
    [], 'open', 'papers/GR.md:843' + E, 'FAITHFUL', [], None, 'Both legs open in GR App. A.')

row('I-288', [GR_G3], ['G3'], 'open', 'papers/GR.md:12' + E, 'FAITHFUL', [], None, "GR ladder: 'G4, the cosmological implications (..., Page curve, ...), conditional on G3'.")

row('I-289',
    [L('Theorem 1 prior-independent realization proved on paper (Main finite-horizon process dilation)', 'papers/Main.md:496' + E, 'paper-derivation', ['rational probabilities'], 'proved'),
     T2_ID, COR,
     L('Pinsker readback bound proved on paper', 'papers/Main.md:167' + E, 'paper-derivation', [], 'proved'),
     L('History-level (C4) ⇒ indivisibility proved on paper; routed form kernel', 'lean:PhysicalC4Discharge.lean:122:routed_forces_indivisible_somewhere', 'kernel', ['routed readback'], 'proved'),
     L('Kernel search: no declaration for the CMI vanishing criterion, Pinsker bound, prior-independent dilation or history-level (C4) indivisibility in OIBridge at eae01647', 'verification/lean-mathlib/OIBridge/' + E, 'none', [], 'open')],
    [], 'open', 'papers/Main.md:99' + E, 'IMPRECISE', [],
    "(1) machine checks of the steps proved only on paper (in §2.2, §2.4, §2.5, §3.1 and §3.4)",
    "Every listed step is indeed unchecked (grep of OIBridge found no formalization). The list omits other paper-only steps the Introduction states: §3.1's Hadamard counterexample and §3.4's factorization half. Conversely §2.3's periodicity has a rooted kernel form (rootedMap_periodic, RootedClassification:135) the Introduction does not cite. Low severity.")

MDET = L("Main Remark (a variational identity, open — and false in its naive form): at fixed hidden dimension (2,3) the minimum equals M_t for 1 of 15 processes (memory_probes.py); the canonical predictive quotient is constructed; 'leaving open only the variational VALUE question'",
         'papers/Main.md:594' + E, 'numerical', [], 'open')
row('I-290', [MDET,
              L('Canonical predictive quotient theorem (existence, universality, canonical quotient), certified exhaustively', 'papers/Main.md:600' + E, 'paper-derivation', [], 'proved')],
    [], 'open', 'papers/Main.md:594' + E, 'FAITHFUL', [], None,
    "Open item matches Main. Completeness (low): the quotient itself is a proved result (Main:600) that the Introduction does not state.")

row('I-291', [MDET,
              L('memory_probes.py: exhaustive over the 720 permutations of C_V×C_H at (2,3), UNIFORM prior only, entropies in floating point; groups processes by their t=2 conditional signature',
                'papers/oi_lattice_code/foundations/memory_probes.py:94' + E, 'numerical', ['uniform prior', '(n_V,n_H)=(2,3)', 'predict X3 from (X0,X1,X2)'], 'proved'),
              L('Countercontrol run in this mapping (scratchpad b4probe/fixeddim.py): minimizing I(hist;H_2|X_2) over ALL priors reproducing each law (convex in the within-class split, Nelder–Mead with restarts), at (2,3): the minimum attains M_t for 2 of 16 processes (grouped by full law); residuals 1/3 and 2/3 bit otherwise',
                'b4probe/fixeddim.py (scratchpad, not in corpus)', 'numerical', ['arbitrary prior on C_V×C_H'], 'proved')],
    ['(n_V,|C_H|)=(2,3)'], 'numerical', 'papers/oi_lattice_code/foundations/memory_probes.py:94' + E, 'FAITHFUL',
    [C('papers/Main.md:594' + E, 'The reading in which the infimum ranges over realizations of FIXED hidden dimension is FALSE: at (n_V,|C_H|)=(2,3) the minimum equals M_t for only one of fifteen distinct processes', "Main's probe restricts the infimum to the uniform prior, narrower than 'realizations of fixed hidden dimension'; the countercontrol shows the falsity survives arbitrary priors (residuals ≥ 1/3 bit), so the conclusion stands but Main's evidence sentence overstates the probe's scope (corpus finding, low)")],
    None,
    "A counterexample with a ≥1/3-bit gap is robust to floating point. The probe searched uniform priors only; this mapping's countercontrol over arbitrary priors confirms falsity (14 of 16 processes fail). Status: numerical evidence, not an exact certificate; no kernel declaration.")

GLUE = L("Main Remark (consolidation): open questions (a) exact gluing for recurrent target families and (b) approximation on windows t ≪ t_R", 'papers/Main.md:618' + E, 'paper-derivation', [], 'open')
ROOTED = L("Kernel (kernel-only, no manuscript): a complete rooted family over a finite visible carrier is realizable by one finite reversible system with one shared prior, at every time, iff it is the identity at the root, row-stochastic and periodic (C_OI(V) = P_per(V)); sufficiency constructive",
           'lean:RootedClassificationAllTime.lean:192:finiteRootedRealizable_iff_pper', 'kernel', ['finite visible carrier', 'rooted families (not full multi-time laws)'], 'proved')
row('I-292', [GLUE, ROOTED,
              L("ROADMAP 'Deliberately not prioritized': recurrent-family gluing and pre-recurrence-window approximation remain open in Main.md", 'verification/ROADMAP.md:1569' + E, 'none', [], 'open')],
    ['multi-time trajectory laws'], 'open', 'papers/Main.md:618' + E, 'UNDERCLAIM',
    [C('verification/lean-manuscript-census.json (family "rooted classification")' + E, 'status kernel-only, manuscript []', 'an established kernel answer at the rooted-family level that no manuscript, including Main and ROADMAP:1569, carries')],
    "(3) exact gluing for recurrent families of multi-time laws (for rooted families, periodicity is necessary and sufficient for exact all-time realization, machine-checked as finiteRootedRealizable_iff_pper)",
    "At the level of rooted families (the Γ_t of §2.5) the exact all-time realization question is settled positively for every periodic family (kernel, constructive). Whether that settles Main's question (a) depends on whether Main means rooted families or full multi-time laws; the full-law version remains open. The Introduction (and Main, ROADMAP) list the item as open without the rooted-level result. OWNER DECISION on scope. Medium-low severity.")

row('I-293', [GLUE,
              L("ROADMAP 'Deliberately not prioritized': pre-recurrence-window approximation open", 'verification/ROADMAP.md:1569' + E, 'none', [], 'open')],
    [], 'open', 'papers/Main.md:618' + E, 'FAITHFUL', [], None, 'Main (b) and ROADMAP agree.')

C2THM = L("Main Theorem (C2 necessity, quantitative mixing form): under the mixing hypothesis ||T^(k) − T^k|| <= (k−1)ε, constant optimal; and Theorem (physical memory: C2, process form): observed I* > 0 forces ε >= ε_min(I*, n_V) — 'This is (C2)'s necessity in the currency of condition (ii)'",
          'papers/Main.md:433' + E, 'paper-derivation', ['hidden-sector mixing hypothesis (TV within ε of π_H)'], 'conditional')
C2LED = L("Main status ledger: 'C2 necessity | Conditional on the hidden-sector mixing hypothesis; the quantitative bound ε >= δ/(k−1) is proved, its constant saturated (c2_mixing_probes.py); ETH is physical motivation, not a premise'",
          'papers/Main.md:720' + E, 'paper-derivation', ['mixing hypothesis'], 'conditional')
row('I-294', [C2THM, C2LED,
              L("ROADMAP 'Declared inputs and conditional hypotheses': hidden-sector/effective mixing hypotheses are declared inputs, 'not currently targeted'", 'verification/ROADMAP.md:1591' + E, 'none', [], 'conditional')],
    ['hidden-sector mixing hypothesis'], 'conditional', 'papers/Main.md:447' + E, 'IMPRECISE',
    [C('papers/GR.md:565' + E, "(C2) lies outside the equivalence, its necessity for physical hidden sectors conditional on the hidden sector's mixing hypothesis", 'GR and Main classify it conditional (proved under the hypothesis), not open')],
    "(4) whether the hidden-sector mixing hypothesis, motivated by eigenstate thermalization, holds, on which the proved necessity of (C2) is conditional [Main §3.4]",
    "Main proves (C2) necessity on paper under the mixing hypothesis (two theorems, probe-certified); its ledger says 'Conditional', not open. Listing '(C2) necessity' under open problems mislabels a proved conditional theorem as open; the open item is the hypothesis (a declared input in ROADMAP). Low severity.",
    cond=['hidden-sector mixing hypothesis'])

row('I-295', [C2THM, C2LED,
              L("Main: 'under the ETH assumption ... dephasing'; ledger: 'ETH is physical motivation, not a premise'", 'papers/Main.md:425' + E, 'paper-derivation', [], 'proved')],
    ['hidden-sector mixing hypothesis'], 'conditional', 'papers/Main.md:720' + E, 'FAITHFUL', [], None,
    "'conditional on a mixing hypothesis motivated by eigenstate thermalization' matches Main's ledger wording exactly.",
    cond=['hidden-sector mixing hypothesis'])

# ======================= §6.4 =================================================================
row('I-296', [T1_K, S_IMP_D, D_IMP_Q, Q_IMP_S], ['finite visible alphabet', 'finite horizon', 'some finite hidden sector and initial law (D_K quantifies over them)'],
    'proved-kernel', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'FAITHFUL', [], None,
    "D_K = S_K (kernel). 'an embedded observer of a finite reversible system' must be read as 'of some finite reversible system' (D_K is a union over systems); a single fixed system records only its own (periodic) laws, which §2.3 states. Acceptable at the conclusion's level of detail.")
row('I-296.a', [D_IMP_Q, Q_IMP_S], ['finite V', 'finite K'], 'proved-kernel', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'FAITHFUL', [], None,
    'D_K ⊆ S_K: composition Qfb_imp_S ∘ D_imp_Qfb inside finite_horizon_equivalence (also immediate: a visible marginal is a probability law).')
row('I-296.b', [S_IMP_D], ['finite V', 'finite K'], 'proved-kernel', 'lean:Equivalence.lean:422:S_imp_D', 'FAITHFUL', [], None, 'S_K ⊆ D_K: S_imp_D.')
row('I-297', [T1_K, D_IMP_Q, Q_IMP_S, S_IMP_D], ['finite visible alphabet', 'finite horizon', 'fixed basis, diagonal initial state'],
    'proved-kernel', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'FAITHFUL', [], None, 'D_K = Q_K (kernel).')
row('I-297.a', [D_IMP_Q], ['finite V', 'finite K'], 'proved-kernel', 'lean:Equivalence.lean:294:D_imp_Qfb', 'FAITHFUL', [], None, 'D_imp_Qfb.')
row('I-297.b', [Q_IMP_S, S_IMP_D], ['finite V', 'finite K'], 'proved-kernel', 'lean:Equivalence.lean:462:finite_horizon_equivalence', 'FAITHFUL', [], None, 'Q_K ⊆ D_K: S_imp_D ∘ Qfb_imp_S (composition in finite_horizon_equivalence).')

row('I-298', [T1_K,
              L("Main Remark (what this equivalence does and does not say): 'Markov and memory-bearing laws alike lie in Q_fb, so representability alone is not the framework's discriminating content'", 'papers/Main.md:534' + E, 'paper-derivation', [], 'proved'),
              T2_K],
    [], 'proved-paper', 'papers/Main.md:534' + E, 'FAITHFUL', [], None, 'Interpretive summary matching Main.')

row('I-299', [T2_K, T2_ID, COR,
              L("Main abstract: 'When (C4) holds, every faithful deterministic completion contains readout-relevant hidden predictive memory'", 'papers/Main.md:20' + E, 'paper-derivation', ['(C4)'], 'proved')],
    ['faithful realization', 'M_t>0 for the memory to be readout-relevant', 'CMI vanishing criterion (not formalized)', 'time-t identification (not formalized)'],
    'proved-paper', 'lean:HiddenMemory.lean:185:unavoidable_hidden_predictive_memory', 'IMPRECISE',
    [C('papers/Introduction.md:12' + I, 'every deterministic completion carries the visible memory in its hidden state', 'abstract restatement (I-008), same wording'),
     C('papers/Main.md:752' + E, 'C4 forces conditional memory, readout-relevant hidden predictive structure in every faithful completion', 'Main conditions on (C4) and uses "faithful"')],
    "which every faithful realization carries in its hidden state",
    "ATTENTION RESOLVED: 'deterministic completion' is undefined in the Introduction; Main uses 'faithful deterministic completion', which is the Introduction's 'faithful realization' (§1.2 Conventions; Main §1.5). The content is Theorem 2(c) (M_t <= I(X_<t;H_t|X_t), unconditional) and the Corollary (readout-relevant hidden memory exactly when M_t>0). Since the antecedent is 'memory' (a law with M_t>0), no M_t>0 qualifier is missing; the fix is terminological. The step not machine-checked is stated in the abstract and §2.4, not here. Low severity.")

row('I-300', [T4_FWD,
              L("ROADMAP P1 H-∞: 'no theorem upgrades the full finite OI→QM characterization to arbitrary infinite-dimensional or QFT systems' — OPEN", 'verification/ROADMAP.md:71' + E, 'none', [], 'open')],
    ['nonempty finite carrier'], 'proved-kernel', 'lean:PhysicalCharacterization.lean:301:physical_of_exactAll', 'IMPRECISE', [],
    "Exact finite operational quantum mechanics is reached only under completion conditions",
    "The necessity direction is kernel-proved for nonempty finite carriers only; the abstract says 'Exact finite operational quantum mechanics'. Dropping 'finite' in the conclusion extends the claim beyond the proved scope (H-∞ open). Low severity.")

row('I-301', [FIVE, OINQ, GR33_IND], ['qubit witnesses'], 'proved-kernel', 'lean:GeneralCarrier.lean:160:oi_alone_not_qm', 'FAITHFUL',
    [STATED_SUBSTRATUM_CONTRA[0]], None,
    'Kernel. Completeness: the stronger result that the stated substratum does not supply (iv) (see I-258) would sharpen this sentence.')

row('I-302', [GL2, P0_RM], [], 'proved-kernel', 'lean:CoherentLiftGauge.lean:537:gl2_strong_gauge_moves_relative_candidate', 'FAITHFUL', [], None,
    'Kernel witness; the selection question is ROADMAP P0 (open). §6.3 does not list P0 among open problems although the abstract does (completeness, low).')

row('I-303', [GR_DESC, L("Book §7.7: 'The framework proposes a dissolution ... the dissolution is conditional on it'", 'book/ch07-gravity.md:167' + E, 'conjecture', ['G3'], 'conditional')],
    ['G3'], 'conjecture', 'papers/GR.md:356' + E, 'FAITHFUL', CC_DISS, None, "Stated as a proposal; matches GR and Book bodies.")

row('I-304', [GR_G3, RM_G3], ['G3'], 'conditional', 'papers/GR.md:12' + E, 'FAITHFUL', CC_DISS[:1], None, 'G3 open in GR and ROADMAP.', cond=['covariant field equations (G3)'])

row('I-305', [BHA_A, BHA_C], ['finite toy classes', 'bijective dynamics'], 'numerical', 'verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:18' + E, 'FAITHFUL', [], None,
    'Non-implication in both directions shown by exhaustive counterexamples in finite toy classes; the sufficient conditions C1/C2 are proved. "separates" is a non-implication claim, which counterexamples establish generally.')

row('I-306', [GR_A9, GR_HSCR, GR_HDEC, GR_SHELL, GR_TRAJ, GR_G3], ['H-scramble', 'H-decouple', 'G3'], 'open', 'papers/GR.md:609' + E, 'FAITHFUL', BH_DISS, None, 'Same as I-264.')

row('I-307', [GR_DESC, GR_A9, GR_G3], ['G3', 'H-scramble', 'H-decouple'], 'open', 'papers/GR.md:12' + E, 'FAITHFUL', CC_DISS + BH_DISS, None,
    "Faithful. Corpus tone findings: 'Dissolution' headings (GR §6, Book §7.7, ch18) and appendix C's 'the proofs are complete'.")

# ======================= Code section =========================================================
REPRO = 'papers/introduction_repro/README.md' + I
row('I-308',
    [L("verification/lean-mathlib/lean-toolchain at 17b830bc = 'leanprover/lean4:v4.33.0'", 'verification/lean-mathlib/lean-toolchain:1@17b830bc', 'none', [], 'proved'),
     L("lakefile.toml at 17b830bc requires mathlib rev = \"v4.33.0\" (a tag); no lake-manifest.json is committed", 'verification/lean-mathlib/lakefile.toml@17b830bc', 'none', [], 'proved'),
     L("Retained expected result: job 121598983127 printed Lean (version 4.33.0, commit d8b18978…) and resolved mathlib to db584cd6…; dependency SHAs recorded", REPRO, 'none', [], 'proved')],
    [], 'proved-kernel', REPRO, 'FAITHFUL', [], None,
    "ATTENTION RESOLVED: toolchain confirmed from the repository (lean-toolchain, lakefile) and from the retained job record. Reproducibility notes: (1) Mathlib is pinned by a tag, not a manifest, so transitive dependencies are resolved at build time (the README records what the job resolved); (2) the attested job restored .lake/build from cache and 'Replayed' all 226 OIBridge modules — the reports are those of an earlier elaboration of the same sources, hash-checked by --rehash (disclosed in the README); the recipe from an empty .lake re-elaborates. Neither makes the sentence false.")

row('I-309', [L('git diff --stat 17b830bc b64919cd -- verification/lean verification/lean-mathlib is empty (also empty to eae01647)', 'git@17b830bc..b64919cd', 'exhaustive-computation', [], 'proved')],
    [], 'proved-kernel', 'git diff 17b830bc b64919cd', 'FAITHFUL', [], None, 'Checked in this mapping; identical also at eae01647.')

row('I-310', [L("release_gate.py step 'lean-axioms' runs tools/lean_axiom_check.py --require-lake; PERMITTED = {'propext','Classical.choice','Quot.sound'}; hard fail on sorryAx and on any #print axioms with no report", 'tools/lean_axiom_check.py:47@17b830bc', 'none', [], 'proved')],
    [], 'proved-kernel', 'tools/lean_axiom_check.py:47@17b830bc', 'FAITHFUL', [], None, 'Unchanged to eae01647.')

row('I-311', [L("Retained expected result (derived from job log 121598983127): each of the 28 Appendix A declarations has exactly one report, each [propext, Classical.choice, Quot.sound]; checked here declaration by declaration, and each declaration's module:line matches its `theorem` line in the source", 'papers/introduction_repro/results-121598983127.json' + I, 'kernel', ['cached replay of an earlier elaboration of identical sources'], 'proved')],
    [], 'proved-kernel', 'papers/introduction_repro/results-121598983127.json' + I, 'FAITHFUL', [], None,
    "ATTENTION RESOLVED: all 28 declarations report exactly the three axioms (none uses fewer). In the 14 modules one uncited lemma, PhysicalCharacterization.levelOne_eq, depends on propext alone; it is not in Appendix A. 'compositions :466–468' are the proof term of finite_horizon_equivalence, not declarations. NOTE: the file exists at #918's head 4a260ca9, not at main eae01647 or b64919cd (the brief's 'at eae01647' is inaccurate). This verifies the retained record, not an independent rebuild.")

row('I-312', [L("papers/introduction_repro/ holds README.md (recipe, provenance, checks) and results-121598983127.json (oi-evidence-result v1, kind bridge, derived)", REPRO, 'none', [], 'proved'),
              L('Recipe tools at 48b18ac5 exist on main (extract_result.py blob e6f69713 matches the recorded blob)', 'verification/audits/evidence-retention/extract_result.py@48b18ac5', 'none', [], 'proved')],
    [], 'proved-kernel', REPRO, 'FAITHFUL', [], None,
    "Present on the Introduction's own commit. Reproducibility notes: the recipe needs network access and a clone whose working tree contains papers/introduction_repro (i.e. #918 or its landing), since the compare step reads it by relative path; this is implicit. No reproduction was run here (no Lean builds).")

order = []
for c in claims:
    n = int(c['id'][2:5])
    if 246 <= n <= 312:
        order.append(c['id'])
        if c.get('direction'):
            order += [sc['id'] for sc in c['direction']['sub_claims']]
missing = [i for i in order if i not in rows]
extra = [i for i in rows if i not in order]
if missing or extra:
    print('MISSING', missing, 'EXTRA', extra); sys.exit(1)
out = [rows[i] for i in order]
json.dump(out, open(D + '/matrix/part-B4.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), Counter(r['verdict'] for r in out))
