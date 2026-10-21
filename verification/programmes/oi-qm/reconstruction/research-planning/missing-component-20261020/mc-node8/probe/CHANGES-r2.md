# Node 8 step 1, revision r2: changed output lines

This file compares `p8s1.r2.run1.out` (from `p8s1_r2.py`, amendment A-4) with `p8s1.r1.run1.out` (from `p8s1_r1.py` at
`d924b5bb`). The r2 output has 403 lines; the r1 output has 372. `diff` reports four hunks: 4c4, 219c219,222,
368a372,399 and 371c402. Each is explained below. Every other line is byte-identical. That includes:

- all access classes, digests, transformation counts, preparable-set and pure-set counts and mutant verdicts;
- SHARED-ALT and the convex-closure lines;
- the 46 realization purification lines (the eight classes, CL and the summary lines). Their concatenation has sha256
  `6b450a54…cd70ab` in both files.

**Outcome comparison.** The review's parser (`parse_outcomes.py` from the review of `d924b5bb`) reads the budget m=3
line, the summary line and the closure line of every class in both files. It reports identical Pur-E counts and Pur-U
words.

| class | r1 | r2 |
|---|---|---|
| R1a, R1b | 2 of 63, fails 61; Pur-U fails | same |
| KSWAP, CLC4 | 2 of 63, fails 61; Pur-U holds | same |
| CL | 2 of 9, fails 7; Pur-U holds | same |
| R2a1, R2b1, R2a2, R2b2 | 4 of 93585, fails 93581; Pur-U fails | same |

No Pur-E or Pur-U outcome changed, and no check changed from pass to fail. No realization line contains "not decided"
or "undecided": the N2 branch is reached only by its fixture.

## Changed lines, by cause

**4c4: input digest and label (N9; no outcome).** The AMENDMENTS sha256 is `37aff9f1…8f70`, not `f0ab4db2…dcc04`,
because A-4 was appended. The label now names A-3 and A-4. The digest is printed, not checked.

**219c219,222: K-PURPOS countercontrols (N1, N2; gating).**
- Lines 219–221 are three new fixture lines through the production one-bit generator (`onebit_grid_text`), printed by
  `pur_line` and labelled as fixtures:
  - line 219: K-SWAP with its reversible maps removed. Pur-U reads "fails (… failing 2)", with "delta_0: connected
    pairs 0 of 2; not connected: (delta_0 x delta_0, delta_0 x delta_1), …" and "no collected reversible transformation
    of B (0 maps)". Pur-E is 2 of 63.
  - line 220: pure composite states {d00, d11}. Pur-U reads "vacuous (no state has two or more purifications)". Pur-E
    is 2 of 63, with one purification each.
  - line 221: pure composite states {d00, ½(d00 + d01)}. Pur-U reads "undecided (states with two or more
    purifications: 1; tested 0, failing 0, not decided 1): not decided for delta_0". Pur-E is 1 of 63.
- Line 222 (r1 line 219) is the K-PURPOS check. Its condition now also requires the three statuses 'fails' (with the
  named pair), 'vacuous' and 'undecided', and its message prints them. It still passes. The first part of the message
  is unchanged.
- The other fixture lines (r1 217–218 and K-PURPOS-SPK) are unchanged. The I-6 gate line is unchanged, because the gate
  is still the K-PURPOS check.

**368a372,399: the N5 block (new lines, after phase C; gates nothing).** The block is inserted after the last "live
content under option (B)" line and before the A1-SCOPE check. It has six new checks:
- **K8-SENS**, a sensitivity block that decides nothing. With priors on the k/8 grid the counts are:
  - one-bit preparable sets 9, 9, 13 and 19 at m = 0..3, against 23, 23, 39 and 63 with F8;
  - one-bit composites 22719, against 195769, from 249 A-side pairs; every non-pure state has a half-mixture witness,
    with 0 fallback;
  - R2 at m = 3: 38749 states, against 93585, from 165 priors.

  The pure sets are the point masses at m = 1, 2, 3, for the composites and for R2, under both conventions. These are
  A-3's numbers, and every count matches the review of `390e252f` (`k8_alt.out`).
- **A4-GRID.** `composite_onebit` reads neither `S_single` nor `W`. Its per-prior grid is the m=3 grid
  `{(k p + (8 - k)(1 - p))/8}`.
- **A4-MARG.** The composite A-marginals at m=3 are 117 states, equal as a set to S_onebit(4) (117). They contain
  S_onebit(3) (63) and add 54 states; 1/16 is a marginal and is not in S_onebit(3). On the per-prior grids,
  ½(α₀ + α₁) gives S_onebit(m+1) at m = 0..3 (23, 39, 63 and 117 states).
- **A4-PURE-E.** One `pur_line` line, under the class label "A-4 accounting: …" and the reading "enlarged local set
  S_onebit(4), weights k/8, sensitivity". Pur-E holds for 2 of 117 and fails for 115. The check confirms that the pure
  composite states are the 4 point masses and that none of the 54 added states has a purification.
- **A3-CLC4-X1.** CL-C4 at x₀ = (1,) has full access, 10 induced maps and 5 reversible ones. Both ordered pairs of B
  point masses are connected by 'perm[id] ; perm[flip]', and the reversible maps are transitive on the 4 point masses
  (x, h). This matches the review of `d924b5bb` (`clc4_x1.out`) and the review of `390e252f` (`purU_check.out`).
- **A3-COMP-U.** This is the composite-level search with A idle (A does perm[id], and the global φ acts on A), over
  sequences of length ≤ 4. Every (A = δ_a, B: δ_b → δ_b′) is connected for K-SWAP and CL-C4, by the same sequences as
  the review of `390e252f` (`purU_check.out`).

**371c402: check total.** The total is 30 PASS, not 24 PASS: the six N5 checks are new. K-PURPOS is the same check
with a stronger condition. The A1-SCOPE line and the final HOLDS line are unchanged; the A1-SCOPE line is now line 400.

## Countercontrol mutation (scratch copies of the node directory; not committed)

| mutant | change in `puru_text` | result |
|---|---|---|
| M1 | status forced to `'holds'` | K-PURPOS FAIL: the removed-maps countercontrol reads 'holds', and the non-product fixture reads 'holds'. "section 6.10: VOID", 0 realization lines, `P8S1  FAILS (1 checks failed)`, exit 1 |
| M2 | r1 rule `'fails' if (failed or undecided)` | K-PURPOS FAIL: the non-product fixture reads 'fails'. VOID, 0 realization lines, exit 1 |
| M3 | vacuous branch returns `'holds'` | K-PURPOS FAIL: the one-purification fixture reads 'holds'. VOID, exit 1 |

Mutant M1 is the review's M6, which survived against `p8s1_r1.py`.

## Replay

`python3 -I -B p8s1_r2.py` was run twice from `probe/` on Python 3.13.16, about 97 s per run. The two outputs are
byte-identical, sha256 `b5ce288c3ed13658198a3a605387a06d76e6270b18923d6129350265426bd951`. The r1 output is reproduced
byte for byte from a checkout of `d924b5bb` with `python3 -I -B p8s1_r1.py`.
