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
  and that no statement or proof step changes. Separately, it offered an optional addition to Lemma P1(c), the clause
  "hence `φ^k(supp μ) = supp μ` for all `k ∈ ℤ`", which the writer adopted; the delta check verified that clause and its
  proof clause (`k1-rdy-proofs-20261105/REVIEW.md`).
- *Changes and their check.* `d8bfd07bf591eeeeb107ef9842547dc53e195bef` applies the review's changes; the delta check of
  `d8bfd07b` accepts them with two count fixes, which `6525ad34b5fc4bd6f25c1c07de4482e35d69ec3c` applies, as the dated
  statement after the report in that comment confirms. Per `k1-rdy-proofs-20261105/REVIEW.md`, that statement condenses
  one the same reviewer wrote at posting time; it is not the reviewer's words verbatim. At `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` `LEMMAS.md` differs from
  `6525ad34` only in its five status lines (`022ae8da`, #1122).
- *Form of the record on `main`.* Comment 6651717259 is the coordinating session's condensed posting of the reviewer's
  delivered report, which the reviewer confirmed matches its verdicts and findings (PR #1119 comment 6653843874); it is
  not the reviewer's verbatim report. In comment 6653737476 only the text between its BEGIN and END markers is the
  reviewer's delta check word for word; the comment's header is the coordinating session's, and its dated statement
  after END is the condensation noted above. `REVIEW.md` quotes the comment with one paragraph of the report omitted and
  marked in place, on which no verdict rests.

**Provenance of the `PROOFS.md` review.**

- *Records.* §1–§6 of `verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/PROOFS.md` were
  reviewed at `06d6ab31f7f35d02c583e06ebf89317d28bd5b98` (#1114 comment 6653236579, ACCEPT WITH CHANGES), and §7 at
  `7c768f0590d96044eebf741834cb4e734ef61666` (#1114 comment 6653410073, the delta check, ACCEPT). Both commits are on
  the evidence branch `evidence/k1-rdy-pref-proofs-20261105`, off `main` (provenance). Between them §1–§6 are unchanged;
  §7 and one row of §0's table are added.
- *Landing.* The blob reviewed at `7c768f05`, `3801aba6c972668fec6ed73a9a01327691fc9018`, is the one landed in
  `022ae8da3b1d6dfc4e632034b07c2e55996abb47`; at `4b4b437cfff9dcf32c882251d1a4c3445ca9e8be` the file differs from it only in its two
  status lines. On `main` the review rests on `k1-rdy-pref-proofs-20261105/REVIEW.md` §1, a hand re-derivation of §1–§7
  in the exact-head review of the landing at `6ff20b91b869ea09d432d2ae54ca8fb46cd4aa0f` (verdict ACCEPT).
- *Statements reviewed.* §1, `E = {x_1, y_1, y_2}` and `W_eq = {x_1, y_1}` (base line 198); §2, Proposition CYC (156
  cycles, the counts by period, `φ^{10} = id`) and the short cycles; §3, P3's image at `t_0` (`Im_O`, index 8,
  `π_0(O) = 1/8`, `D(μ_O) = 3 log 2`; base lines 86–90); §4, Proposition IND and its uses at the instance (§4.3); §5,
  Proposition EN (a)–(c); §6, CR-1 to CR-4, CR-6 and the reading of "every weighting supported on `C`"; §7,
  Proposition LEDGER and its consequence for G4's VOID[row]. CR-5 was checked as stated, that the converse of CR-3 is
  not established; the converse stays open. The short cycles, IND's uses at the instance and the reading in §6 are
  re-derived in `REVIEW.md` §1.

**Ruling.** amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656166518
(2026-11-05T10:54:11Z):

> **R5 — Internal independent review counts.** The existing independent, model-authored reviews of the lemmas on `main` satisfy A5's "pass review" condition **at the internal-verification level**, provided their provenance and exact reviewed statements are established. This ruling does not constitute external peer review, Lean verification, or proof that the physical assumptions follow from OI. CR-5 remains open. Explicitly distinguish the condensed #1119 posting from the reviewer's verbatim report, and record that the full `PROOFS.md` review was performed on an evidence branch.

amaybaum, Claude Code session chat, 2026-11-05, recorded in #1031 comment 6656645169 (2026-11-05T11:18:22Z):

> F2: Approve the broad reading.
> My R5 ruling covers the independently reviewed propositions in both `LEMMAS.md` and `PROOFS.md`.
> The intent is to recognize the existing model-written reviews as internal verification, not to impose an additional verification requirement that the base procedure cannot satisfy.
> Please proceed as follows:
> 1. F1: Apply the reviewer's two wording corrections to A5.
> 2. F2: Add the recommended paragraph identifying precisely which `PROOFS.md` propositions were reviewed, their review records, and the corresponding commit hashes.
> 3. Scope: Internal verification applies only to statements actually covered by those reviews. Do not extend it to unreviewed claims.
> 4. CR-5: Remains open. Internal verification does not establish external or independent human validation.
> 5. Preservation: Do not alter mathematical statements, hypotheses, protected lines, or existing scientific conclusions.
> 6. Final checks: Obtain an independent delta review, re-read the A4 heads, and confirm all existing verification and preservation checks.
>
> Authorization: F1 and F2 are approved as a single control-plane revision.
> Gate F remains undesignated. Bring back the final reviewed head and exact-head verification results before proceeding to F.

With the provenance above and under both rulings, the condition quoted in §12 ("Interpretations that depend on a proof
remain conditional until those proofs pass review") is met at the internal-verification level for the statements
listed under "Statements reviewed" for `LEMMAS.md` and for `PROOFS.md`, and for no others: a claim those reviews did
not cover is outside the rulings. That is not external peer review, not external or independent human validation, not
Lean verification, and not proof that the physical assumptions follow from OI. CR-5 stays open (A8). No statement,
hypothesis or conclusion of the base or of the two proof files is changed.

**Line 163.** Its last sentence states G4's outcome for a B-pl member row. It applies subject to lines 182–184:
VOID[stage], Z1-VOID, a token issued by an earlier gate, or VOID[row] takes precedence over the BLIND it states. For a
sharply ready member, `NB` fails by the blindness lemma (`LEMMAS.md` §2.3).

**CC-SCOPE** (lines 208, 244–245). In B-pl the blindness lemma applies to `δ_0`; in B-eq and B-ct it applies to
`δ_0(· | W_{t_u} = 0) = δ_0`, the only positive-mass conditioning (`LEMMAS.md` §2.3).
