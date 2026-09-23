# Track B act 22 — does the standing prefix through `L4n` force `L5`? The factor-swap relabelling against unchanged factorization, and `ΦCTRL` named for `L4n`: CONTROL PLANE

Owner-called. This file is the whole of act 22's control plane and is merged **alone**, before any
execution object exists. It is a **narrow successor** of act 21: it re-opens nothing of act 21's
census, changes no rung, adds no rung, widens no equivalence, and tests exactly two of the rungs act
21 reported undecided — `L4n` and `L5` — against **two** named transition families at act 21's own
frozen product configuration, with act 21's `ΦPP` consumed as the positive control. One of the two
families is new to the record and is frozen here; the other is act 21's `ΦCTRL`, whose proved
failure of `L4n` act 21 recorded as an observation because its freeze had named no `L4n`
countercontrol. The ladder, the quotient list, the configuration, the one-`|A|` limitation and the
non-adoption clause are act 21's, **consumed unchanged**.

It is **not** a re-run of act 21, **not** an attempt to characterize the surviving class, **not** a
statement about act 21's other undecided rungs `L1`, `L3i` and `L3s`, and **not** an attempt to
derive or to recognise quantum evolution, which stays an explicit non-doing.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The commit vocabulary this freeze uses, fixed first

`AGENTS.md` `§A.37`, at the drafting snapshot, **lines 713–729**, gives a control plane three commit
names, and this file uses them in exactly that sense:

- **`D`, the drafting snapshot** — `d08b932da492891bdadaa5b867fd337250859b99`, certified `main` at
  the landing of the `§A.37` protocol change (#681), whose main-push run 35433619877 is fully green
  with the control-plane base check in mode `B`. Every measurement below — every locating
  coordinate, every pinned blob, every name-freedom check, the drafting check and the supersession
  simulation — was made at `D`, and is a statement about `D`. **`D` is never the execution base.**
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
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'OLN': B}` | **declared**; the validator classifies `OLN` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLN',)}`, in the same file | the seals tree at `B`, read from git, plus the one addition this freeze authorizes, by stem | unchanged; `OLN.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/OLN.json` | **absent** | **written by `P`**: `{"round": "OLN", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `OLN` as `ARCHIVED` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
writes `OLN.json` and removes the `OLN` entry from the prospective declaration, and touches nothing
else. Without `P` the round sits at `LANDED-PENDING-PIN`, permitted at `L` itself, and every head
descending from that unpinned landing fails as *seal pending*.

**No legacy seal constant is written, at any commit of the round.** Nothing matching
`_OLN_(BASE|SEALED_HEAD|MERGE)` exists at any commit, `SI-3`'s standing contract holds at every
head, and the execution's guard clause certifies chronology through one keyed call,
`_si2_authority('OLN', tag='R7-OLN')`, and never through a per-round constant.

### The lifecycle derivation, and why it comes out SEALING

The rule the owner set for act 19 and act 21 is carried: a round is sealing **if and only if** its
execution creates a new formal object whose chronology matters to the result.

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the factor-swap relabelling's ladder conjuncts, its failure of `L5`, the projection of
   act 21's `phiCTRL_census` into the `L4n-RESTRICTS` shape, and the non-implication corollary.
2. **Their chronology is load-bearing.** The round's claim is that its candidate and its proof route
   were frozen — here, in this file — before any kernel work, and that no rung was restated and no
   equivalence widened to reach the verdict; a validator-certified ancestry rooted at this control
   plane's merge commit is what makes that checkable.
3. **A new module with new named results is new seal state**, which only a sealing round's `P` may
   record.

**Therefore act 22 is SEALING, and it owns no other seal state.**

### The tag, the stem, the module and the round directory are free at `D`

At `D`:

- `git grep -- 'R7-OLN'` returns nothing anywhere in the tree, and the tag is absent from the
  **eighty-five** `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries at `D`.
- `git grep -- 'OLN'` returns nothing anywhere in the tree — the bare three-letter form occurs in no
  text file and in no binary artifact — so a bare-stem search for it is unambiguous, and
  `git grep -- '_OLN'` returns nothing.
- No record `verification/seals/OLN.json` exists; the twenty-six records at `D` use the stems `A12P`,
  `A6D`, `A6I`, `A6P`, `ABR`, `CLG`, `CTI`, `HYA`, `HYB`, `HYE`, `OLT`, `PC4`, `PC4S`, `PQT`, `RBR`,
  `RNC`, `RNT`, `SGT`, `SI1`, `SI2`, `SI3`, `TCF`, `TRJ`, `TSG`, `WTS` and `XTS`, and no substring
  search for `OLN` reaches any of them.
- **The alternatives were checked before `OLN` was chosen**, and the check is recorded so that the
  choice is not re-litigated. `OLF` (orbit-law factorization) was the first choice and was rejected:
  `git grep -- 'OLF'` at `D` matches one binary artifact, `papers/Main.pdf`, and a stem whose bare
  form occurs anywhere in the tree fails the unambiguity this freeze requires of it. `OLS` (swap),
  `OLV` and `OLE` each occur in the tree. `OLN` — orbit-law naturality, the rung the round tests
  factorization against — occurs nowhere. `OLT` is act 21's and `RNT` act 20's, excluded on that
  ground alone.

**The round directory and the module name are free at `D` too.** `git grep -- 'act-22'` and
`git grep -- 'OrbitLawNaturalityFactorization'` return nothing. The round directory is
`verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/` and the module
is `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`.

### What this round does NOT own, named exhaustively

It alters **no existing manifest record**. The twenty-six records under `verification/seals/` at
`D` — the seals tree `90d5a4ae59c931216d52a8ce9456ae906366085e` — are **read and never written**;
the one addition this freeze authorizes is `OLN`. It writes **no legacy constant**. It does not
re-pin, re-derive or re-declare any other round's seal: `OLT.json`, `RNT.json` and the rest belong
to the rounds that set them. Inside the guard file the execution **adds** the `R7-OLN` clause,
**sets** the two stem-free declarations named above, and **edits one contract in one closed
round's guard at exactly the place the supersession table names** — and changes nothing else in
the file.

## Provenance — what this freeze carries from act 21, and what is its own

**The rule.** Act 22 consumes act 21's ladder, quotient list, configuration, witness supply and
non-adoption clause **unchanged**, and adds one transition family, two rung targets, one
non-implication corollary and its own lifecycle. Every rung is the declaration act 21's merged
module carries, pinned by blob at `B`; **no rung is restated in this round's module**, and a
restatement would be a defect of the round.

| act 21 section (frozen blob `316d635a…`, line range) | this file | status |
| --- | --- | --- |
| the ladder `L0`–`L5`, lines 735–946 | consumed as `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds` and the inline `L2`, `L4d`, `L4n` of `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | **consumed unrestated** |
| the frozen quotient list, lines 703–733 | the same three equivalences, no fourth | **carried unchanged** |
| the frozen product configuration, lines 1263–1267 | the same configuration | **carried unchanged** |
| the witness supply, lines 1369–1414 | the same supply, plus act 21's merged product-embedding lemmas named below | **carried, extended by merged act 21 results** |
| the status-rule sentences for `Li-RESTRICTS`, `Li-FREE`, `Li-UNDECIDED`, `Φ`-SURVIVES, `Φ`-FAILS, `Φ`-UNDECIDED, lines 1676–1717 | carried verbatim below | **carried verbatim** |
| THE CLAUSE, lines 1897–1905 | carried verbatim with "Act 21" → "Act 22" in its first sentence | **carried, one substitution** |
| `ΦPP`, lines 1340–1347; `ΦCTRL`, lines 1349–1367 | consumed as `phiPP_ladder` and `phiCTRL_census` | **consumed at merged strength** |
| everything else — the shared theorem, the census, `SIOP`, the headlines, the `P0` sentence for act 21's case | not this round's | **untouched** |

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
`control-plane-lint` and the workflow's `control-plane-base-check` job read it.

### The manifest protocol, in the passages this round executes under

`AGENTS.md`, **lines 962–972** (the seal record is data), **1024–1035** (the legacy representation
is retired), **1037–1046** (how a sealing round carries its base), **1047–1053** (how manifest
integrity is declared) and **1055–1061** (a closed round's contracts are read over the records it
manifested) are the passages act 21 quoted at its own base, unchanged in wording at `D`; the last is
the authority for the supersession table below:

> **A closed round's contracts are read over the records it manifested.** A
> landed round's manifest-cardinality and integrity contracts — its record
> count, its authorized-addition set, its census and its probes — are evaluated
> over the records that round manifested, and a later round's authorized
> additions are outside that historical scope.

### The obligation, and what act 21 left in front of it

`verification/ROADMAP.md`, **line 63**, the `P0` row, carries act 21's frozen Case A sentence at its
end; the row's label is **OPEN** and two-part, and this round appends its own frozen sentence after
act 21's and changes the label of nothing.

`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md`, blob
`bb02ef41eb221696ffa45c9281b69553c8279cbb`, the two obstructions this round acts on:

**lines 499–510**, `L4n`:

> **The rung**: representative-level gauge-naturality at act 20's certified strength. **The
> conjunct**: the `RESTRICTS` label's requirement that the exhibited law be the one the rung's
> countercontrol names — and the `L4n` row of the countercontrol table names no construction.

and, from the same passage, the settlement it names:

> **What would settle it**: a later round's freeze naming a transition descending to classes
> with no twisted-natural lift as the `L4n` countercontrol — the observation below is a candidate for
> exactly that — or a universal implication proof.

**lines 556–569**, `L5`:

> **The conjunct**: the `RESTRICTS` label's requirement that the
> violator satisfy every earlier rung. **The step at which the proof stopped**: the named
> violator `ΦCTRL` **fails `L5` exactly as the freeze predicted** […] **and it fails `L4n`,
> an earlier rung**, so it cannot be the exhibited law the label requires.

> **What would settle it**: a law admitting a twisted-natural lift at the
> product configuration that fails factorization — the branch-conditional structure that defeats
> `L4n` is exactly what `ΦCTRL`'s refutation of `L5` uses, so such a law would have to break
> factorization by another mechanism — or a universal proof that `L0`–`L4n` imply factorization at
> the product configuration.

**lines 512–525**, the observation this round names as the `L4n` countercontrol:

> **The observation, recorded and not applied.** `phiCTRL_census`. […] The controlled relabelling `ΦCTRL`, at the frozen product configuration
> `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`, `Γ ≡ 1/16`, satisfies every earlier condition —
> it is an `L-PROP` law (proper, with both propagation clauses), total, admissibility-preserving,
> time-homogeneous, reversible in both conjuncts (`Φ ∘ Φ = id` exactly) and descending — and **admits
> no representative-level lift that is twisted-natural at act 20's strength**, at evidence level 2.

**lines 1015–1023**, the two discrepancies this round's design answers, `DF2` and `DF3`:

> **DF2 — the freeze's `L5` countercontrol fails an earlier rung.** `ΦCTRL` fails `L4n`, which the
> `L5` test did not ask.

> **DF3 — the `L5` countercontrol fails `L4n`, which the freeze did not anticipate.**

### The act 21 declarations this round is stated over

`verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`, blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`: `FactorizesOnProduct` at **lines 143–157**,
`LadderConds` at **lines 179–196** (its ninth conjunct `FactorizesOnProduct A A₁ A₂ e Γ₁ Γ₂ Γ Φ`,
its eighth the inline `L4n`), `witness_supply` at **line 431**, `realizable_relabel` at **388**,
`relabel_gramPhaseEquiv` at **397**, `relabel_relabel_symm` at **405**, `gramPhaseEquiv_of_relabel`
at **420**, `product_cross` at **963–973**, `relabel_product` at **975–984** (stated for
`Equiv.prodCongr σ₁ σ₂` and for nothing else), `product_realizable` at **1015**, `hadamard_entries`
at **1062–1090**, `product_separations` at **1093**, `phiPP_ladder` at **1166–1172**, and
`phiCTRL_census` at **1282–1316**, whose `L4n` conjunct is, verbatim,

```
          ∧ (∀ t, ¬ ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
```

and the exact shape of the `L5` declaration, verbatim, which is what "unchanged `L5`" means:

```
def FactorizesOnProduct {V₁ V₂ : Type} [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
    (A₁ A₂ : Type) [Fintype A₁] [Fintype A₂] (e : V ≃ V₁ × V₂)
    (Γ₁ : ℕ → Matrix V₁ V₁ ℝ) (Γ₂ : ℕ → Matrix V₂ V₂ ℝ) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  Fintype.card A = Fintype.card A₁ * Fintype.card A₂
    ∧ (∀ t i j, Γ t i j = Γ₁ t (e i).1 (e j).1 * Γ₂ t (e i).2 (e j).2)
    ∧ ∃ (Φ₁ : ℕ → (V₁ → Matrix V₁ V₁ ℂ) → (V₁ → Matrix V₁ V₁ ℂ))
        (Φ₂ : ℕ → (V₂ → Matrix V₂ V₂ ℂ) → (V₂ → Matrix V₂ V₂ ℂ)),
        ∀ t (G₁ : V₁ → Matrix V₁ V₁ ℂ) (G₂ : V₂ → Matrix V₂ V₂ ℂ),
          RealizableGram A₁ (Γ₁ t) G₁ → RealizableGram A₂ (Γ₂ t) G₂ →
            GramPhaseEquiv
              (Φ t (fun i => Matrix.of fun j k =>
                G₁ (e i).1 (e j).1 (e k).1 * G₂ (e i).2 (e j).2 (e k).2))
              (fun i => Matrix.of fun j k =>
                Φ₁ t G₁ (e i).1 (e j).1 (e k).1 * Φ₂ t G₂ (e i).2 (e j).2 (e k).2)
```

**Two features of that declaration are load-bearing for this round and are named now.** First,
the quantifier order is `∃ Φ₁ Φ₂, ∀ t G₁ G₂`: the factor maps are **fixed before the inputs**, so a
refutation may instantiate the universal at two inputs against the same `Φ₁`, `Φ₂`. Second, **no
realizability, normalization or admissibility is required of `Φ₁ t G₁` or `Φ₂ t G₂`** — they are
arbitrary tuples — so a refutation may **not** read any invariant of theirs from realizability;
whatever it knows about them it must derive from the displayed `GramPhaseEquiv` alone. The proof
route frozen below is written to that constraint.

### The act 20 declarations consumed

`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, blob
`4c1137f35600320b9273c857ec62271341b05cd0`: `RelabelTransition` at **lines 167–168**
(`fun i => (G (σ i)).submatrix σ σ`, so `RelabelTransition σ G i j k = G (σ i) (σ j) (σ k)`),
`RelabelLift` at **181–182**, `rnt2_lifting_property` at **226–227**, `rnt2_admissible` at
**245–248** (under `Γ (σ i) (σ j) = Γ i j`), `rnt3_law_exact` at **375–378**, each stated for an
arbitrary finite `V`, arbitrary `A`, arbitrary anchor and **arbitrary `σ : Equiv.Perm V`**, as act
20's result records at its lines 625–627. At the product carrier `Fin 4 × Fin 4` the factor
exchange `Equiv.prodComm (Fin 4) (Fin 4)` is such a `σ`.

### The act 12 and act 18 declarations consumed

`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob
`4bba2040c33424fafbc6d31c0d63b86dff33691a`: `GramPhaseEquiv` at **lines 102–103** —
`∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ ∀ i j k, G' i j k = star (c j) * G i j k * c k` — from which the
two facts the refutation uses follow by one line each: **a diagonal entry is preserved**,
`G' i j j = G i j j`, since `star (c j) * c j = 1`; and the cross product is preserved, which is
act 12's `gramPhaseEquiv_cross_invariant` at **870–871**,
`G' i₀ i₁ i₀ * G' i₁ i₀ i₁ = G i₀ i₁ i₀ * G i₁ i₀ i₁`. `RealizableGram` at **108–110**.
`verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean`, blob
`cb14c43b0becfe1a379ae3615d5553723ede9163`: `ProperAt` at **167–171** and `PropagatesFrom` at
**186–193**, with its two clauses.

## Start state, pinned by blob

Pinned **by blob** at `D`. Blob identity is authoritative: the commit locates the tree, the blob is
what is compared, and the `D → B` rows of the block below require each of these unchanged at `B`.

| path | blob at `D` |
| --- | --- |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md` | `316d635a31f91faebeeebef7688b30002d24b4ca` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md` | `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md` | `bb02ef41eb221696ffa45c9281b69553c8279cbb` |
| `verification/seals/OLT.json` | `8ed0ef5391410db3a112cbe845d27536b7c1ab9b` |
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | `6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `tools/control_plane_base_check.py` | `84cdd4518f76d7bbcead3f6dec8e58063617e556` |
| `tools/control_plane_lint.py` | `7678dbe25f51e6e6b14f07e8842f1b6d205f4fed` |

Every one of these is read and never written by this round. If any blob differs at `B`, the
execution records the discrepancy and does not repair the freeze — and for the first nine, the
base check has already refused the merge.

### The files this round writes

**The files this round writes are named separately and are not in the table above.** Each is
pinned by blob at `D` all the same, so that a discrepancy in what the round writes onto is as
visible as a discrepancy in what it reads; a difference at `B` in any of them is recorded in the
result note as a discrepancy and the freeze is not repaired.

| path | blob at `D` | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `cc08d5df3d390c34578a97e655ceb8ef0f8077c9` | **read** as the pinned statement of the `P0` row, and **written** only by appending the frozen post-round sentence for the case reached after act 21's sentence in the same cell; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `57fa9f040f1c628007f3188a6ecbe691a2a735fb` | the `R7-OLN` clause **added**; `_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` **set** as the shape section states, the former emptied by `P`; the supersession table's **one edit** in `R7-OLT`; **nothing else**; no legacy constant written |
| `verification/lean-mathlib/OIBridge.lean` | `7eb77dd0c0385ecb43fe572f004d1a275cba8321` | one import line added directly after `import OIBridge.OrbitLawRigidityTwisted`, at line 210 at `D` |
| `verification/lean-manuscript-census.json` | `2c86fbce9aac3060c146061c0ff643fc7ca37030` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md` | — | created by the execution |
| `verification/seals/OLN.json` | — | created by **`P`**, and by nothing before `P` |

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

The base is fixed the moment this file merges, and whatever sibling lanes have landed in `main` by
then is a fact about the base's tree and not a fact about this round's inputs. The start-state
table above is the complete list of what this round consumes, and a file present at `B` and absent
from that table is read by nothing in this round. The seals tree at `B` is whatever `B` carries;
the execution records the tree it found, and the declared baseline reads it from git.

## Source scoping, carried from acts 13 through 21

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what act 21 left in front of it

Act 21 reached `L-WIDE` over the complete ladder and left five rungs undecided. For three of them —
`L1`, `L3i`, `L3s` — the obstruction is a missing witness of a shape the note describes, and this
round does **not** touch them. For the other two the obstruction is entangled: act 21's `L5`
countercontrol `ΦCTRL` fails `L5` by the two-instance argument its freeze predicted **and** fails
`L4n`, an earlier rung, so it can witness neither `L5-RESTRICTS` (the witness must satisfy every
earlier rung) nor `L4n-RESTRICTS` (act 21's `L4n` row named no countercontrol, and the witness rule
forbids substitution). The two failures have one mechanism — the transition is **conditional on the
class** of its input, which no fixed induced map can see and no fixed pair of factor maps can
reproduce — and so the record cannot tell whether `L5` is a restriction at all once `L4n` is
imposed, or whether naturality already forces factorization.

**That is the question this round asks, and it is the settlement act 21's note names for both rungs
in one construction**: a law with a twisted-natural lift at the product configuration that fails
factorization by another mechanism. The factor-swap relabelling is that construction. It is a carrier
relabelling, so act 20's merged lift and exact law give it `L4n` at once; and it exchanges the two
factors, so it cannot be a fixed local map on each factor for the ordered decomposition `L5` fixes.

### What act 22 inherits, and consumes without re-proving

Consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**, and a
merged statement is not enlarged by being consumed.

1. **Act 21's ladder**, as the declarations of its merged module, and **act 21's rung verdicts**
   `L0-RESTRICTS`, `L1-UNDECIDED`, `L2-RESTRICTS`, `L3i-UNDECIDED`, `L3s-UNDECIDED`, `L4d-HYP`,
   `L4n-UNDECIDED`, `L5-UNDECIDED`, its `SIOP-YES` and its `L-WIDE`, all of which stand as act 21
   states them. **Act 21's historical verdicts are not changed by anything here**: this round earns
   its own rung labels under its own freeze, and act 21's note is not edited.
2. **Act 21's `OL1`, at its exact strength.** `ol1a_descent` assumes descent alone and gives (i)
   well-defined maps on the ambient tuple quotient, (ii) that every solution is the composite of
   those maps applied to its initial class, and (iii) uniqueness of continuation for solutions that
   exist; `ol1b_monoid_action` adds the monoid form at constant `Γ` under `L2`. **Descent alone does
   not supply preservation of the admissible orbit space**: that a realizable class is carried to a
   realizable class is `L1`, and act 21's `l1_free_on_shared_class` supplies it from `L0 ∧ L2 ∧ L4d`
   at constant `Γ` and from nothing weaker. This round reads `OL1` as that and as no more.
3. **Act 21's product-embedding results**: `product_realizable`, `product_cross`, `relabel_product`
   (for product permutations only), `relabel_one`, `hadamard_entries`, `product_separations`,
   `witness_supply`, `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_relabel_symm`,
   `relabel_symm_relabel` and `gramPhaseEquiv_of_relabel`.
4. **Act 21's `phiPP_ladder`**, the positive control: `Φ_{σ×σ}` satisfies `LadderConds` in full at
   the product configuration, `L5` included with content.
5. **Act 21's `phiCTRL_census`**, consumed for exactly what it proves: `ΦCTRL` is an `L-PROP` law,
   total, admissibility-preserving, time-homogeneous, reversible and descending at the product
   configuration, admits no twisted-natural lift at act 20's strength at any `t`, and fails `L5`.
6. **Act 20's lift and its exact law**, `RelabelLift σ`, `RelabelInducedLeft σ`,
   `RelabelInducedRight σ`, `rnt2_lifting_property`, `rnt2_admissible`, `rnt3_law_exact`, at
   arbitrary `V`, `A`, anchor and `σ`; and act 20's `TwistedNatural` as the `L4n` notion, exactly
   as act 21 froze it.
7. **Act 12's `GramPhaseEquiv`, `RealizableGram`, `FibreGram`, `gramPhaseEquiv_cross_invariant`,
   `sh1_necessity`, `sh1_sufficiency`**; **act 17's `GramTrajEquiv`** and its equivalence lemmas;
   **act 18's `ProperAt`, `PropagatesFrom`, `prod_mem_unitaryGroup`, `prod_admissible`**.

## The question, FROZEN

> **Does the standing prefix of act 21's ladder through `L4n` — the `L-PROP` hypotheses, `L0`,
> `L1`, `L2`, `L3i`, `L3s`, `L4d` and `L4n` at act 20's certified strength — imply `L5` as act 21
> froze it, at act 21's frozen product configuration? And does `L4n` itself restrict the class the
> shared theorem produces?**

Both are questions about act 21's exact declarations at act 21's exact configuration. **The round
does NOT try to derive Schrödinger evolution**, does not characterize the surviving class, and does
not ask what factorization means beyond the declaration act 21 froze.

## The strength of the ask, FROZEN

**The ask is two rung-status verdicts and one non-implication, over a closed list of three named
laws, at one frozen configuration.** It asks whether one named law satisfies every condition of the
prefix and fails `L5`; whether one named law, already proved to fail `L4n`, satisfies every
condition before it; and, from the first, whether the prefix implies `L5`. It does **not** undertake
a census, a characterization, a universal implication proof in the other direction, or a fourth
witness completing a square of independences.

**What the primary result would and would not separate, stated in advance.** `L5` as frozen asks
for factorization into **fixed local maps for the ordered decomposition `e`**: one map on the first
factor's orbit space and one on the second, chosen before the inputs, such that the transition of a
product class is the product of the transitions of its factors. The factor-swap relabelling
**preserves product form** — it sends a product class to a product class — and **exchanges the
factors**. If it fails `L5`, what is established is that the prefix through `L4n` does not imply
factorization into fixed local maps for the ordered decomposition; **it is not established that any
surviving law interacts, couples, entangles or fails to compose in any other sense**, and no
sentence of this round says so.

## The objects, FROZEN — act 21's, consumed

`V`, `A`, `a₀`, `Γ`, the transition family, the law it generates, the admissible orbit state space
`Ω(Γ, t)` and the frozen quotient list are act 21's, at its lines 642–733, consumed without
restatement. In particular:

- **A transition family** is `Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)`, written at
  representative level and required to descend; **the law it generates** is
  `∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`.
- **The frozen quotient list** is act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv` and act 21's
  `LawEquiv`, and **no other equivalence may be used in any verdict**. This round's verdicts are
  rung labels and a non-implication; none is taken modulo anything but `GramPhaseEquiv`.

### The frozen product configuration

Act 21's, at its lines 1263–1267: `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`,
`Γ ≡ 1/16` as the pointwise product `Γ₀ ⊗ Γ₀` of two copies of `Γ₀ ≡ ¼`, the decomposition
`e = Equiv.refl (Fin 4 × Fin 4)`, `Γ₁ = Γ₂ = Γ₀` at every `t` — exactly the parameters
`phiPP_ladder` and `phiCTRL_census` are stated at. **`Γ ≡ 1/16` is constant and therefore
invariant under every permutation of the product carrier**, the factor exchange included.

**The one-`|A|`-value caveat, carried from acts 18 and 21 and recorded again.** `|A₁| = |A₂| = 1`
is the strongest case for the per-slice statements and is not degenerate there; it is not
automatically the right case for a cross-time statement, and every verdict of this round is at that
cardinality and at no other.

## The ladder, CONSUMED and not restated

The ladder is act 21's `L0`–`L5` in act 21's wording, at its lines 735–946, as the declarations of
`OrbitLawRigidityTwisted.lean` at blob `860daac4…`: `EvolvesTotally` (`L0`), `PreservesAdmissible`
(`L1`), the inline `∃ Φ₀, ∀ t, Φ t = Φ₀` (`L2`), `Reversible` (`L3i`, `L3s`), the descent conjunct
(`L4d`), the inline `∀ t, ∃ Ψ αL αR, (lifting) ∧ (admissibility) ∧ TwistedNatural a₀ αL αR Ψ`
(`L4n`) and `FactorizesOnProduct` (`L5`), with the standing hypotheses `ProperAt` and
`PropagatesFrom`, conjoined as `LadderConds`. **This round's module states no rung**: every
conjunct it proves or refutes is act 21's declaration applied to a named family, and **the prefix
through `L4n`** means the first eight conjuncts of `LadderConds` — the two standing hypotheses,
`L0`, `L1`, `L2`, `L3`, `L4d`, `L4n` — as `LadderConds` lists them.

### The rung labels, carried

Act 21's three labels and their earning conditions, at its lines 926–946, govern `L4n` and `L5`
here: `Li-RESTRICTS` is earned only by an **exhibited** law satisfying every earlier rung and
failing `Li`, with the failing conjunct and the separating class named; `Li-FREE` only by a
**universal** kernel proof of the implication from the earlier rungs; `Li-UNDECIDED` by the recorded
statement that neither was reached, with the obstruction named. **A label is earned by the witness
the countercontrol table names and by nothing found during execution.** The verdicts are
**one-directional**: a `RESTRICTS` on one rung says nothing about any other rung, an exhibited
failure of one candidate says nothing about candidates of its shape, and **no combination of
labels reached here is reported as an independence of rungs**.

## The frozen candidate law list

**Three named transition families, at the frozen product configuration. The list is closed at this
freeze.** A candidate discovered during execution is recorded as an observation and not executed.

### `Φ_swap` — the factor-swap relabelling, NEW to the record

> **Statement.** `Φ_swap t G = RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` at every `t`,
> that is, `Φ_swap t G (i₁,i₂) (j₁,j₂) (k₁,k₂) = G (i₂,i₁) (j₂,j₁) (k₂,k₁)` — act 20's carrier
> relabelling by the permutation of `Fin 4 × Fin 4` that exchanges the two coordinates.

**Where it comes from, and why it is a law datum.** It is act 19's and act 21's `ΦP` shape at the
product carrier with a permutation that is **not of product form** `σ₁ × σ₂`; `Equiv.prodComm` is
chosen before any lift exists and consults no lift, and `Γ ≡ 1/16` is invariant under it. It names
no interaction, no coupling and no evolution operator. **Its role: the `L5` countercontrol**, and
the witness of the non-implication.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **On products it exchanges the factors.** For any tuples `X` on the first factor and `Y` on the
  second, `RelabelTransition (Equiv.prodComm _ _) (X ⊠ Y) = Y ⊠ X` **exactly**, entrywise: the left
  side at `(i, j, k)` is `(X ⊠ Y) (σ i) (σ j) (σ k) = X i₂ j₂ k₂ · Y i₁ j₁ k₁`, which is `(Y ⊠ X) i j k`.
  **Act 21's `relabel_product` does not cover this** — it is stated for `Equiv.prodCongr σ₁ σ₂`
  only — so the execution proves the identity explicitly, as its own lemma, before any verdict uses
  it.
- **Every conjunct of the prefix is a carrier relabelling's**, and the proof of each is
  `phiPP_ladder`'s with `Equiv.prodCongr σ σ` replaced by `Equiv.prodComm (Fin 4) (Fin 4)`:
  totality, admissibility preservation and `L3s` from `realizable_relabel`; `L3i` from
  `gramPhaseEquiv_of_relabel`; `L4d` from `relabel_gramPhaseEquiv`; `L2` by construction; **`L4n`
  from act 20's merged `RelabelLift`, `rnt2_lifting_property`, `rnt2_admissible` (with `Γ`
  constant) and `rnt3_law_exact` at `σ = Equiv.prodComm (Fin 4) (Fin 4)`**; and the `L-PROP`
  hypotheses from the product separations: `G(H₁) ⊠ G(H₁)` is fixed by the exchange exactly,
  `[G(H₁) ⊠ G(Hᵢ)]` is moved to `[G(Hᵢ) ⊠ G(H₁)]`, the two are `∼_D`-inequivalent by the
  cross-invariant named below, both products are realizable by `product_realizable`, so `ProperAt`
  has its two inequivalent solutions and its non-solution, and `PropagatesFrom` clause (ii) holds at
  `t = 1` with clause (i) from descent.
- **It fails `L5` by the two-instance argument with the normalization gap closed.** Suppose
  `FactorizesOnProduct` held with factor maps `Φ₁`, `Φ₂`. Fix `G₁ = G(H₁)` and put
  `X = Φ₁ 0 G(H₁)`, `Y = Φ₂ 0 G(H₁)`, `Y' = Φ₂ 0 G(Hᵢ)` — arbitrary tuples, about which nothing
  is known but the two displayed equivalences:
  - instance 1, `G₂ = G(H₁)`: `G(H₁) ⊠ G(H₁) ∼_D X ⊠ Y`;
  - instance 2, `G₂ = G(Hᵢ)`: `G(Hᵢ) ⊠ G(H₁) ∼_D X ⊠ Y'`, the left side being `Φ_swap` of
    `G(H₁) ⊠ G(Hᵢ)` by the exchange identity.

  **Diagonal equations.** A `∼_D` preserves every diagonal entry, so at every product index
  `X i₁ j₁ j₁ · Y i₂ j₂ j₂ = 1/16` and `X i₁ j₁ j₁ · Y' i₂ j₂ j₂ = 1/16`, the right sides being the
  diagonals of the Hadamard Grams, `¼ · ¼`. Hence every `X i₁ j₁ j₁` is nonzero and, cancelling
  it, `Y i₂ j₂ j₂ = Y' i₂ j₂ j₂` for every `i₂`, `j₂`.

  **Cross-invariant equations.** Act 12's `gramPhaseEquiv_cross_invariant` read at the product
  fibre pair `((0,m), (1,m))`, through act 21's `product_cross`, gives for instance 1
  `(X 0 1 0 · X 1 0 1) · (Y m m m · Y m m m) = (G(H₁) 0 1 0 · G(H₁) 1 0 1) · (¼ · ¼) = 1/256`, and
  for instance 2 `(X 0 1 0 · X 1 0 1) · (Y' m m m · Y' m m m) = (G(Hᵢ) 0 1 0 · G(Hᵢ) 1 0 1) · (¼ · ¼)
  = i/256`, by `hadamard_entries`. With `Y m m m = Y' m m m` the two left sides are equal, so
  `1/256 = i/256`, which `norm_num [Complex.ext_iff]` refutes — exactly the closing step of
  `phiCTRL_census`. **No realizability, normalization or admissibility of `X`, `Y` or `Y'` is used
  anywhere**; the nonzero factor cancelled is a diagonal entry, read from the equivalence.

  **The separating classes are `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(H₁)]`**, the images of the two
  instances, and the separating invariant is act 12's cross-invariant at `((0,m),(1,m))`, values
  `1/256` and `i/256`.

### `ΦCTRL` — act 21's controlled relabelling, CONSUMED

> **Statement.** Act 21's, at its lines 1349–1367, as the transition family `phiCTRL_census` pins
> by equation: on a class with a product representative whose first factor is `[G(H₁)]`, relabel the
> second factor by `σ = (2 3)`; otherwise the identity.

**Its role: the `L4n` countercontrol**, named here prospectively — which act 21's freeze did not do
— so that the failure act 21 proved and recorded as an observation can earn the label under the
witness rule. **What this round proves about it is a projection of `phiCTRL_census` and nothing
more**: the merged theorem already carries `ProperAt`, `PropagatesFrom`, `EvolvesTotally`,
`PreservesAdmissible`, `L2`, `Reversible`, descent and `∀ t, ¬ (L4n)` for this family at this
configuration, and the execution restates them in the `Li-RESTRICTS` shape by consumption.
**Act 21's historical verdict `L4n-UNDECIDED` is not changed**: it was the correct verdict under
act 21's freeze, and this round's `L4n-RESTRICTS`, if reached, is a verdict under this freeze.

### `ΦPP` — act 21's product permutation, CONSUMED as the positive control

> **Statement.** Act 21's, `Φ_{σ×σ}` with `σ = (2 3)` on each factor.

**Its role: the positive control.** `phiPP_ladder` is consumed for the fact that a law satisfying
the whole prefix **can** satisfy `L5` with content at this configuration, so that a failure of
`L5` by `Φ_swap` is a failure of one law and not a vacuity of the condition. Nothing is re-proved.

**The fourth corner is outside this round.** A law failing `L4n` and satisfying `L5` — a
class-conditional relabelling on one factor tensored with the identity, for instance — would be the
witness that, together with `ΦCTRL` (fails both), `Φ_swap` (satisfies `L4n`, fails `L5`) and `ΦPP`
(satisfies both), would complete a square of independences. **It is not on this freeze's list, it is
not executed here, and no sentence of this round reports an independence of the two rungs.** What
the three named laws can establish is stated one-directionally, target by target, below.

## The witness supply, FROZEN

Act 21's supply at its lines 1389–1409, unchanged — act 12's Hadamard objects `H(1)`, `H(i)`,
`H(−1)` at `Γ₀ ≡ ¼`, act 12's `sh1_sufficiency` and act 17's `tj1_sufficiency`, act 18's
`prod_mem_unitaryGroup` and `prod_admissible`, the moves of acts 11, 12 and 13, and act 20's lift
with its exact law — **extended by act 21's merged product-embedding lemmas** named in the
inheritance list, which are what discharge the realizability of every product tuple this round
names and the entries and separations its verdicts read. **Nothing outside this supply may be
introduced, at any point, for any reason.** The generic witness rule governs every countercontrol:
what a rung's countercontrol names is what is tested, and an alternative witness found during
execution is recorded as an observation and never substituted.

## The countercontrols, one per target

| target | the countercontrol this freeze names | configuration |
| --- | --- | --- |
| `L4n` | `ΦCTRL`, consumed from `phiCTRL_census`: the prefix through `L4d` holds and `∀ t, ¬ (L4n)`, the failing conjunct being the right closure and right intertwining conjuncts of `TwistedNatural` read together with the lifting obligation, the separating classes `[G(H₁) ⊠ G(Hᵢ)]` and `[G(Hᵢ) ⊠ G(Hᵢ)]`, as act 21's §7 records | the product configuration |
| `L5` | `Φ_swap`: the prefix through `L4n` holds, `L4n` through act 20's lift at `σ = Equiv.prodComm (Fin 4) (Fin 4)`, and `¬ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ_swap` by the two instances `G₁ = G(H₁)`, `G₂ ∈ {G(H₁), G(Hᵢ)}` with the diagonal cancellation, separating classes `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(H₁)]` at `((0,m),(1,m))` | the product configuration |
| `L5`, satisfying control | `ΦPP`, consumed from `phiPP_ladder` | the product configuration |
| the non-implication | derived from the `L5` row: one law satisfying the prefix and failing `L5` refutes `∀ Φ, prefix Φ → L5 Φ` at the configuration | the product configuration |

**Evidence that earns any countercontrol**: a Lean theorem at evidence level 2 whose statement pins
the objects by equations, discharges admissibility from merged results, and certifies the separating
quantity at a named index through a named invariant. **Searching and not finding earns nothing.**

## The drafting check, performed before this freeze and recorded here

**The owner authorized a drafting-time check, and it was run before this file was written; its
inputs and outcomes are recorded here as pre-freeze observations, beside the proof reasoning above.
It is analysis and not a finding**: whether the execution's kernel proofs close is for the execution
to establish, and nothing below is evidence for any verdict of this round.

**Inputs.** Exact arithmetic over the Gaussian rationals `ℚ[i]`. `H(z)` as act 12 freezes it,
`½ · [[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]`, indexed row-column, for `z ∈ {1, i, −1}`;
`G(H) i j k = conj(H i j) · H i k` at `|A| = 1`, which is `FibreGram 0 H` by `fibreGram_apply`;
the product embedding `(X ⊠ Y) i j k = X i₁ j₁ k₁ · Y i₂ j₂ k₂` with `e = id`; the relabelling
`RelabelTransition σ G i j k = G (σ i) (σ j) (σ k)` with `σ` the coordinate exchange; the cross
product `P i₀ i₁ i₀ · P i₁ i₀ i₁` in the shape of `gramPhaseEquiv_cross_invariant`.

**Outcomes, each checked exactly and each recorded as it came out.**

1. `RelabelTransition (exchange) (G₁ ⊠ G₂) = G₂ ⊠ G₁` entrywise on the five instances
   `(H₁,H₁)`, `(H₁,Hᵢ)`, `(Hᵢ,H₁)`, `(Hᵢ,Hᵢ)`, `(H₁,H(−1))`: **holds**.
2. `G(H₁) ⊠ G(H₁)`, `G(Hᵢ) ⊠ G(H₁)` and `G(H₁) ⊠ G(Hᵢ)` are Hermitian in each fibre, have every
   diagonal entry `1/16`, have all sampled `2 × 2` minors zero in each fibre (rank at most one),
   and sum over fibres to the identity: **holds** — consistent with `product_realizable`.
3. Act 12's invariant `G(0)(1,0) · G(1)(0,1)` takes the values `1/16`, `i/16`, `−1/16` on `H(1)`,
   `H(i)`, `H(−1)`: **holds**, as `hadamard_entries` states for the first two.
4. The product cross product at `i₀ = (0,m)`, `i₁ = (1,m)`, for every `m`, is `1/256` on
   `G(H₁) ⊠ G(H₁)` and on `G(H₁) ⊠ G(Hᵢ)`, and `i/256` on `G(Hᵢ) ⊠ G(H₁)`: **holds** — the
   first-factor invariant times the second factor's squared diagonal, as `product_cross` gives.
5. The two-instance argument as written above — diagonal cancellation, then the cross equations —
   closes on `1/256 ≠ i/256`, using no property of `X`, `Y`, `Y'` beyond the two equivalences:
   **holds**.
6. The exchange is an involution on tuples; `G(H₁) ⊠ G(H₁)` is fixed by it exactly;
   `[G(H₁) ⊠ G(Hᵢ)] ≠ [G(Hᵢ) ⊠ G(H₁)]` by item 4, so the constant trajectory at `G(H₁) ⊠ G(Hᵢ)`
   is not a solution and the solutions from `[G(H₁) ⊠ G(H₁)]` and `[G(H₁) ⊠ G(Hᵢ)]` are
   inequivalent at `t = 0` and at `t = 1`: **holds**.
7. The diagonal entries and the cross product are unchanged under a random anchored phase drawn
   from the fourth roots of unity: **holds**.

**What the check did not do.** It did not run any kernel proof, did not test any candidate outside
the three named, did not test any rung outside `L4n` and `L5`, and did not probe any configuration
other than the frozen one. Its script is not committed: the round's evidence is the execution's
kernel proofs and nothing computed here.

## The ordering obligation, as it binds a round whose ladder is consumed

Act 21's ordering obligation fixed the ladder before the census. **Here the ladder was fixed before
this freeze, by act 21's merged blob, and this round's obligation is the residue that still
applies:**

> **The ordering obligation, act 22.** The rungs are act 21's declarations at blob `860daac4…` and
> nothing else. The execution's module **states no rung, no equivalence and no top-level definition
> of any kind**; every rung it discharges or refutes is act 21's declaration applied to a family
> pinned by equation. From the first commit that adds the module to the certified head `E`, **no
> commit of the branch adds a definition, restates a rung, or uses an equivalence outside the
> frozen quotient list**, and the candidate `Φ_swap` is pinned in every theorem that names it to
> `fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G` and to nothing else.

### What the execution must record

1. **The declaration table.** For each of `L4n` and `L5`, the act 21 declaration consumed, its line
   range at blob `860daac4…`, and the statement that this round's module carries no declaration of
   its own — checked mechanically by `R7-OLN`, which requires the module to contain no `def`,
   `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`, and to import
   `OIBridge.OrbitLawRigidityTwisted`.
2. **The stage-A commit.** The SHA of the commit that sets the two declarations to `B` and applies
   the supersession table's one edit, and nothing else.
3. **The module commit.** The SHA of the first commit at which the module is present, with the
   named result that entered first.
4. **The immutability span.** The statement, with the command that checks it, that between the
   module commit and `E` no diff introduces a definition:
   `git diff <module commit> <E> -- verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`
   contains no added line beginning with `def `, `abbrev `, `structure `, `class `, `instance `,
   `axiom ` or `opaque `.
5. **The quotient record.** The only equivalence used in any verdict is act 12's `GramPhaseEquiv`,
   with the lemma that uses it, and **no equivalence was introduced or widened**.

### The attestation set, scoped from `B` to the module commit

Act 20's three questions, in act 21's wording at its lines 1033–1043, are answered by the result
note for the span from `B` to the module commit — **Q1 INTENTIONAL**, **Q2 INCIDENTAL**, **Q3
UNAIDED REASONING** — with the partial-fact rule applied. **What the freeze itself places in front
of the execution is not a YES and is listed rather than left implicit**: this file carries the
proof route for every target, the drafting check's outcomes, and — through the start-state table —
act 21's merged theorems and act 21's result note, which records `ΦCTRL`'s failure of `L4n` in
full. The three questions are about what the execution acquired **beyond** the freeze and the
pinned blobs. A YES is disclosed with what was learned and when; it is not concealed and not argued
away, and a disclosure does not cure it.

### The anti-expansion rule, FROZEN

**If execution discovers a fourth candidate law, a further equivalence, a further rung, a further
configuration, a fourth-corner witness, or a strengthening of a merged theorem, it is recorded as an
observation for a later round with its own freeze and is not executed here.** The candidate list is
closed at three, the quotient list at three, the ladder at act 21's `L0`–`L5`, the rungs tested at
`L4n` and `L5`, and the configuration at the frozen product configuration.

## The targets, FROZEN

Five targets, `OF0` through `OF4`. Each names what settles it and what evidence counts.

### `OF0` — does the merged record already decide either rung, or the implication?

**The question.** At `B`, does the merged record contain a statement deciding `L4n`'s or `L5`'s
rung status under act 21's labels, or deciding whether the prefix through `L4n` implies `L5` at the
product configuration?

**What settles it.** Locating and quoting, under act 21's evidence rule at its lines 1456–1467,
over a bounded file set: act 21's `preregistration.md`, `amendments/amendment-1.md` and
`result.md`, act 21's module, act 20's `result.md` and module, and `verification/ROADMAP.md`, with
the terms `L4n`, `L5`, `FactorizesOnProduct`, `TwistedNatural`, `RESTRICTS`, `FREE`, `UNDECIDED`,
`factoriz`, `implies`, `implication`.

**This is a type-P target.** No Lean is written for it, no outcome of it is a theorem, and this
round's own theorems are not retro-evidence about it. **Reconstructive inference is forbidden as a
finding; where the record is silent, the finding is that it is silent.**

### `OF1` — the `L4n` rung status, via `ΦCTRL`

**The statement.** `ΦCTRL`, as `phiCTRL_census` pins it, satisfies `ProperAt`, `PropagatesFrom`,
`EvolvesTotally`, `PreservesAdmissible`, `L2`, `Reversible` and descent at the product
configuration, and at every `t` admits no lift satisfying the lifting obligation, the admissibility
obligation and `TwistedNatural` — which is the `Li-RESTRICTS` shape for `L4n`.

**What settles it.** A Lean theorem at evidence level 2 **obtained from `phiCTRL_census` by
consumption**, restating no rung and re-proving nothing; its statement names the failing conjunct
and the separating classes as act 21's §7 records them.

### `OF2` — the `L5` rung status, via `Φ_swap`, in two parts

**Part (a), the prefix.** `Φ_swap` satisfies the first eight conjuncts of `LadderConds` at the
product configuration — `ProperAt`, `PropagatesFrom`, `EvolvesTotally`, `PreservesAdmissible`, the
inline `L2`, `Reversible`, descent, and the inline `L4n` — each discharged separately, `L4n`
through act 20's merged lift at `σ = Equiv.prodComm (Fin 4) (Fin 4)`.

**Part (b), the failure.** `¬ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1)
(Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ_swap`, by the route frozen under the
candidate: the exchange identity proved explicitly, the two instances, the diagonal cancellation,
the cross equations at `((0,m),(1,m))`, and `norm_num [Complex.ext_iff]` on `1/256 = i/256`.

**What settles it.** One Lean theorem at evidence level 2 whose statement pins `Γ`, `Γ₀`, `H₁`,
`Hᵢ` and `Φ_swap` by equations, as `phiCTRL_census` does, and carries both parts as conjuncts.
**`L5-RESTRICTS` is earned only by both parts together**; part (b) without part (a) is an
observation about a family outside the class and earns no label.

### `OF3` — the positive control

**The statement.** `phiPP_ladder`, consumed: `Φ_{σ×σ}` satisfies `LadderConds` in full at the same
configuration, `L5` with content.

**What settles it.** Consumption, recorded in the result note with the merged theorem's name and
what it states. **No Lean is written for `OF3`.** Its role is to certify that `L5` is satisfiable
with content by a law of the prefix at this configuration, so that `OF2` (b) is a fact about
`Φ_swap` and not about the condition being empty.

### `OF4` — the non-implication

**The statement.** At the product configuration,
`¬ ∀ Φ, (prefix through L4n) Φ → FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1)
(Equiv.refl _) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`, where the prefix is written as the first eight
conjuncts of `LadderConds` and the quantifier ranges over every transition family on
`Fin 4 × Fin 4`.

**What settles it.** A Lean theorem at evidence level 2 obtained from `OF2` by instantiating the
universal at `Φ_swap`. **It is a statement about the exact declarations, at the exact
configuration, for the ordered decomposition `e`**, and about nothing in their neighbourhood.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `OF0` | **negative** — the record decides neither rung status nor the implication | **high** | Act 21's §7 reports both rungs `UNDECIDED` and names the settlement for each; nothing merged since act 21 concerns either. The reading is the freeze's reason; the finding is whatever the execution's bounded search records. |
| `OF1` | **`L4n-RESTRICTS`**, via `ΦCTRL` | **high** | Every conjunct is a conjunct of the merged `phiCTRL_census`; the work is consumption and the shape of the statement. |
| `OF2` (a) | positive | **high** | Every conjunct is a carrier relabelling's, and `phiPP_ladder` proves the same conjuncts for a product permutation at the same configuration; act 20's lift and law are merged at arbitrary `σ`. The one new lemma is the exchange identity, an entrywise `rfl`-shaped computation. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `OF2` (b) | positive — `Φ_swap` fails `L5` | **high** | The drafting check closes the argument exactly; the kernel steps are `phiCTRL_census`'s closing steps with the diagonal-preservation lemma added. **UNDECIDED with the obstruction named is an allowed outcome**, and a failure to close reports the failed obligation and nothing else. |
| `L5`, the rung | **`L5-RESTRICTS`**, via `Φ_swap` | **high**, conditional on `OF2` (a) and (b) | The label is earned only by both parts together. |
| `OF3` | consumed | — | `phiPP_ladder` is merged. |
| `OF4` | positive — the prefix does not imply `L5` | **high**, conditional on `OF2` | Instantiation of the universal at `Φ_swap`. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.
**`L5-FREE` and `L4n-FREE` are not predicted and are not attempted**: each would need a universal
implication proof, and the round attempts none.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
**UNDECIDED is a live preregistered outcome for every target and is not a failure.**

### The outcomes of `OF0`

- **Outcome `OF0`-silent:**
  > On the search this freeze bounds — act 21's control plane, amendment and result note, act 21's
  > module, act 20's result note and module, and `verification/ROADMAP.md`, against the frozen term
  > list — the merged record decides neither the rung status of `L4n` nor that of `L5` under act
  > 21's labels, and does not decide whether the prefix through `L4n` implies `L5` at the product
  > configuration. **The finding is that the record is silent on the point.** It is not a finding
  > that any such statement is false, not a finding that one is unprovable, and not a bound on what
  > a later round could prove.
- **Outcome `OF0`-found:**
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which
  > objects. No merged artifact is edited, and no earlier round's recording is enlarged or corrected.

### The outcomes of `OF1`, `OF2` and the two rungs — act 21's sentences, carried verbatim

- **Outcome `Li-RESTRICTS`**, for a named rung `Li`:
  > An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
  > `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
  > a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
  > statement about the exact condition frozen under the label `Li`, at the configuration named, and
  > it does **not** endorse the condition, does **not** say the programme requires it, and does
  > **not** say it is the right condition to impose.
- **Outcome `Li-FREE`**, for a named rung `Li` — listed so that the label set is complete; not
  attempted here:
  > Every transition family satisfying the earlier rungs of this freeze's ladder satisfies `Li`,
  > proved universally at evidence level 2 at the configuration named. **So `Li` is not a restriction
  > on that class**, and the information it adds to the ladder is none. **The rung stays in the
  > ladder** and stays in the conjunction the headline quantifies over: this is a finding about the
  > condition and not a licence to drop it, and no artifact of this round reports the ladder as having
  > fewer rungs than this freeze names.
- **Outcome `Li`-UNDECIDED**, for a named rung `Li`:
  > The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
  > the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
  > claimed, and no sentence of this round treats the absence of a decision as a decision. In
  > particular the absence of a violating candidate is **not** reported as the rung being free, and
  > the absence of an implication proof is **not** reported as the rung having content.
- **Outcome `Φ`-SURVIVES-PREFIX**, for a named transition family `Φ`, replacing act 21's
  `Φ`-SURVIVES for this round's narrower scope:
  > The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
  > prefix through `L4n` of the ladder act 21 fixes, at the configuration this freeze names for it,
  > at evidence level 2, with each conjunct discharged separately. **This is a statement about the
  > exact family frozen under that label**, and it does **not** endorse it, does **not** say it
  > obtains, and does **not** adopt it as the physical law of evolution.
- **Outcome `Φ`-FAILS**, for a named transition family `Φ` and a named rung:
  > The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
  > evidence level 2, with the failing conjunct and the separating class named. **This settles that
  > family against that rung and nothing in its neighbourhood**, and it is not a statement that
  > families of its shape fail in general.
- **Outcome `Φ`-UNDECIDED**, for a named transition family `Φ` and a named rung:
  > Whether `Φ` satisfies the rung named is undecided in this round, with the obstruction named
  > specifically — the family, the rung, the step and what would settle it. Neither label is claimed.

### The outcomes of `OF4`

- **Outcome `PREFIX-NOT-IMPLIES-L5`:**
  > At the frozen product configuration, the conjunction of the standing `L-PROP` hypotheses with
  > `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and `L4n` at act 20's certified strength does not imply
  > `L5` as act 21 froze it: an exhibited transition family satisfies every conjunct of that prefix
  > and fails factorization into fixed local maps for the ordered decomposition named, at evidence
  > level 2. **This is a statement about the exact declarations at the exact configuration**: it
  > does not say that any surviving law interacts, couples or fails to compose in any other sense,
  > does not say that `L5` fails at any other configuration or decomposition, and does not say that
  > `L5` is or is not the right condition to impose.
- **Outcome `OF4`-UNDECIDED:**
  > The non-implication is undecided in this round, with the obstruction named — which part of `OF2`
  > did not close and at which step. The absence of an exhibited counterexample is not a proof of the
  > implication, and no sentence of this round treats it as one.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The execution appends,
after act 21's sentence in the same cell, exactly the sentence frozen for the case reached.

**Case A — `OF0` silent, `L4n-RESTRICTS`, `L5-RESTRICTS`, `PREFIX-NOT-IMPLIES-L5`.** This is the
case the freeze predicts.

> Act 22 tests two of the rungs act 21 left undecided, at act 21's product configuration and against act 21's unchanged ladder, with a closed list of three named laws frozen with it. Representative-level gauge-naturality at act 20's certified strength has content on the class: act 21's controlled relabelling, named for that rung in advance, satisfies every earlier condition and admits no twisted-natural lift. Factorization over independent systems has content on the class and is not forced by the conditions before it: the relabelling that exchanges the two factors satisfies every condition through gauge-naturality and does not factorize into fixed local maps for the ordered decomposition, so the standing prefix through naturality does not imply factorization at that configuration. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no independence of conditions is asserted, no surviving law is said to interact or to fail to compose in any other sense, act 21's own verdicts stand exactly as act 21 states them, and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

**Three clauses of Case A vary with the outcome, and they vary independently**, each replaced by
the sentence its target's UNDECIDED outcome fixes:

| target | clause | replacement when UNDECIDED |
| --- | --- | --- |
| `OF1` | the sentence beginning "Representative-level gauge-naturality" | "Whether representative-level gauge-naturality at act 20's certified strength has content on the class is recorded undecided, with the obstruction named." |
| `OF2` | the sentence beginning "Factorization over independent systems" | "Whether factorization over independent systems has content on the class, and whether the standing prefix through naturality forces it, is recorded undecided, with the obstruction named; the absence of an exhibited counterexample is not a proof of the implication." |
| `OF4` | the clause "so the standing prefix through naturality does not imply factorization at that configuration" | omitted, the sentence ending at "ordered decomposition" |

**The execution composes the sentence from these substitutions and reports no other wording. No
composition closes `P0`**, and none reports either of its two parts closed.

## Naming a law is not endorsing it, FROZEN

Act 21's four points at its lines 1868–1879 govern here: naming is for testing; the round endorses
none; exclusion is only ever of the precise stated form; the lists are closed at this freeze.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a law's survival could be read as its adoption**, each carriage opening
with one line naming where it is being carried. It is act 21's clause with "Act 21" read as
"Act 22", and nothing else changed.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## What no outcome licenses

These are the forbidden sentences, in terms. None may be written in any artifact of this round, in
any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"This is Schrödinger evolution", "the swap is an entangling gate", "the conditions single out
   quantum dynamics", or any statement that a surviving or failing law is, resembles, approximates
   or points toward quantum evolution.**
2. **"The surviving law is the physical one."** The non-adoption clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
3. **"`L4n` and `L5` are independent", or any report of a square of independences.** Three
   witnesses do not complete it; the fourth corner is outside this round.
4. **"The swap interacts", "couples the systems", "does not compose", or any reading of a failure of
   `L5` as anything but a failure of factorization into fixed local maps for the ordered
   decomposition `e`.**
5. **"`L5` is free" or "`L4n` is free", from the absence of a witness or from anything but a
   universal implication proof**, which this round does not attempt.
6. **"Any parameter set must contain the full permutation group", or any inclusion requirement
   placed on a classification.** What this round's outcome bears on is stated once, in the section
   on what it changes: a full-ladder classification at the product configuration must exclude a
   swap that fails `L5`, and a classification of the prefix must account for it modulo the frozen
   equivalence; **it places no requirement on the separate single-carrier classification**.
7. **"Act 21's `L4n-UNDECIDED` was wrong", or any rewriting of act 21's historical verdicts.** They
   stand; this round's labels are this round's.
8. **"The factor maps' invariants are `1/16` and `i/16`", or any invariant assigned to `Φ₁ G₁` or
   `Φ₂ G₂` from realizability.** The declaration requires none, and the refutation reads them from
   the equivalence and the diagonal cancellation only.
9. **"`relabel_product` gives the exchange identity."** It is stated for product permutations only;
   the exchange identity is proved separately.
10. **"`OL1` shows the evolution preserves the admissible orbit space."** Descent gives maps on the
    ambient quotient and uniqueness of continuation; preservation is `L1`, or the constant-`Γ`
    implication from `L0 ∧ L2 ∧ L4d`.
11. **Any statement about `L1`, `L3i` or `L3s`**, in either direction; about the threading, the
    cross-time representative, the relative evolution or the relative candidate; about act 16's
    cancellation cell; about act 14's carriers; about act 18's `D`-axis; about act 10's anchor axis;
    about Track I, Source B or Source C; or about the substratum Lemma 24.1 rounds.
12. **"`P0` is closed", or "`P0`'s trajectory part is closed."**
13. **"Act 12's classification is strengthened", "act 20's law is enlarged", "act 21's ladder is
    revised."** All are consumed at merged strength.
14. **"The evolution is continuous", "smooth", "generated", "one-parameter"**, or any statement
    resting on structure the index type does not carry.
15. **"OI and QM are inequivalent."**
16. **"The law list is exhaustive", or "the condition list is exhaustive."** Three laws and two
    rungs are tested; nothing outside them is refuted or endorsed here.

## Named hazards

1. **The unnormalized factor maps.** **This is the round's own hazard.** The specific failure guarded
   against is a refutation of `L5` that reads a cross-invariant of `Φ₁ G₁` or `Φ₂ G₂` as `1/16` or
   `i/16` — a value only a realizable Hadamard Gram has — when the declaration requires no
   realizability of them. The frozen route cancels the diagonal, read from the equivalence, and reads
   the invariant equations after; the result note states in terms that no property of the factor
   maps' values was used beyond the two displayed equivalences.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 22 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
2. **The exchange identity assumed.** `relabel_product` covers `prodCongr` and not `prodComm`; a
   proof that rewrites with it at the exchange has proved nothing, and the kernel will say so.
3. **A label from a witness that fails an earlier rung.** Act 21's `DF2` exactly: `L5-RESTRICTS`
   requires `OF2` (a) in full, and a `Φ_swap` failing any conjunct of the prefix earns no label for
   `L5`, whatever part (b) shows.
4. **Substituting a witness.** `ΦCTRL` is the `L4n` countercontrol and `Φ_swap` the `L5`
   countercontrol; neither is tested for the other's rung as a label-earning witness, and any other
   family found during execution is an observation.
5. **Reading three corners as a square.** The fourth witness is outside this round; no independence
   is reported.
6. **Reading factorization failure as interaction.** The swap preserves product form; what fails is
   fixed local maps for the ordered decomposition, and no other sense of composition is at issue.
7. **Enlarging the classification consequence.** Stated once, one-directionally, and never as an
   inclusion requirement on any parameter set.
8. **Rewriting act 21's verdicts.** `L4n-UNDECIDED` and `L5-UNDECIDED` stand as act 21's; this
   round's labels are earned under this freeze and reported as such.
9. **`Li-FREE` from a search.** Not attempted, not reportable from absence.
10. **Restating a rung.** A `def` in this round's module is a defect of the round, and `R7-OLN`
    fails on it.
11. **Choosing a configuration or a decomposition after an outcome is known.** The configuration and
    `e = Equiv.refl` are frozen; a swap that factorized for a *different* ordered decomposition
    would be an observation, not a repair.
12. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.**
    Carried from acts 18 and 21.
13. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
14. **A landing without `P`**, **a stem both declared and recorded**, **a legacy constant
    written**, **editing this freeze after an outcome is known**, **a supersession outside the
    table** — each as act 21's hazards 28, 30, 31 and 34 state them, with `OLN` for `OLT`.
15. **Contamination that no commit records.** The attestation set's third question and the
    partial-fact rule exist for it; the span ends at the module commit.
16. **A `B`-scoped precondition that the freeze's own text falsifies.** Act 21's Amendment 1
    exactly: every `B`-scoped row below is evaluated at `M` before the merge and is written so that
    the presence of this file in the tree does not fail it.

## Non-doings

The round does not: **derive, recognise, approach or claim progress toward quantum evolution**, in
any paraphrase; adopt any surviving law as the physical one; adopt a carrier as the physical one or
define a carrier of its own; endorse any condition or any law; assert or deny that a cross-time law
is required or suffices; **restate, edit, add or remove any rung, or change any conjunction**;
**introduce or widen an equivalence**, or use one outside the frozen quotient list in any verdict;
**test any rung other than `L4n` and `L5`**, or any law outside the frozen three, or any
configuration outside the frozen product configuration, or any decomposition other than
`e = Equiv.refl`; attempt a universal implication proof in either direction; attempt a
characterization, a census or a same-initial-orbit pair; execute or name a fourth-corner witness;
report an independence of rungs; **re-prove or strengthen acts 12, 17, 18, 20 or 21**; revise any
merged label; rewrite, reinterpret or grade any verdict of act 21's note; ask the threading question
or the cross-time representative question, in either direction; touch act 16's cancellation cell;
state anything about act 18's `D`-axis, act 10's anchor axis, act 14's carriers, Track I, Source B
or Source C, or the substratum Lemma 24.1 rounds; realize any transition as an operator, unitary,
generator or group element; introduce continuity, smoothness or a generated evolution; alter any
existing manifest record, or write a legacy seal constant; edit any manuscript; close `P0` or either
of its parts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Act 21's statement at its lines 2130–2143 is carried in full: the question is not asked, not
bounded and not attempted; an execution that begins asking whether any law here looks like unitary
evolution has left the round's scope, and what it finds is recorded as an observation and not
executed. **"Resembles", "is consistent with", "is what one would expect from" and "is a step
toward" are forbidden sentences.**

### What act 22 does and does not change about `P0`, and about the classification

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 22 can
change is the recorded content of two rungs of act 21's ladder, and one implication among them.

**On the classification act 21 named as the obstruction to `L-FAMILY`, stated once and narrowly.**
If `Φ_swap` fails `L5`, then a full-ladder classification at the product configuration must
**exclude** it, and a classification of the prefix through `L4n` at that configuration must
**account for** it, modulo the frozen law equivalence. **This product-configuration result places
no inclusion requirement on the separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`, and no
requirement that any parameter set contain any group.** That is the whole of what this round's
outcome bears on, and it is an observation for the later round that freezes the classification, not
a finding of this one.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about
what fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT
CERTIFIED**.

## Definition budget

**The execution introduces NO top-level Lean definition.** The budget is **zero**, and it is stated
as a number so that it cannot drift: no `def`, `abbrev`, `structure`, `class`, `instance`, `axiom`
or `opaque`. Every rung is act 21's declaration consumed; `Φ_swap`, `ΦCTRL`, the product tuples,
the Hadamard objects, the permutations and the visible families are bound variables pinned by
equations in the statements that need them, as `phiCTRL_census` pins its transition family. The
prefix through `L4n` is written out as the first eight conjuncts of `LadderConds` wherever a
statement needs it, and never abbreviated by a definition. **A definition requires its own
append-only amendment**, separately frozen and merged before the work it affects.

Theorems are not budgeted. The execution proves whatever lemmas its verdicts need — the exchange
identity, the diagonal-preservation lemma, the ladder conjuncts of `Φ_swap`, the projection of
`phiCTRL_census`, the non-implication — as named results, each printed in the axiom table.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `OF1`, for both parts of `OF2`, and for `OF4`,
whichever label each reaches other than UNDECIDED. `decide` over finite index types is permitted;
`native_decide` is not, and neither is `sorry`. `Classical.choice` is expected wherever
`sh1_sufficiency` or `product_realizable` is applied. **`OF0` is type P and carries no evidence
level; `OF3` is consumption and carries act 21's.**

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-OLN`**, reserved here and created by the execution pull request.
The round's stem is **`OLN`**; its seal state is the prospective declaration during execution and
the record `verification/seals/OLN.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 22 object enters the repository tree** — any Lean statement about
   `Φ_swap`, about the exchange identity, about the diagonal lemma, about `ΦCTRL`'s rung shape or
   about the non-implication; any probe clause; any result artifact; any manifest record or
   declaration for `OLN`. **The single permitted exception is the analysis recorded inside this
   control-plane blob itself**, merged *as* the freeze, including the proof routes, the drafting
   check and the supersession simulation.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'OLN': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('OLN',)}`, both outside the validator's marker-bounded regions, and applies the supersession
   table's one edit, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('OLN', tag='R7-OLN')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed — the validator's `EXECUTION` classification.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `OLN` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/OLN.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `OLN` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `OLN` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `OLN`.
9. **No `_OLN_BASE`, `_OLN_SEALED_HEAD` or `_OLN_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-OLN`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains no
    top-level definition of any kind, by extraction of every declaration keyword at line start;
    (b) the module imports `OIBridge.OrbitLawRigidityTwisted`; (c) every theorem naming the swap
    pins it to `RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4))` and no other permutation; (d)
    the stage-A commit and the module commit are on the first-parent chain from `B` to `E`, in that
    order. A synthetic `def` inserted into the module text, a synthetic `prodCongr` substituted for
    `prodComm`, and a fabricated SHA off the chain each **fail** the control.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table and the five records;
    the three attestation answers for the span `B` → module commit; the sentence that no rung was
    restated and no equivalence was widened; each rung label carried with its frozen sentence
    verbatim and with the failing conjunct and separating classes named; **the statement that no
    property of the factor maps beyond the two displayed equivalences was used**; **the statement
    that no independence of rungs is asserted**; **the statement that act 21's historical verdicts
    stand unchanged**; the one-directional reading of what the swap separates; THE CLAUSE carried
    complete at every mention with its count; and the frozen `P0` sentence for the case reached
    present in `verification/ROADMAP.md` verbatim, after act 21's.

### The contract this round supersedes, named in advance

**Under `§A.37`'s closed-round rule, `AGENTS.md` lines 1055–1061, this section is the
authorization.** One closed round's guard carries one contract that reads the **current** round's
declared baseline rather than the state that round manifested, and it fails on any act 22 head for
a reason that has nothing to do with act 22's result. **The failure was measured, not inferred**: at
drafting time a throwaway simulation of an act 22 execution head — one Lean file added, the two
declarations set to `D` with a stem of the same shape — and of its landing and pin — the record
written, the declaration emptied — was run against the guard at `D`. With no disposition applied,
**exactly one** tag went red on the execution head, `R7-OLT`, its authority and ordering conjuncts
both passing; with the disposition below applied, the execution head ran green with every tag
`PASS`, and the landing and pin state — a landing merge of the simulated head onto `D` followed by
a pin commit writing the simulated record with `sealed_head` the simulated head and `merge` the
simulated landing, and emptying the declaration — ran green with every tag `PASS`, the simulated
record admitted by the declared baseline as its one authorized addition and `OLT` still classified
`ARCHIVED`. The simulation's stem was a placeholder and not `OLN`, it carried no guard clause of
its own, and its commits exist on no branch of the repository.

| guard | contract | why an act 22 head fails it | disposition |
| --- | --- | --- | --- |
| `R7-OLT` | `N14`, `_olt_declarations`: act 21's seal state, mode-aware — the conjunct `_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)}` is required in **both** branches, declared and recorded | from act 22's first commit the declared baseline is act 22's, `{'base': B, 'authorized': ('OLN',)}`, while `OLT` is recorded; the conjunct compares a closed round's contract against the current round's declaration | **read over the state `OLT` manifested**: the baseline equality is required only in the **declared** branch, where it is act 21's own executing-mode state; in the **recorded** branch the contract requires exactly what it already requires there — `OLT` not declared, and `OLT.json` `kind: "sealed"` with `base` equal to act 21's mandated base literal `_OLT_B` — and nothing about the current round's baseline. Concretely, the two statements `if not (_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)}): return False` are removed and the declared branch becomes `return (_MANIFEST_BASELINE == {'base': _OLT_B, 'authorized': ('OLT',)} and _MANIFEST_PROSPECTIVE['OLT'] == _OLT_B)`; the recorded branch is unchanged; the docstring is unchanged |

What this table does **not** do: it does not edit any frozen document, does not change what act 21
recorded as its outcomes, does not touch any negative case, mutation control or tag map, and does
not reopen anything adjudicated. **It is the same rule act 21 applied four times to `SI-1`, `SI-2`
and `SI-3`**, applied once to act 21's own clause, and it is the rule's second application to a
Track B round: a closed round's contract about the current declaration is a contract about *that
round's* declaration, and the closed-round rule is how it is read. `R7-SI1`, `R7-SI2` and `R7-SI3`
already read over their own executions and manifested records since act 21's dispositions, and the
simulation confirmed that none of them fails on an act 22 head.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-OLN' D`, `git grep -l -- '_OLN' D`, `git grep -l -- 'OLN' D`, `git grep -l -- 'OrbitLawNaturalityFactorization' D` and `git grep -l -- 'act-22' D` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `90d5a4ae59c931216d52a8ce9456ae906366085e`, twenty-six records, twenty `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green and carries no legacy constant | eighty-five `R7-*` tags, all `PASS`, on main-push run 35433619877; `_SI2_LEGACY_RE` finds zero assignment statements |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each of the first nine paths of the start-state table has at `B` the blob the table names (the `frozen-blob` lines of the block) |
| 6 | `B` | No act 22 execution object exists | the guard file at `B` contains no `R7-OLN` and no `_OLN`; no `verification/seals/OLN.json`; no `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Act 21 is sealed at `B` | `verification/seals/OLT.json` at `B` carries `round` `OLT`, `kind` `sealed`, `base` `10d1041bcc10f25d9f643629d4431acbd0f65a1e`, `sealed_head` `b27f3f1630a25667b6728518d06b55fbdabe0d11`, `merge` `4bd732c54e0804bda3b796fcb93e91b5c4299b87`; the guard file at `B` carries the `R7-OLT` check |
| 9 | `B` | Act 21's module is wired | `OIBridge.lean` at `B` imports `OIBridge.OrbitLawRigidityTwisted` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md` exists at `B`; its blob is the one the `R7-OLN` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are not inputs. **The claim is scoped to the repository record.**

```control-plane-preconditions
d: d08b932da492891bdadaa5b867fd337250859b99
merged: false
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean 860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean 4c1137f35600320b9273c857ec62271341b05cd0
frozen-blob: verification/lean-mathlib/OIBridge/TwoSidedGauge.lean 4bba2040c33424fafbc6d31c0d63b86dff33691a
frozen-blob: verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean cb14c43b0becfe1a379ae3615d5553723ede9163
frozen-blob: verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean afc22cfc93b244c80e1c55a273dcfda1ddebb121
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-OLN' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_OLN' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'OLN' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'OrbitLawNaturalityFactorization' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'act-22' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 90d5a4ae59c931216d52a8ce9456ae906366085e", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-OLN' -e '_OLN'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'OLN.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'OrbitLawNaturalityFactorization'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: act 21 sealed
{"id": "b8-olt-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLT.json | tr -d ' \\n' | grep -e '\"round\":\"OLT\",\"kind\":\"sealed\",\"base\":\"10d1041bcc10f25d9f643629d4431acbd0f65a1e\",\"sealed_head\":\"b27f3f1630a25667b6728518d06b55fbdabe0d11\",\"merge\":\"4bd732c54e0804bda3b796fcb93e91b5c4299b87\"'", "expect": "nonempty"}
{"id": "b8-olt-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLT'\"", "expect": "nonempty"}
# row 9: act 21's module wired
{"id": "b9-import", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawRigidityTwisted$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md", "expect": "exit0"}
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
- **The stage-A commit comes first**, then **the module commit**, and their SHAs are recorded; the
  attestation set is answered for the span `B` → module commit.
- **Then exactly one execution pull request**, based on `B`, carrying the Lean module, the result
  note, the `R7-OLN` guard clause, the two declarations, the supersession table's one edit and
  nothing else in `R7-OLT`, the `ROADMAP` propagation and the census entry. **No manuscript
  changes.**
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
   altered, no legacy constant written, and the base-blob verification recorded;
2. **the ordering obligation's five records** and the attestation set's three answers for the span
   `B` → module commit, with the freeze-supplied facts listed;
3. **`OF0`** — the bounded search, recorded in full;
4. **`OF1`** — `L4n`'s label with its frozen sentence, the consumed theorem named, the failing
   conjunct and separating classes as act 21's §7 records them, and the statement that act 21's
   `L4n-UNDECIDED` stands as act 21's verdict;
5. **`OF2`** — `Φ_swap`'s prefix conjuncts each reported separately, the exchange identity reported
   as proved, `L5`'s label with its frozen sentence, the separating classes and invariant named,
   and **the statement that no property of the factor maps beyond the two displayed equivalences
   was used**;
6. **`OF3`** — `phiPP_ladder` consumed, and what it certifies;
7. **`OF4`** — the non-implication in the frozen sentence, with the one-directional reading of what
   the swap separates and **the statement that no independence of rungs is asserted**;
8. **the scope boundary as honoured**: nothing derives, recognises or approaches quantum evolution;
   `L1`, `L3i`, `L3s` untouched; act 21's verdicts untouched; the threading, act 16's cell, act
   18's `D`-axis, act 10's anchor axis and act 14's carriers untouched;
9. **the non-adoption clause carried verbatim at each mention**, with the count of carriages;
10. the frozen `P0` sentence for the case reached, appended after act 21's, the row's label
    unchanged;
11. what no outcome licenses, in this file's wording, and the status rule as honoured;
12. the relation to acts 12, 17, 18, 20 and 21 — every merged label consumed, none revised;
13. the definition count against the zero budget;
14. the chronology certification, naming the property certified, the ten preconditions with their
    scopes and the block's rows as the base check reported them at `M` and at `B`, the validator's
    classification of `OLN` at `E`, `L` and `P`, the supersession table's one edit reported as a
    measurement with its negative control, and `SI-3`'s standing contract reported as holding;
15. the axiom table with one line per named result;
16. the discrepancies, if any, recorded and not repaired;
17. the observation, if any, for the classification round, stated once and narrowly as the
    non-doings section fixes it.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Every item below is a call
already made**, and the body of this freeze is written to them throughout. **This freeze carries no
open decision.**

1. **The round is narrow.** Two rungs, `L4n` and `L5`; three named laws; one configuration; act
   21's ladder, quotient list, configuration, one-`|A|` limitation and non-adoption clause
   preserved unchanged. Act 21's other undecided rungs are not touched.
2. **The primary target is `Φ_swap` against unchanged `L5`**: it satisfies every standing hypothesis
   and rung through `L4n` and fails `L5` as act 21's declaration states it.
3. **The normalization gap is closed in the proof route.** The declaration requires nothing of the
   factor maps' values; the refutation uses the two instances' diagonal equations and their
   cross-invariant equations, cancelling the nonzero diagonal exactly as `phiCTRL_census` does, and
   the exchange identity is proved explicitly, `relabel_product` covering `prodCongr` only.
4. **What the swap separates is stated precisely and one-directionally**: factorization into fixed
   local maps for the ordered decomposition `e`; the prefix through `L4n` does not imply that `L5`;
   no interaction and no general failure of composition is claimed.
5. **The classification consequence is narrowed** to exclusion from a full-ladder classification
   and accounting in a prefix classification, modulo the frozen equivalence, with no inclusion
   requirement on any parameter set and none on the single-carrier classification.
6. **Status language is one-directional.** No independence square; the fourth corner stays outside
   this round; a swap that fails as a counterexample reports the failed obligation; `L5-FREE`
   requires a universal proof and is not attempted.
7. **`OL1` is carried at its exact strength**: descent gives maps on the ambient tuple quotient and
   uniqueness of continuation; preservation of the admissible orbit space is `L1`, or the
   constant-`Γ` implication from `L0 ∧ L2 ∧ L4d`.
8. **The rider names `ΦCTRL` prospectively for `L4n`**, consuming `phiCTRL_census`; act 21's
   historical verdict is unchanged.
9. **`ΦPP` is the positive control**, consumed.
10. **The drafting check is authorized and recorded** as pre-freeze observations, beside the proof
    reasoning, and is not evidence.
11. **`§A.37`'s `D`/`B`/`M` vocabulary governs**: scoped precondition rows, mode `M` validation of
    the candidate merge before the merge, `B` reserved for the certified control-plane merge.
12. **SEALING**, under the manifest protocol: stem `OLN`, tag `R7-OLN`, `E` → `L` → `P` with `P`
    mandatory, the prospective declaration during execution and the record from `P`; the one
    supersession in `R7-OLT` authorized as the table names it, measured in simulation at drafting
    time, and nothing else in that guard touched.
13. **The definition budget is zero.** Act 21's declarations are consumed and none is restated.
14. **Acts 12, 17, 18, 20 and 21 are consumed at merged strength**: not re-proved, not strengthened,
    not redefined.
