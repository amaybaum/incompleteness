# Track B act 25 — the orbit-geometry isometries: the normalized realizable quotient, the finite family that acts on it, the internal description of its classes at the single carrier, a gated classification of its surjective isometries, and the prefix-constrained corollary: CONTROL PLANE

Owner-called. This file is the whole of act 25's control plane and is merged **alone**, before any
execution object exists. It is a **gated round**: four targets frozen together, each with its own
preregistered proposition, its own verdict rule and its own failure interpretation, executed in a
fixed order in which **each later target is executed only if the earlier ones reach the label the
gate names** — the normalized space and the finite family that acts on it first, the internal
description of the realizable classes at the single-carrier configuration second, the
classification of the surjective isometries of that space third and only then, and the
prefix-constrained corollary for transition families last and only then. It re-opens nothing of
acts 21 through 24, changes no rung, adds no rung to act 21's ladder, widens no equivalence,
adjusts neither act 24's invariant family nor its geometry, and adopts nothing: the family it
freezes is a **named object of test**, written from the Gram data and the dilation alone, and every
verdict is about that named object at the configurations frozen for it.

It is **not** a re-run of act 24, **not** a classification of the isometries of the whole tuple
space or of the whole feature image, **not** a statement about continuity, composition in time or
a generator, **not** a statement about the threading, and **not** an attempt to derive or to
recognise quantum evolution, which stays an explicit non-doing. In particular **no isometry named
here is read as a symmetry of anything**: the entrywise conjugation is the entrywise `star` and the
dilation transpose is the matrix transpose, and neither is identified with a symmetry operation of
quantum mechanics, an antiunitary map, a time reversal, or any quantum-dynamical object.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The commit vocabulary this freeze uses, fixed first

`AGENTS.md` `§A.37`, at the drafting snapshot, **lines 713–729**, gives a control plane three commit
names, and this file uses them in exactly that sense:

- **`D`, the drafting snapshot** — `17272da24e8d65a8d0e2417c6a451a1af3461258`, certified `main` at
  the landing of act 24 (#690), whose main-push run 35467053564 is fully green with `R7-OGS` in
  `ARCHIVED` state and the control-plane base check in mode `B`. Every measurement below — every
  locating coordinate, every pinned blob, every name-freedom check and the chronology simulation —
  was made at `D`, and is a statement about `D`. **`D` is never the execution base.**
- **`B`, the mandated execution base** — the certified merge commit on `main` of **this** file, or
  of the latest execution-affecting append-only amendment to it should one be needed. **Before that
  merge exists `B` has no SHA, and this file assigns it none.** The prospective declaration, the
  declared baseline, the chronology control and the precondition rows scoped at `B` all read `B` in
  this sense.
- **`M`, a candidate control-plane merge** — predictive test state only: the synthetic merge
  continuous integration builds for this pull request, against which the `B`-scoped and `D → B`
  rows of the block below are evaluated in mode `M` before the merge. `M` is never execution
  ancestry, never seal state and never historical evidence; the same rows are re-evaluated in mode
  `B` against the actual merge commit by the main-push certification, and **no execution branch is
  created before that certification is green**.

## The key hazard, stated before anything else

**The classification target of this round can be earned only by a description of the realizable
classes that is derived inside the kernel from act 12's merged sufficiency theorem.** At the
single-carrier configuration that description is a classification of the `4 × 4` matrices of
unit-modulus entries that are unitary up to the factor `½` — the complex-Hadamard matrices of
order four — modulo phases on rows and on columns. That classification exists in the literature and
is cited below as provenance. **It is not consumed.** If proving the description requires a
theorem that the execution cannot derive internally, the second target ends `UNDECIDED` with the
case named, the third target — the classification of the isometries — **returns `UNDECIDED`** with
the obstruction "the realizable image at the configuration was not classified internally", and
**no external classification is silently imported and no weaker domain is substituted**: neither a
subfamily of the realizable classes, nor the Fourier circle alone, nor a finite sample of classes,
nor the whole tuple space, nor the whole feature image is put in the place of the realizable
quotient, and a verdict about any such substitute is a discrepancy of the round and earns no
label. The same holds at the product configuration, where the freeze knows no route at all and
records `UNDECIDED` in advance.

## The round's shape, declared first, in `§A.37`'s terms — under the manifest protocol

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 858–863** at `D`:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes
>    ownership of changing existing seal state — takes a pin commit `P`, and `P`
>    is mandatory.** `P` writes the round's own **manifest record** —
>    `sealed_head` = `E` and `merge` = `L`, under `verification/seals/` — and not
>    a legacy constant; see *Sealing through the manifest* at the end of this

This freeze **creates new seal state**, in the representation `SI-3` left in force — **data under
`verification/seals/`, no constant in the guard file** — and carries it in two places at two times:

| object | where it lives | state during execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'OGC': B}` | **declared**; the validator classifies `OGC` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OGC',)}`, in the same file | the seals tree at `B`, read from git, plus the one addition this freeze authorizes, by stem | unchanged; `OGC.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/OGC.json` | **absent** | **written by `P`**: `{"round": "OGC", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `OGC` as `ARCHIVED` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
writes `OGC.json` and removes the `OGC` entry from the prospective declaration, and touches nothing
else. Without `P` the round sits at `LANDED-PENDING-PIN`, permitted at `L` itself, and every head
descending from that unpinned landing fails as *seal pending*.

**No legacy seal constant is written, at any commit of the round.** Nothing matching
`_OGC_(BASE|SEALED_HEAD|MERGE)` exists at any commit, `SI-3`'s standing contract holds at every
head, and the execution's guard clause certifies chronology through one keyed call,
`_si2_authority('OGC', tag='R7-OGC')`, and never through a per-round constant.

### The lifecycle derivation, and why it comes out SEALING

The rule the owner set for act 19 and act 21 is carried: a round is sealing **if and only if** its
execution creates a new formal object whose chronology matters to the result.

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the family's action on the normalized space, the description of the realizable
   classes, the classification of the isometries or its recorded non-attainment, and the
   corollary.
2. **Their chronology is load-bearing.** The round's claim is that its family, its normalized
   space, its route, its gate and its execution order were frozen — here, in this file — before
   any kernel work, and that no generator was added to the family and no domain substituted for
   the realizable quotient to reach any verdict; a validator-certified ancestry rooted at this
   control plane's merge commit is what makes that checkable.
3. **A new module with new named results is new seal state**, which only a sealing round's `P` may
   record.

**Therefore act 25 is SEALING, and it owns no other seal state.**

### The tag, the stem, the module and the round directory are free at `D`

At `D`:

- `git grep -l -- 'R7-OGC'` returns nothing anywhere in the tree, and the tag is absent from the
  **eighty-eight** `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries at `D`.
- `git grep -l -- 'OGC'` returns nothing anywhere in the tree — the bare three-letter form occurs in
  no text file and in no binary artifact, as a word or as a substring — so a bare-stem search for it
  is unambiguous, and `git grep -l -- '_OGC'` returns nothing.
- No record `verification/seals/OGC.json` exists; the twenty-nine records at `D` use the stems
  `A12P`, `A6D`, `A6I`, `A6P`, `ABR`, `CLG`, `CTI`, `HYA`, `HYB`, `HYE`, `OGS`, `OLG`, `OLN`,
  `OLT`, `PC4`, `PC4S`, `PQT`, `RBR`, `RNC`, `RNT`, `SGT`, `SI1`, `SI2`, `SI3`, `TCF`, `TRJ`,
  `TSG`, `WTS` and `XTS`, and no substring search for `OGC` reaches any of them.
- **The stem was chosen for its reading and checked before anything was written**: `OGC` —
  orbit-geometry classification, the object this round tests — matches nothing at `D`. `OGS` is
  act 24's, excluded on that ground alone.
- **The target names are free.** `git grep -l -- 'ISO0'` through `git grep -l -- 'ISO4'` each
  return nothing, and so do the theorem-name prefixes `iso1_`, `iso2_`, `iso3_` and `iso4_`.

**The round directory and the module name are free at `D` too.** `git grep -l -- 'act-25'`,
`git grep -l -- 'orbit-geometry-isometries'` and `git grep -l -- 'OrbitGeometryIsometries'` return
nothing. The round directory is
`verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/` and the module is
`verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean`.

### What this round does NOT own, named exhaustively

It alters **no existing manifest record**. The twenty-nine records under `verification/seals/` at
`D` — the seals tree `ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f`, twenty-three `sealed` and six
`base-only` — are **read and never written**; the one addition this freeze authorizes is `OGC`. It
writes **no legacy constant**. It does not re-pin, re-derive or re-declare any other round's seal:
`OGS.json`, `OLG.json`, `OLN.json`, `OLT.json` and the rest belong to the rounds that set them.
Inside the guard file the execution **adds** the `R7-OGC` clause and **sets** the two stem-free
declarations named above — and changes nothing else in the file. **No contract of any closed round
is superseded**, and the measurement that none needs to be is recorded in the chronology section.

## Provenance — what this freeze carries from acts 12 through 24, from the literature, and what is its own

**The rule.** Act 25 consumes act 12's slice equivalence, realizable set and sufficiency theorem,
act 21's ladder and configurations, act 23's Fourier family and its admissibility, and act 24's
invariant family, geometry, separation theorem, relabelling isometry and conjugation facts,
exactly as landed, **unchanged**, and adds one finite family of maps with its normal form, one
normalized space bound by equation, four targets, a gate and its own lifecycle. Every rung is the
declaration act 21's merged module carries, pinned by blob at `B`; **no rung is restated in this
round's module**, no definition is introduced, and the invariant family and the geometry are act
24's `mixedTriple` and act 24's frozen equation, consumed and never redefined.

| source (frozen blob, line range) | this file | status |
| --- | --- | --- |
| act 12's `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `TwoSidedGauge.lean` `4bba2040…` lines 95–110 | the quotient; the realizable set every statement quantifies over | **consumed unrestated** |
| act 12's `fibreGram_apply`, line 115, `sh1_necessity`, line 168, `sh1_sufficiency`, line 1070, `gramPhaseEquiv_cross_invariant`, line 870 | the dilation behind every realizable tuple, in both directions; the invariant every separation is read through | **consumed** |
| act 7's `AdmissibleDilationAt`, `DilationChoice.lean` `7e3a8222…` lines 134–136 | the hypothesis under which the dilation transpose is taken | **consumed unrestated** |
| act 17's `GramTrajEquiv` and the three equivalence lemmas, `GramTrajectorySelection.lean` `afc22cfc…` lines 121 and 141–170 | the equivalence-relation facts every statement on classes uses | **consumed** |
| act 18's `ProperAt`, `PropagatesFrom` (`IntermediateCrossTimeStructure.lean` `cb14c43b…` lines 167–171, 186–193) | the standing hypotheses of the corollary's prefix | **consumed** |
| act 20's `RelabelTransition`, `RepresentativeNaturality.lean` `4c1137f3…` line 167 | the diagonal case `(σ, σ)` of the independent relabellings; named, never restated | **consumed unrestated** |
| act 21's ladder `L0`–`L5`, `OrbitLawRigidityTwisted.lean` `860daac4…` lines 96–196, and `ol1a_descent`, line 279 | consumed as `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `LadderConds` and the inline `L2`, `L4d`; the corollary's prefix | **consumed unrestated** |
| act 21's two configurations, its freeze `316d635a…` lines 1263–1267 and its single-carrier configuration | the same two configurations, and no other | **carried unchanged** |
| act 23's Fourier family `H(z)` and `hadamard_z_admissible`, `OrbitLawGaps.lean` `5ed0dad7…` line 116, `fibreGram_z_entries`, line 150 | the normal form the class description reaches; its admissibility | **consumed as landed** |
| act 24's `mixedTriple`, `OrbitGeometrySelector.lean` `ce9d1aa0…` lines 79–80, and the frozen geometry equation | the invariant family and the geometry, consumed; never redefined | **consumed unrestated** |
| act 24's `geo1_triple_metric`, lines 526–566, in particular (iii), (vi-a) and (vi-b); `geo1_separation_single`, line 412; `geo1_equiv_of_zero_single`, line 497; `geo1_zero_of_equiv`, line 480; `realizable_entry_ne_zero`, line 385 | separation, which is what makes the feature image the class space; the full-support fact | **consumed** |
| act 24's `mixedTriple_relabel`, line 598, `geo2_relabel_isometry`, line 607, `mixedTriple_star`, line 114, `realizable_conj`, line 1523, `conj_gramPhaseEquiv`, line 1541, `conj_conj`, line 1534, `geo3_phiConj_isometry`, line 931, `geo4_a0_isometry_injective`, line 1616 | the diagonal relabelling and the conjugation, two of the family's generators, with the facts about them already merged | **consumed** |
| act 24's `geo4_b0_not_relabel_rigid`, line 1714, and its result `a2719d5f…` lines 699–708, the `b` cell's obstruction, and lines 997–1009, the observation for the classification round | the reason this round exists, quoted below | **consumed as landed** |
| the attestation set, act 21's freeze lines 1033–1043 | carried verbatim, asked at **every** boundary of this round | **carried, re-scoped** |
| THE CLAUSE, act 21's freeze lines 1897–1905 | carried verbatim with "Act 21" → "Act 25" in its first sentence | **carried, one substitution** |
| act 13's `P0` threading sentence, its result `2c38dbf1…` lines 267–273 | named as what this round does not touch | **untouched** |
| everything else — the shared theorem, the censuses, `SIOP`, the headlines, the `P0` sentences of acts 21 through 24, act 24's twelve verdicts, its cells and its `GEO1-T` | not this round's | **untouched** |

### External provenance — cited for the route, not for any theorem

Three strands of published mathematics are the provenance of this round's route, and are cited
here **as provenance only**. No theorem of this round is attributed to them, none of their
theorems is consumed, and every statement below is proved in the kernel for this round's own
object.

1. **The classification of complex Hadamard matrices of order four.** U. Haagerup, *Orthogonal
   maximal abelian ∗-subalgebras of the `n × n` matrices and cyclic `n`-roots* (1996); W. Tadej
   and K. Życzkowski, *A concise guide to complex Hadamard matrices* (2006): every complex Hadamard
   matrix of order four is equivalent, under permutations and phases of rows and columns, to a
   member of the one-parameter family `F₄⁽¹⁾(a)`, which is act 23's `H(z)` at `z = i·e^{ia}`.
   **This round's second target is that statement for this round's object — the realizable
   tuples at `Γ₀ ≡ ¼`, `|A| = 1`, modulo act 12's equivalence — derived from act 12's merged
   sufficiency theorem and the unit-modulus identity `(a + b)(b + c)(c + a) = (a + b + c)(ab + bc +
   ca) − abc`; it is proved here or it is `UNDECIDED`, and it is never imported.** Nothing of that
   literature is consumed, and no equivalence-testing machinery of it is used. **The
   classification of complex Hadamard matrices of order sixteen is not known to be complete in that
   literature**, and that is the recorded reason the product configuration is expected to end
   `UNDECIDED`.
2. **Isometries of subsets of Euclidean space.** The classical fact that a distance-preserving map
   between subsets of a Euclidean space extends to an affine isometry of their affine hulls is the
   provenance of the **optional lemma** `ISO3-L` below, and of nothing else: the lemma is proved in
   the kernel for this round's object if it is reached, enters no label, and **linearity is never
   assumed** of any isometry in any statement of this round.
3. **The Wigner-type shape** of the question — a geometry-preserving map on a state space forced
   to be of a named form — is named here as provenance for the *shape of the question* and for
   nothing else: the round has no bridge from its orbit space to any Hilbert space, ray space or
   transition probability, and asserts none. The word "Wigner" appears in this file only here, in
   the forbidden list and in `ISO0`'s term list, and in no other artifact of the round.

## Locating controls — the governing passages at `D`, each with a coordinate

Every quotation below is verbatim from a blob pinned in the start-state table, with its file and
line coordinate at `D`.

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 703–706**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

**The mandated base, stated as this round's own commitment.** The execution branches from the merge
commit of **this** control-plane pull request and from **nothing else**, after that commit's
main-push certification — the four jobs, the control-plane base check in mode `B` included — is
fully green, and not before. **Its first act is to verify that the preregistration at that base
carries the blob this freeze names**, before any target is executed, and to record the verification
in the result note. If the blob differs, the execution records the discrepancy and does not repair
the freeze.

### The three commit names, and the machine-checkable form

`AGENTS.md`, **lines 731–732** and **763–765**:

> Every mechanical precondition names its evaluation scope explicitly as at "D",
> at "B", or from "D" to "B".

> **Machine-checkable form.** A control plane that wants its preconditions run
> mechanically carries one fenced block whose info string is
> `control-plane-preconditions`.

This file carries that block, at the end of the preconditions section, and the release gate's
`control-plane-lint` and the workflow's `control-plane-base-check` job read it. The base check at
`D` evaluates only the control-plane artifacts added or changed relative to the evaluated commit's
first parent, `tools/control_plane_base_check.py` at blob `d6d65782…`; this file is such an artifact
at `M` and at `B`, and is historical at every later commit.

### The manifest protocol, in the passages this round executes under

`AGENTS.md`, **lines 962–972** (the seal record is data), **1024–1035** (the legacy representation
is retired), **1037–1046** (how a sealing round carries its base), **1047–1053** (how manifest
integrity is declared) and **1055–1061** (a closed round's contracts are read over the records it
manifested) are the passages acts 21 through 24 quoted at their own bases, unchanged in wording at
`D` — `AGENTS.md` carries the same blob `a9687b39…` at `D` as at act 24's drafting snapshot.

### The obligation, and what act 24 left in front of it

`verification/ROADMAP.md`, **line 63**, the `P0` row, carries act 21's, act 22's, act 23's and act
24's frozen Case A sentences at its end; the row's label is **OPEN** and two-part, and this round
appends its own frozen sentence after act 24's and changes the label of nothing.

`verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md`, blob
`a2719d5f…`, **lines 699–708**, the obstruction on which act 24's rigidity attempt stopped:

> - **`b`, the prefix with `L5` and isometry forces a relabelling or a relabelling composed with the
>   conjugation.** The step that did not close is the passage from an isometry of the geometry on the
>   realizable tuples to a single permutation `σ` of the carrier `Fin 4 × Fin 4`: the hypotheses
>   constrain `Φ t` through act 12's classes and the feature distances, and no argument in the record
>   produces a permutation of the carrier from an isometry of the feature geometry restricted to the
>   realizable set, the isometries of that geometry not being characterized here and their
>   characterization being out of this round's scope by its own freeze. What would settle it is a
>   classification of the isometries of the feature geometry on the realizable classes at the product
>   configuration, which is a question for a later round with its own freeze. Neither the rigidity
>   label nor its negation is claimed; the absence of a proof is not a counterexample.

and **lines 999–1005**, the observation act 24 left for this round:

> a classification of the isometries of this geometry at the product configuration must **exclude**
> `ΦCTRL`, `Φ_SC`, `Φ_MD`, `Φ_PC` and `Φ_HS`, each proved not an isometry, modulo the frozen law
> equivalence, and must **account for** `ΦPP`, `Φ_swap` and `Φ_conj`, each proved an isometry; at the
> single-carrier configuration it must exclude `ΦC` and account for `ΦI`, `ΦP` and `ΦT`. **These results
> place no inclusion requirement on the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`
> beyond that accounting, and no requirement that any parameter set contain any group or any family.**

**This round is the round act 24 named there**, at the single-carrier configuration first and with
the product configuration recorded, and the accounting act 24 asks for is a control of the third
target below: the family this freeze names contains `ΦI`, `ΦP` and `ΦT`'s maps at the single
carrier and `ΦPP`, `Φ_swap` and `Φ_conj`'s at the product carrier, each as a named element, and
contains none of the non-isometries, which are not isometries and so are excluded by the
hypothesis itself.

`verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md`, **line 10**,
the state of the record after act 24:

> **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-DISCRIMINATES` · `GEO4-UNDECIDED`

`verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md`, blob `2c38dbf1…`,
**lines 267–273**, the threading part of `P0`, which this round does not touch:

> `P0` remains open and two-part, and the threading part is localized exactly: the fibre cross-Gram
> trajectory determines the lift up to one constant in-fibre left move and one time-dependent strong
> right gauge […] nothing in act 13 selects either, and no connection, gauge fixing or
> selection principle is asserted or excluded.

### The act 12 declarations this round is stated over

`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob
`4bba2040c33424fafbc6d31c0d63b86dff33691a`: `FibreGram` at **lines 95–97**, `GramPhaseEquiv` at
**102–103**, `RealizableGram` at **108–110**, `fibreGram_apply` at **115–116**, `sh1_necessity` at
**168–171**, `gramPhaseEquiv_cross_invariant` at **870–871**, `sh1_sufficiency` at **1070**.

The exact shapes, verbatim, of the three declarations every statement of this round is written over:

```
def FibreGram (a₀ : A) (U : Matrix (V × A) (V × A) ℂ) (i : V) : Matrix V V ℂ :=
  (U.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
    * U.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀))
```

```
def GramPhaseEquiv (G G' : V → Matrix V V ℂ) : Prop :=
  ∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ ∀ i j k, G' i j k = star (c j) * G i j k * c k
```

```
def RealizableGram (A : Type) [Fintype A] (Γ : Matrix V V ℝ) (G : V → Matrix V V ℂ) : Prop :=
  (∀ i, (G i).PosSemidef) ∧ (∀ i, (G i).rank ≤ Fintype.card A)
    ∧ (∑ i, G i = 1) ∧ ∀ i j, G i j j = (Γ i j : ℂ)
```

**Four features are load-bearing and are named now.** By `fibreGram_apply`,
`FibreGram a₀ U i j k = ∑ a, star (U (i, a) (j, a₀)) * U (i, a) (k, a₀)`, so at `|A| = 1` a
realizable tuple is `G i j k = star (U (i, 0) (j, 0)) * U (i, 0) (k, 0)` for a unitary `U` with
`‖U (i, 0) (j, 0)‖ ^ 2 = Γ i j`; **a phase on the row `i` of `U` leaves `G` unchanged, and a phase
on the column `j` of `U` is act 12's action** `G' i j k = star (c j) * G i j k * c k`; the rows of
`U` are determined by `G` up to exactly those row phases, because each row's rank-one Gram fixes it
up to a phase when no entry vanishes; and at the frozen configurations no entry vanishes, since
`Γ ≡ ¼` and `Γ ≡ 1/16`. **So at `|A| = 1` the realizable classes are the double cosets of the
unitaries with the prescribed moduli under diagonal unitaries acting on both sides**, and the
transpose of `U`, which exchanges the two sides, descends to the classes. That is the fact the
fourth generator rests on, and it is proved from act 12's merged results, not assumed.

### The act 24 declarations consumed, and the geometry

`verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean`, blob
`ce9d1aa05dfdedfb5cac171cfe6379681942195f`: `mixedTriple` at **lines 79–80**, `mixedTriple_gauge` at
**88**, `mixedTriple_star` at **114**, `coord_le_dist` at **123**, `geo1_separation_star` at
**337**, `realizable_entry_ne_zero` at **385**, `geo1_separation_single` at **412**,
`geo1_separation_product` at **425**, `dist_eq_norm_toLp` at **439**, `geo1_metric_props` at
**451**, `geo1_class_invariant` at **471**, `geo1_zero_of_equiv` at **480**,
`features_eq_of_dist_zero` at **489**, `geo1_equiv_of_zero_single` at **497**,
`geo1_equiv_of_zero_product` at **507**, `geo1_triple_metric` at **526–566**,
`mixedTriple_relabel` at **598**, `geo2_relabel_isometry` at **607**, `mixedTriple_product` at
**642**, `geo2_product_tensor` at **652**, `geo3_phiConj_isometry` at **931**, `conj_eq_transpose`
at **1512**, `realizable_conj` at **1523**, `conj_conj` at **1534**, `conj_gramPhaseEquiv` at
**1541**, `conj_cross` at **1552**, `geo4_a0_isometry_injective` at **1616**,
`geo4_b0_not_relabel_rigid` at **1714**.

The one definition act 24 budgeted, verbatim, consumed here and never redefined:

```
def mixedTriple (G : V → Matrix V V ℂ) : (V × V × V) × (V × V × V) → ℂ :=
  fun p => G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1
```

and the geometry, bound by the same equation in every theorem of this round that names it:

```
d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)
```

### The act 21, act 23, act 20, act 18, act 17 and act 7 declarations consumed

`verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`, blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`: `EvolvesTotally` at **lines 96–100**,
`PreservesAdmissible` at **108–110**, `Reversible` at **123–128** (its second conjunct, `L3s`, is
what supplies surjectivity on classes to the corollary), `FactorizesOnProduct` at **143–157**,
`LadderConds` at **179–196**, `ol1a_descent` at **279–290**, `realizable_relabel` at **388**,
`relabel_gramPhaseEquiv` at **397**, `relabel_one` at **986**, `product_realizable` at **1015**,
`hadamard_entries` at **1062–1080**.
`verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`, blob
`5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`: `hadamard_z_admissible` at **116**,
`fibreGram_z_entries` at **150**, `zseq_facts` at **168**.
`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, blob
`4c1137f35600320b9273c857ec62271341b05cd0`: `RelabelTransition` at **167–168**.
`verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean`, blob
`cb14c43b0becfe1a379ae3615d5553723ede9163`: `ProperAt` at **167–171**, `PropagatesFrom` at
**186–193**.
`verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean`, blob
`afc22cfc93b244c80e1c55a273dcfda1ddebb121`: `GramTrajEquiv` at **121–122**, `gramPhaseEquiv_refl`,
`gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` at **141–170**.
`verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob
`7e3a8222cedf530f3c109662e7174d72b6358063`: `AdmissibleDilationAt` at **134–136**:

```
def AdmissibleDilationAt (G : Matrix V V ℝ) (a₀ : A)
    (U : Matrix (V × A) (V × A) ℂ) : Prop :=
  U ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ i j, G i j = ∑ a : A, ‖U (i, a) (j, a₀)‖ ^ 2
```

Consumed for what they state; none is re-proved.

## Start state, pinned by blob

Pinned **by blob** at `D`. Blob identity is authoritative: the commit locates the tree, the blob is
what is compared, and the `D → B` rows of the block below require each of these unchanged at `B`.

| path | blob at `D` |
| --- | --- |
| `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean` | `ce9d1aa05dfdedfb5cac171cfe6379681942195f` |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | `d41b157a3f38d4ebedbe11ad9682a8693836a383` |
| `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md` | `3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a` |
| `verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md` | `a2719d5f63c4ce517590ec7fbe8e61bafe04c3a7` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md` | `316d635a31f91faebeeebef7688b30002d24b4ca` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md` | `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md` | `bb02ef41eb221696ffa45c9281b69553c8279cbb` |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md` | `b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e` |
| `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md` | `93c06674792fa3565f6f94e5e954e484dca33cf2` |
| `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md` | `174e790d2cc5c663f9f54ae7daaeca90b51f96e1` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | `6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db` |
| `verification/seals/OGS.json` | `5436e01852e9999483dd4aff9f605e47575b7415` |
| `verification/seals/OLT.json` | `8ed0ef5391410db3a112cbe845d27536b7c1ab9b` |
| `verification/seals/OLN.json` | `1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb` |
| `verification/seals/OLG.json` | `8a058df23c07e2b7571672c039a5a7b4f911a339` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `tools/control_plane_base_check.py` | `d6d6578201a9cab3fcb91d63f4818b38104fc4e4` |
| `tools/control_plane_lint.py` | `7678dbe25f51e6e6b14f07e8842f1b6d205f4fed` |

Every one of these is read and never written by this round. If any blob differs at `B`, the
execution records the discrepancy and does not repair the freeze — and for the first twenty-six,
the base check has already refused the merge.

### The files this round writes

**The files this round writes are named separately and are not in the table above.** Each is
pinned by blob at `D` all the same, so that a discrepancy in what the round writes onto is as
visible as a discrepancy in what it reads; a difference at `B` in any of them is recorded in the
result note as a discrepancy and the freeze is not repaired.

| path | blob at `D` | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `fb5a9df14952d24217d677677c6562c4eac562ed` | **read** as the pinned statement of the `P0` row, and **written** only by appending the frozen post-round sentence for the vector reached after act 24's sentence in the same cell; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `bdd76b23985638d6f6715561c8975480b2e53584` | the `R7-OGC` clause **added** directly before `# ---- R7-SI1`, after the `R7-OGS` clause; `_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` **set** as the shape section states, the former emptied by `P`; **nothing else**; no contract of any closed round touched; no legacy constant written |
| `verification/lean-mathlib/OIBridge.lean` | `165f4bf3caf7cb6c5120476969415b5545150bd1` | one import line added directly after `import OIBridge.OrbitGeometrySelector`, at line 213 at `D` |
| `verification/lean-manuscript-census.json` | `02225c2573515aae60a5f73ba0510f8f438a0b53` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/result.md` | — | created by the execution |
| `verification/seals/OGC.json` | — | created by **`P`**, and by nothing before `P` |

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

The base is fixed the moment this file merges, and whatever sibling lanes have landed in `main` by
then is a fact about the base's tree and not a fact about this round's inputs. The start-state
table above is the complete list of what this round consumes, and a file present at `B` and absent
from that table is read by nothing in this round. The seals tree at `B` is whatever `B` carries;
the execution records the tree it found, and the declared baseline reads it from git.

## Source scoping, carried from acts 13 through 24

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what act 24 left in front of it

Act 24 established, at evidence level 2, that the mixed-triple feature map separates act 12's
classes on the realizable tuples at both frozen configurations and that the Euclidean distance of
feature vectors is a metric on those classes; that every carrier relabelling and the entrywise
conjugation are isometries of it; and that its rigidity attempt — the conditions before naturality
with factorization and isometry forcing a relabelling or a relabelling composed with conjugation —
stopped at exactly one step, quoted above: **no argument in the record produces a permutation of
the carrier from an isometry of the feature geometry restricted to the realizable set, the
isometries of that geometry not being characterized.** Three things stand in front of the programme
as a result:

1. **The object is now fixed, and it is not the whole tuple space.** The feature map is
   homogeneous of degree three, `mixedTriple (c • G) = c ^ 3 • mixedTriple G`, so the image of the
   whole tuple space is a cone whose isometries are a different and larger question; and the
   image of the whole feature space is the ambient `ℂ ^ 4096`, whose isometries are all the
   Euclidean ones. Neither is the orbit space. **The orbit space is the realizable quotient**: the
   realizable tuples, which carry the fixed diagonal `Γ` and no scaling freedom, modulo act 12's
   equivalence — and, by act 24's separation theorem and by that theorem only, its image under the
   feature map with the Euclidean metric restricted to it. That image is what this round calls the
   **normalized space**, and every isometry statement of this round is about it.
2. **The family act 24 tested is too small for the question act 24 left.** Act 24 asked whether an
   isometry is a carrier relabelling `RelabelTransition σ`, which applies one permutation `σ` to
   the fibre index and to both matrix indices at once, or such a relabelling composed with
   conjugation. But at `|A| = 1` the realizable tuple is the fibre-Gram data of one unitary `U`
   with prescribed moduli, a permutation of the **rows** of `U` and a permutation of its
   **columns** are independent operations, each preserves realizability at a constant `Γ`, each
   descends to classes, and each is a coordinate permutation of the feature index set and so an
   isometry; `RelabelTransition σ` is the diagonal case in which the two permutations agree. And
   the **transpose** of `U` exchanges rows and columns, exchanges the invisible row phases with act
   12's column phases, and so descends to a well-defined map on classes that is again realizable
   and again an isometry, by a coordinate identity recorded below. **The natural family is
   generated by the independent relabellings, the conjugation and the dilation transpose**, and a
   rigidity statement whose conclusion names a smaller family is refuted by the members it omits
   before any classification is attempted. This freeze names the larger family, in advance, and
   records whether the transpose is already generated by the others as an observation
   sub-question, since the freeze's hand reading does not settle it.
3. **Whether that family is all of the isometries is the classification question, and at the
   single-carrier configuration it has an internal route.** Every realizable tuple there is the
   fibre-Gram data of a `4 × 4` unitary with entries of modulus `½`, that is `½` times a complex
   Hadamard matrix of order four; the classes are those matrices modulo row and column phases; and
   the description of those matrices — every one is, after row and column permutations, act 23's
   `H(z)` at a unit parameter — is a finite case analysis from the unit-modulus identity, derivable
   from act 12's sufficiency theorem inside the kernel. With that description the normalized space
   is a finite union of circles, the Fourier circle and its images under the finite family, and
   the classification of its surjective isometries is a question about that finite union with an
   explicit metric. **The freeze's reading is that the family is the whole isometry group there; no
   complete route to a universal kernel proof of that is in hand, and `UNDECIDED` with the step
   named is the expected label.** At the product configuration the realizable classes are the
   `16 × 16` case, for which the freeze knows no internal description and imports none, and
   `UNDECIDED` is recorded in advance.

**Each target's proof route is the freeze's reading and not a finding**; whether it closes is for the
execution to establish, and every target may end `UNDECIDED` with its obstruction named. **What is
kept out of this round is named now**: composition in time, continuity, generators and any
one-parameter structure; the threading and the cross-time representative; the isometries of any
space other than the realizable quotient at the two frozen configurations; any `|A| > 1`; and any
comparison of any map with a unitary, antiunitary or quantum symmetry. Each is a separate question
for a separate freeze.

### What act 25 inherits, and consumes without re-proving

Consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**, and a
merged statement is not enlarged by being consumed.

1. **Act 12's `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity`,
   `sh1_sufficiency`, `gramPhaseEquiv_cross_invariant`**; **act 7's `AdmissibleDilationAt`**;
   **act 17's `GramTrajEquiv`** and its equivalence lemmas; **act 18's `ProperAt`,
   `PropagatesFrom`**.
2. **Act 20's `RelabelTransition`**, named as the diagonal case and consumed by the corollary
   where act 21's rungs mention it.
3. **Act 21's ladder**, as the declarations of its merged module, its product-embedding results
   `product_realizable`, `hadamard_entries`, `realizable_relabel`, `relabel_gramPhaseEquiv`,
   `relabel_one`, and `ol1a_descent`.
4. **Act 23's `hadamard_z_admissible`, `fibreGram_z_entries`, `zseq_facts`**, and its Fourier
   family `H(z)` as the lambda its merged statements carry.
5. **Act 24's `mixedTriple` and every named result of its module**, in particular
   `geo1_triple_metric` with its conjuncts (i)–(vi-b), `geo1_separation_single`,
   `geo1_equiv_of_zero_single`, `geo1_zero_of_equiv`, `features_eq_of_dist_zero`,
   `realizable_entry_ne_zero`, `dist_eq_norm_toLp`, `mixedTriple_relabel`,
   `geo2_relabel_isometry`, `mixedTriple_star`, `conj_eq_transpose`, `realizable_conj`,
   `conj_conj`, `conj_gramPhaseEquiv`, `conj_cross`, `geo3_phiConj_isometry`,
   `geo4_a0_isometry_injective`.
6. **Acts 21 through 24's historical verdicts are not changed by anything here**: act 24's twelve
   isometry verdicts and seven cells stand as act 24 states them; this round classifies and
   nothing is re-earned, re-graded or reinterpreted.

## The questions, FROZEN — four, gated

> **ISO1.** What is the normalized space — the realizable tuples at each frozen configuration
> modulo act 12's equivalence, carried by act 24's separation theorem onto its feature image with
> the Euclidean metric — and does the finite family generated by the independent relabellings of
> fibres and of matrix indices, the entrywise conjugation and the dilation transpose act on it: is
> each generator well defined on classes, realizability-preserving and an isometry, and does every
> word in the generators reduce to one of four shapes?
>
> **ISO2.** At the single-carrier configuration, is every realizable class the class of an
> independent relabelling of act 23's Fourier tuple at a unit parameter, and is every such tuple
> realizable — derived inside the kernel from act 12's sufficiency theorem and nothing else?
>
> **ISO3.** At the single-carrier configuration, is every surjective isometry of the normalized
> space — every map on realizable tuples that preserves realizability, is surjective on classes
> and preserves the distance on realizable tuples — equal on classes to a member of the finite
> family, and if not, which exhibited isometry lies outside it?
>
> **ISO4.** At the single-carrier configuration, does a transition family satisfying every
> condition of act 21's ladder before naturality and isometry of the geometry act on classes, at
> every time, as a member of the finite family?

Each is a question about act 12's exact equivalence, act 24's exact invariant family and geometry,
and act 21's exact declarations at the record's exact configurations. **The round does NOT try to
derive Schrödinger evolution**, does not classify the isometries of any other space, does not ask
whether the family is the right family or the geometry the right geometry, does not ask about
continuity or composition in time, and does not ask what any rung means beyond the declaration
act 21 froze.

### The correspondence with the owner's direction

| the owner's item | this freeze's target |
| --- | --- |
| `A25-1`, the normalized quotient geometry | `ISO1`, the normalized space, and the family that acts on it |
| `A25-2`, the abstract isometry classification | `ISO2`, the internal description of the realizable classes, gating `ISO3`, the classification of the surjective isometries |
| `A25-3`, the prefix-constrained transition-family corollary | `ISO4` |
| `A25-4`, the branch interpretation forbidden | the forbidden-sentence list and the non-doings, and the statement of every generator by its formula and by nothing else |

The split of `A25-2` into two targets is the key hazard made mechanical: the description of the
realizable classes is the step at which an external classification could be imported, so it is a
target of its own, with its own verdict commit, its own label and its own obstruction sentence,
and `ISO3` is opened only when it has closed at kernel level.

## The strength of the ask, FROZEN

**The ask is one action verdict over a closed family of four generators, one class-description
verdict at one configuration in two directions, one gated classification verdict with a positive
label earned only by a universal kernel proof and a negative label earned only by an exhibited
isometry, and one gated corollary verdict, each earned by its own named route or reported
undecided, in one fixed order.** It does **not** undertake a census, an independence claim, a
statement about the product configuration beyond the recorded cells, or the inference of one
target's status from another's beyond the consumptions the freeze places.

**What each verdict would and would not establish, stated in advance.** An action verdict says
that four specific maps written from the Gram data and the dilation act on the realizable classes
at the frozen configurations and preserve the frozen distance; it says nothing about maps not on
the list and nothing about the family being all the isometries. A class-description verdict says
that one specific set of tuples, modulo one specific equivalence, is exactly the set of
relabellings of one specific one-parameter tuple; it says nothing at `|A| > 1`, nothing at any
other `Γ`, and nothing about the product configuration. A classification verdict, in either
direction, is a statement about the exact hypotheses at the exact configuration on the exact
normalized space; a corollary verdict is that statement read through act 21's exact rungs; **no
outcome of this round says that any map is, resembles or approaches a unitary, an antiunitary, a
symmetry, a time reversal or quantum evolution.**

## The objects, FROZEN — act 12's, act 21's and act 24's, consumed; one normalized space and one family, bound by equation

`V`, `A`, `a₀`, `Γ`, the transition family, the law it generates, the admissible orbit state space
`Ω(Γ, t)` and the frozen quotient list are act 21's, at its lines 642–733, consumed without
restatement; `Ψ = mixedTriple` and `d` are act 24's, consumed without restatement. In particular:

- **The frozen quotient list** is act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv` and act 21's
  `LawEquiv`, and **no other equivalence may be used in any verdict**. Every "equal on classes"
  of this round is `GramPhaseEquiv`, and nothing is taken modulo anything else.
- **Realizable** means `RealizableGram (Fin 1) Γ₀` at the single-carrier configuration and
  `RealizableGram (Fin 1 × Fin 1) Γ` at the product configuration, exactly as act 24 uses the
  word.

### The normalized space, FROZEN — bound by equation, never defined

> **Statement.** At a frozen configuration `(V, A, Γ)`, the normalized space is the set of feature
> vectors of realizable tuples, `{Ψ G | RealizableGram A Γ G} ⊆ ((V × V × V) × (V × V × V)) → ℂ`,
> with the metric `d` restricted to it; by act 24's `geo1_triple_metric` (i) and (iii), `Ψ` maps
> the realizable classes bijectively onto it, and by (vi-a) and (vi-b) `d` on realizable tuples is
> its pullback.

**No Lean object is introduced for it.** A statement "about the normalized space" is a statement
about realizable tuples, with class equality written as `GramPhaseEquiv` and distance written as
`d` bound by act 24's equation, and the passage to the feature image is act 24's theorem consumed
where a statement needs it. In particular **a map of the normalized space** is, in every statement
of this round, a map `φ` on tuples together with the hypotheses written out:

```
(∀ G, RealizableGram A Γ G → RealizableGram A Γ (φ G))
  ∧ (∀ H, RealizableGram A Γ H → ∃ G, RealizableGram A Γ G ∧ GramPhaseEquiv (φ G) H)
  ∧ (∀ G H, RealizableGram A Γ G → RealizableGram A Γ H → d (φ G) (φ H) = d G H)
```

— realizability preserved, surjectivity on classes, isometry on realizable tuples — and **descent
to classes is not a hypothesis, because it follows**: equivalent inputs are at distance `0` by
`geo1_triple_metric` (vi-b), so their images are at distance `0` by isometry, hence equivalent by
(vi-a), which is act 24's cell `a0` read at the single carrier. **Nothing else is assumed of `φ`**:
not linearity, not affinity, not continuity, not that it is induced by any map on dilations.
**Neither compactness of the normalized space nor the quotient topology is assumed or used**:
surjectivity is a hypothesis where a statement needs it, and in the corollary it is supplied by act
21's `L3s`.

### The family, FROZEN — four generators and a normal form, each bound by its formula

On a carrier `V` with `[Fintype V] [DecidableEq V]`, an ancilla `A` with `Fintype.card A = 1` and
anchor `a₀`, and a symmetric `Γ` with constant entries:

> **(R) the independent relabellings.** For `π τ : Equiv.Perm V`,
> `G ↦ fun i => (G (π i)).submatrix τ τ`. Act 20's `RelabelTransition σ` is the case `π = τ = σ`.
>
> **(C) the entrywise conjugation.** `G ↦ fun i => Matrix.of fun j k => star (G i j k)`, act 24's
> `Φ_conj` at any time.
>
> **(T) the dilation transpose.** The relation on tuples
> `fun G G' => ∃ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U ∧ FibreGram a₀ U = G ∧ GramPhaseEquiv G' (FibreGram a₀ Uᵀ)`,
> which on realizable tuples is total and single-valued on classes, and is written relationally
> because it is defined through a choice of dilation.
>
> **The normal form.** Every word in the generators is equal on realizable classes to one of the
> four shapes `(π, τ)`, `(π, τ) ∘ C`, `(π, τ) ∘ T`, `(π, τ) ∘ C ∘ T`, by the relations, on classes,
> `T ∘ (π, τ) = (τ, π) ∘ T`, `T ∘ C = C ∘ T`, `T ∘ T = id`, `C ∘ C = id`, `C ∘ (π, τ) = (π, τ) ∘ C`
> and `(π, τ) ∘ (π', τ') = (π ∘ π', τ ∘ τ')`.

**Written out, the conclusion "`φ` is a member of the family on realizable classes" is the
proposition every classification statement of this round carries**, at the single-carrier
configuration with `Γ₀ ≡ ¼`, `A = Fin 1`, `a₀ = 0`:

```
∃ π τ : Equiv.Perm (Fin 4),
    (∀ G, RealizableGram (Fin 1) Γ₀ G →
        GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
  ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
        GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
  ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) U = G →
        GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
  ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) U = G →
        GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
          star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))
```

written out wherever a statement needs it, never abbreviated. The third and fourth disjuncts
quantify over **every** dilation of `G`, which is what single-valuedness on classes makes
equivalent to a choice of one. **The family is closed at these four generators at this freeze.** A
fifth generator discovered during execution is recorded as an observation and never added; a
surjective isometry outside the family is the witness of `ISO3`'s negative label and of nothing
else.

**Three things about these objects, fixed now.**

1. **Every generator is a coordinate permutation of the feature index set, up to conjugation.**
   `Ψ ((π, τ) G) p = Ψ G ((π, π, π) p.1, (τ, τ, τ) p.2)`, the relabelling case of act 24's
   `mixedTriple_relabel` with the two permutations separated; `Ψ (C G) p = star (Ψ G p)`, act 24's
   `mixedTriple_star`; and for `G = FibreGram a₀ U` at `|A| = 1`,
   `Ψ (FibreGram a₀ Uᵀ) ((i₁, i₂, i₃), (j₁, j₂, j₃)) = star (Ψ G ((j₂, j₃, j₁), (i₁, i₂, i₃)))`,
   because `FibreGram a₀ Uᵀ i j k = star (U (j, a) (i, a₀)) * U (k, a) (i, a₀)` and the three
   factors regroup as the conjugate of `G j₂ i₁ i₂ * G j₃ i₂ i₃ * G j₁ i₃ i₁`. Each is therefore an
   isometry by reindexing one finite sum along a bijection of the index set, as act 24's
   `geo2_relabel_isometry` reindexes its sum. **This is the reading; the kernel is what
   establishes it.**
2. **The transpose is well defined on classes because rows and columns of the dilation carry the
   two phase actions.** If `FibreGram a₀ U = FibreGram a₀ U'` with both admissible at `|A| = 1`
   then, no entry vanishing, each row of `U'` is a unit-modulus multiple of the corresponding row
   of `U` — from the coordinates `(j, j)` the moduli agree, and from the coordinates `(j₀, k)` the
   ratio is independent of `k` — so `U' = D * U` for a diagonal unitary `D`, `U'ᵀ = Uᵀ * D`, and
   `FibreGram a₀ U'ᵀ` is act 12's action by the diagonal of `D` on `FibreGram a₀ Uᵀ`. And if
   `G' i j k = star (c j) * G i j k * c k` with `G = FibreGram a₀ U`, then `U * diag c` is an
   admissible dilation of `G'`, its transpose is `diag c * Uᵀ`, and a diagonal unitary on the left
   leaves the fibre-Gram data unchanged. So the relation `T` is total on realizable tuples by
   `sh1_sufficiency`, single-valued on classes, and descends.
3. **Nothing is defined.** The definition budget below is **zero**; the normalized space, the
   family's generators, the relation `T`, the four-shape conclusion, the isometry proposition and
   every rung are bound variables or written-out propositions in the statements that need them,
   exactly as act 24 binds its geometry and act 21 binds its families. **A definition is a defect
   of the round.**

### The two frozen configurations

Act 21's two, and no other:

- **The single-carrier configuration**: `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ₀ ≡ ¼` — act 12's,
  the one act 24's `geo1_separation_single` is stated at. **This is the primary configuration of
  every target of this round**: `ISO2`, `ISO3` and `ISO4` are stated there, and their labels are
  earned there.
- **The product configuration**: `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`,
  `Γ ≡ 1/16` as the pointwise product `Γ₀ ⊗ Γ₀`, the decomposition `e = Equiv.refl (Fin 4 × Fin 4)`
  — act 21's, the one act 24's `GEO4` is stated at. `ISO1` is stated there as well as at the
  single carrier; `ISO2`, `ISO3` and `ISO4` carry a recorded **product cell** each, `ISO2-P`,
  `ISO3-P`, `ISO4-P`, whose expected outcome is `UNDECIDED` with the obstruction the key hazard
  names, and which **enter no label**.

`ISO1`'s action facts are stated at an arbitrary finite carrier with `Fintype.card A = 1` and a
constant symmetric `Γ` where they can be, and instantiated at both configurations.

**The one-`|A|`-value caveat, carried from acts 18 through 24 and recorded again.** `|A| = 1` is
the strongest case for the per-slice statements and is not degenerate there; it is not
automatically the right case for a cross-time statement, and every verdict of this round is at
that cardinality and at no other. **It is also the case in which the dilation is one unitary with
prescribed moduli and the transpose descends**; nothing here is asserted about `|A| > 1`.

## The ladder, CONSUMED and not restated, and the prefix the fourth target uses

The ladder is act 21's `L0`–`L5` in act 21's wording, at its lines 735–946, as the declarations of
`OrbitLawRigidityTwisted.lean` at blob `860daac4…`, conjoined as `LadderConds` in the order: the
two standing hypotheses `ProperAt` and `PropagatesFrom`, then `L0`, `L1`, `L2`, `L3` (`L3i` then
`L3s`), `L4d`, `L4n`, `L5`. **This round's module states no rung.**

**"The prefix through `L4d`" means, in every statement of this round, the first seven conjuncts of
`LadderConds`**, at the single-carrier configuration with `A = Fin 1`, `a₀ = (0 : Fin 1)`,
`Γ = fun _ => Γ₀`: `ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, the inline
`L2`, `Reversible`, the inline `L4d`. `L5` is act 21's `FactorizesOnProduct` at the product
configuration and enters only the recorded product cell `ISO4-P`; `L4n` enters nothing here.

### The verdict matrix, FROZEN

| target or cell | configuration | assumed | tested | route | explicitly out of scope |
| --- | --- | --- | --- | --- | --- |
| `ISO1` | both | the frozen configuration | each generator preserves realizability, descends to classes, is an isometry; `T` total and single-valued; the six relations of the normal form | coordinate permutation and reindexing; the row-phase lemma; act 12's sufficiency | the family being all the isometries |
| `ISO1-R` (observation) | single carrier | — | whether `T` equals some `(π, τ)` or `(π, τ) ∘ C` on every realizable class | the finite check on the Fourier tuple and one relabelled Fourier tuple, if reached; enters no label | — |
| `ISO2` | single carrier | realizability | the class is a relabelled Fourier class, and conversely | dephasing through act 12's sufficiency, the unit-modulus identity, the finite case analysis | the product configuration; `|A| > 1`; any other `Γ` |
| `ISO2-P` (cell) | product | realizability | the same, for a description the freeze does not have | none known; `UNDECIDED` recorded in advance unless a universal theorem is obtained | any import |
| `ISO3` | single carrier | realizability preserved, surjectivity on classes, isometry | membership in the family, the four-shape conclusion | through `ISO2`'s description: the circles, their metric, the special points; the optional lemma `ISO3-L` | any other space; any linearity assumption |
| `ISO3-L` (optional lemma) | single carrier | the same | extension of `φ` to an affine isometry of the real affine span of the normalized space | the classical extension argument, if reached; enters no label | linearity assumed anywhere |
| `ISO3-P` (cell) | product | the same | the same | none known; `UNDECIDED` recorded in advance | any import |
| `ISO4` | single carrier | the prefix through `L4d`, isometry | at every `t`, `Φ t` is a member of the family on realizable classes | `L1` for realizability, `L3s` for surjectivity, `ISO3` to classify | `L4n`; `L5`, which is not stated at this configuration |
| `ISO4-P` (cell) | product | the prefix through `L4d`, `L5`, isometry | the same | none; needs `ISO3-P` | — |

**Nothing in one row is inferred from another row** beyond the consumptions the rows name: `ISO3`
consumes `ISO2`, `ISO4` consumes `ISO3`, and the cells consume nothing and earn nothing.

### The labels of each target, and the three-way discipline

For each target the frozen route is the **named construction or the named proof route**. A positive
universal label (`ISO1-FAMILY-ACTS`, `ISO2-CLASSIFIED`, `ISO3-RIGID`, `ISO4-CLASSIFIED`) is
earned only by a universal kernel proof; the one negative label of the round, **`ISO3-NOT-RIGID`,
only by an exhibited map** satisfying the three hypotheses at kernel level together with one
exhibited realizable tuple whose image is inequivalent to every one of the four shapes for every
`π`, `τ`, the separating invariant named; **`UNDECIDED` by the recorded statement that neither was
reached, with the obstruction named.** A universal proof is a finding about the condition; it is
never inferred from the failure of a witness, never from the absence of one, and never from census
silence. **Failure to obtain a universal theorem is `UNDECIDED`, never a positive label and never a
negative one.** `ISO1`, `ISO2` and `ISO4` have no negative label: the freeze predicts no witness
against any of them, and a witness found is an observation under the anti-expansion rule.

**On `ISO3`'s negative label, stated exactly.** The freeze names no candidate isometry outside the
family, so a `NOT-RIGID` witness, if there is one, is found during execution. **For this target
alone** such a witness is admissible: it is recorded with the span in which it was found and the
attestation answer that discloses it, its three hypotheses and its separating tuple are proved in
the kernel in the `ISO3` verdict commit, and no other target and no cell is answered by it. A
candidate that fails one of its hypotheses at kernel level is recorded and earns nothing.

## The gate, FROZEN — the execution order and the three failure rules

**The gate is this round's freeze rule and not an `AGENTS.md` rule.** It exists because the four
targets are not independent in meaning: a classification attempted before the family is known to
act, or before the class space is described, would be a verdict about the wrong object or about a
substituted domain; a corollary read through act 21's rungs before the classification has closed
would report a consequence of nothing. The gate keeps every verdict about the object the freeze
names, and it is what makes the key hazard mechanical.

### Safeguard 1 — the fixed order, one verdict commit per executed target, and the attestation set at every boundary

The targets are executed in the order **`ISO1` → `ISO2` → `ISO3` → `ISO4`**, and in no other.

The execution's commits on the first-parent chain from `B` are, in order: **the stage-A commit**
(the two declarations set to `B`, in the guard file only); **the module commit** (the module with
its shared lemmas and **no verdict of any target** — no named result of `ISO1`, `ISO2`, `ISO3` or
`ISO4`); then **exactly one verdict commit per executed target**, in target order, each carrying
that target's named results, its cells and its observation sub-question if any, and nothing of a
later target's; then the packaging commit. A target the gate does not open has **no verdict
commit**, and its label is the label the gate rule below names, with the frozen sentence. A verdict
commit that carries a later target's result, or a target executed out of order, is recorded as a
discrepancy and the round's ordering obligation is reported as undischarged for that target.

**The attestation set is answered at every boundary.** Act 20's three questions, in act 21's
wording at its lines 1033–1043 — **Q1 INTENTIONAL**, **Q2 INCIDENTAL**, **Q3 UNAIDED REASONING** —
are answered by the result note **once per span**, for the spans `B` → module commit, module commit
→ `ISO1`'s verdict commit, `ISO1` → `ISO2`, `ISO2` → `ISO3`, `ISO3` → `ISO4`, each answer a
measurement about what the execution acquired **in that span** bearing on any target **not yet
closed at the span's end**; a span ending at a target the gate did not open is answered for the
targets that remain. The partial-fact rule applies at every boundary: learning during `ISO1` that
a particular realizable class is or is not a relabelled Fourier class is a YES; learning during
`ISO2` that a particular map is or is not in the family is a YES. A YES is disclosed with what was
learned, when, and whether any later target's route changed afterwards; it is not concealed and not
argued away, and a disclosure does not cure it. **What the freeze itself places in front of the
execution is not a YES and is listed rather than left implicit**: this file carries the proof route
for every target, the coordinate identities, the row-phase lemma, the unit-modulus identity, the
shape of the case analysis, the consumption of `ISO2` by `ISO3` and of `ISO3` by `ISO4`, and act
24's result carries every consumed fact; the questions are about what was acquired beyond the freeze
and the pinned blobs.

### Safeguard 2 — the route-authorization matrix

**Each named construction or route may answer exactly the target this matrix authorizes, and no
other.** A fact found or learned during a later target's work may not be retroactively assigned to
an earlier target; an alternative route for any target found during execution is an observation
and never substituted.

| construction or route | `ISO1` | `ISO2` | `ISO3` | `ISO4` |
| --- | --- | --- | --- | --- |
| the coordinate permutations of the three generators, the reindexing of the sum, the row-phase lemma, the transpose's admissibility and descent, the six relations | **authorized** | — | — | — |
| the dephasing through `sh1_sufficiency`, the unit-modulus identity, the finite case analysis over the placement of the antipodal pairs, the converse through `hadamard_z_admissible`, `sh1_necessity` and `ISO1`'s relabelling facts | — | **authorized** | — | — |
| `ISO2`'s description consumed; the intrinsic metric of the Fourier circle; the cross distances; the special points; the optional extension lemma; an exhibited isometry outside the family, if found | — | — | **authorized** | — |
| `L1`, `L3s` and isometry read into `ISO3`'s hypotheses at each `t`; `ISO3` consumed | — | — | — | **authorized** |
| the shared lemmas of the module commit | consumed | consumed | consumed | consumed |

**Shared lemmas are not verdicts.** The module commit's lemmas — the three coordinate identities,
the reindexing lemma with two permutations, the row-phase lemma, the admissibility of the transpose
at `|A| = 1`, the unit-modulus identity `(a + b)(b + c)(c + a) = (a + b + c)(ab + bc + ca) − abc`
and its antipodal-pair consequence, the dephasing lemma, the feature coordinates of `F(z)` as
monomials in `z` and `star z` — are consumed by whichever verdict needs them and answer no target by
themselves.

### Safeguard 3 — the outcome-vector table

The round's headline is a **vector of four labels**, one per target, each drawn from its target's
frozen label set, and **the headline is selected verbatim from the outcome-vector table in the
status rule below**, which lists every admissible vector under the gate. No single-label headline,
no summary label and no combination label exists for this round.

### Failure rule 1 — a universal theorem not obtained is `UNDECIDED`

For every target and every cell, failure to obtain a universal theorem — whether or not one was
attempted — is reported as the `UNDECIDED` label with the obstruction named, never as the positive
label and never as the negative one. Census silence is not a finding about any condition.

### Failure rule 2 — a route that fails its own reading is recorded, not repaired

If a named route unexpectedly fails a step the freeze's reading takes for granted — a coordinate
identity that the kernel computes differently, a case of the finite analysis that does not reach
the Fourier form, a relation of the normal form that fails on classes — the execution **records
that fact**, with the step, and the target takes its **preregistered fallback outcome — its
`UNDECIDED` label with that obstruction named**. **The family is not repaired, no generator is
added or removed, no domain is substituted for the realizable quotient, and no external statement
is imported to bridge the step.**

### Failure rule 3 — the gate closes forward and never reopens, and the key hazard's form of it

`ISO2` is executed only if `ISO1` reaches `ISO1-FAMILY-ACTS`; `ISO3`'s route is run only if `ISO2`
reaches `ISO2-CLASSIFIED`; `ISO4` only if `ISO3` reaches `ISO3-RIGID`. The labels of unopened
targets are fixed by the gate:

- if `ISO1` does not reach its label, `ISO2` takes `ISO2-NOT-EXECUTED`, `ISO3` takes
  `ISO3-NOT-EXECUTED` and `ISO4` takes `ISO4-NOT-EXECUTED`;
- **if `ISO1` reaches its label and `ISO2` does not, `ISO3` takes `ISO3-UNDECIDED`** — the key
  hazard's outcome, by the owner's direction — with the frozen obstruction sentence "the realizable
  image at the configuration was not classified internally", **its route not run, no external
  classification imported and no weaker domain substituted**; and `ISO4` takes
  `ISO4-NOT-EXECUTED`;
- if `ISO3` reaches `ISO3-NOT-RIGID` or `ISO3-UNDECIDED`, `ISO4` takes `ISO4-NOT-EXECUTED`.

A target the gate does not open has no verdict commit; **no partial execution of a closed target is
reported as anything**, and a closed target's route is not attempted "for information". The gate
reads the label as earned and never the freeze's prediction. The product cells `ISO2-P`, `ISO3-P`,
`ISO4-P` are recorded inside their target's verdict commit when that target is executed, and take
their `UNDECIDED` sentences otherwise.

## The family's analysis, recorded here as the freeze's reading and not as a finding

Throughout, `F(z) := FibreGram (0 : Fin 1) (H z)` with `H z` act 23's Fourier matrix at a unit
parameter, written in every statement as the lambda act 23's `hadamard_z_admissible` carries,
`Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)`;
`(π, τ) G` is `fun i => (G (π i)).submatrix τ τ`; `C G` is the entrywise conjugate; `T G` is any
`G'` the transpose relation relates to `G`; `∼` is act 12's `GramPhaseEquiv`; `Ψ` is
`mixedTriple`; and "realizable" is as fixed above.

- **(R) preserves realizability at a constant `Γ`.** Positive semidefiniteness and rank are
  invariant under `submatrix τ τ`; `∑ i, (G (π i)).submatrix τ τ = (∑ i, G i).submatrix τ τ =
  (1 : Matrix).submatrix τ τ = 1`; and the diagonal `Γ (π i) (τ j) = Γ i j` for a constant `Γ`.
  Act 21's `realizable_relabel` is the diagonal case and is consumed where it applies.
- **(R) descends.** If `G' i j k = star (c j) * G i j k * c k` then `((π, τ) G') i j k = star (c (τ
  j)) * ((π, τ) G) i j k * c (τ k)`, the phases `c ∘ τ`.
- **(R) is an isometry.** `Ψ ((π, τ) G) p = Ψ G ((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ
  p.2.2.1, τ p.2.2.2))`, and the sum over `p` is reindexed along the bijection
  `(π.prodCongr (π.prodCongr π)).prodCongr (τ.prodCongr (τ.prodCongr τ))`, as act 24's
  `geo2_relabel_isometry` reindexes along the diagonal one.
- **(C).** Realizability by act 24's `realizable_conj`, descent by `conj_gramPhaseEquiv`, the
  involution by `conj_conj`, isometry from `mixedTriple_star` as `geo3_phiConj_isometry` proves it
  at the product configuration; the arbitrary-carrier statement is proved here from the same
  lemma.
- **(T) is admissible at `|A| = 1` for a symmetric `Γ`.** `Uᵀ` is unitary; `∑ a, ‖Uᵀ (i, a) (j,
  a₀)‖ ^ 2 = ‖U (j, a₀) (i, a₀)‖ ^ 2 = Γ j i = Γ i j` when `A` has one element. So `FibreGram a₀
  Uᵀ` is realizable by `sh1_necessity`.
- **(T) is total, single-valued on classes, and descends** — as the objects section reads it: the
  row-phase lemma from the coordinates `(j, j)` and `(j₀, k)` at full support, the transpose of a
  right diagonal factor being a left diagonal factor and conversely.
- **(T) is an isometry.** The coordinate identity `Ψ (FibreGram a₀ Uᵀ) ((i₁, i₂, i₃), (j₁, j₂,
  j₃)) = star (Ψ (FibreGram a₀ U) ((j₂, j₃, j₁), (i₁, i₂, i₃)))` at `|A| = 1`, from
  `fibreGram_apply` with the one-element sum, then the sum reindexed along the bijection
  `p ↦ ((p.2.2.1, p.2.2.2, p.2.1), p.1)` of `(V × V × V) × (V × V × V)` and `norm_star`.
- **The six relations, on classes.** `T ∘ (π, τ) = (τ, π) ∘ T`: `(π, τ) (FibreGram a₀ U) =
  FibreGram a₀ (P_π U P_τ)` for the permutation matrices, and `(P_π U P_τ)ᵀ = P_τᵀ Uᵀ P_πᵀ`, with
  `P_τᵀ = P_{τ⁻¹}`, so the transpose of the relabelled dilation is the `(τ, π)`-relabelling of the
  transposed dilation up to the inverse permutations, which the existential over `π`, `τ`
  absorbs. `T ∘ C = C ∘ T`: `star ∘ transpose = transpose ∘ star` entrywise, and the conjugate of
  an admissible dilation is admissible. `T ∘ T = id` on classes: `Uᵀᵀ = U`. `C ∘ C = id`:
  `conj_conj`. `C ∘ (π, τ) = (π, τ) ∘ C`: entrywise. `(π, τ) ∘ (π', τ') = (π ∘ π', τ ∘ τ')`: by
  `submatrix_submatrix`. Hence every word reduces to `(π, τ) ∘ C ^ e ∘ T ^ t` with `e, t ∈ {0, 1}`.
- **The accounting act 24 asked for.** `ΦI` is `(1, 1)`; `ΦP` and `ΦT`'s maps are `(σ, σ)` and
  `(1, 1)`; at the product configuration `ΦPP` is `(σ × σ, σ × σ)`, `Φ_swap` is `(prodComm,
  prodComm)`, `Φ_conj` is `C`; each is a named element of the family, and no non-isometry of act
  24's list satisfies the isometry hypothesis, so none is a candidate for membership. **This
  accounting is a control of `ISO1` and earns no label.**

**On whether `T` is generated by `(R)` and `(C)` — the observation sub-question `ISO1-R`.** `H z`
is a symmetric matrix, so `T` fixes every Fourier class `[F(z)]`; a `(π, τ) ∘ C ^ e` equal to `T`
on all classes would therefore fix every Fourier class too, and would have to send the class of
`(swap 0 1, 1) F(z)` — the dilation with its first two rows exchanged — to the class of
`(1, swap 0 1) F(z)`, the dilation with its first two columns exchanged, which is what `T` does
there. **The freeze's hand reading does not settle whether any `(π, τ) ∘ C ^ e` does both**; the
outcomes are `T-REDUNDANT` (one `(π, τ, e)` agrees with `T` on every realizable class, proved
universally), `T-NEW` (one exhibited realizable tuple whose `T`-image is inequivalent to all
`1152` images `(π, τ) C ^ e G`, each inequivalence read through a named invariant), or
`ISO1-R-UNDECIDED`, and **it enters no label**: the family is frozen with all four generators
either way, and the classification statement is the same statement either way.

## The class-description route, recorded as the freeze's reading

At the single-carrier configuration, for a realizable `G`:

1. **The dilation.** `sh1_sufficiency` gives `U` with `AdmissibleDilationAt Γ₀ 0 U` and
   `FibreGram 0 U = G`; write `u i j := U (i, 0) (j, 0)`, so `‖u i j‖ ^ 2 = ¼` for every `i j`, no
   entry vanishes, and `U` is unitary.
2. **Dephasing.** With the unit-modulus phases `r i := 2 * star (u i 0)` and `c j := 2 * star (u 0
   j) * (2 * u 0 0)`, the matrix `K i j := 2 * r i * u i j * c j` has unit-modulus entries,
   `K i 0 = 1` and `K 0 j = 1`, and `K / 2` is unitary; `FibreGram 0 (K/2)` is `G` acted on by the
   phases `c` — the row phases `r` being invisible to `FibreGram` — so `FibreGram 0 (K/2) ∼ G`.
   **This is the step at which the classes become the dephased matrices**, and it uses act 12's
   theorem and nothing else.
3. **The antipodal lemma.** For unit-modulus `a b c` with `1 + a + b + c = 0`: conjugating gives
   `1 + 1/a + 1/b + 1/c = 0`, so `ab + bc + ca + abc = 0`, and
   `(a + b)(b + c)(c + a) = (a + b + c)(ab + bc + ca) − abc = −(ab + bc + ca) − abc = 0`; hence one
   of `a + b`, `b + c`, `c + a` vanishes and the remaining entry is `−1`. **So every row `K i`,
   `i ≥ 1`, is, after one permutation of the columns `1, 2, 3`, of the form `(1, x, −1, −x)` with
   `x` of modulus one.**
4. **The case analysis.** *Case A — some row is not real*: choose `i` with `x ∉ {1, −1}`; after a
   column permutation `τ` fixing `0`, `K i = (1, x, −1, −x)`, and its `−1` is in column `2` alone.
   For another row `K j = (1, y, −1, −y)` up to the position of its `−1`: if the `−1` is in column
   `2`, orthogonality with `K i` gives `2 (1 + y * star x) = 0`, so `y = −x` and
   `K j = (1, −x, −1, x)`; if the `−1` is in column `1`, `K j = (1, −1, y, −y)` and orthogonality
   gives `(1 − star x)(1 − y) = 0`, so `y = 1` and `K j = (1, −1, 1, −1)`; if the `−1` is in column
   `3`, `K j = (1, y, −y, −1)` and orthogonality gives `(1 + star x)(1 + y) = 0`, so `y = −1` and
   `K j = (1, −1, 1, −1)` again. The two rows other than `K i` are orthogonal to each other and so
   distinct, hence they are `(1, −x, −1, x)` and `(1, −1, 1, −1)` in one order or the other; and
   these four rows are, in some row order `π`, the rows of `H x`, since `H x`'s rows are
   `(1, 1, 1, 1)`, `(1, x, −1, −x)`, `(1, −1, 1, −1)`, `(1, −x, −1, x)`. *Case B — every row is
   real*: each row `i ≥ 1` has two entries `−1` among the columns `1, 2, 3`, the three such rows
   are `(1, 1, −1, −1)`, `(1, −1, 1, −1)`, `(1, −1, −1, 1)` in some order, and these are the rows of
   `H 1`. In both cases `K = P_π (H z) P_τ` for a unit `z` and permutations `π`, `τ`, and
   `FibreGram 0 (K/2) = (π, τ) (F(z))` by `fibreGram_apply` and `submatrix_apply`.
5. **The converse.** `(π, τ) (F(z))` is realizable by `hadamard_z_admissible`, `sh1_necessity` and
   `ISO1`'s relabelling fact.

**The statement is an equality of two sets of classes, stated as two directions** under `§A.34`:
every realizable tuple is equivalent to a relabelled Fourier tuple, and every relabelled Fourier
tuple is realizable. **Nothing in the route reaches outside act 12's merged theorem and elementary
algebra**, and that is the whole reason the route is admissible: a step at which the execution
would need the classification as a fact rather than derive it is the key hazard's trigger, and the
target ends `UNDECIDED` there.

## The classification route, recorded as the freeze's reading, and where it is not in hand

With `ISO2` closed, the normalized space at the single carrier is the finite union of the circles
`C_{(π, τ)} := {[(π, τ) F(z)] : star z * z = 1}` over `π τ : Equiv.Perm (Fin 4)`, and it is
**exactly** that union — not a subfamily, not a sample. The freeze records:

1. **The intrinsic metric of the Fourier circle depends on the angle difference alone.** Every
   entry of `F(z)` is one of `±¼`, `±z/4`, `±star z/4`, so every coordinate of `Ψ (F(z))` is
   `± z ^ k / 64` for an integer `k` with `−3 ≤ k ≤ 3` and `star z * z = 1`; hence
   `d (F(z)) (F(w)) ^ 2 = (1/4096) ∑ p, ‖z ^ k_p − w ^ k_p‖ ^ 2`, a function of `w / z` only. The
   rotations `z ↦ e^{iα} z` are isometries **of the circle** for its intrinsic metric; whether any
   extends to the union is the whole question, and the freeze's reading is that none does except
   the finitely many the family induces, because the cross distances `d ((π, τ) F(z)) ((π', τ')
   F(w))` are sums of terms `‖ε z ^ k − ε' w ^ k'‖ ^ 2` with `k ≠ k'`, which are not functions of
   `w / z`.
2. **The special classes.** `[F(1)]`, `[F(−1)]`, `[F(i)]`, `[F(−i)]` and their relabellings are
   the classes at which distinct circles meet — the real Hadamard tuple and the Fourier tuple,
   whose relabelling stabilizers are larger than the generic one — and an isometry permutes the
   finite set of classes whose distance profile is exceptional. **The freeze does not derive that
   this finite set is the set of intersection points, nor that an isometry preserving it and each
   circle is in the family.**
3. **The optional lemma `ISO3-L`.** Any map satisfying the three hypotheses is a distance-preserving
   map of a subset of the Euclidean space `((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → ℂ`,
   read as a real inner-product space, into itself, and by the classical argument extends to an
   affine isometry of the real affine span of the normalized space. **If proved, this is an aid to
   the route above and enters no label; if not proved, nothing changes; and in no statement of this
   round is an isometry assumed affine or linear.** Linearity is earned or absent.

**No complete route from these facts to the four-shape conclusion is in hand at this freeze.** The
execution attempts the route in the order 1, 3, 2, and the step not reached is the obstruction the
`UNDECIDED` sentence names. **`ISO3-UNDECIDED` is the expected label**, at medium strength; the
freeze's reading of the proposition's truth is that the family is the whole isometry group, at
low strength, and the label is earned by the kernel and by nothing stated here.

## The countercontrols and the positive controls, one per target and cell

| target or cell | the route this freeze names | configuration |
| --- | --- | --- |
| `ISO1` (R) | realizability at constant `Γ`, descent with `c ∘ τ`, isometry by reindexing along `(π, π, π) × (τ, τ, τ)` | both |
| `ISO1` (C) | act 24's four conjugation facts consumed; isometry at an arbitrary carrier from `mixedTriple_star` | both |
| `ISO1` (T) | admissibility of `Uᵀ` at `|A| = 1`; totality by `sh1_sufficiency`; the row-phase lemma; single-valuedness and descent by the two-sided phase bookkeeping; isometry by the coordinate identity and reindexing along `p ↦ ((p.2.2.1, p.2.2.2, p.2.1), p.1)` | both |
| `ISO1` normal form | the six relations as read above | both |
| `ISO1-R` | `T` fixes every `[F(z)]`; the finite check at `(swap 0 1, 1) F(z)`, if reached | single carrier |
| `ISO2` | the dilation, the dephasing, the antipodal lemma, the case analysis, the converse, as read above | single carrier |
| `ISO2-P` | none known; `UNDECIDED` in advance with the obstruction: the classes are `16 × 16` unit-modulus unitaries modulo two-sided phases, the antipodal lemma gives no structure for a sum of sixteen unit vectors, and no description is imported | product |
| `ISO3` | the intrinsic metric, the optional extension, the special classes, in that order; `UNDECIDED` at the step not reached | single carrier |
| `ISO3-L` | the classical extension argument on the real affine span | single carrier |
| `ISO3-P` | none known; `UNDECIDED` in advance: needs `ISO2-P` | product |
| `ISO4` | `PreservesAdmissible` gives realizability preserved; `Reversible`'s second conjunct gives surjectivity on classes; the isometry hypothesis is `ISO3`'s third; `ISO3` at each `t` | single carrier |
| `ISO4-P` | none; needs `ISO3-P`; `NOT-EXECUTED` in advance | product |

**Evidence that earns any control or countercontrol**: a Lean theorem at evidence level 2 whose
statement pins the geometry by act 24's equation and every generator by its frozen formula,
discharges realizability from merged results or from the module commit's lemmas, and — for a
negative — certifies the separating quantity at a named coordinate through a named invariant.
**Searching and not finding earns nothing.**

## What was and was not run before this freeze

**No drafting-time check of any target's outcome was run.** By the owner's direction this control
plane was drafted from the sealed record alone: no kernel proof, no exact-arithmetic computation
of any invariant, distance or class, no enumeration of the relabelled Fourier classes, no test of
whether `T` is generated by the other generators, and no test of any construction above was
performed. **Every value and every step in the analyses above is the freeze's reading**, derived by
hand from the merged declarations, and the execution is what establishes or refutes each. A value
or a step stated above that the kernel computes differently is a discrepancy of the freeze's
reading, recorded in the result note and not repaired; it changes no label by itself, the label
being earned by what the kernel proves.

**One simulation was run, and it concerns chronology only.** A throwaway detached worktree at `D`
with the two declarations set to `D` under the stem `OGC` — no Lean file, no guard clause, no
record — was run against the guard at `D`: every one of the eighty-eight `R7-*` tags passed,
`R7-OLT`, `R7-OLN`, `R7-OLG` and `R7-OGS` each classified `ARCHIVED`, reading their own records
and nothing of the declaration. **No contract of any closed round needs superseding for this round
to execute**, and the supersession table below is therefore empty. The simulation's commit exists
on no branch of the repository.

## The ordering obligation, as it binds a gated round with a definition budget of zero

> **The ordering obligation, act 25.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence is act 12's at blob `4bba2040…`, the invariant family and the geometry are act 24's
> at blob `ce9d1aa0…`, and nothing else. The execution's module **states no rung, no equivalence
> and no definition of any kind**; the geometry is bound, in every theorem that names it, to act
> 24's equation; each generator of the family is written, in every theorem that names it, by its
> frozen formula; the transpose is written by its frozen relation; and the four-shape conclusion is
> written out in every classification statement. From the first commit that adds the module to the
> certified head `E`, **no commit of the branch adds a definition, restates a rung, alters the
> geometry's equation, alters a generator's formula, adds or removes a generator, or uses an
> equivalence outside the frozen quotient list**; the module commit carries no verdict of any
> target; the verdict commits of the executed targets follow it in the order `ISO1`, `ISO2`,
> `ISO3`, `ISO4`; and no theorem of a later target's section is present before that target's
> verdict commit.

### What the execution must record

1. **The declaration table.** For `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
   `AdmissibleDilationAt`, `RelabelTransition`, `mixedTriple`, each rung the fourth target's prefix
   names, and act 23's `H z`, the merged declaration consumed with its line range at its blob; and
   for this round's module the statement that it carries **no definition** — checked mechanically
   by `R7-OGC`, which requires the module to contain no line beginning with `def `, `abbrev `,
   `structure `, `class `, `instance `, `axiom ` or `opaque `, and the import
   `OIBridge.OrbitGeometrySelector`.
2. **The stage-A commit.** The SHA of the commit that sets the two declarations to `B`, and nothing
   else.
3. **The module commit.** The SHA of the first commit at which the module is present, with the
   named results it carries, each of which is a shared lemma and none a verdict.
4. **The verdict commits**, in order, each with its SHA and its named results; and, for each target
   the gate did not open, the statement that it has none.
5. **The immutability span.** The statement, with the command that checks it, that between the
   module commit and `E` no diff introduces a definition:
   `git diff <module commit> <E> -- verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean`
   contains no added or removed line beginning with `def `, `abbrev `, `structure `, `class `,
   `instance `, `axiom ` or `opaque `.
6. **The quotient, geometry and family record.** The only equivalence used in any verdict is act
   12's `GramPhaseEquiv`; the geometry's equation and every generator's formula are the displayed
   ones at every mention; **no equivalence was introduced or widened, no generator was added or
   removed, no domain was substituted for the realizable quotient, and nothing was imported**.
7. **The five attestation answers**, one per span, as safeguard 1 fixes them.
8. **The gate record.** For each of `ISO2`, `ISO3`, `ISO4`, the label of the target before it as
   earned, and whether the gate opened; for `ISO3`, whether the key hazard's form of the gate
   applied.

### The anti-expansion rule, FROZEN

**If execution discovers a fifth generator, a second normalized space, a second geometry, a further
equivalence, a further rung, a further configuration, a description of the product configuration's
classes that the freeze did not name a route for, a strengthening of a merged theorem, or a
universal implication for a cell the freeze recorded undecided in advance, it is recorded as an
observation for a later round with its own freeze and is not executed here.** The family is closed
at four generators, the normalized space at the realizable quotient, the geometry at act 24's, the
quotient list at three, the ladder at act 21's `L0`–`L5`, the configurations at act 12's and act
21's. **The one exception the freeze itself places**: a surjective isometry outside the family,
found during `ISO3`, is `ISO3`'s negative witness and is executed there, under the conditions the
label discipline fixes.

## The targets, FROZEN

Five targets, `ISO0` through `ISO4`; `ISO0` is type P and is the record check every round of this
programme has carried, and `ISO1`–`ISO4` are the gated bundle. Each names what settles it and what
evidence counts.

### `ISO0` — does the merged record already decide any of the four questions?

**The question.** At `B`, does the merged record contain a statement classifying the realizable
tuples at either frozen configuration modulo act 12's equivalence, or a statement that a map
other than a carrier relabelling or the entrywise conjugation is an isometry of act 24's geometry,
or a statement that every isometry of it is of any named form, or a statement that any condition
of act 21's ladder with isometry forces a law to act on classes as a member of any named family?

**What settles it.** Locating and quoting, under act 21's evidence rule at its lines 1456–1467,
over a bounded file set: act 12's `result.md` and module, act 21's `preregistration.md`,
`amendments/amendment-1.md`, `result.md` and module, act 23's `preregistration.md`, `result.md`
and module, act 24's `preregistration.md`, `result.md` and module, and `verification/ROADMAP.md`,
with the terms `isometr`, `classif`, `Hadamard`, `Fourier`, `dephas`, `transpos`, `conjugat`,
`antiunitar`, `Wigner`, `rigid`, `relabel`, `permut`, `affine`, `linear`, `compact`.

**This is a type-P target.** No Lean is written for it, no outcome of it is a theorem, and this
round's own theorems are not retro-evidence about it. **Reconstructive inference is forbidden as a
finding; where the record is silent, the finding is that it is silent.** This round's own control
plane is inside the set by construction and its hits are recorded as not relevant to the question.
Act 24's twelve isometry verdicts, its `b₀` witness and its `b` obstruction are expected to be
found, and are recorded as what they are: verdicts about named maps and a recorded non-attainment,
which decide none of the four questions.

### `ISO1` — the normalized space and the family that acts on it

**The statement.** For an arbitrary finite carrier `V`, an ancilla with `Fintype.card A = 1`, an
anchor `a₀` and a constant symmetric `Γ`, with `d` bound to act 24's equation: (i) for every `π τ`
and every realizable `G`, `(π, τ) G` is realizable; (ii) for every `π τ` and all `G G'`,
`GramPhaseEquiv G G' → GramPhaseEquiv ((π, τ) G) ((π, τ) G')`; (iii) for every `π τ` and all
`G H`, `d ((π, τ) G) ((π, τ) H) = d G H`; (iv) for all `G H`, `d (C G) (C H) = d G H`, with
realizability and descent of `C` consumed from act 24; (v) for every admissible `U`, `Uᵀ` is
admissible; (vi) for every realizable `G` there is an admissible `U` with `FibreGram a₀ U = G`;
(vii) for admissible `U U'` with `FibreGram a₀ U = FibreGram a₀ U'`,
`GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ)`; (viii) for admissible `U` and every `G'`
with `GramPhaseEquiv (FibreGram a₀ U) G'`, there is an admissible `U'` with `FibreGram a₀ U' = G'`
and `GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ)`; (ix) for admissible `U U'`,
`d (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ) = d (FibreGram a₀ U) (FibreGram a₀ U')`; (x) the six
relations of the normal form, each stated on classes with the transpose relation written out; and
(xi) the instantiation of (i)–(x) at both frozen configurations.

**What settles it.** One Lean theorem at evidence level 2, `iso1_family_acts`, carrying the
conjuncts above, with the observation sub-question `ISO1-R` recorded in the same verdict commit
under its own name if reached. **`ISO1-FAMILY-ACTS` is earned only by all of (i)–(xi) together**;
a generator proved an isometry without descent, or a transpose proved an isometry without
single-valuedness, earns `ISO1-UNDECIDED` with the missing conjunct named as the obstruction.

### `ISO2` — the internal description of the realizable classes at the single carrier

**The statement.** With `Γ₀ ≡ ¼`: (a) for every `G` with `RealizableGram (Fin 1) Γ₀ G` there are
`π τ : Equiv.Perm (Fin 4)` and `z : ℂ` with `star z * z = 1` and
`GramPhaseEquiv G (fun i => (FibreGram (0 : Fin 1) (H z) (π i)).submatrix τ τ)`; (b) for every
`π τ` and every `z` with `star z * z = 1`,
`RealizableGram (Fin 1) Γ₀ (fun i => (FibreGram (0 : Fin 1) (H z) (π i)).submatrix τ τ)`; with
`H z` written as act 23's lambda.

**What settles it.** One Lean theorem at evidence level 2, `iso2_classes_single`, carrying (a) and
(b) as **separate conjuncts** under `§A.34`. **`ISO2-CLASSIFIED` is earned only by both together,
and only by a proof whose every step is derived from the pinned blobs**; (b) alone, or (a) proved
for a subfamily of the realizable tuples, earns `ISO2-UNDECIDED` with the case named. **The
product cell `ISO2-P`** records `ISO2-P-UNDECIDED` with the frozen obstruction unless the
corresponding two-direction theorem at the product configuration is obtained, in which case it
records `ISO2-P-CLASSIFIED`; it enters no label.

### `ISO3` — the classification of the surjective isometries at the single carrier

**The statement.** With `Γ₀ ≡ ¼` and `d` bound to act 24's equation, for every
`φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)` satisfying the three
hypotheses displayed in the objects section — realizability preserved, surjectivity on classes,
isometry on realizable tuples — the four-shape conclusion displayed there.

**What settles it.** For the positive label: one Lean theorem at evidence level 2,
`iso3_isometries_single`, universal in `φ`. For the negative label: one Lean theorem
`iso3_not_rigid_single` exhibiting `φ`, proving its three hypotheses, and exhibiting one
realizable `G` with, for every `π τ`, the negation of each of the four disjuncts at `G`, each read
through a named invariant. Otherwise **`ISO3-UNDECIDED`** with the step named — and, when `ISO2`
did not classify, with the key hazard's frozen obstruction and no route run. **The optional lemma
`ISO3-L`** and **the product cell `ISO3-P`** are recorded in the same verdict commit under their
own names and enter no label; `ISO3-P` records `ISO3-P-UNDECIDED` with the frozen obstruction
unless a universal theorem at the product configuration is obtained.

### `ISO4` — the prefix-constrained corollary at the single carrier

**The statement.** With `Γ = fun _ => Γ₀`, `Γ₀ ≡ ¼`, `A = Fin 1`, `a₀ = (0 : Fin 1)`, for every
transition family `Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)`
satisfying the first seven conjuncts of `LadderConds` written out and the isometry proposition
`∀ t (G H), RealizableGram (Fin 1) (Γ t) G → RealizableGram (Fin 1) (Γ t) H → d (Φ t G) (Φ t H) = d
G H`: for every `t`, the four-shape conclusion for `φ := Φ t`.

**What settles it.** One Lean theorem at evidence level 2, `iso4_prefix_isometry_single`, whose
proof reads `PreservesAdmissible` into the first hypothesis of `ISO3`, `Reversible`'s second
conjunct into the second, the isometry proposition into the third, and applies `ISO3` at each
`t`. **`ISO4-CLASSIFIED` is earned only by that theorem**; `ISO4-UNDECIDED` with the step named
otherwise; `ISO4-NOT-EXECUTED` when the gate is closed. **The product cell `ISO4-P`**, with `L5`
added to the hypotheses at the product configuration, records `ISO4-P-NOT-EXECUTED` unless
`ISO3-P` was classified, and enters no label.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `ISO0` | **negative** — the record decides none of the four | **high** | Act 24 tested twelve named maps and recorded its rigidity attempt undecided at exactly the step this round freezes; no classification of realizable tuples beyond act 12's separation of two Hadamard classes exists on the record, and no isometry statement about any map outside act 24's list. The finding is whatever the bounded search records. |
| `ISO1` | **`ISO1-FAMILY-ACTS`** | **high** | Every conjunct is a coordinate identity, a reindexing, or two-sided phase bookkeeping from act 12's merged results. **UNDECIDED with the obstruction named is an allowed outcome.** `ISO1-R` is predicted `T-NEW` at **low** strength and enters no label. |
| `ISO2` | **`ISO2-CLASSIFIED`** | **medium** | The route is act 12's sufficiency, a dephasing, one algebraic identity and a case analysis over three rows with unit-modulus unknowns; every step is elementary, but the permutation bookkeeping is new kernel work and any case that does not reach the Fourier form ends the target. **UNDECIDED with the case named is an allowed outcome, and is the key hazard's trigger.** `ISO2-P` is predicted `UNDECIDED` at **high** strength. |
| `ISO3` | **`ISO3-UNDECIDED`** — the proposition's sign read as **positive**, the family being the whole isometry group | **medium** for the label; **low** for the sign | The route reaches the intrinsic metric and, if the optional lemma closes, an affine isometry of a finite-dimensional space preserving a finite union of circles; no route from there to the four-shape conclusion is in hand. `ISO3-L` is predicted `HOLDS` at **medium** strength and enters no label. **`ISO3-RIGID` is not expected; `ISO3-NOT-RIGID` is predicted for no candidate.** `ISO3-P` is predicted `UNDECIDED` at **high** strength. |
| `ISO4` | **`ISO4-NOT-EXECUTED`** | **medium**, following `ISO3` | The corollary is three hypotheses read into `ISO3`; it is executed only if `ISO3` reaches `RIGID`, and then predicted `CLASSIFIED` at **high** strength. `ISO4-P` is `NOT-EXECUTED` in advance. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
**UNDECIDED is a live preregistered outcome for every target and is not a failure, and
NOT-EXECUTED is a live preregistered outcome for every gated target and is not a failure.**

### The outcomes of `ISO0`

- **Outcome `ISO0`-silent:**
  > On the search this freeze bounds — act 12's, act 21's, act 23's and act 24's control planes,
  > amendments, result notes and modules, and `verification/ROADMAP.md`, against the frozen term
  > list — the merged record carries twelve isometry verdicts about named transition families, one
  > witness sending a class off every carrier relabelling's reach, and one recorded non-attainment
  > naming the classification of the isometries as what would settle it, and decides neither what
  > the realizable classes at either frozen configuration are, nor whether any map other than a
  > carrier relabelling or the entrywise conjugation is an isometry of the geometry, nor whether
  > every isometry of it is of any named form, nor whether any condition of act 21's ladder with
  > isometry forces membership in any named family. **The finding is that the record is silent on
  > the point.** It is not a finding that any such statement is false, not a finding that one is
  > unprovable, and not a bound on what a later round could prove.
- **Outcome `ISO0`-found:**
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which
  > objects. No merged artifact is edited, and no earlier round's recording is enlarged or corrected.

### The outcomes of `ISO1`

- **Outcome `ISO1-FAMILY-ACTS`:**
  > The finite family generated by the independent relabellings of fibres and of matrix indices,
  > the entrywise conjugation and the dilation transpose acts on the realizable classes at both
  > frozen configurations: each generator sends realizable tuples to realizable tuples, sends
  > equivalent tuples to equivalent tuples, and preserves act 24's distance on realizable tuples;
  > the transpose, defined through any admissible dilation of the tuple, is defined for every
  > realizable tuple and is the same class whichever dilation is taken; and every word in the
  > generators is, on realizable classes, one of four shapes — a relabelling, a relabelling
  > composed with conjugation, a relabelling composed with the transpose, or a relabelling composed
  > with both — at evidence level 2. **This is a statement about four named maps and the exact
  > quantity frozen**: it does not say the family is all of the isometries, does not say any
  > generator is a symmetry, an antiunitary map or a time reversal, and adopts nothing.
- **Outcome `ISO1-UNDECIDED`:**
  > Whether the four named generators act on the realizable classes at the frozen configurations,
  > and whether their words reduce to the four shapes, is undecided in this round, with the
  > obstruction named specifically — the generator, the conjunct, the step at which the proof
  > stopped, and what would settle it. Neither label is claimed, and the later targets of this round
  > were not executed.
- **Outcome `ISO1-R`, `T-REDUNDANT`:**
  > The dilation transpose agrees on every realizable class at the single-carrier configuration with
  > one named relabelling or one named relabelling composed with conjugation, at evidence level 2;
  > the family is unchanged by this, being frozen with all four generators.
- **Outcome `ISO1-R`, `T-NEW`:**
  > The dilation transpose agrees on every realizable class at the single-carrier configuration with
  > no relabelling and with no relabelling composed with conjugation: one exhibited realizable tuple
  > has a transpose class inequivalent to every one of those images, at evidence level 2, with the
  > separating invariant named. This says nothing about the transpose being a symmetry of anything.
- **Outcome `ISO1-R-UNDECIDED`:**
  > Whether the dilation transpose is generated by the relabellings and the conjugation on the
  > realizable classes is undecided in this round, with the step named; it enters no label.

### The outcomes of `ISO2`

- **Outcome `ISO2-CLASSIFIED`:**
  > At the single-carrier configuration every realizable tuple is equivalent, under act 12's phase
  > action, to an independent relabelling of act 23's Fourier tuple at a unit parameter, and every
  > such tuple is realizable, each direction proved separately at evidence level 2 from act 12's
  > merged sufficiency theorem, act 23's merged admissibility and elementary algebra, with nothing
  > imported. **This is a statement about the exact configuration frozen**: it says nothing at the
  > product configuration, nothing at any other visible family, nothing at `|A| > 1`, and does not
  > say the Fourier tuple is canonical or physical.
- **Outcome `ISO2-UNDECIDED`:**
  > Whether every realizable tuple at the single-carrier configuration is equivalent to a relabelled
  > Fourier tuple at a unit parameter is undecided in this round, with the obstruction named
  > specifically — the case of the analysis that did not reach the Fourier form, or the step at
  > which a fact would have had to be imported rather than derived, and what would settle it.
  > Neither label is claimed, no external classification was imported, no weaker domain was
  > substituted, and the classification of the isometries was not attempted.
- **Outcome `ISO2-NOT-EXECUTED`:**
  > The description of the realizable classes was not attempted, `ISO1` not having reached its
  > label; no sentence of this round reports anything about it.
- **Cell `ISO2-P`, `UNDECIDED`:**
  > What the realizable classes at the product configuration are is undecided in this round: the
  > freeze names no route, the realizable tuples there being the fibre-Gram data of `16 × 16`
  > unitaries with entries of modulus `¼` modulo phases on rows and on columns, and nothing is
  > imported to describe them. Neither a description nor its impossibility is claimed.
- **Cell `ISO2-P`, `CLASSIFIED`:**
  > At the product configuration every realizable tuple is equivalent to a member of an explicitly
  > described family and every member of it is realizable, each direction proved separately at
  > evidence level 2, with the family named and nothing imported.

### The outcomes of `ISO3`

- **Outcome `ISO3-RIGID`:**
  > Every surjective isometry of the normalized space at the single-carrier configuration — every
  > map on realizable tuples that preserves realizability, is surjective on classes and preserves
  > act 24's distance on realizable tuples — agrees on every realizable class with a member of the
  > finite family generated by the independent relabellings, the entrywise conjugation and the
  > dilation transpose, proved universally at evidence level 2, with no linearity, affinity,
  > continuity or dilation-level structure assumed of the isometry. **This is a statement about
  > the exact hypotheses at the exact configuration on the exact space frozen**: it does not say
  > any member of the family is unitary, antiunitary, a symmetry, a time reversal or quantum, says
  > nothing at the product configuration, and changes no verdict of any earlier act.
- **Outcome `ISO3-NOT-RIGID`:**
  > A surjective isometry of the normalized space at the single-carrier configuration lies outside
  > the finite family: an exhibited map preserves realizability, is surjective on classes and
  > preserves act 24's distance on realizable tuples, and sends one exhibited realizable class to
  > a class inequivalent to its image under every member of the family, at evidence level 2, with
  > the separating invariant named. **This settles the frozen family against the frozen
  > proposition and nothing in its neighbourhood**; the exhibited map is named by its formula and
  > is not called a symmetry, an antiunitary map, a time reversal or anything else.
- **Outcome `ISO3-UNDECIDED`, the route having been run:**
  > Whether every surjective isometry of the normalized space at the single-carrier configuration
  > belongs to the finite family is undecided in this round, with the obstruction named
  > specifically — the step of the route that did not close and what would settle it. Neither the
  > rigidity label nor its negation is claimed; no isometry outside the family is exhibited, and
  > the absence of a proof is not a counterexample.
- **Outcome `ISO3-UNDECIDED`, the gate having closed on the key hazard:**
  > Whether every surjective isometry of the normalized space at the single-carrier configuration
  > belongs to the finite family is undecided in this round, because the realizable image at the
  > configuration was not classified internally; no external classification was imported, no
  > weaker domain was substituted, and the route was not run. Neither label is claimed.
- **Outcome `ISO3-NOT-EXECUTED`:**
  > The classification of the isometries was not attempted, `ISO1` not having reached its label; no
  > sentence of this round reports anything about it.
- **Optional lemma `ISO3-L`, `HOLDS`:**
  > Every map satisfying the three hypotheses extends to an affine isometry of the real affine span
  > of the normalized space, at evidence level 2; this enters no label, and linearity is assumed of
  > no isometry anywhere in this round.
- **Optional lemma `ISO3-L`, `UNDECIDED`:**
  > Whether every map satisfying the three hypotheses extends to an affine isometry of the real
  > affine span of the normalized space is undecided in this round, with the step named; it enters
  > no label, and linearity is assumed of no isometry anywhere in this round.
- **Cell `ISO3-P`, `UNDECIDED`:**
  > Whether every surjective isometry of the normalized space at the product configuration belongs
  > to the finite family is undecided in this round, the realizable classes there not being
  > described and nothing being imported to describe them. Neither label is claimed.
- **Cell `ISO3-P`, `RIGID`:**
  > Every surjective isometry of the normalized space at the product configuration agrees on every
  > realizable class with a member of the finite family, proved universally at evidence level 2 over
  > a description of the classes derived internally and named; it enters no label.

### The outcomes of `ISO4`

- **Outcome `ISO4-CLASSIFIED`:**
  > At the single-carrier configuration, every transition family satisfying the conditions of act
  > 21's ladder before naturality and isometry of act 24's geometry on realizable tuples acts on
  > realizable classes, at every time, as a member of the finite family generated by the
  > independent relabellings, the entrywise conjugation and the dilation transpose, proved
  > universally at evidence level 2 through the classification of the isometries. **This is a
  > statement about the exact declarations at the exact configuration**: it does not say any
  > hypothesis is the right condition to impose, does not say the conclusion is unitary,
  > antiunitary, a symmetry or quantum, and changes no verdict of any earlier act.
- **Outcome `ISO4-UNDECIDED`:**
  > Whether the conditions of act 21's ladder before naturality and isometry of the geometry force
  > a transition family to act on realizable classes as a member of the finite family is undecided
  > in this round, with the step named; the classification of the isometries having closed, the
  > step is in the reading of act 21's rungs into its hypotheses. Neither label is claimed.
- **Outcome `ISO4-NOT-EXECUTED`:**
  > The corollary for transition families was not executed, the classification of the isometries
  > not having reached its rigidity label; no sentence of this round reports anything about it.
- **Cell `ISO4-P`, `NOT-EXECUTED`:**
  > The corollary at the product configuration, with factorization among its hypotheses, was not
  > executed, the isometries there not being classified; no sentence of this round reports anything
  > about it.

### The outcome-vector table — every admissible headline under the gate

The headline is one row of this table, verbatim, in this rendering: **Outcome vector:** followed by
the four labels in target order, separated by ` · `. Each row is admissible; the execution selects
the row its verdicts and the gate compose and reports no other wording. **There are six rows and
no others**; every other combination of labels is excluded by failure rule 3.

| # | vector |
| --- | --- |
| 1 | **Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-CLASSIFIED` · `ISO3-RIGID` · `ISO4-CLASSIFIED` |
| 2 | **Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-CLASSIFIED` · `ISO3-RIGID` · `ISO4-UNDECIDED` |
| 3 | **Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-CLASSIFIED` · `ISO3-NOT-RIGID` · `ISO4-NOT-EXECUTED` |
| 4 | **Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-CLASSIFIED` · `ISO3-UNDECIDED` · `ISO4-NOT-EXECUTED` |
| 5 | **Outcome vector:** `ISO1-FAMILY-ACTS` · `ISO2-UNDECIDED` · `ISO3-UNDECIDED` · `ISO4-NOT-EXECUTED` |
| 6 | **Outcome vector:** `ISO1-UNDECIDED` · `ISO2-NOT-EXECUTED` · `ISO3-NOT-EXECUTED` · `ISO4-NOT-EXECUTED` |

**The predicted row is row 4**; row 5 is the key hazard's row.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The execution appends,
after act 24's sentence in the same cell, exactly the sentence frozen for the vector reached.

**Case A — `ISO0` silent, row 4 with the cells as predicted.** This is the case the freeze predicts.

> Act 25 tests, in one gated round with four separately frozen targets, whether the finite family generated by the independent relabellings of fibres and of matrix indices, the entrywise conjugation and the dilation transpose acts on the realizable classes of act 24's geometry at act 12's and act 21's frozen configurations, whether every realizable class at the single-carrier configuration is the class of a relabelled Fourier tuple at a unit parameter, derived from act 12's sufficiency theorem alone, whether every surjective isometry of that normalized space belongs to the family, and whether every transition family satisfying the conditions before naturality and isometry acts on classes as a member of it. The family acts: each generator preserves realizability, descends to classes and is an isometry, and every word in the generators reduces to one of four shapes. Every realizable class at the single-carrier configuration is the class of a relabelled Fourier tuple at a unit parameter, and every such tuple is realizable, each direction proved separately and nothing imported. Whether every surjective isometry of the normalized space at that configuration belongs to the family is recorded undecided, with the step named; no isometry outside the family is exhibited, and the absence of a proof is not a counterexample. The corollary for transition families was not executed. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another beyond the consumptions the freeze places; no condition is adopted; the family and the normalized space are named objects of test and are not adopted as the physical ones; no generator is read as a symmetry, an antiunitary map or a time reversal; nothing is asserted at the product configuration beyond its recorded undecided cells, and nothing at any other configuration; acts 12 through 24's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

**Clauses of Case A vary with the outcome, and they vary independently within the gate**, each
replaced by the sentence its target's other outcomes fix:

| target or cell | clause | replacement |
| --- | --- | --- |
| `ISO1`, `UNDECIDED` | the sentence beginning "The family acts" and **every sentence after it up to** "Each verdict is" | "Whether the family acts on the realizable classes at the frozen configurations is recorded undecided, with the obstruction named, and the later targets were not executed." |
| `ISO2`, `UNDECIDED` | the sentence beginning "Every realizable class at the single-carrier configuration" and every sentence after it up to "Each verdict is" | "Whether every realizable class at the single-carrier configuration is the class of a relabelled Fourier tuple at a unit parameter is recorded undecided, with the case named; no external classification was imported and no weaker domain was substituted, so whether every surjective isometry of the normalized space belongs to the family is recorded undecided on that ground, its route not run, and the corollary for transition families was not executed." |
| `ISO3`, `RIGID` | the sentence beginning "Whether every surjective isometry" | "Every surjective isometry of the normalized space at that configuration belongs to the family, proved universally with no linearity, affinity or continuity assumed." |
| `ISO3`, `NOT-RIGID` | the same sentence, and the sentence "The corollary for transition families was not executed." kept | "A surjective isometry of the normalized space at that configuration lies outside the family: an exhibited map, named by its formula, preserves realizability, is surjective on classes and preserves the distance, and sends one exhibited class off every member's reach." |
| `ISO4`, `CLASSIFIED` | the sentence "The corollary for transition families was not executed." | "Every transition family satisfying the conditions before naturality and isometry acts on classes, at every time, as a member of the family, proved universally at that configuration." |
| `ISO4`, `UNDECIDED` | the same sentence | "Whether every transition family satisfying the conditions before naturality and isometry acts on classes as a member of the family is recorded undecided, with the step named." |
| `ISO2-P`, `CLASSIFIED` | the clause "nothing is asserted at the product configuration beyond its recorded undecided cells" | "at the product configuration the realizable classes are described internally and nothing else is asserted there" |
| `ISO3-P`, `RIGID` | the same clause | "at the product configuration the realizable classes are described internally and every surjective isometry there belongs to the family, and nothing else is asserted there" |

**The execution composes the sentence from these substitutions and reports no other wording. No
composition closes `P0`**, and none reports either of its two parts closed.

## Naming a map or a family is not endorsing it, FROZEN

Act 21's four points at its lines 1868–1879 govern here, read of the family, of each generator and
of the normalized space as well as of every law: naming is for testing; the round endorses none;
exclusion is only ever of the precise stated form; the lists are closed at this freeze.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a map's membership, a classification's success, or a family's
completeness could be read as its adoption**, each carriage opening with one line naming where it
is being carried. It is act 21's clause with "Act 21" read as "Act 25", and nothing else changed.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

**Read of the family and the classification**: an action verdict, a description verdict and a
classification verdict are statements about the frozen family and the frozen space; none adopts
the family as a symmetry group, a principle or a piece of physics, and "the isometries are the
family" is never written as "the symmetries are".

## What no outcome licenses

These are the forbidden sentences, in terms. None may be written in any artifact of this round, in
any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The isometry group is the Wigner group", "the conjugation is the antiunitary case", "the
   transpose is time reversal", "the relabellings are the unitaries", "Wigner's theorem holds on
   the orbit space", or any statement that any generator, the family, or any isometry is,
   resembles, approximates or points toward a quantum symmetry, an antiunitary map, a time
   reversal, unitarity or quantum evolution.** The conjugation is the entrywise `star`; the
   transpose is the matrix transpose of the dilation; each is named by its formula and as nothing
   else; the Wigner-type shape is provenance for the question's shape and for nothing else.
2. **"The family is the physical symmetry group", "the geometry is the physical geometry", "the
   isometries select".** The non-adoption clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
3. **"The classes are the complex Hadamard matrices of order four, by Haagerup", "the
   classification is known", or any attribution of `ISO2`'s theorem to the literature, or any use
   of that literature's classification as a step.** The description is derived here or it is
   `UNDECIDED`; the literature is provenance for the route and for nothing else.
4. **"`ISO3` follows from `ISO2`", "the corollary is immediate", or any inference of one target's
   verdict from another's**, beyond the consumptions the freeze itself places: `ISO2` in `ISO3`,
   `ISO3` in `ISO4`.
5. **"The family acts", "the classes are classified", "the isometries are the family", "the
   corollary holds", from the absence of a counterexample, from a route that failed to close, or
   from anything but the named route.**
6. **"The family is complete because no other isometry was found."** `ISO3-RIGID` is a universal
   theorem or it is nothing; searching and not finding earns `UNDECIDED`.
7. **"Act 24's rigidity cell `b` is now closed", "act 24's `b₀` witness is now accounted for as
   …", "act 21's `L-FAMILY` obstruction is removed", or any rewriting or reinterpretation of any
   earlier act's verdict, witness or obstruction.** They stand; this round's verdicts are about the
   family and the normalized space at the single-carrier configuration, and `b` is at the product
   configuration, which this round records undecided.
8. **"The transpose is a new symmetry of the record", "the record missed the transpose", read as a
   programme statement.** `ISO1-R`'s outcome is a fact about one relation and one family, and
   enters no label.
9. **"The isometry group of the orbit space is …"** stated of any space other than the normalized
   space at the single-carrier configuration, or of that space beyond the label earned; in
   particular nothing about the product configuration beyond the recorded undecided cells, and
   nothing about the whole tuple space or the whole feature image.
10. **"`d` is the natural metric", "the canonical metric", "the Fubini–Study metric", "the Bures
    metric", or any identification of act 24's geometry with a named geometry of any other
    theory.** Carried from act 24.
11. **"Every isometry is linear", "every isometry is affine", "by Mazur–Ulam", as a hypothesis or
    as an unproved step.** Affine extension is the optional lemma `ISO3-L`, proved in the kernel
    for this round's object if reached, entering no label; it is assumed nowhere.
12. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate; about act 16's cancellation cell; about act 14's carriers; about act 18's
    `D`-axis; about act 10's anchor axis; about Track I, Source B or Source C; or about the substratum
    Lemma 24.1 rounds.**
13. **"`P0` is closed", or "`P0`'s trajectory part is closed."**
14. **"Act 12's classification is strengthened", "act 24's geometry is superseded", "act 24's
    family is extended", "act 21's ladder is extended by a rung", "act 23's family is extended."**
    All are consumed at merged strength; the family and the normalized space are this round's
    objects of test and no rung; `ISO2`'s description is a theorem about act 12's realizable set
    and enlarges no merged statement.
15. **"The evolution is continuous", "smooth", "generated", "one-parameter", "composes in time"**,
    or any statement resting on structure the index type does not carry; in particular nothing
    about the parameter of the Fourier family being a time, a flow or a generator, and nothing
    about the rotations of the Fourier circle being a dynamics.
16. **"OI and QM are inequivalent."**
17. **"The generator list is exhaustive", "the family is the only natural family."** Four
    generators are tested; nothing outside them is refuted or endorsed here except as `ISO3`'s
    universal conclusion states, if earned.
18. **A single-label headline.** The headline is the vector, selected verbatim from the table.
19. **"The realizable classes at the product configuration are the `16 × 16` complex Hadamard
    matrices modulo equivalence, which are …"**, or any statement about them beyond the recorded
    obstruction: no description is imported and none is asserted.
20. **A verdict about a substituted domain reported as a verdict of this round**: the Fourier
    circle alone, a finite set of classes, the dephased matrices without the passage through act
    12's theorem, the whole tuple space, or the whole feature image, in the place of the realizable
    quotient. Such a statement, if proved, is an observation and earns no label.

## Named hazards

1. **The key hazard, restated as the round's own.** The description of the realizable classes is
   the step at which an external classification could enter, and the classification of the
   isometries cannot be earned without it. **If the description requires a theorem not derivable
   internally, `ISO2` is `UNDECIDED` with the case named, `ISO3` is `UNDECIDED` with the frozen
   obstruction "the realizable image at the configuration was not classified internally", its
   route is not run, no external classification is silently imported, and no weaker domain is
   substituted for the realizable quotient.** The gate's key-hazard rule and forbidden sentences
   3, 19 and 20 exist for this hazard, and the guard holds the result note to the obstruction
   sentence when row 5 is reached.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
2. **A family too small for the conclusion.** Act 24's rigidity conclusion named carrier
   relabellings and conjugation; the independent relabellings and the transpose are isometries
   that conclusion omits, and a classification with the smaller family would be refuted by them
   before any classification is attempted. The freeze names the four generators now; a fifth found
   during execution is an observation, and a surjective isometry outside the four is `ISO3`'s
   negative witness and nothing else.
3. **A generator whose formula is adjusted.** A relabelling with the permutation applied to only
   one matrix index, a conjugation applied to one fibre, a transpose taken of the tuple's fibres
   rather than of the dilation, or the transpose relation with the phase equivalence dropped is a
   different object; each generator's formula is pinned by the guard in every theorem that names
   it, and a variant is not a member of the family.
4. **The transpose read as a map on tuples.** It is a relation defined through a choice of
   dilation, total and single-valued on classes; a statement that picks one dilation and treats the
   result as a function on tuples has changed the object, and every statement quantifies over
   every dilation of the tuple.
5. **A definition.** The budget is zero; `R7-OGC` fails on any line beginning with a declaration
   keyword in the module at any commit from the module commit to `E`.
6. **Linearity assumed.** An isometry of the normalized space is a map on realizable tuples with
   three hypotheses; a statement that assumes it linear, affine, continuous, or induced by a map
   on dilations has changed the object. Affine extension is the optional lemma and enters no label.
7. **Compactness assumed.** No statement of this round uses compactness of the normalized space or
   the quotient topology; surjectivity is a hypothesis, and in the corollary it is `L3s` consumed.
   Act 24's `GEO1-T` stays undecided and is not reopened here.
8. **The Fourier circle mistaken for the space.** The rotations of the Fourier circle are
   isometries of that circle for its intrinsic metric; a proof that classifies the isometries of
   the circle has classified nothing about the normalized space, which is the union of the
   circle's relabellings, and a verdict about the circle alone is forbidden sentence 20.
9. **The whole tuple space or the whole feature image mistaken for the space.** The feature map is
   homogeneous of degree three on tuples and the ambient space's isometries are all the Euclidean
   ones; neither is the orbit space, and a verdict about either earns nothing.
10. **The product configuration answered by import.** The `16 × 16` case has no internal route in
    this freeze and no description is imported; `ISO2-P` and `ISO3-P` are `UNDECIDED` in advance
    unless a universal theorem is obtained internally, and a partial description is an observation.
11. **A witness for `ISO3` that fails a hypothesis.** A candidate isometry outside the family that is
    not surjective on classes, or not realizability-preserving, or not an isometry on all
    realizable tuples, earns nothing; the three hypotheses are proved in the kernel or the candidate
    is recorded and set aside.
12. **Inferring a target's verdict from another's.** Four theorems; `ISO3` consumes `ISO2` and `ISO4`
    consumes `ISO3` by the freeze's placement, and nothing else is inferred.
13. **A verdict revealed before its commit.** The attestation set at every boundary and the
    partial-fact rule exist for it; a lemma of the module commit that describes a realizable class
    as a relabelled Fourier class is a YES at the first boundary.
14. **A verdict commit carrying two targets.** One per executed target, in order.
15. **Executing a closed target "for information".** Failure rule 3; a closed target's route is not
    run, and a partial result on it is a discrepancy and not an observation — with the key hazard's
    form of the gate stated in terms: when `ISO2` does not classify, `ISO3`'s route is not run.
16. **Reading any generator as a symmetry, an antiunitary or a physical map.** Forbidden sentence
    1; each is its formula and nothing else is said of it.
17. **Choosing a configuration, a tuple or a permutation after an outcome is known.** Every target
    is at the single-carrier configuration named; `ISO1-R`'s finite check is at the tuple named; a
    witness for `ISO3` is recorded with the span in which it was found.
18. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.**
    Carried from acts 18 through 24; and here it is also the case that makes the transpose descend.
19. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
20. **A landing without `P`**, **a stem both declared and recorded**, **a legacy constant
    written**, **editing this freeze after an outcome is known**, **a supersession outside the
    table** — each as act 21's hazards 28, 30, 31 and 34 state them, with `OGC` for `OLT`; the
    table here is empty, so any edit to a closed round's guard is a supersession outside it.
21. **A `B`-scoped precondition that the freeze's own text falsifies.** Every `B`-scoped row below
    is evaluated at `M` before the merge and is written so that the presence of this file in the
    tree does not fail it.
22. **A value in the freeze's reading that the kernel computes differently.** Recorded as a
    discrepancy of the reading; the label is earned by what the kernel proves and by nothing stated
    here — in particular the dephasing phases, the case analysis's orthogonality equations and the
    transpose's coordinate identity.

## Non-doings

The round does not: **derive, recognise, approach or claim progress toward quantum evolution**, in
any paraphrase; adopt any map, the family or the normalized space as a symmetry, a selector, a
principle or the physical geometry, or identify any of them with any named object of any other
theory; read the conjugation as antiunitary, the transpose as time reversal, or the relabellings
as unitaries; attribute any theorem of this round to the literature it cites as provenance, or
consume any theorem of that literature; import any classification of complex Hadamard matrices of
any order; substitute any domain for the realizable quotient; assert anything about the realizable
classes at the product configuration beyond the recorded undecided cells, or at any `|A| > 1`, or
at any visible family other than the frozen two; assume linearity, affinity, continuity or
compactness of anything; adopt a carrier as the physical one or define a carrier of its own;
endorse any condition, any law, the family or the geometry; assert or deny that a cross-time law
is required or suffices; **restate, edit, add or remove any rung, or change any conjunction**;
**introduce or widen an equivalence**, or use one outside the frozen quotient list in any verdict;
**define anything**; add or remove a generator; test any configuration outside the frozen two, or
any decomposition other than `e = Equiv.refl`; infer any target's verdict from another's beyond the
consumptions the freeze places; report an independence of conditions; attempt a census of the
ladder or a same-initial-orbit pair; **re-prove or strengthen acts 12, 13, 17, 18, 20, 21, 22, 23
or 24**; revise any merged label; rewrite, reinterpret or grade any verdict, witness or obstruction
of any earlier act's note; reopen act 24's `GEO1-T`, its cell `b` or its cell `a2`, `a4`; ask the
threading question or the cross-time representative question, in either direction; touch act 16's
cancellation cell; state anything about act 18's `D`-axis, act 10's anchor axis, act 14's carriers,
Track I, Source B or Source C, or the substratum Lemma 24.1 rounds; realize any map as an operator,
unitary, antiunitary, generator or group element; **introduce continuity, smoothness, composition
in time, a semigroup law or a generated evolution**; alter any existing manifest record, supersede
any closed round's contract, or write a legacy seal constant; edit any manuscript; close `P0` or
either of its parts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Act 21's statement at its lines 2130–2143 is carried in full: the question is not asked, not
bounded and not attempted; an execution that begins asking whether the family looks like a
symmetry group of quantum mechanics, or whether any generator looks like an antiunitary symmetry,
has left the round's scope, and what it finds is recorded as an observation and not executed.
**"Resembles", "is consistent with", "is what one would expect from" and "is a step toward" are
forbidden sentences.** The word "Wigner" appears in this file only in the external-provenance
section, the forbidden list and `ISO0`'s term list, and appears in no other artifact of the round.

### What act 25 does and does not change about `P0`, and about act 24's cells

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 25 can
change is the recorded content of one finite family of maps on the per-slice orbit space, the
recorded description of the realizable classes at the single-carrier configuration, the recorded
status of the classification of the isometries of act 24's geometry there, and the recorded status
of one corollary for transition families there.

**On act 24's undecided cells, stated once and narrowly.** Act 24's cell `b` is at the product
configuration and asks for a relabelling or a relabelling composed with conjugation; this round's
classification, if earned, is at the single-carrier configuration and names a larger family. **No
outcome of this round closes act 24's `b`, `a2` or `a4`**; what a positive `ISO3` would supply is
an observation for a later round that freezes the product configuration's description, stated
once in the result note and not executed here.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about
what fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT
CERTIFIED**.

## Definition budget

**The execution introduces ZERO top-level Lean definitions.** The budget is **zero**, and it is
stated as a number so that it cannot drift: no `def`, `abbrev`, `structure`, `class`, `instance`,
`axiom` or `opaque`. The invariant family is act 24's one definition consumed; the normalized
space, the four generators, the transpose relation, the four-shape conclusion, the isometry
proposition, every rung as act 21's declaration consumed, act 23's Fourier matrix and the
permutations are bound variables or written-out propositions in the statements that need them, as
`lc2_regularity_law` pins its pseudometric, as `phiCTRL_census` pins its transition family and as
act 24 pins its geometry. The prefix through `L4d` is written out as the first seven conjuncts of
`LadderConds` wherever a statement needs it, and never abbreviated by a definition. **A definition
requires its own append-only amendment**, separately frozen and merged before the work it affects.

Theorems are not budgeted. The execution proves whatever lemmas its verdicts need — the three
coordinate identities, the reindexing with two permutations, the row-phase lemma, the transpose's
admissibility, the unit-modulus identity and the antipodal lemma, the dephasing lemma, the
monomial coordinates of the Fourier tuple, the case lemmas, the action facts, the description, the
classification or its recorded non-attainment, the corollary — as named results, each printed in
the axiom table.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `ISO1`, `ISO2`, `ISO3` and `ISO4`, whichever label
each reaches other than `UNDECIDED` or `NOT-EXECUTED`. `decide` over finite index types is
permitted; `native_decide` is not, and neither is `sorry`. `Classical.choice` is expected wherever
`sh1_sufficiency`, `Real.sqrt`, the transpose relation's totality or the classical branch of a
statement is used. **`ISO0` is type P and carries no evidence level.**

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-OGC`**, reserved here and created by the execution pull request.
The round's stem is **`OGC`**; its seal state is the prospective declaration during execution and
the record `verification/seals/OGC.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 25 object enters the repository tree** — any Lean statement about the
   family, any generator, the transpose relation, the normalized space, the description of the
   classes, any isometry of the normalized space, the corollary, or any cell; any probe clause;
   any result artifact; any manifest record or declaration for `OGC`. **The single permitted
   exception is the analysis recorded inside this control-plane blob itself**, merged *as* the
   freeze, including the proof routes and the chronology simulation.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'OGC': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('OGC',)}`, both outside the validator's marker-bounded regions, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('OGC', tag='R7-OGC')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed — the validator's `EXECUTION` classification.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `OGC` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/OGC.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `OGC` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `OGC` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `OGC`.
9. **No `_OGC_BASE`, `_OGC_SEALED_HEAD` or `_OGC_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-OGC`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains no
    line beginning with `def `, `abbrev `, `structure `, `class `, `instance `, `axiom ` or
    `opaque `; (b) the module imports `OIBridge.OrbitGeometrySelector`; (c) the geometry is
    pinned, in every theorem that names `d`, to act 24's equation, each generator is written, in
    every theorem that names it, by its frozen formula, and the transpose relation by its frozen
    form; (d) the stage-A commit, the module commit and the verdict commits of the executed targets
    are on the first-parent chain from `B` to `E`, in that order, the module absent before the
    module commit and present from it on, and the module commit carrying no theorem whose name is
    a verdict name; (e) each verdict theorem first appears at its own verdict commit and at no
    earlier commit; (f) the gate: a verdict commit for `ISO2`, `ISO3` or `ISO4` exists only if the
    result note carries the opening label for the target before it, and a run of `ISO3`'s route
    exists only if `ISO2` reached `ISO2-CLASSIFIED`. A definition inserted into the module text, a
    synthetic edit to the geometry's equation or to a generator's formula, a verdict theorem
    inserted into the module commit's text, a fabricated SHA off the chain and an `ISO3` route
    theorem present without `ISO2`'s label each **fail** the control.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table with **no definition**
    and the eight records; the **five** attestation answers, one per span; the sentence that no rung
    was restated, no equivalence was widened, no generator was added or removed, no domain was
    substituted and nothing was imported; each target's label carried with its frozen sentence
    verbatim; the cells `ISO2-P`, `ISO3-P`, `ISO4-P` and the observation sub-questions `ISO1-R`,
    `ISO3-L` each with its label and frozen sentence; **the outcome vector, equal verbatim to one
    of the six rows of the table**; **the gate record**, with the key hazard's rule reported as
    applied or not; **the statement that no verdict was inferred from another beyond the
    consumptions the freeze places**; **the statement that no generator is read as a symmetry, an
    antiunitary map or a time reversal**; **the statement that no theorem is attributed to the
    literature, no classification is imported and no weaker domain is substituted**; **the
    statement that every earlier act's historical verdicts stand unchanged**; the
    route-authorization matrix reported as honoured; THE CLAUSE carried complete at every mention
    with its count; and the frozen `P0` sentence for the case reached present in
    `verification/ROADMAP.md` verbatim, after act 24's.

### The contracts this round supersedes, named in advance — none

**Under `§A.37`'s closed-round rule, `AGENTS.md` lines 1055–1061, a closed round's contract that
reads the current round's declaration would be superseded here. The measurement recorded above
found none**: at `D` every closed round's guard reads its own record, and the placeholder
declaration failed nothing. **The execution edits no contract of any closed round.** Should the
execution find that a closed round's contract fails on an act 25 head for a reason that has nothing
to do with act 25's result, that is a discrepancy recorded in the result note, and the disposition
is an append-only amendment to this freeze, separately merged, and not an edit made during
execution.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-OGC' D`, `git grep -l -- '_OGC' D`, `git grep -l -- 'OGC' D`, `git grep -l -- 'OrbitGeometryIsometries' D`, `git grep -l -- 'orbit-geometry-isometries' D`, `git grep -l -- 'act-25' D`, `git grep -l -- 'ISO1' D` and `git grep -l -- 'iso1_' D` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f`, twenty-nine records, twenty-three `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green and carries no legacy constant | eighty-eight `R7-*` tags, all `PASS`, on main-push run 35467053564; `_SI2_LEGACY_RE` finds zero assignment statements |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each of the first twenty-six paths of the start-state table has at `B` the blob the table names (the `frozen-blob` lines of the block) |
| 6 | `B` | No act 25 execution object exists | the guard file at `B` contains no `R7-OGC` and no `_OGC`; no `verification/seals/OGC.json`; no `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Acts 23 and 24 are sealed at `B` | `verification/seals/OLG.json` at `B` carries `round` `OLG`, `kind` `sealed`, `base` `64214bfb0ae41b9f0a4fb11159089fff32d4dd85`, `sealed_head` `6b9f2e5e765dff3965512ee31a646a22a08e75d2`, `merge` `61c98efc44146ee3bd3650138d8b5ebcc7e1b8b7`; `verification/seals/OGS.json` at `B` carries `round` `OGS`, `kind` `sealed`, `base` `d0fcdbc03c4b828d630f677253cf0914f451b63d`, `sealed_head` `ae7a319b9acfb97843c4a6cfa7cbc24a381be32b`, `merge` `995ad859d0dca20bb76273e5dc4035ed765cb239`; the guard file at `B` carries the `R7-OLG` and `R7-OGS` checks |
| 9 | `B` | Act 24's module is wired | `OIBridge.lean` at `B` imports `OIBridge.OrbitGeometrySelector` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/preregistration.md` exists at `B`; its blob is the one the `R7-OGC` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are not inputs. **The claim is scoped to the repository record.**

```control-plane-preconditions
d: 17272da24e8d65a8d0e2417c6a451a1af3461258
merged: false
frozen-blob: verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean ce9d1aa05dfdedfb5cac171cfe6379681942195f
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean 860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean d41b157a3f38d4ebedbe11ad9682a8693836a383
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawGaps.lean 5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1
frozen-blob: verification/lean-mathlib/OIBridge/TwoSidedGauge.lean 4bba2040c33424fafbc6d31c0d63b86dff33691a
frozen-blob: verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean 8d17177799327d648bbbd001cf237e1ac37bd3fc
frozen-blob: verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean cb14c43b0becfe1a379ae3615d5553723ede9163
frozen-blob: verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean afc22cfc93b244c80e1c55a273dcfda1ddebb121
frozen-blob: verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean 4c1137f35600320b9273c857ec62271341b05cd0
frozen-blob: verification/lean-mathlib/OIBridge/DilationChoice.lean 7e3a8222cedf530f3c109662e7174d72b6358063
frozen-blob: verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md 3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a
frozen-blob: verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md a2719d5f63c4ce517590ec7fbe8e61bafe04c3a7
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md 93c06674792fa3565f6f94e5e954e484dca33cf2
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md 174e790d2cc5c663f9f54ae7daaeca90b51f96e1
frozen-blob: verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md 467d8be147b6ebd91f2eed12404566af74ac779f
frozen-blob: verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md 2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a
frozen-blob: verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md 14a2cd8c54946bf0078329402e6f853107b31d9d
frozen-blob: verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md 6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db
frozen-blob: verification/seals/OGS.json 5436e01852e9999483dd4aff9f605e47575b7415
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/seals/OLN.json 1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb
frozen-blob: verification/seals/OLG.json 8a058df23c07e2b7571672c039a5a7b4f911a339
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-OGC' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_OGC' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'OGC' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'OrbitGeometryIsometries' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'orbit-geometry-isometries' $D", "expect": "empty"}
{"id": "d1-act-free", "scope": "D", "check": "git grep -l -- 'act-25' $D", "expect": "empty"}
{"id": "d1-target-free", "scope": "D", "check": "git grep -l -- 'ISO1' $D", "expect": "empty"}
{"id": "d1-theorem-prefix-free", "scope": "D", "check": "git grep -l -- 'iso1_' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = ffb92daab9ea2f3d64c47b9c73e4b9c3466b763f", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals, the modules and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-OGC' -e '_OGC'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'OGC.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'OrbitGeometryIsometries'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: acts 23 and 24 sealed
{"id": "b8-olg-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLG.json | tr -d ' \\n' | grep -e '\"round\":\"OLG\",\"kind\":\"sealed\",\"base\":\"64214bfb0ae41b9f0a4fb11159089fff32d4dd85\",\"sealed_head\":\"6b9f2e5e765dff3965512ee31a646a22a08e75d2\",\"merge\":\"61c98efc44146ee3bd3650138d8b5ebcc7e1b8b7\"'", "expect": "nonempty"}
{"id": "b8-ogs-sealed", "scope": "B", "check": "git show $REF:verification/seals/OGS.json | tr -d ' \\n' | grep -e '\"round\":\"OGS\",\"kind\":\"sealed\",\"base\":\"d0fcdbc03c4b828d630f677253cf0914f451b63d\",\"sealed_head\":\"ae7a319b9acfb97843c4a6cfa7cbc24a381be32b\",\"merge\":\"995ad859d0dca20bb76273e5dc4035ed765cb239\"'", "expect": "nonempty"}
{"id": "b8-olg-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLG'\"", "expect": "nonempty"}
{"id": "b8-ogs-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OGS'\"", "expect": "nonempty"}
# row 9: act 24's module wired
{"id": "b9-import-ogs", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitGeometrySelector$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/preregistration.md", "expect": "exit0"}
```

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**, and the path this file sits at is pinned with it.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect, each repeating the `M`-then-`B` certification and
  each moving `B` to its own certified merge.
- **This pull request carries this file alone.**
- **The execution branches from `B` and from nothing else**, only after `B`'s main-push
  certification is fully green, and **its first act is to verify that the preregistration at `B`
  carries the blob this freeze names**, recorded in the result note.
- **The stage-A commit comes first**, then **the module commit** with the shared lemmas, no
  definition and no verdict, then **the verdict commits of the executed targets in the order
  `ISO1`, `ISO2`, `ISO3`, `ISO4`**, one per executed target, the gate read between each; their SHAs
  are recorded, and the attestation set is answered for each of the five spans.
- **Then exactly one execution pull request**, based on `B`, carrying the Lean module, the result
  note, the `R7-OGC` guard clause, the two declarations, the `ROADMAP` propagation and the census
  entry. **No manuscript changes. No edit to any closed round's guard.**
- **Before certification the execution never absorbs later `main`.** The certification of record is
  the run whose `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory and pin-only. Landing conflicts are resolved **in `L`, never in `E`**, by merits. Full
  continuous integration must pass again on `P` before the pull request merges, and the resulting
  `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing under the manifest protocol, `E` → `L` → `P`, the
   declarations as set, the record `P` writes named field by field, no existing manifest record
   altered, no closed round's contract edited, no legacy constant written, and the base-blob
   verification recorded;
2. **the ordering obligation's eight records** and the attestation set's **five** answers, one per
   span, with the freeze-supplied facts listed;
3. **`ISO0`** — the bounded search, recorded in full, act 24's twelve verdicts, its `b₀` witness and
   its `b` obstruction recorded as found and as deciding nothing;
4. **`ISO1`** — the label with its frozen sentence, the theorem named, the conjuncts each reported
   separately, the transpose's totality, single-valuedness and descent reported apart from its
   isometry, the six relations reported, the accounting act 24 asked for reported as a control,
   `ISO1-R` recorded with its outcome, and **the statement that no generator is read as a symmetry,
   an antiunitary map or a time reversal**;
5. **`ISO2`** — the label with its frozen sentence, the theorem named, the two directions reported
   apart, the case analysis's cases each named with the step that closed it, **the statement that
   every step was derived from the pinned blobs and nothing was imported**, and `ISO2-P` recorded
   with its outcome and obstruction;
6. **`ISO3`** — the label with its frozen sentence, the theorem named or the step of the route not
   reached, the three hypotheses reported as the whole of what was assumed, **the statement that no
   linearity, affinity, continuity or compactness was assumed**, `ISO3-L` and `ISO3-P` recorded
   with their outcomes, and, when the key hazard's rule applied, the statement that the route was
   not run;
7. **`ISO4`** — the label with its frozen sentence, the theorem named or the gate's closure, the
   reading of `L1`, `L3s` and isometry into `ISO3`'s hypotheses reported, and `ISO4-P` recorded;
8. **the outcome vector**, one of the six rows verbatim, **the gate record**, and **the statement
   that no verdict was inferred from another beyond the consumptions the freeze places**;
9. **the route-authorization matrix as honoured**: each construction used for its own target and
   nothing else, no alternative substituted;
10. **the scope boundary as honoured**: nothing derives, recognises or approaches quantum
    evolution; no continuity, composition or generator; no theorem attributed to the literature,
    none of its theorems consumed, no classification imported, no domain substituted; every earlier
    act's verdicts untouched, act 24's undecided cells not closed; the threading, act 16's cell, act
    18's `D`-axis, act 10's anchor axis and act 14's carriers untouched;
11. **the non-adoption clause carried verbatim at each mention**, with the count of carriages, and
    the sentence that the family and the normalized space are adopted as nothing;
12. the frozen `P0` sentence for the case reached, appended after act 24's, the row's label
    unchanged;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 12, 13, 17, 18, 20, 21, 22, 23 and 24 — every merged label consumed, none
    revised;
15. the definition count against the budget of zero;
16. the chronology certification, naming the property certified, the ten preconditions with their
    scopes and the block's rows as the base check reported them at `M` and at `B`, the validator's
    classification of `OGC` at `E`, `L` and `P`, the empty supersession table reported as
    honoured, and `SI-3`'s standing contract reported as holding;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired — including any value or step of the
    freeze's reading the kernel computed differently;
19. the observation, if any, for a later round on the product configuration, stated once and
    narrowly as the non-doings section fixes it, and the observations the anti-expansion rule
    collected.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Every item below is a call
already made**, and the body of this freeze is written to them throughout. **This freeze carries no
open decision.**

1. **The round is a gated round, the orbit-geometry isometries**: the normalized space and the
   family that acts on it first, the internal description of the realizable classes at the single
   carrier second, the classification of the surjective isometries third and only then, the
   prefix-constrained corollary last and only then; act 12's equivalence, act 21's ladder and
   configurations, and act 24's invariant family and geometry consumed unchanged; every earlier
   act's verdicts consumed as landed and not rewritten.
2. **The object is the normalized realizable quotient and not the whole tuple space or the whole
   feature image**: the realizable tuples modulo act 12's equivalence, carried onto the feature
   image by act 24's separation theorem and by that theorem only; the feature map's homogeneity is
   the recorded reason the whole tuple space is not the object.
3. **The family is generated by four generators — the independent relabellings of fibres and of
   matrix indices, the entrywise conjugation and the dilation transpose — with a four-shape normal
   form**, each generator bound by its formula, the transpose by its relation; act 24's carrier
   relabelling is the diagonal case; whether the transpose is generated by the others is the
   observation sub-question `ISO1-R` and enters no label.
4. **The key hazard is stated first and made mechanical**: the description of the realizable
   classes is its own gated target; if it cannot be derived internally the classification returns
   `UNDECIDED` with the frozen obstruction, its route not run, nothing imported and no weaker
   domain substituted; the complex-Hadamard literature is provenance for the route and for no
   theorem.
5. **The classification's hypotheses are three and no more** — realizability preserved,
   surjectivity on classes, isometry on realizable tuples — with descent derived and not assumed;
   **no linearity, affinity, continuity or compactness is assumed anywhere**; extension to the
   affine span is the optional lemma `ISO3-L`, earned or absent, entering no label; act 24's
   `GEO1-T` is not reopened.
6. **Each target has its own proposition, route, verdict rule and failure interpretation**, and the
   three-way discipline — a universal proof for a positive label, an exhibited isometry outside the
   family for `ISO3`'s negative label and for no other, otherwise `UNDECIDED` — governs each; the
   `ISO3` witness, if any, is found in execution, recorded with its span, and admissible for `ISO3`
   alone.
7. **The three safeguards and the three failure rules are this round's freeze rules and not
   `AGENTS.md` rules**: the fixed order with one verdict commit per executed target and the
   attestation set at every boundary; the route-authorization matrix; the outcome-vector table of
   six rows from which the headline is selected verbatim; a universal theorem not obtained is
   `UNDECIDED`; a route failing its reading is recorded and not repaired; the gate closes forward
   and never reopens, with the key hazard's form of it.
8. **The scope is the two frozen `Fin 4` configurations and no other**: the single-carrier
   configuration is primary and every label is earned there; the product configuration carries
   the recorded cells `ISO2-P`, `ISO3-P`, `ISO4-P`, undecided or not executed in advance, entering
   no label; nothing is asserted at `|A| > 1` or at any other visible family.
9. **The branch interpretation is forbidden**: no generator, no member of the family and no
   isometry is read as a symmetry operation of quantum mechanics, an antiunitary map, a time
   reversal or a quantum-dynamical object; the conjugation is the entrywise `star` and the transpose is the
   matrix transpose of the dilation, and each is named by its formula and as nothing else.
10. **No drafting-time outcome check was run**; the analyses are the freeze's reading; the one
    simulation run concerns chronology only and found no supersession needed.
11. **`§A.37`'s `D`/`B`/`M` vocabulary governs**: scoped precondition rows, mode `M` validation of
    the candidate merge before the merge, `B` reserved for the certified control-plane merge.
12. **SEALING**, under the manifest protocol: stem `OGC`, tag `R7-OGC`, `E` → `L` → `P` with `P`
    mandatory, the prospective declaration during execution and the record from `P`; no
    supersession; nothing in any closed round's guard touched.
13. **The definition budget is zero.** Act 12's, act 21's, act 23's and act 24's declarations are
    consumed and none is restated; the normalized space, the generators, the transpose relation,
    the four-shape conclusion and the isometry proposition are bound by equation or written out.
14. **Acts 12, 13, 17, 18, 20, 21, 22, 23 and 24 are consumed at merged strength**: not re-proved,
    not strengthened, not redefined; act 24's undecided cells are not closed by anything here.
15. **Continuity, composition in time, generators, the threading, the product configuration's
    description, any `|A| > 1`, and any comparison with quantum evolution or quantum symmetry are
    out of this round**, each a separate question for a separate freeze.
