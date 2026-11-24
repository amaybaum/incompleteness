# DESIGN-v5.4: changes against DESIGN-v5.3

## Inputs

I verified each input's sha256 before use:

- `DESIGN-v5.3.md`: 3b24ac8e5e651a5a5651ace69d36112d29e1afe9388696f056631f1c59e7773d
- `review-v5.3/review-v5.3.md`: 20f2c0c3e867cecdbc161dee88df12973f64101acbb15ae1d8a31b6ba1b88b66
  (verdict REVISE: W1-W4, O2, O3)

Owner decisions of 2026-11-23 applied:

- the authority decisions D1-D5, called A-D1 to A-D5 in the design;
- the W1 parity decision;
- the addendum on the trust root of the authority record.

The work stayed paper-only. Nothing was written to the repository, git or GitHub, no workflow ran,
and the Stage 1 worktree was not touched. The one new script is `work-v54/parity.py`; it reads git
objects and P's verified blob. No safeguard was weakened: every change binds an input more tightly
or adds a refusal.

## 1. Corrections and decisions

| Item | DESIGN-v5.4 sections | What changed | How verified |
|---|---|---|---|
| W1 (parity, pass condition 2) and the owner's W1 decision | 6.1 ("What `old_step2` is", "Both units, fail-closed", "Measured on A1", controls); 10.4 S11-57a-b restated, S11-58a-h added; 14 | `(old_step2, new_step2)` is P's alternative version of an edit, not a second step. The tool selects as P's `variant()` does (the first pair whose `old` occurs exactly once) and checks uniqueness at `H` for every edit. It then applies the edits in list order against a running copy, as P's `check` and `apply_edits` do, and requires each splice to be exactly the selected pair at the replaced occurrence's byte offsets. Retained edits are identity with no splice. Anything else is ERROR. The per-edit items 5 and 6 still scan both pairs, as `static_new` does. S11-57a and b now describe two-variant edits whose unapplied variant adds "now" or "no longer"; (c) is kept. Regression controls cover: `H` with `old`; `old_step2` only; neither; both; `old` twice; both ambiguous; a splice for the wrong variant; a progressive loss | `work-v54/parity.py` implements the rule from the text, not from P, and compares it with P's own functions. **A1:** all 401 edits in order bind all 399 splices to `(old, new)` at their offsets; D032 and D039 are identity; P does not refuse; items 5 and 6 give 0/0/0 in both. **Regression and S11-57 cases:** selection, refusal and items 5 and 6 equal P's in every case. **Random enumeration:** 4000 cases, half with two variants and splices built from P's own application; 0 differences in items 5 and 6 and 0 in refusal. **Where the tool refuses and P does not:** a splice for the unselected variant, and one splice over two edits. P has no splice concept, so in both P's own per-edit result is still reproduced and recorded. I found no case where P and v5.4 differ on what P checks |
| A-D1 (owner identity) | 6.3 (authority record `A`, admission points 3 and 7); TR4, TR9, TR20 | The owner is the numeric id 7273571 pinned in `A` (login `amaybaum` recorded). It is never derived from the repository owner, the caller, the environment or the plan. Comments are matched by author numeric id; the login is never decisive | textual; controls |
| A-D2 (edited designation) | 6.3 point 4; TR11 | Any edit ever recorded (REST `updated_at`, GraphQL `lastEditedAt` and `userContentEdits`) permanently invalidates a designation, even if the text is restored. Hidden or unreadable edit status refuses | textual; controls. The host API semantics were not exercised |
| A-D3 (supersession and withdrawal) | 6.3 ("The forms", points 2, 3, 5); TR12, TR16-TR18, TR22 | Exact first-line forms for designate, withdraw and supersede, fixed in `A`. `plan_id` (with its authorized thread) and `round` are defined in `A`, not in `F`. The whole thread is read to its end, with the count checked against the host. Processing is ordered by creation time, then comment id. A conflicting, ambiguous or unverifiable state fails closed | textual; controls |
| A-D4 (repository and workflow) | 6.3 (authority record `A`, admission point 1); 5 (acceptance); TR14, TR15 | Only repository id 1156244443, not a fork. Only the workflow at `A.workflow.path` whose content at `head_sha` hashes to `A.workflow.sha256`. A name or path alone never counts. The tool and the consumer each check both from the host API | textual; controls |
| A-D5 and v5.3 review O3 (durable evidence) | 5 ("Durable evidence") | See "A-D5 in detail" below the table | textual |
| Required safeguards for A-D1 to A-D4 | 6.3 | See "Safeguards in detail" below the table | textual; TR1-TR27 |
| Owner addendum: trust root of `A` | 6.3 ("The trust root, without circularity", "Bootstrap order", "Changes between `F` and execution", "Residual trust assumptions") | See "Trust root in detail" below the table | textual; TR24-TR27 |
| W2-W4 (v5.3 review) | as A-D1 to A-D4 | The repository, run and form bindings the review asked for, with its refusal controls: TR14 (fork or other repository), TR15 (modified or same-named workflow), TR17 (wrong form), TR16 (wrong thread), TR18 (withdrawal), TR19 (deleted or hidden), TR12 (pagination), TR21 (API unavailable) | textual |
| O2 (sentence byte offset) | 6.2 | The offset, in the committed file, of the first byte of the sentence's first non-whitespace character | textual |

**A-D5 in detail.** Acceptance is recorded by landing on `main` in the authorized landing record.
The record commits the accepted `result.json` and its sha256, together with the inputs that verify
it without any CI artifact: the commits; the configuration, `A`, engine and workflow blob hashes;
the designation data; the command; and a byte-for-byte regeneration recipe. CI run metadata is
provenance only. Committing preserves a result and never makes an invalid run acceptable: the
predicate is re-checked from the committed data before merge.

**Safeguards in detail.**

- Authority comes from `A`, reviewed and owner-authorized, and landed before any freeze.
- The caller cannot override the owner id, repository id, forms, thread or workflow by any argument,
  environment value, configuration field or record in `F`. The retirement configuration cannot
  carry these fields.
- Comments are verified by immutable id, author numeric id, creation time and edit status.
- A change to `A` needs its own review and owner authorization and a merge by the owner id that the
  previous `A` pins.
- A copy of `A` in `F` never governs, and a differing copy refuses.

**Trust root in detail.** `A` does not authenticate itself, and its owner id is not the
authentication. The root is:

- the host's attestation of the run's repository, read from the host API by the tool and,
  separately, by the consumer, never from the run's output;
- `A`, read only from `main` of that attested repository through the host API, never from the
  caller, another ref, another repository or `F`;
- acceptance only by landing on `main` of the canonical repository. There the consumer reads `A`
  itself and requires the run's attested repository id to equal it, so a fork with its own `A`
  can never be accepted.

The order of trust is:

- **Bootstrap.** `A` lands through a reviewed, owner-authorized merge before any freeze. Its
  merged-by id is checked against `A.owner` as a consistency check only.
- **Later changes.** Each change must be a reviewed, authorized merge by the previous owner id.
- **Between `F` and execution.** `F` must contain `A`. If `main`'s `A` differs from `F`'s copy, the
  tool refuses unless every change between them is reviewed and authorized.

The design states its residual trust plainly:

- the host's API and attestations;
- the host's access control on `main`;
- the integrity of the first reviewed landing of `A`;
- the owner's account.

## 2. Refusal controls added or restated (sec. 10.4)

- **TR1-TR13:** kept, restated against `A`.
- **TR14-TR23 (owner's list and the review's W2-W4):**
  - fork or other repository (TR14);
  - modified or same-named workflow (TR15);
  - wrong thread (TR16);
  - wrong form, or a near form (TR17);
  - explicit withdrawal (TR18);
  - deleted or hidden comment (TR19);
  - right login, wrong id (TR20);
  - host API unavailable, a page error or a count mismatch (TR21);
  - conflicting designations (TR22);
  - a differing `A` in `F`, or a change to `A` merged by a non-owner (TR23).
- **Superseding comment:** on the first page and beyond it (TR12).
- **Edited, and edited then restored:** TR11.
- **Caller overrides of each pinned value** (owner id, repository id, forms, thread, workflow path,
  workflow hash), each by argument, environment value, configuration field and `F` record: TR9.
- **Trust-root addendum:** a caller-supplied configuration (TR24); `A` from another ref or
  repository (TR25); `A` changed after `F` without and with review (TR26); an `F` older than `A`
  (TR27).

## 3. Unchanged on purpose

Everything outside sec. 5, 6.1, 6.2 (the O2 sentence), 6.3 admission, 10.4 (TR, S11-57, S11-58),
14, 15 item 0a, 16.7 and 16.8's control list is unchanged from v5.3.

`diff DESIGN-v5.3.md DESIGN-v5.4.md` has 18 hunks; the document grows from 2533 to 2759 lines.

## 4. What I could not follow or verify

- **Host API semantics are assumed, not exercised.** No host call was made. These points are
  specified fail-closed and must be confirmed in CI:
  - that `updated_at`, `lastEditedAt` and `userContentEdits` reveal every edit;
  - how hidden or minimized comments are reported;
  - the thread comment count used for the pagination check;
  - a pull request's merged-by id;
  - fork status.
- **The bootstrap of `A` cannot be verified from `A`'s content.** The tool can only check its
  consistency (the merged-by id equals `A.owner`). Its integrity rests on the reviewed,
  owner-merged first landing, and the design names this as a residual trust assumption.
- **What I chose and you should confirm:**
  - the path `tools/ledger_coverage/authority.json`;
  - the exact A1 strings of the three forms;
  - that a change to `A` must be merged by the previous `A`'s owner id;
  - that a login mismatch with the right id is not by itself a refusal; the id decides.
- **The workflow hash and the thread are not yet known.** `A` does not exist, so the workflow path
  and content hash, the issue number of the plan's thread and the round ids are placeholders the
  owner's `A` will fix.
- **Committed `result.json` size.** The accepted result at T1' is about 1.26 MB, and sec. A.42
  item 4 prefers small committed artifacts. A-D5 decides it is committed. Whether to commit it
  compressed is left to the landing record's review.
- **S11-57c and S11-58g are refused by the tool's binding where P, which has no splices, does not
  refuse.** P's own per-edit result is reproduced in both. If the owner counts any refusal P lacks
  as a parity difference, these two are the only cases.
- **Comment ids.** None is held for any owner decision.
