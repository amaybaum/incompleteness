# Track B act 11 — the coherent-lift stabilizer no-go: CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe guard, no roadmap
edit, no census edit, and no outcome label. It **does** carry, deliberately, the frozen derivations
and predictions below — that is what a preregistration is for, and recording them before merge is
what makes them auditable rather than retrospective. Every *execution-specific* object is excluded.
It is merged before any execution begins, and the execution PR descends from the commit that merges
it, under the ancestry certificate frozen below.

## Start state

| | |
| --- | --- |
| Merged `main` | `300cbdddf04f9e14583853ce485789f7b0e4558e` (PR #587) |
| Act 5's result (the smooth diagonal-phase counterexample) | `../act-05-source-a-candidate/result.md`, blob `c8cdd11a96f547d10763caf1922f84b2afaae92f` |
| Act 7's governing preregistration (incl. `D3`) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Act 7's readback amendment (`T3`) | `../act-07-dilation-choice/readback-amendment.md`, blob `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| Act 7 layer 2's result (`DC1`) | `../act-07-dilation-choice/layer-2-result.md`, blob `02f93a1c3ec485b5f46b8e02ff52ca4f73e0ee89` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 9's result (`RB3`, `RB1-A`, `RB1-B`) | `../act-09-readback-robustness/result.md`, blob `f918e7b405dec35e01e9d53ca0dd90eb56c34df4` |
| Act 10's result (`AB0-A`, `AB0-B`) | `../act-10-anchor-robustness/result.md`, blob `ec9a6e0d8a7019805aca069abc39f90d632b6a2b` |
| Act 10's module | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists

Acts 9 and 10 characterized *conventions* — the readback map (`RB3`) and the anchor (`AB0`) — on a
structure that is underdetermined one level up. `AdmissibleDilationAt G a₀ U` constrains `U` **only**
through `G i j = ∑_a ‖U (i,a) (j,a₀)‖²`. That fixes an anchored modulus-squared marginal; **it does
not determine a channel.** So two admissible dilations may induce different quantum operations, and
every ambiguity Track B has chased is a shadow of the missing assignment from OI visible data to a
quantum operation.

**Stinespring uniqueness cannot close that gap**, for a reason of order: it speaks about dilations
*of a given channel*, and here the channel is not yet pinned.

## The structural boundary, FROZEN BEFORE ANYTHING ELSE

**Act 11 is intentionally in dilation-choice territory. Construction and deformation of dilated
families are within scope here. This does not amend or evade act 10; act 10 prohibited those
constructions because its frozen question held the act 7 dilations fixed.**

Act 10's question quantified over anchors with the dilations held fixed, so a constructed dilation
answered a question nobody had preregistered. Act 11's question **is** the dilation-choice question.

**Still out of scope here:** manuscript propagation; any candidate-selection principle; `C5`; any
comparison of Source A with Source B or Source C; any Track I sourcing. Act 11 revises no merged
label.

## The objects, FROZEN — and there are TWO stabilizers, not one

Fix a visible carrier `V`, an ancilla `A`, an anchor `a₀ : A`, and write

    S_{a₀} = span { e_{(j, a₀)} : j ∈ V }   ⊆   ℂ^{V × A}

for the **anchored input subspace**. Right multiplication `U ↦ U K` is the deformation this round
studies. Two nested subgroups matter, and **conflating them is the error this freeze exists to
prevent**:

**The STRONG anchored stabilizer** — fixes each anchored basis vector *pointwise*:

    𝒢ˢ_{a₀} = { K ∈ U(V × A)  :  K restricted to S_{a₀} is the identity }

This is exactly the freedom act 7's merged `admissible_mul_of_fixes_anchor` consumes; its hypothesis
`∀ p j, P p (j, a₀) = if p = (j, a₀) then 1 else 0` says `P ∈ 𝒢ˢ_{a₀}`.

**The WEAK anchored stabilizer** — preserves each anchored *line*:

    𝒢ʷ_{a₀} = { K ∈ U(V × A)  :  K e_{(j, a₀)} ∈ ℂ^× · e_{(j, a₀)}  for every j ∈ V }

**`𝒢ˢ_{a₀} ⊆ 𝒢ʷ_{a₀}`, and the inclusion is strict whenever `|V| ≥ 1`.** Fixing the anchored columns
is **sufficient** to preserve the anchored marginal, **not necessary**: a phase
`K e_{(j,a₀)} = e^{iθ_j} e_{(j,a₀)}` leaves `‖(U K)(i,a)(j,a₀)‖ = ‖U(i,a)(j,a₀)‖` entrywise and so
preserves the whole visible family, while lying outside `𝒢ˢ_{a₀}` unless every phase is `1`.

A **coherent lift** of a visible family `Γ : ℕ → Matrix V V ℝ` is a single family
`U : ℕ → Matrix (V × A) (V × A) ℂ` on **one fixed carrier and anchor**, with `U t` admissible for
`Γ t` at `a₀` for every `t`. Relative objects are `U_{t←s} := U t * (U s)ᴴ`, and the **relative
candidate** is its frozen readback, exactly as act 7's `MovesVisibleCandidate` reads it.

Two coherent lifts are **gauge-related with respect to a class `𝒞`** when there is a family
`K : ℕ → 𝒞` with `U' t = U t * K t` for every `t`. **`K` is not required to be constant in time.**

**The relating family is FORCED, and this is recorded because it makes membership decidable.** Since
each `U t` is unitary, `U' t = U t * K t` has the unique solution `K t = (U t)ᴴ * (U' t)`. So two
lifts are gauge-related with respect to `𝒞` **iff** that forced `K t` lies in `𝒞` for every `t`.
Deciding gauge-relatedness is therefore a **membership check on a computed element**, never a search
over the group.

## Four targets, logically separate, FROZEN

### `GL1s` — the strong stabilizer, exactly, as a LOWER BOUND on invisible freedom

Unitarity forces `S_{a₀}^⊥` to be invariant under any `K ∈ 𝒢ˢ_{a₀}`, whence

    𝒢ˢ_{a₀}  ≅  U(S_{a₀}^⊥)  ≅  U( |V| · (|A| − 1) ),
    dim_ℝ 𝒢ˢ_{a₀} = ( |V| · (|A| − 1) )² ,   trivial exactly when |A| = 1.

Plus the **pointwise orbit classification**:

    U' = U * K  for some K ∈ 𝒢ˢ_{a₀}    ⟺    U' and U agree on S_{a₀},

the reverse direction being `K = Uᴴ U'`, which fixes `S_{a₀}` pointwise and is unitary as a product
of unitaries.

**This dimension is a lower bound on the invisible freedom, not its measure.** `𝒢ˢ_{a₀}` is one
subgroup of the visibility-preserving right action, and the round must not present its dimension as
the size of the ambiguity.

### `GL1w` — the weak stabilizer, and its MAXIMALITY

    𝒢ʷ_{a₀}  ≅  U(1)^{|V|} × U( |V| · (|A| − 1) ),
    dim_ℝ 𝒢ʷ_{a₀} = |V| + ( |V| · (|A| − 1) )² .

**The `|A| = 1` case is the one that exposes the distinction and is part of the target.** There
`𝒢ˢ_{a₀}` is **trivial** while `𝒢ʷ_{a₀} ≅ U(1)^{|V|}` has dimension `|V|` — so a round that measured
invisible freedom by `𝒢ˢ` alone would report *none* exactly where act 5's construction lives.

**Maximality, as a target rather than an assumption.** `𝒢ʷ_{a₀}` is claimed to be the **largest**
class of `K` that preserves the visible marginal of **every** admissible `U` — i.e. the largest
*uniform* visibility-preserving right action. The derivation to be formalized: preservation for all
`U` requires `‖P_i U K e_{(j,a₀)}‖ = ‖P_i U e_{(j,a₀)}‖` for every fibre projection `P_i` and every
unitary `U`, which forces `K e_{(j,a₀)}` to be a unit multiple of `e_{(j,a₀)}`. **The `|V| = 1` case
is degenerate and must be stated**, not assumed away.

**Uniformity is part of the claim and the round may not silently drop it.** For a *single* fixed `U`
there can be further `K` preserving that `U`'s marginal alone; `𝒢ʷ_{a₀}` is maximal among classes
that work for every admissible `U`, and the report must say so in those terms.

### `GL2` — the no-go, on `ℕ`-indexed coherence, over `𝒢ˢ_{a₀}`

There is a coherent lift `U` of a visible family and a family `K : ℕ → 𝒢ˢ_{a₀}` such that
`U' t = U t * K t` is a coherent lift of **the same** visible family, with exact cross-time
composition for both, and yet the relative candidate **differs**. The mechanism is that
`U'_{t←s} = U t * (K t) * (K s)ᴴ * (U s)ᴴ` depends on `K t (K s)ᴴ`.

**`𝒢ˢ_{a₀}` is deliberately the weaker choice here**, and it suffices: a nontrivial *invisible*
subgroup that moves relative candidates is already enough for the no-go, and using the smaller group
makes the statement stronger, not weaker.

**The cocycle condition is vacuous and the freeze says so before the round runs.** With relatives
*defined* as `U t (U s)ᴴ`, the identity `U'_{t←s} U'_{s←r} = U'_{t←r}` holds for **every** family
whatsoever. Coherence in that sense constrains nothing and cannot exclude anything. No argument in
this round may draw force from it.

**`GL2` is scoped to `ℕ`-indexed coherence, because that is what `CoherentLift` expresses.** A
smoothness or continuity claim is **not** provable about an `ℕ`-indexed object, so act 11 does not
claim one. Act 5's smooth construction enters as a **prior, separately merged countercontrol on the
continuous side** — evidence that regularity does not rescue uniqueness — and explicitly **not** as
a theorem about this round's object. Any regularity clause in the prediction is attributed to act 5,
never to a theorem of this round.

### `GL3` — the NECESSITY direction, stated as necessity and no more

If `K t = K` for all `t`, then `K t (K s)ᴴ = 1` and **every relative candidate is unchanged**. So
time-dependence of `K` is **necessary** for this right action to alter a relative object.

**This is one direction only, and the freeze fixes the wording.** `GL3` gives necessity; `GL2` gives
that time-dependence **can be** sufficient, existentially, at one exhibited lift. Neither says, and
the round may not say, that *every* time-dependent `K` moves *every* relative candidate — a
time-dependent `K` whose consecutive ratios happen to act trivially on the readback would not. Any
phrasing of the form "the obstruction is exactly time-dependence", read as a two-sided claim, is
**forbidden**; the two directions are reported separately.

### `GI1` / `GI2` — is the ambiguity entirely gauge? Asked over `𝒢ʷ_{a₀}`

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`GI1`** | **Every** two coherent lifts of the same visible family are gauge-related with respect to `𝒢ʷ_{a₀}` by some time-dependent `K` — the ambiguity is **entirely** invisible-gauge | a universal theorem over coherent lifts of a common visible family |
| **`GI2`** | **There exist** two coherent lifts of the same visible family that are **not** so related — part of the ambiguity is **not** invisible-gauge | an exhibited pair with the **forced** `K t = (U t)ᴴ (U' t)` proved to fall outside `𝒢ʷ_{a₀}` at some `t` |

**These are asked over the WEAK class, and that is the point of the repair.** Failure to lie in
`𝒢ˢ_{a₀}` does **not** make an ambiguity non-gauge, since `𝒢ˢ_{a₀}` is not the invisible-freedom
class. Only failure to lie in `𝒢ʷ_{a₀}` — the maximal uniform class of `GL1w` — supports that
reading, and `GI2` is therefore stated against `𝒢ʷ_{a₀}` and nothing smaller.

**Why the fork decides the shape of the remaining work.** Under `GI1` the extra structure needed is
exactly a gauge fixing — a rule selecting `K t`, i.e. a connection. Under `GI2` the extra structure
must be larger than a gauge fixing.

**`GI1` and `GI2` are NOT predicted**, at any strength; see below.

## The merged witnesses: BOTH are `GL2` instances, and NEITHER is a `GI2` candidate

Act 7's two `DC1` witnesses are **frozen countercontrols, not discoveries of this round**. Their
forced gauge elements are computed here so the execution cannot re-assign them:

- **Witness B.** Lifts `(U_t, U_s) = (𝟙, U)` and `(𝟙, U·P(ρ))` with `ρ = swap((0,1),(1,1))`. The
  forced elements are `K t = 𝟙` and `K s = Uᴴ U P(ρ) = P(ρ)`, and act 7 proved `P(ρ)` fixes every
  anchored column — the `hfix` hypothesis its exhibition discharges. **So `K s ∈ 𝒢ˢ_{a₀}`.**
- **Witness A.** Lifts `(𝟙, P(σ))` and `(𝟙, P(σ·τ))` with `σ = prodComm`,
  `τ = swap((1,0),(1,1))`. Under act 7's convention `permMatrix σ p q = if q = σ p then 1 else 0`,
  the forced element is **conjugated**:

      K s = P(σ)ᴴ P(σ·τ) = P( σ τ σ⁻¹ ) = P( swap(σ(1,0), σ(1,1)) ) = P( swap((0,1),(1,1)) ),

  which is the **same** element as witness B's `ρ` — and therefore also **in `𝒢ˢ_{a₀}`**.

**Consequence, frozen in advance: both merged witnesses are gauge-related in the strong class, and
NO merged object is a candidate `GI2` instance.** The `GI1`/`GI2` fork is therefore wide open with
**no instance in hand on either side**, and the round must find its own or report the fork
undecided. A reading that treats either witness as evidence against `GI1` is wrong, and this file
says so before the outcome is known.

**The conjugation is the trap.** Reading witness A's second permutation as contributing
`swap((1,0),(1,1))` — which *would* move the anchored vector `e_{(1,0)}` — is what the convention
makes false. The execution must compute `K t = (U t)ᴴ (U' t)` rather than read a factor off the
constructor.

## The preregistered predictions, at HONEST and DIFFERENT confidence levels

**`GL1s` and `GL1w` — expected to go through as derived**, including the `|A| = 1` and `|V| = 1` edge
cases and `GL1w`'s maximality-under-uniformity.

**`GL2` and `GL3` — predicted, and strongly**, in this wording:

> Ordinary cross-time coherence does not eliminate the time-dependent anchored-stabilizer freedom.
> The visible OI family therefore does not uniquely determine the relative quantum evolution. Any
> recovery of uniqueness requires an additional principle restricting or selecting the
> time-dependent lift.

The support is not a guess: the cocycle condition is vacuous by construction, and witness B exhibits
an anchor-fixing time-dependent element that moves the relative readout. **Act 5's smooth
diagonal-phase construction is cited as separate prior evidence that regularity does not rescue
uniqueness** — it lies in `𝒢ʷ_{a₀}` and **not** in `𝒢ˢ_{a₀}`, and it is on the continuous side, so
it is a countercontrol rather than an instance of `GL2`'s statement.

**`GI1` versus `GI2` — NOT predicted.** No merged object instantiates either side, the forced-element
computation above having removed the candidate this file's earlier draft relied on. Reporting either
label requires the round's own theorem, and **reporting the fork undecided is an allowed outcome**.

## What none of these outcomes licenses

- **No outcome here closes `P0`**, and none revises act 7 layer 2's caveat or act 9's sharpening of
  it. `GL2` makes the caveat structural rather than provisional; it does not retire it.
- **`GL2` is not a proof that OI and QM are inequivalent.** It says the visible family does not *by
  itself* fix the relative evolution. A conditional equivalence with an additional stated principle
  is untouched, in either direction.
- **`GL2` is not a candidate-selection principle and does not show one is required.** It shows some
  additional structure would be needed for relative uniqueness; naming one is out of scope, and
  `C5` is neither named nor adopted.
- **`GL1s`'s dimension is not the size of the invisible freedom** — see the lower-bound clause.
- **`GI1` does not make the relative candidate an OI observable.**

## The relation to act 7's `D3`, frozen to prevent two labels for one question

> **Act 11 subsumes `D3` as a proposed uniqueness mechanism, but does not close `D3`'s source-level
> existence/regularity audit. `D3` remains open only for whether the source supplies a coherent lift
> and with what regularity; act 11 asks whether coherence, once present, can remove dilation-choice
> freedom.**

**Existence is not presumed cheap.** Pointwise Stinespring plus a vacuous cocycle gives a dilation at
each time, but a coherent lift needs **one fixed carrier and anchor serving the whole family**, and
Source A's stated bounds (`N′ ≤ N²`, `Ñ ≤ N³`) make that a genuine constraint. A failure there is a
**reportable existence gap on `D3`'s side of the split**, not a licence to weaken `GL2`.

## Immutable inputs

Cited and consumed **unmodified**:

- act 7's **`DC1`**, **`DC2a`**, **`D4a`**, **`D4b`**, and `admissible_mul_of_fixes_anchor`;
- act 8's **`CE1`** (existential);
- act 9's **`RB3`**, **`RB1-A`**, **`RB1-B`**, and the sharpened caveat wording;
- act 10's **`AB0-A`**, **`AB0-B`**, the withheld `AB1` labels, `one_admissible_at_every_anchor`;
- act 5's diagonal-phase construction, as a **countercontrol**;
- acts 1–6's labels;
- act 7 layer 2's **`D5` chronological-ordering control**, which stands **NOT CERTIFIED** and is not
  repaired retroactively by anything here.

**The direct-branch statement is frozen exactly, and no more:** `D4a` is positive on the direct
branch; `T1` is **necessary, not sufficient**; the `n = 3` properness statement remains **evidence
level 3**; **no claim is made about what fraction of OI lies in the direct sector.**

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name

1. **This preregistration blob is merged into `main` before any execution-specific act 11 object
   enters the repository tree** — any Lean definition or proof about lifts, stabilizers or their
   orbits, any search, any probe guard, any result artifact. **The single permitted exception is the
   analysis recorded inside this control-plane blob itself**, merged *as* the freeze.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most six** top-level definitions, and these are the six:

1. **`𝒢ˢ_{a₀}`**, the strong anchored stabilizer. *Needed.*
2. **`𝒢ʷ_{a₀}`**, the weak anchored stabilizer. *Needed* — `GI1`/`GI2` are stated over it, and the
   strong/weak distinction is the correction this freeze turns on.
3. **`CoherentLift`** — an admissible `ℕ`-indexed family on a fixed carrier and anchor. *Needed.*
4. **`GaugeRelated`**, parameterized by the class, so one definition serves both stabilizers.
   *Needed.*
5. **A relative-candidate abbreviation**, *if* the propositions cannot be stated readably without
   one. *Conditional.*
6. **`GI1`'s or `GI2`'s proposition**, *unless* statable directly from slots 3 and 4, in which case
   unused. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No lift, stabilizer element,
witness or carrier is a top-level definition** — each is a bound variable pinned by an equation in
the statement that needs it, as act 10 did.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide`.

## Named hazards

1. **Conflating the two stabilizers.** `𝒢ˢ_{a₀}` is sufficient for invisibility, not necessary.
   Presenting its dimension as the invisible freedom, or reading non-membership in it as "not
   gauge", is the error this freeze is built around.
2. **Claiming force from the cocycle condition.** It is vacuous.
3. **Reporting `GI2` against the wrong class.** It must be non-membership in `𝒢ʷ_{a₀}`, the maximal
   uniform class, not in `𝒢ˢ_{a₀}`.
4. **Mis-assigning the witnesses.** Both are `GL2` instances and gauge-related in the strong class;
   **neither** is a `GI2` candidate. Reading witness A's constructor factor instead of computing
   `(U t)ᴴ (U' t)` is the specific trap, and the conjugation is recorded above.
5. **Stating `GL3` two-sidedly.** It is necessity only; `GL2` supplies existential sufficiency.
6. **Claiming a regularity theorem about an `ℕ`-indexed object.** Act 5's smooth construction is a
   prior countercontrol on the continuous side, not a theorem of this round.
7. **Dropping uniformity from `GL1w`'s maximality.** Maximal among classes preserving *every*
   admissible `U`'s marginal — a single fixed `U` admits more.
8. **`GL2` over-read as OI ≠ QM**, or as requiring a candidate-selection principle.
9. **Presuming coherent-lift existence** within Source A's bounds.
10. **Answering `D3`'s existence/regularity audit.** Subsumption is of the uniqueness mechanism only.
11. **A chronology guard that certifies only the head.** See clause 5.

## Non-doings

Do not: run any part of the execution before this file is merged; introduce any execution-specific
object about lifts, stabilizers or their orbits before then (**the frozen derivations inside this
blob are the permitted exception, per chronology clause 1**); present `𝒢ˢ_{a₀}` as the invisible
freedom; state `GI1` or `GI2` over `𝒢ˢ_{a₀}`; treat either merged witness as a `GI2` candidate;
state `GL3` as a two-sided claim; claim a smoothness result about the `ℕ`-indexed object; revise
`DC1`, `DC2a`, `D4a`, `D4b`, `CE1`, `RB3`, `RB1-A`, `RB1-B`, `AB0-A`, `AB0-B`, act 7 layer 2's `D5`
NOT-CERTIFIED status, or any act-1-through-10 finding; claim `P0` closed; retire or weaken act 7
layer 2's caveat; close `D3`'s existence/regularity audit; adopt or propose a candidate-selection
principle; name or adopt `C5`; claim OI and QM inequivalent; compare Source A with Source B or
Source C on any axis; source anything across to Track I; edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob and certifying clause 5's ancestry), the `ROADMAP`
  propagation, and the census entry.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`GL1s`** — the strong stabilizer exactly, with its dimension, the `|A| = 1` triviality, the
   orbit classification, and the statement that its dimension is a **lower bound** on invisible
   freedom;
2. **`GL1w`** — the weak stabilizer exactly, its dimension, its **maximality under uniformity**, and
   the `|A| = 1` / `|V| = 1` edge cases, with the strong/weak gap stated;
3. **`GL2`** — the no-go, existential, over `𝒢ˢ_{a₀}`, on `ℕ`-indexed coherence, with the vacuity of
   the cocycle condition stated rather than leaned on;
4. **`GL3`** — necessity of time-dependence, as a universal theorem, reported as one direction;
5. act 5's smooth construction cited as a **prior continuous-side countercontrol**, with its
   membership in `𝒢ʷ_{a₀}` and non-membership in `𝒢ˢ_{a₀}` recorded;
6. the **forced gauge elements** of both merged witnesses, with the conjugation shown, and the
   record that neither is a `GI2` candidate;
7. **`GI1`, `GI2`, or UNDECIDED** — with the route to the label, `GI2` only via a forced element
   proved outside `𝒢ʷ_{a₀}`;
8. the `D3` split as frozen, with any coherent-lift existence gap reported on that side;
9. what the outcomes do **not** license, in the wording this file fixes;
10. the definition count against the six-slot budget, with conditional slots marked fired or unused;
11. the chronology control, naming the property certified;
12. the axiom report, one line per named result.
