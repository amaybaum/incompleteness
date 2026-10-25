# Novelty and fidelity audit, revision 5

**Status: work-in-progress evidence record.** This is not approval to
publish the introductory paper, and no verdict in it is an established
result. For drafting it supersedes `../NOVELTY-AUDIT.md`, which stays
unchanged as the earlier, unreviewed record.

## Files

Every file is byte-identical to the object that was reviewed or written,
at the sha256 listed in `../SHA256SUMS`.

- `AUDIT.md`: the audit, r3.
- `AUDIT-r2.md`: r2, the object of the independent re-check.
- `AUDIT-r1.md`: r1, the object of the independent review.
- `CHANGES.md`: the change notes r1→r2 and r2→r3. The re-check read it at
  r2, with sha256 `73e53c6f5285e09e52a5c8786c71ce95923c4f0d2b895269acf0be9bc1771e36`;
  r3 appended the r2→r3 section.
- `CHANGES-r1.md`: the change note for r1.
- `review/REVIEW.md`: the independent review of r1. Verdict: BLOCK, on
  wording only.
- `review/RECHECK-r2.md`: the independent re-check of r2. Verdict: ACCEPT
  WITH NITS, with eight nits and none required.

r3 applies those eight nits (Rc2:N1–N8) and changes no classification.
r3 has had no separate review.

The records cite their working locations. `introaudit/novelty-v5/` is this
directory. `revnov5/` is `review/`. `scratchpad/novelty5/repo` was a clean
clone of this repository, read at the commits the audit names.

## Not retained

- **The reviewers' text extractions of the cited literature.** These are
  third-party papers, identified in `AUDIT.md` §0 and §5 and available
  from their publishers or arXiv.
- **The repository snapshots and page-search helper under `revnov5/`.**
  The snapshots are reproducible with `git show` at the cited commits.

## Limitations stated in the audit

- **Source coverage.** A classification is KNOWN or PARTLY KNOWN only
  where the cited passage was read in full text. Everything else is
  PROVISIONAL:
  - the "not located" parts of C1, C1′, C4, C5 and C8-D;
  - C3, C9, C10, C11 and C16e;
  - C13, C14 and C16c;
  - the XOR example.

  Items tagged [secondary] or [from memory] are unverified. The reading
  still required is listed in §5.
- **Attribution.**
  - The only novelty candidate is C8-R, as a two-sided characterization,
    and its novelty is unverified. Its sufficiency half is an instance of
    the construction in Egri et al., Props. 16–18. Its necessity half is
    folklore.
  - The divisibility credit goes to Buscemi–Datta 2016 alone until Cohen
    et al. 1993 or Blackwell 1953 has been read.
  - The XOR example is known, with prior sources still to be read. Doukas
    v3 App. A gives the same example concurrently.
  - "Machine-checked" covers only the kernel declarations, and only for
    the joint law of history, present visible state and hidden state. The
    time-t reading is not formalized.
- **Recommended positioning:** a technical perspective or pedagogical
  review, not a research article (§7).

## Manuscript defects recorded (§4)

These are recorded here only. No manuscript is changed.

- **F14–F20:** Main:210–220, :636 and reference [24].
- **F21:** Main:332, and the book's Breuer–Laine–Piilo sites. The
  bibliography has no entry for that work, and ch01 uses numeric
  citations against an author-year bibliography.
- **F22:** "equivalent to information backflow" at Main:149, Explainer:148
  and ch01:101.
- **F23:** partition-relativity without the canonical-measure scope.
- **F24:** GR:20, "C1–C4 necessary as well as sufficient".
- **F25:** glossary:39 / FULL:6659.
- **F26:** Explainer:378.
- **F27:** `book/README.md:64`.

`AUDIT.md` §1 records which of these sites the draft PRs #925 and #926
change, as their status was when it was written.
