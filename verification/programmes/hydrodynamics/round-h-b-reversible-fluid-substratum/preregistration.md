# Hydrodynamics round H-B — a reversible streaming-and-collision substratum: CONTROL PLANE

Owner-called, under `../PROGRAMME.md` §6 (the second round of the programme, round H-B). This file is
the whole of round H-B's control plane and is merged **alone**, before any execution object exists.
The round is **constructive**: it freezes one candidate reversible substratum of
streaming-and-collision type — a lattice gas on a finite periodic lattice over a finite alphabet,
instantiating the kernel's `Substratum` interface unmodified, with exactly conserved mass and
momentum built in — and asks of it, in order, the four questions round H-A asked of the wave
representative: additivity and closure, exact conservation under the appropriate invariance
principle, isotropy of the lowest-order stencil tensors, and exact closure of a coarse variable.
Each target is reported as **HD**, **HC**, **HI** or **HO** in the programme's taxonomy, or
**UNDECIDED** with the obstruction.

**Blob identity is authoritative.** The execution guard pins this file by content.

**Parallel-track separation.** This round runs on its own branch from `main` at
`aa4ac3a621a4967c1075fd129d49f88c724eecd0`. It neither consumes nor produces evidence for the
OI → QM chain (Track B, Track I), for Bell, or for gravity; the programme's control 1 applies in
full. It is an independent constructive physics programme and does not block the OI → QM chain.

## Start state

| | |
| --- | --- |
| Merged `main` | `aa4ac3a621a4967c1075fd129d49f88c724eecd0` (PR #599) |
| The programme roadmap | `../PROGRAMME.md`, blob `07aaa6c4d96a1ad613d0ff64adbb9f8745f0856f` — consumed as the taxonomy and the round list; its §8 one-line state and its status-base line are not edited by this PR |
| Round H-A, the frozen control plane | `../round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` — the format model, the `q`-gauge test, the `H2b` stencil finding, the `H3a` closure diagnostic |
| Round H-A, the result | `../round-h-a-source-audit/result.md`, blob `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` — every target landed at evidence level 2; H-B named alive |
| Round H-A's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean`, blob `fd5f54d8cbba4f68b67335c111d39a2add0c642f` — `CoarseCloses`, `coarse_evolution_additive`, `totalSum`, `axisMoment4`, `axisMoment4_eq`, `axisMoment4_quartic`, `axisMoment4_not_isotropic`, `SymInvariantQuartic`, `IsotropicQuartic`, `blockSum` |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `Substratum` (`ι`, `V`, `R : Rule ι V`, `Conf := ι → V × V`, `φ := leapEquiv R.F`), `shiftBy`, `A1`, `A2`, `A3`, `A4Exact`, `A4`, `A5`, `a2_every_substratum`, `a1_of_finite`, `a3_of_fintype`, `a4_of_exact`; and the wave instance `waveSubstratum`, `dir`, `nbrs` for comparison only |
| The phase-space update | `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean`, blob `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` — `leap F x i = ((x i).2, F (curOf x) i − (x i).1)`, `leapEquiv`, `curOf`, `prevOf` |
| The rule interface | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` — `Rule` (`F`, `N`, `infl`, `dep`, `mem_infl`) |
| The isotropy layer | `verification/lean-mathlib/OIBridge/CubicIsotropy.lean`, blob `c1918dc0c4ffaf1547f1918e6665f7c086233796` — `IsSign`, `OhInvariant`, `quadratic_isotropic`, `quartic_ohInvariant`, `quartic_not_isotropic` |
| The manuscript's rule and gauge principles | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — §2.7 "The alphabet as gauge freedom"; §4.1's rule and the amplitude-scale-gauge lemma |
| The substratum axioms and their hypothesis dependencies | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — A1–A6; the remark that A5 "is equivalent to amplitude-scale gauge invariance … so nonlinear wave equations on finite lattices are the separate class one obtains exactly when that gauge principle is dropped"; Theorem 24 (ii) |
| The chronology guard, archive mode | `verification/lean/edge_rigidity_probe.py`, blob `1c76095343d47832ec75a66e2d34bfa3d18d38bd` — `_rbr_strong_ancestry`, `_rbr_archive_ancestry`, `R7-HYA` |

## The candidate, FROZEN

One candidate, and only this one. Its `Substratum` instance is `hexSubstratum L` with `[NeZero L]`.

**The lattice.** Sites `ι = Fin 2 → ZMod L`, the `L × L` periodic lattice, read in the **hexagonal
basis** `a₁ = (1, 0)`, `a₂ = (1/2, √3/2)` of `ℝ²`: the site `(a, b)` sits at `a·a₁ + b·a₂`. The
translation group is `ι` itself; nothing about the group changes with the basis. The six lattice
directions, in lattice coordinates and as integers, are

```
c₀ = (1, 0),  c₁ = (0, 1),  c₂ = (−1, 1),  c₃ = (−1, 0),  c₄ = (0, −1),  c₅ = (1, −1),
```

with `c_{k+3} = −c_k`, and their images `a·a₁ + b·a₂` are the six unit vectors at angles `kπ/3`.
This is the triangular lattice with its six nearest neighbours: the least stencil in any dimension
whose fourth moment is rotation-isotropic (recorded analysis below), which is the property H-A's
`H2b` showed the axis stencil lacks.

**The alphabet.** `V = Fin 6 → ZMod 2`: at each site, one Boolean occupation number per channel
(direction) `k`, at most one particle per channel. `V` is an additive group under channel-wise
addition mod 2 (exclusive or), which is all the `Substratum` structure requires of it. **There is no
free alphabet-size parameter**: the alphabet is fixed by the construction, and this is recorded
here because it changes the shape of the `H1`-type question (below).

**The streaming step.** `hexStream : (ι → V) ≃ (ι → V)`, `(stream c) i k = c (i − c_k) k`: the
particle in channel `k` moves one lattice step along `c_k`. Its inverse is `(unstream c) i k =
c (i + c_k) k`. Streaming is the permutation `(i, k) ↦ (i + c_k, k)` of site–channel pairs; it
moves particles and changes no channel index.

**The collision rule.** `hexCollide : Equiv.Perm V`, on-site, the identity on 59 of the 64 local
states and, on the five remaining ones,

- the **head-on** two-body states `{0, 3} ↦ {1, 4} ↦ {2, 5} ↦ {0, 3}` (a 3-cycle: each head-on
  pair rotates by `+60°`);
- the **three-body** symmetric states `{0, 2, 4} ↔ {1, 3, 5}` (a transposition).

Every moved state has mass `2` or `3` and momentum `0`, so the collision preserves local mass and
local momentum on all 64 states. The permutation has order `6`. **It is chiral**: a `+60°` rotation
of head-on pairs is covariant under the `60°` lattice rotation and not under reflection, and this
is not a defect of the choice but a property of the class — a nontrivial permutation of the three
head-on states that commutes with the `60°` rotation (which cycles them) is a power of that
3-cycle, so **no deterministic, reversible, rotation-covariant, nontrivial head-on collision is an
involution**, and none is reflection-covariant. The literature's alternatives (random choice, or
alternation in time) are not autonomous rules and are not available inside the `Rule` interface;
the round records the chirality as a named property (hazard 6) and claims nothing about parity.

**The gas.** `hexGas : (ι → V) ≃ (ι → V)`, `Φ := hexStream ∘ (sitewise hexCollide)` — collide,
then stream. `Φ` is a bijection because both factors are; `Φ⁻¹ = (sitewise hexCollide⁻¹) ∘ unstream`
is local of the same range.

**The substratum rule, and why the dynamics is reversible.** The `Substratum` structure fixes the
dynamics as the kernel's second-order phase-space map `leap F : (p, c) ↦ (c, F c − p)`, which is a
bijection for **every** `F` (`a2_every_substratum`); the interface is consumed unmodified, so the
candidate must be a second-order rule. The round places the first-order gas inside it by
```
F c := Φ c + Φ⁻¹ c        (addition in V, i.e. channel-wise exclusive or),
```
`hexSubstratum L := { ι := Fin 2 → ZMod L, V := Fin 6 → ZMod 2, R := { F, N i := {i + c_k}, infl := N, … } }`.
Then on the **graph sector** `Γ := { x : Conf | prevOf x = Φ⁻¹ (curOf x) }` one has
`F (curOf x) − prevOf x = Φ (curOf x) + Φ⁻¹ (curOf x) − Φ⁻¹ (curOf x) = Φ (curOf x)`, so `leap F`
maps `Γ` to `Γ` and acts on it as `Φ`: **the sector is invariant and the sector dynamics is exactly
the streaming-and-collision gas.** Reversibility therefore holds at two levels, both exact: the
phase-space map is a bijection by the interface's own theorem, and the gas it carries on `Γ` is a
bijection because streaming is a permutation of site–channel pairs and the collision is a
permutation of the local states with an explicit inverse. **Outside `Γ` the dynamics is not the gas**
and conserves nothing this round names (recorded analysis below); every conservation statement of
this round is a statement on `Γ`, and the round says so wherever it states one.

**The conserved fields, FROZEN.** For a finite set of sites `A`, a channel weight `w : Fin 6 → ℤ`
and a slice `c : ι → V`, the channel-weighted total
```
hexSum A w c := Σ_{i ∈ A} Σ_k (c i k).val · w k ∈ ℤ,
```
the integer lift of the Boolean occupations. **Mass** is `M := hexSum univ 1`, **momentum** in
lattice coordinates is `P_j := hexSum univ (k ↦ (c_k)_j)`, `j ∈ {1, 2}`; the Euclidean momentum is
the fixed linear image `P₁ a₁ + P₂ a₂`, so exact conservation of `(P₁, P₂)` is exact conservation
of it. Block charges are `hexSum β w` for a block `β` of the partition into `b × b` squares (in
lattice coordinates, `b ∣ L`, the block of `i` being `k ↦ ⌊(i k).val / b⌋`, H-A's convention).

**What the candidate is, and is not, with respect to A1–A6.** It is finite (A1), deterministic and
reversible (A2), of bounded degree `6` (A3), and translation-covariant in the exact form (A4Exact),
each to be proved (`HB0-a`). **It is not additive: A5 fails by construction** (`HB0-b`). By
[Substratum, the hypothesis-dependency remark] A5 is equivalent to amplitude-scale gauge invariance,
and nonlinear rules on finite lattices are "the separate class one obtains exactly when that gauge
principle is dropped": **the candidate lies in that separate class**, and the round says so in
terms. Whether A5 is a requirement of "OI-compatible" — whether the class obtained by dropping the
amplitude-scale gauge principle is admissible as an OI substratum — is an **owner decision this
round sets up and does not make**; the round reports the candidate's A-profile and nothing about
its admissibility. A6 is a GAP on its own branch and is not touched. The candidate is
two-dimensional; nothing here is a statement about the manuscripts' `d = 3` substratum (hazard 1).

## Why this round exists, and what it can and cannot decide

H-A's lesson is that the wave representative is probably the wrong place to force fluid behaviour:
its additivity forbids an advective term on `ZMod q`-linear coarse variables (`H0`), its only
total-sum conservation law is not `q`-gauge invariant (`H1`), and its axis stencil is anisotropic
at fourth order (`H2b`). Each of those is a property the streaming-and-collision class does not
share by construction — collisions are nonlinear, mass and momentum are conserved by every local
collision, and the hexagonal stencil is fourth-order isotropic — and the programme's H-B asks
whether such a model exists **inside the kernel's `Substratum` interface** with those properties
**proved**, not assumed from the literature. The round freezes one candidate and asks H-A's four
questions of it, so that the two rounds' answers are comparable target by target.

What the round can decide: whether the frozen candidate instantiates the interface with A1–A4 and
without A5; whether its sector carries the gas; whether mass and momentum are exactly conserved on
every configuration for every `L`, and whether they are the **only** site-independent
channel-weighted invariants; whether the stencil's fourth moment is isotropic and its sixth is not;
whether one frozen block variable closes exactly.

What it cannot decide, and does not claim to: whether the candidate has a hydrodynamic limit of any
kind (H-C); whether a statistical closure, local equilibrium or mixing statement holds at any scale
(H3 beyond the exact diagnostic); whether an advective term is present in any coarse description —
non-additivity is necessary for one and not sufficient; whether the candidate carries additional
invariants outside the frozen class (the literature reports staggered invariants for gases of this
type, and the round neither confirms nor excludes them for the candidate); anything about `d = 3`;
anything about the OI → QM chain.

## Recorded analysis — the one permitted pre-execution object

Every computation below was carried out by hand and by an exact script (rational and `√3`
arithmetic, exhaustive enumeration where finite) **before this file was written**, and is recorded
here so that no execution-specific artifact precedes the freeze. The kernel re-derives what it
claims; nothing here is evidence at any level above "recorded analysis".

1. **The collision.** `hexCollide` is a bijection of the 64 states, moving exactly five; it
   preserves mass and momentum on all 64; its order is `6`. It commutes with the channel rotation
   `k ↦ k + 1` and not with the channel reflection `k ↦ −k`. There is **no** nontrivial involution
   of the three head-on states commuting with the 3-cycle the rotation induces on them.
2. **The collision invariants.** For `w : Fin 6 → ℤ`, `Σ_k w_k n_k` is preserved by `hexCollide` on
   every local state **iff**
   ```
   w₀ + w₃ = w₁ + w₄,   w₁ + w₄ = w₂ + w₅,   w₀ + w₂ + w₄ = w₁ + w₃ + w₅,
   ```
   three independent conditions (the 3-cycle supplies two, the transposition one; the fixed states
   supply none). The solution lattice has rank `3`; in the free coordinates `(w₀, w₁, w₂)` it is
   all of `ℤ³`, and the three weights `1`, `d₁ := (k ↦ (c_k)₁) = (1, 0, −1, −1, 0, 1)`,
   `d₂ := (k ↦ (c_k)₂) = (0, 1, 1, 0, −1, −1)` have coordinate determinant `1`. **So the
   site-independent channel-weighted totals conserved by the collision are exactly the `ℤ`-span of
   mass and the two momentum components** — in closed form, `w = a·1 + b₁·d₁ + b₂·d₂` with
   `a = w₀ − w₁ + w₂`, `b₁ = w₂ − w₁`, `b₂ = 2w₁ − w₀ − w₂`. Streaming preserves every
   channel-weighted total whatever `w`, so the same characterizes the totals conserved by `Φ` on
   every configuration.
3. **The sector.** On `L = 1, …, 6` and random configurations, `Φ⁻¹ ∘ Φ = id`, `Φ ∘ Φ⁻¹ = id`,
   `M ∘ Φ = M`, `P ∘ Φ = P`, and `leap F` carries `(Φ⁻¹ c, c)` to `(c, Φ c)`, as the algebra says.
   **Off the sector**: with `prevOf x = 0` and `curOf x` a single particle in channel `0` at the
   origin, the mass after one step is `0` at `L ∈ {1, 2}` (the two images cancel on one site) and
   `2` at `L ≥ 3`; in every case `≠ 1`. Mass is not conserved by `leap F` off `Γ`, for every `L ≥ 1`.
4. **Non-additivity, the witness.** `c` = one particle in channel `0` at the origin, `c'` = one in
   channel `3` at the origin. `F (c + c')` has a particle in channel `1` at the site `c₁` (from
   `Φ`: the head-on pair collides to `{1, 4}` and streams); `F c + F c'` has no particle in channel
   `1` anywhere (single particles do not collide, and channels `0`, `3` are all that occur). Valid
   for every `L ≥ 1`, checked at `L = 1, …, 6`.
5. **The stencil moments**, in the Euclidean embedding `u_k := (c_k)₁ a₁ + (c_k)₂ a₂ =
   (cos kπ/3, sin kπ/3)`: second moment `Σ_k (u_k)_a (u_k)_b = 3 δ_{ab}`; fourth moment
   `Σ_k (u_k)_a (u_k)_b (u_k)_c (u_k)_e = (3/4)(δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc})`
   exactly (`T₁₁₁₁ = 9/4`, `T₁₁₂₂ = 3/4`, `T₁₁₁₂ = 0`), so its quartic form is `(9/4)(k₁² + k₂²)²`;
   **sixth moment not isotropic**: `T₁₁₁₁₁₁ = 33/16`, `T₁₁₁₁₂₂ = 3/16`, ratio `11` where an
   isotropic rank-6 tensor has `5`. For comparison, H-A's `axisMoment4 2 = 2·[a = b = c = e]`
   (`axisMoment4_eq`, stated for every `d`) has quartic form `2(k₁⁴ + k₂⁴)`, equal to `2` at
   `(1, 0)` and `1` at `(1/√2, 1/√2)`, two vectors of the same length.
6. **Rotation covariance.** With the `60°` lattice rotation `ρ (a, b) := (−b, a + b)` (which
   carries `c_k` to `c_{k+1}`) acting on configurations by `(ρ·c) (ρ i) (k + 1) := c i k`,
   `Φ ∘ ρ = ρ ∘ Φ` on `L = 3, 4, 5` and random configurations; with the reflection
   `(a, b) ↦ (a + b, −b)`, `k ↦ −k`, it does not commute. Mass is `ρ`-invariant and momentum
   `ρ`-covariant by inspection.
7. **The block-charge witness** (`HB3-a`), found by exhaustive search over configurations of mass
   `≤ 3`, at `L = 4`, `b = 2` (four `2 × 2` blocks), on the sector:
   - `c`: a particle in channel `0` at `(0, 0)` and a particle in channel `3` at `(0, 1)`;
   - `c'`: the head-on pair `{0, 3}` at `(0, 0)`.
   At `t`: both have block charges `(M, P₁, P₂) = (2, 0, 0)` on block `(0, 0)` and `0` elsewhere.
   At `t − 1`: `Φ⁻¹ c` = channel `3` at `(1, 1)`, channel `0` at `(3, 0)`; `Φ⁻¹ c'` = channel `3` at
   `(1, 0)`, channel `0` at `(3, 0)`; both give `(1, −1, 0)` on block `(0, 0)`, `(1, 1, 0)` on block
   `(1, 0)`, `0` elsewhere. At `t + 1`: `Φ c` = channel `0` at `(1, 0)`, channel `3` at `(3, 1)`,
   block charges `(1, 1, 0)` on `(0, 0)` and `(1, −1, 0)` on `(1, 0)`; `Φ c'` = channel `1` at
   `(0, 1)`, channel `4` at `(0, 3)`, block charges `(1, 0, 1)` on `(0, 0)` and `(1, 0, −1)` on
   `(0, 1)`. **Equal coarse two-time states, different coarse states at `t + 1`.** The search found
   no witness at `L = 2, b = 1` or `L = 3, b = 1` among configurations of mass `≤ 3`; that is a
   bounded search and **not** a closure control, and the round claims nothing about those sizes.

## Targets, FROZEN

Every target is stated for `hexSubstratum L` with `[NeZero L]`, on `Γ` wherever a trajectory is
involved, `L ≥ 1` unless a witness pins a value.

### `HB0` — additivity, and the sector (the `H0`-type question)

**`HB0-a` (kernel).** `hexSubstratum L` satisfies `A1`, `A2`, `A3 6` and `A4Exact`: `A1` through
`a1_of_finite`; `A2` through `a2_every_substratum`; `A3 6` because `N i` is the image of `Fin 6`;
`A4Exact` because streaming and the sitewise collision each commute with every `shiftBy v`, hence
so do `Φ`, `Φ⁻¹` and their sum. **Prediction: positive, full strength.**

**`HB0-b` (kernel).** `hexSubstratum L` fails `A5`: `F (c + c') ≠ F c + F c'` for the witness of
recorded item 4, pinned by equation in the statement, at channel `1` of the site `c₁`, for every
`L ≥ 1`. **Prediction: positive (the failure), full strength.**

**`HB0-c` (kernel).** The sector: for every `x` with `prevOf x = Φ⁻¹ (curOf x)`,
`prevOf (leap F x) = Φ⁻¹ (curOf (leap F x))` and `curOf (leap F x) = Φ (curOf x)`; and the
countercontrol of recorded item 3: for `x` with `prevOf x = 0` and `curOf x` a single particle in
channel `0` at the origin, `M (curOf (leap F x)) ≠ M (curOf x)`, for every `L ≥ 1` (the value being
`0` for `L ∈ {1, 2}` and `2` otherwise; the statement is the inequality). **Prediction: positive,
full strength**, both parts.

**Reported status for the advection obligation: HO for the candidate.** H-A's linearity gate
(`coarse_evolution_additive`, `coarseCloses_additive_on_range`) has `A5` as its hypothesis and does
not apply to the candidate; that lifts H-A's `H0` obstruction **for this candidate** and establishes
nothing positive — non-additivity is necessary for an advective term and not sufficient, and no
coarse description carrying one is exhibited or claimed. The round does not label the advection
obligation HD, HC or HI.

### `HB1` — exact conservation, and the appropriate invariance principle (the `H1`-type question)

**`HB1-a` (kernel).** For every `w : Fin 6 → ℤ` and every slice `c`,
`hexSum univ w (hexStream c) = hexSum univ w c`: streaming permutes site–channel pairs and
preserves the channel index. **Prediction: positive, full strength.**

**`HB1-b` (kernel).** For every `w`:
`(∀ c, hexSum univ w (sitewise hexCollide c) = hexSum univ w c)` **iff**
`w₀ + w₃ = w₁ + w₄ ∧ w₁ + w₄ = w₂ + w₅ ∧ w₀ + w₂ + w₄ = w₁ + w₃ + w₅`. Forward: the three
one-site configurations `{0, 3}`, `{1, 4}`, `{0, 2, 4}` at the origin, each pinned by equation.
Backward: the identity holds at each site for each of the 64 local states, 59 of them trivially.
**Prediction: positive, full strength; high at kernel level** (a finite check over the five moved
states, or over all 64). **Fallback, frozen now:** if the 64-state check does not close at level 2,
the backward direction is stated for the five moved states by case analysis and the reduction is
proved; if that too is out of reach, `HB1-b` is UNDECIDED with the obstruction named, and `HB1-c`
is stated with the three conditions as an explicit hypothesis.

**`HB1-b′` (kernel).** The three conditions hold **iff** `∃ a b₁ b₂ : ℤ, w = a·1 + b₁·d₁ + b₂·d₂`,
with `d₁`, `d₂` the two coordinate rows of `hexDir`; the witnesses are the closed forms of recorded
item 2. **Prediction: positive, high strength** (integer linear algebra; the risk is in the
bookkeeping, not the mathematics).

**`HB1-c` (kernel).** Consequently, for every `L`, every configuration `c` and every `w` satisfying
the three conditions — in particular for mass and both momentum components —
`hexSum univ w (Φ c) = hexSum univ w c`; and along every trajectory in `Γ`,
`hexSum univ w (curOf (leap F x)) = hexSum univ w (curOf x)`. **Prediction: positive, full
strength.** **The reading, frozen:** mass and momentum are exactly conserved by the gas, on every
configuration, for every `L`, with no parameter chosen; and within the class of site-independent
channel-weighted totals **they are the only conserved quantities**, so the candidate carries no
spurious invariant of that shape. Staggered, site-dependent or time-dependent invariants are
outside the class and are **not adjudicated** (hazard 4).

**The invariance principle, FROZEN.** H-A's `H1` test asked whether a candidate conservation law
survives the `q`-gauge principle of [SM §2.7]; the wave representative's did not. **That test has no
analogue here**: the candidate carries no free alphabet parameter — its alphabet is Boolean
occupation by construction — so there is no `q` to vary and no `q` to choose, and the round does not
manufacture one. Whether a fixed Boolean alphabet is admissible under [SM §2.7]'s alphabet-as-gauge
reading is an owner-level question this round records and does not decide (hazard 3). The
principle the round **does** apply is the one a physical conservation law must satisfy on a finite
periodic substratum: **exactness on every configuration, for every lattice size, with no parameter
tuned** (`HB1-c` in terms), together with **translation invariance** of the conserved fields
(`HB1-d`) and, conditionally, **covariance under the lattice's own point symmetry** (`HB1-e`).

**`HB1-d` (kernel).** `hexSum univ w (shiftBy v c) = hexSum univ w c` for every `v`, `w`, `c`.
**Prediction: positive, full strength** (a reindexing of the site sum).

**`HB1-e` (kernel, conditional on budget slot 8).** With `hexRot` the `60°` lattice rotation of
recorded item 6: `Φ (hexRot c) = hexRot (Φ c)` for every `c`; `M (hexRot c) = M c`; and
`(P₁, P₂) (hexRot c) = ρ (P₁, P₂) (c)` with `ρ (a, b) = (−b, a + b)`. **Prediction: positive, high
strength; medium at kernel level** (definitional overhead of the action, and a 64-state check for
the collision's covariance). **Fallback, frozen now:** if not reached at level 2, `HB1-e` is
reported at evidence level 3 from a probe in the execution PR with the label stated, or UNDECIDED;
`HB1-a`–`HB1-d` do not depend on it.

**Reported status for H1: HD for mass and momentum, for the candidate, on the sector** — exact
conservation is a theorem about the microscopic dynamics, as the programme's H1 requires — **with
the uniqueness within the frozen class stated and the outside of the class HO.**

### `HB2` — the lowest-order stencil tensors (the `H2`-type question)

**`HB2-a` (kernel).** The second moment of the embedded stencil is `3 δ_{ab}` (stated inline over
the six unit vectors; no definition). **Prediction: positive, full strength.** This is the order
Corollary 1a's `quadratic_isotropic` speaks to for the cubic case, and it is consumed for comparison
only.

**`HB2-b` (kernel).** `hexMoment4 a b c e = (3/4)(δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc})`, all
sixteen entries; consequently its quartic form is `(9/4)(Σ_i k_i²)²` and is a function of `|k|²`:
for all `k, k' : Fin 2 → ℝ` with `Σ k_i² = Σ k'_i²` the forms agree (the notion `IsotropicQuartic`
uses, stated inline for `Fin 2`). **Prediction: positive, full strength**; the arithmetic is
`(√3/2)² = 3/4`, `(√3/2)⁴ = 9/16`, and the kernel has `Real.sq_sqrt`.

**`HB2-c` (kernel, the comparison).** `axisMoment4 2 = 2·[a = b = c = e]` by H-A's
`axisMoment4_eq`; its quartic form `2(k₁⁴ + k₂⁴)` takes the value `2` at `(1, 0)` and `1` at
`(1/√2, 1/√2)`, two vectors of equal length, so the square four-velocity stencil is **not**
fourth-order isotropic where the hexagonal six-velocity stencil **is**. H-A's `quartic_not_isotropic`
and `axisMoment4_not_isotropic` are the `d = 3` statement of the same failure and are cited, not
re-proved. **Prediction: positive, full strength.**

**`HB2-d` (kernel, the bound).** The sixth moment is not isotropic: stated inline,
`Σ_k (u_k)₁⁶ = 33/16` and `Σ_k (u_k)₁⁴ (u_k)₂² = 3/16`, whereas a rotation-isotropic fully
symmetric rank-6 tensor has `T₁₁₁₁₁₁ = 5 T₁₁₁₁₂₂`. **Prediction: positive (the failure), full
strength.** This bounds `HB2-b`: fourth-order isotropy holds, while isotropy already fails at
sixth order; **no claim is made about higher orders** — the round proves the fourth and the sixth
moment and classifies no other even order. Fourth order is the order the Navier–Stokes stress
expansion needs, and beyond it (Burnett-level) the round says nothing.

**Reported status for H2: the stencil's fourth moment is proved isotropic — HD for the stencil
tensor; for the hydrodynamic stress, HC conditional on H5's closure consuming this tensor, otherwise
HO.** As in H-A, whether the bare fourth moment of the stencil is the rank-4 tensor the H5 stress
closure consumes is a bridge this round does **not** build; the round labels the stencil and not
the obligation (hazard 5).

### `HB3` — exact closure of a coarse variable, and the sector measure (the `H3`-type question)

**`HB3-a` (kernel).** The block-charge two-time state does **not** close on the sector: at `L = 4`,
`b = 2`, the two configurations of recorded item 7, pinned by equation in the statement, have equal
block charges `(hexSum β 1, hexSum β d₁, hexSum β d₂)` for every block `β` at `t` and at `t − 1`
(`t − 1` being `Φ⁻¹` of each, as the sector dictates) and different block charges at `t + 1`;
consequently there is no coarse rule `Ψ` with
`hexSum β w (Φ c) = Ψ (blocks at t, blocks at t − 1) β w` for all `c`. **Prediction: positive
(non-closure), full strength; high at kernel level** (evaluation of `Φ` and `Φ⁻¹` on two explicit
sparse configurations over sixteen sites). **Fallback, frozen now:** an error in the witness
arithmetic sends the execution to search for a larger witness, and if none is found the diagnostic
is UNDECIDED; the witness is not replaced by one at a size the recorded search did not cover
without saying so.

**`HB3-b` (kernel).** The charge sectors are invariant: for every `m : ℤ` and `p : ℤ × ℤ`, `Φ` maps
`{c | M c = m ∧ (P₁ c, P₂ c) = p}` bijectively onto itself, so the counting measure on each charge
sector is `Φ`-invariant. Immediate from `HB1-c` and bijectivity. **Prediction: positive, full
strength.** **The reading, frozen:** this is the exact statement that sits beneath any
local-equilibrium hypothesis for the candidate, and it is **all** the round says in that direction:
it licenses no ergodicity, mixing or equidistribution statement within a sector, and if the
candidate carries further invariants (hazard 4) the sectors decompose further and any such
statement would have to be about the finer pieces.

**Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
of a statistical closure at some other scale or in some other variable; no local-equilibrium or
mixing statement is made in either direction. **No timescale is preregistered and none is
asserted**: no relation between a collision time, a block-crossing time and a hydrodynamic time
appears as a hypothesis or as a finding, and the memory diagnostic is exactly what its statement
says — this block variable needs more than its own two-time state to predict its next value.

### The scaling skeleton, inherited

H-A's `H4a` skeleton — lattice spacing as a function of `L`, time step, field normalization and
lift, carrier growth, convergence topology — is inherited unchanged and not repeated as a target.
The result note records only what the candidate fixes of it: the field lift is the integer count
of Boolean occupations (fixed by the construction, one of the five), and the other four remain
unfixed. **Status: HO.** No limit is taken and no PDE is written.

## The preregistered predictions, and their strengths

| target | prediction | strength | status reported | what would falsify it |
| --- | --- | --- | --- | --- |
| `HB0-a` | positive: A1, A2, A3 with degree 6, A4Exact | full | — | an error in the translation-covariance bookkeeping of `hexStream`; would change nothing about the candidate, only the proof |
| `HB0-b` | positive: A5 fails, witness at channel 1 of site `c₁` | full | advection obligation HO for the candidate | an error in the witness; a different witness is then sought — additivity of a rule with a nontrivial collision is not plausible |
| `HB0-c` | positive: `Γ` invariant, `leap F = Φ` on it; mass not conserved off `Γ` | full | — | nothing plausible; the sector identity is one line of group algebra |
| `HB1-a` | positive | full | — | — |
| `HB1-b` | positive: conserved by the collision iff the three conditions | full; **high at kernel level** | — | a slip in the 64-state enumeration; would change the conditions, not the shape of the finding; frozen fallback |
| `HB1-b′` | positive: the conditions iff `w ∈ span_ℤ{1, d₁, d₂}` | high | — | a non-unimodular basis; the span statement would then be over `ℚ` and the round says so |
| `HB1-c` | positive: mass and momentum exactly conserved, every `L`, every `c`, on `Γ`; unique in the class | full | HD for mass and momentum on the sector; HO outside the class | — |
| `HB1-d` | positive: translation invariance | full | — | — |
| `HB1-e` | positive: `60°` rotation covariance of `Φ`, `M` invariant, `P` covariant | high; **medium at kernel level** | — | a wrong rotation action on lattice coordinates; would be repaired, not reinterpreted; frozen level-3 fallback |
| `HB2-a` | positive: second moment `3 δ` | full | — | — |
| `HB2-b` | positive: fourth moment `(3/4)(δδ + δδ + δδ)`, form `(9/4)|k|⁴` | full | HD for the stencil tensor; HC for the stress if H5 consumes it, else HO | — |
| `HB2-c` | positive: `axisMoment4 2` fails where `hexMoment4` does not | full | — | — |
| `HB2-d` | positive: sixth moment not isotropic, ratio 11 vs 5 | full | — | — |
| `HB3-a` | positive: non-closure witness at `L = 4`, `b = 2` | full; **high at kernel level** | HO for H3 | an error in the witness arithmetic — then a larger witness is sought, and if none is found the diagnostic is UNDECIDED |
| `HB3-b` | positive: charge sectors invariant | full | — | — |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction.

**The programme-level reading the round is allowed to give, if all of the above land:** inside the
kernel's `Substratum` interface, consumed unmodified, there is a finite, deterministic, reversible,
translation-covariant rule of degree `6` whose invariant graph sector carries a
streaming-and-collision gas with **exactly conserved mass and momentum on every configuration for
every lattice size**, with **no other site-independent channel-weighted invariant**, and with a
stencil whose fourth moment is **rotation-isotropic** and whose sixth is not; the rule is **not
additive**, so H-A's linearity gate does not apply to it, and H-A's `q`-gauge finding has no
analogue for it because it carries no free alphabet parameter. The candidate is compatible with
A1–A4 as the kernel states them and lies in the class obtained by dropping A5's amplitude-scale
gauge principle; **whether that class is admissible as an OI substratum is an owner decision this
round does not make.** H3 and H4 remain HO; the round says nothing about H5–H7, nothing about
`d = 3`, and nothing about the OI → QM chain. **This reading is conditional on every qualifier
above**, and the execution may not shorten it.

## The post-round programme status, FROZEN

The programme's H-B obligation, as `../PROGRAMME.md` §6 states it, is an **OI-compatible** reversible
fluid witness. This candidate fails A5 by construction. Therefore, **whatever the execution lands,
the following status rule binds the result note and every propagation of it:**

1. **Round H-B is not reported closed by this round**, and the programme's H-B obligation is not
   reported discharged. The round is reported as **one candidate executed**, with its outcomes.
2. **H1 is not reported "HD for OI"**, and no target's status is written with "for OI" or "for the
   OI substratum" attached. Every HD, HC, HI or HO label in this file is a label **for the
   candidate**, in the class it lies in, and the result note writes it that way.
3. What the execution **can** establish, at full strength, is exactly this: **a rigorous reversible
   fluid witness in the A1–A4, ¬A5 class** — finite, deterministic, reversible, translation-covariant,
   of bounded degree, inside the kernel's `Substratum` interface — **with exact mass and momentum
   conservation on every configuration for every lattice size and fourth-order stencil isotropy**,
   proved and not assumed.
4. **Whether the A1–A4, ¬A5 class counts as admissible OI physics is a separate question** — the
   owner decision named above and in hazard 2 — and the result note records it as **open**, in
   those words, in its status section. If the owner later rules the class admissible, the
   programme-level closure of H-B is a **separate owner action** on the record, not a consequence
   the execution draws; if the owner rules it inadmissible, the candidate stands as a witness
   about the class and H-B's obligation stays open.
5. `../PROGRAMME.md` §8's one-line state, when the execution refreshes it, reads "H-B: one
   candidate executed in the A1–A4, ¬A5 class; OI-compatibility of the class open" or a shorter
   sentence with the same three facts, and nothing stronger.

## What none of these outcomes licenses

- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity —
  control 1. No Track B label is imported as evidence here and none of these findings is exported
  there.
- **Nothing here says H-A's wave representative is wrong for any other purpose.** H-A's findings
  stand as stated for that representative and that class of coarse variables; the present candidate
  is a different object, chosen for a different question, and its A5 failure is not a criticism of
  the manuscripts' linear rule, which A5 is there to secure.
- **Nothing here says OI yields Navier–Stokes.** The programme's control 2 applies: a lattice gas
  with the right conservation laws and stencil is not a hydrodynamic limit, and the candidate is
  not shown to be selected by OI.
- **Nothing here is a continuum statement.** No PDE limit is asserted, no scaling map is fixed
  beyond the field lift, no Euler or Navier–Stokes equation is written, and the continuum-breakdown
  branch (S1–S5) stays closed until H4–H7 exist, per the programme's control 5.
- **No timescale separation is asserted.** No collision, block or hydrodynamic time is named as
  a hypothesis or a finding.
- **Nothing here changes A1–A6 or their status.** A6 remains a GAP on its own branch; the wave
  representative's A1–A5 are consumed as proved; the candidate's A-profile is a fact about the
  candidate.
- **The alphabet-as-gauge and amplitude-scale-gauge principles are consumed as the manuscripts
  state them, not tested.** The candidate's fixed alphabet and its non-additivity are recorded
  against them; whether either disqualifies the candidate as an OI substratum is not decided here.
- **No manuscript is edited by this round.** Publication-facing claims wait, per the programme's
  control 10.
- **Nothing about `d = 3`.** A three-dimensional candidate of the same type is the successor
  question if this round lands, and is not begun here.

## Immutable inputs

Cited and consumed **unmodified**: `Substratum`, `Substratum.Conf`, `Substratum.φ`, `shiftBy`,
`A1`, `A2`, `A3`, `A4Exact`, `A4`, `A5`, `a2_every_substratum`, `a1_of_finite`, `a3_of_fintype`,
`a4_of_exact`; `leap`, `leapEquiv`, `curOf`, `prevOf`, `curOf_leap`; `Rule`; `waveSubstratum`,
`dir`, `nbrs` (comparison only); `CoarseCloses`, `coarse_evolution_additive`,
`coarseCloses_additive_on_range`, `totalSum`, `blockSum`, `axisMoment4`, `axisMoment4_eq`,
`axisMoment4_quartic`, `axisMoment4_not_isotropic`, `SymInvariantQuartic`, `IsotropicQuartic`;
`IsSign`, `OhInvariant`, `quadratic_isotropic`, `quartic_ohInvariant`, `quartic_not_isotropic`;
[SM §2.7], [SM §4.1] and its amplitude-scale-gauge lemma; [Substratum] A1–A6 and the
hypothesis-dependency remark, Theorem 24 (ii); `../PROGRAMME.md` §3, §4, §6, §7.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, with archive mode

1. **This preregistration blob is merged into `main` before any execution-specific H-B object
   enters the repository tree** — any Lean definition or proof about the hexagonal stencil, the
   collision permutation, the streaming map, the graph sector, channel-weighted totals, stencil
   moments, block charges or charge sectors, any probe, any result artifact. **The single permitted
   exception is the analysis recorded inside this control-plane blob itself**, merged *as* the
   freeze, including recorded items 1–7.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode, the rule adopted 2026-09-13 (PR #599).** After the execution PR merges, the
   guard **re-runs the same strong check against the sealed execution head pinned by SHA, together
   with the merge commit that carried it**: the pinned merge commit must carry the sealed head as
   its second parent; the sealed head must pass clauses 4–6 against `B` exactly as it did in its
   own PR run; and **both the sealed head and the merge commit must be reachable from the current
   target** — the real `pull_request.head.sha` in PR CI, `HEAD` otherwise — **fail-closed**, so
   that a rewritten or vanished history fails rather than passes. Archive mode touches no blob pin
   and no base; it re-certifies the object that was reviewed.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most eight** top-level definitions, and these are the eight:

1. **`hexDir`** — `Fin 6 → Fin 2 → ℤ`, the six lattice directions `c_k` as integers, cast to
   `ZMod L` where a site is formed (H-A's `dir_eq_intCast` pattern). *Needed.*
2. **`hexCollide`** — `Equiv.Perm (Fin 6 → ZMod 2)`, the on-site collision with its explicit
   inverse. *Needed.*
3. **`hexStream`** — `Equiv.Perm ((Fin 2 → ZMod L) → (Fin 6 → ZMod 2))`, streaming with its
   inverse. *Needed.*
4. **`hexGas`** — `Φ`, the composite `hexStream ∘ Equiv.piCongrRight (fun _ => hexCollide)`, as an
   `Equiv`. *Needed.*
5. **`hexSubstratum`** — the `Substratum` instance, its `Rule` built inline with
   `F c := hexGas c + hexGas.symm c` and `N i := image (k ↦ i + hexDir k)`. *Needed.*
6. **`hexSum`** — the channel-weighted total over a finite set of sites, `hexSum A w c`; mass,
   momentum and block charges are its instances. *Needed.*
7. **`hexMoment4`** — the fourth moment of the six embedded unit vectors, the embedding written
   inline. *Needed.*
8. **`hexRot`** — the `60°` lattice rotation acting on configurations, only if `HB1-e` is
   attempted at kernel level. *Conditional.*

**A ninth definition requires its own append-only amendment.** **No witness configuration, block
partition instance, trajectory, weight vector or charge sector is a top-level definition** — each is
a bound variable pinned by an equation in the statement that needs it; the graph sector `Γ` is
written as the predicate `prevOf x = hexGas.symm (curOf x)` inside each statement; the second and
sixth moments are written inline. `HydroSourceAudit`'s, `CubicIsotropy`'s and
`SubstratumInterfaceAudit`'s definitions are **reused, not redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for `HB0`,
`HB1-a`–`HB1-d`, `HB2`, `HB3-a` and `HB3-b`, with the preregistered fallbacks for `HB1-b`'s
64-state direction and `HB3-a`'s witness evaluation, and for `HB1-e` under its frozen level-3
fallback. `decide` over finite types is permitted; `native_decide` is not. The inherited scaling
skeleton is a recorded specification, evidence type "prose/source audit" (programme control 9),
and is labelled as such. Recorded items 1–7 are analysis, not evidence.

## Named hazards

1. **Reading a `d = 2` witness as a statement about the manuscripts' `d = 3` substratum.** The
   candidate is two-dimensional because that is where the least fourth-order-isotropic stencil
   lives; nothing about three dimensions is said.
2. **Reading the candidate as OI's substratum.** It instantiates the interface and satisfies
   A1–A4; it fails A5 by construction and is not shown to be selected by anything. "OI has a
   fluid" is forbidden in terms.
3. **Manufacturing a `q`-gauge test.** The candidate has no free alphabet parameter; inventing one
   to run H-A's test would test an object this round did not freeze. The admissibility of a fixed
   Boolean alphabet under [SM §2.7] is recorded as an owner question, not decided.
4. **Reading `HB1-b′` as "no spurious invariants".** The uniqueness is within site-independent
   channel-weighted totals; staggered and time-dependent invariants are outside the class and are
   not adjudicated.
5. **Reading `HB2-b` as HD for the isotropy obligation.** The bare stencil moment is not yet shown
   to be the tensor H5's closure consumes; the status is conditional until that bridge lands —
   the same discipline H-A applied to the negative finding, applied to the positive one.
6. **Losing the chirality.** The collision is rotation-covariant and not reflection-covariant, and
   this is forced in the class, not chosen. Any parity statement, and any consequence for a
   transport coefficient, belongs to H-C and is not made here.
7. **Stating a conservation law off the sector.** `leap F` conserves nothing this round names
   outside `Γ` (`HB0-c`); every conservation statement carries "on `Γ`" and the execution may not
   drop it.
8. **Sliding from non-additivity to advection.** `HB0-b` removes H-A's obstruction for this
   candidate and exhibits no advective term; the advection obligation is HO.
9. **Reading `HB3-a`'s non-closure as absence of local equilibrium, or `HB3-b`'s invariant
   measure as its presence.** One is a diagnostic about one exact coarse variable; the other is
   the trivial invariance of counting measure on a charge sector; the statistical question is HO.
10. **Preregistering a timescale separation.** None is; no relation between times appears as a
    hypothesis or a finding.
11. **Reading the sixth-moment anisotropy as a defect of the candidate for this round.** Fourth
    order is what the stress expansion needs; `HB2-d` bounds the claim and is not a negative
    finding about H2.
12. **Importing OI → QM results or Track B labels** as evidence here, or exporting these findings
    there — control 1.
13. **Speaking about singularities.** S1–S5 remain closed until a continuum map exists.
14. **Using the word that the repository's style rule bans for constructions.** Elementary,
    smallest, least.

## Non-doings

The round does not: modify the `Substratum`, `Rule` or `leap` interfaces, or add fields to them;
construct a second candidate, a three-dimensional candidate, a rest-particle variant or a
time-alternating collision; take any continuum limit or assert any PDE (H-C); assert any
statistical closure, mixing or local-equilibrium statement; test or weaken the alphabet-as-gauge or
amplitude-scale-gauge principles; edit A1–A6 or their kernel status; edit `PROGRAMME.md`'s status
line in this PR; touch any manuscript; say anything about Track B, Track I, Bell, gravity or
singularities.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean
  module, the result note, the probe guard (pinning this blob and certifying clause 5's ancestry,
  with clause 7's archive mode entered once the sealed head and its merge commit are pinned), the
  `PROGRAMME.md` §8 refresh and `ROADMAP` propagation, and the census entry. **No manuscript
  changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`HB0`** — the candidate's A-profile (A1–A4 proved, A5 failing with the witness), the sector
   identity and the off-sector countercontrol; the advection obligation HO, in this file's words;
2. **`HB1`** — streaming invariance, the collision classification `HB1-b`/`HB1-b′` with the three
   conditions and the span, exact conservation of mass and momentum on `Γ` for every `L` and every
   configuration, translation invariance, and rotation covariance at the strength reached or under
   its fallback; the invariance principle stated as this file states it, with the absence of a
   `q`-gauge analogue and the owner question named; HD for mass and momentum on the sector, HO
   outside the class;
3. **`HB2`** — the second, fourth and sixth moments with their values; the comparison with
   `axisMoment4 2` and the citation of H-A's `d = 3` results; HD for the stencil tensor and the
   conditional status for the stress, in this file's words;
4. **`HB3`** — the witness with coordinates; the sector-measure statement; HO for H3; no timescale;
5. the inherited scaling skeleton, with the one choice the candidate fixes named;
6. the programme-level reading, verbatim from this file and conditional on every qualifier, and the
   post-round programme status under the frozen status rule — H-B not reported closed, no label
   written "for OI", the witness stated as a witness in the A1–A4, ¬A5 class, the admissibility of
   that class recorded as open;
7. what the outcomes do **not** license, in this file's wording, with the owner decision on A5
   named as open and `d = 3` named as the successor question;
8. the definition count against the eight-slot budget, the conditional slot marked fired or unused;
9. the chronology certification, including clause 7's archive-mode entry, and the axiom table with
   one line per named result.
