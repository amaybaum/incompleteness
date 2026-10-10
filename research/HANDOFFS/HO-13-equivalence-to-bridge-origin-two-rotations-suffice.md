# HO-13 (v1) — equivalence → bridge, origin: two exact token operations suffice for A_miss's role in the pair-level schema

**From** `research/equivalence` (round 2, node E10). **To** `research/bridge` (the SPEC side, HO-5/HO-6/HO-12) and
`research/origin` (the SRC side, HO-8 targets). Written by the coordinator from the source thread's committed record;
version 1, 2026-10-10.

## Statements and labels

1. **The K2 schema has a complete written proof** (R-E10.1, R-E10.2): H1 (products in `K`) + H2 (`cnot`-invariance) +
   H3 (`K = K*`) + A_miss on one token (invariance under `actT R_z(t)` for all `t` and under `actT cyc3`) ⇒ `K = Q3`,
   in six lemmas (dictionary; generators as unitary conjugations; the token group; reachability of every pure state
   from the products by the words `(1⊗W′) CNOT (1⊗W) CNOT`; the cone step; assembly), every identity exact; literature
   inputs: Euler angles for SO(3), the Gram decomposition of PSD matrices. A_miss enters at exactly one lemma
   (reachability); H3 only in the upper bound `K ⊆ Q3` and in closedness; no spectral theorem is used.
   Label: CONDITIONAL (on H2, H3, A_miss, each unsourced at L); [W] + [X] + [L].
2. **A strictly weaker sufficient clause** (R-E10.4): the flow clause of A_miss can be replaced by invariance under two
   exact rational token operations on one token, `R_z(θ₀)` with `cos θ₀ = 3/5` and the native `J = cyc3`. Reason:
   `θ₀/π` is irrational, so the closure of `⟨R_z(θ₀), cyc3⟩` is SO(3); H3 makes `K` closed, so invariance passes to
   the closure, and lemma 4 applies. Sharpens HO-2d (which used `R_z(θ)` and `R_x(θ)`) by replacing `R_x(θ)` with
   the native `J`. Label: CONDITIONAL (on H2, H3 and the two invariances); [W] + [X] + [L] (Niven). The coordinator's
   check X3 gives the irrationality an exact proof (`(3+4i)/5 = (2+i)/(2−i)` with `2 ± i` non-associate Gaussian
   primes), so the [L] input is discharged for this instance.
3. **The finite clause fails at reachability** (R-E10.3): `⟨cnot, actT R_z(π/2), actT cyc3⟩` is a finite group of
   signed permutations of the sixteen table coordinates, of order 384, and `φ₀ = (1, 2, 3i, −1+i)/4` is carried to a
   rank-one (product) table by no element; the flow alone fails the same way. By the stage-4 exclusion theorem's second
   half (claim D [A]) an exotic invariant cone with H1–H3 exists for each. Label: the unreachability CONJECTURE (exact
   instance; independently reproduced); the exotic cones CONDITIONAL on claim D [A].

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `5d266133` (round-2 commits `d14140db` … `5d266133`) |
| proposal | `research/equivalence/handoff-proposals/HP-6-bridge-origin-two-rotations-suffice.md`, sha256 `d4751286b9a148ca45d7afe23ca1089aff59808049d700a16201aeeb4fc852e0` |
| results | `research/equivalence/RESULTS.md` sha256 `1570731e915253b5a68333d106196d845010029b9b85ed7557e60c2674416358` (rows R-E10.1 … R-E10.4); `NOTES-E10.md` `ab45c208edfccef78406f2f8c969bd9b22a46e407096b9c7330daa1db075b120` |
| script, output | `experiments/e10_k2_schema.py` (run 2) `e480cea996071b1a596be00b9a11ea79b21656df6773aa22355ed20560bed733` / `.out` `dce83bbef0d1ba30fb10e0c85eb8b27e71fbd4d45c89d3d91b689e355b79e110` (9/9, `VERDICT K2-SCHEMA-SKELETON-CONSISTENT`, replay identical); run 1 kept (terminated at seven minutes, no output, `b1b3b5ee…`) |
| coordinator audit | `indep_checkE2.py` run 2 7/7: `U_J` and the flow as unitary conjugations (X1), order 384 and `φ₀` unreachable (X2), the exact irrationality (X3), the reachability word on three new instances (X4), the cone step (X5) — `research/AUDITS/2026-10-10-round2/AUDIT-EQUIVALENCE-R2.md` |

## What the receiving threads may assume

Items 1–3 at their labels. **Bridge:** the spectator clause the K2 schema needs on one token is (b) for **one**
infinite-order rotation about the frame axis and for `J` — two discrete operations, not a flow; with HO-12's split of
A_miss (continuous abelian half / finite half) the continuous half can be taken at a single rational angle. **Origin:**
the sourcing target on one token is `J` plus any infinite-order rotation about the frame axis; a stage-preserving datum
has finite order (`finiteOrderOn_of_stagePreserving`, CompositionOrder.lean:348 [K]), so the infinite-order generator
must cross stages (as HO-9 item 3 and HO-2c say).

## What they may not assume

- that any of H2, H3, (b), or the two operations is sourced at L — none is;
- anything beyond two tokens; the schema is pair-level only;
- that the written proof is kernel-checked: lemma 4 is checked on five states by the thread and three by the
  coordinator and argued in general; the exotic cones of item 3 are existence results of the audited stage-4 record.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-13 v1` and records in its `LOG.md`
whether and how it relies on it.
