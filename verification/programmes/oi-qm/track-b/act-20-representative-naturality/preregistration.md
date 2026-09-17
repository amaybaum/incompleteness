# Track B act 20 — what "gauge-natural" means: the naturality classification: CONTROL PLANE

Owner-called. This file is the whole of act 20's control plane and is merged **alone**, before any
execution object exists. It takes up the one thing act 19 discovered and could not settle: **the
phrase "gauge-natural" was underspecified, between three notions a formalization must choose among
and that prose does not separate.** Act 20 formalizes the three notions, constructs the carrier
relabelling's representative-level lift, and determines which of the three that lift satisfies.

**Act 20 is the naturality-classification round only.** It is **not** a rigidity round. It freezes no
condition ladder, runs no census, counts no survivors, reports no rigidity headline, and runs no
same-initial-orbit test. It does **not** choose which condition a later round's naturality rung ought
to impose. It settles the mathematics that choice depends on and stops.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–778**, quoted verbatim at this base —
the numbered item's opening sentence, ending part-way through line 778:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes
>    ownership of changing existing seal state — takes a pin commit `P`, and `P`
>    is mandatory.**

This freeze **creates new seal state**. The execution writes a new Lean module with its own guard
clause in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-RNT`**, and that
clause carries the archive-mode constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_RNT_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_RNT_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_RNT_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_RNT_SEALED_HEAD` to `E` and `_RNT_MERGE` to `L`, moving the `R7-RNT` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_RNT_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

### The lifecycle derivation, and why it comes out SEALING

**The lifecycle is derived from what the round owns, and not from the fact that acts 13 through 19
each declared themselves sealing.** The rule is: act 20 is sealing **if and only if** its execution
creates a new formal object whose chronology matters to the result. Run against this freeze's own
scope, the derivation is short and it comes out positive for a reason peculiar to this round.

1. **The execution creates new formal objects, and they are the round's whole product.** Three named
   `Prop`s for the three notions; a representative-level lift of the carrier relabelling; an induced
   map on the left and right gauge data; and a theorem classifying the lift against the three
   notions. None of these exists at the base — this freeze records below that the tree contains no
   declaration of any of them.
2. **Their chronology is load-bearing, and this is the round in which that is most acutely true.**
   Act 19 closed because a definition was rewritten mid-round after its author had reasoned, on
   paper, about what the carrier relabelling's lift does. **Act 20's subject is exactly that
   question.** If act 20's three notions were stated after their author already knew which one the
   relabelling satisfies, the classification would be a choice dressed as a finding: one would be
   reporting a definition tuned to its own answer. The ordering obligation frozen below is therefore
   itself a chronology claim, and an ancestry guard rooted at this control plane's merge commit is
   what makes it enforceable rather than aspirational.
3. **A new module with new named results is new seal state** under `§A.37`'s definition, and a new
   `R7-*` ancestry/archive guard is new pin state.

**Therefore act 20 is SEALING, and it owns no other seal state.**

**The negative branch is recorded too, because the rule has one.** Were act 20 directed to be purely
expository over existing formal results — adding no Lean module, no named result and no guard clause
— it would own no seal state, would take `L` alone under `§A.37` item 2, and would **not** acquire a
pin merely by precedent. **That branch is not this round's shape.** In it the three notions would
have no kernel statement an auditor could diff across two commits, the ordering obligation would
lose its mechanical check entirely, and the round's central claim — that the notions were fixed
before the classification was known — would rest on the result note's own testimony. Given what act
19 closed for, that is not an acceptable shape for this round, and the freeze says so rather than
presenting the two as equivalent.

### The tag, the stem, the module and the round directory are free at this base

At **`0840e37b4310a9ee73053d11924ce6517d5b6f8e`**, the certified `main` this freeze is written
against and act 20's only permitted base:

- `git grep -- 'R7-RNT' 0840e37` returns nothing anywhere in the tree, and the tag is absent from the
  `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries.
- `git grep -- 'RNT' 0840e37` returns nothing anywhere in the tree — **the bare three-letter form
  does not occur in prose, in Lean, in Python or in any manuscript**, so a bare-stem search for it is
  unambiguous. This is the property a freedom check needs, and it is why `RNT` was taken.
- `git grep -- '_RNT' 0840e37` returns nothing, so no constant whose name contains the stem `_RNT`
  exists in `verification/lean/edge_rigidity_probe.py` or anywhere else.
- **The alternatives were checked before `RNT` was chosen**, and the check is recorded so the choice
  is not re-litigated. `NAT`, `GN` and `EQV` were rejected without a search, because their bare forms
  are common substrings of English and of Lean identifiers — *natural*, *naturality*, *equivalence*,
  *equiv* — and a bare-stem freedom check for any of them would be ambiguous in exactly the way act
  18 recorded for `ICS` and `CTS`. `OLR` was rejected although it is free outside act 19's directory:
  it is act 19's reserved stem, act 19's control plane is not withdrawn, and reusing a closed round's
  stem would make the record harder to read rather than easier.
- **`OLR` and `R7-OLR` are left alone.** `git grep -- '_OLR' 0840e37` and `git grep -- 'R7-OLR'
  0840e37` return hits in act 19's `preregistration.md` and `closure.md` and **nowhere else** — not
  in the guard file, not in any Lean module, not in the census. Act 20 adds no occurrence of either
  and changes none.

**The round directory and the module name are free at this base too.** `git ls-tree -r 0840e37
--name-only` lists 631 paths and contains no path matching `act-20` and no path matching
`RepresentativeNaturality`; `git grep -- 'act-20'` and `git grep -- 'RepresentativeNaturality'` both
return nothing anywhere in the tree. The round directory is
`verification/programmes/oi-qm/track-b/act-20-representative-naturality/` and the module is
`verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`.

**The seven declaration names this round's budget reserves are free at this base as well**, by exact
string over the whole tree: `StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition`,
`RelabelLift`, `RelabelInducedLeft` and `RelabelInducedRight` each return nothing under `git grep`.

**One nearby word is recorded so that it is not mistaken for a collision.** The strings *natural*,
*naturality* and *equivariant* occur in other programmes' Lean modules and in Track I material.
Those are different objects in different programmes and none of them carries any of the seven names
above or the stem `_RNT`. **A shared English word is not a collision**, and every freedom check in
this section is by exact string and not by theme.

### What this round does NOT own, named exhaustively

It alters **no existing seal constant**. In particular `_XTS_BASE`, `_XTS_SEALED_HEAD` and
`_XTS_MERGE` — act 18's seal — and `_TRJ_BASE`, `_TRJ_SEALED_HEAD` and `_TRJ_MERGE` — act 17's — and
`_RNC_BASE`, `_RNC_SEALED_HEAD` and `_RNC_MERGE` — act 16's — and `_TCF_BASE`, `_TCF_SEALED_HEAD` and
`_TCF_MERGE` — act 15's — and `_PQT_BASE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE` — act 14's — and
`_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE` — act 13's — and `_A12P_*`, `_SGT_*`, `_TSG_BASE`
and `_CLG_BASE` are **read and never written**. An archive seal belongs to the round that set it:
touching the guard file that carries those constants does not make this round their owner, and the
execution's diff against `edge_rigidity_probe.py` **adds** the `R7-RNT` clause and changes nothing
else in the file.

**It owns nothing of act 19's.** Act 19's control plane is not edited, not amended, not withdrawn and
not reinterpreted; act 19's closure is not edited; act 19's reserved tag and stem are not taken over;
and act 19's execution branch is not merged, cherry-picked from, or cited as settled.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`0840e37b4310a9ee73053d11924ce6517d5b6f8e`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

### Act 19's closure, which is the authoritative account of why act 20 exists

`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/closure.md`, blob
**`3d37529cb89a4d2bb60281f14f15645e3beaeb4c`** at this base. **This blob is pinned by SHA as a
locating control**, because act 20's subject is the problem this note names and act 20 may not
restate that problem in its own words without the note's wording in front of it.

**Lines 120–121**, the sentence that names the gap:

> The phrase **"gauge-natural" was underspecified**, between at least three notions that a formalization
> must choose among and that prose does not separate:

**Lines 123–127**, the table that names them — act 20's three notions are these three and no others:

> | notion | statement | what it asserts |
> | --- | --- | --- |
> | strict equivariance | `Ψ (g * U) = g * Ψ U` | the lift commutes with each gauge element itself |
> | twisted equivariance | `Ψ (g * U) = α g * Ψ U`, for one fixed preregistered `α` | the lift commutes up to a fixed induced map on the group |
> | orbit preservation | `Ψ (g * U) = g' * Ψ U`, for some `g'` | the output stays in the orbit, with nothing fixing which element |

**Lines 129–131**, which says what was and was not settled:

> The third is what `52b64009` states, and it should not be called commutation. The scientifically
> interesting question — which act 19 could not settle, because settling it during execution is exactly
> what the ordering obligation forbids — is whether the freeze intended the first or the second.

**Lines 133–137**, which assigns the question to this round and bounds what this round may do with it:

> **That question belongs to a later round with its own freeze**, and this closure neither answers it
> nor prejudges it. The observation to carry forward is that a condition asking one object to respect
> another's symmetry is not fully stated until the respecting is pinned to a particular map, and that
> the difference between the three rows above is the difference between a rigidity verdict that means
> something and one that does not.

**Lines 71–80**, the chronological ground on which act 19 closed, which is what act 20's ordering
obligation is strengthened against:

> **The second ground is chronological and is independent of the first.** The execution disclosed,
> unprompted, that between the ladder commit and the discrimination commit it had worked out by hand
> that a carrier relabelling's natural representative-level lift is a reindexing rather than a left
> multiplication, and that this reasoning is what motivated the change. That is **candidate-specific
> information bearing on which laws survive**, arriving before the rung was rewritten and pointing in
> exactly the direction the rewrite went. The ordering obligation fixes the ladder before knowledge of
> which laws survive, not merely before a theorem appears in version control. A rung rewritten after
> such knowledge does not acquire clean preregistered status from the fact that no theorem had yet been
> committed. **The disclosure establishes the contamination rather than curing it**, and the round is
> better for the disclosure having been made.

**Lines 108–110**, which fixes the status of act 19's execution branch for every successor including
this one:

> **The lower-level proofs on the execution branch remain available as research material.** They are
> not evidence for any later round, and no later round may cite them as settled. Anything a successor
> wants from them it proves again under its own freeze.

**Lines 8–10**, which fixes the register in which act 20 must speak about act 19:

> **Nothing here says any mathematics is false.** The distinction the note keeps throughout is between
> a statement being refuted and a statement being **uncertified by this round**. The conclusions named
> below are the second. They may well be true; act 19 is not what establishes them.

### Act 19's freeze, still valid, not withdrawn, and act 20's subject matter

`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md`, blob
**`8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`** at this base. The closure states at its lines 20–21
that this freeze is intact and is not withdrawn by the closure. Act 20 reads it and edits nothing in
it.

**Lines 554–558**, act 19's `L4n` as its freeze states it — the sentence whose meaning act 20 is
convened to determine:

> **`L4n` — representative-level gauge-naturality.** `Φ` lifts to representatives naturally under act
> 12's two-sided moves: for the constant and time-dependent in-fibre left moves of `LeftFibreGroup`
> and the strong and weak right gauges at `a₀`, the transition commutes with the merged
> transformation laws on `FibreGram` — act 12's `fibreGram_left_mul` and `fibreGram_mul_weak_apply`
> are the two laws it must commute with.

**Lines 912–914**, act 19's frozen `ΦP`, the carrier-relabelling transition whose lift act 20
constructs:

> **Statement.** For a permutation `σ` of `V` under which `Γ` is invariant — `Γ t (σ i) (σ j) = Γ t i
> j` at every `t` — `Φ̂ G i = (G (σ i)) ∘ σ`, the simultaneous relabelling of the fibre index and of
> both matrix indices by `σ`.

**Lines 566–567**, act 19's own statement of the distinction act 20 formalizes:

> **`L4n` is a genuine strengthening and is tested as one.** Descent says the transition is a function
> on classes. Naturality says it comes from a move on representatives that the invisible gauge cannot
> see.

### The two merged transformation laws the notions are stated against

Act 12's laws, read as Lean at this base and not as description of Lean.
`verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, **line 207**, the left law:

> theorem fibreGram_left_mul {L : Matrix (V × A) (V × A) ℂ} (hL : LeftFibreGroup L) (a₀ : A)
>     (U : Matrix (V × A) (V × A) ℂ) (i : V) : FibreGram a₀ (L * U) i = FibreGram a₀ U i := by

and **lines 242–245**, the right law:

> theorem fibreGram_mul_weak_apply {a₀ : A} {K : Matrix (V × A) (V × A) ℂ} {c : V → ℂ}
>     (hc : ∀ p j, K p (j, a₀) = if p = (j, a₀) then c j else 0)
>     (U : Matrix (V × A) (V × A) ℂ) (i j k : V) :
>     FibreGram a₀ (U * K) i j k = star (c j) * FibreGram a₀ U i j k * c k := by

**The asymmetry between the two laws is the reason the round is not trivial, and the freeze names it
here rather than letting the execution discover it.** The left law says the left move is **invisible**
to the fibre-Gram data. The right law says the weak gauge acts on that data by a **specific**
transformation determined by specific anchored phases. A lift that commutes with the first says
something different from a lift that commutes with the second, and the closure's three rows differ
from one another on both sides at once. This is the freeze's **reading of two merged statements**, it
is offered as the reason the round is worth running, and **it is not a finding**: no target below
rests on it.

The classes themselves, `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` **line 78** and
`verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` **lines 101 and 114**:

> def LeftFibreGroup (L : Matrix (V × A) (V × A) ℂ) : Prop :=
>   L ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ p q : V × A, p.1 ≠ q.1 → L p q = 0

> def StrongAnchorStabilizer (a₀ : A) (K : Matrix (V × A) (V × A) ℂ) : Prop :=
>   K ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ p j, K p (j, a₀) = if p = (j, a₀) then 1 else 0

> def WeakAnchorStabilizer (a₀ : A) (K : Matrix (V × A) (V × A) ℂ) : Prop :=
>   K ∈ Matrix.unitaryGroup (V × A) ℂ ∧
>     ∃ c : V → ℂ, ∀ p j, K p (j, a₀) = if p = (j, a₀) then c j else 0

and `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` **lines 95–97, 102–103 and 108–110**, the
fibre-Gram data, its phase equivalence and the realizable tuples:

> def FibreGram (a₀ : A) (U : Matrix (V × A) (V × A) ℂ) (i : V) : Matrix V V ℂ :=
>   (U.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
>     * U.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀))

> def GramPhaseEquiv (G G' : V → Matrix V V ℂ) : Prop :=
>   ∃ c : V → ℂ, (∀ j, ‖c j‖ = 1) ∧ ∀ i j k, G' i j k = star (c j) * G i j k * c k

> def RealizableGram (A : Type) [Fintype A] (Γ : Matrix V V ℝ) (G : V → Matrix V V ℂ) : Prop :=
>   (∀ i, (G i).PosSemidef) ∧ (∀ i, (G i).rank ≤ Fintype.card A)
>     ∧ (∑ i, G i = 1) ∧ ∀ i j, G i j j = (Γ i j : ℂ)

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 697–700**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

**The mandated base, stated as this round's own commitment.** The execution branches from the merge
commit of **this** control-plane pull request and from **nothing else** — not from `main` at any
later point, not from a sibling lane's head, not from act 19's execution branch, and not from a
rebase of any of them. **Its first act is to verify that the preregistration at that base carries the
blob this freeze names**, before any target is executed, and to record the verification in the result
note. If the blob differs, the execution records the discrepancy and does not repair the freeze.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `0840e37b4310a9ee73053d11924ce6517d5b6f8e`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/closure.md` | `3d37529cb89a4d2bb60281f14f15645e3beaeb4c` |
| `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md` | `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/preregistration.md` | `fd3fa1359188966cae006deba4944a14aab5f3dd` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/result.md` | `a252b885c6f7f5f31d3ac101070e7f6ee1ebf5d6` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md` | `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md` | `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` | `47eb21e22845f0319926227c80d0d7f2f033880b` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/AnchorRobustness.lean` | `b74202bc160918b32ca1b333da532a141ea8015d` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/ROADMAP.md` | `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**`verification/ROADMAP.md` is in the read-only table above, and that is a deliberate narrowing of
this round relative to acts 13 through 19.** Each of those rounds both read the `ROADMAP` and
appended a frozen post-round sentence to the `P0` row. **Act 20 appends nothing to it.** The reason
is recorded in its own section below and is put to the owner as an open decision before this freeze
merges.

### The files this round writes

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/lean/edge_rigidity_probe.py` | `5cdd759534c9668c7f447b35a95ff888c973408a` | the `R7-RNT` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `81814f25d9ea17aee2e15237af5bbfbe8dd92cfa` | one import line added |
| `verification/lean-manuscript-census.json` | `86bda14f2f88335dfa4fd3fdb10f693ab134537e` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | — | created by the execution |

**No manuscript file is written, no `ROADMAP` row is written, and no file of act 19's is written.**
A difference in any of the three pinned blobs above is recorded in the result note as a discrepancy,
and the freeze is not repaired.

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**The `§A.37` justification, stated beneath it.** `AGENTS.md` lines 697–700, quoted above, fix the
execution's base as the merge commit of *this* control-plane pull request: the execution branches
from exactly that commit and from nothing else. So the base is fixed the moment this file merges,
and whatever sibling lanes have landed in `main` by then is a fact about the base's tree and not a
fact about this round's inputs. **Sibling results present at the base are not inputs.** The
start-state table above is the complete list of what this round consumes, and a file that is present
at the base and absent from that table is read by nothing in this round.

**Why this matters here, concretely, and with one addition peculiar to act 20.** Sibling lanes are
drafting and executing in parallel with this freeze, and some will merge into `main` before this
round's execution begins. This freeze is written against `0840e37` alone and consumes nothing from
any of them. **And the addition: act 19's execution branch `claude/act-19-execution` is not in the
start-state table and is not an input.** It is preserved evidence and it is readable — the execution
may read it to understand what went wrong — but its proofs are research material. Act 20 may not
cite them as settled, may not import them, may not adapt them under a new name and may not count
them as discharging any obligation of this round. **Anything act 20 needs, act 20's execution proves
under act 20's own freeze**, which is what act 19's closure at its lines 108–110 requires of every
successor.

## Source scoping, carried from acts 13 through 19

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why act 20 exists, and what act 19 left in front of it

Act 19 asked how rigid the class of cross-time laws is. **Its control plane was valid and its
execution was closed uncertified**, on two independent grounds recorded in the closure: the rung it
rewrote no longer stated commutation with two named transformation laws but orbit preservation, and
the rewrite followed pen-and-paper reasoning about a carrier relabelling's lift that arrived before
the rung was rewritten and pointed in the direction the rewrite went.

**The exposed problem is conceptual and not clerical, and act 20 exists for the conceptual part.**
"Gauge-natural" was standing in for three different conditions. Prose does not separate them; the
closure's table does. Until they are separated in the kernel and the carrier relabelling is
classified against them, any rigidity ladder carrying a naturality rung is carrying a rung whose
content nobody has fixed — and, as the closure puts it at its lines 133–137, the difference between
the three rows is the difference between a rigidity verdict that means something and one that does
not.

**Act 20 is therefore convened to be narrow, and the narrowness is the point.** It settles the
mathematics. It does not use the mathematics.

### What act 20 consumes, and at what strength

These are consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**,
and a merged statement is not enlarged by being consumed.

1. **Act 12's `LeftFibreGroup`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram` and
   `AdmissibleDilationAt`**, and act 11's `StrongAnchorStabilizer`, `WeakAnchorStabilizer`,
   `GaugeRelated` and `CoherentLift`. Each is consumed and **none is restated**.
2. **Act 12's two transformation laws**, `fibreGram_left_mul` and `fibreGram_mul_weak_apply`, at
   their own strengths and at the coordinates quoted above. They are the laws the three notions are
   stated against and they are what the round's intertwining target must be read against.
3. **Act 12's `left_preserves_admissible`, `weak_mul`, `gramPhaseEquiv_of_twoSided`,
   `twoSidedRelated_iff` and `sh1_necessity`/`sh1_sufficiency`/`sh1_shape`**, as the merged supply
   for any admissibility obligation act 20's constructions incur.
4. **Act 19's frozen `ΦP`**, quoted above at lines 912–914 of act 19's control plane, as the
   **statement** of the orbit-level transition act 20's lift is a lift of. It is consumed as a frozen
   definition from a valid, unwithdrawn control plane, and **not** as a result: act 19 certified
   nothing about it, and act 20 proves from scratch whatever it needs about it.
5. **Act 19's closure**, as the account of the problem. It is prose on certified `main`, it is
   consumed as such, and it certifies no theorem. In particular the closure's report at its lines
   71–80 that an execution had reasoned that the relabelling's lift "is a reindexing rather than a
   left multiplication" is a **record of a disclosure** and not a kernel result. **Act 20's execution
   proves the defining property of whatever lift it builds, in the kernel, under this freeze**, and
   may not treat that sentence as discharging anything.

### What the merged record supplies about naturality, and what it does not

| question | what the merged record says | label |
| --- | --- | --- |
| how a left in-fibre move acts on the fibre-Gram data | it is invisible: the data is unchanged | act 12's `fibreGram_left_mul` |
| how a weak right gauge at the anchor acts on it | by conjugation by the anchored phases, entrywise | act 12's `fibreGram_mul_weak_apply` |
| what the per-slice classes are | act 12's classification, with the rank bound inside `RealizableGram` | act 12's `SH1`, `TG2` |
| whether a transition descends to classes | for act 18's generator law, yes, discharged at orbit level | act 18's `LC3` descent |
| **what "the transition commutes with those laws" means formally** | **nothing on the record** | — |
| **whether the carrier relabelling has a lift satisfying any of the three notions** | **nothing on the record** | — |
| **whether the per-input existential is weaker than the fixed-`α` form** | **nothing on the record** | — |

**The last three rows are act 20's subject.** The freeze records, as its own bounded reading and not
as a finding, that at this base `git grep` over the tree returns no declaration named for, or stating,
strict equivariance, twisted equivariance or orbit preservation of any lift of any transition. Where
the record is silent the finding is that it is silent — and act 20's finding about the record is
whatever the execution's own reading records, not this paragraph.

## The question, FROZEN

> **What does it mean for a representative-level lift to be "gauge-natural", and which of the three
> notions does the carrier relabelling's lift satisfy?**

**Act 20 answers that and stops.** It does not ask how rigid any class of laws is, does not ask
whether any law propagates, and does not ask what a naturality condition ought to require of a
candidate in a later round.

## The strength of the ask, FROZEN

**The ask is a CLASSIFICATION OF ONE NAMED LIFT AGAINST THREE NAMED NOTIONS, together with the
implications between the notions that the round can prove.** The round asks: what are the three
notions, formally; how do they imply one another; does the carrier relabelling admit a
representative-level lift at all; if it does, is there a single map on the gauge data that
intertwines exactly with it; is that map the identity; is the lift strictly natural; and is the
per-input existential formulation strictly weaker than the fixed-map formulation.

**Why a classification and not the stronger asks, recorded as a reason.** A "which notion should a
naturality condition impose" ask is a **normative** question and is the owner's, not a round's; it
depends on the mathematics act 20 settles and on considerations act 20 has no standing to weigh. A
"classify every lift of every orbit-level transition" ask would quantify over a space nothing on the
record bounds. **One named lift, three named notions, and the implications between them is what the
round can honestly attempt**, and it is what the outcome labels below are calibrated to.

**The ask does not narrow what may be reported.** Every outcome label below is **preregistered as
reachable, each at the full evidence bar frozen for it**, and the negative and UNDECIDED routes carry
the same bar as the positive ones. A result outside the frozen scope is recorded as an observation
and not executed. **The scope is fixed here, before any construction.**

## The scope edges, stated as NON-DOINGS in terms

**These are frozen as non-doings and an execution that does any of them has left the round.** They
are repeated in the non-doings section and in the forbidden sentences, because each is a thing a
capable execution would drift into if the freeze were silent.

1. **Act 20 freezes no condition ladder and runs none.** No rung, no ladder, no conjunction of rungs,
   no `LadderConds` or any analogue of it, appears in this round's module or result note.
2. **Act 20 runs no survivor census and counts no survivors.** It tests no transition family against
   any condition set, and it reports no count of anything that survives anything.
3. **Act 20 reports no rigidity headline.** The labels `L-RIGID`, `L-FAMILY` and `L-WIDE` are act
   19's, they belong to act 19's frozen ladder, and **no artifact of act 20 reports any of them, in
   any paraphrase, in any table cell, or as a parenthetical**.
4. **Act 20 does not run the same-initial-orbit discriminating test.** Act 19's `SIOP` is not stated,
   not attempted, not witnessed and not refuted here, and no statement of act 20 bears on it.
5. **Act 20 does not choose which condition a later round's naturality rung ought to impose.** This is
   the sharpest edge of the round and it is the one the closure draws. Act 20 settles the mathematics
   that choice depends on. **The choice is the owner's, and it goes into act 21's preregistration.**
6. **Act 20 adopts and pre-commits no part of act 21's ladder.** It names no rung of it, proposes
   none, rates none, and orders none.

### Act 21 is a fresh rigidity round, and is written after act 20 lands

**Act 21 is a fresh rigidity round with its own freeze, written only after act 20 is merged, pinned
and reviewed.** It is not a continuation of act 19's execution, not a re-run of act 19 with one rung
edited, and not a resumption of anything. Nothing in act 20 — no label, no theorem, no
recommendation, no observation — is a commitment about act 21's ladder, its quotient list, its
candidate list or its headline. **Whatever act 21 imposes as its naturality condition, it imposes in
its own control plane, with its own reasons, and it may impose a condition act 20 classified as
failing, as holding, or as undecided.** Act 20's merged result is an input to that decision and is
not the decision.

## The objects, FROZEN

Throughout, `V` and `A` are finite types with decidable equality, `a₀ : A` the anchor, `Γ : Matrix V
V ℝ` a visible slice, `U : Matrix (V × A) (V × A) ℂ` a dilation, and the following are consumed
**unmodified**, at their own strengths: `AdmissibleDilationAt`, `readback`, `readback_relabel`,
`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `GaugeRelated`, `CoherentLift`, `LeftFibreGroup`,
`TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`,
`fibreGram_diag`, `fibreGram_diag_of_admissible`, `fibreGram_posSemidef`, `fibreGram_rank_le`,
`sum_fibreGram`, `fibreGram_left_mul`, `mul_weak_anchor_col`, `fibreGram_mul_weak_apply`,
`left_mul_submatrix`, `left_block_unitary`, `left_preserves_admissible`, `one_leftFibreGroup`,
`weak_mul`, `strong_mem_weak`, `weak_anchor_coeff_norm_one`, `gramPhaseEquiv_of_twoSided`,
`twoSidedRelated_iff`, `sh1_necessity`, `sh1_sufficiency` and `sh1_shape`.

**Act 7's boundary is carried at every use of the visible family**, exactly as acts 11 through 19
carry it: act 7's `D4b` came back **negative** — Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V` — and the readback is the repository's own,
frozen by act 7's readback amendment. Every statement in this round about what is visible is a
statement under that convention, said at each use rather than once in a footnote.

### The gauge classes the notions are stated against, named once

**Two classes, on two sides, and the round never merges them.**

- **The left class** is act 12's `LeftFibreGroup`, acting by `U ↦ L * U`. It is anchor-independent.
- **The right class** is act 11's `WeakAnchorStabilizer a₀`, acting by `U ↦ U * K`. It carries the
  anchor, and act 11's `StrongAnchorStabilizer a₀` sits inside it with all coefficients `1`
  (`strong_mem_weak`), so the strong right gauge is the special case of the weak one in which the
  anchored phases are trivial. **The round states its notions against the weak class and reports the
  strong case as the special case it is**, and it does not state a separate notion for the strong
  class.

**Every notion below is a conjunction of a left clause and a right clause**, and every verdict of
this round names which side it is about. A verdict reached on one side is **not** a verdict on the
other, and the result note reports the two separately wherever they can differ.

### The carrier relabelling and the transition it induces, FROZEN

`σ : Equiv.Perm V` is a permutation of the visible carrier under which the visible slice is
invariant, `Γ (σ i) (σ j) = Γ i j`. The orbit-level transition it induces is act 19's frozen `ΦP`,
carried here in act 19's own wording and written `Φ_σ`:

> `Φ_σ G i = (G (σ i)) ∘ σ`, the simultaneous relabelling of the fibre index and of both matrix
> indices by `σ`; entrywise, `Φ_σ G i j k = G (σ i) (σ j) (σ k)`.

**`σ` is chosen before any lift exists and consults no lift.** Nothing in this round requires `σ` to
be canonical in `Γ`, and nothing in this round asserts that `Φ_σ` propagates, descends, satisfies any
condition of any ladder, or is a law of anything. **Act 20 uses `Φ_σ` as the transition whose
representative-level lift it constructs, and for nothing else.**

## The three notions, FROZEN in this wording

**Three `Prop`s, frozen here, in this wording, before any lift is constructed and before any
classification is attempted.** `Ψ : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ` throughout.

### `N-STRICT` — strict equivariance

> **`N-STRICT`.** `StrictNatural a₀ Ψ` holds iff
> `(∀ L U, LeftFibreGroup L → Ψ (L * U) = L * Ψ U)` **and**
> `(∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * K)`.
>
> The lift commutes with **each gauge element itself**, on both sides. This is the closure's first
> row.

### `N-TWIST` — twisted equivariance, for ONE FIXED map

> **`N-TWIST`.** `TwistedNatural a₀ αL αR Ψ` holds, for maps `αL` and `αR` on dilations **fixed
> before the quantifier over inputs**, iff
> `(∀ L, LeftFibreGroup L → LeftFibreGroup (αL L))` **and**
> `(∀ K, WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR K))` **and**
> `(∀ L U, LeftFibreGroup L → Ψ (L * U) = αL L * Ψ U)` **and**
> `(∀ U K, WeakAnchorStabilizer a₀ K → Ψ (U * K) = Ψ U * αR K)`.
>
> The lift commutes **up to a fixed induced map on the class**, the same map at every input. This is
> the closure's second row.

**Two conjuncts of `N-TWIST` are closure conditions and they are load-bearing, not bookkeeping.**
Without `LeftFibreGroup (αL L)` and `WeakAnchorStabilizer a₀ (αR K)`, `αL` and `αR` could carry
gauge elements out of their classes, and the twisted form would then assert less than orbit
preservation rather than more. **They are also exactly what makes the implication to `N-ORBIT`
valid**, and the freeze says so here rather than letting the proof discover it. The maps are fixed
**before** the quantifier over inputs: `∃ αL αR, ∀ L U, …` and never `∀ L U, ∃ …`, and the order of
those quantifiers is the whole difference between this notion and the next.

### `N-ORBIT` — orbit preservation, the unrestricted per-input existential

> **`N-ORBIT`.** `OrbitNatural a₀ Ψ` holds iff
> `(∀ L U, LeftFibreGroup L → ∃ L', LeftFibreGroup L' ∧ Ψ (L * U) = L' * Ψ U)` **and**
> `(∀ U K, WeakAnchorStabilizer a₀ K → ∃ K', WeakAnchorStabilizer a₀ K' ∧ Ψ (U * K) = Ψ U * K')`.
>
> The output stays **somewhere in the gauge orbit**, with nothing fixing which element, and with the
> witness permitted to depend on the input. This is the closure's third row.

**`N-ORBIT` is stated here in the exact shape act 19's execution committed at `52b64009`**, and that
is deliberate. The round's fifth target asks whether this shape is strictly weaker than `N-TWIST`,
and asking it of a paraphrase would answer a different question. **Stating it is not endorsing it**:
`N-ORBIT` is named as an object of test, the closure records that it should not be called
commutation, and act 20 neither adopts it nor rejects it.

## The six targets, FROZEN

Six targets, `RNT1` through `RNT6`. Each names what settles it, what evidence counts, and what it
does **not** settle. **The list is closed at this freeze**, and a seventh question discovered during
execution is recorded as an observation and not executed.

### `RNT1` — the three notions, and the implication chain where it is valid

**The statement.** The three `Prop`s above are stated in the module in this file's wording, and the
implications between them are proved where they hold:

> **`RNT1` (a).** `StrictNatural a₀ Ψ → TwistedNatural a₀ id id Ψ`.
> **`RNT1` (b).** `TwistedNatural a₀ αL αR Ψ → OrbitNatural a₀ Ψ`, for every `αL`, `αR`.

**What settles it.** A Lean theorem at evidence level 2 for each part.

**The validity boundary, stated in advance.** Part (b) is valid **because** `N-TWIST` carries its two
closure conjuncts: the witnesses are `L' = αL L` and `K' = αR K`, and their membership in the classes
is exactly what those conjuncts supply. **The execution states where each conjunct is used**, so that
a reader can see the chain is not free. Part (a) is the special case `αL = αR = id`, whose closure
conjuncts are immediate.

**What `RNT1` does NOT establish.** It establishes **no converse**. That `N-ORBIT` does not imply
`N-TWIST` is `RNT5`'s question and is not settled here; that `N-TWIST` does not imply `N-STRICT` is
not settled here either, in general or for any particular lift. **A chain of implications is not a
chain of strict implications**, and no artifact of this round reports one as the other.

### `RNT2` — the representative-level lift `Ψ_σ`

**The statement.** A single top-level `Ψ_σ` is defined, and it is proved to be a lift of `Φ_σ`:

> **`RNT2` (a), the lifting property.** For every `U` admissible for `Γ` at `a₀`,
> `FibreGram a₀ (Ψ_σ U) = Φ_σ (FibreGram a₀ U)`.
> **`RNT2` (b), admissibility.** For every `U` admissible for `Γ` at `a₀` with `Γ` invariant under
> `σ`, `Ψ_σ U` is admissible for `Γ` at `a₀`.

**What settles it.** A Lean theorem at evidence level 2 for each part, over the `Ψ_σ` the execution
defines.

**The freeze fixes the obligation and NOT the formula, deliberately, and the reason is recorded.**
This freeze states what `Ψ_σ` must satisfy and leaves the construction to the execution. Writing a
formula here would be writing the round's first finding into its own control plane: the value of the
induced map, and therefore the answer to `RNT4`, is determined by the formula chosen. **The freeze
declines to determine it.** What the freeze does fix is that there is **one** `Ψ_σ`, named by one
declaration, and that `RNT3` and `RNT4` are verdicts about **that** declaration.

**What `RNT2` does NOT establish.** It does not establish that `Ψ_σ` is the only lift of `Φ_σ`, that
it is canonical, or that it is in any sense the natural one. **It is a lift, named, with its lifting
property proved**, and every later verdict of this round is a verdict about it and about no other
lift. Nor does it establish anything about `Φ_σ` beyond the two parts stated: no descent claim, no
propagation claim, no membership in any class, no verdict on any condition.

### `RNT3` — the induced map `α_σ` and the EXACT intertwining law

**The statement.** Whether there are maps `αL_σ` and `αR_σ`, **independent of `U`**, with

> `∀ L U, LeftFibreGroup L → Ψ_σ (L * U) = αL_σ L * Ψ_σ U`, together with
> `∀ L, LeftFibreGroup L → LeftFibreGroup (αL_σ L)`;
>
> `∀ U K, WeakAnchorStabilizer a₀ K → Ψ_σ (U * K) = Ψ_σ U * αR_σ K`, together with
> `∀ K, WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR_σ K)`;
>
> that is, whether `TwistedNatural a₀ αL_σ αR_σ Ψ_σ` holds for maps the execution exhibits.

**What settles it.** For the positive outcome, the two maps defined as top-level declarations and the
four conjuncts proved in the kernel at evidence level 2 — **an equality of matrices, universally
quantified over the gauge element and over the dilation, and not an existential over the output.**
For the intermediate outcome, `OrbitNatural a₀ Ψ_σ` proved at evidence level 2 with the exact law not
reached and the obstruction named. For UNDECIDED, the recorded statement with the obstruction named.

**"Not merely `∃ g'`" is the content of this target, and the freeze says so in terms.** An
existential over the output, witnessed input by input, is `N-ORBIT` and is the weaker statement whose
weakness act 19 closed over. **`RNT3`'s positive outcome is earned only by exhibited maps and
universally quantified equalities**, and a proof that produces a witness per input earns
`LAW-ORBIT-ONLY` and not `LAW-EXACT`, however the result note would prefer to phrase it.

**Both sides are reported separately.** The left clause and the right clause are proved and reported
apart, and the positive outcome requires both. Where one side lands and the other does not, the
result note says which, and `RNT3` is reported at the weaker of the two.

### `RNT4` — whether `α_σ` is the identity, and whether `Ψ_σ` is strictly natural

**Two parts, and they are NOT the same question.** This is the target most likely to be reported
sloppily and the freeze separates it now.

> **`RNT4` (a).** Is `αL_σ = id` on the left class, and is `αR_σ = id` on the right class? Decided
> for each side separately, at evidence level 2 — for the affirmative by a universal kernel proof,
> for the negative by an exhibited gauge element at which the map differs from it, with the
> differing entry named.
> **`RNT4` (b).** Does `StrictNatural a₀ Ψ_σ` hold? Decided at evidence level 2 — for the
> affirmative by a universal kernel proof of both clauses, for the negative by an exhibited pair with
> `Ψ_σ (L * U) ≠ L * Ψ_σ U` or `Ψ_σ (U * K) ≠ Ψ_σ U * K`, certified as an inequality at a named
> entry.

**The logical relation between (a) and (b), frozen before either is known, in both directions.**

- **`α_σ = id` implies strict naturality.** If `RNT3` landed exactly and the induced maps are the
  identity, `N-STRICT` follows immediately, and that is the whole of what "strict equivariance is
  the special case" means.
- **`α_σ ≠ id` does NOT imply that `Ψ_σ` fails strict naturality.** A lift can intertwine with a
  non-identity map and also commute with each element — nothing in the definitions forbids it, and
  the execution may not infer one from the other. **Part (b)'s negative is earned only by its own
  exhibited pair**, and an execution that reports "`α_σ ≠ id`, therefore not strictly natural" has
  reported a non-sequitur. This is a named hazard below and a forbidden sentence below.

**The scope of both parts is the lift `RNT2` built, and the freeze fixes that now.** Neither part is
a statement about every lift of `Φ_σ`. **"No lift of `Φ_σ` is strictly natural" is a universal
statement over all lifts, it is NOT this round's target, and no outcome of this round earns it.**
That question is named here as open, is assigned to no round, and is recorded so that a reader of
act 20's result cannot mistake a verdict about one named declaration for a verdict about a class.

### `RNT5` — is the per-input existential STRICTLY weaker than the fixed-map form?

**The statement.** `RNT1` (b) gives one direction. The question is the other:

> **`RNT5`.** Is there a `Ψ` with `OrbitNatural a₀ Ψ` and **no** pair of maps making
> `TwistedNatural` hold — that is, with `¬ ∃ αL αR, TwistedNatural a₀ αL αR Ψ`? Or, at the
> configuration named, does every `OrbitNatural` lift admit such a pair?

**What settles it.**

- For the separation: an **exhibited** `Ψ`, pinned by equations, at evidence level 2, with
  `OrbitNatural a₀ Ψ` proved and the non-existence of the pair proved. Together with `RNT1` (b) this
  is the statement that the implication is strict.
- For the collapse: a **universal** kernel proof at evidence level 2, at the configuration named,
  that `OrbitNatural a₀ Ψ → ∃ αL αR, TwistedNatural a₀ αL αR Ψ`.
- For UNDECIDED: the recorded statement that neither was reached, with the obstruction named — which
  direction, which step, and what would settle it.

**The UNDECIDED route is preregistered here, explicitly, and it is the route an execution takes when
it cannot find a counterexample.** Act 19 preregistered the same shape for its own hard rungs and for
its `L5` construction, and act 20 carries the device for the same reason: so that a round which
cannot separate two notions **reports that it could not** rather than eliding the distinction.
**Searching and not finding earns nothing**, and in particular the absence of a counterexample is
**not** evidence that the two notions coincide. An execution that writes "no counterexample was
found, so the two formulations agree" has committed the exact error the target exists to prevent.

**What `RNT5` does NOT establish, in either outcome.** A separation at one configuration is not a
separation everywhere, and a collapse at one configuration is not a collapse everywhere. The result
note states the configuration at which whatever it proves was proved, and claims nothing outside it.
Nor does either outcome say which notion a condition ought to use.

### `RNT6` — the classification, reported and not applied

**The statement.** Which of the three notions `Ψ_σ` satisfies, composed from `RNT3` and `RNT4`, with
the separation status from `RNT5` carried beside it, reported in the frozen wording of the status
rule below and **with no recommendation attached**.

**What settles it.** Nothing beyond `RNT3`, `RNT4` and `RNT5`: `RNT6` is the composition of their
labels and introduces no new theorem, no new definition and no new claim.

**What `RNT6` is forbidden to contain.** No sentence choosing a notion for a later round; no sentence
rating the three notions against one another for suitability, physical reasonableness, strength of
result, or any other criterion; no rung, ladder or condition; no rigidity label; no recommendation,
suggestion, preference or "the natural choice would be". **The classification is the product. The
choice is the owner's.**

## The outcome labels, per target, FROZEN

**Every label below is preregistered as reachable at the full evidence bar frozen for it.** No label
is a fallback, none is a shortfall, and UNDECIDED is a live outcome for every target.

| target | labels |
| --- | --- |
| `RNT1` | `CHAIN-PROVED` — both implications proved · `CHAIN-PARTIAL` — one proved, the other not, with which named · `CHAIN-UNDECIDED` — neither reached, with the obstruction named |
| `RNT2` | `LIFT-BUILT` — both parts proved of one named declaration · `LIFT-PARTIAL` — the lifting property proved and admissibility not, or the reverse · `LIFT-UNDECIDED` — no lift constructed, with the obstruction named |
| `RNT3` | `LAW-EXACT` — the two maps exhibited and all four conjuncts proved, both sides · `LAW-EXACT-ONE-SIDE` — as above on one side only, with the side named · `LAW-ORBIT-ONLY` — `OrbitNatural a₀ Ψ_σ` proved and no exact law reached, with the obstruction named · `LAW-UNDECIDED` — neither reached |
| `RNT4` (a) | `ALPHA-TRIVIAL` — the induced map is the identity, proved universally, with the side named · `ALPHA-NONTRIVIAL` — an exhibited gauge element at which it is not, with the entry named · `ALPHA-UNDECIDED` |
| `RNT4` (b) | `STRICT-YES` — `StrictNatural a₀ Ψ_σ` proved universally · `STRICT-NO` — an exhibited pair with the two sides unequal at a named entry · `STRICT-UNDECIDED` |
| `RNT5` | `SEP-STRICT` — the counterexample exhibited, so the implication is strict · `SEP-COLLAPSE` — the converse proved universally at the configuration named · `SEP-UNDECIDED` |
| `RNT6` | `CLASS-STRICT` · `CLASS-TWISTED-NOT-STRICT` · `CLASS-TWISTED-AND-STRICT` · `CLASS-ORBIT-ONLY` · `CLASS-UNDECIDED` |

**`RNT6`'s labels are composed and never chosen.** `CLASS-STRICT` requires `STRICT-YES` with
`ALPHA-TRIVIAL`; `CLASS-TWISTED-NOT-STRICT` requires `LAW-EXACT` with `ALPHA-NONTRIVIAL` **and**
`STRICT-NO`; `CLASS-TWISTED-AND-STRICT` requires `LAW-EXACT` with `ALPHA-NONTRIVIAL` and
`STRICT-YES`, which is consistent and is preregistered here precisely because a careless round would
not think to allow for it; `CLASS-ORBIT-ONLY` requires `LAW-ORBIT-ONLY`; and any other combination,
including any UNDECIDED among the inputs, is `CLASS-UNDECIDED` with the obstruction named.

**`CLASS-TWISTED-NOT-STRICT` is not the expected outcome and this freeze does not treat it as one.**
It is listed third in the composition rule above because it needs the most inputs, not because it is
the most likely. Every one of the five labels carries the same evidence bar and the same frozen
post-round sentence discipline.

## The countercontrols

**A negative result is reportable because its shape was fixed before the search.** For each target
the freeze states what a negative answer looks like concretely and what evidence earns it.

**Evidence that earns any countercontrol**: a Lean theorem at evidence level 2 whose statement pins
the objects by equations, discharges admissibility from merged results where admissibility is needed,
and certifies any separating quantity at a named index. **Searching and not finding earns nothing.**

| target | the countercontrol this freeze names |
| --- | --- |
| `RNT1` (a) | none is available and none is named: `N-STRICT` with `αL = αR = id` is `N-TWIST` by unfolding, and a failure here would be a defect in the statement of the notions rather than a finding. Were it to fail, the round reports `CHAIN-PARTIAL` and names the definition at fault |
| `RNT1` (b) | **a `Ψ` twisted by maps that leave the classes** — which the closure conjuncts of `N-TWIST` forbid, so the countercontrol is a check that those conjuncts are used and not a candidate. The execution records where each is used; if the implication is proved **without** using them, that is a defect of the statement of `N-TWIST` and is reported as one |
| `RNT2` | **a construction that lifts `Φ_σ` but leaves admissibility**: a `Ψ_σ` with the lifting property whose output fails `AdmissibleDilationAt` for some admissible input. Reported `LIFT-PARTIAL` with the failing conjunct named |
| `RNT3` | **the input-dependence obstruction**: any step at which a putative `αL_σ` or `αR_σ` cannot be written without mentioning `U`. This is the concrete shape of `LAW-ORBIT-ONLY`, and the execution names the step rather than reporting a weaker theorem as a stronger one |
| `RNT4` (a) | **one gauge element suffices, in either direction.** The negative is an exhibited `L` with `αL_σ L ≠ L`, or an exhibited `K` with `αR_σ K ≠ K`, certified as a matrix inequality at a named entry. **No search is a substitute** |
| `RNT4` (b) | **one pair suffices**: an exhibited `(L, U)` or `(U, K)` with the two sides unequal at a named entry. **`ALPHA-NONTRIVIAL` is NOT a countercontrol for (b)** and may not be offered as one |
| `RNT5` | **named and expected hard**: a `Ψ` satisfying the per-input existential admitting no fixed pair. The freeze names no construction and rates the target accordingly; **`SEP-UNDECIDED` with the obstruction named is an allowed outcome and is not a shortfall** |
| `RNT6` | not a target with a countercontrol: it is the composition of the labels above, and its only failure mode is a composition rule not honoured, which the status rule fixes byte by byte |

**One configuration note, carried from act 18 and act 19 and recorded again.** Act 12's `|A| = 1` is
the strongest case for the per-slice statements and is not degenerate there, and it is **not
automatically the right case** for a statement about the gauge classes: at `|A| = 1` the left class
`LeftFibreGroup` is the diagonal phases on the fibres, which is a proper part of what it is at `|A| ≥
2`. **Where a verdict of this round is reached at `|A| = 1` the result note says so**, and it does not
report a verdict reached there as a verdict at every `|A|`. Where a verdict needs `|A| ≥ 2` the
execution records the value used.

## The evidence rule, FROZEN

1. Every mathematical target of this round — `RNT1` through `RNT5` — is settled by a **kernel-checked
   Lean theorem at evidence level 2**, or by a recorded UNDECIDED with the obstruction named
   specifically: which target, which side, which conjunct, which step, and what would settle it.
2. Where a claim is about the **record** rather than about mathematics — what the merged tree does or
   does not already contain — the evidence is a **verbatim quotation** from a pinned blob with its
   file and line coordinate, or an explicit recorded statement that **the passage sought does not
   exist** on the record searched, with the search **named and bounded**.
3. **Reconstructive inference is forbidden as a finding.** A determination of the form "the record
   must contain X, because otherwise Y would not have been written" may appear only in a clearly
   labelled analysis paragraph that states it is not evidence and that no target rests on it. **Where
   the record is silent, the finding is that it is silent** — not that the thing sought is false, and
   not that it is true.
4. **Searching and not finding is never a settling outcome.** No label of this round is earned by an
   absence: `ALPHA-TRIVIAL` is not earned by failing to find a gauge element where the map differs,
   `STRICT-YES` is not earned by failing to find a failing pair, and `SEP-COLLAPSE` is not earned by
   failing to find a counterexample.
5. **A proof on act 19's execution branch is not evidence.** It may be read; it may not be cited,
   imported, adapted or counted. Act 19's closure requires this of every successor at its lines
   108–110, and this round's result note states that it was honoured.

## The freeze ABSTAINS from two predictions, and records why

**This section exists because act 20's control plane is written by someone who has read act 12's
transformation laws, act 19's freeze and act 19's closure, and who is therefore in a position to form
a view about what `α_σ` is. The freeze withholds that view. The withholding is deliberate, it is
recorded here rather than concealed, and the reason is the round's own subject.**

**The reason.** `RNT3` and `RNT4` are the round's discriminating questions. A control plane that
recorded a predicted value for `α_σ`, or a predicted answer to whether it is the identity, would hand
the execution the answer in the first document it reads, before it has stated a single definition.
The ordering obligation below would then be enforcing a boundary that the freeze had already crossed
on the execution's behalf. **Act 19 closed because candidate-informed reasoning arrived before a
definition was fixed. A freeze that writes that reasoning into itself has not avoided the failure; it
has moved it one document earlier.**

**What is withheld, exactly.** The freeze records no predicted value for `αL_σ` or `αR_σ`, no
predicted answer to `RNT4` (a) or (b), and no predicted `RNT6` label. It records no derivation, no
sketch, no hint and no "one would expect". The prediction table below carries **`abstained`** in
those rows, with this section as the reason.

**What is not withheld.** Everything the freeze needs to be checkable is here: the three notions in
full, the obligations on `Ψ_σ`, the evidence bars, every outcome label at equal standing, and the
countercontrols. Predictions for the targets that are **not** discriminating — `RNT1`, `RNT2` and
`RNT5` — are recorded with their signs, strengths and reasons in the ordinary way.

**And the cost is recorded rather than hidden.** An abstention is weaker preregistration than a
prediction: a freeze that predicts and is wrong has learned something, and a freeze that abstains has
not put itself at risk on that point. **The freeze accepts that cost** on `RNT3` and `RNT4` and on
nothing else, because on those two targets the cost of the alternative is the round.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `RNT1` (a) | **positive** | **high** | With `αL = αR = id` the two closure conjuncts are immediate and the two intertwining conjuncts are the hypotheses unchanged. No merged result is consumed and no construction is required. |
| `RNT1` (b) | **positive** | **high** | The witnesses are `αL L` and `αR K`, and their class membership is exactly what `N-TWIST`'s closure conjuncts supply. The rating is high because the proof is an unfolding; the freeze rates the **statement** of `N-TWIST` as the place where care is needed, not the proof. |
| `RNT2` (a) | **positive** | **medium** | A lift of `Φ_σ` is what act 19's freeze assumed existed when it wrote `L4n`, and act 19's closure records a disclosure that one exists in reindexing form. **Neither is a certified theorem**, so the medium rating is for the kernel work of exhibiting one and discharging the `FibreGram` identity, which no merged result states. |
| `RNT2` (b) | **positive** | **medium** | Admissibility of the output needs the invariance of `Γ` under `σ` and act 12's merged `sh1`-side results, and the bookkeeping over `AdmissibleDilationAt` is real work. **`LIFT-PARTIAL` is an allowed outcome and is not a shortfall.** |
| `RNT3` | **abstained** | — | See the abstention section. Both `LAW-EXACT` and `LAW-ORBIT-ONLY` are preregistered as reachable at the full evidence bar, and `LAW-UNDECIDED` with the obstruction named is allowed. |
| `RNT4` (a) | **abstained** | — | See the abstention section. `ALPHA-TRIVIAL` and `ALPHA-NONTRIVIAL` stand at equal standing, and `ALPHA-UNDECIDED` is allowed. |
| `RNT4` (b) | **abstained** | — | See the abstention section. `STRICT-YES` and `STRICT-NO` stand at equal standing, and `STRICT-UNDECIDED` is allowed. The freeze notes only that (b) is a separate question from (a) and must be earned separately, which is a statement about the logic and not a prediction about the answer. |
| `RNT5` | **not predicted**, with `SEP-UNDECIDED` named as the outcome the freeze expects | **low** | The freeze names no construction for a lift satisfying the per-input existential and admitting no fixed pair, and the merged record supplies none. The converse direction would need a universal statement over lifts that nothing on the record bounds. **`SEP-UNDECIDED` with the obstruction named is an allowed outcome and is the freeze's expectation; it is not a shortfall, and `SEP-STRICT` and `SEP-COLLAPSE` are both preregistered as reachable at full bar.** |
| `RNT6` | **abstained** | — | It is the composition of `RNT3`, `RNT4` and `RNT5`, on three of which the freeze abstains. All five labels stand at equal standing. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

**What this table's shape says, stated plainly.** The freeze predicts, at high confidence, only the
two implications that hold by unfolding, and, at medium, that a lift can be built. **On the question
the round exists to answer it predicts nothing, on purpose.** The round is worth running because the
three notions are worth having in the kernel whichever way the classification falls; because
`RNT1`'s chain is a theorem either way; because a `LAW-ORBIT-ONLY` outcome would be as informative as
a `LAW-EXACT` one, telling a later round that the exact law is not available for this lift; and
because `RNT5`'s expected UNDECIDED is itself the finding that the record does not yet separate two
conditions it has been treating as one.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached. The
wording is fixed before the round runs so that no outcome can choose its own wording. **UNDECIDED is
a live preregistered outcome for every target and is not a failure**; where it is reached the frozen
sentence below is the report, with the obstruction named.

### The outcomes of `RNT1`

- **`CHAIN-PROVED`:**
  > Strict equivariance implies twisted equivariance with the identity as the induced map, and
  > twisted equivariance implies orbit preservation, both proved in the kernel at evidence level 2
  > over this freeze's wording of the three notions. **The second implication is valid because the
  > twisted notion carries its closure conjuncts**, and the proof names where each is used. **No
  > converse is established by either implication**: that orbit preservation does not imply the
  > twisted form is a separate question of this round, and that the twisted form does not imply the
  > strict form is not a statement of this round at all.
- **`CHAIN-PARTIAL`:**
  > One of the two implications is proved at evidence level 2 and the other is not, with which named
  > and the obstruction named specifically. Neither the unproved implication nor its converse is
  > claimed, and no sentence of this round treats a proved implication as a strict one.
- **`CHAIN-UNDECIDED`:**
  > Neither implication was reached, with the obstruction named specifically. The three notions are
  > stated in the kernel and are related by nothing this round proves.

### The outcomes of `RNT2`

- **`LIFT-BUILT`:**
  > A single representative-level map on dilations is exhibited, named by one declaration, and proved
  > at evidence level 2 to induce the carrier relabelling's transition on the fibre-Gram data and to
  > carry admissible dilations to admissible dilations at a visible slice invariant under the
  > relabelling. **This is a construction and not a uniqueness statement**: it does not say that this
  > is the only lift of that transition, does not say it is canonical, and does not say it is the
  > natural one. Every later verdict of this round is a verdict about this declaration.
- **`LIFT-PARTIAL`:**
  > One of the two parts is proved at evidence level 2 and the other is not, with which named and the
  > obstruction named specifically. The later targets are reported of the map as constructed, with
  > the undischarged part carried as an explicit hypothesis wherever it is needed, and the result
  > note says where.
- **`LIFT-UNDECIDED`:**
  > No representative-level lift of the relabelling's transition was constructed in the kernel, with
  > the obstruction named specifically. **The later targets are then reported UNDECIDED for want of
  > an object**, and the round claims nothing about the classification. The absence of a construction
  > is not a finding that none exists.

### The outcomes of `RNT3`

- **`LAW-EXACT`:**
  > Maps on the left and on the right gauge data are exhibited, independent of the dilation, and the
  > exact intertwining law is proved in the kernel at evidence level 2 on both sides: the lift of the
  > relabelling carries a gauge element on its input to the image of that element under the exhibited
  > map on its output, as a universally quantified equality of matrices and **not** as an existential
  > over the output. The exhibited maps carry each class into itself, and the four conjuncts are
  > reported separately. **This settles the law for the lift this round built**, at the configuration
  > named, and says nothing about any other lift of the same transition.
- **`LAW-EXACT-ONE-SIDE`:**
  > The exact intertwining law is proved on one side and not on the other, with the side named and
  > the obstruction on the other side named specifically. **A law on one side is not a law**, and the
  > round is reported at the weaker of the two throughout.
- **`LAW-ORBIT-ONLY`:**
  > The lift is proved to carry gauge elements to gauge elements input by input — orbit preservation
  > in this freeze's wording — and **no map independent of the dilation was exhibited**, with the
  > step at which input-dependence could not be removed named specifically. **This is the weaker of
  > the two statements and is reported as the weaker**, in this round's own terms: what is
  > established is that the output stays in the orbit, and nothing fixes which element. It is not a
  > finding that no such map exists.
- **`LAW-UNDECIDED`:**
  > Neither the exact law nor orbit preservation was reached in the kernel, with the obstruction
  > named specifically. Neither is claimed, and no sentence of this round treats the absence of a
  > proof as a decision.

### The outcomes of `RNT4`

- **`ALPHA-TRIVIAL`, for a named side:**
  > The induced map on the side named is the identity, proved universally in the kernel at evidence
  > level 2. **So on that side the lift is strictly equivariant as the special case of the twisted
  > form in which the induced map is the identity**, and that implication is this round's own first
  > target applied. This is a statement about the lift this round built and about the side named.
- **`ALPHA-NONTRIVIAL`, for a named side:**
  > A gauge element of the class named is exhibited at which the induced map is not the identity,
  > certified as a matrix inequality at a named entry, at evidence level 2. **This does NOT by itself
  > establish that the lift fails strict equivariance**, which is a separate question with its own
  > evidence bar, reported separately below. It is a statement about the induced map this round
  > exhibited, for the lift this round built, on the side named.
- **`ALPHA-UNDECIDED`, for a named side:**
  > Whether the induced map on the side named is the identity is undecided in this round, with the
  > obstruction named specifically. Neither label is claimed, and the absence of an exhibited
  > differing element is not a proof that the map is the identity.
- **`STRICT-YES`:**
  > The lift commutes with each gauge element itself, on both sides, proved universally in the kernel
  > at evidence level 2. **So the relabelling's lift is strictly natural** in this freeze's wording,
  > at the configuration named, for the lift this round built.
- **`STRICT-NO`:**
  > A gauge element and a dilation are exhibited for which the lift of the moved dilation and the
  > move of the lifted dilation are different matrices, certified as an inequality at a named entry,
  > at evidence level 2. **So the relabelling's lift is not strictly natural**, for the lift this
  > round built, at the configuration named. **This is not a statement that no lift of the
  > relabelling's transition is strictly natural**, which is a universal statement over lifts that
  > this round does not attempt and does not earn.
- **`STRICT-UNDECIDED`:**
  > Whether the lift is strictly natural is undecided in this round, with the obstruction named
  > specifically. Neither label is claimed. In particular a non-identity induced map is **not**
  > reported as a failure of strict naturality, and the absence of an exhibited failing pair is
  > **not** reported as strict naturality.

### The outcomes of `RNT5`

- **`SEP-STRICT`:**
  > A lift is exhibited that satisfies the per-input existential formulation and admits no pair of
  > maps making the fixed-map formulation hold, at evidence level 2, with the objects pinned by
  > equations. **Together with this round's implication from the fixed-map form to the existential
  > form, the implication is therefore strict**: the unrestricted existential formulation is strictly
  > weaker. This is a statement at the configuration named and is not a statement that the two
  > formulations differ at every configuration.
- **`SEP-COLLAPSE`:**
  > At the configuration named, every lift satisfying the per-input existential formulation admits a
  > pair of maps making the fixed-map formulation hold, proved universally in the kernel at evidence
  > level 2. **So at that configuration the two formulations coincide**, which is a statement about
  > that configuration and not about every configuration, and which does not make the two wordings
  > interchangeable in general.
- **`SEP-UNDECIDED`:**
  > Whether the unrestricted existential formulation is strictly weaker than the fixed-map
  > formulation is undecided in this round, with the obstruction named specifically — the direction,
  > the step, and what would settle it. **The two formulations are kept apart and are not conflated.**
  > **The absence of a counterexample is not a proof that they coincide**, and no sentence of this
  > round treats a failed search as an equivalence. A later round that wants the separation freezes
  > it.

### The outcomes of `RNT6`

- **`CLASS-STRICT`:**
  > The lift this round built is **strictly natural**: the induced map is the identity on both sides
  > and the lift commutes with each gauge element itself, both proved at evidence level 2.
- **`CLASS-TWISTED-NOT-STRICT`:**
  > The lift this round built is **twisted-natural and not strictly natural**: an exact intertwining
  > law holds with exhibited maps on both sides, at least one of those maps is not the identity at an
  > exhibited gauge element, and an exhibited pair witnesses the failure of strict equivariance —
  > each at evidence level 2 and each earned separately.
- **`CLASS-TWISTED-AND-STRICT`:**
  > The lift this round built is **twisted-natural with a non-identity induced map and also strictly
  > natural**: the exact law holds with exhibited maps, at least one of which is not the identity,
  > and the lift nevertheless commutes with each gauge element itself. **Both are proved and neither
  > is inferred from the other.**
- **`CLASS-ORBIT-ONLY`:**
  > What this round establishes for the lift it built is **orbit preservation** and not commutation:
  > the output stays in the gauge orbit, with the witness depending on the input, and no map
  > independent of the dilation was exhibited. **This is the weakest of the three notions and is
  > reported as such**, and it is not a finding that the stronger notions fail.
- **`CLASS-UNDECIDED`:**
  > The classification is recorded UNDECIDED, with the obstruction named specifically — the target,
  > the side, the step and what would settle it. **An UNDECIDED is a statement about this round and
  > about the record, and not about the question.**

**And every one of the five sentences above is followed, in the result note, by this one, in this
wording:**

> This is a classification of one named lift against three named notions. **It does not say which
> notion a later round's naturality condition ought to impose**, does not rate the three notions
> against one another, and does not open, adopt or pre-commit any part of a later round's ladder.
> That choice is the owner's and it is made in act 21's preregistration.

## The `P0` row is untouched, and the round appends nothing to it

**Act 20 changes nothing in `verification/ROADMAP.md`.** The `P0` row's label, its obligation cell and
its status text are read at the blob pinned above and are not written.

**The reason, recorded rather than assumed.** Acts 13 through 19 each appended a frozen post-round
sentence to `P0` because each settled something about the structure `P0` asks for: what the per-slice
classes are, what the trajectory set is, whether a cross-time law can propagate. **Act 20 settles
nothing of that kind.** What it settles is what a phrase in a round's control plane means and how one
named lift behaves under two merged transformation laws. A sentence appended to `P0` saying that a
programme has clarified its own vocabulary would be reporting apparatus as a finding about the
obligation, and would make the row harder to read rather than easier.

**So `P0` stays OPEN and two-part, its threading part is untouched, its trajectory part is untouched,
and no outcome of this round moves, bounds, narrows or widens either.** The obligation act 20
discharges is to the record of act 19 and to act 21's drafting, not to `P0`. **This is a narrowing
relative to every recent round of this programme and it is put to the owner as an open decision
before this freeze merges**, in the settlements section below.

## Classifying is not choosing, FROZEN

Acts 11 through 19 each carry the non-doing "names, endorses or excludes no selection principle".
**Act 20's analogue is sharper, because the thing act 20 could be misread as endorsing is not a law
but a condition.** The reconciliation is frozen here so that it cannot be improvised afterwards.

1. **Naming is for classifying.** The three notions are named as objects of test and for no other
   purpose. Naming one is not proposing it, not adopting it, not asserting that it is the right shape
   for any condition, and not asserting that the programme needs a naturality condition at all.
2. **A classification is a fact about an object.** That a named lift satisfies, or fails, a named
   notion is a fact about that lift. It is not an argument that the notion is the right condition,
   and it is not an argument that it is the wrong one.
3. **The round recommends nothing.** No outcome of this round recommends a notion, rates the notions
   against one another, or says which one a later round should use. Where the result note is tempted,
   the frozen sentence of the status rule is what it writes instead.
4. **The lists are closed at this freeze.** The execution states these three notions, builds one
   lift, and asks these six questions. A fourth notion, a second lift or a seventh question is
   recorded as an observation and not executed.

### The non-choice clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a classification could be read as a choice.** Each carriage opens with
one line naming where it is being carried, contiguous with the body, so that the carriages read as
distinguishable copies of one clause rather than as one paragraph pasted repeatedly — which is a
defect the repository's duplicate check exists to catch — and the naming line changes nothing about
the clause it introduces. Acts 15, 16, 17, 18 and 19 established this pattern and this round follows
it.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed post-round
sentences of the status rule, which carry the clause's substance in their own frozen wording and
cannot admit a quotation inside a quotation; and the bare list entries that do nothing but name a
notion among the three this round classifies against.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in for,
> constructs the carrier relabelling's representative-level lift, and determines which of the three
> that lift satisfies. **Classifying is not choosing.** No statement of this round says which notion
> a later round's naturality condition ought to impose, which notion is the physically right one, or
> which notion the programme needs: that choice is the owner's and it is made in act 21's
> preregistration, against act 20's merged result. **A classification is a fact about an object, not
> an argument for a condition.** No condition is adopted, no rung is written, no ladder is opened, no
> census is run, and no law, carrier or selection principle is named, endorsed or excluded here.

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"So `L4n` should require twisted equivariance", "the right condition is the strict one", or any
   sentence choosing a notion for a later round.** The choice is the owner's.
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in for,
   > constructs the carrier relabelling's representative-level lift, and determines which of the three
   > that lift satisfies. **Classifying is not choosing.** No statement of this round says which notion
   > a later round's naturality condition ought to impose, which notion is the physically right one, or
   > which notion the programme needs: that choice is the owner's and it is made in act 21's
   > preregistration, against act 20's merged result. **A classification is a fact about an object, not
   > an argument for a condition.** No condition is adopted, no rung is written, no ladder is opened, no
   > census is run, and no law, carrier or selection principle is named, endorsed or excluded here.
2. **"`α_σ` is not the identity, so the lift is not strictly natural."** A non-sequitur: the two are
   separate questions with separate evidence bars, and `RNT4` (b) is earned only by its own exhibited
   pair.
3. **"No lift of the relabelling is strictly natural", or any universal statement over lifts.** This
   round classifies one named declaration. A verdict about it is not a verdict about a class.
4. **"So the relabelling survives `L4n`", or "so it fails `L4n`", or any verdict about any rung of
   act 19's ladder.** Act 19's ladder is act 19's, its `L4n` is uncertified by act 19's own closure,
   and act 20 tests no rung.
5. **"`L-RIGID`", "`L-FAMILY`", "`L-WIDE`", "the class is rigid", "the class is wide", or any
   rigidity headline.** Act 20 reports none, in any form.
6. **"Two laws agree", "two laws diverge", or any same-initial-orbit statement.** Act 19's
   discriminating test is not run here.
7. **"The survivors are …", or any count of anything that survives anything.** No census is run.
8. **"The existential and the fixed-map forms are the same thing", said after a search that found no
   counterexample.** That is `SEP-UNDECIDED` reported as `SEP-COLLAPSE`, and it is the specific
   conflation this round exists to prevent.
9. **"Act 19 was wrong", "act 19's mathematics is false", or any sentence treating act 19's
   uncertified conclusions as refuted.** Act 19's closure fixes the register at its lines 8–10: the
   distinction is between refuted and uncertified, and act 20 keeps it.
10. **"Act 19's execution already proved this."** Its proofs are research material and no later round
    may cite them as settled.
11. **"Act 19's freeze is amended", "withdrawn", "corrected" or "superseded."** It is valid and
    unwithdrawn, and act 20 edits nothing in it.
12. **"This is Schrödinger evolution", "this is unitary evolution", or any statement that anything
    here is, resembles, approximates or points toward quantum evolution.** Out of scope, as it was for
    act 19, and for the same reason: this round has no standard against which resemblance could be
    measured.
13. **"`P0` is closed", "`P0`'s trajectory part is narrowed", or any statement about the `P0` row.**
    The round does not write to it and says nothing about it.
14. **Any statement about the threading, the cross-time representative, the relative evolution or the
    relative candidate.** Not asked here in either direction.
15. **Any statement about act 16's cancellation cell, act 18's `D`-axis, or act 14's four carriers.**
    None is this round's subject and no outcome bears on any of them.
16. **"Act 12's transformation laws are strengthened", or "act 12's classification is enlarged."**
    Both are consumed at merged strength. **A merged statement is not enlarged by being consumed.**
17. **"The condition list is exhaustive", or "these are the notions of naturality."** Three notions
    are frozen for classification, they are the three the closure names, and a fourth is neither
    imposed nor refuted by anything here.
18. **"The evolution is continuous", "smooth", "generated" or "one-parameter."** Nothing in this
    round's index type carries any of it.
19. **Any sentence about Track I**, or about Source B or Source C, on any axis.
20. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **The freeze answering its own question.** **This is the strongest hazard in the round**, and it
   is a hazard of the control plane and not of the execution. The specific failure guarded against is
   a freeze that records a predicted value for the induced map, a predicted answer to whether it is
   the identity, or a derivation of either — and thereby hands the execution the classification in
   the first document it reads. The abstention section is what closes it, and the abstention is
   recorded as a deliberate act with its cost stated.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 20 classifies. It formalizes the three notions the phrase "gauge-natural" was standing in for,
   > constructs the carrier relabelling's representative-level lift, and determines which of the three
   > that lift satisfies. **Classifying is not choosing.** No statement of this round says which notion
   > a later round's naturality condition ought to impose, which notion is the physically right one, or
   > which notion the programme needs: that choice is the owner's and it is made in act 21's
   > preregistration, against act 20's merged result. **A classification is a fact about an object, not
   > an argument for a condition.** No condition is adopted, no rung is written, no ladder is opened, no
   > census is run, and no law, carrier or selection principle is named, endorsed or excluded here.
2. **Reasoning to the answer without running anything.** Act 19's contamination arrived by
   pen-and-paper reasoning, which its attestation questions did not cover. **The definitions this
   round freezes materially determine the classification**: an executing agent that has written the
   lift has, in principle, everything needed to reason to the value of the induced map without
   compiling a line. **The commit boundary alone cannot carry this round's ordering obligation, and
   the freeze says so rather than pretending otherwise.** The third attestation question is what
   carries the rest, and the ordering obligation's rule that the induced maps may not appear before
   the discrimination commit is what makes the boundary checkable at all.
3. **A weaker theorem reported as a stronger one.** The specific failure guarded against is a proof
   that produces a gauge element per input, reported as an exact intertwining law. `LAW-ORBIT-ONLY`
   exists for exactly that result and is preregistered at full bar.
4. **A non-identity induced map reported as a failure of strict equivariance.** The specific failure
   guarded against is the inference in forbidden sentence 2. `RNT4` is split into two parts for it.
5. **A verdict about one lift reported as a verdict about every lift.** The specific failure guarded
   against is "the relabelling is not strictly natural" written where "the lift this round built is
   not strictly natural" is what was proved.
6. **A failed search reported as a collapse.** The specific failure guarded against is
   `SEP-UNDECIDED` written up as though the two formulations had been shown to agree. The evidence
   rule's clause 4 closes it.
7. **The round drifting into a rigidity round.** The specific failure guarded against is an execution
   that, having classified the lift, begins asking whether the relabelling survives a ladder. That
   has left this round's scope; what it finds is **recorded as an observation and not executed**.
8. **The round drifting into act 21's drafting.** The specific failure guarded against is a result
   note that ends with a recommendation. The status rule's closing sentence is what it writes
   instead.
9. **Citing act 19's execution branch.** The specific failure guarded against is a proof adapted from
   `claude/act-19-execution` under a new name and counted as discharging an obligation of this round.
   The closure forbids it at its lines 108–110 and the evidence rule's clause 5 repeats it.
10. **Treating act 19's uncertified conclusions as refuted.** The closure's lines 8–10 fix the
    register and this round keeps it: uncertified is not refuted.
11. **Editing act 19's freeze.** It is valid and unwithdrawn. Act 20 reads it and writes nothing into
    it, and an execution that wants it changed does not change it.
12. **Merging the two sides.** The specific failure guarded against is a verdict proved on the left
    class and reported as a verdict about naturality. The left law says a move is invisible and the
    right law says a move acts by specific phases; the two sides can differ and the round reports
    them apart.
13. **Losing the anchor, and losing the rank bound.** `FibreGram a₀` and `RealizableGram` both carry
    data a construction can silently drop: the anchor, and the `|A|` rank bound that makes act 12's
    sufficiency true.
14. **Treating `|A| = 1` as automatically the right case.** The left class is smaller there than at
    `|A| ≥ 2`, and a verdict reached there is reported as reached there.
15. **A reader supplying a missing theorem from background knowledge the record does not contain.**
    The specific failure guarded against is a step of the form "of course conjugation is a group
    automorphism, so" — plausible-sounding, absent from the record, and licensed by nothing in it.
    Every step is either a merged result cited at its coordinate or a theorem this round proves.
16. **Enlarging a bounded verdict.** Each verdict is bounded to the lift this round built, the notions
    this freeze states, and the configuration named.
17. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
18. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier in a different programme. Nothing is consumed or compared, and a shared word is not a
    bridge.
19. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_RNT_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
20. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
21. **A chronology guard that fixes this round's own pins at `None` for all time.** See the chronology
    control's clause 9, which exists because an earlier round wrote exactly such a clause and its
    whole execution object had to be rebuilt.
22. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: **freeze or run a condition ladder**, state a rung, or open a conjunction of
rungs; **run a survivor census**, count survivors, or test any transition family against any
condition set; **report `L-RIGID`, `L-FAMILY`, `L-WIDE` or any rigidity headline**, in any
paraphrase; **run act 19's same-initial-orbit discriminating test**, or state, witness or refute it;
**choose which condition a later round's naturality rung ought to impose**, recommend a notion, rate
the notions against one another, or say which the programme needs; **adopt or pre-commit any part of
act 21's ladder**, its quotient list, its candidate list or its headline; claim that any lift other
than the one it builds satisfies or fails anything; claim a universal statement over lifts of the
relabelling's transition; derive, recognise, approach or claim progress toward quantum evolution;
adopt a law, a carrier or a selection principle, or assert that one is or is not the physical one;
edit, amend, withdraw, correct or reinterpret act 19's control plane or act 19's closure; merge,
cherry-pick from or cite as settled act 19's execution branch; re-prove, strengthen, redefine or
enlarge acts 7, 10, 11, 12, 13, 17 or 18; redefine `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`LeftFibreGroup`, `WeakAnchorStabilizer`, `StrongAnchorStabilizer` or `CoherentLift`; revise `GL1s`,
`GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`–`AB2`,
`CT1`–`CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3`, `XS0`–`XS5` or any merged
label; answer act 13's fork `CT3` (d) or move it in either direction; ask the threading question or
the cross-time representative question, in either direction; touch act 16's cancellation cell or act
18's `D`-axis, in either direction; introduce a further carrier or revise any of act 14's four;
resolve, reopen or narrow act 10's anchor-axis reclassification; change `D3`, `D4b`, `D5`, the
direct-branch statement or the readback convention; alter any existing archive seal constant; write
to `verification/ROADMAP.md`; edit any manuscript; consume or compare anything from the substratum
Lemma 24.1 rounds; compare Source A with B or C; close `P0` or either of its parts; or say anything
about Track I.

### The normative question is EXPLICITLY OUT OF SCOPE

**"Which of the three notions should a naturality condition impose?" is not asked, not bounded and
not attempted.** It is the natural next question of this round and it is a **normative** question:
answering it requires weighing what a rigidity verdict is for, what a programme wants a naturality
rung to exclude, and what a later ladder is trying to measure — none of which this round has standing
to weigh and none of which an evidence bar could settle. It is named here as a non-doing **so that it
cannot creep in mid-execution**: an execution that has classified the lift and begins arguing for a
notion has left this round's scope, and what it produces is **recorded as an observation and not
executed**. **The choice is the owner's and it is made in act 21's preregistration.**

**And the round refuses the weaker version too.** "The natural choice would be", "this suggests
that", "a later round would presumably", and "the interesting condition is" are forbidden sentences
for the same reason. A round that has no standing to recommend may not hint.

### The direct-branch statement, carried unchanged

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most seven** top-level Lean definitions, and these are the seven:

1. **`StrictNatural`** — `N-STRICT`, in this freeze's wording, as a conjunction of a left clause and
   a right clause. *Needed.*
2. **`TwistedNatural`** — `N-TWIST`, in this freeze's wording, taking the two maps as parameters
   **before** the quantifiers over inputs, and carrying the two closure conjuncts. *Needed.*
3. **`OrbitNatural`** — `N-ORBIT`, in this freeze's wording, the per-input existential on both sides.
   *Needed.*
4. **`RelabelTransition`** — `Φ_σ`, act 19's frozen `ΦP` statement carried into Lean: the
   simultaneous relabelling of the fibre index and of both matrix indices. *Needed*, because `RNT2`'s
   lifting property cannot be stated without it.
5. **`RelabelLift`** — `Ψ_σ`, the representative-level lift, whose obligations `RNT2` freezes and
   whose formula this freeze deliberately does not fix. *Needed.*
6. **`RelabelInducedLeft`** — the induced map on the left gauge data. **Conditional**: it fires only
   if `RNT3` reaches its exact law on the left, and is unused otherwise.
7. **`RelabelInducedRight`** — the induced map on the right gauge data. **Conditional**: it fires only
   if `RNT3` reaches its exact law on the right, and is unused otherwise.

**Slots 6 and 7 are OUTPUTS and not inputs, and the ordering obligation treats them as such.** They
are not present at the definition commit; their first appearance on the execution branch **is** a
discriminating result. Stating them early would be stating `RNT3`'s answer early.

**Why this budget is seven and not fewer, recorded as a reason and not as an expansion.** The three
notions must be three named declarations, because the round's whole product is the distinction
between them and a distinction stated inline in the theorems that use it cannot be diffed across two
commits. The transition and the lift must be named because every later statement quantifies over
them. The two induced maps must be named because `RNT3`'s positive outcome is precisely the
exhibition of maps independent of the dilation, and an existential proof that never names them has
not reached it. **The budget buys the checkability of the ordering obligation**, and the freeze says
so rather than letting the count drift.

**A further definition beyond these seven requires its own append-only amendment**, separately frozen
and merged before the work it affects. **No gauge element, witness, matrix, visible family, Gram
tuple, entry value, permutation or configuration is a top-level definition** — each is a bound
variable pinned by an equation in the statement that needs it, as acts 10 through 19 did. In
particular `RNT5`'s separating lift, if one is found, is a bound variable pinned by equations and not
a declaration. Acts 7's, 10's, 11's, 12's, 13's, 17's and 18's definitions are **reused, not
redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `RNT1` through `RNT5`, whichever label each reaches other
than UNDECIDED. `decide` over finite index types is kernel-checked and permitted; `native_decide` is
not, and neither is `sorry`. `Classical.choice` is expected wherever a merged sufficiency result is
applied and its appearance there is not a defect.

**`RNT6` carries no evidence level of its own**, being the composition of the labels of `RNT3`,
`RNT4` and `RNT5`, and it introduces no theorem. Claims about the **record** — what the merged tree
does or does not already contain — carry no evidence level and are settled by the evidence rule's
clauses 2 and 3.

## The ordering obligation — act 19's mechanism, carried forward and STRENGTHENED

**The rule.** The three notions, the transition and the lift's obligations are fixed by this
control-plane blob and by nothing else. **They cannot be edited after the first discriminating result
has exposed the classification**, and — this is the strengthening — **they cannot be edited after the
execution has learned the classification by any means at all, including by reasoning that ran
nothing.**

**Act 19's failure was not mechanical.** Its ordering obligation was honoured in every respect an
audit of the branch can check: the chain was linear from the mandated base, nothing was amended or
rebased, and no theorem preceded the discrimination commit. What contaminated it arrived by
pen-and-paper reasoning, which its attestation questions did not cover. **Act 20 therefore carries
the mechanism forward and adds a third question to it.**

**The obligation, in its exact frozen wording, which binds the execution:**

> **The ordering obligation.** The three notions `N-STRICT`, `N-TWIST` and `N-ORBIT`, the transition
> `Φ_σ` and the obligations on the lift `Ψ_σ` are fixed by this control-plane blob and by nothing
> else. The execution states each in its Lean module in the wording this file freezes for it,
> **before** it attempts any discriminating result; and from the moment the first discriminating
> result enters the execution branch, **no commit of that branch alters the statement of any of the
> three notions, of the transition, or of the lift's frozen obligations, and none adds a notion,
> removes a notion, or changes which notions the classification is taken against.** The first
> discriminating result is whichever of these enters the branch earliest: the first proof about
> `Ψ_σ` beyond its two frozen obligations, the first appearance of either induced map, the first
> statement of either intertwining law, the first verdict on whether an induced map is the identity,
> the first verdict on strict naturality, and the first witness or refutation of the separation.
> **An execution that cannot demonstrate this ordering has not honoured it**, and the round is
> reported with the ordering obligation named as undischarged.

### The definition commit, the discrimination commit and the immutability span

**Three records, each checkable by an auditor from the branch alone**, plus the attestation set
below. The result note carries all four, and a missing record is a defect of the round and not a
formality.

1. **The definition commit** — act 20's analogue of act 19's ladder commit. The SHA of the commit on
   the execution branch at which **every definition this round freezes is stated in Lean**: the three
   notions, the transition and the lift, each in this file's wording — together with the statement
   that **no discriminating result is present at that commit**. Specifically, at that commit there is
   **no proof about `Ψ_σ`** beyond its two frozen obligations, **no computation of either induced
   map**, **no appearance of `RelabelInducedLeft` or `RelabelInducedRight`**, **no statement of
   either intertwining law**, and **no verdict on whether an induced map is the identity**. An
   auditor checks with `git show` and `git diff` against the mandated base.
2. **The discrimination commit**, named as such. The SHA of the commit at which the first
   discriminating result entered the branch, **with which result it was**, drawn from the list the
   obligation names.
3. **The immutability span.** The statement, with the command that checks it, that between the
   discrimination commit and the certified head `E` **no diff touches the statement of any frozen
   definition**. The command, printed in the result note with its result:
   > `git diff <discrimination commit> <E> -- verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`
   >
   > restricted to the declarations `StrictNatural`, `TwistedNatural`, `OrbitNatural`,
   > `RelabelTransition` and `RelabelLift`, is empty.

**The definition commit's boundary is weaker here than act 19's ladder commit's was, and the freeze
says so rather than overselling it.** Act 19's ladder could be stated without determining which laws
survive it. **Act 20's definitions cannot**: an agent that has written `Ψ_σ` holds, in principle,
everything needed to work out the induced map on paper. The commit boundary therefore checks that the
answer was not *stated* early; it cannot check that it was not *known* early. **That is precisely
what the third attestation question is for**, and it is why the attestation set has three questions
and not two.

### The attestation set — THREE questions, answered in the result note

**The result note answers all three, in this wording, for the span from the mandated base to the
discrimination commit.**

> **Q1 — INTENTIONAL.** Did the execution attempt or run any proof, search, decision procedure or
> numerical experiment intended to reveal the classification — which of the three notions the
> relabelling's lift satisfies, what the induced map on either side is, or whether either induced map
> is the identity?
>
> **Q2 — INCIDENTAL.** Did any compiler response, elaboration result, typeclass resolution, accepted
> or rejected term, or build output reveal any of that unintentionally?
>
> **Q3 — UNAIDED REASONING.** Did the execution **reason its way** to any information bearing on the
> classification **without running anything**?

**A PARTIAL fact counts for all three.** Learning that an induced map is, or is not, the identity on
**even one gauge element**, or that one of the three notions fails on **one input**, is already
discriminating. **A question is answered YES if any such partial fact was acquired**, however
incidentally, however small, and whether or not it was acted on. There is no threshold below which a
fact about the classification does not count.

**How a YES is handled, frozen before it can be needed.** A YES is **disclosed**, with what was
learned, when it was learned relative to the definition commit, and whether any frozen statement
changed afterwards. It is not concealed and it is not argued away. **A disclosure does not cure a
contamination** — act 19's closure is explicit that its disclosure established the contamination
rather than curing it — and equally a YES does not by itself void the round: what it does is put the
adjudication in front of the owner with the facts stated. **Concealment is the defect this set exists
to prevent**, and an execution that answers all three NO is making a substantive claim that the rest
of the record must be consistent with.

**The three answers are reported as measurements and not as intentions**, in the result note's own
words, beside the three commit records.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-RNT`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_RNT_SEALED_HEAD`** and **`_RNT_MERGE`**, with the
base held in **`_RNT_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 20 object
   enters the repository tree** — any Lean definition or proof about a naturality notion, about the
   relabelling's transition, about its representative-level lift or about an induced map on gauge
   data; any probe clause; any result artifact. **The single permitted exception is the analysis
   recorded inside this control-plane blob itself**, merged *as* the freeze, including the reading of
   the two merged transformation laws recorded as the freeze's reason, the bounded reading of what
   the record supplies, and the abstention recorded in place of two predictions.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_RNT_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content at this exact path, and the
   execution ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails closed**,
   with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _RNT_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of `B`**,
   fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for `B`,
   for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_RNT_SEALED_HEAD` and `_RNT_MERGE` are present and **unset** at execution. After
   `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the same strong
   check against the sealed object: the pinned merge's second parent must equal the sealed head; the
   sealed head must pass clause 5 against `B` exactly as in its own run; and both must be reachable
   from the current target — the real `pull_request.head.sha` in pull-request continuous integration,
   `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change recording the two SHAs and
   nothing else.
8. **Existing seal constants are read with mutation controls and never written.** The guard clause
   checks `_XTS_BASE`, `_XTS_SEALED_HEAD`, `_XTS_MERGE`, `_TRJ_BASE`, `_TRJ_SEALED_HEAD`, `_TRJ_MERGE`,
   `_RNC_BASE`, `_RNC_SEALED_HEAD`, `_RNC_MERGE`, `_TCF_BASE`, `_TCF_SEALED_HEAD`, `_TCF_MERGE`,
   `_PQT_BASE`, `_PQT_SEALED_HEAD`, `_PQT_MERGE`, `_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE`
   equal to the values acts 18, 17, 16, 15, 14 and 13 set, because an archive seal belongs to the
   round that set it. **Act 19 set none**, so there is no act 19 triple to read and none is invented.
9. **This round's own triple is never a permanently fixed execution-mode value.** `R7-RNT` must not
   assert `(_RNT_BASE, _RNT_SEALED_HEAD, _RNT_MERGE)` equal to `(_RNT_BASE, None, None)` as a standing
   invariant. Either the round's own triple is **excluded** from the prior-seal integrity clause of
   item 8 — which names other rounds' seals and is the shape this freeze intends, following the
   `_tcf_prior_seals`, `_rnc_prior_seals`, `_trj_prior_seals` and `_xts_prior_seals` precedent of
   **zero executable references to the round's own constants**, with docstring prose explaining the
   exclusion being entirely sufficient — or it is checked **mode-aware**, the expectation being
   `(_RNT_BASE, None, None)` while `_RNT_SEALED_HEAD` is unset and
   `(_RNT_BASE, _RNT_SEALED_HEAD, _RNT_MERGE)` once `P` has set them, and read from the module
   constants rather than from the argument, so that a fabricated tuple cannot define its own
   expectation. A clause that fixes this round's own pins at `None` for all time contradicts item 7,
   under which `P` must set them: the guard would then pass at no commit once the round lands, and the
   round's mandatory lifecycle could not complete. **This item exists because an earlier round wrote
   exactly such a clause and its whole execution object had to be rebuilt**, and it is written so that
   the executing agent cannot reintroduce that failure: **the exclusion route is the one this freeze
   intends**, and the mode-aware route is permitted only in the exact form stated here, with the
   expectation read from the module constants and **never** from the argument. Prior rounds' seals stay
   read-only invariants exactly as item 8 states; this item constrains only how the round treats its
   **own** pins.

**The executing agent is directed to the exclusion route, in terms.** The `R7-RNT` prior-seal
integrity function names acts 13's, 14's, 15's, 16's, 17's and 18's triples and **says nothing whatever
about `_RNT_BASE`, `_RNT_SEALED_HEAD` or `_RNT_MERGE`**: zero executable references to this round's own
constants, with the exclusion explained in the function's docstring. **And the exclusion is verified
empirically before the commit, in three configurations**, the third being the one an earlier round
failed: unmutated, expecting `True`; every single-field fabrication of each prior-seal constant one at
a time, expecting `False` each time; and **this round's own pins set to plausible values with the prior
seals unmutated, expecting `True`**. The three results are reported as measurements and not as
intentions.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-20-representative-naturality/preregistration.md \| git hash-object --stdin` equals the blob the `R7-RNT` clause pins |
| 2 | Act 19's closure and control plane are present, unedited | `git rev-parse B:verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/closure.md` equals `3d37529cb89a4d2bb60281f14f15645e3beaeb4c` and `git rev-parse B:verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md` equals `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057` |
| 3 | Act 19 landed no formal state | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-OLR` and no occurrence of `_OLR`, and `git ls-tree -r B --name-only` contains no `verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean` |
| 4 | Act 18's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_XTS_SEALED_HEAD = '730a518c173460d7bed525da10a95ee6bd32c7de'` and `_XTS_MERGE = '0b893d75cca344faeb9a9e434b5b8537f8b45dac'`, both non-`None` |
| 5 | Act 17's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TRJ_SEALED_HEAD = '94d41561114b2aee5939dcfa976ce98b8f141093'` and `_TRJ_MERGE = 'e8b12a433ebc0e5047504d2c95664a85ca65d1e8'`, both non-`None` |
| 6 | Acts 16's and 15's executions are merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_RNC_SEALED_HEAD = '31db7c1082b012c00c43f3fda35ce44c5653e123'`, `_RNC_MERGE = 'eb70bbb9b2b3311095945ec3ce2418962f3b741a'`, `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, all four non-`None` |
| 7 | Acts 14's and 13's executions are merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'`, `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, all four non-`None` |
| 8 | The modules this round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` and `git cat-file -e B:verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` all succeed |
| 9 | No act 20 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-20-representative-naturality/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` |
| 10 | The guard tag and its stem are still free | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-RNT` and no occurrence of `_RNT` |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are **not** inputs: the anti-contamination invariant governs, and the
round consumes only what this freeze's start-state table names.

**The claim is scoped to the repository record.**

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**, and the path this file sits at is pinned with it, so the directory and filename do
  not move after this merges.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This pull request carries this file alone.**
- **The execution branches from the merge commit of this control-plane pull request and from nothing
  else**, and **its first act is to verify that the preregistration at that base carries the blob this
  freeze names**, before any target is executed. The verification is recorded in the result note.
- **The definition commit comes second**, before any discriminating result, and its SHA is recorded.
  The ordering obligation's three commit records and the three attestation answers are assembled as
  the execution proceeds and are **not reconstructed at the end**.
- **Then exactly one execution pull request**, based on that merge commit, carrying the Lean module,
  the result note, the `R7-RNT` guard clause with `_RNT_SEALED_HEAD` and `_RNT_MERGE` present and
  unset, the `OIBridge.lean` import line and the census entry. **No manuscript changes, and no
  `ROADMAP` changes.**
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no rebase,
  no amend, no force-push. A red badge caused solely by an archive clause that entered `main` after
  the base is not a research failure; the certification of record is the run whose `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled named
   and no existing seal constant altered, and the base-blob verification recorded;
2. **the ordering obligation's records, in full** — the definition commit SHA with the statement of
   what was absent at it, the discrimination commit SHA with which result crossed, the immutability
   span with the command and its result, and **the three attestation answers in the freeze's own
   wording**, with the partial-fact rule stated and any YES disclosed in full;
3. **`RNT1`** — the three notions as stated in the kernel, the implication chain in whichever label it
   reached, with the place each closure conjunct of the twisted notion is used named at the step, and
   with the statement that no converse is established;
4. **`RNT2`** — the lift, named by its declaration, with both parts reported separately, and with the
   statement that it is a construction and not a uniqueness claim;
5. **`RNT3`** — the exact intertwining law or its weaker alternative, reported **per side**, with the
   maps exhibited where they were, and with a weaker theorem never reported as a stronger one;
6. **`RNT4`** — parts (a) and (b) reported **separately and for each side**, with the frozen statement
   that a non-identity induced map does not by itself establish a failure of strict equivariance, and
   with the scope note that the verdicts are about the lift this round built;
7. **`RNT5`** — the separation, the collapse, or the recorded UNDECIDED with the obstruction named,
   and in the UNDECIDED case the explicit statement that the two formulations are kept apart and not
   conflated;
8. **`RNT6`** — the classification in the status rule's frozen wording, followed by the frozen closing
   sentence that the choice of condition is the owner's and is made in act 21's preregistration;
9. **the scope boundary as honoured**: the confirmation that no ladder was frozen or run, no census
   was run, no rigidity headline was reported, act 19's discriminating test was not run, no condition
   was chosen for a later round, and no part of act 21's ladder was adopted or pre-committed;
10. **the act 19 boundary as honoured**: the confirmation that act 19's control plane and closure were
    read and not edited, that act 19's execution branch was not merged, cherry-picked from or cited as
    settled, and that nothing uncertified by act 19 is reported as refuted;
11. **the non-choice clause carried verbatim at each mention**, with the count of carriages;
12. the `|A|` value at which each verdict was reached, and the configuration for each;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 7, 10, 11, 12, 13, 17, 18 and 19 — every merged label consumed, none revised;
15. the definition count against the seven-slot budget, with the two conditional slots marked fired or
    unused;
16. the chronology certification, naming the property certified, the ten preconditions checked at `B`,
    the archive-mode pins as unset at execution, and clause 9 reported as honoured by exclusion with
    the three empirical configurations reported as measurements;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Items 1 through 10 are calls
already made**, written here so the record shows they were settled rather than left open. The body of
this freeze is written to them throughout. **The open decisions follow them in their own section and
are not calls already made.**

1. **The scope is FROZEN as written and is not renegotiated.** Act 20 is the naturality-classification
   round only. No ladder, no census, no survivor count, no rigidity headline, no same-initial-orbit
   test. An execution that wants more freezes its own round.
2. **Act 20 does NOT choose which condition a later round's naturality rung ought to impose.** The
   choice is the owner's and it goes into act 21's preregistration. This is carried in the
   non-doings, in the forbidden sentences, in the hazard list and in the closing sentence of every
   frozen status-rule outcome.
3. **Act 21 is a fresh rigidity round**, written only after act 20 is merged, pinned and reviewed.
   Nothing here is a commitment about it.
4. **The three notions are the closure's three**, stated in this file's wording, with the twisted form
   carrying its two closure conjuncts and its maps fixed before the quantifiers over inputs.
5. **`RNT3`'s positive outcome is an exact law and never an existential over the output.** A per-input
   witness earns the weaker label.
6. **`RNT4` is split into two parts** because a non-identity induced map does not by itself establish
   a failure of strict equivariance, and each part is earned separately.
7. **`RNT5`'s UNDECIDED route is preregistered explicitly**, exactly as act 19 preregistered its own
   fallbacks, so that an execution which cannot find a counterexample reports that rather than
   eliding the distinction.
8. **The chronology obligation carries THREE attestation questions**, because act 19's contamination
   arrived by pen-and-paper reasoning that two questions did not cover, and a partial fact counts for
   all three.
9. **Act 19's control plane and closure are read and not edited**, act 19's execution branch is
   research material and is not cited as settled, and uncertified is not reported as refuted.
10. **Acts 7, 10, 11, 12, 13, 17 and 18 are consumed at merged strength**: not re-proved, not
    strengthened, not redefined.

### Open decisions, recorded for owner settlement before this freeze merges

**These are NOT calls already made.** Each is recorded with its options, this freeze's recommendation
and the reason, in the act 16, 17, 18 and 19 pattern of recording a settlement rather than leaving one
implicit. **The freeze does not merge until each is settled**, and the body above is written to the
recommended option throughout so that settling it the other way is a bounded edit and not a rewrite.

**Open decision 1 — SEALING or NON-SEALING.**

- **Option A, recommended: SEALING**, under the guard tag `R7-RNT`, landing `E` → `L` → `P` with `P`
  mandatory, with chronology clause 9 honoured by excluding this round's own triple from the
  prior-seal integrity clause. **The reason is derived and not defaulted**: act 20's execution creates
  the three notions, the lift, the induced maps and the classifying theorem, none of which exists at
  the base, and the round's whole claim is a claim about **when** those definitions were fixed
  relative to the classification. That is the owner's sealing criterion exactly, and it applies with
  more force here than in act 19, because act 20 is the round convened *because* a definition moved
  after its author knew the answer.
- **Option B: NON-SEALING**, taking `L` alone under `§A.37` item 2. This is correct **only if** the
  owner directs that act 20 add no Lean module, no named result and no guard clause. **The cost is
  recorded honestly**: the three notions would then have no kernel statement to diff, the ordering
  obligation's three commit records would lose their mechanical check entirely, and the round's
  central claim would rest on the result note's testimony alone — which, for the round whose subject
  is act 19's chronology failure, is the weakest possible shape. **The freeze recommends against
  Option B** for that reason and not because recent rounds have been sealing.

**Open decision 2 — whether act 20 appends a sentence to the `P0` row.**

- **Option A, recommended: no `ROADMAP` change at all.** `verification/ROADMAP.md` sits in the
  read-only start-state table and the execution does not write to it. The reason is that act 20
  settles nothing `P0` asks: it clarifies a phrase in a control plane and classifies one lift. A
  sentence appended to `P0` about a programme's own vocabulary would report apparatus as a finding
  about the obligation.
- **Option B: append a short frozen sentence to `P0` recording that the naturality notion a
  cross-time rigidity condition would use has been separated into three and one lift classified
  against them.** The reason this option is live is continuity: every round from act 13 onward has
  propagated, and a reader tracing `P0` through the acts will find act 20 missing from the row. **If
  the owner settles Option B, the sentence is frozen in this file before it merges**, with its per-
  outcome substitutions, and the `ROADMAP` moves from the read-only table to the written table.
  Appending a sentence that was not frozen here is forbidden either way.

**Open decision 3 — whether the module states the notions for a general gauge class or for the two
named ones.** The three notions are frozen above against `LeftFibreGroup` and `WeakAnchorStabilizer`
by name. **Recommended: keep them stated against the two named classes**, because every verdict of
this round is about those two and a general formulation would add a quantifier no target needs. The
alternative is to state them over an arbitrary class predicate and instantiate twice, which is more
general and costs a parameter in every statement and every proof. The freeze recommends the concrete
form, and records that if the execution finds the general form strictly easier it may **not** switch
to it: the notions are frozen in the wording above, and a change of that wording is an append-only
amendment merged before the work it affects.

**Open decision 4 — whether `RNT5` should name a configuration in advance.** `RNT5`'s separation and
collapse outcomes are both stated "at the configuration named", and this freeze does not name one,
because it names no construction for the separating lift and cannot know where one would live.
**Recommended: leave the configuration to the execution, and require it to record the configuration
in the result note at the step, never chosen after the outcome is known.** The alternative is to
freeze act 12's `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼` configuration here and confine `RNT5` to
it, which is cleaner against the hazard of a configuration chosen after an outcome and narrower than
the target needs. The freeze recommends the first with the recording requirement, and records that
the second is a defensible call the owner may take instead.

**One check was performed at drafting time and its outcome is recorded here as a settlement rather
than as a correction in flight.** The two mandatory verbatim clauses of this file — the start-state
discrepancy clause and the anti-contamination invariant — were **extracted by reading bytes** from act
18's preregistration blob `fd3fa1359188966cae006deba4944a14aab5f3dd` and act 19's preregistration blob
`8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`, each bounded by its own paragraph and not by assuming
quote form, and each reproduced here without retyping. The discrepancy clause is **plain prose** in
both files and is plain prose here; the anti-contamination invariant is a **block quote** in both and
is a block quote here. The two act 18 paragraphs and the two act 19 paragraphs were compared byte for
byte and are identical. Each appears in this file **exactly once**, so the carriage device is not
needed for either; it is used only for the three carriages of THE CLAUSE, each opened by a distinct
naming line with the quotation bytes untouched.
