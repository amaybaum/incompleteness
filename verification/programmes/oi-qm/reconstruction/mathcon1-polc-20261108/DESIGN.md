# MATH-CON-1: does one identification rule generate a coherent operation in the polarization closure, or install it?

**Standing.** Preregistration only, under #1169. Writer: Claude Code session, 2026-11-08. Status
of this file: `WIP / UNVERIFIED`, awaiting independent review.

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

Each assumption takes exactly one class. The criterion between [R] and [Q] is the inventory's: a
datum that is a matrix or a matrix family in the complex interface is [Q], and a choice that is
not a matrix is [R].

| # | Assumption | Class | Where it enters |
|---|---|---|---|
| A-1 | Finite reversible substratum; stated observer access, the scaled partial permutations `permClass` | [N] | `PolC.perm`; `permTheory` (SIA:606) is the stated-access theory |
| A-2 | Operational interface: complex matrix kinematics; `FiniteOperationalTheory`; the `InstAvail` rules; `readout` as local Lüders (`readout_is_localLuders`, OA:658); discard after uniform attach | [Q] | common to every theory compared here, including the baseline and the countercontrols. It is disclosed and is not the added rule |
| A-3 | (ℛ-R)(a): polarization, with the position half read | [R] | the added rule, non-matrix part |
| A-4 | (ℛ-R)(b): the observer's state space is the position amplitudes | [R] | the added rule, non-matrix part |
| A-5 | (ℛ-R)(c): the layers are available as their images under a representation | [R] | the added rule, non-matrix part |
| A-6 | (ℛ-Q), shear image: `siteShearImage n` | [Q] | the added rule, matrix part (generator `PolC.shear`) |
| A-7 | (ℛ-Q), swap image: `siteSwapImage n` | [Q] | the added rule, matrix part (generator `PolC.swap`) |
| A-8 | Relabelling closure (`PolC.relabel`), carrying implementation locality | [R] | shared architecture requirement. `polarizedTheoryC_derivedOI` takes `polC_labelInvariant` as an input (PCL:606–609). Implementation locality needs *some* context-stable, label-invariant generating class (IL:370), and `PolC` is the least label-invariant architecture containing `PolGen`. It is not counted as a second added rule unless countercontrol CC-2 shows that it carries the target (§5) |
| A-9 | B23 primitive memberships (`balancedCircuit`, `resetPerm j`, `correction j` ∈ `PolC`) | not assumed | new obligations O-3a–O-3c (§3). If proved, they follow from A-1, A-6 and A-7. If not proved, B23 does not apply to `PolC` and no assumption is added in their place |
| A-10 | Context stability and label invariance for spectators | not assumed | proved for `PolC`: `polC_contextStable` (PCL:584), `polC_labelInvariant` (PCL:172) |
| A-11 | Quarter phases at every level (`PhasesAvailable`) | not assumed | derived for `PolC` from A-6 (`polC_phaseGate`, PCL:443; `polarizedTheoryC_phasesAvailable`, PCL:448). Contrast A7–A9 of the inventory, where `PhasesAvailable` is stipulated |
| A-12 | The monomial baseline `substratumClass` (§4.1) | comparison set | not a premise of the object. It is the set the T2 criterion excludes, and the class of the baseline countercontrol |
| — | Independently motivated physical assumption | [P] | none. Physical selection of the map belongs to the other workstream (FHE-SEL-1) |

**[R] and [Q] split of the map.** The map's [R] part is A-3 to A-5. Its [Q] part is the two
images A-6 and A-7. The [Q] images are what place a non-monomial operator in the class:
`siteSwapImage_not_monomial` (C5D:203). The [R] part alone names no matrix.

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
| **O-1** | Baseline lemma: if an `InstAvail substratumClass` family has a branch equal to `p • conjChannel U`, with `p > 0` and `Uᴴ U = 1`, then `IsMonomial U`. Planned route: `classical_instAvail` (PII:168) gives preservation of the diagonal PSD cone. A conjugation `Ad U` that sends every diagonal rank-one state to a diagonal state has `U` monomial. Stated for the system carrier and for every level | this design | CC-3; Q2 in CT |
| **O-2** | Ablation inclusion: the least label-invariant architecture generated by `substratumClass` together with the monomial elements of a rule's matrix set is contained in `substratumClass` (from SC:231, SC:275). Also `PolC ⊆ 𝓕` and `PolGen ⊆ 𝓕`, where `𝓕` is the fiat class of CC-1. Transfer of availability by `genTheory_mono` (IL:919) | this design | CT Q2 and FC; CC-1 |
| **O-3a** | `PolC Work balancedCircuit`, through the matrix identity `balancedCircuit = (I⊗H⊗H)·Toff·(S⊗I⊗I)·Toff·(I⊗H⊗H)` (CH1:104–105) with the token as Toffoli's target. The factors: `S⊗I⊗I = siteShearImage 4` (`shear`); `H` on an ancilla bit as `relabel` of `siteSwapImage 4` along a self-bijection of `Work`, or as conjugation by a permutation matrix (`perm`, `mul`); Toffoli as `perm` | inventory reading; reviewer hand check of the identity | route (iii) |
| **O-3b** | `PolC Work (resetPerm j)` for every `j` (`perm`, `permClass_permMatrix`) | inventory reading | route (iii) |
| **O-3c** | `PolC Work (correction j)` for every `j`: the identity for `j = 0`, and `Z⊗I = (siteShearImage 4)²` (`mul`) otherwise | inventory reading; review G3 | route (iii) |
| **O-3d** | Apply `instAvail_attempt` and `balanced_finite_available` with `polC_arch`. This gives, in `polarizedTheoryC (Fin 2)`, the heralded branch `(5/8)·Ad(drivePhase)` and every stopped depth. No carrier transport is needed at system level, because `Token = Fin 2` and system availability is `InstAvail PolC (Fin 2)` (IL:852) | inventory reading, confirmed by review r2 §2 | T2 (monomial part only), T4 |
| **O-3e** | System-level `H`: `PolC (Fin 2) hadamard`, by `relabel` of `siteSwapImage 1` along `Fin 2 × Fin 1 ≃ Fin 2`. Then the coherent target `K*_iii`: the branch `(5/8)·Ad(H·drivePhase·H)` of the bind `op H`, then the attempt, then `op H`. Then the checks that `H·drivePhase·H` meets D2 and D3, by exact algebra in `ℚ(i)` | inventory reading; reviewer reading (the 3-4-5 rotation about `X`) | T2 |
| **O-4** | Route (ii), alternative: a heralding instrument whose branch is proportional to `Ad(levelThreeBlock)` on `Fin 2 × Fin 1`. It uses uniform attach of `Fin 3`, a reset to the input fiber `1` and a readout of fiber `0`, because `InstAvail` has no pure-ancilla preparation. The block's membership is already kernel (PCL:731). Then the transport to `Fin 2`, and the D2/D3 checks on the reflection `R` and on `R·Z` with `Z = S²` | inventory reading; reviewer readings F6, F7 | T2 (alternative) |
| **O-5** | Route (i), alternative: an exact characteristic polynomial of the level-three hexagon product of `relabel`ed swap images. D3 as frozen is defined on a qubit carrier (§4.3), so route (i) is scorable for T2 only after an amendment declares an encoding for `Fin 2 × Fin 3`. The numerical record of infinite order never counts | inventory reading; reviewer reading F6 | supplementary |
| **O-6** | CC-2 comparison: decide whether `K*` is available in `polarizedTheory (Fin 2)` (`PolGen`). Otherwise, show that every use of `relabel` in `K*`'s `PolC` derivation is either reproduced on the same carrier by conjugation with a `permClass` member, or is the carrier transport `Fin 2 × Fin 1 ≃ Fin 2` | this design | T1 |
| **O-7** | Carrier transport `Fin 2 ≃ Fin 2 × Fin 1`, needed only for level-indexed restatements (`availExt`) | inventory reading | T4 (level form) |
| **O-8** | The CT runs of §4.4 on the object and on CC-0, CC-1 and CC-4 | this design | T5; controls |
| **O-9** | Spectator form of `K*`, through `instAvail_spectator` with `polC_contextStable` and `polC_labelInvariant` | this design | T4 |

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

#### Inputs

| Input | Content |
|---|---|
| **I-1** Baseline | `𝓑 = substratumClass` (D1) |
| **I-2** Rule text `ℛ` | A finite list of clauses. Each is tagged with its class ([N]/[R]/[Q]/[P]) and its type, as one of two kinds below |
| **I-3** Matrix content `Mat(ℛ)` | Every operator-level matrix that `ℛ` supplies, however it is specified (below) |
| **I-4** Target `K*` | An operation meeting D2. For T5 to bear on T2, it also meets D3 |
| **I-5** Derivation `d*` | A finite derivation tree of `K*` in the rule's theory `𝔗_ℛ`. Its internal nodes are `InstAvail` rules and class-closure constructors; its leaves are class-generator applications and interface primitives, each carrying a concrete matrix |

The two clause types for I-2:
- A **generator clause** makes operators or channels admissible or available.
- An **interface clause** changes the carrier, the identification, the preparations, the readout,
  the discard or the composition rules.

The ways a matrix can be supplied, for I-3. Each of these places the matrix in `Mat(ℛ)`:
- written literally, or by a formula;
- as the image of a stated map at a stated input;
- as a relabelling, transport or nonzero scalar multiple of a supplied matrix;
- as the solution set of a stated condition, when that condition fixes the operator up to a scalar
  (a characterization counts as naming);
- as a Kraus operator of a channel that a clause makes available. A channel counts as monomial
  only if it has a Kraus representation by monomial matrices;
- as an effect, projector or prepared density matrix that an interface clause supplies.

Write `NM(ℛ) := {M ∈ Mat(ℛ) : ¬ IsMonomial M}`.

#### Procedure

- **Step 1 (Q1, the image question).** Mark every leaf of `d*` whose matrix is, up to
  relabelling and a nonzero scalar, an element of `NM(ℛ)`. Record the clause that supplies each
  marked leaf.
  - Q1 = yes iff at least one leaf is marked.
  - Q1 is decided by inspecting the finite tree `d*`.
- **Step 2 (Q2, derivation without naming).**
  - Q2 = yes iff a derivation `d'` of a D2 operation is exhibited in `𝔗_ℛ` such that `d'` has no
    marked leaf and uses at least one clause of `ℛ`. If T2 is being scored, the operation must
    also meet D3.
  - Q2 = no iff it is proved that every such derivation has a marked leaf.
  - Otherwise Q2 = undetermined.
  - For a rule all of whose clauses are generator clauses on the unchanged interface A-2, Q2 = no
    follows from O-2 and O-1. With every non-monomial leaf removed, the class lies inside
    `substratumClass`, and its instruments have no coherent non-monomial branch.
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
| Q2 = no, Q1 = yes, FC = no | `mixed`: non-monomial matrices are named, and they do not suffice without the rule's interface clauses. The record states which part each contributes |
| Q2 = no, Q1 = no | inconsistent: `d*` would be a derivation without a marked leaf. CT is void |
| any other combination | `undetermined` |

T5 holds iff the verdict is `generated`.

**Scope of CT.** CT as frozen applies to rules on the operator-level interface A-2. There,
identifications are carrier relabellings, and "monomial" is the operative test. Shapes 1 and 2
(§7) identify configuration laws through frames. For them "monomial" is not the relevant
criterion, so the same two questions need a frame-level CT variant. That variant is frozen in the
amendment or preregistration that takes the shape up, before any result for that shape.

***

## 5. Countercontrols and controls, with decidable rejection rules

A control that fails, or is vacuous, voids every CT verdict and every T2 score that depends on it.
The outcome is then (I), with the failed control named. Controls are reported before any verdict
in the Stage 1B result record.

| ID | Control | Construction | Pass condition (decidable) | Rejection rule |
|---|---|---|---|---|
| **CC-0** | Calibration for `generated`. A fixture, not a candidate; [Q], superposition closure; excluded from every outcome | `ℛ_0`: a closure clause. If `K, L ∈ 𝓘` on one carrier and `aK + bL` is unitary for some `a, b ∈ ℂ`, then `aK + bL ∈ 𝓘`. Otherwise `𝓑` with the architecture and relabelling. `Mat(ℛ_0) = ∅`. Target `H = (X + Z)/√2` on `Fin 2`, where `X` is `permMatrix (swap 0 1) ∈ permClass` and `Z = diag(1, −1) ∈ 𝓑` | CT returns `generated` (exhibited `d'` with leaves `X` and `Z`) | Any other verdict means CT cannot return `generated` for a rule that names no matrix. CT is then defective and void |
| **CC-1** | Coherent Clifford by fiat | `ℛ_1`: one generator clause, `siteSwapImage n` admissible for every `n`, with no polarization map. Class `𝓕` = the least label-invariant architecture containing `𝓑 ∪ {siteSwapImage n}`. Theory `𝔉 := genTheory 𝓕 (Fin 2)`. By O-2, `PolC ⊆ 𝓕` | (a) Nonvacuity: the object's target `K*` is shown available in `𝔉`. This follows by O-2 and `genTheory_mono` once it is shown in `polarizedTheoryC`. (b) CT returns `installed` for `ℛ_1` | (b) fails: CT is void. (a) fails while `K*` is shown in `polarizedTheoryC`: the inclusion O-2 is false, and the error is recorded. (a) not shown: CC-1 is vacuous, and T2 is unmet in any case |
| **CC-2** | `PolGen` versus `PolC` | `polarizedTheory (Fin 2)` (C5D:247), without `relabel`, against `polarizedTheoryC (Fin 2)` | (a) T1 accounting: `K*` is available in `polarizedTheory (Fin 2)`, or O-6's alternative holds. Either way, the relabelling closure is not a second rule. (b) CT returns the same verdict for `PolGen` and for `PolC` | (a) refuted, meaning `K*` is proved unavailable in `polarizedTheory (Fin 2)` beyond the named transport: T1 is recorded as two rules (map and relabelling closure). (a) undetermined: T1 is undetermined. (b) fails: CT is void |
| **CC-3** | Monomial-only baseline, kill battery, with the `substratumClass` hazard | `𝔅 = substratumTheory (Fin 2)`, with no rule | (a) No D2 operation in `𝔅` at any level (O-1). (b) Hazard nonvacuity: `drivePhase`, the controlled quarter phase on `Fin 2 × Fin 2` and Toffoli on `Work` are each `IsMonomial`, so they are in `𝓑`, and D3 rejects each | (a) refuted: D2 is defective (it admits a monomial-class operation) and void. (b) fails: D3 is defective and void. (a) not established: Q2 = no is not available for any generator-clause rule, CT returns `undetermined` there, and (P) and (C) are both blocked |
| **CC-4** | Disguised variants | DV-a: the swap image stated as "the normalized finite Fourier transform on the position alphabet", `(a, b) ↦ (−1)^{ab}/√2`. DV-b: by characterization, "the unitary, unique up to scalar, with `W X Wᴴ = Z` and `W Z Wᴴ = X`", where `X` and `Z` are monomial. DV-c: the swap image placed only as `reindex e e (siteSwapImage n)` for a fixed nontrivial carrier bijection `e`, for instance on an ancilla bit | CT returns `installed` for each of DV-a, DV-b and DV-c, with target `K*` | Any variant classed otherwise: CT is void |

CC-1 and CC-4 must return `installed`, and CC-0 must return `generated`. These are requirements
on the test, preregistered as rules. They are not predictions of the object's result.

***

## 6. Outcomes: a total, ordered partition

The outcome is evaluated after every control. The first matching row wins.

| Order | Outcome | Condition |
|---|---|---|
| 0 | → (I), void | Any control of §5 fails or is vacuous. Or CT is void. Or both T2 and ¬T2 are proved. The record names the failure |
| 1 | **(P)** positive and noncircular | T1 met (CC-2 passed) ∧ T2 met (D3, at the support standard below) ∧ T3 met (imported, disclosed) ∧ T4 met ∧ CT = `generated` |
| 2 | **(C)** conditional and partial | T2, T3 and T4 met, but (P) not reached. It has two sub-labels: (C-inst), when CT = `installed` or `mixed`; and (C-T1), when CT = `generated` but CC-2 records two rules. Required content of the record: the existing mathematics is stated as valid, with its conditions; the milestone is stated as not reached; the missing rule is identified by the procedure below |
| 3 | **(N)** negative or obstruction | ¬T2 proved for the object: no available family of `polarizedTheoryC (Fin 2)` has a branch meeting D3. Or ¬T3 or ¬T4 proved for every T2 witness. A failed route alone is not (N) |
| 4 | **(I)** inconclusive | Everything else. Examples: T2 neither established nor refuted; CT `undetermined` while T2 holds; Stage 1B not authorized or not completed |

The partition is total, because (I) is the remainder. It is disjoint: (P) and (C) require T2, (N)
requires ¬T2, and a proof of both is void at order 0.

**Support standard for T2.** An established T2 needs either a kernel theorem, or an exact written
derivation with a recorded independent review. Numerical evidence never counts. The outcome
record names the weakest support layer among its links.

**Identifying the missing rule in (C).** The record states these items:
1. Each marked leaf of `d*` and the clause that supplies it. For the object, these are expected
   to be leaves `siteSwapImage n` from A-7.
2. The required form of the missing rule. It is a clause that is not a generator clause. Applied
   with native or monomial data, and with no non-monomial supplied matrix, it yields the marked
   leaves or a D2 operation directly. That is, it is a rule for which CT would return `generated`.
3. Which of the preserved routes and shapes (§7) could supply a rule of that form. No route or
   shape is chosen.

Per the owner's ruling, (C) is not recorded as failure of the construction.

**Mapping onto the target clauses.**

| Outcome | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| (P) | ✓ | ✓ | ✓ (imported A-2) | ✓ | ✓ (`generated`) |
| (C-inst) | ✓, or as CC-2 records | ✓ | ✓ (imported A-2) | ✓ | ✗ (`installed` or `mixed`) |
| (C-T1) | ✗ (two rules) | ✓ | ✓ (imported A-2) | ✓ | ✓ |
| (N) | as recorded | ✗ (proved) | — | — | — |
| (I) | any | unresolved, or void | any | any | unresolved, or void |

**A consequence of the frozen definitions, stated before any result.** The object's rule places
`siteSwapImage n` by the generator `PolC.swap`, and that matrix is non-monomial (C5D:203). Every
derivation in `PolC` of a D2 operation therefore has a `swap` leaf: with `swap` removed, O-1 and
O-2 leave only monomial branches.
- Unless the [R] part A-3 to A-5 is restated as an interface clause that supplies no non-monomial
  matrix, CT on the object can return only `installed`, `mixed` or `undetermined`.
- Such a restatement would be a new premise. It is outside this preregistration and would need an
  amendment and owner authorization.
- On the frozen object, the reachable outcomes are therefore (C), (N) and (I). This follows from
  the owner-ruled object and the frozen test, not from any measurement.
- CC-0 is there to show that the test itself can return `generated`.

***

## 7. Alternative routes and shapes, preserved

No route or shape is chosen beyond the owner's ruling: A10/`PolC` with B23 first.

| Route or shape | What it is | Condition for taking it up |
|---|---|---|
| **Route (iii)**, B23 transfer | O-3a–O-3e, O-9 | Primary, by owner ruling 1 |
| **Route (ii)**, level-three fiber block | O-4. Membership is already kernel (PCL:731). It needs a heralding instrument (reset and readout) and the transport | Taken up if an obligation of route (iii) is refuted, or blocked at a recorded wall, or if the owner authorizes it as an independent second witness for T2. CT's verdict does not depend on the route, because every route uses `swap` leaves |
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

### 10.3 Hazards with cheap mitigations, carried as checkpoints

- **H-1.** A route's T2 witness could be monomial and be scored by mistake. Mitigation: the D3
  check rejects monomials, and it is calibrated on the hazard operations by CC-3(b).
- **H-2.** CT could be unable to return `generated`. Mitigation: CC-0.
- **H-3.** CT could misclass a renamed or characterized `H`. Mitigation: CC-4.
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
- The "consequence of the frozen definitions" paragraph in §6 says what CT can return on the
  object as recorded. It is not an outcome.
- The CC-0 fixture is a calibration of the test. It is not a candidate rule, it is not adopted,
  and it enters no outcome.
- Nothing here bears on a manuscript.
