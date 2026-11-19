# Focused review of S3-U1-r3 against the review of r2

**Objects.** `S3-U1-r3.md` (SHA-256 `d24b1a65…587d`) and `RESPONSE-S3-U1-r2.md` in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at PR #1294 head
`7ee0ed9afcc049c59e21fe0b5500a923ba441bb0`. r2 is unchanged from `134dcc97`, and the retained
`REVIEW-S3-U1-r2.md` is byte-identical to the reviewer's file (both checked).
**Corpus and records.** `origin/main` `dfeec843`; SEL-EXCL-1 at `0ecfddeb`; #1009 c.6559049909,
#1007 c.6719401889 and #1007 c.6719788955, read through the API.
**Reviewer.** The same separate non-author reviewer. Read-only.

## Verdict: ACCEPT WITH CHANGES

N1–N8 are resolved as asked. The two-class C-INT is symmetric between PR and the quantum measurement
pattern, and it does not make PR vanish. The N3 split matches OA-1 D5 and S-C1(c) at source, and the
Q1 attribution is correct.

Two small required changes remain:
- **P1.** A consistency defect in the I-sel definition: it depends on how a program groups its
  regions, and it is applied inconsistently to value writes.
- **P2.** A missing standing note on NC-1.

Both are one-paragraph edits. These are not nits, so I do not yet call U1 ready. Once r4 applies P1
and P2 and a short confirmation of those two items passes, U1 is ready for ChatGPT's exact-head
review.

***

## 1. Disposition of the r2 findings

| Finding | Status | Where in r3 |
|---|---|---|
| N1, Q1 over-applied | **Resolved.** I-sel and I-off are operational, with no refinement test. Q1 applies only to INC, a classification. `T` is operational I-sel, its INC is withheld, and a restriction on I-sel reaches `T`. The AC-1 consequence is stated as open. r2's row is kept, marked withdrawn, with the reason | §4.3, §5.1(iv), §7 AW-3 |
| N2, §5.3's C-INT row | **Resolved.** I-sel is a requirement that places outside `Γ_exe` nothing a model executes; INC is a classification only | §5.3 |
| N3, adaptivity | **Resolved, subject to P1** | §4.2, §4.7, §9, AW-7 |
| N4, the §A.24 ground | **Resolved.** Regrounded on `Θ` (e) and K-rec (SPEC:379, :243), marked [A-inf] | §5.3 |
| N5, unsourced programs | **Resolved.** Three cases stated: in, out, undetermined | §5.3 |
| N6, formalization choices | **Resolved.** Three rows added to the table of choices; only the wording of Q1 and of NC-1's question is listed as sourced | §5.2 |
| N7, the G_SM row | **Resolved** | §4.3 |
| N8, K-acc under the component reading | **Resolved** | §6.1 |

## 2. The checks requested

**K-2, symmetry.** Under the frozen two-class C-INT:
- `T` is I-sel through `x` selecting whether `y` reaches `B`. I re-derived this:
  `y ↦ B₀⊕r⊕(x∧y)` is constant for `x = 0` and injective for `x = 1`.
- A setting that selects an operation on a carrier, which is the quantum measurement pattern, is
  I-sel by the same test.
- Neither is exempted. The informational label INC is withheld for `T`, but no requirement reads INC.
- So the asymmetry found in r2 is gone.

**K-1.** I-sel is a property of the map `φ` effects (but see P1), and INC places nothing in or out of
`Γ_exe`. No clause excludes PR by declaration.

**N3 at source.**
- D5 (OA1:176–183): for affine `Φ` with state `(c, x, u)`, the linear parts and `k` do not depend on
  `c`. (i) The carrier's non-translational map does not depend on `c`. (ii) The functionals read do
  not depend on `c`. "An affine exchange that writes `c` changes neither."
- So D5 excludes record-selected and setting-selected *operations on a carrier*, and leaves affine
  value writes in place.
- S-C1(c) (MR★:508–509): "No record-conditioned operation on the carrier exists". This concerns
  operations, as r3 says.
- SEL-EXCL-1 l. 99's write, "(h,z)↦(h,z⊕f(h)) using an initially blank target and keeping h", is
  quoted correctly.
- The split is correct for a value written by an affine function, or from a single selector region.
  P1 gives the qualification.

**Q1 attribution.** Correct at source.
- #1009 c.6559049909 (`amaybaum`, 2026-11-01T14:08:22Z) is "NC-1 definition review round: closed,
  DEFINITION-OPEN". It defines "a setting-controlled interaction relative to Acc" on the channels
  `Φ_s^{a,π}` (readout experiments), with (A4) "Not a garbling at access level" and (A6) "No common
  refinement".
- It states the owner rule: "A garbling withholds the label at a; finding no garbling never awards
  it".
- Its §6 item 1 is quoted verbatim in r3.
- #1007 c.6719401889 (2026-11-08T08:42:56Z) quotes that item in its §4.
- #1007 c.6719788955 adopts "the proposed conservative rule, subject to the stated access
  assumptions".

**INC applied to `T`.** The readouts on `(B, y)` under `x = 0` and `x = 1`, namely `(B₀⊕r, y)` and
`(B₀⊕r⊕y, y)`, are related by the fixed bijection `(b, y) ↦ (b⊕y, y)` on the output alphabet. That is
a garbling in NC-1's sense: a map on the output alphabet that does not depend on the prepared state.
INC is correctly withheld.

**S7(a) and the comparison tick.** Unchanged and still correct. The N8 addition is accurate.

## 3. Required changes

**P1. I-sel depends on how regions are grouped, and value writes are classified inconsistently with
`T`.**
- *The definition.* I-sel is existential: "There are selector values … a region `Y` … a tick `t`".
  Its selector and carrier are regions of the program's own declaration (§2.1: "its regions (…
  carriers, setting regions `Z` …)").
- *Grouping.* If a program declares `(x, y)` as one setting region, the only carriers left are `r`,
  `A` and `B`. Every partition is then unchanged, and `T` becomes I-off. The class therefore depends
  on a grouping choice. That is the degree of freedom K-1 and K-2 guard against, the sibling of r1's
  carrier clause.
- *Value writes.* §4.2 and §4.3 call "a record-conditioned value write `z ⊕ f(h)`" I-off. That holds
  when `h` is one selector region, or `f` is affine in `h`'s factors. For a non-affine `f` over a
  record that spans several factors, the same test makes the write I-sel. Take `f(h) = h₁∧h₂`, with
  `h₁` as selector and `h₂` as carrier: the write is I-sel, exactly as `T` is. `T` is itself the value
  write of `x∧y` into `B`.
- *Effect.* AW-7's "A record-dependent setting value is I-off" holds only at that scope. SEL-EXCL-1's
  arbitrary adaptive policies `f_i(U_A, H_A^(i−1))` are generically I-sel. The R-lin conclusion is
  unaffected: affine value writes are not excluded by D5, and non-affine ones need a non-affine rule,
  as r3 already says.
- *Fix, in two sentences.*
  - Quantify the selector and the carrier over the factors of the model's declared product
    decomposition (AD-1(a)), not over the program's grouping. I-sel is then a property of `φ` and
    that decomposition.
  - Scope the I-off classification of value writes to `f` affine in the record's factors, or to a
    single-factor record, with non-affine `f` falling under I-sel, consistently with `T`.
- *Statements to adjust.* §4.2, AW-7, and §4.3's I-off list.

**P2. NC-1's standing.** r3 calls NC-1 "a proposed definition, off `main`". At source, its round is
"closed, DEFINITION-OPEN" (c.6559049909). The owner decision says the history landing must not
"silently adopt its rejected NC-1 definition" (c.6719788955).

INC as used is safe:
- it only withholds, never awards;
- no requirement reads it;
- the response says it claims nothing under (A1)–(A3) and (A5).

But r3 does not say this in the note. Fix: in §4.3's INC entry and in §8's row, state that NC-1's
definition is open and was not adopted. Also state that INC takes from it only the withholding
conditions under Q1 and the owner rule, and never awards the label.

## 4. Optional

- **O-a.** §6.1, at r3:747, says "The owner has an open question on whether to keep it." The question
  is U1's own, raised in owner question (1); no owner record of it was found. Write "owner question
  (1) asks whether to keep it".

## 5. Nothing else new

- No new premise.
- No conditional result stated as established. AW-3 is BORDERLINE, author-side and off `main`. The
  AC-1 consequence for Main:412 is stated as open.
- No hidden authorization.
- §A.42 item 8: c.6719401889 and c.6559049909 are added as provenance; no unclassified off-`main`
  reference was found.

## 6. Checked and not checked

- **Checked.**
  - The full r2→r3 diff and the response.
  - The three GitHub records above, at source.
  - OA1:176–183; MR★:508–509; SEL-EXCL-1 l. 99.
  - The `T` algebra under the frozen definition and under the regrouping in P1.
- **Not re-checked.** Citations unchanged since r1, Lean statements, and the internal proofs of the
  records cited.
