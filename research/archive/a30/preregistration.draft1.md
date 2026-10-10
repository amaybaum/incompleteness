# Track B act 30 — act 29's missing conjunct: product-carrier strictification, its transfer, the product-carrier lift, and full admission: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and the
round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 30 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## The declarations

```v3-round
round A30
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-30-product-strict-lift/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-30-product-strict-lift/
record AM verification/receipts/A30.json
execution A verification/lean-mathlib/OIBridge/ProductStrictLift.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean/edge_rigidity_probe.py
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds this preregistration and the result note. The receipt path is
`verification/receipts/A30.json`. Every other path the round changes is an execution path listed
above, and nothing in the legacy-records population is among them.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects).

- **`D`** = `48450428f528fe489d454458e21c9394aef6a02f`, the head of `main` after `V3-14`'s landing,
  certified by push run 36218508975: all three jobs green, the guard 91 PASS and 0 FAIL, the release
  gate 21 of 21 with `v3-receipts` holding on five receipts. Every measurement in this file was taken
  at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E` (or a
  superseded receipt commit); built with `--no-ff` if `main` is still `D`.
- **`Q`** — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A30.json`.

***

## The seven hazards, stated before anything else

**Hazard 1 — strict is not twisted, and the asymmetry runs one way.** Act 20's `rnt1_strict_imp_twisted`
gives `StrictNatural a₀ Ψ → TwistedNatural a₀ id id Ψ`. A strict lift therefore **settles** the
twisted-strength target. The failure to find or prove a strict lift **does not** settle its negation:
a non-strict twisted lift could still exist. So `StrictNatural` is this round's **constructive route**
to `A30-N`, never its target, and `A30-N-NO-LIFT` negates the **twisted** form, for every lift and
every pair of induced maps, and not merely the strict one.

**Hazard 2 — degenerate induced maps.** Conjunct 8 constrains `αL` and `αR` only by act 20's two
closure conjuncts. The constant maps `fun _ => 1` satisfy both, and the record already uses them: act
21's control `ΦC` carries conjunct 8 through a constant lift with `αL = αR = fun _ => 1`. With those
maps, twisted naturality says only that `Ψ` is invariant under the gauge. **No verdict of this round
rests on constant induced maps**: the positive route goes through `StrictNatural`, whose induced maps
are the identities. The reading is recorded as the assumption-watch note below and act 20's
declaration is not repaired.

**Hazard 3 — incompatible witnesses.** A conjunct proved of one family and a conjunct proved of
another prove nothing together. The strictification replaces act 28's family by a pointwise-
equivalent one, and **the replacement must be shown to preserve every conjunct already
established**. That is a named target of this round, `A30-T`, stated as a theorem and never as
prose; `A30-N` and `A30-0` are each a **single existential** whose one witness carries every conjunct
they claim.

**Hazard 4 — reading a single-carrier result into the product carrier.** Act 27's
`a27_0_strict_lift` and `a27_shared_torsor` are statements at carrier `Fin 4` with ancilla `Fin 1`.
Nothing in the record transports them to `Fin 4 × Fin 4` (act 29's RD1). This round **re-proves**
what it needs at the product configuration; it cites act 27 as provenance for the method and
discharges no target by citing it.

**Hazard 5 — a refuted universal read as a refuted existential.** `A30-S` and `A30-T` are
universals; `A30-N` and `A30-0` are existential in the law. One family without a lift refutes no
existential, and act 23's `phiSC_corner` is the standing instance of an eligible family with none.

**Hazard 6 — theorem generalization.** The frozen targets are stated at the exact product
configuration and nowhere else. A carrier-generic helper may appear in the execution as a shared
lemma, but **no verdict is stated of it** and no outcome reports anything at another carrier, ancilla
cardinality or visible family.

**Hazard 7 — a stale status surface.** Acts 28 and 29 each placed a frozen `P0` sentence saying a
question at the product configuration is **undecided**. A decided `A30-0` makes each false, and
`AGENTS.md` §A.27 requires the correction in place. Both sentences are pinned verbatim by those
rounds' guard contracts, `R7-PFR` and `R7-PRA`. The supersession is named in advance below, together
with the contract legs it replaces; nothing else of either contract is touched.

***

## Provenance — what this freeze carries, and what is its own

Consumed as frozen declarations and frozen theorems, never re-proved and never paraphrased:

- **act 7**, `DilationChoice.lean` — `AdmissibleDilationAt`;
- **act 11**, `CoherentLiftGauge.lean` — `WeakAnchorStabilizer`;
- **act 12**, `TwoSidedGauge.lean` — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
  `LeftFibreGroup`, `sh1_sufficiency`, `sh1_necessity`, `fibreGram_apply`,
  `fibreGram_mul_weak_apply`, `weak_diagonal_phase`;
- **act 17**, `GramTrajectorySelection.lean` — `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`,
  `gramPhaseEquiv_trans`;
- **act 18**, `IntermediateCrossTimeStructure.lean` — `ProperAt`, `PropagatesFrom`;
- **act 20**, `RepresentativeNaturality.lean` — `StrictNatural`, `TwistedNatural`,
  `rnt1_strict_imp_twisted`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `EvolvesTotally`, `PreservesAdmissible`, `Reversible`,
  `FactorizesOnProduct`, `LadderConds` (read for its conjunct order only), `realizable_of_gramPhaseEquiv`;
- **act 23**, `OrbitLawGaps.lean` — `phiSC_corner`, the countercontrol;
- **act 27**, `StrictNaturalLift.lean` — `a27_0_strict_lift` and `a27_shared_torsor`, **provenance
  for the method only** (hazard 4);
- **act 28**, `ProductLocusFreedom.lean` — `a28_0_construction`, the family this round strictifies;
- **act 29**, `ProductAdmission.lean` — `a29_p_hold`, consumed at assembly for conjuncts 1 and 2;
  `a29_n_relabel_instance`, cited as the instance act 29 reached.

Its own: everything in the targets below.

## Locating controls — the governing passages at `D`

| what | where at `D` | line |
| --- | --- | --- |
| `FibreGram` | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | 95 |
| `GramPhaseEquiv` | the same file | 102 |
| `RealizableGram` | the same file | 108 |
| `sh1_necessity` | the same file | 168 |
| `sh1_sufficiency` | the same file | 1070 |
| `AdmissibleDilationAt` | `verification/lean-mathlib/OIBridge/DilationChoice.lean` | 134 |
| `WeakAnchorStabilizer` | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | 114 |
| `ProperAt`, `PropagatesFrom` | `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | 167, 186 |
| `StrictNatural`, `TwistedNatural` | `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | 106, 128 |
| `rnt1_strict_imp_twisted` | the same file | 192 |
| `EvolvesTotally`, `PreservesAdmissible`, `Reversible` | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | 96, 108, 123 |
| `FactorizesOnProduct`, `LadderConds` | the same file | 143, 179 |
| `realizable_of_gramPhaseEquiv` | the same file | 355 |
| `phiSC_corner` | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | 850 |
| `a27_shared_torsor`, `a27_0_strict_lift` | `verification/lean-mathlib/OIBridge/StrictNaturalLift.lean` | 249, 330 |
| `a28_0_construction` | `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | 349 |
| `a29_p_hold`, `a29_n_relabel_instance` | `verification/lean-mathlib/OIBridge/ProductAdmission.lean` | 168, 211 |
| act 29's outcome vector | `verification/programmes/oi-qm/track-b/act-29-product-admission/result.md` | 3 |

The blobs at `D` of the modules this round consumes:

| module | blob |
| --- | --- |
| `TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `StrictNaturalLift.lean` | `038f8e77de14f45790fddba69a4a659522d5fa81` |
| `ProductLocusFreedom.lean` | `325c09a180366765ae4d742b752099d3b219d3c9` |
| `ProductAdmission.lean` | `90533c832477ad25e8725f20b7759ac71149c251` |

The names this round reserves were free at `D`, each returning nothing from `git grep -l` at `D`:
`R7-PSL`, `_PSL`, `PSL`, `ProductStrictLift`, `product-strict-lift`, `act-30`, `A30-`, `a30_`. The
bare string `A30` occurs at `D` only inside two binary PDF files.

***

## Why this round exists

Act 29 reached `A29-P-HOLD` · `A29-N-UNDECIDED` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED`. Its
`A29-P` is universal over every family carrying conjuncts 3 to 7, so conjuncts 1 and 2 hold of any
such family. What stopped admission is **conjunct 8**, for a pair of class bijections not induced by
carrier relabellings: act 28's construction supplies an eligible family for every pair, and nothing
in the record supplies a lift for it.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Read from the record at `D`; **nothing was executed**, and the execution is free to find any of it
wrong and record that.

1. **At this configuration the ancilla has one element**, so `LeftFibreGroup` is exactly the diagonal
   row phases and `WeakAnchorStabilizer` exactly the diagonal column phases (act 27 proves both shapes
   at `Fin 4`: `a27_shared_left_shape`, `a27_shared_weak_shape`), and an admissible dilation at the
   product visible family is a unitary every entry of which has modulus `1/4`.
2. **Act 28's family is class-level.** Its value on a locus tuple is `prod (f₁ X) (f₂ Y)` for factors
   `X`, `Y` chosen per class; the anchored phases of the input do not reach the output.
3. **Conjunct 8's lifting clause is an equality.** With right twisted equivariance it forces
   `Φ (K·G) = αR(K)·Φ G` exactly for every dilatable `G` and every column phase `K`, where `K·G` is the
   action of `fibreGram_mul_weak_apply`. Act 28's family satisfies this only up to `GramPhaseEquiv`,
   so it carries no lift as written. **The defect is in the choice of representatives.**
4. **Act 27 removed the same defect at the single carrier.** `a27_0_strict_lift` replaces any
   realizability-preserving descending map by a pointwise-equivalent one with a `StrictNatural` lift,
   through a class-indexed section and `a27_shared_torsor`, which says the gauge action on an
   admissible dilation is free up to one common phase. The argument uses two facts of the
   configuration: the ancilla has one element, and the visible matrix has no zero entry. Both hold at
   the product configuration.
5. **The pairs act 29 reached** are the at most `24 × 24` pairs induced by `σ₁ × σ₂`; the realizable
   class space is not classified in the record.

***

## The configuration, FROZEN — act 29's, unchanged

`V = Fin 4 × Fin 4`, sixteen elements. `A = Fin 1 × Fin 1`, one element. `a₀ = ((0 : Fin 1), (0 : Fin 1))`.
`Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))` on `Fin 4`. The visible family is constant in time,
`Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, every entry `1/16`. The
ordered decomposition is `e = Equiv.refl (Fin 4 × Fin 4)`. **No other configuration is read, and no
verdict is stated of one.**

The notation below abbreviates statements and introduces no definition: `R₁ G` is
`RealizableGram (Fin 1) Γ₀ G` on `Fin 4`; `Rp G` is `RealizableGram (Fin 1 × Fin 1) (Γ 0) G` on
`Fin 4 × Fin 4`; `X ⊠ Y` is `fun i : Fin 4 × Fin 4 => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2`.
Every theorem of the round writes these out.

**The prefix** is act 29's eight conjuncts, in act 21's `LadderConds` order: (1) `ProperAt` and (2)
`PropagatesFrom` of the generated law `fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))`;
(3) `EvolvesTotally`; (4) `PreservesAdmissible`; (5) time homogeneity, `∃ Φ₀, ∀ t, Φ t = Φ₀`;
(6) `Reversible`, both conjuncts; (7) descent, `∀ t G G', GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')`;
(8) at every `t`, `∃ Ψ αL αR`, lifting `FibreGram a₀ (Ψ U) = Φ t (FibreGram a₀ U)` and admissibility
`AdmissibleDilationAt (Γ (t + 1)) a₀ (Ψ U)` for every `U` admissible at `Γ t`, and
`TwistedNatural a₀ αL αR Ψ`.

**A prescribed pair** is act 28's representation of a pair of bijections of the single-carrier
realizable class space: tuple maps `f₁`, `f₂` on `Fin 4` each preserving `R₁`, descending on
realizable tuples, injective on classes and surjective on classes, exactly the eight hypotheses
`a28_0_construction` carries. **The pair clause** for a family `Φ` is
`∀ t G₁ G₂, R₁ G₁ → R₁ G₂ → GramPhaseEquiv (Φ t (G₁ ⊠ G₂)) (f₁ G₁ ⊠ f₂ G₂)`: factorization with the
prescribed maps themselves as factor families. **An eligible family for the pair** carries conjuncts 3
to 7, `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
and the pair clause.

***

## The questions, FROZEN — four targets

### `A30-S` — product strictification

**Does every realizability-preserving, class-descending map at the product configuration have a
pointwise-equivalent replacement with a strictly natural lift?**

> For every `Φ₀` on `Fin 4 × Fin 4` with `∀ G, Rp G → Rp (Φ₀ G)` and
> `∀ G G', Rp G → Rp G' → GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G')`, there exist `Φ₁` and
> `Ψ` with: `∀ G, Rp G → GramPhaseEquiv (Φ₁ G) (Φ₀ G)`; `∀ G, ¬ Rp G → Φ₁ G = Φ₀ G`;
> `∀ G, Rp G → Rp (Φ₁ G)`; for every `U` with `AdmissibleDilationAt (Γ 0) a₀ U`,
> `FibreGram a₀ (Ψ U) = Φ₁ (FibreGram a₀ U)` and `AdmissibleDilationAt (Γ 0) a₀ (Ψ U)`; and
> `StrictNatural a₀ Ψ`.

The clause `∀ G, ¬ Rp G → Φ₁ G = Φ₀ G` is what lets descent, which conjunct 7 states for every tuple,
transfer. Reported `A30-S-HOLD`, `A30-S-FAILS` (an exhibited `Φ₀` with no such `Φ₁`, `Ψ`) or
`A30-S-UNDECIDED`.

### `A30-T` — eligibility survives the replacement

**Does a pointwise-equivalent replacement, equal off realizable tuples, keep eligibility for the same
pair?**

> For every prescribed pair `f₁`, `f₂` and every `Φ₀`, `Φ₁` on `Fin 4 × Fin 4` with
> `∀ G, Rp G → GramPhaseEquiv (Φ₁ G) (Φ₀ G)` and `∀ G, ¬ Rp G → Φ₁ G = Φ₀ G`: if `fun _ => Φ₀` is
> eligible for the pair, so is `fun _ => Φ₁`, with every conjunct of eligibility written out on each
> side.

Reported `A30-T-HOLD`, `A30-T-FAILS` (an exhibited counterexample, naming the conjunct lost) or
`A30-T-UNDECIDED`.

### `A30-N` — act 29's `A29-N`, at its original twisted strength

**For every prescribed pair, is there an eligible family carrying conjunct 8?**

> For every prescribed pair `f₁`, `f₂`, there exists `Φ` on `Fin 4 × Fin 4`, eligible for the pair,
> satisfying conjunct 8 in act 20's existential twisted-lift form, written out:
> `∀ t, ∃ Ψ αL αR, (∀ U, AdmissibleDilationAt (Γ t) a₀ U → FibreGram a₀ (Ψ U) = Φ t (FibreGram a₀ U)) ∧ (∀ U, AdmissibleDilationAt (Γ t) a₀ U → AdmissibleDilationAt (Γ (t + 1)) a₀ (Ψ U)) ∧ TwistedNatural a₀ αL αR Ψ`.

**This is the proposition act 29 froze as `A29-N`**, stated in the same shape, and its answer is the
answer to that target. Its **negation**, the only thing `A30-N-NO-LIFT` may report, is one exhibited
pair for which every eligible family fails conjunct 8 in that form: for **every** `Ψ`, `αL` and `αR`,
not only the strict ones (hazard 1). Reported `A30-N-LIFTS`, `A30-N-NO-LIFT` or `A30-N-UNDECIDED`.

### `A30-0` — act 29's `A29-0`, full admission in ONE existential

> For every prescribed pair `f₁`, `f₂`, there exists **one** `Φ` on `Fin 4 × Fin 4` carrying all
> eight conjuncts of the prefix, each written out, `FactorizesOnProduct` at the frozen decomposition,
> and the pair clause.

**This is the proposition act 29 froze as `A29-0`.** The single-existential requirement is part of
the statement: a conjunction of separate existentials over transition families does not discharge
it. Reported `A30-0-ADMITS`, `A30-0-RESTRICTS` or `A30-0-UNDECIDED`.

### `A29-1` is not a target of this round

Act 29's gated fourth question stays closed here **whatever `A30-0` reaches**. If admission is
reached, `A29-1` is the question for the next round, at act 28's frozen pair, and this round writes
no statement about it.

### Separate verdicts

Each target's label stands on its own measurement. A label is voided by no other target's label;
the gates and corollaries below govern which **combinations** may be reported.

***

## The assumption-watch note — constant induced maps

Recorded here and in the result note, **not repaired**, and not a target.

Conjunct 8 places no constraint on `αL` and `αR` beyond act 20's closure conjuncts. With
`αL = αR = fun _ => 1` it asks for a lift `Ψ` constant along gauge orbits. By the freeze's reading
(hand reasoning, not a result), a family that factors exactly through `GramPhaseEquiv` classes on
dilatable tuples and preserves realizability has such a lift, and every descending family is
pointwise equivalent to one that does. If so, conjunct 8 read with constant maps adds nothing, up to
law equivalence, to conjuncts 4 and 7. **This round establishes none of that**, rests no verdict on
it, and changes no declaration. It is recorded so that a later round reading conjunct 8 as a
restriction knows the reading exists.

***

## The controls

| role | object | what it is for | how consumed |
| --- | --- | --- | --- |
| countercontrol | act 23's `phiSC_corner` | an eligible family with no lift at any time, so no eligible family is assumed liftable; the positive route must replace the family | cited, not re-proved |
| countercontrol | act 27's `a27_t_relabel_no_strict_lift` | a given tuple formula can lack a strict lift while carrying a twisted one, so strict-lift failure of one formula is not read as anything about twisted lifts | cited, not re-proved |
| instance | act 29's `a29_n_relabel_instance` | the relabelling pairs already have eligible liftable families; a positive `A30-N` must reach the pairs that are not so induced | cited, not re-proved |
| positive | act 20's `rnt1_strict_imp_twisted` | the one bridge from the constructive route to the frozen form, used in the forward direction only | consumed |

The identity is not used as a control.

***

## The route, recorded as the freeze's reading and not as a finding

Hand reasoning, with nothing executed.

1. **Shared lemmas at the product configuration** (stage 1): the left and right gauge shapes for the
   one-element ancilla; every entry of an admissible dilation at `Γ 0` is nonzero; the torsor
   statement at `Fin 4 × Fin 4`, following `a27_shared_torsor`'s proof. A carrier-generic form is
   permitted as a shared lemma (hazard 6).
2. **`A30-S`** (stage 2), following `a27_0_strict_lift`'s construction at the product carrier: a
   section `s` of the realizable classes; for realizable `G`, a phase `c` with `G = c · s[G]`; set
   `Φ₁ G = c · Φ₀ (s[G])`, well defined because the phase is unique up to one common factor;
   `Φ₁ = Φ₀` off realizable tuples; `Ψ` defined on each gauge orbit of admissible dilations through a
   dilation of `Φ₁` at the orbit's representative (`sh1_sufficiency`), extended equivariantly, and the
   identity off admissible dilations. The torsor statement makes both well defined and `Ψ` strictly
   natural.
3. **`A30-T`** (stage 3): realizability of `Φ₁ G` from `realizable_of_gramPhaseEquiv`; descent by
   cases, both realizable or both not, since realizability is invariant under `GramPhaseEquiv`;
   `EvolvesTotally`, `Reversible` and the pair clause by transitivity of `GramPhaseEquiv`;
   `FactorizesOnProduct` with the prescribed maps as factor families; time homogeneity because both
   families are constant.
4. **`A30-N`** (stage 4): for a prescribed pair, act 28's `a28_0_construction` gives an eligible family
   (it is time-homogeneous, `Φ t = Φ₀`); `A30-S` at `Φ₀` gives `Φ₁` and `Ψ`; `A30-T` gives
   eligibility of `fun _ => Φ₁`; conjunct 8 at every `t` with that `Ψ` and `αL = αR = id`, the
   lifting and admissibility clauses from `A30-S` (`Γ (t + 1) = Γ t`), and twisted naturality from
   `rnt1_strict_imp_twisted`.
5. **`A30-0`** (stage 4): `a29_p_hold` applied to `A30-N`'s own witness gives conjuncts 1 and 2 of it;
   the eight, factorization and the pair clause then hold of that one family.

### The route-authorization matrix, FROZEN

Authorized for every target without further mention: act 12's `sh1_sufficiency`, `sh1_necessity`,
`fibreGram_apply`, `fibreGram_mul_weak_apply` and `weak_diagonal_phase`; act 17's
`gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`; act 21's
`realizable_of_gramPhaseEquiv`; and this round's own shared lemmas. **A helper needed but absent from
this list is a deviation, recorded against the row it departs from and not repaired.**

| target | may consume | may NOT consume | permitted work |
| --- | --- | --- | --- |
| `A30-S` | the authorized helpers; act 20's and act 12's declarations | `a28_0_construction`; `a29_p_hold`; any single-carrier lift result as a premise | prove or refute the strictification at the product configuration |
| `A30-T` | the authorized helpers; act 21's declarations | `A30-S`'s witness; `a29_p_hold` | prove or refute the transfer |
| `A30-N` | `A30-S`; `A30-T`; `a28_0_construction`; `rnt1_strict_imp_twisted`; the authorized helpers | `a29_p_hold` as a premise for the lift | exhibit the family per pair, or prove the universal negative at an exhibited pair |
| `A30-0` | `A30-N`; `a29_p_hold`; the authorized helpers | act 22's and act 23's verdicts as premises | assemble the single existential, or derive `A30-0-RESTRICTS` from `A30-N-NO-LIFT` |

***

## The preregistered predictions

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A30-S` | `A30-S-HOLD` | **high** | the construction is `a27_0_strict_lift`'s at a carrier where both facts it uses hold; the new work is the product-carrier shape and torsor lemmas |
| `A30-T` | `A30-T-HOLD` | **high** | every conjunct of eligibility is stated up to `GramPhaseEquiv` or is realizability, which that relation preserves, except descent, which the off-realizable equality clause carries |
| `A30-N` | `A30-N-LIFTS` | **high** | corollary of the two above with `a28_0_construction` and `rnt1_strict_imp_twisted` |
| `A30-0` | `A30-0-ADMITS` | **high** | corollary of `A30-N-LIFTS` with `a29_p_hold` |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed, with
the measurement that settled it.

***

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

### `A30-S-HOLD`

> At the frozen product configuration, every map preserving realizability and descending on
> realizable tuples is pointwise `GramPhaseEquiv`-equivalent, and equal off realizable tuples, to a
> map with a strictly natural representative-level lift, at evidence level 2. This is a statement at
> the exact configuration and says nothing about any other.

### `A30-S-FAILS`

> At the frozen product configuration, an exhibited map preserving realizability and descending on
> realizable tuples has no pointwise-equivalent replacement with a strictly natural lift, at evidence
> level 2. This refutes the strictification and nothing more; it says nothing about twisted lifts.

### `A30-S-UNDECIDED`

> Neither the strictification nor a counterexample was obtained. The step at which the proof stopped
> is named, with what would settle it.

### `A30-T-HOLD`

> At the frozen product configuration, replacing a family by one pointwise `GramPhaseEquiv`-equivalent
> on realizable tuples and equal off them keeps every conjunct of eligibility for the same prescribed
> pair, at evidence level 2.

### `A30-T-FAILS`

> At the frozen product configuration, an exhibited replacement of that kind loses the named conjunct
> of eligibility, at evidence level 2.

### `A30-T-UNDECIDED`

> Neither the transfer nor a counterexample was obtained. The conjunct at which the proof stopped is
> named.

### `A30-N-LIFTS`

> At the frozen product configuration, for every prescribed pair of bijections of the single-carrier
> realizable class spaces there is a transition family satisfying conjuncts 3 to 7 and factorization
> with factor families realizing that pair which also satisfies representative-level gauge
> naturality at act 20's certified strength, at the product carrier, at evidence level 2. **This is
> an existence statement about some such family. It does not disturb act 23's verdict about its own
> formula**, which is a statement that one exact formula admits no lift.

### `A30-N-NO-LIFT`

> At the frozen product configuration, for an exhibited pair of bijections of the single-carrier
> realizable class spaces, no transition family satisfying conjuncts 3 to 7 and factorization with
> factor families realizing that pair satisfies representative-level gauge naturality at act 20's
> certified strength at the product carrier, for any lift and any induced maps, at evidence level 2.
> This is a statement about that exhibited pair, and it does not say that any other pair is so
> restricted.

### `A30-N-UNDECIDED`

> Neither a lifting family nor the universal negative was obtained. The obstruction is named, with
> the family or families tried and what would settle it. A family found to admit no lift is recorded
> as that and is not reported as the universal negative, and the absence of a strict lift is not
> reported as the absence of a twisted one.

### `A30-0-ADMITS`

> At the frozen product configuration, for the ordered decomposition named, every pair of bijections
> of the single-carrier realizable class spaces is the class action of the factor families of a
> single transition family satisfying all eight prefix conjuncts and factorization as act 21 froze
> it, at evidence level 2. This is a statement about the exact declarations at the exact
> configuration. It does not say that any particular formula carries those conjuncts, does not
> disturb act 23's verdict about its own formula, and reports nothing about any other configuration
> or decomposition.

### `A30-0-RESTRICTS`

> At the frozen product configuration, for the ordered decomposition named, an exhibited pair of
> bijections of the single-carrier realizable class spaces is the class action of the factor
> families of no transition family satisfying all eight prefix conjuncts and factorization as act 21
> froze it, at evidence level 2. This is a statement about that exhibited pair, and it does not say
> that any other pair is restricted.

### `A30-0-UNDECIDED`

> Neither the universal nor a counterexample was obtained. The conjunct that is missing is named,
> with the step at which the proof stopped and what would settle it.

### The corollaries, REQUIRED

Each must be proved as a theorem and reported wherever its hypothesis is reached.

- **`A30-S-HOLD` and `A30-T-HOLD` give `A30-N-LIFTS`**, through route step 4.
- **`A30-N-LIFTS` gives `A30-0-ADMITS`**, through `a29_p_hold` applied to the same witness.
- **`A30-N-NO-LIFT` gives `A30-0-RESTRICTS`**: a family carrying all eight would be eligible and carry
  conjunct 8.

And the gate: **`A30-0-ADMITS` only with `A30-N-LIFTS`, `A30-0-RESTRICTS` only with
`A30-N-NO-LIFT`**, since `a29_p_hold` makes the eight conjuncts with factorization equivalent to
eligibility with conjunct 8.

### The outcome-vector table

The vector is `A30-S` · `A30-T` · `A30-N` · `A30-0`, and the result note carries **exactly one** of
these rows, verbatim.

| row | vector |
| --- | --- |
| 1 | `A30-S-HOLD` · `A30-T-HOLD` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 2 | `A30-S-HOLD` · `A30-T-FAILS` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 3 | `A30-S-HOLD` · `A30-T-FAILS` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 4 | `A30-S-HOLD` · `A30-T-FAILS` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 5 | `A30-S-HOLD` · `A30-T-UNDECIDED` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 6 | `A30-S-HOLD` · `A30-T-UNDECIDED` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 7 | `A30-S-HOLD` · `A30-T-UNDECIDED` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 8 | `A30-S-FAILS` · `A30-T-HOLD` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 9 | `A30-S-FAILS` · `A30-T-HOLD` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 10 | `A30-S-FAILS` · `A30-T-HOLD` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 11 | `A30-S-FAILS` · `A30-T-FAILS` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 12 | `A30-S-FAILS` · `A30-T-FAILS` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 13 | `A30-S-FAILS` · `A30-T-FAILS` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 14 | `A30-S-FAILS` · `A30-T-UNDECIDED` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 15 | `A30-S-FAILS` · `A30-T-UNDECIDED` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 16 | `A30-S-FAILS` · `A30-T-UNDECIDED` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 17 | `A30-S-UNDECIDED` · `A30-T-HOLD` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 18 | `A30-S-UNDECIDED` · `A30-T-HOLD` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 19 | `A30-S-UNDECIDED` · `A30-T-HOLD` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 20 | `A30-S-UNDECIDED` · `A30-T-FAILS` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 21 | `A30-S-UNDECIDED` · `A30-T-FAILS` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 22 | `A30-S-UNDECIDED` · `A30-T-FAILS` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |
| 23 | `A30-S-UNDECIDED` · `A30-T-UNDECIDED` · `A30-N-LIFTS` · `A30-0-ADMITS` |
| 24 | `A30-S-UNDECIDED` · `A30-T-UNDECIDED` · `A30-N-NO-LIFT` · `A30-0-RESTRICTS` |
| 25 | `A30-S-UNDECIDED` · `A30-T-UNDECIDED` · `A30-N-UNDECIDED` · `A30-0-UNDECIDED` |

Twenty-five rows: nine combinations of `A30-S` and `A30-T`, three `A30-N` labels each, less the two
rows the first corollary removes (`A30-S-HOLD` · `A30-T-HOLD` with `A30-N-NO-LIFT` or
`A30-N-UNDECIDED`), with `A30-0` fixed by `A30-N`.

***

## The `P0` row, per case

**On `A30-0-ADMITS`.** In the `P0` cell of `verification/ROADMAP.md`, act 28's sentence
"At the product configuration, whether factorization restricts which pair of local class bijections
can occur is undecided, with the obstruction named." and act 29's sentence "At the product
configuration, whether the ladder's conditions through factorization admit every pair of local class
bijections is undecided, with the conjunct that is missing named." are each removed together with
the standing clause that follows it, and in their place is written, once:

> At the product configuration, the ladder's conditions through factorization admit every pair of
> local class bijections: each such pair is the class action of the factor families of a single law
> carrying all of them, so those conditions do not select among local behaviours. `P0`'s threading
> part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the
> physical one, and nothing here names, endorses or excludes a selection principle.

The first sentence is act 29's frozen rows 1–3 sentence, verbatim.

**On `A30-0-RESTRICTS`.** The same two sentences with their standing clauses are replaced, once, by
act 29's frozen rows 4, 7 and 10 sentence, verbatim, followed by the standing clause.

**On `A30-0-UNDECIDED`.** The cell is not touched: both sentences stay true.

**The contracts this round supersedes, named in advance — on a decided `A30-0` only.** `R7-PFR`'s
and `R7-PRA`'s predicates on the `P0` cell pin those two sentences verbatim, with mutation controls
for their presence, placement and count. On a decided `A30-0`, exactly those two legs, with their
mutation controls, are replaced by `R7-PSL`'s contract on the corrected cell. **No other leg of
either contract is edited**, both checks stay in the guard and must pass, and the result note lists
the replaced legs by name. On `A30-0-UNDECIDED` no closed round's contract is touched.

***

## What no outcome licenses

- **No outcome licenses "factorization selects" or "factorization does not select."**
- **No outcome disturbs act 23's verdict about its own formula**, act 27's
  `a27_t_relabel_no_strict_lift`, or any verdict of acts 28 and 29, which stand as those rounds state
  them.
- **No outcome reports `A29-1`**, and no outcome is read as bearing on it.
- **No outcome reads the single-carrier classification into the product space.**
- **No outcome reports `L5-FREE`**, and none says a condition is empty, has no content, or fails to
  restrict; the assumption-watch note is a reading, recorded as one.
- **No outcome adopts a law, a carrier or a principle**, and none closes `P0`, which stays `OPEN`.
- **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
  evolution or a dynamics, and none is called canonical, unique or continuous.**

## Non-doings

This round does not: define anything; restate, weaken or strengthen any rung or declaration; read
any configuration but the one frozen; edit any closed round's record; edit any closed round's guard
contract beyond the two `P0` legs named above, and those only on a decided `A30-0`; write any
manuscript file; re-prove act 28's or act 29's results; ask `A29-1`.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no line beginning `def `, `abbrev `, `structure `, `class `,
`instance `, `axiom ` or `opaque `.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`.

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then linear commits from
`F`, each with one parent:

1. **Stage 1 — the module.** Adds `verification/lean-mathlib/OIBridge/ProductStrictLift.lean`
   carrying the shared lemmas only, and its import line in `verification/lean-mathlib/OIBridge.lean`.
   No verdict theorem.
2. **Stage 2 — `A30-S`.** The strictification theorem, named `a30_s_strictify` under `A30-S-HOLD`,
   `a30_s_fails` under `A30-S-FAILS`.
3. **Stage 3 — `A30-T`.** The transfer theorem, `a30_t_transfer` or `a30_t_fails`.
4. **Stage 4 — `A30-N` and `A30-0`**, each theorem with its corollary theorem where the hypothesis is
   reached: `a30_n_lifts` (or `a30_n_no_lift`) and `a30_0_admits` (or `a30_0_restricts`).
5. **Stage 5 — the surfaces.** The guard check `R7-PSL`, and on a decided `A30-0` the two replaced
   legs; the census family for `ProductStrictLift`, `kernel-only`; the `P0` cell per case.
6. **The result note** `result.md`, whose commit is `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40). The branch is pushed at each stage so the
pull-request run builds the module; a stage commit whose build fails is followed by a fixing commit,
never rewritten. Every label is read from the build at `E`.

### The guard check `R7-PSL`, and what it holds

Each clause mutation-tested:

- the module is imported by `OIBridge.lean`, carries no definition line, and prints `#print axioms`
  for every named result;
- **the verdict theorems of the labels earned**, and only those, exist, each at the exact
  configuration, with the declarations applied verbatim; each shape clause below for its own label:
  `A30-S-HOLD` — a universal over `Φ₀` with the two hypotheses, concluding `∃ Φ₁ Ψ` with the six
  conjuncts, `StrictNatural` among them; `A30-T-HOLD` — a universal implication between the two
  eligibility statements, each written out; `A30-N-LIFTS` — `∀` pair, `∃ Φ`, eligibility and conjunct 8
  in act 20's `TwistedNatural` form, never `StrictNatural`; `A30-N-NO-LIFT` — an exhibited pair, `∀ Φ`
  eligible, `¬` conjunct 8 with `Ψ`, `αL` and `αR` all universally quantified; `A30-0-ADMITS` — `∀`
  pair, **one** `∃ Φ` carrying the eight conjuncts written out, `FactorizesOnProduct` and the pair
  clause; `A30-0-RESTRICTS` — an exhibited pair and `∀ Φ` carrying the eight and factorization, `¬` the
  pair clause;
- the corollary theorems exist wherever their hypotheses are reached, and a note carrying a
  corollary's hypotheses without its conclusion fails;
- the census family for `ProductStrictLift` is `kernel-only` with no manuscript anchor;
- the result note carries the outcome vector as one of the twenty-five rows, each label with its
  frozen sentence verbatim, THE CLAUSE once, and the assumption-watch note;
- the `P0` cell is as this freeze prescribes for the case reached.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`, before any other stage |
| no definition is introduced | `C2`: no definition line in the module at any stage commit, locally; `R7-PSL` at `E` |
| every verdict is kernel-checked | `C8`: the dispatch run at `E` — the Lean kernel check and the `Mathlib bridge` build green |
| no named result depends on an axiom beyond the three | `C8`: the release gate's `lean-axioms` step at `E` |
| the frozen statement shapes hold of the theorems | `C8`: `R7-PSL` at `E` |
| the corollaries and gates hold | `C8`: `R7-PSL` at `E` |
| the census stays complete | `C8`: the release gate's `lean-manuscript` step at `E` |
| the rest of the guard is unchanged in verdict | `C8`: the guard at `E` reports `D`'s 91 checks all `PASS`, in `D`'s order, and `R7-PSL` `PASS` |
| the replaced legs are only the two named | `C7`: `git diff D E` on the guard changes nothing inside `R7-PFR` and `R7-PRA` beyond their `P0`-cell predicates and those predicates' mutation controls |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E` lists only governed paths, and no legacy record |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS`, `--receipts Q` holds on six receipts |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### Hazards and their mitigations, frozen

| hazard | mitigation |
| --- | --- |
| strict read as twisted, or its failure read as the twisted negative (1) | `A30-N`'s shape clause requires `TwistedNatural` in the positive and all three lift data universal in the negative; the `A30-N-UNDECIDED` sentence says it |
| a verdict resting on constant induced maps (2) | the positive route's induced maps are `id`, from `rnt1_strict_imp_twisted`; the note is recorded, not relied on |
| incompatible witnesses (3) | `A30-T` is a theorem; `A30-N` and `A30-0` are single existentials, checked by shape |
| single-carrier results used at the product carrier (4) | the route-authorization matrix forbids them as premises of `A30-S` |
| generalization (6) | verdicts are pinned to the exact configuration by `R7-PSL` |
| a stale `P0` surface (7) | the case rule above, with the superseded legs named in advance and `C7` checking nothing else moved |

### The status rule for the round

The labels are the measurements. If `C1` fails the round does not begin. If `C8` fails at `E` for a
cause in the round's paths, that is diagnosed; a Lean statement that does not build is corrected by a
further linear commit before `E` is designated, and a verdict that cannot be obtained is reported as
`UNDECIDED` with the step named, never as a halt. **A round that cannot reach a green `E`** halts under
the specification's `S12`, and records the discrepancy.
