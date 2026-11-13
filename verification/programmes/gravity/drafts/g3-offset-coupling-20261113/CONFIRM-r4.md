# CONFIRM-r4: delta check of G3 unit 1 r4 against CONFIRM-r3

**Verdict: CONFIRMED, with two should-fix precisions and one nit. Nothing is blocking.**

- C-1 to C-6 are resolved as RESPONSE-r3 states.
- The added epoch caveat is correct in direction and does not overclaim. One sentence misattributes what AUDIT item 2.9 says (D-1).
- The verdict text in §0 and §5 has no overclaim. F1's summary line needs one scope clause (D-2).
- Nothing outside RESPONSE-r3's delta table changed.

D-1 to D-3 can be applied without another review round.

**Target.** Branch `research/g3-offset-873-20261113` at `e0383e50234143dfb7d184980e525713e9e6ff08`.

- The parent `95681321` adds CONFIRM-r3, byte-identical to what I issued (checked with `diff`).
- `git diff --name-status b207fbaa e0383e50` shows four additions: CONFIRM-r3.md, G3-UNIT1-r4.md, NOTES-r4.md and RESPONSE-r3.md.
- All earlier files are unchanged: G3-UNIT1 r1–r3, NOTES r1–r3, RESPONSE-r1, RESPONSE-r2, REVIEW-r1 and REVIEW-r2.
- `diff G3-UNIT1-r3.md G3-UNIT1-r4.md` has 28 hunks. Each lies inside a row of RESPONSE-r3's delta table (RESPONSE-r3:119–145):
  - r3:525–531 covers the hunks at 525 and 527–531;
  - r3:536–542 covers the hunks at 536, 539 and 541–542.

  No hunk falls outside the table.

Corpus lines refer to `main` at `c3b5f37a`. "r4:n" means G3-UNIT1-r4.md line n.

**Checks at `e0383e50`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check e0383e50…` | 303 records intact |

None of them scans the drafts. In the drafts, a grep finds no barred strings, no §A.32 or §A.33 phrases, and no "every reading" or "any reading".

***

## Resolution of CONFIRM-r3

| Finding | r4 | Status |
|---|---|---|
| C-1 | §0 r4:42–46; §3.2 r4:369; B5 r4:475–476, :526; §5 r4:564–566; R0; O0 r4:633–634; O1 r4:652; F1; F8 | Resolved. "Every/any reading" no longer appears. (ii-S) excludes K_cpl^free, and under (ii-S) (SI) follows conditionally, consistently throughout. |
| C-2 | §0 r4:47–56; B5 r4:488–530; §4 r4:543; §5 r4:567–570; R0 r4:580–582; O0 r4:635–644; O1 r4:653–654; F8; AW-loop r4:70–73, :690–699 | Resolved. Part 2 is recategorized as "conditional on (ii-L)". The reconciliation through §8.3 is stated as conditional. O0 now separates the open proof question (the force of (ii-L) against fixed points) from the owner's premise decision. Q7's cost is restated correctly ("only if §8.3's identification fails"). |
| C-3 | r4:225–227, :334–336, :376–379 | Resolved. (DZ) is a property of the source map. K_cpl^conv violates it through −ρ_Z g, and K_dec satisfies it. The claim about κ, κ′ pairs is conditional. |
| C-4 | r4:45, :352–354, :526, :565, :577–578, :633–634, F8 | Resolved. The added reason ("at a fixed Λ^free_1, K_cpl^free admits a metric for every value of Λ_eff") is correct [A]. |
| C-5 | r4:475–476, :575–576 | Resolved. The same correction was also applied to the (ii-S) bullet. |
| C-6 | F8 r4:672; r4:532–533 | Resolved. F8 is ELABORATING, and the count sentence is corrected. |

## The added caveat (brief item 2)

The caveat (r4:505–508, AW-loop r4:697–698, NOTES-r4 §3 item 2) is correct in direction and labelled [P]. It does not overclaim.

- It strengthens the conditional character of the reconciliation.
- It leaves C-2's conclusion unchanged. Even if the reconciliation failed, the corpus's use would not admit K_cpl^conv, because Reading 1 removes the constant part by stipulation (r4:515–517). The caveat therefore bears only on whether (ii-L) is consistent with Reading 1, which is what Q7 and Q8 already carry.

D-1 records one imprecision of attribution.

***

## Should-fix

### D-1. The caveat misstates what AUDIT item 2.9 records

**Where.** r4:505–508; AW-loop r4:697–698; NOTES-r4 §3 item 2.

**Evidence.**

- AUDIT.md:374–376 (item 2.9) says the electroweak and QCD transitions "are differences between two configurations occupied at different epochs, so by GR:579's wording they are relative", and that the "absolute" classification at GR:581 is an added assumption.
- GR:579 says only that how the energy of those transitions couples "is not fixed by the relative/absolute distinction".

So the record does not say that classing an epoch-differential term as *relative* lacks support. By the rule's wording it is relative. What the rule leaves undecided is the step from relative-between-epochs to "a classical microstate difference that gravitates". The phrase "between epochs" also comes from AUDIT.md:375, not from GR:579 or from the table row at AUDIT.md:55.

**Fix.** Replace the second and third sentences of r4:505–508 with:

> "GR:579 records that the relative/absolute rule does not fix how the energy of the electroweak and QCD transitions couples. AUDIT item 2.9 (AUDIT.md:371–378) notes that, by the rule's wording, such between-epoch differences are relative. By analogy, the step from an epoch-differential vacuum term being relative to its being a classical microstate difference that gravitates, which §8.3 asserts for relative effects, rests on GR:400's statement and not on a derivation."

Apply the same change to AW-loop and NOTES-r4 §3 item 2. Cite AUDIT.md:371–378 in place of AUDIT.md:55.

### D-2. F1's summary line needs a scope clause

**Where.** F1 at r4:665 ("The non-implication at GR:352 holds, in the two-part form of §0").

**Evidence.** The data GR:352 lists are substratum, partition, reduced law, fixed-basis representation and calibration. Its own section (GR:342–348, the same §6.2) also contains requirement (ii). Part 2 of r4 states that, on GR:346 as argued, the contentful coupled completion is excluded and (DZ) follows. So GR:352's non-implication holds relative to its listed data. For the coupling with physical content, it holds only if (ii-L) lacks force against self-consistent fixed points, which is open.

The rest of r4 already says this. F1's first sentence does not.

**Fix.** Change F1's first sentence to:

> "The non-implication at GR:352 holds relative to the data GR:352 lists. With the ordering requirements of the same section (GR:342–348) included, it holds in the two-part form of §0: for source maps on (ii-W) and (ii-L), and for the coupling with physical content only if (ii-L) lacks force against self-consistent fixed points (open)."

Optionally, add a one-line note to AW-loop or to Q1: GR:352 calls decoupling open at G3, while GR:346 as argued, in the same section, would settle (DZ) conditionally.

## Nit

### D-3. The citation for T^cl in the definition of (DZ)

**Where.** r4:226.

**Evidence.** "`T^cl` given by the classical assignment (P11, W1-0)" cites P11, the source posit. That reads as if (DZ) imported the posit, under which (DZ) would hold trivially. The intended reference is only the definition of T^cl.

**Fix.** Replace "(P11, W1-0)" with "(the classical stress-energy of the total microstate, GR:340; W1-0)". This wording originated in my C-3 text.

***

## Verdict text (brief item 3)

- **§0 (r4:38–56).** No overclaim.
  - Part 1 is scoped to source maps on (ii-W) and (ii-L), with (SI) conditional under (ii-S), and with the world-equivalence qualified.
  - Part 2 is "conditional on (ii-L)", with the open force of (ii-L) against fixed points stated.
  - "No corpus text adopts" (ii-W) for absolute quantities is a negative claim. It is consistent with the corpus search recorded in CONFIRM-r3 and with GR:575 and GR:400.
- **§5 (r4:562–570).** It matches §0, and NOTES-r4 §4 matches both.
- **Support labels.** [A] is used for the source-map algebra and [P] for the readings of paper arguments. No premise is adopted, and R0 and Q7 remain owner decisions under §A.29.

## Disposition

CONFIRMED with D-1 and D-2 (should-fix) and D-3 (nit). All three are textual, and no further review round is needed for them. No manuscript change is proposed.
