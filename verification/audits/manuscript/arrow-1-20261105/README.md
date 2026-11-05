# ARROW-1 manuscript correction round (#1112)

**Status: WIP / UNVERIFIED.** Phase 1 (the theorem-recovery note, `RECOVERY.md`) is in
draft and has not been independently reviewed. No manuscript, book chapter, FULL mirror,
`.tex` or `.pdf` is changed on this branch until that review is complete.

## Scope

Issue #1112 asks whether any argument in the corpus derives a time asymmetry without
time-asymmetric initial or boundary conditions. The read-only analysis
([#1112 c.6643691865](https://github.com/amaybaum/incompleteness/issues/1112#issuecomment-6643691865))
and its independent verification
([#1112 c.6643840329](https://github.com/amaybaum/incompleteness/issues/1112#issuecomment-6643840329))
found that none does. This round applies the owner's decision (Option 3, split): it
separates what is proved under stated conditions from inherited boundary inputs and from
unresolved problems, and propagates the result corpus-wide under AGENTS.md §A.25.

- **Base:** `main` at `f5c281ae10a913ec68fa41b3b839ad0b164979cd`. All line locators in this
  directory are at that commit.
- **Branch:** `fix/arrow-1-20261105`. Designated writer: `writer-arrow`.
- **Underlying research question:** open. This round changes manuscript statements to
  match their support. It does not resolve whether OI explains the observed direction of
  time, and #1112 stays open.

## Authorization

Owner decision, recorded in
[#1112 c.6649271094](https://github.com/amaybaum/incompleteness/issues/1112#issuecomment-6649271094)
(amaybaum, Claude Code session chat, 2026-11-05). It approves the plan in c.6643840329 and
quotes the owner:

> Alignment: Before narrowing the claims, prepare the short theorem-recovery note
> identifying what a common alignment mechanism would need to establish. If no existing
> derivation survives review, mark alignment unresolved rather than refuted.

> Authorize one designated writer on a fresh branch for this manuscript correction round,
> under §A.25. First record the recovery analysis, then implement the supported edits with
> complete cross-document propagation, generated artifacts and mirrors. Obtain independent
> scientific and minimum-change reviews.
>
> No new physical premise, theorem promotion, computation, workflow dispatch or merge is
> authorized.

**Not authorized:** computation, Lean builds, workflow dispatch, new physical premises,
theorem promotion, merge, and changes to frozen records.

## Phases

1. **Phase 1 — recovery note (this checkpoint).** `RECOVERY.md`: the unproved claims quoted
   at the base, the strongest existing result for each, the target statement a proof would
   need, the remaining gap, the obstructions that bound any recovery, a verdict per claim,
   the horizon kinematics written out, and wording principles for Phase 2. Reviewed
   independently before any manuscript edit.
2. **Phase 2 — manuscript edits**, only after that review: the sites below, their FULL
   mirrors, the regenerated `.tex`/`.pdf`, and a change note mapping each edited passage to
   its finding. Independent scientific and minimum-change reviews run on the exact commit.

## Sites Phase 2 will touch

Taken from the plan in c.6643840329, as approved in c.6649271094. Book sites carry their
FULL mirrors (§A.14). Locators are at the base.

**(i) Retain a derived claim (expected unchanged, or conditions only restated where they
already are):** Main:744–756 (selection theorem); Main:758 (selection-rule content);
Substratum:56 (selection sentence); Substratum:409 ("§4.6 is symmetric; the direction is a
convention"); GR:797–805 (Theorem A.6 and "the generalized second law is open");
Explainer:924, 926–928; Complexity:206; Structure:717; ch02:194 (only the clause on no
independent past-hypothesis axiom being required to select where observers exist, with
(EM)); ch03:58 (the Boltzmann-brain exclusion); ch04:30–32; ch07:155–157.

**(ii) Conditional language, conditions named:**
- monotone clock (expanding branch, null energy condition; weak, constant in exact de
  Sitter; replace the ä > 0 criterion): Substratum:379, 405, and 409's "derives the
  existence of a monotonic parameter"; Main:760 (iii); ch02:192; Methodology:184's "from
  horizon growth";
- cosmological arrow (the expanding branch is an input, selected by no theorem):
  Substratum:407 (cosmological step); Explainer:932; Methodology:227;
- thermodynamic arrow (product or low-entropy preparation, plus the open identification of
  horizon area with entropy): Substratum:407 (thermodynamic step); Substratum:56's last
  sentence; GR:607;
- memory and measurement arrows (orientation convention and a non-stationary preparation):
  Substratum:407 (memory and measurement steps);
- "three projections" framing: Substratum:367, 371, 377; GR:32, 561, 709; SM:1366, 1592;
  ch02:176, 182, 184, 198; ch03:62, 202, 204;
- other: Substratum:401 (the confinement; remove the §A.33 history voice), 411 (citation),
  413 (list every dependency); GR:214 (energy orientation, not time direction); ch18:202
  (the trace-out alone gives no asymmetry).

**(iii) Describe an unresolved problem:**
- alignment of arrows: Substratum:401's "every arrow … descends" and 405's "all other
  arrows align"; ch02:196 ("four aligned arrows"); ch18:216;
- claims that the arrow is derived or the objection closed: Substratum:14, 26, 403, 409's
  "answers Ellis's objection", 415; Methodology:184's "none is concealed"; Explainer:930's
  sentence "You don't need to posit low initial entropy to explain why we see it"; ch03:58's "account of the arrow … follows from this exclusion"; ch02:194's
  thermodynamic-arrow and alignment content;
- Main:758's corollary title, retitled "Corollary (observer-selection rule, with its rate
  condition)" with the theorem and hypotheses preserved (see `RECOVERY.md` §F).
- Already correct as unresolved, expected unchanged: ch18:20, 204–214, 218–222, 328, 334;
  ch00:101; README:90; GR:805.

## Side corrections (owner, c.6649271094)

- ch18:208: detailed balance stated as $T_{ij}=T_{ji}$ for transition probabilities; the
  corpus result is reciprocity of transition counts, $T_{ij}=T_{\theta j,\theta i}$, under
  the counting hidden measure (SM Theorem 19; ch06:62).
- ch18:216: "the framework's structural conditions C1–C4 hold at the cosmological boundary";
  (C4) is a named realization condition there, not presently discharged (GR:52; ch07:12).
- GR:214: the kernel theorem `counting_passive` proves passivity *given* a monotone bath
  count `Ω`; the "arrow" there is an energy-sign orientation, not a time direction.
- GR:607: "non-decreasing from a product initial state" overstates Theorem A.6, which is a
  bound relative to $t=0$ holding at every $t$ in both directions.
- Substratum:407: the citation "[GR, §3]" for $\rho_s=\rho_{\rm crit}$; the identity is
  derived in GR §7.2 (GR:428–430), with its temperature input from GR §3.1.
- Substratum:411: "[Main, §1.3] already assumes a causal topology on the partition"; Main
  contains no such assumption.

## Files

- Allowed (c.6649271094): the passages above in `papers/{Substratum,GR,SM,Methodology,
  Explainer,Main}.md` (Main: the §4.6 corollary title and :760 only); `book/ch02`, `ch03`,
  `ch04`, `ch18` and their FULL mirrors; the regenerated `.tex`/`.pdf`; this directory.
- Not allowed: GR:260 and Main:590 (the separate #1029 unit); Lean modules; frozen records;
  every other passage.
- **Open question for the owner (found in Phase 1):** retitling the Main:758 corollary
  changes its identifier in `tools/proof_census.py` (the identifier is built from the
  parenthetical label), so `tools/coverage_check.py` would fail on
  `verification/coverage/LEDGER.json`'s entry `MAIN:C-past-hypothesis-replacement-rate-condition`
  unless that entry is renamed in the same commit. The ledger is a mutable gate file, not a
  frozen record, but it is not in the authorized file list. See `RECOVERY.md` §F.4.

## Contents

- `README.md` — this file.
- `RECOVERY.md` — the theorem-recovery note (Phase 1).

No computation was run and no Lean module was built for this record. Every argument in
`RECOVERY.md` is a paper derivation or a reading of the cited source, and is marked as such.
