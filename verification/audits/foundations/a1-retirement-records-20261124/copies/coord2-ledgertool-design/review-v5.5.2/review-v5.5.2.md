Final narrow confirmation of DESIGN-v5.5.2 (pre-freeze)

Verdict: ACCEPT

Reviewer: the independent, non-author session that wrote review-v5.5 and review-v5.5.1.

Limits kept:
- read-only;
- no repository, git or GitHub write;
- no workflow run and no host call;
- new files only under `D/review-v5.5.2/`.

Date 2026-11-23.

Inputs (sha256, verified; all match the coordinator's values)

- DESIGN-v5.5.2.md 835ff356200349db7689ea41ce936349015fb70f47b35a508945d681a8604323
- CHANGES-v5.5.2.md e5b3a2ab5420154ac5b6436927df330ee238aa3d0448f1b8b11bb24dfb2bcb3c
- Base: DESIGN-v5.5.1.md 8befd35c74b8e4dfa241e360d891de3222b3f878ca2aaf23ceaae1d00fbed649

Stopping rule as approved: a finding blocks only if it is demonstrated or reproducibly supported, and it violates an existing requirement or an agreed pass condition.

1. N3 is implemented correctly and completely

- **The bullet.** Sec. 6.3 "The freeze ledger" gains "Approval of each acceptance-time append (N3)". Every append, the acceptance landing's included, needs its own owner approval comment. The comment must:
  - be in the plan's authorized thread;
  - have the versioned first line `oi-freeze-ledger/1 append plan=<plan_id> round=<round_id> from=<sha256 before> to=<sha256 after>`, with single spaces and lowercase hex, and the first line defined as for the other forms;
  - be authored by numeric owner id `A.owner.id`;
  - be created before the merge.
- **Verification identical to a designation.** By host means:
  - the thread is read completely;
  - the comment is matched by its immutable id, author numeric id, creation time and edit status;
  - it must be never edited, have no edit history, and not be hidden.
- **Refusal.**
  - A malformed or unknown-version `oi-freeze-ledger/` line refuses.
  - Without a valid comment quoting exactly the before and after blob hashes, the append is refused and the landing does not merge.
  - A ledger on `main` carrying an unapproved append is unverifiable, so every later admission refuses (TR36).
- **TR47.** It covers each case separately:
  - no comment;
  - other ledger hashes;
  - another numeric id, even with the owner's login;
  - an edited comment;
  - a hidden comment;
  - a comment outside the thread;
  - a comment created after the merge;
  - a malformed or unknown-version line.

  The expectation follows from the bullet: the append is refused, the landing does not merge, and later admissions refuse.

Two notes, neither blocking:

- **Note A.** Admission point 3's edit-history check and point 4's parsing name the prefixes `oi-freeze/` and `oi-authority/`, which do not include `oi-freeze-ledger/`. I checked the two cases this could affect:
  - An approval comment later edited away from the form leaves its append without a verified approval. The ledger is then unverifiable and admission refuses: fail-closed.
  - A comment edited into the form fails N3's "no edit history" requirement.

  Neither yields an acceptance that should not happen. Adding `oi-freeze-ledger/` to point 3's prefix list would make the two lists consistent. Not blocking under the rule, since I found no counterexample.
- **Note B.** Because every admission re-verifies every append's approval, a later deletion of any approval comment makes all later admissions refuse. That is fail-safe, consistent with D1-D3, and the owner may simply note it.

2. The status section records D1-D4 accurately

As relayed to me by the coordinator:

- **D1:** the residual of a withdrawal created and deleted before any check observed it is accepted as a stated trust limitation, with no claim of complete protection.
- **D2:** the three stricter refusals (i) to (iii) are accepted, with the evidence that valid operations are not rejected.
- **D3:** the append-only freeze ledger is adopted, with N3.
- **D4:** the `authority.json` path, the versioned forms, independently reviewed and owner-approved authority changes, and numeric owner id 7273571 are adopted.

The status section also states that v5.5.1 is accepted and that v5.5.2 adds only N3 and is the frozen design. The decisions carry no comment ids, as before; that is a provenance gap, not a design defect.

3. The diff

`diff DESIGN-v5.5.1.md DESIGN-v5.5.2.md` has exactly 6 hunks:

1. the title;
2. the status bullets (frozen design; D1-D4);
3. the sec. 5 durable-evidence bullet;
4. the sec. 6.3 N3 bullet;
5. TR47;
6. the S13 list, from TR1-TR46 to TR1-TR47.

No rule, form, other control, count or pass condition changed.

4. The two consequential edits

- **The sec. 5 bullet** now says the observed events are appended "only with the append's own owner approval comment". It is necessary: without it, sec. 5 would describe an unconditioned append and contradict N3. It changes nothing else.
- **The S13 list,** TR1-TR46 to TR1-TR47. It is necessary: without it, S13's acceptance criterion would omit N3's control. It changes nothing else.

Findings

None blocking and none required. Optional: Note A (prefix list).

Not verified

- No implementation exists, and no host behaviour was exercised.
- The owner decisions are recorded without comment ids.

Files (D/review-v5.5.2/; MANIFEST.sha256 covers them)

- `review-v5.5.2.md`.
- `diff-v551-v552.txt`.
