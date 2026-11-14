# CONFIRM-BG-r4: delta check of G3 unit 2(b) r4 against CONFIRM-BG-r3

**Verdict: ACCEPT WITH CHANGES.** Nothing is blocking. There are three should-fix findings and one nit.

The changes are textual, and replacement text is given for each. Once they are applied, no further review round is needed: checking the edits against the replacement text is enough. QB7 can go to the owner once DF-3 is applied.

**What holds.**

- **CF-1 to CF-7.** All are resolved at the cited lines.
- **The three-case §8.3 table** (r4:566–572). It is correct and correctly sourced.
- **The withdrawal** of r3's "admitted" argument (r4:722–724). It is clean.
- **The rule's clauses.** §1.1–§1.5 are unchanged from r3, apart from the two §1.3 additions that R-6 and R-7 account for. I checked this with `diff`.

**What needs changing.**

- **The new claim at r4:598–600 is mis-scoped (DF-1).** Unit 2(a)'s "same kind" finding concerns the *R-dependence* of the witness. Under §8.3, F4 excludes the witness through its *absolute* realized value (r4:586–588). A carve-out that admits the running channel therefore does not have to separate same-kind quantities. It has to admit both `H`-dependences and separate them from the absolute part, and that is the relative/absolute question already listed at r4:594–595.
- **R-7 tilts how reachable (A) and (B) are (DF-2).** It makes (B) depend on a universal negative. §7 also omits F4-null, which r4 itself classes as CoC-content. Counting F4-null restores the symmetry.
- **QB7(a) needs one qualifier (DF-3).** QB7(b) can go as written.

**Target.** Branch `research/g3-offset-873-20261113` at `297ee2466801690368c0a307cf5881663d2fcd4e`, parent `651849ab`.

- The commit adds exactly three files: G3-UNIT2B-BG-r4.md (889 lines), NOTES-BG-r4.md (102) and RESPONSE-BG-r3.md (199).
- `651849ab` adds CONFIRM-BG-r3.md, byte-identical to the review I issued (`cmp`).
- `diff` of r3 against r4 gives 37 hunks, which matches RESPONSE §3. The hunk list agrees with RESPONSE's delta table.
- A grep of the three files finds no barred path strings.
- Line references: "r4:n" is G3-UNIT2B-BG-r4.md, "RESP:n" is RESPONSE-BG-r3.md, "N4:n" is NOTES-BG-r4.md, and "U2Ar3:n" and "U1r5:n" are the unit 2(a) r3 and unit 1 r5 records. Corpus lines refer to `main` at `c3b5f37a`.
- I worked by hand reading only, did not compute on OI rules, and adopt no premise.

***

## 1. CF-1 to CF-3

### CF-1: resolved

**F4-c and the outcome.**

- F4-c is listed in §1.3 (r4:213–219) and recorded as R-7 (r4:300).
- F4-8 now gives the right consequence: (C) with K3 named (r4:635–640).
- The same consequence appears consistently at r4:111–113, :520–521, :697–698, :714–716 and :869–872.

**F4-c as a schema.**

- The schema reading is coherent. The rule judges F4-c by whether some class with a difference relevant to grounding exists, and R-5's clause for undetermined controls (r4 §1.4) gives that open question a definite effect on the outcome.
- It does carry a consequence the record should state. If uniform F4 is rejected, (B) needs a proof that *no* grounded class exists, which is a universal negative (DF-2).

**The writer's reading of K3** (N4:49–53; RESP:30–36).

- N4 reads: "K3's wording ('without a stated difference … fails K3') would fail any specific carve already stated". That wording is looser than K3.
- K3 fails a carve only when no difference relevant to grounding is stated for it. Each carve stated so far lacks such a difference, which is why each fails.
- r4 §1.3 states this correctly ("Each candidate class examined so far fails"), so nothing in r4 depends on the loose wording (DF-4).

### CF-2: resolved

**The three-case table** (r4:566–572) is correct. I checked each row against its sources:

- **Row 1: admitted.** A fixed-cell microstate quantity falls outside N3′, which concerns definition (r4 §2.2). Its covariation with `H` is ⊳_D, and K5 separates ⊳_D from ⊳_G.
- **Row 2: excluded by F4-7.** A total over the partition-selected set is grounded in the set's membership, and through N1–N2-G in `g`.
- **Row 3: excluded by N3′.** This holds for the emergent computation as defined.

**The surrounding text** is accurate and correctly sourced:

- The running channel's mechanism quotes GR:374 verbatim ("a state-level quantity depending on the hidden sector's volume"), and cites GR:358 and GR:378(i).
- Reading 1's counterpart is stated as unspecified.
- U1r5:506 is quoted verbatim.
- The branch scope cites U1r5:504–505, with GR:575 excluded.
- The witness's exclusion in either branch (r4:586–588) follows U2Ar3:469 and U1r5:222–225.
- GR:573 and GR:577 are quoted verbatim (r4:560–565).

**Propagation** is complete: r4:88–92, :350, :352, :437–438, :602–604, :624–627, :647–649, :746–748, :806 and :873–875.

### CF-3: resolved

- F4-null reaches the witness on neither route: r4:79–80, :494–495, :611–613 and :805.
- The route "bears on" which scope is natural, and reach is fixed by the scope: r4:105–108, :496–498, :614–617, :710–713 and :772.
- r4:211–212 records F4-null as CoC-content with respect to the witness's term.

***

## 2. CF-4 to CF-7, briefly

- **CF-4: resolved.** R-6 (r4:290–299) records exactly the four r3 edits I listed. The provenance note (r4:141–146) names R-1 to R-7 with their timing. §1.1–§1.5 are otherwise unchanged at r4.
- **CF-5: resolved.** QB7(b) states content, not authorship (r4:873–875).
- **CF-6: resolved.**
  - GR:354 is now attached to "the Type II channel" (r4:96, :442, :634).
  - GR:374's "boundary architecture requires some state dependence on cosmological geometry" is cited as a statement about dependence (r4:93–94, :439–440, :629–630).
  - GR:573 is quoted verbatim.
  - The non-verbatim GR:400 phrase is gone.
  - GR:581's qualifier is restored (r4:357, :590–591).
- **CF-7: resolved.**
  - The commit-state table and the convention are at N4:13–26.
  - The pointer correction is at RESP:144.
  - BG-F6's credit is at r4:683–684 and :806.

***

## 3. The claim at r4:595–600

**What r4 says.** "For the running channel in particular, a carve-out that admits it and excludes the witness must separate two quantities that unit 2(a) found to be of the same kind: emergent vacuum energies depending on `H` through the mode count (U2Ar3:690–693)."

**What U2Ar3:690–693 says.** "The corpus's own emergent vacuum energy … depends on `H` through the mode count. Its loop is the Reading 1 case, and its configuration dependence is of the kind that §4.2 classes as relative. The R-dependence of the witness is the same kind of piece that Reading 1 feeds back."

**Assessment.**

- **Without §8.3** the claim is correct as a statement about the whole quantities. Both are emergent vacuum energies that depend on `H` through the mode count. With no relative/absolute distinction in force, a carve-out that admits one and excludes the other must separate quantities of the same kind.
- **With §8.3** the claim does not hold as stated.
  - Unit 2(a)'s "same kind" finding is about the witness's *R-dependence*, `Δρ_Z`.
  - Under F4, the witness is excluded through its *absolute* realized value. r4:586–588 says so itself: `ρ_Z(R*)` is absolute, with `R₀ = R*` (U2Ar3:469).
  - So under K3 a carve-out that admits the running channel's `H`-dependence must admit the witness's `Δρ_Z` as well. That costs nothing, because the witness's exclusion does not run through `Δρ_Z`.
  - The separation actually needed is between `H`-dependent parts and absolute parts. That is the "relative against absolute" candidate at r4:594–595, which reduces to the counterpart question. A difference defined from metric-defined values is grounded in `g` by N3′, so the split is not by itself a difference relevant to grounding.
- **Net.** The difficulty is real, but r4 locates it in the wrong place. As written, the sentence overstates the case against F4-c in the §8.3 branch (DF-1).

***

## 4. Owner questions QB7(a) and QB7(b)

**QB7(b)** (r4:873–875) is correct and can go to the owner as written. "Under F4 the first is admitted, and the other two are excluded" matches the table.

**QB7(a)** (r4:869–872) gives the right outcome, (C) with F4-c's K3 named, and the right condition for (B). But its premise clause is unqualified: "If it is held, uniform F4 is rejected by (b2)".

- Per F4-8 (r4:636–637), uniform F4 is rejected only where it excludes the channel. That is the case without §8.3, and with §8.3 unless QB7(b) is answered "a fixed-cell microstate quantity".
- In that remaining case uniform F4 admits the channel, holding the channel's sourcing as a premise rejects nothing, and the outcome is (C) for the ordinary reason.
- The outcome stated is still right in every case, but the owner should see how the two questions interact (DF-3).

***

## 5. New errors in the changed hunks

- **DF-1.** The scope of r4:598–600 (§3 above).
- **DF-2.** §7 (r4:699–700) lists F5 as the only CoC-content formalization. But r4:211–212 classes F4-null as CoC-content with respect to the witness's term, under R-6.
- **DF-4.** "Partition-definedness fails K3, because it covers `ρ_Z`" (r4:216–217; also r4:590) misfiles the failure.
  - A class that covers `ρ_Z` makes the witness's term non-grounding, so it is not an instance of F4-c at all, which requires "the witness's term is" grounding.
  - It meets K3 only if `ρ_Z` is removed from the class ad hoc, and that removal then fails K3.
  - There is also a small mismatch of reasons: §0 (r4:69–70) gives "no class … is stated" as the reason K3 is undetermined, while §1.3 (r4:219) gives "not shown to be exhaustive".
- **Quotations.** All other quotations and citations in the changed hunks are accurate: GR:354, :358, :374, :378(i), :400, :573, :577, :581, :633; U1r5:504–506 and :222–225; U2Ar3:469 and :690–693.

***

## Should-fix

### DF-1. The "same kind" sentence is mis-scoped in the §8.3 branch

**Where.** r4:598–600; RESP:80–82.

**Evidence.** See §3 above. The witness is excluded through its absolute part, and unit 2(a)'s "same kind" finding concerns its R-dependence.

**Fix.** Replace r4:598–600 with:

> "For the running channel in particular: without §8.3, a carve-out that admits it and excludes the witness must separate two quantities of the same kind, emergent vacuum energies depending on `H` through the mode count (U2Ar3:690–691). With §8.3, K3 makes it admit the witness's R-dependence too, which unit 2(a) found to be 'the same kind of piece that Reading 1 feeds back' (U2Ar3:692–693). The witness is then excluded only through its absolute part (above), and the separation needed is the relative/absolute one, which reduces to the counterpart question."

### DF-2. State the universal negative behind (B), and count F4-null in §7

**Where.** r4:213–219; r4:520–521; r4:699–700; r4:714–716.

**Evidence.**

- With F4-c as a schema, (B) requires that no grounded class exists. That is a universal negative.
- By R-6, F4-null is CoC-content with respect to the witness's term (r4:211–212, :293–294). Like F4-c, it would also have to be eliminated before (A) could be reached.
- §7 omits it, so the record shows only the grounding side carrying a residual formalization.
- The outcome is unaffected while F5 and uniform F4 are admissible.

**Fix.**

1. In §7, after the F5 line, add:

   > "F4-null is CoC-content with respect to the witness's term (R-6). Its controls are not assessed here; it does not decide the outcome while F5 is admissible, and it would have to be eliminated, with F5, for (A)."

2. After r4:219, add:

   > "(B) through F4-c therefore requires showing that no class with a difference relevant to grounding exists."

### DF-3. QB7(a): qualify the rejection by QB7(b)'s answer

**Where.** r4:869–872 (also r4:111 and r4:714).

**Fix.** Replace "If it is held, uniform F4 is rejected by (b2), and the outcome is (C) with F4-c's K3 named." with:

> "If it is held, uniform F4 is rejected by (b2) wherever it excludes the channel: without §8.3, and with §8.3 unless the answer to (b) is a fixed-cell quantity. The outcome is then (C) with F4-c's K3 named."

Keep the following sentence, "It would be (B) only if no grounded carve-out exists", as it is. Apply the same qualifier at r4:111 and r4:714.

***

## Nit

### DF-4. F4-c's candidate classes: misfiled failure and mismatched reasons

**Where.** r4:216–217; r4:590; r4:69–70; N4:49–53; RESP:30–31.

**Fix.**

1. Change "Partition-definedness fails K3, because it covers `ρ_Z`" (r4:216–217) to:

   > "Partition-definedness covers `ρ_Z`, so it does not yield an F4-c; removing `ρ_Z` from it ad hoc fails K3."

2. Apply the same change at r4:590.
3. At r4:69–70, write "has K3 undetermined, because the candidate classes examined fail and are not shown to be exhaustive".
4. In the next NOTES file, state K3's reading as "K3 fails a carve for which no difference relevant to grounding is stated; each carve stated so far is of that kind".

***

## Disposition

ACCEPT WITH CHANGES.

- DF-1 to DF-3 should be applied before QB7 goes to the owner, together with DF-4. Checking the edits against the replacement text is enough; no further review round is needed.
- The outcome, (C) on Reading G, case β, conditional on N5-G, stands. So does its residual: F4 against F5, with F4's scope and cost stated, and the §8.3 branch undetermined for epoch-differential pieces.

No manuscript change is proposed. No premise is adopted.
