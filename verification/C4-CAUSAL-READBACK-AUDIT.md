# C4 causal-readback strengthening audit — can visible-originating readback recover P-indivisibility?

Owner-called from `main` at `5ca538ad0b149e90d4a1bfdf6e52acd5a5d15e61`, the signed merge of the
stochastic observer-interface audit (#537). This file is the preregistration only. No Lean proof,
probe mutation, manuscript edit, stochastic-to-quantum correspondence, or new physical condition is
introduced in this commit.

## Why this round exists

#537 did **not** show that a sourced stochastic observer law is P-divisible or P-indivisible. It
showed that the presently stated substratum architecture determines neither the observation map nor
the ensemble needed to define one. That gap remains binding: this round may not choose a prior,
root pair, or readout because it gives the desired divisibility result.

A separate mathematical issue remains open inside the manuscripts, however. The manuscript's C4 is
a history-level readback condition: two positive-probability visible histories can end in the same
current visible state and have different next-step laws. The old P-D counterexample shows that this
condition, by itself, does not imply P-indivisibility of the rooted one-time transition family. The
counterexample is exactly P-divisible while its history-level C4 gap is maximal.

So the question is no longer “does C4 imply P-indivisibility?” It does not. The question is:

> Is there a stronger, genuinely causal readback formulation — still recognizably the same physical
> readback idea, and stated *before* inspecting a desired example — that does imply P-indivisibility?

This audit separates that pure mathematical question from the independent sourcing question of
whether the frozen architecture supplies the stronger form.

## Scope amendment — controls execution where it conflicts with provisional language below

The provisional preregistration used “strengthening” as shorthand before the exact relation between
candidate rooted-marginal conditions and the manuscript's history-level C4 had been determined.
That shorthand is now too strong. The controlling scope is:

- `C4e` and `C4r` are **candidate causal-readback forms on rooted one-time marginals**;
- the round must determine their mathematical implications for P-divisibility;
- it must separately determine their logical relation to the manuscript's history-level C4;
- neither is called a strengthening, necessary condition, or equivalent condition unless that
  relation is actually proved;
- no candidate is adopted as a new physical condition merely because it succeeds mathematically.

Where the provisional wording below says “stronger C4”, read “candidate causal-readback form” unless
a theorem in the determination section earns the stronger relation.

## Frozen objects

The round uses only finite types and real row-stochastic matrices.

A rooted visible family is a function

> `Γ : ℕ → Matrix V V ℝ`

with every `Γ t` row-stochastic and `Γ 0 = I`. The `i`th row of `Γ t` is the visible distribution at
time `t` from visible root `i`, under one fixed hidden prior common to all roots.

The divisibility convention is frozen as

> `Γ t = Γ s * Λ`

for `s ≤ t`, with `Λ` row-stochastic. The propagator acts on the visible outcome index by right
multiplication. This orientation is not negotiable after the proof starts.

The concrete realization layer, used only where explicitly stated, is

> `R = (V, H, φ, μ_H)`

with finite visible and hidden types, bijection `φ : V × H ≃ V × H`, and one fixed hidden prior
`μ_H` used for every visible root. Its rooted map is

> `Γ_t(i,j) = Σ_h μ_H(h) · 1[π_V φ^t(i,h)=j]`.

No observation map or prior is claimed sourced merely because this structure can be written down.

## Candidate forms, frozen before proof

### C4e — exact causal readback

There exist distinct roots `a ≠ b` and times `s < t` such that

> `row_a(Γ_s) = row_b(Γ_s)`

but

> `row_a(Γ_t) ≠ row_b(Γ_t)`.

Interpretation: two initially distinguishable visible preparations become observationally identical
at time `s` and later become distinguishable again. The later separation therefore cannot be carried
by the current visible marginal alone.

### C4r — distinguishability revival

There exist roots `a,b` and times `s < t` such that

> `TV(row_a(Γ_s), row_b(Γ_s)) < TV(row_a(Γ_t), row_b(Γ_t))`.

C4e is an exact-zero special case of this form. C4r is chosen because row-stochastic post-processing
must contract total variation.

Neither definition mentions histories. That is intentional: the relation to the manuscript's
history-level C4 is one of the questions to be determined, not assumed.

## Source boundary

This round has two layers and reports them separately.

### M — mathematical layer

Can C4e and/or C4r imply P-indivisibility for any row-stochastic rooted family, without using a
hidden realization at all?

### S — sourcing layer

Does the frozen OI architecture supply the successful candidate form on its own physical
realization, without choosing an observation map, hidden prior, root pair, or times for the desired
verdict?

A positive M result and a negative S result is an admissible and scientifically meaningful outcome.

## The core theorem targets

The mathematical pass must attempt, in this order:

### T1 — total-variation contraction

For probability rows `p,q` and row-stochastic `Λ`, prove

> `TV(p Λ, q Λ) ≤ TV(p,q)`.

This is the data-processing statement needed for C4r. If the kernel already contains exactly this
result at the required orientation, reuse it; otherwise prove it directly from nonnegativity and row
normalization.

### T2 — C4r implies P-indivisibility

Assuming `Γ t = Γ s * Λ` with row-stochastic `Λ`, T1 forbids any strict increase in TV between rows.
Therefore C4r must imply failure of divisibility for at least one pair of times.

### T3 — C4e implies C4r

Equal rows have TV zero. Distinct probability rows have strictly positive TV. Therefore C4e should
imply C4r.

### T4 — exact row-obstruction route

Also prove the stronger algebraic statement, independent of total variation:

> If rows `a` and `b` of `A` are equal, then rows `a` and `b` of `A * B` are equal for every matrix
> `B`.

Hence C4e directly forbids **any** factorization `Γ t = Γ s * Λ`, even without stochasticity of
`Λ`. This is an independent proof of the exact condition's consequence and a useful control on the
TV argument.

### T5 — realization row-stochasticity

For the explicit finite reversible realization `(V,H,φ,μ_H)`, prove `Γ_t` is row-stochastic when
`μ_H` is a probability law. This theorem supplies the bridge from the concrete model to the
mathematical layer but does not source the model.

### T6 — mathematical verdict

Freeze the strongest theorem actually obtained, expected to be

> `C4e ⇒ C4r ⇒ P-indivisibility`

plus the independent exact-row route `C4e ⇒ no factorization`.

Do not promote the implication to an equivalence unless the converse is proved.

### T7 — relation to manuscript C4

The existing P-D law already proves that the manuscript's history-level C4 does not imply
P-indivisibility. Since C4e or C4r would imply P-indivisibility if T2 succeeds, the same control would
then prove that the manuscript's C4 does not imply either candidate form.

The reverse direction must be tested rather than guessed. In particular, if C4e gives two roots
that collide at `s` and separate at `t`, determine whether one can always turn that rooted-marginal
revival into two positive-probability histories with a common current state and different future
laws, or whether extra support/conditioning assumptions are needed.

The relation is reported exactly:

- history C4 ⇒ candidate: true / false / open;
- candidate ⇒ history C4: true / false / conditional / open.

No ordering word is used until this table is settled.

## Controls

### P-D — history memory without P-indivisibility

Reuse and, if needed, kernelize the existing P-D law from `review4_probes.py`:

> `X1 ~ Bern(1/2)` independently of `X0`; `X2 = X0 XOR X1`.

It has maximal order-two history memory but rooted maps `Γ_1 = Γ_2 = J/2`, so it is P-divisible
with the identity propagator. It must fail C4e and C4r if T2 is correct.

### P-E — exact delayed revival

Use a frozen exact control chosen before theorem proof:

> `X1 = X0`; `X2 ~ Bern(1/2)` independently; `X3 = X0`.

Then

> `Γ_1 = I`, `Γ_2 = J/2`, `Γ_3 = I`.

At `s=2`, the two root rows coincide; at `t=3`, they separate exactly. This should satisfy C4e and
be P-indivisible because no stochastic right factor can turn identical rows into distinct rows.

The control is deliberately simple and is not claimed to be OI-sourced.

### Orientation control

Show explicitly that the theorem uses `Γ_t = Γ_s * Λ`, not `Γ_t = Λ * Γ_s`. Left multiplication
mixes over the root index and does not preserve equality of two specified rows. The guard must pin the
right-multiplication convention.

### Realization control

Instantiate one finite reversible visible/hidden realization and verify its `rootedMap` rows sum to
one. This tests the bridge without using a realization to prove the layer-independent no-go.

## Sourcing tests

Only after the mathematical verdict is frozen:

1. Does the frozen architecture determine the `RootedRealization` data used by the theorem?
2. Does any already-stated OI condition imply C4e or C4r on that sourced realization?
3. If a candidate follows only after selecting roots, prior or observation map, record S-B below; do
   not call it sourced.
4. If the architecture cannot even define the rooted family, #537 remains binding and S-B is the
   sourcing verdict regardless of the mathematical result.

The horizon `K` is mathematical. Calling it *physically accessible* requires the existing physical
window condition (for example the manuscript's `K tau_S << t_R` reading); the Lean theorem must not
invent a new clock or silently turn an arbitrary finite `K` into an accessible one.

## Admissible outcomes

The result carries one M label and one S label.

### Mathematical labels

- **M-A:** `C4e ⇒ C4r ⇒ P-indivisibility`, with the direct row-obstruction proof too.
- **M-B:** exact C4e implies P-indivisibility but the TV route fails or requires extra hypotheses.
- **M-C:** even C4e does not imply P-indivisibility; exhibit a counterexample.

### Sourcing labels

- **S-A:** existing architecture supplies the successful candidate on the relevant physical
  realization without tuning.
- **S-B:** the mathematical theorem is valid but the successful candidate and/or its rooted family is
  not sourced by the frozen architecture.
- **S-C:** sourcing is mixed or conditional; state the exact additional hypothesis already present in
  the corpus.

The combined expected verdict is **M-A / S-B**.

## Prediction, recorded before proof

**M-A / S-B is expected.** The mathematical argument is the classical data-processing theorem: a
row-stochastic propagator cannot restore distinguishability once two rooted visible distributions
have merged, and exact equality is preserved under arbitrary right multiplication. The existing
P-D control already says why the stronger marginal revival is genuinely more restrictive than the
manuscript's history-level C4.

S-B is expected because #537 found that the architecture does not source the observation map or the
ensemble needed to form the rooted family at all. This round may formulate that family as data and
prove the conditional theorem, but it may not convert supplied data into a sourced physical
prediction.

The prediction is not a result.

## Guards

The round is invalid if any of the following occurs:

- the composition convention is reversed after the proof begins;
- C4e or C4r is called a strengthening, equivalent, necessary or sufficient relation to manuscript
  C4 before T7 determines that relation;
- P-divisibility is identified with Markovianity;
- roots, times, a hidden prior, or an observation map are selected for the desired outcome and then
  reported as sourced;
- reversibility is used in the layer-independent row-obstruction or TV theorem and then reported as
  necessary there;
- a new physical condition is added or adopted;
- anything is named or adopted as a fifth condition;
- a stochastic-to-quantum correspondence theorem is invoked;
- an arbitrary mathematical horizon is called physically accessible;
- #537's source verdict is weakened without a new source theorem;
- a manuscript is edited in the determination commit;
- a P-D or P-E control is silently replaced after its verdict is known.

---

## Determination

The pass is complete. **M-A / S-B.** The mathematical layer succeeds in both preregistered routes,
the exact row-obstruction route more strongly than required. The sourcing layer remains conditional:
this module takes a rooted family, or a finite reversible visible/hidden realization with a fixed
common hidden prior, as data. It does not derive either from the frozen substratum. The relation to
the manuscript's history-level C4 is one-way negative in the direction that matters for this round:
the old P-D law has maximal history memory and is P-divisible, so history C4 implies neither C4e nor
C4r. The reverse direction needs a positive-support bridge and remains open here; therefore neither
candidate is called a strengthening, a necessary condition, or an equivalent condition.

The Lean implementation is `OIBridge/CausalReadback.lean`. Twenty-one named results print only the
accepted foundation axioms `propext`, `Classical.choice`, `Quot.sound`. The root imports the module,
the exact executable mirror is `verification/lean/c4_readback_probe.py`, the registry carries the
family as kernel-only, and guard `R7-C4R` pins the composition convention, the two proof routes, the
history-level separation, the sourcing boundary, and the absence of any correspondence theorem.

### T1 — TV contraction

`tv_mul_le` proves the data-processing statement in exactly the preregistered orientation. If `p`
and `q` are probability rows and `Λ` is row-stochastic,

> `tv (p *ᵥ Λ) (q *ᵥ Λ) ≤ tv p q`.

The proof does not use a hidden realization, reversibility, or any OI condition. Expanding the
matrix-vector product, applying the triangle inequality outcome by outcome, exchanging the two finite
sums, and using the row sums of `Λ` gives the result. This is genuinely new at the required type:
`FiniteEntropy.tv_marg_le` covers deterministic pushforwards, while `tv_mul_le` covers arbitrary
row-stochastic post-processing.

### T2/T3 — the contraction route

`c4e_implies_c4r` uses only the exact equality at the collision time and inequality at the later
time: total variation is zero at `s` (`tv_eq_zero_iff`) and strictly positive at `t`
(`tv_pos_of_ne`). `c4r_implies_pIndivisible` then applies `tv_mul_le` to any proposed stochastic
propagator and contradicts the strict revival. Thus

> `C4e Γ ⟹ C4r Γ ⟹ PIndivisibleWithin Γ K`

for every rooted row-stochastic family, with no realization hypothesis. `c4e_implies_pIndivisible`
is the composite statement. The horizon is only a finite mathematical bound; nothing in the theorem
calls it physically accessible.

### T4 — the exact route

The direct route is stronger than the contraction route. `rows_eq_of_factor` says that if rows `a`
and `b` of `A` are equal, then the same rows of `A * B` are equal for **every real square matrix
`B`**, with no stochasticity or positivity assumption. `c4e_no_factorization` therefore says an exact
collision followed by a separation forbids any right factor at all; `c4e_implies_pIndivisible_exact`
recovers P-indivisibility as a corollary. The two routes are independent: one is stochastic
contraction, the other is pure matrix algebra.

The orientation control is part of the theorem. Right multiplication preserves equality of two
specified root rows. Left multiplication does not: `leftMul_control` is an explicit `2 × 2` control
with equal rows in `A` and unequal rows in `B*A`. So the frozen convention `Γ_t = Γ_s * Λ` is not
notation; it is the statement under which the readback argument is true.

### T5 — the concrete realization bridge

`RootedRealization V H` is exactly the frozen data layer: a permutation `step` of `V × H`, a common
hidden prior `prior : H → ℝ`, nonnegativity and normalization. `rootedMap R t i j` marginalizes the
`H` coordinate after `t` steps from root `i`. `rootedMap_nonneg`, `rootedMap_rowsum` and
`rootedMap_isRowStochastic` prove that every such map is row-stochastic. No observation map, prior,
root or time is selected; they are fields or theorem parameters. The layer-independent no-go imports
none of this realization structure.

### T7 — relation to manuscript C4

The P-D control is frozen from `review4_probes.py` and rerun exactly by the new mirror:

> `X₁` uniform and independent of `X₀`; `X₂ = X₀ XOR X₁`.

Its rooted family has `Γ₀ = I` and `Γ_t = J/2` for every `t ≥ 1`. `pdFamily_pDivisible` gives an
explicit stochastic propagator for every `s ≤ t`: `J/2` when `s = 0`, identity otherwise.
`pdFamily_not_c4e_not_c4r` proves both candidate forms fail. The exact probe independently computes
the old history fact: `I(X₀;X₂|X₁) = 1` bit, the maximal two-state conditional memory. So the
manuscript's history-level C4 does not imply C4e or C4r.

The reverse direction is not asserted. A rooted marginal collision and later separation does not by
itself provide the positive-probability histories and conditioning events used by the manuscript's
history condition unless an appropriate support hypothesis is added. The audit records that
hypothesis boundary rather than manufacturing it. Consequently the relation table is:

| Direction | Status |
|---|---|
| manuscript history C4 ⇒ C4e | **false** — P-D |
| manuscript history C4 ⇒ C4r | **false** — P-D |
| C4e ⇒ manuscript history C4 | **open here; requires a positive-support bridge** |
| C4r ⇒ manuscript history C4 | **open here; a fortiori not established** |

No ordering word is earned between the manuscript condition and the candidates.

### Separation control P-E

The delayed-revival family is exactly the preregistered one:

> `Γ₀=I`, `Γ₁=I`, `Γ₂=J/2`, `Γ₃=I`, constant thereafter.

`peFamily_c4e` witnesses exact collision at times two and three. `peFamily_pIndivisible` is proved by
the exact route: the two rows at time two are equal and the rows at time three differ, so no matrix
right factor exists. `control_separation` packages P-D and P-E together: history memory without either
candidate and exact marginal revival with P-indivisibility are distinct phenomena.

The executable mirror checks the same matrices by exact rational arithmetic, tests divisibility of
P-D at horizons 1–7, computes the one-bit conditional mutual information directly from the joint
law, verifies the P-E collision/separation and the impossibility of `J/2 * Λ = I`, and reruns the
left-multiplication orientation control. It is independent executable evidence, not the proof.

### Sourcing verdict

**S-B.** The mathematical theorem is valid, but the frozen substratum architecture does not source
the `RootedRealization` used to instantiate it. #537 remains binding: the architecture fixes the
substratum dynamics but does not select an observation map on `Substratum.Conf` or an ensemble, and
therefore does not select the common hidden prior required by the rooted family. The theorem takes
that data; it does not derive it.

No weaker claim is smuggled in under “causal”. `C4e` and `C4r` are marginal-revival signatures. They
show that the current marginal is insufficient to mediate the later family through a stochastic
post-processing map. They do **not** by themselves exhibit a physical hidden variable being written
and later read, and they are not identified with the manuscript's history condition.

## Determination table

| Target | Result | Kernel evidence |
|---|---|---|
| T1 | row-stochastic right factors contract TV | `tv_mul_le` |
| T2 | C4r forbids P-divisibility | `c4r_implies_pIndivisible` |
| T3 | exact collision + later separation implies revival | `c4e_implies_c4r` |
| T4 | exact collision + later separation forbids any right factor | `rows_eq_of_factor`, `c4e_no_factorization`, `c4e_implies_pIndivisible_exact` |
| T5 | finite reversible rooted realization gives row-stochastic family | `rootedMap_nonneg`, `rootedMap_rowsum`, `rootedMap_isRowStochastic` |
| T6 | M-A, both routes; exact route stronger | `causal_readback_verdict` |
| T7 | history C4 does not imply either candidate; converse not proved | `pdFamily_pDivisible`, `pdFamily_not_c4e_not_c4r`, exact P-D probe |
| controls | orientation and phenomenon separation | `leftMul_control`, `peFamily_c4e`, `peFamily_pIndivisible`, `control_separation` |

## What this note does not claim

That C4e or C4r is equivalent to, necessary for, or a proved strengthening of the manuscript's
history-level C4. That either candidate is necessary for P-indivisibility. That P-indivisibility is
Markovianity. That the hidden realization is needed by the no-go: the exact and TV theorems are
layer-independent. That marginal revival alone exhibits a hidden write-then-read mechanism. That
`RootedRealization`, its common prior, or its observation map is sourced by the frozen architecture.
That an arbitrary mathematical horizon is physically accessible. That any new physical condition is
adopted. That a fifth condition exists. That any stochastic-to-quantum correspondence theorem is
stated, cited as a premise, applicable, or inapplicable. That `frozen_sourcing_verdict`,
`krausDense_of_denseControl`, `fixedGateTheory_denseFiniteQM`, `stochastic_interface_gap` or any
existing result is retracted or weakened.

Status: pass complete. M-A on the mathematics and S-B on the sourcing: the frozen chain proved by
two independent routes, the exact route using neither stochasticity nor the layer, the separation
established with the divisibility half in the kernel and the memory half in the exact probe, the
converse to the manuscript's condition left open with its hypothesis named, and the sourcing
conditional with #537 binding; twenty-one named results; no fifth condition; no correspondence
theorem stated or cited; no manuscript edited.


## Post-#538 reconciliation cross-reference — append-only

The later observer-primitive reconciliation (`OBSERVER-PRIMITIVE-RECONCILIATION-AUDIT.md`,
`OBSERVER-PRIMITIVE-RECONCILIATION-RESULT.md`) narrows one sourcing sentence in this frozen round
without changing any C4 mathematics. #537 remains binding for the **reduced A1–A5 substratum
kernel**: invariance alone does not determine an ensemble there, and that kernel carries no
observation projection. It is not, however, a corpus-wide absence theorem.

The maintained manuscript observation layer separately states an `(S, φ, V)` observer cut, a
visible/hidden projection, and a maximal-entropy counting law as its baseline selection principle.
In an exact finite product realization those declared inputs provide a baseline rooted family with a
common uniform hidden prior. Preparation-specific priors remain realization data. Accordingly, the
paragraph above saying that “the stated substratum architecture determines neither the observation
map nor the ensemble” is retained as provenance but is scoped to the reduced substratum layer.

Nothing about `C4e`, `C4r`, `PDivisible`, `PIndivisibleWithin`, their two proofs, or the T7
separation is altered. In particular the manuscript's history-level C4 still has not been proved to
imply `C4e` or `C4r` for the baseline process, so no correspondence audit is earned by this
reconciliation alone.
