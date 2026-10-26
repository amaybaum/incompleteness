#!/usr/bin/env python3
"""Build matrix/part-B1.json (claims I-001..I-091) for the intro-corpus audit."""
import json, sys

A = sys.argv[1]  # audit dir
claims = json.load(open(A + "/inventory/claims.json"))
byid = {}
for e in claims:
    byid[e["id"]] = e
    if e.get("direction"):
        for s in e["direction"]["sub_claims"]:
            byid[s["id"]] = dict(s, _parent=e)

C = "eae01647"
def M(l): return f"papers/Main.md:{l}@{C}"
def GR(l): return f"papers/GR.md:{l}@{C}"
def BK(f, l): return f"book/{f}:{l}@{C}"
def LN(mod, line, decl): return f"lean:OIBridge/{mod}.lean:{line}:{decl}"
def lk(link, source, layer, hyps, status):
    return {"link": link, "source": source, "layer": layer, "hypotheses": hyps, "link_status": status}

EQ_HYP = ["finite visible alphabet V (Fintype, DecidableEq; no |V|>=2 needed)", "finite horizon K"]
K_S_D = lk("S_imp_D: every Stochastic P on Traj V K is RevRealizable (bijection of V x Hid, Hid = clock x trajectory record, initial law on V x Hid that may correlate)", LN("Equivalence", 422, "OIBridge.Equivalence.S_imp_D"), "kernel", EQ_HYP, "proved")
K_D_Q = lk("D_imp_Qfb: every RevRealizable P is QfbRealizable (U = permMatrix of step^-1, init = joint initial law, read = Prod.fst)", LN("Equivalence", 294, "OIBridge.Equivalence.D_imp_Qfb"), "kernel", EQ_HYP, "proved")
K_Q_S = lk("Qfb_imp_S: every QfbRealizable P is Stochastic (chain normalisation from unitarity via sum_chain)", LN("Equivalence", 245, "OIBridge.Equivalence.Qfb_imp_S"), "kernel", EQ_HYP, "proved")
K_FHE = lk("finite_horizon_equivalence: (Stochastic<->RevRealizable) and (RevRealizable<->QfbRealizable) and (QfbRealizable<->Stochastic), each reverse arrow a composition (lines 466-468); no construction taken as hypothesis", LN("Equivalence", 462, "OIBridge.Equivalence.finite_horizon_equivalence"), "kernel", EQ_HYP, "proved")
P_FHE = lk("Main's theorem statement: (S), (D), (Q_fb) coincide for a finite visible alphabet and horizon K; proof (S=>D response table / kernel clock-record carrier, D=>Q_fb permutation unitary, Q_fb=>S Born rule)", M("526-532"), "paper-derivation", EQ_HYP, "proved")

K_HM = lk("unavoidable_hidden_predictive_memory: for a Realization (bijection step : V x H ~ V x H, joint law w on Hist x V x H) (a) nextLaw = pushforward of posterior, (b) TV floor, (c) M_t <= I(X_<t;H_t|X_t) <= log2|H|", LN("HiddenMemory", 185, "OIBridge.HiddenMemory.unavoidable_hidden_predictive_memory"), "kernel", ["joint law of (history, present, hidden) taken as given", "Nonempty H"], "proved")
P_HM_ID = lk("Identification of a realization's time-t law with the kernel's joint law, stated as 'a step not formalized'", M(97), "paper-derivation", ["faithful realization"], "proved")
P_COR = lk("M_t>0 iff every faithful realization carries readout-relevant hidden memory at t: forward by (a) in each realization, converse by (a) in one realization (exists by S_imp_D); uses the CMI vanishing criterion (not formalized)", M(97), "paper-derivation", ["faithful realization", "CMI vanishing criterion [CT06]"], "proved")

rows = []
def row(id_, chain, req, ps, src, verdict, contra=None, fix=None, notes="", cond=None):
    e = byid[id_]
    if "_parent" in e:
        p = e["_parent"]
        r = {"id": id_, "section": p["section"], "line": p["line"], "text": p["text"],
             "sub_claim": {"label": e["label"], "claim": e["claim"]},
             "status_as_stated": e["status_as_stated"]}
    else:
        r = {"id": id_, "section": e["section"], "line": e["line"], "text": e["text"],
             "status_as_stated": e["status_as_stated"]}
        if "line_end" in e: r["line_end"] = e["line_end"]
    r.update({"chain": chain, "required_assumptions": req, "proof_status": ps})
    if cond: r["conditional_on"] = cond
    r.update({"strongest_verified_source": src, "verdict": verdict,
              "contradictions": contra or [], "proposed_fix": fix, "notes": notes})
    rows.append(r)

# ---------------- Abstract ----------------
row("I-001", [
    lk("Observation = triple (S, phi, V), observer a proper subsystem with finitely many states", M(44), "paper-derivation", ["Axiom 1 (perspectival reading)"], "proved"),
    lk("Bijective substratum is a representation choice; total finiteness a physical posit; near-unitarity the motivating input", M(62), "conjecture", ["posit ledger (ii)-(iii)"], "conditional"),
    lk("Physical identification of nature with the finite deterministic ontology is what is empirically at stake, not a theorem", M(704), "conjecture", [], "open")],
    ["total finiteness of S (posit)", "bijective representative (representation choice)", "observer registers only C_V"],
    "conjecture", M(62), "FAITHFUL",
    notes="Definition of the hypothesis; presented as a hypothesis, which matches Main's status Remark (representation choice + posit). No proof obligation.")

row("I-002", [K_FHE, P_FHE], EQ_HYP + ["D_K initial law may correlate visible and hidden coordinates", "Q_K: projective measurement of the whole system in one fixed basis at every step, diagonal initial state, record a fixed function of the outcome"],
    "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL",
    contra=[{"site": M(16), "text": "S <=> D <=> Q_fb at the finite observable-law level", "nature": "same claim, consistent"},
            {"site": "papers/Main.md:2@eae01647 (title)", "text": "The Equivalence of Quantum Mechanics and Embedded Observation", "nature": "Main's subtitle reads as an equivalence with QM entire; the Intro (I-012, I-145) and Main:624 limit it to fixed-basis finite-horizon laws. Owner item, already raised by the claim inventory."}],
    notes="Abstract compresses Q_K to 'fixed-basis Born records of finite unitary systems'; the body (line 44) gives the full definition, which matches QfbReal (measurement in a basis of the whole finite space, read : Bas -> V). Each inclusion traced separately in I-002.a-c.")
row("I-002.a", [K_S_D], EQ_HYP, "proved-kernel", LN("Equivalence", 422, "S_imp_D"), "FAITHFUL",
    notes="Direction S_K subset D_K. Kernel D-class allows a correlated initial law; the independent-prior form is separate (I-071).")
row("I-002.b", [K_D_Q, lk("permMatrix_mem_unitaryGroup", LN("EquivalenceChain", 179, "OIBridge.EquivalenceChain.permMatrix_mem_unitaryGroup"), "kernel", [], "proved")], EQ_HYP, "proved-kernel", LN("Equivalence", 294, "D_imp_Qfb"), "FAITHFUL",
    notes="Direction D_K subset Q_K. The Qfb record measures the full visible x hidden configuration basis and reads the visible factor; this is what Q_K's 'record a fixed function of each outcome' means.")
row("I-002.c", [K_Q_S], EQ_HYP, "proved-kernel", LN("Equivalence", 245, "Qfb_imp_S"), "FAITHFUL",
    notes="Direction Q_K subset S_K. The kernel encodes the every-step projective record by its Born chain formula (QfbReal.chain); that encoding is the standard sequential-measurement formula [SGD19, Eq. (3)], read first-hand.")

row("I-003", [
    lk("EGGH26 Prop. 13: any stochastic process family with finite T is realized by a deterministic system-ancilla dynamics A: T x C x Lambda -> C with a correlated initial family; sketch: 'A large enough ancilla can label a complete system trajectory'", "EGGH26 (arXiv:2602.23491v1), Prop. 13, p. 30", "literature", [], "proved"),
    lk("Barandes: a permutation matrix is unitary and |Sigma_ij|^2 = Sigma_ij, so a permutation process is a special case of a unistochastic process", "Bar25 (arXiv:2302.10778v3), p. 12; Bar23 (arXiv:2309.03085v2) §4.3; Bar26 (arXiv:2608.04354v1) §4", "literature", [], "proved")],
    [], "proved-paper", "EGGH26 Prop. 13; Bar25 p. 12", "FAITHFUL",
    notes="Literature read first-hand from the scratch copies S/lit/egri2602, barandes2302, barandes2309, barandes2608. EGGH26's map is time-indexed and not required to be a bijection; the packaging as one iterated bijection is stated in §2.2 (I-074).")

row("I-004", [K_FHE, lk("S_K is all laws on C_V^{K+1} (Stochastic), so it contains every Markov law; equality carries it to D_K and Q_K", LN("Equivalence", 147, "OIBridge.Equivalence.Stochastic"), "kernel", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL")
row("I-005", [K_FHE, lk("Remark: Markov and memory-bearing laws alike lie in Q_fb, so representability alone is not the discriminating content; the bare form 'non-Markovianity <=> a realization exists' is false", M("534; 596-598"), "paper-derivation", [], "proved")],
    EQ_HYP, "proved-kernel", M(534), "FAITHFUL", notes="Immediate from universality of Theorem 1.")
row("I-006", [lk("Q_fb's Born weights are |U|^2 by definition (QfbReal.born); the supplied unitaries are permutations with 0/1 entries, so every exponent p>0 gives the same table (check 6, equivalence_recovery_probes.py)", M(534), "exact-algebra", [], "proved"),
              lk("QfbReal.born := ||U b' b||^2", LN("Equivalence", 205, "OIBridge.Equivalence.QfbReal.born"), "kernel", [], "proved")],
    [], "proved-paper", M(534), "FAITHFUL", notes="'Not selected' is a statement about the correspondence's construction; its truth is elementary (entries 0/1).")
row("I-007", [lk("'The discriminating content is history readback'", M(16), "paper-derivation", [], "proved"),
              lk("Theorem (unavoidable hidden predictive memory) is universal over realizations, the equivalence existential", M(592), "paper-derivation", [], "proved")],
    [], "proved-paper", M(592), "FAITHFUL", notes="Scope statement; matches Main's abstract and §3.4 Remark.")

row("I-008", [K_HM, P_HM_ID, P_COR],
    ["faithful (deterministic) realization", "identification of the time-t law with the kernel's joint law (not formalized)"],
    "proved-paper", LN("HiddenMemory", 185, "unavoidable_hidden_predictive_memory"), "FAITHFUL",
    contra=[{"site": M(16), "text": "When (C4) holds, every faithful deterministic completion contains readout-relevant hidden predictive memory", "nature": "Main states the readout-relevant form under (C4); the Intro states the capacity-floor form, which holds for every faithful completion and is vacuous when M_t = 0. Consistent."}],
    notes="Attention resolved: 'deterministic completion' is Main's 'faithful deterministic completion' = faithful realization (Main:582 'ANY faithful deterministic realization'). Read as Theorem 2(c), M_t <= I(X_<t;H_t|X_t), the claim holds for every faithful completion with no condition on M_t (it is vacuous at M_t=0); the readout-relevant form is the Corollary, which is the M_t>0 case. Kernel proves (a)-(c) for a joint law; the time-t identification is the unchecked step. The kernel's Realization is a bijection, but only determinism is used.")
row("I-009", [
    lk("Theorem (history readback + finite recurrence implies indivisibility): finite order L gives Gamma_L = I; if every Gamma_k were a permutation, histories with a common endpoint would identify x_0 and could not differ, contradicting C4; the stochastic-inverse lemma then forbids a divisor from Gamma_k to I", M("137-139"), "paper-derivation", ["fixed finite bijection", "history-level (C4)"], "proved"),
    lk("routed_forces_indivisible_somewhere: RoutedReadback K R -> exists n, PIndivisibleWithin n (rootedMap R)", LN("PhysicalC4Discharge", 122, "OIBridge.PhysicalC4Discharge.routed_forces_indivisible_somewhere"), "kernel", ["RoutedReadback (strictly stronger than history-level C4, per the module header)"], "proved"),
    lk("isPermMatrix_of_stochastic_inverse", LN("EquivalenceChain", 110, "OIBridge.EquivalenceChain.isPermMatrix_of_stochastic_inverse"), "kernel", [], "proved"),
    lk("rootedMap_periodic (finite order)", LN("RootedClassification", 135, "OIBridge.RootedClassification.rootedMap_periodic"), "kernel", [], "proved")],
    ["fixed finite reversible substratum", "history-level (C4) (paper) / routed-readback form (kernel)"],
    "proved-paper", M(139), "FAITHFUL",
    notes="Paper proof checked and sound. The kernel proves the conclusion from the routed-readback form, which implies history-level C4 but not conversely; the history-level step (C4 => some rooted map is non-permutation) is on paper. 'Somewhere in the recurrence cycle' matches the kernel's existential n.")
row("I-010", [
    lk("Theorem 2: (a)-(c) kernel for a joint law; time-t identification not machine-checked (one step)", M(97), "paper-derivation", [], "proved"),
    lk("Corollary (readout-relevant form): uses the time-t identification and the CMI vanishing criterion, neither machine-checked (two steps)", M(580), "paper-derivation", [], "proved"),
    lk("Readback: machine-checked from routed readback; from history-level C4 the step 'C4 => non-permutation rooted map' is on paper (one step)", M(139), "paper-derivation", [], "proved")],
    [], "proved-paper", M(580), "IMPRECISE",
    fix="(each machine-checked except for steps proved on paper)",
    notes="Attention resolved. 'One step' is accurate for Theorem 2(c) (time-t identification) and for readback (the history-level C4 step). If I-008 is read as the Corollary's readout-relevant form, two ingredients are unchecked (line 82 names both). The wording should not count steps.")

row("I-011", [lk("Theorem (operational-completion characterization): for every nonempty finite visible system, available families on the system and every positive ancilla level are exactly the normalized finite Kraus instruments iff (i)-(v)", GR(218), "paper-derivation", ["operational-theory standing structure (GR:216)"], "proved"),
              lk("exactAll_iff_physical_general := <physical_of_exactAll, exactAll_of_physical_general>", LN("GeneralCarrier", 100, "OIBridge.exactAll_iff_physical_general"), "kernel", ["FiniteOperationalTheory A, A finite nonempty"], "proved")],
    ["nonempty finite system", "operational theory with the standing structure: identity, coarse-graining, outcome-conditioned composition, uniformly mixed ancilla preparation, spectator-independent readout, ancilla discard"],
    "proved-kernel", LN("GeneralCarrier", 100, "exactAll_iff_physical_general"), "FAITHFUL",
    notes="'Characterized' is relative to the operational-theory structure, which the body states (line 114). GR gives no paper proof; the kernel is the proof (inventory: kernel-only).")
row("I-011.a", [lk("physical_of_exactAll: ExactAll -> PhysicalCompletionConditions", LN("PhysicalCharacterization", 301, "OIBridge.physical_of_exactAll"), "kernel", ["FiniteOperationalTheory A"], "proved")],
    ["operational-theory standing structure"], "proved-kernel", LN("PhysicalCharacterization", 301, "physical_of_exactAll"), "FAITHFUL", notes="Direction: exact finite OQM => (i)-(v).")
row("I-011.b", [lk("exactAll_of_physical_general: PhysicalCompletionConditions -> ExactAll (via krausSoundExt_of_validity_inert, compositeCompleteness_unconditional, exactAll_of_levelOne; isometry extension discharged by finiteIsometryExtensionSF_discharged)", LN("GeneralCarrier", 93, "OIBridge.exactAll_of_physical_general"), "kernel", ["FiniteOperationalTheory A, Nonempty A"], "proved")],
    ["operational-theory standing structure", "A nonempty"], "proved-kernel", LN("GeneralCarrier", 93, "exactAll_of_physical_general"), "FAITHFUL", notes="Direction: (i)-(v) => exact finite OQM. No external premise (GR:218).")
row("I-012", [lk("five_way_minimality: for each of the five conditions a qubit theory realizing the sealed OI core satisfies the other four and fails it", LN("RankGapTheory", 702, "OIBridge.five_way_minimality"), "kernel", ["carrier Fin 2", "OI formalized as RealizesSealedOICore"], "proved"),
              lk("oi_alone_not_qm", LN("GeneralCarrier", 160, "OIBridge.oi_alone_not_qm"), "kernel", [], "proved"),
              lk("'bare finite OI does not imply QM'; every theory with full reversible control realizes the sealed core", GR("220-228"), "paper-derivation", [], "proved")],
    ["OI read as realizing the sealed finite C1-C4 core on the qubit"], "proved-kernel", LN("RankGapTheory", 702, "five_way_minimality"), "FAITHFUL",
    notes="Non-implication needs one countermodel per condition; the qubit countermodels suffice. 'OI alone' is formalized as RealizesSealedOICore, a specific finite C1-C4 process with its visible readout.")
row("I-013", [lk("'The substantive physical question it isolates is whether the OI substratum supplies (iii)-(v)'", GR(228), "paper-derivation", [], "open")],
    [], "open", GR(228), "FAITHFUL")
row("I-014", [lk("'selection of a unique relating evolution from the coherent lifts of one visible family is open'", M(624), "paper-derivation", [], "open")],
    [], "open", M(624), "FAITHFUL")
row("I-015", [lk("No memory-witness outcome falsifies the ontology at present; no ontology-level falsifier is established", M("702-704"), "paper-derivation", [], "open"),
              lk("Framework-level falsification conditions are listed for applications (F1 BEC analogue gravity, F6 DESI Y5 running vacuum)", BK("appendix-a-prediction-status.md", "179; 203; 219"), "paper-derivation", ["G3 and application hypotheses"], "conditional")],
    [], "open", M(704), "IMPRECISE",
    contra=[{"site": BK("appendix-a-prediction-status.md", 219), "text": "BEC analogue-gravity test (F1) and DESI Year 5 running vacuum test (F6) provide the framework's most consequential near-term empirical exposure", "nature": "the corpus lists falsifiers for the framework's applications (OI jointly with application hypotheses); the abstract's 'any test of the hypothesis' reads more broadly than Main §4.5 and the Intro's own §1.1 and §6.3"},
            {"site": M(706), "text": "Laboratory tests of the characterization theorem may be possible in tabletop systems", "nature": "Main gestures at tests while :704 says no experiment falsifies the theorem; corpus-side tension, not the Intro's"}],
    fix="and any experiment that distinguishes OI from standard quantum theory",
    notes="The body states the narrower, sourced claim twice (line 22: no test at the level of memory witnesses; §6.3: no experiment distinguishing OI from standard QT). The abstract's 'any test of the hypothesis' is broader than either and sits beside application falsifiers the corpus does list. Low severity.")
row("I-016", [lk("Descriptive-level distinction: classical substratum (Friedmann value, no zero-point energy) vs emergent QFT (zero-point sum); 'the descriptive-level distinction is established'", GR("336-340; 356"), "paper-derivation", ["framework architecture: substratum vs emergent description"], "proved")],
    ["substratum/emergent architecture"], "proved-paper", GR(356), "FAITHFUL",
    notes="GR calls the descriptive distinction established and the dissolution conditional; the Intro's sentence is the descriptive part and is followed by the conditional status (I-017, I-018).")
row("I-017", [lk("G3 (covariant field equations, conservation/Bianchi, continuum limit) open; the distinct-descriptions argument becomes a theorem only under E_mu_nu[g,OI] = 8 pi G (T - F g)", GR(12), "paper-derivation", [], "open"),
              lk("'the dynamical dissolution is conditional on the G3 coupling theorem'", GR(28), "paper-derivation", [], "open")],
    [], "open", GR(356), "FAITHFUL")
row("I-018", [lk("'the descriptive-level distinction is established and the dissolution is conditional'", GR(356), "paper-derivation", ["G3 coupling step"], "conditional")],
    ["G3 covariant field equations"], "conjecture", GR(356), "FAITHFUL",
    contra=[{"site": GR(326), "text": "## 6. Dissolution of the Cosmological Constant Problem", "nature": "GR's section heading is unqualified; GR's own text (:28, :32, :356) says the dissolution is conditional. Corpus-side heading, consistent in substance with the Intro"}])
row("I-019", [lk("BH-01 claim A: 1376 of 40320 bijections of {0,1}^3 give zero accessible advantage; 60 non-injective maps recover exactly; C1 [PROVED]: bijectivity + complete endpoint access gives exact recovery", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:15-30@eae01647", "exhaustive-computation", ["finite toy classes", "stated access classes"], "proved"),
              lk("Independent review: computations reproduce exactly; written proofs of Lemma 0, C1, C2, C3 (sufficiency), Lemma L, D1 correct", "verification/programmes/black-hole-information/bh01_access_v1/review/REVIEW.md:1-5@eae01647", "exhaustive-computation", [], "proved")],
    ["finite toy models of configurations, permutations and configuration reads"], "numerical", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md@eae01647", "FAITHFUL",
    notes="'Finite computations' is accurate (exhaustive enumerations with written proofs of the sufficiency statements). The abstract omits 'toy models'; the body (line 154) states it.")
row("I-020", [lk("Page curve conditional on H-scramble and H-decouple, with the shell taken as the full product space", GR("603; 715"), "paper-derivation", ["H-scramble", "H-decouple"], "conditional"),
              lk("BH-02 C6(a): H-scramble fails for every bijection in the configuration setting; C6(d) open", "verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:22-26@eae01647", "paper-derivation", [], "proved")],
    [], "open", GR(603), "FAITHFUL")
row("I-021", [lk("Book and GR present the Page curve as conditional; no claim of resolution", BK("appendix-a-prediction-status.md", 102), "paper-derivation", [], "open")],
    [], "open", GR(603), "FAITHFUL",
    contra=[{"site": BK("ch07-gravity.md", 116), "text": "The framework provides an alternative derivation through a substantially different mechanism, conditional on the scrambling condition", "nature": "conditional derivation claim, consistent with 'not resolved'"}])

# ---------------- §1.1 ----------------
row("I-022", [lk("Definition: observation (S, phi, V), V a proper subsystem with finitely many states; product decomposition by Lemma 2; finiteness and bijectivity enter via Lemma 1, Lemma 3 and the status Remark", M("44; 50; 56; 62"), "paper-derivation", [], "proved")],
    [], "proved-paper", M(44), "FAITHFUL",
    notes="Main's Definition does not itself make S finite or phi bijective; the Intro adds both and immediately labels them posits/representation choices (I-023, I-024), as Main:62 does.")
row("I-023", [lk("'The bijective substratum is a representation choice — the minimal recurrent bijective representative of the hidden dynamics; ... observed near-unitarity is the empirical input motivating the choice'", M(62), "conjecture", [], "conditional")],
    ["representation choice"], "conjecture", M(62), "FAITHFUL",
    contra=[{"site": "papers/Methodology.md:235@eae01647", "text": "the rungs relationality, proper-part, dynamics-existence, determinism, finiteness-per-moment, and bijectivity follow as lemmas", "nature": "Methodology states bijectivity as a lemma; Main:62 and the posit ledger (Main:708 iii) make it a part-empirical representation choice (signal S10). Corpus-side; the Intro follows Main"},
            {"site": "papers/Methodology.md:253@eae01647", "text": "Everything else in the foundational layer is a lemma: ... and bijectivity", "nature": "same as above"}])
row("I-024", [lk("'total finiteness of that representative is a physical posit, carried in the posit ledger (§4.5)'", M(62), "conjecture", [], "conditional"),
              lk("Posit ledger (ii): finiteness of the total state space S", M(708), "conjecture", [], "conditional")],
    ["total-finiteness posit"], "conjecture", M(708), "FAITHFUL",
    contra=[{"site": M(46), "text": "What distinguishes the present setting is not the existence of such a map but that it acts on a *finite* $S$ (Lemma 1)", "nature": "Main:46 attributes finiteness of S to Lemma 1, which proves only finite C_V; Main:62 and :113 say total finiteness is a posit. Main-internal inconsistency; the Intro follows the posit reading"}])
row("I-025", [lk("'different hidden states h_k compatible with the same x send it to different futures'", M(105), "paper-derivation", [], "proved"),
              lk("Counter-case: if f_x is constant on the support of the hidden posterior, the visible step from x is deterministic (e.g. a permutation one-step matrix, Main:115-129)", M(119), "exact-algebra", [], "proved")],
    [], "proved-paper", M(105), "IMPRECISE",
    contra=[{"site": M(105), "text": "different hidden states $h_k$ compatible with the same $x$ send it to different futures", "nature": "Main carries the same universal wording"}],
    fix="Hidden states compatible with the same $x$ can send it to different futures, so the visible sector can evolve stochastically although the whole evolves deterministically.",
    notes="Attention resolved: read universally the sentence is false (any realization whose f_x is constant on the posterior's support, e.g. the permutation control in process_dilation_probes.py P4, is visibly deterministic). The existential reading is true and is what the paper uses. Low severity.")
row("I-026", [lk("OI as the physical hypothesis; its physical reading conditional on the representation choice", M(62), "conjecture", [], "conditional")],
    [], "conjecture", M(62), "FAITHFUL")
row("I-027", [lk("'The physical reading ... the identification of nature with a finite reversible substratum — is accordingly conditional on that representation choice, an empirically motivated reconstruction'", M(62), "conjecture", [], "conditional"),
              lk("'what is empirically falsifiable is the framework's physical identification of nature with its deterministic finite ontology'", M(704), "paper-derivation", [], "open")],
    [], "conjecture", M(62), "FAITHFUL", notes="Cited to [Main §4.5]; Main:704 supports it, and Main:62 states it most directly.")
row("I-028", [lk("'The characterization theorem is mathematical ... no experiment falsifies the theorem itself'", M(704), "paper-derivation", [], "proved")],
    [], "proved-paper", M(704), "FAITHFUL")
row("I-029", [lk("'none is established here; no memory-witness outcome therefore falsifies the ontology at present'; 'No ontology-level memory falsifier is established'", M("702-704"), "paper-derivation", [], "open")],
    [], "open", M(702), "FAITHFUL")
row("I-030", [lk("'Observational incompleteness in the sense of the OI core concerns the hidden sector of an embedded observer, not the joint sharpness of non-commuting observables'", M(572), "paper-derivation", [], "proved")],
    [], "proved-paper", M(572), "FAITHFUL")
row("I-031", [lk("'Under (C4) it is present already for a single fixed readout, where no choice between measurements arises'", M(572), "paper-derivation", ["(C4) in Main's reading (hidden memory)"], "proved")],
    [], "proved-paper", M(572), "FAITHFUL",
    notes="Main conditions the sentence on (C4) because it identifies the incompleteness with readout-relevant hidden memory. The Intro defines the incompleteness as inaccessibility of the hidden sector, which is present for a single fixed readout without any condition. Both readings are true; no overclaim.")
row("I-032", [lk("'The visible laws of fixed-readout processes are, by S<=>D<=>Q_fb, exactly the finite stochastic laws, and no uncertainty relation constrains that class'", M(572), "paper-derivation", [], "proved"), K_FHE],
    EQ_HYP, "proved-paper", M(572), "FAITHFUL",
    notes="The class is all laws (kernel), so no non-trivial constraint can hold on it; the inference from 'all laws' to 'no uncertainty relation constrains' is on paper and immediate.")

# ---------------- §1.2 ----------------
row("I-033", [K_D_Q, K_Q_S, lk("'The total system evolves deterministically, but the visible sector alone is stochastic'", M(105), "paper-derivation", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL",
    notes="Every visible marginal of a finite bijection is a stochastic law: D_K subset S_K by composing D_imp_Qfb and Qfb_imp_S.")
row("I-034", [K_S_D, lk("Examples: XOR family (one bit of conditional memory), §2.4 minimal model", M("453; 178-198"), "exact-algebra", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 422, "S_imp_D"), "FAITHFUL",
    notes="Attention resolved: read as 'can produce'. Since S_K subset D_K, every law with conditional memory is a reversible marginal (kernel); the converse universal reading (every marginal has memory) is not asserted.")
row("I-035", [lk("pIndivisible_of_rooted_identity_return_of_overlap", LN("RecurrenceHorizon", 148, "OIBridge.RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap"), "kernel", ["rooted form", "fixed hidden prior"], "proved"),
              lk("Theorem (§2.3): non-permutation T => P-indivisible", M("115-129"), "paper-derivation", [], "proved"), K_S_D],
    [], "proved-kernel", LN("RecurrenceHorizon", 148, "pIndivisible_of_rooted_identity_return_of_overlap"), "FAITHFUL",
    notes="Existential reading; witnesses are kernel-checked (rooted form) and every P-indivisible family is a reversible marginal by S_imp_D.")
row("I-036", [lk("If Gamma_s is invertible, Lambda = Gamma_s^-1 Gamma_t is the unique solution and has unit row sums; if it is not stochastic it has a negative entry", M(121), "exact-algebra", ["Gamma_s invertible"], "proved"),
              lk("'the inverse matrix, if it exists, will always have negative entries unless both matrices are permutation matrices'", "Bar23 (arXiv:2309.03085v2) fn. 5, p. 11", "literature", [], "proved")],
    ["candidate divisor exists (Gamma_s invertible)"], "proved-paper", M(121), "FAITHFUL",
    notes="Elementary: Gamma_s 1 = 1 gives Gamma_s^-1 1 = 1, so row sums are 1. 'Where the candidate exists' is read as invertible Gamma_s; for singular Gamma_s the solution set is affine and 'the candidate' is not unique, a case the parenthesis excludes.")
row("I-037", [lk("Barandes's stochastic-quantum correspondence: indivisible stochastic processes correspond to unitarily evolving quantum systems", "Bar23 (arXiv:2309.03085v2); Bar25 (arXiv:2302.10778v3)", "literature", [], "proved"),
              lk("Main §3.1 uses [11,12] for the same correspondence", M(204), "literature", [], "proved")],
    [], "proved-paper", "Bar25; Bar23", "FAITHFUL")
row("I-038", [K_FHE], EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL",
    notes="'Exact and universal at the level of finite-horizon observable laws' is exactly the kernel statement (every law, each horizon).")
row("I-039", [lk("'representability alone is not the framework's discriminating content. That content is the readback sector'", M(534), "paper-derivation", [], "proved"),
              lk("'The equivalence S<=>D and this universal statement are the paper's core'", M(97), "paper-derivation", [], "proved")],
    [], "proved-paper", M(534), "FAITHFUL",
    notes="Completeness check (owner request): Main's Characterization theorem (Main:516, proof :608; no ledger row, signal S1) is not named in the abstract or §1.2. Its content is (ii) non-Markovian at an accessible order <=> (iii) a per-horizon realization with C1, C3, C4 at k and a fixed hidden prior; plus, under (T), (i) a unitarily evolving representation. Both directions are proved on paper only ((iii)=>(ii) by the Pinsker readback lemma, Main:167-170; (ii)=>(iii) by process dilation and its response-table Extension, Main:496-500), neither formalized (Main:608), and (i) is imported from Barandes under (T). Main itself says (ii)=>(iii) adds only existence of a realization because (C4) coincides with (ii) in every faithful realization (Main:608, :596-598). The Intro carries every ingredient (Theorem 1 for existence; line 84's Pinsker bound; line 86's '(C4) coincides with M_t>0 ... (C1) and (C3) follow') and its internal D_K subset Q_K supersedes (i). Not an understatement of the abstract or §1.2; see part-B1.md, completeness item 1, for an optional sentence.")
row("I-040", [lk("'the equivalence identifies the representation class exactly and stops short of operational quantum mechanics: the instrument algebra is reached exactly when the five operational completion conditions hold'", M(622), "paper-derivation", [], "proved"),
              lk("oi_alone_not_qm", LN("GeneralCarrier", 160, "oi_alone_not_qm"), "kernel", [], "proved")],
    [], "proved-kernel", M(622), "FAITHFUL",
    contra=[{"site": BK("ch01-observation.md", 261), "text": "quantum mechanics is not a separate physical theory ... It is the dynamics that our specific kind of observation produces", "nature": "book essay register asserts more than Theorem 4 and oi_alone_not_qm allow; corpus-side overstatement"},
            {"site": M(22), "text": "In this precise sense the stochastic description of embedded observation and its quantum representation are mathematically equivalent", "nature": "Main limits this to the finite-law level in the same paragraph; consistent"}],
    notes="Faithful for exact operational QM. Completeness: the corpus proves on paper (ledger P, exact probes at d=2) that every bounded quantum experiment of dimension d, horizon K has a finite reversible deterministic epsilon-realization with gluing, and a uniform continuum epsilon-density (Main:544-578; Summary item 4, Main:580). The Intro omits these; they concern realizing quantum statistics inside OI (approximately), not deriving QM from OI, so 'stop short' stays true. Flagged as completeness item 2 in part-B1.md for the §3.4 mapper.")
row("I-041", [lk("CC: descriptive distinction established, dissolution conditional on G3", GR(356), "paper-derivation", [], "open"),
              lk("BH: Page curve conditional on H-scramble and H-decouple", GR(603), "paper-derivation", [], "open")],
    [], "open", GR(356), "FAITHFUL",
    contra=[{"site": GR(326), "text": "## 6. Dissolution of the Cosmological Constant Problem", "nature": "unqualified heading; text conditional (see I-018)"}])
row("I-042", [lk("Main carries the status ledger (§4.5) and points to the probe code papers/oi_lattice_code/foundations/", M("710; 494"), "paper-derivation", [], "proved"),
              lk("Theorem 4 and qubit independence are stated in GR §3.3 with kernel proofs and no paper proof", GR("218-228"), "kernel", [], "proved"),
              lk("§5's results are in BHa/BHb research records and GR App. A", "verification/programmes/black-hole-information/@eae01647", "exhaustive-computation", [], "proved"),
              lk("Theorems 1-3 and the §3.3 lift results are proved in OIBridge modules (Appendix A)", LN("Equivalence", 462, "finite_horizon_equivalence"), "kernel", [], "proved")],
    [], "proved-paper", M(710), "IMPRECISE",
    fix="Most proofs, the status ledger and the probe code are in [Main], which this paper introduces; the operational-completion results are in [GR §3.3], the black-hole computations in [BHa; BHb], and the machine-checked declarations are listed in Appendix A; gravitational applications are in [GR] and [Book].",
    notes="Attention resolved: 'Proofs ... are in [Main]' is broader than the paper's own citations (Theorem 4 to GR §3.3; §5 to BHa/BHb and GR App. A; kernel proofs in OIBridge). Content is not overclaimed; the location is.")

row("I-043", [lk("Every theorem the Intro states traces to Main, GR, BHa/BHb or the kernel (this matrix, rows I-063 onward); the card game is in Book ch01", BK("ch01-observation.md", 265), "paper-derivation", [], "proved")],
    [], "proved-paper", M(526), "FAITHFUL",
    notes="Within my range every result traces to a corpus source. Whether Appendix B adds new content is for the B.x mapper.")
row("I-044", [lk("BH-01 and BH-02 are repository research records, not adopted ('exploratory research ... not adopted')", "verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:3@eae01647", "paper-derivation", [], "proved")],
    [], "proved-paper", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:3@eae01647", "FAITHFUL",
    notes="BH-01's header still says 'unreviewed for adoption' while its review/REVIEW.md records an independent review (BLOCK on wording only) and the report lists post-review changes; the reference list's 'internally reviewed' is consistent with the review file. Reference-list item, not this claim.")
row("I-045", [lk("BH-01 verdicts generated by checks.py; written proofs of C1, C2, C3 (sufficiency), Lemma L, D1; exhaustive enumerations over S_8 and GL(4,2)", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:15-30@eae01647", "exhaustive-computation", [], "proved"),
              lk("BH-02: proofs of C1, C2, C4, C6(a); NUMERICAL (double precision) items C2(ii) and C3, with exact purity controls", "verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:7-30@eae01647", "numerical", [], "proved")],
    [], "proved-paper", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md@eae01647", "FAITHFUL",
    notes="Accurate for every BH result the Intro cites (BH-01 A, C1, C2, item F; BH-02 C1, C6(a)-(b)). BH-02 also contains double-precision items (C2(ii), C3) that are neither exact nor exhaustive; the Intro does not cite them.")
row("I-046", [lk("Status lines: 'not adopted', no theorem designation", "verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:3@eae01647", "none", [], "open")],
    [], "open", "verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:3@eae01647", "FAITHFUL",
    notes="An epistemic disclaimer; no corpus source establishes novelty, and the remnant bound is described in §5 as 'the remnant-capacity form of a known fact'.")
row("I-047", [lk("EGGH26 Prop. 13 (S=>D), Prop. 16 (independent prior); Bar25 p.12, Bar23 §4.3, Bar26 §4 (permutation = unistochastic); SGD19 Eq. (3) (every-step record)", "EGGH26; Bar23; Bar25; Bar26; SGD19 (all read first-hand from arXiv copies)", "literature", [], "proved")],
    [], "proved-paper", "EGGH26 Prop. 13", "FAITHFUL",
    notes="SGD19 (arXiv:1905.03018v2) Eq. (3) read first-hand for this audit: p(r_n|A_0) = tr{P_rn U ... P_r1 U A_0 rho(t_0)}.")
row("I-048", [lk("S_K subset D_K -> EGGH26 Prop. 13 (line 56, 60); D_K subset Q_K -> Bar25 p.12, Bar23 §4.3, Bar26 §4 (line 60); Q_K subset S_K -> 'the Born rule' and SGD19 Eq. (3) (lines 58, 60); reverse inclusions are compositions", "papers/Introduction.md:56-60@4a260ca9", "literature", [], "proved")],
    [], "proved-paper", "SGD19 Eq. (3)", "FAITHFUL",
    notes="Attention resolved: every inclusion has a literature attribution; Q_K subset S_K is attributed to SGD19 Eq. (3), which writes the every-step projectively measured record as a probability.")
row("I-049", [lk("Theorem 2(b),(c) and the capacity bound are data-processing statements (TV monotone under channels; Markov chain X_<t -> H_t -> X_{t+1} given X_t)", M(590), "paper-derivation", [], "proved"),
              lk("Readback lemma uses Pinsker's inequality", M(170), "paper-derivation", [], "proved")],
    [], "proved-paper", M(590), "FAITHFUL")
row("I-050", [lk("Proof uses finite order (phi^N = id) and the contraction direction of the divisibility criterion [4,5]", M("121-129"), "paper-derivation", [], "proved"),
              lk("Buscemi-Datta: equivalence between divisibility and monotonic decrease of information", "BD16 (arXiv:1408.7062v3)", "literature", [], "proved")],
    [], "proved-paper", M(121), "FAITHFUL")
row("I-051", [lk("Doukas Prop. 1 (No distinguishability revival): Markov compatibility implies D(t) <= D(u); 'a distinction that has disappeared cannot reappear'; applied to Rabi oscillations", "Dou26 (arXiv:2602.22095v3), Prop. 1, p. 20", "literature", [], "proved")],
    [], "proved-paper", "Dou26 Prop. 1", "FAITHFUL",
    notes="Doukas states the contraction criterion and the revival obstruction (coincide-then-separate) and applies it to Rabi oscillations; he does not use the finite order of a bijection. Read as 'the contraction criterion ... stated concurrently by Doukas' the clause is exact; read as Doukas stating the finite-recurrence argument, it is slightly loose. Line 92's 'overlap-and-return argument' (another mapper's I-11x) carries the same reading.")
row("I-052", [lk("Theorem 4, independence, oi_alone_not_qm: stated in GR §3.3 with kernel citations; no paper proof (proof inventory: kernel-only)", GR("218-228"), "kernel", [], "proved"),
              lk("§3.3 lift results: stated in Main's Remark with kernel citations (CoherentLiftGauge, TrackBQfbBridge); no written proofs", M(624), "kernel", [], "proved"),
              lk("bridge_traj, rooted_eq_iff_slice_eq, realData_traj_stochastic", LN("TrackBQfbBridge", 276, "bridge_traj"), "kernel", [], "proved")],
    [], "proved-kernel", LN("GeneralCarrier", 100, "exactAll_iff_physical_general"), "MISCITED",
    fix="The results of §3.2–§3.3 are stated in [GR §3.3] and [Main §3.4] and proved in the Lean declarations of Appendix A.",
    notes="Attention resolved: GR and Main carry the statements, but the proofs are the OIBridge declarations; neither paper writes them out (GR:218 is kernel-only per the inventory; Main:624 is a Remark). The content is fine and kernel-proved; 'proved in [GR] and [Main]' names the wrong location.")

row("I-053", [lk("introduction_repro: commit 17b830bc, run 40330683786 (verify, push, success), job 121598983127 'Mathlib bridge' success, toolchain leanprover/lean4:v4.33.0, Mathlib rev v4.33.0 resolved to db584cd6", "papers/introduction_repro/README.md@4a260ca9", "kernel", [], "proved"),
              lk("Lean sources identical: git diff 17b830bc eae01647 -- verification/lean verification/lean-mathlib is empty", "verification/lean-mathlib@eae01647", "kernel", [], "proved")],
    [], "proved-kernel", "papers/introduction_repro/results-121598983127.json@4a260ca9", "FAITHFUL",
    notes="Restricted definition checked: 'machine-checked' names the Appendix A declarations at 17b830bc. What is machine-checked is each declaration's formal statement; where that is narrower than the prose (Theorem 2 for a joint law; Theorem 3 rooted form; readback from routed readback; Theorem 1 with Q_K encoded by its Born chain formula) the Intro says so. No lake-manifest.json is committed, so the Mathlib revision is a tag resolved at run time (README).")
row("I-054", [lk("process_dilation_probes.py: exact Fractions, full-joint equality on specific laws P1-P3 and a permutation control P4", "papers/oi_lattice_code/foundations/process_dilation_probes.py:1-16@eae01647", "exhaustive-computation", [], "proved"),
              lk("review4_probes.py P-G: one non-Markov kernel set, exact", "papers/oi_lattice_code/foundations/review4_probes.py:170-221@eae01647", "exhaustive-computation", [], "proved"),
              lk("c4_backflow_probes.py: laws exact, but I(X_<k;X_{k+1}|X_k) and the bound are evaluated in floating point (float(p)*log2(...), LN2 = log(2.0))", "papers/oi_lattice_code/foundations/c4_backflow_probes.py:15-43@eae01647", "numerical", [], "proved")],
    [], "numerical", "papers/oi_lattice_code/foundations/process_dilation_probes.py@eae01647", "IMPRECISE",
    fix="an \"exact probe\" is a computation on small instances in exact rational arithmetic",
    notes="Attention resolved. The definition promises an exhaustive exact-rational computation. Line 56's probes are exact but check named instances (each enumerated in full), not every law of a small class. Line 84's probe (c4_backflow_probes.py) computes the conditional mutual information and the bound in floating point, so it is not exact-rational; that bears on I-10x (§2.4 mapper). Either narrow the definition or say 'with exact and floating-point probes' at line 84.")
row("I-055", [lk("'a faithful realization is a system as in class (D): a bijection phi of C_V x C_H with an initial law ... which may correlate the hidden and visible coordinates, under which the visible trajectory has the given law'", M(97), "paper-derivation", [], "proved"),
              lk("RevReal / RevRealizable", LN("Equivalence", 157, "OIBridge.Equivalence.RevReal"), "kernel", [], "proved")],
    [], "proved-paper", M(97), "FAITHFUL")
row("I-056", [lk("Glossary: 'Substratum. The framework's underlying deterministic, finite-dimensional, bijective dynamical system (S, phi)'", BK("glossary.md", 137), "paper-derivation", [], "proved"),
              lk("Main: 'The bijective substratum is a representation choice'", M(62), "paper-derivation", [], "proved")],
    [], "proved-paper", BK("glossary.md", 137), "FAITHFUL",
    notes="Attention resolved: the generic usage matches Main and the book glossary. The cubic-lattice bijection with coupling matrix (AGENTS.md, SM, Substratum) is the specific construction of the matter sector, a special case. No conflict for this paper, which never uses the cubic lattice.")

# ---------------- §2.1 ----------------
row("I-057", [lk("'the emergent law is a function of (phi, partition, mu_H)'", M(60), "paper-derivation", [], "proved")], [], "proved-paper", M(60), "FAITHFUL")
row("I-058", [lk("'a realization ... carries its own fixed hidden prior mu_H as part of the realization datum'; Lemma 3: invariance fixes the measure only per orbit, the global choice is 'a selection principle, not uniqueness from invariance alone'", M("56; 60"), "paper-derivation", [], "proved")],
    [], "proved-paper", M(60), "FAITHFUL")
row("I-059", [lk("'the counting measure is selected among invariant measures as the maximal-entropy one'; 'the counting measure is the default, not a constraint on representations'", M("56; 60"), "paper-derivation", [], "proved")], [], "proved-paper", M(60), "FAITHFUL")
row("I-060", [lk("(S) the finite stochastic laws", M(528), "paper-derivation", [], "proved"), lk("Stochastic P := nonneg and sums to 1", LN("Equivalence", 147, "OIBridge.Equivalence.Stochastic"), "kernel", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 147, "Stochastic"), "FAITHFUL")
row("I-061", [lk("(D) visible marginals of finite reversible deterministic systems; the kernel carrier's initial law 'may correlate the hidden and visible coordinates'", M("529; 532"), "paper-derivation", [], "proved"),
              lk("RevReal: Hid finite, step : (V x Hid) ~ (V x Hid), init : V x Hid -> R", LN("Equivalence", 157, "RevReal"), "kernel", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 157, "RevReal"), "FAITHFUL")
row("I-062", [lk("(Q_fb) finite-dimensional unitary systems, projective Born measurement in a fixed basis at every step, initial state diagonal, record a fixed function of each outcome", M(530), "paper-derivation", [], "proved"),
              lk("QfbReal: Bas finite, U unitary, init : Bas -> R (diagonal weights), read : Bas -> V; law = marg of the Born chain", LN("Equivalence", 190, "OIBridge.Equivalence.QfbReal"), "kernel", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 190, "QfbReal"), "FAITHFUL",
    notes="The kernel class has no autonomous-generator clause (Equivalence.lean header); neither does the Intro's definition. Match.")

# ---------------- §2.2 ----------------
row("I-063", [K_FHE, P_FHE, lk("Ledger MAIN:T-finite-horizon-stochastic-reversible-unitary: K3 ('the exact manuscript statement is proved in Lean')", "verification/coverage/LEDGER.json@eae01647", "kernel", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL",
    contra=[{"site": "papers/Introduction.md:36@4a260ca9", "text": "Fix finite sets C_V (with |C_V|>=2)", "nature": "§2.1's standing |C_V|>=2 is not needed: the kernel holds for every finite type. 'For every finite visible alphabet' in Theorem 1 is the accurate (stronger) statement; the restriction is harmless"}],
    notes="Each direction traced separately (I-063.a-c). Hypotheses of the kernel: Fintype and DecidableEq on V, any K. No |V|>=2, no Nonempty.")
row("I-063.a", [K_S_D], EQ_HYP, "proved-kernel", LN("Equivalence", 422, "S_imp_D"), "FAITHFUL")
row("I-063.b", [K_D_Q], EQ_HYP, "proved-kernel", LN("Equivalence", 294, "D_imp_Qfb"), "FAITHFUL")
row("I-063.c", [K_Q_S], EQ_HYP, "proved-kernel", LN("Equivalence", 245, "Qfb_imp_S"), "FAITHFUL")
row("I-064", [K_FHE], EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL", notes="Declaration at Equivalence.lean:462 confirmed at eae01647 (sources identical to 17b830bc); #print axioms at :480.")
row("I-065", [K_S_D], EQ_HYP, "proved-kernel", LN("Equivalence", 422, "S_imp_D"), "FAITHFUL", notes="Declaration at :422 confirmed.")
row("I-066", [K_D_Q], EQ_HYP, "proved-kernel", LN("Equivalence", 294, "D_imp_Qfb"), "FAITHFUL", notes="Declaration at :294 confirmed.")
row("I-067", [K_Q_S], EQ_HYP, "proved-kernel", LN("Equivalence", 245, "Qfb_imp_S"), "FAITHFUL", notes="Declaration at :245 confirmed.")
row("I-068", [lk("Reverse arrows: fun h => Qfb_imp_S P (D_imp_Qfb P h); fun h => S_imp_D P (Qfb_imp_S P h); fun h => D_imp_Qfb P (S_imp_D P h)", LN("Equivalence", 466, "finite_horizon_equivalence (lines 466-468)"), "kernel", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 466, "finite_horizon_equivalence"), "FAITHFUL")
row("I-069", [lk("finite_horizon_equivalence has only P as argument; no realization or construction hypothesis", LN("Equivalence", 462, "finite_horizon_equivalence"), "kernel", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL")
row("I-070", [lk("S_imp_D carrier: Hid = Fin (K+1) x Traj V K (clock and complete trajectory record); init = pushforward of P along tau -> (tau 0, (0, tau)); padded to a bijection by exists_perm_extending", LN("Equivalence", 422, "S_imp_D"), "kernel", [], "proved"),
              lk("EGGH26 Prop. 13: 'A large enough ancilla can label a complete system trajectory'", "EGGH26 (arXiv:2602.23491v1) Prop. 13, p. 30", "literature", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 422, "S_imp_D"), "FAITHFUL",
    contra=[{"site": M(532), "text": "(S => D) is the response-table construction of §3.4 ... (kernel: S_imp_D, by a different carrier, a clock with the complete trajectory record ...)", "nature": "Main's written proof uses the response-table construction; the Intro describes the kernel's carrier. Both are stated in Main; consistent"}])
row("I-071", [lk("Theorem (finite-horizon process dilation): rational multi-time law -> finite C_H, bijection, hidden prior independent of the visible initial state, reproducing the full law", M(496), "paper-derivation", ["rational law", "|C_V|>=2"], "proved"),
              lk("Extension (arbitrary priors — the response-table form): product prior mu(u) = prod_c kern_c(u_c), deterministic step x_{k+1} := u_{c(x<=k)}, ledger and clock complete the bijection; reproduces the full joint 'for arbitrary real kernels'", M(498), "paper-derivation", ["finite horizon"], "proved"),
              lk("process_dilation_probes.py (exact, instances P1-P5) and review4_probes.py P-G (exact, one non-Markov kernel set)", "papers/oi_lattice_code/foundations/process_dilation_probes.py@eae01647", "exhaustive-computation", [], "proved"),
              lk("EGGH26 Prop. 16: independent fixed ancilla distribution for an arbitrary stochastic dynamical system (no rationality; not reversible)", "EGGH26 (arXiv:2602.23491v1) Prop. 16, p. 34", "literature", [], "proved"),
              lk("Status ledger: '(ii) => (iii) ... arbitrary-prior form via the response-table extension'", M(715), "paper-derivation", [], "proved"),
              lk("Partial kernel analogue, rooted families only: responseRealization / responsePrior put any row-stochastic rooted family on one finite seed with one prior shared by every visible root, 'without assuming rational probabilities' (module header); covers Gamma_t(x_0 -> x_t), not the full multi-time law", "lean:OIBridge/RootedClassification.lean:330:OIBridge.RootedClassification.responseRealization", "kernel", ["rooted (one-time) family, not the trajectory law"], "proved")],
    ["finite horizon K", "finite visible alphabet"], "proved-paper", M(498), "UNDERCLAIM",
    fix="A realization whose hidden prior is independent of $x_0$ also exists for every law [Main §3.4, Theorem (finite-horizon process dilation) and its Extension (response-table form)]; it is proved on paper, with exact probes.",
    notes="The rationality restriction belongs to the uniform-tape presentation only; Main's Extension (Main:498), its status ledger (Main:715) and the Characterization theorem (which 'quantifies over general finite-horizon laws') give the independent-prior reversible realization for every finite-horizon law. The argument is short and sound (x_0 drawn independently of the product prior; conditioning exposes u only at visited contexts). Not formalized for the full multi-time law (Main:500: 'the independence of mu_H from the visible initial state rests on the construction above and the cited probes and is not formalized'); the kernel has the independent-prior response-table construction only for rooted families (RootedClassification.responseRealization, no rationality assumption). Coordinator relay from B5 checked and confirmed. The Intro's own attribution sentence cites EGGH26 Prop. 16, which is likewise unrestricted. Also see I-054 on what the probes are.")
row("I-072", [K_D_Q, lk("'for a bijection phi set U_phi|x,h> = |phi(x,h)> and take the initial law diagonal ... sequential projective measurements in the configuration basis do not disturb the state'", M(532), "paper-derivation", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 294, "D_imp_Qfb"), "FAITHFUL",
    notes="Kernel uses permMatrix of step.symm, i.e. U|s> = |phi(s)> in its convention.")
row("I-073", [K_Q_S, lk("'(Q_fb => S) is the Born rule: the record of any finite quantum experiment is a finite stochastic law'", M(532), "paper-derivation", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 245, "Qfb_imp_S"), "FAITHFUL",
    notes="Kernel content is that the Born chain weights are nonnegative and normalize by unitarity (sum_chain), 'not a definitional unfolding'.")
row("I-074", [lk("EGGH26 Prop. 13: deterministic system-ancilla dynamics A : T x C x Lambda -> C, family of correlated initial distributions, M_A = M", "EGGH26 (arXiv:2602.23491v1) Prop. 13, p. 30", "literature", [], "proved"), K_S_D],
    [], "proved-paper", "EGGH26 Prop. 13", "FAITHFUL",
    notes="EGGH26's A is time-indexed and need not be a bijection; the clock-and-pad construction (exists_perm_extending) is the packaging into one iterated bijection, which the sentence acknowledges.")
row("I-075", [lk("EGGH26 Prop. 16: fixed ancilla distribution lambda_0, uncorrelated initial family (114), M_A = M_S; A not required bijective", "EGGH26 (arXiv:2602.23491v1) Prop. 16, p. 34", "literature", [], "proved")],
    [], "proved-paper", "EGGH26 Prop. 16", "FAITHFUL")
row("I-076", [lk("LP17 Prop. 1.5: 'Every transition matrix on a finite state space has a random mapping representation'", "LP17 (Levin-Peres-Wilmer, 2nd ed.) Prop. 1.5", "literature", [], "proved")],
    [], "proved-paper", "LP17 Prop. 1.5", "FAITHFUL")
row("I-077", [lk("'every permutation matrix is unistochastic ... a stochastic process defined by a permutation matrix Sigma is a special case of a unistochastic process'", "Bar25 (arXiv:2302.10778v3) p. 12; Bar23 (arXiv:2309.03085v2) §4.3; Bar26 (arXiv:2608.04354v1) §4", "literature", [], "proved")],
    [], "proved-paper", "Bar25 p. 12", "FAITHFUL")
row("I-078", [lk("Lemma (one-step ancilla dilation): W|i> = sum_j sqrt(T_ij)|j>|i> is an isometry C^n -> C^n (x) C^n with ancilla-marginal T, extending to a unitary on C^n (x) C^n", M("206-208"), "paper-derivation", [], "proved"),
              lk("Bar26 Thm 3.3 (Unistochastic Theorem): N^2 x N^2 unitary with marginalization formula; constructive proof via Theta with |Theta|^2 = Gamma and Kraus K_i = Theta P_i", "Bar26 (arXiv:2608.04354v1) Thm 3.3, pp. 7-10", "literature", [], "proved"),
              lk("Sch21 Thm 2: every stochastic matrix admits a standard dilation by an N^2 x N^2 bi-stochastic, indeed unistochastic, matrix", "Sch21 (arXiv:2106.03513v1) Thm 2, p. 10", "literature", [], "proved"),
              lk("Bar26 fn. 1: 'Schmidt (2021) presented a similar theorem, but the proof there appears to have an error in its construction of the required partial isometry'", "Bar26 (arXiv:2608.04354v1) fn. 1, p. 8", "literature", [], "proved")],
    [], "proved-paper", M(206), "IMPRECISE",
    fix="the one-step $n^2$-dimensional ancilla dilation of [Main §3.1], for a stochastic matrix on $n$ states, has the form of the dilations of Barandes [Bar26, Thm 3.3] and Schmidt [Sch21, Thm 2]",
    notes="Main's W coincides with Bar26's construction for Theta = entrywise sqrt(Gamma). Schmidt's theorem has the same N^2 form, but Barandes reports an apparent error in Schmidt's partial-isometry construction, so 'coincides with the constructions of ... Schmidt' asserts more than is checked. 'n' is undefined in the Intro. Main itself makes no coincidence claim. Low severity.")
row("I-079", [lk("SGD19 Eq. (3): p(r_n|A_0) = tr_SE{P_rn U_{n,n-1} ... P_r1 U_{1,0} A_0 rho_SE(t_0)}", "SGD19 (arXiv:1905.03018v2) Eq. (3), p. 1", "literature", [], "proved")],
    [], "proved-paper", "SGD19 Eq. (3)", "FAITHFUL", notes="Read first-hand for this audit.")
row("I-080", [lk("SGD19 asks when the consistency condition (2), sum over r_k of the joint = the joint with t_k omitted, holds", "SGD19 (arXiv:1905.03018v2) Eq. (2), pp. 1-2", "literature", [], "proved"),
              lk("Milz et al., 'When is a non-Markovian quantum process classical?' (read first-hand in the earlier introductory-paper audit, FT-r4 list)", "Milz20 (arXiv:1907.05807v3)", "literature", [], "proved")],
    [], "proved-paper", "SGD19 Eq. (2)", "FAITHFUL")
row("I-081", [lk("Q_K measures at every step (definition, line 44; QfbReal.chain)", LN("Equivalence", 209, "OIBridge.Equivalence.QfbReal.chain"), "kernel", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 209, "QfbReal.chain"), "FAITHFUL", notes="Definitional.")

# ---------------- §2.3 ----------------
row("I-082", [K_FHE], EQ_HYP, "proved-kernel", LN("Equivalence", 462, "finite_horizon_equivalence"), "FAITHFUL")
row("I-083", [K_FHE, lk("'the process-dilation construction of §3.4 realizes Markov laws as well, so the right-hand side is satisfied by processes with no memory at all'", M(598), "paper-derivation", [], "proved")],
    EQ_HYP, "proved-kernel", M(598), "FAITHFUL")
row("I-084", [lk("'Inside Q_fb the Born dictionary p=|U|^2 is ... part of the definition of the class'", M(534), "paper-derivation", [], "proved"),
              lk("QfbReal.born := ||U b' b||^2", LN("Equivalence", 205, "QfbReal.born"), "kernel", [], "proved")],
    [], "proved-kernel", LN("Equivalence", 205, "QfbReal.born"), "FAITHFUL")
row("I-085", [K_D_Q, lk("'the unitaries it supplies are permutations, whose entries are 0 or 1'", M(534), "paper-derivation", [], "proved")],
    EQ_HYP, "proved-kernel", LN("Equivalence", 294, "D_imp_Qfb"), "FAITHFUL")
row("I-086", [lk("Entries 0/1 give |U|^p = |U|^2 for every p>0; check 6 of equivalence_recovery_probes.py", M(534), "exact-algebra", ["U a permutation matrix"], "proved")],
    ["U a permutation"], "proved-paper", M(534), "FAITHFUL")
row("I-087", [lk("'the construction does not SELECT the quadratic exponent ... no step distinguishes p=2'", M(534), "paper-derivation", [], "proved"),
              lk("Bar26 Thm 3.1 (Born Representation Theorem): every M x N stochastic matrix has Gamma_ij = tr(E_i P_j) with diagonal POVM and PVM", "Bar26 (arXiv:2608.04354v1) Thm 3.1, p. 5", "literature", [], "proved")],
    [], "proved-paper", M(534), "FAITHFUL",
    notes="The exponent argument is Main's (0/1 entries). Bar26 Thm 3.1 shows Born form is available for every stochastic matrix, the related non-selection point; it does not discuss exponents. Acceptable as supporting citation.")
row("I-088", [lk("'a bijection on a finite set has finite order L'", M(618), "exact-algebra", [], "proved"),
              lk("rootedMap_periodic (period from card of Perm(V x H))", LN("RootedClassification", 135, "rootedMap_periodic"), "kernel", [], "proved")],
    [], "proved-kernel", LN("RootedClassification", 135, "rootedMap_periodic"), "FAITHFUL")
row("I-089", [lk("'any fixed realization with a fixed prior has an exactly L-periodic multi-time law (phi^{k+L} = phi^k)'", M(618), "paper-derivation", ["fixed prior"], "proved")],
    [], "proved-paper", M(618), "FAITHFUL")
row("I-090", [lk("'The equivalence is per-horizon'", M(618), "paper-derivation", [], "proved"), K_FHE],
    [], "proved-kernel", M(618), "FAITHFUL")
row("I-091", [lk("'a nonperiodic target admits no exact all-time realization by one fixed finite substratum'", M(618), "paper-derivation", [], "proved"),
              lk("Proposition (no horizon-independent intervened representation) for the intervened case", M(472), "paper-derivation", [], "proved")],
    [], "proved-paper", M(618), "FAITHFUL",
    notes="Every trajectory of one fixed finite bijection is L-periodic, so a law not supported on L-periodic trajectories for any L has no exact all-time realization. Elementary and sound.")

ids = [r["id"] for r in rows]
want = []
for e in claims:
    n = int(e["id"][2:5])
    if n <= 91:
        want.append(e["id"])
        if e.get("direction"):
            want += [s["id"] for s in e["direction"]["sub_claims"]]
assert ids == want, (set(want) - set(ids), set(ids) - set(want))
for r in rows:
    e = byid[r["id"]]
    src = e["_parent"]["text"] if "_parent" in e else e["text"]
    assert r["text"] == src
json.dump(rows, open(A + "/matrix/part-B1.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(rows), Counter(r["verdict"] for r in rows))
print(Counter(r["proof_status"] for r in rows))
