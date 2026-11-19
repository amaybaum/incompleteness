# A1-REMAINDER — what still needs total finiteness after the 2026-11-19 landings

**Status.** Writer's paper-only audit, revised after the independent review of `299aa760` ([#1421 comment 7022761030](https://github.com/amaybaum/incompleteness/pull/1421#issuecomment-7022761030), REVISE); a delta review of the revised head is required. No new proof, Lean,
manuscript edit, premise adoption or merge. A1 (Main posit ledger item (ii)) remains open and
unadopted; physical measurement sourcing remains not passed.

**Authorization and scope.** Owner `amaybaum`, recorded at
[#1055 comment 7022346035](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7022346035),
2026-11-19T21:11:44Z: "yes, start A1-REMAINDER". The comment fixes the question (which conclusions
still need A1 after the landings #1399, #1400, #1402, #1404, #1408, #1412, #1413, #1415, #1417,
#1418, #1419 and #1333, and the weakest assumption supporting each of the others), the three-way
classification, the removal-readiness and inflow items, the controls fixed in advance, and the
limits: paper-only, stop at any row that needs a new lemma and name it, no claim of exhaustiveness.

**Goal link (§A.47), from the authorization.** Decide whether A1 can be removed from OI's
foundations, and if not, what the irreducible residue is, so that the next step (remove it, or
replace it with an observable hypothesis) is chosen on evidence.

**Source pin.** `main` at `21e16c61e4dfa07f5902fdc113fbf8eeb974d441`. `M:n` is line `n` of
`papers/Main.md` at the pin; `GR:n`, `SM:n`, `Sub:n`, `Str:n`, `Comp:n` are lines of
`papers/GR.md`, `papers/SM.md`, `papers/Substratum.md`, `papers/Structure.md` and
`papers/Computation.md` at the pin. Audit records are cited by the short names below, all on `main`
at the pin, paths relative to `verification/`.

| Short name | Path | Role here |
|---|---|---|
| FCLASS | `audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md` | 29-row F1/F2/F3/F4/A1 matrix; defines F1–F4 |
| NEC | `audits/foundations/a1-necessity-20261117/ASSESSMENT.md` | five-family reconciliation |
| ROOTS | `audits/foundations/a1-main-roots-20261118/AUDIT.md` (questions in `ROOTS.md`) | Main roots R0–R8 |
| CENSUS | `audits/foundations/a1-09-dependency-census/CENSUS.md` §§17, 22–27 | declaration and site traces |
| RIGID | `audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md`; `lean-mathlib/OIBridge/ObservableRigidity.lean` | compact-orbit recurrence replacement |
| HIST | `audits/foundations/a1-p8-history-bridge-20261119/RESULT.md` | full-history next-read bound |
| GLUE | `audits/foundations/a1-p12-common-carrier-20261119/A1-P12-GLUE-1.md` | one local reversible infinite carrier |
| P7B | `audits/foundations/p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | A1-free shell count under H1–H14 |
| DS | `audits/foundations/a1-ds-20261117/A1-DS.md` | de Sitter source screen |
| LADDER | `audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md` | F11 near-return |
| REC-1 | `audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md` | contract (V)(M)(I)(P), (RIG) at :68; Props 3.4, 5.1, 6.1, 6.2; verdict table :543–552 |
| RM | `audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md` | prior record of the A4 finding (:47) |
| A1-11 | `audits/foundations/a1-11-local-gauge-forward/FORWARD-ALGEBRA.md` | forward local algebra |
| A1-05 | `audits/foundations/a1-05-p8-observer-selection/SOURCE-MATRIX.md` | P8-M / P8-S |
| PREP | `programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md` | stationarity, budget, escapes |
| OA-1 | `programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` | typing of μ-O, μ-G, μ-R |

**Classes.** (a) A1-free as stated: the cited proof uses no finiteness of the total physical
carrier (it may use a finite representative that it constructs, or finite visible data).
(b) A1-free under a named weaker hypothesis that an existing on-`main` proof supplies. (c) Still
needs total A1: the cited step uses finiteness of the whole carrier, and no traced proof covers the
conclusion without it. A row whose A1-free form would need a lemma absent from the traced corpus is
(c), with the lemma named as its repair; the lemma is not attempted. Several theorems are true
mathematical statements about finite representatives; for those the class refers to the physical
reading the corpus attaches (M:60, M:730 item (ii)), and the row says so. Evidence layers: Lean
(kernel-checked declaration on `main`; not built in this audit), exact, paper, numerical.

## 1. Consumer table

### 1.1 Main

| # | Claim and location | How A1 enters (exact step) | Class | Weaker hypothesis; where proved; layer; sourced or posited | Observable or testable? | Pin |
|---|---|---|---|---|---|---|
| M1 | Lemma 3, selection clause: the counting measure is the maximal-entropy invariant measure (M:54; M:58) | A uniform probability exists only on a finite carrier, and Shannon entropy over invariant probabilities is taken relative to counting. On an infinite carrier there is no counting probability and the maximum is undefined. CENSUS §17 row M:54,84 (A/F); ROOTS R0 row 3 | (c) | None traced. M:58 already treats a structured hidden prior as a realization datum, which replaces selection by a supplied law; that is a posit, not a selection. Repair options in §2 R1 | No: a selection principle over laws on the whole carrier | 21e16c61 |
| M2 | μ-G, μ-O, μ-R and posit (iv) (M:60 end; M:730 (iv); OA-1 r5:100–109; PREP 1.5(b), (b′)) | μ-G is M1. μ-O is "uniform on the orbit of the actual microstate", derived at OA-1 r5:101 from M:54/M:60, whose uniqueness statement is for a finite cycle; a countably infinite orbit carries no invariant probability (equal point masses cannot sum to one). μ-R is uniform on the finite union of record-compatible orbits (PREP 1.5(b′)). The static budgets log₂(\|S\|/ℓ) and log₂(\|S\|/\|U\|) are counting quantities | (c) | None traced. PREP 1.1–1.3 (stationarity, flux balance, no production in law) hold for any T-invariant probability on a measurable carrier [paper, W in PREP], so the exclusion of native autonomous history survives; the typing of which invariant laws are native does not. Repair: posit P-μ (§2 R1) for μ-G and μ-R; for μ-O, lemma L2 (an ergodic component of a declared invariant law as the orbit-level law, with its static budget) | No | 21e16c61 |
| M3 | Baseline transition matrices under the uniform hidden prior; uniform-prior one-step theorem input; doubly stochastic corner (M:60 list; M:113; M:208; M:274; M:280; M:286) | T_ij = \|{h}\|/\|C_H\| counts a finite hidden set; ρ_H = I/m on finite H; "uniform-prior marginal of a bijection is doubly stochastic" | (b) | Rooted maps under any normalized hidden prior shared by roots: Γ_n(a,b) = ρ{h : X(Tⁿ(a,h)) = b} for an invariant product law ν⊗ρ on a measurable carrier (`ObservableRigidity.rootedFamily_productLaw`, Lean; RIGID "common hidden-prior convention", paper). M:135 and M:141 already allow an arbitrary shared μ_H. Double stochasticity: GLUE proves it for its gate class (paper); for a T-invariant law u_V⊗ρ the column sums are \|V\|·μ(T^{−n}C_b) = 1, a one-line consequence of invariance (noted in the review of `299aa760`). The residue in this row is therefore the posit P-μ with ν uniform (R1), not finiteness. Posited (the law) | Rooted matrices are observable given a root-independent hidden preparation; double stochasticity is checkable on visible data | 21e16c61 |
| M4 | §2.3 one-step theorem: non-permutation T implies P-indivisibility (M:113–127) | Step 1 (M:121): a bijection of a finite set has finite order N, so T^(N) = I | (b) | Weakest traced hypotheses, in increasing strength: ladder F11, a single common near-return with margin 2ε < m after the non-permutation time (LADDER §3.4, paper; REC-1:535–537); REC-1 (RIG), subsequential rigidity μ(C_a △ T^{−n_k}C_a) → 0 (REC-1:68, Prop. 3.4, paper); RIGID's compact closure of the joint indicator orbit, which supplies (RIG) (RIGID proof; `ObservableRigidity.exists_pIndivisibleWithin_of_nonPermutation`:358, Lean). Each with a bimeasurable bijection T preserving a normalized μ and positive cell masses; Main's uniform prior is the case μ = u_V⊗ρ. Conclusion: some finite horizon {0,…,n} after the non-permutation time is P-indivisible (REC-1 U1, :545). Strictly weaker than finite S inside the invariant-law class (RIGID rotation × Bernoulli example). Posited (μ, the return condition, reversibility). Lost: the specific N and Γ_N = I | All three return conditions concern unboundedly late times; the sources give no finite-window test for them, and REC-1 Prop. 5.1 shows the first indivisible horizon has no uniform bound across models. Observable alternative for a given family: an observed C4r (row M6) | 21e16c61 |
| M5 | History readback + finite recurrence (M:135–139) | Proof: φ of finite order L gives Γ_L = I and Γ_{t+L} = Γ_t; periodicity bounds s ≤ min(k, L−1) | (b) in the invariant-product-law class; (c) otherwise | Histories meeting at k ⇒ some Γ_s, 1 ≤ s ≤ k, non-permutation, with neither recurrence nor an invariant law (REC-1 Prop. 6.1, :505; RIGID scope bullet 2; paper); then M4's route under F11 or (RIG) (REC-1 U2, :546). Not covered: shared priors that give no invariant product law (RIGID scope bullet 1: register swap with prior δ₀), the bound s ≤ L−1 and the exact cycle endpoint (REC-1 U2: these need (RET) at L). Repair for the uncovered priors: lemma L4 or scope narrowing | As M4 | 21e16c61 |
| M6 | Overlap-and-return theorem (M:141); C4r/C4e no-go | Γ_n = I is supplied; finiteness of C_V × C_H appears only in the setup | (a) | Matrix form needs only row-stochastic Γ_s on finite V (`RecurrenceHorizon.pIndivisible_of_identity_return_of_overlap`, `CausalReadback.c4r_implies_pIndivisible`:134, Lean). Near-return form F11 (LADDER §3.4, paper; `ObservableRigidity.tv_revives_of_nearReturn`:88, Lean) | C4r (a strict increase of rooted-row distance) can be supported by finite data, statistically, with a stated sampling error and a root-independent hidden preparation; C4e needs an exact equality that no finite sample verifies. An observed C4r gives P-indivisibility of the observed family only; it does not recover M4's implication from every non-permutation map | 21e16c61 |
| M7 | Full-support equivalence (M:139 Scope; M:80 item (2)): (i) index-free form, a readback gap at some finite order ⇔ some Γ_s, s ≥ 1, non-permutation ⇔ not P-divisible on some {0,…,n}; (ii) L-indexed form, gap below L ⇔ non-permutation Γ_s with s < L ⇔ indivisible on {0,…,L} | (ii) uses the exact return Γ_L = I and stochastic-inverse rigidity; the index L is the finite order | (i) (b); (ii) (c) | (i) REC-1 Prop. 6.2 (REC-1:521–533, paper) under (V), (M), (I), (P), (RIG) and (FS), each direction proved separately; only (b)⇒(c) uses (RIG), and it holds equally with F11's single near-return (REC-1:535–537). (ii) REC-1 U2 (:546): the bound s ≤ L−1 and the horizon {0,…,L} need (RET) at L. Repair for (ii): scope narrowing to finite representatives | (i) As M4; (ii) No | 21e16c61 |
| M8 | Routed readback, "so for some n" (M:145) | `rootedMap_periodic` on finite C_V × C_H (CENSUS §27.8, M145 row) | (b) | Only the storage-time overlap Γ_s(a,x), Γ_s(b,x) > 0 is used for indivisibility. A later revival follows under F11 or (RIG) (paper) and under RIGID's compactness in Lean (`ObservableRigidity.exists_reviving_return_of_overlap`:342). The write/store/read clauses are formalized only on finite carriers (`PhysicalC4Discharge`, `PhysicalC4StorageReadback`); their transfer is paper-level | Overlap and reappearance clauses are rooted-map data; the write clause is hidden | 21e16c61 |
| M9 | CP-indivisibility theorem (M:330–334) | P witness from §2.3's finite route; channels Φ_t = Tr_H[U^t(ρ⊗μ_H)U^{−t}] with U a permutation unitary on finite H | (c) | The implication "P witness ⇒ CP-indivisibility for diagonal-preserving channels on finite V" is A1-free given a supplied witness (ROOTS R4 row 3; LADDER §5). The channel family on an infinite measurable hidden carrier (a Koopman dilation on ℂ^V ⊗ L²(H,ρ) and its diagonal preservation) is not defined in the traced corpus: lemma L6 | The P witness is observable (M6); CP-indivisibility of the ontic channel is not | 21e16c61 |
| M10 | All-time rooted classification and periodicity of a fixed realization (M:644) | `pper_of_finiteRootedRealizable` (finite order); converse by finite response table (CENSUS §27.8 M644 row) | (a) as a theorem about finite realizations; (c) for the physical reading that nature's all-time rooted family is periodic | No replacement and none is needed for the theorem. Without A1 exactly aperiodic families have exact realizations: GLUE (stationary Markov M_p on one local reversible carrier on ℤ, paper) and the RIGID rotation example (no positive exact identity time, paper) | Exact periodicity versus aperiodicity is not decidable on a finite window | 21e16c61 |
| M11 | Bijectivity of the representative: eventual image, injectivity ⇒ surjectivity, merge prong (M:54; M:60; M:730 (iii)) | Eventual image of a map on a finite set; injective ⇒ bijective on a finite set; prong 1 uses the uniform-prior doubly stochastic marginal on finite C_H | (c) as stated | M:60 and M:730 (iii) already offer the alternative: adopt reversibility as the information-conservation postulate "at no cost to the downstream results". That is a posit (bimeasurable bijection on a measurable carrier), not a lemma, and RIGID/HIST/GLUE all assume it | The anchor is unitarity of the emergent description (Sub:94, matter-wave interference); that constrains the effective quantum dynamics, not ontic bijectivity | 21e16c61 |
| M12 | §3.2 representation: finite H, permutation unitary, Born-form identity, reverse lemma (M:266–288) | Finite H is the setup | (a) for the representation | Finite hidden spaces are constructed per law (M:60 "constructed, not assumed"; M:706; S ⇒ D, `Equivalence.S_imp_D`, Lean). Reading the finite channel as nature's channel needs A1 (as M3, M9) | — | 21e16c61 |
| M13 | Orbit capacity log₂ p (M:60) and genericity count P_perm (M:147–151) | Finite orbit of period p; uniform count over the finite set of bijections | (c) for the physical reading; non-root | ROOTS R0 row 3 and R8 row 1: neither is a premise of R1–R3. Repair: scope narrowing to finite representatives | No | 21e16c61 |
| M14 | Characterization theorem window t ≪ t_R (M:540) | t_R is "the Poincaré recurrence time of any realizing substrate" | (a) | CENSUS §27.8 M540–546 row: the proof at M:634 uses a witness order and finite horizons and never consumes t_R; without a recurrence premise the window condition is vacuous | — | 21e16c61 |
| M15 | C3 capacity bound log₂\|C_H\| ≥ I* (M:508–518) | Counts the hidden states of a realization | (a) | Holds for every finite realization; class D is finite by definition (CENSUS §27.8 M508–518, M620 rows). For an infinite hidden carrier the bound does not bind | The visible quantity I* is observable; the hidden count is not | 21e16c61 |
| M16 | Physical-memory theorem and C2 quantitative form (M:457–475) | Printed in a uniform-prior finite coupling model (CENSUS §17 row 163,457,471: F) | (c) as printed | The total-variation part averages a kernel against a reference prior; a measurable-carrier statement is not in the traced corpus: lemma L7 (restatement on a measurable hidden space). The visible entropy-continuity step uses finite V only | M_k is observable on finite data; π_H and ε are hidden | 21e16c61 |
| M17 | Coupling-graph causal cone, finite-site presentation (M:362); Bell ceiling (M:414–416) | "Finiteness of V is used in the first step" of the finite-site proof | (a) | The same paragraph gives the arbitrary-site form with finite read sets; Corollary part (2) at M:414–416 covers a site set of any cardinality with finite setting and readout regions (FCLASS rows 05, 25; ROOTS R6) | Finite signal speed and no-signaling are tested properties of the emergent description; the ontic read sets are not observed | 21e16c61 |
| M18 | §4.6 theorem: τ_B(V) ≤ τ_mix + O(ε) for the iterated compression K = PUP (M:748–758) | Scope at M:764 lists finiteness of S; K and the inner product use the counting measure; exact Koopman of a finite permutation recurs (M:750) | (b) for the forward operator-decay step only | A1-05 P8-M (SOURCE-MATRIX:15–17, paper): supplied normalized invariant μ, P the conditional expectation onto the declared local observables for that μ, finite readout support with a declared locally finite dependence cone covering its writes and reads, and a quantitative bound ‖Kⁿ‖ ≤ C e^{−nΔt/τ_mix} on centred observables; no total count. Not covered, and a source gap that does not depend on A1: the transferred τ_B bound with its record threshold and error estimate; FCLASS row 23: "Do not promote this to an A1-free full P8 observer-selection theorem". HIST adds an exact full-history next-read bound under a positive read/write table (paper). Posited (μ, EM, positive table). Without A1 exact compressions are not forced to recur (ROOTS R7 row 1, REC-1:583–611), but no traced result transfers EM to PUⁿP | EM concerns the iterated compression, which is not what records show (M:764 (ii)); HIST's bound concerns exact next-read contrasts on declared histories, which are finite data | 21e16c61 |
| M19 | §4.6 observer-selection corollary, equilibrium phase: "(S,φ) in its equilibrium macrostate ⇒ every local subsystem in local equilibrium" by canonical typicality (M:762) | Canonical typicality is a statement about the normalized uniform measure on the unit sphere of a finite-dimensional energy subspace (NEC typicality row; ROOTS R7 row 3); the corollary applies it to the whole finite (S,φ) | (c) | A1-05 P8-S stops at the selected normalized equilibrium state (FCLASS row 24). Repair: scope narrowing (take local equilibrium of Σ_loc as a supplied state), or lemma L8 | Local thermal statistics of a region are observable in principle; the global-to-local inference is not | 21e16c61 |
| M20 | Anti-Boltzmann-brain corollary (M:760) | Inherits the finite (S,φ) setting of M18 | (b) at the operator step; the remaining steps are A1-independent source gaps | The chain is EM + τ_mix ≪ τ_S + uniform erosion (M:163), none of which counts states; at the operator step it reduces to M18's inputs, and the τ_B transfer it also uses is M18's A1-independent source gap. Local equilibrium of the brain's neighbourhood enters as a definition, not via M19. Posited | As M18 | 21e16c61 |
| M21 | Ledger (ii) gauge reading: deep-sector cardinality unobservable; transfer of conclusions across representatives (M:60; M:730 (ii)) | Theorem 24(iii) is a finite decoupled-factor identity (Sub:257–262); M:60 excludes infinite and coupled sectors | (b) for finite windows; (c) for the all-time infinite extension | GR Appendix B (GR:871–905, paper): for a site set of any cardinality under (D1)–(D5), T_ij(mΔt), m ≤ n, is independent of the cardinality and of the law ν beyond the cone. (D2)/(D3) are hypotheses on the dynamics and (D5) is the prior posit μ_H = u_{B_n}⊗ν (GR:877–883). The all-time coherent-channel invariance for an infinite normalized decoupled factor is not proved (Sub:262 "not established by finite uniform counting"): lemma L9 | Unobservable by construction (gauge) | 21e16c61 |

### 1.2 Companion root claims

| # | Claim and location | How A1 enters | Class | Weaker hypothesis; where proved; layer; sourced or posited | Observable or testable? | Pin |
|---|---|---|---|---|---|---|
| C1 | Classical horizon temperature as a counting derivative, H-count (GR:58) | "Under A1, restrict the finite total system to a conserved energy shell"; uniform counting on the shell gives P(i) ∝ Ω_H(E − e_i) | (b) decoupled; (c) coupled | P7B Theorem (P7B:205–223, paper): H1–H14 including H2 finite boundary modes, H4 normalized shell counting ⊗ one deep law ν of any cardinality, decoupled product dynamics, H6 slope, H8 time-even readout, H9 positive paired flux. The coupled case is parked at node 6.3 (P7B:185), at the existence of an invariant shell law (an R1 item). The unconditional replacement (finite boundary count alone) is refuted (P7B node 5). H2, H4, H6 posited | H11/H12 detector matching is an observable requirement in principle; H2/H4/H6 are not | 21e16c61 |
| C2 | Calibration ħ = c³ε²/(4Gσ) and the 1/4 (GR:88; GR:673) | Inherits C1 through H-count | (b)/(c) as C1 | As C1; GR:673's universality claims (U1)–(U3) do not use A1 | As C1 | 21e16c61 |
| C3 | Deep-sector corollary without H-BD (GR:132–138) | Uniform prior on finite C_D in §3.2 | (b) | GR Appendix B, any cardinality (paper; CENSUS §17 GR row 1): (D1) finite V, (D2) finite read sets, (D3) locally finite coupling graph, (D4) finite alphabets on V ∪ B_n, and the prior posit (D5) μ_H = u_{B_n}⊗ν (GR:877–883) | Gauge | 21e16c61 |
| C4 | H-BD and the boundary-only lemma (b) (GR:112–128; H-BD at GR:122) | "At most a fraction Δt/τ_BD of d ∈ C_D"; the proof counts on finite C_D with injectivity | (c) as stated | A measure-theoretic H-BD with a normalized deep law is not in the traced corpus: lemma L10 (CENSUS §17 GR row 1: "the counted H-BD step remains F") | τ_BD is not fixed by S1–S4 (GR:128) | 21e16c61 |
| C5 | Operational completion, OI⁺, typed and quasilocal identifications (GR:239–282) | Finite carriers of the operational theory | (a) | CENSUS §25.9 rows GR:239–241, :249–255, :273–282: A regarding physical A1; the quasilocal completion takes an arbitrary site set with finite local stages | — | 21e16c61 |
| C6 | Substratum A1 and Theorem 23 (Sub:92; Sub:121–131; Sub:193) | A1 is listed among E1–E7, A1–A6; Stage 2 uses the finite periodic lattice of A4 (Sub:98) | (c) | Stage 1's finite S is constructed per window (S ⇒ D), A1-free. GLUE supplies one local reversible carrier on an infinite lattice for stationary Markov laws (paper), short of the observer, wave block, continuum and matter steps (FCLASS row 22; NEC P12 row). Even with posit (ii) removed, A4's finite periodic lattice with finite site alphabets re-implies A1 (`SubstratumInterfaceAudit.a1_of_finite`:109, Lean; CENSUS §17 SM:210 row) | No | 21e16c61 |
| C7 | d = 3 selection under A4 (SM:210) | "coupling graph is a d-dimensional periodic lattice" | (c) via A4 | As C6: finite alphabet plus a finite periodic site model supplies A1 without naming it (CENSUS §17 SM row 210). Repair: obligation O-A4 | — | 21e16c61 |
| C8 | Theorem 24 (i), (iii); Corollary (iii) exact transfer, including recurrence-scale properties (Sub:251–268) | (i) uses uniform ω_H on finite C_H; (iii) a finite factor A; the Corollary transfers a recurrence-scale property "established on a finite representative" | (a) for the finite identities; (c) for transfer of recurrence-scale content and for infinite extensions | Finite-window population law: C3. Infinite decoupled factor: L9. Recurrence-scale content: inherits M4/M7 | Gauge | 21e16c61 |
| C9 | Storage and memory: "S finite capacity (under A1)" (Sub:44) | Explicit | (c), interpretive | Scope narrowing; no theorem rests on the sentence at the traced depth (CENSUS §23.2 row 1) | — | 21e16c61 |
| C10 | Equilibrium scope claims (Sub:56; Str:718) | Consume Main §4.6 | as M18–M20 | CENSUS §23.2 row 3 | — | 21e16c61 |
| C11 | OI-class substrata (A1–A6) in Proposition 9.5 (Str:646) | Class definition | (c) definitional | Str:629's embedded-observer definitions do not force a finite hidden carrier (CENSUS §17 Structure row 1). Narrowing the class to A2–A6 plus the M4/M18 posits is a definition change | — | 21e16c61 |
| C12 | Finite-carrier capacity comparison (Comp:182; CENSUS §23.2 row 5) | "The framework's finiteness hypothesis (A1)" | (c) explicit | The finite-orbit decision test and capacity comparison use A1 by statement | — | 21e16c61 |
| C13 | Forward local gauge algebra (A1-11 §1) | None | (a) | FCLASS rows 20–21 (axes N, N, N, N, N) | — | 21e16c61 |
| C14 | Exact linear rule shell splitting into cycles, motivation for (EM) (M:730 (v); SM §4.2) | Cycle counts on a finite lattice | (c) for that motivation; not a premise of any theorem traced here | M:764 (ii) states the cycle structure does not settle (EM) | — | 21e16c61 |

## 2. Residue summary (class (c) items)

**R1 — the canonical measure.** M1, M2, the coupled case of C1 (existence of an invariant shell
law, P7B 6.3), and C4. *Reason.* A uniform probability exists only on a finite set, and "maximal
entropy among invariant measures" is defined relative to counting; μ-O is unique only on a finite
orbit, μ-R only on a finite orbit union. Every A1-free replacement traced (RIGID, HIST, A1-05 P8-M,
P7B, GLUE, GR Appendix B) takes a normalized invariant law, or a product law with a uniform finite
factor, as a supplied input. *Cheapest repair.* Scope narrowing: replace posit (iv)'s selection by
the posit P-μ, "a declared normalized T-invariant law μ, for Main's rooted convention a product
ν⊗ρ with ν(a) > 0", which M:58 already admits as a realization datum. A selection-preserving
alternative needs lemma L1: a characterization of a distinguished invariant law (for example the
product uniform law as maximal entropy density among invariant laws) for the declared class of
local reversible rules on a finite-alphabet site product. L2 (μ-O as an ergodic component of a
declared invariant law) and L10 (measure-theoretic H-BD) are the smaller repairs inside this
family. The doubly stochastic corner of M3 reduces to P-μ with ν uniform by a one-line invariance
argument, so it carries no separate repair.

**R2 — exact common return.** The exact endpoint Γ_L = I and the bound s ≤ min(k, L−1) in M5,
the L-indexed form (ii) of M7, the physical reading of M10, μ-O and the orbit capacity of M13.
*Reason.* Each uses the finite order of a permutation. F11, REC-1's (RIG) and RIGID's compactness
replace exact return by near-return, which carries the indivisibility conclusion and, under (FS),
the index-free equivalence (REC-1 Prop. 6.2), but not the exact endpoint or the index L.
*Cheapest repair.* Scope narrowing to finite representatives for these statements; lemma L4
(near-return for shared priors that give no invariant product law) where M5's uncovered priors
are to be kept in A1-free form.

**R3 — bijectivity recovery.** M11. *Reason.* The eventual-image restriction and
injectivity-to-surjectivity are finite-set arguments. *Cheapest repair.* The posit already printed
as an alternative at M:60 and M:730 (iii): reversibility as information conservation. No lemma.

**R4 — A4's finite periodic lattice.** C6, C7, and through them Theorem 23. *Reason.* Sub:98
defines the coupling graph as "a finite periodic lattice"; with finite site alphabets
`SubstratumInterfaceAudit.a1_of_finite`:109 gives A1. The same finding is recorded earlier at
RM:47. *Cheapest repair.* Obligation O-A4. Its restatement half already exists in the kernel: the
predicate `SubstratumInterfaceAudit.A4` (:98) is stated on an arbitrary additive group of sites
with no finiteness clause. What remains is to recheck each Stage-2 step that uses the finite
periodic lattice, including Theorem 19's finite normalizer (not traced here). Without O-A4,
deleting posit (ii) leaves A1 in force for the reconstruction.

**R5 — global typicality.** M19. *Reason.* Canonical typicality
is a finite-dimensional energy-shell theorem. *Cheapest repair.* Scope narrowing (local equilibrium
as a supplied state, as A1-05 P8-S already records); lemma L8 (local-equilibrium marginals of a
supplied invariant law on an infinite carrier) if the global-to-local inference is to be kept.

**R6 — finite-carrier channel and model statements.** M9 (L6: Koopman dilation channel family on
ℂ^V ⊗ L²(H,ρ) and its diagonal preservation), M16 (L7: physical-memory theorem on a measurable
hidden space), M21 and C8 (L9: coherent-channel invariance under an infinite normalized decoupled
factor), C9, C11, C12, C14. *Cheapest repair.* Scope narrowing for C9, C11, C12, C14; the named
lemmas for M9, M16, M21.

**Index of named repairs (none attempted here).**

| Id | Kind | Content | Rows |
|---|---|---|---|
| P-μ | Posit | Declared normalized T-invariant law; product ν⊗ρ with ν(a) > 0 for the rooted convention | M1–M3, M18, C1 (coupled) |
| L1 | Lemma | Characterization of a distinguished invariant law for the declared class of local reversible rules on a finite-alphabet site product | M1 |
| L2 | Lemma | μ-O as an ergodic component of a declared invariant law, with its static budget | M2 |
| L4 | Lemma | Near-return route for shared hidden priors that give no invariant product law | M5 |
| L6 | Lemma | Koopman dilation channel family on ℂ^V ⊗ L²(H,ρ); diagonal preservation | M9 |
| L7 | Lemma | Physical-memory theorem on a measurable hidden space | M16 |
| L8 | Lemma | Local-equilibrium marginals of a supplied invariant law on an infinite carrier | M19 |
| L9 | Lemma | Coherent-channel invariance under an infinite normalized decoupled factor | M21, C8 |
| L10 | Lemma | Measure-theoretic H-BD with a normalized deep law | C4 |
| O-A4 | Scope change | A4 without the finite periodic lattice (the kernel predicate `SubstratumInterfaceAudit.A4`:98 already has no finiteness clause); recheck of the Stage-2 steps that use periodicity | C6, C7 |
| O-INFLOW | Obligation | §5 | — |

## 3. Removal readiness

**Verdict: posit (ii) cannot yet be replaced by observer-relative finiteness alone.** Finite
visible alphabet (F3) plus finite causal support (F4) carries every result that uses only Lemma 1
(§6 controls; M6, M12, M14, M15, M17, C5, C13; C3 and the finite-window part of M21 additionally
need the prior posit (D5)), but it does not carry R1, R2, R4 or R5. GLUE
is a direct countercontrol: its carrier is F1 + F4 on an infinite lattice, its flip chain has
noncompact indicator orbits and P-divisible rooted maps (GLUE "Scope of the result"), so F3 + F4
gives neither the recurrence-family conclusion nor any measure selection.

**Hypotheses a replacement must state**, with their status:

| Id | Hypothesis | Replaces | Status | Observable? |
|---|---|---|---|---|
| H-F3 | Uniform finite visible capacity of the observer (Definition, M:42; Lemma 1, M:46) | — (already present) | Stipulated | Operationally, as finite resolution |
| H-F4 | Site factorization (M:730 (viii)); each output reads a finite set of sites and each site is read by finitely many outputs (M:730 (xiii)); finite alphabets on the cone (GR (D4)); finite readout region (GR (D1)) | finite-site cone presentation | Posited | Finite propagation speed of the emergent description is tested; the ontic read sets are not |
| H-REV | T is a bimeasurable bijection of a measurable carrier | M11 (R3) | Posited; printed alternative at M:730 (iii) | No more than A2 under A1 |
| H-μ | A declared normalized T-invariant law μ; for Main's rooted convention μ = ν⊗ρ with ν(a) > 0 | M1–M3, M18, C1 coupled (R1) | Posited | No: a law on the whole carrier |
| H-RIG | A return condition after the non-permutation time; weakest traced form ladder F11's single near-return with margin, then REC-1 (RIG), then RIGID's compact orbit closure (Lean); with (FS) it also gives M7 (i) | M4, M5, M7 (i), M8 | Posited | The sources give no finite-window test; each form concerns unboundedly late times |
| H-A4′ | A4 without the finite periodic lattice clause | C6, C7 (R4) | Requires O-A4 | — |
| H-P7 | P7B H1–H14, including H2 and H4 | C1, C2 | Posited | Detector side only (H11, H12) |
| H-IN | A stated condition on incoming boundary supply (§5) | none under A1 | Open | §5 |

Existing posits unaffected by the change: (EM), the rate condition, uniform erosion, (iv)'s role
as now narrowed, (v)–(xiv).

**Relabelling test.** H-μ and H-RIG are as unobservable as A1: H-μ is a law on the whole carrier,
and every traced form of H-RIG concerns unboundedly late times, for which the sources give no
finite-window test (REC-1 Prop. 5.1: no uniform bound on the first indivisible horizon). The
finite-window consequences of H-μ (every single-time block statistic constant in time, PREP 1.3)
hold equally under A1's counting measure, so they do not discriminate the two. For the
measure-family consumers (R1) and the recurrence family taken through RIGID, the replacement is
therefore a relabelling in observability, although it is logically weaker: RIGID's rotation
example and GLUE's aperiodic chains satisfy the replacement and violate A1. Two parts are not a
relabelling. (1) For a given observed family, P-indivisibility can be obtained instead from an
observed C4r revival on an accessible window (`CausalReadback.c4r_implies_pIndivisible`, Lean):
a strict inequality, supported by finite data only statistically, with a stated sampling error and
a root-independent hidden preparation. C4e needs an exact equality and is not finitely verifiable.
This trades the inaccessible recurrence time for an accessible witness for that family; it does
not recover M4's universal implication from every non-permutation map. (2) The Lemma-1-only results never used A1. H-REV has the same observational
status as A2 under A1, so it adds nothing unobservable that A1 did not already carry.

## 4. Testable-replacement scan

No new derivation; each entry cites what the sources state.

| Candidate | What it would preserve | Observable it predicts | Assessment |
|---|---|---|---|
| Horizon-bounded finiteness (de Sitter entropy) | DS Gate 4 is "Not entered: closure of the physical OI patch has not been established"; its table lists recurrence-scale P-indivisibility, P8, P12(b) and GR:58 as not recovered, with H8, a compatible root-shared prior and an earlier non-permutation map absent for the first. DS states no positive preservation | A finite Gibbons–Hawking entropy, inferred from Λ (an inferred quantity in the sense of §A.24). Under H3 + H4 + H5 + H6 at the benchmark, a log-count excess of about 2 × 10⁶⁰ (DS §2.3): a consistency constraint, not an empirical prediction | DS stops at H5/H8: finite entropy does not bound cardinality (Countercontrol 1.1), finite quantum dimension does not give an exact finite permutation (Countercontrol 1.2), and direct restriction of the unchanged rule is not autonomous (§3.2). Verdict class at most F4-type. Not a testable replacement for A1 |
| Finite total record budget (PREP) | Under A1, Σ_k(1 − h₂(ε_k)) ≤ D₀ ≤ log₂\|S\| (PREP Node 4, consequence 1). Without A1, the local form 2.6 under H-ν keeps the per-cone bound and locates the budget in the incoming boundary data | A cap on simultaneously held, jointly balanced, ε-predictable records; the global cap log₂\|S\| is far beyond any measurable count. A falsifier listed by PREP Node 4: "a local supply shown to require a boundary elsewhere (an incoming stream as in 1.5(d), which needs A1 to fail)" | Preserves none of R1–R5 by itself. PREP 1.5(d) states only that the inflow law is singular to the product-uniform law, so its global budget relative to that law is infinite; the inflow law is itself shift-invariant. A budget condition therefore discriminates only relative to a reference law fixed in advance (§5), which is R1's residue |
| Local finiteness only (F1 + finite read sets; ledger (xiii) clauses; A4 without its finite lattice) | M17, C3, C5, C13; per-window D(K); GLUE's local reversible carrier; NR-1's infinite-lattice analyses; P7B with H2 | Finite propagation speed (tested); local discreteness ε (not tested; M:706) | Carries no recurrence, measure selection or typicality (GLUE countercontrol; NR-1 nonnilpotent class has diagonals ≤ 1/2, RIGID scope bullet 4). The most observable candidate, and the one that leaves R1, R2 and R5 open |

## 5. Inflow obligation

Without A1, PREP 1.5(d) admits an invariant probability on an infinite carrier that supplies
readiness at a constant rate through an incoming low-entropy stream (the shift on {0,1}^ℤ with
Bern(1 − δ)^⊗ℤ), with the supply located at spatial infinity; PREP 1.6 lists it among the surviving
regress endpoints only "without A1". Dropping A1 therefore creates obligation **O-INFLOW** for the
measurement-source programme (#866 under #1169): the native-source contract must either exclude
the incoming-stream endpoint by a stated condition, or admit it as a declared boundary law at
spatial infinity, typed and justified under the same contract as any other boundary law and
judged under §A.29. PREP 1.5(d) states that the inflow law is singular to the product-uniform
law; it is itself shift-invariant, so a budget condition D(p₀‖ν) < ∞ excludes it only when the
reference ν is fixed in advance (for example the product-uniform law) and not chosen to fit. Fixing
that reference is the selection problem of R1, so an exclusion by budget inherits R1's residue.
This record does not investigate O-INFLOW.

## 6. Controls

| Control | Check | Result |
|---|---|---|
| S ⇔ D ⇔ Q_fb | No row reclassifies M:550–556. The equivalence takes a finite visible law on a finite horizon and constructs finite witnesses (`Equivalence.finite_horizon_equivalence`:462, Lean; ROOTS R1; CENSUS §27.8 M550–556 row: A about physical A1) | Untouched |
| C4r route | M6 is (a); M4, M5 and M8 feed into `CausalReadback.c4r_implies_pIndivisible`, whose hypotheses take no hidden cardinality | Untouched |
| Finite-carrier theorems | Every (c) row concerns the physical reading or an A1-free extension; no row asserts that a finite-representative theorem is false. M10 records that the all-time classification is a theorem about finite realizations | Untouched |
| Observer-relative finiteness reading | Lemma 1 and the Definition (M:42–46; M:60 "only finite visible resolution is a theorem") enter no row as a consumer of A1; H-F3 restates them | Untouched |

## 7. Coverage statement

**Traced.** The sixteen sources in the table above at the pin (REC-1 at :60–72, Props 3.4,
5.1, 6.1, 6.2 and the verdict table :543–552; RM at :45–49), with RIGID's Lean statements read
(`ObservableRigidity.lean`, declarations at :88, :280, :342, :358, :388 and the matrix controls;
the module is imported by `OIBridge.lean`:29 and listed in `verification/lean-manuscript-census.json`:1718;
not built here). Main: M:42–64, M:80–97, M:109–181, M:206–222, M:262–336, M:362, M:414–416,
M:457–475, M:508–550, M:606, M:640–650, M:700–766. Companions: GR:58, :88, :112–138, :239–282,
:673, :871–905; Sub:44, :56, :92–104, :121–131, :187–195, :247–272; SM:210; Str:646, :718;
Comp:182. `SubstratumInterfaceAudit.A4` (:98) was read. The Lean declarations named in rows M4–M9, M12, C6 were checked for existence and
signature at the pin.

**Not traced.** The book chapters, `FULL.md` and all `.tex`/PDF mirrors; FCLASS U1 (Page curve,
black holes, cosmology) and U2 (biology, medicine, resources); Complexity, Methodology,
Introduction, Medicine, Bioinformatics, Juno beyond CENSUS §18's rows; SM beyond SM:210 and
CENSUS §17's SM rows (including SM:641's finite normalizer and SM:1376–1388); Main's remaining
kernel citations outside CENSUS §27 and ROOTS; the census's X items; OA-3 and the other
reconstruction records citing μ-O. No proof was rerun, no Lean build or probe was executed. A1-C01
remains incomplete; this record is not an exhaustive census and does not certify the absence of
other A1 consumers.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1055 comment 7022346035 | Authorization and scope | Provenance; quoted above with author and time |
| #1055, #1334, #1169, #866 | Accountability; the obligation named in §5 | Provenance |
| #1399, #1400, #1402, #1404, #1408, #1412, #1413, #1415, #1417, #1418, #1419, #1333 | The landings in scope | Provenance; every result used is cited from its file on `main` at the pin |
| #1394, #1396 (RIGID); #1347 (GR orientation correction) | Review and preservation history named inside cited records | Provenance |

## 9. What an independent reviewer must check

1. Each (c) row's cited step, and that no A1-free proof on `main` covers it (in particular M1,
   M2, M7 (ii), M9, M19, C4, C6).
2. Each (b) row's hypothesis against its source: F11, (RIG) and RIGID's compactness with the
   invariant product law (M4, M5, M7 (i), M8; REC-1 Prop. 6.2), A1-05's P8-M inputs and the
   operator-step scope (M18, M20), P7B's H1–H14 and the decoupled scope (C1), GR Appendix B's
   (D1)–(D5) (C3, M21), and the invariance argument for M3's corner.
3. The A4 finding (R4): that Sub:98 with finite site alphabets re-implies A1, and that the
   kernel predicate `SubstratumInterfaceAudit.A4` has no finiteness clause.
4. The relabelling test of §3, and that the C4r alternative is scoped to a root-independent
   preparation, statistical support and the observed family.
5. That the named lemmas L1, L2, L4, L6–L10 and obligations O-A4, O-INFLOW are absent from the traced
   corpus, and that no row was resolved by a derivation made here.
