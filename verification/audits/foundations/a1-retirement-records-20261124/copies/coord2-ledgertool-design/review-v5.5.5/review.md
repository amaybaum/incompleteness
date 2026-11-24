# Independent review of DESIGN-v5.5.5 (complete amendment v5.5.3 -> v5.5.5)

Reviewer: independent; wrote neither v5.5.4/v5.5.5 nor the v5.5.4 review. Read-only paper review;
no code run, no git or GitHub activity. Scope: the complete amendment v5.5.3 -> v5.5.5 against the
owner's decisions DI-1 (option B) and DI-2 (option A, narrow) and acceptance criteria 1-7, with the
owner's stopping rule (a finding blocks only with a demonstrated or concrete counterexample).

## Verdict: REVISE

Three BLOCKING findings (sec. 4), each with a concrete counterexample and a small text correction
(sec. 5). No authority bypass by a former, future or away-and-back owner was found on any path;
the blocking findings are one internal contradiction that makes a legitimate post-change
designation unadmittable, one residue of the v5.5.4 B2 defect, and missing rejection/acceptance
controls for two amended rules.

## 0. Inputs verified

| File | sha256 | Expected | |
|---|---|---|---|
| DESIGN-v5.5.3.md | 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379 | same | OK |
| DESIGN-v5.5.5.md | f6f966ebbf5bdd2363f7a02318b1c88981aac000b4c966570ee762908029aff9 | same | OK |
| CHANGES-v5.5.5.md | bf721f330959d54264a1cea37c44ec90841075a26814e07e7d9b0926b864dc8b | bf721f33…dc8b | OK |
| CHANGES-v5.5.5.diff | 8845dbf7657d2cc040cc008afdcfc13dbfd87e0a3439dbac5ea2cee57e867ae2 | 8845dbf7…7ae2 | OK |
| CHANGES-v5.5.5-from-v5.5.4.diff | 7f912a1594d101ca68b318e52d20651a1fca4f87264853c427e0bc659bbda292 | 7f912a15…a292 | OK |
| DESIGN-v5.5.4.md | 1ade8b8f43d6259c50ac9847c59e09ce71a645ba0cb8eabe7e1deb84bb4c5e34 | 1ade8b8f…4e34 | OK |
| review-v5.5.4/review.md | 34927de86bdbed0d8e8cc8e4e2438f18bf001082153bfddb283781767c5f0842 | same | OK |
| review-stage1-r4/review.md | e21cf9d34210ca4f41d6397a9f4b91d26674c9601f1399bacb8a57f9d2a5eae0 | (not given) | read |

Fresh `diff -u` of v5.5.3 -> v5.5.5 and of v5.5.4 -> v5.5.5 are byte-identical to the two `.diff`
files apart from the two header (timestamp) lines. 15 hunks; 3027 -> 3137 lines.

## 1. Scope, quotes and ids (criterion 6): MET

- All 15 hunks are DI-1, DI-2, C1-C4, the N3 cross-reference, or direct consequences (title, status
  bullet, snapshot field, merge-time trust attestation, S13 list). No unrelated rewording.
- Every old/new block in CHANGES-v5.5.5.md was checked by script to occur verbatim and
  contiguously in its file (30 blocks; 4 insertion-only "old" blocks).
- C1 and TR65/LN9/LN10 are verbatim from review-v5.5.4 sec. 5 (string compare); C2, C3 verbatim up
  to line wrapping.
- TR54-TR65 and LN1-LN10 (word-bounded grep over every DESIGN*/CHANGES*/diff in the design
  directory) occur only in v5.5.4/v5.5.5 and their change files, with the same meaning. No id reused.

## 2. Decisions and probes (criterion 1): MET

| Item | Closed by | Check |
|---|---|---|
| D1 former owner's designation | Designations bullet (author = governing owner) | TR54 |
| D2 former owner's unledgered withdrawal | Withdrawals bullet | TR55 |
| D3 pre-ownership designation | owner-comment definition | TR56 |
| L5 away-and-back approval | Approvals bullet (no owner change before merge) | TR57 |
| L6 pre-ownership approval | Approvals bullet | TR58 |
| E6 cross-lineage supersedes | lineage bullet | LN1, LN8 |
| v5.5.4 B1 (authorization records) | "Owner authorizations" bullet; point 7 | TR65 |
| v5.5.4 B2 (predecessor authorization vs today's owner) | lineage predecessor clause; predecessor sentence of "Owner authorizations" | LN9 (but see F2 for a residue) |

## 3. Authority paths re-enumerated (criterion 3)

Each path attacked with: former owner (posted while owner, evaluated after change), future owner
(posted before becoming owner), away-and-back (A -> B -> A between posting and evaluation).

| # | Path | Former | Future | Away-and-back | Result |
|---|---|---|---|---|---|
| 1 | `oi-freeze/1 designate` | author != governing owner: no | not owner comment: no | owner change between: no | holds |
| 2 | `supersede`, designating half | as 1 | as 1 | as 1 | holds |
| 3 | `withdraw` / revoking half | counts, binds (decision) | not owner comment: not processed | counts (decision) | holds, but see F1 (state machine) |
| 4 | ledger / snapshot bound events | revoke only; judged by recorded author and time | same | same | holds (K1 intact) |
| 5 | `oi-authority/1 approve` for `A` changes | governing = replaced version; also hash-bound `from=` | not owner comment | hash binding + no owner change | holds |
| 6 | `oi-authority/1 approve` for ledger changes | governing = in force at merge | not owner comment | refused (TR57) | holds |
| 7 | `oi-freeze-ledger/1 append` (N3) | as 6 | as 6 | as 6 | holds |
| 8 | first `A`; new id of owner-id change | n/a; authenticated as pinned id | before merge, no change between | hash-bound | holds |
| 9 | `oi-owner-authorization/1` for records the run uses (incl. reconciliation records after `F`, widening reviews, PIN_OK records) | owner != governing: no | owner not in force at `time`: no | owner change between `time` and admission: no | holds (TR65) |
| 10 | configuration's own authorization | point 7 + rule 9 | same | same | holds (ERROR CONFIG_UNREVIEWED) |
| 11 | `retirement.owner` | data field = current owner; authorization must still count | a future owner's field passes only with a counting authorization | same | holds |
| 12 | predecessor authorizations (DI-2) | completed action, owner at `time` | owner not in force: no (LN9) | counts (completed) | holds for the record's own authorization; **widening-review authorization: F2** |
| 13 | owner identity between admission and acceptance landing | acceptance predicate requires the same `A` blob as `main` now, so any `A` change between run and landing refuses | same | same | holds (unchanged sec. 5) |
| 14 | review records | no owner authority | - | - | n/a |
| 15 | merged-by id | provenance only | - | - | n/a |
| 16 | edit/hide of owner comments (point 3) | former owners' comments now included (refuse-only) | current id's pre-ownership comments included | - | fail-closed; no control (F3) |

Timestamp ties: "in force" uses merge time strictly before `t`; a comment at the same second as an
owner-change merge is judged under the old version. Not exploitable: designations, approvals and
authorizations also require the author/owner to equal the governing owner now, and an away-and-back
needs a second merge strictly later (N4).

Criterion 3: MET (no bypass; F1 and F2 are over-refusals, not grants of authority).

## 4. Findings

### F1 (BLOCKING): point 5 refuses every admission of a round once a former owner's withdrawal or supersession exists; contradicts TR61 and TR55

Text. Point 5: "A form, or half of a supersession, that does not count under "Owner at creation"
is not processed", and the refusal "a withdrawal or supersession naming a commit never
designated". After an owner change, a former owner's designation does not count and is not
processed, while that owner's later withdrawal or supersession counts and is processed. In the
processed sequence the withdrawn commit was therefore "never designated", and the admission refuses.

Counterexample (TR61, second case). 4242 designates `F`; 4242 supersedes `F` by `F2`; 4242 -> 5555;
5555 designates `F2`. Processing: D(4242, F) not processed (author != governing owner); S(4242)
revoking half processed and names `F`, never designated in the processed state -> refuse. TR61
expects "admission of `F2`: ... admitted in the second". The same holds for any new `F'` 5555
designates in that round: the round can never be admitted again, although the owner decision says a
former owner's withdrawal "stays effective" (it should keep `F` withdrawn, not refuse the round)
and the design says "the round is designated again by the owner in force". TR55's stated reason
("designation of a withdrawn commit") likewise presupposes that `F` counts as designated. v5.5.4
had the same text; the contradiction is with the new controls and with the DI-1 bullet.

Correction: C5 (sec. 5).

### F2 (BLOCKING): a predecessor's widening-review authorization is still compared with today's configuration owner (residue of v5.5.4 B2)

Text. The predecessor must "itself pass this lint"; the lint includes the widening rule ("an owner
authorization lists the widening review's blob", "under the same chain as any review (B4)"), hence
the unchanged bullet "an authorization whose `owner` differs from the configuration's owner". C2
replaces that comparison only for "the authorization" of the predecessor, and the C1 sentence speaks
only of "The authorization of a predecessor". A widening review's authorization may be a separate
authorization record (any authorization record may list any set of `{record, review}` pairs).

Counterexample. Allow-rule lineage L: R0; R1 supersedes R0 and widens it; R1's own authorization
and, in a separate record, its widening review's authorization are by 4242 while owner (valid,
completed). 4242 -> 5555. R2 supersedes R1, reviewed and authorized by 5555 (with its own widening
review if needed). Lint of R2 -> predecessor R1 -> R1's widening is valid only with an authorization
whose `owner` 4242 differs from the configuration owner 5555 -> R1 fails -> R2 FAIL
`record-invalid`. The same arises for every configuration lineage (sec. 16.2: every configuration
change is widening unless on the non-widening list). A completed valid action is invalidated by a
later owner change (DI-1; criterion 5). LN9 does not cover it.

Correction: C6 (sec. 5).

### F3 (BLOCKING under criterion 7): two amended rules have no control on one side

- Withdrawals bullet, rejection side: a withdrawal (or revoking half) that is not an owner comment
  at its creation (a future owner's pre-ownership withdrawal) is not processed. No control
  (TR7 covers designations only; TR55/TR61 cover the acceptance side).
- Point 3 extended to every owner comment at creation (former owners' comments) and point 4 parsing
  "the owner comments of point 3": no control on either side (v5.5.4 review N1 recommended one; not
  added).

Criterion 7 requires rejection and legitimate acceptance for every rule. Correction: C7.

### NON-BLOCKING

- **N1.** TR54 (second case), TR61 (second case) and TR60 say "admitted". In a full chain, an `F`
  designated before an owner change cannot be admitted after it: its configuration's authorization
  is in `F`'s tree and so predates the change (C1, point 7). These positives are reachable only in
  the control harness (sec. 6.3: it "may admit a draft configuration without its chain") or, for
  TR60, with an `F` frozen after the change. Recommend "`F` is the one designated commit at point 5
  (control harness)" and, in TR60, "an `F` frozen after the change". Operational consequence for the
  owner: after an owner change every pending `F` is re-frozen with the new owner's authorizations,
  which DI-1 ("current owner when evaluated") requires.
- **N2.** Where the predecessor's review and authorization records are looked up is not stated
  ("read from the object store at or before `F`"). Recommend: the audit directory and the plan's
  record directory at `F` (the domain fork detection uses). Fail-closed either way.
- **N3.** Authorization `time`, `owner` and `comment_id` are writer-asserted and not host-read (the
  existing "Residual limit"); the DI-1 checks on authorization records are as strong as that data.
  Honest records of pre-ownership comments are caught; forgery was already outside v5.5.3's model.
- **N4.** "between its creation and the admission/merge" does not state whether an owner-change
  merge at the same second as the comment is "between"; not exploitable (sec. 3). Recommend
  "at or after its creation".
- **N5.** A former owner can make all later admissions refuse by editing an old comment into a form
  (point 3), or by editing an approval of a completed ledger change. Fail-closed; the moderators'
  hide power is comparable.
- **N6.** Point 4's line "by the forms" is left short instead of reflowed; cosmetic.

## 5. Corrections (exact text)

**C5 (F1).** In admission point 5, replace

`of the following refuses: two live designations; a withdrawal or supersession naming a commit
never designated; a designation of a withdrawn commit; any other conflict.`

by

`of the following refuses: two live designations; a withdrawal or supersession naming a commit
never designated (for this test, a designation that was an owner comment at its creation has
designated its commit, even if it is not processed); a designation of a withdrawn commit; any other
conflict.`

(With this, TR55 refuses for the stated reason, TR61 behaves as stated, TR54/TR56/TR59 are
unchanged, and nothing becomes designated that was not before.)

**C6 (F2).** (a) In the lineage predecessor clause, replace
`the authorization checked as "Owner at creation" states for a predecessor,`
by
`each authorization its lint requires, a widening review's included, checked as "Owner at
creation" states for a predecessor,`.
(b) In "Owner authorizations", replace
`The authorization of a predecessor named by a `supersedes`
  is a completed action: it counts if`
by
`Each authorization of a predecessor named by a `supersedes`, a widening review's included, is a
  completed action: it counts if`.
(c) Control (new id):

```text
| LN11 | an allow rule R1 widening R0, R1's widening review authorized by 4242 while owner in an authorization record separate from R1's own; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run; separately, the same for a configuration lineage | no `record-invalid`; the run uses R2, in both | DI-1, DI-2 |
```

**C7 (F3).** Controls (new ids):

```text
| TR66 | 4242 designates `F`; 5555 posts `oi-freeze/1 withdraw` of `F` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness). Separately, the withdrawal posted by 4242 before the change | the first: `F` is the one designated commit at point 5 (the withdrawal is not an owner comment and is not processed); the second: ERROR (designation of a withdrawn commit) | DI-1 |
| TR67 | a comment without a form, created by 4242 while owner; 4242 -> 5555; the comment then edited by 4242 into a first line beginning `oi-freeze/`. Separately, the same comment left unedited | the first: ERROR (point 3); the second: no refusal from point 3 or 4 | DI-1, point 3 |
```

Consequential: status bullet "TR54-TR62, TR64 and TR65" -> "TR54-TR62 and TR64-TR67"; "LN1-LN10" ->
"LN1-LN11" (status bullet and S13); S13 "TR1-TR65" -> "TR1-TR67"; CHANGES updated.

## 6. Criteria

| # | Criterion | Met | Evidence |
|---|---|---|---|
| 1 | D1-D3, L5/L6, E6, v5.5.4 B1/B2 closed | yes | sec. 2; TR54-TR58, LN1, TR65, LN9 |
| 2 | lineage unambiguous, independently verifiable | yes | same kind/schema/`record_id`, cycles, forks, two heads, `A` by path + first parent (TR63); lookup domain N2 |
| 3 | all authorization paths protected | yes | sec. 3, 16 paths, no bypass |
| 4 | `record_id` limited; null/no-id records usable | yes | id required only in a chain; LN10 |
| 5 | completed actions not invalidated | **no** | F2 (predecessor widening authorization) |
| 6 | diff scope, exact quotes, no id reuse | yes | sec. 1 |
| 7 | controls precise, both sides of every rule | **no** | F1 (TR61 contradicts point 5), F3 (withdrawal and point-3 rules) |
| - | consistency with unchanged text (TR32, N3, authority-change procedure, points 1-7, reconciliation, forms, K1) | yes except F1 | K1 holds: recorded supersessions only revoke; point 5 cross-reference consistent |
