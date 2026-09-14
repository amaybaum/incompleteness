# Hydrodynamics round H-E — H3 as a candidate bridge condition toward closure: CONTROL PLANE

Owner-called, under `../PROGRAMME.md` §3's H3 obligation. This file is the whole of round H-E's
control plane and is merged **alone**, before any execution object exists.

**The round label `H-E` is an identifier, not an ordinal**, in the sense of the repository's rule
that claim IDs are identifiers. Running it before `../PROGRAMME.md` §6's H-C entry is not a
reordering of the H1–H7 ladder: H-E asks what the ladder's closure step would need and whether one
named candidate supplies it, and the ladder itself is untouched. **`H-E` the round label is not
`HD`, `HC`, `HI` or `HO`**, the outcome labels of the programme's §4 taxonomy; this round's targets
carry the prefix `HE` for that reason.

**Blob identity is authoritative.** The execution guard pins this file by content.

**Parallel-track separation.** This round runs on its own branch from `main` at
`b41d22812f8c099a7435cee0d3bb869c3f45474c`. It neither consumes nor produces evidence for the
OI → QM chain (Track B, Track I), for Bell, or for gravity; the programme's control 1 applies in
full.

## The round's shape, declared in `§A.37`'s terms

**This is a SEALING round.**

Under `AGENTS.md` `§A.37`, a round is *sealing* when its preregistration **prospectively owns seal
state** — when it creates new seal and pin state, or explicitly takes ownership of changing seal
state that already exists. This freeze does the first: the execution writes a new Lean module,
`verification/lean-mathlib/OIBridge/HydroClosureBridge.lean`, with its own chronology guard
section `R7-HYE` in `verification/lean/edge_rigidity_probe.py`, and that guard section carries this
round's own seal and pin constants. **The seal constants this round creates and will fill are, by
name:**

| constant | what it holds | when it is set |
| --- | --- | --- |
| `_HYE_BASE` | the mandated execution base — the merge commit of this control plane's pull request | in the execution commit, `E` |
| `_HYE_SEALED_HEAD` | the sealed execution head `E` | in the pin commit, `P` |
| `_HYE_MERGE` | the landing merge `L` that carries `E` as its second parent | in the pin commit, `P` |

`_HYE_SEALED_HEAD` and `_HYE_MERGE` are `None` in the execution commit, so the guard certifies the
run's real target in execution mode; `P` sets them and moves `R7-HYE` to archive mode, which is
what makes the landing certifiable at all.

**Therefore this round lands `E` → `L` → `P`, and `P` is mandatory**, in `§A.37`'s terms and for
`§A.37`'s reason: once `L` is on the head, execution mode's strong ancestry check enumerates the
sibling rounds merged into `main` since the freeze, which do not descend from this round's base,
and without `P` the guard fails closed on the landing.

**What this round does NOT own.** `§A.37` states the rule this freeze obeys: *an archive seal
belongs to the round that set it, and stays immutable afterwards.* Round H-A's constants
(`_HYA_BASE`, `_HYA_SEALED_HEAD`, `_HYA_MERGE`) and round H-B's constants (`_HYB_BASE`,
`_HYB_SEALED_HEAD = 54b33c4304bdbda52a09dfe0a06f3e7ff350d832`, `_HYB_MERGE`) are **read and never
written** by this round. The execution **adds** a guard section to `edge_rigidity_probe.py` and
**alters no existing seal constant in it**. A landing that changed one would be a defect of this
round, and is forbidden in terms.

## Start state — the blobs this round reads and never writes

Pinned **by blob**, at the mandated execution base. Blob identity is authoritative: the commit
locates the tree, the blob is what is compared. The values below are the blobs at
`b41d22812f8c099a7435cee0d3bb869c3f45474c`, and this control plane's pull request carries this file
alone, so its merge commit — the mandated base — carries the same blobs.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/hydrodynamics/PROGRAMME.md` | `b7b24112a462aee083c3e8f3c2980283b38cd10f` |
| `verification/programmes/hydrodynamics/round-h-a-source-audit/preregistration.md` | `934cd6aff1cfb07b823c9b131693ee59bb98c632` |
| `verification/programmes/hydrodynamics/round-h-a-source-audit/result.md` | `56d34463cf6b68bf28d9ab99b6e09f9fa287d826` |
| `verification/programmes/hydrodynamics/round-h-b-reversible-fluid-substratum/preregistration.md` | `37cc9dae301ee10d55adb73b296aa2fc7d0578e3` |
| `verification/programmes/hydrodynamics/round-h-b-reversible-fluid-substratum/result.md` | `dc03b582ed718d374c471b27403b282a295d5c85` |
| `verification/lean-mathlib/OIBridge/HexLatticeGas.lean` | `374db0387337960888a67f4e98609446c8a1b871` |
| `verification/lean-mathlib/OIBridge/HydroSourceAudit.lean` | `fd5f54d8cbba4f68b67335c111d39a2add0c642f` |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean` | `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` |
| `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean` | `fb7e172024597ba3e217a993169447753fa052ec` |
| `verification/lean-mathlib/OIBridge/CubicIsotropy.lean` | `c1918dc0c4ffaf1547f1918e6665f7c086233796` |

Every one of these is read and never written by this round. If any blob differs at the base, the execution records the discrepancy and does not repair the freeze.

**No manuscript is in this table, and no manuscript is read by this round.** `papers/` is outside
the round's surface entirely. That is a deliberate, mechanically auditable boundary and its reason
is given under *The exclusion* below.

### The blobs this round reads and also writes

These are listed separately, with their blobs at the same base, and are **outside** the verbatim
clause above precisely because the round writes them. Each is appended to and none of its existing
content is rewritten by this round.

| path | blob | what the execution adds |
| --- | --- | --- |
| `verification/lean/edge_rigidity_probe.py` | `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` | the `R7-HYE` guard section and its three seal constants; **no existing seal constant is altered** |
| `verification/ROADMAP.md` | `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` | one section for this round, below the H-B section; **no queue row moves** |
| `verification/lean-manuscript-census.json` | `06ad11f4b954f290a5ae523d83a6fb0b142d13e1` | the disposition entry the new module requires under `§A.35` |
| `verification/lean-mathlib/OIBridge.lean` | `179d57a9245b117f0db76fc9dec5362dc7a8fe2b` | the import line for the new module |
| `verification/programmes/hydrodynamics/PROGRAMME.md` | `b7b24112a462aee083c3e8f3c2980283b38cd10f` | the §8 one-line state and the status-base line, refreshed with this round's frozen post-round sentence and **nothing stronger** |

`PROGRAMME.md` appears in both tables and that is not a contradiction: it is **read** as the
taxonomy, the H1–H7 obligation list and the programme controls, and it is **written** only in §8's
one-line state and its status-base line. If its blob differs at the base, the execution records the
discrepancy, refreshes §8 by appending its own frozen sentence, and consumes none of the newer
content as evidence.

## The anti-contamination invariant, FROZEN VERBATIM

A start-state discrepancy does not license the execution to consume the newer sibling result merely because it happens to be present at its mandated base. The round consumes only what its freeze says it consumes.

**Why it matters here specifically:** lane D is reconciling round H-D's sources concurrently, and
its result may be present at this round's mandated base — as a changed `PROGRAMME.md` §8, a changed
`ROADMAP.md`, or a changed `round-h-d-a5-status-adjudication/` — without being consumable by this
round, whose freeze names neither H-D nor any finding of it as an input.

## The exclusion, stated in terms

**The status of A5 relative to the hydrodynamic target is round H-D's lane, and a separate
concurrent round is reconciling its sources. This round does not re-open it, does not re-decide it,
and does not consume it as settled.**

Operationally, and mechanically checkable:

1. `../round-h-d-a5-status-adjudication/preregistration.md` and `.../result.md` are **absent from
   both tables above**. No target reads them, no target cites them, and no finding of theirs is an
   input to any prediction, decision rule or status sentence here.
2. **No manuscript is read**, so no passage bearing on A5's warrant, on the amplitude-scale gauge
   principle, or on the alphabet-as-gauge principle is located, quoted or weighed by this round.
3. **This round consumes only what H-A and H-B established**, at those rounds' own scopes and in
   their own words, together with the kernel objects those rounds proved.
4. Round H-B's candidate lies in the class obtained by dropping A5's amplitude-scale gauge
   principle, and this round **takes that class membership as a recorded fact about the candidate
   and asks no question about it**. Whether the class is admissible as an OI substratum is H-B's
   open owner question; whether A5 is required by the hydrodynamic route is H-D's lane; **both stay
   exactly as they stand, in both directions, whatever this round lands.**
5. The guardrail sentence H-B's consumers carry is carried here unchanged wherever H-B is consumed:

   > **H-B shows that A5 is not needed to obtain a promising reversible fluid candidate with the
   > right microscopic ingredients; it does not yet show that A5 is unnecessary for an actual
   > Euler/Navier–Stokes limit.**

   It is carried as a bound on what H-B supplies, and not as a finding of this round about A5.

## What the merged record establishes, and what it leaves

Assembled here as the freeze's reading; `HE0` and `HE1` re-establish it at the base by quotation,
and a divergence between this reading and what the execution finds is recorded as a discrepancy.

**The hydrodynamic target.** `../PROGRAMME.md` §1 sets the endpoint as a theorem
`concrete OI substratum + explicitly named hydrodynamic conditions -> Navier–Stokes`, strengthened
if the named conditions can themselves be derived, and otherwise a universality/classification
theorem identifying which OI-compatible local reversible substrata have Euler/Navier–Stokes
hydrodynamics. §3 factors the route into obligations H1–H7; §4 fixes the four outcome labels; §7
carries the programme controls, of which control 2 (bare OI is not NS), control 4 (reversibility
versus dissipation must be proved) and control 5 (fix the continuum map before testing
singularities) bind this round.

**What H-A established**, for the manuscripts' wave representative: a linearity gate making the
advection obligation HI conditional on `ZMod q`-linear coarse variables, with real-valued and
nonlinear coarse variables HO; the total-sum conservation law classified exactly, its manuscript
instance conserved iff `q ∣ 4`, hence HI for that candidate field under the `q`-gauge principle and
HO for every other candidate field; the axis stencil's fourth moment proved anisotropic,
conditional HI if H5's stress closure consumes that tensor and otherwise H2 HO; H3 and H4 HO, with
the H4 scaling skeleton recorded as a five-item specification none of whose items is fixed.

**What H-B established**, for one frozen streaming-and-collision candidate inside the kernel's
`Substratum` interface: A1–A4 hold and A5 fails with a witness; the graph sector `Γ` is invariant
and carries the gas; mass and both momentum components are exactly conserved by the gas on every
configuration for every lattice size, on `Γ`, and are **the only** conserved site-independent
channel-weighted totals; the gas commutes with the lattice's `60°` rotation; the stencil's fourth
moment is rotation-isotropic and its sixth is not, with no claim about higher orders; the
block-charge two-time state does **not** close at `L = 4`, `b = 2`; and the charge sectors are
invariant, so the counting measure on each is `Φ`-invariant. H-B reported H3 HO and H4 HO, and its
result note states of the sector measure that it *licenses no ergodicity, mixing or
equidistribution statement within a sector*.

**What remains between those results and closure.** Closure is the step at which the exact
microscopic conservation laws become a self-contained system for coarse fields. The record leaves
exactly this much between:

1. **The flux term is not a function of the coarse state.** H-B's `HB3-a` proves non-closure of the
   block-charge two-time state by a witness: equal coarse two-time states, different coarse states
   one step later. So the conserved-charge balance, which is exact, does not by itself determine
   the next coarse state; what the balance needs is the microscopic flux, and the flux is not
   recovered from the coarse data.
2. **Nothing on the record determines that flux from coarse data, even approximately.** H-B's
   invariant charge sectors are an exact invariance of a counting measure and are declared, in the
   result note itself, to license no statistical statement.
3. **The scaling map is unfixed.** H-A's `H4a` skeleton names five choices — lattice spacing as a
   function of `L`, the time step, the field normalization and lift, the carrier growth, the
   convergence topology — and records that none is fixed by the manuscripts or by A1–A6; H-B fixes
   the field lift and leaves the other four.
4. **The stencil-to-stress bridge is not built.** Both rounds report the isotropy status of the
   stress as conditional on whether H5's closure consumes the bare fourth moment of the stencil,
   and neither builds that bridge.

**What a bridge condition would therefore have to supply.** Given (1) and (2), a bridge cannot be
an exact coarse closure — the record already refutes the one exact candidate examined. It must
supply a **rule that determines the flux term of the conserved-charge balance from coarse charge
data, at a stated accuracy and a stated scale**. Given (3), any statement of "stated accuracy" and
"stated scale" presupposes the scaling map. Those two sentences are the whole of what this round
asks H3 to be measured against.

## H3, the candidate bridge condition, FROZEN

`../PROGRAMME.md` §3 states the H3 obligation as:

> **H3 — local equilibrium / mixing.** State and test the weakest mixing or local-equilibrium
> condition needed to close the macroscopic equations. Existing hidden-sector mixing assumptions
> may be relevant only if a theorem identifies the same object; analogy is not a bridge.

This round states **one candidate condition** against that obligation, for round H-B's frozen
candidate and for it alone. **The round claims no extremal property of the candidate**: it is not
asserted to be the weakest such condition, no target asserts an extremal property, and no sentence
of the execution may add one.

**`H3` — the local-equilibrium bridge candidate, in four clauses.** Write `Φ` for H-B's gas,
`hexDir` for its six lattice directions, `d₁`, `d₂` for the two coordinate rows of `hexDir`, and
`M`, `P₁`, `P₂` for H-B's three conserved charges. The candidate family is parameterized by a
triple `(a, b₁, b₂) : ℝ³` through the channel fugacities `z_k := exp(a + b₁ (c_k)₁ + b₂ (c_k)₂)`.

- **`H3-prod` (product form).** For every parameter triple, the local weight of Gibbs form in the
  three conserved charges factorizes over channels: the weight of a local state is `∏_k z_k^{n_k}`.
- **`H3-inv` (family invariance).** For every parameter triple, the configuration weight
  `∏_i ∏_k z_k^{n_k(i)}`, with the fugacities **site-independent**, is invariant under `Φ`.
- **`H3-flux` (flux as a function of the parameters).** Under a member of the family the mean
  channel occupations are `θ_k = z_k / (1 + z_k)`, and the momentum-flux tensor
  `Σ_k θ_k (u_k)_a (u_k)_b` over the embedded stencil is a function of the parameters alone — so
  that, at the level of the family, the flux is determined by the charge data that names the family
  member.
- **`H3-prop` (propagation).** The coarse evolution of a state whose local charge data varies
  slowly is determined, to the accuracy the hydrodynamic target requires and at the scale the
  scaling map fixes, by `H3-flux` applied locally with the parameters read from the local charge
  data.

**`H3-prod`, `H3-inv` and `H3-flux` are exact finite statements about H-B's candidate**, and the
round decides them in the kernel. **`H3-prop` is the clause that would actually supply closure**,
and the round asks first whether it is statable at all on the merged record, since its statement
names an accuracy and a scale.

**H3 is a CANDIDATE.** This freeze does not preregister H3 as correct, does not preregister it as
the right shape of bridge condition, and does not preregister that its clauses hold. Two questions
are live and are answered separately:

- **does it hold?** — `HE3`, over `H3-prod`, `H3-inv`, `H3-flux`;
- **is it the right bridge?** — `HE6`, the shape adjudication, which has a
  **wrong-shape outcome with its own frozen post-round sentence** and which no prediction here
  anticipates at high strength.

**H3 is not a new condition of the framework.** It is a candidate for an obligation
`../PROGRAMME.md` §3 already carries. The round adds nothing to the A-list, adds nothing to the
observer-admission list, names no further condition, and renumbers nothing (hazard 11).

## The evidence rule for the locating targets, FROZEN

`HE0`, `HE1` and `HE5` are settled by **locating and quoting**, not by proof. For those targets a
determination must be carried by one or more of:

1. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
2. a **verbatim quotation** from a merged result note or preregistration, with its coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist** on the record
   searched, with the search named and bounded.

**Reconstructive inference is not evidence.** A determination of the form "the record must mean X,
because otherwise Y would fail" is **forbidden as a finding** and may appear only in a clearly
labelled analysis paragraph that states it is not evidence and that no target rests on it. **Where
the record is silent, the finding is that it is silent.**

`HE2` and `HE4` are kernel targets at evidence level 2 and are settled by proof; citing a kernel
result of H-A or H-B here **promotes nothing**, and each cited statement is reported at its own
scope.

## Targets, FROZEN

Every kernel target is stated for H-B's candidate with `[NeZero L]`, about the gas `Φ = hexGas L`
acting on configurations. **No kernel target of this round is a statement about a trajectory**, so
none needs the sector qualifier; where any sentence of the execution does speak of a trajectory it
carries "on `Γ`" as H-B's statements carry it, and may not drop it (H-B's hazard 7).

### `HE0` — the record's boundary, located and quoted

Locate and quote, with coordinates, from the four pinned round artifacts: every sentence in which
H-A or H-B reports a status for the H3 obligation; every sentence in which either declares what its
sector-measure, block-variable or mixing content does **not** license; H-A's `H4a` five-item
skeleton and its statement that none is fixed; H-B's record of which one of the five its candidate
fixes; and both rounds' conditional statements about the stencil-to-stress bridge.

**What settles it.** Each listed item quoted with its coordinate, or recorded absent on a named and
bounded search. **What counts as evidence:** the evidence rule above.

### `HE1` — the closure gap, enumerated from the merged record

Report, as a numbered list, what stands between the established microscopic facts and a closed
coarse system, each entry carried by its own quotation. The four items of *What remains between
those results and closure* above are this freeze's reading and are **not** evidence; the execution
re-establishes each by quotation, reports any it cannot, and reports any item the record carries
that this freeze did not name.

**What settles it.** The enumeration, each entry quoted. **A discrepancy between this freeze's four
items and the execution's list is the finding**, recorded and not repaired.

### `HE2` — does H3's decidable part hold for H-B's candidate? (kernel)

**What settles each of `HE2-a`–`HE2-e`:** a named kernel result whose statement is the one written
below, checked at evidence level 2. **What counts as evidence:** the kernel statement itself, with
its axiom line; no probe, no numeric run, and no recorded analysis is evidence for these targets.
A clause neither proved nor refuted at level 2 is **UNDECIDED** with the obstruction named.

**`HE2-a` (kernel).** For every `(a, b₁, b₂) : ℝ³` and every local state `v : Fin 6 → ZMod 2`,
`∏_k z_k^{(v k).val} = exp(a · m(v) + b₁ · p₁(v) + b₂ · p₂(v))`, where `m`, `p₁`, `p₂` are the local
mass and the two local momentum components in H-B's `hexSum` form at a single site. This is
`H3-prod`: the Gibbs weight in the three charges **is** a channel product.

**`HE2-b` (kernel).** For every parameter triple and every `v`,
`∏_k z_k^{(hexCollide v k).val} = ∏_k z_k^{(v k).val}` — the local weight is constant on
`hexCollide` orbits. The mechanism is H-B's collision classification read in the exponent:
`hexCollide` preserves `Σ_k w_k n_k` for every `w` in the `ℤ`-span of `1`, `d₁`, `d₂`
(`hexCollide_conserved_iff`, `hexDir_conditions`, `hexCollide_conditions_iff_span`), and the
exponent of the frozen family is `a · m + b₁ · p₁ + b₂ · p₂`.
**Fallback, frozen now:** H-B's classification is stated for **integer** weights `w : Fin 6 → ℤ`
and the frozen family's parameters are **real**. If the transfer to real parameters does not go
through by reuse, the execution proves the identity directly for the frozen family — the same
64-state case analysis, with the five moved states and the 59 fixed ones — and **records in terms
that it did not reuse H-B's statement**. If neither route closes at level 2, `HE2-b` is UNDECIDED
with the obstruction named, and `HE2-d` is stated with the identity as an explicit hypothesis.

**`HE2-c` (kernel).** For site-independent fugacities, the configuration weight is streaming
invariant: `∏_i ∏_k z_k^{((hexStream L c) i k).val} = ∏_i ∏_k z_k^{(c i k).val}`, by reindexing
each channel's site product along the translation `i ↦ i − c_k`. **The statement carries
"site-independent" and the execution may not drop it** (hazard 4).

**`HE2-d` (kernel).** Consequently the configuration weight is `Φ`-invariant:
`W(z, hexGas L c) = W(z, c)` for every `c` and every parameter triple. This is `H3-inv`.

**`HE2-e` (kernel).** With `θ_k := z_k / (1 + z_k)`, the tensor `Σ_k θ_k (u_k)_a (u_k)_b` over the
six embedded unit vectors is a function of `(a, b₁, b₂)` alone; and at `b₁ = b₂ = 0`, where every
`θ_k` is the common value `θ`, it equals `3 θ δ_{ab}`, through H-B's second-moment identity
`hexMoment2_eq`. This is `H3-flux`, stated as an identity about the family and **not** as a
constitutive law, a stress tensor of a continuum theory, or a term of any equation.

### `HE3` — the assembled determination: does H3's decidable part hold?

**What settles it:** the outcomes of `HE2-a`–`HE2-e`. **What counts as evidence:** nothing new;
`HE3` adds no evidence of its own and is reported at the strength jointly reached by those five.

Exactly one of:

- **`HE3-holds`** — `HE2-a`–`HE2-e` all land positive at evidence level 2, so `H3-prod`, `H3-inv`
  and `H3-flux` hold for H-B's candidate at the scope their statements carry.
- **`HE3-fails`** — at least one of `H3-prod`, `H3-inv`, `H3-flux` is **refuted** for the candidate
  by a proved statement, with the refuting statement named.
- **`HE3-UNDECIDED`** — a clause is neither established nor refuted at level 2, with the
  obstruction named.

**`HE3-holds` is a statement about three clauses of a candidate condition, at one candidate. It is
not closure, and the frozen sentences below say so.**

### `HE4` — the discriminators, and what they bound (kernel)

**What settles each:** a named kernel result at evidence level 2, with every witness pinned by an
equation in the statement. **What counts as evidence:** the kernel statement itself. A witness whose
arithmetic does not evaluate as the execution expects sends the execution to record the discrepancy
and to report the target **UNDECIDED** with the obstruction named; it does not send it to a
different witness silently.

**`HE4-a` (kernel, the non-discrimination discriminator).** The identity-collision rule — pure
streaming, `hexStream L` with no collision — satisfies `H3-prod`, `H3-inv` and `H3-flux` with the
**same** frozen family, by `HE2-a`, `HE2-c` and `HE2-e`, none of which uses the collision; and it
carries **six** independent conserved site-independent channel-weighted totals, one per channel,
through H-B's `hexSum_hexStream`, which holds for **every** weight. The gas carries **three**
(H-B's `hexSum_hexGas_iff_span`), and it does not conserve a single-channel total: with the head-on
pair `{0, 3}` at the origin, pinned by equation in the statement, the channel-`0` total of `Φ c`
differs from that of `c`. **Consequently satisfaction of `H3-prod`, `H3-inv` and `H3-flux` does not
by itself select the candidate's conserved-charge structure**, since a rule with a strictly larger
invariant family satisfies the same three clauses.

**`HE4-b` (kernel, the homogeneity bound).** With **site-dependent** fugacities the configuration
weight is not `Φ`-invariant: for `L ≥ 2`, a configuration with a single particle in channel `0` at
the origin (pinned by equation) and fugacities taking one value at the origin and another at the
site `c₀`, the weight of `Φ c` differs from the weight of `c`. **Consequently `HE2-d`'s invariance
is an invariance of the homogeneous family only**, and the round asserts nothing about families
whose parameters vary from site to site — which is the shape a local-equilibrium statement for a
hydrodynamic limit would need.

**Both `HE4-a` and `HE4-b` are bounds on `HE2`, not findings against H-B's candidate** (hazards 4
and 5). Neither says the candidate lacks closure, and neither says H3 fails.

### `HE5` — is `H3-prop` statable on the merged record? (locate and quote)

`H3-prop` names an accuracy and a scale. Determine, by locating and quoting, whether the merged
record at the base fixes what such a statement requires: each of H-A's five scaling-skeleton items,
reported **separately**, as fixed (with the passage that fixes it) or unfixed (with the passage that
records it unfixed, or with a recorded statement that no passage fixes it on a named and bounded
search).

**What settles it:** the five items reported separately, each fixed with the quotation that fixes it
or recorded unfixed. **What counts as evidence:** the evidence rule above — a verbatim quotation
with a coordinate, or a recorded statement that the passage sought does not exist on a named and
bounded search. **Reconstructive inference is forbidden as a finding here**, and an item the record
does not address is reported as silent rather than as settled either way.

Report, as the determination, exactly one of:

- **`HE5-statable`** — every item `H3-prop`'s statement requires is fixed on the record, with the
  quotations that fix them.
- **`HE5-unstatable`** — at least one required item is unfixed on the record searched, each such
  item named with its quotation, so that `H3-prop` cannot be stated at the base without fixing it
  first.
- **`HE5-UNDECIDED`** — the record does not settle whether an item is fixed, with the obstruction
  named.

**`HE5-unstatable` is a finding about the record, not about H3.** "The propagation clause is false",
"the propagation clause is unprovable", and "no propagation clause can be stated" are forbidden
readings of it, in terms.

### `HE6` — the shape adjudication: is H3 the right bridge condition?

**What settles it:** the outcomes of `HE1`, `HE3`, `HE4` and `HE5` together, read through the two
gates below. **What counts as evidence:** nothing new — `HE6` adds no evidence of its own and is
reported at the strength jointly reached by the targets it rests on; the adjudication is labelled as
this round's adjudication and never as a theorem.

The assembled determination, at the strength jointly reached by `HE1`, `HE3`, `HE4` and `HE5`, in
exactly one of four outcomes. **Both the affirmative and the wrong-shape outcomes are live, and
each has a frozen post-round sentence below.**

- **`HE6-bridge`** — H3 as frozen is the right shape of bridge condition and, with `HE3-holds`, the
  record establishes that H3 together with what H-A and H-B establish supplies the closure step.
  **Requires**: `HE3-holds`, **and** `HE5-statable`, **and** a quoted statement on the record, or a
  proved statement in this round's module, that `H3-prop` follows from the other three clauses at
  the scale fixed. Absent all three, this outcome is **not** written.
- **`HE6-component`** — H3's decidable clauses hold and are a component of a bridge, but H3 as
  frozen does not supply closure: the clause that would supply it is `H3-prop`, and what is missing
  is named — the items `HE5` reports unfixed, and the non-discrimination `HE4-a` records.
- **`HE6-wrong-shape`** — H3 as frozen is **not the right shape of bridge condition**: a condition
  of this shape — an invariance statement about a parameterized family of measures, together with
  a flux identity for that family — cannot supply the closure step, and the round names, from what
  `HE1` enumerated, what shape a bridge would have to have instead. **Requires**: `HE4-a`'s
  non-discrimination established, **and** a recorded argument that the gap `HE1` enumerates is not
  of the kind any strengthening within this shape addresses, stated as an argument from the
  enumerated items and labelled as this round's adjudication rather than as a theorem.
- **`HE6-UNDECIDED`** — the permitted fallback, with the obstruction named.

**The gate on `HE6-bridge`, FROZEN:**

> `HE6-bridge` may be written only if `H3-prop` is both **statable** on the record (`HE5-statable`)
> and **carried** by a quotation or a proved statement. `HE3-holds` alone, and `HE3-holds` together
> with `HE5`, may not produce it. A bridge condition whose closure-supplying clause is not carried
> is not a bridge, whatever its other clauses establish.

**The gate on `HE6-wrong-shape`, FROZEN:**

> `HE6-wrong-shape` may not be written on `HE5-unstatable` alone. That the propagation clause
> cannot be stated at the base is a fact about the scaling map, which is an obligation of the
> ladder (H4) and not a defect of H3's shape. The wrong-shape outcome requires the
> non-discrimination of `HE4-a` **and** the recorded argument that the enumerated gap is not
> addressed by any strengthening within the shape.

**Neither gate binds the predictions**; they bind the decision rule, so that neither outcome can be
reached on the easier question underneath it.

## The preregistered predictions, and their strengths

Recorded before execution, with reasons, so the outcome can be compared against them. Strengths are
**high**, **medium**, **low**.

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `HE0` | positive — every listed passage located | high | the passages were located while drafting this freeze; the risk is a coordinate that moved, not a passage that is absent |
| `HE1` | positive — the enumeration closes | high | the four items are read off two merged result notes; the risk is completeness of the enumeration, and an item this freeze did not name is a reportable finding, not a failure |
| `HE2-a` | positive — the Gibbs weight is a channel product | high | an algebraic identity: the exponent is linear in the channel occupations by construction |
| `HE2-b` | positive — the local weight is constant on collision orbits | medium | it is H-B's collision classification read in the exponent, but that classification is stated for integer weights and the family's parameters are real; the frozen fallback covers the transfer |
| `HE2-c` | positive — streaming invariance of the homogeneous weight | high | a reindexing of each channel's site product, the same mechanism as H-B's `hexSum_hexStream` |
| `HE2-d` | positive — `Φ`-invariance of the homogeneous weight | medium | it is the composition of `HE2-b` and `HE2-c` and inherits `HE2-b`'s strength |
| `HE2-e` | positive — the family's flux tensor is a function of the parameters | high | a finite sum over six embedded unit vectors, with H-B's second-moment identity available for the isotropic case |
| `HE3` | `HE3-holds` | medium | it follows if `HE2-a`–`HE2-e` land as predicted, and `HE2-b` is at medium; a refutation of any clause would be the more interesting outcome and is live |
| `HE4-a` | positive — pure streaming satisfies the three clauses and carries six invariants | high | H-B proved streaming invariance of `hexSum` for **every** weight, so the six invariants are an instance; the remaining work is a two-state witness for the gas |
| `HE4-b` | positive — site-dependent fugacities break invariance | high | a single-particle streaming witness; particles alone do not collide by H-B's `hexCollide_of_single` |
| `HE5` | `HE5-unstatable` | high | this is a determination about the record, not about H3: H-A's `H4a` records in terms that none of the five items is fixed by the manuscripts or by A1–A6, and H-B records that its candidate fixes one of the five |
| `HE6` | `HE6-component` | **medium** | `HE3-holds` with `HE5-unstatable` and `HE4-a` points there: the decidable clauses would hold, the closure-supplying clause would be unstatable at the base, and the clauses that hold would not discriminate. **But whether that makes H3 a component of the right bridge or the wrong shape entirely turns on whether a propagation clause of this shape can supply closure once the scaling map is fixed, which this round cannot settle** |

**No prediction is recorded at high strength for `HE6`, and `HE6-bridge` is not predicted at all.**
`HE6` is what the round exists to decide, and a freeze that predicted it at high strength would be
claiming the answer it is chartered to find. `HE3` is likewise held at medium.

**UNDECIDED remains a permitted label for every target**, reported with the obstruction.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, and the prediction is not amended.

## The status rule — outcomes per target, with the post-round sentence frozen for each

Exactly one sentence per target is written, verbatim, in the result note.

| target | outcome | the frozen post-round sentence |
| --- | --- | --- |
| `HE0` | positive | The boundary of the merged record on closure, local equilibrium, mixing and scaling is located and quoted with coordinates, and every listed passage is present at the mandated base. |
| `HE0` | partial | The boundary of the merged record is located and quoted with coordinates, and the passages recorded absent are named with the bounded search that did not find them. |
| `HE0` | UNDECIDED | Whether the merged record carries the located boundary is UNDECIDED, with the obstruction named; no reading of the record is asserted in its place. |
| `HE1` | positive | What stands between the established microscopic facts and a closed coarse system is enumerated from the merged record, each entry carried by its own quotation, and the enumeration is a statement about the record and not a claim that the list is exhaustive over routes nobody has written. |
| `HE1` | discrepant | The enumeration differs from the freeze's reading, and the difference is recorded as the finding; the freeze is not repaired. |
| `HE1` | UNDECIDED | The closure gap is not enumerable from the merged record at the base, with the obstruction named. |
| `HE2-a`…`HE2-e` | positive | The clause landed at evidence level 2, at the scope its statement carries, and at no wider scope. |
| `HE2-a`…`HE2-e` | negative | The clause is refuted for H-B's candidate by the named statement, and the refutation is a statement about this candidate and this family. |
| `HE2-a`…`HE2-e` | UNDECIDED | The clause is neither established nor refuted at evidence level 2, with the obstruction named, and nothing is asserted in its place. |
| `HE3` | `HE3-holds` | For round H-B's candidate, the product-form, family-invariance and flux clauses of the frozen candidate bridge condition H3 hold at evidence level 2, at the scope their statements carry — the family being homogeneous and the flux identity being an identity about the family. **This is not closure**: the clause that would supply closure is the propagation clause, which this round does not establish, and no hydrodynamic limit, continuum equation or transport coefficient follows from anything here. |
| `HE3` | `HE3-fails` | For round H-B's candidate, the frozen candidate bridge condition H3 fails at the named clause, refuted by the named statement. **This is a finding about one candidate condition at one candidate substratum.** It is not a finding that the candidate lacks a hydrodynamic limit, not a finding that closure is unreachable, and not a finding about any other bridge condition. |
| `HE3` | `HE3-UNDECIDED` | Whether the decidable clauses of the frozen candidate bridge condition H3 hold for round H-B's candidate is UNDECIDED, with the obstruction named. The clauses stand neither established nor refuted, and the programme's H3 obligation stays **HO**. |
| `HE4-a` | positive | Satisfaction of the frozen condition's product-form, invariance and flux clauses does not select round H-B's candidate's conserved-charge structure: the identity-collision rule satisfies the same three clauses with the same family and carries six independent site-independent channel-weighted invariants where the gas carries three. This bounds what those clauses supply and is not a finding against either rule. |
| `HE4-a` | negative or UNDECIDED | The non-discrimination is not established, with the obstruction named, and no adjudication of H3's shape rests on it. |
| `HE4-b` | positive | The invariance established here is an invariance of the homogeneous family: with site-dependent fugacities the configuration weight is not preserved, by the witness pinned in the statement. Nothing is asserted about families whose parameters vary from site to site. |
| `HE4-b` | negative or UNDECIDED | The homogeneity bound is not established, with the obstruction named, and every invariance statement of this round nevertheless carries "site-independent" as its statement carries it. |
| `HE5` | `HE5-statable` | Every item the propagation clause's statement requires is fixed on the merged record at the base, with the quotations that fix them recorded per item. |
| `HE5` | `HE5-unstatable` | The propagation clause of the frozen candidate bridge condition H3 cannot be stated at the mandated base, because the named items of the scaling skeleton are unfixed on the record searched. **That is a statement about the record, not about the clause**: it is not a finding that the clause is false, that it is unprovable, or that no propagation clause can be stated, and the items it names belong to the programme's H4 obligation, which stays **HO**. |
| `HE5` | `HE5-UNDECIDED` | Whether the propagation clause is statable at the mandated base is UNDECIDED, with the obstruction named. |
| `HE6` | `HE6-bridge` | H3, as this round froze it, is a bridge condition of the right shape for the closure step, and the record carries its propagation clause by the quotation or the proved statement named in the result note. **What follows is exactly this and no more**: the closure step is supplied **for round H-B's candidate**, at the scale named, conditional on every qualifier the clauses carry. The programme's H3 obligation is reported **HC**, conditional on H3 as stated, for the candidate; H4–H7 are untouched and stay **HO**; no continuum limit is taken, no equation is written, and nothing is said about OI. |
| `HE6` | `HE6-component` | H3, as this round froze it, is not by itself a bridge condition that supplies closure: its decidable clauses hold for round H-B's candidate at the scope they carry, and what would supply closure is its propagation clause, which is not established here and whose statement requires items of the scaling skeleton that the record leaves unfixed. **H3 stands as a component of a bridge and not as one**, the programme's H3 obligation stays **HO**, and nothing here shows that closure is unreachable or that a bridge condition of another shape would not supply it. |
| `HE6` | `HE6-wrong-shape` | H3, as this round froze it, is **not the right shape of bridge condition**: a condition consisting of an invariance statement for a parameterized family of measures together with a flux identity for that family does not address the gap this round enumerated, and is satisfied by a rule whose conserved-charge structure is not the candidate's. **This is a finding about the shape of the condition, not about round H-B's candidate and not about the programme's target.** The programme's H3 obligation stays **HO**; what shape a bridge would have to have instead is named in the result note as this round's adjudication and not as a theorem; and nothing here shows that closure is unreachable, that no bridge condition exists, or that the ladder is blocked. |
| `HE6` | `HE6-UNDECIDED` | Whether H3, as this round froze it, is the right shape of bridge condition toward closure is UNDECIDED, with the obstruction named. The programme's H3 obligation stays **HO**, and neither the affirmative nor the wrong-shape reading is written anywhere. |

**The programme's status labels, frozen.** Whatever lands, the programme's H3 obligation is
reported **HO** unless `HE6-bridge` is reached, in which case it is reported **HC**, conditional on
H3 as stated, **for round H-B's candidate**, and never "for OI" or "for the OI substratum". H1, H2,
H4, H5, H6 and H7 keep the labels the merged record gives them and are not moved by this round.

## What no outcome licenses

**These sentences are forbidden in the result note, in the `ROADMAP` section, in the `PROGRAMME.md`
§8 refresh, and in the commit messages of this round, in any form.**

- **Establishing H3 is not closure.** Forbidden: "the closure obligation is discharged", "the
  macroscopic equations close", "the candidate has a hydrodynamic limit", "the candidate has a
  Navier–Stokes limit", "H3 is closed", "the ladder is closed to H5". `HE3-holds` is a statement
  about three clauses of one candidate condition at one candidate substratum.
- **Failing to establish H3 is not a finding that closure is unreachable.** Forbidden: "closure is
  unreachable", "no bridge condition exists", "the hydrodynamic programme is blocked",
  "Navier–Stokes is independent of the substratum", "the candidate has no hydrodynamic limit". A
  failed or undecided candidate condition establishes **Open**, never independence; the programme's
  control 8 (outcome asymmetry) applies in full.
- **Nothing about A5's status relative to the hydrodynamic target.** Forbidden: "A5 is required by
  the hydrodynamic route", "A5 is not required by the hydrodynamic route", "A5 is QM-specific",
  "the A1–A4, ¬A5 class is admissible", "the A1–A4, ¬A5 class is inadmissible", and any sentence
  reporting, restating, relying on, or disputing round H-D's findings. That lane is excluded in
  terms, and a sentence of this round that enters it is a defect of this round.
- **Nothing that closes round H-B or the programme's H-B entry.** H-B is not reported closed here,
  its open owner question stays open in its own words, and no label of this round is written "for
  OI" or "for the OI substratum".
- **No continuum statement.** No limit is taken, no PDE is asserted or denied, no Euler or
  Navier–Stokes equation is written, no transport coefficient is named, no viscosity is claimed,
  and the flux identity of `HE2-e` is not a constitutive law. The continuum-breakdown branch
  (S1–S5) stays closed until H4–H7 exist, per the programme's control 5.
- **No statistical statement beyond what is proved.** The invariance of a family of measures is not
  ergodicity, not mixing, not equidistribution, and not local equilibrium in any propagated sense.
  H-B's sentence on its sector measure is carried unchanged.
- **No timescale separation.** No relation between a collision time, a block-crossing time and a
  hydrodynamic time appears as a hypothesis or as a finding.
- **No inhomogeneous claim.** Every invariance statement of this round is about site-independent
  fugacities, and `HE4-b` bounds it. Any sentence dropping that qualifier is a defect.
- **Nothing about `d = 3`.** H-B's candidate is two-dimensional; nothing here is a statement about
  the manuscripts' three-dimensional substratum.
- **Nothing about the OI → QM chain**, Track B's `P0`, Track I, Bell, or gravity — control 1. No
  label is imported as evidence here and no finding is exported there.
- **No new condition is named**, no list of conditions is extended or renumbered, and no sentence
  asserts that the framework requires a further condition.
- **No manuscript is edited**, and no manuscript is read. Publication-facing claims wait, per the
  programme's control 10.
- **No extremal claim.** H3 is one candidate; no sentence asserts it is the weakest, the least, or
  the only such condition.

## Named hazards

1. **Reading `HE3-holds` as closure.** The round's characteristic error. Three clauses of a
   candidate condition hold; the clause that would supply closure is not among them. Every status
   sentence for `HE3` says so, and the gate on `HE6-bridge` exists for this hazard.
2. **Reading `HE5-unstatable` or `HE6-wrong-shape` as a no-go.** Guards against converting an Open
   into an Independent. Failure to state or to establish a bridge condition establishes **HO**
   under the programme's control 8; an impossibility would need a proved no-go, and none is
   attempted here.
3. **Consuming lane D.** Guards against the round re-opening, re-deciding, or treating as settled
   the status of A5 relative to the hydrodynamic target. The H-D artifacts are outside the start
   state, no manuscript is read, and the forbidden sentences are listed.
4. **Dropping "site-independent" from an invariance statement.** Guards against the freeze's
   positive results being read as a local-equilibrium statement for slowly varying data, which is
   what a hydrodynamic limit would need and what `HE4-b` proves the round does not have.
5. **Reading `HE4-a` as a finding against H-B's candidate, or against pure streaming.** Guards
   against a bound being reported as a result. `HE4-a` says what the three clauses do not select;
   it says nothing about either rule's hydrodynamics.
6. **Promoting a cited kernel result.** Guards against H-A's or H-B's theorems being restated more
   broadly than their statements. Nothing cited here gains strength by being cited, and every
   citation is reported at its own scope.
7. **Reusing H-B's integer-weight classification at real parameters without saying so.** Guards
   against a silent gap in `HE2-b`. The frozen fallback requires the direct proof and an explicit
   record that reuse did not carry it.
8. **Reconstructive inference presented as a finding** in `HE0`, `HE1` or `HE5`. Guards against a
   reader who knows the subject supplying a bridging argument the record does not contain. The
   evidence rule forbids it; the final report states which quotation carries each determination.
9. **Treating silence as denial.** Guards against "the record does not fix the time step" being
   reported as "the time step cannot be fixed". Where the record is silent, the finding is that it
   is silent.
10. **Writing a continuum object.** Guards against `HE2-e`'s tensor being called a stress tensor, a
    constitutive relation, or a term of an equation. It is an identity about a family of measures
    on finite configurations.
11. **Naming a new condition.** Guards against the round adding to the framework's condition lists
    or renumbering them. H3 is an obligation `../PROGRAMME.md` §3 already carries, and the round
    states one candidate for it.
12. **Asserting an extremal property of H3.** Guards against the round claiming it has found the
    weakest such condition, which it has not asked and cannot answer.
13. **Confusing the round label `H-E` with an outcome label.** Guards against `H-E` being read as a
    taxonomy value; the round's targets carry the `HE` prefix, and the taxonomy labels are `HD`,
    `HC`, `HI`, `HO`.
14. **Altering an existing seal constant.** Guards against this round's guard work touching
    `_HYA_*` or `_HYB_*`. `§A.37`'s rule is that a seal belongs to the round that set it; this
    round adds `R7-HYE` and its own three constants and alters nothing else in the guard file.
15. **Importing OI → QM results or Track B labels as evidence here, or exporting these findings
    there** — control 1.
16. **Speaking about singularities.** S1–S5 remain closed until a continuum map exists.

## Definition budget

The execution introduces **at most five** top-level definitions, all in the new module
`verification/lean-mathlib/OIBridge/HydroClosureBridge.lean`, and these are the five:

1. **`hexFugacity`** — `ℝ → ℝ → ℝ → Fin 6 → ℝ`, the channel fugacities of the frozen family,
   `(a, b₁, b₂, k) ↦ Real.exp (a + b₁ * (hexDir k 0 : ℝ) + b₂ * (hexDir k 1 : ℝ))`. *Needed.*
2. **`hexLocalWeight`** — `(Fin 6 → ℝ) → (Fin 6 → ZMod 2) → ℝ`, `∏ k, z k ^ (v k).val`, the local
   weight of a state. *Needed.*
3. **`hexConfWeight`** — the product of `hexLocalWeight` over the finite site type, the
   configuration weight of the homogeneous family. *Needed.*
4. **`hexMeanOcc`** — `(Fin 6 → ℝ) → Fin 6 → ℝ`, `z k / (1 + z k)`, the family's mean channel
   occupations. *Needed.*
5. **`hexFamilyFlux`** — the rank-2 tensor `Σ_k (hexMeanOcc z k) * (u_k)_a * (u_k)_b` over the six
   embedded unit vectors, the embedding written inline as H-B writes `hexMoment4`'s. *Conditional*,
   only if `HE2-e` is attempted at kernel level as a named tensor rather than inline.

**A sixth definition requires its own append-only amendment**, separately frozen and merged before
the work it affects, naming the definition and the target it serves. **No witness configuration,
parameter triple, fugacity instance, weight instance or block is a top-level definition** — each is
a bound variable pinned by an equation in the statement that needs it. `HexLatticeGas`'s,
`HydroSourceAudit`'s, `CubicIsotropy`'s and `SubstratumInterfaceAudit`'s definitions are **reused,
not redefined**; in particular `hexDir`, `hexCollide`, `hexStream`, `hexGas`, `hexSubstratum` and
`hexSum` are consumed unmodified.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]` or a subset the kernel reports, **no `sorry`, no `axiom`,
no `native_decide`** — for `HE2-a`–`HE2-e` and `HE4-a`–`HE4-b`, with the frozen fallback for
`HE2-b`. `decide` over finite types is permitted; `native_decide` is not.

**Evidence type "prose/source audit"** (programme control 9) for `HE0`, `HE1` and `HE5`, under the
frozen evidence rule. `HE3` and `HE6` are **assembled determinations**: each is reported at the
strength jointly reached by the targets it rests on, and neither adds evidence of its own.

The result note carries an axiom table with one line per named result of the new module, and says
in terms which targets carry no kernel evidence rather than leaving the absence to be inferred.

## The chronology control

Mechanically checkable, clause by clause. An auditor checks each with the command named.

1. **`§A.37` is present at the base in the wording this freeze uses.** `AGENTS.md` at the mandated
   base has blob `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08`
   (`git hash-object AGENTS.md` at the base). This freeze declares its shape in that section's
   vocabulary, and a base whose `AGENTS.md` blob differs is a recorded discrepancy, not a licence to
   re-read the shape.
2. **Round H-A's execution has merged before the execution begins.** Its sealed head
   `6a8675efca5e5ceeab0195036af1a658b49ace80` is an ancestor of the mandated base
   (`git merge-base --is-ancestor 6a8675efca5e5ceeab0195036af1a658b49ace80 <base>`).
3. **Round H-B's execution has merged before the execution begins.** Its sealed head
   `54b33c4304bdbda52a09dfe0a06f3e7ff350d832` — the value `_HYB_SEALED_HEAD` carries in
   `verification/lean/edge_rigidity_probe.py` — is an ancestor of the mandated base
   (`git merge-base --is-ancestor 54b33c4304bdbda52a09dfe0a06f3e7ff350d832 <base>`).
4. **Nothing else is required to have merged.** In particular **no artifact of lane D is required
   to be present or absent at the base**, and its presence licenses nothing: the anti-contamination
   invariant above governs.
5. **This preregistration blob is merged into `main` before any execution-specific H-E object
   enters the repository tree** — any Lean definition or proof about the fugacity family, the local
   or configuration weight, the mean occupations or the family's flux tensor; any guard section; any
   probe; any result artifact. **There is no permitted pre-execution analysis object**: this freeze
   records no computed witness values, and the execution derives every one it needs.
6. **The execution pull request's base is exactly the merge commit of this control plane's pull
   request**, and its **first act** is to verify this file's blob at that base before any target is
   executed.
7. **The guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
8. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
9. **The check excludes pre-freeze side history.** With `B = _HYE_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of
   `B`**, fail-closed.
10. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
    `B`, for `H`, and for every enumerated commit alike.
11. **Archive mode.** After `L` is appended, `P` sets `_HYE_SEALED_HEAD` and `_HYE_MERGE`, and the
    guard re-runs the same strong check against the sealed head: the pinned merge must carry the
    sealed head as its second parent; the sealed head must pass clauses 8–10 against `B` exactly as
    it did in its own run; and **both must be reachable from the current target**, fail-closed.
12. **The claim is scoped to the repository record.**

## Immutable inputs

Cited and consumed **unmodified**: `Substratum`, `Substratum.Conf`, `Substratum.φ`, `shiftBy`,
`A1`–`A4`, `a1_of_finite`, `a2_every_substratum`, `a3_of_fintype`, `a4_of_exact`; `leap`,
`leapEquiv`, `curOf`, `prevOf`; `Rule`; `hexDir`, `hexDir_add_one`, `hexDir_sub_one`,
`hexDir_conditions`, `hexCollide`, `hexCollide_of_ne`, `hexCollide_of_single`,
`hexCollide_conserved_iff`, `hexCollide_conditions_iff_span`, `hexStream`, `hexStream_apply`,
`hexGas`, `hexGas_apply`, `hexGas_symm_apply`, `hexSubstratum`, `hexSum`, `hexSum_hexStream`,
`hexSum_hexGas`, `hexSum_hexGas_iff_span`, `hexSum_mass_hexGas`, `hexSum_momentum_hexGas`,
`hexSum_leap_sector`, `hexSubstratum_sector`, `hexMoment2_eq`, `hexMoment4_eq`,
`hexMoment4_isotropic`, `hexGas_bijOn_sector`, `hb3a_no_closure`; `CoarseCloses`, `blockSum`,
`axisMoment4`, `axisMoment4_eq`, `IsotropicQuartic`; `quadratic_isotropic`,
`quartic_not_isotropic`; `../PROGRAMME.md` §1, §3, §4, §7; `../round-h-a-source-audit/` and
`../round-h-b-reversible-fluid-substratum/` in full, at their own scopes.

**`A5` is deliberately absent from this list**, as are `hexSubstratum_A5_witness` and
`hexSubstratum_not_A5`. The kernel predicate and its instances are named in this round only in *The
exclusion* above, as a recorded fact about which class H-B's candidate lies in; **no target of this
round consumes any of them, and no finding of this round rests on any of them.**

## Non-doings

The round does not: read any manuscript; edit any manuscript; construct a second substratum
candidate, a three-dimensional candidate, a rest-particle variant or a time-alternating collision;
take any continuum limit or assert any PDE; assert any ergodicity, mixing, equidistribution or
propagated local-equilibrium statement; assert any timescale relation; state any invariance for
site-dependent parameters; modify the `Substratum`, `Rule` or `leap` interfaces, or add fields to
them; alter any existing seal constant or any existing guard section; report round H-B closed or
move its open owner question; re-open, re-decide or consume round H-D's lane; move any `ROADMAP`
queue row; say anything about Track B, Track I, Bell, gravity or singularities.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect. **An execution records discrepancies; it never
  edits the freeze.**
- **This PR carries this file alone.**
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  new Lean module, the result note, the `R7-HYE` guard section with `_HYE_BASE` set and the two seal
  constants `None`, the `OIBridge.lean` import, the census disposition entry, the `PROGRAMME.md` §8
  refresh and the `ROADMAP` section. **No manuscript changes.**
- Exact-head review after execution is complete, with full continuous integration green. A red
  badge arising solely from an archive clause that entered `main` after the base is not a research
  failure; `§A.37`'s exact-head rule applies, and `workflow_dispatch` on the branch is the fallback
  for that case and not the routine.
- **After certification the same pull request carries the landing**: `L` first, its first parent
  current green `main` and its second parent exactly `E`; then `P`, setting `_HYE_SEALED_HEAD` to
  `E` and `_HYE_MERGE` to `L`. Conflicts are resolved in `L`, by merits and never by side, and never
  in `E`.
- Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`HE0`** — the located boundary, each item with its quotation and coordinate, or recorded
   absent on a named and bounded search;
2. **`HE1`** — the closure-gap enumeration, each entry with its quotation, and any discrepancy
   against this freeze's four items recorded as the finding;
3. **`HE2`** — the five kernel statements with their scopes, the `HE2-b` fallback marked used or
   unused, and the "site-independent" qualifier carried in every invariance sentence;
4. **`HE3`** — the assembled determination, with its single frozen sentence;
5. **`HE4`** — the two bounds with their witnesses pinned by equation, each reported as a bound;
6. **`HE5`** — the five scaling items reported separately as fixed or unfixed, with quotations, and
   the determination with its single frozen sentence;
7. **`HE6`** — the shape adjudication, with its gate satisfied or its outcome changed accordingly,
   and its single frozen sentence;
8. what the outcomes do **not** license, in this file's wording, with the lane-D exclusion and the
   H-B guardrail sentence carried unchanged;
9. the definition count against the five-slot budget, the conditional slot marked fired or unused;
10. the chronology certification, clause by clause, including the archive-mode entry at `P`, and
    the axiom table with one line per named result.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **The candidate family is the Gibbs family in H-B's three conserved charges**, parameterized by
   a real triple. An alternative candidate condition — a mixing or approach-to-equilibrium
   statement, with no measure family named — was considered and set aside, because a condition with
   no named object cannot be tested in the kernel and the programme's H3 obligation asks for a
   condition that is stated **and** tested. That choice is recorded here, and `HE6`'s wrong-shape
   outcome is where it is put at risk.
2. **`H3-prop` is stated in the vocabulary of accuracy and scale** rather than in a specific
   limit-theorem form, because fixing a limit-theorem form would fix the scaling map, which is H4's
   obligation and not this round's. `HE5` asks whether the record fixes what the chosen wording
   requires, and reports per item.
3. **The discriminator in `HE4-a` is pure streaming**, the identity-collision rule, because it is
   already inside the merged record's vocabulary — H-B proved its invariance property for every
   weight — and needs no new construction. A different discriminator would need a new candidate and
   a definition budget this round does not spend.
4. **The round is sealing.** An alternative would write no Lean and settle every target by
   locating and quoting, which would make it non-sealing and land `E` → `L`. This freeze does not,
   because `HE2` and `HE4` are exact finite statements about a kernel object and a candidate
   condition that is only located and never tested would leave the programme's H3 obligation
   exactly where it stands.
