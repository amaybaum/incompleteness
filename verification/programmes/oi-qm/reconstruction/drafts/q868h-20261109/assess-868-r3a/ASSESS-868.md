# #868 re-assessment: joint-test validity and composition against the #1210/#1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r3a. r3 followed the independent review
`review/REVIEW-868-r2.md` (sha256 `d37cb1b1…8f11`, REVISE (narrow)); independently reviewed: ACCEPT WITH NITS
(REVIEW-868-r3.md, `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d`); nits applied in r3a.** Nothing
here is adopted, promoted or proposed for the manuscripts. No premise is adopted. A review ACCEPT, if reached,
authorizes nothing further. The r3 text is kept unchanged at `r3/ASSESS-868.md` (`4cd2fb04…f3228`), the r2 text at
`r2/ASSESS-868.md` (`f4873a44…4ff34ae`) and the r1 text at `r1/ASSESS-868.md` (`3499d405…13c3`); each change is
mapped in `DISPOSITIONS-r3a.md` (and, for r3 and r2, `DISPOSITIONS-r3.md` and `DISPOSITIONS-r2.md`).

- **Accountable home:** #868. Parent programme #1169; status source #914 (row O-K2(P)).
- **Authorization:** owner (amaybaum), 2026-11-09, recorded in #1169 c.6740116927 (12:31:12Z) and #868
  c.6740118315. The option text reads: "**#1059/#1049/#868 audits** — One paper-only unit each, re-assessing its open
  question against today's #1210/#1211 findings (Born exponent; linear vs affine dynamics; joint-test validity), each
  with a fresh review. Exact generic checks only." The #868 record adds: "Not authorized: computation on an OI
  mechanism, new physical assumptions, freeze, dispatch, manuscript changes or merges." The owner's direction of
  2026-11-09 (#1169 c.6740778880), relayed by the coordinator, is applied: product-test validity is kept distinct
  from genuinely quantum joint-state behaviour (passing every product test is not being a quantum state), and configuration versus
  encoded carriers, mathematical availability versus derivation from OI, and coherent mixing versus the full quantum
  probability and composition rules are kept apart (§1).
- **What this unit did:** read Issue #868 and its comments, #914's body and comments (for O-K2 and D-02), the records
  below, and the two draft sets; wrote this file and three probes of exact checks on generic matrices (§11). No git,
  repository or GitHub write. No computation on any OI mechanism. Hand reasoning about stated OI constructions is
  marked [A] and rests only on what those records state.

***

## 0. Summary

**Q1. What is established, conditional or missing for the physical source of joint-test validity and composition.**

- *Established, as conditional mathematics.* The pair-cone theorems on `main` hold under explicit hypotheses:
  product inclusion, cone closure, product-test validity (maxCone), and invariance under `cnot` and the drive
  (`EqvK2MaxCone`, `KTokenMaxCone`, kernel). The composite interface laws hold without local tomography (COMP-1,
  kernel). A maximal-cone vector read as an operator carries the Lorentz cone into itself (`lor_toOp_of_maxCone`,
  DIM-1, kernel). None of these sources a hypothesis.
- *Conditional (W).* A common positive-state / local-instrument representation would imply complete-history
  no-signalling and the 2√2 bound (T2 §6, model-reviewed W record). It sources no hypothesis either.
- *Validity restated as a herald condition (§4.1).* On the bilinear carrier `W d` with tests from `eball d`,
  product-test validity holds iff every remote herald by an effect on one wing lies in the Lorentz cone: (⇒) is the
  kernel's `lor_toOp_of_maxCone`; (⇐) follows from the Lorentz pairing bound [A]. In operator form both directions
  are one identity (block positivity is positivity of every local conditional matrix), whose (⇒) direction
  `bridge-compatibility-audit/source-assessment.md:17-19` [W] states. For an available test family, validity holds
  iff the heralds by available effects lie in the **dual cone of the available effects** on the other wing. On the native
  Pauli tests that dual cone is the cube, not the octahedron of the native encoded body, so closure of the native body
  under heralding is *sufficient* for validity on native tests and not necessary (§4.1, witness w3). The heralds are
  slices of the composite preparation, so validity remains a clause about the composite preparations admitted by the
  pair source and dictionary (J13, J1). Test availability (`hsharp`) is a separate hypothesis.
- *Validity is not quantumness.* Passing every product test does not make a joint table a quantum state. The table
  `(I + X⊗X + Z⊗Z)/4` passes every full-ball product test and has eigenvalue −1/4; the swap operator is nonnegative on
  every product of pure states and has eigenvalue −1 (§4.3; G1, G4; r2 V3; r3 W3, W4). In the K2 route validity
  (`hmax`) is one of six hypotheses, all on the cone `K` the table belongs to and not on the table: product inclusion
  (`hH1`), cone closure (`hadd`, `hsmul`), validity, `cnot` invariance (`hH2`) and drive invariance (`hA`). With
  all six, `K = Q3` (kernel).
- *Missing (first missing input per clause, §4).* The physical pair update and preparer (M18/R6.5). The pair's
  state/test dictionary and local tomography (Main:218, Main:652). Product inclusion at full-ball scope: within
  Main:564's interface rules on the configuration carrier, that needs both a non-monomial operation (FI-1's content)
  and a non-real operation, one that takes some state real in the configuration basis to a non-real one (§4.4). The
  quarter phase (O1, adjoined as a stated intervention principle, Main:590) is one source of the second. The kernel's
  layer flow and the driven transition of GR:250, both complex and non-monomial at generic times, are others; none of
  the three is derived from OI. Availability of the non-Pauli sharp tests. An entangling operation acting as the table `cnot`. Drive invariance.
- *Native evidence on composites (scoped).* The one native two-wing construction on `main` is QP node 10 (U′
  encoding, an encoded carrier; independent parities). Its reported correlators ⟨XX⟩ = ⟨ZZ⟩ = 1 force ⟨YY⟩ = −1 for
  any quantum state, while QP reports ⟨YY⟩ = 0, so no completion of its table is quantum (§4.3). Under the [A] zero
  completion of QP's other cross terms, the table passes every full-ball product test. Validity holds there and
  quantumness fails, at the gate. K2-GUARD-1 (kernel) and QP's native one-copy reflection together make C-CP (or a
  composite-level restriction of the translation) necessary for any native route to the table `cnot` that also has
  the `(x+, z+)` preparation, Pauli product reads and sequential composability (§4.3) [A + X]. This is the standard
  fact that a determinant −1 one-copy reflection is positive but not completely positive (L).

**Q2. Overlap.** #868 needs FI-1's content for one of its clauses and is not reached by it; no linear order among the
open obligations is asserted.
- FI-1 (BRIDGE r4 §5.1 [D]) is a necessary condition, in one direction only, for exact finite endomorphic
  operational QM on the configuration carrier. It is not the earliest or the only gap. The quarter phase (O1) and the
  layer flow (O2) are independent obligations on the two-state carrier (K `obligations_independent`,
  C5Discovery.lean:59); that independence is from the layer flow, not from mixing in every form (§4.4). H-Bell is a
  further gap: in the sources read it is not derived from FI-1 or the phase and derives neither, and no independence
  theorem is stated (BRIDGE r4 §5.1(c)).
- #868's full-ball product inclusion (J3) needs, under Main:564's rules, FI-1's content (a non-monomial operation)
  **and** a non-real operation, of which O1 is one source; one operation can meet both (the layer flow, the driven
  transition). Drive invariance (J8) needs a non-monomial operation on the route through available rotations only.
- FI-1's content is not sufficient for #868: a real non-monomial operation such as H⊗H leaves local tomography
  failing (rebits; G5, r2 V6), and the dictionary, the table `cnot` and the composite preparations remain.
- Generating coherent mixing is not supplying the composition rules: J1, J2, J5, J7 and J13 are not reached by any
  mixing operation.
- Relations to #1210 (§6): M18 = J13 and R6.12 = J2 (same clause, same anchor); M17 contains J2 and part of J1;
  R6.11 is a part of J9; R6.9 and J12 are related one way only (under J9 with a cross-wing response present, the
  admissible cone `C_i` lies inside a masking class); J9 ⇒ M20, with M20 ⇏ J9 witnessed by a non-quantum law below
  Tsirelson's bound.
- QX-4's "joint reads" and QX-7's "composition" are sequential, single-carrier objects (#913), not #868's.
- The Bell selection (H-Bell, M19) is separate. In the one-step case Main §3.3 [P] gives |S| ≤ 2; A6.1 [D,
  model-reviewed off `main`] extends it under (D), (L′) and MI, held by design and branch choice, so #868's interface
  reaches |S| > 2 only through a failure of (R) by a coupling path (R6.7/M19).

**Q3. Smallest decisive next paper question (§7): Q-868-H, with two separately stated parts.** On native two-wing
preparations built from product supplies and available couplings, (V) does every remote herald by a natively
available read leave the other wing in the dual cone of the native tests (validity on native tests, J5), and (C)
does it leave the other wing in the SA-1(c)-restricted encoded body with its dictionary sound (closure)? (C) implies
(V); (V) does not imply (C). It needs an authorization this unit does not have: paper analysis of a native
construction.

***

## 1. Conventions

- **Status:** *proved* [layer], *disproved* [counterexample], *conditional* [named hypotheses], *open* [named gap].
- **Layers:** K kernel; P paper proof on `main`; W research record on `main`, model-reviewed (an author-posted or
  model acceptance is not verification, §A.46 item 7); D draft off `main` (today's #1210/#1211 files, or a
  model-reviewed derivation off `main`); A derivation in this file, unreviewed; X exact check on generic objects in
  this unit's probes, or the reviewer's re-run here (computation-supported only); L literature.
- **Ledger columns** (as #1210 SHARED §9 and #1211 §4): (i) mathematically well-defined; (ii) follows from
  independently justified OI principles; (iii) reproduces the QM prediction. **Column (iii) is never support for
  column (ii).** "None identified" in (ii) is open, scoped to the files read (§11).
- **Directionality (§A.34):** every equivalence below names a witness for each direction. An implication is stated
  as one, and a non-implication carries a witness that satisfies the antecedent and fails the consequent.
- **Distinctions kept apart** (owner direction, 2026-11-09):
  - *product-test validity* (joint statistics of product tests are nonnegative and sound) versus *quantum joint-state
    behaviour* (a positive operator on the tensor product);
  - *configuration carrier* (Main:564's interface with configuration-basis readout; FI-1 is posed there) versus
    *encoded carriers* (QP's U′ encoding, the SA-1(c)-restricted body);
  - *mathematical availability* of a map (the kernel's `cnot`, `actT`, the drive) versus its *derivation from OI* as
    an available operation;
  - *coherent mixing* (FI-1's content) versus the *full quantum probability and composition rules* (dictionary, local
    tomography, entangling gate, composition across uses).

## 2. Provenance

- **Corpus:** `git fetch origin main` → `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`
  (2026-11-09 08:36 +0200). Every `main` citation is at that commit. No `--depth`, `gc` or `prune`. Files were read with
  `git show` / `git cat-file`; the working tree's HEAD (`b1d782f9`) was restored after one detached checkout (r1).
- **Boundary-mode pair-operation-source paper:** written on branch `research/oi-qm-ext-1-gate-a-20261106` at
  `e306143d23f534e7bbbb6e72444c026a0d55ad66` (blob `1e6ced538e13427fc6328582b01d9a8bb713ee59`). **It is on `main`:**
  PR #1173 merged 2026-11-07T20:04:12Z (merge commit `dc0b333a1aaee5780d4f3dc514d92337c2c53307`). `e306143d` is an
  ancestor of `origin/main`. The file `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md`
  at `fd539e15` has the same blob `1e6ced53…`. The head branch is not on `origin`: `git ls-remote` returns no ref for it.
  - Review: #1173 c.6707141951 (2026-11-07T12:48:17Z), ACCEPT by `review_boundary_operation`, posted from the owner
    account. It is a model review, so the paper is a W record. The same holds for `prepared-pair-source.md` (blob
    `9123157c…`) and `composition-source-map.md`, also on `main`.
  - The original #868 planning note is off `main`, at `0e0b3ddc` on `plan/joint-tests-source-20261013`. It is used only
    for the Issue's question text (provenance).
- **Draft inputs (D; hypotheses per §A.46 item 7), sha256 at the time read:**
  - `scratchpad/bridge/BRIDGE-UNIT1.md` r4, `4e97610d…85e2`, the working file when read (kept at `bridge/r4/`; the
    working file is now r5, `78f1098e…91a4`, which carries unchanged the two r4 sentences used here, on encoded
    maps without FI-1 and on H-Bell's independence, at r5 l.469 and l.575), under review:
    `review/REVIEW-UNIT1-r4.md` (`e489fc19…`) is REVISE on it. Its R4-B1 and R4-B2 (the driven transition carries the
    phase; moving the all-ones ray is necessary and not sufficient) are used in §4.4. r3 (`ee1c83c0…8219`, archived at
    `bridge/r3/`) was read for r2 of this unit; `review/REVIEW-UNIT1-r3.md` (`7a6a7f1c…`) is REVISE on it. r2
    (`3905569b…`, read for r1 of this unit) drew REVISE in `review/REVIEW-UNIT1-r2.md` (`3cdf7dc2…4eb3`), whose RB1
    rejected the ordering of FI-1 as the earliest unsupported step. The first review, `review/REVIEW-UNIT1.md`
    (`e242a794…`), is REVISE on r1. Sections cited below as BRIDGE r4 were re-read in r4.
  - `scratchpad/qphen/SHARED-MECHANISM.md` r5 (`a7206701…`; the rows used were re-read in r5), `QX6-BELL-CHSH.md` r5
    (`9e9c0d02…`) and `QX4-INCOMPATIBILITY-LG.md` r5 (`7f4cd21d…`). `review/REVIEW-PHASE1-r4.md` (`755c3af0…`) is REVISE
    (narrow) on r4.
- **Planning record (§A.45 rule 1 finding, not a scientific one).** #868's body describes #1173 as "draft/unmerged" in
  two obligation rows. It links the paper by a commit-pinned URL at `e306143d`, which resolves because `e306143d` is
  reachable from `main`, and PR #1173. The only branch it names, `research/oi-qm-composition-source-20261107`, still
  exists (`2de820fb`). The source governs: the paper is on `main`. Correcting the two rows is ordinary planning
  maintenance under §A.45 rule 3, outside this unit's write scope.

***

## 3. What #868 asks, traced to the statements that consume it

The Issue's research question is: "What physical source supplies the joint state/test pairing, validity of the required
product tests and the locally tomographic composition interface?" The clauses it names are hypotheses of these
statements:

| statement | hypotheses (as stated) | layer |
| --- | --- | --- |
| `pairCone_eq_Q3_of_drive_maxCone`, `pairCone_eq_Q3_of_sharp_available` (`OIBridge/EqvK2MaxCone.lean:153-212`); k-token forms (`KTokenMaxCone`) | `hH1` every product of `eball 3` states in `K`; `hadd`, `hsmul` cone closure; `hmax` `K ⊆ maxCone (eball 3)`, or `hvalid` + `hsharp` (validity on an available family containing the sharp tests); `hH2` `cnot` invariance; `hA` invariance of `K` under one-copy rotations and the cyclic map | K, conditional |
| `pairCone_eq_Q3_iff_drive_maxCone` | equality ⟺ (`hH2` ∧ `hA`), **relative to fixed** `hH1`, `hadd`, `hsmul`, `hmax`. Witnesses: `driveInvariant_of_eq_Q3` (⇒), `pairCone_eq_Q3_of_drive_maxCone` (⇐) | K |
| `lor_toOp_of_maxCone` (`OIBridge/CompositeDimension.lean:1049`; DIM-1 `result.md:32, :101`, `preregistration.md:71-72, :147`) | `ω ∈ maxCone (eball d) → Lor f → Lor (toOp ω f)`: a maximal-cone vector read as an operator carries the cone into itself | K |
| carrier `W d` (`CompositeDimension.lean:95-97`) | "Local tomography is the premise this carrier encodes" (also DIM-1 prereg:180) | K (definition) |
| COMP-1 `PreComposite` / `Composite` | product effects are effects on the body (field); `lt` is the single further field; no composite sourced beyond named instances | K |
| K2-GUARD-1 `no_candidateCone_cnot_reflY` | no `K` with all ball products, `K ⊆ maxCone`, invariant under both `cnot` and `actT reflY` | K |
| T2 §6 eq. (1) (`composition-source-map.md`) and composition-access `REPORT.md` (1) | fixed linear `D_i` on an admissible cone `C_i`, positive and trace-matching on `C_i`, intertwining native record-resolved kernels with local CP instruments, at every use | W, conditional sufficiency |
| Main:564 characterization | complex matrix kinematics and composite "taken as given"; (i) validity at every ancilla level; (iii) inert spectators; (iv) composite unitary control; (v) iterated ancilla closure | K + P |

Main states the boundary directly: kinematic locality "does **not**, by itself, prove local tomography or that all
visible composites and coherent interventions belong to one common tensor-product quantum instrument category"
(Main:218; also Main:652).

***

## 4. Restriction ledger

### 4.1 Lemma H: product-test validity as a herald condition

*Setting.* Use `W d` and `eball d` as in the kernel. An effect on `eball d` is an affine `e(x) = c + u·x` with values
in `[0,1]` on the ball. So `c ≥ |u|`, and `e = c · (1, u/c)·(1, x)` with `|u/c| ≤ 1`, or `e = 0`. Hence
`maxCone (eball d) = {ω : ahatᵀ ω bhat ≥ 0 for all a, b ∈ eball d}`, with `ahat = (1, a)`. For `a ∈ eball d`, write the
**heralded B-vector** `h_a(ω) = ahatᵀ ω = (t, v) ∈ ℝ × ℝ^d`. Let `Lor_d = {(t, v) : |v| ≤ t}` be the cone over the
ball.

*Statement.* `ω ∈ maxCone (eball d)` ⟺ `h_a(ω) ∈ Lor_d` for every `a ∈ eball d`. The same holds with the wings
exchanged.

- *(⇒)* Layer K: `lor_toOp_of_maxCone` (DIM-1), in the mirror orientation (`toOp ω f = ω·f` heralds the control wing
  by a target effect). The `h_a` orientation follows by transposition, since `ahatᵀ ω bhat = bhatᵀ ωᵀ ahat` and both
  wings carry `eball d` [A; r3 W5]. Elementary form: if `|v| > t` for some `a`, then `b = −v/|v| ∈ eball d` gives
  `t − |v| < 0`. If `v = 0`, any `b` gives `t ≥ 0`.
- *(⇐)* [A], elementary, from the Lorentz pairing bound (`lor_pair_bound`, same module): for `b ∈ eball d`,
  `ahatᵀ ω bhat = t + v·b ≥ t − |v||b| ≥ 0`. It is not stated in the module as one theorem. In operator form both
  directions are the identity `⟨a⊗b|X|a⊗b⟩ = ⟨b|σ_a|b⟩`, `σ_a = (⟨a|⊗I) X (|a⟩⊗I)` (r3 W5): block positivity is
  positivity of every local conditional matrix (L). `bridge-compatibility-audit/source-assessment.md:17-19` [W]
  states the block-positive ⇒ conditional-PSD direction with that identity.

*Available-family form.* `maxConeOf avail` ⟺ heralds by available A-effects lie in the **dual cone of the available
B-effects** (the vectors on which every available B-effect is nonnegative). Same proof.

*Native form.* On `eball d` the dual cone is `Lor_d` because the Lorentz cone is self-dual (`lor_ehom`,
`isEffectOn_affOf`, `lor_of_forall_pair`). On native data it is not the cone over the native body:
- the native tests are the Pauli reads (J6), whose sharp effects `(1 ± σ_i)/2` have as dual cone the cube
  `{|v_i| ≤ t}` (r2 V1; both inclusions, by an explicit nonnegative decomposition over the cube's vertices, r3 W1);
- the native encoded laws "lie in the octahedron" (QP C-EAR, `DESIGN.md:558`).

Witness w3 (zero marginals, ⟨XX⟩ = ⟨XY⟩ = 1, all other entries 0): all 36 Pauli product values are ≥ 0; its herald
by the A-test +x is `(1, 1, 1, 0)`, inside the cube cone, outside the octahedron cone and outside `Lor_3` (reviewer R3;
r2 V2). So:
- *closure of the native body under heralding ⇒ validity on the native tests* (the octahedron lies in the cube);
- *validity on the native tests ⇏ closure of the native body* (w3).

*Reading, one direction at a time [A].*
- Validity (`hmax`) ⟺ every remote herald lies in the dual cone of the tests (Lemma H). This is a condition on the
  heralded slices of the composite ω, quantified over every composite preparation the pair source and dictionary admit
  (J13, J1). It does not remove the composite quantifier.
- Test availability (`hsharp`, J6) is a separate hypothesis. Validity does not imply it, and it does not imply
  validity.
- Complete-history NS (J10) is a further separate clause. Given NS, soundness of the dictionary on product tests
  implies soundness of the single-wing dictionary on the remotely heralded conditional preparations. This is a
  one-directional step, not part of the equivalence.
- This addresses the Issue's third checklist item ("separate sufficient test availability from soundness on joint
  preparations"): availability is J6; soundness on joint preparations is the herald condition with NS.

*Validity is not quantumness.* The herald condition is about product tests only. Block-positive operators that are not
positive pass it: the swap operator has eigenvalue −1 and is nonnegative on every product of pure states (G1; r2 V3),
and the node-10 table below passes every full-ball product test with eigenvalue −1/4 (G4; r2 V3; r3 W3, W4). Product
tests do not decide whether a table is a quantum joint state. In the K2 route the conclusion `K = Q3` is about a cone
`K`, under hypotheses on `K`: `hH1`, `hadd`, `hsmul`, `hmax`, `hH2` and `hA`. Validity (`hmax`) is one of them.

### 4.2 The ledger

| ID | restriction (source) | (i) well-defined? | (ii) from independently justified OI principles? | (iii) reproduces QM? | status; where the gap sits |
| --- | --- | --- | --- | --- | --- |
| J1 | **Pair state/test dictionary:** fixed linear `D` from physical joint boundary laws on an admissible cone into `W 3` (or COMP-1 product data), not refit per setting (T2 §6; composition-access (1); `EqvK2MaxCone` header) | yes, relative to a specified realization and cone | **none identified.** No pair realization is specified (prepared-pair-source §2; pair-operation-source §§2, 7) | yes: Pauli tables of `Herm(4)` | open; first missing input is the pair realization (J13) |
| J2 | **Local tomography:** states determined by product-test tables (COMP-1 `lt`; encoded by `W d`) | yes | **none identified.** COMP-1 sources none; Main:218, :652: kinematic locality does not prove it | complex QM yes; **real QM no** (G5: 9 < 10; `(I ± εY⊗Y)/4` agree on every real product test; r2 V6) | premise field; open. Tied to the token's complex structure (§4.4) |
| J3 | **Product inclusion** `hH1` at `eball 3` scope | yes | partial. A product law for independent supplies on disjoint cells follows from N2's product counting measure via H-PREP (both posits, SHARED §9). On the configuration carrier at full-ball scope it needs coherent single-token preparations: under Main:564's preparation rules (uniformly mixed ancilla, then available operations), monomial Kraus operators keep every prepared state diagonal (G7) [A + X], so a non-monomial operation (FI-1's content) is necessary; and y-axis states need a non-real operation, since operations that keep real states real keep ⟨Y⟩ = 0 (R6d; r2 V5; r3 W6). O1 is one source of a non-real operation; the layer flow and the driven transition are non-real and non-monomial at once (§4.4). None is derived from OI. On the encoded carrier, at most the stabilizer octahedron, under SA-1/H-PREP | yes | conditional at stabilizer scope (posits); open at full-ball scope, needing a non-monomial operation and a non-real operation under Main:564's rules, or a coherent preparation source outside them |
| J4 | **Cone closure** `hadd`, `hsmul` | yes | conditional yes. Sums and nonnegative multiples of unnormalized measures are measures. Mixing preparations needs a randomizer independent of the residual boundary (composition-access REPORT, randomized controllers) | yes | least problematic; conditional on the randomizer clause |
| J5 | **Product-test validity** `hvalid`/`hmax` (joint-test validity) | yes | **not supplied.** By Lemma H it is the condition that every remote herald, over the admitted composite preparations, lies in the dual cone of the tests. On native Pauli tests closure of the SA-1(c)-restricted body is sufficient and not necessary (w3). SA-1(c) is "QM-only: a hypothesis under test" in SHARED §9 [D], so the sufficient route through the native body rests on it; validity itself is not shown to inherit that status | yes, but non-selective. BP ⊋ PSD: swap is block-positive with eigenvalue −1 (G1). The QP node-10 table passes every full-ball product test (zero completion) and is outside Q3 (G4) | open; locus = the composite preparations' heralds (§7, part V) |
| J6 | **Sharp-test availability** `hsharp` (all sharp effects of `eball 3`) | yes | open. Non-Pauli reads are not native (QX-4 R4.5 [D]; O-GEO #867). K1-SHARP-TESTS-1 classifies `2 ≤ d` as two sharp tests and does not source them | yes | open; single-system (#867) |
| J7 | **Entangling preserving operation** `hH2` (invariance under the table `cnot`) | yes | **none identified;** native evidence is negative in its scopes. M2D Theorem U2 [W]: no encoded entangling unitary under R1^⊗n and H-LIFT at `q = 2`. QP node 10 [W]: the native graded coupling acts as CNOT on encoded functionals, but its reported output has ⟨YY⟩ = 0, not −1 (G4c). K2-GUARD-1 [K] with QP's native translation reflection gives §4.3. The kernel's `cnot` is mathematically available as a map on tables; its availability as a native operation is not derived | yes (Q3 is `cnot`-invariant; the iff above, relative to fixed hypotheses) | open. With `hA`, this is where the K2 route selects Q3 |
| J8 | **Drive invariance** `hA`: invariance of `K` under one-copy rotations and the cyclic map (`EqvK2MaxCone.lean:159-160`, `:212-213`) | yes | open (O-DRV, #865). On the route that obtains `hA` from available continuous rotations, those rotations are non-monomial, so a non-monomial operation (FI-1's content) is necessary on that route. `hA` is an invariance of `K`, not an availability statement, so other routes are not excluded | yes | open |
| J9 | **Composition across uses:** T2 (1) at two uses, reuse closure, post-measurement update (R6.11) | yes, for a specified realization | **none identified;** needs J1 and J13 | yes | open. (1) ⇒ complete-history NS and \|S\| ≤ 2√2 (T2 §6 [W]; operator identity instance G6). The converse fails: the zero-marginal law with correlators (1, 1, 1, 1/2) is NS, has every CHSH form ≤ 5/2 < 2√2 and is not quantum (for ±1 observables ‖Aψ − Bψ‖² = 2 − 2⟨AB⟩ forces ⟨A₁B₁⟩ = 1), hence not J9-representable (reviewer R5b–c; r2 V4) |
| J10 | **Complete-history NS** (R6.8, M20) | yes | not derived: "a requirement of the framework's chosen branch" (SHARED §9 [D]; Main:414, :429). Implied by J9, which is itself unsourced | yes | requirement; open |
| J11 | **Tsirelson soundness** (R6.10, M20) | yes | none independent of QM. J9 would imply it, but J9's premise is a positive representation onto local CP instruments on a quantum state, and T2 §6 says the bound "is conditional on the common representation, not a derivation of it from OI"; that is quantum structure, a column-(iii) input, so it is not a column-(ii) route. SHARED §9's "none identified" stands | yes (L) | QM-only as an independent restriction |
| J12 | **Admissible preparation cone `C_i`** (T2's domain of positivity for `D_i`) | yes, for a fixed realization | none. A class fixed only by the balance equations is fitted (SHARED §9; prepared-pair-source §§4–5 [W]) | NS by definition; 2√2 does not follow | open. Relation to R6.9 (a preparation class under which R6.7's cross-wing response balances): under J9 with a response present, `C_i` lies inside a masking class [A, one direction] |
| J13 | **Pair update / preparer / source** (M18, R6.5) | as a requirement | **none:** the first source stop (prepared-pair-source §2; pair-operation-source §§2, 7; boundary-mode proposal supplies neither update/preparer nor an interface change) | n/a | missing; #868-specific; J1, J2 and J9–J12 depend on it, J3, J6, J7 and J8 do not |
| J14 | **Bell design and selection:** (D), (L′), (R), MI; cross-wing response H-Bell (M19) | yes | (L′), (R): protocol, not OI (SHARED §9 [D]). MI: posit (Main:406). H-Bell: none; the branch is a selection (E + St; #1211 F2 [D]; Main:403–406) | one step: \|S\| ≤ 2 (Main §3.3 [P]); with (D), (L′), (R), MI: \|S\| ≤ 2 (A6.1 [D], model-reviewed off `main`) | separate obligation (#1060/#914 row 16). Constrains #868: see §6 |

### 4.3 Native composite evidence and the C-CP link [A + X]

1. **QP node 10's composite** (QP `DESIGN.md:746-768`, on `main`, W; an encoded carrier).
   - QP states: the determined functionals are `f_x^A + f_x^B` and `f_z^A + f_z^B`; with independent uniform parities,
     ⟨XX⟩ = ⟨ZZ⟩ = 1 and ⟨YY⟩ = 0.
   - *Not quantum, whatever the other cross terms.* Any PSD unit-trace ρ with ⟨XX⟩ = ⟨ZZ⟩ = 1 is Φ⁺ and has ⟨YY⟩ = −1
     (reviewer R4a–b). QP's ⟨YY⟩ = 0 therefore excludes every quantum completion. This uses only QP's reported values.
   - *Full-ball validity depends on the completion.* Reading the other cross terms under QP's N2 rule ("unknown slots
     uniform"), any functional not in the span of the determined ones has mean 0, and the table is
     `T = (I + X⊗X + Z⊗Z)/4` [A, from QP's stated rules, not a run of the construction]. Its heralds are
     `(1, a₁, 0, a₃) ∈ Lor_3`, so `T ∈ maxCone(eball 3)` by Lemma H (⇐) (G4; reviewer R4c; r2 V3; r3 W3, which also
     certifies every full-ball product value directly). Another completion, with ⟨XZ⟩ = 1/2, keeps all 36 Pauli values ≥ 0 but gives −1/4 on a full-ball product (reviewer R4d).
   - So in the native construction (zero completion) product-test validity holds and the table is not a quantum state.
     The quantum `cnot` image of `(x+, z+)` has ⟨YY⟩ = −1 (G4c). The native gate does not act as the table `cnot` on
     that input.
2. **K2-GUARD-1 meets QP's C-CP.**
   - QP introduces C-CP ("no available encoded map has an orientation-reversing (determinant −1) action on the Bloch
     octahedron", QP `DESIGN.md:211`). Its stated reason is progress toward the quantum comparator, which is a
     column-(iii) reason.
   - QP node 9 shows that a constant translation in U′ acts as `Y ↦ −Y`, natively in N via P2 and H-PREP (QP
     `DESIGN.md:727-731`).
   - K2-GUARD-1's chain uses only stabilizer data: the product `(x+, z+)`, `cnot`, one-copy `reflY`, `cnot`, and the
     product of sharp effects along −e₁ and −e₃. It gives −1/2 (`pairVal = −2`). The kernel's signed-permutation `cnot`
     equals the table of quantum CNOT conjugation on all 16 Pauli inputs, and `phiW`, `idW`, `chainW` are reproduced
     entrywise (reviewer R2a–e; writer G3b). The kernel's own determinant-+1 control `nflip = diag(1, −1, −1)` gives 0
     (reviewer R2g); the writer's G3c used conjugation by Z, `diag(−1, −1, 1)`, also determinant +1.
   - *Consequence [A].* Consider any native composite in which:
     - a preparation of `(x+, z+)` is available;
     - Pauli product reads are available;
     - the translation acts on joint tables as `reflY`;
     - some available operation acts on joint tables as the quantum `cnot`;
     - the operation, the translation and the operation again compose sequentially on the intermediate preparations.

     Then that sequence assigns probability −1/2 to a product read. So J5 (with J1) fails, and one of the five must
     go. A native route to Q3 composites (J7 in table form) therefore needs C-CP, or a restriction of the translation
     at composite level.
   - *Column (ii).* This gives C-CP a **consistency** reason: it is necessary for J5 and J7 together. It is not an
     independent OI reason, because J7's target is the quantum `cnot`. The link is the standard fact that a
     determinant −1 one-copy reflection (the transpose) is positive but not completely positive (Peres 1996; Horodecki
     1996; L, not re-read here); `mechanism-1-20261107/DESIGN.md:199` already states that the determinant −1 class "is
     not CP". QP does not cite K2-GUARD-1, and K2-GUARD-1 does not cite QP.
   - *Skepticism, since the reading of item 1 favours the framework.* Validity holding natively is cheap: executed
     Pauli reads have nonnegative probabilities by construction. The informative facts are that the table is not a
     quantum state and that the native gate is not the table `cnot`. Validity for non-Pauli tests is not claimed: those
     tests are not native (J6).

### 4.4 Cross-links found while tracing [A + X]

- **Two necessary inputs for J3 on the configuration carrier [A + G7, R6, r2 V5, r3 W6–W8, W10].**
  - Main:564's rules supply preparations only as a uniformly mixed ancilla, then available operations; readout is
    configuration-basis Lüders.
  - If every available Kraus operator is monomial (permutation × diagonal, phases included), every reachable state is
    diagonal (G7a). A coherent product such as `x+ ⊗ z+` then needs a non-monomial operation, which is FI-1's content,
    or a preparation channel outside those rules.
  - y-axis states need a **non-real operation**: an available operation, or instrument branch, that at some level
    takes some state real in the configuration basis to a non-real one. If every available operation keeps real states real, then the
    uniformly mixed ancilla, real Lüders readout, discard and coarse-graining keep every reachable state real, with
    ⟨Y⟩ = 0, while y+ is not real (R6d; r2 V5; r3 W6).
  - Sources of a non-real operation, none of them derived from OI. The second and third are also non-monomial at
    generic times, so one operation can meet both necessities:
    - *the quarter phase* (O1, `PhasesAvailable`, RouteB.lean:132): monomial and non-real, adjoined "as a stated
      intervention principle" (Main:590). After the real non-monomial H it reaches y+ (r2 V5);
    - *the layer flow* (O2, `LayerFlowExecutable`, LiftAudit.lean:112; available by stipulation in `onesTheory`): on
      `Fin 2`, `unit(X, 1/2)` is non-monomial and non-real, fixes the all-ones vector and takes z+ to y− with no
      separate phase gate (r3 W7; reviewer D1). On `Fin 2` it commutes with X, so it does not by itself settle J3
      at full-ball scope there;
    - *the driven transition* `e^{−itX_ab}` of phase-free richness (GR:250–258; MinimalRepertoire.lean:423); the
      equivalence that consumes it "is not a claim that bare observation incompleteness entails these principles"
      (GR:258). In the substratum-source form, the state-mixing operation added to the substratum class beside the
      stated phases is "added as an empirical controllability resource" (Main:590; also GR:260). "No phase operation
      enters" (GR:250) describes the repertoire, not the drive's content: the drive is complex. On three states it is
      the transposition's layer flow times a continuous relative phase on the configuration it fixes, and at a quarter
      turn, composed with the exchange, it is the quarter phase on the third state as a channel (r3 W10; #1211 bridge
      r4 review R4-B1 [D]). W10's identity is the kernel's isolation identity `gateFlow_isolation`
      (LiftAudit.lean:660) specialised to one transposition on three states, where the sign conjugation is trivial
      and `G(t)² = G(2t)` (reviewer K3; `probes/r3a_check.py`). One drive takes `|10⟩` to `y+ ⊗ z+`, and two drives
      with one exchange take it to `x+ ⊗ z+` (r3 W8; reviewer D2); in that preparation the second drive at π/2
      followed by the exchange on the pair `|10⟩`, `|11⟩` is, as a channel, the inverse quarter phase on wing A, the
      first factor (`probes/r3a_check.py`; reviewer K4 on that pair). No separate phase operation is used, and the
      drive itself is complex. With implementation
      locality and embedded observation, phase-free richness gives exact finite endomorphic operational QM
      (GR:254–258; K `oiPlusMin_iff_qm`). The phase content is then carried by the drive, not dispensed with.
  - *Countercontrol.* A real rotation `e^{θ(E_ab − E_ba)}` is non-monomial and moves the all-ones ray, but it is
    real, so it keeps ⟨Y⟩ = 0 (r3 W10c, W6). Moving the all-ones ray is necessary to any access that supplies the
    phases and is not shown sufficient (GR:260); the real rotation shows it is not sufficient for a non-real
    operation either.
  - *Independence, scoped.* `obligations_independent` (K, C5Discovery.lean:59, two-state carrier) separates O1 from O2:
    the substratum theory has the quarter phase and executes no layer flow; the ones-fixing theory executes every
    layer flow and has no quarter phase. It does not make a non-real operation independent of a non-monomial one, since
    the layer flow and the drive are both.
  - Scope: these necessities hold for that interface on the configuration carrier only. They do not exclude a coherent
    preparation source outside it. On the encoded carrier, stabilizer-scope coherent preparations arise without FI-1
    (BRIDGE r4 §5.1 [D], citing QP).
  - `cnot` itself is a permutation. J7's difficulty is not monomiality but what the gate does to coherent joint inputs.
  - The same G7 argument on the four-state configuration carrier shows that, under Main:564's rules, any
    non-diagonal pair state needs a non-monomial operation (reviewer R6a); only a classically correlated pair source is
    free of it.
- **Mixing does not give the composition rules.** A real non-monomial operation such as H⊗H is available in real QM,
  where local tomography fails (G5; reviewer R6c; r2 V6). Supplying FI-1's content therefore does not supply J2, and
  does not touch J1, J5, J7 or J13.
- **J2 and the token's complex structure.**
  - Local tomography holds for complex and fails for real two-level composites (G5). The real-carrier analogue of the
    token loses J2. This is the rebit fact (Hardy–Wootters; L, not read first-hand here), CONFIRMING DIM-1's note that
    `W d` encodes local tomography.
  - Relevance to #1211: its F4/NQ1 (a complex structure on the six-link carrier's real lift, mathematically available
    off the null modes, not derived) and #868's J2 meet at one question: where a complex, not real, single-token
    kinematics comes from. That is O-GEO/#867 for the token. No identification of the two carriers is claimed.

***

## 5. Answer to Q1: established, conditional, missing

- **Established (K/P, conditional mathematics only):**
  - the K2 pair-cone theorems and their relative iff (witnesses named, §3);
  - COMP-1's laws without `lt`;
  - Lemma H (⇒), `lor_toOp_of_maxCone` (DIM-1);
  - K2-GUARD-1's orientation obstruction;
  - Main's graph-cone separation (Main:652);
  - Main's Bell ceiling under its hypotheses (Main:366–416).
- **Conditional (W/D/A):**
  - T2 (1) ⇒ NS and 2√2 (W);
  - A6.1 under (D), (L′), (R), MI (D, model-reviewed off `main`);
  - Lemma H (⇐) and its available-family and native forms (A; `source-assessment.md:17-19` [W] states (⇒) in
    operator form, with the identity that also gives (⇐); L);
  - J3 at stabilizer scope under N2, H-PREP and SA-1 (posits);
  - J4 under the randomizer clause;
  - the native node-10 table: not quantum for every completion (A from QP's reported values, X for the matrix facts);
    in `maxCone` under the zero completion (A, X).
- **Missing, with dependencies (a partial order, not a sequence):**
  - J13, the pair realization: #868-specific; J1 and J2 need it; J9–J12 need J1 and J13;
  - J3 at full-ball scope: needs a non-monomial operation and a non-real operation under Main:564's rules (O1 is one
    source of the second; one operation can supply both), or a coherent preparation source outside them; independent
    of J13;
  - J8: open; needs a non-monomial operation on the route through available rotations; independent of J13;
  - J6, non-Pauli test availability: single-system (#867); independent of J13;
  - J5, validity: the herald condition over the admitted composite preparations; sufficient through native-body
    closure, which rests on SA-1(c);
  - J7, the table `cnot`: native evidence negative in its scopes; tied to C-CP by §4.3; independent of J13.
- **Column discipline.** Every row's column (iii) is "yes" for QM. For J2 (real QM fails), J5 (non-quantum cones pass)
  and J9 (non-quantum NS laws below 2√2 exist) it is also non-selective. No row's (ii) is answered from (iii); J11's
  conditional route through J9 is a column-(iii) premise and is not used in (ii).

## 6. Answer to Q2: where #868's gap sits relative to #1211 and #1210

| today's finding (D) | relation to #868 | direction |
| --- | --- | --- |
| #1211 FI-1 (BRIDGE r4 §5.1): a necessary condition, one direction only, for exact finite endomorphic operational QM on the configuration carrier. O1 and the layer flow O2 are independent (K `obligations_independent`); the driven transition carries the phase (§4.4). No independence theorem relates H-Bell to FI-1 or the phase (BRIDGE r4 §5.1(c)) | FI-1's content is necessary for J3 at full-ball scope (with a non-real operation, of which O1 is one source) and for J8 on the route through available rotations, under Main:564's rules. It is necessary for any non-diagonal pair state under those rules, so for J13 only when the pair source is to be coherent; a classically correlated pair source does not need it. It is not necessary for J1, J2 or J5 as stated. pair-operation-source §5 applies the same configuration-level and positive-compression ceilings to the pair route, so #868's "additional interface gap" contains FI-1's bipartite instance for operations | necessary for J3 (with a non-real operation) and on J8's availability route; not sufficient (witness: H⊗H real, J2 fails; G5, r2 V6) |
| #1211 "coherent composite kinematics open (Main:218)" | the same anchor as J1 + J2 (O-K2(P)) | shared anchor |
| #1211 "physical preparation mechanism missing" | J13's preparer and J3's coherent preparations | J13 and J3 are bipartite and single-token instances of it |
| #1211 F2: the Bell branch is a selection (H-Bell) | J14; separate from #868 | — |
| #1211: site factorization is an input (SM §2.4) | presupposed by J1/J2: the wing split is the site split | upstream input, not discharged by #868 |
| #1210 A6.1 conditional on (D), (L′), (R), MI | J1–J12 with those hypotheses give \|S\| ≤ 2. #868's interface reaches \|S\| > 2 only through a failure of (R), i.e. R6.7/M19 | #868 ⇏ Bell |
| #1210 QX-6 M17 (cone separation, per-observer access maps, local tomography) | M17 contains J2 and part of J1; its cone lemma is Main §3.3 [P], and its access maps are R6.3's | shared part, not identity |
| #1210 R6.12 (local tomography a hypothesis) | = J2 (same clause, COMP-1 premise field) | identical |
| #1210 M18 / R6.5 (pair source absent) | = J13 (same clause, prepared-pair-source §2) | identical |
| #1210 R6.9 (restricted preparation class balancing R6.7) | related to J12 one way: under J9 with a cross-wing response present, J9's fixed split needs the response masked on `C_i`, so `C_i` lies inside a masking class (T2 §6: a mediator across the split "cannot simply be discarded") [A] | containment, one direction |
| #1210 R6.11 (post-measurement update / reuse) | a part of J9 | part of |
| #1210 M20 (NS; Tsirelson, QM-only) | J9 ⇒ both (T2 §6). M20 ⇏ J9: the NS law with correlators (1, 1, 1, 1/2) satisfies both halves of M20 and is not quantum. J9's premise is a quantum representation, so this is a cross-reference, not a column-(ii) route; SHARED §9's "none identified" stands | J9 ⇒ M20; not ⇐ |
| #1210 QX-4 "joint reads" | sequential joint laws and joint measurability on one carrier. A different object (#913's reusable instrument composition); not #868 | no overlap |
| #1210 QX-7 "composition" (M12, M13) | repeated sequential composition of a fixed operation; not tensor composition (NR-11 is optional) | no overlap |
| #1210 M3 (SA-1(c), QM-only) | the sufficient route to J5 on native tests through native-body closure rests on SA-1(c); J5 itself is not shown to | shared (ii)-gap on the sufficient route |

**Verdict.**
- #868 needs FI-1's content, with a non-real operation (O1 being one source), for J3, and on one route for J8. It has
  a composite residue (J1, J2, J5, J7, J13) that FI-1's content does not reach. No order between #868 and FI-1 beyond these necessities is asserted.
- It shares M18 and R6.12 with #1210 as identical clauses, contains a part of M17, contains R6.11 as a part of J9, is
  related to R6.9 one way through J12, and implies M20 through J9.
- Its title clause, joint-test validity, is the condition that remote heralds of the admitted composite preparations
  lie in the dual cone of the tests. Closure of the native body is a sufficient route to it and shares #1210's M3 gap.

## 7. Answer to Q3: the smallest decisive next paper question

**Q-868-H (heralds on native two-wing preparations), in two parts with separate outcomes.**
- *Setting.* Take the native single-token body as stated in the corpus: apparatus-1's SA-1-restricted encoded
  carrier, in QP's U′ encoding, with P1–P3, E-iso, H-PREP and N2 carried as stated posits. Take every two-wing
  preparation built from product supplies and the couplings P3 may arm between the wings' carrier cells (graded, as
  in QP node 10), and every natively available read on one wing.
- *(V) Validity on native tests.* Does every remote herald lie in the dual cone of the native tests on the other wing
  (the cube cone, for the Pauli reads)? By Lemma H (both directions, available-family form) this is J5 on native tests
  for these preparations.
- *(C) Closure of the native body.* Does every remote herald leave the other wing in the native body (the octahedron,
  Lemma Q's protected parity undetermined, SA-1(c) intact), with the single-wing dictionary sound on it? This is a
  no-restriction condition on the native single-token state set.
- *Relation.* (C) ⇒ (V), since the octahedron lies in the cube. (V) ⇏ (C) (w3). Neither implies J6, J7 or J13.
- *Why it is decisive.*
  - (C) yes: (V) follows, so native joint-test validity holds at stabilizer scope for these preparations, with every
    posit carried. #868's residue is then J1/J2 (pair realization, local tomography), J7 (the table `cnot`, tied to
    C-CP by §4.3), J3 and J8.
  - (C) no, (V) yes: the native composite's heralded preparations leave the native single-token state set while
    validity on native tests holds. The native composite is then not a composite of the native single-token theory,
    which is a finding about closure, not a failure of validity.
  - (V) no: one explicit herald outside the cube cone. J5 fails natively at a named preparation and read,
    independently of FI-1 and of the missing pair source.
  - None of the outcomes makes the composite a quantum state, and none supplies J1, J2 or J7.
- *Why it is small.* It needs no pair source, no separation and no Bell table. It uses only couplings and reads the
  corpus already states. Lemma H is already available (K for ⇒). QP's C-LEAK rows (`DESIGN.md:555-557`) settle the
  within-wing and shared-parity cases. What remains is the two-wing graded-coupling case.
- *Decision rule (fixed before any work), for each of (V) and (C) separately.*
  - Pass: the condition holds for every available read on every such preparation, with every posit carried into the
    conclusion.
  - Fail: one explicit herald violates it, with its membership line.
  - Stop: a preparation or read the question needs is not supplied by the stated posits.

  No probability law, coupling or encoding is to be chosen to make the answer come out either way.
- *Authorization needed.* This is paper analysis of a native construction. The present authorization ("exact generic
  checks only"; "Not authorized: computation on an OI mechanism") does not cover it. Proposed, not activated.

***

## 8. §A.31 classification of this unit's findings

Productivity test: a finding counts only if it is stronger than a restatement and either constrains something or
exposes a hidden assumption. Labels are relative to a `git grep` of `papers/`, `book/` and `verification/` at
`fd539e15` for each finding's terms, extended in r2 to "herald", "steer", "self-dual", "no-restriction",
"block-positiv", "dual cone", "cube cone" and "carries the cone into itself". The r2 hits are: the DIM-1 kernel
lemma and its record (B3 of the review); "herald" as boundary-law and data-file bookkeeping (`oi-qm-ext-1/`,
`composition-access-20261024`, `native-y-continuation-20261024/…/herald.json`); "self-dual" for PSD and
foundations-probe cones (GR:196, `kinf2_foundations_probe.py`) and an SM citation. Re-checked in r3, "block-positiv" hits
`bridge-compatibility-audit/source-assessment.md:17-19` [W], which states Lemma H in operator form (block-positive ⇒
every local conditional PSD, by the identity that also gives the converse), and `kt4_prem1_indep_check.py` (partial
transposes as block-positive tables). None states the native form of Lemma H or sources joint-test validity
physically.

- **Lemma H (⇒): CONFIRMING** of the kernel's `lor_toOp_of_maxCone` (DIM-1), in the wing-exchanged orientation; the
  `h_a` orientation follows by transposition [A]. **(⇐): CONFIRMING** of `source-assessment.md:17-19` [W] and the
  standard fact that block positivity is positivity of every local conditional (L); not stated in the kernel module
  as one theorem.
- **Native form of Lemma H (dual of the native tests is the cube; native-body closure sufficient, not necessary for
  validity on native tests): ELABORATING.** It constrains Q-868-H: its two parts have different outcomes.
- **Native node-10 table (not quantum for every completion; in `maxCone` under the zero completion): ELABORATING.**
  QP states the ⟨YY⟩ mismatch. The completion-independence of non-quantumness and the completion-dependence of
  full-ball validity were not found stated.
- **K2-GUARD-1 ↔ C-CP: CONFIRMING,** with the literature (the transpose is positive, not completely positive; Peres
  1996, Horodecki 1996; L) and `mechanism-1-20261107/DESIGN.md:199`. Assumption-watch marker for #1169 Q-B and any NNB
  composite work: *a native one-copy determinant −1 operation, a quantum entangling gate and sequential composability
  cannot coexist with joint-test validity on `(x+, z+)`.*
- **J3 needs a non-monomial operation and a non-real operation under Main:564's rules: CONFIRMING.** The necessity
  rests on G7 and R6d (r3 W6) under Main:564. The label compares it against the sources of a non-real operation, the
  scope of independence and their context: Main:590, GR:250–260, `obligations_independent` (O1 versus O2 only),
  `gateFlow_isolation`, BRIDGE r4 §5.1 and the bridge r4 review's R4-B1/R4-B2.
- **Local tomography fails for the real analogue: CONFIRMING** (DIM-1 prereg:180; L).
- **Planning-record staleness of #868's body: not scientific;** recorded in §2.

No NEW finding is claimed.

## 9. Questions for the owner (neutral)

1. **Next unit.** Should Q-868-H (§7, parts V and C) be authorized as a paper unit under #868, given that it analyses a
   native construction (QP's U′ composite) and so falls outside "exact generic checks only"? Or should #868 remain
   blocked on J13, the pair update/preparer, as its current planning block states?
2. **D-02 (#914).** It is still listed as pending in the #914 comments read: Branch II as an independent root, or
   L ← O-OBSMU. Should #914 record, for O-K2(P)'s validity clause, that a sufficient route runs through the
   single-token body rows (O-GEO/#867 and the SA-1(c) hypothesis), while the clause itself stays a condition on the
   composite preparations' heralds, with J1/J2/J13 as the composite-specific P side? This would be a planning change
   only.

***

## 10. Answers in one place

- **Q1:** see §5. Validity is restated (Lemma H), not sourced, and is not quantumness. The missing inputs form a
  partial order: J13 → J1/J2 → J9–J12; J3 (a non-monomial and a non-real operation), J8, J6 and J7 do not depend on
  J13.
- **Q2:** see §6. #868 needs FI-1's content for J3 (with a non-real operation, of which O1 is one source) and on one
  route for J8, and is not reached by it. It shares M18 and R6.12 with #1210 as identical clauses, contains parts of M17 and of J9 (R6.11), is related to
  R6.9 one way, and implies M20 through J9.
- **Q3:** Q-868-H (§7), in two parts.

## 11. Verification scope

- **Probes (generic objects only; exact sympy; `python3 -I`; sympy 1.14.0):**
  - `probes/g868_generic_checks.py` (sha256 `292d16b0…ef335`), output `g868_generic_checks.out` (`e93f6541…83e3`): 18
    checks, 0 failures. G1 BP ⊋ PSD; G2 `cnot` exits SEP; G3 the K2-GUARD chain with a determinant-+1 control
    (conjugation by Z); G4 the node-10 table; G5 local tomography, complex vs real; G6 the CHSH operator identity on one
    instance; G7 monomial Kraus operators preserve diagonality, with a control.
    - Run 1 (`g868_generic_checks.run1-misspecified.out`, `d4521708…6a9f`) had 16 checks and failed G3b. The check
      compared `pairVal` with K2-GUARD-1's −1/2, which is the value of the product of sharp effects (`pairVal/4`), and
      its label "(probability −1/8)" was also wrong. The check was corrected to that normalization, matching the
      kernel statement's wording; it was not refit to an output. G7 (two checks) was added between run 1 and the
      recorded run.
  - `probes/r2_validity_scope.py` (r2; recorded at sha256 `60095dc0…0ea2`, kept at `r2/probes/`; in r3 only the V5
    docstring changed, to `cedf6112…7101`), output `r2_validity_scope.out` (`d86e03c1…f020`, byte-identical on re-run
    after that change): 6 checks, 0 failures. Imports no earlier probe. V1 and V3 are illustrations: V1 tests one cube
    vertex and one outside point, and V3 leaves the `a₁² + a₃² ≤ 1` step to a comment; r3 W1 and W3 check both
    claims in full. V2 witness w3; V4 the (1, 1, 1, 1/2) law (NS, max CHSH 5/2) and the PR box (S = 4); V5 ⟨Y⟩ = 0
    under real operations, y+ from S after H (S is one non-real operation, not the only one); V6 H⊗H real and
    non-monomial while `(I ± YY)/4` agree on every real product test. Run 1 (`r2_validity_scope.run1-float.out`,
    `a101caf5…`) failed V4 because its coefficients were Python numbers with the float `1/2` (Python 3's `/` is true
    division), and sympy 1.14 compares Rational and float as unequal under `==`; the coefficients were made exact. The
    run-1 source was not retained; the reviewer's reconstruction (REVIEW-868-r2 E1) and r3 W9 are consistent with this
    account, which states that no expectation was changed.
  - `probes/r3_scope_checks.py` (r3; sha256 `e6afb063…9575`), output `r3_scope_checks.out` (`394b6fd8…8ed9`): 27
    checks, 0 failures, exit 0. Imports no earlier probe. W1 the dual of the six Pauli sharp effects equals the cube
    cone (both inclusions; control outside); W2 octahedron in cube; W3 the node-10 table (herald identity, a
    sum-of-squares certificate for every full-ball product value, eigenvalue −1/4 on the singlet); W4 swap
    block-positive with real and imaginary parts explicit, eigenvalue −1; W5 the conditional-matrix identity for a
    generic complex 4×4 operator and the transposition symmetry of the product value; W6 operations that keep real
    states real keep ⟨Y⟩ = 0; W7 the kernel gate flow on `Fin 2` (re-typed from SecondOrderCircuit.lean:356):
    non-real, non-monomial, fixes the all-ones vector, commutes with X, z+ ↦ y−, with quarter-phase and real-H
    controls; W8 the driven transition `e^{−itX_ab}` (closed form checked against the matrix exponential) prepares
    `y+ ⊗ z+` and `x+ ⊗ z+` with no separate phase operation (the drive itself is complex); W10 the drive equals the
    layer flow times a relative phase on three states (the kernel's `gateFlow_isolation` specialised to one
    transposition on three states: trivial sign conjugation and `G(t)² = G(2t)`; reviewer K3, r3a check) and gives the quarter phase at a quarter turn with the exchange, with a real-rotation countercontrol; W9
    Python and sympy arithmetic (N6). Run 1 (`r3_scope_checks.run1.out`, `ec76650a…7223`, 24 checks) failed the W8
    control because sympy's `simplify` left `(-1)**(1/4)` forms unreduced in a correct identity; the comparison was
    given `expand_complex`, and no expected value changed. W10 (3 checks) was added after run 1, following the bridge
    r4 review's R4-B1, and the W7/W8 labels and docstring were reworded ("no separate phase gate"; the flow and the
    drive are themselves complex) without changing any check; the intermediate passing outputs were overwritten and
    are not retained.
  - `probes/r3a_check.py` (r3a; sha256 `5121c0f4…3f4b5`), output `r3a_check.out` (`6e16d0ea…a01d`): 16 checks,
    0 failures, exit 0. Imports no earlier probe. The drive's closed form solves its generator equation; n2: on three
    states with τ = (01) the sign conjugation of `gateFlow_isolation` is trivial, `G(t)² = G(2t)`, and the kernel's
    left side equals `e^{−iπtX_01}` and W10's right side at θ = πt, with a conjugate-phase control; n6: in W8's
    `x+ ⊗ z+` preparation the exchange after the drive at π/2 on (`|10⟩`, `|11⟩`) equals `S† ⊗ I` (and so as a
    channel on a generic Hermitian state), with `S ⊗ I` and drive-alone controls carrying exact nonzero witnesses.
  - The reviewer's `review/probes/rv_868_checks.py` (`b460abd4…70bc4`) was re-run here: exit 0, output byte-identical
    to `rv_868_checks.out` (27 checks, 0 failures). Checks R1–R6 are cited where named.
  - The r2 reviewer's `review/probes/rv2_868_checks.py` (`791556c5…7a6c`) and `probes/g868_generic_checks.py` were
    re-run for r3 (`rerun-r3/`): exit 0, outputs byte-identical to the recorded ones (26 and 18 checks, 0 failures).
    Checks D1–D2 are cited as "reviewer D1, D2".
  - No OI update rule, encoding, record law or mechanism is simulated or enumerated. The checks control statements in
    this file; they are not evidence for a physical result. Entries resting on them are computation-supported.
- **Read in full:**
  - Issue #868 and comments; #868's body obligation rows (r2, by REST, for the planning finding);
  - `pair-operation-source.md`, `composition-source-map.md`, `round-oi-pair-maxcone-1/result.md`,
    `round-comp-1-composite-interface/result.md`, `round-k2-guard-1-interface/result.md`,
    `bridge-compatibility-audit/source-assessment.md`;
  - `EqvK2MaxCone.lean` statements;
  - BRIDGE-UNIT1 r2 and REVIEW-UNIT1; BRIDGE r3 §0 item 8 and §5.1, and REVIEW-UNIT1-r2 RB1–RB3 (r2);
  - SHARED §§1–4, 8.3, 9 (r4, then the used rows in r5), QX-6 §§3–4 (r4; rows R6.5, R6.9, R6.11, R6.12 in r5), QX-4
    §§1–3 (r4; the r4→r5 diff read);
  - this unit's review in full (r2), and `review/REVIEW-868-r2.md` in full (r3);
  - BRIDGE r4 §0 item 8 and §5.1, and REVIEW-UNIT1-r3 and REVIEW-UNIT1-r4 verdicts and R4-B1/R4-B2 (r3).
- **Read in part:**
  - `prepared-pair-source.md` §§2–5;
  - `round-ktoken-maxcone-1/result.md` head;
  - `round-dim-1-dimension-selector/result.md:32, :101` and `preregistration.md:71-72, :147, :180` (r2);
  - `CompositeDimension.lean:1040-1052` (`lor_toOp_of_maxCone`) and the declarations of `lor_pair_bound` and
    `lor_of_forall_pair` (r2);
  - r3: `C5Discovery.lean:1-67` (`obligations_independent`); `LiftAudit.lean:40-130` (`gateFlow`,
    `LayerFlowExecutable`) and `:655-662` (`gateFlow_isolation`); `SecondOrderCircuit.lean:351-357` (`unit`);
    `RouteB.lean:126-139` (`PhasesAvailable`); `MinimalRepertoire.lean:1-12, :418-428` (`PhaseFreeRichness`);
    `ReachabilitySeam.lean:95` (`flow`); `LieRankSource.lean:199` (`transition`); declarations of
    `oiPlusMin_iff_qm`, `derivedOI_of_qm`, `onesTheory_layerFlowExecutable`, `onesTheory_not_phasesAvailable`;
    `EqvK2MaxCone.lean:150-215`;
  - `composition-access-20261024` REPORT head and README;
  - `physical-state-operation-compatibility/criteria.md` head;
  - `round-k1-sharp-tests-1/result.md`;
  - QP `DESIGN.md` §0, §1.4–1.5, :211, :558 (C-EAR), nodes 9–10 and the C-LEAK rows;
  - `mechanism-1-20261107/DESIGN.md:199` (r2);
  - apparatus-1 `DESIGN.md:1010-1023`; `NO-SIGNALLING.md:325-336`;
  - Main:218, :362, :403–416, :429, :564, :590, :652; GR:246–260 (r3); Substratum:131, :133, :467, :481;
  - #914 rows O-K2, O-DRV, O-GEO, O-4C and D-02.
- **Not read:** `two-system-interface.md` (separately unreviewed), MECH-2 beyond what BRIDGE and QX-6 quote, the
  remaining K-chain rounds, and the book. "None identified" entries are bounded by this list and by the `git grep`
  for `#868`, `joint-test`, `product-test positivity`, `O-K2`, `local tomography`, `herald`, `steer`, `self-dual`,
  `no-restriction`, `block-positiv` and `carries the cone into itself` across `papers/`, `book/` and `verification/`
  at `fd539e15`.
