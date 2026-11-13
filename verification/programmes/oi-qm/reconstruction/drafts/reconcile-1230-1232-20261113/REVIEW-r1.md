# Independent review: #1230 / #1232 reconcile (RECONCILE.md)

**Reviewer.** A fresh, non-author model reviewer (Claude Code subagent), 2026-11-13. Read-only: no
commit, push, comment, edit or dispatch; no computation on any OI rule. Hand checks only. This review
is model-written and is not verification (§A.46 item 7).

**Object.** `RECONCILE.md` in this directory, sha256 `05ad46b2977055069678f7a911d87bcd59f85408e10786ebcdd57d86cf91a71f`.

**Sources were re-read first-hand, not from the reconciler's `src/` or `api/` copies.** Branches were
fetched by name: `research/intervene-1-20261111` = `ea12fde1`; `research/substate-bridge-1-20261111`
= `86a413c8`; `research/rec-1-1169-20261113` = `9f7d2612`; `research/q868h-868-20261113` = `ffc9cda4`;
`research/tune1-step3a-1236-20261113` = `8228b3c2`; `main` = `c3b5f37a`; and for cross-checks
`research/approx-unit1-r4a-1216-20261109` = `e41cf613` (#1221) and `research/bell-scope-868-20261111`
= `e1534b08` (#1231). The GitHub REST API was used for reviews 5857985732 (#1230) and 5859960068 (#1232),
PR bodies, #1169's comments since 2026-11-10, repository issue comments since 2026-11-11, and #1216
c.6793397036. The Lean anchors were read in `verification/lean-mathlib/OIBridge/` at `c3b5f37a`.

## Verdict: ACCEPT WITH CHANGES

The central conclusion is correct: neither draft supplies a Q2-F or Q2-P operation outside 𝒦, and
the boundary point (transformation-level classicality does not decide OBL-SP) is correct. Most
citations check out. Three findings need correction before this record is used:
1. T7(b) is misclassified as new (§A.19).
2. The governance search reports something false.
3. 𝔊_K is mischaracterized in the boundary paragraph.

The remaining changes are precision fixes. The full list is in §3.

## 1. What was confirmed

- **Pins and objects.** The heads, parents and the base `cac5d264` (an ancestor of `c3b5f37a`) are as
  stated. Between the pins only `OIRealization.lean` changed under OIBridge. Every Lean anchor in
  RECONCILE §0 exists at the cited line.
- **Reviews.** 5857985732 (r2, ACCEPT WITH DOCUMENTATION NITS, `ea12fde1`) and 5859960068 (r2, ACCEPT
  WITH NITS, `86a413c8`) are quoted correctly, including "OI-wide verdict remains **INDETERMINATE**"
  and "cannot be used as a positive result for TUNE-1". Both were posted under `amaybaum`.
- **Main drift.** The net shift is −2 lines after line 4. At `c3b5f37a`:
  - Main:362 carries G_φ^K and the linear-update clause, with V and S_i finite;
  - Main:724 reads "Fourteen items" (`cac5d264` read "Thirteen");
  - Main:60 carries the new cardinality sentences;
  - #1233 merged at 2026-11-11T14:09:36Z.

  The quoted text at Main:588, :600 and :718 is unchanged. Nit: the sentence "Wings separated by
  less than the graph cone … fall outside the Corollary" was already at the drafts' pin (Main:416).
  #1233 added the explicit spacelike-at-c window clause. The L2 row's quotation is therefore not new
  text from #1233, though the O2 window as stated is.
- **T5 (re-checked).** Everything was checked against the Lean source:
  - CM satisfies all five `Architecture` fields (:506–516; `ancBlock K f e = K (s,f)(t,e)`,
    AncillaClosure:457).
  - `InstAvail.op` is square with Kᴴ K = 1 (:271–272). A square CM isometry has orthonormal columns
    with one entry each in distinct rows, so it equals `permMatrix σ * diagonal d`; that is
    `IsMonomial` (SubstratumInterface:75; `monomial_entry` fixes the convention).
  - The `readout` constructor maps to substratumClass directly: a reindexed 0/1 diagonal is diagonal,
    hence monomial (`monomial_diagonal`).
  - The reverse direction is `instAvail_mono` (:305).
  - `genTheory`'s data fields (`avail`, `availExt`, `prepAvail`, `readout`) depend on 𝓘 only through
    `InstAvail` (`readout = localLuders`), and the remaining fields are proofs. So
    `genTheory CM = substratumTheory` (RouteB:284–286) follows by propext/funext and proof
    irrelevance.
  - The FI-1 witness |0⟩(⟨0|+⟨1|)/√2 is CM, and it is not monomial (row 0 has two nonzeros).

  **T5 holds.**
- **T7(b) (re-checked).** The mathematics is correct. Its classification is not (finding A below).
- **E2 item 4.** 0 ≤ M ≤ P gives (1−P)M(1−P) = 0, so M = PM = MP. Summing with the orthogonal P_a gives
  P_a Q_b = M_ab = Q_b P_a. Correct.
- **G1/S2c.** (x,y,z) ↦ (z,−y,x) is the Hadamard's Bloch action (HXH = Z, HYH = −Y), has det +1 and
  permutes the six axis points. Spanning forces |Ω_enc| ≤ d². Correct.
- **Saturation.** Under ν(r) = ∏ T(r(s)|s), the register's law given s is T(·|s) on Ω_S′×A. Correct
  under broad H5, and designed from the target.
- **L1 and L4 vs Main:362.** The cone lemma uses only the finiteness of V. Main's linear-update clause
  is L4 for finite S_i. Correct.
- **Stale SUBSTATE text** (§3.1 item 4 "ledger (x) is unscoped"; the "G_φ^K … off `main`"
  sentence). Confirmed.
- **TUNE-1 Step 1** (`TUNE-1-STEP1.md`:2069) quotes "r2 has not been re-reviewed". Confirmed.
- **OA-2.** Checked at `c3b5f37a`:
  - Lemma 0 / N0 (OA2:199–223), N1 (:225–238) and the N2.1 counterexample (:302–318: F₂², reachable
    laws with P(x=y) = ½, complete reads, G3 holds) are as cited.
  - (SP) and Theorem E(b) are at :504–556.
  - REC-1 rows 1, 2, 5, 6, 9, 18, 20, 21, 35, 40, 41 and 46, C5–C7, OBL-SP (:249ff) and §6 are as cited.
- **E1 vs F2-1 A★2.** `A-star.md`:38–45 on `main` is the invariant-measure Koopman form, as stated.
- **MECH-2 Lemma F** uses an orthogonal frame (DESIGN:322–323). So T3's generalization to spanning
  linear frames is described correctly.

## 2. Findings

**A. T7(b) is not new (§A.19; owner priority 1/2).** RECONCILE row T7 says "**+** The (b) lemma is new
at paper level", and §5 lists "the T7(b) realized-sum lemma" among the genuinely additional items.
- The lemma "every branch of a family realized on T is Σ conj(M_i) with M_i ∈ 𝓘(T)" is the kernel
  theorem `realized_of_instAvail` (ImplementationLocality:530) [K] on `main`. Its proof is the same
  induction: op and readout by `realized_conj`, coarse by `realized_sum`, bind by `arch.mul`, and
  discard by `realized_discard`, which uses `discardWith_uniform_conjChannel`, `block` and `smul`.
  INTERVENE cites `Realized` (:250) and re-proves the theorem without citing it.
- The corollary (a non-diagonal-preserving branch has a non-monomial admissible summand) is the
  kernel proof pattern of `exists_nonMonomial_of_layerFlowExecutable` (ExecSource:52–70),
  `configurationLevel_not_layerFlowExecutable` (LiftAudit:183) and
  `configurationLevel_falsifierUnavailable` (ManuscriptAxioms:155). Each is stated there for a
  specific operation.
- The general statement for an arbitrary system branch is already in APPROX r4a (#1221 @ `e41cf613`,
  `APPROX-UNIT1.md`:455–466, [R-off]), which cites `realized_of_instAvail` and
  `discardWith_uniform_conjChannel` explicitly.

T7(b)'s only addition is the label "level-one NX-1 ⇒ FI-1", which #1216 c.6793397036 already records.

**B. A cross-document scope difference was missed (§A.19, "Check cross-document consistency").**
INTERVENE T7 and its §3 table leave "NX-1(C) on the system ⇒ FI-1" open except under
`SystemToLevelOne`. APPROX r4a (:463–467) states it also under `LabelInvariant` transport. For a
label-invariant 𝓘 this is immediate: transport the bare-S witness of T7(b) along S ≃ S×Fin 1, and
non-monomiality is invariant under reindexing (hand check). The substratum and permutation classes
carry kernel label invariance (`substratumClass_labelInvariant`, `permClass_labelInvariant`). Level
n > 1 stays open. This is a stronger result available, not an overclaim, but RECONCILE should record
it.

**C. The governance statement is false as written (item 6).** RECONCILE §4 says that no repository
issue or PR comment created or updated since 2026-11-11 mentions INTERVENE before c.6854241002.
#1216 c.6793397036 (amaybaum, 2026-11-11T10:28:21Z) does mention it, in item 3: "Related draft:
INTERVENE-1 (PR #1230, WIP, under review)". RECONCILE itself cites that comment in row T7. The
comment authorizes nothing ("it authorizes nothing").

The substantive finding stands:
- No #1169 comment mentions INTERVENE-1 or SUBSTATE-BRIDGE-1 before c.6854241002. Every comment since
  2026-11-10 was checked.
- The "Proceed as suggested" quotes on #1169 (c.6763928950, c.6766109672, c.6767228389,
  c.6768774955) concern other units.
- No authorization record for either unit was located.

The reference "(§A.42 item 7)" is the native-round designation clause. For a research record, the
operative rule is §A.45 rule 3 (an authorization entry links the owner's recorded comment).

**D. 𝔊_K is mischaracterized (item 4).** §2 says that N2.1 and 𝔊_K fail simplex-embeddability "when
preparations or reachable laws are non-spanning". That describes N2.1 only. In 𝔊_K every point law
[ab] is reachable through PREP(a,b) (OA2:442–446). The contextuality comes from preparation
differences moved out of reach, with the joint read physically absent: "a designed classical,
per-horizon instance of M-INACC" (OA2:466–467). Corollary B′ (OA2:319–323) states both routes:
"preparation equivalences **or** effect equivalences coarser than ontic equality". The boundary
conclusion survives; only the description changes.

The closing sentence "point at the same room" is an analogy with no formal map (Bridge and no-go
scope):
- G1's non-spanning concerns a route-E_f encoding frame;
- OBL-SP's (SP) concerns the reachable record laws of the native affine class under `D_0`.

**E. The E_f boundary flag is incomplete and imprecise (item 3, inconsistency 1).**
- The §3 directional-table row "faithful (E_f, H-LIFT, linear injective L) ⇒ ¬NX-1(E_f)"
  (INTERVENE:222) also drops "spanning".
- Review nit 3 names only the post-T3 prose.
- Without spanning, the frame matrix is not unique, so "the maps with an entrywise nonnegative frame
  matrix" (INTERVENE:123) is not well defined. On its existential reading the "Fails" verdict holds
  but separates nothing (S2c). The defect is a verdict stated without the hypothesis that gives it
  content, more precisely than "broader than T3 proves".

**F. Q1 labels are attributed to REC-1 that REC-1 does not assign (item 5).** REC-1 rows 9 and 18 are
**Q1-I** only (REC-1-r7:123, :132), not "Q1-I and Q1-μ". Typing H-IND as Q1-I/Q1-μ is RECONCILE's own
reading, and REC-1 has no row for H-IND. P-CONF's H1–H2 are Q1-D (ledger (ii)). "H-IND plays the role
of a fixed lift" asserts an identification that INTERVENE §6 explicitly leaves unaudited ("exact
relation to H-IND … not re-audited").

**G. T2's "Dup" mixes scopes (owner priority 1).**
- OA-2 N0 / Lemma 0 is the same statement at essentially the same scope: protocols from φ, fixed-law
  attachment, discard, heralds and feedback; every φ, μ; a fixed lift playing H-IND's part. The
  differences are adaptive stopping and κ correlated with s.
- OA-1 row 9 and Main:588 are narrower, access-specific (read/write, `obsTheory`) results. They are
  INTERVENE's case (ii), not duplicates of the case-(i) statement.

**H. "Establishes" conflicts with §A.46 item 1 (item 5).** The §5 heading "What each draft
establishes" is applied to off-`main` paper drafts reviewed only by a model.

**I. The Q2 classification of the saturation register is inconsistent with REC-1's practice
(item 4).**
- REC-1 rows 6, 17 and 20 class designed maps reachable from a stated initial law as Q2-F with
  designed-map standing.
- RECONCILE classes the saturation register (a designed bijection with a stated prior) as Q2-A by
  analogy to row 1. Row 1 is the closer analogue, being a per-target realization. That is
  defensible, but "Neither draft exhibits a Q2-F … operation" should then be scoped to operations
  outside 𝒦.

The conclusion relevant to the owner's priority is unaffected: nothing missing is presented as
derived. The register realizes only members of 𝒦, and no draft supplies a state-mixing or other
non-classical operation at any Q2 level above A.

**J. Smaller items.**
- **Writer-pass list.** It omits review 5857985732's nit 2. INTERVENE:108's "Then the output is not a
  function of μ (X7)" generalizes an existence countercontrol to every procedure (finite test →
  universal claim).
- **T5's "nearest" sources.** APPROX r4a also contains C2/C3 ("CM's isometries are exactly the
  monomial ones") and the FI-1 witness (`APPROX-UNIT1.md`:471–483). T5's NEW content is (c),
  `InstAvail CM ↔ InstAvail substratumClass`, and the theory equality.
- **Landing order.** INTERVENE → #1231 is not forced: #1231's files do not cite INTERVENE. Only both
  → SUBSTATE is forced.
- **Re-pin.** The Lean citations did not drift. `SystemToLevelOne` :116 is the docstring line at the
  same commit, and the `def` is at :117.
- **[L] facts.** They are external inputs needing citations, not §A.42 item 8 references to content
  off `main`.
- **Q-868-H pin.** The named branch head is `ffc9cda4`, not `acf28d3a`. The two later commits touch
  the header status, a probe-repeat note and hashes, not (V). (V)'s premises include SA-1(a) and NNB
  besides P3/(iv), E-iso and WL (Q868H-UNIT1:47–54).
- **L1/L4 summary.** "no within-cone dependence" can be read as excluding the O2 window. SUBSTATE
  leaves that window untested.
- **Process.** c.6854241002 requires "ChatGPT review at the exact head", and §A.43 item 2 requires
  pushed checkpoints. A working-area file has no head. The record needs a pushed commit on a branch
  other than #1230's or #1232's.

The other inconsistencies (2–4 of RECONCILE §5) are real and correctly described, subject to F and
to SUBSTATE §3.1 being pin drift rather than an error at its pin. No conditional is promoted to
unconditional in RECONCILE's central claims, and no interface-specific obstruction is stated as
OI-wide, except the wording issues F and H.

## 3. Required changes (exact old → new, in RECONCILE.md; each old string occurs once)

1. **Row T7, reconciliation cell (A, B).**
   - old: `**C** with #1216 c.6793397036 (level-one scope). **+** The (b) lemma is new at paper level.`
   - new: `**C** with #1216 c.6793397036 (level-one scope). **Dup:** the (b) lemma is the kernel theorem \`realized_of_instAvail\` (ImplementationLocality:530) [K], same induction, not cited by the draft; its corollary is the proof pattern of \`exists_nonMonomial_of_layerFlowExecutable\` (ExecSource:52) and \`configurationLevel_falsifierUnavailable\` (ManuscriptAxioms:155) [K], stated for an arbitrary system branch in APPROX r4a (#1221 @ \`e41cf613\`, :455–466, [R-off]). **X (scope):** T7 leaves system NX-1 ⇒ FI-1 open without \`SystemToLevelOne\`; APPROX r4a (:463–467) also states it under \`LabelInvariant\` transport, immediate for a label-invariant 𝓘 (transport along S ≃ S×Fin 1). Level n > 1 stays open.`
2. **§5, additional items (A).**
   - old: `- the T7(b) realized-sum lemma;` (with its line break)
   - new: (delete the line)
3. **§5 option (c) (A).**
   - old: `(T5, T7(b), G1 with E2,`
   - new: `(T5, G1 with E2,`
4. **§4 governance (C).**
   - old: `No #1169 comment, and no repository issue or PR comment created or updated since 2026-11-11, mentions INTERVENE before c.6854241002 (2026-11-13).`
   - new: `No #1169 comment before c.6854241002 (2026-11-13) mentions INTERVENE-1 or SUBSTATE-BRIDGE-1, and no issue or PR comment created or updated since 2026-11-11 records an authorization for either; the one earlier mention found, #1216 c.6793397036 (2026-11-11T10:28:21Z), names INTERVENE-1 as a related draft and authorizes nothing.`
   - In the same bullet, old: `a landing record would have to quote the authorization (§A.42 item 7).` new: `a landing record would have to link the owner's recorded authorization (§A.45 rule 3).`
5. **§2 boundary (D).**
   - old: `OA-2 N2.1 and 𝔊_K (row 20) show that fragments built only from 𝒦 operations can fail to be simplex-embeddable when preparations or reachable laws are non-spanning.`
   - new: `OA-2 N2.1 and 𝔊_K (row 20) show that classical configuration models, all of whose operations lie in 𝒦, can fail to be simplex-embeddable: in N2.1 because the reachable laws do not span (reads complete); in 𝔊_K because preparation differences are moved out of reach of every read (point laws reachable; M-INACC, OA2:466–467; a designed non-affine map).`
   - old: `point at the same room, the (SP)-failing case, that OBL-SP` new: `point, by analogy only, at the (SP)-failing case that OBL-SP` (the remainder of the sentence is unchanged). Then append after that sentence: ` G1's non-spanning concerns an encoding frame on route E_f; OBL-SP's (SP) concerns the reachable record laws of the native affine class under \`D_0\`; no map between them is given.`
6. **Row T3, boundary flag (E).**
   - old: `**Boundary flag:** the §0 table row E_f, the §0 lemma summary and the prose after T3 ("any linear injective frame") all drop "spanning" (review nit 3, unapplied). Without spanning the conclusion is not an obstruction: SUBSTATE S2c gives a non-spanning octahedral frame on which the Hadamard acts as a permutation. As displayed, the §0 verdict is broader than T3 proves.`
   - new: `**Boundary flag:** the §0 table row E_f, the §0 lemma summary, the prose after T3 ("any linear injective frame") and the §3 table row "faithful (E_f, H-LIFT, linear injective L) ⇒ ¬NX-1(E_f)" all drop "spanning" (review nit 3 names the post-T3 prose; unapplied). Without spanning the frame matrix is not unique, so the E_f class ("the maps with an entrywise nonnegative frame matrix", §1.4) is not well defined; on its existential reading "Fails" holds but separates nothing: SUBSTATE S2c gives a non-spanning octahedral frame on which the Hadamard acts as a permutation. As displayed, the §0 verdict is stated without the hypothesis that gives it content.`
7. **§5 conflict 1 (E).**
   - old: `1. **INTERVENE §0, E_f row** (and the post-T3 prose): "spanning" is missing, so the verdict is broader than T3 proves.`
   - new: `1. **INTERVENE §0, E_f row** (and the §0 lemma summary, the post-T3 prose and the §3 table row): "spanning" is missing, so the verdict is stated without the hypothesis that makes the E_f class separating.`
8. **Row T2 (F, G).**
   - old: `In REC-1's vocabulary the premises (state space = laws on configurations, a fixed outside kernel) are **Q1-I and Q1-μ**, not Q1-D. REC-1 classes the same results that way: row 9 (OA-1 configuration ceiling) and row 18 (OA-2 N0, "state-space choice").`
   - new: `In REC-1's vocabulary the state-space premise (laws on configurations, route C's identification) is **Q1-I**, as REC-1 classes the same kind of result: row 9 (OA-1 configuration ceiling) and row 18 (OA-2 N0, "state-space choice"), both Q1-I. Typing H-IND (a fixed outside kernel) as Q1-I/Q1-μ is this reconcile's reading; REC-1 has no row for it. P-CONF's H1–H2 are Q1-D (ledger (ii)).`
   - old: `**C / Dup:** OA-1 row 9 [K] ("an escape must change what an observer operation acts on", OA1:420–421); OA-2 N0 verdict "NO for this class" (row 18); Main:588 (no state-mixing operation under finite bijective read-write dynamics) and Main:718.`
   - new: `**Dup:** OA-2 N0 verdict "NO for this class" (row 18), at the same scope up to adaptive stopping and an s-correlated κ. **C, narrower (access-specific, case (ii)):** OA-1 row 9 [K] ("an escape must change what an observer operation acts on", OA1:420–421) and Main:588 (no state-mixing operation under finite bijective read-write dynamics); Main:718 (diagonal inputs).`
9. **§2 (F).**
   - old: `They do depend on H-IND, which plays the role of a fixed lift (OA-2 N0, MECH-2 H-LIFT) and in REC-1's terms is a Q1-I/Q1-μ premise.`
   - new: `They do depend on H-IND, which is analogous to a fixed lift (OA-2 N0, MECH-2 H-LIFT; the exact relation is not audited, INTERVENE §6) and is read here, not in REC-1, as a Q1-I/Q1-μ premise.`
10. **§2 opening (I).**
    - old: `**No.** Neither draft exhibits a Q2-F or Q2-P operation.`
    - new: `**No.** Neither draft exhibits a Q2-F or Q2-P operation outside 𝒦, and neither exhibits the missing state-mixing operation at any level. The saturation register is a designed bijection with a stated prior; it is classed here with REC-1 row 1 (per-target realization, Q2-A), though under the convention of rows 6, 17 and 20 it would be Q2-F with designed-map standing; either way it realizes only members of 𝒦.`
11. **§5 (I).**
    - old: `None supplies an operation reachable under one fixed dynamics, and none supplies a physically derived one.`
    - new: `None supplies an operation outside 𝒦 reachable under one fixed dynamics, and none supplies a physically derived one.`
12. **§5 heading (H).**
    - old: `**What each draft establishes** (paper level, reviewed by ChatGPT only, conditional throughout):`
    - new: `**What each draft argues** (paper level, off \`main\`, reviewed by ChatGPT only, conditional throughout; not established under §A.46 item 1):`
13. **§5 SUBSTATE bullet (J).**
    - old: `  - Site-fibred substates on \`main\` add no edge and no within-cone dependence (L1, L4).`
    - new: `  - Site-fibred substates on \`main\` add no edge (L1, L4) and leave the within-cone (O2) window as in the finite model, untested.`
14. **§5 option (b), writer pass (J).**
    - old: `a writer pass applying the outstanding nits (T0 termination, "spanning" in §0 and after T3, the H-IND and "case (i)" gloss, the E2 full-domain scope, the item-5 premises);`
    - new: `a writer pass applying the outstanding nits (T0 termination; §1.3's "the output is not a function of μ (X7)" narrowed to the existence statement X7 supports, review nit 2; "spanning" in §0, after T3 and in the §3 table; the H-IND and "case (i)" gloss; the E2 full-domain scope; the item-5 premises; T7(b) citing \`realized_of_instAvail\` and APPROX r4a's \`LabelInvariant\` route);`
15. **Landing order (J).**
    - old: `**Landing order forced by the dependencies:** INTERVENE (with APPROX or BRIDGE or a self-contained definition), then Bell-scope #1231, then SUBSTATE.`
    - new: `**Landing order forced by the dependencies:** INTERVENE (with APPROX or BRIDGE or a self-contained definition) and Bell-scope #1231, in either order (#1231 does not cite INTERVENE), then SUBSTATE.`
    - old: `closing the §4 gaps in the order INTERVENE → #1231 → SUBSTATE` new: `closing the §4 gaps, INTERVENE and #1231 before SUBSTATE`
16. **Re-pin (J).**
    - old: ``**Re-pin needed:** the Main and Lean line citations (−2 shift; `SystemToLevelOne` is at :117).``
    - new: ``**Re-pin needed:** the Main line citations (−2 shift). The Lean citations did not drift (only `OIRealization.lean` changed); `SystemToLevelOne` :116 is its docstring line, the `def` is at :117.``
17. **[L] gap (J).**
    - old: `- **Gap: the [L] facts.** Disintegration, Lusin–Souslin, and Bell's theorem for measurable λ need cited sources.`
    - new: `- **Support gap, not a §A.42 item 8 reference: the [L] facts.** Disintegration, Lusin–Souslin, and Bell's theorem for measurable λ are external inputs and need cited sources.`
18. **Pins (J).**
    - old: ``- Q-868-H r3: `acf28d3a`.``
    - new: ``- Q-868-H r3: `research/q868h-868-20261113` @ `ffc9cda4` (read at `acf28d3a`; the two later commits change the header status, a probe-repeat note and hashes, not (V)).``
    - old: `for native U′ product tests under (iv) via P3, E-iso and WL.` new: `for native U′ product tests under SA-1(a), P3 with (iv), E-iso, WL and NNB.`
19. **Row T5 (J).**
    - old: `The nearest are row 46 (OICORE-1 Lemma M, [R-off]) and APPROX r2/r4a C1 (off \`main\`, #1221).`
    - new: `Its parts (a), (b) and (d) are in APPROX r2/r4a C1–C3 (off \`main\`, #1221, :471–483: CM an Architecture, "CM's isometries are exactly the monomial ones", the FI-1 witness); the NEW step is (c), \`InstAvail CM ↔ InstAvail substratumClass\`, and the theory equality it gives. The nearest REC-1 row is 46 (OICORE-1 Lemma M, [R-off]).`
20. **Standing (process).**
    - old: `It is a working-area record, not on any branch.`
    - new: `It is a working-area record, not yet on any branch; the ChatGPT review that c.6854241002 requires at an exact head needs it pushed to a branch other than #1230's or #1232's (§A.43 item 2).`

Changes 1–5 are required (A, C, D). Changes 6–20 are precision fixes. None of them changes RECONCILE's
central conclusion or its disposition options (a)–(e). Option (c) loses T7(b) and gains a note that
T5's new content is only its part (c).
