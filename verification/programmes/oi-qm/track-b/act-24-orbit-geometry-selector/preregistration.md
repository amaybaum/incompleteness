# Track B act 24 — the orbit-geometry selector audit: complete phase invariants on the per-slice orbit space, the geometry they induce, its controls, the record's laws against it, and a gated rigidity attempt: CONTROL PLANE

Owner-called. This file is the whole of act 24's control plane and is merged **alone**, before any
execution object exists. It is a **gated round**: four targets frozen together, each with its own
preregistered proposition, its own verdict rule and its own failure interpretation, executed in a
fixed order in which **each later target is executed only if the earlier ones reach the label the
gate names** — a complete family of phase invariants and the geometry it induces first, its
controls second, the record's laws against it third, and a rigidity implication last and only then.
It re-opens nothing of acts 21, 22 or 23, changes no rung, adds no rung to act 21's ladder, widens
no equivalence, and adopts nothing: the invariant family it freezes is a **named object of test**,
written from the Gram data alone, and every verdict is about that named object at the
configurations frozen for it.

It is **not** a re-run of any earlier act, **not** a census of act 21's ladder, **not** an attempt to
characterize the surviving class or the isometries, **not** a statement about continuity,
composition in time or a generator, **not** a statement about the threading, and **not** an attempt
to derive or to recognise quantum evolution, which stays an explicit non-doing.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The commit vocabulary this freeze uses, fixed first

`AGENTS.md` `§A.37`, at the drafting snapshot, **lines 713–729**, gives a control plane three commit
names, and this file uses them in exactly that sense:

- **`D`, the drafting snapshot** — `9907d3acefb2bd5e2cc66c007400cc0e194d36ec`, certified `main` at
  the landing of act 23 (#687), whose main-push run 35451692651 is fully green with the
  control-plane base check in mode `B`. Every measurement below — every locating coordinate, every
  pinned blob, every name-freedom check and the chronology simulation — was made at `D`, and is a
  statement about `D`. **`D` is never the execution base.**
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
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'OGS': B}` | **declared**; the validator classifies `OGS` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OGS',)}`, in the same file | the seals tree at `B`, read from git, plus the one addition this freeze authorizes, by stem | unchanged; `OGS.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/OGS.json` | **absent** | **written by `P`**: `{"round": "OGS", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `OGS` as `ARCHIVED` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
writes `OGS.json` and removes the `OGS` entry from the prospective declaration, and touches nothing
else. Without `P` the round sits at `LANDED-PENDING-PIN`, permitted at `L` itself, and every head
descending from that unpinned landing fails as *seal pending*.

**No legacy seal constant is written, at any commit of the round.** Nothing matching
`_OGS_(BASE|SEALED_HEAD|MERGE)` exists at any commit, `SI-3`'s standing contract holds at every
head, and the execution's guard clause certifies chronology through one keyed call,
`_si2_authority('OGS', tag='R7-OGS')`, and never through a per-round constant.

### The lifecycle derivation, and why it comes out SEALING

The rule the owner set for act 19 and act 21 is carried: a round is sealing **if and only if** its
execution creates a new formal object whose chronology matters to the result.

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the one budgeted definition, the invariant family's separation and the induced
   metric's properties, the three controls, the twelve per-law isometry verdicts and the rigidity
   cells.
2. **Their chronology is load-bearing.** The round's claim is that its invariant family, its
   geometry, its controls, its closed law list, its gate, its execution order and its proof routes
   were frozen — here, in this file — before any kernel work, and that no law was added, no
   coordinate of the invariant family adjusted and no rung restated to reach any verdict; a
   validator-certified ancestry rooted at this control plane's merge commit is what makes that
   checkable.
3. **A new module with new named results is new seal state**, which only a sealing round's `P` may
   record.

**Therefore act 24 is SEALING, and it owns no other seal state.**

### The tag, the stem, the module, the definition and the round directory are free at `D`

At `D`:

- `git grep -l -- 'R7-OGS'` returns nothing anywhere in the tree, and the tag is absent from the
  **eighty-seven** `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries at `D`.
- `git grep -l -- 'OGS'` returns nothing anywhere in the tree — the bare three-letter form occurs in
  no text file and in no binary artifact, as a word or as a substring — so a bare-stem search for it
  is unambiguous, and `git grep -l -- '_OGS'` returns nothing.
- No record `verification/seals/OGS.json` exists; the twenty-eight records at `D` use the stems
  `A12P`, `A6D`, `A6I`, `A6P`, `ABR`, `CLG`, `CTI`, `HYA`, `HYB`, `HYE`, `OLG`, `OLN`, `OLT`, `PC4`,
  `PC4S`, `PQT`, `RBR`, `RNC`, `RNT`, `SGT`, `SI1`, `SI2`, `SI3`, `TCF`, `TRJ`, `TSG`, `WTS` and
  `XTS`, and no substring search for `OGS` reaches any of them.
- **The alternative was checked before `OGS` was chosen**, and the check is recorded so that the
  choice is not re-litigated. `OQG` (orbit quotient geometry) was the first choice and was rejected:
  `git grep -l -- 'OQG'` matches one binary artifact at `D`, the book's PDF, so a bare-stem search
  for it would not be unambiguous. `OGS` — orbit-geometry selector, the object this round tests —
  matches nothing and was chosen. `OLT`, `OLN` and `OLG` are acts 21's, 22's and 23's, excluded on
  that ground alone.
- **The one budgeted definition's name is free.** `git grep -l -- 'mixedTriple'`,
  `git grep -l -- 'MixedTriple'` and `git grep -l -- 'mixed_triple'` each return nothing.

**The round directory and the module name are free at `D` too.** `git grep -l -- 'act-24'`,
`git grep -l -- 'orbit-geometry-selector'` and `git grep -l -- 'OrbitGeometrySelector'` return
nothing. The round directory is
`verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/` and the module is
`verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean`.

### What this round does NOT own, named exhaustively

It alters **no existing manifest record**. The twenty-eight records under `verification/seals/` at
`D` — the seals tree `9f762b8d0b5656950e5030c4eb9ca6514362cce0`, twenty-two `sealed` and six
`base-only` — are **read and never written**; the one addition this freeze authorizes is `OGS`. It
writes **no legacy constant**. It does not re-pin, re-derive or re-declare any other round's seal:
`OLT.json`, `OLN.json`, `OLG.json` and the rest belong to the rounds that set them. Inside the guard
file the execution **adds** the `R7-OGS` clause and **sets** the two stem-free declarations named
above — and changes nothing else in the file. **No contract of any closed round is superseded**,
and the measurement that none needs to be is recorded in the chronology section.

## Provenance — what this freeze carries from acts 12 through 23, from the literature, and what is its own

**The rule.** Act 24 consumes act 12's slice equivalence and realizable set, act 21's ladder and
configurations, and the transition families of acts 21, 22 and 23 with their verdicts exactly as
landed, **unchanged**, and adds one invariant family with its one definition, one induced geometry,
one twelfth transition family, four targets, a gate and its own lifecycle. Every rung is the
declaration act 21's merged module carries, pinned by blob at `B`; **no rung is restated in this
round's module**, and a restatement would be a defect of the round. The geometry is bound by
equation in every theorem that names it; the invariant family is the one definition the budget
admits.

| source (frozen blob, line range) | this file | status |
| --- | --- | --- |
| act 12's `GramPhaseEquiv`, `RealizableGram`, `FibreGram`, `TwoSidedGauge.lean` `4bba2040…` lines 95–110 | the quotient the invariants separate; the realizable set every isometry statement quantifies over | **consumed unrestated** |
| act 12's `gramPhaseEquiv_cross_invariant`, line 870, and `sh1_sufficiency`, line 1070 | the cross-invariant, a coordinate of the invariant family up to the diagonal; the full-support fact at the frozen configurations | **consumed** |
| act 12's two-sided gauge, `LeftFibreGroup` line 78, act 13's `WeakAnchorStabilizer` (`CoherentLiftGauge.lean` `8d171777…` line 114), `fibreGram_left_mul` line 207, `fibreGram_mul_weak_apply` line 242 | the second control | **consumed** |
| act 17's `GramTrajEquiv` and the three equivalence lemmas, `GramTrajectorySelection.lean` `afc22cfc…` lines 121 and 141–170 | the equivalence-relation facts every invariance statement uses | **consumed** |
| act 18's `ProperAt`, `PropagatesFrom` (`IntermediateCrossTimeStructure.lean` `cb14c43b…` lines 167–171, 186–193) and `lc2_regularity_law`, line 729 | the standing hypotheses; the pseudometric this round's geometry is measured against and does not reuse | **consumed; the pseudometric not reused** |
| act 20's `RelabelTransition`, `RepresentativeNaturality.lean` `4c1137f3…` line 167 | the first control and five of the record's laws | **consumed unrestated** |
| act 21's ladder `L0`–`L5`, `OrbitLawRigidityTwisted.lean` `860daac4…` lines 96–196 | consumed as `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds` and the inline `L2`, `L4d`, `L4n` | **consumed unrestated** |
| act 21's two configurations, its freeze `316d635a…` lines 1263–1267 and its single-carrier configuration | the same two configurations, and no other | **carried unchanged** |
| act 21's laws `ΦI`, `ΦP`, `ΦC`, `ΦT`, `ΦPP`, `ΦCTRL` with their verdicts, its result `bb02ef41…` lines 578–584 | tested against the geometry, each pinned to its merged equation; verdicts consumed as landed | **consumed as landed** |
| act 22's `Φ_swap` with its verdict, `OrbitLawNaturalityFactorization.lean` `d41b157a…` line 179 | likewise | **consumed as landed** |
| act 23's `Φ_MD`, `Φ_PC`, `Φ_HS`, `Φ_SC` with their verdicts, `OrbitLawGaps.lean` `5ed0dad7…` lines 285, 447, 606, 850 | likewise; act 23's seven shared lemmas consumed | **consumed as landed** |
| act 23's supply item 7, the Fourier family at a unit parameter and its Pythagorean sequence, its freeze `93c06674…` lines 829–836 | consumed, and extended by one rotated point, one index, two bounds and one norm frozen here | **carried, extended** |
| the attestation set, act 21's freeze lines 1033–1043 | carried verbatim, asked at **every** boundary of this round | **carried, re-scoped** |
| THE CLAUSE, act 21's freeze lines 1897–1905 | carried verbatim with "Act 21" → "Act 24" in its first sentence | **carried, one substitution** |
| act 13's `P0` threading sentence, its result `2c38dbf1…` lines 267–273 | named as what this round does not touch | **untouched** |
| everything else — the shared theorem, the censuses, `SIOP`, the headlines, the `P0` sentences of acts 21, 22 and 23 | not this round's | **untouched** |

### External provenance — cited for the route, not for any theorem

Three strands of published mathematics are the provenance of this round's route, and are cited
here **as provenance only**. No theorem of this round is attributed to them, none of their
theorems is consumed, and every statement below is proved in the kernel for this round's own
object, which is not the object any of them treats.

1. **Bargmann invariants.** V. Bargmann, *Note on Wigner's theorem on symmetry operations*,
   J. Math. Phys. 5 (1964): the cyclic products of inner products of a family of vectors are
   invariant under rephasing each vector. The cross-invariant act 12 merged, and the mixed
   triples this round freezes, are quantities of that kind on the fibre-Gram tuple.
2. **Projective unitary equivalence of finite frames.** T.-Y. Chien and S. Waldron, *A
   characterization of projective unitary equivalence of finite frames and applications*: for one
   Gram matrix, diagonal phase conjugation is the equivalence, and for a frame whose Gram matrix
   has no zero entry the triple products of Gram entries determine the equivalence class; when
   zero entries are present, longer cycle products can be needed, and their `n`-cycle example shows
   triples do not suffice in general. **This round's object is not one Gram matrix but a tuple of
   `|V|` Gram matrices with one shared phase action**, equivalently a fibre-labelled multigraph
   version of their graph. The mechanism generalizes, and **the generalization is this round's
   and is proved here**, at full support and for this object, not imported. The zero-entry case
   is out of this round, on exactly their ground.
3. **The one-parameter `4 × 4` complex-Hadamard family.** Act 23's `H(z)`, at
   `star z * z = 1`, is the normalized standard one-parameter family `F₄⁽¹⁾(a)` of the
   complex-Hadamard catalogue (W. Tadej and K. Życzkowski, *A concise guide to complex Hadamard
   matrices*), with the catalogue's parameter `z = i·e^{ia}`; the `4 × 4` equivalence
   classification is part of the Haagerup complex-Hadamard literature (U. Haagerup, *Orthogonal
   maximal abelian ∗-subalgebras of the `n × n` matrices and cyclic `n`-roots*). Act 12's `H(1)`
   and `H(i)` are the real Hadamard and the Fourier points of that family. **Nothing of that
   literature is consumed**: the family is act 23's frozen supply item, its admissibility is act
   23's merged `hadamard_z_admissible`, and its classes are separated here by the record's own
   invariant. In particular the four-entry Haagerup invariant of that literature is not asserted
   to be complete for anything, and no equivalence-testing machinery of that literature is used.

The **Wigner-type shape** of the fourth target — a geometry-preserving map on a state space forced
to be of a named form — is named here as provenance for the *shape of the question* and for nothing
else: the round has no bridge from its orbit space to any Hilbert space, ray space or transition
probability, and asserts none.

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
manifested) are the passages acts 21, 22 and 23 quoted at their own bases, unchanged in wording at
`D` — `AGENTS.md` carries the same blob `a9687b39…` at `D` as at act 23's drafting snapshot.

### The obligation, and what acts 21 through 23 left in front of it

`verification/ROADMAP.md`, **line 63**, the `P0` row, carries act 21's, act 22's and act 23's frozen
Case A sentences at its end; the row's label is **OPEN** and two-part, and this round appends its
own frozen sentence after act 23's and changes the label of nothing.

`verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md`, blob
`14a2cd8c…`, **lines 408–412**, the pseudometric this round's geometry is measured against:

> **The pseudometric is named explicitly in the statement** and is written from the Gram data alone:
> `d(G, G') = ‖G⁰₁₀ · G¹₀₁ − G'⁰₁₀ · G'¹₀₁‖`, the modulus of the difference of act 12's merged
> `∼_D`-invariant. Its three pseudometric properties are proved, and its **`∼_D`-invariance** is
> proved from `gramPhaseEquiv_cross_invariant`, which is what makes it a pseudometric on **orbit
> classes** rather than on representatives.

and act 18's module, `IntermediateCrossTimeStructure.lean` blob `cb14c43b…`, **line 734**, the
equation itself, `d = (fun G G' => ‖G 0 1 0 * G 1 0 1 - G' 0 1 0 * G' 1 0 1‖)`, together with act
18's own recorded failure of that pseudometric to separate: the docstring of the same theorem,
**lines 720–727**, names two `∼_D`-inequivalent classes at distance `0` under it, `[G(H(1))]` and
its column-swapped partner. **That is the reason this round writes a different geometry and does
not reuse act 18's**: one invariant read at one fibre pair is not a complete invariant, and a
pseudometric that vanishes on inequivalent classes cannot be a selector on classes.

`verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md`, blob `174e790d…`,
**line 10**, the state of act 21's ladder after act 23:

> **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n`

and act 21's result, blob `bb02ef41…`, **lines 578–584**, the census every later act consumed: `ΦI`,
`ΦP` and `ΦPP` survive every rung, `ΦX` fails `L0` and is a law rather than a transition family,
`ΦC` fails `L3i` and `L3s` and is not `L-PROP`, `ΦT` fails `L2`, `ΦCTRL` fails `L4n` and `L5`.

`verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md`, blob `2c38dbf1…`,
**lines 267–273**, the threading part of `P0`, which this round does not touch:

> `P0` remains open and two-part, and the threading part is localized exactly: the fibre cross-Gram
> trajectory determines the lift up to one constant in-fibre left move and one time-dependent strong
> right gauge […] nothing in act 13 selects either, and no connection, gauge fixing or
> selection principle is asserted or excluded.

### The act 12 declarations this round is stated over

`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob
`4bba2040c33424fafbc6d31c0d63b86dff33691a`: `LeftFibreGroup` at **lines 78–79**, `FibreGram` at
**95–97**, `GramPhaseEquiv` at **102–103**, `RealizableGram` at **108–110**, `fibreGram_apply` at
**115–116**, `sh1_necessity` at **168**, `fibreGram_left_mul` at **207–208**,
`fibreGram_mul_weak_apply` at **242–245**, `gramPhaseEquiv_cross_invariant` at **870–871**,
`hadamard_slices_not_twoSided` at **907**, `sh1_sufficiency` at **1070**.

The exact shape of `GramPhaseEquiv`, verbatim, which is what "separates act 12's classes" means:

```
def GramPhaseEquiv (G G' : V → Matrix V V ℂ) : Prop :=
  ∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ ∀ i j k, G' i j k = star (c j) * G i j k * c k
```

**Three features are load-bearing and are named now.** The phases `c` are indexed by the matrix
index alone and are the same for every fibre `i`, so a product of Gram entries around a closed walk
of matrix indices is invariant whichever fibre each factor is read in; the relation is an
equivalence relation by act 17's three lemmas; and at `|A| = 1` every realizable tuple has, by
`sh1_sufficiency` and `fibreGram_apply`, the form `G i j k = star (U (i,0) (j,0)) * U (i,0) (k,0)`
with `‖U (i,0) (j,0)‖ ^ 2 = Γ i j`, so that **at the frozen configurations every entry of every
realizable tuple has modulus `Real.sqrt (Γ i j * Γ i k)`, which is `¼` on the single carrier and
`1/16` on the product carrier, and no entry vanishes.** That full-support fact is what makes the
triples complete here, and it is proved from act 12's merged results, not assumed.

### The act 21, act 22 and act 23 declarations consumed

`verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`, blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`: `EvolvesTotally` at **lines 96–100**,
`PreservesAdmissible` at **108–110**, `Reversible` at **123–128**, `FactorizesOnProduct` at
**143–157**, `LadderConds` at **179–196**, `realizable_relabel` at **388**, `relabel_gramPhaseEquiv`
at **397**, `witness_supply` at **431** (its conjuncts `h1i`, the separation `[G(H₁)] ≠ [G(Hᵢ)]`,
`hfix`, `σ` fixes `G(H₁)`, and `h1move`, `[G(H₁)] ≠ [σ G(Hᵢ)]`), `phiI_ladder` at **548**,
`phiP_ladder` at **577**, `phiX_l0_restricts` at **691**, `phiC_census` at **746**,
`phiT_l2_restricts` at **842**, `product_cross` at **963–969**, `relabel_product` at **975–980**,
`relabel_one` at **986**, `product_realizable` at **1015**, `hadamard_entries` at **1062–1080** (its
conjuncts, in order: `d1`, `d2`, `c1`, `c2`, `c3`, `c4`, `e2`, `e3`, `r0`, `r1`, `r2`),
`product_separations` at **1093**, `phiPP_ladder` at **1166** and `phiCTRL_census` at **1282**.
`verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`, blob
`d41b157a3f38d4ebedbe11ad9682a8693836a383`: `relabel_prodComm` at **69**, `gramPhaseEquiv_diag`
at **82**, `phiCTRL_l4n_restricts` at **109**, `phiSwap_l5_restricts` at **179**,
`prefix_not_implies_l5` at **360**.
`verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`, blob
`5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1`: `gramPhaseEquiv_fst_of_product` at **76**,
`product_gramPhaseEquiv_fst` at **94**, `zero_not_realizable` at **106**, `hadamard_z_admissible`
at **116**, `fibreGram_z_entries` at **150**, `zseq_facts` at **168**, `gap_separations` at **222**,
`phiMD_l1_restricts` at **285**, `phiPC_l3i_restricts` at **447**, `phiHS_l3s_restricts` at **606**,
`phiSC_corner` at **850**, `l5_not_implies_l4n` at **1208**. Consumed for what they state; none is
re-proved, and each family is tested here **only against the geometry**, never again against any
rung.

### The act 13, act 17, act 18 and act 20 declarations consumed

`verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob
`8d17177799327d648bbbd001cf237e1ac37bd3fc`: `WeakAnchorStabilizer` at **114–116**.
`verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean`, blob
`afc22cfc93b244c80e1c55a273dcfda1ddebb121`: `GramTrajEquiv` at **121–122**, `gramPhaseEquiv_refl`,
`gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` at **141–170**.
`verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean`, blob
`cb14c43b0becfe1a379ae3615d5553723ede9163`: `ProperAt` at **167–171**, `PropagatesFrom` at
**186–193**, `lc2_regularity_law` at **729–749**.
`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, blob
`4c1137f35600320b9273c857ec62271341b05cd0`: `TwistedNatural` at **128–134**, `RelabelTransition`
at **167–168**, `RelabelLift` at **181–182**.
`verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob
`7e3a8222cedf530f3c109662e7174d72b6358063`: `AdmissibleDilationAt` at **134–136**.

## Start state, pinned by blob

Pinned **by blob** at `D`. Blob identity is authoritative: the commit locates the tree, the blob is
what is compared, and the `D → B` rows of the block below require each of these unchanged at `B`.

| path | blob at `D` |
| --- | --- |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | `d41b157a3f38d4ebedbe11ad9682a8693836a383` |
| `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md` | `316d635a31f91faebeeebef7688b30002d24b4ca` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md` | `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md` | `bb02ef41eb221696ffa45c9281b69553c8279cbb` |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md` | `cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea` |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md` | `b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e` |
| `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md` | `93c06674792fa3565f6f94e5e954e484dca33cf2` |
| `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md` | `174e790d2cc5c663f9f54ae7daaeca90b51f96e1` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | `6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db` |
| `verification/seals/OLT.json` | `8ed0ef5391410db3a112cbe845d27536b7c1ab9b` |
| `verification/seals/OLN.json` | `1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb` |
| `verification/seals/OLG.json` | `8a058df23c07e2b7571672c039a5a7b4f911a339` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `tools/control_plane_base_check.py` | `d6d6578201a9cab3fcb91d63f4818b38104fc4e4` |
| `tools/control_plane_lint.py` | `7678dbe25f51e6e6b14f07e8842f1b6d205f4fed` |

Every one of these is read and never written by this round. If any blob differs at `B`, the
execution records the discrepancy and does not repair the freeze — and for the first twenty-three,
the base check has already refused the merge.

### The files this round writes

**The files this round writes are named separately and are not in the table above.** Each is
pinned by blob at `D` all the same, so that a discrepancy in what the round writes onto is as
visible as a discrepancy in what it reads; a difference at `B` in any of them is recorded in the
result note as a discrepancy and the freeze is not repaired.

| path | blob at `D` | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `d03aa6602d8536ab8aab29dd09ea7602de4d7e78` | **read** as the pinned statement of the `P0` row, and **written** only by appending the frozen post-round sentence for the vector reached after act 23's sentence in the same cell; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `f7a87a38cf04e19be90a96d48d6852e1dccea058` | the `R7-OGS` clause **added**; `_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` **set** as the shape section states, the former emptied by `P`; **nothing else**; no contract of any closed round touched; no legacy constant written |
| `verification/lean-mathlib/OIBridge.lean` | `87a71880518adc9b31672b807323d24270eedfe9` | one import line added directly after `import OIBridge.OrbitLawGaps`, at line 212 at `D` |
| `verification/lean-manuscript-census.json` | `3ade6a83dab02e91c3e7837a4f4b3a77cef48352` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/result.md` | — | created by the execution |
| `verification/seals/OGS.json` | — | created by **`P`**, and by nothing before `P` |

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

The base is fixed the moment this file merges, and whatever sibling lanes have landed in `main` by
then is a fact about the base's tree and not a fact about this round's inputs. The start-state
table above is the complete list of what this round consumes, and a file present at `B` and absent
from that table is read by nothing in this round. The seals tree at `B` is whatever `B` carries;
the execution records the tree it found, and the declared baseline reads it from git.

## Source scoping, carried from acts 13 through 23

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what acts 21 through 23 left in front of it

Acts 21, 22 and 23 settled the content of every rung of act 21's ladder except `L4d`, which is the
shared theorem's own hypothesis: `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4n` and `L5` each restrict, and
neither `L4n` nor `L5` is forced by the prefix with the other. Three things stand in front of the
programme as a result:

1. **The ladder's conditions through `L5` leave a plurality, and the plurality is not of one
   kind.** Among the laws surviving the prefix through `L4d` are the identity, the carrier
   relabellings `ΦP`, `ΦPP` and `Φ_swap`, and the class-conditional relabelling `Φ_SC`, which
   factorizes and admits no twisted-natural lift; among those failing a rung are `ΦC`, `Φ_MD`,
   `Φ_PC` and `Φ_HS`, which merge, drop or shift classes, and `ΦCTRL`, which conditions one factor
   on the other. Every rung of the ladder is a **structural** condition — totality, admissibility,
   time-homogeneity, reversibility, descent, a lift, factorization — and none of them measures how
   far a law moves a class. The record carries no condition of that kind on the orbit space.
2. **The only geometry the record carries on the per-slice orbit space does not separate.** Act
   18's `LC2` pseudometric, act 12's single cross-invariant read at one fibre pair, is proved there
   to be a pseudometric on classes and to vanish on an inequivalent pair. A quantity that is to do
   any selecting on classes must at least separate them; act 18's does not, by act 18's own record.
3. **The natural repair is a complete family of phase invariants, and at the frozen
   configurations it needs only triples.** Every product of Gram entries around a closed walk of
   matrix indices, with a fibre label per step, is invariant under act 12's shared phase action —
   the cross-invariant is the case of a two-step walk. Whether a fixed finite family of such
   products separates classes is a question of the kind the frame literature answers for one Gram
   matrix; for this round's tuple, with a common phase, realizability constraints and a product
   structure, it is answered here. At the frozen configurations no entry of a realizable tuple
   vanishes, so the triples through one base vertex fix every phase, and the family of **all mixed
   triples** — every closed three-step walk with every fibre labelling — is the invariant this
   round freezes. A separating family embeds the class space in a finite-dimensional space, and
   the Euclidean distance of the embedded points is then a metric on classes without any further
   choice; that is the geometry this round tests, and it is induced from the invariants rather than
   proposed as a formula.

**Each target's proof route is the freeze's reading and not a finding**; whether it closes is for the
execution to establish, and every target may end `UNDECIDED` with its obstruction named. **What is
kept out of this round is named now**: composition in time, continuity, generators and any
one-parameter structure; the threading and the cross-time representative; the zero-entry case of
completeness, on which triples are known not to suffice in general; and any comparison of any law
with unitary or quantum evolution. Each is a separate question for a separate freeze.

### What act 24 inherits, and consumes without re-proving

Consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**, and a
merged statement is not enlarged by being consumed.

1. **Act 12's `GramPhaseEquiv`, `RealizableGram`, `FibreGram`, `fibreGram_apply`,
   `gramPhaseEquiv_cross_invariant`, `hadamard_slices_not_twoSided`, `sh1_necessity`,
   `sh1_sufficiency`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`, `LeftFibreGroup`**; **act
   13's `WeakAnchorStabilizer`**; **act 17's `GramTrajEquiv`** and its equivalence lemmas; **act
   18's `ProperAt`, `PropagatesFrom`** and, for measurement only, **`lc2_regularity_law`**.
2. **Act 20's `RelabelTransition`, `TwistedNatural`, `RelabelLift`.**
3. **Act 21's ladder**, as the declarations of its merged module, and **act 21's rung verdicts and
   census**, all of which stand as act 21 states them; **act 21's product-embedding results**
   `product_realizable`, `product_cross`, `relabel_product`, `relabel_one`, `hadamard_entries`,
   `product_separations`, `witness_supply`, `realizable_relabel`, `relabel_gramPhaseEquiv`.
4. **Act 22's verdicts** `L4n-RESTRICTS`, `L5-RESTRICTS`, `PREFIX-NOT-IMPLIES-L5`, its
   `relabel_prodComm` and `gramPhaseEquiv_diag`, and its `Φ_swap` with the prefix conjuncts
   `phiSwap_l5_restricts` carries.
5. **Act 23's verdicts** `L1-RESTRICTS`, `L3i-RESTRICTS`, `L3s-RESTRICTS`, `L5-NOT-IMPLIES-L4n`,
   its seven shared lemmas, and its four families with the conjuncts their verdict theorems carry —
   in particular `phiSC_corner`'s prefix-through-`L4d` and `L5` conjuncts, which one cell of the
   fourth target consumes.
6. **Act 21's and act 23's historical verdicts are not changed by anything here**: this round
   tests every family against the geometry and against nothing else, and no rung status is
   re-earned, re-graded or reinterpreted.

## The questions, FROZEN — four, gated

> **GEO1.** Is the mixed-triple feature map — every product of three Gram entries around a closed
> three-step walk of matrix indices, with a fibre label per step — a complete invariant of act 12's
> classes on the realizable tuples at the frozen configurations, and is the Euclidean distance of
> feature vectors a metric on classes: nonnegative, symmetric, subadditive, constant on each class
> in both arguments, and zero exactly on the pairs `GramPhaseEquiv` relates?
>
> **GEO2.** Do the record's legitimate constructions preserve it: is every carrier relabelling an
> exact isometry of it, does act 12's two-sided gauge act trivially on it, and does the feature
> map turn the product embedding into a tensor product, so that the distance between two products
> with a common second factor is the factors' distance scaled exactly by the common factor's
> feature norm?
>
> **GEO3.** Which of the record's transition families, and the one family frozen new here, are
> isometries of it on realizable tuples at their own configurations, and does at least one law
> satisfying every structural condition of act 21's ladder before naturality fail to be one?
>
> **GEO4.** Does the prefix of act 21's ladder through `L4d`, with factorization and with isometry,
> force a law to act on classes as a carrier relabelling, or as a carrier relabelling composed with
> entrywise conjugation; and how does isometry sit against `L4n` and `L5` in the four implication
> cells the earlier rounds' shape fixes?

Each is a question about act 12's exact equivalence, act 21's exact declarations and the record's
exact families at the record's exact configurations. **The round does NOT try to derive Schrödinger
evolution**, does not characterize the surviving class or the isometries, does not ask whether the
invariant family is the right family, does not ask about continuity or composition in time, and
does not ask what any rung means beyond the declaration act 21 froze.

## The strength of the ask, FROZEN

**The ask is one completeness-and-metric verdict, one control verdict, one discrimination verdict
over a closed list of twelve named families, and one gated rigidity verdict with five recorded
implication cells, each earned by its own named route or reported undecided, in one fixed order.**
It does **not** undertake a census of the ladder, a characterization, an independence claim, or the
inference of one target's status from another's.

**What each verdict would and would not establish, stated in advance.** A completeness verdict
says that one specific finite family of phase invariants, written from the Gram data, separates the
realizable classes at the frozen configurations, and that the geometry it induces is a metric on
them; it says nothing about zero-entry tuples, nothing about that family being minimal, canonical or
physical, and nothing about the induced metric being canonical. A controls verdict says that three
specific constructions of the record respect it; it says nothing about constructions not on the
list. A discrimination verdict says that one specific structurally admissible law of the record
moves realizable classes by unequal amounts; it says nothing about laws not on the list and does not
say that isometry is the right condition to impose. A rigidity verdict, in either direction, is a
statement about the exact hypotheses at the exact configuration; **no outcome of this round says
that any law is, resembles or approaches quantum evolution.**

## The objects, FROZEN — act 12's and act 21's, consumed, one invariant family and one geometry

`V`, `A`, `a₀`, `Γ`, the transition family, the law it generates, the admissible orbit state space
`Ω(Γ, t)` and the frozen quotient list are act 21's, at its lines 642–733, consumed without
restatement. In particular:

- **A transition family** is `Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)`, written at
  representative level; **the law it generates** is `∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`.
- **The frozen quotient list** is act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv` and act 21's
  `LawEquiv`, and **no other equivalence may be used in any verdict**. This round's verdicts are
  about an invariant whose level sets on realizable tuples are act 12's classes, and about a
  distance whose zero set there is `GramPhaseEquiv`; none is taken modulo anything else.

### The invariant family, FROZEN — the one definition the budget admits

On a carrier `V` with `[Fintype V] [DecidableEq V]`, for a tuple `G : V → Matrix V V ℂ`:

> **Statement.** The mixed-triple feature map sends `G` to the function on
> `(V × V × V) × (V × V × V)` — three fibre labels and three matrix indices — whose value at
> `((i₁, i₂, i₃), (j₁, j₂, j₃))` is `G i₁ j₁ j₂ * G i₂ j₂ j₃ * G i₃ j₃ j₁`.

Written as the one definition the execution's module carries, whose body the guard pins verbatim:

```
def mixedTriple (G : V → Matrix V V ℂ) : (V × V × V) × (V × V × V) → ℂ :=
  fun p => G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1
```

**Repeated indices are allowed and are load-bearing.** At `(j, j, j)` the value is a product of
three diagonal entries; at `(j, j, k)` with labels `(i, i, i)` it is `G i j j * G i j k * G i k j`,
the diagonal times the squared modulus of one entry, which is how the family carries the moduli; at
`(i₁, i₁, i₀)` with labels `(i₁, i₀, i₁)` it is `G i₁ i₁ i₁ * G i₀ i₁ i₀ * G i₁ i₀ i₁`, the diagonal
times act 12's cross-invariant at the fibre pair `(i₀, i₁)`, which is how the family carries every
quantity acts 12 through 23 separated classes with. **No other coordinate is singled out**: the
family is the whole finite index set, so that a relabelling of the carrier acts on it by permuting
coordinates.

### The geometry, FROZEN — bound by equation, never defined

> **Statement.** `d G H` is the Euclidean norm of `mixedTriple G − mixedTriple H`.

Written as the equation every theorem of this round that names `d` carries as a hypothesis, and to
which the guard pins it:

```
d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)
```

**Three things about these objects, fixed now.**

1. **Every coordinate is act 12's action read around a loop.** Under `G' i j k = star (c j) * G i j
   k * c k` each of the three factors picks up `star (c jₐ) … c j_b`, and around the closed walk
   `j₁ → j₂ → j₃ → j₁` every `c j` meets its own `star`, so `mixedTriple G' = mixedTriple G`. No new
   relation enters: the induced distance vanishes on `GramPhaseEquiv`-pairs by that computation and
   nowhere else on the realizable tuples by the separation theorem of `GEO1`.
2. **The norm is the Euclidean one on a finite-dimensional space, written as a sum**, and not
   Mathlib's Frobenius instance on matrices, which is scoped; the triangle inequality is
   `EuclideanSpace.norm_eq` and the norm's own subadditivity, and every other property is proved
   from the sum.
3. **`mixedTriple` is the only definition.** The definition budget below is one; `d`, the isometry
   proposition, every family and every auxiliary object are bound variables pinned by equation in
   the statements that need them, exactly as act 18's `lc2_regularity_law` binds its pseudometric
   and as acts 21 through 23 bind their transition families. **A second `def` is a defect of the
   round.**

**The isometry predicate, likewise bound by equation.** For a configuration `(A, Γ)` and a
transition family `Φ`, "`Φ` is an isometry" is the proposition

```
∀ t (G H : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ t) H →
  d (Φ t G) (Φ t H) = d G H
```

written out wherever a statement needs it, never abbreviated. It quantifies over **realizable**
tuples only, at every `t`, and asks for **equality** of distances; a non-expanding map is not an
isometry in this sense, and a map that is an isometry on the reached classes only is not one either.

### The two frozen configurations

Act 21's two, and no other:

- **The single-carrier configuration**: `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ t ≡ ¼` — act 12's,
  the one `phiI_ladder`, `phiP_ladder`, `phiC_census` and `phiT_l2_restricts` are stated at. The
  feature space has `4⁶ = 4096` coordinates.
- **The product configuration**: `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`,
  `Γ ≡ 1/16` as the pointwise product `Γ₀ ⊗ Γ₀` of two copies of `Γ₀ ≡ ¼`, the decomposition
  `e = Equiv.refl (Fin 4 × Fin 4)`, `Γ₁ = Γ₂ = Γ₀` at every `t` — act 21's at its lines 1263–1267,
  the one `phiPP_ladder`, `phiCTRL_census`, `phiSwap_l5_restricts` and act 23's four verdicts are
  stated at. The feature space has `16⁶` coordinates, and no statement of this round enumerates it:
  every product-carrier distance this round bounds is reduced to single-carrier distances by the
  tensor identity of `GEO2`.

`GEO1`'s invariance and metric properties are stated at an arbitrary finite carrier; its separation
is stated at an arbitrary finite carrier under a base-star support hypothesis and instantiated at
both configurations, where the hypothesis is discharged from act 12's merged results. `GEO2`'s
controls are stated at an arbitrary finite carrier where they can be and at arbitrary factor
carriers where the product embedding is involved. `GEO3` tests each family **at the configuration
its own merged verdict is stated at**. `GEO4` is at the product configuration.

**The one-`|A|`-value caveat, carried from acts 18, 21, 22 and 23 and recorded again.**
`|A₁| = |A₂| = 1` is the strongest case for the per-slice statements and is not degenerate there; it
is not automatically the right case for a cross-time statement, and every verdict of this round is
at that cardinality and at no other. **It is also the case in which the triples are complete**: the
full-support fact rests on rank one, and nothing here is asserted about `|A| > 1`.

## The ladder, CONSUMED and not restated, and the prefix the fourth target uses

The ladder is act 21's `L0`–`L5` in act 21's wording, at its lines 735–946, as the declarations of
`OrbitLawRigidityTwisted.lean` at blob `860daac4…`, conjoined as `LadderConds` in the order: the
two standing hypotheses `ProperAt` and `PropagatesFrom`, then `L0`, `L1`, `L2`, `L3` (`L3i` then
`L3s`), `L4d`, `L4n`, `L5`. **This round's module states no rung.**

**"The prefix through `L4d`" means, in every statement of this round, the first seven conjuncts of
`LadderConds`**: `ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, the inline
`L2`, `Reversible`, the inline `L4d`. **"Structurally admissible"** means satisfying that prefix.
`L4n` is the eighth conjunct and `L5` the ninth, each named separately wherever it enters.

### The implication matrix of the fourth target, FROZEN

The fourth target records five implication cells and two rigidity statements, each a separate
proposition, none inferred from another. Throughout, `GEO Φ` abbreviates in this table — and
nowhere in the module — the isometry proposition displayed above at the product configuration.

| cell | assumed | tested | route | explicitly out of scope |
| --- | --- | --- | --- | --- |
| `a0` | `GEO Φ` | the first conjunct of `Reversible` on realizable inputs | universal, from separation: `d (Φ t G) (Φ t G') = 0 → d G G' = 0` | anything about `L3s`, `L1` or `L0` |
| `a1` | the prefix through `L4d`, `L5` | `GEO Φ` | the named witness `Φ_SC`: its prefix and `L5` conjuncts consumed from `phiSC_corner`, its non-isometry from `GEO3` | any independence of `GEO` and `L5` |
| `a2` | the prefix through `L4d`, `L4n` | `GEO Φ` | universal attempt only; no family on the list satisfies the hypotheses and fails `GEO` | any independence of `GEO` and `L4n` |
| `a3` | the prefix through `L4d`, `GEO Φ` | `L5` | the named witness `Φ_swap`: its prefix conjuncts consumed from `phiSwap_l5_restricts`, its `L5` failure from the same, its isometry from `GEO3` | as `a1` |
| `a4` | the prefix through `L4d`, `GEO Φ` | `L4n` | universal attempt only; no family on the list satisfies the hypotheses and fails `L4n` | as `a2` |
| `b₀` | the prefix through `L4d`, `L5`, `GEO Φ` | at every `t`, one `σ : Equiv.Perm V` with `Φ t G ∼ RelabelTransition σ G` for every realizable `G` | the named witness `Φ_conj`, frozen below | — |
| `b` | the prefix through `L4d`, `L5`, `GEO Φ` | at every `t`, one `σ` with, for every realizable `G`, `Φ t G ∼ RelabelTransition σ G`, **or** one `σ` with, for every realizable `G`, `Φ t G ∼ RelabelTransition σ (fun i => Matrix.of fun j k => star (G i j k))` | universal attempt only; no family on the list satisfies the hypotheses and fails the conclusion | any statement that the conclusion is unitary, antiunitary, or quantum |

**Nothing in one row is inferred from another row.** The label of the fourth target is earned by
`b` alone; `a0`–`a4` and `b₀` are recorded sub-verdicts with their own frozen sentences, and no
combination of them is reported as more than itself.

### The labels of each target, and the three-way discipline

For each target the frozen route is the **named construction or the named proof route**. A positive
universal label (`GEO1-METRIC`, `GEO2-CONTROLS-PASS`, `GEO4-RIGID`, and `IMPLIES` in a cell) is
earned only by a universal kernel proof; a negative label (`GEO2-CONTROL-FAILS`,
`GEO3-DISCRIMINATES`, `NOT-IMPLIES` in a cell, `NOT-RIGID` for `b₀`) only by an **exhibited**
witness on the frozen list with the separating quantity named; **`UNDECIDED` by the recorded
statement that neither was reached, with the obstruction named.** A universal proof is a finding
about the condition; it is never inferred from the failure of a witness, never from the absence of
one, and never from census silence. **Failure to obtain a universal theorem is `UNDECIDED`, never a
positive label and never a negative one.**

## The gate, FROZEN — the execution order and the three failure rules

**The gate is this round's freeze rule and not an `AGENTS.md` rule.** It exists because the four
targets are not independent in meaning: a control tested against a non-separating invariant, a
discrimination measured in a geometry a relabelling does not preserve, and a rigidity attempted
with an isometry predicate that discriminates nothing would each be a verdict about the wrong
object. The gate keeps every verdict about the object the freeze names.

### Safeguard 1 — the fixed order, one verdict commit per executed target, and the attestation set at every boundary

The targets are executed in the order **`GEO1` → `GEO2` → `GEO3` → `GEO4`**, and in no other.

The execution's commits on the first-parent chain from `B` are, in order: **the stage-A commit**
(the two declarations set to `B`, in the guard file only); **the module commit** (the module with
the one definition, its shared lemmas and **no verdict of any target** — no named result of `GEO1`,
`GEO2`, `GEO3` or `GEO4`); then **exactly one verdict commit per executed target**, in target order,
each carrying that target's named results and nothing of a later target's; then the packaging
commit. A target the gate does not open has **no verdict commit**, and its label is its
`NOT-EXECUTED` label with the frozen sentence. A verdict commit that carries a later target's
result, or a target executed out of order, is recorded as a discrepancy and the round's ordering
obligation is reported as undischarged for that target.

**The attestation set is answered at every boundary.** Act 20's three questions, in act 21's
wording at its lines 1033–1043 — **Q1 INTENTIONAL**, **Q2 INCIDENTAL**, **Q3 UNAIDED REASONING** —
are answered by the result note **once per span**, for the spans `B` → module commit, module commit
→ `GEO1`'s verdict commit, `GEO1` → `GEO2`, `GEO2` → `GEO3`, `GEO3` → `GEO4`, each answer a
measurement about what the execution acquired **in that span** bearing on any target **not yet
closed at the span's end**; a span ending at a target the gate did not open is answered for the
targets that remain. The partial-fact rule applies at every boundary: learning one family's isometry
status while `GEO2` is open is a YES. A YES is disclosed with what was learned, when, and whether any
later target's route changed afterwards; it is not concealed and not argued away, and a disclosure
does not cure it. **What the freeze itself places in front of the execution is not a YES and is
listed rather than left implicit**: this file carries the proof route for every target, the values
of every separating quantity, the consumption of `GEO3`'s `Φ_SC` and `Φ_swap` verdicts by cells `a1`
and `a3`, and the record's result notes carry every consumed fact; the questions are about what was
acquired beyond the freeze and the pinned blobs.

### Safeguard 2 — the route-authorization matrix

**Each named construction or route may answer exactly the target this matrix authorizes, and no
other.** A fact found or learned during a later target's work may not be retroactively assigned to
an earlier target; an alternative witness for any cell found during execution is an observation and
never substituted.

| construction or route | `GEO1` | `GEO2` | `GEO3` | `GEO4` |
| --- | --- | --- | --- | --- |
| the loop invariance of every coordinate, the based-triangle gauge fixing, the full-support fact from act 12's sufficiency, the Euclidean norm facts | **authorized** | — | — | — |
| the permutation of the index set by a relabelling, the two-sided gauge laws, the tensor identity of the feature map on products | — | **authorized** | — | — |
| the twelve families, each at its own configuration, with the perturbation pairs and the shift argument | — | — | **authorized** | — |
| `Φ_SC` for `a1`, `Φ_swap` for `a3`, `Φ_conj` for `b₀`, the universal routes for `a0`, `a2`, `a4`, `b` | — | — | — | **authorized** |
| the shared lemmas of the module commit | consumed | consumed | consumed | consumed |

**Shared lemmas are not verdicts.** The module commit's lemmas — the invariance of every
coordinate under the phase action, the coordinate bound `‖mixedTriple G p − mixedTriple H p‖ ≤ d G
H`, the cross-invariant coordinates and their values on the pinned objects, the entry bound on the
Fourier family and the coordinate bound it gives, the feature norm of `F(z)` at a unit parameter,
the sequence's two distance identities, and the conjugation facts — are consumed by whichever
verdict needs them and answer no target by themselves.

### Safeguard 3 — the outcome-vector table

The round's headline is a **vector of four labels**, one per target, each drawn from its target's
frozen label set, and **the headline is selected verbatim from the outcome-vector table in the
status rule below**, which lists every admissible vector under the gate. No single-label headline,
no summary label and no combination label exists for this round.

### Failure rule 1 — a universal theorem not obtained is `UNDECIDED`

For every target and every cell, failure to obtain a universal theorem — whether or not one was
attempted — is reported as the `UNDECIDED` label with the obstruction named, never as the positive
label and never as the negative one. Census silence is not a finding about any condition.

### Failure rule 2 — a witness that fails its own hypotheses is recorded, not repaired

If a named witness unexpectedly fails a hypothesis of the cell it is named for — a consumed conjunct
that does not instantiate as the freeze reads it, a perturbation pair one of whose members is not
realizable or is fired when the freeze says it is not — the execution **records that fact**, with the
failing conjunct, and the cell or target takes its **preregistered fallback outcome — its
`UNDECIDED` label with that obstruction named**. The witness set is not repaired, no witness is slid
to another cell, and no other construction is substituted.

### Failure rule 3 — the gate closes forward and never reopens

`GEO2` is executed only if `GEO1` reaches `GEO1-METRIC`; `GEO3` only if `GEO2` reaches
`GEO2-CONTROLS-PASS`; `GEO4` only if `GEO3` reaches `GEO3-DISCRIMINATES`. A target the gate does not
open takes its `NOT-EXECUTED` label, and every later target does too; **no partial execution of a
closed target is reported as anything**, and a closed target's route is not attempted "for
information". The gate reads the label as earned and never the freeze's prediction.

## The frozen family list — twelve named transition families, eleven from the record and one new

**Twelve named transition families, each at the configuration its merged verdict is stated at. The
list is closed at this freeze.** A candidate discovered during execution is recorded as an
observation and not executed. Throughout, `H₁` and `Hᵢ` are act 12's Hadamard dilations at `Γ₀ ≡ ¼`,
`G₁ := FibreGram 0 H₁` and `Gᵢ := FibreGram 0 Hᵢ`; `H(z)` is act 23's Fourier family at a unit
parameter and `F(z) := FibreGram 0 (H(z))`, so that `G₁ = F(1)` and `Gᵢ = F(i)`;
`σ := Equiv.swap (2 : Fin 4) 3`; `X ⊠ Y` is the product embedding
`(X ⊠ Y) i j k = X i.1 j.1 k.1 · Y i.2 j.2 k.2`; `σX` is `RelabelTransition σ X`; `∼` is act 12's
`GramPhaseEquiv`; `Ψ` is `mixedTriple`; and "realizable" means `RealizableGram (Fin 1) Γ₀` on a
factor and `RealizableGram (Fin 1 × Fin 1) (Γ t)` on the product carrier. `ΦX` of act 21 is
**excluded**: act 21's `phiX_l0_restricts` states it as a law on trajectories and not as a
transition family, so the isometry proposition is not stated of it, and its exclusion is recorded
here and is not a verdict.

**Every family is pinned, in every theorem that names it, to the equation its merged verdict
carries**, quoted below verbatim from the merged module, and to nothing else.

### The single-carrier families, at act 12's configuration

| family | merged equation | merged verdict consumed | predicted against the geometry |
| --- | --- | --- | --- |
| `ΦI` | `fun _ G => G` (`phiI_ladder`) | survives every rung | **isometry** — trivially, `d G H = d G H` |
| `ΦP` | `fun _ G => RelabelTransition (Equiv.swap (2 : Fin 4) 3) G` (`phiP_ladder`) | survives every rung | **isometry** — by the relabelling control of `GEO2` |
| `ΦC` | `fun _ _ => FibreGram (0 : Fin 1) H₁` (`phiC_census`) | fails `L3i`, `L3s`; not `L-PROP` | **not an isometry** — the pair `G₁`, `Gᵢ`, both realizable by `sh1_necessity`, both sent to `G₁`: `d G₁ G₁ = 0` while `d G₁ Gᵢ ≥ ‖Ψ G₁ p − Ψ Gᵢ p‖ = ¼ · ‖1/16 − i/16‖ > 0` at the cross-invariant coordinate `p = ((1,0,1),(1,1,0))`, by `hadamard_entries`'s `c1`, `c2` |
| `ΦT` | `fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G` (`phiT_l2_restricts`) | fails `L2` | **isometry** — at each `t` the map is the identity or `σ`, each an isometry |

### The product families, at act 21's product configuration

| family | merged equation | merged verdict consumed | predicted against the geometry |
| --- | --- | --- | --- |
| `ΦPP` | `fun _ G => RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) G` (`phiPP_ladder`) | survives every rung | **isometry** — a relabelling |
| `ΦCTRL` | `fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂ ∧ GramPhaseEquiv G (G₁ ⊠ G₂) then RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G else G` (`phiCTRL_census`, its `⊠` written out) | fails `L4n`, `L5`; satisfies the prefix through `L4d` | **not an isometry** — the perturbation pair below |
| `Φ_swap` | `fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` (`phiSwap_l5_restricts`) | satisfies the prefix through `L4n`, fails `L5` | **isometry** — a relabelling |
| `Φ_MD` | act 23's two-time statement (`phiMD_l1_restricts`, module lines 285–300) | fails `L1` | **not an isometry** — at `t = 0` its map is `Φ_PC`'s, and `Φ_PC`'s pair below refutes it at `t = 0` |
| `Φ_PC` | `fun _ G => if GramPhaseEquiv G (Gᵢ ⊠ G₁) then G₁ ⊠ G₁ else G` (`phiPC_l3i_restricts`, its `⊠` written out) | fails `L3i` | **not an isometry** — the pair `Gᵢ ⊠ G₁`, `G₁ ⊠ G₁`, both realizable by `product_realizable`, both sent to `G₁ ⊠ G₁`: the images are at distance `0` while the inputs differ at the cross-invariant coordinate of the product pair `((0,0),(1,0))`, values `(1/16)(i/256)` and `(1/16)(1/256)` by `product_cross`, `c1`, `c2` and `d1` |
| `Φ_HS` | `fun _ G => if h : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n) then F (Nat.find h + 1) else G` with `F n = FibreGram 0 (H (zs n)) ⊠ G₁` and `zs` act 23's sequence (`phiHS_l3s_restricts`) | fails `L3s` | **not an isometry** — the shift argument below |
| `Φ_SC` | `fun _ G => if ∃ G₂, RealizableGram (Fin 1) Γ₀ G₂ ∧ (GramPhaseEquiv G (Gᵢ ⊠ G₂) ∨ GramPhaseEquiv G (σGᵢ ⊠ G₂)) then RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G else G` (`phiSC_corner`, its `⊠` written out) | satisfies the prefix through `L4d` and `L5`, fails `L4n` | **not an isometry** — the perturbation pair below |

### `Φ_conj` — the entrywise conjugation, NEW to the record; the `b₀` witness, and the twelfth family of `GEO3`

> **Statement.** At every `t`: `Φ_conj t G = fun i => Matrix.of fun j k => star (G i j k)`, at the
> product configuration.

**Where it comes from.** The isometries of the geometry that the record's laws exhibit are all
relabellings, and a rigidity statement whose conclusion is "acts on classes as a relabelling" is
the natural first form of `b`. The freeze's reading is that this form is **false**, and the
witness is the simplest map that preserves every structural condition and every distance while
reversing the orientation of every phase: entrywise complex conjugation. Its role is **the `b₀`
countercontrol**, and it is also the twelfth family tested in `GEO3`, where its predicted verdict is
isometry. **It is named for testing and endorsed for nothing**; in particular nothing here calls it
antiunitary, a symmetry, or a candidate for anything. Its visibility as a separate branch is
deliberate: the complex-Hadamard literature this round cites as provenance treats equivalence to the
entrywise conjugate as a distinct structural question, and this round keeps it distinct too.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **Descent and `L4d`.** If `H = c ⋆ G` then `star H = (star c) ⋆ (star G)` entrywise, with
  `‖star (c j)‖ = 1`; so `G ∼ G' → Φ_conj t G ∼ Φ_conj t G'`.
- **`L1`.** Entrywise conjugation of a positive semidefinite matrix is positive semidefinite (it is
  the transpose of its conjugate transpose, and the transpose of a positive semidefinite matrix is
  positive semidefinite); it preserves rank, sums, and the diagonal, which is real by
  `RealizableGram`'s fourth conjunct. So the image of a realizable tuple is realizable.
- **`L0`, `L2`, `L3i`, `L3s`.** `Φ_conj t ∘ Φ_conj t = id` exactly, so the map is an involution on
  tuples; `L0`'s solutions are the iterates, realizable at every `t` by `L1`; `L2` by construction;
  injectivity and surjectivity on classes from the involution and descent.
- **`L-PROP`.** `ProperAt`: `G₁ ⊠ G₁` and `F(−1) ⊠ G₁` are real tuples, fixed exactly, realizable,
  and `∼`-inequivalent through the product cross-invariant at `((0,1),(0,0))`, values `1/256` and
  `−1/256` by `fibreGram_z_entries` at `z = 1` and `z = −1` and `product_cross`; the non-solution is
  the constant trajectory at `Gᵢ ⊠ G₁`, whose image `F(−i) ⊠ G₁` is inequivalent to it through the
  same pair, values `i/256` and `−i/256`. Propagation clause (i) by descent, clause (ii) at `t = 1`.
- **`L5` holds**, with `Φ₁ = Φ₂ = ` the single-carrier conjugation: `star (X ⊠ Y) = star X ⊠ star Y`
  entrywise, an equality, and the displayed equivalence is `gramPhaseEquiv_refl`.
- **Isometry.** `Ψ (star G) p = star (Ψ G p)` at every coordinate, so
  `‖Ψ (star G) p − Ψ (star H) p‖ = ‖Ψ G p − Ψ H p‖` and the two sums agree termwise.
- **`b₀` fails.** The argument runs on the **cross-invariant** coordinates and on nothing else,
  because the raw coordinates of `Ψ (Gᵢ ⊠ G₁)` take every value in `{±1/4096, ±i/4096}` and would
  not separate. Every cross-invariant of `Gᵢ ⊠ G₁` at any pair of product indices is a product of
  a cross-invariant of `Gᵢ` and one of `G₁`, each of which — including the diagonal pairs, where the
  invariant is the squared diagonal entry `1/16` — lies in `{1/16, i/16}` for `Gᵢ` and equals
  `1/16` for `G₁`; so every cross-invariant of every relabelling `σ (Gᵢ ⊠ G₁)` lies in
  `{1/256, i/256}`. The cross-invariant of `Φ_conj t (Gᵢ ⊠ G₁) = F(−i) ⊠ G₁` at `((0,1),(0,0))` is
  `−i/256`. So for no `σ` is `Φ_conj t (Gᵢ ⊠ G₁) ∼ σ (Gᵢ ⊠ G₁)`, by
  `gramPhaseEquiv_cross_invariant`. **The failing conclusion is the relabelling clause of `b₀`; the
  separating class is `[Gᵢ ⊠ G₁]`, and the separating quantity is the cross-invariant at
  `((0,1),(0,0))`.** The sixteen cross-invariants of `Gᵢ` at ordered pairs are computed in the
  module commit, before any verdict.

## The witness supply, FROZEN

Act 21's supply at its lines 1389–1409 and act 23's item 7, unchanged, **extended by act 23's merged
lemmas** named in the inheritance list, and **extended by three items, frozen now**:

8. **One rotated parameter and one fixed index.** With `zs` act 23's sequence,
   `zs n = ((n² − 1) + 2n·i)/(n² + 1)`, the point `w n := Complex.I * zs n`, of modulus one, with
   `w n ≠ i` for every `n ≥ 1` since `zs n ≠ 1`; and the fixed index `N := 32768`, that is `2¹⁵`,
   at which the perturbation pairs of `GEO3` are read. **This item is used by the `ΦCTRL` and
   `Φ_SC` pairs and by nothing else.**
9. **Two distance identities of the sequence.** `‖zs n − 1‖ ^ 2 = 4 / (n² + 1)` and
   `‖zs (n+1) − zs n‖ ^ 2 = 4 / ((n² + 1) · ((n+1)² + 1))`, for every `n`, from
   `zs n = (n + i)/(n − i)`. Proved in the module commit. **Used by the `ΦCTRL`, `Φ_SC` and `Φ_HS`
   arguments.**
10. **The entry bound, the coordinate bound and the feature norm of the Fourier family.** For unit
    `z`, `z'`: every entry of `F(z)` has modulus `¼`; every entry of `F(z') − F(z)` has modulus at
    most `‖z' − z‖ / 4`, each entry of `F(z)` being one of `±¼`, `±z/4`, `±star z/4`, the
    `z`-dependence cancelling in the entries that pair `z` with `star z` since `star z * z = 1`;
    hence every coordinate of `Ψ (F(z')) − Ψ (F(z))` has modulus at most `3 ‖z' − z‖ / 64`, by the
    three-term product rule with two factors of modulus `¼`, so that, over the `4096` coordinates,
    `d (F(z)) (F(z')) ≤ 3 ‖z' − z‖`; and every coordinate of `Ψ (F(z))` has modulus `1/64`, so that
    `Real.sqrt (∑ p, ‖Ψ (F(z)) p‖ ^ 2) = 1`. Proved in the module commit, the entry facts by cases
    over the sixty-four index triples. **Used by the same three arguments**, and it enlarges no
    merged statement: it is a bound on act 23's family, not an extension of it.

**Nothing outside this supply may be introduced, at any point, for any reason.** The generic witness
rule governs every countercontrol: what a cell's named witness is is what is tested, and an
alternative found during execution is recorded as an observation and never substituted.

### The three perturbation arguments, recorded as the freeze's reading

**The two bounds every argument uses**:

- **Upper, on products with a common second factor**, consumed from `GEO2`'s control (c):
  `d (X ⊠ Y) (X' ⊠ Y) = d X X' · Real.sqrt (∑ p, ‖Ψ Y p‖ ^ 2)`, an equality; with `Y` either of
  `G₁`, `Gᵢ` the feature norm is `1` by item 10, so `d (F(z) ⊠ Y) (F(z') ⊠ Y) = d (F(z)) (F(z')) ≤
  3 ‖z' − z‖`.
- **Lower, at one coordinate**, a shared lemma of the module commit: `‖Ψ G p − Ψ H p‖ ≤ d G H` for
  every `p`, a coordinate of a Euclidean vector being bounded by its norm. At the coordinate
  `p = ((i₁, i₀, i₁), (i₁, i₁, i₀))` the value is `G i₁ i₁ i₁` times act 12's cross-invariant at
  the fibre pair `(i₀, i₁)`; on realizable tuples the first factor is `Γ i₁ i₁`, which is `¼` on the
  single carrier and `1/16` on the product carrier.

**`ΦCTRL`, at `t = 0` and `N = 32768`.** `G := G₁ ⊠ Gᵢ` fires (`G₂ = Gᵢ`, `gramPhaseEquiv_refl`), so
`ΦCTRL 0 G = G₁ ⊠ σGᵢ` by `relabel_product` and `relabel_one`. `H := F(zs N) ⊠ Gᵢ` does not fire:
`H ∼ G₁ ⊠ G₂` for a realizable `G₂` gives `F(zs N) ∼ G₁` by `gramPhaseEquiv_fst_of_product` at
`m = 0` (both second factors have diagonal entry `¼` at `(0,0,0)`, `Gᵢ` by `hadamard_entries`'s `d2`
and `G₂` by realizability), hence `zs N / 16 = 1/16` by `fibreGram_z_entries` and
`gramPhaseEquiv_cross_invariant`, against `zseq_facts`'s `zs n ≠ 1`. Both `G` and `H` are
realizable by `product_realizable` from `hadamard_z_admissible` and `sh1_necessity`. **Then**
`d G H = d G₁ (F(zs N)) ≤ 3 ‖zs N − 1‖ = 6 / Real.sqrt (N² + 1) < 6/N < 1/4096`, while the images
are separated at the cross-invariant coordinate of the product pair `((0,0),(0,2))`: the
cross-invariant of `G₁ ⊠ σGᵢ` there is `(G₁ 0 0 0)² · (σGᵢ invariant at (0,2)) = (1/16)(i/16)` by
`hadamard_entries`'s `d1` and `r2`, and that of `F(zs N) ⊠ Gᵢ` there is `(F(zs N) 0 0 0)² · (Gᵢ
invariant at (0,2)) = (1/16)(1/16)` by `fibreGram_z_entries` and `c3`; the coordinate difference is
`(1/16) · ‖i − 1‖/256 ≥ 1/4096`, so `d (ΦCTRL 0 G) (ΦCTRL 0 H) ≥ 1/4096 > d G H`. **The failing
proposition is isometry at `t = 0` on the pair named; the separating quantity is the
cross-invariant coordinate at `((0,0),(0,2))`.**

**`Φ_SC`, at `t = 0` and `N = 32768`.** `G := Gᵢ ⊠ G₁` fires (`G₂ = G₁`, first disjunct), so
`Φ_SC 0 G = σGᵢ ⊠ G₁`. `H := F(w N) ⊠ G₁` does not fire: the first disjunct gives `F(w N) ∼ Gᵢ` by
the marginal lemma and so `w N / 16 = i/16`, and the second gives `F(w N) ∼ σGᵢ` and so
`w N / 16 = i/16` by `hadamard_entries`'s `r1`; either gives `w N = i`, against item 8. **Then**
`d G H = d Gᵢ (F(w N)) ≤ 3 ‖w N − i‖ = 3 ‖zs N − 1‖ < 1/4096`, while the images are separated at
the cross-invariant coordinate of the product pair `((0,0),(2,0))`: the cross-invariant of
`σGᵢ ⊠ G₁` there is `(σGᵢ invariant at (0,2)) · (G₁ 0 0 0)² = (i/16)(1/16)` by `r2` and `d1`, and
that of `F(w N) ⊠ G₁` there is `(F(w N) 0 2 0 · F(w N) 2 0 2)(1/16) = (1/16)(1/16)`, the first
factor being `z`-free because the rows `0` and `2` of `H(z)` are `z`-free — a shared lemma of the
module commit extending `fibreGram_z_entries` by the pair `(0,2)`. So `d (Φ_SC 0 G) (Φ_SC 0 H) ≥
1/4096 > d G H`. **The failing proposition is isometry at `t = 0` on the pair named; the
separating quantity is the cross-invariant coordinate at `((0,0),(2,0))`.**

**`Φ_HS`, at every `t`.** For `n ≥ 1`, `Φ_HS t (F n) = F (n + 1)`, since the branch index is unique
(act 23's proof, consumed through `zseq_facts`'s injectivity and the marginal lemma). If `Φ_HS` were
an isometry then `d (F (n+1)) (F (n+2)) = d (F n) (F (n+1))` for every `n ≥ 1`, all `F n` being
realizable, and by induction `d (F n) (F (n+1)) = d (F 1) (F 2)` for every `n ≥ 1`. **But** by the
upper bound and item 9, `d (F n) (F (n+1)) = d (F(zs n)) (F(zs (n+1))) ≤ 3 ‖zs (n+1) − zs n‖ =
6 / Real.sqrt ((n² + 1)((n+1)² + 1)) < 6 / (n (n+1))`, which at `n = 300` is below `1/15000`; and
by the lower bound at the cross-invariant coordinate of the product pair `((0,1),(0,0))`,
`d (F 1) (F 2) ≥ (1/16) · ‖zs 1 − zs 2‖ / 256 = ‖i − (3 + 4i)/5‖ / 4096 = Real.sqrt (2/5) / 4096`,
which exceeds `1/7000`. **The failing proposition is isometry on the pair `F 300`, `F 301` against
`F 1`, `F 2`; the separating quantity is the cross-invariant coordinate at `((0,1),(0,0))`.** No
limit is taken; one explicit index suffices, and the freeze's reading names `n = 300`.

### What the discrimination verdicts do and do not depend on

Two of the mechanisms above are recorded, in advance, with their dependence on the choice of
geometry stated exactly, so that the result note can carry the sentence and nothing stronger:

> Merge witnesses are metric-independent once separation is proved. Sequence-discontinuity
> witnesses are invariant across metrics inducing the quotient topology.

`ΦC`, `Φ_PC` and `Φ_MD` send two classes at positive distance to one class; that refutes isometry
for every metric on classes that separates the two, and the separation is act 12's and act 21's.
`ΦCTRL`, `Φ_SC` and `Φ_HS` send inputs whose distance goes below any bound to images whose distance
stays above one; that refutes isometry for every metric inducing the same topology on the
realizable classes, and for no other. **The isometry verdicts of `GEO3` are verdicts about the
frozen `d`**, and this paragraph is what may be said beyond them; whether `d` induces the quotient
topology on the realizable classes is the observation sub-question `GEO1-T` below and enters no
label.

## The countercontrols and the positive controls, one per cell

| target or cell | the route this freeze names | configuration |
| --- | --- | --- |
| `GEO1` (i), invariance | under `G' = c ⋆ G`, each coordinate of `Ψ G'` is the corresponding coordinate of `Ψ G` times `star (c j₁) c j₂ star (c j₂) c j₃ star (c j₃) c j₁ = 1` | arbitrary finite `V` |
| `GEO1` (ii), separation under base-star support | given `Ψ G = Ψ H`, equal diagonals and `G j₀ j₀ j ≠ 0` for every `j`: the coordinate `((j₀, j₀, j₀), (j₀, j₀, j))` gives `‖G j₀ j₀ j‖ = ‖H j₀ j₀ j‖`, so `c j := H j₀ j₀ j / G j₀ j₀ j` has modulus one; the coordinate `((j₀, i, j₀), (j₀, j, k))` — the based triangle `j₀ → j → k → j₀` read in fibres `j₀`, `i`, `j₀` — gives `H j₀ j₀ j · H i j k · H j₀ k j₀ = G j₀ j₀ j · G i j k · G j₀ k j₀`, and with `G j₀ k j₀ = star (G j₀ j₀ k)` by hermiticity of each fibre Gram, `H i j k = star (c j) * G i j k * c k` for every `i`, `j`, `k` | arbitrary finite `V`, a base `j₀` |
| `GEO1` (iii), the full-support instantiation | at each frozen configuration, realizable `G` has, by `sh1_sufficiency` and `fibreGram_apply`, `G i j k = star (U (i,0) (j,0)) * U (i,0) (k,0)` with `‖U (i,0) (j,0)‖ ^ 2 = Γ i j ≠ 0`, so `G 0 0 j ≠ 0` for every `j`; realizable `G`, `H` have equal diagonals `Γ`; (ii) applies | both configurations |
| `GEO1` (iv)–(vi), the metric | `d` is a Euclidean norm of a difference of vectors in `EuclideanSpace ℂ ((V × V × V) × (V × V × V))`, `EuclideanSpace.norm_eq` rewriting the sum; nonnegativity, `d G G = 0`, symmetry and the triangle inequality are the norm's; class-invariance in both arguments from (i); `d G H = 0 → Ψ G = Ψ H` from the norm's definiteness, and then (iii) on realizable tuples; `GramPhaseEquiv G H → d G H = 0` from (i) | (iv), (v), (vi-b) arbitrary `V`; (vi-a) both configurations |
| `GEO2` (a) | for `σ : Equiv.Perm V`, `Ψ (RelabelTransition σ G) p = Ψ G (σ⁶ p)` with `σ⁶` the induced permutation of the index set, so the two sums are reindexed by a bijection and agree: `d (σG) (σH) = d G H` | arbitrary finite `V` |
| `GEO2` (b) | for `L` in `LeftFibreGroup` and `K` a `WeakAnchorStabilizer`, `FibreGram a₀ (L * U * K) i j k = star (c j) * FibreGram a₀ U i j k * c k` by `fibreGram_left_mul` and `fibreGram_mul_weak_apply`, so `GramPhaseEquiv (FibreGram a₀ U) (FibreGram a₀ (L * U * K))` and `d = 0` by `GEO1` (vi-b) | arbitrary finite `V`, `A`, `a₀` |
| `GEO2` (c) | a coordinate of the product carrier's index set is a pair of coordinates of the factors' index sets, and `Ψ (X ⊠ Y) ((a, b)-triples) = Ψ X (a-triples) · Ψ Y (b-triples)` entry by entry, a homogeneous identity of degree three in each factor; hence `∑ ‖Ψ (X' ⊠ Y) − Ψ (X ⊠ Y)‖ ^ 2 = (∑ ‖Ψ X' − Ψ X‖ ^ 2)(∑ ‖Ψ Y‖ ^ 2)` by `Fintype.sum_prod_type` along the index bijection, and `d (X ⊠ Y) (X' ⊠ Y) = d X X' · Real.sqrt (∑ p, ‖Ψ Y p‖ ^ 2)` by `Real.sqrt_mul` | the product carrier, arbitrary factor carriers |
| `GEO3`, each family | the tables above; the perturbation pairs and the shift argument as recorded | each at its own configuration |
| `GEO4` `a0` | from `GEO1`: `d (Φ t G) (Φ t G') = d G G'`, so `GramPhaseEquiv (Φ t G) (Φ t G')` gives `d G G' = 0` by (vi-b) and `GramPhaseEquiv G G'` by (vi-a) | the product configuration |
| `GEO4` `a1` | `Φ_SC`: the prefix through `L4d` and `L5` from `phiSC_corner`, `¬ isometry` from `GEO3` | the product configuration |
| `GEO4` `a3` | `Φ_swap`: the prefix through `L4d` from `phiSwap_l5_restricts`, its `L5` failure from the same, `isometry` from `GEO3` | the product configuration |
| `GEO4` `b₀` | `Φ_conj`: the prefix through `L4d`, `L5` and isometry as analysed, and the cross-invariant `−i/256` against the set `{1/256, i/256}` | the product configuration |
| `GEO4` `a2`, `a4`, `b` | universal attempts, each bounded to the route order below; `UNDECIDED` with the obstruction named is the expected outcome of each | the product configuration |

**Evidence that earns any control or countercontrol**: a Lean theorem at evidence level 2 whose
statement pins the geometry and every family by equation, discharges realizability from merged
results or from the module commit's lemmas, and certifies the separating quantity at a named
coordinate through a named invariant. **Searching and not finding earns nothing.**

## What was and was not run before this freeze

**No drafting-time check of any target's outcome was run.** By the owner's direction this control
plane was drafted from the sealed record alone: no kernel proof, no exact-arithmetic computation of
any invariant or distance, no search for any family's isometry status, and no test of any
construction above was performed. **Every value and every step in the analyses above is the
freeze's reading**, derived by hand from the merged declarations, and the execution is what
establishes or refutes each. A value stated above that the kernel computes differently is a
discrepancy of the freeze's reading, recorded in the result note and not repaired; it changes no
label by itself, the label being earned by what the kernel proves.

**One simulation was run, and it concerns chronology only.** A throwaway worktree at `D` with the
two declarations set to `D` under the stem `OGS` — no Lean file, no guard clause, no record — was
run against the guard at `D`: every one of the eighty-seven `R7-*` tags passed, `R7-OLT`, `R7-OLN`
and `R7-OLG` each classified `ARCHIVED`, reading their own records and nothing of the declaration.
**No contract of any closed round needs superseding for this round to execute**, and the
supersession table below is therefore empty. The simulation's commit exists on no branch of the
repository.

## The ordering obligation, as it binds a gated round whose ladder is consumed

> **The ordering obligation, act 24.** The rungs are act 21's declarations at blob `860daac4…`, the
> equivalence is act 12's at blob `4bba2040…`, and nothing else. The execution's module **states no
> rung, no equivalence, and exactly one top-level definition, `mixedTriple`, with the body this
> freeze displays**; the geometry is bound, in every theorem that names it, to the equation this
> freeze displays, and every family is bound, in every theorem that names it, to the equation its
> merged verdict carries — `Φ_conj` to the entrywise `star`. From the first commit that adds the
> module to the certified head `E`, **no commit of the branch adds a second definition, alters the
> one definition's body, restates a rung, alters the geometry's equation, or uses an equivalence
> outside the frozen quotient list**; the module commit carries no verdict of any target; the
> verdict commits of the executed targets follow it in the order `GEO1`, `GEO2`, `GEO3`, `GEO4`;
> and no theorem block in one family's subsection of `GEO3` names another family.

### What the execution must record

1. **The declaration table.** For `GramPhaseEquiv`, `RealizableGram`, `RelabelTransition`, each
   rung the fourth target's prefix names, and each family, the merged declaration consumed with its
   line range at its blob; and for this round's module the one definition `mixedTriple` with its
   body, and the statement that it carries no other — checked mechanically by `R7-OGS`, which
   requires the module to contain exactly one line beginning with `def `, that line opening
   `def mixedTriple`, no `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`, the
   definition's body equal to the displayed one after whitespace normalization, and the imports
   `OIBridge.OrbitLawGaps`, `OIBridge.OrbitLawRigidityTwisted` and
   `OIBridge.OrbitLawNaturalityFactorization`.
2. **The stage-A commit.** The SHA of the commit that sets the two declarations to `B`, and nothing
   else.
3. **The module commit.** The SHA of the first commit at which the module is present, with the
   definition and the named results it carries, each of which is a shared lemma and none a verdict.
4. **The verdict commits**, in order, each with its SHA and its named results; and, for each target
   the gate did not open, the statement that it has none.
5. **The immutability span.** The statement, with the command that checks it, that between the
   module commit and `E` no diff introduces a definition or touches the one definition:
   `git diff <module commit> <E> -- verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean`
   contains no added or removed line beginning with `def `, `abbrev `, `structure `, `class `,
   `instance `, `axiom ` or `opaque `, and no change inside the definition's block.
6. **The quotient and geometry record.** The only equivalence used in any verdict is act 12's
   `GramPhaseEquiv`; the definition's body and the geometry's equation are the displayed ones at
   every mention; **no equivalence was introduced or widened, and neither the invariant family nor
   the geometry was adjusted**.
7. **The five attestation answers**, one per span, as safeguard 1 fixes them.
8. **The gate record.** For each of `GEO2`, `GEO3`, `GEO4`, the label of the target before it as
   earned, and whether the gate opened.

### The anti-expansion rule, FROZEN

**If execution discovers a thirteenth family, a second invariant family, a second geometry, a
further equivalence, a further rung, a further configuration, a universal implication for a cell
whose witness has closed, a further control, a completeness statement for tuples with zero entries,
or a strengthening of a merged theorem, it is recorded as an observation for a later round with its
own freeze and is not executed here.** The family list is closed at twelve, the invariant family at
the mixed triples, the geometry at one, the quotient list at three, the ladder at act 21's
`L0`–`L5`, the cells at `a0`–`a4`, `b₀` and `b`, and the configurations at act 12's and act 21's.

## The targets, FROZEN

Five targets, `GEO0` through `GEO4`; `GEO0` is type P and is the record check every round of this
programme has carried, and `GEO1`–`GEO4` are the gated bundle. Each names what settles it and what
evidence counts.

### `GEO0` — does the merged record already decide any of the four questions?

**The question.** At `B`, does the merged record contain a statement that a finite family of
phase-invariant products of Gram entries separates act 12's classes, or that a distance on Gram
tuples written from the Gram data does, or that any transition family of the record is or is not
an isometry of any such distance, or that isometry of any such distance follows from or implies any
rung of act 21's ladder?

**What settles it.** Locating and quoting, under act 21's evidence rule at its lines 1456–1467,
over a bounded file set: act 12's `result.md` and module, act 18's `result.md` and module, act 21's
`preregistration.md`, `amendments/amendment-1.md`, `result.md` and module, act 22's
`preregistration.md`, `result.md` and module, act 23's `preregistration.md`, `result.md` and
module, and `verification/ROADMAP.md`, with the terms `metric`, `pseudometric`, `distance`,
`isometr`, `geometr`, `invariant`, `cycle`, `triple`, `Bargmann`, `Hadamard`, `complete`,
`separat`, `Wigner`, `conjugat`, `antiunitar`, `rigid`.

**This is a type-P target.** No Lean is written for it, no outcome of it is a theorem, and this
round's own theorems are not retro-evidence about it. **Reconstructive inference is forbidden as a
finding; where the record is silent, the finding is that it is silent.** This round's own control
plane is inside the set by construction and its hits are recorded as not relevant to the question.
Act 18's `LC2` pseudometric and act 12's cross-invariant are expected to be found, and are recorded
as what they are: one invariant read at one pair, proved not to separate, which decides none of the
four questions.

### `GEO1` — completeness of the mixed triples, and the metric they induce

**The statement.** With `Ψ = mixedTriple` and `d` equal to the displayed equation: (i) for every
finite carrier `V` and all `G H`, `GramPhaseEquiv G H → Ψ G = Ψ H`; (ii) for every finite carrier
`V`, every `j₀ : V` and all `G H` with `∀ i j, G i j j = H i j j` and `∀ j, G j₀ j₀ j ≠ 0`,
`Ψ G = Ψ H → GramPhaseEquiv G H`; (iii) at each of the two frozen configurations, for all
realizable `G H`, `Ψ G = Ψ H → GramPhaseEquiv G H`; (iv) for every finite `V`: `∀ G H, 0 ≤ d G H`,
`∀ G, d G G = 0`, `∀ G H, d G H = d H G`, `∀ G H K, d G K ≤ d G H + d H K`; (v) for every finite
`V`, `∀ G G' H H', GramPhaseEquiv G G' → GramPhaseEquiv H H' → d G H = d G' H'`; (vi-a) at each of
the two frozen configurations, for all realizable `G H`, `d G H = 0 → GramPhaseEquiv G H`; (vi-b)
for every finite `V`, `∀ G H, GramPhaseEquiv G H → d G H = 0`.

**What settles it.** One Lean theorem at evidence level 2, `geo1_triple_metric`, carrying the
conjuncts above, with (vi-a) and (vi-b) as **separate conjuncts** — the equivalence is displayed
nowhere as a single biconditional, each direction having its own witness in the statement, under
`§A.34` — and (ii) and (iii) as separate conjuncts, (iii) being (ii) instantiated at `j₀ = 0` with
the support hypothesis discharged from act 12's merged results. **`GEO1-METRIC` is earned only by
all of (i)–(vi-b) together**; a `Ψ` proved invariant without (ii), or a `d` proved a pseudometric
without (vi-a), earns `GEO1-UNDECIDED` with the missing conjunct named as the obstruction.

**The zero-entry case is out.** No conjunct of `GEO1` asserts completeness for tuples with a
vanishing entry on the base star, at any carrier, and no sentence of this round does either; the
frame literature cited as provenance shows that triples need not suffice there, and this round
asserts nothing about it beyond (ii)'s hypothesis.

**The topology of the induced metric is an observation sub-question, not a conjunct.** Whether the
set of realizable tuples at each frozen configuration is compact and `Ψ` continuous on it, so that
the class space with the metric `d` is compact and `d` induces the quotient topology, is recorded
as `GEO1-T`, with outcome `GEO1-T-HOLDS` or `GEO1-T-UNDECIDED`, **and it does not enter `GEO1`'s
label**; the execution attempts it only after (i)–(vi-b) have closed and only within the `GEO1`
verdict commit.

### `GEO2` — the three controls

**The statement.** (a) For every finite `V`, every `σ : Equiv.Perm V` and every `G H`,
`d (RelabelTransition σ G) (RelabelTransition σ H) = d G H`. (b) For every finite `V`, `A`, anchor
`a₀`, every `U`, every `L` with `LeftFibreGroup L` and every `K` with `WeakAnchorStabilizer a₀ K`,
`d (FibreGram a₀ (L * U * K)) (FibreGram a₀ U) = 0`. (c) For every `X X' : V₁ → Matrix V₁ V₁ ℂ` and
`Y : V₂ → Matrix V₂ V₂ ℂ`: the tensor identity, `∀ a₁ a₂ a₃ b₁ b₂ b₃ j₁ j₂ j₃ k₁ k₂ k₃,
mixedTriple (X ⊠ Y) (((a₁,b₁),(a₂,b₂),(a₃,b₃)), ((j₁,k₁),(j₂,k₂),(j₃,k₃))) = mixedTriple X
((a₁,a₂,a₃),(j₁,j₂,j₃)) * mixedTriple Y ((b₁,b₂,b₃),(k₁,k₂,k₃))`, and its consequence
`d (X ⊠ Y) (X' ⊠ Y) = d X X' · Real.sqrt (∑ p, ‖mixedTriple Y p‖ ^ 2)`, with `d` on each carrier
bound to the displayed equation on that carrier and `⊠` written out.

**What settles it.** Three Lean theorems at evidence level 2, `geo2_relabel_isometry`,
`geo2_twoSided_trivial`, `geo2_product_tensor`. **`GEO2-CONTROLS-PASS` is earned only by all three
together**, (c) with both its identity and its consequence. `GEO2-CONTROL-FAILS` is earned only by
an exhibited instance on the frozen objects at which one of (a), (b), (c) fails, with the instance
named; `GEO2-UNDECIDED` otherwise.

### `GEO3` — the twelve families against the geometry

**The statement.** For each of the twelve families, at its own configuration, with `d` and the
family bound by equation: **either** the isometry proposition, **or** its negation with the pair
and the separating quantity named.

**What settles it.** Twelve Lean theorems at evidence level 2, one per family, each named
`geo3_<family>_isometry` or `geo3_<family>_not_isometry` for the outcome reached — `phiI`, `phiP`,
`phiC`, `phiT`, `phiPP`, `phiCTRL`, `phiSwap`, `phiMD`, `phiPC`, `phiHS`, `phiSC`, `phiConj` — each
in its own subsection of the module's `GEO3` section, naming no other family. **Every family is
tested; no family's verdict is inferred from another's.**

**The label.** `GEO3-DISCRIMINATES` is earned iff at least one of `ΦCTRL`, `Φ_SC` — the two
families of the list that satisfy the prefix through `L4d` and are predicted non-isometries — is
**proved** not an isometry. `GEO3-NO-DISCRIMINATION` is earned iff both `ΦCTRL` and `Φ_SC` are
**proved** isometries. `GEO3-UNDECIDED` otherwise. The other ten families' verdicts are carried in
the census table of the result note with their own frozen sentences and **do not enter the label**:
the families that fail a rung of the prefix are not structurally admissible, and their
non-isometry, if proved, discriminates within a class the ladder already excludes; the relabellings
and the conjugation are predicted isometries, and their isometry, if proved, is the positive side
of the same test.

### `GEO4` — the rigidity attempt and the implication cells

**The statement.** At the product configuration, the seven propositions of the implication
matrix, each stated with the prefix written out as the first seven conjuncts of `LadderConds`, `L5`
as `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀)
(fun _ => Γ₀) Γ Φ`, `L4n` as the eighth conjunct, and isometry as the displayed proposition.

**What settles it.** For `a0`: one Lean theorem `geo4_a0_isometry_injective`, universal. For
`a1`: `geo4_a1_l5_not_implies_geo`, refuting `∀ Φ, prefix → L5 → isometry` by instantiation at
`Φ_SC`, the quantifier ranging over every transition family on `Fin 4 × Fin 4`. For `a3`:
`geo4_a3_geo_not_implies_l5`, refuting `∀ Φ, prefix → isometry → L5` at `Φ_swap`. For `b₀`:
`geo4_b0_not_relabel_rigid`, refuting `∀ Φ, prefix → L5 → isometry → ∀ t, ∃ σ, ∀ G, RealizableGram
… G → GramPhaseEquiv (Φ t G) (RelabelTransition σ G)` at `Φ_conj`, with `Φ_conj`'s prefix, `L5` and
isometry conjuncts discharged in the same theorem. For `a2`, `a4` and `b`: the universal statements
`geo4_a2_l4n_implies_geo`, `geo4_a4_geo_implies_l4n`, `geo4_b_rigid`, each attempted only after the
three witness cells have closed, each `UNDECIDED` with its obstruction named if not obtained.

**The label is earned by `b` alone**: `GEO4-RIGID` by `geo4_b_rigid` at evidence level 2;
`GEO4-UNDECIDED` otherwise, with the obstruction named. No family on the frozen list is predicted to
satisfy `b`'s hypotheses and fail its conclusion, so **no `NOT-RIGID` label exists for `b`**; if a
family unexpectedly does, that is recorded as an observation under the anti-expansion rule and `b`
is `UNDECIDED`. The cells `a0`–`a4` and `b₀` are sub-verdicts, each with its own frozen sentence.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `GEO0` | **negative** — the record decides none of the four | **high** | Act 18's pseudometric and act 12's cross-invariant are the only phase-invariant quantities on the orbit space the record carries, and act 18 proves the former does not separate; no completeness statement and no isometry statement about any law exists on the record. The finding is whatever the bounded search records. |
| `GEO1` | **`GEO1-METRIC`** | **high** | Invariance is a one-line cancellation at every coordinate; separation at full support is a gauge fixing along one star and one triangle per entry, with no graph argument; the full-support fact is act 12's sufficiency read at `|A| = 1`; the metric properties are those of a Euclidean norm. **UNDECIDED with the obstruction named is an allowed outcome**; `GEO1-T` is predicted `HOLDS` at medium strength and enters no label. |
| `GEO2` | **`GEO2-CONTROLS-PASS`** | **high** | (a) is a reindexing of one finite sum along a bijection of the index set; (b) is two merged laws and `GEO1`; (c) is an entrywise identity of monomials and one product of sums. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `GEO3` | **`GEO3-DISCRIMINATES`**, via `ΦCTRL` and `Φ_SC`, with the census as the family tables predict | **medium** | The two perturbation arguments rest on the entry bound at a symbolic parameter, the sequence identities and the marginal lemma, all elementary but new kernel work; the relabelling isometries are `GEO2` (a); the shift argument is an induction plus two explicit bounds. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `GEO4` | **`GEO4-UNDECIDED`**, with `a0` **holds**, `a1` **NOT-IMPLIES**, `a2` **UNDECIDED**, `a3` **NOT-IMPLIES**, `a4` **UNDECIDED**, `b₀` **NOT-RIGID** | **medium** for the cells, **high** for `b` being undecided | `a0` is separation; `a1` and `a3` consume closed verdicts; `b₀`'s witness is an involution whose every conjunct is a computation; `a2`, `a4` and `b` are universal statements about every transition family for which the freeze knows no route. **`GEO4-RIGID` is predicted for no cell and is not expected.** |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
**UNDECIDED is a live preregistered outcome for every target and is not a failure, and
NOT-EXECUTED is a live preregistered outcome for every gated target and is not a failure.**

### The outcomes of `GEO0`

- **Outcome `GEO0`-silent:**
  > On the search this freeze bounds — act 12's, act 18's, act 21's, act 22's and act 23's control
  > planes, amendments, result notes and modules, and `verification/ROADMAP.md`, against the frozen
  > term list — the merged record carries one phase-invariant quantity read at one fibre pair, act
  > 12's cross-invariant, and one geometry built from it, act 18's pseudometric, proved there not to
  > separate act 12's classes, and decides neither whether a finite family of such quantities
  > separates them, nor whether a distance written from the Gram data does, nor whether any
  > transition family of the record is an isometry of any such distance, nor whether such isometry
  > follows from or implies any rung of act 21's ladder. **The finding is that the record is silent
  > on the point.** It is not a finding that any such statement is false, not a finding that one is
  > unprovable, and not a bound on what a later round could prove.
- **Outcome `GEO0`-found:**
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which
  > objects. No merged artifact is edited, and no earlier round's recording is enlarged or corrected.

### The outcomes of `GEO1`

- **Outcome `GEO1-METRIC`:**
  > The mixed-triple feature map — every product of three Gram entries around a closed three-step
  > walk of matrix indices, with a fibre label per step — is invariant under act 12's phase action at
  > every finite carrier, and separates act 12's classes on every pair of tuples with equal diagonals
  > and no vanishing entry on one base star, hence on the realizable tuples at both frozen
  > configurations, where no entry vanishes; and the Euclidean distance of feature vectors is a
  > metric on classes: nonnegative, symmetric, subadditive, constant on each class in both
  > arguments, and zero exactly on the pairs `GramPhaseEquiv` relates on the realizable tuples, each
  > direction of the last proved separately, at evidence level 2. **This is a statement about the
  > exact family and the exact quantity frozen under these names**: it does not say the family is
  > minimal, canonical or physical, does not say the induced metric is canonical or the right
  > geometry to impose, says nothing about tuples with a vanishing entry, and adopts nothing.
- **Outcome `GEO1-UNDECIDED`:**
  > Whether the mixed-triple feature map separates act 12's classes on the realizable tuples at the
  > frozen configurations, and whether the distance it induces is a metric on classes, is undecided
  > in this round, with the obstruction named specifically — the conjunct, the step at which the
  > proof stopped, and what would settle it. Neither the metric label nor its negation is claimed,
  > and the later targets of this round were not executed.

### The outcomes of `GEO2`

- **Outcome `GEO2-CONTROLS-PASS`:**
  > Every carrier relabelling is an exact isometry of the geometry, act 12's two-sided gauge acts
  > trivially on it, and the feature map carries the product embedding to the tensor product of the
  > factors' feature vectors, so that the distance between two products with a common second factor
  > is the factors' distance scaled exactly by the common factor's feature norm, at evidence level 2.
  > **This is a statement about three named constructions of the record and the exact quantity
  > frozen**; it says nothing about constructions not on the list and does not say the geometry is
  > preserved by anything else.
- **Outcome `GEO2-CONTROL-FAILS`:**
  > A named control of the record fails to preserve the geometry at an exhibited instance, at
  > evidence level 2, with the control and the instance named. **This settles that the frozen
  > geometry is not the object the record's legitimate constructions preserve**, and the later
  > targets of this round were not executed; it says nothing about any other geometry.
- **Outcome `GEO2-UNDECIDED`:**
  > Whether the record's three named constructions preserve the geometry is undecided in this round,
  > with the obstruction named specifically — the control, the step, and what would settle it.
  > Neither label is claimed, and the later targets of this round were not executed.
- **Outcome `GEO2-NOT-EXECUTED`:**
  > The controls were not executed, `GEO1` not having reached its metric label; no sentence of this
  > round reports anything about them.

### The outcomes of `GEO3`

- **Outcome `GEO3-DISCRIMINATES`:**
  > The geometry discriminates within the structurally admissible class: an exhibited transition
  > family satisfying every condition of act 21's ladder before naturality, named for this target in
  > advance, is not an isometry of it on realizable tuples, at evidence level 2, with the pair and
  > the separating quantity named; and every family of the frozen list is recorded with its own
  > verdict. **This is a statement about the exact families and the exact quantity frozen**: it does
  > not say isometry is the right condition to impose, does not say any family is excluded from
  > anything by it, and does not adopt the geometry as a selector.
- **Outcome `GEO3-NO-DISCRIMINATION`:**
  > Both structurally admissible families of the frozen list predicted not to be isometries are
  > isometries of the geometry, at evidence level 2. **The frozen geometry does not discriminate
  > within the structurally admissible class on this list**, and the rigidity target was not
  > executed; this says nothing about families not on the list and nothing about any other geometry.
- **Outcome `GEO3-UNDECIDED`:**
  > Whether the geometry discriminates within the structurally admissible class is undecided in this
  > round, with the obstruction named specifically — the family, the step, and what would settle it
  > — and every family of the frozen list is recorded with its own verdict. Neither label is
  > claimed, and the rigidity target was not executed.
- **Outcome `GEO3-NOT-EXECUTED`:**
  > The families were not tested against the geometry, `GEO2` not having reached its controls label;
  > no sentence of this round reports anything about any family's isometry status.
- **Outcome `Φ`-ISOMETRY**, for a named family `Φ`:
  > The transition family named `Φ` is an isometry of the geometry on realizable tuples at the
  > configuration its merged verdict is stated at, at evidence level 2. **This is a statement about
  > the exact family frozen under that label**, and it does **not** endorse it, does **not** say it
  > obtains, and does **not** adopt it as the physical law of evolution.
- **Outcome `Φ`-NOT-ISOMETRY**, for a named family `Φ`:
  > The transition family named `Φ` is not an isometry of the geometry on realizable tuples at the
  > configuration its merged verdict is stated at, at evidence level 2, with the pair and the
  > separating quantity named. **This settles that family against that proposition and nothing in its
  > neighbourhood**, and it is not a statement that families of its shape fail in general.
- **Outcome `Φ`-UNDECIDED**, for a named family `Φ`:
  > Whether `Φ` is an isometry of the geometry is undecided in this round, with the obstruction named
  > specifically — the family, the step and what would settle it. Neither label is claimed.

### The outcomes of `GEO4`, and of its cells

- **Outcome `GEO4-RIGID`:**
  > Every transition family satisfying the conditions of act 21's ladder before naturality,
  > factorization for the ordered decomposition, and isometry of the geometry on realizable tuples,
  > acts on realizable classes at every time as one carrier relabelling or as one carrier relabelling
  > composed with entrywise conjugation, proved universally at evidence level 2 at the frozen product
  > configuration. **This is a statement about the exact hypotheses at the exact configuration**: it
  > does not say the conclusion is unitary, antiunitary or quantum, does not say any hypothesis is
  > the right condition to impose, and changes no verdict of any earlier act.
- **Outcome `GEO4-UNDECIDED`:**
  > Whether the conditions of act 21's ladder before naturality, factorization and isometry of the
  > geometry force a law to act on realizable classes as a carrier relabelling or as one composed with
  > entrywise conjugation is undecided in this round, with the obstruction named specifically — the
  > step of the universal attempt that did not close and what would settle it. Neither the rigidity
  > label nor its negation is claimed; the absence of a proof is not a counterexample.
- **Outcome `GEO4-NOT-EXECUTED`:**
  > The rigidity implication was not attempted, `GEO3` not having reached its discrimination label;
  > no sentence of this round reports anything about it or about any implication cell.
- **Cell `a0`, holds:**
  > Isometry of the geometry on realizable tuples implies injectivity on realizable classes, at
  > evidence level 2, by separation; the converse is not asked.
- **Cell `a1`, `NOT-IMPLIES`:**
  > At the frozen product configuration, the conditions before naturality together with
  > factorization do not imply isometry of the geometry: an exhibited family, named for this cell in
  > advance, satisfies every one of them and is not an isometry, at evidence level 2. No independence
  > of isometry and factorization is asserted.
- **Cell `a3`, `NOT-IMPLIES`:**
  > At the frozen product configuration, the conditions before naturality together with isometry of
  > the geometry do not imply factorization: an exhibited family, named for this cell in advance,
  > satisfies every one of them and does not factorize, at evidence level 2. No independence of
  > isometry and factorization is asserted.
- **Cell `b₀`, `NOT-RIGID`:**
  > At the frozen product configuration, the conditions before naturality, factorization and isometry
  > of the geometry do not force a law to act on realizable classes as a carrier relabelling: an
  > exhibited family, named for this cell in advance, satisfies every one of them and sends one named
  > realizable class to a class no relabelling reaches, at evidence level 2, with the separating
  > invariant named. **This is a statement about the relabelling conclusion alone**; nothing here
  > calls the witness antiunitary, a symmetry, or a candidate for anything.
- **Cell `a2` or `a4`, `IMPLIES`:**
  > At the frozen product configuration, the conditions before naturality together with the named
  > hypothesis imply the named conclusion, proved universally at evidence level 2. This is a
  > statement about the exact declarations at the exact configuration and endorses no condition.
- **Cell `a1`, `a3` or `b₀`, `UNDECIDED`, and cell `a2`, `a4` or `a0`, `UNDECIDED`:**
  > The cell is undecided in this round, with the obstruction named specifically — which conjunct of
  > the named witness did not close and at which step, or which step of the universal attempt did
  > not close. Neither label is claimed; the absence of an exhibited counterexample is not a proof of
  > the implication, and the absence of a proof is not a counterexample.

### The outcome-vector table — every admissible headline under the gate

The headline is one row of this table, verbatim, in this rendering: **Outcome vector:** followed by
the four labels in target order, separated by ` · `. Each row is admissible; the execution selects
the row its verdicts and the gate compose and reports no other wording. **There are seven rows and
no others**; every other combination of labels is excluded by failure rule 3.

| # | vector |
| --- | --- |
| 1 | **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-DISCRIMINATES` · `GEO4-RIGID` |
| 2 | **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-DISCRIMINATES` · `GEO4-UNDECIDED` |
| 3 | **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-NO-DISCRIMINATION` · `GEO4-NOT-EXECUTED` |
| 4 | **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROLS-PASS` · `GEO3-UNDECIDED` · `GEO4-NOT-EXECUTED` |
| 5 | **Outcome vector:** `GEO1-METRIC` · `GEO2-CONTROL-FAILS` · `GEO3-NOT-EXECUTED` · `GEO4-NOT-EXECUTED` |
| 6 | **Outcome vector:** `GEO1-METRIC` · `GEO2-UNDECIDED` · `GEO3-NOT-EXECUTED` · `GEO4-NOT-EXECUTED` |
| 7 | **Outcome vector:** `GEO1-UNDECIDED` · `GEO2-NOT-EXECUTED` · `GEO3-NOT-EXECUTED` · `GEO4-NOT-EXECUTED` |

**The predicted row is row 2.**

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The execution appends,
after act 23's sentence in the same cell, exactly the sentence frozen for the vector reached.

**Case A — `GEO0` silent, row 2 with the cells as predicted.** This is the case the freeze predicts.

> Act 24 tests, in one gated round with four separately frozen targets, whether a finite family of phase invariants written from the Gram data alone — every product of three Gram entries around a closed three-step walk of matrix indices, with a fibre label per step — separates act 12's classes on the realizable tuples, whether the record's legitimate constructions preserve the distance it induces, whether that distance tells the record's structurally admissible laws apart, and whether, together with every condition of act 21's ladder before naturality and with factorization, isometry of it forces a law to act on classes as a carrier relabelling, at act 12's and act 21's frozen configurations, with a closed list of twelve named laws frozen with it. The family separates the classes on the realizable tuples at both configurations, where no entry vanishes, and the Euclidean distance of feature vectors is a metric on classes: nonnegative, symmetric, subadditive, constant on each class in both arguments, and zero exactly on act 12's equivalent pairs. Every carrier relabelling is an exact isometry of it, act 12's two-sided gauge acts trivially on it, and the product embedding with a common second factor scales it exactly by the common factor's feature norm. The geometry discriminates within the structurally admissible class: a law satisfying every condition before naturality and factorizing, and a law satisfying every condition before naturality and conditioning one factor on the other, each named for that target in advance, are not isometries of it, while every relabelling law of the record is one. Whether every law satisfying the conditions before naturality, factorization and isometry acts on classes as a carrier relabelling or as one composed with entrywise conjugation is recorded undecided, with the obstruction named; the entrywise conjugation, named in advance, satisfies every condition before naturality, factorizes, is an isometry, and sends one admissible class to a class no relabelling reaches, so the relabelling conclusion alone is not forced; isometry implies injectivity on classes; and the conditions before naturality with factorization do not force isometry, nor with isometry force factorization. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another; no condition is adopted; the invariant family and its geometry are named objects of test and are not adopted as the physical ones; nothing is asserted about tuples with a vanishing entry; acts 12 through 23's own verdicts stand exactly as they state them; nothing here introduces continuity, composition in time or a generator; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

**Clauses of Case A vary with the outcome, and they vary independently within the gate**, each
replaced by the sentence its target's other outcomes fix:

| target or cell | clause | replacement |
| --- | --- | --- |
| `GEO1`, `UNDECIDED` | the sentence beginning "The family separates the classes" and **every sentence after it up to** "Each verdict is" | "Whether the family separates act 12's classes on the realizable tuples at the frozen configurations, and whether the distance it induces is a metric on classes, is recorded undecided, with the obstruction named, and the later targets were not executed." |
| `GEO2`, `CONTROL-FAILS` | the sentence beginning "Every carrier relabelling" and every sentence after it up to "Each verdict is" | "A named construction of the record does not preserve the distance, at an exhibited instance, and the later targets were not executed." |
| `GEO2`, `UNDECIDED` | the same span | "Whether the record's named constructions preserve the distance is recorded undecided, with the obstruction named, and the later targets were not executed." |
| `GEO3`, `NO-DISCRIMINATION` | the sentence beginning "The geometry discriminates" and every sentence after it up to "Each verdict is" | "Both structurally admissible laws of the frozen list predicted not to be isometries are isometries of it, so the geometry does not discriminate within the structurally admissible class on this list, and the rigidity target was not executed." |
| `GEO3`, `UNDECIDED` | the same span | "Whether the geometry discriminates within the structurally admissible class is recorded undecided, with the obstruction named, and the rigidity target was not executed." |
| `GEO3`, `DISCRIMINATES` by one of the two families only | the clause "a law satisfying every condition before naturality and factorizing, and a law satisfying every condition before naturality and conditioning one factor on the other, each named for that target in advance, are not isometries of it" | the clause naming only the family proved, "a law satisfying every condition before naturality and factorizing, named for that target in advance, is not an isometry of it" or "a law satisfying every condition before naturality and conditioning one factor on the other, named for that target in advance, is not an isometry of it", with the other family's outcome recorded in the census |
| `GEO4`, `RIGID` | the sentence beginning "Whether every law satisfying" | "Every law satisfying the conditions before naturality, factorization and isometry acts on classes as a carrier relabelling or as one composed with entrywise conjugation, proved universally at that configuration; the entrywise conjugation, named in advance, satisfies every condition before naturality, factorizes, is an isometry, and sends one admissible class to a class no relabelling reaches, so the relabelling conclusion alone is not forced; isometry implies injectivity on classes; and the conditions before naturality with factorization do not force isometry, nor with isometry force factorization." |
| cell `b₀`, `UNDECIDED` | the clause "the entrywise conjugation, named in advance, satisfies every condition before naturality, factorizes, is an isometry, and sends one admissible class to a class no relabelling reaches, so the relabelling conclusion alone is not forced" | "whether the relabelling conclusion alone is forced is recorded undecided, with the obstruction named" |
| cell `a0`, `UNDECIDED` | the clause "isometry implies injectivity on classes" | "whether isometry implies injectivity on classes is recorded undecided" |
| cell `a1`, `UNDECIDED` | the clause "the conditions before naturality with factorization do not force isometry" | "whether the conditions before naturality with factorization force isometry is recorded undecided" |
| cell `a3`, `UNDECIDED` | the clause "nor with isometry force factorization" | "and whether they with isometry force factorization is recorded undecided" |
| cell `a2`, `IMPLIES` | appended after the `a3` clause | "; the conditions before naturality with the lift condition force isometry, proved universally" |
| cell `a4`, `IMPLIES` | appended after the `a3` clause | "; the conditions before naturality with isometry force the lift condition, proved universally" |

**The execution composes the sentence from these substitutions and reports no other wording. No
composition closes `P0`**, and none reports either of its two parts closed.

## Naming a law or a geometry is not endorsing it, FROZEN

Act 21's four points at its lines 1868–1879 govern here, read of the invariant family and the
geometry as well as of every law: naming is for testing; the round endorses none; exclusion is only
ever of the precise stated form; the lists are closed at this freeze.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a law's survival, or the geometry's success, could be read as its
adoption**, each carriage opening with one line naming where it is being carried. It is act 21's
clause with "Act 21" read as "Act 24", and nothing else changed.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

**Read of the geometry**: a completeness verdict, a controls verdict and a discrimination verdict
are statements about the frozen family and the frozen quantity; none adopts either as a selector, a
principle or a piece of physics, and "the geometry is preserved by" is never written as "the
geometry selects".

## What no outcome licenses

These are the forbidden sentences, in terms. None may be written in any artifact of this round, in
any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"This is Schrödinger evolution", "the isometries are the unitaries", "the conjugation is the
   antiunitary case", "Wigner's theorem holds on the orbit space", or any statement that a
   surviving or failing law, or the geometry, is, resembles, approximates or points toward quantum
   evolution, unitarity or a quantum symmetry.** `Φ_conj` is named as the entrywise conjugation and
   as nothing else; the Wigner-type shape is provenance for the question's shape and for nothing
   else.
2. **"The surviving law is the physical one", "the geometry is the physical geometry", "the
   geometry selects".** The non-adoption clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
3. **"Isometry and factorization are independent", "isometry and the lift condition are
   independent", "the square is complete", or any report of independences.** Cells are cells.
4. **"`GEO3` follows from `GEO2`", "the rigidity follows from discrimination", or any inference of
   one target's verdict from another's**, beyond the consumptions the freeze itself places in cells
   `a1` and `a3` and in `GEO3`'s upper bound.
5. **"The family is complete", "the controls pass", "the geometry discriminates", "the rigidity
   holds", from the absence of a counterexample, from a witness that failed to close, or from
   anything but the named route.**
6. **"The witness for one cell also settles another."** A witness answers the cell the matrix
   authorizes and no other.
7. **"Act 21's census was wrong", "act 23's `Φ_SC` is now excluded", "act 22's swap witness shows
   …", or any rewriting or reinterpretation of any earlier act's verdict or witness.** They stand;
   this round's verdicts are about the geometry alone.
8. **"The geometry excludes `ΦCTRL`", "the geometry excludes `Φ_SC`", read as a physical or
   programme statement.** A non-isometry is a fact about one map and one distance; nothing is
   excluded from anything by it.
9. **"The isometry group of the orbit space is …", "the isometries are exactly the relabellings
   and conjugations", or any characterization of the isometries** beyond the twelve verdicts and the
   `b` cell's outcome.
10. **"`d` is the natural metric", "the canonical metric", "the unique metric", "the Fubini–Study
    metric", "the Bures metric", or any identification of the frozen geometry with a named
    geometry of any other theory.** No comparison is made and none is licensed. Citing the
    Bargmann-invariant, frame-equivalence and complex-Hadamard literature as the provenance of the
    route, as the external-provenance section does, is not an identification and is permitted in
    that section's wording only.
11. **"This is the Chien–Waldron theorem on our object", "the Haagerup invariant is complete",
    "the triples are complete in general", or any attribution of a theorem of this round to the
    literature, or any completeness claim beyond the base-star support hypothesis.** The tuple
    generalization is this round's and is proved here; completeness with zero entries is out.
12. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate; about act 16's cancellation cell; about act 14's carriers; about act 18's
    `D`-axis; about act 10's anchor axis; about Track I, Source B or Source C; or about the substratum
    Lemma 24.1 rounds.**
13. **"`P0` is closed", or "`P0`'s trajectory part is closed."**
14. **"Act 12's classification is strengthened", "act 18's pseudometric is superseded", "act 21's
    ladder is extended by a rung", "act 23's family is extended."** All are consumed at merged
    strength; the invariant family and the geometry are this round's objects of test and no rung;
    the entry bound, the coordinate bound, the feature norm and the rotated point are this round's
    supply items and enlarge no merged statement.
15. **"The evolution is continuous", "smooth", "generated", "one-parameter", "composes in time"**,
    or any statement resting on structure the index type does not carry; in particular nothing about
    the parameter of the Fourier family being a time, a flow or a generator, and nothing about the
    perturbation index `N` being a limit.
16. **"OI and QM are inequivalent."**
17. **"The law list is exhaustive", "the control list is exhaustive", "the invariant family is the
    only complete one."** Twelve laws, three controls and one family are tested; nothing outside
    them is refuted or endorsed here.
18. **A single-label headline.** The headline is the vector, selected verbatim from the table.
19. **"`Φ_conj` is admissible as a law", "`Φ_conj` survives the ladder".** Its conjuncts are
    discharged for cell `b₀`'s hypotheses and for `GEO3`'s isometry test, and its `L4n` status is
    neither tested nor reported.
20. **"The discrimination verdicts are metric-independent"**, without the two qualifications the
    freeze fixes: merge witnesses once separation is proved, sequence-discontinuity witnesses across
    metrics inducing the quotient topology, and `GEO1-T` entering no label.

## Named hazards

1. **A perturbation pair one of whose members fires, or is not realizable.** **This is the round's
   own hazard.** Each of the `ΦCTRL` and `Φ_SC` pairs rests on the marginal lemma and `zs n ≠ 1`
   for the non-firing member and on `product_realizable` for both; a pair that fails either earns
   nothing and takes failure rule 2's fallback.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
2. **Adjusting the invariant family or the geometry.** A family of based triples only, a family
   with a different walk length, a `sup` in place of the Euclidean norm, or a squared distance in
   place of the square root is a different object; the definition's body and the geometry's
   equation are pinned by the guard, and a variant is not `Ψ` or `d`. In particular a family of
   triples through one base vertex is **not** relabelling-equivariant and would fail control (a);
   the whole index set is what makes (a) a permutation.
3. **A second definition.** The budget is one; `R7-OGS` fails on a second `def` and on any edit to
   the one definition's body.
4. **The Frobenius instance.** Mathlib's `Matrix` Frobenius norm is a scoped instance; a statement
   that reaches for `‖·‖` on a matrix has changed the object. Every norm in every statement is on
   an entry of `ℂ` or on a vector of `EuclideanSpace`, and every sum is written out.
5. **Attributing the completeness theorem, or importing one.** The frame literature's theorem is
   for one Gram matrix and is cited as provenance only; the tuple statement with the shared phase
   is proved here from the based-star gauge fixing, and no result of that literature is consumed.
6. **Completeness asserted past its hypothesis.** Conjunct (ii) needs `G j₀ j₀ j ≠ 0` for every
   `j`; a tuple with a vanishing entry on the base star is outside every completeness statement of
   this round, and the frame literature's `n`-cycle example is the reason. At the frozen
   configurations the hypothesis is discharged from rank one; nothing is asserted at `|A| > 1`.
7. **Raw coordinates mistaken for gauge invariants with signs.** The raw coordinates of
   `Ψ (Gᵢ ⊠ G₁)` take every value in `{±1/4096, ±i/4096}`, so a `b₀` argument on raw coordinates
   would not separate; the argument runs on the cross-invariant coordinates, which are `Γ` times a
   value in `{1/256, i/256}` on every relabelling, and on nothing else.
8. **The `z`-free entries assumed `z`-free.** The entries of `F(z)` in which `z` pairs with
   `star z` are constant only because `star z * z = 1`; the entry bound is stated at unit
   parameters and proved by cases, not by inspection.
9. **Inferring a family's verdict from another's.** Twelve theorems; the relabellings' isometries
   are instances of `GEO2` (a) and are still stated and proved one by one.
10. **Sliding a witness.** `Φ_SC` answers `GEO3` and cell `a1`; `Φ_swap` answers `GEO3` and cell
    `a3`; `Φ_conj` answers `GEO3` and cell `b₀`; none answers anything else, and `Φ_conj`'s `L4n`
    status is not a verdict.
11. **A universal proof attempted while a witness is open.** The route order is witness cells
    first; a universal attempt on `a2`, `a4` or `b` before `a1`, `a3` and `b₀` have closed at a
    named step is a discrepancy.
12. **A verdict revealed before its commit.** The attestation set at every boundary and the
    partial-fact rule exist for it; a shared lemma of the module commit that states a family's
    isometry is a YES at the first boundary.
13. **A verdict commit carrying two targets.** One per executed target, in order.
14. **Executing a closed target "for information".** Failure rule 3; a closed target's route is not
    run, and a partial result on it is a discrepancy and not an observation.
15. **`GEO3-DISCRIMINATES` earned by a family outside the prefix.** `ΦC`, `Φ_MD`, `Φ_PC` and
    `Φ_HS` each fail a rung of the prefix; their non-isometries are census entries and earn the
    label of nothing.
16. **Reading `b₀`'s witness as a symmetry, an antiunitary or a physical map.** Forbidden sentence
    1; it is the entrywise `star` and nothing else is said of it.
17. **Choosing a configuration or an index after an outcome is known.** Every family is at its
    merged configuration; the perturbation index is `N = 32768` and the shift index `n = 300`; a
    pair that works at a different index is an observation, not a repair — with one stated
    exception: if the kernel's bounds at the frozen indices are weaker than the freeze's reading
    and a larger index closes the same argument, the larger index is a discrepancy of the reading
    recorded and used, since the argument is the same and the index is not a parameter of the law.
18. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.**
    Carried from acts 18, 21, 22 and 23; and here it is also the case that makes the triples
    complete.
19. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
20. **A landing without `P`**, **a stem both declared and recorded**, **a legacy constant
    written**, **editing this freeze after an outcome is known**, **a supersession outside the
    table** — each as act 21's hazards 28, 30, 31 and 34 state them, with `OGS` for `OLT`; the
    table here is empty, so any edit to a closed round's guard is a supersession outside it.
21. **A `B`-scoped precondition that the freeze's own text falsifies.** Every `B`-scoped row below
    is evaluated at `M` before the merge and is written so that the presence of this file in the
    tree does not fail it.
22. **A value in the freeze's reading that the kernel computes differently.** Recorded as a
    discrepancy of the reading; the label is earned by what the kernel proves and by nothing stated
    here.

## Non-doings

The round does not: **derive, recognise, approach or claim progress toward quantum evolution**, in
any paraphrase; adopt any surviving law as the physical one; adopt the invariant family or the
geometry as a selector, a principle, or the physical geometry, or identify either with any named
geometry or invariant of any other theory; attribute any theorem of this round to the literature it
cites as provenance, or consume any theorem of that literature; assert completeness for any tuple
with a vanishing entry on the base star, or at any `|A| > 1`; adopt a carrier as the physical one
or define a carrier of its own; endorse any condition, any law, the family or the geometry; assert
or deny that a cross-time law is required or suffices; **restate, edit, add or remove any rung, or
change any conjunction**; **introduce or widen an equivalence**, or use one outside the frozen
quotient list in any verdict; **define anything beyond the one budgeted definition**; test any
family outside the frozen twelve, any invariant family or geometry outside the frozen one, any
control outside the frozen three, any configuration outside the frozen two, or any decomposition
other than `e = Equiv.refl`; infer any target's verdict from another's beyond the consumptions the
freeze places; report an independence of conditions or a square of independences; characterize
the isometries of the orbit space; attempt a characterization, a census of the ladder or a
same-initial-orbit pair; **re-prove or strengthen acts 12, 13, 17, 18, 20, 21, 22 or 23**; revise
any merged label; rewrite, reinterpret or grade any verdict or witness of any earlier act's note;
ask the threading question or the cross-time representative question, in either direction; touch
act 16's cancellation cell; state anything about act 18's `D`-axis, act 10's anchor axis, act 14's
carriers, Track I, Source B or Source C, or the substratum Lemma 24.1 rounds; realize any transition
as an operator, unitary, antiunitary, generator or group element; **introduce continuity,
smoothness, composition in time, a semigroup law or a generated evolution**; alter any existing
manifest record, supersede any closed round's contract, or write a legacy seal constant; edit any
manuscript; close `P0` or either of its parts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Act 21's statement at its lines 2130–2143 is carried in full: the question is not asked, not
bounded and not attempted; an execution that begins asking whether any law here looks like unitary
evolution, or whether the geometry looks like a quantum geometry, has left the round's scope, and
what it finds is recorded as an observation and not executed. **"Resembles", "is consistent with",
"is what one would expect from" and "is a step toward" are forbidden sentences.** The word "Wigner"
appears in this file only in the external-provenance section, the forbidden list and `GEO0`'s term
list, and appears in no other artifact of the round.

### What act 24 does and does not change about `P0`, and about the classification

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 24 can
change is the recorded content of one invariant family and the geometry it induces on the
per-slice orbit space, the recorded isometry status of twelve named laws under it, and the recorded
status of seven implication and rigidity propositions among act 21's rungs and that geometry.

**On the classification act 21 named as the obstruction to `L-FAMILY`, stated once and narrowly.**
A family proved not an isometry is a law a classification of the isometries at the product
configuration must **exclude**, modulo the frozen law equivalence; a family proved an isometry is
one such a classification must **account for**. **These results place no inclusion requirement on
the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`, and no requirement that any
parameter set contain any group or any family.** That is the whole of what this round's outcomes
bear on, and it is an observation for the later round that freezes the classification, not a
finding of this one.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about
what fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT
CERTIFIED**.

## Definition budget

**The execution introduces exactly ONE top-level Lean definition, `mixedTriple`, with the body this
freeze displays.** The budget is **one**, and it is stated as a number so that it cannot drift: one
`def`, and no `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`. The one definition is
budgeted because the invariant family is the object every verdict of the round is about and every
coordinate of it is read in every target; its body is pinned verbatim by the guard, so that the
definition is as immutable as an equation-bound object would be. Everything else — the geometry,
the isometry proposition, every rung as act 21's declaration consumed, the twelve families, the
Fourier family, the sequence and its rotation, the product tuples, the Hadamard objects and the
permutations — is a bound variable pinned by equation in the statements that need it, as
`lc2_regularity_law` pins its pseudometric and as `phiCTRL_census` pins its transition family. The
prefix through `L4d` is written out as the first seven conjuncts of `LadderConds` wherever a
statement needs it, and never abbreviated by a definition. **A second definition requires its own
append-only amendment**, separately frozen and merged before the work it affects.

Theorems are not budgeted. The execution proves whatever lemmas its verdicts need — the coordinate
invariance, the based gauge fixing, the full-support fact at the frozen configurations, the
Euclidean norm facts, the coordinate bound, the cross-invariant coordinates and their values, the
entry bound on the Fourier family and its `(0,2)` invariant, the feature norm at a unit parameter,
the sequence identities, the sixteen cross-invariants of `Gᵢ`, the tensor identity, the
conjugation facts, the twelve verdicts, the cells — as named results, each printed in the axiom
table.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `GEO1`, `GEO2`, `GEO3` and `GEO4`, whichever label
each reaches other than `UNDECIDED` or `NOT-EXECUTED`. `decide` over finite index types is
permitted; `native_decide` is not, and neither is `sorry`. `Classical.choice` is expected wherever
`sh1_sufficiency`, `product_realizable`, `Real.sqrt` or the classical branch of `Φ_HS`'s statement
is used. **`GEO0` is type P and carries no evidence level.**

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-OGS`**, reserved here and created by the execution pull request.
The round's stem is **`OGS`**; its seal state is the prospective declaration during execution and
the record `verification/seals/OGS.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 24 object enters the repository tree** — any Lean statement about the
   invariant family, the geometry, the isometry proposition, any of the twelve families under it,
   the entry bound, the rotated point, `Φ_conj` or any cell; the definition `mixedTriple`; any
   probe clause; any result artifact; any manifest record or declaration for `OGS`. **The single
   permitted exception is the analysis recorded inside this control-plane blob itself**, merged
   *as* the freeze, including the proof routes and the chronology simulation.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'OGS': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('OGS',)}`, both outside the validator's marker-bounded regions, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('OGS', tag='R7-OGS')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed — the validator's `EXECUTION` classification.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `OGS` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/OGS.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `OGS` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `OGS` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `OGS`.
9. **No `_OGS_BASE`, `_OGS_SEALED_HEAD` or `_OGS_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-OGS`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains
    exactly one top-level definition, the line `def mixedTriple` with the body this freeze displays
    after whitespace normalization, and no other declaration keyword at line start; (b) the module
    imports `OIBridge.OrbitLawGaps`, `OIBridge.OrbitLawRigidityTwisted` and
    `OIBridge.OrbitLawNaturalityFactorization`; (c) the geometry is pinned, in every theorem that
    names `d`, to its frozen equation, each family is pinned, in every theorem that names it, to
    its frozen equation, and no theorem block in one family's subsection of the `GEO3` section
    names another family; (d) the stage-A commit, the module commit and the verdict commits of the
    executed targets are on the first-parent chain from `B` to `E`, in that order, the module absent
    before the module commit and present from it on, and the module commit carrying no theorem
    whose name is a verdict name; (e) each verdict theorem first appears at its own verdict commit
    and at no earlier commit; (f) the gate: a verdict commit for `GEO2`, `GEO3` or `GEO4` exists
    only if the result note carries the opening label for the target before it. A second `def`
    inserted into the module text, a synthetic edit to the definition's body or to the geometry's
    equation, a synthetic naming of a family in another family's subsection, a verdict theorem
    inserted into the module commit's text and a fabricated SHA off the chain each **fail** the
    control.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table with the one
    definition and the eight records; the **five** attestation answers, one per span; the sentence
    that no rung was restated, no equivalence was widened, and neither the invariant family nor the
    geometry was adjusted; each target's label carried with its frozen sentence verbatim; the
    twelve-row census with each family's label and frozen sentence; the seven cells each with its
    label and frozen sentence; **the outcome vector, equal verbatim to one of the seven rows of the
    table**; **the gate record**; **the statement that no verdict was inferred from another beyond
    the consumptions the freeze places**; **the statement that no independence of conditions is
    asserted and no characterization of the isometries is made**; **the statement that no theorem
    is attributed to the literature and no completeness is asserted past the base-star hypothesis**;
    **the statement that every earlier act's historical verdicts stand unchanged**; the
    route-authorization matrix reported as honoured, with no witness reassigned; THE CLAUSE carried
    complete at every mention with its count; and the frozen `P0` sentence for the case reached
    present in `verification/ROADMAP.md` verbatim, after act 23's.

### The contracts this round supersedes, named in advance — none

**Under `§A.37`'s closed-round rule, `AGENTS.md` lines 1055–1061, a closed round's contract that
reads the current round's declaration would be superseded here. The measurement recorded above
found none**: at `D` every closed round's guard reads its own record, and the placeholder
declaration failed nothing. **The execution edits no contract of any closed round.** Should the
execution find that a closed round's contract fails on an act 24 head for a reason that has nothing
to do with act 24's result, that is a discrepancy recorded in the result note, and the disposition
is an append-only amendment to this freeze, separately merged, and not an edit made during
execution.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-OGS' D`, `git grep -l -- '_OGS' D`, `git grep -l -- 'OGS' D`, `git grep -l -- 'OrbitGeometrySelector' D`, `git grep -l -- 'orbit-geometry-selector' D`, `git grep -l -- 'act-24' D` and `git grep -l -- 'mixedTriple' D` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `9f762b8d0b5656950e5030c4eb9ca6514362cce0`, twenty-eight records, twenty-two `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green and carries no legacy constant | eighty-seven `R7-*` tags, all `PASS`, on main-push run 35451692651; `_SI2_LEGACY_RE` finds zero assignment statements |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each of the first twenty-three paths of the start-state table has at `B` the blob the table names (the `frozen-blob` lines of the block) |
| 6 | `B` | No act 24 execution object exists | the guard file at `B` contains no `R7-OGS` and no `_OGS`; no `verification/seals/OGS.json`; no `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean`; no definition named `mixedTriple` anywhere under `verification/lean-mathlib/`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Acts 21, 22 and 23 are sealed at `B` | `verification/seals/OLT.json` at `B` carries `round` `OLT`, `kind` `sealed`, `base` `10d1041bcc10f25d9f643629d4431acbd0f65a1e`, `sealed_head` `b27f3f1630a25667b6728518d06b55fbdabe0d11`, `merge` `4bd732c54e0804bda3b796fcb93e91b5c4299b87`; `verification/seals/OLN.json` at `B` carries `round` `OLN`, `kind` `sealed`, `base` `ccd5704fd157348903cbdea746d24cf5d5498b78`, `sealed_head` `64b3d28e9b0265eb96eec61899f6de474496a3a3`, `merge` `664de6b63eb1f8b55e88c314d326176c4c97ff70`; `verification/seals/OLG.json` at `B` carries `round` `OLG`, `kind` `sealed`, `base` `64214bfb0ae41b9f0a4fb11159089fff32d4dd85`, `sealed_head` `6b9f2e5e765dff3965512ee31a646a22a08e75d2`, `merge` `61c98efc44146ee3bd3650138d8b5ebcc7e1b8b7`; the guard file at `B` carries the `R7-OLT`, `R7-OLN` and `R7-OLG` checks |
| 9 | `B` | Acts 21's, 22's and 23's modules are wired | `OIBridge.lean` at `B` imports `OIBridge.OrbitLawRigidityTwisted`, `OIBridge.OrbitLawNaturalityFactorization` and `OIBridge.OrbitLawGaps` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md` exists at `B`; its blob is the one the `R7-OGS` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are not inputs. **The claim is scoped to the repository record.**

```control-plane-preconditions
d: 9907d3acefb2bd5e2cc66c007400cc0e194d36ec
merged: false
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean 860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean d41b157a3f38d4ebedbe11ad9682a8693836a383
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawGaps.lean 5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1
frozen-blob: verification/lean-mathlib/OIBridge/TwoSidedGauge.lean 4bba2040c33424fafbc6d31c0d63b86dff33691a
frozen-blob: verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean 8d17177799327d648bbbd001cf237e1ac37bd3fc
frozen-blob: verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean cb14c43b0becfe1a379ae3615d5553723ede9163
frozen-blob: verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean afc22cfc93b244c80e1c55a273dcfda1ddebb121
frozen-blob: verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean 4c1137f35600320b9273c857ec62271341b05cd0
frozen-blob: verification/lean-mathlib/OIBridge/DilationChoice.lean 7e3a8222cedf530f3c109662e7174d72b6358063
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md 93c06674792fa3565f6f94e5e954e484dca33cf2
frozen-blob: verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md 174e790d2cc5c663f9f54ae7daaeca90b51f96e1
frozen-blob: verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md 467d8be147b6ebd91f2eed12404566af74ac779f
frozen-blob: verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md 2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a
frozen-blob: verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md 14a2cd8c54946bf0078329402e6f853107b31d9d
frozen-blob: verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md 6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/seals/OLN.json 1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb
frozen-blob: verification/seals/OLG.json 8a058df23c07e2b7571672c039a5a7b4f911a339
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-OGS' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_OGS' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'OGS' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'OrbitGeometrySelector' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'orbit-geometry-selector' $D", "expect": "empty"}
{"id": "d1-act-free", "scope": "D", "check": "git grep -l -- 'act-24' $D", "expect": "empty"}
{"id": "d1-def-free", "scope": "D", "check": "git grep -l -- 'mixedTriple' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 9f762b8d0b5656950e5030c4eb9ca6514362cce0", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals, the modules and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-OGS' -e '_OGS'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'OGS.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'OrbitGeometrySelector'", "expect": "empty"}
{"id": "b6-no-def", "scope": "B", "check": "for f in $(git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e '[.]lean$'); do git show $REF:$f | grep -e '^def mixedTriple'; done", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: acts 21, 22 and 23 sealed
{"id": "b8-olt-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLT.json | tr -d ' \\n' | grep -e '\"round\":\"OLT\",\"kind\":\"sealed\",\"base\":\"10d1041bcc10f25d9f643629d4431acbd0f65a1e\",\"sealed_head\":\"b27f3f1630a25667b6728518d06b55fbdabe0d11\",\"merge\":\"4bd732c54e0804bda3b796fcb93e91b5c4299b87\"'", "expect": "nonempty"}
{"id": "b8-oln-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLN.json | tr -d ' \\n' | grep -e '\"round\":\"OLN\",\"kind\":\"sealed\",\"base\":\"ccd5704fd157348903cbdea746d24cf5d5498b78\",\"sealed_head\":\"64b3d28e9b0265eb96eec61899f6de474496a3a3\",\"merge\":\"664de6b63eb1f8b55e88c314d326176c4c97ff70\"'", "expect": "nonempty"}
{"id": "b8-olg-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLG.json | tr -d ' \\n' | grep -e '\"round\":\"OLG\",\"kind\":\"sealed\",\"base\":\"64214bfb0ae41b9f0a4fb11159089fff32d4dd85\",\"sealed_head\":\"6b9f2e5e765dff3965512ee31a646a22a08e75d2\",\"merge\":\"61c98efc44146ee3bd3650138d8b5ebcc7e1b8b7\"'", "expect": "nonempty"}
{"id": "b8-olt-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLT'\"", "expect": "nonempty"}
{"id": "b8-oln-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLN'\"", "expect": "nonempty"}
{"id": "b8-olg-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLG'\"", "expect": "nonempty"}
# row 9: acts 21's, 22's and 23's modules wired
{"id": "b9-import-olt", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawRigidityTwisted$'", "expect": "nonempty"}
{"id": "b9-import-oln", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawNaturalityFactorization$'", "expect": "nonempty"}
{"id": "b9-import-olg", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawGaps$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md", "expect": "exit0"}
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
- **The stage-A commit comes first**, then **the module commit** with the one definition, the
  shared lemmas and no verdict, then **the verdict commits of the executed targets in the order
  `GEO1`, `GEO2`, `GEO3`, `GEO4`**, one per executed target, the gate read between each; their SHAs
  are recorded, and the attestation set is answered for each of the five spans.
- **Then exactly one execution pull request**, based on `B`, carrying the Lean module, the result
  note, the `R7-OGS` guard clause, the two declarations, the `ROADMAP` propagation and the census
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
3. **`GEO0`** — the bounded search, recorded in full, act 12's cross-invariant and act 18's
   pseudometric recorded as found and as deciding nothing;
4. **`GEO1`** — the label with its frozen sentence, the theorem named, the conjuncts each reported
   separately, the two directions of separation reported apart, the support hypothesis and its
   discharge at the frozen configurations reported, `GEO1-T` recorded as an observation with its
   outcome, and **the statement that nothing is asserted about tuples with a vanishing entry or at
   `|A| > 1`**;
5. **`GEO2`** — the label with its frozen sentence, the three theorems named, the tensor identity
   and its consequence reported apart;
6. **`GEO3`** — the label with its frozen sentence, the twelve-row census with each family's label,
   frozen sentence, theorem, and, for each non-isometry, the pair and the separating quantity, **the
   statement that the label was earned by `ΦCTRL` or `Φ_SC` and by no family outside the prefix**,
   and the metric-dependence sentence in the freeze's two-part wording and no stronger;
7. **`GEO4`** — the label with its frozen sentence, the seven cells each with its label, frozen
   sentence and theorem, `Φ_conj`'s conjuncts each reported separately, and **the statement that no
   independence of conditions is asserted and no characterization of the isometries is made**;
8. **the outcome vector**, one of the seven rows verbatim, **the gate record**, and **the statement
   that no verdict was inferred from another beyond the consumptions the freeze places**;
9. **the route-authorization matrix as honoured**: each construction used for its own target and
   cells and nothing else, no witness reassigned, no alternative substituted;
10. **the scope boundary as honoured**: nothing derives, recognises or approaches quantum
    evolution; no continuity, composition or generator; no theorem attributed to the literature and
    none of its theorems consumed; every earlier act's verdicts untouched; the threading, act 16's
    cell, act 18's `D`-axis, act 10's anchor axis and act 14's carriers untouched;
11. **the non-adoption clause carried verbatim at each mention**, with the count of carriages, and
    the sentence that the invariant family and the geometry are adopted as nothing;
12. the frozen `P0` sentence for the case reached, appended after act 23's, the row's label
    unchanged;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 12, 13, 17, 18, 20, 21, 22 and 23 — every merged label consumed, none
    revised;
15. the definition count against the budget of one, with the one definition's body reported
    verbatim;
16. the chronology certification, naming the property certified, the ten preconditions with their
    scopes and the block's rows as the base check reported them at `M` and at `B`, the validator's
    classification of `OGS` at `E`, `L` and `P`, the empty supersession table reported as
    honoured, and `SI-3`'s standing contract reported as holding;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired — including any value or index of the
    freeze's reading the kernel computed differently;
19. the observation, if any, for the classification round, stated once and narrowly as the
    non-doings section fixes it, and the observations the anti-expansion rule collected.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Every item below is a call
already made**, and the body of this freeze is written to them throughout. **This freeze carries no
open decision.**

1. **The round is a gated round, the orbit-geometry selector audit**: a complete family of phase
   invariants and the geometry it induces first, its controls second, the record's laws against it
   third, a rigidity implication last and only if the earlier targets reach their opening labels;
   act 12's equivalence and act 21's ladder and configurations consumed unchanged; every earlier
   act's verdicts consumed as landed and not rewritten.
2. **The invariant family is the mixed-triple feature map, the one budgeted definition, and the
   geometry is the Euclidean distance of feature vectors, bound by equation**; a metric proposed as
   a formula is not used, and act 18's pseudometric is named as what the geometry is measured
   against and is not reused.
3. **Completeness is frozen at full support and at the frozen configurations only**: the
   base-star hypothesis is the whole of what conjunct (ii) assumes, the zero-entry case is out on
   the ground the frame literature gives, and nothing is asserted at `|A| > 1`.
4. **The frame-equivalence, Bargmann-invariant and complex-Hadamard literature is cited as
   provenance only**: the tuple generalization is this round's and is proved here; act 23's `H(z)`
   is recorded as the normalized standard `F₄⁽¹⁾` family in the narrow wording the provenance
   section fixes; no theorem of that literature is consumed and no invariant of it is asserted to
   be complete.
5. **Each target has its own proposition, route, verdict rule and failure interpretation**, and the
   three-way discipline — a universal proof for a positive label, an exhibited witness on the frozen
   list for a negative one, otherwise `UNDECIDED` — governs each.
6. **The three safeguards and the three failure rules are this round's freeze rules and not
   `AGENTS.md` rules**: the fixed order with one verdict commit per executed target and the
   attestation set at every boundary; the route-authorization matrix; the outcome-vector table of
   seven rows from which the headline is selected verbatim; a universal theorem not obtained is
   `UNDECIDED`; a witness failing its hypotheses is recorded and not repaired; the gate closes
   forward and never reopens.
7. **The family list is closed at twelve**: acts 21's, 22's and 23's eleven transition families,
   each at its merged configuration and pinned to its merged equation, and the entrywise
   conjugation, frozen new and kept visible as a distinct branch; act 21's `ΦX` excluded as a law
   rather than a transition family.
8. **`GEO3`'s label is earned by `ΦCTRL` or `Φ_SC` and by nothing outside the prefix**; the other
   ten verdicts are census entries; the product control's tensor identity is an exact equality and
   is what the perturbation arguments consume.
9. **`GEO4`'s label is earned by the conjugation-amended rigidity statement `b` alone**; `a0`–`a4`
   and `b₀` are recorded cells; cells `a1` and `a3` consume `GEO3`'s verdicts by the freeze's
   placement, which is not an attestation YES; no `NOT-RIGID` label exists for `b`.
10. **The metric-dependence of the discrimination verdicts is stated in two parts and no stronger**:
    merge witnesses once separation is proved, sequence-discontinuity witnesses across metrics
    inducing the quotient topology; `GEO1-T` is an observation sub-question and enters no label.
11. **No drafting-time outcome check was run**; the analyses are the freeze's reading; the one
    simulation run concerns chronology only and found no supersession needed.
12. **`§A.37`'s `D`/`B`/`M` vocabulary governs**: scoped precondition rows, mode `M` validation of
    the candidate merge before the merge, `B` reserved for the certified control-plane merge.
13. **SEALING**, under the manifest protocol: stem `OGS`, tag `R7-OGS`, `E` → `L` → `P` with `P`
    mandatory, the prospective declaration during execution and the record from `P`; no
    supersession; nothing in any closed round's guard touched.
14. **The definition budget is one.** `mixedTriple` with its displayed body; act 12's and act 21's
    declarations are consumed and none is restated; the geometry, the isometry proposition and
    every family are bound by equation.
15. **Acts 12, 13, 17, 18, 20, 21, 22 and 23 are consumed at merged strength**: not re-proved, not
    strengthened, not redefined.
16. **Continuity, composition in time, generators, the threading, the zero-entry case, and any
    comparison with quantum evolution are out of this round**, each a separate question for a
    separate freeze.
