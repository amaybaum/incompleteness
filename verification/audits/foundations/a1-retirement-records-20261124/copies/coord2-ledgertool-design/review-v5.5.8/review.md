# Review of DESIGN-v5.5.8 (bounded verification)

Reviewer: independent; wrote neither the draft nor any earlier review. Read-only except this directory.

Inputs (sha256 verified): DESIGN-v5.5.8.md f531948147b3638c5ad567f5ccf0eedfd04650a30be9fd0a9f2084aa13a77ad2;
DESIGN-v5.5.7.md 0a7efa040af44c4bf1e09b3ba026eb6e2a1a0fecc413516a0c2fcbc629504f6f;
DESIGN-v5.5.3.md 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379;
review-v5.5.7/review.md 761585bbbb6be90fd374152d4a6b08455a765170bc87cd9fe7ca875291792c2b.
`sha256sum -c v5.5.8-MANIFEST.sha256`: all four entries OK (DESIGN-v5.5.8.md, CHANGES-v5.5.8.md,
CHANGES-v5.5.8.diff, CHANGES-v5.5.8-from-v5.5.7.diff).

## Verdict: ACCEPT

## 1. Scope: MET

- `diff -u DESIGN-v5.5.7.md DESIGN-v5.5.8.md` reproduces CHANGES-v5.5.8-from-v5.5.7.diff (headers
  aside) and has 6 hunks: title (l.1); status bullet (l.10, 13, 16, 18: version label, "supersedes
  the v5.5.7 draft", "TR54-TR62, TR64-TR70", "LN1-LN12", CHANGES file name); TR60 (l.2338); TR68,
  TR69 and new TR70 directly after TR69 (l.2346-2348); new LN12 directly after LN11 (l.2583); S13
  (l.3147: "LN1-LN12", "TR1-TR70"). Nothing else differs.
- `diff -u DESIGN-v5.5.3.md DESIGN-v5.5.8.md` reproduces CHANGES-v5.5.8.diff (14 hunks).
- v5.5.6 vs v5.5.8: every differing line outside TR/LN/S13 rows is the title or status bullet; no
  design rule text differs from v5.5.7 or v5.5.6.
- TR70 and LN12 are byte-equal (cmp) to the single rows in review-v5.5.7 B-3 and B-4.

## 2. Consistency: MET

Traced against sec. 6.3 "Owner at creation" (l.1321-1360), "Authority changes" (l.1408-1418),
admission points 3-7 (l.1488-1528), lineage lint (l.1248-1257) and widening (l.1612-1618).

- TR60: 5555's designation after the change is an owner comment of the governing owner with no
  later owner change; the configuration authorization by 5555 after the change has owner in force
  5555 = its `owner`, equal to the governing owner, no later change, so point 7 passes; the earlier
  append and authority change are completed actions. `F` admitted - follows (full chain).
- TR68 (with N-3 clause): case 1, the approval was not an owner comment (owner in force 4242) and
  an owner change merged after it; case 2, an owner comment but owner changes merged between its
  creation and the merge ("away and back does not restore"); case 3, an owner change merged between
  the new-id approval and its merge. Each: ERROR. Isolation clause changes no outcome.
- TR69: 5555's first designation was not an owner comment at creation, so for the C5 test it has
  not designated `F`; 5555's withdrawal after the change is processed and names a never-designated
  commit: refusal. The refusal is a round-state condition at point 5, so admission of `F'` also
  refuses: ERROR - follows.
- TR70 (control harness): 4242's designation is not processed (owner change before admission) but
  has designated `F` for the C5 test; 5555's supersession was not an owner comment, so neither half
  is processed (point 5 l.1510; the designating half also fails "Designations"); 5555's later
  designation counts. No two live designations, `F` not withdrawn, the unprocessed supersession
  names a designated commit even if tested. `F` is the one designated commit at point 5 - follows.
  "(control harness)" is correct: in a full chain point 7 would depend on `F`'s configuration
  authorization, which the row does not specify (same pattern as TR54, TR66).
- LN12: case 1, R1's widening-review authorization is a predecessor's completed action and counts
  only if the owner in force at its `time` (4242) equals its `owner` (5555): it does not count;
  case 2, no authorization. Either way the widening review is invalid, R1 fails its lint (widening
  without a valid widening review), so R2's `supersedes` names a predecessor not passing lint:
  FAIL `record-invalid` for R2 - follows.

## 3. Closure: MET

- B-3: wrong implementation W1 (processes the revoking half of every parsed supersession) withdraws
  `F` at 5555's pre-ownership supersession and then refuses 5555's designation as a designation of
  a withdrawn commit: ERROR, versus the correct "`F` is the one designated commit". Differs by
  outcome.
- B-4: wrong implementation W2 (predecessor widening-review authorization unchecked or existence
  only) passes R1, so R2 gets no `record-invalid` in either case, versus FAIL `record-invalid`.
  Differs by outcome.
- N-1: a wrong C5 test (every designation counts as "has designated") treats the withdrawal as
  valid, `F` withdrawn, and admits `F'`; the correct text refuses `F'`. TR69 now differs by
  outcome, not only by reason.

## 4. Ids and quotes: MET

- Word-bounded grep (`grep -cw`) over every DESIGN*.md and CHANGES*.md: TR70 and LN12 occur only in
  DESIGN-v5.5.8.md (3 each: status bullet, row, S13) and CHANGES-v5.5.8.md; no earlier file uses
  either id. No TR/LN row id is duplicated in v5.5.8's tables.
- CHANGES-v5.5.8.md: all 28 old/new blocks of its 14 v5.5.3-relative hunks occur verbatim in
  DESIGN-v5.5.3.md / DESIGN-v5.5.8.md (5 old blocks are "(none: insertion only)"); TR60, TR68,
  TR69, TR70, LN12 lines quoted in CHANGES equal the design rows; hunk headers listed in both hunk
  tables equal those of the two committed diffs; its account of non-verbatim placement (N-1 split
  across columns, N-3 wording, N-2 verbatim) matches the diff.

## Non-blocking (out of scope)

- O-1. Control id Z9h appears as a row in two tables (l.2358 sec. 10 and l.2920 sec. 16) with
  differently worded setups; pre-existing and identical in v5.5.3, not introduced by this
  amendment. Same control restated, not a reuse for a different meaning.
- review-v5.5.6 N8-N12 and review-v5.5.5 N2-N6 not re-examined.
