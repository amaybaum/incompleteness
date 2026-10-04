# Round L3B — orthogonal rule controls and the hidden-law factor under the fixed interface I₃: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #786.

- **`D`** — `b7af4852b79fa3bfa90e9b5c2eca3aca6890395a`, the head of `main` after round CC-2 landed (push run
  37153338826, every job green).
- **`F`** — `d04ab62799afc882c1bf5fb730427495c73c97b9`, parent `D`; `delta(D, F)` is the preregistration alone, blob
  `588404e93867d0556600a5fe4160e4f6bcba9354`, sha256 `b493b34bf79f98f4…`. Its exact-head `workflow_dispatch` run
  37165488993 (attempt 1) concluded `success`, 32 of 32 jobs, its `check-run` attestation; the owner designated `F`
  on PR #786.
- **Shape** — non-sealing; stages C1, S1, S2, one repair commit under preregistration §8, and this note (S3).

**Outcome:** `L3B-READ` (preregistration §9: every run cell of Block 1 carries a label of §5 other than INCONCLUSIVE,
the decision table has a determined row, every Block-2 cell is complete with its tally, every gate V1–V12 passed).
Bands unchanged (§9).

## The execution

| Commit | Content |
|---|---|
| `66ea471b` | C1: `code/` (the ten sealed modules copied verbatim, §7.1; the round's six modules, §7.2), `controls.py`, logs V2–V5 and the memory measurement |
| `3524bb3b` | S1 part 1: gates V6 and V7; Stage A for R_LS, R_NL and R_5 |
| `5eff7c82` | S1 part 2: Stage B for R_LS and R_5; R_NL not entered (0 advancing κ) |
| `af8f37bc` | S1 part 3: Stage C for R_LS and R_5; R_NL not entered (no selected κ) |
| `d26d8bca` | S1 part 4: gate V8 |
| `5b4e68e1` | S1 part 5: gate V9 |
| `1eb3e76a` | S1 part 6: gate V10; S1 complete |
| `00501afe` | S2: the eight Block-2 artifacts and logs, the eight V11 logs, the V12 log; S2 complete |
| `081bfbbb` | parser-only repair of `controls.py` under §8 (below) |
| this commit | S3: this note; candidate `E` |

Every sweep ran in a single driver invocation with no checkpoint resumption (0 checkpointed jobs at the start of each
of the 21 sweeps); checkpoints lived outside the repository and were never committed.

## Block 1 — the rule matrix (preregistration §3–§5)

Stage A (horizon 3, 3; 40,404 protocols; all 143 κ), Stage B (4, 4) for the advancing κ, Stage C (4, 5) for the
§4 selection.

| Cell | Stage A | Stage B | Stage C | Cell label |
|---|---|---|---|---|
| R_LS | 76 ADVANCE (rank 4, dims [2, 3, 4]); 67 NOT-INVASIVE (64 at rank 1, 3 at rank 4) | 76 of 76 AT-RANK (rank 4, dims [2, 3, 4, 4]) | 3 of 3 C-CONSISTENT (dims [2, 3, 4, 4, 4]) at κ ((0,1),(0,1)), ((0,1),(0,2)), ((0,1),(0,3)) | EXPOSED |
| R_NL | 143 OVER-RANK (certified ranks 8 to 17; dims [2, 4, 7] to [2, 5, 12]) | not entered: 0 advancing κ by the frozen advance rule | not entered: no selected κ | OVER |
| R_5 | 76 ADVANCE (rank 4, dims [2, 3, 4]); 67 NOT-INVASIVE (64 at rank 1, 3 at rank 4) | 76 of 76 AT-RANK (rank 4, dims [2, 3, 4, 4]) | 3 of 3 C-CONSISTENT (dims [2, 3, 4, 4, 4]) at the same three κ | EXPOSED |

R_NL's certified Stage-A ranks: 8 (7 κ), 9 (8), 11 (2), 12 (4), 13 (42), 14 (7), 15 (18), 16 (28), 17 (27). The
advancing sets of R_LS and R_5 are the same 76 κ, in the frozen order, as R_LL's at 3A (§0); their Stage-B and
Stage-C records carry the same verdicts and dims as R_LL's sealed artifacts (`48296b18`, `ceb33dc9`).

**Decision table (§3.2), read in order:** R_LS has no κ OVER-RANK, R_NL has 143 κ OVER-RANK, R_5 has no κ OVER-RANK;
the first row holds. **Reading (frozen):** rank behaviour tracks edge-permutivity; neither A5 nor A4-S is the
operative axis. The §3.2 predictions (R_LS and R_5 no κ OVER-RANK; R_NL ≥ 1 κ OVER-RANK) held. R_5 separates
edge-permutivity from A5 and A4-S by construction (§3.1, D1): it violates both and is permutive in its left edge
only, and its three stages are record-for-record identical in verdict and dims to the linear cell's.

No label is R4-CLOSED (§5): this round claims no structural theorem for any new cell; 3A's statement for R_LL is cited
as 3A states it (§0).

## Block 2 — the hidden-law factor (preregistration §6)

Stage A only, all 143 κ per cell, on the cone enumerator `hsim3b.py`; labels of §6.

| Cell | OVER-RANK | NO-OVER-RANK-AT-A | NOT-INVASIVE | non-invasive κ with rank > 4 | artifact |
|---|---|---|---|---|---|
| R_LL × H₁ | 80 (all rank 5) | 60 (all rank 4) | 3 (rank 4) | 0 | `4c8e160a` |
| R_LL × H₂ | 0 | 140 (all rank 4) | 3 (rank 4) | 0 | `460a4024` |
| R_LS × H₁ | 80 (all rank 5) | 60 (all rank 4) | 3 (rank 4) | 0 | `1286d5ca` |
| R_LS × H₂ | 0 | 140 (all rank 4) | 3 (rank 4) | 0 | `a682094f` |
| R_NL × H₁ | 143 (ranks 11 to 17) | 0 | 0 | 0 | `db1eef92` |
| R_NL × H₂ | 143 (ranks 11 to 17) | 0 | 0 | 0 | `085ecd9d` |
| R_5 × H₁ | 142 (14 at rank 7, 128 at rank 8) | 0 | 1 (rank 7) | 1 | `043fae70` |
| R_5 × H₂ | 0 | 140 (all rank 4) | 3 (rank 4) | 0 | `4553283a` |

Facts of the artifacts:

- R_LL × H₁ and R_LS × H₁ have equal tallies and equal rank and dimension profiles (OVER-RANK: 72 κ at rank 5 with
  dims [2, 4, 5], 8 κ at rank 5 with dims [2, 3, 4]; NO-OVER-RANK-AT-A: 60 κ with dims [2, 3, 4]) but not the same
  κ: their OVER-RANK sets share 32 κ and each holds 48 κ the other does not; in each cell 32 of the 80 OVER-RANK κ
  are among the 76 κ that advance under H₀ and 48 among the 67 that are NOT-INVASIVE under H₀. Both OVER-RANK sets
  are contained in R_5 × H₁'s 142, which holds 14 κ beyond their union. R_LL × H₂ and R_LS × H₂ agree label for
  label and rank for rank at every κ.
- Under H₂ the three NOT-INVASIVE κ are ((0,1),(3,2)), ((1,0),(2,3)) and ((1,0),(3,2)) in every cell that has
  them, each at rank 4 with dims [2, 3, 4]; under H₁ the same three κ are NOT-INVASIVE at rank 4 in R_LL and R_LS.
- R_NL's certified rank at each κ is the same under H₁ and H₂: 11 (3 κ), 13 (60), 15 (16), 16 (16), 17 (48).
- R_5 × H₁ differs from R_LS × H₁ in count and rank: 142 κ OVER-RANK (rank 8: 96 κ with dims [2, 5, 8], 32 with
  dims [2, 5, 7]; rank 7: 8 κ with dims [2, 5, 7], 6 with dims [2, 4, 7]) against 80 at rank 5; κ
  ((1,0),(2,3)) and ((1,0),(3,2)), NOT-INVASIVE in every other cell, are OVER-RANK (rank 8) under R_5 × H₁; the one
  NOT-INVASIVE κ, ((0,1),(3,2)), has certified rank 7 and dims [2, 4, 7], the only non-invasive κ with rank above 4
  in the block (§6 reports the rank and the over-rank flag of a NOT-INVASIVE κ and assigns it no other label).

The §6 predictions (not criteria): under H₁ certified rank exceeds 4 in the edge-permutive cells (R_LL, R_LS, R_5),
which is observed at 80, 80 and 142 κ; under H₂ no OVER-RANK in the edge-permutive cells, observed; the interaction
reading, rule × H present for the edge-permutive cells and absent for R_NL, is as stated. NO-OVER-RANK-AT-A means
exactly "no OVER-RANK detected at Stage A" for that (rule, H, κ) (§6, D4); the block assigns no cell label of §5.
The preregistration made no prediction about the size or rank of the H₁ effect, so the difference between R_5 × H₁
and R_LS × H₁ is recorded here as measured and not read; it is outside §3.2, which is read at H₀ only.

## Gates (preregistration §7.3)

| Gate | Result | Log |
|---|---|---|
| V1 | the ten sealed modules' sha256 equal §7.1 (checked by `controls.py` at C1 and at E) | — |
| V2 | census equals §3: LS affine, uses the centre, permutive in all three arguments; NL not affine, no centre, permutive in none; R5 not affine, uses the centre, permutive in the left edge only; linear affine, no centre, permutive in both edges; nonlinear and majority as RECORD; 6 of 16 two-variable functions permutive in some argument, all affine | `V2.log` OK |
| V3 | `record3_fast` = `record3_sim` on LS, NL, R5: 180 protocols, 0 mismatches | `V3.log` OK |
| V4 | `hsim3b` on H₀ = `record3_sim`: 150 protocols, 0 mismatches; = `record3_fast` on the full Stage-A set (40,404) for three κ under `linear` and `R5`: 0 mismatches, enumerator 23 to 26 s per κ against the window simulator's 5 to 7 s | `V4.log` OK |
| V5 | `hsim3b` on H₀, H₁, H₂ = brute force on 54 protocols with ≤ 3 leaps, 0 mismatches | `V5.log` OK |
| V6 | R_LL instrument replay against the sealed 3A artifact (`9b88a7cc`): §7.3 lists ten entries (the nine positions 0, 18, …, 142 and κ ((0,1),(0,1))), which name nine distinct κ, position 0 being ((0,1),(0,1)); the driver deduplicated the list and replayed the nine, 9 of 9 MATCH field by field; the sealed entries are kept in `results/v6_sealed_entries.json` (`c020ba87`) | `V6.log` OK |
| V7 | R_NS-n at positions 0, 71, 142: certified ranks 8, 13, 7; R_NS-m: 13, 20, 13; all six OVER-RANK | `V7.log` OK |
| V8 | Stage-A replay on the reference simulator: R_LS 10 jobs, R_NL 11, R_5 10 (the nine positions plus the first κ of each verdict class not covered), all MATCH. The background command carrying R_5's replay was stopped by the harness at its 2 h limit after 4 of its 10 jobs (all MATCH); the log keeps that attempt as evidence and the gate's verdict rests on the complete 10-job rerun that follows it in the same log | `V8_R_LS.log`, `V8_R_NL.log`, `V8_R_5.log` OK |
| V9 | Stage-B replay for κ ((0,1),(0,1)): reference table of 1,012,435 protocols in 507 chunks on the reference simulator, then the unchanged `analyze`: R_LS MATCH (AT-RANK, rank 4, dims [2, 3, 4, 4]), R_5 MATCH (same); R_NL SKIPPED, recorded (no κ advanced) | `V9_R_LS.log`, `V9_R_5.log` OK; `V9_R_NL.log` SKIPPED |
| V10 | G identities on all 143 κ at the Stage-A horizon: G2 143/143, G3norm 143/143, G3idle 143/143 for each of R_LS, R_NL, R_5 | `V10_*.log` OK |
| V11 | per Block-2 cell, at positions 0, 71, 142: `run_all_H` = `run_H` on all 40,404 Stage-A protocols (0 mismatches), both = brute force on the first 40 protocols with ≤ 3 leaps in lexicographic order (0 mismatches), the H₀ record of the κ under the enumerator = the window-simulator record (3A's sealed entry for R_LL, the Block-1 Stage-A record otherwise): MATCH; 8 cells × 3 positions, all clean | `V11_<cell>_<H>.log` OK × 8 |
| V12 | Stage A of R_5 rerun by the frozen driver from an empty checkpoint root after every other stage of S1 and S2: 143 κ recomputed, artifact sha256 `dcf04f62d4de5c7748cfda979d562b22eaa2b3f0f84c3e87c4f717b63800229b` unchanged; the driver's progress lines appended to the S1 log `stageA_R_5.log` during the rerun are carried in `V12.log` and that log restored to its sealed content | `V12.log` OK |

`controls.py --check C1` passed at C1; `--check E` passes at E with zero errors, printing the three cell labels,
the decision row 1 and the eight Block-2 tallies above; `--self-test` catches 3 of 3 mutations (a dropped Stage-A
record, an alien Block-2 label, a gate log without its OK line).

### The checker's parser defects, found at E and repaired under §8

The first run of `controls.py --check E` at the complete S2 state (`00501afe`) did not pass. Each of its failures was
in the frozen checker's reading of the frozen logs and artifacts; no gate output, artifact, label set, selection
rule, tally or mutation expectation was involved:

1. the gate-line pattern required `GATE Vn … OK` at the start of its line, while the V6, V8 and V9 drivers print it
   after a summary (`REPLAY-A R_5 10 jobs, mismatches 0; GATE V8 OK`): seven logs reported as carrying no OK line
   (V6, the three V8, the three V9);
2. the per-cell V9 log was checked for a gate named `V9_<cell>` rather than the emitted `GATE V9 OK` or
   `GATE V9 SKIPPED`;
3. the layers artifacts, whose records carry the G-identity fields and no verdict field, were scanned for a verdict
   label with an empty label set, raising `KeyError`.

Preregistration §8 allows repairs between stages to `controls.py`'s reporting and to the logs' format without
criterion change. With the owner's authorization the three were repaired in `081bfbbb`, a single-parent child of
`00501afe` touching `controls.py` alone (sha256 `b46bec3b…` at C1, `654a3237…` after the repair): the gate text is
accepted anywhere in its line, the V9 per-cell log is checked for gate `V9`, and an artifact given no label set is
not scanned for a verdict field. `00501afe` is the S2 boundary; no S2 file changed. After the repair `--check E`
reports zero errors and `--self-test` catches 3 of 3.

## Artifacts and modules

Result artifacts (`results/`, sha256 first eight hex digits): `stageA_R_LS` `da53c729`, `stageA_R_NL` `4b1b5012`,
`stageA_R_5` `dcf04f62`; `stageB_R_LS` `2ad89c3e`, `stageB_R_NL` `4f53cda1` (empty list), `stageB_R_5` `fae8bcc2`;
`stageC_R_LS` `4bcbfab0`, `stageC_R_NL` `4f53cda1` (empty list), `stageC_R_5` `1ca4769b`; `layers_R_LS` `014be850`,
`layers_R_NL` `49034310`, `layers_R_5` `718b3a01`; `controls_RNS` `2ecdaddc`; `v6_sealed_entries` `c020ba87`; the
eight Block-2 artifacts as tabulated above.

The round's modules (§7.2), at C1 and unchanged since: `rules3b.py` `4fc004df`, `hsim3b.py` `e58e0a49`,
`analysis3b.py` `cf9d437d`, `driver3b.py` `a4e77e9b`, `replay3b.py` `b61a0a1a`, `validate3b.py` `5a5a8ed3`.
`controls.py`: `b46bec3b` at C1, `654a3237` from `081bfbbb`. The ten sealed modules carry the §7.1 hashes (V1).

The C1 revision of `hsim3b.py` extracts the cone's site bits on demand instead of materializing one array per site:
peak RSS on the 216 six-leap Stage-A protocols of one κ under H₁ fell from the prototype's 4.55 GB to 1.38 GB
(`C1_memory.log`, 23.8 s), so Block 2 ran with 3 workers under §11's rule, and V2–V5 were rerun on the revision at
C1 with the results above.

## Timings (wall clock, 4 cores, 15 GB)

| Sweep | Workers | Duration |
|---|---|---|
| Stage A, each of R_LS, R_NL, R_5 (143 κ) | 4 | 3.5 to 3.6 min |
| Stage B, R_LS and R_5 (76 κ each) | 4 | 50 min each |
| Stage C, R_LS and R_5 (3 κ each) | 4 | 18 min each |
| V7 (6 jobs) | 3 | 13 s |
| V8, per cell | 1 | 10 to 11 jobs; R_5's complete rerun inside one invocation |
| V9, R_LS and R_5 (507 chunks each) | 4 | 52 to 53 min each |
| V10, per cell (143 κ) | 4 | 15 to 16 min |
| Block 2, each H₁ cell (143 κ) | 3 | 19 to 20 min |
| Block 2, each H₂ cell (143 κ) | 3 | 1.3 to 1.4 min |
| V11, each H₁ cell (three positions) | 1 | 2 h 25 min to 2 h 29 min (the four cells run concurrently, one process each) |
| V11, each H₂ cell | 1 | 2 min |
| V12 (143 κ) | 4 | 4 min |

The V11 cost is the per-protocol path `run_H` on the full Stage-A set, about 10 s for each of the 216 six-leap
protocols per position; the trie path shares those cones and runs the same set in 22 to 26 s.

## Interpretation limits (preregistration §10, restated)

Evidence about the interface I₃, observer OBS-R, radius r and the hidden laws H₁, H₂ as defined, at the horizons run,
for the six rules of §3 as the whole class; Block 2's results are stated for H₁ and H₂ at Stage A only. Not a QM
test: no cell outcome bears on strict convexity, continuous reversible transitivity, composites or any Q-layer
premise. Edge-permutivity is a property of F as a Boolean function; the decision table attributes rank behaviour to
it within the radius-1 binary second-order class and says nothing about rules of larger radius or alphabet. The
round touches no manuscript, none of the five deferred correction items, no CC-2 decision, and none of the
architectural questions named in §0.
