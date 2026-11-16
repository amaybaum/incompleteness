# Implementation record 2a r2: CHANGEMAP-A1C-r6-min and its Addendum 1 applied to the manuscript sources

**Scope.** Owner authorization of 2026-11-16 (#1169 c.6907178506), Stage 2a, limited to the 133 entries of CHANGEMAP-A1C-r6-min (as published at research commit c8a2a621; the local copy differs only in the OQ-2 header parenthesis) and necessary propagation, with CHANGEMAP-A1C-r6-min-ADDENDUM-1 as confirmed by its review (REVIEW-ADDENDUM-1, "confirmed with nits") for the seven entries r1 left unapplied. Worktree: branch `paper/a1-min-correction-20261116` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Only `.md` sources and `verification/coverage/LEDGER.json` were edited. No `.tex`/`.pdf`, Lean, tool, guard, AGENTS.md or record file was touched; nothing was committed or pushed; no build was run; no git command that changes refs was run.

**Method.** Each entry was encoded as exact (file, line, old text, new text) pairs taken from its "Minimal change" cell. Before any write, a dry run checked every old text against its line at the base, with the expected number of occurrences, and checked that each book chapter line was byte-identical to its FULL line. The same pair was then applied to the chapter line and its FULL mirror. Whole-line deletions (appendix-a:181, appendix-c:132) also removed the blank line the deletion left doubled (appendix-c only). Entries whose text gives no exact insertion point, or whose literal application would leave broken text, were left unapplied in r1. Addendum 1 gave those seven entries exact old/new pairs; the 21 primary pairs of the review's final apply list were applied in r2 by the same method (dry run of every old string on its line, FULL twin located by byte-identical content, the same pair applied to both), and the three sub-edits the review dropped were not applied, nor any fallback pair.

**Counts.** 133 entries: 132 applied (130 text entries, the registry entry N-D2d, and the check N-D2x), of which N-K01-16 and N-K03-40 are applied in part; 1 not applied (N-Kgl-19, dropped). Addendum 1: 21 pairs applied, 3 sub-edits dropped (ch01:183, ch03:186, glossary:19).

## Per-entry results

Line numbers after the edit. In `papers/` no whole line was deleted, so they equal the base numbers. In appendix-a, lines after 181 move up by 1. In appendix-c, lines after 132 move up by 2. In ch18, lines after 188 move up by 2. In FULL, lines after 4994 move up by 2, lines after 5705 by 3 and lines after 6362 by 5 in all (base numbering).

| Map entry | Result | Site(s) after the edit (file:line; FULL mirror) |
|---|---|---|
| N-M04 | applied | Main.md:20 |
| N-M05 | applied | Main.md:20 |
| N-M06 | applied | Main.md:36 |
| N-M07 | applied | Main.md:44 |
| N-M09 | applied | Main.md:58 |
| N-M10a | applied | Main.md:60 |
| N-M10b | applied | Main.md:60 |
| N-M10c | applied | Main.md:60 |
| N-M10d | applied | Main.md:60 |
| N-M11 | applied | Main.md:64 |
| N-M19 | applied | Main.md:216 |
| N-M22 | applied | Main.md:280 |
| N-M57 | applied | Main.md:216 |
| N-M26 | applied | Main.md:356 |
| N-M31 | applied | Main.md:449 |
| N-M33 | applied | Main.md:592 |
| N-M35 | applied | Main.md:630 |
| N-M36 | applied | Main.md:642 |
| N-M37 | applied | Main.md:654 |
| N-M38 | applied | Main.md:704 |
| N-M39 | applied | Main.md:710 |
| N-M40 | applied | Main.md:714 |
| N-M41 | applied | Main.md:720 |
| N-M42 | applied | Main.md:722 |
| N-M43 | applied | Main.md:724 |
| N-M44 | applied | Main.md:728 |
| N-M45 | applied | Main.md:728 |
| N-M46 | applied | Main.md:728 |
| N-M60 | applied | Main.md:728 |
| N-M44b | applied | Main.md:728 |
| N-M50 | applied | Main.md:746 |
| N-M51 | applied | Main.md:760 |
| N-M54 | applied | Main.md:774 |
| N-G01b | applied | GR.md:20 |
| N-G04 | applied | GR.md:58 |
| N-G10a | applied | GR.md:256 |
| N-G12 | applied | GR.md:342 |
| N-S20 | applied | SM.md:36; SM.md:1520; SM.md:1546; SM.md:1588 |
| N-S01 | applied | SM.md:14 |
| N-S18 | applied | SM.md:1588 |
| N-S19 | applied | SM.md:1592 |
| N-U06 | applied | Substratum.md:56 |
| N-U01 | applied | Substratum.md:14 |
| N-U02 | applied | Substratum.md:16 |
| N-U03 | applied | Substratum.md:22 |
| N-U04 | applied | Substratum.md:44 |
| N-U22 | applied | Substratum.md:216 |
| N-U26 | applied | Substratum.md:367 |
| N-U27 | applied | Substratum.md:401; Substratum.md:407 |
| N-U33 | applied | Substratum.md:14 |
| N-U34 | applied (Addendum 1, pairs a–d). Sub:171 states a Bell no-go, so its sub-edit was kept | papers/Substratum.md:48, :171, :467 |
| N-U35 | applied | Substratum.md:131 |
| N-U38 | applied | Substratum.md:415 |
| N-U29 | applied | Substratum.md:389 |
| N-U30 | applied | Substratum.md:429 |
| N-T1293 | applied | Structure.md:1293 |
| N-Y05 | applied | Methodology.md:162; Methodology.md:283 |
| N-Y08 | applied | Methodology.md:357 |
| N-Y11 | applied (Addendum 1, pairs a–e); the cone sentences of :389 and :391 were already scoped and are unchanged | papers/Methodology.md:339, :381, :385, :389, :391 |
| N-X03 | applied | Complexity.md:212 |
| N-X05 | applied | Complexity.md:374 |
| N-X06 | applied | Complexity.md:434 |
| N-P03 | applied | Computation.md:118 |
| N-P04 | applied | Computation.md:120 |
| N-P06 | applied | Computation.md:180 |
| N-K01-28 | applied | book/ch01-observation.md:28 (FULL:363) |
| N-K01-41 | applied | book/ch01-observation.md:41 (FULL:376) |
| N-K01-85 | applied | book/ch01-observation.md:85 (FULL:420) |
| N-K01-93 | applied | book/ch01-observation.md:93 (FULL:428) |
| N-K01-165 | applied | book/ch01-observation.md:165 (FULL:500) |
| N-K01-181 | applied | book/ch01-observation.md:181 (FULL:516) |
| N-K01-235 | applied | book/ch01-observation.md:235 (FULL:570) |
| N-K01-16 | applied in part (Addendum 1, pairs a–b at ch01:16). Sub-edit (c) at ch01:183 dropped by the review of Addendum 1: the sentence assumes parameter independence, so it is Bell's theorem itself and does not rest on A1 | book/ch01-observation.md:16 (FULL:351) |
| N-K02-16 | applied | book/ch02-substratum.md:16 (FULL:650) |
| N-K02-76 | applied | book/ch02-substratum.md:76 (FULL:710) |
| N-K02-136 | applied | book/ch02-substratum.md:136 (FULL:770); book/ch02-substratum.md:212 (FULL:846) |
| N-K02-184 | applied | book/ch02-substratum.md:184 (FULL:818) |
| N-K02-192 | applied | book/ch02-substratum.md:192 (FULL:826) |
| N-K03-22 | applied | book/ch03-structural-realism.md:22 (FULL:887) |
| N-K03-58 | applied | book/ch03-structural-realism.md:58 (FULL:923) |
| N-K03-196 | applied | book/ch03-structural-realism.md:196 (FULL:1061) |
| N-K03-40 | applied in part (Addendum 1, pairs a–c). Sub-edit (d) at ch03:186 dropped by the review of Addendum 1 (parameter independence assumed) | book/ch03-structural-realism.md:40 (FULL:905); book/ch03-structural-realism.md:162 (FULL:1027); book/ch03-structural-realism.md:180 (FULL:1045) |
| N-K04-26 | applied | book/ch04-methodology.md:26 (FULL:1134) |
| N-K04-36 | applied | book/ch04-methodology.md:36 (FULL:1144); book/ch04-methodology.md:182 (FULL:1290) |
| N-K04-178 | applied | book/ch04-methodology.md:178 (FULL:1286) |
| N-K04-116 | applied | book/ch04-methodology.md:116 (FULL:1224); book/ch04-methodology.md:166 (FULL:1274) |
| N-K05-23 | applied | book/ch05-gauge-structure.md:23 (FULL:1341) |
| N-K05-95 | applied | book/ch05-gauge-structure.md:95 (FULL:1413) |
| N-K05-194 | applied | book/ch05-gauge-structure.md:194 (FULL:1512) |
| N-K06-10 | applied | book/ch06-matter-content.md:10 (FULL:1523) |
| N-K07-12 | applied | book/ch07-gravity.md:12 (FULL:1878); book/ch07-gravity.md:110 (FULL:1976); book/ch07-gravity.md:157 (FULL:2023); book/ch07-gravity.md:159 (FULL:2025); book/ch07-gravity.md:161 (FULL:2027) |
| N-K07-118 | applied | book/ch07-gravity.md:118 (FULL:1984) |
| N-K07-52 | applied | book/ch07-gravity.md:52 (FULL:1918) |
| N-K07-16 | applied | book/ch07-gravity.md:16 (FULL:1882) |
| N-K09-36 | applied | book/ch09-universality.md:36 (FULL:2503) |
| N-K09-18 | applied | book/ch09-universality.md:18 (FULL:2485) |
| N-K09-106 | applied | book/ch09-universality.md:106 (FULL:2573) |
| N-K09-129 | applied | book/ch09-universality.md:129 (FULL:2596) |
| N-K09-184 | applied | book/ch09-universality.md:184 (FULL:2651) |
| N-K14-90 | applied | book/ch14-quantum-computing.md:90 (FULL:3756); book/ch14-quantum-computing.md:268 (FULL:3934) |
| N-K14-164 | applied | book/ch14-quantum-computing.md:164 (FULL:3830) |
| N-K14-160 | applied | book/ch14-quantum-computing.md:160 (FULL:3826) |
| N-K12-213 | applied | book/ch12-evolution-intelligence.md:213 (FULL:3453) |
| N-K18-20 | applied | book/ch18-beyond.md:20 (FULL:4826); book/ch18-beyond.md:28 (FULL:4834); book/ch18-beyond.md:162 (FULL:4968) |
| N-K18-40 | applied | book/ch18-beyond.md:40 (FULL:4846) |
| N-K18-166 | applied | book/ch18-beyond.md:166 (FULL:4972) |
| N-K18-172 | applied | book/ch18-beyond.md:172 (FULL:4978) |
| N-K18-174 | applied | book/ch18-beyond.md:174 (FULL:4980) |
| N-K18-186 | applied (Addendum 1, pairs a–e): :186 return stated for a finite model, physical-units and astronomical-period sentences deleted; :188 Falsifiability paragraph and the blank line after it deleted; :190 opens "A finite model is periodic with period $N$, …", cyclicity-commitment sentence deleted | book/ch18-beyond.md:186 (FULL:4992); book/ch18-beyond.md:188 (FULL:4994) |
| N-K18-192 | applied | book/ch18-beyond.md:190 (FULL:4996); book/ch18-beyond.md:192 (FULL:4998) |
| N-K18-198 | applied | book/ch18-beyond.md:196 (FULL:5002) |
| N-K18-244 | applied | book/ch18-beyond.md:242 (FULL:5048); book/ch18-beyond.md:244 (FULL:5050); book/ch18-beyond.md:260 (FULL:5066) |
| N-K18-290 | applied | book/ch18-beyond.md:288 (FULL:5094) |
| N-K18-328 | applied | book/ch18-beyond.md:326 (FULL:5132) |
| N-K18-122 | applied | book/ch18-beyond.md:122 (FULL:4928); book/ch18-beyond.md:138 (FULL:4944) |
| N-K19-22 | applied | book/ch19-open-problems.md:22 (FULL:5167); book/ch19-open-problems.md:30 (FULL:5175); book/ch19-open-problems.md:72 (FULL:5217) |
| N-K19-126 | applied | book/ch19-open-problems.md:126 (FULL:5271) |
| N-K19-212 | applied | book/ch19-open-problems.md:212 (FULL:5357) |
| N-K19-216 | applied | book/ch19-open-problems.md:216 (FULL:5361) |
| N-K19-214 | applied | book/ch19-open-problems.md:214 (FULL:5359) |
| N-K19-80 | applied | book/ch19-open-problems.md:80 (FULL:5225) |
| N-K19-360 | applied | book/ch19-open-problems.md:360 (FULL:5505) |
| N-Kappa-48 | applied | book/appendix-a-prediction-status.md:48 (FULL:5570) |
| N-Kappa-181 | applied | book/appendix-a-prediction-status.md:181 deleted (FULL:5703 deleted) |
| N-Kappb-22 | applied | book/appendix-b-derivations.md:22 (FULL:5773) |
| N-Kappc-C6 | applied | book/appendix-c-objections.md:114 (FULL:6341); book/appendix-c-objections.md:122 (FULL:6349); book/appendix-c-objections.md:124 (FULL:6351); book/appendix-c-objections.md:128 (FULL:6355); book/appendix-c-objections.md:130 (FULL:6357); book/appendix-c-objections.md:132 deleted (FULL:6360 deleted); book/appendix-c-objections.md:132 (FULL:6359) |
| N-Kappc-154 | applied | book/appendix-c-objections.md:152 (FULL:6379) |
| N-Kappc-32 | applied (Addendum 1, pairs a–b) | book/appendix-c-objections.md:32 (FULL:6259); book/appendix-c-objections.md:34 (FULL:6261) |
| N-Kgl-11 | applied | book/glossary.md:11 (FULL:6590) |
| N-Kgl-19 | **not applied: dropped** by the review of Addendum 1. glossary:19 assumes measurement independence plus ontic parameter independence, which is Bell's theorem with no cone and no finite site set; no fallback applied | — |
| N-Kbk-90 | applied | book/README.md:90 |
| N-D2d | applied: `MAIN:C-observer-selection-rule-rate-condition` fingerprint df04fba6b2d81e20 → 38127d106435567a (the only STALE entry `tools/coverage_check.py` reported); no other field changed | verification/coverage/LEDGER.json (the entry's "fingerprint" field) |
| N-D2x | applied as a check: `tools/coverage_check.py` reported no other stale entry; nothing else in LEDGER.json changed | — |

## Files changed

26 manuscript files and 1 registry file (`git diff --shortstat`, all 27 files: 243 insertions, 253 deletions); r2 added no file:
- papers: `Main.md`, `GR.md`, `SM.md`, `Substratum.md`, `Structure.md`, `Methodology.md`, `Complexity.md`, `Computation.md`;
- book: `ch01-observation.md`, `ch02-substratum.md`, `ch03-structural-realism.md`, `ch04-methodology.md`, `ch05-gauge-structure.md`, `ch06-matter-content.md`, `ch07-gravity.md`, `ch09-universality.md`, `ch12-evolution-intelligence.md`, `ch14-quantum-computing.md`, `ch18-beyond.md`, `ch19-open-problems.md`, `appendix-a-prediction-status.md`, `appendix-b-derivations.md`, `appendix-c-objections.md`, `glossary.md`, `README.md`, `The-Incompleteness-of-Observation-FULL.md`;
- registry: `verification/coverage/LEDGER.json` (one fingerprint).

Not touched, as the map says: Introduction, Medicine, Bioinformatics and Juno.

## Mirror byte-identity

- **Before each edit:** every edited chapter line was byte-identical to its FULL line at the stated offset. The dry run checks this; there were no mismatches.
- **After the edits:**
  - every chapter line longer than 60 characters occurs verbatim in FULL (0 chapters with missing lines);
  - all 80 FULL lines that differ from the base equal a chapter line (0 non-matching).
- The two whole-line deletions were applied to both copies: appendix-a:181 with FULL:5705, and appendix-c:132 (plus the doubled blank) with FULL:6362–6363 (base numbering). In r2, ch18:188 and the blank line 189 were deleted with FULL:4994–4995.

## Checks run (read-only)

| Check | Result |
|---|---|
| `tools/coverage_check.py`, before the registry edit | FAIL (1): `MAIN:C-observer-selection-rule-rate-condition` STALE (df04fba6b2d81e20 → 38127d106435567a). Expected: this is the statement N-M51 edits, which is N-D2d. No other stale entry. |
| `tools/coverage_check.py`, after re-affirming that fingerprint | OK (133 canonical statements, 20 unattached checkers) |
| r2: `tools/coverage_check.py` after the Addendum 1 pairs | OK (133 canonical statements, 20 unattached checkers); no new stale entry, so LEDGER.json was not touched again |
| r2: `tools/lean_manuscript_census.py` | OK (25 current families; complete relative to the maintained registry) |
| r2: `verification/lean/edge_rigidity_probe.py` (guard V1) | ALL CHECKS PASS (exit 0) |
| r2: `tools/claims_check.py` | OK |
| r2: `tools/voice_check.py` | OK (40 manuscript files scanned) |
| r2: `tools/artifact_placement_check.py` | OK |
| r2: `tools/legacy_records_check.py --self-test` | OK |
| r2: mirror check | every chapter line longer than 60 characters occurs verbatim in FULL (0 chapters with missing lines); all 88 FULL lines that differ from the base equal a chapter line (0 non-matching); all 88 chapter/FULL line pairs cited in the per-entry table are byte-identical |
| `tools/lean_manuscript_census.py` | OK (every cited identifier and anchor present; 25 current families) |
| `verification/lean/edge_rigidity_probe.py` (guard V1) | ALL CHECKS PASS (exit 0). Every "FAIL" in the output is part of a PASS line's description. |
| `tools/claims_check.py` | OK |
| `tools/voice_check.py` | OK (40 manuscript files scanned) |
| `tools/artifact_placement_check.py` | OK |
| `tools/legacy_records_check.py --self-test` | OK. The commit-mode check needs a commit and was not run. |
| `tools/staleness_check.py` | FAILED, as expected before the rebuild. `.tex`/`.pdf` are STALE for Main, GR, SM, Substratum, Structure, Methodology, Complexity, Computation and the book. Bioinformatics, Introduction, Juno and Medicine are ok. |

## Unexpected items

**r1.** The seven entries N-U34, N-Y11, N-K01-16, N-K03-40, N-Kappc-32, N-Kgl-19 and N-K18-186 gave no exact insertion point, or would have left a fragment (ch18:190), or carried a reference wrong for the book (glossary "(§3.3)"). They were left unapplied and resolved by Addendum 1.

**r2: for the owner (the authorization's clause on unexpected issues).** The review of Addendum 1 dropped three sub-edits of reviewed r6-min entries: N-K01-16 at ch01:183, N-K03-40 at ch03:186, and N-Kgl-19 at glossary:19 (the whole entry). Each sentence assumes ontic parameter independence and measurement independence rather than deriving parameter independence from the graph cone, so it states Bell's theorem itself, which holds on any hidden-variable probability space and needs no finite site set; Main states the same form unscoped (Main:80, item (4); Main:404). The drops shrink the reviewed entries; no fallback pair was applied.

No other unexpected item in r2:
- each of the 21 old strings matched exactly once on its stated line in `wt-2a`, and each book line had exactly one byte-identical FULL twin;
- after the pairs, no book line contains "Falsifiability.** The recurrence", "cyclic at the substratum", "substratum cyclicity" or "Translating to physical units";
- ch18:186–188 read without a fragment, and the period bounds stay as statements about finite models;
- `tools/staleness_check.py` still reports the expected STALE `.tex`/`.pdf` before the rebuild.
