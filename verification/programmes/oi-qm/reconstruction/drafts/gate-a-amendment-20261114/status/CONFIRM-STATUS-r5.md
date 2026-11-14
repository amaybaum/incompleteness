ACCEPT WITH CHANGES — `STATUS-r5.md` at exact head `f6698a9a2357690c616fdedc691b20a5d6676fe2` (branch `research/gate-a-amendment-1169-20261114`, PR #1289)

# Focused review of STATUS-r5.md (landing-status note for the Gate A amendment record)

This is a model review of the text at the head above. It is not an owner decision. It was done by
a non-author, read-only and paper-only, on 2026-11-14 at about 13:05Z–13:10Z, using `git` inspection
of the record checkout, grep and public GitHub API reads. Nothing was computed on OI rules,
nothing was built or dispatched, and nothing was edited, committed, pushed or posted. It is not
independent mathematical verification (§A.46 item 8). `S5:n` means line n of `STATUS-r5.md`;
`README:n` means line n of `status/README.md` at the head.

## Head and files

- Checkout `HEAD` = `f6698a9a2357690c616fdedc691b20a5d6676fe2`. This equals `git ls-remote origin`
  for the branch and the PR #1289 API head. `main` = `dfeec843`.
- `f6698a9a` is a single-parent child of `c7806483`. It changes three files, all under `status/`:
  it adds `STATUS-r5.md` and `RESPONSE-STATUS-r5.md` and edits `README.md`.
- `STATUS-r5.md`: 278 lines, SHA-256 `082749cd…0f93`. Both match the README row and the response
  note. `STATUS-r4.md` still has SHA-256 `c55797bd…8725`, so r4 is unchanged.

## 1. r4 → r5 diff: every hunk accounted for (PASS, one low note)

`diff STATUS-r4.md STATUS-r5.md` gives 14 hunks. Each maps to a row of `RESPONSE-STATUS-r5.md`:

| Hunk (r5 lines) | Response item |
| --- | --- |
| S5:1 (title) | status line |
| S5:10–13 (header) | status line; item 4 |
| S5:17–18 (read window) | covered by the response's stated read window, not itemized |
| S5:28–32 (§0 head) | item 5 |
| S5:91 (B⇒ row) | item 1 |
| S5:148–159 (§2 #1291 bullet) | item 1 |
| S5:191 (item 8 table header) | item 5 |
| S5:195–196 (item 8 rows) | status line; item 2 |
| S5:222–223 (off-`main` rows) | status line; item 1 |
| S5:240–243 (§4 review, condition, exact-head, CI rows) | status line; items 4, 5 |
| S5:245 (draft row) | item 5 |
| S5:264–265 (§6 item 4) | item 4 |
| S5:275–276 (§6 item 8) | item 3 |
| S5:277–278 (§6 item 9) | status line |

No other text changed. The response says "Nothing else in r4 is changed", which holds.

- **L1 (low).** S5:222 now also lists `status/RESPONSE-CONFIRM-STATUS-r3.md`. The response note's
  status line names only "r3's review file". The addition is correct; it is just not itemized.

## 2. The three corrections from the review of r3 (PASS)

All three are still in place in r5.

- **RQ-1.** The replacement intro is at S5:79–81. The quotation of #1169 comment 6877532844 is at
  S5:134–147. The read bound "comments through 2026-11-14T12:52:30Z" is at S5:179–180. The
  off-`main` row for that comment is at S5:224, classified as quoted with author and time.
- **RQ-2.** S5:196 states §A.46 item 8's own condition separately from §A.45 rule 6.
- **RQ-3.** S5:91 keeps the wording "correlations outside the quantum set for a member inside C
  (r4 §5.2, B⇒)" and the sentence on #1060's body.

RQ-1's §6 item 8 wording and RQ-3's "for the rest of the exclusion see §3 and §6 item 8" were
replaced. Both replacements follow from #1291 being opened (response items 1 and 3) and are
justified.

## 3. #1291 and its pointers, against the API (PASS, three low notes)

**#1291 itself.** It is open and was opened from `amaybaum` (OWNER) at 2026-11-14T13:00:58Z. It
has no comments and no labels. The following match the body verbatim:

- the question (S5:91);
- the planning-status block: tier, prerequisites and readiness read "undetermined pending owner
  decision", and authorization reads "not authorized" (S5:91, S5:154);
- the "**Owner decision** … "I adopt all three"" sentence and the three adopted items (S5:149–154);
- the status section (S5:155–157);
- the fifth requirement (S5:91; the source sets it in bold).

r5 correctly reports that the body's "leaving Tier, Readiness and Authorization undetermined" does
not match the block's Authorization "not authorized" (S5:154).

**The pointer comments.** All three are from `amaybaum` (OWNER) and their quoted fragments are
exact:

- #1060 comment 6877627984 (13:01:10Z): "this Issue is unchanged";
- #868 comment 6877628305 (13:01:12Z): "its scope, readiness and authorization are unchanged";
- #914 comment 6877628626 (13:01:13Z): "The scientific obligation is open."

S5:196 says #1291 is "linked from #1060, #868 and #914". That is true.

**Scope and status.** r5 does not present the obligation as resolved. S5:91 ends "The obligation
is open". S5:196 says that §A.45 rule 6 is met for accountability only and that "the scientific
obligation remains open". This matches #1291's status section.

- **L2 (low).** The #914 pointer (6877628626) says "Tier, readiness and authorization are
  undetermined pending the owner's decision". That repeats the body's mismatch with the block. r5
  quotes only that comment's last sentence, so nothing in r5 is wrong. However, the parenthesis at
  S5:154 could add that the #914 pointer reads the same way.
- **L3 (low).** On S5:91, #1291 appears only in the "Missing / what would resolve it" cell. The
  "Accountable Issue" cell still names #1060 alone. S5:196 treats #1291 as this row's accountable
  Issue for the residual. Suggestion: add "#1291 (QSET-EXCL), for the exclusion beyond the
  Tsirelson bound" to the Accountable Issue cell, so that the column agrees with §3.
  Separately, #1291's question is worded over the whole quantum-set exclusion ("including
  correlations that satisfy the Tsirelson bound but are not quantum"). Its "Why this Issue exists"
  section and the three pointers limit it to the part beyond the Tsirelson bound. r5's split
  (#1060 for the bound, #1291 for the rest) follows the pointers and is consistent with
  requirement 2.
- **L4 (low, unverifiable source).** The owner's words "I adopt all three" were given "in the
  coordinating session". That session is not readable here. The words and the list of three
  adopted items are attested only by #1291's body, posted from the owner's account. Each pointer
  comment carries a "Generated by Claude Code" footer. S5:101–103 already says the note checks
  comment text, not the session. This review accepts the quotation as an accurate quotation of the
  Issue and does not verify it against the session.

## 4. §A.45 rule 6 and §A.46 item 8 against `AGENTS.md` (PASS, informational note)

**At the branch head.** `AGENTS.md` at `f6698a9a` is the branch's copy from base `c3b5f37a`. Its
§A.46 ends at item 7 and has no item 8. r5 does not rely on it. S5:41 pins "`AGENTS.md` at
`dfeec843`", and S5:243 records that the test-merge tree differs from the head's only in
`AGENTS.md`.

**At `dfeec843`, every r5 statement checked matches:**

- the conditions of item 8: "substantive, nonredundant result"; "independent non-author review and
  a ChatGPT exact-head review" with §A.42 item 8 tracing; "an accountable Issue, a verification
  status and, for each verification gap still open, a remediation plan (item 4)"; rationale and a
  separate recorded owner merge decision;
- "A model's acceptance is evidence of review, not independent mathematical verification"
  (S5:63);
- the surviving-claim sentence (S5:200–201).

§A.45 rule 6 reads "One obligation, one accountable Issue" at both `dfeec843` and the head, as
quoted at S5:196.

The text after S5:196's "Separately" applies rule 6 to obligations. That is the note's own stated
reading, labelled as such.

- **I1 (informational).** The pin to `dfeec843` is correct and needs no change. It does mean that
  the policy text r5 relies on is not in the branch's own tree. Updating the branch with `main`
  (§6 item 5) would bring it in.

## 5. Head and CI statements (PASS, two low notes)

Checked against `git` and the API:

| Statement | Location | Result |
| --- | --- | --- |
| Chain through `c7806483` at 12:59:20Z | S5:27–30 | matches |
| `c3b5f37a..c7806483`: 28 files, 5513 added lines, 9 commits | S5:31–32 | matches |
| 9 ahead and 9 behind `main` at 13:02Z | S5:245 | matches |
| Run 43596974572 at `acfdbd0f`: completed 13:01:49Z, 26 success, 1 skipped | S5:243 | matches |
| Run 43597480770 at `c7806483`: "in progress when read at 13:02Z; its outcome is not recorded here" | S5:243 | accurate as dated |

The run at `c7806483` was created 12:59:32Z and has since completed (13:05:38Z, 26 success,
1 skipped). r5 does not guess the outcome.

Three facts are taken from the note, not verified:

- the test-merge commit `0cdbe5c2`, because the PR's merge commit has moved with the head;
- "PR #1289 has no reviews or comments" (S5:195), which the API confirms (0 and 0);
- run 43597893603 at `f6698a9a` (`pull_request`, in progress when read). r5 cannot name this run
  and does not.

- **L5 (low).** S5:241 says "the run at the current head is in progress (next row)". The next row
  (S5:242) is the exact-head review row; the CI row is S5:243. "Current head" also means
  `c7806483` as read, not the commit that carries r5. Suggested wording: "the run at `c7806483`
  was in progress when read at 13:02Z (row "CI at the final head")".
- **L6 (low).** S5:179–180 still bounds the adoption search at "comments through
  2026-11-14T12:52:30Z; none later at 12:57Z". r5's reads ran to 13:03Z. Comments posted after
  12:52:30Z exist: #914 6877628626 at 13:01:13Z, and the #1060 and #868 pointers. None adopts the
  amendment, so the conclusion stands. The bound could be refreshed to "comments through
  2026-11-14T13:01:13Z", which r5 itself quotes in §2.

## 6. Quoted owner words (PASS where readable)

**Read and verified.** The #1291 body, the three pointer comments (§3 above), and the §A.45 rule 6
and §A.46 item 8 wording match their sources exactly.

**Not re-read here.** The other owner quotations (S5:42–44, S5:105–147) are unchanged from r4.
The review of r3 checked them against the API, and this review relies on that.

**Not verifiable.** The session words behind "I adopt all three" (L4).

## 7. Adoption, contracts and authorization (PASS)

r5 adopts nothing:

- It does not adopt the amendment (S5:170–184).
- It changes no contract. `endpoints.md` is unchanged (S5:173).
- It authorizes no merge or work (S5:13–15, S5:235–236, S5:244).
- It does not assign S-J or exactness to an Issue. S5:196 and S5:275–276 say so explicitly and
  leave the choice as an owner question.
- It does not treat #1291 as authorizing work. S5:91 and S5:154 quote "not authorized".

S5:241 states that the owner's acceptance condition is not yet met. §6 item 4 (S5:264–265) leaves
open whether that condition, which names r4, applies to r5.

## 8. Writing rules (PASS for r5 and the response note; see M1 for README)

Grep over `STATUS-r5.md`, `RESPONSE-STATUS-r5.md` and the README lines this commit added found:

- no "closes/fixes/resolves #N";
- no absolute paths;
- none of the three prohibited words the request names (the session working-space term, and the
  two hyphenated state terms);
- no new capitals used for emphasis.

S5:156 contains "Issue closes only the accountability gap". This is a quotation from #1291, not a
closing keyword. The register is plain.

- **L7 (low).** S5:222's label still reads "The non-author review of r1 of this note, the response
  and the confirmation of r2", but the cell now lists the review of r3 and its response as well.
  Suggested label: "The reviews of this note and their responses (r1–r3)".

## README entries added by `f6698a9a`

**Rows.** The `STATUS-r5.md` row's digest matches. The `RESPONSE-STATUS-r5.md` row has no digest,
as other response rows do not. The `STATUS-r4.md` row's digest matches.

- **M1 (medium).** README:30–31 reads "r4 and r5 are unreviewed, and the note remains a draft
  until a focused review of r5 accepts it." This conflicts with the owner's condition and with
  r5 in three ways:
  - The owner's condition, quoted from #1291, names r4. It also requires that "its corrections are
    confirmed" and that "CI passes", in addition to a focused review returning ACCEPT on the exact
    head.
  - r5 itself leaves open, as an owner question, whether the condition applies to r5 (S5:241,
    S5:264–265).
  - The README sentence treats that question as settled for r5 and drops the CI and confirmation
    clauses.

  Suggested replacement: "r4 and r5 are unreviewed. The owner's acceptance condition (#1291)
  names r4 and requires confirmation of its corrections, a focused review returning ACCEPT on its
  exact head, and passing CI; whether it applies to r5 is an open owner question (r5 §6 item 4)."
- **L8 (low).** README:29–30 says "The owner then opened that obligation's accountable Issue,
  #1291". r5's wording is "opened from `amaybaum`" with the decision quoted (S5:148). "Opened by
  owner decision, from the owner's account" would match r5 and the pointers. README:29 also runs
  to 116 characters, unlike the surrounding wrap.

## Summary of findings

| Id | Severity | Lines | Point |
| --- | --- | --- | --- |
| M1 | medium | README:30–31 | restates the acceptance condition as "a focused review of r5", dropping r4, confirmation and CI; pre-decides §6 item 4 |
| L1 | low | S5:222; response | `RESPONSE-CONFIRM-STATUS-r3.md` added but not itemized |
| L2 | low | S5:154 | the #914 pointer repeats the "undetermined" wording for authorization |
| L3 | low | S5:91 | #1291 not in the Accountable Issue cell of the B⇒ row |
| L4 | low | S5:149–154 | "I adopt all three" is a session quotation attested only by #1291's body |
| L5 | low | S5:241 | "(next row)" points to the exact-head row, not the CI row; "current head" is ambiguous |
| L6 | low | S5:179–180 | adoption-search bound not refreshed to r5's reads |
| L7 | low | S5:222 | row label lists r1/r2 only |
| L8 | low | README:29–30 | "The owner then opened" vs r5's "opened from `amaybaum`"; line length |
| I1 | informational | S5:41 | branch `AGENTS.md` lacks §A.46 item 8; r5 correctly pins `dfeec843` |

None is blocking for preservation as a draft. M1 and L5 should be fixed before this note is
accepted under the owner's condition. The remaining low findings are optional.
