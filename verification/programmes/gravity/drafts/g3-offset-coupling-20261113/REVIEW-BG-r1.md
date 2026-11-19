# REVIEW-BG-r1: G3 unit 2(b) r1, the bridge premise B_G

**Verdict: REVISE.** One finding is blocking, five are should-fix and two are nits.

What holds:

- Lemma U is valid given its premises.
- Corollary E is correct, and useful: read as a per-world claim, B_G says nothing more than that the witness's law is not realized.
- Refuting a *fundamental* governing gravitational law (F3) by the single-bijection dynamics P-D is sound.
- Most quotations are accurate.

What does not hold is the outcome (B), "B_G refuted; the term only co-constrains". It is not established, for three reasons.

1. **The rule cannot return (A).** An "OI world" satisfies N1–N3-G and N5-G. By Lemma U, no OI world has a grounding term. So clause (A) can be met only vacuously, and the rule forbids that. Clause (b1) is not barred from vacuous satisfaction in the same way.
2. **F1 and F2 assume the regularity view.** Both are evaluated per world, with the law's holding taken to be satisfaction of its equation and grounding treated as a separate fact. That is the regularity view of laws, which is unit 2(a)'s open condition (b), not a result.
3. **A formalization the corpus supports is missing.** F4: in the boundary law, sourcing is grounding. The corpus uses that language: "sourcing gravity" (GR:340), "source geometry" (GR:352), "everything that contributes to H_tot gravitates" (GR:358), "does not source curvature" (GR:581). F4 is non-fundamental, so P-D does not touch it. It is consistent with P-F's "no substance-level primitives" through mediate grounding. It passes K1–K5. Under F4 the witness's emergent source closes Lemma U's cycle and is excluded, while P11's classical energy content is admitted. That asymmetry is the one the geometry-first proposal intends.

Together these make the honest outcome **(C)**, with the residual narrowed to a sharper gap than unit 2(a)'s: is the boundary law's source term a ground of the metric (F4) or a co-constrained quantity (CoC)? The corpus routes its Einstein equation through Jacobson's equation-of-state argument (GR:162, SM:160), which reads CoC [L, recalled]. But that route is "used … not derived" (GR:162), so the CoC reading is conditional on the G3 law being an equation of state. B_G therefore still reduces in part to G3, through which law and which route. That is the opposite of BG-F2's claim.

**Target.** Branch `research/g3-offset-873-20261113` at `4acb3a49a73898d7ceb67c7f503d72c4597e34d6`, parent `d4fe24be`.

- The commit adds only G3-UNIT2B-BG-r1.md (688 lines) and NOTES-BG-r1.md (139 lines).
- Line references: "BG:n" is the record, "NB:n" is the notes, "U2Ar3:n" is G3-UNIT2A-r3.md, and "U1r5:n" is G3-UNIT1-r5.md. Corpus lines refer to `main` at `c3b5f37a`.
- **Authority.** #873 c.6865179466 (QU5): a bounded, paper-only B_G unit that adopts no premise, makes no manuscript change, starts no Lean build and makes no claim about Λ. The unit stays within that scope.

**Checks at `4acb3a49`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check 4acb3a49…` | 303 records intact |

None of them scans the drafts. A hand scan of the two new files finds no barred strings and no §A.32 or §A.33 phrases.

***

## Blocking

### BG-1. Clause (A) is unreachable by construction, F1–F2 assume the regularity view, and F4 is missing

**Where.**

- the rule: §1.2 (BG:146–159) and §1.3 (BG:161–169);
- Lemma U and Corollary E (BG:267–310);
- §4.2 (BG:388–392, "the disagreement … is not needed");
- §7 (BG:512–525);
- §0 (BG:44–62);
- BG-F1 (BG:604).

**Evidence.**

1. **The rule is asymmetric.**
   - An "OI world" is a realization that "satisfies the premise base" (BG:146–147). The premise base includes N1–N3-G and N5-G (BG:129–131). Lemma U shows that at every such world ¬(t ⊳_G g).
   - Clause (A) asks the premise base to entail that "at every OI world where [the] law holds, that term grounds the realized metric", and adds "The entailment must not pass through the non-realizability of the law" (BG:149–153). Given Lemma U, (A) can hold only vacuously, when no OI world realizes the law, and that is barred. (A) is unattainable for every formalization, before any analysis.
   - Clause (b1) asks the premise base to entail that "at every OI world where such a law holds the term does not ground" (BG:155–156). It carries no bar on vacuous satisfaction.
   - So the rule could return only (B) or (C). This is the direction §A.29 and §A.31 say to watch hardest. NB:74–78 records that the rule was written after an outline of exactly this argument had formed.
2. **Lemma U is Reading G's own reductio restated.** Lemma U's premises are N1–N2-G, N3-G, N3′ and N5-G, and its conclusion is ¬(t ⊳_G g). That is the inference N1–N3 + N5 ⊢ ¬N4 that unit 2(a) already states as Reading G (U2Ar3:277–284). It shows that no world with a grounding term is an OI world. In other words, if the witness's law *requires* a grounding term, Reading G excludes the witness. That is unit 2(a)'s conditional ("excludes the witness if and only if B_G", U2Ar3:504–505), not a refutation of it.
3. **F1 and F2 build in the regularity view.** Both are evaluated per world: "at an OI world `w` where the witness's law holds, its term grounds `g_w`" (BG:163–165). The law's holding is treated as satisfaction of its equation, and grounding as a further fact of `w`. On that view a law's holding never carries a grounding relation, which is unit 2(a)'s open condition (b): "a view of laws in which a derived law's terms do not ground its solutions … The corpus states no view on this" (U2Ar3:537–538). Unit 2(a)'s A8 (U2Ar3:599–601) already identifies the alternative: "a law with an emergent term grounds the metric in that term only if the law is more than a regularity". BG:391–392 says this disagreement "is not needed", because F3 is excluded by ontology and F1–F2 by Lemma U. But F1–F2 meet Lemma U only because they presuppose the regularity view.
4. **F4 is missing.** The formalization the corpus's own sourcing language supports is: "in the boundary law, a source term's energy content grounds the metric; the left side `G_μν[g]` does not; the law is non-fundamental (its grounds trace to `(S, φ)` mediately)".
   - **The corpus uses this language.** GR:340 s.2: "The stress-energy sourcing gravity". GR:352: "it cannot source geometry". GR:358: "everything that contributes to `H_tot` gravitates". GR:581: "does not source curvature". GR:400: "feeds back as a source". BG's own K3 row for P11 grants that "The text fixes neither role" (BG:243).
   - **F4 passes K1–K5.** K1: the C1-type metric is excluded. K2(a): K_dec's classical energy content is grounded in the microstate, not in g, so there is no cycle. K2(b): G_μν is the left side and is not a source. K2(c): the gap equation has no source term. K3: P11's classical energy is admitted; GR:400 Reading 1 is admitted under §8.3 (its piece is classical) and excluded without §8.3, as with (ii-L). K5: two configurations can share a ⊳_D graph and differ in which term is a source.
   - **F4 is not refuted by the premises cited against F3 and A3.**
     - P-D (Main:44, :54; Structure:136) excludes a *fundamental* additional law. F4 is not fundamental.
     - GR:342's "no substance-level primitives … spacetime emerges from `[(S, φ)]/𝒢_sub`" fixes the *ultimate* ground. F4 posits *mediate* grounding among derived items, which that sentence permits.
     - A3's refutation (BG:442–446) relies on Substratum.md:385–389's co-projection of GR and QM. As BG-3 sets out, that is the Substratum paper's statement of the geometry-first separation under test.
   - **Under F4, Lemma U gives the exclusion, not the refutation.** The witness's law makes an emergent-class energy (ρ_Z) a source. Then t ⊳_G g, and with g ⊳_G t that is a cycle, so no OI world realizes the witness's law. P11's source (microstate energy, not grounded in g) closes no cycle. That is the asymmetry geometry-first intends (GR:340, GR:358).
5. **BG's own uniformity claim depends on CoC.** "Nothing in Reading G separates an emergent-class term from `G_μν[g]`" (BG:52–53, :291–293) holds only if every term is CoC. F4 separates them by role: source against geometry. Unit 2(a)'s C2(b) admits the nonlinearity because it "runs through … no emergent relatum" (U2Ar3:485). It does not presuppose CoC for G_μν, so BG:286–288 overstates what C2(b) requires.

**Fix.**

1. **Repair the rule.** In §1.2 (A), either delete the clause "The entailment must not pass through the non-realizability of the law", or add the matching bar to (b1): "and the entailment must not be vacuous". Then evaluate each formalization on its *content*, meaning what the law's holding consists in. Record the change in the rule's provenance note.
2. **Add F4 to §1.3:**

   > "F4 (non-fundamental sourcing-as-grounding). The law is not fundamental; its source term's energy content grounds the metric, and its geometric side does not."

   Apply K1–K5 to F4 (§5), and record the result above.
3. **Restate the decisive step.**
   - Lemma U shows that a grounding source term grounded in g is unrealizable at OI worlds (case β, N5-G). Whether Reading G excludes the witness is then whether the witness's law is F4-type or CoC-type.
   - Replace BG:391–392 with:

     > "F1 and F2 meet Lemma U only on the regularity view; F4 is the non-fundamental grounding view; the corpus's sourcing language (GR:340, :352, :358, :581) is consistent with F4, and its Jacobson route (GR:162, SM:160) reads the law as an equation of state, which supports CoC [L, recalled]; the route is used, not derived (GR:162), so which reading applies to the G3 law is open."
4. **Re-apply the rule (§7).** Unless F4 is refuted from premises not on the excluded list, the outcome is:

   > "(C), with the gap narrowed: whether the boundary law's source term grounds the metric (F4: Reading G excludes the witness) or co-constrains it (CoC: Reading G excludes nothing beyond G3's determination question); the corpus's sourcing language supports F4, its equation-of-state route supports CoC, and that route's status is G3's."

   This is still strictly stronger than unit 2(a)'s gap. The productivity test (§1.5) is met by Corollary E and by the sharper gap.
5. **Reclassify BG-F1.**
   - Change it to "ELABORATING (Lemma U restates Reading G's reductio; Corollary E shows that B_G read per world adds nothing to the exclusion)".
   - Scope its "B_G … is false at every world satisfying Reading G's premises" to "F1, on the regularity view".
   - At BG:286–288, change "That classification presupposes CoC for `G_μν[g]`" to "On CoC the same step covers `G_μν[g]`; C2(b) admits the nonlinearity because it runs through no emergent relatum (U2Ar3:485)".

***

## Should-fix

### BG-2. The "§A.19 correction" (BG-F2) is a reinterpretation. The "two senses of derived" point is half right.

**Where.** §0 (BG:82–86); §4.1–4.2 (BG:355–392); BG-F2 (BG:605); NB:67–68.

**Evidence.**

- **Unit 2(a)'s negative statement.** It is narrow: "Even for a derived law, the corpus states no view on whether its terms ground its solutions" (U2Ar3:59, :538). None of the cited passages states such a view, and BG:389 concedes that "None of them uses 'ground', and none is a general philosophy of laws".
  - **Main:686–692** concerns the Wigner's-friend descriptions ("three descriptions, all derived from the same φ … simultaneous rather than competing"). It is about reduced quantum descriptions, not about a law that relates the metric and an emergent quantity.
  - **SM:158** describes the hypothetical lattice construction: the Clausius relation "*would* constrain the graph's response … *were the curvature step (iv) supplied*". The phrase "the Einstein equations are the equations of motion, not constraints on separate dynamics" is said of continuum GR, as a parallel. That phrase states that the gravitational relation is no separate dynamics, which supports P-D against F3. It says nothing on whether a source term grounds.
  - **GR:144, GR:581 and Substratum.md:387** state correspondence and projection relations. They are consistent with CoC, and GR:581 itself uses "source curvature".
- **The corpus's sourcing language is not weighed** as the corpus's view (BG-1, item 4).
- **The "two senses of derived".** The distinction between status (holds in virtue of `(S, φ)`, fixed for any law that holds by P-D) and derivation (G3) is real. U2Ar3:535's "That is G3" does run them together.
- **But unit 2(a)'s condition also required the metric to be grounded in `(S, φ)` "directly"** (U2Ar3:548–549). P-D fixes the ultimate ground. It does not exclude mediate grounding through derived items. "Directly" is B_G itself, not status.
- **With F4 added, B_G partly reduces to G3 after all.** Whether the G3 law is an equation of state (CoC) or a sourcing law (F4) is a question about which law and which route.

**Fix.**

- Restate BG-F2 as:

  > "Unit 2(a)'s condition (a) ran together the status of a law (fixed by P-D for any law that holds) with its derivation (G3); the status sense does not settle 'directly', which is B_G. The corpus contains passages consistent with co-constraint for its derived matching relations (SM:158, Substratum.md:387, GR:144, GR:581) and sourcing language consistent with grounding (GR:340, :352, :358, :581, :400); it states no view on whether a law's source terms ground its solutions, so unit 2(a)'s negative statement stands as worded."
- Class: ELABORATING (hidden assumption in "That is G3").
- Remove Main:686–692 from the list, or mark it "an analogy, not a statement about laws".
- Replace "B_G does not reduce to G3" (BG:79, :367–368) with "B_G's status component is fixed by P-D; its residual, F4 against CoC, depends on the route by which the G3 law is obtained".

### BG-3. K4 "no import" is not green for the F3, A3 and F4 refutations

**Where.** P-F (BG:66–68); K3 row Substratum.md:385 (BG:246); F3 (b2) (BG:329–336); A3 (BG:442–446); K4 (BG:421).

**Evidence.**

- **Substratum.md:385–389** ("the metric is a property of the classical dynamics of the partition boundary … two different substructures of the same total object"; "Both are derived") states the geometry-first separation of GR from QM, which is (ii-G)'s content.
- **GR:655** ("the effective cosmological constant (a property of the classical substratum's gravitational dynamics)") is the CC-dissolution distinction itself.
- Both play the role of the excluded conclusions: GR:342 "forced", GR:346 s.4 and ch07:187 (BG:136–138). The rule excludes those conclusions but admits these restatements.
- **F3** is refuted by P-D alone (Main:44, :54; Structure:136), which is clean.
- **A3**, and **F4** once it is added, should not rest on Substratum.md:385–389 or GR:655.

**Fix.**

- In K4, list Substratum.md:385–389's metric/QM separation and GR:655 as "conclusion-adjacent, not used in a decisive step".
- Rest F3 on P-D alone, and keep P-F's GR:342 clause ("no substance-level primitives"), which bears only on the *ultimate* ground.
- Re-evaluate A3 and F4 without the conclusion-adjacent premises.

### BG-4. QB1: re-applying unit 2(a)'s rule (§8.5)

**Where.** BG:579–585; QB1 (BG:655–657).

**Evidence.**

- §8.5 says that under unit 2(a)'s rule Reading G meets (B)(b) in case β, because B_G as F2 is "equivalent to the exclusion being tested". That holds only if F2 is *the* B_G.
- Under F4, Reading G's premise is a general claim about sourcing. It is not equivalent to the exclusion, and with N5-G it excludes the witness. Unit 2(a)'s rule then gives (A) for the witness on Reading G given F4, or (C) while F4 against CoC is open. It does not give (B).
- **In case α**, Reading G's reductio is unavailable, so Reading G meets (B)(a). But in that case Reading G is not the reading unit 2(a) formalized (N1–N2 in ⊳_G).
- So unit 2(a)'s outcome moves from (C) to (B) only conditional on N5-G, case β *and* CoC for the boundary law's source term.
- **§8.5's AW-loop statement is premature.** It says that, once B_G is false, "Reading G admits GR:400 Reading 1 in both §8.3 branches" and AW-loop "is then absent on Reading G". That inherits the same condition.

**Fix.** Restate §8.5:

> "Under unit 2(a)'s rule, Reading G meets (B)(b) in case β only if the boundary law's source term co-constrains (CoC); under F4 it meets (A) for the witness, or (C) while F4 against CoC is open. Unit 2(a)'s outcome therefore stays (C), with the gap narrowed to F4 against CoC (BG-1). The §8.3 rows and AW-loop are unchanged until that gap closes."

Answer QB1 in those terms.

### BG-5. Consequences 1–3 and §8.1–8.4 inherit BG-1

**Where.** BG:103–116; §8.1 (BG:536–541); §8.2 (BG:545–551); §8.3 (BG:555–561); §8.4 (BG:566–573); QB2 and QB3 (BG:658–666).

**Evidence.** Each of the following is stated without the CoC condition:

- "On no reading … does GR:346's argument exclude K_cpl^conv's field equation independently of G3 or of an added premise";
- "B_G supplies no exclusion of its own";
- "(DZ) … receives no support from GR:346's argument on any reading examined";
- "Part 2's exclusion of K_cpl^conv from GR:346 holds on no reading".

Under F4, GR:346 on Reading G excludes K_cpl^conv. The added premises are N5-G and F4. N5-G is already Reading G's own premise, and F4 is supported by the corpus's sourcing language.

**Fix.** Condition each of these sentences on "the boundary law's source term co-constrains (CoC), which is open (BG-1)". Hold the QB2 forward notes until the gap is settled.

### BG-6. Scope and overclaim checks

**Where.** §0 Scope (BG:89–99); §4.3 (BG:396–408); §8.6 (BG:588–596).

**Evidence.**

- K_cpl^conv is not claimed admissible in OI (BG:92–93, :688).
- Λ is not addressed (BG:22, :408, :596).
- The de Sitter and M1 scope is kept for the witness (BG:98).

This is correct, and nothing implies admissibility. One sentence overreaches: "Wherever a boundary law with a term that is a function of the emergent class holds, that term co-constrains the realized metric" (BG:46–47, :521–522). It asserts CoC as a result.

**Fix.** Change it to "On the regularity view, wherever …; under F4 no OI world realizes such a law (BG-1)".

***

## Nits

### BG-7. Commit status in the notes

**Where.** NB:17–18 ("The writer did not commit, push or post them").

**Evidence.** Both files are committed at `4acb3a49`. This is the same pattern as U-10 and Y-4.

**Fix.** Write: "committed to the branch at `4acb3a49` by the coordinator".

### BG-8. Uncertain literature details

**Where.** BG:644–645 ("details not verified").

**Fix.** Drop the Loewer and Lange entry, or give it as "the Humean-explanation debate [L, recalled]" without journal or year.

***

## Checked and correct

**Lemma U (BG:267–281) [A].** Valid: transitivity and irreflexivity under N5-G give ¬(t ⊳_G g).

- **"Grounded in the realized metric".** This is established given case β (N1–N2-G) and N3′. B4 (BG:489–492) correctly shows that the horizon area alone suffices, so N3′ is not needed.
- **Case β.** It is assumed, and B2 records case α correctly (Main:26, :48 contain no metric; GR:40 "implements"). AW-part is a sound catch.

**Corollary E (BG:295–310) [A].** Correct. It is the record's main positive result.

**F3 by P-D.** Correct: Main:44 ("iteration of a single transition map") and Main:54 (Lemma 3, a bijection). Structure.md:136 (A1–A6) lists finiteness, determinism (bijection), bounded coupling degree, center independence, linearity and background independence, and no gravitational law.

**Quotations checked on `main`.** All are accurate:

- GR:144 ("same physical degrees of freedom: the boundary modes V × B");
- GR:581 ("correspond to differences in the coupling structure of φ, which the Jacobson derivation reads as curvature");
- GR:655 ("the classical substratum's gravitational dynamics");
- GR:693 ("the framework's *own* emergent-metric geometry");
- SM:158 (the quoted fragments, with the "would … were" conditional noted in BG-2);
- Substratum.md:385, :387, :389 and :393;
- Main:26, :44, :48, :54, :686, :690 and :692;
- GR:160 (the classical route for T_cl);
- U1r5:192;
- the U2Ar3 lines cited: :138–141, :195–202, :277–287, :296–297, :342, :485, :504–507, :535–538, :548–552, :599–601, :612–620, :760–771 and :806–813.

**AW-metric (A6) and A5 (diachronic grounding).** Both are useful. A5 correctly locates its refutation in P-D, not in N5-G.

**Off-main references (NB §7).** Correctly traced under §A.42 item 8.

**Register and labels.** Clean. [A] is used for Lemma U and Corollary E, [P] for readings and [L, recalled] for literature.

***

## Disposition

REVISE.

- **BG-1 (blocking):** repair the rule's asymmetry, add F4, re-apply the rule. The expected outcome is (C), with the gap narrowed to F4 against CoC, which is tied to the route of the G3 law.
- **BG-2 to BG-6 (should-fix):** narrow the BG-F2 correction, remove the conclusion-adjacent imports, condition §8.5 and the consequences, and scope one sentence.
- **BG-7 and BG-8 (nits).**

The unit's real gains survive revision:

- Corollary E;
- the narrower gap, which is no longer "an unstated view of laws" but "is sourcing grounding?";
- F3's refutation by P-D;
- AW-part and AW-metric.

No manuscript change is proposed. No premise is adopted.
