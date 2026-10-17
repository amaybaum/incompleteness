# KINF-COPY-1 (#822): relative-form re-cut, design note for owner review

**Scope.** Drafting only. Nothing is frozen, pushed, dispatched or designated. This note is a review artifact on the
local branch `wip/kinf-copy-1-relative`, not a control-plane file: it is not part of a drafting commit (V3 `S2`, `G9`)
and would fail the record control R at `E`. The preregistration commit `d871aefe` changes only `preregistration.md` and
is the one a drafting pull request would carry. The full diff against PR #822's text is
`git diff 90c72640:<prereg> d871aefe:<prereg>`.

## What "relative form" means here, and its source

The F2 decision memo (`plan/f2-target-extension-scope-20261017` at `362131e0`), §5.1, row #822, has: "relative form
`RelativeGateTransport` run 38606561330 [CD]", "depends on: none of (a)–(d)", and "must keep explicit: integration of
the relative gate with available tests, and its cone hypotheses (planning note :44)". The planning note's row reads
"available-test relative-gate integration and its cone hypotheses".

So the memo's relative form is specific. The two-NOT hypotheses are stated with positivity on `maxConeOf avail`, the
cone of the available tests (`NativeGate2Of`, K1-BRIDGE-1's `NativeGateOf` with two NOTs). Each cone hypothesis that
moves data between that form and the maximal one is a named premise, one per direction. This contains the reading
"every claim relative to explicitly stated hypotheses": every statement is an implication from hypotheses written
out in it, and none reads an F2 choice. It is more than that reading, though: it adds a second kernel module, the
transport theorems and the relative selectors.

## Changes from PR #822's text (`90c72640`, D = `dee3b5ae`), with reasons

1. **D re-cut to `b96662e6`.** The memo (§5.2) allows a re-cut before F. Drift measured: 89 commits, no cited module
   changed, ROADMAP K∞-Copy moved to :1040–1043, last import is `TurnpikePremiseOrientation` (:269), census tail is
   BG-2 (:1485–1492), verify.yml anchors :459–460, :557, :577, :598, :618.
2. **Relative form added** (module `RelativeGateTransport`, cell Q-REL, governed path, second import line, two-module
   census family). This is what the memo names for #822. It also aligns the round with K1 as stated at `D` (ROADMAP
   :68 states the native-gate hypotheses on the cone of the available tests).
3. **Hypotheses named once; per-claim table** of what each claim is relative to, its witnesses per direction, and the
   landed theorems it consumes. This puts the "relative" content in the record rather than in prose.
4. **§A.34.** The one displayed iff (`nativeGate2Of_iff_of_cone_eq`) has its two witnesses named, and an S3 proof-shape
   check is added. Without EQ, only the one-way transports R1 and R2 are stated.
5. **`swapped_nativeGate` described correctly.** The PR says it shows "the same gate is a one-NOT native gate with the
   target NOT". The kernel statement is that the *reduction* of the swapped data is a native gate with the *control*
   NOT `nflip`. The one-NOT reading with the target NOT is the exact check C6 only.
6. **Cell Q-COUNTER and probe 2 added** (`relgate_counter.py`). Its verdict line is renamed from
   `TRANSPORT-NEEDS-CONE-EQUALITY` to `…-CONE-INCLUSION`. `axisFamily` is effect-sound, so SUP holds for it and the
   witness bears on INC only, so "equality" overstated what it shows. C6 is labelled as sampled, with the universal
   claim a written argument.
7. **Negative results scoped.** J/K covers the two named maps. The shear covers the positivity-transfer step only. The
   countercontrol covers one family and one gate, and the transport's conclusion, not the selector's.
8. **R9 (`hcov_of_copyNatural`) scoped.** Copy naturality gives the `hcov` identity only, one direction, and not the
   CONJ conjuncts (`CopyNatural`'s `e` need not fix `z` or preserve the ball).
9. **ROADMAP wording narrowed.** The PR licensed "Copy naturality may be weakened to type covariance". No kernel
   declaration states that one-NOT data meet TC (with `g = id`), so "weakened to" and "the obligation becomes" are not
   licensed. The licensed sentence states sufficiency, maximal and relative.
10. **F2 independence stated.** No target, gate, preserved-law or necessity choice is adopted or read. No F2
    sufficiency contribution is claimed. This follows the memo's "none of (a)–(d)".
11. **Module headers must be rewritten (comments only).** Blob `fb9c73fe`'s header contains "design module" and "Not
    adopted, not certified, not a round", which the PR's own S4 rejects. Blob `507ac329`'s header says "not compiled"
    and it carries two `[unsure]` comments. So the execution blobs are not yet fixed, and the predicted-tree run must
    measure them.
12. **Probe 1's kernel path made executable.** `e2_copy_conj.py`'s `KERNEL` is `'../../../verification/…'` relative
    to the working directory. Run from `verification/lean` it resolves outside the repository. It now resolves from
    the script's directory.
13. **Checker pattern of #829 run 2.** Positive tokens are gated on all 13 static controls. Outcomes are recorded
    explicitly, and absent or non-`True` counts as failed. Unknown stages and modes are refused. There are an
    end-to-end missing-report self-test through the real `check()`, a frozen self-check count, and the shard running
    `controls.py --self-test`.
14. **§A.42.** The PR predates §A.42 (adopted 2026-10-16). The design runs are now cited as provenance only, the
    predicted-tree run is the evidence the rules consume, and two retention pins are pending. The relative-form run's
    branch `ccr-ac945020-v97mrh` no longer exists; its commit `c9f16498` is reachable only from a research branch.
15. **§A.41 table extended**: gating, independence of the probes from the new modules, and the three retention rows.
16. **Stages and record directory** follow #829: `evidence/` and `evidence/f-run/` are admitted, and R requires the
    result note at `E`.

## Claim table

Status: [CD] at `D`; "proved" means a kernel theorem of the stated implication if its cell is positive at `E`.

| # | statement | relative to | witness per direction | status |
|---|---|---|---|---|
| M1 | target-copy conjugation preserves two-NOT data | N2, CONJ | `nativeGate2_conj` | proved (cond.) |
| M2 | conjugated gate is one-NOT with `NC` | N2, TC | `nativeGate_of_conj` | proved (cond.) |
| M3–M5 | `d ∈ {1,3}`; `d = 3` if `2 ≤ d`; CONJ⁻ form | NOT, N2, TC | `dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg` (via landed `dim_of_nativeGate`, `three_of_nativeGate_of_two_le`) | proved (cond.) |
| M6 | N2 with `NC = NT` ⇔ `NativeGate` | — | → `nativeGate_of_nativeGate2`; ← `nativeGate2_of_nativeGate` | proved |
| R0 | N2-rel with `NC = NT` ⇔ `NativeGateOf` | — | → `nativeGateOf_of_nativeGate2Of`; ← `nativeGate2Of_of_nativeGateOf` | proved |
| R1 | relative ⇒ maximal | INC | `nativeGate2_of_cone_subset` | proved (cond.) |
| R2 | maximal ⇒ relative | SUP | `nativeGate2Of_of_cone_superset`, `nativeGateOf_of_cone_superset` | proved (cond.) |
| R3 | EFF ⇒ SUP | EFF | `maxCone_subset_maxConeOf` | proved (cond.) |
| R4 | relative ⇔ maximal | EQ | → `nativeGate2_of_cone_eq`; ← `nativeGate2Of_of_cone_eq` | proved (cond.) |
| R5 | relative conjugacy results | N2-rel, CONJ/TC, EQ | `nativeGate2Of_conj`, `nativeGateOf_of_conj` | proved (cond.) |
| R6 | relative selectors | NOT, N2-rel, TC, K1B | `dim_of_nativeGate2Of_conj`, `three_…_of_two_le`, `…_neg` (via landed `maxConeOf_avail_eq`) | proved (cond.) |
| R7 | relative selector, dense orbit | K1B-dense | `dim_of_nativeGate2Of_conj_dense` (via landed `maxConeOf_avail_eq_of_dense`) | proved (cond.) |
| R8 | ORB ⇒ INC; selector without EFF | ORB | `maxConeOf_subset_maxCone_of_orbit`, `dim_of_nativeGate2Of_conj_of_orbit` | proved (cond.) |
| R9 | CN ⇒ `hcov` | CN | `hcov_of_copyNatural` (converse open) | proved (cond.) |
| P1–P3 | swapped data at `d = 3`; its reduction; all relative-selector hypotheses satisfiable | — | `swapped_nativeGate2`, `swapped_not_ne`, `swapped_nativeGate`, `swapped_relative_hyps` | proved |
| X1 | exact instances; J/K at 5, 7 violate TC | parsed kernel tables | probe 1, 13 checks | exact computation |
| X2 | `axisFamily`: one relative one-NOT gate that is not a native gate | parsed tables; `cone_eq_fails_axis` | probe 2, 11 checks | exact (C6 sampled + written) |
| — | TC, NOT, N2/N2-rel, EFF, ORB, INC for any physical data; converse of R9; TC ⇔ equal ±1 splits; kernel J/K and X2; relative entangling selector; whether TC admits gates copy naturality excludes | — | — | open |

## Kernel identifiers verified at `b96662e6`

All found, at the lines the preregistration's S2 lists: CompositeDimension (`HVec`, `W`, `hom`, `homMap`,
`prodState`, `ehom`, `maxCone`, `actT`, `actC`, `corner`, `IsNot`, `NativeGate`, `cnot`, `z3`, `nflip`, `xplus`,
`isNot_nflip`, `cnot_prodState_mem_maxCone`, `nativeGate_cnot`, `pos_of_isNot`, `dim_of_nativeGate`); TransitiveBody
`eball`; K2Guard `actT_prodState`, `three_of_nativeGate_of_two_le`, `three_of_nativeGateOf_of_two_le`; K1Bridge
`NativeGateOf`, `nativeGate_of_cone_eq`, `dim_of_nativeGateOf`, `cone_eq_fails_axis`; EffectSpace `fullAut`,
`sharpFamily_subset_avail`, `maxConeOf`, `maxConeOf_fullEffects`, `maxConeOf_anti`, `maxConeOf_sharp_subset_maxCone`,
`EffectsOn`, `maxConeOf_avail_eq`, `avail_eq_fullEffects`, `sharpUnitFamily`, `not_fullEffects_of_orbit`,
`axisFamily`; DenseOrbit `DenseBoundaryOrbit`, `maxConeOf_avail_eq_of_dense`; OrbitGeneration `SharpSeed`,
`PreservesBody`, `SeedOrbitAvailable`, `BoundaryTransitive`; KInfFoundations `IsEffectOn`, `CopyNatural`,
`copyNatural_iff_apply`. No new declaration of either module exists on `main`.

## Controls the invariants need (§A.41), for `controls.py` (not written)

C1, C2, S1, S2, S3, S4, W, I, J, P, R, G, T, with the V self-test, as listed in the preregistration's controls
section. All follow the pattern reviewed for #829 (`round-ktoken-maxcone-1/controls.py`, `review/REVIEW-RUN2.md` at
`9a371447`):
- every positive token, `READ` included, is gated on all 13;
- `check` records each outcome as it runs, and absent or non-`True` counts as failed;
- unknown stage or mode raises an error;
- the end-to-end self-test runs the real `check()` on an in-memory `D`/`F`/`E` fixture, with each record call removed
  and each input absent;
- the self-check count is frozen.

The relative form adds three things:
- S3 proof-shape checks: the iff's witnesses, relative selectors routed through the maximal-form selectors, and the R9
  direction;
- the Q-COUNTER probe in `verdict`;
- a one-cell mutation per cell.

## Files the execution will touch, and serialization

- **Added:** `OIBridge/CopyCovariance.lean`, `OIBridge/RelativeGateTransport.lean`, `verification/lean/kinf_copy1_probe.py`,
  `verification/lean/kinf_copy1_relative_probe.py`, and the record directory.
- **Modified:** `verification/lean-mathlib/OIBridge.lean` (two lines after the last import),
  `verification/lean-manuscript-census.json` (one family at the tail) and `.github/workflows/verify.yml` (one shard
  after BG-2, plus the aggregate's `needs`/env/echo/test).
- **Overlap.** These are the same three sites #829 and #831 splice. The memo also notes collisions on `verify.yml` with
  #824 and #830. The memo's order is #829 → #831 → #822, and each landing moves the anchors, so this draft is re-cut
  (re-measuring the anchors, the census tail and the aggregate lines) after each preceding landing and before F.

## Open questions for the owner

1. **Module layout.** Two modules (as compiled in run 38606561330) or one (`RelativeGateTransport`'s content appended
   to `CopyCovariance`)? This draft uses two.
2. **"Weakening" wording.** Add a small declaration that one-NOT data meet TC with `g = h = id`, so that "copy
   naturality may be weakened to type covariance" has a witness? It would be new statement surface, so it needs the
   predicted-tree run. This draft leaves it out and narrows the wording instead.
3. **Probe 2's verdict token rename** (`EQUALITY` → `INCLUSION`): accept? It changes the probe's blob.
4. **Relative entangling selector.** K1 at `D` reaches `d = 3` through `EntanglingOf`. This round reaches it only
   through `2 ≤ d`. Add `three_of_nativeGate2Of_conj` with `EntanglingOf`, or leave it open?
5. **Hygiene.** Remove the unused `first` alternatives in `CopyCovariance` before the predicted-tree run?
6. **Drafting PR.** Reset #822's branch to `d871aefe` (it is a single control-plane commit from `D`), or open a new
   pull request? And when should it be re-cut relative to #829's and #831's landings?
7. **Design-run allowance.** The predicted-tree run at `D` is required before F; it needs the owner's approval to push
   a disposable branch and dispatch.

## Owner recommendations on the open questions (2026-10-17)

These are the owner's recommendations on the questions above, given for `5338022b`. They are recorded as
**recommendations, not adopted decisions**. The draft is prepared to match them, and each stays open until the owner
adopts it explicitly.

| # | Question | Recommendation |
|---|---|---|
| 1 | Module layout | Keep two modules, matching the compiled design (run 38606561330). |
| 2 | "Weakening" wording | Leave the extra declaration out and keep the narrower sufficiency wording. An identity-instance witness alone would not establish a strict weakening. |
| 3 | Probe 2's token | Accept `EQUALITY` → `INCLUSION`, matching what the countercontrol establishes. |
| 4 | Relative entangling selector | Leave it outside this round's scope. |
| 5 | Proof hygiene | Keep the existing proof bodies unless compilation identifies a problem. |
| 6 | Drafting PR | Open a replacement PR, preserving #822's history and linking both. Finalize its `D` and anchors after the preceding landings (#829, then #831), before F. |
| 7 | Predicted-tree run | Prepare the complete package now. Review its exact executable tree before any push or dispatch is authorized. |
