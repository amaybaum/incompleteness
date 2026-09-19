# Track B act 23 — the gaps of act 21's ladder, bundled: `L1`, `L3i`, `L3s` and the fourth corner of `L4n`/`L5`, at act 21's product configuration: CONTROL PLANE

Owner-called. This file is the whole of act 23's control plane and is merged **alone**, before any
execution object exists. It is the **first bundled round**: four targets frozen together, each with
its own preregistered proposition, its own named witness, its own verdict rule and its own failure
interpretation, executed in a fixed order with one verdict commit per target, so that the round can
settle several rung statuses at once without a failure on one target contaminating another. It
re-opens nothing of act 21's census, changes no rung, adds no rung, widens no equivalence, and tests
exactly the three rungs act 21 reported undecided and act 22 did not touch — `L1`, `L3i`, `L3s` —
and the one corner of the `L4n`/`L5` square act 22 left outside, at act 21's own frozen product
configuration. The ladder, the quotient list, the configuration, the one-`|A|` limitation and the
non-adoption clause are act 21's, **consumed unchanged**; act 22's three verdicts are consumed
exactly as landed and are neither rewritten nor reinterpreted.

It is **not** a re-run of act 21 or act 22, **not** an attempt to characterize the surviving class,
**not** a report of an independence of any two rungs, and **not** an attempt to derive or to recognise
quantum evolution, which stays an explicit non-doing.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The commit vocabulary this freeze uses, fixed first

`AGENTS.md` `§A.37`, at the drafting snapshot, **lines 713–729**, gives a control plane three commit
names, and this file uses them in exactly that sense:

- **`D`, the drafting snapshot** — `59c1b7efe36d7768cf53120997ff201e32c8e458`, certified `main` at
  the landing of act 22 (#684), whose main-push run 35441377788 is fully green with the
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
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'OLG': B}` | **declared**; the validator classifies `OLG` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLG',)}`, in the same file | the seals tree at `B`, read from git, plus the one addition this freeze authorizes, by stem | unchanged; `OLG.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/OLG.json` | **absent** | **written by `P`**: `{"round": "OLG", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `OLG` as `ARCHIVED` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
writes `OLG.json` and removes the `OLG` entry from the prospective declaration, and touches nothing
else. Without `P` the round sits at `LANDED-PENDING-PIN`, permitted at `L` itself, and every head
descending from that unpinned landing fails as *seal pending*.

**No legacy seal constant is written, at any commit of the round.** Nothing matching
`_OLG_(BASE|SEALED_HEAD|MERGE)` exists at any commit, `SI-3`'s standing contract holds at every
head, and the execution's guard clause certifies chronology through one keyed call,
`_si2_authority('OLG', tag='R7-OLG')`, and never through a per-round constant.

### The lifecycle derivation, and why it comes out SEALING

The rule the owner set for act 19 and act 21 is carried: a round is sealing **if and only if** its
execution creates a new formal object whose chronology matters to the result.

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the four witnesses' ladder conjuncts and failures, and the corner proposition.
2. **Their chronology is load-bearing.** The round's claim is that its four witnesses, their
   authorized targets, its execution order and its proof routes were frozen — here, in this file —
   before any kernel work, and that no witness was reassigned, no rung restated and no equivalence
   widened to reach any verdict; a validator-certified ancestry rooted at this control plane's merge
   commit is what makes that checkable.
3. **A new module with new named results is new seal state**, which only a sealing round's `P` may
   record.

**Therefore act 23 is SEALING, and it owns no other seal state.**

### The tag, the stem, the module and the round directory are free at `D`

At `D`:

- `git grep -l -- 'R7-OLG'` returns nothing anywhere in the tree, and the tag is absent from the
  **eighty-six** `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries at `D`.
- `git grep -l -- 'OLG'` returns nothing anywhere in the tree — the bare three-letter form occurs in
  no text file and in no binary artifact, as a word or as a substring — so a bare-stem search for it
  is unambiguous, and `git grep -l -- '_OLG'` returns nothing.
- No record `verification/seals/OLG.json` exists; the twenty-seven records at `D` use the stems
  `A12P`, `A6D`, `A6I`, `A6P`, `ABR`, `CLG`, `CTI`, `HYA`, `HYB`, `HYE`, `OLN`, `OLT`, `PC4`, `PC4S`,
  `PQT`, `RBR`, `RNC`, `RNT`, `SGT`, `SI1`, `SI2`, `SI3`, `TCF`, `TRJ`, `TSG`, `WTS` and `XTS`, and no
  substring search for `OLG` reaches any of them.
- **The alternatives were checked before `OLG` was chosen**, and the check is recorded so that the
  choice is not re-litigated. `OLU` (undecided rungs) was the first choice and was rejected: its bare
  form is a substring of ordinary words and `git grep -l -- 'OLU'` matches thirty-eight files at `D`.
  `OLC`, `OLP`, `OLQ` and `OLZ` each match one file, `OLY` two, `OLA` thirty. `OLG`, `OLH`, `OLK`,
  `OLM`, `OLW` and `OLX` match nothing; `OLG` — orbit-law gaps, the undecided rungs and the missing
  corner this round tests — was chosen among them. `OLT` is act 21's and `OLN` act 22's, excluded on
  that ground alone.

**The round directory and the module name are free at `D` too.** `git grep -l -- 'act-23'`,
`git grep -l -- 'orbit-law-gaps'` and `git grep -l -- 'OrbitLawGaps'` return nothing. The round
directory is `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/` and the module is
`verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`.

### What this round does NOT own, named exhaustively

It alters **no existing manifest record**. The twenty-seven records under `verification/seals/` at
`D` — the seals tree `981a23a164b091ae0093facf81f7bd5ccf12e004`, twenty-one `sealed` and six
`base-only` — are **read and never written**; the one addition this freeze authorizes is `OLG`. It
writes **no legacy constant**. It does not re-pin, re-derive or re-declare any other round's seal:
`OLT.json`, `OLN.json`, `RNT.json` and the rest belong to the rounds that set them. Inside the
guard file the execution **adds** the `R7-OLG` clause and **sets** the two stem-free declarations
named above — and changes nothing else in the file. **No contract of any closed round is
superseded**, and the measurement that none needs to be is recorded in the chronology section.

## Provenance — what this freeze carries from acts 21 and 22, and what is its own

**The rule.** Act 23 consumes act 21's ladder, quotient list, configuration, witness supply and
non-adoption clause **unchanged**, consumes act 22's three verdicts exactly as landed, and adds four
transition families, four targets, a bundling discipline and its own lifecycle. Every rung is the
declaration act 21's merged module carries, pinned by blob at `B`; **no rung is restated in this
round's module**, and a restatement would be a defect of the round.

| act 21 section (frozen blob `316d635a…`, line range) | this file | status |
| --- | --- | --- |
| the ladder `L0`–`L5`, lines 735–946 | consumed as `EvolvesTotally`, `PreservesAdmissible`, `Reversible`, `FactorizesOnProduct`, `LadderConds` and the inline `L2`, `L4d`, `L4n` of `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` at blob `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` | **consumed unrestated** |
| the frozen quotient list, lines 703–733 | the same three equivalences, no fourth | **carried unchanged** |
| the frozen product configuration, lines 1263–1267 | the same configuration, for every target | **carried unchanged** |
| the rung labels and their earning conditions, lines 926–946 | carried verbatim, with the earlier-prefix of each rung fixed below in `LadderConds` order | **carried verbatim** |
| the witness supply, lines 1369–1414 | the same supply, extended by act 21's and act 22's merged lemmas and by one new family frozen here | **carried, extended** |
| the status-rule sentences `Li-RESTRICTS`, `Li-FREE`, `Li-UNDECIDED`, lines 1676–1700 | carried verbatim below | **carried verbatim** |
| the attestation set, lines 1033–1043 | carried verbatim, asked at **every** boundary of this round | **carried, re-scoped** |
| THE CLAUSE, lines 1897–1905 | carried verbatim with "Act 21" → "Act 23" in its first sentence | **carried, one substitution** |
| `L1`, `L3i`, `L3s` obstructions, act 21's result `bb02ef41…` lines 412–438 and 455–482 | the constructions those passages name as what would settle each rung, made concrete at the product configuration and frozen as this round's witnesses | **answered, not edited** |
| act 22's verdicts, act 22's result `b0f9ae48…` line 10 | consumed as `L4n-RESTRICTS`, `L5-RESTRICTS`, `PREFIX-NOT-IMPLIES-L5`, unchanged | **consumed as landed** |
| act 22's fourth corner, act 22's freeze `cc83ddb9…` lines 598–603 and result lines 372–374 | the corner named there, frozen here as a target | **answered, not edited** |
| everything else — the shared theorem, the census, `SIOP`, the headlines, the `P0` sentences of acts 21 and 22 | not this round's | **untouched** |

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
manifested) are the passages acts 21 and 22 quoted at their own bases, unchanged in wording at `D`.

### The obligation, and what acts 21 and 22 left in front of it

`verification/ROADMAP.md`, **line 63**, the `P0` row, carries act 21's and act 22's frozen Case A
sentences at its end; the row's label is **OPEN** and two-part, and this round appends its own
frozen sentence after act 22's and changes the label of nothing.

`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md`, blob
`bb02ef41eb221696ffa45c9281b69553c8279cbb`, the three obstructions this round acts on:

**lines 421–438**, `L1`:

> **The rung**: `L1`, the preservation of admissibility for the relation on the whole per-slice orbit
> space. **The conjunct**: the implication from the earlier rung `L0` alone. **The step at which the
> proof stopped**: the freeze's reason — every value of the induced evolution is a slice of a
> pointwise realizable solution — reaches only the classes solutions reach, and at a time `t ≥ 1` a
> transition family satisfying `L0` is unconstrained on classes no solution reaches […]

> **What would
> settle it**: a frozen candidate satisfying `L0` and the standing hypotheses at a time-inhomogeneous
> transition and failing `L1` off the reached classes, or a universal proof from `L0` alone. **An
> observation, recorded and not executed**, under the anti-expansion rule: a transition that at time
> `0` sends one named class onto another and at later times sends the then-unreached class to a
> non-realizable tuple would be such a candidate; it is an eighth law, outside the frozen list, and
> carries no label here.

**lines 464–482**, `L3i` and `L3s`:

> **The step at which the
> proof stopped**: the named countercontrol `ΦC`, the constant transition to `G(H₁)`, **fails `L3i` and
> `L3s` exactly as the freeze predicted** […] **but it is not an `L-PROP` law**: […] **it fails clause (ii)** — from time `1` on every solution sits
> at the one class `[G(H₁)]` […]

> **What would settle it**: an `L-PROP` law, on a later round's frozen list, that
> merges two admissible classes — a partial collapse rather than a total one — or misses one […]

`verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md`,
blob `cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea`, **lines 598–603**, the corner:

> **The fourth corner is outside this round.** A law failing `L4n` and satisfying `L5` — a
> class-conditional relabelling on one factor tensored with the identity, for instance — would be the
> witness that, together with `ΦCTRL` (fails both), `Φ_swap` (satisfies `L4n`, fails `L5`) and `ΦPP`
> (satisfies both), would complete a square of independences. **It is not on this freeze's list, it is
> not executed here, and no sentence of this round reports an independence of the two rungs.**

and act 22's result, blob `b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e`, **lines 372–374**:

> **No independence of rungs is asserted**: `ΦCTRL`
> fails both rungs, `Φ_swap` satisfies `L4n` and fails `L5`, `ΦPP` satisfies both, and the fourth corner
> — a law failing `L4n` and satisfying `L5` — is outside this round, unexecuted and unnamed.

### The act 21 declarations this round is stated over

`verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`, blob
`860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8`: `EvolvesTotally` at **lines 96–107**,
`PreservesAdmissible` at **108–116**, `Reversible` at **123–134** (the first conjunct `L3i`, the
second `L3s`), `FactorizesOnProduct` at **143–157**, `LadderConds` at **179–196**, `ol1a_descent` at
**279**, `realizable_of_gramPhaseEquiv` at **355**, `realizable_relabel` at **388**,
`relabel_gramPhaseEquiv` at **397**, `relabel_relabel_symm` at **405**, `relabel_symm_relabel` at
**412**, `gramPhaseEquiv_of_relabel` at **420**, `witness_supply` at **431**, `siop_yes` at **650**,
`phiC_census` at **746**, `l1_free_on_shared_class` at **933**, `product_cross` at **963–973**,
`relabel_product` at **975–984** (stated for `Equiv.prodCongr σ₁ σ₂`), `product_realizable` at
**1015**, `hadamard_entries` at **1062–1090**, `product_separations` at **1093** and
`phiCTRL_census` at **1282–1316**, whose `L4n` refutation, **lines 1462–1536**, is the argument the
corner witness re-uses: a weak anchored gauge `K = diagonal c` with `c` equal to `−1` at one
product index and `1` elsewhere, the lifting equation read at `U K` and at `U` on the relabelled
branch and on the identity branch, the induced right map's phases `c'` forced to `−1` by the one and
to `1` by the other.

The exact shape of `PreservesAdmissible` and of `Reversible`, verbatim, which is what "unchanged
`L1`", "unchanged `L3i`" and "unchanged `L3s`" mean:

```
def PreservesAdmissible (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ∀ t (G : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ (t + 1)) (Φ t G)
```

```
def Reversible (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  (∀ t (G G' : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ t) G' →
      GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G')
    ∧ ∀ t (G' : V → Matrix V V ℂ), RealizableGram A (Γ (t + 1)) G' →
        ∃ G : V → Matrix V V ℂ, RealizableGram A (Γ t) G ∧ GramPhaseEquiv (Φ t G) G'
```

**Two features are load-bearing and are named now.** `L1` quantifies over **every** realizable `G`
at every `t`, reached by a solution or not, and over every `t`, so a time-inhomogeneous family may
fail it at `t = 1` on a class no solution reaches. `Reversible`'s two conjuncts are separate
propositions on the same `Φ`; a verdict on one is not a verdict on the other, and this freeze names
a separate witness for each.

### The act 22 declarations consumed

`verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean`, blob
`d41b157a3f38d4ebedbe11ad9682a8693836a383`: `relabel_prodComm` at **line 69**,
`gramPhaseEquiv_diag` at **82**, `phiCTRL_l4n_restricts` at **109**, `phiSwap_l5_restricts` at
**179** and `prefix_not_implies_l5` at **360**. Consumed for what they state; none is re-proved and
none is used as a witness here.

### The act 20, act 12, act 13 and act 18 declarations consumed

`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, blob
`4c1137f35600320b9273c857ec62271341b05cd0`: `TwistedNatural` at **lines 128–140** — its second
closure conjunct, `∀ K, WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR K)`, and its right
intertwining conjunct, `∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * αR K`, are the two
the corner's refutation reads — `RelabelTransition` at **167–168**, `RelabelLift` at **181–182**,
`rnt2_lifting_property` at **226**, `rnt2_admissible` at **245**, `rnt3_law_exact` at **375**.
`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob
`4bba2040c33424fafbc6d31c0d63b86dff33691a`: `LeftFibreGroup` at **78**, `FibreGram` at **95**,
`GramPhaseEquiv` at **102–103**, `RealizableGram` at **108–110** (its fourth conjunct,
`∀ i j, G i j j = (Γ i j : ℂ)`, is what the product-marginal lemma below reads), `sh1_necessity` at
**168**, `fibreGram_mul_weak_apply` at **242**, `gramPhaseEquiv_cross_invariant` at **870**,
`hadamard_slices_not_twoSided` at **907**, `sh1_sufficiency` at **1070**.
`verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`: `WeakAnchorStabilizer` at **114**,
`weak_anchor_coeff_norm_one` at **146**, `weak_preserves_admissible` at **273**.
`verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean`, blob
`afc22cfc93b244c80e1c55a273dcfda1ddebb121`: `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`,
`gramPhaseEquiv_trans` at **141–170**.
`verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean`, blob
`cb14c43b0becfe1a379ae3615d5553723ede9163`: `ProperAt` at **167–171** and `PropagatesFrom` at
**186–193**, with its two clauses.

## Start state, pinned by blob

Pinned **by blob** at `D`. Blob identity is authoritative: the commit locates the tree, the blob is
what is compared, and the `D → B` rows of the block below require each of these unchanged at `B`.

| path | blob at `D` |
| --- | --- |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean` | `d41b157a3f38d4ebedbe11ad9682a8693836a383` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md` | `316d635a31f91faebeeebef7688b30002d24b4ca` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md` | `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1` |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md` | `bb02ef41eb221696ffa45c9281b69553c8279cbb` |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md` | `cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea` |
| `verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md` | `b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e` |
| `verification/seals/OLT.json` | `8ed0ef5391410db3a112cbe845d27536b7c1ab9b` |
| `verification/seals/OLN.json` | `1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb` |
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | `6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `tools/control_plane_base_check.py` | `d6d6578201a9cab3fcb91d63f4818b38104fc4e4` |
| `tools/control_plane_lint.py` | `7678dbe25f51e6e6b14f07e8842f1b6d205f4fed` |

Every one of these is read and never written by this round. If any blob differs at `B`, the
execution records the discrepancy and does not repair the freeze — and for the first thirteen, the
base check has already refused the merge.

### The files this round writes

**The files this round writes are named separately and are not in the table above.** Each is
pinned by blob at `D` all the same, so that a discrepancy in what the round writes onto is as
visible as a discrepancy in what it reads; a difference at `B` in any of them is recorded in the
result note as a discrepancy and the freeze is not repaired.

| path | blob at `D` | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `1379654dd278502ce0b588c6b0dac94b9314f2e7` | **read** as the pinned statement of the `P0` row, and **written** only by appending the frozen post-round sentence for the vector reached after act 22's sentence in the same cell; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `36bb18b1ca7430f6dec6bc9877e4b51a1c0fef52` | the `R7-OLG` clause **added**; `_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` **set** as the shape section states, the former emptied by `P`; **nothing else**; no contract of any closed round touched; no legacy constant written |
| `verification/lean-mathlib/OIBridge.lean` | `30a4d439a3ac17e408ea9298292d8070078a8e69` | one import line added directly after `import OIBridge.OrbitLawNaturalityFactorization`, at line 211 at `D` |
| `verification/lean-manuscript-census.json` | `0c258131533c2754cf8bd1b1d851f9dee6cd9fdf` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/result.md` | — | created by the execution |
| `verification/seals/OLG.json` | — | created by **`P`**, and by nothing before `P` |

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

The base is fixed the moment this file merges, and whatever sibling lanes have landed in `main` by
then is a fact about the base's tree and not a fact about this round's inputs. The start-state
table above is the complete list of what this round consumes, and a file present at `B` and absent
from that table is read by nothing in this round. The seals tree at `B` is whatever `B` carries;
the execution records the tree it found, and the declared baseline reads it from git.

## Source scoping, carried from acts 13 through 22

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what acts 21 and 22 left in front of it

Act 21 reached `L-WIDE` over the complete ladder and left five rungs undecided. Act 22 settled two of
them, `L4n` and `L5`, and the non-implication from the prefix through `L4n` to `L5`, and left three
things in front of the programme:

1. **`L1`, `L3i` and `L3s` are undecided for one reason each, and act 21's note names, for each, the
   shape of what would settle it.** For `L1` the obstruction is that `L0` constrains a transition
   family only on the classes its solutions reach, so a time-inhomogeneous family can be
   unconstrained at `t ≥ 1` on an unreached class; the note names the settling construction — a
   transition that at time `0` sends one class onto another and at later times sends the
   then-unreached class to a non-realizable tuple — as an eighth law outside act 21's list. For `L3i`
   and `L3s` the obstruction is that act 21's countercontrol `ΦC` is not an `L-PROP` law: a total
   collapse fixes every later slice on its own; the note names the settling construction — a partial
   collapse that merges two classes, or a law that misses one. None of the three was frozen in act
   22, whose freeze says so in terms.
2. **The fourth corner of the `L4n`/`L5` square is unexecuted and unnamed.** `ΦCTRL` fails both
   rungs, `Φ_swap` satisfies `L4n` and fails `L5`, `ΦPP` satisfies both; a law failing `L4n` and
   satisfying `L5` is the corner act 22's freeze describes and forbids itself to execute.
3. **The three rungs and the corner share one configuration, one quotient and one witness
   infrastructure** — act 21's product configuration, act 12's slice equivalence, the Hadamard
   objects, the product embedding and its merged lemmas, act 20's relabelling lift — so one control
   plane can carry all four with their verdicts kept formally separate. That is what this round does,
   and the bundling discipline below is what keeps the four verdicts separate.

**Each target's proof route is the freeze's reading and not a finding**; whether it closes is for the
execution to establish, and every target may end `UNDECIDED` with its obstruction named.

### What act 23 inherits, and consumes without re-proving

Consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**, and a
merged statement is not enlarged by being consumed.

1. **Act 21's ladder**, as the declarations of its merged module, and **act 21's rung verdicts**
   `L0-RESTRICTS`, `L1-UNDECIDED`, `L2-RESTRICTS`, `L3i-UNDECIDED`, `L3s-UNDECIDED`, `L4d-HYP`,
   `L4n-UNDECIDED`, `L5-UNDECIDED`, its `SIOP-YES` and its `L-WIDE`, all of which stand as act 21
   states them. **Act 21's historical verdicts are not changed by anything here**: this round earns
   its own rung labels under its own freeze, and act 21's note is not edited.
2. **Act 22's verdicts** `L4n-RESTRICTS` via `ΦCTRL`, `L5-RESTRICTS` via `Φ_swap` and
   `PREFIX-NOT-IMPLIES-L5`, exactly as landed, with act 22's one-directional reading of what the swap
   separates; **the swap witness is not reinterpreted**, and act 22's note is not edited.
3. **Act 21's `OL1`, at its exact strength**, as act 22 read it: descent gives maps on the ambient
   tuple quotient and uniqueness of continuation; preservation of the admissible orbit space is
   `L1`, or the constant-`Γ` implication `l1_free_on_shared_class` from `L0 ∧ L2 ∧ L4d`, which is
   **not** the implication `L1-FREE` asks for, `L2` being a later rung.
4. **Act 21's product-embedding results**: `product_realizable`, `product_cross`, `relabel_product`
   (for product permutations), `relabel_one`, `hadamard_entries`, `product_separations`,
   `witness_supply`, `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_relabel_symm`,
   `relabel_symm_relabel`, `gramPhaseEquiv_of_relabel`, `realizable_of_gramPhaseEquiv`,
   `ol1a_descent`, `siop_yes` and `phiC_census`, the last two consumed only for the separations they
   carry.
5. **Act 22's `relabel_prodComm` and `gramPhaseEquiv_diag`.**
6. **Act 20's `TwistedNatural`, `RelabelTransition`, `RelabelLift`, `rnt2_lifting_property`,
   `rnt2_admissible`, `rnt3_law_exact`**, at arbitrary `V`, `A`, anchor and `σ`.
7. **Act 12's `GramPhaseEquiv`, `RealizableGram`, `FibreGram`, `gramPhaseEquiv_cross_invariant`,
   `hadamard_slices_not_twoSided`, `sh1_necessity`, `sh1_sufficiency`, `fibreGram_mul_weak_apply`**;
   **act 13's `WeakAnchorStabilizer`, `weak_anchor_coeff_norm_one`, `weak_preserves_admissible`**;
   **act 17's `GramTrajEquiv`** and its equivalence lemmas; **act 18's `ProperAt`,
   `PropagatesFrom`, `prod_mem_unitaryGroup`, `prod_admissible`**.

## The questions, FROZEN — four, kept apart

> **G1.** Does the prefix before `L1` — the standing `L-PROP` hypotheses and `L0` — imply `L1`, at
> act 21's frozen product configuration; or does an exhibited law satisfying that prefix fail `L1`?
>
> **G2.** Does the prefix before `L3i` — the standing hypotheses, `L0`, `L1`, `L2` — imply `L3i`; or
> does an exhibited law satisfying that prefix fail `L3i`?
>
> **G3.** Does the prefix before `L3s` — the standing hypotheses, `L0`, `L1`, `L2`, `L3i` — imply
> `L3s`; or does an exhibited law satisfying that prefix fail `L3s`?
>
> **G4.** Does the prefix through `L4d` together with `L5` imply `L4n` at act 20's certified
> strength; or does an exhibited law satisfying the prefix through `L4d` and `L5` fail `L4n`?

Each is a question about act 21's exact declarations at act 21's exact configuration. **The round
does NOT try to derive Schrödinger evolution**, does not characterize the surviving class, does not
ask whether any two rungs are independent, and does not ask what any rung means beyond the
declaration act 21 froze.

## The strength of the ask, FROZEN

**The ask is four rung-status verdicts, each earned by its own named witness or reported undecided,
over a closed list of four named laws, at one frozen configuration, in one fixed order.** It does
**not** undertake a census, a characterization, an independence claim, or the inference of one
rung's status from another's.

**What each witness would and would not separate, stated in advance.** A law failing `L1` off the
reached classes separates the demand that the transition preserve admissibility **on the whole
orbit space** from the demand that its solutions stay admissible; it says nothing about laws that
are time-homogeneous. A partial collapse separates injectivity from the standing hypotheses; a
shift that misses one class separates surjectivity from injectivity **on an infinite class space**,
which is the only place the two can come apart, and says nothing about finite configurations. A
class-conditional relabelling of one factor that factorizes separates the existence of a
twisted-natural lift from factorization; it says nothing about whether the two rungs are
independent, which four corners at one configuration do not establish and which no sentence of this
round asserts.

## The objects, FROZEN — act 21's, consumed

`V`, `A`, `a₀`, `Γ`, the transition family, the law it generates, the admissible orbit state space
`Ω(Γ, t)` and the frozen quotient list are act 21's, at its lines 642–733, consumed without
restatement. In particular:

- **A transition family** is `Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)`, written at
  representative level and required to descend; **the law it generates** is
  `∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`. A transition family is any such function; `L1` is
  exactly the condition that it keeps the admissible set, and a family that leaves it is a family
  that fails `L1`.
- **The frozen quotient list** is act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv` and act 21's
  `LawEquiv`, and **no other equivalence may be used in any verdict**. This round's verdicts are rung
  labels and one non-implication; none is taken modulo anything but `GramPhaseEquiv`.

### The frozen product configuration

Act 21's, at its lines 1263–1267: `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`,
`Γ ≡ 1/16` as the pointwise product `Γ₀ ⊗ Γ₀` of two copies of `Γ₀ ≡ ¼`, the decomposition
`e = Equiv.refl (Fin 4 × Fin 4)`, `Γ₁ = Γ₂ = Γ₀` at every `t` — exactly the parameters
`phiPP_ladder`, `phiCTRL_census` and act 22's `phiSwap_l5_restricts` are stated at. **Every target
of this round is at this configuration and at no other.** `Γ ≡ 1/16` is constant and therefore
invariant under every permutation of the product carrier.

**The one-`|A|`-value caveat, carried from acts 18, 21 and 22 and recorded again.** `|A₁| = |A₂| = 1`
is the strongest case for the per-slice statements and is not degenerate there; it is not
automatically the right case for a cross-time statement, and every verdict of this round is at that
cardinality and at no other.

## The ladder, CONSUMED and not restated, and the prefix of each target

The ladder is act 21's `L0`–`L5` in act 21's wording, at its lines 735–946, as the declarations of
`OrbitLawRigidityTwisted.lean` at blob `860daac4…`, conjoined as `LadderConds` in the order: the
two standing hypotheses `ProperAt` and `PropagatesFrom`, then `L0`, `L1`, `L2`, `L3` (`L3i` then
`L3s`), `L4d`, `L4n`, `L5`. **This round's module states no rung**: every conjunct it proves or
refutes is act 21's declaration applied to a named family.

**The prefix of a rung is fixed here, in `LadderConds` order, and is what "every earlier rung"
means in every label of this round.** The standing hypotheses are part of every prefix: a witness
that is not an `L-PROP` law is outside the class the shared theorem produces and earns no label,
which is exactly act 21's `DF1`.

| target | rung tested | its prefix, as conjuncts of `LadderConds` | what the target tests |
| --- | --- | --- | --- |
| `G1` | `L1` | `ProperAt`, `PropagatesFrom`, `EvolvesTotally` | prefix `→ PreservesAdmissible` |
| `G2` | `L3i` | the above, `PreservesAdmissible`, the inline `L2` | prefix `→` first conjunct of `Reversible` |
| `G3` | `L3s` | the above, the first conjunct of `Reversible` | prefix `→` second conjunct of `Reversible` |
| `G4` | the corner | the above, the second conjunct of `Reversible`, the descent conjunct `L4d`, **and `FactorizesOnProduct`** | prefix `∧ L5 →` the inline `L4n` |

### The implication matrix, FROZEN

| | assumed | tested | explicitly out of scope |
| --- | --- | --- | --- |
| `G1` | `L-PROP`, `L0` | `L1` | everything after `L1`; whether `L2` would restore the implication (that is `l1_free_on_shared_class`, merged and not re-asked) |
| `G2` | `L-PROP`, `L0`, `L1`, `L2` | `L3i` | `L3s`; nothing about `L3i` is inferred from `G3` |
| `G3` | `L-PROP`, `L0`, `L1`, `L2`, `L3i` | `L3s` | `L3i`; nothing about `L3s` is inferred from `G2`; finiteness of `Ω_t`, which is neither assumed nor claimed |
| `G4` | `L-PROP`, `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d`, `L5` | `L4n` | any independence of `L4n` and `L5`; any square of independences; act 22's non-implication in the other direction, consumed and not re-proved |

**Nothing in one row is inferred from another row.** A verdict on `G2` says nothing about `G3` and
conversely; a verdict on `G4` says nothing about `G1`–`G3`; and no combination of the four verdicts
is reported as more than the four verdicts.

### The rung labels, carried

Act 21's three labels and their earning conditions, at its lines 926–946, govern `L1`, `L3i` and
`L3s` here: `Li-RESTRICTS` is earned only by an **exhibited** law satisfying every rung of the
prefix fixed above and failing `Li`, with the failing conjunct and the separating class named;
`Li-FREE` only by a **universal** kernel proof of the implication from exactly that prefix;
`Li-UNDECIDED` by the recorded statement that neither was reached, with the obstruction named. **A
label is earned by the witness the authorization matrix names for that target and by nothing found
during execution.** The corner carries the three labels of its own status rule below, earned the
same three ways.

**The three-way discipline, and the order of the routes.** For each of `G1`–`G4` the frozen route
is the named witness. **`FREE` (and, for `G4`, `L5-IMPLIES-L4n`) is earned only by a universal
proof, which the execution attempts only if the named witness fails to close at a named step** —
and then only for the implication from exactly the frozen prefix, at exactly the frozen
configuration. A universal proof is a finding about the condition; it is never inferred from the
failure of a witness, never from the absence of one, and never from census silence. **Failure to
obtain a universal theorem is `UNDECIDED`, never `FREE` and never `RESTRICTS`.**

## The bundling discipline, FROZEN — the three safeguards and the two failure rules

**This is the first bundled round, and the rules that keep its four verdicts separate are frozen
here as this round's rules.** They are not `AGENTS.md` rules; whether they become one is decided
after this round has run under them.

### Safeguard 1 — a fixed execution order, one verdict commit per target, and the attestation set at every boundary

The targets are executed in the order **`G1` → `G2` → `G3` → `G4`**, and in no other. The order
puts the two broad questions about the standing hypotheses and the ladder's first rungs before the
two constructions that act on the ladder's upper rungs, so that whatever is learned settling `L1`
and `L3` is on the record before the more constructive `L4n`/`L5` work begins.

The execution's commits on the first-parent chain from `B` are, in order: **the stage-A commit**
(the two declarations set to `B`, in the guard file only); **the module commit** (the module with
its shared lemmas and **no verdict of any target** — no conjunct of any rung discharged or refuted
for any of the four witnesses); then **exactly one verdict commit per target**, `G1`'s, `G2`'s,
`G3`'s, `G4`'s, each carrying that target's named results and nothing of a later target's; then the
packaging commit. A verdict commit that carries a later target's result, or a target executed out
of order, is recorded as a discrepancy and the round's ordering obligation is reported as
undischarged for that target.

**The attestation set is answered at every boundary.** Act 20's three questions, in act 21's
wording at its lines 1033–1043 — **Q1 INTENTIONAL**, **Q2 INCIDENTAL**, **Q3 UNAIDED REASONING** —
are answered by the result note **five times**, for the spans `B` → module commit, module commit →
`G1`'s verdict commit, `G1` → `G2`, `G2` → `G3`, `G3` → `G4`, each answer a measurement about what
the execution acquired **in that span** bearing on any target **not yet closed at the span's end**.
The partial-fact rule applies at every boundary: learning one conjunct of one later target's witness
is a YES. A YES is disclosed with what was learned, when, and whether any later target's route
changed afterwards; it is not concealed and not argued away, and a disclosure does not cure it.
**What the freeze itself places in front of the execution is not a YES and is listed rather than
left implicit**: this file carries the proof route for every target and act 21's and act 22's
result notes carry every consumed fact; the questions are about what was acquired beyond the freeze
and the pinned blobs.

### Safeguard 2 — the witness-authorization matrix

**Each construction may answer exactly the targets this matrix authorizes, and no other.** A
witness is tested for its own target's prefix and its own target's rung; its status on any later
rung is not a verdict of this round. A witness found or learned during a later target's work may
not be retroactively assigned to an earlier target; an alternative witness for any target found
during execution is an observation and never substituted.

| construction | `G1` (`L1`) | `G2` (`L3i`) | `G3` (`L3s`) | `G4` (the corner) |
| --- | --- | --- | --- | --- |
| `Φ_MD`, the merge-then-drop transition | **authorized** | — | — | — |
| `Φ_PC`, the partial collapse | — | **authorized** | — | — |
| `Φ_HS`, the Hilbert shift | — | — | **authorized** | — |
| `Φ_SC`, the self-controlled relabelling | — | — | — | **authorized** |
| `ΦCTRL`, `Φ_swap`, `ΦPP`, consumed from acts 21 and 22 | — | — | — | context only: the other three corners, not re-proved, not tested, not witnesses of anything here |

**Shared lemmas are not witnesses.** The module commit's lemmas — the product-marginal lemma, the
Fourier-family admissibility lemma, the separation computations and the non-realizability of the
zero tuple — are consumed by whichever verdict needs them and answer no target by themselves.

### Safeguard 3 — the outcome-vector table

The round's headline is a **vector of four labels**, one per target, each drawn from its target's
frozen label set, and **the headline is selected verbatim from the outcome-vector table in the
status rule below**, which lists every admissible vector. No single-label headline, no summary
label and no combination label exists for this round.

### Failure rule 1 — a universal theorem not obtained is `UNDECIDED`

For every target, failure to obtain a universal implication theorem — whether or not one was
attempted — is reported as the target's `UNDECIDED` label with the obstruction named, never as
`FREE`, never as `RESTRICTS`, never as `L5-IMPLIES-L4n`. Census silence is not a finding about any
rung.

### Failure rule 2 — an authorized witness that fails an earlier rung is recorded, not repaired

If an authorized witness unexpectedly fails any rung of its target's prefix, or fails the standing
hypotheses, the execution **records that fact**, with the failing conjunct, and the target takes its
**preregistered fallback outcome — its `UNDECIDED` label with that obstruction named**. The witness
set is not repaired, the witness is not slid to another target, no other construction is
substituted, and no earlier-rung failure of one witness is read as a verdict on that earlier rung:
the earlier rung's status is the status its own target reached, or act 21's, and nothing else.

## The frozen candidate law list — four named transition families, one per target

**Four named transition families, at the frozen product configuration. The list is closed at this
freeze.** A candidate discovered during execution is recorded as an observation and not executed.
Throughout, `G₁ := FibreGram 0 H₁` and `Gᵢ := FibreGram 0 Hᵢ` are the fibre-Gram tuples of act
12's `H(1)` and `H(i)` at `Γ₀ ≡ ¼`; `σ := Equiv.swap (2 : Fin 4) 3`; `X ⊠ Y` is the product
embedding `(X ⊠ Y) i j k = X i.1 j.1 k.1 · Y i.2 j.2 k.2`; `∼` is act 12's `GramPhaseEquiv`; and
"realizable" means `RealizableGram (Fin 1) Γ₀` on a factor and `RealizableGram (Fin 1 × Fin 1) (Γ t)`
on the product carrier.

### `Φ_MD` — the merge-then-drop transition, NEW to the record; the `G1` witness

> **Statement.** At `t = 0`: `Φ_MD 0 G = G₁ ⊠ G₁` if `G ∼ Gᵢ ⊠ G₁`, and `G` otherwise. At every
> `t ≥ 1`: `Φ_MD t G = 0`, the zero tuple, if `G ∼ Gᵢ ⊠ G₁`, and `G` otherwise.

**Where it comes from.** It is the construction act 21's note names as what would settle `L1`, made
concrete: at time `0` one named class is sent onto another, so that from time `1` on it is reached
by no solution; at later times the then-unreached class is sent to a non-realizable tuple. It is
**time-inhomogeneous by construction**, which is permitted because `L2` is after `L1`, and its
role is **the `L1` countercontrol**.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **Descent.** Both conditions are invariant under `∼`, an equivalence relation by act 17's three
  lemmas, and both images depend only on the branch, so `G ∼ G' → Φ_MD t G ∼ Φ_MD t G'` at every
  `t` (the fired branch gives equal tuples; the other gives the hypothesis).
- **`L0`.** For `G₀ ∼ Gᵢ ⊠ G₁` the solution is `𝔾 0 = G₀`, `𝔾 t = G₁ ⊠ G₁` for `t ≥ 1`; since
  `[G₁ ⊠ G₁] ≠ [Gᵢ ⊠ G₁]` — the product cross-invariant at the fibre pair `((0,0),(1,0))`,
  `product_cross` with act 12's values `1/16` and `i/16` from `hadamard_entries`, giving `1/256`
  against `i/256` — every later `Φ_MD t` fixes it. For any other realizable `G₀` the constant
  trajectory is a solution. Every slice is realizable, `G₁ ⊠ G₁` by `product_realizable`.
- **`L-PROP`.** `ProperAt`: the constant solutions at `G₁ ⊠ G₁` and at `G₁ ⊠ Gᵢ`, neither in the
  fired class — `[G₁ ⊠ Gᵢ] ≠ [Gᵢ ⊠ G₁]` is act 22's separation at the same fibre pair — and
  `∼`-inequivalent; the non-solution is the constant trajectory at `Gᵢ ⊠ G₁`, whose image at time
  `0` is `G₁ ⊠ G₁`, inequivalent to it. `PropagatesFrom` clause (i) is uniqueness of continuation
  from descent, as `ol1a_descent` gives it; clause (ii) is the two constant solutions at `t = 1`.
- **`L1` fails**, at `t = 1`, on the realizable tuple `Gᵢ ⊠ G₁` — realizable by `product_realizable`
  from `sh1_necessity` on `Hᵢ` and `H₁` — whose image is the zero tuple, which is not realizable
  because its fibres sum to `0` and not to `1` on the non-trivial index type `Fin 4 × Fin 4`. **The
  failing conjunct is `∑ i, G i = 1` of `RealizableGram` at `t + 1 = 1`; the separating class is
  `[Gᵢ ⊠ G₁]`.**

### `Φ_PC` — the partial collapse, NEW to the record; the `G2` witness

> **Statement.** At every `t`: `Φ_PC t G = G₁ ⊠ G₁` if `G ∼ Gᵢ ⊠ G₁`, and `G` otherwise.

**Where it comes from.** It is act 21's `ΦC` with the collapse restricted to one class: act 21's
note names "a partial collapse rather than a total one" as what would settle `L3i`. It is
time-homogeneous. Its role is **the `L3i` countercontrol**.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **Descent, `L0`, `L1`, `L-PROP`** as for `Φ_MD`'s time-`0` map, at every `t`: the image of a
  realizable tuple is `G₁ ⊠ G₁` or the tuple itself, both realizable, so `L1` holds; `L0`'s solutions
  are constant from time `1`, and every realizable class other than the fired one has a constant
  solution; `ProperAt` and both propagation clauses exactly as above, the two inequivalent constant
  solutions at `G₁ ⊠ G₁` and `G₁ ⊠ Gᵢ` sitting outside the fired class. **`L2` holds** with
  `Φ₀ = Φ_PC 0`.
- **`L3i` fails** at every `t`: `Gᵢ ⊠ G₁` and `G₁ ⊠ G₁` are realizable, their images are the same
  tuple `G₁ ⊠ G₁`, and they are `∼`-inequivalent. **The failing conjunct is injectivity on classes;
  the separating classes are `[Gᵢ ⊠ G₁]` and `[G₁ ⊠ G₁]`, separated by the product cross-invariant
  at `((0,0),(1,0))`, values `i/256` and `1/256`.**

### `Φ_HS` — the Hilbert shift, NEW to the record; the `G3` witness

> **Statement.** Let `H(z) = ½ · [[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]` for `z ∈ ℂ`, act
> 12's frozen family read at an arbitrary parameter, and for `n ≥ 1` let
> `z_n = ((n² − 1) + 2n·i) / (n² + 1)`, so that `|z_n| = 1`, `z_1 = i`, and
> `F_n := FibreGram 0 (H(z_n)) ⊠ G₁`. At every `t`: `Φ_HS t G = F_{n+1}` if `G ∼ F_n` for some
> `n ≥ 1`, and `G` otherwise.

**Where it comes from.** On a finite class space injectivity and surjectivity coincide, and act 21's
freeze stated the two conjuncts apart because `Ω_t` is not known to be finite. At `Γ₀ ≡ ¼` the class
space is infinite — `H(z)` is a unitary with every modulus `½` for **every** unit `z`, and distinct
unit `z` give `∼`-inequivalent classes through act 12's cross-invariant, whose value on `H(z)` is
`z/16` — so an injective self-map that misses one class exists, and the shift along a countable
sub-family with rational coordinates is the simplest one whose distinctness needs no transcendence.
Its role is **the `L3s` countercontrol**, and it is the only witness of this round that uses a
family act 12 did not freeze; the family is frozen here, in the witness supply, before any kernel
work.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **The family is admissible and its classes are distinct.** `H(z)` for unit `z`: the rows are
  pairwise orthogonal, each computation using `z · conj z = 1` once, so `H(z)` is unitary with every
  entry of modulus `½` and `AdmissibleDilationAt Γ₀ 0 (H(z))` holds; `FibreGram 0 (H(z))` is
  realizable by `sh1_necessity`, and `F_n` by `product_realizable`. The cross-invariant of
  `FibreGram 0 (H(z))` at the fibre pair `(1,0)` is `z/16` and of `F_n` at the product fibre pair
  `((1,0),(0,0))` is `z_n/256` by `product_cross`; the real parts `(n² − 1)/(n² + 1)` are strictly
  increasing in `n`, so `n ↦ z_n` is injective, `z_n ≠ 1` for every `n ≥ 1`, and **the classes
  `[F_n]` are pairwise distinct and distinct from `[G₁ ⊠ G₁]` and `[G₁ ⊠ Gᵢ]`**, whose invariant at
  that pair is `1/256`.
- **The branch index is unique.** If `G ∼ F_n` and `G ∼ F_m` then `n = m`, so the statement's
  `if ∃ n, G ∼ F_n then F_{(that n) + 1} else G`, written with a classical choice or `Nat.find` in
  the theorem's own equation, depends only on the class of `G`; descent follows.
- **`L0`, `L1`, `L2`, `L-PROP`.** Every image is realizable; from `F_n` the solution is
  `𝔾 t = F_{n+t}`; from any other realizable class the constant trajectory; `L2` by construction;
  `ProperAt` from the constant solutions at `G₁ ⊠ G₁` and `G₁ ⊠ Gᵢ`, both fixed and inequivalent,
  with the non-solution the constant trajectory at `F_1`, whose image `F_2` is inequivalent to it;
  the propagation clauses as for `Φ_MD`.
- **`L3i` holds.** If `Φ_HS t G ∼ Φ_HS t G'` for realizable `G`, `G'`: if both are in the family,
  `F_{n+1} ∼ F_{m+1}` forces `n = m` and so `G ∼ F_n ∼ G'`; if exactly one is in the family, say
  `G ∼ F_n`, then `G' ∼ F_{n+1}` puts `G'` in the family, a contradiction; if neither, the images
  are `G` and `G'`.
- **`L3s` fails** at every `t`: `F_1 = Gᵢ ⊠ G₁` is realizable, and no realizable `G` has
  `Φ_HS t G ∼ F_1` — an image in the family is some `F_{n+1}` with `n + 1 ≥ 2`, distinct from
  `F_1`; an image outside the family is `G` itself, outside the family. **The failing conjunct is
  surjectivity onto classes; the separating class is `[F_1] = [Gᵢ ⊠ G₁]`, the one the shift never
  reaches.**

### `Φ_SC` — the self-controlled relabelling, NEW to the record; the `G4` witness

> **Statement.** At every `t`: `Φ_SC t G = RelabelTransition (Equiv.prodCongr σ 1) G` if there is
> a realizable `G₂` with `G ∼ Gᵢ ⊠ G₂` or with `G ∼ (RelabelTransition σ Gᵢ) ⊠ G₂`, and `G`
> otherwise.

**Where it comes from.** It is act 22's description of the corner made concrete — "a
class-conditional relabelling on one factor tensored with the identity" — with one refinement forced
by the ladder: the control class and the relabelled factor are the **same** factor, so that the
factor map is class-conditional on its own input, and the controlled set is closed under the
relabelling so that the map is an involution on classes and both conjuncts of `Reversible` hold.
Compare act 21's `ΦCTRL`, which conditions on the first factor and relabels the second: that is
what breaks factorization there, and it is exactly what `Φ_SC` does not do. Its role is **the
witness of the corner**, and it is tested for nothing else.

**Its analysis, recorded here as the freeze's reading and not as a finding.**

- **The product-marginal lemma, proved once in the module commit.** For realizable `G₁`, `G₁'`,
  `G₂`, `G₂'`: `G₁ ⊠ G₂ ∼ G₁' ⊠ G₂'` implies `G₁ ∼ G₁'`. From the phases `c` on `V₁ × V₂` fix any
  `m` and put `c₁ j₁ := c (j₁, m)`; reading the equivalence at the matrix indices `(j₁, m)`, `(k₁, m)`
  gives `G₁' i₁ j₁ k₁ · G₂' i₂ m m = star (c₁ j₁) · G₁ i₁ j₁ k₁ · c₁ k₁ · G₂ i₂ m m`, and the two
  diagonal entries of the second factors are both `Γ₀ i₂ m = ¼` by `RealizableGram`'s fourth
  conjunct, so they cancel. Conversely `G₁ ∼ G₁'` gives `G₁ ⊠ G₂ ∼ G₁' ⊠ G₂` with
  `c (j₁, j₂) := c₁ j₁`. So for realizable `G₁`, `G₂`, **the branch of `Φ_SC` on `G₁ ⊠ G₂` fires
  exactly when `G₁ ∼ Gᵢ` or `G₁ ∼ RelabelTransition σ Gᵢ`**.
- **`L5` holds**, with the factor maps `Φ₁ G₁ := RelabelTransition σ G₁` on that same condition
  and `G₁` otherwise, and `Φ₂ := id`: on the fired branch `Φ_SC t (G₁ ⊠ G₂) = RelabelTransition
  (Equiv.prodCongr σ 1) (G₁ ⊠ G₂) = (RelabelTransition σ G₁) ⊠ G₂` **exactly**, by
  `relabel_product`, which is stated for product permutations and covers this one; on the other
  branch both sides are `G₁ ⊠ G₂`. The displayed equivalence is `gramPhaseEquiv_refl`. **The factor
  maps are fixed before the inputs**, as the declaration's quantifier order requires.
- **Descent, `L0`, `L1`, `L2`, `L4d`.** The condition is `∼`-invariant; images are relabellings or
  the identity, so realizability is preserved by `realizable_relabel` (`Γ` constant) and descent by
  `relabel_gramPhaseEquiv`; `L0`'s solutions are the iterates, realizable at every `t`; `L2` by
  construction; `L4d` is descent.
- **`L3i` and `L3s` hold**, because `Φ_SC t ∘ Φ_SC t = id` **exactly**: `σ` is an involution, so
  `RelabelTransition (Equiv.prodCongr σ 1)` is one by `relabel_relabel_symm`, and the condition is
  preserved by the relabelling — `RelabelTransition (Equiv.prodCongr σ 1) G ∼ Gᵢ ⊠ G₂'` iff
  `G ∼ (RelabelTransition σ Gᵢ) ⊠ G₂'`, by `relabel_product` and `gramPhaseEquiv_of_relabel` — so
  the fired set is closed; injectivity and surjectivity follow exactly as `phiCTRL_census` proves
  `Reversible` for `ΦCTRL`.
- **`L-PROP`.** `ProperAt`: the constant solutions at `G₁ ⊠ G₁` and at `G₁ ⊠ Gᵢ`, neither fired —
  `[G₁] ≠ [Gᵢ]` is act 12's `hadamard_slices_not_twoSided`, and `[G₁] ≠ [RelabelTransition σ Gᵢ]`
  is the cross-invariant at the fibre pair `(0,2)`, values `1/16` and `−1/16` — and inequivalent;
  the non-solution is the constant trajectory at `Gᵢ ⊠ G₁`, fired to
  `(RelabelTransition σ Gᵢ) ⊠ G₁`, inequivalent to it through the same pair. Propagation clause (i)
  by descent, clause (ii) at `t = 1`.
- **`L4n` fails**, by `phiCTRL_census`'s refutation with the roles of the factors exchanged. Take
  the weak anchored gauge `K = diagonal c` with `c (3,0) = −1` and `c j = 1` otherwise, so that
  `Equiv.prodCongr σ 1` carries the index `(2,0)` to `(3,0)`. Any twisted-natural lift `Ψ` with
  induced right map `αR` has `αR K` a weak anchored stabilizer with phases `c'` by the second
  closure conjunct. Read the lifting equation at `U K` and at `U` for a dilation `U` of
  `Gᵢ ⊠ G₁` (fired) and for a dilation of `G₁ ⊠ G₁` (not fired), at the entry
  `((0,0), (0,0), (2,0))`: on the fired branch `Φ_SC` relabels the gauged input, so the left side
  carries `c (3,0) = −1` against the tuple's entry at `((0,0),(0,0),(3,0))`, whose value
  `Gᵢ 0 0 3 · G₁ 0 0 0 = −i/16` is nonzero, while the right side carries
  `star (c' (0,0)) · c' (2,0)` against the same entry; on the identity branch the left side carries
  `c (2,0) = 1` against `G₁ 0 0 2 · G₁ 0 0 0 = 1/16`, nonzero, and the right side the same
  `star (c' (0,0)) · c' (2,0)`. Cancelling the nonzero entries gives `−1 = 1`. **The failing
  conjunct is the right closure and right intertwining conjuncts of `TwistedNatural`, read together
  with the lifting obligation; the separating classes are `[Gᵢ ⊠ G₁]` and `[G₁ ⊠ G₁]`.**

### `ΦCTRL`, `Φ_swap` and `ΦPP` — the other three corners, CONSUMED as context and tested for nothing

Their verdicts are acts 21's and 22's, exactly as landed: `ΦCTRL` fails `L4n` and `L5`, `Φ_swap`
satisfies the prefix through `L4n` and fails `L5`, `ΦPP` satisfies `LadderConds` in full. They are
named here so that the corner is placed, **and for no other purpose**: none is a witness of any
target, none is re-proved, and the four corners together are reported as four separate facts about
four named laws and **never as an independence of `L4n` and `L5`**. That inference, if anyone makes
it, is made in a later synthesis with its own freeze, not here.

## The witness supply, FROZEN

Act 21's supply at its lines 1389–1409, unchanged, **extended by act 21's and act 22's merged
product-embedding lemmas** named in the inheritance list, and **extended by one new family, frozen
now**:

7. **The Fourier family at an arbitrary unit parameter, and its Pythagorean sequence.** `H(z)` as
   act 12 wrote it, read at any `z ∈ ℂ` with `z · conj z = 1`; and the sequence
   `z_n = ((n² − 1) + 2n·i)/(n² + 1)`, `n ≥ 1`, of unit complex numbers with rational coordinates,
   `z_1 = i`. The execution proves, in the module commit and before any verdict, that `H(z)` is an
   admissible dilation of `Γ₀ ≡ ¼` at the anchor `0` for every unit `z`, and that the cross-invariant
   of its fibre-Gram tuple at the fibre pair `(1,0)` is `z/16`. **This item is used by `Φ_HS` and by
   nothing else**, and it enlarges no merged statement: act 12's three values are its instances
   `z ∈ {1, i, −1}`.

**Nothing outside this supply may be introduced, at any point, for any reason.** The generic witness
rule governs every countercontrol: what a target's authorized witness is is what is tested, and an
alternative witness found during execution is recorded as an observation and never substituted.

## The countercontrols, one per target

| target | the countercontrol this freeze names | configuration |
| --- | --- | --- |
| `G1`, `L1` | `Φ_MD`: the prefix `ProperAt`, `PropagatesFrom`, `EvolvesTotally` holds, and `¬ PreservesAdmissible` at `t = 1` on `Gᵢ ⊠ G₁`, the image the zero tuple, failing `∑ i, G i = 1`; separating class `[Gᵢ ⊠ G₁]` | the product configuration |
| `G2`, `L3i` | `Φ_PC`: the prefix through `L2` holds, and injectivity on classes fails at `Gᵢ ⊠ G₁` against `G₁ ⊠ G₁`, equal images, separated at `((0,0),(1,0))`, values `i/256` and `1/256` | the product configuration |
| `G3`, `L3s` | `Φ_HS`: the prefix through `L3i` holds, and surjectivity fails at the class `[F_1] = [Gᵢ ⊠ G₁]`, outside the image, the family's classes separated at `((1,0),(0,0))`, values `z_n/256` | the product configuration |
| `G4`, the corner | `Φ_SC`: the prefix through `L4d` and `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl _) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ_SC` hold, with `Φ₁` the conditional single-carrier relabelling and `Φ₂ = id`, and `∀ t, ¬ (L4n)` by the exchanged-roles refutation; separating classes `[Gᵢ ⊠ G₁]` and `[G₁ ⊠ G₁]` | the product configuration |

**Evidence that earns any countercontrol**: a Lean theorem at evidence level 2 whose statement pins
the objects by equations, discharges admissibility from merged results or from the module commit's
family lemma, and certifies the separating quantity at a named index through a named invariant.
**Searching and not finding earns nothing.**

## What was and was not run before this freeze

**No drafting-time check of any target's outcome was run.** By the owner's direction this control
plane was drafted from the sealed record alone: no kernel proof, no exact-arithmetic computation of
any invariant, no search for any witness's rung status, and no test of any construction above was
performed. **Every value and every step in the four analyses is the freeze's reading**, derived by
hand from the merged declarations, and the execution is what establishes or refutes each. A value
stated above that the kernel computes differently is a discrepancy of the freeze's reading, recorded
in the result note and not repaired; it changes no label by itself, the label being earned by what
the kernel proves.

**One simulation was run, and it concerns chronology only.** A throwaway worktree at `D` with the
two declarations set to `D` under a placeholder stem of the same shape — no Lean file, no guard
clause, no record — was run against the guard at `D`: every one of the eighty-six `R7-*` tags
passed, `R7-OLT` and `R7-OLN` both classified `ARCHIVED`, reading their own records and nothing of
the placeholder's declaration. **No contract of any closed round needs superseding for this round to
execute**, and the supersession table below is therefore empty. The simulation's commits exist on
no branch of the repository.

## The ordering obligation, as it binds a bundled round whose ladder is consumed

> **The ordering obligation, act 23.** The rungs are act 21's declarations at blob `860daac4…` and
> nothing else. The execution's module **states no rung, no equivalence and no top-level definition
> of any kind**; every rung it discharges or refutes is act 21's declaration applied to a family
> pinned by equation. From the first commit that adds the module to the certified head `E`, **no
> commit of the branch adds a definition, restates a rung, or uses an equivalence outside the
> frozen quotient list**; the module commit carries no verdict of any target; the four verdict
> commits follow it in the order `G1`, `G2`, `G3`, `G4`; and each witness is pinned, in every theorem
> that names it, to the equation this freeze gives it and to nothing else — `Φ_MD` to its two-time
> statement, `Φ_PC` to the collapse onto `G₁ ⊠ G₁`, `Φ_HS` to the shift along `F_n`, `Φ_SC` to
> `RelabelTransition (Equiv.prodCongr σ 1)` on the self-controlled set.

### What the execution must record

1. **The declaration table.** For each of `L1`, `L3i`, `L3s`, `L4n` and `L5`, the act 21
   declaration consumed, its line range at blob `860daac4…`, and the statement that this round's
   module carries no declaration of its own — checked mechanically by `R7-OLG`, which requires the
   module to contain no `def`, `abbrev`, `structure`, `class`, `instance`, `axiom` or `opaque`, and
   to import `OIBridge.OrbitLawRigidityTwisted` and `OIBridge.OrbitLawNaturalityFactorization`.
2. **The stage-A commit.** The SHA of the commit that sets the two declarations to `B`, and nothing
   else.
3. **The module commit.** The SHA of the first commit at which the module is present, with the
   named results it carries, each of which is a shared lemma and none a verdict.
4. **The four verdict commits**, in order, each with its SHA and its named results.
5. **The immutability span.** The statement, with the command that checks it, that between the
   module commit and `E` no diff introduces a definition:
   `git diff <module commit> <E> -- verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`
   contains no added line beginning with `def `, `abbrev `, `structure `, `class `, `instance `,
   `axiom ` or `opaque `.
6. **The quotient record.** The only equivalence used in any verdict is act 12's `GramPhaseEquiv`,
   with the lemma that uses it, and **no equivalence was introduced or widened**.
7. **The five attestation answers**, one per span, as safeguard 1 fixes them.

### The anti-expansion rule, FROZEN

**If execution discovers a fifth candidate law, a further equivalence, a further rung, a further
configuration, a universal implication for a target whose witness has closed, or a strengthening of
a merged theorem, it is recorded as an observation for a later round with its own freeze and is not
executed here.** The candidate list is closed at four, the quotient list at three, the ladder at act
21's `L0`–`L5`, the rungs tested at `L1`, `L3i`, `L3s` and, for the corner, `L4n` against the
prefix with `L5`, and the configuration at the frozen product configuration.

## The targets, FROZEN

Five targets, `G0` through `G4`; `G0` is type P and is the record check every round of this
programme has carried, and `G1`–`G4` are the bundle. Each names what settles it and what evidence
counts.

### `G0` — does the merged record already decide any of the four questions?

**The question.** At `B`, does the merged record contain a statement deciding `L1`'s, `L3i`'s or
`L3s`'s rung status under act 21's labels at the product configuration, or deciding whether the
prefix through `L4d` with `L5` implies `L4n` there?

**What settles it.** Locating and quoting, under act 21's evidence rule at its lines 1456–1467,
over a bounded file set: act 21's `preregistration.md`, `amendments/amendment-1.md` and
`result.md`, act 22's `preregistration.md` and `result.md`, act 21's and act 22's modules, act 20's
`result.md` and module, and `verification/ROADMAP.md`, with the terms `L1`, `L3i`, `L3s`, `L4n`,
`L5`, `PreservesAdmissible`, `Reversible`, `injectiv`, `surjectiv`, `RESTRICTS`, `FREE`,
`UNDECIDED`, `corner`, `implies`, `implication`.

**This is a type-P target.** No Lean is written for it, no outcome of it is a theorem, and this
round's own theorems are not retro-evidence about it. **Reconstructive inference is forbidden as a
finding; where the record is silent, the finding is that it is silent.** This round's own control
plane is inside the set by construction and its hits are recorded as not relevant to the question.

### `G1` — the `L1` rung status, via `Φ_MD`

**The statement.** `Φ_MD`, pinned by equation, satisfies `ProperAt`, `PropagatesFrom` and
`EvolvesTotally` at the product configuration, and `¬ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ_MD`.

**What settles it.** One Lean theorem at evidence level 2, `phiMD_l1_restricts`, whose statement
pins `Γ₀`, `H₁`, `Hᵢ`, `Γ` and `Φ_MD` by equations, as `phiCTRL_census` does, and carries the
prefix conjuncts and the failure as conjuncts, with the failing conjunct and the separating class as
the countercontrol table names them. **`L1-RESTRICTS` is earned only by the prefix conjuncts and
the failure together.**

### `G2` — the `L3i` rung status, via `Φ_PC`

**The statement.** `Φ_PC` satisfies `ProperAt`, `PropagatesFrom`, `EvolvesTotally`,
`PreservesAdmissible` and the inline `L2` at the product configuration, and fails the first
conjunct of `Reversible`.

**What settles it.** One Lean theorem at evidence level 2, `phiPC_l3i_restricts`, of the same shape.
**`L3i-RESTRICTS` is earned only by the prefix conjuncts and the failure together.**

### `G3` — the `L3s` rung status, via `Φ_HS`

**The statement.** `Φ_HS` satisfies `ProperAt`, `PropagatesFrom`, `EvolvesTotally`,
`PreservesAdmissible`, the inline `L2` and the first conjunct of `Reversible` at the product
configuration, and fails the second conjunct of `Reversible`.

**What settles it.** One Lean theorem at evidence level 2, `phiHS_l3s_restricts`, of the same
shape, its statement pinning the family `H(·)`, the sequence `z_·` and `Φ_HS` by equations.
**`L3s-RESTRICTS` is earned only by the prefix conjuncts, `L3i` included, and the failure
together**; a shift that is not injective on classes earns nothing for `L3s`.

### `G4` — the corner, via `Φ_SC`

**The statement.** `Φ_SC` satisfies the first seven conjuncts of `LadderConds` — the two standing
hypotheses, `L0`, `L1`, `L2`, `Reversible`, `L4d` — and the ninth,
`FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀)
(fun _ => Γ₀) Γ Φ_SC`, at the product configuration, and fails the eighth: at every `t`, no
`Ψ αL αR` satisfies the lifting obligation, the admissibility obligation and `TwistedNatural`.

**What settles it.** One Lean theorem at evidence level 2, `phiSC_corner`, of the same shape, and
one corollary, `l5_not_implies_l4n`, refuting
`∀ Φ, (prefix through L4d) Φ → FactorizesOnProduct … Φ → (L4n) Φ` by instantiation at `Φ_SC`,
the quantifier ranging over every transition family on `Fin 4 × Fin 4`. **The corner label is
earned only by the prefix conjuncts, `L5` and the `L4n` failure together**; a `Φ_SC` failing any
conjunct of the prefix, or failing `L5`, earns nothing and takes the fallback of failure rule 2.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `G0` | **negative** — the record decides none of the four | **high** | Act 21 reports the three rungs `UNDECIDED` and names what would settle each; act 22 names the corner and forbids itself to execute it. The finding is whatever the bounded search records. |
| `G1` | **`L1-RESTRICTS`**, via `Φ_MD` | **high** | The construction is the one act 21's note names; every conjunct is a case split on one class with merged separations, and the failure is the zero tuple's fibre sum. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `G2` | **`L3i-RESTRICTS`**, via `Φ_PC` | **high** | The construction is act 21's `ΦC` restricted to one class, with the two propagation clauses that `ΦC` lacked supplied by the two untouched classes. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `G3` | **`L3s-RESTRICTS`**, via `Φ_HS` | **medium** | The injectivity case analysis is elementary once the family's classes are shown distinct, but the family is infinite, its admissibility is proved at a symbolic parameter, and the shift's statement carries a classical choice; each is new kernel work. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `G4` | **`L5-NOT-IMPLIES-L4n`**, via `Φ_SC` | **medium–high** | The `L4n` refutation is `phiCTRL_census`'s argument with the factors' roles exchanged; the factorization rests on the product-marginal lemma, which is a one-index cancellation on realizable second factors; reversibility is the involution argument `phiCTRL_census` already carries. **UNDECIDED with the obstruction named is an allowed outcome.** |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.
**No `FREE` label and no `L5-IMPLIES-L4n` is predicted**: each would need a universal implication
proof, which the execution attempts only under the route order fixed above.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
**UNDECIDED is a live preregistered outcome for every target and is not a failure.**

### The outcomes of `G0`

- **Outcome `G0`-silent:**
  > On the search this freeze bounds — act 21's control plane, amendment and result note, act 22's
  > control plane and result note, act 21's and act 22's modules, act 20's result note and module,
  > and `verification/ROADMAP.md`, against the frozen term list — the merged record decides neither
  > the rung status of `L1`, of `L3i` nor of `L3s` under act 21's labels at the product
  > configuration, and does not decide whether the prefix through `L4d` with `L5` implies `L4n`
  > there. **The finding is that the record is silent on the point.** It is not a finding that any
  > such statement is false, not a finding that one is unprovable, and not a bound on what a later
  > round could prove.
- **Outcome `G0`-found:**
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which
  > objects. No merged artifact is edited, and no earlier round's recording is enlarged or corrected.

### The outcomes of `G1`, `G2` and `G3` — act 21's sentences, carried verbatim

- **Outcome `Li-RESTRICTS`**, for a named rung `Li`:
  > An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
  > `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
  > a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
  > statement about the exact condition frozen under the label `Li`, at the configuration named, and
  > it does **not** endorse the condition, does **not** say the programme requires it, and does
  > **not** say it is the right condition to impose.
- **Outcome `Li-FREE`**, for a named rung `Li`:
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
- **Outcome `Φ`-SURVIVES-PREFIX**, for a named transition family `Φ` and its target's rung `Li`:
  > The transition family named `Φ` in this round's frozen list satisfies every conjunct of the
  > prefix before `Li` of the ladder act 21 fixes, at the configuration this freeze names for it,
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

### The outcomes of `G4` — the corner, each sentence frozen in full

- **Outcome `L5-NOT-IMPLIES-L4n`:**
  > At the frozen product configuration, the conjunction of the standing `L-PROP` hypotheses with
  > `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d` and with `L5` as act 21 froze it does not imply `L4n` at
  > act 20's certified strength: an exhibited transition family satisfies every conjunct of that
  > prefix, factorizes into fixed local maps for the ordered decomposition named, and admits no
  > twisted-natural lift, at evidence level 2. **This is a statement about the exact declarations at
  > the exact configuration**: it does not say that `L4n` and `L5` are independent, does not report a
  > square of independences, does not say that any law interacts or fails to compose in any sense,
  > and does not say that either condition is or is not the right condition to impose.
- **Outcome `L5-IMPLIES-L4n`:**
  > Every transition family satisfying the standing `L-PROP` hypotheses, `L0`, `L1`, `L2`, `L3i`,
  > `L3s`, `L4d` and `L5` as act 21 froze it satisfies `L4n` at act 20's certified strength, proved
  > universally at evidence level 2 at the frozen product configuration. **This is a statement about
  > the exact declarations at the exact configuration**, and it does not say that `L4n` is the right
  > condition to impose, does not say that `L5` is, and changes no verdict of act 21 or act 22.
- **Outcome `CORNER-UNDECIDED`:**
  > Whether the prefix through `L4d` with `L5` implies `L4n` at the frozen product configuration is
  > undecided in this round, with the obstruction named specifically — which conjunct of the named
  > witness did not close and at which step, or which step of a universal proof did not close.
  > Neither label is claimed; the absence of an exhibited counterexample is not a proof of the
  > implication, and the absence of a proof is not a counterexample.

### The outcome-vector table — every admissible headline

The headline is one row of this table, verbatim, in this rendering: **Outcome vector:** followed by
the four labels in target order, separated by ` · `. Each row is admissible; the execution selects
the row its four verdicts compose and reports no other wording. **There are eighty-one rows and no
others.**

| # | vector |
| --- | --- |
| 1 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 2 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 3 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 4 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 5 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 6 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 7 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 8 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 9 | **Outcome vector:** `L1-RESTRICTS` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 10 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 11 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 12 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 13 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 14 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 15 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 16 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 17 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 18 | **Outcome vector:** `L1-RESTRICTS` · `L3i-FREE` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 19 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 20 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 21 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 22 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 23 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 24 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 25 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 26 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 27 | **Outcome vector:** `L1-RESTRICTS` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 28 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 29 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 30 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 31 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 32 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 33 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 34 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 35 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 36 | **Outcome vector:** `L1-FREE` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 37 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 38 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 39 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 40 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 41 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 42 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 43 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 44 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 45 | **Outcome vector:** `L1-FREE` · `L3i-FREE` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 46 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 47 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 48 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 49 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 50 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 51 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 52 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 53 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 54 | **Outcome vector:** `L1-FREE` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 55 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 56 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 57 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 58 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 59 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 60 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 61 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 62 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 63 | **Outcome vector:** `L1-UNDECIDED` · `L3i-RESTRICTS` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 64 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 65 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 66 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 67 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 68 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 69 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 70 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 71 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 72 | **Outcome vector:** `L1-UNDECIDED` · `L3i-FREE` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |
| 73 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-NOT-IMPLIES-L4n` |
| 74 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `L5-IMPLIES-L4n` |
| 75 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-RESTRICTS` · `CORNER-UNDECIDED` |
| 76 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-NOT-IMPLIES-L4n` |
| 77 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-FREE` · `L5-IMPLIES-L4n` |
| 78 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-FREE` · `CORNER-UNDECIDED` |
| 79 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-NOT-IMPLIES-L4n` |
| 80 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `L5-IMPLIES-L4n` |
| 81 | **Outcome vector:** `L1-UNDECIDED` · `L3i-UNDECIDED` · `L3s-UNDECIDED` · `CORNER-UNDECIDED` |

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The execution appends,
after act 22's sentence in the same cell, exactly the sentence frozen for the vector reached.

**Case A — `G0` silent, `L1-RESTRICTS`, `L3i-RESTRICTS`, `L3s-RESTRICTS`, `L5-NOT-IMPLIES-L4n`.**
This is the case the freeze predicts.

> Act 23 tests, in one bundled round with four separately frozen targets, the three rungs act 21 left undecided and act 22 did not touch, and the corner of the naturality/factorization square act 22 left outside, at act 21's product configuration and against act 21's unchanged ladder, with a closed list of four named laws frozen with it, one per target. Preservation of admissibility on the whole orbit space has content on the class: a time-inhomogeneous law, named for that rung in advance, satisfies the standing hypotheses and totality and sends an unreached admissible class to a non-admissible tuple. Injectivity on classes has content on the class: a partial collapse, named for that rung in advance, satisfies every earlier condition and merges two admissible classes. Surjectivity onto classes has content on the class and is not forced by injectivity: a shift along an infinite family of admissible classes, named for that rung in advance, satisfies every earlier condition including injectivity and misses one admissible class. Factorization over independent systems together with every condition before naturality does not force representative-level gauge-naturality: a class-conditional relabelling of one factor, named for that corner in advance, satisfies every condition before naturality, factorizes into fixed local maps for the ordered decomposition, and admits no twisted-natural lift. Each verdict is of the exact frozen proposition at the exact configuration and of nothing in its neighbourhood; no verdict is inferred from another; no independence of conditions is asserted; no surviving law is said to interact or to fail to compose in any other sense; act 21's and act 22's own verdicts stand exactly as they state them; and deriving or recognising quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched, **no carrier is adopted as the physical one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or excludes a selection principle.

**Four clauses of Case A vary with the outcome, and they vary independently**, each replaced by the
sentence its target's other outcomes fix:

| target | clause | replacement when `UNDECIDED` | replacement when `FREE` / `L5-IMPLIES-L4n` |
| --- | --- | --- | --- |
| `G1` | the sentence beginning "Preservation of admissibility" | "Whether preservation of admissibility on the whole orbit space has content on the class is recorded undecided, with the obstruction named." | "Preservation of admissibility on the whole orbit space is implied by the standing hypotheses and totality, proved universally, and stays in the ladder." |
| `G2` | the sentence beginning "Injectivity on classes" | "Whether injectivity on classes has content on the class is recorded undecided, with the obstruction named." | "Injectivity on classes is implied by the conditions before it, proved universally, and stays in the ladder." |
| `G3` | the sentence beginning "Surjectivity onto classes" | "Whether surjectivity onto classes has content on the class is recorded undecided, with the obstruction named." | "Surjectivity onto classes is implied by the conditions before it, injectivity included, proved universally, and stays in the ladder." |
| `G4` | the sentence beginning "Factorization over independent systems together with" | "Whether factorization over independent systems together with every condition before naturality forces representative-level gauge-naturality is recorded undecided, with the obstruction named; the absence of an exhibited counterexample is not a proof of the implication." | "Factorization over independent systems together with every condition before naturality forces representative-level gauge-naturality at act 20's certified strength, proved universally at that configuration." |

**The execution composes the sentence from these substitutions and reports no other wording. No
composition closes `P0`**, and none reports either of its two parts closed.

## Naming a law is not endorsing it, FROZEN

Act 21's four points at its lines 1868–1879 govern here: naming is for testing; the round endorses
none; exclusion is only ever of the precise stated form; the lists are closed at this freeze.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a law's survival could be read as its adoption**, each carriage opening
with one line naming where it is being carried. It is act 21's clause with "Act 21" read as
"Act 23", and nothing else changed.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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

1. **"This is Schrödinger evolution", "the shift is a Hilbert-space map", "the conditions single out
   quantum dynamics", or any statement that a surviving or failing law is, resembles, approximates
   or points toward quantum evolution.**
2. **"The surviving law is the physical one."** The non-adoption clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
3. **"`L4n` and `L5` are independent", "the square is complete", or any report of a square of
   independences.** Four corners at one configuration are four facts about four named laws; the
   inference, if made, belongs to a later synthesis with its own freeze.
4. **"`L3s` follows from `L3i`", "`L3i` follows from `L3s`", "`L1` follows from `L3`", or any
   inference of one target's verdict from another's**, in either direction.
5. **"`Li` is free", "the corner is implied", from the absence of a witness, from a witness that
   failed to close, or from anything but a universal implication proof.**
6. **"The witness for `Gk` also settles `Gj`."** A witness answers the target the matrix authorizes
   and no other; its status on any later rung is not a verdict.
7. **"Act 21's `L1-UNDECIDED` was wrong", "act 22's swap witness shows …", or any rewriting or
   reinterpretation of act 21's or act 22's verdicts or witnesses.** They stand; this round's labels
   are this round's.
8. **"The evolution leaves the admissible set", read as a physical statement.** `Φ_MD` fails `L1`
   on one unreached class at one time; that settles the condition's content and nothing about any
   evolution.
9. **"The class space is infinite, so `L3` is vacuous"**, or any statement about `Ω_t`'s
   cardinality beyond what `Φ_HS`'s distinct classes exhibit: infinitely many distinct classes at
   the frozen configuration, and no more.
10. **"`OL1` shows the evolution preserves the admissible orbit space."** Descent gives maps on the
    ambient quotient and uniqueness of continuation; preservation is `L1`, and `L1` is what `G1`
    tests.
11. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate; about act 16's cancellation cell; about act 14's carriers; about act 18's
    `D`-axis; about act 10's anchor axis; about Track I, Source B or Source C; or about the substratum
    Lemma 24.1 rounds.**
12. **"`P0` is closed", or "`P0`'s trajectory part is closed."**
13. **"Act 12's classification is strengthened", "act 20's law is enlarged", "act 21's ladder is
    revised", "act 12's Hadamard family is extended."** All are consumed at merged strength; the
    Fourier family at an arbitrary parameter is this round's supply item and enlarges no merged
    statement.
14. **"The evolution is continuous", "smooth", "generated", "one-parameter"**, or any statement
    resting on structure the index type does not carry; in particular nothing about the parameter
    `z` of the Fourier family being a time, a flow or a generator.
15. **"OI and QM are inequivalent."**
16. **"The law list is exhaustive", or "the condition list is exhaustive."** Four laws, three rungs
    and one corner are tested; nothing outside them is refuted or endorsed here.
17. **A single-label headline.** The headline is the vector, selected verbatim from the table.

## Named hazards

1. **A witness that fails its own prefix.** **This is the bundled round's own hazard, and act 21's
   `DF1` and `DF2` exactly.** Each of `Φ_PC`, `Φ_HS` and `Φ_SC` must be an `L-PROP` law, which `ΦC`
   was not, and must satisfy every rung of its target's prefix; a witness failing one earns nothing
   and takes failure rule 2's fallback. The freeze's analyses check the two propagation clauses for
   every witness by name, which act 21's countercontrol table did not.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 23 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
2. **Sliding a witness.** `Φ_PC` fails `L3s` too, and `Φ_MD` fails `L2` and `L3i`; none of those is
   a verdict, and none may be reported as one. The matrix authorizes one target per witness.
3. **Inferring `L3s` from `L3i`, or conversely.** The two witnesses are separate, and a finiteness
   argument is neither available nor permitted.
4. **The self-controlled set not closed under the relabelling.** A `Φ_SC` conditioned on `[Gᵢ]`
   alone would send `[Gᵢ ⊠ G₂]` to `[σGᵢ ⊠ G₂]`, which the identity branch also fixes, and would
   fail injectivity; the freeze's statement conditions on both classes for this reason, and a
   variant that drops one is not `Φ_SC`.
5. **Reading the corner as an independence.** Four corners are four facts; forbidden sentence 3.
6. **A universal proof attempted while a witness is open.** The route order is witness first; a
   universal attempt before the witness has failed at a named step is a discrepancy.
7. **A verdict revealed before its commit.** The attestation set at every boundary and the
   partial-fact rule exist for it; a proof of `G3`'s injectivity that establishes `G2`'s failure
   before `G2`'s commit is a YES at that boundary.
8. **A verdict commit carrying two targets.** One per target, in order; a commit carrying two is a
   discrepancy for the later one.
9. **The zero tuple mistaken for an admissible tuple, or the Fourier family's unitarity assumed at a
   non-unit parameter.** The module commit proves both facts before any verdict, at the stated
   hypotheses.
10. **`relabel_product` at the exchange.** Not at issue here: every relabelling of this round is a
    product permutation `σ × 1` or `σ` on a factor, which `relabel_product` covers; act 22's
    exchange identity is consumed and not needed.
11. **`Li-FREE` from a search, or from census silence.** Failure rule 1.
12. **Restating a rung.** A `def` in this round's module is a defect of the round, and `R7-OLG`
    fails on it.
13. **Choosing a configuration after an outcome is known.** Every target is at the frozen product
    configuration; a witness that works at a different `Γ`, carrier or decomposition is an
    observation, not a repair.
14. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.**
    Carried from acts 18, 21 and 22.
15. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
16. **A landing without `P`**, **a stem both declared and recorded**, **a legacy constant
    written**, **editing this freeze after an outcome is known**, **a supersession outside the
    table** — each as act 21's hazards 28, 30, 31 and 34 state them, with `OLG` for `OLT`; the
    table here is empty, so any edit to a closed round's guard is a supersession outside it.
17. **A `B`-scoped precondition that the freeze's own text falsifies.** Every `B`-scoped row below
    is evaluated at `M` before the merge and is written so that the presence of this file in the
    tree does not fail it.
18. **A value in the freeze's reading that the kernel computes differently.** Recorded as a
    discrepancy of the reading; the label is earned by what the kernel proves and by nothing stated
    here.

## Non-doings

The round does not: **derive, recognise, approach or claim progress toward quantum evolution**, in
any paraphrase; adopt any surviving law as the physical one; adopt a carrier as the physical one or
define a carrier of its own; endorse any condition or any law; assert or deny that a cross-time law
is required or suffices; **restate, edit, add or remove any rung, or change any conjunction**;
**introduce or widen an equivalence**, or use one outside the frozen quotient list in any verdict;
**test any rung other than `L1`, `L3i`, `L3s` and, for the corner, `L4n` against the prefix with
`L5`**, or any law outside the frozen four, or any configuration outside the frozen product
configuration, or any decomposition other than `e = Equiv.refl`; infer any target's verdict from
another's; report an independence of rungs or a square of independences; attempt a
characterization, a census or a same-initial-orbit pair; **re-prove or strengthen acts 12, 13, 17,
18, 20, 21 or 22**; revise any merged label; rewrite, reinterpret or grade any verdict or witness
of act 21's or act 22's note; ask the threading question or the cross-time representative question,
in either direction; touch act 16's cancellation cell; state anything about act 18's `D`-axis, act
10's anchor axis, act 14's carriers, Track I, Source B or Source C, or the substratum Lemma 24.1
rounds; realize any transition as an operator, unitary, generator or group element; introduce
continuity, smoothness or a generated evolution; alter any existing manifest record, supersede any
closed round's contract, or write a legacy seal constant; edit any manuscript; close `P0` or either
of its parts.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

Act 21's statement at its lines 2130–2143 is carried in full: the question is not asked, not
bounded and not attempted; an execution that begins asking whether any law here looks like unitary
evolution has left the round's scope, and what it finds is recorded as an observation and not
executed. **"Resembles", "is consistent with", "is what one would expect from" and "is a step
toward" are forbidden sentences.**

### What act 23 does and does not change about `P0`, and about the classification

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 23 can
change is the recorded content of three rungs of act 21's ladder, and one implication among its
rungs.

**On the classification act 21 named as the obstruction to `L-FAMILY`, stated once and narrowly.**
Each witness that fails its rung is a law a full-ladder classification at the product configuration
must **exclude**, and a classification of the corresponding prefix must **account for**, modulo the
frozen law equivalence. **These product-configuration results place no inclusion requirement on the
separate single-carrier classification at `Γ ≡ ¼`, `|A| = 1`, and no requirement that any parameter
set contain any group or any family.** That is the whole of what this round's outcomes bear on, and
it is an observation for the later round that freezes the classification, not a finding of this one.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about
what fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT
CERTIFIED**.

## Definition budget

**The execution introduces NO top-level Lean definition.** The budget is **zero**, and it is stated
as a number so that it cannot drift: no `def`, `abbrev`, `structure`, `class`, `instance`, `axiom`
or `opaque`. Every rung is act 21's declaration consumed; the four witnesses, the Fourier family and
its sequence, the product tuples, the Hadamard objects, the permutations and the visible families
are bound variables pinned by equations in the statements that need them, as `phiCTRL_census` pins
its transition family. Each target's prefix is written out as the corresponding conjuncts of
`LadderConds` wherever a statement needs it, and never abbreviated by a definition. **A definition
requires its own append-only amendment**, separately frozen and merged before the work it affects.

Theorems are not budgeted. The execution proves whatever lemmas its verdicts need — the
product-marginal lemma, the Fourier-family admissibility and its invariant, the separations, the
non-realizability of the zero tuple, the four witnesses' conjuncts, the corner corollary — as named
results, each printed in the axiom table.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `G1`, `G2`, `G3` and `G4`, whichever label each reaches
other than UNDECIDED. `decide` over finite index types is permitted; `native_decide` is not, and
neither is `sorry`. `Classical.choice` is expected wherever `sh1_sufficiency`, `product_realizable`
or the classical branch of `Φ_HS`'s statement is used. **`G0` is type P and carries no evidence
level.**

## The chronology control — through the manifest and never a constant

The execution's guard tag is **`R7-OLG`**, reserved here and created by the execution pull request.
The round's stem is **`OLG`**; its seal state is the prospective declaration during execution and
the record `verification/seals/OLG.json` from `P`, and **no constant**.

1. **This preregistration blob is merged into `main`, and its merge commit `B` certified by a fully
   green main-push run including the control-plane base check in mode `B`, before any
   execution-specific act 23 object enters the repository tree** — any Lean statement about any of
   the four witnesses, the product-marginal lemma, the Fourier family at a symbolic parameter or the
   corner; any probe clause; any result artifact; any manifest record or declaration for `OLG`.
   **The single permitted exception is the analysis recorded inside this control-plane blob itself**,
   merged *as* the freeze, including the proof routes and the chronology simulation.
2. **The execution pull request's base must be exactly `B`.** The execution's first commit sets
   `_MANIFEST_PROSPECTIVE = {'OLG': B}` and `_MANIFEST_BASELINE = {'base': B, 'authorized':
   ('OLG',)}`, both outside the validator's marker-bounded regions, and nothing else.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control**, fail-closed.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — one keyed call, `_si2_authority('OLG', tag='R7-OLG')` — with `pull_request.head.sha`
   from the Actions event payload as the target in pull-request continuous integration, `HEAD`
   otherwise, **never** the synthetic merge commit; an unresolvable head fails closed.
5. **The check excludes pre-freeze side history**: `B` ancestor-of `H`, and every commit in
   `git rev-list H ^B` a descendant of `B`, fail-closed — the validator's `EXECUTION` classification.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails.
7. **Archive mode is the record.** At `L` the validator classifies `OLG` as `LANDED-PENDING-PIN`;
   `P` writes `verification/seals/OLG.json` with `base` = `B`, `sealed_head` = `E`, `merge` = `L`,
   removes the `OLG` entry from the prospective declaration, and touches nothing else; from `P` on
   the validator classifies `OLG` as `ARCHIVED`, each conjunct fail-closed.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the records at `B` against mutation, removal and any addition other than `OLG`.
9. **No `_OLG_BASE`, `_OLG_SEALED_HEAD` or `_OLG_MERGE` exists at any commit of the round**, and
   `SI-3`'s standing contract holds at every head.
10. **The ordering obligation's records are checked mechanically by `R7-OLG`**, each with a
    mutation control: (a) the module at every commit from the module commit to `E` contains no
    top-level definition of any kind, by extraction of every declaration keyword at line start;
    (b) the module imports `OIBridge.OrbitLawRigidityTwisted` and
    `OIBridge.OrbitLawNaturalityFactorization`; (c) each witness is pinned, in every theorem that
    names it, to its frozen equation, and no theorem block names a witness other than its own
    target's; (d) the stage-A commit, the module commit and the four verdict commits are on the
    first-parent chain from `B` to `E`, in that order, the module absent before the module commit
    and present from it on, and the module commit carrying no theorem whose name is one of the four
    verdict names; (e) each verdict theorem first appears at its own verdict commit and at no
    earlier commit. A synthetic `def` inserted into the module text, a synthetic reassignment of a
    witness to another target's theorem, a verdict theorem inserted into the module commit's text
    and a fabricated SHA off the chain each **fail** the control.
11. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested:
    the round's shape as sealing with `E` → `L` → `P`; the declaration table and the seven records;
    the **five** attestation answers, one per span; the sentence that no rung was restated and no
    equivalence was widened; each target's label carried with its frozen sentence verbatim and with
    the failing conjunct and separating classes named; **the outcome vector, equal verbatim to one
    row of the table**; **the statement that no verdict was inferred from another**; **the statement
    that no independence of rungs is asserted**; **the statement that act 21's and act 22's
    historical verdicts stand unchanged**; the witness-authorization matrix reported as honoured,
    with no witness reassigned; THE CLAUSE carried complete at every mention with its count; and the
    frozen `P0` sentence for the case reached present in `verification/ROADMAP.md` verbatim, after
    act 22's.

### The contracts this round supersedes, named in advance — none

**Under `§A.37`'s closed-round rule, `AGENTS.md` lines 1055–1061, a closed round's contract that
reads the current round's declaration would be superseded here. The measurement recorded above
found none**: at `D` every closed round's guard reads its own record, and the placeholder
declaration failed nothing. **The execution edits no contract of any closed round.** Should the
execution find that a closed round's contract fails on an act 23 head for a reason that has nothing
to do with act 23's result, that is a discrepancy recorded in the result note, and the disposition
is an append-only amendment to this freeze, separately merged, and not an edit made during
execution.

### What must have merged before the execution begins, checkable mechanically

Each row below names its scope — at `D`, at `B`, or from `D` to `B` — and the block after the table
is the machine-checkable form of the same rows, which the release gate lints and the workflow's
`control-plane-base-check` job evaluates in mode `M` against the candidate merge of this pull
request and, after the merge, in mode `B` against the actual merge commit.

| # | scope | precondition | mechanical check |
| --- | --- | --- | --- |
| 1 | `D` | The names were free when chosen | `git grep -l -- 'R7-OLG' D`, `git grep -l -- '_OLG' D`, `git grep -l -- 'OLG' D`, `git grep -l -- 'OrbitLawGaps' D`, `git grep -l -- 'orbit-law-gaps' D` and `git grep -l -- 'act-23' D` each return nothing |
| 2 | `D` | The seals tree at `D` is the pinned one | `git rev-parse D:verification/seals` is `981a23a164b091ae0093facf81f7bd5ccf12e004`, twenty-seven records, twenty-one `sealed` and six `base-only` |
| 3 | `D` | The guard at `D` is green and carries no legacy constant | eighty-six `R7-*` tags, all `PASS`, on main-push run 35441377788; `_SI2_LEGACY_RE` finds zero assignment statements |
| 4 | `D → B` | `D` is an ancestor of `B` | `git merge-base --is-ancestor D B` succeeds |
| 5 | `D → B` | The blobs this round consumes are unchanged | each of the first thirteen paths of the start-state table has at `B` the blob the table names (the `frozen-blob` lines of the block) |
| 6 | `B` | No act 23 execution object exists | the guard file at `B` contains no `R7-OLG` and no `_OLG`; no `verification/seals/OLG.json`; no `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean`; the round directory holds nothing but `preregistration.md` and, if any, `amendments/amendment-*.md` |
| 7 | `B` | No round is executing at `B` | the guard file at `B` carries `_MANIFEST_PROSPECTIVE = {}` |
| 8 | `B` | Acts 21 and 22 are sealed at `B` | `verification/seals/OLT.json` at `B` carries `round` `OLT`, `kind` `sealed`, `base` `10d1041bcc10f25d9f643629d4431acbd0f65a1e`, `sealed_head` `b27f3f1630a25667b6728518d06b55fbdabe0d11`, `merge` `4bd732c54e0804bda3b796fcb93e91b5c4299b87`; `verification/seals/OLN.json` at `B` carries `round` `OLN`, `kind` `sealed`, `base` `ccd5704fd157348903cbdea746d24cf5d5498b78`, `sealed_head` `64b3d28e9b0265eb96eec61899f6de474496a3a3`, `merge` `664de6b63eb1f8b55e88c314d326176c4c97ff70`; the guard file at `B` carries the `R7-OLT` and `R7-OLN` checks |
| 9 | `B` | Acts 21's and 22's modules are wired | `OIBridge.lean` at `B` imports `OIBridge.OrbitLawRigidityTwisted` and `OIBridge.OrbitLawNaturalityFactorization` |
| 10 | `B` | This control plane is in the tree at its path | `verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md` exists at `B`; its blob is the one the `R7-OLG` clause pins, which the execution's first act verifies by `git hash-object` and the block cannot state of itself |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are not inputs. **The claim is scoped to the repository record.**

```control-plane-preconditions
d: 59c1b7efe36d7768cf53120997ff201e32c8e458
merged: false
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean 860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8
frozen-blob: verification/lean-mathlib/OIBridge/OrbitLawNaturalityFactorization.lean d41b157a3f38d4ebedbe11ad9682a8693836a383
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md 316d635a31f91faebeeebef7688b30002d24b4ca
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1
frozen-blob: verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md bb02ef41eb221696ffa45c9281b69553c8279cbb
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/preregistration.md cc83ddb9ecbc2c8e884d160d1d3ffeba2575baea
frozen-blob: verification/programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization/result.md b0f9ae48dbb2044de353efe1a0f5a1fab4f88c9e
frozen-blob: verification/seals/OLT.json 8ed0ef5391410db3a112cbe845d27536b7c1ab9b
frozen-blob: verification/seals/OLN.json 1552065eeae26b5e07ad1cfe1cdb97b76aefa1bb
frozen-blob: verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean 4c1137f35600320b9273c857ec62271341b05cd0
frozen-blob: verification/lean-mathlib/OIBridge/TwoSidedGauge.lean 4bba2040c33424fafbc6d31c0d63b86dff33691a
frozen-blob: verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean cb14c43b0becfe1a379ae3615d5553723ede9163
frozen-blob: verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean afc22cfc93b244c80e1c55a273dcfda1ddebb121
# row 1: name freedom, a drafting-time fact
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-OLG' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -- '_OLG' $D", "expect": "empty"}
{"id": "d1-bare-free", "scope": "D", "check": "git grep -l -- 'OLG' $D", "expect": "empty"}
{"id": "d1-module-free", "scope": "D", "check": "git grep -l -- 'OrbitLawGaps' $D", "expect": "empty"}
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'orbit-law-gaps' $D", "expect": "empty"}
{"id": "d1-act-free", "scope": "D", "check": "git grep -l -- 'act-23' $D", "expect": "empty"}
# row 2: the seals tree at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = 981a23a164b091ae0093facf81f7bd5ccf12e004", "expect": "exit0"}
# row 4: provenance
{"id": "db4-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
# row 6: no execution object; the names occur in this file, so the guard, the seals and the tree are read directly and never through git grep
{"id": "b6-guard-clean", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-OLG' -e '_OLG'", "expect": "empty"}
{"id": "b6-no-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'OLG.json'", "expect": "empty"}
{"id": "b6-no-module", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/lean-mathlib/ | grep -e 'OrbitLawGaps'", "expect": "empty"}
{"id": "b6-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/ | grep -v -e '/preregistration.md$' -e '/amendments/amendment-[0-9][0-9]*.md$'", "expect": "empty"}
# row 7: no round executing
{"id": "b7-no-prospective", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e '^_MANIFEST_PROSPECTIVE = {}$'", "expect": "nonempty"}
# row 8: acts 21 and 22 sealed
{"id": "b8-olt-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLT.json | tr -d ' \\n' | grep -e '\"round\":\"OLT\",\"kind\":\"sealed\",\"base\":\"10d1041bcc10f25d9f643629d4431acbd0f65a1e\",\"sealed_head\":\"b27f3f1630a25667b6728518d06b55fbdabe0d11\",\"merge\":\"4bd732c54e0804bda3b796fcb93e91b5c4299b87\"'", "expect": "nonempty"}
{"id": "b8-oln-sealed", "scope": "B", "check": "git show $REF:verification/seals/OLN.json | tr -d ' \\n' | grep -e '\"round\":\"OLN\",\"kind\":\"sealed\",\"base\":\"ccd5704fd157348903cbdea746d24cf5d5498b78\",\"sealed_head\":\"64b3d28e9b0265eb96eec61899f6de474496a3a3\",\"merge\":\"664de6b63eb1f8b55e88c314d326176c4c97ff70\"'", "expect": "nonempty"}
{"id": "b8-olt-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLT'\"", "expect": "nonempty"}
{"id": "b8-oln-guard", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e \"check('R7-OLN'\"", "expect": "nonempty"}
# row 9: acts 21's and 22's modules wired
{"id": "b9-import-olt", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawRigidityTwisted$'", "expect": "nonempty"}
{"id": "b9-import-oln", "scope": "B", "check": "git show $REF:verification/lean-mathlib/OIBridge.lean | grep -e '^import OIBridge.OrbitLawNaturalityFactorization$'", "expect": "nonempty"}
# row 10: this control plane at its path
{"id": "b10-self-present", "scope": "B", "check": "git cat-file -e $REF:verification/programmes/oi-qm/track-b/act-23-orbit-law-gaps/preregistration.md", "expect": "exit0"}
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
- **The stage-A commit comes first**, then **the module commit** with shared lemmas and no verdict,
  then **the four verdict commits in the order `G1`, `G2`, `G3`, `G4`**, one per target; their SHAs
  are recorded, and the attestation set is answered for each of the five spans.
- **Then exactly one execution pull request**, based on `B`, carrying the Lean module, the result
  note, the `R7-OLG` guard clause, the two declarations, the `ROADMAP` propagation and the census
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
2. **the ordering obligation's seven records** and the attestation set's **five** answers, one per
   span, with the freeze-supplied facts listed;
3. **`G0`** — the bounded search, recorded in full;
4. **`G1`** — `L1`'s label with its frozen sentence, the theorem named, the failing conjunct and
   separating class named, `Φ_MD`'s prefix conjuncts each reported separately;
5. **`G2`** — `L3i`'s label, likewise, for `Φ_PC`;
6. **`G3`** — `L3s`'s label, likewise, for `Φ_HS`, with the family's admissibility and the
   distinctness of its classes reported as the module commit's lemmas and **the statement that no
   finiteness of the class space was assumed or claimed**;
7. **`G4`** — the corner's label with its frozen sentence, `Φ_SC`'s prefix conjuncts each reported
   separately, `L5` reported with its factor maps named, the `L4n` failure with its separating
   classes, and **the statement that no independence of rungs is asserted**;
8. **the outcome vector**, one row of the table verbatim, and **the statement that no verdict was
   inferred from another**;
9. **the witness-authorization matrix as honoured**: each witness tested for its own target and
   nothing else, no witness reassigned, no alternative substituted;
10. **the scope boundary as honoured**: nothing derives, recognises or approaches quantum evolution;
    act 21's and act 22's verdicts untouched; the threading, act 16's cell, act 18's `D`-axis, act
    10's anchor axis and act 14's carriers untouched;
11. **the non-adoption clause carried verbatim at each mention**, with the count of carriages;
12. the frozen `P0` sentence for the case reached, appended after act 22's, the row's label
    unchanged;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 12, 13, 17, 18, 20, 21 and 22 — every merged label consumed, none revised;
15. the definition count against the zero budget;
16. the chronology certification, naming the property certified, the ten preconditions with their
    scopes and the block's rows as the base check reported them at `M` and at `B`, the validator's
    classification of `OLG` at `E`, `L` and `P`, the empty supersession table reported as
    honoured, and `SI-3`'s standing contract reported as holding;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired — including any value of the freeze's
    reading the kernel computed differently;
19. the observation, if any, for the classification round, stated once and narrowly as the
    non-doings section fixes it.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Every item below is a call
already made**, and the body of this freeze is written to them throughout. **This freeze carries no
open decision.**

1. **The round is the first bundled round**: four targets, one per rung or corner, at act 21's
   product configuration, quotient and unchanged ladder; act 21's and act 22's verdicts consumed as
   landed and not rewritten; the swap witness not reinterpreted.
2. **Each target has its own proposition, witness, verdict rule and failure interpretation**, and
   the three-way discipline — universal proof for `FREE` or for `L5-IMPLIES-L4n`, an
   earlier-prefix witness for `RESTRICTS` or for the corner, otherwise `UNDECIDED` — governs each,
   `L3s` independently of `L3i`.
3. **The corner is frozen narrowly** as the non-implication from the prefix through `L4d` with `L5`
   to `L4n`, never as an independence square; synthesis, if any, is a separate freeze.
4. **The three safeguards are this round's freeze rules and not `AGENTS.md` rules**: a fixed
   execution order `G1` → `G2` → `G3` → `G4` with one verdict commit per target and the attestation
   set at every boundary; the witness-authorization matrix; the outcome-vector table from which the
   headline is selected verbatim. A witness discovered or learned during a later target may not be
   retroactively reassigned to an earlier target.
5. **The two failure rules are frozen**: a universal theorem not obtained is `UNDECIDED`, never
   `FREE` or `RESTRICTS`; an authorized witness that unexpectedly violates an earlier rung is
   recorded, the witness set is not repaired and not slid, and the target takes its preregistered
   fallback.
6. **`L1-FREE` and `L3*-FREE` require universal proofs**; failure to produce them is `UNDECIDED`,
   never inferred from census silence.
7. **No drafting-time outcome check was run**; the analyses are the freeze's reading; the one
   simulation run concerns chronology only and found no supersession needed.
8. **`§A.37`'s `D`/`B`/`M` vocabulary governs**: scoped precondition rows, mode `M` validation of
   the candidate merge before the merge, `B` reserved for the certified control-plane merge.
9. **SEALING**, under the manifest protocol: stem `OLG`, tag `R7-OLG`, `E` → `L` → `P` with `P`
   mandatory, the prospective declaration during execution and the record from `P`; no
   supersession; nothing in any closed round's guard touched.
10. **The definition budget is zero.** Act 21's declarations are consumed and none is restated; the
    Fourier family and its sequence are bound by equation.
11. **Acts 12, 13, 17, 18, 20, 21 and 22 are consumed at merged strength**: not re-proved, not
    strengthened, not redefined.
