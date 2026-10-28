# Applications audit for the Introduction paper (r5 scope)

Read-only audit. Corpus: `main` at `687e885b` (worktree `S/paper/mainwt`). History: the unshallow clone `S/ppe/repo`
(4,758 commits; `research/oi-pseudoentropy-20261025` at `efbfd0d7`, equal to the remote tip, so nothing was fetched).
Nothing in the repository was changed. `S` is the session scratch directory (absolute prefix elided).

Owner rule, 2026-10-26: "ambitious in its scientific implications but conservative in its claims." The section is
titled "Applications and Potential Resolutions". Every permitted sentence below is at the corpus's maintained strength
or weaker, in the neutral register of §A.32/§A.33, and states its conditions next to the claim.

**Checks run here**, all with `python3 -I` in `S/paper/apps/`:

| Script | What it settles | Verification layer |
|---|---|---|
| `quarter.py` | Whether the Bekenstein–Hawking 1/4 is an output of the mode count, or of the calibration | exact symbolic algebra (sympy), with countercontrols |
| `cc.py` | What the "10¹²² = S_dS" identification contains | exact algebra, plus numerics for orders of magnitude |
| `lookelse.py` | How many simple closed forms land near the Cabibbo value | exhaustive finite enumeration of one stated family |

**Git history** (`git log -S` on `S/ppe/repo`) dates the Cabibbo and JUNO forms.

**External literature.** Items marked **[mem]** are cited from memory and were not read first-hand in this audit.
Items marked **[web]** come from a search-result snippet only. Neither supports any manuscript sentence until it is
read. The R11 independent review (`S/paper/r11/REVIEW.md`) was not present when this audit was written, so the
R11 items below rest on `FINDINGS.md` alone.

***

## 0. Summary table

The r5 question each item belongs to: **Q1** "What is OI?", **Q2** "What might it explain?", **Q3** "What remains to be
proved?".

| Candidate | Corpus claim and status (strongest maintained) | Weakest link of the chain | Literature | Recommendation | Permitted status sentence (short form; full form in each section) |
|---|---|---|---|---|---|
| **Cosmological constant** | GR:24 and GR:356: the descriptive distinction is "established"; the dynamical dissolution is "conditional on the G3 coupling theorem". G7 is listed as S, "descriptive relation" | The coupling claim, that the zero-point offset does not source curvature, is Sketch (prose) and is exactly the open Level-G3 step. The quantum-invisibility half is Solid but is already true in standard QM | Unimodular gravity and Jacobson-type Λ as an integration constant; Volovik's two-level vacuum argument; Cohen–Kaplan–Nelson for ρ ~ M_Pl²H² **[mem]** | **Q2, INCLUDE-MAJOR**, a full subsection of about 1.3 pp., labelled a conditional proposal | "The zero-point offset of the emergent description is invisible to every visible transition probability; that it also does not source curvature is the open covariant coupling step, so the proposal is conditional on it and leaves the value of Λ an input." |
| **Black-hole information / Page curve** | ch19:72 and G11 (C): information is preserved by bijectivity; the Page curve is conditional on H-scramble | H-scramble fails for every bijection in GR A.8's own setting (BH-02 C6(a), exhaustive, plus proof). Step A.8 → A.9 is open. GR:811 is a false decoupling inequality | Page 1993/2013; Penington and AEMM 2019; Hayden–Preskill 2007; secret sharing (Shamir) **[mem]** | **Q2, INCLUDE-MAJOR**, about 1.1 pp. (r4 §5 condensed) | "Bijectivity conserves the global state but neither implies nor is necessary for recovery from an observer's accessible records; the framework's Page curve requires the scrambling hypothesis H-scramble, which is open, so the information problem is not resolved." |
| **Emergence of QM (central theme)** | Theorem 1 `finite_horizon_equivalence` and Theorem 4 `exactAll_iff_physical_general` (kernel); `oi_alone_not_qm` (kernel) | Solid at the kernel layer. Physical identification of nature with (S,φ,V) is a hypothesis; (C4) is not discharged at the cosmological cut (GR:20) | Barandes 2023/25/26; Egri et al. 2026; Doukas 2026; Calvo 2026 (in r4). 't Hooft's cellular-automaton interpretation and Wetterich **[mem]**, not in r4 | **Q1 + Q3, INCLUDE-MAJOR** (the body of the paper; already r4 §§2–3, §6) | "At every finite horizon the recordable laws coincide with the finite stochastic laws and with fixed-basis Born laws (machine-checked); exact operational QM holds iff five completion conditions hold (machine-checked), none implied by OI alone." |
| **Horizon thermodynamics: ħ and the 1/4** | GR:12: "obtains … the 1/4 coefficient by direct boundary-mode counting", conditional on H-slope. G3 (ħ) and G4 (1/4) are C. GR:322: "equivalent to the Hawking-temperature normalization" | **Calibration identity** (`quarter.py`): S/(A/l_p²) = k_Q/k_8 = 2π/8π for every mode density η. The count contributes nothing to the 1/4. The calibration fixes only ε/√σ = 2l_p | Hawking 1975 fixes 1/4 from T_H plus the first law, the same identity; Jacobson 1995; Gibbons–Hawking 1977 **[mem]** | **Q2, INCLUDE-BRIEF**, about 0.5 pp., framed as consistency, not prediction | "Matching the classical first-law temperature and the KMS temperature of the same boundary modes calibrates ħ against ε/√σ; with that calibration the mode count reproduces A/4l_p² for every ε and σ, the 1/4 being the ratio 2π/8π, so this is a consistency relation and not a prediction." |
| Measurement problem / wavefunction | Main:666 "measure problem dissolves"; ch19:333 "Dissolved (Bayesian updating)" | Interpretation. The fixed-basis records of Q_K cover only one basis; coherent interventions need Thm 4's conditions, which are open | Epistemic-state and ψ-epistemic literature; 't Hooft; Barandes **[mem]** | Q3, one line in the outlook, as interpretation | "Theorem 1 admits a reading in which records are definite configurations and the quantum state compresses the visible law; it covers fixed-basis records only, and is an interpretation, not a result." |
| Born probabilities | r4 §2.3: p = \|U\|² is definitional; the exponent is not selected | Solid as a negative statement | Barandes 2026 Thm 3.1 | Q3, keep the r4 §2.3 and §6.5 wording | "The relation p=\|U\|² is part of the definition of Q_K; for permutation unitaries every exponent p>0 gives the same table, so the quadratic exponent is not selected." |
| Bell correlations | Main abstract and §3.3: cone plus measurement independence implies \|S\|≤2; quantum values need ontic parameter dependence; H-Bell is open | H-Bell (open) | Bell, CHSH; Hall's measurement-dependence bounds **[mem]** | Q3, keep r4 §6.4(5) | As r4 §6.4(5). |
| Arrow of time | Main §4.6: the observer-selection theorem is "conditional on (EM)"; Substratum:356: "No additional axiom is needed" | (EM) is a hypothesis. Substratum's horizon-clock cascade covers only the ä>0 era | Past hypothesis (Albert); Boltzmann brains (Carroll and others) **[mem]** | Q2, one outlook line at most | "Under the effective-mixing hypothesis (EM), sufficiently fast-mixing equilibrium regions support no observer with persistent, read-back records [Main §4.6]." |
| Dark sector (DM, acceleration, MOND) | G6 a₀=cH/6 (C, factor imported from Verlinde); G9 (C, "partly definitional"); G8 (L); Jiao 2023 and Genzel tensions (GR:12) | The coupling map Q = M_Bc² belongs to the open G3 step (ch07:260–262); the 1/6 is imported | Verlinde 2016; Milgrom's a₀ ≈ cH₀/2π coincidence **[mem]** | Q3, **EXCLUDE** from the main text (at most one clause under gravitational coupling, naming the tensions) | (if used) "A MOND-like scale a₀=cH/6, its factor taken from Verlinde, is conditional on the open coupling step and in tension with the Milky Way outer rotation curve." |
| Information loss and thermodynamics (GSL) | GR A.6 and ch07 §7.6: only a subadditivity inequality; the GSL is open | Open (an identification of S_BH with the von Neumann entropy is missing) | Bekenstein GSL; Wall 2011 **[mem]** | Q3, fold into the BH open steps (r4 §5.4) | "The generalized second law is not derived." |
| Information recovery vs accessibility | BH-01 claim A (exhaustive finite), C1 (proved) | Toy-model scope | Shamir 1979; Hayden–Preskill **[mem]** | This is the BH subsection's content | As for black-hole information. |
| Quantum computing (BQP ceiling) | Computation §4: a "conditional BQP model theorem" | Conditional on global-coverage and model premises | Standard complexity theory | **EXCLUDE** | — |
| Cosmological initial conditions | appendix-a:229: "no current content" | — | — | **EXCLUDE**; the CC subsection states that Λ's value is an input | — |
| **Extra: SM structural forms (Cabibbo 1/(π√2))** | appendix-a:74: S, Layer 1, 0.04%; SM:851: "established at the structural level … emergent dressing pending" | **Postdiction with selection**: the form and its comparison entered together (054eb99a, 2026-04-04); the dispersion and unit prefactor were selected later (3124ef0a/70ffe82f, 2026-07-05/06) against the measured value (the boson kernel was "excluded at ≈190σ"). The emergent dressing is open | λ measured since 1963. Kℓ3 vs Kμ2 tension (Cabibbo-angle anomaly) about 3σ **[web]** | Q3, one outlook line, explicitly as postdictions | "Closed forms such as λ=1/(π√2) agree with values measured before they were written; they are numerical agreements, not independent predictions, and they rest on the cubic-lattice commitment and named bridge hypotheses [SM]." |
| **Extra: JUNO sin²θ₁₂ = 1/3 − 1/(4π²)** | N1: L; Juno:73: derivation postdates the JUNO first results; Juno:409: a 2σ JUNO full-precision disagreement falsifies it | The value needs the Layer-2(b) ratio 4/3, which the natural spurion does not produce (appendix-a footnote ᶠ) | TM1/TM2 sum rules (in Juno.md) | Q3, one outlook line, as the one forward exposure | "The value 0.30798 was written after JUNO's first result; JUNO's design-lifetime precision (±0.0014) will test it, conditional on an underived Wilson-coefficient ratio." |
| **Extra: Page-time β** | ch07:143: β is open; t_P/t_evap = 1−(β/(1+β))^{3/2} is Page 2013 Eq. (8) | β is not derived; the formula is external | Page 2005, 2013 | Q3, **not an application**: two sentences inside the BH subsection (r4 §5.3, condensed) | "The Page-time fraction is Page's, conditional on a constant emission coefficient and on β, which is not derived." |
| **Extra: deterministic randomness (PE-01)** | Branch `efbfd0d7`, REPORT: COUNTEREXAMPLE to the universal ch18:114 statement; one cell, exact enumeration; ch18:114 already rescoped (#933) | Bounded witness (exhaustive finite) | Covered in kind by Gomułkiewicz–Kutyłowski–Wlaź 2006 (counterexample) and AGHP 1992 (passive horizons) | Q2, INCLUDE-BRIEF (about 0.3 pp.) as a scope result, **only after the package lands on `main`** (§A.42) | "A deterministic source is not thereby unpredictable to an embedded observer: in one exhaustively enumerated clock-controlled generator an active two-bit observer predicts its output with advantage 1/8–5/32; this is covered in kind by known clock-control attacks." |

***

## 1. Cosmological constant (leading application): INCLUDE-MAJOR as a conditional proposal

### 1.1 The precise claim
- **GR:24 (Introduction).** "The cosmological constant problem is dissolved by identifying the emergent quantum
  vacuum energy of order M_Pl⁴ and the effective cosmological constant of order H²/G as properties of logically
  distinct objects … the descriptive distinction is established and the dynamical form of the dissolution is
  conditional on the G3 coupling theorem (§6.2)."
- **GR:356 (the anchor; most careful).** "Invisibility to quantum mechanics is not decoupling from gravity; the latter
  is a coupling theorem and is what G3 names as open. Accordingly the descriptive-level distinction is established and
  the dissolution is conditional."
- **Status surfaces.**
  - G7 (appendix-a:113): S, Layer 1, "Descriptive relation".
  - ch19:38: "Dissolved at the descriptive level; the dynamical form is conditional on the covariant coupling theorem".
  - ch19:330: "Dissolved (10¹²² = S_dS)", which carries no condition.
- **Level G3** is defined at GR:12 as "covariant field equations with conservation/Bianchi structure and the continuum
  limit, open". Its target equation is E_μν[g,OI] = 8πG(T_μν − 𝓕[g,T]g_μν).

### 1.2 The chain

| # | Link | Grade | Layer |
|---|---|---|---|
| 1 | Q_K has an exact unitary representation, and an additive shift H→H+E₀ leaves every \|U_ij(t)\|² unchanged (GR §3.3) | Solid | exact algebra, elementary |
| 2 | The emergent QFT assigns ½ħω per mode up to the cutoff 1/ε, giving ρ_QFT ~ M_Pl⁴ (GR §6.1) | Solid as bookkeeping. It also depends on H-local-lift for the QFT form | prose |
| 3 | Gravity is sourced by the classical stress-energy of the substratum microstate, not by ⟨T̂⟩ (GR §6.2, "geometry-first") | **Sketch**. This is the coupling statement. GR:356 itself says it is the open G3 theorem | prose |
| 4 | The relative-vs-absolute split: relative energies gravitate, the uniform offset does not (GR §8.3) | **Sketch**, ambiguous (§1.3 item 3) | prose |
| 5 | The observed density is ρ ~ H²/G (GR §6.1, §6.3) | The Friedmann normalization of the total density, not an output | identity |
| 6 | 10¹²² = S_dS (GR §6.3) | A dimensional identity (§1.3 item 4) | algebra |

The weakest link is 3, so the class is **C** (conditional on Level G3). It sits on the consistency axis: no novel
empirical confrontation is involved. Architecturally the chain is mixed, with emergent-QFT bookkeeping and a
substratum coupling claim.

### 1.3 Hidden assumptions (gem-finding)

1. **"Distinct descriptions" is a reframing plus a conditional proposal; the gauge argument adds no content (NEW).**
   - GR:583 calls the offset "a gauge parameter … unobservable in principle", and "the problem's premise … attributes
     physical content to a gauge degree of freedom".
   - Standard QFT already says the absolute vacuum energy is invisible to every non-gravitational measurement. The
     cosmological constant problem is precisely that gravity is the one probe that sees it.
   - Link 1 therefore restates the premise of the problem. The entire resolving content is link 3, which GR:356
     correctly calls open.
   - GR:583 contradicts GR:356 ("Invisibility to quantum mechanics is not decoupling from gravity").
2. **ρ ~ H²/G is not an output (NEW).**
   - ρ_crit = 3H²c²/(8πG) is the Friedmann equation for the *total* density of a flat universe.
   - Any component with Ω = O(1) sits at "H²/G". The vacuum fraction Ω_Λ ≈ 0.69, and the coincidence Ω_Λ ~ Ω_m now,
     are inputs (`cc.py`).
   - GR:366 and ch07:195 ("not a prediction awaiting future data … the value the framework expects") therefore
     present a normalization as an expectation.
   - GR:360 and ch07:201 concede the value is "set by initial conditions". That is the maintained strength.
3. **Phase-transition vacuum energy is unclassified (NEW).**
   - GR §8.3 says relative energy differences between configurations gravitate and absolute ground-state energies do
     not, and puts the electroweak V(φ_min) shift (~(200 GeV)⁴) in the absolute class.
   - The electroweak and QCD transitions are, however, energy differences between two configurations of the emergent
     fields occupied at different cosmic times. By the stated rule they would be relative.
   - The rule does not decide this case. Only the G3 coupling theorem can, as in unimodular-type completions where it is
     settled by the field equations **[mem]**.
4. **"10¹²² is S_dS" is a dimensional identity (CONFIRMING).**
   - `cc.py` gives (ρ_cut/ρ_crit)/S_dS = (8/3)(l_p/l_cut)⁴, which equals 8/3 at a Planck-length cutoff.
   - Numbers: S_dS = 2.27×10¹²² at H₀ = 67.4, and ρ_P/ρ_crit = 6.0×10¹²².
   - The identity holds for any theory with a Planck cutoff and a Hubble-scale density, in the spirit of
     Cohen–Kaplan–Nelson's ρ ~ M_Pl²H² **[mem]**. It is not an independent output. ch07:195's "independent reason to
     expect" overstates it.
5. **The classical input already contains Einstein dynamics.**
   - The classical first law dE = c²κ dA/(8πG) (GR §3.1) and "the metric evolves via Einstein's equations" (GR §6.2)
     are inputs.
   - Lovelock and the closure theorems leave Λ undetermined (GR §3.2, last paragraph). The proposal therefore converts
     "why is the vacuum energy not Planckian" into "why is the integration constant small". That is a known reframing
     shared with unimodular gravity **[mem]**.
6. **The identifier G3 has three meanings (NEW, editorial hazard).**
   - Level G3 of GR's dependency ladder is the covariant field equations.
   - appendix-a row G3 is the ħ gap equation.
   - Level G3 in Structure and ch03:80–92 is the substratum gauge group.
   - The Introduction must never write a bare "G3". Write "the covariant field equations and their coupling to
     sources (Level G3 of [GR])".

### 1.4 Literature (all **[mem]**, none read in this audit)
- Weinberg 1989 (RMP review).
- Unimodular gravity: Anderson–Finkelstein 1971; Ellis et al. 2011.
- Jacobson 1995: the equation-of-state derivation leaves Λ as an integration constant.
- Padmanabhan's emergent-gravity papers: bulk vacuum energy does not gravitate.
- Volovik, *The Universe in a Helium Droplet* (2003): the effective-theory zero-point sum is cancelled at the
  microscopic level. This is the closest prior form of the "two levels of description" idea.
- Kaloper–Padilla sequestering, 2014.
- Cohen–Kaplan–Nelson 1999.
- GR §6.3 cites Maldacena, CLPW and HUZ. These concern the de Sitter observer and the type II algebra, not
  vacuum-energy decoupling. The corpus's "convergence … strengthens the empirical case for both programs"
  (GR §6.3, ch07 §7.7) is a §A.32 self-assessment and should not be carried into the Introduction.

### 1.5 Recommendation and the permitted sentences
INCLUDE-MAJOR (about 1.3 pp.), titled "The cosmological constant: a conditional proposal". It belongs to **Q2**.

> *Permitted (exact).* In OI the zero-point sum of the emergent quantum description and the effective cosmological
> constant belong to different levels of description. A uniform shift of the emergent Hamiltonian changes no visible
> transition probability, so the quantum description assigns the zero-point offset no observable content [GR §3.3,
> §6.2]. Whether the offset also fails to source curvature is a separate coupling question. Settling it requires
> covariant field equations derived from the substratum, with their coupling to sources, which are open [GR §6.2,
> Level G3]. The proposal that the 10¹²² mismatch requires no cancellation is therefore conditional on that open step.
> It does not explain the observed value of Λ, which enters as a cosmological input. With a Planck-scale cutoff the
> mismatch equals the de Sitter entropy up to a factor of order one; this is a dimensional identity, not an
> independent prediction.

Also permitted, one sentence: "How the energy of electroweak and QCD vacuum transitions couples to gravity is not fixed
by the descriptive distinction and requires the same open coupling step."

Not permitted:
- "dissolves" without the condition;
- "no decoupling mechanism is needed";
- "the value the framework expects";
- "eliminates the 122-digit cancellation";
- any convergence or strengthening language about the de Sitter observer literature.

***

## 2. Black-hole information and the Page curve: INCLUDE-MAJOR (r4 §5, condensed)

### 2.1 The precise claim
- **ch19:72 (scoped anchor).** Information is preserved by bijectivity; recovery is a separate question.
- **G11 (appendix-a:116).** C: "Nested trace-out and H-scramble | Scrambling condition open".
- **GR A.8–A.9.** The Page curve under H-scramble.
- **BH-01 and BH-02 (on `main`, `verification/programmes/black-hole-information/`).**
  - Claim A: bijectivity neither implies nor is necessary for accessible recovery (exhaustive finite).
  - C1–C2: permutation orbits from a configuration are product states; S ≤ H(p₀) (proved, plus exhaustive).
  - C6(a): H-scramble fails for every bijection from a definite configuration with aligned cuts.
  - C7: the Page fraction moves with an M-dependent emission coefficient.

### 2.2 The chain
1. Conservation follows from bijectivity, which is a premise (Main:66). Solid, but it is an input.
2. Recovery from accessible records: claim A refutes "conservation ⇒ recovery". Solid, exhaustive at small size.
3. The Page value enters only through the Haar ensemble that H-scramble posits (BH-02 C6(b)). The hypothesis fails
   in the stated setting (C6(a)). **The weakest link is H-scramble: open, and false in A.8's own setting.**
4. A.8 (a time average at a fixed cut) → A.9 (a pointwise curve on a moving cut) is open (R11 C.4).
5. Decoupling of D over evaporation: GR:811 is false by ≥57 orders of magnitude (R11 item 8). It is an unstated
   condition of A.9.
6. Page time: Page's formula with β not derived (ch07:143).

The class is **C**, and the conditioning hypothesis is obstructed in its stated setting. The result sits on the
consistency axis, with no empirical confrontation (ch07:159).

### 2.3 Hidden assumptions
R11 (`S/paper/r11/FINDINGS.md`) is adopted. Its independent review was not present.

- **Additional (CONFIRMING).** GR:603 makes the cosmological horizon the only primary partition, so a black hole does
  not change the external observer's trace-out. The Page curve "for an external observer" is therefore a statement
  about a nested sub-partition. The Introduction should keep r4's wording, "the framework's nested-partition
  construction [GR App. A]", and not say "the black hole's radiation".
- **No new physical prediction** distinguishes this account from QES/islands. ch07:147 itself says agreement on the
  Page time "is not established".

### 2.4 Recommendation and the permitted sentences
INCLUDE-MAJOR (about 1.1 pp.); **Q2**. Keep r4 §5.1–§5.4, compressed. Keep §5.3 to two sentences (see §8). The
r4 OWNER markers stand. The section must not land before the R11 site corrections, or it must drop the claim-A
paragraph and its restatements.

> *Permitted (exact).* Under OI, information is conserved in the global reversible dynamics because the dynamics is
> a bijection, which is a premise of the framework. Conservation neither implies nor is necessary for recovery from
> the records an observer can access: finite exhaustive computations exhibit bijections with no accessible advantage
> and non-injective maps with exact recovery [BHa]. In the framework's nested-partition construction the Page value
> enters only through the scrambling hypothesis H-scramble, which no bijection satisfies from a definite
> configuration with configuration-aligned cuts, and whose status for the substratum is open [GR App. A; BHb]. The
> black-hole information problem is not resolved here.

***

## 3. Emergence of quantum mechanics (central theme): INCLUDE-MAJOR (Q1 and Q3)

### 3.1 The precise claim
- Theorem 1, S_K = D_K = Q_K: `finite_horizon_equivalence` (kernel).
- Theorem 2 (kernel, for a joint law; the time-t identification is not checked).
- Theorem 3 (kernel, rooted form).
- Theorem 4, the operational-completion characterization: `exactAll_iff_physical_general` (kernel, both directions).
- `oi_alone_not_qm` (kernel).
- Main's abstract states the maintained strength: "the exact equivalence claim is at the finite observable-law level;
  universal Hilbert-space representability is not promoted into a uniqueness theorem for operational quantum
  mechanics entire."

### 3.2 The chain
- At the kernel layer the chain is Solid: the two directions of Theorem 1, both directions of Theorem 4, and the
  independence result.
- The physical identification of nature with a finite (S,φ,V) is a **hypothesis** (r4 §1.1).
- (C4) at the cosmological cut is **not discharged**: GR:20 says "remains conditional on C4". GR:567 says the
  opposite ("so the equivalence applies in our universe").
- This is a representation result, on the consistency axis.

### 3.3 Hidden assumptions
1. **"Equivalence of QM and embedded observation" (Main's subtitle) is stronger than Main's own abstract and than
   `oi_alone_not_qm`.** r4 cites [Main] under that title. Changing the title is an owner decision. The Introduction's
   text must use "finite-horizon correspondence" and never "equivalence of quantum mechanics".
2. **Universality empties representability of discriminating content.** Markov laws lie in all three classes (r4
   §2.3). This is POSITIVE: r4 already states it.
3. **The measurement-problem reading covers fixed-basis records only** (NEW, see §5).
4. **Prior art not in r4 [mem].** 't Hooft's cellular-automaton interpretation (2016) writes permutation dynamics in
   an "ontological basis" as a unitary; that is the D⊆Q direction in kind. Wetterich, "quantum mechanics from
   classical statistics", is related. Read 't Hooft before r5 claims any priority of viewpoint. The theorem
   attribution in r4 is not affected.

### 3.4 Permitted sentence
Use r4 §2.2 and §6.1 as they stand. For the r5 framing:

> At every finite horizon, the laws an embedded observer of a finite reversible system can record coincide with the
> finite stochastic laws and with the fixed-basis Born laws of finite unitary systems [Main §3.4; machine-checked].
> Exact operational quantum mechanics holds if and only if five completion conditions hold [GR §3.3;
> machine-checked], none of which OI implies. OI therefore does not derive quantum mechanics, and the quadratic Born
> exponent is not selected.

***

## 4. Horizon thermodynamics, ħ and the Bekenstein–Hawking 1/4: INCLUDE-BRIEF, as consistency

### 4.1 The precise claim
- **GR:12 (abstract).** "obtains the Bekenstein-Hawking entropy S = A/(4l_p²) including the 1/4 coefficient by direct
  boundary-mode counting — the three conditional on … H-slope … the counting S = σA/ε² itself unconditional".
- **GR:12, same abstract.** G1 is "horizon-normalization identities and conditional thermodynamic relations".
- **GR:320–322.** The 1/4 is "the ratio 2π/8π … a derived structural constant". "The coefficient is equivalent to the
  Hawking-temperature normalization (T = ħκ/2πck_B plus the first law fixes it)."
- **GR §4.** "a self-consistency condition, not an independent determination … fixes only the ratio ε/√σ = 2l_p".
- **Status surfaces.** G3 (ħ) and G4 (1/4) are C, "conditional calibration" and "no direct test".

### 4.2 Decisive computation (`quarter.py`)
The inputs are taken exactly as GR states them. The two normalization constants are left symbolic:
- the first law dE = c²κ dA/(k₈G), where GR has k₈ = 8π;
- the KMS temperature k_BT_Q = ħκ/(k_Q c), where GR has k_Q = 2π;
- the mode count dS = η dA, with η = σ/ε².

Results:
- **ħ from the calibration T_cl = T_Q:** ħ = k_Q c³ε²/(k₈Gσ), which equals c³ε²/(4Gσ) at GR's constants.
- **S/(A/l_p²) after the calibration:** k_Q/k₈. Here η, σ and ε all cancel. At GR's constants this is 1/4.
- **Control.** η = 1/ε², 7/ε² and 10⁻¹²/ε² each give 1/4. Any mode count whatsoever reproduces the 1/4.
- **Countercontrol.** k₈ = 16π gives 1/8. The coefficient is inherited from the first-law prefactor and the KMS
  period.
- **Hawking's route**, with no mode count at all: dS/dA = dE/(T_H dA) = k_B/(4l_p²).
- **Jacobson's direction**, solving for G: G_eff = c³/(4ηħ), the same relation read the other way (GR:164 says so).

**Verdict.** The 1/4 is put in through the calibration. It is the identity by which the first law plus the Hawking/KMS
temperature fixes the Bekenstein–Hawking coefficient (Hawking 1975 **[mem]**). Given the calibration, S = A/4l_p² holds
by construction for every ε and σ. GR §3.1 already says so ("the entropy law is a fixed point of the construction
regardless").

**What the calibration determines.** One relation, ε/√σ = 2l_p, between two unknowns. ħ is an input; nothing about its
value is predicted.

**Classification.** Under the AGENTS scheme this is not a prediction. It belongs with G14 ("normalization identity").
It sits on the consistency axis. A measured Hawking temperature, such as a primordial-black-hole burst, would test the
standard semiclassical T_H normalization, not OI.

### 4.3 Further hidden assumptions
- **"Classical, no ħ" uses Einstein dynamics.** T_cl is defined through Einstein's first law with 8πG, so classical GR
  is an input (GR Lemma 2/3) while covariant field equations from the substratum (Level G3) are open. The "derivation
  of ħ" therefore presupposes gravity's form.
- **GR:162 is circular.** "Any alternative ħ(ε) would fail at least one of these checks" fails as an argument: the 1/4
  check is satisfied by whatever ħ(ε) the calibration produces. Explainer:477 repeats it.
- **"Historically introduced as a proportionality constant" (GR:320) and "conventionally treated as a postulate"
  (glossary:17)** are historically inaccurate. Bekenstein's 1973 coefficient was undetermined, and Hawking fixed it in
  1975 by the same first-law-plus-temperature identity **[mem]**.

### 4.4 Recommendation and the permitted sentence
INCLUDE-BRIEF (about 0.5 pp.); **Q2**, as a consistency relation. It must not be listed among predictions.

> *Permitted (exact).* Applied to the cosmological horizon, OI identifies the classical horizon temperature
> obtained from the first law, dE = c²κ dA/(8πG), with the KMS temperature ħκ/(2πck_B) of the emergent description of
> the same boundary modes. Under the infrared detailed-balance condition H-slope and the horizon and frame conditions
> of [GR §§2–3, §8.5], this calibrates ħ = c³ε²/(4Gσ) against the discreteness scale ε and the entropy σ per
> boundary mode; it fixes only ε/√σ = 2l_p. With that calibration the boundary-mode count σA/ε² equals A/(4l_p²) for
> every ε and σ. The coefficient 1/4 is the ratio 2π/8π of the two normalizations, the same relation by which the
> Hawking temperature fixes the Bekenstein–Hawking entropy. The result is therefore a consistency relation between
> the classical and emergent descriptions, not a prediction, and has no independent empirical test.

***

## 5. Brief candidates

**Measurement problem and wavefunction: one outlook line (Q3).**
- Main:666 says "the Everettian measure problem dissolves". ch19:333 says "Dissolved (Bayesian updating)".
- **Hidden assumption (NEW).** Q_K measures one fixed basis at every step. Coherent preparations and noncommuting
  interventions, which is where the measurement problem lives, need conditions (i)–(v) of Theorem 4. OI does not imply
  those (`oi_alone_not_qm`).
- The "dissolution" therefore covers fixed-basis records only. Permitted: the sentence in the table, labelled an
  interpretation.

**Born probabilities: Q3.** Keep r4 §2.3: the exponent is not selected. F7 ("Born rule transient violations") is a
conditional prospect with no derived form (appendix-a:185). EXCLUDE it.

**Bell: Q3.** Keep r4 §6.4(5): H-Bell is open. No application.

**Arrow of time: Q2, one line, or EXCLUDE.**
- Main §4.6 gives the theorem conditional on (EM) and on the rate condition τ_mix ≪ τ_S.
- **Hidden assumptions (NEW).**
  - Substratum:356 says "No additional axiom is needed", but the cascade rests on (EM), which Main calls "an explicit
    physical hypothesis".
  - The "horizon clock" is monotone only while ä > 0 (Substratum:354). It does not cover the decelerating era, in
    which the thermodynamic arrow already existed.
- Permitted: the table sentence. Nothing about "deriving" the arrow.

**Dark sector: EXCLUDE from the main text.**
- a₀ = cH/6 has its factor imported from Verlinde.
- The 95% is "by construction" (GR:358, G9).
- Q = M_Bc² is part of the open coupling step.
- Two observational tensions are on record (GR:12).
- ch00:89 calls a₀ "a parameter-free prediction". That is an overclaim (§9).

**Information loss and thermodynamics, recovery vs accessibility.** Both fold into §2.

**Quantum computing and cosmological initial conditions: EXCLUDE.**

***

## 6. Structural SM predictions: the Cabibbo form (owner criterion 1)

### 6.1 The chain (SM:833–851)
| # | Link | Grade |
|---|---|---|
| 1 | Cubic lattice, d = 3 | Empirically anchored, not derived: "forced by the observed gauge group" (SM:16). The generation reading is under H-link (and H-spin') |
| 2 | Adjacent T₁ corner distance π√2 | Solid geometry |
| 3 | A 1/\|q\| power, from chirality preservation of the taste-changing vertex | Solid (staggered-fermion literature; prose) |
| 4 | Mixing element = propagator magnitude at the inter-corner momentum, with unit prefactor (c_λ = 1) | SM:849 says "a hypothesis, not a derivation". SM:849–851 then claims the unit prefactor is an algebraic identity of the spin–taste map, with a finite witness, and "emergent dressing pending" |
| 5 | Choice of the adjacent-corner distance "rather than another invariant of the same corner set", and of the emergent continuum dispersion over the substrate kernels | **Selected.** The boson kernel's 1/(2√2) = 0.3536 was rejected as "excluded by the measured Cabibbo angle at ≈190σ" (SM:851) |

The weakest link is 4 or 5: Motivated, with the dressing open. Under AGENTS, S requires every link Solid, so the class
is **C** (conditional on the emergent dressing, H-link and the cubic commitment). appendix-a:74's S is too strong.

### 6.2 Parameter dependence and history (`git log -S`, `S/ppe/repo`)
- The form `\lambda = 1/(\pi\sqrt{2})` and its comparison "0.2250 ± 0.0007, 0.04%" first appear **together** in
  `054eb99a` (2026-04-04, `Predictions.md`). The repository begins 2026-02-12. No pre-comparison registration exists in
  the repository.
- The c_λ hypothesis and the dispersion discrimination (boson kernel rejected against data) first appear in
  `70ffe82f`/`3124ef0a` (2026-07-05/06), three months after the comparison.
- λ has been measured since Cabibbo 1963.
- **Classification.** A postdiction, with one alternative form discarded against data and the unit prefactor adopted
  as a commitment before it was given a structural argument.
- **Look-elsewhere (`lookelse.py`).** The family is (a/b)·π^k·√r^s with a,b ≤ 12, k ∈ {−2,…,1} and r ∈ {1,2,3,5,6}.
  It has 752 distinct values in [0.1, 0.5]. Six land within 1σ of 0.22500; about 2.5 are expected by chance in a ±1σ
  window. 1/(π√2) is the simplest of them.
  - Reading: the agreement is notable for so simple a form, but it is not by itself strong evidence.

### 6.3 Numerical agreement
- SM cites λ = 0.22500 ± 0.00067 (PDG-2022 global fit), giving 0.12σ.
- A CKMfitter 2023 update gives λ ≈ 0.22498 at about 0.1% **[web, abstract snippet only]**.
- The global fit imposes CKM unitarity.
- Direct |V_us| determinations from Kℓ3 and Kμ2 disagree at about 3σ (the Cabibbo-angle anomaly) **[web]**. Agreement
  with 0.22508 therefore depends on which determination is used. Not verified first-hand; the PDG site was
  unreachable from this container.

### 6.4 Independent predictions
None is pre-registered for λ itself. The related JUNO sin²θ₁₂ value (§7) uses λ² and is the one forward exposure.

### 6.5 Recommendation
At most one outlook line (**Q3**), with the permitted sentence in the table. Do not quote "0.04%" or "0.12σ" without
"postdiction". Koide Q = 2/3 is Koide's 1981–83 empirical relation, and λ(M_Pl) = 0 is the Shaposhnikov–Wetterich 2010
boundary condition, with the Higgs measured in 2012 **[mem]**. Both are postdictions of known relations; EXCLUDE them.

***

## 7. Other candidates the corpus supports better

1. **JUNO sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798: one outlook line (Q3).**
   - It is the only quantitative item with a stated falsifier ahead of data (Juno:409): a JUNO design-lifetime
     disagreement at 2σ, with precision ±0.0014.
   - The form first appears in `054eb99a` (2026-04-04), after JUNO's first result (Nov 2025). The central-value
     agreement (0.07σ) is a postdiction (Juno:73 says so). Only the precision test is forward.
   - The value depends on the Wilson-coefficient ratio 4/3. The natural spurion does not produce that ratio
     (appendix-a footnote ᶠ). The class is L.
   - **Undetermined:** whether 4/3 was selected with the measured angles in view. Its history was not traced in this
     audit.
   - The exact sum rule 2sin²θ₁₂ + sin²θ₂₃ = 7/6 follows. Checked: 2(1/3 − 1/4π²) + 1/2 + 1/2π² = 7/6. It is a
     sharper, form-level falsifier and shares the same ratio dependence.
2. **The Page-time β.**
   - β is not derived (ch07:143: "how much state-space entropy the radiation acquires per boundary mode lost is
     open").
   - The fraction formula is Page 2013 Eq. (8). At the mode-count value β = 1 it gives 0.646, and Page's β ≈ 1.485
     gives 0.538.
   - No framework-specific test exists, and ch07:161 ("a sharp prediction once β is derived") is a promissory note.
   - **Not an application.** Keep two sentences in §2 as an open input.
3. **PE-01, deterministic randomness: INCLUDE-BRIEF (Q2), as a scope result.**
   - It is a verified bounded counterexample (exact enumeration, 78/78 jobs, replay byte-identical) to the universal
     statement formerly at ch18:114, now rescoped on `main` by #933.
   - The witness: `G_clk`, n = 5, z⁵ + z² + 1; an active observer with m = 2 memory bits; K = 7; advantage 1/8, 5/32,
     5/32, 1/8 over K′ = 4..7.
   - No passive witness exists in the enumerated scope.
   - Literature: covered in kind by Gomułkiewicz–Kutyłowski–Wlaź 2006 (a clock-control fault attack, outline only), and
     the passive horizons by AGHP 1992's mechanism (annex `TAGS-r2.md`; recheck "ACCEPT WITH NITS").
   - **Blocker:** the package lives only on `research/oi-pseudoentropy-20261025` (`efbfd0d7`), not on `main`. Under
     §A.42 the paper may cite it only after it lands. It must be framed as validation of scope, not as a novel
     prediction.
4. **DESI ν.** G8 is L. The predicted |ν| ~ 10⁻³² is "indistinguishable from zero", which is ΛCDM's own prediction. The
   corpus's falsifier is a confirmed phantom crossing (appendix-a:209). This exposes the framework but does not
   discriminate it from ΛCDM. EXCLUDE.
5. **Memory and indivisibility results (Theorems 2 and 3).** These are the framework's strongest supported content, and
   they are already in r4. One structure-level forward item exists in the corpus: memory-witness experiments. GR:601
   and Main §4.5 say no falsifying constraint is established, so it is not an application.
6. **Gravitational-wave echoes. EXCLUDE (contradictory corpus).** GR:603 says the framework predicts "no OI-specific
   echo" and reports a null stack. ch18:164–180 and appendix-a F5 list echoes as a forward prediction. See §9.

***

## 8. Assumption-watch markers (§A.31 output classes)

This was one depth-first pass per candidate. The fixed point (3–4 passes with no NEW finding) was not reached.

| Marker | Finding | Class | Propagates to |
|---|---|---|---|
| AW-1 | 1/4 = k_Q/k₈ for every η; the count does not supply it | ELABORATING (GR §3.1 has it; the headlines contradict it) | G4, row 24, ch00, preface, glossary, ch07:12/104, GR:12/320/322/707 |
| AW-2 | CC "gauge offset" argument restates the premise; all content is the G3 coupling step | NEW | GR:583, ch07 §7.7, ch19:330, ch02:192 |
| AW-3 | The relative/absolute rule does not classify phase-transition vacuum energy | NEW | GR §8.3 |
| AW-4 | ρ ~ H²/G is the Friedmann normalization of the total density | NEW | GR:366, ch07:195, Explainer:549, GR:358 item (1) |
| AW-5 | 10¹²² = (8/3)·S_dS is dimensional | CONFIRMING | GR §6.3, ch07 §7.7 |
| AW-6 | "G3" names three different objects | NEW (editorial) | Introduction; any cross-document citation |
| AW-7 | The measurement-problem dissolution covers fixed-basis records only | NEW | Main:666, ch19:333 |
| AW-8 | The arrow cascade needs (EM) and covers only the ä > 0 era | NEW | Substratum §5.4 |
| AW-9 | The S class conflates "parameter-free" with "predicted before measurement"; the scheme has no postdiction marker | NEW (methodology) | every S row of appendix-a; SM §7.6 |
| AW-10 | Cabibbo agreement depends on the λ determination (unitarity fit vs direct \|V_us\|) | NEW, unverified | appendix-a:74, :217 |
| AW-11 | R11 items | CONFIRMING | per FINDINGS.md §D |
| AW-12 | Echo prediction contradicts across GR and the book | NEW | GR:603, ch18 §18.6, appendix-a F5 |
| AW-13 | PE-01 is not on `main` | Retention blocker | r5 |
| AW-14 | JUNO value rests on an underived 4/3 ratio | ELABORATING | Juno.md, N1/N3/N6 |

***

## 9. Overclaims to queue for the manuscript-consistency change (not edited here)

Mirrors were checked by full-line `grep -nxF` against FULL.

**Horizon entropy and ħ (AW-1)**
- GR:12: "by direct boundary-mode counting" → "by the calibration of §3 (a consistency relation)".
- GR:162 and Explainer:477: the circular "Any alternative ħ(ε) would fail …". Remove.
- GR:320: "historically introduced as a proportionality constant — is here fixed".
- GR:322 and ch07:104 (FULL:1981): "a derived structural constant".
- GR:707: "follows by direct mode counting … a structural constant rather than an empirical fit".
- ch07:12 (FULL:1889): "derives … by direct boundary-mode counting".
- ch00:21 (FULL:257) and preface:7 (FULL:78): "becomes a derivation rather than a postulate".
- ch00:81 (FULL:317): "obtains the 1/4 factor from mode counting".
- ch00:89 (FULL:325): "the 1/4 factor as a derivation".
- glossary:17 (FULL:6639): "conventionally treated as a postulate … The framework derives the 1/4 factor as a
  structural consequence of mode counting".
- appendix-a:110 (G4, FULL:5663) and :93 (row 24): "C … No direct test" → reclassify as an identity, as G14 is.

**Cosmological constant (AW-2, AW-4)**
- ch07:167 (FULL:2044): "The framework dissolves the problem rather than solving it". §7.7's body never states the
  covariant-coupling condition that ch07:14 (FULL:1891) and GR:356 state.
- ch07:201 (FULL:2078) and GR:360: "eliminates the 122-digit cancellation entirely", unconditional.
- GR:356, last two sentences: "never enters the stress-energy tensor; no decoupling mechanism is needed". This
  assert-then-qualifies against the same paragraph (§A.30).
- GR:366, ch07:195 and Explainer:549: "not a prediction awaiting future data … the value the framework expects" /
  "independent reason to expect".
- GR:583: "it is a theorem of the reconstruction … attributes physical content to a gauge degree of freedom". This
  contradicts GR:356.
- GR:24: "is dissolved by …", then qualified (§A.30 pattern).
- ch02:192 (FULL:835): "The cosmological constant problem dissolves:", unconditional.
- ch19:330 (FULL:5506): "Dissolved (10¹²² = S_dS)" → "Conditional (covariant coupling)". ch19:38 (FULL:5214) is the
  anchor.
- Explainer:533: "Now the cosmological constant problem dissolves."
- GR §6.3 and ch07 §7.7: "a triangulation that strengthens the empirical case for both programs" (§A.32
  self-assessment; no empirical content).
- appendix-a:113 (G7, FULL:5666) and :119 (G14, FULL:5672): class S for a descriptive relation and a normalization
  identity. Neither is a prediction.

**Emergence of QM and scope**
- GR:567: "so the equivalence applies in our universe" contradicts GR:20 ("conditional on C4 … not presently
  discharged").
- GR:711: "establishes that the Standard Model, general relativity, and the arrow of time are three faces … with quantum
  mechanics emerging as the unique self-consistent description for any observer bounded by a causal horizon" and
  "[Main] establishes the equivalence between embedded observation and quantum mechanics". This contradicts
  `oi_alone_not_qm`, Main's abstract and the open G3.
- Main title: "The Equivalence of Quantum Mechanics and Embedded Observation". Owner decision; the Introduction cites
  it.
- ch19:333 (FULL:5509): "Measurement problem | Dissolved (Bayesian updating)" (AW-7).
- Main:666: "The Everettian measure problem dissolves" (interpretive, same scope issue).
- Substratum:356: "No additional axiom is needed" (AW-8).

**Counts and evidential summaries**
- ch18:349 (FULL:5169): "Twenty-two parameter-free Standard Model predictions match observation. Thirteen
  gravitational-sector predictions match observation." This contradicts appendix-a:95, :121 and :231 (7 S of 22; 2 S +
  9 C + 2 L gravitational, several with no test).
- ch19:362 (FULL:5538): "preregistered structural predictions matching observation" contradicts appendix-a:217 ("no
  pre-registered forward confirmation").
- ch19:28 (FULL:5204): "seven independent consistency checks and no fitted parameters". GR:358 itself says item (7)
  includes three matched parameters and that the "<0.1% figures are fits".
- ch19:339 (FULL:5515): "Dark sector budget | Derived (total budget)" vs G9 (C, "partly definitional").
- GR:709: "The dark-sector corollary explains ~95%" (partly definitional).
- ch00:89 (FULL:325): "the MOND scale a₀ = cH/6 as a parameter-free prediction"; the factor is imported (GR:12, G6).
- ch19:336 (FULL:5512): "Hierarchy problem | Dissolved (lattice is UV)". Outside this audit's scope; flagged only.

**Classification**
- appendix-a:74 (FULL:5627), Cabibbo S: the AGENTS S definition needs every link Solid. SM:851 says "emergent dressing
  pending", and the dispersion was selected against data. Proposed: C, with a postdiction marker (AW-9). The same
  question applies to rows 6, 10, 11, 13 and 22. Not audited here.

**Echoes (AW-12)**
- GR:603 ("no OI-specific echo"; null stack) against ch18:164–180 (FULL:4984 ff.) and appendix-a:183 (F5) and :208.
  One side must be corrected.

**Black hole (R11, adopted)**
- ch07:110/1987, ch07:126/2003 (s1, s2), ch07:159–161/2036–2038, ch18:146/4966, ch18:158/4978, ch19:334/5510, GR:811,
  GR:869, and the conditions-level item ch18:148/4968.
- Paraphrases per FINDINGS §D: ch07:12, ch09:108, ch07:118 heading, GR:611, glossary:113, ch07:132, ch07:151, GR:871.

After any of these edits: re-grep the counts corpus-wide (§A.25) and regenerate or flag `GR.tex/.pdf` and
`FULL.tex/.pdf`.

***

## 10. Page budget for r5 (about 13 main-text pages)

| § | Content (question) | Pages | Kept qualifications |
|---|---|---|---|
| 1 | The central idea: (S,φ,V), the OI hypothesis, the contributions paragraph (Q1) | 1.0 | Hypothesis, not established; finiteness posited; no new theorem claimed for Thms 1–4; a short note that the applications are reported from [GR] and [BHa/b] |
| 2 | Mathematical foundation: Theorem 1 with its attribution, scope (Markov laws, Born exponent, periodicity), Theorem 2 with corollary and bounds (Q1) | 2.25 | Each theorem with its hypotheses, verification layer and reference; Appendix A declarations |
| 3 | Indivisibility from recurrence: Theorem 3, readback ⇒ indivisible somewhere, the three notions kept apart (Q1) | 1.25 | Rooted form machine-checked; history-level (C4) on paper; global, not short-window |
| 4 | Examples: minimal model (§4.1) and card table (§4.3); §4.2 as one paragraph (Q1) | 0.75 | The card game is classical on card inputs; Bell-local |
| 5 | **Applications and Potential Resolutions** (Q2) | **4.0** | |
| 5.1 | The cosmological constant: a conditional proposal | 1.3 | §1.5 sentence; Λ value an input; the phase-transition item; the S_dS identity labelled dimensional |
| 5.2 | Black-hole information: conservation vs access, the Page entropy via H-scramble, Page time in two sentences, open steps | 1.1 | §2.4 sentence; R11 gates; toy-model scope |
| 5.3 | Horizon thermodynamics: ħ calibration and the 1/4 as a consistency relation | 0.5 | §4.4 sentence; H-slope and the horizon/frame conditions; ε/√σ only |
| 5.4 | Deterministic sources and embedded prediction (PE-01) | 0.3 | Bounded witness; covered in kind; only after landing on `main` |
| 5.5 | Outlook lines: arrow of time (EM); measurement reading (fixed-basis only); SM closed forms as postdictions; JUNO precision test (L) | 0.8 | One sentence each, with its condition |
| 6 | What remains to be proved (Q3): operational completion (Thm 4 and independence), relating evolution, no fixed finite carrier, Born exponent, Bell (H-Bell), gravitational coupling (covariant field equations), distinguishing experiments (memory witnesses: no constraint yet) | 2.5 | All of r4 §6.1–§6.4 |
| 7 | What is not claimed, and conclusion | 0.75 | r4 §6.5 items 1–6, plus: no prediction of Λ's value; the 1/4 is not a prediction; no SM value is a pre-registered prediction except the JUNO precision test |
| | **Total** | **12.5** | 0.5 pp. slack for displays. Code/data, Appendix A and references are outside the count |

Compression sources against r4:
- §4.1–§4.3 go from about 1.5 pp. to 0.75.
- §5.3 Page time goes from 0.4 pp. to two sentences.
- §5.4's item-F paragraph goes from 0.25 pp. to one sentence, pending R11 at GR:811.

Theorems 1–4 keep their full statements, hypotheses, verification layers and references.
