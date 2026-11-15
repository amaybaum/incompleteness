# Coverage audit r1: manuscript claims against the unified derivation ledger r3

**UNREVIEWED.** This is the coverage audit of condition 6 of the owner's ledger-expansion decision. It
has not been independently reviewed, and its review is required before acceptance. It is paper-only
and read-only. No computation on OI rules was run, no repository file was edited, and nothing was
posted. The ledger under audit, `LEDGER-r3.md`, is itself unreviewed; its review is running in
parallel. Inclusion of a claim here implies no derivation of it. A complete ledger is not a complete
theory.

**Authorization, quoted verbatim.**
- #914 comment 6877871344 (`amaybaum`, 2026-11-14T13:19:06Z), condition 6: "**Completeness audit:**
  Check every substantive physical claim in Main, Substratum, SM, GR and Structure against the
  ledger. Use book chapters 18–19 as additional completeness controls. Record missing entries,
  unsupported claims and mismatches explicitly rather than silently resolving them." Condition 7
  of the same decision: "The resulting r3 and audit require independent review before acceptance."
- #914 comment 6877908458 (`amaybaum`, 2026-11-14T13:22:18Z): "Yes, I approve adding the QCD group to
  r3". Its recording comment places "QCD vacuum energy, condensates and gravitational coupling" in
  "the Level C coverage audit, cross-referenced to GR §6.2" (checked: entry G-13 below, ledger
  C-QCDVAC).

This audit adopts no claim, settles no premise, and proposes no change to any Issue, tier, readiness,
authorization or scientific status. The rows proposed in §4 are proposals for the ledger author.

**Base.** All five papers and both book chapters were read from `main` at `dfeec843`, the commit the
ledger states it holds at. Line numbers are physical lines of those files; paragraphs in `papers/*.md`
are single long lines.

**Method.** Each paper was read section by section. Abstracts, introductions, status and scope
sections, conclusions and every labelled theorem, lemma, proposition, corollary and remark were read
in full or in their claim-bearing part. Long proof bodies and data tables were read at the level of
their stated result and status. Each substantive physical claim was then traced to the ledger row
that covers it, if any, and the row's class (DM, CD, EF, PE, UO, NEG) was compared with what the
source itself states and supports. Repeated statements of one claim are grouped under one entry,
with all locations found. Pure exposition, definitions and literature summaries were excluded unless
they assert something about OI. A claim derived in one paper and restated in another is counted once,
under the paper that derives it, with the other locations listed.

**Codes used in the tables.**
- **C**: covered by a ledger row whose class and evidence match the source.
- **CB**: covered by a broader ledger row (a branch row, a premise list or a "per row at source"
  entry) that does not record the claim separately.
- **CM**: covered, with a mismatch. Either the ledger's class differs from the source's own status,
  or the sources disagree with each other in a way the ledger does not record.
- **U**: no ledger row covers the claim.
- Flag **O**: the source states the claim more strongly than its own proof or cited support reaches.
- Flag **T**: no concrete discriminating test is stated for the claim.

## 1. Summary

| Count | Main | Substratum | GR | SM | Structure | Total |
|---|---|---|---|---|---|---|
| Claims found (grouped entries) | 33 | 23 | 32 | 46 | 16 | **150** |
| Covered (C + CB) | 18 (13 + 5) | 11 (9 + 2) | 19 (13 + 6) | 31 (20 + 11) | 3 (0 + 3) | **82** (55 + 27) |
| Covered with mismatch (CM) | 1 | 6 | 4 | 6 | 0 | **17** |
| Uncovered (U) | 14 | 6 | 9 | 9 | 13 | **51** |
| Overstated at source (flag O; overlaps the rows above) | 2 | 8 | 4 | 6 | 8 | **28** |
| No concrete discriminating test (flag T) | 1 | 3 | 3 | 2 | 4 | **13** |

In every column, covered + covered with mismatch + uncovered = claims found (150 in total).

**Most important findings.**
1. **Structure has no ledger coverage at all.** The ledger cites `papers/Structure.md` at no line.
   Thirteen of its sixteen grouped claims are uncovered, including its one stated negative result
   (matrix-model formulations fail A2 and A5, T-1) and its observer-admission reading of the string
   landscape (T-5).
2. **Structure contradicts Main on observer genericity.** `papers/Structure.md`:733 states that
   "random permutations on finite sets typically lack the coupled-dynamics, non-equilibrium-phase, and
   high-capacity features required for C1–C4". `papers/Main.md`:147–151 proves the opposite for the
   C1 witness: the fraction of bijections whose one-step matrix is a permutation decays exponentially
   in the hidden capacity. SM Theorem 22 (`papers/SM.md`:1376) gives C1 and the C3 capacity floor for
   every connected bounded-degree partition with |V| ≤ N/3. No source establishes that C2 or C4 fail
   generically. The landscape conclusions built on the claim (`papers/Structure.md`:526, 555) carry
   this gap.
3. **Substratum's Stage 2 text states SM outputs without their conditions.** `papers/Substratum.md`:147–153
   lists "Three generations of chiral fermions" and "One Higgs doublet" as outputs; :165 says Theorems
   12 and 13 "give chirality"; :169 calls every step "a uniqueness statement"; :173 gives the status
   "Theorem for the local lattice sector". SM states chirality is open (H-χ′; the minimal embedding is
   certified vector-like, `papers/SM.md`:543), the Higgs doublet is "taken as phenomenological input"
   (:468), and three physical generations are conditional on H-spin′. Theorem 23's own statement
   (`papers/Substratum.md`:193) carries these qualifications; the Stage 2 text does not. :199 adds
   "no fitted parameters, no model-building choices", against SM's statement that the cubic lattice
   is selected by the observed gauge group (ledger B-SM-4, EF).
4. **Prediction counts disagree.** Substratum's Class B gives "1 is structural ... (B-S), 2 are
   conditional structural (B-C)" (`papers/Substratum.md`:525), while SM's table gives 2 S and 5 C
   (`papers/SM.md`:1269–1316) and Substratum:199 itself quotes SM's 2 and 5. SM classes λ(M_Pl) = 0
   as S; the ledger classes it CD[composite Higgs, A₁ taste] (B-SM-HIER-3), and SM Theorem 11 takes the
   Higgs doublet as input.
5. **GR states a neutrino-mass prediction that SM classes as solution-specific.** `papers/GR.md`:410
   and :524 speak of "the OI predictions of normal ordering with Σm_ν near the oscillation minimum of
   0.059 eV" and say the neutrino and dark-energy predictions "both follow from the same lattice
   structure". SM gives the absolute scale as solution-specific (`papers/SM.md`:1468; ledger
   B-SM-NU-3, EF) and normal ordering as a genericity heuristic (:1460; B-SM-NU-2, PE). No derivation
   links the two sectors.
6. **The registered forward tests are untracked.** SM's pre-registered PMNS tests (the sum rule
   2 sin²θ₁₂ + sin²θ₂₃ = 7/6, the θ₂₃ octant, sin²θ₁₃, and JUNO's lifetime precision;
   `papers/SM.md`:1347–1362) are the clearest concrete discriminating tests in the corpus. The ledger
   records only JUNO (C-PRED-1). The source says they are "forced by the same cubic-group structure
   ... with no free parameter". Its own table classes the sum rule and θ₂₃ as L, pending Cond 2.
7. **Several cosmology results and tensions are missing.** These are the McGaugh et al. Tully–Fisher
   evolution tension (`papers/GR.md`:512), the rich-cluster mass residual (:524), the CMB peak match,
   which uses ρ_E ≈ Ω_CDM ρ_crit as an input (:530), and the MOND interpolation constraints (:488–504).
   The ledger records the relaxation kernel as uncomputed (B-COS-5). GR:532, however, states an
   epoch-local kernel, as a reading the text adopts rather than a derivation.
8. **Large proved blocks of Main and of the other papers have no row.** In Main these are the C2 and
   C3 necessity theorems, the phase-locking and Hamiltonian-reconstruction results, the separability
   threshold, CP-indivisibility, the intervention-dilation comb theorem and its negatives, and the
   passive-observation characterization. Elsewhere they are Theorem 24 and Propositions 24.2–24.5 of
   Substratum, SM's observer-level isotropy theorem, its wave-equation form lemma, Theorem 22 and
   Appendix A, and the GR universality theorem.
9. **The status of Lemma 1 differs across papers.** Main says the finiteness of the visible space is
   "stipulated, not derived from the observation axiom", and that invoking holographic bounds there
   "would be circular" (`papers/Main.md`:700). GR says "Lemma 1 is a consequence of partition geometry"
   (`papers/GR.md`:90). SM says finite boundary entropy "follows from the holographic entropy bound"
   (`papers/SM.md`:46). The ledger's §11 does not record this.
10. **The book chapters go beyond the papers in four new places** (§3): ch19:106 says anomaly
    cancellation "forces exactly three candidate matter sectors"; ch19:196 says the framework "derives
    exactly one scalar doublet"; ch19:118 says the framework "derives the total budget"; ch18:144–152
    presents a non-renormalizability "dissolution" that no paper row carries.

## 2. Per-paper tables

### 2.1 `papers/Main.md`

| ID | Location | Claim (paraphrase) | Ledger row | Audit | Notes |
|---|---|---|---|---|---|
| M-1 | 14–18, 97, 546–552, 600(1), 642, 764–768 | S ⟺ D ⟺ Q_fb on every finite horizon; exact and universal | B-QM-1 | C | Kernel, as the ledger states |
| M-2 | 16, 600(2), 602–618 | C4 ⟺ M_t > 0; unavoidable hidden predictive memory (a)–(c) | B-QM-2 | C | Ledger records the unformalized CMI step |
| M-3 | 171–174, 536–542, 628–636, 696, 731–733 | Characterization theorem (ii) ⟺ (iii); readback lemma I ≥ p₀δ²/ln 2; horizon restriction forced | B-QM-2 | CB | The theorem and the readback lemma have no row of their own |
| M-4 | 486, 492–496, 638 | No fixed finite realization carries the instrument continuum; no horizon-independent intervened representation at fixed d (parameter counts); no exact all-time realization (periodicity) | none (B-QM-8 is a different obstruction) | U | NEG, paper proofs |
| M-5 | 109–143, 157 | P-indivisibility from recurrence plus a non-permutation map; stochastic-inverse lemma; rooted and overlap-and-return theorems | B-QM-16 | C | |
| M-6 | 147–151 | A non-permutation one-step matrix is generic among bijections; the failing fraction decays exponentially in n_H | none | U | DM, exact counting. Contradicted by `papers/Structure.md`:733 (T-5) |
| M-7 | 159–169, 443–476, 498–502, 736 | Fast-bath erasure lemma; C2 necessity in quantitative mixing form and in process form; ETH as motivation only, itself a conjecture | input (v) only | U | Persistence form DM; timescale form CD[mixing hypothesis] |
| M-8 | 76, 504–512, 737 | C3 necessity m ≥ 2^{I*}; horizon realization 10¹²² modes against 10⁸⁰ baryons | input "C1–C4" only | U | The horizon numbers come from the GR partition (see the observation after §2.5) |
| M-9 | 182–200 | Six-hidden-state model: P-indivisible and process-tensor non-Markovian | B-QM-16 | CB | Witness |
| M-10 | 206–216, 352–356, 526–534, 656, 730 | ≤ n³ compression imported from Barandes under translation hypothesis (T); one-step ancilla dilation in-house | none | U | External input; its role is stated at source |
| M-11 | 226–260, 716 | Phase-locking: H unique up to shift, rephasing and antiunitary conjugate under (G1)–(G4); ancilla-marginal phase-locking for the listed block structures, with no uniform statement | §2.3 lists (G1)–(G4) only | U | Certified for listed (n, m_a); see G-8 |
| M-12 | 262–290, 342–352 | Stinespring route: permutation unitary, CPTP channel, Born-form identity; C1 alone gives measure-and-prepare channels (exhaustive at small sizes) | B-QM-1 | CB | The C1-insufficiency negative is not recorded |
| M-13 | 292–324, 778 | Boundary bound; channel normal form; separability threshold (entanglement-breaking iff t = s); non-entanglement-breaking iff w < κ; cubic-block criterion | B-P4-QCB-3 covers only the reading at :322 | U | Exact algebra plus exhaustive checks, q = 2 (prime q stated) |
| M-14 | 326–340, 734 | CP-indivisibility follows from P-indivisibility for the permutation-dilation family and fails for general CPTP families; approximate unitarity for t ≪ τ_B | none | U | |
| M-15 | 356, 562, 584–588, 646–650 | Operational completion (i)–(v); (iv) not supplied; OI⁺; tensor-product structure; causal separation | B-QM-3 to B-QM-6 | C | |
| M-16 | 358–427, 770 | Coupling-graph cone; CHSH ≤ 2 under screening; lattice obstruction corollary; measurement-dependence bound; PR laws realized | B-BELL-1 to B-BELL-6 | C | |
| M-17 | 478–484, 556, 682 | Intervention dilation (finite action-labelled comb); the double-slit setting family has a finite reversible realization | B-P4-MEAS-5 covers only the derivation from dynamics (UO) | U | The comb theorem has no row |
| M-18 | 558–560, 600(3) | Classical-dimension obstruction; SIC embedding exact over ℚ(√3) | B-QM-8 | C | |
| M-19 | 564–582, 594–598, 600(4), 772 | Gluing ε-form, rounding lemma, mutual ε-density, single controlled dynamics; context dependence for d ≥ 3 (570) | B-QM-7 | C | The bound on the realized law at finite b is open at source |
| M-20 | 590–592 | Complete passive observation iff the algebra is commutative; passive incompleteness is theory-insensitive and is no evidence for a hidden ontology; uncertainty relations do not discriminate the OI core | none | U | Kernel; scope negative |
| M-21 | 620–622 | Canonical predictive quotient: existence half of purification at substratum level | none | U | Compare S-14 |
| M-22 | 20, 644 | Representability plus coherence does not select the relating evolution | B-QM-10 | C | |
| M-23 | 18, 286, 554 | Born exponent not selected | B-QM-11 | C | |
| M-24 | 660–674 | Rest-frame selection: a horizon partition selects a timelike direction and no spatial axis; boosts excluded; isotropy is a residual input; converse | none | U | Uses a causal horizon |
| M-25 | 684–692 | Wigner's friend: joint law unique given φ; the friend's QM description is a proposal | B-P4-MEAS-2, B-P4-MEAS-3 | C | |
| M-26 | 652, 692 | Measurement as conditioning plus re-marginalization; Lüders rule as Bayesian update | B-P4-MEAS-1 | C | |
| M-27 | 718–722 | No memory-witness outcome falsifies the ontology at present; tabletop tests named without an outcome | C-PRED-9 | C, T | |
| M-28 | 740–758 | Structural observer selection under (EM); anti-Boltzmann-brain corollary; rate condition | B-P4-AOT-2, C-OBS | C | |
| M-29 | 46, 700, 712 | Lemma 1: visible finiteness is stipulated (700) | §1 (ii)/A1; §2.2 chain | CM, O | Main:46 offers "finite-area surface" support; `papers/GR.md`:90 calls Lemma 1 "a consequence of partition geometry"; `papers/SM.md`:46 says the bound "follows from the holographic entropy bound". Not in ledger §11 |
| M-30 | 44 | The map form follows from composition (Cauchy functional equation) | §1 inputs (A2) | CB | Composition presupposes a state map |
| M-31 | 64 | Reversibility is the orthodox assumption, imported | §1 (iii)/A2 | CB | |
| M-32 | 84–90 | Partition-relativity: the emergent law is fixed by partition and measure (the prior is a third datum) | none | U | Consumed by GR §3.1 |
| M-33 | 704 | Relative to QBism and relational QM, "this framework provides a structural *why* and quantitative predictions" | none | U, O | Main itself states no quantitative prediction; any such prediction is downstream |

### 2.2 `papers/Substratum.md`

| ID | Location | Claim (paraphrase) | Ledger row | Audit | Notes |
|---|---|---|---|---|---|
| S-1 | 14, 22–26, 371–397, 417–423, 548–550 | QM and GR are two projections of (S, φ); the unification problem is a category error; "Both are derived rather than fundamental" (389) | none | U, O, T | :423 makes the recasting conditional on G3. The Einstein equations are imported (B-GR-3), so "derived" overreaches. :419 calls the claim non-empirical |
| S-2 | 421 | The synthesis "does establish" that SM and GR are "derived from the same object by the same procedure under the same conditions" | none | U, O | Ledger §9 GR–SM is "undetermined" and Q4 records the conflict in geometry order |
| S-3 | 46 | The 10¹²² ratio is a compression ratio; the dark sector is the gravity of unreadable storage; ħ is a conversion factor | B-CC-1, B-COS-3, B-GR-2 | CM, O | Flat identifications, against CD and partly definitional classes at the anchors |
| S-4 | 76–104, 205–223 | Inputs E1–E7 and A1–A6; the set is sufficient but not shown minimal | §1 | C | |
| S-5 | 121–141 | Stage 1: deterministic embedding with C1–C4 conditional on M1-T; M1-B separate; theorem for the scoped dilation datum | B-BELL-8, §1 | CB | Stage 1 has no row of its own |
| S-6 | 131–135, 171 | H-Bell (i)–(iii); mixing hypothesis open; the exact linear rule splits shells | B-BELL-7, input (v) | C | |
| S-7 | 143–173, 189–195 | Stage 2, Lemma 23.0, Theorem 23 (local residue) | B-BELL-8; pieces in B-SM-1 to B-SM-8 | CM, O | Finding 3 of §1. Theorem 23 at :193 is qualified; Stage 2 text at :147–153, 165, 169, 173 is not |
| S-8 | 199, 203 | Evidential weight: "uniquely derives"; "no fitted parameters, no model-building choices, no landscape of alternatives" | B-SM-4 (EF) | CM, O | :203 concedes that part of the residue is selected; SM:1424 places the cubic lattice and d = 3 in Tier 2 |
| S-9 | 225–227 | The lattice is fundamental; the mass gap can be set aside; structural results are "exact" | B-QCD-6 | CM, O | "exact" omits the H-link, H-cust, H-spin′ and H-χ′ conditions; see SM-41 |
| S-10 | 237–243 | ER=EPR: the weak form is reproduced emergently; the strong form is "predicted *false*" at representative level | none | U, T | PE; the source says a test is beyond reach |
| S-11 | 247–300, 429 | Theorem 24: generators (i), (iii), and (ii) under the alphabet-size hypothesis; (iv) a comparison; completeness open; effective-finiteness corollary; three-level gauge hierarchy with inclusions not established | none | U | A headline theorem with no row |
| S-12 | 278–284, 302–361 | Props 24.2–24.5: block-word rigidity, minimal word realizations, passive predictive quotient, record fibres; memory differs from opacity | none | U | Paper proofs; Lean witnesses named; bounded exact rational controls under `verification/audits/manuscript/` (not run here) |
| S-13 | 270–274 | Amplitude-scale gauge is an adjoined principle; linearity is a sharpened axiom | §1 (vii)/A5 | C | |
| S-14 | 175–185 | Stage 3: ħ relation, conditional on H-slope | B-GR-2 | C | |
| S-15 | 56, 399–413 | Arrow-of-time projection: horizon clock from GR kinematics; layered cascade; alignment not established | B-P4-AOT-1 to B-P4-AOT-5 | C | |
| S-16 | 415 | Flavour CP phases are solution-specific | B-SM-FLAV-4 | C | |
| S-17 | 459 | The triple "generates every concept in fundamental physics"; GR "is the thermodynamic limit of the coupling structure" | none | U, O, T | G3 is open; energy conservation needs extra assumptions (the source says so) |
| S-18 | 461–467 | Measurement account; no branching | B-P4-MEAS-1, B-P4-MEAS-4 | C | |
| S-19 | 478–480 | Class A ("structural theorems"): a stable Z′ falsifies the cubic decomposition; a fourth generation falsifies the taste-reduction derivation | C-PRED-1 (broad) | CM, O | Generations are conditional on H-spin′; the gauge-group reading on H-link and H-cust; cubic selected by the gauge group (EF) |
| S-20 | 481 | Bell/Tsirelson: an excess over 2√2 falsifies QM and the claim that the lift lands in the quantum set; bare C1–C4 do not enforce Tsirelson | A-BELL, B-BELL-1 | C | |
| S-21 | 486–527 | Class B: 13 predictions, counted 1 B-S, 2 B-C, 6 B-L, 2 B-M, 2 B-R; every entry rests on H-spin′ and H-χ′ (488) | B-SM-FLAV-5, C-PRED-1 | CM | Finding 4 of §1. Counts differ from SM (2 S, 5 C) and from Substratum:199 |
| S-22 | 529 | The BH coefficient is a consistency relation with no direct test | B-GR-2, C-PRED-7 | C | |
| S-23 | 54, 92, 533–542 | Effective finiteness; Class C commitments; cosmological commitment; "what does not falsify"; three regimes of deliberate silence | §1 A1, B-COS-3, C-OBS, C-EARLY-1, C-EARLY-4 | CB | The silence regimes have no row |

The form lemma (Substratum:48, 159) and the Jordan–Chevalley decomposition (Substratum:62) are
counted under SM-2 and SM-45.

### 2.3 `papers/GR.md`

| ID | Location | Claim (paraphrase) | Ledger row | Audit | Notes |
|---|---|---|---|---|---|
| G-1 | 12, 24, 78–82, 102, 108–160, 300–306, 625–627, 651 | ħ = c³ε²/(4Gσ) and ε = 2√σ l_p by thermal self-consistency; only ε/√σ fixed; σ = 1 assumed | B-GR-2 | C | |
| G-2 | 12, 28, 156, 310–316, 619, 629, 653 | The count S = σA/ε² is "unconditional"; S = A/(4l_p²) | B-GR-1, B-GR-2 | CM, O | The ledger reclasses the count as CD (the partition takes GR's causal structure as given). The status difference is recorded by the ledger itself |
| G-3 | 38–42, 340–348 | The horizon "is a consequence of GR's causal structure, not a modeling choice"; ħ is observer-universal; geometry-first ordering | B-GR-1, B-CC-1, Q4 | CB | |
| G-4 | 44–52, 456, 661–663 | C1–C3 "Satisfied" at the horizon, with C2 from τ_B ≳ 1/H, which is not derived; C4 not discharged | §1 C1–C4; §9 QM–Cosmology; M7 | C | |
| G-5 | 58–92 | H-count, H-balance, H-slope as selection conditions; α-vacua counterexample; microreversibility gives the classical half | §4.3; B-GR-7 | CB | |
| G-6 | 112–138 | Boundary-only dependence lemma (cone; H-BD posited); deep-sector cardinality is gauge | none | U | Related to Theorem 24(iii) (S-11) |
| G-7 | 162, 691 | Einstein–Hilbert via an external theorem given a single cone; Einstein equations imported | B-GR-3 | C | |
| G-8 | 166–210, 292–296 | Bohr-frequency completeness; D-gauge completeness conditional on H-BG; antiunitary invariance; thermodynamic orientation; coherent-completion classification; orientation no-go | none | U | Kernel names cited; H-BG's comparison with the published classification is open (178) |
| G-9 | 212–276 | Operational completion; OI⁺; primitive-source, substratum-source, layer-flow and typed forms | B-QM-3, B-QM-5, B-QM-6, B-QM-15 | CB | The layer-flow equivalence (262–270) and primitive-source form are manuscript-carried and not separately recorded; B-QM-15 is described as carried by no manuscript (not checked against the census) |
| G-10 | 278–290 | Unique quasilocal completion; restriction to induced dynamics; the continuous extension is not unique | B-QM-9 | C | `continuous_extension_not_unique` not recorded |
| G-11 | 326–336 | H-local-lift locality theorem; scope of the emergent QFT | §6.3 premises; M1 | CB | |
| G-12 | 338–362 | CC: descriptive distinction; decoupling conditional on G3; Λ an input; ratio ~ S_dS | B-CC-1 to B-CC-3 | C | |
| G-13 | 567–581 | Relative effects gravitate; Higgs and QCD vacuum shifts are absolute; QCD binding gravitates | B-CC-4, C-QCDVAC | C | Satisfies the QCD-group cross-reference |
| G-14 | 372–408, 412 | RVM form not distinctive; Type II channel; \|ν\| ~ 10⁻³²; Bertini consistency; DESI phantom tension; Year 5 three-way test | B-COS-1, B-COS-2, C-PRED-5 | C | |
| G-15 | 410, 524 | "OI predictions of normal ordering with Σm_ν near ... 0.059 eV"; neutrino and RVM predictions "both follow from the same lattice structure" | B-SM-NU-2, B-SM-NU-3 | CM, O | Finding 5 of §1 |
| G-16 | 414–452, 458–460 | ~95% dark-sector corollary; ρ_s = ρ_crit; invisibility (ii-a), (ii-b); general-d ratio; a consistency check | B-COS-3, D5 | C | |
| G-17 | 454 | "The corollary's prediction is that no particle dark matter exists" | B-COS-3; §7.6 | CM, O | :458 calls the corollary a budget consistency check, not a derivation of structure; :530 takes ρ_E as an input |
| G-18 | 462–486, 506 | a₀ = cH/6 (factor imported); BTFR; "no free parameters beyond the baryonic mass" | B-COS-4 | C | |
| G-19 | 488–504 | Interpolation constraints (i)–(v); a one-parameter family, steepness bijection-specific; the "simple" interpolation function | none | U | |
| G-20 | 508–522, 536–545 | a₀(z) evolution; three "parameter-free" tests; Milky Way and Genzel tensions | C-PRED-6 | CB | |
| G-21 | 512 | McGaugh et al. (2024): no clear Tully–Fisher evolution, "in tension with the law" (−0.48 dex at z = 2) | none | U | NEG, not in C-PRED-6 |
| G-22 | 524 | Coma matched with the simple interpolation; rich clusters keep a residual of 1.0–1.5, "not closable" by baryons or neutrinos | none | U | NEG (partial). Uses Σm_ν ≈ 0.059 eV (G-15) |
| G-23 | 526, 532 | Bullet Cluster: frozen displacement with τ_relax ~ 1/H (mode relaxation not computed); epoch-local kernel dδ_E/da = (δ_m − δ_E)/a | B-COS-5 (UO) | CM, T | The source states a kernel reading and a numerical check; the ledger records the kernel as uncomputed. The proposed relaxation test (systems ≫ 1 Gyr after collision) is not accessible |
| G-24 | 528–530 | CMB peaks match ΛCDM at linear order, given ρ_E ≈ Ω_CDM ρ_crit as an input; CLASS check at ν = 10⁻⁴ | none | U | EF input; the check uses ν = 10⁻⁴, not 10⁻³²; :530(iii) uses "adiabatic initial conditions set by inflation", while `book/ch19-open-problems.md`:194 says inflation is "Not addressed" |
| G-25 | 536 | "Each follows from partition geometry ... no predictions are fit to the quantities they predict" | B-COS-3, B-COS-4 | C | The table rows themselves state "factor imported" and "partly definitional" |
| G-26 | 318, 547, 597 | GW250114 tests the area theorem, not the 1/4; no echoes | C-PRED-7 | C, T | No direct test of the 1/4 |
| G-27 | 589–595, 607 | Planck-scale ordering may fail; theorem falsifiable only if both routes fail; conditional memory test; analogue-gravity tests without outcome | C-PRED-9 | CB, T | |
| G-28 | 599–605, 709–751, 769–866 | Nested trace-outs (A.1–A.4); GSL open (A.6); Page curve (A.8–A.9) and H-scramble failure; Page time; islands conjectural | B-GR-9, B-BH-3 to B-BH-7 | C | |
| G-29 | 753–767, 785–795 | Theorem A.5 (frozen deep sector gives a mixture of boundary channels; additive form open); Theorem A.7 (effective pure state; a superposed D does not suffice) | none | U | |
| G-30 | 609–679 | Universality theorem: (U1)–(U3) "unconditional" for any substratum meeting S1–S4; (C1′)–(C3′) conditional | none | U, O | (U1) uses Jacobson's relation and H-count for its identification; S1 presupposes a causal horizon; S2 includes the slow-bath C2 |
| G-31 | 689–697 | Spectral dimension → 3; weak-field Newtonian gravity at fixed G; equipartition normalization open | B-GR-5 | C | |
| G-32 | 104 | K = 6 internal components consistent with one boundary mode per cell, "forced rather than assumed" | none | U | Rides H-link |

The free-level dispersion bound and H-Hawking (GR:639–649) are counted under SM-5.

### 2.4 `papers/SM.md`

| ID | Location | Claim (paraphrase) | Ledger row | Audit | Notes |
|---|---|---|---|---|---|
| SM-1 | 12, 26, 32, 218, 242–282 | Theorem 1a (equivariant projection preserves cubic symmetry); Cor 1a (quadratic anisotropy forbidden); Cor 1b (normalized adjacency needs an observer-level center-free kernel); Lemma 1c; Theorem 1 (conditional Klein–Gordon branch) | B-SM-9 only | U | 1a and Cor 1a are classical exact results (DM); 1b and Theorem 1 are CD |
| SM-2 | 224–232; `papers/Substratum.md`:48, 159 | Form lemma: a center-free, cubic-isotropic, linear, second-order reversible nearest-neighbour rule is the wave equation up to α; the nearest-neighbour premise goes beyond A3 | none (§5.2 chain) | U | CD[CI, E4, A5, NN premise] |
| SM-3 | 104–118 | Graph G(x); explicit construction; local gauge invariance from A6 (conditional carrier reading); bijectivity automatic | §1 (xii), (xiii); §9 internal conflict | CB | |
| SM-4 | 120–124, 150, 160–164 | Area-law lemma (proportional over ℝ; boundary bound over ℤ/q); lattice thermality corrections ~10⁻¹²² and ~10⁻⁷⁶ | B-GR-4 | CB | The correction estimate covers input (ii) only (stated) |
| SM-5 | 126–138, 1448; `papers/Substratum.md`:482–484; `papers/GR.md`:639–649 | Emergent Lorentz: no linear term; ω² = k²[1 − (4σ/45)(E/M_Pl)²], subluminal, anisotropy 4:1:0, tree level; rotational E_g sector radiatively "precarious"; UHE bound c₆ ≲ O(1) | none (appendix-a G13 cited in ledger §4.6) | U | Linear-LIV detection is a concrete test (Substratum:484). The amplitude constrains σ and is not near-term. Interacting protection is open |
| SM-6 | 132 | Cross-charged sector is baryon-safe; Pati–Salam U₁ vector leptoquarks (3, 1, 2/3); M_X floor ~1.5×10⁶ GeV or 10³–10⁴ GeV depending on generation structure | none | U | CD[H-link, H-cust, condensate]; M_X solution-level |
| SM-7 | 140–142 | Lattice Bisognano–Wichmann form | B-GR-8 | C | |
| SM-8 | 144–158 | Discrete Einstein equation as a target form; the Ollivier route fails; sparse long-edge diagnostic | B-GR-4; §9 Bell–GR | C | |
| SM-9 | 170–212 | d = 3 from E5–E7 within A4; integer d through A4; not anthropic | B-SM-5 | C | |
| SM-10 | 198, 601–607 | Theorem 16: [g] = (3 − d)/2; asymptotic freedom needs field content | B-SM-11, B-QCD-4 | C | |
| SM-11 | 284–298 | Theorem 2 (Susskind) on the branch; measure-reduction gap; linear dynamics integrable; cycle structure | input (v); B-SM-FLAV-3 | CB | |
| SM-12 | 300–308 | Theorem 3: chiral symmetry iff onsite terms vanish | B-SM-10 | C | |
| SM-13 | 310–344 | Theorem 4 (mass spectrum on the observer branch); Lemma 4a (one cone; species speeds ~(m/M_Pl)²); Prop 4b (custodial scalarity, H-blind); Theorem 5 (condensate stabilizer on H-link + H-cust) | B-SM-2, B-SM-3 | CB | |
| SM-14 | 346–370, 64–74 | H-link; Lemma 6a (the old minimization proof is not established); Theorem 6 (K = 2dm); factorization problem | B-SM-2 | C | The withdrawn minimization route is not recorded as NEG |
| SM-15 | 372–388 | Theorem 7: (3, 2, 1); physical reading conditional; robustness | B-SM-1 | C | |
| SM-16 | 390–416 | Theorem 7b: SC is the unique Bravais lattice compatible with the observed group; Cabibbo on SC, BCC and FCC | B-SM-4 | C | |
| SM-17 | 418–426 | Every irrep of O is "accounted for" | none | U | Identification, PE |
| SM-18 | 430–456 | Theorems 8, 8b, 9, 10; H-spin′; spin-statistics under H-spin′ | B-SM-6 | C | |
| SM-19 | 464–470 | Theorem 11: the Higgs doublet is taken as input; the singlet taste accommodates exactly one | B-SM-12 | CB | Input status not recorded. See S-7 and book finding K-2 |
| SM-20 | 472–533 | Gauge bosons from the Schur complement; cross-charged modes gapped at M_X; level-confusion diagnosis; matter on links (availability only; chirality and selection open) | B-QCD-2 | C | |
| SM-21 | 535–571 | Theorems 12, 13 (chirality conditional; minimal embedding vector-like); Nielsen–Ninomiya "bypassed"; doublers "become, in OI, the physical generations (Theorem 9)" (567) | B-SM-7 | CM, O | :567 states as fact what Theorem 9 leaves open (free kernel refuted, H-spin′ open); which NN assumption fails for the effective construction is open (:567) |
| SM-22 | 573–599 | Theorem 14; Prop 14a; Theorem 15; Prop 15a; Cor 15b \|q_p\| = \|q_e\| (conditional) | B-SM-8 | CB | The charge-magnitude identity is not recorded |
| SM-23 | 609–613, 1538–1582 | Higgs as unique mechanism; chiral protection "structurally identified"; v ≪ f open; coupling deviations ~v²/f² unobservable | B-SM-12, B-SM-HIER-1, B-SM-HIER-2 | C, T | |
| SM-24 | 621–671 | Theorems 17–21; H-top, H-det; nullity; Jarlskog report not available for verification | B-SM-CP-1 to B-SM-CP-3 | C | |
| SM-25 | 675–717, 769–797, 815–817 | 1/α₀ = 23.25; δ₀ empirical; (A, B) fitted; non-unification; δ₀ ≈ Tr[Y²] = 10 observed; 2-loop rebuild does not reproduce δ₀ | B-SM-GAUGE-1, B-SM-GAUGE-2 | C | The 2-loop negative and the numerical observation are not recorded |
| SM-26 | 717–767 | A·B ≈ 48–62 from finite lattices; inconclusive | B-SM-GAUGE-2 | C | |
| SM-27 | 799–813 | Haar measure confines; near-identity measure conjectured; code not extant; dynamical-fermion MC | B-SM-GAUGE-3, B-SM-GAUGE-4, B-SM-NP-1, B-SM-NP-2 | C | |
| SM-28 | 819–841 | No GUT: no GUT proton decay, monopoles or strings; shared coupling origin; not unique to OI | C-EARLY-3, C-PRED-3 | C | |
| SM-29 | 849–903 | Cabibbo (named hypothesis); Wolfenstein A; m_d/m_s via GST; J (η empirical); \|V_cb\| | B-SM-FLAV-1, B-SM-FLAV-5 | C | |
| SM-30 | 1269–1316 | Table: λ(M_Pl) = 0 classed S; Wolfenstein A classed S | B-SM-HIER-3 (CD), B-SM-FLAV-5 | CM, O | Finding 4 of §1. Footnote ʰ says the observed A is fit-family dependent |
| SM-31 | 905–1003 | Koide Q and θ₀ = 2/9 (normalization 1/d versus 1/(2d) open); m_e and m_μ from m_τ; m_b via Q_down (P); m_u/m_d (L) | B-SM-FLAV-1, B-SM-FLAV-2, B-SM-FLAV-5 | C | |
| SM-32 | 1004–1008, 1126 | y_t(M_Pl) = 1 flows to m_t ≈ 207 GeV, a 20% excess; the weak-scale match is a retrodiction with its mechanism open | B-SM-FLAV-5 | CB | The failed route is a NEG with no row |
| SM-33 | 1010–1112 | PMNS from TBM plus λ²; Cond 2 open (A₁ part at Layer 1, A₂ part at 2(b)); JUNO a retrodiction | B-SM-NU-1, B-SM-FLAV-5, C-PRED-1 | C | |
| SM-34 | 1114–1128 | λ(M_Pl) = 0 gives m_H ≈ 129–132 GeV, "4–7 GeV below" observed (1118); "consistent ... to ~2–3σ" (1126); table "m_t-consistent" | C-PRED-2 | CM | The three statements in SM disagree; the ledger carries only the first |
| SM-35 | 1130–1267 | m_b/m_τ = 4.28/Z_S; K = 1/2 with "empirical exclusion of natural fractions" (1206); 3D–4D bridge theorem | B-SM-FLAV-3 | CM | Data select K among the candidates, an EF element the ledger row does not carry. The bridge theorem has no row |
| SM-36 | 1324–1346 | Coincidence bound; the six-observable Casimir table gives "strong evidence for the underlying C₂/d identity" | none | U, O | The table includes the sum rule "via Cond 2" (open) and m_u/m_d at Layer 2(b); all values were known beforehand (1349) |
| SM-37 | 1347–1362, 1590 | Registered forward tests: sum rule 7/6, θ₂₃ = 0.5507 (upper octant), sin²θ₁₃, JUNO at ±0.0014; "forced ... with no free parameter" | C-PRED-1 (JUNO only) | U, O | Finding 6 of §1. These are concrete tests |
| SM-38 | 1374–1388 | Theorem 22: C1 and the C3 floor hold for connected bounded-degree partitions; C2 and C4 are explicit hypotheses | none | U | Bears on T-5 |
| SM-39 | 1390–1446 | Structural versus solution-specific; four layers; selection problem; tiers; constitution Proposition; the mass hierarchy "not a gap" | §5.1 (1424, 1428) | CB | |
| SM-40 | 1448 | "The structural predictions are exact theorems at the lattice level"; the mass gap "does not affect any prediction" | B-QCD-6 | CM, O | §6.5 (801) makes the validity of the perturbative matching depend on the phase of the induced gauge theory; "exact theorems" omits the named conditions |
| SM-41 | 1450–1468 | Neutrino sector (i)–(iv) on the singlet-Higgs branch: Majorana, so 0νββ "should be observed"; NO and hierarchy heuristic; scale and δ_CP solution-specific | B-SM-NU-1 to B-SM-NU-3 | C, T | No sensitivity target is stated; `papers/Structure.md`:1317 notes LEGEND-1000 aims at the inverted-ordering range while OI expects normal ordering |
| SM-42 | 1484–1536 | Substratum B conserved; substratum–emergent operator distinction; sphalerons emergent; no right-handed neutrino; 't Hooft matching under H-χ′ | B-SM-BARY-1, B-SM-NP-3 | CB | |
| SM-43 | 1596–1654 | Appendix A: period qL; Jordan–Chevalley with N² = 0; q-independent conductor; additive decomposition; laws sampled at multiples of q; marginalization keeps N | none | U | Exact, with computational checks for listed q, L |
| SM-44 | 14, 1588 | Abstract: the predictions "are forced by the cubic-lattice geometry and contain no parameters fit to the predicted quantities" | §5.1 (14, 1428) | CM, O | The table has E, R, P, L and M entries, including fitted couplings and Q_down; the conclusion (1588) is qualified |
| SM-45 | 88–96 | Alphabet-size hypothesis; additive automorphisms only | §5.3 | CB | |
| SM-46 | 1470–1482 | The commutant pattern transports; the specific output is OI-specific and conditional | §5.1 | CB | See T-15 |

### 2.5 `papers/Structure.md`

| ID | Location | Claim (paraphrase) | Ledger row | Audit | Notes |
|---|---|---|---|---|---|
| T-1 | 13, 33, 256–353, 359, 514 | Matrix models (BFSS, IKKT) fail A2 and A5 (and A3 on the natural reading); the abstract concludes "The substratum-level equivalence reading does not hold" | none | U, O | NEG, paper-level. The body scopes it to the "standard formulation" (351), calls (c) "provisional" (242) and lists five partial recoveries (337–347). The abstract's unscoped form exceeds the class ruled out |
| T-2 | 361–389 | OI and string theory are independent; no landscape dissolution, cross-attribution or computational gateway; "both programs cannot be foundational descriptions of the same physics simultaneously" (369) | none | U, O | :369 goes beyond T-1's scope |
| T-3 | 391–435 | Swampland: WGC satisfied; Majorana in the WGC-allowed region; dS consistency (dynamical but Λ-like); "no fundamental moduli ... parameters are derived from the cubic-lattice structure" (417); "non-trivial cross-validation" (429) | none | U, O, T | :417 conflicts with SM's solution-specific and fitted parameters (SM:1396, 1440); :403 states Majorana without SM's branch condition |
| T-4 | 443–510 | OI "naturally produces horizon holography"; "any horizon entropy in OI's framework is bounded by A/4" (453); no full AdS/CFT; graviton emergence open; duality analogs speculative | none | U, O | No bound theorem is cited for :453; the GSL is open (G-28) |
| T-5 | 120–122, 516–576, 709–735 | Observer-admission: most substrata and most compactifications are "likely" observer-lacking; fine-tuning dissolved "to a substantial degree"; Prop 9.10, Cor 9.11 | none | U, O, T | Finding 2 of §1. :566 calls it "a structural reading, not a rigorous result" |
| T-6 | 98–198, 892–954 | Two-axis hierarchy; predictions stratified; Cabibbo, Koide and dark-sector phenomenology at G3 × D, "forced by OI's specific" structure (179); a Born-rule test "confirms Level 1" (950) | none | U, O, T | GR:30 and 611–679 place the partition-geometry results at the universality level. The Born form is part of the definition of Q_fb (Main:14), so a Born test does not discriminate OI. Cabibbo is C, not forced |
| T-7 | 620–655 | Definitions 9.1–9.4; Prop 9.5 (generators (i) and (iii) give an observational sub-equivalence; proof sketch); Cor 9.6 | none | U | |
| T-8 | 656–687 | Props 9.7a and 9.7b (minimal Kraus and dilation uniqueness); Cor 9.8 (the substratum description is gauge relative to a fixed reference) | none | U | Standard mathematics, scoped |
| T-9 | 761–825 | OI's algebra-channel pair "captures ... the renormalizable couplings (gauge couplings at M_Z, Yukawa structure producing CKM/PMNS)" (813) | none | U, O | The couplings are matched with fitted thresholds; the Yukawa structure is solution-specific (SM:1396, 1440) |
| T-10 | 829–862, 978–1062 | OI-string class membership open; comparison protocol specified and not executed; Q1–Q7 open | none | U | UO |
| T-11 | 1028–1042 | LQG, causal sets and asymptotic safety fail A2; they may share the partial-trace features class | none | U | NEG, paper-level; :1327 says independent corroboration is lacking |
| T-12 | 956–974 | No-GUT: "the current empirical state moderately favors the no-GUT universality class" | C-EARLY-3, C-PRED-3 | CB, O | SM:841 notes the no-GUT predictions are not unique to OI; the sentence is a self-assessment |
| T-13 | 1064–1084 | Q8–Q12: seesaw scale, v ≪ f, an intermediate scale, baryogenesis without a right-handed neutrino, nonperturbative emergence | B-SM-HIER-2, B-SM-NU-3, B-SM-BARY-2, B-SM-NP-3 | CB | |
| T-14 | 1086–1096 | Limits; Limit 4: the foundational thesis is unfalsifiable on its own, and the content lives in the specific model, including "the ETH-genericity of the hidden sector" | none | U | Scope limit. Main treats ETH as motivation and (EM) as an open premise (Main:500, 758) |
| T-15 | 1106–1261 | Four-feature audit: Born form, channel unitarity, memory and the commutant pattern transport; P-indivisibility is not established across frameworks; asymptotic safety is "closest" | none | U, T | PE, literature comparison |
| T-16 | 1265–1329 | Corroboration and empirical anchors; under-supported items listed (15.6) | C-PRED-1, B-SM-NU-1 | CB | See SM-41 on the 0νββ sensitivity |

**Observation for the parallel review: Main's independence.** The whole-framework rule makes Main
upstream of every companion paper. Four Main passages draw on content that the companion papers
develop: the C3 horizon realization (Main:76, the horizon partition and its 10¹²² count); the
rest-frame lemma, which takes a causal horizon as given (Main:660–674); the abstract's "specific
SM/GR branch" and its [Substratum §3.3] citation for H-Bell (Main:20); and the "quantitative
predictions" sentence (Main:704, M-33). Whether each is an illustration, a stated input or a
dependency needs the dependency trace the rule prescribes. This audit records them and does not
classify them.

## 3. Book-control findings (`book/ch18-beyond.md`, `book/ch19-open-problems.md`)

Already recorded in ledger §11, and confirmed here: D1 (ch19:20 heading), D6 (ch19:178), D7
(ch18:256), D9 (ch19:88). The arrow-of-time, topology, consciousness, inflation, Hubble-tension and
anomaly entries match ledger rows B-P4-AOT-6, C-TOPO, C-CONJ-1, C-EARLY-1, C-HUBBLE and C-ANOM. The
counts at ch19:362 (twenty-two SM entries with two S and five C; seven gravitational; seven neutrino)
match SM's table and `book/appendix-a-prediction-status.md` A.4.2–A.4.3.

New findings, not recorded in the ledger:

| ID | Location | Finding | Against |
|---|---|---|---|
| K-1 | ch19:106 | "anomaly cancellation forces exactly three candidate matter sectors" | `papers/SM.md`:458: anomaly cancellation "fixes charges given the sector pattern"; the selection of the family pattern "is not supplied" |
| K-2 | ch19:196 | "The framework derives exactly one scalar doublet" | `papers/SM.md`:468: Theorem 11 "does **not** derive the existence of a Higgs doublet"; the doublet is taken as input. Substratum:152 lists it as an output (S-7) |
| K-3 | ch19:46 | "Dark matter is not a particle — it is entropy displacement", stated flatly after the label "Conditional" | `papers/GR.md`:458 (a budget consistency check) and :530 (ρ_E an input). The book mirrors GR:454 (G-17) |
| K-4 | ch19:118 | "The framework derives the total budget" | ch19:116 and `papers/GR.md`:536 table: "partly definitional", 1 − Ω_B by construction |
| K-5 | ch19:356 | "The framework derives the fundamental laws" | A-GR (Einstein equations imported, G3 open); SM's own "compression" classification (`papers/SM.md`:14, 1428) |
| K-6 | ch18:144–152; ch19:28–32 | The non-renormalizability of perturbative quantum gravity is "an artifact" that dissolves, conditional on G3, as the third component of a "cumulative case" | No ledger row. Paper support is limited to "the lattice is the fundamental description" (`papers/SM.md`:1448; `papers/Substratum.md`:225) |
| K-7 | ch18:104 | A candidate Bell realization through non-localized cosmological-boundary modes ("not an established Bell mechanism") | No ledger row; book only |
| K-8 | ch18:56–58 | History-dependent Born-rule corrections at late times | C-CONJ-4 covers the equilibrium mechanism, not this |
| K-9 | ch19:226–248 | Radiative stability of the rotational sector open; a symmetric-integration argument; "a direct computation" gives a smearing radius R ≈ ε | No Lorentz row in the ledger (SM-5); the R ≈ ε computation is stated in the book only, with no paper or record cited at that line |
| K-10 | ch19:194 against `papers/GR.md`:530 | Inflation "Not addressed", while GR's CMB argument uses "adiabatic initial conditions set by inflation" | Cross-document tension (G-24) |

Incidental, outside the two control chapters: `book/appendix-a-prediction-status.md` N5 classes normal
ordering as C ("structural"), while `papers/SM.md`:1456–1460 and ledger B-SM-NU-2 give it as a
genericity heuristic (PE).

## 4. Proposed new ledger rows (proposals only)

These are proposals for the ledger author. Each uses an identifier not used in r3; none is adopted
here. The class given is a suggestion read from the source, for independent review.

**Level B, QM branch.**
- **B-QM-17**: C2 and C3 necessity: fast-bath erasure lemma; C2 quantitative mixing form; C2 process
  form; m ≥ 2^{I*} (M-7, M-8). DM for the persistence form and the capacity bound; CD[mixing hypothesis
  (EM)] for the timescale form. P.
- **B-QM-18**: genericity of the non-permutation witness of C1 among bijections (M-6). DM, exact
  counting.
- **B-QM-19**: Hamiltonian reconstruction from transition data. Phase-locking under (G1)–(G4);
  ancilla-marginal phase-locking for the listed block structures; Bohr-frequency completeness;
  D-gauge completeness and coherent-completion classification under H-BG; orientation no-go
  (M-11, G-8). CD[(G1)–(G4); H-BG]; K in part; NEG for orientation selection.
- **B-QM-20**: channel-level results: separability threshold and non-entanglement-breaking criterion
  for the displayed update (q = 2, prime q); CP-indivisibility for the permutation-dilation family;
  approximate unitarity (M-13, M-14). DM within the stated update; XA and EX.
- **B-QM-21**: intervention dilation (finite comb) with its negatives: no uniform finite realization;
  no horizon-independent intervened representation at fixed d; no exact all-time realization
  (M-4, M-17). DM; NEG for the three negatives.
- **B-QM-22**: passive observation is complete iff the algebra is commutative; passive incompleteness
  and the uncertainty relations do not discriminate the OI core (M-20). DM; K; a scope negative.
- **B-QM-23**: predictive quotients and record identification: Main's canonical tail quotient and
  Substratum Props 24.3–24.5 (M-21, S-12). DM; P with bounded exact controls.
- **B-QM-24**: the imported Barandes correspondence and translation hypothesis (T) for the ≤ n³
  compression (M-10). An imported external result; CD[(T)].
- **B-QM-25**: partition-relativity (M-32). DM given Lemma 3's measure, with the prior as a third
  datum.
- **B-QM-26**: rest-frame selection by a horizon partition (M-24). CD[horizon partition selects n;
  T determines the foliation]. Its dependence on a causal horizon is to be traced for Main's
  independence.

**Level B, substratum and structure.**
- **B-SUB-1**: Theorem 23 as a whole (S-7). CD[E1–E7, M1-T, A1–A6, mixing hypothesis, nearest-neighbour
  premise, H-link, H-cust, H-spin′, H-χ′, H-slope]; Bell-inclusive existence CD[H-Bell];
  Bell-inclusive uniqueness UO. To carry the Stage 2 text mismatch.
- **B-SUB-2**: Theorem 24 generators and Prop 24.2, with Structure Prop 9.5 and Cor 9.6 and GR's
  deep-sector-cardinality corollary (S-11, T-7, G-6). DM for (i) and (iii); CD[alphabet-size
  hypothesis] for (ii); completeness UO; CD[H-BD] for GR's part (b).
- **B-SUB-3**: QM and GR as projections of one object (S-1, S-2, S-17). PE; conditional on G3; joint
  satisfiability undetermined (§9 of r3).
- **B-STR-1**: matrix-model formulations fail A2 and A5 in their standard formulation (T-1, T-2).
  NEG, paper-level, scoped to that formulation.
- **B-STR-2**: LQG, causal sets and asymptotic safety fail A2 (T-11). NEG, paper-level.
- **B-STR-3**: universality-class formalism: Props 9.7a and 9.7b, Cor 9.8 (T-8). DM, standard
  mathematics.

**Level B, GR, cosmology and black holes.**
- **B-GR-10**: universality theorem for the partition-geometry results (G-30). CD[S1–S4]; for (b)
  CD[H-count, H-slope, H-frame, H-Hawking, local boost structure]. The "(a) unconditional" label to
  be assessed as for B-GR-1.
- **B-GR-11**: H-local-lift locality theorem (G-11). CD[H-local-lift].
- **B-COS-6**: MOND interpolation constraints and the simple-ν form (G-19). PE; transition steepness
  bijection-specific (EF-type).
- **B-BH-8**: Theorems A.5 and A.7 (G-29). DM within their stated hypotheses; additive form UO.

**Level B, SM branch.**
- **B-SM-13**: observer-level isotropy, Theorem 1a and Cor 1a (DM, classical exact), with Cor 1b and
  Theorem 1 (CD[observer-level center-free kernel]) (SM-1).
- **B-SM-14**: wave-equation form lemma (SM-2). CD[CI, E4, A5, nearest-neighbour premise].
- **B-SM-15**: observer genericity, Theorem 22 (SM-38). DM for C1 and the C3 floor; C2 and C4 as
  hypotheses.
- **B-SM-16**: Appendix A spectral structure (SM-43). DM; exact, with computational checks.
- **B-SM-FLAV-6**: the registered forward PMNS tests: sum rule 7/6, θ₂₃ octant and value, sin²θ₁₃,
  JUNO precision (SM-37). L or C per row at source; concrete discriminating tests.
- **B-SM-FLAV-7**: y_t(M_Pl) = 1 gives m_t ≈ 207 GeV (SM-32). NEG.
- **B-SM-FLAV-8**: the six-observable Casimir consistency table (SM-36). A retrodiction counted as one
  test; one item rests on Cond 2.

**Level C.**
- **C-LIV**: Lorentz-violation content: no linear term; quadratic coefficient 4σ/45, subluminal,
  anisotropy 4:1:0 at tree level; interacting and rotational-radiative protection open (SM-5, K-9).
  CD[observer-level branch; tree level]; UO for protection. A linear-LIV detection is the stated
  falsifier.
- **C-LQ**: cross-charged leptoquark sector and its M_X window (SM-6). CD[H-link, H-cust, condensate];
  M_X solution-level.
- **C-ERP**: ER=EPR, strong form false at representative level (S-10). PE; no test.
- **C-PRED-10**: Tully–Fisher evolution tension, McGaugh et al. 2024 (G-21). NEG (stated tension).
- **C-PRED-11**: cluster scale: Coma matched; rich-cluster residual 1.0–1.5 (G-22). NEG (partial).
- **C-PRED-12**: CMB peaks match ΛCDM given ρ_E ≈ Ω_CDM ρ_crit as an input; CLASS check at ν = 10⁻⁴
  (G-24). CD with an EF input; reproduction of ΛCDM, a cross-check rather than a derivation (XC-type).
- **C-PRED-13**: Bullet Cluster frozen displacement and the epoch-local relaxation kernel (G-23). PE;
  or revise B-COS-5 to record the kernel reading.
- **C-STR-1**: observer-admission reading of the landscape (T-5). PE; contradicted in part by B-QM-18
  and B-SM-15; no test.
- **C-STR-2**: swampland consistency (T-3). PE; consistency only.
- **C-STR-3**: horizon holography in OI (T-4). CD[H-slope and the §8.5(b) conditions]; the A/4 bound
  at Structure:453 unsupported.
- **C-STR-4**: four-feature cross-framework audit (T-15). PE.
- **C-STR-5**: Limit 4, the foundational thesis unfalsifiable on its own (T-14). Scope limit.
- **C-QG-1**: non-renormalizability as a regulator artifact (K-6). PE, conditional on G3.
- **B-BELL-9**: candidate Bell realization by non-localized cosmological-boundary modes (K-7). PE.

**Proposed additions to ledger §11 (document disagreements), as questions, not corrections.**
- The status of Lemma 1 (M-29).
- Substratum's Stage 2 text against SM (S-7, S-8).
- Prediction counts in Substratum Class B against SM's table, and Substratum:199 against :525 (S-21).
- λ(M_Pl) = 0 classed S in SM against CD in the ledger (SM-30).
- GR's Σm_ν "prediction" against SM:1468 (G-15).
- SM's three m_H statements (SM-34).
- Structure:733 against Main:147–151 and SM Theorem 22 (T-5).
- Structure:179 against GR:30 and 611–679 (T-6).
- Structure:403 and 1317 against SM's branch condition for Majorana neutrinos (T-3).
- The book findings K-1 to K-5 and K-10.

## 5. What this pass did not do

- `book/appendix-a-prediction-status.md` B1–B14 and F1–F9 were not classified. Ledger r3 assigns their
  classification to "the coverage audit", but condition 6 names only the five papers and chapters
  18–19, so they lie outside this pass. They remain unclassified in the ledger.
- The SM §7.1–§7.5 sub-derivations (`papers/SM.md`:849–1267) were checked at the level of their
  stated results, statuses and the §7.6 table, not line by line. The same holds for Structure
  §13.1.1.1 and §14.7–§14.9, and for the bodies of the long proofs in Main §3.4 and GR §3.3.
- No kernel identifier cited by a source was checked against
  `verification/lean-manuscript-census.json` or the Lean modules. G-9's question whether the layer-flow
  form is manuscript-carried, while B-QM-15 says its families are not, is left open.
- No script, probe or record under `verification/` was run. Statements that a check was exhaustive,
  exact or numerical are taken from the sources.
- Main's independence (the observation after §2.5) was recorded and not traced.
