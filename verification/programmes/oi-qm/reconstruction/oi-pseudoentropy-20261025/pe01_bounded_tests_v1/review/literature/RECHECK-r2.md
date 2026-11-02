# Re-check of the PE-01 tag annex, r2

- **Objects:**
  - `pe01lit/TAGS-r2.md`. The reviewed r1, `TAGS.md`, has sha256 `ac3cdffe…eb2e`, matching r2's provenance line.
  - `pe01lit_check/linear_rows.py`, sha256 `82014750…4fdb`, matching r2.
  - Its output `out_n3_7.txt`, sha256 `3ac8448a…8671`, matching r2.
  - `pe01lit/REPORT-literature-replacement.md`, which is present.
- **Against:** my `REVIEW.md` (R1–R5, N1–N8), `results/verdict.txt` section 1, PLAN §3, and W3 and W8, re-read
  through my own extractions.
- **Method:** read-only, with Python run under `-I`.

## Verdict: ACCEPT WITH NITS

Every required change is applied correctly. The 222-row extension is justified row by row, as set out below. The
two non-adoptions are acceptable. W8 stays "covered in kind", with the outline qualifier. The REPORT replacement is
accurate. Its only problem is one heading that is broader than r2, and that heading is the one change below that
must be made before the replacement is used.

## 1. The required changes

| Item | Status |
|---|---|
| R1, AGHP reason (2) | Applied verbatim. |
| R1′, the extension | Applied. It is mirrored in "Tag for (ii)" and in §4(ii). |
| R1″, RSV and BDVY | Applied. RSV gains one sentence on `G_filt` and `G_clk`, "at most an upper bound on advantage, which RSV does not evaluate". That sentence is accurate and no stronger. |
| R2, W8 | Applied in §2a, §3(i) (row and bullets), §3(ii) (the "no bearing" row) and §4(i). W8's hash `8f7a5849…68856` equals mine. |
| R3 | Applied: the Chambers–Gollmann DOI, "not attempted", both WEA rows, and the Kholosha title. Crossref confirms 10.1007/3-540-45311-3_27, pp. 287–296, as stated. |
| R4 | Applied in §5. |
| N1–N8 | Applied. N3 adopts the scope statement only (§1(ii), last bullet); see §3 below. |

Two corrections improve on my review:

- **Coincidence of the distributions.** r2 states that ν coincides with AGHP's irreducible-uniform distribution at
  n = 3, 5, 7, not just at n = 3 as I wrote. That is correct: when 2ⁿ − 1 is prime, every irreducible polynomial of
  degree n is primitive.
- **Lemma 1's L1 term.** r2 reconstructs it as (2^k − 1)^{1/2}ε, with a note that the symbols are reconstructed. That
  is consistent with the extraction (`txt/aghp_goldreich.txt:194–197`).

**Quotes.** I re-checked the new W8 quotes in my own extraction, and all are verbatim on the stated printed pages:

- p. 2: "Of course, the fault injected…" and "Our aim is to discover the contents of the control register."
- p. 3: "We guess the position of the flipped bit…"
- p. 1: "This is a report on work on progress".
- p. 5: "The yet unimplemented attack ideas show that".

## 2. The 222-row extension

**Count.** Section 1 of `verdict.txt` has exactly 222 rows on `G_lin`, `G_lin_sib` or the family, in the classes
B3k, B3w, plin_m1–m4(_pred) and emb_m1_passive(_pred). All of them are "untagged". The breakdown is 24 B3k, 18 B3w,
144 plin and 36 emb_m1, which is r2's list exactly. No B1 K1 row (L1), U row, B2 row, B4 row, emb_m2/m3_passive row,
`G_filt` row or `G_clk` row is included. Rows that are nonlinear in the record stay untagged, as r2 states.

**Formula matches.** I checked every row by script against r2's closed forms:

- B3k: K_zero = min(2ⁿ − 2, 127).
- B3w: K_zero = n.
- plin_m1, plin_m1_pred, emb_m1_passive and emb_m1_passive_pred: K_zero = 2^{n+1} − 4.
  - The emb_m1_passive K0 rows at n = 8 sit at their 255 cap.
- Every K1 row in the four classes has K_1/8 = K_1/4 = K_zero + 1, as the dichotomy predicts: a constant parity
  gives advantage 1/2.
- Mismatches: none. The six rows with a `null` K_δ match by inspection, at caps 127 and 255.

**Script hygiene.**

- It imports only `itertools`, `sys` and `json`. It reads no repository file and no download.
- Its method is sound. Under P a linear statistic MX is uniform on the image of the seed map, and under Q on the
  image of M. The two laws are equal iff the ranks are equal (`linear_rows.py:68–77`).
- It encodes the record as PLAN §1 does: h ← L_p h, then x ← x ⊕ h₀ of the new state (`:52–66`).
- It encodes plin as PLAN §3 does: ρ_x(v) = Av ⊕ xb, with the statistic (v_K, X_K) (`:113–131`).

**Values agree with the measured rows.** The script's n = 3..7 output agrees with every one of the following:

- every per-polynomial plin_m1–m3 K1 value on p_n and p′_n, and plin_m4 for n ≤ 6. For example plin_m2 3/12, 4/12,
  12/8, 36/60, 246/132 and plin_m3 3/3, 4/4, 7/7, 22/7, 24/32;
- every plin_m2–m4 K0-average K_zero: 3/3/3, 4/4/4, 8/5/5, 6/6/6, and 12/7 for m = 2, 3 at n = 7;
- B3k and B3w.

**Rerun.** I re-ran `python3 -I linear_rows.py 6`, and the output is byte-identical to the author's (§5).

**Independent control.** `probe/plin_bf.py` compares exact distributions by brute force over all records, with no
rank computation, on my own enumerator. It gives plin_m2 K1 K_zero = 12 on `G_lin` and 8 on `G_lin_sib` at n = 5,
matching `verdict.txt` and the script.

**Untagged rows that were not computed.** r2 tags them for the right reason: the linearity of the statistic, which
holds by PLAN §3's definitions, not by any computation. The box states both this and the list of rows not computed.
I consider that correct for a covered-in-kind tag, which asserts the mechanism and not the values.

**One clarification is missing (nit RN1).** PLAN §3 defines the plin K0 class over *linear prediction tests* only,
χ(v) = c·v ⊕ e. The script computes the K1 class's firing, any F, minimized over the family. The two K_zero values
agree, and the reason is this:

- Suppose a parity c·v_K is constant and contains no X_K. Then c·v_K = (cA)·v_{K−1} ⊕ (c·b)X_{K−1}.
  - If c·b = 1, the same filter's linear prediction fires at K − 1.
  - Otherwise, recurse on (cA)·v_{K−1}. This terminates, because the parity has a nonzero record form.
- So a K1 firing implies a linear-prediction firing at some K′ ≤ K, and K_zero is defined over all K′ ≤ K.

This explains the observed agreement, but r2 asserts the identification without the argument.

## 3. The non-adoptions

- **(a) "The clock is set by the generator itself rather than by a separate register."** Acceptable, and accurate.
  It is arguably more careful than my wording. Rueppel's step, as W1 describes it, is a function of the register's
  state. G_clk's selector x is a component of the generator's own state (x, h). The following sub-bullets state the
  difference in the selector and the observer's role, so nothing is lost.
- **(b) The N3 predicted 1b bounds.** Acceptable. I offered them for the record only, and they bear on no tag (A3
  item 1).

## 4. The REPORT replacement

The replacement is accurate, and apart from the heading at R-1 it is no stronger than r2:

- W8 is described as an "outline", with the five differences from the cell compressed into three.
- The Rueppel bullets match r2 §5.
- The RSV/BDVY bullet matches r2.
- The candidate-NEW and unread lists match r2 §4.

**Required change (R-1).** Line 24, "**Passive horizons on the linear generators are covered in kind.**", is
broader than r2. r2 leaves the B2, B4d2–3 and emb_m2/m3_passive rows on `G_lin`, `G_lin_sib` and 𝔉_lin untagged.
Replace it with:

> - **Passive horizons of linear statistics on the linear generators are covered in kind.**

Line 28 already carries the restriction ("whose statistic is linear in the record"). Only the heading
over-reaches.

**Nits.**

- **RN2.** Line 1: "(ACCEPT WITH CHANGES; the changes are applied in r2)" narrates the annex's revision history.
  Replace it with "and independently re-checked (`revlit` review and re-check)", or simply with "independently
  reviewed", and keep the review records beside the annex under `review/literature/`.
- **RN3.** Line 28: "every PROVED row … B1 K0 (n = 3, 4)" also covers, in mechanism, the B1 K1 rows, which keep their
  A2 tag L1. Optionally add "(the B1 K1 rows keep their A2 tag)" so that the REPORT does not read as retagging them.

## 5. Rerun of the author's script

I ran `python3 -I pe01lit_check/linear_rows.py 6` from `revlit/`, exit 0.

- **Against the author's n ≤ 6 output.** `rerun_n3_6.txt` is byte-identical to the author's `out_n3_6.txt`, sha256
  `1bce1b27…7be4` for both.
- **Against the cited n ≤ 7 output.** It is also byte-identical to the first four lines of `out_n3_7.txt`, the file
  r2 cites.
- **n = 7.** I did not rerun it, because of its cost (§A.40). Its values were compared against `verdict.txt`
  directly in §2.

## Nits on r2 (non-blocking)

- **RN1.** Add the linear-prediction argument of §2 to the check box, after "their K0-average K_zero, which is the
  minimum over the family". Suggested text:

  > PLAN §3's plin K0 class uses linear prediction tests only. The two K_zero values agree because a constant
  > parity c·v_K without X_K equals (cA)·v_{K−1} ⊕ (c·b)X_{K−1}, so the same filter's linear prediction fires at an
  > earlier K′.

- **RN4.** The status line, "Independently reviewed: ACCEPT WITH CHANGES. Those changes are applied in r2", should
  name this re-check's verdict once it is resolved.

## Evidence (scratch)

- `revlit/linrows.txt`: the 222 rows extracted from `verdict.txt` section 1.
- `revlit/probe/plin_bf.py`: the independent brute-force control.
- `revlit/rerun_n3_6.txt`: my rerun of `linear_rows.py 6`.
