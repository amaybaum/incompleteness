# Measurement as an additional condition: node 1 on the F2 missing premises O-A and O-B

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to the repository.

**Base.** Papers and kernel at `origin/main` = `df9e601ebe2a4e5af2a82f2d06ca2797c3a10f88`; every [AT] name below was
confirmed by `git grep` of its declaration there (Lean paths under `verification/lean-mathlib/OIBridge/`). Paper lines
(Main.md:n, GR.md:n) and ROADMAP lines (RM:n) are at `df9e601e`. LG = `f2-ledger-20261020/LEDGER.md` (branch `ccr-9c2ecca4-vkb666` at
`38e9af32`; its own base `ec49d0b4`). N1 = O-A node 1 (`../oa-node1/NODE.md`, with its review outcome). XS, MI+, SC =
`REPORT.md`, `mi-plus/{PREREG,RESULT}.md`, `source-search-20261020/SOURCE-CHECKPOINT.md` on
`research/x-screen-20261018` @ `76383997`. PM = `premise-memo/PREMISE-MEMO.md` on `staging/premise-memo-864-20261018`
@ `641ae161`. H = thread H @ `804843f1`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (two runs, byte-identical);
[UP] unsourced premise; [L] literature; [rec] recorded in the cited record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "no listed condition
supplies O-A/O-B" and either constrains the form the missing component must take or exposes a hidden assumption.

***

## 1. Inventory of OI's posits, lemmas and conditions against O-A and O-B

"O-A" = continuous non-monomial operation on the elementary system (LG §3); "O-B" = compatibility/validity with G3 (LG §3).
"none" = supplies nothing at the observer's operation or cone level.

| # | item | location | supplies at the observer level | O-A / O-B | settling result |
|---|---|---|---|---|---|
| 1 | observation triple, proper subsystem | Main.md:44 | the frame | none | — |
| 2 | Lemma 1, finite visible space | Main.md:48 | finite carriers | none; it is CR premise P1 (N1 §2.1) | `obsTheory_nonnegBounded` FrozenSourcing.lean:84 |
| 3 | Lemma 2, causal partition | Main.md:50 | hidden sector | none | — |
| 4 | Lemma 3, bijectivity; counting-measure selection | Main.md:56–62; ledger (iii), (iv) Main.md:708 | permutation dynamics; canonical prior | none: operations are permutations | `permClass` SubstratumInterfaceAudit.lean:236, `obsTheory_eq_permTheory` :774, `permTheory_not_qm` :716 |
| 5 | total finiteness (Substratum A1) | Main.md:708 (ii) | finite representative | none; CR P1 | N1 CR [W] |
| 6 | hidden prior μ_H as realization datum | Main.md:60 | real mixtures | none | N1 row 2 [W] |
| 7 | C1–C4 (C4 primitive) | Main.md:74–80, :604 | diagnostics of the visible law | none: configuration-diagonal, fixed by Γ | PM F-α; SC N9 [rec] |
| 8 | S ⇔ D ⇔ Q_fb | Main.md:528–534 | fixed-basis representation | none (representability) | `finite_horizon_equivalence` Equivalence.lean:459; PG §3.12 |
| 9 | classical-dimension obstruction | Main.md:538 | no fixed finite realization reproduces a qubit's prepare–measure theory | constrains any test-side source that keeps a fixed finite carrier; OI's per-experiment carriers evade it, so CR is the operative obstruction | paper half [W]; unboundedness [L] (Heinosaari et al. [55]) |
| 10 | gluing; uniform-continuum realization | Main.md:542, :562 | finite-accuracy realizations | none under exact A1 | — |
| 11 | unavoidable hidden predictive memory | Main.md:582 | classical memory bounds | none | `unavoidable_hidden_predictive_memory` HiddenMemory.lean:179 |
| 12 | canonical predictive quotient; open purification lift | Main.md:600–602 | existence half of purification at substratum level | O-B only through OP, screened | XS S1, op-fork [rec]; `fiber_freedom` [rec] |
| 13 | update = Bayesian conditioning, diagonal sector | Main.md:632 | native update | O-B diagonal sector only | PM UPD [rec] |
| 14 | native readout is local Lüders; the recorder | — | configuration Lüders instrument; record writing | none: holds in permTheory | `readout_is_localLuders` OperationalAssembly.lean:658; `recordInstr_apply` InternalObserver.lean:252, `recordInstr_writes` :272, `recordInstr_not_passive` :290 |
| 15 | passive observation theorems | Main.md:570 | complete passive observation ⟺ commutative | none: theory-insensitive | `complete_passive_iff_commutative` CentralObservation.lean:620, `passivelyIncomplete_of_card` PassiveIndependence.lean:80 |
| 16 | embedded observation (R)(L)(M) | GR.md:258 | iterated ancilla closure | none: satisfied by generated theories | `EmbeddedObservation` EmbeddedObservation.lean:123, `embeddedObservation_of_qm` :327, `embeddedObservation_independent` :343 |
| 17 | conditions (i)–(v) | GR.md:216–228 | (iv) full reversible control | (iv) contains O-A; none supplied by bare OI | `exactAll_iff_physical_general` GeneralCarrier.lean:100, `oi_alone_not_qm` :160, `five_way_minimality` RankGapTheory.lean:702 |
| 18 | phase intervention (stated); layer-flow box | GR.md:260, :266–272 | phases as an assumption; layer flow unsourced | O-A, split into a uniform-ray breaker (phase) and a continuum (layer flow) | `permClass_onesFixing` PhaseSource.lean:79; `derivedOI_qm_iff_layerFlowExecutable'` DerivedQ3.lean:222; `substratumTheory_not_layerFlowExecutable` LiftAudit.lean:200 |
| 19 | controllability resource | GR.md:260–264 | posit | O-A posit | `substratum_plus_control_qm` StructuralClosure.lean:414; `readWriteSourced_not_qm` ReadWriteControl.lean:174 |
| 20 | coherent-completion classification; global antiunitary | GR.md:192–214 | uniqueness given existence; one ℤ₂ | none for O-A; GTR fails G3 | SC N5 [rec] |
| 21 | global lattice orientation | Main.md:656–658 | fixed frame | none | N1 row 3; SC N6 [rec] |
| 22 | continuous-time path; non-unique interpolation | Main.md:568; GR.md:332 | representation-level flows | O-A represented, not available | `driveQ_isContinuousPath` SecondOrderDrive.lean:225; `continuous_extension_not_unique` RegionLimit.lean:296; N1 §3 |
| 23 | rooted class | — | the rooted visible law | control | `finiteRootedRealizable_iff_pper` RootedClassificationAllTime.lean:192 |
| 24 | Bell branch (ontic parameter dependence) | Main.md:394–405 | correlation structure | none; set-level clauses are Γ-invariant | PM SET, F-β [rec] |
| 25 | ledger items (v)–(xii) (mixing, isotropy, A5, site factorization, degree, range, A4, A6) | Main.md:708 | rule properties | none for operations | `obsTheory_rule_independent` SubstratumInterfaceAudit.lean:779; `cx3b_complex_not_A1` A6Instantiation.lean:512 |
| 26 | passive thermal orientation | GR.md:188–190 | global orientation | O-B only as TH, class (iii) | `counting_passive` ThermalOrientation.lean:256; PM TH [rec] |

**Inventory finding.** The two items that state O-A content are posits (18, 19). Item 9 is a paper-level test-side
obstruction that CR does not contain, but it binds only a fixed carrier. Every other item supplies nothing at the level
of available operations. At the cone level, items 12, 13 and 26 reach O-B only in screened forms.

***

## 2. "The act of measurement" as an added condition: the distinct strengthenings

CR (N1 §2.1, reviewed): under OI-1, supervenience (P2) and countably many carriers, the available conjugations are
countable. Under A1, a supervenient condition therefore cannot supply O-A. The table classifies each strengthening by
whether it keeps the operations native, and so supervenient.

| id | strengthening | native? | screened as | verdict |
|---|---|---|---|---|
| MC1 | measurement is a reversible coupling to an internal meter | yes (CNOT, `permClass_readWrite` :412) | XS S2 (MI), MI+ C0–C13; H E1 and AW-H5 for symplectic meters | adds no operation (G4); MI insufficient alone [rec] |
| MC2 | outcome-conditioned updates are valid on the observer's states | yes | PM UPD | class (iii); collapses to K ⊆ Q3 under local unitaries [rec] |
| MC3 | repeatability, record stability | yes | MI+ C3 REP, C7 REC | DERIVED, holds on every domain cone [rec] |
| MC4 | M1 on retained protocols, disturbance by new ones | yes for M1 | MI+ C13 SYM; H check B | M1 is a control. "New protocols disturb" presupposes non-native protocols, i.e. MC10 |
| MC5 | information–disturbance trade-off | yes | — | theory-insensitive (`passivelyIncomplete_of_card`); quantitative forms presuppose non-commuting tests (MC10) [W] |
| MC6 | Born weights from hidden-sector counting or typicality | yes | PM F-α | fixes diagonal statistics only; Γ-blind; adds no operation [W] |
| MC7 | relational or observer-relative readout | yes | SC §1 (Wigner's-friend covariance, observer-partition covariance) | the operation class does not see the cut (`obsTheory_rule_independent`) [rec] |
| MC8 | embedded observation (regrouping) | yes | kernel | satisfied by every generated theory with a label-invariant class (`genTheory_embeddedObservation` ImplementationLocality.lean:904) [AT] |
| MC9 | sharp-update geometry | yes | PM GEO; MI+ A1 | no pair form; unproved [rec] |
| MC11 | measurement in any basis one can prepare (preparation side) | no (coherent preparations) | LG §3 monomial-branch lemma | with configuration readouts, every branch is row-monomial, so no coherent control [rec] |
| **MC10** | **TU: sharp tests in non-configuration token bases are available, with the Lüders update** | **no** | **not screened as a source** (see below) | **the node** |
| MC12 | unsharp or non-Lüders updates as available instruments | no | — | generic unsharp Lüders updates are `OnesNormal` (§3 T2); the open residue is §4 2(iii) |

**Screening status of MC10.** `git grep` for teleportation, measurement-based and Zeno has two hits, neither
substantive: E-bell-composite.md:280 at `804843f1` lists "teleportation" among composite protocols, and Substratum.md:50
uses "measurement-based" for a separation criterion. The records do treat non-configuration tests, but as
*consequences* of O-A:
- the token ball and its non-configuration effects come from O-A (LG:106, :134);
- thread I's H11b (I:325) is a closure clause;
- the K∞ chain derives the sharp family from a body-preserving group (`sharpFamily_subset_avail` EffectSpace.lean:374).
TU runs in the converse direction, from tests to operations. That is not circular, but it sources nothing (G2 FAIL, §3).

MC1–MC9 keep the operation class inside `permClass`, so under A1 none can supply O-A (CR). Each adds no operation, so
each fails G4 standalone. MC10 is non-native: its Kraus branch |v⟩⟨v| has two nonzero entries per row, while native
branches have at most one (LG §3). MC10 therefore violates P2, and CR does not exclude it a priori.

***

## 3. Pressure test of TU (§A.31, favourable branch)

**Decision rule (fixed before computing).**
- TU is a *complete* O-A source iff, with the native class (permutations, configuration attach, discard, outcome-conditioned
  composition), it makes available exactly (a) some non-monomial reversible operation and (b) some unitary that moves the
  all-ones ray.
- It is a *partial* source iff (a) holds and (b) fails by an invariant.
- It is *empty* iff (a) fails.

**T1. TU makes the layer flow of X executable, exactly and deterministically [EC A1–A8].**
- A Lüders Y-test on a fresh |0⟩, with native X on outcome −i, yields |+i⟩ in both branches.
- Attach that ancilla and apply CNOT with the ancilla as control and the data as target. Then Lüders-test the ancilla in
  the real basis w = (cos φ, sin φ), w⊥ = (−sin φ, cos φ), and apply native X on outcome w⊥.
- Both branches are then ∝ R_x(−2φ), and the coarse-grained channel is conjugation by R_x(−2φ) on a generic input.
- `unit g t` (SecondOrderCircuit.lean:356) is exp(iπt(1−g)/2), so `unit X t` = e^{iπt/2} R_x(πt), and `gateFlow`
  (LiftAudit.lean:47) is built from it. With φ = −πt/2 the protocol realizes conjugation by `gateFlow X t`.
- `LayerFlowExecutable` (LiftAudit.lean:112) asks, for all n and t, for
  `availExt n Unit (conjChannel (gateFlow (levelPerm σ n) t))`. The protocol meets it for σ = X on a token, with the
  other tokens and the level ancilla as spectators [W].
- The kernel attaches only a maximally mixed ancilla, so preparing the fresh |0⟩ needs a readout and a conditional swap
  inside the discard [W].
- R_x(π/2) is non-monomial and breaks entrywise nonnegativity and reality (A6, A7). Every R_x(t) fixes the all-ones ray (A8).
- Exactness at every t needs the continuum of real bases. A finite basis set gives countably many angles, consistent with CR.

**T2. Sharp Lüders measurement in any basis preserves the protocol invariant [W from AT].**
- The kernel's `OnesNormal` (InstrumentRealization.lean:172) asks for a Kraus decomposition with Σ_i K_i^H 1 = 1.
- `instAvail_onesNormal` (:313) proves that every constructor of `InstAvail` (ImplementationLocality.lean:268) preserves it,
  for a ones-fixing class.
- The `readout` case uses only `readProj_sum` (:207), Σ_k P_k = 1, and a reindexing.
- So the proof carries over unchanged when the readout constructor admits *any* complete orthogonal projective family,
  in particular TU's |v⟩⟨v| ⊗ I, |v⊥⟩⟨v⊥| ⊗ I in every basis.
- Class-level step. Every orthogonal projector P lies in `onesClass` (InstrumentRealization.lean:446): take
  E = [P; 1−P], F = [1; 0] (both ones-compatible) and W = 1, so that EᴴWF = P (review `rev_exact.py` B6, token and
  two-token instances).
  - `onesClass` is an architecture (`onesClass_arch` :628) and is ones-fixing (`isometry_fixes_ones` :833). It contains
    every permutation matrix and every gate flow of a layer.
  - T2 therefore runs inside the kernel's own class with hf := `isometry_fixes_ones`, and the readout projectors are
    admissible there (the `hP` premise of the readout constructor).
- The invariant is also wider than sharp readout. `OnesNormal` is existential and allows Kraus operators to be split, so
  it holds for a primitive family {K_j} exactly when 1 ∈ span{K_jᴴ1}. The bind, coarse and discard cases work for any
  primitive that has it.
  - Generic unsharp Lüders instruments satisfy it. For E = diag(1/4, 3/4), the split with s = √3 − 1 gives Σ K^H 1 = 1
    (review B1, B2).
  - A replace-by-ψ channel satisfies it exactly when ⟨1|ψ⟩ ≠ 0 (review B4, B5). This is why |+i⟩ is reachable and |−⟩
    is not.
- `instAvail_unitary_fixes_ones` (:398) then gives: **every unitary conjugation available in the TU-extended theory fixes
  the all-ones ray.**
- Consequences:
  - The quarter phase S and the sign Z are unavailable, so the theory is not QM on any carrier with ≥ 2 states, by the
    argument of `onesTheory_not_phasesAvailable` (FlowEndpoint.lean:177).
  - Relative to `SourcedOI`, the phase-free driven transition that `sourcedOI_qm_iff_phaseFree` requires moves the ray
    (`onesTheory_not_phaseFree` :142), so TU cannot supply it either.
  - Deterministic preparation of any state with zero uniform weight (e.g. |−⟩) from configuration states is impossible.

**T3. Checks of T2 [EC B0–B7; solver].**
- The full Kraus list of T1's protocol satisfies Σ K^H 1 = 1 (B1) and Σ K^H K = I (B2). That list includes the |+i⟩
  preparation subtree and the configuration Kraus of the discard, and B0 confirms it gives the same channel.
- The equatorial phase teleport (test angle θ) keeps the invariant (B3). Its branches are D and Z·D, with
  D = diag(1, e^{−iθ}) (B4), and Z moves the ray (B5), so it is not deterministic.
- Sensitivity:
  - the single-Kraus decomposition I⊗⟨m| fails the identity (B3b; the invariant is existential, so this is a
    code-path control);
  - B6, an unsharp Lüders instrument with the single-Kraus-per-branch decomposition, is a **vacuous** sensitivity
    control: that instrument is `OnesNormal` under splitting (review B1, B2);
  - attaching |−⟩ makes the CNOT kickback exactly Z and violates the invariant (B7).
- The AND-OR solver (`det_solver.py`, exact Gaussian rationals; least fixed point on the explored graph, so a reported win
  is a real finite protocol):
  - |−⟩ is never deterministic with Pauli Lüders tests at n = 2 and n = 3, affine permutations, full graphs of 125 and
    3229 states;
  - nor at n = 3 with Toffoli/Fredkin, bounded at 30 000 states;
  - positive controls: |+i⟩ and |+⟩ are deterministic, with explicit protocols found (|+⟩: X-test; on −, CNOT then
    X-test);
  - negative controls: configuration tests only, and a single token, never give |−⟩.
  - T2 predicted every MAIN row in advance; the solver is an independent code path.

**T4. One discrete sign completes TU [EC C1–C3 for single-token relations; L for registers; W for QM].**
- With Z available, the phase teleport is deterministic for every θ (C1).
- Exact relations: H ∝ R_z(π/2)R_x(π/2)R_z(π/2) (C2), and S ∝ R_z(π/2) (C3).
- With the native CNOT, every unitary on a 2^k register is an exact product of CNOTs and single-token unitaries
  [L: Barenco et al. 1995].
- So TU + Z + native ⟹ full reversible control on qubit-power registers, hence QM-reg through `exactAll_iff_physical_general`.
  This is [W]: (iii) and (v) hold inside the PSD carrier, and the corner cases are not re-derived.
- Converse: with full control, the Lüders instrument in basis U|c⟩ is Ad_U ∘ readout ∘ Ad_{U†} [W]. Relative to the
  native class, then, TU ⊕ Z ⟺ full control on 2^k registers, with one witness per direction (§A.34). In place of Z, a
  deterministic |−⟩ preparation gives Z by the CNOT kickback (B7). The display is stated for Z, not for an arbitrary
  uniform-ray breaker.

**T5. Destructive tests do not suffice [W; EC DES row].**
- A destructive non-configuration test followed by native re-attach has branches ⟨v|_A M (I ⊗ |c⟩_A).
- Each column has at most one nonzero entry, which makes the branches column-monomial: the dual of LG's row-monomial
  lemma for preparations. A unitary column-monomial branch is monomial.
- Coherent preparations alone give row-monomial branches, and coherent destructive tests alone give column-monomial ones.
  T1 needs both, which the Lüders post-measurement state supplies.
- The solver agrees: with destructive Pauli tests, |+i⟩ is not deterministic (8 reachable states, all configuration states).

**Skepticism on the favourable reading "measurement is the missing component".**
1. *Source.* TU is non-native (§2), so it violates P2 exactly as the drive does. The word "measurement" adds no sourcing
   argument (G2 FAIL). Nothing in OI places a non-configuration test into availability: the update is conditioning on a
   visible configuration (Main.md:632).
2. *Equivalence in kind.* TU carries the content of `LayerFlowExecutable` (T1), and full control implies TU (T4 converse).
   It is the layer-flow posit expressed on the test side.
3. *Incompleteness.* By T2 TU cannot carry the uniform-ray part, so it cannot be the whole missing component.
4. *Knobs.* TU must posit a continuum of bases. T1 uses a one-parameter real family plus the Y basis, and choosing
   that family is a G7 question.
5. *O-B.* A local Lüders filter maps every domain cone into SEP ⊆ K: for X ∈ maxCone, (P_v⊗I)X(P_v⊗I) = |v⟩⟨v| ⊗ (a PSD
   conditional) [W]. TU's own pair-level compatibility is therefore automatic. Preservation of K by the TU-generated
   flow reduces to ATT, NC₃ for the CNOT ancilla→data, a non-configuration RO₃ and DIS. These are Σ3-type clauses
   (LG §4), unsourced, in agreement with AW-F1 [W]. TU does not source O-B.

**Verdict (by the rule).** TU is a *partial* O-A source. It supplies (a), the non-monomial continuum (the layer flow),
exactly. It cannot supply (b), by the invariant `OnesNormal`. It is non-supervenient and does not source O-B. Measurement
in the von Neumann–Lüders sense is therefore not the missing component under any availability strengthening whose
primitives are `OnesNormal` over the ones-fixing native class. That scope covers sharp tests in every basis and generic
unsharp Lüders updates.

***

## 4. The logical form the missing component must have

From CR, T2 and T4, any extension yielding exact QM on qubit-power registers from OI's native class needs:

1. **Non-supervenience** (CR): some available primitive is not a function of an implementing substratum process plus
   countable context, or else the substratum is enlarged.
2. **A non-`OnesNormal` primitive** (T2). Each such primitive is one of:
   - (i) an admissible isometry that moves the all-ones ray, a phase-type operation;
   - (ii) a preparation of non-uniform weight, e.g. |−⟩, whose ω = ⟨1|·⟩ differs from that of configuration states;
   - (iii) more generally, any primitive family {K_j} with 1 ∉ span{K_jᴴ1}, such as Z or a deterministic preparation
     of |−⟩. Generic unsharp Lüders updates are not in this class (T2).
   Given TU, one discrete real sign Z (equivalently one deterministic zero-weight preparation) suffices (T4).
3. **An uncountable non-monomial family** (A1 with `countable_not_pairFlowSourced` PairFlowEquivalence.lean:218):
   either a continuous operation family or, equivalently for this purpose, a continuum of sharp Lüders test bases (T1).
4. **O-B**:
   - the fixed identification G3: native operations act by Ad_P, and a TU branch acts by Ad_{P_v};
   - compatibility clauses reaching three tokens (AW-F1), since TU's pair-level compatibility is automatic and excludes
     nothing (§3 item 5).

In the kernel's own split (GR.md:266–272: phase intervention plus layer flow), measurement can stand in for the layer flow
and not for the phase intervention. Relative to `SourcedOI`, where no phase is assumed, the two are fused in the phase-free
rotation, and no measurement condition reaches it.

**Controls any candidate must preserve, fixed in advance (§A.29).**
- (1) `permTheory_not_qm` and the monomial class (`substratum_residual` StructuralClosure.lean:383) stay non-QM when the
  extension is removed.
- (2) The rooted law (`finiteRootedRealizable_iff_pper`) is unchanged for native protocols.
- (3) M1 on retained protocols: TU and sign primitives add protocols and leave native ones unchanged.
- (4) Must-fail: preparations alone give no coherent control (LG §3).
- (5) Must-fail, new: sharp measurements alone give no phase (T2).
- (6) The candidate names which CR premise it gives up.
- (7) Γ(Q3) and K(Z_F) are excluded only through the fixed identification and multi-token clauses.
- (8) The fixed-carrier obstruction of Main.md:538 is respected.

**Independent prediction (G6).** OPEN. The TU-only world predicts that no state of zero uniform weight can be prepared
deterministically, and that no deterministic sign flip exists. Laboratory practice contradicts both, which rules out
TU-alone. That is a retrodiction against an incomplete candidate, not a prediction of a complete one.

***

## 5. Hidden-assumption watch (measurement framing)

| # | assumption | where | finding |
|---|---|---|---|
| HA-M1 | the barrier against coherent control is "configuration readout" | LG §3 monomial lemma; `InstAvail` readout constructor | **exposed.** The configuration restriction is load-bearing only for monomiality, the continuum part. The phase part rests on completeness Σ P_k = 1 together with ones-fixing isometries, which survive any sharp basis (T2) |
| HA-M2 | O-A is one premise | LG §3, §5; N1 | **CONFIRMING, not exposed.** The split into a uniform-ray breaker and a continuum is already in the records: LG:346; H:42 and :245–250 (I3 = `OnesFixing`, E4); I:263–271 and :531; and the kernel pattern `onesTheory_layerFlowExecutable` FlowEndpoint.lean:87 with `onesTheory_not_phasesAvailable` :177, into which TU embeds. The node adds that, given TU, a single sign suffices |
| HA-M3 | "valid measurements" and "nonclassical operations" are separate F2 targets | RM:1125–1127 | with native multi-token protocols, tests carry operation content (T1), and full control implies TU (T4). The targets are not independent |
| HA-M4 | measurement content is the effect (test) | MI+, PM OVc/MEV | the Lüders post-measurement state is load-bearing (T5). Coherent effects and coherent post-measurement states are needed together |
| HA-M5 | deterministic exactness needs feed-forward | GR.md:216 (outcome-conditioned composition) | admitted by the operational-theory definition; not hidden |
| HA-M6 | sharp Lüders form | `readout_is_localLuders` forces it for sharp native readout only | not load-bearing for T2. Generic unsharp Lüders updates are `OnesNormal` (review B1, B2). The open class is primitives with 1 ∉ span{K_jᴴ1} (§4 2(iii)); which non-Lüders updates fall in it is not classified [U] |
| HA-M7 | the finite-substratum obstruction applies to OI | Main.md:538 | it binds a fixed carrier. OI grows carriers per experiment, so CR is the operative obstruction |

Assumption-watch markers:
- **AW-MC1.** `OnesNormal` survives sharp Lüders measurement in every basis. A claim that measurement supplies phases or
  dense unitary control must name its non-`OnesNormal` primitive.
- **AW-MC2** (CONFIRMING; LG:346, H:42, I:263–271). O-A = a uniform-ray breaker plus a continuum. Records citing O-A
  should state which part a candidate supplies.
- **AW-MC3.** TU implies the layer flow. "Measurement sources the drive" is at most the layer-flow half, and it is non-native.
- **AW-MC4.** Destructive tests give column-monomial branches and preparations give row-monomial branches. Only their
  combination, the Lüders update, gives coherent control.

***

## 6. Not verified

- T2 is a written transfer of `instAvail_onesNormal` and `instAvail_unitary_fixes_ones` to a readout constructor admitting
  arbitrary complete projective families. It is not formalized or compiled. The readout case was read at
  InstrumentRealization.lean:331–335.
- T4's step to QM-reg rests on [L] Barenco et al. for exact two-level decomposition, and on GR's characterization.
  Whether the TU ⊕ Z theory meets `DerivedOI` (RouteB.lean:141) was not checked; the route used avoids it.
- The O-B reduction (§3 item 5) is [W]. The three-token clauses were not computed.
- The solver is bounded for the Toffoli/Fredkin case (truncated at 30 000 states). Its negative rows are relative to the
  bound and to Pauli bases; T2 is the general statement.
- Non-Lüders instruments (MC12) are not classified against the criterion 1 ∈ span{K_jᴴ1}. Unsharp Lüders instruments
  are settled by the review (B1, B2).
- [rec] rows (XS, MI+, SC, PM, H, N1) were taken as recorded. LG and N1 line citations are at `ec49d0b4`.
- The first run of `mc_check.py` had two FAILs (B1, B3). The check used the single-Kraus decomposition I⊗⟨w|, which
  is not the decomposition the invariant is stated for. The corrected check uses the Lüders projector with the
  configuration Kraus of the discard (B0 shows the channel is the same) and keeps the wrong form as B3b. A8's inert first
  disjunct was removed. Final outputs are two byte-identical runs.

***

## 7. Files (`probe/`)

| file | sha256 | role |
|---|---|---|
| `mc_check.py` | `44ced633…efd7` | blocks A–D, 21 checks (SymPy 1.14.0, Python 3.13.16, `-I -B`) |
| `mc_check.run1.out`, `.run2.out` | `6a725d91…cb05` (both) | 21 PASS, 0 FAIL |
| `det_solver.py` | `ae626b43…920a` | exact AND-OR solver |
| `run_solver.py` | `d4aab9ce…29e9` | 8 rows with controls |
| `run_solver.run1.out`, `.run2.out` | `815b6d8c…4ad2` (both) | 8 PASS |

Full digests are in `probe/SHA256SUMS`; the review files and their digests are in `probe/review/`.

***

## 8. Productivity verdict

**Gem: yes.** The node yields three facts strictly stronger than "no listed condition supplies O-A/O-B":
1. Granting the strongest measurement-availability condition (TU), even non-supervenient and uncountable, does not
   supply the uniform-ray part of O-A. Every available unitary stays ones-fixing [W from AT; EC].
2. TU supplies exactly the other part, the layer flow that GR.md:272 records as unsourced, deterministically
   and exactly [EC].
3. Given TU, the residue is one non-`OnesNormal` primitive, and a single discrete sign suffices. The evidence is [EC] for
   the single-token relations (C1–C3), [L] (Barenco et al.) for registers, and [W] for QM via
   `exactAll_iff_physical_general`.

These constrain the form of the missing component (§4). They expose HA-M1 (the configuration restriction is not what
blocks phases). HA-M2 is CONFIRMING (§5).

**Ledger correction (F4).** LG:352–353 reads: "The monomial lemma is a must-fail control: a construction that adds only
preparations, or any other non-operation resource, to the native class does not qualify." T1 contradicts the second
clause: TU adds instruments, not operations, and yields an exact non-monomial continuum. The lemma's scope is protocols
whose instruments are configuration readouts. Proposed wording, to be propagated per §A.25 wherever the lemma is restated
(LG §3 item "New [W]", §5 item 2):

> The monomial lemma is a must-fail control: a construction that adds only preparations to the native class, with
> configuration readouts as the only instruments, does not qualify. Non-configuration sharp instruments with the Lüders
> update fall outside the lemma. They yield the layer flow exactly, but remain within the invariant `OnesNormal`, so
> they supply no uniform-ray-breaking operation.

**Classification (as corrected by the independent review): NEW (narrow).** The new content is the gadget direction
"Lüders tests ⟹ layer flow" and the ledger correction F4. Everything else is ELABORATING or CONFIRMING:
- the invariant is the kernel's own (`instAvail_onesNormal`), and its transfer to arbitrary projectors runs inside
  `onesClass`;
- the phase/layer-flow split is already recorded (HA-M2);
- the one-bit teleportation gadgets are standard [L: Zhou–Leung–Chuang 2000; Nielsen 2003].

Answer to the owner's question: The act of measurement, in every native form, adds no operation. In its
only non-native form (TU) it can be one half of O-A, the continuum, and provably not the other half, the uniform-ray
breaker. It does not source O-B.

***

## Independent review outcome

Review: `probe/review/` (`rev_exact.py`, `rev_random.py`, their outputs and `SHA256SUMS`, copied unchanged from
the reviewer's working copy). The corrections above are applied in place. The pre-review text is not kept here; its
sha256 is `c7e2ccb212fc0d91bfa7d189ef18d466f89f0d019f4dd5ad9756ca66bb7ad87f`.

| claim | verdict | applied as |
|---|---|---|
| 1 TU ⟹ layer flow (T1) | CONFIRMED | review A0–A7 re-derive it; F1 notes on `LayerFlowExecutable`, `unit` and ancilla preparation added |
| 2 OnesNormal survives sharp tests (T2) | CONFIRMED | class-level step re-based on projectors ∈ `onesClass` (F3) |
| 3 checks of T2 (T3) | CONFIRMED | B6 marked vacuous; the replace-by-ψ criterion explains |+i⟩ vs |−⟩ (F2) |
| 4 residue and T4 display | CORRECTED | §4 2(iii) restated as 1 ∉ span{K_jᴴ1}, since generic unsharp Lüders updates are `OnesNormal` (F2); display is TU ⊕ Z (F7); tags split [EC]/[L]/[W]; verdict scoped to `OnesNormal` primitives |
| 5 destructive tests (T5) | CONFIRMED | — |
| 6 O-B reduction | CONFIRMED | — |
| 7 HA-M1 / HA-M2 | HA-M1 CONFIRMED; HA-M2 REFUTED as "exposed" | HA-M2 retagged CONFIRMING with record citations (F5) |
| screening statement | CORRECTED | grep hits named; tests-as-consequence records cited (F6) |
| ledger | NEW | LG:352–353 wording correction proposed (F4) |

**Overall classification: NEW (narrow).** The new content is the gadget direction "Lüders tests ⟹ layer flow" and the
ledger correction F4. Everything else is ELABORATING or CONFIRMING.
