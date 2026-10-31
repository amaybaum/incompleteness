# PC-1 — amendment PC-S2: stage 2, controls only

**Status: append-only amendment. It executes nothing.** It fixes the controls-only stage 2 that the
owner authorized in PR #1022 comment 6547077354 (amaybaum, OWNER), Decision 2. Execution may begin
only after an independent review of this exact commit is accepted. It changes no earlier file.

**Frozen inputs.** Each is recorded by git blob and sha256 at `89a8feba039303d26e4d1c280f2ee082e290ace9`.

| File | Blob | sha256 | Last commit |
|---|---|---|---|
| `preregistration.md` | `414f31686e7890117abaa599b7e7ef18b7049ae8` | `9754d93187b8ffc68645f4873247aaac73dc26b78880a05dec0b3ef5b8ee87fc` | `948b30c1` |
| `amendments/PC-star.md` | `79aad250aa63558c18739d94ba114baced78ca1d` | `97e3567e1303ccda1698f9f19dad069f3bbbf93013021dd281a4751f643532b6` | `72b4af27` |
| `amendments/stage1-log.json` | `744c28c88d31176847c55d89946670706bb39a02` | `6f2b74b70dd2d589c3a24975c3ee1d924c296ccf00d72b0d63b8c65d434aa3ab` | `9245d542` |
| `amendments/PC-star-disposition.md` | `a94c531b2e8cedf5fc8b05848bcd41e1cc6b3cf0` | `4dac1d3599740af6621138b64e071dba48963ab9974e661bc544fef533c77207` | `89a8feba` |

**Scope.** Stage 2 runs only:
- the reference controls of the preregistration's §9;
- the mutations M1–M17 of §10;
- the decision-function self-test of §10;
- the fixed Lean statements below.

**What stage 2 does not run.**
- No candidate is frozen (PC★), so no probe is run: there is no `C` to transplant. The
  candidate-dependent rows (2's probe and held-out triggers for `Π★`, and 4–8) are exercised only by
  synthetic self-test files.
- No `R`, `P`, `P₁`, `Gauge`, §7 value or held-out outcome is computed on a new or previously
  rejected candidate (F2-1's 13 rules, Q1–Q12). There is no re-screen.
- The §7 values are computed only for the positive control C7 (exact QM) and the classical control
  C10, as the frozen controls require.

***

## S2-1. The token: two tracks, encoded in data

The owner's Decision 1 (`PC-star-disposition.md`) fixes the strict stage-1 token at
`INCONCLUSIVE (void)` under clause 0(vi), and carries the scientific stage-1 finding only under a
disclosed one-time exception. Stage 2 cannot change either.

- The results file carries `stage1.forbidden_precomputation: true`, with its source (the
  disposition file's path and sha256, and the owner comment id). The unit decision function reads
  this field. It is not a constant in code: M9 and the self-test of S2-5 check this.
- `token` is always `"INCONCLUSIVE (void)"`. `void_reasons` starts with `"0(vi)"` and gains a
  further entry for every failed stage-2 clause-0 check: 0(i) control, mutation or self-test; 0(ii)
  freeze; 0(iv) float; 0(v) kernel step or axiom check.
- `scientific_finding` is a separate field. It is never a second token, and its text never uses
  the gap token's name.

  ```
  "scientific_finding": {
    "statement": "No admissible candidate among the 25 screened (F2-1's 13 rules and Q1–Q12); the
                  obstruction is G★ item 3 for native couplings: A★2 premise (ii) is broken by no
                  native source.",
    "scope": "PC★ §PC★4: couplings whose joint process is a classical measurable bijection with
              function-valued records; the sources at 5914c17c and the named branches; not a no-go.",
    "exception": "PR #1022 comment 6547077354",
    "status": "carried under exception" | "withheld: <void reasons beyond 0(vi)>" |
              "pending exact-head review",
    "review": null | {"reviewer": …, "time": …, "head": …, "quote": …}
  }
  ```

  The status is `carried under exception` only when every stage-2 clause-0 check passes, both
  kernel steps succeed, and the independent exact-head review is recorded. If any stage-2 check
  fails, it is `withheld`, with the failing checkpoints named.
- There are two decision functions, kept apart.
  - `decide_row(record)` implements §6 unchanged, rows 0–10, for synthetic records and control
    records. A synthetic row-1 record yields the gap token as a self-test output. It is written
    only to `selftest`, never to `token`.
  - `unit_token(results)` produces `token`, `void_reasons` and `scientific_finding`. It never
    returns the gap token.

## S2-2. The F2-1 dependency: byte-identical vendoring, checked by blob id

**Strategy.** The files stage 2 needs from the unmerged branch `research/substate-2-recursive-20261030`
are copied byte for byte into this branch from the pinned commit
`4e7ddb70749e7ee49f43f5af2707a84524d1226a`. At run time, the script checks each copy by computing
its git blob id (`sha1("blob <len>\0" + bytes)`) and comparing it with the id fixed here. Neither
the build nor the run reads the unmerged branch. A reviewer checks the ids with
`git rev-parse 4e7ddb70:<path>`.

| Source path at `4e7ddb70` | Destination on this branch | Blob | sha256 |
|---|---|---|---|
| `verification/lean-mathlib/OIBridge/F2CoherenceControls.lean` | same path | `fbf475043ce589ccf1bfac511898eda821636137` | `66ab7a9c96e7eda9385a08208483164f65621a064cb9b2167e40d2783c092897` |
| `…/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py` | `stage2/vendor/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py` | `18c519f3a423db7506d1438b8ef22a9ca847e481` | `7994448e707373cb0f64c5cc262508d1d61c7703b2783f3b64b1fbf1625dc09f` |
| `…/recursive-substates/fixed-scale-skew/fixed_scale_probe.py` | `stage2/vendor/recursive-substates/fixed-scale-skew/fixed_scale_probe.py` | `313c2f80476d3d464b75f3b98ed48379959b5ac6` | `524c599e89282f7d1d9e95f60f1a36d4cff630afdac464cbea3057276bf39f8c` |
| `…/recursive-substates/native-padic-bridge/native_padic_probe.py` | `stage2/vendor/recursive-substates/native-padic-bridge/native_padic_probe.py` | `0bdb22325d44394bbaa590581a71bc13e6d62608` | `72ff1a1bc5cc8cab9fb72bc46d5e2301216972fef682847380fb4063a29c092c` |

`stage2/` is relative to the PC-1 unit directory. In the table, `…` stands for
`verification/programmes/substratum`.

**Why this strategy.**
- **The Lean module.** It is vendored whole, rather than its 19 statements being restated with
  re-written proofs. Its exact bytes built green in ordinary draft-PR CI at PR head `1d345126`
  (run 41221595790, `Build` and `Release gate` both `success`, F2-1 run-2 RESULT). So statement
  identity is a byte identity, and no proof is re-authored. The 19 statements keep A★-1.3's digests
  (combined `ee8a6ce6bbc2badf86d86dc808b17d2d7db987698b01df647a119febfbb0f5a3`) and their
  `open Matrix` context, by blob identity. If both branches later land, the two additions are the
  same blob.
- **The Python copies.** They keep their relative layout, so that F2-1's path constants
  (`UNIT = HERE.parent.parent`, `SUBSTATE2 = UNIT.parent`) resolve inside `vendor/`. Its C2 and C9
  then load the vendored probes. Only F2-1's functions and helpers are imported. Its `main`,
  `build`, `kernel_map` and `astar_statements` are not called, because they read paths that do not
  exist in the vendored tree. The two probes import only the standard library.
- **Known risk.** `main` has moved since `1d345126`. A cited declaration that changed would fail the
  build. That would be 0(v) evidence, logged and not repaired (S2-7).

## S2-3. The Lean statements

**Files the execution changes on this branch.** No other path may change.
1. `verification/lean-mathlib/OIBridge/F2CoherenceControls.lean`: the vendored copy (S2-2).
2. `verification/lean-mathlib/OIBridge/PC1Controls.lean`: new; module `OIBridge.PC1Controls`.
3. `verification/lean-mathlib/OIBridge.lean`: two import lines only, `import OIBridge.F2CoherenceControls`
   and `import OIBridge.PC1Controls`.
4. `verification/lean-manuscript-census.json`: two entries, both `"status": "kernel-only"` and
   `"manuscript": []`.
   - F2-1's entry, byte-identical to the one added at `05ecc873`.
   - A PC-1 entry: name `"PC-1 stage-2 kernel controls (research)"`, modules `["PC1Controls"]`.
     Its note states the content of the statements below, and that it makes no manuscript, sourcing
     or no-go claim.

Every other `OIBridge` module stays blob-identical to `5914c17c`.

**The complete context of `PC1Controls.lean`.** The module is:
- the header block below;
- the fixed statements, in order, with proofs (proofs are not fixed);
- one `#print axioms OIBridge.PC1Controls.<name>` line per theorem, after the namespaces close;
- the closing lines `end PC1Controls` and `end OIBridge`.

Auxiliary lemmas are allowed only if named `aux_*`. They are not fixed statements and are not
evidence.

**Extraction rule.** Take the first `lean` block of this file. A new declaration starts at each
line beginning `def `, `noncomputable def ` or `theorem `. Keep its non-empty continuation lines,
join them with `\n`, and strip trailing whitespace. Lines before the first declaration are the
header. The run requires the header and each statement to occur verbatim in `PC1Controls.lean`,
and records each statement's sha256.

```lean
import OIBridge.F2CoherenceControls

namespace OIBridge
namespace PC1Controls

open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion
open Matrix

noncomputable def gaugeD : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.diagonal fun p => if p.1 = 0 then 1 else Complex.I
theorem gaugeD_unitary : gaugeDᴴ * gaugeD = 1
theorem gauged_rot_fixes_ones :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) • InstrumentRealization.ones (Fin 2 × Fin 1)
theorem gauged_rot_mem_onesClass :
    InstrumentRealization.onesClass (Fin 2 × Fin 1) (gaugeDᴴ * DiagonalTheory.rot * gaugeD)
theorem scaled_rot_not_gauge_nonneg :
    ¬ ∃ (d : Fin 2 × Fin 1 → ℂ) (c a : ℂ) (M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ),
      c ≠ 0 ∧ (∀ p, ‖d p‖ = 1) ∧ (∀ i j, (0 : ℂ) ≤ M i j) ∧
        (Matrix.diagonal d)ᴴ * (c • DiagonalTheory.rot) * Matrix.diagonal d = a • M
theorem not_p1_of_nonnegBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : FrozenSourcing.NonnegBounded T) :
    ¬ T.availExt 1 Unit (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1))))
theorem not_p1_of_onesBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : F2CoherenceControls.OnesBounded T) :
    ¬ T.availExt 1 Unit (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1))))
theorem permTheory_onesBounded_all {A : Type} [Fintype A] [DecidableEq A] :
    F2CoherenceControls.OnesBounded (SubstratumInterfaceAudit.permTheory A)
theorem permTheory_not_p1 :
    ¬ (SubstratumInterfaceAudit.permTheory (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1))))
theorem permTheory_not_gauged_rot :
    ¬ (SubstratumInterfaceAudit.permTheory (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (gaugeDᴴ * DiagonalTheory.rot * gaugeD))
theorem falsifier_available_of_mem {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘) (h : 𝓘 (Fin 2 × Fin 1) DiagonalTheory.rot) :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory 𝓘 arch (Fin 2))
theorem rot_mem_realClass : F2CoherenceControls.realClass (Fin 2 × Fin 1) DiagonalTheory.rot
theorem realSubclass_not_p1 {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K →
      F2CoherenceControls.realClass S K) :
    ¬ (InterventionLocality.genTheory 𝓘 arch (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1))))
theorem realSubclass_not_phases {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K →
      F2CoherenceControls.realClass S K) :
    ¬ RouteB.PhasesAvailable (InterventionLocality.genTheory 𝓘 arch (Fin 2))
```

That is 14 declarations: 1 `def` and 13 theorems. Together with the 19 vendored F2-1 statements
(3 `def`s and 16 theorems), there are 33 fixed statements in two modules.

**The names the statements rely on, checked present at `5914c17c`.**
- `DiagonalTheory.rot`: `DiagonalTheory.lean:368`.
- `InstrumentRealization.ones` and `InstrumentRealization.onesClass`: `InstrumentRealization.lean:446`.
- `FrozenSourcing.NonnegBounded`: `FrozenSourcing.lean:65`.
- `LieRankSource.phaseGate`: `LieRankSource.lean:209`.
- `SubstratumInterfaceAudit.permTheory`: `SubstratumInterfaceAudit.lean:606`.
- `InterventionLocality.ImplementationClass`, `InterventionLocality.Architecture`
  (`ImplementationLocality.lean:506`) and `InterventionLocality.genTheory` (`:852`).
- `RouteB.FalsifierUnavailable` (`RouteB.lean:179`) and `RouteB.PhasesAvailable` (`:132`).
- `F2CoherenceControls.OnesBounded` and `F2CoherenceControls.realClass`, from the vendored module.

The `hle` binder copies the form of `genTheory_mono`'s hypothesis (`ImplementationLocality.lean:920`).

**Which statement serves which control.**

| Statement | Serves |
|---|---|
| `gaugeD_unitary`, `gauged_rot_fixes_ones`, `gauged_rot_mem_onesClass` | PC-F1; C15 (`Gauge_O` fails) |
| `scaled_rot_not_gauge_nonneg` | `Gauge_N` necessary for `R` at level one (through the Kraus bridge); C15 |
| `not_p1_of_nonnegBounded`, `not_p1_of_onesBounded` | `¬P₁` for C1, C2, C4, C10, C11a and C14 |
| `permTheory_onesBounded_all` | C11a on `Fin 3` and `Fin 4` (`O`) |
| `permTheory_not_p1`, `permTheory_not_gauged_rot` | C12, with the transport of S2-4 |
| `falsifier_available_of_mem`, `rot_mem_realClass`, `realSubclass_not_p1`, `realSubclass_not_phases` | C15 (`R`, `¬P₁`, `¬P`); C13 (`¬P₁`) |

## S2-4. The controls and their reference expectations (§9, unchanged)

Every control is a non-candidate. Its record has L1 `not met`, and its row comes from
`decide_row`. "Kernel" means a fixed statement, or a declaration cited at `5914c17c`, entering only
through CI step conclusions (S2-7). "Exact" means `python3 -I`, with `fractions`, Gaussian
rationals, and `ℚ(√3)` or `ℚ(√−3)`, and no floats.

| ID | Model or object, fixed here | Reference (frozen) | Evidence |
|---|---|---|---|
| C1 | F2-1 `c1()` (vendored): the odometer and Θ-K compressions for `m ≤ 6` | row 9; `N`, `O`, `¬R`, `¬P₁` | exact containment; kernel `nonnegClass_nonnegBounded`, `falsifierUnavailable_of_nonnegBounded`, `not_p1_of_nonnegBounded` |
| C2 | F2-1 `c2()` (vendored: B1, B2, FIXED-SCALE, XOR truncations) | row 9; coherent and dephased returns both 1 | as C1 |
| C3 | `substratumTheory` | row 3(a): `P`, `¬R`; screen flags `phaseOperator` | kernel `substratumTheory_derivedOI`, `substratumTheory_falsifierUnavailable` |
| C4 | `onesTheory` | row 9; `O`, `¬R`, `¬P₁` | kernel `onesTheory_falsifierUnavailable`, `onesBounded_of_onesFixing`, `not_p1_of_onesBounded` |
| C5 | obstruction lemmas | all built green; any record with `R ∧ N` or `R ∧ O` voids | kernel |
| C6 | F2-1 `c6_odometer()`, `c6_wave()` | row 3(b); exhibits verified | exact; kernel as C1 |
| C7 | exact QM, `fullClass` | row 3(a); `R`, `R†`, `P`; values 1, 337/625, 16/25, 576/625, 0 | kernel `fullTheory_*`; exact `c7()` |
| C8 | `realClass` | row 3(a); `R`, `¬P` | kernel `realTheory_rot`, `realTheory_not_phases` |
| C9 | F2-1 `c9()` | mutant backflow detected; none under α=1 | exact |
| C10 | F2-1 `c10()` (Kochen–Specker) | row 9; reproduces 1, 337/625 and the C7 frequencies | exact (published marginal, cited) |
| C11a | `S₃` on `Fin 3`, generators `(0 1)` and `(0 1 2)`; Spekkens' reversible group `S₄` on `Fin 4`, generators `(0 1)` and `(0 1 2 3)`. Register readouts: cells `{0}, {1, 2}` (S₃) and `{0, 1}, {2, 3}` (S₄); the baseline compressions in the normalized indicator basis under the uniform measure | row 9; `N`, `O`, `Gauge` fails (identity gauge), `¬P`, `¬R`, `¬P₁` | exact: every generator a permutation matrix; every compression entrywise nonnegative. Kernel: `permClass_permMatrix`, `permTheory_nonnegBounded`, `permTheory_onesBounded_all`, `permTheory_phase_ceiling`, and, through `nonnegClass`, `falsifierUnavailable_of_nonnegBounded` and `not_p1_of_nonnegBounded` |
| C11b | the C11a models with exhibits: the 3-cycle in an orthonormal basis of the sum-zero plane (rotation by `2π/3`, over `ℚ(√3)`); `diag(ω, ω²)` in the Fourier basis (over `ℚ(√−3)`) | row 3(b) | exact: `R³ = 1`, `R ≠ 1`, trace `−1`, non-monomial; a non-real ratio `ω/ω²` |
| C12 | the gauged permutation class (§9, review fix 10). The gauge is `D_S = D ⊗ 1` on every carrier `Fin 2 × Fin n` and its block-compatible products, with `D = diag(1, i)`, and `D_S = 1` on carriers without the register factor | row 9, obstruction `Gauge_N`; the detector flags it | exact: `D·swap·D† = [[0, −i], [i, 0]]`, neither nonnegative nor ones-fixing; the detector finds `D†` mapping the generators to permutations. Kernel: `permTheory_not_gauged_rot`, `permTheory_not_p1`. Paper: the transport lemma below |
| C13 | the polar factor of a 2-cell baseline compression. Fixed model: `X = Fin 13` with the uniform measure, `C₀ = {0..3}`, `C₁ = {4..12}`, `σ = (0 4)(1 5)(2 6)(3 7)` | **frozen reference: row 3(a)**; screen item 11 flags it | exact: the compression `K = [[0, 2/3], [2/3, 5/9]]` and its polar factor `U = [[−5/13, 12/13], [12/13, 5/13]]`, checked by `UᵀU = 1` and `UᵀK` symmetric positive semidefinite. Kernel: `realSubclass_not_p1` (paper: the class is real). See S2-8 item 1 |
| C14 | controlled lift `F(x, s) = (T_s x, s)` on `Fin 3 × {0, 2}`, with `T₀ = (0 1)`, `T₂ = (0 1 2)` | row 9; screen item 8 fails (`s` conserved); class `⊆ permClass` | exact: `F` is a bijection, preserves `s` on every state, and `T₀T₂ ≠ T₂T₀`; kernel as C11a |
| C15 | the least architecture containing `rot` | row 3(a); `R`, `Gauge_N` holds, `Gauge_O` fails, `¬P` | kernel: `falsifier_available_of_mem`, `scaled_rot_not_gauge_nonneg`, `gauged_rot_mem_onesClass`, `rot_mem_realClass` with `realSubclass_not_phases`. Paper: `realClass` is an architecture containing `rot`, so it contains the least one |

**The C12 transport lemma (paper; fixed here).** Let `𝓘' := D·𝓘·D†`, with `D_S` as above.
1. `D_S` commutes with the register projectors, and `D_{S×Fin m} = D_S ⊗ 1` commutes with the
   ancilla blocks. So `𝓘'` is an `Architecture` whenever `𝓘` is.
2. `InstAvail 𝓘'` holds of `conjChannel V` if and only if `InstAvail 𝓘` holds of
   `conjChannel(D†VD)`. This is by induction on `InstAvail`, using that each of its constructors
   commutes with the conjugation.
3. Hence `R` for `T_{𝓘'}` is equivalent to the availability of `D† rot D` in `T_𝓘`, and `P₁` for
   `T_{𝓘'}` is equivalent to `P₁` for `T_𝓘`, because `phaseGate` commutes with `D`.

The kernel statements cover the right-hand sides for `𝓘 = permClass`. The transport itself is
paper-grade, and recorded as such.

**Probes and candidate rows.** The `probes` field is `null`, with reason "no candidate frozen
(PC★)". Rows 2 (probe and held-out triggers), 4, 5, 6, 7 and 8 are reached only by synthetic
self-test files.

## S2-5. Mutations and the self-test

**Mutations.** M1–M17 run exactly as frozen in §10, in stand-in form where no candidate exists.
- M1, M3, M4, M6 and M7 reuse F2-1's exact helpers (`g4`, `haar_invariant`, `has_float`,
  `g4b_label_ok`, `freq`).
- M2, M5, M8, M9 and M10–M17 act on PC-1's `decide_row`, `screen` and `unit_token`, using synthetic
  records:
  - M2 adds `phaseGate` to C3's generators;
  - M10 is a constant rule `:= rot` on a C2 record;
  - M11 disables the gauge check on C12;
  - M12 declares the C11b basis as the readout;
  - M13 counts both orders of C14 as executed;
  - M14 drops the failure branches;
  - M15 chooses `μ` for L2;
  - M16 puts L2 text on a row-7 file;
  - M17 claims invariance from a two-member sample.
- Each must change its outcome as §10 states. A mutation that is not caught is a 0(i) failure.

**Self-test** (`decide_row`). At least one synthetic record per row and sub-row of §6: 0(i)–(vii),
1, 2 (each trigger), 3(a), 3(b), 4 and 5 (both grades), 6(a)–(d), 7, 8, 9, 10. It also includes
every case listed in §10 and its review amendments:
- 6(d) when not transplantable;
- 7 with an exhibit;
- 8 with one of `R`, `P₁` refuted and the other undecided;
- 6(c) for `P₁ ∧ ¬R`;
- 6(a);
- `¬R ∧ ¬P₁` on all members with `S` varying, which gives 7;
- `Π_C = ℤ/4` with IP-2 undecided, which gives 6(d);
- C15's shape, which gives 6(c) and never 7;
- `Φ_min` without `P`, which gives 6(b) and never 5.

**Self-test** (`unit_token`, added by this amendment).
- U1: `forbidden_precomputation: true`, every control, mutation and self-test green, both kernel
  steps `success`, and a review recorded. The output must be `token = "INCONCLUSIVE (void)"`,
  `void_reasons = ["0(vi)"]`, and `scientific_finding.status = "carried under exception"`. The gap
  token must appear nowhere in `token` or in `scientific_finding`.
- U2: as U1, with one control failing. The output must be `void_reasons = ["0(vi)", "0(i)"]`,
  with the status `withheld: …`.
- U3: as U1, with the `Build` step failing. The output must have `"0(v)"` added and the status
  withheld.
- U4: as U1, with no review. The status must be `pending exact-head review`.
- U5: as U1, but with `forbidden_precomputation: false` and the disposition digest unchanged.
  - The freeze checkpoint requires the field to be `true` whenever the disposition file has its
    frozen digest. So it fails closed: `void_reasons = ["0(ii)"]`, the status is withheld, and the
    token is `INCONCLUSIVE (void)`.
  - The absence of `"0(vi)"` shows that the entry is read from the field, not hard-coded.
  - In no case is the gap token produced.

## S2-6. Results schema (`pc1-stage2-results/1`)

```json
{
  "schema": "pc1-stage2-results/1",
  "inputs": {"<frozen file>": {"blob": "…", "sha256": "…"}, "PC-S2.md": {"commit": "…", "sha256": "…"}},
  "vendor": {"<path>": {"expected_blob": "…", "actual_blob": "…", "pass": true}},
  "stage1": {"candidate": null, "forbidden_precomputation": true,
             "source": {"path": "amendments/PC-star-disposition.md", "sha256": "…"},
             "owner_decision": "PR #1022 comment 6547077354"},
  "statements": {"<name>": {"module": "F2CoherenceControls|PC1Controls", "statement_sha256": "…",
                 "verbatim_in_module": true, "build_step": "pending|success|failure",
                 "axiom_check_step": "pending|success|failure"}},
  "exact": {"<check id>": {"value": "<exact string>", "expected": "<exact string>", "pass": true}},
  "controls": {"C1": {"record": {}, "expected_row": "9", "row": "9", "pass": true}, "…": {}},
  "probes": null, "probes_reason": "no candidate frozen (PC★)",
  "mutations": {"M1": {"as_stated": true}, "…": {}},
  "selftest": {"decide_row": {"<case>": {"expected": "…", "got": "…", "pass": true}},
               "unit_token": {"U1": {}, "…": {}}},
  "token": "INCONCLUSIVE (void)",
  "void_reasons": ["0(vi)"],
  "scientific_finding": {"statement": "…", "scope": "…", "exception": "PR #1022 comment 6547077354",
                         "status": "…", "review": null},
  "verdict_status": "awaiting CI step conclusions | final",
  "run": {"head": null, "script_sha256": "…"}
}
```

## S2-7. Execution, checkpoints and reproducibility

**Files.**
- `stage2/controls.py`: one script, `python3 -I -B`, exact arithmetic only.
- `stage2/results.json`: its output, before CI, with the kernel fields `pending`.
- `stage2/RESULT.md`: actual against expected, failures stated as such.
- After CI: `stage2/kernel-steps.json` and `stage2/kernel-decision.json`.
- After the exact-head review: `stage2/review.json`.

**Checkpoints.** Each gives a 0-clause reason on failure.

| Checkpoint | Rule | On failure |
|---|---|---|
| Freeze | the four frozen inputs match S2's table, and `PC-S2.md` matches its commit | 0(ii) |
| Vendor | each vendored file's blob id equals S2-2 | 0(ii) |
| Statements | the header and each statement verbatim in `PC1Controls.lean`; the vendored module's blob as fixed | 0(ii) |
| Untouched | every other `OIBridge` module blob-identical to `5914c17c`; no frozen PC-1 file changed | 0(ii) |
| Exact | no `float` anywhere in `results.json` | 0(iv) |
| Controls, mutations, self-test | each as S2-4 and S2-5 state | 0(i) |
| Kernel | for the 33 statements, the `Mathlib bridge` job's `Build` and `Release gate` step conclusions at the exact head, read from the host's run, job and step records, with `#print axioms` decided by the gate's `lean_axiom_check` (no `sorryAx`; only `propext`, `Classical.choice`, `Quot.sound`). Log text is never read (§A.44) | 0(v) |
| Replay | the normal and `-O` runs byte-identical; `results.json` regenerates byte for byte; `--kernel kernel-steps.json [--review review.json]` byte-identical in both modes | 0(ii) |

**The exact-head record** (in `RESULT.md` and `kernel-steps.json`):
- the PR head SHA, noting that the ordinary PR run tests a synthetic merge;
- the CI run id;
- the job id;
- the `Build` and `Release gate` conclusions;
- the axiom-check conclusion;
- the sha256 of the script and of each output file;
- the independent exact-head review: reviewer, time, quote and head (`review.json`).

Ordinary draft-PR CI only. No dispatch, no special workflow, and no `F`/`E` designation.

**Failures and repairs.** A failure is recorded as it occurs, with its checkpoint, in
`results.json` and `RESULT.md`. Nothing is repaired silently. A statement, premise, expected value,
verdict definition, vendored byte or earlier outcome is never edited. Any substantive defect,
including a Lean statement that does not elaborate, stops the run for a new owner decision. A later
attempt goes in a new run directory, as F2-1's `run-2` did, and earlier attempts are kept.

## S2-8. Unresolved items for the reviewer and the owner, before execution

1. **C13's frozen reference looks unreachable (a pre-execution defect, not repaired here).**
   - **Why (paper argument).** For a 2-valued register under one invariant measure, every
     two-state stationary chain satisfies detailed balance. So every baseline compression is
     symmetric in the `L²(μ)` indicator basis. Its polar factor is therefore `1`, or one fixed
     reflection determined by the cell masses: for the fixed model, `U` above.
   - **Consequence at level one.** The generated class contains only multiples of `1` and `U`,
     and products of rank at most one. It does not contain a multiple of `rot`, so `R` fails at
     level one. `P₁` fails too, because the class is real.
   - **Expected routing.** The exhibit `U` is verified, so `decide_row` would give row 3(b), not the
     frozen 3(a). Elements generated at ancilla levels are not ruled out by this argument.
   - **Owner decision requested before execution.** Either (a) run C13 as frozen, with a mismatch
     recorded as 0(i), which also withholds `scientific_finding`; or (b) a decision on C13's
     reference. This amendment does not choose. Without a decision, (a) applies.
2. **The C12 and C15 class facts are partly paper.** The transport lemma for C12 and minimality for
   C15 are paper. Formalizing a uniform carrier-indexed gauge or a least-architecture closure was
   not attempted, so the elaboration risk stays bounded. The kernel statements cover the
   transported targets.
3. **`R` is decided on paper for C13** (the level-one closure argument), labelled `paper`.
4. **Build risk against the current `main`** for the vendored module (S2-2). Any failure is 0(v)
   and stops the run.

## S2-9. What this amendment does not do

It runs nothing, writes no code or Lean, and changes no frozen file. It does not authorize
execution before its independent exact-commit review. It does not change the strict token, which
is `INCONCLUSIVE (void)` under 0(vi) whatever stage 2 shows.
