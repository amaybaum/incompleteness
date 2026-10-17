# P0 subsystem locality, correction 1 (2026-10-15): circuit depth and the Heisenberg cone

Append-only correction, raised in owner review. `RULES.md`, `RESULT.md`, `p0_exact.py` and its
output are unchanged.

## The defect

`RULES.md` §2 defines `L-disc` as follows: a lift is `d`-local if every tick increment
`U_{t+1}U_tᴴ` is a depth-`d` circuit of gates on edges. It then adds: "Equivalently for the cone:
conjugating any site operator by the increment leaves it supported in the radius-`d` ball."

The two are not equivalent in general.

- **Depth `d` implies the radius-`d` cone.** Conjugating a site operator by one layer of gates
  enlarges its support by at most one edge, so `d` layers enlarge it by at most `d` edges.
- **The converse needs further assumptions about how the gates are scheduled and how the circuit
  is realized.** Translations show this:
  - On a ring, a translation has a radius-1 cone and is not a depth-1 circuit.
  - On an infinite chain, a translation has a nonzero index, so no finite-depth circuit realizes
    it.

`L-disc` is the circuit form, and the radius-`d` cone is a consequence of it, not a restatement.

## What it bears on

Nothing measured changes.

- `L-disc` was stated and not tested. Every verdict concerns `SL-U`.
- The statement that `L-disc` yields `SL-U` on a cut that no edge crosses holds under either
  reading:
  - A depth-`d` circuit with no gate crossing the cut is a product across it.
  - A unitary whose cone never crosses the cut maps each side's operator algebra into itself.
    Then the argument written for EQ1 in `RESULT.md` makes it a product.

## The relation to E1-L, stated with its existing record

F2-2 correction 1 (on the F2 research branch) classifies E1-L's three locality-type properties by
generator family:

- **L0, completion of the tick.** It holds on `Γ_comm` and fails on `Γ_all`.
- **L3, the strict one-edge cone.** It holds on `Γ_comm` and fails on `Γ_all`.
- **L1, factorization across uncoupled blocks.** It holds on all of `Γ_all`, including choices that
  fail L0 and L3.

Hence `SL-U` holds across every cut that no edge crosses for every E1-L generator choice. Even if
it were sourced from E1-L, it could not select `Γ_comm`.

The forward implications from `Γ_comm` to L0, L3 and L1 are F2-2 correction 1's. Whether the strict
cone implies `Γ_comm` is open.

In addition, no map identifies Track B's lifts, carriers, hidden factors or declared decomposition
with E1-L's sites and evolutions. So no E1-L property bears on a Track B lift until that interface
is specified.

## Three distinct candidates

This round and the F2 records bear on three different possible additions. None is adopted, and
none implies another:

- **No-signalling between declared parts.** It needs a physical source, such as relativistic
  causality or uncoupled interaction.
  - At `|A| = 1` it is equivalent to `SL-U`.
  - At `|A| ≥ 2` it is strictly weaker (`P0-NS-WEAKER`).
- **Hidden-sector separability.** This is the surplus of `SL-U` over no-signalling at `|A| ≥ 2`.
- **A commuting-generator rule for E1-L's layers (`Γ_comm`).** It concerns edges that share a
  site, a setting where `SL-U` has no content.
