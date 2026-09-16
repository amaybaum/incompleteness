# Act 17 — what selects or constrains the cross-time Gram/orbit trajectory: RESULT

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md`, blob
`3b5570102aa6aacb09788059989a70d8cdd5b70f`, from `02cfc9be141a44aaebf847d8e7d9fdd0d0a18f08` — the
merge commit of that control plane, which the freeze fixes as this round's **mandated execution
base**.

**The round's first act was to verify the freeze's blob at that base.**
`git rev-parse HEAD:verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md`
returned `3b5570102aa6aacb09788059989a70d8cdd5b70f`, which is the blob the freeze names. **The freeze
is immutable and was not edited.** Where this execution found something at variance with it, the
discrepancy is **recorded and not repaired**, in the section that ends this note.

## 1. The round's shape, restated

**This is a SEALING round** under `AGENTS.md` `§A.37`. It creates new seal state — a new Lean module
carrying this round's own named results — and therefore takes a pin commit. It lands
**`E` → `L` → `P`, with `P` mandatory**.

The seal constants this round owns and fills are `_TRJ_BASE`, `_TRJ_SEALED_HEAD` and `_TRJ_MERGE`,
under the reserved guard tag `R7-TRJ`. **`_TRJ_SEALED_HEAD` and `_TRJ_MERGE` are unset at
execution.** That is a statement about this execution and stays true as one: the pin commit `P` sets
them, after the landing merge `L`, and pinning them inside the execution would make the execution's
own head depend on where it landed.

**No existing seal constant is altered.** `_RNC_*`, `_TCF_*`, `_PQT_*`, `_CTI_*`, `_A12P_*`,
`_SGT_*`, `_TSG_BASE` and `_CLG_BASE` are **read and never written**: an archive seal belongs to the
round that set it, and touching the guard file that carries those constants does not make this round
their owner. The execution's diff against `verification/lean/edge_rigidity_probe.py` **adds** the
`R7-TRJ` clause and changes nothing else in the file.

## 2. The four frozen items, as honoured

| frozen item | how it was honoured |
| --- | --- |
| item 1 — the candidate list | **unchanged and closed.** `SP1L`, `SP1G`, `SP2`, `SP3`, `SP5` and the probe `SP4` were tested and **no other candidate was executed.** The frozen selector class `𝒮` has exactly the four members `SP1L`, `SP2`, `SP3`, `SP5`; `SP1G` is a determination claim and `SP4` a regime probe, and **neither is in `𝒮`**. |
| item 2 — the data regime | **respected and checked.** Every member of `𝒮` consults only the licensed set `L` — the visible family `Γ`, the index `ℕ` with its successor and order, and the carrier cardinalities with the anchor as a label — and `SP3` consults the index and its successor only, not `Γ`. **Nothing in the forbidden set `F` is consulted by any member of `𝒮`**: not the lift, not the raw fibre-Gram representative, not act 13's cross-time data at any level, not act 14's four carriers, not acts 15's or 16's statements, and nothing from the substratum Lemma 24.1 rounds or from Track I. `SP4` is the one deliberate exception and **is outside the class**. |
| item 3 — the cross-time equivalence | **`GramTrajEquiv` was used and no other relation.** Every quotient in this round is taken over it, by name. Raw Gram equality, uniform-phase equality and act 13's level-2 and level-3 relations were **not adopted** and appear nowhere in any statement. |
| item 4 — the countercontrols | **each was reached**, at exactly the configurations the freeze names and at no others. The per-candidate record is in section 6. |

**The execution used the frozen configurations only.** Act 12's Hadamard objects at `Γ ≡ ¼`,
`|V| = 4`, `|A| = 1` carry every countercontrol, and the deterministic island act 12's `SH1-C2`
supplies is **cited and never used as a witness**. **No configuration was chosen after an outcome
was known.** One alternative kernel route through the same configuration is recorded as an
observation in section 13 and **was never substituted as the witness**.

## 3. `TJ0` — the bounded search, recorded in full

**Outcome reached: `TJ0`-silent.**
> On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
> `verification/lean/`, every `preregistration.md` and `result.md` under
> `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
> the merged record contains no statement constraining the Gram/orbit trajectory across time
> beyond the per-slice realizability of `SH1`, and decides no candidate of the frozen class in
> either direction. **The finding is that the record is silent on the point.** It is not a finding
> that any such statement is false, not a finding that one is unprovable, and not a bound on what a
> later round could prove.

**The file set, taken from `git ls-tree -r --name-only B` at the mandated base**, so that untracked
package trees are outside it by construction: **223 files** — 169 `*.lean` under
`verification/lean-mathlib/`, 6 `*.lean` under `verification/lean/`, 47 `preregistration.md` and
`result.md` files under `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`.

**The question asked of each hit**, as frozen: does this declaration decide, for some visible family
or for every visible family, whether the Gram/orbit trajectory is constrained **across time** beyond
the per-slice realizability of `SH1` — or does it decide, for any member of `𝒮` or for `SP1G`,
whether that candidate holds of every coherent lift or selects at any configuration?

| term | files | hits | recorded answer |
| --- | --- | --- | --- |
| `FibreGram` | 14 | 220 | **Does not supply it.** Thirty-eight merged declarations carry `FibreGram` in their statement; six are `ℕ`-indexed and every one of the six is per-slice, definitional or about a different datum — `twoSidedRelated_iff` (quoted below), `ct3g_fibreGram_strong_right` (strong-right invariance at each time), `fibreCrossGram_diag` (a definitional identity), `ct3b_hadamard_trajectory_control` (existential, about act 13's separating datum), `pq2b_strong_right_crossFibreGram` and `reanchoredChannel_eq_trace` (act 14's and act 16's carriers). None constrains the trajectory across time. |
| `GramPhaseEquiv` | 8 | 36 | **Does not supply it.** Act 12's relation is stated on one slice's tuple; no declaration couples two times through it. |
| `RealizableGram` | 7 | 21 | **Does not supply it.** `sh1_shape` is both directions **at a single slice**, and its hypotheses mention no second time. |
| `TwoSidedRelated` | 7 | 23 | **Does not supply it.** `twoSidedRelated_iff` is the per-slice relation applied pointwise, and says so; quoted below. |
| `CoherentLift` | 88 | 300 | **Does not supply it.** The definition carries no cross-time conjunct whatever; quoted below. |
| `trajector` | 32 | 337 | **Does not supply it.** Every occurrence is a naming, a non-doing, or act 13's `CT3` (b), which names act 12's pair "the trajectory-type control" and is **existential** about that pair. |
| `select` | 96 | 652 | **Does not supply it.** Every occurrence in the programme files is the recurring non-doing "names, endorses or excludes no selection principle", or is unrelated vocabulary in other programmes' modules. No declaration decides any candidate. |
| `stationar` | 15 | 139 | **Does not supply it.** No declaration of any kind states a stationarity condition on the Gram data; the occurrences are prose in non-doings lists and in other programmes. |
| `diagonal` | 108 | 1643 | **Does not supply it.** `fibreGram_diag`, `fibreGram_diag_of_admissible` and `fibreGram_of_deterministic` are **per-slice** statements about one dilation; the last gives the closed form on deterministic slices and quantifies over no family and no second time. |
| `TG2` | 17 | 87 | **Does not supply it.** `TG2` classifies **one slice**'s orbit. |
| `TG3` | 17 | 82 | **Does not supply it.** `TG3` is **existential**, about its own two exhibited dilations and their lifted pair. It exhibits a trajectory that moves; it constrains none. |
| `SH1` | 16 | 157 | **Does not supply it.** `SH1` is the **per-slice** realizability characterization, both directions, at one time. |
| `RO1` | 17 | 58 | **Not relevant to the question.** `RO1` is right-only insufficiency carried by left moves, a statement about the gauge class and not about the trajectory. |
| `CT2` | 14 | 90 | **Not relevant to the question.** `CT2` (a) and (b) are about the column cross-Gram and the fibre cross-Gram determining the **lift** up to threading, which this round's relation cannot see. |
| `CT3` | 16 | 221 | **Does not supply it.** `CT3` (G) is strong-right invariance at every level; `CT3` (b) is existential about act 12's pair; `CT3` (d) is act 13's fork and stays UNDECIDED and untouched. |
| `CT4` | 14 | 120 | **Not relevant to the question.** `CT4` is a constant-left obstruction on the relative candidate. |
| `GL2` | 20 | 197 | **Not relevant to the question.** `GL2` is about the relative evolution under a strong right gauge; its pair is **one** trajectory for this round. |

**The two decisive quotations, with their coordinates.**

`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, **lines 836–838**:
> **THE LIFTED FORM, SLICE-WISE** — two `ℕ`-indexed lifts are two-sided related exactly when their
> fibre-Gram data are `∼_D`-equivalent at every time. A corollary of `twoSided_slice_iff`, and **per
> slice only**: nothing couples the Gram data across time (hazard 3).

`verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, **lines 124–125**:
> def CoherentLift (a₀ : A) (Γ : ℕ → Matrix V V ℝ) (U : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
>   ∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)

**`TJ0` is a type-P target and carries no evidence level.** It was settled by locating and quoting
and by a recorded bounded-search negative, and by nothing else. **No Lean was written for `TJ0`** and
no outcome of `TJ0` is a theorem of this round. **Reconstructive inference is refused as a finding
here**: nothing below rests on an argument of the form "the record must contain X, because otherwise
Y would not have been written". **Searching and not finding is never a settling outcome**, and no
line of this round's hierarchy is earned by the absence of a witness. **Nor are this round's own
theorems treated as retro-evidence about `TJ0`.**

**The prediction was `TJ0` negative at high, and it landed.**

## 4. `TJ1` — the pointwise characterization, and the baseline finding

**Outcome reached: `TJ1`-both-directions.** **Necessity and sufficiency both landed, at evidence
level 2.**
> The Gram trajectories of the coherent lifts of a visible family are exactly the pointwise
> realizable assignments, at evidence level 2, through act 12's merged `SH1` consumed in both
> directions slice by slice. **The admissible trajectory set is the product over time of the
> per-slice realizable sets, and the merged record therefore imposes no coupling between slices.**
> This is a statement about what is constrained and **not** a selection principle: it asserts no
> coupling and denies none, and it establishes that **every** cross-time constraint on the
> trajectory is additional structure rather than a consequence of coherence. The per-slice
> constraint it records is act 12's `SH1`, consumed at its own strength and neither enlarged nor
> revised, and the narrowing the rank bound `|A|` effects is **pointwise** and is labelled
> pointwise. **And it settles, positively, that there is no additional universal cross-time
> constraint on coherent Gram trajectories beyond pointwise realizability**: any such constraint
> would have to hold of every coherent lift's trajectory while some pointwise realizable trajectory
> failed it, and sufficiency realizes every pointwise realizable trajectory by a coherent lift, so
> the two demands are jointly unsatisfiable. **Line 3 of this round's hierarchy is thereby ruled out
> by this target rather than left undecided**, and the exclusion is reported as a finding of the
> round and not as an absence of one. It is a statement about `CoherentLift` as the programme
> defines it, `ℕ`-indexed and pointwise in time; it is **not** a statement that no cross-time
> structure could be added to the programme, **not** a statement that the trajectory question is
> closed, and **not** a bound on what a later round could constrain under a different notion of
> coherence or a larger licensed data set.

**What carries each direction.**

* **Necessity** — `tj1_necessity`. Act 12's merged `sh1_necessity` applied at each `t`, with no
  assembly required. `CoherentLift` is definitionally `∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)`, so
  there is nothing cross-time to discharge.
* **Sufficiency** — `tj1_sufficiency`. Act 12's merged `sh1_sufficiency` is stated per slice with no
  hypothesis on `Γ` beyond realizability, so the assembly is a choice over `t`. `Classical.choice`
  appears here and **its appearance is not a defect**, as the freeze records in advance.
* **Both as one** — `tj1_trajectory_set`, the biconditional.

**The narrowing this target records is POINTWISE, and is labelled pointwise in terms.** The rank
bound `|A|` inside `RealizableGram` excludes trajectory values **slice by slice**. That exclusion is
**not** a coupling between times, and reporting it as one is exactly the defect line 3's clause (iii)
exists to prevent. **The rank bound is act 12's and is not re-proved, enlarged or revised here**; what
is this round's own is the statement over **all** times at once and the assembly of the lift.

**`TJ1` is a statement about Gram trajectories and not about lifts.** Two lifts with one Gram
trajectory may differ arbitrarily in the threading, and that is untouched here.

### The `TJ1` baseline finding, stated in its own right — CO-PRIMARY AND OUTSIDE THE LADDER

**This is a positive result and it is reported as one, not as the absence of something.**

`tj1_no_universal_cross_time_constraint` is the kernel statement: for **every** property `Q` of Gram
trajectories that holds of `𝔾(U)` for every coherent lift `U`, `Q` holds of **every** pointwise
realizable assignment. So a property cannot both be universal over coherent lifts and exclude a
pointwise realizable trajectory. **The present `CoherentLift` notion contributes no further universal
cross-time constraint on the Gram/orbit trajectory at all: any such law must enter the programme as
additional structure.**

**This finding is on its own axis and is not a line of the `TJ3` hierarchy.** The two answer
different questions, and the freeze fixes the reason: "OI itself imposes no cross-time coupling" is
not naturally above or below "these four proposed selectors all fail at one admissible
configuration". **The two are reported separately throughout this note and are never merged into one
ordering.**

**Line 3 of the hierarchy is thereby RULED OUT, and the exclusion is this round's own theorem.**
Line 3's clause (i) requires a universal property `Q`, and its clause (ii) requires a pointwise
realizable trajectory that **fails** `Q`. Sufficiency realizes that purported counterexample by a
coherent lift, and clause (i) then forces it to satisfy `Q`. **Clauses (i) and (ii) are jointly
unsatisfiable given `TJ1` sufficiency**, so no property whatever can earn line 3. **Line 3 is
therefore not reported UNDECIDED**, and it is not reported at all: the exclusion is reported here,
under `TJ1`, as this target's own finding.

**What the ruling-out is not.** It is **not** a statement that no cross-time structure could be added
to the programme, **not** a statement that the trajectory question is closed, and **not** a bound on
what a later round could constrain under a different notion of coherence or a larger licensed data
set. It is a statement about `CoherentLift` as the programme defines it, indexed by the naturals and
pointwise in time.

**Both `TJ1` predictions were positive at high, and both landed.**

## 5. The scope boundary against threading, as honoured

`gramTrajEquiv_of_threading` is the demonstration, in the kernel and not in prose. If
`U'_t = W · U_t · K_t` with `W ∈ 𝒢_L` **constant** and `StrongAnchorStabilizer a₀ (K t)` at every
`t` — which is act 13's residual threading freedom exactly — then the two lifts have the **same**
fibre-Gram tuple at every time, by act 12's `fibreGram_left_mul` on the left factor and act 13's
`ct3g_fibreGram_strong_right` on the right, hence **one** trajectory under `GramTrajEquiv` with the
trivial phase family.

**Every pair act 13's `CT2` (b) leaves undetermined is identified by this round's relation**, and
**act 11's `GL2` pair is ONE trajectory here**: it shares every fibre-Gram matrix at every time and
differs in relative evolution, and this round says **nothing whatever** about the difference.

**No statement of this round distinguishes two lifts the relation identifies.** That is checked by
reading every statement in the module: each is either universally quantified over lifts and
trajectories, or pins its objects by equations at the one frozen configuration, and none mentions the
relative object, the relative candidate, the anchored channel, the re-anchored channel, or any
cross-Gram datum except inside `tj2f_sp4_containment`, which is the out-of-regime probe and is
outside the class. **The cost of the boundary is accepted deliberately**: no outcome of this round
can bear on the relative evolution, on the threading, or on any carrier of act 14.

## 6. `TJ2` — the six parts, each with its frozen label and sentence

**Every part landed, and every part landed at the sign and label the freeze predicted.** No `TJ2`
verdict is against prediction, and none is UNDECIDED.

### `TJ2` (a) — `SP1L`, the per-lift law-determination constraint

**Question (A): `SP1L-ADD`.** Carried by `tj2a_sp1l_add`.
> The candidate named `SP1L` in this round's frozen list **fails for an exhibited coherent lift of an
> exhibited visible family**, at evidence level 2, with the violating times named and the
> inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `SP1L` is
> additional structure and not a consequence of coherence.** This is a verdict on the exact
> proposition frozen under the label `SP1L`, on the data grant frozen for it, and on nothing in its
> neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
> refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
> strengths and none is enlarged.

The violating times are **`t = 0` and `s = 1`**, the visible family is `Γ ≡ ¼` and is **constant in
time** so that `Γ 0 = Γ 1` holds as a conjunct of the statement, and the inequivalence is act 12's
merged `hadamard_slices_not_twoSided`, certified through the named `∼_D`-invariant
`G^{(0)}_{10} · G^{(1)}_{01}`, which act 12 computes as `1/16` for `H(1)` and `i/16` for `H(i)`.

**Question (B): `SP1L-NOSEL`.** Carried by `tj2a_sp1l_nosel`.
> At the exhibited configuration, two coherent lifts of one visible family both satisfy `SP1L` and
> their trajectories are **inequivalent under `GramTrajEquiv`**, this round's frozen cross-time
> equivalence, at a named time and through a named invariant, at evidence level 2. **So `SP1L` does
> not select there.** This settles **one configuration**: it is not a statement that `SP1L` fails to
> select at every configuration, and act 12's `SH1-C2` supplies configurations — the deterministic
> visible laws — where the per-slice orbit is unique for free. It is **not** a statement that no
> principle selects, which is line 4's question and is settled there.

**The configuration is named**: `|V| = 4`, `|A| = 1`, anchor `0`, visible family `Γ ≡ ¼` constant in
time. The two lifts are the **constant** lifts `U ≡ H(1)` and `U' ≡ H(i)`, each satisfying `SP1L`
because a constant lift has a constant trajectory, and the separating time is **`t = 0`**.

### `TJ2` (b) — `SP1G`, the cross-lift law-determination claim

**Question (A): `SP1G-ADD`.** Carried by `tj2b_sp1g_add`. **`SP1G` is not a member of `𝒮`** — it is a
determination claim across lifts, not a predicate on a single lift — so question (B) is not asked of
it and **no line of this round's hierarchy quantifies over it**.
> The candidate named `SP1G` in this round's frozen list **fails for an exhibited coherent lift of an
> exhibited visible family**, at evidence level 2, with the violating times named and the
> inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `SP1G` is
> additional structure and not a consequence of coherence.** This is a verdict on the exact
> proposition frozen under the label `SP1G`, on the data grant frozen for it, and on nothing in its
> neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
> refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
> strengths and none is enlarged.

The two constant lifts `U ≡ H(1)` and `U' ≡ H(i)` are read **across lifts** at `t = s = 0`: their
visible laws agree by hypothesis, both being coherent lifts of one `Γ`, and their per-slice orbit
classes do not.

### `TJ2` (c) — `SP2`, orbit stationarity under a constant visible law

**Question (A): `SP2-ADD`.** Carried by `tj2c_sp2_add`, on the same exhibited lifted pair, whose
visible family is constant and whose orbit is not.
> The candidate named `SP2` in this round's frozen list **fails for an exhibited coherent lift of an
> exhibited visible family**, at evidence level 2, with the violating times named and the
> inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `SP2` is
> additional structure and not a consequence of coherence.** This is a verdict on the exact
> proposition frozen under the label `SP2`, on the data grant frozen for it, and on nothing in its
> neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
> refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
> strengths and none is enlarged.

**Question (B): `SP2-NOSEL`.** Carried by `tj2c_sp2_nosel`, at the same named configuration, the two
constant lifts being stationary by construction and inequivalent at the named time `t = 0`.
> At the exhibited configuration, two coherent lifts of one visible family both satisfy `SP2` and
> their trajectories are **inequivalent under `GramTrajEquiv`**, this round's frozen cross-time
> equivalence, at a named time and through a named invariant, at evidence level 2. **So `SP2` does
> not select there.** This settles **one configuration**: it is not a statement that `SP2` fails to
> select at every configuration, and act 12's `SH1-C2` supplies configurations — the deterministic
> visible laws — where the per-slice orbit is unique for free. It is **not** a statement that no
> principle selects, which is line 4's question and is settled there.

**The propagation, reported as propagation and not as a discovery restated four times.** The frozen
chain is `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2`, with no implication reversing. `SP2` is the **weakest** member,
so its refutation is the one the other three inherit, and the four (A) verdicts above and below are
**one merged witness family and the consequences this round draws from it** — act 12's Hadamard
objects at `Γ ≡ ¼`, `|V| = 4`, `|A| = 1` — and never four independent findings.

### `TJ2` (d) — `SP3`, a homogeneous transition rule on the orbit trajectory

**Question (A): `SP3-ADD`.** Carried by `tj2d_sp3_add`. The exhibited coherent lift of the constant
family has slices `H(1)`, `H(i)`, `H(1)`, `H(1)` at `t = 0, 1, 2` and `t ≥ 3`: **the orbits at
`t = 0` and `t = 2` agree while those at `t = 1` and `t = 3` do not**, so the frozen implication
fails at `t = 0`, `s = 2`. Each slice's admissibility is merged, and the inequivalence is merged.
**The freeze rated this row at medium, for the bookkeeping of a piecewise lift over `ℕ` and the case
split, and it landed.**
> The candidate named `SP3` in this round's frozen list **fails for an exhibited coherent lift of an
> exhibited visible family**, at evidence level 2, with the violating times named and the
> inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `SP3` is
> additional structure and not a consequence of coherence.** This is a verdict on the exact
> proposition frozen under the label `SP3`, on the data grant frozen for it, and on nothing in its
> neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
> refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
> strengths and none is enlarged.

**The refutation is of the exact frozen proposition and of nothing in its neighbourhood.** It is
**not** a refutation of memorylessness, of homogeneity, or of any other transition-rule condition.
The freeze states the **law-free** form as `SP3`, on the narrower data grant of the index and its
successor only; the **law-reading variant is a different and weaker proposition**, named by the
freeze as parked and **not executed** in this round, and it belongs to a later round with its own
freeze. Nothing here bears on it in either direction.

**Question (B): `SP3-NOSEL`.** Carried by `tj2d_sp3_nosel`, at the same named configuration: each
constant lift satisfies the implication because its conclusion is reflexivity, and the two are
inequivalent at the named time `t = 0`.
> At the exhibited configuration, two coherent lifts of one visible family both satisfy `SP3` and
> their trajectories are **inequivalent under `GramTrajEquiv`**, this round's frozen cross-time
> equivalence, at a named time and through a named invariant, at evidence level 2. **So `SP3` does
> not select there.** This settles **one configuration**: it is not a statement that `SP3` fails to
> select at every configuration, and act 12's `SH1-C2` supplies configurations — the deterministic
> visible laws — where the per-slice orbit is unique for free. It is **not** a statement that no
> principle selects, which is line 4's question and is settled there.

### `TJ2` (e) — `SP5`, the decoherence rule: the orbit is the diagonal tuple

**Question (A): `SP5-ADD`.** Carried by `tj2e_sp5_add`, at `H(1)` itself.
> The candidate named `SP5` in this round's frozen list **fails for an exhibited coherent lift of an
> exhibited visible family**, at evidence level 2, with the violating times named and the
> inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `SP5` is
> additional structure and not a consequence of coherence.** This is a verdict on the exact
> proposition frozen under the label `SP5`, on the data grant frozen for it, and on nothing in its
> neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
> refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
> strengths and none is enlarged.

The violating time is **`t = 0`** and the named invariant is the **vanishing of an off-diagonal Gram
entry**, which phase equivalence preserves entrywise: `‖G^{(0)}_{01}‖ = ¼` for every coherent lift of
this family, while the diagonal tuple's off-diagonal entries are zero.

**Question (B): `SP5-EMPTY`.** Carried by `tj2e_sp5_empty`. **The mechanism is emptiness and not
survival, and the two are kept apart.**
> At the exhibited configuration **no** coherent lift of the named visible family satisfies `SP5`,
> proved universally over the lifts of that family at evidence level 2, with the excluded quantity
> computed — while the family **does** have coherent lifts, exhibited. **So `SP5` does not select
> there, by excluding every trajectory rather than by leaving several.** The two mechanisms are
> kept apart: this is not the outcome in which several trajectories survive. It settles one
> configuration and is not a statement about every configuration.

**The configuration is named**: `|V| = 4`, `|A| = 1`, anchor `0`, `Γ ≡ ¼` constant in time. **The
excluded quantity is computed**: at `|A| = 1` admissibility forces `‖U_t(i,0)(j,0)‖ = ½` at every
anchored entry, so `‖G^{(i)}_{jk}(U_t)‖ = ¼` at **every** `j` and `k` — the off-diagonal Gram mass is
`¼` and never vanishes — while the diagonal tuple has zero there and phase equivalence preserves
vanishing entrywise. The exhibited coherent lift of the same family is `U ≡ H(1)`. **The freeze rated
this row at medium and it landed.** The route through act 12's rank bound that the freeze's
countercontrol column names is recorded as a discrepancy in section 13 and the freeze is not edited.

**The refutation is of the exact frozen proposition.** It is **not** a refutation of decoherence in
general, nor of any other condition in `SP5`'s neighbourhood.

### `TJ2` (f) — `SP4`, the regime probe

**Outcome reached: `SP4-THM`, and vacuous.** Carried by `tj2f_sp4_containment`.
> The candidate named `SP4` holds of **every** coherent lift of every visible family over every
> finite carrier, at evidence level 2. **So `SP4` is not additional structure and constrains
> nothing**: it selects no trajectory, because it excludes none. This is a statement about `SP4` as
> this freeze states it, on its frozen data grant, and it endorses no principle and requires none.

**The finding is the containment, and the frozen wording says so.** Act 13's `fibreCrossGram_diag` is
a definitional identity — `Ξ_i^{(t,t)}(U) = G^{(i)}(U_t)` — so act 13's level-2 datum **contains** the
Gram trajectory at its diagonal, and a rule permitted to read it determines the trajectory **by
containing it**. **That is a theorem about containment and not a selection.**

**`SP4` is outside the frozen selector class and was executed as a probe of the data regime**, so
that the effect of crossing the data line is on the record as a theorem rather than as a warning.
**`SP4`'s verdict is not evidence about any member of `𝒮`**, in either direction, and **no line of
the hierarchy quantifies over `SP4`.** **The prediction was `SP4-THM` and vacuous, at high, and it
landed.**

### What no `TJ2` verdict establishes

* **A verdict on one candidate is not a verdict on another**, except along the frozen chain
  `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2`, where a refutation of a weaker member refutes every stronger one, and
  that propagation is reported **as propagation**.
* **`X-ADD` is not a criticism and `X-THM` is not praise.** They answer whether the candidate is
  additional structure, which is a prerequisite question and not a verdict on merit. A negative at
  (A) is what a selection principle **must** return; a positive at (A) would mean the candidate
  selects nothing.
* **`X-NOSEL` and `X-EMPTY` at one configuration are not statements about every configuration.** Act
  12's `SH1-C2` supplies configurations — the deterministic visible laws — at which the per-slice
  orbit is unique for free, so a failure to select somewhere is **not** a failure to select
  everywhere.
* **Naming a candidate is not endorsing it.** Each was named as an object of test and for no other
  purpose. **The round endorses none**, and no sentence here says a selection principle is required.

## 7. `TJ3` — the outcome, on its own axis

**Outcome reached: line 4, `TJ3-IMP`.** Carried by
`tj3_imp_class_level_selection_impossibility`.
> **Selection impossibility at the class level is exhibited.** There is a configuration —
> admissible under exactly this round's own constraints, the visible family having at least one
> coherent lift, exhibited — at which **every** member of the frozen selector class
> `𝒮 = {SP1L, SP2, SP3, SP5}` fails to select, each for a recorded reason: either two
> `GramTrajEquiv`-inequivalent trajectories survive it, or it excludes every trajectory. At
> evidence level 2, with the quantifiers in the order `∃ C ∀ S` and the configuration chosen first.
> **This is impossibility within a frozen class of four named principles at one exhibited
> configuration.** It is **not** impossibility over all conceivable selection principles, **not** a
> statement that no selection principle exists, **not** a statement that selection fails at every
> configuration — act 12's `SH1-C2` supplies configurations where the per-slice orbit is unique for
> free — and **not** a bound on what a later round could name or prove. It was earned by an
> exhibited countermodel and never by a search. `P0` stays **OPEN** and two-part, its threading
> part is untouched, and nothing here names, endorses or excludes a selection principle beyond
> refuting the four exact propositions this freeze states.

**The line reached is the highest the kernel actually carries, and no higher.**

* **Line 1, `TJ3-UNIQ`, is NOT claimed, by either route.** **Route A was not taken** — no universal
  `SelectsAt` theorem for a named member of `𝒮` is proved, and three of the four are refuted at (B)
  at an exhibited configuration while the fourth is empty there. **Route B was not taken** — the
  `SP1G` determination claim is **refuted** at `TJ2` (b), not proved. **Neither route was taken and
  the two are not mixed.** **An unrefuted candidate is not a selecting one**, and no candidate of
  this round is even unrefuted.
* **Line 2, `TJ3-CLASS`, is NOT claimed.** No parameter type and no map from parameters to Gram
  trajectories is exhibited, and in particular **the completeness direction — the surjectivity
  obligation — is not proved.** `TJ1` characterizes the admissible set as the product over time of
  the per-slice realizable sets, which is a **description** and not a parameterization by a type
  independent of the trajectories. **No parameterization is reported as a classification.**
* **Line 3, `TJ3-CON`, is RULED OUT by `TJ1` and is not reported here at all** — and **not reported
  UNDECIDED either**. The exclusion is reported in section 4, under `TJ1`, as that target's own
  positive finding. **No pointwise narrowing is reported as a cross-time constraint.**
* **Line 5, UNDECIDED, is not the outcome**, because a settling outcome was reached.

**The prediction was line 4, `TJ3-IMP`, at medium, and it landed.** The medium rating was for
`SP5` (B)'s computation, on which the fourth conjunct depends; that conjunct landed, so line 4's
`∀ S` conjunct is complete over all four members and the round did not fall to line 5.

### The quantifier structure, written out

**Line 4, as proved:**

> **∃** a configuration `C` = (`V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼` constant in time), such
> that `C` is **admissible** — `∃ U₀, CoherentLift a₀ Γ U₀`, exhibited as a conjunct — **∀** `S` in
> the frozen four-member class `𝒮 = {SP1L, SP2, SP3, SP5}`, `¬ SelectsAt a₀ Γ S`.

**The quantifier order is `∃ C ∀ S` and it is load-bearing.** The configuration is chosen **first**
in the statement and in the proof, and it defeats **all four** members. **The reversed order
`∀ S ∃ C` — for every selector some configuration defeats it — is a strictly weaker statement and is
NOT line 4**: it is exactly the conjunction of the four per-candidate `X-NOSEL` and `X-EMPTY`
verdicts, it is reported under `TJ2` in section 6 where those verdicts live, and **it is not labelled
line 4 anywhere in this round.**

**`C` is admissible under the round's own constraints**, and the statement carries the existence of a
coherent lift of `Γ` as a conjunct for exactly that reason: an impossibility bought by stepping
outside the admissible class would prove nothing about selection within it.

**The statement records which of the two mechanisms holds for each of the four members separately**,
as conjuncts: `SP1L`, `SP2` and `SP3` are each satisfied by **two** exhibited coherent lifts whose
trajectories are inequivalent — the survival mechanism — while `SP5` is satisfied by **no** coherent
lift of the family at all — the emptiness mechanism.

**The relation any quotient is taken over is `GramTrajEquiv`, by name, and no other relation.** It is
not act 12's per-slice `GramPhaseEquiv` at a single time, and it is not act 13's threading relation.

**Lines 1 and 2 are not reported, so their quantifier structures are not written out**: there is
nothing of that shape in the kernel to write.

## 8. The two axes, kept apart

**These are two findings answering two questions, and this round reports them on two axes.**

| axis | finding | where it is reported |
| --- | --- | --- |
| **the `TJ1` baseline, outside the ladder** | The admissible Gram trajectories of a visible family are exactly the pointwise realizable assignments, so **the present `CoherentLift` notion contributes no further universal cross-time constraint, and any such law must enter as additional structure.** A **positive** result, co-primary, and **not** a hierarchy line. | section 4 |
| **the `TJ3` selector-class outcome** | Against that baseline, four frozen candidate principles were tested, and the outcome is **line 4, class-level selection impossibility at one exhibited admissible configuration**. | section 7 |

**The two are not merged into one ordering, and the `TJ1` result is not reported as a hierarchy
line.** The freeze fixes the reason and it is recorded here: "OI itself imposes no cross-time
coupling" is not naturally above or below "these four proposed selectors all fail at one admissible
configuration". **Neither axis is evidence for the other**, beyond the one dependency the freeze
states in both directions — that `TJ1` sufficiency rules line 3 out.

## 9. The anti-conflation clause, carried verbatim at each mention

**THE CLAUSE is carried at every prose mention of act 16's positive as bearing on trajectory
freedom.** **Six carriages in all**: **four** in this result note, **one** in the module docstring,
and **one** in the `ROADMAP`. Each carriage opens with **its own naming line, distinct per carriage
and placed as the first line inside the block quote**, contiguous with the body, so that the
carriages read as distinguishable copies of one clause rather than as one paragraph pasted
repeatedly.

**The relation to acts 15 and 16, stated once.** Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are the
nearest positives to this round's subject and are the ones most easily misread into it. They appear
in **analysis only**.
> **THE CLAUSE, carried at this mention — the result note's statement of the relation to acts 15 and 16.**
> Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
> that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
> re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
> time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
> statement about the threading pair on a named carrier, and it is not a statement about the
> cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
> those two carriers **does not license the assumption that all residual trajectory freedom is
> gauge**: act 16 established a cancellation on named carriers and established **nothing** about
> whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
> rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
> treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
> is physical; no target of this round consumes either for that purpose; and no candidate selection
> principle is named, rated, predicted, admitted or refuted on their strength.**

**No target of this round is carried by them.** No target cites either as evidence, and no
determination changed sign or strength because of either. **Neither was consumed as evidence about
trajectory freedom** anywhere in this round: the Lean module imports act 16's module only as the
tail of the repository's linear import chain, and **no result of act 15 or act 16 is applied in any
proof here.** This is checked by reading the proof of every named result in the module: the merged
results actually applied are act 12's `sh1_necessity`, `sh1_sufficiency`, `fibreGram_apply`,
`fibreGram_left_mul`, `hadamard_slices_not_twoSided` and `star_mul_self_eq_norm_sq`, and act 13's
`ct3g_fibreGram_strong_right` and `fibreCrossGram_diag` — and nothing else from acts 14, 15 or 16.

**One resemblance is recorded so that it is not mistaken for a bridge.** Act 16's triples and this
round's trajectories are both built from the same lift and the same two group actions. But act 16's
objects live where a constant in-fibre left move and a strong right family **can be seen**, and this
round's equivalence is constructed so that neither can be seen at all. **The two rounds quantify over
different things and neither would establish the other.** Recording the resemblance is not
transferring it.
> **THE CLAUSE, carried at this mention — the result note's record of the structural resemblance recorded as not a bridge.**
> Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
> that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
> re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
> time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
> statement about the threading pair on a named carrier, and it is not a statement about the
> cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
> those two carriers **does not license the assumption that all residual trajectory freedom is
> gauge**: act 16 established a cancellation on named carriers and established **nothing** about
> whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
> rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
> treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
> is physical; no target of this round consumes either for that purpose; and no candidate selection
> principle is named, rated, predicted, admitted or refuted on their strength.**

## 10. What no outcome licenses, in the freeze's own wording

**None of the following is written in any artifact of this round, in any paraphrase, summary line,
abstract, table cell or propagation line.**

1. **"The trajectory freedom is gauge", or "the trajectory freedom is physical."** Not written.
   Act 14's status rule that there is no carrier-free verdict binds this round too, this round
   adopts no carrier and defines none of its own, and **nothing here says the residual trajectory
   freedom is redundancy and nothing here says it is not.**
2. **Any sentence that treats act 16's `RN3⁺` or act 15's `PQ3-d⁺` as evidence about the trajectory
   freedom.** Not written. The anti-conflation clause governs:
   > **THE CLAUSE, carried at this mention — the result note's list of what no outcome licenses.**
   > Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
   > that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
   > re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
   > time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
   > statement about the threading pair on a named carrier, and it is not a statement about the
   > cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
   > those two carriers **does not license the assumption that all residual trajectory freedom is
   > gauge**: act 16 established a cancellation on named carriers and established **nothing** about
   > whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
   > rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
   > treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
   > is physical; no target of this round consumes either for that purpose; and no candidate selection
   > principle is named, rated, predicted, admitted or refuted on their strength.**

3. **"No selection principle exists", or "nothing can select the trajectory."** Not written. Line 4
   is impossibility within a frozen class of four named principles at one exhibited configuration,
   and **it quantifies over `𝒮` and over nothing else.**
4. **"Selection fails everywhere."** Not written. Act 12's `SH1-C2` proves the per-slice orbit unique
   on deterministic visible laws, so the trajectory there is determined by the law for free, and
   **every non-selection verdict of this round names its configuration.**
5. **"The candidate class is exhaustive", or "these are the selection principles."** Not written. The
   class is four named propositions frozen for testing.
6. **"A selector is required", or "`P0` needs additional structure of shape X."** Not written. `TJ1`
   says every cross-time constraint is additional structure; **it does not say one is needed.**
7. **"The trajectory is unconstrained", asserted on the strength of a necessity-only `TJ1`.** Not
   written. Both directions landed, and the statement made is the characterization, not an
   unconstrainedness claim.
8. **"The narrowing is cross-time", asserted of a pointwise constraint.** Not written. **`TJ1`'s rank
   bound narrows slice by slice and is labelled pointwise in terms.**
9. **"The admissible set is classified", asserted on the strength of a parameterized family.** Not
   written. **No parameterization is exhibited at all**, and the completeness direction is not
   proved.
10. **"No selector selects", asserted on the strength of `∀ S ∃ C`.** Not written. **Line 4 is
    `∃ C ∀ S`, and the difference is the whole content of the line.**
11. **"A witness was sought and not found, so there is none."** Not written. **No search is presented
    as exhaustive**, and no line of the hierarchy is earned by the absence of a witness.
12. **Any statement about the threading, the cross-time representative, the relative evolution or the
    relative candidate.** Not written. These are invisible to this round's relation by construction,
    and **a round that cannot see a distinction may not report one**, in either direction.
13. **Any statement about act 14's four carriers**, or any adoption of a carrier, or any assertion
    that a carrier is not the physical one. Not written. **This round defines no carrier and reads
    none.**
14. **"`P0` is closed", or "`P0`'s trajectory part is closed."** Not written. **The row stays OPEN and
    two-part**, and `P0`'s threading part is untouched.
15. **"Act 12's `SH1` is enlarged", or "`TG3` is a universal statement."** Not written. `SH1` is
    consumed in both directions at its own strength and `TG3` existentially, about its own exhibited
    dilations. **A merged existential is not enlarged to a universal by being consumed.**
16. **"Act 13 is revised", or "`CT2` (b) is weakened."** Not written. This round consumes
    `ct3g_fibreGram_strong_right` and `fibreCrossGram_diag` and **revises nothing**.
17. **"OI and QM are inequivalent."** Not written. **Two lifts differing is not two theories
    differing**, and every visibility statement here is under act 7's own readback convention with
    `D4b` **negative**.
18. **"The trajectory is continuous", "smooth", "generated by a Hamiltonian".** Not written.
    **`CoherentLift` is `ℕ`-indexed and this round does not change that**; no continuity,
    differentiability or limit is used anywhere.
19. **Any sentence about Track I**, or about Source B or Source C, on any axis. Not written. **Only
    Source A is adjudicated**, and Track I is not touched in either direction.
20. **Any import from the substratum Lemma 24.1 rounds.** Not written. **A shared word is not a
    bridge.**

**The status rule as honoured.** Each target above is reported with **exactly the sentence frozen for
the outcome reached**, quoted verbatim. **No outcome chose its own wording, and no target is reported
at a strength the kernel does not carry.** **UNDECIDED was a live preregistered outcome for every
target and was not reached for any.** **The anti-contamination invariant is honoured**: sibling
results present at the mandated base are **not** inputs, nothing from any sibling lane is consumed,
cited, compared or waited for, and the round consumes only what the start-state table names.

### The freeze's named hazards, each checked

**The strongest hazard is letting act 16's positive carry into the trajectory question**, and it did
not occur.
> **THE CLAUSE, carried at this mention — the result note's account of the freeze's strongest hazard.**
> Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
> that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
> re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
> time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
> statement about the threading pair on a named carrier, and it is not a statement about the
> cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
> those two carriers **does not license the assumption that all residual trajectory freedom is
> gauge**: act 16 established a cancellation on named carriers and established **nothing** about
> whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
> rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
> treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
> is physical; no target of this round consumes either for that purpose; and no candidate selection
> principle is named, rated, predicted, admitted or refuted on their strength.**

The remaining hazards, each checked: **no candidate read unlicensed data** — the per-candidate grants
were respected and `SP4` was executed **outside the class** precisely so the effect of crossing the
line is a theorem; **the question was not answered in the equivalence relation** — the uniform-phase
relation, which couples the slices, was **not adopted** and is recorded as a distinct relation;
**the threading was not seen** — `gramTrajEquiv_of_threading` proves it invisible and `GL2`'s pair is
one trajectory here; **raw Gram equality was not read as the round's relation** — every statement
names `GramPhaseEquiv` or `GramTrajEquiv` and none asserts raw equality as trajectory equality;
**line 2 was not reported on a parameterized family** — none was exhibited; **no trivial
parameterization was taken**; **line 3 was not reported on a pointwise narrowing**, and **not
reported UNDECIDED where sufficiency landed**; **line 1's two routes were not mixed** and neither was
taken; **line 4's quantifiers were not reversed**; **the countermodel is inside the admissible
class**, the existence of a coherent lift being a conjunct; **line 4 was not enlarged to all
selection principles**; **no unrefuted candidate was treated as a selecting one**; **the round was
not enlarged mid-execution** — every outcome reported was preregistered with its own frozen wording;
**no candidate was endorsed by being named**; **no neighbourhood was refuted in place of a
proposition**; **`TG3` and `SH1-C2` were not consumed beyond their strengths**; **the anchor and the
rank bound were not dropped** — `FibreGram a₀` carries its anchor in every statement and
`sh1_sufficiency` is used with its rank hypothesis intact; **no time structure the index type does
not have was imported**; **`P0`'s threading part was not touched**; **no sibling round's result was
consumed**; and **no substratum vocabulary was imported**.

## 11. The frozen `P0` sentence for the case reached

**Case A governs** — `TJ0` silent, `TJ1` landed in both directions, `TJ2` (a)–(f) landed as
predicted, and `TJ3` reached line 4. **This is the case the freeze predicts.** The sentence appended
to the `P0` row is Case A's, verbatim, with the baseline clause, the verdict clause and the bound
clause all taken as Case A writes them, because `TJ1` and `TJ3` both landed in the Case A branch:
> `P0` remains open and two-part, and the answers of acts 11 through 16 stand exactly as those rounds
> state them. The part act 16 left standing — what selects or constrains the Gram/orbit trajectory
> across time — is now bounded rather than resolved. Relative to the round's frozen cross-time
> equivalence, under which two lifts have the same trajectory when their per-slice fibre-Gram tuples
> agree modulo the anchored phases at every time and which therefore identifies every pair act 13
> localized as threading-related, the admissible Gram trajectories of a visible family are exactly
> the pointwise realizable assignments: the merged record constrains each slice by act 12's `SH1` and
> imposes no coupling between slices, so every cross-time constraint on the trajectory is additional
> structure rather than a consequence of coherence, and there is no additional universal cross-time
> constraint on coherent Gram trajectories beyond pointwise realizability — a statement about
> coherence as the programme defines it, indexed by the naturals and pointwise in time, and not a
> statement that no cross-time structure could be added to the programme. Against that baseline four named candidate
> principles were frozen before the search and tested — a per-lift law-determination constraint,
> orbit stationarity under a constant visible law, a homogeneous transition rule, and the decoherence
> rule that the orbit is the diagonal tuple — together with the cross-lift law-determination claim
> and one deliberate out-of-regime probe, and on that class the outcome is class-level selection
> impossibility: there is one visible family, admitting coherent lifts, at which every member of the
> frozen class fails to select, three by leaving two inequivalent trajectories and the decoherence
> rule by excluding every trajectory through act 12's rank bound. That is impossibility within a
> frozen class of four named principles at one exhibited configuration, earned by an exhibited
> countermodel and never by a search; it is not impossibility over all conceivable selection
> principles, and act 12's `SH1-C2` supplies deterministic visible laws where the per-slice orbit is
> unique for free. Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are carrier-specific cancellation verdicts
> about the threading pair and are not evidence that the trajectory freedom is redundancy; nothing
> here treats them as such. `P0`'s threading part is untouched, **no carrier is adopted as the
> physical one**, and nothing here names, endorses or excludes a selection principle beyond refuting
> the exact propositions this round froze.

**The `P0` row's label is unchanged: it stays OPEN.** **No composition closes `P0`, and neither of
its two parts is reported closed.**

## 12. The relation to acts 11 through 16 — every merged label consumed, none revised

| act | labels | how consumed |
| --- | --- | --- |
| act 7 | `D3`, `D4a`, `D4b`, `D5`, `R-2`, `R-3`, the readback amendment | `AdmissibleDilationAt` and the readback convention are consumed **unmodified**; **act 7's boundary is carried at every use of the visible family** — `D4b` came back **negative**, so Source A supplies no general map carrying the relative candidate on the dilated carrier back to `V`. `D5` stands **NOT CERTIFIED** and is not touched. |
| act 11 | `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2` | `CoherentLift`, `StrongAnchorStabilizer`, `WeakAnchorStabilizer` and `GaugeRelated` are consumed **unmodified**. **`GL2`'s pair is one trajectory for this round**, and nothing here bears on the relative evolution. None is revised. |
| act 12 | `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `RO1`, `LG1` | **`SH1` is consumed in BOTH directions at its own strength**, slice by slice, and is neither enlarged nor revised; the rank bound is act 12's. **`TG3` is consumed EXISTENTIALLY**, about its own exhibited dilations, and is not enlarged to a universal. **`SH1-C2` is consumed as an at-most-one statement about deterministic slices** and is cited as supplying configurations where the orbit is unique for free — never as a witness of this round. `TG2` is the per-slice orbit theorem and is not restated. |
| act 13 | `CT1`, `CT2`, `CT3`, `CT4`, `CL1` | `ct3g_fibreGram_strong_right` and `fibreCrossGram_diag` are consumed and **nothing of act 13 is revised**. **`CT3` (d) is act 13's fork, stays UNDECIDED, and is untouched by this round.** `CT2` (b)'s residual is **identified** by this round's relation, which is a property of the relation and not a weakening of `CT2` (b). |
| act 14 | `PQ0`–`PQ4` | **Not consumed.** The four carriers are in the forbidden data set `F`, and no result of act 14 is applied in any proof here. **Act 14's status rule that there is no carrier-free verdict binds this round too.** |
| act 15 | `CF0`–`CF5`, `PQ3-d⁺` | **Not consumed as evidence about anything in this round**, and appearing in analysis only, under the anti-conflation clause. **`PQ3-d⁺` stands exactly as act 15 states it** and is not weakened, qualified, revised or enlarged. |
| act 16 | `RN0`–`RN4`, `RN3⁺` | **Not consumed as evidence about anything in this round**, and appearing in analysis only, under the anti-conflation clause. **`RN3⁺` stands exactly as act 16 states it** and is not weakened, qualified, revised or enlarged. |

**No merged label is revised, corrected, reinterpreted or normalized by anything in this round.**

## 13. Discrepancies — recorded and NOT repaired

**Two items are recorded. Neither is repaired, and the freeze is not edited.** The preregistration is
immutable once merged, and an execution that diverges **records the discrepancy** rather than
repairing the freeze.

**(1) Act 12's lifted `TG3` statement does not expose the constancy of its visible family.** The
freeze's countercontrol for `SP1L` (A) and `SP2` (A) names "the coherent lift of the **constant**
visible law `Γ ≡ ¼`", and act 12's merged `hadamard_lifts_not_twoSided` states that both lifts are
coherent lifts of **one** `Γ` but **does not carry `Γ`'s constancy as a conjunct**, so the constancy
`SP2`'s hypothesis needs cannot be read off it. The constancy is exposed by act 12's own
`hadamard_slices_not_twoSided`, which pins `Γ = Matrix.of (fun _ _ => 1/4)` by an equation. This
round therefore re-exhibits act 12's **same** lifted pair from the slices — the same matrices, the
same anchor, the same visible family, the same configuration — with the constancy written as a
conjunct of its own statements. **Act 12's statement is neither enlarged, revised, nor re-proved**;
what is added is this round's own statement of the same exhibited objects. **Recorded, and the freeze
is not edited.**

**(2) `SP5` (B)'s kernel route is not the route the freeze's countercontrol column forecasts.** The
freeze names `fibreGram_rank_le`, `sh1_necessity` and `hadamard_slices_not_twoSided` as what the
emptiness "would consume", through the observation that the diagonal tuple for `Γ ≡ ¼` on `|V| = 4`
is `(1/4)·I₄` in every fibre, of rank `4`, against the rank bound `|A| = 1`. The kernel route
actually taken computes **the excluded quantity itself**: at `|A| = 1` admissibility forces
`‖U_t(i,0)(j,0)‖ = ½`, so every fibre-Gram entry has modulus `¼` and **no off-diagonal entry
vanishes**, while phase equivalence preserves vanishing entrywise and the diagonal tuple's
off-diagonal entries are zero. **The configuration is the one the freeze names and no other, the
frozen label reached is `SP5-EMPTY` as predicted, and the countercontrol shape is the frozen one** —
a universal exclusion over the lifts of that family, with the excluded quantity computed, plus an
exhibited coherent lift of the same family. `fibreGram_rank_le` is still consumed in this round,
inside act 12's own `sh1_necessity` through `RealizableGram`, at `TJ1`. **This is recorded as a
divergence from the freeze's forecast of consumption and is not repaired, not corrected, not
reinterpreted and not normalized.**

**Two observations, recorded as observations and never substituted as witnesses.**

* **At the frozen configuration `SP1L` and `SP2` coincide extensionally.** Because `Γ ≡ ¼` is
  constant in time, `Γ t = Γ s` holds for all `t` and `s`, so `SP1L`'s hypothesis is always
  discharged and the two predicates have the same extension **at that configuration**. They remain
  **distinct frozen propositions** — `SP2` is `SP1L` restricted to constant families, and `SP1L` is
  strictly the stronger — and line 4's `∀ S` ranges over the four-member class as frozen. **This is
  recorded, and it changes no verdict and no quantifier.**
* **A second kernel route to `SP5`'s refutation exists at the same configuration**, through act 12's
  rank bound as the freeze forecasts. It was not taken, for the reason recorded in item (2). **It is
  recorded as an observation and was never substituted as the witness**, because a configuration or
  a witness chosen after an outcome is known is a preregistration failure in miniature.

**No start-state discrepancy arose.** Every blob in the freeze's start-state table, and every blob in
its table of files this round writes onto, matches at the mandated base; the verification is in
section 14.

**No candidate discovered during execution was executed.** The candidate list is closed at the
freeze, and none was added.

## 14. The chronology certification

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The question is asked of the **real** `pull_request.head.sha` from the Actions event
payload, **never** the synthetic merge commit, and an unresolvable head **fails closed** with no
fallback. The check also requires that **every** commit of `git rev-list H ^B` itself descends from
`B`, so that pre-freeze side history merged in alongside the execution is refused.

**This is a SEALING round** under `AGENTS.md` `§A.37`. It lands **`E` → `L` → `P`, with `P`
mandatory**. **`_TRJ_SEALED_HEAD` and `_TRJ_MERGE` are unset at execution.** That is a statement
about this execution and stays true as one. **The seal-integrity clause excludes this round's own
triple.** `_trj_prior_seals` names **only** acts 13's, 14's, 15's and 16's triples and says nothing
whatever about `_TRJ_BASE`, `_TRJ_SEALED_HEAD` or `_TRJ_MERGE`, so the clause is true both before and
after the mandatory pin commit `P` sets this round's pins. **A clause fixing this round's own pins at
unset for all time would contradict the mandatory lifecycle** — the guard would then pass at no
commit once the round landed — **and that is precisely how an earlier round in this programme was
found non-landable after certifying at its own head.** **Acts 13's, 14's, 15's and 16's seals are
untouched** and **no existing seal constant is altered.** **Before certification this execution
absorbed no later `main`**: no merge from `main`, no rebase, no amend and no force-push.

**The eight preconditions, each checked at the mandated base `B` = `02cfc9be`:**

| # | precondition | result |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | **PASS** — `git rev-list --parents -n 1 B` shows two parents, and the preregistration blob at the pinned path hashes to `3b5570102aa6aacb09788059989a70d8cdd5b70f` |
| 2 | Act 16's execution is merged and sealed | **PASS** — `_RNC_SEALED_HEAD` and `_RNC_MERGE` both present and non-unset at the values act 16 set |
| 3 | Act 15's execution is merged and sealed | **PASS** — `_TCF_SEALED_HEAD` and `_TCF_MERGE` both present and non-unset at the values act 15 set |
| 4 | Act 14's execution is merged and sealed | **PASS** — `_PQT_SEALED_HEAD` and `_PQT_MERGE` both present and non-unset at the values act 14 set |
| 5 | Act 13's execution is merged and sealed | **PASS** — `_CTI_SEALED_HEAD` and `_CTI_MERGE` both present and non-unset at the values act 13 set |
| 6 | The modules this round consumes are in the tree | **PASS** — all three `git cat-file -e` checks succeed |
| 7 | No act 17 execution object precedes the freeze | **PASS** — the act 17 directory holds `preregistration.md` alone, and no `GramTrajectorySelection.lean` is in the tree |
| 8 | The guard tag and its stem are still free | **PASS** — no occurrence of `R7-TRJ` and no occurrence of `_TRJ` in the guard file |

**No sibling lane's merge is a precondition of this round**, and the execution waited for none.

**The claim is scoped to the repository record.**

## 15. The axiom table — one line per named result

| named result | axioms |
| --- | --- |
| `gramPhaseEquiv_refl` | `[propext, Classical.choice, Quot.sound]` |
| `gramPhaseEquiv_symm` | `[propext, Classical.choice, Quot.sound]` |
| `gramPhaseEquiv_trans` | `[propext, Classical.choice, Quot.sound]` |
| `gramTrajEquiv_refl` | `[propext, Classical.choice, Quot.sound]` |
| `gramTrajEquiv_symm` | `[propext, Classical.choice, Quot.sound]` |
| `gramTrajEquiv_trans` | `[propext, Classical.choice, Quot.sound]` |
| `gramTrajEquiv_of_threading` | `[propext, Classical.choice, Quot.sound]` |
| `tj1_necessity` | `[propext, Classical.choice, Quot.sound]` |
| `tj1_sufficiency` | `[propext, Classical.choice, Quot.sound]` |
| `tj1_trajectory_set` | `[propext, Classical.choice, Quot.sound]` |
| `tj1_no_universal_cross_time_constraint` | `[propext, Classical.choice, Quot.sound]` |
| `tj2a_sp1l_add` | `[propext, Classical.choice, Quot.sound]` |
| `tj2c_sp2_add` | `[propext, Classical.choice, Quot.sound]` |
| `tj2b_sp1g_add` | `[propext, Classical.choice, Quot.sound]` |
| `tj2d_sp3_add` | `[propext, Classical.choice, Quot.sound]` |
| `tj2e_sp5_empty` | `[propext, Classical.choice, Quot.sound]` |
| `tj2e_sp5_add` | `[propext, Classical.choice, Quot.sound]` |
| `hadamard_constant_lifts` | `[propext, Classical.choice, Quot.sound]` |
| `tj2a_sp1l_nosel` | `[propext, Classical.choice, Quot.sound]` |
| `tj2c_sp2_nosel` | `[propext, Classical.choice, Quot.sound]` |
| `tj2d_sp3_nosel` | `[propext, Classical.choice, Quot.sound]` |
| `tj2f_sp4_containment` | `[propext, Classical.choice, Quot.sound]` |
| `tj3_imp_class_level_selection_impossibility` | `[propext, Classical.choice, Quot.sound]` |

**Twenty-three named results, nothing outside the three standard axioms, no `sorry`, no added axiom
and no `native_decide`.** `decide` over finite index types is kernel-checked and is used at four
places, all of them deciding numeral disequalities in `Fin 4` and `ℕ`. **`Classical.choice` appears
in `TJ1`'s sufficiency direction, which assembles a lift from a per-time choice, and its appearance
there is not a defect**, as the freeze records in advance. **`TJ0` is type P and is not in this
table.**

**Evidence level 2** is reached for `TJ1`, for each part of `TJ2` at the label it reached, and for
`TJ3` at line 4.

## 16. The definition budget

**Four slots were budgeted. Two fired and two are unused. No fifth definition was introduced and no
amendment was needed.**

| slot | definition | state |
| --- | --- | --- |
| 1 | `GramTrajEquiv` — the round's frozen cross-time equivalence on Gram trajectories | **fired** |
| 2 | `SelectsAt` — the selection predicate lines 1 and 4 both quantify over | **fired** |
| 3 (conditional) | a predicate for `SP3` | **unused** |
| 4 (conditional) | a named diagonal Gram tuple | **unused** |

Slots 3 and 4 are unused because `TJ2` (d), `TJ2` (e) and line 4 are all readable with the conditions
written **inline**: `SP3`'s implication and `SP5`'s diagonal tuple appear as bound predicates pinned
by equations in the statements that need them, which is exactly what the freeze's conditional wording
contemplates.

**The module holds exactly two top-level definitions and no others.** **No lift, gauge element,
witness, matrix, visible family, Gram tuple, entry value or configuration is a top-level
definition** — each is a bound variable pinned by an equation in the statement that needs it, as acts
10 through 16 did. **Acts 7's, 10's, 11's, 12's and 13's definitions are reused, not redefined**: in
particular `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `CoherentLift` and `TwoSidedRelated` are
consumed and **none is restated**.

## 17. The predictions, against the outcomes

| target | predicted | strength | reached | verdict |
| --- | --- | --- | --- | --- |
| `TJ0` | negative — the record is silent | high | `TJ0`-silent | **as predicted** |
| `TJ1` necessity | positive | high | positive | **as predicted** |
| `TJ1` sufficiency | positive | high | positive | **as predicted** |
| `TJ2` (a) `SP1L` (A) | `SP1L-ADD` | high | `SP1L-ADD` | **as predicted** |
| `TJ2` (a) `SP1L` (B) | `SP1L-NOSEL` | high | `SP1L-NOSEL` | **as predicted** |
| `TJ2` (b) `SP1G` (A) | `SP1G-ADD` | high | `SP1G-ADD` | **as predicted** |
| `TJ2` (c) `SP2` (A) | `SP2-ADD` | high | `SP2-ADD` | **as predicted** |
| `TJ2` (c) `SP2` (B) | `SP2-NOSEL` | high | `SP2-NOSEL` | **as predicted** |
| `TJ2` (d) `SP3` (A) | `SP3-ADD` | medium | `SP3-ADD` | **as predicted** |
| `TJ2` (d) `SP3` (B) | `SP3-NOSEL` | high | `SP3-NOSEL` | **as predicted** |
| `TJ2` (e) `SP5` (A) | `SP5-ADD` | high | `SP5-ADD` | **as predicted** |
| `TJ2` (e) `SP5` (B) | `SP5-EMPTY` | medium | `SP5-EMPTY` | **as predicted** |
| `TJ2` (f) `SP4` | `SP4-THM`, and vacuous | high | `SP4-THM`, and vacuous | **as predicted** |
| `TJ3` | line 4, `TJ3-IMP` | medium | line 4, `TJ3-IMP` | **as predicted** |
| `TJ3` → line 1, route A | not predicted | low | not reached | **as predicted** |
| `TJ3` → line 1, route B | not predicted | low | not reached | **as predicted** |
| `TJ3` → line 2 | not predicted | low | not reached | **as predicted** |
| `TJ3` → line 3 | ruled out, conditional on `TJ1` sufficiency | high, *that it is ruled out* | ruled out by `TJ1` | **as predicted** |
| `TJ3` → line 5 | not predicted | medium | not reached | **as predicted** |

**No prediction of this freeze is falsified, and none is against sign.** That is itself worth stating
plainly rather than leaving to inference: **this round confirmed its freeze throughout**, and the two
rows the freeze rated at medium — `SP3` (A) and `SP5` (B) — both landed, which is why line 4's
`∀ S` conjunct is complete and the round did not fall to line 5.
