# Track B act 7 — RESUMPTION control plane (append-only)

**This is an append-only resumption freeze for act 7. It is NOT a new act, NOT a rewrite of act 7's
preregistration, and NOT a revision of any act-7 finding.** Act 7's frozen preregistration —
`preregistration.md` in this directory, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` — remains the
governing control plane in full. Everything below either cites it or narrows the scope of what is
executed next; nothing below loosens it.

**Start state.** Merged `main` at `608a507032976511581475f1f1db6b14e34cf2e0`.

**The licence to resume.** Act 8 closed at **`CE1`**
(`programmes/oi-qm/track-b/act-08-continuous-extension/result.md`), exhibiting a Source-A-admissible
continuous extension whose discrete restriction is act 6's frozen off-direct witness, still
off-direct at the frozen index, with every compatible potential there non-unitary. That is the object
act 7 lacked.

## What this resumption is, in one paragraph

Act 7 stopped at **`DC2a`** — its layer-1 `D2` failed, because §3.4's inherited continuity condition
is uninstantiated on the `ℕ`-indexed witness. `D4a` and `D4b` were therefore recorded **not reached**.
Act 8 supplies an object that meets the contract. **This freeze authorises exactly one thing: asking
and answering `D4a` and `D4b` on Source A, with the signs unset.** The outcome labels, the stop
table, the strength rules and the readback route are act 7's, unchanged.

## `DC2a` is NOT revised, and the repair is by SUBSTITUTION of the object under test

**`DC2a` remains historically and presently correct.** It says act 7's own `ℕ`-indexed off-direct
witness lies outside §3.4's input contract, and that is still true of that family. Nothing in act 8
contradicts it and nothing here revises it.

**What act 8 changed is which object is under test, not what `D2` returned about the old one.** The
distinction is load-bearing and is stated rather than blurred: a round that quietly re-answered `D2`
would be rewriting act 7, which this freeze forbids.

**The object under test is FROZEN HERE**, so it cannot be swapped at execution time:

| | Fixed as |
| --- | --- |
| The continuous family | the extension exhibited by `OIBridge.ContinuousExtension.admissible_offDirect_continuous_extension` |
| Its discrete restriction | `Γ n = 𝟙` at even `n`, act 6's collapsing slice `A = ![![1,0],![1,0]]` at odd `n` — the whole family, proved at every index |
| The admissibility predicate it satisfies | `OIBridge.ContinuousExtension.SourceAAdmissible`, act 8 layer 1's transcription of Source A's contract |
| The off-directness index | `n = 1`, act 8's `L1`, fixed before act 8's construction |

**Substituting a different witness requires an append-only amendment merged before use**, exactly as
act 8's own witness discipline required. Act 8's `CE1` is **existential**, so this resumption runs on
**that one witness** and every finding it produces inherits that scope. `CE1` is never restated here
as a statement about the OI class, and no result of this resumption may be quantified beyond the
witness it was run on.

### Two carried caveats, recorded so they are not discovered later as convenient

1. **The target domain is `ℝ≥0`.** Act 8 instantiates the contract on the non-negative half-line.
   Source A's target-time convention (§2.1 p. 3) is hedged by "usually", and act 7's own `D2` already
   classified that as a domain mismatch rather than an independent prerequisite. **That reading is
   inherited unchanged and is not re-adjudicated.** Nothing here claims the witness satisfies or
   fails a real-line requirement, because the source states none.
2. **The witness is off-direct at odd indices and is the identity at even ones.** The identity is
   unistochastic, so §3.4's dilation is triggered at some times and not others. `D4a` and `D4b` are
   questions about **Source A's text**, so this does not bear on them — but it is recorded now
   because it will bear on which slice any later layer-2 comparison runs at, and the frozen index is
   `n = 1`.

## The question, and its exact scope

**Adjudicate `D4a` and `D4b`. Nothing else.**

Act 7's frozen wording governs both and is carried verbatim:

> **`D4a` — is a candidate formed from the dilated unitary at all?** Does any equation form the
> relative operator (39), or any readout of (42)'s shape, from the **dilated** unitary — on the
> dilated carrier or anywhere? **If the source never forms one, the round stops at `DC2b`**: building
> that composite would be constructing on the source's behalf, which act 4 declined to do and this
> round declines likewise.

> **`D4b` — is that candidate brought back to the original visible carrier?** Given that a candidate
> is formed on the dilated carrier, does the source supply a map returning it to `V`? **A negative
> answer here does NOT stop the round.** It is recorded as a finding, our own readback is frozen per
> T3, and every layer-2 outcome is reported at **reduced strength**. `DC2b` is reserved for D4a.

**`D1`, `D2` and `D3` are NOT re-asked as outcome-bearing questions.** They are merged act-7 findings
and are cited, not re-derived: `D1` fixes the dilated object as `Θ(t ← 0)` (§3.4 p. 10); `D2`
returned the contract and its failure on the old witness; `D3` inventoried the freedoms and recorded
the derivation-and-selection gap. **`D3`'s gap — Stinespring supplying pointwise existence with no
coherent time-indexed family derived or selected, and no stated link from regularity of the visible
family to regularity of `Θ` or `U` — remains separately OPEN and is not closed by anything here.**

**`D5a`, `D5b` and layer 2 stay *not reached*** until and unless the routing below reaches them.
`D6` is answered in act 7 and is corroboration only, as act 7 froze it.

## Routing — act 7's stop table, with the row this resumption enters

The table is act 7's and is reproduced to fix which row is live, not to restate the round:

| Layer-1 finding | Layer 2 | Outcome |
| --- | --- | --- |
| §3.4's input contract is not met by the off-direct witness | not reached | **`DC2a`** — act 7's recorded stop, on its own witness |
| Contract met, but the source forms **no candidate at all** from the dilated unitary | **not reached** | **`DC2b`** |
| Contract met; a candidate is formed on the dilated carrier; the source **supplies** a map back to `V` | executed at **full strength** | `DC1`, `DC3` or `DC4` |
| Contract met; a candidate is formed on the dilated carrier; the source supplies **no** map back to `V` | **paused** until an append-only amendment freezing the readback map is merged, then executed at **reduced strength** | `DC1`, `DC3` or `DC4`, each marked reduced-strength |

**This resumption enters at the contract-met rows, on act 8's witness.** Which of the three it lands
on is what `D4a` and `D4b` decide, and it is not decided here.

- **`D4a` negative → `DC2b`, and the round STOPS.** Layer 2 is recorded *not reached — the source
  layer stopped the round*, never *unresolved*. Act 5's status discipline governs.
- **`D4a` positive, `D4b` positive → the full-strength layer-2 route**, exactly as act 7 froze it.
- **`D4a` positive, `D4b` negative → PAUSE.** No witness computation, no witness B, no `T1`–`T4`
  formalization, no Lean, no candidate comparison. The next artifact is **the append-only readback
  amendment**, written, reviewed and merged, after which layer 2 runs at **reduced strength**.

**The third and fourth rows are different branches and must not be run together**, per act 7. A stop
and a strength reduction are not the same instruction.

## Under a non-source readback, every later label is bounded — carried forward now

Act 7's `T3` rules are inherited in full and are restated here because the pause branch is the one
this freeze considers likeliest to be entered:

- If the source specifies the readback, it is **transcribed**, and the round runs at full strength.
- If it does not, the readback is fixed by a **merged append-only amendment**, never chosen at
  execution time, and **every** layer-2 label is bounded by it. `DC3`/`DC4` would state invariance
  **under that readback**, never invariance simpliciter; `DC1` would state divergence **under that
  readback**, never underdetermination of Source A's own visible prediction and never a demonstrated
  need for a selection principle.

**A difference produced under an amendment's readback could still be an artifact of the extra map
rather than of the dilation freedom.** That is why the strength is reduced, and the reduction is
reported in the result rather than inferred by a reader.

## Prediction, recorded before executing — and it is NOT the default answer

Act 7's result records a counterfactual source reading of **`D4a` positive / `D4b` negative**, with
coordinates (§3.4 p. 10; (28) p. 11; §3.5 p. 13; and for `D4b`, marginalization supplied only for the
rooted object at fixed initial ancilla configuration, with §3.7's (45)–(46) p. 17 and (50)–(52) p. 18
conditioned on idealizations the source does not state of a generic Stinespring dilation).

**That reading is carried here as a PREREGISTERED PREDICTION and nothing more.** Act 7's own note
says of it that it "settles nothing in this round". This freeze adds no new source reading to it.

**The prediction may not become the default answer, and the execution may not start from it.** `D4a`
and `D4b` are each asked on the authoritative surface and answered with coordinates, and an answer
that merely agrees with the prediction must still be earned the same way. **If the execution returns
the predicted pair, the result says the prediction held — it does not say the prediction was the
finding.** A prediction that is allowed to stand in for a reading is how a counterfactual gets
promoted to a result, which act 8's freeze forbade and this one forbids again.

## Source discipline

**Source A only**, at act 1's frozen identity: *The Stochastic-Quantum Correspondence*,
arXiv:2302.10778v3. The **authoritative surface is the PDF**, verified by its p. 1 stamp before
reading, per act 5's rule; the arXiv HTML rendering is non-admissible. Sources B and C are not
consulted and not compared with Source A on any axis. Every finding carries a page and, where one
exists, an equation coordinate.

**Inherited prerequisites count**, per act 7's clause: a hypothesis the construction actually needs
is in the answer whether or not §3.4 restates it locally. And the symmetric error is forbidden: no
condition is added because including it would change the branch.

## Execution discipline — stated in advance, including the branch-dependent artifact count

Act 8's two-PR rule does not transfer unchanged, because the pause branch inserts an artifact. The
full sequence is therefore fixed **now**, so that a third or fourth PR cannot later read as protocol
drift:

1. **Control-plane PR — this file alone.** No execution, no source adjudication, no Lean, no probe
   guard, no roadmap edit. Reviewed and merged before anything else.
2. **Adjudication PR** — the `D4a`/`D4b` result note, from the resulting `main`. Under `DC2b` this
   PR also closes the round and carries the `verification/ROADMAP.md` `P0` propagation.
3. **Only if `D4b` is negative: the readback-amendment PR** — an append-only amendment in this
   directory fixing the exact readback map, reviewed and merged **before** any layer-2 work.
4. **Layer-2 execution PR**, if and only if the routing reaches it.

**`ROADMAP.md`'s `P0` row is propagated by the ADJUDICATION PR, not by this one.** The roadmap's own
rule is that a status change "belongs in that linked artifact first; this file follows it", so the
row may still read `OPEN` while this freeze governs the obligation. That lag is accepted for act 8's
reason: it keeps the control-plane PR to this file alone, and the adjudication PR knows the branch
and can set the row once instead of setting it twice.

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- Exact-head review after the adjudication is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**

## Definition budget

**Act 7's budget is inherited unchanged, and is neither enlarged NOR narrowed here.** Act 7's
execution introduces **at most six** top-level definitions, and these are the six, carried from the
frozen preregistration:

1. the source-admissible dilation predicate (`T2`);
2. the dilated-family carrier or datum, **if** the predicate cannot be stated without one;
3. the visible readback map (`T3`);
4. the `DC1` proposition — two admissible dilations, different visible candidates;
5. the `DC4` proposition — visible invariance over all admissible dilations;
6. the double-stochasticity screen predicate, **if** act 2's `IsRowStochastic`/`IsColStochastic` pair
   does not already state it without a new name.

**The two conditional slots — 2 and 6 — are part of the budget and are carried as conditional.**
Dropping either would narrow act 7's frozen layer-2 control plane, which this file has no authority
to do: the original preregistration governs in full, and "in full" includes the slots that may turn
out to be unneeded.

**Witnesses are built inside the proofs that need them**, per act 3's lesson — no top-level witness
definitions. Merged definitions are consumed, never redefined. **If layer 1's findings require a
seventh, that is an append-only amendment**, separately frozen and merged before the work it affects;
it is not a licence taken at execution time.

All six slots belong to act 7's **layer 2** and are untouched while layer 2 is unreached. **The
adjudication itself introduces NO definitions and NO Lean**: it is a reading of the accepted text,
act 1's evidence level 3.

## Mandatory controls

1. **Scope.** `D4a` and `D4b` only, signs unset. `D1`–`D3` are cited, never re-adjudicated; `D5` and
   layer 2 stay *not reached* unless the routing reaches them.
2. **Act 8 is not revisited.** Its construction, its contract transcription, its `O-B`/`O-C`
   discharge and its `CE1` label are consumed as merged, and no part of this resumption reopens,
   re-proves or weakens them.
3. **Acts 1–6 stay closed.** `BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1` and `UB2` are cited and
   never revised.
4. **`DC2a` is not revised**, and the repair is reported as a substitution of the object under test.
5. **No new outcome labels.** The grid is act 7's: `DC1`, `DC2a`, `DC2b`, `DC3`, `DC4`, with the
   reduced-strength marking where the readback is ours. Nothing new is coined.
6. **`DC2b` is `D4a`'s answer only.** A source that forms a candidate but supplies no map back to `V`
   is `D4b`, which lowers strength rather than stopping.
7. **`DC3` is never evidence of uniqueness** and never upgrades to `DC4`; **`DC4` is earned only by a
   theorem over a stated class**; failure to prove either is not the other. Act 5's `A1` discipline.
8. **The readback is never chosen at execution time.** Transcribed if the source supplies one;
   otherwise fixed by a merged amendment, with every label bounded by it.
9. **The prediction is not the answer**, and an agreeing result says the prediction held rather than
   that it was the finding.
10. **No construction of any kind in the control-plane PR or the adjudication PR** — no dilation
    built, no readback chosen, no witness B, no candidate comparison, no `T1`–`T4`, no Lean.
11. **Existential scope is preserved.** `CE1` is existential and is never restated as a
    classification; nothing here is quantified beyond act 8's single frozen witness.
12. **No manuscript edit**, whatever is found.

## Non-doings

Do not: test or compare dilation choices; construct a dilation, a readback, or witness B; run act 7's
layer 2 or any part of `T1`–`T4`; adopt or propose a candidate-selection principle; claim Source A is
applicable or inapplicable; claim the external correspondence succeeds or fails; read `DC2b` or
`DC3` as impossibility; promote act 7's counterfactual to a finding; revise `DC2a`; reopen act 8;
adjudicate act 5's gauge-versus-empirical tension or decide `F1` versus `F2`; close `D3`'s gap; name
or adopt `C5`; compare Source A with Source B or Source C on any axis; edit manuscripts.

## The one restraint that matters most

**Do not jump to testing dilation choices. Earn `D4a` and `D4b` on the source first.** The whole
reason act 7 stopped cleanly rather than producing a misleading comparison is that its layer order
was binding, and the same order binds here: the source is read before anything is built, and what is
built is determined by what the reading returns — not the other way round.
