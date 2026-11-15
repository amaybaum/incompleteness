# Unified derivation ledger, r3: levels A, B and C, and dependency map

**UNREVIEWED.** r3 applies the independent review of r2 (verdict ACCEPT WITH CHANGES) and the
owner's expansion of the ledger. The disposition of each finding is in `RESPONSE-r2.md`. r2 and
its review are preserved unchanged on draft PR #1292 at `7971631f`. r3 itself has not been
reviewed. A complete ledger is not a complete theory: an entry records the evidential status of a
claim, and inclusion implies no derivation.

**Authorizations, quoted verbatim.**
- Part 4 and the ledger: #914 comment 6877420015 (`amaybaum`, 2026-11-14T12:42:16Z), "Yes I approve,
  proceed as suggested".
- The expansion: #914 comment 6877871344 (`amaybaum`, 2026-11-14T13:19:06Z), "Yes, this is my
  decision, proceed as planned". Its conditions include: "Level A represents core theoretical
  obligations, not necessarily completed derivations. Level B covers all substantive derivation
  claims in the manuscript, whether established or not. Level C covers predictions, phenomenology
  and scope limits."; "Every entry must distinguish derivation from a common model, conditional
  derivation, empirical fitting, proposed explanation, and unresolved obligation. Negative results
  and explicit failures must also be recorded."; "Do not assume that the Standard Model branch is
  the common model. This remains an open scientific decision."; "Add explicit entries for the arrow
  of time, measurement problem and quantum–classical boundary, together with the specified Standard
  Model subquestions. Do not create a fifth part."; "a complete ledger is not a complete theory".
  It "does not adopt any scientific claim, settle any open premise, alter Issue priorities or
  statuses, or authorize new physical derivations."
- The QCD group: #914 comment 6877908458 (`amaybaum`, 2026-11-14T13:22:18Z), "Yes, I approve adding
  the QCD group to r3".

Paper-only record under these authorizations, serving the target recorded in #914 comments
6875046763, 6875548603 and 6877420015 and #1169 comment 6876591512. Reading, analysis and writing
only. The coverage audit of condition 6 is a separate later task; this record does not perform it. This record adopts no premise,
extension E or sector condition C, changes no scientific status, and proposes no tier, readiness,
authorization or status change. Statuses below are those the cited sources give; where this record
says "conflicting", "consistent" or "undetermined", the reason and the source are stated. Issue
numbers name planning records (AGENTS.md §A.45 rule 1); naming or assigning an Issue discharges no
scientific obligation.

**Base.** All `papers/`, `book/` and `verification/` content was read at `c3b5f37a`; current `main`
(`dfeec843`, unchanged when r3 was written) differs from it only in `AGENTS.md` (§A.46: the opening
paragraph, items 2 and 4, the new item 8 and the adoption line), so every line reference below
holds at `dfeec843`. Line numbers are physical lines; `papers/*.md` paragraphs are single long
lines.

**Vocabulary.** "Kernel" = Lean module on `main` under `verification/lean-mathlib/OIBridge/` (not
rebuilt here; no `sorry` or `axiom` declaration found by grep). "Kernel-only" = a census family in
`verification/lean-manuscript-census.json` that no manuscript carries. "Exhaustive" = exhaustive
finite computation in a script on `main` (not run here). "Paper" = derivation on paper. "Research
record (paper-level)" = a record under `verification/programmes/` whose own status note classes its
findings as paper-level and not adopted; under §A.46 items 1 and 7 none is an established claim or
usable as an established premise, and each is cited here at the scope its status note states.
"Numerical", "conditional", "posited", "open", "refuted" as in the Code Review Rules. Part 4
classes: **CR** = conditional reconstruction; **UD** = unified physical derivation (Part 4, #914
comment 6877420015). "Inferred" marks an entry this ledger derives and no source states.

**Evidence classes (condition 3 of #914 comment 6877871344).** Every registry entry carries one:
- **DM**, derivation from a common model. No common model is adopted (condition 4; Q13), and r3
  does not treat the SM branch's lattice model as the common model. DM is therefore used only for
  a result that holds for every model of the bare finite class (finite S, bijection φ, partition V,
  `papers/Main.md`:42 and ledger items (ii)–(iii) at :724), so that it holds in whichever common
  model is later fixed. DM marks the scope of the result; the bare-class inputs remain posited (§1).
- **CD[…]**, conditional derivation. The brackets name the hypotheses, each with its status at
  source.
- **EF**, empirical fitting: a value fixed by matching data, or a selection made by observation.
- **PE**, proposed explanation: stated at source as a proposal, mechanism proposal, reframing,
  candidate or conjecture.
- **UO**, unresolved obligation: no derivation at source.

A **NEG** flag marks a negative result or explicit failure: refutation, no-go, failed route,
retraction. **Support** gives the strongest layer at source: K (kernel), XA (exact algebra), EX
(exhaustive finite computation), P (paper), N (numerical), RR (paper-level research record, not
established, §A.46 items 1 and 7) or BK (book prose only). **XC** marks a reproduction of a known
calculation, which is a cross-check and not a derivation from OI (#914 comment 6877908458).

**Identifiers.** Entries are identified as A-*, B-<branch>-n and C-n. An identifier is not an
ordinal: it is not renumbered and is not reused. The B list records the derivation claims this
record found. The coverage audit will check it against every substantive claim in Main,
Substratum, SM, GR and Structure, using book chapters 18–19 as controls, and it may add entries.

## L. Registry

### L.A Level A: core theoretical obligations

These are obligations, not completed derivations. Each is UO as a whole; the cross-referenced
entries are the existing partial results.

| ID | Obligation | Class | What exists (cross-reference) | Source |
|---|---|---|---|---|
| A-QM | Inclusion QM ⊆ OI + E on one common realization, and the sector equivalence for a physically justified C, with its coverage and soundness directions | UO | Finite-law equivalence, the completion characterization, the extension characterizations and the obstructions: B-QM-1 to B-QM-16; branch detail §2 | #914 comments 6875046763, 6875548603; #1169 comment 6876591512 (answers 1–4) |
| A-BELL | Full quantum Bell-set soundness over the agreed two-wing interface inside C (BELL-QSET), H-Bell, and Tsirelson selection | UO | B-BELL-1 to B-BELL-8; §3. The finite construction realizes PR laws, so Tsirelson is not selected (`papers/Main.md`:360) | #914 comment 6875046763, decision 3; #1060 questions 1–3 |
| A-GR | GR ⊆ OI on the same substratum and observer | UO | B-GR-1 to B-GR-9; §4. The Einstein equations are imported, not derived (`papers/GR.md`:162) | #914 comment 6875548603 |
| A-REAL | One common physical realization satisfying the necessary premises jointly (Part 4 and joint satisfiability) | UO | §9 (joint-satisfiability table and the conflicts beneath it); §10 (shared missing mechanisms); Q13 (no common model fixed) | #914 comment 6877420015, items 1 and 4 |

### L.B Level B: derivation claims in the manuscripts

**B-QM (operational QM; detail §2).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-QM-1 | S ⟺ D ⟺ Q_fb on every finite horizon; universal, so representability does not single out the memory-bearing sector | DM | K | `papers/Main.md`:14–18, 97 |
| B-QM-2 | C4 ⟺ positive conditional memory; readout-relevant hidden memory in every faithful completion | DM | K in part (CMI criterion and one reading step not formalized) | `papers/Main.md`:97 |
| B-QM-3 | Available families are exactly the Kraus instruments iff completion conditions (i)–(v) | CD[finite carrier; complex matrix kinematics taken as given, derivation open] | K | `papers/GR.md`:212–216; `papers/Main.md`:562 |
| B-QM-4 | Under the stated substratum interventions, (iv) is not supplied | DM, NEG | K (two-state carrier) | `papers/Main.md`:80, 588 |
| B-QM-5 | Substratum plus one continuously tunable state-mixing operation gives operational QM, and conversely | CD[added operation, posited as an "empirical controllability resource"] | K | `papers/Main.md`:588; `papers/GR.md`:256 |
| B-QM-6 | OI⁺ ⟺ exact finite endomorphic operational QM, each added principle independent | CD[OI⁺ principles, posited] | K | `papers/Main.md`:584–588 |
| B-QM-7 | One finite reversible realization reproduces a bounded quantum envelope to accuracy ε | DM | P, with probe checks | `papers/Main.md`:596–598 |
| B-QM-8 | No fixed finite realization is exactly operationally equivalent to a qubit's full theory | DM, NEG (under the factorization interface) | P for the factorization half; unboundedness imported from [55] | `papers/Main.md`:558 |
| B-QM-9 | The quasilocal completion is unique given its stages and dynamics; no state or representation is selected | CD[stages and dynamics given]; a uniqueness, not an equivalence (§A.34) | K | `papers/Main.md`:588 |
| B-QM-10 | Representability plus coherence does not select the relating unitary evolution | DM, NEG | P | `papers/Main.md`:20 |
| B-QM-11 | The Born exponent is not selected by the equivalence | UO (frontier item) | P | `papers/Main.md`:18, 554 |
| B-QM-12 | Every operation the present interface sources preserves nonnegative entries | DM, NEG | K (kernel-only) | `verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84 |
| B-QM-13 | Affine-class and G_SM prepare–measure fragments are simplex-embeddable under named observer hypotheses; finite reversible emergent group | CD[(H1), H-AR, (H3), (H4), (SP), (xiv); for G_SM Theorem S's conditions], NEG within those hypotheses | RR | OA-1, OA-2, OA-3 status notes (§2.1) |
| B-QM-14 | The first state/readout bridge of candidate E-AR fails on any one fixed finite-dimensional quantum carrier | CD[E-AR], NEG (candidate-scoped) | P (hand proof) | `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md`:11–19 |
| B-QM-15 | Kernel-only reductions: necessary coherent continuum; real pair flow supplies the datum; fixed gate gives dense, not exact, QM | CD[stated datum, flow or gate as input] | K (kernel-only) | census families (§2.4) |
| B-QM-16 | On one fixed finite reversible representative the rooted visible process is indivisible somewhere in its recurrence cycle whenever some rooted map is not a permutation | DM given A1 | P | `papers/Main.md`:18 |

**B-BELL (detail §3).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-BELL-1 | Unrestricted OI realizes arbitrary finite stochastic laws, PR-box laws included | DM; NEG for Tsirelson selection | P, with a negative control | `papers/Main.md`:360, 427 |
| B-BELL-2 | Influence advances one edge of the coupling graph per update | CD[(viii) site factorization] | P; an algebraic cone in K | `papers/Main.md`:362 |
| B-BELL-3 | CHSH ≤ 2 for a screened local completion | CD[(viii), (xiv), the screening conditions] | P; EX for the 16-table bound | `papers/Main.md`:364–389 |
| B-BELL-4 | The reference nearest-neighbour graph alone cannot supply parameter dependence for wings outside the graph cone | CD[global A5, (viii), (x), (xiv), the Corollary's conditions], NEG | P | `papers/Main.md`:414 |
| B-BELL-5 | A linear update has the same dependence graph at every state class, so preparation-indexed adjacency lies outside (vii) | DM, NEG for that route under A5 | XA | `papers/Main.md`:362, 414 |
| B-BELL-6 | Measurement-dependent bound CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}; recorded, not adopted | CD[measurement dependence] | P | `papers/Main.md`:416–423 |
| B-BELL-7 | H-Bell (i)–(iii) | UO | — | `papers/Substratum.md`:131–133 |
| B-BELL-8 | A Bell-inclusive completion exists only conditional on H-Bell (Theorem 23) | CD[H-Bell; Theorem 23's hypotheses, A5 included] | P | `papers/Substratum.md`:193 |

**B-GR (detail §4).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-GR-1 | Horizon count S = σA/ε², stated as unconditional | CD[the horizon partition, which takes GR's causal structure as given] | P | `papers/GR.md`:12, 24, 28, 40 |
| B-GR-2 | ħ = c³ε²/(4Gσ), ε = 2√σ l_p, S = A/(4l_p²); fixes only ε/√σ | CD[H-slope, H-count (W1 the load-bearing part), horizon and frame conditions, local boost structure, symmetric rate ratio] | P | `papers/GR.md`:12, 24, 28, 306, 547 |
| B-GR-3 | The Einstein equations | UO (imported through Jacobson's relation, not derived) | — | `papers/GR.md`:162; `book/ch07-gravity.md`:44 |
| B-GR-4 | Discrete Einstein equation κ_OR = α𝒯 | UO (target form); NEG for the hop-metric Ollivier route on the reference graph | P | `papers/SM.md`:144–150; `papers/Substratum.md`:171 |
| B-GR-5 | Newtonian limit and Poisson equation at fixed G | CD[energy shell assumed; N_dof = A/l_p² adopted] | P (consistency) | `papers/GR.md`:689–697 |
| B-GR-6 | Covariant field equation and stress-energy coupling (G3); matter-coupling completion selection | UO | — | `papers/GR.md`:12, 350, 352 |
| B-GR-7 | W1 is an additional assumption; no tested mechanism derives it; the gap route C6(a) fails in the real lift of the linear rule | NEG | RR | `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48–62 |
| B-GR-8 | Lattice Bisognano–Wichmann form | UO (open hypothesis) | — | `papers/SM.md`:140–142 |
| B-GR-9 | Nested trace-outs are quantum-classically consistent (Theorems A.1–A.4) | CD[the nested-partition setting of GR Appendix A] | P | `papers/GR.md`:601, 739 |

**B-SM (detail §5).** General entries, then the owner's subquestions as groups.

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-1 | Six signed links decompose as T₁(3) ⊕ E(2) ⊕ A₁(1) (Theorem 7) | CD[cubic lattice, ledger (x)] | K | `papers/SM.md`:374 |
| B-SM-2 | Identification of the link space with the physical carrier | CD[H-link single-copy, H-cust, H-blind; open] | — | `papers/SM.md`:12, 26, 32, 374 |
| B-SM-3 | Gauge group from the bicommutant; reduction to SU(3)×SU(2)×U(1) | CD[specified charged matter action; anomaly cancellation] | P | `papers/Substratum.md`:163 |
| B-SM-4 | Simple cubic is the one Bravais lattice compatible with the observed gauge group (Theorem 7b) | EF (selection by the observed group; "the same fact stated in two directions") | P | `papers/SM.md`:390, 1424 |
| B-SM-5 | d = 3 | EF (filters E5–E7, self-consistency strength; E7 inherits H-count) | P | `papers/SM.md`:30, 1424 |
| B-SM-6 | 1 ⊕ 3 tastes (Theorem 8); three generations | K for the decomposition; CD[H-spin′] for generations; NEG for the free-kernel and 4D-staggered routes | K; N | `papers/SM.md`:543, 1320 |
| B-SM-7 | Weak chirality | UO (H-χ′ open); NEG: the minimal embedding is vector-like | N (certified) | `papers/SM.md`:543, 1320 |
| B-SM-8 | Hypercharges unique given family pattern and chirality, apart from Y_Q = 0 (Theorem 15) | CD[family pattern, chirality] | XA | `papers/SM.md`:589 |
| B-SM-9 | The observer-level map φ → L_obs → Δ_g | UO ("not proved anywhere in this framework") | — | `papers/SM.md`:232 |
| B-SM-10 | Exact chiral symmetry ⟺ vanishing onsite terms (Theorem 3) | CD[the stated opposite-parity hopping family; the bridge to center dependence is separate] | K (both directions) | `papers/SM.md`:302–308 |
| B-SM-11 | [g] = (3 − d)/2, dimensionless iff d = 3 (Theorem 16) | CD[the Yang–Mills action form] | K | `papers/SM.md`:603–607 |
| B-SM-12 | The Higgs is the unique renormalizable unitarity-preserving mass mechanism; H = (1, 2, +½) | CD[chiral symmetry and the center-independent gauge sector] | P (standard QFT argument) | `papers/SM.md`:611 |

*SM-CP, strong CP.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-CP-1 | T-invariance of the wave equation; θ ∈ {0, π}; reciprocity of visible transition counts at every time scale (Theorems 17–19) | CD[T-invariant substratum update] | P | `papers/SM.md`:667 |
| B-SM-CP-2 | Reciprocity does not make the emergent Hamiltonian T-invariant; θ̄ is not fixed (Proposition 20, Theorem 21) | NEG | P | `papers/SM.md`:667; `book/ch19-open-problems.md`:80 |
| B-SM-CP-3 | H-top (θ = 0 over π) and H-det (arg det(Y_uY_d) = 0); neutron EDM | UO | — | `papers/SM.md`:669 |

The reported Jarlskog computation at `papers/SM.md`:671 is stated there as not available for
verification, and is not entered.

*SM-HIER, the Higgs hierarchy.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-HIER-1 | Cutoff insensitivity of m_H by singlet-taste chiral protection | PE ("structurally identified"; "the theorem-level derivation is deferred") | P (outline) | `papers/SM.md`:613, 1570 |
| B-SM-HIER-2 | The origin of v ≪ f | UO | — | `papers/SM.md`:613; `book/ch19-open-problems.md`:88 |
| B-SM-HIER-3 | λ(M_Pl) = 0 on the composite-Higgs branch | CD[composite Higgs, A₁ taste] | P, with 3-loop RGE (XC) | `papers/SM.md`:1116–1118 |

*SM-FLAV, flavour and masses.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-FLAV-1 | Structural form of the flavour pattern: Cabibbo λ from Brillouin geometry, Wolfenstein hierarchy, Koide target A² = C₂(T₁) | CD (Layer 1, one named open link each, at source) | P | `book/ch19-open-problems.md`:154–156, 162; `papers/SM.md` §7.1–§7.2 |
| B-SM-FLAV-2 | Koide amplitude from non-perturbative dynamics (perturbative taste-breaking gives A² ≈ 0.34 against 2) | UO; NEG for the perturbative route | N | `book/ch19-open-problems.md`:154 |
| B-SM-FLAV-3 | m_b/m_τ = 4.28/Z_S(λg₀²) | CD[measure identification, open, `papers/SM.md`:809]; Layer 2(a) verification residual | N (Monte Carlo with the standard Haar measure, `papers/SM.md`:813) | `papers/SM.md` §7.5; `book/appendix-a-prediction-status.md`:85 |
| B-SM-FLAV-4 | m_s, m_c, CP phases | UO (m_s, m_c); EF (CP phases, solution-specific inputs) | — | `papers/SM.md`:1322; `papers/Substratum.md`:415 |
| B-SM-FLAV-5 | The 22 tabulated observables (2 S, 5 C, the rest L/M/R/P/E) | per row at source | per row | `papers/SM.md`:1269–1316; C-PRED-1 |

*SM-NU, neutrinos.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-NU-1 | Majorana neutrinos and large PMNS mixing (from representation theory) | CD[the branch where the singlet taste hosts the Higgs (Theorem 11 taken as input) and no gauge-singlet fermion is present; the mechanism otherwise open] | P | `papers/SM.md`:1452–1462 |
| B-SM-NU-2 | Normal ordering and a hierarchical spectrum | PE (genericity heuristics, on the same branch) | P | `papers/SM.md`:1456–1464; `book/ch19-open-problems.md`:158 |
| B-SM-NU-3 | Absolute scale, Δm² ratio, δ_CP | EF (solution-specific) | — | `papers/SM.md`:1468 |

*SM-BARY, baryogenesis.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-BARY-1 | Baryon number is exactly conserved by the substratum dynamics | CD[bilinear coupling structure of the lattice wave equation] | P | `papers/SM.md`:1486–1490 |
| B-SM-BARY-2 | η_B | Not derived; treated at source as solution-specific, inheriting the flavour-CP input (EF-type) | — | `book/ch19-open-problems.md`:178, 184–188 |
| B-SM-BARY-3 | Weinberg-operator leptogenesis gives η_B ~ 4×10⁻¹¹, about 15× below observation | NEG | P | `book/ch19-open-problems.md`:180 |
| B-SM-BARY-4 | Substratum-level instanton-like B-violation | NEG (retracted: the substratum has no Euclidean action) | P | `book/ch19-open-problems.md`:182 |

*SM-GAUGE, gauge dynamics and confinement.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-GAUGE-1 | Induced coupling 1/α₀ = 23.25 | CD[single-copy H-link (N_f = 6), T(R) = ½]; for hypercharge also H-observer-bundle, H-Y-vertex | P (one-loop computation) | `papers/SM.md`:793 |
| B-SM-GAUGE-2 | Couplings at M_Z | EF (δ₀ fitted to the U(1) row; A, B matched to SU(2), SU(3)); A·B inconclusive; non-unification structural | P; N | `papers/SM.md`:797, 817 |
| B-SM-GAUGE-3 | The Haar-measure induced theory confines, against the deconfined phase the matching needs | NEG | N | `papers/SM.md`:801 |
| B-SM-GAUGE-4 | The framework's gauge measure is a near-identity pushforward | PE (stated as a conjecture about the correct map); NEG: the natural polar candidate gives a Haar pushforward | N | `papers/SM.md`:803, 809, 811 |
| B-SM-GAUGE-5 | Local gauge dynamics and action selection (same-update source, measure, observables, action) | UO | — | No fundamental gauge action (`papers/SM.md`:827); the frozen roadmap names "a rigorous derivation or classification of local gauge dynamics" as the first milestone of a "conditional future programme" (`verification/ROADMAP.md`:1525–1536); planning record #1063 |

*SM-NP, nonperturbative effects.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-NP-1 | Z_S, the matching scale and the chiral condensate from dynamical-fermion Monte Carlo | XC (standard Haar measure); agreement with the framework's induced measure open | N | `papers/SM.md`:813, 1144 |
| B-SM-NP-2 | Archived code for §6.5 and §7.5 no longer extant; archived values not reproduced; Z_S universality violated (+2.6% ± 0.15%) for the directly sampled measure at the archived point | NEG | N | `papers/SM.md`:805 |
| B-SM-NP-3 | Non-perturbative B + L violation through emergent sphaleron physics, with no substratum channel | PE (stated as "the correct picture") | BK | `book/ch19-open-problems.md`:182 |

**B-QCD (QCD group; Level B, within the SM branch).** Eleven coverage obligations (#914 comment
6877908458). Pure Yang–Mills (B-QCD-6) is kept distinct from full QCD with dynamical quarks
(B-QCD-5, B-QCD-8). Gauge dynamics, action selection and the mass gap are linked to #1063; closed
PR #1003 is provenance only.

| ID | Obligation | Class | Support | Source / cross-reference |
|---|---|---|---|---|
| B-QCD-1 | Colour gauge symmetry | CD[H-link, H-cust; the cubic-lattice commitment] | K (decomposition) | B-SM-1 to B-SM-4 |
| B-QCD-2 | Quarks and gluons | CD[matter on links; H-link]: gluons as the SU(3) adjoint in End(V₃) = 8 ⊕ 1; Q_L ∈ (3, 2) in V₃ ⊗ V₂ on links | P | `papers/SM.md`:489, 523–525; spin under H-spin′ (B-SM-6) |
| B-QCD-3 | Quantum Yang–Mills theory | UO. No fundamental gauge action: couplings induced from the fermion determinant (CD, `papers/SM.md`:827); action selection open | P (induced structure) | B-SM-GAUGE-1, B-SM-GAUGE-5, B-SM-11; #1063 |
| B-QCD-4 | Running coupling and asymptotic freedom | XC (the SM running assumes the stated SM field content and standard beta functions); asymptotic freedom "does not follow from dimensionless coupling" | P | `papers/SM.md`:34, 607 |
| B-QCD-5 | Confinement (full QCD) | UO; NEG for the Haar-measure induced theory against the matching (B-SM-GAUGE-3) | N | `papers/SM.md`:801–811; D8 |
| B-QCD-6 | Mass gap (pure Yang–Mills) | UO. The sources state that the rigorous mass-gap proof is "not required by the OI framework" and "does not affect any prediction" | — | `papers/Substratum.md`:225; `papers/SM.md`:1448; #1063 |
| B-QCD-7 | Chiral symmetry breaking | XC (staggered Monte Carlo with the standard Haar measure shows spontaneous breaking, Σ ≈ 0.20); relation to the framework's measure open | N | `papers/SM.md`:813, 1144 |
| B-QCD-8 | Hadron spectrum (full QCD) | UO; no manuscript derivation found | — | searched `papers/` for "hadron", "pion", "proton mass": only `papers/GR.md`:581 (proton mass as QCD binding energy, in the CC argument) |
| B-QCD-9 | Strong CP | see B-SM-CP-1 to B-SM-CP-3 | — | cross-reference |
| B-QCD-10 | Nonperturbative QCD | see B-SM-NP-1 to B-SM-NP-3 and B-SM-FLAV-3 | — | cross-reference |
| B-QCD-11 | Nuclear consequences | PE at the book source ("mechanism structural", parameters solution-specific); UO in the papers | BK | `book/ch10-chemistry.md`:86–88; D8 |

**B-CC (detail §6).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-CC-1 | Descriptive distinction: the zero-point sum belongs to the emergent description | CD[geometry-first ordering, `papers/GR.md`:340–348] | P | `papers/GR.md`:352 |
| B-CC-2 | Dynamical decoupling of the uniform offset | CD[G3, open] | P | `papers/GR.md`:352, 577 |
| B-CC-3 | The value of Λ | EF (an input set by initial conditions) | — | `papers/GR.md`:356 |
| B-CC-4 | Higgs and QCD vacuum shifts are absolute properties of the emergent ground state; same dissolution | CD[geometry-first proposal; open coupling step] | P | `papers/GR.md`:569–579; C-QCDVAC |

**B-COS (detail §7).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-COS-1 | Type II running-vacuum channel | PE ("a structural reading, not a derived law"; the form is not distinctive) | P | `papers/GR.md`:374–380 |
| B-COS-2 | \|ν\| ≈ \|ν_QFT\| ~ 10⁻³² | CD[the §7.3 split; emergent running] | P | `papers/GR.md`:382–398 |
| B-COS-3 | ~95% dark budget | CD (partly definitional, 1 − Ω_B by construction) | P | `papers/GR.md`:418–452 |
| B-COS-4 | a₀ = cH/6; BTFR | CD[H-count, H-slope, H-frame, H-Hawking]; the 1/6 factor imported | P | `papers/GR.md`:466–486 |
| B-COS-5 | MOND-like core to CDM-like growth crossover; relaxation kernel | UO | — | `papers/GR.md`:524 |

**B-BH (detail §8).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-BH-1 | Information conserved | DM given A2 (by premise) | — | `book/ch19-open-problems.md`:72 |
| B-BH-2 | Bijectivity does not imply recovery from accessible records; complete endpoint access with bijectivity suffices | DM, NEG | RR (exhaustive, exploratory, internally reviewed) | `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md` |
| B-BH-3 | H-scramble fails for every bijection on definite configurations at aligned bipartitions; Theorems A.8–A.9 as stated have no instance there | DM, NEG | P; EX (BH-02 C1, C6(a)) | `papers/GR.md`:805, 813–823 |
| B-BH-4 | S(ρ_R(t)) ≤ H(p₀) at aligned cuts, for every bijection | DM | P; EX in part (BH-02 C2) | `papers/GR.md`:823–827 |
| B-BH-5 | Page curve outside the counted setting; GSL | UO | — | `papers/GR.md`:603, 815, 827–829, 839; `book/appendix-a-prediction-status.md`:111 |
| B-BH-6 | Page time 0.646 t_evap | CD[β = 1, half-entropy turnover, constant emission coefficient] | P | `papers/GR.md`:605 |
| B-BH-7 | Island ↔ cycle correspondence | PE (conjectural) | — | `papers/GR.md`:861 |

**B-P4 (named Part 4 entries).**

*P4-AOT, the arrow of time.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-P4-AOT-1 | The substratum has no arrow of time (φ and φ⁻¹ equally valid) | DM | P | `papers/Substratum.md`:56, 409 |
| B-P4-AOT-2 | Observers satisfying C2 in its timescale form are confined to the non-equilibrium phase (structural observer selection) | CD[(EM); τ_mix ≪ τ_S; the iterated one-step-channel description; bounded diameter of V] | P | `papers/Main.md`:742–758; `papers/Substratum.md`:401 |
| B-P4-AOT-3 | The horizon area is non-decreasing on the expanding branch | CD[expanding branch (observed, an input); null energy condition (assumed)]; "not a prediction derived from the substratum" | P (standard GR kinematics) | `papers/Substratum.md`:405 |
| B-P4-AOT-4 | The direction of coarse-grained entropy increase; alignment of the thermodynamic, memory and measurement arrows | UO for alignment ("not established"); the direction rests on a low-entropy or product boundary condition (EF-type input) | P | `papers/Substratum.md`:56, 407, 409 |
| B-P4-AOT-5 | Ordering of moments | UO (the section's results inherit its open status) | — | `papers/Substratum.md`:413 |
| B-P4-AOT-6 | The arrow as observer-emergent, through the trace-out of a non-equilibrium initial condition | PE ("reframes rather than explains") | BK | `book/ch18-beyond.md`:202, 218–222 |

*P4-MEAS, the measurement problem.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-P4-MEAS-1 | Observer-relative account at the fixed-basis level: measurement conditions on a visible outcome and re-marginalizes the hidden sector | PE (interpretive account) over B-QM-1 | P | `papers/Substratum.md`:463; `book/ch19-open-problems.md`:64 |
| B-P4-MEAS-2 | Wigner's friend: the joint marginal law exists, is unique given φ, and reproduces both observers' laws | DM | P | `papers/Main.md`:686–692 |
| B-P4-MEAS-3 | Friend's reduced description is quantum-mechanical under C1–C4 | PE (stated as "the framework's proposal"); the established part is the fixed-basis representation | P | `papers/Main.md`:688 |
| B-P4-MEAS-4 | No branching: a fixed bijection has one trajectory from each state | DM given A2 | P | `papers/Substratum.md`:465 |
| B-P4-MEAS-5 | Derivation of the double-slit interference pattern from the dynamics; full operational protocols; Frauchiger–Renner premises | UO | — | `papers/Substratum.md`:463; `papers/Main.md`:682; `book/ch19-open-problems.md`:64 |

*P4-QCB, the quantum–classical boundary.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-P4-QCB-1 | The boundary is drawn in the memory currency by C1–C4; representability is universal | DM (from B-QM-1, B-QM-2) | K, P | `book/ch18-beyond.md`:64, 72; `papers/Main.md`:97 |
| B-P4-QCB-2 | Restricted quantum-statistical regime (partial distinguishability revival at marginal hidden capacity) | PE (mechanism proposal; conjecture on where it occurs) | BK | `book/ch18-beyond.md`:74–88 |
| B-P4-QCB-3 | Coherence as a bulk quantity and decoherence as an area quantity | PE ("an interpretation of the one-step result") | P | `papers/Main.md`:322 |
| B-P4-QCB-4 | Gravitational decoherence and gravitationally mediated entanglement | UO (selection among completions (a)–(c) open) | — | `papers/GR.md`:350 |

### L.C Level C: predictions, phenomenology and scope limits

| ID | Item | Class | Source |
|---|---|---|---|
| C-QCDVAC | QCD vacuum energy, condensates and gravitational coupling: absolute ground-state energies do not gravitate; QCD binding energy is relative and gravitates; how energy released in the electroweak and QCD transitions couples "requires the same open coupling step" | CD[geometry-first proposal of GR §6.2; G3] | `papers/GR.md`:579, 581; B-CC-4 |
| C-EARLY-1 | Inflation | UO ("Not addressed"; three possibilities, none developed: PE) | `book/ch19-open-problems.md`:194–202 |
| C-EARLY-2 | Transient Born-rule violations in primordial statistics (F7) | PE (conditional prospect; source dynamics, initial-deviation family and observable map not fixed) | `book/ch18-beyond.md`:36–52; `book/appendix-a-prediction-status.md`:180 |
| C-EARLY-3 | No GUT monopoles, so no monopole problem; no GUT-chain cosmic strings | CD[no GUT (Layer A, conditional on H-link, H-cust)] | `papers/SM.md`:823, 833–835 |
| C-EARLY-4 | Initial state of (S, φ): partially gauge, partially outside scope | PE (the existence question named irreducible) | `book/ch19-open-problems.md`:208–216 |
| C-EARLY-5 | The Hubble rate H | EF (initial-condition input) | `papers/GR.md`:356 |
| C-OBS | Observer selection and the anti-Boltzmann-brain corollary | CD[(EM); τ_mix ≪ τ_S; the uniform-erosion hypothesis of the erasure lemma] | `papers/Main.md`:742–758; B-P4-AOT-2 |
| C-HUBBLE | Hubble tension | NEG as a scope limit: "at the framework's predicted magnitude the effect is too small" (ΔH₀/H₀ ~ 0.4% even at ν ~ 2.5×10⁻³ against ~8%); "makes no specific claim" on its resolution | `book/ch19-open-problems.md`:168–172, 343 |
| C-TOPO | Cosmic topology | Scope limit: silent on global topology; compatible with, not predicting, compact topologies; the non-orientability–chirality question open (UO) | `book/ch18-beyond.md`:228–262 |
| C-CONJ-1 | Consciousness: observation as a necessary but not sufficient condition | PE ("offered as a conjecture"; Direction 1 a conjecture, not a theorem) | `book/ch18-beyond.md`:6, 268–274 |
| C-CONJ-2 | Biological candidates for the restricted regime (protein conformational dynamics, single-enzyme kinetics) | PE (conjecture) | `book/ch18-beyond.md`:80–88 |
| C-CONJ-3 | Condensed-matter relevance of the restricted regime | PE ("speculative and has not been developed") | `book/ch19-open-problems.md`:356 |
| C-CONJ-4 | Born rule as dynamical read-write equilibrium | PE (mechanism proposal; estimate heuristic) | `book/ch18-beyond.md`:34–36 |
| C-ANOM | Precision-sector anomalies (g − 2, R_K, m_W) | Scope limit: framework corrections O(10⁻³⁴) at 100 GeV, unobservable | `book/ch19-open-problems.md`:354 |
| C-PRED-1 | SM observables (appendix-a entries 1–23), neutrino entries N1–N7 | per row at source (S/C/L/M/R/P/E); JUNO sin²θ₁₂ a retrodiction now, a forward test at design-lifetime precision | `book/appendix-a-prediction-status.md`:70–92, 98, 127–133, 211 |
| C-PRED-2 | Higgs mass from λ(M_Pl) = 0: m_H ≈ 129–132 GeV for m_t = 172–173 GeV, against 125.10 GeV | CD (B-SM-HIER-3); the λ(M_Pl) value consistent at 0.6σ, the m_H value 4–7 GeV above the observed value | `papers/SM.md`:1116–1118; appendix-a:91 |
| C-PRED-3 | No GUT proton decay (τ_p ~ 10⁴⁵–10⁴⁶ yr); detection falsifies | CD[no GUT; Planck-suppressed dimension-6 operators] | `papers/SM.md`:831, 839 |
| C-PRED-4 | Gravitational entries G2–G13 | per row at source | `book/appendix-a-prediction-status.md`:106–113 |
| C-PRED-5 | DESI Y5: \|ν\| ≳ 10⁻³ refutes the magnitude; a high-confidence phantom crossing falsifies at structural level | test of B-COS-1, B-COS-2 | `papers/GR.md`:412, 591–593 |
| C-PRED-6 | Rotation curves: Milky Way decline and high-z curves in tension | NEG (stated tensions) | `papers/GR.md`:12, 536–545 |
| C-PRED-7 | GW250114 tests the area theorem, not the 1/4 coefficient; no echoes expected | scope limit | `papers/GR.md`:12, 318, 597 |
| C-PRED-8 | Cosmic recurrence: period at most g(\|S\|), \|S\| not fixed | logically falsifiable only | `book/appendix-a-prediction-status.md`:181 |
| C-PRED-9 | Memory-witness tests | none decisive at present ("no memory-witness outcome therefore falsifies the ontology at present") | `papers/Main.md`:718–722 |

The biological entries B1–B14 and F1–F9 of appendix-a (`book/appendix-a-prediction-status.md`:145–158,
170–187) fall under Level C, but this record has not classified them. Their classification
belongs to the coverage audit.

## 0. Branch table

Sections 0–12 give the branch detail that the registry entries summarize. They carry r2's text,
with REVIEW-r2's changes applied.

| Branch | Headline result at source | Status at source | Weakest link | First missing step | Part 4 class |
|---|---|---|---|---|---|
| QM (operational) | S ⟺ D ⟺ Q_fb at the finite observable-law level; exact finite operational QM iff completion conditions (i)–(v); bare finite OI ⇏ QM | Kernel (equivalence, characterization, non-implication); (iv) not supplied by the stated substratum interventions (kernel, on the two-state carrier) | Physical source of the added principles (posited as an "empirical controllability resource") | An independently justified operation, inside one model, that supplies continuously tunable state mixing and phases (condition (iv)) | CR |
| Bell | Screened local completion ⇒ CHSH ≤ 2; reference nearest-neighbour graph Bell-local; adopted branch: ontic parameter dependence with measurement independence | Paper proof + exhaustive 16-table check; H-Bell open | H-Bell (open hypothesis) | A preparation-indexed adjacency rule that gives quantum CHSH values with operational no-signalling | Open in the common model (H-Bell (i) is the required dependence); in the abstract class, response-table realizations of quantum and supraquantum laws exist |
| GR | Horizon calibration ħ = c³ε²/(4Gσ), S = A/(4l_p²), Newtonian weak field at fixed G | Paper, conditional (H-slope, H-count, horizon/frame conditions); Einstein equations imported via Jacobson, not derived | G3: covariant field equations and stress-energy coupling, open | A derivation of the covariant field equation from (S, φ) | CR (G1–G2 only) |
| Standard Model | Gauge group SU(3)×SU(2)×U(1), (3,2,1) multiplicities, 1⊕3 candidate sectors, hypercharges, 22 tabulated observables | Six-link decomposition kernel; physical carrier conditional on H-link, H-cust; generations on H-spin′; chirality open (H-χ′); simple cubic selected by the observed gauge group (Theorem 7b) and d = 3 by filters E5–E7, both empirically selected | H-χ′ (open); H-link with H-cust conditional | Derivations from the model of the observer-level map φ → L_obs, the physical carrier identification (H-link) and weak chirality (H-χ′) | CR given the cubic-lattice commitment, which the observed gauge group selects ("maximally tight compression" at source) |
| Cosmological constant | 10¹²² ratio read as S_dS; zero-point sum assigned to the emergent description | Descriptive distinction established (paper); dynamical decoupling conditional on G3; value of Λ an input | G3 coupling theorem | A coupling theorem showing the uniform emergent offset does not source curvature | CR |
| Cosmology (dark sector, expansion) | Type II running-vacuum reading, \|ν\| ~ 10⁻³²; ~95% dark budget; a₀ = cH/6; BTFR | Conditional (H-count, H-slope, H-frame, H-Hawking; G3); form not derived; budget partly definitional; factor 1/6 imported; two rotation-curve tensions | Matter-to-boundary coupling map (open, G3) | The H-dependence of the uniform/structured split of boundary entropy, and the relaxation kernel | CR |
| Black-hole information | Information conserved by bijectivity; cycle-averaged Page curve under H-scramble and H-decouple | Conservation by premise (A2). H-scramble fails for every bijection in the setting Theorems A.8–A.9 count: definite initial configurations, bipartition aligned with the configuration coordinates (paper proof; exact, BH-02 C1 and C6(a)); in that setting the theorems as stated have no instance. Outside it (initial superposition, non-aligned bipartition, proper shell) the Page curve is open (G11 open). GSL open | H-scramble | A preparation or partition that yields entanglement across the black-hole/radiation cut, and a scrambling statement attainable under it | Open (G11 open; no instance in the counted setting) |

## 1. Inputs the corpus states for the observation triple

The single object is the observation triple (S, φ, V) (`papers/Main.md`:42). The table lists the
inputs the corpus states, with status at source. It does not fix a common model (Q13). Items
(vii) and (ix)–(xiii), with the Stage-2 inputs, specify the lattice model the SM branch uses
(linear second-order update, bounded degree, nearest-neighbour simple-cubic reference graph;
`papers/SM.md`:60). They are listed as the corpus's
commitments; this record does not treat that model as the common model (#914 comment 6877871344,
condition 4).

| Input | Content | Status at source | Site |
|---|---|---|---|
| Axiom 1 | tokened differentiation occurs | indubitable floor | `papers/Main.md`:36 |
| Ledger (i) | Axiom 2, recurrence | posited (countermodel for non-derivability) | `papers/Main.md`:724 |
| Ledger (ii) / A1 | total finiteness of the bijective representative | posited; E3 bounds only C_V × C_B under H-BD | `papers/Main.md`:724; `papers/Substratum.md`:92 |
| Ledger (iii) / A2 | bijectivity | part-empirical (observed doubly stochastic statistics) plus eventual-image principle | `papers/Main.md`:724; `papers/Substratum.md`:94 |
| Ledger (iv) | maximal-entropy measure selection | posited | `papers/Main.md`:724 |
| Ledger (v) | hidden-sector mixing hypothesis (C2 slow-bath form) | open; motivated only numerically, by a rounded map outside A5 | `papers/Main.md`:724; `papers/Substratum.md`:135 |
| Ledger (vi) / E4 | spatial isotropy | empirical input | `papers/Main.md`:724 |
| Ledger (vii) / A5 | linearity of the update | posited; affine part necessary given amplitude-scale gauge invariance, itself assumed (its derivation from the q-size gauge freedom is an open step); the restriction to linear is imposed; no derivation from bare OI found on the record searched | `papers/Main.md`:724; `papers/Substratum.md`:100; `verification/programmes/hydrodynamics/round-h-d-a5-status-adjudication/result.md`:647–700 |
| Ledger (viii) | site factorization | posited (dynamics not shown to select it) | `papers/Main.md`:724 |
| Ledger (ix) / A3 | bounded coupling degree (family form) | posited | `papers/Main.md`:724 |
| Ledger (x) | nearest-neighbour range; simple-cubic reference graph | posited (beyond A3), scoped to the reference vacuum/uniform state class | `papers/Main.md`:724; `papers/SM.md`:226 |
| Ledger (xi) / A4 | center independence | posited; anchored to homogeneity of law | `papers/Substratum.md`:98 |
| Ledger (xii) / A6 | background independence (covariant link interface) | posited; restricts no rule | `papers/Substratum.md`:102 |
| Ledger (xiii) | second-order form x(t+1) = F(x(t)) − x(t−1) | posit of the selected lattice model (kernel `ruleDynamics`) | `papers/Main.md`:724 |
| Ledger (xiv) | measurement independence p(Ω∣a,b) = p(Ω) | posited on the initial condition | `papers/Main.md`:724, 404–410 |
| C1–C4 | coupling, persistence, capacity, readback | diagnostics of a realization; C4 not discharged at the cosmological cut | `papers/Main.md`:70–78; `papers/GR.md`:52 |
| E1–E7 | unitary QM, Bell violation, boundary entropy, isotropy, propagating gravity, stable matter, ρ_s/ρ_crit ≈ 1 | empirical inputs of the reverse reconstruction | `papers/Substratum.md`:76–88 |

Kernel coverage of A1–A6 (census family "manuscript axioms A1-A6"): no manuscript-level conjunct
is a faithful predicate of the bare theory; A1 and A2 have exact realized-core images and are
formalization gaps at the substratum level absent an identification map; A3–A6 are gaps with the
missing interface recorded.

No extension E and no sector condition C is adopted (#914 comments 6875046763, 6875548603,
6877420015; #1169 comment 6876591512). On `main`, the Gate A endpoint contract states the
E-indexed two-direction target for each nonempty finite carrier as "proposed obligations, not
proved statements" (`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`:51–69).
One candidate extension, E-AR, is stated clause by clause
(`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md`:21 onward). Its
first state/readout bridge fails: its preparations have no realization by density states and
preparation-independent effects on any one fixed finite-dimensional quantum carrier (:11–16). That
is a hand proof about one added-access extension, "not a no-go for bare OI, other
preparation/access principles, or finite-menu representations with growing dimension" (:17–19).
The collection's guide gives the content and limit of its eighteen records
(`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/README.md`:24–43). Other records under
`verification/programmes/oi-qm/reconstruction/` assess supplied inputs and further candidate
mechanisms (for example `apparatus-1-20261107/` and `mechanism-1-20261107/`); this ledger made no
inventory of every candidate stated there. No sector condition C in the target's sense and no
access-closure condition is stated on `main` (searched: `papers/`, `book/` and `verification/`, for
"sector condition", "condition C", "extension E" and "access closure"; the one hit for "sector
condition", `verification/audits/manuscript/representation-sector-audit.md`:23, concerns
superselection sectors). Access closure appears as an open item in the reports under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/` (for example
`EQUIVALENCE-OBLIGATIONS.md`:73, `branch_v10/REPORT.md`:84) and as a hypothesis of one conditional
composition theorem in a research draft
(`verification/programmes/oi-qm/reconstruction/composition-access-20261024/REPORT.md`:3–5, 34–39).
The reverse reconstruction (Theorem 23, `papers/Substratum.md`:193) takes observed QM (E1) and Bell
data (E2) as inputs; it is a uniqueness statement for the local lattice/gauge residue, not a
forward derivation.

## 2. QM (operational)

**2.1 Results and status.**
- S ⟺ D ⟺ Q_fb on every finite horizon (`papers/Main.md`:14–18, 97). Kernel: `finite_horizon_equivalence`, `S_imp_D`, `D_imp_Qfb`, `Qfb_imp_S` (`OIBridge/Equivalence.lean`). Universal over finite laws, so representability does not single out the memory-bearing sector (`papers/Main.md`:18).
- C4 ⟺ positive conditional memory; readout-relevant hidden memory in every faithful completion. Kernel for the pushforward identity; the CMI vanishing criterion and one reading step are stated as not formalized (`papers/Main.md`:97).
- Operational-completion characterization: on a finite carrier, with complex matrix kinematics taken as given, available families are exactly the Kraus instruments iff (i)–(v) (`papers/GR.md`:212–216; `papers/Main.md`:562). Kernel: `exactAll_iff_physical_general`, `five_way_minimality`, `oi_alone_not_qm`. The kinematics itself is not derived (`papers/GR.md`:212).
- Under the stated substratum interventions, (iv) is not supplied (kernel `substratumGen_not_control`, stated on the two-state carrier, `Fin 2` in `OIBridge/StructuralClosure.lean`; `papers/Main.md`:80, 588); with one continuously tunable state-mixing operation added "as an empirical controllability resource" the result is operational QM (kernel `substratum_plus_control_qm`, converse `qm_generated_by_substratum_extension`; `papers/Main.md`:588; `papers/GR.md`:256). Every operation the present interface sources preserves nonnegative entries (kernel `frozen_sourcing_verdict`, carried by no manuscript; `verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84).
- OI⁺ ⟺ exact finite endomorphic operational QM, each added principle independent (kernel `carrier_general_oiPlus`, `oiPlus_independence`; `papers/Main.md`:584–588). A characterization of an extension, not an entailment from bare OI (`papers/Main.md`:588).
- Approximate inclusion: one finite reversible realization reproduces a bounded quantum envelope to accuracy ε (paper proof with qubit-instance probe checks; `papers/Main.md`:596–598). Exact inclusion on one fixed finite carrier is obstructed (classical-dimension Proposition, `papers/Main.md`:558: the factorization half is proved there, the unboundedness of nonnegative rank is imported from [55]; the SIC remark is certified exactly over ℚ(√3), :560). Any exact endpoint needs a closure beyond one carrier whose finite predictive rank is not proved (`papers/Main.md`:356). The quasilocal completion exists and is unique given its stages, with no state or representation selected (kernel family "quasilocal completion"; `papers/Main.md`:588).
- Representability plus coherence does not select the relating unitary evolution (`papers/Main.md`:20).
- Research records on `main` (paper-level; not adopted, not kernel-checked; independent AI-agent reviews of each report; accountable Issue #1169 per their status notes):
  - OA-1 (`verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`:48–59). Under one affine φ acting on every cell, a stored setting acts on a carrier only by translation, under every measure; Fredkin bijections supply control, so the gap is specific to the gauge-derived affine class. The configuration-level interface is capped for every rule [K]; operations beyond it are open, not shown impossible.
  - OA-2 (`verification/programmes/oi-qm/reconstruction/oa-2-20261112/STATUS.md`:56–69). Theorem C: at a fixed finite carrier, reversible trace-preserving emergent operations form a finite group, for every rule. Theorem E(b): for the affine class, under (H1), H-AR (additive, cell-aligned observers), (H3) no supplied control, (H4) nested records, (SP) spanning and ledger item (xiv), the prepare–measure fragment is simplex-embeddable. The record labels its hand derivations unreviewed (:34–36). Non-affine rules are open.
  - OA-3 (`verification/programmes/oi-qm/reconstruction/oa-3-20261112/STATUS.md`:48–67). In SM's ring rule G_SM, with additive observers holding three consecutive sites, history or heralded composites, heralds, a measurement stage of at least 2(L−2) and condition (PT), the prepare–measure fragment is a simplex (Theorem S). Verdict "OPEN, narrowed"; not an impossibility result for G_SM. N4 there: Theorem E(b) holds with (H4) replaced by the heralded-composite effect class.
  - By contraposition (inferred): within these records' hypotheses, a prepare–measure fragment that is not simplex-embeddable needs a rule outside the affine class or the failure of one listed hypothesis (for G_SM, one of Theorem S's conditions). The candidate-specific Gate A results are in §1.

**2.2 Chain to the common model.** Axiom 1 + Definition → Lemma 1 (stipulated finite capacity) →
Lemmas 2–3 (partition; bijectivity part-empirical; measure posited) → S ⟺ D ⟺ Q_fb (kernel) →
C1–C4 diagnostics (kernel/paper) → operational QM only with (iv) and the OI⁺ principles added
(kernel for the implication; the added operation posited). Weakest link: the added operation.

**2.3 Additional premises.** Complex matrix kinematics (taken as given; open). Completion
conditions (iii)–(v) (not supplied; (iv) shown not supplied on the two-state carrier). Phases (a
stated intervention principle, not a consequence; kernel `onesFixing_not_phasesAvailable`,
`papers/GR.md`:256). The state-mixing datum (postulate; census family "state-mixing coupling
construction"). The Born exponent: not selected by the equivalence, a frontier item
(`papers/Main.md`:18, 554). (G1)–(G4) genericity for the Barandes route (`papers/Main.md`:716).
Sector condition C and access closure: not stated on `main` (§1).

**2.4 First missing step.** A physically sourced operation, in the same model, supplying condition
(iv) (and the phases), together with a sector condition C stated on the model with its coverage and
soundness directions (#1169 comment 6876591512, answer 2, where necessity is optional).
Kernel-only results narrow the target; each takes its datum, flow or gate as a stated input, and
none is carried by a manuscript:
- a class whose generated theory executes the layer flow has uncountably many pairwise
  non-proportional non-monomial rays at level one; necessary only (census family
  "coherent-continuum source");
- a nontrivial continuous one-parameter real orthogonal action on one distinguishable pair supplies
  the mixing datum under the five stated hypotheses, and with the stated closure gives exact finite
  operational QM on the two-valued carrier; the family's sourcing audit finds no corpus structure establishing those
  hypotheses (census family "real pair-flow reduction"; the theory-level biconditional, stated
  with nothing generalized beyond `Fin 2`, is "operational pair-flow equivalence");
- one fixed gate at an angle α with α/π irrational gives dense unitary control (census family
  "discrete completion") and, with the closure, dense but not exact finite QM, nothing beyond
  `Fin 2` at the endpoint (census family "dense-instrument bridge").

Accountable Issues: #1169, #1236.

**2.5 Compatibility.** See §9 rows QM–Bell, QM–GR, QM–SM, QM–BH and the QM–A1 entry beneath §9.
Exact inclusion is impossible on one fixed finite carrier under the factorization interface of
`papers/Main.md`:558 (factorization half proved, unboundedness imported), while A1 (ledger (ii)) is
used by the recurrence results (`papers/Substratum.md`:92), by `papers/GR.md`:585 and by the
Page-curve cycle averages. The recorded target already excludes one fixed finite total carrier
(#914 comment 6875046763).

**2.6 Test.** None stated as decisive: "no memory-witness outcome therefore falsifies the
ontology at present" (`papers/Main.md`:718–720). Tabletop tests with tunable hidden capacity are
named without a predicted outcome (`papers/Main.md`:722).

**2.7 Classification.** S/C/L: C (conditional on added principles), Layer 0, mixed (substratum
dynamics with an emergent operational layer). Part 4: CR.

## 3. Bell

**3.1 Results and status.**
- Unrestricted OI realizes PR-box behaviour (response-table construction; `papers/Main.md`:360, 427). Paper, with negative control in a probe. The same construction realizes arbitrary finite stochastic laws (`papers/Main.md`:360).
- Coupling-graph causal cone: influence moves one edge per update (`papers/Main.md`:362). Paper; an algebraic causal cone is kernel-checked in `OIBridge/QuasilocalAlgebra.lean`. No CHSH statement found in the kernel.
- Bell ceiling for a screened local completion, CHSH ≤ 2 (`papers/Main.md`:364–389). Paper proof; the pointwise bound over 16 response tables is exhaustive (`papers/oi_lattice_code/foundations/equivalence_recovery_probes.py`, check 11).
- Corollary: the nearest-neighbour cubic reference graph alone cannot supply option (a) for wings outside the graph cone (`papers/Main.md`:414). Paper.
- For a linear update (ledger (vii)) the dependence graph is the same at every state class, so a graph that varies between state classes requires an update outside (vii); the preparation-indexed edges of the adopted branch are dependences present at some states and absent at others, so that implementation "lies outside ledger item (vii)" (`papers/Main.md`:362, 414; `papers/SM.md`:104). Exact algebra (differences telescope). For the "equivalent nonlocal response map" named as an alternative (`papers/Main.md`:412), the status relative to (vii) is not stated.
- Measurement-dependent alternative: CHSH ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}, so I_ont ≥ 0.0309 bits for the quantum value; recorded, not adopted (`papers/Main.md`:416–423). Paper.
- H-Bell: prepared long-edge graphs must (i) supply parameter dependence, (ii) keep operational no-signalling, (iii) keep the metric/Ollivier–Ricci continuum limit (`papers/Substratum.md`:131–133). Open. Round `verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/` has a preregistration only.

**3.2 Chain.** Site factorization (viii) → coupling graph → cone (paper) → Bell ceiling under
(ii)–(iv) (paper) → observed violation (E2) forces giving up ontic parameter independence →
preparation-indexed adjacency (proposed) → H-Bell (open). Weakest link: H-Bell.

**3.3 Premises.** (viii) site factorization (posited); (xiv) measurement independence (posited);
determinism (A2); M1-B, the branch assignment of Bell data (`papers/Substratum.md`:123), a modeling
premise; H-Bell (open). Exclusion of supraquantum correlations in the physical sector: required by
the target (#914 comment 6875046763, decision 3; comment 6875548603); full quantum Bell-set
soundness over the agreed two-wing interface inside a physically justified C is the planning
obligation BELL-QSET (#1060, question 3). No mechanism is stated in the corpus.

**3.4 First missing step.** A specified preparation-indexed edge rule (or response map) for which
the CHSH value is the quantum one and the remote marginal is setting-independent. Beyond CHSH
values, the recorded obligation covers the whole agreed two-wing interface (permitted
preparations, settings, interventions, compositions and complete accessible histories) inside a C
justified without testing whether the resulting correlations are quantum (#1060, question 3).

Accountable Issues: #1060, for H-Bell, Tsirelson selection and BELL-QSET, the last added by owner
decision (`amaybaum`, 2026-11-14, quoted verbatim): "I approve, proceed as suggested" (#914
comment 6877803663, 2026-11-14T13:13:09Z; also #1060's body). The
quantum-set coverage direction stays under #868; the broader operational-selection problem is
related to #1143. #1291 is provenance only: BELL-QSET's scope requirements were first drafted there,
and it is closed as a duplicate of #1060.

**3.5 Compatibility.** Known not to hold with global A5 for the preparation-indexed adjacency
implementation (exact algebra, `papers/Main.md`:362, 414). Under global A5 with (viii), (x), (xiv)
and the Corollary's intervention and readout conditions, CHSH ≤ 2 for wings outside the graph cone;
wings inside the graph cone, including wings spacelike with respect to a wave-speed cone, are not
covered (`papers/Main.md`:414). (x) and Stage 2's result are scoped to the reference class
(`papers/Main.md`:724; `papers/Substratum.md`:171); no source so scopes A5. Theorem 23 assumes
A1–A6, A5 included, and makes the Bell-inclusive completion conditional on H-Bell alone
(`papers/Substratum.md`:193); see D4. Undetermined with GR curvature (H-Bell (iii)). Which cone is
the physical c (graph cone, ℓ₁ reach 1/‖n̂‖₁, against wave speed 1/√3) is not derived
(`papers/Main.md`:414).

**3.6 Test.** None stated beyond E2 itself, which already excludes the reference-graph-only model
for wings outside the graph cone (`papers/Main.md`:414).

**3.7 Classification.** L (pending H-Bell), Layer 0 (spatial constitution), substratum. Part 4:
open in the common model, since H-Bell's clause (i) is the required dependence itself; in the
abstract class, response-table realizations of quantum and supraquantum laws exist
(`papers/Main.md`:360, 427).

## 4. GR (field equations and matter–geometry coupling)

**4.1 Results and status.**
- Ladder: G1 horizon identities (this paper's register); G2 weak-field consistency; G3 covariant field equations with conservation/Bianchi structure and continuum limit, open; G4 cosmological implications conditional on G3 (`papers/GR.md`:12).
- ħ = c³ε²/(4Gσ), ε = 2√σ l_p, S = A/(4l_p²): conditional on H-slope, H-count, horizon and frame conditions, local boost structure, symmetric rate ratio; the count S = σA/ε² unconditional (`papers/GR.md`:12, 24, 28). Paper. The relation fixes only ε/√σ (`papers/GR.md`:306, 547).
- The Einstein equations are used through Jacobson's relation and not derived (`papers/GR.md`:162; `book/ch07-gravity.md`:44). Closure, Lovelock and spin-2 routes require hypotheses not established (`papers/GR.md`:162).
- Discrete Einstein equation κ_OR = α𝒯 is a target form; the hop-metric Ollivier route fails at the reference instantiation (ℓ₁ metric, √2 stretch), and the equation is not established by the cited chain (`papers/SM.md`:144–150; `papers/Substratum.md`:171). Lattice Bisognano–Wichmann form is an open hypothesis (`papers/SM.md`:140–142).
- Newtonian a = GM/r² and Poisson equation at fixed G from holographic equipartition, on an assumed energy shell; N_dof = A/l_p² adopted, not derived; nonlinear G_μν = 8πG T_μν not established (`papers/GR.md`:689–697). Paper, consistency level.
- Matter coupling: three completions for a laboratory source in superposition, selection open (`papers/GR.md`:350); whether the uniform offset sources curvature is the open G3 coupling step (`papers/GR.md`:352). Accountable Issue: #873.

**4.2 Chain.** Cosmological horizon as the partition (`papers/GR.md`:40, which takes GR's causal
structure as given) → C1–C3 checked, C4 not discharged (`papers/GR.md`:46–52) → H-count classical
temperature (`papers/GR.md`:58) → H-slope KMS matching (`papers/GR.md`:74) → ħ calibration →
Jacobson input → (G3 open). Weakest link: G3; at G1, H-slope.

**4.3 Premises.** H-count, H-slope, H-balance, H-frame, H-Hawking (i)–(v) ((iv),(v) discharged by
§4), H-state split into H-shell, H-energy, H-spectrum, H-BD (posited), H-BG, H-local-lift, local
boost structure, symmetric rate ratio, σ = 1 for quoted ε (`papers/GR.md`:58–60, 88, 122, 328,
649). H-slope and H-count are selection conditions that do not follow from bijectivity
(`papers/Substratum.md`:181). Energy shell: assumed, not a consequence of Lemma 3
(`papers/GR.md`:697). W1, the equality of the whole hidden sector's shell entropy–energy slope
with the boundary-count slope, is an additional assumption on the paper-level W1-1 record; GR:58's
setting with H-count implies its prerequisite W1-0 and its counted-set form W1-min (reading L), and
the converse fails by a witness (`verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48–59,
66–67; `W1-1-REPORT-r4.md`:301–302). The one distinct sufficient route found, a deep sector whose
thermally accessible configurations are collective (C6(a)), is open for the finite substratum and
fails in the real lift of the linear rule, |α| < 1/d (W1-1 STATUS:60–62; paper-level).

**4.4 First missing step.** The covariant field equation, including which stress-energy sources
curvature, from (S, φ) (G3), with a curvature construction that works on the reference graph.

**4.5 Compatibility.** GR's geometry-first ordering (classical metric prior to the trace-out,
`papers/GR.md`:340–348) and SM §3.1's route, in which geometry is read from a coupling graph that
varies with the state (`papers/SM.md`:104, 158), differ in which comes first; no source states
them inconsistent: undetermined (Q4). The proved conflict between a graph that varies with the
state and global A5 is internal to SM (§9, beneath the table). H-shell assumes weak boundary
coupling while C1 requires nonzero cross-boundary coupling; the source states the tension
(`papers/GR.md`:60).

**4.6 Test.** GW250114 tests the classical area theorem, which the framework preserves, not the
1/4 coefficient (`papers/GR.md`:12, 318). Free-dispersion Lorentz violation O((kε)²), interactions
open (`book/appendix-a-prediction-status.md`:113). Gravitationally mediated entanglement tests
depend on the open (a)–(c) selection (`papers/GR.md`:350). No echoes expected (`papers/GR.md`:597).

**4.7 Classification.** Calibration C, Layer 0, mixed; field equations imported (E-type input).
Part 4: CR at G1–G2; GR ⊆ OI not established.

## 5. Standard Model (gauge group, matter, interactions, parameters)

**5.1 Results and status.**
- Six signed links decompose exactly as 6 = T₁(3) ⊕ E(2) ⊕ A₁(1) (Theorem 7, `papers/SM.md`:374). Kernel (census family "representation bridge and counting": `theorem_7`, `LinkDecomposition`); integer certificates in `verification/lean/OI_Gauge_Certificates.lean`.
- Identification of the link space with the physical carrier: H-link (single-copy clause K = 6); custodial route H-cust (condensate clause a premise); component-blind trace-out H-blind (`papers/SM.md`:12, 26, 32, 374).
- Gauge group U(3)×U(2)×U(1) from the bicommutant; reduction to SU(3)×SU(2)×U(1) uses a specified charged matter action and anomaly cancellation (`papers/Substratum.md`:163). Paper.
- Simple cubic selected among the 14 Bravais lattices as the one compatible with the observed gauge group (Theorem 7b, `papers/SM.md`:390); "empirically-anchored", "forced by the observed gauge group" (`papers/SM.md`:14, 56, 1424). "The Standard Model from a cubic lattice" and "the lattice is cubic because SU(3) is observed" are "the same fact stated in two directions" (`papers/SM.md`:1424).
- d = 3 by filters E5–E7 within A4's periodic-lattice class; self-consistency strength; E7 inherits H-count (`papers/SM.md`:30, 1424; `papers/Substratum.md`:157).
- 1 ⊕ 3 taste decomposition proved (Theorem 8, kernel `theorem_8`); three physical generations conditional on H-spin′ (free kernel refuted and 4D-staggered route negative, numerical probes; condensate-dressed form open); chirality H-χ′ open, minimal embedding certified vector-like (`papers/SM.md`:543, 1320).
- Hypercharges unique given the family pattern and chirality, apart from Y_Q = 0 (Theorem 15, `papers/SM.md`:589). Paper (exact algebra).
- Couplings: 1/α₀ = 23.25 computed; δ₀ empirical; SU(2), SU(3) retrodictions; A·B comparison inconclusive (`papers/SM.md`:14, 1273–1276). The Haar-measure induced theory confines in Monte Carlo, against the deconfined phase the matching needs; candidate resolution via H-observer-bundle and H-Y-vertex (`papers/SM.md`:801–811).
- Parameters: of 22 tabulated observables, 2 S, 5 C, rest L/M/R/P/E (`papers/SM.md`:1269–1316); m_s, m_c, CP phases, neutrino masses open or solution-specific (`papers/SM.md`:1322). Strong CP: θ ∈ {0, π}; θ̄ open under H-top, H-det (`papers/SM.md`:655, 669).
- The observer-level operator: "the map φ → L_obs → Δ_g is not proved anywhere in this framework"; §4's dispersion results, the Lorentz-invariance argument and Theorem 6's mode count rest on it (`papers/SM.md`:232).
- Source self-classification: "a tight compression of the Standard Model onto the cubic-lattice commitment … rather than … a derivation of the Standard Model from first principles" (`papers/SM.md`:14, 1428; `book/ch19-open-problems.md`:224).

**5.2 Chain.** (S, φ) + (viii) + A3–A6 + (x) → wave equation (`papers/SM.md`:224, uses A5) → cubic
lattice (selected by observed gauge group) → Theorem 7 (kernel) → H-link/H-cust → gauge group →
staggered tastes → H-spin′ → H-χ′ → hypercharges → induced coupling + empirical threshold. The SM
paper consumes "the emergent quantum description and its Born-rule statistics" from [Main]
(`papers/SM.md`:22). Weakest link: H-χ′ (open); H-link and H-cust are conditional.

**5.3 Premises.** A3–A6, (viii), (x), (xiii); H-link, H-cust, H-blind, H-spin′, H-χ′, H-top, H-det,
H-observer-bundle, H-Y-vertex; alphabet-size hypothesis (`papers/SM.md`:56); E4–E7; site and
internal factorizations as Tier 3 stipulations (`papers/SM.md`:1426).

**5.4 First missing step.** Three steps are stated as unproved or open, each to be derived from the
model: the observer-level map φ → L_obs (`papers/SM.md`:232), the physical carrier identification
(H-link) and weak chirality (H-χ′). The sources state no order among them.

**5.5 Compatibility.** Uses A5 (Stage 2(b), `papers/Substratum.md`:159), which conflicts with the
Bell route's preparation-indexed implementation and with SM's own §3.1 geometry as stated (§9).
Uses QM as an input (E1; `papers/SM.md`:22).

**5.6 Test.** JUNO sin²θ₁₂ = 1/3 − 1/(4π²): a retrodiction at current precision, with JUNO's
design-lifetime precision named as a pre-registered forward test
(`book/appendix-a-prediction-status.md`:98, 211); detection of proton decay falsifies; monopole
non-observation (`papers/SM.md`:831, 839); no θ̄/EDM prediction (`papers/SM.md`:655).

**5.7 Classification.** Gauge group: C (H-link, H-cust) given the cubic-lattice commitment. That
commitment is selected by the observed gauge group (Theorem 7b; `papers/SM.md`:1424), so as a
forward derivation from the model the gauge group is an empirical input (E). Layer 0, substratum.
The lattice and d = 3 are E-type inputs; generations C (H-spin′); chirality open. Part 4: CR.

## 6. Cosmological constant

**6.1 Results and status.** Two descriptions: classical substratum ρ ~ H²/G vs emergent QFT
ρ_QFT ~ M_Pl⁴ (`papers/GR.md`:334–336). Ratio ~ S_dS (dimensional identity; `papers/GR.md`:362).
Descriptive distinction established; dynamical decoupling conditional on G3: two gravitational
completions share the same substratum, partition, transition law and calibration while differing
by the offset (`papers/GR.md`:352). The value of Λ is an input set by initial conditions
(`papers/GR.md`:356). Higgs and QCD vacuum shifts treated the same way, conditional on the same
coupling step (`papers/GR.md`:569–575). Paper.

**6.2 Chain.** QM branch (emergent Ĥ_eff) + GR branch (geometry-first ordering, `papers/GR.md`:340–348)
→ H_tot vs Ĥ_eff distinction (`papers/GR.md`:358) → G3 coupling (open). Weakest link: G3.

**6.3 Premises.** Geometry-first ordering (stated as forced by definiteness, non-circularity and
universality of ħ, `papers/GR.md`:344–348; status: argument on paper, its dynamical content
conditional on G3); H-local-lift for the local emergent QFT (`papers/GR.md`:328); spatial product
structure of C_V.

**6.4 First missing step.** The G3 coupling theorem stated for the uniform offset.

**6.5 Compatibility.** Requires the same metric to be classical at the partition boundary (GR) and
to emerge from the substratum graph (SM §3.1): undetermined (§9). The ν magnitude in §7 imports the
emergent running that §6.2 denies gravitates absolutely; the source states two readings
(`papers/GR.md`:400).

**6.6 Test.** None stated for the dissolution; the descriptions are stated to be non-adjudicable
from accessible data (`papers/GR.md`:362). The ν test belongs to §7.

**6.7 Classification.** Descriptive part: paper result; dynamical dissolution C pending G3, Layer
0, mixed; Λ value E. The condition the CR carries is the selection between two gravitational
completions that share substratum, partition, reduced transition law, fixed-basis representation
and calibration and differ only in the offset (`papers/GR.md`:352). Part 4: CR.

## 7. Cosmology (dark sector, expansion)

**7.1 Results and status.**
- Running vacuum Λ_eff(H) = Λ₀ + 3ν(H² − H₀²)/(8πG): form "not a distinctive prediction" (every smooth model has it); content is the Type II channel, a structural reading, not a derived law (`papers/GR.md`:374–380). |ν| ≈ |ν_QFT| ~ 10⁻³², conditional on the §7.3 split, not at theorem level (`papers/GR.md`:382–398; `book/appendix-a-prediction-status.md`:109, class L).
- ρ_s = ρ_crit identity; ~95% invisible budget, fraction 1 − Ω_B by construction, partly definitional (`papers/GR.md`:418–452). Its step (ii-b) needs the geometry-first ordering (`papers/GR.md`:448–450).
- a₀ = cH/6 with the factor imported from Verlinde; BTFR; conditional on H-count, H-slope, H-frame, H-Hawking (`papers/GR.md`:466–486). MOND-like core vs CDM-like linear growth: crossover not derived, relaxation kernel uncomputed (`papers/GR.md`:524).
- Tensions: Jiao et al. (2023) Milky Way decline and Genzel et al. high-z curves (`papers/GR.md`:12, 536–545); DESI phantom-crossing preference 3–4σ against w ≈ −1 (`papers/GR.md`:412).
- Expansion history: H value an initial-condition input (`papers/GR.md`:356); inflation "not addressed" (`book/ch19-open-problems.md`:194); Hubble tension open (`book/ch19-open-problems.md`:168).

**7.2 Chain.** Horizon partition → H-count/H-slope de Sitter temperature (conditional) → Jacobson
Clausius at the horizon (imported) → geometry-first ordering → Q = M_Bc² (local assumption,
`papers/GR.md`:466) → Verlinde factor (imported). Weakest link: matter-to-boundary coupling (G3).

**7.3 Premises.** As §4.3, plus C2 at the horizon (τ_B ≳ 1/H, "not derived from the substratum
dynamics", `papers/GR.md`:456), Q = M_Bc², elasticity assumption of [20], emergent locality of
boundary coarse-graining (`papers/GR.md`:400 remark).

**7.4 First missing step.** The H-dependence of the uniform/structured split of boundary entropy,
which fixes ν (`papers/GR.md`:382–386), and the relaxation kernel.

**7.5 Compatibility.** ν magnitude uses SM masses through the Shapiro–Solà formula
(`papers/GR.md`:390–394) and the same emergent-locality premise as Lorentz invariance
(`papers/GR.md`:400): consistent as stated, undetermined in substance. E7, used for d = 3 in the SM
branch, is an inferred ΛCDM-pipeline quantity (`papers/Substratum.md`:88).

**7.6 Test.** DESI Y5: |ν| ≳ 10⁻³ refutes the magnitude at the specific-representative level
(`papers/GR.md`:591–593); a high-confidence detection of phantom crossing falsifies the prediction
at structural level (`papers/GR.md`:412, outcome (iii)); detection of particle dark matter
accounting for the structured sector falsifies the corollary (`papers/GR.md`:460); rotation-curve
comparisons not yet quantitative (`papers/GR.md`:12).

**7.7 Classification.** a₀ C (factor imported), budget C (partly definitional), ν L at Layer 2(a)
(`book/appendix-a-prediction-status.md`:109); a₀ Layer 0/1 and budget Layer 1 (same table); mixed.
Part 4: CR.

## 8. Black-hole information

**8.1 Results and status.**
- Information conserved because φ is bijective by premise; how much the radiation carries is not settled by bijectivity (`book/ch19-open-problems.md`:72). Bijectivity does not imply recovery from accessible records, and complete endpoint access with bijectivity suffices (exhaustive finite computation, exploratory, internally reviewed: `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md`).
- Nested trace-outs consistent (Theorems A.1–A.4, `papers/GR.md`:601). GSL open; Theorem A.6 bound two-sided (`papers/GR.md`:603).
- Page curve: Theorems A.8–A.9 conditional on H-scramble and H-decouple with the full product shell (`papers/GR.md`:605, 797, 831). H-scramble fails for every bijection on a definite configuration with an aligned bipartition; the theorems "as stated have no instance" in that setting (`papers/GR.md`:805, 813–823). Paper proof; exhaustive check (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`, C1, C6(a)). Entropy at an aligned cut is bounded by the initial distribution's entropy, S(ρ_R(t)) ≤ H(p₀), for every bijection (`papers/GR.md`:823–827; C2 there); from a supplied superposition, random permutations give Page-like states (C3 there, numerical, scoped; the superposition is supplied by the analyst and is not an OI mechanism, and C3 is not a derivation of H-scramble). BH-02 is exploratory research, internally reviewed, not adopted (REPORT:3). C1's exhaustive check covers (q,n) = (2,2), (2,3), (3,2) and 500 sampled permutations at (2,4); the general statement is the paper proof. Open outside the counted setting: an initial superposition (`papers/GR.md`:815, 827, 839), a non-aligned bipartition (:815), an ensemble restatement of A.8 (:827, "not given here"), and the proper-shell case (:829). Page time 0.646 t_evap conditional on β = 1 and the half-entropy turnover (`papers/GR.md`:605; BH-04).
- Status row G11: open (`book/appendix-a-prediction-status.md`:111).

**8.2 Chain.** A2 (premise) → nested partition (paper) → H-scramble (fails in the counted
setting; open outside it) → Page value. Weakest link: H-scramble.

**8.3 Premises.** A2; H-scramble (fails for every bijection in its counted setting; open outside
it. BH-02 C3, numerical and exploratory, gives Page-like states from a supplied superposition under
random permutations; this is not an OI mechanism); H-decouple (open); full product energy shell
(open for an evaporating hole); β = 1; the island ↔ cycle correspondence (conjectural,
`papers/GR.md`:861).

**8.4 First missing step.** A preparation (initial superposition) or a non-aligned bipartition that
the model supplies, under which a scrambling statement holds (`papers/GR.md`:815;
`papers/Introduction.md`:169).

**8.5 Compatibility.** H-scramble fails, for every bijection, on definite initial configurations at
aligned bipartitions (proved). The failure comes from configurations being mapped to
configurations, not from finiteness of the orbit; finiteness enters only through A.8's
cycle-average bookkeeping (`papers/GR.md`:813, 823; BH-02 C6(b)). The exact linear rule splits
large energy shells into many cycles at prime q (`papers/Main.md`:724 (v); `papers/SM.md`:294):
tension with single-shell cycle typicality, undetermined.

**8.6 Test.** Controls stated in the programme record (non-scrambling permutation must fail). No
observational test of the Page curve is stated; standard ringdown without echoes is expected
(`papers/GR.md`:597).

**8.7 Classification.** Open (G11 open; no instance in the counted setting). Part 4: neither CR
nor UD at present.

## 9. Joint-satisfiability table

"Known not to" means a stated result makes the two premises jointly inconsistent as stated.

| Pair | Premises A | Premises B | One model known to satisfy both? | Reason / source |
|---|---|---|---|---|
| QM–Bell | completion (i)–(v), added control | (viii), (xiv), H-Bell | undetermined | Composition of entangled preparations needs coherent instruments (`papers/Main.md`:572); neither is sourced |
| QM–GR | finite carrier, C1–C4; Ĥ_eff | horizon partition presupposing GR causal structure; H-state, H-energy | undetermined | `papers/GR.md`:40, 60: Ĥ_eff not shown to survive the trace-out; C4 not discharged at the horizon (`papers/GR.md`:52) |
| QM–SM | operational QM from the model | E1 (observed QM) as input; Born statistics consumed; A5; G_SM | undetermined | SM uses QM as input (`papers/SM.md`:22; `papers/Substratum.md`:76, 123), a stated dependence, not a conflict. Separately, under A5's affine class and named observer hypotheses the prepare–measure fragment is simplex-embeddable (OA-2 Theorem E(b)), and so is G_SM's under OA-3's conditions; a stored setting acts only by translation (OA-1 Gap 2). These are paper-level research findings, not established (§A.46 item 7), and conditional on the listed hypotheses (§2.1). Forward trace is #1211 |
| QM–CC | Ĥ_eff offset invisible to quantum data | G3 coupling | undetermined | `papers/GR.md`:352 |
| QM–Cosmology | C2 slow bath at horizon | τ_B ≳ 1/H not derived | undetermined | `papers/GR.md`:456 |
| QM–BH | exact QM inclusion; coherent preparation | A1 cycle averages; superposed initial state | known not to, for exact inclusion on one fixed finite S under the factorization interface of `papers/Main.md`:558; undetermined on a completion, where A.8's finite cycle decomposition would need a counterpart (not stated) | `papers/Main.md`:356, 558; `papers/GR.md`:605, 815 |
| Bell–GR | preparation-indexed long edges | Ollivier–Ricci/continuum curvature | undetermined | H-Bell (iii) open; hop-metric route fails even on the reference graph (`papers/SM.md`:150; `papers/Substratum.md`:171) |
| Bell–SM | preparation-indexed adjacency (update outside (vii)) | A5 linearity in Stage 2(b), wave equation | known not to, for global A5 with the preparation-indexed adjacency route; undetermined for the "equivalent response map" alternative and with A5 restricted to the reference class | Exact algebra, `papers/Main.md`:362, 414; `papers/SM.md`:104, 224. Under global A5 with (viii), (x), (xiv) and the Corollary's conditions, CHSH ≤ 2 for wings outside the graph cone; wings inside it are not covered (`papers/Main.md`:414). For the response-map alternative (`papers/Main.md`:412) the status relative to (vii) is not stated. (x) and Stage 2 are scoped to the reference class (`papers/Main.md`:724; `papers/Substratum.md`:171); A5 is not, and no source treats that restriction |
| Bell–CC | — | G3 | undetermined | no shared premise traced |
| Bell–Cosmology | — | emergent locality of boundary coarse-graining | undetermined | long edges vs locality premise of `papers/GR.md`:400; not traced further |
| Bell–BH | entangling preparation | H-scramble needs superposed initial state | undetermined | both need a preparation resource not sourced |
| GR–SM | geometry-first ordering; harmonic boundary modes (SM wave equation, `papers/GR.md`:695) | A5; Stage 2(b) | undetermined | no conflict between GR's premises and A5 traced; the stated conflict involving SM §3.1 is internal to SM (beneath this table) |
| GR–CC | G3 open | G3 coupling | consistent as dependency | CC dissolution is conditional on the GR step |
| GR–Cosmology | H-count, H-slope, H-frame, H-Hawking | the same, plus Q = M_Bc² | consistent as stated (same premises) | `papers/GR.md`:466 |
| GR–BH | horizon conditions | H-decouple, full shell | undetermined | `papers/GR.md`:605 |
| SM–CC | Higgs and QCD vacuum shifts | uniform-offset decoupling | undetermined | `papers/GR.md`:569–575, conditional on G3 |
| SM–Cosmology | SM masses; d = 3 via E7 | Shapiro–Solà ν; E7 inherits H-count | consistent as dependency | `papers/GR.md`:390; `papers/SM.md`:30 |
| SM–BH | A5 exact linear rule | single-shell typicality | undetermined (tension) | `papers/SM.md`:294 |
| CC–Cosmology | offset does not gravitate | emergent running enters ν | consistent under either reading stated | `papers/GR.md`:400 |
| CC–BH | — | — | undetermined | no shared premise traced |
| Cosmology–BH | cosmological horizon primary partition | BH horizon not an epistemic partition | consistent as stated | `papers/GR.md`:597 |

Stated conflict with a common-model input. QM–A1: exact inclusion (the target) and A1 as stated
(`papers/Substratum.md`:92) are known not to be jointly satisfiable on one fixed finite carrier,
under the factorization interface of `papers/Main.md`:558 (factorization half proved there,
unboundedness imported from [55]). The recorded target already excludes one fixed finite total
carrier (#914 comment 6875046763); which A1 uses must be restated on an admitted carrier is Q5.

Stated conflicts and tensions inside a branch: SM §3.1's principle that the coupling graph G(v)
evolves with the state (`papers/SM.md`:104, 158; its Einstein step a target form, :144) is known
not to hold together with global A5 (exact algebra, `papers/Main.md`:362; `papers/SM.md`:104),
which SM's wave equation and Stage 2(b) use (`papers/SM.md`:60, 224); C1 (nonzero coupling) against
H-shell (weak boundary coupling), `papers/GR.md`:60; C2 slow-bath motivation from a rounded map
outside A5, `papers/Main.md`:724 (v); MOND-like vs CDM-like regimes, `papers/GR.md`:524; graph cone
vs wave speed as the physical c, `papers/Main.md`:414.

## 10. Shared missing mechanisms

Entries in "Branches blocked" marked "inferred" are this ledger's assignments; no source states
them.

| # | Mechanism | Corpus statement | Branches blocked |
|---|---|---|---|
| M1 | Observer-interface lift: a derived map from φ to the observer-level operator and generator, preserving locality and isotropy | φ → L_obs → Δ_g not proved (`papers/SM.md`:232); H-local-lift (`papers/GR.md`:328); Ĥ_eff vs H_tot (`papers/GR.md`:60); relating evolution not selected (`papers/Main.md`:20) | QM, SM, GR, Cosmology (ν), CC |
| M2 | Nonclassical operation resource: continuously tunable state mixing and phases | not supplied (kernel `substratumGen_not_control` on the two-state carrier, `frozen_sourcing_verdict`); posited as a resource (`papers/Main.md`:588); kernel-only reductions in §2.4 | QM, Bell (coherent composite instruments) |
| M3 | Preparation resource: coherent or superposed preparations, entangling preparations, the hidden prior μ_H | μ_H not fixed by the partition (`papers/GR.md`:88); superposed initial state or non-aligned partition needed (`papers/GR.md`:815); entangling preparation supplies long edges (`papers/Substratum.md`:131) | BH, Bell, QM, GR (H-state) |
| M4 | A nonlinear or preparation-indexed update | Bell branch outside (vii) (`papers/Main.md`:414); G(x) varying with the state outside A5 (`papers/SM.md`:104); mixing evidence from a rounded map (`papers/Main.md`:724 (v)); affine-class constraints, paper-level: OA-1 Gap 2, OA-2 Theorem E(b) (§2.1), which are obstructions within the affine class under named hypotheses, not statements that a nonlinear update is needed | Bell, SM §3.1 geometry route; QM and BH inferred; conflicts with SM Stage 2(b) |
| M5 | Completion beyond one finite carrier | classical-dimension obstruction (`papers/Main.md`:558); closure rank not proved (`papers/Main.md`:356); quasilocal completion selects no state (`papers/Main.md`:588) | QM (exact inclusion); conflicts with A1 as total finiteness on one fixed finite carrier (§9, QM–A1); A1 uses (recurrence, BH cycle averages) to be restated (Q5); GR inferred (G3's continuum limit, `papers/GR.md`:12, is a different completion) |
| M6 | Matter–geometry coupling theorem (G3) | `papers/GR.md`:12, 350, 352; matter-to-boundary map (`book/appendix-a-prediction-status.md`:102) | GR, CC, Cosmology |
| M7 | Physical discharge of C4 at the physical cuts | not discharged at the cosmological cut (`papers/GR.md`:52); sealed core carries no routed witness (`verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md`:30–45) | QM (physical realization), GR, Cosmology (memory effect), SM prerequisites |
| M8 | Continuum geometry from the graph | hop-metric Ollivier route fails; re-founding on Laplacian geometry proposed (`papers/SM.md`:150; `papers/Substratum.md`:171) | GR, Bell (H-Bell (iii)); Cosmology inferred (its chain uses horizon thermodynamics, `papers/GR.md`:422–426, 466) |
| M9 | Energy shell and density-of-states conditions | shell assumed (`papers/GR.md`:697); H-count, H-slope selection conditions (`papers/Substratum.md`:181); W1 an additional assumption, and W1-0, the conserved real-valued energy shell, not carried by the ħ condition lists or Main's posit ledger; the C6(a) route fails in the real lift of the linear rule (paper-level, `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48, 60–62, 71–73) | GR, Cosmology, CC, BH (full shell) |

## 11. Document disagreements and mirror gaps

- D1. `book/ch19-open-problems.md`:20 heads §19.2 "Problems resolved". Its entries state "the paradox is not resolved" (:72), strong CP "Not resolved" (:80), quantum gravity "Partially addressed" (:28), and the section's opening sentence (:22) itself names an unresolved entry and split-status entries. The disagreement is the heading at :20 against the entries.
- D2. H-Bell section reference: `papers/Main.md`:20, `papers/SM.md`:14 and `papers/SM.md`:60 cite [Substratum §3.3]; `papers/Introduction.md`:145 cites [Substratum §3.2]; the definition is at `papers/Substratum.md`:131–133, inside §3.2 (Stage 1), and its Stage-2 use at :171, inside §3.3.
- D3. Dual citation, consistent: the five completion conditions are cited as [GR §3.3] (`papers/Substratum.md`:14; `book/ch01-observation.md`:185; `book/ch00-introduction.md`:55) and as Main §3.4 (`papers/Main.md`:80); both sites carry the statement (`papers/GR.md`:212–216; `papers/Main.md`:562), and `papers/Substratum.md`:373 cites both. Not a disagreement.
- D4. The statement that a coupling graph varying between state classes needs an update outside (vii)/A5 is at `papers/Main.md`:362, 414 and `papers/SM.md`:104. Not found in `book/` or in the H-Bell definition (`papers/Substratum.md`:131–133) on the phrases searched ("item (vii)", "outside A5", "varies with the state", A5 near Bell or G(x)). The book chapters carry the preparation-indexed route without that condition. Theorem 23 (`papers/Substratum.md`:193) takes A1–A6, A5 included, and makes the Bell-inclusive completion conditional on H-Bell alone; its preparation-indexed implementation (:131) is outside (vii) by `papers/Main.md`:414.
- D5. The dark-sector corollary is stated "under Lemmas 1–3 and conditions (C1)–(C4)" (`papers/GR.md`:418); its proof step (ii-b) uses the geometry-first ordering (`papers/GR.md`:448–450), step (i) uses Jacobson's Clausius relation (:426) and a classical temperature T_cl taken from §3.1 (:422), which rests on H-count (:58), and the abstract places the dark sector at G4, conditional on G3 (`papers/GR.md`:12).
- D6. `book/ch19-open-problems.md`:178 states the framework "does not carry an obligation" to derive the baryon-to-photon ratio; the adopted Part 4 requires accounting for "other claimed downstream consequences" (#914 comment 6877420015). Planning record against manuscript; recorded as a question (Q6), not a correction.

D7–D10 were found while the r3 registry was built. They are recorded, not resolved, and the
coverage audit is separate.

- D7. `book/ch18-beyond.md`:256 describes "SU(2) as chiral and SU(3) as vector-like, derived from the staggered trace-out". Chirality is open under H-χ′, and the minimal embedding is certified vector-like (`papers/SM.md`:543, 1320; `book/ch19-open-problems.md`:328).
- D8. `book/ch10-chemistry.md`:86–88 states that "SU(3) color confinement (Chapter 5 §5.4) produces bound hadrons" and that the nuclear-binding mechanism "is derived from the gauge structure of SU(3)". `book/ch05-gauge-structure.md` §5.4 (from :81) carries no confinement statement, and the papers carry no derivation of confinement for the framework's gauge measure (`papers/SM.md`:801–811; B-QCD-5).
- D9. `book/ch19-open-problems.md`:88 states that the substratum lattice "eliminates the divergence and with it the cutoff sensitivity of m_H". `papers/SM.md`:613 and :1570 present that protection as "structurally identified", with "the theorem-level derivation" deferred.
- D10. `book/ch10-chemistry.md`:78–80 calls the Sakharov ingredients "derived" and the possibility of baryogenesis "a theorem" from the three-generation structure and P-breaking. Three physical generations are conditional on H-spin′, chirality is open (`papers/SM.md`:1320), and the CP phases are solution-specific inputs (`papers/Substratum.md`:415; `book/ch19-open-problems.md`:184).

## 12. Open owner questions

1. **One observer interface.** The branches use different cuts: the abstract visible/hidden partition (QM), the cosmological horizon (GR, CC, cosmology), the component-complete site observer (SM, H-blind), nested horizons (BH). The recorded target already requires a compatible model and operational interface (#914 comment 6875046763). Must Part 4's single model carry one interface, or a stated family of nested partitions (GR Appendix A) counted as one interface?
2. **Linearity.** Keep A5 globally (excluding the stated Bell route and SM §3.1 geometry), restrict it to the reference state class, or replace it? Which A5-dependent results (wave equation, Stage 2(b), harmonic boundary modes, the eight located uses in round H-D) are to serve as preserved controls under §A.29?
3. **Empirical selection.** Do the simple-cubic Bravais type (selected by the observed gauge group) and d = 3 (filters E5–E7) count under Part 4 as admissible empirical inputs, or as assumptions introduced to reproduce the outcome that Part 4 excludes?
4. **Geometry order.** Is a classical metric at the partition boundary a premise of the model (`papers/GR.md`:340–348), or must it be derived from (S, φ) (`papers/SM.md`:104; `papers/GR.md`:689)? The QM branch's physical partition currently presupposes GR causal structure (`papers/GR.md`:40).
5. **Carrier.** The recorded target excludes one fixed finite total carrier (#914 comment 6875046763) and requires arbitrarily large finite carriers (#1169 comment 6876591512, answer 3). Which finite-carrier results (recurrence, P-indivisibility at `papers/GR.md`:585, A.8's cycle averages) must be restated on the admitted carrier?
6. **Scope of Part 4.** Are solution-specific quantities (CP phases, m_s, m_c, neutrino masses, baryon asymmetry; `papers/SM.md`:1322; `book/ch19-open-problems.md`:178) inside the derivation obligation, or recorded empirical inputs?
7. **Bell sector.** The exclusion of supraquantum correlations in the physical sector is decided (#914 comments 6875046763, decision 3, and 6875548603; access closure, #1169 comment 6876591512, answer 4) and is tracked as BELL-QSET (#1060). Is H-Bell (no-signalling, continuum curvature) the route by which C's recorded exclusion is to be met, or is that exclusion to be stated on C directly?
8. **Initial-condition posits.** Are measurement independence (xiv) and the hidden prior μ_H admissible as posits about initial conditions, or must the model derive them?
9. **QM as input to SM.** Is a forward SM trace (#1211) that consumes observed QM (E1) to be recorded as an intermediate result? Part 4 already states that a conditional reconstruction "does not discharge" the derivation obligation (#914 comment 6877420015), so the open part is how such a trace is recorded, not whether it discharges the obligation.
10. **Black-hole information.** Is information conservation by the premise A2 accepted for Part 4, or is recovery from accessible radiation records required (BH-01 shows the two differ)?
11. **Manuscript disagreements D1, D2, D4, D5 and D7–D10.** Should any be scheduled as a separate correction unit under §A.25? This ledger authorizes none.
12. **Standard of independent physical justification.** What standard does Part 4 apply to named hypotheses that a source records as additional assumptions (for example W1, `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48, and H-count, H-slope and H-scramble, `papers/GR.md`:58, 74, 815)?
13. **Common model.** Which model is the common model of Part 4? The owner records this as "an open scientific decision" (#914 comment 6877871344, condition 4). In particular, is it the SM branch's lattice model (§1, items (vii) and (ix)–(xiii)), a completion of it (Q5), or another model? The registry's DM class is scoped so that it does not depend on the answer.
14. **Pure Yang–Mills and QCD in Part 4.** The papers state that the rigorous mass-gap proof is not required by the framework (`papers/Substratum.md`:225; `papers/SM.md`:1448), while Part 4 lists gauge dynamics, confinement and nonperturbative effects among the obligations (#914 comments 6877871344 and 6877908458). Are the mass gap (B-QCD-6), confinement (B-QCD-5) and the hadron spectrum (B-QCD-8) derivation obligations of Part 4, or recorded scope limits?

## 13. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #914 comments 6875046763, 6875548603, 6877420015; #1169 comment 6876591512 | The target, Part 4 wording and owner answers the ledger serves and quotes (header, §L.A, §2.4, §3.3, §9, §12) | Provenance: owner records quoted for scope; no scientific claim rests on them |
| #914 comments 6877871344 and 6877908458 | The levels, evidence classes, Part 4 entries, Level C items and QCD group that structure §L (header, §L, Q13, Q14) | Provenance: owner records quoted for scope; no scientific claim rests on them |
| #914 comment 6877803663, #1060 (question 3, BELL-QSET) and the owner decision quoted in §3.4 | The planning obligation named in §L.A, §3.3–§3.4 and Q7 | Provenance: planning records (§A.45 rule 1) |
| #868, #1063, #1143, #873, #1169, #1211, #1236 | Named as accountable or related Issues (#1063 in B-SM-GAUGE-5, B-QCD-3 and B-QCD-6) | Provenance: planning records |
| PR #1003 (closed) | Named in §L.B as provenance for the Yang–Mills question | Provenance only |
| PR #1292 at `7971631f` | Where r2 and its review are preserved (header) | Provenance |
| #1291 | Where BELL-QSET's scope was first drafted (§3.4) | Provenance only; closed as a duplicate of #1060 |
| PR #1173 and PR #1265 review comments, linked from the `oi-qm-ext-1`, OA and W1-1 records | Review provenance of records cited in §1, §2.1, §4.3, §9 and §10 | Provenance; the records and their proofs are on `main` and are cited at their own stated scope |
| PR #1289 and the drafts it carries | Not cited as support | Not used |

Every scientific status in the ledger cites a file on `main` at `dfeec843`.
