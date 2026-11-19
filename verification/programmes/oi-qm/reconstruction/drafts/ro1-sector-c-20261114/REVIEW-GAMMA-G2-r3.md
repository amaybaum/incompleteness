# Focused confirmation of GAMMA-1 unit G2 r3; independent, non-author, paper-only

**Object.** `GAMMA-G2-r3.md`, blob `43a3f0ca0f5829c60fea5f9cf4bf5b8e4d567dd3`, with
`RESPONSE-GAMMA-G2-r2.md`, retained on PR #1294 at `e44c06f3` in
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`. The copies read are
byte-identical to the retained ones. Cited r3:N. The confirmation being applied is
`REVIEW-GAMMA-G2-r2.md` (blob `5301853e`, verified), cited RG2b-CN.

**Reviewer.** Claude, author of RG2 and RG2b and of none of G2. Read-only; hand checks only.

**Verdict: ACCEPT.** C1 to C5 and the optional item are applied as required. The r2-to-r3 diff, read
in full, contains nothing beyond them and the revision notes. Every proof is as in r1. No D-1 verdict
is drawn. One optional wording note follows (§3).

## 1. The five points asked

1. **G_SM.** Applied. r3:788–792 states SIG's identification (SIG:78–81, proved there: the binary SM
   ring is G-ring at `q = 2`) and that G_SM meets Theorem G2-2's hypothesis as G-ring does, since the
   state space is a product over sites and slices. r3:158 names G_SM among §7's members. r2's "not
   shown to meet the hypothesis" is gone from §7 and from §11 (r3:890). A grep finds no other G_SM
   occurrence. The SM:104–106 class beyond SM:112 is left as SIG screens it. Correct.
2. **§6.2.** Applied. r3:745–749 says only that the control images separate: C0's is `−b_j`, and
   PC-wave's departs from it wherever the cross term is nonzero. It says that greenness needs target
   data that is not supplied (G3: Sinha's `δ` not reported), and that the controls are not evaluated
   as green. A grep finds no other "green" or "C0 fails" claim. Condition 6 of r3:258 cites §6.2
   consistently.
3. **C13 and C15 labels.** Applied.
   - G2-C13 (r3:298) reads "only by design: a necessity example of G2-C2's kind". It gives the
     independent variant `[c ∈ {0, 1}]`, with `P(both = 1) = 1/4 = (1/2)(1/2)`, which I re-checked.
   - G2-C15 (r3:615) reads "only by design, or within H-K1 through an expansion error". It states that
     C15 shares G2-C5's expansion, and gives the `a = 2` over `ℤ/4` failure outside H-K1: coefficient
     `−2`, and `u_2(0) mod 2 = y_0 mod 2`, which I re-checked.
   - G2-C11 and G2-C14 also carry RG2b-C5's wording.
4. **The fringe candidate.** Applied at r3:246–274, :819–821 and :892.
   - *Status.* It is a candidate, not a counted miss under SNR-1, and even counted it would falsify
     `(M, κ)` at that scope only.
   - *Scope.* The six conditions match RG2b §3: A-reg, or A-cur outside (NW); a screen outside §3.2's
     class; the alternative reading of U1:514; C-REC and C-RET sourced; the κ instance with κ-ens and
     H-ens; the controls green.
   - *Comparison.* The observable is the first clause of G1 §5.7, the `π_C`-sorted pair ratio. The
     targets are Walborn 2002 Figs. 4–5 (non-delayed), Kim 2000 `R01` and `R02` (a6-delayed, needing
     C-RET or R-seq), and Ma 2013 only through `κ_scale`, all as in LIT 1.6–1.8.
   - *a1.* r3:234–237 states that a1 has no target that `κ` compares in the sources read.
5. **Nothing else, and D-1.** The diff contains only the header scope (r3:10–11), the revision and
   review-status notes, and the items above. D-1 appears only at r3:14, :53, :503 ([A-inf] bearing on
   (β)), :842 (undecided), :871 and :927. None of these is a verdict.

## 2. Hand checks recorded

- The `t = 1` A-reg wording at r3:486 now names the `y_D`-marginal, matching the RG2b derivation.
- The response's control census is consistent with r3's table labels. Counted: C4, C5, C6, C7, C9,
  C11, C12, C14. Necessity or design examples: C2, C13, C15. Not counted: CC-1 to CC-5.

## 3. Optional note (not required)

Condition 4 (r3:254–255) lists C-REC and C-RET for the marker and the screen. The route also needs the
herald itself retained to `t_c` (G1 §3.1; G1 §4.2 names this as the visible-herald route's first
missing step; r3:239 says so). The list is a set of necessary conditions, so the omission makes no
statement false. Adding "and the herald" would make it complete.

Nothing here counts under SNR-1; r3 is confirmed as a paper-only draft.
