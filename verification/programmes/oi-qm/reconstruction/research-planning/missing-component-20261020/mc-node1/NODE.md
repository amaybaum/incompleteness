# Measurement as an additional condition: node 1 on the F2 missing premises O-A and O-B

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to the repository.

**Base.** Papers and kernel at `origin/main` = `df9e601ebe2a4e5af2a82f2d06ca2797c3a10f88`; every [AT] name below was
confirmed by `git grep` of its declaration there (Lean paths under `verification/lean-mathlib/OIBridge/`). Paper lines
(Main.md:n, GR.md:n) and ROADMAP lines (RM:n) are at `df9e601e`. LG = `f2-ledger-20261020/LEDGER.md` (branch `ccr-9c2ecca4-vkb666`;
its own base `ec49d0b4`). N1 = O-A node 1 (`../oa-node1/NODE.md`, with its review outcome). XS, MI+, SC =
`REPORT.md`, `mi-plus/{PREREG,RESULT}.md`, `source-search-20261020/SOURCE-CHECKPOINT.md` on
`research/x-screen-20261018` @ `76383997`. PM = `premise-memo/PREMISE-MEMO.md` on `staging/premise-memo-864-20261018`
@ `641ae161`. H = thread H @ `804843f1`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (two runs, byte-identical);
[UP] unsourced premise; [L] literature; [rec] recorded in the cited record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "no listed condition
supplies O-A/O-B" and either constrains the form the missing component must take or exposes a hidden assumption.

**Productivity test for node 1b (fixed before node 1b, §9).** Node 1b is productive iff it yields a fact strictly stronger
than "the phase no-go holds for deterministic channels", and does either of the following:
- (a) states the exact protocol class each phase claim covers (ancillas, feed-forward, discard, coarse-graining,
  heralding, postselection, limits), with a proof or an exact computation for each case;
- (b) determines what TU plus heralding supplies relative to the A1 endpoint, through the kernel's availability
  notions.

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
  - A replace-by-ψ channel satisfies it exactly when ⟨1|ψ⟩ ≠ 0 (review B4, B5). This is why |+i⟩ is deterministically reachable and |−⟩
    is not.
- `instAvail_unitary_fixes_ones` (:398) then gives: **every unitary conjugation that the TU-extended theory makes
  available as a one-outcome family, i.e. a deterministic trace-preserving channel, fixes the all-ones ray.**
  - Scope (§9.1): finite protocols with configuration and TU-prepared ancillas, classical feed-forward, discard and
    coarse-graining.
  - It says nothing about individual branches of multi-outcome instruments. Heralded and postselected branches lie
    outside it, and so do limits of channels.
  - T2 is a statement about finite protocols and is not limit-stable. `OnesNormal` is not closed under channel limits:
    the finite repeat-until-success channels Φ_n are `OnesNormal`, and their limit Ad Z is not (§9.2 item 1).
- Consequences:
  - The quarter phase S and the sign Z are unavailable *as deterministic channels*, so the theory is not QM on any
    carrier with ≥ 2 states. The endpoint asks for every one-outcome Kraus instrument (§9.2), and the argument is that
    of `onesTheory_not_phasesAvailable` (FlowEndpoint.lean:177).
  - An instrument with an exact Z branch *is* available, and so is a heralded |−⟩ preparation with p = 1/2 (§9.1(b)).
  - Relative to `SourcedOI`, the phase-free driven transition that `sourcedOI_qm_iff_phaseFree` requires moves the ray
    (`onesTheory_not_phaseFree` :142), so TU cannot supply it as a deterministic channel either.
  - No state with zero uniform weight (e.g. |−⟩) can be prepared *deterministically* from configuration states.

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

**T4. The deterministic sign Z completes TU [EC C1–C3 for single-token relations; L for registers; W for QM].**
The sufficiency is shown for the deterministic Z channel, or for a deterministic |−⟩ preparation through B7, and for
nothing else. Other uniform-ray breakers, and heralded Z, are not shown to complete TU exactly (§9.1(c)).
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
3. *Incompleteness.* By T2, no finite TU protocol realizes a ray-moving unitary as a deterministic channel. TU does give
   an exact Z on a heralded branch, and channels within Choi distance 2^{−n} of Z (§9.1). Under A1 exactness it therefore
   cannot be the whole missing component.
4. *Knobs, and the source of the continuum.* The flow is realizable *given* TU, but OI does not supply TU.
   - OI's measurement is conditioning on a visible configuration (Main.md:632).
   - The non-configuration bases and their continuous real parameter are posited by TU and are themselves unsourced.
   - T1 uses a one-parameter real family plus the Y basis. Choosing that family is a G7 question.
5. *O-B.* A local Lüders filter maps every domain cone into SEP ⊆ K: for X ∈ maxCone, (P_v⊗I)X(P_v⊗I) = |v⟩⟨v| ⊗ (a PSD
   conditional) [W]. TU's own pair-level compatibility is therefore automatic. Preservation of K by the TU-generated
   flow reduces to ATT, NC₃ for the CNOT ancilla→data, a non-configuration RO₃ and DIS. These are Σ3-type clauses
   (LG §4), unsourced, in agreement with AW-F1 [W]. TU does not source O-B.

**Verdict (by the rule).** TU is a *partial* O-A source.
- It supplies (a), the non-monomial continuum (the layer flow), exactly. The basis continuum it uses is posited, not
  sourced.
- It does not supply (b) as a deterministic channel, by the invariant `OnesNormal`. Within the protocol class of §9.1(a)
  no finite protocol realizes Z, S or another ray-moving unitary deterministically.
- It does supply (b) in two weaker forms: as an exact heralded branch of a complete instrument, and as a limit of
  channels. A1 counts neither (§9.2).
- It is non-supervenient and does not source O-B, which stays open.

Measurement in the von Neumann–Lüders sense is therefore not the missing component *at the A1 endpoint*, under any
availability strengthening whose primitives are `OnesNormal` over the ones-fixing native class. That scope covers sharp
tests in every basis and generic unsharp Lüders updates.

***

## 4. The logical form the missing component must have

From CR, T2 and T4, any extension yielding exact QM on qubit-power registers from OI's native class needs:

1. **Non-supervenience** (CR): some available primitive is not a function of an implementing substratum process plus
   countable context, or else the substratum is enlarged.
2. **A non-`OnesNormal` primitive** (T2), or else an operational-completion rule admitting limits such as
   almost-surely terminating protocols (§9.3). One of these is needed for a *deterministic* ray-moving channel at A1
   exactness, with availability generated by finite protocols. Heralded branches and channel approximants need
   neither (§9.1). Each non-`OnesNormal` primitive is one of:
   - (i) an admissible isometry that moves the all-ones ray, a phase-type operation;
   - (ii) a preparation of non-uniform weight, e.g. |−⟩, whose ω = ⟨1|·⟩ differs from that of configuration states;
   - (iii) more generally, any primitive family {K_j} with 1 ∉ span{K_jᴴ1}, such as Z or a deterministic preparation
     of |−⟩. Generic unsharp Lüders updates are not in this class (T2).
   Given TU, a deterministic Z channel suffices, or equivalently a deterministic |−⟩ preparation (T4). This is shown for
   Z only.
3. **An uncountable non-monomial family** (A1 with `countable_not_pairFlowSourced` PairFlowEquivalence.lean:218):
   either a continuous operation family or, equivalently for this purpose, a continuum of sharp Lüders test bases (T1).
   In the second form, the bases and their parameter are themselves an unsourced posit.
4. **O-B**:
   - the fixed identification G3: native operations act by Ad_P, and a TU branch acts by Ad_{P_v};
   - compatibility clauses reaching three tokens (AW-F1), since TU's pair-level compatibility is automatic and excludes
     nothing (§3 item 5).

In the kernel's own split (GR.md:266–272: phase intervention plus layer flow), TU can stand in for the layer flow. It
supplies the phase intervention only in heralded or approximate form, never as the deterministic channel that
`PhasesAvailable` (RouteB.lean:128) asks for. Relative to `SourcedOI`, where no phase is assumed, the two are fused in
the phase-free rotation, and no `OnesNormal` measurement condition reaches it as a deterministic channel.

**Controls any candidate must preserve, fixed in advance (§A.29).**
- (1) `permTheory_not_qm` and the monomial class (`substratum_residual` StructuralClosure.lean:383) stay non-QM when the
  extension is removed.
- (2) The rooted law (`finiteRootedRealizable_iff_pper`) is unchanged for native protocols.
- (3) M1 on retained protocols: TU and sign primitives add protocols and leave native ones unchanged.
- (4) Must-fail: preparations alone give no coherent control (LG §3).
- (5) Must-fail, new: sharp measurements alone give no deterministic ray-moving channel by finite protocols (T2). This
  is not a must-fail for heralded branches (§9.1(b)).
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
| HA-M1 | the barrier against coherent control is "configuration readout" | LG §3 monomial lemma; `InstAvail` readout constructor | **exposed.** The configuration restriction is load-bearing only for monomiality, the continuum part. The phase part rests on completeness Σ P_k = 1 together with ones-fixing isometries, which survive any sharp basis for deterministic channels (T2; heralded branches excepted, §9.1) |
| HA-M2 | O-A is one premise | LG §3, §5; N1 | **CONFIRMING, not exposed.** The split into a uniform-ray breaker and a continuum is already in the records: LG:346; H:42 and :245–250 (I3 = `OnesFixing`, E4); I:263–271 and :531; and the kernel pattern `onesTheory_layerFlowExecutable` FlowEndpoint.lean:87 with `onesTheory_not_phasesAvailable` :177, into which TU embeds. The node adds that, given TU, a single sign suffices |
| HA-M3 | "valid measurements" and "nonclassical operations" are separate F2 targets | RM:1125–1127 | with native multi-token protocols, tests carry operation content (T1), and full control implies TU (T4). The targets are not independent |
| HA-M4 | measurement content is the effect (test) | MI+, PM OVc/MEV | the Lüders post-measurement state is load-bearing (T5). Coherent effects and coherent post-measurement states are needed together |
| HA-M5 | deterministic exactness needs feed-forward | GR.md:216 (outcome-conditioned composition) | admitted by the operational-theory definition; not hidden |
| HA-M6 | sharp Lüders form | `readout_is_localLuders` forces it for sharp native readout only | not load-bearing for T2. Generic unsharp Lüders updates are `OnesNormal` (review B1, B2). The open class is primitives with 1 ∉ span{K_jᴴ1} (§4 2(iii)); which non-Lüders updates fall in it is not classified [U] |
| HA-M7 | the finite-substratum obstruction applies to OI | Main.md:538 | it binds a fixed carrier. OI grows carriers per experiment, so CR is the operative obstruction |

Assumption-watch markers:
- **AW-MC1.** `OnesNormal` survives sharp Lüders measurement in every basis.
  - A claim that measurement supplies *deterministic* phases, or dense unitary control in the operator-norm sense of
    `DenseUnitaryControl`, must name its non-`OnesNormal` primitive.
  - Heralded phase branches and channel-metric approximation need none.
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
- Node 1b items are [W]:
  - the widened `InstAvail` class of §9.1(a) is not formalized;
  - the diamond-distance equality in §9.1(c) is not computed (the Choi value is);
  - `KrausDense` for the TU theory is not checked;
  - the QMfin failure at m = 1 is read from the definitions.
- `chan_solver.py` uses Pauli bases and affine permutations only. Its negative rows are consistency checks of (a), not
  evidence for it.
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
| `heralded.py` | `ed4cd81c…9845` | node 1b: heralded Z, repeat-until-success (n ≤ 4), operator-norm bound; 25 checks |
| `heralded.run1.out`, `.run2.out` | `01088fda…09db` (both) | 25 PASS |
| `chan_solver.py` | `5ae13603…0684` | node 1b: AND-OR search for deterministic data channels under heralding and feed-forward |
| `chan_solver.run1.out`, `.run2.out` | `9f7c39f4…091e` (both) | 8 PASS |
| `rus_limit.py` | `dd1d225e…1ad2` | node 1b: Φ_n, the limit Ad Z, the three invariants; 16 checks |
| `rus_limit.run1.out`, `.run2.out` | `04ec6c80…740c` (both) | 16 PASS |

Full digests are in `probe/SHA256SUMS`; the review files and their digests are in `probe/review/`.

***

## 8. Productivity verdict

**Gem: yes.** The node yields three facts strictly stronger than "no listed condition supplies O-A/O-B":
1. Granting the strongest measurement-availability condition (TU), even non-supervenient and uncountable, does not
   supply the uniform-ray part of O-A as a deterministic channel. Every unitary available as a one-outcome family stays
   ones-fixing [W from AT; EC]. Heralded branches are not covered (§9).
2. TU supplies exactly the other part, the layer flow that GR.md:272 records as unsourced, deterministically
   and exactly [EC].
3. Given TU, the residue is one non-`OnesNormal` primitive, and a deterministic Z suffices (shown for Z only). The evidence is [EC] for
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
> they supply no deterministic, trace-preserving operation that breaks the uniform ray. Heralded instruments can
> carry an exact Z branch.

**Classification (as corrected by the independent review): NEW (narrow).** The new content is the gadget direction
"Lüders tests ⟹ layer flow" and the ledger correction F4. Everything else is ELABORATING or CONFIRMING:
- the invariant is the kernel's own (`instAvail_onesNormal`), and its transfer to arbitrary projectors runs inside
  `onesClass`;
- the phase/layer-flow split is already recorded (HA-M2);
- the one-bit teleportation gadgets are standard [L: Zhou–Leung–Chuang 2000; Nielsen 2003].

Answer to the owner's question, as scoped in §9:
- The act of measurement, in every native form, adds no operation.
- In its only non-native form (TU) it supplies one half of O-A, the continuum, from a posited basis continuum.
- It provably does not supply the other half, the uniform-ray breaker, as a deterministic channel by finite protocols.
- It does supply that half as a heralded exact branch and as a channel limit, neither of which meets A1.
- It does not source O-B.

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

***

## 9. Node 1b: scope of the phase no-go

**Trigger (owner review of PR #885 at `5de64a1a`).**
- A Lüders X-test on |0⟩ yields |−⟩ with p = 1/2, heralded.
- A CNOT from the data into that ancilla applies Z to the data.
- Repeating with a fresh ancilla until success terminates with probability 1, and every terminating run applies exactly
  Z.
- So a statement that measurement never supplies a phase cannot be unrestricted. T2 concerns one-outcome families
  generated by finite protocols. This section separates the three notions in play and gives each its own exact
  statement. The productivity test is fixed at the head of the file.

### 9.1 Three notions, kept apart (the decisive outcome)

**(i) A heralded operation: exact Z on the success branch [EC `heralded.py` b1–b8].**
- The X-test on |0⟩ gives |−⟩ with p = 1/2 (b1).
- The heralded-Z instrument is: attach |0⟩, X-test, CNOT data→ancilla on outcome −, discard. Then:
  - its success branch is exactly ½ ZρZ, with every success Kraus operator ∝ Z (b2, b3);
  - its failure branch is ½ ρ (b4);
  - it is complete (b5) and `OnesNormal` as a whole (b6), so the TU theory makes it available as a two-outcome family;
  - its Z branch alone is not `OnesNormal`-compatible (b7), and coarse-graining the herald gives dephasing, not Z (b8).
- A postselected Z, with the branch renormalized and kept as a one-outcome family, is not a kernel availability
  operation:
  - `FiniteOperationalTheory` (OperationalAssembly.lean:594) is closed under coarse-graining (`avail_coarse` :604);
  - `InstAvail` has no sum and no outcome-selection constructor (docstring at ImplementationLocality.lean:260–267).

**(ii) An almost-surely terminating unbounded protocol. It defines Ad Z exactly as a limit, and it is not a finite
protocol [EC `rus_limit.py` L1–L6, `heralded.py` c1–c4].**
- Truncating at depth n, and doing nothing after n failures, gives the complete channel
  Φ_n(ρ) = (1 − 2^{−n}) ZρZ + 2^{−n} ρ:
  - the protocol's own Kraus list gives it (c.1);
  - its Kraus form is {√(1−2^{−n}) Z, √(2^{−n}) I} (L1);
  - its failure probability is 2^{−n} (c.2);
  - its Choi trace distance to Ad Z is exactly 2^{−n} (c.4).
- The unbounded protocol terminates with probability 1, after 2 attempts on average (L6). Every terminating run applies
  exactly Z (b3). Its channel is lim Φ_n = Ad Z exactly (L4).
- **`OnesNormal` holds for every Φ_n.** The definition (InstrumentRealization.lean:172) asks for a finite Kraus list
  with F = Σ conj K_i and Σ K_iᴴ1 = 1. No weights enter it; `splitWeight` is internal to the discard case of
  `instAvail_onesNormal`.
  - The decomposition {√p I, ±√((1−p)/2) Z}, with p = 2^{−n}, reproduces Φ_n and is complete. The Z pair cancels in
    Σ Kᴴ1, but the sum is √p·1 ≠ 1 (M1). The normalization has to be fixed by splitting the identity branch.
  - Fixed decomposition: 2^n copies of 2^{−n} I, plus the pair ±√((1−2^{−n})/2) Z. It reproduces Φ_n, is complete, and
    has Σ Kᴴ1 = 1 (M2, n = 1–6). The protocol's own Kraus list also works (c.3, n ≤ 4).
  - Exactly 2^n Kraus operators are needed and suffice [W + EC].
    - Every Kraus operator of Φ_n is α_j I + β_j Z. The four maps ρ ↦ AρBᴴ with A, B ∈ {I, Z} are linearly independent
      (rank 4; review ii5), so the coefficient relations Σ|α_j|² = 2^{−n}, Σ|β_j|² = 1 − 2^{−n} and Σ α_j β̄_j = 0 are
      fixed.
    - The Z parts contribute only multiples of (1, −1), so Σ ᾱ_j = 1. Cauchy–Schwarz then gives m ≥ 2^n (M3).
    - Exactly 2^n operators suffice (review ii6; n = 2: ¼I ± √(3/8) Z, ¼I, ¼I). The 2^n + 2 list of M2 is valid but
      not minimal.
- **`OnesNormal` fails for the limit.** Every Kraus operator of the unitary channel Ad Z is c_j Z, and 1 ∉ span{Zᴴ1}
  = span{(1, −1)} (L3).
- **So `OnesNormal` is not closed under channel limits (L5).** The minimal decomposition size, exactly 2^n, diverges
  along the sequence.
- The kernel already records this pattern for its own repeat-until-success construction:
  - BridgeFiniteProtocol.lean:6–7: "Every finite depth is available from these primitive resources, rather than assumed
    as a whole approximation sequence";
  - :9–10: "No limiting-channel availability … is established by these theorems";
  - `instAvail_stopped` :63, `finite_protocol_available` :236, and `balanced_stopped_formula` :245, which gives
    (1 − (3/8)^k) Ad drivePhase + (3/8)^k id at every finite depth k. That construction assumes its circuit and Z-type
    corrections are admissible (`balanced_finite_available` :256).

**(iii) An operation admitted by `InstAvail`. Finite protocols only, so Ad Z is not available [W from AT; EC].**
- *Class.* The constructors of `InstAvail` (ImplementationLocality.lean:268) over `onesClass`, with the readout
  constructor widened to any complete orthogonal projective family (§3 T2):
  - `op`: ones-fixing isometries, including the native permutations and the gate flows;
  - `readout`: configuration or TU bases;
  - `coarse`;
  - `bind`: classical feed-forward, native corrections included;
  - `discard`: configuration ancillas are derived from it, and TU-prepared ancillas are sub-protocols.
- *Read as* one-outcome families, i.e. total trace-preserving channels.
- *Proof.*
  - Every generated family is `OnesNormal` (`instAvail_onesNormal` InstrumentRealization.lean:313, readout case
    widened).
  - A unitary channel in the class fixes the all-ones ray (`instAvail_unitary_fixes_ones` :398).
  - Ad Z, Ad S and every other ray-moving unitary channel are therefore not available.
  - A deterministic |−⟩ preparation has every Kraus operator of the form |−⟩⟨u|, so Kᴴ1 = 0. It is not `OnesNormal`
    (review B4) and not available.
- *Heralding and feed-forward do not evade this.* Any finite tree of heralds and feed-forward is a `bind`/`coarse`
  composite, and its total channel is `OnesNormal`.
- *Exact consistency checks.*
  - `chan_solver.py` searches Pauli Lüders tests on any token, affine permutations and feed-forward of unbounded depth.
    It finds no deterministic Z or S at n = 2 (912 operator states) or n = 3 (34 032), both full graphs.
  - It finds the positive controls: I, X, R_x(π/2) (the TU gadget), and Z from an ancilla started in |−⟩.
  - `run_solver.py` finds no deterministic |−⟩.
  - These are checks of (iii), not evidence for it: Pauli bases only.

**NonnegBounded along the sequence [EC L7–L9].**
- The coefficient of ρ₀₁ in Φ_n(ρ) is 2^{1−n} − 1 (L7). Φ_1 preserves entrywise nonnegativity on |+⟩⟨+|; every Φ_n with
  n ≥ 2 breaks it (L8), and so does the limit (L9).
- Entrywise nonnegativity is limit-closed: along unitary limits by `preservesNonneg_of_approx` (FrozenSourcing.lean:127),
  and along channel limits [W]. The native theory satisfies it (`obsTheory_nonnegBounded` :84). No native protocol
  reaches Φ_n (n ≥ 2), and no limit of native protocols reaches Ad Z (§9.2 item 3).
- Φ_n becomes available only through TU's non-native X-test. Once TU is admitted, `NonnegBounded` is already broken by TU
  branches themselves, and the barrier left at finite depth is `OnesNormal`, the one invariant that is not
  limit-closed.

**Main result of node 1b.** Measurement plus unbounded repetition produces the exact phase channel Ad Z
mathematically: an X-test on |0⟩, kickback, and repeat until success give Ad Z as the almost-sure limit (L4, L6).
- It is not an operation that finite `InstAvail` admits: limiting-channel availability is left unestablished
  (BridgeFiniteProtocol.lean:9–10).
- Its construction relies on non-configuration measurements that native OI does not supply.
- OI still has to justify the required measurements, and any operational-completion rule that admits the limit.

### 9.2 Three invariants, named separately

Each statement below concerns one named invariant. No statement here is about "the barrier invariants" as a group.

**1. `OnesNormal`** (InstrumentRealization.lean:172; existential over finite Kraus decompositions, Σ K_iᴴ1 = 1).
- It holds for every Φ_n (M2) and fails for Ad Z (L3). **Not closed under channel limits** (L5, M3).
- T2 and §9.1 (iii) are therefore statements about finite protocols. They are not limit-stable.

**2. Fixing the uniform pure state**, Φ(|u⟩⟨u|) = |u⟩⟨u| with u = 1/√N. **Native readout does not satisfy it, so it is
not a barrier.**
- Coarse-grained configuration readout sends |u⟩⟨u| to I/2 while satisfying `OnesNormal` (review u2, u3). The
  condition is therefore not an invariant of the native theory, and it bars nothing that native OI cannot already do.
- It is a closed condition under channel limits [W: one linear equation in Φ].
- Φ_n fails it for every n ≥ 1: Φ_n(|u⟩⟨u|) = (1 − 2^{−n})|−⟩⟨−| + 2^{−n}|u⟩⟨u| (U1). Ad Z fails it as well (U2).
- **`OnesNormal` is strictly weaker.**
  - Fixing |u⟩⟨u| implies `OnesNormal` [W]. If Φ fixes |u⟩⟨u|, every Kraus operator satisfies K_j u = λ_j u, so
    u = Σ_j K_jᴴK_j u = Σ_j λ_j K_jᴴu, and 1 ∈ span{K_jᴴ1}. Exact instances: U3. The step from the span criterion to a
    decomposition uses splitting (review B1, B2; M2 here).
  - Φ_n is `OnesNormal` and does not fix |u⟩⟨u|.
  - The identity branch restores the `OnesNormal` sum, but it does not make the channel preserve what the Z branch
    violates.
- *Kernel relation.* For unitary channels the two coincide. `instAvail_unitary_fixes_ones` (:398) derives "U fixes the
  all-ones ray" from `OnesNormal` of an available unitary conjugation. Every Kraus operator of Ad U is ∝ U
  (`kraus_of_conj_unitary` MicroscopicReversibility.lean:189), which forces Uᴴ1 ∝ 1. Conversely, a ray-fixing unitary
  rescaled by its eigenvalue (the `op` case of :313) satisfies the sum.

**3. Entrywise nonnegativity** (`PreservesNonneg`; `NonnegBounded` FrozenSourcing.lean:65 for theories).
- The kernel's limit statement is `preservesNonneg_of_approx` (FrozenSourcing.lean:127). Its hypotheses: U is unitary,
  and for every ε > 0 there is a unitary W with `PreservesNonneg (conjChannel W)` and ‖U − W‖ < ε (operator norm).
  Its conclusion: `PreservesNonneg (conjChannel U)`.
- That is closure along unitary limits. Closure under general pointwise channel limits also holds, since the condition
  is a closed cone condition [W], but it is not the kernel statement.
- Φ_2 already violates it at finite depth: Φ_2([[1,1],[1,1]]) = [[1, −½], [−½, 1]] (N1). In general the off-diagonal
  coefficient is 2^{1−n} − 1, negative from n = 2 (L7, L8).
- So `NonnegBounded` stays a valid barrier for the native sourced theory. The RUS channels are excluded by it at
  finite depth, because they need TU's non-native tests.

| invariant | closed under limits? | Φ_n (finite n) | Ad Z (limit) |
|---|---|---|---|
| `OnesNormal` | **no** (channel limits) | holds (M2) | fails (L3) |
| fixing the uniform state (not satisfied by native readout; not a barrier) | yes [W] | fails, n ≥ 1 (U1) | fails (U2) |
| entrywise nonnegativity | yes: unitary limits (`preservesNonneg_of_approx` :127); channel limits [W] | fails, n ≥ 2 (N1, L8) | fails (L9) |
| ones-fixing of unitaries (K1 = z1) | yes, operator-norm limits (H:42 [W, rec]) | not a unitary | fails |

Operator-norm density fails for the TU theory, sharply. For every ones-fixing unitary V (Vu = zu, |z| = 1) and unit
scalar c, ‖(Z − cV)u‖² = 1 + |cz|² = 2, since Zu ⊥ u. So ‖Z − cV‖ ≥ √2.
- `heralded.py` d1 checks the identity |(Z − cV)1|² = 2 + 2|w|²; |w| = 1 then gives √2. The review's d1 checks the
  sharp form.
- So `DenseUnitaryControl` (DiscreteCompletion.lean:45) fails for the TU theory, whatever else holds [W]. Whether
  channel-metric density holds is open (§9.6).

**Corrected wording for oa-node1's route-table row R1** (`../oa-node1/NODE.md`, R1, "decisive obstruction" column):

> A1 + countability: `countable_not_pairFlowSourced`, `mixTheoryR_not_qm`, `fixedGateTheory_not_qm`,
> `uncountable_of_layerFlowExecutable`. Two invariants are closed under limits, each under its stated hypotheses:
> - entrywise nonnegativity of unitary conjugations: if U is unitary and is approximated in operator norm by unitaries
>   whose conjugations preserve nonnegativity, its conjugation preserves nonnegativity (`preservesNonneg_of_approx`
>   FrozenSourcing.lean:127);
> - ones-fixing of unitaries, which is closed under operator-norm limits (H:42 [W]).
> The protocol invariant `OnesNormal` is not closed under channel limits: the finite repeat-until-success channels
> built from non-configuration Lüders tests are `OnesNormal` and converge to Ad Z, which is not (`mc-node1` §9.2).

The "level" column becomes "closed-K for availability; the limit-invariance step is [W] except for the kernel statement
`preservesNonneg_of_approx`". R1's conclusion for the native class is unchanged: the native theory is `NonnegBounded`,
and nonnegativity is limit-closed.

### 9.3 The limit against the existing records

- **AW-X4** (XS REPORT:157): "exactness is asymmetric — closure is free for preservation, but countability theorems [AT]
  block it for availability".
  - For a single target channel such as Ad Z, countability blocks nothing: the approximants are countable and so is
    the target.
  - What blocks Ad Z is the finite-protocol generation of availability (`InstAvail`; BridgeFiniteProtocol.lean:9–10).
  - AW-X4 is accurate for uncountable target families (flows), and needs this qualification for single limiting
    channels.
- **XS gate ambiguity** (REPORT, "Gate ambiguities"): "A1 vs limit closure: treated as the dense endpoint relabelled; not
  admitted". Intake R5 bars limit closure as a standalone X. R5's G4 invariants are `NonnegBounded`, the uniform ray for
  unitaries, and reality. They are limit-closed, and `OnesNormal` was never on R5's list. This node therefore qualifies
  R5's parenthetical; it does not correct it.
- **F2 memo §1.1**: A1 exact means `QMfin` = `ShadowQuantum`, characterized by `typed_determined_iff`
  (TypedCompletion.lean:850). A2 dense needs an endpoint defined first, and exists only on `Fin 2` (`DenseFiniteQM`
  DiscreteCompletion.lean:59).

**Does an RUS-closure rule count as A1 exact availability, or as the barred limit closure?** From the definitions:
1. A1 asks that the theory's availability predicate be exactly the Kraus instruments for every outcome count m,
   including m = 1 (`ExactFiniteEndomorphicQuantumOps` KrausSoundness.lean:134 with :112; `ExactCompositeQuantumOps`
   AncillaClosure.lean:364).
2. In the F2 setting that predicate is generated by `InstAvail`'s five finite constructors. The kernel's bridge
   establishes every finite stopping depth and no limiting channel (BridgeFiniteProtocol.lean:6–10).
3. The channel of an almost-surely terminating unbounded protocol is lim_n Φ_n, a limiting channel. No finite
   composition of the five constructors yields it (§9.1 (iii)).

An RUS-closure rule is therefore a new closure rule on availability. It is a restricted form of limit closure: only
limits along one protocol tree whose unfinished weight tends to 0. It is not A1 availability as currently defined.
- Under the adopted gates it falls under "A1 vs limit closure: not admitted", unless the owner rules separately on a
  restricted, almost-sure-termination closure.
- That ruling would be a target-definition decision, fixed before screening (G8).
- It differs from the full dense endpoint in kind. With TU it would give the exact channel Ad Z, not merely
  approximants. So it is not "the dense endpoint relabelled" in the sense of approximation.
- Whether it keeps CR's countability is not examined. Infinite adaptive trees over a countable alphabet form an
  uncountable set, so CR does not apply to it automatically [W].

### 9.4 What the endpoint asks for, and what TU with heralding supplies

- `typed_determined_iff` (TypedCompletion.lean:850) and `ExactFiniteEndomorphicQuantumOps` require, at m = 1, the
  one-outcome family {Ad Z}. `PhasesAvailable` (RouteB.lean:128) asks for `availExt n Unit (conjChannel (phaseGate a))`.
- **The endpoint requires the deterministic Z channel, not an instrument containing a Z branch.**
- Relative to it, TU with heralding supplies, all inside `InstAvail`:
  - the layer flow exactly as a deterministic channel (T1);
  - every heralded instrument built from TU tests, exactly, including heralded Z and heralded |−⟩;
  - channels within 2^{−n} of Ad Z.
- It does not supply the one-outcome Ad Z or Ad S families. So `ExactFiniteEndomorphicQuantumOps` fails at m = 1, and
  QMfin fails [W from the definitions and T2].
- The basis continuum that TU uses is posited, not sourced. O-B stays open.

### 9.5 Proposed replacement texts

**(i) PLAN.md, Status, the `mc-node1/` bullets** (final; replacing the bullets from "No `OnesNormal` primitive breaks
the uniform ray" through "O-B is not sourced"):

> - Three notions are kept apart:
>   - Heralded: the tests give an exact Z on a heralded branch. An X-test on |0⟩ yields |−⟩ with probability 1/2,
>     then kickback.
>   - Almost surely terminating: repeating until success terminates with probability 1 and defines Ad Z exactly, but
>     only as the limit of the finite-depth channels Φ_n = (1 − 2^−n) Ad Z + 2^−n id.
>   - Finite protocols: finite `InstAvail` protocols built from primitives satisfying `OnesNormal` (generic unsharp
>     Lüders instruments included) yield no deterministic ray-moving unitary channel and no deterministic |−⟩.
> - Every Φ_n is `OnesNormal` and Ad Z is not, so `OnesNormal` is not closed under channel limits. The cost is exactly
>   2^n Kraus operators at depth n. Entrywise nonnegativity of unitary conjugations is limit-closed
>   (`preservesNonneg_of_approx`), and Φ_n already violates nonnegativity from n = 2. Only non-native tests make Φ_n
>   available at all.
> - The A1 endpoint requires the deterministic Ad Z channel. Admitting almost-surely terminating protocols would be a
>   restricted limit-closure rule, which the adopted gates do not admit without a separate owner ruling. Whether TU
>   meets the existing A2 endpoint (`KrausDense`, `DenseFiniteQM`) is open.
> - The continuum of measurement bases that makes the layer flow exact is itself unsourced: OI's readout is
>   configuration readout, and the bases are posited.
> - Adding the deterministic Ad Z channel to these tests gives full control on qubit registers. This is shown for Z
>   only, and the register step rests on Barenco et al. [L] and a written argument [W].
> - O-B is not sourced and stays open.

The "Form the missing component must take" bullet becomes (final):

> - It includes a primitive outside `OnesNormal`, such as a phase-type isometry or a deterministic preparation of |−⟩,
>   or else a rule admitting almost-surely terminating protocols. This is needed for a deterministic phase at A1
>   exactness; heralded phase branches need neither.

**(ii) F2 ledger §5 item 2, the monomial-lemma bullet** (final; replacing LEDGER.md:352–355 at `ab25f17a`):

> - The monomial lemma is a must-fail control: a construction that adds only preparations to the native class, with
>   configuration readouts as the only instruments, does not qualify. Non-configuration sharp instruments with the
>   Lüders update fall outside the lemma. They make the layer flow executable exactly, but stay within the invariant
>   `OnesNormal`. So in finite protocols (ancillas, feed-forward, discard, coarse-graining) they yield no deterministic
>   unitary channel that moves the uniform ray, and no deterministic preparation of a state orthogonal to the uniform
>   vector. They do yield an exact Z on a heralded branch, and Ad Z as the limit of almost-surely terminating
>   repeat-until-success protocols. The A1 endpoint counts neither (missing-component node `mc-node1`, PR #885).

**(iii) oa-node1, route-table row R1:** the final wording is in §9.2.

### 9.6 The question this opens for step 2 (not answered here)

Is there an operational-completion rule justified by OI itself that admits the limiting phase operation? One example
is almost-sure termination of protocols the observer can run. Such a rule would have to:
- supply Ad Z (or another uniform-ray breaker) without positing Z;
- pass G2 sourcing;
- explain the continuum of measurement choices that TU posits;
- keep the countercontrols: `permTheory` and the monomial class non-QM, and K_B, K(Z_F) and Γ(Q3) excluded;
- address O-B.

**Open question for step 2 (A2).**
- Does `KrausDense` (DiscreteCompletion.lean:52) hold for TU on qubit registers? It looks likely: Φ_n → Ad Z in the
  channel metric, with trace distance 2^{−n}, and T4's construction with Φ_n in place of the exact Z would approximate
  every instrument. This is not checked.
- If it holds, `DenseFiniteQM` (:59) may hold for TU. The phase gap would then exist only at A1, and vanish at the
  existing A2 endpoint.
- `DenseUnitaryControl` fails for TU regardless (‖Z − cV‖ ≥ √2, §9.2).

### 9.7 Productivity verdict (node 1b)

**Productive: yes**, under the test fixed above.
- (a) Each phase claim now carries an exact protocol class, with a proof or computation for every case: heralded
  branches (i), almost-surely terminating protocols (ii), and finite `InstAvail` protocols with heralding and
  feed-forward (iii).
- (b) The endpoint asks for the one-outcome Ad Z. TU with heralding supplies heralded exact Z and the finite channels
  Φ_n, and it reaches Ad Z only through a limit that `InstAvail` and A1 do not admit.
- The fact strictly stronger than "the no-go holds for deterministic channels" is the three-way distinction of §9.2:
  - `OnesNormal` is not closed under channel limits (M2, L3), at a cost of exactly 2^n Kraus operators at depth n (M3,
    review ii5–ii6);
  - fixing the uniform state is limit-closed and fails at every finite n (U1), but native readout fails it as well, so
    it is not a barrier;
  - entrywise nonnegativity is limit-closed (`preservesNonneg_of_approx` along unitary limits; channel limits [W]) and
    fails from n = 2 (N1).
  - TU's phase gap is therefore a finite-protocol exactness gap, not a countability gap.
- This qualifies the recorded claim that "the barrier invariants are closed under limits".
  - XS R5's invariants are limit-closed, and the claim concerns limit closure as a standalone X.
  - oa-node1's R1 row is reworded in §9.2.
  - AW-X4 is qualified for single limiting channels.

**Classification (node 1b): ELABORATING, with one NEW (narrow) item.** The new item is the non-closure of `OnesNormal`
under channel limits, with the three-way separation it forces. The finite-depth-available, limit-unestablished pattern
is CONFIRMING: the kernel's own bridge records it (BridgeFiniteProtocol.lean:6–10). The heralded-Z and RUS
constructions are elementary [L: standard repeat-until-success]. The node's overall classification stays **NEW
(narrow)**, with this item added. Not independently reviewed.

***

## Node 1b review outcome

Review: `probe/review1b/` (`rev_1b.py`, 19 PASS, its output and `SHA256SUMS`, copied unchanged from
the reviewer's working copy). The texts before node 1b and before its review are not kept here; their sha256 are
`079d6672b195a28c1d34c351a791fa6fba731303f488ad3f6a149b5888b7c9ed` and `c83d01e1f32e8e16ef743a5186723023264df97a60038444572e37197a07ea95`.

| item | verdict | applied as |
|---|---|---|
| (i) heralded Z | CONFIRMED | — |
| (ii) RUS limit | CONFIRMED | — |
| (iii) finite `InstAvail`, and the endpoint reading | CONFIRMED | — |
| `OnesNormal` non-closure | CONFIRMED | the minimum is exactly 2^n; the linear-independence step is cited (F6) |
| nonnegativity | CONFIRMED | — |
| RUS-closure as barred restricted limit closure | CONFIRMED | — |
| uniform-state fixing | CORRECTED | not satisfied by native readout, so not a barrier; removed from R1 and PLAN, labelled in the §9.2 table (F1) |
| ledger wording | CORRECTED | "no deterministic unitary channel that moves the uniform ray, and no deterministic preparation of a state orthogonal to the uniform vector" (F2) |
| PLAN finite-protocol bullet | CORRECTED | F3 wording |
| XS R5 | CORRECTED | "qualifies", not "corrects" (F4) |
| A2 and d1 | CORRECTED | the A2 question raised to §9.6; d1 sharpened to √2 (F5) |

**Final classification of node 1b: ELABORATING, with one NEW (narrow) item.** The item is the non-closure of
`OnesNormal` under channel limits, at a cost of 2^n Kraus operators at depth n. Combined with node 1's NEW (narrow)
gadget direction, mc-node1 overall stays **NEW (narrow)**.
