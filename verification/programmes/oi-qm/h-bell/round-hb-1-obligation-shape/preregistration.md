# H-Bell round 1 — the shape of the obligation: CONTROL PLANE

Owner-called. This file is the whole of the round's control plane and is merged **alone**, before
any execution object exists. It takes up one question about the `ROADMAP` row `P1 — H-Bell —
composite and Bell closure`: **what shape is the obligation in** — what H-Bell would require, which
of its inputs exist and in what form, which do not exist on a named bounded search, and what a later
round would have to build.

**Blob identity is authoritative.** The execution guard pins this file by path and content.

## The round's shape, declared first, in `§A.37`'s terms

**Type-P round.** Every substantive target is a determination about **what the merged record and the
manuscripts say**. Nothing is proved about graphs, curvature, measures or matrices; no Lean is
written; no kernel object is produced. The round is settled by locating and quoting, and its
evidence rule is frozen below.

**NON-SEALING round, under `AGENTS.md` `§A.37`.** The rule keys the landing shape to what a round
**owns**, not to what it touches:

> **A non-sealing round — a round that owns no seal state — takes `L` alone.** It **may** modify
> other contracts inside an existing guard; it **may not** alter existing seal constants. It has
> nothing to pin, and a pin commit added there would pin nothing.

and, in the same section:

> **An archive seal belongs to the round that set it, and stays immutable afterwards.** A later
> round does not re-pin it, and does not acquire a pin commit merely by touching the guard file that
> carries it. An existing seal constant changes only in a round whose own preregistration says in
> advance that it changes it — and such a round is *sealing*, because it has taken ownership of that
> state prospectively rather than as a side effect of its diff.

**So the round lands `E` → `L`, with no archive-pin commit `P`.** The justification is the ownership
rule applied to a definition budget of zero: the execution writes no Lean module, so there is no
kernel object for an ancestry guard to order, there is no ancestry check to move from execution mode
to archive mode, and a `P` commit added here would pin nothing. A sealing shape is not held in
reserve and is not taken "if needed": an outcome that would require creating or changing seal state
is **out of scope for this round**, and an execution that finds itself wanting one is recording a
discrepancy rather than exercising a permission.

### What this round would own, and what it would not

**It would own, and may change, guard contracts that are not seal state.** The execution **adds** exactly one
clause to `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-HBS`**, whose
whole content is a **content contract**: that this preregistration is present at its path with the
blob this control plane merges as; that the result note is present at its path; and that the
`ROADMAP` row `P1 — H-Bell` carries the label the status rule leaves it carrying. That clause
declares **no** `_HBS_BASE`, **no** `_HBS_SEALED_HEAD` and **no** `_HBS_MERGE`, and performs **no**
ancestry check.

**It would own no seal state and may touch none.** Every constant below is read and never written,
each belonging to the round that set it:

| seal constant | owner round | this round's access |
| --- | --- | --- |
| `_PC4_BASE`, `_PC4_SEALED_HEAD`, `_PC4_MERGE` | physical C4 round 1 | read only |
| `_PC4S_BASE`, `_PC4S_SEALED_HEAD`, `_PC4S_MERGE` | physical C4 round 2 | read only |
| `_TCF_BASE`, `_TCF_SEALED_HEAD`, `_TCF_MERGE` | Track B act 15 | read only |
| `_CTI_*`, `_PQT_*`, `_A6P_*`, `_A6D_*`, `_A6I_*`, `_HYA_*`, and every other `_*_BASE`, `_*_SEALED_HEAD` or `_*_MERGE` in that file | their own rounds | read only |

The execution's diff against `edge_rigidity_probe.py` **adds** the `R7-HBS`
clause and changes nothing else in the file.

**The landing shape does not turn on that clause.** The round is non-sealing and lands `E` → `L`
because it owns no seal state, and a content contract is not seal state. The clause is required, so
this preregistration is pinned by the guard and by the start-state tables together, and the opening
statement that the execution guard pins it by path plus blob holds without qualification. The
decision is recorded in *Settled by the owner before this freeze merges* below.

## What this round is not, stated before anything else

This is the boundary the round is most likely to be pushed across, so it is stated before the
targets rather than after them.

**This round does not preregister Bell-inclusive closure.** It does not preregister full-substratum
uniqueness. It preregisters **no target whose success would amount to establishing either**, and no
target whose success would amount to satisfying H-Bell, discharging any conjunct of H-Bell, or
re-founding the curvature functional. The reason is quoted rather than asserted: `verification/ROADMAP.md`
lines `764–769`, under the section `P1 — H-Bell and composite closure`, carried here word for word
because the whole scope of this round is fixed by it:

> **And H-Bell is downstream of a harder obligation**, which this row records rather than leaves
> buried: for the degree-6 cubic reference graph the intrinsic hop metric is exactly `ℓ¹`, a `√2`
> diagonal stretch that does not decay at any scale, so the hop-metric curvature route fails for the
> reference family **before any Bell edge is added**. The curvature functional has to be re-founded on
> the propagation/Laplacian geometry rather than on shortest-path counts. Bell-inclusive
> full-substratum uniqueness is not established.

**The curvature re-founding is an unmet upstream obligation, and this round does not meet it.** It
is named here as out of scope, for every target, under every outcome. What this round does *instead*
is establish **the shape of the obligation**: what H-Bell would require, in the manuscripts' own
enumeration and in the queue's; which inputs exist on the merged record and in what form; which do
not exist on a named bounded search; and what a later round would have to build. A census of an
obligation is not a discharge of it, and no sentence of this round's artifacts may treat it as one.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared. A file
that moved is the same file; a file that was rewritten is not.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `papers/Main.md` | `a8de3cb760fcb56be7e661bc388b71f7ba2316fb` |
| `papers/Substratum.md` | `9ac6b732e8786897cade416b67c3f7f1df81ab84` |
| `papers/SM.md` | `26d6cbfb230c105eb00a979c2b69c363568455dd` |
| `papers/GR.md` | `0258ccb7a5ef02877a01638428ae7ab8ba91bf71` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md` | `a80334a5d5f19125b69459523acf723b607f97e1` |
| `verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md` | `64a610859e834663cf1d5cc73d0ab9a2ab9dd882` |
| `verification/programmes/physical-realization/round-c4-2-storage-readback/preregistration.md` | `16cfd1303e7c279c8d6bab68b7112c3f25a7460e` |
| `verification/programmes/physical-realization/round-c4-2-storage-readback/result.md` | `db94942843bd806df3c5e6ba80b77b9445488d4e` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md` | `1d649101fa5013d1f484711e8d7deaab188424f8` |
| `verification/programmes/oi-qm/track-i/causal-readback-discovery/result.md` | `9dfc5a4785045c69f8daccff69168159a3c7ec6f` |
| `verification/programmes/oi-qm/PROGRAMME.md` | `56b399443d19c65c315a935647147e6749356add` |
| `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean` | `832eeac3ee5f8df770b478b272842729183c7e48` |
| `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` | `8bdf3c77acf51f074c4f05dc440e3511137cdf9c` |
| `verification/lean-mathlib/OIBridge/CausalReadback.lean` | `d7b71cf56aaddb24724653caa0d96b525134f95e` |
| `verification/lean-mathlib/OIBridge/IndependenceCensus.lean` | `b31f8ea03736af2b3dfedd316ecd85ae363e1d27` |
| `verification/lean-mathlib/OIBridge/OIRealization.lean` | `4df632b73d3cfefc5923958a802319a552150afc` |
| `verification/lean-mathlib/OIBridge/StochasticInterface.lean` | `0f4d1b1625e9c5c5070750bab04c9c989f0f0d04` |
| `verification/lean-mathlib/OIBridge/SubstratumInterface.lean` | `1c61fa6e4e5a668af55eea074898e87cc3866c06` |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean` | `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| `verification/lean-mathlib/OIBridge/CubicIsotropy.lean` | `c1918dc0c4ffaf1547f1918e6665f7c086233796` |
| `verification/lean-mathlib/OIBridge/ImplementationLocality.lean` | `d96b65bd262e658baf0be52cfaf4b6e33de0dd28` |
| `verification/lean-mathlib/OIBridge/CompositeSoundness.lean` | `3e153fa433f644a3746a36e09a4558e24f475d4b` |
| `verification/lean-mathlib/OIBridge/CompositionalIndependence.lean` | `7279014f320f1a9356935e2d36571dc4e0d9ca98` |
| `verification/lean-mathlib/OIBridge/MonoidalCompletion.lean` | `b1b7e0103a5b6fbe590ea003804214501aa9c0a5` |
| `verification/lean-mathlib/OIBridge/SpectatorBridge.lean` | `b4cdd8c36b77291ee8119181bd8cc2eb9fa83781` |
| `verification/lean-mathlib/OIBridge/Separability.lean` | `b36bb84357cc9b962bfaf78547f60c67e131c665` |
| `verification/lean/physical_c4_storage_readback_probe.py` | `4ba2fd45a9affbeb22a29ea48ff8290123866842` |
| `verification/lean/physical_c4_toy_instance_probe.py` | `4dc012429ca598dff8022de1ae4db404a268b61c` |
| `verification/lean-manuscript-census.json` | `3e968e6c970301be5ba0b9631b234c957a6222d1` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

### The bounded-search surfaces, pinned by tree

`HB2`, `HB3` and `HB5` are settled in part by searches over whole directories rather than over
enumerated files, so those directories are pinned **by tree hash** at the same base. A tree hash
pins a directory by content exactly as a blob pins a file, and it is what makes a recorded absence
checkable: the execution states which tree it searched.

| directory | tree at the base |
| --- | --- |
| `verification/lean-mathlib/OIBridge` | `272c38eae04ecbb7d9980f8879243c4fa2dcfd3f` |
| `verification/lean` | `881fb525fb0f60d05c0945e4023d147dfa60b3b4` |
| `verification/programmes` | `55820145f5ea02323fd85c1722f06375a0a6e8b8` |
| `verification/audits` | `545381ec6e3b2890eda124c22b15304a1f9626df` |
| `papers` | `4db74e8a3b176aa69892612e6544acf433d2cfcc` |

The read-only clause above governs these directories too, and a tree that differs at the base is a
discrepancy recorded in the same way as a blob that differs.

### Files this round reads AND writes

These are **not** covered by the read-only clause above, and are listed separately so that the
clause is exact rather than approximately true. Each is pinned by blob at this base all the same, so
that a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads.

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | **read** as the pinned statement of the row, the section and the status vocabulary; **written** only by appending the frozen post-round paragraph for the case reached, inside the existing section `P1 — H-Bell and composite closure`; the row's label and the row's five cells unchanged |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the `R7-HBS` content clause **added**; **no seal constant, no merge constant, no base constant altered**, and nothing else in the file changed |
| `verification/README.md` | `d25eb2d44d0aa324c095930f40174296fd0f2279` | one appended paragraph recording this round; no existing paragraph edited |
| `verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/result.md` | absent | this round's result note, created by the execution |

A blob difference in a written file at the base is recorded in the same way as one in a read-only
file, and the execution proceeds from what it finds rather than from what the table says.

### The anti-contamination invariant, FROZEN VERBATIM

> A start-state discrepancy does not license the execution to consume the newer sibling result merely
> because it happens to be present at its mandated base. The round consumes only what its freeze says
> it consumes.

**Its `§A.37` justification, stated in terms.** Under `§A.37` the control plane's **merge commit is
the mandated execution base**: the execution branches from this control plane's merge commit and
from nothing else. The base is therefore *fixed* at the moment this file merges, and everything that
reaches `main` afterwards is outside it. Sibling results that happen to be present at that base —
and several will be, since sibling control planes open and land concurrently — **are not inputs to
this round**. Their presence is a fact about the tree, not a licence to read them.

**Why it bites hardest here.** A round whose whole business is recording what does and does not
exist is exactly the round most tempted to reach for a result that arrived after the freeze, because
a newer result would change a recorded absence into a recorded presence. It does not: an absence
recorded against this freeze's pinned blobs and trees is a statement about those blobs and trees,
and it stays true whatever lands later.

## Locating controls quoted at the base

The governing passages, each with its coordinate, quoted here so that the targets are stated over
located text rather than over remembered text. `HB0` re-locates every one of them at the execution
base and records any that has moved.

### The queue row and its section

`verification/ROADMAP.md`, line `67`, the queue table:

```
| **P1** | H-Bell — composite and Bell closure | OI→QM / Bell | **OPEN** | Bell-inclusive completion |
```

`verification/ROADMAP.md`, lines `758–762`, the section `P1 — H-Bell and composite closure`:

> Full operational quantum mechanics in the sense of entangled composites, local operations and Bell
> correlations needs more than the finite rooted-law equivalence. H-Bell requires the
> preparation-indexed state-dependent graph family to preserve operational no-signaling **and** to
> satisfy a curvature/metric convergence condition strong enough for the Ollivier–Ricci continuum step
> the Einstein reconstruction uses.

`verification/ROADMAP.md`, lines `22–31`, the status vocabulary, read **literally**; its seven
entries are the whole menu, and this round adds no label and redefines none.

### The manuscripts' statement of H-Bell

`papers/Substratum.md`, line `132`, the enumeration this round treats as the manuscripts' own
statement of what H-Bell would require:

> H-Bell is the remaining compatibility statement for that branch: the preparation-indexed graphs
> must (i) supply the required ontic parameter dependence, (ii) preserve operational no-signaling,
> and (iii) satisfy a metric/Ollivier--Ricci stability condition strong enough that the
> continuum-curvature step of [SM §3.1] remains valid on the state classes to which the Einstein
> reconstruction is applied. [...] H-Bell is therefore an explicit
> curvature-stability/composite-existence hypothesis, not a consequence of A1–A6 or of the
> nearest-neighbor wave equation.

`papers/Substratum.md`, line `130`, the hypothesis' own statement, and line `192`, Theorem 23, whose
closing sentence bounds what the reconstruction establishes: *"The theorem does **not** establish
uniqueness of that Bell-inclusive full completion."*

`papers/Main.md`, line `394`, the Bell–lattice obstruction corollary, and line `392`, branch (a);
`papers/Main.md`, line `212`, the four standing scope conditions carried throughout the framework,
and line `678`, §4.2 Scope; `papers/Main.md`, line `22`, the abstract's statement of the two
logically separate completion questions.

`papers/SM.md`, lines `140–146`, the discrete Einstein equation with its proof step (iv) and the
recorded reference debt, and line `148`, the sparse preparation-indexed-edge diagnostic with its own
closing disclaimer that it *"is not a theorem that $\kappa_{OR}$ converges everywhere"*.

### The upstream obligation, quoted verbatim

`papers/Substratum.md`, line `170`, **Bell compatibility**, the manuscript's own statement of the
same upstream obligation the `ROADMAP` paragraph records:

> Nor does it cover the unperturbed reference graph, and there the situation is worse
> than open: the degree-$6$ cubic hop metric is exactly $\ell_1$, with a scale-independent $\sqrt2$
> diagonal stretch, so the hop-metric curvature route fails for the reference family and no $D=3$
> extension of the cited theorem would rescue it. The repair is to re-found curvature on the
> propagation/Laplacian geometry, which the substratum's isotropic leading dispersion already
> supplies [SM §3.2].

The `ROADMAP`'s own statement of it is carried verbatim in *What this round is not* above, at its
coordinate, and is not repeated here.

## The two readings of the store clause: THE READBACK CLAUSE, FROZEN VERBATIM

An input to this round was corrected by the physical C4 round 2 sealed execution, and the correction
changes what may be said about the store clause of the realization condition. The clause below is
**THE READBACK CLAUSE**, and it is carried as a block quote **at every prose mention of the two
readings** in this file and in every artifact of this round.

**THE READBACK CLAUSE:**

> `RoutedReadback` is physical C4 round 1's predicate and `RoutedReadbackAtStorage` is round 2's. `RoutedReadback` conditions the **initial hidden seed**; `RoutedReadbackAtStorage` conditions the **hidden state at the storage time**. Round 2 established that **neither implies the other**, by two exhibited carriers with exact certificates: neither is stronger, neither is weaker, and no ordering of them is asserted. **Neither is the correct reading of C4** — round 2's bounded search found the manuscripts silent on which random variable the realization clause's record is at the storage surface, and the silence is the finding. **"The C4 reading" therefore names no single predicate.** Any determination of this round that consumes a readback predicate names which of the two it consumes, at the point of consumption; a sentence that consumes "the C4 reading", or that reads a statement about one predicate as a statement about the other, is a **defect of this round** and is checked for in the final report.

The clause's warrant is quoted, not paraphrased. `round-c4-2-storage-readback/result.md`, lines
`444–447`, the frozen post-round sentence for `CS5-b`:

> Neither reading implies the other, by two exhibited carriers with exact certificates; the two are
> incomparable as predicates, and no ordering of them is asserted.

and lines `475–477`, from that round's own list of what its outcomes do not license:

> **No claim that `RoutedReadbackAtStorage` is the correct reading of C4.** The round determines what
> the record says and what each predicate carries on each carrier. Which reading the manuscripts
> intend is the question `CS0-d` asked of them, and they are silent.

### How each carriage is written, and why

Each carriage opens with one line naming where it is being carried, and then states the clause word
for word. The naming line is there so that the carriages read as distinguishable copies of one
clause rather than as one paragraph pasted repeatedly — which is a defect the repository's
`duplicate_check` exists to catch — and it changes nothing about the clause it introduces.

### Where THE READBACK CLAUSE is carried, and where it is not

**Carried, as a block quote with its own naming line:** in `HB3`'s treatment of the readback row of
the census; in `HB4`, which is the target the correction bears on; in the status rule; and in
hazard 2.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE READBACK CLAUSE: the byte-fixed
post-round sentences, which carry the clause's substance in their own frozen wording and cannot
admit a quotation inside a quotation; and the bare entries of *What no outcome of this round
licenses* and of the start-state tables, which do nothing but name the two predicates or their
files.

## The objects, FROZEN

**`ROW`** — the row `P1 — H-Bell — composite and Bell closure` of `verification/ROADMAP.md`, quoted
above, with its five cells.

**`VOCAB`** — the queue's status vocabulary, `verification/ROADMAP.md` lines `22–31`, read
literally.

**`OBLIGATION`** — what H-Bell would require. Located, not reconstructed, and located in **two
statements kept apart**: the manuscripts' enumeration (`[Substratum]` line `132`, its three
conjuncts (i)–(iii), with `[Main]` line `394` and `[Substratum]` line `130` as its companions) and
the queue's (`ROADMAP` lines `758–762`, its two conjuncts). The two are reported separately and
never merged; if they differ, the difference is the finding and is reported as a discrepancy of the
record rather than repaired.

**`UPSTREAM`** — the curvature re-founding: the obligation the `ROADMAP` paragraph and
`[Substratum]` line `170` place **before** H-Bell, which no round has met. It is an object of the
census and never a target of the round.

**`INPUTS`** — the named ingredients H-Bell's statement quantifies over, each to be classified as
present in the kernel, present in the manuscripts in words only, or absent on a named bounded
search.

**`BUILD`** — what a later round would have to build: the separable jobs each of which is derived
from a quoted obligation and each of which the record says is not begun. A census of absences, never
a plan asserted to suffice.

The round adds **no** object of its own. Where a distinction is needed that the record does not
draw, the execution **records that the record does not draw it** and does not draw it on the
record's behalf.

## The evidence rule, FROZEN

**This is a type-P round.** Every substantive determination must be carried by one or more of:

1. a **verbatim quotation** from a pinned blob, with its file path and line coordinate; or
2. a **verbatim quotation** from a merged result note, preregistration or audit, with its
   coordinate; or
3. an explicit, recorded statement that **the passage or declaration sought does not exist** on the
   record searched, with the search **named and bounded** — the tree enumerated by its pinned hash,
   the file set stated, the search terms listed, and the result recorded for each term.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the record must
contain X, because otherwise Y would not have been written" may appear only in a clearly labelled
analysis paragraph that states it is not evidence and that no target rests on it.

**Silence is a finding.** Where the record is silent, the finding is that it is silent — not that
the thing sought is false, and not that it is true. In particular, that no kernel object bears on
`UPSTREAM` would be a fact about the kernel at a pinned tree, and **not** an argument that the
curvature re-founding is impossible, nor that it is available.

**Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`. A
determination carried by a passage that names a thing without displaying it is at most `medium`.

### The bounded searches, fixed now

Fixed here so that their boundaries cannot be chosen after their results are known.

**Search `S-curv`, for `HB2`.** File set: every `*.lean` file under
`verification/lean-mathlib/OIBridge` (tree `272c38eae04ecbb7d9980f8879243c4fa2dcfd3f`) and under
`verification/lean` (tree `881fb525fb0f60d05c0945e4023d147dfa60b3b4`); every `*.py` probe under
`verification/lean`; every `preregistration.md`, `result.md` and amendment under
`verification/programmes` (tree `55820145f5ea02323fd85c1722f06375a0a6e8b8`); every `*.md` under
`verification/audits` (tree `545381ec6e3b2890eda124c22b15304a1f9626df`); and `verification/ROADMAP.md`,
`verification/README.md` and `verification/lean-manuscript-census.json`. Terms: `Ollivier`, `Ricci`,
`curvature`, `kappa_OR`, `hop metric`, `hop-metric`, `shortest path`, `graph metric`, `Laplacian`,
`dispersion`, `continuum limit`, `mesoscopic`, `area law`, `Jacobson`, `Einstein equation`,
`re-found`, `refound`. The question asked of each hit: **does this declaration or passage state a
curvature functional on the substratum's propagation or Laplacian geometry, or a convergence theorem
for one?** The recorded answer per hit is one of: *supplies it* (quoted, with coordinate); *does not
supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

**Search `S-inputs`, for `HB3`.** Same file set and same trees. Terms, grouped by the ingredient
each tests: `Bell`, `CHSH`, `PR box`, `PR-box`, `Tsirelson`, `nonlocal`, `no-signaling`,
`noSignaling`, `no_signaling`, `signalling`; `coupling graph`, `causal cone`, `adjacency`,
`preparation-indexed`, `state-dependent graph`, `G(x)`, `long edge`, `long-edge`; `composite`,
`tensor`, `local tomography`, `spectator`, `ancilla closure`, `instrument`; `Ollivier`, `Ricci`,
`curvature`. The question asked of each hit: **does this declaration or passage supply, as a formal
object or as a stated manuscript condition, the ingredient the row is about — and if so, at what
scope?** Recorded answers as for `S-curv`.

**Search `S-hbell`, for `HB5` and `HB6`.** Same file set and same trees, plus `papers` (tree
`4db74e8a3b176aa69892612e6544acf433d2cfcc`). Terms: `H-Bell`, `M1-B`, `Bell-inclusive`,
`Bell closure`, `composite and Bell`, `Bell-violating completion`. The question asked of each hit:
**does this passage state a job H-Bell would require, and does it record that job as begun, in
progress, or not begun?** Recorded answers as for `S-curv`.

**A search that finds the thing is a finding, and a search that does not is equally a finding** —
the second being that the record is silent on the point.

## The targets, FROZEN

Seven targets, `HB0` through `HB6`. Each names what settles it and what evidence counts. **No target
attempts, and no target's success would amount to, Bell-inclusive closure, full-substratum
uniqueness, the discharge of any H-Bell conjunct, or the curvature re-founding.**

### `HB0` — locating controls, cheap and certain

Re-locate and quote, with coordinates at the execution base, every passage of *Locating controls
quoted at the base*: `ROW`; `VOCAB`'s seven entries; the `ROADMAP` section `P1 — H-Bell and
composite closure` in full, including the harder-obligation paragraph; `[Substratum]` lines `130`,
`132`, `170` and `192`; `[Main]` lines `22`, `212`, `392`, `394` and `678`; `[SM]` lines `140–146`
and `148`; and, for THE READBACK CLAUSE's warrant, `round-c4-2-storage-readback/result.md` lines
`444–447` and `475–477`.

**Falsifier.** Any of these absent from the pinned blobs at the base, or present at a different
coordinate. A coordinate that has moved is recorded and the quotation is re-taken; a passage whose
text has changed is a start-state discrepancy and is recorded, not repaired.

### `HB1` — what H-Bell would require, decomposed by quotation

Determine, by quotation alone, the exact content of `OBLIGATION`, reported as **two enumerations
kept apart**:

- **`HB1-m`, the manuscripts' enumeration.** `[Substratum]` line `132`'s three conjuncts (i), (ii)
  and (iii), each quoted as its own item, together with `[Substratum]` line `130`'s statement of the
  implementation the conjuncts are about and `[Main]` line `394`'s statement of what remains to be
  proved.
- **`HB1-q`, the queue's enumeration.** The `ROADMAP` section's two conjuncts — preservation of
  operational no-signaling, and a curvature/metric convergence condition strong enough for the
  Ollivier–Ricci continuum step — quoted as its own item each.

Then determine, and report as a third and separate item, **whether the two enumerations are the same
list**. The candidate difference to be checked and not assumed: `HB1-m` carries a conjunct (i) about
supplying the required ontic parameter dependence that `HB1-q` does not state. Whether that is a
difference of content or of compression is what the item settles, and if the record does not say,
the finding is that it does not say.

**This target does not judge any conjunct discharged, undischarged, easy or hard.** It reports what
the two statements say.

### `HB2` — the upstream obligation, and what the record carries toward it

Determine, by quotation, that `UPSTREAM` is stated on the record and is stated as unmet: the
`ROADMAP` paragraph, `[Substratum]` line `170`, and `[Main]` line `394`'s corollary, each quoted
with its coordinate and each reported separately. Determine also, by quotation, the manuscripts' own
statement of the reference debt at `[SM]` line `146` step (iv) and of the diagnostic's limits at
`[SM]` line `148`.

Then run **search `S-curv`** and record, per the evidence rule, whether the merged record carries
**any** formal object or landed round bearing on the curvature re-founding — a curvature functional
on propagation or Laplacian geometry, or a convergence theorem for one.

**The finding is the search.** A recorded absence here is a statement about the pinned trees and is
**not** a claim that the re-founding is impossible, not a claim that it is available, and **not a
step toward performing it**. `CubicIsotropy.lean`'s result — that cubic symmetry forbids quadratic
anisotropy, with the quartic term deliberately not rotationally invariant — is to be recorded as
what it is and specifically **not** as bearing on the hop-metric obstruction, which is a statement
about the intrinsic graph metric and not about a Fourier symbol.

### `HB3` — the input census: which inputs exist, and in what form

For each ingredient below, determine and record exactly one classification, with its evidence:
**KERNEL** (a formal object exists; name the identifier and its module, and state its scope),
**WORDS** (the manuscripts state it and the kernel does not; quote it with its coordinate), or
**ABSENT** (neither, on search `S-inputs`, with the search recorded).

| # | ingredient | where the obligation names it |
| --- | --- | --- |
| 1 | preparation-indexed / state-dependent adjacency `G(x)` | `[Substratum]` 130; `[SM]` 140 |
| 2 | operational no-signaling for the prepared family | `[Substratum]` 132 (ii); `ROADMAP` 758–762 |
| 3 | ontic parameter dependence | `[Substratum]` 132 (i); `[Main]` 392 |
| 4 | the coupling-graph causal cone | `[Main]` 358–360 |
| 5 | Ollivier–Ricci curvature, mesoscopic curvature, and their convergence | `[SM]` 144–146; `[Substratum]` 132 (iii) |
| 6 | the intrinsic hop metric and its `ℓ¹` identification | `ROADMAP` 764–769; `[Substratum]` 170 |
| 7 | the propagation/Laplacian geometry the re-founding would use | `ROADMAP` 767–768; `[Substratum]` 170 |
| 8 | the discrete Einstein equation and the area law | `[SM]` 140–146 |
| 9 | the composite / operational-lifting conditions | `[Main]` 22, 212, 409 ff. |
| 10 | Bell, CHSH and the PR-box construction | `[Main]` 354 ff., 392 |
| 11 | the readback predicates of the physical C4 programme | `OIBridge/PhysicalC4Discharge.lean`; `OIBridge/PhysicalC4StorageReadback.lean` |

**Row 11 is where the correction bites, and THE READBACK CLAUSE is carried at it.**

> **THE READBACK CLAUSE, carried at this mention — the readback row of the `HB3` census.** `RoutedReadback` is physical C4 round 1's predicate and `RoutedReadbackAtStorage` is round 2's. `RoutedReadback` conditions the **initial hidden seed**; `RoutedReadbackAtStorage` conditions the **hidden state at the storage time**. Round 2 established that **neither implies the other**, by two exhibited carriers with exact certificates: neither is stronger, neither is weaker, and no ordering of them is asserted. **Neither is the correct reading of C4** — round 2's bounded search found the manuscripts silent on which random variable the realization clause's record is at the storage surface, and the silence is the finding. **"The C4 reading" therefore names no single predicate.** Any determination of this round that consumes a readback predicate names which of the two it consumes, at the point of consumption; a sentence that consumes "the C4 reading", or that reads a statement about one predicate as a statement about the other, is a **defect of this round** and is checked for in the final report.

So row 11 is recorded as **two rows in the result note, one per predicate**, each with its own
identifier, its own module and its own scope, and never as one row for "the readback predicate".

**A `KERNEL` classification is not a discharge.** It records that an object exists at a stated
scope, and nothing about whether the obligation's conjunct holds of the physical substratum.

### `HB4` — does the obligation consume a readback predicate at all, and if so which?

Determine, by quotation from the pinned blobs and by search `S-hbell`, whether the record makes
H-Bell consume a readback predicate of the physical C4 programme — and, if it does, **which reading**
it consumes, named in the record's own words.

> **THE READBACK CLAUSE, carried at this mention — the target that asks which reading, if any, the obligation consumes.** `RoutedReadback` is physical C4 round 1's predicate and `RoutedReadbackAtStorage` is round 2's. `RoutedReadback` conditions the **initial hidden seed**; `RoutedReadbackAtStorage` conditions the **hidden state at the storage time**. Round 2 established that **neither implies the other**, by two exhibited carriers with exact certificates: neither is stronger, neither is weaker, and no ordering of them is asserted. **Neither is the correct reading of C4** — round 2's bounded search found the manuscripts silent on which random variable the realization clause's record is at the storage surface, and the silence is the finding. **"The C4 reading" therefore names no single predicate.** Any determination of this round that consumes a readback predicate names which of the two it consumes, at the point of consumption; a sentence that consumes "the C4 reading", or that reads a statement about one predicate as a statement about the other, is a **defect of this round** and is checked for in the final report.

Three outcomes, and exactly one is recorded:

- **`HB4-named`** — the record makes H-Bell consume a readback predicate and names which reading.
  Requires a quotation that names the predicate or the random variable, not merely the condition
  label.
- **`HB4-silent`** — the record does not make H-Bell consume a readback predicate, on search
  `S-hbell`. The finding is the silence, recorded with the search.
- **`HB4-UNDECIDED`** — the record connects the two without naming a reading, so that which reading
  is meant cannot be settled by quotation. The obstruction is named and quoted, and **no reading is
  supplied on the record's behalf**.

**Under every outcome, no ordering of the two predicates is asserted and neither is called the
correct reading of C4.** Round 2's own boundary is quoted where this target is reported:
`round-c4-2-storage-readback/result.md` lines `485–487`, *"**Nothing about H-Bell**, locality,
composites, Bell correlations or the Ollivier–Ricci step. **H-Bell is downstream of this round and
is not entered here**; its freeze must consume this round's execution result, which did not exist
before this head."* This freeze is that freeze, and consuming that result is exactly what `HB3` row
11 and this target do.

### `HB5` — what a later round would have to build

Enumerate, from the quoted obligations of `HB1` and `HB2` and from the classifications of `HB3`, the
separable jobs a later round would have to build, **each item derived from a quotation and each
marked with what the record says about whether it is begun**. The expected shape, to be checked and
not assumed, is an ordering in which the curvature re-founding stands before every Bell-edge job,
because the `ROADMAP` paragraph and `[Substratum]` line `170` both place it there.

**Three standing restrictions on this target.**

1. **It is a census of absences, not a plan.** No item is asserted to be sufficient, and the list as
   a whole is not asserted to be complete in the sense that building every item would establish
   H-Bell. The record does not say that, and neither does this round.
2. **No item is scored as easy, hard, tractable or blocked.** Where the record grades an item, the
   grade is quoted with its coordinate and attributed; where it does not, the item carries no grade.
3. **No item is begun.** Naming a job is not starting it, and the definition budget is zero.

### `HB6` — the row's label against the queue's vocabulary

Determine which entry of `VOCAB`, read literally, is true of `ROW` given `HB1`–`HB5`. Run **all
seven entries** and record for each whether it is a candidate, so that the determination is a menu
applied and not a pair compared.

- **`HB6-open`** — `OPEN`'s stated meaning, "A named obligation not closed at the required scope: no
  closing construction or theorem, and no impossibility theorem. It does **not** mean untouched", is
  true of the row.
- **`HB6-other`** — some other entry of `VOCAB` is true of it, identified and carried by quotation.
  **An outcome that would require the row to leave the queue is out of scope for this round** and is
  recorded as a recommendation to the owner rather than written, since departure belongs to
  `DERIVED` and no target here could carry it.
- **`HB6-UNDECIDED`** — the record does not settle which entry applies, with the obstruction named
  and quoted.

**Whatever this target returns, the row's label is written only where `HB6-open` is reached**, in
which case it is written by leaving it byte-identical. Under `HB6-other` and `HB6-UNDECIDED` the row
is left exactly as the base carries it and the finding is recorded in the result note and in the
appended `ROADMAP` paragraph.

## The preregistered predictions, with signs, strengths and recorded reasons

Recorded before execution, with reasons, so that the outcome can be compared against them.

| target | prediction | sign | strength expected | recorded reason |
| --- | --- | --- | --- | --- |
| `HB0` | every passage located at its coordinate | positive | full | every one was located while drafting this freeze, at the blobs the start-state table pins |
| `HB1-m` | the three conjuncts (i)–(iii) are located and quotable as three items | positive | full | `[Substratum]` 132 enumerates them in one sentence with explicit numerals |
| `HB1-q` | the two conjuncts are located and quotable as two items | positive | full | the `ROADMAP` section states them with an explicit **and** |
| `HB1` third item | the two enumerations are **not** the same list, the difference being conjunct (i) | positive | **medium** | the difference is visible in the two quotations, but whether it is content or compression is a judgement about two passages and the record may not settle it |
| `HB2` | `UPSTREAM` is stated on the record and stated as unmet | positive | high | three coordinates state it, two of them in the manuscripts' own voice |
| `HB2` search `S-curv` | **the record carries no formal object bearing on the curvature re-founding** | positive, as a recorded absence | high | no module name in the pinned `OIBridge` tree names curvature, Ricci or a graph metric, and the one hit expected is a hydrodynamics source audit whose subject is a stress closure; a passage found in a probe or a programme note would move it |
| `HB3` | every ingredient classifies, with rows 1–3 and 5–8 expected `WORDS` or `ABSENT`, rows 4, 9 and 11 expected `KERNEL` at a stated scope, and row 10 expected `WORDS` | positive | **medium** on the classification of rows 4 and 9, high elsewhere | the composite and locality material in the kernel is about operational theories on finite carriers, and whether any of it is the ingredient H-Bell's statement quantifies over is exactly the judgement the census must return rather than assume |
| `HB4` | **`HB4-silent`** | positive | **medium** | `[Substratum]` 130–132 and `[Main]` 394 state H-Bell over graphs, curvature and no-signaling and name no readback predicate; but `[Substratum]` 126–128 places the C-conditions in the same stage, so a passage connecting them is possible and is what the target must look for. `HB4-named` is the live alternative and `HB4-UNDECIDED` the live fallback |
| `HB5` | an enumeration is produced, with the curvature re-founding ordered before every Bell-edge job, and with no item recorded as begun | positive | **medium** | the ordering is stated at two coordinates, but which jobs are separable is a judgement about quoted obligations and the freeze declines to fix the count in advance |
| `HB6` | **`HB6-open`** | positive | high | the row carries `OPEN` at the base, `VOCAB`'s entry for `OPEN` names exactly a named obligation with no closing construction and no impossibility theorem, and nothing this round does could close or refute one |

**`HB4` and the `HB1` third item are deliberately held at medium.** They are the two determinations
whose answers this freeze does not have, and a freeze that predicted either at high would be
claiming an answer it is chartered to find. **`HB3`'s rows 4 and 9 are held at medium** for the
reason recorded in the table.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, and the prediction is not amended. **A negative is permitted anywhere**, and is
earned only by a quotation or by a named and bounded search — never by a failed look.

## The STATUS RULE, FROZEN

1. **Every target admits `UNDECIDED` as a live preregistered outcome, and `UNDECIDED` is not a
   failure.** It is recorded with the obstruction named and quoted, and it is reported in the same
   register as a positive. A round that cannot settle a question about the record has determined
   something about the record.
2. **No target of this round may be satisfied by an argument.** Evidence is a quotation with a
   coordinate, or a recorded absence on a named and bounded search over a pinned tree.
3. **The row's label is not moved.** `ROW` carries `OPEN` at the base and carries `OPEN` on this
   round's head. The five cells are byte-identical under every outcome.
4. **Nothing is preregistered, attempted or reported that would amount to Bell-inclusive closure,
   full-substratum uniqueness, the discharge of any conjunct of H-Bell, or the curvature
   re-founding.** An execution that finds itself drafting such a sentence is recording a discrepancy,
   not exercising a permission.
5. **The two enumerations of `OBLIGATION` are written as two things** and are never merged into one
   list. A result note that presents a single merged enumeration is a defect of the execution.
6. **`UPSTREAM` is written as an unmet obligation standing before H-Bell**, at every place H-Bell's
   status is characterized, and never as a remark.
7. **The two readings are written as two predicates.** THE READBACK CLAUSE governs every mention.

   > **THE READBACK CLAUSE, carried at this mention — the status rule's clause on the two predicates.** `RoutedReadback` is physical C4 round 1's predicate and `RoutedReadbackAtStorage` is round 2's. `RoutedReadback` conditions the **initial hidden seed**; `RoutedReadbackAtStorage` conditions the **hidden state at the storage time**. Round 2 established that **neither implies the other**, by two exhibited carriers with exact certificates: neither is stronger, neither is weaker, and no ordering of them is asserted. **Neither is the correct reading of C4** — round 2's bounded search found the manuscripts silent on which random variable the realization clause's record is at the storage surface, and the silence is the finding. **"The C4 reading" therefore names no single predicate.** Any determination of this round that consumes a readback predicate names which of the two it consumes, at the point of consumption; a sentence that consumes "the C4 reading", or that reads a statement about one predicate as a statement about the other, is a **defect of this round** and is checked for in the final report.

8. **No seal constant, merge constant or base constant is touched**, and none is created. An outcome
   requiring otherwise is out of scope and is recorded as such.
9. **No merged result note, preregistration or audit is edited**, and no existing `README` round
   record is edited. Those are statements about their own rounds and stay true.
10. **No manuscript is edited.** `papers/` and `book/` are read and never written. Where this round
    finds a manuscript passage it judges imprecise, it **records the finding and does not act on
    it**, and the repair is a separate publication-record task with its own control plane.
11. **No `ROADMAP` row, section or research status other than the `P1 — H-Bell` section is
    touched**, and that section is touched only by appending the frozen paragraph for the case
    reached.
12. **The definition budget is zero and is not spent.** Naming a formal object that a later round
    would build is permitted; building one is not.

## The frozen post-round sentences, one per outcome

Exactly one sentence per target is written, verbatim, in the result note, and the `ROADMAP`
paragraph for the case reached is written once.

### `HB0` sentences

**Located:**

> Every governing passage the freeze records is present at the execution base at its recorded
> coordinate, and is quoted in this note with that coordinate.

**Moved or altered:**

> A governing passage the freeze records is present at a different coordinate, or its text differs
> at the base; the discrepancy is recorded here and the freeze is not repaired.

**`HB0-UNDECIDED`:**

> Whether a governing passage the freeze records is the passage the freeze names cannot be settled
> by quotation, and the obstruction is named and quoted here.

### `HB1` sentences

**Both enumerations located, and they are not the same list:**

> What H-Bell would require is stated twice on the record and the two statements are not the same
> list: the manuscripts enumerate three conjuncts — ontic parameter dependence, operational
> no-signaling, and a metric/Ollivier–Ricci stability condition — while the queue enumerates two, and
> the difference is the parameter-dependence conjunct. Both enumerations are reported here in full,
> separately, and neither is rewritten into the other.

**Both enumerations located, and they are the same list:**

> What H-Bell would require is stated twice on the record and the two statements carry the same
> conjuncts, the queue compressing into its second conjunct what the manuscripts state as their
> first and third. Both enumerations are reported here in full, separately, and neither is rewritten
> into the other.

**`HB1-UNDECIDED`:**

> Whether the manuscripts' enumeration of what H-Bell would require and the queue's are the same list
> is UNDECIDED: the two are quoted here in full and separately, the candidate difference is named,
> and no passage settles whether it is a difference of content or of compression.

### `HB2` sentences

**Stated and unmet, and the record carries nothing toward it:**

> The curvature re-founding is stated on the record at three coordinates and is stated as unmet: the
> intrinsic hop metric of the degree-6 cubic reference graph is exactly `ℓ¹` with a scale-independent
> `√2` diagonal stretch, so the hop-metric curvature route fails for the reference family before any
> Bell edge is added, and the functional has to be re-founded on the propagation/Laplacian geometry.
> On the bounded search recorded here, over the pinned trees, the merged record carries no formal
> object and no landed round bearing on that re-founding. The finding is the silence: it says nothing
> about whether the re-founding is available, and this round does not begin it.

**Stated and unmet, and the record carries something toward it:**

> The curvature re-founding is stated on the record at three coordinates and is stated as unmet, and
> the bounded search recorded here locates material bearing on it, quoted with its coordinate and
> reported at its own scope. Nothing here discharges the re-founding, extends what the located
> material establishes, or says that the located material suffices.

**`HB2-UNDECIDED`:**

> Whether the merged record carries anything bearing on the curvature re-founding is UNDECIDED on the
> search recorded here, with the obstruction named and quoted; the re-founding itself is stated on
> the record as unmet, and this round does not begin it.

### `HB3` sentences

**Every ingredient classified:**

> Each named ingredient of H-Bell is classified against the pinned trees as present in the kernel at
> a stated scope, present in the manuscripts in words only, or absent on the bounded search recorded
> here. A kernel classification records that an object exists at a stated scope and says nothing
> about whether the conjunct it belongs to holds of the physical substratum. The two readback
> predicates are classified as two objects with two scopes.

**`HB3-UNDECIDED` on one or more ingredients:**

> One or more named ingredients of H-Bell cannot be classified by quotation or by the bounded search
> recorded here; each is reported UNDECIDED with its obstruction named and quoted, and no
> classification is supplied on the record's behalf.

### `HB4` sentences

**`HB4-named`:**

> The record makes H-Bell consume a readback predicate of the physical C4 programme and names which
> reading, quoted here with its coordinate. The two readings remain two predicates: neither implies
> the other, neither is stronger, and neither is the correct reading of the realization clause on
> this evidence. Naming the reading the record consumes settles what the record says and settles
> nothing about the relation between the predicates.

**`HB4-silent`:**

> The record does not make H-Bell consume a readback predicate of the physical C4 programme, on the
> bounded search recorded here; the finding is the silence, and no consumption is supplied on the
> record's behalf. The two readings remain two predicates: neither implies the other, neither is
> stronger, and neither is the correct reading of the realization clause.

**`HB4-UNDECIDED`:**

> The record connects H-Bell to the physical C4 programme without naming which reading of the store
> clause is meant, so which predicate would be consumed is UNDECIDED, with the obstruction named and
> quoted. No reading is supplied on the record's behalf, neither implies the other, and neither is
> the correct reading of the realization clause.

### `HB5` sentences

**An enumeration produced:**

> What a later round would have to build is enumerated here from quoted obligations, each item with
> its coordinate and with what the record says about whether it is begun; the curvature re-founding
> stands before every Bell-edge item, at the two coordinates that place it there. The list is a
> census of what the record says is absent. No item is asserted sufficient, the list is not asserted
> complete, no item is graded, and no item is begun.

**`HB5-UNDECIDED`:**

> What a later round would have to build cannot be enumerated from the record as separable jobs, with
> the obstruction named and quoted; the obligations located by `HB1` and `HB2` are reported as they
> stand and nothing is assembled from them.

### `HB6` sentences

**`HB6-open`:**

> The row `P1 — H-Bell — composite and Bell closure` carries `OPEN`, and `OPEN` is the label the
> queue's vocabulary supports read literally: a named obligation not closed at the required scope,
> with no closing construction or theorem and no impossibility theorem, and not untouched. The row is
> byte-identical at this head. Nothing here closes H-Bell, discharges a conjunct of it, establishes
> Bell-inclusive completion or full-substratum uniqueness, or meets the curvature obligation standing
> before it.

**`HB6-other`:**

> Read literally, the queue's vocabulary supports an entry other than `OPEN` for the row, identified
> and carried by quotation here. The row is left exactly as the base carries it and the finding is
> recorded as a recommendation to the owner, a label change being outside this round's scope.

**`HB6-UNDECIDED`:**

> Which entry of the queue's vocabulary the record supports for the row is UNDECIDED, with the
> obstruction named and quoted. The row keeps `OPEN` and stays in the queue byte-identical.

### The frozen `ROADMAP` paragraph, per case

Appended inside the existing section `P1 — H-Bell and composite closure`, after its existing
paragraphs and before its link line. Exactly one is written.

**If `HB6-open` with `HB4-silent`:**

> Round HB-1 is a record round and recorded the shape of this obligation without entering it. What
> H-Bell would require is stated twice — three conjuncts in `[Substratum §3.3]`, two in this section —
> and both statements are reported in the round's note, separately. The curvature re-founding stated
> above stands before every Bell-edge job, and on the round's bounded search the merged record
> carries nothing toward it. The round makes no claim that H-Bell holds or fails, adds no formal
> object, and leaves this row `OPEN` with its five cells byte-identical. The record does not make
> H-Bell consume a readback predicate of the physical C4 programme; the two readings of the store
> clause are incomparable as predicates and neither is the correct reading of the realization clause.

**If `HB6-open` with `HB4-named`:**

> Round HB-1 is a record round and recorded the shape of this obligation without entering it. What
> H-Bell would require is stated twice — three conjuncts in `[Substratum §3.3]`, two in this section —
> and both statements are reported in the round's note, separately. The curvature re-founding stated
> above stands before every Bell-edge job, and the round's note records what the merged record
> carries toward it. The round makes no claim that H-Bell holds or fails, adds no formal object, and
> leaves this row `OPEN` with its five cells byte-identical. Where the record makes H-Bell consume a
> readback predicate of the physical C4 programme it names which reading, quoted in the note; the two
> readings are incomparable as predicates and neither is the correct reading of the realization
> clause.

**If `HB6-open` with `HB4-UNDECIDED`:**

> Round HB-1 is a record round and recorded the shape of this obligation without entering it. What
> H-Bell would require is stated twice — three conjuncts in `[Substratum §3.3]`, two in this section —
> and both statements are reported in the round's note, separately. The curvature re-founding stated
> above stands before every Bell-edge job. The round makes no claim that H-Bell holds or fails, adds
> no formal object, and leaves this row `OPEN` with its five cells byte-identical. Which reading of
> the store clause the record would have H-Bell consume is UNDECIDED and is left so; the two readings
> are incomparable as predicates and neither is the correct reading of the realization clause.

**If `HB6-other` or `HB6-UNDECIDED`:**

> Round HB-1 is a record round and recorded the shape of this obligation without entering it, and
> returned a finding about this row's label that the round's own scope does not let it write: the
> note carries it as a recommendation to the owner, with its quotation. The row is left `OPEN` and
> byte-identical. The curvature re-founding stated above stands before every Bell-edge job, and the
> round makes no claim that H-Bell holds or fails and adds no formal object.

## What no outcome of this round licenses

- **Nothing that says H-Bell holds, fails, is closed, or is closer to being closed.** The round
  records the shape of an obligation. A census of an obligation adds no theorem and removes none.
- **Nothing about Bell-inclusive completion or full-substratum uniqueness, in either direction.**
  `[Substratum]` Theorem 23's closing sentence — that the theorem does not establish uniqueness of
  the Bell-inclusive full completion — stands exactly as the manuscripts carry it, and no outcome of
  this round strengthens or weakens it.
- **Nothing about the curvature re-founding.** A recorded absence is a statement about the pinned
  trees. It is not a claim that the re-founding is impossible, not a claim that it is available, not
  a specification of what would meet it, and not a step toward performing it.
- **Nothing that orders the two readback predicates, or names either the correct reading of the
  realization clause.** Round 2's certificates and its recorded silence of the manuscripts stand as
  merged, and are consumed here and not reopened.
- **Nothing about the physical C4 row, in either direction.** Round 1's and round 2's theorems are
  true of their own predicates, stay merged, and are neither revised nor promoted; their row's
  residual is untouched.
- **Nothing that identifies the kernel's composite and locality material with the ingredient
  H-Bell's statement quantifies over**, unless `HB3` establishes that identification by quotation
  and reports its scope. A `KERNEL` classification at a stated scope is not that identification.
- **No claim about the reference graph's Bell content.** `[Main]` line 394's corollary is consumed
  as the manuscripts state it, at their scope, and is neither extended nor narrowed.
- **Nothing about the sparse-neighborhood diagnostic being a convergence theorem.** `[SM]` line 148
  states in its own voice that it is not one, and that statement is carried wherever the diagnostic
  is mentioned.
- **Nothing about the cubic isotropy result bearing on the hop-metric obstruction.** One is about a
  Fourier symbol's quadratic and quartic structure; the other about an intrinsic graph metric.
- **Nothing about Track B, `P0`, A6, Lemma 24.1, H-link, H-state, hydrodynamics or the substratum's
  ensemble**, in either direction.
- **Nothing about accessibility, no horizon called accessible, and no clock attached to anything.**
- **No manuscript claim change**, and no `ROADMAP` row moved, relabelled or reworded.
- **No archive seal re-pinned, and no archive pin created.** See the chronology control.

## Named hazards

1. **The round widening into an attempt at Bell closure.** This is the failure mode of this round
   and it is named first. The pressure is structural: a census of an obligation reads, at every
   item, like the first half of a discharge of it, and an execution that has just enumerated what a
   later round would build is one sentence away from building the easiest item. **It would be a
   defect, not an achievement.** The definition budget is zero, status rule clause 4 forbids the
   sentence, `HB5`'s three standing restrictions forbid the list becoming a plan, and the final
   report checks for it explicitly. The tell to look for: any sentence in which a located ingredient
   is said to *give*, *supply*, *establish* or *nearly establish* a conjunct of H-Bell, rather than
   to exist at a stated scope.
2. **Conflating the two readings of the store clause, or ordering them.** The second named hazard.
   The correction landed recently and the familiar phrase "the C4 reading" survives it while naming
   nothing; the tempting error is to write a census row for "the readback predicate" and let one
   predicate's scope stand for both.

   > **THE READBACK CLAUSE, carried at this mention — the hazard of conflating the two readings.** `RoutedReadback` is physical C4 round 1's predicate and `RoutedReadbackAtStorage` is round 2's. `RoutedReadback` conditions the **initial hidden seed**; `RoutedReadbackAtStorage` conditions the **hidden state at the storage time**. Round 2 established that **neither implies the other**, by two exhibited carriers with exact certificates: neither is stronger, neither is weaker, and no ordering of them is asserted. **Neither is the correct reading of C4** — round 2's bounded search found the manuscripts silent on which random variable the realization clause's record is at the storage surface, and the silence is the finding. **"The C4 reading" therefore names no single predicate.** Any determination of this round that consumes a readback predicate names which of the two it consumes, at the point of consumption; a sentence that consumes "the C4 reading", or that reads a statement about one predicate as a statement about the other, is a **defect of this round** and is checked for in the final report.

3. **Reconstructive inference filling a silence.** The round's most likely soft failure: the record
   is silent on a point, the silence is inconvenient for a tidy census row, and a sentence of the
   form "the record must mean X" fills it. Forbidden as a finding by the evidence rule; permitted
   only in a labelled analysis paragraph that says no target rests on it.
4. **A recorded absence read as a negative result.** That no kernel object bears on the curvature
   re-founding is a fact about a pinned tree. Written carelessly it reads as "the re-founding cannot
   be done", which no evidence here supports. Every recorded absence is written with its search and
   with its scope.
5. **The two enumerations merged.** `HB1` exists because `OBLIGATION` is stated twice and the two
   statements may not be the same list. Merging them produces a list no coordinate carries, and the
   candidate difference — the parameter-dependence conjunct — is exactly what would vanish.
6. **The sparse-neighborhood diagnostic mistaken for the convergence theorem.** `[SM]` line 148's
   own disclaimer is the guard, and it is quoted wherever the diagnostic is mentioned.
7. **The isotropy of the leading dispersion mistaken for the curvature route being intact.**
   `[Substratum]` line 170 states both facts in one sentence — the dispersion is isotropic, the
   hop-metric route fails — and a census row that carries the first without the second inverts the
   paragraph's content.
8. **A builder reading the diff rather than the freeze and concluding this round owes an archive
   pin.** The diff may touch `verification/lean/edge_rigidity_probe.py`, the file that carries every
   sealed head, so a landing built by inspecting which files moved would add a `P` commit that pins
   nothing. **The shape is named by this freeze and not by the diff**: the round owns a content
   contract and no seal state, and its landing is `E` → `L`.
9. **A sibling result present at the base read as an input.** Governed by the anti-contamination
   invariant above; the hazard is recorded here so that the invariant is checked rather than
   assumed.
10. **`HB5`'s enumeration read as a specification.** Naming the jobs a later round would have to
    build is not specifying them, and a later round's control plane owes its own targets. An item of
    `HB5` is a located absence with a coordinate, not a design.
11. **The round's own artifacts narrating the correction rather than consuming it.** The physical C4
    round 2 result is consumed at its blob, as a merged result, by quotation. This round's artifacts
    state what the two predicates are and what the certificates establish; they do not narrate how
    the record came to say it.

## Definition budget

**ZERO.** No Lean module, no definition, no theorem, no probe function. The round writes prose, an
appended `ROADMAP` paragraph, an appended `README` paragraph, and the `R7-HBS` content clause,
which declares no seal constant and performs no ancestry check.

**No slot is reserved, because none would be spendable.** If the census uncovers a precise formal
subclaim worth separating, the execution **names it and does not build it**, and it becomes a
candidate for a later round with its own control plane and its own budget. Naming a candidate is an
`HB5` item; building one is a discrepancy.

## Evidence level

**Type P throughout.** No target is at evidence level 2, there is no axiom table, and there is no
`#print axioms` line, because no Lean is written. The result note says so in terms rather than
leaving the absence to be inferred. **No `sorry`, no `axiom`, no `native_decide`** appears anywhere,
which is trivially true of a round that writes no Lean and is recorded so that it is checked rather
than assumed.

**`python3 verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS PASS`** at this freeze's
base and must print it again on the execution head and on the landing.

## The chronology control

Phrased so that each clause is checkable mechanically.

1. **This preregistration is merged alone**, before any execution object exists. Once merged it is
   **immutable**; an execution that diverges records the discrepancy rather than repairing it.
2. **The mandated execution base is the merge commit of this control plane's pull request.** The
   execution branches from exactly that commit and from nothing else, and its first act is
   `git hash-object` on this file at that base, compared against the blob this control plane merges
   as, before any target is executed.
3. **The base of this control plane is `b78eac870ba3ee9ef9e98659ac933bf97dc62226`**, and every blob
   and tree in the start-state tables is the blob or tree at that commit.
4. **No new guard file is added and no ancestry guard is written.** The definition budget is zero
   and no Lean module is written, so there is no kernel object for an ancestry guard to order. The
   `R7-HBS` tag carries content contracts only.
5. **No seal state is created or altered.** Every `_*_BASE`, `_*_SEALED_HEAD` and `_*_MERGE` in
   `verification/lean/edge_rigidity_probe.py` is read and never written.
6. **Because the round is non-sealing, its landing under `§A.37` is the merge alone**: current green
   `main` as first parent, the exact-head-certified execution head `E` as second, and **no
   archive-pin commit**. The execution commit is never modified; conflicts are resolved in the
   landing merge `L` and never in `E`.
7. **The `ROADMAP` is shared ground**, and sibling rounds may move rows and sections in the same
   file between this freeze and this landing. The landing resolves such collisions **by merits per
   `§A.37`** — this round's own appended paragraph from the execution, every other row and section
   from `main` — and afterwards the landing is verified to add exactly the execution's own diff
   against its own base and nothing else, by comparing the two diffs and accounting for every
   difference. A clean automatic merge is not treated as evidence of a correct one.
8. **The certification of record is the run whose `head_sha` is `E`**, and not whichever run happens
   to be latest on the branch.
9. **A transient red from an archive clause that entered `main` after the base does not invalidate
   an exact-head certification**, per `§A.37`, and is not cured by merging `main` into the
   execution. For this non-sealing round, `L` is the end of it: there is no check of its own to
   switch to archive mode.
10. **Full continuous integration passes again on `L`** before the pull request merges, and the
    resulting `main` build is green before the next round's landing is constructed.

### What must have merged before the execution begins, checkable mechanically

At the mandated execution base:

- `verification/programmes/physical-realization/round-c4-2-storage-readback/result.md` is present
  with blob `db94942843bd806df3c5e6ba80b77b9445488d4e`;
- `verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md` is present
  with blob `64a610859e834663cf1d5cc73d0ab9a2ab9dd882`;
- `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean` is present with blob
  `8bdf3c77acf51f074c4f05dc440e3511137cdf9c` and contains the declaration
  `RoutedReadbackAtStorage`;
- `verification/lean-mathlib/OIBridge/PhysicalC4Discharge.lean` is present with blob
  `832eeac3ee5f8df770b478b272842729183c7e48` and contains the declaration `RoutedReadback`;
- `verification/ROADMAP.md` contains the row line quoted in *The queue row and its section*,
  character for character, and the harder-obligation paragraph quoted in *What this round is not*,
  character for character;
- `AGENTS.md` contains the heading `## §A.37 Round lifecycle: control plane, then execution and landing`
  and both numbered clauses of its landing-shape split.

A failure of any of these is recorded as a discrepancy and the execution does not repair the freeze.

## Non-doings

No Lean. No definition. No theorem. No probe. No new guard file. No ancestry guard. No archive pin.
No seal constant touched or created. No manuscript edit. No census anchor. No merged result note,
preregistration or audit edited. No existing `README` round record edited. No `PROGRAMME.md` edit.
No `ROADMAP` row moved, relabelled or reworded, and no section other than `P1 — H-Bell and composite
closure` touched. No Bell-inclusive closure attempted. No full-substratum uniqueness attempted. No
conjunct of H-Bell discharged. No curvature functional defined, re-founded or specified. No ordering
of the two readback predicates asserted. No reading named the correct reading of the realization
clause. No distinction drawn on the record's behalf, and no object of this round's own.

## Execution discipline

The execution produces **the result note**, the appended `ROADMAP` paragraph, the appended `README`
paragraph, and the `R7-HBS` content clause, and nothing else. One pull
request from the mandated base carrying the execution; after certification the same pull request
carries the landing merge `L`, and no pin commit.

## Allowed final report

Every target with its outcome, evidence type, strength and the quotation or bounded search carrying
it; the two enumerations of `OBLIGATION` reported separately; the `HB3` census as a table with the
two readback predicates on two rows; the three bounded searches recorded in full, term by term, each
naming the tree it ran over; the single frozen post-round sentence per target; the single frozen
`ROADMAP` paragraph; the discrepancy section; an explicit statement that the round is type P with no
axiom table and no Lean; an explicit statement that the round is **non-sealing**, that no seal
constant was touched or created, and that the landing is `E` → `L` with no pin; an explicit
statement that no target attempted Bell-inclusive closure, full-substratum uniqueness, the discharge
of an H-Bell conjunct or the curvature re-founding; and an explicit statement that every mention of
the two readback predicates carries THE READBACK CLAUSE or is one of the two kinds of mention the
clause's own section governs. Nothing else.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **`OBLIGATION` is treated as stated twice rather than once.** A different reading would treat the
   `ROADMAP` section as a summary of `[Substratum §3.3]` and quote only the manuscripts. This freeze
   does not, because the queue's own text is what the row is adjudicated against, and because a
   summary that has dropped a conjunct is exactly the kind of drift a census exists to surface.
2. **The census classifies ingredients, not conjuncts.** An alternative would ask, per conjunct of
   `HB1-m`, what exists toward it. This freeze asks per ingredient, because a per-conjunct census
   invites the reader to score conjuncts as partly discharged, which is the widening hazard in its
   most plausible form.
3. **`HB4` asks whether the obligation consumes a readback predicate at all**, rather than assuming
   it does and asking which. The freeze expects silence and records the expectation as a medium
   prediction rather than as a premise.
4. **The curvature re-founding is an object of the census and never a target.** An alternative would
   preregister a bounded formal question about it — a definition of a Laplacian-geometry curvature
   functional, say, with no convergence claim. This freeze does not, because the definition budget
   is zero and because a round that defines the object is a round that has begun the re-founding
   under another name.
5. **The round is non-sealing and the guard clause is content-only.** An alternative would give the
   round its own guard tag with an ancestry seal, which would make it sealing and require `P`. This
   freeze does not, because there is no kernel object to order and because taking a seal would be
   taking ownership of state the round has no use for.

## Settled by the owner before this freeze merges

**Naming is load-bearing**: the execution guard pins this preregistration by path plus blob, so a
rename after this merges breaks the pin and cannot be repaired without a new control plane. Each
decision below is settled, and the freeze carries it.

1. **The directory and the round's name stand as written** —
   `verification/programmes/oi-qm/h-bell/round-hb-1-obligation-shape/preregistration.md`, with
   `h-bell/` a third track directory beside `track-b/` and `track-i/`, on the ground that the row's
   track cell reads `OI→QM / Bell`.
2. **The round's label in prose is `HB-1`**, and the targets are `HB0`–`HB6`.
3. **The execution writes the `R7-HBS` clause, and that clause is content contracts only** — no
   `_HBS_BASE`, no `_HBS_SEALED_HEAD`, no `_HBS_MERGE`, and no ancestry check. `R7-HBS` collides
   with no tag present in `verification/lean/edge_rigidity_probe.py` at the base. The landing shape
   is `E` → `L`, which the clause does not touch.
4. **The `README` round record is appended by this execution**, one paragraph, with no existing
   paragraph edited.
5. **`HB6` stands in this round.** Adjudicating the row's label against `VOCAB` is cheap and type P,
   and it authorizes no change to the row: the status rule's clause 3 keeps the row byte-identical
   whatever `HB6` returns.
6. **`HB3` row 9 stays a bounded census.** The freeze pins six candidate modules by blob in the
   start-state table and leaves the identification of which of them, if any, is the ingredient
   H-Bell quantifies over to the census under search `S-inputs`. Naming the composite and the
   operational-lifting modules individually in the freeze would answer part of that census in the
   freeze, which is why that row's prediction is held at medium.
