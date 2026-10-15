# F2-5 — OI's operational primitives through E1-L's dictionary: rules

This is an exploratory research record on the F2 research branch. It is kept separate from BG-2 and from P0's locality
work. It is not a native round and adopts nothing. It is written and committed before its script exists. The decision
rules fix what each measurement decides; they do not fix expected values.

## 1. The question

F2-4 (`../f2-4-control-robustness/RESULT.md` §5) lists what unitary control does not supply: preparation,
measurement, holding a state, ancillas and composites.

On OI's own carrier `ℂ^Conf` (`obsTheory 𝒮 = permTheory 𝒮.Conf`, SubstratumInterfaceAudit.lean:769), the adopted
kernel already supplies several of these:
- a basis seed (`pureSeedPrep_available_of_swap`, OperationalAssembly.lean:675);
- the Lüders basis readout (`readout_is_localLuders`, :658);
- the uniform attach and the discard (`FiniteOperationalTheory`, :594–649);
- spectator adjunction (`instAvail_withSpectator`, ImplementationLocality.lean:820).

Phases are what is missing (`NonnegBounded`, FrozenSourcing.lean:84).

E1-L does not enlarge that theory. It replaces the carrier: `ℂ^Conf` becomes `ℂ^{V^N}`, and "the configuration-bijection
class is replaced, not enlarged" (thread H, E1(b)). So no adopted theorem about `ℂ^Conf` transfers to E1-L
automatically.

This study asks, for each of OI's primitives, whether its image under E1's dictionary is a physical operation on the
register. The dictionary sends a law on the phase space `Conf` to an operator via phase-point operators (thread H,
E1(e)1 and P-1). Being physical means positive, completely positive, or a state, as the case requires. The answer says
which ingredients OI's adopted operational theory supplies to E1-L through the dictionary, and which E1-L has to
postulate or replace.

## 2. The dictionary (fixed)

- **Prime and phase space.** `q = 3` with `ω = e^{2πi/3}`, so all arithmetic is exact in `ℚ(ω)`, whose real subfield is
  `ℚ`. A site's phase-space point is `z = (x, ξ)`, where `x` is the registered current component `c` and `ξ` is the
  hidden previous component `p`.
- **Weyl operators.** `D(x, ξ) = ω^{−2⁻¹ x ξ} Z^ξ X^x`, with `X|y⟩ = |y+1⟩` and `Z|y⟩ = ω^y |y⟩`.
- **Phase-point operators.** `A(z) = D(z) Π D(z)†`, with `Π|y⟩ = |−y⟩`. On `N` sites they are tensor products of
  one-site ones.
- **States.** A law `μ` on `Conf` maps to `ρ_μ = Σ_z μ(z) A(z)`.
- **Operations.** A (sub)stochastic map `T(z' | z)` maps to `Φ_T(ρ) = Σ_{z,z'} T(z' | z) W_ρ(z) A(z')`, with
  `W_ρ(z) = q^{−N} tr(A(z) ρ)`.

This is Wootters' and Gross's discrete Wigner representation for odd `q` [L: Wootters 1987; Gross 2006]. A different
linear relabelling of `(x, ξ)` changes the dictionary but none of the counts below. `SL(2, q)` is normal in
`GL(2, q)`, so the relabelling maps the affine symplectic group to itself, `AGL` to itself, and lines to lines.

## 3. Cells (N = 1 unless stated)

| cell | positive token | rule |
| --- | --- | --- |
| OD-SUB | `OD-SUB-LINES` | Every `A(z)` is not PSD. For every 3-subset `S` of `Conf` (84 of them), `Σ_{z ∈ S} A(z)/3` is PSD iff `S` is one of the 12 affine lines |
| OD-REV | `OD-REV-CLIFFORD` | Over all `9!` permutations `π` of `Conf`: `Φ_π` is CP exactly for `π ∈ ASL(2,3)` (216 maps) and positive exactly for `π ∈ AGL(2,3)` (432). Every other `π` maps some line to a non-line, which by OD-SUB sends a stabilizer state to a non-PSD operator. On `AGL ∖ ASL`, `Φ_π ∘ θ` is CP, where `θ` is the transpose in the computational basis |
| OD-PREP | `OD-PREP-REGISTERED-UNIFORM` | Every point-configuration law `δ_z` maps to a non-state. For each registered value `x = a` and each hidden prior `ν` on the 28 laws with entries in `{0, 1/6, …, 1}`, `ρ = Σ_ξ ν(ξ) A(a, ξ)` is PSD iff `ν` is uniform. The counting measure on `Conf` maps to `I/3` |
| OD-READ | `OD-READ-BACKACTION` | The non-disturbing readout `T_k(z' ∣ z) = δ_{z'z}[x(z) = k]` gives a `Φ_{T_k}` that is not CP, for each `k`. The re-randomizing readout `T'_k(z' ∣ z) = [x(z) = k][x(z') = k]/3` gives exactly the Lüders map `ρ ↦ Π_k ρ Π_k`, for each `k`. The two agree on every diagonal `ρ` |
| OD-AD | `OD-AD-TRANSFER` | At `N = 2`: `A(z₁, z₂) = A(z₁) ⊗ A(z₂)` for all 81 `z`; `μ ⊗ (counting)` maps to `ρ_μ ⊗ I/3`; marginalizing site 2 maps to `tr₂`, i.e. `tr₂ A(z₁, z₂) = A(z₁)` for all `z` |
| OD-COMP | `OD-COMP-STABILIZER` | At `N = 2`, all 40 Lagrangian subspaces `L` of `(ℤ/3)⁴` are enumerated. The uniform law on each maps to a rank-one projector. The image is entangled (reduced state `I/3`) exactly when `L` is not a product of two lines, and a product state exactly when it is |
| OD-HOLD | `OD-HOLD-STROBOSCOPIC` | The covariance unitary of the free leap `J: (x, ξ) ↦ (−ξ, x)` satisfies `U A(z) U† = A(Jz)` for all `z`, `U⁴ ∝ I` and `U² ∝ Π`. Lüders registration is idempotent. One free tick after registration does not return the registered value with certainty; four free ticks do |

The covariance unitary is `U_S ∝ Σ_z D(Sz) D(z)†`. It is checked nonzero, unitary up to a positive rational scale, and
covariant.

## 4. Controls

| id | content |
| --- | --- |
| K0 | standard library only; exact `ℚ(ω)` arithmetic; two runs byte-identical |
| K-weyl | `D(z)` unitary; `tr D(z) = 3 δ_{z,0}`; `D(z) D(w) = ω^{2⁻¹⟨z,w⟩} D(z + w)` for all `z, w`, with `⟨z,w⟩ = x ξ' − ξ x'` |
| K-pp | `A(z)` Hermitian, `tr A(z) = 1`, `tr A(z) A(w) = 3 δ`, `Σ_z A(z) = 3I` |
| K-psd | Two PSD tests, `LDL*` with zero-pivot handling and the signs of the characteristic polynomial's elementary symmetric functions, agree on every matrix tested. They accept `I` and a rank-one projector, and reject `diag(1, −1)` and `A(0)` |
| K-choi | Choi of the identity PSD of rank 1; of the transpose not PSD; of full dephasing PSD |
| K-AGL | An independent enumeration of `AGL(2,3)` and `ASL(2,3)`, from matrices and translations, gives 432 and 216 maps. They equal the sets found by OD-REV's sweep |
| K-cov-neg | A covariance check against a wrong target, `A(Jz + (1,0))` in place of `A(Jz)`, fails |
| K-psd-neg | The PSD test rejects the operator of a non-uniform registered prior and accepts the uniform one, by both methods |

A token printed over a failed control is void, and the study then prints `VOID`.

## 5. Reading

When all seven tokens print, the study prints `OD-READ`:

> Under E1's dictionary at `q = 3`:
> - OI's reversible operations that act on the register as quantum operations are exactly the affine symplectic ones.
> - OI's point-configuration preparations and non-disturbing readouts have no physical image.
> - Registered preparations are physical exactly with the counting measure on the hidden half, and registered readouts
>   exactly with the hidden half re-randomized, which is Lüders back-action.
> - Uniform attachment, discard and site composition transfer exactly.

Otherwise the study prints the tokens that hold and `OD-NOT-READ`.

## 6. Non-claims fixed in advance

- **The dictionary is E1's posit.** Positivity is judged in the register's quantum description, which E1 assumes. The
  study therefore says what E1-L must supply or replace. It does not show that OI forces quantum mechanics.
- **Scope.** Only `q = 3`, at `N ≤ 2`. For general odd `q` the literature is cited, not proved here.
- **Nothing is said about `q = 2`.**
- **Bell violation is not tested.** Wigner-positive states with stabilizer operations admit a noncontextual model
  [L: Veitch et al. 2012; Howard et al. 2014]. Violation needs operations outside the dictionary's image, which in
  E1-L means `T`'s sub-period flows.
- **No adoption.** No operational principle is adopted or proposed for adoption.
