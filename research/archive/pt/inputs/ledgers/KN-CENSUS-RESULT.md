# Kₙ census — elementary-to-arbitrary-carrier lift (read-only, off-repo)

Base: the certified CONSC-2 landing **L = `95cb01ff0c3afdaf35be23b96fff25d79fd6e9fa`** (detached worktree, nothing
written). CONSC-2 changed manuscripts only; every Lean module read here is byte-identical to DIM-1's landing.

## Disposition: **SEPARATE-KN-OBLIGATION**

The arbitrary-n lift is absent: no theorem consumes the reconstructed `d = 3` ball, the candidate K2 route composes
copies of the elementary system and supplies no subspace or face principle, and every theorem of the K3 chain has
carrier-general complex matrix structure in its types. In addition, the census found that two K∞ geometric premises
are false for complex quantum systems of level ≥ 3, so K∞ itself must be scoped to elementary systems — which is why
the lift cannot be absorbed into K∞.

## Q1 — DIM-1 → arbitrary carrier: **no such theorem**

- Import graph of `verification/lean-mathlib/OIBridge` at L (transitive closure, computed): the ball side
  (`KInfFoundations`, `OrbitGeneration`, `OrbitNormalization`, `InvariantInnerProduct`, `StageCompletion`,
  `TransitiveBody`, `NativeGateBall`, `CompositeDimension`, `CompositeInterface`, `CompositionOrder`) and the complex
  operational side (`OperationalAssembly`, `ImplementationLocality`, `SubstratumSource`, `TypedCompletion`,
  `CarrierGeneralOIPlus`, `CompletedOI`, `LevelOneSeam`) share **no import edge in either direction**.
- `CompositeDimension` (DIM-1) is a leaf: no module imports it. Its matrices are real (`Matrix (Fin m) (Fin m) ℝ`).
- The only ℂ object on the ball side is `KInfFoundations.qubit_certain_face` (§F), a fixed `2 × 2` instance labelled
  "imported kinematics and not a field-neutral result".
- The ℂ-side modules mentioning qubit/Bloch/Pauli structure (`DiscreteCompletion`, `PolarizationClosure`,
  `WeylTwirl`) work inside complex matrix carriers already given; none derives a carrier from a qubit.

## Q2 — K2 scope: **composites of the elementary system only; no subspace/face principle**

- ROADMAP K2 (OPEN): "a candidate `d = 3` composition route … the formal composition theorem, the antiunitary and
  complete-positivity bridge, and the relation to the K3 machinery are open." The route's objects are two identical
  d-balls on a locally tomographic carrier (NB-1, DIM-1; the Masanes–Müller 2013 family).
- The off-repo research map (thread R) states it directly: the ball/transitivity premise is elementary-scoped ("ELEM's
  dimension-relevant content is exactly TRANS, which the qutrit violates"), and the one known route to general level
  structure — Hardy's `K = N^r` with integral `r` — "needs N = 3 systems through the subspace axiom, which is outside
  ELEM".
- Repository search at L: no subspace axiom, equivalence-of-subspaces principle, ideal compression, or face-as-system
  principle in any Lean module, the ROADMAP or the programme documents. The only face principle is
  `KInfFoundations.SingletonFaces`, which says the opposite — certain faces are points.
- So K2, even closed, yields composites `B_3 ⊗ … ⊗ B_3` (carriers of dimension `2^k` at best, and only with the
  composite theorem); it produces no 3-level system and nothing equivalent to arbitrary `M_n(ℂ)`.
- (Naming: `PROGRAMME.md:597` uses "K2" as a *grade* label for the two-branch theorem; that is unrelated to the K2
  composite row.)

## Q3 — K3 assumption audit: **carrier generality is in the types**

| object | where "every finite carrier" enters |
|---|---|
| `ImplementationClass` (`ImplementationLocality.lean:244`) | **first entry, at the type**: `∀ (S : Type) [Fintype S] [DecidableEq S], Matrix S S ℂ → Prop` — a predicate on complex matrices at every finite carrier |
| `FiniteOperationalTheory A` (`OperationalAssembly.lean:594`) | **at the type**: operations on `Matrix A A ℂ` for an arbitrary finite carrier `A`, and on `A × Fin n` for **every** `n` (`availExt`, `prepAvail_uniform`, `readout`) |
| `Architecture` (`ImplementationLocality.lean:506`) | premise fields quantified `∀ S` (`one`, `mul`, `smul`, `proj`, `block` with `S × Fin m`) |
| `ContextStable`, `LabelInvariant` (`:359`, `:364`); `DaggerStable` (`MicroscopicReversibility.lean:216`) | premises quantified `∀ R S` / `∀ S S'` |
| `DrivesElementary` (`SubstratumSource.lean:77`) | premise: flows, swaps and phase gates admissible **at every finite carrier `S`** |
| `QuantumArchitecture` (`:86`) | bundles the above |
| `genTheory_qm_of_quantumArchitecture` (`:136`) | concludes per fixed carrier `A`, consuming admissibility at all `A × Fin n` |
| `TypedOperationalTheory` (`TypedCompletion.lean:165`) | **at the type**: `availT` over all carrier pairs `S → S'` |
| `ShadowQuantum` (`:291`) | premise: exact finite QM **on every nonempty carrier** |
| `typed_determined_iff` (`:850`) | `ShadowQuantum ↔` typed-Kraus availability over all `S, S'` |
| `oiPlus_iff_qm` (`CarrierGeneralOIPlus.lean:207`) | per carrier `A`, over `FiniteOperationalTheory A` |

Nothing in the K3 chain derives a complex matrix carrier of size `n` from a two-level system; the carriers and their
ancilla extensions are supplied by the types. ROADMAP K3's "CONDITIONAL on reaching complex matrix kinematics" is
therefore conditional on the kinematics at **every** finite carrier.

## The K∞ scope finding (NEW; assumption-watch marker)

Exact check (rational arithmetic) on the qutrit state space with the full effect family:

- `e(ρ) = tr(Pρ)`, `P = diag(1,1,0)`: an effect, proper (`e(|2⟩⟨2|) = 0`), certain on `|0⟩⟨0|` and `|1⟩⟨1|` —
  **`SingletonFaces Ω (fullEffects Ω)` fails**;
- the midpoint of `|0⟩⟨0|` and `|1⟩⟨1|` is a boundary state (extending beyond it away from `|2⟩⟨2|` leaves `Ω`) —
  **`RelStrictConvex Ω` fails**;
- countercontrol: the qubit's rank-1 test has a single certain state.

So the K∞ obligations as the ROADMAP words them ("the certain outcome of a proper sharp binary test identifies one
state") and the ball conclusion they feed are **false for complex QM at level ≥ 3**. They can only be sourced for
an *elementary* (two-level) system. Consequences: (i) K∞ must carry an explicit elementary scope — which in turn
needs a field-neutral definition of "elementary system"; (ii) the lift from the elementary system to arbitrary
carriers cannot come from K∞ and must be its own obligation, with a principle that relates higher systems to
elementary ones (subspace/face equivalence, or systems built from elementary ones plus a composite theorem). This
should be carried into the successor foundations round that corrects the singleton-face statement.

## Proposed ROADMAP text (not applied)

Under P1 — K, after K∞:

> - **Kₙ — elementary-to-arbitrary-carrier lift. OPEN.** Derive the carrier-general finite complex operational
>   architecture — the complex matrix carriers of every finite size and their ancilla extensions, which
>   `FiniteOperationalTheory`, `ImplementationClass`, `DrivesElementary` and `ShadowQuantum` take as given — from the
>   reconstructed `d = 3` elementary system together with independently sourced composite/subsystem principles. No
>   theorem consumes the DIM-1 ball, and K2's candidate route composes elementary systems only; a subspace or face
>   principle relating higher-level systems to elementary ones is not in the corpus. K∞'s geometric obligations
>   (singleton faces, relative strict convexity, the ball) hold for the qubit and fail for complex QM at level ≥ 3,
>   so they are obligations about elementary systems, and Kₙ is not a consequence of them.

And in the K∞ bullet, the singleton-face entry would gain the scope "for an elementary system".

## Dependency position

```
K∞ (elementary scope) → ball (TRB-1, IIP-1) → effects (EFF-1) → K2 (two elementary copies) → native gate → K1 (DIM-1: d = 3)
                                                                                                         ↓
                                                    Kₙ (elementary → every finite carrier, needs subspace/composite principle)
                                                                                                         ↓
                                                                     K3 (QuantumArchitecture ⇒ finite operational QM)
```

Kₙ sits between K1 and K3; it depends on K2's composite theorem if the composite route is chosen, and on a new
subspace/face principle if the subspace route is chosen.
