# The instrument completion audit (post-Level III, instrument thread)

Level III completed the algebra, the state space, and one discrete dynamics. It did not complete
the **operational availability relation** of Level II. That seam is what this thread investigates.

This is an audit, not a level. The target is not fixed in advance: the purpose of the first entry
is to decide *which* class of quasilocal instruments the operational statement should be about,
and to record what is decided and what is not. No level number is assigned until a target has an
independent definition, an exact theorem, and its countercontrols.

## The convention

Instruments are stated in the Heisenberg picture. For a unital C\*-algebra `𝒜`, a finite-outcome
instrument is a family

> `Φ_x : 𝒜 → 𝒜`, each completely positive, with `Σ_x Φ_x(1) = 1`.

The normalization is unitality of the sum, not of each map. Where the kernel needs a concrete
witness of complete positivity it uses Kraus form, `Φ_x(z) = Σ_{k ∈ out⁻¹(x)} b_k* z b_k` with
`Σ_k b_k* b_k = 1`, which is a sufficient condition and the form Levels I and II already use.
Whether the abstract CP class is larger than the Kraus class on the quasilocal algebra is one of
the open questions below, and nothing here assumes it is not.

## The three candidate targets

Nested by construction, and **not assumed to coincide**:

1. **Finite-support instruments.** A Level-II finite-dimensional instrument acting on the matrix
   algebra of one finite region, tensored with the identity outside it — an inert spectator
   extension.
2. **Stage-compatible instruments.** Global finite-outcome instruments determined coherently by
   their action on the finite stages: a family `{Φ_x^Λ}` commuting with the inclusions, together
   with whatever passage to the completion that family admits.
3. **All C\*-algebraic instruments.** Arbitrary finite-outcome completely positive maps on the
   completed quasilocal algebra whose sum is unital.

The audit asks whether `1 = 2`, whether `2 = 3`, and — separately from either — whether the
members of 2 that are not in 1 are *operationally available* under the assumptions OI_Q already
carries.

## The discipline

- Every displayed equivalence carries separately identified kernel witnesses for both directions
  (§A.34). Extension, uniqueness, density, and canonical isomorphism do not count as converses.
- Mathematical extension is not operational availability. Level II says each finite-stage
  instrument exists. It does not say that an infinite coherent choice of them is one physically
  available operation. That gap is a question in its own right, to be closed by a derivation or by
  an independence witness, never by definition.
- No claim that a class exhausts the CP instruments on the quasilocal algebra is accepted without
  a countermodel search first.
- The other threads stay frozen: no continuous-time dynamics, no sector-selection work, and no
  manuscript propagation during the audit. The manuscript changes only after a target has an
  independent definition, an exact theorem, and its countercontrols.
- Bare OI, and the frozen Level I, Level II and Level III statements, are untouched.

## Pre-registered questions

| # | Question |
|---|---|
| Q1 | Is a finite-support quasilocal instrument exactly a Level-II finite instrument on a region with an inert spectator extension, in both directions? |
| Q2 | Does a compatible family of finite-stage instruments determine an instrument on the completion? |
| Q3 | Are such families operationally available from the assumptions OI_Q already carries, or is that a further principle? |
| Q4 | Is every CP instrument on the quasilocal algebra stage-compatible? |
| Q5 | Is an explicit operational-completion principle required, and if so what does it say? |

Q1 is the interface test: if it does not fall out cleanly, the interface is defined incorrectly
and the round stops rather than adjusting the target to fit.

## Pre-registered countermodels

1. **A theory containing every finite-support instrument and not closed under infinite-region
   compatible operations.** Tests whether operational completion is an extra principle rather than
   a consequence. Bears on Q3 and Q5.
2. **A genuinely infinite-support quasilocal map.** An infinite product of nontrivial onsite
   phase conjugations: every local observable samples finitely many of the phases, so the family is
   compatible with the inclusions, while no finite region carries the whole map. Bears on
   separating class 1 from the stage-compatible maps.
3. **A witness against any future claim that stage-compatible instruments exhaust the CP
   instruments** on the completion. Required before such a claim is accepted. Bears on Q4.

## First entry: the interface and the finite-support redundancy theorem

**The instrument interface** (`OIBridge/InstrumentCompletion.lean`). On the quasilocal algebra a
finite-outcome instrument is given by conjugation data: elements `β k` of the algebra and an
outcome map, with `Σ_k star (β k) * β k = 1` (`IsQInstrument`). Each branch
`qBranch β out x z = Σ_{k ∈ out⁻¹(x)} star (β k) * z * β k` is linear, positive in the concrete
sense that it carries `star z * z` to a sum of such terms, and the branch sum is unital
(`qBranch_sum_one`). No extension machinery is needed for the branches themselves: multiplication
in the completion is already defined, so a conjugation family acts on the whole algebra directly.

**Finite support.** An instrument is finite-support when all its conjugation elements lie in the
image of one finite stage (`IsFiniteSupport`).

**Q1, decided in both directions.** A finite-region Kraus instrument — operators
`K : Fin (n+1) → M_Λ` with `Σ_k (K k)ᴴ * K k = 1`, the Level-II normalization — yields a
finite-support quasilocal instrument by `β k = stage Λ (K k)`, and the normalization transports
because `stage Λ` is a unital star homomorphism (`qInstrument_of_kraus`). Its action on the
observables of any larger region is the inert spectator extension: the Kraus operators extended by
the identity off `Λ`, acting on the larger region (`qBranch_stage_inclObs`). Conversely, a
finite-support quasilocal instrument comes from a finite-region Kraus instrument, recovered by
injectivity of the stage embedding, and the Level-II normalization is recovered with it
(`kraus_of_finiteSupport`). The two directions are separate theorems with separate witnesses;
neither is inferred from the other, and `finiteSupport_iff_kraus` states the biconditional only
because both are proved.

**Countermodel 2, constructed.** The all-sites phase family assigns to a region the diagonal
unitary whose entry at a configuration is the product, over the sites of the region, of a phase
depending on the configuration there. The family is compatible with the inclusions, because two
configurations agreeing off a region contribute equal factors at every site outside it and those
factors cancel between the operator and its adjoint (`phaseAllWt_compat`, `inclObs_wtConj`).
It therefore defines
an isometric unital star-endomorphism of the local algebra and of its completion (`phaseAllQ`,
`norm_phaseAllQ`, `phaseAllQ_mul`, `phaseAllQ_star`). Invertibility is not proved and is not
needed. It is the total map of no finite-support instrument: for any candidate region there is a
site outside it whose single-site matrix unit the map multiplies by `i`, while an instrument
supported in that region fixes it (`phaseAll_not_finiteSupport`). **Finite-support instrument
totals do not exhaust the stage-compatible quasilocal maps** — the strict separation the
pre-registration expected. The map is not itself packaged as an `IsQInstrument`, whose data is
conjugation by elements of the algebra; whether it belongs to a formally defined class-2 instrument
waits on class 2 being formalized.

**What the countermodel does not settle.** It exhibits one compatible family that does extend. It
does not show that every compatible family extends: for a general compatible family of unital
completely positive stage maps the passage to the completion needs a uniform norm bound. Branches
are subunital — only the branch sum is unital — so the relevant input is the standard
`‖Φ‖ = ‖Φ(1)‖` control for positive maps on a C\*-algebra, or a direct Kraus-form bound sufficient
for continuous extension. Neither is in the kernel. Q2 therefore stands decided for star
endomorphisms arising from compatible weight families, and open in general.

## Second entry: countermodel 1, and Q3 decided negatively

**The test.** The first entry showed that operations no finite region carries exist as maps.
Existence is not availability. Q3 asks whether availability *follows* from the assumptions OI_Q
already carries. The way to decide it negatively is to build a theory that keeps everything the
frozen levels supply and withholds exactly one thing.

**The countermodel** (`OIBridge/InstrumentAvailability.lean`). `AvailFS` declares an operation
available exactly when it is a finite-support instrument. It is a predicate *on* the Level III
objects, not a replacement for them: the quasilocal algebra, its states and its dynamics are
unchanged, and `states_untouched` and `dynamics_untouched` restate the frozen state and dynamics
theorems on the same algebra so that this is checkable rather than asserted. Instrument data is
generalized from `Fin n` to an arbitrary finite index (`IsQInstrJ`, `IsFSJ`, `qTotalJ`, `qBranchJ`,
agreeing with the first entry on `Fin n`) so that composition can use a product index and the
exclusion holds at every finite outcome index.

**Nothing frozen is weakened.** Every finite-support Level II instrument is available
(`availFS_of_kraus`) and conversely every available operation is one (`kraus_of_availFS`), so the
theory contains exactly the operations the first entry characterized. It is closed under the
operations the framework performs: the identity (`availFS_id`); composition, on the union of the
two regions (`availFS_comp`); outcome relabelling (`availFS_relabel`); outcome coarse-graining, the
branches of a coarser outcome map being sums of branches (`qBranchJ_coarse`, `sum_qBranchJ`); and
the frozen OI-induced dynamics, which carries an available operation to an available operation on
the hat region (`availFS_dyn`). Carrier attachment and discard are Level II operations on finite
carriers rather than operations of this quasilocal interface; they are neither used nor withheld.

**What it withholds.** The all-sites phase map is the total map of no available operation, at any
finite outcome index (`phaseAll_not_availFS`). The mechanism is locality plus the normalization: an
available operation fixes the observables of a region disjoint from its support
(`qTotalJ_stage_of_disjoint`), while the phase map moves a single-site matrix unit at every site.

**Q3, decided negatively** (`q3_countermodel`):

> the structure the frozen levels supply does not entail the availability of genuinely
> infinite-support coherent operations.

**Q5 sharpens accordingly.** A target theory containing such operations requires an explicit
operational-completion principle. That principle is an addition, not a consequence — which is the
checkpoint for deciding whether the stronger target is worth adopting at all.

**What the countermodel does not show.** It does not show that OI forbids such operations. It is an
independence result about the frozen structure, not an impossibility result, and a further
principle or a different substratum may well supply them. The finite-support theory is a witness,
not a proposal about the intended physics. And the closure list above is the set of operations
checked, not a claim that a completed framework performs no others.

## Status after the second entry

| Question | Status |
|---|---|
| Q1. Finite-support instrument extension from Level II | **decided**, both directions (`qInstrument_of_kraus`, `kraus_of_finiteSupport`, `finiteSupport_iff_kraus`) |
| Q2. Compatible finite-stage family extends to the quasilocal algebra | **open in general**; decided affirmatively for the star-endomorphisms of compatible weight families. Not pursued in this round |
| Q3. Such families available from existing OI_Q assumptions | **decided negatively** (`q3_countermodel`): the frozen structure does not entail their availability |
| Q4. Every quasilocal CP instrument is stage-compatible | **open**. Class 3 is still unformalized; countermodel 3 remains required before any claim |
| Q5. Extra operational-completion principle required | **sharpened**: necessary for any target containing genuinely infinite-support operations, by the second entry. What such a principle should say, and whether the stronger target is worth adopting, is the next decision |
| Finite-support instrument totals exhaust the stage-compatible quasilocal maps | **decided negatively** (`phaseAll_not_finiteSupport`) |

## Status after the first entry

| Question | Status |
|---|---|
| Q1. Finite-support instrument extension from Level II | **decided**, both directions (`qInstrument_of_kraus`, `kraus_of_finiteSupport`, `finiteSupport_iff_kraus`) |
| Q2. Compatible finite-stage family extends to the quasilocal algebra | **open in general**; decided affirmatively for the star-endomorphisms of compatible weight families (`wtQ_mul`, `norm_wtQ`). The general case needs a uniform norm bound for positive subunital branch maps, or a direct Kraus-form bound, neither in the kernel |
| Q3. Such families available from existing OI_Q assumptions | **open**. Nothing in Levels I–III quantifies over infinite coherent choices; countermodel 1 is not yet built |
| Q4. Every quasilocal CP instrument is stage-compatible | **open**. Class 3 is not formalized, and no claim about it is made; countermodel 3 is required before any is accepted |
| Q5. Extra operational-completion principle required | **open**. The fork the second entry addresses |
| Finite-support instrument totals exhaust the stage-compatible quasilocal maps | **decided negatively** (`phaseAll_not_finiteSupport`) |

## What is not claimed

- No infinite-dimensional analogue of the Level II instrument characterization. The kernel
  characterizes the finite-support class and nothing wider.
- No claim that the Kraus class exhausts the completely positive instruments on the quasilocal
  algebra, in either direction; the abstract CP class is not formalized in this entry.
- No claim that stage-compatible instruments are operationally available under OI_Q. That is Q3,
  and it is open.
- The phase map is not packaged as an instrument of any formally defined class: class 2 is not
  formalized in this entry, and the separation proved is between finite-support instrument totals
  and stage-compatible maps.
- The phase witness is a witness of non-finite-support, not a claim about what OI permits: whether
  the substratum makes such an operation available is not decided here, and the Level III
  countermodel already shows it is induced by no reversible finite-range substratum dynamics.
- The second entry's countermodel is an independence result, not an impossibility result: nothing
  here says OI forbids infinite-support operations, only that the frozen structure does not entail
  their availability.
- Bare OI and the frozen Level I, Level II and Level III statements are untouched. No manuscript
  change is made in these rounds.
