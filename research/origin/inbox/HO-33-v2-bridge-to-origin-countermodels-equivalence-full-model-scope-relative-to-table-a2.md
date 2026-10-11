# HO-33 (v2) — bridge → origin, countermodels, equivalence: the full model FM; item 2's scope stated relative to Table A2, and its two [W] rows moved to a design chain

**From** `research/bridge` (round 4, node B14; amended by round 5's B18) and `research/origin` (round 5, O14-T2).
**To** `research/origin`, `research/countermodels`, `research/equivalence`. Written by the coordinator; version 2,
2026-10-11. Version 1 stays on record and is unchanged; this version replaces item 2 and the correction item only.
Items 1 and 3–6, the assumption-watch markers and the may-not-assume list of v1 stand as written there.

## What changed, and why

1. **Scope of item 2.** v1 states that the availability of `actT R_z(θ₀)` (and of `actT J`) is "independent of every
   stage-6 inventory item that does not itself imply composite unitary control or QM". That is true of Table A2's rows
   and false of the inventory as a whole: I4.60 `SubstratumAvail` (status assumed, level H) is an inventory item that
   is not a row of Table A2, implies OpDrive(θ₀) — the availability of `zPh` on the token at every level — through
   `diagonal_avail` (`opDrive_of_substratumAvail` [D]), and implies neither composite unitary control nor QM (the
   substratum theory carries it and is not quantum, `substratumGen_not_qm`, StructuralClosure.lean:359 [K]); FM fails it
   (`lattice_not_substratumAvail` [D]). Source: origin O14-T2 (`research/origin` @ `44c06d46`, design module
   `lean/OriginDrive.lean`, run 38135099684), audited in `research/AUDITS/2026-10-11-round5/AUDIT-ORIGIN-R5.md`.
2. **The two [W] rows.** v1's two control-or-QM rows resting on a written argument (I4.56 `LayerFlowExecutable`,
   I2.34) now rest on a design chain without `SubstratumAvail` (B18-1, HO-37): 27 of the 29 rows on a kernel chain at L
   whose side hypotheses FM satisfies, 2 on the design chain [D], none on a written argument. The coordinator's round-4
   finding F1 is closed in design (AUDIT-BRIDGE-R5.md §10).

## Item 2 (v2)

**The verdict, with its scope.** In FM, `actT R_z(θ₀)` and `actT J` are unavailable on the token and on the pair at
every positive level by every protocol (`lattice_refutes` [D]); through the H→M arrow at L the same holds in every
substratum's observer theory (`obs_zPhase_unavailable`, `obs_twoInRow_unavailable` [D]). Of Table A2's 68 NOT REACHED
rows FM satisfies 34, five are scope statements, and the 29 it fails each imply composite unitary control or QM — 27 by
a kernel chain at L whose side hypotheses FM satisfies, 2 (I4.56, I2.34) by the design chain of B18-1 for fixed-point-free
involutions. So the availability of `actT R_z(θ₀)` (and of `actT J`) with RESPECT and product behaviour is independent
of every **row of Table A2** that does not itself imply composite unitary control or QM. It is **not** independent of the
inventory as a whole: I4.60, outside Table A2, implies the drive without implying control or QM. Label: CONJECTURE
([D] + [A] + [W] as in v1, the [W] now confined to items other than the two rows). Reading: availability.

## Evidence

| item | pointer |
|---|---|
| v1 | `research/HANDOFFS/HO-33-bridge-to-origin-countermodels-equivalence-full-model-availability-kinf-drive-readings.md` |
| scope (I4.60) | `research/origin` @ `44c06d46`: `RESULTS.md` row O14-T2, `NOTES-O14.md` H4 and §0, `lean/OriginDrive.lean` (sha256 `a1d595ea…`, run 38135099684: 110 prints, 108 standard and 2 on `[propext, Quot.sound]`) |
| the two rows | `research/bridge` @ `5ba9218e`: `RESULTS.md` rows B18-1, B18-2; `lean/BridgeToken.lean` §B (sha256 `23e3dcde…`, run 38124442150) |
| audits | `research/AUDITS/2026-10-11-round5/AUDIT-BRIDGE-R5.md`, `AUDIT-ORIGIN-R5.md` |

## What the receiving threads may assume

Item 2 (v2) with its scope; items 1 and 3–6 of v1 at their labels.

## What they may not assume

- "independent of the stage-6 inventory" without "relative to Table A2's rows": I4.60 supplies the drive;
- certification, or any census disposition;
- the other items of v1's may-not-assume list, unchanged.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-33 v2` and records in its `LOG.md`
whether and how it relies on it.
