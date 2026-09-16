# Track B act 17 — what selects or constrains the cross-time Gram/orbit trajectory: CONTROL PLANE

Owner-called. This file is the whole of act 17's control plane and is merged **alone**, before any
execution object exists. It takes up the part of `P0` that act 16 froze as the next separate
question: **what selects or constrains the Gram/orbit trajectory across time.** That is `P0`'s first
part in the programme's own words. It is **not** the threading part, which act 13 localized and
acts 14, 15 and 16 pursued carrier by carrier, and it is **not** the question of which representative
is chosen inside an orbit.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–778**, quoted verbatim at this base —
the numbered item's opening sentence, ending part-way through line 778:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes ownership of
>    changing existing seal state — takes a pin commit `P`, and `P` is mandatory.**

This freeze **creates new seal state**. The execution writes a new Lean module with its own guard
clause in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-TRJ`**, and that
clause carries the archive-mode constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_TRJ_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_TRJ_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_TRJ_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_TRJ_SEALED_HEAD` to `E` and `_TRJ_MERGE` to `L`, moving the `R7-TRJ` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_TRJ_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

**Why sealing rather than non-sealing, stated as a reason and not as a habit.** The execution adds a
new Lean module carrying this round's own named results, and the round's whole value depends on those
results having been reached **after** this freeze and from this freeze's base — a preregistered
search for selection principles that could be assembled after the outcomes were known would be worth
nothing. A new module with new named results is new seal state under `§A.37`'s definition, so the
round owns a pin and takes one. It owns **no other** seal state.

**The tag and its stem are free at this base, and the check is recorded.** At
`236a71a04a91895ed1fad84765b86288c06ca212`, `git grep -- 'R7-TRJ'` returns nothing anywhere in the
tree, `git grep -- 'TRJ'` returns nothing anywhere in the tree, and no constant whose name contains
the stem `_TRJ` exists in `verification/lean/edge_rigidity_probe.py`. The stem was chosen after
checking the alternatives: `_SEL` occurs as a substring of the existing `_A6P_SELF` and was rejected
for that reason, so that a stem search can never be ambiguous.

**What this round does NOT own, named exhaustively.** It alters **no existing seal constant**. In
particular `_RNC_BASE`, `_RNC_SEALED_HEAD` and `_RNC_MERGE` — act 16's seal — and `_TCF_BASE`,
`_TCF_SEALED_HEAD` and `_TCF_MERGE` — act 15's — and `_PQT_BASE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE`
— act 14's — and `_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE` — act 13's — and `_A12P_*`,
`_SGT_*`, `_TSG_BASE` and `_CLG_BASE` are **read and never written**. An archive seal belongs to the
round that set it: touching the guard file that carries those constants does not make this round
their owner, and the execution's diff against `edge_rigidity_probe.py` **adds** the `R7-TRJ` clause
and changes nothing else in the file.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`236a71a04a91895ed1fad84765b86288c06ca212`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

### The obligation itself, and the two-part structure in the programme's own words

`verification/ROADMAP.md`, **line 63**, the `P0` row's obligation cell and its status opening:

> | **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED: act 11's `GL2` proved the visible family does not fix the relative evolution;

and, from the same line, the sentence that makes the row two-part and names this round's part first:

> so what remains is **two-part**: what selects or constrains the Gram/orbit trajectory **across time**, and what determines the cross-time threading within those orbits, which act 11's `GL2` shows is not fixed even by the full Gram trajectory

and, from the same line, the clause act 16 added, which names this round's part as the one act 16
left standing:

> `P0`'s other part — what selects or constrains the Gram/orbit trajectory across time — is untouched, and nothing here names, endorses or excludes a selection principle.

### The statement that made `P0` two-part, with its coordinate

`verification/ROADMAP.md`, **lines 229–235**:

> **What this changes about `P0`.** The quotient by the defined two-sided action is classified
> exactly, and `P0` remains **two-part**: what selects or constrains the Gram/orbit trajectory across
> time, and what determines the cross-time representative — the threading — within those selected
> orbits. **Act 11's `GL2` shows the second is not fixed even by the full Gram trajectory**: a
> time-dependent strong right gauge fixes every anchored column, hence every fibre-Gram matrix at
> every time, yet changes the relative evolution. No connection, gauge-fixing mechanism, or selection
> principle is asserted. Both parts are the next frontier, and neither is act 12's.

### The interpretation boundary the whole of `P0` sits inside

`verification/ROADMAP.md`, **lines 52–57**:

> Accordingly, a failure of uniqueness at `P0` is not by itself a failure of quantum emergence. It
> determines the ontology of that emergence: either the residual lift freedom is physically redundant,
> additional structure selects one quantum history, or observational incompleteness determines only an
> equivalence class of quantum histories. Only an empirically distinguishable residual not removed by
> the physically appropriate equivalence relation would license a claim of physics beyond standard
> quantum mechanics.

### What act 11 left unconstrained about the shape of the determining structure

`verification/ROADMAP.md`, **lines 164–169**, beginning part-way through line 164 — the paragraph
opens at line 162, and the span quoted here is the part that governs this round:

> Act 11 does **not** constrain that structure's shape. `GI2` does not do it: its
> witness lies outside the weak class yet has *identical* relative objects, so it separates the lift
> space from the gauge class without separating the relative evolutions. **The shape question stays
> open**, and what would bear on it is a same-visible pair that is **both** outside the weak class
> **and** different in relative evolution. Act 11 supplies none and shows neither that one exists nor
> that one cannot.

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 697–700**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `236a71a04a91895ed1fad84765b86288c06ca212`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/preregistration.md` | `48099a3b334e8d01f31af706e8738cd49cfca774` |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/result.md` | `b13d684cb7454ff414a34ed9b6dca39065c3470f` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` | `fe8df06ffefac22ce87668ecf026f4c9ebc5c13f` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md` | `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md` | `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md` | `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
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
| `verification/ROADMAP.md` | `c59efc91a8730c285598fe41d29b98b271bde986` | **read** as the pinned statement of the `P0` row, of its two-part structure and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `6d2e2ea7e4b6beeff717a53497870904d2bd6cef` | the `R7-TRJ` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `fa2d1341c40a08891a5fc7b41c925ae0abd645f5` | one import line added after act 16's module |
| `verification/lean-manuscript-census.json` | `59d9f724422ff778f30fce0a72d326e52853a07b` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one prose file this round both reads and writes, and it is listed
here rather than above for exactly that reason: the verbatim clause governs the read-only table
without qualification, and the `ROADMAP`'s treatment is stated in its own row. If its blob differs
at the base, the execution records the discrepancy and does not repair the freeze.

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
against `236a71a` alone and consumes nothing from any of them. No lane's unlanded output is read,
cited, compared or waited for.

## Source scoping, carried from acts 13 through 16

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what act 16 left in front of it

Act 16 answered the cancellation question on the re-anchored-channel carrier and reached `RN3⁺`. Its
own closing settlement names this round's subject and parks it. From
`act-16-reanchored-channel-cancellation/preregistration.md`, **lines 1275–1278**:

> 3. **Cross-time Gram/orbit selection is the next separate `P0` question, and stays out of scope
>    here.** What selects or constrains the Gram/orbit trajectory across time is `P0`'s other part.
>    It is not asked, not bounded and not prejudged by this round, it remains a non-doing of this
>    freeze, and no outcome reached here bears on it in either direction.

**This round takes that question up.** It bounds it, and the whole of the bounding is frozen here,
before any theorem is searched for: the candidate selection principles, the data each may read, the
cross-time equivalence relation, and the countercontrol for each candidate. Those four are the heart
of the round and each has its own section below.

### What the merged record supplies for this part, and what it does not

This table is a reading of the merged record, stated so that the gap this round works in is visible
and so that no target of this round has to discover it. Each cell cites the merged label that fills
it.

| question about the Gram/orbit trajectory | what the merged record says | label |
| --- | --- | --- |
| what the per-slice orbit is | classified exactly: the orbits of the two-sided uniform gauge are determined by the fibre-Gram data modulo the anchored phases | act 12's `TG2` |
| which per-slice Gram tuples occur | exactly the realizable ones: positive semidefinite, rank at most `\|A\|`, summing to the identity, diagonal equal to the visible slice | act 12's `SH1`, both directions |
| whether the visible law fixes the per-slice orbit | **no in general** — two admissible dilations of one law lie in different orbits — and **yes on deterministic laws** | act 12's `TG3`; act 12's `SH1-C2` |
| whether the per-slice orbit trajectory can change under a constant visible law | **yes** — exhibited | act 12's `TG3`, lifted form |
| whether the Gram trajectory fixes the threading | **no** — a strong right gauge fixes every fibre-Gram matrix at every time and still moves the relative evolution | act 11's `GL2`, as the `ROADMAP` states it |
| what constrains the trajectory **across** time | **nothing on the record** | — |

**That last row is this round's subject.** The merged record constrains the trajectory slice by
slice and says nothing whatever about a coupling between slices. Whether that silence is a gap or is
the answer is what the round's first target asks of the record and what its second target asks of
the kernel.

## The strength of the ask, FROZEN

**The ask is CONSTRAINTS-ONLY.** The round asks whether anything **excludes** cross-time Gram/orbit
trajectories, and it does **not** undertake to produce a principle that picks out a single one, nor
a classification of the admissible set. That is the round's obligation, and falling short of
uniqueness or of classification is **not** a shortfall of this round.

**Why constraints-only and not the two stronger asks, recorded as a reason.** The candidates that
would deliver uniqueness all read the visible law, and the merged record already carries a witness —
act 12's `TG3` — of two admissible dilations of one visible law in different per-slice orbits, so a
uniqueness ask would preregister an obligation the freeze has strong reason to think unreachable
from the licensed data. A classification ask would additionally require the surjectivity obligation
of line 2 below, over the whole trajectory space of an arbitrary finite carrier, which this round's
definition budget does not fund and which no merged result supplies. Constraints-only is what the
round can honestly attempt, and it is what the graded hierarchy is calibrated to.

**What the other two asks would have changed.** A uniqueness ask would have made line 1 of the
hierarchy the round's obligation and every lower line a shortfall, would have required a prediction
for line 1 at a strength this freeze cannot justify, and would have made UNDECIDED a failure rather
than a live preregistered outcome. A classification ask would have made line 2 the obligation, would
have required a definition slot for the parameter type and its map, and would have made the
completeness direction a mandatory rather than a conditional target.

**The ask does not narrow what may be reported.** Lines 1 and 2 of the graded hierarchy below are
**preregistered as reachable outcomes with their own frozen post-round sentences**, at the full
evidence bar frozen for them, and rated *not predicted* at low. This is the round's answer to the
scope question the hierarchy raises: a stronger result is reportable **because it was preregistered
as reachable**, and never because the execution enlarged the round after finding it. **The scope is
fixed here, before the search.** The alternative reading — parking a proved uniqueness or
classification theorem as an out-of-scope observation with the reported outcome held inside the
settled ask — is drafted at the owner-decision section below and is the owner's to choose.

## The scope boundary against threading and representative choice, FROZEN

**Act 17 asks about the trajectory. It does not ask which lift threads it, and it does not ask which
representative is chosen inside an orbit.** This boundary is not a stylistic preference and it is not
enforced by prose alone: it is enforced by the round's equivalence relation and by its data regime,
both frozen below, and the enforcement is mechanical.

1. **The threading question belongs to act 13 and to acts 14, 15 and 16.** Act 13 localized the
   residual threading freedom exactly — relative to the fibre cross-Gram trajectory it is a
   strong-right family modulo a constant together with one constant in-fibre frame. Acts 14, 15 and
   16 asked what that residual means relative to four frozen carriers of observables. **None of those
   questions is asked here, in either direction.**
2. **Every pair act 13 localized as threading-related is ONE trajectory for this round.** If
   `U'_t = W · U_t · K_t` with `W ∈ 𝒢_L` constant and `K_t` strong at every `t`, then
   `FibreGram a₀ (U'_t) i = FibreGram a₀ (U_t) i` for every `t` and every fibre `i` — by act 12's
   `fibreGram_left_mul` on the left factor and act 13's `ct3g_fibreGram_strong_right` on the right —
   so the two lifts have the **same** Gram trajectory, hence the same trajectory under this round's
   equivalence with the trivial phase family. **The threading freedom is invisible to every object
   of this round.**
3. **Act 11's `GL2` pair is one trajectory for this round.** That pair shares every fibre-Gram matrix
   at every time and differs in relative evolution. This round sees one trajectory there and says
   nothing whatever about the difference, which is exactly why the trajectory question and the
   threading question are different questions and not two phrasings of one.
4. **The representative choice inside an orbit is likewise invisible.** The round's equivalence takes
   the per-slice `∼_D` class and never the raw Gram representative, so which Gram matrix inside a
   phase class a lift realizes is not a distinction this round can make, state or use.
5. **The cost of the boundary, stated plainly.** Because the boundary is enforced by the equivalence
   and not merely declared, **no outcome of this round can bear on the relative evolution, on the
   threading, or on any carrier of act 14.** That is a real cost and it is accepted deliberately: a
   relation that could see the threading would make every trajectory statement a statement about the
   threading too, and the round would be asking both parts of `P0` at once.

## The act 16 anti-conflation clause, FROZEN VERBATIM

Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are the nearest positives to this round's subject and are the
ones most easily misread into it. The clause below is **THE CLAUSE**, and it is carried as a block
quote **at every prose mention of act 16's positive as bearing on trajectory freedom** in this file
and in every artifact of this round.

**How each carriage is written, and why.** Each carriage opens with one line naming where it is
being carried, and then states the clause word for word. The naming line is there so that the
carriages read as distinguishable copies of one clause rather than as one paragraph pasted
repeatedly — which is a defect the repository's duplicate check exists to catch — and it changes
nothing about the clause it introduces. Acts 15 and 16 established this pattern and this round
follows it.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed post-round
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name act 16's labels among the labels this round does not touch.

**THE CLAUSE:**

> Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
> that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
> re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
> time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
> statement about the threading pair on a named carrier, and it is not a statement about the
> cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
> those two carriers **does not license the assumption that all residual trajectory freedom is
> gauge**: act 16 established a cancellation on named carriers and established **nothing** about
> whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
> rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
> treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
> is physical; no target of this round consumes either for that purpose; and no candidate selection
> principle is named, rated, predicted, admitted or refuted on their strength.**

Act 16's and act 15's positives therefore appear in **analysis only**. **No target of this round is
carried by them**, no target cites them as evidence, and no determination changes sign or strength
because of them. Writing an outcome of this round as if act 16's cancellation bore on the trajectory
freedom, or as if a trajectory outcome bore on act 16's carriers, is a **defect of this round** and
is checked for in the final report.

For the reader's convenience, act 16's own statement of what its positive is about, quoted verbatim
from `act-16-reanchored-channel-cancellation/result.md`, lines 213–218 — and governed by the clause
above:

> **What `RN3-a⁺` does not establish.** It settles **one triple**. It is not a universal statement
> about triples, and it is not a bound on what a later round could exhibit in either direction. It is
> **not** a statement that `𝒪₃` and `𝒪₂` agree in general, and it is **not** a statement that either
> carrier is observable. **Act 15's `PQ3-d⁺` on `𝒪₂` stands exactly as act 15 states it** and is not
> weakened, qualified, revised or enlarged by this: the two are verdicts on different carriers, and
> neither is evidence about the other.

> **THE CLAUSE, carried at this mention — the quotation of act 16's own bound on its positive.**
> Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
> that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
> re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
> time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
> statement about the threading pair on a named carrier, and it is not a statement about the
> cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
> those two carriers **does not license the assumption that all residual trajectory freedom is
> gauge**: act 16 established a cancellation on named carriers and established **nothing** about
> whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
> rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
> treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
> is physical; no target of this round consumes either for that purpose; and no candidate selection
> principle is named, rated, predicted, admitted or refuted on their strength.**

**One resemblance is recorded here so that it is not mistaken for a bridge, in this round's own
terms.** Act 16's triples and this round's trajectories are both built from the same lift and the
same two group actions, and act 16's `RN2` runs between two carriers' equalities. But act 16's
objects live where a constant in-fibre left move and a strong right family **can be seen**, and this
round's equivalence is constructed so that neither can be seen at all. The two rounds therefore
quantify over different things and **neither would establish the other**. Recording the resemblance
is not transferring it, and no target of this round is stated over act 16's objects.

## Naming a candidate is not endorsing it, FROZEN

Acts 11, 12, 13, 14, 15 and 16 each carry the non-doing "names, endorses or excludes no selection
principle". **This round names selection principles, and it must, because it cannot test what it
cannot name.** The reconciliation is frozen here so that it cannot be improvised afterwards.

1. **Naming is for testing.** Each candidate below is named as an **object of test** and for no other
   purpose. Naming it is not proposing it, not adopting it, not asserting that it is the right shape,
   and not asserting that the programme needs a selection principle at all.
2. **The round still endorses none.** No outcome of this round endorses any candidate, and no
   sentence of any artifact of this round says that a selection principle is required, on any
   carrier or carrier-free.
3. **Exclusion is only ever of the precise stated form.** Where a candidate is refuted, what is
   refuted is the **exact proposition frozen below under that candidate's label**, on the exact data
   grant frozen for it, and nothing in its neighbourhood. A refutation of `SP3` as this freeze states
   it is not a refutation of any other memorylessness or homogeneity condition, and the result note
   says so at each such refutation.
4. **The candidate list is closed at this freeze.** The execution tests these candidates and no
   others. A candidate discovered during execution is **recorded as an observation and not executed**,
   and belongs to a later round with its own freeze.

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12 and 13

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `Γ : ℕ → Matrix V V ℝ` a **visible
family**, `U : ℕ → U(V × A)` a lift, and the following are consumed **unmodified**, at their own
strengths: `readback`, `AdmissibleDilationAt`, `admissible_mul_of_fixes_anchor`,
`readback_isColStochastic`, `readback_relabel` (`R-3`), `one_admissible_at_every_anchor`,
`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `strong_mem_weak`,
`gl2_strong_gauge_moves_relative_candidate` (`GL2`), `gl3_constant_gauge_preserves_relative` (`GL3`),
`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`fibreGram_apply`, `fibreGram_diag`, `fibreGram_diag_of_admissible`, `fibreGram_posSemidef`,
`fibreGram_rank_le`, `sum_fibreGram`, `fibreGram_left_mul`, `left_preserves_admissible`,
`fibreGram_mul_weak_apply`, `gramPhaseEquiv_of_twoSided`, `twoSided_slice_iff`,
`twoSidedRelated_iff` (`TG2`, lifted), `gramPhaseEquiv_cross_invariant`, `hadamard_cross_ratio`,
`hadamard_slices_not_twoSided`, `hadamard_lifts_not_twoSided` (`TG3`), `sh1_necessity`,
`sh1_sufficiency`, `sh1_shape` (`SH1`), `sh1_c1`, `fibreGram_of_deterministic`,
`sh1_c2_at_most_one`, `sh1_c2_unique_orbit` (`SH1-C2`), `ro1_right_only_insufficient` (`RO1`),
`FibreCrossGram`, `fibreCrossGram_diag`, `ct2b_fibreCrossGram_iff` (`CT2` (b)),
`ct3g_fibreGram_strong_right` and `ct3g_fibreCrossGram_strong_right` (`CT3` (G)),
`ct4_constant_left_obstruction` (`CT4`) and `cl1_constant_left_moves_relative_candidate` (`CL1`).

**The Gram trajectory of a lift**, written `𝔾(U)`, is the family `fun t => FibreGram a₀ (U t)` —
one tuple of `V × V` matrices per time. Act 12 defines `FibreGram` and applies it to a single
dilation; this round needs the whole `ℕ`-indexed family, because every statement below quantifies
over all times at once.

**The per-slice orbit** of a lift at time `t` is the `GramPhaseEquiv`-class of `FibreGram a₀ (U t)`,
which act 12's `TG2` proves is exactly the orbit of the two-sided uniform gauge at that slice. **The
Gram/orbit trajectory** is the sequence of those classes, and the round's equivalence relation below
is what says when two lifts have the same one.

**Act 7's boundary is carried at every use of the visible family**, exactly as acts 11 through 16
carry it: act 7's `D4b` came back **negative** — Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V` — and the readback is the repository's own,
frozen by act 7's readback amendment. Every statement in this round about what is visible is a
statement under that convention, said at each use rather than once in a footnote.

## Frozen item 3 — the cross-time equivalence relation, `≈_O`

**What counts as the same cross-time trajectory for this round, stated once and used everywhere.**

> **`≈_O` — the round's frozen cross-time equivalence.** Two lifts `U`, `U'` over one carrier and
> anchor have the **same trajectory** iff for **every** time `t` the per-slice Gram tuples are
> phase-equivalent: `GramPhaseEquiv (FibreGram a₀ (U t)) (FibreGram a₀ (U' t))`. The phase family is
> chosen **independently at each time** and is not required to be the same at two times.

Stated directly on trajectories rather than on lifts: two Gram trajectories `𝔾`, `𝔾'` are the same
iff `GramPhaseEquiv (𝔾 t) (𝔾' t)` for every `t`. That is the relation this round's Lean module names
`GramTrajEquiv`, definition slot 1, and it is the **only** relation any quotient in this round is
taken over.

**Where `≈_O` sits relative to act 12's relation.** It **is** act 12's lifted two-sided relation, on
unitary lifts: `twoSidedRelated_iff` proves `TwoSidedRelated a₀ U U'` iff
`∀ t, GramPhaseEquiv (FibreGram a₀ (U t)) (FibreGram a₀ (U' t))`. So `≈_O` adopts act 12's per-slice
quotient **pointwise in time and adds no cross-time identification of its own**. Act 12's relation is
**consumed, not redefined**; what this round adds is a name for it as a relation on **trajectories**,
so that it can also compare trajectories that are not yet known to be a lift's — which is what line 2
of the hierarchy and the `TJ1` statement both need.

**Where `≈_O` sits relative to act 13's relation, demonstrated and not asserted.** `≈_O` is
**strictly coarser** than act 13's level-2 relation. If `U'_t = W · U_t · K_t` with `W ∈ 𝒢_L`
constant and `StrongAnchorStabilizer a₀ (K t)` for every `t` — which is act 13's residual threading
freedom exactly, and is literally the `TwoSidedRelated` shape with `L_t := W` and `K_t` strong hence
weak — then `FibreGram a₀ (U'_t) = FibreGram a₀ (U_t)` at every `t`, by `fibreGram_left_mul` and
`ct3g_fibreGram_strong_right`, so `U ≈_O U'` with the constant phase family `c ≡ 1`. **Every pair
act 13's `CT2` (b) leaves undetermined is identified by `≈_O`.** The converse fails: act 12's
Hadamard slices are `≈_O`-inequivalent and are not threading-related either, so the coarsening is
proper in the direction the round needs.

**Three relations this round deliberately does NOT adopt, each named so that it cannot be adopted by
accident.**

- **Raw Gram equality**, `FibreGram a₀ (U t) = FibreGram a₀ (U' t)` at every `t`. This is **strictly
  finer** than `≈_O`: act 13 records that raw level-0 equality is a representative-level equality,
  moved by the weak right action with anchored phases, and sufficient but not necessary for
  membership in one two-sided orbit. Adopting it would make the round able to see the representative
  choice inside an orbit, which boundary clause 4 above forbids.
- **Uniform-phase equality** — the same relation with **one time-independent** phase family `c`.
  This is also strictly finer than `≈_O`, and it is finer in exactly the direction the round is
  supposed to be testing: it couples the slices. **Assuming a cross-time coupling in the equivalence
  relation would answer the round's question in the relation rather than in the kernel**, and the
  freeze refuses it for that reason. It is recorded here as a distinct relation, neither adopted nor
  excluded as an object of a later round.
- **Act 13's level-2 or level-3 cross-time relations.** These see the threading and are outside the
  boundary.

**Two consequences of `≈_O` worth stating in advance.** Phase equivalence preserves the diagonal,
since `star (c j) * G i j j * c j = G i j j` when `‖c j‖ = 1`; so `≈_O`-equivalent coherent lifts
have the **same visible family**, by `fibreGram_diag_of_admissible`. And `≈_O` is an equivalence
relation on trajectories, which the execution proves or records as an obstruction before any quotient
is taken over it.

## Frozen item 2 — the data regime, and the per-candidate data grants

**The failure mode this section exists to make impossible** is a candidate that quietly reads data
the round has not licensed, and thereby "selects" a trajectory by having been handed it. The line is
drawn here, before any candidate is stated.

### The constrained object, and the licensed side data

**The object a candidate constrains** is the Gram/orbit trajectory: the sequence `t ↦` the
`GramPhaseEquiv`-class of `FibreGram a₀ (U t)`. A candidate is a condition **on that object**.

**The licensed side data, `L` — what a candidate may consult.** Exactly these, and nothing else:

| licensed datum | what it is | why it is licensed |
| --- | --- | --- |
| the visible family `Γ : ℕ → Matrix V V ℝ` | the anchored readback at each time, under act 7's convention with `D4b` negative | it is the operationally visible datum of the whole programme, and `SH1` proves it is exactly the diagonal of the Gram data |
| the time index `ℕ`, with its successor and its order | the index structure `CoherentLift` already carries | the question is about time, and the index is all the time structure the programme has; **no metric, no continuity, no derivative and no continuum limit** |
| the cardinalities `\|V\|` and `\|A\|` and the anchor `a₀` as a label | the carrier data every merged statement carries | they are parameters of the setting, not facts about the lift |

**The forbidden data, `F` — what no candidate in the frozen class may consult.** Exactly these, and
whatever is definable from them:

- **the lift `U` itself**, at any time;
- **the raw fibre-Gram representative** `FibreGram a₀ (U t)` as a matrix, as opposed to its
  `GramPhaseEquiv`-class — reading the representative would let a candidate detect the choice inside
  an orbit, which `≈_O` quotients away;
- **act 13's cross-time data at every level** — the fibre cross-Gram `FibreCrossGram`, the anchored
  block, and the full column cross-Gram `CrossGram`;
- **act 14's four carriers** `𝒪₀`, `𝒪₁`, `𝒪₂`, `𝒪₃`, the relative object `U_t U_sᴴ`, the relative
  candidate and the anchored channel;
- **anything from acts 15 and 16**, whose statements are about the carriers above;
- **anything from the substratum Lemma 24.1 rounds or from Track I.**

**Why the line falls there, stated as the reason it is.** `L` is the operationally visible data of
the programme together with the bare index structure. `F` is structural or kernel data: objects that
exist in the formalization and are coordinates on the lift space, which act 12 and act 13 both say in
terms of the Gram data. **A candidate allowed kernel data can "succeed" in a way that answers a
different question than `P0` asks** — it can select a trajectory by reading something that already
determines it — and the round is designed so that no member of its selector class can do that.

**The one deliberate exception, and it is outside the class.** `SP4` below is granted act 13's
level-2 cross-time data **on purpose**, as a **regime probe**: it exists to record, as a theorem
rather than as a warning, what happens when the line is crossed. **`SP4` is not a member of the
frozen selector class `𝒮`**, no line of the graded hierarchy quantifies over it, and no outcome of
`SP4` is evidence for or against any member of `𝒮`.

### The per-candidate data grants

| candidate | in `𝒮`? | may consult | may not consult |
| --- | --- | --- | --- |
| `SP1L` | yes | `Γ`, the index `ℕ` | everything in `F` |
| `SP1G` | no — it is a determination claim, not a selector | `Γ`, the index `ℕ` | everything in `F` |
| `SP2` | yes | `Γ`, the index `ℕ` | everything in `F` |
| `SP3` | yes | the index `ℕ` and its successor only | `Γ` as well as everything in `F` |
| `SP5` | yes | `Γ`, the index `ℕ` | everything in `F` |
| `SP4` | **no — regime probe** | act 13's level-2 fibre cross-Gram trajectory | — |

**`SP3`'s grant is narrower than the others' on purpose.** A homogeneous transition rule that may
read the visible law at each step is a different and weaker proposition than one that may not; the
freeze states the law-free form as `SP3` and records the law-reading variant as **named and not
executed**, belonging to a later round.

## Frozen item 1 — the candidate selection principles

**Five candidates plus one regime probe. The list is closed.** Each is stated as a proposition in
the programme's vocabulary, with its provenance named. `𝒢_L` is act 12's `LeftFibreGroup`, `𝒢ˢ_{a₀}`
act 11's `StrongAnchorStabilizer`, and `[G]` the `GramPhaseEquiv`-class of a tuple `G`.

### `SP1L` — the per-lift law-determination constraint

> **Statement.** For every coherent lift `U` of every visible family `Γ`, and all times `t`, `s`:
> if `Γ t = Γ s` then `[FibreGram a₀ (U t)] = [FibreGram a₀ (U s)]`.

A condition on one lift's trajectory, parameter-free, consulting only `Γ` and the index. **Where it
comes from.** Act 12's `SH1` proves the visible law is exactly the diagonal of the Gram data, which
makes "the rest of the Gram datum is a function of its diagonal" the first candidate any reader
reaches for.

### `SP1G` — the cross-lift law-determination claim

> **Statement.** For all coherent lifts `U` of `Γ` and `U'` of `Γ'` over one carrier and anchor, and
> all times `t`, `s`: if `Γ t = Γ' s` then `[FibreGram a₀ (U t)] = [FibreGram a₀ (U' s)]`.

**This is a determination claim, not a selector.** It is a universal statement across lifts, and if
true it would supply a canonical map from visible laws to per-slice orbits and hence genuine
selection from the licensed data — it is the round's only route to uniqueness from `L`. **It is not a
predicate on a single lift**, so it is **not** a member of `𝒮` and no line of the hierarchy
quantifies over it; its verdict is reported at its own target. `SP1G` implies `SP1L` and `SP1L` does
not imply `SP1G`, by the shape of the quantifiers alone: `SP1L` is `SP1G` restricted to `U = U'`.
**So `SP1G` is strictly the stronger**, and no prediction in this freeze rates it above `SP1L`.

**Where it comes from.** Act 12's `SH1-C2` proves it **on deterministic visible laws**: there the
orbit is unique, so the law does determine it. `SP1G` is that island's proposed extension to all
laws.

### `SP2` — orbit stationarity under a constant visible law

> **Statement.** For every coherent lift `U` of every visible family `Γ` that is **constant in time**,
> and all times `t`, `s`: `[FibreGram a₀ (U t)] = [FibreGram a₀ (U s)]`.

**Where it comes from.** The "no hidden dynamics beyond the visible law" shape. Act 13's `CT3` (b)
names act 12's Hadamard pair "the trajectory-type control", which is what this candidate is measured
against. `SP1L` implies `SP2` and `SP2` does not imply `SP1L`: `SP2` is `SP1L` restricted to constant
families. **So `SP2` is strictly the weaker of the two**, and no prediction rates `SP1L` above `SP2`.

### `SP3` — a homogeneous transition rule on the orbit trajectory

> **Statement.** For every coherent lift `U` of every visible family, and all times `t`, `s`: if
> `[FibreGram a₀ (U t)] = [FibreGram a₀ (U s)]` then
> `[FibreGram a₀ (U (t+1))] = [FibreGram a₀ (U (s+1))]`.

**The parameter-free form is the frozen one.** The equivalent shape "there is one map `Φ` on orbit
classes with `[G_{t+1}] = Φ([G_t])` for every `t`" quantifies over functions on a quotient and is
**not** what the execution states; the displayed form says the same thing without the quotient
construction and is what the kernel carries. The two are recorded as the same proposition and the
execution uses the displayed one.

**Where it comes from.** It is the memorylessness-and-homogeneity shape — one time-independent rule
stepping the hidden datum forward — which every prior act's non-doings list names as a condition it
declines to introduce. It is named here as an object of test and is not introduced as a condition of
this round.

### `SP5` — the decoherence rule: the orbit is the diagonal tuple

> **Statement.** For every coherent lift `U` of every visible family `Γ` and every time `t`:
> `[FibreGram a₀ (U t)] = [fun i => Matrix.diagonal (fun j => ((Γ t) i j : ℂ))]` — the per-slice
> orbit is the class of the tuple whose `i`-th matrix is the diagonal matrix with entries
> `(Γ t) i j`, and which therefore carries no off-diagonal Gram mass at all.

A named function of the licensed datum `Γ` alone, so it is a genuine selector in the sense line 1 of
the hierarchy requires: **if it held it would pick the trajectory outright from the visible family**.

**Where it comes from.** Act 12's `SH1` says the residual freedom after the two-sided gauge is
exactly the off-diagonal Gram data, so "there is none" is the sharpest possible selection rule in
that vocabulary; and act 12's `fibreGram_of_deterministic` proves the closed form
`G^{(i)}_{jk} = δ_{jk} Γ_{ij}` for deterministic slices, which is exactly this candidate's value
there. **`SP5` implies `SP1G`**, since it exhibits the required function of the law, and `SP1G` does
not imply `SP5`. **So `SP5` is strictly the strongest of the four law-facing candidates**, and the
frozen chain is `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2`, with no implication reversing. **No prediction in this
freeze rates a stronger member of that chain above a weaker one.**

### `SP4` — the regime probe: cross-time data determination

> **Statement.** For all coherent lifts `U`, `U'` over one carrier and anchor: if
> `FibreCrossGram a₀ U i t s = FibreCrossGram a₀ U' i t s` for every fibre `i` and all times `t`, `s`,
> then `U ≈_O U'`.

**`SP4` is outside the frozen selector class and is executed as a probe of the data regime.** It
reads act 13's level-2 cross-time datum, which is forbidden to every member of `𝒮`. Its expected
verdict is the point of executing it: act 13's `fibreCrossGram_diag` is a definitional identity,
`FibreCrossGram a₀ U i t t = FibreGram a₀ (U t) i`, so the level-2 datum **contains** the Gram
trajectory, and a rule permitted to read it determines the trajectory by containing it. **That is a
theorem about containment and not a selection**, and the frozen wording for its outcome says so.

### The frozen selector class `𝒮`

> **`𝒮` has exactly four members: `SP1L`, `SP2`, `SP3` and `SP5`.** These are the per-lift
> predicates, each parameter-free, each consulting only licensed data. `SP1G` is a determination
> claim and `SP4` is a regime probe; **neither is in `𝒮`**, and no statement quantifying over `𝒮`
> says anything about either. **The membership of `𝒮` is fixed by this freeze and does not change
> during the execution.**

## Frozen item 4 — the countercontrols, one per candidate

**A negative result is reportable because its shape was fixed before the search.** For each candidate
the freeze states here what a negative answer looks like concretely and what evidence earns it. Two
distinct questions are asked of each member of `𝒮`; `SP1G` and `SP4` are asked one question each.

**Question (A) — addition or theorem?** Does the candidate hold of every coherent lift?

- **Countercontrol shape**: an **exhibited** coherent lift of an **exhibited** visible family whose
  trajectory violates the candidate, with the violating times named and the inequivalence of the two
  orbit classes proved in the kernel.
- **Evidence that earns it**: a Lean theorem at evidence level 2 whose statement pins the family and
  the lift by equations, carries `CoherentLift` for the lift as a conjunct, and carries the negated
  `GramPhaseEquiv` at the named times as a conjunct.
- **What a negative here means**: the candidate is **additional structure**, which is what a
  selection principle must be. A negative at (A) is **not** a criticism of the candidate; a positive
  at (A) is, because a candidate that is already a theorem selects nothing.

**Question (B) — does it select?** Fix a configuration: a carrier, an anchor and a visible family
`Γ` admitting at least one coherent lift. The candidate **selects at that configuration** iff the set
of `≈_O`-classes of `{𝔾(U) : U` a coherent lift of `Γ` satisfying the candidate`}` has **exactly
one** element.

- **Countercontrol shape 1, non-selection**: two **exhibited** coherent lifts of one exhibited visible
  family, **both satisfying the candidate**, whose trajectories are `≈_O`-inequivalent, with the
  separating time and the separating invariant named.
- **Countercontrol shape 2, emptiness**: an exhibited visible family with an exhibited coherent lift,
  such that **no** coherent lift of it satisfies the candidate — a universal statement over the
  lifts of that family, proved, not searched.
- **Evidence that earns either**: a Lean theorem at evidence level 2 with the objects pinned by
  equations. For shape 1 the two lifts' coherence is discharged from merged results and the
  inequivalence is certified at a named time through a named `∼_D`-invariant. For shape 2 the
  exclusion is proved from a merged necessity result, with the excluded quantity computed.
- **Why the two shapes are kept apart**: both are failures to select, and the mechanisms are opposite
  — too many survivors against none at all. Reporting one as the other is a defect.

### The countercontrol named for each candidate, in advance

| candidate | question | the countercontrol this freeze names | what it would consume |
| --- | --- | --- | --- |
| `SP1L` | (A) | act 12's `TG3` lifted pair: the coherent lift of the **constant** visible law `Γ ≡ ¼` on `\|V\| = 4`, `\|A\| = 1` that is `H(1)` at `t = 0` and `H(i)` afterwards, whose orbit classes at `t = 0` and `t = 1` are inequivalent | `hadamard_lifts_not_twoSided`, `hadamard_slices_not_twoSided` |
| `SP1L` | (B) | the two **constant** coherent lifts `U ≡ H(1)` and `U' ≡ H(i)` of that same family: both satisfy `SP1L` trivially, and their trajectories are `≈_O`-inequivalent at every time | `hadamard_slices_not_twoSided`, `gramPhaseEquiv_cross_invariant` |
| `SP1G` | (A) | the same two constant lifts, read across lifts at `t = s = 0` | `hadamard_slices_not_twoSided` |
| `SP2` | (A) | the same lifted `TG3` pair, whose visible family is constant and whose orbit is not | `hadamard_lifts_not_twoSided` |
| `SP2` | (B) | the same two constant lifts: both stationary, `≈_O`-inequivalent | `hadamard_slices_not_twoSided` |
| `SP3` | (A) | the coherent lift of the constant family whose slices are `H(1)`, `H(i)`, `H(1)`, `H(1)` at `t = 0, 1, 2` and `t ≥ 3`: the orbits at `t = 0` and `t = 2` agree while those at `t = 1` and `t = 3` do not | `hadamard_slices_not_twoSided`, admissibility of each slice |
| `SP3` | (B) | the same two constant lifts: each is trivially a homogeneous trajectory, and they are `≈_O`-inequivalent | `hadamard_slices_not_twoSided` |
| `SP5` | (A) | `H(1)` itself: at `\|A\| = 1` the tuple is `G^{(i)}_{jk} = conj(H_{ij}) H_{ik}`, whose off-diagonal entries are nonzero, so the trajectory is not the diagonal one | `fibreGram_apply` |
| `SP5` | (B) | **emptiness** at the Hadamard family: the diagonal tuple for `Γ ≡ ¼` on `\|V\| = 4` is `(1/4)·I₄` in every fibre, of rank `4`, and `\|A\| = 1`, so act 12's `fibreGram_rank_le` excludes it from being any admissible dilation's Gram tuple — while the family has coherent lifts | `fibreGram_rank_le`, `sh1_necessity`, `hadamard_slices_not_twoSided` |
| `SP4` | (A) | **none is named**: the freeze predicts `SP4` is a theorem, by `fibreCrossGram_diag`, and the finding is the containment | `fibreCrossGram_diag` |

**One witness family, several consequences — reported as one witness and its consequences.** Act
12's Hadamard objects at `Γ ≡ ¼`, `|V| = 4`, `|A| = 1` carry most of the countercontrols above. The
execution reports that as **one merged witness family and the consequences this round draws from
it**, and never as several independent findings. The frozen chain `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2` means a
refutation of the weakest refutes all four, and the result note states the propagation rather than
restating a discovery four times.

**The countercontrols consume merged witnesses; they do not enlarge them.** Act 12's `TG3` and
`SH1-C2` are consumed at their own strengths — `TG3` existentially, about its own exhibited
dilations, and `SH1-C2` as an at-most-one statement about deterministic slices — and neither is
enlarged, restated or revised by anything here.

## The evidence rule, FROZEN

`TJ0` is settled by **locating and quoting**, not by proving a theorem. Its evidence rule is frozen
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
`TJ0`. No line of the graded hierarchy is earned by the absence of a witness: line 4 in particular
requires an **exhibited** countermodel and is **not** earned by a failed search, which belongs at
line 5 with the obstruction named. The same rule forbids concluding that a candidate is a theorem
because no violating lift was found.

**The bounded search for `TJ0` is fixed now**, so that its boundary cannot be chosen after its result
is known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/` and under
  `verification/lean/`; every `preregistration.md` and `result.md` under
  `verification/programmes/oi-qm/`; and `verification/ROADMAP.md`. The set is taken from
  `git ls-tree -r --name-only B`, so untracked package trees are outside it by construction.
- **The search terms**: `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `TwoSidedRelated`,
  `CoherentLift`, `trajector`, `select`, `stationar`, `diagonal`, and the merged label names `TG2`,
  `TG3`, `SH1`, `RO1`, `CT2`, `CT3`, `CT4`, `GL2`.
- **The question asked of each hit**: does this declaration decide, for some visible family or for
  every visible family, whether the Gram/orbit trajectory is constrained **across time** beyond the
  per-slice realizability of `SH1` — or does it decide, for any member of `𝒮` or for `SP1G`, whether
  that candidate holds of every coherent lift or selects at any configuration?
- **The recorded answer per hit** is one of: *supplies it* (quoted, with coordinate); *does not
  supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

The execution records the search in the result note in full. **A search that finds a decision is a
finding, and a search that does not is equally a finding** — the second being that the record is
silent on the point, which is what `TJ0` asks.

## The targets, FROZEN

Four targets, `TJ0` through `TJ3`. Each names what settles it and what evidence counts.

### `TJ0` — does the merged record decide the trajectory question, in either direction?

**The question.** At this freeze's base, does the merged record contain any statement — universal or
existential — constraining the Gram/orbit trajectory across time beyond per-slice realizability, or
deciding any candidate of the frozen class?

**What settles it.** The bounded search frozen above, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule if a decision is found — a verbatim
quotation with a coordinate, plus a statement of exactly what it decides and for which families.
Rule 3 if none is found — the recorded statement that the passage sought does not exist on the named
and bounded search, with the per-term record.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `TJ0`**, and no outcome of `TJ0` is a theorem
of this round.

**What `TJ0` is not.** It is not a claim that any statement it fails to find is false, not a claim
that one is unprovable, and not a claim about what a later round could prove. It is a statement about
the merged record at this freeze's base. **Nor is it a licence to treat this round's own theorems as
retro-evidence about it.**

### `TJ1` — the admissible trajectory set, characterized pointwise

**The statement, both directions.** For every finite `V` and `A`, every anchor `a₀ : A` and every
visible family `Γ : ℕ → Matrix V V ℝ`:

- **necessity** — for every lift `U` with `CoherentLift a₀ Γ U` and every time `t`,
  `RealizableGram A (Γ t) (FibreGram a₀ (U t))`;
- **sufficiency** — for every assignment `G : ℕ → V → Matrix V V ℂ` with `RealizableGram A (Γ t) (G t)`
  at every `t`, there is a lift `U` with `CoherentLift a₀ Γ U` and `FibreGram a₀ (U t) = G t` at every
  `t`.

**Hence the Gram trajectories of coherent lifts of `Γ` are exactly the pointwise-realizable
assignments**, and the admissible set is the **product over time** of the per-slice realizable sets.

**What settles it.** A Lean theorem at evidence level 2, consuming act 12's merged `sh1_necessity`
slice by slice for the first direction and act 12's merged `sh1_sufficiency` slice by slice for the
second, together with `CoherentLift`'s own definition — `∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)`,
which carries **no cross-time condition whatever** — and a choice principle to assemble the per-time
dilations into one lift.

**Bounded reading, frozen.**

- **It is the round's null, and it is not a selection principle.** It says what the merged record
  constrains, which is each slice separately, and **it asserts no coupling between slices and denies
  none**. What it establishes is that **every** cross-time constraint on the trajectory is additional
  structure rather than a consequence of coherence — which is the precondition for the trajectory
  question being a real question, and is not an answer to it.
- **It is a statement about Gram trajectories and not about lifts.** Two lifts with one Gram
  trajectory may differ arbitrarily in the threading, which is scope boundary clause 2 above and is
  not touched here.
- **The per-slice constraint it records is `SH1`'s, consumed.** The rank bound `|A|` is act 12's and
  is not re-proved, enlarged or revised. What is this round's own is the statement over **all** times
  at once and the assembly of the lift.
- **A narrowing recorded here is pointwise and is labelled pointwise.** The rank bound excludes
  trajectory values slice by slice; that exclusion is **not** a cross-time coupling, and reporting it
  as one is the defect the hierarchy's line 3 exists to prevent.

### `TJ2` — the per-candidate verdicts

Six parts, predicted and reported separately: `TJ2` (a) `SP1L`, (b) `SP1G`, (c) `SP2`, (d) `SP3`,
(e) `SP5`, (f) `SP4`. Each part carries question (A) and, for the members of `𝒮` and for those only,
question (B).

**The frozen verdict labels, exhaustive per question.**

| label | question | statement | earned only by |
| --- | --- | --- | --- |
| `X-ADD` | (A) | `X` fails for an exhibited coherent lift of an exhibited visible family, so `X` is additional structure | a kernel proof at evidence level 2, objects pinned by equations, coherence discharged from merged results, the violation certified at named times through a named invariant |
| `X-THM` | (A) | `X` holds of every coherent lift of every visible family, so `X` is no addition and constrains nothing | a **universal** kernel proof at evidence level 2 over every finite carrier, every anchor, every visible family and every coherent lift |
| `X-NOSEL` | (B) | `X` does not select at an exhibited configuration, because two `≈_O`-inequivalent coherent lifts of one visible family both satisfy it | a kernel proof at evidence level 2 exhibiting both lifts with `X` as a conjunct for each and the `≈_O`-inequivalence certified at a named time |
| `X-EMPTY` | (B) | `X` does not select at an exhibited configuration, because **no** coherent lift of that visible family satisfies it although the family has coherent lifts | a kernel proof at evidence level 2 of a universal exclusion over the lifts of that family, with the excluded quantity computed, plus an exhibited coherent lift of the same family |
| `X-SEL` | (B) | `X` selects at every configuration: the `≈_O`-classes satisfying it number exactly one | a **universal** kernel proof at evidence level 2 over every configuration; **an unrefuted candidate is not a selecting one** |
| UNDECIDED | either | neither was reached | the recorded statement that neither was reached, with the obstruction named — which candidate, which step, and what would settle it |

**What no `TJ2` verdict establishes.**

- **A verdict on one candidate is not a verdict on another**, except along the frozen chain
  `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2`, where a refutation of a weaker member refutes every stronger one and
  the propagation is reported as propagation.
- **`X-ADD` is not a criticism and `X-THM` is not praise.** They answer whether the candidate is
  additional structure, which is a prerequisite question and not a verdict on its merit.
- **`X-NOSEL` and `X-EMPTY` at one configuration are not statements about every configuration.** Act
  12's `SH1-C2` supplies configurations — the deterministic visible laws — at which the per-slice
  orbit is unique for free, so a failure to select somewhere is not a failure to select everywhere,
  and the result note says so where it reports either label.
- **`SP4`'s verdict is not evidence about any member of `𝒮`**, in either direction, and no line of
  the hierarchy quantifies over `SP4`.

### `TJ3` — THE GRADED SUCCESS HIERARCHY

**The canonical order, stated once:** unique selector → complete classification → proper nontrivial
cross-time constraint → class-level selection impossibility → UNDECIDED with the obstruction named.

**The hierarchy is strict and exhaustive, and the outcome reached is the highest line the kernel
actually carries** — never a higher one. Each line's frozen post-round sentence is written out in the
status rule below.

| # | outcome | statement, with its quantifiers | earned only by |
| --- | --- | --- | --- |
| 1 | **`TJ3-UNIQ`** | see the frozen statement below | a universal kernel proof at evidence level 2 that some named member of `𝒮` selects at every configuration |
| 2 | **`TJ3-CLASS`** | see the frozen statement below | a kernel proof at evidence level 2 of **both** the soundness and the **completeness** direction, with the parameter type and its map written in the statement |
| 3 | **`TJ3-CON`** | see the frozen statement below | a kernel proof at evidence level 2 of a universal property, its properness exhibited in **both** directions, and its **cross-time** character proved |
| 4 | **`TJ3-IMP`** | see the frozen statement below | a kernel proof at evidence level 2 of an `∃ C ∀ S` statement with `C` admissible under this round's own constraints |
| 5 | **UNDECIDED** | none of the above was reached | the recorded statement that none was reached, with the obstruction named specifically — which candidate, which step, what would settle it |

#### Line 1 — `TJ3-UNIQ`, a unique selector, FROZEN STATEMENT

> **There exists a member `S` of the frozen selector class `𝒮` — named explicitly in the statement,
> one of `SP1L`, `SP2`, `SP3`, `SP5` — such that for every finite `V`, every finite `A`, every anchor
> `a₀ : A` and every visible family `Γ : ℕ → Matrix V V ℝ` admitting at least one coherent lift,
> `S` selects at that configuration: there is a coherent lift `U₀` of `Γ` with `S U₀`, and for every
> coherent lift `U` of `Γ` with `S U`, `𝔾(U) ≈_O 𝔾(U₀)` — the quotient being taken over
> `GramTrajEquiv`, this round's frozen cross-time equivalence, and over no other relation.**

#### Line 2 — `TJ3-CLASS`, a complete classification, FROZEN STATEMENT

> **There exist a parameter type `P` and a map `f : P → (ℕ → V → Matrix V V ℂ)` from parameters to
> Gram trajectories, both written explicitly in the statement and both defined from `Γ`, `V`, `A`
> and `a₀` alone, such that, for the visible family `Γ` the statement names: (i) SOUNDNESS — for
> every `p : P` there exists a lift `U` with `CoherentLift a₀ Γ U` and
> `GramTrajEquiv (𝔾 U) (f p)`; and (ii) COMPLETENESS, the surjectivity obligation — for EVERY lift
> `U` with `CoherentLift a₀ Γ U` there EXISTS `p : P` with `GramTrajEquiv (𝔾 U) (f p)`. The quotient
> in (ii) is taken over `GramTrajEquiv`, this round's frozen cross-time equivalence, BY NAME, and
> over no other relation: it is NOT taken over act 12's per-slice `GramPhaseEquiv` at a single time,
> and NOT over act 13's threading relation. Neither `P` nor `f` may be, or contain, the type of
> lifts or the type of Gram trajectories, and `P` is either a `Fintype` — the finite case — or a
> named parameter type — the parametric case.**

**The completeness direction is what separates line 2 from line 3, and it is a mathematical
requirement and not a wording preference.** Exhibiting a parameterized family of admissible
trajectories — however natural or convenient its parameterization — earns **line 3 and not line 2**.
Without (ii) proved, the result is reported at line 3 with the parameterization **recorded as a
finding rather than as the classification**, in those words. **The trivial parameterization is
excluded in terms** by the clause forbidding `P` or `f` to be or contain the lift or trajectory
types: taking `P` to be the admissible trajectories and `f` the identity satisfies both directions
and classifies nothing.

#### Line 3 — `TJ3-CON`, a proper nontrivial cross-time constraint, FROZEN STATEMENT

> **There is a property `Q` of Gram trajectories, stated over the licensed data `L` only, such that:
> (i) UNIVERSALITY — for every finite carrier, every anchor, every visible family `Γ` and every lift
> `U` with `CoherentLift a₀ Γ U`, `Q` holds of `𝔾(U)`; (ii) PROPERNESS, exhibited in BOTH directions
> — a named visible family `Γ`, a named Gram trajectory that is pointwise realizable for `Γ` and
> FAILS `Q`, and a named coherent lift of `Γ` whose trajectory SATISFIES `Q`, all three proved, so
> that the narrowing is shown to be neither empty nor everything; and (iii) CROSS-TIME CHARACTER —
> `Q` is not equivalent, over pointwise-realizable trajectories, to any pointwise condition of the
> form `∀ t, q (G t)`, and the inequivalence is proved by an exhibited trajectory that satisfies the
> pointwise condition and fails `Q`.**

**Clause (iii) is what stops line 3 being earned by restating `SH1`.** A narrowing that is a
per-slice constraint lifted pointwise to trajectories — which is what `TJ1`'s rank bound is — does
**not** earn line 3; it is recorded under `TJ1` and labelled pointwise. Whether clause (iii) should
be required at all is one of the owner decisions recorded below.

#### Line 4 — `TJ3-IMP`, class-level selection impossibility, FROZEN STATEMENT

> **THERE EXISTS a configuration `C` — a finite `V`, a finite `A`, an anchor `a₀ : A` and a visible
> family `Γ : ℕ → Matrix V V ℝ` — such that `C` is ADMISSIBLE under exactly the frozen constraints
> this round uses everywhere else, namely that there is at least one lift `U₀` with
> `CoherentLift a₀ Γ U₀`, AND such that FOR EVERY selector `S` in the frozen selector class
> `𝒮 = {SP1L, SP2, SP3, SP5}`, `S` FAILS TO SELECT at `C`: the set of `GramTrajEquiv`-classes of the
> trajectories of coherent lifts of `Γ` satisfying `S` does NOT have exactly one element — either it
> is empty, or it contains two `GramTrajEquiv`-inequivalent members — and the statement records
> which of the two holds for each of the four members of `𝒮` separately.**

**The quantifier order is `∃ C ∀ S`, and it is load-bearing.** The countermodel is chosen **first**
and defeats **all four** selectors. **The reversed order `∀ S ∃ C` — for every selector some
configuration defeats it — is a strictly weaker statement and is NOT line 4**: it is exactly the
conjunction of the four per-candidate `X-NOSEL` and `X-EMPTY` verdicts, it is reported under `TJ2`
where those verdicts live, and reporting it as line 4 is a defect this paragraph exists to prevent.

**`C` must be admissible under the round's own constraints**, and the statement carries the
existence of a coherent lift of `Γ` as a conjunct for exactly that reason: an impossibility bought by
stepping outside the admissible class proves nothing about selection within it.

**What line 4 does NOT establish.** It is impossibility **within the frozen class of four named
principles at one exhibited configuration**. It is **not** impossibility over all conceivable
selection principles, **not** a statement that no selection principle exists, **not** a statement
that selection fails at every configuration — act 12's `SH1-C2` supplies configurations where the
per-slice orbit is unique for free — and **not** a bound on what a later round could name or prove.

#### The adjunct rule, and what may not be done with the hierarchy

**If a higher line and line 4 are both earned, the outcome is the higher line and line 4's verdict is
reported alongside it with its own frozen sentence.** A class-level impossibility theorem is not
information the ladder may discard, and the ladder orders the **outcome**, not the **record**.

**What `TJ3` may not do.**

- It may not report an outcome at a strength the kernel does not carry.
- It may not report line 2 on the strength of a parameterized family without the completeness
  direction. **That is line 3**, and the gap between them is the surjectivity obligation.
- It may not report line 3 on the strength of a pointwise narrowing. **That is a `TJ1` finding.**
- It may not report line 4 on the strength of `∀ S ∃ C`. **That is a `TJ2` finding.**
- It may not report any line on the strength of a witness sought and not found. **Absence of a
  witness is line 5**, with the obstruction named.
- It may not report line 1 or line 2 on the strength of a candidate merely surviving the round's
  tests. **An unrefuted candidate is not a selecting one.**

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `TJ0` | **negative** — the record is silent; no statement constrains the trajectory across time or decides any candidate | **high** | A pre-freeze survey of the file set named in the evidence rule found every merged statement about the Gram data to be per-slice — `SH1` and `SH1-C2` about one dilation, `TG2` about one slice, `TG3` about two slices and their lifted pair — and act 13's cross-time statements to be about the column-Gram family and the threading, not about the orbit trajectory. The survey is the freeze's **reason**, not a finding: `TJ0`'s finding is whatever the execution's own bounded search records. |
| `TJ1` necessity | positive | **high** | Act 12's merged `sh1_necessity` applied at each `t`, with no assembly required. |
| `TJ1` sufficiency | positive | **high** | Act 12's merged `sh1_sufficiency` is stated per slice with no hypothesis on `Γ` beyond realizability, and `CoherentLift` is definitionally `∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)` with no cross-time conjunct, so the assembly is a `choose` over `t`. |
| `TJ2` (a) `SP1L` (A) | **`SP1L-ADD`** | **high** | Act 12's merged `hadamard_lifts_not_twoSided` exhibits a coherent lift of a constant visible family, and `hadamard_slices_not_twoSided` proves its two slices `∼_D`-inequivalent. |
| `TJ2` (a) `SP1L` (B) | **`SP1L-NOSEL`** | **high** | The two constant lifts are coherent by the same merged admissibility conjuncts, both satisfy `SP1L` because a constant lift has a constant trajectory, and their inequivalence is the same merged conjunct. |
| `TJ2` (b) `SP1G` (A) | **`SP1G-ADD`** | **high** | The same pair, read across lifts at one time. Rated **at or below** `SP1L`'s (A) rating, never above it, because `SP1G` is strictly the stronger proposition and any route refuting the weaker refutes it. |
| `TJ2` (c) `SP2` (A) | **`SP2-ADD`** | **high** | The same lifted pair. `SP2` is the weakest member of the frozen chain; its refutation is the one the other three inherit, and this row is rated **at or above** every other (A) row for that reason. |
| `TJ2` (c) `SP2` (B) | **`SP2-NOSEL`** | **high** | The two constant lifts are stationary by construction and inequivalent. |
| `TJ2` (d) `SP3` (A) | **`SP3-ADD`** | **medium** | The four-slice lift `H(1), H(i), H(1), H(1)` needs each slice's admissibility — merged, from `hadamard_slices_not_twoSided` — and one inequivalence, also merged; the medium rating is for the bookkeeping of a piecewise lift over `ℕ` and the case split at `t = 0, 1, 2`, not for doubt about the route. **Reporting `SP3` (A) UNDECIDED with the obstruction named is an allowed outcome.** |
| `TJ2` (d) `SP3` (B) | **`SP3-NOSEL`** | **high** | Both constant lifts satisfy `SP3` because a constant trajectory satisfies the implication vacuously, and they are inequivalent. |
| `TJ2` (e) `SP5` (A) | **`SP5-ADD`** | **high** | At `\|A\| = 1` the tuple is `G^{(i)}_{jk} = conj(H_{ij}) H_{ik}` by `fibreGram_apply`, and every entry of `H(1)` is nonzero, so an off-diagonal entry is nonzero. Rated **at or below** `SP1G`'s (A) rating, `SP5` being strictly the stronger of the chain. |
| `TJ2` (e) `SP5` (B) | **`SP5-EMPTY`** | **medium** | The diagonal tuple for `Γ ≡ ¼` on `\|V\| = 4` is `(1/4)·I₄` in each fibre, which is invertible and therefore of rank `4`, while `fibreGram_rank_le` bounds the rank by `\|A\| = 1`. The medium rating is for the rank computation in the kernel, not for the argument. **UNDECIDED with the obstruction named is an allowed outcome and does not move (A).** |
| `TJ2` (f) `SP4` | **`SP4-THM`, and vacuous** | **high** | `fibreCrossGram_diag` is `rfl`: the level-2 datum contains the Gram trajectory at its diagonal, so equality of the former gives equality of the latter and hence `≈_O` with the trivial phase family. |
| `TJ3` | **line 4, `TJ3-IMP`** | **medium** | Conditional on `TJ2` (a)–(e) landing as predicted, in which case the single configuration `Γ ≡ ¼` on `\|V\| = 4`, `\|A\| = 1` defeats all four members of `𝒮` at once — `SP1L`, `SP2` and `SP3` by two surviving inequivalent trajectories, `SP5` by exclusion of every trajectory — which is the `∃ C ∀ S` shape. The medium rating is for `SP5` (B)'s rank computation, on which the fourth conjunct depends; if it is UNDECIDED, so is line 4, and `TJ3` falls to line 5. |
| `TJ3` → line 1, `TJ3-UNIQ` | not predicted | **low** | Its only routes are through the members of `𝒮`, every one of which the freeze predicts refuted at (A) or defeated at (B) by one merged witness family. The freeze names no further route and rates none better than low. |
| `TJ3` → line 2, `TJ3-CLASS` | not predicted | **low** | The completeness direction would need a surjectivity proof over the trajectory space of an arbitrary finite carrier. `TJ1` characterizes that space as a product of per-slice realizable sets, which is a description and not a parameterization by a type independent of the trajectories; the freeze names no parameterization and does not fund building one. |
| `TJ3` → line 3, `TJ3-CON` | not predicted | **low** | Clause (iii) requires a cross-time property, and the freeze's whole expectation from `TJ1` is that the merged record supplies none. Rated **at or above** line 2's strength, because a complete classification with clause (iii)'s cross-time content would also exhibit a cross-time constraint, while the converse fails. |
| `TJ3` → line 5, UNDECIDED | not predicted | **medium** | Reached if `SP5` (B) or `SP3` (A) does not land, since line 4's `∀ S` conjunct needs all four. Rated below line 4 and above lines 1, 2 and 3. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

**The rows rating lines 1, 2 and 3 at low are the freeze's whole position on whether anything
selects.** No sentence of this file predicts, at medium or high, that any candidate selects, that the
admissible set is classified, or that a cross-time constraint exists.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached. The
wording is fixed before the round runs so that no outcome can choose its own wording. **UNDECIDED is
a live preregistered outcome for every target and is not a failure**; where it is reached the frozen
sentence below is the report, with the obstruction named.

### The outcomes of `TJ0`

- **Outcome `TJ0`-silent** — the bounded search records that the passage sought does not exist:
  > On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
  > `verification/lean/`, every `preregistration.md` and `result.md` under
  > `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
  > the merged record contains no statement constraining the Gram/orbit trajectory across time
  > beyond the per-slice realizability of `SH1`, and decides no candidate of the frozen class in
  > either direction. **The finding is that the record is silent on the point.** It is not a finding
  > that any such statement is false, not a finding that one is unprovable, and not a bound on what a
  > later round could prove.
- **Outcome `TJ0`-found** — the search locates a deciding statement:
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which visible
  > families. Whether that statement settles the trajectory question is `TJ3`'s question and is not
  > settled by locating it. No merged artifact is edited, and no earlier round's recording is
  > enlarged or corrected.

### The outcomes of `TJ1`

- **Outcome `TJ1`-both-directions:**
  > The Gram trajectories of the coherent lifts of a visible family are exactly the pointwise
  > realizable assignments, at evidence level 2, through act 12's merged `SH1` consumed in both
  > directions slice by slice. **The admissible trajectory set is the product over time of the
  > per-slice realizable sets, and the merged record therefore imposes no coupling between slices.**
  > This is a statement about what is constrained and **not** a selection principle: it asserts no
  > coupling and denies none, and it establishes that **every** cross-time constraint on the
  > trajectory is additional structure rather than a consequence of coherence. The per-slice
  > constraint it records is act 12's `SH1`, consumed at its own strength and neither enlarged nor
  > revised, and the narrowing the rank bound `|A|` effects is **pointwise** and is labelled
  > pointwise.
- **Outcome `TJ1`-necessity-only:**
  > The necessity direction holds at evidence level 2: every coherent lift's Gram trajectory is
  > pointwise realizable. The sufficiency direction — that every pointwise realizable assignment is
  > some coherent lift's trajectory — was not reached, with the obstruction named, so the admissible
  > set is bounded above and not characterized, and no statement of this round says the trajectory is
  > unconstrained across time.
- **Outcome `TJ1`-UNDECIDED:**
  > Neither direction was reached in the kernel, with the obstruction named, and every later target
  > stated over the characterization is reported UNDECIDED with this recorded as the obstruction. Act
  > 12's `SH1` stands as act 12 states it and nothing is claimed from it here.

### The outcomes of `TJ2`, per candidate and per question

- **Outcome `X-ADD`**, for a named candidate `X`:
  > The candidate named `X` in this round's frozen list **fails for an exhibited coherent lift of an
  > exhibited visible family**, at evidence level 2, with the violating times named and the
  > inequivalence of the orbit classes certified through a named `∼_D`-invariant. **So `X` is
  > additional structure and not a consequence of coherence.** This is a verdict on the exact
  > proposition frozen under the label `X`, on the data grant frozen for it, and on nothing in its
  > neighbourhood; no other memorylessness, stationarity, determination or decoherence condition is
  > refuted, named or excluded by it. The merged witnesses it consumes are consumed at their own
  > strengths and none is enlarged.
- **Outcome `X-THM`**, for a named candidate `X`:
  > The candidate named `X` holds of **every** coherent lift of every visible family over every
  > finite carrier, at evidence level 2. **So `X` is not additional structure and constrains
  > nothing**: it selects no trajectory, because it excludes none. This is a statement about `X` as
  > this freeze states it, on its frozen data grant, and it endorses no principle and requires none.
- **Outcome `X-NOSEL`**, for a named candidate `X` in `𝒮`:
  > At the exhibited configuration, two coherent lifts of one visible family both satisfy `X` and
  > their trajectories are **inequivalent under `GramTrajEquiv`**, this round's frozen cross-time
  > equivalence, at a named time and through a named invariant, at evidence level 2. **So `X` does
  > not select there.** This settles **one configuration**: it is not a statement that `X` fails to
  > select at every configuration, and act 12's `SH1-C2` supplies configurations — the deterministic
  > visible laws — where the per-slice orbit is unique for free. It is **not** a statement that no
  > principle selects, which is line 4's question and is settled there.
- **Outcome `X-EMPTY`**, for a named candidate `X` in `𝒮`:
  > At the exhibited configuration **no** coherent lift of the named visible family satisfies `X`,
  > proved universally over the lifts of that family at evidence level 2, with the excluded quantity
  > computed — while the family **does** have coherent lifts, exhibited. **So `X` does not select
  > there, by excluding every trajectory rather than by leaving several.** The two mechanisms are
  > kept apart: this is not the outcome in which several trajectories survive. It settles one
  > configuration and is not a statement about every configuration.
- **Outcome `X-SEL`**, for a named candidate `X` in `𝒮`:
  > The candidate named `X` selects at **every** configuration, at evidence level 2: for every finite
  > carrier, anchor and visible family with a coherent lift, the trajectories of the coherent lifts
  > satisfying `X` form exactly one class under `GramTrajEquiv`. **This is a statement about `X` as
  > this freeze states it and on its frozen data grant.** It does **not** endorse `X`, does not say a
  > selector is required, and adopts no carrier and no principle; and it says nothing about any other
  > candidate, named or unnamed.
- **Outcome `X`-UNDECIDED**, for a named candidate `X` and a named question:
  > The question asked of `X` is undecided in this round, with the obstruction named specifically —
  > the candidate, the step at which the proof stopped, and what would settle it. Neither label is
  > claimed, and no sentence of this round treats the absence of a decision as a decision. In
  > particular the absence of a refutation is **not** reported as the candidate holding, and the
  > absence of a witness is **not** reported as there being none.

### The outcomes of `TJ3` — five lines, each with its sentence frozen in full

- **Outcome line 1, `TJ3-UNIQ`:**
  > A member of the frozen selector class selects: for every configuration, the trajectories of the
  > coherent lifts satisfying the named principle form exactly one class under `GramTrajEquiv`, at
  > evidence level 2. **This is a statement about the four named principles of this round's frozen
  > class, on their frozen data grants, and about nothing else.** It does **not** say that the
  > principle is true of nature, does not adopt it, does not say a selector is required, and does not
  > close `P0`: what it establishes is that one preregistered rule, if imposed, leaves one trajectory.
  > `P0` stays **OPEN** and two-part, its threading part is untouched, and no carrier is adopted as
  > the physical one.
- **Outcome line 2, `TJ3-CLASS`:**
  > The admissible trajectory set at the named visible family is **completely classified**: a
  > parameter type and a map from it to Gram trajectories are exhibited, every parameter's trajectory
  > is realized by a coherent lift, and **every** coherent lift's trajectory is equivalent to some
  > parameter's under `GramTrajEquiv` — the surjectivity obligation, proved, and the quotient taken
  > over this round's frozen cross-time equivalence by name and over no other relation. At evidence
  > level 2. **This is a classification of trajectories and not of lifts**: the threading is
  > invisible to the relation and is not classified, bounded or touched. `P0` stays **OPEN** and
  > two-part, and nothing here names, endorses or excludes a selection principle.
- **Outcome line 3, `TJ3-CON`:**
  > A **proper cross-time constraint** on the admissible trajectory class is exhibited: a property of
  > Gram trajectories stated over the licensed data alone, holding of every coherent lift's
  > trajectory, with a named pointwise-realizable trajectory that fails it and a named coherent lift
  > whose trajectory satisfies it, and with its cross-time character proved by an exhibited
  > trajectory satisfying the corresponding pointwise condition and failing the property. At evidence
  > level 2. **This is a narrowing and not a classification**: no parameterization is claimed, and in
  > particular no completeness direction is proved, so nothing here says the surviving trajectories
  > are enumerated or parameterized. **It is not a selection**: the survivors are not claimed unique.
  > `P0` stays **OPEN** and two-part.
- **Outcome line 4, `TJ3-IMP`:**
  > **Selection impossibility at the class level is exhibited.** There is a configuration —
  > admissible under exactly this round's own constraints, the visible family having at least one
  > coherent lift, exhibited — at which **every** member of the frozen selector class
  > `𝒮 = {SP1L, SP2, SP3, SP5}` fails to select, each for a recorded reason: either two
  > `GramTrajEquiv`-inequivalent trajectories survive it, or it excludes every trajectory. At
  > evidence level 2, with the quantifiers in the order `∃ C ∀ S` and the configuration chosen first.
  > **This is impossibility within a frozen class of four named principles at one exhibited
  > configuration.** It is **not** impossibility over all conceivable selection principles, **not** a
  > statement that no selection principle exists, **not** a statement that selection fails at every
  > configuration — act 12's `SH1-C2` supplies configurations where the per-slice orbit is unique for
  > free — and **not** a bound on what a later round could name or prove. It was earned by an
  > exhibited countermodel and never by a search. `P0` stays **OPEN** and two-part, its threading
  > part is untouched, and nothing here names, endorses or excludes a selection principle beyond
  > refuting the four exact propositions this freeze states.
- **Outcome line 5, `TJ3`-UNDECIDED — its post-round sentence frozen in full:**
  > **The question of what selects or constrains the cross-time Gram/orbit trajectory is recorded
  > UNDECIDED.** None of the four settling outcomes was reached in this round, and **none is
  > claimed**: no member of the frozen class is shown to select, no classification is proved, no
  > proper cross-time constraint is exhibited, and no class-level countermodel is exhibited. The
  > obstruction is named specifically — the candidate, the step and what would settle it. **What this
  > round adds is the bounding and, where they landed, the per-candidate verdicts and the pointwise
  > characterization, and not a resolution.** **An UNDECIDED is a statement about this round and
  > about the record, and not about the question.** It is **not** a finding that the question is
  > unresolvable, **not** a finding that it is hard, **not** a bound on what a later round can do,
  > and **not** a finding against any settled result of acts 11 through 16: `GL2`, `GL3`, `GI2`,
  > `LG1`, `RO1`, `TG2`, `TG3`, `SH1` with `SH1-C1` and `SH1-C2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`,
  > `PQ0`–`PQ4`, act 15's `PQ3-d⁺` and act 16's `RN3⁺` stand exactly as those rounds state them. **No
  > carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and nothing here names,
  > endorses or excludes a selection principle.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The sentence the execution
appends to it is fixed here.

**Case A — `TJ0` silent, `TJ1` lands in both directions, `TJ2` (a)–(f) land as predicted, and `TJ3`
reaches line 4.** This is the case the freeze predicts.

> `P0` remains open and two-part, and the answers of acts 11 through 16 stand exactly as those rounds
> state them. The part act 16 left standing — what selects or constrains the Gram/orbit trajectory
> across time — is now bounded rather than resolved. Relative to the round's frozen cross-time
> equivalence, under which two lifts have the same trajectory when their per-slice fibre-Gram tuples
> agree modulo the anchored phases at every time and which therefore identifies every pair act 13
> localized as threading-related, the admissible Gram trajectories of a visible family are exactly
> the pointwise realizable assignments: the merged record constrains each slice by act 12's `SH1` and
> imposes no coupling between slices, so every cross-time constraint on the trajectory is additional
> structure rather than a consequence of coherence. Against that baseline four named candidate
> principles were frozen before the search and tested — a per-lift law-determination constraint,
> orbit stationarity under a constant visible law, a homogeneous transition rule, and the decoherence
> rule that the orbit is the diagonal tuple — together with the cross-lift law-determination claim
> and one deliberate out-of-regime probe, and on that class the outcome is class-level selection
> impossibility: there is one visible family, admitting coherent lifts, at which every member of the
> frozen class fails to select, three by leaving two inequivalent trajectories and the decoherence
> rule by excluding every trajectory through act 12's rank bound. That is impossibility within a
> frozen class of four named principles at one exhibited configuration, earned by an exhibited
> countermodel and never by a search; it is not impossibility over all conceivable selection
> principles, and act 12's `SH1-C2` supplies deterministic visible laws where the per-slice orbit is
> unique for free. Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are carrier-specific cancellation verdicts
> about the threading pair and are not evidence that the trajectory freedom is redundancy; nothing
> here treats them as such. `P0`'s threading part is untouched, **no carrier is adopted as the
> physical one**, and nothing here names, endorses or excludes a selection principle beyond refuting
> the exact propositions this round froze.

**Three clauses of Case A vary with the outcome, and they vary independently.** Naming them here,
and fixing each clause's substitutions against the target that governs it, is what lets the execution
compose the sentence it actually earned rather than carry a clause that reads against its own
outcome.

- **The baseline clause**, governed by `TJ1`, is Case A's
  > "the admissible Gram trajectories of a visible family are exactly the pointwise realizable
  > assignments: the merged record constrains each slice by act 12's `SH1` and imposes no coupling
  > between slices, so every cross-time constraint on the trajectory is additional structure rather
  > than a consequence of coherence"
- **The verdict clause**, governed by `TJ3`, is Case A's sentence beginning "Against that baseline"
  from the words "and on that class the outcome is" to the end of that sentence.
- **The bound clause**, governed by `TJ3`, is Case A's sentence beginning "That is impossibility
  within a frozen class".

**The verdict clause and the bound clause, per `TJ3` outcome.**

| `TJ3` | verdict clause | bound clause |
| --- | --- | --- |
| line 4, `TJ3-IMP` (**Case A**) | as written above | as written above |
| line 1, `TJ3-UNIQ` (**Case B**) | "and on that class one named principle selects: at every configuration the trajectories of the coherent lifts satisfying it form exactly one class under the round's cross-time equivalence" | "That is a statement about one preregistered rule and what imposing it leaves, earned universally in the kernel; it does not adopt the rule, does not say a selector is required, and does not close `P0` or either of its parts." |
| line 2, `TJ3-CLASS` (**Case C**) | "and on the named visible family the admissible trajectory set is completely classified, the completeness direction proved so that every coherent lift's trajectory is equivalent to a parameter's under the round's cross-time equivalence" | "That is a classification of trajectories and not of lifts, the threading being invisible to the relation; it selects nothing and endorses no principle." |
| line 3, `TJ3-CON` (**Case D**) | "and a proper cross-time constraint on the admissible trajectory class is exhibited, with a pointwise realizable trajectory that fails it, a coherent lift whose trajectory satisfies it, and its cross-time character proved" | "That is a narrowing and not a classification and not a selection: no parameterization is claimed, no completeness direction is proved, and the survivors are not claimed unique." |
| line 5, UNDECIDED (**Case E**) | "and on that class the outcome is recorded UNDECIDED: no member is shown to select, no classification is proved, no proper cross-time constraint is exhibited, and no class-level countermodel is exhibited, with the obstruction named" | "That is a statement about this round and about the record and not about the question: it is not a finding that the question is unresolvable, not a finding that it is hard, and not a bound on what a later round can do." |

**Case F — `TJ1` reaches necessity only, or is UNDECIDED:** the baseline clause is replaced by "the
admissible Gram trajectories of a visible family are pointwise realizable, the converse being
undecided in this round with the obstruction named, so the admissible set is bounded above and not
characterized"; every other clause stands at whatever the other targets reach, and **no sentence
says the trajectory is unconstrained across time**.

**Case G — one or more `TJ2` parts UNDECIDED while `TJ3` reaches line 4:** unreachable by
construction, since line 4's `∀ S` conjunct needs all four members settled; if any is UNDECIDED,
`TJ3` falls to line 5 and Case E governs, with the undecided candidate named in the obstruction.

**The execution composes the sentence from these substitutions and reports no other wording.** **No
composition closes `P0`**, and none reports either of its two parts closed.

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The trajectory freedom is gauge", or "the trajectory freedom is physical."** Act 14's status
   rule that there is no carrier-free verdict binds this round too, and this round adopts no carrier
   and defines no carrier of its own. Nothing here says the residual trajectory freedom is
   redundancy and nothing here says it is not.
2. **Any sentence that treats act 16's `RN3⁺` or act 15's `PQ3-d⁺` as evidence about the trajectory
   freedom.** The anti-conflation clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
   > that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
   > re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
   > time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
   > statement about the threading pair on a named carrier, and it is not a statement about the
   > cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
   > those two carriers **does not license the assumption that all residual trajectory freedom is
   > gauge**: act 16 established a cancellation on named carriers and established **nothing** about
   > whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's
   > status rule that there is no carrier-free verdict binds this round too. **No outcome of this
   > round may treat act 16's positive, or act 15's, as evidence that the trajectory freedom is
   > gauge or that it is physical; no target of this round consumes either for that purpose; and no
   > candidate selection principle is named, rated, predicted, admitted or refuted on their
   > strength.**
3. **"No selection principle exists", or "nothing can select the trajectory."** Line 4 is
   impossibility within a frozen class of four named principles at one exhibited configuration. It
   quantifies over `𝒮` and over nothing else.
4. **"Selection fails everywhere."** Act 12's `SH1-C2` proves the per-slice orbit unique on
   deterministic visible laws, so the trajectory there is determined by the law for free. Every
   non-selection verdict of this round names its configuration.
5. **"The candidate class is exhaustive", or "these are the selection principles."** The class is
   four named propositions frozen for testing. A candidate outside it is neither refuted nor endorsed
   by anything here, and a candidate discovered during execution is recorded as an observation and
   not executed.
6. **"A selector is required", or "`P0` needs additional structure of shape X."** `TJ1` says every
   cross-time constraint is additional structure; it does not say one is needed, and the round names,
   endorses and excludes no selection principle beyond refuting the exact propositions it froze.
7. **"The trajectory is unconstrained", asserted on the strength of a necessity-only `TJ1`.** Without
   the sufficiency direction the admissible set is bounded above and not characterized.
8. **"The narrowing is cross-time", asserted of a pointwise constraint.** `TJ1`'s rank bound narrows
   slice by slice. **A pointwise constraint lifted to trajectories is not a coupling between times**,
   and line 3's clause (iii) is what separates the two.
9. **"The admissible set is classified", asserted on the strength of a parameterized family.**
   Without the completeness direction proved — for **every** admissible trajectory, **some**
   parameter, modulo `GramTrajEquiv` — the result is line 3 and the parameterization is a finding.
10. **"No selector selects", asserted on the strength of `∀ S ∃ C`.** The reversed quantifier order
    is a conjunction of per-candidate negatives. **Line 4 is `∃ C ∀ S`, and the difference is the
    whole content of the line.**
11. **"A witness was sought and not found, so there is none."** Absence of a witness in this round is
    not a negative result, no search is presented as exhaustive, and the outcome of a failed search
    is line 5 with the obstruction named.
12. **Any statement about the threading, the cross-time representative, the relative evolution or
    the relative candidate.** These are invisible to this round's equivalence relation by
    construction. **A round that cannot see a distinction may not report one**, in either direction.
13. **Any statement about act 14's four carriers**, or any adoption of a carrier, or any assertion
    that a carrier is not the physical one. This round defines no carrier and reads none.
14. **"`P0` is closed", or "`P0`'s trajectory part is closed."** The row stays OPEN and two-part in
    every case, and `P0`'s threading part is untouched by this round.
15. **"Act 12's `SH1` is enlarged", or "`TG3` is a universal statement."** `SH1` is consumed in both
    directions at its own strength and `TG3` is existential, about its own exhibited dilations. **A
    merged existential is not enlarged to a universal by being consumed.**
16. **"Act 13 is revised", or "`CT2` (b) is weakened."** Act 13's statements are about the column
    cross-Gram family and the threading; this round consumes `ct3g_fibreGram_strong_right` and
    `fibreCrossGram_diag` and revises nothing.
17. **"OI and QM are inequivalent."** Two lifts differing is not two theories differing, and the
    established finite observable-law correspondence is untouched. Every visibility statement here is
    further a statement under act 7's own readback convention, with `D4b` negative.
18. **"The trajectory is continuous", "smooth", "generated by a Hamiltonian", or any statement
    resting on structure the index type does not carry.** `CoherentLift` is `ℕ`-indexed and this
    round does not change that; act 5's smooth construction is a separate merged countercontrol on
    the continuous side and is not consumed here.
19. **Any sentence about Track I**, or about Source B or Source C, on any axis.
20. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **Letting act 16's positive carry into the trajectory question.** **This is the strongest hazard
   in the round**, because act 16 has just landed a positive about a pair of exactly the two group
   actions whose residual this round quotients away, and because "cancellation exists, therefore the
   freedom is gauge" is a short and plausible-sounding step that nothing licenses. The anti-conflation
   clause is carried verbatim at every mention:
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
   > that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
   > re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
   > time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
   > statement about the threading pair on a named carrier, and it is not a statement about the
   > cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
   > those two carriers **does not license the assumption that all residual trajectory freedom is
   > gauge**: act 16 established a cancellation on named carriers and established **nothing** about
   > whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's
   > status rule that there is no carrier-free verdict binds this round too. **No outcome of this
   > round may treat act 16's positive, or act 15's, as evidence that the trajectory freedom is
   > gauge or that it is physical; no target of this round consumes either for that purpose; and no
   > candidate selection principle is named, rated, predicted, admitted or refuted on their
   > strength.**
2. **A candidate reading data the round has not licensed.** The specific failure guarded against is a
   principle that "selects" because it was handed an object that already determines the trajectory.
   The data regime fixes the licensed set `L` and the forbidden set `F` in advance, the per-candidate
   grants are tabulated, and `SP4` is executed **outside the class** precisely so that the effect of
   crossing the line is on the record as a theorem rather than as a warning.
3. **Answering the question in the equivalence relation.** The specific failure guarded against is
   adopting the uniform-phase relation, which couples the slices, and then reporting the coupling as
   a finding. The freeze adopts the per-slice relation applied pointwise and records the uniform-phase
   relation as a distinct relation it does not adopt.
4. **Seeing the threading.** The specific failure guarded against is a statement of this round
   distinguishing two lifts that `≈_O` identifies — for instance reporting that act 11's `GL2` pair
   has two trajectories. It has one, for this round, and the round says nothing about the difference.
5. **Reading raw Gram equality as the round's relation.** Raw equality is strictly finer and is a
   representative-level equality, as act 13 records. The specific failure guarded against is a proof
   that establishes raw equality and a statement that reports it as trajectory equality, or the
   reverse.
6. **Reporting line 2 on a parameterized family without completeness.** The gap is the surjectivity
   obligation: **for every** admissible trajectory, **some** parameter, modulo `GramTrajEquiv`. Line 3
   and its frozen sentence exist to make the weaker report the natural one.
7. **A trivial parameterization at line 2.** The specific failure guarded against is taking the
   parameter type to be the trajectories themselves, or the lifts, with the identity map, which
   satisfies both directions and classifies nothing. Line 2's statement forbids `P` and `f` to be or
   contain either type.
8. **Reporting line 3 on a pointwise narrowing.** `TJ1`'s rank bound excludes trajectory values slice
   by slice and is not a coupling. Clause (iii) of line 3 is the discriminator and is proved, not
   asserted.
9. **Reversing line 4's quantifiers.** `∀ S ∃ C` is the conjunction of the per-candidate negatives
   and belongs to `TJ2`. **Line 4 is `∃ C ∀ S`**, and the specific failure guarded against is a
   result note that collects four per-candidate countermodels and calls the collection an
   impossibility theorem.
10. **A line-4 countermodel outside the admissible class.** The specific failure guarded against is a
    configuration whose visible family has no coherent lift, at which every principle fails to select
    vacuously. The statement carries the existence of a coherent lift as a conjunct.
11. **Enlarging line 4 to all selection principles.** The specific failure guarded against is a
    sentence of the form "so nothing can select the trajectory". The class has four members and is
    frozen.
12. **Treating an unrefuted candidate as a selecting one.** The specific failure guarded against is
    reporting `X-SEL` because no counterexample was found. `X-SEL` needs a universal proof; a failed
    search is UNDECIDED.
13. **Enlarging the round mid-execution because something stronger was found.** The specific failure
    guarded against is an execution that sets out under a constraints-only ask, proves a uniqueness or
    classification theorem, and then reports the round as having asked for it all along. **The scope
    is fixed by this freeze before the search**: lines 1 and 2 are preregistered as reachable with
    their own frozen sentences and their own evidence bars, and anything not preregistered is recorded
    as an observation and not executed.
14. **Naming a candidate and thereby endorsing it.** The specific failure guarded against is a
    sentence reading as a proposal — "the natural principle here is …". Naming is for testing, the
    round endorses none, and every refutation is of the exact frozen proposition and of nothing in
    its neighbourhood.
15. **Refuting a neighbourhood instead of a proposition.** The specific failure guarded against is
    reporting `SP3`'s refutation as a refutation of memorylessness, or `SP5`'s as a refutation of
    decoherence in general. Each verdict names the frozen proposition and its data grant.
16. **Consuming `TG3` or `SH1-C2` at more than their strength.** `TG3` is existential about its own
    exhibited dilations; `SH1-C2` is an at-most-one statement about deterministic slices. The
    specific failure guarded against is citing either as though it quantified over visible families
    or over lifts.
17. **A reader supplying a missing theorem from background knowledge the record does not contain.**
    The specific failure guarded against is a step of the form "of course the hidden datum must
    evolve continuously" or "of course a Gram trajectory is determined by its initial value" —
    plausible-sounding, absent from the record, and licensed by nothing in it. Every step of every
    proof in this round is discharged from a merged result cited by name or from an argument written
    out in the kernel.
18. **Forgetting the anchor, and forgetting the rank bound.** `FibreGram a₀` and `RealizableGram`
    both carry data that a trajectory statement can silently drop: the anchor, and the `|A|` rank
    bound that makes `SH1` sufficiency true. The specific failures guarded against are a statement
    that silently changes which configuration is anchored — which act 7's `R-3` explicitly does
    **not** license — and a use of `SH1` sufficiency without its rank hypothesis.
19. **Importing time structure the index type does not have.** `ℕ` carries successor and order and
    nothing else. The specific failure guarded against is a candidate, a proof or a sentence resting
    on continuity, differentiability or a limit.
20. **Touching `P0`'s threading part.** What determines the cross-time representative within the
    selected orbits is not this round's subject. The specific failure guarded against is a sentence
    of this round bearing on it in either direction.
21. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs; the specific failure guarded against is an execution that
    reads a lane that merged between this freeze and its base.
22. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier in a different programme. Nothing is consumed or compared, and a shared word is not a
    bridge.
23. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_TRJ_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
24. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
25. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: adopt a carrier as the physical one or define a carrier of its own; endorse any
selection principle; assert or deny that a selector, a connection or a gauge fixing is required or
suffices; **ask the threading question or the cross-time representative question, in either
direction**; state anything about the relative object, the relative candidate, the anchored channel
or the re-anchored channel; revise `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
`SH1`, `SH1-C1`, `SH1-C2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(d),
`PQ4`, `CF0`–`CF5`, `RN0`–`RN4` or any merged label; answer act 13's fork `CT3` (d) or move it in
either direction; weaken, qualify or revise act 15's `PQ3-d⁺` or act 16's `RN3⁺`, or read either as
bearing on trajectory freedom; test a candidate outside the frozen class; adopt the uniform-phase or
the raw-Gram relation; change `CoherentLift`'s `ℕ`-indexing or introduce continuity, smoothness,
regularity, homogeneity of the carrier, a generated evolution as a condition of the round, a
measurement model or a source-level coherence condition; introduce a further carrier or revise any of
act 14's four; report a parameterization as a classification, or a pointwise narrowing as a
cross-time constraint, or `∀ S ∃ C` as `∃ C ∀ S`; change `D3`, `D4b`, `D5`, the direct-branch
statement or the readback convention; alter any existing archive seal constant; consume or compare
anything from the substratum Lemma 24.1 rounds; compare Source A with B or C; edit any manuscript;
close `P0` or either of its parts; or say anything about Track I.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most four** top-level Lean definitions, and these are the four:

1. **`GramTrajEquiv`** — the round's frozen cross-time equivalence on Gram trajectories,
   `GramTrajEquiv 𝔾 𝔾' := ∀ t, GramPhaseEquiv (𝔾 t) (𝔾' t)`. Act 12 defines `GramPhaseEquiv` per
   slice and `TwoSidedRelated` on lifts; this round needs the relation on **trajectories**, because
   line 2's completeness direction and `TJ1`'s statement both compare trajectories that are not yet
   known to be a lift's. *Needed.*
2. **`SelectsAt`** — the selection predicate, `SelectsAt a₀ Γ S` holding iff there is a lift `U₀`
   with `CoherentLift a₀ Γ U₀` and `S U₀`, and every lift `U` with `CoherentLift a₀ Γ U` and `S U`
   has `GramTrajEquiv (𝔾 U) (𝔾 U₀)`. Lines 1 and 4 both quantify over it, and writing it out inline
   at each of the four members of `𝒮` would make line 4's statement unreadable. *Needed.*
3. **A predicate for `SP3`** — the homogeneous-transition condition as one `Prop` over a lift — *if*
   `TJ2` (d) and line 4 cannot be stated readably with the condition written inline; unused
   otherwise. *Conditional.*
4. **A named diagonal Gram tuple** — `fun i => Matrix.diagonal (fun j => ((Γ t) i j : ℂ))` as a
   definition — *if* `SP5`'s statement and its emptiness proof cannot be stated readably with it
   written inline; unused otherwise. *Conditional.*

**A fifth definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. **No lift, gauge element, witness, matrix, visible family, Gram tuple, entry
value or configuration is a top-level definition** — each is a bound variable pinned by an equation
in the statement that needs it, as acts 10, 11, 12, 13, 14, 15 and 16 did. Acts 7's, 10's, 11's,
12's and 13's definitions are **reused, not redefined**; in particular `FibreGram`, `GramPhaseEquiv`,
`RealizableGram`, `CoherentLift` and `TwoSidedRelated` are consumed and none is restated.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `TJ1`, for each part of `TJ2` whichever label it reaches,
and for `TJ3` whichever line of its hierarchy is reached other than line 5. `decide` over finite
index types is kernel-checked and permitted; `native_decide` is not, and neither is `sorry`.
`Classical.choice` is expected to appear in `TJ1`'s sufficiency direction, which assembles a lift
from a per-time choice, and its appearance there is not a defect.

**`TJ0` is type P and carries no evidence level.** It is settled by the frozen evidence rule —
verbatim quotation with a coordinate, or the recorded statement that the passage sought does not
exist on the named and bounded search — and by nothing else. **Reconstructive inference is forbidden
as a finding**, and where the record is silent the finding is that it is silent.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-TRJ`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_TRJ_SEALED_HEAD`** and **`_TRJ_MERGE`**, with
the base held in **`_TRJ_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 17 object
   enters the repository tree** — any Lean definition or proof about Gram trajectories, about the
   cross-time equivalence, about any candidate selection principle or about the graded hierarchy; any
   search artifact; any probe clause; any result artifact. **The single permitted exception is the
   analysis recorded inside this control-plane blob itself**, merged *as* the freeze, including the
   frozen evidence rule, the table of what the merged record supplies, and the pre-freeze survey
   recorded as the reason for `TJ0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_TRJ_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content at this exact path, and the
   execution ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _TRJ_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of
   `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_TRJ_SEALED_HEAD` and `_TRJ_MERGE` are present and **unset** at execution.
   After `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the
   same strong check against the sealed object: the pinned merge's second parent must equal the
   sealed head; the sealed head must pass clause 5 against `B` exactly as in its own run; and both
   must be reachable from the current target — the real `pull_request.head.sha` in pull-request
   continuous integration, `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change
   recording the two SHAs and nothing else.
8. **Existing seal constants are read with mutation controls and never written.** The guard clause
   checks `_RNC_SEALED_HEAD`, `_RNC_MERGE`, `_TCF_SEALED_HEAD`, `_TCF_MERGE`, `_PQT_SEALED_HEAD`,
   `_PQT_MERGE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE` equal to the values acts 16, 15, 14 and 13 set,
   because an archive seal belongs to the round that set it.
9. **This round's own triple is never a permanently fixed execution-mode value.** `R7-TRJ` must not
   assert `(_TRJ_BASE, _TRJ_SEALED_HEAD, _TRJ_MERGE)` equal to `(_TRJ_BASE, None, None)` as a
   standing invariant. Either the round's own triple is **excluded** from the prior-seal integrity
   clause of item 8 — which names other rounds' seals and is the shape this freeze intends — or it
   is checked **mode-aware**, the expectation being `(_TRJ_BASE, None, None)` while
   `_TRJ_SEALED_HEAD` is unset and `(_TRJ_BASE, _TRJ_SEALED_HEAD, _TRJ_MERGE)` once `P` has set
   them, and read from the module constants rather than from the argument, so that a fabricated
   tuple cannot define its own expectation. A clause that fixes this round's own pins at `None` for
   all time contradicts item 7, under which `P` must set them: the guard would then pass at no
   commit once the round lands, and the round's mandatory lifecycle could not complete. **This item
   exists because an earlier round wrote exactly such a clause and its whole execution object had to
   be rebuilt.** Prior rounds' seals stay read-only invariants exactly as item 8 states; this item
   constrains only how the round treats its **own** pins.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md \| git hash-object --stdin` equals the blob the `R7-TRJ` clause pins |
| 2 | Act 16's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_RNC_SEALED_HEAD = '31db7c1082b012c00c43f3fda35ce44c5653e123'` and `_RNC_MERGE = 'eb70bbb9b2b3311095945ec3ce2418962f3b741a'`, both non-`None` |
| 3 | Act 15's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, both non-`None` |
| 4 | Act 14's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` |
| 5 | Act 13's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` |
| 6 | The modules this round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` and `git cat-file -e B:verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` all succeed |
| 7 | No act 17 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` |
| 8 | The guard tag and its stem are still free | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-TRJ` and no occurrence of `_TRJ` |

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
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  Lean module, the result note, the `R7-TRJ` guard clause with `_TRJ_SEALED_HEAD` and `_TRJ_MERGE`
  present and unset, the `ROADMAP` propagation and the census entry. **No manuscript changes.**
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

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled
   named and no existing seal constant altered;
2. **the four frozen items as honoured** — the candidate list unchanged and closed, each candidate's
   data grant respected and checked, the cross-time equivalence used and no other, and each
   countercontrol either reached or recorded as not reached;
3. **`TJ0`** — the bounded search, recorded in full, with the per-term result and the finding stated
   as a finding about the record;
4. **`TJ1`** — the pointwise characterization, both directions or the direction reached, with the
   narrowing it records labelled **pointwise** in terms;
5. **`TJ2`** — the six parts, each reported separately with its frozen label and sentence, each
   refutation stated of the exact frozen proposition and of nothing in its neighbourhood, and each
   non-selection or emptiness verdict naming its configuration;
6. **`TJ3`** — the outcome as the highest line of the five-line hierarchy the kernel actually
   carries, in the status rule's frozen wording, with line 4's verdict reported alongside if it is
   also earned, and with the obstruction named specifically in the UNDECIDED case;
7. **the quantifier structure of whichever of lines 1, 2 and 4 is reported**, written out, together
   with the name of the relation any quotient is taken over;
8. **the scope boundary as honoured**: the demonstration that every act 13 threading-related pair is
   one trajectory for this round, and the confirmation that no statement of the round distinguishes
   two lifts the relation identifies;
9. **the anti-conflation clause carried verbatim at each mention**, with the count of carriages, and
   the confirmation that no target consumed act 15's or act 16's positives as evidence about
   trajectory freedom;
10. the frozen `P0` sentence for the case reached, verbatim, and the row's label unchanged;
11. what no outcome licenses, in this file's wording, and the status rule as honoured;
12. the relation to acts 11, 12, 13, 14, 15 and 16 — every merged label consumed, none revised —
    with `SH1` and `TG3` consumed at their own strengths;
13. the definition count against the four-slot budget, with each conditional slot marked fired or
    unused;
14. the chronology certification, naming the property certified, the eight preconditions checked at
    `B`, and the archive-mode pins as unset at execution;
15. the axiom table with one line per named result;
16. the discrepancies, if any, recorded and not repaired.

## Open decisions for the owner, to be settled before this freeze merges

Under `§A.37` this file is immutable once merged, so these are settled **before** the merge and not
afterwards. Each is a fork with alternatives and this draft's recommendation; the draft as written
takes the recommended branch in every case, and changing a branch changes the sections named.

1. **The strength of the ask.** (a) **Constraints-only** — the round asks what excludes trajectories
   and undertakes neither uniqueness nor classification. (b) **Uniqueness** — the round's obligation
   is line 1 and every lower line is a shortfall. (c) **Classification** — the obligation is line 2,
   with the completeness direction mandatory. **Recommendation: (a)**, and the draft takes it. The
   merged record already carries act 12's `TG3`, two admissible dilations of one visible law in
   different orbits, so a uniqueness ask would preregister an obligation the freeze expects to be
   unreachable from the licensed data; and a classification ask would require a surjectivity proof
   over the trajectory space that the definition budget does not fund. *Changing this changes*: the
   ask section, the prediction table's calibration, `TJ3`'s obligation, and the `P0` sentence's
   Case A.
2. **Whether a surprise upper-line result is reportable or parked.** (a) **Reportable** — lines 1 and
   2 are preregistered as reachable with their own frozen sentences and their own evidence bars, so
   a stronger result is reported because it was preregistered and never because the round enlarged
   itself. (b) **Parked** — a proved uniqueness or classification theorem is recorded as an
   out-of-scope observation and the reported outcome stays inside the constraints-only ask.
   **Recommendation: (a)**, and the draft takes it. Under (b) a kernel-proved theorem would sit in
   the record without a frozen sentence, which invites the execution to describe it in wording of its
   own — the failure the status rule exists to prevent. Under (a) the scope is still fixed before the
   search, because the bar for lines 1 and 2 is frozen here. *Changing this changes*: the last
   paragraph of the ask section, `TJ3`'s lines 1 and 2, their frozen sentences, and hazard 13.
3. **Whether line 3 requires a CROSS-TIME constraint, or admits a pointwise one.** (a) **Cross-time
   required** — clause (iii) of line 3, with the inequivalence to any pointwise condition proved.
   (b) **Pointwise admitted** — any proper narrowing earns line 3, including `TJ1`'s rank bound
   lifted to trajectories. **Recommendation: (a)**, and the draft takes it. Under (b) line 3 is
   earned by restating act 12's `SH1` over all times, the ladder loses its discriminating power at
   exactly the boundary the hierarchy exists to police, and the round's predicted outcome silently
   moves from line 4 to line 3. *Changing this changes*: line 3's frozen statement, its frozen
   sentence, `TJ1`'s bounded reading, the prediction table's `TJ3` row, and hazard 8.
4. **The membership of the frozen selector class `𝒮`.** (a) **Four members** — `SP1L`, `SP2`, `SP3`,
   `SP5` — with `SP1G` a determination claim and `SP4` a regime probe, neither in the `∀`-scope of
   line 4. (b) **Five members**, admitting `SP1G` by reformulating it as a per-lift predicate
   relative to a fixed function of the law. (c) **Three members**, dropping `SP3` as the least
   grounded in the merged record. **Recommendation: (a)**, and the draft takes it. `SP1G` is not a
   predicate on one lift and forcing it into that shape would require the free function `Φ`, which
   any candidate could then fit to any configuration, making "selects" meaningless. *Changing this
   changes*: the candidate section, the class definition, line 4's statement, and the prediction
   table.
5. **The adjunct rule when a higher line and line 4 are both earned.** (a) **Report the higher line
   as the outcome and line 4 alongside with its own frozen sentence.** (b) **Report line 4 as the
   outcome**, on the ground that a class-level impossibility theorem is the stronger claim.
   (c) **Report only the higher line**, discarding line 4. **Recommendation: (a)**, and the draft
   takes it, because the owner's canonical order places line 4 below line 3 and (c) would discard a
   proved theorem. The tension is real and is recorded here rather than hidden: the ordering treats a
   positive narrowing as better than a negative impossibility, which is a judgement about what the
   programme wants and not a mathematical fact. *Changing this changes*: the adjunct rule and the
   allowed final report's item 6.
6. **Whether `SP4` is executed at all.** (a) **Executed as a regime probe outside `𝒮`**, so that the
   effect of crossing the data line is on the record as a theorem. (b) **Not executed**, and the
   containment recorded in prose only. **Recommendation: (a)**, and the draft takes it: the
   containment is a one-line consequence of `fibreCrossGram_diag` being `rfl`, and having it in the
   kernel is what makes the data regime a checkable constraint rather than an exhortation. *Changing
   this changes*: the data regime section, `TJ2` (f), and the prediction table.
7. **Whether the `SP3` variant that reads the visible law is executed.** (a) **Not executed**, named
   and parked for a later round, which is the draft. (b) **Executed as a sixth candidate.**
   **Recommendation: (a)**. The law-reading variant is a weaker and different proposition, and adding
   it would put a fifth member in `𝒮` and a fifth conjunct in line 4, for content the freeze cannot
   predict at better than low. *Changing this changes*: the candidate section, `𝒮`, line 4 and the
   definition budget.
8. **Whether the uniform-phase relation is tested rather than merely recorded.** (a) **Recorded as a
   distinct relation this round does not adopt**, which is the draft. (b) **Tested**, by asking
   whether it differs from `≈_O` on some pair of coherent lifts. **Recommendation: (a)** for this
   round. Under (b) the round would be asking a question about the relation itself, which is a
   different question from what constrains the trajectory, and the answer would not bear on any line
   of the hierarchy. It is a clean target for a later round. *Changing this changes*: the equivalence
   section and the target list.
9. **Whether the execution may report a candidate's verdict at a configuration of its own choosing.**
   (a) **Only at configurations this freeze names** — the Hadamard family and the deterministic
   island — which is the draft, since the countercontrol table names the configuration for every
   verdict. (b) **At any configuration it constructs**, provided the construction is exhibited.
   **Recommendation: (a)**, because a configuration chosen after an outcome is known is a
   preregistration failure in miniature. *Changing this changes*: the countercontrol table and the
   `TJ2` evidence bars.
