# Substratum — A6 instantiation, round 2: does the manuscripts' substratum instantiate the covariant interface? — RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`6f991c1348e0c568261894c41b129b7f942abee6`, merged into `main` as
`3e5d6a8f75166581213b6c5b7c0dbca1671b030e` (PR #623) — the freeze's mandated execution base.

**This is an instantiation round, and the outcome below is read accordingly.** The interpretation
problem is settled elsewhere: `A6-cov` is the adopted publication meaning and the `ROADMAP` row
`P1 — A6` reads `CONDITIONAL`. This round asks whether the objects the manuscripts actually carry
are instances of the interface on which that meaning is stated, in the two halves the freeze keeps
**apart**. It does not re-open the interpretation, adopts, revises or ranks no reading, and **does
not move the row's label**.

**The organizing caveat, stated first because it governs every positive below.** Round 1 proved
`a6cov_all : ∀ N M, A6Cov N M` — the adopted reading holds **identically** on every link-coupled
rule of the interface, so its content is the covariant interface itself and not a constraint. A
full positive therefore says exactly that the manuscripts' rule **is of that form**. It does
**not** say that a nontrivial condition was tested and survived. Any sentence of the form "the
assumption was checked on the substratum and holds" would be a defect even on a full positive, and
this note repeats the caveat wherever it reports one.

**Notation.** `A6-cov`, `A6-inv`, `A6-glob` and `A6-sd` are four objects on three interfaces and
**no two of them are identified here**. The bare name appears only inside a quotation, in the row
name `P1 — A6`, and in guard, family, directory and round names.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `3e5d6a8f75166581213b6c5b7c0dbca1671b030e` (merge of PR #623) |
| This round's frozen control plane | `preregistration.md`, blob `6f991c1348e0c568261894c41b129b7f942abee6` — matches the freeze |
| Round 1's control plane and result, read and never edited | `../a6-background-independence/preregistration.md`, blob `afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`; `../a6-background-independence/result.md`, blob `331b1928adde22d5c716a92adb864b523d0c09b8` — both match the freeze |
| The covariance propagation's control plane, read and never edited | `verification/audits/foundations/a6-covariance-propagation-audit.md`, blob `e7cb7013747f783135c8e166d290ce6670df0ae9` — matches the freeze |
| The round-1 module | `verification/lean-mathlib/OIBridge/BackgroundIndependence.lean`, blob `5ec9fe52835642724d0685d9b920f613874279d6` — matches the freeze |
| The substratum interface | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` — matches the freeze |
| `Rule` and `leapEquiv` | `verification/lean-mathlib/OIBridge/SecondOrderLayer.lean`, blob `fb7e172024597ba3e217a993169447753fa052ec` — matches the freeze |
| The interface audit and the manuscript-axiom audit | `verification/programmes/substratum/interface-audit.md`, blob `e4e0d02bfa67ea428391c0df77ad36f2689b87a3`; `verification/programmes/substratum/manuscript-axiom-audit.md`, blob `53eb9d646c51475553c3df47caec17077ab5471f` — both match the freeze |
| The queue row and its section | `verification/ROADMAP.md`, blob `8f3f9b7758bffc86ba4b2888761770fb1881a180` — matches the freeze; the row is at `:65`, the section at `:394–472`, the label vocabulary at `:22–31` |
| The verification landing page | `verification/README.md`, blob `0ee2a993279b5502ee5893c53fe63194608da51d` — matches the freeze |
| The guard file | `verification/lean/edge_rigidity_probe.py`, blob `c7e9827c6eb2be9ac7cb660f964d5b610eb3411c` — matches the freeze; `R7-A6I` absent from it at that blob |
| The census | `verification/lean-manuscript-census.json`, blob `16cc96e65357ec1e17742633f5614984c08620ca` — matches the freeze |
| The manuscript surfaces, read and never edited | `papers/SM.md`, blob `26d6cbfb230c105eb00a979c2b69c363568455dd`; `papers/Substratum.md`, blob `9ac6b732e8786897cade416b67c3f7f1df81ab84`; `papers/Main.md`, blob `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` — all match the freeze |
| The book surfaces, read and never edited | `book/ch02-substratum.md`, blob `519188eac9e4c347d7f01eb5b559cfb01df48ea9`; `book/ch05-gauge-structure.md`, blob `0f55ef3a7b5fca4172073f330f373f4b16542402`; `book/glossary.md`, blob `e811a2cc00b39d03b1a7adf263e31e63d4bcf957` — all match the freeze |
| This round's module | `verification/lean-mathlib/OIBridge/A6Instantiation.lean` |

**Every blob in the freeze's start-state table was found byte-identical at the mandated base, and
every quoted passage was located by content and found verbatim at the coordinates the freeze
records.** No target was reported UNDECIDED for a missing quotation, and **no discrepancy against
the freeze's start-state table is recorded** — see "Discrepancies" below, which records the one
judgement the classification required and which is not a divergence from the freeze.

## Outcome, in one line

**Every kernel target landed positively at evidence level 2 as predicted, including the
preregistered negative `CX3-b` as a proved negative; `CX2`'s frozen fallback did not fire, the
matrix-unitary packaging landing in the kernel at level 2; and both type-P determinations returned
their predicted classifications.** No target moved from its predicted strength, no target fell to
UNDECIDED, and no falsifier fired. **The row's label stands at `CONDITIONAL`, unchanged, and this
round recommends no label change.**

## `PK0` — what the manuscripts' rule consists of, and whether the interface has a place for each datum

**`PK0` — evidence type P**: a prose determination by quotation with coordinates against the blobs
in the start-state table, made from `SM.md:306`, `:308`, `:112`, `:372`, `:328`, `:422` and
`Substratum.md:162` and no others. It is not a kernel result and does not appear in the axiom
table.

**Outcome: (a) for every datum, as predicted; strength high.** By datum:

| datum | where the manuscripts state it | class |
| --- | --- | --- |
| site type | `SM.md:306` writes the field as $\boldsymbol{\phi}(\mathbf{n}, t)$ on the cubic lattice; `:308` sums over $j = 1 \ldots d$ axes | **(a)** — `Substratum.ι`, a site type with lattice translations, instantiated at the cubic torus `Fin d → ZMod L` |
| alphabet and component count | `SM.md:306`: "Each site now carries a K-component vector $\boldsymbol{\phi}(\mathbf{n}, t) \in (\mathbb{Z}/q\mathbb{Z})^K$"; `Substratum.md:162` fixes the multiplicities $(3,2,1)$ on $V_K$; `SM.md:372` the six link vectors | **(a)** — `Substratum.V`, **any additive commutative group**, instantiated at `Fin 6 → ZMod q`. The internal index enters only through the alphabet; `Substratum` has no field for it and **none is added** |
| neighbourhood | `SM.md:306`: the sum over $\boldsymbol{\phi}(\mathbf{n}+\hat{e}_j, t) + \boldsymbol{\phi}(\mathbf{n}-\hat{e}_j, t)$ | **(a)** — `Rule.N`, instantiated at the merged axis neighbourhood `nbrs d L` |
| coupling, in link-valued form | `SM.md:112` writes $M(\mathbf{n}, \hat{e}_j)$; `:372`: "the same 6D space on which the coupling matrix $M(\mathbf{n}, \hat e_j)$ of §4.4 acts" | **(a)** — `linkF`'s parameter `M : ι → ι → (V →+ V)`, carried as a parameter and never instantiated |
| the second-order term | `SM.md:306`: "Reversibility requires $D = -I_K$"; `:308` writes $- \boldsymbol{\phi}(\mathbf{n}, t-1)$ | **(a)** — carried by the phase-space map `leapEquiv` and **not part of `F`**, exactly as round 1 froze it |
| the normalization | `SM.md:308` writes $\frac1d M \sum_{j=1}^{d}[\cdots]$ | **(a)**, with a recorded reading — see below |
| the isotropy constraint | `SM.md:306`: "spatial isotropy requires $M^{(j)} = M$ for all $j$" | **(a)**, with a recorded reading — see below |

**The two recorded readings, exactly as the freeze fixes them, and neither is silently absorbed.**

1. **The normalization $\frac1d$ of `SM.md:308` goes into the coupling parameter `M`**, because
   `linkF`'s coupling is exactly a map `V →+ V` per ordered pair of sites and `SM.md:306`'s own
   text gives the unnormalized isotropic form with $M^{(j)} = M$. Whether $\frac1d$ is available
   in $\mathbb{Z}/q\mathbb{Z}$ at a given `d`, `q` is not decided and is not needed: `M` is a
   parameter and **no instance is chosen**.
2. **The isotropy constraint goes into the link-coupled form**, as a coupling that depends on the
   ordered pair of sites — the `SM.md:112` form — with the constant coupling one instance. The
   manuscripts index by a site and a direction and `linkF` indexes by an ordered pair; on the axis
   neighbourhood the direction is recoverable from the pair, and no statement is proved about
   neighbourhoods where it is not.

**The symmetric point $M = \mu I_6$ of `SM.md:328` and `:422`** — "the coupling matrix $M$ itself
is scalar, $M = \mu I$" — is an **instance** of the coupling parameter, used in `PK5` and chosen
nowhere else.

**No falsifier fired.** No datum was found with no field and no parameter; no datum required the
coupling to depend on the configuration, which is `A6-sd` and a different object; no datum required
`Substratum` to carry the component index as a field. **No field was added to `Substratum`.**

## `PK1`, `PK2` — the packaging, the bridge equation, and the covariance instance

- **`PK1` — level 2, positive, as predicted; strength high.** `linkRule` packages `linkF N M` as a
  `Rule ι V`, discharging `dep` — the observation that the sum over `N i` reads the configuration
  only on `N i` — and `mem_infl`, carried as the symmetry hypothesis on the neighbourhood function
  and supplied at the manuscripts' data by the merged `mem_nbrs_symm`. `linkSubstratum` builds the
  `Substratum`. `pk1_packaging` records the packaged carrier's data at the manuscripts' site type,
  alphabet and neighbourhood: `R.N = nbrs d L`, `R.infl = nbrs d L`, `R.F = linkF (nbrs d L) M`,
  with `ι = Fin d → ZMod L`, `V = Fin 6 → ZMod q` and `M` a parameter. **Neither falsifier
  occurred**: `mem_infl` is exactly `mem_nbrs_symm`, and the `dep` obligation is met by
  `Finset.sum_congr`.
- **`PK2-a` — level 2, positive, as predicted; strength full.** `pk2a_bridge`:
  `R.F = linkF R.N M` for the packaged carrier, read on the carrier's **own** neighbourhood
  function, for the very `M` the packaging carries. Stating it as a theorem rather than leaving it
  to definitional unfolding is what makes the bridge auditable. The general form is
  `linkSubstratum_bridge`, polymorphic in the alphabet.
- **`PK2-b` — level 2, positive, as predicted; strength full.** `pk2b_covariance`:
  `A6Cov (nbrs d L) M`, an instance of `a6cov_all`.

**Bounded reading of `PK2`, as frozen. The content of `PK2` is `PK2-a`** — the identification of
the manuscripts' carrier with the interface's. **Because `A6Cov` holds for every neighbourhood
function and every link coupling, `PK2-b` carries exactly the information that the packaged
carrier's rule is link-coupled, and carries no information that a condition was tested and
survived.** It is an instance of a merged identity and **not a new theorem**. `PK2-a`'s falsifier —
a packaging whose `F` is not the link-coupled map, for instance one in which the normalization or
the isotropy constraint has to be applied outside `linkF` — did not occur: both are inside `M`, as
`PK0` records.

## `PK3` — the packaged carrier against A1–A5, each at its own strength

| conjunct | result | prediction | reached |
| --- | --- | --- | --- |
| **`PK3-a` (A1)** | `pk3a_A1`, under `NeZero L`, `NeZero q` | positive, full | positive, level 2, full |
| **`PK3-b` (A2)** | `pk3b_A2`, by `a2_every_substratum` through `linkSubstratum_A2` | positive, full | positive, level 2, full |
| **`PK3-c` (A3)** | `pk3c_A3`: `A3 (2 * d)`, by `Finset.card_image_le` against the `Fin d × Bool` index of the axis steps — the merged `waveSubstratum_A3` argument on the same neighbourhood | positive, high | positive, level 2, high |
| **`PK3-d` (A4)** | `pk3d_A4Exact`: `A4Exact` **under the translation-invariance hypothesis on the link coupling**, `∀ v i j, M (i + v) (j + v) = M i j` | positive under that hypothesis, high | positive under that hypothesis, level 2, high |
| **`PK3-e` (A5)** | `pk3e_A5`, each `M i j` additive and the neighbour sum finite | positive, full | positive, level 2, full |

**`PK3-d`'s hypothesis is part of the statement and is reported with it every time.** The
manuscripts' isotropic coupling supplies it and the constant coupling satisfies it outright.
**`A4Exact` for a general link coupling is false** — without the hypothesis the rule at a
translated site consults a translated coupling and nothing makes the two agree — and this note says
so wherever `PK3-d` appears. The falsifier the freeze named, the translation of the neighbourhood
not matching, did not occur: `nbrs_sub` proves `nbrs d L (i - v) = (nbrs d L i).image (· - v)`
directly from `nbrs` being an image of `i + dir p`.

**Bounded reading of `PK3`, as frozen.** `PK3` is about the packaged carrier, an object built in
the kernel from the data the manuscripts state. It is **not** a statement that the manuscripts'
physical substratum satisfies `A1`–`A5`; that identification is a premise no round can discharge.

## `PK4` — the internal index of the packaged carrier is not the degenerate one

**Level 2, positive, as predicted; strength full.** `pk4_shift_not_scalar`: on
`V = Fin 6 → ZMod q` with `q ≥ 2` the cyclic component shift, pinned by the equation
`∀ v, g v = fun k => v (k + 1)` as in the merged `d3b_witness`, is an additive automorphism with
`∀ μ : ZMod q, ∃ v, g v ≠ μ • v`. The witness is `Pi.single 0 1` read at component `5`.

**Bounded reading, frozen.** Round 1's **degeneracy** verdict — `D2-iii`: the singleton-`K`
rescalings are the amplitude-scale freedom the manuscripts assign to A5, not the internal-index
freedom of the sixth assumption — **stands for `waveSubstratum`**, is not touched, and **does not
apply to the packaged carrier**. That is what `PK4` establishes and all it establishes. It does
**not** say that `AddAut (Fin 6 → ZMod q)` is the manuscripts' $G(\mathbf{n})$: over the finite
alphabet there is no unitary group, and none is introduced.

## `PK5` — the separate stronger condition on the packaged carrier at the symmetric point

**Level 2, positive, as predicted; strength high.** `pk5_symmetric_point`: at the constant coupling
pinned by `M₀ v = μ • v` for a unit `μ : (ZMod q)ˣ`, on the packaged carrier with `d ≥ 1`, `L ≥ 2`,
`q ≥ 2`, the **fixed-background** condition `A6-inv` **fails** on the carrier's own update map and
the global specialization `A6-glob` **holds** there — instances of the merged `d4b_mu_id` and
`a6glob_constLink` at the manuscripts' site type and component count. The edge between distinct
sites is supplied by `i + dir (k, true) ≠ i`, which needs `d ≥ 1` for an axis and `L ≥ 2` for the
step to be nonzero; the two elements of `AddAut (Fin 6 → ZMod q)` are `PK4`'s shift and the
identity.

**`L = 1` is excluded by hypothesis and is reported as excluded, not as a counterexample**: the
one-site torus has no edge between distinct sites, so `d4b_mu_id`'s hypothesis is unavailable
there.

**Bounded reading, frozen, and it is the sharpest place this round can be misread.** This is
`A6-inv`, the separate and strictly stronger **fixed-background** condition, failing on the
packaged carrier — and `A6-inv` is **not** the adopted meaning. The failure is the recorded reason
it is not the adopted meaning: as the definition it would refute the manuscripts' own rule for
exactly the site-dependent transformations the gauge reading needs. It is neither a defect of the
manuscripts' rule nor a failure of the sixth assumption. **The sentence "the substratum violates
A6" is forbidden in terms, and this note does not write it in any form.**

## `CX0` — which part of the derivation needs what, by quotation

**`CX0` — evidence type P**: a prose determination by quotation with coordinates, made from
`SM.md:112`, `:114`, `:334`, `:487`, `Substratum.md:162` and `book/ch05-gauge-structure.md:145` and
no others. It is not a kernel result and does not appear in the axiom table.

**Outcome: exactly the predicted classification at all six coordinates.**

| coordinate | what the passage says | class | strength |
| --- | --- | --- | --- |
| `SM.md:112` | the transformation law $\phi(\mathbf{n}) \to G(\mathbf{n})\,\phi(\mathbf{n})$, $M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n}+\hat{e}_j)^{-1}$ | **(i)** — a linear action on the configuration and a conjugation of the coupling; the display names no inner product, no unitarity constraint and no complex scalar structure | high |
| `SM.md:114` | "The wave equation is carried to itself: this is the covariance that (A6) asserts, and once the link variable is data transported in this way the local transformation law imposes no further condition on the rule." | **(i)** — the identity needs only that each $G(\mathbf{n})$ be additive and invertible, so that $G(\mathbf{n}+\hat{e}_j)^{-1}$ cancels against the transformed configuration at the neighbouring site | high |
| `SM.md:334` (Theorem 5) | "Let $\Sigma=\langle\phi\phi^\dagger\rangle$ be $O$-equivariant … For generic distinct block values its stabilizer in $\mathrm U(6)$ is $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$." | **(iii)** — the dagger is an inner product, $\Sigma$ is a condensate, $O$-equivariance is the cubic action on the component index, and $\mathrm U(6)$ is unitarity as a constraint | high |
| `SM.md:487` | "The substratum dynamics is locally $\mathrm{U}(6)$ invariant and does not exclude them" | **(iii)** | **medium** — the coordinate names a group and an invariance **without displaying the identity it is an invariance of**; see the unsettled points below |
| `Substratum.md:162` | "The unitary group of the bicommutant of the cubic-group action on $V_K = V_3 \oplus V_2 \oplus V_1$" | **(iii)** — a unitary group, a bicommutant, and the cubic action on the component index | high |
| `book/ch05-gauge-structure.md:145` | "Under a site-dependent transformation $G(\mathbf{n})$ … with $G(\mathbf{n}) \in \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ at each site, the matrix wave equation is invariant provided the coupling matrix transforms as $M(\mathbf{n}, \hat{e}_j) \to G(\mathbf{n})\,M(\mathbf{n}, \hat{e}_j)\,G(\mathbf{n} + \hat{e}_j)^{-1}$" | **(ii)** — the transformation is named as an element of a complex matrix group, which is a complex scalar structure beyond (i), **while the identity displayed needs only (i)** | high |

**Hazard 20 discharged.** `book/ch05-gauge-structure.md`'s three paragraphs at `:141`, `:143` and
`:145` were read in the chapter file **and** in `book/The-Incompleteness-of-Observation-FULL.md`,
and are byte-identical in both. **No difference between them is recorded, because none was found.**

**No falsifier fired.** The freeze's falsifier is a coordinate **inside the covariance statement
itself** that consumes the inner product or unitarity. `SM.md:112` and `:114` are the covariance
statement and neither consumes either: `:112` is a conjugation, `:114` is the cancellation. The
three class-(iii) coordinates are outside the covariance statement — they are Theorem 5, the gauge
boson content, and the gauge-group identification. So the prediction that the covariance statement
needs only additive structure is **not** refuted at any coordinate, and `CX1`'s bounded reading is
not narrowed. **No manuscript is edited, whatever `CX0` returns, and none was.**

## `CX1`, `CX2` — the covariance statement at the complex carrier, and the instance relation

- **`CX1` — level 2, positive, as predicted; strength full.** `cx1_complex_covariance`:
  `A6Cov N M` at `V = Fin 6 → ℂ`, for every neighbourhood function and every link coupling
  `M : ι → ι → (V →+ V)`, by `a6cov_all`. **No new definition and no structure added**: the
  interface's own predicate at an alphabet the interface already admits, the complex carrier being
  an additive commutative group by the mathlib instances the interface already uses. The falsifier
  — an instance obligation the complex carrier cannot meet — did not occur.
- **`CX2` — level 2, positive, as predicted; strength high. The frozen fallback did NOT fire.**
  Three results:
  - `cx2_clinear_forgets`: a site-dependent family of `ℂ`-linear automorphisms of `Fin 6 → ℂ` is a
    `g : ι → AddAut V` of the interface, with the transformation, its inverse and the transported
    coupling each pinned by an equation; `gaugeLink g M i j v = G i (M i j ((G j).symm v))` is
    `SM.md:112`'s law. The step is that a `ℂ`-linear equivalence forgets to an additive one, which
    is what `LinearEquiv.toAddEquiv` is.
  - `cx2_manuscript_law`: for such a family, the link-coupled rule with the transported coupling
    carries the transformed configuration exactly as the untransformed rule carries the
    configuration — the identity `SM.md:114` displays, at the complex six-component carrier, as an
    instance of `a6cov_all` and of nothing else.
  - `cx2_unitary_gaugeLink`: **the matrix-unitary packaging, in the kernel at level 2.** A
    site-dependent family of `6 × 6` complex matrices with `star U * U = 1` and `U * star U = 1`
    acts on `Fin 6 → ℂ` by `mulVec`, and that action is an additive automorphism; the transported
    coupling is `SM.md:112`'s law with $G(\mathbf{n})$ unitary and $G(\mathbf{n}+\hat{e}_j)^{-1}$
    its conjugate transpose, and the covariance identity holds of it by `a6cov_all`. **Because this
    landed in the kernel, the freeze's frozen fallback to a level-3 analysis did not fire, and no
    part of `CX2` is reported at level 3.**

**Bounded reading of `CX1` and `CX2`, as frozen.** What comes inside the interface is the
**covariance identity**. The inner product, unitarity as a constraint, the condensate $\Sigma$, the
stabilizer in $\mathrm{U}(6)$, the cubic decomposition and the reduction to
$\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ do **not** come inside, and none of them is
introduced. `A6Cov` at the complex carrier quantifies over **all** additive automorphisms of
`Fin 6 → ℂ`, a strictly larger class than the unitary group; the interface's statement therefore
**contains** the manuscripts' transformation law as a specialization and is **not identical to
it**, and the two are reported separately here and never as one. That the manuscripts'
transformation is an instance is a statement about the **class**, not about the group: it does not
identify `AddAut (Fin 6 → ℂ)` with $\mathrm{U}(6)$, does not say that unitarity is derivable, and
does not say that unitarity is dispensable in the manuscripts' derivation — only that the
covariance identity does not consume it, unitarity being used in `cx2_unitary_gaugeLink` **only to
invert the action**. The containment from the unitary matrices into the interface's transformation
class is **proved there and not asserted by fiat**, and it is the second such result in hand beside
the merged `addAut_zmod_smul`.

## `CX3` — A2, A3, A5, A4Exact-under-hypothesis at the complex carrier, and the proved failure of A1

- **`CX3-a` — level 2, positive, as predicted; strength high.** `cx3a_complex_axioms`: on the
  packaging of `PK1` at `V = Fin 6 → ℂ` — **the same construction**, `linkSubstratum` stated once
  and instantiated at both alphabets — `A2`, `A3 (2 * d)`, `A5` and `A4Exact` all hold, the last
  **under the translation-invariance hypothesis on the link coupling**, which is part of that
  conjunct and is reported with it. The freeze's falsifier, a `PK3` proof secretly using finiteness
  of the alphabet, did not occur: the four generic lemmas `linkSubstratum_A2`, `linkSubstratum_A3`,
  `linkSubstratum_A5` and `linkSubstratum_A4Exact` are stated polymorphically in the alphabet and
  each is used at both carriers.
- **`CX3-b` — level 2, the preregistered NEGATIVE, proved as predicted; strength high.**
  `cx3b_complex_not_A1`: `A1` **fails** at the complex carrier. `Substratum.A1` is
  `Finite (ι → V × V)` and the constant families exhibit an injection from `ℂ`, so the
  configuration space is infinite. **This is a computed certificate in the kernel, not a failed
  proof search.**

**Bounded reading of `CX3`, as frozen, and it is this round's most load-bearing distinction.**
"Bringing the complex lift inside the interface" can mean two different things, and they come apart
here. **The covariance statement comes inside** (`CX1`, `CX2`). **The complex carrier does not come
inside as a substratum in the kernel's sense** (`CX3-b`), because the interface's first axiom is
finiteness and the complex carrier is infinite. That is **not a defect of the interface, not a
defect of the manuscripts, and not a defect of the complex lift**: the manuscripts' substratum is
the finite object of `SM.md:306` and the complex carrier is the object on which the derivation of
`SM.md:114` and Theorem 5 is conducted. The two facts are reported **together** here, and reporting
the first without the second would overstate the round. **`A1` is not weakened, no finiteness
parameter is added, and no second substratum structure is introduced.**

## `AS1` — the covariant form reaches the second-order dynamics

**Level 2, positive, as predicted; strength high.** `as1_leap_covariant`, stated once
polymorphically in the alphabet: for a link-coupled rule, any site-dependent `g`, and the
phase-space map `leapEquiv`, the second-order map of the **transported** rule is carried to the
second-order map of the **original** by the pointwise action on both slots. Instantiated at
`V = Fin 6 → ZMod q` (`as1_finite`) and at `V = Fin 6 → ℂ` (`as1_complex`). The proof shape is the
merged `leap_siteAct` with `a6cov_all` supplying the commutation instead of a hypothesis; the
falsifier — the leap's subtraction not commuting with `g i` — did not occur, `map_sub` supplying it
from additivity.

**Bounded reading, frozen.** This is what makes the covariance a statement about **the dynamics** of
`SM.md:306`–`:308` rather than about the first-order half of it. It is still the identity
`a6cov_all` records, and it is still a statement whose content is the interface, not a constraint.
Read `as1_complex` with `CX3-b`: the identity holds at the complex carrier, and that carrier is not
a substratum satisfying `A1`.

## `AS2` — the status determination

**`AS2` — evidence type P.** The two halves of the row's named hypothesis, in two sentences that
are **never merged**, at the strength reached.

**The packaging half.** It is discharged at evidence level 2: the manuscripts' six-fold
link-coupled rule **is** packaged as a `Substratum` of the kernel's own structure with no field
added — the cubic torus, the six-component alphabet over $\mathbb{Z}/q\mathbb{Z}$, the axis
neighbourhood, the link-valued coupling as a parameter and the second-order term carried by the
leap — the interface's link-coupled map **is** its update map (`PK2-a`), `A1`–`A5` hold of it
(`PK3`, `A4Exact` under the translation-invariance hypothesis on the link coupling), its
transformation class is larger than the singleton-index one (`PK4`), and the adopted reading holds
of its own link data (`PK2-b`) — **and because the adopted reading holds identically on every
link-coupled rule, what that last clause discharges is that the rule is of the covariant form, and
not that a condition was tested and survived.**

**The lift half.** It is discharged **for the covariance statement only**: the covariance statement
is statable and proved at a complex six-component carrier with no new definition (`CX1`), the
manuscripts' site-dependent transformation — `ℂ`-linear, and unitary in the matrix packaging — is
an instance of the interface's transformation class (`CX2`), and the covariant form reaches the
second-order dynamics there (`AS1`, `as1_complex`); while the complex carrier is **proved not to
be** a `Substratum` satisfying `A1` (`CX3-b`), so the **carrier** does not come inside the
interface, and the residual `CX0` classifies as (iii) — the inner product, unitarity as a
constraint, the condensate, the stabilizer in $\mathrm{U}(6)$ and the cubic decomposition — stays
outside and is named here as the residual.

**No target is UNDECIDED**, so no residual sentence of `AS2` carries an UNDECIDED target.

**The label.** The `ROADMAP` row `P1 — A6` carries `CONDITIONAL` at the start of this round and
carries `CONDITIONAL` at the end of it. **Whether these outcomes warrant a stronger label is an
owner decision, taken in a separate propagation round, and this round takes none and recommends
none.** What such a label would **not** be entitled to assert is recorded in the next section, in
the freeze's own words, and it is recorded here in advance of any decision rather than after it.

## What these outcomes do NOT license

- **They do not assert that a condition was tested and survived.** `A6Cov` holds identically on
  every link-coupled rule (`a6cov_all`); a positive says the manuscripts' rule is of the covariant
  form and says nothing more. A row labelled as derived would have to be read as "the manuscripts'
  carrier is an instance of the covariant interface", never as "the assumption was verified".
- **They do not assert anything about the physical substratum.** The packaged carrier is a formal
  object built from stated data; that the physical substratum is that object is a premise no round
  can discharge, and it is the residual that survives every outcome here. **Nothing here says the
  sixth assumption holds of the physical substratum, or fails of it.**
- **They do not assert a derivation of the gauge group.** Satisfying covariance on a packaged
  carrier is not a derivation of $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$, is not a
  step of Theorem 5 or Theorem 7, and licenses no sentence about the Standard Model. Theorems 5
  and 7 of `SM`, H-link, H-cust, the $(3,2,1)$ decomposition, the condensate stabilizer, the
  reduction to $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ and the Wilson action are
  **neither consumed nor judged, in either direction**. The conditional carrier reading of
  `SM.md:110` is preserved exactly as it stands.
- **Nothing here identifies any two of the four readings**, and nothing adopts, revises or ranks a
  reading. The adopted meaning is the propagation's and is consumed, not re-adjudicated.
- **Nothing here says that `A6-cov` is a constraint on the manuscripts' rule.** Its content is the
  covariant interface, and a positive is an instantiation result, not a verification result.
- **Nothing here is a complex-lift interface.** The alphabet is instantiated at a complex carrier;
  no unitary group as a structure on the interface, no inner product, no condensate, no state and
  no cubic action enters, and the part of the derivation that needs them stays outside and is named
  as the residual. **`CX3-b` licenses no weakening of `A1`** to make the complex carrier fit.
- **`PK5` is not "the substratum violates A6".** It is the separate stronger fixed-background
  condition failing, which is the recorded reason it is not the adopted meaning.
- **`PK4` is not more than the removal of the degeneracy verdict for this carrier.**
  `AddAut (Fin 6 → ZMod q)` is not $\mathrm{GL}(6,\mathbb{Z}/q\mathbb{Z})$ by fiat and
  `AddAut (Fin 6 → ℂ)` is not $\mathrm{U}(6)$; the one containment used is proved, in
  `cx2_unitary_gaugeLink`, and it runs one way only.
- **Nothing here decides whether A4 and the sixth assumption overlap** (`Substratum.md:104`),
  whether the assumption is independent of A1–A5, or what "the cubic-symmetric coupling matrix"
  denotes — `M` remains a parameter of every reading, so both the scalar $\mu I_6$ and the
  block-scalar equivariant object are instances and neither is chosen.
- **`A6-sd` is not formalized**, and nothing is said about H-Bell, preparation-indexed adjacency or
  the state-dependent Einstein construction.
- **Nothing here is about Track B, `P0`, physical C4, the fibre-Gram classification, Lemma 24.1,
  H-B or hydrodynamics**, in either direction.
- **The bare-carrier finding stands untouched.** The manuscript-axiom audit's verdict — that no
  manuscript-level conjunct of A1–A6 is a faithful predicate of the bare operational theory, which
  has no distinguished substratum — is about a different carrier and is neither consumed nor
  weakened.
- **No manuscript is edited.** `papers/` and `book/` were read and never written; the unsettled
  points below are listed for an owner call, not repaired.
- **`d`, `L`, `q` and the coupling are not settled.** The packaged carrier is a family in those
  parameters; `d = 3` is an empirical filter in the manuscripts that no target here asserts, and no
  instance of `M` is chosen.

## The points at which the manuscripts' intended reading was found unsettled, listed and not resolved

1. **`SM.md:487`'s "locally $\mathrm{U}(6)$ invariant".** The coordinate names a group and an
   invariance without displaying the identity it is an invariance of, so whether it intends the
   covariant statement of `:112`–`:114` or the separate fixed-background one is not fixed by the
   sentence. `CX0` classifies it **(iii)** at **medium** strength, by quotation, and leaves it.
2. **`book/ch05-gauge-structure.md:145`'s naming of the transformation group.** The passage takes
   $G(\mathbf{n}) \in \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$, a group defined by
   unitarity and a determinant condition, while the identity it displays consumes neither. Whether
   the passage intends that unitarity to be part of what the covariance requires, or only the
   ambient complex linear structure in which the matrix group lives, is not fixed by the sentence;
   `CX0` records **(ii)** as the freeze predicts, on the second reading, and does not resolve the
   first.
3. **The denotation of "the cubic-symmetric coupling matrix".** Whether it denotes the scalar
   $M = \mu I_6$ of `SM.md:422` or the block-scalar $O$-equivariant object of `SM.md:372` is not
   decided here: `M` is a parameter of every reading, so both are instances, and **no instance was
   chosen to resolve it**. Round 1 recorded this and it is still open.
4. **Whether `K = 6` should be tied to `d = 3` inside the packaging.** `Substratum.md:162` fixes
   $K = 6$ through the $(3,2,1)$ decomposition and `SM.md:372` through the link count at `d = 3`,
   while `SM.md:306` writes a general `K`. This round fixes the component count at six, because
   that is the object the owner's framing names, and leaves `d`, `L` and `q` as parameters. Not
   decided.
5. **Whether $\frac1d$ of `SM.md:308` is available in $\mathbb{Z}/q\mathbb{Z}$** at a given `d`,
   `q`. Not decided and not needed: the normalization is carried inside the coupling parameter and
   no instance of `M` is chosen.
6. **Whether the row's second half should be read as discharged when only the covariance statement
   is settled.** The freeze splits "inside the interface" into the covariance statement and the
   carrier and reports the two separately; which of them an owner wishes the row to track is
   **the owner's call and is not taken here**.

## Discrepancies

**None against the freeze's start-state table.** Every blob the freeze pins was found
byte-identical at the mandated base — the sixteen surfaces listed above — and every quoted passage
was located by content and found verbatim at the line the freeze records: `SM.md:100`, `:110`,
`:112`, `:114`, `:306`, `:308`, `:328`, `:334`, `:372`, `:422`, `:487`; `Substratum.md:102`,
`:104`, `:144`, `:162`, `:220`; `book/ch05-gauge-structure.md:141`, `:143`, `:145`;
`ROADMAP.md:22–31` and `:65`. The freeze cites the `ROADMAP` section as `:394–471`; at the base the
section heading is at `:394` and the next heading at `:473`, so the section body runs `:394–472`
with a trailing blank line, and every sentence the freeze quotes from it was found verbatim. That
is recorded for completeness and is not a divergence.

**One judgement the classification required, recorded and not repaired.** `CX0`'s class (ii) at
`book/ch05-gauge-structure.md:145` was reached by reading the named group as fixing the ambient
complex linear structure rather than as imposing unitarity on the covariance identity, because the
identity displayed there consumes neither the inner product nor unitarity. The freeze fixes (ii) for
that coordinate and this note reports (ii); the alternative reading is listed above as unsettled
point 2 and is **not** resolved here. **This is not a divergence from the freeze**, and no
falsifier fired.

**The reserved guard tag did not collide.** `R7-A6I` is absent from
`verification/lean/edge_rigidity_probe.py` at the base blob `c7e9827c`, so no mechanical adjustment
was needed and none was made.

## The `ROADMAP` propagation, and the re-pin that was NOT performed

The `ROADMAP` edit is confined to the `P1 — A6` section: one paragraph recording what this round
settled and what it did not, and two links to this round's directory. **The row's label cell reads
`**CONDITIONAL**` before and after, and the row's reasons are left byte-identical**, because they
are the reasons the label is `CONDITIONAL` and every one of them still holds: `A6Cov` is a predicate
of a neighbourhood function and a link coupling rather than of a `Substratum`; the covariance of
`SM.md:112–114` on the complex lift is not kernel-checked as the manuscripts conduct it, on the
carrier they conduct it on; and nothing is proved of the manuscripts' **physical** object.

**Status rule clause 2's permitted re-pin was therefore not performed, because its condition was
not met.** That clause re-pins guard `R7-A6D`'s row clause and its `DERIVED`-overclaim mutation
control **if the row's reasons change**. They do not change, so `R7-A6D`'s row clause stands
unmodified and its `DERIVED` mutation control is preserved as a mutation control, untouched. No
other merged guard's row clause is touched either. No other row, section or research status is
edited.

## The chronology control

**`R7-A6I` certifies the strong property**, reusing act 10's strengthened mechanism by name through
the merged `_rbr_strong_ancestry` and `_rbr_archive_ancestry`:

- this round's preregistration blob is pinned **by content** to
  `6f991c1348e0c568261894c41b129b7f942abee6`, with a drift control — one byte appended fails the
  pin;
- the real execution head `H` is resolved from `pull_request.head.sha` in a pull-request run —
  **never** the synthetic merge commit `refs/pull/<n>/merge` — failing closed with no fallback;
- `B = 3e5d6a8f75166581213b6c5b7c0dbca1671b030e`, the merge commit of the control-plane pull
  request, must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must itself be a descendant of `B`**, which excludes
  pre-freeze side history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it;
- **archive-mode scaffolding is present with its pins left unset**, so the guard runs in execution
  mode; once the sealed execution head and its merge commit are recorded in a follow-up after
  exact-head review and merge, the same strong check is re-run against the sealed head, the pinned
  merge's second parent is required to be that head, and both are required reachable from the
  current target, each fail-closed, through the existing mechanism and not a re-implementation.
  Nothing about the base or the blob pin changes in archive mode;
- `R7-A6I` also pins **by content** the three artifacts this round must not edit — round 1's
  `preregistration.md` (`afbf1ee0e8ea94cb7fb3e57e690cd08b8d7e0bc3`) and `result.md`
  (`331b1928adde22d5c716a92adb864b523d0c09b8`), and the covariance propagation's control plane
  (`e7cb7013747f783135c8e166d290ce6670df0ae9`) — so that status rule clause 9 is a checked fact and
  not a promise, each with a drift control.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The claim is scoped to the repository record. Commit SHAs locate; **blob SHAs are
what is pinned**.

**The single permitted exception to the "no execution object before the freeze" clause** — the
analysis recorded inside the control-plane blob itself: the frozen objects, the targets, the
predictions and the proof shapes named in them — was the only A6-instantiation-specific material in
the tree before this round, and every proof shape used here is one of those, unchanged.

## Definition budget: **TWO of the five frozen slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `linkRule` | **fired** |
| 2 | `linkSubstratum` | **fired** |
| 3 (conditional) | `TranslationInvariant` | **unused** |
| 4 (conditional) | a complex-carrier abbreviation for `Fin 6 → ℂ` | **unused** |
| 5 (conditional) | `IsLinkCoupled` | **unused** |

Slot 3 did not fire: `PK3-d` and `CX3-a` are stated readably with the hypothesis written inline as
`∀ v i j, M (i + v) (j + v) = M i j`, which discharges hazard 11 by the statement itself rather than
by a name — the hypothesis is visible in every statement that carries it and in every place this
note reports it. Slot 4 did not fire: `CX1`–`CX3` read `Fin 6 → ℂ` written out. Slot 5 did not fire:
`PK2-a` is stated as the equation it is, on the packaged carrier
(`R.F = linkF R.N M`), and `AS2` is prose, so no packaging predicate was needed; accordingly **no
covariance predicate is defined on `Substratum` and nothing is named a reading, a strengthening or
a variant of the sixth assumption**.

**No sixth definition was introduced.** No field is added to `Substratum`; no predicate for
`A6-sd`; no unitary group, inner product, condensate, state or cubic group action; no connectivity
predicate; no phase-space form of any reading as a separate definition — `AS1` is a theorem about
`siteAct`, `gaugeLink` and `leapEquiv`. **No witness, carrier, transformation, configuration or
coupling is a top-level definition**: each is a bound variable pinned by an equation in the
statement that needs it, including the cyclic shift of `PK4`, the constant coupling of `PK5`, the
`ℂ`-linear family and the unitary family of `CX2`, and the injection of `CX3-b`. `Substratum`,
`Rule`, `leapEquiv`, `siteAct`, `PreservesPointwise`, `A6Inv`, `A6Glob`, `linkF`, `gaugeLink`,
`A6Cov`, `dir`, `nbrs`, `mem_nbrs_symm`, `waveF`, `waveRule` and `waveSubstratum` are consumed
unmodified.

**One notational point, recorded.** The freeze writes `PK1`'s carrier with `ι`, `V`, `N`, `infl`
and `F` fixed by equations; because `Rule.mem_infl` is `∀ i j, j ∈ N i → i ∈ infl j` and `infl` is
taken to be `N`, `linkRule` carries the neighbourhood symmetry as an explicit hypothesis rather than
proving it for an arbitrary neighbourhood function, and the manuscripts' data supply it through the
merged `mem_nbrs_symm`. The hypothesis is part of both definitions and is discharged at every use.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Twenty-five named results, **no `sorry`, no `axiom`, no
`native_decide`**, each with its own `#print axioms` line and none printing anything outside
`[propext, Classical.choice, Quot.sound]`; one prints a strict subset of the three, which is
recorded as printed. **`CX2`'s frozen fallback did not fire, so nothing in this round is reported
at level 3.** **No type-P item is in this table**: `PK0`, `CX0` and `AS2` are prose determinations
and are listed nowhere below.

| Result | Axioms |
| --- | --- |
| `linkSubstratum_bridge` | `[propext, Classical.choice, Quot.sound]` |
| `linkSubstratum_A2` | `[propext, Classical.choice, Quot.sound]` |
| `linkSubstratum_A5` | `[propext, Classical.choice, Quot.sound]` |
| `linkSubstratum_A3` | `[propext, Classical.choice, Quot.sound]` |
| `nbrs_sub` | `[propext, Classical.choice, Quot.sound]` |
| `linkSubstratum_A4Exact` | `[propext, Classical.choice, Quot.sound]` |
| `pk1_packaging` | `[propext, Classical.choice, Quot.sound]` |
| `pk2a_bridge` | `[propext, Classical.choice, Quot.sound]` |
| `pk2b_covariance` | `[propext, Classical.choice, Quot.sound]` |
| `pk3a_A1` | `[propext, Classical.choice, Quot.sound]` |
| `pk3b_A2` | `[propext, Classical.choice, Quot.sound]` |
| `pk3c_A3` | `[propext, Classical.choice, Quot.sound]` |
| `pk3d_A4Exact` | `[propext, Classical.choice, Quot.sound]` |
| `pk3e_A5` | `[propext, Classical.choice, Quot.sound]` |
| `pk4_shift_not_scalar` | `[propext, Quot.sound]` |
| `pk5_symmetric_point` | `[propext, Classical.choice, Quot.sound]` |
| `cx1_complex_covariance` | `[propext, Classical.choice, Quot.sound]` |
| `cx2_clinear_forgets` | `[propext, Classical.choice, Quot.sound]` |
| `cx2_manuscript_law` | `[propext, Classical.choice, Quot.sound]` |
| `cx2_unitary_gaugeLink` | `[propext, Classical.choice, Quot.sound]` |
| `cx3a_complex_axioms` | `[propext, Classical.choice, Quot.sound]` |
| `cx3b_complex_not_A1` | `[propext, Classical.choice, Quot.sound]` |
| `as1_leap_covariant` | `[propext, Classical.choice, Quot.sound]` |
| `as1_finite` | `[propext, Classical.choice, Quot.sound]` |
| `as1_complex` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It moves no label and recommends none.** The row `P1 — A6` carries `CONDITIONAL` before and
  after. **The stronger-label decision these outcomes set up is named as open, the owner's, and not
  this round's.**
- **It adopts, revises or ranks no reading**, and it identifies no two of the four.
- **It proves or refutes the sixth assumption for nothing physical.** No sentence here begins "the
  substratum satisfies A6" or "the substratum violates A6", and neither is a possible outcome of
  this round.
- **It reports the gauge-group derivation neither settled nor unsettled**, in either direction, and
  no outcome here is connected to the Standard Model.
- **It enlarges the interface only by the alphabet instantiation the freeze records as a decision.**
  No field is added to `Substratum`; no unitary group, inner product, condensate, state, cubic
  group action, connectivity notion or state-dependent rule family is defined; no predicate is
  defined for `A6-sd`; `A1` is not weakened and no second substratum structure is introduced.
- **It edits no manuscript, no round-1 artifact, no propagation control plane and no historical
  round record.** Round 1's two artifacts and the propagation's control plane are pinned by blob in
  `R7-A6I`, so that this is a checked fact rather than a promise.
- **It revises nothing merged.** `Substratum`, `A1`–`A5`, `A4Exact`, `A3Family`, the four
  `Substratum` theorems, `waveF`, `waveRule`, `waveSubstratum`, `nbrs`, `dir`, `mem_nbrs_symm`, the
  five `waveSubstratum_A*` theorems, `Rule`, `leapEquiv` and all sixteen named results of the
  round-1 module are cited and consumed unmodified; the interface audit's Q1 verdict table and the
  manuscript-axiom audit's verdict for the bare operational carrier stand as they are.
