# Substratum — A6 instantiation, round 2: does the manuscripts' substratum instantiate the covariant interface? CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe guard, no
`ROADMAP` edit, no README edit, no census edit, no manuscript edit and no outcome label. It
**does** carry, deliberately, the frozen objects, the frozen targets, their predictions with sign
and strength, their falsifiers, the status rule and the definition budget — that is what a
preregistration is for, and recording them before merge is what makes them auditable rather than
retrospective. Every *execution-specific* object is excluded. It is merged **alone**, before any
execution begins, and the execution pull request descends from the commit that merges it, under the
ancestry certificate frozen below. **Blob identity is authoritative.** The execution guard pins this
file by content.

**Notation.** In this file's own prose the four readings are always suffixed — `A6-cov`, `A6-inv`,
`A6-glob`, `A6-sd` — as round 1's rule requires and the covariance propagation carried forward. The
bare name appears only inside quotations, inside manuscript text quoted as it stands, in the row
name `P1 — A6`, and in guard, family, directory and round names. **No two of the four are ever
identified, in this file or in the execution.**

## The owner's framing, quoted as the authority for this round's scope

> A6 instantiation: test the actual K=6 link-coupled substratum and complex lift against A6-cov.
> The interpretation problem is solved; now it is a concrete implementation/discharge problem.

and, on what the round is for:

> Settling that instantiation question is the only thing that would justify a stronger label than
> CONDITIONAL.

The round is therefore an **instantiation round**: it asks whether the objects the manuscripts
actually carry are instances of the interface on which the adopted meaning is stated, and it asks
that question in two halves, because the `ROADMAP` row names two obstacles and they are obstacles
of different kinds. It does not re-open the interpretation. It does not adopt, revise or rank any
reading. It does not move the row's label.

The round is placed under `verification/programmes/substratum/a6-instantiation/`, a round directory
new at this commit, beside the round-1 directory `a6-background-independence/` (AGENTS.md §A.36:
preregistration and outcome stay together inside the round that produced them). Round 1's
directory and both its artifacts are consumed unmodified and are blob-pinned by the execution guard.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Merged `main` | `7f130c37939896cdbf6ecfcaaf359f6da8edd7e4` (merge of PR #620), the commit this branch is created from |
| Round 1's control plane (the four readings, the least interface, the frozen witnesses, the twelve hazards) | `verification/programmes/substratum/a6-background-independence/preregistration.md`, blob `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` |
| Round 1's result (`D1`–`D4`, the one-directional distinction, the degenerate form labelled so, what none of it licenses) | `verification/programmes/substratum/a6-background-independence/result.md`, blob `331b1928adde22d5c716a92adb864b523d0c09b8` |
| The covariance propagation's control plane (the owner decision, the adopted meaning, the label's reasons, the named hypothesis) | `verification/audits/foundations/a6-covariance-propagation-audit.md`, blob `e7cb7013747f783135c8e166d290ce6670df0ae9` |
| The round-1 module: `siteAct`, `PreservesPointwise`, `A6Inv`, `A6Glob`, `linkF`, `gaugeLink`, `A6Cov`, sixteen named results | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` |
| The substratum interface: `Substratum` (`ι`, `V`, `R`), `shiftBy`, `Conf`, `φ`, `A1`, `A2`, `A3`, `A4Exact`, `A4`, `A5`, `A3Family`, `a2_every_substratum`, `a1_of_finite`, `a3_of_fintype`, `a4_of_exact`; `dir`, `dir_flip`, `nbrs`, `mem_nbrs_symm`, `waveF`, `waveRule`, `waveSubstratum`, `waveSubstratum_A1`–`_A5` | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| The second-order rule `Rule ι V` (`F`, `N`, `infl`, `dep`, `mem_infl`) and the phase-space map `leapEquiv` | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` |
| The substratum-interface audit (Q1's row for the sixth assumption) and the manuscript-axiom audit (the bare-carrier finding) | `verification/programmes/substratum/interface-audit.md`, blob `e4e0d02bfa67ea428391c0df77ad36f2689b87a3`; `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` |
| The queue row `P1 — A6` (`CONDITIONAL`, `ROADMAP.md:65`), its section "P1 — A6, and what is and is not already represented" (`:394–471`) and the label vocabulary (`:22–31`) | `verification/ROADMAP.md`, blob `8f3f9b7758bffc86ba4b2888761770fb1881a180` — pinned **by quotation** in the sections below; other rounds move that file, so the blob is informational |
| The verification landing page, carrying the round-1 record (`:2042–2061`) and the propagation record (`:2271–2305`) | `verification/README.md`, blob `0ee2a993279b5502ee5893c53fe63194608da51d` |
| The guard file: `R7-A6D` (round 1's contracts and mutation controls), `R7-A6P` (the propagation's), `_rbr_strong_ancestry`, `_rbr_archive_ancestry`, `_bb_blob` | `verification/lean/edge_rigidity_probe.py`, blob `c7e9827c6eb2be9ac7cb660f964d5b610eb3411c` |
| The census | `verification/lean-manuscript-census.json`, blob `16cc96e65357ec1e17742633f5614984c08620ca` |
| The manuscript surfaces stating the six-fold link-coupled rule and the complex lift, read and never edited | `papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd` (§3.1 at `:98–114`; §4.4 at `:304–338`; §4.5 at `:340`; §4.6 at `:366–422`; `:487`); `papers/Substratum.md`, blob `9ac6b732e8786897cade416b67c3f7f1df81ab84` (`:102`, `:104`, `:144`, `:162`, `:220`); `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` (`:358`, `:392`) |
| The book surfaces carrying the same content, read and never edited | `book/ch02-substratum.md`, blob `519188eac9e4c347d7f01eb5b559cfb01df48ea9` (`:86`); `book/ch05-gauge-structure.md`, blob `0f55ef3a7b5fca4172073f330f373f4b16542402` (`:141`, `:143`, `:145`); `book/glossary.md`, blob `e811a2cc00b39d03b1a7adf263e31e63d4bcf957` |
| The control planes this file is modelled on | `verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md`, blob `a80334a5d5f19125b69459523acf723b607f97e1`; `verification/programmes/substratum/a6-background-independence/preregistration.md`, blob `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3` |
| The strengthened chronology mechanism, carried forward by name, with archive mode | `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500`; the archive rule of PR #599 |

Line coordinates below refer to these blobs. A quotation is cited as `file:line`. **The execution
locates every quoted passage by content at its own base, never by the line numbers recorded here**;
a passage whose quoted text is not found verbatim at the execution base is reported as a
discrepancy, and a target that depends on it is reported UNDECIDED with that discrepancy as the
obstruction.

**Independence.** This round is independent of Track B, `P0`, physical C4, H-Bell, Lemma 24.1, H-B
and hydrodynamics, in both directions: nothing from those rounds is consumed as evidence here and
nothing here is evidence there.

## Why this round exists

The covariance propagation adopted `A6-cov` as the publication meaning of the sixth structural
assumption and moved the queue row from `GAP` to `CONDITIONAL`. The label's own vocabulary
(`ROADMAP.md:28`) is "Formally present, carrying a named hypothesis this programme has not
discharged", and the propagation named the hypothesis in two halves, quoted here from the row as it
stands:

> the named hypothesis is that the manuscripts' substratum instantiates that interface: the `K = 6`
> link-coupled rule is not packaged as a `Substratum` (the interface's `waveSubstratum` has a
> singleton internal index) and the complex lift on which `[SM §3.1]` conducts the gauge derivation
> is outside the interface

and from the section:

> Discharging the first half is a packaging job on the finite alphabet; the second needs an
> interface the programme has not built.

Those two halves are obstacles of different kinds and this round keeps them apart throughout. The
first is a question about whether the kernel's `Substratum` structure can hold the manuscripts'
six-fold link-coupled rule at all, and — if it can — what the adopted reading then says of it. The
second is a question about what the interface's covariance statement reaches when the alphabet is
complex, and about what stays outside it even then. **Merging them would make either outcome
unreadable**: a positive on the packaging says nothing about the lift, and a positive on the lift
says nothing about the packaging.

One further thing this round exists to say plainly, because it is the trap the whole enterprise sits
over. Round 1 proved `a6cov_all : ∀ N M, A6Cov N M` — **the adopted reading holds identically on
every link-coupled rule of the interface, so its content is the covariant interface itself and not a
constraint**. It follows that an instantiation positive carries exactly the information that the
manuscripts' rule *is of the link-coupled form*, and carries no information that a condition was
tested and survived. Any sentence of the form "the assumption was checked on the substratum and
holds" would be a defect even on a full positive. This is stated in the status rule, in the
licences, and in the hazards, and the execution repeats it wherever it reports a positive.

## The frozen objects

Four objects are frozen. Each is pinned by module and name, or by manuscript location and blob, and
what is currently proved about each is stated **at its own strength** and nowhere above it.

### Object 1 — the least interface

`verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob
`5ec9fe52835642724d0685d9b920f613874279d6`, together with
`verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob
`56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8`.

```
siteAct g c            :=  fun i => g i (c i)
PreservesPointwise g M :⟺  ∀ i v, g i (M v) = M (g i v)
linkF N M c            :=  fun i => ∑ j ∈ N i, M i j (c j)
gaugeLink g M          :=  fun i j => g i ∘ M i j ∘ (g j).symm
A6Cov N M              :⟺  ∀ g c, linkF N (gaugeLink g M) (siteAct g c) = siteAct g (linkF N M c)
A6Inv F M              :⟺  ∀ g, PreservesPointwise g M → ∀ c, F (siteAct g c) = siteAct g (F c)
A6Glob F M             :⟺  ∀ g : AddAut V, (∀ v, g (M v) = M (g v)) →
                              ∀ c, F (fun i => g (c i)) = fun i => g (F c i)
```

with `ι` the site type, `V` the alphabet — **any additive commutative group** — `g : ι → AddAut V`
the site-dependent internal-index transformations, `M : V →+ V` the site coupling and
`M : ι → ι → (V →+ V)` the link coupling. The substratum interface carries

```
structure Substratum where
  ι : Type ; V : Type ; [DecidableEq ι] [AddCommGroup ι] [AddCommGroup V] ; R : Rule ι V
```

with `Rule ι V` carrying `F`, `N`, `infl`, `dep : ∀ i c c', (∀ j ∈ N i, c j = c' j) → F c i = F c' i`
and `mem_infl : ∀ i j, j ∈ N i → i ∈ infl j`, and the axioms `A1` (finiteness of `ι → V × V`), `A2`
(bijectivity of `φ = leapEquiv R.F`), `A3 D`, `A4Exact`, `A4 G` and `A5` stated on it.

**What is proved about the interface, at its own strength.** `A6Cov` is a predicate of a
neighbourhood function and a link coupling, **not of a `Substratum`** (round 1's freeze, and the
module's own docstring). `A6Inv` and `A6Glob` are predicates of a bare update map and a site
coupling. `Substratum` has **no field** for an internal index, a coupling matrix, or a link
coupling; the internal index enters only through the alphabet, and no field is added by round 1.
`waveSubstratum d L q α` is the interface's only `Substratum` instance, with `V = ZMod q` — the case
of a singleton internal index — and it satisfies `A1`–`A5` as stated.

### Object 2 — the covariance reading, and exactly what is proved of it

`A6Cov` as displayed above, and the level-2 result

```
a6cov_all : ∀ (N : ι → Finset ι) (M : ι → ι → (V →+ V)), A6Cov N M
```

**At its own strength:** for every site type, every additive commutative alphabet, every
neighbourhood function and every link coupling, the transported link coupling carries the
link-coupled update map to itself under the site action. **Bounded, as round 1 froze it and the
propagation carried forward:** `A6-cov` restricts no link-coupled rule; its content is the interface,
not a constraint. It is **not** "local gauge invariance is trivial", and it is **not** a statement
about the derivation conducted at `SM.md:112–114`.

The three readings that are not the adopted one are frozen with it and are never identified with it
or with each other: `A6-inv`, the separate and strictly stronger fixed-background condition, refuted
on the frozen two-site carrier (`d3b_not_a6inv`), rigid across every coupled pair of sites on the
constant-coupling rule (`d4a_single_edge`, `d4b_edge_rigidity`, `d4b_not_a6inv_of_nonconstant`) and
failing at the symmetric point `M = μ I_6` (`d4b_symmetric_point`, `d4b_mu_id`); `A6-glob`, the
global specialization (`a6glob_of_a6inv`, `a6glob_constLink`, `d2ii_wave_a6glob`); and `A6-sd`, the
state-dependent coupling graph of `SM.md:100`, a structural property of a rule family, not an
invariance under any group, and **not formalized**.

### Object 3 — the six-fold link-coupled rule, as the manuscripts state it

`papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd`.

**`SM.md:306`** — each site carries a `K`-component vector
$\boldsymbol{\phi}(\mathbf{n}, t) \in (\mathbb{Z}/q\mathbb{Z})^K$; the general second-order linear
update is
$\boldsymbol{\phi}(\mathbf{n}, t+1) = C\,\boldsymbol{\phi}(\mathbf{n}, t) + \sum_j M^{(j)}[\boldsymbol{\phi}(\mathbf{n}+\hat{e}_j, t) + \boldsymbol{\phi}(\mathbf{n}-\hat{e}_j, t)] + D\,\boldsymbol{\phi}(\mathbf{n}, t-1)$
with $C, D, M^{(j)} \in \mathrm{Mat}(K)$; reversibility gives $D = -I_K$, center independence
$C = 0$, spatial isotropy $M^{(j)} = M$.

**`SM.md:308`** — the resulting normalized form,
$\boldsymbol{\phi}(\mathbf{n}, t+1) = \frac1d M \sum_{j=1}^{d}[\boldsymbol{\phi}(\mathbf{n}+\hat{e}_j, t) + \boldsymbol{\phi}(\mathbf{n}-\hat{e}_j, t)] - \boldsymbol{\phi}(\mathbf{n}, t-1)$,
labelled there as the observer-level normalized branch.

**`SM.md:112`** — the link-valued form of the coupling, $M(\mathbf{n}, \hat{e}_j)$, and its
transformation law. **`SM.md:372`** — the six-dimensional link space is "the same 6D space on which
the coupling matrix $M(\mathbf{n}, \hat e_j)$ of §4.4 acts". **`SM.md:328`, `:422`** — the symmetric
point $M = \mu I_6$, "the coupling matrix $M$ itself is scalar, $M = \mu I$".
**`Substratum.md:162`** — $K = 6$ with multiplicities $(3,2,1)$.

**What is proved about it, at its own strength: nothing.** It is not packaged as a `Substratum`
(round 1's conditional slot 8, unused, and the propagation records the packaging as a job the
programme has not done); no kernel statement quantifies over it; `waveSubstratum`, the interface's
only `Substratum` instance, has a
singleton internal index and is a different object. The round-1 results `d4b_symmetric_point` and
`d4b_mu_id` are stated for an abstract site type and an abstract constant coupling `M₀ v = μ • v` on
`K → ZMod q`, and are **not** instantiated at the manuscripts' site type, neighbourhood function or
component count.

### Object 4 — the complex lift, as the manuscripts conduct the gauge derivation on it

`papers/SM.md` at the same blob, and `papers/Substratum.md`, blob
`9ac6b732e8786897cade416b67c3f7f1df81ab84`.

**`SM.md:112`** — the transformation law
$\phi(\mathbf{n}) \to G(\mathbf{n})\,\phi(\mathbf{n})$,
$M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$.
**`SM.md:114`** — "The wave equation is carried to itself: this is the covariance that (A6) asserts,
and once the link variable is data transported in this way the local transformation law imposes no
further condition on the rule", then the connection, the plaquette, the adjoint transformation and
the Wilson action. **`SM.md:334`** (Theorem 5) — $\Sigma=\langle\phi\phi^\dagger\rangle$
$O$-equivariant, block decomposition on $T_1\oplus E\oplus A_1$, "for generic distinct block values
its stabilizer in $\mathrm U(6)$ is $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$".
**`SM.md:487`** — "The substratum dynamics is locally $\mathrm{U}(6)$ invariant".
**`Substratum.md:162`** — "The unitary group of the bicommutant of the cubic-group action on
$V_K = V_3 \oplus V_2 \oplus V_1$". **`book/ch05-gauge-structure.md:145`** — the same transformation
law with $G(\mathbf{n}) \in \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$.

**What is proved about it, at its own strength: nothing in the kernel.** The covariance identity of
`SM.md:114` is the manuscript's own elementary computation, stated as mathematics in manuscript
voice; **it is not kernel-checked**, and the propagation's frozen record says so in the `ROADMAP`
section, in the verification landing page and in this file. Round 1's least interface excludes a
complex alphabet, a unitary group, an inner product, a condensate $\Sigma$ and a cubic group action
on the component index by that round's own scoping decision, recorded there as "What the interface
does not contain, by decision".

**This freeze's scope decision on the alphabet, recorded as a decision.** `A6Cov` is stated for an
alphabet that is any additive commutative group, so instantiating the alphabet at `Fin 6 → ℂ`
introduces **no definition and no structure**: it is the interface's own predicate at a carrier the
interface already admits. This round therefore instantiates the alphabet at a complex carrier and
**does not** introduce a unitary group as a structure on the interface, an inner product, a
condensate, a cubic group action, a state, or any field on `Substratum`. What that instantiation
reaches, and what it leaves outside, is the business of targets `CX1`–`CX3` and is not asserted
here.

## The targets, FROZEN

All targets live in one new module, `OIBridge/A6Instantiation.lean`, importing
`OIBridge.BackgroundIndependence` and guarded by **`R7-A6I`**, a name absent from the guard file at
the start-state blob. Every predicate not named in the definition budget below is the merged
interface's, **reused and never redefined**; in particular `siteAct`, `PreservesPointwise`, `A6Inv`,
`A6Glob`, `linkF`, `gaugeLink`, `A6Cov`, `Substratum`, `A1`–`A5`, `A4Exact`, `Rule`, `leapEquiv`,
`dir`, `nbrs`, `mem_nbrs_symm`, `waveF`, `waveRule` and `waveSubstratum` are consumed unmodified.
Every carrier, transformation, configuration and coupling that is not a budget slot is a **bound
variable pinned by an equation** in the statement that needs it.

**UNDECIDED is a permitted outcome for every target**, reported with the obstruction named and
quoted. **A negative is a permitted outcome for every kernel target**, and is earned by a computed
certificate in the kernel, never by a failed proof search. **No target may be reported at a strength
above the one reached.**

### Family `PK` — the first obstacle: packaging the six-fold link-coupled rule as a `Substratum`

#### `PK0` — what the manuscripts' rule consists of, and whether the interface has a place for each datum

**Evidence type P** — a determination by quotation with coordinates against the blobs in the
start-state table, made from `SM.md:306`, `:308`, `:112`, `:372`, `:328`, `:422` and
`Substratum.md:162` and no others. For each datum of the manuscripts' rule — site type, alphabet and
component count, neighbourhood, coupling and its link-valued form, the second-order term, the
normalization — the execution records which of the following holds:

- **(a)** the interface has a field or a parameter for it;
- **(b)** the interface has no place for it and the packaging would need a new field on
  `Substratum`, which this round will not add;
- **UNDECIDED** — the manuscripts do not fix the datum; the obstruction is quoted.

**Prediction: (a) for every datum, with two recorded readings.** The site type is the cubic torus
`Fin d → ZMod L`, which `Substratum.ι` admits; the alphabet is `Fin 6 → ZMod q`, which
`Substratum.V` admits, `V` being any additive commutative group; the neighbourhood is `nbrs d L`,
which `Rule.N` carries; the coupling in link-valued form is `linkF`'s parameter
`M : ι → ι → (V →+ V)`; the second-order term $-\boldsymbol{\phi}(\mathbf{n}, t-1)$ is carried by the
phase-space map `leapEquiv` and is not part of `F`, exactly as round 1 froze it. The two recorded
readings: the normalization $\frac1d$ of `SM.md:308` is absorbed into the coupling parameter `M`,
which the round carries as a parameter and does not instantiate; and `M^{(j)} = M` isotropic,
carried in the link-coupled form as a coupling that depends on the ordered pair of sites, is the
`SM.md:112` form, with the constant coupling one instance. **Strength: high.**

**What would falsify it:** a datum with no field and no parameter — for instance a requirement that
the coupling depend on the configuration, which is `A6-sd` and a different object, or a requirement
that `Substratum` carry the component index as a field. Either outcome is reported **(b)** with the
datum named, and the round then reports `PK1` negative or UNDECIDED and **does not add the field**.

#### `PK1` — the packaging exists

**Kernel, level 2.** There is a `Substratum` — call it the packaged carrier — with
`ι = Fin d → ZMod L`, `V = Fin 6 → ZMod q`, `R.N = nbrs d L`, `R.infl = nbrs d L` and
`R.F = linkF (nbrs d L) M` for a link coupling `M : ι → ι → (V →+ V)` carried as a parameter, with
`Rule.dep` and `Rule.mem_infl` discharged.

**Prediction: positive; strength high.** `dep` is the observation that the sum over `N i` reads `c`
only on `N i`; `mem_infl` is the merged `mem_nbrs_symm`, which is exactly the symmetry the axis
neighbourhood has. **What would falsify it:** `Rule.mem_infl` failing for `nbrs` at some `d`, `L` —
it does not, `mem_nbrs_symm` being proved — or a `dep` obligation that the link-coupled sum cannot
meet. Either is a **negative** and is reported as such, with the packaging recorded as impossible in
the interface as it stands and the obstruction named; the round does not repair it by changing
`Substratum`.

#### `PK2` — the packaged carrier's update map is the interface's link-coupled map, and the adopted reading holds of its own link data

**Kernel, level 2.** Two conjuncts, both required.

- **`PK2-a`** — the bridge equation: for the packaged carrier, `R.F = linkF R.N M` for the very `M`
  the packaging carries. **Prediction: positive; strength full** — it is the packaging's defining
  equation, and stating it as a theorem rather than leaving it to definitional unfolding is what
  makes the bridge auditable.
- **`PK2-b`** — `A6Cov (nbrs d L) M` for that `N` and that `M`, an instance of `a6cov_all`.
  **Prediction: positive; strength full.**

**Bounded reading, frozen:** `PK2-b` is an **instance** of a merged identity and is not a new
theorem. The content of `PK2` is `PK2-a` — the identification of the manuscripts' carrier with the
interface's — and the execution reports it in those terms. Because `A6Cov` holds for every `N` and
`M`, `PK2-b` carries exactly the information that the packaged carrier's rule is link-coupled, and
carries no information that a condition was tested. **What would falsify `PK2-a`:** a packaging
whose `F` is not the link-coupled map — for instance one in which the normalization or the isotropy
constraint has to be applied outside `linkF`. That is a **negative**, reported with the equation that
fails.

#### `PK3` — the packaged carrier against A1–A5

**Kernel, level 2.** Five conjuncts, each reported separately and at its own strength.

- **`PK3-a` (A1).** `A1` holds for `NeZero L`, `NeZero q`. **Prediction: positive; strength full.**
- **`PK3-b` (A2).** `A2` holds, by `a2_every_substratum`. **Prediction: positive; strength full.**
- **`PK3-c` (A3).** `A3 (2 * d)` holds. **Prediction: positive; strength high** — the merged
  `waveSubstratum_A3` argument, `Finset.card_image_le`, applies to the same neighbourhood.
- **`PK3-d` (A4).** `A4Exact` holds **under the translation-invariance hypothesis on the link
  coupling**, `∀ v i j, M (i + v) (j + v) = M i j`, which the manuscripts' isotropic coupling
  supplies and which the constant coupling satisfies outright. **Prediction: positive under that
  hypothesis; strength high.** **What would falsify it:** the translation of the neighbourhood not
  matching, `nbrs d L (i - v) ≠ (nbrs d L i) - v` — it does match, by the definition of `nbrs` as an
  image of `i + dir p`. **Reported without its hypothesis it is a defect**, and hazard 11 names that.
  `A4Exact` for a general link coupling is **false** and the round says so.
- **`PK3-e` (A5).** `A5` holds. **Prediction: positive; strength full** — each `M i j` is additive
  and the sum is finite.

**Bounded reading, frozen:** `PK3` is about the packaged carrier, an object built in the kernel from
the data the manuscripts state. It is **not** a statement that the manuscripts' physical substratum
satisfies `A1`–`A5`; that identification is a premise no round can discharge, and hazard 1 names it.

#### `PK4` — the internal index of the packaged carrier is not the degenerate one

**Kernel, level 2.** On `V = Fin 6 → ZMod q` with `q ≥ 2` there is an additive automorphism that is
not multiplication by a unit scalar — the cyclic component shift `v ↦ fun k => v (k + 1)`, pinned by
that equation, as in the merged `d3b_witness`. Hence the site-dependent transformations available to
the packaged carrier are strictly more than the alphabet-rescaling freedom of the singleton-index
case.

**Prediction: positive; strength full.** **What would falsify it:** nothing plausible; the shift is
exhibited.

**Bounded reading, frozen:** round 1's **degeneracy** verdict (`D2-iii`: the singleton-`K`
rescalings are the amplitude-scale freedom the manuscripts assign to A5, not the internal-index
freedom of the sixth assumption) stands for `waveSubstratum`, is not touched, and **does not apply
to the packaged carrier**, which is what `PK4` establishes and all it establishes. It does **not**
say that `AddAut (Fin 6 → ZMod q)` is the manuscripts' $G(\mathbf{n})$: over
the finite alphabet there is no unitary group, and none is introduced. Hazard 12 names that.

#### `PK5` — the separate stronger condition on the packaged carrier at the symmetric point

**Kernel, level 2.** At the manuscripts' symmetric point, the constant coupling pinned by
`M₀ v = μ • v` for a unit `μ : (ZMod q)ˣ`, on the packaged carrier with `d ≥ 1`, `L ≥ 2`, `q ≥ 2`:
`A6Inv (linkF (nbrs d L) (fun _ _ => M₀)) M₀` **fails**, and `A6Glob (linkF (nbrs d L) (fun _ _ => M₀)) M₀`
**holds** — instances of the merged `d4b_mu_id` and `a6glob_constLink` at the manuscripts' site type
and component count, with the edge between distinct sites supplied by `i + dir (k, true) ≠ i` and
the two elements of `AddAut (Fin 6 → ZMod q)` by `PK4`'s shift.

**Prediction: positive; strength high.** **What would falsify it:** `L = 1`, where the torus has one
site and no edge between distinct sites, so the hypothesis of `d4b_mu_id` is unavailable; the round
states the condition `L ≥ 2` and reports the degenerate case as excluded by hypothesis, not as a
counterexample.

**Bounded reading, frozen, and it is the sharpest place the round can be misread:** this is the
**fixed-background** condition `A6-inv` failing on the packaged carrier, and `A6-inv` is **not** the
adopted meaning. The failure is the recorded reason it is not the adopted meaning — as the
definition it would refute the manuscripts' own rule for exactly the site-dependent transformations
the gauge reading needs — and it is neither a defect of the manuscripts' rule nor a failure of the
sixth assumption. **The sentence "the substratum violates A6" is forbidden in terms**, and hazard 4
names it.

### Family `CX` — the second obstacle: the complex lift

#### `CX0` — which part of the derivation needs what, by quotation

**Evidence type P** — a determination by quotation with coordinates, made from `SM.md:112`, `:114`,
`:334`, `:487`, `Substratum.md:162` and `book/ch05-gauge-structure.md:145` and no others. For each
coordinate the execution records which of the following the passage requires of its carrier:

- **(i)** additive structure and invertibility of the site-dependent transformation, and nothing
  more;
- **(ii)** a complex scalar structure — linearity over `ℂ` — beyond (i);
- **(iii)** an inner product, unitarity as a constraint, a state or condensate, or the cubic action
  on the component index;
- **UNDECIDED** — the passage does not fix what it requires; the obstruction is quoted.

**Prediction: (i) at `SM.md:112` and `:114`; (iii) at `SM.md:334`, `:487` and `Substratum.md:162`;
(ii) at `book/ch05-gauge-structure.md:145`, where the transformation is named as an element of
$\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ while the identity displayed needs only (i).
Strength: high** for `SM.md:112`, `:114`, `:334` and `Substratum.md:162`; **medium** for `SM.md:487`,
whose "locally $\mathrm{U}(6)$ invariant" names the group without displaying the identity it is
invariance of.

**What would falsify it:** a coordinate inside the covariance statement itself that consumes the
inner product or unitarity — then that coordinate is reported **(iii)**, the prediction that the
covariance statement needs only additive structure is refuted at that coordinate, and `CX1`'s
bounded reading is narrowed accordingly in the report. **No manuscript is edited whatever `CX0`
returns.**

#### `CX1` — the covariance statement at a complex carrier is inside the interface

**Kernel, level 2.** `A6Cov N M` at `V = Fin 6 → ℂ` — the interface's own predicate, at an alphabet
the interface already admits, with no new definition and no structure added — and `a6cov_all` gives
it for every `N` and every link coupling `M : ι → ι → (V →+ V)`.

**Prediction: positive; strength full.** `a6cov_all` is stated for an arbitrary additive commutative
alphabet and `Fin 6 → ℂ` is one. **What would falsify it:** an instance obligation that the complex
carrier cannot meet — none is expected, the carrier being an additive commutative group by the
mathlib instances the interface already uses.

**Bounded reading, frozen:** what comes inside the interface is the **covariance identity**. The
inner product, unitarity as a constraint, the condensate $\Sigma$, the stabilizer in $\mathrm{U}(6)$,
the cubic decomposition and the reduction to $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$
do **not** come inside, and none of them is introduced. Furthermore `A6Cov` at the complex carrier
quantifies over **all** additive automorphisms of `Fin 6 → ℂ`, a strictly larger class than the
unitary group; the statement therefore **contains** the manuscripts' transformation law as a
specialization and is not identical to it. Reporting the general statement as a $\mathrm{U}(6)$
theorem, or the specialization as the general statement, is a defect, and hazard 13 names it.

#### `CX2` — the manuscripts' site-dependent transformation is an instance

**Kernel, level 2, with a frozen fallback.** Every `ℂ`-linear automorphism of `Fin 6 → ℂ` is an
additive automorphism of it, so a site-dependent family of such automorphisms is a
`g : ι → AddAut V`, and `SM.md:112`'s transformation law
$M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$
is `gaugeLink g M` at that carrier.

**Prediction: positive; strength high.** The step is that a `ℂ`-linear equivalence forgets to an
additive equivalence. **Frozen fallback, and using it is not a negative:** if carrying the statement
all the way to a matrix unitary group in the pinned mathlib exceeds the round, the execution states
`CX2` for a `ℂ`-linear automorphism pinned by its defining equation, records that **unitarity is not
consumed by the covariance statement** — which is `CX0`'s prediction (i) at `SM.md:112` in kernel
form — and reports the matrix-unitary packaging as analysis, at level 3, labelled so. **What would
falsify the target itself:** a `ℂ`-linear automorphism that is not additive, which cannot occur.

**Bounded reading, frozen:** that the manuscripts' transformation is an instance of the interface's
transformation class is a statement about the **class**, not about the group. It does not identify
`AddAut (Fin 6 → ℂ)` with $\mathrm{U}(6)$, does not say that unitarity is derivable, and does not
say that unitarity is dispensable in the manuscripts' derivation — only that the covariance identity
does not consume it.

#### `CX3` — the complex carrier is not a `Substratum` satisfying A1, and the round proves it

**Kernel, level 2 — a preregistered negative.** A `Substratum` with `ι = Fin d → ZMod L`,
`V = Fin 6 → ℂ` and `R.F = linkF (nbrs d L) M` is constructible by exactly the argument of `PK1`,
and on it:

- **`CX3-a`** — `A2` and `A5` hold, and `A3 (2 * d)` holds, and `A4Exact` holds under the
  translation-invariance hypothesis of `PK3-d`. **Prediction: positive; strength high** — the `PK3`
  proofs do not use finiteness of the alphabet.
- **`CX3-b`** — `A1` **fails**: `Substratum.A1` is `Finite (ι → V × V)` and `Fin 6 → ℂ` is infinite.
  **Prediction: the failure is proved; strength high** — the formal cost is exhibiting an injection
  from an infinite type, and the statement is a proved negative, not a failed search.

**Bounded reading, frozen, and it is the round's most load-bearing distinction:** "bringing the
complex lift inside the interface" can mean two different things, and they come apart here. The
**covariance statement** comes inside (`CX1`, `CX2`). The **complex carrier does not come inside as
a substratum in the kernel's sense**, because the interface's first axiom is finiteness and the
complex carrier is infinite. That is not a defect of the interface and not a defect of the
manuscripts: the manuscripts' substratum is the finite object of `SM.md:306` and the complex carrier
is the object on which the derivation of `SM.md:114` and Theorem 5 is conducted. The round reports
both facts together and names the residual, and it does **not** weaken `A1`, add a finiteness
parameter, or define a second substratum structure. **What would falsify `CX3-b`:** nothing
plausible.

### Family `AS` — the assembled statement

#### `AS1` — the covariant form reaches the second-order dynamics

**Kernel, level 2.** For a link-coupled rule, any site-dependent `g`, and the phase-space map
`leapEquiv`: the second-order map of the transported rule is carried to the second-order map of the
original by the pointwise action on both slots,

```
leapEquiv (linkF N (gaugeLink g M)) (fun i => (g i (x i).1, g i (x i).2))
  = fun i => (g i (leapEquiv (linkF N M) x i).1, g i (leapEquiv (linkF N M) x i).2)
```

stated once, polymorphically in the alphabet, and instantiated at `V = Fin 6 → ZMod q` and at
`V = Fin 6 → ℂ`.

**Prediction: positive; strength high.** The proof shape is the merged `leap_siteAct` with
`a6cov_all` supplying the commutation instead of a hypothesis; the second-order term
$-\boldsymbol{\phi}(\mathbf{n}, t-1)$ passes because each `g i` is additive. **What would falsify
it:** the leap's subtraction not commuting with `g i` — it does, by `map_sub`.

**Bounded reading, frozen:** this is what makes the covariance a statement about **the dynamics** of
`SM.md:306`–`:308` rather than about the first-order half of it. It is still the identity
`a6cov_all` records, and it is still a statement whose content is the interface.

#### `AS2` — the status determination

**Evidence type P.** The execution states, in two separate sentences that are never merged, what the
round settled about each half of the row's named hypothesis and what it did not, at the strength
reached, with the label left where it stands. The outcome menu and what each licenses is the section
"What each outcome licenses for the row's label, and what it does not" below.

## The preregistered predictions, and their strengths

| target | type | prediction | strength | what would falsify it |
| --- | --- | --- | --- | --- |
| `PK0` | P | (a) for every datum; the normalization absorbed into `M`, the second-order term carried by the leap | high | a datum with no field and no parameter — reported (b), and no field is added |
| `PK1` | level 2 | positive: the packaging exists, `dep` and `mem_infl` discharged | high | `mem_infl` or `dep` unmeetable for `linkF` at `nbrs d L` — a negative, reported as such |
| `PK2-a` | level 2 | positive: `R.F = linkF R.N M` for the packaged carrier | full | a packaging whose `F` is not the link-coupled map — a negative |
| `PK2-b` | level 2 | positive: `A6Cov` on its own link data, an instance of `a6cov_all` | full | — it is an instance of a merged identity |
| `PK3-a` | level 2 | positive: A1 for `NeZero L`, `NeZero q` | full | — |
| `PK3-b` | level 2 | positive: A2 | full | — `a2_every_substratum` |
| `PK3-c` | level 2 | positive: A3 with degree `2d` | high | proof effort only; the merged argument transports |
| `PK3-d` | level 2 | positive: A4Exact **under** translation invariance of `M` | high | the neighbourhood not translating — it does; without the hypothesis A4Exact is false and is reported so |
| `PK3-e` | level 2 | positive: A5 | full | — |
| `PK4` | level 2 | positive: a non-scalar additive automorphism of `Fin 6 → ZMod q` for `q ≥ 2` | full | — the shift is exhibited |
| `PK5` | level 2 | positive: at `M₀ = μ • id`, `A6-inv` fails and `A6-glob` holds on the packaged carrier, `d ≥ 1`, `L ≥ 2`, `q ≥ 2` | high | `L = 1`, excluded by hypothesis and reported as excluded |
| `CX0` | P | (i) at `SM.md:112`, `:114`; (iii) at `:334`, `:487`, `Substratum.md:162`; (ii) at `ch05:145` | high, except medium at `SM.md:487` | a coordinate inside the covariance statement consuming the inner product or unitarity |
| `CX1` | level 2 | positive: `A6Cov` at `V = Fin 6 → ℂ`, no new definition | full | an instance obligation the complex carrier cannot meet |
| `CX2` | level 2 | positive: a site-dependent `ℂ`-linear automorphism is a `g : ι → AddAut V`, and `SM.md:112`'s law is `gaugeLink g M` | high | — ; frozen fallback to the `ℂ`-linear form with the matrix-unitary packaging at level 3, which is **not** a negative |
| `CX3-a` | level 2 | positive: A2, A3, A5 and A4Exact-under-hypothesis on the complex carrier | high | a `PK3` proof secretly using finiteness of the alphabet |
| `CX3-b` | level 2 | **the failure is proved**: A1 fails on the complex carrier | high | nothing plausible |
| `AS1` | level 2 | positive: the covariant phase-space form, at both alphabets | high | the leap's subtraction not commuting with `g i` — it does |
| `AS2` | P | the two halves reported separately, the label left where it stands | — | — |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction named and
quoted. **A negative is a real outcome for every kernel target** and is reported as a result, not as
a shortfall. **No target has a fallback other than `CX2`'s**, which is frozen above and labelled at
level 3 where it fires.

## The STATUS RULE, FROZEN

1. **The round may not move the `ROADMAP` label beyond what it proves.** The row `P1 — A6` carries
   `CONDITIONAL` at the start state and carries `CONDITIONAL` at the end of this round's execution.
   A stronger or weaker label is an **owner decision**, taken after this round's result is reported,
   in a separate propagation round, and it is not this round's to take or to recommend into the file.
2. **The execution's `ROADMAP` edit is confined to the `P1 — A6` row and its section**, and within
   them to the reasons the row gives and the round's links. The label cell reads `**CONDITIONAL**`
   before and after. No other row, section or research status is touched. If the row's reasons
   change, guard `R7-A6D`'s row clause and its `DERIVED`-overclaim mutation control are re-pinned to
   the new row string and to nothing else, and the `DERIVED` mutation control is preserved as a
   mutation control.
3. **The round may not identify any two of the four readings.** `A6-inv`, `A6-cov`, `A6-glob` and
   `A6-sd` are four objects on three interfaces. Any sentence using the bare name outside a
   quotation, the row name, or a guard, family, directory or round name is a defect.
4. **The round may not report the gauge-group derivation settled**, in either direction. Theorems 5
   and 7 of `SM`, H-link, H-cust, the $(3,2,1)$ decomposition, the condensate stabilizer, the
   reduction to $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ and the Wilson action are
   neither consumed nor judged.
5. **The round must record UNDECIDED, with the obstruction named and quoted, wherever it cannot
   settle a target**, and must report every negative as a computed certificate rather than as a
   failed search.
6. **The round may not edit any manuscript.** `papers/` and `book/` are read and never written. A
   point at which the manuscripts' intended reading is found unsettled is recorded in the result and
   left for an owner call.
7. **The round may not enlarge the interface beyond the alphabet instantiation recorded above.** No
   field is added to `Substratum`; no unitary group, inner product, condensate, state, cubic group
   action, connectivity notion or state-dependent rule family is defined; no predicate is defined for
   `A6-sd`; `A1` is not weakened and no second substratum structure is introduced.
8. **The round may not define a covariance predicate on `Substratum` and name it a reading of the
   sixth assumption.** The bridge between the packaged carrier and the interface is the equation of
   `PK2-a`. If the packaging predicate of budget slot 5 fires, it is named for what it is — that a
   substratum's rule is link-coupled — and never as a reading, a strengthening or a variant of the
   assumption.
9. **Round 1's artifacts, the propagation's control plane, the interface audit, the manuscript-axiom
   audit and every historical round record are read and never edited**, and are blob-pinned by the
   execution guard so that this is a checked fact rather than a promise.

## What each outcome licenses for the row's label, and what it does not

The vocabulary is read literally from `ROADMAP.md:22–31`. **In every case below the round leaves the
label where it stands**; what follows is what the outcome would license an owner to decide, recorded
in advance so that the decision is made against a preregistered statement rather than against a
result already in hand.

**If every target lands as predicted.** What is then kernel-proved: that a `Substratum` built from
the data the manuscripts state — cubic torus, six-component alphabet over `ℤ/qℤ`, axis
neighbourhood, link-valued coupling, second-order leap — exists, satisfies `A1`–`A5` (with `A4Exact`
under translation invariance of the coupling), has the interface's link-coupled map as its update
map, and therefore satisfies the adopted reading on its own link data; that the covariance statement
is statable and proved at a complex six-component carrier with no new definition; that the
manuscripts' site-dependent transformation is an instance of the interface's transformation class;
that the covariant form reaches the second-order dynamics; and that the complex carrier is **not** a
substratum satisfying `A1`. The named hypothesis of the row, **as the propagation stated it**, is
then discharged in its packaging half and discharged **for the covariance statement only** in its
lift half.

That outcome would license an owner to consider a stronger label, and the round records, in advance,
the three things such a label would **not** be entitled to assert:

- **It would not assert that a condition was tested and survived.** `A6Cov` holds identically on
  every link-coupled rule (`a6cov_all`); a positive says the manuscripts' rule is of the covariant
  form and says nothing more. A row labelled as derived would have to be read as "the manuscripts'
  carrier is an instance of the covariant interface", never as "the assumption was verified".
- **It would not assert anything about the physical substratum.** The packaged carrier is a formal
  object built from stated data; that the physical substratum is that object is a premise no round
  can discharge, and it is the residual that survives every outcome below.
- **It would not assert a derivation of the gauge group.** Satisfying covariance on a packaged
  carrier is not a derivation of $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$, is not a
  step of Theorem 5 or Theorem 7, and licenses no sentence about the Standard Model. The residual on
  the lift side is precisely the part `CX0` predicts to be class (iii): the inner product, unitarity
  as a constraint, the condensate, the stabilizer and the cubic decomposition, none of which this
  round brings inside and none of which it attempts.

**If `PK1` or `PK2-a` is negative.** The packaging is impossible in the interface as it stands, the
obstruction is named, and the row keeps `CONDITIONAL` with its first half re-stated in the narrower
terms the negative supplies. That is a real result: it would say the interface's `Substratum` cannot
hold the manuscripts' rule without a field it does not have, which is a finding about the interface
and a candidate scope for a later owner-called round.

**If `PK3-d` is negative for the manuscripts' coupling as they state it.** The packaged carrier
would satisfy `A1`, `A2`, `A3`, `A5` and not `A4Exact`, the complete `A1`–`A6` formal package the
row's closing column names would be out of reach for that carrier, and the round would report the
coupling class for which `A4Exact` does hold. The row keeps `CONDITIONAL`, its hypothesis narrowed to
the A4 clause, and the finding is recorded and not repaired.

**If `CX1` or `CX2` is negative or UNDECIDED.** The lift half stays undischarged, the obstruction is
named, and the row keeps `CONDITIONAL` with its second half re-stated. `CX3-b` landing while `CX1`
does not would be the sharpest form of that outcome and would be reported as such.

**If `CX3-b` lands, whatever else does.** The round records that the complex carrier is not a
substratum in the kernel's sense, and the row's second half is re-stated to distinguish the
covariance statement from the carrier. **No outcome of this round licenses weakening `A1` to make
the complex carrier fit**, and hazard 9 names that.

**If any target is UNDECIDED.** The obstruction is named and quoted, the row keeps `CONDITIONAL`,
and the residual sentence of `AS2` carries the UNDECIDED target explicitly rather than reporting
around it.

## What none of these outcomes licenses

- **Nothing here says the sixth assumption holds of the physical substratum, or fails of it.** Every
  kernel target is about a carrier built in the kernel; `PK0`, `CX0` and `AS2` are about text.
- **Nothing here touches the Standard-Model gauge-group derivation.** Theorems 5 and 7 of `SM`,
  H-link, H-cust, the $(3,2,1)$ decomposition, the condensate stabilizer, the reduction to
  $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ and the Wilson action are neither consumed
  nor judged, in either direction. The conditional carrier reading of `SM.md:110` is preserved
  exactly as it stands.
- **Nothing here identifies any two of the four readings**, and nothing adopts, revises or ranks a
  reading. The adopted meaning is the propagation's and is consumed, not re-adjudicated.
- **Nothing here says that `A6-cov` is a constraint on the manuscripts' rule.** Its content is the
  covariant interface, and a positive is an instantiation result, not a verification result.
- **Nothing here is a complex-lift interface.** The alphabet is instantiated at a complex carrier;
  no unitary group, inner product, condensate, state or cubic action enters the interface, and the
  part of the derivation that needs them stays outside and is named as the residual.
- **Nothing here decides whether A4 and the sixth assumption overlap** (`Substratum.md:104`), whether
  the assumption is independent of A1–A5, or what "the cubic-symmetric coupling matrix" denotes —
  `M` remains a parameter of every reading, so both the scalar `μ I_6` and the block-scalar
  equivariant object are instances and neither is chosen.
- **Nothing here formalizes `A6-sd`**, and nothing is said about H-Bell, preparation-indexed
  adjacency or the state-dependent Einstein construction.
- **Nothing here is about Track B, `P0`, physical C4, the fibre-Gram classification, Lemma 24.1,
  H-B or hydrodynamics.**
- **The bare-carrier finding stands untouched.** The manuscript-axiom audit's verdict — that no
  manuscript-level conjunct of A1–A6 is a faithful predicate of the bare operational theory, which
  has no distinguished substratum — is about a different carrier and is neither consumed nor
  weakened.
- **No manuscript is edited**, and no `ROADMAP` status other than the `P1 — A6` row's reasons and
  links is touched.

## Numbered hazards

1. **Reading a packaging positive as a statement about the physical substratum.** The packaged
   carrier is a formal object built from the data the manuscripts state. "The substratum satisfies
   A6" is not an outcome of this round in any of its senses.
2. **Reading `PK2-b` as a verified constraint.** `A6Cov` holds identically. A sentence of the form
   "the assumption was checked on the manuscripts' rule and holds" asserts something the kernel does
   not say, and is a defect even on a full positive.
3. **Letting an instantiation result slide into the Standard Model.** Covariance on a packaged
   carrier is not a derivation of the gauge group. Any sentence connecting this round's outcome to
   $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$, to Theorem 5, to Theorem 7, to H-link or
   to H-cust is a defect, including a hedged one.
4. **Reading `PK5` as "the substratum violates A6".** `PK5` is the separate stronger
   fixed-background condition failing, which is the recorded reason it is not the adopted meaning.
   The sentence is forbidden in terms.
5. **Identifying the interface's transformation class with a group the manuscripts name.**
   `AddAut (Fin 6 → ZMod q)` is not $\mathrm{GL}(6,\mathbb{Z}/q\mathbb{Z})$ by fiat and
   `AddAut (Fin 6 → ℂ)` is not $\mathrm{U}(6)$; each containment or coincidence that is used must be
   proved and cited at its own strength, and the merged `addAut_zmod_smul` is the only such result in
   hand.
6. **Reporting `CX1` as the manuscripts' covariance.** `A6Cov` at the complex carrier quantifies over
   all additive automorphisms and contains the manuscripts' law as a specialization; the two
   statements are reported separately and never as one.
7. **Calling `CX1`+`CX2` "the complex lift brought inside the interface" without `CX3`.** The
   covariance statement comes inside; the carrier does not come inside as a substratum. Reporting the
   first without the second overstates the round.
8. **Reporting `CX3-b` as a defect of the interface, of the manuscripts, or of the complex lift.** It
   is the boundary between the finite substratum and the carrier the derivation is conducted on,
   proved.
9. **Weakening `A1`, adding a finiteness parameter, or defining a second substratum structure** so
   that the complex carrier fits. The round proves the boundary; it does not move it.
10. **Adding a field to `Substratum`**, or defining a covariance predicate on `Substratum` and
    naming it a reading. Status rule clauses 7 and 8.
11. **Reporting `PK3-d` without its translation-invariance hypothesis.** `A4Exact` for a general link
    coupling is false; the hypothesis is part of the statement and is reported with it every time.
12. **Reading `PK4` as more than the removal of the degeneracy verdict.** It says the packaged
    carrier's transformation class is larger than the alphabet-rescaling freedom of the
    singleton-index case. It does not identify that class with the manuscripts' $G(\mathbf{n})$.
13. **Treating the normalization, the isotropy constraint or the second-order term as silently
    absorbed.** `PK0` records where each goes: the normalization into the coupling parameter, the
    isotropy constraint into the link-coupled form, the second-order term into the leap. A
    positive that quietly changes one of those placements is a different theorem.
14. **Taking `d`, `L`, `q` or the coupling as settled.** The packaged carrier is a family in those
    parameters; `d = 3` is an empirical filter in the manuscripts and no target of this round asserts
    it, and no instance of `M` is chosen.
15. **Deciding the denotation of "the cubic-symmetric coupling matrix" by instantiating `M`.** Round
    1 recorded the denotation as unsettled and this round does not resolve it by choosing.
16. **Reporting a failed proof search as a negative.** Every negative is a computed certificate.
    "Could not prove it" is UNDECIDED with the obstruction named, and the two are never interchanged.
17. **Moving the label inside the round**, recommending a label into the result note, or writing the
    result note so that a stronger label reads as already earned.
18. **Editing a manuscript, a round-1 artifact, the propagation's control plane, or a historical
    round record** — including "helpfully" correcting a sentence that describes the state an earlier
    round consumed.
19. **Importing Track B, `P0`, physical C4, H-Bell, Lemma 24.1, H-B or hydrodynamics** as evidence
    here, or exporting these findings there.
20. **Reading only one book source.** Where a book coordinate is quoted for `CX0`, the chapter file
    and `book/The-Incompleteness-of-Observation-FULL.md` are both read, and a difference between
    them is recorded as such and not repaired.
21. **Using the words the repository's style rule bans**, and never the bare reading name outside the
    permitted positions of the notation rule.

## Definition budget

The execution introduces **at most five** top-level definitions, in one module, and these are the
five:

1. **`linkRule`** — the `Rule ι V` whose `F` is `linkF N M`, whose `N` and `infl` are the given
   neighbourhood function, with `dep` and `mem_infl` discharged. *Needed:* `Substratum` carries a
   `Rule` and `Rule` has proof fields, so the packaging cannot be stated without it.
2. **`linkSubstratum`** — the `Substratum` built from `linkRule` at a site type, an alphabet, a
   neighbourhood function and a link coupling, all parameters. *Needed:* it is the object `PK1`–`PK5`
   and `CX3` are about, and it is stated once and instantiated at both alphabets so that the finite
   and complex carriers are the same construction and the difference between them is visible.
3. **`TranslationInvariant`** — the hypothesis `∀ v i j, M (i + v) (j + v) = M i j` on a link
   coupling. *Conditional:* fires only if `PK3-d` and `CX3-a` cannot be stated readably with the
   hypothesis written inline. It is a hypothesis, never an axiom and never a reading.
4. **A complex-carrier abbreviation** for `Fin 6 → ℂ`. *Conditional:* fires only if `CX1`–`CX3`
   cannot be stated readably without it. It abbreviates a type and introduces no structure.
5. **`IsLinkCoupled`** — `∃ M, 𝒮.R.F = linkF 𝒮.R.N M`, the packaging property of a substratum.
   *Conditional:* fires only if `PK2-a` and `AS2` cannot be stated without it. **It is named for what
   it is — that a substratum's rule is link-coupled — and never as a reading, a variant or a
   strengthening of the sixth assumption**, per status rule clause 8.

**A sixth definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. In particular: **no field is added to `Substratum`**; **no predicate for
`A6-sd`**; **no unitary group, inner product, condensate, state or cubic group action**; **no
connectivity predicate**; **no phase-space form of any reading as a separate definition** — `AS1` is
a theorem about `siteAct`, `gaugeLink` and `leapEquiv`; and **no witness, carrier, transformation,
configuration or coupling is a top-level definition** beyond slots 1, 2 and 4 — each is a bound
variable pinned by an equation in the statement that needs it. The merged modules' definitions are
**reused, never redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for `PK1`,
`PK2`, `PK3`, `PK4`, `PK5`, `CX1`, `CX2`, `CX3` and `AS1`, with the single preregistered exception of
`CX2`'s frozen fallback, whose matrix-unitary packaging is reported at **level 3** and labelled so.

**Evidence type P** — a prose determination by quotation with coordinates against the blobs in the
start-state table — for `PK0`, `CX0` and `AS2`. A type-P result is **labelled as such wherever it is
reported**, is never listed among the kernel results, and is never counted in the axiom table.

UNDECIDED is permitted for every target, with the obstruction named and quoted. No floating-point
evidence enters any label; there is none in this round.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, plus archive mode

1. **This preregistration blob is merged into `main` before any execution-specific object of this
   round enters the repository tree** — any Lean definition or proof about the packaged carrier, the
   complex carrier, the covariant phase-space form or the packaging property; any probe; any guard;
   any result artifact; any `ROADMAP`, README or census edit of this round. **The single permitted
   exception is the analysis recorded inside this control-plane blob itself**, merged *as* the
   freeze — the frozen objects, the targets, the predictions, the proof shapes named in them — so
   that no execution-specific artifact needs to precede it.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and it is never updated from later `main`.
3. **The execution guard `R7-A6I` pins both**: this file's blob SHA **by content**, through
   `_bb_blob`, with a drift control (one byte appended fails the pin); and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An unresolvable
   head **fails closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and `H`
   the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a
   descendant of `B`**, fail-closed. A guard that checks only the head does not discharge this clause.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching an
   absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated commit
   alike.
7. **Archive mode, the rule of PR #599.** After the execution pull request merges, neither `HEAD` on
   `main` nor a later pull request's head is the execution head, so the guard re-runs **the same
   strong check against the sealed execution head pinned by SHA together with its merge commit**: the
   pinned merge's second parent must equal the sealed head; the sealed head must pass clause 5
   against `B` exactly as it did in its own run; and both must be reachable from the current target —
   the real `pull_request.head.sha` in PR CI, `HEAD` otherwise — each fail-closed, through the
   existing `_rbr_archive_ancestry` mechanism and not a re-implementation. The pins are added in a
   follow-up that records the sealed head after exact-head review and merge; until then the guard
   runs in execution mode. Nothing about the base or the blob pin changes in archive mode.
8. **`R7-A6I` also pins, by content, the artifacts this round must not edit**: round 1's
   `preregistration.md` (`afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`) and `result.md`
   (`331b1928adde22d5c716a92adb864b523d0c09b8`), and the covariance propagation's control plane
   (`e7cb7013747f783135c8e166d290ce6670df0ae9`), so that status rule clause 9 is a checked fact and
   not a promise.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**, and the two are named as such wherever both appear.

**Guard tag reserved: `R7-A6I`.** It is absent from `verification/lean/edge_rigidity_probe.py` at
blob `c7e9827c6eb2be9ac7cb660f964d5b610eb3411c` and is reserved for this round's execution; on a
collision at the execution base the name is mechanically adjusted and the adjustment is reported.

## Immutable inputs

Cited and consumed **unmodified**: `Substratum`, `Substratum.Conf`, `Substratum.φ`, `A1`–`A5`,
`A4Exact`, `A4`, `A3Family`, `a2_every_substratum`, `a1_of_finite`, `a3_of_fintype`, `a4_of_exact`;
`shiftBy`, `dir`, `dir_flip`, `nbrs`, `mem_nbrs_symm`, `waveF`, `waveRule`, `waveSubstratum` and
`waveSubstratum_A1`–`_A5`; `Rule` and `leapEquiv`; `siteAct`, `PreservesPointwise`, `A6Inv`,
`A6Glob`, `linkF`, `gaugeLink`, `A6Cov` and all sixteen named results of the round-1 module, in
particular `a6cov_all`, `a6glob_of_a6inv`, `a6glob_constLink`, `leap_siteAct`, `d4a_single_edge`,
`d4b_edge_rigidity`, `d4b_not_a6inv_of_nonconstant`, `d4b_symmetric_point`, `d4b_mu_id`,
`addAut_zmod_smul` and `addAut_nontrivial_of_ne_neg`; round 1's `D1`–`D4` and its bounded readings;
the covariance propagation's owner decision, adopted meaning, label reasons and named hypothesis; the
interface audit's Q1 verdict table and the manuscript-axiom audit's verdict for the bare operational
carrier; and every merged label of every programme.

**The audits' rule is frozen with them:** a predicate found on inspection to be stronger, weaker or
differently scoped than the manuscript axiom is recorded as such and not adjusted to fit.

## Non-doings

The round does not: run any part of the execution before this file is merged; introduce any
execution-specific object before then (the analysis inside this blob is the permitted exception, per
chronology clause 1); adopt, revise or rank any reading; prove or refute the sixth assumption for
anything physical; package the manuscripts' rule by changing `Substratum`; build a unitary,
inner-product, condensate or cubic-action interface; formalize `A6-sd`, $\mathcal{G}_{\rm sub}$ or
any connectivity notion; touch the Standard-Model derivation chain or any of H-link, H-cust, H-Bell;
say anything about Track B, `P0`, physical C4, Lemma 24.1, H-B or hydrodynamics; decide the A4/A6
overlap or the denotation of "the cubic-symmetric coupling matrix"; edit any manuscript, any round-1
artifact, the propagation's control plane or any historical round record; change the `P1 — A6` row's
label or any other `ROADMAP` status; or recommend a label.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**: the commit SHA locates the tree, the blob SHA is what the guard compares.
- Once merged, this file is immutable; execution-affecting corrections are append-only amendments,
  separately frozen and merged before the work they affect.
- **This pull request carries this file alone.** No Lean, no probe, no guard, no manuscript edit, no
  `ROADMAP`, README or census edit.
- **Then exactly one execution pull request**, based on exactly the merge commit of this one,
  carrying the Lean module `OIBridge/A6Instantiation.lean`, the result note in this round's
  directory, the probe guard `R7-A6I` (pinning this blob by content with its drift control, pinning
  the three untouched artifacts by content, resolving the real `pull_request.head.sha`, certifying
  clause 5's side-history-excluding ancestry, and carrying the archive-mode pins once merged), the
  `ROADMAP` propagation confined to the `P1 — A6` row's reasons and links with the label unchanged,
  the `R7-A6D` re-pin of the row clause and its `DERIVED` mutation control if and only if the row's
  reasons change, the verification landing-page paragraph, and the census entry. **No manuscript
  changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**

## Allowed final report

1. **`PK0`** — the datum table with each classification by quotation, labelled type P, and the two
   recorded readings on the normalization and the isotropy constraint;
2. **`PK1`, `PK2`** — the packaging, the bridge equation, and the covariance instance, with the
   bounded reading in this file's words: the identification is the content, and the covariance
   carries exactly that the rule is link-coupled;
3. **`PK3`** — A1–A5 on the packaged carrier, each at its own strength, with `PK3-d`'s hypothesis
   stated every time it is reported;
4. **`PK4`** — the non-scalar automorphism, with round 1's degeneracy verdict recorded as standing
   for `waveSubstratum` and not applying to this carrier, and nothing further;
5. **`PK5`** — the fixed-background condition failing and the global specialization holding at the
   symmetric point on the packaged carrier, with the forbidden reading restated;
6. **`CX0`** — the coordinate table with each requirement class by quotation, labelled type P;
7. **`CX1`, `CX2`** — the covariance statement at the complex carrier, the instance relation for the
   manuscripts' transformation, the fallback label if it fired, and the bounded reading: the
   identity comes inside, the group does not, and the general statement contains the specialization;
8. **`CX3`** — A2, A3, A5 and A4Exact-under-hypothesis on the complex carrier, and the **proved
   failure of A1**, reported together with the distinction they establish;
9. **`AS1`** — the covariant phase-space form at both alphabets;
10. **`AS2`** — the two halves of the row's named hypothesis, reported in two sentences that are
    never merged, at the strength reached, with UNDECIDED targets carried explicitly;
11. what the outcomes do **not** license, in this file's wording, and the row's label recorded as
    unchanged with the stronger-label decision named as **open, the owner's, and not this round's**;
12. the points at which the manuscripts' intended reading was found unsettled, listed and not
    resolved;
13. the definition count against the five-slot budget, with conditional slots marked fired or unused;
14. the chronology certification, naming the property certified — no commit reachable from the
    execution head lies outside the control-plane merge's descendants — and, once merged, the
    archive-mode pins;
15. the axiom table, one line per named kernel result, with no type-P item in it.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **The normalization $\frac1d$ of `SM.md:308`.** The freeze carries it inside the coupling
   parameter `M` rather than as a separate scalar, because `linkF`'s coupling is exactly a map
   `V →+ V` per ordered pair of sites and the manuscripts' own text at `:306` gives the unnormalized
   isotropic form with $M^{(j)} = M$. Whether $\frac1d$ is available in `ℤ/qℤ` at a given `d`, `q` is
   not decided and is not needed: `M` is a parameter and no instance is chosen.
2. **Link coupling versus site coupling.** The manuscripts' `:306` writes one matrix `M`; `:112`
   writes the link-valued $M(\mathbf{n}, \hat{e}_j)$. Round 1 froze the site coupling as the constant
   link coupling and this round keeps that reading, packaging with the link-valued form so that the
   constant case is an instance. Which form `Substratum.md:102`'s "the coupling data carried on the
   links" denotes at each coordinate is not re-adjudicated.
3. **Ordered pair of sites versus site and direction.** `linkF`'s coupling is indexed by an ordered
   pair; the manuscripts index by a site and a direction. Round 1 froze the pair indexing; the round
   keeps it and records that the two agree on the axis neighbourhood, where the direction is
   recoverable from the pair, without proving a statement about neighbourhoods where it is not.
4. **`d = 3` and `q`.** The packaged carrier is a family in `d`, `L` and `q`. The manuscripts fix
   `d = 3` by empirical filters and `K = 6` by the link count at `d = 3`; the round fixes the
   component count at six, because that is the object the owner's framing names, and leaves `d`, `L`
   and `q` as parameters. Whether `K = 6` should be tied to `d = 3` inside the packaging is not
   decided here.
5. **What "inside the interface" means for the complex lift.** The freeze splits it into the
   covariance statement and the carrier, and `CX1`–`CX3` report the two separately. Whether an owner
   wishes the row's second half to be read as discharged when only the first is settled is recorded
   as the owner's call and is not taken here.
6. **`SM.md:487`'s "locally $\mathrm{U}(6)$ invariant".** The coordinate names a group and an
   invariance without displaying the identity it is an invariance of, so `CX0`'s class for it is
   predicted at medium strength and the freeze does not decide whether it intends the covariant
   statement of `:112`–`:114` or the fixed-background one. It is reported by quotation and left.

Status: preregistered; execution follows only after this file is merged alone, on a branch based on
exactly its merge commit, under guard `R7-A6I`.
