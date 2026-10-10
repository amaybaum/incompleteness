# Reconstruction round K2-GUARD-1 — two interface facts of the composite route: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #800.

- **`D`** — `8daf2bc0ad9c4fe4e9ae422b3a9a010a80ab9e53`, the head of `main` after the ROADMAP change #799 landed,
  certified by push run 37457928970.
- **`F`** — `9c4834b050a87e82b1c44d048f902976b2511131`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `12800955d371b8c07acbf513b113a742e762b00f`. Its
  exact-head `workflow_dispatch` run 37476267644 concluded `success` with all 32 jobs succeeded, its `check-run`
  attestation; the owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 (`a9c9c8bf`, `controls.py` blob `d33086bb`), S1 (`8f4f9459`,
  the module, the import line and the census family) and this note (S2).

**Outcome:** `K2-GUARD-1-READ`

**Q-ORIENTATION: K2-ORIENTATION-OBSTRUCTION-PROVED.** No set `K` of joint vectors of two copies of `eball 3` that
contains every product state of the ball and lies in `maxCone (eball 3)` is invariant under both `cnot` and
`actT reflY`, where `reflY = diag(1, −1, 1)` acts on the second copy alone (`no_candidateCone_cnot_reflY`). The
product state `prodState xplus z3`, then `cnot`, then `actT reflY`, then `cnot`, lands on a joint vector on which the
product of the sharp effects along `−e₁` and `−e₃` takes the value `−1/2` (`chain_eq`, `chain_value`), so it lies
outside `maxCone (eball 3)`. The controls hold: `cnot` satisfies DIM-1's native-gate hypotheses; `reflY` maps the ball
into itself with determinant `−1`, and `nflip` has determinant `1`; the product states with their `cnot` images form a
candidate cone invariant under `cnot`, and the product states alone form one invariant under `actT reflY`; with
`nflip` in place of `reflY` the same chain takes the value `0` on the same pair of effects. The obstruction therefore
comes from the joint invariance requirement. The earned reading is only this: a composite route that admits `cnot` and
chooses its cone from this candidate family cannot also admit `reflY` on one copy as a reversible symmetry.

**Q-ENTANGLING: K1-ENTANGLING-WEAKENED.** With `2 ≤ d` in place of the entangling clause, DIM-1's `IsNot` and
`NativeGate` give `d = 3` (`three_of_nativeGate_of_two_le`, through `dim_of_nativeGate`), and K1-BRIDGE-1's relative
hypotheses with effect soundness, body preservation, K∞-Seed, K∞-Trans and K∞-V4 give `d = 3`
(`three_of_nativeGateOf_of_two_le`, through `dim_of_nativeGateOf`). Under DIM-1's hypotheses the entangling clause
gives `2 ≤ d` (`two_le_of_entangling`); no converse is stated and no equivalence is claimed. The interval with its
classical gate satisfies `IsNot` and `NativeGate` at `d = 1`, where `2 ≤ d` fails (`two_le_load_bearing`), and DIM-1's
gate satisfies every hypothesis at `d = 3` (`two_le_satisfiable`). The earned reading is only this: the entangling
clause is sufficient to exclude `d = 1`, and DIM-1's dimension conclusion consumes only `2 ≤ d`. The dimension path
now reads `NativeGateOf` with `2 ≤ d` gives `d = 3`; where `2 ≤ d` comes from remains open.

The two cells are read by separate rules and neither depends on the other.

This round does not derive local tomography; does not identify the physical composite cone; does not derive the
product-test structure; does not source K∞-Act; does not source a continuous or dense family of reversible
operations; does not adopt a topological closure of the available operations; does not derive K∞-Copy; does not show
that every theory excludes one-copy reflections; does not derive `2 ≤ d` from OI; does not discharge K2; and does not
alter H-Bell. It edits no manuscript and not `verification/ROADMAP.md`, and the DIM-1, EFF-1 and K1-BRIDGE-1 records
stand as they are.

***

## Execution facts

- **C1** — `a9c9c8bf5556aa3b05b6b5c54373c256c955d87f`, single parent `F`, adds `controls.py`, blob `d33086bb5560ed979f808ab2ec953f364dacd21d`, the frozen blob;
  `--self-test` passes 53 checks.
- **S1** — `8f4f94591cebce9ccf23b39ab55f90f88fef5835`, single parent C1, adds the module (blob `ec8ba57b178561c81b082404ceb02241ada1fe1e`), the import line (`OIBridge.lean`,
  blob `58d7ecaeb47dfe25992afeb3cea85f6faf92a05b`) and the census family (blob `05be8369fcb8e6578ac991a7b56ca6b492318f9e`), the blobs of the predicted execution tree.
  `controls.py check S1 --freeze F` passes 21 checks. Its exact-head `workflow_dispatch` run @@S1_RUN@@
  (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge (job @@S1_BRIDGE@@) built
  `OIBridge.K2Guard` with each of the 19 frozen `#print axioms` lines within `[propext, Classical.choice,
  Quot.sound]`, and the release gate passed every step; the Lean kernel check (job @@S1_KERNEL@@) and the probe
  aggregate (job @@S1_PROBE@@) succeeded. No repair was needed.
- **The cells** — `controls.py verdict` at S1 prints `K2-ORIENTATION-OBSTRUCTION-PROVED` and `K1-ENTANGLING-WEAKENED`,
  each read from the module's statements by its own frozen rule.
- **Count facts** — the module carries 19 `#print axioms` lines; the release gate's `lean-axioms` step reports 5762
  named results at S1 and 5743 at `D`, the 19 short names being new.
