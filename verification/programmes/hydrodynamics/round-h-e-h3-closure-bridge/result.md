# Hydrodynamics round H-E — H3 as a candidate bridge condition toward closure: RESULT

Executed under the frozen control plane `preregistration.md` in this directory, blob
`9f3f4ff4115c8d95215462acd257b4f6b32c9926`, from `main` at
`0975bbab380b26cd2bb06ec65ed68f8bcc23937f` — the merge commit of that control plane's pull request
#633, which the freeze fixes as this round's **mandated execution base**. The first recorded act of
this execution was verifying that blob at that base; it matches.

**This is a SEALING round** in `AGENTS.md` `§A.37`'s terms: it creates the Lean module
`verification/lean-mathlib/OIBridge/HydroClosureBridge.lean` and the guard section `R7-HYE` in
`verification/lean/edge_rigidity_probe.py`, and that guard section carries this round's own seal
constants. In this execution commit `_HYE_BASE` is the mandated base,
`_HYE_SEALED_HEAD` is `None` and `_HYE_MERGE` is `None`; **archive mode is prepared and not yet
entered**, and the pin commit `P` sets the two. **No existing seal constant is altered by this
round**, and no existing guard section is altered.

## Outcome at a glance

**Every target landed at its predicted sign, and every kernel target landed at evidence level 2.**
`HE2-f` landed in its **global** form, so its frozen local fallback was **not** used, and `HE2-b`'s
frozen fallback — the direct 64-state case analysis at real parameters — was **not** used either.
**No target is UNDECIDED, and no target landed against its preregistered sign.**

| target | outcome | predicted | evidence |
| --- | --- | --- | --- |
| `HE0` | positive | positive, high | prose/source audit, type P |
| `HE1` | positive | positive, high | prose/source audit, type P |
| `HE2-a` | positive | positive, high | level 2, `hexLocalWeight_hexFugacity` |
| `HE2-b` | positive | positive, medium | level 2, `hexLocalWeight_hexCollide` |
| `HE2-c` | positive | positive, high | level 2, `hexConfWeight_hexStream` |
| `HE2-d` | positive | positive, medium | level 2, `hexConfWeight_hexGas` |
| `HE2-e` | positive | positive, high | level 2, `hexFamilyFlux_apply`, `hexFamilyFlux_isotropic` |
| `HE2-f` | positive, **global** | positive, high | level 2, `hexMeanCharge_injective` |
| `HE3` | `HE3-holds` | `HE3-holds`, medium | assembled, no evidence of its own |
| `HE4-a` | positive | positive, high | level 2, `hexStream_clauses_and_six_invariants` |
| `HE4-b` | positive | positive, high | level 2, `hexConfWeight_site_dependent_not_invariant` |
| `HE5` | `HE5-unstatable` | `HE5-unstatable`, high | prose/source audit, type P |
| `HE6` | `HE6-component` | `HE6-component`, medium | assembled, no evidence of its own |

**`HE0`, `HE1` and `HE5` carry no kernel evidence and are not part of the axiom table.** They are
determinations by locating and quoting under the freeze's evidence rule; each is carried below by a
verbatim quotation with a file-and-line coordinate, or by a recorded statement that the passage
sought does not exist on a named and bounded search. **`HE3` and `HE6` are assembled determinations
and add no evidence of their own.**

## The exclusion, carried

**The status of A5 relative to the hydrodynamic target is round H-D's lane, and this round does not
re-open it, does not re-decide it, and does not consume it as settled.** No target of this round
reads `round-h-d-a5-status-adjudication/`, no manuscript is read, and `A5`, `hexSubstratum_A5_witness`
and `hexSubstratum_not_A5` are consumed by no target and carry no finding here. That round H-B's
candidate lies in the class obtained by dropping A5's amplitude-scale gauge principle is taken as a
recorded fact about the candidate and no question is asked about it.

> **THE H-B GUARDRAIL SENTENCE, carried at this mention, where H-B is consumed as the source of the
> candidate:** H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with
> the right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
> Euler/Navier–Stokes limit.

## `HE0` — the record's boundary, located and quoted

**Evidence type: prose/source audit, type P.** Each item below is a verbatim quotation with its
coordinate. **The bounded search is the four pinned round artifacts** —
`../round-h-a-source-audit/preregistration.md`, `../round-h-a-source-audit/result.md`,
`../round-h-b-reversible-fluid-substratum/preregistration.md` and
`../round-h-b-reversible-fluid-substratum/result.md` — **together with `../PROGRAMME.md`**, all at
the mandated base. No manuscript is read.

### `HE0-i` — every sentence reporting a status for the H3 obligation

H-A, `../round-h-a-source-audit/result.md` lines 220–225:

> **Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
> of a statistical closure at some other scale or in some other variable, and no local-equilibrium or
> mixing statement is made in either direction (hazard 7). **No relation `τ_B ≪ τ_S` is
> preregistered**, no timescale is asserted (hazard 8), and the memory diagnostic is exactly what its
> statement says: this block variable needs more than its own two-time state to predict its next
> value.

H-B, `../round-h-b-reversible-fluid-substratum/result.md` lines 303–309:

> **Reported status for H3: HO.** Non-closure of one exact coarse observable is not an impossibility
> of a statistical closure at some other scale or in some other variable; no local-equilibrium or
> mixing statement is made in either direction (hazard 9). **No timescale is preregistered and none
> is asserted**: no relation between a collision time, a block-crossing time and a hydrodynamic time
> appears as a hypothesis or as a finding (hazard 10), and the memory diagnostic is exactly what its
> statement says — this block variable needs more than its own two-time state to predict its next
> value.

H-B, `../round-h-b-reversible-fluid-substratum/result.md` line 332, inside the programme-level
reading it carries verbatim from its own freeze:

> H3 and H4 remain HO; the round says
> nothing about H5–H7, nothing about `d = 3`, and nothing about the OI → QM chain.

Both located. **No further sentence reporting a status for H3 exists on the searched record**: the
search was `H3` over the five files named above, and the remaining occurrences are the label of
H-A's `H3a` target section, the programme's own H3 obligation text at `../PROGRAMME.md` lines 69–71,
and the evidence-level lines that name `H3a`/`HB3-a` as kernel targets.

### `HE0-ii` — every sentence declaring what the sector-measure, block-variable or mixing content does not license

H-B, `../round-h-b-reversible-fluid-substratum/result.md` lines 293–301:

> **`HB3-b`.** For every `m : ℤ` and `p : ℤ × ℤ`, `hexGas L` maps
> `{c | hexSum univ 1 c = m ∧ (hexSum univ d₁ c, hexSum univ d₂ c) = p}` bijectively onto itself
> (`hexGas_bijOn_sector`, a `Set.BijOn`), so the counting measure on each charge sector is
> `Φ`-invariant. Immediate from `HB1-c` and bijectivity. **Positive, full strength.** **The
> reading, frozen:** this is the exact statement that sits beneath any local-equilibrium hypothesis
> for the candidate, and it is **all** the round says in that direction: it licenses no ergodicity,
> mixing or equidistribution statement within a sector, and if the candidate carries further
> invariants (hazard 4) the sectors decompose further and any such statement would have to be
> about the finer pieces.

The two H3-status passages quoted under `HE0-i` are themselves the block-variable non-licences, in
both rounds' own words, and are not requoted here. H-B,
`../round-h-b-reversible-fluid-substratum/result.md` lines 289–291, adds the bound on its own
recorded search:

> The recorded bounded search at
> `L = 2, b = 1` and `L = 3, b = 1` is not a closure control, and the round claims nothing about
> those sizes.

### `HE0-iii` — H-A's `H4a` five-item skeleton, and its statement that none is fixed

`../round-h-a-source-audit/result.md` lines 229–243:

> Not a theorem, and no theorem is claimed; evidence type "prose/source audit" (programme control 9).
> A continuum map for this substratum must fix, before any PDE statement is meaningful:
>
> 1. the lattice spacing as a function of `L`;
> 2. the time step;
> 3. the field normalization — including how `ZMod q` values are lifted (to `ℤ`, to `ℝ`, or otherwise)
>    and rescaled;
> 4. the carrier growth — how `L`, `q` and the coarse-graining scale are taken together;
> 5. the topology in which convergence would be claimed.
>
> **None is fixed by the manuscripts or by A1–A6.** [SM §4.1] fixes the rule and [SM §2.7] the
> alphabet as gauge; neither names a spacing, a time step, a lift, a joint growth, or a norm, and
> `waveSubstratum_A1`–`A5` are statements at one finite `L` and `q`. **Reported status for H4: HO**,
> with the skeleton as the deliverable. No limit is taken and no PDE is written.

### `HE0-iv` — H-B's record of which one of the five its candidate fixes

`../round-h-b-reversible-fluid-substratum/result.md` lines 313–319:

> H-A's `H4a` skeleton — lattice spacing as a function of `L`, time step, field normalization and
> lift, carrier growth, convergence topology — is inherited unchanged and is not a target of this
> round; evidence type "prose/source audit" (programme control 9). The candidate fixes **one** of
> its five choices: the field lift is the integer count of Boolean occupations, `(c i k).val`, fixed
> by the construction. The other four — the lattice spacing as a function of `L`, the time step,
> the carrier growth and the convergence topology — remain unfixed. **Reported status for H4: HO.**
> No limit is taken and no PDE is written.

### `HE0-v` — both rounds' conditional statements about the stencil-to-stress bridge

H-A, `../round-h-a-source-audit/result.md` lines 178–182:

> **Reported status for H2: exact stencil anisotropy proved; conditional HI if H5's stress closure
> consumes this tensor; otherwise H2 remains HO.** Whether the bare fourth moment of the stencil is
> the effective rank-4 tensor the H5 stress closure consumes is a bridge this round does **not**
> build; until it lands, the anisotropy is a proved fact about the stencil and a *conditional* finding
> about hydrodynamics, and the round does not label the isotropy obligation HI outright (hazard 5).

H-B, `../round-h-b-reversible-fluid-substratum/result.md` lines 257–261:

> **Reported status for H2: the stencil's fourth moment is proved isotropic — HD for the stencil
> tensor; for the hydrodynamic stress, HC conditional on H5's closure consuming this tensor,
> otherwise HO.** As in H-A, whether the bare fourth moment of the stencil is the rank-4 tensor the
> H5 stress closure consumes is a bridge this round does **not** build; the round labels the stencil
> and not the obligation (hazard 5).

### `HE0` — the determination

Every listed item is located and quoted with its coordinate, and none is recorded absent.

**The boundary of the merged record on closure, local equilibrium, mixing and scaling is located and
quoted with coordinates, and every listed passage is present at the mandated base.**

## `HE1` — the closure gap, enumerated from the merged record

**Evidence type: prose/source audit, type P**, same bounded search as `HE0`. The freeze's four items
are its own reading and are not evidence; each is re-established below by quotation.

**1. The flux term is not a function of the coarse state.**
`../round-h-b-reversible-fluid-substratum/result.md` lines 283–288:

> At `t + 1` the momentum component `P₁` on block `(0, 0)` is `1` for
> `c` and `0` for `c'`. **Equal coarse two-time states, different coarse states at `t + 1`.**
> Consequently there is no coarse rule `Ψ` with
> `hexSum β w (Φ c) = Ψ (blocks at t, blocks at t − 1) β w` for all `c`, the blocks carrying
> `(hexSum β 1, hexSum β d₁, hexSum β d₂)` (`hb3a_no_closure`). **Positive (non-closure), full
> strength; reached at kernel level**

Re-established.

**2. Nothing on the record determines that flux from coarse data, even approximately.** The sector
measure is an exact invariance of a counting measure and is declared, in H-B's result note itself, to
license no statistical statement — the passage quoted under `HE0-ii` at lines 293–301, whose own
words are that it *licenses no ergodicity, mixing or equidistribution statement within a sector*.
Both rounds' H3-status passages, quoted under `HE0-i`, add that *no local-equilibrium or mixing
statement is made in either direction*. Re-established.

**3. The scaling map is unfixed.** The two passages quoted under `HE0-iii` and `HE0-iv`:
H-A records that **none** of the five items is fixed by the manuscripts or by A1–A6, and H-B records
that its candidate fixes **one** of the five and that *the other four — the lattice spacing as a
function of `L`, the time step, the carrier growth and the convergence topology — remain unfixed*.
Re-established.

**4. The stencil-to-stress bridge is not built.** The two passages quoted under `HE0-v`: both rounds
report the isotropy status of the stress as conditional on whether H5's closure consumes the bare
fourth moment of the stencil, and each says in terms that this *is a bridge this round does **not**
build*. Re-established.

**No item of the freeze's four could not be re-established, and the execution's list of what stands
between the established microscopic facts and a closed coarse system is exactly those four.**

**One qualifier the freeze did not name, recorded rather than added to the list.** The microscopic
facts H-B establishes carry a scope qualifier in their own statements.
`../round-h-b-reversible-fluid-substratum/result.md` lines 217–219:

> Every
> conservation statement of this round is a statement on `Γ`; off `Γ`, `leap F` conserves nothing
> this round names (`HB0-c`).

**This round's reading, labelled as a reading and not as evidence: that qualifier is part of the
statement of the established facts rather than something standing between them and a closed coarse
system, so it is recorded here and is not a further entry in the enumeration.** Every sentence of
this round that speaks of those facts carries `on Γ` as H-B's statements carry it. **Whether the
qualifier should instead be enumerated as a further gap entry is a reading this round records and
does not settle.**

**What stands between the established microscopic facts and a closed coarse system is enumerated from the merged record, each entry carried by its own quotation, and the enumeration is a statement about the record and not a claim that the list is exhaustive over routes nobody has written.**

## `HE2-a`–`HE2-e` — does H3's decidable part hold for H-B's candidate?

All five at **evidence level 2**, in `OIBridge/HydroClosureBridge.lean`. Every named result prints
`[propext, Classical.choice, Quot.sound]`; there is no `sorry`, no `axiom` and no `native_decide` in
the module.

**`HE2-a` (`H3-prod`, product form) — `hexLocalWeight_hexFugacity`.** For every
`(a, b₁, b₂) : ℝ³` and every local state `v : Fin 6 → ZMod 2`,
`∏ k, z k ^ (v k).val = exp (a · m(v) + b₁ · p₁(v) + b₂ · p₂(v))`, the three charges written in
H-B's `hexSum` form at a single site with weights `1`, `d₁ = (k ↦ hexDir k 0)` and
`d₂ = (k ↦ hexDir k 1)`. **`HE2-a`: The clause landed at evidence level 2, at the scope its statement
carries, and at no wider scope.**

**`HE2-b` (the collision) — `hexLocalWeight_hexCollide`.** For every parameter triple and every `v`,
`∏ k, z k ^ (hexCollide v k).val = ∏ k, z k ^ (v k).val`. **The mechanism is H-B's collision
classification read in the exponent, reused and not re-proved**: `hexCollide_conserved_iff` applied
to the integer weights `1`, `d₁` and `d₂` (the latter two through `hexDir_conditions`) is packaged as
`hexCollide_charges`, and `HE2-a` reduces the real-parameter weight to the exponential of a real
combination of those integer charges. **The transfer went through by reuse**: the real parameters
multiply integer charges, so H-B's integer-weight statement is exactly what is needed.
**The frozen fallback — the direct 64-state case analysis at real parameters — was NOT used**, and
`HE2-d` is stated without the identity as a hypothesis. **`HE2-b`: The clause landed at evidence
level 2, at the scope its statement carries, and at no wider scope.**

**`HE2-c` (streaming) — `hexConfWeight_hexStream`.** For **site-independent** fugacities — one
vector `z`, the same at every site, which is what `hexConfWeight`'s type carries — the configuration
weight is invariant under `hexStream L`, by reindexing each channel's site product along the
translation `i ↦ i − c_k`. **The statement carries "site-independent" and this round does not drop
it anywhere.** **`HE2-c`: The clause landed at evidence level 2, at the scope its statement carries,
and at no wider scope.**

**`HE2-d` (`H3-inv`, family invariance) — `hexConfWeight_hexGas`.** For **site-independent**
fugacities, `hexConfWeight (hexFugacity a b₁ b₂) (hexGas L c) = hexConfWeight (hexFugacity a b₁ b₂) c`
for every parameter triple, every configuration and every `L` with `[NeZero L]`. The collision half
is `HE2-b`, the streaming half `HE2-c`. **The invariance is an invariance of the homogeneous family;
`HE4-b` below bounds it, and the qualifier is not dropped.** **`HE2-d`: The clause landed at
evidence level 2, at the scope its statement carries, and at no wider scope.**

**`HE2-e` (`H3-flux`, the flux in the parameters) — `hexFamilyFlux_apply` and
`hexFamilyFlux_isotropic`.** With `θ k = z k / (1 + z k)`, the tensor `Σ_k θ_k (u_k)_x (u_k)_y` over
the six embedded unit vectors is `hexFamilyFlux a b₁ b₂ x y`; `hexFamilyFlux_apply` gives it in the
fugacities written out inline, and `hexFamilyFlux_isotropic` gives
`hexFamilyFlux a 0 0 x y = 3 · (eᵃ / (1 + eᵃ)) · δ_{xy}` through H-B's `hexMoment2_eq`, consumed and
not re-proved. **The statement's variable is the parameter triple `(a, b₁, b₂)`.** It establishes a
function of the parameters and **establishes no function of the coarse charges**; what joins the two
is `HE2-f` alone, and only in `HE2-f`'s terms. **This is an identity about a family of measures on
finite configurations: it is not a stress tensor of a continuum theory, not a constitutive law, and
not a term of any equation.** **`HE2-e`: The clause landed at evidence level 2, at the scope its
statement carries, and at no wider scope.**

## `HE2-f` — Gibbs parameter identifiability

**The object, as frozen.** `hexMeanCharge : (Fin 3 → ℝ) → (Fin 3 → ℝ)` is the triple of the expected
mass and the two expected momentum components at one site under the family member `λ = (a, b₁, b₂)`,
the momentum components taken in H-B's lattice coordinates as `hexSum`'s weights `d₁`, `d₂` take
them. `hexMeanCharge_apply` writes it against the sufficient-statistic vectors
`t k = (1, (c k)₁, (c k)₂)`, spelled out inline inside the statement rather than as a definition.

**The domain is the whole of `ℝ³`, as frozen.** No parameter is restricted, no degenerate set is
excised, no compactness is assumed and no bound is placed on the triple; `hexFugacity_pos` records
that every fugacity is strictly positive at every triple.

**The form of recovery reached: GLOBAL.** `hexMeanCharge_injective` proves
`Function.Injective hexMeanCharge` at evidence level 2 — for all `λ μ : ℝ³`, `Ψ λ = Ψ μ → λ = μ`.
The kernel re-derives the mechanism the freeze recorded as analysis: `hexSigma_strictMono` gives
strict monotonicity of `σ x = eˣ / (1 + eˣ)`, `hexSigma_mul_nonneg` and `hexSigma_mul_eq_zero` give
that each of the six products `(σ ⟨t k, λ⟩ − σ ⟨t k, μ⟩) · ⟨t k, v⟩` is non-negative and vanishes only
when `⟨t k, v⟩ = 0`, `hexSpan_sum_zero` gives that their sum is the pairing of `Ψ λ − Ψ μ` with
`v = λ − μ` and so vanishes, and the three vectors `t 0`, `t 1`, `t 2` force `v = 0`.
**The frozen local fallback was NOT used, and the global statement was reached.**

**What `HE2-f` does not establish.** The image of `hexMeanCharge` is **not characterized** by this
round. That characterization is not a target here, is not attempted, and is reported **HO**. No
statement of this round places the charge data of any coarse state in the image.

> **THE `im Ψ` RESTRICTION, carried at this mention as `H3-ident` states it:** injectivity supplies a
> recovery only where a preimage exists, so `H3-ident` names exactly one family member for a triple
> of coarse charge values **lying in `im Ψ`**, and `HE2-e`'s flux identity is thereby a function of
> the charge data **on `im Ψ` and nowhere else**. The restriction is part of the clause, not a gloss
> on it. Whether any particular charge data lies in `im Ψ` is a question this round does not ask, and
> the image stays **HO**.

> **THE `im Ψ` RESTRICTION, carried at this mention as `H3-prop` states it:** where the local charge
> data leaves `im Ψ` the propagation clause says nothing, and no sentence of this round extends it by
> continuity, by approximation, or by taking the nearest family member. The restriction is part of
> the clause, not a gloss on it.

**`HE2-f`: The mean-charge map of the frozen family is injective on the whole of `ℝ³` at evidence
level 2, so a triple of mean-charge values names at most one parameter triple, and `H3-ident` holds
**with the restriction its own statement carries**: the flux identity of `HE2-e` is a function of the
charge data **on `im Ψ` and nowhere else**. **Injectivity is all that is established**: the image is
not characterized, that characterization is not a target of this round and stays **HO**, and nothing
here is closure.**

## `HE3` — the assembled determination

`HE2-a`–`HE2-e` all landed positive at evidence level 2, and those five alone settle this target;
`HE2-f` is excluded from it by construction and its outcome moves it in neither direction. `HE3`
adds no evidence of its own and is reported at the strength jointly reached by those five, which is
the medium of `HE2-b` and `HE2-d`.

**`HE3-holds`: For round H-B's candidate, the product-form, family-invariance and flux clauses of the
frozen candidate bridge condition H3 hold at evidence level 2, at the scope their statements carry —
the family being homogeneous, and the flux identity being an identity about the family **in its
parameters, which is a function of the coarse charges only so far as `HE2-f` separately
establishes**. **This is not closure**: the clause that would supply closure is the propagation
clause, which this round does not establish, and no hydrodynamic limit, continuum equation or
transport coefficient follows from anything here.**

## `HE4` — the discriminators, and what they bound

**`HE4-a`, the non-discrimination discriminator — `hexStream_clauses_and_six_invariants`**, at
evidence level 2, every witness pinned by an equation in the statement. The theorem carries four
conjuncts: the identity-collision rule satisfies `H3-inv` with the same frozen family
(`hexConfWeight_hexStream`, which uses no collision, `H3-prod` and `H3-flux` being statements that do
not mention the rule at all); pure streaming preserves the channel-weighted total for **every** weight
(H-B's `hexSum_hexStream`), so the six single-channel weights are six independent site-independent
channel-weighted invariants; the gas preserves the total exactly for the weights in the `ℤ`-span of
mass and the two momentum rows (H-B's `hexSum_hexGas_iff_span`), which is three; and the gas does not
preserve a single-channel total — with `w = ![1, 0, 0, 0, 0, 0]` and
`c = Pi.single ![0, 0] ![1, 0, 0, 1, 0, 0]`, the head-on pair `{0, 3}` at the origin, both pinned by
equation, `hexSum univ w c = 1` and `hexSum univ w (hexGas L c) = 0`. **The witness arithmetic
evaluated exactly as the freeze recorded it.**

**`HE4-a`: Satisfaction of the frozen condition's product-form, invariance and flux clauses does not
select round H-B's candidate's conserved-charge structure: the identity-collision rule satisfies the
same three clauses with the same family and carries six independent site-independent channel-weighted
invariants where the gas carries three. This bounds what those clauses supply and is not a finding
against either rule.**

**`HE4-b`, the homogeneity bound — `hexConfWeight_site_dependent_not_invariant`**, at evidence
level 2, for `2 ≤ L`, every witness pinned by an equation in the statement. With
`c = Pi.single ![0, 0] ![1, 0, 0, 0, 0, 0]`, a single particle in channel `0` at the origin, and the
site-dependent assignment `Z i = (fun _ => 2)` at the origin and `(fun _ => 1)` elsewhere — in
particular at the site `c₀`, where the particle arrives — the weight of `c` is `2` and the weight of
`Φ c` is `1`. Single particles do not collide (H-B's `hexCollide_of_single`), so the gas simply
streams the particle to `c₀`; that step is `hexGas_single_zero`. **The witness arithmetic evaluated
exactly as the freeze recorded it.**

**`HE4-b`: The invariance established here is an invariance of the homogeneous family: with
site-dependent fugacities the configuration weight is not preserved, by the witness pinned in the
statement. Nothing is asserted about families whose parameters vary from site to site.**

**Both are bounds on `HE2`, not findings against H-B's candidate.** Neither says the candidate lacks
closure, and neither says H3 fails.

## `HE5` — is `H3-prop` statable on the merged record?

**Evidence type: prose/source audit, type P.** `H3-prop` names an accuracy and a scale, so its
statement presupposes the scaling map. The five items of H-A's skeleton are reported **separately**.
**The bounded search** is the five files named under `HE0`, at the mandated base, searched for
`spacing`, `time step`, `topolog`, `carrier growth` and `lift`.

| item | status on the record searched | the passage |
| --- | --- | --- |
| 1. the lattice spacing as a function of `L` | **unfixed** | H-A result 239 (*None is fixed by the manuscripts or by A1–A6*); H-B result 317–318 (*the other four — the lattice spacing as a function of `L`, the time step, the carrier growth and the convergence topology — remain unfixed*) |
| 2. the time step | **unfixed** | the same two passages |
| 3. the field normalization and lift | **fixed**, by H-B's candidate | H-B result 315–317: *The candidate fixes **one** of its five choices: the field lift is the integer count of Boolean occupations, `(c i k).val`, fixed by the construction.* |
| 4. the carrier growth | **unfixed** | the same two passages as items 1 and 2 |
| 5. the topology in which convergence would be claimed | **unfixed** | the same two passages as items 1 and 2 |

**Recorded statement on the bounded search.** Beyond the passages above, the only occurrences of
those terms on the searched record are `../PROGRAMME.md` line 75, which names the same list as what
the H4 obligation requires to be defined —

> Define the microscopic-to-continuum map and the scaling regime explicitly: lattice spacing, time scaling, field normalization, carrier growth, and the topology/norm in which convergence is claimed.

— and `../PROGRAMME.md` line 200, which directs a later round to freeze them. **Neither fixes any
item**, and the two preregistrations repeat the skeleton without fixing anything.
**No passage on the record searched fixes the lattice spacing, the time step, the carrier growth or
the convergence topology.** Where the record is silent, the finding is that it is silent: this is a
determination that no such passage was found on a named and bounded search, and it is not a finding
that those items cannot be fixed.

**`HE5-unstatable`: The propagation clause of the frozen candidate bridge condition H3 cannot be
stated at the mandated base, because the named items of the scaling skeleton are unfixed on the
record searched. **That is a statement about the record, not about the clause**: it is not a finding
that the clause is false, that it is unprovable, or that no propagation clause can be stated, and the
items it names belong to the programme's H4 obligation, which stays **HO**.**

## `HE6` — the shape adjudication

**The adjudication rests on `HE1`, `HE3`, `HE4` and `HE5` and adds no evidence of its own.** It is
this round's adjudication and is not a theorem.

**The gate on `HE6-bridge`, requirement by requirement:**

| requirement | status |
| --- | --- |
| `HE3-holds` | **satisfied** |
| `HE2-f` positive in its **global** form | **satisfied** |
| `H3-prop` statable on the record (`HE5-statable`) | **unmet** — `HE5-unstatable` |
| `H3-prop` carried by a quotation or a proved statement | **unmet** — no such passage exists on the bounded search of `HE5`, and no such statement is proved in `OIBridge/HydroClosureBridge.lean` |

Two of the four are unmet, so **`HE6-bridge` is not written**. A flux that is a function of the
parameters is not yet a function of the coarse charges; `HE2-f` supplies that conversion on `im Ψ`,
and even so the closure-supplying clause is neither statable nor carried here.

**The gate on `HE6-wrong-shape`, requirement by requirement:** `HE4-a`'s non-discrimination is
**established**, but the second requirement — a recorded argument that the gap `HE1` enumerates is
not of the kind any strengthening within this shape addresses — is **not made, and this round does
not make it**. Two of `HE1`'s items tell against making it: `HE2-e` together with a positive global
`HE2-f` does address items 1 and 2 on `im Ψ`, by giving a rule that reads the flux off charge data
there, so a condition of this shape is not shown unable to address the enumerated gap. And the gate
says in terms that `HE5-unstatable` alone may not produce this outcome, item 3 being an obligation of
the ladder rather than a defect of H3's shape. **`HE6-wrong-shape` is not written.**

What remains is `HE6-component`, which is what the freeze predicted, at the medium strength it
predicted.

**`HE6-component`: H3, as this round froze it, is not by itself a bridge condition that supplies
closure: its decidable clauses hold for round H-B's candidate at the scope they carry, and what would
supply closure is its propagation clause, which is not established here and whose statement requires
items of the scaling skeleton that the record leaves unfixed. **H3 stands as a component of a bridge
and not as one**, the programme's H3 obligation stays **HO**, and nothing here shows that closure is
unreachable or that a bridge condition of another shape would not supply it.**

**The programme's status labels.** The H3 obligation is reported **HO**. H1, H2, H4, H5, H6 and H7
keep the labels the merged record gives them and are not moved by this round. No label of this round
is written "for OI" or "for the OI substratum".

## What these outcomes do not license

**Establishing H3's decidable clauses is not closure.** The closure obligation is not discharged
here, no macroscopic equations are closed, the candidate is not said to have a hydrodynamic limit or
a Navier–Stokes limit, H3 is not closed, and the ladder is not closed to H5. `HE3-holds` is a
statement about three clauses of one candidate condition at one candidate substratum.

**A flux in the parameters is not a flux in the coarse charges.** `HE2-e` establishes a function of
`(a, b₁, b₂)`; closure needs a function of the charges; the two are joined here by `HE2-f` and by
nothing else. No sentence of this round writes a charge where `HE2-e`'s statement has a parameter.

> **THE RECOVERY CONSEQUENCE, carried at this mention in the freeze's own words, so that the reader
> meets it beside the outcome it governs:** If `HE2-f` is UNDECIDED, `HE3` can still establish
> product form, invariance and parameter-space flux, and `HE6-component` remains reachable. What
> cannot be claimed is closure from charge data.

**Even with a positive global `HE2-f`, the flux-from-charges rule holds only on `im Ψ`.** Nothing
here says the flux is a function of the coarse charges without that restriction, nothing says the
parameters are read from the local charge data without it, nothing extends the recovery by
continuity, nothing takes the nearest family member where no preimage exists, and no propagation
sentence is written about sites whose local charge data this round has not placed in `im Ψ` — which
is every site, since the round places none.

**A positive `HE2-f` is injectivity, not surjectivity, and not closure.** It is not said that every
coarse charge state is a family member, that the family exhausts the charge sectors, that the
recovery is defined on all charge data, that the coarse charge data lies in `im Ψ`, or that recovery
gives closure. The image of the mean-charge map is not characterized by this round and stays **HO**,
so whether the charge data any particular coarse state carries lies in `im Ψ` is unsettled here and
is reported unsettled.

**Failing to establish `H3-prop` is not a finding that closure is unreachable.** Closure is not said
to be unreachable, no bridge condition is said not to exist, the hydrodynamic programme is not said
to be blocked, Navier–Stokes is not said to be independent of the substratum, and the candidate is
not said to have no hydrodynamic limit. A candidate condition not established establishes **Open**,
never independence; the programme's control 8 applies in full.

**Nothing about A5's status relative to the hydrodynamic target.** That lane is excluded in terms:
nothing here says A5 is required by the hydrodynamic route or that it is not, nothing here calls A5
QM-specific, nothing here says the A1–A4, ¬A5 class is admissible or inadmissible, and no sentence of
this round reports, restates, relies on or disputes round H-D's findings.

> **THE H-B GUARDRAIL SENTENCE, carried at this mention as the bound on what H-B supplies to the
> outcomes just listed, and not as a finding of this round about A5:** H-B shows that A5 is not
> needed to obtain a promising reversible fluid candidate with the right microscopic ingredients; it
> does not yet show that A5 is unnecessary for an actual Euler/Navier–Stokes limit.

**Nothing that closes round H-B or the programme's H-B entry.** H-B is not reported closed here, its
open owner question stays open in its own words, and no label of this round is written "for OI".

**No continuum statement.** No limit is taken, no PDE is asserted or denied, no Euler or
Navier–Stokes equation is written, no transport coefficient is named, no viscosity is claimed, and
`HE2-e`'s identity is not a constitutive law. The continuum-breakdown branch stays closed until
H4–H7 exist, per the programme's control 5, and nothing here speaks about singularities.

**No statistical statement beyond what is proved.** The invariance of a family of measures is not
ergodicity, not mixing, not equidistribution, and not local equilibrium in any propagated sense.
H-B's sentence on its sector measure is carried unchanged under `HE0-ii`.

**No timescale separation.** No relation between a collision time, a block-crossing time and a
hydrodynamic time appears here as a hypothesis or as a finding.

**No inhomogeneous claim.** Every invariance statement of this round is about site-independent
fugacities, and `HE4-b` bounds it.

**Nothing about `d = 3`.** H-B's candidate is two-dimensional, and nothing here is a statement about
the manuscripts' three-dimensional substratum.

**Nothing about the OI → QM chain**, Track B's `P0`, Track I, Bell or gravity — the programme's
control 1. No label is imported as evidence here and no finding is exported there.

**No new condition is named**, no list of conditions is extended or renumbered, and no sentence here
asserts that the framework requires a further condition. H3 is an obligation `../PROGRAMME.md` §3
already carries, and this round states one candidate for it.

**No manuscript is edited, and no manuscript is read.** Publication-facing claims wait, per the
programme's control 10.

**No extremal claim.** H3 is one candidate. No sentence here asserts that it is the weakest, the
least, or the only such condition, and the round did not ask and cannot answer that question.

## Definition budget: **SIX of the frozen six slots fire**

| slot | definition | status |
| --- | --- | --- |
| 1 | `hexFugacity` | **fired** |
| 2 | `hexLocalWeight` | **fired** |
| 3 | `hexConfWeight` | **fired** |
| 4 | `hexMeanOcc` | **fired** |
| 5 | `hexFamilyFlux` | **fired** — the conditional slot, fired because `HE2-e` was stated at kernel level as a named tensor rather than inline |
| 6 | `hexMeanCharge` | **fired** |

**No seventh definition was introduced**, and none was needed, so no append-only amendment was
required. **No witness configuration, parameter triple, fugacity instance, weight instance,
sufficient-statistic vector or block is a top-level definition**: each is a bound variable pinned by
an equation in the statement that needs it, and the vectors `t k` of `HE2-f` are written out inside
`hexMeanCharge_apply`, `hexSpan_sum_zero` and `hexMeanCharge_injective`. `HexLatticeGas`'s,
`HydroSourceAudit`'s, `CubicIsotropy`'s and `SubstratumInterfaceAudit`'s definitions are reused, not
redefined; in particular `hexDir`, `hexCollide`, `hexStream`, `hexGas`, `hexSubstratum` and `hexSum`
are consumed unmodified.

## Start-state discrepancies, recorded and not repaired

The freeze pins twelve read-only blobs and five read-and-write blobs. **All twelve read-only blobs
match the freeze exactly at the mandated base**, `AGENTS.md`, `../PROGRAMME.md`, the four H-A and H-B
artifacts and the six Lean modules alike. **Four of the five read-and-write blobs differ**, and each
difference is an addition landed on `main` by the physical-realization programme's round C4-2 between
the writing of this freeze and the cutting of this round's base — that round's control plane merge
and its landing are both ancestors of the base, and this round's control-plane branch took `main`
into itself before freezing, which `§A.37` permits a control plane and which is why the base carries
them.

| path | blob in the freeze | blob at the base | what differs |
| --- | --- | --- | --- |
| `verification/lean/edge_rigidity_probe.py` | `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` | `55e7c3e3139741521bc5aeac6add56f557be5943` | 491 lines added, all of them the `R7-PC4S` guard section and its three seal constants `_PC4S_BASE`, `_PC4S_SEALED_HEAD`, `_PC4S_MERGE`. Nothing is removed and no existing seal constant moved. |
| `verification/ROADMAP.md` | `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` | `c356e9b5f857ef18a992d67df613b9db96a949d7` | 31 lines added, all of them the round C4-2 section and its two links. No queue row moved. |
| `verification/lean-manuscript-census.json` | `06ad11f4b954f290a5ae523d83a6fb0b142d13e1` | `59f94ac1d18d1f965541a523629e5df9dafd9359` | one disposition entry added, for `PhysicalC4StorageReadback`. |
| `verification/lean-mathlib/OIBridge.lean` | `179d57a9245b117f0db76fc9dec5362dc7a8fe2b` | `4ecbb73105e659e8f8664d2d77988d73f0101e78` | one import line added, `import OIBridge.PhysicalC4StorageReadback`. |
| `verification/programmes/hydrodynamics/PROGRAMME.md` | `b7b24112a462aee083c3e8f3c2980283b38cd10f` | `b7b24112a462aee083c3e8f3c2980283b38cd10f` | unchanged. |

**None of the four differences touches any surface this round reads.** The hydrodynamics programme
file, the four H-A and H-B artifacts and the six Lean modules of the read-only table are
byte-identical to the freeze, so no target's evidence is affected. **The freeze is not repaired and
neither is any file**, and **no newer sibling result is consumed**: this round consumes only what its
freeze says it consumes, and nothing of round C4-2 is read, cited or relied on anywhere.

**One consequence for the surfaces this round writes, recorded.** `../PROGRAMME.md` §8's one-line
state and its status-base line are **appended to** rather than replaced: H-B's sentence and H-B's
status-base line stay byte-identical, because `R7-HYB` pins both as guard contracts and the freeze's
non-doings forbid this round to alter any existing guard section. This round's own sentence and its
own status-base line are written beside them.

## Chronology certification, clause by clause

1. **`§A.37` is present at the base in the wording this freeze uses.** `AGENTS.md` at the mandated
   base has blob `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08`, exactly the value the freeze names.
   Verified. **No discrepancy.**
2. **Round H-A's execution has merged before the execution begins.**
   `git merge-base --is-ancestor 6a8675efca5e5ceeab0195036af1a658b49ace80 0975bbab` returns true.
   Verified.
3. **Round H-B's execution has merged before the execution begins.**
   `git merge-base --is-ancestor 54b33c4304bdbda52a09dfe0a06f3e7ff350d832 0975bbab` returns true, and
   `_HYB_SEALED_HEAD` in `verification/lean/edge_rigidity_probe.py` carries that value. Verified.
4. **Nothing else is required to have merged.** No artifact of lane D is required present or absent,
   and the anti-contamination invariant governs whatever is present. Held.
5. **This preregistration blob is merged into `main` before any execution-specific H-E object enters
   the repository tree.** The base commit's tree carries the preregistration and no H-E Lean
   definition, guard section, probe or result artifact. Held.
6. **The execution pull request's base is exactly the merge commit of this control plane's pull
   request**, and its first act was to verify this file's blob at that base before any target was
   executed. `git rev-parse HEAD:.../preregistration.md` at `0975bbab` returned
   `9f3f4ff4115c8d95215462acd257b4f6b32c9926`. Held and recorded.
7. **The guard pins both**, the preregistration blob by content and the execution ancestry,
   fail-closed. `R7-HYE`'s `_hye_freeze_pin` and `_hye_execution_ancestry` do this.
8. **The ancestry question is asked of the real execution head**, `pull_request.head.sha` from the
   Actions event payload and never the synthetic merge commit; an unresolvable head fails closed with
   no fallback. `_rbr_target_commit` supplies the head and `R7-HYE` returns `False` when it is `None`.
9. **The check excludes pre-freeze side history.** `_rbr_strong_ancestry` requires `_HYE_BASE` to be
   an ancestor of the head **and** every commit of `git rev-list H ^B` to descend from the base,
   fail-closed.
10. **The guard recovers whatever history it needs itself** and fails if recovery fails, for the
    base, for the head and for every enumerated commit alike.
11. **Archive mode.** `_HYE_SEALED_HEAD` and `_HYE_MERGE` are `None` in this execution commit, so the
    guard runs in execution mode and certifies the run's real target. **Archive mode is prepared and
    not yet entered**; the pin commit `P` sets both, after which the same strong check re-runs against
    the sealed head, the pinned merge is required to carry it as its second parent, and both are
    required reachable from the current target, fail-closed. **This sentence is a statement about
    this execution and stays true afterwards.**
12. **The claim is scoped to the repository record.**

## Axiom table — one line per named result of the new module

Every result below is at **evidence level 2**, kernel-checked, with **no `sorry`, no `axiom` and no
`native_decide`** anywhere in `OIBridge/HydroClosureBridge.lean`. `decide` over finite types is used
and is permitted.

| result | axiom line |
| --- | --- |
| `hexFugacity_pos` | `[propext, Classical.choice, Quot.sound]` |
| `hexLocalWeight_zero` | `[propext, Classical.choice, Quot.sound]` |
| `hexLocalWeight_hexFugacity` | `[propext, Classical.choice, Quot.sound]` |
| `hexCollide_charges` | `[propext, Classical.choice, Quot.sound]` |
| `hexLocalWeight_hexCollide` | `[propext, Classical.choice, Quot.sound]` |
| `hexConfWeight_hexStream` | `[propext, Classical.choice, Quot.sound]` |
| `hexConfWeight_hexGas` | `[propext, Classical.choice, Quot.sound]` |
| `hexFamilyFlux_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexFamilyFlux_isotropic` | `[propext, Classical.choice, Quot.sound]` |
| `hexMeanCharge_apply` | `[propext, Classical.choice, Quot.sound]` |
| `hexSigma_strictMono` | `[propext, Classical.choice, Quot.sound]` |
| `hexSigma_mul_nonneg` | `[propext, Classical.choice, Quot.sound]` |
| `hexSigma_mul_eq_zero` | `[propext, Classical.choice, Quot.sound]` |
| `hexSpan_sum_zero` | `[propext, Classical.choice, Quot.sound]` |
| `hexMeanCharge_injective` | `[propext, Classical.choice, Quot.sound]` |
| `hexStream_clauses_and_six_invariants` | `[propext, Classical.choice, Quot.sound]` |
| `hexGas_single_zero` | `[propext, Classical.choice, Quot.sound]` |
| `hexConfWeight_site_dependent_not_invariant` | `[propext, Classical.choice, Quot.sound]` |

**Which targets carry no kernel evidence, stated rather than left to be inferred:** `HE0`, `HE1` and
`HE5` carry none — they are determinations by locating and quoting, evidence type prose/source audit,
type P, and they are **not** in the table above. `HE3` and `HE6` carry none of their own — they are
assembled determinations over the targets named in their own sections.

## Owner questions this round records and does not settle

1. **Whether the sector qualifier belongs in `HE1`'s enumeration.** Recorded under `HE1` above, with
   the quotation, as this round's reading rather than as a settled classification.
2. **Whether the charge data a coarse state carries lies in `im Ψ`.** Deliberately left outside this
   round by the freeze; it is a different statement, it would need its own target, and it stays
   **HO**. Until it is settled, `H3-ident`'s and `H3-prop`'s restriction bites wherever either clause
   is used.
3. **Round H-B's open owner question** — whether the A1–A4, ¬A5 class is admissible as an OI
   substratum — stays exactly as H-B left it, in H-B's own words, in both directions.
