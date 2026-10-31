# SUBSTATE-2 unit F2-1 — amendment A★-1: elaboration context only

**Status: append-only, context-only amendment.** It amends `A-star.md` (frozen at `b86f0547`,
sha256 `3d84c2054872046bdff88b52ba5ba7dfaa86bf5519fbf2e36d94efb25fdd5b05`) under the owner's bounded-recovery authorization in PR
#1011, comment 6546214912 (amaybaum, OWNER), step 1. It changes no statement, definition,
hypothesis, control, self-test, expected output or decision logic. It runs nothing, builds
nothing, and does not touch the Lean module, `stage2/controls.py` or any other file. It takes
effect as evidence only after an independent reviewer accepts this exact commit.

## A★-1.1 The earlier stage-2 attempt stays as it is

- **The attempt.** Stage 2 at `05ecc8732160736b538b422114a5a1738d682c16`, with its ordinary PR CI
  run 41220197866, failed its Lean `Build` step. Under the frozen rule (prereg §4, clause 0(v)) its
  outcome is `INCONCLUSIVE (void)`.
- **Preserved unchanged.** That outcome, the run record and the files of that commit, including
  `stage2/results.json`, `stage2/RESULT.md` and `stage2/controls.py`. They are not overwritten or
  relabelled.

## A★-1.2 The context change

A★ §A★5 fixes the elaboration context of its 19 statements as the two lines

```lean
open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion
```

That context omits `open Matrix`. The statements use two scoped notations of the `Matrix` namespace:
- `ᴴ`, for `Matrix.conjTranspose`, in `OnesBounded` and `fullTheory_rotDagger`;
- `*ᵥ`, for `Matrix.mulVec`, in `OnesBounded` and `rot_moves_ones`.

These do not parse without `open Matrix`. The corrected context is A★'s two lines followed by
`open Matrix`:

```lean
open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion
open Matrix
```

Nothing else changes. The statement block below is A★'s block with exactly that one line inserted
after `open OperationalAssembly MonoidalCompletion`. Deleting the line gives A★'s block byte for
byte.

## A★-1.3 The 19 fixed statements, unchanged

The statements below were extracted programmatically from `A-star.md`, using the same rule as
`stage2/controls.py`'s `astar_statements`:
- take the first `lean` block;
- start a new declaration at each line beginning `def ` or `theorem `;
- keep its non-empty continuation lines;
- join them with `\n` and strip trailing whitespace.

The block is written here from those extracted bytes, so the same extraction applied to this file's
third `lean` block, the statement block, returns the same 19 strings. Each digest is the sha256 of the UTF-8 statement string. Every digest
equals the `statement_sha256` recorded for that declaration in the preserved
`stage2/results.json` of `05ecc873`. The combined digest is the sha256 of the 19 strings joined by
`\n\n`: `ee8a6ce6bbc2badf86d86dc808b17d2d7db987698b01df647a119febfbb0f5a3`.

| # | Declaration | sha256 |
|---|---|---|
| 1 | `OnesBounded` | `ca5a780aef401ef352a4d94c5045aedc75d16a37f6e5c24ea0e761b762affc79` |
| 2 | `rot_not_preservesNonneg` | `9f8f95080d250efa528ae9db248f849a886a348eb5942a4efad638a502744550` |
| 3 | `rot_moves_ones` | `5632c158fa1c1887c45a1b05540bf162a27d84a82b05390ddd689128206d6e2e` |
| 4 | `falsifierUnavailable_of_nonnegBounded` | `aab60341150c338d416a4531023fd90b00589d8940bfff9ae7e8460611041528` |
| 5 | `falsifierUnavailable_of_onesBounded` | `daa04869a79f782c79502253d37608e6a4feb493af0c4e350e050ab302cab695` |
| 6 | `onesBounded_of_onesFixing` | `0fd3fa9b489e3b0f09cb829a54fa1946b65a7918dd3d458e4fa0175abffe9dec` |
| 7 | `permTheory_onesBounded` | `4445000e19eeecbb6570455bef79ecc1de8193c7669a782a4c941dbb2e32a66a` |
| 8 | `onesTheory_falsifierUnavailable` | `1d12f11ba87c988907463e0f7d7a2c70365ebc4fcd1cf79cf2a4e692d7550703` |
| 9 | `nonnegClass` | `0442e82e1febdfe0062677902c5857f06b5877508d22fc6a2dca2a252809e1e2` |
| 10 | `nonnegClass_arch` | `8b0f3899e3ae902edf8a5b7c009ae291093a7f979159dc60ce43065fdf4b1a5a` |
| 11 | `nonnegClass_nonnegBounded` | `2ba9a7adcb1e84896853044a24479a6dd4e230efe2768ef95ec160e97f015162` |
| 12 | `nonnegClass_onesFixing` | `38778839677136914faa94da81166a5e219303ada81497ef1a57fa0c8049fe68` |
| 13 | `realClass` | `24a871a5b99105b22db0606298a80123dc61322974b40bbc43a90c63f233716a` |
| 14 | `realClass_arch` | `e9b667c38e423195347c0f02ddbaad7d4d718acef0de3e859de0718365f3fdd7` |
| 15 | `realTheory_rot` | `ff2463bead80562b2ebf649680556b9f8fb10fc639deda7054548f5044103fed` |
| 16 | `realTheory_not_phases` | `72fbf03898979884713e3a1f2b1480748fbcb8c684f9b497a6f2b909a8565f59` |
| 17 | `fullTheory_rot` | `aa7d163085000219847fe36a95141d6e587de040dc3db71fe87557bb61fe5a64` |
| 18 | `fullTheory_rotDagger` | `1a14a6a3d6562d38515f64c5184c030689769733c4bf79ebbe02940ad7a8c64f` |
| 19 | `fullTheory_phases` | `44896c9e71b69b2d6688a00bf63c23d7665a190a846c1c86db1db2963246963d` |

```lean
open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion
open Matrix

def OnesBounded {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 →
    T.availExt n Unit (fun _ => conjChannel U) →
      ∃ z : ℂ, U *ᵥ InstrumentRealization.ones (A × Fin n) = z • InstrumentRealization.ones (A × Fin n)
theorem rot_not_preservesNonneg :
    ¬ SubstratumInterfaceAudit.PreservesNonneg (conjChannel DiagonalTheory.rot)
theorem rot_moves_ones :
    ¬ ∃ z : ℂ, DiagonalTheory.rot *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = z • InstrumentRealization.ones (Fin 2 × Fin 1)
theorem falsifierUnavailable_of_nonnegBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : FrozenSourcing.NonnegBounded T) : RouteB.FalsifierUnavailable T
theorem falsifierUnavailable_of_onesBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : OnesBounded T) : RouteB.FalsifierUnavailable T
theorem onesBounded_of_onesFixing {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hf : InstrumentRealization.OnesFixing 𝓘) {A : Type} [Fintype A] [DecidableEq A] :
    OnesBounded (InterventionLocality.genTheory 𝓘 arch A)
theorem permTheory_onesBounded : OnesBounded (SubstratumInterfaceAudit.permTheory (Fin 2))
theorem onesTheory_falsifierUnavailable : RouteB.FalsifierUnavailable (FlowEndpoint.onesTheory (Fin 2))
def nonnegClass : InterventionLocality.ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℂ), ‖a‖ ≤ 1 ∧ (∀ i j, (0 : ℂ) ≤ M i j) ∧ K = a • M
theorem nonnegClass_arch : InterventionLocality.Architecture nonnegClass
theorem nonnegClass_nonnegBounded {A : Type} [Fintype A] [DecidableEq A] :
    FrozenSourcing.NonnegBounded (InterventionLocality.genTheory nonnegClass nonnegClass_arch A)
theorem nonnegClass_onesFixing : InstrumentRealization.OnesFixing nonnegClass
def realClass : InterventionLocality.ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℝ), ‖a‖ ≤ 1 ∧ K = a • M.map (fun x => (x : ℂ))
theorem realClass_arch : InterventionLocality.Architecture realClass
theorem realTheory_rot :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory realClass realClass_arch (Fin 2))
theorem realTheory_not_phases :
    ¬ RouteB.PhasesAvailable (InterventionLocality.genTheory realClass realClass_arch (Fin 2))
theorem fullTheory_rot :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2))
theorem fullTheory_rotDagger :
    (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel DiagonalTheory.rotᴴ)
theorem fullTheory_phases :
    RouteB.PhasesAvailable (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2))
```

**Verification recipe** (from the repository root, `python3 -I`):
- Extract the statements from `A-star.md` (its first `lean` block) and from this file (its third
  `lean` block) with the rule above, and require the two lists of 19 strings to be equal.
- Require each string's sha256 to match the table.
- Require `A-star.md`'s sha256 to equal the value stated at the top of this file.
- Require this file's `lean` statement block, with the `open Matrix` line removed, to equal
  A★'s block byte for byte.

## A★-1.4 What the separate step-2 attempt will contain

This section describes; nothing is executed under this amendment. Step 2 needs the independent
acceptance of this commit, then the owner-authorized proof-only repair.

- **Lean module.** `OIBridge/F2CoherenceControls.lean` gets `open Matrix` in its context, as
  fixed here. It also gets the proof-only repairs the authorization names:
  - `realClass_arch.block`: a type-correct real block construction, replacing the complex
    `AncillaClosure.ancBlock` applied to a real matrix;
  - the `simp` that makes no progress.

  Strictly necessary dependent tactic corrections may follow from these. No statement text,
  definition, hypothesis or declaration meaning changes, and there is no `sorry`, `admit`, new
  axiom or weakening. Any other substantive defect stops the work pending fresh authorization.
- **A new results file.** It is written at `stage2/run-2/results.json`, beside the preserved
  `stage2/results.json`, with its own note and its own CI record.
- **The only permitted output differences** from the preserved `stage2/results.json`:
  - run-specific metadata: the run directory, commit and CI identifiers, and the amendment
    reference;
  - the build-status and kernel fields: each declaration's `build_step` and `axiom_check_step`,
    and the resulting `token` and `verdict_status`;
  - the sha256 of this file, `A-star-1.md`, bound into `controls.py`'s freeze check as the
    reviewer required, beside the existing digests of the preregistration, A★ and the stage-1 log.

  Every other control, mutation, self-test and exact value must reproduce byte for byte.
