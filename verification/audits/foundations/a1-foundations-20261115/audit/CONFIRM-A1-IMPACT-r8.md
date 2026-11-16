# Focused confirmation of the A1 impact audit, r8

**Independent, non-author, paper-only, read-only.** Nothing in the repository was edited, committed or
pushed; no GitHub record was written; nothing was computed or built. This file is the only output.

- **Target.** `A1-IMPACT-AUDIT-r8.md`, sha256
  `f43261fea2b841392bfdafcd344113d01573b9963d430ed31320b79224e70b3d` (verified; 3583 lines). It was read
  by section and by search, not in full (see "Coverage" at the end).
- **Inputs.** `REVIEW-A1-IMPACT-r6.md` (findings F1–F22, its sections 2 and 11); `A1-IMPACT-AUDIT-r6.md`
  for the earlier wording of the questions; `EF-1-r6.md`, sha256
  `34f3ec8f019053cb0755cc089d94a91f45ef6c19ac354e763b5b8285e6fe6d9f` (verified; read only for its
  coherence class).
- **Base.** `main` at `bf89ba133ee9f2926a317e8af067ccaa862ce2db`. Papers, Lean source and the census
  registry were read at that commit by `git show`.
- **#1169.** Read through the GitHub connector: comments 6894872312, 6895032895, 6896070253, 6896252651,
  6896496410, 6896771264, 6896890693, 6896940222, 6897254631, 6897455387, 6897859755, 6897946443,
  6898395533, 6898613777 and 6898760764. The issue had 272 comments when read; 6898760764 is the last.
- **Governing direction** (adopted direction, c.6898395533; review text relayed and adopted by the owner,
  amaybaum, 2026-11-15, adoption recorded in c.6898760764): "Marking changed rows unreviewed is
  appropriate, but any change that materially alters a question's basis needs focused confirmation
  before that question is called decision-ready."
- **Three additions by the coordinator** (the coordinator's own instructions, not owner directions): a
  stricter bar for Q12; a check of how the downstream site lists are presented; attribution reported as
  two separate checks. They are answered in sections 8, 9 and 7.

"r8" below is the target. "This confirmation" marks a reading or a check made here; such readings are
unreviewed. Every correction is a recommendation to the author; none is applied.

## 1. Result

| Question | r8 marks it | Verdict | Corrections | Rows and texts checked here at `main` |
|---|---|---|---|---|
| Q11 | needs confirmation | CONFIRMED WITH CORRECTION | E11 | AM-21.1 (Main:453, :469; GR:132; Sub:262), AM-23.2 (§12.3 cell against F6) |
| Q1 | needs confirmation | CONFIRMED WITH CORRECTION | E12 | AM-22 (GR:58, :68, :70), AM-31 (SM:1376–1382; Main:506–512), AM-36 (cell only); Main:700; GR:787, :795; GR:90, :665 |
| Q8 | needs confirmation | CONFIRMED WITH CORRECTION | E13, E14, E15 | AM-7.1, AM-7.2, AM-7.3 (Main:362–386, :414, :724 (ix), (xiii), (xiv); `RegionTower.lean:250–304`; `SecondOrderDrive.lean:306`; `SecondOrderLayer.lean:208`), AM-23.2 |
| Q6 | needs confirmation | CONFIRMED WITH CORRECTION | E15, E16, E17, E18 | AM-21.1, AM-22, AM-31, AM-4.4 (SM:334); Main:54, :58, :516, :724 (iv); Sub:262; GR:132 |
| Q5 | needs confirmation | CONFIRMED (decision-ready) | none (see E3 for P10, in Q12) | AM-22, AM-30 (SM:643), AM-33.1 (GR:791; `SubstratumInterfaceAudit.lean:106`); Main:60, :724 (iii) |
| Q9 | needs confirmation | CONFIRMED (decision-ready) | none | AM-6.2, AM-9.2 (§12.3 cells, §12.4; Main:216, :558, :600) |
| Q3 | needs confirmation | CONFIRMED WITH CORRECTION | E19, E33 | AM-11 (Sub:137, :157, :167; Sub:98); N-3 (`ch09-universality.md:104`, :106) |
| Q2 | needs confirmation | CONFIRMED WITH CORRECTION; option (b) stays not decision-ready until the destinations of §12.2 are agreed (adopted direction, c.6896890693) | E20, E21, E22, E23, E29 | AM-5b (Main:290–324), AM-4.2 (cell only), AM-1.1 (cell only) |
| Q13 | needs confirmation | CONFIRMED WITH CORRECTION | E24, E25 | AM-5b (Main:312, :314; census family 1), AM-30 (SM:643; `Reciprocity.lean:129`) |
| Q14 | needs confirmation | CONFIRMED WITH CORRECTION | E26 | the records of AM-18, AM-26, AM-35 (files and cited lines; receipts, seals and the legacy manifest searched) |
| Q12 | needs confirmation | CONFIRMED WITH CORRECTION | E1 to E7 | AM-7.2, AM-7.3, AM-21.1, AM-22; §14 (P1 to P16), the gate tally |
| Q7 | ready | basis untouched by r7 and r8; one error in r8's text of option (b) | E27 | Main:742–758; AM-8 item 3; §12.2 |
| Q10 | ready | basis untouched | none | `ch18-beyond.md:168`, :172, :244, :290; N-1 |
| Q4 | ready | basis untouched | E33 (wording of the site counts) | Main:724; the by-number and by-name sites (searched) |
| Q15 | ready | basis untouched | none | Main:638; §10 family 40 |

"Decision-ready" here means only that the question's text, options, basis and dependencies were checked
and stand, with the listed corrections applied. It does not mean that any recovery route was verified.
No route or direct-proof target was verified here. All fifteen questions remain pending.

Counts: confirmed 2 (Q5, Q9); confirmed with correction 9 (Q11, Q1, Q8, Q6, Q3, Q2, Q13, Q14, Q12);
not confirmed 0. Of the four marked ready, the basis of each is untouched; Q7 needs one correction of
r8's option text.

## 2. The rule for FIRM

**Stated once, in the adopted terms.** Yes. §0 quotes the rule exactly (compared with c.6898395533):
“"Firm" needs one consistent rule: all premises required by the proposed route are already available. It
still means neither that the route works nor that recovery is proved. Keep replacement separate.” §14.4
no longer redefines it.

**Premises of the four FIRM rows, each location read at `main`.**

| Row | Premises r8 lists | Found at `main` |
|---|---|---|
| AM-2.1 | Lemma 1 (Main:46); a finite realization with a root-independent prior (Main:516); diagonal preservation (Main:326–328; `isDiag_Phi`, `EquivalenceChain.lean:253`); the argument of Main:332 | all four as cited. `isDiag_Phi` takes any `μ : H → ℂ`. The theorem's own hypothesis, P-indivisibility of the population process (Main:330), is not in §14.1's list and should be (E10) |
| AM-5 | Lemma 1 (Main:46); the finite-horizon realization (Main:97, :516); the kernel channel with a general hidden weight (`EquivalenceChain.lean:241–253`) | as cited; `Phi` is defined at :242 with `μ : H → ℂ` |
| AM-31 | Theorem 22's graph hypothesis (SM:1376); C1 proved without finiteness (SM:1378); the bound of Main:506–512; Lemma 1 (Main:46) | as cited. SM:1382's use of `N − ∣V∣ ≥ 2N/3` is the C3 step, which for a hidden sector of undetermined cardinality is a floor that holds vacuously when the sector is infinite, as r8 says |
| N-6 | a ledger disposition (Main:724) | as cited |

**Uniform application.** Not fully. Two tests are in use, and §0 states one of them:

1. *Worded on `main`.* §0: a premise is available when it is on `main` as a theorem, a kernel
   statement, a posit in force "or a hypothesis already named in the statement being recovered".
2. *Needed of nature.* AM-4.4 is classed NEW although its measure hypothesis is named in the statement
   being recovered (SM:334: "extensions of the rule whose dynamics, measure and observer $\sigma$-algebra
   are equivariant"). It is NEW only because asserting the result of nature needs that measure to be
   nature's. That is the review's "rule of application" (its F5), which §0 does not state.

r8 in fact requires both: FIRM only if nothing further is needed of nature and every hypothesis the
restated statement carries is worded on `main`. AM-4.4 fails the second test in r8's reading of nature;
AM-7.2 and AM-7.3 fail the first test only. That conjunction is consistent, but it must be written
(E8). Also, AM-7.2 and AM-7.3 do not meet §0's definition of CONTINGENT ("an undecided reading of a text
on `main`"): r8's own CONTINGENT table says "neither added hypothesis is worded on `main`", and no
option of Q8 as worded for nature's carrier decides whether a statement about completions may carry
them. If r8's class is kept, the definition needs a second clause (E9).

**The three disputed rows: are both positions shown fairly?**

- *AM-7.2, AM-7.3.* Fairly, with two additions. (i) The review's own words that P4 "is not premise-free"
  and that the comparison of routes is "undetermined until P4 is written" (its section 11, item 5)
  belong beside its count; r8 has them in §20 item 5 and not in §14.1. (ii) The side that reads the rows
  as FIRM has one fact r8 does not put in the dispute: the dependency-sense coupling graph is on `main`
  as the hypothesis of the kernel cone lemma (`CouplingGraph`, `RegionTower.lean:254–256`;
  `iterate_dependsOnlyOn_ball`, :283, for a site type of any cardinality), which r8 cites under AM-7.1.
- *AM-21.1.* Overstated as a dispute. The review's proposed rule of application (F5: "A row is classed
  by what is needed to assert its result of nature") gives NEW for AM-21.1, as r8 does. Its figure
  7, 3, 8, 1 is r6's count with AM-31 moved (its section 11, item 1), not a count under that rule.
  Under the review's two remedies together (F5's rule and F7) the counts are 6, 3, 9, 1, and the only
  rows on which r8 and the review differ are AM-7.2 and AM-7.3 (E28).

**This confirmation's own classification (a recommendation; the owner decides).**

| Row | Recommended class | Reasons |
|---|---|---|
| AM-21.1 | NEW; conditional theorem available (as r8) | The row lands as a statement about nature's hidden conditional laws. On `main` the theorem is stated for a model with its own prior ("Model one coupling step as the uniform-prior bijection marginal of §3.2's construction", Main:453; the persistence form, Main:469). Said of nature it needs a joint law of record and hidden state, which `main` has only as the hypothesis of conditionals (GR:132, "given a normalized product prior on it"; Sub:262). The conditional theorem needs only Lemma 1 and standard inequalities |
| AM-7.2 | FIRM, with the scope of the excluded class stated | (a) The row lands NC: it excludes a class of completions and asserts nothing of nature, before and after the restatement. (b) The cone lemma for a dependency-sense graph on a carrier of any cardinality is a kernel statement on `main` (`RegionTower.lean:254–283`), so reading hypothesis (iii) with that graph uses a hypothesis already named on `main`, though not in the prose of Main:362–386. (c) Measurable response functions are a condition for the statement's own objects to exist: the theorem names `p(Ω)` and `P(q,r∣a,b)` (Main:372–378), and outcome probabilities are defined only if the events `{q_a = q, r_b = r}` are measurable; from those, each `q_a` and `r_b` is measurable. [This confirmation's reading; one line; not on `main`; unreviewed.] (d) No ledger item and no option of Q8 changes whether the Bell statement must carry the two hypotheses. What the restatement costs is scope, not a premise: the class excluded is the class of completions with a dependency-sense graph and defined outcome probabilities, and the row must say so |
| AM-7.3 | FIRM, with the same scope note | The cone is the kernel's by construction (`leapFiniteRange`, `SecondOrderDrive.lean:306`; `gateRegion`, `SecondOrderLayer.lean:208`), for a site type of any cardinality. Only point (c) above remains, and measurement independence is a hypothesis of the corollary as stated (Main:414) |

On this recommendation the counts are FIRM 6 (AM-2.1, AM-5, AM-7.2, AM-7.3, AM-31, N-6), CONTINGENT 3
(AM-7.1, AM-23.2, AM-33.1), NEW 9, replacement candidate 1; 6 + 3 + 9 + 1 = 19. r8's 4, 5, 9, 1 is the
stricter application, in which any hypothesis that the restated statement must carry and that is not
worded on `main` defeats FIRM. Both are consistent rules. The adopted words do not choose between them,
since they turn on whether a hypothesis that only narrows the class a no-go excludes is a "premise
required by the proposed route". The range the owner should see is FIRM 4 to 6, with AM-7.2 and AM-7.3
the only rows that move. Limit of this recommendation: point (c) is an argument made here and checked by
no one, and P4 has not been written.

## 3. Q5 and Q6 against Q12 (F2)

The contradiction found in F2 is gone. Q5 and Q6 each separate what may be proved conditionally from
what may be asserted of nature; Q12's second stage proves P6 in its conditional form and no longer
lists AM-22; the gate tally of §14.3 makes the same split; §12.4 concedes the rows as conditional. No
sentence of the kind "cannot proceed" or "are unavailable" remains for P5b, P6, P10 or P13.

Three loose ends of the same kind remain, none a contradiction. Each has an exact edit.

- P10. Q12 says the conditional form of P10 "is what this stage proves", but AM-33.1 is in neither
  group of that stage and has no direct-proof target in §12.3 (E3).
- Part (3) of P9. The gate tally says it "needs Q6(d) only", while Q6 and Q12 have it proved as a
  conditional theorem under (e) without (d) (E5).
- P5a. Q6's paragraph "What each choice allows" does not say what Q6 does for AM-21.1, although r8
  names that row's move to NEW as material to Q6 (E17).

## 4. Row AM-5b (Main:290–324)

Every line the row cites was read at `main` and matches: Main:60 ("by the finite hidden space of the
§3.2 setup"), :266, :280–282, :292, :304, :310 ("With the hidden input uniform"), :312, :316 ("the
hidden sector initially uncorrelated and maximally mixed"), :318, :322 ("the criterion carries no
dependence on $|H|$"), :324 ("All of this concerns the realization displayed above").

| Column | r8 | Finding |
|---|---|---|
| Category | RM | Stands. The passage states properties of one displayed realization's one-step channel, and Main:324 says so |
| Reason | (i) | Stands: A1 enters through the finite `C_H` and `ρ_H = I_m/m` of the §3.2 channel (Main:266, :280) |
| Lands as; class | not applicable; none | Stand |
| Q2 subset | the 18th | Stands |
| Observable conclusion about a finite experiment | no | Stands as this audit's entry. EF-1 r6's second §4.2 table has "**Partly.**" for the same class. That difference is not among T22–T31 (E29) |
| Concession | FM | Stands |
| Window confinement | yes, for one step | Stands; agrees with EF-1 r6 |
| Census | "unclassified", witnesses "not located" | **Correctable.** Main:314 names the witnesses: `entanglementBreaking_twirl`, `not_entanglementBreaking_twirl`, `exists_lagrangian_tuple` (`WeylLift.lean:652`, :781, :361), `isotropic_iff_commute` (`WeylTwirl.lean:263`), `separable_imp_ppt` (`Separability.lean:199`). The registry carries them in family 1, with the Main anchors "separability threshold" (Main:312) and `` `entanglementBreaking_twirl` `` (Main:314). r8's own §10 lists Main:312 and :314 among family 1's anchors and omits AM-5b from that row (E24, E25) |
| Treatment | RM; stays in Main §3.2 | Stands, with three corrections below |

Three corrections to the row's treatment.

1. *The threshold Theorem is A1-free.* Main:312 is a statement about abelian subgroups of the Weyl group
   on `s` qubits. It uses no hidden sector. A1 enters only Lemma 2 (iii) and the two Corollaries, through
   the uniform hidden input. The row and Q2(b) should say that the Theorem stays as it is under every
   option, since Q2(b)'s rule for kernel-checked statements would otherwise reach it (E21, E22).
2. *The hypothesis is not restated by a placement option.* §12.1 (row 57) and Q2(b) say the hypothesis
   is "restated as a uniform law on the hidden boundary sites, uncorrelated with the visible input". That
   is a different statement with no proof on `main`; the row's own item 3 calls it "a candidate [IR],
   with no recovery credit". Q2 changes placement only. The restatement is not part of option (b) (E20,
   E21).
3. *What P1 forces here.* Lemma 2's statement (Main:304–308) and Corollary 2 (Main:318) do not state the
   uniform hidden input; they inherit it from Main:280. Only Corollary 1 (Main:316) states it. If P1
   replaces `I_m/m` by `diag μ_H` at Main:280, the hypothesis has to be written into those two
   statements. The row's item 5 says the results "keep the uniform hidden state as their stated
   hypothesis", which is true of Corollary 1 only (E23).

The headline sentence that AM-5b "does not establish one either" is supported: Main:324 says that
non-entanglement-breaking "is a statement about a single channel, not about quantum mechanics".

## 5. Arithmetic

Recounted by script from the table cells, not from the prose.

| Table | Stated | Recount |
|---|---|---|
| §12 summary (57 lines, 10 cells each) | categories 2 + 1 + 4 + 3 + 18 + 16 + 10 + 3 = 57 | RD 2, TD 1, RU 4, RW 3, RM 18, RC 16, RX 10, OP 3; 57 |
| §12, reasons | 48 + 6 + 3 | 48, 6, 3 |
| §12, classes | 4 + 5 + 9 + 1 = 19; 38 with no class | 4, 5, 9, 1; 38 |
| §12.1 (57 lines) | Q2 subset 18; 39 not reached | 18; 39; the 5 + 7 + 1 + 1 + 3 = 17 of Q2(b) match the cells, and AM-5b |
| §12.3 (57 lines) | yes 11, partly 13, no 33 | 11, 13, 33 |
| §12.3, concessions | 23 + 5 + 13 + 4 + 12 = 57 | FM 23, RT 5, CD 13, removed 4, none 12; the lists of §12.4 match the cells |
| §14.1 | 16 RC = 3 + 5 + 8; 3 OP = 1 + 1 + 1; cross-tabulation 7 = 1 + 4 + 1 + 1, 12 = 3 + 1 + 8 | as stated |
| §14.3, Table 5 | 21 lines; 38 rows = 17 + 5 + 10 + 6; 38 + 19 = 57 | as stated |
| §14.4 | 8 lines; 11 rows | as stated |
| §21 | 46 + 11 = 57; 17 changed and 29 unchanged of the 46; 29 + 9 = 38 | as stated |
| §18 | 18 + 10 + 10 + 19 = 57; 4, 5, 9, 1; 23, 5, 13, 4, 12 | as stated |
| §22, response table | F1 to F22 | 22 lines |

The coverage denominator is 57 in §21 and §18. **One stale total:** §14.1, "Population.": "The other 37
rows have no class." It is 38 (E30).

## 6. The response table (F1–F22)

All 22 findings have a visible disposition. Checked against the text: F3, F4, F6, F7, F11, F12, F13,
F14, F16, F17, F18, F19, F20, F22 are applied as the table says. Two entries overstate.

- **F15** ("applied; summary rewritten"). The three inexact sentences survive in shorter form (E31): §18
  still says "57 results that the papers tie to the whole world being finite (A1)", though six rows hold
  without A1 and AM-3.1 assumes no size; "10 are kept as statements or rewordings" does not say that one
  rewording changes the falsifiability sentence; "4 are firm" does not say that one of the four is the
  ledger entry, for which there is nothing to prove.
- **F9** ("AM-5b has a value in every column, 'unclassified' for its census entry only"). §10 has no
  line for AM-5b at all (E25).

Three dispositions carry an attribution that r8's own correction retired: "applied; a substantive
correction (owner)" (F2), "applied by the owner's rule" (F5), "applied as a row (owner)" (F9) (E32).

## 7. Attribution

**(i) Accuracy of the quotations.** Every quotation in Standing from the thirteen comments was compared
with the comment on GitHub by reading, including the marks inside the three sentences r8 says it
corrected and the dashes in c.6896771264 and c.6898395533. None differs. The quoted strings elsewhere
in r8 that stand beside a comment id were compared with Standing by script (36 strings). Of these, 28 are
substrings of Standing's text. Four more are quotations that Standing does not carry, and were compared
with the comment directly: the rule for FIRM in §0, "But two shortcuts would be unjustified:" and two
cells of the table of c.6897946443. The other four are not quotations from a comment (r8's own phrase
"recovery not proved", one sentence of r5 and two of EF-1). The comparison with GitHub was by reading,
not by a byte-for-byte tool; a difference in an invisible character would not have been caught.

**(ii) Accuracy of the record of adoption.** Comment 6898760764 was read. The owner's words in it are
"Relayed, and I adopt them." It lists ten comments: 6896252651, 6896496410, 6896771264, 6896890693,
6896940222, 6897254631, 6897455387, 6897859755, 6897946443, 6898395533, and says the same holds for the
pilot recommendation quoted in 6898613777. r8 labels as adopted direction exactly those ten. It keeps
6894872312, 6895032895 and 6896070253 as the owner's own words, which 6898760764 also states, and in
6896070253 it attributes the proposal to the coordinator and the acceptance to the owner, as the comment
does. From 6898613777 it quotes only the owner's own words and labels none of the pilot text as adopted.
r8 labels as adopted no relayed text outside that record. No comment later than 6898760764 exists on the
issue, and r8 cites no relayed text sent after it.

Two points for the coordinator's judgment, neither an error of r8.

- 6898760764 speaks of "the quotations in the comments listed". The table of 6896940222 and the table of
  6897946443 stand outside the quotation marks in those comments. r8 treats both as part of the adopted
  text ("the adopted table"). For 6897946443 that is the natural reading, since the quoted sentence
  before the table ends with a colon. The record does not say it in terms.
- The sentence "a recovery candidate is not a recovered result" is recorded in 6897859755 as "an owner
  sentence from earlier in the same session". r8 treats it as adopted direction on the strength of
  6898760764's statement about the quotations of that comment. That is consistent with the record.

**Leftover attributions to the owner** (E32): the header's "only to quote the owner; twelve are quoted";
§0, "are not the owner's"; the heading of §1 and its line "C10 (owner records)"; the three dispositions
named in section 6.

## 8. Q12: what is inconsistent, and the edit

The reason "the first tranche needs no premise and no reading" is false of two of its five units as r8
now stands, and Q12 schedules one proof twice.

1. P4. §14 lists two "Premises added" for the measurable-`Ω` route and says "neither is on `main` as
   worded". §14.1 classes AM-7.2 and AM-7.3 CONTINGENT on "a reading the owner decides (Q8)". So on
   r8's own classification P4 needs two hypotheses and a reading. Yet P4's gate is "—" in §12 and §14,
   and Q12(b) calls the tranche "the units that wait on no owner question".
2. P5a. It serves AM-21.1 only as a conditional theorem; the row is NEW, and its reading for nature
   waits on Q11 and Q6.
3. P4 again. The stage after the first tranche lists "AM-7.2 and AM-7.3" among the rows to be proved,
   and §12.3 gives their route as P4. P4 is thus in the first tranche and in the later stage.
4. "serves Main roots (the §3.2, cone and Bell layers)". The tranche holds no cone unit (P3 waits on Q8
   and Q11), and P9 is in SM.

What makes an edit possible without settling the disputed class: the object that is proved is the same
under either class. P4, written with its two hypotheses named, is one conditional no-go about
completions whether those hypotheses are later counted as available or not; proving it adopts nothing.
That is the split F2 required for P6 and P10. The edit below keeps the tranche's membership and restates
its reason so that it is true whichever class AM-7.2 and AM-7.3 take. It is complete in the sense that
after E1 to E7 no sentence of r8 says or implies that P4 or P5a is free of added hypotheses, and each
replaced string was found exactly once in r8. On that footing Q12 is CONFIRMED WITH CORRECTION.

## 9. Downstream site lists (the coordinator's addition)

r8 states the limit in two places only: §22, "Still not done" (the 267 downstream citations of the
recovery rows were checked for existence and for a keyword; the 65 "A1–A6" lines, the four by-number and
ten by-name citations of item (ii), the 18 headline sites and the sites of §9 were not recounted), and
Standing, "Scope limits" (the row list is complete relative to its recipe). It is not stated where the
sites are listed or counted. No sentence of r8 says outright that every affected site has been found.
Six places imply it by giving a list or a count with no qualifier:

- §8: "Population of this table: 18 headline, abstract and summary sites."
- §9 item 1: "only the citations of (ii) change (by number: Main:60, :700, :718; GR:585)" and "none in
  GR, SM, Sub, Struct, Cx or `book/`".
- §9 item 3: "65 lines match … each range is rewritten".
- Q3(a): "The 65 lines that say "A1–A6" are rewritten".
- Q4(a): "The four citations of the item by number and the ten by name are rewritten."
- The item "Downstream." of every row in §2 to §7, and §21, whose bullet on citations sends the reader
  to §22.

Replacement wording is in E33. As a spot check made here by search at `main`: the pattern
`A1–A6|A1-A6` matches 65 lines in 10 files of `papers/` and `book/`; "total-finiteness posit" occurs on
ten lines (Main:44, :60, :111, :129, :216, :222, :266, :716, :718; Comp:118); item (ii) is cited by
number at Main:60, :700, :718 and GR:585, beside the ledger itself at Main:724. Those three counts match
r8. They are counts relative to a search pattern. A paraphrase would not be found by it.

## 10. Corrections, as exact edits

Each "replace" string occurs exactly once in r8 unless stated. Line numbers are r8's.

### Q12 (§19) and what it rests on

**E1.** Q12, option (b). Replace

> After the two reviews, the units that wait on no owner question are authorized first: P1 (the §3.2 channel and Born form for a realization's prior; AM-5, AM-2.1); P5a (the C2 persistence form as a conditional theorem; AM-21.1); P15 (the characterization theorem's proof uses no `t_R`; AM-20.1); P4 for a measurable `Ω`, with hypothesis (iii) read as in AM-7.2 (AM-7.2, AM-7.3); and parts (1) and (2) of P9 (AM-31).

by

> After the two reviews, the units whose proof can be written without an owner answer, and which assert nothing of nature, are authorized first, in two groups. Group 1, no premise beyond those on `main` and no reading: P1 (the §3.2 channel and Born form for a realization's prior; AM-5, AM-2.1); P15 (the characterization theorem's proof uses no `t_R`; AM-20.1); parts (1) and (2) of P9 (AM-31). Group 2, conditional theorems whose statements carry hypotheses that are not all worded on `main`: P5a (the C2 persistence form, for any hidden space carrying a joint law of record and hidden state; AM-21.1, which is NEW for nature); P4 for a measurable `Ω` (the Bell ceiling under hypotheses (i)–(iv), with hypothesis (iii) taken with a coupling graph in the dependency sense, and with measurable response functions; AM-7.2 and AM-7.3, whose class is disputed, §14.1). P4's proof cites the cone in its dependency form (kernel, `iterate_dependsOnlyOn_ball`, `RegionTower.lean:283`, for one alphabet); for site-dependent alphabets it also needs the short embedding step that §14 lists as unproved under P3, which is written with it.

**E2.** Q12, recommendation. Replace

> Reason: the first tranche needs no premise and no reading, and serves Main roots (the §3.2, cone and Bell
> layers); a proof counts for a row only when it has been checked against the properties that row's theorem
> uses (§14.3).

by

> Reason: every unit of the first tranche can be written and proved without an owner answer and asserts nothing of nature. P1, P15 and parts (1) and (2) of P9 need no premise beyond those on `main` and no reading. P5a and P4 are conditional theorems: each names in its statement hypotheses that are not all worded on `main` (P5a: a joint law of record and hidden state; P4: hypothesis (iii) with a coupling graph in the dependency sense, and measurable response functions), and proving them adopts neither a premise nor a reading. What a proved P5a or P4 counts for is decided elsewhere: P5a's reading for nature at Q11 and Q6 (AM-21.1 is NEW); the class of AM-7.2 and AM-7.3 under the rule for FIRM (§14.1, disputed; on this audit's classification, at Q8). P1, P4, P5a and P15 are inside Main; P9 is in SM (§14). A proof counts for a row only when it has been checked against the properties that row's theorem uses (§14.3).

**E3.** Q12, bullet "Changed in r6 …, corrected in r7". (a) Replace

> (AM-14; AM-23.2, a "partly" row; part (3) of AM-31, a replacement part)

by

> (AM-23.2, a "partly" row; part (3) of AM-31, a replacement part; AM-14 only for a form without GR:132's own hypotheses, since with them it is already direct on `main`, §12.3)

(b) Replace

> then those whose route needs one named property of K3 (AM-7.2 and AM-7.3; AM-30). Each is proved as a conditional theorem with its condition named. For P6 and P10 the conditional form (the measure, and bijectivity or injectivity, as named hypotheses) is what this stage proves; it asserts nothing of nature (Q5, Q6).

by

> then the row whose route needs one named property of K3 and is not already in the first tranche (AM-30, by P6; AM-7.2 and AM-7.3 are served by P4, which is in the first tranche). Each is proved as a conditional theorem with its condition named. For P6 the conditional form (the measure, bijectivity and time-reversal covariance as named hypotheses) is what this stage proves. P10 (AM-33.1) has no direct-proof target in §12.3; its conditional form (injectivity as a named hypothesis) may be written in the same stage. Neither asserts anything of nature (Q5, Q6).

**E4.** Q12, "Decision-ready?". Replace the two sentences from "The reason given for the first tranche, that it "needs no premise and no reading", was written while AM-7.2 was FIRM:" to "whether P4 stays in the first tranche is for the confirmation." by

> The first tranche's membership is unchanged. Its reason is restated so that it holds whichever class AM-7.2 and AM-7.3 take, and the later stage no longer lists them (focused confirmation of r8).

**E5.** §14.3, gate tally. (a) Replace "part (3) of P9 needs Q6(d) only," (the string runs over a line
break) by

> part (3) of P9 cannot be asserted of nature before Q6(d), and as a conditional theorem with a starting law as a named hypothesis it waits on Q11 and Q1(b-loc) only,

(b) After "`Ω`), P5a, P11 (as a conditional theorem), P14 and P15 wait on no owner question beyond authorization (Q12)." add

> P4 and P5a do so as conditional theorems whose statements carry hypotheses that are not all worded on `main` (Q12).

**E6.** Gate cells for P4. §12, row 17 (AM-7.2), "— (the `Ω_n` route: Q8)"; row 18 (AM-7.3), "—"; §14, P4, "— (the `Ω_n` route also Q8)". To each add

> ; none for the proof as a conditional theorem; the row's class is disputed (§14.1)

and delete the bullet "**Q12.**" from §22, "Still not done".

**E7.** Q12, "What it changes". After "It grants no recovery credit and adopts nothing." add

> No option names a writer or a reviewer, which the plain statement asks about: under §A.45 rule 3 each unit that starts also needs a designated writer recorded, and that is a separate record.

### The rule for FIRM (§0, §14.1, §20)

**E8.** §0, FIRM, after "is not FIRM." add

> A row is classed for the claim as it lands: what asserting it of nature needs, or, for a row that lands NC or RM, what the statement about the class of models needs. A hypothesis named in a statement on `main` is available for the conditional theorem; it is available for a claim about nature only if `main` also has it of nature (AM-4.4: the measure is named at SM:334 and is not on `main` as nature's).

**E9.** Needed only if AM-7.2 and AM-7.3 stay CONTINGENT. §0, CONTINGENT, after the first sentence add

> Also classed here: a row whose restated statement must carry a hypothesis that is not worded on `main` and asserts nothing of nature, where the undecided matter is whether such a hypothesis counts as a premise under the rule for FIRM (AM-7.2, AM-7.3; disputed, §14.1). For these two rows the decision is the owner's on the rule itself; no option of Q8 as worded for nature's carrier decides it.

**E10.** §14.1, table "Classes under the one rule", AM-2.1, last cell. After "the argument of Main:332" add

> ; P-indivisibility of the population process on the window, the theorem's own hypothesis (Main:330)

and in the dispute paragraph, after "(its F10)" in the AM-7.2 sentence, add

> ; the review also says that P4 "is not premise-free" and that the comparison of routes is "undetermined until P4 is written" (its section 11, item 5). For the reading as FIRM: the dependency-sense graph is the hypothesis of the kernel cone lemma on `main` (`CouplingGraph`, `RegionTower.lean:254`; `iterate_dependsOnlyOn_ball`, :283)

**E28.** (a) §20, "Disagreements with the review of r6", item 2. Replace "the reviewer's adjudication has all three FIRM" by

> the review's figure 7, 3, 8, 1 keeps AM-7.2 and AM-7.3 FIRM. For AM-21.1 the review gives FIRM by the conditional theorem and NEW by its own proposed rule of application (its F5), so on that rule it agrees with r7. Under the review's F5 rule and F7 together the counts are 6, 3, 9, 1, and the rows in dispute are AM-7.2 and AM-7.3 only

(b) §14.1, "Counts.". Replace "with the review's adjudication of those three rows the counts are" by

> with the review's figure for those three rows (r6's rule, with AM-31 moved) the counts are

and after "5 to 8." add

> Under the review's proposed rule of application (F5) AM-21.1 is NEW, as here; the counts are then 6, 3, 9, 1.

### Q11, Q1, Q8, Q6, Q3 (§19)

**E11.** Q11, option (a). Replace "A statement about nature's whole dynamics that assumes no size stays, with its status label:" by

> A statement about nature's whole dynamics that assumes no size stays, or, where it is the landing of a candidate recovery, may land, with its status label. Only the first of the following is on `main` in that form; the others are landings of candidates that have no recovery credit:

and, in the same sentence, replace "(AM-21.1, AM-21.2)" by

> (AM-21.1, as a conditional theorem on a joint law; AM-21.2, which also needs a reference prior under Q6(c))

**E12.** Q1, option (b-mode). After "P7 needs it (AM-22, AM-36, and through P7 AM-11 and AM-24)." add

> P7 also needs a shell measure (Q6(c)) and an invertible time-reversal-covariant rule (Q5(b) or (d)), and no route for AM-22 was found that avoids a shell measure (§12.3). Under the recommended answers to Q6 and Q5, P7 is not attempted, and (b-mode) then changes nothing for these four rows beyond keeping GR's existing conditional statements.

In option (a) and in "What it changes", after "part (3) of P9" add "(a replacement part, not a recovery)".

**E13.** Q8, option (a). Replace "is restated as a degree bound on one carrier of undetermined cardinality, from which finite reading sets follow." by

> is restated for one carrier of undetermined cardinality in the dependency sense: each site's update is a function of the values at a bounded number of sites. A bound on the degree of the graph that Main:362 reads from single-component sensitivity would not give this on an infinite carrier (EF-1 r6 N1.2).

**E14.** Q8, "What it changes". Replace "Four of the five CONTINGENT rows: AM-7.1 and AM-23.2 through finite reading sets, and AM-7.2 and AM-7.3 through P4's two added hypotheses (§14.1);" by

> Two CONTINGENT rows, AM-7.1 and AM-23.2, through finite reading sets; and, on this audit's disputed classification only, AM-7.2 and AM-7.3 through P4's two added hypotheses (§14.1). Those two hypotheses are properties of completions, and under each of (a), (b) and (c) the Bell statement would carry them itself;

**E15.** Q8(c) and Q6(e), "Basis" (the string occurs twice). Replace `Main:724 ("the named hypotheses ... are carried where they enter")` by

> Main:724 ("the named hypotheses of the matter, gauge and gravity sectors are carried where they enter"); applying that convention to this hypothesis is this audit's proposal and is not stated by Main

The same full quotation in Q8's recommendation and in §9 item 1.

**E16.** Q6, recommendation. Replace "for (c) and (d) no support was found beyond rescuing the rows that need them, which is the first barred shortcut." by

> for (c) no support was found beyond rescuing the rows that need it, which is the first barred shortcut (§14.4); for (d) no §A.29 case is drafted (which results it preserves, and what it predicts), and under (e) every statement that needs probabilities is still available as a conditional theorem.

Reason for E16: §14.4 says of a normalized starting law that it "is not specific to this row", so "solely
because it rescues a desired result" is not shown for (d); r6's reviewed reason for (d) was the missing
§A.29 case. In the same bullet replace "the review of r6 recommends the same, its D17" by "the review of
r6 recommends (e) and does not dispute (a), its section 11, item 4".

**E17.** Q6, "What each choice allows". After "under (e) without (d) it is a conditional theorem only." add

> The same holds for P5a (AM-21.1): under (d) its bound could be read of nature's hidden conditionals, with Q11(a); under (e) without (d) it is a conditional theorem on a joint law (§14.4).

**E18.** No edit: option (e) now has its text and its basis in the question, as c.6898395533 asks, and r8
states that it is not endorsed. With E15 the basis is quoted in full.

**E19.** Q3, option (a). Replace `A4's parenthesis, "a finite periodic lattice" (Sub:98), is restated;` by

> A4's parenthesis, "a finite periodic lattice" (Sub:98), is restated, with the sentence of Stage 2 (a) that uses it (Sub:157);

### Q2, Q13 and row AM-5b

**E20.** §12.1, row 57, column "Under Q2(b)". Replace "stays in Main §3.2 with its proofs; the hypothesis restated as a uniform law on the hidden boundary sites, uncorrelated with the visible input. Changed after review; unreviewed." by

> stays in Main §3.2 with its proofs and its hypothesis (the hidden input uniform and uncorrelated with the visible input, Main:310, :316), as under Q2(a). The threshold Theorem (Main:312–314) is A1-free and is unchanged. Changed after review; unreviewed.

**E21.** Q2, option (b). Replace "AM-5b, the 18th, stays in Main §3.2 with its proofs, its hypothesis restated as a uniform law on the hidden boundary sites, uncorrelated with the visible input [unreviewed]." by

> AM-5b, the 18th, stays in Main §3.2 with its proofs and its hypothesis, as under (a). A form with a uniform law on the hidden boundary sites alone is a candidate with no proof on `main` and no recovery credit (AM-5b, item 3); it is not part of this option.

and add to the list of A1-free results that stay in place: "the separability-threshold Theorem (Main:312–314, with the kernel witnesses named there)".

**E22.** Q2, "What it changes". After "N-1's bound under Q10(c))" add

> and the model-class sentence kept under Q9(c), whose content is already at Main:638 ("any fixed realization with a fixed prior has an exactly $L$-periodic multi-time law"), which stays in Main as AM-9.1 [this confirmation's reading]

and add to §12.2 a line "AM-5b (Main:290–324) | the census anchors at Main:312 and :314; other kept text that refers to the passage was not searched for here | **Stays in Main §3.2** | No exposure | yes", with the population line changed from 12 to 13 lines.

**E23.** Row AM-5b. (a) Item 1, after "Corollaries 1–2 (Main:304–320)" add

> ; the Theorem itself (Main:312) is a statement about abelian Weyl subgroups on `s` qubits and uses no hidden sector, so A1 enters Lemma 2 (iii) and the Corollaries only

(b) Item 5. Replace "these results keep the uniform hidden state as their stated hypothesis." by

> the uniform hidden state is written into the statements of Lemma 2 (Main:304–308) and Corollary 2 (Main:318), which now inherit it from Main:280; Corollary 1 (Main:316) states it already.

**E24.** Row AM-5b, item 4. Replace "Kernel witnesses for the threshold theorem are reported by the review of r6 and were not located for r7: **unclassified** in the census table (§10)." by

> Kernel witnesses for the threshold Theorem are named at Main:314 (`entanglementBreaking_twirl`, `not_entanglementBreaking_twirl`, `exists_lagrangian_tuple`, `isotropic_iff_commute`, `separable_imp_ppt`). Census: family 1, anchors "separability threshold" (Main:312) and `` `entanglementBreaking_twirl` `` (Main:314); no registry action while Main:312–314 stay, which every option of Q2 provides.

Q13, option (a): replace "AM-5b's census entry is unclassified: its kernel witnesses were not located." by

> AM-5b is in family 1 (anchors at Main:312 and :314) and needs no action while those lines stay.

Q13, "Decision-ready?" and "Unchecked rows": drop "its kernel witnesses not located".

**E25.** §10, family 1, column "Rows". Replace "AM-2.1, AM-5, AM-30" by "AM-2.1, AM-5, AM-5b, AM-30".

### Q14, Q7

**E26.** Q14. (a) After "none was read by the review of r6." add

> None of these files is governed by a receipt, a seal record or the legacy manifest (a search of `verification/receipts/`, `verification/seals/` and `verification/infrastructure/` at `main` for their directories finds nothing), and MR-1's preregistration says of itself that it is "not a native V3 control plane and not an `F` candidate". On that evidence none is a frozen record in the sense of §A.39; all are research or audit records [focused confirmation of r8; a search, not a reading of every receipt].

(b) Option (c). Replace "Frozen records are left unchanged, and only where a surviving claim cites one is a mutable note added on `main` that names the change." by

> The records are left as they stand, as records of what was premised when they were written, and only where a surviving claim cites one is a mutable note added on `main` that names the change. Were any of them frozen, it would be left unchanged for that reason as well.

(c) Recommendation. Replace "Reason: frozen records are never edited (§A.42 item 6); §A.46 item 4 asks for a mutable note only where verification status matters to a surviving claim." (the string runs over a line break) by

> Reason: none of the three is frozen, so §A.42 item 6 does not decide the matter. They are historical research and audit records, and the Code Review Rules keep such records as they stand ("do not rewrite historical commits or status records merely to make the history agree with the latest result"). §A.46 item 4 asks for a stated status where a surviving claim relies on one, which a mutable note supplies. MR-1 is a live stage-0 preregistration and takes the change in its own next revision if it proceeds.

**E27.** Q7, option (b). Replace "(EM) and `τ_B` move into Substratum §1.3 or §2.3" by "(EM) and `τ_B` move into Main §1.3 or §2.3, so that Main stays independent". Source: AM-8, item 3, and §12.2, both of which say Main.

### Tables, summary, attribution, site lists

**E29.** §20, after T31, add an entry with a new identifier: "AM-5b | finite-experiment "Partly": a direct proof for one step of the displayed update | "no": a property of a model's one-step channel | Main:316, :324; both can stand; no bearing on a class". Population 11.

**E30.** §14.1, "Population.". Replace "The other 37 rows have no class." by "The other 38 rows have no class."

**E31.** §18. Replace "The audit now covers 57 results that the papers tie to the whole world being finite (A1):" by

> The audit now covers 57 results that the row list ties to A1; in 48 of them the link to nature runs through A1:

Replace "10 are kept as statements or rewordings;" by "10 are kept: seven as statements and three as rewordings, one of which changes the falsifiability sentence (Main:718);". Replace "4 are firm (premises already on main; nothing proved)" by "4 are firm (three results and the ledger entry itself; premises already on main; nothing proved)".

**E32.** Attribution. Header: "only to quote the owner; twelve are quoted" becomes "only to quote the record; twelve were quoted in r6". §0: "are not the owner's" becomes "are not part of the adopted table". §1 heading: "and the owner directions applied" becomes "and the directions applied"; "C10 (owner records)" becomes "C10 (the #1169 records)". §22: "applied; a substantive correction (owner)" becomes "applied; a substantive correction (adopted direction, c.6898395533)"; "applied by the owner's rule" becomes "applied by the adopted rule (c.6898395533)"; "applied as a row (owner)" becomes "applied as a row (adopted direction, c.6898395533)".

**E33.** Site lists. (a) §21, replace the bullet "**Citations.** …" by

> **Citations and site lists.** For r8 the citations of the 19 recovery rows and of AM-5b were checked at `main`. The lists of downstream sites in the rows of §2 to §7 were checked only for existence and for a keyword of the row's subject on the cited line. The site counts of §8 and §9 are counts relative to the search patterns stated there and were not recounted for r8. A site that paraphrases its subject, or lies outside those patterns, would not have been found. No list in this audit is claimed to hold every affected site.

(b) §8, replace "Population of this table: 18 headline, abstract and summary sites." by "Population of this table: the 18 headline, abstract and summary sites found by this audit; the list is not claimed complete (§21)."

(c) §9, at its head add: "Each count below is the number of lines matching the stated pattern at `bf89ba13`. A paraphrase would not be counted (§21)."

(d) Q3(a): "The 65 lines that say "A1–A6" are rewritten;" becomes "The lines that say "A1–A6" are rewritten (65 by the pattern of §9 item 3; paraphrases are found at correction time by the corpus search of §A.25);". Q4(a): "The four citations of the item by number and the ten by name are rewritten." becomes "The citations of the item are rewritten (four by number and ten by name were found by search, §9 item 1; the corpus search of §A.25 is repeated at correction time)."

## 11. What was not checked

- **Rows.** Only the rows named in the table of section 1. No other row of the 57 was re-read. The
  eleven rows the review of r6 did not check stay unchecked except AM-5b.
- **Proofs.** No recovery route, no direct-proof target and no proof sketch was verified. P4 and the
  measurability argument of section 2 are unwritten and unchecked. The Lean statements were read, not
  built.
- **EF-1 r6.** Read only for its coherence class (its two §4.2 lines and nit 5). No other citation of
  EF-1 was checked, and none of its mathematics.
- **Sections of r8 not read:** §1 beyond three lines, §2 to §7 outside the rows named, §13, §14.2,
  §14.3 outside Table 5's counts and the gate tally, §15 beyond its first bullet, §16, §17, and §20's
  tables D1–D25 and T1–T21. Unverified statements there are r7's and r8's.
- **Citations.** Q1's statement that E3's justification is open; `GR:835`; `appendix-c-objections.md:132`
  and `book/README.md:90`; the FULL mirrors; Main:155, :157, :338, :354; the 107 census anchors of §10
  other than family 1 and the cells of families 8, 33, 34 and 40 as r8 prints them.
- **Records of Q14.** The files and the cited lines were read; whether a surviving claim cites any of
  them was not traced.
- **Quotations.** Compared with GitHub by reading (section 7).
- **The pilot** authorized in c.6898613777, and which questions wait on it.

## 12. Coverage

Of the 57 rows, 21 were checked here against `main` for the purpose of a question or of the rule for
FIRM: AM-2.1, AM-5, AM-5b, AM-6.2, AM-7.1, AM-7.2, AM-7.3, AM-8, AM-9.2, AM-11, AM-21.1, AM-22, AM-23.2,
AM-30, AM-31, AM-33.1, AM-4.4, N-3, N-6, and, for their cells only, AM-36 and N-1. A check was a reading
of the cited text and of the cited Lean statement, not a derivation, and for most of these rows it
covered only the lines that the question or the class rests on. The other 36 rows were not checked here. All fifteen questions were read in
full, with the readiness field, options, basis, recommendation and dependencies of each; the dependency
diagram and the order of decision agree with the questions. Nothing here adopts a premise, credits a
recovery or decides a question.
