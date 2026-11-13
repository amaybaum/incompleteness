# CONFIRM-BG-r2: delta check of G3 unit 2(b) r2 against REVIEW-BG-r1

**Verdict: REVISE.** Three findings are blocking, six are should-fix and four are nits.

What holds:

- BG-2, BG-3, BG-4, BG-5, BG-6 and BG-8 are resolved. BG-7 is resolved for r1 and recurs for r2 (nit BC-13).
- BG-1 is partly resolved. r2 states r1's rule defect as a defect, adds F4, withdraws (B) and reaches (C).
- Lemma U, Corollary E, F3's refutation by P-D and F4-1 (the presentation-invariant statement) are correct.
- The outcome letter (C) and its scope (Reading G, case β, conditional on N5-G) survive this review.

What does not hold:

1. **BC-1. The repaired rule, as instantiated, returns (A), not (C).** The only CoC-content formalizations it lists are F1 and F2. By r2's own Corollary E (r2:314–316), F1 is false at every OI world where the law holds, and F2 holds only vacuously. Neither is admissible under r2's own definition (r2:156–157).
2. **BC-2. F4-6 contradicts F4's own statement.** §3.4 states F4 on the energy content of every non-Einstein term, a constant Λ term included (r2:337–341). On the Jacobson route the witness's dependence moves into the integration constant, which is a uniform term of the realized equation. F4 as stated still reaches it there. "Confined to a divergence-free sourcing law" is not supported.
3. **BC-3. F4-5 is misplaced, and it understates F4's cost.**
   - With N3′, Lemma U's cycle does not depend on whether a term is emergent. Under F4, every source term that is a function of the metric closes it, in both §8.3 branches.
   - The classification of the corpus's horizon-defined sources is therefore not a condition on excluding the witness. It decides what else F4 excludes on Reading G: the running-vacuum form (GR:376–378) and the §7.3 source term (GR:528–530), which the writer did not consult.
   - This also corrects REVIEW-BG-r1 BG-1 item 4. That item stated that F4 admits GR:400 Reading 1 under §8.3, and that F4's asymmetry is the one the geometry-first proposal intends.

**Rule repair (question 2).**

- R-1 is a genuine, declared repair, and its structure is symmetric.
- It is a different rule from the review's minimal patch: it compares the admissibility of content kinds instead of per-world entailments. r2 says so.
- I find no sign in the rule's structure that it was fitted to (C). But two things need recording:
  - §1.1–§1.5 carry edits that §1.6 does not record (BC-4);
  - the "not tuned" argument in RESPONSE is not evidence (BC-7).

**Target.** Branch `research/g3-offset-873-20261113` at `8a3c43e19d3debd629f3e8506b96b00b47f4db6b`, parent `1970a36a`.

- `git show --stat` shows that the commit adds exactly three files: G3-UNIT2B-BG-r2.md (701 lines), RESPONSE-BG-r1.md (184) and NOTES-BG-r2.md (105). No other file changes.
- `diff` of r1 against r2 gives 56 hunks, as N2:77–78 states.
- Line references: "r2:n" is G3-UNIT2B-BG-r2.md, "r1:n" is G3-UNIT2B-BG-r1.md, "RESP:n" is RESPONSE-BG-r1.md, "N2:n" is NOTES-BG-r2.md, "U2Ar3:n" is G3-UNIT2A-r3.md and "U1r5:n" is G3-UNIT1-r5.md. Corpus lines refer to `main` at `c3b5f37a`.
- **Method.** Hand reading only, as the brief requires. No repository tool was run. I grepped the three new files for the barred path prefixes and for the §A.32/§A.33 phrase families I searched, and found none. I did not compute on OI rules, and I adopt no premise.

***

## 1. BG-1 to BG-8 at r2

| Finding | r2 location | Grade |
|---|---|---|
| BG-1 item 1 (rule asymmetric) | R-1 at r2:215–226; repaired §1.2 at r2:144–171 | **Partly resolved.** The defect is stated as a defect. The repaired rule is mis-instantiated (BC-1), and §1.1–§1.5 carry unrecorded edits (BC-4). |
| BG-1 item 2 (Lemma U is the reductio) | r2:306–308 | Resolved. |
| BG-1 item 3 (F1 and F2 assume the regularity view) | r2:175–179, :317–318, :493–494 | Resolved as a label. Labelling F1 and F2 "CoC-content" creates BC-1. |
| BG-1 item 4 (F4 missing) | r2:182–186, §3.4 (r2:333–364), §6.1 (r2:451–489) | **Partly resolved.** F4 is added and assessed, and F4-1 is sound. F4-3, F4-5 and F4-6 narrow the exclusion of the witness in ways the argument does not support (BC-2, BC-3, BC-5). |
| BG-1 item 5 (uniformity depends on CoC) | r2:308–310; the r1 §0 sentence is gone (grep) | Resolved. |
| BG-1 fixes 3 to 5 | r2:362–364, :393–424; outcome r2:532–554; BG-F1 at r2:628 | Resolved, subject to BC-2 for the route wording. |
| BG-2 | BG-F2 at r2:629 (the review's text verbatim); Main:686 at r2:403; SM:158 at r2:273; "directly" at r2:386–391; withdrawal at r2:548 | Resolved. The route sentence (r2:82–87) inherits BC-2. |
| BG-3 | R-2 at r2:139–142, :227–228; F3 at r2:320–331; A3 at r2:509–513; K4 at r2:435, :440–441 | Resolved. The excluded-list entry is stronger than the review asked, and correctly so. |
| BG-4 | §8.5 at r2:601–608; QB1 at r2:670–672 | Resolved. |
| BG-5 | r2:100–110, :563–599; forward notes held at r2:110, :598, :673–674 | Resolved. Consequence 1 gains a new "if and only if" (BC-6). |
| BG-6 | The overreaching sentence is removed (grep finds no "that term co-constrains"). Scope kept at r2:90–98, :692–701. | Resolved. |
| BG-7 | N2:13–17 | Resolved for r1. N2:18–19 repeats the pattern for r2 (BC-13). |
| BG-8 | r2:661–663 | Resolved. |

***

## 2. The rule repair

**Is R-1 genuine?** Yes.

- r1's clause (A) (r1:149–153) barred non-realizability. Its clause (b1) carried no such bar. Given Lemma U, (A) was unreachable. r2:215–222 says exactly this.
- The repair is stated as a repair, with its timing (r2:116–122, :697–698).

**Is it outcome-neutral?** In structure, yes.

- (A) needs CoC eliminated while a grounding-content formalization survives. (B) needs the reverse.
- The non-vacuity bar applies to both sides (r2:169–171).
- The second sentence of the non-vacuity paragraph is one-sided, but it is needed: without it, a grounding-content formalization could never meet (A), because its content together with Lemma U implies that the witness is unrealized. It does not make (A) easier than (B).

**Can (A) now be reached? Can (B)?**

- **As written, (A) is reached trivially.** The rule decides by which kinds remain admissible. Its CoC-content kind is represented only by F1 and F2, and neither is admissible by r2's own definition (BC-1). Literal application therefore gives grounding-content F4 admissible and no CoC-content formalization admissible, which is (A).
- **Once a proper CoC formalization is stated** (BC-1's F5), each outcome is reachable in principle:
  - (A), if a non-excluded premise states a governing view of derived laws, or if CoC fails K3 against the corpus's source vocabulary without a stated difference;
  - (B), if F4 fails a control or contradicts a premise.
- On the present corpus neither (A) nor (B) is reached. The corpus states no view on whether a derived law's source terms ground its solutions (U2Ar3:538, kept at r2:404–405). The excluded list removes P11, GR:575 and the Substratum.md separation clauses, which are the passages most likely to decide the question.
- Under the repaired rule, then, (C) is the outcome whenever the premise base is silent. That was knowable from unit 2(a) before this unit began.

**Was the rule fitted to (C)?** I find no evidence of fitting in the rule's structure.

- Evidence against fitting:
  - The rule is symmetric.
  - The deleted r1 clause "A failed control voids it, and the outcome is then (C)" (r1:191–192) removed a route *to* (C), not away from it.
  - The controls added at r2:197–198 (GR:384, GR:482) press on F4, the branch favourable to decoupling, not on CoC.
- Evidence for caution:
  - The repairs were written after the review named (C), and r2 says so (r2:120–121). That disclosure is necessary but does not remove the risk.
  - RESP:31–32 argues "Not tuned. The repaired rule was applied and gave (C), not r1's (B)". Agreeing with the reviewer's prediction is consistent with fitting to that prediction, so it is not evidence against it (BC-7).
  - The edits to §1.1–§1.5 are unrecorded, although r2:116 says those sections are unchanged except where §1.6 states a repair (BC-4). That is the "quiet" pattern the writer was told to avoid. None of those edits favours (C), but each must be stated.

***

## 3. F4: each condition checked by hand

**F4-1 (presentation; r2:335–343, :453–454).** Correct.

- `G[g] + Λ_c g = 8πG(T^cl − ρ_Z g)` rearranges to `G[g] + (Λ_c + 8πGρ_Z) g = 8πG T^cl` [A] (U2Ar3:342).
- A side-keyed F4 would classify a presentation, so the energy-content statement is needed. It strengthens F4 rather than narrowing it.
- That statement explicitly covers "a constant Λ term" (r2:341), which matters for F4-6.

**F4-3 (relata; r2:458–466).** Valid as a statement about variants. It does not narrow the exclusion of the witness.

- The acyclic chain needs a partition at `s` that is fixed by the metric at `s` alone. Given a first slice it is then also well-founded, which N5-G needs beyond acyclicity.
- The witness's partition is "the static patch of a geodesic observer. Its horizon is the event horizon of GR:40" (U2Ar3:303–304). An event horizon depends on the future metric, and r2's own second sub-bullet says the cycle then returns.
- In exact de Sitter, the static patch is itself fixed by the global Killing structure, not by a slice.
- So the escape needs a slice-local horizon, which is neither GR:40's partition nor the witness's.
- §0 (r2:66) drops the event-horizon alternative altogether. §7 (r2:542) keeps only "synchronic relata". Both overstate the condition (BC-5).
- r2's correction of r1's node A5 (P-D does not exclude macro-to-macro diachronic grounding) is sound.

**F4-5 (the corpus's "gravitating" quantities; r2:471–481).** These quantities are at stake, more broadly than r2 says. But they are not a condition on excluding the witness (BC-3).

- **The mechanism.** r2's own N3′ (r2:250–251) makes any quantity defined as a function of the metric grounded in it. Under F4 every such source term closes Lemma U's cycle, whether it is emergent or classical. F4 with Lemma U therefore filters sources by whether they depend on the metric, not by whether they are emergent.
- **GR:384 (`ρ_s`).** At stake.
  - `ρ_s` is built from the horizon area and `T_cl(H)` (GR:422–424), so it is grounded in `g` through the horizon.
  - On the de Sitter family it is structurally the witness's loop with `Λ_c = 0` and `F ≡ 0`. That is why GR:384 calls it "an identity".
  - r2's carve-out, "geometric identity", rests on a determination feature: every `R` solves. K5 (r2:202–203) says a determination feature does not settle grounding.
  - A carve-out that is relevant to grounding is available: "a consequence of the law, not a term of it". GR:426 supports it: "a consequence of Jacobson's Clausius relation applied to the de Sitter horizon". r2 does not state it.
- **GR:482 (§7.3).** At stake, and the "intermediary" carve-out is contested by the corpus's own text, which r2 did not read (N2:31 lists GR:462–482 only).
  - GR:528: the CMB peaks "require a non-oscillating gravitational source … The entropy displacement satisfies this requirement".
  - GR:530: "(i) its effective density is taken as `ρ_E ≈ Ω_CDM ρ_crit` … (iii) it grows under its own gravity … (iv) its growth equation … has the same source term as CDM".
  - GR:530 (ii) pulls the other way: "a gravitational effect at the horizon, not a fluid component".
  - So the corpus does not state the intermediary classification. Its own text treats `ρ_E` as a source term.
- **GR:376–378 (not examined by r2).** At stake. The running-vacuum form `Λ_eff(H)`, which GR:378 says the framework "forces", gets its `H`-dependence "via `A = 4πc²/H²`". Under F4 with N3′ it is a metric-dependent source.
- **GR:400 Reading 1.** Excluded under F4 in both §8.3 branches.
  - Its "curvature response … `∼ m²H²` piece" is defined as a function of `H`.
  - §8.3's classical/relative classification does not remove the edge `g ⊳_G` piece that N3′ supplies.
  - So r2:281 ("Under §8.3 … F4 and CoC both admit it"), r2:455–457 ("Under F4 without §8.3") and r2:567–568 (§8.3 "admits the configuration-differential part") are inconsistent with r2:250–251 and node B4. `Δρ_Z(R)` is a function of `R` through the horizon.
- **GR:695.** Not at stake.
  - The law obtained, `a = GM/r²` and the Poisson equation, has the mass as its source.
  - The equipartition temperature and degree-of-freedom count enter through the derivation and the constants (`G` fixed through `ε`). There the intermediary reading is apt.
  - r2:474 and BG-F6 (r2:633) overcount.
- **Partition-definedness cannot serve as the carve-out.**
  - `ρ_Z` is partition-defined: `N_modes = A/ε²` (U2Ar3:309; node B4).
  - GR:581 gives exactly that ground for the absolute zero-point baseline not sourcing: "a property of the partition geometry, not of the dynamics, and therefore … does not source curvature".
  - A carve-out drawn there would put `ρ_Z` on the non-source side, and F4 would no longer exclude the witness.
  - A carve-out drawn at "emergent against classical" is GR:575's clause, which is excluded (K4).
- **Consequence for K3.**
  - Uniform F4 classes these sources as sources, as the corpus's vocabulary does. K3 is then green, and their unrealizability on Reading G is a cost, like AW-loop under F4-2.
  - The corpus already carries this tension internally: GR:581's ground on one side, GR:384 and GR:528–530 on the other.
  - A carved F4 has K3 open until it states a difference that is relevant to grounding.
  - r2's "green; conditional on that classification" (r2:434, :538) prints a verdict over an undetermined control, which r2:205 does not allow.

**F4-6 (route; r2:482–485).** The relocation is correct. The narrowing is not (BC-2).

- U1r5:603–606 shows that the null flux does not see `−ρ g`. U1r5:596–600 shows that the witness's dependence can then enter only through the datum that selects the integration constant: "(SI′) fails if the selecting datum is `Λ_int` defined from a trace that contains `ρ_x(r)`".
- SM:162 displays the realized equation with `Λ g_μν`. Under §3.4's F4, that term's energy content grounds the curvature, and r2:341 applies F4 to constant Λ terms explicitly.
- If `Λ_int` is selected through `ρ_Z`, its energy content is grounded in `g`, and F4 with Lemma U gives the cycle.
- So F4 does not reach the witness on the Jacobson route only on a narrower F4, one restricted to the null-flux source term. r2 states no such F4.
- Separately, SM:160 conditions the Jacobson route itself "on the source coupling of [GR §6.2], open at G3". r2 calls the route "conditional", and that is enough.

**Net effect on BG-1.**

- REVIEW-BG-r1's statement "Under F4 … the witness … is excluded" stands for the witness as defined. It has one genuine refinement: on the Jacobson route the exclusion runs through the selection of the integration constant, and so depends on F4's scope.
- F4-3 and F4-6 as written reduce its force without warrant. F4-5 adds a condition that is not one.
- In the other direction, BG-1 item 4's statement that F4 admits classical sources in the geometry-first pattern was itself too strong. F4 is a costlier reading of the corpus than either document says.
- The errors in r2 do not run in one direction: F4-3 and F4-6 under-reach, and F4-5 understates cost.

***

## 4. Quotations and citations in the changed hunks

**Checked against `c3b5f37a` and the branch files. Accurate:**

- GR:40, GR:144, GR:162 ("uses the Einstein equations through Jacobson's relation (§3.1) and does not derive them"), GR:340 s.2, GR:342, GR:346, GR:352 ("does not entail that it cannot source geometry"; "a coupling theorem"), GR:358, GR:384, GR:422–426, GR:482, GR:581 ("does not source curvature"), GR:400 ("feeds back as a source"), GR:655 and GR:693;
- SM:158 (both clauses);
- Substratum.md:385, :389 and :393;
- U1r5:158, :198–204, :352–355, :419–421, :589–606 and :671;
- U2Ar3:76–78, :82–85, :277–287, :303–313, :342, :469–470, :485, :524–527, :535–538, :548–549, :617–620, :684–696, :715–720, :746, :770–771 and :829–832;
- CORR r2 X-1 (CORR-r2:67, :75–77).
- RESPONSE's r2 line pointers resolve to the cited text throughout.

**Errors** (nits BC-10 to BC-12):

- the SM:160 paraphrase at r2:274;
- the composite quotation at r2:386–388;
- two re-pointed U2Ar3 citations at r2:421–422.

The attribution of a source/intermediary distinction to SM:160 is a should-fix (BC-8).

***

## 5. Verdict and its scope

"(C), Reading G, case β, conditional on N5-G, residual F4 against CoC, partly reducing to G3" is right with these qualifications:

- **(C).** Supported once BC-1 is fixed (state F5) and BC-4's control clause is restored.
- **Reading G, case β, conditional on N5-G.** Exactly right (r2:51–52, :95–97).
- **Residual F4 against CoC.** Right in kind. Its stated conditions are wrong:
  - F4-3 does not apply to the witness as defined;
  - F4-6 is a relocation, not a confinement;
  - F4-5 is a cost, not a condition.
  - The cost itself (BC-3) is missing from the verdict.
- **Partly reducing to G3.** Supported only in a narrower sense. G3's equation decides whether the witness's dependence sits in a source term or in the selection of an integration constant, and so which scope of F4 is at issue. Under §3.4's F4 the route does not remove F4's reach (r2:82–87, :546–547).
- **Productivity (r2:550–554).** It survives. "three conditions F4 needs and … a route on which F4 does not apply" should become the corrected description.
- **§A.31 count.** The finding behind BC-3 is a candidate NEW: under F4, Lemma U's cycle is indifferent to emergence. The writer should reassess the claim of 0 NEW (r2:526–527).

***

## 6. Owner questions QB1 to QB5

- **QB1 to QB3.** Well posed.
- **QB4.** Inherits BC-3. Its F4 scoping ("also excludes emergent sources grounded in the metric") should read "also excludes every source term defined as a function of the metric, including the corpus's own §7.1–§7.3 constructions unless a grounded carve-out is found".
- **QB5(a).** Should add:
  - GR:376–380 and GR:528–530 to the audit list;
  - GR:581's ground against GR:384;
  - F4's scope (law terms, or the energy content of the realized equation).
- **Missing.** A question on the rule itself (BC-9):
  - whether the owner accepts the repaired rule as the rule of record for this unit;
  - whether the next unit's decision rule is to be fixed and reviewed before its analysis starts (§A.29: preregister the rule, not the expected numbers).

***

## Blocking

### BC-1. The CoC side of the repaired rule is instantiated by inadmissible formalizations

**Where.** r2:149–157 (definitions); r2:175–179 (F1, F2); r2:314–316 (Corollary E); r2:362–364; r2:428–436 (controls table, column "F1/F2"); r2:537 (§7).

**Evidence.**

- "Admissible: a formalization that passes K1–K5 and is not contradicted by a premise in the premise base" (r2:156–157).
- F1 asserts "its term grounds `g_w`" at every OI world where the law holds. r2:314 states "F1 is false at every OI world (Lemma U) [A]". So F1 is contradicted by the premise base.
- F2 holds "if and only if no OI world realizes K's law" (r2:315). On the regularity view the law can be realized, and F2 is then false. Where it is true, it is true only through non-realization, which r2:169–170 does not count.
- F1 and F2 are B_G read on the regularity view. They are not a formalization of the CoC content.
- r2:362 nevertheless says "F1 and F2 … pass K1–K5 … and no premise outside the excluded list contradicts them". This contradicts r2:314.
- Taken literally, §7 then has F4 admissible and no admissible CoC-content formalization, which is outcome (A).

**Fix.**

1. In §1.3, after F2, add:

   > "F5 (co-constraint, regularity view; added at review, R-4). The boundary law's holding is satisfaction of its equation. Its term and the realized metric have grounds in `(S, φ, x₀)`, and the term does not ground the metric. CoC-content."

2. Replace "CoC-content." at r2:177 and "CoC-content in the same sense." at r2:179 with:

   > "This is B_G read on F5's view. By Corollary E it is false at every OI world where the law holds (F1), or holds only if none does (F2). It is not itself a CoC-content formalization."

3. Replace r2:362 ("F1 and F2, the regularity view, pass K1–K5 (§5), and no premise outside the excluded list contradicts them.") with:

   > "F5 passes K1–K5 (§5), and no premise outside the excluded list contradicts it. At every OI world where the witness's law holds, Lemma U entails F5's clause `¬(t ⊳_G g)`."

4. Replace r2:537 with:

   > "**CoC-content formalizations.** F5 is admissible (§3.4, §6.2). F1 and F2 are B_G on F5's view and fail by Corollary E."

5. Rename the controls column "F1/F2 (CoC-content)" to "F5 (CoC-content)".
6. Add R-4 to §1.6.

### BC-2. F4-6: the Jacobson route moves the question; it does not put the witness beyond F4

**Where.**

- §0: r2:67 and r2:84–87;
- §4.3: r2:409–416;
- F4-6: r2:482–485;
- branch result: r2:487–489;
- §7: r2:542–547;
- BG-F5: r2:632;
- N2:66; RESP:10–11 and RESP:56–58.

**Evidence.**

- §3.4 states F4 on "every term other than the Einstein tensor, taken as the scalar energy density and pressure it carries", and applies it to "a constant Λ term" (r2:337–341).
- The realized equation on the Jacobson route carries `Λ g_μν` (SM:162). By U1r5:596–600, the witness's dependence then sits in the datum that selects `Λ_int`.
- If `Λ_int` is selected through `ρ_Z(r)`, its energy content is grounded in `g`, and F4 with Lemma U gives the cycle.
- "F4, a claim about sources, does not reach it" (r2:87) holds only for an F4 restricted to the null-flux source term. r2 states no such F4.

**Fix.**

1. Replace the verdict of F4-6 (r2:483–485, from "F4 then does not reach") with:

   > "The F4-against-CoC question then moves from a source term to the relation that selects the integration constant (U1r5:596–600). Under §3.4's statement, which covers the energy content of a uniform term of the realized equation, F4 with Lemma U excludes a selection through `ρ_Z`. Only an F4 restricted to the null-flux source term leaves it unreached. Verdict: the route decides where F4 applies, and whether it applies depends on F4's scope, which the premise base does not fix. [P]"

2. Replace r2:84–87 ("On the corpus's conditional Jacobson route … F4, a claim about sources, does not reach it.") with:

   > "On the corpus's conditional Jacobson route, the uniform term has zero null flux (U1r5:671; U1r5:603–606) [A]. The witness's emergent dependence can then enter only through the datum that selects the integration constant, which is unit 1's R2a question (U1r5:589–606). F4 as stated in §3.4 still reaches it there; an F4 restricted to the null-flux source does not."

3. Delete the bullet at r2:67.
4. Apply the same change to:
   - r2:412–415;
   - r2:488 ("a divergence-free sourcing law");
   - r2:542 and r2:546–547. Replace the latter with "the route decides whether the witness's dependence sits in a source term or in the selection of the integration constant, and so which scope of F4 is at issue (§4.3)";
   - BG-F5 (r2:632);
   - N2:66;
   - RESP:10–11 and RESP:56–58.

### BC-3. F4-5 is a cost of F4, not a condition on excluding the witness, and the cost is understated

**Where.**

- §0: r2:68–69;
- §2.4: r2:274, :278–281, :283–286;
- r2:352 and r2:434;
- F4-2: r2:455–457;
- F4-5: r2:471–481;
- branch result: r2:487–489;
- r2:538;
- §8.1: r2:567–568;
- BG-F6: r2:633;
- AW-entropic: r2:643–645;
- N2:36–39 and N2:64–67.

**Evidence.** See §3 above. In summary:

- N3′ (r2:250–251) and node B4 make every metric-defined source term grounded in `g`. Under F4, Lemma U then excludes it on Reading G whether it is emergent or classical, and whether or not §8.3 is in force.
- The corpus cases at stake are:
  - GR:376–378 (not examined);
  - GR:400 Reading 1, in both branches;
  - GR:528–530 (not read: §7.3's `ρ_E`, with "the same source term as CDM");
  - GR:384, if `ρ_s` is a term of the law.
- GR:695 is not at stake.
- Partition-definedness cannot separate these from `ρ_Z`, which is partition-defined, and GR:581 uses exactly that ground for the absolute baseline.
- The witness's exclusion under F4 does not depend on how these quantities are classified. Their classification decides what else F4 excludes.
- r2's "green; for F4, conditional on that classification" (r2:434) prints a verdict over an undetermined control, against r2:205.
- REVIEW-BG-r1 BG-1 item 4 made the same §8.3 assertion. This finding corrects it too.

**Fix.**

1. Replace r2:68–69 with a separate bullet after the F4 bullet:

   > "**The cost of F4 on Reading G [P].** With N3′, Lemma U's cycle does not depend on whether a term is emergent. Applied uniformly, F4 also makes unrealizable on Reading G the corpus's own metric-dependent sources: the running-vacuum form (GR:376–378), GR:400 Reading 1 in both §8.3 branches, the §7.3 source (GR:528–530) and GR:384's `ρ_s` if it is a term of the law and not a consequence of it (GR:426). No carve-out that admits these and excludes the witness on a ground relevant to grounding has been stated. Partition-definedness does not supply one, because `ρ_Z` is partition-defined (§6 node B4) (§6 node F4-5)."

2. Replace F4-5 (r2:471–481) with:

   > "**F4-5. The corpus's metric-dependent sources.** With N3′, a term defined as a function of the metric is grounded in it, emergent or not, and under F4 a source term of that kind closes Lemma U's cycle. Cases: GR:376–378 (`Λ_eff(H)`, `H`-dependent 'via `A = 4πc²/H²`'); GR:400 Reading 1, in both §8.3 branches; GR:528–530 (`ρ_E`, with 'the same source term as CDM'; but '(ii) … a gravitational effect at the horizon, not a fluid component'); GR:384's `ρ_s`, unless it is read as a consequence of the law (GR:426) rather than a term of it. GR:695 is not a case: its law's source is the mass, and the horizon quantities enter its constants. A carve-out needs a difference relevant to grounding. Partition-definedness fails, because `ρ_Z` is partition-defined, and GR:581 gives that same ground for the absolute baseline not sourcing. 'Emergent against classical' is GR:575's excluded clause. Verdict: uniformly applied, F4 is admissible and passes K3 by classing these as sources, as the corpus's vocabulary does. On Reading G it then makes them unrealizable along with the witness, which is the tension the corpus carries between GR:581 and GR:384 and GR:528–530 (AW-entropic). Whether a grounded carve-out exists is open. [P]"

3. Make these consequential edits:
   - r2:281: "Under F4, excluded on Reading G in both §8.3 branches (N3′); CoC admits it."
   - r2:455–457: replace "Under F4 without §8.3" with "Under F4, with or without §8.3".
   - r2:567–568: "Given F4 … it also excludes sources defined as functions of the metric, including the configuration-differential part, which is a function of `R` through the horizon (§6 node B4)".
   - K3 cell r2:434: "green for uniform F4 (classes the corpus's metric-dependent sources as sources); their unrealizability on Reading G is a cost (AW-entropic, F4-5). A carved F4 has K3 open."
   - r2:538: delete "F4's K3 is conditional on F4-5's classification".
   - r2:283–286, r2:487–489 and BG-F6 (r2:633): align with the above. Drop GR:695 from BG-F6.
   - AW-entropic (r2:643–645): extend its sites to GR:376–378 and GR:528–530.
   - Reclassify BG-F6 as a candidate NEW, and recount r2:526–527.

***

## Should-fix

### BC-4. §1.1–§1.5 carry edits §1.6 does not record

**Where.** r2:116; §1.1 at r2:127–129; §1.4 at r2:189–205; §1.5 at r2:209–211.

**Evidence.** `diff` of r1:120–200 against r2:114–232 shows the following edits outside R-1 to R-3:

- §1.1 drops "and has no role off it" and the rationale clause of the excluded list.
- K1 drops "so that the verdict depends on the order of grounding and not on values".
- K3:
  - its list drops "(P11)";
  - Substratum.md:385–389 becomes :385–393;
  - it adds GR:384 and GR:482;
  - the comparison changes from "a verdict that classes the witness's term differently from a corpus use … is void" to "a classification that differs from a corpus use … fails K3".
- The closing line drops "A failed control voids it, and the outcome is then (C) with the failed control named" and adds "for the formalizations it rests on".
- §1.5 drops "Otherwise it is recorded as a coherence check."

r2:116 states that these sections are "unchanged except where §1.6 states a repair". r2:442 records the K3 additions only in §5. None of these edits favours (C). Dropping the failure clause removes a route to (C), but it also leaves the rule with no clause for an undetermined control (BC-3).

**Fix.**

1. Add to §1.6:

   > "R-5 (edits to §1.1–§1.5). [list each edit above, with its reason]."

2. Restore the closing line of §1.4 as:

   > "A verdict is written only if K1–K5 are green for the formalizations it rests on. A formalization with a failed control is rejected; one with an undetermined control is neither admitted nor rejected, and if that decides the outcome, the outcome is (C) with the control named."

3. Restore §1.5's last sentence.

### BC-5. F4-3 does not narrow the exclusion of the witness as defined

**Where.** r2:66, :458–466, :488, :542, :632; N2:65; RESP:48–51.

**Evidence.**

- The witness's partition is the static patch whose horizon is GR:40's event horizon (U2Ar3:303–304). By r2's own second sub-bullet (r2:461–462), the cycle returns with that partition.
- The diachronic escape needs a partition fixed by the slice alone. In exact de Sitter, the static patch is fixed by the global Killing structure.
- r2:66 and r2:542 omit the event-horizon alternative.

**Fix.**

1. Replace F4-3's verdict (r2:465–466) with:

   > "Verdict: diachronic relata remove the exclusion only for a variant whose partition is fixed by the metric on the slice (a slice-local horizon), and then only given a first slice for well-foundedness. With GR:40's event-horizon partition, which the witness uses (U2Ar3:303–304), the cycle returns. F4-3 does not narrow the exclusion of the witness as defined. [P]"

2. In §0 (r2:66) and §7 (r2:542), state the condition as:

   > "unless the partition is slice-local and the relata diachronic (F4-3)"

### BC-6. Consequence 1's "if and only if" needs its scope (§A.34)

**Where.** r2:102–104.

**Evidence.**

- The "if" direction is F4 with Lemma U [A].
- The "only if" direction holds only relative to the formalizations examined. Its support is that F3 is refuted and CoC excludes nothing. No result shows that the list is exhaustive.

**Fix.**

> "On Reading G, among the formalizations examined (F1–F5), GR:346 excludes K_cpl^conv's field equation if F4 holds for the boundary law's source term, subject to nodes F4-3 and F4-6; given F5 (CoC), it excludes no field equation beyond G3's determination question [A] given each branch, [P] for the readings."

### BC-7. The "not tuned" argument and the default outcome

**Where.** RESP:31–32; r2:116–122; r2:697–698.

**Evidence.** RESP:31–32 reads: "Not tuned. The repaired rule was applied and gave (C), not r1's (B)." Agreement with the reviewer's named expectation is not evidence against fitting to it (§2 above).

**Fix.**

1. Replace RESP:31–32 with:

   > "**Tuning.** The repaired rule is symmetric (§1.2), and the controls added at review press on the F4 branch. Under it, (C) is the outcome whenever the premise base states no view on whether a derived law's source terms ground its solutions, which unit 2(a) recorded (U2Ar3:538). That (C) agrees with REVIEW-BG-r1's expectation is not evidence either way."

2. Add the third sentence to r2's provenance note (r2:120–122).

### BC-8. The source/intermediary distinction is a reading, not stated at SM:160; the §A.19 search was too narrow

**Where.** r2:274 (column "Relation stated"); r2:434; r2:478–479; r2:633; RESP:54–55; N2:36–39.

**Evidence.**

- SM:160 lists four inputs, and says "(iii) is a definition and (iv) an identity" given the manifold.
- It classes no input as source or intermediary.
- The search for "gravitating" (N2:36) missed GR:376–378 and GR:528–530, which use "forces", "gravitational source" and "source term" instead.

**Fix.**

1. Move "input (iii) is the source; (i) and (ii) are thermodynamic intermediaries" from the "Relation stated" column to the "Reading [P]" column.
2. Replace "a distinction stated at SM:160" (r2:434) and "the input (iii) against (i)–(ii) distinction of SM:160" (r2:478–479) with "a reading [P] of SM:160's list of inputs".
3. Apply the same change at BG-F6 and RESP:54–55.
4. Record the wider search in NOTES-BG-r3.

### BC-9. Owner questions: one missing, two to update

**Where.** r2:668–688.

**Fix.**

1. Add:

   > "**QB6. The rule.** The decision rule of this unit was repaired after a review that named the expected outcome (§1.6). Is the repaired rule accepted as the rule of record here, and should the next unit's rule be fixed and reviewed before its analysis (§A.29)?"

2. In QB4, replace "given F4, it also excludes emergent sources grounded in the metric" with:

   > "given F4, it also excludes every source term defined as a function of the metric, including the corpus's §7.1–§7.3 constructions unless a grounded carve-out is found (§6 node F4-5)"

3. In QB5(a), add:
   - GR:376–380 and GR:528–530;
   - GR:581's ground against GR:384;
   - "F4's scope: law terms, or the energy content of the realized equation (§6 node F4-6)".

***

## Nits

### BC-10. SM:160 paraphrase

**Where.** r2:274.

**Evidence.** The row reads "(i) area law, (ii) Unruh temperature of a reduced state". SM:160 has "(i) a proportional entropy law `δS = η δA`; (ii) the Unruh temperature `T = ħκ/(2πc k_B)`". "Of a reduced state" is not in SM:160.

**Fix.** Write "(i) a proportional entropy law, (ii) the Unruh temperature".

### BC-11. Composite quotation

**Where.** r2:386–388.

**Evidence.** The quoted sentence "the boundary law is a coarse-grained consequence of the substratum dynamics in which the realized metric is grounded in `(S, φ)` directly" splices U2Ar3:524 and U2Ar3:548–549.

**Fix.** Quote U2Ar3:548–549 verbatim: "the boundary metric's law is a coarse-grained consequence of `φ` in which the realized metric is grounded in `(S, φ)` directly".

### BC-12. Re-pointed citations

**Where.** r2:421–422.

**Evidence.**

- U2Ar3:697–714 is world-equivalence and (DZ), not the determination question. r1:401–404 cited :697–702 for the world-equivalence.
- U2Ar3:847–848 is QU5(b) itself. It is not support for "its `Z` would be a consequence of `φ`".

**Fix.** Write "(cf. U2Ar3:697–702, world-equivalence)" and "(unit 2(a)'s QU5(b), U2Ar3:847–848)", as r1:401 did.

### BC-13. NOTES-BG-r2

**Where.** N2:18–19 and N2:78.

**Evidence.**

- N2:18–19 reads "The writer did not commit, push or post it". r2 is committed at `8a3c43e1`. This is the BG-7 pattern again.
- N2:78 reads "RESPONSE-BG-r1 §3 maps the hunks". The delta table is RESPONSE §4.

**Fix.**

- Record in NOTES-BG-r3 that r2 was committed at `8a3c43e1` by the coordinator.
- Change "§3" to "§4".

***

## Disposition

REVISE.

- **BC-1 to BC-3 (blocking).**
  - State F5 and restate F1 and F2.
  - Restate F4-6 as a relocation that depends on F4's scope.
  - Move F4-5 from condition to cost, and state that cost with N3′.
- **BC-4 to BC-9 (should-fix).**
  - Record the rule edits, and restore the clause for undetermined controls.
  - Correct F4-3's reach.
  - Scope the "if and only if".
  - Restate the tuning argument.
  - Reattribute the SM:160 distinction.
  - Add QB6.
- **BC-10 to BC-13 (nits).**

Once these are applied, the outcome stays (C), with the same scope. The residual becomes: F4, with its scope and cost stated, against F5. Its partial reduction to G3 is through where the route puts the witness's dependence.

The fixes are textual, apart from the wider §A.19 read already done here. No new computation is needed.

No manuscript change is proposed. No premise is adopted.
