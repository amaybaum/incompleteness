# Focused delta check of `STATUS.md` r2 for PR #1274

**Verdict: ACCEPT.**

- Every finding and nit of CONFIRM-STATUS is applied with the text I specified.
- The split-frame variant is correct.
- The notes label the sympy run adequately as outside scope, not relied on and not landed. Nothing
  in `STATUS.md` rests on it.
- Nothing else changed: the reviewed record files are unchanged since `d015131d`.

Three optional nits follow at the end.

## Object

- **Head.** Branch `research/optc-1230-1232-20261113`, fetched by name with no `--depth` and checked
  out in a detached worktree in the working area. HEAD is exactly
  `4cb2618df0e63184ebe601fd2d28426ef539954c`.
- **History.** `f4c300bc` → `f17020af` → `4cb2618d`.
- **Checks.** The five cheap check scripts were run at the head and all report OK. Nothing else was
  run.

## 1. Each finding and nit is applied as specified

The `STATUS.md` diff `f17020af..4cb2618d` matches the full diff reproduced in
`review/RESPONSE-STATUS.md`, hunk for hunk.

- **Finding 1.** All four parts carry my text:
  - row 3.1 (:75);
  - the claim sentence (:92–94);
  - the "known to be invalid" sentence (:110–113);
  - the scope paragraph on `NEW-RESULTS.md`:322–323 (:134–138).
- **Finding 2.** The basis is stated as "proposed …, pending the owner's ruling under OQ-10
  (c.6865177667)" (:214–215).
- **Finding 3.** The source sentence for the Issue assignments is added (:149–150). The quoted
  PR-body lines match those I read for #1231 and #1232.
- **Nit 1.** The ambiguous sentence is reworded (:181–183).
- **Nit 2.** `review/REVIEW-r1.md` and `review/CONFIRM-r2.md` are named at :111–112 and :121.
- **Nit 3.** `NOTES-STATUS.md`:5–6 reads "At drafting, nothing was committed, pushed or posted…".
- **Open owner question.** The question whether to correct `NEW-RESULTS.md`:322–323 is recorded as
  open owner point 6, with the copied sentence at :290–292 noted alongside it.

The register of the added `STATUS.md` text is neutral. The only "currently" is the verbatim
quotation at :83, and no barred path string or session-storage word appears in `STATUS.md`,
`NOTES-STATUS.md` or `RESPONSE-STATUS.md`.

## 2. The split-frame variant (`NOTES-STATUS.md`, Finding 1, item 5)

The variant is correct.

1. **The frame.** Split tetrahedral point 1 into points 1 and 5, each with probability p₁/2. Then
   L′ = S∘L, where S: ℝ⁴ → ℝ⁵ is (p₁/2, p₂, p₃, p₄, p₁/2).
2. **Non-spanning.** The image lies in {x₁ = x₅} and spans that 4-dimensional subspace, so L′ is
   non-spanning in the record's sense (§0.3, Span(L(states)) = ℝ^{Ω_enc}). Every point carries
   positive probability for some state.
3. **The merge map.** Let C: ℝ⁵ → ℝ⁴ merge points 1 and 5. Then C∘S = I₄.
4. **The key identity.** For any representative T′ with L′∘E = T′∘L′:
   C T′ S L = C T′ L′ = C L′ E = C S L E = L E.
   So C T′ S is a representative on the spanning tetrahedral frame, and it equals the unique F.
5. **Conclusion.** C and S are entrywise nonnegative. A nonnegative T′ would therefore make F
   nonnegative, but F has the entry −1/2 for the Hadamard. So no representative is nonnegative, and
   the test separates on this non-spanning frame.

The direct form is also right:

- Since T′S = SF on ℝ⁴, column 2 of T′ is S F e₂, whose second entry is F₂₂.
- For σ = (1, −1, −1), Hσ = (−1, 1, 1), so σ·Hσ = 2σ₁σ₃ − 1 = −3 and F₂₂ = 1/4 − 3/4 = −1/2.
- This uses the probe's point order, in which point 2 is σ = (1, −1, −1) (see nit 2).

The zero-point argument in items 1–4 matches mine:

- Columns 1–4 are fixed to F with a zero fifth row.
- The entry at σ_j = (1,1,1), σ_k = (−1,1,−1) is −1/2.
- Column 5 is free, so on that frame the test agrees with the spanning test for every E.

## 3. The sympy run

The labelling is adequate:

- The notes call the run "outside this task's paper-only scope and not relied on".
- They name the hand check as the support.
- They state that the script is a working file and is not landed.
- They state that it encodes no OI rule.

Nothing rests on it. `STATUS.md` does not mention a script or any computed value. Its scope paragraph
states only the zero-point counterexample, and items 1–4 of the notes derive that by hand.
`RESPONSE-STATUS.md`:7 cites the hand check, not the run.

## 4. Nothing else changed

- `f17020af` adds only `review/CONFIRM-STATUS.md`, byte-identical to my CONFIRM-STATUS.
- `4cb2618d` changes only `STATUS.md` and `review/NOTES-STATUS.md`, and adds
  `review/RESPONSE-STATUS.md`.
- `d015131d..4cb2618d` touches only these four paths. `NEW-RESULTS.md`, `DEPENDENCIES.md`,
  `PROVENANCE.md`, `CHANGES.md`, `review/REVIEW-r1.md`, `review/RESPONSE-r1.md` and
  `review/CONFIRM-r2.md` are unchanged.

## Nits (optional)

1. **Missing file names.** `review/RESPONSE-STATUS.md`:3 and :12, and `NOTES-STATUS.md`'s r2
   paragraph, name "`STATUS-r2.md`" and "`NOTES-STATUS-r2.md`". No such files exist in the tree; they
   were the working copies, committed as `STATUS.md` and `review/NOTES-STATUS.md`. Say so, or use the
   committed names.
2. **Point labelling in item 5.** The direct form, "the entry −1/2 directly (row 2, column 2)",
   depends on which tetrahedral point is labelled 2. State it: "point 2 being σ = (1, −1, −1), so
   F₂₂ = −1/2".
3. **Disclosure on the PR.** The out-of-scope sympy run is disclosed in the drafting log. If that log
   does not land (§A.28), the disclosure would be lost from the repository. It could also be recorded
   in the PR's checkpoint description, as the drafts did for their excluded runs.
