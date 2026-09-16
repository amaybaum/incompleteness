# Track B act 16 — the cancellation question on the re-anchored-channel carrier: RESULT

Executed under the frozen control plane at this directory's `preregistration.md`, blob
`48099a3b334e8d01f31af706e8738cd49cfca774`, from the merge commit of that control plane,
`d05399020d05d4a7b6f662d2e069062452e7d6b4`, which the freeze fixes as this round's mandated base.

**The round's first act was the blob verification the freeze's lifecycle rule requires.**
`git rev-parse HEAD:verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/preregistration.md`
at the base returned `48099a3b334e8d01f31af706e8738cd49cfca774`, which is the blob the freeze names.
It was verified before any target was executed.

**The headline, stated once and then reported per target.** The freeze's central prediction is
**falsified**. It rated `RN3` (a)'s sign **negative at low** and rated `RN3` (b) **UNDECIDED at
medium**; the kernel returns `RN3-a⁺` and, through it, **line 1 of the `RN3` (b) hierarchy —
`RN3⁺`**. Act 15's exhibited triple is `𝒪₃`-cancelling as well — decided on `𝒪₃`'s own terms by
computing the channel, and **not** transferred from `𝒪₂`, where act 15's verdict stands exactly as
act 15 states it. The reversal is reported as the reversal it is, and the outcome is earned by a
proved triple and never by a search.

---

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It **creates new seal state** and alters no
existing seal constant. It lands **`E` → `L` → `P`, with `P` mandatory**.

| constant | what it holds | state in this execution |
| --- | --- | --- |
| `_RNC_BASE` | the mandated execution base — the merge commit of the control-plane pull request | set to `d05399020d05d4a7b6f662d2e069062452e7d6b4` |
| `_RNC_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** (`None`) |
| `_RNC_MERGE` | the landing merge `L` carrying `E` as its second parent | **present and unset** (`None`) |

**`_RNC_SEALED_HEAD` and `_RNC_MERGE` are unset at execution.** That is a statement about this
execution and stays true as one: pinning them here would make the execution's own head depend on
where it landed, and the pin commit `P` is the one commit entitled to set them.

**No existing seal constant is altered**, and the execution's diff against
`verification/lean/edge_rigidity_probe.py` **adds** the `R7-RNC` clause and changes nothing else in
the file. **Acts 13's, 14's and 15's seals are untouched**: `_CTI_BASE`, `_CTI_SEALED_HEAD`,
`_CTI_MERGE`, `_PQT_BASE`, `_PQT_SEALED_HEAD`, `_PQT_MERGE`, `_TCF_BASE`, `_TCF_SEALED_HEAD` and
`_TCF_MERGE` are read as invariants and never written, as are `_A12P_*`, `_SGT_*`, `_TSG_BASE` and
`_CLG_BASE`. An archive seal belongs to the round that set it.

**Before certification this execution absorbed no later `main`**: no merge from `main`, no rebase,
no amend, no force-push. Its single parent is the mandated base. **The claim is scoped to the
repository record.**

---

## 2. `RN0` — the bounded search, recorded in full

**`RN0` is a type-P target and carries no evidence level.** No Lean was written for it, and no
outcome of `RN0` is a theorem of this round.

### The file set, as the freeze bounds it

Taken from `git ls-tree -r --name-only B` at `B = d05399020d05d4a7b6f662d2e069062452e7d6b4`: every
`*.lean` file under `verification/lean-mathlib/` (168 files) and under `verification/lean/` (6
files); every `preregistration.md` and `result.md` under `verification/programmes/oi-qm/` (48
files); and `verification/ROADMAP.md` (1 file). **223 files in total.** Untracked package trees are
outside the set by construction, which is why the set is taken from the tree listing rather than
from the working directory.

### The question asked of each hit

Does this declaration decide, for some triple or for every triple `(U, W, K)`, any one of `C₃`, `L₃`
or `R₃` — that is, does it state a conclusion about `AnchoredChannel a₀` applied to a **relative
object** `U_t U_sᴴ` or to its composite counterpart, at every time pair — or a statement from which
such a conclusion follows by consuming merged results alone, with the consumption exhibited?

### The per-term record

| term | hits | files | recorded answer |
| --- | --- | --- | --- |
| `AnchoredChannel` | 61 | 5 | **Does not supply it.** Exactly one file in the set is a Lean file: act 14's `OIBridge/ThreadingObservability.lean`, with 42 occurrences. Every declaration there applies the channel to a **single-time** object. The four prose files are act 14's two artifacts, act 15's preregistration and this round's own control plane. |
| `ReanchoredChannel` | 5 | 1 | **Not relevant to the question.** All five occurrences are in this round's own control-plane blob, which chronology clause 1 names as the single permitted exception; no merged Lean declaration of that name exists at `B`. |
| `CrossFibreGram` | 29 | 5 | **Does not supply it.** Act 14's module carries 22 occurrences; each states a law about `Y_{i i'}(M)` for a single matrix `M`, or about `M K` and `W M`, and none is stated over a relative object at every time pair. |
| `ThreadingRelated` | 21 | 7 | **Not relevant to the question.** `≈_T` names the relation whose residual the pair generates; no occurrence carries a conclusion about the anchored channel of a relative object. |
| `LeftFibreGroup` | 77 | 13 | **Not relevant to the question.** Every occurrence is a membership hypothesis or a law about `𝒢_L` on the fibre Gram, the cross-fibre Gram or the per-time lift. |
| `StrongAnchorStabilizer` | 76 | 13 | **Not relevant to the question.** Every occurrence is a membership hypothesis or a law about the strong class on single-time anchored data. |
| `cancel` | 555 | 94 | **Does not supply it.** The overwhelming majority are Mathlib-idiom identifiers (`mul_cancel`, `sub_cancel`, and the like) in files with no bearing on the pair. The substantive occurrences are act 14's `PQ3` (d) fork and act 15's `CF1`–`CF5`, all indexed to `𝒪₂`, plus act 14's `pq3b_no_cancellation_on_anchoredChannel`, indexed to `𝒪₁`. |
| `redundan` | 276 | 25 | **Does not supply it.** Every redundancy verdict in the merged record names its carrier and every one names `𝒪₀`, `𝒪₁` or `𝒪₂`. None names `𝒪₃`. |
| `PQ0` | 46 | 8 | **Does not supply it.** `PQ0` (a) is universal over matrices `M` and at `M = U_t U_sᴴ` gives this round's `RN1`; `RN1` relates two carriers' equalities and decides none of `C₃`, `L₃` and `R₃`. `PQ0` (c) gives `𝔇_{a₀}(M K) = 𝔇_{a₀}(M)` for strong `K`, which is not the shape of any of the three. `PQ0` (b) and (d) are the diagonal and the trace law. |
| `PQ2` | 53 | 8 | **Does not supply it.** `pq2b_anchored_column_identity` is about the per-time lift's anchored columns, and the relative object is **not** of the form `M K`: `(U_t K_t)(U_s K_s)ᴴ` is `U_t K_t K_sᴴ U_sᴴ`, which no merged statement about `M K` reaches. |
| `PQ3` | 225 | 8 | **Does not supply it.** `PQ3` (a) is `𝒪₀`; `PQ3` (b) is `𝒪₁` and is stated for a single matrix `M` and a single constant strong `K`; `PQ3` (c) and `PQ3` (d) are `𝒪₂`. |
| `PQ4` | 51 | 8 | **Not relevant to the question.** `PQ4` describes what a selector would have to select, conditionally and never as a proposal; it decides no predicate on any carrier. |
| `CF1` | 27 | 5 | **Does not supply it.** `CF1` is an identity of **matrices** about the composite's relative object; it says nothing about the value of any carrier on it. |
| `CF5` | 55 | 5 | **Does not supply it.** `CF5` is `PQ3-d⁺` on `𝒪₂`, an existential about the relative candidate. It decides no `𝒪₃` predicate, and reading it as bearing on `𝒪₃` is the carrier rule's first named failure. |
| `CT2` | 81 | 12 | **Not relevant to the question.** `CT2` (a) and (b) are act 13's determination statements about the column Gram data. |
| `CT3` | 189 | 13 | **Not relevant to the question.** `CT3` (G) is about the fibre cross-Gram under strong-right families; `CT3` (d) is act 13's fork and belongs to act 13. |

**The one near miss, recorded so that it is not mistaken for a hit.** The string
`AnchoredChannel a₀ (U t * (U s)ᴴ)` does occur once in the merged Lean record, at line 42 of act 14's
`OIBridge/ThreadingObservability.lean`, inside act 14's **prose carrier table**, where it names `𝒪₃`
as a carrier. That is a definition of the carrier and not a statement about any triple; it decides
none of `C₃`, `L₃` and `R₃`.

### The outcome, in the status rule's frozen wording

**Outcome reached: `RN0`-silent.** The prediction was **negative at high strength**, and the finding
**matches** it.

> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record decides none of `C₃`, `L₃` and `R₃`, for any triple or for all triples: it
> contains no statement about the anchored channel of a relative object under a constant in-fibre
> left move together with a time-dependent strong right gauge. **The finding is that the record is
> silent on the point.** It is not a finding that any such statement is false, not a finding that
> one is unprovable, and not a bound on what a later round could prove.

**Reconstructive inference is refused as a finding here.** No sentence of this section reads "the
record must contain X, because otherwise Y would not have been written". **Nor is `RN0` treated as
retro-evidence about anything this round proved**: what `RN1`, `RN2`, `RN3` and `RN4` establish is
this round's own, and what `RN0` records is what was in the record before this round wrote anything.

---

## 3. `RN1` — the refinement, with its bounded reading and its refused converse

**Outcome reached: `RN1`-positive.** The prediction was **positive at high strength**, and the
outcome **matches** it.

> `𝒪₃`-equality implies `𝒪₂`-equality, universally, at evidence level 2, through act 14's merged
> `PQ0` (a) consumed. **This is a refinement within the re-anchored row and nothing more**: it
> asserts no implication between the one-time row and the re-anchored row in either direction, its
> converse is refused and not claimed, it asserts no strictness, and it says nothing about which
> carrier is observable. **No carrier is adopted as the physical one.**

The kernel carries it in two forms. `rn1_reanchored_refines_relative` is the statement at one time
pair: for every anchor, every pair of lifts over the same finite carrier and all `t, s`, if
`AnchoredChannel a₀ (U'_t U'_sᴴ) = AnchoredChannel a₀ (U_t U_sᴴ)` then
`RelativeCandidate a₀ U' t s = RelativeCandidate a₀ U t s`.
`rn1_reanchored_refines_relative_family` is the whole-family form every later target consumes. The
route is the one the freeze names and no other: act 14's merged `pq0a_readback_is_diagonal_action`
read at `M = U_t U_sᴴ`, applied at the matrix unit `E_{jj}` and the output entry `(i, i)`, followed
by injectivity of the real-to-complex coercion.

**The converse is refused in terms.** `𝒪₂`-equality does not give `𝒪₃`-equality; nothing here says
it does; and no later target of this round uses a converse. In particular `C₃` is nowhere concluded
from `C₂` — that step would make `RN3` (a) true by fiat and is exactly the error the fork exists to
decide. `RN3` (a) is settled by computing the channel from the cross-fibre Gram of each relative
object.

**No strictness is claimed.** This round does not prove that the implication fails to reverse and
does not assert that it does. **`𝒪₃` is not claimed to be strictly finer than `𝒪₂`.**

---

## 4. `RN2` — the two contrapositives and the instantiation, reported separately

**Outcome reached: `RN2`-all-three.** Parts (a) and (b) were predicted **positive at high**, part
(c) **positive at medium**; all three **match** their predictions.

> For every triple, a left part that moves `𝒪₂` moves `𝒪₃`, and a strong-right part that moves
> `𝒪₂` moves `𝒪₃`; and act 15's exhibited triple therefore satisfies `¬L₃` and `¬R₃`. All three at
> evidence level 2. **These supply two of the three conjuncts of the `𝒪₃` fork and not the third.**
> Nothing here is evidence that `C₃` holds on that triple or on any triple, nothing here is
> evidence that an `𝒪₃`-cancelling triple exists, and **act 15's `PQ3-d⁺` is consumed at its own
> existential strength and is not carried from `𝒪₂` to `𝒪₃`.**

**(a) and (b)**, as conjuncts of one theorem `rn2_nontriviality_transfer`: for every triple,
`¬L₂ → ¬L₃` and `¬R₂ → ¬R₃`, each the whole-family form of `RN1` contraposed, at the pair
`(U, W U_·)` and at the pair `(U, U_· K_·)` respectively.

**(c)**, as `rn2c_act15_triple_nontrivial_on_reanchored`: act 15's merged
`cf5_cancelling_triple_exists` is obtained at its own **existential** strength, its eleven conjuncts
destructured, and (a) and (b) applied to the two `𝒪₂` inequalities its statement carries explicitly.
The resulting existential records, for that triple, the lift's coherence, `LeftFibreGroup W`, the
strong family, the threading relation, `C₂` as act 15 states it, and `¬L₃ ∧ ¬R₃`.

**What `RN2` does not do, said in terms.** It supplies **two** of the three conjuncts of the `𝒪₃`
fork and **not** the third. It is not evidence that `C₃` holds on act 15's triple or on any triple;
whether `C₃` holds is `RN3` and is settled there on its own kernel evidence. It is not evidence that
an `𝒪₃`-cancelling triple exists, because a triple satisfying two of three conjuncts is not a
witness. It does not carry `PQ3-d⁺` from `𝒪₂` to `𝒪₃`: what travels is exactly the two
contrapositives `RN1` licenses and nothing else. **`GL2`, `CT4` and `CL1` are not enlarged** from
existential to universal by anything here.

---

## 5. `RN3` (a) — the decision about act 15's triple on `𝒪₃`

**Outcome reached: `RN3-a⁺`.** The freeze predicted that `RN3` (a) would **resolve** at high strength
— it did — and predicted its **sign negative at low strength**. **That sign prediction is
falsified.** The freeze's own recorded reason for the negative rating was that act 15 built its
triple to cancel on `𝒪₂` and nothing in that construction constrained it on `𝒪₃`. The kernel returns
the opposite, and it is reported as the reversal it is.

> Act 15's exhibited triple satisfies `C₃` at every time pair, at evidence level 2. With `RN2` (c)
> it is therefore `𝒪₃`-cancelling, and `RN3` (b) reaches line 1 through it and through no other
> route. **This is a statement about `𝒪₃` and travels to no other carrier**, and it carries act 7's
> boundary — `D4b` negative, the readback the repository's own.

**The objects are pinned by the equations in the statement**, and those equations are act 15's own:
on `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`, with `w = swap((0,0),(0,1))`,
`u = swap((0,0),(1,1))` and `k = swap((0,1),(1,2)) · swap((0,2),(1,1))`, the constant left element is
`W = P(w)`, the lift is `U_t = P(1)` at `t = 0` and `P(u)` afterwards, and the strong family is
`K_t = P(1)` at `t = 0` and `P(k)` afterwards. No lift, gauge element, witness, matrix, triple,
entry value or pair is a top-level definition.

**The computation, and why it is not an accident of the readback.** At `(0,0)`, and at any pair of
times that behave alike, both relative objects are the identity permutation. At `(1,0)` the
composite's relative object is `w⁻¹ k u w` and the lift's is `u`, and their **anchored columns
differ**: the preimages of the anchored column set are `(1,2)` and `(1,0)` for the composite against
`(1,1)` and `(1,0)` for the lift. Yet every cross-fibre Gram entry agrees — both are supported on the
fibre pair `(1,1)` with the value `1` at `(0,0)` and at `(1,1)` and zero elsewhere, the off-diagonal
fibre pairs included. The pair `(0,1)` is the inverse of `(1,0)` and agrees for the same reason.
Because the anchored channel is a function of the cross-fibre Gram — act 14's merged
`anchoredChannel_eq_trace` — the two channels coincide as functions of the input state, at every
time pair.

**What `RN3-a⁺` does not establish.** It settles **one triple**. It is not a universal statement
about triples, and it is not a bound on what a later round could exhibit in either direction. It is
**not** a statement that `𝒪₃` and `𝒪₂` agree in general, and it is **not** a statement that either
carrier is observable. **Act 15's `PQ3-d⁺` on `𝒪₂` stands exactly as act 15 states it** and is not
weakened, qualified, revised or enlarged by this: the two are verdicts on different carriers, and
neither is evidence about the other.

---

## 6. `RN3` (b) — the fork on `𝒪₃`, at the highest line the kernel carries

**Outcome reached: line 1, `RN3⁺`.** The freeze predicted **UNDECIDED at medium strength**, rating
line 1 **not predicted, at low**. **That prediction is falsified**, by the route the freeze itself
names as the only one to line 1: "if (a) is positive, line 1 follows at once through `RN2` (c) and
this row is falsified."

> An `𝒪₃`-cancelling triple is exhibited: relative to the re-anchored-channel carrier, and under
> act 7's readback convention with `D4b` negative, the pair of a constant in-fibre left move and a
> time-dependent strong right gauge can be redundancy while neither part is. The triple's three
> conjuncts are proved in the kernel at evidence level 2, with the lift's coherence discharged from
> merged results and the two inequalities certified at named time pairs and named entries. **This
> is a statement about `𝒪₃` and travels to no other carrier**; act 14's `PQ3` (b) settles the
> analogous question negatively on `𝒪₁` and the two do not conflict, `𝒪₁` and `𝒪₃` being computed
> from different operations on the lift with no implication proved between them in either
> direction, and act 15's `PQ3-d⁺` on `𝒪₂` is a separate verdict on a separate carrier. **No
> carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and nothing here names,
> endorses or excludes a selection principle.

**The line reached is the highest the kernel actually carries, and no higher.** Line 1 is an
existential and it is what the kernel has: `rn3_plus_cancelling_triple_on_reanchoredChannel` exhibits
the triple with `C₃ ∧ ¬L₃ ∧ ¬R₃`. Lines 2 and 3 are the two universal propositions and **neither is
claimed**: `S₃` and `N₃` are both **refuted** by the exhibition, not proved, and the refutation is
recorded in the weaker direction the kernel establishes — `rn3_not_no_cancelling_on_reanchoredChannel`
proves that `N₃` is false, and `¬S₃` follows because `S₃` implies `N₃`. **That direction is reported
as following, not as separately proved.**

**The three conjuncts, and how each is earned.**

- `C₃` at every time pair is `RN3-a⁺`, computed in the kernel from the cross-fibre Gram of each
  relative object and never transported from `C₂`.
- `¬L₃` and `¬R₃` are `RN2` (a) and (b) — the two contrapositives of `RN1` — applied to the triple's
  own `𝒪₂` separations, which are act 15's certified ones: `𝒪₂(W U_·)` is `1` where `𝒪₂(U)` is `0`
  at the time pair `(1, 0)` and the entry `(0, 0)`, and `𝒪₂(U_· K_·)` is `1` where `𝒪₂(U)` is `0`
  at the time pair `(0, 1)` and the entry `(0, 0)`.
- The two inequalities are **additionally certified on `𝒪₃` itself**, at named time pairs and named
  entries, as conjuncts of the exhibition: at the time pair `(1, 0)`, on the input state `E_{00}`
  and at the output entry `(0, 0)`, `𝒪₃(W U_·)` is `1` while `𝒪₃(U)` is `0`; at the time pair
  `(0, 1)`, on the same input state and the same output entry, `𝒪₃(U_· K_·)` is `1` while `𝒪₃(U)`
  is `0`.
- The lift's coherence and the composite's are discharged from merged results — act 7's
  `admissible_mul_of_fixes_anchor` and act 12's `left_preserves_admissible`.
- `C₂` is recorded as a conjunct of the exhibition and is obtained **from `C₃` through `RN1`**, in
  the one direction `RN1` runs. The converse is used nowhere.

**What `RN3` (b) did not do.** It reports no outcome at a strength the kernel does not carry. It
reports line 1 on an **exhibited** triple and not on an unexhibited construction, and not on the
strength of act 15's `PQ3-d⁺`, which is about `𝒪₂`. It does not report line 2 or line 3 at all,
because neither universal is proved and both are in fact refuted. **No settling outcome is reported
because a witness was sought and not found** — the opposite: a witness was sought and **found**, and
it is written out.

**One resemblance is recorded here so that it is not mistaken for a bridge, and this paragraph is
analysis and not evidence.** Lines 2 and 3 of this hierarchy would each have wanted a universal
theorem about a conjugation that does not move an anchored datum, and act 13's `CT3-d⁺` branch wants
one too. The anchored datum here is the anchored **channel** rather than the anchored readback, which
puts the two statements further apart rather than closer, and the two theorems quantify over
different things — act 13's over constant-left elements forced by `Ξ`-equality on strong-right-related
pairs, this round's over triples `(U, W, K)`. **Neither would establish the other**, neither line was
reached in any case, and no target of this round is stated over act 13's objects.

> **THE CLAUSE, carried at this mention — the result note's record of the structural resemblance at
> the fork.** `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column
> cross-Gram separates **every** strong-right threading — a question about one datum's separating
> power. This round asks whether a constant in-fibre left move and a time-dependent strong right
> gauge can cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to
> that carrier while neither part is — a question about cancellation between two parts of one
> relation, on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the
> other, and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED
> whatever this round returns, and no outcome of this round moves it in either direction.

---

## 7. `RN4` — the non-factorization consequence, on `𝒪₂` and on nothing else

**Outcome reached: `RN4`-positive.** The prediction was **positive at high strength**, and the
outcome **matches** it.

> Relative to the relative-candidate carrier, the redundancy subrelation of the threading
> equivalence does not factor as the product of the two parts' redundancy subrelations: there is a
> triple whose composite is redundant relative to `𝒪₂` while neither half is, at evidence level 2,
> consuming act 15's exhibition at its own existential strength. **This is a statement about `𝒪₂`
> and travels to no other carrier**, and it carries act 7's boundary. It does **not** say a
> selector is required, and it names, endorses and excludes no selection principle, connection or
> gauge fixing. **Act 14's `PQ4` (c) is not corrected**: its word is "together", the conjunctive
> reading, which is untouched; what is refuted is the factoring reading, and the two readings are
> recorded apart in the discrepancies section and nowhere else.

`rn4_redundancy_does_not_factor_on_relativeCandidate` carries two conjuncts. The first is act 15's
exhibition, restated over this round's frozen predicates: there is a triple with `C₂ ∧ ¬L₂ ∧ ¬R₂`.
The second is the consequence: the universal statement that a composite redundant relative to `𝒪₂`
has both halves redundant relative to `𝒪₂` is **false**. **No new witness is constructed**, and the
existential content is act 15's throughout.

**It adds nothing to act 15.** What `RN4` states is the consequence act 15's exhibition carries for
`PQ4` (c)'s factoring reading, and nothing further. It is not a claim about which choices a physical
selector would face, because no carrier is adopted as the physical one.

---

## 8. The carrier rule as honoured, clause by clause

**Every verdict in this round names its carrier, and no verdict is reported on a carrier other than
the one its proof is about.** The freeze's four consequences, checked one by one:

1. **`PQ3-d⁺` is about `𝒪₂`.** It is cited in this round only at `RN2` (c) and `RN4`, at its own
   existential strength. It is cited nowhere as bearing on `𝒪₃`'s fork beyond the two contrapositives
   `RN2` proves. In particular `RN3` (a) does **not** rest on it: `C₃` is computed, and had the
   computation gone the other way the outcome would have been `RN3-a⁻` with `PQ3-d⁺` untouched.
2. **`PQ3` (b) is about `𝒪₁`.** It is not cited as evidence about `𝒪₃` in either direction. `𝒪₁` and
   `𝒪₃` share the anchored channel `𝔇_{a₀}` as their value map, and **a shared construction is not a
   shared verdict**: `𝒪₁` applies `𝔇_{a₀}` to `U_t` and `𝒪₃` applies it to `U_t U_sᴴ`, and act 14
   records that no implication between the one-time row and the re-anchored row is proved in either
   direction. That act 14's `𝒪₁` answer is negative and this round's `𝒪₃` answer is positive is not
   a conflict: they are two carriers and two verdicts.
3. **The one refinement claimed is stated within the re-anchored row and nowhere else.** `RN1`
   proves `𝒪₃`-equality implies `𝒪₂`-equality. It says nothing about `𝒪₀` and `𝒪₁`, and its
   converse is refused.
4. **No carrier is adopted as the physical one, and none is asserted not to be.** Every `𝒪₂` and
   `𝒪₃` statement carries act 7's boundary — `D4b` negative, the readback the repository's own — at
   each use rather than once in a footnote.

**The three named failure modes of hazard 1 did not occur.** No sentence of this round reports act
15's `PQ3-d⁺` as bearing on `𝒪₃` beyond the two contrapositives `RN2` proves. No sentence reports act
14's `PQ3` (b) — the `𝒪₁` non-cancellation — as bearing on `𝒪₃` because both carriers are built from
`𝔇_{a₀}`. No sentence reports an `𝒪₃` outcome as bearing on `𝒪₂` in either direction; the one
`𝒪₂` statement in the exhibition, `C₂`, is derived through `RN1`'s licensed direction and is labelled
as such where it appears.

---

## 9. The frozen `P0` sentence for the case reached

The case reached is **Case B** — `RN0` silent, `RN1` and `RN2` land, `RN3` (a) reaches `RN3-a⁺`,
`RN3` (b) reaches line 1, and `RN4` lands. The freeze fixes Case B by substitution into Case A: the
**fork clause** and the **resolution phrase** take their line-1 forms, and the **transfer clause**
takes its `RN3-a⁺` form. **The `P0` row stays OPEN and its label does not change.** The sentence
appended to the row is, verbatim as the freeze composes it:

> `P0` remains open and two-part, and acts 14's and 15's answers relative to each frozen carrier of
> observables stand exactly as those rounds state them. The cancellation question is now asked of the
> one frozen carrier on which the merged record said nothing about the pair — the re-anchored-channel
> carrier — and on that carrier it is answered positively: relative to the re-anchored-channel
> carrier, under act 7's readback convention with `D4b` negative, the two parts can cancel, so the
> pair can be redundancy relative to that carrier while neither part is. What this round adds on that
> carrier is a refinement and two of the three conjuncts, together with the resolution: equality of
> the re-anchored channel at every time pair implies equality of the relative candidate at every time
> pair, so a part that moves the relative candidate moves the re-anchored channel, and act 15's
> exhibited triple therefore satisfies both non-triviality conjuncts on the re-anchored-channel
> carrier while its composite is redundant there at every time pair. On the named and bounded search
> this round records, the merged record decides none of the three conditions on that carrier for any
> triple. Relative to the relative-candidate carrier, act 15's `PQ3-d⁺` further gives that the
> redundancy subrelation of the threading equivalence does not factor as the product of the two
> parts' redundancy subrelations; act 14's `PQ4` (c) is not edited, its conjunctive wording being
> untouched. Act 13's `CT3` (d) stays UNDECIDED and is untouched; neither question answers the other.
> **No carrier is adopted as the physical one**, `P0`'s other part — what selects or constrains the
> Gram/orbit trajectory across time — is untouched, and nothing here names, endorses or excludes a
> selection principle.

**No composition closes `P0`**, and none reports either of its two parts closed. The sentence above
is the only wording this round reports for the row.

---

## 10. What no outcome licenses, and the status rule as honoured

The freeze's eighteen forbidden sentences, none of which appears in any artifact of this round, in
any paraphrase, in a summary line, an abstract, a table cell or a propagation line:

1. **"The question on `𝒪₃` is unresolvable."** Not written. The question is resolved at line 1, and
   nothing here calls any question unresolvable, undecidable or hard.
2. **Any transfer of a verdict between carriers, in any direction.** Not written; section 8 checks
   the three named cases clause by clause.
3. **"Act 15 was wrong."** Not written. `RN3-a⁺` is a verdict on `𝒪₃` about the same triple, and
   `PQ3-d⁺` is a verdict on `𝒪₂`; neither weakens, qualifies or revises the other.
4. **"`𝒪₃` is strictly finer than `𝒪₂`."** Not written. `RN1` proves one implication, and this round
   proves no strictness and asserts none.
5. **"No cancelling triple relative to `𝒪₃` exists."** Not written, and it is in fact refuted here.
6. **"A witness was sought and not found, so there is none."** Not written; a witness was found.
7. **Any sentence of `S₃`'s form on the strength of line 3.** Line 3 was not reached, and no sentence
   of `S₃`'s form appears in any paraphrase: `S₃` is refuted here, not asserted.
8. **"The record's silence shows the statement sought is false."** Not written. `RN0`'s finding is
   that the record is silent, and **silence is a finding, not a truth value**.
9. **Any sentence carrying an outcome of this round to act 13's `CT3` (d), or an ingredient of
   `CT3` (d) to this round.** Not written. The anti-conflation clause governs:
   > **THE CLAUSE, carried at this mention — the result note's list of what no outcome licenses.**
   > `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
   > separates **every** strong-right threading — a question about one datum's separating power. This
   > round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
   > cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that
   > carrier while neither part is — a question about cancellation between two parts of one relation,
   > on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.
10. **"The threading freedom is gauge" or "the threading freedom is physical."** Not written; there
    is no carrier-free verdict here and every verdict names its carrier.
11. **"Carrier `𝒪ₓ` is the physical one", or "carrier `𝒪ₓ` is not the physical one."** Not written.
12. **"`P0` is closed", or "`P0`'s threading part is closed."** Not written; the row stays OPEN and
    two-part.
13. **"The selection principle is …", "the connection is …", "the gauge fixing is …"** No sentence of
    this round begins that way, and none asserts or denies that a connection or gauge fixing exists
    or suffices. **`RN4` in particular does not say a selector is required**, on any carrier.
14. **"Act 14's `PQ4` (c) is corrected."** Not written; its two readings are **recorded** in
    section 15 and act 14's merged text stands as written.
15. **"Act 14 asked its fork on `𝒪₃`."** Not written; the role-description seam is **recorded** in
    section 15 and no reading of it is chosen.
16. **"OI and QM are inequivalent."** Not written. Two lifts differing is not two theories differing,
    and the established finite observable-law correspondence is untouched.
17. **Any sentence about Track I, or about Source B or Source C.** None appears. **Only Source A is
    adjudicated**, and Track I is not touched in either direction.
18. **Any import from the substratum Lemma 24.1 rounds.** None. A shared word is not a bridge.

**The status rule as honoured.** Each target above is reported with exactly the sentence the freeze
fixes for the outcome reached, quoted verbatim: `RN0`-silent, `RN1`-positive, `RN2`-all-three,
`RN3-a⁺`, `RN3` (b) line 1 `RN3⁺`, and `RN4`-positive. No outcome chose its own wording, and no
target is reported at a strength the kernel does not carry.

**The named hazards, checked.** Hazard 3 — reading `RN1` as an equivalence — did not occur: the
converse is used nowhere, and `C₃` is never concluded from `C₂`. Hazard 5 — treating `RN2` as two
thirds of a witness — did not occur: the third conjunct is proved, not inferred from the other two,
and no sentence reads "so only `C₃` remains, and it plainly holds". Hazard 10 — a reader supplying a
missing universal theorem from background knowledge — did not occur: every step is discharged from a
merged result cited by name or written out in the kernel, and in particular no step of the form "of
course a unitary conjugation does not change a partial trace" appears. Hazard 11, the conjugation
trap: anchored columns, conjugates, channel entries and separating entries are computed through
`permMatrix_apply_eq`, `permMatrix_mul` and `conjTranspose_permMatrix`, never read off a constructor.
Hazard 12, forgetting the anchor: `AnchoredChannel a₀`, `readback a₀` and the strong class all carry
`a₀` throughout and no statement silently changes which configuration is anchored. Hazard 17 —
enlarging `PQ3-d⁺`, `GL2`, `CT4` or `CL1` from existential to universal — did not occur. Hazard 18 —
touching `P0`'s other part — did not occur: **what selects or constrains the Gram/orbit trajectory
across time is not asked, not bounded and not prejudged here, and no outcome reached bears on it in
either direction.** Hazard 19 — consuming a sibling round's result because it is present at the
mandated base — did not occur: **the anti-contamination invariant is honoured**, and the start-state
table is the complete list of what this round consumed.

---

## 11. The relation to acts 11, 12, 13, 14 and 15

**Every merged label consumed, none revised.** `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`,
`TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(d), `PQ4`,
`CF0`, `CF1`, `CF2`, `CF3`, `CF4` and `CF5` are consumed at their own strengths and none is revised,
enlarged or restated. The definitions of acts 7, 10, 11, 12, 13, 14 and 15 are **reused, not
redefined**; in particular `AnchoredChannel` and `RelativeCandidate` are consumed and neither is
restated.

The load-bearing consumptions, named: act 14's `pq0a_readback_is_diagonal_action` is the whole of
`RN1`; act 14's `anchoredChannel_eq_trace` and `anchoredChannel_unit` are how every `𝒪₃` value in
`RN3` is computed; act 15's `relativeCandidate_of_permMatrix` is how every `𝒪₂` value is computed;
act 15's `cf5_cancelling_triple_exists` is consumed at its existential strength at `RN2` (c) and at
`RN4`; act 7's `admissible_mul_of_fixes_anchor` and act 12's `left_preserves_admissible` discharge
coherence. **The four carriers are act 14's**, frozen there with their presuppositions, and none is
adopted as the physical one and none is asserted not to be.

**Act 13's `CT3` (d) is still UNDECIDED and is untouched by this round.** No target of this round is
carried by it, no target cites it as evidence, and no determination changes sign or strength because
of it.

> **THE CLAUSE, carried at this mention — the result note's statement of the relation to the earlier
> acts.** `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column
> cross-Gram separates **every** strong-right threading — a question about one datum's separating
> power. This round asks whether a constant in-fibre left move and a time-dependent strong right
> gauge can cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to
> that carrier while neither part is — a question about cancellation between two parts of one
> relation, on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the
> other, and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED
> whatever this round returns, and no outcome of this round moves it in either direction.

**The freeze's second named hazard, and how it was avoided.** The two questions are structurally
similar — both turn on a constant left element interacting with a strong right family — and the
specific failure guarded against is an artifact of this round reporting an outcome as bearing on
`CT3` (d), or citing `CT3` (d)'s ingredients as evidence here. Neither happened. Nothing in the Lean
module is stated over `CT3` (d)'s objects, and act 13's `ct2a_relative_conj` — which is `CT3` (d)'s
neighbourhood — is consumed nowhere in this round's proofs.

> **THE CLAUSE, carried at this mention — the result note's account of the freeze's second hazard.**
> `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
> separates **every** strong-right threading — a question about one datum's separating power. This
> round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
> cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that
> carrier while neither part is — a question about cancellation between two parts of one relation,
> on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the other,
> and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
> this round returns, and no outcome of this round moves it in either direction.

---

## 12. The definition budget

| slot | definition | state |
| --- | --- | --- |
| 1 | `ReanchoredChannel` — the `𝒪₃` value at one time pair | **fired** |
| 2 (conditional) | an `𝒪₃`-cancelling-triple predicate | **unused** |

`verification/lean-mathlib/OIBridge/ReanchoredChannelScope.lean` contains exactly one top-level
`def`, `ReanchoredChannel`, in the freeze's name and with the freeze's body:
`ReanchoredChannel a₀ U t s := AnchoredChannel a₀ (U t * (U s)ᴴ)`. The conditional second slot was
**not** needed: `RN2` and `RN3` are stated readably with the conjuncts written inline, as acts 14 and
15 wrote theirs. **No third definition was introduced** and **no amendment was needed**. No lift,
gauge element, witness, matrix, triple, entry value or pair is a top-level definition — each is a
bound variable pinned by an equation in the statement that needs it.

---

## 13. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The guard tag is **`R7-RNC`**, created by this execution pull request, and it pins
both halves: this round's preregistration blob by content at its exact path, and the execution
ancestry, fail-closed. The ancestry question is asked of the real `pull_request.head.sha` from the
Actions event payload and never the synthetic merge commit; an unresolvable head fails closed with no
fallback; and the check requires `B` to be an ancestor of `H` **and** every commit in
`git rev-list H ^B` to be itself a descendant of `B`. The guard recovers whatever history it needs
and fails if recovery fails.

**`_RNC_SEALED_HEAD` and `_RNC_MERGE` are unset at execution.** After the landing merge `L` the
mandatory pin commit `P` sets them to `E` and to `L`, moving the clause to archive mode, where the
same strong check is re-run against the sealed object.

**The seal-integrity clause excludes this round's own triple.** `_rnc_prior_seals` checks acts 13's,
14's and 15's triples and says nothing whatever about `_RNC_BASE`, `_RNC_SEALED_HEAD` or `_RNC_MERGE`
— the shape act 15's `_tcf_prior_seals` established and the shape this freeze's chronology clause 9
intends. A clause fixing this round's own pins at `None` for all time would contradict clause 7,
under which `P` must set them, and the guard would then pass at no commit once the round landed.

### The six preconditions, checked at `B` with the freeze's own commands

| # | precondition | result |
| --- | --- | --- |
| 1 | this control plane is merged and `B` is its merge commit | **PASS** — `git rev-list --parents -n 1 B` shows two parents, `59cfd54d` and `7cd82504`; the preregistration blob at `B` hashes to `48099a3b334e8d01f31af706e8738cd49cfca774` |
| 2 | act 15's execution is merged and sealed | **PASS** — `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, both non-`None` |
| 3 | act 15's module and result are in the tree | **PASS** — both `git cat-file -e` checks succeed |
| 4 | act 14's execution is merged and sealed | **PASS** — `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` |
| 5 | act 13's execution is merged and sealed | **PASS** — `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` |
| 6 | no act 16 execution object precedes the freeze | **PASS** — `git ls-tree -r B --name-only` lists exactly one path under this round's directory, `preregistration.md`, and no `OIBridge/ReanchoredChannelScope.lean` |

**No sibling lane's merge was a precondition of this round**, and the execution waited for none.

---

## 14. The axiom table — one line per named result

Every line is the module's own `#print axioms` output.

| named result | axioms |
| --- | --- |
| `reanchoredChannel_eq_trace` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredChannel_congr_crossFibreGram` | `[propext, Classical.choice, Quot.sound]` |
| `rn1_reanchored_refines_relative` | `[propext, Classical.choice, Quot.sound]` |
| `rn1_reanchored_refines_relative_family` | `[propext, Classical.choice, Quot.sound]` |
| `rn2_nontriviality_transfer` | `[propext, Classical.choice, Quot.sound]` |
| `rn2c_act15_triple_nontrivial_on_reanchored` | `[propext, Classical.choice, Quot.sound]` |
| `relativeObject_permMatrix` | `[propext, Classical.choice, Quot.sound]` |
| `crossFibreGram_permMatrix` | `[propext, Classical.choice, Quot.sound]` |
| `rn3a_act15_triple_cancels_on_reanchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `rn3_plus_cancelling_triple_on_reanchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `rn3_not_no_cancelling_on_reanchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `rn4_redundancy_does_not_factor_on_relativeCandidate` | `[propext, Classical.choice, Quot.sound]` |

**Twelve named results, nothing outside the three standard axioms, no `sorry`, no added axiom and no
`native_decide`.** `decide` over finite index types is used and is kernel-checked. **`RN0` is type P
and is not in this table**: it carries no evidence level and is settled by the frozen evidence rule
alone.

---

## 15. The discrepancies, recorded and not repaired

**Five items are recorded. None is repaired, and the freeze is not edited.** The preregistration is
immutable once merged; an execution that diverges records the discrepancy and does not repair the
freeze.

**(1) Four of the freeze's start-state blobs differ at the mandated base.** The freeze pins its
start state at its **own** base, `main` at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`, while the
execution's mandated base is the control plane's merge commit `d053990`. All eighteen read-only
blobs match at `d053990`. The four files the round **writes** do not:

| path | freeze's pin | blob at `d053990` |
| --- | --- | --- |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | `78e36c1d3648fd318f5b9c3de7bb312e6a27a99f` |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | `f32855589c5150068ffaa22826354260281f605d` |
| `verification/lean-mathlib/OIBridge.lean` | `0bff51eb9cc3c22859da2ac0efc622910e77d7b4` | `c6f77a8473de1bd464b814419430343a0d1847ee` |
| `verification/lean-manuscript-census.json` | `3e968e6c970301be5ba0b9631b234c957a6222d1` | `3e23ceed1dc7751a647c59de30e8b38820584414` |

The cause is the one the freeze itself names: sibling lanes merged into `main` between the freeze's
base and the control plane's merge. **Nothing from those lanes is consumed here**; the four files are
appended to exactly as this round's own row in the freeze's table directs, and no sibling round's
result, label, number, prediction or finding is read, cited or compared.

**(2) Act 14's `𝒪₃` role-description seam.** Act 14's result note, lines 123–125, names `𝒪₃` as the
carrier "where the cancellation fork is asked", while act 14's fork as stated at its
preregistration's lines 409–412 — and as act 15 answered it — is asked on `𝒪₂`. **This is recorded
as a seam in the merged record and is not repaired, not corrected, not reinterpreted and not
normalized.** Act 14's merged text stands exactly as act 14 wrote it, and this round asserts nothing
about what act 14 "meant". What this round does instead is ask the question of `𝒪₃` explicitly under
labels of its own, `RN0` through `RN4`. **No target of this round is carried by this seam**, and no
prediction changed sign or strength because of it.

**(3) Act 14's `PQ4` (c) carries two readings, and they are not equivalent.** On the **conjunctive**
reading a selector must supply both choices, which says nothing about whether the two may be made
independently. On the **factoring** reading a selector's job decomposes into two separate choices,
one per part, so that fixing each part's class fixes the composite's. `PQ4` (c)'s word is "together",
which is the conjunctive reading, and **the conjunctive reading is untouched by anything in this
round**. What `RN4` refutes is the factoring reading, on `𝒪₂`, and it says so in those words.
**Act 14's merged text stands exactly as act 14 wrote it**; nothing here edits it, reinterprets it or
normalizes it.

**(4) The freeze's central prediction is falsified, in two rows.** `RN3` (a)'s sign was predicted
**negative at low** and the kernel returns **`RN3-a⁺`**; `RN3` (b) was predicted **UNDECIDED at
medium** and the kernel reaches **line 1, `RN3⁺`**. Both rows are reported as reversed rather than
quietly satisfied, and both reversals travelled the route the freeze itself named as the only route
to line 1. The freeze's recorded reason for the low negative rating — that act 15 built its triple to
cancel on `𝒪₂` and nothing in that construction constrained it on `𝒪₃` — is the freeze's **reason**
and never was a finding; what the kernel returns is the outcome. **The freeze is not edited**, and
the two prediction rows stand as written.

**(5) Line 1's assembly in the kernel differs from the freeze's stated route, in plumbing and not in
content.** The freeze says line 1 is earned by "`RN3-a⁺` together with `RN2` (c)". `RN2` (c)'s
witness is obtained from `cf5_cancelling_triple_exists`, whose witness is an **existential** and is
therefore opaque: the kernel cannot identify it with the triple `RN3` (a) pins by equations, and no
merged statement licenses doing so. So the line-1 theorem re-derives the **pinned** triple's own two
`𝒪₂` separations from act 15's merged `relativeCandidate_of_permMatrix`, and applies `RN2` (a) and
(b) — the same two contrapositives `RN2` (c) uses — to obtain `¬L₃` and `¬R₃`. `RN2` (c) is stated
and proved separately, exactly as the freeze specifies, consuming `CF5` at its own existential
strength. **Act 15's `CF5` is neither re-proved nor revised**: what is re-derived is the pinned
triple's own data, not act 15's theorem. This is recorded and the freeze is not repaired.

---

**Sources.** Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** =
arXiv:2507.21192v1, **C** = arXiv:2309.03085v2. **Only Source A is adjudicated. Track I is not
touched**, in either direction, and neither branch is evidence for the other. **No manuscript was
edited**, and nothing under `papers/` or `book/` was changed.

**The direct-branch statement is unchanged:** `D4a` positive on the direct branch; `T1` **necessary,
not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what fraction of OI
lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.
