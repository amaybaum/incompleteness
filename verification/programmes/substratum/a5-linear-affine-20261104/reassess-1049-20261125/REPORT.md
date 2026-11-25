**Superseded; kept as research history.** This file is revision r1 of the #1049 report and is superseded. The authoritative revision is REPORT-r4.md in this directory, and its correction record is CHANGES-r4.md; the earlier corrections are recorded in CHANGES-r2.md (r1 to r2) and CHANGES-r3.md (r2 to r3). Below this notice the text of r1 is unchanged. It is kept as the research history, and its conclusions are not current results.

# #1049 research report: linear vs affine microscopic dynamics (paper-only, read-only)

## 0. Status, pin, sources

**Status.** I read sources and reasoned on paper only. I wrote nothing to git or GitHub, edited no manuscript, ran no computation and built no Lean. Nothing here changes a premise. A5 stays a posit (owner, #1049 c.6624263637). Every new step below is labelled [A] (exact algebra by hand in this report, unreviewed) or [W] (reasoning in this report, unreviewed).

**Pin.** `main` = `e2e2a623265187a28ebec604ab8bcc672742888f`. Manuscript line numbers below refer to that commit.

**Sources read**
- AGENTS.md at the pin: §A.19, A.21, A.22, A.29, A.31, A.42 item 8, A.46.
- #1049: body and all 17 comments. #1083: PR record and comments (merged as `9e0560d8`, reviewed head `0e7e412a`).
- Records on `main`:
  - `verification/programmes/substratum/a5-linear-affine-20261104/`:
    - `A5-LINEAR-AFFINE.md` ("A5-LA");
    - `A5-Q4-STAGE2D.md` ("Q4");
    - `q3-a6-offsets-20261108/ASSESSMENT.md` ("Q3"; merged as `45eea51d`, head `25384b13`).
  - `verification/programmes/hydrodynamics/round-h-d-a5-status-adjudication/result.md` ("H-D") and `round-h-f-a5-hc-decision/result.md`.
  - `verification/audits/foundations/posit-min-20261120/AUDIT.md` ("POSIT-MIN"; model review ACCEPT WITH NITS at `a4a1e5bb`).
  - `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` ("OA-1").
  - `verification/programmes/substratum/continuous-substates/` (README and the `native-*affine*` / `native-nonlinear-compensation` notes), for context only.
- Off `main`: branch `research/a5-reassessment-r5-1049-20261110` (draft PR #1226, unmerged), file `ASSESS-1049.md` ("r5"). It was accepted by a model review at `2d9bb8d1`; branch head `f1a8f1a5`.
- Lean modules in `verification/lean-mathlib/OIBridge/` (statements read, nothing built):
  - `FrozenSourcing.lean`: `obsTheory_nonnegBounded`, `permMatrix_preservesNonneg`, `sourcing_rule_independent`, `phase_ceiling_rule_independent`.
  - `SubstratumInterfaceAudit.lean`: `A5`, `obsTheory_eq_permTheory`, `obsTheory_rule_independent`.
  - `StructuralClosure.lean`: `substratumClass_not_drivesElementary`, `substratum_plus_control_qm`.
  - `SubstratumSource.lean`: `DrivesElementary`.
  - `SecondOrderLayer.lean`: `Rule`, a general `F : (ι → V) → (ι → V)` with no additivity.
- Manuscripts:
  - Main:736 (posit ledger, items (v), (vii), (xii), (xiii));
  - Main:424 (Bell branch);
  - SM:96, :240, :577, :587;
  - Substratum:100, :163, :220, :270–274.

**External sources.** None retrieved. Every literature statement is marked [background].

***

## 1. Assessment of the record

### 1.1 What is established, and at what level

None of the A5 records is established in the §A.46 item 1 sense. All are WIP / UNVERIFIED research records whose new steps carry model reviews only. The levels:

- **Kernel theorems [K]:**
  - The observer theory of any substratum is the permutation theory of its configuration space, whatever the rule (`obsTheory_eq_permTheory`, `obsTheory_rule_independent`). Both hold by `rfl`.
  - That theory preserves nonnegative entries (`obsTheory_nonnegBounded`). So it has no phases and no dense unitary control on `Fin 2`, for every `Rule`, additive or not (`phase_ceiling_rule_independent`).
  - Every permutation matrix preserves nonnegative entries (`permMatrix_preservesNonneg`, for any `σ`).
  - The monomial class fails `DrivesElementary`, which requires transition flows `flow (transition a b) t` for all real `t`, swaps and quarter phases. Any structurally closed extension that drives them gives exact finite quantum completeness (`substratum_plus_control_qm`).
  - `driveQ` is a continuous path of *-automorphisms for every `Rule`, with no additivity used (A5-LA C5).
  - No module of the OI → QM chain consumes `Substratum.A5`. Its consumers are closed at four modules (H-D `A5S-1b`, an enumeration over kernel objects).
- **Manuscript statements [P]:**
  - SM:240 gives the S1 witness: affine, reversible, translation-commuting, center-free, with no fixed point, so no time-independent relabelling makes it linear.
  - Substratum:272 and SM:96 state that affine relabelling covariance alone allows nonlinear rules.
  - Main:736 (vii) records A5 as "a further restriction beyond the affine condition", with no physical warrant stated.
- **Derivations in model-reviewed records [D] (A5-LA, Q4, Q3):**
  - **R1:** Φ^t = τ_{p(t)} ∘ L^t.
  - **R2:** an affine bijection is linearizable by a time-independent bijection iff it has a fixed point iff β ∈ Im(I − L).
  - **R3:** the obstruction is resonance with the zero modes of A − 2I.
  - **R4:** A5 is invariant under the uniform-shift gauge iff κ ≡ 2.
  - **R6 (Theorem 2.1):** linear and affine laws are equal for relational readouts 𝒜_W and 𝒜_C, for every preparation and at all times.
  - **R7 (Theorem 2.2, Corollary 2.3):** at Main's absolute interface they are equal up to a time-dependent outcome relabelling.
  - **R8:** the spectra agree on the W-invariant algebra and differ on the full algebra for S1.
  - **R9:** the kernel-consumer conclusions extend to uniform offsets.
  - **Q4:** outcome (iii) for O1–O4. It rests on the (A-lin) reading and holds given H-b, on the lift, for a uniform offset; O5 is not examined.
  - **Q3:** outcome (N), conditional on amplitude-scale gauge.
- **Reviewed research records [R]:**
  - OA-1 D5: under any affine rule a stored setting acts on a carrier only by translation, for every measure. It is one paper proof, re-derived twice at the same layer.
  - OA-1 D6: rule-derived and nonlinear configuration-level interfaces stay inside the kernel ceiling. This is [W] built on [K].
  - POSIT-MIN rows (vii) and T1/T4/K5.
- **Off `main`, accepted by model review only:** r5's P1 witnesses (non-affine rules covariant under every uniform affine map, d = 2 and 3) and its GA7-α recovery. Citing either as support in a landing would be support off `main`, a §A.42 item 8 gap.

### 1.2 Negative findings to preserve

- **R5:** among the selection principles N1–N11, none selects b = 0 with an independent justification. N8 does so only at odd q, and N9/E1 relocates the assumption rather than deriving it. This is a finite search, not an impossibility result.
- **Q3 (N):** none of E1–E3 is independently justified as the extension of A6 to offsets.
- **H-D:** no derivation of A5 from bare OI was found on the record searched.
- **POSIT-MIN (vii)(c):** NOT FORCED by observation.
- **OA-1 D5:** dropping A5 while keeping the affine form does not restore classical control.
- **OA-1 D6:** non-affine rules at configuration level do not close the quantum gap.
- **Q4 G1:** the claim "u_R has no home for any lift" is withdrawn. It fails at s = −5.

### 1.3 The #1083 review-provenance issue

**What it was.** The claim "The Q4 note is accepted at `645bae17`" (#1049 c.6626401398) had no traceable review on GitHub. The core file's acceptance at `f07f55d0` was traceable (#1083 c.6622660127). The Q1/Q2 owner decisions were still listed as open in the file.

**How it was repaired.**
- The original review texts were posted verbatim (#1083 c.6718252075, c.6718263472).
- On the owner's request, a fresh exact-head review was made at `22ad8d69` (c.6718607630). Delta checks follow through `0e7e412a` (c.6718644099).
- A correction comment was posted (#1049 c.6718344623). Q1/Q2 were recorded in the file at `22ad8d69`.
- The owner approved the merge, which keeps every reviewed commit reachable from `main`.

**Effect on standing: none on any result's evidence layer.** The reviews were always model reviews, evidence of review rather than verification (§A.46 item 8). The records never claimed established status. Residual limits:
1. The reviewers are unnamed and the review times are unattested file times. The texts are provenance under §A.42 item 2; no claim rests on them alone.
2. Q4's "decision criteria fixed before §3" is the author's statement only. §1 and §§3–4 entered in one commit (`8de75f7c`; Q4 §8.2). The preregistration label therefore carries no chronological weight.
3. These records landed on 2026-11-08, before §A.46 item 8 (2026-11-14). In the files citing them I found no per-claim remediation plan in §A.46 item 4 form: evidence level, missing verification, accountable Issue, and the evidence that would resolve the gap. This is an administrative reconciliation item, not a scientific defect.

### 1.4 The earliest unresolved scientific question

Taken in order of logical dependency, the record shows three questions:

- **Q-α (upstream of #1049's framing): is the update affine at all?**
  - Main's own adopted Bell branch "lies outside ledger item (vii)" (Main:424), and Main's difference argument holds verbatim for affine φ (POSIT-MIN T1).
  - Under the inclusion reading, with settings, records and carriers as site-additive cell content, configuration-level control and confined records need a non-affine update (OA-1 D5; POSIT-MIN T4/O4).
  - Under an observer-level reading with coarse variables that are not site-additive, an affine rule can carry Toffoli visible dynamics (POSIT-MIN K5).
  - Q-α is open and turns on owner decision POSIT-MIN D2 together with A6's interface (r5 O-G).
- **Q-β (the earliest open question inside #1049's own framing): does any result whose other support stands consume b = 0 of the substratum rule, rather than only its linear part?**
  - The record narrows this to one locus: the uniform k = 0 A₁ sector at κ ≡ 2, equivalently μ_{A₁} = 1. It is A5-LA R3, Q4c and r5 §3.3 together.
  - Only there does a nonzero offset carry invariant content: no fixed point, a secular uniform drift on the lift, and loss of the singlet U(1)'s linear part under (A-lin).
  - Off that locus, at prime q, a static uniform shift removes the offset. The owner's Q2 ruling treats that shift as a mathematical relabelling.
  - Q-β is open through Q4b (are the Stage 2(d) symmetries taken of the rule or of the coupling, and linear or affine?) and Q4c (is A₁ resonant on the maintained branch?). Q4c is conditional on SM:232's unproved bridge from φ to L_obs.
- **Q-γ: which principle selects b = 0?** A scoped negative is recorded (R5, Q3 (N)).

**Reason for the choice.** Q-γ matters only if Q-β is answered "yes". Q-α is logically earlier, but it reaches beyond #1049: it concerns the affine posit, not the offset. I name **Q-β as #1049's earliest unresolved scientific question**, and Q-α as the upstream question it presupposes.

**Re-pin check [W].** Stage 2(d) at Substratum:163 now reads: "the unitary stabilizer of the O-equivariant condensate … is U(3)×U(2)×U(1) [SM Theorem 5]". That is the Σ-route. Q4 §2 S2–S3 located the offset's entry on that route, through the symmetries of the dynamics, so the text revisions since Q4's pin `1609dc44` do not dissolve the D3 candidate.

***

## 2. The questions

The coordinator's clarification is applied throughout. Results about **affine offsets** (A) are kept apart from results about **genuinely nonlinear, non-affine** rules (N), and neither stands in for the other.

**Basic structural fact [A; background: inhomogeneous linear recurrences].** An affine map is linear plus a translation. Affine maps compose to affine maps, and the linear part is a homomorphism. Differences of trajectories evolve exactly by L (A5-LA B0.1). So no amount of affine iteration gives non-affine behaviour. Every limitation derived from the difference structure transfers unchanged from linear to affine. Affine relaxation is therefore not a route to nonlinearity.

### 2.1 Question 1: is microscopic linearity physically necessary? (Also covers the owner's "selecting principle" question.)

- **Selection by an independently justified principle: not found.**
  - R5 examined N1–N11, criteria (a)–(g). Superposition, quadratic energy, time reversal, recurrence, the maximal-entropy measure and isotropy are all satisfied by S1 or presuppose the origin.
  - "Existence of a vacuum" (N6) selects "linear up to a translation", not b = 0, and its period-k variant fails the hard-to-vary test (g).
  - Rescaling as a dynamical symmetry (N8) forces b = 0 only at odd q, presupposes the origin, and was declined by the owner (Q2).
  - E1 relocates additivity to the links (Q3).
  - Support: [D] model-reviewed; finite search, scoped negative.
- **Additional point, an addition to N3 [W] that sharpens the negative.** Linearity of quantum evolution is not evidence for A5. The Koopman operator of any bijection, nonlinear ones included, is a linear unitary permutation, and the continuous *-automorphism path exists for every `Rule` [K]. The two properties the quantum description needs, linearity and continuity, are therefore supplied whatever the form of the rule over ℤ/q.
- **Necessity for observation: not forced.** POSIT-MIN (vii)(c), [R]; H-D, enumeration and adjudication.
- **Necessity for results:**
  - Main's theorems do not take (vii) as a premise (A5-LA D8, D9; POSIT-MIN Q1), [P]/[K]. Main uses (vii) to state what it excludes, at Main:364 and Main:424.
  - In the companion results, A5 as stated is consumed by:
    - Stage 2(d) under (A-lin): the singlet U(1)'s linear part is lost at group level, O1–O4 survive, and carrier-level agreement is conditional (Q4);
    - the quadratic invariant Q, which an offset replaces by Q′ (A5-LA N4);
    - the four kernel modules as stated, whose affine extensions are [D];
    - SM:1416's Layer-2 classes.
  - The consumers that need only the linear part are D1, D2 and D4 (A5-LA §2, [D]).
- **Conclusion (A):** b = 0 is necessary only for statements written under A5, and for the resonant uniform A₁ sector under (A-lin). It is not shown necessary for any observation. Support: [D]/[R]; conditional on the Q4b reading.
- **Conclusion (N), kept separate.** The record contains no argument that additivity, as opposed to affinity, is necessary physically. Against even affinity it records tensions, not refutations (POSIT-MIN T1, T4, T5; each uses an open posit or an interface reading).

**Coordinate vs physical equivalence.** Calling A5 "linear up to relabelling" is a coordinate statement: under the declared shift gauge, A5 is a gauge-fixing condition when κ ≢ 2 (R4, [D]). The physical status of that gauge is open (Substratum:272 "Status (open)"; owner Q2).

### 2.2 Question 2: are affine dynamics observationally distinguishable from linear dynamics?

This is about the statistics of an embedded observer, not about available operations.

- **Relational readouts (𝒜_W, or 𝒜_C for uniform offsets).** Indistinguishable, for every preparation and at all times (R6, [D]).
  - This is identity of laws, with no transformation needed. It is therefore physical equivalence for any observer whose readout class is relational.
  - The owner ruled (Q1) that the shift-invariant interface is "a legitimate conditional alternative, not yet a derived description of all OI observers".
- **Main's absolute interface (the owner's Q1 baseline).** Distinguishable in labelled statistics: S1 shows 𝟙 at t = 1 where L shows 0 (Proposition 2.6(a), [D]). Every per-time-relabelling-invariant statistic agrees, including entropies, the readback mutual information, Markov, P- and CP-divisibility, and finite-horizon representability up to a permutation unitary (R7, [D]).
  - **Off the resonant locus (κ ≢ 2, prime q):** a static uniform shift removes the offset (R3). This is coordinate equivalence. It becomes physical equivalence exactly if amplitude-scale gauge is physical, which is open.
  - **On the resonant locus (κ ≡ 2):** only a time-dependent relabelling relates the two rules, and its admissibility is not established (A5-LA §3.3.7). Invariant differences exist on the full algebra: a full-state observer can detect fixed points; tr U_Φ = #Fix(Φ) is 0 for S1 and at least 1 for L (R8, Proposition 2.6(b)).
  - **Partial visibility with a uniform hidden prior:** agreement holds iff p_V(t) ∈ Im π_V(L^t − I). Not settled by hand (Proposition 2.6(c)).
- **Structural limitations.** Affine and linear are not distinguishable on any limitation that rests on differences:
  - the state-independent dependency graph and the Bell-ceiling argument (Main:364 holds verbatim for affine; POSIT-MIN T1);
  - classical setting control (OA-1 D5).
  - Support: [R]/[A].
- **Open, conjecture [W].** For an embedded observer whose apparatus cells evolve under the same affine rule, the offset drives the uniform mode of system and apparatus alike. Whether apparatus-referenced readouts fall automatically into 𝒜_C is not derived anywhere in the record. It would bear on whether Q1's absolute baseline is operationally realizable by an embedded observer. Candidate gem; unverified.
- **Conclusion (A):** affine and linear dynamics are observationally equivalent except for labelled absolute readouts. Even there, the only content not removable by a static shift lies on the resonant uniform sector. [D], conditional on the readout class.
- **Conclusion (N):** not addressed by these results. Non-affine rules change the difference structure itself and are generally distinguishable. Nothing here transfers.

### 2.3 Question 3: when can affine offsets be eliminated by physically admissible transformations?

| Transformation | Removes b when | Mathematical | Physically admissible on the record |
|---|---|---|---|
| Time-dependent uniform translation z ↦ z − p(t) | always | conjugacy of trajectories (R1) [D] | not established; Theorem 24's generators and the amplitude group are time-independent |
| Static uniform shift | b ∈ (κ − 2)ℤ/q (R3) [D] | coordinate change | only if amplitude-scale gauge is physical (open; owner Q2: "mathematical relabellings unless … justified"). Never available for S1 (κ = 2) |
| Static site-dependent translation | β ∈ Im(I − L), i.e. a fixed point exists (R2) [D] | coordinate change | not declared gauge. Under Main's absolute interface it is visible (Proposition 2.6(b)). A site-dependent relational reading would trivialize every configuration readout |
| Static nonlinear bijection | iff a fixed point exists (R2) | coordinate change | as above |
| Affine internal maps at Stage 2(d) (A-aff) | off resonance: G_0 conjugated about the fixed point | coordinate change | Stage 2(d)'s U(K) contains no affine maps; their status is open (Q4 §4 caveat) |
| Identity, relational readouts | always | none needed (R6) | physical equivalence iff the observer's readout class is relational (open; Q1 baseline is absolute) |

**Conclusion.** Elimination is a mathematical fact whenever a fixed point exists. It is physically justified only under amplitude-scale gauge, which is open, and only off the zero-mode resonance. On resonance no static admissible transformation exists. This holds on finite carriers. On infinite lattices or open chains a site-dependent quadratic profile removes the offset (A5-LA §6, open), and the admissibility question repeats there.

### 2.4 Question 4: would relaxing linearity overcome the existing operational limitations?

The owner's three-way distinction is applied here directly.

- **(A) Affine relaxation, b ≠ 0: no, for every limitation examined.**
  - Under any affine rule a setting acts only by translation (OA-1 D5, [R]). Dropping A5 while keeping the affine form does not restore control.
  - The dependency graph is unchanged on every state class, so the Bell ceiling at Main:364 stands (POSIT-MIN T1, [A]/[R]).
  - Affine relaxation also cannot reach the quantum ceiling (next item).
  - It does supply something, but only of a classical-descriptive kind: no fixed point and a uniform drift on the resonant sector. Neither is an operational capability.
- **(N) Genuine nonlinearity, quantum limitations: no, at the configuration-level interface. This is a negative backed by kernel theorems.**
  - The observer theory is `permTheory` on the configuration space, independent of the rule by definition (`obsTheory_rule_independent`, `rfl`).
  - It preserves nonnegative entries, so it has no phases and no dense control on `Fin 2`, for every `Rule` (`phase_ceiling_rule_independent`) [K].
  - Pressure test of the favourable-looking "rule independence" (§A.31): rule independence holds by definition, so it is not the load-bearing content. The load-bearing statement is `permMatrix_preservesNonneg`, which holds for **every** permutation σ. Any deterministic bijective update, however nonlinear over ℤ/q, has a permutation Koopman operator. That operator lies in the monomial class, which already contains every permutation of every carrier.
  - Adding nonlinear rules therefore adds no element to the class, and `substratumClass_not_drivesElementary` [K] stands. Transition flows at generic t are not monomial.
  - A rule-derived interface is a sub-theory and inherits the ceiling (OA-1 D6, [W] built on [K]).
  - Support: [K], with a one-line composition [A].
  - Scope: the configuration-level identification. Encoded frames are capped by paper results at stabilizer/Clifford operations (OA-1 5c, [R]; [background]: Gottesman–Knill). Record-level interfaces with M-INACC on growing carriers (OA-1 5d) remain **open, not shown impossible**. Emergent amplitude spaces (5e) import their resources.
  - The #1558 hypothesis "relaxing linearity could help overcome the operational limitations" is therefore **refuted at configuration level for the quantum limitations, for every rule class**. It is unevaluated for interfaces outside that identification.
- **(N) Genuine nonlinearity, classical limitations: yes, under named readings.**
  - A non-affine switch supplies classical setting-selective control (OA-1 gap 2, "classical repair only" [R]; [background]: Fredkin and Toffoli reversible logic).
  - It supplies confined records and conditional dynamics under the inclusion reading (POSIT-MIN T4, [R]).
  - It supplies the state-dependent coupling graph that Main's Bell branch requires (Main:424, [P]).
  - Pressure test: POSIT-MIN K5 shows an affine microscopic rule can carry non-affine (Toffoli) visible dynamics through coarse variables that are not site-additive ([W], reviewer-checked at n = 4). Even classical control is therefore not strictly a reason to require microscopic nonlinearity; it depends on owner decision POSIT-MIN D2.
- **Hydrodynamic limitation (classical).**
  - The coarse-closure obstruction for advection holds under additivity [K: `coarseCloses_nsmul`]. It extends to affine rules with degree ≤ 1 in n (A5-LA B3.4, [D]).
  - Non-affine rules escape the hypothesis. The kernel's `hexSubstratum_not_A5` is a non-A5 reversible lattice gas. Whether escaping it yields advection is not established here.

***

## 3. Classification table

| Conclusion | Support class | Evidence | Conditions |
|---|---|---|---|
| No principle among N1–N11 selects b = 0 independently | paper derivation, model-reviewed; finite search | A5-LA R5 | not an impossibility result |
| None of E1–E3 justifies extending A6 to offsets | paper derivation, model-reviewed | Q3 (N) | amplitude-scale gauge; reviewed scope |
| A5 not forced by observation; not derived from bare OI | reviewed research record; enumeration | POSIT-MIN (vii)(c); H-D | records searched |
| Linearity of quantum evolution and the continuous path do not select A5 | kernel theorem + [A] | `driveQ_isContinuousPath` for every `Rule`; Koopman of any bijection | — |
| Linearizable by a time-independent bijection iff a fixed point exists | paper derivation | A5-LA R2 | finite abelian G |
| Affine = linear for relational readouts, all times, all preparations | paper derivation | A5-LA R6 | readouts in 𝒜_W or 𝒜_C |
| At the absolute interface: equal up to a time-dependent relabelling; invariant differences only on the resonant sector | paper derivation | A5-LA R3, R7, R8, Proposition 2.6 | prime q for the static-shift statement |
| Static elimination physically justified only under amplitude gauge, off resonance | paper derivation + manuscript status | A5-LA §3.3.7; Substratum:272 | amplitude gauge open |
| b = 0's invariant content is confined to the uniform A₁ sector at κ ≡ 2 | paper derivation (A5-LA); off-`main` r5 §3.3 | A5-LA R3; Q4c; r5 | H-b; lift; uniform offset |
| Stage 2(d) under (A-lin): U(1)_S lost; O1–O4 agree at group level | paper derivation, model-reviewed | Q4 outcome (iii) | H-b, lift, uniform v ≠ 0; O5 not examined |
| Affine rules give no classical setting control | reviewed record (one proof, three derivations) | OA-1 D5 | inclusion reading |
| No rule, linear, affine or nonlinear, moves the phase or dense-control ceiling | kernel theorem | `obsTheory_rule_independent`, `permMatrix_preservesNonneg`, `phase_ceiling_rule_independent`, `substratumClass_not_drivesElementary` | configuration-level identification |
| Non-affinity supplies classical control, records, the Bell-branch graph | reviewed records + manuscript | OA-1 gap 2; POSIT-MIN T1, T4; Main:424 | inclusion reading (D2); K5 escape for coarse variables that are not site-additive |
| Embedded-apparatus readouts automatically relational | conjecture | §2.2 here | unverified |

***

## 4. Outcome against the three possibilities

- **Linearity derivable:** not supported. The scoped negatives are R5, Q3 (N), H-D and POSIT-MIN. A finite search does not exclude a principle.
- **Linearity unnecessary:** the best-supported reading for the affine-vs-linear question.
  - Main's theorems do not use it.
  - Relational observation cannot see it.
  - Absolute observation sees it only through labels, and invariantly only on the resonant uniform A₁ sector.
  - The structural limitations of linear and affine coincide.
- **Necessary but not derivable:** survives on one locus only. That is the resonant sector under (A-lin) at Stage 2(d), with labelled absolute readouts. It is contingent on Q4b, Q4c and SM:232.
- **Overall:** the evidence currently supports "unnecessary at the examined scope, with one residual locus whose status is a reading, not a derivation". Support level: paper derivation, model-reviewed.
- **What would decide it:** Q4b (rule or coupling stabilizer; linear or affine elements), Q4c (resonance of A₁ on the maintained branch), and the interface reading (Q1 baseline versus relational).
- **On a separate axis:** genuine nonlinearity is neither needed for, nor capable of, sourcing quantum operations at the configuration level [K]. Its relevance is classical. The #1049 question and the #1558 limitations are therefore decoupled at that level.

***

## 5. Smallest discriminating next step (proposal only; needs separate owner authorization)

**Paper-only "b-consumption trace" at the current pin.**
- **Step:** re-pin every A5 consumer: A5-LA D1–D16; Stage 2(d) as now worded on the Σ-route (Substratum:163; SM Theorem 5); Theorem 23; SM:1416; the four kernel modules.
- **Classification:** each consumer goes into one of three classes:
  - (a) uses only the linear part or the lift;
  - (b) uses b = 0 removable by a static uniform shift;
  - (c) uses b = 0 on the resonant uniform A₁ sector.
- **Decision rule, preregistered as a rule:**
  - If no consumer falls in (c) under the reading the manuscript states, outcome "unnecessary at stated scope" (criterion 2).
  - Otherwise #1049 reduces to Q4c, conditional on SM:232.
- **Controls:** A5-LA C1–C8. Countercontrol: S1's absolute readout.
- **Coordination:** this overlaps POSIT-MIN D1(b), the lift-level sufficiency trace, and should be coordinated under #1169 so it is not duplicated.
- **Optional computation, separate authorization:** A5-LA §7's exact controls for R2, R3, R6, R7 and Proposition 2.6(c), CI-scale. They upgrade [D] to exhaustive finite computation on named cases. Nothing more is proposed for the nonlinearity question: the configuration-level negative is kernel-settled, and the open interfaces (OA-1 5d) belong to #914/#1169, not #1049.

***

## 6. Limitations; manuscript and record inaccuracies (listed, not edited)

**Limitations.**
- I did not re-derive every A5-LA or Q4 step; I spot-checked B0.1–B0.3, N8 and the kernel compositions.
- I did not read MR★, NR-1, UNIV-1 or the #1043 PR itself.
- r5 is off `main`. Its P1/GA7-α results are cited as context only.
- No literature was retrieved.

**Inaccuracies found.**
1. **SM:587, candidate.** It states "the two combinations of (B, L, S) orthogonal to hypercharge cannot be gauged: gauging them would introduce non-cancelling chiral anomalies".
   - On Hom-type carriers (V_K ⊗ V_K*, SM:519–539), the direction (1,1,1) acts trivially [A].
   - The two-dimensional orthogonal complement therefore contains a combination that acts on fermions as a multiple of Y, which is anomaly-free.
   - "Orthogonal" also presupposes an inner product that is not stated.
   - This carries Q4 N8b's moderate confidence and is independent of A5. Suggested route: #1029.
2. **Main:736 (vii) versus Main:424.** The ledger lists A5 unscoped, while Main's adopted Bell branch lies outside (vii). This is known (POSIT-MIN T1/D1) and pending an owner decision; it is not new.
3. **OA-1 D5, record wording.** Its "Scope" line says ledger (vii) "derives the affine form from amplitude-scale gauge invariance". The current ledger and SM:96 derive affinity from base-point independence, and state that affine covariance alone allows nonlinear rules.
4. **Stale citations in pinned records.** A5-LA §3.3.8 / §5(a) and Q4 §2 S1 quote Substratum wording that has since changed. Not errors at their pins, but they need re-pinning before reuse.

Nothing in this report adopts, weakens or changes any premise, A5 included.
