# CONFIRM-BG-r3: delta check of G3 unit 2(b) r3 against CONFIRM-BG-r2

**Verdict: ACCEPT WITH CHANGES.** Nothing is blocking. There are four should-fix findings and three nits.

Two of the should-fix findings (CF-1, CF-2) must be applied before QB7 goes to the owner, because as written QB7 states the consequence of an owner decision wrongly.

What holds:

- **BC-1 to BC-13.** BC-1, BC-2, BC-3 (except one point), BC-5 to BC-12 and BC-13 for r2 are resolved at the cited lines. BC-4 is partly resolved (CF-4).
- **The rule.** Under the rule as written, (C) is now reached honestly:
  - F5 is admissible;
  - uniform F4 is admissible, with K3 green by uniformity;
  - F1 and F2 are correctly placed as B_G evaluated on F5's view.
- **(A) and (B).** Both remain reachable in principle. F4-8 is a concrete route toward (B), which is evidence against the rule having been fitted to (C).
- **F4-7, F4-3, F4-6 and F4-null.** F4-7 is sound. F4-3 and F4-6 are now correctly stated. F4-null is correctly classed as CoC-content with respect to the witness's term.

**The disputed BC-3 point.** I concede part of it and rebut part of it (CF-2).

- **Conceded.** CONFIRM-BG-r2's "excluded in both §8.3 branches" was unconditional, and too strong for GR:400 Reading 1. GR:573 makes a relocation reading available.
- **Rebutted.** r3 states an admission where the sources support only "undetermined". For the running-vacuum channel, r3's admission contradicts r3's own F4-7, because the corpus describes that channel's `H`-dependence as a quantity of the partition-selected hidden sector.

**Target.** Branch `research/g3-offset-873-20261113` at `7fd16a5d81f20d85b98544b8349f550c07b4c519`, parent `27c409a0`.

- The commit adds exactly three files: G3-UNIT2B-BG-r3.md (793 lines), NOTES-BG-r3.md (112) and RESPONSE-BG-r2.md (216).
- `27c409a0` adds CONFIRM-BG-r2.md, byte-identical to the review I issued (`cmp`).
- Line references:
  - "r3:n" is G3-UNIT2B-BG-r3.md, "r2:n" is G3-UNIT2B-BG-r2.md;
  - "RESP:n" is RESPONSE-BG-r2.md, "N3:n" is NOTES-BG-r3.md;
  - "U2Ar3:n" and "U1r5:n" are the unit 2(a) r3 and unit 1 r5 records.
  - Corpus lines refer to `main` at `c3b5f37a`.
- I worked by hand reading only. I did not compute on OI rules, and I adopt no premise.

***

## 1. BC-1 to BC-13 at r3

| Finding | r3 location | Status |
|---|---|---|
| BC-1 | R-4 at r3:242–249; F5 at r3:197–199; F1 and F2 at r3:184–189; r3:362–364; F5 admissible at r3:409–412; §7 at r3:620–621; column at r3:470 | Resolved. F5 is not contradicted: Lemma U entails its clause `¬(t ⊳_G g)` wherever the law holds. Its common base rests on GR:342's non-excluded clause and transitivity. |
| BC-2 | F4 in §1.3 at r3:192–196; §3.4 at r3:378–392; F4-6 at r3:544–552; §0 at r3:71–75; §4.3 at r3:456–458; §7 at r3:631–632 | Resolved in substance. BG-F5 and the "route decides scope" wording introduce a new error (CF-3). |
| BC-3 | cost framing at r3:76–91 and r3:507–543; K3 at r3:476; r2:538's conditional removed; GR:695 at r3:324 and r3:517; BG-F6 at r3:715; AW-entropic at r3:725–727 | Resolved, except the §8.3 point (CF-2). |
| BC-4 | R-5 at r3:250–266; clause at r3:220–222; §1.5 at r3:228–229 | **Partly resolved.** r2's edits are now recorded. r3's own edits to §1.2 and §1.3 are not, although r3:127 says every later edit is (CF-4). |
| BC-5 | r3:68–70, r3:496–503, r3:625–627 | Resolved. |
| BC-6 | r3:112–115 | Resolved, with the non-exhaustiveness stated. |
| BC-7 | r3:130–134 | Resolved. |
| BC-8 | r3:312; search at N3:35–49 | Resolved. |
| BC-9 | QB4 at r3:756–762; QB5(a) at r3:764–767; QB6 at r3:772–774 | Resolved. QB7 is new and needs CF-1 and CF-2. |
| BC-10 to BC-12 | r3:312; r3:430–431 (now verbatim U2Ar3:548–549); r3:462–464 | Resolved. |
| BC-13 | N3:13–16 | Resolved for r2. The pattern recurs at N3:17–18 for r3 (CF-7). |

***

## 2. The new repairs and the rule

**R-4** (r3:242–249) is correct and honestly stated. It says that r2's rule, read literally, returned (A), and that this "came from omitting the CoC formalization from the list".

**F5 passes K1 to K5:**

- K1: the C1-type metric is excluded by its nature.
- K2: F5 classes nothing as grounding.
- K3: F5 reads "source" as a term of the equation, and keeps GR:581's distinction as presence in, or absence from, the equation.
- K4: F5 uses no excluded premise.
- K5: holds.

**R-5** (r3:250–266) records r2's edits accurately. I checked it against the r1/r2 diff I made for BC-4. The restored undetermined-control clause is r1's own (r1:191–192), generalized. It is not a new bias toward (C).

**Is (C) reached honestly?** Yes. Both kinds are admissible, and the rule returns (C). r3:51–53 and :132–134 state openly that (C) is the outcome whenever the corpus is silent on whether derived laws' source terms ground their solutions.

**Can (A) and (B) be reached?**

- **(A)** needs F5 eliminated. That would take a non-excluded premise stating a grounding or governing view of derived law terms, or a K3 failure for F5.
- **(B)** needs uniform F4 rejected, and every carved F4 rejected as well. F4-8 shows how uniform F4 could be rejected: by holding the running-vacuum channel as a premise. But a carved F4 with K3 undetermined then decides the outcome. By r3's own clause (r3:220–222), the result is (C) with K3 named, not (B) (CF-1).
- So (B) is reachable in two steps, not one.

***

## 3. The disputed BC-3 point: GR:400 Reading 1 under §8.3

**The writer's argument** (RESP:68–91; r3:518–532). GR:573 says relative differences have "a classical microstate difference corresponding to this energy difference" and "appear in the classical stress-energy tensor and gravitate". Under §8.3, then, the gravitating item is a classical counterpart defined on the microstate, like `T^cl`. N3′ does not apply to it, and its covariation with `H` is ⊳_D.

**What I concede.**

- CONFIRM-BG-r2 BC-3 took the gravitating item to be the emergent computation as defined: the "`∼ m²H²` piece", a function of `H`.
- GR:573 makes a different reading available: the item is the classical counterpart. On that reading N3′ is not shown to apply.
- My statement "excluded in both §8.3 branches" was therefore too strong as an unconditional claim.
- r3 handles the point properly in form: it records both readings, and it shows that the witness is unaffected.
- The witness is indeed unaffected:
  - its realized value is absolute (U2Ar3:469);
  - §8.3's correspondence is stated only for relative differences;
  - with no relocation, `ρ_Z` stays as defined from the class (U1r5:222–225).
  
  This needs no appeal to GR:575's excluded clause.

**What I rebut.**

1. **The scope of the correspondence.** GR:573's examples are configuration differences at a fixed geometry ("An electron at rest vs. no electron"). GR:577, a search hit at N3:42 that r3 does not cite, states the scope: mode structure producing relative differences "corresponds to classical microstate differences, is determined by the visible data, and gravitates". An epoch difference in the vacuum energy is not one of these cases. U1r5:506 records that extending the correspondence to it "rests on GR:400's statement and not on a derivation".
2. **The corpus's own mechanism for the running-vacuum `H`-dependence is partition-level.**
   - The emergent vacuum energy is "a state-level quantity depending on the hidden sector's volume" (GR:374; also GR:358).
   - Its `H`-dependence is inherited because `S_dS` "depends on `H` via `A = 4πc²/H²`" (GR:378(i)).
   - A classical counterpart of that difference is an energy total over the partition-selected hidden sector. That is a set-level quantity, and r3's own F4-7 (r3:553–557) grounds such quantities in `g`. Only the state of a fixed cell escapes.
   - So r3:522–524 ("F4 admits … GR:374–380's `H`-dependent part, under §8.3") contradicts F4-7 for the channel as the corpus describes it.
3. **Reading 1's adiabatic curvature response.** GR:400 describes it as a response to the local curvature, a different mechanism. The corpus specifies no classical counterpart for it. "Its covariation with `H` is ⊳_D" (r3:522) assumes the counterpart is a microstate quantity defined independently of the metric. That is not shown. The status is undetermined, not admitted.

**Resolution.** Under §8.3, F4's treatment of these pieces depends on what the classical counterpart is:

| The counterpart is … | Under F4 |
|---|---|
| a fixed-cell microstate quantity, as in GR:573's examples | admitted |
| a total over the hidden sector, as GR:374 and GR:378(i) describe the running channel | excluded, by F4-7 |
| not used, with the item taken to be the emergent computation as defined | excluded, by N3′ |

The corpus fixes none of these for epoch-differential pieces. So the right statement is "undetermined", with the running-vacuum channel leaning toward exclusion on the corpus's stated mechanism. Neither r3's "admitted" nor CONFIRM-BG-r2's unconditional "excluded" is right.

One further point. U1r5:504–505 places §8.3's identification within the geometry-first proposal (GR:573–579; P17), whose "What does not gravitate" half (GR:575) is excluded. Using GR:573 as a branch condition is consistent with unit 2(a)'s two-branch treatment. The branch should be labelled as conditional on that posit.

***

## 4. New material

**F4-7 (the label escape fails; r3:553–557).** Sound [P].

- A count, total or density over a set is grounded partly in the facts about which cells are members of the set. Under N1–N2-G those membership facts are grounded in `g`.
- `T^cl`, the total over the whole microstate, is not selected by the partition, so it correctly escapes.
- The node also corrects r2's Substratum.md row, which was "grounding in the classical dynamics of the cells that the metric picks out". That wording has been dropped (r3:308).
- F4-7 bears on §8.3 as well (CF-2).

**F4-8 (running-vacuum channel; r3:558–567).** The cost reading is correct on the present premise base. Two parts need correction:

- (a) The branch restriction "without §8.3" does not hold for the channel's hidden-sector-volume dependence (CF-2).
- (b) "That branch's outcome would be (B)" contradicts the rule as applied in §5 and §7 (CF-1).
- Also, GR:354's "a structural reading, not a derived law" is said of "the Type II channel" (matter conserved, compensation through running `G`). It is not said of the running-vacuum form as such. GR:374 also calls "some state dependence on cosmological geometry" required ("The defensible statement is that boundary architecture requires …"). That statement concerns the emergent vacuum energy's dependence, not its sourcing, so it does not turn the cost into a (b2) rejection. But r3 should cite it, and should base the non-premise status on GR:400's non-adjudication and GR:633's "not derived" rather than on GR:354 (CF-6).

**F4-null (r3:196, :549–550).** Correctly classed as CoC-content with respect to the witness's term.

- `g_μν k^μ k^ν = 0` is algebraic, so the null flux of `ρ g` vanishes on every route.
- F4-null therefore reaches the witness on neither route. That makes BG-F5's "F4-null reaches only the first" wrong (CF-3).

**Quotations and citations in the changed hunks.** All of the following are accurate:

- GR:374, GR:378(i), GR:384, GR:400 (both readings), GR:426, GR:528–530, GR:532, GR:633;
- SM:160 ("(iii) is a definition and (iv) an identity");
- U1r5:222–225 and U1r5:506;
- U2Ar3:303–304, U2Ar3:469, U2Ar3:548–549 and U2Ar3:696.

Small inaccuracies are listed in CF-6.

RESP's r3 pointers resolve, except "GR:695 is dropped (r3:324, r3:531)". r3:531 is in the §8.3 dispute; the GR:695 line is r3:517.

***

## 5. Verdict and its scope

"(C), Reading G, case β, conditional on N5-G, residual F4 against F5" is exactly supported.

"Partly reducing to G3" is weaker than r3:95–97 and :631–632 state:

- F4 as stated reaches the witness on both routes.
- F4-null reaches it on neither.
- The route bears on which scope is the natural one (the null flux is the source input of the Jacobson route). It does not decide reach, given a scope (CF-3).

***

## 6. Owner questions QB1 to QB7

- **QB1 to QB6.** Well posed. QB6 correctly says "repaired twice".
- **QB7(a).** Misstates the consequence. Holding the channel as a premise rejects uniform F4, but the outcome is (C) with K3 named, unless no grounded carve-out exists or carved F4 is dropped as a formalization (CF-1). The branch qualifier "without §8.3" is too narrow (CF-2).
- **QB7(b).** Framed as "this record's reading … CONFIRM-BG-r2's". It should state the content as the three cases of §3 above.
- **Missing.** Nothing else, provided QB5(a)'s audit list is taken to include specifying the carved F4 and GR:577's scope clause.

***

## Should-fix

### CF-1. F4-8 and QB7 state (B) where the rule as applied gives (C) with K3 named

**Where.** r3:558–561; r3:776–778; RESP:15–16, :96–97, :144–145; N3:74–76.

**Evidence.**

- §5 and §7 count a carved F4 as a grounding-content formalization with K3 undetermined (r3:476, :480–481, :619).
- If the channel is held as a premise, uniform F4 is rejected by (b2). The carved F4 is, by construction, an F4 that admits the corpus's metric-dependent sources, so the channel premise does not touch it.
- By r3:220–222, an undetermined control that decides the outcome gives (C) with the control named.
- r3 cannot both count the carved F4 in §7 and ignore it in F4-8.

**Fix.**

1. Add the carved F4 to §1.3:

   > "F4-c (carved sourcing as grounding). As F4, except that a stated class of metric-defined terms is not grounding while the witness's term is; grounding-content. No class with a difference relevant to grounding is stated (§6 node F4-5), so its K3 is undetermined."

2. Replace "If the channel were a stated premise, F4 would be rejected by (b2) in that branch, and that branch's outcome would be (B)" (r3:560–561) with:

   > "If the channel were a stated premise, uniform F4 would be rejected by (b2). F4-c, whose K3 is undetermined, would then decide the outcome, which by §1.4 is (C) with K3 named. It becomes (B) only if no grounded carve-out exists."

3. Restate QB7(a), RESP:15–16, :96–97, :144–145 and N3:74–76 to match.

### CF-2. The §8.3 relocation is undetermined, not an admission; for the running-vacuum channel it conflicts with F4-7

**Where.**

- r3:79–85;
- r3:316;
- r3:518–532;
- r3:540–541;
- r3:558–559;
- r3:572–573;
- r3:655–657;
- r3:715;
- r3:779–780;
- RESP:68–91.

**Evidence.** See §3 above:

- the scope stated at GR:573 and GR:577;
- the mechanism stated at GR:358, GR:374 and GR:378(i);
- F4-7;
- U1r5:504–506.

**Fix.**

1. Replace the first sub-bullet of the §8.3 paragraph (r3:519–524) with:

   > "§8.3 states that relative differences correspond to a classical microstate difference and 'appear in the classical stress-energy tensor' (GR:573), for differences 'determined by the visible data' (GR:577). What F4 does under §8.3 depends on the counterpart. A fixed-cell microstate quantity is admitted. A total over the hidden sector is excluded by F4-7, and that is how GR:358, GR:374 and GR:378(i) describe the running channel's `H`-dependence ('depending on the hidden sector's volume'; 'via `A = 4πc²/H²`'). With no relocation, the emergent computation as defined is excluded by N3′. The corpus fixes the counterpart for no epoch-differential piece (U1r5:506), so under §8.3 the status is undetermined. For the running channel it leans to exclusion on the corpus's stated mechanism. The §8.3 branch rests on the geometry-first identification (U1r5:504–505)."

2. In §0 (r3:79–85), move "the `H`-dependence of the running-vacuum source (GR:374–380)" to a third heading: "**Undetermined with §8.3 in force:** GR:400 Reading 1 and the running channel's `H`-dependence (§6 node F4-5)."
3. Make the following matching edits:
   - Change "without a classical microstate counterpart" (r3:541, :572–573) to "without a fixed-cell classical counterpart".
   - At r3:655–657, write "a relative piece whose classical counterpart is a fixed-cell microstate quantity".
   - At r3:715, list Reading 1 and GR:374–380 as "excluded without §8.3; undetermined with it".
   - Restate QB7(b) as: "Under §8.3, is a relative epoch-differential piece's gravitating item a fixed-cell microstate quantity, a hidden-sector total, or the emergent computation as defined?"

### CF-3. F4-null reaches the witness on neither route; the route does not "decide" F4's scope

**Where.** r3:95–97; r3:456–458; r3:631–632; r3:681; BG-F5 at r3:714.

**Evidence.**

- The null flux of `ρ g_μν` vanishes algebraically on every route. r3:550 itself classes F4-null as CoC-content with respect to the witness's term.
- BG-F5's "F4 as stated reaches both, and F4-null reaches only the first" is therefore wrong in its second clause.
- What the route bears on is which scope is the natural one. On the Jacobson route the null flux is input (iii). On a 𝒞_div law the whole right side is the source.

**Fix.**

1. BG-F5's last sentence should read:

   > "G3's route decides whether the witness's dependence sits in a source term or in the selection of the integration constant. F4 as stated reaches both; F4-null reaches neither. The route bears on which scope is natural, and does not fix it."

2. Replace "It therefore decides which scope of F4 is at issue" (r3:95–96) and "and so which scope of F4 is at issue" (r3:631–632) with "and so bears on which scope of F4 is natural; reach is fixed by the scope, which the premise base does not fix".
3. At r3:456–458, write "Only F4-null leaves the witness unreached, on either route."

### CF-4. r3's own edits to §1.2 and §1.3 are not recorded

**Where.** r3:127; §1.2 at r3:160–176; §1.3 at r3:192–194.

**Evidence.** A `diff` of r2:124–211 against r3:137–229 shows these r3 edits outside R-4 and R-5:

- **Content definitions.** The classification is now "with respect to the witness's term". Grounding-content is "by that term", where r2 had "by its source term". CoC-content is "that term does not ground the metric", where r2 had "it includes no such grounding". The edit is substantive: it is what classes F4-null as CoC-content (r3:549–550).
- **Clause (A).** It drops "On Reading G (N5-G, case β) the witness is then excluded by the content of its law".
- **Clause (C).** "stated precisely" becomes "stated".
- **F4's §1.3 statement.** "the energy content of its source term" becomes "the energy content of every term of the realized equation other than the Einstein tensor". That is BC-2's scope change, and it is recorded only as "R-3 … F4 is added".

r3:127 says that "every later edit [is] recorded in §1.6". None of these edits favours (C).

**Fix.** Add to §1.6:

> "R-6 (r3). §1.2's content classes are relativized to the witness's term, which makes F4-null CoC-content (§6 node F4-6); (A) drops its closing sentence, which restated Lemma U's consequence; (C) 'stated precisely' becomes 'stated'; F4's §1.3 statement is restated on every non-Einstein term of the realized equation (CONFIRM-BG-r2 BC-2)."

Alternatively, restore r2's wording where no change was intended.

***

## Nits

### CF-5. Owner-question framing

**Where.** r3:779–780.

**Evidence.** QB7(b) names the two readings by their authors.

**Fix.** State the content. The CF-2 text above does this.

### CF-6. Quotation precision

- **GR:354.** r3:85, :316, :404, :562 and :776 cite GR:354's "a structural reading, not a derived law" for "that channel". In GR:354 the phrase qualifies "the Type II channel". Write "the Type II channel, 'a structural reading, not a derived law' (GR:354)". Add GR:374's "boundary architecture requires some state dependence on cosmological geometry", noting that it concerns dependence, not sourcing.
- **GR:573.** r3:519 quotes "correspond to". GR:573 has "corresponding to this energy difference".
- **GR:400.** r3:524 and RESP:85 quote "fixed by the substratum budget". GR:400 has "the substratum budget fixes the constant part of `ρ_Λ`".
- **GR:581.** r3:323 elides the qualifier from "a property of the partition geometry … and therefore … does not source curvature". Restore "on the geometry-first proposal of §6.2 and conditional on its open coupling step".

### CF-7. Notes and response bookkeeping

- **Commit status.** N3:17–18 says "The writer did not commit, push or post it". r3 is committed at `7fd16a5d`. Record this in the next NOTES file. It is the third recurrence of the pattern, so the next NOTES should state the commit state at the time it is read.
- **RESP:59.** "r3:531" should be "r3:517".
- **r3:607.** The NEW of pass 7 (BG-F6) was first reported in CONFIRM-BG-r2 BC-3. Credit it: "pass 7 (… ) confirms 1 NEW, BG-F6, reported by CONFIRM-BG-r2 BC-3".

***

## Disposition

ACCEPT WITH CHANGES.

- **Before QB7 is put to the owner:** apply CF-1 to CF-4.
- **With them:** CF-5 to CF-7.
- **Review needed:** a delta check of CF-1 to CF-3 is sufficient. No further full round is needed.

The outcome (C) and its scope stand. Once these changes are applied, the residual is F4 against F5, with F4's scope and cost stated. The §8.3 branch is undetermined for epoch-differential pieces.

No manuscript change is proposed. No premise is adopted.
