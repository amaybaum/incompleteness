# Draft — ROADMAP row K (scratchpad only; not committed, not part of NB-1)

Written against `verification/ROADMAP.md` at `D` = `fdebc6e3`. Two insertions, in the file's own format.

## Cover note for the owner (not part of the insertion)

- **Placement.** The queue-table row goes directly after the `H-Bell` row. The section goes directly after
  `### P1 — H-Bell and composite closure`, before `### P2 — Bekir–Golomb integer classification`.
- **Research-only work.** The K2.0 / K2.2 / K2.3 results exist only as read-only research in the scratchpad. Under the
  ROADMAP's own rule (each row links to its audit or preregistration and carries no proof discussion), they are not
  cited or summarised in the insertion. K2 reads `OPEN` with no governed round. They enter the row only after a
  governed round records them.
- **K1's status.** `ACTIVE` is correct while NB-1 executes, per the status vocabulary ("a round is running"). The link
  targets the preregistration path. That path exists on `main` only after NB-1 lands, so the row is committed after
  the landing, or together with a link that resolves at that commit.
- **K0 is `GAP`, not `OPEN`.** The status vocabulary reserves `GAP` for a condition with no predicate at all in the
  formal interface, and the K0 source audit found no state-space-as-convex-set object.
- **Voice.** The file is public. The text avoids process vocabulary and makes no claim beyond the linked artifacts.

## Insertion 1 — the queue table, after the `H-Bell` row

```text
| **P1** | K — pre-quantum kinematics: ball and full-effect local systems, the dimension, the complex composite | OI→QM / Reconstruction | **OPEN** — K1 **ACTIVE** (round NB-1, conditional on one common NOT on identical copies); K0 **GAP**; K2 **OPEN**; K3 is the landed typed Kraus characterization | complex quantum kinematics in the conclusion rather than the premises |
```

## Insertion 2 — the section, after `### P1 — H-Bell and composite closure`

```text
### P1 — K: pre-quantum kinematics

The finite operational characterization (`oiPlus_iff_qm`, `typed_determined_iff`) is stated over
complex matrix carriers: the quantum kinematics is in its premises. This row tracks the obligation
to derive that kinematics, or to isolate the minimal field-free principles from which it follows,
before the typed characterization is invoked. It has four parts, each with its own status.

- **K0 — local state spaces.** Derive, or state as an explicit principle, that a binary system's
  normalized state space is a Euclidean ball and that its effect cone is the full dual cone.
  **GAP.** No round addresses it, and the formal interface has no object for a state space as a
  convex set: every state space is given as a simplex or as a positive-semidefinite cone. A fixed
  finite substratum can carry the ball's state geometry but not its sharp effects ([Main]), so a
  full-effect principle, if adopted, belongs to a limit endpoint (row H-∞).
- **K1 — the dimension.** For two locally tomographic `d`-balls with full self-dual effect cones, one
  common NOT involution on both copies, and a native CNOT satisfying the two NOT relations with
  two-sided product positivity, `d ∈ {1, 3}`. **ACTIVE** (round NB-1). The theorem for general `d` is
  certified in layers — kernel, exact computation and written proof — and is not a kernel theorem.
  Its reading for OI is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, which the corpus
  does not derive; dropping the control-NOT relation, or allowing different NOTs on the two copies,
  admits `d = 5` countermodels.
- **K2 — the composite.** Select the standard complex two-qubit composite, up to local orientation,
  from the `d = 3` native gates together with the local reversible structure available. **OPEN.** No
  governed round has addressed it.
- **K3 — the operations.** Once the complex kinematics is reached, the typed characterization gives
  exactly the finite typed Kraus instruments. **Landed** (`typed_determined_iff`,
  `typed_determined_of_oiPlusElem`), under its own premises.

The premises this row does not discharge are named here so that none is counted silently:
ball-shaped local state spaces and full effects (K0), identical-copy covariance (K1), and the source
of the local reversible structure K2 requires.

→ [round NB-1 preregistration](programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/preregistration.md)
→ [`TypedCompletion.lean`](lean-mathlib/OIBridge/TypedCompletion.lean)
→ [`CarrierGeneralOIPlus.lean`](lean-mathlib/OIBridge/CarrierGeneralOIPlus.lean)
```
