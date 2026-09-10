# Track B act 2 — the Lean transpose bridge: preregistration

Base: `main` at `cf581479eab0e47d8c1f81984d7d6ec31184c150` (post-PR #560, Track B act 1 closed at `(BD3, BR3)`).

This preregistration **presupposes act 1** (`verification/BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, merged by PR #560), whose Q4 established in prose the transposition this round formalizes. That ordering is carried in **ancestry, not prose**: every commit of this branch descends from the merge that brought act 1 to `main`. It is a separate control-plane PR so that its blob freezes on its own.

Track B, act 2, and step 5 of the Amendment 2 sequence. This is a **proof round** over this programme's own definitions. It consumes no primary source and adds no external hypothesis.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no execution begins before the freeze is merged.**

## Why this round exists

Act 1's Q4 answered a question about an external text, and it did so with a **prose transposition**. Under the frozen evidence hierarchy of act 1, prose sits at level 3 and a Lean formalization of the transposed predicate sits at level 2 — "worth more than a prose transposition", in the freeze's own words. Act 1 deferred that upgrade to this round by design.

So this round is not bookkeeping. It is a **check on act 1**. The prose claim was:

> After transposing his column-stochastic left action to our row-stochastic right action, the factorization equation of `Γ(t←t₀) = Γ̃(t←t′) Γ(t′←t₀)` is the body of `PDivisible` exactly, with `s := t′` and `Λ := Γ̃(t ← t′)ᵀ`.

If the kernel confirms it, act 1's Q4 rises from level 3 to level 2 on its this-side half. **If the kernel refuses it, the kernel wins**, and act 1's Q4 receives an appended correction note under the same discipline act 1 applied to itself. That possibility is `RT3` below and is a real admissible outcome, not a formality.

## What is fixed before proving

These are the merged definitions this round builds on. They are quoted so the target is fixed and not remembered.

From `OIBridge/CausalReadback.lean`:

```lean
def IsRowStochastic (M : Matrix V V ℝ) : Prop :=
  (∀ i j, 0 ≤ M i j) ∧ ∀ i, ∑ j, M i j = 1

def PDivisible (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∀ s t : ℕ, s < t → t ≤ K → ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ

def PIndivisibleWithin (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ¬ PDivisible K Γ
```

A search of `OIBridge/` finds **no** existing column-stochastic predicate, so `IsColStochastic` is introduced by this round rather than reused. Nothing merged is restated or redefined.

## The four targets

**T1 — the predicate duality.** Define

```lean
def IsColStochastic (M : Matrix V V ℝ) : Prop :=
  (∀ i j, 0 ≤ M i j) ∧ ∀ j, ∑ i, M i j = 1
```

and prove `IsRowStochastic M ↔ IsColStochastic Mᵀ`, together with the dual direction `IsColStochastic M ↔ IsRowStochastic Mᵀ`. Both directions are stated because a single implication would leave the bridge one-way exactly where act 1 claimed an equivalence.

**T2 — the single-pair factorization bridge.** For matrices `A B Λ : Matrix V V ℝ`:

`(A = B * Λ ∧ IsRowStochastic Λ)  ↔  (Aᵀ = Λᵀ * Bᵀ ∧ IsColStochastic Λᵀ)`

This is the exact content of act 1's transposition, at one time pair, with the propagator moving from the right of a row-stochastic action to the left of a column-stochastic one.

**T3 — the family-level restatement.** Define `PDivisibleCol` in Barandes's orientation — propagator on the left, column-stochastic, acting on a family of transposed maps — and prove

`PDivisible K Γ  ↔  PDivisibleCol K (fun t => (Γ t)ᵀ)`

together with the immediate corollary for `PIndivisibleWithin`. This is where the equivalence becomes a statement about the *predicate*, not about one factorization instance.

**T4 — the two scope markers, made checkable.** Act 1 reported exactly two differences of `PDivisible` against the external equation: the **horizon** bound `t ≤ K`, and the admission of `s = 0` where the external range is `t > t′ > t₀` strictly. The horizon has no external counterpart and is left as a stated difference. The endpoint is claimed vacuous, and that claim is provable here:

`Γ 0 = 1 → IsRowStochastic (Γ t) → ∃ Λ, IsRowStochastic Λ ∧ Γ t = Γ 0 * Λ`

so the `s = 0` instances of `PDivisible` are discharged by `Λ := Γ t` whenever the family trivializes at the root, which `rootedMap R 0 = 1` supplies. Proving this converts "the extra case is vacuous rather than stronger" from an assertion into a lemma.

## Admissible outcomes

**RT1 — the bridge is kernel-closed.** All four targets proved, axiom-clean. Act 1's Q4 transposition stands at evidence level 2 on its this-side half.

**RT2 — closed with a named extra hypothesis.** T1 and T2 close, but T3 requires a hypothesis act 1's prose did not name (finiteness beyond `Fintype`, decidability, nonemptiness, or a trivialization condition). The hypothesis is named in the result and act 1's Q4 gets an appended note recording it. This is a partial confirmation, reported as one.

**RT3 — an orientation obstruction.** Some direction of T1, T2 or T3 is false, or provable only one way. Act 1's Q4 is then wrong in the corresponding direction and receives an appended correction note. The round reports the obstruction and does not repair act 1's prose silently.

**RT4 — blocked.** A target is neither proved nor refuted within the round. Recorded as open with what is missing. A failed proof attempt is never reported as a negative result.

## Prediction recorded before proving

**RT1 is predicted, with high confidence.** The ground is that `Matrix.transpose_mul` gives `(B * Λ)ᵀ = Λᵀ * Bᵀ` over a commutative semiring, transposition is involutive, and row and column sums exchange under transpose over a `Fintype` by `Finset.sum` commutation — so no step of T1–T3 needs anything act 1's prose omitted.

The prediction is recorded because a confident prediction that turns out wrong is the informative case, and recording it beforehand is what makes `RT3` a real outcome rather than a face-saving relabelling.

**No prediction is recorded on whether the horizon difference of T4 can be removed.** It cannot be removed — it is a genuine difference of quantifier domain — and the round does not attempt to.

## Mandatory controls

1. **No claim about any Barandes predicate.** Act 1 settled the definition axis at `BD3`. This round formalizes a transposition between two orientations of **our own** predicate; it does not identify `PIndivisibleWithin` with any external notion, and `BD3` is not reopened, softened, or re-derived.
2. **No primary source is consulted.** The round needs none. Any statement about what an external text says is out of scope, and act 1's determinations are cited rather than re-litigated.
3. **Kernel discipline.** No `sorry`, no custom `axiom`, no `native_decide`. Every named result carries a `#print axioms` line printing only `[propext, Classical.choice, Quot.sound]`.
4. **Nothing merged is restated.** `IsRowStochastic`, `PDivisible` and `PIndivisibleWithin` are used, not redefined. `IsColStochastic` and `PDivisibleCol` are new because no equivalent exists in `OIBridge/`.
5. **No manuscript edit.** Whatever is found, no manuscript, book, bibliography or publication edit occurs. The Explainer surface act 1 flagged stays on the backlog untouched.
6. **No sourcing inference.** Nothing proved here is described as OI *sourcing* anything. A transposition identity is a fact about matrices.
7. **Track separation.** Amendment 2's rule is binding both ways.
8. **No fifth condition**, and no deferred Arc D resource is adjudicated.
9. **If the kernel contradicts act 1, act 1 is corrected, not the kernel.** The correction is an appended note under act 1's own amendment discipline, and it is reported in this round's result rather than folded in quietly.

## Non-doings

Before freeze and during this round, do not:

- assert any relation between `PIndivisibleWithin` and an external predicate;
- reopen or re-derive act 1's `BD3` or `BR3`;
- consult a primary source;
- begin Arc D round 2 or Arc E work;
- edit manuscripts, books, bibliography or publication claims;
- adjudicate any deferred resource;
- describe a transposition identity as evidence for a correspondence.

## Execution discipline

- Freeze this preregistration by exact commit SHA **and blob SHA** before any Lean is written. **Blob identity is authoritative.**
- Once frozen, this file is immutable. Any execution-affecting correction is an append-only amendment, separately frozen, and committed before the work it affects.
- **Two PRs, in order.** A control-plane PR carrying this file and nothing else is reviewed, frozen and merged before any execution; then exactly one execution/result PR branched from the `main` that already carries the frozen blob.
- Final exact-head review is required after the kernel module, the guard, the result note and any registry updates are complete.
- No merge without an explicit owner direction after exact-head review.

## Allowed final report

The final report states separately:

1. each of the four targets, with its outcome and the named results that carry it;
2. the axiom line for every named result, and the count;
3. the outcome label `RT1`–`RT4`, with the prediction and whether it held;
4. whether the kernel confirmed or contradicted act 1's Q4 transposition, and if contradicted, the appended correction act 1 receives;
5. what the horizon difference of T4 remains, stated as a difference and not as a defect;
6. what a later Track B round could begin from, without executing it;
7. explicitly, that nothing here is a claim about any Barandes predicate and nothing here is a sourcing claim.
