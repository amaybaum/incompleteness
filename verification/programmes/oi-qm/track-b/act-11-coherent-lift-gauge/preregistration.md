# Track B act 11 — the coherent-lift gauge no-go: CONTROL PLANE

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
| Act 5's result (the smooth diagonal-gauge counterexample) | `../act-05-source-a-candidate/result.md`, blob `c8cdd11a96f547d10763caf1922f84b2afaae92f` |
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

## Why this round exists, and what it replaces

Acts 9 and 10 characterized *conventions* — the readback map (`RB3`) and the anchor (`AB0`) — on a
structure that is underdetermined one level up. `AdmissibleDilationAt G a₀ U` constrains `U` **only**
through `G i j = ∑_a ‖U (i,a) (j,a₀)‖²`. That fixes an anchored modulus-squared marginal; **it does
not determine a channel.** So two admissible dilations may induce genuinely different quantum
operations, and every ambiguity Track B has chased is a shadow of the missing assignment from OI
visible data to a quantum operation.

**Stinespring uniqueness cannot close that gap**, and the reason is a matter of order: Stinespring
speaks about dilations *of a given channel*, whereas here the channel is not yet pinned. Acts 9 and
10 closing without restoring uniqueness is exactly what this diagnosis predicts.

**This round attacks the level above.** It asks what a coherent time-indexed lift on a fixed carrier
determines, and what it leaves free.

## The structural boundary, FROZEN BEFORE ANYTHING ELSE

**Act 11 is intentionally in dilation-choice territory. Construction and deformation of dilated
families are within scope here. This does not amend or evade act 10; act 10 prohibited those
constructions because its frozen question held the act 7 dilations fixed.**

That sentence is frozen first because the round would otherwise look like the move act 10 was
blocked for. The difference is not presentational: act 10's question quantified over anchors with
the dilations held fixed, so a constructed dilation answered a question nobody had preregistered.
Act 11's question **is** the dilation-choice question, so constructing and deforming families is the
subject matter rather than a trespass.

**Still out of scope here:** manuscript propagation; any candidate-selection principle; `C5`; any
comparison of Source A with Source B or Source C; any Track I sourcing. And **act 11 revises no
merged label** — see the immutable inputs below.

## The objects, FROZEN

Fix a visible carrier `V`, an ancilla `A`, and an anchor `a₀ : A`. Write

    S_{a₀} = span { e_{(j, a₀)} : j ∈ V }   ⊆   ℂ^{V × A}

for the **anchored input subspace**, and

    𝒢_{a₀} = { K ∈ U(V × A)  :  K restricted to S_{a₀} is the identity }

for the **anchored stabilizer**. This is exactly the freedom act 7's merged
`admissible_mul_of_fixes_anchor` consumes: its hypothesis `∀ p j, P p (j, a₀) = if p = (j, a₀) then
1 else 0` says `P` fixes each anchored basis vector, i.e. `P ∈ 𝒢_{a₀}`.

A **coherent lift** of a visible family `Γ : ℕ → Matrix V V ℝ` is a single family
`U : ℕ → Matrix (V × A) (V × A) ℂ` on **one fixed carrier and anchor**, with `U t` admissible for
`Γ t` at `a₀` for every `t`. Relative objects are `U_{t←s} := U t * (U s)ᴴ`, and the **relative
candidate** is its frozen readback, exactly as act 7's `MovesVisibleCandidate` reads it.

Two coherent lifts are **gauge-related** when there is a family `K : ℕ → 𝒢_{a₀}` with
`U' t = U t * K t` for every `t`. **`K` is not required to be constant in time** — that is the whole
point, and see `GL3`.

## Three targets, logically separate, FROZEN

### Target 1 — `GL1`, the gauge-group theorem

Unitarity forces `S_{a₀}^⊥` to be invariant under any `K ∈ 𝒢_{a₀}`, whence

    𝒢_{a₀}  ≅  U(S_{a₀}^⊥)  ≅  U( |V| · (|A| − 1) ),
    dim_ℝ 𝒢_{a₀} = ( |V| · (|A| − 1) )².

**The edge case is part of the target**: `|A| = 1` gives the trivial group, and the round must say so
rather than leave it implicit. On act 7's carrier (`|V| = |A| = 2`) this is `U(2)`, of real
dimension `4`.

`GL1` also carries the **pointwise orbit classification**:

    U' = U * K  for some K ∈ 𝒢_{a₀}    ⟺    U' and U agree on S_{a₀}.

The reverse direction is `K = Uᴴ U'`: agreement on `S_{a₀}` makes that `K` fix the subspace
pointwise, and it is unitary as a product of unitaries.

**A consequence to be recorded, because it disposes of a weaker question in advance.** The
per-time gauge-invariant content of a lift is therefore the **anchored columns themselves** —
complex amplitudes, phases included — and **not merely their moduli**. The OI-visible datum is a
coarse-graining of those columns (squared moduli summed over the ancilla index within each visible
fibre). So **every OI-visible quantity is gauge-invariant, and strictly fewer than the
gauge-invariants.** A round asking "are the gauge-invariants exactly the visible data?" would be
asking a question already settled in the negative by algebra; act 11 does not ask it.

### Target 2 — `GL2`, the no-go, and `GL3`, its exact locus

**`GL2`** — there is a coherent lift `U` of a visible family, and a family `K : ℕ → 𝒢_{a₀}`, such
that `U' t = U t * K t` is a coherent lift of **the same** visible family, with **exact cross-time
composition** holding for both, and yet the relative candidate **differs**. The mechanism is that
`U'_{t←s} = U t * (K t) * (K s)ᴴ * (U s)ᴴ` depends on `K t (K s)ᴴ`.

**The cocycle condition is vacuous and the freeze says so before the round runs.** With relatives
*defined* as `U t (U s)ᴴ`, the identity `U'_{t←s} U'_{s←r} = U'_{t←r}` holds for **every** family
whatsoever. So "coherence" in the cocycle sense constrains nothing and cannot exclude anything. Any
round that claimed to derive force from it would be claiming force from a tautology.

**`GL3` — the obstruction is exactly TIME-DEPENDENCE.** If `K t = K` for all `t`, then
`K t (K s)ᴴ = 1` and **every relative candidate is unchanged**. A constant gauge is invisible even
relatively. So the freedom that moves the relative candidate is precisely the *time-dependence* of
`K`, which is why the missing structure has the shape of a connection rather than of a single frame
choice. `GL3` is a universal statement and is required to be proved as such, not asserted.

**Regularity does not rescue this, and act 5 is the frozen countercontrol.** Act 5's merged result
already exhibits a **smooth** `D(s) = diag(1, exp(iπ f(s)))` with `D(0) = D(t′) = 𝟙`,
`D(t) = diag(1, −1)`, leaving `Γ(s ← 0)` unchanged at **every** `s` while the relative readout moves
from the identity to the swap. Whatever regularity class the execution assumes, `K` may be chosen in
the same class.

### Target 3 — `GI1` / `GI2`, is the ambiguity *entirely* gauge?

This is the target that matters for the equivalence theorem, and it is **not** settled by `GL2`.

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`GI1`** | **Every** two coherent lifts of the same visible family are gauge-related by some time-dependent `K : ℕ → 𝒢_{a₀}` — the whole relative ambiguity is **pure gauge** | a universal theorem over coherent lifts of a common visible family |
| **`GI2`** | **There exist** two coherent lifts of the same visible family that are **not** gauge-related — part of the ambiguity is **not** gauge at all | an exhibited pair, with non-gauge-relatedness **proved**, not observed |

`GI1` and `GI2` are contradictory. **Neither is preregistered as the expected answer at the strength
`GL1`–`GL3` are**; see the prediction section, which separates the confidence levels honestly.

**Why the distinction decides the shape of the remaining work.** Under `GI1`, the extra structure
needed to reach QM is exactly a gauge fixing — a rule selecting `K t`, i.e. a connection — and the
relative candidate is not an OI observable without one. Under `GI2`, "gauge" does not even name the
whole ambiguity, and the extra structure must be larger than a gauge fixing.

## The merged witnesses do DIFFERENT work here, and their roles are frozen now

Act 7's two `DC1` witnesses are **frozen countercontrols, not discoveries of this round**. They enter
in **different** roles, and the derivation is recorded so the execution cannot re-assign them:

- **Witness B is a `GL2` instance.** Its two lifts are `(U_t, U_s) = (𝟙, U)` and
  `(𝟙, U·P(ρ))` with `ρ = swap((0,1),(1,1))`. So `K t = 𝟙` and `K s = Uᴴ U P(ρ) = P(ρ)`, and act 7
  proved `P(ρ)` fixes every anchored column — that is precisely the `hfix` hypothesis its exhibition
  discharges. **So witness B's two lifts ARE gauge-related, by a time-dependent `K`**, and the
  relative candidate moves from `1/2` to `0`. Witness B is therefore an instance of `GL2`'s
  mechanism and is **silent on `GI1` versus `GI2`**.
- **Witness A is a candidate `GI2` instance.** Its two lifts are `(𝟙, P(prodComm))` and
  `(𝟙, P(prodComm · swap((1,0),(1,1))))`, so `K s = P(swap((1,0),(1,1)))` — which **moves**
  `(1,0) ∈ S_{a₀}` and is therefore **not** in `𝒢_{a₀}`. Two admissible dilations of one slice need
  not agree on the anchored columns, since admissibility constrains only a fibre-summed modulus, so
  non-gauge-relatedness is available in principle.

**Both readings are predictions, not results, and both must be PROVED in execution.** In
particular, witness A being a `GI2` instance requires proving that **no** `K ∈ 𝒢_{a₀}` relates the
pair — not merely that the obvious candidate `K s` fails. Exhibiting one non-stabilizer `K` is not
the statement; the statement is universal over `𝒢_{a₀}`, and this file records that in advance
because the cheap version is the tempting one.

## The preregistered predictions, at HONEST and DIFFERENT confidence levels

**`GL1` — expected to go through as stated**, including the `|A| = 1` edge case. It is linear algebra
and the derivation is written out above.

**`GL2` and `GL3` — predicted, and strongly.** In the frozen wording:

> Ordinary cross-time coherence, even with the currently admitted smoothness/regularity, does not
> eliminate the time-dependent stabilizer freedom. The visible OI family therefore does not uniquely
> determine the relative quantum evolution. Any recovery of uniqueness requires an additional
> principle restricting or selecting the time-dependent lift.

The support is not a guess: the cocycle condition is vacuous by construction, act 5 exhibits a smooth
time-dependent gauge that moves the relative readout, and witness B exhibits an anchor-fixing one.

**Why the prediction is nevertheless worth proving.** It converts three separate merged observations
into one structural statement about what OI does and does not fix, with the locus identified
(`GL3`: time-dependence) and the gauge measured (`GL1`: `dim = (|V|(|A|−1))²`). That is what the
classification step needs and what none of the three observations supplies alone.

**`GI1` versus `GI2` — NOT predicted at that strength.** The witness-A reading above is the round's
expectation, which would give **`GI2`**, but it rests on an unproved universal over `𝒢_{a₀}` and
this file declines to assert it. A round that reported `GI2` merely because the obvious `K` fails
would be reporting a failed search as a universal — the error acts 7, 9 and 10 each refused.

## What none of these outcomes licenses

- **No outcome here closes `P0`**, and none revises act 7 layer 2's caveat or act 9's sharpening of
  it. `GL2` makes the caveat structural rather than provisional; it does not retire it.
- **`GL2` is not a proof that OI and QM are inequivalent.** It says the visible family does not *by
  itself* fix the relative evolution. A conditional equivalence with an additional stated principle
  is untouched, in either direction.
- **`GL2` is not a candidate-selection principle, and does not show one is required.** It shows
  that *some* additional structure would be needed for relative uniqueness. Naming or endorsing a
  particular one is out of scope, and `C5` is neither named nor adopted.
- **`GI1` does not make the relative candidate an OI observable.** Under `GI1` the ambiguity is pure
  gauge, which is a statement about the *shape* of the freedom, not its elimination.

## The relation to act 7's `D3`, frozen to prevent two labels for one question

> **Act 11 subsumes `D3` as a proposed uniqueness mechanism, but does not close `D3`'s source-level
> existence/regularity audit. `D3` remains open only for whether the source supplies a coherent lift
> and with what regularity; act 11 asks whether coherence, once present, can remove dilation-choice
> freedom.**

**Existence is not presumed cheap.** Pointwise Stinespring plus a vacuous cocycle gives a dilation at
each time, but a coherent lift needs **one fixed carrier and anchor serving the whole family**, and
Source A's stated bounds (`N′ ≤ N²`, `Ñ ≤ N³`) make that a genuine constraint. If the execution
cannot exhibit a coherent lift within those bounds on the witnesses it uses, that is a **reportable
existence gap on `D3`'s side of the split**, not a licence to weaken `GL2`'s hypothesis.

## Immutable inputs

Cited and consumed **unmodified**. None may be revised, re-strengthened or re-scoped by this round:

- act 7's **`DC1`** — existential, at reduced strength, under `R_{a₀}` on anchored dilations, with
  both witness exhibitions;
- act 7's **`DC2a`**, **`D4a`**, **`D4b`**, and the merged `admissible_mul_of_fixes_anchor`;
- act 8's **`CE1`** (existential);
- act 9's **`RB3`**, **`RB1-A`**, **`RB1-B`**, and the sharpened caveat wording;
- act 10's **`AB0-A`**, **`AB0-B`**, the withheld `AB1` labels, and
  `one_admissible_at_every_anchor`;
- act 5's diagonal-gauge construction, as a **countercontrol**;
- acts 1–6's labels;
- act 7 layer 2's **`D5` chronological-ordering control**, which stands **NOT CERTIFIED** and is not
  repaired retroactively by anything here.

**The direct-branch statement is frozen exactly, and no more:** `D4a` is positive on the direct
branch; `T1` is **necessary, not sufficient**; the `n = 3` properness statement remains **evidence
level 3**; **no claim is made about what fraction of OI lies in the direct sector.** This round
targets the off-direct extension problem **without** assuming the direct branch is large.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name

The ordering discipline is act 10's, and the execution **must reuse act 10's guard mechanism** rather
than re-derive one. Three defects of this family have already been found in review — a shallow-clone
gap, a synthetic-merge-commit gap, and head-only ancestry — and each showed green under a weaker
design:

1. **This preregistration blob is merged into `main` before any execution-specific act 11 object
   enters the repository tree** — any Lean definition or proof about lifts, gauges or their orbits,
   any search, any probe guard, any result artifact. **The single permitted exception is the analysis
   recorded inside this control-plane blob itself**, which is merged *as* the freeze.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An unresolvable
   head **fails closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` the merge commit of this control plane
   and `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed. Head-only ancestry admits a commit made before `B` and
   later merged alongside it, and is therefore insufficient.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated
   commit alike.

**The claim is scoped to the repository record**: git certifies what entered the tree and when, not
what anyone thought or drafted outside it.

## Definition budget

The execution introduces **at most five** top-level definitions, and these are the five:

1. **The anchored stabilizer `𝒢_{a₀}`** — as a predicate or subgroup. *Needed.*
2. **`CoherentLift`** — an admissible family on a fixed carrier and anchor. *Needed.*
3. **`GaugeRelated`** — two lifts related by a time-dependent stabilizer element. *Needed.*
4. **A relative-candidate abbreviation**, *if* the propositions cannot be stated readably without
   one. *Conditional.*
5. **`GI1`'s or `GI2`'s proposition**, *unless* each is statable directly from slots 2 and 3, in
   which case unused. *Conditional.*

**A sixth definition requires its own append-only amendment**, separately frozen and merged before
use. **No lift, gauge element, witness or carrier is a top-level definition** — each is a bound
variable pinned by an equation in the statement that needs it, as act 10 did.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide`.

## Named hazards

1. **Claiming force from the cocycle condition.** It is vacuous. Any argument that coherence
   *constrains* the gauge is wrong, and the freeze records this before the round runs.
2. **Reporting `GI2` from a failed search.** Non-gauge-relatedness is a universal over `𝒢_{a₀}`. The
   obvious `K` failing is not the statement — this is the same error `DC4`, `RB1` and `AB0` each
   guarded against, here in a third shape.
3. **Mis-assigning the witnesses.** Witness B is gauge-related and is a `GL2` instance; witness A is
   the `GI2` candidate. Using B for `GI2`, or A for `GL2`, would misreport both.
4. **`GL2` over-read as OI ≠ QM.** It bounds what the visible family fixes by itself, and says
   nothing about a conditional equivalence with a stated extra principle.
5. **`GL2` over-read as requiring a candidate-selection principle.** It shows *some* structure is
   needed for relative uniqueness, not that any particular one is.
6. **Presuming coherent-lift existence.** A fixed carrier within Source A's bounds serving the whole
   family is a real constraint; a failure there is a `D3`-side existence gap to report, not a reason
   to weaken `GL2`.
7. **Answering `D3`'s existence/regularity audit.** Subsumption here is of the *uniqueness
   mechanism* only, per the frozen clause.
8. **A chronology guard that certifies only the head.** See clause 5.

## Non-doings

Do not: run any part of the execution before this file is merged; introduce any execution-specific
object about lifts, gauges or their orbits before then (**the frozen derivations inside this blob are
the permitted exception, per chronology clause 1**); revise `DC1`, `DC2a`, `D4a`, `D4b`, `CE1`,
`RB3`, `RB1-A`, `RB1-B`, `AB0-A`, `AB0-B`, act 7 layer 2's `D5` NOT-CERTIFIED status, or any
act-1-through-10 finding; claim `P0` closed; retire or weaken act 7 layer 2's caveat; close `D3`'s
existence/regularity audit; assert `GI1` or `GI2` without a theorem of the stated shape; report
`GL1` without the `|A| = 1` edge case; adopt or propose a candidate-selection principle; name or
adopt `C5`; claim OI and QM inequivalent; compare Source A with Source B or Source C on any axis;
source anything across to Track I; edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.** No Lean, no probe guard, no roadmap edit, no census edit.
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard (pinning this blob and certifying the side-history-excluding ancestry
  of clause 5), the `ROADMAP` propagation, and the census entry.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`GL1`** — the stabilizer identified exactly, with its dimension and the `|A| = 1` edge case, and
   the pointwise orbit classification;
2. the recorded consequence that the per-time gauge-invariants are the anchored **amplitudes**, and
   that the OI-visible data are a strict coarse-graining of them;
3. **`GL2`** — the no-go, existential and bounded exactly as `DC1` is bounded, with the vacuity of
   the cocycle condition stated rather than leaned on;
4. **`GL3`** — the obstruction localized to time-dependence, as a universal theorem, with the
   constant-gauge case proved harmless;
5. act 5's smooth construction and witness B's anchor-fixing one, cited as **countercontrols** with
   their roles as frozen above;
6. **`GI1` or `GI2`** — with the route to the label, and with `GI2` presented as a proved universal
   over `𝒢_{a₀}` rather than a failed search; or **neither**, reported as undecided, if no theorem of
   the stated shape was reached;
7. the `D3` split as frozen: uniqueness mechanism subsumed, existence/regularity audit still open,
   with any coherent-lift existence gap reported on that side;
8. what the outcomes do **not** license, in the wording this file fixes;
9. the definition count against the five-slot budget, with conditional slots marked fired or unused;
10. the chronology control, naming the property certified — no commit reachable from the execution
    head lies outside `B`'s descendants — and what it does not certify;
11. the axiom report, one line per named result.
