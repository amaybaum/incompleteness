# Implementation record 2a r1: CHANGEMAP-A1C-r6-min applied to the manuscript sources

**Scope.** Owner authorization of 2026-11-16 (#1169 c.6907178506), Stage 2a, limited to the 133 entries of CHANGEMAP-A1C-r6-min (as published at research commit c8a2a621; the local copy differs only in the OQ-2 header parenthesis) and necessary propagation. Worktree: branch `paper/a1-min-correction-20261116` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Only `.md` sources and `verification/coverage/LEDGER.json` were edited. No `.tex`/`.pdf`, Lean, tool, guard, AGENTS.md or record file was touched; nothing was committed or pushed; no build was run; no git command that changes refs was run.

**Method.** Each entry was encoded as exact (file, line, old text, new text) pairs taken from its "Minimal change" cell. Before any write, a dry run checked every old text against its line at the base, with the expected number of occurrences, and checked that each book chapter line was byte-identical to its FULL line. The same pair was then applied to the chapter line and its FULL mirror. Whole-line deletions (appendix-a:181, appendix-c:132) also removed the blank line the deletion left doubled (appendix-c only). Entries whose text gives no exact insertion point, or whose literal application would leave broken text, were left unapplied and are reported below.

**Counts.** 133 entries: 126 applied (124 text entries, the registry entry N-D2d, and the check N-D2x), 7 not applied.

## Per-entry results

Line numbers after the edit. In `papers/` no whole line was deleted, so they equal the base numbers. In appendix-a, lines after 181 move up by 1. In appendix-c, lines after 132 move up by 2. In FULL, lines after 5705 move up by 1 and lines after 6362 by 3 in all.

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
| N-U34 | **not applied** — the Bell-scope inserts at Sub:48, :171, :467 give no insertion point ("at each Bell conclusion"), and Sub:171 has no Bell conclusion on the line; the :467 cone sub-edit is exact but the entry is left whole | — |
| N-U35 | applied | Substratum.md:131 |
| N-U38 | applied | Substratum.md:415 |
| N-U29 | applied | Substratum.md:389 |
| N-U30 | applied | Substratum.md:429 |
| N-T1293 | applied | Structure.md:1293 |
| N-Y05 | applied | Methodology.md:162; Methodology.md:283 |
| N-Y08 | applied | Methodology.md:357 |
| N-Y11 | **not applied** — ":339 add … after graph cone" is exact, but the Bell-scope inserts at Meth:381, :385, :389, :391 give no insertion point | — |
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
| N-K01-16 | **not applied** — ":16 gives exact causal cones → …for finite-range couplings" is exact, but the Bell-scope inserts at ch01:16 and :183 give no insertion point | — |
| N-K02-16 | applied | book/ch02-substratum.md:16 (FULL:650) |
| N-K02-76 | applied | book/ch02-substratum.md:76 (FULL:710) |
| N-K02-136 | applied | book/ch02-substratum.md:136 (FULL:770); book/ch02-substratum.md:212 (FULL:846) |
| N-K02-184 | applied | book/ch02-substratum.md:184 (FULL:818) |
| N-K02-192 | applied | book/ch02-substratum.md:192 (FULL:826) |
| N-K03-22 | applied | book/ch03-structural-realism.md:22 (FULL:887) |
| N-K03-58 | applied | book/ch03-structural-realism.md:58 (FULL:923) |
| N-K03-196 | applied | book/ch03-structural-realism.md:196 (FULL:1061) |
| N-K03-40 | **not applied** — no insertion point given for ":40 add 'with finite setting and readout regions'" or for the Bell-scope inserts at :162, :180, :186 | — |
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
| N-K18-186 | **not applied** — the :190 sub-edit deletes "The framework predicts that the universe is *cyclic at the substratum level* —", which leaves the fragment "periodic with period $N$, …" starting a sentence; the replacement wording for the kept clause is not given. The :186 and :188 sub-edits are exact; the entry is left whole | — |
| N-K18-192 | applied | book/ch18-beyond.md:192 (FULL:4998); book/ch18-beyond.md:194 (FULL:5000) |
| N-K18-198 | applied | book/ch18-beyond.md:198 (FULL:5004) |
| N-K18-244 | applied | book/ch18-beyond.md:244 (FULL:5050); book/ch18-beyond.md:246 (FULL:5052); book/ch18-beyond.md:262 (FULL:5068) |
| N-K18-290 | applied | book/ch18-beyond.md:290 (FULL:5096) |
| N-K18-328 | applied | book/ch18-beyond.md:328 (FULL:5134) |
| N-K18-122 | applied | book/ch18-beyond.md:122 (FULL:4928); book/ch18-beyond.md:138 (FULL:4944) |
| N-K19-22 | applied | book/ch19-open-problems.md:22 (FULL:5169); book/ch19-open-problems.md:30 (FULL:5177); book/ch19-open-problems.md:72 (FULL:5219) |
| N-K19-126 | applied | book/ch19-open-problems.md:126 (FULL:5273) |
| N-K19-212 | applied | book/ch19-open-problems.md:212 (FULL:5359) |
| N-K19-216 | applied | book/ch19-open-problems.md:216 (FULL:5363) |
| N-K19-214 | applied | book/ch19-open-problems.md:214 (FULL:5361) |
| N-K19-80 | applied | book/ch19-open-problems.md:80 (FULL:5227) |
| N-K19-360 | applied | book/ch19-open-problems.md:360 (FULL:5507) |
| N-Kappa-48 | applied | book/appendix-a-prediction-status.md:48 (FULL:5572) |
| N-Kappa-181 | applied | book/appendix-a-prediction-status.md:181 deleted (FULL:5705 deleted) |
| N-Kappb-22 | applied | book/appendix-b-derivations.md:22 (FULL:5775) |
| N-Kappc-C6 | applied | book/appendix-c-objections.md:114 (FULL:6343); book/appendix-c-objections.md:122 (FULL:6351); book/appendix-c-objections.md:124 (FULL:6353); book/appendix-c-objections.md:128 (FULL:6357); book/appendix-c-objections.md:130 (FULL:6359); book/appendix-c-objections.md:132 deleted (FULL:6362 deleted); book/appendix-c-objections.md:132 (FULL:6361) |
| N-Kappc-154 | applied | book/appendix-c-objections.md:152 (FULL:6381) |
| N-Kappc-32 | **not applied** — no insertion point given for the Bell scope at appendix-c:32 and :34 | — |
| N-Kgl-11 | applied | book/glossary.md:11 (FULL:6592) |
| N-Kgl-19 | **not applied** — the insertion point is given ("before 'gives Bell factorization'"), but the phrase to insert, taken verbatim from N-M37, ends "(§3.3)", which in the glossary would cite the book's §3.3 rather than Main §3.3; the reference has to be adapted, which the entry does not give | — |
| N-Kbk-90 | applied | book/README.md:90 |
| N-D2d | applied: `MAIN:C-observer-selection-rule-rate-condition` fingerprint df04fba6b2d81e20 → 38127d106435567a (the only STALE entry `tools/coverage_check.py` reported); no other field changed | verification/coverage/LEDGER.json (the entry's "fingerprint" field) |
| N-D2x | applied as a check: `tools/coverage_check.py` reported no other stale entry; nothing else in LEDGER.json changed | — |

## Files changed

26 manuscript files and 1 registry file (`git diff --stat`: 218 insertions, 224 deletions in the manuscripts):
- papers: `Main.md`, `GR.md`, `SM.md`, `Substratum.md`, `Structure.md`, `Methodology.md`, `Complexity.md`, `Computation.md`;
- book: `ch01-observation.md`, `ch02-substratum.md`, `ch03-structural-realism.md`, `ch04-methodology.md`, `ch05-gauge-structure.md`, `ch06-matter-content.md`, `ch07-gravity.md`, `ch09-universality.md`, `ch12-evolution-intelligence.md`, `ch14-quantum-computing.md`, `ch18-beyond.md`, `ch19-open-problems.md`, `appendix-a-prediction-status.md`, `appendix-b-derivations.md`, `appendix-c-objections.md`, `glossary.md`, `README.md`, `The-Incompleteness-of-Observation-FULL.md`;
- registry: `verification/coverage/LEDGER.json` (one fingerprint).

Not touched, as the map says: Introduction, Medicine, Bioinformatics and Juno.

## Mirror byte-identity

- **Before each edit:** every edited chapter line was byte-identical to its FULL line at the stated offset. The dry run checks this; there were no mismatches.
- **After the edits:**
  - every chapter line longer than 60 characters occurs verbatim in FULL (0 chapters with missing lines);
  - all 80 FULL lines that differ from the base equal a chapter line (0 non-matching).
- The two whole-line deletions were applied to both copies: appendix-a:181 with FULL:5705, and appendix-c:132 (plus the doubled blank) with FULL:6362–6363.

## Checks run (read-only)

| Check | Result |
|---|---|
| `tools/coverage_check.py`, before the registry edit | FAIL (1): `MAIN:C-observer-selection-rule-rate-condition` STALE (df04fba6b2d81e20 → 38127d106435567a). Expected: this is the statement N-M51 edits, which is N-D2d. No other stale entry. |
| `tools/coverage_check.py`, after re-affirming that fingerprint | OK (133 canonical statements, 20 unattached checkers) |
| `tools/lean_manuscript_census.py` | OK (every cited identifier and anchor present; 25 current families) |
| `verification/lean/edge_rigidity_probe.py` (guard V1) | ALL CHECKS PASS (exit 0). Every "FAIL" in the output is part of a PASS line's description. |
| `tools/claims_check.py` | OK |
| `tools/voice_check.py` | OK (40 manuscript files scanned) |
| `tools/artifact_placement_check.py` | OK |
| `tools/legacy_records_check.py --self-test` | OK. The commit-mode check needs a commit and was not run. |
| `tools/staleness_check.py` | FAILED, as expected before the rebuild. `.tex`/`.pdf` are STALE for Main, GR, SM, Substratum, Structure, Methodology, Complexity, Computation and the book. Bioinformatics, Introduction, Juno and Medicine are ok. |

## Unexpected items (entries left unapplied)

Each needs a precise instruction before it can be applied.

1. **N-U34 (Sub:48, :171, :467).** "Insert the Bell scope of N-M37 at each Bell conclusion" names no insertion point. Sub:171 has no Bell conclusion on the line (no CHSH or factorization statement). The :467 cone sub-edit ("gives an exact causal cone" → "…for finite-range couplings") is exact but was not applied alone, because the entry was left whole.
2. **N-Y11 (Meth:339, :381, :385, :389, :391).**
   - :339 ("with finite setting and readout regions" after "graph cone") is exact.
   - The Bell-scope inserts at :381, :385, :389 and :391 name no insertion point.
3. **N-K01-16 (ch01:16, :183).**
   - The :16 cone sub-edit is exact.
   - The Bell-scope inserts at :16 and :183 name no insertion point.
4. **N-K03-40 (ch03:40, :162, :180, :186).** No insertion point is given for ":40 add 'with finite setting and readout regions'", nor for the Bell scope at :162, :180 and :186.
5. **N-Kappc-32 (appendix-c:32, :34).** No insertion point is given.
6. **N-Kgl-19 (glossary:19).**
   - The insertion point is given ("before 'gives Bell factorization'").
   - The phrase taken verbatim from N-M37 ends "(§3.3)". In the glossary that would cite the book's §3.3 instead of Main §3.3, and the entry gives no adapted reference.
7. **N-K18-186 (ch18:186, :188, :190).**
   - The :190 sub-edit deletes "The framework predicts that the universe is *cyclic at the substratum level* —". The kept text would then start a sentence with the fragment "periodic with period $N$, the least common multiple of the bijection's cycle lengths."
   - No replacement wording is given.
   - The :186 and :188 sub-edits are exact; the entry was left whole.
   - Because of this, ch18:186, :188 and :190 still state the cosmic-recurrence prediction (Q10 (c)) at the base wording.

No other unexpected item:
- every applied old text matched exactly once at its stated line (twice where the entry repeats it: ch18:246);
- no needed change outside the map was found;
- no LEDGER.json field other than the one fingerprint needed a change.
