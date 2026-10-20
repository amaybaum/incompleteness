# Corrections to DESIGN-NOTE.md (GEOM-ODD-1, PR #830), answering the review in `scratchpad/rev830/REVIEW.md`

| file | sha256 |
| --- | --- |
| `DESIGN-NOTE.original.md` (byte-identical copy of the note as reviewed) | `9b5ffea6a79360be76039bb01051d22dce944ce3fcef5560d8194f6d831baf15` |
| `DESIGN-NOTE.md` (corrected) | `26eed555616424c4a5708e767d1a2569dc4f0d9aa6738494d0e3fe696275091e` |
| `rev830/REVIEW.md` (the review answered) | `4837f8185e3dddd02a531b9e1609c67101c913f9965ae896fafb320ff0f30b9e` |

Recorded run outputs of the first pass are unchanged. New outputs are added beside them; the one script edited in place
(`scripts/a3_rigidity.py`, sha256 before `2e42a30b…f10ea`, after `8b12dc02…0b40d2df`) gains an optional `A3_REF`
input and behaves as before without it. The first attempt at `a14_orbit.py` (Fraction positivity on all 4064
outside-class twists) was stopped for cost; its partial output is kept as `work/a14-orbit.partial.out` (sha256
`ac48fbec…a9f`) and agrees with the final run on every twist it reached.

## New computations (this pass)

| script | output (sha256) | result |
| --- | --- | --- |
| `scripts/a14_orbit.py` (sha256 `2ee802c8…5639`) | `work/a14-orbit.out` (`b1e5a3f7…698f`) | candidate equals `(1 ⊗ diag(1,1,−1)) R (Zπ ⊗ (−1₃))` exactly; 32 distinct class members in `F`, all of the form `R ∘ diag(s)`, 8 involutions; 4096 sign twists in `F`; the 32 class members pass `posFwd` and `posInv` exactly on pools A ∪ B, 0 of the other 4064 do |
| `scripts/a15_members.py` (`a616b7e6…55e1`) + `scripts/a3_rigidity.py` with `A3_REF` | `work/a15-orbit-isolation.out` (`4ed4183b…a4d`) | every one of the 32 members: tightness confirmed exactly, tight rows rank 48 modulo `2³¹ − 1`, exact Stiemke certificate with all `yᵢ > 0` (minimum 0.096–0.383 under `max yᵢ ≤ 1`) |
| `scripts/a6_omegah_vertex.py`, quiet host (load 0.46 at start, 2.12 at end) | `work/a6-omegah-quiet.out` (`085b58bc…ecf5`) | 3000 rows built in 0.5 s; LP 44.0 / 69.2 / 122.6 s on 3000 / 4500 / 6000 rows; separation 0.2–8.2 s; violated 43 305 → 16 770 → 16 472; LP 3 unfinished within 300 s |
| `scripts/x3_eball7F.rev830-copy.py` (copy of the review's `x3_eball7F.py`) | `work/x3-rerun.out` | `eball 7`, family pair: frame consistent, 1024 free entries, `dim F = 960`; Ω_h pair `dim F = 960` |

## Changes, by finding

### B1 (blocking): the SLP candidate is a local relabelling of `cnot`

Verified independently with my own exact code (`a14_orbit.py`, Fraction arithmetic for the decomposition and the
class, exact int64 evaluation on positive integer rescalings for the 4096 twists), not only by re-running `x2_equiv.py`.

- §2.2: the novelty wording ("`G ≠ R`, `G ≠ R ∘ (Zπ ⊗ 1)`, `G² ≠ 1`", "non-product sign pattern") is removed. The hit
  is stated as the exact decomposition and as a member of `R`'s 32-point class; the reading says "recovered `cnot` up
  to a local relabelling in one of five starts".
- §F2: the target is restated as a set of 32 points forming one local-relabelling class, with the counts above, the
  exact transfer of whole-body positivity from `R` (`nativeGate_cnot`), and exact isolation in `K_A` of each member
  (the review asserted "at least 32 isolated points"; isolation of the 31 members other than `R` was not covered by
  the first pass's certificate, and is now checked member by member).
- The float off-pool diagnostic (`a13`) is dropped as evidence; positivity follows exactly from `R`'s. Its output file
  stays in `work/` as a recorded run.
- §2.3 item 4 and open question 5: the involutive ansatz keeps `R`'s class (8 of 32 members are involutions) and drops
  24 representatives, among them the SLP hit; the false premise that it would lose a gate class is removed.
- §2.3 item 5 cites the review's check that all 32 members share `R`'s commutation counts.
- §4: N1.2 is added. It records that the favourable branch N1.1 should have run the local-relabelling equivalence test
  (§A.31) and did not, and sets that test as an assumption-watch marker; §3.3 and §3.4 carry it as a countercontrol
  and a checkpoint.

### B2 (blocking): F3's throughput diagnosis

Verified independently by a quiet-host replay of the frozen generator's vertex step.

- The root cause is restated as LP cost (44 → 69 → 102–123 s per round, growing with the row count).
- "Vectorise row building" is removed from the top of §2.3; repair 1 is now LP warm-starting, solver choice and the
  all-rows-versus-incremental comparison, with the note that row construction (0.5 s for 3000 rows) is not a
  bottleneck at these sizes.
- The LP row counts are corrected: rounds 0, 1, 2 were solved on 3000, 4500, 6000 rows (`a6` prints the count after
  separation). The contended timings (74 s, 72 s, 135 s) are no longer used.
- "At least about 29 rounds" is withdrawn, with the reason (one round removed 26 535 violations, the next 298). §3.5's
  "over an hour" is withdrawn; §3.5 now gives the measured LP-time trajectory and states that no time-to-vertex
  estimate is supported until repair 1 is timed.
- "No pool-feasible vertex for `G`" is replaced by what the log shows: at least seven separation calls, `G` and `H`
  sharing one cut set, so the log does not say which vertex step was running at the deadline.

### B3 (blocking): claims stronger than their evidence

- F2 and N1: "cannot converge" becomes "did not converge to any member of the class in any start tried" (36 CI starts,
  9 local basin trials). The causal link between isolation and the stall is removed, with the observation that SLP
  converges to the same isolated points.
- N2 and F3: only `rank_ℚ ≥ 768` is exact (face of `P_A` of dimension at most 192); the rank 768 itself and the
  176–192 flat directions are float measurements; first-order flatness in the coupled relaxation is stated not to
  imply non-isolation in `K_A`. "Not isolated" is removed throughout, including §2.3's closing paragraph.
- N4: restricted to gates isolated in `K_A`; the `2²⁰` denominator cap of `exactify` is noted; the face case (rational
  gates near an irrational one) is stated. §3.6 is aligned.

### Notes (non-blocking)

- Stiemke normalisation stated: the note's `min yᵢ = 0.1774` is under `max yᵢ ≤ 1`; the review's `0.4747` is under
  `Σ yᵢ = 400` (quoted, not recomputed).
- Basin comparison: §2.2 states that the alternation's runs perturbed `H` alone and SLP's perturbed both, so the results
  are not like-for-like.
- π-rotation: the single counter-angle is replaced by the two-line argument (`relC` holds iff `R_θ` commutes with
  `diag(1, 1, −1, −1)`, iff `sin θ = 0`), with the exact witnesses kept as agreement.
- P4: a stage checkpoint is added (the `eball 7` run must reach the Ω_h control's stage, pool-feasible `G` and `H`
  vertices and a recorded residual trajectory), in §3.1(d), §3.2 and §3.4; a stalled `eball 7` run leaves `HIT` unread.
- P1's bite: §2.3 item 2 records that `a10_slp.py` reads `lam-eball3.json`, a reference table, which a frozen generator
  must not read.
- Held-out calibration: §2.2 and §3.1(b) record that SLP was chosen after observing `eball3`; P2's `eball3` control
  becomes the held-out `Ω_R(1, 1; 2)` (family parametrisation, family pool rules, unused seeds); open question 2 is
  reworded accordingly.
- Ω_h P2 PASS: §3.1(b) and open question 7 state that a PASS on a pool-blind point of the first-order-flat face
  calibrates only relative to the pools; question 7 now names the exact check (modular nullspace, rational
  reconstruction, integer check, then a curve in `K_A` or "first-order flat").
- §4's closing line: two passes made, the second produced a NEW finding, so the fixed point is not reached.

## Owner-decision list, revised

Questions 1, 2, 4, 5 and 7 are reworded (repair 1 is LP cost; the `eball3` control is the held-out family form; P4
carries the stage condition; the involutive ansatz keeps `R`'s class; Ω_h's flat directions with the exact check and
the PASS caveat). Questions 3 and 6 are unchanged.

## Not verified in this pass

- The review's Stiemke figure `0.4747` under `Σ yᵢ = 400` and its `G`-only / `H`-only countercontrol (`x1b_gonly.py`)
  are quoted, not re-run.
- The review's frozen-generator replay of CI starts 1–3 and its unmodified `controls_gen.py` run are quoted, not re-run.
- The review's commutation counts over all 32 members (`x4_sym.py`) are quoted; only `R`'s were computed here (`a7`).
- Whether Ω_h's flat directions extend to curves in `K_A` (open question 7) is not computed.
- The LP times are from single runs on this host; the 122.6 s versus 101.6 s spread at round 2 between this run and
  the review's shows run-to-run variation, and the load rose to 2.1 by the end of this run.

## Re-review R1 (applied by the session lead)

- Line 54: the accepted set narrowed to "among the 4096 sign twists in F the verifier accepts exactly 32, one local-relabelling class; whether other points of F pass is not determined".
- §F2: `a15-orbit-isolation.out` labelled a filtered log.
- §2.2: "a rate against at least that 32-point class".
- N1 verdict: "includes a set of 32 points (all the accepted sign twists) …, other accepted points of F not excluded".
- DESIGN-NOTE.md sha256 26eed555616424c4a5708e767d1a2569dc4f0d9aa6738494d0e3fe696275091e → 918b15b0b79fc03bec0082dfd9233f0c92fb622e7a604383dea66336aca40894.

## Publication copy

- Local working paths are replaced by `<work-dir>`, `<review-dir>`, `<scratch>/` and `<clone>` in the files below; no other byte changes. sha256 of each file before the replacement:
  - `DESIGN-NOTE.md`: `918b15b0b79fc03bec0082dfd9233f0c92fb622e7a604383dea66336aca40894`
  - `DESIGN-NOTE.original.md`: `9b5ffea6a79360be76039bb01051d22dce944ce3fcef5560d8194f6d831baf15`
  - `work/a10-s3.full`: `d2cd9c5574aa9b7876002c0c7f44d9cdbfb47906f1687ce232d30b1fbf4cf1f4`
  - `work/a3-eball3-AB.out`: `dbdac8856a889fe8ac44787cc6b668d5919d189eec3ad145f842d48d0d40cc2c`
