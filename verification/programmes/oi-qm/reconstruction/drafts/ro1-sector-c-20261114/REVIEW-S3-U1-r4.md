# Confirmation of S3-U1-r4 against P1 and P2

**Objects.** `S3-U1-r4.md` (SHA-256 `5c8c091d…aca8`) and `RESPONSE-S3-U1-r3.md`, in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, at PR #1294 head
`7887d33fead850adb1fbb3b2aa95ec394862bc6b`. r3 is unchanged from `7ee0ed9a`, and the retained
`REVIEW-S3-U1-r3.md` is byte-identical to the reviewer's file; I checked both.
**Reviewer.** The same separate non-author reviewer. Read-only.

## Verdict: ACCEPT. Ready for ChatGPT's exact-head review at `7887d33f`

P1(a), P1(b) and P2 are resolved, and the R-lin [A-inf] is correct. The diff touches only the
passages those findings named, plus O-a. Two leftover sites from P1(b) are nits (§3 below). They do
not change any verdict, so they can be carried as a note for the exact-head review or fixed in
passing.

## 1. The findings

| Item | Status | Evidence |
|---|---|---|
| P1(a), grouping | **Resolved** | §4.3(i): selector and carrier range over "nonempty, disjoint sets of factors of the model's declared product decomposition (AD-1(a); Main:48–52)", with "every such pair of sets" considered. A program's grouping can no longer change the class. `T` stays I-sel, with selector `{x}` and carrier `{y}` |
| P1(b), value writes | **Resolved** | §4.2's value-write entry and (iv) paragraph, §4.3's I-off list, §4.7's adaptivity clause, the S-A2 row of §5.2 and AW-7 now classify `z ⊕ f(h)` as I-off only for `f` affine in the record's factors, or for a single-factor record. The worked case `f = h₁∧h₂` is I-sel, "as `T` is". SEL-EXCL-1's arbitrary adaptive policies are stated to be generically I-sel |
| P2, NC-1's standing | **Resolved** | §4.3's INC entry, the inputs list and the §8 row state "open and not adopted", quoting "DEFINITION-OPEN" and "silently adopt its rejected NC-1 definition". INC takes only (A4) and (A6) under Q1 plus the owner rule. It never awards the label and claims nothing under (A1)–(A3) or (A5) |
| O-a | **Resolved** | §6.1: "Owner question (1) of this note asks whether to keep it; no owner record of that question exists yet" |

## 2. The checks requested

**The R-lin [A-inf] is correct.**
- R-lin is affine, so `φ^t` is affine. For any disjoint selector set `S` and carrier set `C`, with
  the rest fixed, `pr_Y φ^t = L_C s_C + L_S z + (terms in the rest) + k`.
- The partition of the carrier's content is the coset partition of `ker L_C`, and it does not depend
  on `z`. So no pair of factor sets yields I-sel. This agrees with D5 (OA1:176–183), which is
  measure-free.
- A non-affine value write cannot be effected by an affine `φ`. "Not available on R-lin" is
  therefore right, at D5's scope ([M-r]).

**The diff is limited.**
- The r3→r4 diff of the note changes only: the header, the inputs line, §4.2 (two passages), §4.3
  (selector and carrier, the I-off list, the new R-lin line, the INC standing), §4.7(i), two rows of
  §5.2, §6.1 (O-a), AW-7 and the §8 row.
- AD-1, the four outcomes, G1–G7, the comparison-tick rule, C-PREP, C-REC, C-RET, C-REN, K-1 to K-6,
  AC-1, the stops and the §9 verdict are unchanged.

**Coverage after the reclassification.**
- No coverage claim in U1 depends on an adaptive operation being available.
- The bare-model coverage half is "criterion-neutral, coverage absent by model" (§5.3). Operational
  I-sel "places outside `Γ_exe` nothing a model executes": whether `φ` effects a record-selected
  operation is a property of the rule. On R-lin it does not (D5, at scope), and on G_SM it is present
  with unsourced inputs.
- SEL-EXCL-1's adaptive policies appear only as off-`main` evidence and as a pointer for U2 (AW-7).
  They are not classified, and they are not stated to be available.
- Reclassifying non-affine adaptive values as I-sel therefore removes nothing that U1 elsewhere
  treats as available. The quantum and PR adaptive programs face the same test (K-1(ii)).

**Nothing else new.**
- No new premise.
- Nothing conditional is stated as established.
- No hidden authorization.
- No off-`main` reference is left unclassified.

## 3. Nits, not blocking

- **n1.** Two sites still state the unscoped form, "Adaptive setting values are not excluded there
  by D5": §4.7(iv) (r4:642) and the §9 composition row (r4:899). Write "affine adaptive setting
  values" at both, to match §4.2 and AW-7. As written, these lines also cover non-affine values, which
  r4 itself classifies as I-sel and as excluded on R-lin. Since "not excluded" is not a negative, no
  SNR-1 count is affected.
- **n2.** AW-5 (r4:847) reduces adaptive values to "a record-conditioned value write with a blank
  target (C-PREP)". Add ", or to C-INT for a non-affine function", as r4:356 already does.

## 4. Checked and not checked

- **Checked.**
  - The full r3→r4 diff.
  - The response.
  - Integrity of r3 and of the retained review.
  - The R-lin argument, against OA1:176–183.
  - Every "adaptive" occurrence in r4.
- **Not re-checked.** Citations unchanged since r1; Lean statements; the internal proofs of the
  records cited.
