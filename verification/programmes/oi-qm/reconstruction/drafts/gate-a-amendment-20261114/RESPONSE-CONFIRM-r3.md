# Response to CONFIRM-r3.md

Dispositions of the required changes in `CONFIRM-r3.md`, which reviewed `GATE-A-AMEND-r3.md` and
`OWNER-QUESTIONS-r3.md` at commit `65b0a9293c1eb15a56409f7d06d22734bb0378ec` (ACCEPT WITH CHANGES).
`r4:n` is line n of `GATE-A-AMEND-r4.md`; `OQ4:n` is line n of `OWNER-QUESTIONS-r4.md`; `EP:n` is
line n of `endpoints.md`, blob `d9d92e038a8022e854586101067ce4de9789fdf6` on `main` at `c3b5f37a`.
r4 is limited to these findings and is unreviewed. Every earlier file in the folder is unchanged
(checked by SHA-256 before and after writing r4).

Each change was checked against the r3 text it replaces and against EP, and its logic was worked by
hand, before it was applied.

| ID | Disposition | Where | Check and reason |
| --- | --- | --- | --- |
| RC1(a) | applied | r4:78–86 | Confirmed: r3 used "experiment family" both for the labelled law (C-law row) and for the complete family of admissible procedures (S-A). Fam(M) and ≃ are defined once in §2, with the restricted reading of owner question 4 stated. |
| RC1(b) | applied | r4:220–224 | Confirmed: r3 never said what "C(M)" means for a model. One meaning is fixed for S⇒, S-A, S⇐, S⇐ᴺ, S-J, B and C-1 to C-5. |
| RC1(c) | applied, modified | r4:228 | The reviewer's row is used, except for its last clause, which reads "an obligation on the admitted class, that is on E" where the review had "on E and 𝔄". S⇒ and S-A range over every member of `M(E, J_exact(A))` that satisfies C, and such a member need not be an instance of 𝔄 (the point of REVIEW-r1 F11). The rules of 𝔄 therefore cannot secure S-A for those members. Only the admission condition E can. |
| RC1(d) | applied | r4:279–280 | The reviewer's text is used. |
| RC1(e) | applied | r4:320–321 | The reviewer's text is used. |
| RC2(a) | applied | r4:295–309 | Confirmed that r3's "S⇐ implies S⇐ᴺ" held only for a C that is a function of p_M over the whole of `J_exact(A)`. The three logical claims of the new text were checked by hand. (i) From S⇐, C(M₀) and M₀ ≡ T; S-A then gives M₀ ≃ T; for any M′ ≃ T, invariance gives C(M′). (ii) For a C that is a function of p_M: M ≃ T and M′ ≃ T give M ≡ T ≡ M′, so the laws and the values of C are equal. (iii) S⇐ᴺ with I gives S⇐ only when the witness of I satisfies ≃, since the antecedent of S⇐ᴺ is ≃. The antecedent is changed from ≡ to ≃ as the review requires. |
| RC2(b) | applied | r4:229 | The reviewer's text is used. |
| RC2(c) | applied | r4:370–377 | The reviewer's text is used. The bullet's heading reads "the type and domain of C", matching §5.2. |
| RC2(d) | applied | r4:412–421 | The reviewer's items 1 and 2 are used verbatim. Items 3 and 4 are unchanged. |
| RC2(e) | applied | OQ4:6–13, OQ4:21–23 | The reviewer's two replacements are used verbatim. Two references in the file are updated because it describes r4: the title and details line name `GATE-A-AMEND-r4.md`, and "the reading taken in r3" reads "the reading taken in the amendment". The file is 46 lines. |
| RC3(a) | applied | r4:237–244 | Confirmed: three openings were not literally covered by r3's C-1, namely the instances of 𝔄, choice among candidate conditions, and thresholds derived from quantum theory. The reviewer's sentence is used verbatim. |
| RC3(b) | applied | r4:258–261 | Confirmed: r3 applied EP:102, EP:104 and EP:164 to C, but applied C-1 to C-3 to nothing in E, and R3 notes that a condition folded into E would meet EP:56–64. EP:102 already requires that E be "specified independently of equality to the quantum comparator's probabilities". The clause adds C-1's exclusions and C-2 and C-3 for conditions in E; it tightens the target and relaxes nothing in EP. |
| RC4 | applied | r4:323–327 | Confirmed: without membership in `M(E, J_Bell(A₁, A₂))`, B⇐ added nothing to S⇐, since the witness already matches T on `J_exact(A₁ × A₂)`. The reviewer's text is used. |

## Trace

No disposition of the contract changes. `GATE-A-AMEND-r3-TRACE.md` stands, and r4 cites it. No r4
trace file is written.

## Optional suggestions left unapplied

None of O1–O8 is applied. None is a factual correction inside the amendment text.

- **O1–O3** concern `README.md` and are for the coordinator.
- **O4** (OQ:10–11, "C can then be read physically"), **O5** (OQ:20, "only coverage is required"),
  **O6** (OQ:28–29, attribution of the quoted sentence to the proposal the owner accepted) and
  **O7** (OQ:37–39, "its author asks for") concern `OWNER-QUESTIONS-r3.md`. The same wording is
  carried into `OWNER-QUESTIONS-r4.md` at OQ4:15–16, OQ4:26, OQ4:34–35 and OQ4:43–45.
  O6 and O7 are points of attribution accuracy in an owner-facing file. I checked O7 at source:
  #1169 c.6703342848 reads "It requires both target coverage and a quantum counterpart for every
  behavior admitted by the physical OI interface", where "It" is the accepted Gate A contract, so
  "states that the accepted contract requires" is the exact form. The amendment text itself
  (r4, §8 item 4) says "the same comment states, in its author's words", which is accurate. Both
  can be applied to the owner-questions file on the coordinator's instruction.
- **O8** (I-2, an added clause on per-procedure dependence) is an addition, not a correction. The
  kept lines EP:75, EP:90 and EP:100 already require it.

## What was not checked

- The commit `65b0a929` and its checkout were not read. r4 was written from the r3 files in this
  folder, which the review reports as the files at that commit.
- No source outside this folder and EP was read again for this revision, apart from the
  #1169 c.6703342848 passage for O7, which was already held from the earlier reading.
