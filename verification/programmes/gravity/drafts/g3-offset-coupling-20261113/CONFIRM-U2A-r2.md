# CONFIRM-U2A-r2: delta check of G3 unit 2(a) r2 against REVIEW-U2A-r1

**Verdict: CONFIRMED, with one should-fix and four nits. Nothing is blocking.**

- **Findings.** U-1 to U-11 are resolved as RESPONSE-U2A-r1 states.
- **The rule.** Applying it after adding Reading G is legitimate: the outcome clauses of §1.2 are byte-identical to r1's, and the outcome moved from (B) to (C), against the writer's earlier result.
- **The gap.** Reading G and B_G are stated faithfully, and the gap that makes the outcome (C) is precise.
- **§4.5, A9 and the §8.3 table.** The two collapse attempts are sound and not overclaimed. The Substratum.md quotations are accurate. The table is correct.
- **Delta scope.** Nothing outside RESPONSE's delta table changed.

The should-fix concerns one sentence in A9, which understates what Substratum.md:385 says. Its effect strengthens A9's own verdict.

**Target.** Branch `research/g3-offset-873-20261113` at `43cd2cad5a7b153ed0a9079bd0983d02070ed093`. `git log -1` gives "unit 2(a) r2 from REVIEW-U2A-r1, verdict (C)". Its parent is `a87c410d`.

- `a87c410d` adds REVIEW-U2A-r1 byte-identical to what I issued (checked with `diff`).
- `git diff --name-status 46a548fb 43cd2cad` shows four additions: G3-UNIT2A-r2.md, NOTES-U2A-r2.md, RESPONSE-U2A-r1.md and REVIEW-U2A-r1.md. G3-UNIT2A-r1.md and NOTES-U2A-r1.md are unchanged.

Line references: "r2:n" means G3-UNIT2A-r2.md, "RESP:n" means RESPONSE-U2A-r1.md and "N2:n" means NOTES-U2A-r2.md. Corpus lines refer to `main` at `c3b5f37a`.

**Checks at `43cd2cad`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check 43cd2cad…` | 303 records intact |

None of them scans the drafts. A hand scan of the three new files finds no barred strings and no §A.32 or §A.33 phrases.

***

## Brief items

### 1. Each finding is resolved as RESPONSE states

| Finding | r2 | Status |
|---|---|---|
| U-1 | Reading G: ⊳_G and N5-G (r2:210–227); GR:342 s.1 quoted in full (r2:231); vocabulary split (r2:237–247); (ii-G) (r2:256); validity and B_G (r2:273–283); applied in ⊳_G (r2:439–444); controls on Reading G (r2:479–482); rule re-applied (r2:491–511); §4.5; A1, A3, A7–A9, G1–G2; consequences and findings scoped | Resolved. r2:502–503 is the review's replacement sentence. QU3 offers both scopings. |
| U-2 | §4.2 two-branch table (r2:451–473); C2(c) on the same branch (r2:482); consequence 2 (r2:684–688) | Resolved. See item 5. |
| U-3 | GR:378(i) quoted (r2:329–335); U2A-F2 restated and reclassified ELABORATING (r2:737); "GR:362's density estimate" at r2:82, :317, :644, :682 | Resolved. |
| U-4 | r2:699–703; §0 item 3 (r2:87–89) | Resolved. Unit 1's fine-tuning statement is left untouched. |
| U-5 | C1′ in §1.6 (r2:178–181), marked as added at review; per-reading row (r2:485); weight (r2:487–489); U2A-F7 | Resolved. C1′ is not pass/fail, and the outcome does not depend on it. This is the right handling of a control added after the rule. |
| U-6 | heading "Decision rule" and qualifier (r2:102–107); §10 (r2:855–856); N2 §3 | Resolved. |
| U-7 | r2:60–63, :315; M1 in the scope (r2:72–73, :665); B1 (r2:633) | Resolved. |
| U-8 | U2A-F1's class (r2:736); consequence 6 (r2:716–720) | Resolved. RESP:111–112 departs by naming Reading D as well. That is correct: §4.4 shows Reading D does not exclude the witness either. |
| U-9 | r2:122–124; A4 (r2:573–576) | Resolved. |
| U-10 | N2:12–15 | Resolved for r1. N2:16–17 repeats the pattern for r2 (nit Y-4). |
| U-11 | r2:810–813 | Resolved, and scoped to the order of determination. |

### 2. Applying the rule after adding Reading G is legitimate

- **Outcome clauses unchanged.** I extracted §1.2 from both revisions and compared them with `diff`. The outcome clauses (A), (B) and (C) are byte-identical: r1:99–113 against r2:129–143.
- **§1.3–§1.5 unchanged.** No hunk touches them. The only hunks in §1 are the heading and opening qualifier (r1:77, :79), the GR:340 entry (r1:94) and the new §1.6.
- **Clause (B) already required this.** Clause (B) quantifies over "every reading of the premise set". Adding an omitted reading is therefore applying the rule, not changing it.
- **No tuning toward a favoured result.** The change of outcome runs against the writer's earlier result. C1′ is explicitly kept out of the pass/fail controls (r2:180–181, :487–489).
- **Premise set.** It is unchanged. The GR:340 entry now gives the correct reason for each sentence's exclusion. "QM is emergent" (GR:342 s.1, second clause) is admitted as N3's emergence form, while the first clause stays excluded as the conclusion. That split is principled: QM's emergence by trace-out is Main's result, not the ordering that (i)–(iii) are said to force.

### 3. Reading G, B_G and the gap

- **The relation.** ⊳_G (r2:210–213) and N5-G (r2:222–227) are stated in the review's sense and correctly marked [P], with the recalled dissent cited (r2:798–802).
- **The bridge premise.** B_G (r2:281–283) is exactly the premise the review named.
- **Validity.** Reading G's validity (r2:273–280) is stated without overclaim. The exclusion is "if and only if B_G" (r2:48–50, :500–503), and (A) is "not established".
- **The gap.** The gap that makes the outcome (C) (r2:506–509) is the review's wording. It is narrowed precisely at r2:544–548 to two conditions: whether the boundary law is a coarse-grained consequence of φ (that is G3, open), and the stance on whether a derived law's terms ground its solutions (the corpus states none).

### 4. The §4.5 collapse attempts and A9

- **Attempt 1 (r2:515–536).** Correctly conditional. Its three limits are the right ones: (a) G3 is open; (b) it needs a stance on laws, here the regularity view against governing views, cited as recalled; (c) charity, through C1′. It does not overclaim.
- **Attempt 2 (r2:538–542).** Correct. Reading G's exclusion goes through N3-G, N5-G and B_G and does not assume the route ban, so the collapse into S fails as an argument. "Its bearing on K_cpl^free is not examined here" is an honest scope note.
- **Substratum.md quotations.**
  - Substratum.md:389 reads "Both are emergent. Both depend on the trace-out and the partition. Both are derived rather than fundamental. The fundamental object is (S, φ)". r2:524–525 elides "are" and the third sentence with ellipses, which is accurate.
  - Substratum.md:385 reads "the metric is a property of the classical dynamics of the partition boundary" and "two different substructures of the same total object (S, φ)". Both quotations at r2:526–527 are accurate.
  - GR:162 reads "uses the Einstein equations through Jacobson's relation (§3.1) and does not derive them". The quotation at r2:604–605 is accurate.
- **A9.** Its reasoning and verdict ("weighs against B_G and does not settle it") are sound, with one inaccuracy (Y-1).

### 5. The §8.3 table (r2:461–468)

Every cell is correct.

- (ii-L) on the witness is not excluded with §8.3, because the absolute part carries no loop and Δρ_Z is classical. It is excluded without §8.3.
- (ii-L) on Reading 1 is admitted with §8.3 and excluded without it.
- (ii-G) with B_G on the witness is excluded in both branches. This is right because grounding needs no covariation: the absolute value is a property of the realized class.
- (ii-G) with B_G on Reading 1 is admitted with §8.3 and excluded without it.
- (ii-W) excludes neither, in either branch. (ii-S) excludes the witness in both.

The closing sentence (r2:472–473) follows from the table. Two cells could be stated more precisely (Y-3).

### 6. Nothing outside the delta table changed

`diff G3-UNIT2A-r1.md G3-UNIT2A-r2.md` has 62 hunks, and each falls inside a row of RESP:59–104. I inspected the rows marked "format": r1:169/171/173, r1:194–203, r1:307–308 and r1:465. Each moves a label or reflows text and changes no content.

***

## Should-fix

### Y-1. A9 says Substratum.md:385 "does not fix" whether its subject is the description or the metric. It names the metric.

**Where.** r2:613–615.

**Evidence.**

- Substratum.md:385: "the wave function is a property of the embedded observer's compressed description of the visible sector; **the metric is a property of the classical dynamics of the partition boundary**." The subject is the metric itself.
- N2's own reading log quotes the same sentence (N2, §2 table).

Read in ⊳_G, that sentence makes the metric partly grounded in the dynamics of the partition boundary. N1–N2 fix that boundary by the metric's causal structure. That is a ⊳_G-cycle inside the corpus's own account, and it arises before any emergent term and independently of B_G.

So Reading G is consistent with Substratum.md:385 only if "a property of the classical dynamics of the partition boundary" is not grounding. That is the co-constraint stance Attempt 1 needs. The point strengthens A9's verdict and does not reverse it.

**Fix.** Replace r2:613–615 with:

> "Substratum.md:385 names the metric: it is 'a property of the classical dynamics of the partition boundary'. Read in ⊳_G, that sentence and N1–N2 give a ⊳_G-cycle independent of B_G. Reading G is consistent with Substratum.md:385 only if 'property of' there is co-constraint, not grounding, which is the stance Attempt 1 needs. Recorded under AW-ground and not adjudicated."

Update the AW-ground entry (r2:755–758) to match.

## Nits

### Y-2. "On Readings D, S and G, (ii) excludes them itself" needs its conditions

**Where.** r2:70 and the C1′ row at r2:485.

**Evidence.** On Reading D the exclusion goes through N5-D, which §2.2 shows is false. On Reading G it holds given a B_G-type premise for the semiclassical or emergent term.

**Fix.** Write: "On Reading S (ii) excludes them itself; on Reading G it does so given a B_G-type premise; on Reading D only through N5-D, which is false (§2.2)."

### Y-3. Two cells of the §8.3 table

**Where.** r2:465 and r2:468.

**Evidence.**

- In the ⊳_G row, the split ρ_Z(R₀) + Δρ_Z depends on the choice of R₀. What grounds the realized metric is ρ_Z(R*).
- The (ii-S) row omits Reading 1.

**Fix.**

- In the (ii-G) cell, add "(take R₀ = R*: the realized value is absolute)".
- In the (ii-S) row, add a Reading 1 entry: "excludes Reading 1 unless §8.3 makes its piece classical".

### Y-4. N2 states that r2 was not committed, but the head contains it

**Where.** N2:16–17.

**Evidence.** The r2 files are committed at `43cd2cad`. This is the same pattern as U-10.

**Fix.** Write: "Written in the working area by the writer; committed to the branch at `43cd2cad` by the coordinator."

### Y-5. Consequence 8's (ii-L) clause needs the §8.3 condition

**Where.** r2:725–726, "holds with (ii-L) added".

**Evidence.** Per §4.2, (ii-L) excludes the witness only without §8.3.

**Fix.** Write "holds with (ii-L) added and §8.3 not in force, or on Reading G given B_G".

***

## Disposition

CONFIRMED, with Y-1 (should-fix) and Y-2 to Y-5 (nits). All are textual, and no further review round is needed. The verdict (C), with the gap B_G narrowed to G3 and to a stance on laws, is supported by the record as revised.

No manuscript change is proposed. No premise is adopted.
