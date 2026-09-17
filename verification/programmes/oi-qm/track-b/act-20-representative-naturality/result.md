# Track B act 20 — what "gauge-natural" means: the naturality classification: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
**`131783f48ac492fdfdc46072aee3f39278973622`**, from `main` at
**`84f27b50198ee31c224e31284905ff6c284ea9db`** — the merge commit of that control plane, which
`AGENTS.md` `§A.37` fixes as this round's mandated execution base and which this execution verified
by blob as its first act, before any target was executed.

**Outcome reached: `CLASS-TWISTED-NOT-STRICT`, with `SEP-STRICT` on both sides of `RNT5`.**

**Every target of this round landed at the full evidence bar frozen for it. No target is
UNDECIDED.**

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It creates new seal state — a new Lean
module with new named results, and a new `R7-*` ancestry/archive guard clause — and it lands
**`E` → `L` → `P`, with `P` mandatory**.

| constant | what it holds | state at this execution |
| --- | --- | --- |
| `_RNT_BASE` | the mandated execution base | set to `84f27b50198ee31c224e31284905ff6c284ea9db` |
| `_RNT_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** |
| `_RNT_MERGE` | the landing merge `L` | **present and unset** |

**`_RNT_SEALED_HEAD` and `_RNT_MERGE` are unset at execution.** They are set by the mandatory pin
commit `P` after the landing merge `L`, and not by this execution: pinning them here would make the
execution's own head depend on where it landed. That is a statement about this execution and stays
true as one.

**No existing seal constant is altered.** `_XTS_*`, `_TRJ_*`, `_RNC_*`, `_TCF_*`, `_PQT_*`,
`_CTI_*`, `_A12P_*`, `_SGT_*`, `_TSG_BASE` and `_CLG_BASE` are read and never written, and the
execution's diff against `verification/lean/edge_rigidity_probe.py` **adds** the `R7-RNT` clause and
changes nothing else in the file. **Act 19 set no seal triple**, so there is none to read and none
is invented.

**The base-blob verification is recorded.** `git cat-file -p B:verification/programmes/oi-qm/track-b/act-20-representative-naturality/preregistration.md | git hash-object --stdin` returns
`131783f48ac492fdfdc46072aee3f39278973622`, which is the blob the freeze names and the blob the
`R7-RNT` clause pins.

**The files this round writes** are the new module
`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, this result note, one import
line in `verification/lean-mathlib/OIBridge.lean`, one census entry in
`verification/lean-manuscript-census.json`, and the `R7-RNT` clause. **No manuscript file is
written and `verification/ROADMAP.md` is not written.**

## 2. The start state

Every path the freeze pins by blob was checked at `B`, and **every one matches**. The three files
this round writes onto carry their pinned blobs at `B` as well:
`verification/lean/edge_rigidity_probe.py` at `5cdd759534c9668c7f447b35a95ff888c973408a`,
`verification/lean-mathlib/OIBridge.lean` at `81814f25d9ea17aee2e15237af5bbfbe8dd92cfa`, and
`verification/lean-manuscript-census.json` at `86bda14f2f88335dfa4fd3fdb10f693ab134537e`.

**No start-state discrepancy arose in any pinned blob.**

**The anti-contamination invariant is honoured**, carried here in the freeze's own wording:

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

Sibling lanes present at `B` are not inputs and none was read. The start-state table is the
complete list of what this round consumes.

## 3. The ordering obligation's records

The obligation, in the freeze's own wording, which binds this execution:

> **The ordering obligation.** The three notions `N-STRICT`, `N-TWIST` and `N-ORBIT`, the transition
> `Φ_σ` and the obligations on the lift `Ψ_σ` are fixed by this control-plane blob and by nothing
> else. The execution states each in its Lean module in the wording this file freezes for it,
> **before** it attempts any discriminating result; and from the moment the first discriminating
> result enters the execution branch, **no commit of that branch alters the statement of any of the
> three notions, of the transition, or of the lift's frozen obligations, and none adds a notion,
> removes a notion, or changes which notions the classification is taken against.** The first
> discriminating result is whichever of these enters the branch earliest: the first proof about
> `Ψ_σ` beyond its two frozen obligations, the first appearance of either induced map, the first
> statement of either intertwining law, the first verdict on whether an induced map is the identity,
> the first verdict on strict naturality, and the first witness or refutation of the separation.
> **An execution that cannot demonstrate this ordering has not honoured it**, and the round is
> reported with the ordering obligation named as undischarged.

### 3.1 The definition commit

**`ce33bb2b4a3b2e6b473b4798d91ab08619649aed`.**

At that commit every definition the freeze freezes is stated in Lean in the freeze's own wording:
`StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition` and `RelabelLift`. Also
present are `RNT1` (a) and (b), which are statements about an arbitrary map on dilations and not
about this round's lift, and the lift's two frozen obligations `rnt2_lifting_property` and
`rnt2_admissible`.

**Nothing discriminating is present at that commit, and the absences are stated item by item
against the obligation's own list.** At `ce33bb2b` there is **no proof about `Ψ_σ` beyond its two
frozen obligations** — the module contains exactly two theorems naming `RelabelLift`, and they are
those two obligations, with unitarity of the output proved inline inside obligation (b) as the
first conjunct of its own conclusion rather than as a separate result; **no appearance of
`RelabelInducedLeft` or `RelabelInducedRight`**, neither name occurring anywhere in the tree at that
commit outside the frozen control plane; **no statement of either intertwining law**; **no verdict
on whether an induced map is the identity**; **no verdict on strict naturality**; and **no witness
or refutation of the separation**. **No product of the lift with a gauge element on either side
occurs anywhere in the tree at that commit.**

An auditor checks with `git show ce33bb2b` and `git diff 84f27b50 ce33bb2b`, whose whole content is
one import line and the new module.

### 3.2 The discrimination commit

**`b848b12723fe82d567671ab88cd6d63863e1735e`**, and the result that first crossed is, in the
obligation's own order, **the first appearance of either induced map** — the declarations
`RelabelInducedLeft` and `RelabelInducedRight`, budget slots 6 and 7 — **together with the first
statement of either intertwining law**, `rnt3_left_law` and `rnt3_right_law`. Both entered in that
one commit; no earlier commit on the branch carries any item from the obligation's list.

**The step at which the classification became available is named**: `relabelLift_mul`. Reindexing
both indices along one equivalence is conjugation by a permutation matrix, so the lift is
multiplicative, and that is what lets the induced maps be written without mentioning the dilation.

### 3.3 The immutability span

From the discrimination commit through the certified head `E`, **no diff touches the statement of
any frozen definition**. The command the freeze specifies, with its result:

```
$ git diff b848b12723fe82d567671ab88cd6d63863e1735e <E> \
      -- verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean
```

restricted to the declarations `StrictNatural`, `TwistedNatural`, `OrbitNatural`,
`RelabelTransition` and `RelabelLift`, **is empty**. The five declaration bodies were additionally
extracted and hashed at the definition commit, at the discrimination commit and at `E`, and the
three hashes are equal.

### 3.4 The `RNT5` collapse-configuration record

**No `SEP-COLLAPSE` was attempted on either side**, so no collapse configuration was committed on
either side and none is required. Both sides reached `SEP-STRICT`, whose configuration is part of
its existential witness and is pinned in the statement of the theorem that exhibits it.

## 4. The attestation set — three questions, answered as measurements

The questions, in the freeze's wording:

> **Q1 — INTENTIONAL.** Did the execution attempt or run any proof, search, decision procedure or
> numerical experiment intended to reveal the classification — which of the three notions the
> relabelling's lift satisfies, what the induced map on either side is, or whether either induced map
> is the identity?
>
> **Q2 — INCIDENTAL.** Did any compiler response, elaboration result, typeclass resolution, accepted
> or rejected term, or build output reveal any of that unintentionally?
>
> **Q3 — UNAIDED REASONING.** Did the execution **reason its way** to any information bearing on the
> classification **without running anything**?

**The partial-fact rule, as the freeze states it and as this execution applied it.** Learning that
an induced map is, or is not, the identity on **even one gauge element**, or that one of the three
notions fails on **one input**, is already discriminating; a question is answered YES if any such
partial fact was acquired, however incidentally, however small, and whether or not it was acted on.
**There is no threshold below which a fact about the classification does not count.**

**The span answered for is stated exactly, because the two readings of it differ.** The answers
below are for the span from the mandated base `84f27b50` **to the definition commit `ce33bb2b`** —
the period in which a contamination could have tuned a frozen definition to its own answer, which
is what act 19 closed over. What happened between `ce33bb2b` and the discrimination commit
`b848b127` is reported separately and openly below, because that is the period in which the
discriminating work was *supposed* to be done.

| question | answer, for `84f27b50` → `ce33bb2b` |
| --- | --- |
| **Q1 — INTENTIONAL** | **NO** |
| **Q2 — INCIDENTAL** | **NO** |
| **Q3 — UNAIDED REASONING** | **NO** |

**Q1, in detail.** The only things run in that span were: the baseline `lake build`, release gate
and edge-rigidity probe, all before any act 20 file existed; and `lake build` on the module carrying
the five frozen definitions, `RNT1` and the two `RNT2` obligations. No proof, search, decision
procedure or numerical experiment intended to reveal the classification was attempted or run. No
expression of the form `Ψ_σ (L * U)` or `Ψ_σ (U * K)`, and no occurrence of either induced map, was
elaborated in that span.

**Q2, in detail.** The compiler responses received in that span concerned `Matrix.submatrix`
unitarity, the direction of `Matrix.conjTranspose_submatrix`, and unused-section-variable linter
warnings. **None mentioned either induced map, either intertwining law, or any product of the lift
with a gauge element**, and no accepted or rejected term in that span bore on whether either induced
map is the identity or on whether the lift is strictly natural.

**Q3, in detail, and with the one thing that must be disclosed rather than left implicit.** The
execution did not, before the definition commit, compute or reason about the value of either induced
map, about whether either induced map is the identity, about whether the lift is strictly natural,
or about any product of the lift with a gauge element on either side, on paper or otherwise.

**What is disclosed, and why it is disclosed although the answer is NO.** The freeze pins act 19's
closure as a **locating control** and directs this execution to read it, and quotes its lines 71–80
in the freeze's own body at lines 174–186. Those lines record that an earlier execution had worked
out by hand that "a carrier relabelling's natural representative-level lift is a reindexing rather
than a left multiplication". That sentence was therefore in front of this execution before the
definition commit, **because the freeze put it there**. It is recorded here so that the owner can
weigh it rather than discover it. Three things bound it. It is a **record of a disclosure and not a
kernel result**, which the freeze states in terms at its lines 420–424 while requiring act 20 to
prove the defining property of whatever lift it builds from scratch, which this round did. It bears
on the **shape of the lift**, which is `RNT2`'s frozen obligation and is **not** on the ordering
obligation's list of discriminating results. And it says nothing whatever about either induced map,
about whether either is the identity, or about strict naturality, which are the round's
discriminating questions.

**How the lift's formula was actually arrived at, stated so that the derivation is checkable.** The
formula is read off from `RNT2` (a), which the freeze fixes: the obligation
`FibreGram a₀ (Ψ_σ U) i j k = FibreGram a₀ U (σ i) (σ j) (σ k)` determines, through act 12's merged
`fibreGram_apply`, that `Ψ_σ U` must carry the entry at `((i, a), (j, a₀))` to `U ((σ i, a), (σ j, a₀))`,
and the simultaneous relabelling of the visible component of both indices is the direct reading of
that. **The freeze's own obligation is what fixes it.**

**What happened between the definition commit and the discrimination commit, reported openly.** In
that span the exact intertwining law on both sides and the two `RNT4` (a) negatives were worked out
and compiled. That is the discriminating work, done after the definitions were fixed and committed,
which is what the ordering obligation requires. **No frozen statement changed at or after the
definition commit**, as §3.3 records.

**Per-side attestations for `RNT5`** are not required and none is given, because **no
`SEP-COLLAPSE` was attempted on either side**. A separation needs no such answer, its configuration
being part of its witness.

### 4.1 The history-integrity statement

**No commit on this branch was amended, reset, rebased over, cherry-picked over or force-pushed
away. There are no superseded SHAs.** The chain is linear from the mandated base:

```
84f27b50 (B, on main)  →  ce33bb2b (definition)  →  b848b127 (discrimination)  →  … → E
```

**One working-tree manoeuvre is disclosed for exactness, because it affects what was known when.**
After the definition commit, `RNT3` and the two `RNT4` (a) negatives were written and compiled
together on disk. Before the discrimination commit was created, the `RNT4` (a) section was moved out
of the working file and kept aside, so that the discrimination commit would carry exactly one
identifiable crossing — the induced maps and the intertwining laws — and it was restored into the
next commit. **So `RNT4` (a) was proved on disk before `b848b127` was created, and it entered the
branch at `21909c8`.** No history was rewritten by this; no commit was superseded; and all of it
postdates the definition commit, which is the boundary the obligation draws.

## 5. `RNT1` — the three notions, and the implication chain where it is valid

**Outcome reached: `CHAIN-PROVED`.**

> Strict equivariance implies twisted equivariance with the identity as the induced map, and
> twisted equivariance implies orbit preservation, both proved in the kernel at evidence level 2
> over this freeze's wording of the three notions. **The second implication is valid because the
> twisted notion carries its closure conjuncts**, and the proof names where each is used. **No
> converse is established by either implication**: that orbit preservation does not imply the
> twisted form is a separate question of this round, and that the twisted form does not imply the
> strict form is not a statement of this round at all.

The three notions are stated in the kernel as `StrictNatural`, `TwistedNatural` and `OrbitNatural`,
each in this freeze's wording, each a conjunction of a left clause against act 12's `LeftFibreGroup`
and a right clause against act 11's `WeakAnchorStabilizer a₀`. `TwistedNatural` takes its two maps
as **parameters, before the quantifiers over inputs**, and carries its two closure conjuncts.

| part | declaration | statement |
| --- | --- | --- |
| `RNT1` (a) | `rnt1_strict_imp_twisted` | `StrictNatural a₀ Ψ → TwistedNatural a₀ id id Ψ` |
| `RNT1` (b) | `rnt1_twisted_imp_orbit` | `TwistedNatural a₀ αL αR Ψ → OrbitNatural a₀ Ψ` |

**Where each closure conjunct of the twisted notion is used, named at the step.** In
`rnt1_twisted_imp_orbit` the left witness is `L' = αL L`, and the term `hαL L hLm` — the **first
closure conjunct** — is what supplies `LeftFibreGroup L'`; the right witness is `K' = αR K`, and the
term `hαR K hKm` — the **second closure conjunct** — is what supplies `WeakAnchorStabilizer a₀ K'`.
**The chain is not free**: drop either conjunct and the corresponding witness has no membership
proof. The countercontrol the freeze names for `RNT1` (b) is therefore discharged as a check and not
as a candidate, and the implication is **not** proved without using them.

`RNT1` (a) is the special case `αL = αR = id`: the two closure conjuncts are the hypotheses
themselves and the two intertwining conjuncts are `h.1` and `h.2` unchanged.

## 6. `RNT2` — the representative-level lift

**Outcome reached: `LIFT-BUILT`.**

> A single representative-level map on dilations is exhibited, named by one declaration, and proved
> at evidence level 2 to induce the carrier relabelling's transition on the fibre-Gram data and to
> carry admissible dilations to admissible dilations at a visible slice invariant under the
> relabelling. **This is a construction and not a uniqueness statement**: it does not say that this
> is the only lift of that transition, does not say it is canonical, and does not say it is the
> natural one. Every later verdict of this round is a verdict about this declaration.

The lift is the single declaration **`RelabelLift`**, the simultaneous relabelling of the visible
component of the row index and of the column index by `σ`, leaving the ancilla component alone:
entrywise `RelabelLift σ U (i, a) (j, b) = U (σ i, a) (σ j, b)`. The transition it lifts is
**`RelabelTransition`**, act 19's frozen `ΦP` statement carried into Lean.

**The two parts are reported separately.**

- **`RNT2` (a), the lifting property — proved.** `rnt2_lifting_property` :
  `FibreGram a₀ (RelabelLift σ U) = RelabelTransition σ (FibreGram a₀ U)`, at **every** dilation,
  with no admissibility hypothesis. The proof is entrywise through act 12's merged `fibreGram_apply`.
- **`RNT2` (b), admissibility — proved.** `rnt2_admissible` : at a visible slice invariant under the
  relabelling, `Γ (σ i) (σ j) = Γ i j`, the lift carries admissible dilations to admissible
  dilations **at the same anchor**. The invariance hypothesis is used at exactly one step. **The
  anchor is carried and not moved**: the lift fixes the ancilla component, so the anchored column
  `(j, a₀)` goes to `(σ j, a₀)` and `a₀` is unchanged.

**The countercontrol the freeze names for `RNT2` did not fire.** A construction lifting the
transition but leaving admissibility would have earned `LIFT-PARTIAL` with the failing conjunct
named; both conjuncts of `AdmissibleDilationAt` are discharged, so no conjunct is carried as a
hypothesis anywhere later in this round.

**Act 7's boundary is carried at this use of the visible family**, as at every other in this round:
act 7's `D4b` came back **negative** — Source A supplies no general map carrying the relative
candidate on the dilated carrier back to `V` — and the readback is the repository's own, frozen by
act 7's readback amendment. Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## 7. `RNT3` — the induced maps and the exact intertwining law, per side

**Outcome reached: `LAW-EXACT`.**

> Maps on the left and on the right gauge data are exhibited, independent of the dilation, and the
> exact intertwining law is proved in the kernel at evidence level 2 on both sides: the lift of the
> relabelling carries a gauge element on its input to the image of that element under the exhibited
> map on its output, as a universally quantified equality of matrices and **not** as an existential
> over the output. The exhibited maps carry each class into itself, and the four conjuncts are
> reported separately. **This settles the law for the lift this round built**, at the configuration
> named, and says nothing about any other lift of the same transition.

The two maps are the declarations **`RelabelInducedLeft`** and **`RelabelInducedRight`**, budget
slots 6 and 7, **both fired**. Each is the relabelling applied to the gauge element itself, and each
is **independent of the dilation**: neither takes a dilation argument.

**The four conjuncts, reported separately.**

| conjunct | declaration | what it states |
| --- | --- | --- |
| left closure | `rnt3_left_closure` | `LeftFibreGroup L → LeftFibreGroup (RelabelInducedLeft σ L)` |
| left law | `rnt3_left_law` | `RelabelLift σ (L * U) = RelabelInducedLeft σ L * RelabelLift σ U` |
| right closure | `rnt3_right_closure` | `WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (RelabelInducedRight σ K)` |
| right law | `rnt3_right_law` | `RelabelLift σ (U * K) = RelabelLift σ U * RelabelInducedRight σ K` |

`rnt3_law_exact` assembles the four into
`TwistedNatural a₀ (RelabelInducedLeft σ) (RelabelInducedRight σ) (RelabelLift σ)`, at **arbitrary**
`V` and `A` and at **every** anchor.

**The two intertwining conjuncts are equalities of matrices, universally quantified over the gauge
element and over the dilation, and they are not existentials over the output.** Each holds for
**every** pair of matrices, the class hypothesis being unused in the law itself and needed only for
the closure conjuncts. **`LAW-ORBIT-ONLY` was not reached and is not claimed**, and the
input-dependence obstruction the freeze names as its concrete shape did not arise: the step at which
the dilation drops out is `relabelLift_mul`, and no putative induced map ever had to mention `U`.

**The left side and the right side are proved and reported apart.** `rnt3_left_closure` transports
the off-fibre vanishing of act 12's `LeftFibreGroup` because `σ` is injective. `rnt3_right_closure`
is a different theorem against a different class: it carries act 11's anchor and reindexes the
anchored phases, `c ↦ c ∘ σ`. **That the two maps are given by the same formula is an observation
about the formula and is not one verdict covering both sides**, and nothing proved on one side is
transferred to the other.

`rnt3_orbit` records `OrbitNatural a₀ (RelabelLift σ)` as the **consequence** of the exact law
through this round's own `RNT1` (b), so that the weaker statement is visible as the weaker one. **The
exact law is what this round reports, and the weaker theorem is never reported as the stronger
one.**

Act 11's `StrongAnchorStabilizer a₀` sits inside the weak class with all coefficients `1`, by act
11's merged `strong_mem_weak`, so the strong right gauge is **the special case of the weak one that
it is**, and no separate notion was stated for it.

## 8. `RNT4` (a) — whether each induced map is the identity, per side

**Outcome reached: `ALPHA-NONTRIVIAL` on the left side, and `ALPHA-NONTRIVIAL` on the right side.
The two are separate verdicts, each earned separately.**

### 8.1 `RNT4` (a), the left side

> **THE FROZEN SENTENCE, carried at this mention — `ALPHA-NONTRIVIAL` on the LEFT side.**
> A gauge element of the class named is exhibited at which the induced map is not the identity,
> certified as a matrix inequality at a named entry, at evidence level 2. **This does NOT by itself
> establish that the lift fails strict equivariance**, which is a separate question with its own
> evidence bar, reported separately below. It is a statement about the induced map this round
> exhibited, for the lift this round built, on the side named.

`rnt4a_left_nontrivial` exhibits `σ = Equiv.swap 0 1` on `V = Fin 2` and the gauge element
`L = Matrix.diagonal (fun p => if p.1 = 0 then 1 else -1)`, proves `LeftFibreGroup L`, and certifies
the inequality **at the named entry `((0, a₀), (0, a₀))`**, where `RelabelInducedLeft σ L` takes the
value `-1` and `L` itself takes the value `1`. **One gauge element suffices and no search is a
substitute**; none was run.

### 8.2 `RNT4` (a), the right side

> **THE FROZEN SENTENCE, carried at this mention — `ALPHA-NONTRIVIAL` on the RIGHT side, which is a separate verdict against a separate class.**
> A gauge element of the class named is exhibited at which the induced map is not the identity,
> certified as a matrix inequality at a named entry, at evidence level 2. **This does NOT by itself
> establish that the lift fails strict equivariance**, which is a separate question with its own
> evidence bar, reported separately below. It is a statement about the induced map this round
> exhibited, for the lift this round built, on the side named.

`rnt4a_right_nontrivial` exhibits the same permutation and the same matrix read as a member of act
11's weak anchored stabilizer, proves `WeakAnchorStabilizer a₀ K` with anchored phases
`c j = if j = 0 then 1 else -1`, and certifies the inequality **at the named entry
`((0, a₀), (0, a₀))`**, where `RelabelInducedRight σ K` takes the value `-1` and `K` itself takes the
value `1`.

**Both negatives are exhibited at `V = Fin 2` with `A` arbitrary and the anchor arbitrary**, so
neither is a verdict reached only at `|A| = 1` and neither is reported as one. `ALPHA-TRIVIAL` was
not reached on either side and is not claimed.

## 9. `RNT4` (b) — whether the lift is strictly natural

**Outcome reached: `STRICT-NO`.**

> A gauge element and a dilation are exhibited for which the lift of the moved dilation and the
> move of the lifted dilation are different matrices, certified as an inequality at a named entry,
> at evidence level 2. **So the relabelling's lift is not strictly natural**, for the lift this
> round built, at the configuration named. **This is not a statement that no lift of the
> relabelling's transition is strictly natural**, which is a universal statement over lifts that
> this round does not attempt and does not earn.

**This was earned by its own exhibited pairs and by nothing else.** Neither proof mentions
`RelabelInducedLeft` or `RelabelInducedRight`, and neither is obtained from `RNT4` (a). **"The
induced map is not the identity, therefore the lift is not strictly natural" is a non-sequitur, it
is a forbidden sentence of this freeze, and it is not the argument made here.** `ALPHA-NONTRIVIAL`
is not offered as a countercontrol for part (b) and would not have been accepted as one.

| clause refuted | declaration | the exhibited pair | the two values at `((0, a₀), (0, a₀))` |
| --- | --- | --- | --- |
| left | `rnt4b_strict_fails_left` | `L = diagonal(1, -1)`, `U = 1` | `-1` and `1` |
| right | `rnt4b_strict_fails_right` | `U = 1`, `K = diagonal(1, -1)` | `-1` and `1` |

Each clause of `StrictNatural` is refuted on its own by its own exhibited pair, so the verdict does
not rest on either side alone. `rnt4b_not_strictNatural` records
`¬ StrictNatural a₀ (RelabelLift (Equiv.swap 0 1))` at `V = Fin 2` with `A` and the anchor
arbitrary. **`STRICT-YES` was not reached and is not claimed.**

## 10. `RNT5` (L) — is the per-input existential strictly weaker, on the LEFT side

**Outcome reached on the left side: `SEP-STRICT`.**

> **THE FROZEN SENTENCE, carried at this mention — `SEP-STRICT` on the LEFT side.**
> On the side named, a lift is exhibited that satisfies that side's per-input existential conjunct
> and admits no map making that side's fixed-map conjunct hold, at evidence level 2, with the
> objects and the configuration pinned by equations. **Together with this round's implication from
> the fixed-map form to the existential form, the implication is therefore strict on that side.**
> This is a statement at the configuration exhibited and on the side named; it is not a statement
> that the two formulations differ at every configuration, and it is **not a statement about the
> other side**.

The side is the **left** side, over act 12's in-fibre left moves. `rnt5_left_separation` exhibits a
map on dilations **pinned by two equations** — `Ψ 0 = 1` and `Ψ U = U` for every `U ≠ 0` — at the
configuration `V = Fin 2` with `A` and the anchor arbitrary, and proves both halves:

- the **left conjunct of `OrbitNatural`** holds for it, witnessed by `L' = L` at every non-zero
  dilation and by `L' = 1` at the zero dilation, the membership of the second witness coming from
  act 12's merged `one_leftFibreGroup` and the non-vanishing of `L * U` from the cancellability of a
  unitary left factor;
- **no** map `αL` exists carrying `LeftFibreGroup` into itself with `Ψ (L * U) = αL L * Ψ U` at every
  `L` and every `U`. Read at `U = 1` a fixed map would have to satisfy `αL L = L`; read at `U = 0` it
  would have to satisfy `αL L = 1`; and the exhibited `L = diagonal(1, -1)` is not `1`, at the entry
  `((1, a₀), (1, a₀))` where it takes the value `-1`.

**The input-dependence is the content of the separation**: the witness the existential supplies
genuinely depends on the dilation, and that is exactly what a map fixed before the quantifier over
inputs cannot absorb.

**This is a statement at the configuration exhibited and on the left side. It is not a statement
that the two formulations differ at every configuration, and it is not a statement about the right
side.**

## 11. `RNT5` (R) — is the per-input existential strictly weaker, on the RIGHT side

**Outcome reached on the right side: `SEP-STRICT`. This verdict is proved independently and is not
inherited from the left one.**

> **THE FROZEN SENTENCE, carried at this mention — `SEP-STRICT` on the RIGHT side, asked independently and inheriting nothing.**
> On the side named, a lift is exhibited that satisfies that side's per-input existential conjunct
> and admits no map making that side's fixed-map conjunct hold, at evidence level 2, with the
> objects and the configuration pinned by equations. **Together with this round's implication from
> the fixed-map form to the existential form, the implication is therefore strict on that side.**
> This is a statement at the configuration exhibited and on the side named; it is not a statement
> that the two formulations differ at every configuration, and it is **not a statement about the
> other side**.

The side is the **right** side, over act 11's weak anchored gauges. `rnt5_right_separation` exhibits
a map on dilations pinned by the same two equations, at the same configuration, and proves both
halves with its own witness, its own cancellation step and its own non-existence argument: the
**right conjunct of `OrbitNatural`** holds for it, witnessed by `K' = K` at every non-zero dilation
and by `K' = 1` at the zero dilation, whose membership in act 11's weak class is proved here with
all anchored phases `1`; and **no** map `αR` exists carrying `WeakAnchorStabilizer a₀` into itself
with `Ψ (U * K) = Ψ U * αR K`, for the same reason read on the right, with the exhibited
`K = diagonal(1, -1)` and the entry `((1, a₀), (1, a₀))`.

**There is no global `RNT5` label and neither side inherits the other's.** The two sides are
reported above as two components with independent evidence bars.

**No `SEP-COLLAPSE` was attempted on either side**, so no configuration was committed for one, and
no sentence of this note reports a collapse, at any configuration, on either side. **`SEP-UNDECIDED`
was not reached on either side.** Nothing here says that the two formulations coincide, that the
notions agree, or that the wordings are interchangeable.

## 12. `RNT6` — the classification, reported and not applied

**Outcome reached: `CLASS-TWISTED-NOT-STRICT`.** The composition rule the freeze fixes requires
`LAW-EXACT` with `ALPHA-NONTRIVIAL` **and** `STRICT-NO`, and all three inputs landed at the full
evidence bar frozen for each.

> The lift this round built is **twisted-natural and not strictly natural**: an exact intertwining
> law holds with exhibited maps on both sides, at least one of those maps is not the identity at an
> exhibited gauge element, and an exhibited pair witnesses the failure of strict equivariance —
> each at evidence level 2 and each earned separately.

> This is a classification of one named lift against three named notions. **It does not say which
> notion a later round's naturality condition ought to impose**, does not rate the three notions
> against one another, and does not open, adopt or pre-commit any part of a later round's ladder.
> That choice is the owner's and it is made in act 21's preregistration.

> **THE CLAUSE, carried at this mention — the classification.**
> Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in
> for, constructs the carrier relabelling's representative-level lift, and determines which of the
> three that lift satisfies. **Classifying is not choosing.** No statement of this round says
> which notion a later round's naturality condition ought to impose, which notion is the
> physically right one, or which notion the programme needs: that choice is the owner's and it is
> made in act 21's preregistration, against act 20's merged result. **A classification is a fact
> about an object, not an argument for a condition.** No condition is adopted, no rung is written,
> no ladder is opened, no census is run, and no law, carrier or selection principle is named,
> endorsed or excluded here.

**The separation status is carried beside the classification and not folded into it**:
`SEP-STRICT` on the left side and `SEP-STRICT` on the right side, each at the configuration its own
witness pins.

## 13. The scope boundary as honoured

**No ladder was frozen and none was run.** No rung, no ladder, no conjunction of rungs, no
`LadderConds` and no analogue of it appears in this round's module or in this note.

**No survivor census was run and no survivors were counted.** No transition family was tested
against any condition set.

**No rigidity headline was reported, in any form.** `L-RIGID`, `L-FAMILY` and `L-WIDE` are act 19's,
they belong to act 19's frozen ladder, and no artifact of this round reports any of them in any
paraphrase, in any table cell, or as a parenthetical.

**Act 19's same-initial-orbit discriminating test was not run.** `SIOP` is not stated, not
attempted, not witnessed and not refuted here, and no statement of this round bears on it.

**No condition was chosen for a later round**, no notion was recommended, no notion was rated
against another for suitability, physical reasonableness, strength of result or any other criterion,
and **no part of act 21's ladder was adopted or pre-committed** — no rung of it is named, proposed,
rated or ordered.

**The normative question was not asked, not bounded and not attempted.** "Which of the three notions
should a naturality condition impose?" is out of scope by this freeze and the choice is the owner's.
The weaker versions are refused too: no sentence of this note says "the natural choice would be",
"this suggests that", "a later round would presumably" or "the interesting condition is".

**Nothing here is, resembles, approximates or points toward quantum evolution**, and nothing here
says the evolution is continuous, smooth, generated or one-parameter.

**`P0` is untouched.** `verification/ROADMAP.md` was read at its pinned blob and not written; the
`P0` row's label, its obligation cell and its status text are unchanged; and no outcome of this round
moves, bounds, narrows or widens either part of it. Nothing here says `P0` is closed.

**No seventh question was executed.** The list of six targets is closed at the freeze, and nothing
outside it was attempted.

## 14. The act 19 boundary as honoured

**Act 19's control plane and closure were read and not edited.** Both carry their pinned blobs at
`B` and both are unchanged on this branch. Act 19's freeze is not amended, not withdrawn, not
corrected and not superseded; it is valid and unwithdrawn, and this round says so.

**Act 19's execution branch `claude/act-19-execution` was not merged, not cherry-picked from and not
cited as settled.** Its proofs are research material. Nothing in this round imports them, adapts
them under a new name, or counts them as discharging any obligation of this round. Everything act 20
needed, act 20 proved under act 20's own freeze, in the kernel, which is what act 19's closure
requires of every successor at its lines 108–110.

**Nothing uncertified by act 19 is reported as refuted.** The register act 19's closure fixes at its
lines 8–10 is kept throughout: the distinction is between a statement being **refuted** and a
statement being **uncertified by that round**, and act 19's conclusions are the second. Nothing here
says act 19 was wrong or that act 19's mathematics is false.

**Act 19's `L4n` is not adjudicated here.** No sentence of this round says that the relabelling
survives `L4n`, or that it fails `L4n`, or delivers any verdict about any rung of act 19's ladder.

## 15. The configurations, and the `|A|` value at which each verdict was reached

| target | configuration | `|A|` |
| --- | --- | --- |
| `RNT1` (a), (b) | arbitrary `V`, `A`, anchor; arbitrary map on dilations | every `|A|` |
| `RNT2` (a), (b) | arbitrary `V`, `A`, anchor; `σ` arbitrary, `Γ` invariant under `σ` for (b) | every `|A|` |
| `RNT3`, all four conjuncts | arbitrary `V`, `A`, anchor; `σ` arbitrary | every `|A|` |
| `RNT4` (a), left and right | `V = Fin 2`, `σ = Equiv.swap 0 1`, `A` arbitrary, anchor arbitrary | every `|A| ≥ 1` |
| `RNT4` (b), both clauses | `V = Fin 2`, `σ = Equiv.swap 0 1`, `A` arbitrary, anchor arbitrary | every `|A| ≥ 1` |
| `RNT5` (L) and (R) | `V = Fin 2`, `A` arbitrary, anchor arbitrary | every `|A| ≥ 1` |

**No verdict of this round was reached at `|A| = 1` only**, and none is reported as a verdict at
every `|A|` on the strength of a computation at one. The configuration note the freeze carries from
acts 18 and 19 is honoured directly rather than by caveat: the left class `LeftFibreGroup` is a
proper part at `|A| = 1` of what it is at `|A| ≥ 2`, so the two `RNT4` and the two `RNT5` witnesses
were stated with `A` **arbitrary** so that each holds at every `|A|`.

**Every verdict of this round is bounded to the lift this round built, the notions this freeze
states, and the configuration named.** None is a universal statement over lifts of the relabelling's
transition, and none is enlarged beyond what its own theorem pins.

## 16. What no outcome licenses

The forbidden sentences of this freeze, and the record that none is written here.

1. **No sentence chooses a notion for a later round.** The choice is the owner's.

> **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
> Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in
> for, constructs the carrier relabelling's representative-level lift, and determines which of the
> three that lift satisfies. **Classifying is not choosing.** No statement of this round says
> which notion a later round's naturality condition ought to impose, which notion is the
> physically right one, or which notion the programme needs: that choice is the owner's and it is
> made in act 21's preregistration, against act 20's merged result. **A classification is a fact
> about an object, not an argument for a condition.** No condition is adopted, no rung is written,
> no ladder is opened, no census is run, and no law, carrier or selection principle is named,
> endorsed or excluded here.

2. **"`α_σ` is not the identity, so the lift is not strictly natural" is not written**, and is not
   the argument of §9: `RNT4` (b) was earned only by its own exhibited pairs.
3. **No universal statement over lifts is written.** "No lift of the relabelling is strictly
   natural" is not this round's target and no outcome of this round earns it. This round classifies
   one named declaration, and a verdict about it is not a verdict about a class.
4. **No verdict about any rung of act 19's ladder is written**, in either direction.
5. **No rigidity headline is written**, in any form.
6. **No same-initial-orbit statement is written.**
7. **No count of anything that survives anything is written.**
8. **No failed search is reported as an agreement between the two formulations.** No search was run
   for `RNT5`; both sides were settled by exhibited witnesses.
9. **No `SEP-COLLAPSE` is reported without a configuration and a side**, because none is reported at
   all.
10. **No `RNT5` sentence carries no side**, and no result on one side is reported as a result about
    `RNT5`.
11. **Act 19 is not said to be wrong**, its freeze is not said to be amended, withdrawn, corrected
    or superseded, and its execution branch is not cited as settled.
12. **Nothing here is said to be, resemble, approximate or point toward quantum evolution.**
13. **Nothing is said about `P0`**, about the threading, the cross-time representative, the relative
    evolution or the relative candidate, about act 16's cancellation cell, act 18's `D`-axis or act
    14's four carriers.
14. **Act 12's transformation laws are not strengthened and act 12's classification is not
    enlarged**: both are consumed at merged strength, and **a merged statement is not enlarged by
    being consumed.**
15. **The condition list is not called exhaustive.** Three notions are frozen for classification,
    they are the three act 19's closure names, and a fourth is neither imposed nor refuted by
    anything here.
16. **Nothing is said about Track I, about Source B or about Source C**, on any axis, and nothing is
    imported from the substratum Lemma 24.1 rounds: **a shared word is not a bridge.**

**The status rule was honoured byte for byte.** Each target above is reported with exactly the
sentence this freeze freezes for the outcome reached, and `RNT6`'s sentence is followed by the
frozen closing sentence about the choice being the owner's.

## 17. The relation to the merged record

| act | what is consumed | at what strength |
| --- | --- | --- |
| act 7 | `readback`, `readback_relabel`, `AdmissibleDilationAt`, the readback amendment's convention, `D4b` negative, `D5` NOT CERTIFIED | merged; none re-proved |
| act 10 | the anchor-axis reclassification | untouched in either direction |
| act 11 | `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `GaugeRelated`, `CoherentLift`, `strong_mem_weak`, `weak_anchor_coeff_norm_one` | merged; none re-proved |
| act 12 | `LeftFibreGroup`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `TwoSidedRelated`, `fibreGram_apply`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`, `one_leftFibreGroup`, `weak_mul`, `sh1_necessity` | merged; none re-proved |
| act 13 | the cross-time invariants and the level-2 datum | not consumed and not moved; `CT3` (d) is not answered |
| act 17 | `TJ1`, `TJ3` and the trajectory results | not consumed; not revised |
| act 18 | `XS0`–`XS5` and the two axes | not consumed; not revised |
| act 19 | the frozen `ΦP` statement, as a **statement** and not as a result; the closure, as the account of the problem | the freeze is valid and unwithdrawn; nothing of act 19's is certified by act 20 and nothing of act 19's is edited |

**No merged label is revised.** `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
`SH1`, `SH1-C1`, `SH1-C2`, `AB0`–`AB2`, `CT1`–`CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4`,
`TJ0`–`TJ3` and `XS0`–`XS5` are untouched. `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`LeftFibreGroup`, `WeakAnchorStabilizer`, `StrongAnchorStabilizer` and `CoherentLift` are **reused,
not redefined**. `D3`, `D4b`, `D5`, the direct-branch statement and the readback convention are
unchanged.

**The direct-branch statement, carried unchanged:** `D4a` positive on the direct branch; `T1`
**necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

**Two hazards of the freeze are recorded as directly addressed.** The anchor and the rank bound were
not silently dropped: `FibreGram a₀` carries its anchor through `rnt2_lifting_property` and
`rnt3_right_closure`, and `RealizableGram`'s rank bound is not touched because this round makes no
sufficiency claim. And no step of this round supplies a missing theorem from background knowledge:
every step is either a merged result cited at its coordinate or a theorem this round proves.

## 18. The definition budget

**Seven slots were budgeted. Seven fired, and both conditional slots fired. No eighth definition was
introduced and no amendment was needed.**

| slot | declaration | status |
| --- | --- | --- |
| 1 | `StrictNatural` | **fired**, at the definition commit |
| 2 | `TwistedNatural` | **fired**, at the definition commit |
| 3 | `OrbitNatural` | **fired**, at the definition commit |
| 4 | `RelabelTransition` | **fired**, at the definition commit |
| 5 | `RelabelLift` | **fired**, at the definition commit |
| 6 (conditional) | `RelabelInducedLeft` | **fired**, at the discrimination commit |
| 7 (conditional) | `RelabelInducedRight` | **fired**, at the discrimination commit |

**Slots 6 and 7 are outputs and not inputs, and they were treated as such**: they are absent at the
definition commit and their first appearance on the branch **is** the discrimination commit.

**No gauge element, witness, matrix, visible family, Gram tuple, entry value, permutation or
configuration is a top-level definition.** Each is a bound variable pinned by an equation in the
statement that needs it, as acts 10 through 19 did. In particular `RNT5`'s separating map on
dilations is a bound variable pinned by the two equations `Ψ 0 = 1` and `Ψ U = U` for `U ≠ 0`, and is
**not** a declaration.

## 19. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants**, with `B = _RNT_BASE = 84f27b50198ee31c224e31284905ff6c284ea9db`. The question is
asked of the real `pull_request.head.sha` from the Actions event payload and **never** of the
synthetic merge commit; an unresolvable head **fails closed** with no fallback; the check excludes
pre-freeze side history by requiring every commit in `git rev-list H ^B` to be itself a descendant of
`B`; and the guard recovers whatever history it needs and fails if recovery fails.

**This is a SEALING round** under `AGENTS.md` `§A.37`. It lands **`E` → `L` → `P`, with `P`
mandatory**. **`_RNT_SEALED_HEAD` and `_RNT_MERGE` are unset at execution.** That is a statement
about this execution and stays true as one.

**Before certification this execution absorbed no later `main`.** No merge from `main`, no rebase,
no amend and no force-push was performed at any point.

**The seal-integrity clause EXCLUDES this round's own triple.** `_rnt_prior_seals` names acts 13's,
14's, 15's, 16's, 17's and 18's triples and says nothing whatever about `_RNT_BASE`,
`_RNT_SEALED_HEAD` or `_RNT_MERGE`: there are **zero executable references** to this round's own
constants in that function, with the exclusion explained in its docstring. **A clause fixing this
round's own pins at unset for all time would contradict the mandatory lifecycle**, under which `P`
must set them — the guard would then pass at no commit once the round landed.

**Clause 9 was verified EMPIRICALLY before the commit**, in the freeze's three configurations,
reported as measurements and not as intentions:

| configuration | expected | measured |
| --- | --- | --- |
| unmutated | `True` | **`True`** |
| each of the eighteen prior-seal constants fabricated one at a time | `False` each time | **`False`, eighteen of eighteen** |
| **this round's own pins set to plausible values, prior seals unmutated** | `True` | **`True`** |

**The third configuration is the decisive one**: it is the post-pin configuration the mandatory pin
commit `P` will create, and it is the one an earlier round in this programme failed.

**Acts 13's, 14's, 15's, 16's, 17's and 18's seals are untouched**, and **no existing seal constant
is altered**. An archive seal belongs to the round that set it; this round reads them and never
writes them. **Act 19 set no seal triple**, so none is read and none is invented.

### The ten preconditions checked at `B`

| # | precondition | result |
| --- | --- | --- |
| 1 | this control plane is merged and `B` is its merge commit | **PASS** — `git rev-list --parents -n 1 B` shows two parents, `0840e37b` and `0a2d0c80`; the blob is `131783f48ac492fdfdc46072aee3f39278973622` |
| 2 | act 19's closure and control plane are present, unedited | **PASS** — `3d37529cb89a4d2bb60281f14f15645e3beaeb4c` and `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057` |
| 3 | act 19 landed no formal state | **PASS** — no `R7-OLR`, no `_OLR`, no `OrbitLawRigidity.lean` |
| 4 | act 18's execution is merged and sealed | **PASS** — `_XTS_SEALED_HEAD` and `_XTS_MERGE` both non-`None` and equal to the pinned values |
| 5 | act 17's execution is merged and sealed | **PASS** — `_TRJ_SEALED_HEAD` and `_TRJ_MERGE` both non-`None` and equal to the pinned values |
| 6 | acts 16's and 15's executions are merged and sealed | **PASS** — all four constants non-`None` and equal to the pinned values |
| 7 | acts 14's and 13's executions are merged and sealed | **PASS** — all four constants non-`None` and equal to the pinned values |
| 8 | the modules this round consumes are in the tree | **PASS** — all five present |
| 9 | no act 20 execution object precedes the freeze | **PASS** — the round directory holds `preregistration.md` alone and no `RepresentativeNaturality.lean` exists |
| 10 | the guard tag and its stem are still free | **PASS** — no `R7-RNT` and no `_RNT` in the guard file, and all seven reserved declaration names free by exact string over the whole tree |

**No sibling lane's merge is a precondition of this round**, and none was waited for.

**The claim is scoped to the repository record.**

## 20. The axiom table — one line per named result

**Evidence level 2 throughout**: kernel-checked, no unproved declaration, no added axiom, no
kernel-bypassing decision procedure, no `sorry` and no `native_decide`. `Classical.choice` appears
where a merged result is applied and its appearance is not a defect.

| declaration | axioms |
| --- | --- |
| `rnt1_strict_imp_twisted` | `[propext, Classical.choice, Quot.sound]` |
| `rnt1_twisted_imp_orbit` | `[propext, Classical.choice, Quot.sound]` |
| `rnt2_lifting_property` | `[propext, Classical.choice, Quot.sound]` |
| `rnt2_admissible` | `[propext, Classical.choice, Quot.sound]` |
| `relabelLift_apply` | `[propext, Classical.choice, Quot.sound]` |
| `relabelLift_eq_submatrix` | `[propext, Classical.choice, Quot.sound]` |
| `relabelLift_mul` | `[propext, Classical.choice, Quot.sound]` |
| `relabelLift_one` | `[propext, Classical.choice, Quot.sound]` |
| `relabelLift_unitary` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_left_closure` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_left_law` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_right_closure` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_right_law` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_law_exact` | `[propext, Classical.choice, Quot.sound]` |
| `rnt3_orbit` | `[propext, Classical.choice, Quot.sound]` |
| `diag_unit_mem` | `[propext, Classical.choice, Quot.sound]` |
| `rnt4a_left_nontrivial` | `[propext, Classical.choice, Quot.sound]` |
| `rnt4a_right_nontrivial` | `[propext, Classical.choice, Quot.sound]` |
| `rnt4b_strict_fails_left` | `[propext, Classical.choice, Quot.sound]` |
| `rnt4b_strict_fails_right` | `[propext, Classical.choice, Quot.sound]` |
| `rnt4b_not_strictNatural` | `[propext, Classical.choice, Quot.sound]` |
| `eq_zero_of_left_mul_eq_zero` | `[propext, Classical.choice, Quot.sound]` |
| `eq_zero_of_mul_right_eq_zero` | `[propext, Classical.choice, Quot.sound]` |
| `rnt5_left_separation` | `[propext, Classical.choice, Quot.sound]` |
| `rnt5_right_separation` | `[propext, Classical.choice, Quot.sound]` |

Twenty-five named results, seven top-level definitions, one module.

## 21. The predictions, reported against their outcomes

| target | prediction | outcome | reported as |
| --- | --- | --- | --- |
| `RNT1` (a) | **positive**, high | `CHAIN-PROVED` | **as predicted** |
| `RNT1` (b) | **positive**, high | `CHAIN-PROVED` | **as predicted** |
| `RNT2` (a) | **positive**, medium | `LIFT-BUILT` | **as predicted** |
| `RNT2` (b) | **positive**, medium | `LIFT-BUILT` | **as predicted** |
| `RNT3` | **abstained** | `LAW-EXACT` | abstention honoured; the freeze put nothing at risk here and nothing is scored |
| `RNT4` (a) | **abstained** | `ALPHA-NONTRIVIAL`, both sides | abstention honoured |
| `RNT4` (b) | **abstained** | `STRICT-NO` | abstention honoured |
| `RNT5` (L) | **not predicted**, `SEP-UNDECIDED` named as the freeze's expectation, low | `SEP-STRICT` | **against the freeze's stated expectation, and recorded as such** |
| `RNT5` (R) | **not predicted**, `SEP-UNDECIDED` named as the freeze's expectation, low | `SEP-STRICT` | **against the freeze's stated expectation, and recorded as such** |
| `RNT6` | **abstained** | `CLASS-TWISTED-NOT-STRICT` | abstention honoured |

**No prediction of this freeze is falsified.** The freeze predicted nothing on `RNT3`, `RNT4` or
`RNT6`, deliberately and with its reason recorded, and the two targets it did predict came out as
predicted.

**`RNT5` is the one place the round went past what the freeze expected, and it is recorded as that
and not as a confirmation.** The freeze named `SEP-UNDECIDED` as its expectation on each side, at
low strength, because it named no construction for a separating map and the merged record supplies
none. Both sides reached `SEP-STRICT` instead, each by an exhibited witness at full bar. **A
separation reached where an UNDECIDED was expected is a stronger outcome than the freeze forecast,
and the freeze's own text preregisters `SEP-STRICT` as reachable at full bar on each side
independently**, so this is an outcome inside the frozen scope and not outside it.

**The freeze predicted nothing about whether the two sides would agree**, and this round's two
`RNT5` results are not evidence about each other: each side carries its own witness and its own
non-existence argument, and neither was inferred from the other.

## 22. The discrepancies

**Two items are recorded. Neither is repaired, and the freeze is not edited.** The preregistration
is immutable once merged; an execution that diverges records the discrepancy and does not repair the
freeze.

**`DF1` — a garbled clause in the mandated base's own merge-commit message, archival only.** The
merge commit `84f27b50198ee31c224e31284905ff6c284ea9db` describes this round's module as "module
OrbitRepresentativeNaturality's file RepresentativeNaturality.lean". **The module act 20 owns is
`OIBridge/RepresentativeNaturality.lean`**, and the frozen preregistration's naming at its lines 102
through 107 is authoritative and correct. **This is a harmless archival wording defect in a commit
message.** It needs **no repair to `main` and none to the freeze**: a commit message is not a pinned
blob, nothing in the guard or in the start-state table reads it, and rewriting it would rewrite
certified history for a typographical reason. It is recorded here so that a reader comparing the
commit message with the module path is not left to wonder which is right.

**`DF2` — `RNT5` landed beyond the freeze's stated expectation on both sides.** The freeze named
`SEP-UNDECIDED` as the outcome it expected on each side and predicted neither. Both sides reached
`SEP-STRICT`. This is recorded as a divergence from the freeze's forecast and is not repaired, not
corrected, not reinterpreted and not normalized. **`SEP-STRICT` is preregistered as reachable at the
full evidence bar on each side independently**, so the outcome is inside the frozen scope; what
diverged is the expectation and not the scope.

**No start-state discrepancy arose**, in any pinned blob or in any of the ten preconditions:
**every one matches** and **all ten pass**.

**No candidate discovered during execution was executed.** **No configuration was chosen after an
outcome was known.** **No alternative witness was substituted for a named one.** The list of six
targets is closed at the freeze and nothing outside it was attempted; no fourth notion was stated,
no second lift was built, and no seventh question was executed.

> **THE CLAUSE, carried at this mention — the discrepancies, where a classification could be read as a choice.**
> Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in
> for, constructs the carrier relabelling's representative-level lift, and determines which of the
> three that lift satisfies. **Classifying is not choosing.** No statement of this round says
> which notion a later round's naturality condition ought to impose, which notion is the
> physically right one, or which notion the programme needs: that choice is the owner's and it is
> made in act 21's preregistration, against act 20's merged result. **A classification is a fact
> about an object, not an argument for a condition.** No condition is adopted, no rung is written,
> no ladder is opened, no census is run, and no law, carrier or selection principle is named,
> endorsed or excluded here.

**The non-choice clause is carried verbatim at three mentions in this note** — at the classification
in §12, at the list of what no outcome licenses in §16, and here — **and at one mention in the module
docstring**, each opening with its own naming line, for **four carriages** in this round's artifacts.
