# Thread O: where the drive comes from (DRIVE). Result

Read-only research against certified main L = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`. Nothing here is
governed or landed.

Conventions:
- Paths are under `verification/lean-mathlib/OIBridge/`.
- Abbreviations: KF KInfFoundations, OG OrbitGeneration, ON OrbitNormalization, LA LiftAudit, SS SubstratumSource,
  SC StructuralClosure, DC DiscreteCompletion, SMC StateMixingCoupling, RPF RealPairFlow, PFE PairFlowEquivalence,
  OA OperationalAssembly, SIA SubstratumInterfaceAudit.

Evidence levels:
- **kernel**: a landed identifier, checked at L with file:line.
- **exact**: `o_drive.py` in this directory, `OK -- 52 checks, 0 failed`. It uses sympy exact arithmetic and
  replays byte-identically. sha256 of the script `61e5f4f2…cd148`, of the output `8f5d6281…3406a`.
- **written**: an argument given here.
- **citation**: literature.

Nothing here is called proved unless it names a landed identifier.

***

## 0. Verdict

1. **No honest, non-circular, field-neutral drive-source theorem is available at L.**
   - The missing ingredient is **OPACT**: an action of the extended theory's reversible operations on the
     completion body Ω∞ by affine automorphisms.
   - KInfFoundations has no operations at all.
   - OPACT cannot be built one finite stage at a time. A continuous flow preserves no polytope
     (`isEmpty_drivability_of_finite_orbits` ON:124, plus the finite automorphism group of a polytope, written).
   - So OPACT has to be built on the completion, by transporting effects. That needs SC∞ and the P2 effect family,
     and neither is landed.
   - Without OPACT, any resource stated on Ω∞ is the set of fields D1–D9 of `ElementaryDrivability` restated, i.e.
     the conclusion in disguise.

2. **Every landed route that does supply a drive fixes the body as the Bloch ball.**
   - Those routes are `LayerFlowExecutable`, `PairFlowSourced`, `DrivesElementary`, the classes MixC and FlowR, and
     the fixed gate together with D3.
   - On that body the drive is free in the kernel: `ball3_drivable` KF:490 and `boundaryTransitive_ball3Drive`
     ON:667.
   - So these routes source only the drive's *availability*, never its existence on a body that is not yet known.
   - Fed into OG-1 they make DIM3 and the ellipsoid trivial. Read that way they are circular. They are legitimate
     only as the reverse instance: QM satisfies the premises.

3. **NEW (F1, exact + kernel ingredients): in the matrix regime, the continuum of the drive need not lie in the
   gate flow.**
   - Under `SubstratumAvail` (LA:745), the round-62 interface's continuum of diagonal phases, **one fixed Clifford
     gate** gives the whole non-integer gate flow at every level.
   - The identity (exact I0, I1, I2, symbolic t, levels n = 1, 2, 3) is
     `gateFlow (levelPerm (swap 0 1) n) t = M_n · (diag(1, e^{iπt}) ⊗ 1_n) · M_n⁷`,
     with `M_n = mixImage n (π/4)`, and equally with `M_n = siteSwapImage n`, the Hadamard image.
   - So the owner's "extension containing the non-integer gate flow" can be cut down to a single non-monomial
     operator plus a **physical** phase continuum.
   - Either a continuum of gate times or a continuum of phases must be physical. OI sources neither: the
     observer-sourced theory fails `SubstratumAvail` (SIA:695), and the manuscripts call diagonal-unitary
     conjugation gauge.

4. **NEW (F2): `ElementaryDrivability` is mis-typed as the target.**
   - It is a property of the body alone, with no availability content.
   - OG-1 needs the drive operationally, and only through V4′.
   - The correct target is an *operational* drive, one whose flow members and J are available operations. Together
     with closure of the effect family under those operations, it discharges V4′ (§2, D-1).

5. **Recommendation.**
   - A preregistered round is possible **now** for the matrix-regime statement (§2, D-3) together with the
     field-neutral vocabulary and controls (§2, D-1). No premise is adopted in it.
   - **No round** for a field-neutral drive *source* until OPACT exists, which is M's R2 completion definitions,
     and until the owner chooses which continuum is physical (§5).

***

## 1. Inventory: every landed object with a continuous one-parameter flow (question 1)

Classes used in the table:
- **FN-def**: field-neutral, a definition or a control.
- **ℂ-math**: a mathematical object in a complex algebra, not an operation of any theory.
- **ext**: a predicate or class that postulates a control extension (ℂ).
- **sub**: supplied by a substratum class.

"Presupposes the body" means its two-level state space is the ℂ² density-matrix body, i.e. the Bloch ball.

| object | file:line | kind | flow? | presupposes the quantum body? |
|---|---|---|---|---|
| `ElementaryDrivability` | KF:264 | FN-def | the fields D1–D9, no availability | no; any Ω |
| `rot3`, `ball3Drive`, `ball3_drivable` | KF:411, :449, :490 | FN-def, control | Rz flow on the stipulated `ball3` | the body is stipulated; the module "sources nothing" (KF header) |
| `driveWords3`, `rotX`, `boundaryTransitive_ball3Drive` | ON:571, :581, :667 | FN-def, control | the words of `ball3Drive` | stipulated `ball3` |
| `SecondOrderCircuit.unit` / `flow` | :356 / :432 | ℂ-math | a group in t (`unit_mul_unit`); `unit g 1 = g` | ℂ algebra. The interpolation is not unique: odd branches (exact A7) |
| `SecondOrderCircuit.drive` | :635 | ℂ-math | a two-piece **path**, not a group | ℂ |
| `swapU`, `swapQ` | SwapLayer:95, :372 (group law :494, continuity :446) | ℂ-math | a strongly continuous group of *-automorphisms of the quasilocal algebra | ℂ quasilocal algebra |
| `layerQ` | SecondOrderLayer:675 (group law :966) | ℂ-math | the same | ℂ |
| `driveQ` | SecondOrderDrive:135 (path :225, endpoint :829) | ℂ-math | the update's **path**; no group law (header; toy, exact H1) | ℂ |
| `gateFlow` | LA:47 | ℂ-math | a group; `gateFlow_one`; Bloch image Rx(πt) (exact A5) | ℂ² |
| `LayerFlowExecutable` | LA:112 | ext predicate | availability of `gateFlow` at every time | ℂ. Refuted for `substratumTheory` (LA:200); holds under composite control (LA:117) |
| `ReachabilitySeam.flow` | RS:95 | ℂ-math | e^{−itH} | ℂ |
| `DrivesElementary`, `QuantumArchitecture` | SS:77, :86 | ext class predicate | transition flows at every carrier | ℂ. Witnessed only by `fullClass` (SS:147), which is QM by definition |
| `rot`, `mixImage`, `MixC` | SMC:45, :50, :72 | ext ("the datum … a postulate") | a real mixing angle at every θ | ℂ theory. `mixTheory_qm` SMC:511 |
| `PairFlow`, `PairFlowSourced` | RPF:41, PFE:48 | ext | a real orthogonal 2×2 group | the matrix is real, the theory is ℂ. `qm_iff_derivedOI_pairFlowSourced` PFE:199 |
| `FixedGateSourced`, `fixedGateTheory` | DC:34, :1926 | ext, one angle | **no flow**: countable up to scalar (SMC:662), dense (DC:1942), not QM (DC:1948) | ℂ |
| `ClosureAvail` (D3) | DC:63 | definition, not adopted | supplies flows only in the closure | ℂ |
| diagonal phases in `substratumClass` | SC:180, :333; `SubstratumAvail` LA:745; `diagonal_avail` LA:754 | **sub** (round-62 interface reading) | t ↦ diag(1, e^{it}) is **available** in `substratumTheory`. It acts as Rz(t), with N = Z; D1–D8 hold and D9 fails within substratum operations (exact B1, B5) | ℂ². Absent from the observer-sourced theory (SIA:695); "gauge" in the manuscripts |
| `ReadWriteFamily.couple` | ReadWriteControl:86–87 | sub | permutation-valued, so no flow (constant if continuous) | n/a |
| `HasCompositeUnitaryControl` | OA:665 | ext | contains every flow | ℂ |

**Field-neutral:** only the KF and ON rows, and those are definitions or controls on a stipulated body.
**The only substratum-supplied continuous flow** is the interface's phase circle. It is ℂ-typed and fails the
off-axis clause.

***

## 2. Candidate statements (question 2; deliverable (a))

### D-1. Vocabulary and the V4′ discharge (field-neutral; kernel-cheap; no premise adopted)

```lean
namespace DriveSource
open KInfFoundations OrbitGeneration OrbitNormalization
variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- An elementary drive implemented by the available reversible operations `Gav`. -/
structure OperationalDrive (Ω : Set V) (Gav : Subgroup (V ≃ᵃ[ℝ] V))
    extends ElementaryDrivability Ω where
  flow_mem : ∀ t, flow t ∈ Gav
  J_mem    : J ∈ Gav

/-- EFFCLOSE: available effects are closed under transport by available operations
    (sequential composition read on effects). -/
def EffClose (Gav : Subgroup (V ≃ᵃ[ℝ] V)) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ g ∈ Gav, ∀ e ∈ avail, seedTransport e g ∈ avail

theorem seedOrbitAvailable_of_operationalDrive {Ω} {Gav} (D : OperationalDrive Ω Gav)
    {r avail} (hr : r ∈ avail) (hE : EffClose Gav avail) :
    SeedOrbitAvailable (words (Set.range D.flow ∪ {D.J})) r avail
```

Proof (written):
- `words S ⊆ Gav` by `Subgroup.closure_le`, since S ⊆ Gav.
- Then EFFCLOSE applies to r.

What D-1 does:
- It moves V4′ onto two premises: the drive is operational, and EFFCLOSE holds.
- `PreservesBody` follows from the drive via `preservesBody_driveWords` (ON:107).

Controls, cheap and in KF vocabulary:
- If Gav is commutative, no `OperationalDrive` exists in it: J commutes with the flow, so D9 fails.
- If Gav is countable, none exists either: t ↦ flow t x is continuous with countable range, hence constant, which
  contradicts N_moves.

### D-2. The drive-source schema (field-neutral; written; *conditional on OPACT*, entered here as the datum Gav)

Hypotheses. Ω is compact and convex, `[FiniteDimensional ℝ V]`, `affineSpan ℝ Ω = ⊤` (the chart, after
`hypotheses_restrict` ON:529), and `PreservesBody Ω Gav`.

Conclusion. `Nonempty (OperationalDrive Ω Gav)` from **one continuum package**, plus **OFF**, plus **VIS**.

OFF and VIS:
- **OFF(j, φ)**: some j ∈ Gav does not normalize the circle φ(ℝ) on Ω. This is D9 with J := j.
- **VIS(φ)**: the circle acts nontrivially on Ω. This is D6.

The three continuum packages:
- **(R1) GATEFLOW**: an additive, jointly continuous φ : ℝ → Gav with φ(1) equal to the substratum's visible
  exchange. This is the field-neutral `LayerFlowExecutable`; it gives N = exchange (NAL).
- **(R2) PHASEFLOW**: φ is a one-parameter group of substratum phase operations (the interface reading). Then N is
  the phase flip, OFF needs **one** fixed extension operation j, and NAL fails.
- **(R3) FIXGATE + LIMCLOSE**: some g ∈ Gav has infinite order on Ω, and Gav is closed. LIMCLOSE is the
  field-neutral D3.
  - Theorem (written; citation for Cartan's closed-subgroup theorem and for compact abelian Lie groups):
    cl⟨g⟩ is compact abelian and infinite, so its identity component is a torus Tᵏ with k ≥ 1.
  - A primitive circle in that torus gives φ with φ(1/2) involutive.
  - φ(1/2) moves a state, because an affine map that fixes Ω fixes `affineSpan Ω = V`.
  - So D1–D8 hold in Gav.
  - **Without LIMCLOSE this fails.** ⟨g, finitely many others⟩ is a finitely generated linear group. It is
    residually finite (Malcev), so it has no nontrivial divisible subgroup and admits **no** additive
    ℝ → Gav at all.

Proof once a package is given: field by field (written). The schema's honest content is *which* package is used.
On Ω itself, R1 + OFF + VIS restate D1–D9, so D-2 is a typed interface and not a source until Gav is constructed
from OI (OPACT).

### D-3. The matrix regime: the extension's minimal resource (imported ℂ; kernel-cheap; preregistrable)

```lean
theorem layerFlowExecutable_of_substratumAvail_fixedGate (T : FiniteOperationalTheory (Fin 2))
    (hsub : LiftAudit.SubstratumAvail T)
    (hg : DiscreteCompletion.FixedGateSourced (Real.pi / 4) T) :
    LiftAudit.LayerFlowExecutable T (Equiv.swap 0 1)

theorem qm_iff_fixedGate_of_substratumAvail (T : FiniteOperationalTheory (Fin 2))
    (hd : RouteB.DerivedOI T) (hsub : LiftAudit.SubstratumAvail T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ DiscreteCompletion.FixedGateSourced (Real.pi / 4) T

-- controls (kernel corollaries)
theorem fixedGateTheory_quarter_not_substratumAvail :
    ¬ LiftAudit.SubstratumAvail (DiscreteCompletion.fixedGateTheory (Real.pi / 4))
theorem substratumTheory_not_fixedGateSourced_quarter :
    ¬ DiscreteCompletion.FixedGateSourced (Real.pi / 4) (RouteB.substratumTheory (Fin 2))
```

Proof of the first theorem:
- Write the gate flow by the identity in §0.3.
- `M_n` is available by `hg n`.
- `M_n⁷ = M_nᴴ` (exact I0) is available by repeated `avail_conj_mul` (LA:770).
- The diagonal factor is available by `diagonal_avail` (LA:754).
- The product is available by `avail_conj_mul`.

The iff:
- Forward: through `derivedOI_qm_iff_layerFlowExecutable` (LA:812), with x = 0.
- Reverse: QM gives composite control (`physical_of_exactAll`), and `mixImage_unitary` (SMC:152) does the rest.

The controls:
- First: from `fixedGateTheory_derivedOI` DC:1929, `_fixedGateSourced` DC:1933 and `_not_qm` DC:1948.
- Second: from LA:200, `substratumTheory_derivedOI` RouteB:290 and `substratumTheory_substratumAvail` LA:750.
- Together they show that **each of the two premises is necessary relative to the other**, both witnessed in the
  kernel.
- The Hadamard variant (`siteSwapImage`, exact I2) has a third control, `polarizedTheoryC` (PolarizationClosure:606,
  :620).

A moderate-cost generalization:
- Any fixed non-monomial pair gate can replace the angle π/4. The phase generator and Ad(J) of it span su(2) (exact
  I4, I5; monomial controls I6), and the conclusion goes through `exactReachability_of_hcontrol` OR:625.
- No irrationality is needed. The irrational angle of DC was needed only because the phase continuum was absent.

Scope: D-3 is about ℂ theories, whose body is the Bloch ball. It identifies the smallest extension of the
substratum that contains the non-integer gate flow. It does **not** source the field-neutral drive.

***

## 3. Dependency chain (deliverable (b))

```
[OPACT: Gav on Ω∞ by effect transport]  ← needs SC∞ + P2 effect family     MISSING (not landed)
  ├─ R1 GATEFLOW | R2 PHASEFLOW (interface phases) | R3 FIXGATE + LIMCLOSE(D3)   named premises (§5)
  ├─ OFF (one non-normalizing operation)                                       named premise
  └─ VIS (the circle acts nontrivially on Ω∞)                                  named premise (body-level)
        ⇒ OperationalDrive Ω∞ Gav                                              D-2 (written)
        ⇒ PreservesBody (words …)                     preservesBody_driveWords ON:107 (kernel)
        + DIM3 (OPEN) ⇒ ellipsoid + transitivity      K-T4 (written, unlanded)
        + NORM                                        seedOrbit_eq_of_normalization ON:307 (kernel)
        + EFFCLOSE + r ∈ avail ⇒ V4′                  D-1 (written; kernel-cheap)
        + P1 SharpSeed (OPEN, SC∞)
        ⇒ seedOrbit_ball3_eq OG:348 → ballEffect_mem_avail OG:369 → lorentz_of_available OG:422 (kernel)

Matrix regime (reverse instance only):
  SubstratumAvail LA:745 (interface stipulation) + FixedGateSourced (π/4) DC:34 (extension datum)
    ⇒ LayerFlowExecutable LA:112                    D-3 (exact identity I1; kernel-cheap)
    + DerivedOI RouteB:141 ⇒ QM                     derivedOI_qm_iff_layerFlowExecutable LA:812 (kernel)
    ⇒ [Bloch map, unlanded B12] OperationalDrive on ball3   (body fixed by type)
```

***

## 4. Countermodel and circularity audit (deliverable (c), question 3)

| hypothesis | model where it fails, or where the rest holds without it | what breaks | evidence |
|---|---|---|---|
| OPACT | KF vocabulary: no operations exist | nothing can be stated off the body; D-2 collapses to D1–D9 | kernel (KF header lines 6–9) |
| OPACT, stage-wise | any finite stage (polytope body) | a continuous flow cannot preserve the stage | ON:124 (kernel) + written |
| continuum: R1 | `substratumTheory`: monomials only | no gate flow at t = 1/2 | LA:200, SC:383 (kernel) |
| continuum: R1/R3, dense | `fixedGateTheory α`: countable up to scalar, dense | no layer flow and not QM | SMC:673, DC:1948, PFE:218 (kernel) |
| continuum: R3 without LIMCLOSE | ⟨g⟩ ≅ ℤ, or any finitely generated linear group | no additive ℝ → Gav at all | written + citation (Malcev) |
| continuity field D3 | Hamel flow t ↦ Rz(π φ(t)), φ : ℝ → ℚ additive, J = cyc3 on `ball3` | all fields hold except continuity; the group is countable and not transitive | written (choice); K 2.N3 |
| continuum on a classical body | [−1, 1], polytopes | no drive exists | `not_drivable_Icc` KF:529, ON:124 (kernel) |
| group law | `driveQ`, the update path | a path, not a group | SecondOrderDrive:225 (kernel, path only); toy, exact H1 |
| OFF | ones-fixing theory: the whole gate flow (FlowEndpoint:87), no off-axis element | every ones-fixing unitary acts as an Rx rotation and commutes with the flow, so D9 fails | kernel FlowEndpoint:87, :177; exact D1–D3 |
| OFF | rebit: the real pair flow, real monomials, disk body | J R J⁻¹ = R(±) for every J ∈ O(2), so D9 fails | exact C5–C7; F B6 (written) |
| OFF | real monomial J (signs, X) | the flow is normalized | exact B5; `obligations_independent` C5Discovery:59 (kernel) |
| OFF ⟺ ℂ phase | monomial J = diag(1, e^{iφ}) or X·diag(1, e^{iφ}) against the gate flow | D9 holds iff sin φ ≠ 0 | exact B3, B4 |
| VIS / N_moves | `substratumTheory` with substratum effects: operational body is a segment, phases act trivially; identity involution | D6 fails | G (written); DerivedQ3:294 (kernel) |
| EXCH alignment (NAL) | pair-flow NOT: Bloch diag(−1, 1, −1) ≠ X's diag(1, −1, −1); R2's NOT is the phase flip | OG-1 is unaffected; NB-1's N-ALIGN fails | exact C3, C4 |
| EFFCLOSE | avail₀ = {r} (Thread I) | V4′ fails while the drive holds | written (I) |
| ℓ^∞ typing | induced action on ℓ^∞(E∞) | the indicator of one effect is displaced by 1 under R_n → id, so `flow_continuous` fails | exact E1, E2 |
| D-3: SubstratumAvail | `fixedGateTheory (π/4)`; `polarizedTheoryC` | not QM | kernel DC:1948, PolarizationClosure:620 |
| D-3: fixed gate | `substratumTheory` | no layer flow | kernel LA:200 |

**Circularity checks.**

1. **No dimension 3 from NB-1.** No premise of D-1, D-2 or D-3 mentions dimension.
   - The B⁴ drive Rz⊕1, cyc3⊕1 satisfies every drive field and is not boundary-transitive (exact F1–F3; K 3.11).
   - `boundaryTransitive_ball4` (ON:735) shows that even transitivity does not fix d.
   - DIM3 stays a separate open premise.
2. **No substratum-only drive.**
   - Every continuum package is an extension (R1, R3) or the interface phase stipulation (R2), which the
     observer-sourced theory lacks (SIA:695).
   - OFF is a non-monomial operation or a non-real phase.
   - The refuted route `elementaryDrivability_of_substratum` is not used. Its group-level form is re-checked (B5).
3. **The conclusion in disguise.**
   - D-2 on Ω is definitional (§2), and it is labelled that way.
   - D-3's resources are a single fixed gate and monomial phases. Neither alone gives the conclusion; the kernel
     witnesses each failure (row D-3).
   - "A continuous family of gates acting as Bloch rotations" is never a premise.
4. **The body is not fixed as the Bloch ball** in D-1 or D-2. D-3 fixes it by type and is scoped as the reverse
   instance.

***

## 5. Question 4: is there a route that does not fix the body as the Bloch ball?

**No landed route does.** Every landed operational flow is typed over ℂ (§1). The only body-agnostic objects are
the KF definitions.

A non-circular route exists **in schema form** (D-2). It is conditional on OPACT, and it needs the owner to choose
which continuum is physical. That choice is the real content of DRIVE:

| package | continuum carried by | adoption cost | NOT = visible exchange? |
|---|---|---|---|
| R1 GATEFLOW | non-integer times of the exchange (the CT2 interpolation, branch-dependent, exact A7) | a new continuous control | yes |
| R2 PHASEFLOW | the substratum's phase circle, plus **one** fixed gate | phases must be physical operations, against the manuscripts' "gauge" reading (interface-audit.md:66–72) | no (phase flip) |
| R3 FIXGATE + LIMCLOSE | one infinite-order gate, with limits adopted | adopting D3, "deliberately not adopted" (DC header) | no (half-turn of the closure circle) |

Each package also needs OFF and VIS.
- In the matrix regime, OFF is exactly a non-real relative phase or a non-monomial gate (B3, B4, I4–I6).
- VIS is exactly the visibility of coherences to the effect family. That couples DRIVE to P2 and EFFCLOSE.

***

## 6. Classification of findings (§A.31)

- **F1, NEW.** Relocating the continuum: `SubstratumAvail` + `FixedGateSourced (π/4)` ⇒ `LayerFlowExecutable`.
  - Exact at every level checked (I0–I2); kernel-cheap.
  - Hidden assumption exposed: "the extension must contain the non-integer gate flow" holds only when the phase
    continuum is unphysical (the stated-access reading).
  - Cross-propagates to DiscreteCompletion: irrationality is needed only without phases.
  - Cross-propagates to K §3: "the one unsourced ingredient" is reading-dependent.
- **F2, NEW.** `ElementaryDrivability` has no availability content.
  - The operational drive together with EFFCLOSE discharges V4′.
  - Assumption-watch marker for the V4′ and P2 threads: DRIVE must be typed as `OperationalDrive`.
- **F3, ELABORATING.** OFF is independent of the flow. For monomial J it is equivalent to a non-real phase. The
  ones-fixing theory and the rebit are the countermodels.
- **F4, ELABORATING.** Dense versus exact, field-neutrally.
  - A finitely generated group admits no additive flow; a countable set admits no continuous one.
  - LIMCLOSE plus one infinite-order gate gives a continuous flow (Cartan).
- **F5, ELABORATING.** The ℓ^∞ typing hazard: the drive must be stated on the chart.
- **F6, CONFIRMING.** OPACT must live at the completion level (ON:124).
- **F7, CONFIRMING.** The drive does not fix dimension.
- **F8, BORDERLINE.** The update path is not a group (toy).

***

## 7. Recommendation

1. **Preregisterable now: round DRIVE-1** (no premise adopted, cheap).
   - Statement: D-3, i.e. `layerFlowExecutable_of_substratumAvail_fixedGate` and
     `qm_iff_fixedGate_of_substratumAvail`, with the two corollary controls and the Hadamard variant.
   - D-1 (`OperationalDrive`, `EffClose`, `seedOrbitAvailable_of_operationalDrive`) and its two KF countercontrols:
     a commutative Gav, and a countable Gav.
   - Scope sentence: *the matrix-regime statements import ℂ and fix the body by type. They identify the smallest
     extension containing the non-integer gate flow relative to the interface's phase continuum. They do not
     source field-neutral drivability.*
   - Exact probe for the preregistration: `o_drive.py` §I.
2. **Later, moderate.**
   - The general fixed non-monomial gate, through OR:625.
   - R3 as a theorem (Cartan is not in Mathlib; a single-frequency variant through `dense_angles` DC:518 is cheaper).
3. **Not preregisterable yet: a field-neutral drive source.**
   - It is blocked on OPACT, which needs M's R2: `DirectedStages` with SC∞, `completionBody`, and an effect-transport
     action.
   - It is also blocked on the owner's choice of package (§5).
   - Until both exist, DRIVE stays a named open premise, best typed as `OperationalDrive Ω∞ Gav` together with
     EFFCLOSE.

## Scope and limits

- Kernel claims are the identifiers cited, checked at L.
- D-1, D-2 and D-3 are candidates and are unlanded.
- R3 rests on citations: Cartan's closed-subgroup theorem, the torus structure of compact abelian Lie groups, and
  Malcev's residual finiteness.
- The Hamel countermodel uses choice and is written.
- No Lean was run. No repository, ROADMAP or manuscript edit was made. The worktree is untouched and in place.
