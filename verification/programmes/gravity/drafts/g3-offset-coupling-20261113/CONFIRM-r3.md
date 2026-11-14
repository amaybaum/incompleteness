# CONFIRM-r3: delta check of G3 unit 1 r3 against REVIEW-r2

**Verdict: NOT CONFIRMED, two blocking findings.** Both trace in part to wording in REVIEW-r2 (R2-1), which I correct here.

R2-2 to R2-9 are resolved as RESPONSE-r2 states. Both departures from my wording are correct and are not rescues:

- (DZ) is genuinely needed. It needs a stated domain (C-3).
- "Not read back from the field equation" is the right precision.

The delta from `1aaf87a2` touches only what RESPONSE-r2 lists.

The two blocking findings are both in the verdict text:

- **C-1.** Part 1 says "(SI) is not implied on any reading of (ii)", but the draft's own (ii-S) excludes the witness K_cpl^free.
- **C-2.** Part 2 rests on "the corpus's use (GR:400 Reading 1) admits a loop through post-partition data". GR:400 classes the piece it feeds back as a relative effect "in the sense of §8.3", which the corpus identifies with a classical microstate difference (GR:573). REVIEW-r2 R2-1 asserted "a loop of the same form" without accounting for that qualifier. The corpus's use therefore does not establish that it admits K_cpl^conv, whose offset is absolute (GR:575). For the same reason, F8 is ELABORATING, not NEW (C-6).

**Target.** Branch `research/g3-offset-873-20261113` at `b207fbaaff23988c6bdf1330f4b7e993bee4e5e9`.

- The parent `25257ae5` adds REVIEW-r2, byte-identical to the review as issued (checked with `diff`).
- The r3 head adds G3-UNIT1-r3.md, NOTES-r3.md and RESPONSE-r2.md.
- `git diff --name-status 1aaf87a2 b207fbaa` shows four additions and no modification. The r1 files, the r2 files, RESPONSE-r1 and REVIEW-r1 are unchanged.
- `diff G3-UNIT1-r2.md G3-UNIT1-r3.md` has 42 hunks, each inside a row of RESPONSE-r2's delta table (RESPONSE-r2:109–139). No change falls outside the table.

Corpus lines refer to `main` at `c3b5f37a`. "r3:n" means G3-UNIT1-r3.md line n, and "N3:n" means NOTES-r3.md line n.

**Checks at `b207fbaa`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check b207fbaa…` | 303 records intact |

None of them scans the drafts.

***

## Blocking

### C-1. Part 1 says "any reading", but (ii-S) excludes K_cpl^free

**Where.** Part 1 at r3:40 and r3:527, with the same claim at r3:357 (§3.2 row), r3:489 (node verdict), r3:593 (O0), F1 at r3:619 and F8 at r3:626.

**Evidence.** r3:460–462 defines (ii-S) and states: "(ii-S) excludes K_cpl^free and K_cpl^conv, and every `λ ≠ 0` in either family [A]. Under (ii-S), (SI) and (DZ) for the uniform term hold at fixed `κ`."

The witness of Part 1 is K_cpl^free, and its law has the argument e_free(r). That argument is a coordinate on the σ-orbit of a post-partition object, which is exactly what (ii-S) forbids. "Not implied on any reading" and "survives (ii) on every reading" therefore contradict r3:460–462.

The phrase "on every reading" comes from REVIEW-r2 R2-1. There I meant GR:346 as argued and as used, and that review did not separately consider (ii-S).

**Fix.** At r3:40 and r3:527, replace "on any reading of requirement (ii)" with:

> "on the weak and loop readings of requirement (ii) ((ii-W), (ii-L)); under the strong reading (ii-S), which corresponds for the source to GR:400 Reading 2, (SI) follows conditionally"

At r3:357, r3:489, r3:593, F1 (r3:619) and F8 (r3:626), replace "every reading" with "(ii-W) and (ii-L); excluded by (ii-S)".

### C-2. Part 2's "as the corpus uses it" basis does not account for GR:400's own "relative" qualifier

**Where.** Part 2 at r3:45–49 and r3:529–531; the corpus-use bullets at r3:472–483; the node verdict at r3:490–493; AW-loop at r3:62–63 and r3:644–648; O0 at r3:595; O1 at r3:606–608; F8 at r3:626; Q7 and Q8 at N3:97–105.

**Evidence.**

- GR:400 Reading 1 describes the fed-back piece as "the emergent layer's curvature response — the ∼m²H² piece that survives adiabatic renormalization precisely because it is an epoch-differential (relative) effect in the sense of §8.3".
- §8.3 (GR:573) says relative differences gravitate because "there is a classical microstate difference corresponding to this energy difference … Relative differences appear in the classical stress-energy tensor". GR:575 places absolute levels assigned by the emergent description on the other side, as "not a property of the microstates themselves".
- GR:358 has the same split. Feedback runs "through state-level quantities", while "the zero-point sum" is excluded.

On the corpus's own account, then, what Reading 1 feeds back is the emergent computation of a quantity that has a classical counterpart. That is a classical source evaluated through the emergent description. It is not a loop through data that exist only after the partition. GR:346 forbids the latter ("If the metric were derived from QM"). On this reading Reading 1 and GR:346 are reconciled, and the corpus's use admits nothing for absolute emergent quantities.

K_cpl^conv's e_Z is the absolute ground eigenvalue (GR:332, GR:358), which GR:575 classes as having no classical counterpart. The corpus's use therefore does not establish that it admits K_cpl^conv. K_cpl^conv survives only under (ii-W) applied to absolute emergent quantities, and no corpus text adopts that reading.

Two qualifications apply.

1. The reconciliation rests on §8.3's identification of relative emergent effects with classical microstate differences. That identification is part of the geometry-first proposal and is conditional (GR:573–579; P17).
2. GR:358 and GR:374 speak of "the emergent vacuum energy". So the textual tension that AW-loop records is real at the level of wording. It is removable by §8.3's conditional identification and is not a structural blind spot (see C-6).

REVIEW-r2 R2-1 item 3 ("a self-consistent loop of exactly GR:346's form") overstated GR:400. This finding corrects it.

**Fix.**

1. **Part 2.** Restate Part 2 (r3:45–49 and r3:529–531) as:

   > "K_cpl^conv, the coupled completion with physical content, violates (DZ). It is excluded by (ii-S) and by GR:346 as argued (ii-L). It is not admitted by the corpus's use, which feeds back only a piece GR:400 classes as relative in the sense of §8.3 (GR:573), conditional on that identification. K_cpl^conv is compatible with OI's results only under (ii-W) applied to absolute emergent quantities, a reading no corpus text adopts. (DZ) for the convention-fixed offset therefore follows conditional on GR:346's argument (ii-L) [P]. Whether that argument holds against self-consistent fixed points is not established; it is a derivation-order requirement, not a proof that no fixed point exists."

   Choose the verdict category for Part 2 accordingly. "Conditional on (ii-L)" fits the evidence better than "counterexample".
2. **The corpus-use bullets and the node verdict.** Replace r3:478–480 and r3:490–493 with the §8.3 analysis above.
3. **AW-loop.** Rewrite AW-loop (r3:62–63, :644–648) as:

   > "GR:346 and the wording 'emergent vacuum energy' at GR:358, GR:374 and GR:400 are in apparent tension. GR:400's own qualifier ('relative … in the sense of §8.3') reconciles them, conditional on §8.3's identification of relative emergent effects with classical microstate differences (GR:573), which is part of the geometry-first proposal. The reconciliation is not stated at GR:346."
4. **The owner questions.**
   - In Q7 (N3:97–100), the cost "removal of GR:400 Reading 1" holds only if that identification fails. Otherwise holding (ii-L) leaves Reading 1 standing.
   - Restate Q8 (N3:101–105) to match.
5. **O0 and O1.** Update O0 (r3:595) and O1 (r3:607–608) to match.

***

## The two departures (brief item 2)

### D-1. (DZ) in place of "(SI) for the convention-fixed offset": accepted; C-3 below must be applied

- **Correct and needed.** e_Z is a function of the operational class [r], and σ_C leaves [r] fixed. So K_cpl^conv satisfies (SI) and (SI′), as r3:323–325 states [A]. My phrase in REVIEW-r2 was wrong.
- **Not a rescue.** (DZ) is the proposition GR:352's contrast concerns: whether the zero-point sum gravitates. It is preregistered in §2 before it is used, it is not adjusted to fit any outcome, and Part 2's verdict under it is conditional either way.
- **Directionality kept.** (DZ) ⇒ (TL) is trivial, and only the forward direction is posed (r3:221–222).

### D-2. "Fixed by the emergent class and not read back from the field equation": accepted

"Independently of the metric" would contradict the loop, because e_Z depends on [r], [r] on the partition, and the partition on the metric (GR:346). The replacement keeps the contrast I intended, a convention fix as opposed to a read-back from the field equation.

***

## Should-fix

### C-3. (DZ) needs a stated domain

**Where.** r3:215–218, r3:323–325, r3:364.

**Evidence.** (DZ) is "the source is constant in `e_Z`", with the source written "as a function of `(T^cl, g, e_Z)`", and K_cpl^conv's violation is a response "at fixed `T^cl`". At fixed κ, both T^cl and e_Z are fixed, as r3:364 itself says: "At fixed `κ` nothing differs". So (DZ) is a statement across classical data.

That variation needs pairs κ, κ′ with T^cl(κ) = T^cl(κ′) and e_Z(κ) ≠ e_Z(κ′). Their existence is not shown. By GR:573 the relative differences that fix the gaps "appear in the classical stress-energy tensor", so a change of gaps at fixed T^cl may not occur. The "[A]" on the violation presupposes it does.

**Fix.** Define (DZ) without requiring independent variation:

> "(DZ): the source minus `T^cl` contains no dependence on `e_Z([r])`, with `T^cl` given by the classical assignment (P11, W1-0)."

Then K_cpl^conv violates (DZ), since its source minus T^cl is −ρ_Z g, and K_dec satisfies it, without any claim about κ-space. Drop "at fixed `T^cl`" at r3:323–325 and r3:364, or mark it conditional on the existence of such pairs.

### C-4. "World-equivalent to K_dec" needs a qualifier

This wording comes from REVIEW-r2.

**Where.** r3:41–42, r3:340–341, r3:489, r3:527–528, F8.

**Evidence.**

- K_dec at a fixed Λ₀ admits only metrics with Λ_eff = Λ₀.
- K_cpl^free at a fixed Λ^free_1 admits a metric for every value of Λ_eff, one for each origin coordinate.
- So K_cpl^free(Λ^free_1) admits the worlds of the union of K_dec(Λ₀) over all Λ₀. That is K_dec with Λ left undetermined, which is the corpus's standing for Λ (GR:162, GR:334, GR:356).
- It does not admit the worlds of K_dec at one fixed Λ₀.

**Fix.** At each place, replace "world-equivalent to K_dec" with:

> "world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356)"

### C-5. "(DZ) … follows at fixed `κ`" is incoherent with r3:364

**Where.** r3:537–538.

**Evidence.** At fixed κ, e_Z is fixed, so "(DZ) at fixed κ" has no content.

**Fix.** Replace "at fixed `κ`" with "for the uniform term". After C-3, (DZ) is a property of the source map.

***

## Classification of F8 (brief item 4)

### C-6. Reclassify F8 from NEW candidate to ELABORATING

- **Search.** I found no record of the GR:346 / GR:400 tension. My search over `papers/`, `book/` and `verification/` for "no entry point", "non-circularity", "Reading 1", "Reading 2" and "strict geometry-first" returns only GR:346 and its book mirrors, GR:400, and unrelated uses of "non-circularity" (GR:154, oi-qm ANALYSIS).
- **Why not NEW.** GR:400 itself supplies the reconciliation by classing the fed-back piece as relative in the sense of §8.3 (C-2). So the finding is that the reconciliation is conditional on §8.3 and is not stated at GR:346. That is stronger than a restatement, and it bears on Q7's stated cost, but it is not a structural blind spot.
- **Fix.** Class: "ELABORATING (assumption-watch AW-loop: the GR:346 / GR:400 reconciliation is conditional on §8.3 and unstated)".

***

## Resolution of R2-2 to R2-9 (brief item 1)

| Finding | r3 | Status |
|---|---|---|
| R2-1 | as above | Applied. Corrected by C-1, C-2, C-4 and C-6. Parts of R2-1's own wording were wrong (C-1, C-2, C-4). |
| R2-2 | r3:333–336 | Resolved, verbatim. |
| R2-3 | r3:328–329 | Resolved. |
| R2-4 | F5, r3:623 | Resolved. |
| R2-5 | r3:281–282, :388–389, F2 at r3:620 | Resolved. |
| R2-6 | r3:606–608 | Resolved in form. Its "for K_cpl^free" clause inherits C-1, and its K_cpl^conv clause inherits C-2. |
| R2-7 | r3:182–183 | Resolved. |
| R2-8 | r3:576–577 | Resolved. |
| R2-9 | r3:485 | Resolved. |

## Verdict text (brief item 3)

§0 and §5 overclaim in three places:

- "any reading" (C-1);
- "compatible … as the corpus uses it" (C-2);
- "world-equivalent to K_dec" without the qualifier (C-4).

Neither section makes any other new overclaim, and no new premise is adopted.

## Register

The drafts contain no §A.32 or §A.33 phrases and no barred path strings. The only hit for "cheaply" is RESPONSE-r2:103, which quotes the replaced word.

***

## Disposition

NOT CONFIRMED.

- **C-1 and C-2 are blocking.** The fixes are textual, but C-2 changes the verdict basis for Part 2, and probably its category.
- **C-3 to C-5 are should-fix, and C-6 is a reclassification.**

A delta check of the lines listed above is enough for confirmation. No manuscript change is proposed.
