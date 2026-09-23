# Barandes indivisibility and correspondence bridge audit — preregistration

Base: `main` at `7b0e450227c3e577959167b95b0f7cc543527b5a` (post-PR #557, Amendment 2 merged).

This preregistration **presupposes Amendment 2** (`verification/OI-QM-RESEARCH-PROGRAMME-AMENDMENT-2.md`, merged by PR #557), which establishes the two-track programme this round is act 1 of. That ordering is carried in **ancestry, not prose**: every commit of this branch descends from the merge that brought Amendment 2 to `main`, so the control-plane sequence is checkable from the history. It is a separate control-plane PR so that its blob freezes on its own.

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

**Q8 — sufficiency of our data.** Does the merged rooted-realization datum — a fixed reversible update on `V × H` together with one hidden prior common to every visible root, as `RootedRealization` carries it — provide **all** his required stochastic data, or is something missing? Name anything missing.

The prior is a **fixed ingredient of that datum** and is not claimed to be sourced from bare OI; #537 settled that and control 9 governs the language. The question is the sufficiency of the data, not its provenance, and an answer that describes the prior as sourced is wrong on the corpus regardless of what it concludes about sufficiency.

**Q9 — what the correspondence delivers.** Exactly what does his correspondence give: Hilbert representation only, empirical equivalence to textbook QM, measurement structure, composites and entanglement? For each item, is it a **theorem-level result** in the paper or an **interpretive claim**? This distinction is the deliverable, not a caveat on it.

## Admissible outcome shapes — two independent axes

The verdict is an **ordered pair** `(BDi, BRj)`. Both axes are always reported, and neither is reported without the other.

They are separated because they are independent, and a single precedence over a merged list would suppress the combination that matters most. An **exact definitional match** can perfectly well coexist with **indivisibility not being required for the basic correspondence**: the two would say that our predicate is exactly his, and that his theorem does not use it. That pair is the scientifically central outcome, and no ordering may hide half of it.

Within each axis the labels are mutually exclusive and exhaustive. There is no precedence within an axis and none between them.

### Axis A — the definition bridge

After the stated transposition and time-index identification, how does our `PIndivisibleWithin` stand to Barandes's divisibility predicate?

**BD1 — exact definitional match.** His divisibility predicate is literally ours under a stated transposition and time-index identification, so his indivisibility is literally `PIndivisibleWithin`. This is a determination about definitions, not a theorem.

**BD2 — qualified or one-way definitional match.** They coincide only under stated further conditions — matching conditioning times, orientation, horizon, time domain — or one is definitionally a restriction of the other in one direction. Reported as a **candidate implication**, not as an implication: the round forbids proof attempts, so the theorem belongs to the next formalization round. The single exception is an identification that is **literally definitional** after the stated transpose and index matching, which is reported as such and still not called a theorem.

**BD3 — definitional mismatch.** They are different predicates and no stated transposition identifies them. What differs is reported at the granularity of the three hazards named above.

**BD4 — undetermined.** The primary sources do not fix his predicate precisely enough to compare. Recorded as such, with what would fix it. A failed determination is never promoted to a finding.

### Axis B — the logical role in the correspondence

What does the basic correspondence do with divisibility?

**BR1 — required.** The basic correspondence uses actual failure of divisibility as a hypothesis.

**BR2 — not assumed, and not required.** The correspondence starts from the transition data. Divisibility is not assumed, and its failure is not a hypothesis of the basic theorem; "indivisible stochastic process" names the framework rather than a hypothesis. "Not assumed divisible" and "assumed not divisible" are different, and this label is the former.

**BR3 — required only downstream.** Failure of divisibility is not needed for the correspondence itself, but is used for specifically nonclassical or interference consequences.

**BR4 — version-dependent or undetermined.** The role differs across versions, or the sources do not fix it. Version-dependence is reported **per version** and is never collapsed into "undetermined"; the two are distinguished in the report even though they share a label.

### The finding that BR2 or BR3 carries

Either of those two means P-indivisibility has a **different logical role** than the one the manuscript gives it: explaining specifically nonclassical or interference behaviour rather than licensing the Hilbert-space correspondence. That is a corpus-consistency finding of the first order. It becomes a backlog item with a named manuscript surface, **without** any manuscript edit in this round, and it is a finding about the role, independent of whatever the definition axis returns.

## Prediction recorded before source inspection

Recorded so that the outcome cannot be read as confirmation of whatever is found.

**On the role axis: BR2 is predicted**, at roughly two-to-one against BR1. The ground is `BARANDES-BOUNDARY-AUDIT-RESULT.md`, which found that the 2023 theorem imposes no separate indivisibility hypothesis and that the unitarization proof begins from the transition matrix entries. That is a prior, not evidence, and if the accepted text contradicts it the accepted text wins.

**On the definition axis: no prediction is recorded.** The orientation and time-index hazards named above are exactly the kind that go either way, and a prediction here would be a guess dressed as a prior.

## Mandatory controls

1. **No proof attempt.** This round determines definitions. It does not prove, or claim, any relation between `PIndivisibleWithin` and any Barandes predicate. A determination that the definitions coincide is a determination about definitions, not a theorem, and is reported as such.
2. **Transposition is explicit.** Every comparison across the orientation boundary states the transposition performed. An unstated transposition is a defect even when the conclusion is right.
3. **Version discipline.** Each answer names the version it is answering from. Where versions differ, all are reported and the latest is not projected backward.
4. **No manuscript edit.** No manuscript, book, bibliography or publication edit occurs in this round, whatever is found. A `BR2` or `BR3` outcome creates a backlog item and nothing else.
5. **Track separation.** Nothing determined here is used as evidence for any Track I result, and no Track I result is used as evidence for a determination here. Amendment 2's rule is binding.
6. **Deferred resources.** Nothing here adjudicates any resource deferred by the Arc D preregistration, and no determination is stated as bearing on one.
7. **Arc D's quarantine is not reopened.** The S1 padding theorem stands. If the Barandes correspondence supplies operational content, that is because of its own hypotheses, and it does not make representational presence a ground for anything.
8. **No fifth condition.** The round does not name or adopt C5.
9. **Sourcing language.** Nothing determined here is described as OI *sourcing* any resource. What a correspondence theorem supplies under its own hypotheses is a different claim from what OI sources, and the report keeps them apart.

## Evidence hierarchy

1. **Primary source text at a pinpoint location** — the only admissible evidence for an answer about what Barandes's definitions and theorems say. The evidentiary requirement is the **location**: source, version, date, and the definition, theorem, equation or section number. Brief quotation may accompany it where it helps the reader, and is not itself the requirement.
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
3. the headline verdict as the ordered pair `(BDi, BRj)`, with both axes reported and neither omitted;
4. what the correspondence delivers, itemized, each item marked theorem-level or interpretive;
5. whether any determination contradicts or destabilizes a merged description in this corpus, and the backlog item it becomes;
6. what the next Track B round can begin from, without executing it;
7. evidence type for every determination, and what remains undetermined;
8. explicitly, that nothing here is a sourcing claim.
