# Reconstruction round ORD-1 — iterated operation data and finite or infinite order on the completed body: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round ORD-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-ord-1-composition-order/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-ord-1-composition-order/
record AM verification/receipts/ORD-1.json
execution A verification/lean-mathlib/OIBridge/CompositionOrder.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/ORD-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, and no other round's
record change under any outcome.**

## The objects

- **`D`** = `afa66d16d7adaffe94fb9bac391e6039c51dad8a`, the head of `main` after round TRB-1 landed (push run
  37231625458, every job green; the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

OPACT-1 landed completion-valued operation data, the affine map each datum induces on the chart of a completed body
of finite rank, the composition law `after` with `induced_after`, and the affine equivalence `inducedEquiv` a datum
with an inverse datum induces. TRB-1 landed the geometry of a boundary-transitive body with no notion of the order of a
map in it. This round is the order side, on its own spine and consuming nothing of TRB-1:

```
OPACT composition (after, induced_after) → iterated operation data (iterAfter) → finite or infinite order on the body
```

1. **Order predicates.** `InfiniteOrderOn Ω g := ∀ m ≥ 1, ∃ x ∈ Ω, g^[m] x ≠ x`;
   `FiniteOrderOn Ω g := ∃ N ≥ 1, ∀ x ∈ Ω, g^[N] x = x`; **ORD∞** `OrdInf Ω G := ∃ g ∈ G, InfiniteOrderOn Ω g`, a
   predicate on a set of automorphisms saying nothing about closure or transitivity; `MulClosed G`, composition
   closure. Finite and infinite order exclude each other, one theorem per direction.
2. **Iterated data.** `iterAfter C T hT m`, the `m`-fold composite of a datum with itself through `after`; it
   respects affine relations, and the map it induces is the `m`-fold composite of the induced map.
3. **Infinite order keeps every power nontrivial.** A reversible datum whose induced automorphism has infinite order
   on the chart body has, for every `m ≥ 1`, a preparation that `iterAfter m` moves.
4. **Stage preservation gives finite order (DRIVE F-D3).** A reversible datum that carries each stage's preparations
   to preparation vectors of the same stage induces an automorphism of finite order on the chart body: a finite
   affinely spanning subset of the chart generators exists (`exists_finset_affineSpan_eq_top`), each generator returns
   under some positive power, a common period exists, and an affine map of the chart fixing a spanning set is the
   identity. Reversibility (both `Undoes` clauses) and finite rank (through the chart `C`) are load-bearing: a
   per-stage constant datum is stage preserving and respects affine relations with no positive power of its induced
   map the identity, and without a chart no uniform period exists.
5. **The closure test.** A finite composition-closed set of affine automorphisms has no member of infinite order
   (`not_ordInf_of_finite_of_mulClosed`). The countercontrol that keeps the closure hypothesis honest is the
   singleton of the one-radian rotation of the ball: finite, not composition-closed, with a member of infinite order
   (`ordInf_singleton_rot3`). A checker that substituted "finite listed family" for "finite closed set" would be
   caught by it.
6. **Controls on the ball.** The rotation by one radian has infinite order (π irrational); the Householder
   reflections have none; the affine automorphisms of the ball and the rotation family each have a member of
   infinite order.
7. **Not stated.** No implication from transitivity to order in any dimension, including `d = 2`: the question
   whether a composition-closed boundary-transitive family in dimension ≥ 2 has a member of infinite order stays
   open, its known proofs passing through Jordan–Schur or Cartan's closed-subgroup theorem, neither in Mathlib
   `v4.33.0`. No ball, ellipsoid or dimension statement; no drive, flow or continuity; nothing of
   `InvariantInnerProduct` or `TransitiveBody` is imported or cited.

### In scope
- the module `OIBridge/CompositionOrder.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any theorem with a transitivity hypothesis and an order conclusion, or the converse; the `d = 2` statement;
- any statement about transitivity, a ball, an ellipsoid, a dimension, a drive, a flow, continuity or compactness
  (the controls use `ball3`, `rot3` and `hh3` as concrete affine equivalences and sets only);
- any OI sourcing of an operation datum, of `FiniteRank`, of a completion chart or of stage preservation;
- anything from round L3B; 3A banking, the EO countermodel round, manuscript follow-ups.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

The design theorem identity is the statement surface of `CompositionOrder` embedded in `controls.py` (blob
`6cb4471b948a9a8ea22e310118d6f7fa1af6eb63`): the preamble, every context line in order, the 45 declarations in order
and by kind, every theorem's signature up to `:=`, every definition whole, and the 35 `#print axioms` lines. The
reference module is blob `d8e04d32423c1f5ec33c1c9100822f6dadc727eb` (`claude/ord1-dev2` at `76ec9f10`, the module of
`claude/ord1-dev` at `ba7983ba` unchanged). A repair may change proofs only. `OIBridge.lean` is `D`'s with
`import OIBridge.CompositionOrder` inserted directly after `import OIBridge.TransitiveBody` (blob
`6f94ffa30a393b38da4fc431424b6901c823a3c6`). The census is `D`'s with one family, embedded in `controls.py`, inserted
directly after the TRB-1 family (blob `d975aa8d1d59ccc029ef80554cb7b3c27683638f`).

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| ORD | `InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf`, `MulClosed` | the definitions of §1, whole |
| DIR | `finiteOrderOn_of_not_infiniteOrderOn`, `not_infiniteOrderOn_of_finiteOrderOn`, `not_infiniteOrderOn_iff` | `¬ InfiniteOrderOn Ω g → FiniteOrderOn Ω g`; `FiniteOrderOn Ω g → ¬ InfiniteOrderOn Ω g`; the `iff` cites both |
| CLO | `not_ordInf_of_finite_of_mulClosed` | `G.Finite → MulClosed G → ¬ OrdInf Ω G` |
| FIN | `exists_finset_affineSpan_eq_top` | `affineSpan ℝ s = ⊤ → ∃ t : Finset P, ↑t ⊆ s ∧ affineSpan ℝ ↑t = ⊤` in a finite-dimensional torsor |
| PER | `exists_return`, `exists_common_period` | a finite set carried into itself by an injective map returns every point; finitely many returning points share a period |
| IT | `idDatum`, `StagePreserving`, `iterAfter`, `stageGen` | the definitions of §2 and §4, whole |
| B | `affineRespect_idDatum`, `induced_idDatum`, `affineRespect_iterAfter`, `induced_iterAfter`, `coe_induced_iterAfter`, `coe_inducedEquiv` | `iterAfter` respects affine relations; `induced C (iterAfter C T hT m) _ = affPow (induced C T hT) m`; coercions |
| C | `iterate_eq_id_of_fix`, `exists_moved_of_infiniteOrderOn` | infinite order on the chart body ⟹ `∀ m ≥ 1, AffineRespect (iterAfter C T hT m) ∧ ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x` |
| **FD3** | `finiteOrderOn_of_stagePreserving` | `(hS : AffineRespect S) (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (hsp : StagePreserving T) : FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)`, with `C : CompletionChart D` the section variable |
| FD3′ | `not_infiniteOrderOn_of_stagePreserving`, `not_stagePreserving_of_infiniteOrderOn` | the two contrapositive forms |
| E1 | `finiteOrderOn_refl`, `hh3_hh3`, `finiteOrderOn_hh3`, `not_ordInf_householder3` | the identity and every Householder reflection have finite order; `¬ OrdInf ball3 householder3` |
| E2 | `rot3_one_iterate`, `infiniteOrderOn_rot3_one` | `InfiniteOrderOn ball3 (rot3 1)` |
| E3 | `ordInf_fullAut3`, `ordInf_range_rot3`, `ordInf_singleton_rot3` | ORD∞ for the automorphisms of the ball, the rotation family and the singleton `{rot3 1}` |
| core | `ord1_core` | FD3, C, E2, E1's last row, E3's singleton and CLO together |

Supporting declarations frozen with the surface: `affPow`, `coe_affPow`, `finiteOrderOn_of_iterate_eq`, `nonempty_prep`,
`exists_gen_finset`, `mem_stageGen`, `mapsTo_stageGen`, `householder3`, `rot3_mem_fullAut3`.

### Semantic guards (in `controls.py`)

- **S1 separation.** None of the tokens `BoundaryTransitive`, `CoversBoundaryFrom`, `IsBodyGroup`, `TransBody`,
  `Transitive`, `ElementaryDrivability`, `Continuous`, `IsCompact`, `invMatrix`, `SCInf`, `BinaryVisible`,
  `SharpSeed`, `centroid`, `qBall`, `eball` occurs in the module; no import of `OIBridge.TransitiveBody` or
  `OIBridge.InvariantInnerProduct`; the header carries "No transitivity, ball, dimension, drive or flow is claimed;
  TRANS ⇒ ORD∞ is not stated." Mutations: a theorem with `BoundaryTransitive` among its hypotheses and `OrdInf` in
  its conclusion; the `TransitiveBody` import line.
- **S2 dimension.** Outside the §E controls section no statement names `3`, `Fin 3`, `ball3`, `rot3`, `hh3`,
  `fullAut3` or `finrank`; the verdict's first clause is the stage-preservation theorem for every chart. Mutation:
  `C.d = 3` conjoined to FD3's conclusion.
- **S3 F-D3 hypotheses exactly.** FD3's binders are `{S T : OpDatum D}`, `(hS : AffineRespect S)`,
  `(hT : AffineRespect T)`, `(hST : Undoes C S T hS)`, `(hTS : Undoes C T S hT)`, `(hsp : StagePreserving T)` — five
  explicit binders and the section variable `C` — and its conclusion is
  `FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)`. Mutation: `hTS` dropped.
- **S4 definitions are what they say.** `InfiniteOrderOn`, `FiniteOrderOn`, `MulClosed`, `StagePreserving` (the
  same `i` on both sides), `idDatum` (`τ := prepVec D`) and `iterAfter` (step `after C T (iterAfter T hT m) hT`) carry
  their frozen bodies; `OrdInf` is existential over `G`. Mutations: `∀ g ∈ G`; `⟨j, y⟩`.
- **S5 closure control.** CLO carries both `(hG : G.Finite)` and `(hcl : MulClosed G)` with conclusion
  `¬ OrdInf Ω G`; `ordInf_singleton_rot3 : OrdInf ball3 {rot3 1}` is a kernel theorem with its print. Mutation:
  `MulClosed G` dropped.
- **S6 controls present.** E1–E3 and CLO are kernel theorems with axiom prints. Mutation: the print of
  `infiniteOrderOn_rot3_one` removed.
- **S7 one direction per theorem.** DIR's two directions are two theorems without `↔`; the `iff` names both in its
  proof. Mutation: one direction removed.
- **N1–N3** as TRB-1: declaration list and kinds, binder contexts, statements and definitions, no `sorryAx`; every
  `#print axioms` within `[propext, Classical.choice, Quot.sound]`.

`controls.py`:
- is blob `6cb4471b948a9a8ea22e310118d6f7fa1af6eb63` (SHA-256
  `12144fbf66a8ffeb2777f9cdbd7e148e47f802bb8bfac247ecd6d8b99cc68e45`, 644 lines), carried by the predicted execution
  tree on the disposable branch `claude/ord1-predicted`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 29 checks; its 13 module mutation controls each fail with their named code, and the import and
  census controls each pass the frozen edit and fail a dropped line or a changed status.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| order predicates | `coe_affPow`, `finiteOrderOn_of_not_infiniteOrderOn`, `not_infiniteOrderOn_of_finiteOrderOn`, `not_infiniteOrderOn_iff`, `finiteOrderOn_refl`, `finiteOrderOn_of_iterate_eq` | built; axioms standard | S4, S7 |
| closure | `not_ordInf_of_finite_of_mulClosed`, `ordInf_singleton_rot3` | as above | S5 |
| finite extraction | `exists_return`, `exists_common_period`, `exists_finset_affineSpan_eq_top` | as above | N2 |
| iteration | `affineRespect_idDatum`, `induced_idDatum`, `affineRespect_iterAfter`, `induced_iterAfter`, `coe_induced_iterAfter`, `coe_inducedEquiv` | as above | N2 |
| infinite order | `iterate_eq_id_of_fix`, `exists_moved_of_infiniteOrderOn` | as above | N2, S1 |
| stage preservation | `nonempty_prep`, `exists_gen_finset`, `mem_stageGen`, `mapsTo_stageGen`, `finiteOrderOn_of_stagePreserving`, `not_infiniteOrderOn_of_stagePreserving`, `not_stagePreserving_of_infiniteOrderOn` | as above | S2, S3 |
| controls | `hh3_hh3`, `finiteOrderOn_hh3`, `not_ordInf_householder3`, `rot3_mem_fullAut3`, `rot3_one_iterate`, `infiniteOrderOn_rot3_one`, `ordInf_fullAut3`, `ordInf_range_rot3` | as above | S6 |
| verdict | `ord1_core` | as above | S1–S3 |

## Design evidence

Design runs (Mathlib bridge job read only):

| Run | Branch, commit | Workflow run | Bridge result |
|---|---|---|---|
| 1 | `claude/ord1-dev` `50a96964` (from `7c821261`) | 37226093756 | red on one error: `idDatum` must be `noncomputable`; every theorem already printed standard axioms |
| 2 | `claude/ord1-dev` `ba7983ba` | 37226273423 | **green**: built (3625 jobs); every `#print axioms` line `[propext, Classical.choice, Quot.sound]`; release gate PASS (lean-axioms 5526 named results, no sorry; lean-manuscript OK) |
| 3 | `claude/ord1-dev2` `76ec9f10` (from `D`, the module of run 2 unchanged; import after `TransitiveBody`; census family after TRB-1's) | 37232152756 | **green**: built (3630 jobs); every `#print axioms` line of the module `[propext, Classical.choice, Quot.sound]`; release gate PASS (lean-axioms 5552 named results, no sorry; lean-manuscript OK with the ORD-1 family after TRB-1's; 30 receipts hold; legacy 303) |

Mathlib names at `v4.33.0` the design had to correct: `irrational_pi` lives in `Mathlib.Analysis.Real.Pi.Irrational`;
`Function.iterate_one` takes its function implicitly; the finset-to-set image lemma is `Finset.subset_set_image_iff`;
`Finset.not_mem_empty` is `Finset.notMem_empty`; `push_neg` is `push Not`. The finite-extraction lemma built on the
`vectorSpan` route (`AffineSubspace.nonempty_of_affineSpan_eq_top`, `AffineSubspace.vectorSpan_eq_top_of_affineSpan_eq_top`,
`vectorSpan_eq_span_vsub_set_right`, `exists_linearIndependent`, `LinearIndependent.set_finite_of_isNoetherian`,
`AffineSubspace.affineSpan_eq_top_iff_vectorSpan_eq_top_of_nonempty`, `Submodule.span_mono`), with the pull-back
`insert p ((· +ᵥ p) '' b)`.

Statement changes forced by the design runs against the design document: none. Beyond the design surface the module
carries the proof-support lemmas `finiteOrderOn_of_iterate_eq` and `mem_stageGen` and the `iff` corollary
`not_infiniteOrderOn_iff`, which the design permitted; the rotation-family control is named `ordInf_range_rot3`. The
order predicates, the rotation and reflection controls were drafted first inside TRB-1's design module, compiled there
with standard axioms, and were moved here by the owner's scope cut; TRB-1 landed with no order predicate.

### The predicted execution tree

⟨filled in the freeze revision: the commit on `claude/ord1-predicted`, a single-parent child of `D`, carrying this
preregistration in its previous revision, `controls.py`, the module, the import and the census family; its
`workflow_dispatch` run and the controls check at that commit⟩

## Stages

1. **C1** adds `controls.py`, blob `6cb4471b`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom
     set within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`ORD-1-COMPOSITION-ORDER-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head
  run at `E` is green on every job, the Mathlib bridge building `CompositionOrder` with every frozen `#print axioms`
  reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The result note
  states: iterated composition, nontrivial powers under infinite order, finite order from stage preservation and
  reversibility on a finite-rank chart body, the closure control with its countercontrol, and the ball controls — and
  nothing about transitivity, a ball theorem, a dimension, a drive, a flow or OI sourcing.
- **`ORD-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome states an implication between transitivity and order in either direction, sources an operation datum,
finite rank, a completion chart or stage preservation, or claims a ball, an ellipsoid or a dimension.
