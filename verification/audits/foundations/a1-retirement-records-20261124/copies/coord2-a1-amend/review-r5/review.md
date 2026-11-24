# Focused delta review, r5 against r4, and the final O-13 text (r5b)

Reviewer: independent, non-author, 2026-11-24. This review is paper-only and covers only the corrections the owner
ordered on 2026-11-24 (items 1–6). It reopens nothing else.

- Nothing was written in the repository.
- GitHub was read by REST GET only: three runs, one jobs list per run, and two comments.
- P's checkers ran only on copies under `review-r5/`.

**Inputs.** `MANIFEST.sha256` passes. The objects reviewed:

| File | sha256 |
|---|---|
| CHANGES-r4-to-r5 | `a7f45091…4c37` |
| O13-INVENTORY-r5 | `440934e5…be8a` |
| O13-DECISION-FINAL-r5 | `8da312b5…d268` |
| O13-DECISION-FINAL-r5b | `b6ccefbc…34bb` |
| O13-DECISION-FINAL-r4 (base) | `2633770b…5914` |
| review-r4 (base) | `be8879aa…83f4` |

## Verdict: ACCEPT-WITH-NITS

Every correction is applied exactly and nothing else changed. All hashes reproduce. The facts in the run bullet are
correct. r5b is ready for the owner to adopt as is, once the placeholders are filled (§5). Two optional wording nits
are listed in §4.

## 1. N1 applied to D402

The new D402 reads: "…cited for it; it is not established whether the entries require finiteness of the substratum;
this turns in particular on the measure conditions of Lemma 1c or Proposition 4b, the continuum conditions of the
$d = 3$ selection (§3.2) and, for $1/\alpha_0$, which is computed from the lattice momentum integral of §6.1 over the
whole Brillouin zone, on that integral's counterpart for a finite substratum and on the normalization of the vertex
coupling."

**What it does.**
- It states the uncertainty unconditionally, for all entries. The "where those theorems use …" construction is gone,
  so nothing implies that an entry outside a listed condition is independent of A1.
- All five open points stay named in the sentence:
  - the measure of Lemma 1c;
  - the measure of Proposition 4b;
  - the d = 3 continuum conditions;
  - the finite counterpart of the integral;
  - the vertex normalization.
- The text before "cited for it;" is byte-identical to r4.

**The completion of my "…" is correct.** It carries r4's reviewed 1/α₀ content unchanged: "computed from the lattice
momentum integral of §6.1 over the whole Brillouin zone", its finite-substratum counterpart, and the vertex
normalization. P's `INF` scan reports 0 hits.

**The descriptions that follow D402 all match the new text:**
- the D402 `reason` field;
- the §32.9 bullet "D402 states in the sentence that it is not established whether the entries require finiteness of
  the substratum, and names the conditions on which this turns";
- the §32.9 edit-table cell, which is exact against the record;
- the inventory's frame row and its strengthened? cell, which now reads "…without implying that any entry is
  independent of it where a listed condition is absent";
- the 1/α₀ row;
- the §2 sentence.

## 2. N3 applied; no other change to the inventory

`diff O13-INVENTORY-r4 O13-INVENTORY-r5` shows only these changes:
- the heading;
- the frame row (the D402 description);
- the Higgs row, where "E" becomes "none (unchanged)";
- the 1/α₀ row (the D402 description);
- the two §2 bullets that quote D402;
- the Appendix A source label, now "r5 ledger";
- D402's new_sha256 and new text.

I re-verified Appendix A against the r5 ledger and H (`inventory_check.out`). For all 11 edits the spans, both
hashes, the old bytes at H and the new text are correct.

## 3. Hashes and checks, reproduced in `review-r5/sb`

| Item | Result |
|---|---|
| `edits.json` | P's edits plus the r5 records: 412 records, `f99d705ae896c891806ee99c2217e24237cada5ac49e607b0b013bd43c6dd38d`. Matches. Between r4 and r5 only D402 changed, in its `new` and `reason` fields. |
| `ledger.json` | `--build-ledger`: 410 splices in 44 files, `65c8c866fa1ebebb338c869113ed3e1275a9aca1ededab58f6bdf286aab1a2e8`. Matches. |
| Ledger against r4 | Only splice D402 differs: same span, same old_sha256 `227117bc…`, new_sha256 `ac5a1b8504586ec1432cba5ec278947a6ecc025f2df101e1d794bd7c78592c32`. The other 409 splices are byte-identical to r4. Of the `files` entries, only `papers/SM.md`'s changes. |
| Configuration | The r4→r5 diff changes exactly the two pins, to `65c8c866…` and `f99d705a…` |
| PREREG r5 | Pure append onto P. Against r4, §32 differs only in the D402 table cell, the one bullet and the two §32.10 pins. |
| P's checkers | `--static` (infinity 0), `--simulate`, `--pins`, `--repo-scan --simulate --final`, `--verify-ledger`, `--verify-pins` (pin findings 0) and both self-tests: all exit 0 / PASS |
| Item 7 as frozen | PASS: the pointer grep finds only the 4 "(A1)" false positives; the count grep finds 0. NC1–NC5 each FAIL. |
| Gate tools on H plus D402–D412 | coverage, claims, voice, citation_roles and both label checks give the same output as at H. staleness reports SM and book as STALE, which is expected before the TeX is regenerated. |
| SM.tex | The diff against T1′ is confined to the SM:1394 paragraph (lines 7617–7631 of T1′) and the stamp. The stamp `ce949807…` equals my rebuilt SM.md. `work-r5/SM.tex.proposed` is `778c10c0…`. The FULL.tex diff is unchanged from r4. |

## 4. The O-13 text, r5b

**Against O13-DECISION-FINAL-r4.md** (the C1–C4 text), r5b differs only in:
- "proposal r5";
- the two digests;
- D402's new_sha256;
- the inventory file and its hash (two places);
- the review references, which add the r5 delta-review placeholder (two places);
- item 2's run bullet.

Item 2's other bullets, from C1 and C2, are unchanged.

**Run facts, verified by REST GET** (records are in `rest/`):

| Run | Workflow | Event and ref | Commit | Created | Conclusion |
|---|---|---|---|---|---|
| 45077568347 | `A1-EXIT trial verify` (`a1exit-trial-verify.yml`) | `workflow_dispatch`, `main` | `413b0bb8` | 2026-11-22T22:24:42Z | **failure** |
| 45080985924 | the same | `workflow_dispatch`, `main` | `413b0bb8` | 2026-11-22T23:02:06Z | success |
| 45083256017 | `verify` (`verify.yml`) | `workflow_dispatch`, `trial/a1exit-T1prime-4c79be64` | `14ac71b4` | 2026-11-22T23:26:21Z | success, with the jobs list showing 41 of 41 successful |

**The steps of run 45077568347** (jobs record): steps 1–8 succeeded; step 9 `preserve` failed; step 10 `guards` was
skipped; steps 11–12 succeeded; step 13, the final gate, failed.

**c.7087039188** (2026-11-22T22:44:06Z, never edited) records that:
- the run has "Conclusion failure, which N1 preregisters for T0";
- preserve's "only failing check is the comparison of the committed PDFs";
- TRIAL EXPECTED, RESULT PASS;
- "Unexpected failures, unexpected skips, infrastructure problems or missing evidence: none";
- "T0' acceptance awaits the owner's decision".

The plan's §31.8 states the T0′ expectation "as §29 item 1". The run's trial and plan inputs are as the comment records
them.

**c.7088175248** (2026-11-23T00:13:57Z, never edited) contains the quoted sentence verbatim: "Owner decisions in this
session accepting the T0' trial (run 45077568347, recorded at c.7087039188)". It also contains `--expect-trial T1`
TRIAL EXPECTED and `--expect-verify` TRIAL EXPECTED.

**The bullet is accurate.**
- It distinguishes the failed run from the two successful ones.
- It keeps all three runs.
- It does not present the failure as acceptance evidence, and it says that none of the three is acceptance evidence
  for the amended plan.

r5b's description, "a preregistered expected failure accepted as the T0′ trial", is correct and more accurate than
r5's bare "failure".

**Optional nits:**
- **(a)** The bullet's "(§31.8; N1)" could be confused with this series' review nit N1. Suggested: "(§31.8, as §29
  item 1)".
- **(b)** Both comments appear under the owner's GitHub account but were posted by the session's tooling (each ends
  "Generated by Claude Code"). c.7088175248 is the session's record of an in-session owner decision, not a separately
  authored owner comment. "accepted it as the T0′ trial in session, as recorded at #1169 c.7088175248" is accurate as
  it stands. To be fully explicit: "…as recorded by the session at #1169 c.7088175248 (posted under the owner's
  account)".

## 5. Ready to adopt; placeholder text

r5b is ready for the owner to adopt as is. Nits (a) and (b) are optional.

The two placeholders read "<focused delta review: file, sha256, verdict>". Replace each with:

> `review-r5/review.md` (sha256 `<SHA256 OF THIS FILE, as returned with this review>`), verdict ACCEPT-WITH-NITS

The sha256 of this file is reported in the hand-back message and in `review-r5/MANIFEST.sha256`; a file cannot
contain its own hash. The final text should be re-hashed after the fill.

## Files (`review-r5/`)

- `review.md`
- `item7.py` and `item7.out`
- `ledger_cmp.out` and `inventory_check.out`
- the checker outputs and `rc.out`
- `gate_tools.out` and `*_tree.out`
- `rest/`: the run, jobs and comment JSON
- `sb/` and `work/`

`tree/` and `tmp/` are scratch and are not in the manifest.
