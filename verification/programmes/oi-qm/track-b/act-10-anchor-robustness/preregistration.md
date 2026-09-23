# Track B act 10 — anchor robustness (`P0b`): CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no execution, no Lean, no probe
guard, no roadmap edit, and no outcome label. It **does** carry, deliberately, the frozen
`a₀′ = 1` derivation and the `AB0` prediction it supports — that is what a preregistration is for,
and recording them here before merge is what makes them auditable rather than retrospective. Every
*execution-specific* anchor object is excluded. It is merged before any execution begins, and the
execution PR descends from the commit that merges it, under the strengthened ancestry certificate
frozen below.

## Start state

| | |
| --- | --- |
| Merged `main` | `d7b99c3bd516dd422c42379044e8c84f7b8f4c42` (PR #585) |
| Act 7's governing preregistration | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Act 7's readback amendment (`T3`) | `../act-07-dilation-choice/readback-amendment.md`, blob `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| Act 7 layer 2's result (`DC1`) | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 9's preregistration (`P0a`) | `../act-09-readback-robustness/preregistration.md`, blob `061fd38343185b4c6f764da0da9602367ad8f370` |
| Act 9's result (`RB3`, `RB1-A`, `RB1-B`) | `../act-09-readback-robustness/result.md`, blob `f918e7b405dec35e01e9d53ca0dd90eb56c34df4` |
| Act 9's module | `verification/lean-mathlib/OIBridge/ReadbackRobustness.lean`, blob `2dc9db6dbeb9fd18532e89d266257d1e1d6fc23d` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## The licence to run, and the exact question

Act 7 layer 2's merged limitation has two axes. Act 9 closed the **map** axis (`P0a`): `RB3` proved
`R-2` alone forces every same-interface readback to agree with the merged `R_{a₀}` on every
modulus-squared unitary, and `RB1-A`/`RB1-B` carried each witness's divergence across the whole
frozen readback class. Act 9's result fixed what remains, in the wording it froze in advance:

> not an artifact of the readback map within the `R-1`/`R-2`/`R-3` same-interface class; dependence
> on the **anchoring convention** remains open.

**This round asks the anchor half, and only that:** holding act 7's compared dilations fixed, does
some other anchor at which they all still reproduce their visible slices make the two visible
candidates **agree**?

## The structural distinction, FROZEN BEFORE ANYTHING ELSE

**`P0b` is: vary the ANCHOR, hold the DILATIONS fixed.**

**Changing a dilation in order to make some anchor admissible is NOT `P0b`.** It is a second
dilation search, and it belongs to dilation-choice / coherence territory — act 7's `DC` grid and act
7's open `D3` gap — not here. This distinction is frozen first because it is the single way this
round could silently become a different round: on discovering that no alternative anchor is jointly
admissible, the tempting next move is to adjust a dilation until one is, and that move answers a
question nobody preregistered.

**Concretely, the following are all OUT OF SCOPE:** replacing either `G₁`-side dilation; replacing
the `G₂`-side dilation; enlarging or changing the ancilla carrier (which changes the dilations, since
they are matrices on `V × A`); composing a dilation with anything; and re-deriving act 7's
exhibitions on different data. **The compared dilations are exactly act 7 layer 2's, cited by name
from the merged module and unmodified.**

**And the ancilla is therefore fixed too.** Act 7's exhibitions live on `A = Fin 2`, so the anchor
domain of this round is `Fin 2` — two candidates, one of which is the already-used `a₀ = 0`. A round
that "needed a bigger ancilla" would be changing the dilations, per the paragraph above.

## The property cut, FROZEN — availability is a PREREQUISITE, not an inference

An anchor is **jointly reproducing** for a compared configuration exactly when **every** dilation in
that configuration is admissible, at that anchor, for the visible slice it dilates — in act 7's own
`AdmissibleDilationAt` sense, cited unmodified. Four dilations enter each of act 7's `DC1`
exhibitions (`U₂`, `U₁`, `U₂′`, `U₁′`), so all four must reproduce at the candidate anchor.

**This is a property cut, never an enumeration.** No list of "reasonable" anchors may be written down
in this file or at execution time; the family is exactly the jointly reproducing anchors, and
membership is decided by the property.

**Availability is an explicit prerequisite with its own obligation.** Before any `AB1` or `AB2` label
may be assigned, the execution must **exhibit a jointly reproducing anchor distinct from the anchor
act 7 already used**, and prove it jointly reproducing. Failing that, the outcome is `AB0` and no
`AB1`/`AB2` label is assigned.

> **`AB1` IS NOT EARNABLE VACUOUSLY.** `AB1` is a universal over the jointly reproducing anchors, so
> it is vacuously true over an empty alternative-anchor domain and trivially true over the singleton
> `{a₀}` already used. **Neither counts.** A universal quantifier satisfied only because its domain
> has no new element is not a robustness result, and this round refuses to report one as such.

## The outcome grid — PER WITNESS, and three-valued

Act 7 layer 2 reported witnesses A and B separately and never merged them; act 9 kept them separate;
**this round keeps them separate on the same rule.** Six labels, three per witness.

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`AB1-X`** | **Every** anchor jointly reproducing witness X's compared dilations **preserves** the divergence | a universal theorem over the jointly reproducing anchors, **plus** an exhibited second such anchor |
| **`AB2-X`** | **There exists** a jointly reproducing anchor under which witness X's two visible candidates **agree** | an exhibited anchor, proved jointly reproducing, with the agreement proved |
| **`AB0-X`** | **No second jointly reproducing anchor exists**, so the robustness question **collapses** to the anchor already used and yields no new comparison | a **theorem** that every jointly reproducing anchor equals the one act 7 used — by exhaustion over the finite anchor domain, never by an unsuccessful search |

`AB1-X` and `AB2-X` are contradictory for a fixed witness. **`AB0-X` is incompatible with both**, and
is not a weaker version of either: it reports that the comparison the round was set up to make does
not exist on that witness.

**A split outcome across witnesses is permitted and reportable** — `AB0` on one and `AB1` or `AB2` on
the other is a legitimate result, not a sign of error.

**`AB0` is a POSITIVE finding about availability, and it is earned like one.** It must be proved, not
observed: the anchor domain is finite, so exhaustion is available, and "we looked and found none" is
not the statement. This mirrors the discipline act 7 applied to `DC4` and act 9 to `RB1` — a
universal is never earned by a failed search — applied here to the negative.

## The preregistered prediction: `AB0` on BOTH witnesses

**`AB0-A` and `AB0-B` are predicted, and the prediction is a COMPUTATION against the merged objects,
checked before this freeze was written — not a guess, and not a finding.** The computation is
recorded in full so the execution cannot quietly substitute a different one.

The anchor domain is `A = Fin 2`, so the only candidate distinct from act 7's `a₀ = 0` is `a₀′ = 1`.
Marginalizing each merged dilation at `a₀′ = 1`:

| Dilation | Slice it must reproduce | Anchored marginal at `a₀′ = 1` | Reproduces? |
| --- | --- | --- | --- |
| `U₂ = U₂′ = 𝟙` | `𝟙` | `[[1,0],[0,1]]` | **yes** |
| witness A's `U₁ = P(prodComm)` | `Aᵀ = [[1,1],[0,0]]` | `[[0,0],[1,1]]` | no |
| witness A's `U₁′ = P(prodComm · swap((1,0),(1,1)))` | `Aᵀ` | `[[0,0],[1,1]]` | no |
| witness B's `U` (the `s = √(1/2)` unitary) | `Bᵀ = [[1,1/2],[0,1/2]]` | `[[1/2,0],[1/2,1]]` | no |
| witness B's `U · P(swap((0,1),(1,1)))` | `Bᵀ` | `[[0,1/2],[1,1/2]]` | no |

So on **both** witnesses the only alternative anchor fails joint reproduction, and it fails on the
`G₁` side — **the identity dilation of `G₂ = 𝟙` is admissible at every anchor**, which localizes the
collapse rather than leaving it diffuse.

**The structural reason, recorded so the prediction is not mistaken for an accident of these
permutations.** For a permutation dilation, act 7's merged closed form gives the reproduced slice as
`if (σ.symm (j, a₀)).1 = i then 1 else 0` — a `0/1` matrix whose single occupied row index is
`(σ.symm (j, a₀)).1`. **Moving the anchor moves which preimage fibre is read, and so in general moves
that row index.** The anchor is therefore tightly coupled to the slice a permutation dilation
reproduces, and joint reproduction at two anchors is a strong coincidence rather than the default.

**Why the round is still worth running, stated before it runs.** If `AB0` lands it lands because the
anchor and the reproduced slice are coupled, not because the anchor space was searched cleverly —
the same kind of honesty act 8 could only record after the fact and act 9 recorded in advance. What
the round buys is: the collapse **proved** by exhaustion rather than asserted; the localization to
the `G₁` side recorded; the anchor axis' status settled from *open and untested* to *untestable by
this construction*, which is a different and more useful thing to know; and the `P0b`-versus-
dilation-choice boundary held while that is established.

## What `AB0` does NOT license — the control this round most needs

**`AB0` does NOT close the anchor half of act 7's caveat.** This is the round's central control and
is frozen in advance because the temptation runs the other way.

- `AB0` says the anchoring convention **cannot be varied downstream** on these witnesses with these
  dilations held fixed. It does **not** say the convention makes no difference, and it does **not**
  say the divergence is convention-independent.
- The **upstream** choice remains a choice. Act 7's dilations were built around `a₀ = 0`; a different
  anchor chosen upstream would have produced **different dilations**, and whether that pairing
  diverges is exactly the out-of-scope question frozen above. `AB0` is silent on it.
- Therefore act 7 layer 2's caveat, as act 9 sharpened it, **stands unchanged** under `AB0`:
  dependence on the anchoring convention **remains open**. If anything `AB0` makes the caveat more
  necessary, not less: the convention could not even be varied to test it.

**A result note that reads `AB0` as closing `P0`, closing the anchor axis, or retiring the caveat is
wrong, and this file says so before the outcome is known.** Under `AB0`, `P0` is **not** closed and
the anchor-axis dependence is **not** resolved — it is reclassified as not reachable by this
construction, with the upstream question named as the live remainder.

## Immutable inputs

These are **cited and consumed unmodified**. None may be revised, re-strengthened or re-scoped by
this round:

- act 7's **`DC1`** — existential, at reduced strength, under `R_{a₀}` on anchored dilations, with its
  two witness exhibitions (`witnessA_moves_visible_candidate`, `witnessB_moves_visible_candidate`);
- act 9's **`RB3`**, **`RB1-A`**, **`RB1-B`**, and the sharpened caveat wording;
- act 7's **`DC2a`**, **`D4a`**, **`D4b`**; act 8's **`CE1`** (existential); acts 1–6's labels;
- act 7 layer 2's **`D5` chronological-ordering control**, which stands **NOT CERTIFIED** and is not
  repaired retroactively by anything here.

**Act 7's `D3` coherent-dilation gap is untouched.** It is neither closed nor used, and it remains
**separately OPEN** — still the route by which a `DC4`-shaped invariance could hold on a narrower,
coherence-restricted class. Note that the out-of-scope "change the dilation to admit a new anchor"
move lands squarely in that territory, which is a second reason the boundary above is frozen.

## The chronology control — act 9's CORRECTED mechanism, carried forward by name

The ordering discipline is act 9's, and the execution **must reuse act 9's corrected guard
mechanism** rather than re-derive one, strengthened as clause 5 requires. Act 9's guard took two
review rounds to get right — a shallow-clone gap, then a synthetic-merge-commit gap — and clause 5
closes a third, found in review of this freeze. Every one of the three would have passed silently
under a weaker design and shown green. They are avoidable here, and are hereby avoided:

1. **This preregistration blob is merged into `main` before any execution-specific anchor object
   enters the repository tree** — any Lean definition or proof about an alternative anchor, any
   search, any probe guard, any result artifact. **The single permitted exception is the analysis
   recorded inside this control-plane blob itself**: the frozen `a₀′ = 1` derivation and the `AB0`
   prediction of the section above are part of the freeze, are merged *as* the freeze, and are
   exactly what a preregistration is for. What the ordering discipline forbids before merge is
   execution material beyond this file, not this file's own recorded expectation.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR**, and its
   first commit must descend from it.
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head.** In a `pull_request` Actions run the
   guard resolves `pull_request.head.sha` from the event payload — **never** the synthetic merge
   commit `refs/pull/<n>/merge`, whose parents include the PR base, which would make the check
   vacuous. An unresolvable head **fails closed**, with no fallback.
5. **The ancestry check must exclude pre-freeze side history, not merely certify the final head.**
   Head-only ancestry is too weak for the claim it is asked to support. Let `B` be the merge commit
   of this control-plane PR and `H` the real execution head resolved by clause 4. Requiring only
   `git merge-base --is-ancestor B H` admits this counterexample: an anchor-specific commit `E` is
   made **before** `B` exists, and is later merged together with `B` into `H`. Then `B` is an
   ancestor of `H` and a head-only guard passes, while `E` is reachable from `H` and never descended
   from `B` — execution material that entered history before the freeze, certified clean. The guard
   must therefore require, fail-closed:
   - `B` is an ancestor of `H`; **and**
   - **every** commit in `git rev-list H ^B` is itself a descendant of `B`.

   Equivalent formulations are permitted, but the property certified must be the strong one: **no
   commit reachable from the execution head lies outside `B`'s descendants.** A guard that checks
   only the head does not discharge this clause.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, or fetching an
   absent commit — and **fails** if recovery fails. Recovery never substitutes for the check, and it
   applies to `B`, to `H`, and to the commits enumerated under clause 5 alike.

**The claim this supports is scoped to the repository record**: git certifies what entered the tree
and when, not what anyone thought, drafted outside the tree, or worked out privately. As in act 9,
the central prediction is written into this freeze before merge, so **the merged blob is itself the
record** of what was expected.

## Definition budget

The execution introduces **at most four** top-level definitions, and these are the four:

1. **The jointly-reproducing-anchor predicate** — the property cut. *Needed.*
2. **A carrier or bundle for the compared configuration** (the visible pair and the four dilations),
   *if* the propositions cannot be stated without one. *Conditional.*
3. **`AB1`'s proposition.** *Needed.*
4. **`AB2`'s proposition** — *unless* stated as the negation of (3), in which case unused.
   *Conditional.*

**`AB0` gets no slot of its own**, deliberately: it is statable as a theorem over slot 1 — every
jointly reproducing anchor equals the one act 7 used — and a definition for it would be budget spent
on a proposition the property cut already expresses.

**A fifth definition requires its own append-only amendment**, separately frozen and merged before
use. **No anchor, dilation, witness or configuration is a top-level definition** — each is built
inside the proof that needs it, per act 3's lesson and acts 7/9's practice.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide`.

## Named hazards

1. **The anchor test becoming a dilation search.** The hazard the first frozen section exists for,
   and the likeliest one given the prediction. Any change to a compared dilation, to the ancilla, or
   to the visible pair takes the round out of `P0b`.
2. **Vacuous `AB1`.** A universal over an empty or singleton-already-used domain. Availability is a
   prerequisite, and `AB0` is the honest outcome when it is not met.
3. **`AB0` read as closure.** See the control section. `AB0` reclassifies the anchor axis; it does not
   resolve it, and it does not touch act 7's caveat.
4. **`AB0` asserted rather than proved.** The domain is finite; exhaustion is available; a failed
   search is not the statement.
5. **Merging the two witnesses.** They are reported separately, as in acts 7 and 9.
6. **A chronology guard that certifies only the head.** Head-only ancestry passes over pre-freeze
   side history merged in later, as the chronology section's counterexample shows. This is the third
   distinct way this family of guard has been found too weak — after act 9's shallow-clone gap and
   its synthetic-merge-commit gap — and each was invisible from a green check. The guard must
   certify clause 5's strong property, and a green result that only establishes head ancestry does
   not discharge it.

## Non-doings

Do not: run any part of the execution before this file is merged; introduce any execution-specific
object about an alternative anchor — a Lean definition, a proof, a search, a probe guard or a result
artifact — before then (**the frozen derivation and prediction recorded inside this blob are the
permitted exception, per the chronology section's clause 1**); change any compared dilation, the
ancilla, or the visible pair; enumerate "reasonable" anchors instead of cutting the family by the
property; assign `AB1` or `AB2` without an exhibited second jointly reproducing anchor; assign `AB0`
by search rather than by theorem; claim `P0` closed; claim the anchor-axis dependence resolved; revise
`DC1`, `RB3`, `RB1-A`, `RB1-B`, `DC2a`, `D4a`, `D4b`, `CE1`, act 7 layer 2's `D5` NOT-CERTIFIED
status, or any act-1-through-9 finding; close or silently use act 7's `D3` gap; adopt or propose a
candidate-selection principle; name or adopt `C5`; compare Source A with Source B or Source C on any
axis; source anything across to Track I; edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.** No Lean, no probe guard, no roadmap edit, no census edit.
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob, resolving the real PR head by act 9's corrected
  mechanism, and certifying the **side-history-excluding** ancestry of the chronology section's
  clause 5), the `ROADMAP` `P0` propagation, and the census entry.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. The jointly-reproducing property as cut, with the compared dilations cited unmodified from act 7's
   merged module;
2. **availability answered first** — whether a second jointly reproducing anchor exists, per witness,
   and how that was established;
3. the per-witness outcome — `AB1-X`, `AB2-X` or `AB0-X` — **separately**, with the route to each
   label, and with `AB0` presented as a proved exhaustion rather than a search report;
4. where an `AB0` collapse localizes (which side's dilations fail, and at which anchor), since a
   localized collapse is more informative than a bare one;
5. what `AB0` does **not** license, in the wording this file fixes: `P0` **not** closed, the
   anchor-axis dependence **not** resolved but reclassified, act 7's caveat **unchanged**, and the
   upstream anchor choice named as the live remainder;
6. `D3` restated as separately open and untouched;
7. the chronology control, naming the property actually certified — **no commit reachable from the
   execution head lies outside the control-plane merge's descendants** — and what it does not
   certify (anything outside the repository record);
8. the definition count against the four-slot budget, with conditional slots marked fired or unused;
9. the axiom report, one line per named result.
