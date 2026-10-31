# Re-check: MIGRATION-r2, RETIREMENT-r2, CHANGES-r2

Objects: `S/paper/retire/{MIGRATION-r2,RETIREMENT-r2,CHANGES-r2}.md`, checked against my review
`S/paper/retire-review/REVIEW.md` (RC1–RC7). The r1 files are unchanged.
Base: `main` `687e885b`. Read-only. Every git command ran with
`-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: ACCEPT WITH NITS

RC1–RC7 are all applied correctly. Nothing blocks. The four nits below are wording or accuracy
points. Fix them in the next revision; none of them changes the plan.

## RC by RC

| RC | Applied? | Evidence |
|---|---|---|
| RC1 `LEDGER.json:3100` | **Yes. Leaving it unchanged is the right default** | The route string is 339,146 chars long. It opens with the CURRENT RECONSTRUCTION ROUTE, and at char 589 it reads: "The following independent-track development notes are historical and do not restore reconstruction closure." All 15 "Explainer" mentions come after that label: first at char 95,277, last at char 327,156. The notes are labelled historical, `coverage_check` does not read the route, and §A.42 item 4 is forward-only. Leaving the line unchanged is compliant. The survivor list (§2.4) and §4.1(5) are corrected. See N2 on the owner option |
| RC2 redirect stub (S2) | **Yes** | §2.1 adds the stub with the exact review text and the inertness constraints. M1/M2 are stated correctly: `staleness_check.py:58–65` reports an unstamped stub without failing; under M1, `build.sh:84` builds it. §3.1 adds B′. §3.2 records the dry run and the "≥9 places" argument. §3.3(b) has the text. §4.1(8) makes inertness a checkpoint: byte-equal plus an sha256 record, and empty greps for `kernel:`, statement headings, `*.py`, and the voice PATTERNS. The survivor list adds the stub, its `.tex` under M1, and `git grep -I`. README:115 is OQ2, LICENSE is optional, and R1 is mitigated |
| RC3 reproducibility (S1) | **Yes** | §2.5 has the rule, the table, three required commit-message sentences and the checkpoint mapping (`v3-receipts`, `legacy-records`, re-grep). **CC-1's working-tree default** (`controls.py:388`, `--repo` default `.`) is handled correctly. (i) No CI step, workflow or tool runs CC-1 or CC-2 controls: `git grep` for `round-cc`, `corpus-correction`, `CC-1` and controls globs over `.github/`, `tools/` and `verification/lean/*.py` finds nothing; `verify.yml` invokes only other rounds' controls, by explicit path. (ii) Running at HEAD already fails, independent of the move: CC-2's governed sources at its `e` `36b12c4c` differ from 687e885b for `papers/Main.md` (dc0b2285 vs d1cbc109), `Explainer.md`, `GR.md` and `Substratum.md`. (iii) The required message text confines reproduction to materialized historical trees. See N3 for CC-1's halted status |
| RC4 legacy-file invariant | **Yes, and the author's count is the right one** | Lines 3, 682, 686, 763, 781, 818 and 822 make **7 changed lines**, carrying 1 notice + 8 link targets (763 and 781 hold two each). My "9" counted targets, not lines. The check compares each `-`/`+` pair by script, keeps the length at 1059, and adds `--follow` and `-B -M` review. I re-verified `-B -M` showing `papers/{ => legacy}/Explainer.md \| 2 +-` and `--follow` with a stub in the same commit, in a scratch repo. `git diff --no-index <(git show …) file` works on git 2.43 (tested); see N4 |
| RC5 ordering | **Yes** | P6(c) moves the probe pre-check into acceptance review and lists the loops: :2877–2882, :3113, :3273, :3737, :4691/:4833. P7(a)–(d) cover the re-grep including alias lines, open rounds' governed paths, evidence-retention mapped citing files, and the filename. Informational: in the current draft `S/paper/draft/Introduction.md` none of the sampled forbidden terms occur. Sampled: `reversible implementation locality`, `Route B`/`RouteB`, `DerivedOI`, `routeB_target`, `ExecSource`, `obs_not_layerFlowExecutable`, `waveSubstratum`, `LiftSource`, `coherentLiftClass`, the superseded package names, the R7-OINN phrases. The accepted text still decides |
| RC6 holography | **Yes** | Row 23a: unique, (c) by default, with :699's list as (d) against GR:360, glossary:75 and SM:1259. The owner option is an Appendix C section from primary sources. It is carried into §1, §5 and OQ3 |
| RC7 supersession | **Yes** | §3 is conditional on the accepted text's kernel map (Appendix A or Alt-L §3), checked at P6(b), with a fallback to Main:710–722 and B.7. **Verified locally:** the draft `S/paper/draft/Introduction.md:414–438` has `## Appendix A. Kernel map` with **16 data rows**, matching the coordinator's report. I checked the scratchpad file, not commit `8fcc6443` |

Nits of the review also applied:
- GR:360 and :358 in row 2;
- Main:119 in row 7;
- OUTLINE-r4 named as governing; :72–73 is correct, my :61–62 was wrong;
- the six census note lines;
- the P7(d) path.

New risks R13–R16 are present. R16 is right: only `_a12p_m3` reads the Explainer. The
countercontrol phrase `qm requires oi` (a reading the guard forbids: only core containment is proved) in §4.1(4)(ii) is in the R7-OINN loop at probe :3115, so the
countercontrol is live.

## Nits

- **N1. MIGRATION-r2 row 19 over-reaches.**
  - The (d) now includes :549's "the framework explains why". The full sentence is "The framework
    explains why: there is nothing to cancel". It refers to the 122-digit cancellation, which
    `GR.md:360` itself says the framework "eliminates … entirely".
  - So that clause is not (d). The row's (d) should rest on :551, "predicts the observed value",
    alone.
- **N2. RC1's owner option edits labelled history.** RETIREMENT-r2 §2.4 and PD6 offer to drop
  "Explainer" from the route's "pending-action sentences".
  - Those sentences ("NEXT: … the Main/Explainer update", "are to be updated … once round
    twenty-four lands") sit inside the block the route labels historical.
  - Editing them would rewrite history (§A.27; §A.42 item 4). Drop the option, or state that
    leaving the line unchanged is the only compliant choice.
- **N3. CC-1 is a halted round.** Its receipt has `status: halted`, `withdrawal 5ae15444…` and no
  `e`.
  - §2.5's "materialized D/E trees" and "`--check E` at the candidate" should name, for CC-1, its D
    and the withdrawn candidate.
  - For CC-2 (complete, `e` `36b12c4c`), D/E is correct as written.
- **N4. Portability of the §4.1(7) diff.** `git diff --no-index` reads process-substitution pipes
  only on git ≥ 2.42. On the canonical (e.g. macOS) toolchain, write `git show
  <base>:papers/Explainer.md` to a temporary file first.
