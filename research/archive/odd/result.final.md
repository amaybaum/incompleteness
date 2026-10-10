# Reconstruction round ODD-CHAR-1 — the dimensions that carry a NOT, the frame and the gate relations, and forward positivity at every odd dimension above one: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #804.

- **`D`** — `3c92d16b2f33d6a6acd32e96922a1f66ee735220`, the head of `main` after round PARITY-NOT-1 landed, certified
  by push run 37631392533.
- **`F`** — `d3d058d9cd85b81c1e70919190b7b3b234b41a94`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `1b6ecb9339c5900522771e89ad147d215afe2caf`. Its exact-head
  `workflow_dispatch` run 37656780308 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F`. That run attests the control plane only. An earlier dispatch on `F`, run 37653582697, created 31
  of the workflow's 32 jobs and is not its attestation.
- **Shape** — non-sealing; stages C1 (`cdec5d0b`, `controls.py` blob `95781938`), S1 (`3775d2eb`, the module, the import
  line and the census family) and this note (S2).

**Outcome:** `ODD-CHAR-1-READ`

**Q-FAM: ODD-FAMILY-PROVED.** For every `k`, `nK k`, the diagonal map with sign `−1` on the homogeneous indices above
`k`, is a NOT of `eball (2k + 1)` with axis the last coordinate `zK k` (`isNot_nK`), and the sign-free reversal gate
`gRev k` satisfies `NativeGate`'s frame (`gRev_frame`) and `GateRel (nK k) (gRev k)` (`gateRel_gRev`), through
PARITY-NOT-1's `sgate_relT` and `sgate_relC` and the exchange of the two sign classes by `Fin.rev` (`oddK_rev`). The
eigenspaces of the homogenized `nK k` are balanced (`finrank_plus_eq_finrank_minus_nK`). Neither positivity clause is
read.

**Q-ODD: ODD-CHARACTERIZATION-PROVED.** Some `z`, `N`, `G` with `IsNot (eball d) z N`, `NativeGate`'s frame and
`GateRel N G` exist exactly when `d` is odd (`exists_frame_gateRel_iff_odd`). The forward direction is PARITY-NOT-1's
`not_even_of_gateRel`, which does not read the frame; the reverse direction is DIM-1's `cnot1` with `neg1` and `z1` at
`d = 1`, and `gRev k` with `nK k` and `zK k` at `d = 2k + 1` for `k ≥ 1`.

**Q-POS: HIGHER-ODD-POSFWD-FAILURE-PROVED.** For every `k ≥ 1`, the image under `gRev k` of the product of the first
axis `xK k` with the corner `zK k` pairs to `−1/10` with the sharp effects of `wK k = −(3/5 e_{2k−1} + 4/5 e_{2k})` and
`zK k` (`gRev_value`), so it lies outside the maximal cone (`gRev_not_mem_maxCone`), forward positivity fails on
`eball (2k + 1)` (`not_posFwd_gRev`) and `gRev k` is not a native gate (`not_nativeGate_gRev`). The failure is read from
that explicit rational witness, not from DIM-1's dimension corollaries.

The three cells are read by separate rules and none reads another's outcome. The earned reading:

> The frame and both relations admit exactly the odd dimensions. For every odd dimension at least 3, an explicit member
> of this family fails forward positivity. Combined with DIM-1, the positivity assumptions are therefore collectively
> load-bearing for excluding the higher odd dimensions.

At each odd `d ≥ 5`, `exists_frame_gateRel_iff_odd` supplies a NOT, the frame and both relations, and DIM-1's
`dim_of_nativeGate` excludes any gate with all five clauses; the two positivity clauses together are what that
exclusion reads at those `d`. The round does not separate them: each gate of the family is its own inverse, and the
round exhibits no gate with the frame, both relations and one positivity clause that fails the other. Whether either
clause is needed without the other is open.

This round selects no dimension from positivity, classifies no gate with the frame, the relations and positivity in any
dimension, and does not show that the frame, `relT` or `relC` is needed for oddness or for any exclusion. It concerns
no complex structure and gives no interpretation of `J²`, and it concerns no NOT or gate carried or realized by a
physical theory: `nK`, `gRev`, `xK` and `wK` are mathematical witnesses. It adopts no premise, edits no manuscript and
not `verification/ROADMAP.md`, and the DIM-1 and PARITY-NOT-1 records stand as they are.

***

## Execution facts

- **C1** — `cdec5d0b97d932ca1852cbf482530fe647832a32`, single parent `F`, adds `controls.py`, blob `957819380643ff7690a6125d54b011f61aec403d`, the frozen blob;
  `--self-test` passes 62 checks.
- **S1** — `3775d2ebf05283175c4a1e316414eb92f4a32623`, single parent C1, adds the module (blob `bbb8a63229870f61445d5dbb3fe9102b826d9208`), the import
  line (`OIBridge.lean`, blob `ff535cd4c970bd2485faa3013da2bc6d8d5dc948`) and the census family (blob `6fc3423103bb70765d72b483e60ef8e91ded1209`), the blobs of the predicted
  execution tree. `controls.py check S1 --freeze F` passes 20 checks. Its exact-head `workflow_dispatch` run
  37659104049 (attempt 1) concluded `success` with all 32 jobs succeeded: the Mathlib bridge (job 112921745895) built
  `OIBridge.OddChar` with each of the 12 frozen `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`
  and no warning in the module, and the release gate passed every step; the Lean kernel check (job 112921746270) and the probe aggregate (job
  112928987529) succeeded. No repair was needed.
- **The cells** — `controls.py verdict` at S1 prints `ODD-FAMILY-PROVED`, `ODD-CHARACTERIZATION-PROVED` and
  `HIGHER-ODD-POSFWD-FAILURE-PROVED`, each read from the module's statements and the landed statements at `D` by its own
  frozen rule.
- **Count facts** — the module carries 12 `#print axioms` lines; the release gate's `lean-axioms` step reports 5826
  named results at S1 and 5814 at `D`, the 12 short names being new.
