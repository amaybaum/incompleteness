# Working notes: STATUS.md for PR #1274

Writer pass under #1169 c.6865177667 OQ-1 (`amaybaum`, 2026-11-13T21:19:31Z): prepare a `STATUS.md`
for #1274 only; reviewed files unchanged; no merge. Scope kept narrow per #1274 c.6863419164.
At drafting, nothing was committed, pushed or posted, and no file other than `STATUS.md` and this
note was written.

## Sources read

- Package at `research/optc-1230-1232-20261113` = `d015131d6aad4ab09f80a7a78eb123384430186d` (read-only
  checkout): NEW-RESULTS.md, DEPENDENCIES.md, PROVENANCE.md, CHANGES.md, review/REVIEW-r1.md,
  review/RESPONSE-r1.md, review/CONFIRM-r2.md.
- Integration assessment, branch `research/integration-assess-20261113` fetched by name without
  `--depth`, read with `git show` at `c7ce4f2852cb90883b7a7c8ed645ba09db19f7ca`:
  INTEGRATION-ASSESS-r2.md (§0 item 1, §1, §2.2 #1274, §3 #1274, §4 step 1, §6 Basis, §7 OQ-1/OQ-9/OQ-10),
  REVIEW-r1.md (F6, F7, F8, F9, F11), CONFIRM-r2.md (incl. optional note A).
  The branch head moved during the pass to `d82dd02d` (adds NOTE-OQ10.md only; `c7ce4f28` is its
  parent). NOTE-OQ10.md skimmed: consistent with the basis wording used (practice, not literal
  item 2; ruling open).
- ChatGPT review 5895564670 via REST: user `amaybaum`, submitted 2026-11-13T17:44:35Z, commit
  `d015131d6aad…`, state COMMENTED. Integration requirements 1–3 copied byte-for-byte into STATUS.md
  (markup kept).
- OA-1 precedent: `origin/main:verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`.
- Owner comments via REST (author, created_at): #1169 c.6854728636 (amaybaum, 13:45:13Z);
  c.6855167580 (14:02:39Z); c.6863414487 (19:58:05Z); c.6865177667 (21:19:31Z); #1274 c.6863419164
  (19:58:18Z); #1265 c.6846206075 (06:44:20Z). All 2026-11-13.
- #1169 comments after 14:03Z grepped for #1230/#1232/step 5/#1274: no record replaces the
  2026-11-11 draft approvals. #1230, #1232, #1271 PR comments: none after their r2/r3 checkpoints.

## Measurements (2026-11-13)

- `git ls-remote`: main `c3b5f37a`; optc `d015131d`; rec-1 `3a3aa146`; intervene `ea12fde1`; substate
  `86a413c8`; reconcile `703ae20e`; bell-scope `e1534b08`; approx r4a `e41cf613`.
- PRs #1274, #1230, #1232, #1271, #1221, #1231, #1268: all open drafts (REST).
- `REC-1-r7.md` blob `f1ffac0e…` at `9f7d2612`, `cd38655c`, `3a3aa146`.
- Package blobs at `d015131d` and SHA-256 of each file: as tabled in STATUS.md (git ls-tree; sha256sum
  of `git show`).
- Last change to the four record files: `4b40dcdc`. Review files committed at `3f56d543` (REVIEW-r1),
  `4b40dcdc` (RESPONSE-r1), `d015131d` (CONFIRM-r2).
- `git merge-tree --write-tree origin/main d015131d`: exit 0. Check runs at `d015131d`: 26 success,
  1 skipped. (Not stated in STATUS.md: merge-time checks belong to the final head.)
- `tools/claims_check.py --root <status dir>`: OK; `tools/staleness_check.py`: OK.
- Forbidden-string grep of STATUS.md (path prefixes, session-storage word, "now", "no longer",
  "still", "currently"): one hit, "currently", inside a verbatim quotation of NEW-RESULTS.md:11–15.

## Decisions

- Heading "What the record supports, and at what strength" (assessment REVIEW-r1 F7).
- Superseded lines (F8): DEPENDENCIES.md:31 (row H head `cd38655c` "at this writing") and
  PROVENANCE.md:17 (same head "at writing"). PROVENANCE.md:17 carries the same time-indexed fact as
  row H; the assessment names row H only. Not listed: PROVENANCE.md:100 (F8: accurate), the
  "(open, draft)" states (measured: true), PROVENANCE.md:13 (heads measured: equal).
- Own-branch commits (F11) plus `d015131d`, which this note and review 5895564670 cite.
- Optional nit DEPENDENCIES.md:18 not applied (assessment §3, F9 reason).
- Basis stated as owner practice, ruling open (OQ-10); "not established" grounded in the record's
  own label rather than asserting the item-1 question (CONFIRM-r2 note A).
- §A.46 item 4 categories: "independently verified: none; known-invalid: none known"; whether
  model-written hand checks count as "partially verified" left to OQ-10, not decided.
- Accountable Issues: A1, D2, D3 → #1169; E2 → #868 (#1231 is the Bell-scope unit under #868;
  DEPENDENCIES row E2 ties it to the Bell ladder #868). Assessment wrote "under #868/#1169".
- REVIEW-r1 counts not restated: its summary says "Ten should-fix items" but its headings list
  findings 2–12 (eleven). STATUS.md says "findings 1–12, finding 1 blocking, and nits 1–13".

## Open points for the caller

1. c.6865177667 OQ-2/OQ-3 names #1231 and #1232 L3, not #1232 L2; gap D3 needs L2 (and class (a)3).
2. E2's accountable Issue (#868) differs from the assessment's "#868/#1169"; confirm.
3. PROVENANCE.md:17 listed beside row H as superseded; the assessment's step 1 names row H only.
4. The REC-1 head (row H) is re-measured at landing; STATUS.md records `3a3aa146`.
5. The package REVIEW-r1 should-fix count inconsistency (ten vs eleven) is in a reviewed
   file and is left unchanged.

## r2: response to the focused check (review/CONFIRM-STATUS.md)

Object: `research/optc-1230-1232-20261113` fetched by name at `f17020af` (adds
`review/CONFIRM-STATUS.md`; parent `f4c300bc` adds `STATUS.md` and `review/NOTES-STATUS.md`). The
committed `STATUS.md` and `review/NOTES-STATUS.md` at `f4c300bc` are byte-identical to the drafts of
r1. The working-area copy of CONFIRM-STATUS.md is byte-identical to the committed file. Only
`STATUS-r2.md`, this note and `RESPONSE-STATUS.md` were written; nothing was committed, pushed or
posted in this pass.

### Finding 1 checked independently before any change

Definitions used (`NEW-RESULTS.md` §0.3, copied from I:123, I:143): spanning is
`Span(L(encoded states)) = ℝ^{Ω_enc}`; a frame matrix of E is any T with `L∘E = T∘L`; without
spanning the test is "E has a nonnegative frame representative" (S:290, the existential reading of
R3:44).

1. Non-spanning. With L(ρ)(5) = 0 for every ρ, every vector of L(states) has fifth coordinate 0, so
   the span lies in {x₅ = 0} and is not ℝ⁵. The image spans that 4-dimensional subspace, because the
   tetrahedral images span ℝ⁴ (`NEW-RESULTS.md`:312–313). Non-spanning in the record's sense: yes.
   Nothing in §0.3 or I:123/I:143 requires every point of Ω_enc to have positive probability.
2. Representatives. T is fixed on the span, so its first four columns are fixed: rows 1–4 are the
   tetrahedral frame matrix F of E, row 5 is 0; column 5 is free.
3. The entry. F_kj = 1/4 + r_k·(R r_j) (`NEW-RESULTS.md`:312–313), r = σ/2, σ of even sign product.
   R(x,y,z) = (z,−y,x). σ_j = (1,1,1) gives Rσ_j = (1,−1,1); σ_k = (−1,1,−1) (sign product +1) gives
   σ_k·Rσ_j = −3, so F_kj = 1/4 − 3/4 = −1/2. This is also the X5 value the reconciliation records
   for the Hadamard on a spanning frame (R3:44, "Hadamard minimum −1/2").
4. Separation. Every representative of the Hadamard has the −1/2 entry; the identity has the
   nonnegative representative I₅. On this frame the test agrees with the tetrahedral (spanning) test
   for every E, since column 5 can always be chosen as a probability vector.
5. The zero-probability point is not essential. Split tetrahedral point 1 into two points of
   probability p₁/2 each. The frame is non-spanning (x₁ = x₅ on the image) and every point has
   positive probability for some state. With C (merge 1 and 5) and S (split 1 in half), both
   nonnegative, C∘T∘S is a representative on the spanning tetrahedral frame, hence equals F; so no
   representative T is nonnegative. Every representative also has the entry −1/2 directly (row 2,
   column 2).

Exact check, outside this task's paper-only scope and not relied on (the hand check above is the
support; the script is a working file, not landed) (my own script, sympy rationals, no OI rule encoded): ranks of the image 4/4
(tetrahedral), 4/5 (zero point), 4/5 (split), 4/6 (octahedral); the tetrahedral Hadamard frame
matrix is unique with minimum −1/2; for the zero-point frame the general solution has columns 1–4
fixed as above and column 5 free; for the split frame C·T·S − F = 0 identically. Control: on the
octahedral frame the general solution contains the permutation matrix of S2c (setting the free
parameters), reproducing the record's witness.

Verdict: finding 1 is correct. The counterexample is valid against `NEW-RESULTS.md`:322–323 as
written ("separates only on spanning frames"; "on non-spanning frames … does not separate"). The
supported statement is "need not separate" (octahedral, Husimi). `STATUS.md` row 3.1 and the claim
sentence repeated the universal form. The copied draft sentence at `NEW-RESULTS.md`:290–292 ("without
spanning … does not separate") is true on its "need not" reading only. `NEW-RESULTS.md`:97–99
("Without spanning the frame matrix of a map is not unique") holds for every non-spanning L.

### Dispositions

- Finding 1: applied with the reviewer's text (row 3.1, claim sentence, scope paragraph, the
  "known to be invalid" sentence). The extra no-zero-point variant (item 5) is kept here, not in
  `STATUS.md`.
- Finding 2: applied with the reviewer's text.
- Finding 3: applied with the reviewer's text; PR-body lines re-read through the REST API (#1231
  "Accountable Issue: #868."; #1232 "Accountable Issue: #1169.").
- Nit 1: applied with the reviewer's text.
- Nit 2: applied at both places.
- Nit 3: applied at line 5 of this note ("At drafting, …"). Whether a drafting log lands on `main`
  is left to the landing step (§A.28).

### Open owner points added

6. Whether to correct `NEW-RESULTS.md`:322–323 (and, on its universal reading, the copied draft
   sentence at :290–292) is an owner question: OQ-1 keeps the reviewed files unchanged.

## r3: response to the check of the :322–323 correction (review CONFIRM-CORR322, REVISE)

Object: `research/optc-1230-1232-20261113` at `040d929e` (fast-forward pull; HEAD unchanged). Owner
exception: #1274 c.6865575359 (`amaybaum`, 2026-11-13T21:39:25Z), "Correct it forward
(Recommended)", for :322–323 with a CHANGES Δ row and STATUS alignment only. The edits below are
left uncommitted.

### Hand check before editing (no script run)

1. Rotation counterexample on the spanning tetrahedral frame. C(x,y,z) = (y,z,x) is a cyclic
   coordinate permutation with determinant +1, so it is the Bloch action of a unitary. On the
   even-sign vectors it fixes (1,1,1) and cycles (1,−1,−1) → (−1,−1,1) → (−1,1,−1) → (1,−1,−1).
   With r = σ/2, r_k·r_m is 3/4 for equal points and −1/4 for distinct ones (two signs differ), so
   F_kj = 1/4 + r_k·(C r_j) is 1 when r_k = C r_j and 0 otherwise: a permutation matrix, unique by
   spanning. C sends the diagonal state with Bloch vector (0,0,1) to (0,1,0), which is not diagonal.
   So on a spanning frame a non-diagonal-preserving unitary passes the test, and "the E_f verdict
   separates on spanning frames" is false in the sense G1 uses. Verdict: the counterexample is valid.
2. What T3 gives. I:143: the frame matrix is "unique by injectivity and spanning", and an induced
   map lies in the class. It gives no exclusion. Exclusion on a spanning frame is shown in the record
   only for S2b (minimum entry −2/5 for the rotation about z with cos 3/5, `NEW-RESULTS.md`:309–316).
3. Octahedral versus Husimi. Octahedral, p_{±e_i}(r) = (1 ± r_i)/6: a row of a representative for
   the point m = ±e_a, written as entries α_i ± β_i on ±e_i, gives Σ_i α_i/3 + Σ_i β_i r_i/3, which
   must equal (1 + (Rᵀm)·r)/6. So Σ_i α_i = 1/2 and β_i = ±R_ai/2. Nonnegativity needs
   α_i ≥ |β_i|, hence Σ_i |R_ai| ≤ 1; for a unit row this forces a single nonzero entry ±1. Only
   signed-permutation rotations pass: the octahedral frame excludes every other rotation, and admits
   the Hadamard (S2c). Husimi: every unitary acts by the point map n ↦ Rn (S2), a measurable
   bijection, so every unitary has a nonnegative representative. Hence "on the Husimi frame every
   unitary does" is correct, and it does not hold for the octahedral frame.

### Edits (reviewer's text)

- `NEW-RESULTS.md`, "What it adds" of §3.1: the reviewer's sentence replaces the corrected one; the
  paragraph is re-wrapped to the file's width (no other words change).
- `CHANGES.md`: Δ30's new-text cell matches; the header's second sentence takes the reviewer's
  clause on Δ30; the header paragraph is re-wrapped.
- `STATUS.md`: row 3.1 and the claim sentence take the reviewer's text; the verification-status
  paragraph is re-wrapped.

### Open points for the owner

- The optional scope line for the copied sentences at `NEW-RESULTS.md`:275–276 and :290–292 (the
  rotation (x,y,z) ↦ (y,z,x) on the tetrahedral frame; a Hadamard-invariant tetrahedron) is not
  added. It states a fact the record does not carry.
- Δ30's reason cell describes only the non-spanning clause; the narrowing of the spanning clause is
  recorded in its new-text cell and in the header clause.
- The claim sentence reads "the nonnegative-frame test has a unique frame matrix under spanning",
  as the reviewer gives it; its subject is the test, not the map.
