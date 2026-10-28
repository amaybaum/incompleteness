# Changes in revision 2 (MIGRATION-r2.md, RETIREMENT-r2.md)

**Source.** Independent review `S/paper/retire-review/REVIEW.md` (ACCEPT WITH CHANGES), plus the
owner decisions of 2026-10-26.

**What is unchanged.** `MIGRATION.md` and `RETIREMENT.md` (revision 1, the reviewed objects) are
kept as they were. No repository file was changed. Every git command ran with
`-c gc.auto=0 -c maintenance.auto=false`.

## Owner decisions recorded as decided

They are recorded in both r2 files.

| ID | Decision | Where it lands in r2 |
|---|---|---|
| OD1 | Strategy approved, conditional on independent review and acceptance of the Introduction | RETIREMENT-r2 header; P1 |
| OD2 | Move to `papers/legacy/` approved, after acceptance | §2.1; §3.1 option B′ |
| OD3 | Superseded notice required | §3.3(a) (legacy file), §3.3(b) (stub) |
| OD4 | `Main.md:66` → `[Substratum §6.2]` | §2.2 (unchanged from r1) |
| OD5 | One PR, two commits | §2.0 |
| OD6 | S1, historical reproducibility | new §2.5 |
| OD7 | S2, redirect at `papers/Explainer.md` | §2.1, §3.2, §3.3(b), §4.1(8) |

## Required changes

| RC | Change | Where |
|---|---|---|
| RC1 | `verification/coverage/LEDGER.json:3100` (backlog rank-1 route; its "Main/Explainer" pending-action notes) is now accounted for. Default: left unchanged, because the route text labels its notes historical and `coverage_check` does not read route text; forward correction is an owner option (PD6). The survivor list and the §4.1(5) re-grep expectation are corrected | RETIREMENT-r2 §2.4 (new row; survivor list); §5 PD6 |
| RC2 | Redirect stub at `papers/Explainer.md`, using the review's exact text. No tool exclusion: the review's dry run shows every scanner passes the stub unmodified, and an exclusion would need at least nine edits. Stub artifacts: M1 (build and commit `.tex/.pdf`) is recommended, M2 (`build.sh` skip) is the alternative. Further edits: §2.1 adds the stub and M1/M2 and replaces r1's D2 "remove"; §2.4 survivors updated; §3.1 gains option B′; §3.2 adds the stub analysis; R1 is marked mitigated; README:115 becomes owner decision OQ2; LICENSE's minimal edit becomes optional | RETIREMENT-r2 §2.1, §2.2, §2.4, §3.1–§3.3, §4.1(1), §4.1(8), §5 |
| RC3 | New §2.5, historical reproducibility. It has a table of every place old paths occur in immutable or historical evidence (review §6, spot-checked: `v3_verifier.py:979`; CC-1 `controls.py:388` `--repo .`; A45 `controls.py:207–212` `git show`; no Explainer path in any receipt or seal). It also sets the rule that no record is rewritten, adds the required C2 commit-message text (frozen controls run only on materialized historical trees, never on HEAD) and names the checkpoints | RETIREMENT-r2 §2.5 |
| RC4 | New check §4.1(7): an exact line diff of the legacy file against the base blob (7 changed lines: line 3 and lines 682, 686, 763, 781, 818, 822, carrying the 8 link targets; each pair script-checked), the length held at 1059, `git log --follow`, and review under `git diff -B -M`. The review's "9" counts link targets; r2 states both counts. New risk R13 | RETIREMENT-r2 §4.1(7), §4.2, §5 R13 |
| RC5 | (a) The D7 probe pre-check moves into acceptance review as P6(c), with the loops to check against the accepted text; r1's D7 becomes plan default PD4. (b) New P7: re-derivation at the cut base. It covers the dependency re-grep including probe alias lines, open rounds' governed paths, evidence-retention mapped citing files if that archive has landed, and confirmation of the Introduction filename | RETIREMENT-r2 §1 P6, P7; §2.3 heading |
| RC6 | MIGRATION row 23a: the holography/Ryu–Takayanagi FAQ answer (Explainer:694–699) is classed (c) by default, with an owner option of a new book Appendix C section from primary sources. :699's consequence list is (d) and excluded (`GR.md:360`; `glossary.md:75`; `SM.md:1259`) | MIGRATION-r2 §1 items 3–4, §2 row 23/23a, §5; RETIREMENT-r2 OQ3 |
| RC7 | MIGRATION §3: the supersession of the summary tables is conditional on the accepted Introduction carrying the kernel map (Appendix A, or the Alt-L §3 table; `OUTLINE-r4.md:325–336`, `:342`), checked at P6(b). The coordinator reports that the draft at #918 `8fcc6443` has a 16-row Appendix A. That object is not in the local store and was **not verified** here. A fallback is stated: Main:710–722 and B.7 | MIGRATION-r2 §3, §4, §5; RETIREMENT-r2 P6(b) |

## Nits

- **Row 2:** `GR.md:362` → `:360`. The (d) now rests on the superlative "strongest piece of existing
  evidence" and §A.23, with GR:358 cited for the CC dissolution as cumulative evidence.
- **Row 19:** `GR.md:362` → `:360`. The (d) is narrowed to "predicts the observed value";
  "sits exactly at the classical geometric scale" is no longer (d), since it is close to GR:358.
- **Row 7:** `Main.md:118` → `:119`.
- **Governing outline.** MIGRATION-r2 names OUTLINE-r4 as the governing revision. Claim IDs are
  stable per `OUTLINE-r4.md:72–73`; the review cited :61–62, but the sentence is at :72–73.
- **Census notes.** RETIREMENT-r2 §2.2 lists all six current-state note lines (298, 411, 453, 551,
  573, 798). Line 1014 is kept, as before.
- **Introduction filename.** RETIREMENT-r2 P7(d) cites the full path for "audit README.md:112": it is
  cited via `SOURCES-r3.md:317–318` as
  `verification/audits/manuscript/introductory-paper-20261025/README.md` on the audit branch. The
  local copy at `S/pintro/repo` does not state the filename at :112, so P7 confirms it.

## Remaining owner decisions, as listed by the review (§10)

RETIREMENT-r2 §5, OQ1–OQ6:
- OQ1: M1 or M2;
- OQ2: what README:115 points to;
- OQ3: the holography objection in Appendix C;
- OQ4: the optional book items (lineage, navigation table after #931, the double-difference display
  from Main);
- OQ5: LICENSE wording and the pre-existing licence and Computation gaps;
- OQ6: the README Core-papers row and §1.

r1's D3, D4, D6, D7 and D8 are now plan defaults PD1–PD5 (adopted unless the owner objects). PD6 is
new.

## Other edits

- Expected re-grep survivors: the stub's `.tex` matches. The stub `.pdf` may appear as a binary match,
  so the re-grep uses `git grep -I`.
- New risks R14 (Zenodo latest-version content; the existing `cc-by-4.0` vs LICENSE gap), R15 (plan
  vs base drift → P7) and R16 (probe mutations: only `_a12p_m3`).
