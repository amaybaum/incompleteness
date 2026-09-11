# Milestone: the conditional finite-QM reconstruction

**Frozen formal state: `dev` at `ea70067` (parent `7a89018`).**

This file records a checkpoint in the OI→QM verification programme. It is a status record
for the formal layer, not a manuscript section, and it makes no claim beyond what the Lean
kernel checks at the commit named above.

## Status

> **Current result.** Under explicit compositional and operational-control conditions, the
> OI-compatible framework reconstructs the complete algebra of finite endomorphic quantum
> instruments. The measurement update and the pure ancillary seed required by the
> reconstruction are derived rather than independently assumed.
>
> **Not yet established.** That these conditions exclude additional non-quantum operations,
> or that the required operational conditions themselves follow from bare OI. This is
> therefore **not** an OI ⇔ QM theorem.

Three levels, kept apart:

1. **Bare OI** still admits multiple coherent completions. Three of them, over one shared
   C1–C4 core, are kernel-constructed in `OIBridge/IndependenceCensus.lean`
   (`oi_core_underdetermines_completion`), so the underdetermination is a theorem and not an
   expectation.
2. **OI plus the identified operational conditions** is sufficient to reconstruct all finite
   endomorphic quantum instruments. That is this milestone.
3. **An exact QM characterization** requires proving quantum soundness — that nothing beyond
   the quantum instruments is available — and formally connecting the round-24 OI word
   completion to the operational theory. Neither is done at `ea70067`.

## The theorem

`OIBridge/StinespringAssembly.lean`, namespace `OIBridge.StinespringAssembly`:

```lean
theorem fullInstruments_of_control (T : FiniteOperationalTheory A)
    (hext : FiniteIsometryExtensionSF A) (hctrl : HasCompositeUnitaryControl T) :
    HasFullFiniteEndomorphicInstruments T
```

Unfolded: for every `n m : ℕ`, every square Kraus family `K : Fin (n+1) → Matrix A A ℂ`
with `∑ k, (K k)ᴴ * K k = 1`, and every classical output map `out : Fin (n+1) → Fin m`, the
coarse-grained instrument `instrumentBranch K out` is available in `T`.

The two hypotheses:

- `FiniteIsometryExtensionSF A` — every system-first isometry `V` with `Vᴴ * V = 1` extends
  to a unitary `U` with `U * Esf k₀ = V`. This is a `def : Prop`, carried in the theorem's
  own binder list, not an `axiom` in the file.
- `HasCompositeUnitaryControl T` — for every ancilla size `n` and every unitary `U` on
  `A × Fin n`, the conjugation `conjChannel U` is available on the composite carrier.
  Composite-dimension, not a premise about `A` alone.

### Derived inside the chain, not assumed

- **The Lüders readout shape.** `FiniteOperationalTheory` postulates only that a native
  ancilla readout exists and is map-spectator-independent. `readout_is_localLuders`
  (`OIBridge/OperationalAssembly.lean`) derives the form `id_A ⊗ ℒ_k` from
  `mapSpectatorIndependent_iff_localLuders`. No `H-readout` hypothesis appears.
- **The pure ancillary seed.** The only preparation the structure grants is
  `prepAvail_uniform`, the maximally mixed attachment. `pureSeedPrep_available` proves the
  pure attachment `ρ ↦ ρ ⊗ |k₀⟩⟨k₀|` is available, by reading the uniform ancilla, applying
  the outcome-dependent swap correction (`conj_ancSwap_single`), and forgetting the outcome.
  No `H-pure-seed` hypothesis appears.

### Scope, in the predicate's own name

`HasFullFiniteEndomorphicInstruments`: the Kraus operators are **square**, so this is all
finite **endomorphic** instruments on a fixed system `A` — not "all finite quantum
instruments" unqualified, which needs rectangular Kraus maps or a dimension-changing
encoding.

`HasCompositeUnitaryControl` is a **sufficient** Stinespring architecture for operational
richness. It is not asserted to be necessary for exact system-level quantum operations, and
no theorem here claims it is — the same relationship the round-19 Lie certificate has to
universal operational control (`centralDrift_not_HControl`).

## External boundary

The project's global external-analytic boundary stands at **exactly four items** and is not
widened by this milestone:

1. compact Lie integration,
2. finite isometry extension,
3. PSD square-root / factorization,
4. finite Uhlmann / Schmidt uniqueness.

> **Historical, superseded by the Round 35 boundary audit.** Item 3 was discharged internally in
> Round 34 (`psdFactorization_of_spectral`, `DimensionalCountermodel.lean`); the current unresolved
> external boundary is three items (1, 2, 4 above). See `BoundaryAudit.lean`. The four-item
> statement is preserved here as the record of the boundary at the time of this milestone.
> Rounds 45, 48 and 50 then discharged items 2, 4 and 1 in turn (`IsometryExtension.lean`,
> `UhlmannUniqueness.lean`, `OrbitReachability.lean`); the unresolved external boundary is empty.

**This reconstruction uses only item 2.** Purification and Uhlmann uniqueness are not used:
the assembly needs pure seed, Stinespring, unitary control and local readout only, and the
first of those is itself derived. Items 1, 3 and 4 are untouched by
`fullInstruments_of_control`.

## Formal hygiene at `ea70067`

- No `sorry`, no `axiom`, no `native_decide` anywhere in the Lean layer.
- Every named result carries `#print axioms`, with target
  `[propext, Classical.choice, Quot.sound]`.
- `lake build` clean (3143 jobs).
- `verification/lean/edge_rigidity_probe.py` (R7 lint, thirty-three files) green;
  `verification/lean/bohr_frequency_probe.py` (F35–F39) green.
- `python3 tools/release_gate.py` 11/11.

The supporting chain, in dependency order: `OIBridge/CoherentExtension.lean` (round 17
correlation family) → `OIBridge/InstrumentDilation.lean` (round 20 ancilla-first dilation) →
`OIBridge/MonoidalCompletion.lean` (round 24 compositional principle and control separation)
→ `OIBridge/OperationalAssembly.lean` (rounds 25/25b/25c operational closure) →
`OIBridge/StinespringAssembly.lean` (the Kraus assembly). `OIBridge.lean` imports all of
them, so CI builds every one.

## The open question this checkpoint sets up

What must be added to turn **inclusion** of QM into **equality** with QM?

```
QM_instruments ⊆ Ops(T)      proved at ea70067
Ops(T) = QM_instruments      open at ea70067
```

`FiniteOperationalTheory.avail` is an abstract predicate, so a theory may satisfy the
capstone and still admit a transpose, a trace amplifier, or any other non-quantum linear
map. Closing the gap needs a soundness principle, which is a restriction on what a theory
admits and cannot be constructed the way richness was. Separately, round 24's `HComp`
speaks about coherent completions of OI intervention words while `FiniteOperationalTheory`
speaks about operational circuits; those are not yet one object, and conjoining predicates
on unrelated parameters would not make them one.

Work after this checkpoint builds on it rather than restating it.
