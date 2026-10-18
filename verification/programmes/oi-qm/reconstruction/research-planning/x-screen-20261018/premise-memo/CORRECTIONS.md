# Corrections to the minimal-premise memo

This change note maps each finding of the independent review to the edits in `PREMISE-MEMO.md`.

**Provenance.**
- The original memo is PR #864 comment 6254405090, kept byte-identical here as `PREMISE-MEMO.original.md` (sha256
  `78057ac60820fb4f776bda4fb3293d7969e403777c7e76bc522b3d8865f7849e`).
- The review is PR #864 comment 6254408285.
- `dc_premise.py` and `dc.out` are byte-identical to the originals. The script reads no file, so the memo's text is
  not an input to it. A replay under `python3 -I -B` gives rc 0, 27 PASS and 0 FAIL, byte-identical to `dc.out`.

**Scope.** This is a correction only. It adds no probe, premise, result or status change, and it adopts nothing.
The arguments and checks it cites from the review are tagged [W, rev] and [EC, rev] and are not replayed. The
corrected memo awaits independent review.

**Line references.** "o" gives lines in `PREMISE-MEMO.original.md` and "c" gives lines in `PREMISE-MEMO.md`.

| finding | lines changed | what changed |
|---|---|---|
| 1 (blocker): UPD's class | o94 → c96; o97–100 → c99–106; o123–124 → c129–130; o131 → c137; o134 → c140; o142–148 → c148–175; o312 → c347 (G2 cell); o333–334 → c368–369; o336–339 → c371–382; o360 → c408–409; o396–397 → c446–452 | Class (iii) now also covers F2 G2's transfer-clause form (F2 §2.2 Fact A, §2.3 G2, §2.4 LO and DT). UPD moves from (i) to (iii): its state side is preservation by one operation, and its test side is closure of the product tests under pullback through CN. Under continuous local rotations, UPD applied to "local unitary → CN → native readout" is equivalent to K ⊆ Q3. The memo cites the Schmidt-form argument and the witness: on the K(Z_F) defects, V = √2·Cᵀ gives eigenvalue −½, and the mutation V = I gives none. It also states what UPD does contain: it is not vacuous, it excludes Γ(Q3), K_Γ and maxCone, and on native operations alone it does not imply K ⊆ Q3. OVr, whose basis was UPD's, is unresolved. SP⊕UPD becomes (iii) by the composite rule. The statement that no D3 check fires is withdrawn. U3 is restated as the open items the classification leaves. §6's criteria drop "no PSD import"; each item states its class and its PSD use instead. §6(b) states that UPD's link is a compatibility clause |
| 2: parity control | o145–148 → removed within c148–175; o371–372 → c421; o421 → removed (U20 "the hmax parity") | The `hmax` parity control is removed: as a class decider, and as a frozen or recommended criterion in the next preregistration target. Item 1 there now asks for a disguise criterion frozen in advance with no built-in outcome, which decides U3. The hmax analogy stays as a description, with the reason it does not fix the class |
| 3: native-operation restriction | o123 → c129 (protocol class stated); c157–170; o176 → c203 (new §3.2 row); o186 → c213; o202–203 → c229–230; o253 → c286; o270–271 → c303–306; o312 → c347 (G5 cell); o336–339 → c375–377; o341–342 → c384–385; o382 → c431–432; c449–450 (U3) | The restriction is disclosed at every place where UPD's non-discrimination of K(Z_F), or its separation from K ⊆ Q3, is stated. Either the restriction is a knob (G7), or UPD collapses to K ⊆ Q3. "The only route" to excluding K(Z_F) is narrowed to native protocols |
| 4: G7 for UPD | o312 → c347 (G7 cell); o318 → c353 (G7 cell, the same correction for SP⊕UPD) | "PASS: no knob" becomes "not a pass": either the restriction to native protocols is a knob, or, lifted, UPD collapses to K ⊆ Q3 |
| 5: PSD assumptions | o229–230 → c256–261; o123 → c129; c152–153; c373–374 | The UPD, OVr and OVc rows are identified as evaluating PSD of compressions of competing-cone elements, read as token states only through the coherent update (U2). The blanket "no entry uses PSD" is narrowed to the remaining rows |
| 6: SP⊕UPD conditional | o131 → c137; o261 → c294; o318 → c353 (G5 cell); o343–345 → c386–393; o369 → c418–419 | SP⊕UPD is stated as conditional on U3 resolving in UPD's favour, on U7 for L and on U6 for SP's exclusion of K(Z_F). "No membership or preservation clause" becomes "without a membership clause". The next target is marked conditional on U3 |
| 7a: dual pair | o339 → c381–382 | "MI is the state-side dual of UPD" becomes "the exact dual pair is MI (G ⊆ K) and OVr (G ⊆ K\*)" |
| 7b: citation | o327 → c362 | `NonnegBounded` is cited at FrozenSourcing.lean:65; `obsTheory_nonnegBounded` is at :84 |
| 7c: necessity | o364 → c413 | "What is necessary on the examined clause class" becomes "every examined Γ-breaker carries" |
| — (citation tag) | o28 → c29–30 | A tag is added for arguments and checks cited from the review, [W, rev] and [EC, rev] |
