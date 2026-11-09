# Review of OI-SM-QM-BRIDGE unit 1, revision r3 (BRIDGE-UNIT1.md)

**Reviewer.** A fresh, independent reviewer (Claude Code subagent, 2026-11-09). The review is
paper-only and full-text. It made no git write, GitHub write or Lean action, and no manuscript
change. This review authorizes nothing. A review ACCEPT would not authorize a freeze, an
implementation, a manuscript change or a merge (#1211 c.6738806776). The two owner decisions of
c.6740537555 that take effect on an ACCEPT, tracking the complex structure as its own item and the
correction unit, are not triggered by this review, because its verdict is REVISE.

**Objects.** Hashes were verified before reading.
- `BRIDGE-UNIT1.md` (r3): `ee1c83c04366ea62c73b3d256e44e8e7415e3561b9a0a5a7576a278892038219`, read
  in full (1068 lines).
- `DISPOSITIONS-UNIT1-r3.md`: `4d6867f0380e6708dc83674ff1b980ce082f02fe641dc7906df47c8c2e887414`.
- `r2/BRIDGE-UNIT1.md`: `3905569b…`.
- `review/REVIEW-UNIT1-r2.md`: `3cdf7dc2…`.
- `review/REVIEW-UNIT1.md`: `e242a794…`.
- `probes/r3_generic_checks.py`: `6489694c…`.
- `NOTES-r3-parallel-gaps.md`: `cb439009…16ce`. These are the writer's proposed r4 changes C1–C5,
  sent by the coordinator during the review. They were verified as the writer's own claims and
  were not adopted (§4).

**Owner records**, read with `gh api`:
- #1211 c.6738806776 and c.6739843458;
- #1211 c.6740537555, the five questions, quoted verbatim;
- #1169 c.6740778880, the parallel presentation of the three gaps and the three distinctions.

**Sources.** Read with `git show fd539e15:<path>` after `git fetch origin main`
(`fd539e150759a6ea51ab279aeeac80fc06050ade`). No working copies were written.

**Verdict: REVISE.** Every r2 finding is fixed correctly (§1), and the partial refusal of RB2 is
correct (§1.1). Claim (a) is verified (§5). There are five blockers:
- **B1.** The owner's parallel presentation is only partly met; the writer's own notes say the
  same.
- **B2.** The independence of the phase is overgeneralized from the layer flow to state mixing in
  general.
- **B3.** FI-1 is said to rest on site factorization and the second-order form. The kernel results
  it cites use neither.
- **B4.** NQ1's scope guard over $\mathbb Z_q$ is false. It has been present since r1 and is now
  repeated in §5.2.
- **B5.** The lift formulations that land are labelled "excluded", which is stronger than the
  verdict the lift-source audit's scope amendment allows.

There are eleven nits.

***

## 1. The r2 findings

| Item | Fixed in r3 | Correct against source |
|---|---|---|
| RB1 | §0 item 8; §5.1 *Position*; §10's FI-1 label; §11 | Yes. `obligations_independent` (C5Discovery.lean:59) states the phase without the flow in `substratumTheory (Fin 2)`, and the flow without the phase in `onesTheory (Fin 2)`. `exec-source-audit.md`:297: "two named assumptions, the phase intervention and the executability". `PolC` is cited as the countermodel to sufficiency (`polarizedTheoryC_derivedOI` :606, `polarizedTheoryC_not_layerFlowExecutable` :389, `polarizedTheoryC_not_qm` :620). "Weakest … therefore" is gone (grep). The scope of the stated independence is the subject of B2. |
| RB2 | FI-1 is restated on $S\times\mathrm{Fin}\,1$; "exact finite endomorphic … within the structural architecture" is restored; the encoded and finite-accuracy sentence is added | Yes. ExecSource.lean:52 gives the witness `K : Matrix (S × Fin 1) (S × Fin 1) ℂ`. Main:566, Main:584 and Main:600 are read correctly. The partial refusal is assessed in §1.1. |
| RB3 | §5.1 *Status* | Yes. `obsTheory := permTheory 𝒮.Conf` (SubstratumInterfaceAudit.lean:770); `obs_availExt_le_substratum` (:837); `substratumClass := IsMonomial` (StructuralClosure.lean:180); the exec-source scope amendment is quoted verbatim; `availExt_bind` (OperationalAssembly.lean:617) is a field of every theory; QP:851–863. "Adaptive" is removed. The four candidates include C5 candidate 2 (`hadamard_not_monomial` C5Discovery:162, `polGen_not_configurationLevel` :242). The layer-flow negatives are correctly withheld from ¬FI-1. |
| n1 | l.384–388 | Yes (K2; `gateFlow_half_not_preservesDiag`, LiftAudit). |
| n2 | §5.1(d) | Yes (Main:556 "entries are 0 or 1"; QP:855; K3). |
| n3 | §6 Born row | Yes. "Which presupposes" replaces "equivalently". |
| n4 | §0 item 8; §5.1 candidate 1 | Yes. Both gaps are stated (SM:232; GR:270). |
| n5 | *Closest derived objects* | Yes. `SecondOrderCircuit`, `SwapLayer` and `SecondOrderLayer` exist; `gateFlow_not_monomial` is at CoherentContinuumSource:74; `driveQ_isContinuousPath` is at SecondOrderDrive:225. |
| n6 | §9 | Yes. It now matches the header. |
| n7 | F8 | Yes. The qualifier is quoted, and the reason the finding stands is given. |
| n8 | §4 counts | Yes. D-partial is 4, with B9 listed. |
| n9 | Header; §13 | Yes. Every identifier listed exists at the cited file and line, with one exception: `availExt_bind` is a structure field at :617, as stated. |
| n10 | §5.1(e) | Yes. |

### 1.1 The partial refusal of RB2 is correct

The r2 review asked for "with the phase stated" wherever FI-1's necessity is stated. The kernel
does not need the phase for the necessity:
- `exists_nonMonomial_of_layerFlowExecutable` (ExecSource.lean:52) has hypotheses only on the
  architecture, a moved configuration and executability.
- `layerFlowExecutable_of_control` (LiftAudit.lean:117) needs only `HasCompositeUnitaryControl`,
  which `physical_of_exactAll` supplies from exact QM. `derivedOI_qm_iff_layerFlowExecutable'`'s
  forward direction uses exactly this route (DerivedQ3.lean:222–227).
- `uncountableNonMonomialRays_of_qm` (CoherentContinuumSource.lean:195) composes
  `derivedOI_layerFlowExecutable_of_qm` with T2. It has no phase hypothesis.

The r2 request was too broad. The phase is used for the converse direction, for the equivalence
and for FI-1's position as "first", and r3 attaches it there (l.402–405).

Two scope facts r3 should carry (nit n2):
- The necessity holds for a theory generated by an architecture (`genTheory 𝓘 arch S`). This is
  what "within the structural architecture" means.
- `uncountableNonMonomialRays_of_qm` is stated on `Fin 2`. The general-carrier form follows by
  the same composition, but that composition is not stated as a theorem.

***

## 2. Blockers

### B1. The parallel presentation that #1169 c.6740778880 requires is only partly met

The owner directs: "presents phase, FI-1 and H-Bell in parallel. Each gap states its carrier and
scope", with three distinctions. r3 meets this in part:
- **Met.** FI-1's carrier and scope are exact. The three gaps are named as unordered (§0 item 8,
  §5.1(b)–(c), §5.2).
- **Not met: the phase.** Its carrier and scope appear only in §6's phases row and §5.1(b).
- **Not met: H-Bell.** H-Bell's carrier and scope are stated nowhere. Where H-Bell is
  characterized ("H-Bell concerns outcome statistics", l.126–127), the description omits
  condition (iii), curvature stability (Sub:133).
- **Not met: the distinctions.** None of the three distinctions is stated as a distinction. The
  content is scattered (§5.1 *Scope of necessity*, *Closest derived objects*; §5.2 arrows 3–4).

The writer's `NOTES-r3-parallel-gaps.md` reaches the same conclusion.

*Required.* Adopt the writer's C1–C4, corrected as §4 sets out, and with B2's correction in the
third distinction.

### B2. The phase is independent of the layer flow, not of state mixing in general

These passages state the following:
- §5.2 arrow 3: "The phase is an input beside mixing, not an output of it".
- §5.2 summary: "two independent obligations, the phase and the flow".
- C1, third distinction: "Even with FI-1 and the flow, exact QM follows only with the phase as
  well".

The kernel proves independence between O1 (`PhasesAvailable`) and O2 (`LayerFlowExecutable`),
witnessed on `Fin 2`. The witness theory `onesTheory` executes every layer flow and lacks the phase
because every gate flow fixes the all-ones ray, and the phase requires an operator that moves it
(GR:260; `onesFixing_not_phasesAvailable`, PhaseSource.lean:53).

The corpus also states a mixing resource of another form that supplies the phase:
- GR:250 and GR:256 (with Main:590): "phase-free richness" (a continuously drivable pair and the
  exchanges, "No phase operation enters"), with implementation locality and embedded observation,
  is equivalent to exact finite endomorphic operational QM.
- GR:258: "the quarter phase is dispensable at every level". The imaginary transitions arise as
  brackets of drives that share a state (GR:250, `bracket_XX`).
- `c5-discovery-audit.md`:18–48 frames outcome A as one condition sourcing both O1 and O2.

So a continuous state-mixing operation that moves the all-ones ray would discharge the phase
obligation, while the layer flow does not. Reviewer check R5 illustrates the operator-level fact:
- a driven transition at angle $\pi/4$ on three states is non-monomial *and* moves the all-ones
  ray;
- the exchange's gate flow at $t=1/2$ is non-monomial and fixes it.

The two necessary conditions (FI-1; an operator moving the all-ones ray) are independent, as the
writer's K4 shows, but one operator can meet both.

*Required.*
- State the independence as O1 versus O2, the layer flow, on the two-state witnesses.
- Replace "the phase is an input beside mixing" with that scoped statement, and add the
  phase-free-richness route (GR:250–258) as the mixing form under which the phase is not a
  separate input.
- Carry the same scope into §0 item 8, §5.1(b), the §5.2 summary, §11's last bullet and C1.

This bears directly on the owner's "promising common research target": whether state mixing is
shared with the phase depends on whether the mixing resource fixes the all-ones ray.

### B3. FI-1 is said to rest on site factorization and the second-order form; the cited kernel results use neither

The passages:
- §5.1 *Conditionality* (l.390–397): FI-1 "is posed on stipulated inputs … the site
  factorization (B4; the kernel's `Substratum` is site-factorized …) … and the second-order form".
- §5.2 *earliest unproved assumption* (l.528–532): "the access posits (P1–P3, E-iso, the
  read/write access) are stated on the cells of that factorization … All of these are upstream of
  FI-1, which is posed on them".
- §0 item 8 (l.130–131).

The kernel facts:
- The read/write access is `ReadWriteFamily (a b : S)`, a permutation family supported on two
  *states* of an arbitrary finite carrier (ReadWriteControl.lean:86–89). It is not defined on
  cells or sites.
- `permTheory A` is defined for every finite `A`.
- `obsTheory_rule_independent` says the observer theory depends only on the configuration set.
- `exists_nonMonomial_of_layerFlowExecutable` and `layerFlowExecutable_of_control` hold for every
  finite `S` and every involution with a moved point.
- GR:270 says the equivalence is "stated for each involution with a moved configuration, whether
  or not it is a gate of that factorization".

So FI-1's statement, its one-directional necessity and its negative under the stated read/write
access all hold on any finite configuration set with a bijection. They consume neither the site
factorization nor the second-order form.

Site factorization, and the second-order form, are upstream of other things:
- the physical identification of the carrier with lattice fields, and the choice of layers;
- the cell-based posits P1–P3, E-iso and H-PREP of class N (QP:124–176), which the kernel's FI-1
  negative does not use;
- the spatial route and S13, FI-1's candidate source 1;
- H-Bell's graph.

This matters for the distinction the owner calls "especially important". As written, §5.2 places
site factorization upstream of the mixing gap. The kernel places it upstream of the carrier's
physical reading and of the routes that might supply FI-1, not of FI-1 itself.

*Required.*
- Restate *Conditionality* and the §5.2 bullet to this effect.
- Keep the stated read/write access, defined on states, as the input the negative uses.

### B4. NQ1's scope guard over $\mathbb Z_q$ is false

The claim: "over $\mathbb Z_q$ a $J$ with $J^2=-1$ exists only where $-1$ is a square". It appears
at l.938–940, unchanged since r1 and missed by both earlier reviews, and r3 now repeats it in §5.2
row 5.

It is false on the even-rank phase space where NQ1 poses $J$. Reviewer check R1 is exact over
$\mathbb F_p$ for $p\le13$:
- $J_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ satisfies $J_0^2=-I$ for every $p$, including $p=3,7,11$.
- For the mode map $f_a=\begin{pmatrix}0&1\\-1&a\end{pmatrix}$, a symplectic $J$ commuting with
  $f_a$ with $J^2=-I$ exists exactly when $4-a^2$ is a nonzero square mod $p$. This is the
  finite-field analogue of $\sin\omega\ne0$.
- At $p=3$, $a=0$ such a $J$ exists although $-1$ is a non-square.
- At $p=5$, $a=1$ none exists although $-1$ is a square. The scalar $2I$ squares to $-I$ but has
  determinant $-1$.
- Countercontrol: none exists at the null modes $a=\pm2$.

21 of the 39 pairs $(p,a)$ with $p\in\{3,5,7,11,13\}$ contradict the stated guard.

Where the claim is used: no source states it (corpus grep: no hit). It is the writer's own claim,
and it is load-bearing only as a scope guard.

*Required.*
- Delete it from §5.2 row 5, where it plays no role in the wave-operator route.
- In NQ1, replace it with a correct statement, or simply with the point the guard serves: the
  question is posed on the real lift, and a positive answer there does not source a complex
  structure at the fundamental level.

The finite-field criterion above is computation-supported for prime $p\le13$ only. It is not
proved here, and it is not needed in the text.

### B5. "Excluded" for the lift formulations that land is stronger than the verdict the lift-source audit allows

§5.2 row 3 has "**Excluded under stated conditions** (stated access, the lift formulations that
land, …)", and row 5 has "**excluded under stated conditions** for the formulations that land".

The lift-source audit's scope amendment (`lift-source-audit.md`:250–264) records that the owner
found the stronger headline overbroad. The verdict is "stated, from here on, in the form the
kernel proves: no formulation that lands derives either target". The nonreversible L1 channels'
implementation classes are not classified, and not every Kraus realization of L2 is shown to be
configuration-level. GR:270 says the same ("whether every realization of those channels is
configuration-level is not decided"). r3 itself keeps that question open as candidate 2 of §5.1.

For the stated access, "excluded" is correct (`obs_availExt_le_substratum`, `substratumClass`
monomial). For the lift formulations it is not.

*Required.* In rows 3 and 5, write "not derived (the formulations that land derive neither
target)", and carry the undecided realization question into the same cell. Keep "excluded" for
the stated access alone. §5.1 and §0 already use "not supplied … by any stated lift formulation",
which reads as non-derivation, and those passages need no change.

***

## 3. Nits

- **n1 (§0 item 8, l.126–128; §5.1(c)).** Two problems in "H-Bell concerns outcome statistics,
  which fixed bijections realize to finite accuracy … (Main:403–406, Main:566, Main:584), so it
  does not wait on FI-1":
  - Main:566's realization has no spatial graph (Main:362: the unrestricted class reaches the PR
    box), and H-Bell (iii) is a curvature condition.
  - The non-dependence rests more firmly on H-Bell being posed within bijective dynamics
    (Sub:131, preparation-indexed adjacency on $G(x)$), which is configuration-level by
    construction. Main:566/584 then add that the statistics alone need no non-monomial operator
    at finite accuracy.

  Replace "does not wait on" with "is not derived from FI-1 and does not derive it". The wording
  "beside FI-1 … no source read derives either from the other" (l.488–491) is accurate as a
  non-derivation statement. It is not, and is not claimed to be, a kernel independence result.
- **n2 (carriers of witnesses).** The following are on `Fin 2`; say so where they are cited,
  including C1:
  - `obligations_independent`;
  - `polarizedTheoryC_derivedOI`, `_not_qm`, `_phasesAvailable`;
  - `uncountableNonMonomialRays_of_qm`.

  Refuting a universal implication needs only one carrier, so no claim changes.
- **n3 (§5.2 arrow 4).** "The typed form drops the endomorphic qualifier (Main:590)": Main:590
  states the typed form for the primitive-source equivalence (`typed_determined_of_oiPlusMin`).
  Its transfer to the layer-flow closure form is not stated. Scope it, or cite the composition.
- **n4 (writer's probe K1).** Countercontrol c2 adds the same-colour read *through an AND*, so it
  does not separate the read pattern from nonlinearity, and that separation is what the MECH-2
  attribution turns on. Reviewer check R2(ii) supplies it: a *linear* rule with one same-colour
  read breaks the split. Cite R2, or add the linear same-colour countercontrol.
- **n5 (§5.2 row 5).** "The three formulations that name anything on the carrier: the coherent
  completion, the projected observer operator and the generator reading". The audit's census
  says the generator reading L4 names no operation (D1, D2) and is tested by a countermodel
  (T4). Say instead "the three formulations the lift-source audit tests (L1, L2, L4)".
- **n6 (§6 Bell row; C1 H-Bell scope).** "Realizes the quantum Bell set" is a gloss. The sources
  state H-Bell's target as the ontic parameter dependence that M1-B requires for the observed
  violation E2, with (i)–(iii) (Sub:129, Sub:131, Sub:133). Use the source wording. See §4 on
  exactness.
- **n7 (C1, H-Bell row).** MECH-2's Proposition B / M-FIX (MECH-2 DESIGN:543–567, verified) is
  "a necessary condition derived from H-Bell", a constraint on any H-Bell mechanism, not progress
  toward one. Place it under constraints, with the record's standing ("promotes no claim").
- **n8 (C2).** "There is no single earliest missing mechanism" asserts more than the sources show.
  Write "The sources read establish no order among three missing mechanisms" (Code Review Rules,
  negative results scoped to what is ruled out).
- **n9 (C1 opening).** "State mixing is a common research target" should be attributed: it is the
  owner's provisional characterization ("promising common research target"; "the shared-gap
  convergence remains provisional", #1169 c.6740778880). Whether it is shared is the dependency
  matrix's question, and B2 bears on it.
- **n10 (§12 Q1–Q2).** Both questions were answered in c.6740537555. The complex structure is to
  be tracked independently "if the review confirms it is an additional premise", and the
  correction unit is "Yes … after the audit". Both take effect only on an ACCEPT. Record the
  answers and their condition instead of asking again.
  - For the condition: this review confirms, as the r1 and r2 reviews did, that the complex
    structure is a premise of Theorem 5 that SM:340–342 does not list (F4; C1/C2 checks re-read).
- **n11 (H-Bell row of C1; §0).** H-Bell is described as "Configuration (ontic) level … with
  diagonal outcome statistics". Add that (iii) is a geometric condition on the prepared graph
  family (Sub:133), so H-Bell is not an outcome-statistics condition alone.

***

## 4. The writer's proposed r4 changes C1–C5

| Change | Needed | Correct as proposed | Corrections |
|---|---|---|---|
| C1, new §5.3 table and the three distinctions | Yes (B1) | Mostly. Phase row: `obs_not_phasesAvailable` fails at level 2 (SubstratumInterfaceAudit.lean:668); `onesFixing_not_phasesAvailable` fails at level 1, "unavailability at every composite level … not separately proved" (PhaseSource.lean:53–55); `phase_monomial` (SubstratumInterface.lean:102); `polarizedTheoryC_phasesAvailable` (PolarizationClosure.lean:448, `Fin 2`). All verified. FI-1 row: verified, apart from carriers. H-Bell row: Main:362, Main:416, Main:429 and Sub:131–133 are verified. | B2 in the third distinction and the opening; B3 if site factorization is listed; n2 carriers; n6 source wording for H-Bell's scope; n7 M-FIX placement; n9 attribution; n11. In the phase row's scope, "exact, finite, endomorphic (kernel predicate)" misdescribes `PhasesAvailable`, which is the quarter phase on every state at every level and is not an exactness predicate. State that as the carrier and scope, and note that exact QM implies it (`derivedOI_of_qm`). |
| C2, §5.2 "earliest missing mechanism" | Yes | Yes, with n8's wording | Add B2: under phase-free richness the phase is not a separate missing mechanism. |
| C3, §11 last bullet | Yes | Yes | Same scope as B2. |
| C4, §0 cross-reference | Yes | Yes | — |
| C5, dispositions | Yes | — | Also trace B1–B5 and n1–n11. |

**The open question on H-Bell's target: exact or finite-accuracy realization?** The sources state
no exactness qualifier. H-Bell's target is the observed violation E2, through M1-B (Sub:129,
Sub:131). That target is empirical and has finite precision, so the finite-accuracy reading is the
one faithful to the sources.

The reviewer adds one generic observation, which bounds the question without answering it.
Under the counting measure (B3; Main:56), every probability a finite realization produces is a
ratio of counts and therefore rational. So:
- The Tsirelson-point law, whose $P(a{=}b)=(2+\sqrt2)/4$ is irrational, cannot be realized
  exactly by any finite realization of that kind.
- Exactly rational quantum laws that violate CHSH do exist. Reviewer check R4 gives one with a
  maximally entangled state, $\cos\alpha=4/5$, all 16 probabilities rational, no-signalling, and
  CHSH $=344/125$.
- So an "exact" reading of H-Bell would exclude part of the quantum Bell set, though not every
  violation.

This is [A] for the rationality argument, and computation-supported for the witness. It relates
to Main:564's classical-dimension obstruction and is offered as ELABORATING, not as a finding for
the text. If r4 records the question, it should label this bound as reviewer-supplied.

***

## 5. Claim (a): the read pattern, not linearity

The claim is verified.
- **G1.** QP:254–257 uses only which sites the update reads. With "a function of" in place of
  "a linear combination of", the induction goes through unchanged. Reviewer check R2 runs on
  $K_{2,3}$, a different graph from the writer's:
  - a nonlinear rule with opposite-colour reads keeps the split, and the rule is shown non-affine;
  - a *linear* rule with one same-colour read breaks it;
  - so does a nonlinear rule with the same read;
  - the linear rule with opposite-colour reads is the control.
- **G2.** Step 3 (QP:366–368) needs only $F(y+ce)-F(y)$ to be independent of $y$, which affinity
  gives (R3, with an AND countercontrol).
- **SM:569.** $\Gamma A\Gamma=-A$ excludes same-sublattice and diagonal entries, so the shared
  premise is the read pattern.
- **The MECH-2 attribution.**
  - MECH-2:530–534 reads "whose nonlinearity breaks the grading".
  - Apparatus-1's type grading (apparatus-1 DESIGN §4.2, read for this review) is the slot-type
    statement. On a functional reading it is the same sector split.
  - $f_i(u)=u_{i-1}\oplus(u_{i+1}\vee u_{i+2})$ breaks it at $u_{i+2}$, the same-colour read.
    The rule depends on that read whenever $u_{i+1}=0$.

  The correction of the attribution is therefore right.

What is not claimed is also stated correctly: G1's Lagrangian consequences, and apparatus-1's
exclusion of $Y_\pm$ *states*, are not claimed to survive. The record's conclusion is unaffected.

The ELABORATING label is right. A corpus grep for grading together with
nonlinear/same-colour/read-pattern finds only MECH-2:532.

***

## 6. §5.2, question by question

| Question | r3 answer and status | Assessment |
|---|---|---|
| Site factorization | Assumed; derivability open (SM:68; Main:726 (viii)) | Correct (SM:68 and Main:726 (viii) verified). Main:726 also calls (viii) "foundational", with (ix)–(xi) and (xiii) stated relative to it. Its placement upstream of FI-1 is wrong (B3). |
| Observer read/write access | Assumed; sufficiency for the target excluded under stated conditions | Correct. `obs_not_phasesAvailable`, `obs_not_layerFlowExecutable` and `obs_not_derivedOI` are proved, `prepAvail_uniform` is the only preparation, and P1–P3 are supplied posits (QP:173). |
| Non-monomial mixing | Excluded under stated conditions; open for four candidates | Correct for the stated access. "Excluded" for the lift formulations is too strong (B5). "Without importing quantum operations" is answered: every construction on `main` that has it adds it. |
| Existing results | Open; none closes the gap under the same hypotheses | Correct against the outcome sections of the six foundations audits. Each verdict quoted matches (exec-source :236–300; lift-source :250–290; C5 :228–233, verdict C; polarization :216–237, split; coherent-continuum :220–277, outcome 2; state-mixing :227–280, outcome 1 from a postulated datum, `mixTheory_qm` StateMixingCoupling:511). |
| SM wave-operator route | Open; excluded for the formulations that land | "Open" is correct (SM:232; GR:270; coherent-continuum S7: "unresolved rather than excluded"). The second status needs B5's wording, the $\mathbb Z_q$ sentence must go (B4), and n5 applies. |

**The two notions of "earliest"** are kept apart in form, but B3 misplaces site factorization
relative to FI-1. Once corrected:
- *Earliest unproved assumptions.* B1–B3, then the stated read/write access with the phase, which
  are what FI-1's negative uses. Separately, site factorization with the second-order form is
  upstream of the physical carrier, the cell-based posits, the spatial route, S13 and H-Bell.
- *Earliest missing mechanism.* Per C2 and B2.

**The necessity check the owner requires.** For the representation and target audited, a
configuration carrier at level one and exact finite endomorphic operational QM generated by an
architecture, FI-1 is necessary, by `exists_nonMonomial_of_layerFlowExecutable` composed with
`layerFlowExecutable_of_control`. It is not necessary:
- for finite-accuracy reproduction (Main:566, Main:584, Main:600);
- on encoded carriers (QP NNB; MECH-2 U2).

r3 states this, and §5.2's one-sentence scope (l.542–544) does not become a universal claim. The
one universality gap is B2: the *phase's* independence is stated for "mixing" in general.

**The arrow-by-arrow table.**
- Arrow 1 is correct: only converse necessity is proved.
- Arrow 2 is correct.
- Arrow 3 overreaches (B2).
- Arrow 4 is correct with n3.
- "A branching structure, not a chain" is supported, with B2's qualification: under phase-free
  richness the phase branch merges into the mixing branch.

***

## 7. Other checks

- **The three gaps.** State mixing is never called the universally earliest gap. FI-1 is "first"
  only "once the phase is taken as stated" (l.138, l.485, l.983). H-Bell's wording is accurate as
  non-derivation (n1). "Only phase/flow independence is kernel-proved" is accurate.
- **The three distinctions.** Their content is present: §5.1 *Scope of necessity* (encoded
  carriers), *Closest derived objects* (availability versus derivation), §5.2 arrows 3–4. None is
  stated as a distinction (B1), and the third must carry B2.
- **The three-column separation.** It holds in B1–B27, §6, §9 and the new §5.2. Column (iii) is
  never support.
- **The §A.31 labels.** These are right: Q6 connection, Q6 shared premise, F1, F4, F5 and F8
  ELABORATING; FI-1 and the others CONFIRMING; nothing NEW.
- **Authorization.** Nothing implies one:
  - the header quotes c.6738806776 and c.6739843458;
  - every manuscript finding is "recorded only";
  - §12 asks and does not act, apart from n10's stale questions;
  - unit 2 is not selected;
  - the checks are generic.
- **New errors elsewhere.** None beyond B2–B5 and the nits. §3, §4, F1–F11 and §10's other
  bullets are unchanged from r2 and were spot-checked.

***

## 8. Exact checks

**The writer's probe.** `python3 -I probes/r3_generic_checks.py` was re-run. Its output is
byte-identical to `probes/r3_generic_checks.out` (`d85a1a9f…`; copy at
`review/probes/r3_generic_checks.rerun.out`). All 14 checks pass.
- The controls are non-vacuous: K1 has a non-affine witness and two countercontrols, and K3 and
  K4 compare distinct cases.
- K1's c2 does not isolate linearity (n4).

**Reviewer probe** `review/probes/r3rev_checks.py`.
- Hashes: script `5aff65f5743421986ba723624447f30c74f67dd08bf61cdb8d7ed1708768b9b9`; output
  `r3rev_checks.out` `42a9a59581b5402e0f847319ab29ceaff6f35f0ad331bcbc428314f31e66d36a`. All 25
  checks pass.
- Method: exact arithmetic only (integers mod $p$, $\mathbb F_2$, sympy rationals) on generic
  objects. It imports no earlier script and runs no OI mechanism, under c.6739843458.
- Results:
  - **R1:** the $\mathbb Z_q$ scope guard, with a null-mode countercontrol (B4).
  - **R2:** the sector split, separating the read pattern from nonlinearity on $K_{2,3}$ (§5, n4).
  - **R3:** affinity in G2 step 3, with an AND countercontrol.
  - **R4:** a rational quantum CHSH violation, and the irrational Tsirelson point (§4).
  - **R5:** a drive that is non-monomial and moves the all-ones ray, against a ones-fixing gate
    flow (B2).

  These are witnesses and controls for algebra stated here. No verdict rests on them alone.

***

## 9. What r4 needs for ACCEPT

1. B1: §5.3 per C1, as corrected in §4, together with C2–C4.
2. B2: scope the phase's independence to the layer flow, and add the phase-free-richness route.
3. B3: remove site factorization and the second-order form as premises of FI-1, and place them
   where they act.
4. B4: delete or correct the $\mathbb Z_q$ scope guard (§5.2 row 5; NQ1).
5. B5: replace "excluded" for the lift formulations that land with "not derived", carrying the
   undecided realizations.
6. n1–n11.

The changes are confined to §0 item 8, §5.1 *Conditionality*/*Position*, §5.2, the new §5.3,
§6's Bell row, §11 and §12. A delta review of those passages is enough if nothing else changes.
