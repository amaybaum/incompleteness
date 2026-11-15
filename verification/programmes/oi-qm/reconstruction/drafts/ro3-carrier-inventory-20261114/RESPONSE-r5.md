# RO-3: response to the independent review of inventory r5

**UNREVIEWED.** This file gives the writer's disposition of each item of the independent review of
r5 (delivered as `REVIEW-1303-INVENTORY-r5.md`, ACCEPT WITH CHANGES, no label refuted; SHA-256
`16b5d919d9a1b44cad60c55eaead6d258db8676bdc6316184f5de23445faa8d1`). The items are H1–H5, the minor
items H6 and H6′, and the completion of findings F6–F12 of the review of r4. r5 is left unchanged;
the changes are in `RO3-INVENTORY-r6.md`. Each item was checked at `main`
`7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac` with `git show 7ac74a4b:<path>`, and the governance
comments through the GitHub API, before it was applied. Paper-only: nothing was built or run, and
no repository, Issue or PR was written.

**Authorization.** The coordinator requested r6 after the review. No owner comment authorizing r6 by
name was found on #914, #1055, #1169 or #1303 after 2026-11-15T11:34Z. #1169 comment 6893687398
covers r5 and its independent review. r6 Standing records this for the owner to confirm.

Dispositions:
- **accepted**: applied as the review proposes;
- **accepted, modified**: applied with a stated difference;
- **noted**: no change needed.

Section numbers below refer to r6.

## H1. §7.3 and AM-5 misread Main:716

**Disposition: accepted.**
- **Checked.** Main:716: "the stochastic-quantum bridge (§3.1 and §3.2; two routes reach its
  transition-statistics layer ...)". Main:352: "The two routes agree on the configuration-transition
  probabilities". Main:356: "Both routes above are constructive". Main:354 places the in-house
  fixed-basis representation, by the permutation unitary of any realization, inside the
  framework's own results. Main:208: the §3.1 route rests on (T) and finite `C_V`.
- **Applied.** AM-5 and §7.3 say that Main:716's two routes are §3.1 and §3.2. The conclusion that a
  route avoiding A1 exists now rests on Main:354 and Main:60, with Main:208 for §3.1. r5's "§3.4
  route" citation of Main:716 is removed.

## H2. §7.3 leaves out a reading the source supports

**Disposition: accepted.**
- **Checked.** Main:60's sentence: "The physical reading of the characterization theorem — the
  identification of nature with a finite reversible substratum — is accordingly conditional on that
  representation choice, an empirically motivated reconstruction rather than a pure derivation; the
  law-level equivalence of §3.4 itself holds for every finite-horizon law." DEPENDENCY-AUDIT.md:282:
  "existence of finite representatives of finite visible laws; not a characterization of the actual
  infinite substrate".
- **Applied.**
  - §7.3 quotes both halves of Main:60 and presents three readings: the law-level equivalence, the
    §3.2 route, and the characterization theorem with its physical reading.
  - r5's "does not treat the §3.4 equivalence as conditional on A1" is narrowed to the law-level
    equivalence.
  - DEPENDENCY-AUDIT.md:282 is added to §7.3 and to the 1.6 row, with a pointer to AM-20.
  - The difference stays a finding for the owner.

## H3. Consumers the map did not list

**Disposition: accepted.** Each was read at source.
- **(a) Main:536 and its recurrence-time qualifier: new row AM-20.** It covers :536, :540, :733, :18,
  :80 item (2), :626, and Main:60's physical-reading sentence (the coordinator's item 2).
- **(b) Main:453 and :467: new row AM-21.** It also covers :445–449 and :502, and is cross-linked from
  AM-5 and AM-11.
- **(c) GR:58: new row AM-22.** It notes that DEPENDENCY-AUDIT.md:289 is probably the same item.
- **(d) Comp:100: new row AM-23.**
- **(e) Methodology.** Meth:156 is added to AM-15 and AM-3. Meth:339–369 is a new row, AM-24.
- **(f) Census 15 and 31 as consumers: new row AM-25.** It cites `obsTheory`
  (`SubstratumInterfaceAudit.lean:770`, Section E from :764) and `obsTheory_nonnegBounded`
  (`FrozenSourcing.lean:84`; the review's :83 is the docstring line).
- **(g) Census 53.** `cx3b_complex_not_A1` (`A6Instantiation.lean:512`) is recorded in §7.2. Census 49,
  `hexSubstratum_A1` (`HexLatticeGas.lean:312`), is in AM-16 as an instance that satisfies A1.
- **(h) The MR-1 preregistration: new row AM-26, context only.** The record cites "Main:62", which is
  Main:60 at this base.
- **(i) Mirrors.** GR:90 is added to AM-1 and GR:342 to AM-11.
- **§5 and §7.1.**
  - §5 now says that r5's search for "A1" used a trailing space, which misses "A1)". That is how
    Comp:100 was missed. §5 adds the review's phrases as whole-word searches and states how each
    group of hits was read.
  - §7's title and §7.1, and the Standing scope bullet, describe the map as bounded by the searches
    of §5, not as corpus-wide.
- **Also added by the writer, from the same searches.**
  - §7.2: Substratum's class-defining statements for A1–A6, and GR:260.
  - AM-17: `book/README.md:100` and `readers-guide.md:79`.

## H4. The D-CQ reading

**Disposition: accepted.** This is the coordinator's item 4.
- **Checked.**
  - #1169 c.6891338304, first-hand. It says: "C may lie inside Q (soundness), or C may intersect
    other subsets of OI with different properties. An intersection with stronger-than-quantum
    behaviour in experiments not yet performed would be a testable prediction, not a defect." It also
    says: "Excluding PR is no longer a goal."
  - Answer 4's last sentence (c.6876591512).
  - #914 c.6893722503 §3–§4.
- **Applied.**
  - **Standing.** The reading is marked [IR].
    - Amended by D-CQ: answer 2's soundness half, answer 4's first sentence, and the exclusion
      purpose of answer 4's last sentence.
    - Not amended by D-CQ's text: answer 4's second sentence and answer 3.
    - Open: whether the anti-selection part of access closure survives as a coverage and
      agreement-with-data condition. This is the proposal in #914 c.6893722503 §4.
  - **Corrections.**
    - r5's "makes the same point" sentence is removed. That sentence attributed a different
      clause to §4.
    - §3 of the #914 record is cited as agreeing with reading answers 2 and 4 as amended.
  - **Q13.** It quotes answer 4's last sentence verbatim and asks the owner to confirm the reading.

## H5. Label coverage

**Disposition: accepted.** This completes F6 and F7.
- **Full label applied** at:
  - §0 (the null-measure remark);
  - 1.2 G-fact;
  - 2.2 and 2.3 G-sub;
  - the §3 preservation-control bullets;
  - AM-1, AM-16 and AM-20;
  - Q3, which the review did not list.
- **§6.** The "Use here" cell of the OBL-RO3-2 row now lists:
  - 1.2 G-fact, 2.2, 2.3, 2.6;
  - §3 with its preservation controls;
  - Q3 and Q6;
  - AM-1, AM-2, AM-4, AM-8, AM-16 and AM-20.

## H6. AM-3: the hidden-sector injectivity prong

**Disposition: accepted.**
- **Checked.** Main:60's two prongs.
- **The review's [IR] countercontrol, checked on paper.** The doubling map preserves Lebesgue measure
  and is onto. It is 2-to-1 and its eventual image is the whole circle.
- **Applied.** AM-3 now records two things. Without A1, the hidden-sector prong is unsupported, as
  well as surjectivity. The infinite substitute, the natural extension, is a factor relation, not a
  restriction.

## H6′. AM-7: the coupling-graph hypothesis

**Disposition: accepted.** This is the coordinator's item 5.
- **Checked.**
  - `iterate_dependsOnlyOn_ball` (`RegionTower.lean:283`), with section variables at :246 and
    `CouplingGraph` at :254. The statement is for `Q`-valued `f`.
  - `site_iterate_dependsOnlyOn` (:297).
  - `FiniteRange` (`QuasilocalAlgebra.lean:919`).
  - `leapFiniteRange` (`SecondOrderDrive.lean:306`).
  - Posits (viii) and (xiii) (Main:724).
- **The review's countercontrol, checked on paper.** The map `φ(s) = s + 1_T(s)·(1, 1, …)` is a
  bijection. Each output is insensitive to every single other component, and no output is a function
  of finitely many components.
- **Applied.**
  - AM-7 states that the hypothesis is not derived without A1.
  - It sources the hypothesis to posits (xiii) and (viii), to GR:132 for I-deep, and to
    `FiniteRange` and `leapFiniteRange` in the kernel.
  - It states the `Q`-valued scope, and that I-meas lacks the hypothesis.
  - r5's "by definition" is removed.
  - The status reads "conditional[the coupling-graph hypothesis ...]".

## The review's §7: recommended first recovery target

**Disposition: accepted, as a recommendation only.** This is the coordinator's item 6.
- **Applied in §3.** AM-3 is recorded as the review's recommended first target, with:
  - two separately stated questions, Q-A and Q-B;
  - the first missing step of each;
  - the review's statement of skepticism;
  - controls and countercontrols fixed in advance;
  - what counts as recovery (Q-A), as a negative (Q-B) and as anything else.

  The infinite form of Theorem 24(iii) is recorded second.
- **Not chosen.** Choosing the target is the owner's decision. §3 says so, and no candidate is marked
  chosen.
- **Not proved here.** The outline of Q-A is the review's, including its use of the Lusin–Souslin
  theorem. It is recorded, not proved.

## Completion of F6–F12 of the review of r4

- **F6, F7.** Completed by H5.
- **F8–F11.** Completed by H1–H3 and H6, H6′.
- **F12.** Completed by H4.

## Goal link

**Applied.** The r6 header carries one line: "Priority item 2: the A1 dependence of the main
equivalence (§7.3)."

## Not applied

- **An OBL-RO3-2 r3.** It still needs its own authorization. The review accepts that.
- **No status changes.** No cell's status changes. No result is withdrawn, and no premise is adopted.
