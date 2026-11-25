# Focused confirmation review of GAMMA-1 unit G1 r6

**Object.** The review covers three files, retained on PR #1294 at `9aa994db4`. The local copies match
these blobs.

| File | Blob |
|---|---|
| `GAMMA-G1-r6.md` | `3d56aa18` |
| `RESPONSE-GAMMA-G1-r5.md` | `1be1807a` |
| `GAMMA-G1-r5.md` (the base, unchanged) | `4f3482f9` |

**Reviewer.** Claude, the non-author reviewer of r5 (`REVIEW-GAMMA-G1-r5.md`, cited RG1r5). The review
is read-only.

**Method.** I read the full r5→r6 diff (121 lines) and checked each changed passage against RG1r5.

## Verdict: ACCEPT

- Findings 1 to 4 are applied as asked.
- Finding 5 is applied, with a correct sentence.
- `−b_j` is held pending owner confirmation, with no Δ comparison against a background target until
  then.
- Nothing else changed.
- One optional pointer is suggested in §2.

## 1. Each item

**Finding 1: applied.**
- §5.4 "Gated targets" and a new §10 item state the herald no-image clause in both directions:
  - against coverage: no image, no agreement;
  - for K1 against falsification: the GRA herald-gated `α_exp ≅ 0.18` cannot yield a counted miss
    against K1's derived-level `α = 1`.
- They also state the limit of the clause. Clock-gated Jacques data are normalized by `μ(𝔈_a)` and
  keep an image on K1, and four blockers remain: X-2's program outside `𝒜_10`, availability, controls
  and AW-σ.
- r5's one-sided phrase "a consequence unfavourable to K1" is removed.

**Finding 2: applied.** §13 has two new rows.
- Row (a): G2 r3 §1.2 and §6.3 give `α = 1`, set against clock-gated X-2 data. Both Jacques values are
  quoted correctly: 0.13 ± 0.01 and 1.00 ± 0.06. The row states that no comparison is made.
- Row (b): the fringe candidate's condition 6 and §6.2's deferral of greenness. The §6.2 row now says
  that the PC-wave law is unchanged but that the criterion it defers to is not.

**Finding 3: applied.**
- The NC-γ1 row states "Not met by `κ^{r5}`". It says the checkpoint is met only by instances declared
  after r5, and that NC-γ5's disclosure "stands in place of it, and does not meet it".
- The NC-γ5 row says that it "discloses … does not certify". It also lists the three grounds and the
  trial count, one added declaration.
- §9 carries the same statement.

**Finding 4: applied as pending.**
- §7.1 adds a "Pending owner confirmation" paragraph. It separates the image `−b_j`, a by-hand
  consequence of §§5.1 and 5.4, from its use as the reference value. It states: "no comparison of `Δ`
  against a target with background is made under either reference value; for `b_j = 0` the two
  coincide."
- The same hold is marked in four further places:
  - PC-wave's required result;
  - NC-γ6's C0 data side;
  - §10 ("merits … does not settle authority");
  - §13.
- §12 quotes question 1 verbatim and marks it **not settled**. It separates out the part of the F10(b)
  reconciliation that follows from r4 §5.4 alone and is therefore not held: `I_AB` ≠ `Δ`, the raw
  route, §5.5's classes, and the background scope of check 5 and of `I_3`. That separation is correct.

**Finding 5: applied.**
- In §5.4 and §7.2, "not invariant under a common rescaling of the counts" is replaced by "`α` needs
  per-gate probabilities, hence the gate count, not only ratios among counts made in integration time".
  The new sentence is correct.
- r5's sentence held only if `N_A` was left out of the rescaling. If `N_A` is rescaled too, `α` is
  invariant. So r5's sentence was false on the natural reading, and the replacement is warranted.

**Finding 6 (optional): not applied, and declared as not applied.** Acceptable.

**Nothing else changed.**
- Every diff hunk maps to findings 1 to 5, to the header note, or to the §11 provenance row.
- No number, definition, rule or control changed outside these items.
- No verdict on γ or D-1 appears.

## 2. Optional pointer (low)

§5.4's all-paths-blocked count item describes the raw route by which a `Δ` comparison with a background target
would be made. It does not point to §7.1's hold. A one-clause pointer would stop a reader from applying
§5.4 alone: "(any such `Δ` comparison is held, §7.1, pending owner confirmation)".

## 3. G2 owner question 1, in plain terms (for the owner)

1. With no background, the classical one-path-per-particle control C0 predicts an interference defect `Δ` of
   exactly 0. G1's own rules say that a source's stated detector background must be added to every
   model's prediction rather than subtracted from the data. With the background added, C0's prediction
   becomes `−b_j`, not 0.
2. Each answer changes what C0 is tested against:
   - **Yes** tests C0 against `−b_j`. C0 then fails only where the measured raw defect differs from its
     own background-shifted prediction, so background alone can no longer make C0 look refuted.
   - **No** keeps 0 as the reference. Then, for any target with background, C0 is either "refuted" by
     the background alone, if raw data are compared, or cannot be compared at all, because comparing
     against background-subtracted data is barred.
3. The raw-direct rule (§A.24) compares data as measured and puts the background into the model, so it
   favours "yes". The two answers give the same result wherever the background is zero.
