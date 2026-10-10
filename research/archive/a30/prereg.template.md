# Track B act 30 — act 29's missing conjunct: product-carrier strictification, its transfer, the product-carrier lift, and full admission: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and the
round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

@@CLAUSE_BLOCK@@

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

The record directory holds this preregistration, the round's frozen controls `controls.py`, and
the result note. The receipt path is `verification/receipts/A30.json`. Every other path the round
changes is an execution path listed above, and nothing in the legacy-records population is among
them. `edge_rigidity_probe.py` and `ROADMAP.md` are governed for one purpose only: on a decided
`A30-0`, the `P0` cell is corrected and acts 28 and 29 cease to own its current status (below). On
`A30-0-UNDECIDED` neither file changes.

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
to `A30-N`, never its target, and `A30-N-NO-LIFT` is the negation of the **twisted** form, `¬ P_N`,
in which `Ψ`, `αL` and `αR` all sit under the negated existential.

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
prose; `P_N` and `P_0` are each a **single existential** whose one witness carries every conjunct
they claim.

**Hazard 4 — reading a single-carrier result into the product carrier.** Act 27's
`a27_0_strict_lift` and `a27_shared_torsor` are statements at carrier `Fin 4` with ancilla `Fin 1`.
Nothing in the record transports them to `Fin 4 × Fin 4` (act 29's RD1). This round **re-proves**
what it needs at the product configuration; it cites act 27 as provenance for the method and
consumes none of its results.

**Hazard 5 — a refuted universal read as a refuted existential.** `P_S` and `P_T` are universals;
`P_N` and `P_0` are existential in the law. One family without a lift refutes no existential, and act
23's `phiSC_corner` is the standing instance of an eligible family with none.

**Hazard 6 — theorem generalization.** The frozen propositions are stated at the exact product
configuration and nowhere else. A carrier-generic helper may appear in the execution as a shared
lemma, but **no verdict is stated of it** and no outcome reports anything at another carrier, ancilla
cardinality or visible family.

**Hazard 7 — a stale status surface, and who owns it.** Acts 28 and 29 each placed a frozen `P0`
sentence saying a question at the product configuration is **undecided**. A decided `A30-0` makes
each false, and `AGENTS.md` §A.27 requires the correction in place. Both sentences are pinned
verbatim by live-status legs of those rounds' guard contracts, `R7-PFR` and `R7-PRA`. The resolution
is **not** that act 30 teaches acts 28 and 29 the new answer: it is that **acts 28 and 29 cease to
own the current status of the `P0` cell**. On a decided `A30-0` exactly the live-`ROADMAP` legs of
those two contracts are retired, by the frozen splice ledger below, and every other byte of the
guard — their theorem pins, census and result-note checks, outcome-vector checks, and every
historical record of either act — is unchanged. Act 30 adds no guard clause (§A.39); its own
contracts are the frozen round-local `controls.py`.

***

## Provenance — what this freeze carries, and what is its own

Consumed as frozen declarations and frozen theorems, never re-proved and never paraphrased:

- **act 7**, `DilationChoice.lean` — `AdmissibleDilationAt`;
- **act 11**, `CoherentLiftGauge.lean` — `WeakAnchorStabilizer`, `weak_preserves_admissible`,
  `weak_anchor_coeff_norm_one`;
- **act 12**, `TwoSidedGauge.lean` — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
  `LeftFibreGroup`, `sh1_sufficiency`, `sh1_necessity`, `fibreGram_apply`, `fibreGram_left_mul`,
  `left_preserves_admissible`, `one_leftFibreGroup`, `fibreGram_mul_weak_apply`, `weak_mul`,
  `gramPhaseEquiv_of_twoSided`, `weak_diagonal_phase`, `twoSided_slice_iff`;
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

Its own: the four frozen propositions below, their proofs or refutations, the three corollary
theorems, the shared lemmas, and `controls.py`.

## Locating controls — the governing passages at `D`

| what | where at `D` | line |
| --- | --- | --- |
| `FibreGram` | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | 95 |
| `GramPhaseEquiv` | the same file | 102 |
| `RealizableGram` | the same file | 108 |
| `fibreGram_apply` | the same file | 115 |
| `sh1_necessity` | the same file | 168 |
| `fibreGram_left_mul`, `left_preserves_admissible`, `one_leftFibreGroup` | the same file | 207, 217, 226 |
| `fibreGram_mul_weak_apply`, `weak_mul`, `gramPhaseEquiv_of_twoSided` | the same file | 242, 252, 263 |
| `weak_diagonal_phase` | the same file | 723 |
| `twoSided_slice_iff` | the same file | 826 |
| `sh1_sufficiency` | the same file | 1070 |
| `AdmissibleDilationAt` | `verification/lean-mathlib/OIBridge/DilationChoice.lean` | 134 |
| `WeakAnchorStabilizer` | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | 114 |
| `weak_anchor_coeff_norm_one`, `weak_preserves_admissible` | the same file | 146, 273 |
| `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | 141, 146, 162 |
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
| act 29's frozen `P0` sentences, per case | `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | 692 |
| the `P0` cell | `verification/ROADMAP.md` | 63 |

The blobs at `D` of the files this round consumes or changes:

| file | blob |
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
| `verification/lean-mathlib/OIBridge.lean` | `b530b5b705a55b15e92eccfcab65d8e50a99ea0a` |
| `verification/lean/edge_rigidity_probe.py` | `@@GUARD_BLOB_D@@` |
| `verification/lean-manuscript-census.json` | `3b8b0747f0a4ca81fadecd8e9ffdfe69b57ef244` |
| `verification/ROADMAP.md` | `@@ROADMAP_BLOB_D@@` |

The names this round introduces were free at `D`, each returning nothing from `git grep -l` at `D`:
`ProductStrictLift`, `product-strict-lift`, `act-30`, `A30-`, `a30_`. The bare string `A30` occurs at
`D` only inside two binary PDF files.

***

## Why this round exists

Act 29 reached `A29-P-HOLD` · `A29-N-UNDECIDED` · `A29-0-UNDECIDED` · `A29-1-NOT-EXECUTED`. Its
`A29-P` is universal over every family carrying conjuncts 3 to 7, so conjuncts 1 and 2 hold of any
such family. What stopped admission is **conjunct 8**, for a pair of class bijections not induced by
carrier relabellings: act 28's construction supplies an eligible family for every pair, and nothing
in the record supplies a lift for it.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Read from the record at `D`; **no proof was executed**, and the execution is free to find any of it
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
   through a class-indexed choice of admissible dilations and `a27_shared_torsor`, which says the
   gauge action on an admissible dilation is free up to one common phase. The argument uses two
   facts of the configuration: the ancilla has one element, and the visible matrix has no zero entry.
   Both hold at the product configuration.
5. **The pairs act 29 reached** are the at most `24 × 24` pairs induced by `σ₁ × σ₂`; the realizable
   class space is not classified in the record.

***

## The configuration, FROZEN — act 29's, unchanged

`V = Fin 4 × Fin 4`, sixteen elements. `A = Fin 1 × Fin 1`, one element. `a₀ = ((0 : Fin 1), (0 : Fin 1))`.
`Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))` on `Fin 4`. The visible family is constant in time,
`Γ = fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, every entry `1/16`. The
ordered decomposition is `e = Equiv.refl (Fin 4 × Fin 4)`. **No other configuration is read, and no
verdict is stated of one.** Each frozen proposition binds `Γ₀` and `Γ` universally under exactly these
two equations, as act 29's theorems do.

In prose below, `R₁ G` abbreviates `RealizableGram (Fin 1) Γ₀ G` on `Fin 4`, `Rp G` abbreviates
`RealizableGram (Fin 1 × Fin 1) (Γ 0) G` on `Fin 4 × Fin 4`, and `X ⊠ Y` abbreviates
`fun i : Fin 4 × Fin 4 => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2`. The frozen propositions
write everything out and introduce no definition.

**The prefix** is act 29's eight conjuncts, in act 21's `LadderConds` order: (1) `ProperAt` and (2)
`PropagatesFrom` of the generated law `fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))`;
(3) `EvolvesTotally`; (4) `PreservesAdmissible`; (5) time homogeneity, `∃ Φh, ∀ t, Φ t = Φh`;
(6) `Reversible`, both conjuncts; (7) descent, `∀ t G G', GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')`;
(8) at every `t`, `∃ Ψ αL αR`, lifting `FibreGram a₀ (Ψ U) = Φ t (FibreGram a₀ U)` and admissibility
`AdmissibleDilationAt (Γ (t + 1)) a₀ (Ψ U)` for every `U` admissible at `Γ t`, and
`TwistedNatural a₀ αL αR Ψ`.

**A prescribed pair** is act 28's representation of a pair of bijections of the single-carrier
realizable class space: tuple maps `f₁`, `f₂` on `Fin 4` each preserving `R₁`, descending on
realizable tuples, injective on classes and surjective on classes — exactly the eight hypotheses
`a28_0_construction` carries, in its order. **The pair clause** for a family `Φ` is
`∀ t G₁ G₂, R₁ G₁ → R₁ G₂ → GramPhaseEquiv (Φ t (G₁ ⊠ G₂)) (f₁ G₁ ⊠ f₂ G₂)`: factorization with the
prescribed maps themselves as factor families. **An eligible family for the pair** carries conjuncts 3
to 7, `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`
and the pair clause.

***

## The frozen propositions — the exact Lean text

The four targets are four closed propositions, `P_S`, `P_T`, `P_N` and `P_0`, frozen here verbatim.
**A positive label is a theorem whose statement is the proposition; a negative label is a theorem
whose statement is its negation.** Nothing else earns a label.

### The module header, FROZEN

`verification/lean-mathlib/OIBridge/ProductStrictLift.lean` begins with exactly the line
`import OIBridge.ProductAdmission` and imports nothing else; its declarations sit in
`namespace OIBridge` / `namespace ProductStrictLift`; and it carries exactly one `open` command, before
its first theorem, verbatim:

```lean
@@OPEN@@```

Every frozen statement is elaborated under exactly this header. The module carries no `variable`,
`include`, `omit`, `attribute`, `notation`, `local`, `scoped`, `universe` or further `open` command,
no `open … in`, no definition of any kind, and no `sorry`, `admit` or `native_decide`.

### `P_S`

```lean
@@P_S@@
```

### `P_T`

```lean
@@P_T@@
```

### `P_N`

```lean
@@P_N@@
```

### `P_0`

```lean
@@P_0@@
```

### The theorems, FROZEN by name and statement form

Each is declared `theorem NAME :` with no binder before the colon, and its statement is the text
shown, compared after collapsing whitespace.

| label | theorem | statement |
| --- | --- | --- |
| `A30-S-HOLD` | `a30_s_strictify` | `P_S` |
| `A30-S-FAILS` | `a30_s_fails` | `¬ (P_S)` |
| `A30-T-HOLD` | `a30_t_transfer` | `P_T` |
| `A30-T-FAILS` | `a30_t_fails` | `¬ (P_T)` |
| `A30-N-LIFTS` | `a30_n_lifts` | `P_N` |
| `A30-N-NO-LIFT` | `a30_n_no_lift` | `¬ (P_N)` |
| `A30-0-ADMITS` | `a30_0_admits` | `P_0` |
| `A30-0-RESTRICTS` | `a30_0_restricts` | `¬ (P_0)` |
| corollary | `a30_c_lift` | `(P_S) → (P_T) → (P_N)` |
| corollary | `a30_c_admit` | `(P_N) → (P_0)` |
| corollary | `a30_c_restrict` | `(P_0) → (P_N)` |

Each `P_·` stands for the frozen text above, substituted in parentheses. A target with neither of its
two theorems is `UNDECIDED`; a target with both is a failure of the round. Every other theorem of
the module is named `a30_shared_…`. Every theorem is followed by its `#print axioms` line.

A negative theorem's proof instantiates the negated universal at an explicit counterexample, and the
result note names it: for `P_S` a map, for `P_T` a pair and two maps, and for `P_N` or `P_0` a pair.
That counterexample is what the frozen sentences call exhibited. A proof of `¬ P` that exhibits none
earns no label, and the target is reported `UNDECIDED` with the argument recorded.

### Pre-freeze elaboration — design evidence, not attestation

@@EVIDENCE@@

***

## The questions, FROZEN — four targets

### `A30-S` — product strictification

**Does every realizability-preserving, class-descending map at the product configuration have a
pointwise-equivalent replacement, equal to it off realizable tuples, with a strictly natural lift?**
The statement is `P_S`. The clause `∀ G, ¬ Rp G → Φ₁ G = Φ₀ G` is what lets descent, which conjunct 7
states for every tuple, transfer. Reported `A30-S-HOLD`, `A30-S-FAILS` or `A30-S-UNDECIDED`.

### `A30-T` — eligibility survives the replacement

**Does a pointwise-equivalent replacement, equal off realizable tuples, keep eligibility for the same
prescribed pair?** The statement is `P_T`, with every conjunct of eligibility written out on each
side. Reported `A30-T-HOLD`, `A30-T-FAILS` or `A30-T-UNDECIDED`; the result note names the conjunct
lost under `A30-T-FAILS`.

### `A30-N` — act 29's `A29-N`, at its original twisted strength

**For every prescribed pair, is there an eligible family carrying conjunct 8?** The statement is
`P_N`, conjunct 8 in act 20's existential twisted-lift form. **This is the proposition act 29 froze as
`A29-N`**, in the same shape, and its answer is the answer to that target. `A30-N-NO-LIFT` is
`¬ P_N`: classically, a pair for which every eligible family fails conjunct 8 for **every** `Ψ`, `αL`
and `αR`, not only the strict ones (hazard 1). Reported `A30-N-LIFTS`, `A30-N-NO-LIFT` or
`A30-N-UNDECIDED`.

### `A30-0` — act 29's `A29-0`, full admission in ONE existential

The statement is `P_0`: for every prescribed pair, **one** `Φ` carrying all eight conjuncts of the
prefix, each written out, `FactorizesOnProduct` at the frozen decomposition, and the pair clause.
**This is the proposition act 29 froze as `A29-0`.** A conjunction of separate existentials does not
discharge it. Reported `A30-0-ADMITS`, `A30-0-RESTRICTS` or `A30-0-UNDECIDED`.

### `A29-1` is not a target of this round

Act 29's gated fourth question stays closed here **whatever `A30-0` reaches**. If admission is
reached, `A29-1` is the question for the next round, at act 28's frozen pair, and this round writes
no statement about it.

### Separate verdicts

Each target's label stands on its own theorem. A label is voided by no other target's label; the
corollaries below govern which **combinations** may be reported.

***

## The assumption-watch note — constant induced maps

Recorded here and in the result note, **not repaired**, and not a target.

@@WATCH@@

***

## The controls

| role | object | what it is for | how consumed |
| --- | --- | --- | --- |
| countercontrol | act 23's `phiSC_corner` | an eligible family with no lift at any time, so no eligible family is assumed liftable; the positive route must replace the family | cited, not re-proved |
| countercontrol | act 27's `a27_t_relabel_no_strict_lift` | a given tuple formula can lack a strict lift while carrying a twisted one, so strict-lift failure of one formula is not read as anything about twisted lifts | cited, not re-proved |
| instance | act 29's `a29_n_relabel_instance` | the relabelling pairs already have eligible liftable families; a positive `A30-N` must reach the pairs that are not so induced | cited, not re-proved |
| positive | act 20's `rnt1_strict_imp_twisted` | the one bridge from the constructive route to the frozen form, used in the forward direction only | consumed |

The identity is not used as a control. The round's static contracts are in `controls.py`, below.

***

## The route, recorded as the freeze's reading and not as a finding

Hand reasoning, with no proof executed.

1. **Shared lemmas at the product configuration** (stage 1): the left and right gauge shapes for the
   one-element ancilla; closure of `LeftFibreGroup` under multiplication; admissibility at `Γ 0` is
   invariant under the left and right gauge; every entry of an admissible dilation at `Γ 0` is
   nonzero; two admissible dilations with equal fibre Gram differ by a left gauge element; and the
   torsor statement at `Fin 4 × Fin 4` — `D * U * K = D' * U * K'` iff `D' = u • D` and
   `K' = u⁻¹ • K` for one `u` of modulus one — following `a27_shared_torsor`'s proof. A
   carrier-generic form is permitted as a shared lemma (hazard 6).
2. **`P_S`** (stage 2), act 27's quotient-and-dilation route at the product carrier.
   - Let `R` be the tuples realizable at `Γ 0`, with the setoid `GramPhaseEquiv` and its quotient
     `Q`. For each class `ω` choose an admissible dilation `S ω` at `Γ 0` whose fibre Gram is
     `Quotient.out ω` (`sh1_sufficiency`).
   - `Φ₀` descends to a class map `f̄ : Q → Q`, well defined by the descent hypothesis and landing in
     `Q` by realizability preservation. For admissible `U`, `q U` is the class of `FibreGram a₀ U`.
   - Since `FibreGram a₀ U` and `FibreGram a₀ (S (q U))` are `GramPhaseEquiv`, `twoSided_slice_iff`
     decomposes `U = D * S (q U) * K` with `D` in `LeftFibreGroup` and `K` in
     `WeakAnchorStabilizer a₀`; one decomposition is chosen per `U`.
   - The lift transports the dilation: `Ψ U = D * S (f̄ (q U)) * K` for admissible `U`, and `Ψ U = U`
     otherwise. By the torsor lemma two decompositions of `U` differ by one common phase, which
     cancels, so `Ψ U` does not depend on the choice. `Ψ` preserves admissibility
     (`left_preserves_admissible`, `weak_preserves_admissible`) and is `StrictNatural`: a gauge
     element on either side leaves `q` unchanged (`fibreGram_left_mul`, `gramPhaseEquiv_of_twoSided`,
     `one_leftFibreGroup`) and is absorbed into the decomposition (the left-closure lemma, `weak_mul`).
   - **The replacement tuple is read off the transported dilation.** For realizable `G`, choose an
     admissible `U_G` with `FibreGram a₀ U_G = G` (`sh1_sufficiency`) and set
     `Φ₁ G = FibreGram a₀ (Ψ U_G)`. **Off realizable tuples, `Φ₁ G = Φ₀ G`**, where act 27 had the
     identity.
   - Then `Φ₁ G` lies in the class `f̄ [G]`, so `GramPhaseEquiv (Φ₁ G) (Φ₀ G)`; it is realizable
     (`sh1_necessity`); and the lifting equality holds for every admissible `U`, because `U` and
     `U_{FibreGram a₀ U}` have equal fibre Gram, so they differ by a left gauge element, which `Ψ`
     carries strictly and `FibreGram` absorbs (`fibreGram_left_mul`). The lifting clause is an
     equality, and it holds because `Φ₁` is defined from `Ψ` and not `Ψ` from `Φ₀`.
3. **`P_T`** (stage 3):
   - realizability of `Φ₁ G` from `realizable_of_gramPhaseEquiv`;
   - descent by cases, both inputs realizable or both not, since realizability is invariant under
     `GramPhaseEquiv`;
   - `EvolvesTotally`, both conjuncts of `Reversible`, `FactorizesOnProduct` with the same factor
     families, and the pair clause by transitivity of `GramPhaseEquiv`, with a case split on whether
     the product input is realizable (the two maps agree off realizable tuples);
   - time homogeneity because both families are constant.
4. **`a30_c_lift` and `P_N`** (stage 4):
   - For a prescribed pair, act 28's `a28_0_construction` gives an eligible family `Φ` with
     `Φ t = Φh` for every `t`.
   - `P_S` at `Φh` gives `Φ₁` and `Ψ`. Its hypotheses are `PreservesAdmissible` at `t = 0` with
     `Γ 1 = Γ 0`, and descent restricted to realizable tuples.
   - `P_T` gives eligibility of `fun _ => Φ₁`.
   - Conjunct 8 holds at every `t` with that `Ψ` and `αL = αR = id`. The lifting and admissibility
     clauses come from `P_S`, since `Γ (t + 1) = Γ t`. Twisted naturality comes from
     `rnt1_strict_imp_twisted`.
   - `a30_n_lifts` is `a30_c_lift` applied to `a30_s_strictify` and `a30_t_transfer`.
5. **`a30_c_admit`, `a30_c_restrict` and `P_0`** (stage 4):
   - `a30_c_admit` is `a29_p_hold` applied to `P_N`'s own witness, which gives conjuncts 1 and 2 of
     that one family.
   - `a30_c_restrict` is the projection from the eight conjuncts, factorization and the pair clause
     to eligibility and conjunct 8.
   - So `P_N ↔ P_0`, and `A30-0` is fixed by `A30-N`.

### The route-authorization matrix, FROZEN

Authorized for every target without further mention: act 12's `sh1_sufficiency`, `sh1_necessity`,
`fibreGram_apply`, `fibreGram_left_mul`, `left_preserves_admissible`, `one_leftFibreGroup`,
`fibreGram_mul_weak_apply`, `weak_mul`, `gramPhaseEquiv_of_twoSided`, `weak_diagonal_phase` and
`twoSided_slice_iff`; act 11's `weak_preserves_admissible` and `weak_anchor_coeff_norm_one`; act 17's
`gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`; act 21's
`realizable_of_gramPhaseEquiv`; Mathlib; and this round's own shared lemmas. **A helper needed but
absent from this list is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may consume | may NOT consume | permitted work |
| --- | --- | --- | --- |
| `P_S`'s | the authorized helpers; act 20's and act 12's declarations | `a28_0_construction`; `a29_p_hold`; any act 27 result | prove or refute the strictification at the product configuration |
| `P_T`'s | the authorized helpers; act 21's declarations | `P_S`'s theorem; `a29_p_hold` | prove or refute the transfer |
| `a30_c_lift` | its two hypotheses; `a28_0_construction`; `rnt1_strict_imp_twisted`; the authorized helpers | `a29_p_hold` | derive `P_N` from `P_S` and `P_T` |
| `P_N`'s | `a30_c_lift` with `P_S`'s and `P_T`'s theorems; or, for `¬ P_N`, the authorized helpers and act 20's declarations | `a29_p_hold` as a premise for the lift | the positive by the corollary, or the universal negative |
| `a30_c_admit`, `a30_c_restrict` | their hypotheses; `a29_p_hold`; the authorized helpers | act 22's and act 23's verdicts as premises | the two assembly implications |
| `P_0`'s | `a30_c_admit` or `a30_c_restrict` with `P_N`'s theorem | anything else | the label from `A30-N`'s |

***

## The preregistered predictions

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A30-S` | `A30-S-HOLD` | **high** | the construction is `a27_0_strict_lift`'s at a carrier where both facts it uses hold; the new work is the product-carrier shape and torsor lemmas |
| `A30-T` | `A30-T-HOLD` | **high** | every conjunct of eligibility is stated up to `GramPhaseEquiv` or is realizability, which that relation preserves, except descent, which the off-realizable equality clause carries |
| `A30-N` | `A30-N-LIFTS` | **high** | `a30_c_lift` with the two above |
| `A30-0` | `A30-0-ADMITS` | **high** | `a30_c_admit` with `A30-N-LIFTS` |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed, with
the measurement that settled it.

***

## The outcomes per target, each with its FROZEN post-round sentence

@@SENTENCES_SECTION@@
### The corollaries, REQUIRED

- **`a30_c_admit` and `a30_c_restrict` are required in every case.** Together they make `P_N` and
  `P_0` equivalent, so `A30-0-ADMITS` is reported exactly with `A30-N-LIFTS`, `A30-0-RESTRICTS` exactly
  with `A30-N-NO-LIFT`, and `A30-0-UNDECIDED` exactly with `A30-N-UNDECIDED`.
- **`a30_c_lift` is required wherever `A30-S-HOLD` and `A30-T-HOLD` are both reached**, and then
  `A30-N-LIFTS` is reached through it. It is permitted in every other case.

@@TABLE_SECTION@@
***

## The `P0` row, per case

**On `A30-0-ADMITS`.** In the `P0` cell of `verification/ROADMAP.md`, act 28's sentence
"@@P0_PFR@@" and act 29's sentence "@@P0_PRA@@" are each removed together with the standing clause
that follows it, and in their place is written, once:

> @@P0_ADMITS@@ @@P0_STANDING@@

The first sentence is act 29's frozen rows 1–3 sentence, verbatim.

**On `A30-0-RESTRICTS`.** The same two sentences with their standing clauses are replaced, once, by
act 29's frozen rows 4, 7 and 10 sentence, verbatim, with the standing clause:

> @@P0_RESTRICTS@@ @@P0_STANDING@@

**On `A30-0-UNDECIDED`.** The cell is not touched: both sentences stay true.

The expected `ROADMAP.md` at `E` is `D`'s with that one replacement, or `D`'s unchanged, byte for byte;
`controls.py` rebuilds it from `D`. Rehearsed at `D`, the two decided cells give `ROADMAP.md` blobs
`@@ROADMAP_BLOB_ADMITS@@` (`A30-0-ADMITS`) and `@@ROADMAP_BLOB_RESTRICTS@@` (`A30-0-RESTRICTS`).

## Acts 28 and 29 cease to own the `P0` cell — the frozen retirement, on a decided `A30-0` only

**What is retired.** The authority of `R7-PFR` and `R7-PRA` over the **current** status of the `P0`
cell: the `ROADMAP` constants, the `P0`-cell reader `_pfr_p0_cell` (read by those two legs and
nothing else), each round's `ROADMAP` read and gating predicate, their `roadmap` check entries with
their `road-mut` mutation controls, `R7-PRA`'s `road-successor-tolerated` positive control, and the
phrases of the two check descriptions that say the `ROADMAP` cell is read. **Reachability and
physical presence are retired together**: every retired line is deleted, and nothing is deleted that
the ledger below does not name — no deletion is inferred from dead code.

**What is kept byte-identical.** Every other byte of the guard: both checks stay, under their tags, in
their places, and must pass; their theorem pins, zero-definition and import checks, census checks
with every census mutation, result-note and outcome-vector checks, and every historical record of acts
28 and 29. Act 27's `R7-NLV`, which pins act 27's own `P0` sentence, is untouched: that sentence
concerns the single carrier and stays true.

**The ledger, FROZEN.** Each entry is an exact splice of the guard at `D`: its old text occurs there
exactly once, and it is replaced by the new text. The full old and new texts are carried in
`controls.py` and reproduced by it; their SHA-256 digests are frozen here.

@@LEDGER_TABLE@@

Applied in order to the guard at `D` (blob `@@GUARD_BLOB_D@@`), the ledger gives the retired guard,
blob **`@@GUARD_BLOB_RETIRED@@`**, 121 lines shorter, compiling. On a decided `A30-0` the guard at `E`
is exactly that blob; on `A30-0-UNDECIDED` it is exactly `D`'s. The result note lists the retired
legs by their ledger names.

**Rehearsed at `D`, locally** (design evidence, not attestation; the dispatch runs are recorded
above):

| guard | `ROADMAP.md` | verdict |
| --- | --- | --- |
| retired | `A30-0-ADMITS` cell | 91 PASS, 0 FAIL, the tags in `D`'s order; `R7-PFR` 57 contracts, `R7-PRA` 72 |
| retired | `A30-0-RESTRICTS` cell | 91 PASS, 0 FAIL, the tags in `D`'s order |
| retired | `D`'s cell | 91 PASS, 0 FAIL, the tags in `D`'s order |
| `D`'s | `A30-0-ADMITS` cell | 89 PASS, 2 FAIL: `R7-PFR` (`roadmap`) and `R7-PRA` (`roadmap`, `road-successor-tolerated`) |
| `D`'s | `A30-0-RESTRICTS` cell | the same two failures |

The last two rows are the countercontrol: they show that a corrected cell cannot land under `D`'s
guard, and that the legs the ledger retires are exactly the legs that fail.

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

This round does not:
- define anything;
- restate, weaken or strengthen any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- add a guard clause, or edit any closed round's guard contract beyond the frozen ledger — and that
  only on a decided `A30-0`;
- write any manuscript file;
- re-prove act 28's or act 29's results;
- ask `A29-1`.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-30-product-strict-lift/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, written before `F` and added by the execution with exactly this blob. It
imports nothing from the repository and changes nothing. It reads `D` and the commit under check
through `git`, and it embeds every frozen text it compares against:
- the four propositions;
- the header;
- the label and corollary theorem names and statement forms;
- the twenty-five rows;
- the twelve sentences;
- the clause;
- the assumption-watch note;
- the `P0` texts;
- the retirement ledger in full;
- the blobs above.

`controls.py check <commit>` reads the module's labels off its theorems and fails unless:

- **the module** begins with the frozen import and carries the one frozen `open`, no forbidden command
  or token, a `#print axioms` line for every theorem and none for a non-theorem, only the frozen
  theorem names or `a30_shared_…`, each label and corollary theorem with its frozen statement, at most
  one label per target, `a30_c_admit` and `a30_c_restrict`, and `a30_c_lift` where `A30-S-HOLD` and
  `A30-T-HOLD` are both earned;
- **the vector** so read is one of the twenty-five rows;
- **the result note** carries that row exactly once and no other complete vector, each earned label's
  frozen sentence exactly once and no unearned label's, THE CLAUSE's mention exactly once with the
  complete clause following it, the assumption-watch note, and — on a decided `A30-0` — every ledger
  entry by name;
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen replacement for the case, or to `D`'s;
- **the guard** is byte-identical to the ledger applied to `D`'s, or to `D`'s, for the case, and the
  ledger applied to `D`'s guard reproduces blob `@@GUARD_BLOB_RETIRED@@`;
- **the census** is `D`'s with exactly one family appended, last, for module `ProductStrictLift`,
  `kernel-only`, no manuscript anchor, its note carrying the bare vector once;
- **`OIBridge.lean`** is `D`'s with `import OIBridge.ProductStrictLift` inserted directly after
  `import OIBridge.ProductAdmission`;
- **the paths** changed from `D` are exactly: the three record files and the module (added);
  `OIBridge.lean` and the census (modified); and, on a decided `A30-0` only, the guard and
  `ROADMAP.md` (modified).

`controls.py --self-test` also checks the constants above against this preregistration, beside it. It
then builds a synthetic execution for each of the twenty-five rows and requires every one to hold.
Finally it applies @@N_MUTATIONS@@ mutation controls, each of which must fail with its named code:
- a definition, a `variable`, an `include`, a second or altered `open`, `open … in`, a second import
  or a `sorry`;
- a dropped `#print axioms`;
- a stray theorem name;
- `StrictNatural` put for `TwistedNatural` in `P_N`;
- a second existential in `P_0`;
- `P_S`'s off-realizable clause dropped;
- a binder added before a colon;
- the configuration changed;
- a negative label not negated;
- both labels of one target;
- each required corollary missing;
- a corollary altered;
- the two gate violations;
- in the result note: a vector mismatch, a second vector, an altered sentence, an unearned sentence,
  the clause twice, the mention twice, the clause detached or truncated, the assumption-watch note
  dropped, or a leg unlisted;
- in `ROADMAP.md`: a stale sentence kept, the wrong case, the standing clause dropped, or the cell
  touched when undecided;
- in the guard: one byte, the guard left untouched when decided, the guard retired when undecided,
  or one leg restored;
- in the census: a promoted status, another entry changed, a wrong vector, or the entry absent;
- in the wiring: the import absent or misplaced;
- in the paths: an extra path or a missing note;
- a tampered ledger entry.

Run at `D` beside this file, the self-test prints:

@@SELFTEST@@

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then linear commits from
`F`, each with one parent:

1. **Stage 1 — the module and the controls.** Adds `controls.py` with its frozen blob; adds
   `verification/lean-mathlib/OIBridge/ProductStrictLift.lean` carrying the frozen header and the
   shared lemmas only, each with its `#print axioms`; and adds its import line to
   `verification/lean-mathlib/OIBridge.lean`. No label or corollary theorem.
2. **Stage 2 — `P_S`.** `a30_s_strictify` or `a30_s_fails`, or neither.
3. **Stage 3 — `P_T`.** `a30_t_transfer` or `a30_t_fails`, or neither.
4. **Stage 4 — `P_N` and `P_0`.** `a30_c_admit` and `a30_c_restrict`; `a30_c_lift` where required;
   then `a30_n_lifts` or `a30_n_no_lift` or neither, and `a30_0_admits` or `a30_0_restricts` to match.
5. **Stage 5 — the surfaces.** The census family for `ProductStrictLift`, `kernel-only`, appended last;
   and, on a decided `A30-0` only, the `P0` cell for the case and the guard as the ledger gives it.
6. **The result note** `result.md`, whose commit is `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40). The branch is pushed at each stage so the
pull-request run builds the module; a stage whose build fails is followed by a fixing commit, never
rewritten. Every label is read from the module at `E`.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F`, before any other stage |
| the round's controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E` is `@@CONTROLS_BLOB@@`; `controls.py --self-test` prints `controls: self-test OK` at `E` |
| no definition is introduced, the header is the frozen one | `C2`: `controls.py check` on each stage commit, locally, for its module checks; `C9` at `E` |
| every frozen proposition elaborates as frozen | before `F`: the elaboration run above; at `E`: `C8`, since each label and corollary theorem is compiled under its frozen statement |
| every verdict is kernel-checked | `C8`: the dispatch run at `E` — the Lean kernel check and the `Mathlib bridge` build green |
| no named result depends on an axiom beyond the three | `C8`: the release gate's `lean-axioms` step at `E` |
| the frozen statement shapes, the vector, the corollaries and gates hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the census stays complete | `C8`: the release gate's `lean-manuscript` step at `E`; `C9` for the appended family |
| the surfaces are exactly the frozen ones for the case | `C9`: `ROADMAP.md`, the guard, the census and `OIBridge.lean` rebuilt from `D` and compared byte for byte |
| the rest of the guard is unchanged in verdict | `C8`: the guard at `E` reports 91 checks, all `PASS`, in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E` is the frozen set for the case, and no legacy record; `C9` checks the same set |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS`, `--receipts Q` holds on six receipts |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### Hazards and their mitigations, frozen

| hazard | mitigation |
| --- | --- |
| strict read as twisted, or its failure read as the twisted negative (1) | `P_N` carries `TwistedNatural` under `∃ Ψ αL αR`, and `A30-N-NO-LIFT` is `¬ P_N`, both checked verbatim by `controls.py` |
| a verdict resting on constant induced maps (2) | the positive route's induced maps are `id`, from `rnt1_strict_imp_twisted`; the note is recorded, not relied on |
| incompatible witnesses (3) | `P_T` is a theorem; `P_N` and `P_0` are single existentials, checked verbatim |
| single-carrier results used at the product carrier (4) | the route-authorization matrix forbids act 27's results for `P_S`'s theorem |
| generalization (6) | the frozen propositions are stated at the exact configuration, checked verbatim |
| a stale `P0` surface, or a closed round's contract edited beyond need (7) | the case rule, the frozen ledger, and `controls.py`'s byte comparison of the guard and `ROADMAP.md` against `D` |
| a frozen proposition that does not typecheck | the pre-freeze elaboration run and its countercontrol, above |

### The status rule for the round

The labels are the measurements, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen proposition unchanged** is repairable. That covers
  a proof that does not build, a shared lemma that is false as first stated and is restated, a tactic
  failure, or a stage that fails its checks. It is repaired by later linear commits before `E` is
  designated, never by rewriting a commit.
- **A verdict that cannot be obtained** is reported `UNDECIDED`, with the step named. That is a
  measurement, not a failure.
- **A freeze failure** is not `UNDECIDED` mathematics, and it cannot be repaired after `F` by changing
  the target. It is any of:
  - a frozen proposition that is ill-typed;
  - a frozen proposition that cannot be stated as frozen under the frozen header, so that elaborating
    it needs any change to its text, to the header or to the configuration;
  - a required corollary that is false as frozen.

  The round then halts under the specification's `S12`: the withdrawal commit `W` when execution
  commits exist, or the record-only child of `F` when none do, with the result note naming the
  proposition and the elaboration error. A successor round re-freezes.
- **A round that cannot otherwise reach a green `E`** also halts under `S12` and records the
  discrepancy.
