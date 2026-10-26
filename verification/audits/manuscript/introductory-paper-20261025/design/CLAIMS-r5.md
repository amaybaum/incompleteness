# Introduction r5: register of new claims

This register lists every claim r5 makes beyond r4. The claims r4 already makes are carried at r4's reviewed
strength. Their sources are in r4, its re-checks and the design records `SOURCES-r4.md` and `ERRATUM-r4.md`, and
they are not repeated here. Exact wording is in `OUTLINE-r5.md`.

## Key

**Status:**
- **proved** — a written proof or a kernel proof exists for the object stated;
- **conditional (on X)**;
- **identity** — true by construction or by dimensional algebra;
- **postdiction** — agreement with a value measured before the expression was written;
- **interpretation**;
- **open**;
- **structural** — the paper's own organization, with no physical content.

**Agreement:**
- **NA** — numerical agreement with existing data;
- **IP** — an independent prediction stated before comparison;
- **none** — no empirical number is involved.

**Literature:**
- **[abs]** — the arXiv abstract was read first-hand through the arXiv API on 2026-10-26, and the body was not read;
- **[pkg]** — read by a reviewed package's literature study, not by this design;
- **[mem]** — not read; may not support a sentence.

## Register

| ID | Claim (short) | Status | Source at 687e885b | Layer | Agreement and dating | Literature |
|---|---|---|---|---|---|---|
| N-INT1 | The paper is organized by three questions | structural | — | — | none | — |
| N-INT2 | §5's applications are reported from [GR] and unpublished computations [BHa; BHb] whose novelty has not been established, each with its conditions, and none is claimed as a new physical result | structural, scope | r4:32; BH package READMEs ("not adopted") | — | none | — |
| N-INT3 | Status key: consistency relation, numerical agreement, independent prediction | structural | owner decision, 2026-10-26 | — | none | — |
| N-LIT1 | 't Hooft argued that QM may be a tool for analysing a system classical at its core, and discussed reconciliation with Bell | literature report | — | L | none | 't Hooft, arXiv:1405.1548v3 **[abs]**. The body is not read, so no statement about permutation unitaries or "ontological basis" is made |
| N-CC0 | The Planck-cutoff zero-point density is about 10¹²² times the observed density | identity, numerical background | `cc.py`: ρ_P/ρ_crit = 6.0×10¹²² at H₀ = 67.4 | A, N | none (background) | standard; Weinberg 1989 **[mem]**, not cited |
| N-CC1 | A uniform shift of the emergent Hamiltonian changes no visible transition probability | proved (one line: global phase) | GR:356 | A | none | standard QM. The required qualifier says so (AW-2) |
| N-CC2 | Whether the offset sources curvature is a separate coupling question; the covariant field equations with source coupling are open; the no-cancellation proposal is conditional on them | conditional on the covariant field equations (Level G3 of [GR]) | GR:356 ("Invisibility to quantum mechanics is not decoupling from gravity"); GR:12 (ladder: "G3, covariant field equations … open") | I, O | none | — |
| N-CC3 | Two gravitational completions differing by ρ_C g_μν share the same substratum, partition, visible law, representation and calibration | proved at prose level (an existence observation) | GR:356 | I (prose) | none | — |
| N-CC4 | *If* the field equations take GR's target form with the substratum's classical stress-energy as source, the zero-point sum is not a source | conditional | GR:12, the target $E_{\mu\nu}=8\pi G(T_{\mu\nu}-\mathcal F g_{\mu\nu})$ | I, O | none | — |
| N-CC5 | Λ's value is an input; ρ ~ H²/G is the Friedmann normalization of the total density; Ω_Λ is an input | identity, and a stated input | GR:360 ("set by initial conditions via the Friedmann equation"); `cc.py` | A | none. Explicitly **not** a prediction (AW-4) | — |
| N-CC6 | The 10¹²² mismatch equals S_dS up to (8/3)(l_p/l_cut)⁴: a dimensional identity | identity | `cc.py` (sympy exact) | A | none. **Not** an independent prediction | CKN 1999 **[abs]**: the abstract states a UV–IR cutoff relation and CC implications, **not** ρ ~ M_P²H². Not cited for that |
| N-CC7 | The coupling of electroweak and QCD vacuum-transition energy to gravity is not fixed by the descriptive distinction | open | GR:581 classifies the Higgs shift; AUDIT AW-3 shows the rule does not decide it | O | none | Kaloper–Padilla 2014 **[abs]** (sequestering covers phase transitions), cited in N-LIT2 only |
| N-CC8 | Deriving the covariant field equations, with conservation and source coupling, would settle the proposal | open (programme statement) | GR:12 (named open items) | O | none | — |
| N-LIT2 | Related proposals: trace-free Einstein equations (Λ's value unexplained); sequestering (extends to phase transitions); Volovik (thermodynamics of many-body ground states). OI differs in locating the source in the substratum microstate | literature report | — | L | none | Ellis–van Elst–Murugan–Uzan, arXiv:1008.1196 **[abs]**; Kaloper–Padilla, arXiv:1309.6562 **[abs]**; Volovik, arXiv:gr-qc/0604062 **[abs]**. Each carries a VERIFY (body). Unimodular gravity (Anderson–Finkelstein 1971) and Padmanabhan **[mem]**, not cited |
| N-BH1 | Conservation by bijectivity neither implies nor is necessary for recovery from accessible records | proved (finite: exhaustive counterexamples) | Main:66 (premise); BH-01 REPORT:17, :36; ch19:72 | E | none | r4 [Sha79] VERIFY kept |
| N-BH2 | The Page value enters only through H-scramble, which no bijection satisfies from a definite configuration with aligned cuts; on a shell the Haar value differs from S_Page | proved (C1, C6(a), one-line proof plus exhaustive); C6(b) a proof reading; C6(c) conditional | BH-02 REPORT:14, :18–20 | P, E | none | Page 1993 (in r4) |
| N-BH3 | GR's Page curve is conditional: H-scramble is open; D-decoupling over the evaporation is assumed and not supplied by timescale ordering (t_evap/τ_B^D ≥ 10⁵⁷ at 30 M☉); the cycle-typicality argument gives a time average at a fixed bipartition, and the pointwise curve is open. The information problem is not resolved | conditional, and open | GR:817, :841 (labels); GR:811 (false; R11 #8); BH-01 REPORT:211–241 (item F); BH-02 REPORT:21 (C6(d)); REVIEW.md §1 (C.4 SITE-ERROR) and §4 O-1 | E (intervals), P, O | none. GR's own "no empirical confrontation" (ch07:159 family) stands | Penington 2020 (in r4). QES agreement not established |
| N-BH4 | Page-time fraction (Page's formula, for a constant coefficient, S_BH ∝ M² and constant β), 0.646 at β = 1; β not derived; an M-dependent coefficient moves it | identity (external formula), conditional | ch07:143; GR:611; BH-02 REPORT:22 (C7); REVIEW §0 (ODE control) | A | none. 0.646 is not compared with data; there is no framework-specific test (AUDIT §7.2) | Page 2013 (in r4) |
| N-HT1 | The calibration T_cl = T_KMS gives ħ = c³ε²/(4Gσ), fixing only ε/√σ = 2l_p; σA/ε² = A/4l_p² for every ε, σ; 1/4 = 2π/8π; a consistency relation, not a prediction | identity, conditional on H-slope and the horizon and frame conditions | GR:148 (Step 4); GR:12 (conditions); GR:310; GR:320 | A (`quarter.py`: k_Q/k₈ for every η, with countercontrols) | none. **Not** a prediction; no independent test. GW250114 tests the area law, not the 1/4 (GR:322) | Hawking 1975 **[mem]**: VERIFY on the historical clause. The relation itself is checked by `quarter.py`'s Hawking route. Jacobson 1995 **[abs]**: the abstract supports the first-law/Einstein link only |
| N-HT2 | The classical temperature uses Einstein's first law as an input | identity (scope statement) | GR §3.1 (GR:96–104) | I | none | — |
| N-PE1 | In one exhaustively enumerated clock-controlled generator an active 2-bit observer predicts with advantage 1/8–5/32; this bounds a framework statement's scope and predicts no new effect | proved for one cell (existence, exact enumeration) | PE-01 REPORT at `efbfd0d7` ("Result" table). **Not on `main`: gated (§A.42)** | E | none. **Framework validation** (owner decision); no physical prediction; dated 2026-10 | "Known in kind" from the package's A3 tags **[pkg]**: Gomułkiewicz–Kutyłowski–Wlaź 2006, AGHP 1992. Not cited by r5 |
| N-AR1 | Under (EM), fast-mixing equilibrium regions support no observer with persistent, read-back records | conditional on (EM) and the rate condition | Main:726–734 (Theorem, "conditional on (EM)") | P, I | none | Past-hypothesis literature **[mem]**, not cited |
| N-MR1 | Theorem 1 admits a definite-records reading; fixed-basis records only; an interpretation | interpretation | Main:632 ("for the represented diagonal sector — … not the instrument algebra") | I | none | ψ-epistemic literature **[mem]**, not cited |
| N-GC1 | The covariant field equations are not derived; §5.1 is conditional on them; §5.3 uses Einstein's first law; (C4) is not shown at the cosmological partition | open | GR:12; GR:20; GR:52 ("Not presently discharged") | O | none | — |
| N-EX1 | No experiment yet distinguishes OI from standard QT; no memory-witness falsifier is established | open | Main:704 | O | none | Bäcker–Beyer–Strunz (r4 [BBS24], VERIFY kept) |
| N-EX2 | SM closed forms such as λ = 1/(π√2) agree with values measured before they were written; they are numerical agreements, not predictions, and rest on the cubic commitment and bridge hypotheses | postdiction with selection, class **C** (AUDIT §6.1; appendix-a:74's S is too strong) | SM:849 ("This is a hypothesis, not a derivation"; "the empirical match at 0.04% confirms the commitment but does not derive it"); appendix-a:217 ("no pre-registered forward confirmation") | N | **NA (postdiction).** Dating: form and comparison first appear together in `054eb99a` (2026-04-04); the c_λ commitment and the dispersion choice, with the boson kernel rejected "at ≈190σ", in `70ffe82f`/`3124ef0a` (2026-07-05/06); λ measured since 1963. Look-elsewhere: 6 of 752 simple forms within 1σ, about 2.5 expected (`lookelse.py`) | PDG λ = 0.22500 ± 0.00067 is as cited in SM. The Cabibbo-angle anomaly (Kℓ3 vs Kμ2, ~3σ) is **[web]**, not read, so r5 quotes no σ |
| N-EX3 | sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798, written after JUNO's first result; the projected ±0.0014 will test it; conditional on an underived 4/3 ratio | postdiction (central value) **and** a stated forward test (precision); class **L** | Juno:73 ("carried out in 2026, after the JUNO first results"); Juno:409 (±0.0014, 2σ falsifier); appendix-a:97 (footnote ᶠ, Layer 2(b)) | N, O | **NA** for the central value (0.07σ; postdiction). **IP-in-kind** for the precision test only: the value and falsifier are stated before JUNO's full-precision data. Whether the 4/3 ratio was selected with the measured angles in view is **undetermined** (AUDIT §7.1); until traced, r5 calls it "a stated test", not "an independent prediction" | JUNO first-result paper **[mem]** (cited inside Juno.md) |

## L. Literature status

### Read first-hand at abstract level

Read through the arXiv API on 2026-10-26; the records are in `design-r5/dl/`.

| Key | arXiv | What the abstract supports | What it does **not** support |
|---|---|---|---|
| [tH14] | 1405.1548v3 | QM as a tool for a system "classical at its core"; reconciliation with Bell; superdeterminism discussed | any statement about permutation unitaries or the D ⊆ Q direction (AUDIT §3.3 item 4, which is [mem]) |
| [EvEMU11] | 1008.1196v2 (*CQG* 28, 225007) | trace-free Einstein equations resolve the discrepancy and do not explain Λ's observed value | — |
| [KP14] | 1309.6562v2 (*PRL* 112, 091304) | sequestering of all matter vacuum energy, including phase transitions | — |
| [Vol06] | gr-qc/0604062v4 (*IJMPD* 15, 1987) | thermodynamics of the many-body ground state; the zero-point UV sum does not set the vacuum energy | — |
| [Jac95] | gr-qc/9504004v2 (*PRL* 75, 1260) | the Einstein equation from S ∝ A and δQ = T dS | "Λ as an integration constant" (AUDIT [mem]) |
| [CKN99] | hep-th/9803132v2 (*PRL* 82, 4971) | a UV–IR cutoff relation and CC implications | "ρ ~ M_P²H²" (AUDIT [mem]) |
| [Cal26] | 2601.18720v2 | r4, unchanged | — |

### Not read; cited only behind a VERIFY, or not at all

- **[Haw75]** (Hawking, *Commun. Math. Phys.* 1975): the historical clause in N-HT1, VERIFY.
- **Not cited:** Weinberg 1989; Anderson–Finkelstein 1971; Padmanabhan; Wetterich; Hall (measurement dependence);
  Bekenstein 1973; Hayden–Preskill 2007; Gomułkiewicz–Kutyłowski–Wlaź 2006; AGHP 1992; PDG and CKMfitter updates;
  Cabibbo-anomaly papers.

### 't Hooft and novelty of viewpoint

Only the abstract was read. **r5 therefore makes no claim of novelty of viewpoint.** It states the opposite as
non-claim (10), at the strength of the abstract. A full read of 't Hooft (2016, the book version) is needed before any
sentence comparing OI's results with 't Hooft's constructions (e.g. the D ⊆ Q direction) is added. r5 adds no such
sentence.

## Summary for the owner

- **Q2 contains no independent prediction.** Its items are:
  - a conditional proposal (the cosmological constant);
  - a conditional result with an open status (the Page curve), alongside a proved finite non-implication
    (preservation is not recovery);
  - a consistency relation (the 1/4 and ħ);
  - a scope-validation result (PE-01, gated);
  - one conditional theorem (the arrow, under (EM));
  - one interpretation (measurement).
- **The only item with a stated test ahead of data** is the JUNO precision test (N-EX3). It is in Q3, with its 4/3
  selection history undetermined.
- **Every numerical agreement in r5 is a postdiction:** the Cabibbo form and the JUNO central value. The text says so
  next to the number.
