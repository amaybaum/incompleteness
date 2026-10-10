# HO-11 (v1) — bridge → countermodels: HO-4's composition-clause proposal tested; the excluding clause is family membership; Stab_loc(K(Z_F)) = V4

**From** `research/bridge` (round 2, node B8), answering HO-4. **To** `research/countermodels` (the realization-facing
structure of K(Z_F); explicit cones for finite groups). The manuscript-obligation items are recorded in the overview
(hold), not applied. Written by the coordinator from the source thread's committed record; version 1, 2026-10-10.

## Statements and labels

1. **Clause (4) is the composite action for the instruments it is given** (B8-1). Main.md:552 ("`𝓘_a ⊗ 𝓘_b` on the
   joint branch register") for a unitary local instrument is, through the dictionary, exactly `actC B(U)` /
   `actT B(U)` on the pair table. The theorem's input is a fixed quantum experiment with a finite family `𝓕`, so no
   clause of it makes continuous (or any further) local operations joint instruments; K(Z_F) lies outside its range by
   the hypothesis "quantum experiment", not by clause (4); B4's realization of K(Z_F) satisfies clause (4) for its own
   local family. Label: CONDITIONAL (the reading of Main.md:552 through the dictionary; the identity exact [X] for the
   drive step, `S`, `H`, the `cyc3` lift and all 16 basis tables).
2. **The excluding clause is family membership** (B8-2, B8-3): "an operation available to a token in isolation is a
   joint instrument". Its matrix form is `InertSpectatorCompositionality` ⟺ `HasParallelReferenceExtension`, and the
   kernel proves it is not implied by the sealed C1–C4 core with exact system QM and full composite unitary control:
   **CERTIFIED** [K at L, OIRealization.lean:360 `finiteOI_not_implies_inert`; SpectatorBridge.lean:223, :233]. With
   clause (4) it is (b): disguise test FAILS. So HO-4's proposal is confirmed and sharpened — the clause that would
   exclude K(Z_F) from a realization theorem is (b) itself.
3. **Stab_loc(K(Z_F)) = V4** (B8-4). The single-token rotations preserving K(Z_F) are exactly
   `V4 = {I, R_x(π), R_y(π), R_z(π)}` on each token: exact among the 24 Cliffords (40 certified exclusions, each a
   negative pairing with a certified member); over all of SO(3) CONDITIONAL on KZ7 [A] with a group argument [W]; the
   flow laws for the two A_miss axes re-derived (`−s`, `+s`). Consequence: one single-token rotation outside `V4`,
   discrete or continuous, already excludes K(Z_F); continuity is needed only to force `Q3` (the native discrete
   Clifford family, order 11520, leaves exotic cones — HO-12 item 3, HO-14).

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `3686049e` |
| proposal | `research/bridge/handoff-proposals/HP-5-composition-clause-V4.md`, sha256 `a029f06f68b146a05941791971de610d81d27bf8ad09b6c7a10afd605c3451e9` |
| results | `research/bridge/RESULTS.md` sha256 `dc17220c…` (rows B8-1 … B8-4); `NOTES-B8.md` `c3d96eb93056940dd2ebdba90fdd20b4cf701a46ed4ff5838fb35a0c964fe292` |
| script, output | `experiments/b8_composition.py` `765e806a67d748911890a0c3f1dde898f53425332b511f536e4c2544893d0983` / `.out` `4ff4f49a4809c1cca0aa13918afddefe4aa250972db5a44cca831ff4dc401c58` (4/4, replay identical) |
| coordinator audit | `indep_checkB2.py` X2 (exactly `V4` on each token permutes `Z_F`; every other octahedral rotation moves a defect out, witnessed); the kernel statements of item 2 read at L — `AUDIT-BRIDGE-R2.md` |

## What the receiving thread may assume

Items 1–3 at their labels; item 3's Clifford part as exact; item 2's certified non-implication at L. For explicit-cone
work: a cone invariant under any single-token rotation outside `V4` on either token is not K(Z_F) (nor, by C4.3, any
level-(ii) Bell-type cone with the same stabilizer).

## What it may not assume

That any clause of the realization theorem sources (b); that KZ7 is certified (it is an audited record); anything
about the manuscript (hold).

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-11 v1` and records in its `LOG.md`
whether and how it relies on it.
