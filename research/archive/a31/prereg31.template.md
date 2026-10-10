# Track B act 31 — off-locus uniqueness after full product admission: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull
request from `D`, the control plane drafted on it, execution after the owner designates `F`, and the
round's protocol record a receipt on which `tools/v3_verifier.py --verify-round` must print
`VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
@@CLAUSE_Q@@

## The declarations

```v3-round
round A31
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/
record AM verification/receipts/A31.json
execution A verification/lean-mathlib/OIBridge/ProductOffLocusUniqueness.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/A31.json`. Every other path the round changes
is an execution path listed above. The guard is not governed and does not change; `ROADMAP.md`
changes only on a decided outcome.

## The objects

- **`D`** = `@@D@@`, act 30's receipt commit `Q`, the head of `main` after act 30's landing,
  certified by push run 36230402641: all three jobs green, the guard 91 PASS and 0 FAIL, the release
  gate 21 of 21 with `v3-receipts` holding on six receipts. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A31.json`.

A31 runs beside act 32. It reads no object, result, receipt or control plane of act 32, and a later
movement of `main` enters it only by reconciliation after `E`.

***

## The hazards, stated before anything else

**Hazard 1 — properness is not disagreement.** Act 28's `a28_s_proper` says the off-locus
realizable class space is nonempty. That fixes nothing about the values of any law there, and it is
consumed as provenance only.

**Hazard 2 — an opaque witness.** `a28_s_proper` packs its witness under `∃ G`; its entries cannot be
computed after it is obtained. A disagreement needs two **explicit** off-locus classes, so this round
re-derives them, as the frozen statement `S_W` requires.

**Hazard 3 — hidden values.** That act 28's construction fixes every class without a product
representative is true only inside its proof, and the families of act 30 are existential. No step of
this round may rest on the off-locus values of a law it did not construct.

**Hazard 4 — descent on every tuple.** Conjunct 7 quantifies over **all** tuples, realizable or not.
A modification of a law must descend everywhere, and `S_TAU` requires it of the transposition.

**Hazard 5 — incompatible witnesses.** Conjunct 8 of the second law comes from act 30's
strictification of the precomposed family. Conjuncts 1 and 2 must then be proved of **that final
family**, through `a29_p_hold`, and not of the family before strictification.

**Hazard 6 — the time index.** Both verdicts compare the two laws at time `0`. That makes them exact
complements; a verdict at every time would not be the negation of a verdict at some time.

**Hazard 7 — vocabulary.** Act 29 called a family carrying conjuncts 3 to 7, factorization and the
pair clause *eligible*. A family carrying all eight conjuncts, factorization and the pair clause is
here a **fully admitted law**, and the two terms are not interchanged.

**Hazard 8 — generalization.** Every frozen statement is at the exact product configuration and the
exact pair. No outcome reports anything at another pair, another configuration, or another time.

***

## Provenance

Consumed as frozen declarations and frozen theorems, never re-proved and never paraphrased:

- **acts 11, 12, 17 and 18** — `WeakAnchorStabilizer`, `FibreGram`, `GramPhaseEquiv`,
  `RealizableGram`, `sh1_necessity`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`,
  `gramPhaseEquiv_trans`, `ProperAt`, `PropagatesFrom`;
- **act 20**, `RepresentativeNaturality.lean` — `TwistedNatural`, `StrictNatural`,
  `RelabelTransition`, `rnt1_strict_imp_twisted`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `EvolvesTotally`, `PreservesAdmissible`, `Reversible`,
  `FactorizesOnProduct`, `realizable_of_gramPhaseEquiv`, `realizable_relabel`,
  `relabel_gramPhaseEquiv`, `relabel_relabel_symm`, `relabel_symm_relabel`,
  `gramPhaseEquiv_of_relabel`, `witness_supply`, `relabel_product`, `relabel_one`,
  `product_realizable`;
- **act 27**, `StrictNaturalLift.lean` — `a27_shared_fibreGram_entry`;
- **act 28**, `ProductLocusFreedom.lean` — `a28_s_locus_first_index`, `a28_shared_product_realizable`;
  `a28_s_proper`, provenance only (hazard 1);
- **act 29**, `ProductAdmission.lean` — `a29_p_hold`, `a29_n_relabel_instance`;
- **act 30**, `ProductStrictLift.lean` — `a30_s_strictify`, `a30_t_transfer`, `a30_0_admits`.

The pair is act 28's, stated there in prose and pinned here as Lean equations:
`f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3)` and `f₂ = fun G => G` (act 28's preregistration,
lines 295–298; act 29's, lines 378–380). The two alternatives are act 29's frozen `A29-1`, taken at
time zero (hazard 6).

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| act 28's locus clause, in `a28_s_proper` | `verification/lean-mathlib/OIBridge/ProductLocusFreedom.lean` | 207 |
| `a28_s_locus_first_index` | the same file | 178 |
| `a28_shared_product_realizable` | the same file | 304 |
| `a29_p_hold`, `a29_n_relabel_instance` | `verification/lean-mathlib/OIBridge/ProductAdmission.lean` | 168, 211 |
| `a30_s_strictify`, `a30_t_transfer`, `a30_0_admits` | `verification/lean-mathlib/OIBridge/ProductStrictLift.lean` | 449, 479, 904 |
| `RelabelTransition`, `rnt1_strict_imp_twisted` | `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | 167, 192 |
| `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_relabel_symm`, `relabel_symm_relabel`, `gramPhaseEquiv_of_relabel` | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | 388, 397, 405, 412, 420 |
| `witness_supply`, `relabel_product`, `relabel_one`, `product_realizable` | the same file | 431, 975, 986, 1015 |
| `a27_shared_fibreGram_entry` | `verification/lean-mathlib/OIBridge/StrictNaturalLift.lean` | 20 |
| act 29's frozen `A29-1` sentences and `P0` rows | `verification/programmes/oi-qm/track-b/act-29-product-admission/preregistration.md` | 692 |

| file at `D` | blob |
| --- | --- |
| `ProductLocusFreedom.lean` | `325c09a180366765ae4d742b752099d3b219d3c9` |
| `ProductAdmission.lean` | `90533c832477ad25e8725f20b7759ac71149c251` |
| `ProductStrictLift.lean` | `902581e3f33aade4c3366276046a03157248d237` |
| `OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `StrictNaturalLift.lean` | `038f8e77de14f45790fddba69a4a659522d5fa81` |
| `verification/lean-mathlib/OIBridge.lean` | `7a6aaa6cd4011d03932a0c65fe622e6fc521b2c8` |
| `verification/lean-manuscript-census.json` | `97436abcb04df23a821a33e5bba463122647378e` |
| `verification/ROADMAP.md` | `@@ROADMAP_BLOB_D@@` |
| `verification/lean/edge_rigidity_probe.py` | `@@GUARD_BLOB_D@@` |

The names this round introduces — `ProductOffLocusUniqueness`, `act-31`, `A31-`, `a31_` — return
nothing from `git grep -l` at `D`.

***

## Why this round exists

Act 29 froze `A29-1` at act 28's pair and gated it on `A29-0-ADMITS`, which act 29 did not reach.
Act 30 reached `A30-0-ADMITS`: at the product configuration every pair of local class bijections is
the class action of the factor families of a single fully admitted law. The gate is open, and the
residual question is whether two fully admitted laws for the same pair can differ away from the
product inputs.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Read from the record at `D`; no proof was executed.

1. **Any fully admitted law permutes the off-locus classes.** The pair clause and the class bijection
   `f★₁ × f★₂` carry locus classes onto locus classes, and conjunct 6 makes the law a bijection on
   realizable classes.
2. **Right precomposition keeps admission.** A transposition `τ` of two off-locus classes, fixing
   every locus tuple and descending on every tuple, leaves conjuncts 3 to 7, factorization and the pair
   clause of `G ↦ Φ t (τ G)` intact. Act 30 then restores conjunct 8 by strictification, and act 29's
   universal `a29_p_hold` gives conjuncts 1 and 2 of the resulting family.
3. **Two off-locus classes exist explicitly.** `W` is act 28's witness, act 21's product
   `G(H₁) ⊠ G(Hᵢ)` relabelled by the transposition of `(0, 1)` and `(1, 0)`. `W₂` is the same with
   `G(Hᵢ)` relabelled by `(2 3)` first. Both are off-locus, with the entries `1/16` and `I/16` that act
   28 reads at fibres `(0, 1)` and `(1, 1)`. They are inequivalent: at fibres `(0, 0)` and `(0, 2)`,
   matrix indices `(0, 0)` and `(0, 2)`, the entries of `W` are `1/16` and `1/16` and those of `W₂` are
   `1/16` and `I/16`. These values were computed in exact Gaussian-integer arithmetic before the
   freeze and are what `S_W` requires the kernel to establish.

So at this pair, uniqueness holds exactly when the off-locus class space has one element, and the
freeze's reading is that it has at least two.

***

## The configuration, FROZEN — act 30's, unchanged

`V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = ((0 : Fin 1), (0 : Fin 1))`,
`Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`, the constant product visible family
`Γ = fun _ => Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, and the ordered decomposition
`Equiv.refl (Fin 4 × Fin 4)`, each bound in every frozen proposition exactly as act 30 binds it.

**A fully admitted law for the pair** is a transition family carrying act 30's `P_0` body: all eight
prefix conjuncts in act 21's order, each written out, `FactorizesOnProduct` at the frozen decomposition,
and the pair clause. **A tuple off the product locus** is a tuple `G` with act 28's clause
`∀ X Y, R₁ X → R₁ Y → ¬ GramPhaseEquiv (X ⊠ Y) G`, written out.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

`verification/lean-mathlib/OIBridge/ProductOffLocusUniqueness.lean` begins with exactly the line
`import OIBridge.ProductStrictLift` and imports nothing else; its declarations sit in
`namespace OIBridge` / `namespace ProductOffLocusUniqueness`; and it carries exactly one `open`
command, before its first theorem, verbatim:

```lean
@@OPEN@@```

The module carries no `variable`, `include`, `omit`, `attribute`, `notation`, `local`, `scoped`,
`universe` or further `open` command, no `open … in`, no definition of any kind, and no `sorry`,
`admit` or `native_decide`.

### `P_N` — two fully admitted laws disagree at time zero off the locus

```lean
@@P_N@@
```

### `P_U` — every two fully admitted laws agree at time zero off the locus

```lean
@@P_U@@
```

**The two are duals by construction.** Both are built from one head, one admission body `A` for `Φ`
(with `A'` its copy for `Φ'`), one realizability clause `R`, one off-locus clause `O`, and one time-zero
comparison `E`: `P_N` is `∃ Φ Φ', A ∧ A' ∧ ∃ G, R ∧ O ∧ ¬ E` and `P_U` is
`∀ Φ Φ', A → A' → ∀ G, R → O → E`. `controls.py` rebuilds both from those components and checks the
frozen texts against them, so `P_N ↔ ¬ P_U` holds by the shape of the statements.

### The statements required under `A31-1-NONUNIQUE`

The kernel must establish the explicit witnesses, the transposition and the precomposition as
separate theorems, each with the statement frozen here, before `a31_nonunique` consumes them.

`S_W` — `W` and `W₂` are realizable, off the locus, and inequivalent:

```lean
@@S_W@@
```

`S_TAU` — a transposition of any two such classes exists that preserves realizability, descends on
every tuple, is an involution up to `GramPhaseEquiv`, fixes every tuple of the product locus, and
carries the first class to the second:

```lean
@@S_TAU@@
```

`S_PRE` — precomposition by such a transposition keeps conjuncts 3 to 7, factorization and the pair
clause, the family being `fun t G => Φ t (τ G)`:

```lean
@@S_PRE@@
```

### The theorems, FROZEN by name and statement form

Each is declared `theorem NAME :` with no binder before the colon; statements are compared after
collapsing whitespace.

| role | theorem | statement |
| --- | --- | --- |
| `A31-1-NONUNIQUE` | `a31_nonunique` | `P_N` |
| `A31-1-UNIQUE` | `a31_unique` | `P_U` |
| corollary, required in every case | `a31_c_exclusive` | `(P_N) → ¬ (P_U)` |
| required under `A31-1-NONUNIQUE` | `a31_shared_witnesses` | `S_W` |
| required under `A31-1-NONUNIQUE` | `a31_shared_transposition` | `S_TAU` |
| required under `A31-1-NONUNIQUE` | `a31_shared_precompose` | `S_PRE` |

A module with neither verdict theorem reports `A31-1-UNDECIDED`; a module with both is a failure of
the round. Every other theorem is named `a31_shared_…`. Every theorem is followed by its
`#print axioms` line. A consequence the construction proves beyond the verdict — for instance that
every fully admitted law has a second one disagreeing with it off the locus — may be recorded as an
`a31_shared_…` theorem; no label is stated of it.

### Pre-freeze elaboration — design evidence, not attestation

@@EVIDENCE@@

***

## The question, FROZEN — one target

### `A31-1` — off-locus uniqueness at the fixed pair

**For act 28's pair, do two fully admitted laws always agree at time zero, up to `GramPhaseEquiv`, on
every realizable tuple off the product locus?** Reported `A31-1-NONUNIQUE` (the theorem `P_N`),
`A31-1-UNIQUE` (the theorem `P_U`) or `A31-1-UNDECIDED`. Under `A31-1-NONUNIQUE` the result note names
the two laws and the tuple the proof exhibits.

***

## The controls

| role | object | what it is for | how consumed |
| --- | --- | --- | --- |
| provenance | act 28's `a28_s_proper` | the off-locus class space is nonempty; it is not the disagreement point | cited, not consumed by the verdict |
| instance | act 29's `a29_n_relabel_instance` | a fully admitted law for the pair exists before this round: the relabelling family of `(2 3) × 1` | consumed as the base law of the route |
| duality | `a31_c_exclusive` and `controls.py` | the two verdicts cannot both be earned | proved; checked by shape |

***

## The route, recorded as the freeze's reading and not as a finding

1. **The base law.** `Φa := fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) 1)`
   is fully admitted for the pair: `a29_n_relabel_instance` with `σ₁ = (2 3)` and `σ₂ = 1` gives
   conjuncts 3 to 8, factorization and the product equation; `relabel_one` turns the second factor
   into the identity, giving the pair clause; `a29_p_hold` gives conjuncts 1 and 2.
2. **`S_W`.** The realizability of `W` and `W₂` by `product_realizable`, `sh1_necessity` and
   `realizable_relabel`; their off-locus clauses by `a28_s_locus_first_index` read at fibres `(0, 1)`
   and `(1, 1)` with matrix indices `(2, 0)` and `(2, 1)`, as act 28 reads it; their inequivalence at
   fibres `(0, 0)` and `(0, 2)` with matrix indices `(0, 0)` and `(0, 2)`, one common phase function
   being forced to carry `1/16` to `1/16` and `1/16` to `I/16`. Entries by
   `a27_shared_fibreGram_entry` from `witness_supply`'s explicit matrices.
3. **`S_TAU`.** Under `classical`, `τ G := if G ≈ W then W₂ else if G ≈ W₂ then W else G`, each
   property by cases with `gramPhaseEquiv_refl`, `symm` and `trans`. A locus tuple is equivalent to
   neither `W` nor `W₂`, since each is off the locus, so `τ` fixes it.
4. **`S_PRE`.** Each conjunct of the precomposed family by cases: total evolution by iterating `Φ`
   after `τ`; admissibility by `τ`'s and `Φ`'s; homogeneity by `funext`; injectivity through `τ`'s
   involution; surjectivity by precomposing `Φ`'s preimage with `τ`; descent on every tuple; and
   factorization and the pair clause unchanged, `τ` fixing every product tuple.
5. **`a31_nonunique`.** Precompose `Φa` by `τ` (`S_PRE`); strictify with `a30_s_strictify` and
   transfer eligibility with `a30_t_transfer`; conjunct 8 with the strict lift and the identities
   (`rnt1_strict_imp_twisted`); conjuncts 1 and 2 of that final family by `a29_p_hold`. The second
   law's value at `W` is equivalent to `Φa W₂`; if it were equivalent to `Φa W`, injectivity of `Φa`
   (`gramPhaseEquiv_of_relabel`) would give `W ≈ W₂`, against `S_W`.
6. **`a31_c_exclusive`.** From `P_N`'s witnesses, `P_U` gives the equivalence `P_N` negates.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| `a31_shared_witnesses` | `a28_s_proper` as a premise; any verdict of this round |
| `a31_shared_transposition`, `a31_shared_precompose` | any verdict of this round |
| `a31_nonunique` | `a28_s_proper`; any off-locus value of a law it did not construct (hazard 3) |
| `a31_unique` | `a31_shared_witnesses`, `a31_shared_transposition`, `a31_shared_precompose` |
| `a31_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A31-1` | `A31-1-NONUNIQUE` | **very high** | uniqueness at this pair would require a single off-locus class, and the freeze's reading exhibits two, checked in exact arithmetic |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A31-1-NONUNIQUE`

> @@S_N@@

### `A31-1-UNIQUE`

> @@S_U@@

### `A31-1-UNDECIDED`

> @@S_X@@

### The corollary, REQUIRED

`a31_c_exclusive : (P_N) → ¬ (P_U)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label.

| row | outcome |
| --- | --- |
| 1 | `A31-1-NONUNIQUE` |
| 2 | `A31-1-UNIQUE` |
| 3 | `A31-1-UNDECIDED` |

***

## The `P0` row, per case

The `P0` cell of `verification/ROADMAP.md` ends, at `D`, with act 30's sentence and its standing
clause:

> @@P0_ADMITS@@ @@P0_STANDING@@

**On `A31-1-NONUNIQUE`** the following is appended once, after that standing clause — act 29's frozen
row 1 addition, verbatim, and the standing clause:

> @@P0_N@@ @@P0_STANDING@@

**On `A31-1-UNIQUE`**, likewise, act 29's frozen row 2 addition, verbatim, and the standing clause:

> @@P0_U@@ @@P0_STANDING@@

**On `A31-1-UNDECIDED`** the cell is not touched. The expected `ROADMAP.md` at `E` is `D`'s with that one
insertion, or `D`'s unchanged, byte for byte; rehearsed at `D`, the two decided cells give blobs
`@@ROAD_N@@` (`A31-1-NONUNIQUE`) and `@@ROAD_U@@` (`A31-1-UNIQUE`), and with either the guard reports 91
PASS and 0 FAIL with `D`'s verdict map.

***

## What no outcome licenses

- **No outcome licenses "factorization selects" or "factorization does not select."**
- **No outcome disturbs any verdict of acts 22 to 30**, which stand as those rounds state them.
- **No outcome reports anything at another pair, configuration or time.**
- **No outcome reports `L5-FREE`**, and none says a condition is empty, has no content, or fails to
  restrict.
- **No outcome adopts a law, a carrier or a principle**, and none closes `P0`, which stays `OPEN`.
- **No law exhibited here is read as a symmetry, an antiunitary map, a time reversal, a unitary
  evolution or a dynamics, and none is called canonical, unique or continuous.**

## Non-doings

This round does not define anything, restate any rung or declaration, read any configuration but
the one frozen, edit any closed round's record or guard contract, write any manuscript file, or read
any object of act 32. **Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within `propext`,
`Classical.choice` and `Quot.sound`.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, written before `F` and added by the execution with exactly this blob. It
imports nothing from the repository and changes nothing; it reads `D` and the commit under check
through `git`, and embeds every frozen text it compares against.

`controls.py check <commit>` fails unless:

- **the duality holds:** the frozen `P_N` and `P_U` are exactly the existential and universal forms
  rebuilt from the shared components, the second law's admission body is the first's with `Φ`
  renamed `Φ'`, and the comparison is at time zero;
- **the module** begins with the frozen import and carries the one frozen `open`, no forbidden
  command or token, a `#print axioms` line for every theorem, only the frozen names or `a31_shared_…`,
  each frozen theorem with its frozen statement, at most one verdict theorem, `a31_c_exclusive`, and
  under `A31-1-NONUNIQUE` the three required shared statements;
- **the result note** carries the outcome line once, the earned label's frozen sentence once and no
  other label's, THE CLAUSE's mention once with the complete clause following it, and under
  `A31-1-NONUNIQUE` the three required shared statements by name;
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen insertion for the case, or to `D`'s;
- **the guard** is byte-identical to `D`'s;
- **the census** is `D`'s with exactly one family appended, last, for `ProductOffLocusUniqueness`,
  `kernel-only`, no manuscript anchor, its note naming the label and no other;
- **`OIBridge.lean`** is `D`'s with `import OIBridge.ProductOffLocusUniqueness` inserted directly
  after `import OIBridge.ProductStrictLift`;
- **the paths** changed from `D` are exactly the three record files and the module (added),
  `OIBridge.lean` and the census (modified), and on a decided outcome `ROADMAP.md` (modified).

`controls.py --self-test` also checks the constants against this preregistration, beside it, the
duality of the frozen texts together with @@N_DMUTS@@ duality mutations each of which must be rejected,
builds a synthetic execution for each of the three rows and requires every one to hold, and applies
@@N_MUTS@@ mutation controls, each of which must fail with its named code. Run at `D` beside this file,
it prints:

@@SELFTEST@@

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then linear commits from
`F`, each with one parent:

1. **Stage 1 — the module and the controls.** `controls.py` with its frozen blob; the module with the
   frozen header and shared lemmas only, among them, on the route to `A31-1-NONUNIQUE`, the three
   required shared statements; the import line. No verdict theorem and no corollary.
2. **Stage 2 — the verdict.** `a31_nonunique` or `a31_unique`, or neither, and `a31_c_exclusive`.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last; the `P0` cell for the
   case.
4. **The result note** `result.md`, whose commit is `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40). A stage whose build fails is followed by a fixing
commit, never rewritten. The label is read from the module at `E`.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the frozen propositions elaborate as frozen | before `F`: the elaboration run above; at `E`: `C8`, every frozen theorem compiled under its statement |
| every verdict is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces are exactly the frozen ones for the case, and the guard is untouched | `C9` |
| the guard stays green | `C8`: 91 checks, all `PASS`, in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen propositions unchanged** is repaired by later
  linear commits before `E`.
- **A verdict that cannot be obtained** is reported `A31-1-UNDECIDED`, with the step named.
- **A freeze failure** — a frozen proposition that is ill-typed or cannot be stated as frozen, or a
  required statement (`S_W`, `S_TAU`, `S_PRE`, the corollary) that is false as frozen when the route
  through it is taken — is not `UNDECIDED` mathematics and is not repaired by changing the target:
  the round halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
