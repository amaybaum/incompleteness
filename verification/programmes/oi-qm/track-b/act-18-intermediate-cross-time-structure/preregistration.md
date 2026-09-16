# Track B act 18 — the intermediate regime: what extra structure supplies cross-time information: CONTROL PLANE

Owner-called. This file is the whole of act 18's control plane and is merged **alone**, before any
execution object exists. It takes up the question act 17 leaves standing inside `P0`'s trajectory
part: **what is the weakest physically meaningful extra structure that supplies genuine cross-time
information without simply handing over the trajectory itself.** It is **not** the threading
question, which act 13 localized and acts 14, 15 and 16 pursued carrier by carrier, and it is
**not** the question of which representative is chosen inside an orbit.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–778**, quoted verbatim at this base —
the numbered item's opening sentence, ending part-way through line 778:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes ownership of
>    changing existing seal state — takes a pin commit `P`, and `P` is mandatory.**

This freeze **creates new seal state**. The execution writes a new Lean module with its own guard
clause in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-XTS`**, and that
clause carries the archive-mode constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_XTS_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_XTS_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_XTS_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_XTS_SEALED_HEAD` to `E` and `_XTS_MERGE` to `L`, moving the `R7-XTS` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_XTS_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

**Why sealing rather than non-sealing, stated as a reason and not as a habit.** The execution adds a
new Lean module carrying this round's own named results, and the round's whole value depends on those
results having been reached **after** this freeze and from this freeze's base. A candidate list
assembled after it was known which candidates survive would be worth nothing, and the two ladders
below would then be reporting a search that had already seen its own answer. A new module with new
named results is new seal state under `§A.37`'s definition, so the round owns a pin and takes one. It
owns **no other** seal state.

**The tag and its stem are free at this base, and the check is recorded.** At
`ece8f9635a85eb1e57daaa13bb2dec34ae431d20`, `git grep -- 'R7-XTS'` returns nothing anywhere in the
tree, `git grep -- 'XTS'` returns nothing anywhere in the tree, and no constant whose name contains
the stem `_XTS` exists in `verification/lean/edge_rigidity_probe.py`. The stem was chosen after
checking the alternatives: the three-letter forms `ICS` and `CTS` both occur as substrings of
existing text in the tree — `ICS` in the book chapters, `CTS` in the lattice probes and the coverage
ledger — so a bare-stem search for either would be ambiguous, and both were rejected for that reason.
`XTS` occurs nowhere. The existing tag `R7-WTS` and its stem `_WTS_` are a different three-letter
stem and no substring search for `XTS` or `_XTS` can reach them.

**The round directory and the module name are free at this base too.**
`git ls-tree -r ece8f96 --name-only` contains no path matching `act-18`, and no path matching
`IntermediateCrossTimeStructure`; `git grep -- 'act-18'` and
`git grep -- 'IntermediateCrossTimeStructure'` both return nothing anywhere in the tree.

**What this round does NOT own, named exhaustively.** It alters **no existing seal constant**. In
particular `_TRJ_BASE`, `_TRJ_SEALED_HEAD` and `_TRJ_MERGE` — act 17's seal — and `_RNC_BASE`,
`_RNC_SEALED_HEAD` and `_RNC_MERGE` — act 16's — and `_TCF_BASE`, `_TCF_SEALED_HEAD` and `_TCF_MERGE`
— act 15's — and `_PQT_BASE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE` — act 14's — and `_CTI_BASE`,
`_CTI_SEALED_HEAD` and `_CTI_MERGE` — act 13's — and `_A12P_*`, `_SGT_*`, `_TSG_BASE` and `_CLG_BASE`
are **read and never written**. An archive seal belongs to the round that set it: touching the guard
file that carries those constants does not make this round their owner, and the execution's diff
against `edge_rigidity_probe.py` **adds** the `R7-XTS` clause and changes nothing else in the file.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`ece8f9635a85eb1e57daaa13bb2dec34ae431d20`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

### The obligation, and the part of it act 17 has now bounded

`verification/ROADMAP.md`, **line 63**, the `P0` row's obligation cell and its status opening:

> | **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED: act 11's `GL2` proved the visible family does not fix the relative evolution;

and, from the same line, the sentence that makes the row two-part and names this round's part first:

> so what remains is **two-part**: what selects or constrains the Gram/orbit trajectory **across time**, and what determines the cross-time threading within those orbits, which act 11's `GL2` shows is not fixed even by the full Gram trajectory

and, from the same line, the clause act 17 added, which is the baseline this round starts from:

> the admissible Gram trajectories of a visible family are exactly the pointwise realizable assignments: the merged record constrains each slice by act 12's `SH1` and imposes no coupling between slices, so every cross-time constraint on the trajectory is additional structure rather than a consequence of coherence, and there is no additional universal cross-time constraint on coherent Gram trajectories beyond pointwise realizability — a statement about coherence as the programme defines it, indexed by the naturals and pointwise in time, and not a statement that no cross-time structure could be added to the programme

### The act 17 baseline in the `ROADMAP`'s own words

`verification/ROADMAP.md`, **lines 560–565**, beginning part-way through line 560 — the bullet opens
at line 556, and the span quoted here is the part that governs this round:

> **there is no additional universal cross-time constraint on coherent Gram trajectories
> beyond pointwise realizability** — the present notion of coherence contributes no coupling between
> times at all, and **any such law must enter as additional structure**. The narrowing act 12's rank
> bound effects is **pointwise** and is labelled pointwise. This is a statement about coherence as
> the programme defines it, indexed by the naturals and pointwise in time, and **not** a statement
> that no cross-time structure could be added to the programme.

### The two-axis reporting precedent this round follows

`verification/ROADMAP.md`, **lines 585–587**:

> **The two findings are on two axes and are not merged into one ordering.** "The present notion of
> coherence imposes no cross-time coupling" is not above or below "these four proposed selectors all
> fail at one admissible configuration": they answer different questions.

### The level-2 datum this round bounds its Type D candidates below

`verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md`, **lines 135–139**:

> **Consequence, stated exactly:** the fibre cross-Gram trajectory determines the lift up to a
> **constant** in-fibre left move and a **time-dependent strong** right gauge — its residual is exactly
> `GL2`'s mechanism together with one constant `𝒢_L` conjugation, and nothing else. With `CT1`:
> relative to the level-2 data, the threading freedom of `P0` is exactly a strong-right family `K_t`
> modulo a constant, together with one constant in-fibre frame.

### The anchor axis this round's anchor-coherence candidates are grounded in

`verification/programmes/oi-qm/track-b/act-10-anchor-robustness/result.md`, **lines 113–114**:

> **`P0` is not closed and the anchor-axis dependence is not resolved.** It is **reclassified** as not
> reachable by this construction, with the upstream anchor choice named as the live remainder.

### The interpretation boundary the whole of `P0` sits inside

`verification/ROADMAP.md`, **lines 52–57**:

> Accordingly, a failure of uniqueness at `P0` is not by itself a failure of quantum emergence. It
> determines the ontology of that emergence: either the residual lift freedom is physically redundant,
> additional structure selects one quantum history, or observational incompleteness determines only an
> equivalence class of quantum histories. Only an empirically distinguishable residual not removed by
> the physically appropriate equivalence relation would license a claim of physics beyond standard
> quantum mechanics.

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 697–700**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

**The mandated base, stated as this round's own commitment.** The execution branches from the merge
commit of **this** control-plane pull request and from **nothing else** — not from `main` at any
later point, not from a sibling lane's head, and not from a rebase of either. **Its first act is to
verify that the preregistration at that base carries the blob this freeze names**, before any target
is executed, and to record the verification in the result note. If the blob differs, the execution
records the discrepancy and does not repair the freeze.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `ece8f9635a85eb1e57daaa13bb2dec34ae431d20`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md` | `3b5570102aa6aacb09788059989a70d8cdd5b70f` |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/result.md` | `a252b885c6f7f5f31d3ac101070e7f6ee1ebf5d6` |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/preregistration.md` | `48099a3b334e8d01f31af706e8738cd49cfca774` |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/result.md` | `b13d684cb7454ff414a34ed9b6dca39065c3470f` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` | `fe8df06ffefac22ce87668ecf026f4c9ebc5c13f` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md` | `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md` | `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/result.md` | `ec9a6e0d8a7019805aca069abc39f90d632b6a2b` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md` | `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/lean-mathlib/OIBridge/ReanchoredChannelScope.lean` | `16f08f712cbbb0a0f752ac8d7e072b1d5e52d761` |
| `verification/lean-mathlib/OIBridge/CancellationFork.lean` | `2cdfdf7742694391f16a73eebe37e1c0dcad6674` |
| `verification/lean-mathlib/OIBridge/ThreadingObservability.lean` | `91508205b33d9419fbffec5ad44035fad35de5f1` |
| `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` | `47eb21e22845f0319926227c80d0d7f2f033880b` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/lean-mathlib/OIBridge/AnchorRobustness.lean` | `b74202bc160918b32ca1b333da532a141ea8015d` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `c69987e9eb8080efce0d2a61120019407d0e1997` | **read** as the pinned statement of the `P0` row, of act 17's baseline and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `d5558a7230d539c6bf5115a704cf1b7cddfb1db2` | the `R7-XTS` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `da9b4c1e9ec4b570925c853b1bc2a8954f8f96e7` | one import line added after act 17's module |
| `verification/lean-manuscript-census.json` | `4ed64a1412f71bd5c96ab67118c63b6c986def45` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one prose file this round both reads and writes, and it is listed
here rather than above for exactly that reason: the verbatim clause governs the read-only table
without qualification, and the `ROADMAP`'s treatment is stated in its own row. A difference in that
one blob at the base is recorded in the result note as a discrepancy, and the freeze is not repaired.

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

**Why this matters here, concretely.** Sibling lanes are drafting and executing in parallel with this
freeze, and some will merge into `main` before this round's execution begins. This freeze is written
against `ece8f96` alone and consumes nothing from any of them. No lane's unlanded output is read,
cited, compared or waited for.

## Source scoping, carried from acts 13 through 17

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what act 17 left in front of it

Act 17 established two things this round consumes and neither re-proves nor strengthens.

1. **`TJ1`, both directions.** The Gram trajectories of coherent lifts of a visible family are
   **exactly** the pointwise realizable assignments, so the admissible set is the **product over
   time** of the per-slice realizable sets. The present `CoherentLift` notion contributes no
   cross-time coupling whatever, and **any cross-time law must enter the programme as additional
   structure**.
2. **`TJ3` at line 4.** Class-level selection impossibility, quantified `∃ C ∀ S`: one admissible
   configuration defeats every member of the frozen four-member selector class.

Act 13 established the **level 2** datum: the fibre cross-Gram trajectory determines the lift up to
one constant in-fibre left move and one time-dependent strong right gauge. Act 12 established the
per-slice classification and the per-slice realizability characterization. Act 11 established that
the Gram trajectory does not fix the threading.

**So the record now carries two poles and nothing between them.** At one pole, act 17: the
operationally visible data alone, on the frozen candidate class, do not select. At the other pole,
act 13: the level-2 datum effectively contains the trajectory — act 17's own out-of-regime probe
`SP4` records the containment as a theorem rather than as a warning. **The whole subject of act 18 is
the interval between those poles**, and the question is the one the owner has frozen: **what is the
weakest physically meaningful extra structure that supplies genuine cross-time information without
simply handing over the trajectory itself?**

### What the merged record supplies for this interval, and what it does not

This table is a reading of the merged record, stated so that the gap this round works in is visible
and so that no target of this round has to discover it. Each cell cites the merged label that fills
it.

| question about the interval | what the merged record says | label |
| --- | --- | --- |
| what the admissible trajectory set is | exactly the product over time of the per-slice realizable sets | act 17's `TJ1`, both directions |
| whether coherence alone couples the times | **no** — no universal cross-time constraint beyond pointwise realizability | act 17's `TJ1` baseline finding |
| whether the frozen visible-data selectors select | **no** at one admissible configuration, for all four at once | act 17's `TJ3-IMP` |
| what the level-2 datum determines | the lift up to a constant in-fibre left move and a time-dependent strong right gauge | act 13's `CT2` (b), both directions |
| whether the level-2 datum determines the trajectory | **yes, by containing it** at its diagonal — a containment theorem and not a selection | act 17's `SP4-THM` |
| what lies strictly between the visible data and level 2 | **nothing on the record** | — |
| whether a pointwise law can propagate one time from another | **nothing on the record** | — |

**The last two rows are this round's subject.** The merged record says what happens at each pole and
is silent on the interval and on the propagation question. Whether that silence is a gap or is the
answer is what the round's first target asks of the record and what its later targets ask of the
kernel.

## The strength of the ask, FROZEN

**The ask is BOUNDED EXISTENCE ON TWO AXES, and the owner has settled it as such.** On each axis the
round asks whether a structure of the frozen type, drawn from the frozen candidate list, reaches the
axis's top line, its middle line, or neither; and where neither is reached it reports a **bounded
no-go over the frozen list** or **UNDECIDED with the obstruction named**. It does **not** undertake
to produce the coarsest such structure, to classify the structures that work, or to show that any of
them obtains.

**Why bounded existence and not the stronger asks, recorded as a reason.** A "coarsest determining
datum" ask would require a lattice argument over an unbounded space of functionals of the lift, which
this round's definition budget does not fund and which no merged result supplies; it is named as an
explicit non-doing below for exactly that reason. A "classification of the laws that propagate" ask
would require a surjectivity obligation over the space of laws, which nothing on the record bounds.
Bounded existence over a closed, pre-named candidate list is what the round can honestly attempt, and
it is what the two ladders are calibrated to.

**The ask does not narrow what may be reported.** The top line of each axis is **preregistered as a
reachable outcome with its own frozen post-round sentence**, at the full evidence bar frozen for it.
A stronger result is reportable **because it was preregistered as reachable**, and never because the
execution enlarged the round after finding it. **The scope is fixed here, before the search**, and a
result outside it is recorded as an observation and not executed.

## The headline is the ORDERED PAIR of two co-equal axis outcomes, FROZEN

**There is no single headline line, and no ladder ranks the two axes against each other.** The
round's outcome is the **ordered pair** `(D-axis outcome, L-axis outcome)`, reported as a pair
throughout, exactly as act 17 reported its two findings on two axes rather than merging them into one
ordering.

- **The `D`-axis** asks: is there a **readback datum** — a functional of the lift — that is strictly
  more informative than act 17's visible data, strictly less informative than act 13's level-2 datum,
  and still determines the Gram trajectory?
- **The `L`-axis** asks: is there a **structural law** — a constraint writable from `(a₀, Γ)` alone,
  before any lift is chosen — that is genuinely proper and non-trivial, and that propagates one time
  from another given an initial orbit?

**These are different questions and neither is above the other.** A datum is something one reads off
a history that already exists; a law is something one imposes before any history is chosen. An
affirmative on one axis is **not** evidence about the other in either direction, and the result note
carries that sentence at each place it reports one axis beside the other. **The pair is the result**;
neither element is "the" answer and neither is a fallback for the other.

## The two candidate TYPES, frozen separately

**A candidate is frozen with its type, and a candidate may NOT change type during execution.** The
type fixes which obligations it carries, which ladder it runs on and which frozen sentence reports
it. A candidate that looks during execution as though it would be better placed on the other axis is
**recorded as an observation and not moved**; the same object may be frozen as two separate
candidates, one of each type, and where this freeze wants that it does it explicitly, below.

**Why the types are kept apart, stated as the reason it is.** A readback datum and a structural law
answer to different obligations. A datum has to be shown *not* to contain the answer, which is what
the refinement sandwich does. A law has to be shown *not* to be vacuous and *not* to be the answer in
disguise, which is what the one-configuration non-triviality witness does. Letting a candidate drift
between the two mid-execution would let it answer whichever set of obligations it happened to
satisfy, which is the preregistration failure this section exists to prevent.

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13 and 17

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `Γ : ℕ → Matrix V V ℝ` a **visible
family**, `U : ℕ → U(V × A)` a lift, and the following are consumed **unmodified**, at their own
strengths: `readback`, `AdmissibleDilationAt`, `readback_relabel` (`R-3`),
`one_admissible_at_every_anchor`, `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`,
`GaugeRelated`, `strong_mem_weak`, `gl2_strong_gauge_moves_relative_candidate` (`GL2`),
`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`fibreGram_apply`, `fibreGram_diag`, `fibreGram_diag_of_admissible`, `fibreGram_posSemidef`,
`fibreGram_rank_le`, `sum_fibreGram`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`,
`left_preserves_admissible`, `gramPhaseEquiv_of_twoSided`, `twoSided_slice_iff`,
`twoSidedRelated_iff` (`TG2`, lifted), `gramPhaseEquiv_cross_invariant`, `hadamard_cross_ratio`,
`hadamard_slices_not_twoSided`, `hadamard_lifts_not_twoSided` (`TG3`), `sh1_necessity`,
`sh1_sufficiency`, `sh1_shape` (`SH1`), `sh1_c2_unique_orbit` (`SH1-C2`), `FibreCrossGram`,
`fibreCrossGram_apply`, `fibreCrossGram_apply_dotProduct`, `fibreCrossGram_diag`,
`sum_fibreCrossGram`, `crossGram_two_sided`, `crossGram_left_mul`, `fibreCrossGram_mul_weak_apply`,
`ct2a_crossGram_iff_constLeft` (`CT2` (a)), `ct2b_fibreCrossGram_iff` (`CT2` (b)),
`ct3g_fibreGram_strong_right` and `ct3g_fibreCrossGram_strong_right` (`CT3` (G)), and act 17's
`GramTrajEquiv`, `gramTrajEquiv_refl`, `gramTrajEquiv_symm`, `gramTrajEquiv_trans`,
`gramTrajEquiv_of_threading`, `tj1_necessity`, `tj1_sufficiency`, `tj1_trajectory_set`,
`tj1_no_universal_cross_time_constraint`, `hadamard_constant_lifts`, `SelectsAt` and
`tj3_imp_class_level_selection_impossibility`.

**The Gram trajectory of a lift**, written `𝔾(U)`, is the family `fun t => FibreGram a₀ (U t)`, and
**the Gram/orbit trajectory** is the sequence of `GramPhaseEquiv`-classes of those tuples, exactly as
act 17 uses both terms.

**`≈_O` is act 17's `GramTrajEquiv`, consumed and NOT redefined.** Two trajectories are the same iff
`GramPhaseEquiv (𝔾 t) (𝔾' t)` at every `t`, the phase family being chosen independently at each
time. It is the only relation any quotient in this round is taken over. It is act 17's definition,
built on act 12's per-slice `GramPhaseEquiv`, and this round adds no relation of its own and adopts
neither raw Gram equality nor the uniform-phase relation nor act 13's level-2 or level-3 relations.

**Act 7's boundary is carried at every use of the visible family**, exactly as acts 11 through 17
carry it: act 7's `D4b` came back **negative** — Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V` — and the readback is the repository's own,
frozen by act 7's readback amendment. Every statement in this round about what is visible is a
statement under that convention, said at each use rather than once in a footnote.

## The data ladder, FROZEN — `D₀`, `D₂`, and the augmented datum `D_F`

**Three objects, named once and used everywhere.**

- **`D₀`, act 17's visible datum.** `D₀(U) := fun t i j => ∑ a, ‖U t (i, a) (j, a₀)‖²` — the anchored
  readback of the lift at each time, under act 7's convention with `D4b` negative. For a coherent
  lift of `Γ` this is `Γ` itself, by `AdmissibleDilationAt`'s second conjunct.
- **`D₂`, act 13's level-2 datum.** `D₂(U) := fun i t s => FibreCrossGram a₀ U i t s` — the fibre
  cross-Gram trajectory, act 13's level 2, consumed at merged strength.
- **`D_F`, the augmented datum.** For a functional `F` of the lift, `D_F := (D₀, F)`, and
  `D_F(U) = D_F(U')` means `D₀(U) = D₀(U')` **and** `F(U) = F(U')`.

### The well-posedness check, performed at drafting time and recorded here

**Obligation 1 below requires `D_F = (D₀, F)` to consume no information beyond level 2, and applied
to the pair it requires `D₀` itself to factor through `D₂`.** The check was performed against act
17's and act 13's frozen text before this freeze was written, and it went the clean way.

**`D₀` factors through `D₂`, unconditionally, and the chain is two merged steps.** Act 13's
`fibreCrossGram_diag` is a definitional identity — `FibreCrossGram a₀ U i t t = FibreGram a₀ (U t) i`
by `rfl` — so `D₂` contains the per-slice Gram tuple at every time. Act 12's `fibreGram_diag` then
gives `FibreGram a₀ U i j j = ((∑ a, ‖U (i, a) (j, a₀)‖² : ℝ) : ℂ)` **with no admissibility
hypothesis at all**, so the anchored readback of the lift at each time is a function of the per-slice
Gram tuple's diagonal. Composing: `D₂(U) = D₂(U') ⟹ D₀(U) = D₀(U')`, for arbitrary lifts and at any
fixed anchor `a₀`, with no hypothesis on `Γ` and no appeal to coherence.

**So obligation 1 is stated for the full pair `D_F = (D₀, F)`**, and the fallback the owner named —
stating obligation 1 of `F` alone and recording `D₀` as a fixed-parameter comparison basis — is **not
used**. It is recorded here as considered and unnecessary, so that a later reader does not have to
re-derive why. **The stronger form is the one that is frozen**: equality of `D₂` implies equality of
`D_F`, both components at once.

**One consequence worth stating in advance.** Because `D₀` factors through `D₂`, the whole content of
obligation 1 falls on `F`, and the whole content of obligations 2 and 3 is about where `F` sits
between the two poles. The pair notation is kept because the substantive target is stated of the
pair, and because a candidate `F` that is uninformative on its own may still be informative beside
the visible family.

## Type D — a readback datum, FROZEN

**A Type D candidate is a functional `F` of the lift**, named in this freeze, and its frozen
obligations are these three plus one substantive target. `U`, `U'` range over lifts over one carrier
and one anchor.

> **The refinement sandwich.** For a Type D candidate `F`, with `D_F := (D₀, F)`:
> **obligation 1 — bounded above by level 2:** `D₂(U) = D₂(U') ⟹ D_F(U) = D_F(U')`, so `D_F` consumes
> no information beyond act 13's level-2 datum;
> **obligation 2 — strictly above act 17's visible data:** `∃ U, U'` with `D₀(U) = D₀(U')` and
> `D_F(U) ≠ D_F(U')`, so `D_F` is genuinely more informative than the operationally visible datum;
> **obligation 3 — strictly below act 13's datum:** `∃ U, U'` with `D_F(U) = D_F(U')` and
> `D₂(U) ≠ D₂(U')`, so `D_F` is genuinely less informative than the level-2 datum.

**The substantive target, stated separately and never folded into the sandwich:**

> **`D`-determination.** `D_F(U) = D_F(U') ⟹ 𝔾(U) ≈_O 𝔾(U')` — equality of the augmented datum
> implies the two lifts have the same Gram/orbit trajectory, the quotient being taken over act 17's
> `GramTrajEquiv` and over no other relation.

### Obligation 3 is stated against `D₂` and NEVER against the trajectory

**This is the one place where the obvious phrasing is wrong, and the freeze states it in terms so
that no executing agent reintroduces it.** Obligation 3 is *same `D_F`, different `D₂`*. It is **not**
*same `D_F`, inequivalent Gram trajectories*.

**Why the second phrasing is unsatisfiable exactly when the round succeeds.** The substantive target
says that equal `D_F` implies `≈_O`. So a pair with equal `D_F` and inequivalent trajectories is
precisely a counterexample to the substantive target. A candidate that reaches the top of the `D`-axis
therefore **cannot** have such a pair, by definition and not by accident: the two clauses are
contradictory. Writing obligation 3 in the second form would make the top line of the `D`-axis
unreachable by construction, and would do so silently — the execution would be searching for a
witness whose existence its own target forbids.

**What obligation 3 is actually doing.** It asks that `D_F` be a **strict coarsening of `D₂`** — that
some level-2 difference be invisible to it. That is a statement about the two data, not about the
trajectories they determine, and it is exactly what "genuinely less informative than act 13's datum"
means. **The execution states obligation 3 against `D₂` and against nothing else**, and a result note
that states it against the trajectory is a defect of this round.

### The frozen structural prediction on the `D`-axis, `P-D`

**This is preregistered as a prediction the round reports against, in the act 16 spirit, with its
falsification condition named.**

> **`P-D`.** Any `F` that reaches the top line of the `D`-axis discards, relative to `D₂`, **precisely
> threading and representative information and nothing else** — that is, the information `D₂` carries
> and `D_F` does not lies entirely in the directions `≈_O` already quotients: the per-time choice of
> in-fibre frame and the per-time anchored phase. **No `F` reaches the top line by discarding
> cross-time content.**

**The forcing argument, written out so the reader need not reconstruct it.** Suppose `F` satisfies
obligation 1, obligation 3 and the substantive target. Let `U`, `U'` be obligation 3's witness pair:
`D_F(U) = D_F(U')` and `D₂(U) ≠ D₂(U')`. The substantive target gives `𝔾(U) ≈_O 𝔾(U')`. Act 12's
merged `twoSidedRelated_iff` says that is exactly `TwoSidedRelated a₀ U U'` — a **time-dependent**
in-fibre left move together with a **weak** right gauge at each time. Act 13's merged `CT2` (b) says
`D₂(U) = D₂(U')` is exactly a **constant** in-fibre left move together with a **strong** right gauge
at each time. So the pair differs by the gap between those two relations, and by nothing else: the
time-dependence of the left factor and the weakening of the right factor. **That gap is the per-time
frame and the per-time anchored phase**, which is what `≈_O` quotients and what act 11's `GL2` and
act 13's `CT3` (G) describe. It is not cross-time content.

**What falsifies `P-D`, said exactly.** `P-D` is falsified by an exhibited `F` on this freeze's list
that reaches the top line of the `D`-axis **together with** an exhibited obligation 3 witness pair
whose two lifts are **not** two-sided related at every time. **Such a pair would contradict act 12's
`twoSidedRelated_iff`**, which is merged, so a falsification here would mean this freeze has misread
a merged result rather than that the round has discovered something. **The round reports it either
way**, and where `P-D` is falsified the result note says in terms which merged statement the freeze
misread and does not present the falsification as a finding about nature.

**What `P-D` is not.** It is **not** a prediction that the top line is reached — that is the `D`-axis
outcome and is predicted separately, per candidate, in the predictions table. It is a prediction
about the **shape** of any `F` that does reach it.

## Type L — a structural law, FROZEN

**A Type L candidate is a constraint on trajectories, writable from `(a₀, Γ)` alone, before any lift
is chosen.** Two definitions are frozen here and used everywhere below.

> **A law datum and a law.** A **law datum** `C` is an object written from `a₀`, `Γ` and the index
> `ℕ` alone — constructed before any lift exists and consulting no lift at any point. `Law(C, ·)` is
> a predicate on Gram/orbit trajectories that is **`≈_O`-invariant**: if `𝔾 ≈_O 𝔾'` then
> `Law(C, 𝔾) ↔ Law(C, 𝔾')`. **A law is POINTWISE** iff there is a family `(c_t)` with
> `Law(C, 𝔾) ≡ ∀ t, c_t(𝔾 t)`.

**The `≈_O`-invariance requirement is the orbit-level well-definedness obligation, and it binds every
Type L candidate.** A constraint stated on representatives that is not invariant under the per-time
phase and frame freedom is not a constraint on the Gram/orbit trajectory at all: it would "select" by
fixing an unphysical frame. Every Type L candidate below carries this obligation, and the generator
law carries it in an explicit and stronger form.

### Non-triviality is witnessed at ONE COMMON CONFIGURATION, FROZEN

> **The one-configuration non-triviality witness.** A Type L candidate is **genuine and proper** at a
> configuration iff there are `C`, and trajectories `G₁`, `G₂`, `H`, **all three pointwise
> realizable at that one configuration**, with
> `Law(C, G₁) ∧ Law(C, G₂) ∧ G₁ ≉_O G₂ ∧ ¬Law(C, H)`.

**What the single witness proves, in one object.** The law's solution set at `C` is **nonempty**
(`G₁` is in it), **non-singleton modulo `≈_O`** (`G₂` is in it and `G₁ ≉_O G₂`), and **proper**
(`H` is pointwise realizable and is not in it). Three properties, one configuration, one witness.

**Why split configurations fail, stated as the reason they do.** Suppose non-emptiness and
non-singularity were witnessed at one configuration and properness at another. Then a law that
permits **everything** at the first configuration and **exactly one** trajectory at the second passes
both separated tests while being **vacuous at the first** — it constrains nothing there — and **the
answer in disguise at the second** — it hands over the trajectory there. Neither failure is visible to
either separated test, because each test looks at the configuration where the other failure does not
occur. **The common configuration is what makes the three properties statements about one and the
same solution set**, and it is why this freeze requires them together.

**`H`'s pointwise realizability is load-bearing, and it is available only because of `TJ1`.** The
properness clause has to exhibit a trajectory the law excludes **from inside the admissible set**; a
trajectory excluded because it is not admissible at all proves nothing about the law. Act 17's `TJ1`
sufficiency is what makes "pointwise realizable" and "is some coherent lift's trajectory" the same
thing, so `H` can be named by its per-slice values and its admissibility discharged from a merged
result. **Without `TJ1` the clause would need a lift constructed by hand at every use.**

### Propagation, FROZEN — two clauses, because the initial orbit has to do work

> **Propagation.** A Type L candidate **propagates** at a configuration iff both:
> **(i) uniqueness from the initial orbit** — any two pointwise realizable solutions of the law whose
> per-slice orbit classes agree at time `0` have the same trajectory under `≈_O`; and
> **(ii) the initial orbit contributes** — there is a time `t ≥ 1` at which the solutions of the law,
> taken **without** fixing the initial orbit, include two `≈_O`-inequivalent per-slice orbit classes.

**Clause (ii) is part of what "propagates" means and is not an extra rung.** "A law plus one initial
orbit propagates uniquely" says the initial orbit does work. A law that fixes every later slice on
its own satisfies clause (i) while the initial orbit contributes nothing, and calling that
propagation would report a slice-by-slice determination as a cross-time relation — which is the
distinction this whole round exists to keep. **Clause (ii) is checked at the same configuration as
the non-triviality witness**, and the result note reports both clauses separately.

## The shared structural theorem, which RUNS FIRST — `XS1`

**This target runs before either ladder**, and both ladders are written so that their candidate lists
depend on its outcome in a way this freeze fixes in advance.

> **`XS1` — pointwise laws factor.** If `Law(C, 𝔾) ≡ ∀ t, c_t(𝔾 t)`, then its solution set is the
> **product over time** of its per-time solution sets: a trajectory solves the law iff each of its
> slices solves the corresponding per-time condition, and any assignment whose slices solve the
> per-time conditions is a solution. **Any uniqueness such a law produces is therefore slice-by-slice
> uniqueness, never a relation propagating one time from another.**

> **The corollary.** Whenever two different allowed orbits survive at **some later time**, fixing the
> initial orbit cannot select between them through a pointwise law. Formally: if `Law(C, ·)` is
> pointwise and `G₁`, `G₂` are pointwise-realizable solutions whose per-slice orbit classes differ at
> some time `t* ≥ 1`, then there is a pointwise-realizable solution `G'` with `G'` agreeing with `G₁`
> at every time other than `t*` and with `G₂` at `t*`; and `G'(0) = G₁(0)` while `G' ≉_O G₁`.

**The hypothesis "at some later time" is load-bearing and is stated rather than assumed.** Two
solutions that differ **only at time `0`** are not spliceable into a counterexample to propagation,
and a pointwise law whose per-time solution sets are singletons modulo `≈_O` at every `t ≥ 1` can
satisfy a uniqueness-from-the-initial-orbit clause — but only because the later slices were already
fixed by the per-time conditions with the initial orbit doing no work at all. **That degenerate case
is what the second clause of the propagation definition below excludes**, and the two are frozen
together for exactly that reason.

**`XS1` leans on `TJ1`, and the freeze says where.** Intersecting a product constraint with a
non-product ambient set need not factor: the splice of two solutions is a solution **of the law**
immediately, but it has to be **admissible** as well, and that is what act 17's `TJ1` supplies. `TJ1`
proves the admissible set **is** the product of the per-slice realizable sets, so the intersection of
two products is a product and the splice stays inside it. **Without `TJ1` the corollary does not
follow**, and the execution cites `TJ1` at exactly that step.

### What `XS1` is NOT, stated in terms

**`XS1` is not "no pointwise constraint yields cross-time determination", and that sentence is
FALSE.** A pointwise `c_t` whose solution set at every `t` is a single orbit class determines the
trajectory outright, slice by slice, with no initial condition needed. **What fails is propagation,
not determination.** A pointwise law can pin the trajectory; what it cannot do is let one time's value
constrain another's. Any artifact of this round that writes the false sentence, in any paraphrase, is
defective.

**And the pointwise law that determines slice by slice earns no line of the `L`-axis either**, for a
different reason: its solution set is a single class modulo `≈_O`, so the one-configuration
non-triviality witness fails at its non-singleton clause. **That is a failure of non-triviality and
not a failure of determination**, and the result note says which.

### The `XS1` dependency, FROZEN IN BOTH DIRECTIONS

> **If `XS1` lands, every pointwise candidate is ruled out as a route to the top line of the `L`-axis
> AS A THEOREM OF THIS ROUND** — not left UNDECIDED, and not recorded as a failed search. **The
> argument is exhaustive over the two cases and both are closed.** If clause (ii) of propagation
> holds for a pointwise law, two inequivalent orbit classes survive at a time `t ≥ 1`, the splice of
> the corollary is a pointwise realizable solution agreeing at time `0` and inequivalent, and clause
> (i) fails. If clause (ii) fails, the law's later slices are fixed by the per-time conditions alone
> and the initial orbit contributes nothing, so it does not propagate in the frozen sense. **Either
> way the top line is unreachable for a pointwise law.** The exclusion is bounded to **the notion of
> law this freeze defines**: a law datum written from `(a₀, Γ)` and the index alone, an
> `≈_O`-invariant predicate on trajectories, and pointwise in the frozen sense. It is **not** a
> statement about every conceivable pointwise condition, **not** a statement about laws on any other
> object, and **not** a bound on what a later round could prove under a different notion of law.
>
> **If `XS1` does not land, the pointwise candidates stay live** and the `L`-ladder runs against the
> **full** candidate list, `LC0` included, under its own unchanged evidence bar. Nothing about the
> other candidates changes in either case.

**Where this leaves the `L`-list.** With `XS1` landed, `LC0` is excluded from the top line by this
round's own theorem and is reported as excluded, with its middle-line standing reported on its own
merits; the remaining candidates run unchanged. Without `XS1`, all four run unchanged.

## The frozen candidate list

**Four Type L candidates and three Type D candidates. The list is closed at this freeze.** Each is
stated as a proposition in the programme's vocabulary, with its provenance named and its type fixed.
A candidate discovered during execution is **recorded as an observation and not executed**, and
belongs to a later round with its own freeze.

### `DF1` — adjacent-pair cross-Gram, Type D

> **Statement.** `F₁(U) := fun i t => FibreCrossGram a₀ U i t (t+1)` — the fibre cross-Gram at
> **adjacent time pairs only**, every fibre, every `t`. Pairs `(t, s)` with `s ≠ t+1` are withheld.

**Where it comes from.** It is the leanest cross-time datum act 13's level-2 family contains: one
step of memory and no more. **Its type is D and does not change.**

**A recorded reason, and a predicted obstruction.** At `|A| = 1` the anchored fibre columns are
single row vectors of unit norm, so `Ξ_i^{(t,s)}` is a rank-one outer product and
`Ξ_i^{(t,t+1)} · Ξ_i^{(t+1,t+2)} = Ξ_i^{(t,t+2)}` identically, the middle factor being `∑_j Γ_{ij}`,
which is `1` at `|A| = 1` because the row `(i, a₀)` of a unitary lift has unit norm and the ancilla
index contributes a single term. **At `|A| = 1` the adjacent-pair data therefore determine the whole
of `D₂` by matrix multiplication**, and obligation 3 cannot be witnessed at act 12's Hadamard
configuration.
This is written here as the freeze's **reason** for predicting `DF1` obligation 3 at `|A| = 2`, and it
is **analysis, not a finding**: whether it holds is for the execution to prove or to refute, and no
target of this round rests on it.

### `DF2` — diagonal cross-time overlaps, Type D

> **Statement.** `F₂(U) := fun i t s j => FibreCrossGram a₀ U i t s j j` — the **diagonal** entries
> of the fibre cross-Gram at every time pair, the entries where the two column indices coincide. The
> off-diagonal entries `j ≠ k` are withheld.

**Where it comes from.** It is the cross-time analogue of act 12's `SH1` reading: the visible law is
exactly the diagonal of the Gram data, and this candidate asks what the diagonal of the **cross-time**
data supplies. At `t = s` it returns `D₀` and nothing more, by `fibreCrossGram_diag` and
`fibreGram_diag`; at `t ≠ s` it carries genuine cross-time content. **Its type is D and does not
change.**

### `DF3` — cross-time anchor coherence, Type D

> **Statement.** `F₃(U) := fun t s => ∑ i, FibreCrossGram a₀ U i t s` — the anchored block of the
> column cross-Gram at every time pair, which act 13's `sum_fibreCrossGram` identifies with the fibre
> sum of level 2. It is act 13's **level 1**, strictly between level 0 and level 2 on that family.

**Where it comes from, and the anchor grounding.** Act 10 reclassified the anchor axis as **not
resolved**, with the upstream anchor choice named as the live remainder. This datum is defined only
relative to the anchoring convention: it is the mutual coherence of the **anchored** columns at two
times, and its very statement moves if the convention moves. Freezing it as a candidate is how this
round asks whether cross-time anchor coherence is the intermediate datum, **without** asserting
anything about the anchor axis: no outcome of `DF3` resolves, reopens, narrows or bears on act 10's
reclassification in either direction, and the result note says so where it reports `DF3`. **Its type
is D and does not change.**

### `LC0` — a pointwise admissibility law, Type L

> **Statement.** `Law(C, 𝔾) ≡ ∀ t, c_t(𝔾 t)` for a family `(c_t)` of conditions on per-slice orbit
> classes written from `(a₀, Γ t)` alone.

**Where it comes from.** It is the pointwise archetype, and it is the object `XS1` is about. It is
frozen as a candidate so that `XS1`'s consequence for it is reported as a verdict on a named
candidate rather than as an aside. **Its type is L and does not change.**

### `LC1` — cross-time anchor coherence as a law, Type L

> **Statement.** There is a family `C = (C_t)` of `V × V` complex matrices written from
> `(a₀, Γ t, Γ (t+1))` alone, and `Law(C, 𝔾)` holds iff at every `t` the classes `[𝔾 t]` and
> `[𝔾 (t+1)]` admit representatives realized by admissible dilations `U_t` of `Γ t` and `U_{t+1}` of
> `Γ (t+1)` whose anchored cross-time coherence `∑ i, X_i(U_t)ᴴ X_i(U_{t+1})` equals `C_t`.

**Where it comes from, and why it is a SEPARATE candidate from `DF3`.** Cross-time anchor coherence
is frozen as **two candidates**, `DF3` of Type D and `LC1` of Type L, so that neither can drift type
mid-execution. `DF3` **reads** the coherence off a lift that already exists; `LC1` **prescribes** it
from `(a₀, Γ)` before any lift is chosen. They are different propositions with different obligations
and different ladders, and a verdict on one is not a verdict on the other in either direction. Both
are grounded in act 10's reclassified anchor axis and neither bears on it. **`LC1`'s type is L and
does not change.**

**The existential over representatives is what makes `LC1` a condition on classes**, and it is how
`LC1` discharges the `≈_O`-invariance obligation: the condition asks that *some* representatives
realize `C_t`, so it cannot distinguish two representatives of one class.

### `LC2` — regularity in a Gram metric, Type L

> **Statement.** For a pseudometric `d` on per-slice orbit classes, **named explicitly in the
> statement** and written from the Gram data alone, and a bound `ε_t` written from
> `(Γ t, Γ (t+1))` alone: `Law(C, 𝔾) ≡ ∀ t, d([𝔾 t], [𝔾 (t+1)]) ≤ ε_t`.

**Where it comes from, and why it is kept apart from the data-reading candidates.** "The trajectory
does not jump" is the oldest regularity idea in the programme's neighbourhood, and it is **an axiom,
not a readback**: nothing reads `d` off anything, and the constraint is imposed before any lift
exists. It is frozen as Type L for that reason and is not paired with a Type D twin. **Its type is L
and does not change.**

**Two things `LC2` does not import.** It does not import continuity, differentiability or a limit:
`ℕ` carries successor and order and nothing else, and `d` is a pseudometric on the **value** space,
not on the index. And it does not import a canonical `d`: the pseudometric is named in the statement
and the verdict is about that named `d`, not about regularity in general.

### `LC3` — a generator law, Type L, WITH A DESCENT OBLIGATION

> **Statement.** `U(t+1) = V_t · U(t)` with `V_t` depending only on `(Γ t, Γ (t+1))` — a law of
> evolution written from the visible family before any lift exists.

> **The descent obligation, which is part of the candidate and not a commentary on it.** `LC3` is
> executed **either** written directly as an orbit-level transition
> `[G_{t+1}] = Φ_{Γ_t, Γ_{t+1}}([G_t])`, **or** with the representative-level `V_t` proved
> **gauge-natural** and shown to **descend** to such a `Φ`. Without one of the two, the candidate is
> reported UNDECIDED with the descent obligation named as the obstruction, and **no verdict about
> propagation is recorded for it**.

**Why the descent obligation is load-bearing.** A representative-level generator that does not
descend "selects" by fixing an unphysical frame: it would pick out one lift inside an orbit and then
report that the orbit trajectory is determined, when what was determined is the frame. **This is the
same well-definedness question acts 11 and 12 already formalized for the two-sided invisible gauge**,
so it can be discharged against existing results — act 12's `fibreGram_left_mul` and
`fibreGram_mul_weak_apply` and act 11's orbit theorem are what a gauge-naturality proof would run
through — and the execution discharges it there rather than inventing a new notion.

**And a law of this shape legitimately determines the trajectory GIVEN an initial condition.** That
is what a law of evolution **is**, and it is not a cheat here, because `V_t` is writable from `Γ`
before any lift exists: nothing about the history is read in order to state it. The one-configuration
non-triviality witness is what keeps it honest — the law must still have two inequivalent solutions
and still exclude something realizable — and the initial orbit is an input the axis names explicitly
in its top line. **Its type is L and does not change.**

## The witness supply, FROZEN

**Every witness of this round is drawn from this supply, and the configuration for each obligation is
named in the countercontrol table below, in advance.** A configuration chosen after an outcome is
known is a preregistration failure in miniature, and an alternative witness found during execution is
**recorded as an observation and never substituted**.

1. **Act 12's Hadamard objects** at `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼`, with the frozen
   family `H(z) = ½ · [[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]` and the merged admissibility
   and inequivalence of `H(1)` and `H(i)`. Act 17's `hadamard_constant_lifts` supplies the two
   constant coherent lifts.
2. **The piecewise-Hadamard lifts.** For `S ⊆ ℕ`, `U_S(t) := H(i)` if `t ∈ S` and `H(1)` otherwise.
   Each is a coherent lift of `Γ ≡ ¼` because each slice is admissible, which is merged; and
   `U_S ≈_O U_{S'}` iff `S = S'`, by act 12's `∼_D`-invariant at each time.
3. **Act 12's `sh1_sufficiency` and act 17's `tj1_sufficiency`**, which realize any pointwise
   realizable tuple and any pointwise realizable assignment by an admissible dilation and by a
   coherent lift respectively, at any finite `|A|` satisfying the rank bound. This is what supplies
   witnesses outside `|A| = 1` without a new hand-built matrix, and what supplies `H` in the
   one-configuration non-triviality witness.
4. **The moves of acts 11, 12 and 13**: the constant and time-dependent in-fibre left moves of
   `LeftFibreGroup`, and the strong and weak right gauges at `a₀`, with their merged transformation
   laws on `FibreGram` and on `FibreCrossGram`.

**The one-`|A|`-value caveat, recorded.** Act 12's `|A| = 1` is the strongest case for the per-slice
statements and is not degenerate there. **It is not automatically the right case for a cross-time
statement**, and the `DF1` reason above is the concrete instance: at `|A| = 1` the adjacent-pair data
may collapse onto the whole of level 2. Where a countercontrol needs `|A| ≥ 2` the table says so, and
the witness comes from supply item 3.

## The countercontrols, one per obligation

**A negative result is reportable because its shape was fixed before the search.** For each candidate
the freeze states here what a negative answer looks like concretely and what evidence earns it.

**Evidence that earns any countercontrol**: a Lean theorem at evidence level 2 whose statement pins
the objects by equations, discharges coherence from merged results, and certifies the separating
quantity at a named index through a named invariant. **Searching and not finding earns nothing.**

| candidate | obligation | the countercontrol this freeze names | configuration |
| --- | --- | --- | --- |
| `DF1` | 1 | none needed: `F₁` is a restriction of `D₂`, so equality of `D₂` gives equality of `F₁` by congruence | any |
| `DF1` | 2 | the two constant Hadamard lifts `H(1)` and `H(i)`: both coherent lifts of `Γ ≡ ¼`, so `D₀` agrees, and `Ξ_i^{(t,t+1)}` is the fibre-Gram tuple for each, which act 12 proves not even phase-equivalent | supply 1 and 2, `\|A\| = 1` |
| `DF1` | 3 | a pair agreeing at every adjacent pair and differing at one non-adjacent pair, built at `\|A\| = 2` from supply 3; the `\|A\| = 1` collapse recorded above is the reason the table names `\|A\| = 2` here | supply 3, `\|A\| = 2` |
| `DF2` | 1 | none needed: `F₂` is a restriction of `D₂` | any |
| `DF2` | 2 | `U_∅` against `U_{\{1\}}` at `(t, s) = (0, 1)`, fibre `1`, column `1`: the diagonal overlap is `¼` for one and `¼ i` for the other | supply 1 and 2, `\|A\| = 1` |
| `DF2` | 3 | the two constant Hadamard lifts `H(1)` and `H(i)`: every entry of each has modulus `½`, so the diagonal cross-time overlap is the constant `¼` at every `(i, t, s, j)` for both and `F₂` agrees, while `D₂` differs already at `(t, s) = (0, 0)`, where `fibreCrossGram_diag` returns the fibre-Gram tuples act 12 proves inequivalent | supply 1 and 2, `\|A\| = 1` |
| `DF2` | determination | the same pair: `F₂` and `D₀` agree while the trajectories are `≈_O`-inequivalent at every time, through act 12's merged `∼_D`-invariant `G^{(0)}_{10} · G^{(1)}_{01}` | supply 1 and 2, `\|A\| = 1` |
| `DF3` | 1 | none needed: `F₃` is the fibre sum of `D₂`, by `sum_fibreCrossGram` | any |
| `DF3` | 2 | `U_∅` against `U_{\{1\}}` at `(t, s) = (0, 1)`: the anchored block is the identity for one and `H(1)ᴴ H(i) ≠ 1` for the other | supply 1 and 2, `\|A\| = 1` |
| `DF3` | 3 | **named and expected hard**: a pair agreeing on the fibre sum and differing fibre by fibre, with the visible family held equal. The freeze names no construction and rates it accordingly; **UNDECIDED with the obstruction named is an allowed outcome and is not a shortfall** | supply 3 |
| `LC0` | non-triviality | `C` the condition "the class at `t` is one of `[G(H(1))]`, `[G(H(i))]`"; `G₁` constant at the first, `G₂` constant at the second, `G₁ ≉_O G₂` merged; `H` constant at `[G(H(-1))]`, pointwise realizable and excluded | supply 1 and 3, `\|A\| = 1` |
| `LC1` | non-triviality | `C_t := 1` at every `t`; `G₁` and `G₂` the two constant Hadamard trajectories, each realized by a constant lift whose anchored coherence is the identity; `H` the alternating trajectory, excluded if no admissible representatives give the identity | supply 1, 2 and 3, `\|A\| = 1` |
| `LC2` | non-triviality | `d` the named pseudometric and `ε` below `d([G(H(1))], [G(H(i))])`; `G₁`, `G₂` the two constant trajectories, both with zero steps; `H` the alternating trajectory, whose steps exceed `ε` | supply 1, 2 and 3, `\|A\| = 1` |
| `LC3` | descent | discharged by writing the candidate directly at orbit level as `Φ`, or by a gauge-naturality proof through act 12's `fibreGram_left_mul` and `fibreGram_mul_weak_apply` | any |
| `LC3` | non-triviality | `Φ` the identity on orbit classes; `G₁`, `G₂` the two constant trajectories, both solutions, inequivalent; `H` the alternating trajectory, excluded because the identity transition forbids a change of class | supply 1, 2 and 3, `\|A\| = 1` |

**One witness family, several consequences — reported as one witness and its consequences.** Act
12's Hadamard objects carry most of the table. The execution reports that as **one merged witness
family and the consequences this round draws from it**, and never as several independent findings.

**The countercontrols consume merged witnesses; they do not enlarge them.** Act 12's `TG3` is
existential about its own exhibited dilations, act 12's `SH1` is the per-slice characterization at
its own strength, and act 13's `CT2` (b) is consumed at merged strength. None is enlarged, restated
or revised by anything here.

## The evidence rule, FROZEN

`XS0` is settled by **locating and quoting**, not by proving a theorem. Its evidence rule is frozen
here and binds the execution:

1. Evidence is a **verbatim quotation** from a pinned blob, with its file path and line coordinate;
   or
2. a **verbatim quotation** from a merged result note or preregistration, with its coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist** on the record
   searched, with the search **named and bounded** — the file set enumerated, the search terms
   listed, and the result recorded for each term.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the record must
contain X, because otherwise Y would not have been written" may appear only in a clearly labelled
analysis paragraph that states it is not evidence and that no target rests on it. **Where the record
is silent, the finding is that it is silent** — not that the thing sought is false, and not that it
is true. **Silence is a finding.**

**Searching and not finding is never a settling outcome.** This binds the Lean targets as well as
`XS0`. No line of either ladder is earned by the absence of a witness: a bounded no-go requires an
**exhibited** failure per candidate and is **not** earned by a failed search, which belongs at
UNDECIDED with the obstruction named. The same rule forbids concluding that a candidate satisfies an
obligation because no counterexample was found.

**The bounded search for `XS0` is fixed now**, so that its boundary cannot be chosen after its result
is known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/` and under
  `verification/lean/`; every `preregistration.md` and `result.md` under
  `verification/programmes/oi-qm/`; and `verification/ROADMAP.md`. The set is taken from
  `git ls-tree -r --name-only B`, so untracked package trees are outside it by construction.
- **The search terms**: `FibreCrossGram`, `CrossGram`, `GramTrajEquiv`, `RealizableGram`,
  `CoherentLift`, `propagat`, `transition`, `generator`, `regular`, `metric`, `coarse`, `refine`,
  `intermediate`, and the merged label names `TJ1`, `TJ3`, `CT2`, `CT3`, `SH1`, `TG2`, `TG3`, `GL2`.
- **The question asked of each hit**: does this declaration decide, for any datum strictly between
  the anchored readback and act 13's level-2 datum, whether it determines the Gram/orbit trajectory —
  or does it decide, for any constraint writable from `(a₀, Γ)` alone, whether that constraint is
  proper, non-trivial or propagating?
- **The recorded answer per hit** is one of: *supplies it* (quoted, with coordinate); *does not
  supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

The execution records the search in the result note in full. **A search that finds a decision is a
finding, and a search that does not is equally a finding** — the second being that the record is
silent on the point, which is what `XS0` asks.

## The targets, FROZEN

Six targets, `XS0` through `XS5`. Each names what settles it and what evidence counts.

### `XS0` — does the merged record decide the interval question, in either direction?

**The question.** At this freeze's base, does the merged record contain any statement — universal or
existential — deciding, for any datum strictly between the anchored readback and act 13's level-2
datum, whether it determines the Gram/orbit trajectory; or deciding, for any constraint writable from
`(a₀, Γ)` alone, whether it is proper, non-trivial or propagating?

**What settles it.** The bounded search frozen above, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule if a decision is found. Rule 3 if none is
found — the recorded statement that the passage sought does not exist on the named and bounded
search, with the per-term record.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `XS0`**, and no outcome of `XS0` is a theorem
of this round. **Nor is it a licence to treat this round's own theorems as retro-evidence about it.**

### `XS1` — the factorization theorem for pointwise laws

**The statement.** As frozen above: a pointwise law's solution set is the product over time of its
per-time solution sets, with the splicing corollary, and with `TJ1` cited at the step where the
ambient set has to be a product.

**What settles it.** A Lean theorem at evidence level 2, consuming act 17's merged `tj1_sufficiency`
and `tj1_trajectory_set` and act 12's `SH1` at their own strengths.

**Bounded reading, frozen.**

- **It is about propagation, not about determination.** A pointwise law with a unique solution at
  every time determines the trajectory, and `XS1` says so rather than denying it.
- **It is bounded to the notion of law this freeze defines**, and is not a statement about every
  conceivable pointwise condition on any object.
- **It is not a no-go about this round's other candidates.** `LC1`, `LC2` and `LC3` are not
  pointwise, and `XS1` says nothing about them in either direction.
- **The `TJ1` dependence is named at the step, not in a footnote.** Intersecting a product constraint
  with a non-product ambient set need not factor, and it is act 17 that proved the admissible set is
  the product.

### `XS2` — the Type D per-candidate obligations and the `D`-determination target

Three parts, predicted and reported separately: `XS2` (a) `DF1`, (b) `DF2`, (c) `DF3`. Each part
carries obligations 1, 2 and 3 and the substantive `D`-determination target, each reported with its
own frozen label.

**The frozen verdict labels for a Type D candidate `X`, exhaustive per obligation.**

| label | what it says | earned only by |
| --- | --- | --- |
| `X-SANDWICH` | all three obligations hold: `X` is a genuine intermediate datum, strictly above the visible data and strictly below level 2 | a kernel proof at evidence level 2 of obligation 1 universally, and of obligations 2 and 3 by exhibited pairs with the separating index and quantity named |
| `X-NOT-ABOVE` | obligation 2 fails: `X` adds nothing to the visible data | a **universal** kernel proof at evidence level 2 that `D₀` equality implies `D_F` equality |
| `X-NOT-BELOW` | obligation 3 fails: `X` recovers the whole of level 2 | a **universal** kernel proof at evidence level 2 that `D_F` equality implies `D₂` equality |
| `X-DET` | the substantive target holds: equal `D_F` implies `≈_O` | a **universal** kernel proof at evidence level 2 over every finite carrier, anchor, visible family and pair of lifts |
| `X-RESID` | the substantive target fails: residual trajectory freedom remains | a kernel proof at evidence level 2 exhibiting two lifts with equal `D_F` and `≈_O`-inequivalent trajectories, the separating time and invariant named |
| UNDECIDED | neither was reached for the named obligation | the recorded statement that neither was reached, with the obstruction named — which candidate, which obligation, which step, and what would settle it |

**What no `XS2` verdict establishes.** A verdict on one candidate is not a verdict on another. An
`X-SANDWICH` is not an endorsement: it says the datum sits in the interval, and says nothing about
whether it is the right datum. An `X-DET` is not an adoption. An `X-NOT-BELOW` is not a criticism of
the candidate — it is the finding that the candidate is act 13's datum in another coat, which is
worth recording and is what obligation 3 exists to detect.

### `XS3` — the Type L per-candidate obligations

Four parts, predicted and reported separately: `XS3` (a) `LC0`, (b) `LC1`, (c) `LC2`, (d) `LC3`. Each
part carries the `≈_O`-invariance obligation, the one-configuration non-triviality witness and — for
`LC3` — the descent obligation, plus the propagation question.

**The frozen verdict labels for a Type L candidate `Y`, exhaustive per obligation.**

| label | what it says | earned only by |
| --- | --- | --- |
| `Y-WELLDEF` | the `≈_O`-invariance obligation is discharged | a kernel proof at evidence level 2 that the predicate respects `GramTrajEquiv` |
| `Y-PROPER` | the one-configuration non-triviality witness lands: nonempty, non-singleton modulo `≈_O`, and proper, all three at one configuration | a kernel proof at evidence level 2 of the four-conjunct statement with `G₁`, `G₂`, `H` pinned by equations and all three pointwise realizable |
| `Y-VACUOUS` | the properness clause fails: the law excludes no pointwise realizable trajectory at the named configuration | a **universal** kernel proof at evidence level 2 over the pointwise realizable trajectories there |
| `Y-SINGLE` | the non-singleton clause fails: the law's solution set at the named configuration is one class modulo `≈_O` | a **universal** kernel proof at evidence level 2 of that uniqueness |
| `Y-PROPAGATES` | given the non-triviality witness, **both** propagation clauses hold: solutions agreeing at time `0` are `≈_O`, and the law without the initial orbit leaves two inequivalent classes at some `t ≥ 1` | a **universal** kernel proof at evidence level 2 of clause (i) over the pointwise realizable solutions, together with an exhibited witness for clause (ii) |
| `Y-RESID` | propagation clause (i) fails: two solutions agree at time `0` and are `≈_O`-inequivalent | a kernel proof at evidence level 2 exhibiting both, with the separating time and invariant named |
| `Y-DEGENERATE` | propagation clause (ii) fails: the law fixes every slice from `t = 1` on by itself, so the initial orbit contributes nothing | a **universal** kernel proof at evidence level 2 that the solution set at every `t ≥ 1` is one class modulo `≈_O` |
| UNDECIDED | neither was reached for the named obligation | the recorded statement that neither was reached, with the obstruction named |

**What no `XS3` verdict establishes.** A verdict on one candidate is not a verdict on another. A
`Y-PROPAGATES` is not an adoption and is not a claim that the law obtains: it says what imposing that
law leaves. A `Y-VACUOUS` or `Y-SINGLE` is a verdict at the **named** configuration and is not a
statement about every configuration.

### `XS4` — the `D`-axis outcome

**The axis, stated once and reported in the status rule's frozen wording.**

| line | outcome | statement | earned only by |
| --- | --- | --- | --- |
| top | **`D-DET`** | a genuine intermediate datum determines the Gram trajectory | a named candidate with `X-SANDWICH` **and** `X-DET`, both at evidence level 2 |
| middle | **`D-MID`** | a genuine intermediate datum exists but residual trajectory freedom remains | a named candidate with `X-SANDWICH` **and** `X-RESID`, both at evidence level 2 |
| bounded no-go | **`D-NOGO`** | no candidate on this freeze's Type D list is a genuine intermediate datum | for **every** candidate on the list, an exhibited failure of obligation 2 or of obligation 3, each at evidence level 2, with the failing obligation named per candidate |
| otherwise | **`D-UNDECIDED`** | none of the above was reached | the recorded statement that none was reached, with the obstruction named specifically — which candidate, which obligation, which step, what would settle it |

**`D-DET` and `D-MID` are mutually exclusive and jointly exhaustive once a candidate reaches
`X-SANDWICH`**, and the outcome is whichever the kernel carries. **`D-NOGO` is bounded to this
freeze's three-member list** and is not a statement that no intermediate datum exists.

### `XS5` — the `L`-axis outcome

| line | outcome | statement | earned only by |
| --- | --- | --- | --- |
| top | **`L-PROP`** | a genuine proper law plus one initial orbit propagates uniquely | a named candidate with `Y-WELLDEF`, `Y-PROPER` and `Y-PROPAGATES`, all at evidence level 2, and for `LC3` with the descent obligation discharged |
| middle | **`L-PROPER`** | a genuine proper cross-time constraint, and it does not propagate — either residual histories remain after the initial orbit is fixed (`Y-RESID`), or the initial orbit contributes nothing because the law fixes every later slice by itself (`Y-DEGENERATE`) | a named candidate with `Y-WELLDEF` and `Y-PROPER` and either `Y-RESID` or `Y-DEGENERATE`, all at evidence level 2, **the two mechanisms kept apart and named**: reporting one as the other is a defect |
| bounded no-go | **`L-NOGO`** | no candidate on this freeze's Type L list is a genuine proper law | for **every** candidate on the list, an exhibited `Y-VACUOUS` or `Y-SINGLE` or a discharged exclusion, each at evidence level 2, with the failing clause named per candidate |
| otherwise | **`L-UNDECIDED`** | none of the above was reached | the recorded statement that none was reached, with the obstruction named specifically |

**Where `XS1` landed, `LC0`'s exclusion from `L-PROP` is a theorem of this round** and is reported as
one, under `XS1` and under `XS3` (a), and never as an undecided line. **It does not by itself earn
`L-NOGO`**, which quantifies over the whole list.

**Neither axis is above the other.** The outcome of the round is the ordered pair `(XS4, XS5)`, and
no artifact of this round writes a sentence ranking one against the other.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `XS0` | **negative** — the record is silent on the interval and on propagation | **high** | A pre-freeze reading of the file set named in the evidence rule found act 12's and act 13's statements to be about the poles — per-slice realizability at one end, the level-2 determination at the other — and act 17's to be about the visible-data class and about the absence of a universal coupling. Nothing addresses a datum strictly between them, and nothing states a law of the frozen shape. The reading is the freeze's **reason**, not a finding: `XS0`'s finding is whatever the execution's own bounded search records. |
| `XS1` | positive | **high** | The factorization is immediate from the shape of `∀ t, c_t(𝔾 t)`, and the corollary's splice stays admissible by act 17's merged `tj1_trajectory_set`. No new construction is required. |
| `XS2` (a) `DF1` obligations 1, 2 | **`DF1`** obligations 1 and 2 hold | **high** | Obligation 1 is congruence on a restriction. Obligation 2 is act 12's merged inequivalence read at one adjacent pair on the two constant Hadamard lifts, where the adjacent-pair datum is the fibre-Gram tuple itself. |
| `XS2` (a) `DF1` obligation 3 | not predicted | **low** | The `|A| = 1` collapse recorded above means the frozen Hadamard configuration cannot supply it, and the `|A| = 2` construction from `sh1_sufficiency` is not built by any merged result. **UNDECIDED with the obstruction named is an allowed outcome and is the freeze's expectation.** |
| `XS2` (b) `DF2` obligations 1, 2, 3 | **`DF2-SANDWICH`** | **high** | Obligation 1 is congruence on a restriction. Obligation 2 is the merged inequivalence read at the entry `(1, 1)` of the `(0, 1)` overlap of the piecewise pair. Obligation 3 is the two constant Hadamard lifts: every entry has modulus `½`, so both diagonal cross-time overlaps are the constant `¼`, while the level-2 data differ already at `(t, s) = (0, 0)` by act 12's merged inequivalence. |
| `XS2` (b) `DF2` determination | **`DF2-RESID`** | **high** | The same constant pair has equal augmented datum and `≈_O`-inequivalent trajectories, through act 12's merged `∼_D`-invariant. Withholding the off-diagonal entries withholds exactly the residual act 12's `SH1` identifies as the whole of the freedom after the two-sided gauge, so the datum is informative across time and still does not determine the trajectory. |
| `XS2` (c) `DF3` obligations 1, 2 | hold | **high** | Obligation 1 is act 13's merged `sum_fibreCrossGram`. Obligation 2 is the anchored block differing between the two constant Hadamard lifts at one time pair. |
| `XS2` (c) `DF3` obligation 3 | not predicted | **low** | The freeze names no construction separating the fibre sum from the per-fibre data at equal visible family, and the merged record supplies none. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `XS3` (a) `LC0` | **`LC0-PROPER`**, and **excluded from `L-PROP` by `XS1`** | **high** for the properness, **high** for the exclusion conditional on `XS1` | The three-trajectory witness is built from act 12's Hadamard family and act 17's `tj1_sufficiency`. The exclusion is the frozen `XS1` dependency and is a theorem of this round wherever `XS1` lands. |
| `XS3` (b) `LC1` | not predicted | **low** | Whether the alternating trajectory is excluded turns on whether some pair of admissible representatives realizes the prescribed coherence, which no merged result decides. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `XS3` (c) `LC2` | **`LC2-PROPER`** and **`LC2-RESID`** | **medium** | Both constant trajectories have zero steps and satisfy the bound; the alternating trajectory's step is the merged inequivalence and exceeds a bound chosen below it. Propagation clause (ii) holds, the solution set at every later time containing both constant classes. Clause (i) is predicted to fail because the solutions reachable from a fixed initial class form a metric ball and the realizable set at `Γ ≡ ¼` contains the whole `H(z)` family, so the ball is predicted not to be one class; the medium rating is for the kernel computation of the named pseudometric on that family, not for the shape of the argument. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `XS3` (d) `LC3` descent | discharged | **high** | Writing the candidate directly at orbit level as `Φ` discharges it, and the freeze permits that route explicitly. |
| `XS3` (d) `LC3` | **`LC3-PROPER`** and **`LC3-PROPAGATES`** | **medium** | With `Φ` the identity the two constant Hadamard trajectories are inequivalent solutions and the alternating trajectory is excluded, which is the non-triviality witness; solutions agreeing at time `0` agree at every time, which is propagation clause (i); and the solutions without the initial orbit fixed occupy both constant classes at every later time, which is clause (ii), so the initial orbit does work. The medium rating is for the bookkeeping of stating `Φ` at orbit level, not for the argument. **This candidate's stationary instance is the same proposition act 17 refuted as a SELECTOR (`SP2-ADD`, `SP2-NOSEL`), and the two verdicts are consistent**: act 17 showed it is additional structure that does not select from the visible family alone, and this round asks what it does as additional structure with an initial orbit supplied. |
| `XS4`, the `D`-axis | **`D-MID`**, via `DF2` | **medium** | Conditional on `DF2-SANDWICH` and `DF2-RESID` landing as predicted, in which case a genuine intermediate datum is exhibited and residual trajectory freedom remains at it. The medium rating is for the kernel computation that the diagonal cross-time overlap is the constant `¼` at every index for both constant Hadamard lifts, not for the argument. `D-NOGO` is **not** predicted, because it requires an exhibited failure for **every** candidate and the freeze predicts obligation failures for none. If `DF2` obligation 3 does not land, the axis falls to **`D-UNDECIDED`**, and that branch is rated **not predicted, at low-to-medium**. |
| `XS5`, the `L`-axis | **`L-PROP`**, via `LC3` | **medium** | Conditional on `LC3`'s descent and non-triviality landing as predicted. **This is a positive prediction and it is the freeze's whole position on the `L`-axis.** The medium rating is for the orbit-level statement of `Φ`. If `LC3` is UNDECIDED, `LC2` is predicted to carry the axis to **`L-PROPER`**, and the axis outcome falls there. |
| the headline pair | **(`D-MID`, `L-PROP`)** | **medium** | The composition of the two rows above. **The pair is the prediction**, and neither element is predicted as the round's answer on its own. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

**What this table's shape says, stated plainly.** The freeze predicts, at medium, that the interval
between act 17's visible data and act 13's datum is **inhabited** and that what inhabits it there
does **not** determine the trajectory, while a generator law written at orbit level reaches the top
of the `L`-axis. **That asymmetry is the freeze's substantive position**: a law of evolution supplies
cross-time information cheaply and legitimately, because it is writable before any lift exists, while
a readback datum strictly between the two poles carries cross-time content without carrying enough of
it. The round is worth running because that position is testable, because the `D`-axis top line and
the `L`-axis no-go are both preregistered as reachable, and because the freeze rates its own position
at medium and not higher.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached. The
wording is fixed before the round runs so that no outcome can choose its own wording. **UNDECIDED is
a live preregistered outcome for every target and is not a failure**; where it is reached the frozen
sentence below is the report, with the obstruction named.

### The outcomes of `XS0`

- **Outcome `XS0`-silent** — the bounded search records that the passage sought does not exist:
  > On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
  > `verification/lean/`, every `preregistration.md` and `result.md` under
  > `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
  > the merged record decides nothing about a datum strictly between the anchored readback and act
  > 13's level-2 datum, and nothing about whether a constraint writable from the anchor and the
  > visible family alone is proper, non-trivial or propagating. **The finding is that the record is
  > silent on the point.** It is not a finding that any such statement is false, not a finding that
  > one is unprovable, and not a bound on what a later round could prove.
- **Outcome `XS0`-found** — the search locates a deciding statement:
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which objects.
  > Whether that statement settles either axis is the axis's own question and is not settled by
  > locating it. No merged artifact is edited, and no earlier round's recording is enlarged or
  > corrected.

### The outcomes of `XS1`

- **Outcome `XS1`-landed:**
  > A law that is pointwise in this freeze's sense has a solution set equal to the **product over
  > time** of its per-time solution sets, at evidence level 2, the ambient admissible set being a
  > product by act 17's merged `TJ1`. **Any uniqueness such a law produces is slice-by-slice
  > uniqueness and never a relation propagating one time from another**, and whenever two different
  > allowed orbits survive at some later time, fixing the initial orbit cannot select between them
  > through a pointwise law. **This is not the statement that no pointwise constraint yields
  > cross-time determination**, which is false: a pointwise condition with a unique solution at every
  > time determines the trajectory slice by slice, and what fails is propagation, not determination.
  > **Every pointwise candidate is thereby ruled out as a route to the top line of the `L`-axis, as a
  > theorem of this round and not as a failed search.** The exclusion is bounded to the notion of law
  > this freeze defines and is not a statement about every conceivable pointwise condition, not a
  > statement about laws on any other object, and not a bound on what a later round could prove under
  > a different notion of law.
- **Outcome `XS1`-UNDECIDED:**
  > The factorization was not reached in the kernel, with the obstruction named. **The pointwise
  > candidates therefore stay live** and the `L`-ladder runs against the full frozen candidate list
  > under its own unchanged evidence bar. Act 17's `TJ1` stands as act 17 states it and nothing is
  > claimed from it here.

### The outcomes of `XS2`, per candidate and per obligation

- **Outcome `X-SANDWICH`**, for a named Type D candidate `X`:
  > The candidate named `X` in this round's frozen list is a **genuine intermediate datum** at
  > evidence level 2: equality of act 13's level-2 datum implies equality of the augmented datum,
  > universally; two exhibited lifts share the anchored readback and differ in the augmented datum;
  > and two exhibited lifts share the augmented datum and differ in the level-2 datum, the separating
  > index and quantity named in each case. **So `X` sits strictly between act 17's visible data and
  > act 13's datum.** This is a statement about the exact functional frozen under the label `X`, and
  > **it does not endorse `X`, does not say the programme needs a datum of this shape, and does not
  > adopt `X` as the physical carrier of cross-time information.**
- **Outcome `X-NOT-ABOVE`**, for a named Type D candidate `X`:
  > Equality of the anchored readback implies equality of the augmented datum for `X`, universally,
  > at evidence level 2. **So `X` adds nothing to act 17's visible data** and cannot supply
  > cross-time information the visible data do not already carry. This is a statement about the exact
  > functional frozen under the label `X` and about nothing in its neighbourhood.
- **Outcome `X-NOT-BELOW`**, for a named Type D candidate `X`:
  > Equality of the augmented datum for `X` implies equality of act 13's level-2 datum, universally,
  > at evidence level 2. **So `X` recovers the whole of level 2 and is not strictly below it**: any
  > determination it supplies is act 13's determination, reached by containing the same information.
  > This is a finding and not a criticism, and it is exactly what obligation 3 exists to detect.
- **Outcome `X-DET`**, for a named Type D candidate `X`:
  > Equality of the augmented datum for `X` implies that the two lifts have the same Gram/orbit
  > trajectory under `GramTrajEquiv`, universally over every finite carrier, anchor, visible family
  > and pair of lifts, at evidence level 2. **This is a statement about the exact functional frozen
  > under the label `X`**, on its frozen data grant. It does **not** endorse `X`, does **not** say a
  > determining datum is required, and does **not** close `P0` or either of its parts.
- **Outcome `X-RESID`**, for a named Type D candidate `X`:
  > Two exhibited lifts share the augmented datum for `X` and their trajectories are **inequivalent
  > under `GramTrajEquiv`**, at a named time and through a named invariant, at evidence level 2. **So
  > `X` leaves residual trajectory freedom.** This settles the datum, not a neighbourhood of it, and
  > it is not a statement that no datum of Type D determines the trajectory.
- **Outcome `X`-UNDECIDED**, for a named Type D candidate `X` and a named obligation:
  > The obligation asked of `X` is undecided in this round, with the obstruction named specifically —
  > the candidate, the obligation, the step at which the proof stopped, and what would settle it.
  > Neither label is claimed, and no sentence of this round treats the absence of a decision as a
  > decision. In particular the absence of a counterexample is **not** reported as the obligation
  > holding, and the absence of a witness is **not** reported as there being none.

### The outcomes of `XS3`, per candidate and per obligation

- **Outcome `Y-PROPER`**, for a named Type L candidate `Y`:
  > At one exhibited configuration the law `Y` prescribes has a solution set that is **nonempty**,
  > **non-singleton modulo `GramTrajEquiv`** and **proper**, all three witnessed together by three
  > pointwise realizable trajectories named in the statement, at evidence level 2. **So `Y` is a
  > genuine proper constraint there**, neither vacuous nor the trajectory in disguise. This settles
  > **one configuration** and is not a statement about every configuration, and it does **not**
  > endorse `Y`, does **not** say a law of this shape is required, and does **not** adopt it.
- **Outcome `Y-VACUOUS`**, for a named Type L candidate `Y`:
  > At the exhibited configuration the law `Y` prescribes excludes **no** pointwise realizable
  > trajectory, proved universally over them at evidence level 2. **So `Y` is vacuous there** and
  > constrains nothing. It settles one configuration and is not a statement about every
  > configuration.
- **Outcome `Y-SINGLE`**, for a named Type L candidate `Y`:
  > At the exhibited configuration the law `Y` prescribes has exactly one solution class under
  > `GramTrajEquiv`, proved universally at evidence level 2. **So `Y` hands over the trajectory there
  > rather than constraining it**, and the non-singleton clause of the non-triviality witness fails.
  > **This is a failure of non-triviality and not a failure of determination**, and it settles one
  > configuration.
- **Outcome `Y-PROPAGATES`**, for a named Type L candidate `Y`:
  > Given the non-triviality witness, **both** propagation clauses hold at evidence level 2: two
  > pointwise realizable solutions of the law `Y` prescribes that agree at time `0` have the same
  > trajectory under `GramTrajEquiv`, proved universally; and the law without the initial orbit fixed
  > leaves two inequivalent orbit classes at an exhibited time after the initial one, so **the initial
  > orbit does work**. **So the law plus one initial orbit propagates uniquely.** That is what a law of
  > evolution does and it is not a cheat here, the law datum being writable from the anchor and the
  > visible family before any lift exists. **This is a statement about the exact law frozen under the
  > label `Y`**: it does **not** endorse it, does **not** say such a law obtains, does **not** adopt
  > any carrier or principle as the physical one, and does **not** close `P0` or either of its parts.
- **Outcome `Y-RESID`**, for a named Type L candidate `Y`:
  > Two exhibited pointwise realizable solutions of the law `Y` prescribes agree at time `0` and
  > their trajectories are **inequivalent under `GramTrajEquiv`**, at a named time and through a
  > named invariant, at evidence level 2. **So residual histories remain after the initial orbit is
  > fixed** and the law plus one initial orbit does not propagate uniquely. It settles that law and
  > nothing in its neighbourhood, and it is **not** the outcome in which the initial orbit does no
  > work; the two mechanisms are kept apart.
- **Outcome `Y-DEGENERATE`**, for a named Type L candidate `Y`:
  > At the exhibited configuration the solutions of the law `Y` prescribes occupy exactly one orbit
  > class at every time after the initial one, proved universally at evidence level 2. **So the law
  > fixes every later slice by itself and the initial orbit contributes nothing**, and what the law
  > produces is slice-by-slice determination and not propagation. It settles that law at that
  > configuration, and it is **not** the outcome in which residual histories remain after the initial
  > orbit is fixed; the two mechanisms are kept apart.
- **Outcome `Y`-UNDECIDED**, for a named Type L candidate `Y` and a named obligation:
  > The obligation asked of `Y` is undecided in this round, with the obstruction named specifically —
  > the candidate, the obligation, the step at which the proof stopped, and what would settle it. For
  > the generator law the descent obligation is named where it is the obstruction, and **no verdict
  > about propagation is recorded where the descent is not discharged.** Neither label is claimed, and
  > no sentence of this round treats the absence of a decision as a decision.

### The outcomes of `XS4` — the `D`-axis, each sentence frozen in full

- **Outcome `D-DET`:**
  > **A genuine intermediate readback datum determines the Gram/orbit trajectory.** The named datum
  > satisfies all three frozen obligations — bounded above by act 13's level-2 datum, strictly above
  > act 17's visible data, strictly below act 13's — and equality of it implies equality of the
  > trajectory under `GramTrajEquiv`, at evidence level 2. **This is a statement about the exact
  > functional this freeze names, on its frozen data grant, and about nothing else.** It does not say
  > the datum is the physical one, does not adopt it, does not say the programme requires such a
  > datum, and does not close `P0` or either of its parts. **The `L`-axis outcome is reported beside
  > it and neither is above the other.** `P0` stays **OPEN** and two-part, its threading part is
  > untouched, and no carrier is adopted as the physical one.
- **Outcome `D-MID`:**
  > **A genuine intermediate readback datum exists, and residual trajectory freedom remains.** The
  > named datum satisfies all three frozen obligations, and two exhibited lifts share it while their
  > trajectories are inequivalent under `GramTrajEquiv`, at evidence level 2. **So the interval
  > between act 17's visible data and act 13's datum is inhabited, and what inhabits it there does
  > not determine the trajectory.** This settles the named datum and is not a statement that no
  > intermediate datum determines it. **The `L`-axis outcome is reported beside it and neither is
  > above the other.** `P0` stays **OPEN** and two-part.
- **Outcome `D-NOGO`:**
  > **No candidate on this freeze's Type D list is a genuine intermediate datum.** For every member
  > of the list an obligation fails, each failure exhibited at evidence level 2 and the failing
  > obligation named per candidate. **This is a bounded no-go over a closed three-member list frozen
  > before the search**, and it is **not** a statement that no intermediate datum exists, **not** a
  > statement that the interval is empty, and **not** a bound on what a later round could name. **The
  > `L`-axis outcome is reported beside it and neither is above the other.** `P0` stays **OPEN** and
  > two-part.
- **Outcome `D-UNDECIDED`:**
  > **The `D`-axis is recorded UNDECIDED.** No candidate on the frozen list reached a settling
  > outcome, and none is claimed: no intermediate datum is shown to determine the trajectory, none is
  > shown to leave residual freedom with all three obligations discharged, and no bounded no-go over
  > the list is earned. The obstruction is named specifically — the candidate, the obligation, the
  > step and what would settle it. **An UNDECIDED is a statement about this round and about the
  > record, and not about the question.** It is not a finding that the question is unresolvable, not a
  > finding that it is hard, and not a bound on what a later round can do. **The `L`-axis outcome is
  > reported beside it and neither is above the other.**

### The outcomes of `XS5` — the `L`-axis, each sentence frozen in full

- **Outcome `L-PROP`:**
  > **A genuine proper structural law, together with one initial orbit, propagates uniquely.** The
  > named law is written from the anchor and the visible family alone, before any lift is chosen;
  > it respects `GramTrajEquiv`; its solution set at one exhibited configuration is nonempty,
  > non-singleton modulo `GramTrajEquiv` and proper, all three witnessed together; two solutions
  > agreeing at time `0` have the same trajectory; and the law without the initial orbit fixed leaves
  > two inequivalent orbit classes at an exhibited time after the initial one, **so the initial orbit
  > does work and what is reported is propagation and not slice-by-slice determination**. At evidence
  > level 2. **That a law of evolution
  > determines a history given an initial condition is what such a law is**, and it is legitimate here
  > because the law datum is writable before any lift exists. **This is a statement about the exact
  > law this freeze names and about nothing else**: it does not say the law obtains, does not adopt
  > it, does not say the programme requires one, and does not close `P0` or either of its parts.
  > **The `D`-axis outcome is reported beside it and neither is above the other.** `P0` stays
  > **OPEN** and two-part, its threading part is untouched, and no carrier is adopted as the physical
  > one.
- **Outcome `L-PROPER`:**
  > **A genuine proper cross-time constraint is exhibited, and it does not propagate.** The named law
  > respects `GramTrajEquiv` and its solution set at one exhibited configuration is nonempty,
  > non-singleton modulo `GramTrajEquiv` and proper, all three witnessed together; and one of the two
  > propagation clauses fails, at evidence level 2, by the mechanism the report names — **either**
  > two exhibited solutions agree at time `0` while their trajectories are inequivalent, so residual
  > histories remain after the initial orbit is fixed, **or** the solutions occupy one orbit class at
  > every time after the initial one, so the initial orbit contributes nothing. **The two mechanisms
  > are kept apart and the report names which holds**; reporting one as the other is a defect. **This
  > is a narrowing and not a propagation.** It settles the named law at the named configuration. **The
  > `D`-axis outcome is reported beside it and neither is above the other.** `P0` stays **OPEN** and
  > two-part.
- **Outcome `L-NOGO`:**
  > **No candidate on this freeze's Type L list is a genuine proper law.** For every member of the
  > list a clause of the non-triviality witness fails, or the candidate is excluded by this round's
  > own factorization theorem, each at evidence level 2 and the failing clause named per candidate.
  > **This is a bounded no-go over a closed four-member list frozen before the search**, and it is
  > **not** a statement that no such law exists, **not** a statement that cross-time laws are
  > impossible, and **not** a bound on what a later round could name. **The `D`-axis outcome is
  > reported beside it and neither is above the other.** `P0` stays **OPEN** and two-part.
- **Outcome `L-UNDECIDED`:**
  > **The `L`-axis is recorded UNDECIDED.** No candidate on the frozen list reached a settling
  > outcome, and none is claimed: no law is shown to propagate, none is shown proper with residual
  > histories, and no bounded no-go over the list is earned. The obstruction is named specifically —
  > the candidate, the clause, the step and what would settle it, with the descent obligation named
  > where it is the obstruction. **An UNDECIDED is a statement about this round and about the record,
  > and not about the question.** **The `D`-axis outcome is reported beside it and neither is above
  > the other.**

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The sentence the execution
appends to it is composed from the clauses fixed here, and from no other wording.

**Case A — `XS0` silent, `XS1` lands, the `D`-axis reaches `D-MID` and the `L`-axis reaches
`L-PROP`.** This is the case the freeze predicts.

> `P0` remains open and two-part, and the answers of acts 11 through 17 stand exactly as those rounds
> state them. Act 17's baseline is untouched: the admissible Gram trajectories of a visible family
> are exactly the pointwise realizable assignments, and any cross-time law must enter as additional
> structure. Act 18 asks what such a structure would have to be, on two axes that are not ranked
> against each other, against a candidate list frozen before the search. On the structural question
> that runs first, a law that is pointwise in this round's sense has a solution set equal to the
> product over time of its per-time solution sets, so any uniqueness it produces is slice-by-slice
> uniqueness and never a relation propagating one time from another — which is not the statement that
> no pointwise constraint yields cross-time determination, that being false, but the statement that
> propagation is what fails. On the readback axis, which asks whether a datum strictly between the
> operationally visible data and act 13's level-2 datum determines the trajectory, one named datum
> discharges all three obligations of the refinement sandwich — it consumes nothing beyond act 13's
> level-2 datum, it separates lifts the operationally visible data do not separate, and two lifts
> share it while their level-2 data differ — and two lifts sharing it have inequivalent trajectories,
> so the interval is inhabited and what inhabits it there leaves residual trajectory freedom. On
> the structural-law axis, which asks whether a constraint writable from the anchor and the visible
> family alone is proper and propagates, one named generator law, written at orbit level so that it
> descends, has a solution set at one exhibited configuration that is nonempty, non-singleton modulo
> the round's cross-time equivalence and proper, and two of its solutions agreeing at the initial
> time have the same trajectory. That a law of evolution determines a history given an initial
> condition is what such a law is, and it is legitimate here because the law is writable before any
> lift exists; it is not an assertion that the law obtains, not an adoption of it, and not a claim
> that the programme requires one. The candidate lists are closed and are not exhaustive, each
> verdict is of the exact frozen proposition and of nothing in its neighbourhood, and the coarsest
> determining datum is out of scope by this round's own freeze. `P0`'s threading part is untouched,
> act 10's anchor-axis reclassification is untouched in either direction, **no carrier is adopted as
> the physical one**, and nothing here names, endorses or excludes a selection principle.

**Three clauses of Case A vary with the outcome, and they vary independently.** Naming them here, and
fixing each clause's substitutions against the target that governs it, is what lets the execution
compose the sentence it actually earned rather than carry a clause that reads against its own
outcome.

- **The structural clause**, governed by `XS1`, is Case A's sentence beginning "On the structural
  question that runs first".
- **The readback clause**, governed by `XS4`, is Case A's sentence beginning "On the readback axis".
- **The law clause**, governed by `XS5`, is Case A's sentence beginning "On the structural-law axis"
  together with the sentence beginning "That a law of evolution".

**The structural clause, per `XS1` outcome.**

| `XS1` | structural clause |
| --- | --- |
| landed (**Case A**) | as written above |
| UNDECIDED | "On the structural question that runs first, the factorization of a pointwise law's solution set was not reached, with the obstruction named, so the pointwise candidates stay live and the structural-law axis ran against the full frozen list." |

**The readback clause, per `XS4` outcome.**

| `XS4` | readback clause |
| --- | --- |
| `D-MID` (**Case A**) | as written above |
| `D-DET` | "On the readback axis the outcome is that a named datum strictly between the operationally visible data and act 13's level-2 datum determines the Gram/orbit trajectory, all three obligations of the refinement sandwich discharged, which is a statement about that exact functional and not an adoption of it." |
| `D-NOGO` | "On the readback axis no candidate on the frozen three-member list is a datum strictly between the operationally visible data and act 13's level-2 datum, an obligation failing for each and each failure exhibited, which is a bounded no-go over that closed list and not a statement that the interval is empty." |
| `D-UNDECIDED` | "On the readback axis the outcome is recorded undecided with the obstruction named, no candidate on the frozen three-member list having discharged every obligation of the refinement sandwich together with the determination target." |

**The law clause, per `XS5` outcome.**

| `XS5` | law clause |
| --- | --- |
| `L-PROP` (**Case A**) | as written above |
| `L-PROPER` | "On the structural-law axis one named law, writable from the anchor and the visible family alone, has a solution set at one exhibited configuration that is nonempty, non-singleton modulo the round's cross-time equivalence and proper, while one of the two propagation clauses fails by the mechanism the record names — either two solutions agreeing at the initial time have inequivalent trajectories, or the later slices are fixed by the law alone so the initial orbit contributes nothing — so it narrows the histories without propagating." |
| `L-NOGO` | "On the structural-law axis no candidate on the frozen four-member list is a genuine proper law, a clause of the non-triviality witness failing for each or the candidate being excluded by this round's factorization theorem, which is a bounded no-go over that closed list and not a statement that no such law exists." |
| `L-UNDECIDED` | "On the structural-law axis the outcome is recorded undecided with the obstruction named, no candidate on the frozen four-member list having discharged its non-triviality witness together with the propagation question, and the descent obligation named where it is the obstruction." |

**The execution composes the sentence from these substitutions and reports no other wording.** **No
composition closes `P0`**, and none reports either of its two parts closed. **The two axis clauses
appear in the order readback-then-law in every composition**, which is an ordering of the sentence
and not a ranking of the axes, and the composition says so where it is read as one.

## Naming a candidate is not endorsing it, FROZEN

Acts 11 through 17 each carry the non-doing "names, endorses or excludes no selection principle".
**This round names candidate structures, and it must, because it cannot test what it cannot name.**
The reconciliation is frozen here so that it cannot be improvised afterwards.

1. **Naming is for testing.** Each candidate is named as an **object of test** and for no other
   purpose. Naming it is not proposing it, not adopting it, not asserting that it is the right shape,
   and not asserting that the programme needs extra structure at all.
2. **The round still endorses none.** No outcome of this round endorses any candidate, and no
   sentence of any artifact of this round says that extra cross-time structure is required, on any
   carrier or carrier-free.
3. **Exclusion is only ever of the precise stated form.** Where a candidate fails an obligation, what
   fails is the **exact proposition frozen below under that candidate's label**, on the exact data
   grant frozen for it, and nothing in its neighbourhood. A failure of `LC2` as this freeze states it
   is not a refutation of regularity in general, and the result note says so at each such failure.
4. **The candidate lists are closed at this freeze.** The execution tests these candidates and no
   others, and no candidate changes type.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a candidate's survival could be read as its adoption.** Each carriage
opens with one line naming where it is being carried, contiguous with the body, so that the carriages
read as distinguishable copies of one clause rather than as one paragraph pasted repeatedly — which
is a defect the repository's duplicate check exists to catch — and the naming line changes nothing
about the clause it introduces. Acts 15, 16 and 17 established this pattern and this round follows
it.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed post-round
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name a candidate among the candidates this round tests.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
> either axis is a statement about the exact structure this freeze names, on the data grant frozen
> for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
> programme requires it, and **not** an adoption of it as the physical carrier of cross-time
> information. A datum that determines the trajectory does not thereby become the right datum, and a
> law whose solutions at a configuration are one history is not thereby the law of evolution: the
> refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
> `L`-axis exist because a structure can reach a top line by containing the answer rather than by
> supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
> adopted as the physical one, and no candidate changes type during execution.**

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The trajectory freedom is gauge", or "the trajectory freedom is physical."** Act 14's status
   rule that there is no carrier-free verdict binds this round too, and this round adopts no carrier
   and defines no carrier of its own.
2. **"The datum that works is the physical one", or "this is the law of nature."** The non-adoption
   clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
   > either axis is a statement about the exact structure this freeze names, on the data grant frozen
   > for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
   > programme requires it, and **not** an adoption of it as the physical carrier of cross-time
   > information. A datum that determines the trajectory does not thereby become the right datum, and a
   > law whose solutions at a configuration are one history is not thereby the law of evolution: the
   > refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
   > `L`-axis exist because a structure can reach a top line by containing the answer rather than by
   > supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
   > adopted as the physical one, and no candidate changes type during execution.**
3. **"No pointwise constraint yields cross-time determination."** This sentence is **false**, and
   `XS1` does not say it. A pointwise condition with a unique solution at every time determines the
   trajectory slice by slice. **What fails is propagation, not determination.**
4. **"`XS1` rules out cross-time laws."** It is bounded to pointwise laws in this freeze's sense, and
   `LC1`, `LC2` and `LC3` are not pointwise.
5. **"Same augmented datum, inequivalent trajectories" reported as obligation 3.** Obligation 3 is
   *same augmented datum, different level-2 datum*. The trajectory phrasing is unsatisfiable exactly
   when the axis succeeds, and stating it that way is a defect of this round.
6. **"The candidate list is exhaustive", or "these are the intermediate structures."** Three Type D
   and four Type L propositions are frozen for testing. A candidate outside them is neither refuted
   nor endorsed by anything here.
7. **"The coarsest determining datum is …", or any lattice statement about the space of data.** That
   question is explicitly out of scope, by this freeze's own non-doing.
8. **"One axis answers the other", or any ranking of the two axes.** The outcome is the ordered pair,
   and neither element is a fallback for the other.
9. **"The bounded no-go shows no such structure exists."** Each no-go quantifies over a closed list
   named in this freeze and over nothing else.
10. **"A witness was sought and not found, so there is none."** Absence of a witness in this round is
    not a negative result, no search is presented as exhaustive, and the outcome of a failed search
    is UNDECIDED with the obstruction named.
11. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate.** These are invisible to `≈_O` by construction. **A round that cannot see
    a distinction may not report one**, in either direction.
12. **Any statement about act 16's cancellation cell**, in either direction, and any reading of act
    16's `RN3⁺` or act 15's `PQ3-d⁺` as bearing on trajectory freedom or on cross-time structure.
13. **Any statement about act 14's four carriers**, or any adoption of a carrier, or any assertion
    that a carrier is not the physical one. This round defines no carrier and reads none.
14. **"Act 10's anchor axis is resolved", or "reopened", or "narrowed."** The anchor-coherence
    candidates are grounded in act 10's reclassification and bear on it in neither direction.
15. **"`P0` is closed", or "`P0`'s trajectory part is closed."** The row stays OPEN and two-part in
    every case.
16. **"Act 13's level-2 result is strengthened", or "act 17's `TJ1` is enlarged."** Both are consumed
    at merged strength. **A merged statement is not enlarged by being consumed.**
17. **"The trajectory is continuous", "smooth", "generated by a Hamiltonian", or any statement
    resting on structure the index type does not carry.** `CoherentLift` is `ℕ`-indexed and this
    round does not change that, and `LC2`'s pseudometric is on the value space and never on the
    index.
18. **"OI and QM are inequivalent."** Two lifts differing is not two theories differing, and the
    established finite observable-law correspondence is untouched. Every visibility statement here is
    further a statement under act 7's own readback convention, with `D4b` negative.
19. **Any sentence about Track I**, or about Source B or Source C, on any axis.
20. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **A candidate that reaches a top line by containing the answer.** **This is the strongest hazard
   in the round.** The non-adoption clause is carried verbatim at every mention:
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 18 names candidate structures in order to test them, and adopts none. Reaching the top line of
   > either axis is a statement about the exact structure this freeze names, on the data grant frozen
   > for it, and it is **not** a finding that the structure obtains in nature, **not** a finding that the
   > programme requires it, and **not** an adoption of it as the physical carrier of cross-time
   > information. A datum that determines the trajectory does not thereby become the right datum, and a
   > law whose solutions at a configuration are one history is not thereby the law of evolution: the
   > refinement sandwich of the `D`-axis and the one-configuration non-triviality witness of the
   > `L`-axis exist because a structure can reach a top line by containing the answer rather than by
   > supplying one. **No candidate gains physical status by surviving, no carrier and no principle is
   > adopted as the physical one, and no candidate changes type during execution.**
2. **Obligation 3 restated against the trajectory.** The specific failure guarded against is a result
   note that writes "same augmented datum, inequivalent trajectories" and then searches for a witness
   its own determination target forbids. **Obligation 3 is stated against act 13's level-2 datum**,
   and the section that freezes it says why in terms.
3. **A candidate changing type mid-execution.** The specific failure guarded against is a Type D
   candidate that fails the sandwich being re-reported as a Type L law, or the reverse, so that it
   answers whichever obligations it happens to satisfy. Cross-time anchor coherence is frozen as
   **two separate candidates** for exactly this reason.
4. **Split-configuration non-triviality.** The specific failure guarded against is a law shown
   non-empty and non-singleton at one configuration and proper at another, which passes both
   separated tests while being vacuous at the first and the answer in disguise at the second. **The
   witness is at one common configuration and carries all four conjuncts.**
5. **A properness witness outside the admissible set.** The specific failure guarded against is an
   excluded trajectory that is not pointwise realizable, which proves nothing about the law. `H`'s
   realizability is a conjunct, and it is available only because of act 17's `TJ1`.
6. **A generator law that does not descend.** The specific failure guarded against is a
   representative-level `V_t` that "selects" by fixing an unphysical frame. The descent obligation is
   part of the candidate, and where it is not discharged **no propagation verdict is recorded**.
7. **Reading `XS1` as a no-go about determination.** The specific failure guarded against is the
   false sentence "no pointwise constraint yields cross-time determination". `XS1` is about
   propagation.
8. **Reporting a degenerate propagation as propagation.** The specific failure guarded against is a
   law whose per-time solution sets are single classes at every time after the initial one, which
   satisfies the uniqueness clause while the initial orbit does no work at all. **Clause (ii) of the
   frozen propagation definition is what excludes it**, and the two non-propagation mechanisms —
   residual histories after the initial orbit is fixed, and an initial orbit that contributes
   nothing — are kept apart and named.
9. **Forgetting that `XS1` needs `TJ1`.** The specific failure guarded against is a factorization
   argument that splices two solutions and forgets to show the splice is admissible. Intersecting a
   product constraint with a non-product ambient set need not factor.
10. **Ranking the two axes.** The specific failure guarded against is a result note that reports the
    `L`-axis outcome as the round's answer and the `D`-axis as a shortfall, or the reverse. **The
    headline is the ordered pair.**
11. **Treating an undischarged obligation as discharged because no counterexample was found.** The
    specific failure guarded against is reporting `X-SANDWICH` on two obligations and a search.
12. **Enlarging a bounded no-go.** The specific failure guarded against is a sentence of the form "so
    no intermediate datum exists" or "so no cross-time law exists". Each list is closed and named.
13. **Letting the lattice question creep in.** The specific failure guarded against is an execution
    that, having found one intermediate datum, starts characterizing the coarsest one. **It is an
    explicit non-doing** and belongs to a later round with its own freeze.
14. **Consuming act 13's level-2 result at more than merged strength.** `CT2` (b) is a
    both-directions statement about the fibre cross-Gram trajectory and the threading residual. The
    specific failure guarded against is citing it as though it quantified over data it does not
    mention.
15. **Consuming act 17's `TJ1` or `TJ3` at more than their strength.** `TJ1` is about `CoherentLift`
    as the programme defines it; `TJ3-IMP` is impossibility within a four-member class at one
    configuration. Neither is a universal statement about structures.
16. **Seeing the threading.** The specific failure guarded against is a statement of this round
    distinguishing two lifts that `≈_O` identifies — for instance reporting that act 11's `GL2` pair
    has two trajectories. It has one, for this round, and the round says nothing about the
    difference.
17. **Reading raw Gram equality or act 13's relation as this round's relation.** `≈_O` is act 17's
    `GramTrajEquiv`, consumed and not redefined, and is the only relation any quotient is taken over.
18. **Touching act 16's cancellation cell or the threading question.** Neither is asked here, in
    either direction, and no outcome of this round bears on either.
19. **Reading a `DF3` or `LC1` outcome as an anchor-axis finding.** Both are grounded in act 10's
    reclassification and neither resolves, reopens or narrows it. The specific failure guarded against
    is a sentence that reads an anchor-coherence verdict as progress on the upstream anchor choice.
20. **Importing time structure the index type does not have.** `ℕ` carries successor and order and
    nothing else. The specific failure guarded against is a candidate, a proof or a sentence resting
    on continuity, differentiability or a limit — `LC2` included, whose pseudometric is on the value
    space.
21. **Choosing a configuration after an outcome is known.** The countercontrol table names the
    configuration for every obligation in advance, and an alternative found during execution is
    recorded as an observation and never substituted.
22. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.** Act
    12's `|A| = 1` is the strongest case for the per-slice statements; the `DF1` reason recorded above
    is the concrete instance where it may collapse a cross-time distinction.
23. **A reader supplying a missing theorem from background knowledge the record does not contain.**
    The specific failure guarded against is a step of the form "of course an intermediate datum
    exists" or "of course a law of evolution is available here" — plausible-sounding, absent from the
    record, and licensed by nothing in it.
24. **Forgetting the anchor, and forgetting the rank bound.** `FibreGram a₀`, `FibreCrossGram a₀` and
    `RealizableGram` all carry data a cross-time statement can silently drop: the anchor, and the
    `|A|` rank bound that makes `SH1` sufficiency true.
25. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
26. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier in a different programme. Nothing is consumed or compared, and a shared word is not a
    bridge.
27. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_XTS_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
28. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
29. **A chronology guard that fixes this round's own pins at `None` for all time.** See the
    chronology control's clause 9, which exists because an earlier round wrote exactly such a clause
    and its whole execution object had to be rebuilt.
30. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: adopt a carrier as the physical one or define a carrier of its own; endorse any
candidate structure, datum or law; assert or deny that extra cross-time structure is required or
suffices; **ask the threading question or the cross-time representative question, in either
direction**; touch act 16's cancellation cell, in either direction; state anything about the relative
object, the relative candidate, the anchored channel or the re-anchored channel; revise `GL1s`,
`GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`, `AB1`,
`AB2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3` or any
merged label; answer act 13's fork `CT3` (d) or move it in either direction; re-prove or strengthen
act 13's level-2 result, which is consumed at merged strength and below which every Type D candidate
is mechanically bounded by obligation 1; re-prove or strengthen act 17's `TJ1` or `TJ3`; redefine act
17's `GramTrajEquiv`; test a candidate outside the frozen lists; let a candidate change type; adopt
the uniform-phase or the raw-Gram relation; change `CoherentLift`'s `ℕ`-indexing or introduce
continuity, smoothness, a generated evolution as a **condition of the round** rather than as a named
candidate, a measurement model or a source-level coherence condition; introduce a further carrier or
revise any of act 14's four; resolve, reopen or narrow act 10's anchor-axis reclassification; rank
the two axes; report a bounded no-go as a general impossibility; change `D3`, `D4b`, `D5`, the
direct-branch statement or the readback convention; alter any existing archive seal constant; consume
or compare anything from the substratum Lemma 24.1 rounds; compare Source A with B or C; edit any
manuscript; close `P0` or either of its parts; or say anything about Track I.

### The lattice question is EXPLICITLY OUT OF SCOPE

**"Characterize the coarsest determining datum" is not asked, not bounded and not attempted.** It is
the natural stretch target of this round and it is unbounded: it quantifies over the space of
functionals of the lift, it requires an order on that space that no merged result supplies, and it
has no evidence bar this freeze could honestly fix. It is named here as a non-doing **so that it
cannot creep in mid-execution**: an execution that finds one intermediate datum and begins comparing
it with others has left this round's scope, and what it finds is **recorded as an observation and not
executed**. A later round that wants the lattice question must freeze it first.

### What act 18 does and does not change about `P0`

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 18 can change
is the **bounding** of its trajectory part, and only that: act 17 established that every cross-time
constraint on the trajectory is additional structure, and act 18 asks what such a structure would
have to be, on two axes, against a closed candidate list. **No outcome of this round closes `P0`, no
outcome closes either of its parts, and no outcome makes either part closable.** `P0`'s threading
part is untouched in either direction. And an affirmative on either axis is a statement about **one
named structure** and not a statement that the programme has found the structure `P0` asks for: what
`P0` asks is what **determines** the relative quantum evolution, and naming a structure that would
suffice if imposed is not naming the one that obtains.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most five** top-level Lean definitions, and these are the five:

1. **`PointwiseLaw`** — the predicate that a law is pointwise in this freeze's sense,
   `PointwiseLaw Law := ∃ c, ∀ 𝔾, Law 𝔾 ↔ ∀ t, c t (𝔾 t)`. `XS1` is stated over it and cannot be
   stated readably without it. *Needed.*
2. **`DeterminesTraj`** — the `D`-determination target as one `Prop` over a functional,
   `DeterminesTraj a₀ F := ∀ U U', D₀ U = D₀ U' → F U = F U' → GramTrajEquiv (𝔾 U) (𝔾 U')`. Three
   candidates are stated over it. *Needed.*
3. **`ProperAt`** — the one-configuration non-triviality witness as one `Prop`, carrying all four
   conjuncts with `G₁`, `G₂`, `H` existentially quantified and pointwise realizable. Four candidates
   and the `L`-axis top line are stated over it. *Needed.*
4. **`PropagatesFrom`** — the propagation predicate, carrying **both** frozen clauses:
   `PropagatesFrom a₀ Γ Law` holds iff any two pointwise realizable solutions agreeing at time `0`
   are `GramTrajEquiv`, **and** there is a `t ≥ 1` at which the solutions, without the initial orbit
   fixed, occupy two inequivalent orbit classes. The `L`-axis top line is stated over it. *Needed.*
5. **A named functional for one Type D candidate** — `F₁`, `F₂` or `F₃` written as a definition —
   *if* its obligations cannot be stated readably with the functional written inline; unused
   otherwise. *Conditional.*

**A further definition beyond these five requires its own append-only amendment**, separately frozen
and merged before the work it affects. **No lift, gauge element, witness, matrix, visible family,
Gram tuple, entry value, law datum or configuration is a top-level definition** — each is a bound
variable pinned by an equation in the statement that needs it, as acts 10 through 17 did. Acts 7's,
10's, 11's, 12's, 13's and 17's definitions are **reused, not redefined**; in particular `FibreGram`,
`GramPhaseEquiv`, `RealizableGram`, `CoherentLift`, `FibreCrossGram`, `TwoSidedRelated`,
`GramTrajEquiv` and `SelectsAt` are consumed and none is restated.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `XS1`, for each part of `XS2` and `XS3` whichever label
it reaches, and for `XS4` and `XS5` whichever line each reaches other than UNDECIDED. `decide` over
finite index types is kernel-checked and permitted; `native_decide` is not, and neither is `sorry`.
`Classical.choice` is expected wherever act 17's `tj1_sufficiency` is applied, which assembles a lift
from a per-time choice, and its appearance there is not a defect.

**`XS0` is type P and carries no evidence level.** It is settled by the frozen evidence rule —
verbatim quotation with a coordinate, or the recorded statement that the passage sought does not
exist on the named and bounded search — and by nothing else. **Reconstructive inference is forbidden
as a finding**, and where the record is silent the finding is that it is silent.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-XTS`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_XTS_SEALED_HEAD`** and **`_XTS_MERGE`**, with
the base held in **`_XTS_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 18 object
   enters the repository tree** — any Lean definition or proof about an intermediate datum, about a
   structural law, about the factorization of pointwise laws or about either axis; any search
   artifact; any probe clause; any result artifact. **The single permitted exception is the analysis
   recorded inside this control-plane blob itself**, merged *as* the freeze, including the frozen
   evidence rule, the well-posedness check, the table of what the merged record supplies, and the
   pre-freeze reading recorded as the reason for `XS0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_XTS_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content at this exact path, and the
   execution ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _XTS_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of
   `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_XTS_SEALED_HEAD` and `_XTS_MERGE` are present and **unset** at execution.
   After `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the
   same strong check against the sealed object: the pinned merge's second parent must equal the
   sealed head; the sealed head must pass clause 5 against `B` exactly as in its own run; and both
   must be reachable from the current target — the real `pull_request.head.sha` in pull-request
   continuous integration, `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change
   recording the two SHAs and nothing else.
8. **Existing seal constants are read with mutation controls and never written.** The guard clause
   checks `_TRJ_BASE`, `_TRJ_SEALED_HEAD`, `_TRJ_MERGE`, `_RNC_BASE`, `_RNC_SEALED_HEAD`,
   `_RNC_MERGE`, `_TCF_BASE`, `_TCF_SEALED_HEAD`, `_TCF_MERGE`, `_PQT_BASE`, `_PQT_SEALED_HEAD`,
   `_PQT_MERGE`, `_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE` equal to the values acts 17, 16,
   15, 14 and 13 set, because an archive seal belongs to the round that set it.
9. **This round's own triple is never a permanently fixed execution-mode value.** `R7-XTS` must not
   assert `(_XTS_BASE, _XTS_SEALED_HEAD, _XTS_MERGE)` equal to `(_XTS_BASE, None, None)` as a
   standing invariant. Either the round's own triple is **excluded** from the prior-seal integrity
   clause of item 8 — which names other rounds' seals and is the shape this freeze intends, following
   the `_tcf_prior_seals`, `_rnc_prior_seals` and `_trj_prior_seals` precedent of **zero executable
   references to the round's own constants**, with docstring prose explaining the exclusion being
   entirely sufficient — or it is checked **mode-aware**, the expectation being
   `(_XTS_BASE, None, None)` while `_XTS_SEALED_HEAD` is unset and
   `(_XTS_BASE, _XTS_SEALED_HEAD, _XTS_MERGE)` once `P` has set them, and read from the module
   constants rather than from the argument, so that a fabricated tuple cannot define its own
   expectation. A clause that fixes this round's own pins at `None` for all time contradicts item 7,
   under which `P` must set them: the guard would then pass at no commit once the round lands, and
   the round's mandatory lifecycle could not complete. **This item exists because an earlier round
   wrote exactly such a clause and its whole execution object had to be rebuilt**, and it is written
   so that the executing agent cannot reintroduce that failure: the exclusion route is the one this
   freeze intends, and the mode-aware route is permitted only in the exact form stated here, with the
   expectation read from the module constants and **never** from the argument. Prior rounds' seals
   stay read-only invariants exactly as item 8 states; this item constrains only how the round treats
   its **own** pins.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/preregistration.md \| git hash-object --stdin` equals the blob the `R7-XTS` clause pins |
| 2 | Act 17's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TRJ_SEALED_HEAD = '94d41561114b2aee5939dcfa976ce98b8f141093'` and `_TRJ_MERGE = 'e8b12a433ebc0e5047504d2c95664a85ca65d1e8'`, both non-`None` |
| 3 | Act 16's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_RNC_SEALED_HEAD = '31db7c1082b012c00c43f3fda35ce44c5653e123'` and `_RNC_MERGE = 'eb70bbb9b2b3311095945ec3ce2418962f3b741a'`, both non-`None` |
| 4 | Act 15's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, both non-`None` |
| 5 | Act 14's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` |
| 6 | Act 13's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` |
| 7 | The modules this round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` and `git cat-file -e B:verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` all succeed |
| 8 | No act 18 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` |
| 9 | The guard tag and its stem are still free | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-XTS` and no occurrence of `_XTS` |

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
  else**, and **its first act is to verify that the preregistration at that base carries the blob
  this freeze names**, before any target is executed. The verification is recorded in the result
  note.
- **Then exactly one execution pull request**, based on that merge commit, carrying the Lean module,
  the result note, the `R7-XTS` guard clause with `_XTS_SEALED_HEAD` and `_XTS_MERGE` present and
  unset, the `ROADMAP` propagation and the census entry. **No manuscript changes.**
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no
  rebase, no amend, no force-push. A red badge caused solely by an archive clause that entered
  `main` after the base is not a research failure; the certification of record is the run whose
  `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled named
   and no existing seal constant altered, and the base-blob verification recorded;
2. **the frozen items as honoured** — the two candidate lists unchanged and closed, **no candidate
   having changed type**, each candidate's obligations respected and checked, act 17's
   `GramTrajEquiv` used and no other relation, and each countercontrol either reached or recorded as
   not reached at the configuration this freeze names;
3. **`XS0`** — the bounded search, recorded in full, with the per-term result and the finding stated
   as a finding about the record;
4. **`XS1`** — the factorization theorem or its obstruction, with the `TJ1` dependence named at the
   step, with the corollary stated as being about propagation, with the false sentence about
   determination explicitly refused, and with the dependency's consequence for the pointwise
   candidates reported as this round's own theorem wherever `XS1` landed;
5. **`XS2`** — the three Type D parts, each reported separately with its frozen label and sentence,
   **obligation 3 stated against act 13's level-2 datum and never against the trajectory**, and each
   verdict stated of the exact frozen functional and of nothing in its neighbourhood;
6. **`XS3`** — the four Type L parts, each reported separately with its frozen label and sentence,
   each non-triviality witness reported as **one witness at one configuration carrying all four
   conjuncts**, **both propagation clauses reported separately** with the two non-propagation
   mechanisms kept apart, and the descent obligation reported as discharged or as the obstruction;
7. **`XS4` and `XS5`** — the two axis outcomes in the status rule's frozen wording, **reported as an
   ordered pair with neither ranked above the other**, with the obstruction named specifically in
   each UNDECIDED case and with each bounded no-go stated as bounded to its closed list;
8. **`P-D`** — the frozen structural prediction, reported against: whether any candidate reached the
   top of the `D`-axis, and if so whether what it discards relative to act 13's datum is threading
   and representative information and nothing else, with the falsification condition and its meaning
   stated where it is met;
9. **the well-posedness check as it stood at execution** — whether `D₀` still factors through `D₂` on
   the merged results this freeze names, and the record of the two-step chain;
10. **the scope boundary as honoured**: the confirmation that no statement of the round distinguishes
    two lifts `≈_O` identifies, that act 16's cancellation cell and the threading question are
    untouched in either direction, and that act 10's anchor-axis reclassification is untouched;
11. **the non-adoption clause carried verbatim at each mention**, with the count of carriages, and the
    confirmation that no candidate is adopted, endorsed or given physical status by surviving;
12. the frozen `P0` sentence for the case reached, composed from the frozen clauses, verbatim, and
    the row's label unchanged;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 10, 11, 12, 13, 14, 15, 16 and 17 — every merged label consumed, none
    revised — with act 13's level-2 result and act 17's `TJ1` and `TJ3` consumed at merged strength;
15. the definition count against the five-slot budget, with the conditional slot marked fired or
    unused;
16. the chronology certification, naming the property certified, the nine preconditions checked at
    `B`, and the archive-mode pins as unset at execution, with clause 9 reported as honoured by
    exclusion or by the exact mode-aware form;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **These are calls already
made**, written here so the record shows they were settled rather than left open. The body of this
freeze is written to them throughout; nothing below is a proposal, an option or a residual choice.

1. **The scientific scope is FROZEN as written and is not renegotiated.** No rung is added to either
   axis, neither axis is widened, and the candidate lists are closed. An execution that wants more
   freezes its own round.
2. **The headline is the ORDERED PAIR of two co-equal axis outcomes.** Neither axis is above the
   other and they answer different questions, exactly as act 17's two findings were reported on two
   axes. No composition of this round's wording ranks them.
3. **A candidate may NOT change type during execution.** Cross-time anchor coherence is frozen as two
   separate candidates, one of each type, for exactly that reason.
4. **Type L non-triviality is witnessed at ONE COMMON CONFIGURATION**, with all four conjuncts
   together. Split-configuration witnesses are refused and the reason is recorded: a law that permits
   everything at one configuration and exactly one trajectory at another passes both separated tests
   while being vacuous at the first and the answer in disguise at the second.
5. **Type D obligation 3 is stated against act 13's level-2 datum.** The trajectory phrasing is
   unsatisfiable exactly when the axis succeeds and is refused in terms.
6. **Propagation carries TWO clauses**, uniqueness from the initial orbit and the initial orbit
   contributing, because "a law plus one initial orbit propagates uniquely" says the initial orbit
   does work. A law that fixes every later slice by itself satisfies the first clause while the
   initial orbit contributes nothing, and calling that propagation would report a slice-by-slice
   determination as a cross-time relation. The two non-propagation mechanisms are kept apart and
   named.
7. **The `XS1` dependency is frozen in BOTH directions.** If the factorization lands, every pointwise
   candidate is ruled out as a route to the top of the `L`-axis as a theorem of this round, bounded to
   the notion of law this freeze defines; if it does not land, the pointwise candidates stay live and
   the `L`-ladder runs against the full list.
8. **`XS1` is NOT stated as "no pointwise constraint yields cross-time determination."** That sentence
   is false and is on the forbidden list. What fails is propagation.
9. **Act 13's level-2 result and act 17's `TJ1`, `TJ3` and `GramTrajEquiv` are consumed at merged
   strength**: not re-proved, not strengthened, not redefined. Every Type D candidate is mechanically
   bounded below act 13's datum by obligation 1.
10. **The lattice question is OUT OF SCOPE**, named as a non-doing so that it cannot creep in
    mid-execution.
11. **`P-D` is frozen as a prediction the round reports against**, with its forcing argument written
    out and its falsification condition and meaning stated, so that a falsification is reported as a
    misreading of a merged result rather than as a discovery about nature.
12. **The generator law carries a descent obligation that is part of the candidate.** Where the
    descent is not discharged, no propagation verdict is recorded for it.
13. **The execution uses the FROZEN configurations only**, from the frozen witness supply, at the
    configuration the countercontrol table names for each obligation. An alternative found during
    execution is recorded as an observation and never substituted.
14. **The round is SEALING, under the guard tag `R7-XTS`**, with `E` → `L` → `P` and `P` mandatory,
    and with chronology clause 9 honoured by excluding this round's own triple from the prior-seal
    integrity clause.

**One check was performed at drafting time and its outcome is recorded here as a settlement rather
than as a correction in flight.** The well-posedness of obligation 1 applied to the pair
`D_F = (D₀, F)` requires the anchored readback to factor through act 13's level-2 datum, and it does:
`fibreCrossGram_diag` gives the per-slice Gram tuple at the diagonal by definitional identity, and
act 12's `fibreGram_diag` gives the anchored readback from that tuple's diagonal with **no**
admissibility hypothesis. **Obligation 1 is therefore frozen for the full pair**, and the fallback of
stating it of `F` alone with the visible datum as a fixed-parameter comparison basis was considered
and is **not** used.
