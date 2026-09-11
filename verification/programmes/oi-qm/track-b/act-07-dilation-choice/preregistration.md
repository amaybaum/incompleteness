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
difference is deliberate. Layer 2 is meaningful only if layer 1 establishes both that Source A's
dilation **accepts our data** and that the source itself **forms a candidate from the dilated
unitary at all**. If either fails, the round **stops at layer 1 and reports that**, rather than
constructing something broader on the source's behalf. Whether that candidate is then brought back
to `V` is a third, separate question: it does not stop the round, it sets the **strength** at which
the round reports.

### The stop table

| Layer 1 finding | Layer 2 | Outcome |
| --- | --- | --- |
| §3.4's input contract is not met by the off-direct witness | **not reached** | `DC2a` |
| Contract met, but the source forms **no candidate at all** from the dilated unitary — not even on the dilated carrier | **not reached** | `DC2b` |
| Contract met; a candidate is formed on the dilated carrier; the source **supplies** a map back to `V` | executed at **full strength** | `DC1`, `DC3` or `DC4` |
| Contract met; a candidate is formed on the dilated carrier; the source supplies **no** map back to `V` | **paused** until an append-only amendment freezing the readback map is merged, then executed at **reduced strength** | `DC1`, `DC3` or `DC4`, each marked reduced-strength |

**The third and fourth rows are different branches and must not be run together.** `DC2b` is
reserved for the case where the source forms no candidate at all; a source that forms one on the
dilated carrier but never brings it back to `V` does **not** stop the round — it lowers the strength
of whatever the round concludes, per T3.

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

**What the answer would mean, and under which readback.** If every source-admissible dilation of a
fixed off-direct OI process yields the same visible candidate **under a readback the source itself
specifies**, the freedom is representation freedom and a strong conditional `OI → QM` statement stays
reachable. If the readback is **ours** (T3), the same finding says only that the candidate is
invariant under **our** chosen readback, which is a weaker statement and is never paraphrased as the
stronger one.

**The divergence direction is bounded the same way, and for the same reason.** If two admissible
dilations yield different visible candidates **under a readback the source itself specifies**, then
OI plus Source A's construction does not determine the visible prediction, and the reachable
statement is `OI + a named selection principle ⇒ QM` rather than `OI ⇔ QM`. **Under a readback fixed
by our own amendment the same exhibition establishes strictly less**: that two source-admissible
dilations give different outputs **under that map**. The difference could still be an artifact of the
extra map rather than of the dilation freedom, so it does not by itself show Source A's own visible
prediction underdetermined, and it does not by itself require a selection principle. Either answer is
a result at its own strength. Neither is assumed here.

## Layer 1 — the source reading

**Evidence level 3** (act 1's hierarchy): a reading of the accepted text, not a theorem. Executed
**before** any Lean, and its findings are what layer 2's definitions are transcribed from.

Six questions, each answered with exact equation and page coordinates on the authoritative surface,
or answered *not determinable from the text* — which is itself an answer and is recorded as one.

**D1 — what object is dilated.** Exactly which object does §3.4, p. 10 take as input: the visible
transition family `Γ`, the potential matrix `Θ(t ← 0)`, or something else? Quote the defining
sentence.

**D2 — what the input contract is, in Source A's own orientation and including what it inherits.**
What hypotheses does §3.4 require of that object? List them individually.

**Orientation.** Source A's stochastic matrix is in the **external column-stochastic** orientation,
which acts 2 and 6 reach through `(Γ t)ᵀ`. The contract is therefore tested against the exact
external object — `(Γ t)ᵀ`, or the `Θ` built from it — and **never** against our raw internal `Γ`.
Testing the wrong orientation would answer a different question, and act 2's `RT1` is what makes the
translation legitimate rather than assumed.

**Inherited prerequisites count.** The list is **not** limited to hypotheses §3.4 restates locally.
It must include every upstream prerequisite the construction actually needs — the time-domain and
continuity assumptions carried down from earlier sections, and whatever the `Θ`/Kraus construction
presupposes. Scoping D2 to §3.4's own sentences would be the way to miss a genuine `DC2a`.

State, for each hypothesis, whether our discrete `PPer` witness in the external orientation satisfies
it. **If any fails, the round stops at `DC2a` with that hypothesis named**, whether it is stated in
§3.4 or inherited.

**D3 — what is free in the completion, including ACROSS TIMES.** Enumerate every choice the
construction leaves open: carrier dimension, the completion's free block, phases, ordering, anything
else. Each freedom is recorded as *examined* or *not examined*, per act 5's discipline — absence is
never silent.

**And one freedom that a pointwise reading would hide.** §3.4 invokes Stinespring to obtain a dilated
unitary time-evolution operator, but the downstream candidate at (39)/(42) consumes **two** times,
through `U(t ← 0) U†(t′ ← 0)`. A pointwise existence theorem at each time is **not** the same object
as one coherently chosen time-indexed family. So D3 must ask explicitly: does the source **fix**,
**prove**, or merely **assume** cross-time coherence of the dilated family, and what regularity does
it require of it? Any freedom there is enumerated with the rest.

**This may be exactly where a dilation choice becomes load-bearing**, by act 5's own `F1` mechanism.
Two families can reproduce the **same visible stochastic matrix at every time** while differing **as
unitaries** — and then their relative operators at a pair of times differ, because the relative
operator is built from the unitaries and not from the visible matrices. That is precisely act 5's
witness: `U′(s ← 0) = U(s ← 0) D(s)` gives `|U′(s ← 0)|² = |U(s ← 0)|²` at every `s`, yet the
relative readout at `(t, t′)` is the identity from one and the swap from the other. **Note what the
sentence does not say:** families whose *unitaries* agree pointwise have identical relative objects,
trivially. The freedom lives in agreeing on the visible data while differing underneath.

**D4 — what consumes the dilation downstream, asked as TWO separate questions.** Which subsequent
equations use the dilated object? The two questions below are distinct and route
differently. Running them together would leave the execution branch ambiguous — a stop and a
strength reduction are not the same instruction — so they are asked separately and answered
separately.

**D4a — is a candidate formed from the dilated unitary at all?** Does any equation form the relative
operator (39), or any readout of (42)'s shape, from the **dilated** unitary — on the dilated carrier
or anywhere? **If the source never forms one, the round stops at `DC2b`**: building that composite
would be constructing on the source's behalf, which act 4 declined to do and this round declines
likewise.

**D4b — is that candidate brought back to the original visible carrier?** Given that a candidate is
formed on the dilated carrier, does the source supply a map returning it to `V`? **A negative answer
here does NOT stop the round.** It is recorded as a finding, our own readback is frozen per T3, and
every layer-2 outcome is reported at **reduced strength**. `DC2b` is reserved for D4a.

**D5 — is the dilation padding-like in act 3's sense, and does act 3's theorem actually reach it?**
Act 3 proved `candidateOf_uniformWeight_padData_eq`: for an **arbitrary** finite ancilla, unitary and
weight, the induced candidate is **unmoved**, because the ancilla marginalizes at every horizon.

**But that theorem is about our internal construction, and two bridge conditions must both hold
before it bears on Source A's candidate at all.** It proves invariance of `candidateOf` under the
exact `padData` tensor-product padding, at `uniformWeight` specifically. It does **not** prove
invariance of Source A's (39)/(42) relative-unitary candidate merely because §3.4 also introduces an
ancilla. So D5 returns **both** of:

- **D5a — the shape condition.** Does §3.4's dilation match `padData`'s shape: the visible carrier
  tensored with a finite ancilla, with the unitary and the weight in the form the theorem covers, the
  weight uniform? Structural resemblance is not enough; the answer names the mismatch if there is one.
- **D5b — the quantity condition.** Is the candidate-and-readback under test **identified with**, or
  **proved equivalent to**, the theorem's `candidateOf … uniformWeight`? The relative-unitary
  candidate of (39)/(42) and our `candidateOf` are different constructions until something says
  otherwise, and no merged theorem says otherwise today.

**If both hold, the merged theorem is evidence and `DC3`/`DC4` is the live branch. If either fails,
the padding theorem is recorded as an ANALOGY AND CONTROL ONLY — not evidence for `DC3` or `DC4` —
and the round proceeds with the witnesses as though it did not exist.** In no case does D5 make
`DC1` forbidden: a merged theorem about a different quantity forbids nothing about this one.

If the dilation instead alters the visible block rather than tensoring beside it, `DC1` is live.
Determine which, with coordinates. **This question must be answered before any witness is examined**,
so that the answer is not selected by the outcome.

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

A predicate naming exactly the hypotheses D2 returns, and nothing else — **stated about the external
object** `(Γ t)ᵀ` or its `Θ`, in Source A's column-stochastic orientation, matching D2. Act 2's `RT1`
is what licenses moving between orientations and is consumed, never re-proved.

**The binding control.** Admissibility is **transcribed from §3.4's stated hypotheses**. If the
construction turns out to need a condition the source leaves implicit, that condition is recorded as
a **finding** — a hypothesis the source does not state — and named in the result. **No condition may
be added because it makes `DC1` or `DC3` come out.** This is act 6's typed-from-the-source discipline
one act on, and it is the single most likely way this round could be quietly unfalsifiable.

### T3 — the visible readback, fixed before comparison

An explicit map carrying a candidate on the dilated carrier back to a matrix on `V`. **The readback
is outcome-bearing** — different restriction or marginalization conventions can create or erase a
visible divergence — so it is never an execution-time choice. No alternative convention may be
introduced after seeing a result, and none may be selected while a result is in view.

**And its provenance is itself reported.** This is D4b's branch, and it is reached only once D4a has
established that the source forms a candidate on the dilated carrier at all — if it does not, the
round has already stopped at `DC2b` and there is nothing to read back.

- **Source specifies the readback** → it is transcribed, and the round runs at **full strength**.
- **Source specifies none** → the absence is a recorded finding, and **layer 2 PAUSES**. It does not
  proceed under a map chosen at execution time. Instead:
  1. the finding is recorded;
  2. an **append-only control-plane amendment** specifying the exact readback map is written,
     reviewed and **merged** — a separate freeze, under the same split protocol as this document;
  3. only then does layer 2 resume, at **reduced strength**, under that separately frozen map.

  This keeps the reduced-strength branch available without letting the execution choose the
  observable being compared. **All three layer-2 labels are bounded by it, not only the negative
  ones.** A `DC3` or `DC4` reached that way says the candidate is unmoved **under the amendment's
  readback**, and is never paraphrased as invariance simpliciter; a `DC1` reached that way says the
  two dilations differ **under the amendment's readback**, and is never paraphrased as Source A's
  visible prediction being underdetermined or as a selection principle being required.

Act 3's reference points are `candidateOf` and act 5's (42) readout; neither is adopted by default.

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

**The execution must prove** both witnesses are lawful `PPer` families, must prove both off-direct,
and must lift both to a genuine `RootedRealization` through the merged
`pper_has_responseRealization`, as act 6 did. None of that is carried by this freeze; only witness
A's `PPer` membership is merged, from act 6.

**Why two.** Witness A is rank-one degenerate, so a dilation result on it alone could be an artifact
of rank collapse rather than a fact about the dilation. Witness B separates the two.

**Their results are reported separately and never merged.** A divergence on **either** earns the
existential positive. Agreement on **both** earns only *not exhibited on these witnesses*.

## Outcome grid — deliberately ASYMMETRIC

**`DC1` — the dilation moves the visible candidate.** Two **source-admissible** dilations of one
fixed off-direct OI witness are **exhibited**, giving **different** visible candidates under the
frozen T3 readback. Exhibition at the **visible** level, never the operator level — act 4's earned
control, load-bearing here as it was in act 5. Earned by one witness; the result names which.

**`DC1` carries a strength, exactly as `DC3` and `DC4` do.** Under a **source-specified** readback it
licenses the full conclusion: Source A's own visible prediction is underdetermined by the visible
data, and a selection principle is required. Under a readback fixed by **our** amendment it licenses
only that the two dilations differ **under that map** — the divergence could be an artifact of the
extra map — and the result states that and not the full conclusion.

**`DC2a` — the input contract fails.** §3.4 does not accept the off-direct witness, with the failed
hypothesis named. Layer 2 *not reached*.

**`DC2b` — the source forms no candidate at all from the dilated unitary.** The contract is met, but
nothing downstream builds a relative object or readout from the dilated unitary, on the dilated
carrier or anywhere. Layer 2 *not reached*. This is act 4's `MP4` one branch over and is a live
possibility, not a formality. **`DC2b` is D4a's answer only**: a source that forms the candidate on
the dilated carrier but supplies no map back to `V` is D4b, which lowers strength rather than
stopping the round.

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

**Act 3's padding theorem bears on this round only through D5a AND D5b, and the round must not
over-apply it.** `candidateOf_uniformWeight_padData_eq` proves that `padData` padding leaves **our
`candidateOf` at `uniformWeight`** unmoved. That is a statement about a particular internal
construction and a particular weight — not about Source A's relative-unitary candidate, which is a
different quantity built from the unitaries rather than from fibre weightings.

So: **the merged corpus forbids nothing about this round's question**, and no sentence in the result
may say it does. If D5a and D5b both hold, the theorem is evidence and `DC3`/`DC4` is correspondingly
more likely. If either fails, the theorem is an **analogy and a control** — useful for seeing what
*kind* of enlargement leaves a candidate fixed — and the witnesses are examined as though it were
absent. `DC1` is never ruled out in advance by it.

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
4. **`DC2b` is D4a's answer only.** A source that forms no candidate from the dilated unitary stops
   the round; a source that forms one on the dilated carrier but supplies no map back to `V` does
   **not** stop it. The two are never merged.
5. **The readback is never chosen at execution time.** If the source supplies one it is transcribed;
   if it does not, layer 2 **pauses** for an append-only, separately frozen and merged amendment
   specifying the map, and resumes at reduced strength under it. Its provenance is reported either
   way, and under a non-source readback **every** layer-2 label is bounded by it: `DC3`/`DC4` state
   invariance **under that readback**, never invariance simpliciter, and `DC1` states divergence
   **under that readback**, never underdetermination of Source A's visible prediction and never a
   requirement for a selection principle (T3).
6. **Act 3's padding theorem is applied only if D5a AND D5b both hold** — the shape condition and the
   identification of the quantity under test with `candidateOf … uniformWeight`. Absent either it is
   an analogy and a control, never evidence for `DC3`/`DC4`, and it rules out `DC1` in no case.
7. **The input contract is tested in Source A's external orientation** — `(Γ t)ᵀ` or its `Θ`, never
   raw internal `Γ` — and covers **inherited** prerequisites, not only what §3.4 restates locally
   (D2, T2). Act 2's `RT1` licenses the orientation move and is consumed, never re-proved.
8. **Cross-time coherence of the dilated family is asked explicitly** (D3), since (39)/(42) consume
   two times and a pointwise existence theorem is not a coherently chosen family.
9. **Visible level, never operator level.** A divergence in dilations, unitaries or hidden carriers
   is **not** a `DC1`. Act 4's control, and act 5's exhibition burden.
10. **Per-witness reporting.** Witness A and witness B results are stated separately and never merged
   into one claim.
11. **`DC3` may not be paraphrased as uniqueness, harmlessness or representation freedom.**
12. **`DC4` is earned only by a theorem over all admissible dilations**, never by an unsuccessful
   search.
13. **Source coordinates** follow act 1's frozen table and act 5's authoritative surface, and are
   never mixed across sources. Only Source A is adjudicated; Sources B and C are not compared with it
   on any axis.
14. **The `n = 3` properness is cited, not proved**, is recorded at evidence level 3, and **no
   outcome rests on it**. The `n = 2` coincidence is proved in-round without external citation.
15. **The screen is necessary, not sufficient**, and is stated that way everywhere it appears.
16. **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are cited and never revised.** Acts
   1 through 6 are not reopened.
17. **No manuscript edit**, whatever is found.
18. **No sourcing inference.** Track separation both ways, per Amendment 2. No fifth condition, no
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

**If layer 1 passes, the two outcomes are close to balanced, and D5 is what moves the balance.** Act
5 exhibited a unitary-lift freedom moving the visible candidate on the direct branch, and that same
freedom sits inside any dilated unitary — which argues for `DC1`, and argues at full force, since it
is a statement about the same kind of object. Act 3's padding theorem argues the other way **only if
D5a and D5b both hold**; absent either, it is an analogy and shifts nothing. The honest prior is
therefore tilted toward `DC1` rather than balanced, and the freeze records it that way — while noting
that a prior is not a finding and `DC1` is earned only by an exhibited visible divergence.

**The prediction is recorded at that strength and no higher.** It is not a finding. `DC1` is earned
only by an exhibited visible divergence, `DC4` only by a universal theorem, and if neither is
produced the answer is `DC3`.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **One amendment is anticipated by name.** If D4b returns negative — the source forms a candidate on
  the dilated carrier but supplies no map back to `V` — layer 2 pauses and an amendment fixing the
  exact readback map is written, reviewed and merged before any layer-2 formalization or witness
  calculation. That amendment is a control-plane artifact under this same protocol, not an execution
  decision.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`.
- Final exact-head review after the source reading, any Lean, the result note and registry updates
  are complete.
- No merge without an explicit owner direction after exact-head review, naming the exact head SHA.

## Allowed final report

1. D1, D2, D3, D4a, D4b, D5a, D5b and D6 answered with exact coordinates, each freedom recorded
   *examined* or *not examined* — cross-time coherence among them — and D5's determination stated
   before any witness result, including whether act 3's padding theorem was applied as **evidence**
   (D5a and D5b both holding) or recorded as **analogy and control only**;
2. the admissibility predicate, stated in Source A's external orientation, listing the **inherited**
   prerequisites as well as §3.4's local ones, with any source-implicit condition named as a finding;
3. the readback map and **whose** it is — the source's, or the one a merged append-only amendment
   froze — with the strength of every layer-2 claim adjusted accordingly: under a non-source readback,
   `DC3`/`DC4` stated as invariance under **that** readback, and `DC1` stated as divergence under
   **that** readback rather than as underdetermination of Source A's visible prediction;
4. the screen T1, stated as necessary and not sufficient, with the `n = 2` proof in-round and the
   `n = 3` properness cited at evidence level 3;
5. both witnesses, their `PPer` membership and off-direct status proved, and their results
   **separately**;
6. the outcome — `DC1`, `DC2a`, `DC2b`, `DC3` or `DC4` — with the route to the label stated, since
   `DC2` has two routes, `DC3` and `DC4` must not be confused, and a `DC2b` must be shown to answer
   D4a rather than D4b;
7. the recorded predictions and whether each held;
8. the definition count and the `#print axioms` line for every named result;
9. what remains open and what would settle it;
10. explicitly: that `UB2` is existential and is not restated as a classification; that `DC3`, if
    reached, is unresolved and not evidence of uniqueness; that no candidate-selection principle has
    been adopted; that `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are unrevised; that no outcome says
    Source A is inapplicable or that the correspondence fails; and that nothing here is a sourcing
    claim.
