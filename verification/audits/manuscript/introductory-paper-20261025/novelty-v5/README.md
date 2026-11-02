# Novelty and fidelity audit, revision 5

**Status: work-in-progress evidence record.** It is not approval to
publish the introductory paper, and no verdict in it is an established
result. For drafting it supersedes `../NOVELTY-AUDIT.md`, which stays
unchanged as the earlier, unreviewed record.

**Current revision: r4, read at `main` `52e2db40`.**
- The owner authorized r4's re-base and publication.
- It was re-checked (`review/RECHECK-r4.md`: ACCEPT WITH NITS), and its
  required items and nits are applied.

## Files

Every file is byte-identical to the object that was reviewed or written,
at the sha256 listed in `../SHA256SUMS`.

- `AUDIT.md`: the audit, r4.
- `AUDIT-r4-prerecheck.md`: r4 exactly as the re-check of r4 read it
  (sha256 `b896788700f4904719ebe101e3f10c119187a5d6acb6f8ad5fb6b7b77974a781`).
  `AUDIT.md` applies that re-check's R1, R2 and N1–N7, which it marked as
  needing no re-review.
- `AUDIT-r3.md`: r3, applying the re-check's nits.
- `AUDIT-r2.md`: r2, the object of the independent re-check.
- `AUDIT-r1.md`: r1, the object of the independent review.
- `CHANGES.md`: the change notes r1→r2, r2→r3 and r3→r4, the last with
  the re-check of r4 applied.
  - The re-check read it at r2, with sha256
    `73e53c6f5285e09e52a5c8786c71ce95923c4f0d2b895269acf0be9bc1771e36`.
  - r3 and r4 appended their sections.
- `CHANGES-r1.md`: the change note for r1.
- `review/REVIEW.md`: the independent review of r1. Verdict: BLOCK, on
  wording only.
- `review/RECHECK-r2.md`: the independent re-check of r2. Verdict: ACCEPT
  WITH NITS, with eight nits and none required.
- `review/RECHECK-r4.md`: the independent re-check of r4. Verdict: ACCEPT
  WITH NITS, with two required wording fixes and seven nits, all applied.

The records cite their working locations:
- `introaudit/novelty-v5/` is this directory;
- `revnov5/` is `review/`;
- `scratchpad/novelty5/repo` and `scratchpad/novelty6/repo` were clean
  clones of this repository, read at the commits the audit names.

## Not retained

- **The literature PDFs and their text extractions.** These are
  third-party documents.
  - r4's sources are listed in `AUDIT.md` §8, by URL and the sha256 of
    the file read, with the page and quoted passage relied on.
  - The literature studies' sources are identified in `AUDIT.md` §0 and §5.
- **The repository snapshots and page-search helpers.** The snapshots are
  reproducible with `git show` at the cited commits.

## What r4 changed

- **Re-base** to `52e2db40`, after #925, #926, #927, #928, #916 and #930.
  - For every fidelity note, `AUDIT.md` §4 records whether its site is
    fixed, changed or open, with the fixing commit.
  - **Fixed:** F6, F10, F12, F21, F22, F23, F24, F25, F27, F28.
  - **Changed, with part still open:** F3, F4, F5, F8.
  - **Open:** F7, F14–F20, F26.
  - **Kept separate:** F13.
  - **New, F28, now fixed:**
    - Introduced by #927: Main:332 credited [4] with the ancilla
      distinguishability characterization, without its bijective scope.
      The mirror at appendix-b:96 / FULL:5885 lacked the scope and pointed
      at §3.4.
    - #930 (merge `52e2db40`) attributes the characterization to [9] with
      the bijective scope, and scopes and re-points the mirror to §3.2.
    - #930 also cites [5] Eq. (15) at Main:606 for the XOR example.
  - **New, F29 (candidate for the owner):** the witness-horizon clause at
    glossary:39, FULL:6661 and GR:20, read literally, holds vacuously for
    Markov laws.
- **First-hand full-text reading** of the highest-priority pending
  literature (`AUDIT.md` §0.2 and §8).

## Status summary

- **Correct is not the same as original.**
  - A class in the audit concerns originality only.
  - Correctness is recorded separately: kernel, prose or probe.
  - A kernel proof is not evidence of originality, and a KNOWN class is
    not evidence against correctness (`AUDIT.md` §0.4 and §7).
- **The only novelty candidate is C8-R**, the two-sided rooted
  classification.
  - It is proved in the kernel for a finite visible alphabet.
  - Its originality is unverified. It is a candidate, not an established
    novelty claim, and it carries **no priority sentence**.
  - Its sufficiency half is an instance of the construction in Egri et
    al., Props. 16–18. Its necessity half is folklore.
  - The divisibility and revival literature (§5 P1.3) is now read.
  - Realization theory and automata (§5 P1.1–P1.2) were read only through
    open surveys. Their primary texts are unread (below).
- **The XOR example is known.**
  - The same process is Rivas–Huelga–Plenio 2014, Eq. (15), which is
    Main's own [5].
  - Capela et al. 2019 give a four-time parity version.
  - Doukas v3 App. A is concurrent.
  - Who first stated it is unverified.
- **C3 has full-text support** (Strasberg–García Díaz, Eq. (3)).
- **The divisibility credit** goes to Rivas–Huelga–Plenio 2014 Thm 2.4
  and Buscemi–Datta. Cohen et al. 1993 and Blackwell 1953 are unread and
  not needed.
- **C4 and C5 remain partially verified.**
  - C4's packaging part rests on one unread area, the quantum-comb
    realization theorem.
  - C5's rational clause has a full-text construction (Johnson–Dulmage–
    Mendelsohn 1960) but no located explicit statement.
- **Still PROVISIONAL:**
  - the "not located" parts of C1, C1′, C4, C5 and C8-D;
  - C9, C10, C11 and C16e (attribution only);
  - C13, C14 and C16c.
- **"Machine-checked"** covers only the kernel declarations. For C10 it
  covers only the joint law of history, present visible state and hidden
  state; the time-t reading is not formalized.
- **Recommended positioning:** a technical perspective or pedagogical
  review, not a research article (`AUDIT.md` §7).

## Primary texts not read, and why

| Reason | Works |
|---|---|
| Bot challenge | Blackwell 1953 (Project Euclid); van Kampen 1998 (SciELO) |
| Not attempted, same host as Blackwell's bot challenge | Feller 1959, Heller 1965 (Project Euclid) |
| HTTP 403 from the publisher | Cohen et al. 1993, Rabin 1963, Carlyle 1963 (ScienceDirect) |
| Paywall | Anderson 1999; Vidyasagar 2011; Davis 1961; Bennett 1973; Fine 1982; König 1916 |
| Books | Paz 1971; Kallenberg; Breuer–Petruccione; Parzen; van Kampen; Cover–Thomas |
| Not yet attempted | the quantum-comb realization theorem; BD's forward citations; #917's records |

## Manuscript defects recorded (`AUDIT.md` §4)

These are recorded here only. No manuscript is changed.

- **Open at `52e2db40`:**
  - F3: the $e^{-i\hat H}$ remark at Main:532;
  - F4: Main's title;
  - F5 and F26: Explainer:373;
  - F7: Main:580(4);
  - F14–F20: Main:210–220, :636 and reference [24];
  - the C12/C10-B conflation at Substratum:126;
  - F29 (candidate): the witness-horizon clause.
- **Fixed by #925–#927 and #930:** F6, F10, F12, F21–F25, F27, F28.
