# Hydrodynamics round H-A — the source audit of the concrete wave representative: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`934cd6aff1cfb07b823c9b131693ee59bb98c632`, merged into `main` as
`ae81459372887cfbe27b427b30bbdad1b564f2b7` (PR #595) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `ae81459372887cfbe27b427b30bbdad1b564f2b7` (merge of PR #595) |
| This round's frozen control plane | `preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` |
| The programme roadmap | `../PROGRAMME.md`, blob `bda6a01e41c046b07536e06d2f81b4085b89cd0b` at the base; its §8 one-line state and its status-base line are refreshed by this execution PR, recording this round's outcome and the new base and nothing more |
| The concrete substratum in the kernel | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `waveF`, `waveRule`, `waveSubstratum`, `dir`, `nbrs`, `waveSubstratum_A1` … `waveSubstratum_A5` |
| The phase-space update | `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean`, blob `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` — `leap`, `leapEquiv`, `curOf`, `prevOf` |
| The rule interface | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` — `Rule` |
| The isotropy layer | `verification/lean-mathlib/OIBridge/CubicIsotropy.lean`, blob `c1918dc0c4ffaf1547f1918e6665f7c086233796` — `IsSign`, `flip`, `isSign_flip`, `OhInvariant`, `ohInvariant_iff`, `quadratic_isotropic`, `quartic_ohInvariant`, `quartic_not_isotropic` |
| The manuscript's rule and gauge principle | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — §2.7, §4.1, Corollary 1a, "The two roles of the dynamics" |
| The substratum gauge group | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — Theorem 24 (ii) |
| This round's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean` |

Every blob in the freeze's start-state table is the blob at the base: nothing consumed moved
between the freeze and the execution. **Parallel-track separation holds**: nothing here consumes
or produces evidence for the OI → QM chain (Track B, Track I), for Bell, or for gravity.

## Outcome, in one line

**Every target landed at its predicted sign and at evidence level 2, and the `H2a` dimension count
was reached at kernel level — the frozen level-3 fallback for the `H2a` dimension count was not
used.** The linearity gate closes as the composition of two additive maps (`H0`); the total-sum
conservation law is classified exactly and its manuscript instance is conserved iff `q ∣ 4`
(`H1`); the fully symmetric `O_h`-invariant rank-4 tensors are exactly the two-parameter family
spanned by `Σ_i k_i⁴` and `(Σ_i k_i²)²`, with the rotation-invariant ones the one-parameter
multiples of the latter (`H2a`); the axis stencil's fourth moment is `2 · [a = b = c = e]`,
`O_h`-invariant and not rotation-invariant (`H2b`); the frozen block variable does not close at
`d = 1`, `L = 6`, `b = 3` for every `q ≥ 2`, and the `L = 4`, `b = 2` control closes (`H3a`); the
scaling skeleton is recorded below (`H4a`). **Nothing moved from its predicted strength, and no
target is UNDECIDED.**

## `H0` — the linearity gate

`CoarseCloses`, `coarse_evolution_additive`, `coarseCloses_additive_on_range`,
`coarseCloses_nsmul`, with `curOf_add`, `prevOf_add`, `curOf_leap` and `map_zero_of_additive` as
the mechanism, and `wave_coarse_evolution_additive`, `wave_coarseCloses_additive_on_range` as the
instances consuming `waveSubstratum_A5` through `waveSubstratum_F`.

**`H0-a`.** For every additive coarse map `C : (ι → V) →+ (B → V)` and every additive microscopic
rule `F`, the coarse two-time evolution `(x_{t−1}, x_t) ↦ (C x_t, C x_{t+1})` — the step being the
kernel's `leap`, `curOf (leap F x) = F (curOf x) − prevOf x` — is an additive map of the phase
space (`coarse_evolution_additive`, an `AddMonoidHom` whose values are pinned by the statement).
Over `ZMod q` an additive map is `ZMod q`-linear. The wave instance is `wave_coarse_evolution_additive`,
whose only input beyond `C` is `waveSubstratum_A5`.

**`H0-b`.** If a coarse rule `Φ` closes — `C x_{t+1} = Φ (C x_t, C x_{t−1})` for every
microscopic pair, the predicate `CoarseCloses` — then `Φ` agrees with an additive map on the range
of `(C, C)`: `Φ (C x_t + C y_t, C x_{t−1} + C y_{t−1}) = Φ (C x_t, C x_{t−1}) + Φ (C y_t, C y_{t−1})`
for all microscopic pairs `x`, `y` (`coarseCloses_additive_on_range`), and consequently is
`ℕ`-homogeneous of degree one on those states, `Φ (n·u, n·v) = n·Φ (u, v)` (`coarseCloses_nsmul`).
An advective term `(u·∇)u` is quadratic and would scale as `n²`. **Consequently no closed
`ZMod q`-linear coarse description of the present rule carries a quadratic (advective) term on the
coarse states it is defined on.** The proof is the composition of two additive maps, as the freeze
said it would be.

**Reported status for the advection obligation: HI, conditional on the coarse-variable class.** The
class is `ZMod q`-linear coarse-graining, named in the statement. **Real-valued or nonlinear coarse
variables are HO**: the round does **not** assert "the mod-`q` wraparound is the only nonlinearity
available" — a real lift `ZMod q → ℤ → ℝ` followed by products is *a* nonlinear coarse-graining, and
whether it carries an advective term is a separate question this round neither asks nor answers.
The status carries its class; dropping the class over-reads it (hazard 4).

## `H1` — the total-sum conservation law and its `q`-gauge invariance

`totalSum`, `totalSum_waveF`, `totalSum_leap`, `totalSum_second_difference`, `totalSum_single`,
`deltaS_conserved_iff`, `combination_conserved_iff`, `deltaS_conserved_iff_dvd_four`,
`deltaS_conserved_iff_two_or_four`.

**The torus identity.** `Σ_i F(x)(i) = 2dα · Σ_i x(i)` (`totalSum_waveF`): every translate of a
configuration has the same total, so each of the `2d` neighbour sums is the total, and the
`2d = card (Fin d × Bool)` is counted by the kernel. Hence `S_{t+1} = 2dα S_t − S_{t−1}` on every
trajectory (`totalSum_leap`), and the zero-mode second difference is `(2dα − 2) S_t`
(`totalSum_second_difference`) — recorded, as the freeze records it, as an interpretation of the same
identity and not as a separate target; it licenses no claim about a mass, a metric, or a continuum
operator.

**`H1-a`.** `ΔS_t = S_t − S_{t−1}` is conserved along every trajectory **iff**
`(2dα − 2 : ZMod q) = 0` (`deltaS_conserved_iff`), both directions in one statement. The converse
uses the trajectory with `x_{t−1} = 0` and `x_t = δ_{i₀}` at the site `i₀ = 0` of a nonempty torus
(`[NeZero L]`): `S_t = 1`, `ΔS_t = 1`, `ΔS_{t+1} = 2dα − 2`. The theorem is stated for every `q`;
its content for the alphabet class `q ≥ 2` is the one the freeze asks for.

**`H1-b`.** `a S_t + b S_{t−1}` is conserved on every trajectory **iff** `b = −a` and
`a · (2dα − 2) = 0` in `ZMod q` (`combination_conserved_iff`): two trajectories — `(0, δ_{i₀})` and
`(δ_{i₀}, 0)` — force the shape and the coefficient condition, and the backward direction is the
recurrence. So the first difference is the only shape a universally conserved total-sum combination
can take, and it is available exactly when the coefficient `2dα − 2` annihilates `a`.

**`H1-c`, the manuscript instance `d = 3`, `α = 1`.** `ΔS` is conserved for every trajectory
**iff** `q ∣ 4` (`deltaS_conserved_iff_dvd_four`, through `ZMod.natCast_eq_zero_iff`), i.e. for
`q ≥ 2` **iff** `q ∈ {2, 4}` (`deltaS_conserved_iff_two_or_four`). The arithmetic the freeze
recorded by hand is the arithmetic the kernel returns: `2·3·1 − 2 = 4`.

**The `q`-gauge test, in the freeze's words.** [SM §2.7] and [Substratum, Theorem 24 (ii)] make
`q` a gauge parameter whose choice leaves all observables unchanged. A conservation law of a
physical hydrodynamic field is an observable statement. `H1-c` shows the candidate law holds for two
alphabet sizes and fails for every other `q ≥ 2`. **Therefore the candidate conserved field `ΔS` is
not `q`-gauge invariant**, and under the stated gauge principle it cannot be the universal conserved
hydrodynamic momentum of the present wave rule. **The execution does not choose `q = 2` or `q = 4`
to rescue the field**, and the round does not report "the substratum has a conserved momentum at
`q = 4`" as a hydrodynamic finding (hazard 2).

**Bounded reading, in the freeze's terms.** The finding is that **this candidate field**, under
**this rule**, fails `q`-gauge invariance. It is **not** a universal no-go for all possible
hydrodynamic variables: block variables, real-lifted variables, currents built from differences, and
any variable of a different substratum are outside `H1` and are **HO** until a round asks about
them. "No hydrodynamic variable can be conserved" is not said here, in any form (hazard 1).

**Reported status for H1: HI for the total-sum candidate under the `q`-gauge principle; HO for
every other candidate conserved field.** The `q`-gauge principle is consumed as the manuscripts
state it, not tested; if it were weakened elsewhere, `H1`'s status claim would need re-reading, and
`H1-a`–`H1-c` themselves would not change.

## `H2a`, `H2b` — the fourth-rank tensor Navier–Stokes needs, and the axis stencil against it

`SymInvariantQuartic`, `IsotropicQuartic`, `quartic_form_diag`, `quartic_form_pair`,
`quartic_form_span`, `symInvariant_eq_zero_of_single`, `exists_perm_zero_one`,
`symInvariant_closed_form`, `symInvariantQuartic_span`, `symInvariantQuartic_iff`,
`symInvariant_isotropic_iff`; `dir_eq_intCast`, `axisMoment4`, `axisMoment4_eq`,
`axisMoment4_quartic`, `axisMoment4_three_eq`, `axisMoment4_symInvariant`,
`axisMoment4_form_not_isotropic`, `axisMoment4_not_isotropic`.

**`H2a`, the fully symmetric counts, reached at level 2.** `SymInvariantQuartic T` is: full
symmetry (the three adjacent slot transpositions, which generate `S_4`), invariance under every
sign flip of the axes (`IsSign`, reused), and invariance under every coordinate permutation — the
`O_h`-invariant fully symmetric rank-4 tensors, identified with the `O_h`-invariant homogeneous
quartic forms through `k ↦ Σ_{abce} T_{abce} k_a k_b k_c k_e`. With
`D_{abce} = [a = b = c = e]`, the tensor of `Σ_i k_i⁴` (`quartic_form_diag`), and
`P = δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc}`, three times the tensor of `(Σ_i k_i²)²`
(`quartic_form_pair`):

- **the spanning statement and the dimension count, `2`:** `symInvariantQuartic_iff` — `T` is
  `SymInvariantQuartic` **iff** `T = x·D + y·P` for a **unique** pair `(x, y) ∈ ℝ²`, an `∃!`.
  Existence is the finite averaging argument, carried out in the kernel: a sign flip at an axis
  occurring exactly once kills the entry (`symInvariant_eq_zero_of_single`), a coordinate
  permutation carrying `0 ↦ a`, `1 ↦ c` (`exists_perm_zero_one`) equates every `aaaa` entry to
  `T₀₀₀₀` and every `aabb` arrangement to `T₀₀₁₁`, and the 81 index tuples are then decided one
  by one (`symInvariant_closed_form`); uniqueness reads the coefficients off `T₀₀₀₀` and `T₀₀₁₁`.
  The converse is `symInvariantQuartic_span`. A space in bijective linear coordinates with `ℝ²` is
  two-dimensional; the count is stated as this coordinatization, and no `Module.finrank` numeral
  is computed.
- **the rotation-invariant ones, `1`:** `symInvariant_isotropic_iff` — for the spanning family,
  `IsotropicQuartic (x·D + y·P) ↔ x = 0`, where `IsotropicQuartic` says the form is a function of
  `|k|²` (two vectors of the same length give the same value: the notion `quartic_not_isotropic`
  already speaks in, and for a homogeneous polynomial it is rotation invariance since the rotations
  act transitively on each sphere). So the rotation-invariant fully symmetric `O_h`-invariant
  tensors are exactly the multiples of `P`, one-dimensional.

**The counts are the fully symmetric ones — 2 versus 1.** The general (non-symmetric) rank-4
invariant counts are different objects and are not this round's (hazard 6). The freeze predicted
the dimension count at medium strength at kernel level with a level-3 fallback; **the fallback is
not used**, and no probe was added.

**`H2b`, the axis stencil.** `axisMoment4 d` is
`T_{abce} = Σ_{p} (dir p)_a (dir p)_b (dir p)_c (dir p)_e` over the `2d` axis directions `±e_k`,
taken in the real embedding of the integer stencil that `dir_eq_intCast` identifies with the
kernel's own `dir` (`dir d L p` is the `ZMod L`-cast of the integer vector `±e_{p.1}`). Then, for
every `d`:

- `T_{abce} = 2 · [a = b = c = e]` — nonzero only on the diagonal (`axisMoment4_eq`);
- its quartic form is `2 Σ_i k_i⁴` (`axisMoment4_quartic`);

and at `d = 3`, where `axisMoment4 3 = 2·D + 0·P` (`axisMoment4_three_eq`): `T` is
`O_h`-invariant (`axisMoment4_symInvariant`) and **not** rotation-invariant — in the freeze's form,
two vectors of the same length on which its quartic form differs (`axisMoment4_form_not_isotropic`,
consuming `quartic_not_isotropic`), and in the predicate of `H2a`
(`axisMoment4_not_isotropic`). **The present stencil fails the isotropy the stress expansion
requires**, at fourth order.

**Reported status for H2: exact stencil anisotropy proved; conditional HI if H5's stress closure
consumes this tensor; otherwise H2 remains HO.** Whether the bare fourth moment of the stencil is
the effective rank-4 tensor the H5 stress closure consumes is a bridge this round does **not**
build; until it lands, the anisotropy is a proved fact about the stencil and a *conditional* finding
about hydrodynamics, and the round does not label the isotropy obligation HI outright (hazard 5).
This is the cubic-lattice fourth-order anisotropy that deterministic lattice-gas hydrodynamics
historically had to escape by changing the stencil; it says nothing about stencils the round does
not examine, and it is precisely the kind of finding H-B is designed to act on. **Corollary 1a's
quadratic isotropy is consumed unchanged and is not contradicted**: quadratic order is isotropic,
quartic order is not, and Navier–Stokes needs the quartic order.

## `H3a` — a block-observable diagnostic for closure

`blockSum`, `blockSum_apply`, `sum_fin_one_fun`, `waveF_one_dim`, `blockSum_one_dim`,
`sum_zmod_six`, `sum_zmod_four`, `h3a_block_state_not_closed`, `h3a_no_closure`,
`h3a_control_L4_closes`.

`blockSum d L q b` is the block-partition coarse map: the block of a site is
`β(i)_k = ⌊i_k / b⌋ ∈ ZMod (L / b)` and `B_β(x) = Σ_{i ∈ β} x(i) ∈ ZMod q`, an additive map onto
`Fin d → ZMod (L / b)`; the partition into cubes of side `b` is the case `b ∣ L`.

**The witness, with coordinates** (`h3a_block_state_not_closed`), at `d = 1`, `L = 6`, `b = 3`,
`α = 1`, for **every** `q ≥ 2`, every configuration pinned by an equation in the statement:

- both pairs have `x_{t−1} = 0`; one has `x_t = 0`, the other `x_t = y = (−1, 1, 0, 0, 0, 0)`,
  i.e. `y(i) = −1` if `i = 0`, `1` if `i = 1`, `0` otherwise;
- both block states are `(0, 0)` at `t` and at `t − 1`: `B(0) = 0` and `B(y) = 0` on both blocks,
  `−1 + 1 + 0 = 0` and `0 + 0 + 0 = 0`;
- at `t + 1` the zero trajectory stays zero, while on block `{0, 1, 2}`
  `Σ_{i∈{0,1,2}} F(y)_i = (y_5 + y_1) + (y_0 + y_2) + (y_1 + y_3) = 1 ≠ 0` — the kernel returns
  `1` on that block (`blockSum … (fun _ => 0) = 1`), and `1 ≠ 0` in `ZMod q` for `q ≥ 2`;
- so the block states at `t + 1` differ.

**Consequently no coarse rule closes on this block variable**: `¬ ∃ Φ, CoarseCloses (blockSum 1 6 q 3)
(waveF 1 6 q 1) Φ` (`h3a_no_closure`), for every `q ≥ 2`.

**The closing control.** The smaller candidate `d = 1`, `L = 4`, `b = 2` is **not** a witness, and
this is proved rather than only recorded: there the block sum of `F` over `{0, 1}` is
`α · ((x_3 + x_1) + (x_0 + x_2))`, `α` times the total sum, which the two block sums determine, so
`Φ (u, v)(β) = α · (u(0) + u(1)) − v(β)` closes, for every `q` and every `α`
(`h3a_control_L4_closes`).

**Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
of a statistical closure at some other scale or in some other variable, and no local-equilibrium or
mixing statement is made in either direction (hazard 7). **No relation `τ_B ≪ τ_S` is
preregistered**, no timescale is asserted (hazard 8), and the memory diagnostic is exactly what its
statement says: this block variable needs more than its own two-time state to predict its next
value.

## `H4a` — the scaling skeleton

Not a theorem, and no theorem is claimed; evidence type "prose/source audit" (programme control 9).
A continuum map for this substratum must fix, before any PDE statement is meaningful:

1. the lattice spacing as a function of `L`;
2. the time step;
3. the field normalization — including how `ZMod q` values are lifted (to `ℤ`, to `ℝ`, or otherwise)
   and rescaled;
4. the carrier growth — how `L`, `q` and the coarse-graining scale are taken together;
5. the topology in which convergence would be claimed.

**None is fixed by the manuscripts or by A1–A6.** [SM §4.1] fixes the rule and [SM §2.7] the
alphabet as gauge; neither names a spacing, a time step, a lift, a joint growth, or a norm, and
`waveSubstratum_A1`–`A5` are statements at one finite `L` and `q`. **Reported status for H4: HO**,
with the skeleton as the deliverable. No limit is taken and no PDE is written. The rigorous-limit
literature is calibration for H5–H7 only and is not attached to H4 (hazard 9).

## The programme-level reading, verbatim from the freeze and conditional

> the present wave representative is pushed toward **HI for a direct Navier–Stokes limit** by the
> linearity gate on `ZMod q`-linear coarse variables, together with the `q`-dependence of the only
> total-sum conservation law, and — **conditionally on H5's closure consuming the stencil's fourth
> moment** — by the fourth-order anisotropy of the axis stencil; while the broader construction
> programme (H-B: other OI-compatible reversible local substrata) is **entirely alive** and is where
> the next round belongs. **This reading is conditional on every qualifier above**, and the
> execution may not shorten it.

The execution does not shorten it. Each qualifier is carried by a theorem statement: the class
`ZMod q`-linear in `H0`, the candidate field `ΔS` in `H1`, the bare stencil moment in `H2b`.

## What these outcomes do NOT license

- **Nothing here says OI cannot support fluid hydrodynamics.** The findings are about one
  representative rule, one stencil, one class of coarse variables, and one candidate conserved
  field. H-B's construction question is untouched and unprejudiced, and H-B is entirely alive.
- **Nothing here is a continuum statement.** No limit is taken, no PDE is asserted or denied, and
  the continuum-breakdown branch (S1–S5) stays closed until H4–H7 exist, per the programme's
  control 5.
- **Nothing here changes A1–A6 or their status.** A6 remains a GAP on its own branch; A5 is
  consumed as proved.
- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity —
  control 1. No Track B label is imported as evidence here and none of these findings is exported
  there (hazard 10).
- **The `q`-gauge principle is consumed as the manuscript states it, not tested.**
- **No manuscript is edited by this round.** Publication-facing claims wait, per the programme's
  control 10.

## The chronology control

**`R7-HYA` certifies the strong property**, reusing act 10's mechanism by name through acts 11 and
12's copies:

- the preregistration blob is pinned **by content** to `934cd6aff1cfb07b823c9b131693ee59bb98c632`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = ae81459372887cfbe27b427b30bbdad1b564f2b7` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** **The claim is scoped to the repository record.** The preregistration blob was
merged alone, before any execution-specific H-A object entered the tree; the single permitted
exception — the `H1` arithmetic and the `H2b` moment recorded inside the control plane itself — is
the analysis the kernel re-derives above. **No discrepancy between the preregistration and the
execution was found**; the preregistration is unamended.

## Definition budget: **SIX of the frozen seven slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `totalSum` | **fired** |
| 2 | `blockSum` | **fired** |
| 3 | `CoarseCloses` | **fired** |
| 4 | `axisMoment4` | **fired** |
| 5 (conditional) | `SymInvariantQuartic` | **fired** — `H2a` was attempted, and reached, at kernel level |
| 6 (conditional) | `IsotropicQuartic` | **fired** — the "1" side is stated as a predicate and proved, not only consumed from `quartic_not_isotropic` |
| 7 (conditional) | a `ΔS` abbreviation | **unused** |

Slot 7 did not fire: `ΔS` is written out as `totalSum (curOf x) − totalSum (prevOf x)` in every
statement that needs it. **No eighth definition was introduced**, and no witness configuration,
block partition instance, or trajectory is a top-level definition — each is a bound variable pinned
by an equation in the statement that needs it. `CubicIsotropy`'s and `SubstratumInterfaceAudit`'s
definitions are reused, not redefined; `D` and `P` of `H2a` are written out inside the statements
that use them.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked, for `H0`, `H1`, `H2a`, `H2b` and `H3a`. Forty-four named
results, **no `sorry`, no `axiom`, no `native_decide`**, every axiom line within
`{propext, Classical.choice, Quot.sound}` — three definitional lemmas depend on no axiom at all and
two on `[propext, Quot.sound]`, which the kernel reports as such and is recorded as such:

| Result | Axioms |
| --- | --- |
| `curOf_add` | does not depend on any axioms |
| `prevOf_add` | does not depend on any axioms |
| `curOf_leap` | does not depend on any axioms |
| `map_zero_of_additive` | `[propext, Quot.sound]` |
| `coarse_evolution_additive` | `[propext, Classical.choice, Quot.sound]` |
| `coarseCloses_additive_on_range` | `[propext, Classical.choice, Quot.sound]` |
| `coarseCloses_nsmul` | `[propext, Classical.choice, Quot.sound]` |
| `waveSubstratum_F` | `[propext, Classical.choice, Quot.sound]` |
| `wave_coarse_evolution_additive` | `[propext, Classical.choice, Quot.sound]` |
| `wave_coarseCloses_additive_on_range` | `[propext, Classical.choice, Quot.sound]` |
| `totalSum_apply` | `[propext, Classical.choice, Quot.sound]` |
| `totalSum_waveF` | `[propext, Classical.choice, Quot.sound]` |
| `totalSum_leap` | `[propext, Classical.choice, Quot.sound]` |
| `totalSum_second_difference` | `[propext, Classical.choice, Quot.sound]` |
| `totalSum_single` | `[propext, Classical.choice, Quot.sound]` |
| `deltaS_conserved_iff` | `[propext, Classical.choice, Quot.sound]` |
| `combination_conserved_iff` | `[propext, Classical.choice, Quot.sound]` |
| `deltaS_conserved_iff_dvd_four` | `[propext, Classical.choice, Quot.sound]` |
| `deltaS_conserved_iff_two_or_four` | `[propext, Classical.choice, Quot.sound]` |
| `quartic_form_diag` | `[propext, Classical.choice, Quot.sound]` |
| `quartic_form_pair` | `[propext, Classical.choice, Quot.sound]` |
| `quartic_form_span` | `[propext, Classical.choice, Quot.sound]` |
| `symInvariant_eq_zero_of_single` | `[propext, Classical.choice, Quot.sound]` |
| `exists_perm_zero_one` | `[propext, Classical.choice, Quot.sound]` |
| `symInvariant_closed_form` | `[propext, Classical.choice, Quot.sound]` |
| `symInvariantQuartic_span` | `[propext, Classical.choice, Quot.sound]` |
| `symInvariantQuartic_iff` | `[propext, Classical.choice, Quot.sound]` |
| `symInvariant_isotropic_iff` | `[propext, Classical.choice, Quot.sound]` |
| `dir_eq_intCast` | `[propext, Quot.sound]` |
| `axisMoment4_eq` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_quartic` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_three_eq` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_symInvariant` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_form_not_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_not_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `blockSum_apply` | `[propext, Classical.choice, Quot.sound]` |
| `sum_fin_one_fun` | `[propext, Classical.choice, Quot.sound]` |
| `waveF_one_dim` | `[propext, Classical.choice, Quot.sound]` |
| `blockSum_one_dim` | `[propext, Classical.choice, Quot.sound]` |
| `sum_zmod_six` | `[propext, Classical.choice, Quot.sound]` |
| `sum_zmod_four` | `[propext, Classical.choice, Quot.sound]` |
| `h3a_block_state_not_closed` | `[propext, Classical.choice, Quot.sound]` |
| `h3a_no_closure` | `[propext, Classical.choice, Quot.sound]` |
| `h3a_control_L4_closes` | `[propext, Classical.choice, Quot.sound]` |

`H4a` is a recorded specification, evidence type "prose/source audit", and is labelled as such
above.

## What this round does not do

- **It constructs no different substratum or stencil** — that is H-B, which is entirely alive.
- **It takes no continuum limit and asserts no PDE** — that is H-C, whose two evidence tracks
  (formal Chapman–Enskog expansion versus rigorous hydrodynamic-limit theorem) the freeze keeps
  apart and this round does not enter.
- **It neither tests nor weakens the `q`-gauge principle.**
- **It edits neither A1–A6 nor their kernel status.**
- **It touches no manuscript.**
- **It says nothing about Track B, Track I, Bell, or gravity**, and nothing here is evidence for
  anything there.
