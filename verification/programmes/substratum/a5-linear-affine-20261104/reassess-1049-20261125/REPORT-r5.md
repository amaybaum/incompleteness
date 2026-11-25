# #1049 research report: linear vs affine microscopic dynamics (paper-only, read-only)

## 0. Status, pin, sources

**Status.** I read sources and reasoned on paper only. I wrote nothing to git or GitHub, edited no manuscript, ran no computation and built no Lean. Nothing here changes a premise. A5 stays a posit (owner, #1049 c.6624263637). Every new step below is labelled [A] (exact algebra by hand in this report, unreviewed) or [W] (reasoning in this report, unreviewed). Cited support is labelled [K] (kernel theorem; statement read at the pin, nothing built), [K, definitional] (a kernel theorem that holds by definition, `rfl` or `Iff.rfl`), [P] (manuscript statement), [D] (derivation in a model-reviewed record), [R] (reviewed research record) or [background] (literature, not retrieved). A combined label such as [K]+[W], [D]/[R], [R]/[A] or [A]/[W] gives the support of the parts of one statement; the statement takes its weakest part.

**Revision r2.** This revision applies the owner decision "#1561 | Apply the four previously specified scope and interpretation corrections." (amaybaum, 2026-11-25), namely the blocking findings R1–R4 of the independent review on PR #1561 (comment 7166779576). The edited passages are §1.1 (kernel bullets), §2.1 (one bullet, kept consistent with §4), §2.2 (Main's absolute interface; Conclusion (A)), §2.4 (genuine nonlinearity, quantum limitations), §3 (the corresponding rows), §4 and one clause of §5. CHANGES-r2.md maps each finding to its change. The Lean statements cited in the edited passages were re-read at the pin.

**Revision r3.** Revision r3 applies the owner decision "#1561 — Linearity | Apply F1–F3 and the remaining minor scope and labelling corrections." (amaybaum, 2026-11-25, #1169 comment 7167242160), with the reviewer's proposed wording for F1, as a minimal revision addressing only the findings F1–F3 and the nits of the delta review of r2 on PR #1561. The edited passages are §0 (this line and the label list), §1.2 (OA-1 D6), §2.1 (one bullet), §2.2 (one body bullet and Conclusion (A)) and §5 (one outcome). CHANGES-r3.md lists each change.

**Revision r4.** Revision r4 applies the owner decision "#1049 | Narrow the three passages to support available on main. Retain r5 as provenance only, not acceptance support." and "Both | Add the preservation rationale and remediation plan required by §A.46 item 8." (amaybaum, 2026-11-25, #1169 comment 7167657546). The edited passages are §0 (this line), §1.4 (the last Q-α bullet and the first two Q-β bullets), §3 (one row) and §6 (one limitation), and §7 is new. The narrowed passages rest only on records on `main` at the pin; r5 is provenance only. No other result changes. CHANGES-r4.md lists each change.

**Revision r5.** Revision r5 applies the owner decision "#1049 — Linearity | Resolve nits 1–6. Add the superseded notice to REPORT-r3.md." (amaybaum, 2026-11-25T16:29:44Z, #1169 comment {{ID:c29}}), resolving nits 1–6 of the delta review of r4. The edited passages are §0 (this line), §1.4 (one clause of the second Q-β bullet), §7.3 (the r3 and r4 lines), §7.6 (V-1 and V-2), §7.7 and §7.8 (three rows, one of them new). No result changes. CHANGES-r5.md lists each change.

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
  - `FrozenSourcing.lean`: `obsTheory_nonnegBounded`, `permMatrix_preservesNonneg`, `sourcing_rule_independent`, `phase_ceiling_rule_independent`, `nonnegBounded_not_denseUnitaryControl`, `permTheory_dense_ceiling`.
  - `SubstratumInterfaceAudit.lean`: `Substratum`, `a2_every_substratum`, `permClass`, `A5`, `obsTheory_eq_permTheory`, `obsTheory_rule_independent`.
  - `DiscreteCompletion.lean`: `DenseUnitaryControl` (defined for theories on `Fin 2` only).
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
  - The observer theory of any kernel substratum is the permutation theory of its configuration space, whatever the rule (`obsTheory_eq_permTheory`, `obsTheory_rule_independent`). Both hold by `rfl`: `obsTheory` is an `abbrev` for `permTheory` of the configuration space, and the rule does not occur in it. A kernel `Substratum` is a finite-range second-order `Rule ι V`, update (p, c) ↦ (c, F c − p), on additive groups ι and V; `obsTheory` exists only for finite ι and V. The scheme is bijective by construction (`a2_every_substratum`) and affine in p, whatever F.
  - That theory preserves nonnegative entries (`obsTheory_nonnegBounded`). So it has no phases, for every such `Rule`, additive or not (`phase_ceiling_rule_independent`, which proves ¬`PhasesAvailable` and nothing about dense control).
  - Dense unitary control is defined only for theories on `Fin 2` (`DenseUnitaryControl`). No nonnegativity-bounded theory on `Fin 2` has it (`nonnegBounded_not_denseUnitaryControl`), and in particular `permTheory (Fin 2)` does not (`permTheory_dense_ceiling`). Neither theorem involves a rule. The observer theory's carrier ι → V × V has |V|^{2|ι|} elements, a perfect square and never 2, so no `Rule` gives a theory on `Fin 2` [A]. Applying the dense-control ceiling to a qubit encoded in a substratum is a separate encoding step, [A]/[W] per encoding, not a kernel statement.
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
- **OA-1 D6:** non-affine rules at configuration level do not close the quantum gap at the configuration-level interface as defined; [R].
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
  - Q-α is open. On the records on `main` it turns on owner decision POSIT-MIN D2, the interface reading of O4. An answer that requires a non-affine update would also need A6's formal interface, which types the link coupling as additive (`linkF : V →+ V`), checked for the additivity it builds in (POSIT-MIN (xii)(e) and DV-1; A5-LA D14). Whether A6's interface, read for non-additive link maps, itself bears on where the affine restriction comes from is not addressed in the records on `main` read for this report (§0); it is open.
- **Q-β (the earliest open question inside #1049's own framing): does any result whose other support stands consume b = 0 of the substratum rule, rather than only its linear part?**
  - The records on `main` locate the content of a uniform offset that no static uniform shift removes at one locus. For a second-order, translation-commuting rule the offset is uniform, and a static uniform shift removes it iff b ∈ (κ − 2)ℤ/q (A5-LA B0.3(a), (c); R3), so at prime q it is irremovable only at κ ≡ 2. On the lift this is the uniform k = 0 mode (A5-LA Proposition 2.5). With H-b the offset lies in the A₁ block (Q4 N0), and κ_{A₁} = 2μ_{A₁}, so the locus is the A₁ resonance μ_{A₁} = 1 (Q4, paragraph "Resonance" before §1; Q4c). Support: [D]. Whether every consumer's use of b = 0 reduces to this locus is not traced in the records on `main`; that is the §5 trace, and it is open.
  - On that locus the offset carries content that no static uniform shift removes [D]: on the real lift the uniform mode grows secularly as bt²/2 (A5-LA Proposition 2.5); there is no fixed point on the lift (Q4 N1, resonance case) or for S1 over 𝔽₅ (C2; B0.3(d)), although over ℤ/q with an odd prime q ∣ N a fixed point with a non-uniform profile exists (B0.3(e)); and under (A-lin) the loss of the singlet U(1)'s linear parts, which Q4 finds at every nonzero uniform offset, is removed off the locus by the static uniform shift to the fixed point, as a relabelling (owner Q2), and is not removed on it (Q4 N1, (L) and (A-aff) off-resonance branches; [D]+[W]).
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
  - Main uses (vii) at Main:368 (G_φ^K = G_φ for every non-empty state class K) and at Main:736 (with (x), the bound of (ix) for G_φ); those uses need only the affine condition (POSIT-MIN T1), [P]; affine sufficiency [R]/[A]. Main also uses (vii) to state what it excludes, at Main:368 and Main:424.
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
- **Main's absolute interface (the owner's Q1 baseline).** Distinguishable in labelled statistics: S1 shows 𝟙 at t = 1 where L shows 0 (Proposition 2.6(a), [D]). The difference is not confined to S1 or to the resonant locus: for any nonzero offset β, at every κ, the sharp preparation at the zero configuration gives Φ(0) = β ≠ 0 = L(0) at t = 1, so labelled one-step statistics differ [A]. Every per-time-relabelling-invariant statistic agrees, including entropies, the readback mutual information, Markov, P- and CP-divisibility, and finite-horizon representability up to a permutation unitary (R7, [D]).
  - **Off the resonant locus (κ ≢ 2, prime q):** a static uniform shift removes the offset (R3). This is coordinate equivalence. It becomes physical equivalence only if amplitude-scale gauge is physical, which is open.
  - **On the resonant locus (κ ≡ 2):** only a time-dependent relabelling relates the two rules, and its admissibility is not established (A5-LA §3.3.7). Invariant differences exist on the full algebra: a full-state observer can detect fixed points; tr U_Φ = #Fix(Φ) is 0 for S1 and at least 1 for L (R8, Proposition 2.6(b)).
  - **Partial visibility with a uniform hidden prior:** agreement holds iff p_V(t) ∈ Im π_V(L^t − I). Not settled by hand (Proposition 2.6(c)).
- **Structural limitations.** Affine and linear are not distinguishable on any limitation that rests on differences:
  - the state-independent dependency graph and the Bell-ceiling argument (Main:364 holds verbatim for affine; POSIT-MIN T1);
  - classical setting control (OA-1 D5).
  - Support: [R]/[A].
- **Open, conjecture [W].** For an embedded observer whose apparatus cells evolve under the same affine rule, the offset drives the uniform mode of system and apparatus alike. Whether apparatus-referenced readouts fall automatically into 𝒜_C is not derived anywhere in the record. It would bear on whether Q1's absolute baseline is operationally realizable by an embedded observer. Candidate gem; unverified.
- **Conclusion (A), stated per readout class.** [D], with the [A] step above.
  - **Relational readouts (𝒜_W, 𝒜_C):** indistinguishable; identity of laws (R6). This is physical equivalence for an observer whose readout class is relational, which owner ruling Q1 records as a conditional alternative, not as the baseline.
  - **Main's absolute interface (Q1 baseline):** distinguishable in labelled statistics at every κ whenever the offset is nonzero. At that interface labelled statistics are observable, so this is an observational difference at that interface as defined; whether it is physical turns on the gauge reading below.
  - **Off the resonant locus:** a static uniform shift removes the offset (R3). That is coordinate equivalence; it is physical equivalence only if amplitude-scale gauge is physical, which is open (owner Q2).
  - **On the resonant locus:** no static admissible transformation removes the offset. The differences invariant under every static relabelling lie on the resonant uniform sector (R8, Proposition 2.6(b)). The one exhibited, #Fix(Φ) = tr U_Φ, is read on the full algebra and needs a full-state observer; that an embedded observer can read it is not shown.
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
- **(N) Genuine nonlinearity, quantum limitations: cannot be affected at the configuration-level interface, which is rule-blind by construction [K, definitional]; for interfaces derived from the rule, [W] via OA-1 D6; elsewhere unevaluated.**
  - **Class covered by the kernel statement.** Finite configuration spaces; second-order kernel rules (p, c) ↦ (c, F c − p), F finite-range, on finite sites ι and a finite alphabet V (`Substratum`, `Rule`; `obsTheory` needs `[Fintype ι] [Fintype V]`); the configuration-level interface as defined, that is, `obsTheory` = `permTheory` of ι → V × V. "Every `Rule`" means every F inside this fixed scheme, which is bijective and affine in p whatever F is.
  - **Phases [K].** `obsTheory` is `permTheory` on the configuration space, and the rule does not occur in it (`obsTheory_eq_permTheory`, `obsTheory_rule_independent`, `sourcing_rule_independent`: `rfl` / `Iff.rfl`). It is nonnegativity-bounded (`obsTheory_nonnegBounded`), so ¬`PhasesAvailable` for every such `Rule` (`phase_ceiling_rule_independent`).
  - **Dense control [K] only on `Fin 2`.** No nonnegativity-bounded theory on `Fin 2` has dense unitary control (`nonnegBounded_not_denseUnitaryControl`, `permTheory_dense_ceiling`). No `Rule` gives a theory on `Fin 2` (§1.1). Its application to a substratum-encoded qubit is a separate stated encoding step, [A]/[W] per encoding.
  - **What carries the result (pressure test, §A.31).** Rule independence holds by definition. `permMatrix_preservesNonneg` states that the conjugation channel of any permutation matrix preserves nonnegative entries, which is elementary. The load-bearing content is the modelling choice that the observer's operations are exactly the configuration space's scaled partial permutations (`permClass`, `permTheory`). The kernel therefore shows that this interface, as defined, cannot see the rule. It does not test whether a nonlinear rule changes the interface an embedded observer actually realizes.
  - **Classes in play.** The nonnegativity ceiling is a property of `permClass` / `permTheory`. The monomial `substratumClass` contains `phaseGate` (`phase_monomial`, SubstratumInterface.lean) and every permutation matrix (`monomial_permMatrix`), and fails `DrivesElementary` only through the transition flows `flow (transition a b) t` at generic t (`substratumClass_not_drivesElementary`) [K]. A permutation Koopman operator lies in both classes, and admitting further rules on the same configuration space enlarges neither.
  - **Other bijections of the configuration space**, not of second-order form, are outside the kernel statement. If the same interface definition is assumed for them, the observer theory is again `permTheory` of the finite configuration space and the phase ceiling follows [A]. Their Koopman operator is a permutation matrix and preserves nonnegativity (`permMatrix_preservesNonneg`, for any σ, [K]).
  - **Outside the statement:** non-bijective, dissipative or stochastic rules, and infinite or continuous-state dynamics. §A.29's research target allows a deeper dynamics that "need not be quantum or finite", and these classes bear on the question while retirement of total finiteness (A1) is open under #1169. Nothing here evaluates them.
  - **Interfaces derived from the rule:** a rule-derived interface is a sub-theory and inherits the ceiling (OA-1 D6, [W] built on [K]).
  - **Further interfaces.** Encoded frames are capped by paper results at stabilizer/Clifford operations (OA-1 5c, [R]; [background]: Gottesman–Knill). Record-level interfaces with M-INACC on growing carriers (OA-1 5d) remain **open, not shown impossible**. Emergent amplitude spaces (5e) import their resources.
  - **The #1558 hypothesis** "relaxing linearity could help overcome the operational limitations", for the quantum limitations: for finite configuration spaces and second-order kernel rules (other bijections via the [A] extension), it cannot be affected at the configuration-level interface as defined, which is rule-blind by construction [K, definitional]; for interfaces derived from the rule the same holds at [W] (OA-1 D6); for encoded frames the OA-1 5c cap applies [R]; for record-level interfaces on growing carriers, emergent amplitude spaces, and non-bijective, dissipative, stochastic, infinite or continuous dynamics it is unevaluated. Support class: [K]+[W].
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
| At Main's absolute interface: labelled statistics differ at every κ for any nonzero offset; laws equal up to a time-dependent relabelling; differences invariant under static relabelling only on the resonant sector, read by a full-state observer | paper derivation + [A] | A5-LA R3, R7, R8, Proposition 2.6; §2.2 here | prime q for the static-shift statement; physical equivalence off resonance only if amplitude-scale gauge is physical (open) |
| Static elimination physically justified only under amplitude gauge, off resonance | paper derivation + manuscript status | A5-LA §3.3.7; Substratum:272 | amplitude gauge open |
| At prime q, the content of a uniform offset that no static uniform shift removes is confined to the uniform sector at κ ≡ 2, which with H-b is the A₁ resonance μ_{A₁} = 1; whether every consumer's use of b = 0 reduces to it is open | paper derivation, model-reviewed | A5-LA R3, B0.3, Proposition 2.5; Q4 N0, N1, Q4c | second-order, translation-commuting rules; prime q; H-b; lift; uniform offset; consumer reduction not traced (§5) |
| Stage 2(d) under (A-lin): U(1)_S lost; O1–O4 agree at group level | paper derivation, model-reviewed | Q4 outcome (iii) | H-b, lift, uniform v ≠ 0; O5 not examined |
| Affine rules give no classical setting control | reviewed record (one proof, three derivations) | OA-1 D5 | inclusion reading |
| No phases in the observer theory, for every second-order kernel rule; the configuration-level interface is rule-blind by construction | kernel theorem, definitional | `obsTheory_eq_permTheory`, `obsTheory_rule_independent`, `obsTheory_nonnegBounded`, `phase_ceiling_rule_independent` | finite ι and V; rules (p, c) ↦ (c, F c − p); interface as defined; other bijections only via [A] under the same interface definition; non-bijective, dissipative, stochastic, infinite or continuous dynamics outside |
| No dense unitary control for nonnegativity-bounded theories on `Fin 2` | kernel theorem | `nonnegBounded_not_denseUnitaryControl`, `permTheory_dense_ceiling` | `Fin 2` only; no rule involved and no `Rule` gives a `Fin 2` theory; application to an encoded qubit is a separate step [A]/[W] |
| The monomial class fails `DrivesElementary`; further rules on the same configuration space enlarge neither it nor `permClass` | kernel theorem + [A] | `substratumClass_not_drivesElementary`, `monomial_permMatrix`, `permMatrix_preservesNonneg` | fails through the transition flows; `substratumClass` contains `phaseGate` |
| Rule-derived interfaces inherit the ceiling | [W] built on [K] | OA-1 D6 | sub-theory reading |
| #1558 application: nonlinearity cannot lift the quantum limitations | [K]+[W] | rows above; §2.4 | configuration-level interface as defined [K, definitional] and rule-derived interfaces [W]; elsewhere unevaluated |
| Non-affinity supplies classical control, records, the Bell-branch graph | reviewed records + manuscript | OA-1 gap 2; POSIT-MIN T1, T4; Main:424 | inclusion reading (D2); K5 escape for coarse variables that are not site-additive |
| Embedded-apparatus readouts automatically relational | conjecture | §2.2 here | unverified |

***

## 4. Outcome against the three possibilities

- **Linearity derivable:** not supported. The scoped negatives are R5, Q3 (N), H-D and POSIT-MIN. A finite search does not exclude a principle.
- **Linearity unnecessary:** assessed as two separate questions.
  - **Owner question (1), whether any established prediction needs b = 0: none is shown to.** Main's uses of (vii) need only the affine condition (Main:368; POSIT-MIN T1). The companion consumers of b = 0 are statements written under A5 and the resonant uniform A₁ sector under (A-lin) at Stage 2(d) (§2.1). The structural limitations of linear and affine dynamics coincide (§2.2, §2.4). Support: [D]/[R], conditional on the Q4b reading.
  - **Owner question (2), whether affine dynamics are observationally distinguishable: it depends on the readout class** (§2.2 Conclusion (A)). For relational readouts, no: the laws are identical. At Main's absolute baseline interface, yes: labelled statistics differ at every κ for any nonzero offset.
  - **"Unnecessary" is therefore conditional on the readout class and on the gauge reading.** It holds in sense (1) on the record examined. In the observational sense it holds for relational readouts. At Main's absolute baseline it holds only if labelled differences are discounted. Off resonance that is licensed only if amplitude-scale gauge is physical (open), and on resonance by no established transformation.
- **Necessary but not derivable:** survives on one locus only. That is the resonant sector under (A-lin) at Stage 2(d), with labelled absolute readouts. It is contingent on Q4b, Q4c and SM:232.
- **Overall:** for question (1), the evidence supports "no established prediction shown to need b = 0 at the examined scope, with one residual locus whose status is a reading, not a derivation". For question (2), affine and linear dynamics are indistinguishable for relational readouts and distinguishable in labelled statistics at Main's absolute baseline. Whether that difference is physical is open: off resonance it turns on amplitude-scale gauge, and on resonance no admissible static transformation is established. Support level: paper derivation, model-reviewed, with the [A] step of §2.2.
- **What would decide it:** Q4b (rule or coupling stabilizer; linear or affine elements), Q4c (resonance of A₁ on the maintained branch), the interface reading (Q1 baseline versus relational), and the status of amplitude-scale gauge.
- **On a separate axis:** at the configuration-level interface as defined, genuine nonlinearity cannot affect the quantum ceilings, because that interface is rule-blind by construction. Phases are [K] for every second-order kernel rule on finite sites and alphabet. Dense control is [K] on `Fin 2` only, and reaches an encoded qubit only through a separate encoding step [A]/[W]. For rule-derived interfaces the statement is [W] (OA-1 D6); elsewhere it is unevaluated. The demonstrated relevance of nonlinearity is classical. At the configuration-level interface as defined, the #1049 question and the #1558 limitations are therefore decoupled; beyond it, decoupling is not established.

***

## 5. Smallest discriminating next step (proposal only; needs separate owner authorization)

**Paper-only "b-consumption trace" at the current pin.**
- **Step:** re-pin every A5 consumer: A5-LA D1–D16; Stage 2(d) as now worded on the Σ-route (Substratum:163; SM Theorem 5); Theorem 23; SM:1416; the four kernel modules.
- **Classification:** each consumer goes into one of three classes:
  - (a) uses only the linear part or the lift;
  - (b) uses b = 0 removable by a static uniform shift;
  - (c) uses b = 0 on the resonant uniform A₁ sector.
- **Decision rule, preregistered as a rule:**
  - If no consumer falls in (c) under the reading the manuscript states, outcome "unnecessary in sense (1) at stated scope" (criterion 2).
  - Otherwise #1049 reduces to Q4c, conditional on SM:232.
- **Controls:** A5-LA C1–C8. Countercontrol: S1's absolute readout.
- **Coordination:** this overlaps POSIT-MIN D1(b), the lift-level sufficiency trace, and should be coordinated under #1169 so it is not duplicated.
- **Optional computation, separate authorization:** A5-LA §7's exact controls for R2, R3, R6, R7 and Proposition 2.6(c), CI-scale. They upgrade [D] to exhaustive finite computation on named cases. Nothing more is proposed for the nonlinearity question: at the configuration-level interface as defined the rule cannot enter, by construction [K, definitional], and the open interfaces (OA-1 5d) belong to #914/#1169, not #1049.

***

## 6. Limitations; manuscript and record inaccuracies (listed, not edited)

**Limitations.**
- I did not re-derive every A5-LA or Q4 step; I spot-checked B0.1–B0.3, N8 and the kernel compositions.
- I did not read MR★, NR-1, UNIV-1 or the #1043 PR itself.
- r5 (draft PR #1226, unmerged) is off `main` and is provenance only: no conclusion of this report rests on it. §7.8 classifies each reference to it.
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

***

## 7. Preservation and verification status (§A.46 items 4 and 8)

### 7.1 What the record contains

This report is a research record, not an established claim (§A.46 item 1). Its substantive, nonredundant content is:
- **A per-question synthesis of the A5 records on `main`** (A5-LA, Q4, Q3, H-D, POSIT-MIN, OA-1) against the owner's three questions (#1049 comment 7163815560), with affine offsets (A) and non-affine rules (N) kept apart throughout (§§2–4).
- **New steps not stated in those records:**
  - at Main's absolute interface, labelled one-step statistics differ at every κ for every nonzero offset (§2.2, [A]), whereas the differences invariant under every static relabelling lie on the resonant uniform sector;
  - the observer theory's carrier never has two elements, so no `Rule` gives a theory on `Fin 2` (§1.1, [A]);
  - linearity and continuity of the quantum description are supplied whatever the rule, so they do not select A5 (§2.1, [W], an addition to N3);
  - the scope statement of the kernel negative for non-affine rules: the configuration-level interface is rule-blind by construction, with the pressure test that names the modelling choice carrying it (§2.4, [K, definitional]);
  - the conjecture on embedded-apparatus readouts (§2.2, [W]).
- **The identification of Q-β** as #1049's earliest unresolved scientific question, with Q-α as the upstream question it presupposes (§1.4).
- **The proposed b-consumption trace** with a preregistered decision rule (§5), and **four listed inaccuracies** (§6), among them the SM:587 candidate.

### 7.2 Scope and limits of the evidence

- Paper-only. No computation was run, no Lean was built and no literature was retrieved. Kernel statements were read at the pin; their kernel standing comes from the kernel build on `main`, not from this report.
- Manuscript and record pin: `main` = `e2e2a623265187a28ebec604ab8bcc672742888f`.
- Every new step is [A] or [W] in this report and has been checked only by the model reviews of §7.3.
- The cited records are model-reviewed research records; none is established (§1.1). A conclusion here takes the weakest support of its parts (§0).
- The limitations listed in §6 apply.

### 7.3 Independent reviews

Each review was made by a Claude reviewer agent started with a fresh context, which wrote none of the reviewed work (owner decision at #1169 comment 7166418469). A model's acceptance is evidence of review, not independent mathematical verification (§A.46 item 8), and it changes no evidence layer.
- r1 (REPORT.md, commit `8aef91cf1b7876ea9d70d5ac474684e123d8c510`): PR #1561 comment 7166779576, verdict REVISE, with blocking findings R1–R4. Applied in r2.
- r2 (REPORT-r2.md, commit `0c058645b1cb0a642f0de6afa7cab129f383dc2e`): delta review, PR #1561 comment 7167108875, verdict ACCEPT-WITH-NITS, with findings F1–F3 and nits. Applied in r3.
- r3 (REPORT-r3.md, commit `389d6ea46a2bac11f257acd78536a982a5b2c15d`): delta review, PR #1561 comment {{ID:1561-r3}}, verdict ACCEPT.
- r4 (REPORT-r4.md, commit `46e82783ad2f33e3ce956e3189ad9c54ca541bab`): bounded delta review, as the owner's decision requires (§7.9); it is not yet recorded on GitHub, and its verdict is not stated here. Its nits 1–6 are applied in r5.

### 7.4 Accountable Issue

#1049. The guiding pull request is #1561. Gaps that belong to other programmes name their own Issue in §7.6.

### 7.5 Verification status per claim class

| Claim class (label) | Where | Status (§A.46 item 4) |
|---|---|---|
| Kernel theorems [K], [K, definitional] | §1.1, §2.4, §3 | independently verified at the kernel layer for the statements as proved; their application here (scope, interface reading, encoding steps) is [A]/[W] and partially verified |
| Manuscript statements [P] | §1.1, §2.1 | cited as stated at the pin; they carry the manuscript's own status |
| Derivations in model-reviewed records [D] (A5-LA, Q4, Q3) | §§1–4 | partially verified: paper derivations with model reviews, no exact controls run |
| Reviewed research records [R] (OA-1, POSIT-MIN, H-D) | §§1–4 | partially verified: paper results with model reviews |
| New [A] and [W] steps of this report | §1.1, §2.1, §2.2, §2.4 | partially verified: model reviews of r1–r3 only |
| Conjecture (embedded-apparatus readouts) | §2.2, §3 | exploratory |
| Q4 G1, "u_R has no home for any lift" | §1.2 | known-invalid: withdrawn, it fails at s = −5 |
| Inaccuracies listed in §6 | §6 | findings for routing; item 1 is a candidate ([A], moderate confidence) |

### 7.6 Remediation plan for each open verification gap

This plan authorizes no work (§A.46 item 4; §A.45 rule 3). An obligation may remain open.

| Gap | Current evidence level | Missing verification | Accountable Issue | Evidence or decision that would resolve it |
|---|---|---|---|---|
| V-1. A5-LA R2, R3, R6, R7, Proposition 2.6(c), B0.3(a), (c), (d), (e) and Proposition 2.5, and Q4 N0, N1 and outcome (iii), on which §§2.2–2.3, the narrowed §1.4 and §3 rest | [D], model-reviewed | exact finite controls, or an independent non-model mathematical review | #1049 | A5-LA §7's exact controls run under a separate owner authorization (CI-scale), with green controls, for R2, R3, R6, R7 and Proposition 2.6(c); exact controls for B0.3, Proposition 2.5 and Q4 N0, N1 and outcome (iii), which A5-LA §7 does not cover; or a recorded independent review |
| V-2. Whether every consumer's use of b = 0 reduces to the resonant uniform A₁ locus (Q-β; §1.4, §3) | not traced on `main` | the b-consumption trace of §5 | #1049, coordinated with #1169 (POSIT-MIN D1(b)) | the §5 trace under a separate owner authorization, independently reviewed; landing #1226 solely to resolve this dependency is not authorized (owner decision, §7.9) |
| V-3. Q4b (rule or coupling stabilizer; linear or affine elements) and Q4c (A₁ resonance on the maintained branch) | open owner questions; Q4c also conditional on SM:232's unproved bridge from φ to L_obs | owner decisions; for Q4c, a proof of the bridge or a decision on the maintained branch | #1049 | owner decisions on Q4b and Q4c; a derivation of φ → L_obs |
| V-4. The [A] steps of §1.1 (no `Rule` gives a `Fin 2` theory) and §2.2 (labelled one-step difference at every κ) | hand algebra in this report, model-reviewed | an independent check | #1049 | an exhaustive finite computation on named cases (S1; A5-LA B0.3(f)) under a separate authorization, or a recorded independent review |
| V-5. The [W] steps: the N3 addition (§2.1), the encoding step for an encoded qubit (§1.1, §2.4), and rule-derived interfaces (OA-1 D6) | [W], model-reviewed | a derivation at [D] or better, with review | #1049 for the N3 addition and the encoding step; #1169 for OA-1 D6 | a written derivation per encoding, independently reviewed; OA-1's own remediation |
| V-6. Q-α, whether the update is affine (§1.4) | open; turns on owner decision POSIT-MIN D2 | the owner decision; for a non-affine answer, a check of A6's formal interface for the additivity it types in | #1169 | owner decision D2; a check of `linkF : V →+ V` against the selected class |
| V-7. Embedded-apparatus readouts automatically relational (§2.2) | conjecture | a derivation | #1049 | a paper derivation, independently reviewed, or a counterexample |
| V-8. SM:587 candidate inaccuracy (§6 item 1) | [A], moderate confidence | an independent check and a manuscript decision | #1029 | a recorded independent check; the manuscript correction or its rejection under #1029 |
| V-9. [background] statements (§2, §2.4) | literature not retrieved | retrieval and citation | #1049 | the cited sources read and recorded |
| V-10. Per-claim remediation plans for the A5 records that landed before §A.46 item 8 (§1.3 item 3) | administrative; none found in §A.46 item 4 form | a mutable record on `main` carrying them | #1049 | that record, reviewed |

### 7.7 Preservation rationale

The record is kept on `main` because it answers the owner's three questions for #1049 at the stated scope from records already on `main`, and because its new steps (§7.1) and its identification of the residual locus and of the open decisions (§7.6 V-2, V-3, V-6) are not stated elsewhere on `main`. Preservation establishes no claim (§A.46 item 1). REPORT.md (r1), REPORT-r2.md, REPORT-r3.md and REPORT-r4.md are kept with superseded notices as the research history; this revision, REPORT-r5.md, is authoritative, and CHANGES-r2.md, CHANGES-r3.md, CHANGES-r4.md and CHANGES-r5.md record the corrections. Merging the record into `main` needs a separate recorded owner decision (§A.46 item 8; §A.50 item 1).

### 7.8 Trace of references to content not on `main` (§A.42 item 8)

Each reference was classified by reading the claim it is attached to. Commits marked "on `main`" were checked as ancestors of `e2e2a623`.

| Reference | Where | Classification |
|---|---|---|
| r5: file `ASSESS-1049.md` on branch `research/a5-reassessment-r5-1049-20261110`, draft PR #1226 | §0 (sources read; revision r4 line) | provenance: records what was read and its standing |
| r5's P1 witnesses and GA7-α recovery | §1.1, last bullet | provenance: the bullet states their standing and that they are not support; no conclusion uses them |
| r5 | §6, limitations | provenance |
| commits `2d9bb8d1` (r5's model-reviewed head) and `f1a8f1a5` (branch head), not on `main` | §0 sources | provenance |
| #1049 comment 6624263637 (owner decisions Q1, Q2; A5 stays a posit) | §0, §1.4, §2 | support on `main`: the decisions are quoted with author and time in A5-LA §6 (Q1) and in Q4 before §1 and at §5 (Q2; "Retain linearity as a posit") |
| #1049 comments 6626401398 and 6718344623; #1083 comments 6622660127, 6718252075, 6718263472, 6718607630 and 6718644099 | §1.3 | provenance: review history; the reviewed commits `645bae17`, `f07f55d0`, `22ad8d69`, `0e7e412a` and the merge `9e0560d8` are on `main`, and no claim rests on the comments alone |
| #1049 comment 7163815560 (owner's three-question framing) | §7.1 | provenance: defines the questions; no result uses it |
| PR #1561 comments 7166779576 and 7167108875, the r3 delta review (PR #1561 comment {{ID:1561-r3}}) and the r4 delta review (not yet recorded on GitHub) | §0, §7.3 | provenance for every scientific claim; evidence of review for §A.46 item 8 |
| #1169 comments 7166418469, 7166845267 (the owner decision applied in r2), 7167242160, 7167657546 and {{ID:c29}} | §0, §7.3, §7.9 | provenance: authority records for the revisions; no result uses them |
| #1558 (the hypothesis assessed in §2.4) | §2.4, §3 | provenance: the object of assessment, not support |
| #914, #1029, #1043, #1169 | §§1, 5, 6, 7.6 | provenance: routing and accountability |
| commits `8aef91cf`, `0c058645`, `389d6ea4`, `46e82783` (reviewed revision heads, PR #1561 branch) | §7.3 | provenance |
| commits `45eea51d`, `25384b13`, `a4a1e5bb`, `8de75f7c`, `1609dc44` | §0, §1.3, §1.4 | on `main` |

Support off `main`: none.

### 7.9 Status of r4

WIP / UNVERIFIED research record, revision r4, written under the owner decision (amaybaum, 2026-11-25, #1169 comment 7167657546): "#1049 | Narrow the three passages to support available on main. Retain r5 as provenance only, not acceptance support."; "Both | Add the preservation rationale and remediation plan required by §A.46 item 8."; "Keep r1 and r2 with explicit superseded notices. Each notice should identify the authoritative revision and its corresponding correction record. Preserving the research history is valuable, provided obsolete conclusions cannot be mistaken for current results."; "Do not land #1226 merely to resolve the #1049 dependency when the narrower, independently supported conclusions are sufficient."; "Obtain bounded independent reviews and fresh CI at the corrected heads."
