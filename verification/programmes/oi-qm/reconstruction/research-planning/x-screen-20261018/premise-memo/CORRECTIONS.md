# Corrections to the minimal-premise memo

This change note maps each finding of the three independent reviews to the edits in `PREMISE-MEMO.md`: the first
pass answers the review of the original memo, the second pass answers the review of the first-pass correction, and the
third pass answers the review of the second-pass correction. The last section records evidence corrections, which
answer no review finding.

**Provenance.**
- The original memo is PR #864 comment 6254405090, kept byte-identical here as `PREMISE-MEMO.original.md` (sha256
  `78057ac60820fb4f776bda4fb3293d7969e403777c7e76bc522b3d8865f7849e`).
- The review of the original memo is PR #864 comment 6254408285. The review of the first-pass correction (commit
  `11562acebd30d3ae61a099f3484631c3f7dd8fc5`) is PR #864 comment 6254747204. The review of the second-pass correction
  (commit `6df43b2c08907c9572408c6ef627da5ec9071e81`) is PR #864 comment 6254962113. The three reviews are kept
  verbatim in `reviews/`, with their digests and provenance in `reviews/PROVENANCE.md`.
- On 2026-10-19 the owner authorized factual and evidence corrections to this memo and this record, and only those;
  no premise is adopted and no class or status changes under the authorization. The third pass applies it to correct
  the equivalence the MEV row stated between MEV and OV-LU (finding 1 of comment 6254962113), with the low-priority
  items of the same review. The evidence corrections apply it as well.
- `dc_premise.py` and `dc.out` are byte-identical to the originals. The script reads no file, so the memo's text is
  not an input to it. A replay under `python3 -I -B` gives rc 0, 27 PASS and 0 FAIL, byte-identical to `dc.out`.

**Scope.** This is a correction only. It adds no premise, result or status change and no probe of any screen, and it
adopts nothing. The arguments it cites from the reviews are tagged [W, rev] and the reviews' exact checks [NR, rev]
(scripts not retained); none is replayed in the repository. [EC, v] marks the memo's own exact check of the witness
the reviews report. Where a pass ran its own scratch computation, its section says so; such a computation is not
committed and is not retained evidence. The three passes were reviewed independently, and the third was accepted with
nits (summarized in PR #864 comment 6257588156). The evidence corrections are not yet independently reviewed.

**Line references.** "o" gives lines in `PREMISE-MEMO.original.md`. "c" gives lines in `PREMISE-MEMO.md` at commit
`11562ace`, the first-pass correction. "n" gives lines in `PREMISE-MEMO.md` at commit `6df43b2c`, the second-pass
correction. "t" gives lines in `PREMISE-MEMO.md` after the third pass. "e" gives lines in `PREMISE-MEMO.md` after the
evidence corrections.

## First pass (review comment 6254408285)

| finding | lines changed | what changed |
|---|---|---|
| 1 (blocker): UPD's class | o94 → c96; o97–100 → c99–106; o123–124 → c129–130; o131 → c137; o134 → c140; o142–149 → c148–175; o312 → c347 (G2 cell); o333–334 → c368–369; o336–339 → c371–382; o360 → c408–409; o396–397 → c446–452 | Class (iii) now also covers F2 G2's transfer-clause form (F2 §2.2 Fact A, §2.3 G2, §2.4 LO and DT). UPD moves from (i) to (iii): its state side is preservation by one operation, and its test side is closure of the product tests under pullback through CN. Under continuous local rotations, UPD applied to "local unitary → CN → native readout" is equivalent to K ⊆ Q3. The memo cites the Schmidt-form argument and the witness: on the K(Z_F) defects, V = √2·Cᵀ gives eigenvalue −½, and the mutation V = I gives none. It also states what UPD does contain: it is not vacuous, it excludes Γ(Q3), K_Γ and maxCone, and on native operations alone it does not imply K ⊆ Q3. OVr, whose basis was UPD's, is unresolved. SP⊕UPD becomes (iii) by the composite rule. The statement that no D3 check fires is withdrawn. U3 is restated as the open items the classification leaves. §6's criteria drop "no PSD import"; each item states its class and its PSD use instead. §6(b) states that UPD's link is a compatibility clause |
| 2: parity control | o145–149 → removed within c148–175; o371–372 → c421; o421 → removed (U20 "the hmax parity") | The `hmax` parity control is removed: as a class decider, and as a frozen or recommended criterion in the next preregistration target. Item 1 there now asks for a disguise criterion frozen in advance with no built-in outcome, which decides U3. The hmax analogy stays as a description, with the reason it does not fix the class |
| 3: native-operation restriction | o123 → c129 (protocol class stated); c157–170; o176 → c203 (new §3.2 row); o186 → c213; o202–203 → c229–230; o253 → c286; o270–271 → c303–306; o312 → c347 (G5 cell); o336–339 → c375–377; o341–342 → c384–385; o382 → c431–432; c449–450 (U3) | The restriction is disclosed at every place where UPD's non-discrimination of K(Z_F), or its separation from K ⊆ Q3, is stated. Either the restriction is a knob (G7), or UPD collapses to K ⊆ Q3. "The only route" to excluding K(Z_F) is narrowed to native protocols |
| 4: G7 for UPD | o312 → c347 (G7 cell); o318 → c353 (G7 cell, the same correction for SP⊕UPD) | "PASS: no knob" becomes "not a pass": either the restriction to native protocols is a knob, or, lifted, UPD collapses to K ⊆ Q3 |
| 5: PSD assumptions | o229–230 → c256–263; o123 → c129; c152–153; c373–374 | The UPD, OVr and OVc rows are identified as evaluating PSD of compressions of competing-cone elements, read as token states only through the coherent update (U2). The blanket "no entry uses PSD" is narrowed to the remaining rows |
| 6: SP⊕UPD conditional | o131 → c137; o261 → c294; o318 → c353 (G5 cell); o343–345 → c386–393; o369 → c418–419 | SP⊕UPD is stated as conditional on U3 resolving in UPD's favour, on U7 for L and on U6 for SP's exclusion of K(Z_F). "No membership or preservation clause" becomes "without a membership clause". The next target is marked conditional on U3 |
| 7a: dual pair | o339 → c381–382 | "MI is the state-side dual of UPD" becomes "the exact dual pair is MI (G ⊆ K) and OVr (G ⊆ K\*)" |
| 7b: citation | o327–328 → c362–363 | `NonnegBounded` is cited at FrozenSourcing.lean:65; `obsTheory_nonnegBounded` is at :84 |
| 7c: necessity | o364–365 → c413–414 | "What is necessary on the examined clause class" becomes "every examined Γ-breaker carries" |
| — (citation tag) | o28 → c29–30 | A tag is added for arguments and checks cited from the review, [W, rev] and [EC, rev] |

## Second pass (review comment 6254747204)

The second review confirmed UPD's class (iii) on the state-side transfer-clause reading (F2 §2.1, §2.2 Fact A, §2.3
G2) and asked for the corrections below; its item numbers are given in the last column.

| fix | lines changed | what changed | reason |
|---|---|---|---|
| 1: DT basis | c100–102 → n103–106; c104–105 → n108–109; c129 → n133; c150–155 → n154–161; c347 → n363 (G2 cell); c373–374 → n391–393; c446 → n468–469 | Class (iii) covers a bare transfer clause and F2's DT, complete dual-test closure (SA:48–59); "or its dual, closure of a test family under pullback" is removed, and closure of a smaller family is stated not to be F2's DT (SA:57–59). "Both readings above have that form" is removed: UPD is (iii) on its state-side reading only, and the test-side reading is described as DT-type closure restricted to product tests, not F2's DT. MI+ D3 is removed as a G2 ground; the PSD use and the equivalence to K ⊆ Q3 under local rotations are stated not to be G2 grounds (Fact A) | item 1: the widened definition went beyond F2's DT and would also have placed OVc, OVn and MEV in (iii); Fact A does not make equivalence to K ⊆ Q3 a G2 ground |
| 2: PSD list | c258–263 → n267–279 | MEV is added, with its negative rank-one compression Tr(P_m z) = −½. A check of every row of §4 found two further entries of the same kind: OVn, whose recorded exclusion CN Γ(B) CN ∉ maxCone is the product-test evaluation after the coupling that OVc uses, and SP⊕UPD, which inherits UPD's. The CPK row, which records exclusion only by importing PSD, is named. With these, the sentence "Apart from these rows, no entry uses PSD or CP of a competing cone's elements" holds and is kept | item 2: the sentence was false for MEV |
| 3: criterion | c368–369 → n384–387; c373–374 → n391–393; c385 → n404–406; c387 → n408 | "No PSD import" is restored as a §6 criterion, worded as in the original memo (o333). UPD, OVr, OVc and MEV are stated not to meet it, and OVn's exclusions are stated to be of the same kind. Each §6 item states whether it meets the criterion: UPD, OVr and OVc (item 1), MEV (item 2) and SP⊕UPD (item 3) do not; CH's exclusions use no PSD evaluation | item 3: dropping the criterion was outside the authorized scope (§A.29) |
| 4: witness convention | c163–164 → n169–173; c203 → n212 | The convention is stated: \|ij⟩ = \|i⟩⊗\|j⟩ with token 1 first, m = (\|00⟩ + b\|01⟩ − bd\|10⟩ + d\|11⟩)/2 as in `dc_premise.py`, C_ij = ⟨ji\|m⟩, V = √2·Cᵀ, conjugation z ↦ (I⊗V) z (I⊗V)†. Under it the outcome-0 conditional has eigenvalue −½ for all four defects. The review's observation is recorded: with C_ij = ⟨ij\|m⟩ the same formula puts −½ at outcome 0 only for the d = −1 defects, and UPD excludes all four either way. The §3.2 row points to the convention. That the stated convention puts −½ at outcome 0 for all four defects was checked in exact arithmetic during this pass by a scratch computation that is not committed and is not retained evidence; the review's witness check is the cited source | item 4: the convention was not fixed, and "outcome 0" depends on it |
| 5: evidence tag | c286 → n302 | "UPD ≡ K ⊆ Q3" is tagged [W, rev]; [EC, rev] stays on the witness only | item 5 |
| 6: stale sentence | c399 → n420–421 | "through validity of the update or test, not through membership" becomes "by a route that is neither membership nor a transfer clause (F2 G2), for example test validity", with the statement that update validity in UPD's form is a transfer clause under the present F2 rules | item 6: the old wording required the form now classed (iii) |
| 7: OVr caveat | c287 → n303 | The OVr K(Z_F) cell is restricted to native protocols, and states that with local unitaries admitted before the coupling OVr also reduces to K ⊆ Q3 [W, rev] | item 7 |
| 8: self-description and §A.42 | c4–6 → n4–7; c8 → n9–10; c17 → n19–20; c35 → n38; c40–41 → n43–44 | "It makes no commit, push, probe or repository edit" becomes a description of the memo as a research record in this directory that runs no probe and edits no other repository file. The base worktree, the `s1018/…` search files and `run1-wrong-expected/` are stated not to be retained in the repository. The script is cited as the committed `dc_premise.py` | item 8: c4 was stale; the references point outside the repository |
| — (tag scope) | c29–30 → n32–33 | The [W, rev] and [EC, rev] tags cover both reviews, since fixes 4 and 7 cite the second | consequence of fixes 4 and 7 |
| 9: line ranges | this file, first-pass table | Finding 1: o142–148 becomes o142–149. Finding 5: c256–261 becomes c256–263. Finding 7b: o327 → c362 becomes o327–328 → c362–363. Finding 7c: o364 → c413 becomes o364–365 → c413–414. The same re-wrapped end line is corrected in finding 2's range, o145–148 → o145–149. The review lists c256–263 twice; the first-pass table carries that range once | item 9: the ranges omitted re-wrapped end lines |

**Consistency of the judgment calls the review accepted.** After fix 1, class (iii) rests on the state-side form
"named operations preserve physical states" and on complete dual-test closure.
- OVc, OVn and MEV are test-validity clauses over restricted families: product tests after the coupling, product tests
  after native protocols, and maximally entangled projectors. None is complete dual-test closure. The state-side forms
  of OVc and OVn conclude membership in maxCone, the fixed product-test window; MEV's concludes membership in the dual
  of the maximally entangled projectors, also a fixed cone. None concludes membership in the physical state space.
  Leaving them unreclassified, with their reading against the transfer-clause form open under U3, is consistent with
  the narrowed definition.
- OVr's state-side reading is UPD's restricted to outcome 0. Marking it unresolved under U3, rather than (iii), asserts
  no class that conflicts with fix 1.

**Checks for the second pass.** `PREMISE-MEMO.original.md`, `dc_premise.py` and `dc.out` are byte-identical to
commit `11562ace`. The replay under `python3 -I -B` gives rc 0, 27 PASS and 0 FAIL, byte-identical to `dc.out`. No
probe was added and no file other than `PREMISE-MEMO.md` and this record changed.

## Third pass (review comment 6254962113)

The review accepted the second pass with notes. Its finding 1, present since the original memo (o127), needed owner
authorization; the owner authorized its correction together with the low-priority items, with no class or status
change. Item numbers of the review are given in the last column.

| fix | lines changed | what changed | reason |
|---|---|---|---|
| 1: MEV and OV-LU | n137 → t137; new §3.4 row at t244; n244–246 → t246–249; n366 → t369 (G1 cell); n402–406 → t405–410; this file, consistency paragraph (second-pass :56–60) | The MEV row states MEV's own content: Tr(P_ψX) ≥ 0 for every physical X and every maximally entangled ψ. Its operational form is the fixed product test \|+⟩⟨+\|⊗P_0 after every local unitary and the coupling (B = CN(\|+⟩⟨+\|⊗P_0)CN [EC, dc]; every maximally entangled vector is a local-unitary image of (\|00⟩ + \|11⟩)/√2 [W]). OV-LU, validity of every product test after a local unitary and the coupling, implies MEV; MEV implies neither OV-LU nor OVc, by X_c: Tr(P_v X_c) = ½ − 53/100 < 0 with P_v = CN(e_v⊗P_0)CN [EC, dc]. §3.4 gains the row "OV-LU ⇒ MEV; MEV ⇏ OVc, hence MEV ⇏ OV-LU", with the step OV-LU ⇒ OVc (identity unitary) stated, and the X_c note states that X_c fails OVc. The G1 cell keeps BORDERLINE and drops "unless stated as OV-LU", since OV-LU is a different, stronger premise; it names MEV's operational form instead. §6 item 2 states MEV as validity of the maximally entangled projectors, with its operational form and the two non-implications. In this file, MEV's state-side form concludes membership in the dual of the maximally entangled projectors, not in maxCone. MEV keeps class (i) and every cell of its §4 and §5 rows other than G1's wording | finding 1: X_c is ME-valid and fails a product test after the coupling, so the stated equivalence was false; with OVc ⇒ UPD and the collapse under local rotations it would also have made MEV imply K ⊆ Q3, against the row's own entry |
| 2: tags | n168–173 → t168–174; n363 → t366 (G5 cell); n33 → t33 | The witness's PSD claims keep [EC, rev]. The convention-specific claim (−½ at outcome 0 for all four defects with C_ij = ⟨ji\|m⟩) cites comment 6254962113, and the d = −1 observation cites comments 6254747204 and 6254962113. The G5 cell's combined "[W + EC, rev]" is split: the witness is [EC, rev] and UPD ≡ K ⊆ Q3 is [W, rev]. The tag definition lists the third review | item 2 |
| 3: D3 wording | n103–106 → t103–106; n133 → t133 | Class (iii)'s D3 entry reads "a premise that posits PSD or CP on K by definition (D3, as in row CPK)". The UPD row says UPD evaluates PSD of compressions but posits no PSD or CP on K, which is the case the D3 entry covers, in place of "MI+ D3 is not among them" | item 3: the two sentences read as conflicting |
| 4: PSD definition | n267–268 → t270–271 | The rows "evaluate positivity on competing-cone elements in an order other than the competing cone's own: PSD-type compressions to planes or vectors that are not product" | item 4: read literally, the old wording also covered PC's maxCone exclusion, which uses maxCone's own order |
| 5: F2 classes in §6 | n402 → t405; n408 → t412–413 | Item 2 states that CH and MEV are class (i); item 3 states that SP⊕UPD is class (iii) by the composite rule. Both classes are those of §2 | item 5: §6 says each item states its F2 class |
| 6: cosmetic | n109–110 → t109–110; this file, second-pass rows 4 and 6; this file :14–16 | The class paragraph is re-wrapped. Fix 4's range becomes c163–164 → n169–173, and fix 6's becomes c399 → n420–421. The scope paragraph states that review checks are not replayed in the repository and that a pass's own scratch computation is disclosed in its section and not retained | item 6 |

**Checks for the third pass.** `PREMISE-MEMO.original.md`, `dc_premise.py` and `dc.out` are byte-identical to
commit `6df43b2c`. The counterexample was checked in exact arithmetic during this pass by a scratch computation that
is not committed and is not retained evidence: X_c's product-test value after the coupling is −3/100, its minimum over
maximally entangled projectors is 15/136 and over product vectors 1/850, and the identity B = CN(|+⟩⟨+|⊗P_0)CN and
the witness convention of fix 2 were rechecked. No probe was added and no file other than `PREMISE-MEMO.md` and this
record changed.

## Evidence corrections (no review finding)

These corrections answer no review finding; the owner's authorization of 2026-10-19 covers them (provenance above).
The three reviews report their exact checks by result only. The scripts were not posted with comments 6254408285,
6254747204 and 6254962113 and are not retained, so those checks cannot be replayed from the repository. The
corrections re-tag them, keep the reviews verbatim and add an exact check of the witness written for this memo. They
change no claim, class, label or status.

| fix | lines changed | what changed |
|---|---|---|
| tag definitions | t32–33 → e31, e33–35 | [W, rev] is defined for the reviews' written arguments alone and points to `reviews/`. [NR, rev] replaces [EC, rev] for the reviews' exact checks: the result is reported, the script is not retained, and the check is not replayed. [EC, v] is defined for the witness check |
| witness check | e48–55; new files `witness_check.py`, `witness_check.out` | A new exact check of the §2 witness, not a reproduction of the reviews' checks, written from the memo's definitions and the construction in `dc_premise.py`. Its claims: W1, −½ at outcome 0 for all four defects with C_ij = ⟨ji\|m⟩; W2, −½ at outcome 0 exactly for the d = −1 defects with C_ij = ⟨ij\|m⟩; W3, UPD excludes all four either way; W4, no violation under V = I. Its controls K1–K4 include the countercontrol K4, the PSD perturbations I/2 − P_m/4 |
| witness | t168–175 → e179–186 | That the native UPD conditionals of the four defects are PSD is tagged [EC, dc] (`dc.out`: "defects: even block PSD", "defects: odd block PSD (K(Z_F) satisfies UPD)", "cond(X,0) = even(X)", "cond(X,1) = odd block"). The six 2-subset compressions carry [NR, rev] only. The convention-specific eigenvalues and the mutation V = I carry [NR, rev] for what the reviews report and [EC, v] for the witness check; "UPD excludes all four either way" carries [EC, v] |
| downstream tags | t213 → e224 (§3.2 row), t223 → e234 (§3.3 row), t305 → e316 (§4 UPD row, K(Z_F) cell), t366 → e377 (§5 UPD row, G5 cell) | The witness carries [NR, rev]; [EC, v] in place of [EC, rev]. Each [W, rev] tag, including UPD ≡ K ⊆ Q3, is unchanged |
| reviews | new directory `reviews/` | Comments 6254408285, 6254747204 and 6254962113 are kept byte-exact, with `SHA256SUMS` and `PROVENANCE.md` (id, author, timestamps, URL, digest, fetch method and time) |
| this file | :5–6 (introduction), :13–18 (provenance), :22–27 (scope), :31–32 (line references) | The introduction names this section; the provenance names `reviews/` and the owner's authorization and its scope; the scope paragraph names the three tags and the review status; "e" is defined |
| `../REPORT.md` | :7 | The first replay attempt's outputs, cited at a path outside the repository, are stated not to be retained |

**Checks for these corrections.** `PREMISE-MEMO.original.md`, `dc_premise.py` and `dc.out` are byte-identical to
commit `641ae161`. The replay under `python3 -I -B` gives rc 0, 27 PASS and 0 FAIL, byte-identical to `dc.out`.
`witness_check.py` was run twice under `python3 -I -B`: rc 0, 8 PASS and 0 FAIL, byte-identical outputs, every
control green and W1–W4 holding. No probe of any screen was added, and no file outside this directory other than
`../REPORT.md` changed.
