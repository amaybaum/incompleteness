# NOTES-E3 — Kₙ: the exact obstruction, and the smallest theorem that moves it

Base L = `9f9f8257`. Evidence as in LEDGER.md. Productivity test (fixed before the probe): a finding counts only if it
is strictly stronger than "no theorem lifts the elementary system to every carrier" and it changes what the obligation
must contain or exposes an assumption hidden in its current statement.

## 1. The obstruction, exactly

The ROADMAP row (:1058–1069) and the census audit (`verification/audits/foundations/kn-elementary-carrier-census.md`)
state three facts, all confirmed at L:

1. **No theorem consumes the DIM-1 ball on the complex side.** Re-checked at L by the transitive closure of the
   `import OIBridge.*` lines: the ball-side modules (the census's list plus the later K1-route modules CompletionAction,
   EffectSpace, K1Bridge, K2Guard, SharpTests, DenseOrbit, ParityNot, OddChar, RelcSelect{Parity,Block,Squeeze,C5}) and
   the complex operational modules (OperationalAssembly, ImplementationLocality, SubstratumSource, TypedCompletion,
   CarrierGeneralOIPlus, CompletedOI, LevelOneSeam) share no import edge, direct or transitive, in either direction.
   `CompositeDimension` is imported directly only by EffectSpace.
2. **K2's candidate route composes elementary systems only**, so at best it reaches carriers of size `2^k`.
3. **Carrier generality is in the types of the K3 interfaces.** Quoted at L:
   - `ImplementationClass` (ImplementationLocality.lean:244): `∀ (S : Type) [Fintype S] [DecidableEq S], Matrix S S ℂ → Prop`;
   - `DrivesElementary` (SubstratumSource.lean:77): `(∀ S … (a b : S) (t : ℝ), 𝓘 S (flow (transition a b) t)) ∧
     (∀ S … (a b : S), 𝓘 S (permMatrix (Equiv.swap a b))) ∧ (∀ S … (a : S), 𝓘 S (phaseGate a))`;
   - `QuantumArchitecture` (:86) bundles `Architecture`, `ContextStable`, `LabelInvariant`, `DaggerStable`,
     `DrivesElementary`; `genTheory_qm_of_quantumArchitecture` (:136) concludes exact finite QM at a carrier from it.

The census concludes that a three-level system, and `M_n(ℂ)` in general, needs a principle relating higher-level
systems to elementary ones — a subspace or face principle — which the corpus lacks.

## 2. Inside the K3 architecture the face principle is already a theorem schema (W-DESC)

**Hidden assumption exposed.** The census treats the subspace principle as missing. At the matrix level it is a
consequence of three clauses that `QuantumArchitecture` already contains:

- `ContextStable` (ImplementationLocality.lean:359): `𝓘 S K → 𝓘 (R × S) (tensorOf (1 : Matrix R R ℂ) K)`;
- `LabelInvariant` (:364): `𝓘 S K → 𝓘 S' (Matrix.reindex e e K)` for every bijection `e : S ≃ S'`;
- `Architecture.block` (:506–517): `𝓘 (S × Fin m) K → 𝓘 S (ancBlock K f e)`, with `ancBlock K f e = Matrix.of fun s t =>
  K (s, f) (t, e)` (AncillaClosure.lean:457).

**W-DESC (written; CONJECTURE [W] + [X]).** Let `𝓘` satisfy those three clauses, `S` finite and nonempty, `T` finite,
`ι : S ↪ T` and `𝓘 T K`. Then `𝓘 S (K.submatrix ι ι)` — every admissible operator compresses to an admissible operator
on any coordinate subspace. *Proof.* (1) `ContextStable` with `R = S`: `𝓘 (S × T) (1_S ⊗ K)`. (2) Fix `s₀ ∈ S`; the map
`(s, 0) ↦ (s₀, ι s)` is injective, and `|S × T| = |S × Fin |T||`, so it extends to a bijection `e : S × T ≃ S × Fin |T|`
with `e (s₀, ι s) = (s, 0)`; `LabelInvariant` gives `𝓘 (S × Fin |T|) (reindex e e (1_S ⊗ K))`. (3) `block` at `(0, 0)`:
the entry at `(s, s')` is `(1_S ⊗ K) (s₀, ι s) (s₀, ι s') = K (ι s) (ι s')`. ∎

**Consequence for drivability.** For `a ≠ b` in `S`, the generators at `ι a, ι b` act inside the coordinate subspace
`ι(S)` and are the identity off `{ι a, ι b}`, so their compressions are the generators at `a, b`:
`(flow (transition (ι a) (ι b)) t).submatrix ι ι = flow (transition a b) t`, and likewise for `permMatrix (swap · ·)` and
`phaseGate`. Hence **drivability at one carrier `T` gives drivability at every carrier of size ≤ |T|**, and drivability
at the carriers `Fin (2^k)`, all `k`, gives `DrivesElementary` outright.

**Exact check** (`experiments/e3_compress.py`, 7/7, `VERDICT COMPRESSION-DESCENT-EXACT`, replay identical; sha256 py
`18c3aa1b…`, out `f4b93781…`): the closed form `(1 − P) + cos t P − i sin t H` of `flow (transition a b) t` solves
`M' = −iHM`, `M(0) = 1` (F0); steps (1)–(3) built literally — tensor, an explicit bijection, reindex, block — return the
three generator families exactly for `(|S|, |T|) = (3, 4), (3, 8), (5, 8)` with non-initial embeddings, 32 ordered pairs
(G1–G3, B1); compressing a flow that leaves `ι(S)` gives a non-unitary block, `B Bᴴ − 1` with entry `−sin² t` (K1).

**Load-bearing `ContextStable` (countercontrol, [W] + [X] instance).** Without step (1), `block` and `LabelInvariant`
cannot reach `Fin 3` from `Fin 4` (no bijection `Fin 4 ≃ Fin 3 × Fin m`). The class "every matrix at carriers of size
`2^k`, unit-disk diagonal matrices at every other carrier" satisfies `one`, `mul`, `smul`, `proj`, `block`,
`LabelInvariant` and `DaggerStable` (unit-disk diagonals are closed under products, scalars of modulus ≤ 1, reindexing,
diagonal blocks and adjoints; `|S| · m = 2^k` forces `|S| = 2^j`, so a block of a full-class matrix lands in a full
class) and is drivable at every `Fin (2^k)`, yet it is not drivable at `Fin 3` (a transition flow is not diagonal) and it
violates `ContextStable` (`1_3 ⊗ X` on `Fin 3 × Fin 2` is not diagonal) — K2 checks the two failure instances exactly.
Whether `block` and `LabelInvariant` are each load-bearing was not tested.

## 3. The smallest theorem that moves Kₙ

**Kₙ-DESC (proposed; provable at L as a pure matrix statement).**

```lean
def DrivesElementaryAt (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] : Prop :=
  (∀ (a b : T) (t : ℝ), 𝓘 T (flow (transition a b) t)) ∧ (∀ a b : T, 𝓘 T (permMatrix (Equiv.swap a b)))
    ∧ ∀ a : T, 𝓘 T (phaseGate a)
theorem compress_mem (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    {S T : Type} [Fintype S] [DecidableEq S] [Nonempty S] [Fintype T] [DecidableEq T]
    (ι : S ↪ T) {K : Matrix T T ℂ} (hK : 𝓘 T K) : 𝓘 S (K.submatrix ι ι)
theorem drivesElementary_of_pow (arch : Architecture 𝓘) (hC : ContextStable 𝓘) (hL : LabelInvariant 𝓘)
    (hpow : ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))) : DrivesElementary 𝓘
-- the iff, one witness per direction (§A.34):
theorem quantumArchitecture_iff_pow :
    QuantumArchitecture 𝓘 ↔ Architecture 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘 ∧ DaggerStable 𝓘
      ∧ ∀ k : ℕ, DrivesElementaryAt 𝓘 (Fin (2 ^ k))
-- (→) projection of `drives`; (←) `drivesElementary_of_pow`
```

Its cost: an `Equiv` extending a prescribed injection between finite types of equal cardinality (Mathlib's
`Equiv.extendSubtype` on a permutation of one type, composed with `Fintype.equivOfCardEq`), `Matrix.reindex_apply`,
`tensorOf_apply`, and a compression lemma for `flow (transition · ·)` — most cheaply through the closed form of F0, i.e.
a lemma `flow (transition a b) t = (1 − P) + cos t • P − (I sin t) • H` for `a ≠ b`, proved from `H³ = H`.

**What the theorem changes.** The Kₙ obligation shrinks from "the operational architecture at every finite carrier" to:

1. **drivability on qubit registers**: an implementation class on the carriers `Fin (2^k)` containing the three
   generator families — what k elementary tokens with K2's composite and the generation results would give (EQ2's
   Theorem C [A], written and conditional on its composition premises), *through a dictionary from the field-neutral
   k-token composite to `Matrix (Fin (2^k)) (Fin (2^k)) ℂ`* (the two-token dictionary is exact, k2c P1 [A]; the k-token
   chart family needs the parity/IE₂ premises, EQ2 §2(b) [A]); and
2. **the closure clauses** `Architecture`, `ContextStable`, `LabelInvariant`, `DaggerStable` of that class. These are
   themselves carrier-general; `ContextStable` is the matrix form of the spectator clause that stage 5 identified as
   β, the clause yielding the composite action (b) [A]. So the carrier-generality of Kₙ, in this formulation, lives in
   the same missing clause as K2's local-action clause.

The face principle the census asked for is therefore not a new principle at the K3 interface: it is `ContextStable +
LabelInvariant + block`. It is still absent at the field-neutral level, where no notion of "a face of a system is a
system" exists — but the route need not use one, if it reaches K3 through qubit registers.

## 4. Classification and scope (§A.31)

- W-DESC and Kₙ-DESC: **NEW** (scoped). They expose that the census's "subspace principle" is implied, at the matrix
  level, by clauses `QuantumArchitecture` already carries, and they reduce Kₙ's "every finite carrier" to qubit-power
  carriers plus those clauses. Pressure test: the favourable reading is that Kₙ is "almost free"; it is not — the
  closure clauses are carrier-general premises, unsourced for any class that drives (the substratum class has them as
  theorems, `substratum_residual` StructuralClosure.lean:383, and lacks drivability), and `ContextStable` is the (b)-type
  spectator clause that stages 4–6 found independent of everything at L.
- Not decided: whether OI supplies drivability on any carrier; whether the k-token dictionary exists without IE₂;
  whether `block` and `LabelInvariant` are individually load-bearing for the descent.
