# P0 — subsystem locality as a candidate selection principle: result

Research result on the planning branch of #834. It is not a native round, and nothing in it is
adopted. It is not for merge without separate review.

- **Rules.** `RULES.md` was frozen at commit `fd471a9d` (blob
  `988b4fe218dcf014f91e0f883c56dd4a3bc2a1a0`), before the script existed. Its blob is unchanged
  here.
- **Script.** `p0_exact.py`, sha256 `00cb032b71dce6eb994864e8e18bf6748192f38a644898a9c3685d453ecd155c`.
  It works in exact `ℚ(ζ₁₆)` arithmetic and imports only `itertools` and `math.gcd`.
- **Output.** `p0-exact-output.txt`, sha256
  `14428b8dd5e6008eb06bbe0e5516f05a570da056c3c9a6b20889a21f9fd58701`.
  - Two runs under Python 3.13 with `-I` gave byte-identical output.
  - 114 checks pass and none fail.

## Outcome

| token | meaning |
| --- | --- |
| `P0-SL-DISTINGUISHES-TRAJ` | some pair of `𝒪₀`-compatible lifts in different trajectory classes has the admitted one kept and the other excluded, with the excluded lift's `𝒪₁` value outside every admitted value (`C21`) |
| `P0-SL-DISTINGUISHES-THREAD` | the same within one trajectory class, at `C21` and at `CCT4` |
| `P0-SL-REDUCES-ONLY` | every main cell where the freedom is present is `REDUCES`; none is `ELIMINATES` |
| `P0-NS-HOLDS` · `P0-NS-NONVACUOUS` · `P0-NS-EQUIV-A1` | no-signalling holds on every admitted lift, fails on the frozen countercontrols, and at `|A| = 1` coincides with `SL-U` |
| `P0-NS-WEAKER` | three exact witnesses pass every no-signalling test and are excluded by `SL-U`: `Lcc`, `WW.Ke`, `Ucv` |

**The answer to the success criterion.**

- *Does subsystem locality distinguish two observationally compatible histories?*
  - It does, on both freedoms, relative to `𝒪₁`, and on `𝒪₂` and `𝒪₃` beside it. It does so at
    act 21's product configuration, with act 17's witness in each factor, and at CT4 on both
    factors.
  - *Does it select?* It does not: it reduces the freedom and never removes it.
  - The written reduction lemma states what remains. The admitted value set is exactly the
    product of the two factors' value sets.
  - So `SL-U` removes only cross-cut structure, and leaves each subsystem's own P0 freedom
    untouched.
- *What justifies it?*
  - At `|A| = 1` it is exactly prep no-signalling between the declared parts (EQ1).
  - At `|A| ≥ 2` it is strictly stronger than no-signalling. The surplus excludes hidden-sector
    correlation between the parts.

## 1. Written statements [W]

**RL (reduction).**

- *The operator identity.* `⊠` is the Kronecker product conjugated by the fixed reshuffle
  permutation. It is therefore multiplicative and commutes with `ᴴ`, so
  `(U¹_t ⊠ U²_t)(U¹_s ⊠ U²_s)ᴴ = (U¹_t U¹_sᴴ) ⊠ (U²_t U²_sᴴ)`.
- *The anchored column.* The anchor is `(a₀₁, a₀₂)`. So the anchored column `(j, a₀)` of `U¹ ⊠ U²`
  is the tensor product of the factor anchored columns.
- *Readback.* `Σ_{a₁,a₂} |U¹(i₁a₁, j₁a₀₁)|² |U²(i₂a₂, j₂a₀₂)|² = R¹(i₁,j₁) R²(i₂,j₂)`.
- *Channels.* The anchored channel of `U¹ ⊠ U²` agrees with `𝔇(U¹) ⊗ 𝔇(U²)` on product operators.
  By linearity, it equals it.
- *Hence* `𝒪ₓ(U¹ ⊠ U²) = 𝒪ₓ(U¹) ⊠ 𝒪ₓ(U²)` for `x = 0, 1, 2, 3`.
- *Coherence.* Every `Rᵏ` is column-stochastic, since `Σ_i Rᵏ(i,j) = ‖Uᵏ e_{(j,a₀)}‖² = 1`.
  - If `R¹ ⊗ R² = Γ¹ ⊗ Γ²` with every `Γᵏ` column-stochastic, summing over `i₂` gives `R¹ = Γ¹`,
    and likewise `R² = Γ²`. The converse is the product formula.
  - So the factor-1 lifts that occur in admitted lifts, with factor 2 fixed, are exactly the
    coherent lifts of `Γ¹`.

∎

**PL (locus).**

- `X_{(i₁,i₂)} = X¹_{i₁} ⊗ X²_{i₂}`, so `G^{(i)}_{jk} = G¹^{(i₁)}_{j₁k₁} G²^{(i₂)}_{j₂k₂}`. This is
  act 28's pointwise product.
- `G(Uᵏ)` is realizable at `Γᵏ` (`sh1_necessity`).
- Hence an admitted lift's class at each `t` lies in act 28's product locus.
- So a tuple violating `a28_s_locus_first_index` belongs to no admitted lift's class.

∎

**PC.** By RL, an admitted value is `A ⊗ B` in the cut reshuffle, `vec(A) vec(B)ᵀ`, which has rank at
most 1.

- If every 2×2 minor through one nonzero pivot `(p, q)` vanishes, every row is `T_{rq}/T_{pq}`
  times row `p`. So the rank is 1, and the test is complete.

∎

**NS.**

- *Interventions factorize.* `R₂ ⊗ 1_A` reshuffles to `1_{V₁×A₁} ⊠ (R₂ ⊗ 1_{A₂})`. So for an
  admitted lift, `U_t U_sᴴ (R₂ ⊗ 1_A) U_s = U¹_t ⊠ M²_R`, where
  `M²_R = U²_t U²_sᴴ (R₂ ⊗ 1) U²_s`.
- *Tracing out factor 2.* Its anchored channel is `𝔇(U¹_t) ⊗ 𝔇(M²_R)`. `𝔇(M²_R)` preserves the
  trace, so `Tr_{V₂}` of the response is `𝔇(U¹_t)(Tr_{V₂} ρ)`.
- *Conclusion.* The response is independent of `R₂`, and depends on a product preparation's second
  factor only through its trace. The same holds with the factors exchanged.

∎

**EQ1.** Let `|A| = 1` and `Tr_{V₂}[U(ρ₁ ⊗ ρ₂)Uᴴ]` be independent of `ρ₂`.

- *The image of `B(V₁) ⊗ 1`.* For `X₁` on `V₁`, set `Y = Uᴴ(X₁ ⊗ 1)U`. Then `Tr[Y(ρ₁ ⊗ ρ₂)]`
  does not depend on `ρ₂`. So `Tr_{V₁}[Y(ρ₁ ⊗ 1)] ∝ 1` for every `ρ₁`, and `Y ∈ B(V₁) ⊗ 1`.
- *Bijectivity.* `X ↦ UᴴXU` is an injective `*`-homomorphism of `B(V₁) ⊗ 1` into itself. It is
  therefore bijective, and it maps the commutant `1 ⊗ B(V₂)` onto itself.
- *Inner restrictions.* By Skolem–Noether both restrictions are inner, by `V₁` and `V₂`. Then
  `Uᴴ(X₁ ⊗ X₂)U = (V₁ ⊗ V₂)ᴴ(X₁ ⊗ X₂)(V₁ ⊗ V₂)` for all `X₁, X₂`.
- *Conclusion.* `U(V₁ ⊗ V₂)ᴴ` is central, so `U = λ(V₁ ⊗ V₂)`.

With RL, `SL-U` at `|A| = 1` holds iff prep no-signalling holds in one direction at every `t`. ∎

**HZ.** For `(U₀, U₁)` with `U_t = U₁` for `t ≥ 1`, every value at `(t,s)` equals the value at
`(min(t,1), min(s,1))`. For `s ≥ 1`, `U_t U_sᴴ = 1`. ∎

**The `CELIM` point.**

- The admitted lifts are `D_t ⊠ U²_t`, where `D_t` is a diagonal phase. That is forced by
  `|D_t|² = 1` on `Fin 2` with `|A₁| = 1`.
- So `U_t U_sᴴ = (D_t D_sᴴ) ⊠ (U²_t U²_sᴴ)`. Its readback is
  `δ_{ij} Σ_{a₂} |(U²_t U²_sᴴ)(a₂, 0)|² = δ_{ij}`.

∎

**Sesquilinear certificate.** Take a unitary `R₂ = Σ r_{cd} E_{cd}`.

- The response is `Σ r_{cd} conj(r_{ef}) B(E_{cd}, E_{ef})`.
- If `B(E_{cd}, E_{ef}) = δ_{ce} β(d,f)`, this sum is `Σ_{d,f} β(d,f)(R₂ᴴR₂)_{fd} = Σ_d β(d,d)`.
- That value is independent of `R₂`, and equals the value at `R₂ = 1`.

∎

## 2. Measurements (exact)

All status checks hold:

- each lift is unitary and admissible at `t = 0, 1`;
- each lift's computed `SL-U` status equals the frozen table's;
- each `TRAJ` pair is certified inequivalent at `t = 1`;
- each `THREAD` pair is certified equivalent at `t = 0, 1` by its exhibited `D_t`.

The `TRAJ` inequivalences of `F` and `PF` are certified by `a28_s_locus_first_index`, at fibres
`(0,0)` and `(1,0)` with indices `(0,0)` and `(0,1)`: `1/16` against `i/16`. The others are certified
by `Ψ`, `1/256` against `i/256`.

**Pair verdicts at the main configurations.** `PHYS` = `SEP-PHYS`, `REP` = `SEP-REP`, `KEEP` =
`KEEP-BOTH`.

| config | freedom | pair [component] | `𝒪₁` | `𝒪₂` | `𝒪₃` |
| --- | --- | --- | --- | --- | --- |
| `C21` | `TRAJ` | `(P,F)` | PHYS | REP | REP |
| | | `(P,T)` | PHYS | REP | REP |
| | | `(P,PF)` | PHYS | PHYS | PHYS |
| | | `(P,Q)` | KEEP | SAME | SAME |
| | | `(P,PQ)` | KEEP | KEEP | KEEP |
| `C21` | `THREAD` | `(P,Wd.P)` [L] | PHYS | REP | REP |
| | | `(P,Wp.P)` [L] | KEEP | SAME | SAME |
| | | `(PQ,Wd.PQ)` [L] | PHYS | REP | PHYS |
| | | `(PQ,Wp.PQ)` [L] | KEEP | SAME | KEEP |
| | | `(PQ,PQ.Dn)` [D] | PHYS | PHYS | PHYS |
| | | `(PQ,PQ.Dp)` [D] | KEEP | KEEP | KEEP |
| `CCT4` | `THREAD` | `(I,Lcc)` [L] | PHYS | REP | REP |
| | | `(I,Llp)` [L] | KEEP | SAME | SAME |
| | | `(X,We.X)` [L] | PHYS | PHYS | PHYS |
| | | `(X,W1.X)` [L] | KEEP | KEEP | KEEP |
| | | `(WW,WW.Ke)` [S] | REP | PHYS | PHYS |
| | | `(WW,WW.X1)` [S] | SAME | KEEP | KEEP |

**Cells.**

- Every `C21` cell and every `CCT4 THREAD` cell is `REDUCES`, on every carrier.
- `CCT4 TRAJ` is `UNCHANGED (absent)`: every lift's tuple is the SH1-C2 closed form.
- `C1A` and `C1B` are `UNCHANGED (present)` on every carrier.
- `CELIM THREAD 𝒪₂` is `ELIMINATES`. Its `𝒪₁` and `𝒪₃` cells are `UNDETERMINED`, since no
  written argument fixes the admitted values there.
- `CENT` and `CCC` are `EXCLUDES-ALL`.

**No-signalling.**

| lift | `SL-U` | prep `t=0` | prep `t=1` | intervention `s=0, t=1` |
| --- | --- | --- | --- | --- |
| `C21`: `P`, `Q`, `PQ`, `Wp.P`, `Wp.PQ`, `PQ.Dp` | yes | holds | holds | holds (24 permutations each way) |
| `C21`: `F`, `T`, `Wd.P`, `Wd.PQ` | no | violated | violated | not run |
| `C21`: `PF`, `PQ.Dn` | no | holds | violated | `PF`: violated, by `(0,1,3,2)` on `V₂` |
| `CCT4`: `I`, `X`, `W1.X`, `Llp`, `WW`, `WW.X1` | yes | holds | holds | holds (every unitary) |
| `CCT4`: `We.X` | no | violated | violated | violated |
| `CCT4`: `Lcc`, `WW.Ke` | no | holds | holds | holds (every unitary) |
| `CENT`: `CN` | no | violated | violated | holds (constant lift) |
| `CCC`: `Ucv` | no | holds | holds | holds (every unitary) |

**Controls.** All are green:

- K0;
- K-frozen: act 17's `1/16` against `i/16`; CT4's `1` against `0`; act 28's `1/16` against `i/16`;
- K-17-embed;
- K-single;
- K-unique;
- K-reach;
- K-cert: rank 1 on every admitted value; rank ≥ 2 on `F₁₆` and on the one-entry mutation;
- K-indep:
  - `𝒪₀` and `𝒪₂` are the diagonal actions of `𝒪₁` and `𝒪₃` on every lift;
  - the dilation route agrees with the defining sum on every lift with `|A| ≥ 2`, and on `P` and
    `F`;
  - at `|A| = 1` the two routes coincide symbolically, so the remaining `C21` lifts add no
    independent check.

## 3. Findings

Each finding was pressure-tested against the reading least favourable to `SL-U`.

**F1. `SL-U` distinguishes, and the distinction is physical relative to `𝒪₁`.**

- *The trajectory freedom (`C21`).*
  - `F` and `T` are coherent lifts of `Γ ≡ 1/16` whose classes lie off act 28's product locus.
  - Their `𝒪₁` values are non-product, so no admitted lift reproduces them.
  - `PF` is excluded on all three carriers.
- *The threading freedom.* Three things move `𝒪₁`, and in each case the non-product variant is
  excluded while the product variant survives:
  - left moves at `C21`;
  - anchored phases at `C21`;
  - left moves at `CCT4`.
- *What is not shown.* These are distinctions between histories the visible law cannot tell
  apart. They are made only under the premise that the parts are uncoupled, and `𝒪₀` cannot check
  that premise when `Γ` is a product.

**F2. `SL-U` reduces and does not select.**

- In every main cell where the freedom is present, an admitted pair survives with distinct values:
  - `(P,Q)` and `(P,PQ)`: act 17's freedom;
  - `(X,W1.X)`: CT4's freedom;
  - `(WW,WW.X1)`: a strong right move;
  - `(I,Llp)` and `(PQ,PQ.Dp)`.
- By RL this is forced. The admitted value set is the product of the factor sets.
- So `SL-U` can only remove what crosses the cut. On one system it is vacuous (K-single).
- The single-system freedom that act 17 and act 13 exhibit passes through it unchanged.

**F3. On the two-time carriers, constant lifts hide the trajectory freedom.**

- `(P,F)` and `(P,T)` are `SEP-REP` on `𝒪₂` and `𝒪₃`: every constant lift has the identity there.
- So a trajectory difference between constant lifts is visible on `𝒪₁` only.
- The strong-right component behaves the other way: `(WW,WW.Ke)` is `SEP-REP` on `𝒪₁`, consistent
  with CT3(G), and `SEP-PHYS` on `𝒪₂` and `𝒪₃`. Its exclusion is therefore visible only under the
  re-anchoring presupposition.
- Which part of `SL-U`'s exclusions counts as physical depends on the carrier. That is act 14's
  rule, now measured for one principle.

**F4. At `|A| = 1`, `SL-U` coincides with operational no-signalling (EQ1).**

- Every `C21` lift that is not admitted signals by preparation at some `t`.
- At this configuration, `SL-U` therefore adds nothing to "varying the preparation of one part does
  not change the other part's reduced state".
- It inherits that principle's justification. Relativistic causality, or physically uncoupled
  parts, motivates it independently of the P0 problem.
- So the T1-type exclusions at act 17's witness are operational.

**F5. At `|A| ≥ 2`, no-signalling does not imply `SL-U`, and the surplus is a hidden-sector
premise.** Three exact witnesses pass prep and intervention no-signalling, in both directions and
for every visible unitary, and are excluded by `SL-U`:

- **`Lcc` (`CCT4`).** A hidden entangler in each fibre produces correlated partial dephasing,
  `ρ ↦ (9/25)ρ + (16/25)(Z⊗Z)ρ(Z⊗Z)`. Its `𝒪₁` is non-product.
- **`WW.Ke` (`CCT4`).** An entangling strong right move, visible on `𝒪₂` and `𝒪₃` only.
- **`Ucv` (`CCC`).** Its visible law `(9/25)·1 + (16/25)(X_v ⊠ X_v)` is not a product. `SL-U`
  excludes every lift of it, while no-signalling admits it.

What these show:

- The consequence of `SL-U` that no-signalling does not restate is the absence of correlation
  between the parts' hidden sectors. It is visible as product visible noise (`𝒪₁`), and as a
  product visible law (`𝒪₀`).
- *In ordinary quantum mechanics.* Two systems that do not interact but share an environment do
  show correlated noise of this kind. `SL-U` matches ordinary quantum mechanics only when
  "uncoupled" includes "separate, uncorrelated environments".
- So at `|A| ≥ 2`, part of what `SL-U` excludes rests on a premise about OI's hidden sector, not on
  an operational principle.

**Classification.**

- F1 and F2 are ELABORATING: act 28's properness, carried to lift level and to carriers.
- F4 is POSITIVE: it gives an operational characterization at `|A| = 1`.
- F3 and F5 are NEW:
  - F3: which carriers see which of `SL-U`'s exclusions;
  - F5: the hidden-sector separability content of `SL-U`, with a visible-law witness.
- Assumption-watch marker for later P0 candidates: *a locality principle stated on dilations
  constrains the hidden sector; at `|A| ≥ 2`, check whether no-signalling alone already justifies
  its exclusions.*

## 4. Against the owner's requirements

- **A.**
  - `SL-U` constrains both freedoms, reducing each: `TRAJ` at `C21`; `THREAD` at `C21` and `CCT4`.
    Within `THREAD`, it constrains every component (L, S and D).
  - Neither freedom was quotiented as gauge. Each verdict is per carrier, and `SEP-REP` records
    where an exclusion is invisible.
- **B.**
  - The tested notion is the common content of strict-cone and Lieb–Robinson locality on a cut
    that no edge crosses.
  - It excludes no evolution of uncoupled systems with separate environments.
  - Coupled cuts are not tested.
- **C.** The observables, preparations and interventions were fixed in `RULES.md` §6 before the
  runs.
  - No-signalling is a consequence of `SL-U` (NS), and is not vacuous.
  - At `|A| = 1` it is equivalent to `SL-U`, so there it is an operational restatement, not an
    independent prediction.
  - At `|A| ≥ 2` it is strictly weaker. The consequence that is not a restatement is F5's: product
    visible laws and product visible noise for uncoupled parts, which no-signalling does not imply.
    Matching ordinary quantum mechanics there is consistency, not correctness (§A.23).
- **Act 17's witness**, embedded without restriction (K-17-embed):
  - the factor lifts are unrestricted;
  - the composite scope is every coherent lift;
  - the invariant survives;
  - the only added structure is the declared decomposition.

## 5. Sourcing obligations (unresolved)

- **(i) The decomposition.** `V ≅ V₁ × V₂` is input. At `C21` every identification makes `Γ` a
  product.
- **(ii) The hidden sector.** `A ≅ A₁ × A₂`, with a product anchor. This is vacuous at `|A| = 1`,
  and it is all of F5's surplus at `|A| ≥ 2`.
- **(iii) The uncoupled premise.** `𝒪₀` cannot check it when `Γ` is a product.
- **(iv) The carriers' presuppositions.**
  - Re-anchoring for `𝒪₂` and `𝒪₃`, which F3 shows to carry the strong-right exclusions.
  - The composition `U_t U_sᴴ` for the intervention response.
- **E1-L.** Its rule for absent couplings is a candidate source of `SL-U` across a cut that no edge
  crosses, at the substratum level. It is not a source: no map from E1-L's register to Track B's
  dilation carrier exists.

## 6. Open, and non-claims

**Open.**

- Coupled cuts: `L-disc` and `L-cont` with crossing edges. This includes the F2-3 question of
  `RULES.md` §9.
- `TRAJ` at `|A| ≥ 2`. The only `|A| ≥ 2` main configuration is deterministic, so its trajectory
  freedom is absent.
- Identifications other than the declared ones.
- Interventions that are not visible unitaries.
- Intervention no-signalling at `C21`, beyond the permutation spot check. That case is covered by
  NS [W].
- Kernel proofs of RL, EQ1 and NS.

**Non-claims.**

- No carrier, locality notion or source factorization is adopted.
- No outcome is claimed beyond its configuration, pairs and carrier.
- Nothing says whether nature satisfies `SL-U`.
- Nothing says whether any other principle selects quantum dynamics.
