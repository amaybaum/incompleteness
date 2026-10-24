# Node 8 preregistration: confirmatory review of the frozen file

- Frozen: `mc8/PREREG.md`, 1313 lines, sha256 `ca5f976071f3dc257c0e4abefff9b782c9eca0db9c06ddffea8df69f486bf9dd`,
  re-verified. The blob at `382fc9e4:verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node8/PREREG.md`
  has the same hash; its parent's blob is `2ff8367f…` = `.PREREG.rev5.md`. `review/REVIEW-prefreeze-v5.md` in the commit
  is byte-identical to the scratchpad copy.
- Diff: `.PREREG.rev5.md` → `PREREG.md`, 13 hunks. Line numbers below are in the frozen file.
- Corpus read: worktree `mc8w`, mc-node6/NODE.md:209–214. Nothing computed under any candidate.

## Verdict: DEFECT (three mutant definitions; everything else stands)

The four blocking items are fixed and the reviewer's correctness claims check out. The notes were taken. The diff
adds three defects, all in §14's mutant list, and none touches a verdict-bearing computation. One comes from the new
timing convention, which leaves KM-31's case vacuous. Two are errors in the reviewer's own suggested mutant cases,
copied verbatim. Each needs an amendment before the mutant runs in step 3. Every computation earlier in step 3, and
every control, can run under the freeze as it stands.

## 1. Blocking items of v5

| # | status | where |
|---|---|---|
| 1 QM closure | fixed. The 91 states are 60 pure, 30 (I±P)/4 and I/4. The 12 states ψ⊗I/2 = (I + P_A⊗I)/4 or (I + I⊗P_B)/4 are among the 30. Closure checked by hand: Cliffords permute stabilizer groups; a Pauli readout Q on (I+P)/4 gives order 4 if [Q,P] = 0 and Q ≠ ±P, and (I±Q)/4 if they anticommute; Tr_B (I±P_A⊗P_B)/4 is (I±P_A)/2 if P_B = I and I/2 otherwise. There are 24 entangled states = 60 − 36, and U ↦ (I⊗U)\|Φ⁺⟩ is injective modulo phase, so these are the 24 (I⊗U)\|Φ⁺⟩. Transitive on B: Pur-U holds. The scope clause (A = one qubit, B = one qubit) is present. I-57 is updated (7 + 91). | l. 529, 1288 |
| 2a timing | fixed. Stated once (l. 598–600). The K-SWAP sequence 0, h, 0, h is consistent with it: x₀ is the O3 point mass, and the readout after step 1 is h. ℛ₂, K-SWAP and CL-C4 are named as dependent. | l. 523, 598–600 |
| 2b composites | fixed for ℛ₁, ℛ₂ and K-SWAP: sharing rule, joint prior, local class. CL-C4 is covered only through "coincides with K-SWAP" (note 4). | l. 592–596, 604, 608 |
| 2c K-SWAP class | fixed: I-52 entry (Ω, φ, bijections, ancillas, prior set, composites), step-3 order, §16 non-gem clause | l. 605–608, 1192, 1299–1300 |
| 2c prior domain | fixed: the prior is on h; preparable set is "whatever … yield", up to denominator 64; correct | l. 588–591 |
| 2d CL-C4 | fixed: φ = swap, no coupling step, citing mc-node6/NODE.md:211–212, which reads "(x, h) ↦ (h, x)" with history x₀, x₁, x₂. Matches. | l. 526, 609–611 |
| 3 stale mirrors | fixed: scorecard l. 1019; I-48 l. 1277, which also cites the existing KM-29 (I-48, l. 1116); I-40 l. 1269; l. 235–237 (inverse of a visible permutation is accessible, true for a finite permutation group); K-IF l. 1053 | as cited |
| 4 mutants | added KM-32 to KM-36 and cross-referenced at I-54, I-55, I-57 and I-59. Three of them are defective (§3 below). | l. 1120–1127 |

## 2. Notes of v5

All five taken. "Pending review" vs "provisional": l. 1012–1013. Live content under (B): l. 612–614. SPK-orig hand
expectation: l. 521, labelled "not a verdict". Full-access list: l. 452–454, 1192. Note 5 needed no change.

## 3. Defects (amend before the mutant run)

- **D1. KM-31 (l. 1119) is vacuous under the new timing convention (l. 598–600).** One step is the observer's selected
  permutation (the identity included), then φ, then the readout. For K-SWAP a single waiting step therefore already
  reads x₁ = h. A computation that composes only one-step protocols reports full access, not "none", so the mutant's
  output equals the correct output and I-58 cannot catch it. Fix: make the case "zero-step protocols only (readout of
  x₀)", which reports "none". Alternatively, target ℛ₂ᵃ's one-bit observer: reaching the original h₂ there needs two
  steps. That target needs its own must-hold, because I-58's must-hold covers K-SWAP only.
- **D2. KM-32 (l. 1120–1121) is not shown to fail, and is probably vacuous.** v5 §D computes that on ℛ₁'s grid, with
  weight-½ mixing available, the preparable-weight rule already makes only δ₀ and δ₁ pure. A further hand case:
  1/64 = (1/8)·(1/8) + (7/8)·0. So the mutant's printout "only δ₀, δ₁ pure" is likely the correct printout. Fix: use a
  fixture on which the two rules provably differ. For example, take the state set {δ₀, δ₁, (1/3, 2/3)} with preparable
  weights {0, ½, 1}. The preparable-weight rule gives three pure states, because none of the three ½-mixtures lies in
  the set. Real convex combination gives two.
- **D3. KM-33 (l. 1122–1123) names the wrong catching check.** diag(1/3, 2/3) has rational entries, so it lies in
  ℚ(i, √2) and the field check passes it. The mutant is caught by I-57's closure enumeration instead: H ω H† =
  (I − X/3)/2 is not an instance state. Fix: change "caught by the field check" to "caught by the closure enumeration".
  Alternatively, keep the field check and use a state with an entry outside the field, such as one involving √3.

## 4. Notes (amendment-grade, non-blocking)

1. **Full access is stated before I-58 measures it.** The Lemma A paragraph (l. 452–454) and the §16 non-gem clause
   (l. 1192) say "the full-access classes ℛ₁ᵃ, ℛ₂ᵃ, K-SWAP, CL-C4". §6.10 (l. 614) says "expected". For ℛ₂ᵃ and
   CL-C4, full access is an expected shape, not a must-hold; v5 §D wanted ℛ₂ᵃ's left unstated. The §16 classification
   should apply "if I-58 prints full access for the class". No verdict is pre-stated, since this concerns access and
   not purification.
2. **Stale mirror at I-50 (l. 1279).** It still reads "ℛ₁ and ℛ₂ outputs", but K-SWAP and CL-C4 are now §6.10
   classes (l. 1299–1300).
3. **Stale mirror at l. 1059.** "QM must satisfy all" is wider than the narrowed QM row (l. 529: Pur-E and Pur-U for
   A = one qubit, plus X-1 to X-5).
4. **CL-C4's inputs are self-contradictory (l. 610–611, 526).** The entry says it "coincides with K-SWAP up to the
   prior set", then says "Prior as in K-SWAP". With the prior shared, only the initial x can differ, and neither entry
   fixes CL-C4's initial x (O3, l. 158: a point mass fixed by the protocol). CL-C4's composites line ("as §6.10 fixes
   them") has no explicit §6.10 entry. I-52 prints the inputs, so this is a disclosure gap rather than a free choice,
   provided the code takes K-SWAP's prior. The amendment should state the initial x (protocol-chosen point mass or
   fixed at 0) and the composites, and should delete "the prior set".
5. **Shared ancilla (l. 593–596).** The text should state explicitly whether each copy's local preparation bijections
   may act on the shared hidden ancilla. "Common to both copies" with §2.2's local-operation definition (l. 238–239)
   reads as yes. The answer decides whether correlated composite states, and hence Pur-E witnesses, exist.
6. **KM-36 (l. 1126) and I-3 (l. 1232).** I-3's check is a parameter table "compared by the reviewer", which is not a
   mechanical check that can fail cleanly. The amendment should name a mechanical catcher, such as the printed
   n = 2 counts 60/30/1, which an extra size-8 state turns into 31, or a coset-membership assertion. It should also
   add KM-36 to I-3's row.
7. **K-IF on SPK-conv (l. 1053).** SPK-conv's state set is a continuum, so "sizes printed" needs a reading, such as
   the extreme points and a polytope description.
8. **K-SWAP's expected shape (l. 608).** "Read, wait, read" is correct but not minimal: under l. 598–600 one waiting
   step suffices. This is cosmetic, but it ties to D1.

## 5. New-defect sweep of the diff

- Undefined terms: none. Q_fb is defined at l. 97/430, KM-29 at l. 1116, ω_{1/3} inline, and O3 at l. 158.
- Pre-stated verdicts: none. The hand expectations at l. 521 and 529 are labelled as control shapes. Note 1 concerns
  access, not purification.
- Claims stronger than their evidence: none beyond Note 1.
- Re-grep of stale mirrors: "60 two-qubit", "products of a stabilizer", "Bloch" (l. 429 is literature, legitimate),
  "qubit control", "fiber freedom" (l. 132/470, legitimate) and "9 product effects" each have 0 stale hits. "PC-4a"
  has 0 hits. "provisional" hits are all the I-53 sense. The stale hits found are I-50 and l. 1059 (notes 2 and 3).
- Register: no caps emphasis or history voice was added.
