# #868 re-assessment: joint-test validity and composition against the #1210/#1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Pending a fresh, independent review.**
Nothing here is adopted, promoted or proposed for the manuscripts. No premise is adopted. A review ACCEPT, if
reached, authorizes nothing further.

- **Accountable home:** #868. Parent programme #1169; status source #914 (row O-K2(P)).
- **Authorization:** owner (amaybaum), 2026-11-09, recorded in #1169 c.6740116927 (12:31:12Z) and #868
  c.6740118315. The option text reads: "**#1059/#1049/#868 audits** — One paper-only unit each, re-assessing its open
  question against today's #1210/#1211 findings (Born exponent; linear vs affine dynamics; joint-test validity), each
  with a fresh review. Exact generic checks only." The #868 record adds: "Not authorized: computation on an OI
  mechanism, new physical assumptions, freeze, dispatch, manuscript changes or merges."
- **What this unit did:** read Issue #868 and its comments, #914's body and comments (for O-K2 and D-02), the records
  below, and the two draft sets; wrote this file and one probe of exact checks on generic matrices (§11). No git,
  repository or GitHub write. No computation on any OI mechanism. Hand reasoning about stated OI constructions is
  marked [A] and rests only on what those records state.

***

## 0. Summary

**Q1. What is established, conditional or missing for the physical source of joint-test validity and composition.**

- *Established, as conditional mathematics.* The pair-cone theorems on `main` hold under explicit hypotheses:
  product inclusion, cone closure, product-test validity (maxCone), and invariance under `cnot` and the drive
  (`EqvK2MaxCone`, `KTokenMaxCone`, kernel). The composite interface laws hold without local tomography (COMP-1,
  kernel). A common positive-state / local-instrument representation would imply complete-history no-signalling and
  the 2√2 bound (T2 §6, model-reviewed W record). None of these sources a hypothesis.
- *Reduced here [A, both directions proved separately, §4.1].* On the bilinear carrier `W d`, product-test validity is
  equivalent to **heralding closure**: every remote herald by an effect on one wing leaves the other wing's
  unnormalized vector in the cone over its single-token body. Joint-test validity is therefore not an independent
  composite principle once a dictionary is fixed. Its content is a single-system property: the single-token body is
  closed under remote heralding, and its dictionary is sound on heralded preparations. Its OI status is the status of
  the single-token body. The only native body stated in the corpus is the SA-1(c)-restricted encoded carrier, and
  #1210's SHARED §9 marks SA-1(c) as QM-only.
- *Missing (first missing input per clause, §4).* The physical pair update and preparer (M18/R6.5). The pair's state/test
  dictionary and local tomography (Main:218, Main:652). Product inclusion at full-ball scope. Within Main:564's
  interface rules that needs a non-monomial operation, i.e. #1211's FI-1 (§4.4, G7). Availability of the non-Pauli
  sharp tests. An entangling operation acting as the table `cnot`. The drive.
- *Native evidence on composites (scoped).* The one native two-wing construction on `main` is QP node 10 (U′
  encoding, independent parities). By its reported correlators it gives a joint table that passes every Pauli product
  test and lies outside Q3 (G4) [A + X]. In that construction validity holds; quantumness fails at the gate, not at
  validity. K2-GUARD-1 (kernel) and QP's native one-copy reflection together make C-CP (or a composite-level
  restriction of the translation) necessary for any native route to the table `cnot` that also has the `(x+, z+)`
  preparation and Pauli product reads (§4.3) [A + X].

**Q2. Overlap.** #868's gap is **not** at #1211's earliest unsupported forward step FI-1, but **downstream of it**, with
a composite residue of its own:
- FI-1 is necessary for the coherent clauses of the K2 route: full-ball product inclusion and the drive.
- FI-1 is not sufficient: the dictionary and local tomography, the table `cnot` and heralding closure remain.
- #868 coincides with #1211's missing items "coherent composite kinematics" (Main:218) and "physical preparation
  mechanism".
- It coincides with #1210's composition gaps M17, M18, R6.9, R6.11 and R6.12, and is upstream of M20: J9 ⇒ NS and the
  2√2 bound; the converse fails.
- QX-4's "joint reads" and QX-7's "composition" are sequential, single-carrier objects (#913), not #868's.
- The Bell selection (H-Bell, M19) is separate. A6.1 makes #868's interface insufficient for |S| > 2 without a failure
  of (R). That failure must then be masked by the admissible cone of J9, which is R6.9.

**Q3. Smallest decisive next paper question (§7): Q-868-H, heralding closure on the native encoded body.** Does every
remote herald by a natively available read, on every native two-wing preparation built from product supplies and
available couplings, leave the other wing in the SA-1(c)-restricted encoded body with its dictionary sound? By §4.1
this decides joint-test validity for OI's only stated native body, independently of FI-1 and of the missing pair
source. It needs an authorization this unit does not have: paper analysis of a native construction.

***

## 1. Conventions

- **Status:** *proved* [layer], *disproved* [counterexample], *conditional* [named hypotheses], *open* [named gap].
- **Layers:** K kernel; P paper proof on `main`; W research record on `main`, model-reviewed (an author-posted or
  model acceptance is not verification, §A.46 item 7); D draft off `main` (today's #1210/#1211 files); A derivation in
  this file, unreviewed; X exact check on generic objects in this unit's probe (computation-supported only); L
  literature.
- **Ledger columns** (as #1210 SHARED §9 and #1211 §4): (i) mathematically well-defined; (ii) follows from
  independently justified OI principles; (iii) reproduces the QM prediction. **Column (iii) is never support for
  column (ii).** "None identified" in (ii) is open, scoped to the files read (§11).
- **Directionality (§A.34):** every equivalence below names a witness for each direction. An implication is stated
  as one.

## 2. Provenance

- **Corpus:** `git fetch origin main` → `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`
  (2026-11-09 08:36 +0200). Every `main` citation is at that commit. No `--depth`, `gc` or `prune`. Files were read with
  `git show` / `git cat-file`; the working tree's HEAD (`b1d782f9`) was restored after one detached checkout.
- **Boundary-mode pair-operation-source paper:** written on branch `research/oi-qm-ext-1-gate-a-20261106` at
  `e306143d23f534e7bbbb6e72444c026a0d55ad66` (blob `1e6ced538e13427fc6328582b01d9a8bb713ee59`). **It is now on
  `main`:** PR #1173 merged 2026-11-07T20:04:12Z (merge commit `dc0b333a1aaee5780d4f3dc514d92337c2c53307`).
  `e306143d` is an ancestor of `origin/main`. The file
  `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/pair-operation-source.md` at `fd539e15` has the same
  blob `1e6ced53…`. The branch is no longer on `origin`: `git ls-remote` returns no ref for it.
  - Review: #1173 c.6707141951 (2026-11-07T12:48:17Z), ACCEPT by `review_boundary_operation`, posted from the owner
    account. It is a model review, so the paper is a W record. The same holds for `prepared-pair-source.md` (blob
    `9123157c…`) and `composition-source-map.md`, also on `main`.
  - The original #868 planning note is still off `main`, at `0e0b3ddc` on `plan/joint-tests-source-20261013`. It is
    used only for the Issue's question text (provenance).
- **Draft inputs (D; hypotheses per §A.46 item 7), sha256 at the time read:**
  - `scratchpad/bridge/BRIDGE-UNIT1.md` r2, `3905569b…`. Its first review, `review/REVIEW-UNIT1.md`
    (`e242a794…`), is REVISE on r1; r2 awaits a fresh review.
  - `scratchpad/qphen/SHARED-MECHANISM.md` r5 (`a7206701…`, the live file changed during this unit; the rows used were
    re-read in r5), `QX6-BELL-CHSH.md` r5 (`9e9c0d02…`) and `QX4-INCOMPATIBILITY-LG.md` r5 (`7f4cd21d…`).
    `review/REVIEW-PHASE1-r4.md` (`755c3af0…`) is REVISE (narrow) on r4.
- **Planning record (§A.45 rule 1 finding, not a scientific one).** #868's body still describes #1173 as
  "draft/unmerged" and links the deleted branch. The source governs: the paper is on `main`. Correcting this is
  ordinary planning maintenance under §A.45 rule 3, outside this unit's write scope.

***

## 3. What #868 asks, traced to the statements that consume it

The Issue's research question is: "What physical source supplies the joint state/test pairing, validity of the required
product tests and the locally tomographic composition interface?" The clauses it names are hypotheses of these
statements:

| statement | hypotheses (as stated) | layer |
| --- | --- | --- |
| `pairCone_eq_Q3_of_drive_maxCone`, `pairCone_eq_Q3_of_sharp_available` (`OIBridge/EqvK2MaxCone.lean:153-212`); k-token forms (`KTokenMaxCone`) | `hH1` every product of `eball 3` states in `K`; `hadd`, `hsmul` cone closure; `hmax` `K ⊆ maxCone (eball 3)`, or `hvalid` + `hsharp` (validity on an available family containing the sharp tests); `hH2` `cnot` invariance; `hA` rotation/cyclic invariance | K, conditional |
| `pairCone_eq_Q3_iff_drive_maxCone` | equality ⟺ (`hH2` ∧ `hA`), **relative to fixed** `hH1`, `hadd`, `hsmul`, `hmax`. Witnesses: `driveInvariant_of_eq_Q3` (⇒), `pairCone_eq_Q3_of_drive_maxCone` (⇐) | K |
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

### 4.1 Lemma H: product-test validity is heralding closure [A]

*Setting.* Use `W d` and `eball d` as in the kernel. An effect on `eball d` is an affine `e(x) = c + u·x` with values
in `[0,1]` on the ball. So `c ≥ |u|`, and `e = c · (1, u/c)·(1, x)` with `|u/c| ≤ 1`, or `e = 0`. Hence
`maxCone (eball d) = {ω : ahatᵀ ω bhat ≥ 0 for all a, b ∈ eball d}`, with `ahat = (1, a)`. For `a ∈ eball d`, write the
**heralded B-vector** `h_a(ω) = ahatᵀ ω = (t, v) ∈ ℝ × ℝ^d`. Let `Cone_d = {(t, v) : |v| ≤ t}` be the cone over the body.

*Statement.* `ω ∈ maxCone (eball d)` ⟺ `h_a(ω) ∈ Cone_d` for every `a ∈ eball d`. The same holds with the wings
exchanged.

- *(⇐)* For `b ∈ eball d`, `ahatᵀ ω bhat = t + v·b ≥ t − |v||b| ≥ 0`.
- *(⇒)* If `|v| > t` for some `a`, then `b = −v/|v| ∈ eball d` gives `t − |v| < 0`. If `v = 0`, any `b` gives
  `t ≥ 0`.

The same proof holds for an available family: `maxConeOf avail` ⟺ heralds by available A-effects land in the cone
of B-vectors on which every available B-effect is nonnegative. The bridge audit's "LC" remark
(`bridge-compatibility-audit/source-assessment.md`) is the (⇒) direction for PSD-type data. The reduction is
ELABORATING (§8).

*Reading.* If the joint statistics of executed product tests are physical probabilities, they are nonnegative
automatically. What `hvalid` adds is twofold:
- *availability:* the effects quantified over are physically available (`hsharp`);
- *soundness:* the table assigned by the dictionary equals the physical joint statistics.

Given no-signalling, soundness on product tests is soundness of the single-wing dictionary on the remotely heralded
conditional preparations. So **#868's "validity of the required product tests" decomposes into:**
- (a) test availability, a single-system clause (O-GEO/#867; QX-4 R4.5);
- (b) closure of the single-token body under remote heralding, with the dictionary sound there;
- (c) complete-history NS.

This answers the Issue's third checklist item ("separate sufficient test availability from soundness on joint
preparations"): soundness is (b) + (c); availability is (a).

### 4.2 The ledger

| ID | restriction (source) | (i) well-defined? | (ii) from independently justified OI principles? | (iii) reproduces QM? | status; where the gap sits |
| --- | --- | --- | --- | --- | --- |
| J1 | **Pair state/test dictionary:** fixed linear `D` from physical joint boundary laws on an admissible cone into `W 3` (or COMP-1 product data), not refit per setting (T2 §6; composition-access (1); `EqvK2MaxCone` header) | yes, relative to a specified realization and cone | **none identified.** No pair realization is specified (prepared-pair-source §2; pair-operation-source §§2, 7) | yes: Pauli tables of `Herm(4)` | open; first missing input is the pair realization (J13) |
| J2 | **Local tomography:** states determined by product-test tables (COMP-1 `lt`; encoded by `W d`) | yes | **none identified.** COMP-1 sources none; Main:218, :652: kinematic locality does not prove it | complex QM yes; **real QM no** (G5: 9 < 10; `(I ± εY⊗Y)/4` agree on every real product test) | premise field; open. Tied to the token's complex structure (§4.4) |
| J3 | **Product inclusion** `hH1` at `eball 3` scope | yes | partial. A product law for independent supplies on disjoint cells follows from N2's product counting measure via H-PREP (both posits, SHARED §9). At full-ball scope it needs coherent single-token preparations: under Main:564's preparation rules (uniformly mixed ancilla, then available operations), monomial Kraus operators keep every prepared state diagonal (G7) [A + X], so a non-monomial operation (FI-1) or a coherent preparation source is necessary. Natively, at most the stabilizer octahedron, under SA-1/H-PREP | yes | conditional at stabilizer scope (posits); open at full-ball scope, downstream of FI-1 |
| J4 | **Cone closure** `hadd`, `hsmul` | yes | conditional yes. Sums and nonnegative multiples of unnormalized measures are measures. Mixing preparations needs a randomizer independent of the residual boundary (composition-access REPORT, randomized controllers) | yes | least problematic; conditional on the randomizer clause |
| J5 | **Product-test validity** `hvalid`/`hmax` (joint-test validity) | yes | **reduced, not supplied.** By Lemma H it equals heralding closure of each single-token body with a sound dictionary, given J1, plus test availability (J6) and NS (J10). The native body is SA-1(c)-restricted. SA-1(c) is "QM-only: a hypothesis under test" in SHARED §9 [D], so J5 on the native body inherits that status | yes, but non-selective. BP ⊋ PSD: swap is block-positive with eigenvalue −1 (G1). The QP node-10 table is Pauli-valid and outside Q3 (G4) | open; locus = single-token body closure under heralding (§7) |
| J6 | **Sharp-test availability** `hsharp` (all sharp effects of `eball 3`) | yes | open. Non-Pauli reads are not native (QX-4 R4.5 [D]; O-GEO #867). K1-SHARP-TESTS-1 classifies `2 ≤ d` as two sharp tests and does not source them | yes | open; single-system (#867) |
| J7 | **Entangling preserving operation** `hH2` (invariance under the table `cnot`) | yes | **none identified;** native evidence is negative in its scopes. M2D Theorem U2 [W]: no encoded entangling unitary under R1^⊗n and H-LIFT at `q = 2`. QP node 10 [W]: the native graded coupling acts as CNOT on encoded functionals, but its reported output has ⟨YY⟩ = 0, not −1 (G4c). K2-GUARD-1 [K] with QP's native translation reflection gives §4.3 | yes (Q3 is `cnot`-invariant; the iff above, relative to fixed hypotheses) | open. With `hA`, this is where the K2 route selects Q3 |
| J8 | **Drive invariance** `hA` | yes | open (O-DRV, #865). Continuous rotations are non-monomial, so FI-1 is necessary | yes | open; downstream of FI-1 |
| J9 | **Composition across uses:** T2 (1) at two uses, reuse closure, post-measurement update (R6.11) | yes, for a specified realization | **none identified;** needs J1 and J13 | yes | open. (1) ⇒ complete-history NS and \|S\| ≤ 2√2 (T2 §6 [W]; operator identity instance G6). Converse fails: the PR box is NS (T2 §5.2) |
| J10 | **Complete-history NS** (R6.8, M20) | yes | not derived: "a requirement of the framework's chosen branch" (SHARED §9 [D]; Main:414, :429). Conditionally implied by J9 | yes | requirement; open |
| J11 | **Tsirelson soundness** (R6.10, M20) | yes | none independent of QM. **Conditionally implied by J9**, which is itself unsourced, so the gap is relocated, not closed. SHARED §9 lists "none identified" without this conditional route | yes (L) | QM-only as an independent restriction; downstream of #868 on the QX-6 route |
| J12 | **Admissible preparation cone `C_i`** / restricted preparation class (R6.9) | yes, for a fixed realization | none. A class fixed only by the balance equations is fitted (SHARED §9; prepared-pair-source §§4–5 [W]) | NS by definition; 2√2 does not follow | open. Under J9, `C_i` (the cone on which `D_i` is positive) is this same object |
| J13 | **Pair update / preparer / source** (M18, R6.5) | as a requirement | **none:** the first source stop (prepared-pair-source §2; pair-operation-source §§2, 7; boundary-mode proposal supplies neither update/preparer nor an interface change) | n/a | missing; earliest #868-specific input |
| J14 | **Bell design and selection:** (L′), (R), MI; cross-wing response H-Bell (M19) | yes | (L′), (R): protocol, not OI (SHARED §9 [D]). MI: posit (Main:406). H-Bell: none; the branch is a selection (E + St; #1211 F2 [D]; Main:403–406) | (L′) + (R) + MI give \|S\| ≤ 2 (A6.1, model-reviewed D derivation) | separate obligation (#1060/#914 row 16). Constrains #868: see §6 |

### 4.3 Native composite evidence and the C-CP link [A + X]

1. **QP node 10's composite** (QP `DESIGN.md:746-768`, on `main`, W).
   - QP states: the determined functionals are `f_x^A + f_x^B` and `f_z^A + f_z^B`; with independent uniform parities,
     ⟨XX⟩ = ⟨ZZ⟩ = 1 and ⟨YY⟩ = 0.
   - Reading the other cross terms under QP's N2 rule ("unknown slots uniform"): any functional not in the span of
     the determined ones has mean 0. The table is then `T = (I + X⊗X + Z⊗Z)/4`. This reading is [A] from QP's stated
     rules, not a run of the construction.
   - G4 (exact, generic): `pairVal = 1 + a₁b₁ + a₃b₃ ≥ 0` on the unit balls, so `T ∈ maxCone`. `T` has eigenvalue −1/4,
     so `T ∉ Q3`. All 36 signed Pauli product values are ≥ 0. `T` is invariant under one-copy `Y ↦ −Y`.
   - So in the native construction, validity holds and the cone is not Q3. The quantum `cnot` image of `(x+, z+)` has
     ⟨YY⟩ = −1 (G4c). The native gate does not act as the table `cnot` on that input.
2. **K2-GUARD-1 meets QP's C-CP.**
   - QP introduces C-CP ("no available encoded map has an orientation-reversing (determinant −1) action on the Bloch
     octahedron", QP `DESIGN.md:211`). Its stated reason is progress toward the quantum comparator, which is a
     column-(iii) reason.
   - QP node 9 shows that a constant translation in U′ acts as `Y ↦ −Y`, natively in N via P2 and H-PREP (QP
     `DESIGN.md:727-731`).
   - K2-GUARD-1's chain uses only stabilizer data: the product `(x+, z+)`, `cnot`, one-copy `reflY`, `cnot`, and the
     product of sharp effects along −e₁ and −e₃. It gives −1/2 (G3b reproduces −1/2, i.e. `pairVal = −2`). The
     determinant-+1 control stays valid (G3c).
   - *Consequence [A].* Consider any native composite in which:
     - a preparation of `(x+, z+)` is available;
     - Pauli product reads are available;
     - the translation acts on joint tables as `reflY`;
     - some available operation acts on joint tables as the quantum `cnot`.

     Then that sequence assigns probability −1/2 to a product read. So J5 (with J1) fails, and one of the four must
     go. A native route to Q3 composites (J7 in table form) therefore needs C-CP, or a restriction of the translation
     at composite level.
   - *Column (ii).* This gives C-CP a **consistency** reason (type C): it is necessary for J5 and J7 together. It is
     not an independent OI reason, because J7's target is the quantum `cnot`. QP does not cite K2-GUARD-1, and K2-GUARD-1
     does not cite QP; the link is ELABORATING (§8).
   - *Skepticism, since the reading of item 1 favours the framework.* Validity holding natively is cheap: executed
     Pauli reads have nonnegative probabilities by construction. The informative facts are that the table is outside
     Q3 and that the native gate is not the table `cnot`. Validity for non-Pauli tests is not claimed: those tests
     are not native (J6).

### 4.4 Cross-links found while tracing [A + X]

- **FI-1 is necessary for J3 and J8 [A + G7].**
  - Main:564's rules supply preparations only as a uniformly mixed ancilla, then available operations; readout is
    configuration-basis Lüders.
  - If every available Kraus operator is monomial (permutation × diagonal, phases included), every reachable state is
    diagonal (G7a). A coherent product such as `x+ ⊗ z+` then needs a non-monomial operation, which is FI-1, or a
    preparation channel outside those rules.
  - Scope: this necessity holds for that interface only. It does not exclude a coherent preparation source outside
    it.
  - `cnot` itself is a permutation. J7's difficulty is not monomiality but what the gate does to coherent joint inputs.
- **J2 and the token's complex structure.**
  - Local tomography holds for complex and fails for real two-level composites (G5). The real-carrier analogue of the
    token loses J2. This is the rebit fact (Hardy–Wootters; L, not read first-hand here), CONFIRMING DIM-1's note that
    `W d` encodes local tomography.
  - Relevance to #1211: its F4/NQ1 (complex structure on the six-link carrier) and #868's J2 meet at one question:
    where a complex, not real, single-token kinematics comes from. That is O-GEO/#867 for the token. No identification
    of the two carriers is claimed.

***

## 5. Answer to Q1: established, conditional, missing

- **Established (K/P, conditional mathematics only):**
  - the K2 pair-cone theorems and their relative iff (witnesses named, §3);
  - COMP-1's laws without `lt`;
  - K2-GUARD-1's orientation obstruction;
  - Main's graph-cone separation (Main:652);
  - Main's Bell ceiling under its hypotheses (Main:366–416).
- **Conditional (W/D/A):**
  - T2 (1) ⇒ NS and 2√2 (W);
  - A6.1 under (L′), (R), MI (D, reviewed);
  - Lemma H (A);
  - J3 at stabilizer scope under N2, H-PREP and SA-1 (posits);
  - J4 under the randomizer clause;
  - the native node-10 table placement (A from QP's reported values, X for the matrix facts).
- **Missing, by first missing input:**
  - J13, the pair realization: first, and #868-specific;
  - J1 and J2, the dictionary and local tomography: need J13;
  - J3 at full-ball scope and J8, the drive: need FI-1 or a coherent preparation source;
  - J6, non-Pauli test availability: single-system (#867);
  - J5, validity: reduces to heralding closure of the single-token body, which inherits SA-1(c)'s QM-only status;
  - J7, the table `cnot`: native evidence negative in its scopes; tied to C-CP by §4.3;
  - J9 through J12: downstream of J1 and J13.
- **Column discipline.** Every row's column (iii) is "yes" for QM. For J2 (real QM fails), J5 (non-quantum cones pass)
  and J9 (the PR box is NS) it is also non-selective. No row's (ii) is answered from (iii).

## 6. Answer to Q2: where #868's gap sits relative to #1211 and #1210

| today's finding (D) | relation to #868 | direction |
| --- | --- | --- |
| #1211 FI-1, the earliest unsupported forward step (BRIDGE §5.1) | **upstream** of J3 (full ball) and J8; **not** upstream of J1, J2, J5 or J13. pair-operation-source §5 already applies the same configuration-level and positive-compression ceilings to the pair route, so #868's "additional interface gap" is FI-1's bipartite instance for operations | FI-1 necessary (§4.4), not sufficient |
| #1211 "coherent composite kinematics open (Main:218)" | same object as J1 + J2 (O-K2(P)) | identical anchor |
| #1211 "physical preparation mechanism missing" | J13's preparer and J3's coherent preparations | same gap, bipartite form |
| #1211 F2: the Bell branch is a selection (H-Bell) | J14; separate from #868 | — |
| #1211: site factorization is an input (SM §2.4) | presupposed by J1/J2: the wing split is the site split | upstream input, not discharged by #868 |
| #1210 A6.1 conditional on (L′), (R) | J1–J12 with (L′), (R), MI give \|S\| ≤ 2. #868's interface is not sufficient for Bell violation without a failure of (R), i.e. M19 | #868 ⇏ Bell |
| #1210 QX-6 M17, R6.12 (local tomography a hypothesis), R6.3 | = J2 and part of J1 | identical |
| #1210 M18 / R6.5 (pair source absent) | = J13 | identical |
| #1210 R6.9 (restricted preparation class) | = J12, the admissible cone of J9. On the H-Bell route, J9's fixed split needs the cross-wing response masked on `C_i` (T2 §6: a mediator across the split "cannot simply be discarded") | same object |
| #1210 R6.11 (post-measurement update / reuse) | part of J9 | identical |
| #1210 M20 (NS; Tsirelson, QM-only) | downstream: J9 ⇒ both (T2 §6). SHARED §9's "none identified" for Tsirelson omits this conditional route; it relocates (ii) to #868 without supplying it | J9 ⇒ M20; not ⇐ |
| #1210 QX-4 "joint reads" | sequential joint laws and joint measurability on one carrier. A different object (#913's reusable instrument composition); not #868 | no overlap |
| #1210 QX-7 "composition" (M12, M13) | repeated sequential composition of a fixed operation; not tensor composition (NR-11 is optional) | no overlap |
| #1210 M3 (SA-1(c), QM-only) | J5's native status by Lemma H | shared (ii)-gap |

**Verdict.**
- #868's gap is a **different place** from #1211's earliest step. It is downstream of FI-1 and partly fed by it, with a
  composite residue (J1, J2, J5, J7, J13) that FI-1 does not reach.
- It **coincides** with #1210's composition gaps M17, M18, R6.9, R6.11 and R6.12, and lies upstream of M20.
- Its title clause, joint-test validity, reduces to the single-token body's heralding closure, which shares #1210's
  M3 gap.

## 7. Answer to Q3: the smallest decisive next paper question

**Q-868-H (heralding closure on the native encoded body).**
- *Question.* Take the native single-token body as stated in the corpus: apparatus-1's SA-1-restricted encoded
  carrier, in QP's U′ encoding, with P1–P3, E-iso, H-PREP and N2 carried as stated posits. Take every two-wing
  preparation built from product supplies and the couplings P3 may arm between the wings' carrier cells (graded, as
  in QP node 10). Does every remote herald by a natively available read on one wing leave the other wing in a state of
  that body (Lemma Q's protected parity undetermined, SA-1(c) intact), with the single-wing dictionary sound on it?
- *Why it is decisive.* By Lemma H (both directions), the answer is J5 for OI's only stated native body.
  - If yes: native joint-test validity holds at stabilizer scope. #868's residue is then exactly J1/J2 (pair
    realization, LT), J7 (the table `cnot`, tied to C-CP by §4.3), and the FI-1-dependent J3 and J8.
  - If no (a herald exposes or biases the protected parity: QP's C-LEAK across wings): the native composite is not a
    composite of the native single-token theory. J5 then fails natively at a named clause, independently of FI-1 and
    of the missing pair source.
- *Why it is small.* It needs no pair source, no separation and no Bell table. It uses only couplings and reads the
  corpus already states. Lemma H is already proved here. QP's C-LEAK rows (`DESIGN.md:555-557`) settle the
  within-wing and shared-parity cases. What remains is the two-wing graded-coupling case.
- *Decision rule (fixed before any work).*
  - Pass: closure holds for every available read on every such preparation, with every posit carried into the
    conclusion.
  - Fail: one explicit herald leaves the body, with its membership line.
  - Stop: a preparation or read the question needs is not supplied by the stated posits.

  No probability law, coupling or encoding is to be chosen to make the answer come out either way.
- *Authorization needed.* This is paper analysis of a native construction. The present authorization ("exact generic
  checks only"; "Not authorized: computation on an OI mechanism") does not cover it. Proposed, not activated.

***

## 8. §A.31 classification of this unit's findings

Productivity test: a finding counts only if it is stronger than a restatement and either constrains something or
exposes a hidden assumption. Labels are relative to a `git grep` of `papers/`, `book/` and `verification/` at
`fd539e15` for each finding's terms.

- **Lemma H (validity ⟺ heralding closure): ELABORATING.** The (⇒) direction for PSD-type data is the bridge audit's
  LC remark. Both directions, and the decomposition of #868's validity clause into availability, single-body closure
  and NS, were not found stated. It constrains: J5 cannot be sourced as a separate composite principle once J1 is
  fixed.
- **Native node-10 table placement (in maxCone, outside Q3): ELABORATING.** QP states the ⟨YY⟩ mismatch. The
  maxCone/Q3 placement and "validity holds, the gate fails" were not found stated.
- **K2-GUARD-1 ↔ C-CP: ELABORATING.** It exposes an assumption: QP motivates C-CP by the comparator. The kernel gives
  a consistency reason, conditional on the table `cnot`. Assumption-watch marker for #1169 Q-B and any NNB composite
  work: *a native one-copy determinant −1 operation and a quantum entangling gate cannot coexist with joint-test
  validity on `(x+, z+)`.*
- **J9 ⇒ M20 omitted from SHARED §9's Tsirelson row: ELABORATING** (cross-propagation between a W record and a D
  draft).
- **FI-1 necessary for J3/J8 under Main:564's rules: CONFIRMING.** It follows from Main:564 and BRIDGE §6's
  "coherent state composition" row.
- **Local tomography fails for the real analogue: CONFIRMING** (DIM-1 prereg:180; L).
- **Planning-record staleness of #868's body: not scientific;** recorded in §2.

No NEW finding is claimed.

## 9. Questions for the owner (neutral)

1. **Next unit.** Should Q-868-H (§7) be authorized as a paper unit under #868, given that it analyses a native
   construction (QP's U′ composite) and so falls outside "exact generic checks only"? Or should #868 remain blocked on
   J13, the pair update/preparer, as its current planning block states?
2. **D-02 (#914).** It is still listed as pending in the #914 comments read: Branch II as an independent root, or
   L ← O-OBSMU. This unit finds that O-K2(P)'s validity clause reduces to a single-token body property (Lemma H). Should
   #914 record O-K2(P)'s validity clause as L-dependent on the single-token body rows (O-GEO/#867 and the SA-1(c)
   hypothesis), keeping J1/J2/J13 as the composite-specific P side? This would be a planning change only.

***

## 10. Answers in one place

- **Q1:** see §5. Validity is reduced (Lemma H), not sourced. The missing inputs, in order, are J13, J1/J2,
  FI-1-dependent J3/J8, J6 and J7.
- **Q2:** see §6. #868's gap is a different place from FI-1, downstream of it. It is identical to #1210's
  M17/M18/R6.9/R6.11/R6.12 and upstream of M20.
- **Q3:** Q-868-H (§7).

## 11. Verification scope

- **Probe:** `scratchpad/reassess/868/probes/g868_generic_checks.py` (sha256 `292d16b0…ef335`), output
  `g868_generic_checks.out` (`e93f6541…3e3`), run with `python3 -I`, sympy 1.14.0: 18 checks, 0 failures.
  - It covers exact sympy on generic two-qubit / two-rebit matrices only: G1 BP ⊋ PSD; G2 `cnot` exits SEP; G3 the
    K2-GUARD chain with its determinant-+1 control; G4 the node-10 table; G5 local tomography, complex vs real; G6 the
    CHSH operator identity on one instance; G7 monomial Kraus operators preserve diagonality, with a control.
  - No OI update rule, encoding, record law or mechanism is simulated or enumerated. The checks control statements
    in this file; they are not evidence for a physical result.
  - Run 1 (`g868_generic_checks.run1-misspecified.out`, `d4521708…`) failed G3b. The check compared `pairVal` with
    K2-GUARD-1's −1/2, which is the value of the product of sharp effects (`pairVal/4`). The check was corrected to
    that normalization, matching the kernel statement's wording. It was not refit to an output.
  - The probe is not independently reproduced. Entries resting on it are computation-supported.
- **Read in full:**
  - Issue #868 and comments;
  - `pair-operation-source.md`, `composition-source-map.md`, `round-oi-pair-maxcone-1/result.md`,
    `round-comp-1-composite-interface/result.md`, `round-k2-guard-1-interface/result.md`,
    `bridge-compatibility-audit/source-assessment.md`;
  - `EqvK2MaxCone.lean` statements;
  - BRIDGE-UNIT1 r2 and REVIEW-UNIT1;
  - SHARED §§1–4, 8.3, 9 (r4, then the used rows in r5), QX-6 §§3–4 (r4), QX-4 §§1–3 (r4; the r4→r5 diff read).
- **Read in part:**
  - `prepared-pair-source.md` §§2–5;
  - `round-ktoken-maxcone-1/result.md` head;
  - `composition-access-20261024` REPORT head and README;
  - `physical-state-operation-compatibility/criteria.md` head;
  - `round-k1-sharp-tests-1/result.md`;
  - QP `DESIGN.md` §0, §1.4–1.5, nodes 9–10 and the C-LEAK rows;
  - apparatus-1 `DESIGN.md:1010-1023`; `NO-SIGNALLING.md:325-336`;
  - Main:218, :362, :403–416, :429, :564, :652; Substratum:131, :133, :467, :481;
  - #914 rows O-K2, O-DRV, O-GEO, O-4C and D-02.
- **Not read:** `two-system-interface.md` (separately unreviewed), MECH-2 beyond what BRIDGE and QX-6 quote, the
  remaining K-chain rounds, and the book. "None identified" entries are bounded by this list and by the `git grep`
  for `#868`, `joint-test`, `product-test positivity`, `O-K2` and `local tomography` across `papers/` and
  `verification/` at `fd539e15`.
