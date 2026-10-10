# K0 source audit — ball and full effects (read-only, at `D` = `fdebc6e3`)

**Question.** Does anything in the current OI/substratum construction constrain a single system's normalized state
space or effect space strongly enough to imply a Euclidean ball with the full self-dual effect cone?

**Answer: no.** There is no GPT layer to derive it in. Every single-system state space in the corpus is put in by
hand: either classical (row-stochastic matrices, simplices) at the visible and substratum level, or complex matrices
(`Matrix S S ℂ`, PSD) at the operational level. Spot-checked citations are marked ✓.

| # | principle | status | strongest citation | note |
| --- | --- | --- | --- | --- |
| 1 | pure-state transitivity | **assumed**; implicit countermodel | `CarrierGeneralOIPlus.lean:110-117` (`ReversibleRichness`); `DiagonalTheory.lean:390` `diag_not_control` ✓ | Full unitary control is a premise; `diagTheory` realizes the same OI core without it |
| 2 | spectral decomposition | **assumed** (a property of the matrix carrier) | `OperationalRigidity.lean:884`, `hermitian_spectral_edyad` | Mathlib's spectral theorem on `ℂ` matrices, not an operational postulate |
| 3 | self-duality / homogeneity | self-duality **assumed**, proved only for the PSD cone; homogeneity **absent** | `JordanClassification.lean:81-85` | used as a tool inside `M_D(ℂ)` |
| 4 | purification | **assumed** in the matrix model; substratum analogue gives existence only | `BoundaryAudit.lean:104-108`; `Main.md:598-600` | uniqueness of whole completions fails (`fiber_freedom`) |
| 5 | bit symmetry | **absent** | not found | would follow from assumed full control; `diagTheory` breaks it |
| 6 | continuous reversible dynamics | **assumed**, and named as the decisive open property | `SubstratumSource.lean:44-55` ✓ (`DrivesElementary`) | "a continuously drivable off-diagonal reversible transition" — not derived |
| 7 | no-restriction / full effects | **absent** as a principle; **obstructed** at a fixed finite substratum | `Main.md:540` ✓ | the SIC embedding carries the Bloch ball's geometry into `Δ₃`, but the sharp effects fail (`½ + √3/2 > 1` at a vertex) |
| 8 | any GPT layer | **absent** | not found: no `Effect`, `Cone`, `StateSpace` or `GPT` object; prose only (`Structure.md:592`) | the only convexity is simplices and PSD cones |

**What this means for K0.**
- Ballness has no source in the present axioms. Of the principles that give balls in the literature, transitivity and
  continuous reversibility are premises, and bit symmetry is absent.
- **Full effects are worse than absent.** `Main.md:540` records that a fixed finite substratum can carry the ball's
  state geometry but not its sharp effects. So no-restriction is in tension with the finite substratum, and at best
  lives at a continuum or limit endpoint (the H-∞ row).
- The corpus says the same in its own voice, several times (✓ `Main.md:352`): the reconstruction axioms are
  hypotheses of the continuum endpoint; bare finite OI does not select QM; the finite characterization is a
  classification conditional on completion conditions.
- **A K0 theorem would need a new layer first**: a formal object for a state space as a convex set, before either a
  ballness derivation or a named ballness principle can be stated in the kernel.

**Aside, outside K0's scope.** `Main.md:540` opens "Remark (correction of record; …)" and "An earlier version
argued …". That is revision-history voice in `papers/`, which §A.30 and §A.33 prohibit. It needs a separate hygiene
edit, not part of any K round.
