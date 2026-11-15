ACCEPT

# Focused confirmation review of COVERAGE-AUDIT-r4

This review is read-only and paper-only. `COVERAGE-AUDIT-r4.md` was confirmed byte-identical to its copy
on PR #1292 at `a68c7ba7` and compared with r3 by `diff`. Owner comment 6878781541 on #914 was read
through the API. No other file was written, no computation was run and nothing was posted.

## The four checks

**1. F-37 is on the unresolved list, and the count is 10: confirmed.**
- §10 lists F-37 and says that F-28's b₂₃ = 1 item is separate.
- The count is 10 at both places it appears: §2 ("**Unresolved findings:** 10") and §10 ("Ten
  findings remain unresolved").
- No stale "9" or "Nine" for unresolved findings remains in r4.

**2. The owner guidance is quoted verbatim, with author and time: confirmed.**
- The API returns author `amaybaum` and created time 2026-11-14T14:26:48Z, which match r4's header.
- The eleven quoted lines in r4's header are identical to the comment's quoted block, line for line.
- r4 identifies the comment's closing paragraph as recording text, which is correct.
- The paraphrase and the "record not supplied" note are removed.
- The §9 off-`main` row now cites the comment as provenance and authorization only.

This closes REVIEW-AUDIT-r2 N6 and REVIEW-AUDIT-r3 N4.

**3. Nits N2 and N3 are applied: confirmed.**
- **N2.** The SM-35 note cites SM:1229, "**Closed at Level 1 framework-essentially via the explicit
  theorem below**", beside SM:1257. It gives parts (b, γ₀) and (d) as Level 2, citing SM:1249 and :1253.
- **N3.** §6 now reads SM:1285–1286.

**4. Nothing else changed: confirmed.** The diff touches only:
- the title;
- the header, to name the r4 inputs and to replace the paraphrase with the quote;
- the §2 and §10 unresolved counts and the F-37 list item;
- the SM-35 note;
- the §6 location;
- the §9 row.

No table code, flag, count or class changed apart from these. The claim counts stay at 155: 50 C, 30 CB,
23 CM and 52 U, with O = 36 and T = 13.

## Remaining items

None. The verdict ACCEPT concerns the audit as a record of coverage findings. It adopts none of the
findings, proposed rows or classifications. The ledger author and the owner decide those separately
(condition 7 of #914 comment 6877871344).
