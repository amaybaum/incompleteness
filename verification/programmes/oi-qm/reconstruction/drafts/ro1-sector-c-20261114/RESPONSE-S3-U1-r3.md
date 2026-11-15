# Response to the focused review of S3-U1-r3

**Review.** `REVIEW-S3-U1-r3.md`, on PR #1294 at `ce9a7e12`, by the same separate non-author
reviewer. Verdict: ACCEPT WITH CHANGES. It reviewed `S3-U1-r3.md` at `7ee0ed9a`.

**Revision.** `S3-U1-r4.md` applies P1, P2 and O-a, and nothing else. r3 is left unchanged; I checked
that it is byte-identical to the branch copy. r4 is unreviewed and paper-only, under #1169
c.6890079967. It adopts no new premise. The S7 and O11 stops, S5's separation, H-RR as a hypothesis,
AC-1 and SNR-1 are all unchanged.

## P1. I-sel depended on how regions are grouped, and value writes were classified inconsistently. Accepted.

Edited sections in r4: §4.2, §4.3, §4.7, §5.2, §7 (AW-7).

- **(a) Grouping.** In r4, I-sel's selector and carrier range over nonempty, disjoint sets of factors
  of the model's declared product decomposition (AD-1(a); Main:48–52), not over regions as a program
  groups them. Every such pair of sets is considered, so declaring `(x, y)` as one setting region
  cannot turn `T` into I-off. With `{x}` as selector and `{y}` as carrier, `T` stays I-sel.
- **(b) Value writes.** I-off for `z ⊕ f(h)` is now limited to `f` affine in the record's factors, or
  to a single-factor record.
  - Check: for affine `f`, the dependence on any carrier factor is `a_j h_j` plus a constant fixed by
    the other factors, so the partition does not change. With a single-factor record, the only
    carrier left is `z` itself, and on `z` the write is a translation.
  - A non-affine `f` over several factors is I-sel. `f = h₁∧h₂` is the example given, matching `T`,
    since `T` is the value write of `x∧y` into `B`. Such a write is a record-selected operation and
    falls under C-INT.
  - AW-7 now says that SEL-EXCL-1's arbitrary adaptive policies are generically I-sel. The §5.2
    table's two rows are scoped the same way.
- **The R-lin conclusions are confirmed unchanged.** I added an [A-inf] line in §4.3.
  - D5 states for any affine `Φ` that the linear parts do not depend on the setting (OA1:176–183). An
    affine map restricted to any pair of disjoint factor sets keeps that property, so quantifying
    over factor sets adds no I-sel on R-lin.
  - A non-affine value write is I-sel and is not affine, so it is not available on R-lin. This agrees
    with r3's "needs a rule that is not affine".
  - The verdict rows in §9 need no change.

## P2. NC-1's standing. Accepted.

Edited sections in r4: §4.3 INC entry, §8 row, inputs list.

- I checked at source:
  - c.6559049909 is headed "NC-1 definition review round: closed, DEFINITION-OPEN";
  - #1007 c.6719788955 says the history landing must not "silently adopt its rejected NC-1
    definition".
- r4 now states that NC-1's definition is open and is not adopted here.
- It states that INC takes only NC-1's withholding conditions ((A4) and (A6) under Q1) and the owner
  rule, never awards the label, and claims nothing under (A1)–(A3) or (A5).
- The two places where r3 called NC-1 a "proposed definition" (the inputs list and the §8 row) now
  give the same standing, so the note does not contradict itself.

## Optional

| # | Disposition | Reason |
|---|---|---|
| O-a | Applied (§6.1) | No owner record of this question exists. r4 now reads "Owner question (1) of this note asks whether to keep it; no owner record of that question exists yet." |

## Not changed

Everything else is as in r3: the verdict, AD-1, the four outcomes, the comparison-tick rule, the S7(a)
narrowing and its reversion paragraph, AW-3, and the §5.1(iv) table.

## Not checked in this revision

These were not checked in r1–r3 either:
- the Lean statements;
- the internal proofs of the records cited;
- whether Theorem N's criteria are at least as weak as C-RET's;
- NC-1's clauses (A1)–(A3) and (A5).
