# Delta review of the G1 correction, PR #1274

**Verdict: ACCEPT WITH CHANGES.**

The mathematics of the final §3.1 sentence (`NEW-RESULTS.md`:332–335) and of the scope line
(:302–310) is correct. Every one of items (i)–(vi) checks by hand. The scope line meets the
requirement of ChatGPT review 5900794367, and the copied text is byte-for-byte unchanged.
`review/CONFIRM-CORR322.md` is the receipt that the r3 response answers.

The changes are bookkeeping in `STATUS.md`:

- four line references are stale at `bb80e420` (R1);
- the header and the record table still name the `d015131d` texts as the accepted record (R2);
- the verification-status pointer names the wrong "scope line" (R3).

One scope point stays open. The copied X5 sentence (:275–276) was flagged in CONFIRM-CORR322 and
is still not covered (C1, recommended).

## Object

- **Branch and head.** Branch `research/optc-1230-1232-20261113` at
  `bb80e4201c9917be0a668ced71dedcfe9c2f7aa6`, read from a detached worktree. Nothing was written to
  the repository.
- **Deltas.** `d015131d..0b68c9e1` (Δ30, `STATUS.md`, review files) and `0b68c9e1..bb80e420` (scope
  line, Δ31, STATUS cross-references, `review/CONFIRM-CORR322.md`). Across `d015131d..bb80e420`,
  only the record directory changes (9 files). `DEPENDENCIES.md`, `PROVENANCE.md`,
  `review/REVIEW-r1.md`, `review/RESPONSE-r1.md` and `review/CONFIRM-r2.md` are unchanged.
- **GitHub records read first-hand.**
  - ChatGPT review 5900794367 (`amaybaum`, 2026-11-14T02:17:05Z, commit `0b68c9e1`, REVISE).
  - ChatGPT review 5895564670 (`d015131d`).
  - #1169 comment 6872005186 (`amaybaum`, 2026-11-14T04:53:06Z).
  - #1274 comment 6865575359 (`amaybaum`, 2026-11-13T21:39:25Z).
  - #1274 checkpoint comment 6865777592.
  - #1169 comment 6865177667, for the OQ-1 quote.
- **Method.** All mathematics was checked by hand. No script was run on any OI rule. Git was used
  only for diffs, blob ids and digests.

## 1. Mathematics

Definitions (§0.3, :92–107):

- A frame matrix of E is any T with L∘E = T∘L.
- Spanning means Span(L(encoded states)) = ℝ^{Ω_enc}.
- Without spanning, the test asks whether E has a nonnegative representative.

**(i) T3 gives uniqueness. Holds.** If L spans, T is determined on all of ℝ^{Ω_enc} by T(Lρ) = L(Eρ).
For the qubit tetrahedral frame, L is a linear bijection from the 4-dimensional real span of the
states onto ℝ⁴, so T = L E L⁻¹ exists and is unique.

T3 also gives inclusion: an induced T is nonnegative, so E is in the class. It gives no exclusion.
Membership in the class is fixed by the map ("the E_f class is fixed by the map"), but nothing in T3
puts any given non-diagonal-preserving map outside the class.

**(ii) The cyclic rotation passes on the spanning tetrahedral frame. Holds.**

- C(x,y,z) = (y,z,x) is an even coordinate permutation, so det C = +1 and C is the Bloch action of
  a unitary.
- C preserves the sign product. It fixes (1,1,1) and cycles (1,−1,−1) → (−1,−1,1) → (−1,1,−1) →
  (1,−1,−1).
- With r = σ/2, r_k·r_m = 3/4 for k = m and −1/4 otherwise. So F_kj = 1/4 + r_k·(C r_j) is 1 when
  r_k = C r_j and 0 otherwise. The frame matrix is a permutation matrix, unique by spanning.
- C sends Bloch (0,0,1) to (0,1,0), so it is not diagonal-preserving.

**(iii) S2b gives −2/5. Holds.** For the rotation about z with cos 3/5 and sin 4/5:

    σ_k·Rσ_j = (3/5)(p+q) + (4/5)(σ_k2σ_j1 − σ_k1σ_j2) + pq,  with p = σ_k1σ_j1, q = σ_k2σ_j2.

The even-sign constraint gives σ_k3σ_j3 = pq. The three cases:

| Case | Middle term | Value |
|---|---|---|
| p = q = 1 | 0 | 11/5 |
| p = q = −1 | 0 | −1/5 |
| p = −q | ±2, so (4/5)(±2) | ±8/5 − 1 |

The minimum is −13/5, attained at j = (1,1,1), k = (1,−1,−1). Then F = 1/4 − 13/20 = −2/5.

The record's derivation of F_kj = 1/4 + r_k·(R r_j) also holds: Σ r_k r_kᵀ = I, because the
off-diagonal sums vanish, and Σ r_k = 0.

**(iv) Octahedral: the Hadamard passes; not every rotation does. Holds.**

- (x,y,z) ↦ (z,−y,x) maps ±e_x ↔ ±e_z and ±e_y ↦ ∓e_y. It is a permutation of the six points, so
  it has a nonnegative representative.
- For a general R, take a row of a representative for the output point e_a. Write its entries as
  α_i ± β_i on ±e_i. Matching (1 + (Rᵀe_a)·r)/6 forces Σα_i = 1/2 and β_i = R_ai/2.
- Nonnegativity needs α_i ≥ |β_i|, hence Σ_i |R_ai| ≤ 1. For a unit row this forces a single entry
  ±1.
- So only signed-permutation rotations pass. The S2b rotation does not.
- Independent cross-check: suppose R⁻¹n_i is not an axis point for some i. Take the input pure
  state with Bloch vector −R⁻¹n_i. Every input probability is positive, while output i is 0. A
  nonnegative T then needs row i to vanish, which is impossible because p_i(Rr) is not identically
  0.
- The record states no "every rotation" claim for the octahedral frame. :334–335 correctly reserve
  "every unitary" for the Husimi frame.

**(v) Husimi: every unitary acts as a point map. Holds.**

- UρU† has Bloch vector Rr, so its density at n is 1 + (Rr)·n = 1 + r·(Rᵀn).
- Hence L(UρU†) is the pushforward of L(ρ) under n ↦ Rn, which preserves area.
- That pushforward is a nonnegative (Markov) representative, for every U.

**(vi) The tetrahedral frame plus a zero-probability point. Holds.**

- L(ρ) = (p₁,…,p₄,0). The image lies in {x₅ = 0}, so it does not span ℝ⁵, and L is injective.
- Any T with T L = L H has its 4×4 block fixed: the first four coordinates span ℝ⁴. Row 5 is 0 on
  columns 1–4. Column 5 is free.
- The fixed block is the tetrahedral Hadamard matrix, F_kj = 1/4 + (σ_k1σ_j3 − σ_k2σ_j2 +
  σ_k3σ_j1)/4. At j = (1,1,1), k = (−1,1,−1) it equals 1/4 − 3/4 = −1/2.
- So every representative has the entry −1/2, and the test excludes the Hadamard on this
  non-spanning frame.
- The split-point variant also forces −1/2: the entry sits at (2,2), outside the split index.

**The sentence at :332–335.** Each clause is supported for the stated objects:

- "unique ... fixed by the map (T3)";
- "on the tetrahedral frame it excludes a rational rotation (S2b)";
- "need not separate: on the octahedral and Husimi frames ... (S2c, S2)";
- "on the Husimi frame every unitary does".

**The scope line at :302–310.** Its two mathematical claims are (vi) and (ii). Both are correct.

## 2. Does the scope line meet review 5900794367?

- **Not a universal non-separation claim. Met.** ":302–310 They do not state that the test fails to
  separate on every non-spanning frame", followed by the zero-point witness.
- **Examples of frame-relativity. Met in substance.** "They are supported for the frames they name:
  on the octahedral and Husimi frames …".
- **T3 gives uniqueness, not guaranteed exclusion. Met.** "Nor does T3 give exclusion on spanning
  frames: it gives uniqueness of the frame matrix", with the cyclic rotation as witness.
- **Copied text unchanged. Met.**
  - :1–301 at `bb80e420` are identical to :1–301 at `d015131d`. This covers the Finding at :265–269
    and the whole Argument at :271–296.
  - The hand-check and Hypotheses blocks (:312–331) are identical to `d015131d`:302–321.
  - The tail after "What it adds" is identical apart from the re-wrap of that paragraph's last line.
- **Owner boundary. Met.** c.6872005186 asks to "Add the narrow clarification for the earlier copied
  passages". The edit is one paragraph plus its Δ row and STATUS cross-references. No T5 expansion,
  physical operation or OI↔QM claim is added.

## 3. Findings

### R1 (required). Four line references in `STATUS.md` are stale at `bb80e420`

The bb80e420 commit message says "STATUS cross-references and line numbers updated". Only :111 and
:134 were updated.

Three rows were written against `d015131d`. They were off by 3 after Δ30 and are off by 13 now. Row
3.1 is broken by the inserted scope line.

| `STATUS.md` | Current | Content | Replace with |
|---|---|---|---|
| :123 (row 3.1) | "hand checks in `NEW-RESULTS.md`:298–316" | :298–300 and :312–326; :302–310 is now the scope line | "hand checks in `NEW-RESULTS.md`:298–300 and :312–326" |
| :124 (row 3.2) | "S3 and Husimi bound: `NEW-RESULTS.md`:358–365" | :371–378 (from "Hand checks for the [X] tag and the Husimi bound" to "where it is 1/4 < 1/2") | "S3 and Husimi bound: `NEW-RESULTS.md`:371–378" |
| :127 (row 5) | "S4 arithmetic: `NEW-RESULTS.md`:497–500" | :510–513 | "S4 arithmetic: `NEW-RESULTS.md`:510–513" |
| :128 (row 6) | "S7 arithmetic: `NEW-RESULTS.md`:591–595" | :604–608 | "S7 arithmetic: `NEW-RESULTS.md`:604–608" |

All other `NEW-RESULTS.md` references in `STATUS.md` are correct at `bb80e420`: :3–15, :9, :11–15,
:33–36, :215–224, :302–310 and :332–335. Those in `CHANGES.md` Δ31 (:302–310) are also correct.

### R2 (required). The header and the record table identify the `d015131d` texts as the record

`STATUS.md`:3–5 reads: "It does not change `NEW-RESULTS.md`, `DEPENDENCIES.md`, `PROVENANCE.md`,
`CHANGES.md` or any file in `review/`; their texts at `d015131d…` are the accepted texts."
:11–19 then gives the `d015131d` blobs (`NEW-RESULTS.md` 627 lines, `CHANGES.md` 70 lines).

At `bb80e420`, `NEW-RESULTS.md` and `CHANGES.md` differ from those blobs by Δ30 and Δ31, under owner
decisions c.6865575359 and c.6872005186. The note never says so outside the scope paragraph, so a
reviewer checking the landing against the table finds mismatched blobs.

Replace :3–5 with:

> This note gives the standing of the records in this directory. `DEPENDENCIES.md`, `PROVENANCE.md`
> and the files in `review/` present at `d015131d6aad4ab09f80a7a78eb123384430186d` are unchanged
> from that commit. `NEW-RESULTS.md` and `CHANGES.md` differ from it only by `CHANGES.md` Δ30 and
> Δ31 (owner decisions #1274 c.6865575359 and #1169 c.6872005186).

After the sentence ending at :19 ("… `c3b5f37a354bb26437e2e0165c576a347a63c153`."), add:

> The two files changed by Δ30 and Δ31 are, at the head that carries them:
>
> | File | Blob | SHA-256 | Lines |
> |---|---|---|---|
> | `NEW-RESULTS.md` | `0933f50ef2979d8afd5e2a7c43516f37f7912564` | `38417d1142a233e3d34f1793c89df212695641c7a39eaf813a074e6cfafbb22a` | 640 |
> | `CHANGES.md` | `a84018ba3ee11a8904639b676bc029d3168487cc` | `9cf6ccbf8d69acb42763883faa7f1ac0986f643a621e27ba41171c63c4eeb6f7` | 74 |

These values are measured at `bb80e420`. Re-measure them if R1 or C1 changes either file. R1 changes
only `STATUS.md`. C1 changes both files.

### R3 (required). The verification-status pointer names the wrong "scope line"

`STATUS.md`:110–111 reads: "see the scope line on `NEW-RESULTS.md`:332–335 and `CHANGES.md` Δ30."
Since Δ31, "scope line" names :302–310 in `CHANGES.md` Δ31, in `STATUS.md`:139 and in the commit
message, while :332–335 is the narrowed "What it adds" sentence. The claim "No carried statement is
known to be invalid at the scope of its witnesses" depends on the copied passages' scope, which
:302–310 states.

Replace with:

> see `NEW-RESULTS.md`:302–310 and :332–335 and `CHANGES.md` Δ30 and Δ31.

### C1 (recommended). Scope the copied X5 sentence and state the content directly

- **The gap.** CONFIRM-CORR322 §4 and the r3 open point named two copied passages: :275–276 ("its
  control X5 (a negative entry in the Hadamard's frame matrix) is a property of spanning frames")
  and :290–292. Review 5900794367 names :265–269 and :290–292. The scope line covers the Finding and
  the closing paragraph, not the X5 sentence.
- **Why X5 matters.** It admits an overbroad reading in both directions:
  - Read as "only spanning frames": the scope line's own zero-point witness is non-spanning and
    carries X5, since every representative has −1/2.
  - Read as "every spanning frame": a regular tetrahedron with a 2-fold axis along (1,0,1)/√2 is
    Hadamard-invariant (CONFIRM-CORR322 §1). The record does not carry that fact, and the
    replacement below does not use it.
- **Wording.** "They do not state that …" makes a claim about the copied text that its literal
  wording at :290–292 does not bear out. Stating the mathematical content is more robust.
- **Wording.** "Nor does T3 give exclusion on spanning frames" can be misread as "spanning frames
  exclude nothing". The tetrahedral frame does exclude, by S2b. The intended content is that T3 does
  not make the test exclude every non-diagonal-preserving unitary.
- **Citation.** The −1/2 hand check is in `review/NOTES-STATUS.md` r2, "Finding 1 checked
  independently". The scope line reaches it only through `CHANGES.md`.

Replace :302–310 with:

> **Scope of the copied passages.** The Finding, the Argument's sentence on X5 and the Argument's
> closing paragraph above are copied without change. The non-separation they state is shown for the
> frames they name: on the octahedral and Husimi frames non-diagonal-preserving unitaries have
> nonnegative frame representatives (S2c, S2). It does not hold on every non-spanning frame: the
> tetrahedral frame extended by a point of probability zero does not span, and every frame
> representative of the Hadamard on it has the entry −1/2 (`review/NOTES-STATUS.md`, r2, finding 1;
> `CHANGES.md` Δ30), so X5 is not confined to spanning frames. Nor does spanning make the test
> exclude every non-diagonal-preserving unitary: T3 gives uniqueness of the frame matrix, and the
> cyclic rotation `(x,y,z) ↦ (y,z,x)` permutes the tetrahedral points, so it passes the test
> although it is not diagonal-preserving (`review/NOTES-STATUS.md`, r3).

If C1 is taken, make these follow-on edits:

- **Δ31 reason cell.** Replace "the copied Finding (S:278) and the Argument's closing paragraph
  (within S:102–108)" with "the copied Finding (S:278), the Argument's sentence on X5 (S:102) and its
  closing paragraph (within S:102–108)".
- **STATUS.md:138–139.** Replace "The copied Finding and Argument of §3.1 carry the same scope" with
  "The copied Finding, X5 sentence and closing paragraph of §3.1 carry the same scope".
- **Line numbers.** If the paragraph's line count changes, update :302–310, :332–335 and the R1
  numbers wherever they are cited.

If C1 is declined, the present scope line meets the review's stated requirement. Then only the
citation fix is recommended: replace "(`CHANGES.md` Δ30, Δ31)" at :307 with
"(`review/NOTES-STATUS.md`, r2, finding 1; `CHANGES.md` Δ30)".

### C2 (recommended). Name the retained receipt and the new reviews outside `review/`

`review/CONFIRM-CORR322.md` is retained, but no non-review file names it. Review 5900794367's
provenance note asks to "retain/identify" it. Δ30's reason cell describes only the non-spanning
clause; r3 records this as an open owner point.

**Δ30 reason cell.** After "…and `review/NOTES-STATUS.md`.", insert:

> The spanning clause is narrowed because T3 gives uniqueness of the frame matrix, not exclusion:
> the rotation (x,y,z) ↦ (y,z,x) permutes the tetrahedral points (`review/CONFIRM-CORR322.md`
> finding 1; `review/NOTES-STATUS.md` r3).

**STATUS.md review trail (:20–30).** After the CONFIRM-r2 bullet, add:

> - `review/CONFIRM-STATUS.md` (committed at `f17020af`), `review/RESPONSE-STATUS.md` (`4cb2618d`),
>   `review/CONFIRM-STATUS-r2.md` (`040d929e`), `review/RESPONSE-CORR322.md` (`0b68c9e1`) and
>   `review/CONFIRM-CORR322.md` (blob `9375d5e6`, committed at `bb80e420`; the check of `040d929e`
>   that the r3 response answers): focused checks of `STATUS.md` and of Δ30, with the writer's
>   responses and hand checks in `review/NOTES-STATUS.md`.
> - ChatGPT review 5900794367 (posted under `amaybaum`, 2026-11-14T02:17:05Z) at `0b68c9e1`: REVISE,
>   for the scope line that Δ31 adds.

**STATUS.md Dependencies table (:164–166).** It lists "The references this note adds" but omits
#1274 c.6865575359, #1169 c.6872005186, review 5900794367 and the commits `f4c300bc` to `bb80e420`.
Add them to the governance-provenance row, the review row and the commits row respectively. They
are cited at :137–140 and in Δ30 and Δ31.

### Nits (optional)

- **N1.** The scope line's "the frames they name" lists the octahedral and Husimi frames. The
  closing paragraph also names a profinite carrier, reached by transporting the Husimi frame through
  a Borel isomorphism. That claim is the Husimi frame transported and is consistent with the scope
  line; "(and the Husimi frame transported to a profinite carrier)" would make the list complete.
- **N2.** `review/RESPONSE-CORR322.md`'s diff shows the STATUS line references as :322–323. The
  committed STATUS at `0b68c9e1` reads :322–325, as the checkpoint comment 6865777592 states. This
  is a response-file artifact; no change is needed.

## 4. Consistency of quotes and ids

- **Δ30.** "Owner decision #1274 c.6865575359" resolves. The comment authorizes a forward edit of
  :322–323 with a Δ row and STATUS alignment.
- **Δ30's spanning clause.** The clause went beyond the literal wording of c.6865575359. It is
  covered by c.6872005186: "The corrected Δ30 wording is scientifically valid."
- **Δ31.**
  - "ChatGPT review 5900794367 (`amaybaum`, 2026-11-14)" is correct (state COMMENTED, verdict
    REVISE, commit `0b68c9e1`).
  - "Owner decision 2026-11-14, recorded at #1169 c.6872005186" is correct. The comment quotes the
    owner verbatim and lists 5900794367 at `0b68c9e1` with the :265–269 and :290–292 requirement.
  - "S:278" for the Finding and "within S:102–108" for the closing paragraph match the record's
    labels (:265, :271).
- **CHANGES header.** "Δ31 adds a scope line for copied text and changes none" is true.
- **STATUS.md.**
  - Row 3.1 (:75) and the claim sentence (:92–94) match :332–335.
  - The scope paragraph (:134–140) cites c.6865575359 and c.6872005186 correctly.
  - The OQ-1 quote at :57–59 matches #1169 c.6865177667.

## 5. Provenance of `review/CONFIRM-CORR322.md`

- **Digest.** Blob `9375d5e6994d120018c5be50436015a0469c9d7f`, SHA-256
  `fa3e09eb665b623a15466dac0946be99a707439789643102dadd29adb40d7f24`, 165 lines, added at `bb80e420`
  and unchanged since. Neither `RESPONSE-CORR322.md` nor `NOTES-STATUS.md` r3 records a digest, so
  byte identity cannot be checked from the repository alone.
- **Working copy.** The reviewer's working copy outside the repository has the same SHA-256. Its
  mtime is 2026-11-13T21:44:44Z, after `040d929e` (21:41:00Z) and before `0b68c9e1` (21:49:41Z).
  That timing is consistent with r3 answering this text. This is provenance only; it is not on
  `main`.
- **Object.** It names `040d929e` and owner comment c.6865575359, matching r3's object line.
- **Finding 1, first clause overclaims.** Applied verbatim: :332–335 equal CONFIRM-CORR322:125–128,
  with the same line breaks. Its hand checks match r3 items 1–3: the cyclic rotation, "T3 gives
  uniqueness … not exclusion", and the octahedral Σ|R_ai| ≤ 1 argument. I re-derived each in §1.
- **Finding 2, STATUS row 3.1 and claim sentence.** Applied verbatim at :75 and :92–94. The optional
  scope-paragraph addition was not applied and is listed as an owner point in r3. It is now
  partly realized by :302–310, which uses the cyclic rotation rather than the Hadamard-invariant
  tetrahedron.
- **Finding 3, header clause.** Applied verbatim in `CHANGES.md`:5–6.
- **Formatting nit, re-wrap.** Applied.
- **§4, copied sentences :275–276 and :290–292.** Recorded as an open owner point in r3. :290–292 is
  now scoped by Δ31; :275–276 is not (C1).
- **CONFIRM-STATUS and CONFIRM-STATUS-r2.** Both are also byte-identical to the reviewer's working
  copies.

## 6. Register

- The scope line, Δ31 and the STATUS additions use the record's neutral technical register. They
  contain no self-assessment, no capitals for emphasis and no "now / no longer / formerly"
  narration.
- "Copied without change" states provenance in the same idiom as the record's "(copied; …; no
  mathematical change)" labels.
- "They do not state that …" is interpretive. C1's replacement states the content instead.
- No claim goes beyond T5(c) or G1 scope. All added mathematics concerns qubit frame
  representations, with no OI hypothesis, no physical operation and no OI↔QM result.

## Summary

| Item | Result |
|---|---|
| Mathematics (i)–(vi), :332–335, :302–310 | correct |
| Scope line against review 5900794367 | requirement met; copied text unchanged |
| `STATUS.md` line references at `bb80e420` | four stale (R1) |
| `STATUS.md` header and record table | name `d015131d` texts as the record (R2) |
| `STATUS.md` verification pointer | names the wrong scope line (R3) |
| Owner quotes and review ids | accurate |
| CONFIRM-CORR322 receipt | consistent with r3; byte-identical to the reviewer's working copy |
| Register | neutral; no scope beyond G1 |

R1–R3 are text-only edits to `STATUS.md`. C1 and C2 are recommended. No merge is implied.
