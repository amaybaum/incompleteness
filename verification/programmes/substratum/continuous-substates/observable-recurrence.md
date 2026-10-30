# SUBSTATE-1: observable-level recurrence without a finite carrier

**Status: research-only; the all-`L` Fourier proof below is on paper,
not Lean-checked. Separate finite-visible set, stochastic-inverse and
conditional ENNReal measured-return lemmas were kernel-built on
`a02e197d`. The full physical bridge remains independently unreviewed.** Related to #1007 and draft #1009. This is a statement about
measure-preserving dynamics and its observations, **not** a proof of OI's full
substratum reconstruction, gauge dynamics, or quantum equivalence.

## A finite observable factor suffices for the recurrence obstruction

Let `(X, Σ, μ)` be a probability space, `T: X → X` an invertible
measure-preserving map, and `π: X → V` a measurable finite-valued
observation. Discard null cells so that each `C_a = π⁻¹(a)`, `a ∈ V`,
has positive measure. For every integer `t ≥ 0` define the **rooted**
row-stochastic transition

`Γ_t(a,b) = μ(C_a ∩ T⁻ᵗ(C_b)) / μ(C_a)`.

This is a family of transitions **from the original preparation**, not a
claim that the observed process is Markovian.

**Lemma 1 (exact return of a finite observable).** For any `L > 0`,

`Γ_L = I ⇔ π(T^L x) = π(x)` for μ-almost every `x`.

*Proof.* All terms are nonnegative. `Γ_L = I` means every off-diagonal
intersection `C_a ∩ T⁻ᴸ(C_b)` for `a ≠ b` has measure zero. The
finite union of these intersections is exactly the set where
`π(T^L x) ≠ π(x)`, modulo null cells. Conversely, if this set is
null, each diagonal conditional probability is one and every
off-diagonal probability is zero. □

In particular, `π ∘ T^L = π` almost everywhere is **sufficient** for the
recurrence step in Main §2.3 even if `X` is infinite. It is not
automatic for infinite measure-preserving carriers.

**Lemma 2 (P-indivisibility from a finite visible return).** Suppose
`|V| ≥ 2`, `Γ_L = I`, and there is a time `0 < s < L` for which
`Γ_s` is not a permutation matrix. Then there is **no**
row-stochastic `Π_{s,L}` with `Γ_L = Γ_s Π_{s,L}`. Hence this
rooted family is not P-divisible on `{0, …, L}`.

*Proof.* If square row-stochastic matrices `A,B` satisfy `AB = I`,
then row `i` of `A` writes the vertex `e_i` of the probability
simplex as a convex combination of rows of `B`. Every row of `B`
receiving nonzero weight must therefore equal `e_i`. The supports of
the `|V|` rows of `A` are nonempty and disjoint subsets of the
`|V|` column indices. Consequently each support is a singleton and
`A` is a permutation matrix. Apply this to `A = Γ_s` and
`B = Π_{s,L}`. □

**Boundaries.** Lemma 1 specifies exact return at a common time,
almost everywhere. It is stronger than Poincaré recurrence; it does not
require pointwise return of the entire hidden state. Lemma 2 is a
**sufficient** obstruction, not an equivalence to all forms of memory.
Neither lemma establishes the OI readback route, `S ⇔ D ⇔ Q_fb`,
reconstruction of gauge groups, the area law, or exact operational QM.

## Application: every ring size L ≥ 3 for the free 1-D wave map

Take `F = [[S + S⁻¹, -I], [I, 0]]` on the integral
state `(u_t,u_{t-1})` of an `L`-site periodic ring, where `S`
is the spatial cyclic shift. The same integer matrix induces a
Haar-preserving automorphism of `X = (R/Z)^(2L)`.

**Proposition 3 (parabolic-mode cancellation, all L ≥ 3).**
Set `M=F^L-I`. Then `M ≠ 0`, `M²=0`, and the image of `M`
has only the spatially uniform Fourier mode and, for even `L`,
the alternating Fourier mode. Therefore, with the readout row
`v_r = u(0)-u(r)`, one has `v_2 M=0` for all `L ≥ 3`,
and `v_1 M=0` for odd `L`. Thus `v_r F^{mL}=v_r`
for every integer `m ≥ 1` in the stated cases, and any
finite partition of the corresponding `v_r · x mod 1` has exact
visible return at time `L` for **every** `x`.

*Proof.* Complexify and diagonalize the cyclic shift `S`. For a
Fourier eigenvalue `z` with `z^L=1`, the time-update block is
`B_z=[[z+z⁻¹,-1],[1,0]]`, with eigenvalues `z,z⁻¹`.
When `z ≠ ±1` these eigenvalues are distinct, so
`B_z^L=I`. For `z=±1`, write `B_z=zI+N_z`
with `N_z²=0` and `N_z ≠ 0`. Since `z^L=1`,
`B_z^L=I+L z^(L-1)N_z`. These are precisely the
uniform (`z=1`) and, if the ring is even, alternating
(`z=-1`) spatial modes. It follows mode by mode that
`M²=0`, and the `z=1` contribution makes `M ≠ 0`.
The difference `u(0)-u(r)` annihilates the uniform mode,
and it annihilates the alternating mode exactly when `r`
is even. Hence `v_rM=0` for the claimed `r`.
Finally `F^{mL}=(I+M)^m=I+mM`, giving `v_rF^{mL}=v_r`.
The argument is over complexified integer matrices, so the
resulting identities hold exactly over integers and on the torus. □

For the two-cell partition used by `wave_torus_probe.py`, the
time-one map `Γ_1` is the uniform `2 × 2` matrix: the rows
`v_r` and `v_rF` are linearly independent over `Q`
(the former observes only `u_t`, the latter has a nonzero
`u_{t-1}` component). The joint torus homomorphism has
rank two and pushes Haar measure to Haar measure on the
two-torus. Lemmas 1–2 therefore imply P-indivisibility
of these **rooted** families for all `L ≥ 3` (and the
stated `r`), not just the probed sizes 3–10.

For a single-site `v=u(0)`, `vM ≠ 0`; the free wave
map does **not** yield a common return from the same
parabolic-cancellation argument. The current exact probe
checks the stronger non-return statement only for `L=3…10`,
not every ring size.

**Pointwise state recurrence is different.** Here
`F^{mL}x=x+mMx` on the torus. For each fixed `x`, set
`y=Mx`. Compactness of the torus (the pigeonhole
argument for multiples of a fixed `y`) yields arbitrarily
large positive `m` with `my` arbitrarily close to zero.
Thus **every orbit of this specific unipotent torus map**
returns arbitrarily close to its initial state along a
point-dependent sequence. This is a separate proof:
Poincaré's measure-theoretic theorem alone guarantees
recurrence only almost everywhere, and neither statement
implies a common exact return time for the single-site
observation.

## What the p-adic factor argument does and does not show

For `X=Z_p^n` and `F ∈ GL_n(Z_p)`, the reduction map
`ρ_k: Z_p^n → (Z/p^kZ)^n` obeys
`ρ_k(Fx)=(F mod p^k)ρ_k(x)`.
Consequently a readout factoring through `ρ_k`
depends only on the first `k` p-adic digits; every
visible word returns at the finite order of `F mod p^k`.
The higher digits are **invisible to that readout under
this class of congruence-compatible dynamics**.

This does not prove that *all* p-adic states or all possible
observation maps are physically inert, nor that
`Z_p` alone supplies a connected Lie gauge group.
Other interactions, observables and gauge constructions
remain untested. A no-go claim outside this class is
not authorized.

## Independence and literature controls

- The finite-partition return criterion is a direct
  measure-theoretic identity and needs no new physical
  premise. Standard Poincaré recurrence yields almost-everywhere,
  not a synchronized return; see M. Hochman, *Notes on
  Ergodic Theory* (2017), §2.2:
  https://math.huji.ac.il/~mhochman/courses/ergodic-theory-2017/notes.pdf
- Haar-pushforward and the Fourier calculation are
  mathematical arguments for this **free** system only.
- In Wilson lattice gauge theory, continuous **link**
  group values, Haar measure and gauge-invariant plaquette
  actions are distinct ingredients. Introducing a compact
  continuum alone does not select an action; for a
  basic treatment see *Lectures on QCD Foundations*,
  https://www.phenix.bnl.gov/WWW/publish/elke/EIC/BOOKs/Lectures-on-QCD.Foundations.pdf

**Still open:** the `d=3` carrier, an actual gauge-coupled
update, the exact OI readback/operational control list
from #1007, and a hard-to-vary independent Wilson/
Yang–Mills payoff. Do not promote this note to a
manuscript theorem before independent review.
