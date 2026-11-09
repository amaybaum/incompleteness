# Notes for r4: "three gaps in parallel" (owner, chat, 2026-11-09, relayed)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Not applied. r3
(`BRIDGE-UNIT1.md`, sha256 `ee1c83c0…8219`) is under review and was not modified. Line numbers
are r3 lines. Sources were read at `fd539e15`.

## Does r3 meet the instruction?

In part.
- **Met.** The three gaps (phase, FI-1, H-Bell) are named as independent, not as a sequence, in:
  - §0 item 8 (l.120–146);
  - §5.1 *Position* (b)–(c) (l.479–506);
  - §5.2 "earliest missing mechanism" (l.533–540).

  FI-1's carrier and scope are stated exactly: configuration carrier, level one; exact finite
  endomorphic operational QM within the structural architecture (§5.1 l.378–425).
- **Missing.**
  1. No single place gives all three gaps side by side, each with its carrier, scope, what is
     proved toward it and what is open. The phase's carrier and scope appear only in §6's
     "Complex phases" row and in §5.1(b). H-Bell's carrier and scope are not stated anywhere.
  2. The three pairs the owner asked to keep apart are not stated as distinctions:
     - configuration versus encoded carrier;
     - mathematically available versus derived from OI;
     - generating coherent mixing versus establishing the full probability and composition
       rules.
  3. Residual sequence wording. Two places lead with FI-1 and place the other gaps "beside" it:
     - §5.2's "earliest missing mechanism" bullet (l.533–534);
     - §11's conclusion (l.983–986).

    These are correct as conditional statements, but they are not a parallel presentation.

## Proposed changes (not applied)

**C1. New §5.3, inserted after §5.2 (after l.559).**

> ### 5.3 The three gaps in parallel
>
> The phase, state mixing (FI-1, the necessary condition of the flow) and H-Bell are independent
> obligations. None is derived from another in the sources read, and the phase and the flow are
> kernel-proved independent (K `obligations_independent`). No one of them is the earliest
> unconditionally: FI-1 comes first only once the phase is taken as stated (Main:590, GR:268).
> State mixing is a common research target. It is the flow's necessary condition, and its
> candidate source 1, the lift S13, is shared with the spatial route (§5.1).
>
> | Gap | Carrier | Scope | Proved toward it | Open |
> |---|---|---|---|---|
> | **Phase (O1)** | Configuration carrier: the quarter phase on every state at every level (`PhasesAvailable`). Its encoded counterpart, the encoded quarter phase $S$, is a separate object on an encoded carrier | Exact, finite, endomorphic (kernel predicate). The encoded $S$ is at single-qubit stabilizer scope (QP) | **Not supplied** by the stated access: K `obs_not_phasesAvailable`, failure exhibited at level 2; for any ones-fixing architecture, failure at level one, with no claim at each composite level (GR:260; K `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing`). **Necessary condition:** an operator moving the all-ones ray, not shown sufficient (GR:260). The phase is **available by stipulation**, as a member of the substratum class (K `phase_monomial`), and is **not derived** (Main:590). **Mathematically available** in `PolC` at every level (K `polarizedTheoryC_phasesAvailable`), through a polarization map the corpus does not supply. **Encoded:** non-adaptive native $S$ is excluded on class N (QP Lemma G2); NNB supplies $S$ with a C-CP cost (premise I, QP:805–840); MECH-2's Theorem U2 excludes encoded $S$ for every fixed bijection under the frame $R1^{\otimes n}$ and H-LIFT | A source of the configuration-level phase from the stated dynamics and access. On the encoded side, adaptive native $S$ (QP:897–915) |
> | **State mixing (FI-1; flow O2)** | Configuration carrier at level one, $S\times\mathrm{Fin}\,1$. Encoded non-monomial maps are a different object and do not meet FI-1 | Exact finite endomorphic operational QM within the structural architecture. FI-1 is not necessary for finite-accuracy reproduction of quantum statistics (Main:566, Main:584, Main:600) | **Necessity**, in one direction only (K `exists_nonMonomial_of_layerFlowExecutable`), with a stronger form (K `uncountableNonMonomialRays_of_layerFlowExecutable`). **Not sufficient** (`PolC`). **Not supplied** by the stated read/write access or by the lift formulations that land in the operational interface (§5.1 *Status*). **Mathematically available, not derived:** the gate flows and `driveQ` (§5.1 *Closest derived objects*). **Available by stipulation:** `onesTheory`, `LayerFlowExecutable`, and the postulated datum of `state-mixing-coupling-audit.md` | The four candidate sources of §5.1: the site-space wave lift (S13), the lift's channel realizations, C5 candidate 2's map, and extended access |
> | **H-Bell** | Configuration (ontic) level on the SM/GR graph: preparation-indexed adjacency or a nonlocal response map, with diagonal outcome statistics (Sub:131; Main:414) | The quantum Bell set with operational no-signalling and curvature stability (H-Bell (i)–(iii), Sub:133). The finite realizations cited (Main:566, Main:584) are finite-accuracy and are not on the SM/GR graph | **Reference graph Bell-local**, CHSH $\le2$, under measurement independence and screened wings (Main:416). The **unrestricted response class reaches the PR box** (Main:362), so the quantum set is not selected natively. Finite response constructions **realize no-signalling target laws** (Main:429). Which hypothesis is given up is a **choice** (Main:403–406). MECH-2's Proposition B gives a necessary condition (M-FIX); that record promotes no claim | H-Bell (i)–(iii) for a specified preparation-indexed rule (Sub:133) |
>
> Three distinctions are kept apart throughout:
> - **Configuration versus encoded carrier.** FI-1 and the phase (O1) are statements about the
>   configuration carrier. Encoded $S$ and $H$, and encoded tetrahedral rotations, are maps on
>   encoded carriers. They can be non-monomial, or phase-like, while every configuration-level
>   operation stays in `permTheory` (QP:846–877; MECH-2 §0).
> - **Mathematically available versus derived from OI.** The gate flows, `driveQ`, `PolC`'s
>   phases and Hadamard, and the postulated mixing datum exist as mathematical objects or as
>   stipulated classes. None is derived from the stated dynamics and access (§5.1;
>   `coherent-continuum-source-audit.md`, routes S5 and S8).
> - **Generating coherent mixing versus the full probability and composition rules.** Even
>   with FI-1 and the flow, exact QM follows only with the phase as well, within the closure
>   (K `qm_of_derivedOI_layerFlowExecutable`). Complex matrix kinematics and the tensor-product
>   composite are taken as given (Main:218). The Born exponent is not selected (Main:556). The
>   physical preparation mechanism is open (B25). `PolC` has non-monomial operators, the phases
>   and the closure, and is not QM.

**C2. §5.2, the "earliest missing mechanism" bullet (l.533–540).** Lead with the parallel
statement. Replace "With those inputs granted and the phase taken as stated, it is a mechanism
supplying FI-1, …" with:

> There is no single earliest missing mechanism. Three stand side by side, none derived from
> another (§5.3): a source of the phase (O1), a source of state mixing with FI-1 as its
> necessary condition (O2), and the H-Bell response mechanism. Only relative to the phase taken
> as stated is FI-1 the first.

Keep the S13 sentence as it is.

**C3. §11, the last bullet (l.983–986).** Replace "With the phase taken as stated, the first
unsupported step … is FI-1; the phase and H-Bell are unsupported implications beside it, not
after it, …" with:

> The phase, state mixing (FI-1) and H-Bell are independent unsupported obligations, with the
> carriers and scopes of §5.3. FI-1 is the first step toward exact finite endomorphic
> operational QM only with the phase taken as stated. The earliest unproved assumptions are the
> stated inputs upstream of all three (§5.2).

**C4. §0 item 8 (l.120).** Change "(§5.1, §5.2)" to "(§5.1–§5.3)".

**C5. Dispositions r4.** Record C1–C4 as traced to this owner instruction.

## Checks behind C1, read at `fd539e15`

- `obs_not_phasesAvailable` and `permTheory_not_phasesAvailable`: the docstrings say "failure
  exhibited at level 2" (SubstratumInterfaceAudit.lean:668–670).
- `onesFixing_not_phasesAvailable`: failure at level 1, with "unavailability at every composite
  level … not separately proved" (PhaseSource.lean:53–55).
- `polarizedTheoryC_phasesAvailable` (PolarizationClosure.lean:448): on the `Fin 2` carrier.
- `phase_monomial` (SubstratumInterface.lean:102).
- Main:362, Main:414, Main:416, Main:429; Sub:131, Sub:133; MECH-2 Proposition B
  (DESIGN:544–560).
- **Not established:** whether H-Bell's target needs exact rather than finite-accuracy
  realization. The sources state no such qualifier for H-Bell, and C1 does not supply one.
