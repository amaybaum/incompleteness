# Barandes indivisibility and correspondence bridge audit — preregistration

Base: `main` at `58a7ef040869bad92daa51a80de283e48d37215a` (post-PR #554, Arc D round 1 closed at RD1).

This preregistration **presupposes Amendment 2** (`verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-2.md`, PR #557), which establishes the two-track programme this round is act 1 of. It is a separate control-plane PR so that its blob is frozen on its own; it should be merged after Amendment 2, and nothing in it executes before both are on `main`.

Track B, act 1, under the two-track programme established by Amendment 2. This is a **definition-level audit**, not a proof round. Its deliverable is a determination of what Barandes's objects and hypotheses *are*, transposed into this programme's formal vocabulary, and nothing more.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no execution begins before the freeze is merged.**

## Why this round exists, and why it is narrow

The programme does not attempt

`PIndivisible_OI  ↔  Indivisible_Barandes`

in this round. It cannot: the right-hand side has never been fixed at definition level against the accepted text. Preregistering the equivalence before fixing the definition would be preregistering a proof of an unstated proposition, and any verdict reached that way would be about a paraphrase rather than about the source.

The round is therefore deliberately unambitious. It answers nine questions, records the answers, and stops. Whether the equivalence then holds is the *next* round's question, and this preregistration does not prejudge it.

`BARANDES-BOUNDARY-AUDIT.md` and its result are the prior art and are not re-run. That round settled the **minimal input object** and the **ensemble requirement**: no primary-source theorem it examined requires a uniquely selected invariant law on the whole configuration space as the input that makes the transition law representable. Its Q3 touched the role of indivisibility but did not perform a definition-level transposition of the divisibility predicate itself, which is what this round adds.

## Primary-source restriction

Execution may use only Barandes primary sources — official arXiv versions and/or publisher versions — of:

- arXiv:2302.10778 (*The Stochastic-Quantum Correspondence*),
- arXiv:2309.03085 (*The Stochastic-Quantum Theorem*),
- arXiv:2507.21192.

Secondary summaries, search snippets, this repository's own paraphrases — **including `BARANDES-BOUNDARY-AUDIT-RESULT.md` and the manuscripts** — and later commentary may be used only to locate a primary source, never as evidence for a verdict.

Every answer records source title, version and date, and the exact definition or theorem location. Where the papers alter terminology or the role of indivisibility across versions, the latest statement is **not** silently projected backward onto the earlier theorem, and the divergence is reported.

**Execution precondition.** This round cannot begin until the primary sources are actually readable by the executing environment. `arxiv.org` is currently blocked by network egress policy in the session that drafted this file (403 CONNECT denial; `EGRESS_BLOCKED` from the fetch tool). Executing against the repository's paraphrases instead would violate the primary-source restriction above, so it is forbidden rather than degraded-to. The freeze may be merged while this precondition is unmet; **execution may not start until it is met**, by one of: allow-listing the source host for the environment, committing the primary-source text to the repository under its own provenance record, or executing the round in an environment with access.

## The objects on this side of the bridge, fixed before inspection

These are the merged definitions the audit transposes *to*. They are quoted here so that the comparison is against a fixed target and not against a remembered one.

From `OIBridge/CausalReadback.lean`:

```lean
def IsRowStochastic (M : Matrix V V ℝ) : Prop :=
  (∀ i j, 0 ≤ M i j) ∧ ∀ i, ∑ j, M i j = 1

def PDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∀ s t : ℕ, s < t → t ≤ K → ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ

def PIndivisibleWithin (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ¬ PDivisible K Γ
```

Three features of this side are load-bearing and are named now so that a mismatch is reported rather than absorbed:

1. **One time index, root fixed.** `Γ t` is the rooted map from the root time to time `t`. Barandes's `Γ_{t←t₀}` carries two. Ours is the `t₀ = 0` slice.
2. **Orientation.** Ours factors as `Γ t = Γ s * Λ`, with the propagator on the **right**. Barandes writes `Γ_{t←t₀} = Γ̃_{t←t'} Γ_{t'←t₀}`, with the propagator on the **left**. Row-stochastic-acting-on-the-right and column-stochastic-acting-on-the-left are the same content under transpose; that they are the same *here* is a claim to check, not to assume. The corpus already carries a live instance of exactly this hazard — two permutation-matrix conventions that are transposes of each other, bridged by `permMatrix_eq_coherent` — so the hazard is not hypothetical.
3. **Horizon-bounded and universally quantified.** Ours asks for a propagator at **every** admissible pair below a horizon `K`; its negation is therefore **existential failure at one pair**. Whether Barandes's notion is existential failure, generic failure, or failure everywhere is question 6 below, and the three are not interchangeable.

## The nine frozen questions

Answered in order. Each answer is a determination with a source location, or an explicit "not determinable from the primary sources examined".

**Q1 — the exact stochastic object.** What is Barandes's exact stochastic object in the accepted version: what data does the tuple carry, and what is contingent rather than nomological?

**Q2 — conditioning and target times.** What precisely counts as a conditioning time and what as a target time? Is the conditioning-time set a distinguished piece of the data, and does the theorem quantify over it?

**Q3 — the divisibility predicate.** What is his exact divisibility predicate, written out with its quantifiers and its stochasticity requirement on the intermediate object?

**Q4 — literal comparison after transposition.** After transposing row/column conventions and matching the time indexing, is his equation **literally** our stochastic-factorization equation? Report the transposition explicitly; a mismatch in orientation or in which factor is required stochastic is a finding, not a formatting detail.

**Q5 — required or merely unassumed.** Does his use of "indivisible stochastic process" **require failure of divisibility**, or does it name the larger framework in which divisible processes are admitted as special cases? The accepted text says the transition law is not assumed divisible and will generically be indivisible; "not assumed divisible" and "assumed not divisible" are different hypotheses and the audit must say which the theorem uses.

**Q6 — the shape of the failure, if it is required.** If actual indivisibility matters, is it existential failure at one `(t₀, t', t)`, failure generically, failure everywhere, or something else? Ours is existential failure below a horizon; any difference is reported at that granularity.

**Q7 — time domain.** Does our finite discrete-time rooted process satisfy his time-domain assumptions, or is an embedding or interpolation theorem needed? If one is needed, state what it would have to prove.

**Q8 — sufficiency of our data.** Does the sourced common-hidden-prior construction provide **all** his required stochastic data, or is something missing? Name anything missing.

**Q9 — what the correspondence delivers.** Exactly what does his correspondence give: Hilbert representation only, empirical equivalence to textbook QM, measurement structure, composites and entanglement? For each item, is it a **theorem-level result** in the paper or an **interpretive claim**? This distinction is the deliverable, not a caveat on it.

## Admissible outcome shapes

Exactly one headline is reported, and the precedence is `BB1 > BB2 > BB3 > BB4`.

**BB1 — exact match.** Our P-indivisibility is precisely Barandes's divisibility failure, after a stated transposition and time-index matching. The original chain is restored close to verbatim, and the next round's equivalence target is well-posed.

**BB2 — implication with qualifications.** Our notion implies his, or his ours, under matching conditioning times, orientation and time domain, with the qualifications named. Still a strong result; the next round's target is the implication, at the stated scope.

**BB3 — indivisibility is not required for the basic correspondence.** The correspondence starts from the transition data and does not use failure of divisibility as a hypothesis. Then P-indivisibility has a **different logical role** than the one the manuscript gives it: it would explain specifically nonclassical or interference behaviour rather than license the Hilbert-space correspondence. This is a corpus-consistency finding of the first order and becomes a backlog item with a named manuscript surface, **without** any manuscript edit in this round.

**BB4 — not determinable.** The primary sources examined do not fix the answer. Recorded as such, with what would fix it. A failed determination is never promoted to a finding.

## Prediction recorded before source inspection

Recorded so that the outcome cannot be read as confirmation of whatever is found.

**BB3 is the predicted outcome**, at roughly two-to-one against BB1 or BB2 combined. The ground is `BARANDES-BOUNDARY-AUDIT-RESULT.md`, which found that the 2023 theorem imposes no separate indivisibility hypothesis and that the unitarization proof begins from the transition matrix entries. That is a prior, not evidence, and if the accepted text contradicts it the accepted text wins.

## Mandatory controls

1. **No proof attempt.** This round determines definitions. It does not prove, or claim, any relation between `PIndivisibleWithin` and any Barandes predicate. A determination that the definitions coincide is a determination about definitions, not a theorem, and is reported as such.
2. **Transposition is explicit.** Every comparison across the orientation boundary states the transposition performed. An unstated transposition is a defect even when the conclusion is right.
3. **Version discipline.** Each answer names the version it is answering from. Where versions differ, all are reported and the latest is not projected backward.
4. **No manuscript edit.** No manuscript, book, bibliography or publication edit occurs in this round, whatever is found. A BB3 outcome creates a backlog item and nothing else.
5. **Track separation.** Nothing determined here is used as evidence for any Track I result, and no Track I result is used as evidence for a determination here. Amendment 2's rule is binding.
6. **Deferred resources.** Nothing here adjudicates any resource deferred by the Arc D preregistration, and no determination is stated as bearing on one.
7. **Arc D's quarantine is not reopened.** The S1 padding theorem stands. If the Barandes correspondence supplies operational content, that is because of its own hypotheses, and it does not make representational presence a ground for anything.
8. **No fifth condition.** The round does not name or adopt C5.
9. **Sourcing language.** Nothing determined here is described as OI *sourcing* any resource. What a correspondence theorem supplies under its own hypotheses is a different claim from what OI sources, and the report keeps them apart.

## Evidence hierarchy

1. **Primary source quotation with location** — the only admissible evidence for an answer about what Barandes's definitions and theorems say.
2. **Lean formalization of the transposed predicate** — admissible, and preferred, for the *this-side* half of the bridge. A transposed predicate defined in Lean and proved equivalent to `PDivisible` under the stated transposition is worth more than a prose transposition, and step 5 of the Amendment 2 sequence is where that belongs. No `sorry`, no custom axioms, no `native_decide`; every named result carries a `#print axioms` line printing only `[propext, Classical.choice, Quot.sound]`.
3. **Prose determination** — permitted where the source is genuinely ambiguous, with the ambiguity stated in the same place as the determination.

Mathematical status and kernel status are reported separately, as always.

## Non-doings

Before freeze and during this round, do not:

- assert any relation between `PIndivisibleWithin` and a Barandes predicate;
- treat this repository's paraphrases of Barandes as primary evidence;
- project a later version's terminology backward onto an earlier theorem;
- describe anything a correspondence theorem supplies as something OI sources;
- edit manuscripts, books, bibliography or publication claims;
- adjudicate any deferred resource;
- reopen, restate or re-prove any merged Arc B, C or D result;
- begin Arc D round 2 or Arc E work.

## Execution discipline

- Freeze this preregistration by exact commit SHA **and blob SHA** before any source inspection, transposition, formalization or determination. **Blob identity is authoritative.**
- Once frozen, this file is immutable. Any execution-affecting correction is an append-only amendment, separately frozen, and committed before the work it affects.
- **Two PRs, in order.** A control-plane PR carrying this file and nothing else is reviewed, frozen and merged before any execution; then exactly one execution/result PR branched from the `main` that already carries the frozen blob.
- Execution does not begin until the primary-source access precondition above is met.
- Final exact-head review is required after the result note and any registry updates are complete.
- No merge without an explicit owner direction after exact-head review.

## Allowed final report

The final report states separately:

1. each of the nine questions, with its determination, its source location and its version;
2. the transposition performed between orientations and time indexings, written out;
3. the headline outcome BB1 / BB2 / BB3 / BB4;
4. what the correspondence delivers, itemized, each item marked theorem-level or interpretive;
5. whether any determination contradicts or destabilizes a merged description in this corpus, and the backlog item it becomes;
6. what the next Track B round can begin from, without executing it;
7. evidence type for every determination, and what remains undetermined;
8. explicitly, that nothing here is a sourcing claim.
