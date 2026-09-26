# Track B act 32 — classification of the single-carrier surjective isometries: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 32 classifies the surjective isometries of the frozen normalized single-carrier space relative
> to the frozen four-shape family, and adopts none. A map satisfying the frozen isometry hypotheses
> is a mathematical isometry of that quotient space; it is not thereby a physical symmetry, a
> transformation law, a dynamics, a time reversal, an antiunitary operation or a principle of nature.
> A `RIGID` verdict classifies that frozen isometry problem, and a `NOT-RIGID` verdict exhibits a
> mathematical isometry outside the frozen family. Neither verdict selects a physical law or closes
> `P0`. No isometry, carrier, family or principle gains physical status by appearing in this
> classification, and nothing here derives, recognises or approaches quantum evolution.

## The declarations

```v3-round
round A32
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/
record AM verification/receipts/A32.json
execution A verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
execution M verification/lean/edge_rigidity_probe.py
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A32.json`. Every
other path the round changes is an execution path listed above.

The guard and `ROADMAP.md` change only on a decided outcome, and only as this file freezes:
- the guard by the ledger below;
- `ROADMAP.md` by the `P0` correction for the case.

## The objects

- **`D`** = `d61c6c5409db201e3c25abbf3ec0ecce1f530684`: act 30's receipt commit `Q` and the head of `main` after act 30's landing. It
  is certified by push run 36230402641: all three jobs green, the guard 91 PASS and 0 FAIL, and the
  release gate 21 of 21 with `v3-receipts` holding on six receipts. Every measurement here was taken
  at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A32.json`.

A32 runs beside act 31. It reads no object, result, receipt or control plane of act 31, and a later
movement of `main` enters it only by reconciliation after `E`. Both rounds append to the `P0` cell
and to the census, so whichever lands second resolves those two files by merits in its
reconciliation. Each row is taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — act 26's frozen negative form is stronger than the negation.**
- Act 26 froze `NOT-RIGID` as one exhibited class separated from every member of the family at once.
- Act 26's own result (its DF3, result note lines 1011–1016) found that no such class exists for any
  isometry: every per-circle map is realized by some member.
- This round's negative label is therefore the exact logical negation of the positive one, `P_N` =
  `∃ φ, H(φ) ∧ ¬ FOUR(φ)`. The class that separates the map from a member may depend on the member.

**Hazard 2 — a map stated through an `if`.** The witness is characterized by equations on the nine
relabelled Fourier circles of act 26, `WIT(φ)`. It is not stated as a case split that would need
`open Classical in`.

**Hazard 3 — overlap.** The circles meet, so the equations of `WIT` must agree wherever two
circles share a class. Otherwise no map satisfies them and every statement about such a map is
vacuous. The overlap control and `S_EXIST` exclude this.

**Hazard 4 — vacuity of the countercontrol.** A quarter-turn of the Fourier circle with the identity
on the other eight circles has inconsistent equations, since the quarter-turn moves the classes the
circles share. The countercontrol is therefore stated piecewise:
- the quarter-turn on the classes of the Fourier circle;
- the identity on every class off it.

Its existence is a conjunct of the statement.

**Hazard 5 — no global invariant separates.**
- Before the freeze, three kinds of invariant were tested: forms that are bilinear, trilinear or
  slot-twisted in the feature coordinates and invariant under coordinate permutations.
- None of them separates the witness from the family.
- The reason is that global conjugation is itself the index reversal of the walk.

Separation is therefore member by member: a finite check over the 576 pairs of relabellings and the
four shapes.

**Hazard 6 — kernel time.**
- The member-by-member separation is the heaviest step. It was rehearsed in CI before the freeze;
  see the evidence below.
- The strategy is not frozen. The proposition, the family, the witness equations and the permitted
  provenance are.

**Hazard 7 — history.**
- Act 25 recorded `ISO3-UNDECIDED`, and act 26 recorded `A26-2-UNDECIDED`. Both stand as recorded,
  and no outcome here revises them.
- A decided outcome settles the same mathematical question with new evidence. It is stated as "the
  positive classification proposition posed as act 25's `ISO3` is false (or holds) at the frozen
  single-carrier configuration", never as "act 25's `ISO3` was false".

**Hazard 8 — a stale current-status clause.**
- The `P0` cell of `verification/ROADMAP.md` carries a clause twice, once in act 25's sentence and
  once in act 26's: the classification is "recorded undecided …; no isometry outside the family is
  exhibited".
- Both sentences are pinned verbatim in the `ROADMAP` by the guard contracts `R7-OGC` and `R7-CGR`.
- A decided outcome makes the clause stale, and under §A.27 it is corrected in place. The legs of
  those two contracts whose sole purpose is to keep that wording current are retired by the frozen
  ledger below. Their result-note contracts are unchanged.

**Hazard 9 — vocabulary.** An isometry of the normalized space is not a symmetry, and the finite
family is not a group adopted as physical. Neither is written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `realizable_of_gramPhaseEquiv`;
- **act 23**, `OrbitLawGaps.lean` — `hadamard_z_admissible`;
- **act 24**, `OrbitGeometrySelector.lean`:
  - `mixedTriple`, `mixedTriple_gauge` and `mixedTriple_star`;
  - `coord_le_dist`, `fourier_dist_le` and `geo1_class_invariant`;
  - the frozen distance equation;
- **act 25**, `OrbitGeometryIsometries.lean`:
  - `iso1_single_carrier` and `iso2_classes_single`;
  - `mixedTriple_relabel2`, `mixedTriple_transpose` and `fibreGram_unique`;
  - `relabel2_isometry`, `conj_isometry` and `relabel2_realizable`;
  - the four generators and the four-shape conclusion;
- **act 26**, `OrbitGeometryRigidity.lean`:
  - `a26_1_circle_count` with its nine circles `R`, `perm_decomp` and `pred_stab`;
  - `stab_row_double` and `stab_col_double`;
  - `rigid_motion_of_tuple_isometry` and `a26_0_affine_extension`;
  - the frozen hypotheses and four-shape text of its preregistration, lines 668–710.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| act 26's frozen hypotheses and four-shape conclusion | `verification/programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity/preregistration.md` | 668–710 |
| act 25's `ISO3` route, recorded undecided | `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean` | 1110 |
| `iso1_single_carrier`, `iso2_classes_single` | the same file | 770, 1081 |
| `mixedTriple_relabel2`, `fibreGram_unique`, `mixedTriple_transpose` | the same file | 72, 82, 94 |
| `relabel2_realizable`, `relabel2_isometry`, `conj_isometry` | the same file | 273, 300, 313 |
| `mixedTriple`, `mixedTriple_gauge`, `mixedTriple_star`, `coord_le_dist` | `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean` | 79, 88, 114, 123 |
| `geo1_class_invariant`, `fourier_dist_le` | the same file | 471, 727 |
| `a26_0_affine_extension`, `stab_row_double`, `stab_col_double`, `perm_decomp` | `verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean` | 444, 581, 602, 620 |
| `pred_stab`, `a26_1_circle_count`, `rigid_motion_of_tuple_isometry` | the same file | 2134, 2160, 2309 |
| `hadamard_z_admissible` | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | 116 |
| `realizable_of_gramPhaseEquiv` | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | 355 |
| `gramPhaseEquiv_refl`, `_symm`, `_trans` | `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | 141, 146, 162 |

| file at `D` | blob |
| --- | --- |
| `OrbitGeometryRigidity.lean` | `3e15384196203939d348f2a313a873818ec4b684` |
| `OrbitGeometryIsometries.lean` | `954fbddaa7511713a26c316b3b2e0f29497e81d2` |
| `OrbitGeometrySelector.lean` | `ce9d1aa05dfdedfb5cac171cfe6379681942195f` |
| `OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `verification/lean-mathlib/OIBridge.lean` | `7a6aaa6cd4011d03932a0c65fe622e6fc521b2c8` |
| `verification/lean-manuscript-census.json` | `97436abcb04df23a821a33e5bba463122647378e` |
| `verification/ROADMAP.md` | `e6779380f858bcb905fc9877ed2f11bf5de75c95` |
| `verification/lean/edge_rigidity_probe.py` | `0475fe3d8c5724a7bf918bf3fd75ae06370cef26` |

The names this round introduces return nothing from `git grep -l` at `D`: `OrbitIsometryClassification`,
`act-32`, `A32-` and `a32_`.

***

## Why this round exists

Act 26 left the classification undecided. Two things were in place when it stopped:
- its first positive-route step was proved: every tuple isometry with the three hypotheses is, on
  feature vectors, a rigid motion carrying the normalized set onto itself;
- its record noted that the isometries of the union of the nine circles outnumber the family, but
  exhibited no isometry outside the family in the kernel.

This round decides the question at the same configuration, with the same domain, metric, quotient
and family.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

These are computations outside the kernel. They certify nothing.

1. **The normalized space.** The nine relabelled Fourier circles are round circles in the feature
   space. Each coordinate of a relabelled Fourier tuple is `S z^m / 64` with `S = ±1` and
   `m ∈ {−1, 0, 1}`. The imaginary directions of the nine circles are mutually orthogonal: their Gram
   matrix is `1536` times the identity.
2. **The witness.**
   - The map is conjugation of the Fourier parameter on the Fourier circle, and the identity on the
     classes of the other eight circles.
   - It preserves every distance. On the Fourier circle together with each other circle, it agrees
     with a relabelling of the family. Two of those relabellings are act 26's `stab_row_double` and
     `stab_col_double`.
   - Checked exactly against all 2304 words of the family, it is none of them.
3. **The overlaps.**
   - The Fourier circle meets exactly four of the other eight: circles 4 and 8 at the parameter
     `1`, and circles 5 and 7 at `−1`. The circles are numbered in `a26_1_circle_count`'s order,
     from 0.
   - At each overlap, one coordinate has exponent `±1` on the Fourier circle and exponent `0` on the
     other circle. This forces the parameter to be `±1`, where conjugation is the identity.
   - The other four circles never meet it: a coordinate constant on both circles differs in sign.
4. **The separation encoding.**
   - At the parameter `i` every coordinate of the Fourier tuple is `i ^ n(q) / 64`. The exponent
     `n(q)` is read off a four-by-four integer table.
   - This agrees with the complex definition on all 4096 coordinates.
   - For each of the four shapes, a small cover of test points separates all 576 pairs of
     relabellings. A test point is a test circle together with a coordinate, and the covers have 4, 5,
     2 and 2 test points.

***

## The configuration, FROZEN — act 26's, unchanged

- The carrier is `Fin 4`, the ancilla `Fin 1`, and `Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))`.
- The distance is act 24's equation, bound as a hypothesis as act 26 binds it.
- The Fourier tuple at `z` is act 23's lambda, which act 26's statements carry.
- The nine circles are act 26's list `R`, in its order.
- The **designated circle** is the Fourier circle, the pair `(1, 1)`; the other eight are `R` less
  `(1, 1)`.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

- `verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean` begins with exactly the
  line `import OIBridge.OrbitGeometryRigidity` and imports nothing else.
- Its declarations sit in `namespace OIBridge` / `namespace OrbitIsometryClassification`.
- It carries exactly one `open` command, before its first theorem, verbatim:

```lean
open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity
```

The module carries none of the following:
- a `variable`, `include`, `omit`, `attribute`, `notation`, `local`, `scoped`, `universe` or further
  `open` command, or an `open … in`;
- a definition of any kind;
- `sorry`, `admit` or `native_decide`.

`decide +kernel`, which reduces in the kernel with the standard axioms, is not excluded.

### `P_R` — every map with the three hypotheses satisfies the four-shape conclusion

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
      ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
      ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)) →
    (∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))
```

### `P_N` — some map with the three hypotheses does not

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
      ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
      ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
    ∧ ¬ (∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))
```

**The two are duals by construction.** Both are built from one head, one hypothesis text `H` and one
four-shape text `FOUR`:
- `P_R` is `∀ φ, (H) → (FOUR)`;
- `P_N` is `∃ φ, (H) ∧ ¬ (FOUR)`.

`controls.py` rebuilds both from those components and checks the frozen texts against them, so
`P_N ↔ ¬ P_R` holds by the shape of the statements. `H` and `FOUR` are act 26's texts, verbatim.

### The statements required under `A32-NOT-RIGID`

The kernel must establish each of these as a separate theorem, with the statement frozen here, before
`a32_not_rigid` consumes them.

`S_EXIST` — a map satisfying the witness equations exists:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
        ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
        GramPhaseEquiv (φ G) G))
```

`S_ISO` — every such map satisfies the three hypotheses:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
        ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
        GramPhaseEquiv (φ G) G)) →
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
      ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
      ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
```

`S_SEP` — no such map satisfies the four-shape conclusion:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
        ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
        GramPhaseEquiv (φ G) G)) →
    ¬ (∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))
```

### The five controls, required under `A32-NOT-RIGID`

`S_OVL` — **overlap compatibility.** Wherever the Fourier circle meets another of the nine, the
conjugation rule and the identity rule give the same class:

```lean
∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
  ∀ z w : ℂ, star z * z = 1 → star w * w = 1 →
    GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
    GramPhaseEquiv (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))
```

`S_MOVE` — **nontrivial motion.** Every map satisfying the witness equations moves some realizable
class:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, star z, -1, -star z; 1, -1, 1, -1; 1, -star z, -1, star z] p.1 q.1))))
      ∧ (∀ r ∈ [((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)],
        ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (r.1 i)).submatrix r.2 r.2) →
        GramPhaseEquiv (φ G) G)) →
    ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ ¬ GramPhaseEquiv (φ G) G
```

`S_GLOBAL` — **a positive family control.** Global conjugation, a member of the family, satisfies the
hypotheses and the four-shape conclusion, so `¬ FOUR` is not vacuously true:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), φ = (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => fun i => Matrix.of fun j k => star (G i j k)) →
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
      ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
      ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
    ∧ (∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))
```

`S_ID` — **the identity is not separated.** The identity satisfies the hypotheses and the four-shape
conclusion:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), φ = (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G) →
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
      ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
      ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H))
    ∧ (∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))
```

`S_QUARTER` — **the failing-isometry countercontrol.** A map that turns the parameter of the Fourier
circle by a quarter, and fixes every class off that circle, exists and does not preserve the
distance:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ∀ (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
  (∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (Complex.I * z), -1, -(Complex.I * z); 1, -1, 1, -1; 1, -(Complex.I * z), -1, (Complex.I * z)] p.1 q.1))))
      ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G →
        (∀ z : ℂ, star z * z = 1 →
          ¬ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))) →
        GramPhaseEquiv (φ G) G)))
  ∧ ∀ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    ((∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →
        GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) →
        GramPhaseEquiv (φ G) (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (Complex.I * z), -1, -(Complex.I * z); 1, -1, 1, -1; 1, -(Complex.I * z), -1, (Complex.I * z)] p.1 q.1))))
      ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G →
        (∀ z : ℂ, star z * z = 1 →
          ¬ GramPhaseEquiv G (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))) →
        GramPhaseEquiv (φ G) G)) →
    ¬ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)
```

Under `A32-RIGID`, `S_GLOBAL` and `S_ID` are required. Under `A32-UNDECIDED` none of these is
required. Whichever is present carries its frozen statement.

### The theorems, FROZEN by name and statement form

Each is declared `theorem NAME :` with no binder before the colon. Statements are compared after
collapsing whitespace.

| role | theorem | statement |
| --- | --- | --- |
| `A32-RIGID` | `a32_rigid` | `P_R` |
| `A32-NOT-RIGID` | `a32_not_rigid` | `P_N` |
| corollary, required in every case | `a32_c_exclusive` | `(P_N) → ¬ (P_R)` |
| required under `A32-NOT-RIGID` | `a32_shared_exists` | `S_EXIST` |
| required under `A32-NOT-RIGID` | `a32_shared_isometry` | `S_ISO` |
| required under `A32-NOT-RIGID` | `a32_shared_separation` | `S_SEP` |
| control, required under `A32-NOT-RIGID` | `a32_control_overlap` | `S_OVL` |
| control, required under `A32-NOT-RIGID` | `a32_control_moves` | `S_MOVE` |
| control, required under both decided labels | `a32_control_global` | `S_GLOBAL` |
| control, required under both decided labels | `a32_control_identity` | `S_ID` |
| control, required under `A32-NOT-RIGID` | `a32_control_quarter` | `S_QUARTER` |

A module with neither verdict theorem reports `A32-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a32_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed. Each
is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design evidence**
recorded here: none is a `check-run` attestation, and no predicate of the round reads them.

**The ten texts and the corollary.** The elaboration file is
`verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean`, blob `fd5bc69b5dedd824937d44ce6a1097066cbcc936`. Under
the frozen header it carries eleven `#check` commands and nothing else: the ten propositions frozen
above, each verbatim, and the corollary form `(P_N) → ¬ (P_R)`.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36241719499 | `9bbbde0d86b936e73287d2574431bde8b2c203fd` | the elaboration file, its import line directly after `OrbitGeometryRigidity`, a disposable census family | red at the numerical probes only. The guard's `R7-NLV` fails its wiring check, because the import split `R7-NLV`'s pinned adjacency of `OrbitGeometryRigidity` and `StrictNaturalLift`. The `Mathlib bridge` build and the release gate are green |
| 36243196377 | `ea8f9edd73ca9fc8076c0978983babcd94969961` | the same, with the import moved directly after `StrictNaturalLift` | all three jobs green. The `Mathlib bridge` build prints the eleven `#check` results and no error. The release gate passes all 21 steps |
| 36243198088 | `f521d8d4f6cc851a5872d2f474242e7e5710294c` | **the countercontrol**: the elaboration file with one deliberate defect, the first shape of `P_R` written `.submatrix τ` with one index | red, as required. The Lean kernel check and the numerical probes are green. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/OrbitIsometryClassification.lean:29:47: Type mismatch`, at that shape |

The countercontrol shows that the elaboration check has force: an ill-typed frozen statement fails
the build at its own line, and nothing else fails.

**The separation, rehearsed in the kernel.** The rehearsal module proves the frozen `S_SEP` by the
strategy recorded in the route. It has 28 theorems:
- entry and value lemmas for the Fourier tuple at `i` and `−i`;
- the conversions of the conjugated and transposed shapes;
- four core lemmas and eight bridge lemmas;
- four exponent tables over all 576 pairs;
- `S_SEP` itself.

| run | head | outcome |
| --- | --- | --- |
| 36244347747 | `43e3b7b52186593fe8ec3c2ac3f8ebbe103cdd10` | red. The four tables, proved by `decide`, reach the elaborator's limit of 200000 heartbeats in `whnf`. The designated-circle bridges fail on an unparenthesized test class. Everything else compiles, including the 64-case entry lemmas |
| 36244571105 | `bcf6ee799b42e0b0c49ffeeb3370dd0723b6a2f0` | all three jobs green. The tables are proved by `decide +kernel`. `Built OIBridge.OrbitIsometryClassification (23s)`. All 28 theorems print only `propext`, `Classical.choice` and `Quot.sound`. The release gate passes all 21 steps |

The strategy is not frozen. This evidence shows only that `S_SEP` as frozen is provable in the
kernel, in a time the build tolerates.

**The retired guard and the corrected cells, exercised in CI.**

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36244774129 | `55c72286ab31641a4a5908c7946794318cbb8e03` | the elaboration file, the retired guard (blob `d28e9b3cf2093984a1c453892204b9932a685b2e`) and the `A32-NOT-RIGID` cell (`ROADMAP.md` blob `2496ee6fad349e6d07a7dcb2fd335a8701fc0723`) | all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order. The release gate passes all 21 steps |
| 36244775311 | `120e6de20271ed67cf12b90cf0ab3e55124078a7` | the same, with the `A32-RIGID` cell (`ROADMAP.md` blob `4d64cdde5987016541390e9beac29affd5050942`) | all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order. The release gate passes all 21 steps |

Those two heads carry the cells as drafted before the final wording of this round's standing clause
(`ROADMAP.md` blobs `2496ee6fad349e6d07a7dcb2fd335a8701fc0723` and `4d64cdde5987016541390e9beac29affd5050942`). The frozen cells differ from them only in that
clause, and have blobs `ebe80f84eadb7c48e0e566f8501887e291b0ca9f` and `30f7f80f7c155752242a7d09eb9f3bbd64268ece`. The guard reads none of the text
this round appends. The local guard matrix below is run against the frozen cells.

**The native lifecycle, rehearsed locally.** Three executions were built in scratch worktrees and
never pushed, one per row. Each is a `D → F → E → Λ → Q` chain:
- `F` is this file.
- `E` is one execution commit. It carries `controls.py`, a synthetic module with the frozen
  statements (never compiled), the census family, the import line, the result note, and the surfaces
  for its row.
- `Λ` is a `--no-ff` merge of `E` into `D`.
- `Q` adds the receipt built by `tools/v3_receipt.py`, with placeholder attestations.

In all three cases:
- `controls.py check E` prints `controls: check OK`;
- `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`;
- `--receipts Q` prints `RECEIPTS  7 receipt(s), all hold`;
- `tools/legacy_records_check.py Q` prints `LEGACY  303 record(s) in 75 closed namespace(s), all intact`.

The paths changed from `D` to `E` number eight on the two decided rows and six on `A32-UNDECIDED`,
where the guard and `ROADMAP.md` are untouched. Each run matches the frozen set.

The scripts that produced this evidence, none of which is landed:

| script | SHA-256 |
| --- | --- |
| `gen_props32.py` | `57b99c06ca9307a1406b886356f970fd3dca52fa146a13d249ab178a3d090033` |
| `gen_elab32.py` | `1d64011593a4f67f5d9a3654802b6d01c54b99c0e3026feb262d8b79a1c90127` |
| `gen_sep32.py` | `53eb5bdd81be2bcfc4ed3ca85b562b7607ded8e1a8cf7398e1b74e130fe6f523` |
| `build_retire32.py` | `8bcb3941f2a91a244d49c5f3004ce3a2f82464a460e170124ad2be0234de87e8` |
| `p0_32.py` | `ad9a31edde7b96cf0086dcc2834676d350c1ad5e60bfffdc826ab3675b864b03` |
| `ctlcheck.py` | `973f36355f80552c826a6539d201cd84c9e3fc1e7a7649146f7f3614b9a86226` |
| `sepenc.py` | `223ed53fb3e45edb5f5e18d57bb06a65e535ce4201b238ac4e3ea019c679e4d8` |
| `sim_a32.py` | `be916b0087c6e38878e06a4d5c141776e15c0ce9a10c9e534ec4bec633097f05` |

***

## The question, FROZEN — one target

### `A32` — the classification at the single carrier

**At the frozen single-carrier configuration, does every map on tuples satisfy act 25's four-shape
conclusion, if it preserves realizability, is surjective on classes and preserves act 24's distance
on realizable tuples?**

The answer is reported as one of three labels:
- `A32-RIGID`, the theorem `P_R`;
- `A32-NOT-RIGID`, the theorem `P_N`, earned through the witness equations;
- `A32-UNDECIDED`.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| overlap compatibility | `a32_control_overlap` | the witness equations agree where circles meet |
| existence | `a32_shared_exists` | the statements about maps satisfying the witness equations are not vacuous |
| nontrivial motion | `a32_control_moves` | the witness is not the identity on classes |
| positive family control | `a32_control_global` | `FOUR` is satisfiable by a family member other than the identity |
| identity not separated | `a32_control_identity` | the separation does not refute the identity |
| failing-isometry countercontrol | `a32_control_quarter` | the isometry proof has force: a nearby, well-defined circle map fails it |
| duality | `a32_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`S_EXIST`.** Under `classical`, choose for each class on the Fourier circle its parameter, and
   send it to the Fourier tuple at the conjugate. Every other tuple is fixed. The choice is well
   defined because distinct unit parameters give distinct classes, and the rules agree on overlaps
   (the reading of `S_OVL`).
2. **`S_ISO`.** Every realizable tuple lies on one of the nine circles, by `iso2_classes_single` and
   `a26_1_circle_count` (iii).
   - **Realizability** is preserved by `hadamard_z_admissible` and `realizable_of_gramPhaseEquiv`.
   - **Surjectivity** holds on the Fourier circle by conjugating the parameter back, and by the
     identity elsewhere.
   - **The distance** is preserved in three cases:
     - on the Fourier circle, by `conj_isometry`;
     - off it, trivially;
     - across, by the relabelling that agrees with the map on the Fourier circle together with the
       other circle, and `relabel2_isometry`.
3. **`S_SEP`**, the rehearsed strategy, not frozen. Push the negation. Read each shape at a test class
   `C_r(i)` through a coordinate:
   - through `mixedTriple_relabel2`, `mixedTriple_star`, `mixedTriple_transpose` and
     `mixedTriple_gauge`;
   - for the transpose shapes, with the dilation `iso1_single_carrier` supplies;
   - at the parameter `i`, where every coordinate is an explicit power of `i` over `64`.

   Each of the four shapes then reduces to a congruence of exponents mod 4. The four tables of those
   congruences over all 576 pairs are proved by `decide +kernel`.
4. **The controls.**
   - `S_OVL`: at each overlap, one coordinate forces the parameter to be `±1`.
   - `S_MOVE`: the class at `i` goes to the class at `−i`, and one coordinate separates them.
   - `S_GLOBAL`: by `iso1_single_carrier` and `conj_isometry`, and the second shape at `(1, 1)`.
   - `S_ID`: directly, and the first shape at `(1, 1)`.
   - `S_QUARTER`: existence as in step 1. For the failure, take a class of another circle close to a
     class the quarter-turn moves. `coord_le_dist` bounds one distance below and `fourier_dist_le`
     bounds the other above.
5. **`a32_not_rigid`** from `S_EXIST`, `S_ISO` and `S_SEP`.
6. **`a32_c_exclusive`**: `P_R` applied to `P_N`'s witness contradicts its `¬ FOUR`.

No route to `A32-RIGID` is expected. The freeze's reading is that `P_R` is false.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| `a32_shared_exists`, `a32_shared_isometry`, `a32_shared_separation` | either verdict theorem; `a32_c_exclusive` |
| every `a32_control_…` | either verdict theorem; `a32_c_exclusive` |
| `a32_rigid` | `a32_shared_exists`, `a32_shared_isometry`, `a32_shared_separation` |
| `a32_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A32` | `A32-NOT-RIGID` | **very high** | the witness preserves every distance and is none of the 2304 words, both checked exactly; the separation was rehearsed in the kernel before the freeze |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A32-RIGID`

> At the frozen single-carrier configuration, every map on tuples that preserves realizability, is surjective on classes and preserves act 24's distance on realizable tuples satisfies act 25's four-shape conclusion, at evidence level 2. This is a classification of the surjective isometries of the normalized space at that configuration; it adopts no isometry as a symmetry, a principle or a law.

### `A32-NOT-RIGID`

> At the frozen single-carrier configuration, the positive classification proposition posed as act 25's `ISO3` is false, at evidence level 2: a map that conjugates the Fourier parameter on the Fourier circle and fixes the class of every point of the other eight relabelled Fourier circles preserves realizability, is surjective on classes and preserves act 24's distance on realizable tuples, and for no pair of relabellings does it satisfy any of the four shapes. This is a statement about the frozen space and the frozen family; it adopts no isometry as a symmetry, a principle or a law, and it leaves act 25's and act 26's recorded verdicts as those rounds recorded them.

### `A32-UNDECIDED`

> Neither the classification nor its negation was obtained. The step at which the proof stopped is named, with what would settle it.

### The corollary, REQUIRED

`a32_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label.

| row | outcome |
| --- | --- |
| 1 | `A32-RIGID` |
| 2 | `A32-NOT-RIGID` |
| 3 | `A32-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` carries this clause twice, once in act 25's
sentence and once in act 26's:

> Whether every surjective isometry of the normalized space at that configuration belongs to the family is recorded undecided, with the step named; no isometry outside the family is exhibited, and the absence of a proof is not a counterexample.

The cell ends with act 30's sentence and its standing clause:

> At the product configuration, the ladder's conditions through factorization admit every pair of local class bijections: each such pair is the class action of the factor families of a single law carrying all of them, so those conditions do not select among local behaviours. `P0`'s threading part is untouched, no carrier is adopted as the physical one, no surviving law is adopted as the physical one, and nothing here names, endorses or excludes a selection principle.

**On a decided outcome**, each occurrence of that clause is removed; the rest of act 25's and act
26's sentences stands. Then this round's sentence for the case is appended once after act 30's
standing clause, followed by its standing clause:
- **`A32-NOT-RIGID`:**

  > At the single-carrier configuration, the positive classification proposition posed as act 25's `ISO3` is false: the map that conjugates the Fourier parameter on the Fourier circle and fixes the class of every point of the other eight relabelled Fourier circles preserves realizability, is surjective on classes and preserves the distance, and for no pair of relabellings does it satisfy any of the four shapes of act 25's family. `P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

- **`A32-RIGID`:**

  > At the single-carrier configuration, every surjective isometry of the normalized space belongs, on realizable classes, to act 25's finite family. `P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On `A32-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that correction, or `D`'s unchanged, byte for byte.
Rehearsed at `D`, the two decided cells give these blobs:
- `ebe80f84eadb7c48e0e566f8501887e291b0ca9f` (`A32-NOT-RIGID`);
- `30f7f80f7c155752242a7d09eb9f3bbd64268ece` (`A32-RIGID`).

## Acts 25 and 26 cease to own the current wording of that clause — the frozen retirement, on a decided `A32` only

**What is retired.** Retired is the authority of `R7-OGC` and `R7-CGR` over the **current** wording of
the `P0` cell, which consists of:
- each contract's read of `verification/ROADMAP.md`;
- the four `ROADMAP` conjuncts of each contract's `P0` predicate: the sentence in the `ROADMAP`, the
  previous act's sentence in the `ROADMAP`, their order, and the row's `OPEN` label;
- each contract's `ROADMAP` mutation control;
- the phrase of each check description that says the `ROADMAP` is read.

**Reachability and physical presence are retired together.** Every retired line is deleted, and
nothing is deleted that the ledger below does not name. No deletion is inferred from dead code.

**What is kept byte-identical.** Every other byte of the guard is kept.
- Both checks stay under their tags, in their places, and must pass.
- Each keeps its module, wiring, statement and mutation checks, and its `P0` predicate's
  result-note conjuncts: the frozen sentence in the round's own result note, and the case text there.
- Act 27's `R7-NLV` is untouched. It reads the `P0` row only for act 27's sentence, the prefix
  `Act 26 tests,` before it, and the `OPEN` label, and each of these survives the correction.

**The ledger, FROZEN.** Each entry is an exact splice of the guard at `D`: its old text occurs there
exactly once, and it is replaced by the new text. The full old and new texts are carried in
`controls.py` and reproduced by it; their SHA-256 digests are frozen here.

| entry | what it removes or rewrites | old text, SHA-256 | new text, SHA-256 |
| --- | --- | --- | --- |
| `ogc-road-read` | R7-OGC's read of verification/ROADMAP.md, read only by its ROADMAP conjuncts and mutation | `3c7549bb4a6f4973d285ea607b705ce26ee199ce7c20bbda65ab44738d6efe8d` | empty, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `ogc-p0-road-conjuncts` | R7-OGC's P0 predicate, less its ROADMAP parameter and its four ROADMAP conjuncts; its result-note conjuncts unchanged | `860ae7d978c6be9cf83606a0638145ecfc2fe622d1b055cc9c44651a9132b54f` | `203b6d9e59b093084ad400437c726c2b9a8c4d78c932ef4110960e184312331e` |
| `ogc-road-mut` | R7-OGC's ROADMAP mutation control | `4315f96a0318a2a5508676ea60b7391c696fe25fcc89404648a47e068edda810` | empty, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `ogc-description` | R7-OGC's check description, with the ROADMAP reading replaced by the result-note reading it keeps | `5320c62b5610e080fc28a6bac0d32c4a7da2113b5e42b8e138b18320bdd247e7` | `e7a0faaae2f1efc7c63dc16bf6379c05d02f721e047187b6b7e82788c9a462b6` |
| `cgr-road-read` | R7-CGR's read of verification/ROADMAP.md, read only by its ROADMAP conjuncts and mutation | `a6accd67df91aa2d87d10abee56ef9d3c18a9b8d584057e2a4990a3060f8bc3f` | empty, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `cgr-p0-road-conjuncts` | R7-CGR's P0 predicate, less its ROADMAP parameter and its four ROADMAP conjuncts; its result-note conjuncts unchanged | `649c99cd0b5629fa484febb385e24f1c73041d5bee4b349b5443ed64a89f5fc7` | `7b1c9f33ad8cb53511cda51903120602d3de30e5a5d8ba3e0c44be9510c861b4` |
| `cgr-road-mut` | R7-CGR's ROADMAP mutation control | `6ce19663c1bf483978b3f91e262923bff85753d50e5abaae725b9150739a96f5` | empty, `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `cgr-description` | R7-CGR's check description, with the ROADMAP reading replaced by the result-note reading it keeps | `9d1f877ee780db43985f3868b28aa596a4868027d64acec06ebd90f5c6a2ca9a` | `96c58a32c1cb17b79f2e5a7c2af20ee9757f594665beeacf208f36744d671aa2` |

Applied in order to the guard at `D` (blob `0475fe3d8c5724a7bf918bf3fd75ae06370cef26`), the ledger gives the retired guard,
blob **`d28e9b3cf2093984a1c453892204b9932a685b2e`**. It is 11 lines shorter and compiles. On a decided `A32` the guard
at `E` is exactly that blob; on `A32-UNDECIDED` it is exactly `D`'s. The result note lists the
retired legs by their ledger names.

The retired guard references none of the bindings the ledger removes: `_OGCROAD`, `_CGRROAD`,
`_ogc_m11` and `_cgr_m11`. `controls.py` checks this, and a mutation that references one must fail it.

**Rehearsed at `D`, locally** (design evidence, not attestation; the dispatch runs are recorded
above):

| guard | `ROADMAP.md` | verdict |
| --- | --- | --- |
| retired | `A32-NOT-RIGID` cell | 91 PASS, 0 FAIL, the tags in `D`'s order |
| retired | `A32-RIGID` cell | 91 PASS, 0 FAIL, the tags in `D`'s order |
| retired | `D`'s cell | 91 PASS, 0 FAIL, the tags in `D`'s order |
| `D`'s | `A32-NOT-RIGID` cell | 89 PASS, 2 FAIL: `R7-OGC` and `R7-CGR` |
| `D`'s | `A32-RIGID` cell | 89 PASS, 2 FAIL: `R7-OGC` and `R7-CGR` |

The last two rows are the countercontrol. They show two things:
- a corrected cell cannot land under `D`'s guard;
- the legs the ledger retires are exactly the legs that fail.

***

## What no outcome licenses

- **No outcome revises act 25's `ISO3-UNDECIDED` or act 26's `A26-2-UNDECIDED`.** Those are the
  verdicts those rounds recorded, and they stand.
- **No outcome is written as "the symmetries are the family".** An isometry of the normalized space
  is not adopted as a symmetry, a principle or a law.
- **No outcome reports anything at the product configuration**, and none reports act 26's
  `A26-2-P` or `A26-3`.
- **No outcome reports anything about transition families or dynamics**, and none closes `P0`,
  which stays `OPEN`.
- **The witness is not called canonical, unique, continuous or physical.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit any guard contract beyond the frozen ledger;
- write any manuscript file;
- read any object of act 31.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within `propext`,
`Classical.choice` and `Quot.sound`.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/controls.py`, blob
**`43ba5c18bf2d0ca44fb97f074edeaf0c713a7074`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against, and the retirement ledger in full.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` and `P_N` are exactly the universal and existential forms rebuilt from the
    shared components.
  - Every other statement carries the one hypothesis text, the one four-shape text, the one
    distance conjunct, the one witness text and the one quarter-turn text, verbatim.
  - `S_QUARTER` opens with its existence conjunct.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a32_shared_…`;
  - gives each frozen theorem its frozen statement;
  - has at most one verdict theorem, and `a32_c_exclusive`;
  - carries the statements the earned label requires.
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires;
  - on a decided outcome, every ledger entry by name.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen correction for the case, or to `D`'s.
- **The guard** is byte-identical to the ledger applied to `D`'s, or to `D`'s, for the case.
  - The ledger applied to `D`'s guard reproduces blob `d28e9b3cf2093984a1c453892204b9932a685b2e`.
  - On a decided outcome, no removed binding is referenced.
- **The census** is `D`'s with exactly one family appended, last, for `OrbitIsometryClassification`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.OrbitIsometryClassification` inserted directly
  after `import OIBridge.StrictNaturalLift`. That keeps `R7-NLV`'s pinned adjacency of
  `OrbitGeometryRigidity` and `StrictNaturalLift`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files and the module;
  - modified: `OIBridge.lean` and the census;
  - modified on a decided outcome only: `ROADMAP.md` and the guard.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 9 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies 54 mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 9 duality mutations fail as required
controls: 3 rows hold as frozen, 54 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module and the controls.**
   - `controls.py` with its frozen blob.
   - The module with the frozen header and its shared lemmas. On the route to `A32-NOT-RIGID` these
     include `S_EXIST`, `S_ISO`, `S_SEP` and the five controls.
   - The import line.

   No verdict theorem and no corollary.
2. **Stage 2 — the verdict.** `a32_not_rigid` or `a32_rigid`, or neither, and `a32_c_exclusive`.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last. On a decided
   outcome only, the `P0` cell for the case and the guard as the ledger gives it.
4. **The result note** `result.md`, whose commit is `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40). A stage whose build fails is followed by a fixing
commit, never rewritten. The label is read from the module at `E`.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the frozen propositions elaborate as frozen | before `F`: the elaboration run above; at `E`: `C8`, every frozen theorem compiled under its statement |
| every verdict and control is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary, controls and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces and the guard are exactly the frozen ones for the case | `C9` |
| the guard stays green | `C8`: 91 checks, all `PASS`, in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen propositions unchanged** is repaired by later
  linear commits before `E`.
- **A verdict that cannot be obtained** is reported `A32-UNDECIDED`, with the step named. In that
  case the guard and `ROADMAP.md` are not touched.
- **A decided label whose required controls are not all proved** is not reported; it is
  `A32-UNDECIDED` with the missing control named. A verdict prints only over green controls.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is either of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken.

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
