# Substratum — A6 background independence, round 1: definition and closure — CONTROL PLANE

Owner-called. This file is the whole of the round's control plane and is merged **alone**, before
any execution object exists. It is a **definition round**, not a proof round: the `ROADMAP` carries
A6 as a `GAP` — the manuscript states the condition and the formal interface has no predicate for
it at all — and the audits that found the gap also found that the manuscript wording admits an
invariant reading and a covariant reading which must not be silently identified. This round does
not try to prove A6. It freezes what A6 could mean formally, specifies the least interface on which
each reading can be stated, and determines by quotation which reading each manuscript coordinate
asserts. Nothing here says A6 holds of anything physical.

**Blob identity is authoritative.** The execution guard pins this file by content.

## Start state

| | |
| --- | --- |
| Merged `main` | `b821d69ae86f7d76020383735b3161e77c064ccc` (PR #591), the commit this branch is created from |
| The queue row (`P1`, A6, `GAP`) and its section "P1 — A6, and what is and is not already represented" | `verification/ROADMAP.md`, blob `3965d9305452cbfa37104366031655f07fb897aa` |
| The substratum-interface audit (Q1's A6 row: gap, two readings named) | `verification/programmes/substratum/interface-audit.md`, blob `e4e0d02bfa67ea428391c0df77ad36f2689b87a3` |
| The manuscript-axiom audit (A6 a gap on the operational carrier) | `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` |
| The `Substratum` structure, `A1`–`A5`, `A3Family`, `waveSubstratum` and its five theorems; no A6 predicate | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| The realized-core images and the configuration-level sourcing bound | `verification/lean-mathlib/OIBridge/ManuscriptAxioms.lean`, blob `f7befdc7b5e814677e6220d91e06fc35b8950c49` |
| The second-order rule `Rule ι V` (`F`, `N`, `infl`, `dep`, `mem_infl`) | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` |
| The A1–A6 list and §3 of the reconstruction | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` |
| §3.1 (background independence, the state-dependent graph, the link transformation law) and §4.4–§4.6 (the `K`-component rule, `M`, `M = μ I_6`) | `papers/SM.md`, blob `bad76808e6ab708732edcb3c6294236aa052cf34` |
| The coupling graph as fixed one-step dependency | `papers/Main.md`, blob `deedef7a0053c6fa7054cad6bc1f9e5ee6580517` |
| The control plane this file is modelled on | `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| The strengthened chronology mechanism, carried forward by name | `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |

Line coordinates below refer to these blobs. A quotation is cited as `file:line`.

## Why this round exists

The substratum-interface audit built `Substratum` — a site type with translations, an additive
alphabet `V`, a finite-range second-order rule — and stated A1, A2 and A5 on it outright, A3 with
the degree as a parameter and in family form, A4 with the gauge as a parameter. For A6 it defined
**no predicate**, for two reasons it recorded separately (`interface-audit.md:106`):

1. the alphabet of `Substratum` carries no internal index and no coupling matrix; and
2. the manuscript statement "admits two readings that the manuscripts distinguish only by saying
   the promotion to local gauge invariance is a derivation step — invariance of the rule under
   `g : ι → Aut V` with each `g i` commuting with a coupling endomorphism `M`, which for the
   nearest-neighbour linear rule forces `g` constant on neighbours, or invariance with the coupling
   transformed covariantly, which is local gauge invariance."

The `ROADMAP` row keeps both reasons attached and says what closing the gap needs: "Closing it is a
definitional job before it is a proof job" (`ROADMAP.md:227–229`). This round is that definitional
job, and only that. The manuscript-axiom audit's finding — that no manuscript-level conjunct of
A1–A6 is a faithful predicate of the **bare operational theory** — is about a different carrier and
is untouched (`ROADMAP.md:231–235`).

The second reason is the one this round exists for. The interface audit's parenthetical already
contains an analysis — "which for the nearest-neighbour linear rule forces `g` constant on
neighbours" — that, if it holds in the kernel, changes what the invariant reading can mean for the
manuscripts' own rule. The analysis was recorded, not executed, and the two readings were named,
not defined. Defining them without first freezing them, their interface, and the prediction of how
they relate would invite exactly the drift this programme's control planes exist to prevent:
defining one of them, calling it A6, and proving something about it.

## The manuscript coordinates, quoted

The determination `D1` is made from these quotations and no others. They are recorded here so that
the freeze and the determination read the same text.

**The definition.** `Substratum.md:102`:

> (A6) **Background independence.** The dynamics is invariant under spatially-varying
> internal-index transformations that preserve the cubic-symmetric coupling matrix pointwise. The
> promotion of the resulting global commutant symmetry to local gauge invariance is then a
> derivation step ([SM §3.1]) — not part of the assumption itself.

**The overlap remark.** `Substratum.md:104`: "A4 (center independence) and A6 (background
independence) overlap in physical content (A6 promotes the symmetry that A4 constrains)".

**The use in Stage 2, step (d).** `Substratum.md:162`: "Background independence (A6) then promotes
the remaining global $SU(3) \times SU(2) \times U(1)$ to local gauge invariance ([SM §3.1])."

**The hypothesis-dependency remark.** `Substratum.md:220`: "A6 (background independence) is
standard for gauge theories."

**The consumption.** `Substratum.md:144` lists A6 among the inputs of Stage 2; `Substratum.md:188`
and `:192` consume A1–A6 in Lemma 23.0 and Theorem 23.

**SM §3.1, the opening notion.** `SM.md:100`:

> The companion paper [Main] treats the coupling graph as fixed. In general relativity, the
> spacetime geometry is dynamical. If space is the coupling graph, background independence requires
> the graph to evolve with the state: s(t+1) = φ_{s(t)}(s(t)), where each φ_s is a bijection but
> G_{φ_s} varies with s.

with the three constraints on the state-dependent graph at `SM.md:104` and the explicit ring
construction at `SM.md:108`.

**SM §3.1, the promotion.** `SM.md:110`: "Background independence is then the premise promoting the
surviving global stabilizer to the local gauge reading developed below." `SM.md:112`:

> $\phi(\mathbf{n}) \to G(\mathbf{n})\,\phi(\mathbf{n}), \qquad M(\mathbf{n}, \hat{e}_j) \to
> G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$

`SM.md:114`: "The wave equation is invariant. This is local gauge invariance. The link variable
$M(\mathbf{n}, \hat{e}_j)$ transforms as a gauge connection".

**The `K`-component rule and the coupling matrix.** `SM.md:306`: each site carries
$\boldsymbol{\phi}(\mathbf{n}, t) \in (\mathbb{Z}/q\mathbb{Z})^K$; the general second-order linear
update has $C, D, M^{(j)} \in \mathrm{Mat}(K)$; reversibility gives $D = -I_K$, center independence
$C = 0$, isotropy $M^{(j)} = M$. `SM.md:308` is the resulting rule with one matrix $M$. `SM.md:328`
and `SM.md:422`: at the symmetric point $M = \mu I_6$; "the coupling matrix $M$ itself is scalar,
$M = \mu I$"; the Standard-Model group is "the commutant (stabilizer) of the $O$-equivariant
condensate $\Sigma$ (Theorem 5)". `SM.md:372`: the six-dimensional link space is "the same 6D space
on which the coupling matrix $M(\mathbf{n}, \hat e_j)$ of §4.4 acts".

**Main, the fixed graph.** `Main.md:358`: the coupling graph $G_\varphi$ is defined by one-step
dependency of $\varphi$; `Main.md:392`: "[SM §3.1] already uses a state-dependent coupling graph
$G(x)$".

## The readings, FROZEN

Throughout, `ι` is the site type, `V` the alphabet — an additive group — and `F : (ι → V) → (ι → V)`
an update map, the `F` field of a `Rule ι V`. The internal index enters **only through the
alphabet**: the manuscripts' `K`-component site variable in `(ℤ/qℤ)^K` is the alphabet
`V := K → ZMod q` for a finite index type `K` (`K = Fin 6` in the manuscripts), and `Substratum`
already admits it, since `V` is any additive group. **No field is added to `Substratum`.**

**Site-dependent internal-index transformations** are maps `g : ι → AddAut V` — at each site an
additive automorphism of the alphabet. On `V = K → ZMod q` these are exactly the `ZMod q`-linear
automorphisms, the `GL(K, ℤ/qℤ)` of the manuscripts' `G(n)`; over the finite alphabet there is no
unitary group and none is introduced. A **global** transformation is a constant `g`.

**The action on configurations** is pointwise: `(g · c) i = g i (c i)` on `ι → V`, and on the
phase-space form `Conf = ι → V × V` pointwise on both slots. Because each `g i` is additive, the
pointwise action commutes with the second-order leap `(p, c) ↦ (c, F c − p)` exactly when it
commutes with `F`; every reading below is therefore stated on `F` and its phase-space form is a
corollary, not a separate reading.

**The site coupling** is an additive endomorphism `M : V →+ V` — the manuscripts' single isotropic
matrix `M ∈ Mat(K)` of `SM.md:308`. **The link coupling** is a family `M : ι → ι → (V →+ V)` — the
manuscripts' link variable `M(n, ê_j)` of `SM.md:112`, indexed by an ordered pair of sites rather
than by a site and a direction; the site coupling is the constant link coupling. Which of the two
the manuscripts' phrase "the cubic-symmetric coupling matrix" denotes — the scalar `M = μ I_6` of
`SM.md:422`, whose pointwise stabilizer is everything, or the block-scalar `O`-equivariant object
whose stabilizer is `U(3) × U(2) × U(1)` — is **not decided here**; `M` is a parameter of every
reading, so both are instances.

**Pointwise preservation.** `g` preserves the site coupling `M` pointwise when `∀ i, ∀ v,
g i (M v) = M (g i v)` — each `g i` lies in the commutant of `M`.

### `A6-inv` — invariance of a fixed rule under site-dependent transformations preserving `M`

```
A6Inv F M  :⟺  ∀ g : ι → AddAut V, PreservesPointwise g M → ∀ c, F (g · c) = g · (F c)
```

The coupling is **fixed**: `F` does not change, `M` does not change, and the transformation acts on
the configuration alone. This is the literal first sentence of `Substratum.md:102`.

### `A6-cov` — covariance: the coupling transforms with the configuration

Stated on **link-coupled rules** only, because covariance needs the coupling as data the
transformation can act on, which a bare `F` does not expose:

```
linkF N M c i        :=  Σ_{j ∈ N i} M i j (c j)
gaugeLink g M i j    :=  g i ∘ M i j ∘ (g j)⁻¹
A6Cov N M            :⟺  ∀ g : ι → AddAut V, ∀ c,
                            linkF N (gaugeLink g M) (g · c) = g · (linkF N M c)
```

No pointwise-preservation hypothesis: the coupling is transported, so nothing needs preserving.
This is the transformation law of `SM.md:112` with the second-order term `− φ(n, t−1)` carried by
the leap. **`A6-cov` is not a predicate of a `Substratum`**; it is a predicate of a neighbourhood
function and a link coupling. That `A6-inv` and `A6-cov` live on different interfaces is the first
reason they must not be identified.

### `A6-glob` — the global commutant symmetry

```
A6Glob F M  :⟺  ∀ g : AddAut V, (∀ v, g (M v) = M (g v)) → ∀ c, F (fun i => g (c i)) = fun i => g (F c i)
```

The special case of `A6-inv` with `g` constant. It is the "global commutant symmetry" the second
sentence of `Substratum.md:102` names as what A6 yields before promotion, and it is frozen as a
reading in its own right because the analysis below predicts that on the manuscripts' own rule
`A6-inv` has no content beyond it.

### `A6-sd` — the state-dependent graph

`SM.md:100` calls a different thing background independence: the coupling graph is a function of
the configuration, `s(t+1) = φ_{s(t)}(s(t))`, a configuration-indexed family of rules with the
bijectivity of the phase-space map automatic. This is a **structural property of a rule family**,
not an invariance under any group, and it needs an interface — `Conf → Rule ι V`, with the three
constraints of `SM.md:104` — that none of the three readings above needs. **It is frozen as a
reading so that it cannot be identified with `A6-cov`**: a coupling that transforms under a gauge
group and a coupling that depends on the state are not the same object, and the manuscripts'
Bell branch (`Main.md:392`, preparation-indexed adjacency) uses the second. **No predicate is
defined for `A6-sd` in this round**; it is part of `D1`'s decision menu only.

**The relations expected among the readings, recorded as analysis and tested as targets.**
`A6-inv ⟹ A6-glob` by specialization, always. On a link-coupled rule `A6-cov` is predicted to be an
identity — true of every `N` and `M` — so as a restriction on rules it is empty, and its content
is the declaration that the coupling is link-valued data the transformation acts on. And on the
constant-coupling `K`-component wave rule with `M` injective, `A6-inv` is predicted to force `g`
equal on every edge, so that a nonconstant `g` in the pointwise stabilizer refutes it. None of
these is asserted here; each is a preregistered target below.

## The least interface, FROZEN

Everything the four readings need, and nothing else:

| object | form | already present? |
| --- | --- | --- |
| internal index | the alphabet `V := K → ZMod q`, `K` a finite type | yes — `Substratum.V` is any additive group; `waveSubstratum` uses `K` a singleton, `V = ZMod q` |
| site coupling | `M : V →+ V` | new, as a parameter of `A6Inv`/`A6Glob` — never a field |
| link coupling | `M : ι → ι → (V →+ V)` | new, as a parameter of `linkF`/`A6Cov` |
| the transformation group | `ι → AddAut V` (site-dependent), `AddAut V` (global) | Mathlib's `AddAut` |
| the action | pointwise, `siteAct` | new |
| pointwise preservation | `PreservesPointwise g M` | new |
| the readings | `A6Inv`, `A6Glob`, `A6Cov` | new |

**What the interface does not contain, by decision:** no complex or real lift of the alphabet; no
unitary group; no condensate `Σ`; no cubic group action on `K`; no `𝒢_sub`; no state-dependent rule
family; no change to `Substratum`, `Rule`, `leapEquiv` or `waveSubstratum`. Each of these is a
possible next interface and none is needed to *state* the readings, which is all this round does.

## The targets, FROZEN

### `D1` — which reading each manuscript coordinate asserts

**Evidence type P** — a prose determination by quotation with coordinates, not a kernel result.
Decided from the quotations recorded above and no others. The outcome menu:

- **(a)** the coordinate asserts `A6-inv`;
- **(b)** the coordinate asserts `A6-glob`;
- **(c)** the coordinate asserts `A6-cov`, the transformation of the coupling being part of the
  assumption;
- **(d)** the coordinate asserts `A6-sd`;
- **SPLIT** — different coordinates assert different readings, each listed with its coordinate;
- **UNDECIDED** — the text does not fix a reading at a coordinate; the obstruction is quoted.

**Prediction: SPLIT**, as follows. `Substratum.md:102`, first sentence, asserts **(a)** literally —
"spatially-varying … preserve … pointwise" is `A6Inv` word for word — and its second sentence
glosses the assumption's content as **(b)**, "the resulting global commutant symmetry", while
placing **(c)** outside the assumption, "a derivation step … not part of the assumption itself".
`Substratum.md:104`, `Substratum.md:162` and `SM.md:110` use A6 as the premise that *promotes* the
global symmetry to local gauge invariance — reading **(c)**, the promotion being what A6 supplies
rather than what is derived from it. `SM.md:100` is **(d)** under the same name. `Substratum.md:220`
fixes nothing. Strength: **high** — the quotations are in hand and the determination consists of
matching them to the frozen definitions.

**What would falsify it:** a reading of the three use-sites under which "promotes" names a
derivation from `A6-inv` or `A6-glob` together with some further premise, rather than A6 as the
promoting premise; if the execution finds that reading supportable from the quoted text, `D1` is
reported as **(a)/(b) at the definition, UNDECIDED at the use-sites**, not as SPLIT.

**What `D1` does not decide:** which reading the programme *adopts*. That is an owner decision,
made after `D1`, `D3` and `D4` are reported together, and it is not this round's.

### `D2` — the manuscripts' wave rule against `A6-inv` on the least interface

`waveSubstratum d L q α` has alphabet `V = ZMod q` and no internal index. On the least interface
this is the case `K` a singleton: `AddAut (ZMod q)` is the unit group `(ZMod q)ˣ` acting by
multiplication, the site coupling is multiplication by `α`, and every `g` preserves it pointwise.
So `A6-inv` is **statable** on `waveSubstratum` — it is not unstatable — but in a **degenerate**
form, and the target has three parts.

- **`D2-i` (kernel, level 2).** `A6Inv (waveSubstratum d L q α).R.F (mulLeft α)` **fails** for
  `q ≥ 3`, `L ≥ 3`, `α` a unit, `d ≥ 1`: a nonconstant unit-valued `g` exists and the neighbour sum
  does not commute with it. Frozen witness: `d = 1`, `L = 3`, `q = 3`, `α = 1`, `g 0 = 1`,
  `g 1 = 2`, `g 2 = 1`, and `c` the indicator of site `1` with value `1`; then
  `F (g · c) 0 = 2` and `g 0 (F c 0) = 1`. **Prediction: positive (the failure is proved); strength
  full.** The execution may pin a different witness, stating the equation.
- **`D2-ii` (kernel, level 2).** `A6Glob (waveSubstratum d L q α).R.F (mulLeft α)` **holds** for
  every `d L q α`: a constant unit factor passes through `α · Σ` by additivity and commutativity of
  `ZMod q`. **Prediction: positive; strength high** — the only risk is the formal step from an
  additive automorphism of `ZMod q` to a `ZMod q`-linear one.
- **`D2-iii` (evidence type P).** The degenerate statement is **not the manuscripts' A6**: with `K`
  a singleton the transformation group is the alphabet's unit group acting by rescaling, which is
  the amplitude-scale freedom the manuscripts assign to A5 (`Substratum.md:100`, "amplitude-scale
  gauge invariance — that the field-value scale is unphysical"), not the internal-index freedom of
  A6, which needs `K = 6`. **Prediction: the wave substratum's A6 status at manuscript level remains
  a gap after `D2`**, exactly as the interface audit's rule requires — a predicate found stronger,
  weaker or differently scoped than the axiom is recorded as a gap, not adjusted — and `D2-i`/`D2-ii`
  are reported as facts about the degenerate form, labelled so.

**So the answer to "vacuous or unstatable" is: neither.** Statable; degenerate; false in the
degenerate form for `q ≥ 3`; true in its global specialization; and not the axiom.

### `D3` — `A6-inv` and `A6-cov` are provably distinct on a small carrier

**Kernel, level 2.** Two halves, both required.

- **`D3-a` — `A6-cov` is an identity.** `∀ N M, A6Cov N M`: for every neighbourhood function and
  link coupling, `linkF N (gaugeLink g M) (g · c) i = Σ_j g i (M i j ((g j)⁻¹ (g j (c j)))) =
  g i (Σ_j M i j (c j))`. **Prediction: positive; strength full** — a two-line computation.
  **Bounded reading:** `A6-cov` restricts no link-coupled rule; its content is the interface, not a
  constraint.
- **`D3-b` — a link-coupled rule failing `A6-inv`.** Frozen carrier: `ι = Fin 2` with
  `N 0 = {1}`, `N 1 = {0}`; `V = Fin 2 → ZMod 2`; `M i j = id` (the constant site coupling `id`,
  which every `g` preserves pointwise); `g 0 = id`, `g 1 =` the component swap; `c 1 = (1, 0)`.
  Then `linkF N M (g · c) 0 = (0, 1)` and `g 0 (linkF N M c 0) = (1, 0)`. **Prediction: positive;
  strength full.**

**Bounded reading of `D3`:** the distinction is **one-directional**. On link-coupled rules `A6-cov`
always holds and `A6-inv` sometimes fails, so `A6-inv` is the strictly stronger condition there,
and **no rule satisfies `A6-inv` and fails `A6-cov`**. "Provably distinct" means exactly: there is a
carrier on which one holds and the other fails, in the one direction available.

### `D4` — single-edge rigidity of `A6-inv` on the constant-coupling rule

**Kernel, level 2.** The interface audit's parenthetical, made a target. For the constant link
coupling `M i j = M₀` with `M₀ : V →+ V`:

- **`D4-a`.** If `F (g · c) = g · (F c)` for the rule `linkF N (fun _ _ => M₀)` and a given `g`,
  and `j ∈ N i`, then `∀ v, g i (M₀ v) = M₀ (g j v)`. Proof shape: evaluate at `c` the indicator
  of `j` with value `v`; the sum over `N i` has one nonzero term. **Prediction: positive; strength
  high** — the only formal cost is the indicator sum.
- **`D4-b`.** Hence if `M₀` is injective and `g` preserves `M₀` pointwise, `g i = g j` on every
  edge: a nonconstant `g` in the pointwise stabilizer, together with one edge between sites where
  it differs, refutes `A6-inv` for the constant-coupling rule. In particular at `M₀ = μ • id` with
  `μ` a unit — the manuscripts' symmetric point `M = μ I_6`, where the pointwise stabilizer is all
  of `AddAut V` — `A6-inv` **fails** whenever `AddAut V` has two elements and `N` has an edge,
  while `A6-glob` **holds** there. **Prediction: positive; strength high.**

**Bounded reading of `D4`:** it is a single-edge statement and needs no connectivity. Its
connected-carrier corollary — on a connected `N` with injective `M₀`, `A6-inv` holds iff every
pointwise-stabilizing `g` is constant, i.e. iff `A6-inv` adds nothing to `A6-glob` — is recorded
here as analysis, **not** as a target, because "connected" is a definition this round does not
spend. **What `D4` says about the manuscripts:** under reading (a), the manuscripts' own
`K`-component rule at `M = μ I_6` violates A6 for every nonconstant `G(n)`; under (b) it satisfies
A6; under (c) A6 is an identity on it. `D4` does not choose among these.

## The preregistered predictions, and their strengths

| target | type | prediction | strength | what would falsify it |
| --- | --- | --- | --- | --- |
| `D1` | P | SPLIT: (a) literal and (b) glossed at `Substratum.md:102`; (c) at `Substratum.md:104`, `:162`, `SM.md:110`; (d) at `SM.md:100` | high | the use-sites read as derivation-from-A6 rather than A6-as-premise; then (a)/(b) at the definition, UNDECIDED at the use-sites |
| `D2-i` | level 2 | `A6-inv` fails on the degenerate form at `q = 3` | full | nothing plausible; the equation is written above |
| `D2-ii` | level 2 | `A6-glob` holds for every `waveSubstratum` | high | only the additive-to-linear step for `AddAut (ZMod q)` |
| `D2-iii` | P | the degenerate form is not the axiom; A6 for the wave substratum stays a gap at manuscript level | high | a manuscript coordinate assigning site-dependent alphabet rescaling to A6 rather than to A5 |
| `D3-a` | level 2 | `A6-cov` is an identity on link-coupled rules | full | — |
| `D3-b` | level 2 | the frozen two-site swap witness fails `A6-inv` | full | — |
| `D4-a` | level 2 | single-edge rigidity | high | the indicator-sum formalization only |
| `D4-b` | level 2 | at `M₀ = μ • id`, `μ` a unit, `A6-inv` fails and `A6-glob` holds | high | rides on `D4-a` |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction. **No
target has a fallback**: each is level 2, or type P, or UNDECIDED.

## What none of these outcomes licenses

- **Nothing here says A6 holds of the physical substratum**, or fails of it. Every kernel target is
  about a frozen reading on a frozen carrier; `D1` is about text.
- **Nothing here touches the Standard-Model gauge-group derivation.** Theorems 5 and 7 of `SM`,
  H-link, H-cust, the `(3,2,1)` decomposition, the condensate stabilizer and the reduction to
  `SU(3) × SU(2) × U(1)` are neither consumed nor judged. `D3-a`'s "identity" is a statement about
  the frozen `A6Cov` on link-coupled rules over a finite alphabet, not about the promotion to local
  gauge invariance on the complex lift, which is outside the interface.
- **Nothing here is about Track B, `P0`, the fibre-Gram classification, or hydrodynamics.** The
  substratum programme and the OI→QM programme share the repository and nothing else in this round.
- **No reading is "the" A6.** After this round A6 has candidate predicates and a determination of
  which coordinate asserts which; it has no adopted predicate, and the `ROADMAP` row's label
  changes only by an owner decision recorded in the execution PR's propagation, not by this file.
- **`A6-sd` is not formalized**, and nothing is said about H-Bell, preparation-indexed adjacency,
  or the state-dependent Einstein construction.
- **No manuscript is edited by this round.** The conflict `D1` is predicted to find between the
  definition and the use-sites is reported, not repaired; whether and how to repair it is an owner
  call for a propagation round.
- **Nothing here decides whether A4 and A6 overlap** (`Substratum.md:104`) or whether A6 is
  independent of A1–A5.

## Immutable inputs

Cited and consumed **unmodified**:

- `Substratum`, `Substratum.Conf`, `Substratum.φ`, `A1`–`A5`, `A4Exact`, `A3Family`,
  `a2_every_substratum`, `a1_of_finite`, `a3_of_fintype`, `a4_of_exact`;
- `waveF`, `waveRule`, `waveSubstratum`, `nbrs`, `dir`, and `waveSubstratum_A1` … `_A5`;
- `SecondOrderLayer.Rule` and `SecondOrderCircuit.leapEquiv`;
- the interface audit's Q1 verdict table and its A6 row; the manuscript-axiom audit's gap verdict
  for A6 on the operational carrier and its scope repair;
- the `ROADMAP` row `P1 — A6`, `GAP`, and its two attached qualifications about A3 and A4.

**The audits' rule is frozen with them:** a predicate found on inspection to be stronger, weaker or
differently scoped than the manuscript axiom is recorded as such and not adjusted to fit.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name

1. **This preregistration blob is merged into `main` before any execution-specific A6 object enters
   the repository tree** — any Lean definition or proof about `siteAct`, `PreservesPointwise`,
   `A6Inv`, `A6Glob`, `linkF`, `gaugeLink`, `A6Cov`, any witness, any probe guard, any result
   artifact. **The single permitted exception is the analysis recorded inside this control-plane
   blob itself**, merged *as* the freeze — the quotations, the three witnesses with their
   equations, and the expected relations among the readings — so that no execution-specific
   artifact needs to precede it.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An
   unresolvable head **fails closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed. A guard that checks only the head does not discharge
   this clause.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated
   commit alike.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most nine** top-level definitions, and these are the nine:

1. **`siteAct`** — the pointwise action of `g : ι → AddAut V` on `ι → V`. *Needed.*
2. **`PreservesPointwise`** — `g` commutes with the site coupling `M` at every site. *Needed.*
3. **`A6Inv`** — on a bare update map `F` and site coupling `M`. *Needed.*
4. **`A6Glob`** — on `F` and `M`. *Needed.*
5. **`linkF`** — the link-coupled update map from `N` and `M : ι → ι → (V →+ V)`. *Needed.*
6. **`gaugeLink`** — the transported link coupling. *Needed.*
7. **`A6Cov`** — on `N` and `M`. *Needed.*
8. **A `Rule`/`Substratum` packaging of `linkF`**, *if* a target must be stated on a `Substratum`
   rather than on `linkF` directly. *Conditional.*
9. **A constant-coupling abbreviation** `linkF N (fun _ _ => M₀)`, *if* `D4` cannot be stated
   readably without one. *Conditional.*

**A tenth definition requires its own append-only amendment.** In particular **no predicate for
`A6-sd`**, no connectivity predicate, and no phase-space form of any reading as a separate
definition — the phase-space form, if recorded, is a theorem about `siteAct` and `leapEquiv`.
**No witness, carrier, transformation, configuration or coupling is a top-level definition** —
each is a bound variable pinned by an equation in the statement that needs it. The predicates are
stated on a bare `F` so that `D2` reads them on `(waveSubstratum d L q α).R.F` with no new
definition.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for `D2-i`,
`D2-ii`, `D3-a`, `D3-b`, `D4-a`, `D4-b`. **Evidence type P** — a prose determination by quotation
with coordinates against the blobs in the start-state table — for `D1` and `D2-iii`; a type-P
result is **labelled as such wherever it is reported** and is never listed among the kernel
results or counted in the axiom table. UNDECIDED is permitted for every target, with the
obstruction.

## Named hazards

1. **Silently identifying the readings.** `A6-inv`, `A6-cov`, `A6-glob` and `A6-sd` are four
   objects on three interfaces. Any sentence using "A6" without a suffix, other than in a quotation
   or in "the `ROADMAP` row A6", is a defect.
2. **Reading the derivation step as part of the assumption.** `Substratum.md:102` says the
   promotion is "not part of the assumption itself". `D1` may find that other coordinates say
   otherwise; the freeze does not let the execution resolve that by choosing.
3. **Enlarging the interface.** No lift to `ℂ`, no unitary group, no condensate, no cubic-group
   action, no `𝒢_sub`, no state-dependent rule family, no new field on `Substratum`. The readings
   are stated on the finite alphabet the manuscripts' substratum has.
4. **Calling any reading "the" A6 before `D1` is decided** — and after: `D1` determines what the
   text asserts, not what the programme adopts.
5. **Reporting `D3` as symmetric.** The distinction is one-directional; "provably distinct" is
   exactly the one-directional statement.
6. **Promoting `D3-a` to physics.** "`A6-cov` is an identity on link-coupled rules over a finite
   alphabet" is not "local gauge invariance is trivial" and not a statement about `SM.md:114`'s
   derivation on the complex lift.
7. **Reporting the degenerate `D2` form as the wave substratum's A6 verdict.** `D2-iii` fixes the
   label: the degenerate form is not the axiom, and the manuscript-level status stays a gap.
8. **Conflating `A6-sd` with `A6-cov`.** A state-dependent coupling and a gauge-transported coupling
   are different objects; `Main.md:392`'s preparation-indexed adjacency is the former.
9. **Taking singleton-`K` rescalings for internal-index transformations.** They are the A5
   amplitude-scale freedom; the hazard is exactly what `D2-iii` exists to name.
10. **Deciding what "the cubic-symmetric coupling matrix" denotes.** `M` is a parameter; whether the
    manuscripts mean `μ I_6` or the block-scalar equivariant object is recorded as unsettled and is
    not resolved by choosing an instance.
11. **Spending a connectivity definition.** `D4` is single-edge by design; the connected corollary
    is analysis.
12. **Any sentence beginning "the substratum satisfies A6" or "A6 is refuted".** Neither is a
    possible outcome of this round.

## Non-doings

The round does not: adopt a reading; prove or refute A6 for anything physical; formalize `A6-sd`,
`𝒢_sub`, the complex lift, the cubic-group action on `K`, or any connectivity notion; touch the
Standard-Model derivation chain or any of H-link, H-cust, H-Bell; say anything about Track B,
`P0`, or hydrodynamics; decide the A4/A6 overlap; edit any manuscript; change `Substratum`,
`Rule`, `waveSubstratum` or any merged label; or change the `ROADMAP` row's status in this PR.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**: the commit SHA locates the tree, the blob SHA is what the guard compares.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean
  module, the result note, the probe guard (pinning this blob and certifying clause 5's ancestry),
  the `ROADMAP` propagation, and the census entry. **No manuscript changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`D1`** — the reading asserted at each quoted coordinate, labelled type P, with the outcome
   label (SPLIT, a single letter, or UNDECIDED at named coordinates) and the quotations;
2. **`D2`** — `D2-i` and `D2-ii` at level 2 with the pinned witness and equation, and `D2-iii`
   labelled type P, in this file's words: statable, degenerate, not the axiom, gap unchanged at
   manuscript level;
3. **`D3`** — `D3-a` universally and `D3-b` on the frozen carrier, with the one-directional bounded
   reading stated;
4. **`D4`** — single-edge rigidity and its symmetric-point consequence, with the connected
   corollary reported only as the analysis it is;
5. the relations among the readings actually reached (`A6-inv ⟹ A6-glob`; `A6-cov` an identity;
   `A6-inv` rigid on the constant-coupling rule), each at the strength reached;
6. what the outcomes do **not** license, in this file's wording, and the owner decision they set up
   — which reading to adopt — named as **open and not this round's**;
7. the points where the manuscript's intended reading was found unsettled, listed and not
   resolved: the definition/use-site split, the `μ I_6`-versus-block-scalar denotation of "the
   cubic-symmetric coupling matrix", and the shared name between `A6-sd` and the gauge readings;
8. the definition count against the nine-slot budget, with conditional slots marked fired or
   unused;
9. the chronology certification, and the axiom table with one line per named kernel result and no
   type-P item in it.
