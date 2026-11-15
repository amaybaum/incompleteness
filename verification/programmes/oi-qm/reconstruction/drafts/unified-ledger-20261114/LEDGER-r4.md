# Unified derivation ledger, r4: levels A, B and C, findings and dependency map

**UNREVIEWED.** r4 applies two reviewed inputs: the independent review of r3 (`REVIEW-r3.md`,
verdict ACCEPT WITH CHANGES), and the confirmed findings of the coverage audit
(`COVERAGE-AUDIT-r3.md`, as confirmed by `REVIEW-AUDIT-r1.md`, `REVIEW-AUDIT-r2.md` and
`REVIEW-AUDIT-r3.md`). The disposition of each item is in `RESPONSE-r3.md`. r3 and its review are
left unchanged. r4 itself has not been reviewed. A complete ledger is not a complete theory: an
entry records the evidential status of a claim, and inclusion implies no derivation. The ledger
records status; it does not rank branches or obligations, and no ordering of rows or findings
expresses a priority.

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
- Guidance for r4: #914 comment 6878781541 (`amaybaum`, 2026-11-14; recorded at 2026-11-14T14:26:48Z),
  quoted verbatim: "Ledger r4 should incorporate confirmed findings and retain unresolved ones
  explicitly. The subsequent queue proposal should distinguish manuscript corrections, missing ledger
  coverage, and scientific research obligations—they require different work and authorization." and
  "The audit does not yet justify promoting QCD or another downstream branch ahead of the shared
  foundational gaps." The same record asks that each confirmed finding have "paired source passages
  and the supporting proof's actual scope", and that direct contradictions be separated "from
  differences in assumptions, scope or manuscript revision". That record "changes no priority, status
  or authorization".

Paper-only record under these authorizations, serving the target recorded in #914 comments
6875046763, 6875548603 and 6877420015 and #1169 comment 6876591512. Reading, analysis and writing
only. The coverage audit of condition 6 was performed separately (`COVERAGE-AUDIT-r3.md`); r4
incorporates only the findings its reviews confirm, and records them in §F and §U. This record adopts no premise,
extension E or sector condition C, changes no scientific status, and proposes no tier, readiness,
authorization or status change. Statuses below are those the cited sources give; where this record
says "conflicting", "consistent" or "undetermined", the reason and the source are stated. Issue
numbers name planning records (AGENTS.md §A.45 rule 1); naming or assigning an Issue discharges no
scientific obligation.

**Base.** All `papers/`, `book/` and `verification/` content was read at `c3b5f37a`; current `main`
(`dfeec843`, unchanged when r4 was written) differs from it only in `AGENTS.md` (§A.46: the opening
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
- **DM**, derivation from a common model. No common model is adopted (condition 4; Q13), and this
  record does not treat the SM branch's lattice model as the common model. DM is therefore used
  only for a result that holds for every model of the bare finite class (finite S, bijection φ,
  partition V, `papers/Main.md`:42 and ledger items (ii)–(iii) at :724). It holds in a common model
  only if that model is a member of the bare finite class. The recorded target excludes one fixed
  finite total carrier (#914 comment 6875046763), so whether each DM result transfers to an admitted
  carrier is open (Q5, Q13). DM marks the scope of the result; the bare-class inputs remain posited
  (§1).
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

**Identifiers.** Registry entries are identified as A-<name>; B-<branch>[-<group>]-n, with QCD as
the branch-level group B-QCD and with B-SUB and B-STR for results stated in Substratum and
Structure; and C-<group>[-n]. Aggregate rows carry sub-identifiers keyed to their source rows:
C-PRED-1/<row> for appendix-a rows 1–23 and N1–N7, C-PRED-4/<row> for G2–G13, and B-SM-FLAV-5/<row>
for the rows of SM's table at `papers/SM.md`:1269–1316 (for example C-PRED-1/12 for appendix-a row
12). Findings carry the identifiers of the series that recorded them: D (this ledger), F and K (the
coverage audit), J (§9 conflicts) and M (§10 mechanisms). An identifier is not an ordinal: it is not
renumbered and is not reused. Rows added in r4 have identifiers not used before.

**Work kinds (#914 comment 6878781541).** Every finding carries one or more, kept in separate
columns of §F:
- **MC**, manuscript-correction candidate. The passage is unchanged in the manuscript; this record
  makes and authorizes no correction, which belongs to a separate §A.25 correction unit.
- **LC**, missing ledger coverage: a row added or corrected here, or still to be added.
- **RO**, scientific research obligation: an open derivation, computation or test.

**Row provenance.** A row marked "(audit)" is the coverage audit's proposal as its reviews accepted
it. A row marked "(r4)" was added by r4 for a confirmed uncovered entry for which the audit proposed
no row, and its class is r4's reading of the cited source, not yet reviewed.

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
| B-QM-5 | Substratum plus one continuously tunable state-mixing operation gives operational QM, and conversely (converse witnessed by the full implementation class `fullClass`) | CD[added operation, posited as an "empirical controllability resource"] | K | `papers/Main.md`:588; `papers/GR.md`:256; `verification/lean-mathlib/OIBridge/StructuralClosure.lean`:419–429 |
| B-QM-6 | OI⁺ ⟺ exact finite endomorphic operational QM, each added principle independent | CD[OI⁺ principles, posited] | K | `papers/Main.md`:584–588 |
| B-QM-7 | One finite reversible realization reproduces a bounded quantum envelope to accuracy ε | DM | P, with probe checks | `papers/Main.md`:596–598 |
| B-QM-8 | No fixed finite realization is exactly operationally equivalent to a qubit's full theory | DM, NEG (under the factorization interface) | P for the factorization half; unboundedness imported from [55] | `papers/Main.md`:558 |
| B-QM-9 | The quasilocal completion is unique given its stages and dynamics; no state or representation is selected | CD[stages and dynamics given]; a uniqueness, not an equivalence (§A.34) | K | `papers/Main.md`:588 |
| B-QM-10 | Representability plus coherence does not select the relating unitary evolution | DM, NEG | P | `papers/Main.md`:20 |
| B-QM-11 | The Born exponent is not selected by the equivalence | UO (frontier item) | P | `papers/Main.md`:18, 554 |
| B-QM-12 | Every operation the present interface sources preserves nonnegative entries | DM, NEG | K (kernel-only) | `verification/programmes/oi-qm/PROGRAMME.md`:40, 80–84 |
| B-QM-13 | Affine-class and G_SM prepare–measure fragments are simplex-embeddable under named observer hypotheses; under one affine φ a stored setting acts on a carrier only by translation (OA-1 Gap 2) | CD[(H1), H-AR, (H3), (H4), (SP), (xiv); for G_SM Theorem S's conditions; OA-1 Gap 2 within the gauge-derived affine class], NEG within those hypotheses | RR | OA-1 STATUS:48–51; OA-2 STATUS:62–64; OA-3 STATUS:55–58 (§2.1) |
| B-QM-14 | The first state/readout bridge of candidate E-AR fails on any one fixed finite-dimensional quantum carrier | CD[E-AR], NEG (candidate-scoped) | P (hand proof) | `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md`:11–19 |
| B-QM-15 | Kernel-only reductions: necessary coherent continuum; real pair flow supplies the datum; fixed gate gives dense, not exact, QM | CD[stated datum, flow or gate as input] | K (kernel-only) | census families (§2.4) |
| B-QM-16 | On one fixed finite reversible representative the rooted visible process is indivisible somewhere in its recurrence cycle whenever some rooted map is not a permutation | DM given A1 | P | `papers/Main.md`:18 |
| B-QM-17 (audit) | Necessity of C2 and C3 | CD[the coupling-step model of the physical-memory theorem] for the persistence form; CD[that model; (EM)] for the timescale form; DM for m ≥ 2^{I*} (data processing for any bijective realization) | P | `papers/Main.md`:76, 159–169, 443–476, 498–512, 736–737 |
| B-QM-18 (audit) | The C1 witness is generic among bijections: the fraction failing C1 decays exponentially in n_H | DM | P (exact counting) | `papers/Main.md`:147–151 |
| B-QM-19 (audit) | Hamiltonian reconstruction from transition data; orientation selection | CD[(G1)–(G4); H-BG]; NEG for orientation selection | P | `papers/Main.md`:226–260, 716; `papers/GR.md`:166–210, 292–296 |
| B-QM-20 (audit) | Separability threshold; CP-indivisibility; approximate unitarity | CD[the displayed nearest-neighbour update over 𝔽₂] for the threshold; CD[the permutation-dilation family] for CP-indivisibility | P | `papers/Main.md`:292–340, 734, 778 |
| B-QM-21 (audit) | Intervention dilation, and three negatives: no uniform finite realization; no horizon-independent intervened representation at fixed d; no exact all-time realization | DM, NEG | P | `papers/Main.md`:478–496, 556, 638, 682 |
| B-QM-22 (audit) | Passive observation is complete iff commutative; non-discriminating | DM, NEG as a scope limit | P | `papers/Main.md`:590–592 |
| B-QM-23 (audit) | Canonical predictive quotient; Props 24.3–24.5 | DM (any finite permutation with a passive readout) | P | `papers/Main.md`:620–622; `papers/Substratum.md`:278–284, 302–361 |
| B-QM-24 (audit) | Barandes ≤ n³ compression; ancilla dilation | CD[translation hypothesis (T); the imported external theorem] | P | `papers/Main.md`:206–216, 352–356, 526–534 |
| B-QM-25 (audit) | Partition-relativity lemma | CD[Lemma 3's selected measure; prior as a third datum] | P | `papers/Main.md`:84–90 |
| B-QM-26 (audit) | Rest-frame selection by a horizon partition | CD[horizon partition selects n; T fixes the foliation] | P | `papers/Main.md`:660–674 |
| B-QM-27 (audit) | P-indivisibility carries over to a finite representative of the constraint surface | CD[finite φ-invariant representative of the constraint surface] | P | `papers/GR.md`:587 |
| B-QM-28 | At a fixed finite carrier, reversible trace-preserving emergent operations form a finite group, for every rule (OA-2 Theorem C; split from B-QM-13) | DM (scope stated at source: every rule, at a fixed finite carrier) | RR | OA-2 STATUS:56–57 |

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
| B-BELL-9 (audit) | Candidate Bell realization by cosmological-boundary modes | PE | BK | `book/ch18-beyond.md`:104 |

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
| B-GR-10 (audit) | Universality theorem for the partition-geometry results (the source labels part (a) "Unconditional") | CD[S1–S4]; for (b) CD[H-count, H-slope, H-frame, H-Hawking, local boost structure] | P | `papers/GR.md`:609–679 (part (a) at :615) |
| B-GR-11 (audit) | Locality of the local emergent QFT | CD[H-local-lift] | P | `papers/GR.md`:326–336 |
| B-GR-12 (r4) | With K = 2d link components, one mode per boundary cell is consistent, the consistency stated as "forced rather than assumed" | CD[H-link] | P | `papers/GR.md`:104 |

**B-SM (detail §5).** General entries, then the owner's subquestions as groups.

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-1 | Six signed links decompose as T₁(3) ⊕ E(2) ⊕ A₁(1) (Theorem 7) | CD[cubic lattice, ledger (x)] | K | `papers/SM.md`:374 |
| B-SM-2 | Identification of the link space with the physical carrier | CD[H-link single-copy, H-cust, H-blind; open] | — | `papers/SM.md`:12, 26, 32, 374 |
| B-SM-3 | Gauge group from the bicommutant; reduction to SU(3)×SU(2)×U(1) | CD[H-link (single-copy), H-cust; amplitude-scale gauge invariance; A6; specified charged matter action; anomaly cancellation]; the cubic-lattice commitment is EF (B-SM-4) | P | `papers/SM.md`:374; `papers/Substratum.md`:163 |
| B-SM-4 | Simple cubic is the one Bravais lattice compatible with the observed gauge group (Theorem 7b) | EF (selection by the observed group; "the same fact stated in two directions") | P | `papers/SM.md`:390, 1424 |
| B-SM-5 | d = 3 | EF (filters E5–E7, self-consistency strength; E7 inherits H-count) | P | `papers/SM.md`:30, 1424 |
| B-SM-6 | 1 ⊕ 3 tastes (Theorem 8); three generations | CD[cubic lattice, ledger (x)] for the decomposition; CD[H-spin′] for generations; NEG for the free-kernel and 4D-staggered routes | K (decomposition); N (routes) | `papers/SM.md`:448, 543, 1320 |
| B-SM-7 | Weak chirality | UO (H-χ′ open); NEG: the minimal embedding is vector-like | N (certified) | `papers/SM.md`:543, 1320 |
| B-SM-8 | Hypercharges unique given family pattern and chirality, apart from Y_Q = 0 (Theorem 15) | CD[family pattern, chirality] | XA | `papers/SM.md`:589 |
| B-SM-9 | The observer-level map φ → L_obs → Δ_g | UO ("not proved anywhere in this framework") | — | `papers/SM.md`:232 |
| B-SM-10 | Exact chiral symmetry ⟺ vanishing onsite terms (Theorem 3) | CD[the stated opposite-parity hopping family; the bridge to center dependence is separate] | K (both directions) | `papers/SM.md`:302–308 |
| B-SM-11 | [g] = (3 − d)/2, dimensionless iff d = 3 (Theorem 16) | CD[the Yang–Mills action form] | K | `papers/SM.md`:603–607 |
| B-SM-12 | The Higgs is the unique renormalizable unitarity-preserving mass mechanism; H = (1, 2, +½) | CD[chiral symmetry and the center-independent gauge sector] | P (standard QFT argument) | `papers/SM.md`:611 |
| B-SM-13 (audit) | Theorem 1a and Cor 1a; Cor 1b and Theorem 1 | CD[cubic reference lattice; finite equivariant projection]; for Cor 1b and Theorem 1 also CD[an observer-level center-free kernel] | P | `papers/SM.md`:12, 26, 32, 218, 242–282 |
| B-SM-14 (audit) | Wave-equation form lemma | CD[center independence, E4, A5, nearest-neighbour premise] | P | `papers/SM.md`:224–232; `papers/Substratum.md`:48, 159 |
| B-SM-15 (audit) | Theorem 22 | CD[wave-equation or energy-conserving dynamics on a connected bounded-degree graph]; C2 and C4 as hypotheses | P | `papers/SM.md`:1374–1388 |
| B-SM-16 (audit) | Appendix A spectral structure of the ring evolution (period formula, Jordan–Chevalley decomposition) | CD[A5 linear rule on the ring lattice; prime q, gcd(L, q) = 1] | P | `papers/SM.md`:1596–1654 |
| B-SM-17 (r4) | All five irreps of O are "accounted for … either by identified physical role or by derived absence" | CD[cubic lattice; the physical roles assigned under H-link and Theorem 11's input] | P | `papers/SM.md`:418–426 |

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
| B-SM-FLAV-1 | Structural form of the flavour pattern: Cabibbo λ from Brillouin geometry (its identification a "hypothesis, not a derivation"), Wolfenstein hierarchy and A, Koide target A² = C₂(T₁) | CD (Layer 1, one named open link each, at source); the Koide normalization is selected by match (B-SM-FLAV-9, EF) | P | `papers/SM.md`:859–867, 871, 881, 911; `book/ch19-open-problems.md`:154–156, 162 |
| B-SM-FLAV-2 | Koide amplitude from non-perturbative dynamics (perturbative taste-breaking gives A² ≈ 0.34 against 2) | UO; NEG for the perturbative route | N | `book/ch19-open-problems.md`:154 |
| B-SM-FLAV-3 | m_b/m_τ = 4.28/Z_S(λg₀²) | CD[measure identification, open, `papers/SM.md`:809]; EF for the matching coefficient K = 1/2 ("empirical fitting on a moderately-restricted set", SM:1215); Layer 2(a) verification residual; the analytical K is unresolved (U-7) | N (Monte Carlo with the standard Haar measure, `papers/SM.md`:813) | `papers/SM.md`:1130–1160, 1172, 1196, 1215–1219, 1229, 1257; `book/appendix-a-prediction-status.md`:85 |
| B-SM-FLAV-4 | m_s, m_c, CP phases | UO (m_s, m_c); EF (CP phases, solution-specific inputs) | — | `papers/SM.md`:1322; `papers/Substratum.md`:415 |
| B-SM-FLAV-5 | The 22 tabulated observables (2 S, 5 C, the rest L/M/R/P/E); sub-rows B-SM-FLAV-5/<row> | per row, with the S/C/L/M/R/P/E labels mapped: S → CD[cubic commitment, B-SM-4 (EF)], not DM; C, L, M → CD; R, E, P → EF | per row | `papers/SM.md`:1269–1316; C-PRED-1 |
| B-SM-FLAV-6 (audit) | Forward PMNS commitments (sum rule, θ₁₂, θ₂₃, θ₁₃) | CD[Cond 2] for the sum rule; CD[Cond 2; b₂₃ = 1] for θ₁₂ and θ₂₃ individually; CD[Cabibbo identification] for θ₁₃. Tests: the 7/6 sum rule, the octant ("A lower-octant determination excludes the prediction", SM:1112), θ₁₃ tightening | P | `papers/SM.md`:1026, 1048, 1056, 1066–1068, 1112, 1290–1291, 1353, 1360 |
| B-SM-FLAV-7 (audit) | y_t(M_Pl) = 1 gives m_t ≈ 207 GeV, a 20% excess; the weak-scale m_t = v/√2 is a retrodiction whose fixed-point mechanism is open | CD[unit compositeness normalization], NEG | P | `papers/SM.md`:14, 1006–1008 |
| B-SM-FLAV-8 (audit) | The six-observable Casimir table as "strong evidence for the underlying C₂/d identity" | PE (the claim that one identity explains six retrodicted values); the values keep their own classes; the 1/d normalization is selected by match (B-SM-FLAV-9) | P | `papers/SM.md`:1324–1346, 1349 |
| B-SM-FLAV-9 (audit) | Koide normalization and the reactor-angle route | EF for the selection by match ("Only 2/9 matches"); UO for the 1/d derivation | P | `papers/SM.md`:936, 940, 944–952, 1034, 1036 |
| B-SM-FLAV-10 (audit) | Routes to Cond 2 tried: the natural-form Yukawa gives b₁₂ : b₁₃ : b₂₃ = m_τ/m_μ : 1 : 1; first-order-squared effects excluded by spectrum dominance; the geometric second-order route excluded by monomial orthogonality (ρ "exactly zero") | NEG, scoped to the hop model with its declared inputs and the strict second-order extraction; UO for Cond 2 itself ("a stated condition") and for the recorded, unpursued O(λ³) route | P | `papers/SM.md`:1026, 1076, 1084, 1088–1094, 1108 |

*SM-NU, neutrinos.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-NU-1 | Majorana neutrinos and large PMNS mixing (from representation theory) | CD[the branch where the singlet taste hosts the Higgs (Theorem 11 taken as input) and no gauge-singlet fermion is present; the mechanism otherwise open] | P | `papers/SM.md`:1452–1462 |
| B-SM-NU-2 | Normal ordering and a hierarchical spectrum; Σm_ν near the oscillation minimum | PE (genericity heuristics, on the same branch); GR:410 calls these "OI predictions" and couples them to the running vacuum without a derivation (F-7) | P | `papers/SM.md`:1456–1464; `book/ch19-open-problems.md`:158; `papers/GR.md`:410 |
| B-SM-NU-3 | Absolute scale, Δm² ratio, δ_CP | EF (solution-specific) | — | `papers/SM.md`:1468 |

*SM-BARY, baryogenesis.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-BARY-1 | Baryon number is exactly conserved by the substratum dynamics | CD[bilinear coupling structure of the lattice wave equation] | P | `papers/SM.md`:1486–1490 |
| B-SM-BARY-2 | η_B | EF (downstream of the CP phases taken as solution-specific inputs, `book/ch19-open-problems.md`:184–188); UO in `papers/SM.md`:1526 ("open work"); see D11 | — | `book/ch19-open-problems.md`:178, 184–188; `papers/SM.md`:1526 |
| B-SM-BARY-3 | Weinberg-operator leptogenesis gives η_B ~ 4×10⁻¹¹, about 15× below observation | NEG | BK | `book/ch19-open-problems.md`:180 |
| B-SM-BARY-4 | Substratum-level instanton-like B-violation | NEG (retracted: the substratum has no Euclidean action) | BK | `book/ch19-open-problems.md`:182 |

*SM-GAUGE, gauge dynamics and confinement.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-GAUGE-1 | Induced coupling 1/α₀ = 23.25 | CD[single-copy H-link (N_f = 6), T(R) = ½]; for hypercharge also H-observer-bundle, H-Y-vertex | P (one-loop computation) | `papers/SM.md`:793 |
| B-SM-GAUGE-2 | Couplings at M_Z | EF (δ₀ fitted to the U(1) row; A, B matched to SU(2), SU(3)); A·B inconclusive; non-unification structural | P; N | `papers/SM.md`:797, 817 |
| B-SM-GAUGE-3 | The Haar-measure induced theory confines, against the deconfined phase the matching needs | NEG; whether the nonperturbative phase affects the coupling predictions is unresolved (U-3) | N | `papers/SM.md`:801 |
| B-SM-GAUGE-4 | The framework's gauge measure is a near-identity pushforward | PE (stated as a conjecture about the correct map); NEG: the natural polar candidate gives a Haar pushforward | N | `papers/SM.md`:803, 809, 811 |
| B-SM-GAUGE-5 | Local gauge dynamics and action selection (same-update source, measure, observables, action) | UO | — | No fundamental gauge action (`papers/SM.md`:827); the frozen roadmap names "a rigorous derivation or classification of local gauge dynamics" as the first milestone of a "conditional future programme" (`verification/ROADMAP.md`:1525–1536); planning record #1063 |

*SM-NP, nonperturbative effects.*

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SM-NP-1 | Z_S, the matching scale and the chiral condensate from dynamical-fermion Monte Carlo | XC (standard Haar measure); agreement with the framework's induced measure open | N | `papers/SM.md`:813, 1144 |
| B-SM-NP-2 | Archived code for §6.5 and §7.5 no longer extant; archived values not reproduced; Z_S universality violated (+2.6% ± 0.15%) for the directly sampled measure at the archived point | NEG | N | `papers/SM.md`:805 |
| B-SM-NP-3 | Non-perturbative B + L violation through emergent sphaleron physics, with no substratum channel | PE (the substratum-emergent operator distinction; "the correct picture" in the book) | P | `papers/SM.md`:1496–1506; `book/ch19-open-problems.md`:182 |

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
| B-QCD-6 | Mass gap (pure Yang–Mills) | UO. The sources state that the rigorous mass-gap proof is "not required by the OI framework" and "does not affect any prediction"; whether the nonperturbative phase affects the coupling predictions is unresolved (U-3) | — | `papers/Substratum.md`:225; `papers/SM.md`:801, 1448; #1063 |
| B-QCD-7 | Chiral symmetry breaking | XC (staggered Monte Carlo with the standard Haar measure shows spontaneous breaking, Σ ≈ 0.20); relation to the framework's measure open | N | `papers/SM.md`:813, 1144 |
| B-QCD-8 | Hadron spectrum (full QCD) | UO; no manuscript derivation found | — | searched `papers/` for "hadron", "pion", "proton mass": only `papers/GR.md`:581 (proton mass as QCD binding energy, in the CC argument) |
| B-QCD-9 | Strong CP | see B-SM-CP-1 to B-SM-CP-3 | — | cross-reference |
| B-QCD-10 | Nonperturbative QCD | see B-SM-NP-1 to B-SM-NP-3 and B-SM-FLAV-3 | — | cross-reference |
| B-QCD-11 | Nuclear consequences | UO; the book asserts a derivation without support (D8) | BK | `book/ch10-chemistry.md`:86–88; D8 |

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
| B-COS-3 | ~95% dark budget | CD[Lemmas 1–3, C1–C4, Jacobson's Clausius relation, H-count via T_cl, geometry-first ordering] (D5); partly definitional, 1 − Ω_B by construction | P | `papers/GR.md`:418–452 |
| B-COS-4 | a₀ = cH/6; BTFR | CD[H-count, H-slope, H-frame, H-Hawking]; the 1/6 factor imported | P | `papers/GR.md`:466–486 |
| B-COS-5 | MOND-like core to CDM-like growth crossover; microscopic relaxation kernel | UO ("the same uncomputed kernel"); an effective epoch-local relaxation law is posited separately (C-PRED-13, PE) | — | `papers/GR.md`:524–532 |
| B-COS-6 (audit) | Interpolation constraints on the MOND-like regime | PE; the steepness is bijection-specific (EF-type) | P | `papers/GR.md`:488–504 |

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
| B-BH-8 (audit) | Theorems A.5 and A.7 | CD[frozen deep sector; D initially a configuration] | P | `papers/GR.md`:753–767, 785–795 |

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
| B-P4-QCB-1 | The boundary is drawn in the memory currency by C1–C4; representability is universal | DM for the representability and memory results (B-QM-1, B-QM-2); PE for identifying the quantum–classical boundary with the C1–C4 memory sector ("the framework's identification") | K, P | `book/ch18-beyond.md`:64, 72; `papers/Main.md`:97 |
| B-P4-QCB-2 | Restricted quantum-statistical regime (partial distinguishability revival at marginal hidden capacity) | PE (mechanism proposal; conjecture on where it occurs) | BK | `book/ch18-beyond.md`:74–88 |
| B-P4-QCB-3 | Coherence as a bulk quantity and decoherence as an area quantity | PE ("an interpretation of the one-step result") | P | `papers/Main.md`:322 |
| B-P4-QCB-4 | Gravitational decoherence and gravitationally mediated entanglement | UO (selection among completions (a)–(c) open) | — | `papers/GR.md`:350 |

**B-SUB (results stated in Substratum).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-SUB-1 (audit) | Theorem 23, layered local reconstruction; the displayed "bidirectional correspondence" (E1–E7) + (A1–A6) ⟷ [(S, φ)]_loc/𝒢_sub | CD[E1–E7, M1-T, A1–A6, mixing hypothesis, nearest-neighbour premise, H-link, H-cust, H-spin′, H-χ′, H-slope] for the data → class direction (a uniqueness and reconstruction statement, §A.34); Bell-inclusive existence CD[H-Bell]; Bell-inclusive uniqueness UO; the class → data direction UO (no separate witness) | P | `papers/Substratum.md`:147–173, 189–203, 231–235 |
| B-SUB-2 (audit) | Theorem 24 with Prop 24.2, Structure Prop 9.5 and Cor 9.6, and GR's deep-sector corollary | DM for (i) and (iii) at a fixed finite interface; CD[alphabet-size hypothesis] for (ii); completeness UO; CD[H-BD] for GR part (b) | P | `papers/Substratum.md`:247–300, 429; `papers/Structure.md`:620–655; `papers/GR.md`:112–138 |
| B-SUB-3 (audit) | QM and GR as two projections of one object; the unification problem a category error | PE, conditional on G3 | P | `papers/Substratum.md`:14, 22–26, 371–397, 417–423, 459, 548–550 |

**B-STR (results stated in Structure).**

| ID | Claim | Class | Support | Source |
|---|---|---|---|---|
| B-STR-1 (audit) | Matrix models (BFSS, IKKT) fail A2 and A5 in their standard formulation | CD[BFSS and IKKT in their standard formulation], NEG | P | `papers/Structure.md`:13, 33, 256–353, 359–389, 514 |
| B-STR-2 (audit) | LQG, causal sets and asymptotic safety fail A2 | CD[the formulations cited], NEG | P | `papers/Structure.md`:1028–1042 |
| B-STR-3 (audit) | Props 9.7a, 9.7b and Cor 9.8 | DM (general operator theory) | P | `papers/Structure.md`:656–687 |
| B-STR-4 (r4) | The OI-string universality class; its protocol stated and not executed | UO | — | `papers/Structure.md`:829–862, 978–1062 |

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
| C-TOPO | Cosmic topology | UO (scope limit: silent on global topology; compatible with, not predicting, compact topologies; the non-orientability–chirality question open) | `book/ch18-beyond.md`:228–262 |
| C-CONJ-1 | Consciousness: observation as a necessary but not sufficient condition | PE ("offered as a conjecture"; Direction 1 a conjecture, not a theorem) | `book/ch18-beyond.md`:6, 268–274 |
| C-CONJ-2 | Biological candidates for the restricted regime (protein conformational dynamics, single-enzyme kinetics) | PE (conjecture) | `book/ch18-beyond.md`:80–88 |
| C-CONJ-3 | Condensed-matter relevance of the restricted regime | PE ("speculative and has not been developed") | `book/ch19-open-problems.md`:356 |
| C-CONJ-4 | Born rule as dynamical read-write equilibrium | PE (mechanism proposal; estimate heuristic) | `book/ch18-beyond.md`:34–36 |
| C-ANOM | Precision-sector anomalies (g − 2, R_K, m_W) | CD[(E/M_Pl)² suppression, `papers/SM.md`:1448]; scope limit: framework corrections O(10⁻³⁴) at 100 GeV, unobservable | `book/ch19-open-problems.md`:354 |
| C-PRED-1 | SM observables (appendix-a entries 1–23), neutrino entries N1–N7; sub-rows C-PRED-1/<row> | per row, with the labels mapped: S → CD[cubic commitment, B-SM-4 (EF)], not DM; C, L, M → CD; R, E, P → EF. Sub-rows with a confirmed finding: C-PRED-1/1 (F-35), /6 (F-25), /10–11, 15, 21 (F-26), /12–14, 19 and /N1–N3, N6 (F-8, F-27, F-28), /16 (F-30), /17 (F-29), /18 and /N4 (F-7), /22 (F-6), /N5 (F-36: PE, a heuristic, against the label C). JUNO sin²θ₁₂ a retrodiction now, a forward test at design-lifetime precision | `book/appendix-a-prediction-status.md`:70–92, 96, 98, 127–135, 211 |
| C-PRED-2 | Higgs mass from λ(M_Pl) = 0: m_H ≈ 129–132 GeV for m_t = 172–173 GeV, against 125.10 GeV | CD (B-SM-HIER-3); the λ(M_Pl) value consistent at 0.6σ, the m_H value 4–7 GeV above the observed value | `papers/SM.md`:1116–1118; appendix-a:91 |
| C-PRED-3 | No GUT proton decay (τ_p ~ 10⁴⁵–10⁴⁶ yr); detection falsifies | CD[no GUT; Planck-suppressed dimension-6 operators] | `papers/SM.md`:831, 839 |
| C-PRED-4 | Gravitational entries G2–G13; sub-rows C-PRED-4/<row> | per row, with the labels mapped as in C-PRED-1; C-PRED-4/G13 is C-LIV | `book/appendix-a-prediction-status.md`:106–113 |
| C-PRED-5 | DESI Y5: \|ν\| ≳ 10⁻³ refutes the magnitude; a high-confidence phantom crossing falsifies at structural level (appendix-a F6) | CD[§7.3 split], as the test of B-COS-1 and B-COS-2 | `papers/GR.md`:412, 591–593; `book/appendix-a-prediction-status.md`:179 |
| C-PRED-6 | Rotation curves: Milky Way decline and high-z curves in tension | NEG (stated tensions) | `papers/GR.md`:12, 536–545 |
| C-PRED-7 | GW250114 tests the area theorem, not the 1/4 coefficient; no echoes expected | CD[horizon conditions]; scope limit | `papers/GR.md`:12, 318, 597 |
| C-PRED-8 | Cosmic recurrence: period at most g(\|S\|), \|S\| not fixed (appendix-a F8) | DM given A1; logically falsifiable only | `book/appendix-a-prediction-status.md`:181 |
| C-PRED-9 | Memory-witness tests | UO: none decisive at present ("no memory-witness outcome therefore falsifies the ontology at present") | `papers/Main.md`:718–722 |
| C-PRED-10 (audit) | Tully–Fisher evolution tension | CD (the tested law, B-COS-4); NEG | `papers/GR.md`:512 |
| C-PRED-11 (audit) | Rich-cluster residual, "not closable by undetected cluster baryons" | CD (the tested law with the simple interpolation, B-COS-6); NEG | `papers/GR.md`:524 |
| C-PRED-12 (audit) | CMB match | CD[ρ_E ≈ Ω_CDM ρ_crit input; inflationary initial conditions]; EF for the input; the ΛCDM reproduction is XC | `papers/GR.md`:528–530 |
| C-PRED-13 (audit) | Bullet Cluster and the epoch-local relaxation equation dδ_E/dt = (δ_m − δ_E)/τ_relax | PE | `papers/GR.md`:524–532 |
| C-LIV (audit) | Lorentz violation (appendix-a G13): LIV 4σ/45; rotational sector | CD[observer-level branch; tree level]; UO for interacting and rotational-radiative protection | `papers/SM.md`:126–138, 1448; `papers/Substratum.md`:482–484; `papers/GR.md`:639–649; `book/appendix-a-prediction-status.md`:113 |
| C-LQ (audit) | Leptoquark sector and the M_X window; cross-charged boost-LV decoupling (appendix-a F13) | CD[H-link, H-cust, condensate]; M_X EF (solution-level) | `papers/SM.md`:130–134; `book/appendix-a-prediction-status.md`:196 |
| C-ERP (audit) | Weak ER=EPR form recovered; the strong form "predicted *false*" | PE; no test | `papers/Substratum.md`:237–243 |
| C-STR-1 (audit) | Observer admission: "Most arbitrary (S, φ) pairs do not admit observers" | PE; its coupling clause conflicts with B-QM-18 (F-2); its C2–C4 clauses unresolved (U-2); no test | `papers/Structure.md`:120–122, 516–576, 709–735 |
| C-STR-2 (audit) | Swampland consistency | PE | `papers/Structure.md`:391–435 |
| C-STR-3 (audit) | Horizon holography: an A/4 bound "under the conditions of the horizon calibration" | CD[H-slope and the §8.5(b) conditions]; a bound on "any horizon entropy" is not established beyond the calibration's conditions | `papers/Structure.md`:443–510 |
| C-STR-4 (audit) | Four-feature audit | PE | `papers/Structure.md`:1106–1261 |
| C-STR-5 (audit) | Limit 4: the bare thesis is not falsifiable | PE (the source's own assessment; a scope statement) | `papers/Structure.md`:1086–1096 |
| C-STR-6 (r4) | The algebra-channel pair "captures … gauge couplings at M_Z, Yukawa structure producing CKM/PMNS" | PE; the couplings are fitted and the Yukawas solution-specific (`papers/SM.md`:1396, 1440) | `papers/Structure.md`:761–825 |
| C-QG-1 (audit) | Non-renormalizability as an artifact of treating the lattice as a regulator | PE, conditional on G3 | `book/ch18-beyond.md`:144–152; `book/ch19-open-problems.md`:28–32 |
| C-EARLY-6 (r4) | History-dependent Born-rule corrections at late times | PE (within the mechanism proposal; their size "the framework does not quantify") | `book/ch18-beyond.md`:56–58 |
| C-BIO (audit) | Appendix-a B1–B14 (biology and medicine) and F1–F4 (quantum engineering), F9–F12 (biology and medicine) | PE (conjectural chapters: `book/ch16-medicine.md`:6, `book/ch17-bioinformatics.md`:6); sub-rows C-BIO/<row>. The S labels of B1, B2 and B6–B14 conflict with those notices (F-34); B3's label unchecked; F1 a "proposed model form; derivation unpackaged"; F2–F4 not quantified; F12 a retrodiction listed as a forward item | `book/appendix-a-prediction-status.md`:145–158, 170–173, 187–190 |

Appendix-a's 64 rows map as follows. Rows 1–23, N1–N7 and G2–G13 are C-PRED-1 and C-PRED-4 (G13 is
C-LIV). B1–B14 (:145–158; biology and medicine), F1–F4 (:170–173; quantum engineering) and F9–F12
(:187–190; biology and medicine) are C-BIO. F6, F7 and F8 (:179–181; cosmology) are C-PRED-5,
C-EARLY-2 and C-PRED-8. F13 (:196; boost-LV) is C-LQ. There is no row F5. The derivations behind
C-BIO, in book chapters 13–17, were not audited.

## 0. Branch table

Sections 0–12 give the branch detail that the registry entries summarize. They carry r3's text,
with REVIEW-r3's §1 change (N7) applied; the registry, §11, §F and §U carry the other r4 changes.

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
(vii)–(xiii), with the Stage-2 inputs and H-link, specify the lattice model the SM branch uses
(site factorization, linear second-order update, bounded degree, nearest-neighbour simple-cubic
reference graph, the link carrier; `papers/SM.md`:60). They are listed as the corpus's
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

D7–D11 are recorded as manuscript-correction candidates only; no manuscript is changed. The coverage
audit's findings are in §F and §U, which also give each D entry its kind of work.

- D7. `book/ch18-beyond.md`:256 describes "SU(2) as chiral and SU(3) as vector-like, derived from the staggered trace-out". Chirality is open under H-χ′, and the minimal embedding is certified vector-like (`papers/SM.md`:543, 1320; `book/ch19-open-problems.md`:328). FULL mirror: `book/The-Incompleteness-of-Observation-FULL.md`:5062.
- D8. `book/ch10-chemistry.md`:86–88 states that "SU(3) color confinement (Chapter 5 §5.4) produces bound hadrons" and that the nuclear-binding mechanism "is derived from the gauge structure of SU(3)". `book/ch05-gauge-structure.md` §5.4 (from :81) carries no confinement statement, and the papers carry no derivation of confinement for the framework's gauge measure (`papers/SM.md`:801–811; B-QCD-5). FULL mirror: `book/The-Incompleteness-of-Observation-FULL.md`:2894.
- D9. `book/ch19-open-problems.md`:88 states that the substratum lattice "eliminates the divergence and with it the cutoff sensitivity of m_H". `papers/SM.md`:613 and :1570 present that protection as "structurally identified", with "the theorem-level derivation" deferred. FULL mirror: `book/The-Incompleteness-of-Observation-FULL.md`:5235.
- D10. `book/ch10-chemistry.md`:78–80 calls the Sakharov ingredients "derived" and the possibility of baryogenesis "a theorem" from the three-generation structure and P-breaking. Three physical generations are conditional on H-spin′, chirality is open (`papers/SM.md`:1320), and the CP phases are solution-specific inputs (`papers/Substratum.md`:415; `book/ch19-open-problems.md`:184). Baryon number is conserved at the substratum (`papers/SM.md`:1486–1490); its violation is emergent (`papers/SM.md`:1496–1506). FULL mirror: `book/The-Incompleteness-of-Observation-FULL.md`:2886–2888.
- D11. `papers/SM.md`:1526 states the baryogenesis mechanism as open and the full quantitative prediction as "open work"; `book/ch19-open-problems.md`:184–188 classes η_B as solution-specific and not "an unmet derivation obligation".

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
11. **Manuscript-correction candidates.** Should any of D1, D2, D4, D5, D7–D11, or the candidates in §F's MC column, be scheduled as a separate correction unit under §A.25? This ledger authorizes none.
12. **Standard of independent physical justification.** What standard does Part 4 apply to named hypotheses that a source records as additional assumptions (for example W1, `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48, and H-count, H-slope and H-scramble, `papers/GR.md`:58, 74, 815)?
13. **Common model.** Which model is the common model of Part 4? The owner records this as "an open scientific decision" (#914 comment 6877871344, condition 4). In particular, is it the SM branch's lattice model (§1, items (vii) and (ix)–(xiii)), a completion of it (Q5), or another model? The registry's DM class is scoped so that it does not depend on the answer.
14. **Pure Yang–Mills and QCD in Part 4.** The papers state that the rigorous mass-gap proof is not required by the framework (`papers/Substratum.md`:225; `papers/SM.md`:1448), while Part 4 lists gauge dynamics, confinement and nonperturbative effects among the obligations (#914 comments 6877871344 and 6877908458). Are the mass gap (B-QCD-6), confinement (B-QCD-5) and the hadron spectrum (B-QCD-8) derivation obligations of Part 4, or recorded scope limits?

## F. Findings register and kinds of work

Every finding the ledger carries is listed once, with its kind of work in three separate columns
(#914 comment 6878781541). An MC entry names the passage that would need correcting; it is a
candidate only, and the passage is unchanged. An LC entry names the row added or corrected here, or
states that coverage is still missing. An RO entry names the open scientific question. "—" means
none. The F and K findings are the coverage audit's, as its reviews confirmed them; their passages,
proof scopes and conflict classes are in `COVERAGE-AUDIT-r3.md` §3 and §8, and the status column uses
the audit's terms. Unresolved findings are marked U-n and listed with their paired passages in §U.

**Conflict classes.** DC = direct contradiction; DA = difference in assumptions; DS = difference in
scope; MR = manuscript-revision difference; SO = single-source overstatement; COV = coverage, not a
conflict.

**F.1 Ledger findings (D series, §11).**

| ID | Finding | Class | Status | MC | LC | RO |
|---|---|---|---|---|---|---|
| D1 | ch19 §19.2 heading "Problems resolved" against its entries | DC (within the chapter) | classified; stands | `book/ch19-open-problems.md`:20 | — | — |
| D2 | H-Bell section cited as §3.3 and as §3.2 | citation | classified; stands | `papers/Main.md`:20; `papers/SM.md`:14, 60; `papers/Introduction.md`:145 | — | — |
| D3 | Five completion conditions cited at two sites | none (consistent) | no conflict | — | — | — |
| D4 | The (vii) condition on a graph that varies with the state is missing from the book and from the H-Bell definition; Theorem 23 assumes A5 | DA | classified; stands | the book chapters carrying the preparation-indexed route; `papers/Substratum.md`:131–133, 193 | — | Q2 (linearity); J-1 |
| D5 | The dark-sector corollary's stated premises omit those its proof uses | DA | classified; stands | `papers/GR.md`:418 | B-COS-3 (corrected) | — |
| D6 | No obligation to derive η_B, against Part 4's scope | scope (planning record against manuscript) | open owner question Q6 | `book/ch19-open-problems.md`:178, contingent on Q6 | — | — |
| D7 | Chirality called "derived" | DC | classified; stands | `book/ch18-beyond.md`:256; FULL:5062 | — | — |
| D8 | Confinement and nuclear binding called "derived", citing a section with no confinement statement | DC | classified; stands | `book/ch10-chemistry.md`:86–88; FULL:2894 | B-QCD-11 (corrected) | B-QCD-5 (confinement) |
| D9 | Cutoff sensitivity "eliminated" against a deferred derivation | DS | classified; stands | `book/ch19-open-problems.md`:88; FULL:5235 | — | B-SM-HIER-1 (the deferred derivation) |
| D10 | The possibility of baryogenesis called "a theorem" | DA | classified; stands | `book/ch10-chemistry.md`:78–80; FULL:2886–2888 | — | — |
| D11 | Baryogenesis "open work" in SM against "solution-specific" in ch19 | DA | classified; stands | `papers/SM.md`:1526 or `book/ch19-open-problems.md`:184–188 | B-SM-BARY-2 (corrected) | — |

**F.2 Coverage-audit register (F series).** F-10 is withdrawn and kept as withdrawn.

| ID | Finding | Class | Status | MC | LC | RO |
|---|---|---|---|---|---|---|
| F-1 | Structure has no ledger coverage | COV | unresolved (U-1) | — | B-STR-1 to B-STR-4, C-STR-1 to C-STR-6 added; T-6 still uncovered | — |
| F-2 | Observer genericity: "Most arbitrary (S, φ) pairs do not admit observers" | DC (coupling clause); unresolved (C2–C4 clauses) | coupling clause classified; stands. C2–C4 unresolved (U-2) | `papers/Structure.md`:733; `book/ch03-structural-realism.md`:26; FULL:891 | B-QM-18, C-STR-1 added | whether C2 and C4 fail for typical bijections |
| F-3 | Substratum Stage 2 states SM outputs without SM's conditions | DC (chirality, :165 against SM:543); DA (generations, Higgs) | classified; stands | `papers/Substratum.md`:151–152, 165, 169, 173, 201, 203 | B-SUB-1 added | — |
| F-4 | "No model-building choices" | DS | classified; stands | `papers/Substratum.md`:199 | — | — |
| F-5 | Prediction counts with an unexplained residue | DS | classified; stands | `papers/Substratum.md`:525 (state the mapping) | — | — |
| F-6 | λ(M_Pl) = 0 classed S | DA | classified; stands | `papers/SM.md`:1293; `book/appendix-a-prediction-status.md`:91 | C-PRED-1/22 | — |
| F-7 | Σm_ν called an "OI prediction" and coupled to the running vacuum | DA; SO (coupling sentence) | classified; stands | `papers/GR.md`:410 | B-SM-NU-2 (corrected) | — |
| F-8 | PMNS forward commitments "forced … no free parameter" | DA | classified; stands | `papers/SM.md`:1353, 1360 | B-SM-FLAV-6 added | — |
| F-9 | m_H comparison stated three ways | MR | classified; stands | `papers/SM.md`:1118, 1126, 1294 | — | — |
| F-10 | Lemma 1 status | DS | no conflict (withdrawn) | optional: `papers/GR.md`:90 looser than :585 | — | — |
| F-11 | C2 "Satisfied" at the horizon | DS | classified; stands | `papers/GR.md`:48 | §9 QM–Cosmology (already) | — |
| F-12 | GR summary-table preamble "no predictions are fit" | DS | classified; stands | `papers/GR.md`:536 | — | — |
| F-13 | "No particle dark matter" | DS | classified; stands | `papers/GR.md`:454; `book/ch19-open-problems.md`:46 | — | — |
| F-14 | Relaxation kernel uncomputed; an effective law posited | DS | classified; stands | — | B-COS-5 (corrected); C-PRED-13 added | the relaxation kernel |
| F-15 | Inflationary initial conditions used where inflation is "not addressed" | DA | classified; stands | `papers/GR.md`:530 (state it as an input) | C-PRED-12 added | — |
| F-16 | Displayed "bidirectional correspondence" with one witnessed direction (§A.34) | SO (directionality) | classified; stands | `papers/Substratum.md`:231–233 | B-SUB-1 added | — |
| F-17 | Gauge group "uniquely"; dark-sector level placement | DA (:703); DC (:179 against :191–192) | classified; stands | `papers/Structure.md`:179, 703 | — | — |
| F-18 | Emergent QFT parameters "derived" | DC | classified; stands | `papers/Structure.md`:417 | — | — |
| F-19 | Majorana neutrinos without the branch condition | DA | classified; stands | `papers/Structure.md`:403, 1317 | — | a 0νββ sensitivity target (SM-41) |
| F-20 | Scope of the matrix-model negative | DS | classified; stands | `papers/Structure.md`:13, 369 | B-STR-1 added | — |
| F-21 | Doublers "become … the physical generations" | DC | classified; stands | `papers/SM.md`:567 | — | — |
| F-22 | Mass gap "does not affect any prediction" | DS; unresolved part | unresolved (U-3) | `papers/SM.md`:1448; `papers/Substratum.md`:225 | B-QCD-6, B-SM-GAUGE-3 (corrected) | whether the nonperturbative phase affects the coupling predictions |
| F-23 | "Forced … no parameters fit"; "six masses from one input" | SO | classified; stands | `papers/SM.md`:14, 847, 989, 1588 | — | — |
| F-24 | GST "a corollary" and "an external empirical relation" | DC | classified; stands | `papers/SM.md`:863 or :887 | — | — |
| F-25 | Wolfenstein A identification asserted, class S | DA | classified; stands | `papers/SM.md`:1279 | B-SM-FLAV-1 (corrected); C-PRED-1/6 | — |
| F-26 | Koide normalization selected by match | DA | unresolved (U-4) | — | B-SM-FLAV-9 added | the 1/d amplitude derivation |
| F-27 | Reactor-angle route uses its own target | DA | unresolved (U-5) | `papers/SM.md`:1026, 1036 (state the load-bearing route) | B-SM-FLAV-9 added | — |
| F-28 | Normalization b₂₃ = 1 not listed as an open link | DA | unresolved (U-6) | SM footnote ᶠ; `book/appendix-a-prediction-status.md`:96 | B-SM-FLAV-6 added | a derivation of b₂₃ = 1 |
| F-29 | m_u/m_d data values | MR | classified; stands | `papers/SM.md`:981, 1289, 1335; `book/appendix-a-prediction-status.md`:86 | — | — |
| F-30 | Matching mass "derived" against "empirical fitting" | DS | unresolved (U-7) | `papers/SM.md`:1152, 1172 | B-SM-FLAV-3 (corrected) | the analytical K |
| F-31 | Anomaly cancellation "forces" three sectors | DC | classified; stands | `book/ch19-open-problems.md`:106 | — | — |
| F-32 | "Derives exactly one scalar doublet" | DC | classified; stands | `book/ch19-open-problems.md`:196 | — | — |
| F-33 | "Derives the total budget" | DC (within the chapter) | classified; stands | `book/ch19-open-problems.md`:118 | — | — |
| F-34 | Biology rows classed S against the chapters' conjectural status | DC | classified; stands | `book/appendix-a-prediction-status.md`:145–158 | C-BIO added | — |
| F-35 | Row 1, 1/α₀, classed S | DA | classified; stands | `book/appendix-a-prediction-status.md`:70 | C-PRED-1/1 | — |
| F-36 | N5 classed C against its own note | DC | classified; stands | `book/appendix-a-prediction-status.md`:131 | C-PRED-1/N5 | — |
| F-37 | Excluded routes to Cond 2 | COV (a negative result missing) | classified; stands. Whether any route derives Cond 2: unresolved (U-8) | — | B-SM-FLAV-10 added | the O(λ³) route, or exact diagonalization at physical λ |
| F-38 | The sum-rule match read as evidence that the mechanism is realized | SO | classified; stands | `papers/SM.md`:1092, 1100, 1110 | — | — |

**F.3 Single-source overstatements without a second passage (audit §3.2).**

| ID | Passage | Status | MC | LC | RO |
|---|---|---|---|---|---|
| M-33 | "quantitative predictions" | classified; stands | `papers/Main.md`:704 | — (see U-10) | — |
| S-1, S-2, S-17 | QM and GR "derived rather than fundamental"; "does establish"; "generates every concept" | classified; stands | `papers/Substratum.md`:389, 421, 459 | B-SUB-3 added | — |
| S-3 | "The dark sector is the gravitational effect of the unreadable storage" | classified; stands | `papers/Substratum.md`:46 | — | — |
| S-10 | Weak ER=EPR "as a structural consequence" | classified; stands | `papers/Substratum.md`:239 | C-ERP added | — |
| S-19 | Class A "structural theorems" | classified; stands | `papers/Substratum.md`:475–479 | — | — |
| G-2 | Count "unconditional" | classified; stands | `papers/GR.md`:12 | B-GR-1 (already) | — |
| G-30 | "(a) *Unconditional.*" | classified; stands | `papers/GR.md`:615 | B-GR-10 added | — |
| SM-36 | "strong evidence for the underlying C₂/d identity" | classified; stands | `papers/SM.md`:1339 | B-SM-FLAV-8 added | — |
| T-4 | A/4 bound on "any horizon entropy" | classified; stands | `papers/Structure.md`:453 | C-STR-3 added | — |
| T-9 | The pair "captures" couplings | classified; stands | `papers/Structure.md`:813 | C-STR-6 added | — |
| T-12 | "moderately favors the no-GUT universality class" | classified; stands | `papers/Structure.md`:970 | — | — |

**F.4 Book-control findings (audit §8, K series).** K-1 to K-4, K-10 and K-11 are F-31, F-32, F-13,
F-33, F-15 and F-2.

| ID | Finding | Status | MC | LC | RO |
|---|---|---|---|---|---|
| K-5 | "The framework derives the fundamental laws" | classified; stands | `book/ch19-open-problems.md`:356 | — | — |
| K-6 | Non-renormalizability "dissolution", conditional on G3 | coverage | — | C-QG-1 added | — |
| K-7 | Candidate Bell realization by boundary modes | coverage | — | B-BELL-9 added | — |
| K-8 | Late-time history-dependent Born corrections | coverage | — | C-EARLY-6 added | — |
| K-9 | Rotational radiative stability; a "direct computation" R ≈ ε with no record cited | unresolved (U-9) | — | coverage of the computation's record | the computation and its record |

**F.5 Joint-satisfiability conflicts (J series, §9) and shared mechanisms (M series, §10).** These
are scientific findings. None is a manuscript-correction candidate.

| ID | Finding | Status | MC | LC | RO |
|---|---|---|---|---|---|
| J-1 | Global A5 against the preparation-indexed Bell implementation (§9 Bell–SM) | known not to, as stated | — | — | Q2 (linearity) |
| J-2 | SM §3.1's evolving graph against global A5 (beneath §9) | known not to, as stated | — | — | Q2 |
| J-3 | Exact inclusion against A1 on one fixed finite carrier (QM–A1) | known not to, as stated | — | — | Q5 |
| J-4 | Exact inclusion against A.8's finite cycle averages on one fixed finite S (§9 QM–BH) | known not to, as stated | — | — | Q5 |
| M1–M9 | Shared missing mechanisms (§10) | open | — | — | each mechanism |

**Missing coverage still outstanding.** T-6 (Structure's level hierarchy and placements, and its
Born test; `papers/Structure.md`:98–198, 892–954) has no row. The audit proposed none, and r4 adds
none.

## U. Unresolved findings

These ten findings are retained unresolved. Each gives its paired source passages, what is open,
and its kind of work. None is resolved here. Adding a row that covers a finding's subject does not
resolve it.

| ID | Finding | Passage A | Passage B | Scope and what is open | Work |
|---|---|---|---|---|---|
| U-1 | F-1, Structure coverage | `papers/Structure.md`, entries T-1 to T-17 (`COVERAGE-AUDIT-r3.md` §4.5) | ledger r3, which cites Structure at no line | r4 adds rows for every uncovered Structure entry except T-6. Whether coverage is complete is for a re-audit | LC |
| U-2 | F-2, C2–C4 clauses | `papers/Structure.md`:733, "random permutations on finite sets typically lack the coupled-dynamics, non-equilibrium-phase, and high-capacity features" | `papers/Main.md`:147–151, which proves genericity of the C1 witness only | B's proof is exact counting over all bijections for a fixed product partition. The corpus proves neither that typical bijections fail C2–C4 nor that they satisfy them | MC (as F-2); RO |
| U-3 | F-22, nonperturbative phase | `papers/SM.md`:1448, "it does not affect any prediction of the OI framework"; `papers/Substratum.md`:225 | `papers/SM.md`:801, the deconfined phase "required for the perturbative matching to be valid"; :803–811 | A concerns the lattice's structural results; B the validity of the coupling matching. Whether the nonperturbative phase affects the coupling predictions is open | MC; RO |
| U-4 | F-26, Koide normalization | `papers/SM.md`:936, "Only 2/9 matches"; :940, "the unique match to observation" | `papers/SM.md`:944, "A first-principles derivation of the specific 1/d amplitude scaling … remains an open task"; :946–952 | The resolving computation is specified and not performed | LC (B-SM-FLAV-9); RO |
| U-5 | F-27, reactor-angle route | `papers/SM.md`:1036, the sin²θ₁₃ coefficient used to determine A₁ | `papers/SM.md`:1034, sin θ₁₃ = A²λ with α = √C₂/d, whose 1/d normalization is open (:944) | Which route is load-bearing for "independent of Condition 2" (:1026) is not stated | MC; LC |
| U-6 | F-28, b₂₃ = 1 | `papers/SM.md`:1048, "The natural-normalization choice b₂₃ = 1"; :1056 | SM footnote ᶠ and `book/appendix-a-prediction-status.md`:96, naming only Condition 2 as the open link | The normalization is not derived | MC; LC; RO |
| U-7 | F-30, matching coefficient K | `papers/SM.md`:1152, "The matching scale is derived"; :1172, "a representation-theoretic structural identity" | `papers/SM.md`:1160, 1196, 1215 ("empirical fitting on a moderately-restricted set"), 1219 | The form is argued; the coefficient comes from data selection and Monte Carlo with the standard measure. The analytical K is open | MC; LC; RO |
| U-8 | F-37, Cond 2 | `papers/SM.md`:1108, "The second-order route is thereby closed in the negative, and the recorded O(λ³) construction is what remains" | `papers/SM.md`:1076, Cond 2 at Layer 2(b), "the O(λ³) interference route recorded, not pursued" | The negative is scoped to the hop model and the strict second-order extraction. Whether any route derives Cond 2 is open | LC (B-SM-FLAV-10); RO |
| U-9 | K-9, rotational radiative stability | `book/ch19-open-problems.md`:244, "A direct computation of that width on the cubic lattice gives R ≈ ε" | no record cited at that line; the audit did not locate the computation | Whether a record of the computation exists, and what it shows | LC; RO |
| U-10 | Main's independence | `papers/Main.md`:76 (the C3 horizon numbers), :660–674 (rest-frame lemma taking a causal horizon as given), :20 (the "specific SM/GR branch" and the [Substratum §3.3] citation), :704 ("quantitative predictions") | the companion-paper content these passages draw on (`COVERAGE-AUDIT-r3.md`, observation after §4.5) | Whether each is an illustration, a stated input or a dependency, under the Code Review Rules' Main-independence rule, was recorded and not traced | MC or LC, depending on the trace |

The ledger records these findings and ranks none of them. Nothing in §F or §U places QCD or any
other downstream branch ahead of the shared foundational gaps (#914 comment 6878781541).

## 13. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #914 comments 6875046763, 6875548603, 6877420015; #1169 comment 6876591512 | The target, Part 4 wording and owner answers the ledger serves and quotes (header, §L.A, §2.4, §3.3, §9, §12) | Provenance: owner records quoted for scope; no scientific claim rests on them |
| #914 comments 6877871344 and 6877908458 | The levels, evidence classes, Part 4 entries, Level C items and QCD group that structure §L (header, §L, Q13, Q14) | Provenance: owner records quoted for scope; no scientific claim rests on them |
| #914 comment 6877803663, #1060 (question 3, BELL-QSET) and the owner decision quoted in §3.4 | The planning obligation named in §L.A, §3.3–§3.4 and Q7 | Provenance: planning records (§A.45 rule 1) |
| #868, #1063, #1143, #873, #1169, #1211, #1236 | Named as accountable or related Issues (#1063 in B-SM-GAUGE-5, B-QCD-3 and B-QCD-6) | Provenance: planning records |
| PR #1003 (closed) | Named in §L.B as provenance for the Yang–Mills question | Provenance only |
| PR #1292 at `7971631f`, and the audit drafts it carries (`edc50055`, `70748aad`, `964d9bd6`) | Where r2, its review and the coverage audit drafts are preserved (header) | Provenance |
| #914 comment 6878781541 | The guidance r4 applies (header, §F, §U) | Provenance: owner guidance quoted for scope; no scientific claim rests on it |
| `REVIEW-r3.md`, `COVERAGE-AUDIT-r3.md`, `REVIEW-AUDIT-r1.md` to `REVIEW-AUDIT-r3.md` (drafts, not on `main`) | The findings r4 applies (§L rows marked "(audit)", §F, §U) | Provenance: each finding r4 carries cites its manuscript lines on `main`, and every status rests on those lines |
| #1291 | Where BELL-QSET's scope was first drafted (§3.4) | Provenance only; closed as a duplicate of #1060 |
| PR #1173 and PR #1265 review comments, linked from the `oi-qm-ext-1`, OA and W1-1 records | Review provenance of records cited in §1, §2.1, §4.3, §9 and §10 | Provenance; the records and their proofs are on `main` and are cited at their own stated scope |
| PR #1289 and the drafts it carries | Not cited as support | Not used |

Every scientific status in the ledger cites a file on `main` at `dfeec843`.
