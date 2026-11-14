ACCEPT — `OBL-RO3-2-r2.md`, `RESPONSE-OBL-r1.md` and `RO3-INVENTORY-r4.md` at `ef8d353e4c05e6e4de2f813478bc279f3fa00eb4` (PR #1303); two nonblocking nits

# Focused confirmation review: OBL-RO3-2 r2 and RO3-INVENTORY r4

- **Reviewer.** The independent reviewer of r1 (`REVIEW-OBL-r1.md`). Paper-only and read-only: no
  computation, no Lean build, no edits.
- **Scope.** The four checks the coordinator asked for, and the m7 question. Steps 1–8, which r1's
  review confirmed, were compared line by line in the diff and are unchanged.

## What changed between `76ca4c3d` and `ef8d353e`

- **Commits.** Two, both single-parent:
  - `62048070` adds `REVIEW-OBL-r1.md` and one README row. The file is byte-identical to the review
    as delivered.
  - `ef8d353e` adds `OBL-RO3-2-r2.md`, `RESPONSE-OBL-r1.md`, `RO3-INVENTORY-r4.md` and three README
    rows.
- **Files left unchanged.** `OBL-RO3-2-r1.md`, `RO3-INVENTORY-r1.md`, `-r2.md`, `-r3.md`,
  `REVIEW-r1.md` and `RESPONSE-r1.md` are blob-identical to `76ca4c3d`.
- **README hashes.** The SHA-256 values for `OBL-RO3-2-r2.md`, `RO3-INVENTORY-r4.md` and
  `REVIEW-OBL-r1.md` match the files.

## 1. R1 applied at every place that rests on it: confirmed

The changes are in `OBL-RO3-2-r2.md`.

- **§3.2 (lines 233–260).**
  - The heading is now "`F` has infinite order; periodic points are `μ`-null".
  - The subsection states Poincaré recurrence almost everywhere, the `d = 2` fixed-point example and
    the `d = 1` case, the null-set proof by ergodicity and full support, and what 3.2 does not claim.
  - The writer's remark about `p = 2` (line 250) is correct: `2α^{-1} = 0`, so the equation is
    `Au = 0`, and the recursion still runs both ways.
  - The countability sentence is gone.
- **§6, summary row (line 377).** Updated to match §3.2.
- **§4.1 (lines 320–322).** The torus's null measure is now derived from its finiteness and the
  absence of atoms. It cites 3.2 only for the null set of periodic points. Correct.
- **No other place rests on R1.**
  - In r2, no other passage uses the overstatement. §3.4, §3.5 and §7 were checked, and a grep finds
    no surviving "microscopic recurrence", "refuted on `X`" or countability claim.
  - In the inventory, the only related statement is the 1.1 I-qloc context, at r4 line 153: "no
    nonzero finitely supported configuration is periodic, so `φ^L ≠ id`". It remains true.
  - Line 154 (I-meas, "open as a microscopic statement") and line 440 (Poincaré recurrence for
    I-nonorm) are consistent with the corrected 3.2.
  - §7 of r2 proposes moves only for 1.2, 1.3 and 2.3, not for 1.1.

## 2. m1–m8: all applied

- **m1, line 342.** Order 4 for odd `p`; the swap, of order 2, for `p = 2`. Correct.
- **m2, lines 313–319 and line 341.** The `p ∤ L, L ≥ 2` case is cited to SM:296, and the `p | L`
  case follows from finiteness of the group. Correct.
- **m3, lines 158–163, with lines 339–340 and 318.**
  - The scope note gives the two facts that 4(b) uses: Haar orthonormality, and characters mapping
    to characters. Both hold on every compact abelian group.
  - The countercontrol rows and §4.1 cite the note.
- **m4, lines 221–228.** The cell-conditioned convention is stated. The coincidence with Main's
  maps is restricted to `π = res_Λ`, and the coarse-grained case is excluded. Correct.
- **m5, lines 263–275.** "Unavailable" replaces "refuted". The near-return variant is added.
  - The late-time exclusion is valid. Failure for a single root suffices, so the stated bound
    `δ < min_a (1 − μ(C_a))` is sufficient, though stronger than needed.
  - The bounded-time case is open.
- **m6, line 352.** (ii-b) is now "proved on paper from the definitions on `main`; not
  kernel-checked". The calculation matches the definitions:
  - `emb` (`QuasilocalAlgebra.lean:242–245`) on `diag g` gives `g(glob Λ s) δ_{patch Λ s (glob Λ s)}`;
  - `heis` (:999), with `permOp` (:966) and `permOpInv_apply` (:981), gives `heis Φ D_f = D_{f ∘ φ}`;
  - `leap` gives `φ = F`.

  See n1 and n2.
- **m7, lines 98–104.** See the m7 section below.
- **m8, r4 line 408.** "This route is not checked here." Correct.

## 3. r4 against r3: confirmed

`diff RO3-INVENTORY-r3.md RO3-INVENTORY-r4.md` has three hunks:
- the title, r3 → r4;
- the header, which describes the r4 change and moves r3's own header under "r3's history";
- line 401/408, m8's wording.

There is no other difference.

## 4. Nothing else changed: confirmed

Every hunk of `diff OBL-RO3-2-r1.md OBL-RO3-2-r2.md` is one of the following:
- the title and the header, which lists the changes;
- R1 (§3.2, §4.1, §6);
- m1–m7 as above;
- the §5 closing note and the §7 I-qloc sentence, which separate (ii-a) and (ii-b) from (ii-c) as a
  consequence of m6;
- the §8 row for the review.

Steps 0–8, §3.1's argument, §3.4 and §3.5 are verbatim. The README gains only the four rows.

## m7: the unmet mandate item

- **Stated plainly.** Lines 98–104 say, addressed to the owner:
  - that the mandate's requirement to verify Halmos and Rokhlin from primary sources "is not met";
  - that neither the writer nor the reviewer consulted the texts;
  - that the named textbook treatments were not consulted either.
- **Consistent with §1.** The section heading (line 74) and lines 92–97 say the same thing.
- **The direct proofs are unaffected.**
  - The disclosure attaches only to the attribution of (H) and (R).
  - Step 4 proves, from S1–S3, exactly the two implications the result uses, and §6 labels Step 4
    "proved, given S1–S3". No step cites either criterion as an input.
  - Whether the classical theorems are stated as the sketch says therefore bears on no step.
- **Assessment.** The accepted proofs stand, and the owner is correctly told that one mandate item is
  open. Whether the unmet item blocks acceptance of the unit is a governance question for the owner,
  not a mathematical one.

## Nonblocking nits

- **n1, line 352.** "The one identity assumed here and not looked up", `patch Λ s (glob Λ s) = s`, is
  the kernel theorem `patch_glob` (`QuasilocalAlgebra.lean:136`). Cite it and drop the caveat.
- **n2, line 352, step (3).** Passing from `heis (emb Λ (diag g)) = D_{g ∘ res_Λ ∘ F}` to the trace
  of `transported Φ Λ (diag g)` uses two further facts:
  - that a stage operator determines its matrix (for example through `kern_patch`, :178);
  - that the matrix here is diagonal, with entries `g ∘ res_Λ ∘ F` on `Conf (hat Φ Λ)`.

  The step is routine, but one clause should name it.
