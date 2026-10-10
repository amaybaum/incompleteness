# AUDIT-R — coordinator's audit of R6 (stage 6, step 3: the countermodel reassessment)

Base L = `9f9f8257…`, read-only. Written 2026-10-10, 18:45Z, after R6 reported (`.end_marker` 18:34:13Z) and
against the predictions and decision rules fixed beforehand in `pt/audit/stage6-inputs/PRE-AUDIT-R6T6.md`
(18:05Z). Inputs read: `pt/R6/RESULT.md` (sha256 `15cdea9d…`), `pt/R6/REASSESSMENT.md` (`1ff62ad6…`), the six
script outputs, and R6's §4 hash list. Nothing under `pt/R6/` was modified.

## 1. Mechanical verification

- **Hashes.** `r6_listed_hashes.txt`: all 59 files R6 lists in RESULT §4 verify (`sha256sum -c`, 59/59 OK);
  RESULT.md itself hashes to `15cdea9d…`.
- **Replays.** `replay/REPLAY-LOG.txt`: the six final scripts (`r1_inventory`, `r2_cones`, `r3_seeds`,
  `r4_tables`, `r5_realization`, `r6_single`) re-run from a copy under `R-audit/replay/` with `python3 -I -B`,
  stdout and stderr byte-identical to R6's own outputs, 6/6 (18:38:15Z–18:39:05Z).
- **Integrity.** R6's start (17:57Z) and end (18:34:13Z) markers carry the manifest checks, base HEAD = L,
  clean porcelain, the eleven protocol prefixes and sidecars; sweep clean; writes only under `pt/R6/`; one
  transient file of its own removed. Kept failed runs: `r1` 1–2, `r2` 1–2, `r3` 1; header-only reruns `r1` 3,
  `r2` 3–4 kept. Every `.err` is `exit 0`.

## 2. Comparison with the pre-audit predictions (PRE-AUDIT-R6T6 §2)

| prediction | R6's result | match |
|---|---|---|
| every pair-level kernel theorem at L is SATISFIED by K(Z_F), K(E0), Q3 alike or NOT REACHED; none excludes a cone | 118 SATISFIES per alternative; EXCLUDED-BY-L: none; Q3 column fails nothing (r4 control) | yes |
| every H-, M-, G-level item NOT REACHED (no bridge at L) | 68 NOT REACHED per alternative; the 208 NOT REACHED cells name the absent bridge (86 "level M", 12 "level G", 10 mixed spans, 18 "no ≥3-token structure", 12 P-STAGE2/P-ACT2 routing, 6 A3/A4, 3 I1 bridge-field none) | yes |
| FAILS = do-not-assume hypotheses only: (b) in every form, IE₁, Q3/PSD reachability, pair-level T | 13 FAILS: IE1, IE1Drive, Q3-reachability, (b_S4), (b_n), (b_R1), (b_DJ), FC, K2's compatibility clause, [D] KT4Core H and FCC (uniform), PT-record H and T; §7 pressure test: no FAILS row is a theorem or definition at L | yes (the [D] four-token hypotheses and PT-record H were not in my list; they are hypotheses, not L items, so the rule holds) |
| K(E0) additionally fails the NOT-only and SWAP forms | `actC nflip`, `actT nflip` move K(E0) (pairing −1); SWAP −5/13 (r2 C8) | yes (P5b: −1 witness, 3/13 / −5/13) |
| K(Z_F) fails κ | K(Z_F) leaves itself under `cyc3` (−1/2) and under the drive's quarter-turn about x (−1/2); the κ Bell seed is a separate EXOTIC-E alternative (A4b) | consistent (P5a: `actC J` moves `z_(1,1)` out, −1/2) |
| no embedded-observer realization attached at L, with the mechanical ground | r5: only the root aggregator reaches both a pair module and an H-level realization module; CompositeInterface.lean:53 algebraic only; 0 text lines carry both vocabularies | yes (AUDIT-I §2 import-graph check: same conclusion) |
| single-token structure inherited from Q3 (P6) | §5: inherited by construction; r6 12/12 exact checks with countercontrols | yes |

Decision rule of PRE-AUDIT §3 for R6, clause by clause: every SATISFIES/FAILS for the explicit cones is backed by
an exact `r2` line with a Q3 control (`MAP … Q3 control invariant`; countercontrols CC e_{3/2}, nonorthogonal pair,
twin, Q3-not-reflY-invariant, Q3-no-defect); every NOT REACHED names the bridge; no H-level item is marked
satisfied or failed for a cone-level alternative (the `hmg` class is NOT REACHED throughout); statements (i)–(iii)
are present per alternative (REASSESSMENT §4); the FAILS sets consist of hypotheses only. **R6 is accepted.**

## 3. Spot checks against my own earlier code

- The R1 witness value −2383/5316 for K(Z_F) under the order-3 rotation about (5,1,1) is the value my stage-4
  audit found with its own witness (`pt/audit/Y/indep_checkY.out` line 37, AUDIT-Y R7).
- The `actC J` / `cyc3` witness −1/2 for K(Z_F) is P5a of `preaudit_r6t6.py` (run 2).
- The K2-guard pairing figures differ from mine only by witness choice and normalization (R6: −1 and −1/8 for
  `actT reflY` on K(E0), K(Z_F); mine: −1 for the joint eigenvector against E0, −2 for `idW` against the singlet),
  the same conclusion: the no-go constrains the operation, not the cone (P1a–P1d).
- The orbit minima 5/256 at 16/48/768/384 rays, the X⊗X forms 1/9 and 121/42, the monomial bound 1/15 and the
  seed windows (4609/4608, 517/512, 513/512, 17409/17408, c = 2 for the Bell seed) agree with AUDIT-Y, AUDIT-Z,
  AUDIT-C (level (ii) orbit counts) and AUDIT-D.

## 4. Items R6 records that the integration note and T6 carry

1. **A1.5 gap (coordinator's).** `K({F, cnot F})` and `K(e_c)`, named in `PROTOCOL-STAGE6.md` step 3, were omitted
   from the amendment's A1.5 list and are not reassessed (RESULT §3, REASSESSMENT §1, §9). Covering argument,
   stated for T6: every pair-level item at L that reaches a cone constrains the gate on products, the effects,
   the single-token slices, the `maxCone` bound or the operation `actT reflY`, never the cone beyond H1–H3; R6's
   A3 argument applies to any closed self-dual `cnot`-invariant cone `K ⊇ SEP` (then `K = K* ⊆ SEP* = maxCone`).
   Where the stage-3 record establishes H1–H3 for those two cones, the same 199-item table applies; T6 is told
   they are not reassessed and may rely on the explicit cones and the EXOTIC-E seeds only.
2. **Node T UNDECIDED** for the existence-only alternatives (stage 4: EXCLUDES-KNOWN only). No change.
3. **Assumption-watch marker (NEW, R6 §6).** The one H-level composition clause at L, Main.md:552, takes the local
   instruments' action `I_a ⊗ I_b` as input, the composite action every alternative lacks; so L's realization
   statements cannot be read as realizing an exotic pair with local interventions, and Main.md:562's
   non-quantum families are not stated for cones in `W 3`. Realization: open; obstruction: none proved.
4. **K∞-Geom's pair reading** fails for Q3 and the explicit cones alike (r2 C10; I4.236's scope): not a
   discriminator.
5. **Input outside the listed set.** R6 read the stage-3 record `pt/X/x8_fcc_crossnote.out` and the matching
   script lines (the FCC witness arguments). `pt/X/` is a stage-3 thread record under `pt/`, which the stage-6
   protocol's read rule allows ("everything under `pt/` except …"); A1.2 lists the stage-4/5 records explicitly
   and the stage-3 ones by their audits. Allowed; recorded because A1.2's list is narrower than the protocol's.
6. **Deviations R6 disclosed** (RESULT §5): header times first estimated, corrected to `date -u`, forcing
   header-only reruns (outputs byte-identical); one version check via `python3 -I -B -c`. Cosmetic.

## 5. Verdict

R6's reassessment stands: for every alternative, no item at L excludes it; the FAILS rows are hypotheses
(do-not-assume items, [D] four-token hypotheses, PT-record candidates) and never theorems or definitions at L;
H-, M-, G-level items are NOT REACHED because L has no H→P, M→P or G→P bridge (G6's NO-MEET, independently
reproduced in AUDIT-G); no embedded-observer realization or obstruction is attached to any cone at L; the
single-token premises are inherited from Q3. Every load-bearing number is backed by an exact script that replays
byte-identically and agrees with my own earlier independent computations.

Gem classification: CONFIRMING (the stage-3/4/5 certificates), NEW as an assumption-watch marker (item 3 above),
POSITIVE (pair-blindness of the single-token premises).

## 6. Files

`r6_listed_hashes.txt` (59/59 OK), `replay/REPLAY-LOG.txt` (6/6 IDENTICAL), `replay/r*_*.{out,err}` (the replay
outputs), this file.
