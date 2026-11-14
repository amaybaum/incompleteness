# Focused check of the forward correction of `NEW-RESULTS.md`:322–323 (PR #1274)

**Verdict: REVISE (one item).** The correction narrows the clause about non-spanning frames
correctly, and nothing else changed. The new sentence still overclaims in its first clause, "The
E_f verdict separates on spanning frames (T3)". That clause is false in one reading and unproved in
the other (finding 1). `STATUS.md` repeats it, in wording I proposed in CONFIRM-STATUS (finding 2).
The fix is text only and stays inside the owner's exception for :322–323 and the STATUS alignment.
Part of it states a fact the record does not yet carry, so it is offered for the owner's choice.

## Object

- **Head.** Branch `research/optc-1230-1232-20261113`, fetched by name with no `--depth` and checked
  out in a detached worktree in the working area. HEAD is exactly
  `040d929ea22e4ea470849ec5067c9d4311c79d86`, with parent `4cb2618d`.
- **Owner record.** #1274 c.6865575359 (`amaybaum`, 2026-11-13T21:39:25Z), read through the REST API.
  It authorizes "Correct it forward (Recommended)", as a narrow exception to OQ-1 for this item only.
  The edit it specifies is "a statement that the test *need not* separate without spanning, as shown
  by the octahedral and Husimi frames", together with a CHANGES.md Δ row and STATUS.md alignment.
- **Checks.** The five check scripts all report OK at the head. Nothing else was run. Every
  mathematical point below was checked by hand.

## 1. Is the new sentence correct and exactly scoped?

**Labels.** In `NEW-RESULTS.md`, S2 is the Husimi frame ("Counter-structure 2 (continuum) [X S2].
Husimi frame", :285) and S2c is the octahedral frame (:278). Both citations are correct.

**Second clause: correct, and inside the owner's wording.** "Without spanning the nonnegativity test
need not separate, as on the octahedral and Husimi frames" holds in the sense that G1 uses (S:278):
on both frames a non-diagonal-preserving unitary has a nonnegative frame representative. It no
longer states non-separation for every non-spanning frame, so the zero-point counterexample no
longer applies.

**First clause: overclaims.** The record uses "separates" in two senses, and the clause fails in
both.

- **Strong sense** (the test admits exactly the diagonal-preserving unitaries; G1, S:278 and the
  copied :290–291). Here the clause is false, already for the record's own spanning tetrahedral frame
  (r_k = σ_k/2, σ_k of even sign product; :309–313).
  - The rotation C(x,y,z) = (y,z,x), a proper rotation and so a unitary's Bloch action, permutes
    the four points: (1,1,1) is fixed and the other three are cycled.
  - So F_kj = 1/4 + r_k·C r_j is 1 when r_k = C r_j and 1/4 − 1/4 = 0 otherwise. The frame matrix
    is a permutation matrix.
  - C sends the diagonal state with Bloch vector (0,0,1) to (0,1,0), so its conjugation does not
    preserve diagonals.
  - On this spanning frame, then, a non-diagonal-preserving unitary passes the test, exactly as the
    Hadamard does on the octahedral frame.
- **Weak sense** (the test excludes some unitary; I:147's "the target is at positive distance").
  - T3 does not give this. T3 gives uniqueness of the frame matrix and inclusion of induced maps in
    the class, not exclusion.
  - The target need not be excluded on every spanning frame. The Hadamard's Bloch action is the
    π-rotation about (1,0,1)/√2. A regular tetrahedron rotated so that one of its 2-fold axes lies
    along (1,0,1)/√2 is invariant under that rotation. On the spanning frame it defines, the
    Hadamard's frame matrix is a permutation.
  - That every spanning frame excludes some unitary is true. Otherwise every frame matrix of a
    unitary, and that of its inverse, would be nonnegative, hence a permutation, and the unitaries
    form a continuous group. That argument is not in the record, however. The record shows exclusion
    only on the frames it checks: S2b, a rational rotation on the tetrahedral frame.
- **The octahedral frame in the weak sense.** It excludes every rotation outside the octahedral
  group.
  - A row of a frame representative has the form Σ_i (α_i u_i + β_i d_i). Here u_i is the indicator
    of the pair ±e_i and d_i = e_{+i} − e_{−i}.
  - Matching p(Rr) forces β_i = ±R_ai/2 and Σ_i α_i = 1/2.
  - Nonnegativity needs α_i ≥ |β_i|, hence Σ_i |R_ai| ≤ 1 for every row a. For a unit row this
    holds only for ±e_i, so R must be a signed permutation.
  - So the octahedral frame witnesses "need not separate" in the strong sense only. Only the Husimi
    frame, on which every unitary is a point map (S2), witnesses it in the weak sense.

The contrast the corrected sentence draws, spanning separates and non-spanning need not, is
therefore not what the record shows. What spanning gives (T3, §0.3) is uniqueness, so that the class
is fixed by the map. Admitting non-diagonal-preserving unitaries is frame-relative in both cases.

## 2. Δ30 and the CHANGES header

- **Δ30 is accurate as a record of the edit.** Its old and new texts match the diff. It cites the
  zero-point counterexample's sources (`review/CONFIRM-STATUS.md` finding 1;
  `review/NOTES-STATUS.md`), c.6865575359 resolves, and "no copied statement or proof changes" is
  true. Its description of the old sentence, "stated non-separation for every non-spanning frame; the
  record shows it for two frames", is right.
- **The header is true in its stated scope but no longer covers the whole table.** It says every
  change to text *copied from* the drafts is listed and that "None changes a statement's
  mathematics". Δ30 changes package text (Δ26), not copied text, so it falls outside that sentence.
  But the table now holds a row that withdraws a false mathematical statement of the package's own,
  and the header then reads as covering every row.

**Fix.** Append to the header's second sentence:

> ; Δ30 narrows a sentence written for this record (Δ26), which overstated G1, and changes no copied
> text.

## 3. STATUS.md against the new text

The scope paragraph (:134–138) and the pointer (:110–111) agree with the new sentence. They inherit
the first-clause problem, however, and so do row 3.1 (:75) and the claim sentence (:92–94). Those
read "the nonnegative-frame test is separating under T3's spanning hypothesis" and "is separating
under spanning". That wording came from my CONFIRM-STATUS finding 1, and it overclaims for the same
reason as the first clause.

## 4. Nothing else changed; other lines in NEW-RESULTS

- **The commit's changes.** It changes `NEW-RESULTS.md` at :322–323 only, adds one `CHANGES.md` row
  (Δ30), changes `STATUS.md` at :110–111 and :134–138, and adds `review/CONFIRM-STATUS-r2.md`,
  byte-identical to mine.
- **Formatting nit.** The two edited lines of `NEW-RESULTS.md`, and `STATUS.md`:110, are not
  re-wrapped: they run past the surrounding width.
- **Other lines with the same overclaim.**
  - No other package-written line in `NEW-RESULTS.md` states non-separation for every non-spanning
    frame.
  - The section heading at :263 ("frame-relative without spanning") is correct in §0.3's sense, that
    the class is not fixed by the map.
  - :290–292 is copied (S:108) and true on its "need not" reading. It carries the same implied
    contrast as the first clause.
  - :275–276 is copied (S:102): "its control X5 (a negative entry in the Hadamard's frame matrix) is a
    property of spanning frames". This is likewise not a property of every spanning frame (the
    Hadamard-invariant tetrahedron above).

  Both copied sentences fall outside the owner's exception. They can be stated in `STATUS.md` rather
  than edited.

## Findings and fixes

### 1. The first clause of :322 overclaims (blocking for this correction)

**Fix (inside the owner's exception).** Replace :322–323 up to "(S2c, S2; R3:59)." with:

> **What it adds.** On spanning frames the frame matrix is unique, so the E_f class is fixed by the
> map (T3); on the tetrahedral frame it excludes a rational rotation (S2b). Without spanning the test
> need not separate: on the octahedral and Husimi frames non-diagonal-preserving unitaries have
> nonnegative frame representatives (S2c, S2; R3:59), and on the Husimi frame every unitary does.

Update Δ30's new-text cell to match.

### 2. STATUS.md repeats the overclaim, in wording I proposed (blocking for this correction)

**Fix.**

- **Row 3.1 (:75).** Write: "G1: on route E_f, under T3's spanning hypothesis the frame matrix is
  unique and the class is fixed by the map; without spanning the test need not separate: on the
  octahedral and Husimi frames non-diagonal-preserving unitaries have nonnegative frame
  representatives, and on the Husimi frame every unitary does".
- **Claim sentence (:92–94).** Replace "is separating under spanning and need not separate without it
  (octahedral and Husimi frames)" with "has a unique frame matrix under spanning and need not
  separate without it (octahedral and Husimi frames)".
- **Scope paragraph (:134–138).** Add, for the owner to accept or decline because it states a fact
  the record does not carry:

  > Spanning does not exclude non-diagonal-preserving unitaries either. The rotation
  > (x,y,z) ↦ (y,z,x) permutes the tetrahedral points, so its frame matrix is a permutation, and on
  > a regular tetrahedron with a 2-fold axis along (1,0,1)/√2 the Hadamard's frame matrix is a
  > permutation. The copied sentences at `NEW-RESULTS.md`:275–276 and :290–292 are read at that
  > scope.

### 3. The CHANGES header (should-fix)

**Fix.** As in §2 above.

## Summary against the four questions

1. **The new sentence.** The second clause is correct and matches the owner's wording, and S2 is the
   Husimi label. The first clause overclaims (finding 1).
2. **Δ30 and the header.** Δ30 is accurate. The header is true in its own scope but should name Δ30
   (finding 3).
3. **STATUS.md.** It is consistent with the new text but inherits the overclaim (finding 2).
4. **Other changes.** Nothing else changed. No other package-written line repeats the old universal.
   Two copied sentences (:275–276, :290–292) carry the spanning contrast and are best scoped in
   `STATUS.md`.
