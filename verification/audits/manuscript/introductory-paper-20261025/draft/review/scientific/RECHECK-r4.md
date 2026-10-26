# Scientific confirmation re-check: Introduction draft, revision 4

- **Object:** `draft/Introduction-r4.md` at `ebd425c0` on #918, sha256 `5f9fdcc5…68f6` (verified).
- **Also read:** `draft/CHANGES-r4.md`.
- **Diff:** r3→r4 by `git -c gc.auto=0 -c maintenance.auto=false diff --no-index --word-diff`.
- **Commit scope:** the commit touches only the audit directory. The draft itself changes on 8
  lines: l.32, 114, 234, 241, 257, 289, 291 and 313.
- **Read-only.** No repository file was changed.

## Verdict: ACCEPT WITH NITS

Everything requested is applied correctly. The N3 departure is right. No claim changed strength.
One optional wording nit (N-a) is below.

## 1. T1, T2 and N1–N3

| Item | Result |
|---|---|
| T1 (l.234) | Verbatim: "the gravitational continuum limit of the substratum's spatial coupling graph". Correct per Main:22 and :394 |
| T2 (l.289, l.291) | "Unpublished research record, internally reviewed" is in both [BHa] and [BHb]. This is accurate: the BH-01 re-check gave ACCEPT at `df2ea6f5` and the BH-02 re-check gave ACCEPT at `ce7937d2`; both package READMEs say "not external validation or owner adoption" |
| N1 (l.114) | Verbatim: "[Main §1.3, the realization clause of (C4)]" |
| N2 (l.313) | The VERIFY now cites AUDIT r4 C4 [FT], Thm 1, p. 4, and says the body was not re-read for this draft. Accurate |
| N3 (l.241) | The departure is **correct**. My "proved on paper **and** checked …" would have said every §5 result is both proved and checked, which is false. The §5.1 enumeration counts (40,320 / 1,376; sixty; 32) are computations only; item F is exact interval arithmetic; C7 is exact algebra. C1, C2, C6(a) and C6(b) are written proofs, and C1 and C2 are also checked. "Each proved on paper or checked exhaustively at small size or by exact arithmetic" is accurate for every result |

## 2. The added Contributions sentence (l.32)

> "The black-hole results of §5 are reported from unpublished repository computations [BHa; BHb] whose novelty has not been established."

**Novelty clause: accurate.** AUDIT r4 leaves C16-S unclassified because no literature was
examined, and #917's records were not read (AUDIT:1397–1398). It classes the Page-time fraction
KNOWN (Page 2013), and BH-01 itself calls C2 "the remnant-capacity form of a known fact". So
"novelty has not been established" is the right status.

**Consistency with "claims no new theorem or physical result": consistent.** The sentence reports
results and claims no novelty for them.

**One imprecision.** "Computations" understates the records, which also contain written proofs:
BH-01's C1–C4 and BH-02's C1, C2, C4 and C6(a)–(b). It also sits slightly at odds with §6.5 item 4,
"each proved on paper or checked …". This is nit N-a.

## 3. The [BHa] entry (l.289)

The neutral, unquoted description "recovery from accessible records in finite reversible models" is
acceptable. The record's actual title, "BH-01 access audit, v1: report", carries a round name. The
description is faithful to the report's subject (REPORT.md "Answer to the question").

## 4. Nothing else changed claim strength

- **l.32.** The editorial rewording ("It presents … together, separates …, states …, and summarizes
  … within the scope stated in §5") keeps the same content and the same scope limit.
- **l.257.** The recipe moved from a code block to inline code. The text is identical.
- **No other text changed.** Theorems 1–4, §5's claims, the R11 and R12 markers, §6.5's
  non-claims, Appendix A and every other reference are unchanged.

## 5. Nit

**N-a (optional), l.32.** Replace "reported from unpublished repository computations [BHa; BHb]" with:
> reported from unpublished repository research records [BHa; BHb], with written proofs and exact or exhaustive checks,

so that the sentence matches §6.5 item 4.
