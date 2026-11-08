# MATH-CON-1: does one identification rule generate a coherent operation in the polarization closure, or install it?

**Standing.** Preregistration only, under #1169. Writer: Claude Code session, 2026-11-08. Status
of this file: `WIP / UNVERIFIED`. Revision r2 responds to the independent review of r1 at
`e593465b` (REVISE: blocking B1–B4, non-blocking N1–N14). §13 maps each finding to its change;
r1 is commit `e593465bdecd96bff92877f9ecf4fcf8befec845`.

This file fixes an object, definitions, a circularity test, countercontrols and an outcome
partition before any result exists. It contains:
- no derivation;
- no Lean statement or build;
- no scientific computation;
- no new premise;
- no manuscript change;
- no V3 step.

Every mathematical statement below is either a citation of a kernel theorem on `main` or an
obligation for a later stage (§3, "new"). It is never a result of this file. Stage 1B, the
derivation and the Lean membership proofs, needs a separate owner authorization (§10).

**Authority.**
- Owner decision, [#1169 comment 6721267600](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6721267600)
  (amaybaum, 2026-11-08T12:05:53Z). The rulings for MATH-CON-1:

  > 1. Starting construction: Prioritize the existing polarization-closure construction, A10/PolC,
  >    together with B23's finite protocol. Avoid duplicating established K-chain results.
  > 2. Decisive question: Determine whether one added identification rule genuinely generates a
  >    coherent operation, or merely installs Hadamard behavior by definition. Freeze the monomial
  >    baseline and use the coherent Clifford by fiat countercontrol.
  > 3. Authorization boundary: Prepare and independently review the MATH-CON-1 preregistration
  >    only. No derivation, Lean execution, scientific computation, new premise or merge is
  >    authorized.
  >
  > The preregistration should preserve the inventory's alternative routes and explicitly
  > distinguish results already proved from new obligations.
  >
  > Importantly, if A10 supplies Hadamard by definition, that does not make the existing
  > conditional mathematics invalid. It means the noncircular construction milestone has not been
  > reached.
  >
  > The appropriate next step would be to identify the missing access or identification rule, not
  > to declare the construction a failure in every sense.

- Owner decision, [#1169 comment 6720678942](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6720678942)
  (amaybaum, 2026-11-08T11:03:23Z). It supplies the target, the four assumption classes, and
  refinements 1 and 2 on the circularity test and on Theorems NC and U2. The target:

  > Construct an explicit extension of OI with one additional, clearly identified access or
  > identification rule that generates at least one genuinely non-stabilizer quantum-compatible
  > operation, including valid measurement behavior and repeatable composition, without defining
  > that operation into existence.

**Inputs.**
- The MATH-CON-0 inventory, revision r3 (sha256 `e68058ba…28df5`; #1169 comments 6721102809 and
  6721121369).
- Its two independent reviews (#1169 comments 6721133702 and 6721137458). r1 returned REVISE;
  r2 returned ACCEPT WITH CHANGES, with G1–G4 applied in r3.

Labels carried from those records keep their meaning: the rows A1–A12, B1–B26, C1–C11 and D1–D9;
the target clauses T1–T5; the classes [N], [R], [Q] and [P]; routes (i), (ii) and (iii); and
shapes 0–3. *Inventory reading* and *reviewer reading* mark pointers from those records. They are
carried here as obligations, not results.

**Source snapshot.** Every repository citation is to `main` at
`45eea51d67237f2a41865dd7efc1ea97e2bc904f` (`main@45eea51d`). Since the inventory's corpus
`9c201475`, that commit adds only the A5-Q3 record directory (`q3-a6-offsets-20261108/`, four
files). No Lean file and no file cited here changed. A citation `X:n` means line `n` of file `X`
at `main@45eea51d`.

Kernel files, all under `verification/lean-mathlib/OIBridge/`:

| Abbreviation | File |
|---|---|
| **BFP** | [`BridgeFiniteProtocol.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean) |
| **PCL** | [`PolarizationClosure.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/PolarizationClosure.lean) |
| **C5D** | [`C5Discovery.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/C5Discovery.lean) |
| **IL** | [`ImplementationLocality.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/ImplementationLocality.lean) |
| **SC** | [`StructuralClosure.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/StructuralClosure.lean) |
| **SI** | [`SubstratumInterface.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/SubstratumInterface.lean) |
| **SIA** | [`SubstratumInterfaceAudit.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean) |
| **RB** | [`RouteB.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/RouteB.lean) |
| **MR** | [`MicroscopicReversibility.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/MicroscopicReversibility.lean) |
| **PII** | [`PreservationInductionInstances.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean) |
| **CCS** | [`CoherentContinuumSource.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/CoherentContinuumSource.lean) |
| **OA** | [`OperationalAssembly.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/OperationalAssembly.lean) |
| **DG** | [`DynamicsGlue.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/DynamicsGlue.lean) |
| **AC** | [`AncillaClosure.lean`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/lean-mathlib/OIBridge/AncillaClosure.lean) |

Records:

| Abbreviation | Record |
|---|---|
| **C5A** | [`verification/audits/foundations/c5-discovery-audit.md`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/audits/foundations/c5-discovery-audit.md) |
| **PCA** | [`verification/audits/foundations/polarization-closure-audit.md`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/audits/foundations/polarization-closure-audit.md) |
| **CH1** | [`round-oi-channel-1-audit/result.md`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/programmes/oi-qm/reconstruction/round-oi-channel-1-audit/result.md) |
| **FP1** | [`round-oi-finite-protocol-1/`](https://github.com/amaybaum/incompleteness/tree/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/programmes/oi-qm/reconstruction/round-oi-finite-protocol-1) |
| **M2D** | [`mechanism-2-20261108/DESIGN.md`](https://github.com/amaybaum/incompleteness/blob/45eea51d67237f2a41865dd7efc1ea97e2bc904f/verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md) |

**Not read.** The FHE-SEL-1 physical-preregistration branches (#1203–#1205) and the content of
#1198.

***

## 1. The object

### 1.1 What the object is

The object is the label-invariant polarized theory on the two-valued alphabet, read together
with B23's finite protocol.

- **The theory.** `polarizedTheoryC (Fin 2) := genTheory PolC polC_arch (Fin 2)` (PCL:189).
  - `genTheory` makes system availability `InstAvail PolC (Fin 2)`, and level-`n` availability
    `InstAvail PolC (Fin 2 × Fin n)` (IL:852–855).
  - The `InstAvail` rules are `op`, `readout`, `coarse`, `bind` and `discard` with uniform attach
    (IL:268).
- **The class.** `PolC` (PCL:150) is the inductive closure of the following under `mul`, `smul`
  (`‖a‖ ≤ 1`), `proj`, `block` and `relabel` along every carrier bijection:
  - `perm`: the members of `permClass`, the contractively scaled partial permutations (SIA:236);
  - `shear n`: `siteShearImage n = diag(p ↦ if p.1 = 1 then i else 1)`, which is `S ⊗ I_n`
    (C5D:192);
  - `swap n`: `siteSwapImage n`, which is `H ⊗ I_n` (C5D:196).
- **B23's architecture.** For any `Architecture 𝓘` with `𝓘 Work balancedCircuit`,
  `∀ j, 𝓘 Work (resetPerm j)` and `∀ j, 𝓘 Work (correction j)`:
  - the four-outcome attempt instrument is `InstAvail 𝓘 Token (Fin 4)`
    (`instAvail_attempt`, BFP:212);
  - its branch 0 is `(5/8) • conjChannel drivePhase`, with `drivePhase = diag(1, 3/5 + (4/5)i)`,
    and its other branches are `(1/8) • id` (`attempt_balanced_branch`, BFP:194);
  - every stopped depth is available and equals `(1 − (3/8)^k)·Ad(drivePhase) + (3/8)^k·id`
    (`balanced_finite_available`, BFP:256; `balanced_stopped_formula`, BFP:245);
  - the types are `Token = Fin 2` and `Work = Token × Fin 4` (BFP:99–100).

  MATH-CON-1 uses B23 as proved and reproves none of it.
- **The K-chain.** Rows B1–B22 and B24–B26 are not inputs. No K-chain result is restated or
  reproved.

### 1.2 The stated rule

The added rule is the polarization map of C5A candidate 2 (C5A:91–106; its explicit form is T4,
C5A:247). It has two parts.

**(ℛ-R), the non-matrix part:**
- (a) Each site's phase space `V × V` is split into a position half, which the observer reads,
  and a momentum half.
- (b) The observer's state space is the amplitudes over the position alphabet. On the two-valued
  alphabet the system carrier is `Fin 2`, and level `n` is `Fin 2 × Fin n` with the ancilla a
  spectator.
- (c) The substratum's two canonical layers are available to the observer as their images under
  a representation of the layers on that space.

**(ℛ-Q), the matrix part:** the images of the layers.
- The shear layer goes to the quarter phase: `shear n ↦ siteShearImage n`.
- The swap layer goes to the finite Fourier transform on the position alphabet, the Hadamard
  matrix: `swap n ↦ siteSwapImage n`.

C5A names this representation the Weil representation of the canonical layers. The kernel enters
the two images as the generators `PolC.shear` and `PolC.swap` (PCL:152–153).

The corpus does not supply the map (C5A test 8, T6 row, C5A:249). Its status is *proposed* (§9).

### 1.3 Classification of every assumption

Each assumption takes exactly one class, and each clause of the rule takes exactly one CT kind
(§4.4). The criterion between [R] and [Q] is the inventory's: a datum that is a matrix or a matrix
family in the complex interface is [Q], and a choice that is not a matrix is [R]. The kind is read
from the clause's text alone, by the definitions of §4.4, and is fixed here before any derivation.

| # | Assumption | Class | CT kind (§4.4) | Reason for the kind | Where it enters |
|---|---|---|---|---|---|
| A-1 | Finite reversible substratum; stated observer access, the scaled partial permutations `permClass` | [N] | G-n, admission form | It admits a stated set of matrices, every one monomial, so it never produces a marked node | `PolC.perm`; `permTheory` (SIA:606) is the stated-access theory |
| A-2 | Operational interface: complex matrix kinematics; `FiniteOperationalTheory`; the `InstAvail` rules; `readout` as local Lüders (`readout_is_localLuders`, OA:658); discard after uniform attach; the architecture constructors `one`, `mul`, `smul`, `proj`, `block` | [Q] | shared reference interface | It is the same in every theory compared here, so it is not a clause of the rule. `proj` names only 0/1 diagonal projectors, which are monomial | common to the baseline, the countercontrols and the object. It is disclosed and is not the added rule |
| A-3 | (ℛ-R)(a): polarization, with the position half read | [R] | I-f | It fixes which half of the phase space the observer reads. Formally the carrier stays `Fin 2`, the same as `substratumTheory (Fin 2)`'s; the `InstAvail` rules are unchanged; the clause states no matrix | the added rule, non-matrix part |
| A-4 | (ℛ-R)(b): the observer's state space is the position amplitudes | [R] | I-f | It fixes the identification of the carrier with the position alphabet, which formally is the carrier `Fin 2` and nothing else. It states no matrix and changes no `InstAvail` rule | the added rule, non-matrix part |
| A-5 | (ℛ-R)(c): the layers are available as their images under a representation | [R] | G-n, admission form | It makes operators available, and its text refers to specific matrices: the images at the two stated inputs, the shear and swap layers. Its values are A-6 and A-7 | the added rule, non-matrix part |
| A-6 | (ℛ-Q), shear image: `siteShearImage n` | [Q] | G-n, admission form (literal) | A literal matrix admitted at every level | the added rule, matrix part (generator `PolC.shear`) |
| A-7 | (ℛ-Q), swap image: `siteSwapImage n` | [Q] | G-n, admission form (literal) | A literal matrix admitted at every level | the added rule, matrix part (generator `PolC.swap`) |
| A-8 | Relabelling closure (`PolC.relabel`), carrying implementation locality | [R] | G-u, shared | Uniform over all class members, names no matrix; the same closure is imposed on the baseline and on the fiat class | shared architecture requirement. `polarizedTheoryC_derivedOI` takes `polC_labelInvariant` as an input (PCL:606–609). Implementation locality needs *some* context-stable, label-invariant generating class (IL:370), and `PolC` is the least label-invariant architecture containing `PolGen`. It is not counted as a second added rule unless countercontrol CC-2 shows that it carries the target (§5) |
| A-9 | B23 primitive memberships (`balancedCircuit`, `resetPerm j`, `correction j` ∈ `PolC`) | not assumed | — | — | new obligations O-3a–O-3c (§3). If proved, they follow from A-1, A-6 and A-7. If not proved, B23 does not apply to `PolC` and no assumption is added in their place |
| A-10 | Context stability and label invariance for spectators | not assumed | — | — | proved for `PolC`: `polC_contextStable` (PCL:584), `polC_labelInvariant` (PCL:172) |
| A-11 | Quarter phases at every level (`PhasesAvailable`) | not assumed | — | — | derived for `PolC` from A-6 (`polC_phaseGate`, PCL:443; `polarizedTheoryC_phasesAvailable`, PCL:448). Contrast A7–A9 of the inventory, where `PhasesAvailable` is stipulated |
| A-12 | The monomial baseline `substratumClass` (§4.1) | comparison set | — | — | not a premise of the object. It is the set the T2 criterion excludes, and the class of the baseline countercontrol |
| — | Independently motivated physical assumption | [P] | — | — | none. Physical selection of the map belongs to the other workstream (FHE-SEL-1) |

**[R] and [Q] split of the map.** The map's [R] part is A-3 to A-5. Its [Q] part is the two
images A-6 and A-7. The [Q] images are what place a non-monomial operator in the class:
`siteSwapImage_not_monomial` (C5D:203). A-3 and A-4 name no matrix. A-5 names its images.

**Consequence of the kinds for CT.** The rule's interface part (A-3, A-4) is formally neutral, and
its generator part (A-1, A-5–A-7) admits named matrices and adds no closure step beyond the shared
A-2 and A-8. So the rule lies inside the restricted shortcut of §4.4, Step 2. `PolC` is exactly
the least label-invariant architecture containing `permClass` and the two images.

***

## 2. Target clauses and their frozen readings

| Clause | Frozen reading for this object |
|---|---|
| **T1** One added rule | The rule text has exactly one clause group outside [N] and the shared interface A-2. Here that group is the polarization map, A-3 to A-7. T1 fails if CC-2 shows that the relabelling closure A-8 carries the target, which would make it a second rule |
| **T2** Genuinely non-stabilizer operation | An operation meeting D3 (§4.3) is available in `polarizedTheoryC (Fin 2)` |
| **T3** Valid measurement instrument | The target family is `InstAvail`. It is then completely positive (`cp_of_instAvail`, IL:541) and trace-summing (`instAvail_trace`, IL:317). The theory's readout is local Lüders (OA:658). The theory is implementation-generated (`genTheory_generated`, IL:926), so it is composite Kraus-sound (`krausSoundExt_of_implementationGenerated`, IL:963). The status is "met through the imported interface A-2", and the rule is never credited with it |
| **T4** Repeatable composition | The target family composes with itself and with every available family by `InstAvail.bind`. It extends by spectators under `ContextStable` and `LabelInvariant` (`instAvail_spectator`, IL:789), both proved for `PolC`. For a repeat-until-success construction, every finite stopped depth is available. The limiting channel (`k → ∞`) is not claimed |
| **T5** Not defined into existence | The circularity test CT (§4.4) returns `generated` |

***

## 3. Already proved versus new obligations

### 3.1 Already proved: kernel at `main@45eea51d`

Support layer K throughout. Nothing in this table is reproved.

| Item | Kernel name | File:line |
|---|---|---|
| The class and its architecture | `PolC`; `polC_arch`; `polC_labelInvariant`; `polGen_le_polC` | PCL:150, 165, 172, 176 |
| The theory | `polarizedTheoryC` | PCL:189 |
| Countable up to scalar; no layer flow | `polC_countable_upToScalar`; `polarizedTheoryC_not_layerFlowExecutable` | PCL:372, 389 |
| Quarter phase at every configuration and level (O1) | `polC_phaseGate`; `polarizedTheoryC_phasesAvailable` | PCL:443, 448 |
| Dagger and context stability | `polC_daggerStable`; `polC_contextStable` | PCL:485, 584 |
| Consequence closure; not QM; extended kill battery | `polarizedTheoryC_derivedOI`; `polarizedTheoryC_not_qm`; `killBattery'_not_qm` | PCL:606, 620, 631 |
| Level-three word and its block | `levelThreeWord_mem`; `levelThree_word_block`; `levelThree_block_not_clifford`; `polC_levelThree_block` | PCL:651, 703, 724, 731 |
| The images, and the swap image's non-monomiality | `siteShearImage`; `siteSwapImage`; `siteSwapImage_not_monomial`; `hadamard_not_monomial`; `hadamard_not_preservesDiag` | C5D:192, 196, 203, 162, 179 |
| The class without relabelling and its theory | `PolGen`; `polGen_arch`; `polarizedTheory` | C5D:221, 234, 247 |
| Half-time swap flow `H·S·H` | `gateFlow_half_eq_hsh` | C5D:287 |
| Kill battery | `KillBattery`; `killBattery_substratum`; `killBattery_not_qm` | C5D:71, 74, 81 |
| B23 (for any architecture holding the three primitives) | `instAvail_attempt`; `attempt_balanced_branch`; `finite_protocol_available`; `balanced_stopped_formula`; `balanced_finite_available`; `finite_protocol_spectator`; `balancedCircuit_isometry`; `correction_isometry` | BFP:212, 194, 236, 245, 256, 269, 159, 173 |
| B23 definitions | `resetPerm`; `balancedCircuit`; `drivePhase`; `correction` | BFP:106, 153, 167, 170 |
| Interface | `InstAvail`; `Architecture`; `ContextStable`; `LabelInvariant`; `ImplementationLocality`; `genTheory`; `genTheory_mono`; `genTheory_generated`; `realized_of_instAvail`; `cp_of_instAvail`; `instAvail_trace`; `instAvail_spectator`; `krausSoundExt_of_implementationGenerated` | IL:268, 506, 359, 364, 370, 852, 919, 926, 530, 541, 317, 789, 963 |
| Coherent one-outcome step ⇒ scaled member | `exists_scaled_mem_of_instAvail_unitary` | MR:251 |
| Monomial class: definition, architecture, invariances | `IsMonomial`; `substratumClass`; `substratumClass_arch`; `substratumClass_contextStable`; `substratumClass_labelInvariant`; `substratumClass_not_countablyCovered` | SI:75; SC:180, 231, 261, 275; CCS:235 |
| Monomial-class instruments preserve the diagonal cone | `classicalClass` (`:= substratumClass`); `classical_instAvail` | PII:39, 168 |
| Stated-access class and theory | `permClass`; `permClass_permMatrix`; `permTheory`; `permTheory_not_qm` | SIA:236, 406, 606, 717 |
| Baseline theory | `substratumTheory` | RB:284 |
| Fresh-ancilla block | `ancBlock` | AC:457 |
| Local Lüders readout | `readout_is_localLuders` | OA:658 |

### 3.2 New obligations for Stage 1B

None of these is attempted here. Each row says where the step came from: an *inventory reading*,
a *reviewer reading* (from the MATH-CON-0 reviews), or *this design*.

| ID | Obligation | Origin | Feeds |
|---|---|---|---|
| **O-1** | Baseline lemma: if an `InstAvail substratumClass` family has a branch equal to `p • conjChannel U`, with `p > 0` and `Uᴴ U = 1`, then `IsMonomial U`. Planned route: `classical_instAvail` (PII:168) gives preservation of the diagonal PSD cone. A conjugation `Ad U` that sends every diagonal rank-one state to a diagonal state has `U` monomial: column `i` of `U` has exactly one nonzero entry, and orthogonality puts these in distinct rows. Proof template: `conj_diag_entry` (DG:90) and the rank-one-indicator column argument of `diagonalGlue_forces_monomial` (DG:101), which use the same technique for a fixed target permutation. `exists_scaled_mem_of_instAvail_unitary` (MR:251) covers single-outcome families only. Stated for the system carrier and for every level | this design; template per review N13 | CC-3; Q2 in CT |
| **O-2** | Ablation inclusion: the least label-invariant architecture generated by `substratumClass` together with the monomial elements of a rule's matrix set is contained in `substratumClass` (from SC:231, SC:275). Also `PolC ⊆ 𝓕` and `PolGen ⊆ 𝓕`, where `𝓕` is the fiat class of CC-1. Transfer of availability by `genTheory_mono` (IL:919) | this design | CT Q2 and FC; CC-1 |
| **O-3a** | `PolC Work balancedCircuit`, through the matrix identity `balancedCircuit = (I⊗H⊗H)·Toff·(S⊗I⊗I)·Toff·(I⊗H⊗H)` (CH1:104–105) with the token as Toffoli's target. The factors: `S⊗I⊗I = siteShearImage 4` (`shear`); `H` on an ancilla bit as `relabel` of `siteSwapImage 4` along a self-bijection of `Work`, or as conjugation by a permutation matrix (`perm`, `mul`); Toffoli as `perm` | inventory reading; reviewer hand check of the identity | route (iii) |
| **O-3b** | `PolC Work (resetPerm j)` for every `j` (`perm`, `permClass_permMatrix`) | inventory reading | route (iii) |
| **O-3c** | `PolC Work (correction j)` for every `j`: the identity for `j = 0`, and `Z⊗I = (siteShearImage 4)²` (`mul`) otherwise | inventory reading; review G3 | route (iii) |
| **O-3d** | Apply `instAvail_attempt` and `balanced_finite_available` with `polC_arch`. This gives, in `polarizedTheoryC (Fin 2)`, the heralded branch `(5/8)·Ad(drivePhase)` and every stopped depth. No carrier transport is needed at system level, because `Token = Fin 2` and system availability is `InstAvail PolC (Fin 2)` (IL:852) | inventory reading, confirmed by review r2 §2 | T2 (monomial part only), T4 |
| **O-3e** | System-level `H`: `PolC (Fin 2) hadamard`, by `relabel` of `siteSwapImage 1` along `Fin 2 × Fin 1 ≃ Fin 2`. Then the coherent target `K*_iii`: the branch `(5/8)·Ad(H·drivePhase·H)` of the bind `op H`, then the attempt, then `op H`. Then the checks that `H·drivePhase·H` meets D2 and D3, by exact algebra: `H·drivePhase·H ∈ M₂(ℚ(i))`, while `H` itself carries the kernel's `hc = 1/√2`, so the branch identity uses `hc² = 1/2`; B23's scalar is typed `(5/8 : ℂ)` and D2's `p` is real, so a cast is needed. Depth form for T4: the stopped loop conjugated by `H` through `bind`, `(1 − (3/8)^k)·Ad(H·drivePhase·H) + (3/8)^k·id`, available at every finite depth `k` | inventory reading; reviewer reading (the 3-4-5 rotation about `X`); review N9, N12 | T2, T4 |
| **O-4** | Route (ii), alternative: a heralding instrument whose branch is proportional to `Ad(levelThreeBlock)` on `Fin 2 × Fin 1`. It uses uniform attach of `Fin 3`, a reset to the input fiber `1` and a readout of fiber `0`, because `InstAvail` has no pure-ancilla preparation. The block's membership is already kernel (PCL:731). Then the transport to `Fin 2`, and the D2/D3 checks on the reflection `R` and on `R·Z` with `Z = S²` | inventory reading; reviewer readings F6, F7 | T2 (alternative) |
| **O-5** | Route (i), alternative: an exact characteristic polynomial of the level-three hexagon product of `relabel`ed swap images. D3 as frozen is defined on a qubit carrier (§4.3), so route (i) is scorable for T2 only after an amendment declares an encoding for `Fin 2 × Fin 3`. The numerical record of infinite order never counts | inventory reading; reviewer reading F6 | supplementary |
| **O-6** | CC-2 comparison: decide whether `K*` is available in `polarizedTheory (Fin 2)` (`PolGen`). Otherwise, show that every use of `relabel` in `K*`'s `PolC` derivation is either reproduced on the same carrier by conjugation with a `permClass` member, or is the carrier transport `Fin 2 × Fin 1 ≃ Fin 2`. *Reviewer reading (pointer, not a result):* `ancBlock (siteSwapImage 1) 0 0 = hadamard` (AC:457, C5D:196), so `PolGen.block 1 _ 0 0 (PolGen.swap 1)` places the system-level `H` in `PolGen (Fin 2)` without `relabel`; the ancilla-bit `H` of O-3a is `P·(H⊗I)·Pᵀ` with `P ∈ permClass` (`perm`, `mul`); route (ii) uses `relabel` essentially (PCL:731–733) | this design; review N2 | T1 |
| **O-7** | Carrier transport `Fin 2 ≃ Fin 2 × Fin 1`, needed only for level-indexed restatements (`availExt`) | inventory reading | T4 (level form) |
| **O-8** | The CT runs of §4.4 on the object and on CC-0, CC-1 and CC-4 (DV-a to DV-e) | this design | T5; controls |
| **O-9** | Spectator form of `K*`, through `instAvail_spectator` with `polC_contextStable` and `polC_labelInvariant` | this design | T4 |
| **O-10** | Lowest non-monomial node: in a derivation whose leaves are monomial, the first node carrying a non-monomial matrix applies a constructor that does not preserve monomiality. The constructors of A-2 and A-8 preserve it (SC:231, SC:275), and an `InstAvail` family whose realization uses only monomial class members has no D2 branch (O-1). Needed for Q2 = no for rules outside the restricted shortcut, here DV-d | this design | CC-4 (DV-d); CT Step 2 |

***

## 4. Frozen definitions

These are fixed before any result. They change only by an amendment in `amendments/`, made
before the result they would affect is known.

### 4.1 D1: the monomial baseline

- **The baseline class.** `𝓑 := substratumClass` (SC:180): at every finite carrier, every matrix
  `permMatrix σ * diagonal d` with arbitrary complex `d` (`IsMonomial`, SI:75). It contains
  `permClass`, every diagonal matrix (zeros included), and so every partial permutation with
  phases.
- **The baseline theory.** `𝔅 := substratumTheory (Fin 2) = genTheory substratumClass
  substratumClass_arch (Fin 2)` (RB:284). It is a kill-battery member (C5D:74), so it is not QM
  (C5D:81).

**Why all monomials and not `permClass`.** This choice is fixed by the decision question, not by
any outcome.
1. *Alignment with T2.* The T2 criterion must exclude monomial operations (inventory §1 hazard
   (b); D3 below). If the baseline were `permClass`, then monomial operations outside `permClass`
   would count as new contributions of the rule while not counting toward T2. Examples are the
   quarter phase `S`, `Z⊗I` and `drivePhase`. The baseline and the T2 exclusion would then
   disagree. With `𝓑 = substratumClass`, the baseline is exactly the set the T2 exclusion
   removes. The only contribution a rule can be credited with is non-monomial content, which is
   what the decisive question asks about.
2. *The stricter comparison.* `substratumClass ⊇ permClass`. Every comparison of the form "is X
   new relative to the baseline" is therefore at least as hard to pass against `𝓑` as against
   `permClass`.
3. *Nonvacuity is checked, not assumed.* `𝓑` contains every hazard operation of the inventory's
   §1: Toffoli, the controlled quarter phase `diag(1,1,1,i)` and `drivePhase` are all `IsMonomial`
   by definition. Its diagonal content is uncountable (CCS:235). CC-3 requires D3 to reject each
   of them.

The stated-access theory `permTheory` (SIA:606) stays a recorded comparator, and A-1 is its class.
It is not the baseline.

### 4.2 D2: coherent non-monomial operation

An operation is *coherent non-monomial* in a theory `𝔗` on carrier `T` when all of the following
hold. Here `T` is `Fin 2`, or `Fin 2 × Fin n` at level `n`.
- There is an available family `F : O → Channel T`: `𝔗.avail` or `𝔗.availExt n`. For
  `genTheory 𝓘`, both mean `InstAvail 𝓘`.
- For some outcome `o`, `F o = p • conjChannel U` as linear maps, where:
  - `p` is real with `0 < p ≤ 1`, so the branch probability is independent of the input;
  - `Uᴴ U = 1`;
  - `¬ IsMonomial U`.

`p = 1` is allowed, for a deterministic operation. Given a concrete `U`, monomiality is decided by
its support pattern: at most one nonzero entry in each row and each column.

### 4.3 D3: the T2 criterion (genuinely non-stabilizer)

A D2 operation on the declared encoded qubit `T = Fin 2` (the system carrier, `Token`) whose `U` is
non-Clifford:
- some `P ∈ {X, Z}` of the computational basis of `Fin 2` has `U P Uᴴ` not proportional to any of
  `I, X, Y, Z`.

Decision is by exact algebra on the entries of `U`. A level-one operation on `Fin 2 × Fin 1` counts
after transport O-7. Other carriers need an amendment that declares their encoding before they
are scored.

D3 deliberately has these features:
- **It excludes monomials.** Non-Clifford monomials, such as `drivePhase`, Toffoli and controlled
  `S`, do not count (inventory §1 hazard, points 1 and 2).
- **It does not require infinite order.** A finite-order non-Clifford non-monomial operation
  counts. Infinite projective order is recorded as an attribute, not a criterion. The reasons:
  - owner refinement 2: U2 does not exclude every finite-order non-Clifford operation in a
    different extension;
  - infinite order does not separate the target from the baseline (hazard point 2).
- **It does not by itself decide T5.** By hazard point 3, one coherent Clifford with native
  monomials meets D3 through B23-type circuits. T5 is decided by CT alone.

### 4.4 CT: the circularity test ("generated" versus "installed")

The test answers the owner's two questions. Q1: is the coherent operation the image of a stated
map applied to a stated generator, or built from such images? Q2: can it be derived from the rule
plus native or monomial generators without naming its image?

#### Clause kinds

Each clause of a rule has exactly one kind, read from its text before any derivation.

| Kind | Definition | Marked when applied? |
|---|---|---|
| **G-n**, naming generator clause | Makes operators or channels admissible or available, and its text refers to specific matrices. This covers: a constant; a formula; a stated map at stated inputs; a relabelling, transport or scalar multiple of a stated matrix; a condition that mentions stated matrices, *whether or not* it fixes the operator up to a scalar; and a closure step that combines class members with a stated matrix, such as `K ↦ K·M`. A G-n clause has the *admission form* when it only admits matrices and adds no closure step | Yes: every node that applies it and carries a non-monomial matrix |
| **G-u**, uniform closure law | A closure constructor whose text quantifies uniformly over all class members and refers to no specific matrix. Examples: `mul`, `smul`, `block`, `relabel`, and the superposition law of CC-0 | No |
| **I-f**, formally neutral interface clause | Describes the carrier, identification or access, and leaves A-2 formally unchanged: the same carrier type, the same `InstAvail` rules, and no stated matrix | No; it has no node |
| **I-m**, interface clause that changes A-2 | Changes the carrier, identification, preparations, readout, discard or composition rules formally. Every effect, projector, prepared state or channel its text states is a stated matrix | Yes: every node that uses a stated non-monomial matrix of the clause |

The shared constructors of A-2 and A-8 are not clauses of any rule. `proj` names only 0/1
diagonal projectors, which are monomial, so it never carries a marked node.

#### Inputs

| Input | Content |
|---|---|
| **I-1** Baseline | `𝓑 = substratumClass` (D1) |
| **I-2** Rule text `ℛ` | A finite list of clauses. Each is tagged with its class ([N]/[R]/[Q]/[P]) and its kind (G-n, G-u, I-f or I-m) |
| **I-3** Stated matrices `Mat(ℛ)` | Every matrix that the text of a G-n or I-m clause states. For a family-valued specification, a condition on stated matrices, every member of the family. For a channel or instrument that the clause *itself* states, its Kraus operators and effects; such a channel counts as monomial only if it has a Kraus representation by monomial matrices. A channel that becomes available only through derivations in `𝔗_ℛ` is not in `Mat(ℛ)` |
| **I-4** Target `K*` | An operation meeting D2. For T5 to bear on T2, it also meets D3 |
| **I-5** Derivation `d*` | A finite derivation tree of `K*` in the rule's theory `𝔗_ℛ`. Each node, leaf or internal, carries a concrete matrix or channel and names the clause, constructor or `InstAvail` rule it applies |

Write `NM(ℛ) := {M ∈ Mat(ℛ) : ¬ IsMonomial M}`.

#### Procedure

- **Step 1 (Q1, the image question).** Mark every node of `d*`, leaf or internal, that applies a
  G-n clause and carries a non-monomial matrix, or that uses a stated non-monomial matrix of an
  I-m clause. Record the clause that supplies each marked node.
  - Q1 = yes iff at least one node is marked.
  - Q1 is decided by inspecting the finite tree `d*`.
- **Step 2 (Q2, derivation without naming).**
  - Q2 = yes iff a derivation `d'` of a D2 operation is exhibited in `𝔗_ℛ` such that `d'` has no
    marked node and uses at least one clause of `ℛ`. If T2 is being scored, the operation must
    also meet D3. The operation `d'` derives need not be `K*`. If it differs, it is the reported
    T2/T5 witness, and T3 and T4 are checked for it.
  - Q2 = no iff it is proved that every such derivation has a marked node.
  - Otherwise Q2 = undetermined.
  - **Restricted shortcut.** Suppose every clause of `ℛ` is I-f or G-n of the admission form. The
    rule's class is then the least label-invariant architecture containing `𝓑`, or the [N] class
    `permClass`, together with the admitted matrices. In that case Q2 = no follows from O-2 and
    O-1. A derivation with no marked node uses only monomial admitted matrices, so by O-2 its
    class lies inside `substratumClass`, and by O-1 it has no D2 branch.
  - A rule that adds a closure step (G-u, or G-n not in admission form) or an I-m clause is
    outside the shortcut. Its Q2 is decided by exhibition or by proof. One proof method is O-10,
    the lowest non-monomial node: in a derivation from monomial leaves, a non-monomial matrix
    first appears at a node whose constructor does not preserve monomiality. The constructors
    of A-2 and A-8 preserve it (SC:231, SC:275). So if every non-preserving constructor of `ℛ`
    is G-n or I-m, that node is marked.
- **Step 3 (FC, the fiat check).** Let `𝓕_ℛ` be the least label-invariant architecture containing
  `𝓑` together with the square matrices of `NM(ℛ)`, and let `𝔉_ℛ := genTheory 𝓕_ℛ`.
  - FC = yes iff `K*` is shown available in `𝔉_ℛ`.
  - FC = no iff it is shown unavailable there.
  - Otherwise FC = undetermined.

#### Verdict

The verdict is generated from (Q1, Q2, FC) by this table, read top to bottom:

| Condition | Verdict |
|---|---|
| Q2 = yes | `generated` |
| Q2 = no, Q1 = yes, FC = yes | `installed`: the rule's non-monomial matrices are the target's source, and they suffice by fiat |
| Q2 = no, Q1 = yes, FC = no | `mixed`: non-monomial matrices are named, and they do not suffice without the rule's other clauses. The record states which part each contributes |
| Q2 = no, Q1 = no | inconsistent: `d*` would be a derivation without a marked node. CT is void |
| any other combination | `undetermined` |

T5 holds iff the verdict is `generated`.

**Class disclosure beside the verdict.** The outcome record states every clause's class ([R] or
[Q]) beside the CT verdict. `generated` means that no operation is named specifically. It does not
mean that the rule imports no quantum structure: CC-0's [Q] superposition law is `generated`.

**Scope of CT.** CT as frozen applies to rules on the operator-level interface A-2. There,
identifications are carrier relabellings, and "monomial" is the operative test. Shapes 1 and 2
(§7) identify configuration laws through frames. For them "monomial" is not the relevant
criterion, so the same two questions need a frame-level CT variant. That variant is frozen in the
amendment or preregistration that takes the shape up, before any result for that shape.

#### CC-0 rechecked under clause-instance marking

`ℛ_0`'s only clause is the superposition law. It quantifies uniformly over the class and refers to
no matrix, so it is G-u and `Mat(ℛ_0) = ∅`. The exhibited `d'` has:
- leaves `X = permMatrix (swap 0 1)` and `Z = diag(1, −1)`, both in `𝓑` and monomial;
- one internal node, the G-u law applied to `(X, Z)` with `a = b = 1/√2`, which is unmarked;
- the root `op H`.

No node is marked, so Q2 = yes and CT returns `generated`. `ℛ_0` adds a closure step, so the
restricted shortcut does not apply to it, and the shortcut and the exhibited `d'` do not conflict.
The independent review of `e593465b` (§C.5) checked the same derivation.

### 4.5 Choices not ruled by the owner

Three elements of CT and of the outcome record go beyond any owner ruling. They are the writer's
choices, stated here so that the owner can rule on them.

1. **A characterization counts as naming.** This includes family characterizations: a G-n clause
   is any condition that mentions stated matrices, whether or not it fixes the operator. As a
   consequence, every formulation of A-5 as the Weil representation is marked: literal images, an
   intertwiner definition through the action on `X` and `Z` (DV-b), or a family (DV-e). CT
   therefore treats any formulation of the Weil clause as `installed`. The reason: the action on
   `X` and `Z` fixes `H` up to a scalar and is its definition.
2. **The form of the missing rule in (C).** CT entails only this: the missing rule is a clause
   that states no non-monomial matrix in the sense of §4.4 and yields a D2 (D3) operation. That
   means a G-u law, an I-f clause, or an I-m clause whose stated matrices are monomial. The
   narrower requirement, that it be an access or identification clause, comes from the owner's
   wording in 6721267600: "identify the missing access or identification rule". It is not a
   consequence of CT. The (C) record states both forms and attributes each to its source.
3. **Leniency toward uniform closure laws.** A G-u law is never marked, even when it is [Q], as
   CC-0's superposition law is. CT detects operation-specific naming, not imported quantum
   structure. The question of quantum import moves to the class disclosure beside the verdict.
   The owner has not ruled on this.

***

## 5. Countercontrols and controls, with decidable rejection rules

Controls are reported before any verdict in the Stage 1B result record.

**Routing.**
- A control is *refuted* when its pass condition is shown false. A refuted CC-0, CC-1, CC-3(a) or
  CC-4, or a failed CC-2(b) where it applies, shows a defective test or definition. The outcome
  goes to order 0 of §6: (I), void, with the control named.
- A control that is *vacuous* or *not established* is not a pass. (P) and (C) require it passed.
  The outcome then goes to (N) if (N)'s own condition holds, and to (I) at order 4 otherwise.
- *Why vacuity does not void at order 0.* CC-1(a) is vacuous exactly when `K*` is not shown,
  which is the case when ¬T2 holds. Voiding at order 0 would pre-empt a legitimate (N). This
  departs from the review's N4 wording for that reason.

| ID | Control | Construction | Pass condition (decidable) | Rejection rule |
|---|---|---|---|---|
| **CC-0** | Calibration for `generated`. A fixture, not a candidate; [Q], superposition closure; excluded from every outcome | `ℛ_0`: one G-u clause. If `K, L ∈ 𝓘` on one carrier and `aK + bL` is unitary for some `a, b ∈ ℂ`, then `aK + bL ∈ 𝓘`. Otherwise `𝓑` with the architecture and relabelling. `Mat(ℛ_0) = ∅`. Target `H = (X + Z)/√2` on `Fin 2`, where `X` is `permMatrix (swap 0 1) ∈ permClass` and `Z = diag(1, −1) ∈ 𝓑` | CT returns `generated`, with the exhibited `d'` of §4.4 | Any other verdict shows that CT cannot return `generated` for a rule that names no matrix. Refuted, order 0 |
| **CC-1** | Coherent Clifford by fiat | `ℛ_1`: one G-n clause of admission form, `siteSwapImage n` admissible for every `n`, with no polarization map. Class `𝓕` = the least label-invariant architecture containing `𝓑 ∪ {siteSwapImage n}`. Theory `𝔉 := genTheory 𝓕 (Fin 2)`. By O-2, `PolC ⊆ 𝓕` | (a) Nonvacuity: the object's target `K*` is shown available in `𝔉`. This follows by O-2 and `genTheory_mono` once it is shown in `polarizedTheoryC`. (b) CT returns `installed` for `ℛ_1`, which lies in the restricted shortcut | (b) any other verdict: refuted, order 0. (a) false while `K*` is shown in `polarizedTheoryC`: O-2 is false; recorded; refuted, order 0. (a) not shown: vacuous, so not a pass (routing above) |
| **CC-2** | `PolGen` versus `PolC` | `polarizedTheory (Fin 2)` (C5D:247), without `relabel`, against `polarizedTheoryC (Fin 2)` | (a) T1 accounting: `K*` is available in `polarizedTheory (Fin 2)`, or O-6's alternative holds. Either way, the relabelling closure is not a second rule. (b) Applies only when `K*` is available in both theories: CT returns the same verdict for `PolGen` and for `PolC` | (a) refuted, meaning `K*` is proved unavailable in `polarizedTheory (Fin 2)` beyond the named transport: T1 is recorded as two rules (map and relabelling closure). (a) undetermined: T1 is undetermined. (b) fails where it applies: refuted, order 0 |
| **CC-3** | Monomial-only baseline, kill battery, with the `substratumClass` hazard | `𝔅 = substratumTheory (Fin 2)`, with no rule | (a) No D2 operation in `𝔅` at any level (O-1) | (a) refuted: D2 is defective, since it admits a monomial-class operation; order 0. (a) not established: not a pass. The restricted shortcut is then unavailable, Q2 is `undetermined` for every rule inside it, and (P) and (C) are unreachable |
| **CC-3(b)** | Definitional calibration of D3 on the hazard operations. It is recorded, and it cannot fail | — | `drivePhase` passes D3's non-Clifford clause (`D X Dᴴ = (3/5)X + (4/5)Y`) and is rejected only by the monomial clause, which is the clause that does the work. The controlled quarter phase on `Fin 2 × Fin 2` and Toffoli on `Work` are monomial, and they are also outside D3's carrier `Fin 2` | — |
| **CC-4** | Disguised variants. Each is stated at every level `n` with the ancilla a spectator, as the object's images are | DV-a: the swap image stated as "the normalized finite Fourier transform on the position alphabet", `(a, b) ↦ (−1)^{ab}/√2`. DV-b: by characterization, "the unitary, unique up to scalar, with `W X Wᴴ = Z` and `W Z Wᴴ = X`", where `X` and `Z` are monomial. DV-c: the swap image placed only as `reindex e e (siteSwapImage n)` for a fixed nontrivial carrier bijection `e`, for instance on an ancilla bit. DV-d: a constant inside a closure step, "if `K ∈ 𝓘` on `Fin 2 × Fin n`, then `K·siteSwapImage n ∈ 𝓘`". DV-e: a family characterization, "the swap layer goes to some unitary `W` with `W X Wᴴ = Z`", whose solution set `{diag(e^{ia}, e^{ib})·H}` is not unique up to a scalar | CT returns `installed` for each of DV-a to DV-e, with target `K*`. DV-a, DV-b, DV-c and DV-e lie in the restricted shortcut. DV-d adds a closure step, so its Q2 = no needs O-10 | Any variant classed otherwise: refuted, order 0 |

CC-1 and CC-4 must return `installed`, and CC-0 must return `generated`. These are requirements
on the test, preregistered as rules. They are not predictions of the object's result. DV-d and DV-e
are the two relocations that a leaf-only marking would miss: a constant inside a closure step,
and a characterization that is not unique up to a scalar.

***

## 6. Outcomes: a total, ordered partition

The outcome is evaluated after every control. The first matching row wins. Write
**Ctrl** for the condition that CC-0, CC-1, CC-3(a) and CC-4 are all passed, and that CC-2(b) is
passed wherever it applies.

| Order | Outcome | Condition |
|---|---|---|
| 0 | → (I), void | A control is refuted (§5, routing). Or CT is inconsistent. Or both T2 and ¬T2 are proved. The record names the failure |
| 1 | **(P)** positive and noncircular | Ctrl ∧ T1 met (CC-2(a) passed) ∧ T2 met (D3, at the support standard below) ∧ T3 met (imported, disclosed) ∧ T4 met ∧ CT = `generated` |
| 2 | **(C)** conditional and partial | Ctrl ∧ T2 ∧ T3 ∧ T4 ∧ [(CT ∈ {`installed`, `mixed`}) ∨ (CT = `generated` ∧ CC-2 records two rules)]. The first disjunct is (C-inst); the second is (C-T1). Row 2 is exactly the union of the two sub-labels |
| 3 | **(N)** negative or obstruction | ¬T2 proved for the object at the support standard: no available family of `polarizedTheoryC (Fin 2)` has a branch meeting D3. Or ¬T3 or ¬T4 proved for every T2 witness. A failed route alone is not (N) |
| 4 | **(I)** inconclusive | The remainder. Examples: T2 neither established nor refuted; CT `undetermined` while T2 holds; CT = `generated` with T1 undetermined; a control vacuous or not established; Stage 1B not authorized or not completed |

The owner's record (6720678942) names three outcomes: positive, conditional/partial and negative.
(I) is the remainder that makes the partition total. It is not a fourth kind of result.

The partition is disjoint:
- (P) requires CT = `generated` with T1 met.
- (C) requires CT ∈ {`installed`, `mixed`}, or CT = `generated` with two rules. Either excludes
  (P).
- (N) requires ¬T2, while (P) and (C) require T2. A proof of both is void at order 0.

**Support standard for T2.** An established T2 needs either a kernel theorem, or an exact written
derivation with a recorded independent review. Numerical evidence never counts. The outcome
record names the weakest support layer among its links, and states the classes of the rule's
clauses beside the CT verdict (§4.4).

**Required content of a (C) record.**
- The existing mathematics is stated as valid, with its conditions.
- The milestone is stated as not reached.
- The missing rule is identified by the three items below.

Per the owner's ruling, (C) is not recorded as failure.

**Identifying the missing rule in (C).**
1. Each marked node of `d*` and the clause that supplies it. For the object, these are expected
   to be the `PolC.swap` nodes, supplied by A-7 through A-5.
2. The form of the missing rule. The form CT entails: a clause that yields a D2 (D3) operation,
   from native or monomial data, in a derivation with no marked node. That is a G-u law, an I-f
   clause, or an I-m clause whose stated matrices are monomial. The narrower form from the
   owner's wording: an access or identification clause of that kind. Each form is stated and
   attributed to its source (§4.5, item 2).
3. Which of the preserved routes and shapes (§7) could supply such a rule. None is chosen. For
   shapes 1 and 2 the frame-level CT variant is not frozen. They are named as possible sources
   and are not scored against the operator-level form.

**Mapping onto the target clauses.**

| Outcome | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| (P) | ✓ | ✓ | ✓ (imported A-2) | ✓ | ✓ (`generated`) |
| (C-inst) | ✓, ✗ or undetermined, as CC-2 records | ✓ | ✓ (imported A-2) | ✓ | ✗ (`installed` or `mixed`) |
| (C-T1) | ✗ (two rules) | ✓ | ✓ (imported A-2) | ✓ | ✓ |
| (N) | as recorded | ✗ (proved) | — | — | — |
| (I) | any | unresolved, or void | any | any | unresolved, or void |

**What MATH-CON-1 can settle on this object.** On this object, MATH-CON-1 tests whether the rule
is sufficient for T2–T4, and identifies the missing rule. It cannot settle T5. The reason, which
follows from the frozen definitions before any result, holds conditionally on O-1 and O-2:
- The rule admits `siteSwapImage n` by `PolC.swap`, a G-n clause in admission form, and that
  matrix is non-monomial (C5D:203). Every `swap` node is marked.
- Suppose O-2 and O-1 hold. A `PolC` derivation with no `swap` node lies inside
  `substratumClass` and has no D2 branch, so Q2 = no by the restricted shortcut (§1.3, last
  paragraph). And `PolC ⊆ 𝓕` gives FC = yes whenever T2 holds in `PolC`. So CT = `installed`
  whenever T2 holds.
- The reachable labels are (C-inst) with CT = `installed`, (N) and (I). The other labels are
  excluded for these reasons:
  - (P) and (C-T1) both need CT = `generated`;
  - `mixed` needs FC = no, which `PolC ⊆ 𝓕` excludes once T2 holds; the object also has no I-m
    clause.
- If O-1 or O-2 is refuted, CC-3(a) or CC-1(a) is refuted, and the outcome is void at order 0. If
  either is only not established, Q2 is `undetermined`, CT is `undetermined`, and the outcome is
  (I).
- To reach `generated`, the map would have to be restated so that no G-n clause admits the swap
  image. The image would instead have to follow from a G-u law or an interface clause. That
  restatement is a new premise, outside this preregistration, and it would need an amendment and
  owner authorization.

Most of this follows from the object and the question, which the owner chose. The three choices
of §4.5 are the writer's. CC-0 shows that CT itself can return `generated`.

***

## 7. Alternative routes and shapes, preserved

No route or shape is chosen beyond the owner's ruling: A10/`PolC` with B23 first.

| Route or shape | What it is | Condition for taking it up |
|---|---|---|
| **Route (iii)**, B23 transfer | O-3a–O-3e, O-9 | Primary, by owner ruling 1 |
| **Route (ii)**, level-three fiber block | O-4. Membership is already kernel (PCL:731). It needs a heralding instrument (reset and readout) and the transport | Taken up if an obligation of route (iii) is refuted, or blocked at a recorded wall, or if the owner authorizes it as an independent second witness for T2. CT's verdict does not depend on the route, because every route has marked `swap` nodes |
| **Route (i)**, level-three hexagon product | O-5 | Only after an amendment declares an encoding of `Fin 2 × Fin 3` for D3, and only if routes (iii) and (ii) are both blocked. Its numerical record of infinite order does not count |
| **Shape 0** | Routes (i)–(iii) on A10. This preregistration | Current |
| **Shape 1**, non-injective protected-functional access rule (encoded frameworks; for example a Lemma Q-type conserved form, or M-INACC) | A single rule making one ontic functional per encoded system inaccessible | After MATH-CON-1 reaches (C) or (N), as a candidate for the missing rule. It needs its own preregistration, a frame-level CT variant, and owner authorization. If #1198 has landed by then, M-INACC is re-read on `main`. NC and U2 constrain it within their hypotheses (§8) |
| **Shape 2**, a changed identification paired with nonlinear native transport (`G_SM`) | One rule replacing R1 by an identification under which P★-type conditioning is completely positive | Under the same conditions as shape 1. In addition, the preregistration states whether the dynamics and the identification together count as one rule for T1 |
| **Shape 3**, coherent mixing from B1's native template with a phase-congruent readout quotient | The readout quotient is the single rule | Under the same conditions as shape 1. In addition, E-real, E-pair and isolation are counted against T1. The quadratic sensor is disclosed as [Q] |

***

## 8. Theorems NC and U2, within their exact hypotheses

Source: M2D nodes 2–4 and 7–8 (M2D:404–410 for U2; M2D:485–498 for NC). Both are paper records on
`main`, and neither is kernel-checked. They are stated here only for scope, and neither is an
input to the object.

**Shared hypotheses (Lemma F).**
- **H-F1:** one fixed bijection of a finite configuration set acts at every tick.
- **H-F2:** the observer's operations are exactly these: attach cells in fixed nonnegative laws,
  apply the bijection, feedback, discard by marginalization, and condition on configuration
  records.
- **H-F3 (H-LIFT):** every cell correlated with the encoded carrier at an operation's input
  belongs to it.
- **H-F4:** a linear identification by an orthogonal frame of unit-trace operators: R1^⊗n at
  `q = 2`, R-W at odd `q`.

**Theorem U2** is stated only for R1^⊗n at `q = 2`.
- (i) An ontic permutation acts completely positively iff it lies in `A_4 ≀ S_n`.
- (ii) Under H-F1–H-F3 with injectivity, every heralded encoded unitary branch with
  input-independent `p > 0` lies in that group.

*Owner refinement.* U2 restricts the available encoded unitaries only under its finite-frame and
operation-set assumptions. It does not exclude every finite-order non-Clifford operation in a
different extension. Its odd-`q` analogue is MECH-1's Proposition AS and Theorem W, not U2.

**Theorem NC.** Assume H-F1–H-F4 with an injective identification, and take as operational
equivalences equal operators and equal maps. These coincide with statistical equivalence when the
reachable preparations and reads span. Then the laws, branch matrices and response functions form
a preparation-, transformation- and measurement-noncontextual model, whatever the bijection. At
`q = 2`, spanning needs a `Y` read that is not exhibited natively.

*Owner refinement.* NC supplies a noncontextual model under its identification and spanning-read
conditions. Noncontextuality alone does not rule out every state labelled non-stabilizer under a
chosen representation. MECH-2's P★ is such a state, inside a model whose instrument fails
complete positivity. The milestone therefore tests the full operation together with its
measurement instrument, for validity (T3) and composability (T4), and not a state label.

**Applicability to the object.** Neither theorem applies. The polarization map identifies native
layers with operators (`swap ↦ H`). It is not a nonnegative frame on configuration laws, and the
object's operations are the `InstAvail` rules, not H-F2. So H-F2 and H-F4 fail (inventory A10
row). The consequences:
- No outcome of MATH-CON-1 on the object is presented as escaping, contradicting or confirming NC
  or U2.
- For shapes 1 and 2, both theorems constrain the candidate within their hypotheses. Their
  preregistrations state which hypothesis the candidate leaves, as in inventory §7(b).

***

## 9. Statuses

| Status | Meaning | Applies here to |
|---|---|---|
| **proposed** | Stated as a candidate rule, with no claim that it suffices | The polarization map (A-3 to A-7), in Stage 1A and after Stage 1B. The corpus does not supply it (C5A:249) |
| **mathematically sufficient** | Proved, at a stated support layer, that the rule plus the disclosed inputs (A-1, A-2, A-8) yields the stated target clauses | Reachable in Stage 1B for T2–T4 under (P) or (C). Under (C) it is reported as sufficient for T2–T4 with T5 not met, and conditional on A-2 [Q] and on the map's [Q] images |
| **derived from native OI** | The rule itself is proved from [N] premises | Not claimed and not in scope. Sourcing the map is the physical-selection workstream's question |

No outcome promotes the map's status beyond *proposed*. No outcome is presented as derived from
bare OI.

***

## 10. Process

### 10.1 Stage boundary

This file is Stage 1A, the preregistration. **Stage 1B** is the derivation, the Lean membership
proofs O-1 to O-9, the CT runs and the result record. It needs a separate recorded owner
authorization. Stage 1B writes `RESULT.md` in this directory, with the control table first and
the outcome generated from §6.

Amendments to §§1–7 go in `amendments/`, are reviewed, and land before any result they affect.

### 10.2 §A.41: invariants and their checkpoints

| Invariant asserted | Checkpoint that measures it |
|---|---|
| Stage 1A contains no derivation, Lean, computation or new premise | The commit adding this file changes exactly one path, this file (`git show --stat`). No `.lean`, `.py` or result file is added |
| Definitions D1–D3, CT and the controls are frozen before any result | At Stage 1B's result commit, `git diff <this commit> -- DESIGN.md` is empty. Any change sits in `amendments/`, with a commit earlier than the first commit adding a result file |
| The baseline is `substratumClass` | Same checkpoint, together with grep for `𝓑 := substratumClass` in §4.1 |
| Controls are reported before the verdict, and a failed control voids it | `RESULT.md` has a control table whose rows are CC-0 to CC-4, each pass or fail with evidence, and a verdict section whose derivation from §6 cites those rows. A reviewer checks the order-0 row |
| Every citation is pinned to `main@45eea51d` | Every `github.com/.../blob/` or `/tree/` link in this file contains `45eea51d67237f2a41865dd7efc1ea97e2bc904f` (grep) |
| Every cited kernel name exists at the cited file and line | `git grep -n` of each §3.1 name at `45eea51d`, compared with the table. Run by the writer before commit; re-run by the reviewer |
| No kernel name of the read-write-sourced family is cited | grep for that family's identifier prefix (`readWrite` immediately followed by `Sourced`) in this file returns no line |
| No content of #1203–#1205 or #1198 is used | §11 classifies #1198 as provenance; the reviewer confirms that no claim here rests on it |
| Status never exceeds *proposed* for the map | §9; the reviewer checks the outcome text in Stage 1B against §9 |
| Stage 1B starts only under a separate owner authorization | `RESULT.md` quotes the authorizing owner comment with its author and time, and the first Stage 1B commit is later than that comment |
| Clause kinds (§1.3) are fixed before any derivation | Covered by the frozen-definitions checkpoint: the §1.3 kind column is unchanged at the result commit |
| CT can return `generated`, and its marking catches relocated naming | `RESULT.md`'s control table reports CC-0 as `generated` and DV-d and DV-e as `installed` |
| The class of every rule clause is stated beside the CT verdict | The verdict section of `RESULT.md` carries the class column of §1.3 for the rule's clauses |

### 10.3 Hazards with cheap mitigations, carried as checkpoints

- **H-1.** A route's T2 witness could be monomial and be scored by mistake. Mitigation: the D3
  check rejects monomials, and CC-3(b) records that the monomial clause alone rejects
  `drivePhase`.
- **H-2.** CT could be unable to return `generated`. Mitigation: CC-0.
- **H-3.** CT could misclass a renamed or characterized `H`. Mitigation: CC-4 (DV-a to DV-c).
- **H-5.** Naming could be relocated so that no leaf carries it: a constant inside a closure
  step, or a characterization that is not unique up to a scalar. Mitigation: clause-instance
  marking (§4.4) and CC-4 (DV-d, DV-e).
- **H-4.** The relabelling closure could act as a hidden second rule. Mitigation: CC-2.

***

## 11. §A.42 item 8: references not on `main`

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 6721267600 (amaybaum, 2026-11-08T12:05:53Z) | Authority: rulings 1–3 and the quoted passages | Provenance (authorization); quoted with author and time |
| #1169 comment 6720678942 (amaybaum, 2026-11-08T11:03:23Z) | Authority: target, classes, refinements | Provenance (authorization); quoted with author and time |
| MATH-CON-0 inventory r3 (#1169 comments 6721102809, 6721121369; sha256 `e68058ba…28df5`) | Rows, routes, shapes, hazard, gap assessment | Provenance. Every kernel item used here was re-read at `main@45eea51d` (§3.1). Every inventory reading is carried as a new obligation (§3.2), not as support |
| MATH-CON-0 reviews (#1169 comments 6721133702, 6721137458) | Reviewer readings: the circuit identity, `H·D·H`, `R` checks, the routes | Provenance. Carried as obligations O-3a, O-3e and O-4, not as support |
| #1198 (open pull request, M-INACC; not merged at `45eea51d`; owner-approved for normal merge after #1199 in 6721267600) | Shape 1, a pointer only | Provenance only. Its title and state were read; its content was neither read nor used. Shape 1's take-up re-reads it on `main` if it has landed |
| KT4-PREM-1 design modules (`kt4_forward_ie1`, `fourCopyCoherent_of_kt4Core`) at `ff9c3a358c57ce938978f15f2915d2145ae7b4a5`, not an ancestor of `45eea51d`; no Lean module on `main` contains them | Not used. The K-chain is not an input (§1.1) | Provenance only. No claim here uses them. The support gap belongs to the frozen KT4-PREM-1 record (inventory §7(c)1) and is not inherited |
| OI-FINITE-PROTOCOL-1 design commit `70815342` | B23's history | Provenance. The proof bodies cited (BFP) are on `main` |
| Independent review of r1 at `e593465b` (session scratchpad, `REVIEW-MATHCON1-e593465b.md`) | r2 revisions (§13); reviewer readings in O-1, O-3e and O-6 | Provenance. Its readings are carried as obligations or pointers, not as support |

No claim in this file rests on content off `main`. Every support citation is to `main@45eea51d`.

***

## 12. Scope and non-claims

This file:
- proves nothing;
- adopts no premise;
- chooses no route beyond the owner's ruling;
- runs no computation or Lean build.

Specifically:
- The membership lemmas of route (iii) are new obligations, not results.
- The paragraph "What MATH-CON-1 can settle on this object" in §6 says what CT can return on the
  object as recorded, conditionally on O-1 and O-2. It is not an outcome.
- The three choices of §4.5 are the writer's, not owner rulings.
- The CC-0 fixture is a calibration of the test. It is not a candidate rule, it is not adopted,
  and it enters no outcome.
- Nothing here bears on a manuscript.

***

## 13. Dispositions of the independent review of r1 (`e593465b`)

| Finding | Change in r2 |
|---|---|
| B1: leaf-only marking and scalar-unique characterizations can be evaded; CC-4 cannot fail | §4.4: clause kinds G-n, G-u, I-f, I-m; Step 1 marks every node, leaf or internal, that applies a G-n clause (or uses a stated I-m matrix) and carries a non-monomial matrix; G-n covers conditions on stated matrices whether or not unique, and closure steps with a stated matrix; I-3 places every member of a family in `Mat(ℛ)`. CC-4 gains DV-d (constant inside a closure step) and DV-e (family characterization). CC-0 rechecked under the new marking: `generated` (§4.4, last subsection) |
| B2: the Step-2 shortcut is contradicted by CC-0 | Shortcut restricted to rules whose clauses are I-f or G-n of admission form, adding no closure step; rules outside it are decided by exhibition or proof, with O-10 as one method |
| B3: row 2 overlaps the (I) remainder | Row 2 is `Ctrl ∧ T2 ∧ T3 ∧ T4 ∧ [(CT ∈ {installed, mixed}) ∨ (CT = generated ∧ two rules)]`, exactly the union of (C-inst) and (C-T1); `undetermined` and T1-undetermined cases fall to (I). Routing of refuted, vacuous and unestablished controls stated in §5 |
| B4: the object's clauses carry no type; A-3/A-4 conflict with §6 | §1.3 gains a kind column with reasons: A-3, A-4 I-f; A-1, A-5, A-6, A-7 G-n admission form; A-8 G-u shared; A-2 shared reference interface. §6 does not presuppose that A-3–A-5 are not interface clauses |
| N1: missing-rule form | §6 item 2 states the form CT entails and, separately, the narrower form from the owner's wording; §4.5 item 2 |
| N2: CC-2(b) can void a legitimate outcome; simpler O-6 route | CC-2(b) applies only when `K*` is available in both theories; O-6 carries the `ancBlock` pointer (reviewer reading) |
| N3: CC-3(b) cannot fail | Restated as a recorded definitional calibration: `drivePhase` passes the non-Clifford clause and is rejected by the monomial clause; the other two are also outside D3's carrier |
| N4: CC-1 rejection text | CC-1(a) not shown is vacuous, not a pass. It routes to (N) or (I), not to order 0, because vacuity coincides with ¬T2 and order 0 would pre-empt a legitimate (N); reason stated in §5 |
| N5: Q2's witness need not be `K*` | Step 2: a different operation derived by `d'` is the reported witness, with T3 and T4 checked for it |
| N6: scope of the Kraus and effect bullets | I-3 limited to channels, instruments and effects the clause itself states |
| N7: §6 consequence unconditional; reachability list | Restated as conditional on O-1 and O-2, with routing if either fails; reachable labels (C-inst) with `installed`, (N), (I); `mixed` and (C-T1) excluded, with reasons |
| N8: what CC-0 calibrates | §4.4 requires the clauses' classes beside the CT verdict; `generated` is stated not to mean "imports no quantum structure"; §4.5 item 3 |
| N9: depth form for `K*` | Added to O-3e |
| N10: Stage 1B gate checkpoint | Added to §10.2 |
| N11: shapes 1–2 in the (C) record | §6 item 3: named as possible sources, not scored against the operator-level form |
| N12: exactness notes | Added to O-3e (`hc² = 1/2`; the `(5/8 : ℂ)` cast) |
| N13: O-1 template | O-1 cites `conj_diag_entry` (DG:90) and `diagonalGlue_forces_monomial` (DG:101) |
| N14: the added (I) | §6 states that (I) is the remainder that makes the partition total, not a fourth result type |
| Review §D | §6 states that on this object MATH-CON-1 tests sufficiency for T2–T4 and identifies the missing rule, and cannot settle T5; §4.5 lists the three choices not ruled by the owner |
