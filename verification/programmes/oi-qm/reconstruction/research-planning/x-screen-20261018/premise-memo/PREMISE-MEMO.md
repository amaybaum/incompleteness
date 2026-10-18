# Additional physical premise for quantum-compatible joint evolution: design memo

Design-only research memo for PR #864 (F2-reg physical-extension X screen). Consistency axis (§A.23). This memo
adopts no X, designates no F or E, and changes no status, theorem, ROADMAP entry or manuscript. It makes no commit,
push, probe or repository edit. Every claim below is relative to the alternatives named; none is a global minimality,
equivalence or impossibility claim.

**Base.** Tree `s1018/xop/wt` at `85e949ad583db593768b9bb399f7192e6c8d30ba` (PR #864 head), clean. D =
`verification/programmes/oi-qm/reconstruction/research-planning/x-screen-20261018/`. Lean paths are under
`verification/lean-mathlib/OIBridge/`.

**Records read.**
- `D/REPORT.md`, `D/op-fork/RESULT.md`, `D/mi-plus/PREREG.md`, `D/mi-plus/RESULT.md` and
  `D/mi-plus/amendments/A1-A2-sources.md`.
- The F2 decision memo at `acfef447` (§1–§4).
- The readout-as-interaction search: `s1018/ri-native/SEARCH-LEDGER.md`, `s1018/ri-review/REVIEW-SEARCH.md` and
  `s1018/ri-review/SEARCH-LEDGER.corrected.md`.
- At `1d4606b2`: #820 `physical-state-operation-compatibility/spectrality.md`, plus `bridge-compatibility-audit/`
  `result.md` and `source-assessment.md`.
- ROADMAP :1011–1019, :1044–1046 and :1088–1091; Main.md :600–602 and :628–632; GR.md :184–190.
- The kernel anchors cited inline, each grep-checked at the base.

**Tags.**
- [AT]: kernel theorem at the base.
- [EC]: exact computation.
  - [EC, rec] is recorded in the cited screen.
  - [EC, dc] is this memo's design-evidence check (below). It is not a probe of any screen and certifies no verdict.
- [W]: written argument. "[W, new]" marks an argument first made here and not yet reviewed.
- [W, rev] and [EC, rev]: a written argument or exact check from the independent review of this memo (PR #864
  comment 6254408285). They are cited from the review and not replayed here.
- [U]: unresolved.
- [I]: imported (literature or an external postulate).

**Design evidence (record only).**
- Script: `s1018/premise-memo/dc_premise.py`, sha256 `ce9971be4ae90f9c98f9f74df3902d65ce376e0eb4906ef21c19b60af68f357e`.
- Output: `dc.out`, sha256 `5cc79d31536d470363a028b51ea1e16be2174b43686e0eaee4b29b8720b577fe`.
- Runs: twice under `python3 -I -B` (SymPy, exact `Rational`/`I`), rc 0, byte-identical. 27 PASS, 0 FAIL; one
  countercontrol and one mutation are included.
- An earlier run had one FAIL, caused by a wrong expected formula: a spurious transpose in the pairing identity.
  Its output and script are kept in `run1-wrong-expected/` (output sha256 `8908337e…800ef`). The corrected check
  includes the wrong form as a mutation that must fail.

## 1. Question and scope

**Owner's question.** What is the weakest independently meaningful additional physical premise that could
distinguish quantum-compatible joint evolution from its nonquantum alternatives, while retaining native OI readout
and M1?

**Domain and fixed identification.**
- Pair cones K with SEP ⊆ K ⊆ maxCone. These are the premises `hH1`, `hadd`, `hsmul` and `hmax` of
  `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153) [AT].
- Operations act on pair tables through the dictionary, for example `dict_cnot` (BridgeDictionary.lean:71) [AT].
- The test family is the product effects on `eball 3`. The native subfamily is the configuration effects.
- Under G3 the identification of operations and tests is the same for every cone: no re-identification under Γ.

**Alternatives.**
- Γ(Q3), the partial transpose on token 2 of Q3.
- K_B = SEP + ℝ₊B.
- K(Z_F) = (Q3 ∩ Z_F\*) + cone(Z_F).
- SEP.
- The classical diagonal cone, a positive control for the conditional mathematics only (memo §3.3).
- Diagnostics: L = Q3 ∩ Z_F\*, K_Γ = Q3 + ℝ₊Γ(B) and maxCone.

**Notation.**
- CN is the native read-write coupling: CNOT with control token 1 (`permClass_readWrite`
  SubstratumInterfaceAudit.lean:412 [AT]).
- P_k is the native configuration readout (`readout_is_localLuders` OperationalAssembly.lean:658 [AT]).
- Π_e and Π_o are the projectors onto span{|00⟩, |11⟩} and span{|01⟩, |10⟩}.
- cond_k(X) := Tr₂[(I⊗P_k) CN X CN] is token 1's conditional description after the coupling and the native
  readout k of token 2.
- T_X is the correlation matrix of normalized X, (T_X)_ij = Tr[(σ_i⊗σ_j)X].

**Three facts the analysis rests on.**
- **F-α.** Native statistics depend only on diagonals across `InstAvail permClass`. This is
  `realized_of_instAvail` (ImplementationLocality.lean:530) [AT] together with the trace identity of MI+ N3 [W, EC rec].
  Every domain cone has the classical diagonal set, and Γ fixes every diagonal.
- **F-β.** Γ(Q3) is invariant under every local unitary, native or not, continuous or not:
  Ad(U⊗V)∘Γ = Γ∘Ad(U⊗V̄) [W]. The set of token effects is closed under f ↦ fᵀ (the ball's y-reflection). So
  any clause over K's order, classical realization, native statistics, all local operations, or the product-test
  family taken as a set holds on Γ(Q3) iff it holds on Q3. Sources: review §1.4 and memo Fact B [W, EC rec].
- **F-γ.** On product tests Γ acts as a mirror reflection of token 2's ball (det −1; op-fork control C5 [EC rec]).
  It flips the sign of det T_X. The Γ ambiguity is therefore the relative orientation of the two token frames,
  which is visible only in joint coherences [W, new].
  - [EC, dc]: T(B) = diag(1, −1, 1), T(Γ(B)) = I and T(singlet) = −I.
  - The four K(Z_F) defects z = I/2 − P_m have orthogonal T with det +1, while each P_m has det −1. The K(Z_F)
    defects carry the same orientation defect as Γ(Q3), consistent with AW-X7 ("Γ-images of four entangled
    stabilizer projectors"). §A.31 class: ELABORATING (it extends AW-X7 and review §1.4).

**Not in scope.**
- The availability side of A1: the continuous resource that G4 requires.
- K-token composition.
- Any sufficiency claim beyond those labelled.

## 2. Premise inventory

Each premise has exactly one class, or is marked unresolved:
- **(i)** a new postulate;
- **(ii)** an existing OI consequence, with a citation;
- **(iii)** a compatibility restatement. This covers a membership "native coherent output ∈ K" (MI+ D2(a)/(b)) and
  PSD/CP on K by definition (D3). It also covers a transfer clause in the sense of F2 G2: preservation of physical
  states by named operations, or its dual, closure of a test family under pullback (F2 §2.2 Fact A, §2.3 G2, §2.4
  LO and DT).

A composite takes class (iii) if a load-bearing component is (iii). UPD is classified against the transfer-clause
form. OVr, whose basis is UPD's, is unresolved (U3). The other rows keep the class assigned against the membership
and PSD forms; their reading against the transfer-clause form is open (U3).

| id | premise, stated operationally | class | basis | source status |
|---|---|---|---|---|
| EA | **Independent fixing of the entangling action.** The native coupling acts on pair descriptions by the native conjugation Ad(P_CN) | (ii) | InstAvail `op` is `conjChannel` (ImplementationLocality.lean:271); `cp_of_instAvail` :541; `correlationExtension_ones_eq_conjChannel` SpectatorBridge.lean:282; `dict_cnot` [AT]. G3 fixes the identification for every cone | sourced on the matrix carrier. That physical pair descriptions transform this way is H-CAR [U]. It says nothing about K (§4) |
| PC | the native coupling maps physical pair states to physical pair states | (iii) | D2(b) known-answer (MI+ §5.2) | [U] |
| MI | the coupling of any token state to a ready meter yields a physical pair state; equivalently G := {Σ a_ij \|ii⟩⟨jj\| : a ⪰ 0} ⊆ K [EC, dc] | (iii) | D2(a)/(b) (MI+ §5.2; RESULT C0) | [U] |
| CPK | **CP / PSD-order bridge on system ⊗ ancilla**, as a clause on K: the composite with an ancilla is PSD, or K-maps are CP | (iii) | D3: presupposes PSD (MI+ A2 S14; S19/S20); review C4 | ROADMAP :1018–1019 records the bridge as open. CP is [AT] for native maps on the PSD carrier, and mentions no K |
| GRV | a Γ-covariant K-relative positivity or reversibility fork: every native bijection has some extension that classically realizes it and is K-positive (or a K-automorphism) | (i) | not in the corpus (review §1.4, §6 last row) | [U] |
| OI⁺1 | **OI⁺-1-type invariance.** Preservation of K by ball3Drive's flow plus the J-conjugate on one token (PT stage 6 missing assumption (b)) | (iii) | preservation (LO-type); fails the disguise test (REPORT R2; memo §2.4 H-OI_g/H-T) | [U] |
| SP | **Spectrality.** Every state lies in a frame of perfectly distinguishable pure states (Barnum–Müller–Ududec Postulate 1) | (i) | external postulate (#820) | [I]; no OI derivation |
| SP+Φ | spectrality plus preservation by the stopped maps Φ_k | (iii) | preservation component (SA LO) | SP ⇒ Φ_k preservation UNRESOLVED (memo §2.4) |
| OPw | OP-weak: purification existence plus relation-only uniqueness | (i) | Chiribella–D'Ariano–Perinotti [I]; Main.md:600 supplies the existence half at substratum level [MP] | uniqueness [U]; `fiber_freedom` threatens a substratum source |
| OPs | OP-strong: the relating map is a K-automorphism | (iii) | the automorphism clause is compatibility by definition; OP's exclusion power on K(Z_F) lies there (REPORT S1 G2, P3) | [U] |
| OPs⊕PC | the strongest composite (REPORT S3) | (iii) | OPs, PC | [U] |
| LT | **Local tomography / composition interface COMP-1.** Joint states are fixed by product statistics | (ii) | built into the domain coordinates: `lt` is a theorem of the coordinate model; laws hold for every body between the minimal and maximal (corrected ledger R17, review C7) | — |
| HC | **Spectator compositionality H_comp.** The coherent map of id_R × g is id_R ⊗ (that of g) | (i) | `HComp` MonoidalCompletion.lean:311 is a hypothesis (CP world) | [U] |
| GEO | **Sharp-update principle K∞-Geom.** The certain outcome of a proper sharp binary test identifies one state | (i) | ROADMAP :1044–1046, :1088–1091 | unproved, statement not frozen; no pair form (MI+ A1 S18) |
| DRV-a | **Continuity / drive, availability.** The local rotation flow `actT (rotLin t)` and `cycEquiv`, as available operations | (i) | E0 if posited as a resource (REPORT R1); A1 needs an uncountable resource | [U]; countable native classes fail (`countable_not_pairFlowSourced` etc.) |
| DRV-p | **Continuity / drive, preservation.** K is invariant under those flows (hA) | (iii) | LO-type preservation (SA :34–46) | [U] |
| SWP | **Factor exchange.** Native SWAP routes token structure across the cut | (ii) | SWAP ∈ permClass; `factorExchange_exposes_ancTranspose` FactorExchange.lean:140 [AT, conditional on KrausSound] | sourced (operation); its cone use is PC24-type |
| NST | native-statistics clauses: DIAG, RO, REC, NS, readback | (ii) | MI+ C1–C7, N2–N3 [W]; `recordInstr_apply` [AT]; F-α | — |
| SD | **Self-duality**, K = K\* under the trace pairing | (i) | Jordan route [I]; ROADMAP :1053–1056 names it as an unsourced alternative | [U] |
| **UPD** | **Update validity after native premeasurement.** For every physical pair state and each native readout outcome k of token 2 after the native coupling, token 1's conditional description cond_k(X) is a token state. Equivalent forms on the domain: Π_eXΠ_e ⪰ 0 and Π_oXΠ_o ⪰ 0 [EC, dc]; nonnegative probability for "coupling, native readout of the target, token test on the control" (test side). The protocol class is the native one: no local unitary precedes the coupling | (iii) | A transfer clause under F2 G2 [W, rev]. The state-side reading is preservation by one pair-to-token operation, which is compatibility (F2 §2.1). The test-side reading is closure of the product-test subfamily under pullback through CN, a restricted dual-test closure (DT). Unfolded, it requires PSD of the two parity compressions of every X ∈ K, a fragment of K ⊆ Q3, and it reads as a token state only through the coherent update (U2). Under continuous local rotations, UPD applied uniformly to "local unitary → CN → native readout" is equivalent to K ⊆ Q3 (disguise note) [W, rev] | [U]: Main.md:632 sources the Lüders update for the diagonal sector only; the coherent extension "belongs to the operational bridge". U3 open |
| OVr | UPD at outcome 0 only (equivalently G ⊆ K\*) | unresolved | as UPD; open under U3 | [U]; carries a knob (which outcome) |
| OVc | OV-CNOT: CN(K) ⊆ maxCone (every product test after the coupling is valid) | (i) | not flagged by D2 | [U]; non-native tests (MI+ review, A4) |
| OVn | OV-nat (MI+ C11): Π(K) ⊆ maxCone for every native protocol Π | (i) | MI+ D2 must-not-flag control (§5.2) | S13 [U] (MI+ RESULT C11) |
| MEV | ME-valid (= OV-LU): every maximally entangled projector is a valid test, i.e. product tests after "local unitary, coupling" are valid | (i) | test validity; does not imply K ⊆ Q3 (countermodel in §3) [W + EC, dc] | [U]; needs non-native local unitaries |
| CH | **Correlation chirality.** No physical pair state has a perfect co-oriented correlation: T_X orthogonal ⇒ det T_X = −1, read from fixed product tests whose cross-token identification is native SWAP transport | (i) | uses no operation; on the domain it is equivalent to K ∩ Γ(ME) = ∅ [W, new], where ME is the maximally entangled pure states | [U]; no OI source; constructed knowing the target |
| TH | **Joint passive state.** A positive-temperature equilibrium state of a fixed interacting pair generator (e.g. the Heisenberg pair) is a physical state | (iii) | D2(a): the shadow "Gibbs ∈ maxCone" holds on every cone while the clause excludes fixtures | the global analogue exists: GR.md:188–190, one passive state fixes the global orientation; `counting_passive` ThermalOrientation.lean:256 [AT] gives the classical layer. The relative (pair) version and the generator are [U] |
| SET | set-level correlation bounds over all product tests (Tsirelson- or IC-type) | (i) | [I] | [U]; Γ-invariant by F-β |
| SP⊕UPD | composite | (iii) | UPD is (iii); SP is (i) | both [U]; U3 open |
| SP⊕CH | composite | (i) | both components (i) | both [U] |

**Disguise note on UPD.** UPD has two equivalent readings.

- *Test side.* "A composite procedure built from the native coupling, the native readout and a token test has
  nonnegative probability." This is validity (X-5) for a composed test.
- *State side.* "The native instrument 'coupling, read the target, discard it' maps physical pair states into
  token states." This is preservation for one pair-to-token operation, which F2 §2.1 would read as compatibility
  (X-4).

The MI+ checks D2(a) and D2(b) were written for conclusions of the form "∈ K", and neither fires: the target cone
is the fixed token cone and is self-dual, so the D2(a) shadow is the clause itself. F2 G2 is not limited to those
checks. It rejects a bare transfer clause and dual-test closure as renamings of preservation (F2 §2.2 Fact A, §2.4 LO
and DT). Both readings above have that form: the state side is preservation by one operation, and the test side is
closure of the product tests e⊗P_k under pullback through CN [W, rev]. MI+ D3 bears on the same point: UPD requires
PSD of two compressions of each element of K, and with local unitaries admitted it implies K ⊆ Q3. UPD is therefore
class (iii) under the present F2 rules. Whether a disguise criterion frozen in advance, with no built-in outcome,
classifies any statement of UPD's content otherwise is U3.

**Collapse under local rotations [W, rev].** Every pure pair vector is a local-unitary image of a vector in
span{|00⟩, |11⟩} (Schmidt form). The outcome-0 conditional after "local unitary → CN → native readout" is the even
compression of the rotated X, so requiring it to be a token state for every local unitary tests X on every pure
vector. Under the continuous local rotations the target needs (A1, F2 Fact A, §5 G4), UPD applied uniformly to that
protocol class is therefore equivalent to K ⊆ Q3.
- Exact witness [EC, rev]: on the K(Z_F) defects z = I/2 − P_m, native UPD and all six configuration 2-subset
  compressions are PSD. After I⊗V with V = √2·Cᵀ, a local unitary built from the defect's coefficient matrix C
  (convention as in the review), the outcome-0 conditional has eigenvalue −½.
- Mutation control: V = I gives no violation.

**What UPD does contain.** UPD is not vacuous: on native operations it excludes Γ(Q3), K_Γ and maxCone [EC, dc].
On native operations alone it does not imply K ⊆ Q3, since K(Z_F) satisfies it [EC, dc]. That separation rests on
restricting the protocol class to native operations. Either the restriction is a knob (G7), or UPD collapses to
K ⊆ Q3.

UPD has the form of `hmax` (equivalently LC, SA :15–32) with local rank-one filters replaced by the native coupling
plus native readout: K ⊆ maxCone ⟺ every local rank-one conditional is a token state [W, from the definition of
maxCone and SA :15–32]. The analogy does not fix UPD's class. maxCone is invariant under local unitaries, so `hmax`
stays non-discriminating under them, while UPD under them becomes K ⊆ Q3 [W, rev].

## 3. Drop-one minimality

The conclusions are relative to the named alternatives. Here "drop X → C" means that with X removed, the cone C
satisfies the rest and is not Q3.

**3.1 Recorded composites.**

| candidate | drop | witness | evidence |
|---|---|---|---|
| OPs⊕PC | PC | Γ(Q3) | [EC, rec] REPORT P1 |
| | OP | K(Z_F) (satisfies PC) | [EC, rec] REPORT S3, AW-X7 |
| | weaken OPs to OPw | L, K(Z_F) | [EC + W, rec] op-fork N3–N4 |
| SP+Φ | Φ_k preservation | Γ(Q3) satisfies SP | [W + EC, rec] #820 |
| | SP | Γ(Q3) satisfies Φ_k preservation (F-β), and so does SEP | [W] |
| OI⁺1 | — | standalone: Γ(Q3) satisfies it (F-β) | [W] |
| | J-conjugate clause | the flow clause alone already excludes K_B (−1/4) and K(Z_F) (−1/16); the J-conjugate's own exclusion role is not isolated | [EC, rec] bridge audit, stage 6 historical level; [U] for the J-conjugate |

**3.2 Γ-breakers: the internal assumptions of UPD, OVr, MI and CH.**

| candidate | drop | witness | evidence |
|---|---|---|---|
| UPD | fixed identification (allow ΓAd(CN)Γ on Γ(Q3)) | Γ(Q3) satisfies the re-identified clause, since Tr₂[(I⊗P_k)Γ(Y)] = Tr₂[(I⊗P_k)Y] | [EC, dc] identity; [W] |
| | the non-configuration token state space (check conditionals by native configuration tests only) | vacuous on every domain cone | [W] F-α |
| | outcome 1 (UPD → OVr) | K_Γ satisfies OVr and fails UPD: even(Γ(B)) = I/2, odd(Γ(B)) has eigenvalue −½ | [EC, dc] |
| | the coupling (local filters only) | reduces to `hmax`: holds on every domain cone | [W] |
| | the restriction to CN (all 24 native pair permutations, either readout token) | no change: the conditional after σ and a readout is a compression to a 2-subset of configurations. The product 2-subsets are PSD on every domain cone by LC, and the two entangled 2-subsets are the CN parity blocks, so UPD-24 ≡ UPD-CN | [W, new] |
| | the native-protocol restriction (admit local unitaries before the coupling) | no non-Q3 survivor: UPD becomes K ⊆ Q3 (Schmidt form). K(Z_F) is excluded: V = √2·Cᵀ gives an outcome-0 eigenvalue −½, and the mutation V = I gives none | [W, rev]; [EC, rev] |
| MI | non-configuration inputs (ρ diagonal only) | vacuous: the outputs are diagonal, hence in SEP | [W] |
| | the coupling | reduces to `hH1` | [W] |
| CH | cross-token identification (relabel token-2 tests f ↦ fᵀ) | Γ(Q3) satisfies it | [W] F-β |

**3.3 New composites.**

| candidate | drop | witness | evidence |
|---|---|---|---|
| SP⊕UPD | UPD | Γ(Q3), which satisfies SP; whether K_Γ also survives is [U] (SP on K_Γ undecided) | [W + EC, rec] #820 |
| | SP | K_B, K(Z_F), SEP and L all satisfy UPD on native protocols; K(Z_F) fails it once local unitaries precede the coupling (§3.2) | [W]; [EC, dc] for the defects; [EC, rev] |
| SP⊕CH | CH | Γ(Q3) | [W + EC, rec] |
| | SP | K_B, L, SEP (subcones of Q3 satisfy CH) | [W] |
| CH⊕MI or MEV⊕MI | — | **L** survives the composite: L ⊆ Q3 satisfies CH and MEV, and L satisfies MI | [EC, rec] op-fork "Both satisfy MI"; [W]. Not sufficient |

**3.4 Strength relations on the domain.**

| relation | separating witness | evidence |
|---|---|---|
| PC ⇒ MI | — | [W, rec] |
| MI ⇏ PC | maxCone | [EC, rec] |
| PC ⇒ OVc ⇒ UPD ⇒ OVr | OVc ⇒ UPD because the tests e⊗P_k after the coupling yield cond_k | [W] |
| OVr ⇏ UPD | K_Γ | [EC, dc] |
| UPD ⇏ OVc | no witness found | [U] |
| UPD and OVc ⇏ PC | K_B | [EC, rec] that PC fails on K_B; [W] that UPD and OVc hold, since K_B ⊆ Q3 |
| MI vs UPD: incomparable | SEP satisfies UPD and fails MI (B ∉ SEP); maxCone satisfies MI and fails UPD | [W]; [EC, dc]: Γ(P_singlet) has an even block with eigenvalues ±½ |
| UPD vs CH: incomparable, for native UPD | K(Z_F) satisfies native UPD and fails CH; cone(SEP ∪ {X_c}) satisfies CH and fails UPD | [EC, dc] + [W] |
| UPD vs MEV: incomparable, for native UPD | the same two cones | [EC, dc] + [W] |
| MEV ⇒ CH | — | [W] |
| CH ⇏ MEV | cone(SEP ∪ {Γ(B)/2 + I/8}) | [W] |
| MEV ⇏ K ⊆ Q3 | X_c | [EC, dc] + [W] |

Here X_c = I/2 − (53/100)P_v with v ∝ 4|00⟩ + |11⟩: block-positive, ME-valid, not PSD, and failing UPD. Its bounds
follow from Schmidt arguments [W]: product overlap 16/17 and maximally entangled overlap 25/34, both exact in
[EC, dc].

**3.5 Single premises, not composites.**
- SP: drop it and K_B, K(Z_F) survive [W + EC, rec].
- SD: Γ(Q3) and K(Z_F) are self-dual (Γ is a trace isometry; the K(Z_F) certificate is historical) [W].
- GEO: [U]; no pair form.
- TH: drop the interacting generator and the clause is empty.

**Not claimed.** That any composite here is minimal among all premise sets; that SP⊕UPD or SP⊕CH implies K = Q3
(no classification of their survivors was attempted); that UPD restricted to ancilla-assisted native protocols adds
nothing.

## 4. Discrimination matrix

**Legend.**
- *pass*: Q3 satisfies the premise.
- *excl*: the premise excludes the cone.
- *surv*: the cone satisfies the premise.

Identification is fixed throughout.

**PSD assumptions.** The UPD, OVr and OVc rows evaluate PSD of compressions of competing-cone elements. UPD tests its
two parity compressions, OVr the even one, and OVc the conditionals that its tests e⊗P_k yield after the coupling.
For example, Γ(Q3) is excluded because Γ(P_singlet)'s even block has eigenvalues ±½. These rows read a compression
as a token state only through the coherent update, whose source is open (U2). Apart from these rows, no entry uses
PSD or CP of a competing cone's elements. Entries that use K_B ⊆ Q3 or L ⊆ Q3 concern a cone's fixed membership, not
an import.

| premise | Q3 | Γ(Q3) | K_B | K(Z_F) | SEP | classical | other |
|---|---|---|---|---|---|---|---|
| EA (alone) | — | surv: no K content [W] | surv | surv | surv | surv | — |
| PC | pass [AT `Q3_cnot`] | excl [EC, rec P2] | excl (\|+i⟩ input) [EC, rec] | surv [EC, rec] | excl, B ∉ SEP [W] | pass [W] | maxCone excl [EC, rec] |
| MI | pass [W] | excl [EC, rec p3] | excl [EC, rec] | surv [EC, rec] | excl [W] | pass on diagonal inputs [W] | maxCone surv, L surv [EC, rec] |
| CPK on K | pass | excl only by importing PSD (D3) | idem | idem | idem | — | inadmissible as a discriminator |
| GRV, positivity form | pass | surv: ΓAd(DP_G)Γ [EC, rec B1–B6] | surv: the fully dephased extension maps every domain cone into the diagonal cone [W, new] | surv | surv | pass | vacuous on the domain [W] |
| GRV, automorphism form | pass | surv [W + EC, rec] | [U] | surv via PC24 [EC, rec] | [U] | pass | — |
| OI⁺1 / DRV-p | pass [AT `driveInvariant_of_eq_Q3`] | surv [W] F-β | excl (−1/4) [EC, rec] | excl (−1/16, historical) [EC, rec] | surv [W] | pass [W, SA] | L [U] |
| SP | pass [W, rec] | surv [W + EC, rec] | excl [W + EC, rec] | excl [W + EC, rec; historical self-duality] | excl [W, rec] | pass [W, rec] | L excl [W, new: #820's X_Z face argument with L\* = K(Z_F)]; K_Γ [U] |
| OPw | pass | surv [W + EC, rec] | excl (E) [EC, rec] | surv [EC + W, rec] | excl (E) | — | L, maxCone surv |
| OPs | pass | surv [EC, rec P1] | excl | excl [EC + W, rec] | excl | — | maxCone surv [W, rec] |
| OPs⊕PC | pass | excl | excl | excl | excl | — | K = Q3, conditional [W, rec; AT `pairCone_eq_Q3_of_drive_maxCone`] |
| LT / COMP-1 | pass | surv | surv | surv | surv | pass | holds on every domain cone [W, rec C7] |
| HC | pass | surv: local forms are Γ-covariant [W, rec] | [U] | [U] | [U] | — | — |
| GEO, single body | pass | surv | surv | surv | surv | — | the token ball is common to every domain cone [W] |
| GEO, pair form | [U] | surv for any form stated with K's own effects or the native Lüders update [W, F-β] | [U] | [U] | [U] | — | a form with fixed entangled sharp tests reduces to MEV-type [W] |
| DRV-a | — | surv: no K content | surv | surv | surv | — | — |
| SWP | pass | surv [EC, rec P2: local/swap subgroup] | surv [W] | surv [EC, rec] | surv | pass | — |
| NST | pass | surv [W] F-α | surv | surv | surv | pass | vacuous [W, rec] |
| SD | pass | surv [W] | excl: K_B\* ⊋ Q3 ⊋ K_B [W] | surv (historical) [W] | excl: SEP\* = maxCone [W] | pass | — |
| **UPD** | pass [W] | **excl** [EC, dc]: Γ(P_singlet) has even block eigenvalues ±½ | surv [W] | surv on native protocols [EC, dc defects + W]; excl once local unitaries precede the coupling, where UPD ≡ K ⊆ Q3 [EC, rev] | surv [W] | pass [W] | K_Γ excl, maxCone excl [EC, dc]; L surv [W] |
| OVr | pass | excl [EC, dc] | surv | surv [EC, dc] | surv | pass | K_Γ surv [EC, dc] |
| OVc | pass | excl [EC, rec] | surv [W] | surv: PC [EC, rec] and K(Z_F) ⊆ maxCone | surv | pass | maxCone excl [EC, rec] |
| OVn (C11) | pass [AT `cp_of_instAvail` + W] | excl [EC, rec] | surv [W] | [U]: Δ2 unrun | surv | pass | — |
| MEV | pass [W] | excl [EC, rec Fact B] | surv [W] | **excl**: Tr(P_m z) = −½ [EC, dc] | surv | pass | K_Γ excl [W]; maxCone excl; L surv |
| CH | pass [W] | **excl**: T(Γ(B)) = I [EC, dc] | surv [W] | **excl**: det T(z) = +1 [EC, dc] | surv [W] | pass | K_Γ, maxCone excl; L surv |
| TH (Heisenberg pair) | pass | excl for β > (ln 3)/4 [W, new] | excl (twirl) [W, new] | [U] | excl [W] | — | needs a non-native generator |
| SET | pass | surv [W] F-β | [U] | [U] | surv | — | — |
| SP⊕UPD | pass | excl (UPD) | excl (SP) | excl (SP, resting on the historical self-duality certificate: U6) | excl | pass | L excl (SP [W, new, unreviewed]: U7); maxCone excl; K_Γ excl (UPD). UPD's class: U3. K = Q3 [U] |
| SP⊕CH | pass | excl | excl | excl | excl | pass | L, K_Γ, maxCone excl. K = Q3 [U] |

**Headlines.**
- **Γ(Q3).** Of the examined premises, only those carrying a cross-token orientation datum fixed independently of K
  exclude it: PC, MI, UPD, OVr, OVc, OVn, MEV, CH, TH and the composites built on them.
  - Everything built from K's order, native statistics, local operations (native or continuous), set-level
    product-test clauses, SP, SD, OP or LT leaves it surviving (F-α, F-β).
- **Some alternatives only.**
  - On native protocols, UPD and OVc distinguish Γ(Q3), K_Γ and maxCone, and OVr distinguishes Γ(Q3) and maxCone;
    none of them distinguishes K_B or K(Z_F). For UPD this rests on restricting the protocol class to native
    operations. With local unitaries admitted before the coupling, UPD excludes K(Z_F) and is equivalent to
    K ⊆ Q3 (§3.2). Either the restriction is a knob (G7), or UPD collapses to K ⊆ Q3.
  - SP and OPs distinguish K_B and K(Z_F) but not Γ(Q3).
  - MI distinguishes Γ(Q3) and K_B but not K(Z_F).
  - MEV and CH distinguish Γ(Q3) and K(Z_F) but not K_B, L or SEP.
- **Q3 subcones.** No upper-bound (test-validity) premise excludes a Q3 subcone such as K_B, L or SEP [W]. Excluding
  those needs a lower bound (MI-type), a homogeneity clause (OP, a flow) or a frame clause (SP).
- **Source validity is separate.** No premise that excludes Γ(Q3) has an OI source (§7).

## 5. F2 gate map

The gates are G1–G8 as written in memo §2.3, with M1 per §3.2. G5 is headline exclusion of K_B, K(Z_F) and Γ(Q3) by
the candidate itself (§3.3); control preparation is a separate subfinding and is never a PASS on its own. This memo
prepares no controls, so no G5 headline here exceeds "exclusion aspect met, controls unprepared".

G2 is shown as (i)/(ii)/(iii):
- (i) independently meaningful;
- (ii) its own sourcing argument;
- (iii) a consequence beyond compatibility.

A premise that is only named does not pass G2.

| candidate | G1 | G2 (i/ii/iii) | G3 | G4 | G5 | G6 | G7 | G8 | M1 |
|---|---|---|---|---|---|---|---|---|---|
| EA | PASS | yes/[AT]/no → FAIL (no K content) | FAIL | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| PC | PASS | rename/no/no → FAIL | PASS | FAIL | FAIL (K(Z_F)) | OPEN | PASS | PASS | PASS [W] |
| MI | PASS | yes/no/no → FAIL (membership) | PASS | FAIL | FAIL (K(Z_F)) | OPEN | PASS | PASS | PASS [W, EC rec P5] |
| CPK | FAIL (PSD by fiat) | FAIL | n/a | FAIL | n/a | OPEN | — | PASS | — |
| GRV | PASS | yes/[U]/no → FAIL | FAIL | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| OI⁺1 / DRV-p | PASS | rename → FAIL | FAIL | FAIL alone | FAIL (Γ) | OPEN | PASS | PASS | PASS |
| SP | PASS | yes/[I]/no → FAIL | FAIL [rec] | FAIL | FAIL (Γ) | OPEN | PASS | PASS | PASS |
| SP+Φ | PASS | FAIL | FAIL | FAIL | FAIL (Γ) | OPEN | PASS | PASS | PASS |
| OPw | BORDERLINE [rec] | FAIL [rec] | FAIL | OPEN [rec] | FAIL | OPEN | PASS | PASS | NOT TESTED |
| OPs | PASS | FAIL (strict) [rec] | FAIL | PASS, conditional [rec] | FAIL (Γ) | OPEN | PASS | PASS | PASS [W] |
| OPs⊕PC | PASS | FAIL [rec] | PASS | PASS, conditional | exclusion met, conditional [rec]; controls unprepared | OPEN | PASS | PASS | PASS |
| LT | PASS | non-discriminating | FAIL [rec C3] | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| HC | PASS | hypothesis → FAIL | FAIL | FAIL | [U] | OPEN | PASS | PASS | — |
| GEO | PASS | [U] (unproved, unfrozen) → FAIL | FAIL (single body); pair form [U] | [U] | [U] | OPEN | [U] (statement unfrozen) | PASS | [U] |
| DRV-a | PASS | E0 → FAIL | FAIL | conditional (adds a continuous operation) | FAIL | OPEN | flow branch fixed? [U] | PASS | PASS [W] |
| SWP | PASS | sourced/non-discriminating | FAIL | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| NST | PASS | vacuous | FAIL | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| SD | PASS | [I] → FAIL | FAIL | FAIL | FAIL | OPEN | PASS | PASS | PASS |
| **UPD** | PASS: readout, coupling, conditional state | transfer clause, class (iii) [W, rev] (U3) / [U]: the coherent update is not sourced (Main.md:632) / none → FAIL | PASS [EC, dc] | FAIL (adds no operation) | FAIL standalone on native protocols (K_B, K(Z_F) survive); with local unitaries admitted K(Z_F) is excluded and UPD ≡ K ⊆ Q3 [W + EC, rev] | OPEN | not a pass: outcomes and orientation are fixed, but either the restriction to native protocols is a knob, or, lifted, UPD collapses to K ⊆ Q3 [W, rev] | PASS | PASS [W]: uses the retained readout; retained protocols unchanged |
| OVr | PASS | as UPD → FAIL | PASS | FAIL | FAIL | OPEN | FAIL (outcome knob) | PASS | PASS |
| OVc / OVn | PASS | yes/[U] S13/none → FAIL | PASS | FAIL | FAIL | OPEN | PASS | PASS | PASS [W] |
| MEV | BORDERLINE: lists test matrices unless stated as OV-LU | yes/[U]/none → FAIL | PASS | FAIL (posits non-native local unitaries) | FAIL (K_B) | OPEN | PASS | PASS | PASS [W] |
| CH | BORDERLINE: equivalent to excluding the named family Γ(ME) [W, new] | [U]/[U]/none → FAIL | PASS | FAIL | FAIL (K_B) | OPEN | PASS | PASS | PASS [W] |
| TH | PASS | membership (D2(a)) → FAIL; partial route GR.md:188–190 | PASS [W] | conditional (needs a continuous generator) | [U] (K(Z_F)) | OPEN | β, generator: knobs unless fixed [U] | PASS | [U] (added dynamics) |
| SP⊕UPD | PASS | FAIL: both components unsourced | PASS | FAIL | exclusion met conditionally [W + EC]: K(Z_F) via SP rests on the historical certificate (U6), and UPD's class is U3; controls unprepared | OPEN | as UPD: not a pass | PASS | PASS [W] |
| SP⊕CH | BORDERLINE (CH) | FAIL | PASS | FAIL | exclusion met [W + EC]; controls unprepared | OPEN | PASS | PASS | PASS [W] |

**G6.** No candidate has a concrete independent prediction.
- The consequences these premises carry are standard quantum facts, for example "no pair state has
  ⟨XX⟩ = ⟨YY⟩ = ⟨ZZ⟩ = +1" (CH) or entangled low-temperature equilibria (TH).
- Such facts are retrodictions on the consistency axis and are excluded from G6 by the rule of MI+ §9.

**G4.** No examined Γ-breaker adds an operation. Any X built from them needs a separate availability component that
breaks `NonnegBounded` (FrozenSourcing.lean:65 [AT]; `obsTheory_nonnegBounded` :84) and the uniform-ray and
reality invariants. That component is an uncountable resource under A1, and it is unsourced.

## 6. Conclusion and next preregistration target

**The weakest candidates, under the relative criteria.** The criteria: logical strength on the domain; exclusion of
the named alternatives under fixed identification; no membership clause; native readout and M1 retained. Each item
states its F2 class and its PSD use (§2, §4). The weakest premises form an antichain, not a single premise.

1. **Γ-breaking content without a membership clause: UPD.** "After the native read-write coupling and a native
   readout of the partner, the token's conditional description is a token state."
   - Under the present F2 rules it is a transfer clause, class (iii) (§2; U3). Its discrimination evaluates PSD of
     two compressions of each element of K (§4).
   - Its separation from K ⊆ Q3 rests on the restriction to native protocols. With local unitaries admitted before
     the coupling it is equivalent to K ⊆ Q3 (§3.2), so either the restriction is a knob (G7) or UPD collapses to
     K ⊆ Q3.
   - It is strictly weaker than PC (witness K_B: PC fails [EC, rec], UPD holds [W]). It is implied by OVc [W], and
     whether the converse fails is [U]. Its single-outcome restriction OVr is strictly weaker (K_Γ [EC, dc]) but
     carries a knob (G7).
   - UPD and MI are incomparable (§3.4). The exact dual pair is MI (G ⊆ K), a membership (class (iii)), and OVr
     (G ⊆ K\*).
2. **Γ(Q3) and K(Z_F) together in one premise: CH, or its convex form MEV.** CH is the weaker of the two
   (MEV ⇒ CH, CH ⇏ MEV [W]). Both are incomparable with native UPD (§3.4). CH is G1-borderline: on the domain it is
   equivalent to excluding a named matrix family [W, new]. MEV needs non-native local unitaries before the coupling.
3. **All named alternatives (K_B, K(Z_F), Γ(Q3), SEP, L, maxCone) excluded without a membership clause: SP⊕UPD,
   conditionally.** The conditions:
   - As a composite free of compatibility clauses, it holds only if U3 resolves in UPD's favour.
   - The exclusion of L rests on U7, a written argument not yet reviewed.
   - SP's exclusion of K(Z_F) rests on U6, a historical certificate.

   Its survivors, including K_Γ under SP, are not classified, and sufficiency is [U]. SP⊕CH also excludes K_Γ but
   inherits CH's G1 defect. The two composites are not shown comparable.

No examined premise passes G2(ii), G4 or G6. No examined premise is adopted.

**The physical content a premise must add.** In one line: a constraint tying the two tokens' relative orientation,
which is visible only in joint coherences (for example the parity block that the native coupling maps onto one
token), to the physical state space through validity of the update or test, not through membership.

**Testing the review's claim** that "excluding Γ(Q3) requires the entangling action fixed independently of K, from a
source other than membership". The claim is confirmed in substance and corrected in two respects.

- **(a) The action is already fixed.** On the matrix carrier it is fixed by native semantics [AT], and for every
  cone by G3's fixed identification. Fixing it adds no K content (row EA). What is missing is the link from K to
  the action.
- **(b) A link other than membership exists in form.** UPD and its OV forms supply it, with conclusions in the fixed
  token cone or as test validity. Under the present F2 rules UPD is a transfer clause (§2), so the link it supplies
  is a compatibility clause (U3). Its source is still [U].
- **(c) An entangling operation is not necessary.** CH excludes Γ(Q3) and K(Z_F) using fixed product tests alone,
  with native SWAP supplying the cross-token identification [EC, dc; W]. This bears on the reading in REPORT's gate
  ambiguities ("only entangling native operations can separate"), which is correct for native tests only.
  - Every examined Γ-breaker carries a cross-token orientation datum [W, scoped by F-α and F-β], fixed
    independently of K, that involves a non-configuration token resource: a test, a preparation, or local
    operations entering a joint protocol.
  - §A.31: NEW (scoped); under maximum skepticism the CH instance itself is not viable as X (G1).

**Next testable preregistration target: the UPD screen, with SP⊕UPD as its composite, both conditional on U3.** It
needs the following.

1. **A disguise criterion frozen in advance, with no built-in outcome.** It decides U3.
   - Known answers: PC and MI must flag; OVn (C11) must not.
   - The dual-reading case (UPD's state-side reading as pair-to-token preservation) is ruled on explicitly.
2. **A source node, closure mode with a kill test.** Can token-state validity of coherent conditionals after a native
   premeasurement be derived?
   - Inputs: the Lüders/Bayesian update (Main.md:632, diagonal sector), `readout_is_localLuders` and LC.
   - Kill tests: the Γ re-identification control (§3.2) must fail any proposed derivation that does not use the
     fixed identification; a derivation using only diagonal data is void by F-α.
3. **Exact discrimination, with certificates.** UPD on Q3, Γ(Q3), K_B, K(Z_F), SEP, L, K_Γ, maxCone and the
   classical cone. Also UPD over ancilla-assisted native protocols on K(Z_F), the Δ2-type node, which is the only
   native-protocol route by which UPD-family premises could exclude K(Z_F). Admitting local unitaries before the
   coupling excludes K(Z_F) but collapses UPD to K ⊆ Q3 (§3.2).
4. **SP nodes.**
   - An independent check of this memo's adaptation "L fails SP".
   - A decision of SP on K_Γ.
   - A classification of the SP ∧ UPD survivors on the domain, or a named exact countermodel to K = Q3.
5. **Gates fixed before results.**
   - G4: name the availability component.
   - G6: preregister a decision rule for one independent prediction, or record G6 OPEN.
   - M1: the P5-type retained-law replay plus a check that UPD's conditional is the native Lüders branch.

## 7. Unsourced and unresolved obligations

1. U1: H-CAR. Physical pair descriptions transform by the native conjugation (EA) [U].
2. U2: the source of UPD. The coherent update beyond the diagonal sector [U] (Main.md:632).
3. U3: the classification of UPD. Under the present F2 rules it is a transfer clause, class (iii) (§2). Open [U]:
   - whether a disguise criterion frozen in advance, with no built-in outcome, classifies any statement of UPD's
     content otherwise;
   - whether the restriction to native protocols can be fixed other than as a knob, given that UPD with local
     unitaries admitted is K ⊆ Q3 (§3.2);
   - OVr's class, whose basis is UPD's;
   - the reading of the other class-(i) rows against the transfer-clause form (§2).
4. U4: availability of non-configuration token tests or states composed with native operations: X-5, for OVr, OVc,
   OVn, MEV and CH [U]. `avail_eq_fullEffects` (EffectSpace.lean:727) does not apply to countable classes.
5. U5: UPD and OVn over ancilla-assisted native protocols against K(Z_F) (Δ2 unrun) [U].
6. U6: the SP source [I/U]. SP's exclusion of K(Z_F) rests on the historical self-duality certificate [W].
7. U7: "L fails SP" [W, new, unreviewed].
8. U8: SP on K_Γ [U].
9. U9: sufficiency of SP⊕UPD and SP⊕CH for K = Q3 [U].
10. U10: the pair form of K∞-Geom (unfrozen); KINF-1 halted [U].
11. U11: OI⁺-1. Whether the J-conjugate clause carries exclusion power beyond the flow [U].
12. U12: the GRV automorphism form on K_B and SEP [U].
13. U13: TH. The interacting generator, transport of the relative orientation (the pair analogue of GR.md:190's
    H-orientation transport) and K(Z_F) [U].
14. U14: the CH source, and its G1 status [U]. Any link to OI's time-reversal structure (the hidden predictive memory
    carries future tails, Main.md:600) is a speculative lead only, with no argument given [U].
15. U15: the G4 availability component, a continuous phase resource that is not merely posited [U].
16. U16: G6 for every candidate [U].
17. U17: OP-strong sourcing, the trivial-system clause (AW-OP2) and maxCone under OPs [U, rec].
18. U18: SP ⇒ Φ_k preservation [U, rec].
19. U19: F-β's scope. It covers clauses over the listed data. It is not a no-go for premises that fix new
    cross-token structure [W].
20. U20: every [W, new] argument here awaits independent review:
    - F-γ;
    - UPD-24 ≡ UPD-CN;
    - CH ⟺ K ∩ Γ(ME) = ∅;
    - L fails SP;
    - the GRV dephasing;
    - TH.
