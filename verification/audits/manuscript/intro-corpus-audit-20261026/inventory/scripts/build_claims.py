"""Build the Introduction claim inventory (audit step 2a).

Usage: python3 -I build_claims.py <intro.md> <out_claims.json> <out_stats.json>
Every `text` is validated as a verbatim substring of the cited line(s).
"""
import json, sys, collections

SRC, OUT, STATS = sys.argv[1], sys.argv[2], sys.argv[3]
LINES = open(SRC, encoding="utf-8").read().split("\n")

def L(n):
    return LINES[n - 1]

SECTIONS = [
    (12, 12, "Abstract"), (16, 22, "§1.1"), (24, 26, "§1.2"), (28, 28, "§1.2 Contributions"),
    (30, 30, "§1.2 Conventions"), (34, 44, "§2.1"), (46, 60, "§2.2"), (62, 68, "§2.3"),
    (70, 86, "§2.4"), (88, 98, "§2.5"), (102, 108, "§3.1"), (110, 120, "§3.2"),
    (122, 126, "§3.3"), (128, 130, "§3.4"), (132, 136, "§3.5"), (138, 152, "§4"),
    (154, 162, "§5"), (166, 168, "§6.1"), (170, 179, "§6.2"), (181, 185, "§6.3"),
    (187, 191, "§6.4"), (193, 200, "Code, data and formal verification"),
    (202, 215, "Appendix A"), (217, 228, "Appendix B.1"), (230, 232, "Appendix B.2"),
    (234, 255, "Appendix B.3"), (257, 343, "References"),
]

def section_of(n):
    for a, b, s in SECTIONS:
        if a <= n <= b:
            return s
    raise SystemExit(f"no section for line {n}")

LEVELS = {"K": "proved-kernel", "P": "proved-paper", "C": "conditional", "CAL": "calibration",
          "N": "numerical", "CJ": "conjecture", "O": "open", "U": "unstated"}
TYPES = {"theorem-statement", "result", "negative", "status", "scope", "numerical",
         "attribution", "definition-used"}

ENTRIES = []

def E(line, text, claim, typ, level, cited=(), hyp=(), note=None, direction=None,
      line_end=None, after=None, flag=None):
    """text: a verbatim string, or (start, end) anchors resolved on the line(s)."""
    block = "\n".join(LINES[line - 1:(line_end or line)])
    if isinstance(text, tuple):
        a, b = text
        i = block.index(a, block.index(after) if after else 0)
        j = block.index(b, i) + len(b)
        text = block[i:j]
    start = block.index(after) if after else 0
    pos = block.find(text, start)
    if pos < 0:
        raise SystemExit(f"line {line}: span not found: {text[:80]!r}")
    assert typ in TYPES, typ
    st = {"level": LEVELS[level], "hypotheses": list(hyp)}
    if note:
        st["note"] = note
    e = {"section": section_of(line), "line": line}
    if line_end:
        e["line_end"] = line_end
    e.update({"text": text, "claim": claim, "type": typ, "status_as_stated": st,
              "cited": list(cited), "direction": direction})
    if flag:
        e["attention"] = flag
    ENTRIES.append((line, pos, len(ENTRIES), e))

def D(kind, *subs):
    """Direction object. subs: (label, claim, level, cited, rests_on/note)."""
    return {"kind": kind, "sub_claims": [
        {"label": lab, "claim": c, "status_as_stated": LEVELS[lv], "cited": list(ci),
         **({"note": nt} if nt else {})} for (lab, c, lv, ci, nt) in subs]}

SF = " (sentence-final)"
OI_HYP = "OI (physical hypothesis)"

# ---------------------------------------------------------------- Abstract (line 12)
E(12, "Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics",
  "OI is defined as the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only visible marginals.",
  "definition-used", "CJ", hyp=[OI_HYP], note="stated as a hypothesis, not established")
THM1_DIR = lambda lv, ci: D("set-equality (three classes; each inclusion is one direction)",
    ("S_K ⊆ D_K", "Every finite-horizon law has a faithful finite reversible realization.", lv, ci + ["`S_imp_D`"], None),
    ("D_K ⊆ Q_K", "Every visible law of a finite bijection is a fixed-basis Born record of a finite unitary system.", lv, ci + ["`D_imp_Qfb`"], None),
    ("Q_K ⊆ S_K", "Every fixed-basis Born record law is a probability law on visible trajectories.", lv, ci + ["`Qfb_imp_S`"], None))
E(12, "At every finite horizon, three classes of law on visible trajectories coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the fixed-basis Born records of finite unitary systems",
  "Abstract form of Theorem 1: at every finite horizon, finite stochastic laws = visible marginals of finite reversible dynamics = fixed-basis Born records of finite unitary systems.",
  "theorem-statement", "U", note="abstract carries no status; body (§2.2) states machine-checked",
  direction=THM1_DIR("U", []))
E(12, "The components of this correspondence are known, from the trajectory-labelling realization of Egri et al. and Barandes's treatment of permutation dynamics as unistochastic processes",
  "The components of the correspondence are known from Egri et al.'s trajectory-labelling realization and Barandes's treatment of permutation dynamics as unistochastic.",
  "attribution", "U", note="authors named without bracket citations in the abstract")
E(12, "Each class contains the Markov laws", "Each of the three classes contains the Markov laws.", "result", "U")
E(12, "so representability does not distinguish a law with memory from one without",
  "Representability (realization / fixed-basis unitary representation) does not distinguish laws with memory from Markov laws.", "negative", "U")
E(12, "and the Born exponent is not selected", "The correspondence does not select the Born exponent.", "negative", "U")
E(12, "The discriminating content concerns memory", "The discriminating content of OI concerns memory.", "scope", "U")
E(12, "every deterministic completion carries the visible memory in its hidden state",
  "Every deterministic completion (faithful realization) carries the visible law's memory in its hidden state.",
  "result", "P", note="abstract: machine-checked except one step (\"each with one step not machine-checked\"); weakest link therefore proved on paper",
  flag="Abstract says 'every deterministic completion carries the visible memory'; body (Theorem 2, Corollary) says readout-relevant hidden memory exists in every faithful realization exactly when M_t>0. Mapper: confirm 'deterministic completion' = 'faithful realization' and that the claim is conditional on M_t>0.")
E(12, "on a fixed finite reversible system finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle",
  "On a fixed finite reversible system, finite recurrence plus history readback (C4) forces stochastic indivisibility somewhere in the recurrence cycle.",
  "result", "P", hyp=["(C4) history readback", "fixed finite reversible system"],
  note="abstract: machine-checked except one step; body: machine-checked from routed-readback (C4), on paper from history-level (C4)")
E(12, "(each with one step not machine-checked)",
  "The two preceding abstract results are each machine-checked except for one step.", "status", "P",
  flag="'one step' is unspecified. For Theorem 2 the body names two unchecked ingredients (time-t identification and the CMI vanishing criterion, line 82); for readback the unchecked step is history-level (C4). Mapper: check that 'one step' is accurate for each.")
E(12, "Exact finite operational quantum mechanics is characterized by five completion conditions",
  "Exact finite operational QM is characterized (iff) by five completion conditions (Theorem 4).", "theorem-statement", "U",
  note="abstract carries no status; body (§3.2) states both directions machine-checked",
  direction=D("equivalence (characterization)",
    ("⇒", "If the available families are exactly the normalized finite Kraus instruments, conditions (i)–(v) hold.", "U", [], None),
    ("⇐", "If conditions (i)–(v) hold, the available families are exactly the normalized finite Kraus instruments.", "U", [], None)))
E(12, "none implied by OI alone", "None of the five completion conditions is implied by OI alone.", "negative", "U")
E(12, "Open are which of conditions (iii)–(v) a physical substratum supplies",
  "Which of conditions (iii)–(v) a physical substratum supplies is open.", "status", "O")
E(12, "the selection of the evolution relating two times", "Selection of the evolution relating two times is open.", "status", "O")
E(12, "and any test of the hypothesis", "Any test of the OI hypothesis is open.", "status", "O")
E(12, "Applied to the cosmological constant, OI places the zero-point sum and the effective cosmological constant at different levels of description",
  "OI places the zero-point sum and the effective cosmological constant at different levels of description.", "result", "U")
E(12, "whether the zero-point sum sources curvature depends on covariant field equations that are not derived",
  "Whether the zero-point sum sources curvature depends on covariant field equations that are not derived.", "status", "O",
  hyp=["covariant field equations (not derived)"])
E(12, "so this is a proposal, not a resolution", "The cosmological-constant treatment is a proposal, not a resolution.", "status", "CJ")
E(12, "Applied to black-hole information, finite computations separate the conservation of information under bijective dynamics from its recovery by an observer with restricted access",
  "Finite computations separate information conservation under bijective dynamics from recovery by an observer with restricted access.", "result", "N")
E(12, "the framework's Page curve is not established", "The framework's Page curve is not established.", "status", "O")
E(12, "the information problem is not resolved", "The black-hole information problem is not resolved.", "negative", "O")

# ---------------------------------------------------------------- §1.1
E(18, ("Embedded observation is modelled by a triple", r"not $h\in\mathcal C_H$."),
  "Embedded observation is modelled by (S, φ, V): finite S = C_V × C_H, a bijection φ of S, and an observer registering x ∈ C_V and not h ∈ C_H.",
  "definition-used", "U", cited=["[Main §1.2]"])
E(20, r"The bijection $\varphi$ is the reversible representative of the hidden dynamics, motivated by observed near-unitarity",
  "Taking φ bijective (reversible representative of the hidden dynamics) is a posit motivated by observed near-unitarity.",
  "status", "CJ", cited=["[Main §1.2, Remark (status of the early commitments)]" + SF], note="posit, motivated empirically")
E(20, "finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]",
  "Finiteness of all of S is a posit.", "status", "CJ", cited=["[Main §1.2, Remark (status of the early commitments)]"], note="posit")
E(20, "Hidden states compatible with the same $x$ send it to different futures, so the visible sector evolves stochastically although the whole evolves deterministically.",
  "Hidden states compatible with the same x send it to different futures, so the visible sector evolves stochastically though the whole is deterministic.",
  "result", "U",
  flag="Stated universally; it holds only when f_x is non-constant on the support of the hidden posterior. Mapper: read as 'can send'.")
E(22, "Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation.",
  "OI is the physical hypothesis that every physical observer is in the (S, φ, V) situation.", "definition-used", "CJ", hyp=[OI_HYP])
E(22, "Identifying nature with such a system is a representation choice, motivated empirically",
  "Identifying nature with such a system is an empirically motivated representation choice.", "status", "CJ", cited=["[Main §4.5]" + SF])
E(22, "the theorems below are mathematical", "The paper's theorems are mathematical (not tests of the physical identification).", "scope", "U", cited=["[Main §4.5]" + SF])
E(22, "no test of the identification at the level of memory witnesses is established [Main §4.5]",
  "No test of the identification at the level of memory witnesses is established.", "status", "O", cited=["[Main §4.5]"])
E(22, "The incompleteness is inaccessibility of the hidden sector, not joint unsharpness of non-commuting observables",
  "OI's incompleteness is inaccessibility of the hidden sector, not joint unsharpness of non-commuting observables.", "scope", "U", cited=["[Main §3.4]" + SF])
E(22, "it is present for a single fixed readout", "The incompleteness is present for a single fixed readout.", "result", "U", cited=["[Main §3.4]" + SF])
E(22, "no uncertainty relation constrains fixed-readout visible laws [Main §3.4]",
  "No uncertainty relation constrains fixed-readout visible laws.", "negative", "U", cited=["[Main §3.4]"])

# ---------------------------------------------------------------- §1.2
E(26, "Marginalizing a reversible dynamics over an unobserved register produces stochastic laws",
  "Marginalizing reversible dynamics over an unobserved register yields stochastic visible laws.", "result", "U")
E(26, "conditional memory", "Marginalizing reversible dynamics can produce conditional memory.", "result", "U",
  flag="'produces' read as 'can produce' for memory and divisibility failure (not every marginal has them).")
E(26, "and failures of stochastic divisibility, in which no stochastic intermediate transition map exists",
  "Marginalizing reversible dynamics can produce failures of stochastic divisibility (no stochastic intermediate map exists).", "result", "U")
E(26, "(where the candidate intermediate matrix exists, it has negative entries)",
  "In a divisibility failure, where the candidate intermediate matrix exists, it has negative entries.", "result", "U",
  note="holds when Γ_s is invertible: Γ_s^{-1}Γ_t has unit row sums, so non-stochastic means a negative entry")
E(26, "The stochastic–quantum correspondence relates these features to quantum theory [Bar23; Bar25].",
  "The stochastic–quantum correspondence relates stochastic laws, memory and indivisibility to quantum theory.", "attribution", "U", cited=["[Bar23; Bar25]"])
E(26, "At the level of finite-horizon observable laws the correspondence of §2 (Theorem 1) is exact and universal",
  "Theorem 1's correspondence is exact and universal at the level of finite-horizon observable laws.", "result", "U")
E(26, "so the content lies in where the memory of a law must sit (§2.4) and what finite recurrence does with it (§2.5)",
  "Because the correspondence is universal, the content lies in where memory must sit and what finite recurrence does with it.", "scope", "U")
E(26, "its foundation and quantum-emergence results, which stop short of operational quantum mechanics (§§2–3)",
  "OI's foundation and quantum-emergence results stop short of operational quantum mechanics.", "negative", "U")
E(26, "Neither application is a demonstrated resolution of its problem",
  "Neither the cosmological-constant nor the black-hole application is a demonstrated resolution.", "negative", "O")
E(26, "Proofs, the status ledger and the probe code are in [Main], which this paper introduces",
  "The proofs, status ledger and probe code are in [Main].", "scope", "U", cited=["[Main]"],
  flag="Theorem 4 and §3.2 are cited to [GR §3.3]; §5's results to [BHa; BHb] and [GR App. A]; line 28 says §3.2–§3.3 results are proved in [GR] and [Main]. 'Proofs ... are in [Main]' is broader than the citations support.")
E(28, "The paper claims no new theorem or physical result; its contribution is expository.",
  "The paper claims no new theorem or physical result; it is expository.", "scope", "U")
E(28, "The black-hole results of §5 are reported from unpublished repository research records [BHa; BHb]",
  "The §5 black-hole results come from unpublished repository research records.", "status", "U", cited=["[BHa; BHb]"])
E(28, "with written proofs and exact or exhaustive checks",
  "The §5 black-hole results have written proofs and exact or exhaustive checks.", "status", "P", cited=["[BHa; BHb]"],
  note="also numerical (exact/exhaustive checks)")
E(28, "whose novelty has not been established", "The novelty of the §5 black-hole results has not been established.", "status", "O")
E(28, "The components of Theorem 1 are known [EGGH26; Bar23; Bar25; Bar26; SGD19]",
  "The components of Theorem 1 are known in the literature.", "attribution", "U", cited=["[EGGH26; Bar23; Bar25; Bar26; SGD19]"])
E(28, "the paper states them as one theorem with each direction attributed",
  "Each direction of Theorem 1 is attributed to prior literature.", "scope", "U",
  flag="Check that every inclusion has a literature attribution: Q_K ⊆ S_K is attributed only as 'the Born rule' (line 58) and [SGD19] (line 60).")
E(28, "The memory bounds of §2.4 are forms of the data-processing and Pinsker inequalities.",
  "The §2.4 memory bounds are forms of the data-processing and Pinsker inequalities.", "attribution", "U")
E(28, "The recurrence argument of §2.5 combines finite order with the known contraction criterion for divisibility [RHP14; BD16]",
  "The §2.5 recurrence argument combines finite order with the known contraction criterion for divisibility.", "attribution", "U", cited=["[RHP14; BD16]"])
E(28, "stated concurrently by Doukas [Dou26]", "Doukas states the recurrence argument concurrently.", "attribution", "U", cited=["[Dou26]"])
E(28, "The results of §3.2–§3.3 are proved in [GR] and [Main].",
  "The §3.2–§3.3 results are proved in [GR] and [Main].", "status", "P", cited=["[GR]", "[Main]"],
  note="wording 'proved' does not name the layer; Appendix A lists kernel declarations for §3.2–§3.3",
  flag="The §3.2–§3.3 kernel declarations are OIBridge modules; check that [GR]/[Main] actually carry these results (especially §3.3's coherent-lift results and the qubit independence).")
E(30, ('"Machine-checked" means checked in Lean 4/Mathlib', "(declarations in Appendix A)"),
  "'Machine-checked' means checked in Lean 4/Mathlib at commit 17b830bc by the stated recipe, declarations in Appendix A.",
  "definition-used", "U", cited=["[dMU21; Mathlib20]"])
E(30, 'an "exact probe" is an exhaustive computation in exact rational arithmetic at small size',
  "An 'exact probe' is an exhaustive exact-rational computation at small size.", "definition-used", "U",
  flag="Mapper: each 'with exact probes' claim (lines 56, 84) must be backed by probes that are exhaustive and exact-rational, per this definition.")
E(30, (r"A *faithful realization* of a law", "has that law"),
  "A faithful realization of a law is a bijection φ of C_V × C_H with an initial law under which the visible trajectory has that law.",
  "definition-used", "U")
E(30, r"the finite reversible system $(S,\varphi)$ is the *substratum*",
  "The finite reversible system (S, φ) is called the substratum.", "definition-used", "U",
  flag="Corpus usage of 'substratum' (e.g. AGENTS.md: bijection on a cubic lattice with coupling matrix) is more specific; check consistency with Main/GR.")

# ---------------------------------------------------------------- §2.1
E(38, "The visible law of a realization depends on the dynamics, the partition and the initial law",
  "A realization's visible law depends on the dynamics, the partition and the initial law.", "scope", "U",
  cited=["[Main §1.2, Remark (the measure as a realization datum)]" + SF])
E(38, r"the prior is part of the realization datum, not selected by invariance under $\varphi$",
  "The prior is part of the realization datum and is not selected by φ-invariance.", "definition-used", "U",
  cited=["[Main §1.2, Remark (the measure as a realization datum)]" + SF])
E(38, "the counting measure is a maximal-entropy default [Main §1.2, Remark (the measure as a realization datum)]",
  "The counting measure is a maximal-entropy default, not a derived prior.", "definition-used", "U",
  cited=["[Main §1.2, Remark (the measure as a realization datum)]"])
E(42, r"**$\mathsf S_K$**: all probability distributions on $\mathcal C_V^{K+1}$.",
  "S_K is the set of all probability distributions on C_V^{K+1}.", "definition-used", "U", cited=["[Main §3.4] (list heading, line 40)"])
E(43, (r"**$\mathsf D_K$**", "visible and hidden coordinates."),
  "D_K is the set of visible trajectory laws of a bijection of C_V × C_H, some finite C_H, with an initial law that may correlate visible and hidden coordinates.",
  "definition-used", "U", cited=["[Main §3.4] (list heading, line 40)"])
E(44, (r"**$\mathsf Q_K$**", "a fixed function of each outcome."),
  "Q_K is the set of laws of finite-dimensional unitary systems with projective Born measurement in one fixed basis at every step, initial state diagonal in that basis, record a fixed function of each outcome.",
  "definition-used", "U", cited=["[Main §3.4] (list heading, line 40)"])

# ---------------------------------------------------------------- §2.2
E(48, ("**Theorem 1**", r"on $\mathcal C_V^{K+1}$.*"), line_end=52,
  claim="Theorem 1: for every finite visible alphabet and finite horizon K, S_K = D_K = Q_K (= all probability laws on C_V^{K+1}).",
  typ="theorem-statement", level="K", cited=["[Main §3.4]"], hyp=["finite C_V (|C_V| ≥ 2, line 36)", "finite horizon K"],
  note="status from line 54 (machine-checked)", direction=THM1_DIR("K", ["[Main §3.4]"]))
E(54, "Theorem 1 is machine-checked as `finite_horizon_equivalence`",
  "Theorem 1 is machine-checked as finite_horizon_equivalence.", "status", "K", cited=["`finite_horizon_equivalence`"])
E(54, r"$\mathsf S_K\subseteq\mathsf D_K$ (`S_imp_D`)", "S_K ⊆ D_K is machine-checked as S_imp_D.", "status", "K", cited=["`S_imp_D`"])
E(54, r"$\mathsf D_K\subseteq\mathsf Q_K$ (`D_imp_Qfb`)", "D_K ⊆ Q_K is machine-checked as D_imp_Qfb.", "status", "K", cited=["`D_imp_Qfb`"])
E(54, r"$\mathsf Q_K\subseteq\mathsf S_K$ (`Qfb_imp_S`)", "Q_K ⊆ S_K is machine-checked as Qfb_imp_S.", "status", "K", cited=["`Qfb_imp_S`"])
E(54, "and the reverse inclusions as their compositions", "The reverse inclusions are machine-checked as compositions of the three.", "status", "K")
E(54, "no construction enters as a hypothesis", "No realization or representation construction enters Theorem 1 as a hypothesis.", "scope", "K")
E(56, ("For $\\mathsf S_K\\subseteq\\mathsf D_K$ the realization", "EGGH26, Prop. 13]"),
  "The S_K ⊆ D_K realization stores a sampled trajectory, with a clock, in the hidden register.", "result", "U",
  cited=["[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence)]", "[EGGH26, Prop. 13]"])
E(56, ("For a law with rational probabilities", "(finite-horizon process dilation)]"),
  "For rational-probability laws, a realization with hidden prior independent of x_0 exists.", "result", "P",
  cited=["[Main §3.4, Theorem (finite-horizon process dilation)]"], hyp=["rational probabilities"],
  note="'it is proved on paper, with exact probes' (same line)")
E(58, ("For $\\mathsf D_K\\subseteq\\mathsf Q_K$ the representation", "[Main §3.4]"),
  "The D_K ⊆ Q_K representation is the permutation unitary U_φ read out in the configuration basis at every step.", "result", "U", cited=["[Main §3.4]"])
E(58, r"$\mathsf Q_K\subseteq\mathsf S_K$ is the Born rule", "Q_K ⊆ S_K is the Born rule.", "result", "U")
E(60, "The trajectory-labelling realization is that of Egri et al. [EGGH26, Prop. 13], packaged as one iterated bijection",
  "The trajectory-labelling realization is Egri et al.'s Prop. 13, packaged as one iterated bijection.", "attribution", "U", cited=["[EGGH26, Prop. 13]"])
E(60, "the independent-prior form is their Prop. 16, without reversibility",
  "The independent-prior form is EGGH26 Prop. 16, which lacks reversibility.", "attribution", "U", cited=["[EGGH26] Prop. 16 ('their')"])
E(60, "its Markov one-step case is the random-mapping representation [LP17, Prop. 1.5]",
  "The Markov one-step case of the independent-prior form is the random-mapping representation.", "attribution", "U", cited=["[LP17, Prop. 1.5]"])
E(60, "A permutation dynamics is a special case of a unistochastic process [Bar25, p. 12; Bar23 §4.3; Bar26 §4]",
  "A permutation dynamics is a special case of a unistochastic process.", "attribution", "U", cited=["[Bar25, p. 12; Bar23 §4.3; Bar26 §4]"])
E(60, ("the one-step $n^2$-dimensional ancilla dilation", "[Sch21, Thm 2]"),
  "Main §3.1's one-step n²-dimensional ancilla dilation coincides with Barandes's and Schmidt's constructions.", "attribution", "U",
  cited=["[Main §3.1]", "[Bar26, Thm 3.3]", "[Sch21, Thm 2]"], note="'n' is not defined in the Introduction")
E(60, "The every-step projectively measured record as a probability law is in [SGD19, Eq. (3)]",
  "The every-step projectively measured record as a probability law appears in SGD19 Eq. (3).", "attribution", "U", cited=["[SGD19, Eq. (3)]"])
E(60, "that work and [Milz20] study whether such records are consistent with omitting measurements",
  "SGD19 and Milz20 study whether such records are consistent with omitting measurements.", "attribution", "U", cited=["[SGD19]", "[Milz20]"])
E(60, r"a question $\mathsf Q_K$, which measures at every step, does not meet",
  "Q_K, measuring at every step, does not meet the measurement-omission (classicality) question.", "scope", "U")

# ---------------------------------------------------------------- §2.3
E(64, "Markov laws lie in all three classes.", "Markov laws lie in S_K, D_K and Q_K.", "result", "U")
E(64, ("So neither a finite reversible realization", "not hypotheses)]"),
  "Neither a finite reversible realization nor a fixed-basis unitary representation distinguishes a law with memory from one without.",
  "negative", "U", cited=["[Main §3.4, Remark (the conditions are diagnostics, not hypotheses)]"])
E(66, r"The relation $p=|U|^2$ is part of the definition of $\mathsf Q_K$, not an output.",
  "p = |U|² is part of Q_K's definition, not an output.", "scope", "U")
E(66, "The unitaries supplied are permutations, with entries 0 and 1",
  "The unitaries supplied by the correspondence are permutations with entries 0 and 1.", "result", "U")
E(66, r"so the recovered table is the same for $|U|^p$ at every $p>0$",
  "The recovered transition table is the same for |U|^p at every p > 0.", "result", "U")
E(66, "The quadratic exponent is therefore not selected [Main §3.4; Bar26, Thm 3.1].",
  "The correspondence does not select the quadratic (Born) exponent.", "negative", "U", cited=["[Main §3.4; Bar26, Thm 3.1]"])
E(68, "A finite bijection has finite order $L$", "A finite bijection has finite order L.", "result", "U", cited=["[Main §3.4]" + SF])
E(68, "so one fixed realization has an $L$-periodic multi-time law", "One fixed realization has an L-periodic multi-time law.", "result", "U", cited=["[Main §3.4]" + SF])
E(68, "the correspondence holds per horizon", "The correspondence holds per horizon (not for all times at once).", "scope", "U", cited=["[Main §3.4]" + SF])
E(68, "a nonperiodic law has no exact all-time realization by one fixed finite substratum [Main §3.4]",
  "A nonperiodic law has no exact all-time realization by one fixed finite substratum.", "negative", "U", cited=["[Main §3.4]"])

# ---------------------------------------------------------------- §2.4
E(72, r"Write $M_t := I(X_{<t};X_{t+1}\mid X_t)$ for the conditional memory at time $t$.",
  "Conditional memory M_t := I(X_{<t}; X_{t+1} | X_t).", "definition-used", "U")
T2C = ["[Main §3.4] (Theorem 2 header)"]
T2NOTE = "line 80: machine-checked for a joint law of history, present and hidden state; identification with a realization's time-t law not machine-checked; written proof in Main"
T2HYP = ["faithful realization"]
E(76, r"*(a) $P(X_{t+1}\mid p,x)=(f_x)_\#\mu_p$;*",
  "Theorem 2(a): the next-step law after history p ending at x is the pushforward of the hidden posterior μ_p under f_x.",
  "theorem-statement", "P", cited=T2C, hyp=T2HYP, note=T2NOTE)
E(77, ("*(b) for histories", ";*"),
  "Theorem 2(b): TV distance between next-step laws of two histories ending at x is at most the TV distance between their hidden posteriors.",
  "theorem-statement", "P", cited=T2C, hyp=T2HYP, note=T2NOTE)
E(78, r"*(c) $M_t\le I(X_{<t};H_t\mid X_t)",
  "Theorem 2(c), first inequality: M_t ≤ I(X_{<t}; H_t | X_t).", "theorem-statement", "P", cited=T2C, hyp=T2HYP, note=T2NOTE)
E(78, r"\le\log_2|\mathcal C_H|$;*" if r"\le\log_2|\mathcal C_H|$;*" in L(78) else r"\le\log_2|\mathcal C_H|$",
  "Theorem 2(c), second inequality: I(X_{<t}; H_t | X_t) ≤ log₂|C_H|.", "theorem-statement", "P", cited=T2C, hyp=T2HYP, note=T2NOTE)
E(80, "(a)–(c) are machine-checked for a joint law of history, present and hidden state.",
  "Theorem 2(a)–(c) are machine-checked for a joint law of history, present and hidden state.", "status", "K",
  cited=["Appendix A: `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory`"])
E(80, "Their identification with a realization's time-$t$ law is not machine-checked.",
  "The identification of that joint law with a realization's time-t law is not machine-checked.", "status", "P")
E(80, "The written proof is in [Main §3.4, Theorem (unavoidable hidden predictive memory)]",
  "Theorem 2 has a written proof in Main §3.4.", "status", "P",
  cited=["[Main §3.4, Theorem (unavoidable hidden predictive memory)]", "[CT06] ('see also')"])
E(82, ("**Corollary**", "different pushforwards."),
  "Corollary: M_t > 0 iff every faithful realization carries readout-relevant hidden memory at t (two posteriors with different pushforwards).",
  "theorem-statement", "P", cited=["[Main §1.5]"],
  note="'proved on paper'; vanishing criterion and time-t identification not machine-checked",
  direction=D("equivalence ('exactly when')",
    ("⇒ (forward)", "If M_t > 0, every faithful realization has two hidden posteriors with different f_x-pushforwards at t.", "P",
     ["[Main §1.5]", "Theorem 2(a)", "[CT06]"], "rests on Theorem 2(a) in each realization and the CMI vanishing criterion"),
    ("⇐ (converse)", "If every faithful realization carries readout-relevant hidden memory at t, then M_t > 0.", "P",
     ["[Main §1.5]", "Theorem 2(a)", "`S_imp_D`", "[CT06]"],
     "rests on Theorem 2(a) in one realization, whose existence Theorem 1 supplies (S_imp_D), and the CMI vanishing criterion")),
  flag="Mapper: confirm Main §1.5 is the Corollary's location (Theorem 2 is cited to Main §3.4).")
E(82, ("both use the standard vanishing criterion", "is not machine-checked"),
  "Both Corollary directions use the CMI vanishing criterion, which (like the time-t identification) is not machine-checked.", "status", "P", cited=["[CT06]"])
E(84, ("A realization of a law whose conditional past–future information", "(machine-checked in the same form as Theorem 2)"),
  "A realization of a law whose conditional past–future information reaches I* needs |C_H| ≥ 2^{I*}.",
  "theorem-statement", "P", hyp=["faithful realization"],
  note="'machine-checked in the same form as Theorem 2', i.e. for a joint law; realization identification not machine-checked",
  cited=["Appendix A: `c3_necessity`, `card_hidden_ge_two_pow_Istar`"],
  flag="'conditional past–future information' is not defined in the Introduction (M_t? I(X_{<t};X_{>t}|X_t)?), and 'in the same form as Theorem 2' leaves the checked statement implicit. Mapper: pin down the quantity and the checked form.")
E(84, ("If two values of $X_{<k}$", "[Main §2.3; CT06]."),
  "If two histories with common present, each of joint probability ≥ p0, induce next-step laws at TV distance ≥ δ, then I(X_{<k}; X_{k+1} | X_k) ≥ p0 δ²/ln 2 bits (Pinsker).",
  "theorem-statement", "P", cited=["[Main §2.3; CT06]"], note="'proved on paper, with exact probes'")
E(86, ("[Main §1.3] names four conditions", "different next-step laws."),
  "Main §1.3 names four hidden-sector conditions: (C1) influence, (C2) persistence of records, (C3) capacity, (C4) history readback (two histories with the same present induce different next-step laws).",
  "definition-used", "U", cited=["[Main §1.3]"])
E(86, r"In a faithful realization (C4) coincides with $M_t>0$ by the vanishing criterion [CT06]",
  "In a faithful realization, (C4) holds iff M_t > 0.", "result", "U", cited=["[CT06]"],
  direction=D("equivalence ('coincides with')",
    ("(C4) ⇒ M_t>0", "Two positive-probability histories with the same present and different next-step laws give M_t > 0.", "U", ["[CT06]"], None),
    ("M_t>0 ⇒ (C4)", "M_t > 0 gives two histories with the same present and different next-step laws.", "U", ["[CT06]"], None)),
  flag="(C4) as defined on line 86 is a property of the visible law, so 'in a faithful realization' is idle here; line 96 also uses a realization clause ('routed readback'). Mapper: check which (C4) Main §1.3 defines and at which t.")
E(86, "the Corollary places it in the hidden state", "Via the Corollary, (C4) is carried in the hidden state of every faithful realization.", "result", "P")
E(86, "(C1) and (C3) follow from it", "(C1) influence follows from (C4).", "result", "U")
E(86, "(C1) and (C3) follow from it", "(C3) capacity follows from (C4).", "result", "U")
E(86, "(C2) is a physical-regime premise", "(C2) persistence of records is a physical-regime premise, not derived.", "status", "CJ",
  flag="§6.3 item (4) lists '(C2) necessity' as open and conditional on a mixing hypothesis; check the two statements agree with Main.")
E(86, "The conditions are diagnostics of a realization, not hypotheses of Theorem 1.",
  "(C1)–(C4) are diagnostics of a realization, not hypotheses of Theorem 1.", "scope", "U")

# ---------------------------------------------------------------- §2.5
E(90, (r"The family is *P-divisible on", r"$\Gamma_t=\Gamma_s\Lambda$."),
  "Rooted P-divisibility on {0..n}: for all s < t ≤ n some stochastic Λ has Γ_t = Γ_s Λ (Γ_t rooted at time 0, rows x_0).",
  "definition-used", "U",
  flag="This is a rooted (from time 0) divisibility; [RHP14]/[BD16] criteria are for two-time divisibility. Mapper: check the attribution on line 90 applies to the rooted form.")
E(90, "A stochastic divisor contracts total variation, so under P-divisibility", "Under P-divisibility, TV distance between rows of Γ_t cannot increase in t.", "result", "U")
E(90, "This is the divisibility criterion of [RHP14, Thm 2.4] and the data-processing direction of [BD16, Prop. 1].",
  "The TV-contraction criterion is RHP14 Thm 2.4 and the data-processing direction of BD16 Prop. 1.", "attribution", "U",
  cited=["[RHP14, Thm 2.4]", "[BD16, Prop. 1]"])
E(92, ("**Theorem 3**", "not P-divisible on $\\{0,\\dots,n\\}$.*"),
  "Theorem 3: for a bijection with fixed hidden prior, if two rows of Γ_s overlap in a column and Γ_n = I for some n > s, the family is not P-divisible on {0..n}.",
  "theorem-statement", "K", cited=["[Main §2.3]"],
  hyp=["bijection of C_V × C_H", "fixed hidden prior", "rows of Γ_s overlap", "Γ_n = I, n > s"],
  note="line 94: machine-checked in its rooted form",
  flag="'fixed hidden prior' is ambiguous (fixed in time? independent of x_0?). Mapper: match against the Lean hypothesis.")
E(94, "Theorem 3 is machine-checked in its rooted form", "Theorem 3 is machine-checked in rooted form.", "status", "K",
  cited=["Appendix A: `pIndivisible_of_rooted_identity_return_of_overlap`"])
E(94, "Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]",
  "Doukas states the same overlap-and-return argument concurrently.", "attribution", "U", cited=["[Dou26, Prop. 1]"])
E(94, "Monotone distance is necessary for P-divisibility", "Monotone TV distance is necessary for P-divisibility.", "result", "U", cited=["[Main §2.3]" + SF])
E(94, "but not sufficient [Main §2.3]", "Monotone TV distance is not sufficient for P-divisibility.", "negative", "U", cited=["[Main §2.3]"])
E(96, "A finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix [BB12, Problem 23] (machine-checked).",
  "A finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix.", "result", "K",
  cited=["[BB12, Problem 23]", "Appendix A: `isPermMatrix_of_stochastic_inverse`"])
E(96, ("With this lemma, on a fixed finite reversible substratum", "implies indivisibility)]"),
  "On a fixed finite reversible substratum, history readback (C4) forces indivisibility somewhere in the recurrence cycle.",
  "theorem-statement", "P", cited=["[Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]"],
  hyp=["fixed finite reversible substratum", "(C4) history readback"],
  note="machine-checked from routed-readback (C4); on paper from history-level (C4)")
E(96, ("The conclusion is machine-checked, by the route of Theorem 3", "the realization clause of (C4)]"),
  "The readback-forces-indivisibility conclusion is machine-checked, via Theorem 3, from routed-readback (C4).", "status", "K",
  cited=["[Main §1.3, the realization clause of (C4)]", "Appendix A: `routed_forces_indivisible_somewhere`"], hyp=["routed-readback (C4)"])
E(96, "from history-level (C4) it is proved on paper", "From history-level (C4), readback-forces-indivisibility is proved on paper.", "status", "P")
E(98, "a minimal model of Theorem 3 with six hidden states",
  "Appendix B.1 is a minimal model of Theorem 3 with six hidden states.", "result", "U",
  flag="'minimal model' (6 hidden states) sits beside 'the smallest realization of Theorem 3' (the card game, 2 hidden values). The sense of 'minimal' is unstated.")
E(98, "a two-card game, the smallest realization of Theorem 3",
  "The two-card game is the smallest realization of Theorem 3.", "result", "U",
  flag="Minimality claim with no proof or citation and no stated measure of size; check Main/Book.")

# ---------------------------------------------------------------- §3.1
E(104, "The indivisibility of §2.5 is global: it occurs somewhere in the recurrence cycle, not on every window.",
  "The §2.5 indivisibility occurs somewhere in the recurrence cycle, not on every window.", "scope", "U")
E(104, "Conditional memory does not force short-window indivisibility (Appendix B).",
  "Conditional memory does not force short-window indivisibility.", "negative", "U", cited=["(Appendix B)"])
E(106, ("Three notions are distinct, and no unconditional implication holds among them", "(three notions, kept apart)]"),
  "Accessible memory, P-indivisibility, and quantum non-Markovianity are distinct, with no unconditional implication among them.",
  "negative", "U", cited=["[Main §3.2, Remark (three notions, kept apart)]"],
  note="six directed implications are denied; 'unconditional' scope")
E(106, "Tracing out a permutation unitary from a diagonal hidden state gives channels that preserve diagonal states",
  "Tracing out a permutation unitary from a diagonal hidden state gives diagonal-preserving channels.", "result", "U",
  cited=["[Main §3.2, Theorem (CP-indivisibility, framework scope)]" + SF])
E(106, "and for them (2) implies CP-indivisibility [Main §3.2, Theorem (CP-indivisibility, framework scope)]",
  "For diagonal-preserving channel families, P-indivisibility of populations implies CP-indivisibility.", "theorem-statement", "U",
  cited=["[Main §3.2, Theorem (CP-indivisibility, framework scope)]"])
E(106, ("Outside that class the implication fails", "is not quantum non-Markovianity)]"),
  "Outside the diagonal-preserving class, P-indivisibility does not imply CP-indivisibility (Hadamard-then-identity family: CP-divisible, populations ½J → I P-indivisible).",
  "negative", "U", cited=["[Main §3.2, Remark (scope: P-indivisibility is not quantum non-Markovianity)]"])
E(106, "Distinguishability backflow witnesses divisibility failure in one direction only [BLP09]",
  "Distinguishability backflow implies divisibility failure but not conversely.", "attribution", "U", cited=["[BLP09]"])
E(106, ("for bijective dynamical maps on a $d$-dimensional system", "[BJA17]"),
  "For bijective dynamical maps on a d-dim system, CP-divisibility ⇔ monotone distinguishability with a (d+1)-dim ancilla.",
  "attribution", "U", cited=["[BJA17]"],
  direction=D("equivalence (literature)",
    ("⇒", "CP-divisible bijective dynamical maps give monotone distinguishability with a (d+1)-dimensional ancilla.", "U", ["[BJA17]"], None),
    ("⇐", "Monotone distinguishability with a (d+1)-dimensional ancilla implies CP-divisibility for bijective dynamical maps.", "U", ["[BJA17]"], None)))
E(108, ("Theorem 1 is a representation result", "(representation, not explanation)]"),
  "Theorem 1 states which laws admit realizations/representations, not why a physical system exhibits memory.", "scope", "U",
  cited=["[Main §3.4, Remark (representation, not explanation)]"])
E(108, ("Calvo states a proof of the six axioms", "[Cal26]"),
  "Calvo states a proof of textbook QM's six axioms from the single axiom of generally indivisible stochastic evolution.", "attribution", "U", cited=["[Cal26]"])
E(108, "Theorem 1 is a correspondence between classes of law and derives no such axioms.",
  "Theorem 1 derives no quantum axioms.", "negative", "U")

# ---------------------------------------------------------------- §3.2
E(112, ("Operational quantum mechanics requires", "one instrument theory."),
  "Operational QM requires coherent preparations, noncommuting interventions and composites in one instrument theory, beyond fixed-basis statistics.",
  "scope", "U")
E(114, ("Fix a nonempty finite system and an operational theory", "[GR §3.3]."),
  "Standing structure for Theorem 4: identity, coarse-graining and outcome-conditioned composition closure, uniformly mixed ancilla preparation, spectator-independent local ancilla readout, and ancilla discard.",
  "definition-used", "U", cited=["[GR §3.3]"])
E(114, ("The five conditions are:", "gives an available operation."),
  "Conditions (i) positivity/trace, (ii) one-state ancilla, (iii) untouched independent system, (iv) all finite unitaries on composites, (v) fresh uniformly prepared ancilla attach-act-discard.",
  "definition-used", "U", cited=["[GR §3.3]" + " (preceding sentence)"])
E(116, ("**Theorem 4**", "conditions (i)–(v) hold.*"),
  "Theorem 4: for every nonempty finite system, available families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments iff (i)–(v) hold.",
  "theorem-statement", "K", cited=["[GR §3.3]"], hyp=["standing structure of line 114", "nonempty finite system"],
  note="line 118: both directions machine-checked",
  direction=D("equivalence (iff)",
    ("⇒", "Exactly Kraus instruments at every level ⇒ conditions (i)–(v).", "K", ["[GR §3.3]", "`physical_of_exactAll`"], None),
    ("⇐", "Conditions (i)–(v) ⇒ exactly Kraus instruments at every level.", "K", ["[GR §3.3]", "`exactAll_of_physical_general`"], None)),
  flag="Line 114 says 'at every ancilla level'; Theorem 4 says 'at every positive ancilla level'. Mapper: check which the Lean statement uses.")
E(118, r"Both directions are machine-checked, $\Rightarrow$ as `physical_of_exactAll`",
  "Theorem 4 ⇒ is machine-checked as physical_of_exactAll.", "status", "K", cited=["`physical_of_exactAll`"],
  flag="Appendix A places physical_of_exactAll in PhysicalCharacterization, not GeneralCarrier; check it holds 'for every nonempty finite carrier' as line 118 states.")
E(118, r"and $\Leftarrow$ as `exactAll_of_physical_general`, for every nonempty finite carrier",
  "Theorem 4 ⇐ is machine-checked as exactAll_of_physical_general for every nonempty finite carrier.", "status", "K",
  cited=["`exactAll_of_physical_general`"])
E(120, "On the qubit, each condition is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4).",
  "On the qubit, each of (i)–(v) is independent of the other four and of a fixed finite observation process satisfying (C1)–(C4).",
  "result", "K", cited=["[GR §3.3]" + " (end of paragraph)", "Appendix A: `five_way_minimality`"],
  note="body sentence carries no status; Appendix A lists it as machine-checked")
E(120, "For each condition there is a qubit theory that realizes that process and the other four conditions, and fails it.",
  "For each condition, some qubit theory realizes the observation process and the other four conditions but fails it.", "result", "K",
  cited=["Appendix A: `five_way_minimality`"])
E(120, "In particular, a qubit theory that never creates coherence realizes the observation process and is not quantum.",
  "A qubit theory that never creates coherence realizes the observation process and is not quantum.", "result", "K",
  cited=["Appendix A: `oi_alone_not_qm`"])
E(120, "So OI alone does not imply quantum mechanics.", "OI alone does not imply quantum mechanics.", "negative", "K",
  cited=["Appendix A: `oi_alone_not_qm`"],
  note="non-implication by qubit witness; 'OI' here = a fixed finite observation process satisfying (C1)–(C4)")
E(120, "Which of (iii)–(v) a physical substratum supplies is open [GR §3.3].",
  "Which of (iii)–(v) a physical substratum supplies is open.", "status", "O", cited=["[GR §3.3]"],
  flag="Implicitly treats (i) and (ii) as supplied or not at issue; the Introduction gives no statement or citation for that.")

# ---------------------------------------------------------------- §3.3
E(122, "The evolution relating two times is not selected", "The evolution relating two times is not selected (heading).", "negative", "U")
E(124, ("Representability does not fix the unitary evolution relating two times", "relating evolution)]."),
  "Representability does not fix the unitary evolution relating two times.", "negative", "U",
  cited=["[Main §3.4, Remark (scope: representability, not selection of the relating evolution)]"])
E(124, ("Two coherent lifts of one visible family", "have different relating evolutions"),
  "Two coherent lifts of one visible family can differ by a time-dependent right action invisible to the visible law and have different relating evolutions.",
  "result", "K", cited=["Appendix A: `gl2_strong_gauge_moves_relative_candidate`"], note="'(both machine-checked)'")
E(124, "while a constant deformation cancels from every relating evolution (both machine-checked)",
  "A constant deformation cancels from every relating evolution.", "result", "K",
  cited=["Appendix A: `gl3_constant_gauge_preserves_relative`"])
E(126, "Take a lift with trivial ancilla at one time, and form the fixed-basis datum whose evolution is the lift's unitary, with uniform initial law and identity readout.",
  "Setting for the bridge results: fixed-basis datum from a lift with trivial ancilla at one time, uniform initial law, identity readout.",
  "definition-used", "U")
E(126, "If two such data have the same one-step visible matrix, their root-conditioned trajectory laws agree at every horizon (`bridge_traj`)",
  "Same one-step visible matrix ⇒ same root-conditioned trajectory laws at every horizon.", "result", "K", cited=["`bridge_traj`"])
E(126, "conversely, if their rooted families agree, their one-step visible matrices are equal (`rooted_eq_iff_slice_eq`, forward direction)",
  "Equal rooted families ⇒ equal one-step visible matrices.", "result", "K", cited=["`rooted_eq_iff_slice_eq` (forward direction)"],
  direction=D("converse pair presented with the preceding entry ('conversely')",
    ("one-step ⇒ trajectory laws", "Same one-step visible matrix ⇒ same root-conditioned trajectory laws at every horizon.", "K", ["`bridge_traj`"], None),
    ("rooted family ⇒ one-step", "Same rooted family ⇒ same one-step visible matrix.", "K", ["`rooted_eq_iff_slice_eq` (forward direction)"], None)),
  flag="§A.34: the 'converse' has a different middle term (rooted families vs root-conditioned trajectory laws at every horizon), so the two cited results do not form an iff unless the mapper shows the two notions coincide. Also only the forward direction of an iff declaration is cited.")
E(126, "Each such trajectory law is fixed-basis realizable", "Each such trajectory law is fixed-basis realizable.", "result", "K",
  cited=["`realData_traj_stochastic`"],
  flag="The declaration name suggests stochasticity only; check it also establishes fixed-basis realizability.")
E(126, "and stochastic (`realData_traj_stochastic`)", "Each such trajectory law is stochastic.", "result", "K", cited=["`realData_traj_stochastic`"])
E(126, "The fixed-basis correspondence therefore acts on the quotient by visible equality.",
  "The fixed-basis correspondence acts on the quotient by visible equality.", "result", "U")
E(126, "A selection condition beyond representability and ordinary coherence would be needed",
  "Selecting the relating evolution would require a condition beyond representability and ordinary coherence.", "result", "U")
E(126, "and none is supplied here", "No such selection condition is supplied.", "status", "O")

# ---------------------------------------------------------------- §3.4
E(128, "No fixed finite carrier reproduces a qubit", "No fixed finite carrier reproduces a qubit (heading).", "negative", "C",
  hyp=["imported unboundedness [GH03; Mon08; Har04; HKLP24]"],
  flag="Heading is broader than the body ('the full prepare-and-measure theory of a qubit exactly'); 'carrier' is also used for Theorem 4's system ('every nonempty finite carrier', line 118).")
E(130, "A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states.",
  "A fixed finite realization with N ontic configurations yields only behaviour matrices with nonnegative factorization through N states.",
  "result", "P", note="'the factorization is proved' (same line)")
E(130, "Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments",
  "Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments.", "result", "U",
  note="imported ('the unboundedness is imported')")
E(130, "explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08]",
  "Galvão–Hardy and Montina give explicit tasks showing unbounded classical memory.", "attribution", "U", cited=["[GH03]", "[Mon08]"])
E(130, "Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]",
  "Montina reports Hardy's result that the number of ontic states cannot be finite.", "attribution", "U", cited=["[Mon08; Har04]"],
  note="[Har04] reference carries a VERIFY comment: content not read, cited as reported in [Mon08]")
E(130, "So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly",
  "No fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly.", "negative", "C",
  hyp=["imported unboundedness"],
  cited=["[Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form); HKLP24, Thm 4]" + SF])
E(130, ("the factorization is proved, and the unboundedness is imported", "HKLP24, Thm 4]"),
  "The factorization step is proved; the unboundedness step is imported.", "status", "P",
  cited=["[Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]", "[HKLP24, Thm 4]"])
E(130, "The obstruction does not touch Theorem 1, whose realization is chosen per law.",
  "The finite-carrier obstruction does not affect Theorem 1, whose realization is chosen per law.", "scope", "U")

# ---------------------------------------------------------------- §3.5
E(134, ("The origin of the quadratic Born exponent", "is open [Main §3.4; Bar26, Thm 3.1]."),
  "The origin of the quadratic Born exponent is open.", "status", "O", cited=["[Main §3.4; Bar26, Thm 3.1]"])
E(136, ("A deterministic completion that keeps pointwise causal cones", "[Bel64; CHSH69; Main §3.3]"),
  "A deterministic completion with pointwise causal cones and a setting-independent ensemble satisfies |S_CHSH| ≤ 2.", "result", "U",
  cited=["[Bel64; CHSH69; Main §3.3]"])
E(136, "so a deterministic completion reproducing quantum Bell correlations must give up one of the two",
  "A deterministic completion reproducing quantum Bell correlations must give up pointwise causal cones or measurement independence.", "result", "U")
E(136, ("The framework keeps measurement independence and adopts ontic parameter dependence", "without operational signalling"),
  "The framework keeps measurement independence and adopts ontic parameter dependence (remote-setting-dependent microstate response, no operational signalling).",
  "scope", "CJ", hyp=["H-Bell"], note="framework posit")
E(136, ("the compatibility of that choice with operational no-signalling", "is the open hypothesis H-Bell [Main §3.3]"),
  "Compatibility of ontic parameter dependence with operational no-signalling and the gravitational continuum limit of the spatial coupling graph is the open hypothesis H-Bell.",
  "status", "O", cited=["[Main §3.3]"], hyp=["H-Bell"])

# ---------------------------------------------------------------- §4
E(140, ("Summing zero-point energies", "Eqs. (3.4)–(3.6)]"),
  "Summing zero-point energies to a Planck cutoff gives a vacuum energy density ~120 orders of magnitude above the observed value.",
  "numerical", "U", cited=["[Wei89, §I; §III, Eqs. (3.4)–(3.6)]"])
E(140, "the exact power depending on the cutoff convention", "The exact power of the mismatch depends on the cutoff convention.", "scope", "U")
E(140, "if that density sources curvature, it must be cancelled to that accuracy [Wei89, §III]",
  "If the zero-point density sources curvature, it must be cancelled to ~120 orders.", "attribution", "U", cited=["[Wei89, §III]"])
E(142, "In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and the effective cosmological constant are defined at different levels of description.",
  "In OI the zero-point sum (emergent description) and the effective cosmological constant are defined at different levels.", "result", "U")
E(142, "A uniform shift of the emergent Hamiltonian changes no visible transition probability",
  "A uniform shift of the emergent Hamiltonian changes no visible transition probability.", "result", "U", cited=["[GR §6.2]" + SF])
E(142, "so the offset has no content in the visible statistics of the quantum description [GR §6.2]",
  "The zero-point offset has no content in the visible statistics.", "result", "U", cited=["[GR §6.2]"])
E(142, "The invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum energy",
  "No non-gravitational measurement sees the absolute vacuum energy (standard).", "attribution", "U", note="no citation given")
E(142, "OI's proposal is that the mismatch requires no cancellation",
  "OI proposes that the vacuum-energy mismatch requires no cancellation.", "status", "CJ",
  hyp=["covariant field equations (open; line 144)"], note="'proposal'; line 144 makes it conditional")
E(142, "and its content lies in how the two levels couple to geometry",
  "The proposal's content lies in how the two levels couple to geometry.", "scope", "U")
E(144, "Whether the offset also fails to source curvature is a separate coupling question.",
  "Whether the offset fails to source curvature is a separate coupling question.", "scope", "U")
E(144, "Settling it requires covariant field equations derived from the substratum, with their coupling to sources (Level G3 of [GR])",
  "Settling the coupling question requires covariant field equations derived from the substratum, with source coupling (GR Level G3).",
  "scope", "U", cited=["Level G3 of [GR]", "[GR §6.2]" + SF])
E(144, "which are open [GR §6.2]", "The covariant field equations with source coupling (GR Level G3) are open.", "status", "O", cited=["[GR §6.2]"])
E(144, (r"The quantum description therefore does not decide between gravitational completions", "[GR §6.2]."),
  "The quantum description does not decide between gravitational completions differing by ρ_C g_μν.", "negative", "U", cited=["[GR §6.2]"])
E(144, "The proposal that the mismatch requires no cancellation is therefore conditional on that open step.",
  "The no-cancellation proposal is conditional on the open field-equation step.", "status", "C", hyp=["covariant field equations with source coupling"])
E(146, ("the form [GR] targets", r"\mathcal F[g,T]\,g_{\mu\nu})$"),
  "GR targets field equations E_μν[g,OI] = 8πG(T_μν − F[g,T] g_μν) with the substratum's classical stress-energy as source.", "scope", "U", cited=["[GR]"])
E(146, "the zero-point sum of the emergent description is not a source and needs no cancellation",
  "If the field equations take GR's target form, the zero-point sum is not a source and needs no cancellation.", "result", "C",
  hyp=["field equations of GR's target form", "classical substratum stress-energy as source"])
E(146, r"the vacuum term that remains, from the substratum's classical energy density and from $\mathcal F$, is not computed",
  "The remaining vacuum term (substratum classical energy density and F) is not computed.", "status", "O")
E(146, "It does not explain the observed value of Λ", "The proposal does not explain the observed value of Λ.", "negative", "U")
E(146, "which enters as a cosmological input", "The observed value of Λ enters as a cosmological input.", "status", "CAL")
E(146, r"The scale $\rho\sim H_{\rm Hub}^2/G$, with $H_{\rm Hub}$ the Hubble rate, is the Friedmann normalization of the total density",
  "The scale ρ ~ H²/G is the Friedmann normalization of the total density.", "result", "U")
E(146, "and the fraction carried by Λ is an input", "The fraction of the density carried by Λ is an input.", "status", "CAL")
E(148, "With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff convention",
  "With a Planck cutoff, the mismatch equals the de Sitter entropy up to a cutoff-convention factor.", "numerical", "CAL")
E(148, "this is a dimensional identity, not an independent prediction",
  "The mismatch–de Sitter entropy relation is a dimensional identity, not an independent prediction.", "status", "CAL")
E(148, "How the energy of electroweak and QCD vacuum transitions couples to gravity is not fixed by the descriptive distinction",
  "The descriptive distinction does not fix how electroweak/QCD vacuum-transition energy couples to gravity.", "negative", "U")
E(148, "and requires the same open coupling step", "The coupling of vacuum-transition energy requires the same open coupling step.", "status", "O")
E(150, "Removing the vacuum energy of matter as a source of curvature is also the aim of the trace-free Einstein equations",
  "Trace-free Einstein equations aim to remove matter vacuum energy as a curvature source.", "attribution", "U", cited=["[EvEMU11]" + SF])
E(150, "which leave the observed value of Λ unexplained [EvEMU11]", "Trace-free Einstein equations leave the observed Λ unexplained.", "attribution", "U", cited=["[EvEMU11]"])
E(150, "and of vacuum-energy sequestering", "Vacuum-energy sequestering aims to remove matter vacuum energy as a curvature source.", "attribution", "U", cited=["[KP14]" + SF])
E(150, "which also renders contributions from phase transitions small [KP14]", "Sequestering renders phase-transition contributions small.", "attribution", "U", cited=["[KP14]"])
E(150, ("Volovik argues", "[Vol06]"),
  "Volovik argues from quantum many-body ground-state thermodynamics that the UV zero-point sum does not set the vacuum energy.", "attribution", "U", cited=["[Vol06]"])
E(150, "The present proposal differs in locating the gravitational source in the substratum microstate",
  "The OI proposal differs from these by locating the gravitational source in the substratum microstate.", "scope", "U")
E(150, "and its coupling step is open", "The OI proposal's coupling step is open.", "status", "O")
E(152, "A derivation of the covariant field equations, with their conservation and source coupling, from the substratum would turn the proposal into a theorem or refute it.",
  "Deriving covariant field equations (conservation, source coupling) from the substratum would decide the proposal.", "scope", "U")
E(152, "Until then the proposal reinterprets the problem and does not resolve it.",
  "The proposal reinterprets the cosmological constant problem and does not resolve it.", "negative", "O")

# ---------------------------------------------------------------- §5
E(156, "The black-hole information problem asks whether the radiation of an evaporating black hole carries the information of what formed it [Haw76; Pag93; Pag13].",
  "The BH information problem asks whether evaporating-BH radiation carries the information of what formed it.", "attribution", "U", cited=["[Haw76; Pag93; Pag13]"])
E(156, ("Because the dynamics of OI is a bijection observed through a partition", "its *access class*"),
  "Since OI dynamics is a bijection observed through a partition, global conservation and accessible recovery are separate questions.", "scope", "U")
E(156, "The results below are finite computations in toy models of configurations, permutations and configuration reads.",
  "The §5 results are finite computations in toy models of configurations, permutations and configuration reads.", "scope", "N")
E(156, "They concern the framework's nested-partition construction [GR App. A; Book §7.6], not a particular black hole.",
  "The §5 results concern the framework's nested-partition construction, not a particular black hole.", "scope", "U", cited=["[GR App. A; Book §7.6]"])
E(158, "Under OI, information is conserved in the global reversible dynamics because the dynamics is a bijection, which is a premise of the framework.",
  "Under OI, information is conserved globally because the dynamics is a bijection (a premise).", "result", "C", hyp=["bijective dynamics (framework premise)"])
E(158, "Conservation neither implies", "Global conservation does not imply recovery from accessible records.", "negative", "N", cited=["[BHa]" + SF])
E(158, "nor is necessary for recovery from the records an observer can access",
  "Global conservation is not necessary for recovery from accessible records.", "negative", "N", cited=["[BHa]" + SF])
E(158, "finite exhaustive computations exhibit bijections with no accessible advantage, that is, no gain in success probability over a blind guess",
  "Exhaustive finite computations exhibit bijections with zero accessible advantage over a blind guess.", "numerical", "N", cited=["[BHa]" + SF])
E(158, "and non-injective maps with exact recovery [BHa]", "Exhaustive finite computations exhibit non-injective maps with exact recovery.", "numerical", "N", cited=["[BHa]"])
E(160, r"Of the 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage for a binary message with one register unread after two emissions.",
  "Of the 40,320 bijections of {0,1}³, 1,376 give zero accessible advantage (binary message, one register unread, two emissions).",
  "numerical", "N", cited=["[BHa] (end of next sentence)"], note="40,320 = 8!")
E(160, "For bijective dynamics, complete endpoint access gives exact recovery",
  "For bijective dynamics, complete endpoint access gives exact recovery.", "result", "U", cited=["[BHa]" + SF])
E(160, r"with $\mathcal U$ inaccessible $P_{\mathrm{succ}}\ge1/|\mathcal U|$",
  "For bijective dynamics with the unread registers U inaccessible, P_succ ≥ 1/|U|.", "result", "U", cited=["[BHa]" + SF])
E(160, r"so zero advantage in a bijective instance requires $|\mathcal U|\ge|\mathcal M|$",
  "Zero accessible advantage in a bijective instance requires |U| ≥ |M|.", "result", "U", cited=["[BHa]" + SF],
  flag="Derivation needs the blind-guess baseline 1/|M| (uniform message prior); the prior is not stated in the Introduction.")
E(160, r"32 non-injective maps of $\{0,1\}^2$ violate the bound on $P_{\mathrm{succ}}$ [BHa]",
  "32 non-injective maps of {0,1}² violate the P_succ ≥ 1/|U| bound.", "numerical", "N", cited=["[BHa]"],
  flag="Population counted (maps {0,1}²→{0,1}²? which register unread?) is unspecified.")
E(160, "These endpoint guarantees are sufficient, not necessary.", "The endpoint guarantees are sufficient conditions, not necessary ones.", "scope", "U",
  flag="Ambiguous: sufficient/necessary for what (recovery? the bound?) is not stated.")
E(160, "The bound is the remnant-capacity form of a known fact", "The P_succ bound is the remnant-capacity form of a known fact.", "attribution", "U", cited=["[BHa; Sha79]" + SF])
E(160, "and its linear case is the secret-sharing threshold [BHa; Sha79]", "The bound's linear case is the secret-sharing threshold.", "attribution", "U",
  cited=["[BHa; Sha79]"], note="[Sha79] reference carries a VERIFY comment: content not read")
E(162, "The Page-curve calculation of [GR App. A] addresses recovery under its own conditions and is a conditional result [Book §7.6, §18.5].",
  "GR App. A's Page-curve calculation is a conditional result.", "status", "C", cited=["[GR App. A]", "[Book §7.6, §18.5]"])
E(162, ("Its configuration space is", "[GR App. A.1, A.7]."),
  "The Page-curve configuration space is C_V × C_B × C_D (exterior, interior, beyond the cosmological horizon); the radiation R ⊂ V is emitted from B.",
  "definition-used", "U", cited=["[GR App. A.1, A.7]"])
E(162, ("For all but an exponentially negligible fraction of initial conditions", "Thms A.8–A.9]."),
  "For all but an exponentially negligible fraction of initial conditions, the full-cycle time-averaged radiation entanglement entropy at fixed bipartition equals S_Page(d_B,d_R) up to Theorem A.8's correction.",
  "theorem-statement", "C", cited=["[Pag93; GR, Thms A.8–A.9]"], hyp=["H-scramble", "H-decouple", "single energy shell C_B × C_R"])
E(162, "This holds under the scrambling hypothesis H-scramble, that the orbit ensemble equidistributes over quantum pure states on the shell",
  "The Page-value result holds under H-scramble (orbit ensemble equidistributes over pure states on the shell).", "status", "C", hyp=["H-scramble"])
E(162, "H-scramble fails for every bijection acting on a definite initial configuration with the bipartition aligned to the configuration coordinates",
  "H-scramble fails for every bijection acting on a definite initial configuration with configuration-aligned bipartition.", "negative", "U",
  cited=["[GR App. A.7; BHb, C1, C6(a)–(b)]" + SF],
  flag="Universal 'for every bijection' claim attributed to an unpublished record; check whether BHb C1 proves it or checks it finitely.")
E(162, "and is not established [GR App. A.7; BHb, C1, C6(a)–(b)]", "H-scramble is not established.", "status", "O", cited=["[GR App. A.7; BHb, C1, C6(a)–(b)]"])
E(162, ("It also needs the decoupling condition H-decouple", "over whole cycles of the dynamics"),
  "The Page-value result also needs H-decouple: B ∪ R uncoupled from D and V∖R, jointly pure, over whole cycles.", "status", "C", hyp=["H-decouple"])
E(162, "timescale ordering does not supply it [BHa, item F]", "Timescale ordering does not supply H-decouple.", "negative", "U", cited=["[BHa, item F]"])
E(162, "and it is not established [GR App. A.7]", "H-decouple is not established.", "status", "O", cited=["[GR App. A.7]"])
E(162, r"Theorem A.8 of [GR] takes the whole configuration space $\mathcal C_B\times\mathcal C_R$ as a single energy shell.",
  "GR Theorem A.8 takes all of C_B × C_R as a single energy shell.", "scope", "U", cited=["Theorem A.8 of [GR]"])
E(162, "That requires the energy to be constant there, so that energy conservation places no constraint on the orbit",
  "A single shell requires constant energy on C_B × C_R, so conservation does not constrain the orbit.", "scope", "U")
E(162, "and it does not follow from the conservation of a Hamiltonian that takes more than one value there",
  "The single-shell assumption does not follow from conservation of a Hamiltonian taking more than one value there.", "negative", "U")
E(162, "An evaporating black hole whose radiation carries away its energy is in the proper-shell case",
  "An evaporating BH whose radiation carries away its energy is in the proper-shell case.", "result", "U", cited=["[GR App. A.7; BHb, C6(c)]" + SF])
E(162, "where the mean entropy depends on the shell and in general differs from the Page value",
  "On a proper shell the mean entropy depends on the shell and in general differs from the Page value.", "result", "U", cited=["[GR App. A.7; BHb, C6(c)]" + SF])
E(162, "that case is open [GR App. A.7; BHb, C6(c)]", "The proper-shell case is open.", "status", "O", cited=["[GR App. A.7; BHb, C6(c)]"])
E(162, "The result is a time average at a fixed bipartition", "The Page-value result is a time average at a fixed bipartition.", "scope", "U")
E(162, "whether the entropy along a single trajectory follows the same curve is open [GR App. A.7; BHb, C6(d)]",
  "Whether single-trajectory entropy follows the Page curve is open.", "status", "O", cited=["[GR App. A.7; BHb, C6(d)]"])
E(162, "In the dependency ladder of [GR] the Page curve is also conditional on the covariant field equations.",
  "In GR's dependency ladder the Page curve is conditional on the covariant field equations.", "status", "C", hyp=["covariant field equations"], cited=["[GR]"])
E(162, "The generalized second law is not derived [GR App. A.6]", "The generalized second law is not derived.", "status", "O", cited=["[GR App. A.6]"])
E(162, "agreement with quantum-extremal-surface computations [Pen20] is not established",
  "Agreement with quantum-extremal-surface computations is not established.", "status", "O", cited=["[Pen20]"])
E(162, "the correspondence between islands and substratum cycles is conjectural [Book §7.6]",
  "The islands ↔ substratum-cycles correspondence is conjectural.", "status", "CJ", cited=["[Book §7.6]"])
E(162, "The Page curve of [GR App. A] is therefore not established", "The Page curve of GR App. A is not established.", "status", "O", cited=["[GR App. A]"])
E(162, "and the black-hole information problem is not resolved here", "The BH information problem is not resolved.", "negative", "O")

# ---------------------------------------------------------------- §6.1
E(168, "If the hypothesis holds, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer",
  "If OI holds, quantum fixed-basis statistics are the visible laws of an embedded observer.", "result", "C", hyp=[OI_HYP])
E(168, "and their departures from Markov behaviour are memory carried in an inaccessible sector",
  "If OI holds, departures from Markov behaviour are memory carried in an inaccessible sector.", "result", "C", hyp=[OI_HYP])
E(168, "whether the rest of operational quantum mechanics follows depends on completion conditions that OI does not imply (§3.2)",
  "The rest of operational QM depends on completion conditions OI does not imply.", "negative", "U")
E(168, "Quantum Bell correlations are not accounted for by memory alone",
  "Memory alone does not account for quantum Bell correlations.", "negative", "U")
E(168, "with measurement independence kept, they need ontic parameter dependence",
  "With measurement independence kept, quantum Bell correlations need ontic parameter dependence.", "result", "U")
E(168, "whose compatibility with operational no-signalling and the continuum limit is the open hypothesis H-Bell (§3.5)",
  "Compatibility of ontic parameter dependence with no-signalling and the continuum limit is the open hypothesis H-Bell.", "status", "O", hyp=["H-Bell"])

# ---------------------------------------------------------------- §6.2
E(172, "No derivation of quantum mechanics", "The paper does not derive quantum mechanics.", "negative", "U")
E(172, "Theorem 1 contains every finite law", "Theorem 1's classes contain every finite law.", "result", "U")
E(172, "and the Born exponent is not selected", "The Born exponent is not selected.", "negative", "U")
E(173, "No unique selection of the operational theory", "The operational theory is not uniquely selected.", "negative", "U")
E(173, "conditions (i)–(v) are not implied by OI alone", "Conditions (i)–(v) are not implied by OI alone.", "negative", "U")
E(173, "their independence is shown on the qubit", "Independence of (i)–(v) is shown on the qubit.", "result", "U")
E(173, "which of (iii)–(v) a physical substratum supplies is open", "Which of (iii)–(v) a physical substratum supplies is open.", "status", "O")
E(173, "the visible law does not fix the relating evolution", "The visible law does not fix the relating evolution.", "negative", "U")
E(174, "No characterization of memory by the existence of a realization (§2.3)",
  "Memory is not characterized by existence of a realization.", "negative", "U")
E(174, "no identification of P-indivisibility with quantum non-Markovianity",
  "P-indivisibility is not identified with quantum non-Markovianity.", "negative", "U")
E(174, "no claim that memory forces indivisibility on short windows (§3.1)",
  "No claim that memory forces short-window indivisibility.", "negative", "U")
E(175, "No resolution of the black-hole information problem", "No resolution of the BH information problem.", "negative", "O")
E(175, "the Page curve of [GR App. A] is not established (§5)", "The GR App. A Page curve is not established.", "status", "O", cited=["[GR App. A]"])
E(175, ("the results of §5 reported from [BHa; BHb] concern finite toy models", "or by exact arithmetic"),
  "The §5 results from BHa/BHb concern finite toy models, each proved on paper or checked exhaustively or by exact arithmetic.",
  "status", "P", cited=["[BHa; BHb]"], note="mixed proved-paper / numerical per result")
E(175, "No claim is made that information reaches $D$", "No claim that information reaches D.", "scope", "U")
E(175, "that [GR, Thm A.7] fails within its stated scope", "No claim that GR Thm A.7 fails within its stated scope.", "scope", "U", cited=["[GR, Thm A.7]"],
  flag="Cites GR Thm A.7, while the Page-value result is cited as GR Thms A.8–A.9 (line 162). Mapper: identify GR Thm A.7 (decoupling?) and confirm the intended theorem.")
E(175, "or that no other decoupling argument exists", "No claim that no other decoupling argument exists.", "scope", "U")
E(176, "No claim that the physical hypothesis is established or tested.", "The OI hypothesis is neither established nor tested.", "status", "O")
E(177, "No claim that the card game (Appendix B) produces quantum rather than classical statistics",
  "No claim that the card game produces quantum statistics.", "scope", "U")
E(177, "on card inputs its statistics are classical stochastic ones", "On card inputs the card game's statistics are classical stochastic.", "result", "U")
E(177, "under the unitary embedding its one-step channel is entanglement-breaking", "Under the unitary embedding, the card game's one-step channel is entanglement-breaking.", "result", "U")
E(177, "its two-step family admits a classical-memory decomposition", "The card game's two-step family admits a classical-memory decomposition.", "result", "U")
E(177, "it violates no Bell inequality", "The card game violates no Bell inequality.", "negative", "U")
E(178, r"No prediction of the value of Λ or $\Omega_\Lambda$", "No prediction of Λ or Ω_Λ.", "negative", "U")
E(178, "no resolution of the cosmological constant problem", "No resolution of the cosmological constant problem.", "negative", "O")
E(178, "§4 is conditional on the covariant field equations", "§4 is conditional on the covariant field equations.", "status", "C", hyp=["covariant field equations"])
E(179, "No claim that the viewpoint is new", "No claim that the viewpoint is new.", "scope", "U")
E(179, "deterministic systems analysed with quantum methods have been studied before, for example in [tH14]",
  "Deterministic systems analysed with quantum methods have been studied before (e.g. 't Hooft).", "attribution", "U", cited=["[tH14]"])
E(179, "What the paper states are the cited theorems and their scopes.", "Everything the paper states is a cited theorem with its scope.", "scope", "U")

# ---------------------------------------------------------------- §6.3
E(183, "whether a physical substratum supplies completion conditions (iii)–(v)", "Whether a physical substratum supplies (iii)–(v) is an open decisive test.", "status", "O")
E(183, "whether history readback (C4) holds at the cosmological partition [GR §2.2]", "Whether (C4) holds at the cosmological partition is open.", "status", "O", cited=["[GR §2.2]"])
E(183, "no experiment distinguishing OI from standard quantum theory", "No experiment distinguishing OI from standard QM is established.", "status", "O", cited=["[Main §4.5]" + SF])
E(183, "and no memory-witness constraint, is established [Main §4.5]", "No memory-witness constraint is established.", "status", "O", cited=["[Main §4.5]"])
E(183, "For the cosmological constant: a derivation of the covariant field equations with their source coupling.",
  "The decisive open test for the cosmological constant is deriving covariant field equations with source coupling.", "status", "O")
E(183, "whether H-scramble and H-decouple hold", "Whether H-scramble and H-decouple hold is open.", "status", "O", hyp=["H-scramble", "H-decouple"])
E(183, "the Page value on a proper energy shell and along a single trajectory", "The Page value on a proper shell and along a single trajectory is open.", "status", "O")
E(183, "and, in [GR]'s ladder, the covariant field equations", "In GR's ladder the covariant field equations are an open test for BH information.", "status", "O", cited=["[GR]"])
E(185, "(1) machine checks of the steps of §2.2, §2.4 and §2.5 that lack one", "Machine checks of the unchecked steps of §2.2, §2.4, §2.5 are open.", "status", "O")
E(185, "(2) whether the minimal hidden predictive memory equals $M_t$ once ledger bits that cannot influence the future are quotiented",
  "Whether minimal hidden predictive memory equals M_t after quotienting non-influencing ledger bits is open.", "status", "O", cited=["[Main §3.4]" + SF])
E(185, "(the fixed-dimension form is false)", "The fixed-dimension form of the minimal-memory = M_t statement is false.", "negative", "U", cited=["[Main §3.4]" + SF])
E(185, "(3) exact gluing for recurrent target families", "Exact gluing for recurrent target families is open.", "status", "O", cited=["[Main §3.4]" + SF])
E(185, "and approximation on windows short compared with the recurrence time [Main §3.4]",
  "Approximation on windows short compared with the recurrence time is open.", "status", "O", cited=["[Main §3.4]"])
E(185, "(4) (C2) necessity", "(C2) necessity is open.", "status", "O", cited=["[Main §3.4]" + SF])
E(185, "which is conditional on a hidden-sector mixing hypothesis motivated by eigenstate thermalization [Main §3.4]",
  "(C2) necessity is conditional on a hidden-sector mixing hypothesis motivated by ETH.", "status", "C", cited=["[Main §3.4]"],
  hyp=["hidden-sector mixing hypothesis (ETH-motivated)"])

# ---------------------------------------------------------------- §6.4
E(189, "At every finite horizon the laws an embedded observer of a finite reversible system can record are exactly the finite stochastic laws",
  "At every finite horizon, the laws an embedded observer of a finite reversible system can record are exactly the finite stochastic laws (D_K = S_K).",
  "theorem-statement", "U",
  direction=D("equivalence ('exactly')",
    ("D_K ⊆ S_K", "Every recordable law is a finite stochastic law.", "U", [], None),
    ("S_K ⊆ D_K", "Every finite stochastic law is recordable by an embedded observer of some finite reversible system.", "U", [], None)))
E(189, "and exactly the fixed-basis unitary Born laws",
  "The recordable laws are exactly the fixed-basis unitary Born laws (D_K = Q_K).", "theorem-statement", "U",
  direction=D("equivalence ('exactly')",
    ("D_K ⊆ Q_K", "Every recordable law is a fixed-basis unitary Born law.", "U", [], None),
    ("Q_K ⊆ D_K", "Every fixed-basis unitary Born law is recordable.", "U", [], None)))
E(189, "because the representation is universal, the discriminating content lies in memory",
  "Because the representation is universal, the discriminating content lies in memory.", "scope", "U")
E(189, "which every deterministic completion carries in its hidden state", "Every deterministic completion carries the memory in its hidden state.", "result", "U",
  flag="Repeats the abstract's 'every deterministic completion' claim (I-008); in the body the hidden memory is readout-relevant exactly when M_t>0.")
E(189, "Exact operational quantum mechanics is reached only under completion conditions",
  "Exact operational QM is reached only under the completion conditions (Theorem 4, ⇒ direction).", "result", "U")
E(189, "that OI alone does not imply", "OI alone does not imply the completion conditions.", "negative", "U")
E(189, "representability does not select the evolution relating two times", "Representability does not select the evolution relating two times.", "negative", "U")
E(191, "Applied to vacuum energy, OI proposes that the zero-point sum of the emergent description is not a gravitational source",
  "OI proposes the emergent zero-point sum is not a gravitational source.", "status", "CJ")
E(191, "conditional on covariant field equations that are not derived", "The vacuum-energy proposal is conditional on underived covariant field equations.", "status", "C",
  hyp=["covariant field equations"])
E(191, "applied to black-hole information, it separates conservation from accessible recovery",
  "OI separates information conservation from accessible recovery.", "result", "N")
E(191, "while the framework's Page curve is not established", "The framework's Page curve is not established.", "status", "O")
E(191, "Neither application is a demonstrated resolution of its problem.", "Neither application is a demonstrated resolution.", "negative", "O")

# ---------------------------------------------------------------- Code, data and formal verification
E(195, "The declarations in Appendix A were checked in Lean 4.33.0 with Mathlib v4.33.0 at commit 17b830bcd0ecc36e10eff5b9eeca03bdd7198d86",
  "Appendix A declarations were checked with Lean 4.33.0 / Mathlib v4.33.0 at commit 17b830bc.", "status", "K",
  flag="Mapper: confirm toolchain versions (lean-toolchain, lake manifest) at 17b830bc.")
E(195, "whose Lean sources are identical at the corpus commit `b64919cd`",
  "The Lean sources at 17b830bc are identical to those at corpus commit b64919cd.", "status", "U")
E(195, ("whose `lean-axioms` step requires", "`Quot.sound`"),
  "The release gate's lean-axioms step requires every #print axioms report to lie within propext, Classical.choice, Quot.sound.", "scope", "U")
E(195, "Each declaration in Appendix A reports exactly these three",
  "Every Appendix A declaration's axiom report is exactly {propext, Classical.choice, Quot.sound}.", "status", "K",
  flag="'exactly these three' is stronger than 'within'; check every declaration's report, including small lemmas that may use fewer.")
E(195, "the expected result and the comparison recipe are in `papers/introduction_repro/`",
  "The expected result and comparison recipe are retained in papers/introduction_repro/.", "status", "U")

# ---------------------------------------------------------------- Appendix A
def AD(line, span, ident, loc, what, flag=None, direction=None, cited_extra=()):
    E(line, span, f"`{ident}` ({loc}) is a machine-checked declaration for {what}.", "status", "K",
      cited=[f"`{ident}` ({loc})", *cited_extra], flag=flag, direction=direction)

AD(208, "`finite_horizon_equivalence` (Equivalence:462)", "finite_horizon_equivalence", "Equivalence:462", "Theorem 1")
AD(208, "`S_imp_D` (:422)", "S_imp_D", "Equivalence:422", "S_K ⊆ D_K")
AD(208, "`D_imp_Qfb` (:294)", "D_imp_Qfb", "Equivalence:294", "D_K ⊆ Q_K")
AD(208, "`Qfb_imp_S` (:245)", "Qfb_imp_S", "Equivalence:245", "Q_K ⊆ S_K")
E(208, "compositions :466–468", "The reverse inclusions are machine-checked as compositions at Equivalence:466–468.", "status", "K", cited=["Equivalence:466–468"])
AD(208, "supporting `permMatrix_mem_unitaryGroup` (EquivalenceChain:179)", "permMatrix_mem_unitaryGroup", "EquivalenceChain:179",
   "the permutation matrix being unitary (supporting Theorem 1)")
E(208, "Prior independence is proved on paper.", "The independent-prior realization is proved on paper (not machine-checked).", "status", "P")
AD(209, "`pushforward_identity`", "pushforward_identity", "HiddenMemory:83", "Theorem 2 (joint-law form; presumably (a))",
   flag="Appendix A does not say which declaration proves which part of Theorem 2; mapper to assign.")
AD(209, "`distinguishability_floor`", "distinguishability_floor", "HiddenMemory:114", "Theorem 2 (joint-law form; presumably (b))")
AD(209, "`capacity_floor`", "capacity_floor", "HiddenMemory:170", "Theorem 2 (joint-law form; presumably (c))")
AD(209, "`unavoidable_hidden_predictive_memory`", "unavoidable_hidden_predictive_memory", "HiddenMemory:185", "Theorem 2 (joint-law form; combined)")
E(209, ("the time-$t$ identification and the standard vanishing criterion", "are not machine-checked"),
  "The time-t identification and the CMI vanishing criterion are not machine-checked.", "status", "P", cited=["[CT06]"])
AD(210, "`c3_necessity`", "c3_necessity", "C3Necessity:80", "the capacity bound |C_H| ≥ 2^{I*}")
AD(210, "`card_hidden_ge_two_pow_Istar`", "card_hidden_ge_two_pow_Istar", "C3Necessity:117", "the capacity bound |C_H| ≥ 2^{I*}")
AD(211, "`isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110)", "isPermMatrix_of_stochastic_inverse", "EquivalenceChain:110",
   "the stochastic-inverse lemma")
AD(211, "`pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148)", "pIndivisible_of_rooted_identity_return_of_overlap",
   "RecurrenceHorizon:148", "Theorem 3 (rooted form)")
AD(212, "`routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122) for routed readback", "routed_forces_indivisible_somewhere",
   "PhysicalC4Discharge:122", "readback forces indivisibility (routed readback)")
E(212, "on paper for (C4)", "Readback forces indivisibility is proved on paper for history-level (C4).", "status", "P")
AD(213, "`gl2_strong_gauge_moves_relative_candidate`", "gl2_strong_gauge_moves_relative_candidate", "CoherentLiftGauge:537",
   "time-dependent right action changing the relating evolution")
AD(213, "`gl3_constant_gauge_preserves_relative`", "gl3_constant_gauge_preserves_relative", "CoherentLiftGauge:451",
   "constant deformation cancelling from the relating evolution")
AD(213, "`bridge_traj`", "bridge_traj", "TrackBQfbBridge:276", "same one-step matrix ⇒ same root-conditioned trajectory laws")
AD(213, "`rooted_eq_iff_slice_eq` (forward direction)", "rooted_eq_iff_slice_eq", "TrackBQfbBridge:180",
   "equal rooted families ⇒ equal one-step matrices (forward direction only cited)")
AD(213, "`realData_traj_stochastic`", "realData_traj_stochastic", "TrackBQfbBridge:286",
   "fixed-basis realizability and stochasticity of the trajectory laws")
AD(214, "`exactAll_iff_physical_general` (GeneralCarrier:100)", "exactAll_iff_physical_general", "GeneralCarrier:100",
   "Theorem 4 (both directions)",
   direction=D("equivalence (iff declaration)",
     ("⇒", "exactAll ⇒ physical (conditions (i)–(v)).", "K", ["`physical_of_exactAll` (PhysicalCharacterization:301)"], None),
     ("⇐", "physical ⇒ exactAll.", "K", ["`exactAll_of_physical_general` (GeneralCarrier:93)"], None)),
   flag="The body (line 118) names only the two directional declarations; Appendix A adds the iff declaration. Mapper: check the iff is assembled from these two directions.")
AD(214, "$\\Rightarrow$ `physical_of_exactAll` (PhysicalCharacterization:301)", "physical_of_exactAll", "PhysicalCharacterization:301", "Theorem 4 ⇒")
AD(214, "$\\Leftarrow$ `exactAll_of_physical_general` (GeneralCarrier:93)", "exactAll_of_physical_general", "GeneralCarrier:93", "Theorem 4 ⇐")
AD(214, "`krausSoundExt_of_validity_inert` (OperationalValidity:124)", "krausSoundExt_of_validity_inert", "OperationalValidity:124", "a step of Theorem 4 ⇐")
AD(214, "`compositeCompleteness_unconditional` (IsometryExtension:179", "compositeCompleteness_unconditional", "IsometryExtension:179",
   "a step of Theorem 4 ⇐ (composite completeness)")
AD(214, "premise discharged by `finiteIsometryExtensionSF_discharged`, :116)", "finiteIsometryExtensionSF_discharged", "IsometryExtension:116",
   "discharging the premise of compositeCompleteness_unconditional")
AD(214, "`exactAll_of_levelOne` (LevelOneSeam:196)", "exactAll_of_levelOne", "LevelOneSeam:196", "a step of Theorem 4 ⇐ (level one to all levels)")
AD(215, "`five_way_minimality` (RankGapTheory:702)", "five_way_minimality", "RankGapTheory:702", "independence of (i)–(v) on the qubit")
AD(215, "`oi_alone_not_qm` (GeneralCarrier:160)", "oi_alone_not_qm", "GeneralCarrier:160", "OI alone does not imply QM (qubit)")

# ---------------------------------------------------------------- Appendix B.1
E(221, ("Let $\\mathcal C_V=\\{0,1\\}$", "and $5$ with $6$."),
  "B.1 model: C_V={0,1}, C_H={1..6}; for h∈{1,2} φ flips x and keeps h (recording the flip); for fixed x, φ swaps h 3↔4 and 5↔6.",
  "definition-used", "U", cited=["[Main §2.4]"],
  flag="B.1 is cited to [Main §2.4] while Theorem 3 is cited to [Main §2.3]; check the model's location in Main.")
E(221, "A second application reads the record and flips the bit back.", "Applying φ twice returns the visible bit (Γ_2 = I).", "result", "U")
E(223, r"\Gamma_1=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}", "B.1: with h uniform, Γ_1 = [[2/3,1/3],[1/3,2/3]].", "numerical", "U", hyp=["h uniform"])
E(223, r"\Gamma_2=I", "B.1: Γ_2 = I.", "numerical", "U", hyp=["h uniform"])
E(224, r"\Gamma_1^{-1}\Gamma_2=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}", "B.1: Γ_1^{-1}Γ_2 = [[2,-1],[-1,2]].", "numerical", "U")
E(226, "The only candidate divisor has negative entries, so the family is P-indivisible.",
  "B.1's only candidate divisor has negative entries, so the family is P-indivisible.", "result", "U")
E(226, "A Markov chain with the same one-step matrix would instead give $\\Gamma_1^2$, with diagonal entries 5/9 and off-diagonal entries 4/9.",
  "A Markov chain with B.1's one-step matrix gives Γ_1² with diagonal 5/9, off-diagonal 4/9.", "numerical", "U")
E(228, "With $x_0$ uniform and independent of $h$, $P(x_2{=}0\\mid x_1{=}1,x_0{=}0)=1$",
  "B.1 with x_0 uniform and independent of h: P(x_2=0 | x_1=1, x_0=0) = 1.", "numerical", "U", hyp=["x_0 uniform, independent of h"])
E(228, "while $P(x_2{=}0\\mid x_1{=}1)=1/3$", "B.1: P(x_2=0 | x_1=1) = 1/3.", "numerical", "U", hyp=["x_0 uniform, independent of h"])
E(228, "For $P(x_0{=}0)=a$, the second value is $a/(2-a)$.", "B.1: for P(x_0=0)=a, P(x_2=0 | x_1=1) = a/(2−a).", "numerical", "U")

# ---------------------------------------------------------------- Appendix B.2
E(232, "Every two-time transition matrix is $\\tfrac12J$", "B.2 (X_2 = X_0 ⊕ X_1): every two-time transition matrix is ½J.", "numerical", "U")
E(232, "so the family factors through $\\Lambda=I$ and is P-divisible", "B.2's family factors through Λ = I and is P-divisible.", "result", "U")
E(232, "Yet $I(X_0;X_2\\mid X_1)=1$ bit.", "B.2: I(X_0; X_2 | X_1) = 1 bit.", "numerical", "U")
E(232, "Up to flipping the final bit, this is the process of [RHP14, Eq. (15)]", "B.2 is, up to a final bit flip, RHP14 Eq. (15).", "attribution", "U", cited=["[RHP14, Eq. (15)]"])
E(232, "it appears concurrently in [Dou26, App. A]", "B.2's process appears concurrently in Doukas App. A.", "attribution", "U", cited=["[Dou26, App. A]"])

# ---------------------------------------------------------------- Appendix B.3
E(236, ("The two-card game of [Book §1.11]", "drawn uniformly and independently."),
  "Card game: visible hole card h, face-down burn card b uniform and independent; a street swaps them; a peek reveals h and overwrites b with a fresh uniform card.",
  "definition-used", "U", cited=["[Book §1.11]"])
CARD_NOTE = "'obtained by exact enumeration of the equally likely cases' (line 238)"
E(242, "| one shuffle | 1/2 |", "Card game: P(showdown hole card = dealt) after one shuffle = 1/2.", "numerical", "N", note=CARD_NOTE)
E(243, "| two shuffles | 1 |", "Card game: after two shuffles = 1.", "numerical", "N", note=CARD_NOTE)
E(244, "| two shuffles, with a peek between them | 1/2 |", "Card game: two shuffles with a peek between = 1/2.", "numerical", "N", note=CARD_NOTE)
E(245, "| Markov prediction for two shuffles, $\\Gamma_1^2$ | 1/2 |", "Card game: Markov prediction Γ_1² for two shuffles = 1/2.", "numerical", "N", note=CARD_NOTE)
E(247, "Here $\\Gamma_1=\\tfrac12J$ and $\\Gamma_2=I$.", "Card game: Γ_1 = ½J, Γ_2 = I.", "numerical", "U")
E(247, ("The two rows of $\\Gamma_1$ are equal", "the family is P-indivisible."),
  "Card game: equal rows of Γ_1 make Γ_1Λ ≠ I for every Λ, so the family is P-indivisible.", "result", "U")
E(249, "if the peek only reveals or replaces the hole card, the probability is 1",
  "If the peek only reveals or replaces the hole card, the two-shuffle probability is 1.", "numerical", "U")
E(249, "so the 1/2 comes from overwriting the record, not from looking",
  "The 1/2 with a peek is due to overwriting the record, not to observation.", "result", "U")
E(249, "With anticorrelated cards ($b=1-h$), $\\Gamma_1$ is a permutation and the game is divisible.",
  "With anticorrelated cards, Γ_1 is a permutation and the game is divisible.", "result", "U")
E(251, "On card inputs the game is a classical stochastic process", "On card inputs the game is a classical stochastic process.", "result", "U")
E(251, "and its P-indivisibility is notion (2) of §3.1", "The game's P-indivisibility is notion (2) (stochastic P-indivisibility).", "scope", "U")
E(251, "The one-step channel is then the constant channel $\\rho\\mapsto\\operatorname{tr}(\\rho)\\,I/2$",
  "Under the permutation-unitary embedding with uniform diagonal burn card, the one-step channel is ρ ↦ tr(ρ) I/2.", "result", "U",
  cited=["[Main §3.2] (preceding sentence)"])
E(251, "which is entanglement-breaking [Main §3.2, Remark (failure of (C1))]", "The constant one-step channel is entanglement-breaking.", "result", "U",
  cited=["[Main §3.2, Remark (failure of (C1))]"])
E(251, "The two-step map is the identity channel.", "The card game's two-step map is the identity channel.", "result", "U")
E(251, "The family is therefore CP-indivisible [Main §3.2, Theorem (CP-indivisibility, framework scope)].",
  "The embedded card-game family is CP-indivisible.", "result", "U", cited=["[Main §3.2, Theorem (CP-indivisibility, framework scope)]"])
E(253, ("Following Bäcker, Beyer and Strunz [BBS24]", "conditioned on its outcome."),
  "BBS24: a two-step process has classical memory when the second map is an instrument realizing the first map followed by outcome-conditioned channels.",
  "attribution", "U", cited=["[BBS24]"])
E(253, "With the hidden slot initialized to a fixed card instead, the swap has the maps $\\rho\\mapsto|0\\rangle\\langle0|$ and $\\rho\\mapsto\\rho$",
  "With a fixed hidden card, the swap's one- and two-step maps are ρ ↦ |0⟩⟨0| and ρ ↦ ρ.", "result", "U", cited=["[Main §4.5]" + SF])
E(253, "and admits no such decomposition [Main §4.5]", "The fixed-card swap admits no classical-memory decomposition.", "negative", "U", cited=["[Main §4.5]"])
E(253, "With the uniform burn card it does", "With the uniform burn card, the swap admits a classical-memory decomposition.", "result", "U")
E(253, ("the instrument $\\rho\\mapsto\\tfrac14\\sigma_o\\rho\\sigma_o$", "sums to the one-step map"),
  "The Pauli instrument ρ ↦ ¼σ_oρσ_o sums to the one-step map.", "result", "U")
E(253, "the identity $\\sum_o\\sigma_oX\\sigma_o=2\\operatorname{tr}(X)\\,I$", "Σ_o σ_o X σ_o = 2 tr(X) I (Pauli twirl identity).", "numerical", "U")
E(253, "and the channels $\\rho\\mapsto\\sigma_o\\rho\\sigma_o$, conditioned on $o$, return $\\rho$",
  "Conditioning on o and applying σ_o returns ρ (two-step map = identity).", "result", "U")
E(255, "A card arrangement violates no Bell inequality [Book §1.11; Main §3.3].", "No card arrangement violates a Bell inequality.", "negative", "U",
  cited=["[Book §1.11; Main §3.3]"], flag="'A card arrangement' read as 'any card arrangement'.")

# ---------------------------------------------------------------- References (status of corpus records)
E(267, "unpublished research record, internally reviewed", "[BHa] is an unpublished, internally reviewed research record.", "status", "U", cited=["[BHa]"])
E(269, "unpublished research record, internally reviewed", "[BHb] is an unpublished, internally reviewed research record.", "status", "U", cited=["[BHb]"])

# ---------------------------------------------------------------- assemble
ENTRIES.sort(key=lambda t: (t[0], t[1], t[2]))
out = []
for k, (_, _, _, e) in enumerate(ENTRIES, 1):
    cid = f"I-{k:03d}"
    rec = {"id": cid}
    rec.update(e)
    if rec["direction"]:
        for s in rec["direction"]["sub_claims"]:
            s["id"] = f"{cid}.{'ab'[rec['direction']['sub_claims'].index(s)] if len(rec['direction']['sub_claims'])<=2 else 'abc'[rec['direction']['sub_claims'].index(s)]}"
    out.append(rec)

# verify verbatim
for r in out:
    blk = "\n".join(LINES[r["line"] - 1:r.get("line_end", r["line"])])
    assert r["text"] in blk, r["id"]

json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(OUT, "a").write("\n")
bysec = collections.OrderedDict()
for r in out:
    bysec[r["section"]] = bysec.get(r["section"], 0) + 1
bytype = collections.Counter(r["type"] for r in out)
bylev = collections.Counter(r["status_as_stated"]["level"] for r in out)
json.dump({"total": len(out), "by_section": bysec, "by_type": dict(bytype), "by_level": dict(bylev),
           "with_direction": [r["id"] for r in out if r["direction"]],
           "attention": [(r["id"], r["line"], r["attention"]) for r in out if "attention" in r]},
          open(STATS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
