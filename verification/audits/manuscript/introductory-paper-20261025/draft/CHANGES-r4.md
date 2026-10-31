# Introduction draft, revision 4: changes

**Applies:**
- the scientific re-check `S/paper/sci-review/RECHECK-r3.md`;
- the editorial re-check `S/paper/ed-review/RECHECK-r3.md`.

Both re-checks concern r3 (`83313e2c…6a68`), which is kept unchanged. The output is `Introduction-r4.md`. Line numbers refer to r4. The r3→r4 diff touches 8 lines, and Appendix A is unchanged.

| Item | Status | r4 line |
|---|---|---|
| Sci T1, "the lattice" | Applied verbatim: "the gravitational continuum limit of the substratum's spatial coupling graph" | 234 |
| Sci T2, BH evidential status | Applied: "unpublished research record, internally reviewed" in [BHa] and [BHb] | 289, 291 |
| Sci N1, cite object | Applied: "[Main §1.3, the realization clause of (C4)]" | 114 |
| Sci N2, [Cal26] VERIFY | Reworded; still a VERIFY. The §2.2 sentence was taken from the v2 abstract. The novelty audit's literature study records v1 and v2 as read in full text, with the claim at Thm 1, p. 4 (AUDIT r4 C4, [FT]). The body was not re-read for this draft | 313 |
| Sci N3, §6.5 item 4 | **Applied with a deviation.** r4 reads: "the results of §5 concern finite toy models, each proved on paper or checked exhaustively at small size or by exact arithmetic". The suggested "proved on paper and checked …" would say every result is both proved and checked. The enumeration counts of §5.1 are computations only | 241 |
| Ed N-a, line 32 | Applied verbatim: "It presents the established mathematical results of OI together, separates …, states …, and summarizes … within the scope stated in §5." | 32 |
| Ed [SCI] / O-1, "no new … result" against §5 | Applied. The sentence added after the self-description reads: "The black-hole results of §5 are reported from unpublished repository computations [BHa; BHb] whose novelty has not been established." The §5 statements themselves are unchanged | 32 |
| Ed N-c, [BHa] title | Not verbatim: the record's actual title is "BH-01 access audit, v1: report" (`bh01_access_v1/REPORT.md`). The entry now describes the record neutrally and without quotation marks: "recovery from accessible records in finite reversible models". [BHb]'s quoted title is the descriptive part of its actual title, so it is kept | 289 |
| Ed N-d, code block split across pp. 12/13 | Applied as the reviewer suggested: the recipe is inline code in the sentence, not a block. There is no raw LaTeX, the text is unchanged, and it sets with 0 overfull lines. The whole Code section now begins on p. 13, so the split is gone | 257 |
| Title hyphenation | Unchanged; this is an owner item. **Correction to CHANGES-r3:** the `\hyphenation{Deterministic}` line suggested there is not a fix. Per the editorial re-check (§5), it removes the hyphen but leaves an 11.1 pt overfull title line. The editorial re-check lists the remaining options: (a) accept the hyphen; (b) a pandoc `%` title block, with no raw LaTeX but 16 pp and a departure from the sibling papers; (c) a raw line, accepting the overrun | 1 |

## Build and checks

- **Build:** 16 pp, 0 overfull boxes, 0 missing characters, median 2,554 characters per page.
- **Layout:** §1–§7 end on p. 12, so the main narrative is 12 pages, as in r3 and within the owner's 12–15. The Code section, Appendix A and the references take pp. 13–16, and p. 16 carries the last three references. The extra page comes from the T2 clauses, the added Contributions sentence and R2-1's longer wording. No qualification was cut to recover it.
- **Cosmetic:** the last line of §4's lead sentence, "(§4.3).", now falls at the top of p. 7.
- **`voice_check`, `claims_check` and `duplicate_check`:** OK, both on a fresh `git archive` of `687e885b` with r4 at `papers/Introduction.md` and in the #918 clone.
- **The editorial reviewer's `identcheck.py`, run on r4:** 28 Lean identifiers, 0 unresolved, 28 Appendix A line numbers with 0 mismatches.
- **§A.32/§A.33 scan of the changed lines:** no history voice, no first person, and no caps other than CHSH. The remaining hits are deliberate source-status wording: "novelty … not established" ([SCI]) and "internally reviewed" (T2, in the bibliography only).
