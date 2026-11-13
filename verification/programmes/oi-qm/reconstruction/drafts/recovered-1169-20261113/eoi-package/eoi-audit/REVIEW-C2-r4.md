# REVIEW-C2 r4: diff-check of AUDIT-C2 r4 against r3

- **File reviewed:** `AUDIT-C2.md` (r4). I recomputed its sha256:
  `c84e6fb46922f91b5c3961070923037403743bf68a7dc50823eecc75a5cdda24`.
- **Diff base:** `AUDIT-C2-r3.md`, sha256 `b6d2bd3f78c423c2dbcd83b540351625960651343016f9cd50b8f6fb955faf6f`.
- **Snapshot:** `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`. Access was read-only.
- **Line references:** `A:n` is a line of r4.

## Verdict: **ACCEPT WITH CHANGES**

All five REVIEW-C2-r3 edits are applied, and every claim carries the right strength label. One change remains. It is
a citation fix with a one-phrase label, not a blocker. It comes from a wrong line reference in my own r3 review.

## 1. The five REVIEW-C2-r3 edits

1. **Applied, with a wrong citation.**
   - **What r4 adds:** R is justified by read statistics at A:706-711, and the not-state-valued caveat is at
     A:712-717. Both carry "(auditor/reviewer, paper)" and "(reviewer, paper)" labels.
   - **The wrong citation:** A:709 cites QA DESIGN.md:108-112 for the read probability. Those lines hold the
     comparator list only. See §2.
2. **Applied.**
   - "closed at paper level (auditor; re-derived by reviewer)" appears at A:740-741 and in summary item 12 (A:818).
   - The lemma heading carries "re-derived by reviewer" and the frame-type qualification (A:724-726).
3. **Applied.**
   - The reachable-laws form is split at A:742-756.
   - The closable sub-case (no conditioning, dyadic supplies) is labelled "(reviewer, paper; integer control for
     m ≤ 5 only)". This is correct. The descent itself is a proof for every m; the control covers only m ≤ 5.
   - What remains open is stated: non-dyadic supplies, citing QA :649-650 (verified), and any conditioned protocol,
     using the 3/4-herald counterexample.
4. **Applied.**
   - The AGL(4,2) check is scoped to bijections, where h_a takes the values ±1 (A:757-767).
   - Its numbers match my control: 768 maps induced, of which 384 have determinant +1 and 384 have determinant −1.
   - It is labelled "a control, not evidence".
5. **Applied.** A:129 now describes minacc-1 DESIGN.md:619 as "a control that checks the family is not cited".
   This is accurate.

**Other changes.** None outside these five.

**Unchanged and still correct.** Summary item 12 no longer says that Q-C2-2 is "named only". §17 still carries the
statement "named only … not authorized, adopted or started" (A:694), so nothing is lost.

## 2. Where the read statistics are stated: the writer's flagged point

Searches of the reconstruction records at `origin/main` found no record that states
`r_a(μ) = μ(f_a = 0) − μ(f_a = 1)`, or `E_μ[(−1)^{f_a}]`, on all laws. The searches covered `r_a =`, `μ(f_`,
`(−1)^{f`, `E_μ` and variants. The closest hit, FB RESULT.md:121, is the Bloch action of a translation, not this
formula.

The records state two ingredients, on different sides:

- **The native side: a read returns f_a.**
  - FB RESULT.md:43-44: "A read of axis a returns f_a; bit 0 denotes the + eigenvalue." This sits under H-L, whose
    preparations are the level-set laws (:38-42).
  - QA DESIGN.md:583-589 (node 8, *Reads*): "A read of `f_a` along `J f_a` … On `Λ_{a,b}` it records `b` with
    certainty … On `Λ_{c,b}` with `c ≠ a`, it records a uniform `r` … On `Λ_0` it records a uniform `r`". This
    covers only the level-set family.
- **The comparator side: the outcome probability.**
  - QA DESIGN.md:116-117: "A read along axis `a` gives outcome bit `b` with probability `(1 + (−1)^b r_a)/2`". This
    belongs to the imported comparator (I1, :108-113), not to the native model.
  - My REVIEW-C2-r3 cited :108-112 for this formula. That was wrong: the correct lines are :116-117.

**Conclusion.** No record states the formula on all laws. It follows from combining the native read (FB :43-44) with
the comparator's outcome rule (QA :116-117), applied to every law. It is therefore **derived (auditor/reviewer,
paper)**. On QA's family, the records do fix its values, through QA node 8's read transitions (:583-589) and the
comparator: `r(Λ_{a,b}) = (−1)^b e_a` and `r(Λ_0) = 0`.

**Requested change at A:707-711:**

- replace "QA's comparator Pauli reads (QA DESIGN.md:108-112)" with "QA's comparator outcome rule, `(1 + (−1)^b r_a)/2`
  (QA DESIGN.md:116-117; comparator I1, :108-113)";
- add QA DESIGN.md:583-589 beside FB :43-44 for the native read on the family;
- label the line "Together these give `r_a(μ) = μ(f_a = 0) − μ(f_a = 1)` on every law" as **derived (auditor/reviewer,
  paper); no record states it on all laws**.

The lemma is unaffected. Its proof uses only this R. The "forced" wording at A:707 stays correct as a derivation once
the label is attached.
