# FRONTIER — result note (read-only; base `b7af4852b79fa3bfa90e9b5c2eca3aca6890395a`)

Companions: DEPENDENCY.md (the DAG), FRONTIER.md (missing arrows), DELETION_TESTS.md, MINIMAL_HYPOTHESES.md.
Every kernel citation was read at the base; design notes, prose, names and comments were used as pointers only.
No file in any checkout was modified; no git write command was run; nothing under `level3b/` was read.

***

## 1. Most likely final theorem statement

With the bridge lemmas of FRONTIER.md accepted and the premises of MINIMAL_HYPOTHESES Bundle A in force:

> **(Single system.)** Let `D` be a directed system of finite observer stages with stage consistency and finite
> rank, whose completed body `Ω` (compact, convex, nonempty relative interior) carries a group `G` of affine
> automorphisms induced by reversible, affinely respectful, limit-closed operation data, a sharp available seed
> `r`, and effects closed under sequential composition with `G`. If `G` is boundary-transitive
> (`BoundaryTransitive Ω G`) and energy-observable, then `Ω` is affinely a 3-ball, the available effects contain
> the sharp directional family `(1 + b·x)/2`, and the state/effect pair is the qubit's up to an affine change of
> coordinates.
>
> **(Composite.)** If two identical such systems compose locally-tomographically, share one native NOT, and admit
> a reversible nonlocal gate with the native CNOT relations and two-sided product positivity, the local dimension
> is forced to 3 independently of energy observability (NB-1), and — conditional on the open K2 composition
> theorem — the composite is the quantum tensor product.
>
> **(Operations.)** If at every composite level the theory is implementation-local, embedded, and drives one
> transition continuously (phase-free richness; in GR's smallest form one executable layer flow within the
> substratum's closure with the phase intervention), then the available outcome families are exactly the finite
> Kraus instruments on every carrier (`oiPlusMin_iff_qm`, `typed_determined_iff`), up to one global antiunitary
> orientation (`operational_orientation_noGo`), which one oriented (passivity) premise removes.
>
> **(Reverse.)** Finite-dimensional complex QM satisfies every premise: kernel witnesses for the drive, exact
> transitivity, the sharp seed and its orbit, (SEC)/(SF)/K∞-1 on the ball, the five completion conditions, the
> layer flow, local tomography, purification and the pure seed; written/exact witnesses for EO, ORD∞, OFF, a QM
> stage tower, LIMCLOSE-C and the NB-1 gate.

This is an **F2/F3-shaped** statement: an explicit selection bundle on top of OI, not a derivation from OI. No arrow
from the OI axioms (A1–A6, C1–C4, Axioms 1–2) to any item of the bundle is sealed; the sealed arrows in that
direction are negative (`oi_alone_not_qm`, `substratum_residual`, `obs_not_layerFlowExecutable`,
`onesFixing_not_phasesAvailable`), and the only OI-sourced exposed sector computed exactly (Level 3A) is a
polytope with a finite action group.

## 2. Assumptions most likely to disappear after bridge lemmas

1. **ORD∞** — derivable from exact `BoundaryTransitive` (FRONTIER F7(b)); its only surviving content is "the body is
   not a point or a segment".
2. **The drive as a separate premise (D1–D9)** — D1–D8 from ORD∞ by Route Γ (F5); D9 (OFF) is not needed when
   transitivity is assumed rather than derived.
3. **DIM3** — from {TRANS, EO} (F8; Thread R), or from the composite layer (NB-1).
4. **The ellipsoid / `T '' Ω = ball3`** — from exact TRANS + IIP-1 via Lemma B (F7(c)); DIM3 and the drive are not
   needed for it.
5. **(SEC), (SF), K∞-1 on the ball, P1, Kraus soundness, composite unitary control, typed QM, the OI-core
   conjunct** — already sealed consequences (MINIMAL_HYPOTHESES Bundle B).
6. **Copy naturality** — possibly, via the untested "type covariance of native inversion" reduction.

## 3. Assumptions most likely to remain explicit

- **EO** (the single-system fingerprint of ℂ): independent of every other single-system clause (B⁴/Sp(1), exact),
  unsourced, with no kernel vocabulary.
- **Exact boundary transitivity** (`BoundaryTransitive`), or its continuity-bearing drive substitute: no sealed
  hypothesis implies it; the kernel's own control `not_boundaryTransitive_flow` shows a continuous flow does not.
- **LIMCLOSE-C** / limit-closure of availability: independent at the matrix level (`fixedGateTheory`).
- **SEQ and TRANS±** (operational availability of the drive and of transported effects): no source in any field.
- **FiniteRank of an infinite-substratum completion** and **an OI stage tower itself**: unknown; the finite case is
  provably a polytope (NG1), where every selector fails.
- **Composite existence, LT, a nonlocal reversible `G`, common `N`**: premises; common `N` and the control-NOT
  relation are exactly independent; LT and `G`-existence have no corpus witness either way.
- **Composite-level phase-free richness / implementation locality / embedded observation**: the five completion
  conditions are mutually independent in the kernel (`five_way_minimality`, `oiPlus_independence`,
  `independence_matrix`), and nothing single-system supplies the level-`n` drive.
- **Orientation**: a genuine ℤ₂^anti residue of all operational data (`operational_orientation_noGo`).
- **The relative evolution between two times** (ROADMAP P0): open and orthogonal to the reconstruction.

## 4. The single next lemma / countermodel search that reduces uncertainty most

**Lemma (kernel-cheap, decisive for the shape of the selector):**
`BoundaryTransitive Ω G → PreservesBody Ω G → (∀ x, IsBoundaryState Ω x → x ∈ extremePoints ℝ Ω) ∧
(2 ≤ dim Ω → ∃ g ∈ G, ∀ m ≥ 1, g ^ m ≠ 1)`, together with the IIP-1 corollary
`IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty → BoundaryTransitive Ω G → PreservesBody Ω G → Ω is the
invMatrix-ball about the centroid`.
It settles that the kernel's K∞-R is *not* the SELECT note's non-selective TRANS (it excludes every polytope of
dimension ≥ 2, the Level 3A octahedron included), makes ORD∞ redundant, removes the drive and DIM3 from the
ellipsoid step, and reduces the single-system selector to {exact TRANS, EO, V4′-availability}. It costs little:
IIP-1 and Lemma B (`eq_closedBall_of_frontier_subset_sphere`, KF:770) are landed; the extreme-point argument is two
lines; the uncountability step needs Schur–Jordan or the closed-subgroup theorem (the one citation).

**Countermodel search (decisive for F1 versus F2/F3, deliberately not run here — it is Level 3B's territory):**
an OI protocol tower (lattice cone tower, product or correlated initial measure) with `FiniteRank` whose completed
body is **not a polytope** (equivalently, carries an infinite-order automorphism). Level 3A's linear rule gives the
octahedron; OI-STAGE's exact ranks grow for the nonlinear rule. If no OI tower has finite rank and a non-polytope
body, every selector above is unsatisfiable on OI-sourced completions and the final theorem is F3 with the
selector as an explicit, OI-external principle.

## 5. Ingredients NOT located at the base (classified unresolved)

| ingredient | where the notes place it | status |
|---|---|---|
| `EnergyObservable`, `genAlg`, `Obs`; any dynamical-correspondence statement | Thread R, SELECT | absent (grep over all declarations and comments) |
| `DriveCore` (drive without continuity/NOT) | Thread N | absent |
| `OperationalDrive`, `EffClose`, `BodyOperationalTheory`, `SeqClosed`, `DriveAvailable` | Threads O, P | absent (Thread P's `.lean.txt` is uncompiled) |
| LIMCLOSE / field-neutral closure of availability | DRIVE, SELECT | absent; only `DiscreteCompletion.ClosureAvail` (DC:63), ℂ-typed and "deliberately not adopted" |
| `elementaryDrivability_of_substratum` | several notes | absent |
| `ell_ellipsoid`, `ell_closure`, `rotWords`, `kR_exact_words`, `NormalizedInvariance`, `ell_normalization` | Thread N | absent |
| `dim3_of_transitive_energyObservable` | Thread R | absent |
| any `DirectedStages` instance from an OI construction (PT/CT) | OI-STAGE | absent; instances are `badD`, `bitTower`, `midD` only |
| any `ElementaryDrivability` other than `ball3Drive`; the B⁴/Hamel/Sp(1) drives | Threads N, R, O | absent |
| field-neutral composite of bodies, local tomography, readout, discard, register | K∞ design, NB-1 header | absent; NB-1's "locally tomographic" is prose in the header |
| NB-1 general-`d` S1/S2/S4 | NB-1 | written + exact `d ≤ 7`; not kernel |
| a QM `DirectedStages` with phase/Clifford `OpDatum` (reverse instance) | DRIVE §1 | absent |
| Cartan closed-subgroup theorem; compact rank-1 classification | DRIVE Γ2, Thread R step 8 | not in Mathlib at the pinned tag (per Thread N's table; not independently re-audited) |
| H-Bell round result | `programmes/oi-qm/h-bell/round-hb-1-obligation-shape` | preregistration only; no result note |
| kernel Bloch adapter (ball ≅ qubit density matrices; `SO(3)` ≅ `SU(2)` conjugation) | implicit everywhere | absent (`qubit_certain_face` KF:995 is a fragment) |

## 6. Predicates treated informally as equivalent that differ materially (flagged)

1. **TRANS (SELECT) ≠ K∞-R (kernel).** `select/checks.log` tests "Sym({0,1}²) transitive on the 6 vertices" and
   infers "TRANS is satisfied by the octahedron". The kernel's `BoundaryTransitive Ω G` (OG:79) quantifies over
   *all* `IsBoundaryState`s (KF:130), including relative interiors of faces; affine automorphisms preserve extreme
   points, so **no polytope of dimension ≥ 2 is `BoundaryTransitive` under body-preserving maps**. The SELECT gem
   "transitivity does not select; ORD∞ is the first selective premise" holds for vertex-transitivity and fails
   for the kernel predicate, under which ORD∞ is derivable (F7). The §4 composition target is stated with
   `BoundaryTransitive`, so its hypothesis 2 is already strong enough to exclude the octahedron without
   hypothesis 1.
2. **K∞-R exact words ≠ closure transitivity.** Hamel model (Thread N): dense orbit, countable word group;
   `flow_continuous` load-bearing. OG-1 consumes the exact form.
3. **ORD∞ ≠ continuous one-parameter flow ≠ boundary transitivity.** ORD∞ ⇒ flow needs compactness + finite rank +
   closure (Cartan); flow ⇏ transitivity (`not_boundaryTransitive_flow`, OG:620, kernel); transitivity ⇒ ORD∞ (F7(b)).
4. **`ElementaryDrivability` ≠ an available drive.** The structure (KF:264) has no availability field; Thread P's
   CM2 (exact) has the drive present with its flow unavailable, V4′ failing.
5. **SC∞ ≠ LIMCLOSE-C.** Table consistency of forward maps (SC:78) versus limit closure of available operations;
   CMP-1 closes states (`body D := closure …`, SC:141), never operations.
6. **(SEC)/(SF) of KINF-1 ≠ of KINF-2.** The halted round's predicates were trivialized by the unit effect;
   KINF-2's quantify over `IsProperOn` effects (KF:125–140). Only KINF-2's are authoritative.
7. **`PreservesBody Ω G` vs `g '' Ω = Ω`.** Equivalent (two directions), but IIP-1 is stated with the latter and
   OG-1 with the former; the chart form is `image_bodyR_eq` (IIP:428). Adapter, not content.
8. **`OIPlus` (CompletedOI:418) ≠ `OIPlus` (CarrierGeneralOIPlus:185).** Same name; the first carries the OI-core
   conjunct. `oiPlus_qubit_iff` (CarrierGeneralOIPlus:224) identifies them on the qubit only.
9. **"Phase-free richness ⇒ composite control" is conditional on iterated ancilla closure** at carriers with ≤ 2
   states (`control_of_phaseFree`, MR:529, via `descend` and `not_hControl_two`) — not an unconditional
   implication, contrary to a casual reading of GR.md:246.
10. **"Composite" in `FiniteOperationalTheory` ≠ two arbitrary systems.** Levels are `A × Fin n` (ancilla
    extensions of one visible carrier); two-system composition `A ⊗ B` with a `B`-side theory is not an object of
    the interface, which is why NB-1's two-copy hypotheses have no kernel home.
11. **Local tomography (NB-1 header, GPT sense) ≠ `local_tomography_physical`** (InstrumentDilation:440), a theorem
    on `Matrix (A × B) (A × B) ℂ` that presupposes the quantum tensor product; using it to supply LT is the
    circularity the mission names.
12. **`DerivedOI` ≠ bare OI.** `DerivedOI` (RouteB:141) includes `PhasesAvailable`, the phase intervention GR calls
    "an assumption on the substratum class"; the layer-flow equivalence `derivedOI_qm_iff_layerFlowExecutable'`
    is relative to that closure, not to the OI axioms.
13. **"Drives the elementary transitions" in two strengths.** `DrivesElementary` (SubstratumSource:77) demands
    flows, exchanges and quarter phases at every carrier; `PhaseFreeRichness` (MR:423) one driven pair and the
    exchanges per level, no phase. Equivalent theories (`oiPlusMin_iff_oiPlusPos`), different resources.
14. **"Represented" ≠ "available".** Arc D's quarantine (PROGRAMME §3.12) is sealed at the matrix level; every
    Q*/Q_fb statement (N1) carries no availability content, and the notes respect this. Recorded because the
    final theorem's single-system leg is a representation statement until the availability premises (V4′ and its
    sources) are added.

## 7. Classification of the thread's findings (§A.31)

- **NEW:** item 6.1 (the SELECT/kernel TRANS divergence and its consequence: ORD∞ redundant, drive and DIM3
  unnecessary for the ellipsoid under exact K∞-R); the chart-body compactness adapter (F3) as the one missing
  piece between IIP-1 and OPACT-1; the complete inventory of absent identifiers (§5).
- **POSITIVE:** the sealed tail OG-1 → NB-1 Lorentz bridge composes literally with CMP-1's `sharpSeed_completion`
  and OPACT-1's `preservesBody_inducedEquiv` once the normalization `T '' Ω = ball3` is supplied — the types do
  line up on the ball side.
- **CONFIRMING:** EO independent (Thread R), LIMCLOSE-C independent (DC fixed-gate theory), composite premises
  independent of control (rounds 34–39), V4′'s decomposition (Thread P).
- **BORDERLINE:** whether `FiniteRank` can hold for any non-polytope OI completion — the F1/F2 decision point,
  left to Level 3B.

## 8. Standing

Nothing here is proved; nothing is modified; no round is proposed. Evidence types are stated beside each claim:
kernel (identifier + file:line at the base), exact off-repo (replayed scratchpad scripts, cited as pointers),
written (this note or a cited note), citation (literature). Under PROGRAMME §6, the chain's status is:
representation **Derived** (N1); single-system selection **Conditional** on {TRANS-x, EO, V4′-availability,
FiniteRank, LIMCLOSE-C}; composite **Conditional/Open** (NB-1 conditional, K2 open); operations **Conditional** on
the five completion conditions; sourcing of any selector from OI **Open** (finite case **Independent** by NG1 /
Level 3A).
