# Introduction paper: outline, revision 5 (design stage, for owner review)

**Stage.** This is a design for r5, authorized by the owner on 2026-10-26. It contains no paper text. Each claim is
given the sentence the draft must use, or the r4 sentence it must carry, together with its source and its
verification layer. Nothing in the repository was changed.

**Baseline.**
- `S/paper/draft/Introduction-r4.md`, sha256 `5f9fdcc5…68f6`, accepted. "r4:N" means line N of that file.
- Q1 and Q3 content reuses r4's reviewed sentences. Where this outline says "verbatim", the draft copies the r4
  text unchanged.

**Sources.**
- `main` at `687e885b`; "GR:N", "Main:N" and so on refer to that commit.
- The applications audit, `S/paper/apps/AUDIT.md` (its scripts `quarter.py` and `cc.py` were re-run here and
  reproduce the audit's numbers).
- The black-hole corrections, `S/paper/r11/FINDINGS.md` as amended by `S/paper/r11/REVIEW.md`. **REVIEW.md governs**
  wherever the two differ.
- The PE-01 package on `research/oi-pseudoentropy-20261025` at `efbfd0d7` (#923), which is not on `main`.

**Claim IDs.** New claims are numbered `N-…` and registered in `CLAIMS-r5.md`. Claims carried from r4 are cited
by r4 line.

**The owner's aim.** "Ambitious in its scientific implications but conservative in its claims", organized by three
questions:
- **Q1.** What is OI?
- **Q2.** What might it explain?
- **Q3.** What remains to be proved?

## Page budget

r4's main narrative is about 4,600 words on 12 pages of the repository default format, or about 385 words per page
with its displays. The budget below assumes the same density.

| § | Title | Tag | Words | Pages |
|---|---|---|---|---|
| — | Abstract | Q1–Q3 | 220 | 0.6 |
| 1 | The central idea | Q1 | 390 | 1.0 |
| 2 | Mathematical foundation | Q1 | 870 | 2.25 |
| 3 | Indivisibility from recurrence | Q1 | 480 | 1.25 |
| 4 | Two examples | Q1 | 200 | 0.5 |
| 5 | **Applications and Potential Resolutions** | Q2 | 1,540 | **4.0** |
| 5.0 | Lead and status key | | 80 | 0.2 |
| 5.1 | The cosmological constant: a conditional proposal | | 540 | 1.4 |
| 5.2 | Black-hole information: preservation and accessible recovery | | 420 | 1.1 |
| 5.3 | Horizon thermodynamics: a consistency relation | | 190 | 0.5 |
| 5.4 | Deterministic sources and embedded prediction (gated) | | 110 | 0.3 |
| 5.5 | Further readings | | 200 | 0.5 |
| 6 | What remains to be proved | Q3 | 1,050 | 2.7 |
| 7 | What is not claimed; conclusion | Q3 | 340 | 0.9 |
| | **Main text** | | **≈5,090** | **≈13.2** |
| — | Code, data and formal verification; Appendix A (declarations); Appendix B (the card table); references | | outside the count | ≈3.5 |

- **Fallback if the build runs over 13.5 pp.** Cut §5.5 to its first two items. Do **not** cut any qualification
  listed below. That would breach the owner's rule never to weaken an essential qualification to meet the page
  target.
- **If §5.4 is not yet citable** (PE-01 not on `main`), drop it and give its 0.3 pp to §5.1.

## Section plan

Each section gives its purpose, its claims with their wording, source and layer, and what it explicitly does not
claim. Layers are:

| Code | Layer |
|---|---|
| K | Lean kernel (machine-checked) |
| P | written proof (proved on paper) |
| E | exhaustive finite computation or exact probe |
| A | exact algebra |
| N | numerical |
| L | literature |
| I | interpretation |
| O | open |

### Abstract (Q1–Q3, 220 words)

The abstract is new, because the scope changes. It has one or two sentences per question, each built from the
permitted sentences below and no stronger than they are.
- **Q1.** r4:12, sentences 1–3: the hypothesis, the coincidence of the three classes, and the known components.
- **Q2.** The cosmological constant as a proposal conditional on the open covariant field equations (N-CC2). Black
  holes as preservation versus accessible recovery, with the information problem stated as not resolved (N-BH1, N-BH3).
- **Q3.** The open list: operational completion, the Born exponent, Bell (H-Bell), gravitational coupling, and the
  absence of an experimentally distinguishing prediction (N-EX1).

**Must not contain:** "dissolve(s)", "resolve(s)" without "potential" and a stated condition, any number presented as
a prediction, "derivation of quantum mechanics".

**Owner markers.** The abstract's R11 marker, r4:14, is carried with the R11 status of `DEPENDENCIES-r5.md` §D.

### §1 The central idea (Q1, 1.0 pp)

**Purpose.** State the hypothesis and the paper's three questions, define terms, and set the contributions
paragraph.

**§1.1 Embedded observation.** r4:20–26, verbatim (r4 §1.1 as reviewed).

**§1.2 Three questions.**
- **New lead sentence (N-INT1).** "The paper asks what OI is (§§2–4), what it might explain (§5), and what remains
  to be proved (§§6–7)." This is structural only.
- **Contributions.** r4:32 verbatim, with one change. Its black-hole sentence is replaced by N-INT2:

  > The applications of §5 are reported from [GR] and from unpublished repository computations [BHa; BHb] whose
  > novelty has not been established; each is stated with its conditions, and none is claimed as a new physical
  > result.

  This keeps r4's reviewed novelty clause.
- **Positioning sentence (N-LIT1),** placed after r4:72's Calvo sentence in §2.2, not here.
- **Conventions.** r4:34 verbatim. Its decision-2 OWNER marker (r4:36) is carried.

**Does not claim:** a new theorem; novelty of the viewpoint (see N-LIT1); that OI is established or tested.

### §2 Mathematical foundation (Q1, 2.25 pp)

**Purpose.** The three classes, Theorem 1, its scope, and Theorem 2 with its corollary.

r4:40–100 are carried **verbatim**, with these exceptions:
- The §2 lead sentence (r4:42) is kept.
- **The Attribution paragraph (r4:70) and the Calvo sentence (r4:72) are kept.** After them, add N-LIT1 (one
  sentence):

  > 't Hooft has argued that quantum mechanics may serve as a tool for analysing a system that is classical at its
  > core, and has discussed how such a view can be reconciled with Bell's theorem [tH14].

  This is taken from the arXiv abstract of 1405.1548v3, read first-hand on 2026-10-26; the body was not read.
- **Permitted trim (presentation only), if needed for length:** the two Realization sentences r4:66 s2–s3
  (the step mechanics) may be cut to one. The hypothesis-carrying sentences may not be cut: the record makes the
  step injective; the prior-independent form exists, proved on paper with exact probes.

**Theorems carried without change** (statement, hypotheses, reference, verification layer, witnesses):
- **Theorem 1** (r4:58–64): K, `finite_horizon_equivalence` and its three directions.
- **Theorem 2** (r4:86–92): K for a joint law. The time-t identification is not machine-checked (r4:92).
- **The Corollary** (r4:94): P.
- **The capacity bound** (K) and the **Pinsker bound** (P with exact probes), r4:96.
- **(C1)–(C4)** (r4:98).

**Does not claim:** that representability distinguishes memory (r4:76); selection of the Born exponent (r4:78);
an all-time realization (r4:80).

### §3 Indivisibility from recurrence (Q1, 1.25 pp)

r4:102–124, verbatim.
- **Theorem 3** (r4:110): K, rooted form.
- **Readback forces indivisibility** (r4:114): machine-checked from the routed-readback form [Main §1.3, the
  realization clause of (C4)]; from history-level (C4) proved on paper.
- **The three notions** (r4:118–120).
- **Theorem 1 as a representation result** (r4:122).

**Permitted trim:** none. This section carries the sci-N2 correction and §A.34 witnesses.

**Does not claim:** short-window indivisibility; an identification of P-indivisibility with quantum
non-Markovianity.

### §4 Two examples (Q1, 0.5 pp)

**§4.1** is r4:130–139 verbatim. **§4.2** is r4:141–143 verbatim. One closing sentence points to Appendix B:

> A two-card game with a hidden burn card realizes Theorem 3 with the smallest alphabet; it is worked in Appendix B,
> with its classical and quantum scope.

**The card table moves to Appendix B,** r4:145–166 verbatim, keeping the RC-2/ERRATUM-r4 decomposition statement.
Non-claim 6 (§7) still points to it. This is the owner's "detailed technical material in an appendix where
practical". It saves about 0.9 pp and loses no qualification.

**Does not claim:** that the card game is quantum.

### §5 Applications and Potential Resolutions (Q2, 4.0 pp)

The title is fixed by the owner. **Never** "Solved Problems", "Dissolutions" or "Predictions".

**§5.0 Lead and status key (80 words; N-INT3).**

> Each application below is stated with the conditions it rests on. A *consistency relation* follows from the
> framework's own calibrations and has no independent test; a *numerical agreement* matches a value measured before
> the framework's expression was written; an *independent prediction* is a value stated before comparison with data.
> The applications in this section are proposals and consistency relations; §6.7 lists the one quantitative item
> with a stated test ahead of full-precision data.

#### §5.1 The cosmological constant: a conditional proposal (Q2, lead application, 1.4 pp)

**Purpose.** This is the owner's leading application, given the most space. It is stated as a proposed resolution,
explicitly conditional on the open covariant field equations.

The paragraph order and claims are as follows.

1. **The problem (N-CC0).** This is standard background, with no framework claim.

   > Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density about
   > 10¹²² times the observed one; if that density sources curvature, it must be cancelled to that accuracy.

   - The number is the audit's `cc.py`: ρ_P/ρ_crit = 6.0×10¹²² at H₀ = 67.4.
   - Layer: A + N.
2. **The two levels (N-CC1).** This is the audit's permitted sentence §1.5, sentences 1–2, verbatim:

   > In OI the zero-point sum of the emergent quantum description and the effective cosmological constant belong to
   > different levels of description. A uniform shift of the emergent Hamiltonian changes no visible transition
   > probability, so the quantum description assigns the zero-point offset no observable content [GR §6.2].

   - Source: GR:356, "Quantum transition data are invariant under Ω_eff→Ω_eff+CI (a global phase)".
   - Layer: A (one line).
   - **The required qualifier follows immediately (AW-2):**

     > The invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum
     > energy; the proposal's content lies in how the two levels couple to geometry.
3. **Why it is conditional (N-CC2).** This is the audit's §1.5, sentences 3–5, verbatim, followed by GR:356's
   two-completion observation (N-CC3):

   > Whether the offset also fails to source curvature is a separate coupling question. Settling it requires
   > covariant field equations derived from the substratum, with their coupling to sources, which are open [GR §6.2].
   > Two gravitational completions, $\mathcal G_{\mu\nu}=8\pi G\,T^{\rm cl}_{\mu\nu}$ and
   > $\mathcal G_{\mu\nu}=8\pi G\,(T^{\rm cl}_{\mu\nu}-\rho_C\,g_{\mu\nu})$, can share the same substratum, partition,
   > visible law, fixed-basis representation and action-scale calibration while differing in exactly that offset
   > [GR §6.2]. The proposal that the 10¹²² mismatch requires no cancellation is therefore conditional on that open
   > step.

   - Sources: GR:356 for the two completions and "Invisibility to quantum mechanics is not decoupling from gravity";
     GR:12 for the dependency ladder.
   - Layer: I + O. The two-completion statement is a prose observation in GR.
   - **Naming rule (AW-6).** Write "the covariant field equations and their coupling to sources (Level G3 of [GR])"
     at first use, then "the covariant field equations". **Never** write a bare "G3".
4. **What the proposal would give, and what it would not (N-CC4, N-CC5).**
   - If the covariant field equations take the form [GR] targets, $E_{\mu\nu}[g,\mathrm{OI}] = 8\pi G\,(T_{\mu\nu}
     - \mathcal F[g,T]\,g_{\mu\nu})$ with the classical stress-energy of the substratum as source (GR:12), the
     zero-point sum of the emergent description is not a source and no cancellation is required. This is a
     conditional statement, layer I + O.
   - Then, verbatim from the audit's §1.5:

     > It does not explain the observed value of Λ, which enters as a cosmological input.

     Source: GR:360, "set by initial conditions via the Friedmann equation".
   - Plus the scale qualifier (AW-4, N-CC5):

     > The scale ρ ~ H²/G is the Friedmann normalization of the total density, and the fraction carried by Λ is an
     > input.

     Layer A (`cc.py`).
5. **The 10¹²² number (N-CC6).** The audit's §1.5 last sentence, verbatim:

   > With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a factor of order one; this is a
   > dimensional identity, not an independent prediction.

   - Exact factor: (ρ_cut/ρ_crit)/S_dS = (8/3)(l_p/l_cut)⁴ (`cc.py`).
   - Layer A.
6. **Phase transitions (N-CC7).** The audit's permitted sentence, verbatim:

   > How the energy of electroweak and QCD vacuum transitions couples to gravity is not fixed by the descriptive
   > distinction and requires the same open coupling step.

   - GR:581 classifies the Higgs shift as not gravitating. r5 does not repeat that classification (AW-3).
   - Layer O.
7. **Related proposals (N-LIT2).** One or two sentences, at the strength of the abstracts read:

   > Removing the vacuum energy of matter as a source of curvature is also the aim of the trace-free Einstein
   > equations, which leave the observed value of Λ unexplained [EvEMU11], and of vacuum-energy sequestering, which
   > extends to the vacuum energy of phase transitions [KP14]; Volovik argues from the thermodynamics of quantum
   > many-body ground states that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]. The present
   > proposal differs in locating the gravitational source in the substratum microstate, and its coupling step is
   > open.

   - Layer: L, abstracts only (VERIFY on each).
   - "Differs in locating …" is a description of the proposal, not a priority claim.
8. **What would settle it (N-CC8).**

   > A derivation of the covariant field equations, with their conservation and source coupling, from the substratum
   > would turn the proposal into a theorem or refute it (§6.6).

   Source: GR:12, which lists field equations, stress-energy coupling, Bianchi structure and the continuum limit as
   the named open items. Layer O.

**Does not claim:**
- "dissolves" or "dissolution";
- "no decoupling mechanism is needed" (GR:356, last sentence; see `DEPENDENCIES-r5.md`);
- "eliminates the 122-digit cancellation";
- "the value the framework expects";
- ρ ~ H²/G as an output;
- a prediction of Λ or of Ω_Λ;
- any convergence or strengthening language about the de Sitter literature;
- that the gauge argument (GR:583) settles the coupling.

#### §5.2 Black-hole information: preservation and accessible recovery (Q2, 1.1 pp)

**Purpose.** r4 §5, condensed, with its status aligned to R11 REVIEW.md.

1. **Setting.** r4:172, verbatim, minus its "checked exhaustively" sentence. That sentence moves into item 4.
2. **Conservation versus access (N-BH1).** The audit's §2.4 sentences 1–2, verbatim:

   > Under OI, information is conserved in the global reversible dynamics because the dynamics is a bijection, which is
   > a premise of the framework. Conservation neither implies nor is necessary for recovery from the records an
   > observer can access: finite exhaustive computations exhibit bijections with no accessible advantage and
   > non-injective maps with exact recovery [BHa].

   - Sources: Main:66 (the premise); BH-01 REPORT:17 and :36 (claim A); ch19:72 (the scoped anchor).
   - Layer: E.
   - Then r4:181's counts sentence, cut to its first clause and the bound: "Of the 40,320 bijections of {0,1}³,
     1,376 give zero accessible advantage …; with $\mathcal U$ inaccessible $P_{\rm succ}\ge1/|\mathcal U|$". Keep
     "The endpoint guarantees above are sufficient, not necessary" and the [Sha79] sentence, with Sha79's VERIFY.
3. **Where the Page value enters (N-BH2).** r4:185 and r4:188–190, compressed to two sentences, keeping C6(a),
   C6(b) and C6(c):

   > In the framework's nested-partition construction the Page value enters only through the scrambling hypothesis
   > H-scramble, which no bijection satisfies from a definite configuration with configuration-aligned cuts [BHb,
   > C1, C6(a)–(b)]. On an energy shell the Haar-typical value differs from the Page value $S_{\rm Page}(d_B,d_R)$,
   > in a direction that depends on the shell [BHb, C6(c)].

   - Source: BH-02 REPORT:14, :18–20.
   - Layer: P + E.
   - This is the necessity form, which REVIEW §4 O-1 permits.
4. **Status of the Page curve (N-BH3).** This sentence **replaces** any sufficiency form. It agrees with REVIEW.md
   §1 C.4, §1 item 8 and §4 O-1:

   > The Page curve of [GR App. A] is a conditional result. Its stated hypothesis H-scramble is open; it also
   > assumes that the sector beyond the cosmological horizon stays decoupled from the black hole and its radiation
   > over the evaporation, which timescale ordering does not supply, since $t_{\rm evap}/\tau_B^D \ge 10^{57}$ at 30
   > solar masses over the assumed parameter intervals [BHa, item F]; and what the cycle-typicality argument
   > supplies is a time average at a fixed bipartition, so the pointwise curve along one trajectory is open [BHb,
   > C6(d)]. The black-hole information problem is not resolved here.

   - Sources:
     - GR:817 and :841 (labels);
     - GR:811 (the false decoupling inequality; R11 item 8, confirmed);
     - BH-01 REPORT:211–241 (item F);
     - BH-02 REPORT:21 (C6(d)); REVIEW.md §1 C.4 ("SITE-ERROR (proof scope)").
   - Layers: E (item F intervals), P (C6(a)), O.
   - The R2-3 non-claims are carried as one clause in §7 item 4: no claim that information reaches D, that [GR,
     Thm A.7] fails within its stated scope, or that no other decoupling argument exists.
   - **Owner default pending.** The decoupling condition is stated in words. It is named "H-decouple" only if the
     owner adopts that label (REVIEW §4 O-1).
   - **"A.9 restated for time averages"** is the corpus correction in `DEPENDENCIES-r5.md` §D. r5 states the
     time-average scope itself, so it does not depend on that correction landing. It must not cite A.9 as a
     pointwise curve.
5. **Page time (N-BH4).** Two sentences, condensing r4:195–197:

   > The Page-time fraction $t_P/t_{\rm evap}=1-(\beta/(1+\beta))^{3/2}$ is Page's [Pag13, Eq. (8)], for a constant
   > emission coefficient, $S_{\rm BH}\propto M^2$ and a constant ratio β of radiation entropy gained to black-hole
   > entropy lost; it is 0.646 at β = 1, β is not derived, and a mass-dependent coefficient moves the fraction [BHb, C7].

   All three inputs stay named, because non-claim 4 refers to them.

   - Layer: A (C7 exact algebra plus ODE control, confirmed in REVIEW §0).
   - R12 marker carried.
6. **Open steps.** r4:201, condensed to one clause each: H-scramble or a substitute; the generalized second law [GR
   App. A.6]; agreement with QES Page-time computations [Pen20]; the island correspondence, conjectural [Book §7.6].

**Does not claim:**
- resolution of the paradox;
- that the radiation carries the information;
- the pointwise Page curve;
- a falsifier (REVIEW O-4);
- agreement with QES/islands;
- that a black hole changes the external observer's primary partition. The r4 wording "the framework's
  nested-partition construction" is kept (GR:603).

**Owner markers.** The R11 markers at r4:14, :178, :187, :203, :241 and :251 are carried. Their text is updated to
the REVIEW verdict ("claims more than its support" where REVIEW says so). R12 (r4:194) is carried.

#### §5.3 Horizon thermodynamics: a consistency relation (Q2, 0.5 pp)

**Owner decision.** The coefficient is introduced through calibration, so it is described as consistency, not
prediction.

**N-HT1.** The audit's §4.4 permitted sentence, verbatim:

> Applied to the cosmological horizon, OI identifies the classical horizon temperature obtained from the first law,
> dE = c²κ dA/(8πG), with the KMS temperature ħκ/(2πck_B) of the emergent description of the same boundary modes.
> Under the infrared detailed-balance condition H-slope and the horizon and frame conditions of [GR §§2–3, §8.5],
> this calibrates ħ = c³ε²/(4Gσ) against the discreteness scale ε and the entropy σ per boundary mode; it fixes only
> ε/√σ = 2l_p. With that calibration the boundary-mode count σA/ε² equals A/(4l_p²) for every ε and σ. The
> coefficient 1/4 is the ratio 2π/8π of the two normalizations, the same relation by which the Hawking temperature
> fixes the Bekenstein–Hawking entropy. The result is therefore a consistency relation between the classical and
> emergent descriptions, not a prediction, and has no independent empirical test.

- **Sources.**
  - GR:148, Step 4;
  - GR:12, for the condition list: "H-slope (§3.2) together with the horizon and frame conditions of §2 and §8.5";
  - GR:310 ("a self-consistency condition, not an independent determination");
  - GR:320 ("$\sigma A/\epsilon^2 = A/(4l_p^2)$ … whatever σ"; "2π/8π").
- **Layer.** A: `quarter.py` (sympy) gives S/(A/l_p²) = k_Q/k₈ for every mode density, with countercontrols.
- **Literature.** "The same relation by which the Hawking temperature fixes …" is a historical attribution to
  Hawking 1975, cited from memory: VERIFY [Haw75] before landing. The relation itself is checked by `quarter.py`'s
  Hawking route.
- **Required qualifier (N-HT2), one clause:**

  > The classical temperature uses Einstein's first law as an input, so the relation presupposes the form of gravity
  > whose derivation from the substratum is open (§6.6).

  Source: GR §3.1. AW-1 hidden assumption.

**Does not claim:**
- that the 1/4 is derived by mode counting or predicted;
- that ħ is predicted;
- that GW250114 tests the 1/4 (GR:322 tests the area law);
- "historically a postulate" (GR:320; glossary:17).

#### §5.4 Deterministic sources and embedded prediction (Q2, 0.3 pp, **gated**)

**Owner decision.** PE-01 is a framework-validation result, not a novel physical prediction.

**Gate (§A.42).** PE-01 is on `research/oi-pseudoentropy-20261025` at `efbfd0d7` (#923), not on `main`. The draft
cites it only after the package lands on `main`, with its expected result retained. Until then this subsection is
omitted (see the fallback in the page budget).

**N-PE1.** The audit's permitted sentence, with "validation" framing:

> A deterministic source is not thereby unpredictable to an embedded observer: in one exhaustively enumerated
> clock-controlled generator, an active observer with two bits of memory predicts its output with advantage between
> 1/8 and 5/32 over a four-step window [PE01]. This bounds the scope of a statement of the framework rather than
> predicting a new effect; attacks of this kind on clock-controlled generators are known.

- Source: PE-01 REPORT (efbfd0d7), "Result" table: `G_clk`, n = 5, z⁵+z²+1, m = 2, K = 7, advantages 1/8, 5/32,
  5/32, 1/8. The statement holds for this generator, observer and horizon only.
- Layer: E (exact enumeration, 78/78 jobs, replay byte-identical).
- **Literature.** "Known in kind" rests on the package's A3 tags (Gomułkiewicz–Kutyłowski–Wlaź 2006; AGHP 1992).
  Those were read by the package's literature review, not by this design. No citation of them is made in r5 until
  read; the clause says only "known", with [PE01] as source.

**Does not claim:** a passive witness (none exists in scope); family-wide predictability; a physical prediction.

#### §5.5 Further readings (Q2, 0.5 pp)

One sentence each, each labelled with its status.

- **Arrow of time (N-AR1).** The audit's permitted sentence:

  > Under the effective-mixing hypothesis (EM), sufficiently fast-mixing equilibrium regions support no observer
  > with persistent, read-back records [Main §4.6].

  - Source: Main:730, "Theorem (structural observer selection — conditional on (EM))".
  - Layers: P + I.
  - **Does not claim:** that the arrow is derived; that no additional axiom is needed (Substratum:356); coverage
    of the decelerating era.
- **Measurement (N-MR1).** The audit's permitted sentence:

  > Theorem 1 admits a reading in which records are definite configurations and the quantum state compresses the
  > visible law; it covers fixed-basis records only, and is an interpretation, not a result.

  - Source: Main:632 (the Lüders rule "transcribes Bayesian updating … for the represented diagonal sector — which
    is the transition-statistics layer, not the instrument algebra").
  - Layer: I.
  - **Does not claim:** that the measurement problem is dissolved.
- **Excluded from §5:** the dark sector, a₀ and the 95% budget; quantum computing; cosmological initial conditions;
  DESI ν; echoes; Koide; λ(M_Pl) = 0. The reasons are in AUDIT §§5–7. The SM closed forms and JUNO go to §6.7, as
  Q3 items about tests.

### §6 What remains to be proved (Q3, 2.7 pp)

**Purpose.** The owner's Q3 list, in the owner's order.

- **§6.1 Full quantum equivalence: operational completion.** r4:210–220, verbatim: Theorem 4 with both directions
  and their witnesses; "for every nonempty finite carrier"; qubit independence; "OI alone does not imply quantum
  mechanics"; "(iii)–(v) open".
- **§6.2 The evolution relating two times is not selected.** r4:222–226, verbatim. Permitted trim: the coherent-lift
  gloss may move to a footnote-free parenthesis. No identifier or "forward direction" may move.
- **§6.3 No fixed finite carrier reproduces a qubit.** r4:228–230 (R2-2 text), verbatim.
- **§6.4 The Born rule.** One sentence, pointing to r4:78 (§2.3). It states that the origin of the quadratic
  exponent is open [Main §3.4; Bar26, Thm 3.1]. It does not repeat r4:78, because `duplicate_check` fails on a
  repeated paragraph.
- **§6.5 Bell structure.** r4:234 item (5), with T1, verbatim, as its own paragraph. The other items of r4:234
  ((1)–(4)) go to §6.8.
- **§6.6 Gravitational coupling (N-GC1).** New.

  > The covariant field equations, with their conservation structure, source coupling and continuum limit, have not
  > been derived from the substratum [GR, Level G3]. The cosmological-constant proposal of §5.1 is conditional on
  > them, and the horizon calibration of §5.3 uses Einstein's first law as an input. The memory-bearing condition
  > (C4) is not shown to hold at the cosmological partition [GR §2.2].

  - Sources: GR:12; GR:20 and GR:52 ("(C4) is therefore a named realization condition at the cosmological cut. Not
    presently discharged").
  - Layer: O.
  - **Does not claim:** GR:567's "the equivalence applies in our universe".
- **§6.7 Experimentally distinguishing predictions (N-EX1 to N-EX3).** New.
  - **N-EX1:**

    > No experiment yet distinguishes OI from standard quantum theory: the theorems of §§2–3 are mathematical, and
    > no constraint on eligible processes that a memory-witness experiment could falsify is established [Main §4.5].

    Source: Main:704 ("no experiment falsifies the theorem itself … No ontology-level memory falsifier is
    established"). Layer O.
  - **N-EX2:**

    > Closed forms in the companion Standard-Model work, such as λ = 1/(π√2) for the Cabibbo parameter, agree with
    > values measured before they were written; they are numerical agreements, not independent predictions, and
    > rest on the cubic-lattice commitment and named bridge hypotheses [SM].

    - Sources: SM:849 ("hypothesis, not a derivation"); appendix-a:217 ("no pre-registered forward confirmation");
      the audit's §6.2 git dating.
    - Layer: N, as a postdiction.
    - **Must not quote** "0.04%" or "0.12σ" without "postdiction". **Must not** write "parameter-free prediction".
  - **N-EX3:**

    > The value sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798 was written after JUNO's first result; JUNO's projected
    > design-lifetime precision of ±0.0014 will test it, conditional on an underived Wilson-coefficient ratio [Juno].

    - Sources: Juno:73 (postdates the first results); Juno:409 (projected precision and the 2σ falsifier);
      appendix-a footnote ᶠ (the 4/3 ratio).
    - Layer: N (central value, a postdiction) + O (precision test).
    - Whether 4/3 was selected with the data in view is **undetermined** (AUDIT §7.1). See CLAIMS.
- **§6.8 Further open problems.** r4:234 items (1)–(4), verbatim, together with r4:232–234's lead clause, adjusted to
  the new section numbers.

### §7 What is not claimed; conclusion (Q3, 0.9 pp)

**§7.1 What is not claimed.** r4:238–243 items 1–6, verbatim, with these exceptions:
- **Item 4** gets the N-BH3 status and the R2-3 non-claims.
- **Item 6** points to Appendix B.

New items, in the register of r4's list:
- **(7)** No prediction of the value of Λ or of Ω_Λ, and no claim that the cosmological constant problem is resolved:
  the proposal of §5.1 is conditional on the covariant field equations.
- **(8)** No claim that the 1/4 of the Bekenstein–Hawking entropy, or ħ, is predicted: §5.3 is a consistency
  relation.
- **(9)** No Standard-Model value is claimed as an independent prediction. The JUNO precision test of §6.7 is the
  one quantitative item with a stated test ahead of full-precision data.
- **(10)** No claim that the viewpoint is new: a deterministic core analysed by quantum methods is 't Hooft's
  [tH14]. The paper's results are the theorems and their scopes.
- **(11)** No claim that §5.4 predicts a physical effect. Include this item only if §5.4 is included.

**§7.2 Conclusion,** about 120 words. Three sentences, one per question, built from N-INT1, the abstract's Q1
sentences, N-CC2 and N-BH3, and §6's list. The R11 marker (r4:251) is carried.

### Back matter (outside the count)

- **Code, data and formal verification.** r4:254–262, verbatim. Add the PE-01 path only once landed. Keep the §A.42
  retention marker (r4:256).
- **Appendix A.** r4:264–277, verbatim.
- **Appendix B. The card table.** r4:145–166, verbatim. Inside the approved raw `\begingroup…\endgroup` group or
  before it: the drafter checks that the card table's display math is unaffected by `\small\raggedright`, or places
  Appendix B before Appendix A, outside the group.
- **References.** r4's list, plus [tH14], [EvEMU11], [KP14], [Vol06], [Haw75] (VERIFY), [PE01] (gated), [SM] and
  [Juno] as corpus entries. [Jac95] and [CKN99] are cited only if the draft uses them. Their abstracts do not state
  what the audit attributed to them from memory (see CLAIMS-r5 §L).
