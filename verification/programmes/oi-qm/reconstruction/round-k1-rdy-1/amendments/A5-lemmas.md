# A5. Lemmas used by the base

**Governs:** base line 95 (the heading's parenthetical), the support of the statements at base lines 97–114, base
line 163 (its last sentence) and base lines 244–245 (the clause "The P1 lemma and the blindness lemma (CC-SCOPE)").

**Support.** Written proofs of the blindness lemma (lines 97–100), L-O(i) (lines 102–106) and L-O(ii) (lines 102–103,
107–110), for the statements as made, are in `verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md`
§2–§4, on `main` at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be`. "The P1 lemma" (line 244) is Lemma P1 of that file,
§1.1, whose parts (a)–(c) carry the uses at lines 72–76 and 244. Line 95's parenthetical is provenance.

**Review.** The independent review of those proofs is recorded in
`verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/REVIEW.md` at the same commit: PR #1119 comment
6651717259 (verdict ACCEPT WITH CHANGES on `1901063504f649bd453d7b5f87add395d6974ec7`) and the delta check, PR #1119
comment 6653737476, quoted there, with the changes applied in `d8bfd07bf591eeeeb107ef9842547dc53e195bef` and
`6525ad34b5fc4bd6f25c1c07de4482e35d69ec3c`. The review is model-authored and read-only.

**Provenance of the review.**

- *Statements reviewed.* At `1901063504f649bd453d7b5f87add395d6974ec7`: Lemma P1 as assembled in `LEMMAS.md` §1.1
  (parts (a)–(d); part (d) is not used by the base), the blindness lemma (§2, base lines 97–100), L-O(i) (§3, lines
  102–106) and L-O(ii) (§4, lines 102–103, 107–110). The review states that its changes are wording and locator fixes
  with no change to a statement or proof step, apart from one clause added to Lemma P1(c).
- *Changes and their check.* `d8bfd07bf591eeeeb107ef9842547dc53e195bef` applies the review's changes; the delta check of
  `d8bfd07b` accepts them with two count fixes, which `6525ad34b5fc4bd6f25c1c07de4482e35d69ec3c` applies, as the same
  reviewer's dated statement in that comment confirms. At `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` `LEMMAS.md` differs from
  `6525ad34` only in its five status lines (`022ae8da`, #1122).
- *Form of the record on `main`.* Comment 6651717259 is the coordinating session's condensed posting of the reviewer's
  delivered report, which the reviewer confirmed matches its verdicts and findings (PR #1119 comment 6653843874); it is
  not the reviewer's verbatim report. The delta check, comment 6653737476, is the reviewer's report word for word,
  except one paragraph omitted and marked in place, on which no verdict rests.

**Ruling.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656166518
(2026-11-05T10:54:11Z):

> **R5 — Internal independent review counts.** The existing independent, model-authored reviews of the lemmas on `main` satisfy A5's "pass review" condition **at the internal-verification level**, provided their provenance and exact reviewed statements are established. This ruling does not constitute external peer review, Lean verification, or proof that the physical assumptions follow from OI. CR-5 remains open. Explicitly distinguish the condensed #1119 posting from the reviewer's verbatim report, and record that the full `PROOFS.md` review was performed on an evidence branch.

With the provenance above, the condition quoted in §12 ("Interpretations that depend on a proof remain conditional
until those proofs pass review") is met for these statements at the internal-verification level only. That is not
external peer review, not Lean verification, and not proof that the physical assumptions follow from OI. CR-5 stays
open (A8). The provenance of the `PROOFS.md` review is recorded in A7.

**Line 163.** Its last sentence states G4's outcome for a B-pl member row. It applies subject to lines 182–184:
VOID[stage], Z1-VOID, a token issued by an earlier gate, or VOID[row] takes precedence over the BLIND it states. For a
sharply ready member, `NB` fails by the blindness lemma (`LEMMAS.md` §2.3).

**CC-SCOPE** (lines 208, 244–245). In B-pl the blindness lemma applies to `δ_0`; in B-eq and B-ct it applies to
`δ_0(· | W_{t_u} = 0) = δ_0`, the only positive-mass conditioning (`LEMMAS.md` §2.3).
