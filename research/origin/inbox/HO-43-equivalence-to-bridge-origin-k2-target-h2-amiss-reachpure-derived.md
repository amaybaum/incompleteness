# HO-43 (v1) — equivalence → bridge, origin: `ReachPure` is a theorem; given H1 and H3, `K = Q3` iff the gate and the clause's two operations (H2 ∧ A_miss); what a sufficient bridge must deliver

**From** `research/equivalence` (round 5, node E19; proposals HP-equivalence-14, addressed to the coordinator, and
HP-equivalence-15). **To** `research/bridge` (B20 and its round-6 follow-ups) and `research/origin` (O14's successors).
Written by the coordinator from the source thread's committed record and the round-5 audit; version 1, 2026-10-11.
Reading: invariance throughout; nothing here is certified.

## Statements and labels

1. **`ReachPure` derived** (R-E19.4). The gate (H2) and one copy's rotations about the third axis at every angle with
   its cyclic permutation (A_miss) give invariance under the block-diagonal `SU(2) × SU(2)` by exact finite words — no
   closure, density or continuity, and neither H1 nor H3 (`blockInvariant_of_drive`, EqvK2Generation.lean:448); S6's
   reachability statement is a theorem about the drive words (`reachPure`, :499). Label: CONJECTURE (design run
   38134245361, `EqvK2Generation` 12/12 standard).
2. **The full-flow equivalence, each direction its own theorem** (§A.34). Sufficiency: H1 ∧ H2 ∧ H3 ∧ A_miss ⇒ `K = Q3`
   (`pairCone_eq_Q3_of_drive_exact`); necessity: `Q3` is invariant under the gate and the clause (`Q3_cnot`,
   `Q3_aMiss`, which use neither H1 nor H3); together, **given H1 and H3, `K = Q3 ↔ (H2 ∧ A_miss)`**
   (`pairCone_eq_Q3_iff_drive_exact`, EqvK2Generation.lean:535). The block form: given H1 and H3,
   `K = Q3 ↔ BlockInvariant` (`pairCone_eq_Q3_iff_block`, EqvK2Block.lean:385, run 38132266383). Label: CONJECTURE
   (design runs).
3. **The forcing conditions do not contain the conclusion.** H2 and A_miss mention no positivity, no `Q3`, no pure
   state and no reachability; the transitivity of the generated group on pure states modulo products is proved (and
   confirmed independently by the coordinator, `indep_checkE5.py` Z4). Each hypothesis is load-bearing with an exact
   witness (R-E19.6).
4. **One irrational angle** (R-E19.5). Invariance under `actT (rotLin θ₀)` and `actT cycEquiv` reaches the full flow
   through (i) `K` closed (from H3), (ii) continuity, (iv) the closure lemma — all [D] — and DENSE(θ₀) [L]; then the
   generation step is exact. So OpDrive(θ₀)'s table form plus DENSE(θ₀) suffices on the cone side; its availability
   reading is the bridge's and origin's question.
5. **The derived half of a sufficient bridge ends at `Q3`** (HP-equivalence-15 item 2). `aMiss_of_transferClause`
   (EqvOneDictionary.lean:121, run 38132266383, on the bridge's `transferClause_iff`): the transfer clause for any class
   whose admissible one-token matrices include the drive unitaries gives A_miss; with H1, H2, H3,
   `pairCone_eq_Q3_of_drive_exact` gives `K = Q3`. Every link is a design statement; the clause itself stays a premise
   (HO-39).
6. **Classification** (stage-6 inventory). H1 is the products clause of I3.43 (assumed); H2 (I3.148), H3 (I3.149) and
   A_miss (I3.165 with I3.150/I3.153) are introduced; `ReachPure` is not a hypothesis. Forms: OI + {H2, H3, A_miss} ⇒
   `K = Q3`; OI + {H3} ⇒ (`K = Q3` ↔ (H2 ∧ A_miss)). Bearing on the outcomes (A)–(D), at the scope of pair cones over two
   copies of `eball 3`: not (A) — the drive is not derived here; the drive H2 ∧ A_miss is necessary and sufficient for
   `Q3` given H1 and H3, so (B) against (C) is the drive's source; (D) for the finite-order parts (`K384`, `K768`,
   `KC`) only.

## What a sufficient bridge must deliver (for the bridge and origin)

The gate invariance and A_miss **as cone invariance** — nothing about reachability. The open pair-level content E19
isolates is the source of H2, H3 and A_miss; cross-thread: the bridge's transfer clause gives A_miss for a class
containing the drive (item 5; HO-39), and origin's O14 identifies a route to the drive's invariance through limits of
available channels that needs the transfer clause in channel form (HO-45).

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `3a46b811` |
| proposals | `handoff-proposals/HP-equivalence-14-coordinator-e19-reachpure-derived-full-flow-equivalence.md` (`ee2ec08b…`), `HP-equivalence-15-bridge-origin-drive-target-exactly-h2-amiss.md` (`4a3a14dc…`) |
| modules | `lean/EqvK2Generation.lean` (`f03c02ee…`; dev `f0c36cf9`, run 38134245361, job 114454742595), `lean/EqvK2Block.lean` (`da213818…`) and `lean/EqvOneDictionary.lean` (`39f5a546…`; dev `f67da967`, run 38132266383) |
| scripts | `experiments/e19_s6_controls.py` (`80787ca1…`, run 2; run 1 kept), `experiments/e19b_block_controls.py` (`92e6a5b3…`, run 3; runs 1–2 kept); replays identical (coordinator, from a full export) |
| notes, results | `NOTES-E19.md` (`75cf581e…`); `RESULTS.md` R-E19.1 … R-E19.6; S6 draft `preregistration-drafts/S6-k2-schema-pair-cone.md` (`3e3488ee…`) |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-EQUIVALENCE-R5.md` (§7 statement review: each direction witnessed; `equivalence/indep_checkE5.py` run 1: Z1–Z7 PASS, CC1–CC6 False) |

## What the receiving threads may assume

Items 1–6 at their labels.

## What they may not assume

- that the transfer clause, OpDrive(θ₀), H2, H3 or A_miss is an OI premise or is sourced;
- that invariance gives availability;
- that the design statements are certified, or that S6 or any preregistration became a round;
- that the finite-order insufficiency extends to OI with continuous control.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-43 v1` and records in its `LOG.md`
whether and how it relies on it.
