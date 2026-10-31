# SC-22 audit: the book's 𝒩-regime vocabulary (WIP, unreviewed)

Read-only audit at `main` `1a60e06b`, an owner-approved separate audit item (2026-10-27). Scope: "define the 𝒩-regime
vocabulary precisely before changing the manuscript … The objective is consistent terminology, not additional physical
assumptions or stronger theorem claims."

The scripts use exact `Fraction` arithmetic; the CMI floats printed are illustrative only. Run them from this directory:
- `python3 -I -B regime_exact.py`
- `python3 -I -B enum_window.py .`
- `python3 -I -B blp_unbounded.py .`

The coordinator replayed all three, and each matched its committed output exactly. `proposals.py` holds 56 rewrites. Each
old string is verified unique in its chapter and in FULL. With all 56 applied to a scratch copy, `architecture_check.py`
reports 259 invariants and 0 violations. Controls are green: a Markov family; the sequence (I, J/2, I); the tape-and-ledger
coin; and the guard check's own positive control.

## Findings
1. **𝒩 has no formula anywhere in the corpus**, including the code and `verification/`.
   - Three incompatible identifications are given:
     - a "P-indivisibility measure" (ch18 :74);
     - BLP and RHP (ch18 :78, ch13 :134), although RHP measures CP-indivisibility;
     - a verbal trace-distance form (ch15 :168).
   - The object it applies to and the time window are never specified.
   - There are no regime thresholds. "Maximal" is meaningless for the cumulative BLP measure, which is unbounded (the
     Main §2.4 model gives 2/3, 4/3, 10/3, 20/3 at K = 2, 4, 10, 20). "Weak" occurs only in a table. The ch18 table's
     τS/τB bands contradict the placements at ch13 :138.
2. **F(r) = 2r − r² and "𝒩 → 1 for r ≫ 1" are not derived.** ch15 :156 says the derivation is "not packaged". The claim
   "non-monotonic" (ch15 :154, :168) is false for the stated form, which is nondecreasing on [0, 1].
   - r = N_H/N_V, a ratio of mode counts. This is not Main's C3 quantity (log₂|C_H| ≥ I*), so "marginal C3" in Main's
     sense means saturation.
3. **The links are not derived:**
   - **(a) C3 margin ⇒ 𝒩: refuted (exact).** XOR with an idle hidden ledger has an arbitrary C3 margin yet 𝒩_W = 0.
     Block-XOR with n_H/n_V = 1/k has peak revival 1. ch13 :138's capacities (≥ 10^28 in ratio) would place biology at
     the maximal end, contradicting ch13 :134 and ch18 :85–:86.
   - **(b) τS/τB ⇒ 𝒩: not derived.** Only ceilings on memory are proved. A static bath (τB = ∞) has 𝒩_W = 0. Two
     opposite heuristics coexist: the ch18 table and ch15 :187, against ch15 :103 and Complexity §7.6.
   - **(c) C1–C4 ⇒ 𝒩 > 0: refuted on accessible windows**, by the Track B and D countermodels. Exhaustively, among models
     with a gap inside the window: (2,2) 8 of 12 have 𝒩_W = 0; (2,3) 540 of 576; (3,2) 192 of 616. The converse holds:
     𝒩_W > 0 never occurs without a gap in the window. On the recurrence cycle 𝒩 > 0 for every non-deterministic
     representative, so it cannot separate regimes.
   - **(d) 𝒩 as "memory strength": conflated.** XOR has M = 1 bit and 𝒩_W = 0. Sites: ch13 :136, ch15 :152, ch18 :78,
     glossary :115.
4. **Other inconsistencies:**
   - appendix-a :213 ("no analog in standard QM") contradicts ch18 :78.
   - ch13 :68 cross-references ch18 §18.3; F(r) is in ch15 §15.7.
   - The symbol 𝒩 collides with SM's taste-loop 𝒩 = 1/9 (SM §7.2, ch06 :179).

## Proposed definition set (only what the corpus proves)
- **D1 Memory.** M_t > 0 on W, equivalently a (C4) gap inside W. "Memoryless" means Markov on W.
- **D2 P-divisibility on W.** As in Main :137 and Lean `PDivisible`.
- **D3 Revival.** 𝒩_W := max over pairs of initial laws and s < t ≤ K of [d_t − d_s]⁺. This is the bounded, peak form of
  BLP, in [0, 1]. Restricted to point roots, 𝒩_W > 0 is exactly Lean `C4r K Γ`.
- **Regimes, on W only:** no revival (𝒩_W = 0); revival (𝒩_W > 0); complete revival (𝒩_W = 1, attained at (2,2) and
  (3,2)); partial revival (0 < 𝒩_W < 1, the mechanism proposal's label). "Weak" is dropped.

Implications:
- 𝒩_W > 0 ⇒ P-indivisible on W (Lean `c4r_implies_pIndivisible`; general pairs via `tv_mul_le`). The converse does not hold.
- 𝒩_W > 0 ⇒ memory on W, under a full-support visible prior (Track B paper proof; exact here).
- **Sufficient** for 𝒩_W > 0: C4e on W (Lean).
- **Not sufficient**: C1–C4, any C3 margin, or τB = ∞ (exact).

## Decisions the owner needs to make
- The peak or the cumulative definition of 𝒩.
- Whether to keep the "partially-quantum" label.
- Whether to remove or relabel the ch18 :82–:88 table. The rewrite list removes it.

All rewrites remove or narrow claims, so the correctness bands are unchanged.

## Not rewritten here (other units or owner decisions)
- ch15 :103 (the O(τS/τB) heuristic).
- ch15 :112, :114 (SC-16).
- glossary :91, :105 and Main :334 (SC-5/SC-16 terminology).
- ch01 :225.
- appendix-c :62.
- ch13 :142, :146, :170: "specific algebraic predictions", which are stated nowhere.
- The L ≈ 5 overlap between ch15 :112 and :164.
