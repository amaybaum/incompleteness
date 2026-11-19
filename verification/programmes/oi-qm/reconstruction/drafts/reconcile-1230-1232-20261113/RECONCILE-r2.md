# #1230 / #1232 reconcile: INTERVENE-1 and SUBSTATE-BRIDGE-1 against the current corpus

**Standing.** This is a read-only review and reconciliation. It makes no new derivation and no
computation on any OI rule. Individual steps were hand-checked only where noted. Nothing was
committed, pushed, posted or dispatched. It is a working record, not yet on any branch; the ChatGPT review that c.6854241002 requires at an exact head needs it pushed to a branch other than #1230's or #1232's (§A.43 item 2). It is a
model-written review, so it is not verification (§A.46 item 7).

**Authority.** #1169 c.6854241002 (account `amaybaum`, 2026-11-13T13:24:47Z). The comment records
the owner's selection in the coordinating session: "TUNE-1 sourcing unit, REC-1 P0 (supporting),
#1230/#1232 reconcile". Item 3 reads: "A read-only review and reconciliation of the existing
INTERVENE-1 and SUBSTATE-BRIDGE paper drafts. No new derivations. No writes to those PRs' branches."

## 0. Objects and pins

| Draft | PR (state) | Branch @ head | Files read | Reviews at the head |
|---|---|---|---|---|
| INTERVENE-1 unit 1 r2 | #1230 (open, WIP, "not for merge") | `research/intervene-1-20261111` @ `ea12fde1bbc4b546f4690bf89817971796aeb501` (parent `592fede0`, base `cac5d264`) | `verification/programmes/oi-qm/reconstruction/drafts/intervene-1-20261111/{INTERVENE-UNIT1.md, DISPOSITIONS-r2.md, checks.py, checks.out}` | 5857231398 (r1 `592fede0`, REVISE). 5857985732 (r2 `ea12fde1`, **ACCEPT WITH DOCUMENTATION NITS**, conditional paper result). Both are ChatGPT reviews posted under the owner's account. |
| SUBSTATE-BRIDGE-1 unit 1 r2 | #1232 (open, WIP, "not for merge") | `research/substate-bridge-1-20261111` @ `86a413c88cd14d344aa41b6f47885aeb24da6910` (parent `b94b283a`, base `cac5d264`) | `.../drafts/substate-bridge-1-20261111/{SUBSTATE-BRIDGE-UNIT1.md, DISPOSITIONS-r2.md, probes/generic_substate_checks.{py,out}}` | 5858000929 (r1 `b94b283a`, REVISE). 5859960068 (r2 `86a413c8`, **ACCEPT WITH NITS**; "OI-wide verdict remains INDETERMINATE"; "cannot be used as a positive result for TUNE-1"). |

The reconciliation corpus:
- `main` @ `c3b5f37a`: Main, OA-1 r5, OA-2 r4, OA-3 r4, TUNE-1 Step 1 and Step 2 (S3, S4, P), and the Lean modules (statements read).
- REC-1 r7: `research/rec-1-1169-20261113` @ `9f7d2612`, `REC-1-r7.md` (47 rows, C1–C18, OBL-SP with H-xiv).
- TUNE-1 Step 3A r3: `8228b3c2`.
- Q-868-H r3: `research/q868h-868-20261113` @ `ffc9cda4` (read at `acf28d3a`; the two later commits change the header status, a probe-repeat note and hashes, not (V)).

Both drafts pin `main` at `cac5d264`, an ancestor of `c3b5f37a`. Several facts on `main` changed after the drafts were written. They are listed in §3.

The Lean anchors were re-read at `c3b5f37a`: `PreservesDiag` (DiagonalTheory:68), `preservesDiag_add` (:77), `IsMonomial` (SubstratumInterface:75), `preservesDiag_conj_of_monomial` (:126), `InstAvail` (ImplementationLocality:268), `Realized` (:250), `Architecture` (:506), `genTheory` (:852), `substratumTheory = genTheory substratumClass` (RouteB:282–285), `avail_of_availExt_one` (LevelOneSeam:107, a theorem), `SystemToLevelOne` (LevelOneSeam:117, a `def … : Prop`; INTERVENE cites :116), `discardWith_uniform_conjChannel` (AncillaClosure:461), `exists_nonMonomial_of_layerFlowExecutable` (ExecSource:52) and `project_waveStep` (NativePadicReduction:56). All exist as cited. Between `cac5d264` and `c3b5f37a` only `OIRealization.lean` changed under OIBridge.

## 1. Per-result table

Codes used in the table:
- **Layer:** [A] paper argument in the draft, unreviewed except by the PR reviews; [X] the draft's generic exact checks; [K] kernel; [P] manuscript; [R] research record on `main`; [R-off] research record off `main`.
- **Q2** follows REC-1 §1. A = definable or representable. F = reachable under one fixed dynamics. P = physically derived. "UB" = an upper bound on what is reachable, with no operation exhibited.
- **Recon** (reconciliation): **C** consistent, **Dup** duplicated (with the citation), **X** conflict, **+** supplies something the others lack.

### 1a. INTERVENE-1 r2 (#1230 @ `ea12fde1`)

| ID | Claim (draft's wording, condensed) | Status / proof | Review: supported at stated scope? | Reconciliation | Q2 |
|---|---|---|---|---|---|
| T0 | Under P-CONF (H1–H3), H4 and H-IND, every procedure induces a family in 𝒦: nonnegative branches whose sum is column-stochastic. | [A] §1.3, a pushforward of μ⊗κ. X7 is a countercontrol. | **Yes, with one gap.** The column-sum identity assumes the procedure terminates. Review nit 1 on 5857985732 is still unapplied in r2. SUBSTATE E1 repairs this with a ⊥ outcome. Nonnegativity is unaffected. **Hand-check:** the outcome may be any function of the trajectory, so T0 holds under REC-1's open typing choices C5, C6 and C7 alike. | **Dup:** OA-2 Lemma 0 and N0 (REC-1 row 18), where the "fixed lift" is H-IND's role; F2-1 A★2 (operator form, frozen on `main`); MECH-2 Lemma F's proof (row 40). **+** Adaptive record-dependent stopping, made explicit, and the H-IND/C-dyn split as one named hypothesis. OA-2 N1 (without H-LIFT) is the same split. | UB |
| T1 | 𝒩 ⊆ 𝒦. | [A], with an instance check in X5. | Yes. | **Dup:** OA-2 Lemma 0; MECH-2 Lemma F's premise; kernel nonnegativity (`nonnegClass_nonnegBounded`). | UB |
| T2 / NX-1(C) | Every ℂ-linear lift of a real-linear map on laws preserves diagonals. Hence NX-1 fails on route C, "case (i)", given P-CONF, H4 and H-IND. | [A], three lines. | **Correct, but nearly definitional.** It uses only linearity and the fact that native states are diagonal. The force of the verdict lies in route C's identification (H3 plus "states = diagonal matrices"), not in T0. **Label flag:** "case (i), access-model-independent" holds only inside route C and under H-IND (review gloss, nit 4). In REC-1's vocabulary the state-space premise (laws on configurations, route C's identification) is **Q1-I**, as REC-1 classes the same kind of result: row 9 (OA-1 configuration ceiling) and row 18 (OA-2 N0, "state-space choice"), both Q1-I. Typing H-IND (a fixed outside kernel) as Q1-I/Q1-μ is this reconcile's reading; REC-1 has no row for it. P-CONF's H1–H2 are Q1-D (ledger (ii)). | **Dup:** OA-2 N0 verdict "NO for this class" (row 18), at the same scope up to adaptive stopping and an s-correlated κ. **C, narrower (access-specific, case (ii)):** OA-1 row 9 [K] ("an escape must change what an observer operation acts on", OA1:420–421) and Main:588 (no state-mixing operation under finite bijective read-write dynamics); Main:718 (diagonal inputs). **X (labelling only):** "case (i)" vs Q1-I. There is no mathematical conflict. | UB |
| T3 / NX-1(E_f) | With L linear, injective and **spanning**, and with H-LIFT, every induced encoded map has a nonnegative frame matrix. Hence NX-1 fails on E_f. | [A]. X5 is the control (Hadamard minimum −1/2). | **T3 itself: yes.** **Boundary flag:** the §0 table row E_f, the §0 lemma summary, the prose after T3 ("any linear injective frame") and the §3 table row "faithful (E_f, H-LIFT, linear injective L) ⇒ ¬NX-1(E_f)" all drop "spanning" (review nit 3 names the post-T3 prose; unapplied). Without spanning the frame matrix is not unique, so the E_f class ("the maps with an entrywise nonnegative frame matrix", §1.4) is not well defined; on its existential reading "Fails" holds but separates nothing: SUBSTATE S2c gives a non-spanning octahedral frame on which the Hadamard acts as a permutation. As displayed, the §0 verdict is stated without the hypothesis that gives it content. | **Dup / +:** MECH-2 Lemma F(b) (row 40) and TUNE-1 L4 escape audit, exact form (row 35; orthogonal frames on 𝓛_fin). T3 generalizes "orthogonal" to "spanning linear". **Note:** row 35 and 3A A.2 record that Lemma F assumes a finite configuration set (S3:241). T3 does too (finite carriers). | UB |
| T4 | FI-1ᵘ (an isometric non-monomial step) fails on the system and at every level of every theory faithful to 𝒦. | [A from K + X3]. | Yes; immediate from T2 and `preservesDiag_conj_of_monomial`. | **Dup in substance:** OA-1 row 9 [K] (`obsTheory` has no phases and is not DerivedOI); TUNE-1 Step 1 B.1 (`substratumGen_not_control`, diagonal preservation "operative"). **+** The quantifier over all faithful theories (paper level). | UB |
| T5 | FI-1 is not theory-invariant: `genTheory CM = substratumTheory` on every carrier, yet FI-1 holds for CM and fails for substratumClass. | [A], an induction on `InstAvail`. X1, X2 and X4b are support-level controls. **Not kernel-checked.** | **Yes (hand-checked).** CM is an Architecture (fields at :506–516). A square CM isometry is a permutation times a phase diagonal. In the readout case, a reindexed 0/1 diagonal is monomial. `genTheory` depends on 𝓘 only through `InstAvail` (:852ff), so propositional extensionality closes the step. | **+ NEW** at paper level. No REC-1 row covers it. Its parts (a), (b) and (d) are in APPROX r2/r4a C1–C3 (off `main`, #1221, :471–483: CM an Architecture, "CM's isometries are exactly the monomial ones", the FI-1 witness); the NEW step is (c), `InstAvail CM ↔ InstAvail substratumClass`, and the theory equality it gives. The nearest REC-1 row is 46 (OICORE-1 Lemma M, [R-off]). It bears on the wording of FI-1 in BRIDGE §5.1 and #1216, and on `exists_nonMonomial_of_layerFlowExecutable`, whose conclusion *is* FI-1. | A |
| T6 | `PhasesAvailable` is not fixed by the action on laws: `substratumTheory` and `permTheory` agree on diagonal inputs, yet differ on phases. | [A from K]. X4a is the instance. | Yes. | **C / elaborates:** Main:588 (phases "as a stated intervention principle"); K `obligations_independent`. | A |
| T7(a)–(c) | (a) NX-1(C) on T ⇒ FI-1ᵘ on an iterated-ancilla extension. (b) NX-1(C) on T ⇒ a non-monomial admissible operator on T. At level one this gives FI-1, and on the system it does so only under `SystemToLevelOne`. (c) FI-1ᵘ(T) ⇒ NX-1(C) on T. No equivalence is claimed. | [A], an induction on `InstAvail`. X6a and X6b. | **Yes. Directional, as §A.34 requires.** Hand-checked (b): each realized branch is Σ conj(M_i) with M_i ∈ 𝓘(T); discard gives m⁻¹Σ conj(block) = Σ conj(m^{-1/2}·block), admissible by `smul` and `block`; and if conj M fails `PreservesDiag`, M is not column-monomial. | **C** with #1216 c.6793397036 (level-one scope). **Dup:** the (b) lemma is the kernel theorem `realized_of_instAvail` (ImplementationLocality:530) [K], same induction, not cited by the draft; its corollary is the proof pattern of `exists_nonMonomial_of_layerFlowExecutable` (ExecSource:52) and `configurationLevel_falsifierUnavailable` (ManuscriptAxioms:155) [K], stated for an arbitrary system branch in APPROX r4a (#1221 @ `e41cf613`, :455–466, [R-off]). **X (scope):** T7 leaves system NX-1 ⇒ FI-1 open without `SystemToLevelOne`; APPROX r4a (:463–467) also states it under `LabelInvariant` transport, immediate for a label-invariant 𝓘 (transport along S ≃ S×Fin 1). Level n > 1 stays open. | A |
| C-dyn / E_r | Not decided. Selection and native operational sourcing remain open. | Statement of scope. | Yes (r1 overreach repaired). | **C:** REC-1 row 6 (Main:564/580, designed map, Q2-F at most), §4's final paragraph (selection on (φ, μ_H)), C11. TUNE-1 Step 1 D2 and D3 name the same routes. | — |
| §4 Q1–Q6 | Six candidate principles scored under §A.29. None adopted. Q3 (P-POL) is called the "most hard-to-vary". | Scoring. | Yes. Q1a is correctly labelled insufficient. | **C**, at a different level from REC-1 C1–C18. INTERVENE's candidates are *added operation principles*; REC-1's are *interaction-class restrictions*. Overlaps: Q6 ↔ REC-1 selection on (φ, μ_H); Q4 ↔ the kernel convention `permClass_le_of_exchanges`; Q5 (P-NB, non-bijective) has no REC-1 row. | — |
| AW marker | A premise not fixed by its action on diagonal laws has no native content under P-CONF, H4 and H-IND. | Methodology. | Yes, within its hypotheses. | **C:** REC-1 row 2 ("representability alone is not discriminating", Main:554); row 9. | — |

### 1b. SUBSTATE-BRIDGE-1 r2 (#1232 @ `86a413c8`)

| ID | Claim (condensed) | Status / proof | Review: supported at stated scope? | Reconciliation | Q2 |
|---|---|---|---|---|---|
| E1 | T0 extends to an arbitrary measurable hidden carrier. The induced object is a (sub-)Markov kernel, with ⊥ for non-termination. | [A]. Conditional on P-CONF∞, H4 and H-IND, plus measurability. | Yes. The disintegration and Lusin–Souslin facts are [L], labelled as such. | **Dup / +:** F2-1 A★2 (invariant-measure Koopman form; frozen on `main`); `pair-operation-source.md` §4 [R] as TUNE-1 Step 1 D1 quotes it. **+** E1 drops measure invariance and covers adaptive stopping. It also repairs T0's termination nit. | UB |
| Saturation | 𝒦_∞ = 𝒦 for a finite identified carrier: a finite register with prior ν(r) = ∏ T(r(s)∣s) induces any member of 𝒦. | [A]. X S1 (6 cases). | **Yes (hand-checked)**, under the *broad* H5. Review nit: this is not OI-native realizability. The register and its prior are designed from the target, as in REC-1 row 1 (S ⇒ D). | **C** with REC-1 row 1. | A |
| G1 / Q1c | T3's spanning hypothesis carries the finiteness (|Ω_enc| ≤ d²). On non-spanning frames (finite octahedral, continuum Husimi), non-diagonal-preserving unitaries have nonnegative frame maps. So E_f's "classical class" is frame-relative. | [A]. X S2, S2b and S2c. | **Yes (hand-checked).** The octahedron is permuted by (x,y,z) ↦ (z,−y,x), and the dimension bound follows from linearity. | **X with INTERVENE §0** as displayed: E_f without "spanning". There is no conflict with T3 itself. **+ NEW.** It bears on REC-1 rows 35 and 40 (their frames are orthogonal or spanning, so they are unaffected) and on OBL-SP: the remaining room lies at non-spanning preparations (OA-2 N2.1, (SP)). | A |
| E2 | Single-POVM lemma: under one linear encoding of **all** density matrices into laws, shared by all procedures, every native measurement is a post-processing of one POVM. So native measurements are jointly measurable, and sharp ones commute. | [A]. X S3. | **Yes (hand-checked item 4:** 0 ≤ M ≤ P ⇒ M = PMP). **Scope flag:** the hypothesis requires L to be positive on *every* density matrix. The epistricted and stabilizer-type encodings used by MECH-1, QP/U′ and Q-868-H are positive only on a restricted preparation set, so E2 does not reach them. This is the restricted-preparation, non-(SP) route. The draft's scope note lists context-dependent, non-linear and history-dependent encodings, but not a restricted domain. | **C / partial Dup:** MECH-2 Theorem NC (row 41: injective plus spanning reads ⇒ a noncontextual model); OA-2 E(b) (row 21). **+** E2 is finiteness-free and needs no spanning-read certification, but it concludes only joint measurability, not a noncontextual model. | UB |
| §2.4 1–5, G3 | Five changes on an infinite hidden factor. Item 5: on a continuum, "states are laws" no longer excludes amplitude coordinates, and "an infinite carrier is *necessary* for an exact register encoding over the full menu". | Items 1–4 are [A] or [W]. Item 5 is [A] with Main:564 at the pin. | Items 1–4: yes. **Item 5 flag:** the necessity rests on Main's classical-dimension obstruction (now Main:558). REC-1 row 5 classes that obstruction Q1-D + Q1-I + Q1-μ, with two premises: the preparation → finite ontic → measurement factorization, and a measurement-independent ontic law. Item 5 states the necessity without carrying them. It is a conditional result stated as unconditional, though minor, because it is a requirement and not a positive claim. | **C** with Main:58 (measure as realization datum; item 2) and TUNE-1 Step 1 D1 (exact `rot` needs an infinite carrier). **+** G3 (H3 is cardinality-dependent; site factorization (viii) is what excludes entangled amplitude configurations). | A |
| E3 | Profinite towers with continuous maps and readouts reduce to a finite stage at each finite horizon. | [A] on the RS/ANALYSIS lemma ([W]) and `RecursiveFiniteFactor` ([K], conditional). | Yes, at its scope. The review nit applies: it is not a no-go for non-continuous access or unbounded time. | **Dup:** assembled from records on `main`; TUNE-1 Step 1 D4 already cites it ("towers: finite stage per horizon"). | UB |
| L1 | Enlarging site alphabets at a fixed stencil adds no edge to G_φ. The cone is unchanged. | [A] on Main:362's argument. | Yes. Main's cone lemma uses only the finiteness of V. | **Dup / +:** Main:362 states the cone lemma for finite S_i. **+** L1 drops that finiteness. | UB |
| L4 | For an additive update on abelian site groups, G_φ^K is the same for every non-empty K, so no preparation indexes an edge. | [A], one line. | Yes. | **Dup (now on `main`):** Main:362 at `c3b5f37a`, merged via #1233 on 2026-11-11T14:09Z, after r2: "For a linear update … G_φ^K = G_φ for every non-empty K; a graph that differs between state classes requires an update outside (vii)" [P]. Main states this for finite S_i. **+** L4 extends it to infinite groups (R/Z, Z_p). **Stale in the draft:** "G_φ^K is defined in the head of PR #1233, off `main`" and "ledger (x) is unscoped". At `c3b5f37a`, (x) binds only G_φ^ref. | UB |
| L2 | Site-fibred towers under a stencil-respecting rule are in 𝒞_sep whenever the finite model is, so the bound ε ≥ (√2−1)/4 applies. | [A on D]. Conditional on Bell-scope Theorem N (#1231, [D]) and on Bell's theorem for measurable λ ([L]). | Yes, conditional as labelled. It excludes the O2 window. | **C:** Main:364–381 and :414 (REC-1 row 10). The window is now stated on `main` (Main:414, "Wings separated by less than the graph cone … fall outside the Corollary"). | UB |
| L3 | A shared factor that both wings read and no setting writes is a common cause. (Sep) is sufficient, not sharp (directed vs symmetrized G_φ). | [A]. X S5 (300 random cases). | Yes; this is the standard Bell argument. | **C** with Q-868-H r3 (V): a cube-vertex deterministic local model for native U′ product tests under SA-1(a), P3 with (iv), E-iso, WL and NNB. **+** G2: the directed-path refinement of (Sep). | UB |
| (NS_A), (PAD), S7 | Operational no-signalling is stated on the conditional laws μ_ab over complete histories, for each preparable law and both wings. A measure-transporting relabelling is a sufficient condition. A marginal-preserving relabelling can still signal when settings correlate with the pad. | [A]. X S7 (control and countercontrol). | Yes. The Haar pad is labelled a candidate distribution, not a sourced family. | **C** with Main §3.3(a) (operational no-signalling is "an additional requirement"), REC-1 C12 and H-xiv (setting–variable independence across admitted procedures). **+** An explicit counterexample showing that unconditional-marginal invariance does not give no-signalling. | A |
| Routes A/B/C, N1–N4 | A Bell escape (with MI kept) needs parameter dependence through A (a non-site-fibred factor), B (prepared long edges, which need an update outside (vii)) or C (within-cone propagation, untested). N1 and N2 apply to A only; N3 and N4 apply to all. | [A] classification. N1–N4 are open. | Yes (the r1 overreach is repaired). | **C** with Main:362 and :414 (option (a), long edges, the window), REC-1 rows 10–11, and the Bell-first note c.6791556736 (verdict 3, "INDETERMINATE … minimal missing lemma"). Route C is under MIXED-PATH-1 (#1235, branch `research/mixed-path-868-20261111`), which this reconcile did not read. | — |
| Q3 summary | F2-1 is `INCONCLUSIVE (gap)` on 13 screened rules. NATIVE-PADIC-1 and the related rounds are classical witnesses. None is a no-go, and none is spatial. | A description of records on `main`. | Yes, quoted with scope. | **Dup** of records on `main`. | — |
| Q4 / SLL | Indeterminate for OI. "Unable" is shown on four named classes, and a "possible carrier" is reduced to seven named properties, none supplied. SLL decides route A only. | Synthesis. | Yes (non-promotion kept). | **C** with REC-1 §3–4. SLL's exclusion branch turns on whether (viii) binds a deep hidden sector, an owner question parallel to Bell-scope F1 on (x). | — |
| §5 R1–R3 | No property meets §A.29. N3 (Haar pad) is the most hard-to-vary of them and supplies masking only. | Scoring. | Yes. | **C** with INTERVENE Q1b ("QM by fiat") and with REC-1 C2, C11 and C15. | — |

## 2. Q2: do the drafts supply an operation an embedded observer can reach?

**No.** Neither draft exhibits a Q2-F or Q2-P operation outside 𝒦, and neither exhibits the missing state-mixing operation at any level. The saturation register is a designed bijection with a stated prior; it is classed here with REC-1 row 1 (per-target realization, Q2-A), though under the convention of rows 6, 17 and 20 it would be Q2-F with designed-map standing; either way it realizes only members of 𝒦. Their constructive items are all Q2-A, that is, definable or representable:
- INTERVENE: the CM presentation (T5).
- SUBSTATE: the saturation register, chosen from the target kernel; the Husimi and octahedral frames, which represent operations rather than reach them; the Kibble-type embedding (§2.4 item 5, labelled "a statement about representability"); and the generic channel + pad tables (S4).

The substantive content is of the **upper-bound** kind:
- T0 and E1 say that any operation reachable under one fixed dynamics, under P-CONF(∞), H4 and H-IND, lies in 𝒦.
- T2, T3 and E2 then exclude non-classical transformations on route C and on spanning E_f, and incompatible sharp measurements under one full-domain linear encoding.

Because T0's outcome is an arbitrary function of the trajectory, these bounds do not depend on REC-1's open typing choices (C5, C6, C7). They do depend on H-IND, which is analogous to a fixed lift (OA-2 N0, MECH-2 H-LIFT; the exact relation is not audited, INTERVENE §6) and is read here, not in REC-1, as a Q1-I/Q1-μ premise.

**A boundary for the owner.** The drafts' classicality criteria are transformation-level: NX-1, `PreservesDiag`, nonnegative frame matrices. The criterion of OA-2, OA-3 and REC-1 OBL-SP is G3 simplex-embeddability of the prepare–measure fragment, and the two are different. OA-2 N2.1 and 𝔊_K (row 20) show that classical configuration models, all of whose operations lie in 𝒦, can fail to be simplex-embeddable: in N2.1 because the reachable laws do not span (reads complete); in 𝔊_K because preparation differences are moved out of reach of every read (point laws reachable; M-INACC, OA2:466–467; a designed non-affine map). So the drafts' negatives do **not** decide OBL-SP. Their non-spanning finding (G1) and E2's full-domain hypothesis point, by analogy only, at the (SP)-failing case that OBL-SP's P0 is set up to examine. G1's non-spanning concerns an encoding frame on route E_f; OBL-SP's (SP) concerns the reachable record laws of the native affine class under `D_0`; no map between them is given.

## 3. Drift since the drafts' pin (`cac5d264` → `c3b5f37a`)

1. **#1233 merged** (2026-11-11T14:09Z):
   - ledger (x) is now scoped to G_φ^ref;
   - G_φ^K and the linear-update statement are in Main:362 (this is L4 for finite S_i);
   - (xiv) is a ledger item ("Fourteen items");
   - the O2 window is stated at Main:414.

   SUBSTATE §3.1 item 4, the N1 status cell and the §6 row for #1233 ("provenance … off `main`") are stale. Its verdicts do not change.
2. **Main line numbers have shifted by −2** after line 4. The status Remark (Main:60) now states that "The Definition and the two axioms do not fix the cardinality of S", and the bijective representative is "defined here for a finite system only". This strengthens INTERVENE's "P-CONF posited" label. The quoted text at Main:588, :600 and :718 is unchanged.
3. **TUNE-1 Step 1 on `main`** cites both drafts as [D] context only. It quotes their headers' "r2 has not been re-reviewed". Both r2 heads have since received ACCEPT re-reviews (5857985732, 5859960068). The quote is accurate as to the file header but out of date as to status. This is a minor finding for that mutable record.
4. **APPROX** (the source of NX-1's definition) is now at r4a on #1221 (`e41cf613`, open). INTERVENE uses r2 from the session branch `ccr-9c2ecca4-vkb666` @ `820519cf`. **BRIDGE-UNIT1** (the source of FI-1's definition) is on that session branch only. Neither is on `main`.

## 4. §A.42 item 8 gaps if the drafts were to land

**INTERVENE-1:**
- **Gap: NX-1's definition and route split** (C, E_f, E_r, C-dyn). They come from APPROX r2 on the session branch `820519cf`, and r4a on #1221 is not reconciled. Options: land APPROX (#1221), or state NX-1 self-contained in the record.
- **Gap: FI-1's definition** comes from BRIDGE-UNIT1 (same session branch). A cheap closure is available: FI-1 *is* the conclusion of K `exists_nonMonomial_of_layerFlowExecutable` (ExecSource:52, on `main`), so the definition can be anchored there. K2 is already re-derived (the T4 proof, X3).
- **Gap: `checks.py` and `checks.out`.** They land with the record.
- **Re-pin needed:** the Main line citations (−2 shift). The Lean citations did not drift (only `OIRealization.lean` changed); `SystemToLevelOne` :116 is its docstring line, the `def` is at :117.
- **Governance provenance not located:** the PR body says "Owner approval: 2026-11-11 … (recorded on #1169)". No #1169 comment before c.6854241002 (2026-11-13) mentions INTERVENE-1 or SUBSTATE-BRIDGE-1, and no issue or PR comment created or updated since 2026-11-11 records an authorization for either; the one earlier mention found, #1216 c.6793397036 (2026-11-11T10:28:21Z), names INTERVENE-1 as a related draft and authorizes nothing. The same holds for SUBSTATE's "Proceed as suggested". These are not support gaps, but a landing record would have to link the owner's recorded authorization (§A.45 rule 3).

**SUBSTATE-BRIDGE-1:**
- **Gap: INTERVENE r2** (#1230) for P-CONF, the routes and T2–T4. E1 re-proves T0, but Q1b's consequences and G1 depend on INTERVENE.
- **Gap: Bell-scope r2** (#1231 @ `e1534b08`, open) for 𝒞_sep, Theorem N, Lemma G, O1–O3 and the constant. L2 and part of the §3.5 synthesis rest on it.
- **Support gap, not a §A.42 item 8 reference: the [L] facts.** Disintegration, Lusin–Souslin, and Bell's theorem for measurable λ are external inputs and need cited sources.
- **Gap: the probe files.** They land with the record.
- **Reclassify the #1233 row:** it is now support on `main` (Main:362).
- **No gap: the `wave_torus*.py` runs.** They are excluded from the evidence chain. They were disclosed, and the review accepted the quarantine, which is not a retroactive authorization.

**Landing order forced by the dependencies:** INTERVENE (with APPROX or BRIDGE or a self-contained definition) and Bell-scope #1231, in either order (#1231 does not cite INTERVENE), then SUBSTATE. REC-1 r7 itself cannot land while its own rows rest on #1267 and #1214 (REC-1 §6). Adding these drafts as REC-1 rows would add more such gaps.

## 5. Conclusion

**What each draft argues** (paper level, off `main`, reviewed by ChatGPT only, conditional throughout; not established under §A.46 item 1):
- **INTERVENE-1:**
  - Under P-CONF, H4 and H-IND, every procedure acts on configuration laws by a nonnegative kernel family. So no linear lift leaves `PreservesDiag` on route C, and no spanning linear frame gives a negative frame matrix on E_f.
  - FI-1 as formulated is a property of the presentation, not of the generated theory (T5).
  - The NX-1 ↔ FI-1 relations are level-scoped and one-directional (T7).
- **SUBSTATE-BRIDGE-1:**
  - These hold for an arbitrary measurable hidden carrier (E1, saturation).
  - The E_f obstruction needs spanning and has a finiteness-free measurement-side replacement (E2).
  - Site-fibred substates on `main` add no edge (L1, L4) and leave the within-cone (O2) window as in the finite model, untested.
  - Bell escapes split into routes A, B and C. Route A needs N1–N4, none supplied, and SLL is the missing lemma for route A only.
  - The verdict is indeterminate for OI.

**What they add to the current picture.** Most of the route-C/E_f core duplicates results already on `main`:
- OA-2 Lemma 0 and N0;
- MECH-2 Lemma F;
- OA-1's configuration ceiling;
- F2-1 A★2;
- Main:362, now including the finite form of L4.

The genuinely additional items, all [A]/[X] and off `main`:
- T5 (FI-1 non-invariance), NEW;
- G1 (the E_f classical class is frame-relative without spanning), NEW, together with E2;
- E1's removal of invariance and finiteness, and its ⊥ repair of T0;
- L1 and L4 for infinite site groups;
- the conditional-law form of (NS_A) with countercontrol S7;
- the A/B/C route classification with SLL.

None supplies an operation outside 𝒦 reachable under one fixed dynamics, and none supplies a physically derived one.

**Conclusion, at its exact strength.** Neither draft establishes an operation that is physically reachable under the currently demonstrated OI premises (REC-1 Q2-F or Q2-P). This is a finding about what the drafts and the corpus supply, not a documentation gap. It is also not a claim that such operations are impossible: routes C-dyn, E_r, non-spanning preparations and the O2 window remain open. Mathematical existence is a separate matter. For example, `realized_of_instAvail` [K] and T5 are proved, and conditional on their hypotheses, but they concern representations and generated theories, not physical reachability. The two obstructions to simplex-embeddability cited in §2 also remain distinct: N2.1 arises because the reachable laws do not span, and 𝔊_K is an instance of M-INACC (preparation differences out of reach of every read).

**Conflicts:**
1. **INTERVENE §0, E_f row** (and the §0 lemma summary, the post-T3 prose and the §3 table row): "spanning" is missing, so the verdict is stated without the hypothesis that makes the E_f class separating. SUBSTATE G1/S2c shows that the omission matters. Fixing it is the outstanding review nit 3.
2. **"Case (i) access-model-independent"** (INTERVENE) vs REC-1's **Q1-I/Q1-μ** classification of the same kind of result (rows 9 and 18). The conflict is in vocabulary, not mathematics; the review's own gloss resolves it.
3. **SUBSTATE §3.1 and §6** are stale against `main` after #1233 (the (x) scoping, G_φ^K and L4 now in Main:362).
4. **SUBSTATE §2.4 item 5** omits the factorization and measurement-independence premises of the classical-dimension obstruction (REC-1 row 5).

No mathematical contradiction was found between either draft and OA-1/2/3, REC-1 r7, TUNE-1 Step 2 or 3A r3, or Q-868-H r3.

**Disposition options for the owner** (no decision is made here; each needs its own owner record under §A.45 rule 7):
- **(a) Keep both as open drafts**, cited only as [D]/[R-off] context, as TUNE-1 Step 1 does now. Nothing is lost. The duplicated core stays available on `main` through OA-2, MECH-2 and Main.
- **(b) Land both as research records.** The prerequisites are:
  - a writer pass applying the outstanding nits (T0 termination; §1.3's "the output is not a function of μ (X7)" narrowed to the existence statement X7 supports, review nit 2; "spanning" in §0, after T3 and in the §3 table; the H-IND and "case (i)" gloss; the E2 full-domain scope; the item-5 premises; T7(b) citing `realized_of_instAvail` and APPROX r4a's `LabelInvariant` route);
  - a re-pin to current `main` and a refresh of SUBSTATE's #1233 text;
  - closing the §4 gaps, INTERVENE and #1231 before SUBSTATE (FI-1 anchored on the kernel theorem; NX-1 via #1221 or self-contained);
  - an independent non-author delta review;
  - an integration authorization.
- **(c) Land a reduced extract.** It would carry only the non-duplicated items (T5, G1 with E2, E1, L1 and L4 for infinite groups, (NS_A) with S7, the A/B/C routes with SLL), cite OA-2, MECH-2 and Main:362 for the rest, and translate the labels into REC-1's Q1/Q2 vocabulary. This is a new writer unit and needs its own authorization.
- **(d) Record them as [R-off] rows in a later REC-1 revision**, without landing. Under REC-1 §6 this adds off-`main` support gaps that would have to close before REC-1 lands.
- **(e) Retire them under §A.43 item 6** to #1169, without merging and keeping the branches, if the owner judges them inactive. The non-duplicated items listed in (c) would then survive only on branches.
