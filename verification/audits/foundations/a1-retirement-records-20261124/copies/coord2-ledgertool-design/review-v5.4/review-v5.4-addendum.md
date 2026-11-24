Addendum to review-v5.4: the owner's points of 2026-11-23

This addendum belongs to `review-v5.4.md` (sha256 bc0921e37a1d941f3845b200dd90e744dcf0fdd635f8cac7fb2b6ca9d67af854), which is unchanged. It answers the owner's points against DESIGN-v5.4 (sha256 a980251709485e7c1b26c91c32a18d8fdf412adb6f6d8058c382892bc29b9cb3). The verdict stays **REVISE**. The required corrections V1-V5 of the review stand, and the changes below are added to them.

This is read-only work. No host call was made, and the only new evidence comes from my v5.4 scripts.

1. Parity: the two stricter-than-P cases, classified

Being stricter is not by itself the same as being equivalent. For each case below I state what the tool would accept if it did not refuse, and whether that differs from the frozen plan.

- **(i) A splice built for the variant P does not select (S11-58g): a justified fail-closed addition, not a parity defect.**
  - The frozen plan consists of P's edit list and the ledger frozen at `F`. P applies the variant `variant()` selects.
  - A splice for the other variant writes different bytes into the corpus than P's application would. Accepting it would let the retirement's actual edit diverge from the frozen plan.
  - Refusing is therefore required for equivalence with the plan's edit; it is not extra strictness.
  - Items 5 and 6 are still computed per edit, both pairs, exactly as P computes them, so no item-5 or item-6 verdict differs from P.
- **(ii) One splice covering two edits (S11-57c): a justified fail-closed addition, not a parity defect.** Here P's combined application and the splice can produce the same bytes, so the result text could equal P's. The refusal is still justified for two reasons:
  - The frozen ledger schema ("a1exit deletion exact-edit ledger v2") gives each splice exactly one `id`, an edit id. A splice that stands for two edits cannot name both, so it is a malformed ledger under the plan's own schema, not a different reading of P.
  - Items 5 and 6 again equal P's per edit. The refusal is an integrity ERROR on the ledger input, not a different verdict on anything P checks.

  The owner should still confirm this, because P alone would not object to the combined text.
- **(iii) Chained edits (not listed by the writer; review V1): justified fail-closed, for the owner to confirm.**
  - P can apply an edit whose `old` text an earlier edit created. No set of disjoint splices at `H` can represent that, so the ledger cannot express the plan's application.
  - Refusing is the only safe outcome. It does not occur in A1: all 401 edits bind 1:1, as `out54-a1bind.txt` shows.
  - The design must name this case and give it a control (review V1).

Under condition 2, none of the three changes a result that P computes. Each refuses a ledger that cannot faithfully encode P's application. My classification: justified fail-closed additions, provided the design states, for each case:

- why the ledger is unfaithful or malformed;
- that P's per-edit result for items 5 and 6 is still computed and recorded.

v5.4 states this for (i) and (ii), but not for (iii).

2. Trust bootstrap

- **Repository and run identity, independently of `A`: met in principle.**
  - The tool and the consumer each read the run record from the host API by the host-assigned run id. The record states the repository's numeric id and fork status.
  - That attestation is read before `A` and does not depend on it. `A` is then read from `main` of the attested repository, and `A.repository` is only compared with it.
  - Caveat, review V2 and V3: run identity currently binds the repository and the workflow file, but not the commit the run executes from or the code it runs. Until V2 and V3 are fixed, run identity is incomplete.
- **The first `A` cannot authorize itself: met.** v5.4 states that the first version of `A` cannot be authenticated from its own content, and that the merged-by check is a consistency check only. Its integrity is a stated residual trust assumption: the reviewed, owner-merged first landing.
- **Recommended strengthening (part of point 3).** The bootstrap merge should also carry the owner's explicit approval comment, in the approval form below. That comment should be checked by the same host means as a designation, against the numeric id the new `A` pins. This is still a consistency check for the first `A`, because the id comes from `A` itself, but it makes the bootstrap approval host-verifiable on record. That circularity cannot be removed and must stay named as a residual.

3. Authority changes: approval as distinct from a merge by the owner's account (not met)

v5.4 requires each later change to `A` to be:

- a merge with "its own review record and owner authorization (sec. 6.3)";
- merged by the numeric id that the previous `A` pins.

This does not meet the owner's preference, for two reasons:

- A sec. 6.3 owner-authorization record quotes an owner comment with `comment_id`, but the tool never checks that quote against the host. Sec. 6.3's residual limit says identity "rests on the reviewer's and the owner's own recorded statements". So the approval is not "verifiable by the same means as designations".
- The merge by the owner's account is provenance. It does not show that the owner approved this content.

**Changes needed:**

- (a) An authority change takes effect only with an **owner approval comment**. That comment must:
  - be in the thread `A` names for authority changes;
  - use the exact versioned form below;
  - quote the sha256 of the new `A` blob and the sha256 of the `A` it replaces.

  It is verified exactly as a designation is: author numeric id equal to the previous `A`'s owner id, never edited, not hidden, the thread read completely, and the same rules for deleted, superseded and ambiguous comments, including review V4.
- (b) Besides the approval comment, the change needs an independent review record that names both blobs and is bound to the new blob by sha256 (sec. 6.3).
- (c) The merge by the pinned owner id stays a required provenance check. It is no longer the authorization.
- (d) An owner-id change itself must be approved by the old owner id. If the new `A` pins a different id, the approval must also come from that new id, so that a mistyped id cannot take effect.
- (e) Controls:
  - a merge by the owner's account with no approval comment: refused;
  - an approval comment quoting another blob: refused;
  - an approval comment edited: refused;
  - an approval by another numeric id: refused;
  - an owner-id change approved only by the old id: refused.

4. Comment handling: always fail-safe (not met today; review V4 and V5)

- **Edits.** Read the edit status of every comment of the owner id in the thread. A designation, withdrawal, supersession or approval with any recorded edit refuses, and so does a comment whose edit history ever contained a form's first line. v5.4 checks only comments that are relevant by their current text, so a withdrawal edited into an irrelevant comment revives a designation.
- **Withdrawals and supersessions.** A deleted withdrawal or supersession revives the earlier designation, because deletion is invisible to a listing and to the current count. One of the following is needed:
  - a durable second record of the round's state, for example each withdrawal or supersession also landed as an owner-approved change on `main`, so that a designation is admitted only if `main`'s record agrees with the thread;
  - a host deletion-event check, if the host exposes one, with refusal on any deletion in the thread;
  - an explicit residual naming who can delete comments, which falls short of "always fail-safe".
- **Missing comments.** A missing designation already refuses (TR19).
- **Ambiguous ordering.** Ordering by creation time and then comment id is deterministic, and conflicts refuse. Add that a relevant comment for another plan, or a form of an unknown version, refuses.
- **Line endings.** Define the first line as the bytes up to the first LF, with one trailing CR removed and no other normalization (review V5).

5. Durable evidence: independent check and regeneration (partly met)

v5.4 commits:

- the accepted `result.json` and its sha256;
- the commits;
- the configuration, `A`, engine and workflow hashes;
- the designation data (comment ids, author ids, times, edit status and first-line sha256);
- the command and a regeneration recipe.

Re-running reproduces the result "as long as the designation comments are unchanged". That makes regeneration depend on mutable host state.

**Changes needed:**

- (a) Commit the admission snapshot. For every comment the decision used, record:
  - id;
  - author numeric id;
  - creation time;
  - edit status;
  - the full first line;
  - body sha256.

  Also record the thread's complete comment-id list and count, and the run record fields used: repository id, fork status, workflow path and content sha256, `head_sha`, and, after V2, the evaluated commits and the executed tool blobs (V3).
- (b) Add an offline replay mode. It recomputes `result.json` byte for byte from the committed snapshot plus git objects, with admission taken from the snapshot and marked `"admission": "replay"`. It is never acceptable as a new run, but it is an independent check of the committed result.
- (c) State plainly what remains host-attested: whether the snapshot's comments and run record were genuine at acceptance time. That rests on the acceptance-time check and its provenance, and is not reproducible offline.

6. The writer's four choices against the owner's provisional preferences

| Choice | v5.4 | Meets the preference? | Change needed |
|---|---|---|---|
| Authority path `tools/ledger_coverage/authority.json` | as stated | yes | none |
| Comment forms: exact, versioned, machine-readable, explicit plan and round | exact, with explicit plan and round, but **not versioned** and free-text in shape | partly | add a version token and a key=value shape (proposal below). Unknown versions refuse |
| Authority updates: independent review plus explicit owner approval verifiable like designations | review record plus a merge by the pinned id; the approval is not host-verified | no | point 3 |
| Owner identity: immutable numeric id; login for readability | numeric id 7273571 decides; the login is recorded | yes | none |

Proposed exact forms, for the owner's consideration: first line only, single spaces, LF-terminated (one trailing CR tolerated), 40-hex lowercase ids, sha256 lowercase hex.

- `oi-freeze/1 designate plan=<plan_id> round=<round_id> commit=<F>`
- `oi-freeze/1 withdraw plan=<plan_id> round=<round_id> commit=<F>`
- `oi-freeze/1 supersede plan=<plan_id> round=<round_id> commit=<F> by=<F2>`
- `oi-authority/1 approve from=<sha256 of the A replaced> to=<sha256 of the new A>`

Any owner comment whose first line begins with `oi-freeze/` or `oi-authority/` but does not match one of these exactly, or names an unknown version, refuses for the plan or authority thread it is in.

7. The authority-record format

The verdict is REVISE, so I give the format that v5.4 defines, followed by the fields the changes above add, so that the owner can see both. This is a proposal for display, not an approved record.

v5.4 defines `oi-tool-authority/1` at `tools/ledger_coverage/authority.json` with these fields:

- `owner` (numeric id 7273571; login `amaybaum` for readers);
- `repository` (numeric id 1156244443; full name `amaybaum/incompleteness`; not a fork);
- `workflow` (path, content sha256);
- `plans` (`plan_id`, authorized thread as repository id and issue number, allowed `round` ids, and the pin-table path);
- `forms` (the three first-line forms).

The proposed shape, with the changes of points 3, 5 and 6 marked `(added)`:

```json
{
 "schema": "oi-tool-authority/2",
 "owner": {"id": 7273571, "login": "amaybaum"},
 "repository": {"id": 1156244443, "full_name": "amaybaum/incompleteness", "fork": false},
 "workflow": {"path": "<.github/workflows/...>", "content_sha256": "<64-hex>",
              "tool_source": "head_sha tree; engine and adapter blobs verified against the pins (added, review V3)"},
 "engine_pins": {"<path>": "<blob sha256>"},
 "plans": [
  {"plan_id": "<id>", "thread": {"repository_id": 1156244443, "issue": <n>},
   "rounds": ["<round_id>"], "pin_table_path": "<path in F>"}
 ],
 "authority_thread": {"repository_id": 1156244443, "issue": <n>},
 "forms": {
  "version": 1,
  "designate": "oi-freeze/1 designate plan=<plan_id> round=<round_id> commit=<F>",
  "withdraw": "oi-freeze/1 withdraw plan=<plan_id> round=<round_id> commit=<F>",
  "supersede": "oi-freeze/1 supersede plan=<plan_id> round=<round_id> commit=<F> by=<F2>",
  "approve_authority": "oi-authority/1 approve from=<sha256> to=<sha256>",
  "first_line": "bytes up to the first LF; one trailing CR removed; no other normalization"
 },
 "supersedes": {"path": "tools/ledger_coverage/authority.json", "blob_sha256": "<64-hex> or null for the first record"}
}
```

These fields are additions to v5.4:

- `schema` version 2;
- `workflow.tool_source` and `engine_pins` (V3);
- `authority_thread` and `forms.approve_authority` (point 3);
- `forms.version` and the key=value forms (point 6);
- `forms.first_line` (V5);
- `supersedes` (the change chain).

The placeholders are values the owner's `A` must fix: the workflow path and content hash, the thread and issue numbers, the round ids and the engine pins.

8. Consolidated list of changes needed beyond review-v5.4's V1-V5

- C1. Authority changes approved by a host-verified owner approval comment in the versioned form, plus an independent review record; the merge by the pinned id is provenance only (point 3).
- C2. Versioned, key=value designation, withdrawal and supersession forms; unknown versions refuse (point 6).
- C3. An admission snapshot committed with the result, and an offline replay mode; what remains host-attested is stated (point 5).
- C4. The three stricter-than-P refusals stated with their justification, with (iii) named and controlled (point 1).

The authority record proposal is in point 7. The owner decisions listed in review-v5.4 remain open.
