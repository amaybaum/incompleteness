# Hydrodynamics round H-B — a reversible streaming-and-collision substratum: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`37cc9dae301ee10d55adb73b296aa2fc7d0578e3`, merged into `main` as
`8de0478ef31fe4cabcf89fc5787f80f38376a957` (PR #601) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `8de0478ef31fe4cabcf89fc5787f80f38376a957` (merge of PR #601) |
| This round's frozen control plane | `preregistration.md`, blob `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` |
| The programme roadmap | `../PROGRAMME.md`, blob `07aaa6c4d96a1ad613d0ff64adbb9f8745f0856f` at the base; its §8 one-line state and its status-base line are refreshed by this execution PR, in the frozen words and nothing stronger |
| Round H-A, the frozen control plane | `../round-h-a-source-audit/preregistration.md`, blob `934cd6aff1cfb07b823c9b131693ee59bb98c632` — the format model |
| Round H-A, the result | `../round-h-a-source-audit/result.md`, blob `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` — the format model; H-B named alive |
| Round H-A's module | `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean`, blob `fd5f54d8cbba4f68b67335c111d39a2add0c642f` — `axisMoment4`, `axisMoment4_eq`, `axisMoment4_quartic`, `curOf_leap`, `IsotropicQuartic`, `blockSum`, `CoarseCloses` consumed for comparison |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — `Substratum`, `shiftBy`, `A1`, `A2`, `A3`, `A4Exact`, `A4`, `A5`, `a2_every_substratum`, `a1_of_finite`, `a4_of_exact` |
| The phase-space update | `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean`, blob `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` — `leap`, `leapEquiv`, `curOf`, `prevOf` |
| The rule interface | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` — `Rule` |
| The isotropy layer | `verification/lean-mathlib/OIBridge/CubicIsotropy.lean`, blob `c1918dc0c4ffaf1547f1918e6665f7c086233796` — `quadratic_isotropic`, `quartic_not_isotropic`, cited |
| The manuscript's rule and gauge principles | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` — §2.7, §4.1 |
| The substratum axioms and their hypothesis dependencies | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` — A1–A6, the hypothesis-dependency remark |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `921a7a24d4a9c6b9e529fcc1ce283b69630de3d5` at the base — `_rbr_strong_ancestry`, `_rbr_archive_ancestry`, `R7-HYA` |
| This round's module | `verification/lean-mathlib/OIBridge/HexLatticeGas.lean` |

Every kernel and manuscript blob in the freeze's start-state table is the blob at the base:
nothing consumed moved between the freeze and the execution (`edge_rigidity_probe.py` moved from
`1c760953…` to `921a7a24…` by the intervening archive-pin PRs, which touch no mechanism this round
reuses). **Parallel-track separation holds**: nothing here consumes or produces evidence for the
OI → QM chain (Track B, Track I), for Bell, or for gravity.

## Outcome, in one line

**Every target landed at its predicted sign and at evidence level 2, at full strength: `HB1-b`'s
64-state direction closed at kernel level by case analysis on the five moved states, `HB1-e` was
reached at kernel level, and `HB3-a`'s recorded witness evaluated exactly as recorded — the frozen
fallbacks for `HB1-b`, `HB1-e` and `HB3-a` were not used.** The candidate satisfies A1–A4 and
fails A5 with the recorded witness (`HB0`); its graph sector is invariant and carries the gas, and
mass is not conserved off it (`HB0-c`); mass and both momentum components are exactly conserved by
the gas on every configuration for every `L`, on `Γ`, and are the only conserved site-independent
channel-weighted totals (`HB1`); the stencil's second moment is `3 δ`, its fourth moment is
`(3/4)(δδ + δδ + δδ)` and rotation-isotropic, and its sixth is not (`HB2`); the block-charge
two-time state does not close at `L = 4`, `b = 2`, and the charge sectors are invariant (`HB3`).
**Nothing moved from its predicted strength, and no target is UNDECIDED.**

## The post-round programme status, under the frozen rule

1. **Round H-B is not reported closed by this round**, and the programme's H-B obligation is not
   reported discharged. The round is reported as **one candidate executed**, with the outcomes
   below.
2. **No label in this note is written "for OI"** or "for the OI substratum". Every HD, HC, HI or
   HO label below is a label **for the candidate**, in the class it lies in.
3. What the execution establishes, at full strength, is exactly this: **a rigorous reversible
   fluid witness in the A1–A4, ¬A5 class** — finite, deterministic, reversible,
   translation-covariant, of bounded degree, inside the kernel's `Substratum` interface — **with
   exact mass and momentum conservation on every configuration for every lattice size and
   fourth-order stencil isotropy**, proved and not assumed.
4. **Whether the A1–A4, ¬A5 class counts as admissible OI physics is a separate question** — the
   owner decision the freeze names — and **its admissibility is recorded here as open.** If the
   owner later rules the class admissible, the programme-level closure of H-B is a separate owner
   action on the record, not a consequence this execution draws; if the owner rules it
   inadmissible, the candidate stands as a witness about the class and H-B's obligation stays open.
5. `../PROGRAMME.md` §8's one-line state is refreshed by this PR to read "H-B: one candidate
   executed in the A1–A4, ¬A5 class; OI-compatibility of the class open", and nothing stronger.

## The candidate, as the kernel has it

`hexDir`, `hexCollide`, `hexStream`, `hexGas`, `hexSubstratum`, `hexSum`, `hexMoment4`, `hexRot`.

Sites `Fin 2 → ZMod L`, the `L × L` periodic lattice in the hexagonal basis; the six directions
`hexDir : Fin 6 → Fin 2 → ℤ` are `c₀ = (1, 0)`, `c₁ = (0, 1)`, `c₂ = (−1, 1)`, `c₃ = (−1, 0)`,
`c₄ = (0, −1)`, `c₅ = (1, −1)`, with `c_{k+3} = −c_k` (`hexDir_add_three`,
`hexDir_cast_add_three`), cast to `ZMod L` wherever a site is formed. The alphabet is
`Fin 6 → ZMod 2`. The collision `hexCollide : Equiv.Perm (Fin 6 → ZMod 2)` is the product of the
three transpositions `swap {0,3} {1,4} · swap {1,4} {2,5} · swap {0,2,4} {1,3,5}`, so its inverse
is explicit; it carries `{0, 3} ↦ {1, 4} ↦ {2, 5} ↦ {0, 3}` and `{0, 2, 4} ↔ {1, 3, 5}`
(`hexCollide_moved`) and fixes every other state (`hexCollide_of_ne`), in particular every state
occupying at most one channel (`hexCollide_of_single`) and the empty state (`hexCollide_zero`).
It commutes with the channel rotation `k ↦ k + 1` on all 64 states (`hexCollide_channel_rot`)
and not with the channel reflection `k ↦ −k` (`hexCollide_not_reflection`): the chirality of the
freeze's recorded item 1 is recorded as a named property, and no parity statement is made.
Streaming is `hexStream L : (stream c) i k = c (i − c_k) k` with inverse `c (i + c_k) k`; the gas
is `hexGas L := (Equiv.piCongrRight fun _ => hexCollide).trans (hexStream L)`, collide then
stream, with `hexGas L c i k = hexCollide (c (i − c_k)) k` and
`(hexGas L).symm c i = hexCollide.symm (fun k => c (i + c_k) k)` (`hexGas_apply`,
`hexGas_symm_apply`, both definitional). `hexSubstratum L` is the kernel's `Substratum`,
consumed unmodified, with its `Rule` built inline: `F c := hexGas L c + (hexGas L).symm c`,
`N i := image (k ↦ i + c_k)` (`hexSubstratum_F`, `hexSubstratum_N`, both definitional).
`hexSum A w c := Σ_{i ∈ A} Σ_k (c i k).val · w k`. `hexMoment4` is the fourth moment of the six
embedded unit vectors `u_k = ((c_k)₁ + (c_k)₂/2, (c_k)₂ √3/2)`, the embedding written inline.
`hexRot L` is `(ρ·c) i k = c (ρ⁻¹ i) (k − 1)` with `ρ⁻¹ (a, b) = (a + b, −a)`, i.e.
`(ρ·c) (ρ i) (k + 1) = c i k` for `ρ (a, b) = (−b, a + b)`.

## `HB0` — the A-profile, the sector, and the off-sector control

`hexSubstratum_A1`, `hexSubstratum_A2`, `hexSubstratum_A3`, `hexSubstratum_A4Exact`,
`hexSubstratum_A4`, `hexSubstratum_A5_witness`, `hexSubstratum_not_A5`, `hexSubstratum_sector`,
`hexSubstratum_mass_not_conserved_off_sector`, with `single_channel_zero`,
`hexGas_single_channel`, `hexGas_symm_single_channel`, `hexCollide_symm_channel_one`,
`hexSum_intCast_two`, `hexSum_add_intCast_two` as the mechanism.

**`HB0-a`, the A-profile.** For every `L` with `[NeZero L]`: `A1` through `a1_of_finite`
(`hexSubstratum_A1`); `A2` through `a2_every_substratum` (`hexSubstratum_A2`); `A3 6`, because
`N i` is the image of `Fin 6` (`hexSubstratum_A3`); `A4Exact`, because streaming and the sitewise
collision each commute with every `shiftBy v`, hence so do `Φ`, `Φ⁻¹` and their sum
(`hexSubstratum_A4Exact`), and consequently `A4 ⊥` through `a4_of_exact` (`hexSubstratum_A4`).
**Positive, full strength**, as predicted.

**`HB0-b`, A5 fails.** The witness of recorded item 4, pinned by equation in the statement:
`c = Pi.single 0 ![1, 0, 0, 0, 0, 0]` (one particle in channel `0` at the origin),
`c' = Pi.single 0 ![0, 0, 0, 1, 0, 0]` (one in channel `3` at the origin). At channel `1` of the
site `c₁`, `F (c + c') = 1` — the head-on pair collides to `{1, 4}` and streams — and
`F c + F c' = 0` — single particles do not collide, and channels `0`, `3` are all that occur — so
`F (c + c') ≠ F c + F c'`, for every `L ≥ 1` (`hexSubstratum_A5_witness`, stated for the rule
`F c = hexGas L c + (hexGas L).symm c`, which is `(hexSubstratum L).R.F` by `hexSubstratum_F`),
and therefore `¬ (hexSubstratum L).A5` (`hexSubstratum_not_A5`). **Positive (the failure), full
strength**, as predicted. The candidate lies in the class obtained by dropping A5's
amplitude-scale gauge principle, and the round says so in terms.

**`HB0-c`, the sector.** For every `x : (hexSubstratum L).Conf` with
`prevOf x = (hexGas L).symm (curOf x)`: `prevOf (leap F x) = (hexGas L).symm (curOf (leap F x))`
and `curOf (leap F x) = hexGas L (curOf x)` (`hexSubstratum_sector`) — the sector `Γ` is
invariant and the sector dynamics is exactly the streaming-and-collision gas, by the one line of
group algebra `F (curOf x) − prevOf x = Φ c + Φ⁻¹ c − Φ⁻¹ c = Φ c`. The countercontrol of recorded
item 3: for `x` with `prevOf x = 0` and `curOf x = Pi.single 0 ![1, 0, 0, 0, 0, 0]`, the mass of
`curOf x` is `1` and the mass of `curOf (leap F x)` is not `1`, for every `L ≥ 1`
(`hexSubstratum_mass_not_conserved_off_sector`). The kernel proof is by parity rather than by the
case split of the recorded analysis: `F c = Φ c + Φ⁻¹ c` read in `ZMod 2` is additive
(`hexSum_add_intCast_two`), each summand has mass `1` by `HB1-c`, so the mass of `F c` is even and
is not `1`; the recorded values `0` for `L ∈ {1, 2}` and `2` for `L ≥ 3` remain recorded analysis,
and the statement is the inequality, as frozen. **Positive, full strength**, both parts.

**Reported status for the advection obligation: HO for the candidate.** H-A's linearity gate
(`coarse_evolution_additive`, `coarseCloses_additive_on_range`) has `A5` as its hypothesis and does
not apply to the candidate; that lifts H-A's `H0` obstruction **for this candidate** and establishes
nothing positive — non-additivity is necessary for an advective term and not sufficient, and no
coarse description carrying one is exhibited or claimed. The round does not label the advection
obligation HD, HC or HI.

## `HB1` — exact conservation, and the appropriate invariance principle

`hexSum`, `hexSum_apply`, `hexSum_single`, `hexSum_hexStream`, `hexCollide_conserved_iff`,
`collide_single`, `hexSum_collide_iff`, `hexCollide_conditions_iff_span`, `hexSum_hexGas`,
`hexSum_hexGas_iff`, `hexSum_hexGas_iff_span`, `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`,
`hexSum_leap_sector`, `hexSum_shiftBy`, `hexDir_conditions`; and for `HB1-e`, `hexRot`,
`hexRot_apply`, `hexRot_apply'`, `hexRot_site`, `hexDir_sub_one`, `hexDir_add_one`,
`hexGas_hexRot`, `hexSum_hexRot`, `hexSum_neg_weight`, `hexSum_add_weight`, `hexRot_charges`.

**`HB1-a`.** `hexSum univ w (hexStream L c) = hexSum univ w c` for every `w` and every `c`
(`hexSum_hexStream`): streaming permutes site–channel pairs and preserves the channel index, so
each channel's site sum is reindexed by the translation `Equiv.subRight c_k`. **Positive, full
strength.**

**`HB1-b`.** On-site (`hexCollide_conserved_iff`): the collision preserves `Σ_k w_k n_k` on every
one of the 64 local states **iff**
`w₀ + w₃ = w₁ + w₄ ∧ w₁ + w₄ = w₂ + w₅ ∧ w₀ + w₂ + w₄ = w₁ + w₃ + w₅`. Forward: the three states
`{0, 3}`, `{1, 4}`, `{0, 2, 4}`. Backward: the identity holds for each of the 64 states — the five
moved states by the conditions, the 59 others because they are fixed (`hexCollide_of_ne`). On
configurations (`hexSum_collide_iff`): for every `L`,
`(∀ c, hexSum univ w (fun i => hexCollide (c i)) = hexSum univ w c)` **iff** the same three
conditions, the forward direction through the three one-site configurations at the origin
(`collide_single`, `hexSum_single`). **Positive, full strength; reached at kernel level** — the
64-state direction closed as a case analysis on the five moved states with the rest fixed, so the
frozen fallback (the five-state restriction, or UNDECIDED) was not used.

**`HB1-b′`.** The three conditions hold **iff** `∃ a b₁ b₂ : ℤ, w = fun k => a + b₁ · hexDir k 0 +
b₂ · hexDir k 1` (`hexCollide_conditions_iff_span`), the span of mass and the two coordinate rows
of `hexDir`, over `ℤ` — the basis is unimodular, so the span statement is over `ℤ` and not only
over `ℚ`. The kernel's witnesses are `a = w₀ − w₁ + w₂`, `b₁ = w₁ − w₂`, `b₂ = 2w₁ − w₀ − w₂`.
**Positive, full strength** (the freeze predicted high; the bookkeeping closed). **The one
discrepancy of the round is here**, and it is in the recorded analysis, not in a target: recorded
item 2 writes `b₁ = w₂ − w₁`; the correct closed form, which the kernel returns, is
`b₁ = w₁ − w₂` (from `w₀ = a + b₁` with `a = w₀ − w₁ + w₂`); `a` and `b₂` are as recorded. The
statement of `HB1-b′` is unchanged by this, and the preregistration is unamended.

**`HB1-c`.** For every `L`, every configuration `c` and every `w` satisfying the three
conditions, `hexSum univ w (hexGas L c) = hexSum univ w c` (`hexSum_hexGas`); in particular for
mass, `hexSum univ 1` (`hexSum_mass_hexGas`), and for both momentum components,
`hexSum univ (fun k => hexDir k j)` (`hexSum_momentum_hexGas`, the conditions for each row being
`hexDir_conditions`); and along every trajectory in `Γ`,
`hexSum univ w (curOf (leap F x)) = hexSum univ w (curOf x)` (`hexSum_leap_sector`, with the
sector relation `prevOf x = (hexGas L).symm (curOf x)` as its hypothesis). Conversely
(`hexSum_hexGas_iff`, `hexSum_hexGas_iff_span`): the gas preserves the total with weight `w` on
every configuration **iff** the three conditions hold **iff** `w ∈ span_ℤ {1, d₁, d₂}`.
**Positive, full strength.** **The reading, frozen:** mass and momentum are exactly conserved by
the gas, on every configuration, for every `L`, with no parameter chosen; and within the class of
site-independent channel-weighted totals **they are the only conserved quantities**, so the
candidate carries no spurious invariant of that shape. Staggered, site-dependent or
time-dependent invariants are outside the class and are **not adjudicated** (hazard 4).

**`HB1-d`.** `hexSum univ w (shiftBy v c) = hexSum univ w c` for every `v`, `w`, `c`
(`hexSum_shiftBy`), a reindexing of the site sum by `Equiv.subRight v`. **Positive, full
strength.**

**`HB1-e`, reached at kernel level; budget slot 8 fired.** With `hexRot L` the `60°` lattice
rotation of recorded item 6: `hexGas L (hexRot L c) = hexRot L (hexGas L c)` for every `c`
(`hexGas_hexRot`) — streaming is carried along by `ρ⁻¹ (i − c_k) = ρ⁻¹ i − c_{k−1}`
(`hexRot_site`, `hexDir_sub_one`) and the collision commutes with the channel rotation on all 64
states (`hexCollide_channel_rot`); `M (hexRot L c) = M c`; and
`(P₁, P₂) (hexRot L c) = (−P₂ c, P₁ c + P₂ c) = ρ (P₁, P₂) (c)` with `ρ (a, b) = (−b, a + b)`
(`hexRot_charges`, through `hexSum_hexRot`: a rotated configuration's total is the total with the
weight rotated, `w ↦ (k ↦ w (k + 1))`, and `hexDir_add_one`). **Positive, full strength; the
frozen level-3 fallback was not used, and no probe was added.**

**The invariance principle, as frozen.** H-A's `H1` test asked whether a candidate conservation
law survives the `q`-gauge principle of [SM §2.7]. **That test has no analogue here**: the
candidate carries no free alphabet parameter — its alphabet is Boolean occupation by construction
— so there is no `q` to vary and no `q` to choose, and the round does not manufacture one.
Whether a fixed Boolean alphabet is admissible under [SM §2.7]'s alphabet-as-gauge reading is an
owner-level question this round records and does not decide (hazard 3). The principle the round
**does** apply is exactness on every configuration, for every lattice size, with no parameter
tuned (`HB1-c`), together with translation invariance of the conserved fields (`HB1-d`) and
covariance under the lattice's own point symmetry (`HB1-e`).

**Reported status for H1: HD for mass and momentum, for the candidate, on the sector** — exact
conservation is a theorem about the microscopic dynamics, as the programme's H1 requires — **with
the uniqueness within the frozen class stated and the outside of the class HO.** Every
conservation statement of this round is a statement on `Γ`; off `Γ`, `leap F` conserves nothing
this round names (`HB0-c`).

## `HB2` — the lowest-order stencil tensors

`hexMoment2_eq`, `hexMoment4`, `hexMoment4_eq`, `hexMoment4_quartic`, `hexMoment4_isotropic`,
`axisMoment4_two_not_isotropic`, `hexMoment6_not_isotropic`.

**`HB2-a`.** The second moment of the embedded stencil is `3 δ_{ab}`, stated inline over the six
unit vectors (`hexMoment2_eq`): `Σ_k (u_k)_a (u_k)_b = 3 · [a = b]`. **Positive, full strength.**
This is the order Corollary 1a's `quadratic_isotropic` speaks to for the cubic case, consumed for
comparison only.

**`HB2-b`.** `hexMoment4 a b c e = (3/4)(δ_{ab}δ_{ce} + δ_{ac}δ_{be} + δ_{ae}δ_{bc})` on all
sixteen entries (`hexMoment4_eq`): `T₁₁₁₁ = T₂₂₂₂ = 9/4`, `T₁₁₂₂ = 3/4` in every arrangement, the
odd entries `0`. Consequently its quartic form is `(9/4)(Σ_i k_i²)²` (`hexMoment4_quartic`) and is
a function of `|k|²`: for all `k, k' : Fin 2 → ℝ` with `Σ k_i² = Σ k'_i²` the forms agree
(`hexMoment4_isotropic`, the notion `IsotropicQuartic` uses, stated inline for `Fin 2`). The
arithmetic is `(√3/2)² = 3/4`, `(√3/2)⁴ = 9/16`, through `Real.sq_sqrt`. **Positive, full
strength.**

**`HB2-c`, the comparison.** `axisMoment4 2 = 2 · [a = b = c = e]` by H-A's `axisMoment4_eq`; its
quartic form `2 (k₁⁴ + k₂⁴)` (`axisMoment4_quartic`) takes the value `2` at `k = (1, 0)` and `1` at
`k' = (1/√2, 1/√2)`, two vectors of equal length, on which the hexagonal form agrees
(`axisMoment4_two_not_isotropic`, the two vectors pinned by equation). So the square
four-velocity stencil is **not** fourth-order isotropic where the hexagonal six-velocity stencil
**is**. H-A's `quartic_not_isotropic` and `axisMoment4_not_isotropic` are the `d = 3` statement of
the same failure and are cited, not re-proved. **Positive, full strength.**

**`HB2-d`, the bound.** The sixth moment is not isotropic, stated inline
(`hexMoment6_not_isotropic`): `Σ_k (u_k)₁⁶ = 33/16` and `Σ_k (u_k)₁⁴ (u_k)₂² = 3/16`, so
`Σ_k (u_k)₁⁶ ≠ 5 · Σ_k (u_k)₁⁴ (u_k)₂²` — ratio `11` where a rotation-isotropic fully symmetric
rank-6 tensor has `T₁₁₁₁₁₁ = 5 T₁₁₁₁₂₂`. **Positive (the failure), full strength.** This bounds
`HB2-b`: fourth-order isotropy holds, while isotropy already fails at sixth order; **no claim is
made about higher orders** — the round proves the fourth and the sixth moment and classifies no
other even order. Fourth order is the order the Navier–Stokes stress expansion needs, and beyond
it (Burnett-level) the round says nothing. The sixth-moment anisotropy is not a negative finding
about H2 (hazard 11).

**Reported status for H2: the stencil's fourth moment is proved isotropic — HD for the stencil
tensor; for the hydrodynamic stress, HC conditional on H5's closure consuming this tensor,
otherwise HO.** As in H-A, whether the bare fourth moment of the stencil is the rank-4 tensor the
H5 stress closure consumes is a bridge this round does **not** build; the round labels the stencil
and not the obligation (hazard 5).

## `HB3` — exact closure of a coarse variable, and the sector measure

`hexSum_single_site`, `hexSum_two_sites`, `hb3a_gas_values`, `hb3a_mem`,
`hb3a_block_state_not_closed`, `hb3a_no_closure`, `hexGas_bijOn_sector`.

**`HB3-a`, the witness with coordinates**, at `L = 4`, `b = 2` (four `2 × 2` blocks, the block of
`i` being `k ↦ ⌊(i k).val / 2⌋`, H-A's convention, with the block labels read in `ℕ`), on the
sector, every configuration pinned by equation in the statement:

- `c`: a particle in channel `0` at `(0, 0)` and a particle in channel `3` at `(0, 1)`;
- `c'`: the head-on pair `{0, 3}` at `(0, 0)`.

The gas and its inverse on both, every one of the sixteen sites decided (`hb3a_gas_values`):
`Φ⁻¹ c` = channel `3` at `(1, 1)`, channel `0` at `(3, 0)`; `Φ⁻¹ c'` = channel `3` at `(1, 0)`,
channel `0` at `(3, 0)`; `Φ c` = channel `0` at `(1, 0)`, channel `3` at `(3, 1)`; `Φ c'` = channel
`1` at `(0, 1)`, channel `4` at `(0, 3)` — exactly as recorded. Then
(`hb3a_block_state_not_closed`), for every block `β` and **every** channel weight `w` — in
particular for `(hexSum β 1, hexSum β d₁, hexSum β d₂)` — the block charges of `c` and `c'` agree
at `t` and at `t − 1` (`t − 1` being `Φ⁻¹` of each, as the sector dictates): at `t` both give
`w₀ + w₃` on block `(0, 0)` and `0` elsewhere; at `t − 1` both give `w₃` on block `(0, 0)`, `w₀` on
block `(1, 0)`, `0` elsewhere. At `t + 1` the momentum component `P₁` on block `(0, 0)` is `1` for
`c` and `0` for `c'`. **Equal coarse two-time states, different coarse states at `t + 1`.**
Consequently there is no coarse rule `Ψ` with
`hexSum β w (Φ c) = Ψ (blocks at t, blocks at t − 1) β w` for all `c`, the blocks carrying
`(hexSum β 1, hexSum β d₁, hexSum β d₂)` (`hb3a_no_closure`). **Positive (non-closure), full
strength; reached at kernel level** — the recorded witness arithmetic was correct, no larger
witness was sought, and the frozen fallback was not used. The recorded bounded search at
`L = 2, b = 1` and `L = 3, b = 1` is not a closure control, and the round claims nothing about
those sizes.

**`HB3-b`.** For every `m : ℤ` and `p : ℤ × ℤ`, `hexGas L` maps
`{c | hexSum univ 1 c = m ∧ (hexSum univ d₁ c, hexSum univ d₂ c) = p}` bijectively onto itself
(`hexGas_bijOn_sector`, a `Set.BijOn`), so the counting measure on each charge sector is
`Φ`-invariant. Immediate from `HB1-c` and bijectivity. **Positive, full strength.** **The
reading, frozen:** this is the exact statement that sits beneath any local-equilibrium hypothesis
for the candidate, and it is **all** the round says in that direction: it licenses no ergodicity,
mixing or equidistribution statement within a sector, and if the candidate carries further
invariants (hazard 4) the sectors decompose further and any such statement would have to be
about the finer pieces.

**Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
of a statistical closure at some other scale or in some other variable; no local-equilibrium or
mixing statement is made in either direction (hazard 9). **No timescale is preregistered and none
is asserted**: no relation between a collision time, a block-crossing time and a hydrodynamic time
appears as a hypothesis or as a finding (hazard 10), and the memory diagnostic is exactly what its
statement says — this block variable needs more than its own two-time state to predict its next
value.

## The scaling skeleton, inherited

H-A's `H4a` skeleton — lattice spacing as a function of `L`, time step, field normalization and
lift, carrier growth, convergence topology — is inherited unchanged and is not a target of this
round; evidence type "prose/source audit" (programme control 9). The candidate fixes **one** of
its five choices: the field lift is the integer count of Boolean occupations, `(c i k).val`, fixed
by the construction. The other four — the lattice spacing as a function of `L`, the time step,
the carrier growth and the convergence topology — remain unfixed. **Reported status for H4: HO.**
No limit is taken and no PDE is written.

## The programme-level reading, verbatim from the freeze and conditional

> inside the kernel's `Substratum` interface, consumed unmodified, there is a finite,
> deterministic, reversible, translation-covariant rule of degree `6` whose invariant graph sector
> carries a streaming-and-collision gas with **exactly conserved mass and momentum on every
> configuration for every lattice size**, with **no other site-independent channel-weighted
> invariant**, and with a stencil whose fourth moment is **rotation-isotropic** and whose sixth is
> not; the rule is **not additive**, so H-A's linearity gate does not apply to it, and H-A's
> `q`-gauge finding has no analogue for it because it carries no free alphabet parameter. The
> candidate is compatible with A1–A4 as the kernel states them and lies in the class obtained by
> dropping A5's amplitude-scale gauge principle; **whether that class is admissible as an OI
> substratum is an owner decision this round does not make.** H3 and H4 remain HO; the round says
> nothing about H5–H7, nothing about `d = 3`, and nothing about the OI → QM chain. **This reading
> is conditional on every qualifier above**, and the execution may not shorten it.

The execution does not shorten it. Each qualifier is carried by a theorem statement: the sector
relation as the hypothesis of `hexSubstratum_sector` and `hexSum_leap_sector`, the class of
site-independent channel-weighted totals as the shape of `hexSum` in `hexSum_hexGas_iff`, the
fourth and sixth orders as the two moments actually stated, and the A5 failure as
`hexSubstratum_not_A5`.

## What these outcomes do NOT license

- **Nothing here bears on the OI → QM chain**, on Track B's `P0`, on Bell, or on gravity —
  control 1. No Track B label is imported as evidence here and none of these findings is exported
  there (hazard 12).
- **Nothing here says H-A's wave representative is wrong for any other purpose.** H-A's findings
  stand as stated for that representative and that class of coarse variables; the present
  candidate is a different object, chosen for a different question, and its A5 failure is not a
  criticism of the manuscripts' linear rule, which A5 is there to secure.
- **Nothing here says OI yields Navier–Stokes.** The programme's control 2 applies: a lattice gas
  with the right conservation laws and stencil is not a hydrodynamic limit, and the candidate is
  not shown to be selected by OI. "OI has a fluid" is not said here, in any form (hazard 2).
- **Nothing here is a continuum statement.** No PDE limit is asserted, no scaling map is fixed
  beyond the field lift, no Euler or Navier–Stokes equation is written, and the
  continuum-breakdown branch (S1–S5) stays closed until H4–H7 exist, per the programme's
  control 5 (hazard 13).
- **No timescale separation is asserted.** No collision, block or hydrodynamic time is named as a
  hypothesis or a finding.
- **Nothing here changes A1–A6 or their status.** A6 remains a GAP on its own branch; the wave
  representative's A1–A5 are consumed as proved; the candidate's A-profile is a fact about the
  candidate.
- **The alphabet-as-gauge and amplitude-scale-gauge principles are consumed as the manuscripts
  state them, not tested.** The candidate's fixed alphabet and its non-additivity are recorded
  against them; **whether either disqualifies the candidate as an OI substratum is not decided
  here — the owner decision on A5 is open.**
- **No manuscript is edited by this round.** Publication-facing claims wait, per the programme's
  control 10.
- **Nothing about `d = 3`.** The candidate is two-dimensional because that is where the least
  fourth-order-isotropic stencil lives (hazard 1); **a three-dimensional candidate of the same
  type is the successor question** if this round's class is ruled admissible, and is not begun
  here.

## The chronology control

**`R7-HYB` certifies the strong property**, reusing act 10's mechanism by name through
`R7-HYA`'s shape:

- the preregistration blob is pinned **by content** to `37cc9dae301ee10d55adb73b296aa2fc7d0578e3`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = 8de0478ef31fe4cabcf89fc5787f80f38376a957` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze
  side history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it;
- **archive mode is prepared and not yet entered**: `_HYB_SEALED_HEAD` and `_HYB_MERGE` are `None`
  in this PR, so the guard certifies the run's real target; once the sealed execution head and the
  merge commit that carries it are pinned, the guard re-runs the same strong check against that
  object and requires both reachable from the current target, fail-closed (clause 7).

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** **The claim is scoped to the repository record.** The preregistration blob was
merged alone, before any execution-specific H-B object entered the tree; the single permitted
exception — recorded items 1–7 inside the control plane itself — is the analysis the kernel
re-derives above. **One discrepancy between the preregistration's recorded analysis and the
execution was found and is recorded above**: the sign of `b₁` in recorded item 2's closed form
(`w₁ − w₂`, not `w₂ − w₁`); it affects no target's statement, and **the preregistration is
unamended**.

## Definition budget: **EIGHT of the frozen eight slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `hexDir` | **fired** |
| 2 | `hexCollide` | **fired** — a product of three transpositions, so the inverse is explicit |
| 3 | `hexStream` | **fired** |
| 4 | `hexGas` | **fired** |
| 5 | `hexSubstratum` | **fired** — its `Rule` built inline |
| 6 | `hexSum` | **fired** |
| 7 | `hexMoment4` | **fired** |
| 8 (conditional) | `hexRot` | **fired** — `HB1-e` was attempted, and reached, at kernel level |

**No ninth definition was introduced.** No witness configuration, block partition instance,
trajectory, weight vector or charge sector is a top-level definition — each is a bound variable
pinned by an equation in the statement that needs it; the graph sector `Γ` is written as the
predicate `prevOf x = (hexGas L).symm (curOf x)` inside each statement; the block of a site is
written as the filter `(fun j => (i j).val / 2) = β` inside each statement; the second and sixth
moments are written inline. `HydroSourceAudit`'s, `CubicIsotropy`'s and
`SubstratumInterfaceAudit`'s definitions are reused, not redefined.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked, for `HB0`, `HB1-a`–`HB1-e`, `HB2`, `HB3-a` and `HB3-b`.
Seventy-one named results, **no `sorry`, no `axiom`, no `native_decide`**, every axiom line
within `{propext, Classical.choice, Quot.sound}` — four decidable stencil facts depend on
`[propext]` alone and four definitional lemmas on `[propext, Quot.sound]`, which the kernel
reports as such and is recorded as such. `decide` over finite types is used for the 64-state and
sixteen-site checks, as the freeze permits.

| Result | Axioms |
| --- | --- |
| `hexDir_add_three` | `[propext]` |
| `hexDir_cast_add_three` | `[propext, Quot.sound]` |
| `hexDir_add_one` | `[propext]` |
| `hexDir_sub_one` | `[propext]` |
| `hexDir_conditions` | `[propext]` |
| `hexCollide_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_moved` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_of_ne` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_symm_of_ne` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_moved_support` | `[propext, Quot.sound]` |
| `hexCollide_of_single` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_symm_of_single` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_zero` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_channel_rot` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_not_reflection` | `[propext, Classical.choice, Quot.sound]` |
| `hexStream_apply` | `[propext, Quot.sound]` |
| `hexGas_eq` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_symm_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_F` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_N` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A1` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A2` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A3` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A4Exact` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A4` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_single` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_single_site` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_two_sites` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_neg_weight` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_add_weight` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_intCast_two` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_add_intCast_two` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_hexStream` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_conserved_iff` | `[propext, Classical.choice, Quot.sound]` |
| `collide_single` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_collide_iff` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_conditions_iff_span` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_hexGas` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_hexGas_iff` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_hexGas_iff_span` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_mass_hexGas` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_momentum_hexGas` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_shiftBy` | `[propext, Classical.choice, Quot.sound]` |
| `single_channel_zero` | `[propext, Quot.sound]` |
| `hexGas_single_channel` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_symm_single_channel` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_symm_channel_one` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_A5_witness` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_not_A5` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_sector` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_leap_sector` | `[propext, Classical.choice, Quot.sound]` |
| `hexSubstratum_mass_not_conserved_off_sector` | `[propext, Classical.choice, Quot.sound]` |
| `hexMoment2_eq` | `[propext, Classical.choice, Quot.sound]` |
| `hexMoment4_eq` | `[propext, Classical.choice, Quot.sound]` |
| `hexMoment4_quartic` | `[propext, Classical.choice, Quot.sound]` |
| `hexMoment4_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `axisMoment4_two_not_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `hexMoment6_not_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `hb3a_gas_values` | `[propext, Classical.choice, Quot.sound]` |
| `hb3a_mem` | `[propext, Classical.choice, Quot.sound]` |
| `hb3a_block_state_not_closed` | `[propext, Classical.choice, Quot.sound]` |
| `hb3a_no_closure` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_bijOn_sector` | `[propext, Classical.choice, Quot.sound]` |
| `hexRot_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexRot_apply'` | `[propext, Classical.choice, Quot.sound]` |
| `hexRot_site` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_hexRot` | `[propext, Classical.choice, Quot.sound]` |
| `hexSum_hexRot` | `[propext, Classical.choice, Quot.sound]` |
| `hexRot_charges` | `[propext, Classical.choice, Quot.sound]` |

The inherited scaling skeleton is a recorded specification, evidence type "prose/source audit",
and is labelled as such above. Recorded items 1–7 are analysis, not evidence.

## What this round does not do

- **It does not report round H-B as closed**, and does not report the programme's H-B
  obligation discharged; it reports one candidate executed, in the A1–A4, ¬A5 class, with the admissibility
  of that class open.
- **It constructs no second candidate, no three-dimensional candidate, no rest-particle variant
  and no time-alternating collision.**
- **It takes no continuum limit and asserts no PDE** — that is H-C.
- **It asserts no statistical closure, mixing or local-equilibrium statement.**
- **It neither tests nor weakens the alphabet-as-gauge or amplitude-scale-gauge principles.**
- **It edits neither A1–A6 nor their kernel status.**
- **It touches no manuscript.**
- **It says nothing about Track B, Track I, Bell, or gravity**, and nothing here is evidence for
  anything there.
