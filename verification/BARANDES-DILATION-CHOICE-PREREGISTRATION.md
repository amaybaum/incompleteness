# Track B act 7 — the dilation-choice round: preregistration

Frozen before any execution. Blob identity is authoritative.

Source identities per act 1's frozen table: **A** = *The Stochastic-Quantum Correspondence*,
arXiv:2302.10778v3; **B** = arXiv:2507.21192v1; **C** = *The Stochastic-Quantum Theorem*,
arXiv:2309.03085v2. **Only Source A is adjudicated in this round.** Every coordinate is read off act
5's **authoritative surface**: the PDF of arXiv:2302.10778v3, which self-identifies by its p. 1 stamp
`arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`. The arXiv HTML rendering numbers differently and is
**not** an admissible surface.

Executed from `main` at `375e8cd50e2fc916ff96dd45ce072a1a2fdf63e4`, the merge of act 6 (PR #571).

## The question

Act 6 closed at `(TI1, UB2)`. `UB2` refutes `DirectBranch` by one exhibited lawful witness, so a
correspondence covering **all** of `PPer` cannot stay entirely on Source A's direct unistochastic
branch and must handle the **dilated** branch for the off-direct members. Directly unistochastic
members remain eligible for the direct branch; `UB2` classifies nothing beyond its witness.

This round asks the next question, and only it:

> For an OI/`PPer` process off the direct branch, does Source A's dilation contain free choices that
> move the **visible** candidate — not merely the hidden carrier or the unitary representing it?

## Two layers, and they are SEQUENTIAL rather than orthogonal

Act 6's two layers were independent and reported as a pair. **This round's are not**, and the
difference is deliberate. Layer 2 is meaningful only if layer 1 establishes that Source A's dilation
accepts our data and that the source itself forms a visible candidate from the dilated object. If it
does not, the round **stops at layer 1 and reports that**, rather than constructing something
broader on the source's behalf.

### The stop table

| Layer 1 finding | Layer 2 | Outcome |
| --- | --- | --- |
| §3.4's input contract is not met by the off-direct witness | **not reached** | `DC2a` |
| Input contract met, but the source forms no visible candidate from the dilated object | **not reached** | `DC2b` |
| Input contract met and a visible candidate is formed | executed | `DC1`, `DC3` or `DC4` |

*Not reached* and *unresolved* are different statuses and are never interchanged, per act 5's
discipline. Under `DC2a` and `DC2b` the layer-2 questions are recorded **not reached — the source
layer stopped the round**, never *unresolved*.

## Why this round is on the critical path

Act 3 (`CU1a`) established that the representation does not select the candidate. Act 4 (`MP4`)
found Source C's construction produces no intermediate candidate at all. Act 5 (`SA2`) found Source
A **does** form one, load-bearing for its interference formula, but computes it from a unitary lift
the visible data does not fix — exhibited at the visible level as the identity against the swap.
Act 6 (`UB2`) then put the full-class route onto the branch act 5 scoped out.

So the dilation is the one unexamined step on which a full-class `OI → QM` statement now depends,
and act 5 recorded its freedom (`F4`, the Stinespring dilation freedom) as **scoped, not dismissed**
precisely against this round.

**What the answer would mean.** If every source-admissible dilation of a fixed off-direct OI process
yields the same visible candidate, the freedom is representation freedom and a strong conditional
`OI → QM` statement stays reachable. If two admissible dilations yield different visible candidates,
then OI plus Source A's construction does not determine the visible prediction, and the reachable
statement is `OI + a named selection principle ⇒ QM` rather than `OI ⇔ QM`. Either answer is a
result. Neither is assumed here.

## Layer 1 — the source reading

**Evidence level 3** (act 1's hierarchy): a reading of the accepted text, not a theorem. Executed
**before** any Lean, and its findings are what layer 2's definitions are transcribed from.

Six questions, each answered with exact equation and page coordinates on the authoritative surface,
or answered *not determinable from the text* — which is itself an answer and is recorded as one.

**D1 — what object is dilated.** Exactly which object does §3.4, p. 10 take as input: the visible
transition family `Γ`, the potential matrix `Θ(t ← 0)`, or something else? Quote the defining
sentence.

**D2 — what the input contract is.** What hypotheses does §3.4 require of that object? List them
individually. State, for each, whether a general row-stochastic-only `PPer` family satisfies it.
**If any hypothesis fails, the round stops at `DC2a` with that hypothesis named.**

**D3 — what is free in the completion.** Enumerate every choice the construction leaves open:
carrier dimension, the completion's free block, phases, ordering, anything else. Each freedom is
recorded as *examined* or *not examined*, per act 5's discipline — absence is never silent.

**D4 — what consumes the dilation downstream.** Which subsequent equations use the dilated object?
In particular: **does any equation form the relative operator (39) from the DILATED unitary, and
does any equation read a candidate back onto the original visible carrier?** If the source never
does, the round stops at `DC2b`: forming that composite would be constructing on the source's
behalf, which act 4 declined to do and this round declines likewise.

**D5 — is the dilation padding-like in act 3's sense?** Act 3 proved
`candidateOf_uniformWeight_padData_eq`: tensoring an **arbitrary** finite ancilla with an arbitrary
unitary and weight leaves the induced candidate **unmoved**, because the ancilla marginalizes at
every horizon. So if §3.4's dilation is of that shape, a merged theorem already bears on the answer
and `DC3`/`DC4` is the live branch. If it is not — if it alters the visible block rather than
tensoring beside it — `DC1` is live. Determine which, with coordinates. **This question must be
answered before any witness is examined**, so that the answer is not selected by the outcome.

**D6 — does the source itself acknowledge the freedom.** Record whether §3.4 or its surroundings say
anything about non-uniqueness of the completion, as act 5 recorded p. 7's "not unique" and footnote
6. Corroboration only: no admissibility judgement may **rest** on such a remark, for the reason act
5 froze — a sentence about empirical results being unchanged can be read as restricting which
transformations count, which would make the citation circular.

## Layer 2 — the formal targets

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, `axiom` or `native_decide`.

### T1 — the visible screen

A corollary of act 6's structural lemma and act 2's bridge:

    IsUnistochastic ((Γ t)ᵀ)  →  IsRowStochastic (Γ t) ∧ IsColStochastic (Γ t)

Under `PPer` the row half is already carried, so the content is the **column** half: a `PPer` member
can lie on the direct branch only if `Γ t` is **doubly stochastic at every `t`**. This is a
**necessary** condition and the round states it as one.

**It is not sufficient, and the freeze records that here rather than leaving it to be discovered.**
At `n = 2` the two coincide, and that direction is proved **inside this round without external
citation**: every bistochastic `[[a, 1−a], [1−a, a]]` is `|U|²` entrywise for the real orthogonal

    U  =  [[√a, √(1−a)], [√(1−a), −√a]]

At `n = 3` the inclusion is **proper** — the unistochastic matrices are a proper subset of the
Birkhoff polytope — which is cited to the external literature (Bengtsson–Ericsson–Kuś–Tadej–
Życzkowski; Dunkl–Życzkowski) and **not** proved here. That citation is at act 1's evidence level 3
and the round claims it at no higher level. Nothing in this round's outcome may rest on the `n = 3`
statement; it is recorded so the screen is not over-read as a characterization.

### T2 — source admissibility, transcribed and not invented

A predicate naming exactly the hypotheses D2 returns, and nothing else.

**The binding control.** Admissibility is **transcribed from §3.4's stated hypotheses**. If the
construction turns out to need a condition the source leaves implicit, that condition is recorded as
a **finding** — a hypothesis the source does not state — and named in the result. **No condition may
be added because it makes `DC1` or `DC3` come out.** This is act 6's typed-from-the-source discipline
one act on, and it is the single most likely way this round could be quietly unfalsifiable.

### T3 — the visible readback, fixed before comparison

An explicit map carrying a candidate on the dilated carrier back to a matrix on `V`, **fixed in this
freeze's execution before either witness is examined**. No alternative projection, restriction or
marginalization convention may be introduced after seeing a result.

**And its provenance is itself reported.** If the source specifies the readback, it is transcribed
and the round runs at full strength. If the source does **not** specify one, that absence is a
recorded finding, the readback is declared **ours**, and every layer-2 outcome is reported at
**reduced strength** — because a divergence produced under a readback we chose could be an artifact
of that choice rather than of the dilation freedom. Act 3's reference points are `candidateOf` and
act 5's (42) readout; neither is adopted by default.

### T4 — two witnesses, reported separately

**Witness A** — act 6's merged family: on `Fin 2`, `Γ 0 = 1`, period `2`, and at odd times the
row-stochastic

    A  =  [[1, 0], [1, 0]]

**rank one** — it collapses both states.

**Witness B** — planned as: the same shape with

    B  =  [[1, 0], [1/2, 1/2]]

rows summing to `1`, `det = 1/2` so **full rank**, column sums `3/2` and `1/2` so **not** doubly
stochastic, hence off the direct branch by T1. **Recorded as the planned witness, not as a result**:
the execution must still prove `PPer` membership and off-direct status, and may substitute another
family meeting the same three stated properties, recording the substitution and why.

Both witnesses are lawful `PPer` families and both are lifted to a genuine `RootedRealization`
through the merged `pper_has_responseRealization`, as act 6 did.

**Why two.** Witness A is rank-one degenerate, so a dilation result on it alone could be an artifact
of rank collapse rather than a fact about the dilation. Witness B separates the two.

**Their results are reported separately and never merged.** A divergence on **either** earns the
existential positive. Agreement on **both** earns only *not exhibited on these witnesses*.

## Outcome grid — deliberately ASYMMETRIC

**`DC1` — the dilation moves the visible candidate.** Two **source-admissible** dilations of one
fixed off-direct OI witness are **exhibited**, giving **different** visible candidates under the
frozen T3 readback. Exhibition at the **visible** level, never the operator level — act 4's earned
control, load-bearing here as it was in act 5. Earned by one witness; the result names which.

**`DC2a` — the input contract fails.** §3.4 does not accept the off-direct witness, with the failed
hypothesis named. Layer 2 *not reached*.

**`DC2b` — the source forms no visible candidate from the dilated object.** The contract is met but
nothing downstream reads the dilated object back to a candidate on `V`. Layer 2 *not reached*. This
is act 4's `MP4` one branch over and is a live possibility, not a formality.

**`DC3` — no visible divergence exhibited on the tested witnesses. UNRESOLVED.**

> **`DC3` is not evidence of uniqueness, and this is the round's central control.** An unsuccessful
> search over two witnesses says nothing about all admissible dilations of all off-direct members.
> The quantifier is wrong twice over — over dilations and over members. `DC3` must be reported as
> *unresolved*, with what was tried and what would settle it, and **may not** be paraphrased as "the
> freedom is harmless", "the dilation is representation freedom", or any equivalent.

**`DC4` — visible invariance, PROVED.** A theorem quantified over **all** source-admissible
dilations of a stated class, proving the visible candidate is unmoved. A strictly stronger label than
`DC3` and reachable **only** by such a theorem. **`DC4` is never earned by an unsuccessful witness
search**, and `DC3` never upgrades to it.

**Failure to prove `DC4` is not `DC1`**, and failure to exhibit `DC1` is not `DC4`. This is act 5's
`A1` discipline and act 6's `TI2`/`UB2` discipline, stated a third time because it is the error this
programme has had to repair at every act where an existential met a universal.

## The control this round exists to protect

**An existential result and a universal result are different propositions, in both directions.**

- `UB2` is existential and is cited as such. Nothing here may restate it as a classification of the
  OI class.
- `DC1` would be existential: one pair of dilations, one witness. It would **not** show that every
  off-direct OI process has choice-dependent visible predictions.
- `DC3` is the absence of an exhibition and licenses nothing.
- `DC4` alone is universal, and only over the class its statement names.

**Act 3's padding theorem is a live and merged constraint, not a rhetorical one.**
`candidateOf_uniformWeight_padData_eq` proves that arbitrary finite-ancilla unitary padding leaves
the candidate unmoved. If D5 finds §3.4's dilation is padding-like, `DC1` is correspondingly
unlikely and the round should say so rather than hunt for a divergence its own merged corpus
forbids. If D5 finds it is not padding-like, that difference is the mechanism and must be named.

## Definition budget

The execution introduces **at most six** top-level definitions, and these are the six:

1. the source-admissible dilation predicate (T2);
2. the dilated-family carrier or datum, if the predicate cannot be stated without one;
3. the visible readback map (T3);
4. the `DC1` proposition — two admissible dilations, different visible candidates;
5. the `DC4` proposition — visible invariance over all admissible dilations;
6. the double-stochasticity screen predicate, if act 2's `IsRowStochastic`/`IsColStochastic` pair
   does not already state it without a new name.

**Witnesses are built inside the proofs that need them**, per act 3's lesson — no top-level witness
definitions. Merged definitions are consumed, never redefined. If layer 1's findings require a
seventh, that is an **append-only amendment**, separately frozen and merged before the work it
affects; it is not a licence taken at execution time.

## Mandatory controls

1. **Kernel discipline.** No `sorry`, `axiom`, `native_decide`; `#print axioms` on **every** named
   result; any new module registered in `verification/lean-manuscript-census.json` and imported in
   `OIBridge.lean`.
2. **Layer 1 before layer 2.** No Lean for the dilation is written before the source reading is
   complete, and layer 2's definitions are transcribed from D1–D6's findings.
3. **Admissibility is transcribed, not invented** (T2). Any condition the source leaves implicit is
   reported as a finding, named, and never added to make an outcome come out.
4. **The readback is fixed before either witness is examined**, and its provenance — source's or
   ours — is reported, with reduced strength in the second case (T3).
5. **Visible level, never operator level.** A divergence in dilations, unitaries or hidden carriers
   is **not** a `DC1`. Act 4's control, and act 5's exhibition burden.
6. **Per-witness reporting.** Witness A and witness B results are stated separately and never merged
   into one claim.
7. **`DC3` may not be paraphrased as uniqueness, harmlessness or representation freedom.**
8. **`DC4` is earned only by a theorem over all admissible dilations**, never by an unsuccessful
   search.
9. **Source coordinates** follow act 1's frozen table and act 5's authoritative surface, and are
   never mixed across sources. Only Source A is adjudicated; Sources B and C are not compared with it
   on any axis.
10. **The `n = 3` properness is cited, not proved**, is recorded at evidence level 3, and **no
    outcome rests on it**. The `n = 2` coincidence is proved in-round without external citation.
11. **The screen is necessary, not sufficient**, and is stated that way everywhere it appears.
12. **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are cited and never revised.** Acts
    1 through 6 are not reopened.
13. **No manuscript edit**, whatever is found.
14. **No sourcing inference.** Track separation both ways, per Amendment 2. No fifth condition, no
    deferred Arc D resource adjudicated, §3.6 not reopened.

## Non-doings

Do not: adopt or propose a candidate-selection principle; adjudicate act 5's gauge-versus-empirical
tension; prove or claim anything about interference; decide `F1` versus `F2`; claim Source A is
inapplicable on any outcome; claim the external correspondence fails; infer visible unistochasticity
from the existence of any representation; read `UB2` as a classification of the OI class; read `DC3`
as uniqueness; compare Source A with Source C on any axis; begin the `BD3` follow-up, Arc D round 2
or Arc E; edit manuscripts.

## Prediction, recorded before executing

**Layer 1 is genuinely uncertain, and `DC2b` carries real weight.** Act 4 found Source C's
construction produces no intermediate candidate at all; it would not be surprising if Source A's
**dilated** branch likewise never forms a visible relative candidate, since (39) and (42) are
introduced on the direct branch where the unitary is already at hand. That is recorded as a material
possibility rather than a formality — call it around one in three — and it is the reason D4 is asked
before any witness work.

**If layer 1 passes, the two outcomes are close to balanced, and the deciding fact is D5.** Two
merged results pull opposite ways. Act 5 exhibited a unitary-lift freedom moving the visible
candidate on the direct branch, and that same freedom sits inside any dilated unitary — which argues
for `DC1`. Act 3 proved arbitrary finite-ancilla padding leaves the candidate unmoved — which argues
for `DC3` or `DC4` if the dilation is padding-like. Which merged result governs is exactly what D5
decides, and the round is designed so that D5 is answered before the witnesses rather than after.

**The prediction is recorded at that strength and no higher.** It is not a finding. `DC1` is earned
only by an exhibited visible divergence, `DC4` only by a universal theorem, and if neither is
produced the answer is `DC3`.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`.
- Final exact-head review after the source reading, any Lean, the result note and registry updates
  are complete.
- No merge without an explicit owner direction after exact-head review, naming the exact head SHA.

## Allowed final report

1. D1–D6 answered with exact coordinates, each freedom recorded *examined* or *not examined*, and
   D5's determination stated before any witness result;
2. the admissibility predicate, with any source-implicit condition named as a finding;
3. the readback map and **whose** it is, with the strength of every layer-2 claim adjusted
   accordingly;
4. the screen T1, stated as necessary and not sufficient, with the `n = 2` proof in-round and the
   `n = 3` properness cited at evidence level 3;
5. both witnesses, their `PPer` membership and off-direct status proved, and their results
   **separately**;
6. the outcome — `DC1`, `DC2a`, `DC2b`, `DC3` or `DC4` — with the route to the label stated, since
   `DC2` has two routes and `DC3` and `DC4` must not be confused;
7. the recorded predictions and whether each held;
8. the definition count and the `#print axioms` line for every named result;
9. what remains open and what would settle it;
10. explicitly: that `UB2` is existential and is not restated as a classification; that `DC3`, if
    reached, is unresolved and not evidence of uniqueness; that no candidate-selection principle has
    been adopted; that `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are unrevised; that no outcome says
    Source A is inapplicable or that the correspondence fails; and that nothing here is a sourcing
    claim.
