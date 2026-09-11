# Track B act 8 — the continuous-extension round: preregistration

Frozen before any execution. Blob identity is authoritative.

Source identities per act 1's frozen table: **A** = *The Stochastic-Quantum Correspondence*,
arXiv:2302.10778v3; **B** = arXiv:2507.21192v1; **C** = *The Stochastic-Quantum Theorem*,
arXiv:2309.03085v2. **Only Source A is adjudicated in this round.** Every coordinate is read off act
5's **authoritative surface**: the PDF of arXiv:2302.10778v3, which self-identifies by its p. 1 stamp
`arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`. The arXiv HTML rendering numbers differently and is
**not** an admissible surface.

Executed from `main` at `e0c0c709620db0d114dbd7061975b6747cb7aabc`, the merge of act 7 layer 1
(PR #574). Act 7's own freeze is commit `06ea197f02e736dbeb4247c0ecd0f57f9b381a73`, blob
`810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19`; it is **cited and not reopened**.

## The question

Act 7 layer 1 closed at **`DC2a`**: Source A's §3.4 dilation runs on an inherited contract — the
continuity condition of p. 4, that `Γ(t ← t₀)` approaches `Γ(t₀ ← t₀) = 𝟙` in the limit `t → t₀` —
which act 6's `ℕ`-indexed off-direct witness does not instantiate. The round stopped there rather
than narrowing the contract after reading the source.

That stop names its own repair, and this round is exactly that repair and nothing more:

> **Construct a Source-A-admissible CONTINUOUS EXTENSION of a lawful off-direct OI/`PPer` witness —
> with its discrete restriction identified and off-directness preserved — or prove that no such
> extension exists under the OI constraints.**

### The first mathematical question, asked sharply and asked first

    ┌──────────────────────────────────────────────────────────────────────────────┐
    │  E0.  Can a periodic finite-state OI visible family be embedded into a        │
    │       continuous stochastic family  Γ̂  with                                  │
    │                                                                              │
    │            Γ̂(n) = Γ_n ,     Γ̂(0) = 𝟙 ,     Γ̂(t) → 𝟙  as  t → 0 ,           │
    │                                                                              │
    │       while retaining a non-unistochastic slice at the location the           │
    │       off-direct branch requires?                                            │
    └──────────────────────────────────────────────────────────────────────────────┘

**E0 is asked first because it isolates the obstruction before Stinespring or readback freedom
enters.** Act 7's `DC2a` is a statement about the *time domain and the limit at `t₀`* — nothing
downstream of §3.4 was reached. If the obstruction lives in E0, it lives there independently of every
question act 7 fenced, and the round finds that out before touching a dilation.

**And E0 alone settles nothing — this is the round's first control.** See *The triviality control*
below. A positive answer to E0 is a **screening** result, not a `CE1`.

## Three layers, SEQUENTIAL, and the first is Track I

Act 7's layers were sequential; this round's are too, and there is a further asymmetry: **layer 0 is
a Track I question executed inside a Track B round**, which is the one structural hazard this freeze
must handle before anything else.

| Layer | Track | Evidence level | What it does |
| --- | --- | --- | --- |
| **0** | **Track I** | 2 where kernel-checked, 3 where a definitional choice is recorded | Defines the extension relation itself. Borrows **nothing** from Track B. |
| **1** | **Track B** | 3 — a reading of the accepted text | Transcribes Source A's full admissibility contract **before** any construction is attempted. |
| **2** | **Track B** | 2 — kernel-checked | Constructs the extension, or proves impossibility, against the layer-0 relation and the layer-1 contract. |

### The track-separation control, stated structurally rather than as an intention

*"Neither branch may be used as evidence for the other"* is enforced here by keeping the two
predicates **separate objects**, not by a promise in prose:

1. **Layer 0's extension relation is defined without Source A vocabulary.** Its statement may not
   mention Source A, `Θ`, unistochasticity, dilation, Stinespring, or any Track B label — `BD3`,
   `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2`, `DC2a`. It is a relation between an OI visible
   family and a continuous-time family, and it must be readable, and defensible, with Source A
   absent from the room.
2. **Source-A admissibility is a SECOND and separate predicate** (layer 1, E3), applied *to* an
   extension. The two are never fused into one definition, and no clause migrates from the second
   into the first.
3. **No Track I conclusion in this round is drawn from any Track B finding, and no Track B
   conclusion from any Track I finding.** That Track B *wants* a continuous-time OI class is a
   motive, never evidence; if layer 0 returns `CE3`, that is a Track I finding about OI structure and
   is reported as one, without Source A carrying any of its weight.

**Why this is the hazard.** The extension relation is being defined at the exact moment a Track B
round needs it to come out a particular way. A definition tuned to make a Source-A obligation
succeed would be a Track B result wearing Track I clothing, and it would be invisible afterwards.
Control 1 makes the tuning detectable, because a Source-A-shaped clause cannot be stated in layer 0's
vocabulary at all.

### The stop table

| Layer 0 finding | Layer 1 | Layer 2 | Outcome |
| --- | --- | --- | --- |
| The extension relation **cannot be defined** from current OI structure without an extra principle, and the principle is **named** | **not reached** | **not reached** | `CE3` |
| Relation defined; contract transcribed; a Source-A-admissible extension is **exhibited** and off-directness is preserved at the frozen location | executed | executed | `CE1` |
| Relation defined; contract transcribed; an extension exists but **every** construction tested or derived lands on the direct branch | executed | executed | `CE2` |
| Relation defined; contract transcribed; a theorem proves **no** admissible off-direct extension exists in a stated class | executed | executed | `CE4` |
| Relation defined; contract transcribed; neither a construction nor an impossibility theorem is produced | executed | executed | `CE5` |

*Not reached* and *unresolved* are different statuses and are never interchanged, per act 5's
discipline. Under `CE3` the layer-1 and layer-2 questions are recorded **not reached — the
definitional layer stopped the round**, never *unresolved*.

**`CE3` is not the fallback for a hard afternoon.** It requires an argument that the relation is not
definable from current OI structure, together with the **named** extra principle that would supply
it. A round that simply does not settle on a definition is `CE5`, not `CE3`.

## Why this round is on the critical path

Acts 1–6 put the full-class `OI → QM` route onto Source A's **dilated** branch, by exhibiting one
lawful `PPer` member off the direct unistochastic branch (`UB2`, existential, and cited as
existential). Act 7 then found the dilated branch untestable on that witness, because the witness is
outside §3.4's inherited time-domain contract (`DC2a`).

So the ladder is blocked at a single joint: **there is no object in hand that is simultaneously a
lawful OI visible family, off the direct branch, and inside Source A's stated contract.** Producing
one, or proving none exists, is the whole content of this round. Nothing else in the programme
advances until that joint is resolved.

**What each answer would mean.** `CE1` reopens act 7 at its fenced counterfactual and the `OI → QM`
route resumes, at the reduced strength act 7 already fixed. `CE4` would say the OI class and Source
A's contract are incompatible **on the off-direct branch of the stated class** — a classification
result about the two together, and the strongest outcome available here. `CE2` says the constructions
reached so far all land on the wrong branch, which is informative and is **not** `CE4`. `CE3` relocates
the obligation to Track I. `CE5` retires nothing and says so.

## Layer 0 — the extension relation (Track I)

### E1 — define it, and state what it does and does not require

The definition returns all five of:

- **(a) the time domain** of the continuous family, and whether it is `ℝ`, `ℝ≥0`, an interval, or
  something else — stated as a choice, with the choice recorded;
- **(b) the embedding** of the discrete index into that domain — the map `ℕ →` domain — stated
  explicitly rather than left as "the obvious inclusion";
- **(c) the agreement condition** on the image of that embedding: `Γ̂ ∘ ι = Γ`, in the orientation
  layer 0 fixes;
- **(d) the restriction map** in the other direction — given `Γ̂`, which discrete family is *the*
  restriction — and whether the restriction of an extension of `Γ` is `Γ` on the nose;
- **(e) what is required at non-integer times**, and what is not: stochasticity, continuity,
  differentiability, periodicity, or nothing.

**The restriction must be identified, not assumed.** Act 7's obligation says "with its discrete
restriction identified": `Γ̂` determines its restriction only once (b) and (d) are fixed, and a round
that exhibits a continuous family without naming which discrete family it restricts to has not met
the obligation, however admissible the continuous family is.

**`PPer` is `ℕ`-indexed by definition** — `PPer Γ := Γ 0 = 1 ∧ (∀ t, IsRowStochastic (Γ t)) ∧
PeriodicFamily Γ` — so there is no such thing as a continuous `PPer` family, and the round does not
speak of one. The object sought is a continuous-time family whose restriction under (d) **is** a
lawful `PPer` member.

**Periodicity is asked, not assumed.** `PPer` requires a positive finite period of the discrete
family. Whether the extension is required to be periodic in continuous time, or only to restrict to
a periodic discrete family, is a choice, and E1(e) records which was taken and why.

### E2 — is the extension determined, or chosen?

Record whether OI structure **determines** a unique extension of a given `PPer` family, admits a
**class** of them, or admits **none**. If plural, then every extension this round exhibits is a
**selection**, the round says so in those words, and no result is stated as though the extension were
canonical.

**One merged precedent is on point and is ANALOGY AND CONTROL ONLY.**
`RegionLimit.continuous_extension_not_unique` exhibits two Hermitian generators whose flows are
isometries, agree at every integer time, and differ at `t = 1/2`. It is evidence that continuous time
is additional structure **at the operator level**, which is the level it is stated at.

**It is not evidence about the visible level, and the reason is recorded here so it is not
mis-cited.** Both flows in that theorem have the **same** entrywise modulus-squared at every time —
the identity — so their visible shadows coincide and the theorem exhibits no visible non-uniqueness
whatsoever. If this round cites it for anything, that arithmetic is proved in-round; and it may be
cited only as an analogy for *what kind of thing* a continuous extension is, never as evidence that
visible continuous extensions are non-unique. This is act 7's D5 discipline applied to a different
merged theorem.

### The triviality control — a rooted interpolation is EXPECTED, and is not `CE1`

**Recorded before execution, so a positive E0 cannot be over-read.** The row-stochastic matrices over
a finite carrier form a convex set containing `𝟙`, so continuous paths from `𝟙` to any row-stochastic
matrix exist by convexity alone, and a path that returns to `𝟙` can be concatenated to match a
periodic discrete family at every integer. Nothing about that construction is hard, and this freeze
expects the rooted, continuity-at-`0` form of E0 to come out **positive**.

**Therefore a rooted continuous interpolation, by itself, is NOT a `CE1` and may not be reported as
one.** `CE1` requires the **full** contract E3 returns — every clause of it, including whatever E4
determines about the two-time family and whatever regularity E3 finds — together with off-directness
at the location E5 freezes. The convexity observation is recorded as a control on over-reading; it is
**not proved here**, and the execution proves or refutes it rather than citing this paragraph.

**This is the act-7 lesson carried forward.** Act 7 reached an honest `DC2a` only because its freeze
forbade narrowing the contract to the hypotheses §3.4 restates locally. The corresponding move here
would be to answer the easy rooted question, call it the obligation, and skip the contract. The
control above is written before the source is re-read, against exactly that move.

## Layer 1 — the source contract, transcribed BEFORE construction (Track B)

**Evidence level 3.** Executed **before** any construction is attempted, and its findings are what
layer 2's admissibility predicate is transcribed from.

### E3 — the full admissibility contract for a continuous-time family, with coordinates

Transcribe, with exact equation and page coordinates on the authoritative surface, **every**
hypothesis Source A requires of a continuous-time transition family, including:

- the **time domain** (§2.1 p. 3 and anything stronger elsewhere);
- the **continuity condition** (p. 4, after (5)) — quoted, with its quantifier structure stated: over
  which `t₀`, and in which variable the limit is taken;
- the **root condition** `Γ(t₀ ← t₀) = 𝟙` (p. 4);
- **non-negativity** (2) p. 4 and **normalization over the first index** (3) p. 4, in Source A's
  external **(column) stochastic** orientation;
- any **differentiability or smoothness** required anywhere the construction's outputs are consumed —
  act 7's D3 recorded (33) p. 12 assuming the post-(28) unitary family is "a differentiable function
  of the time `t`", and E3 determines whether an analogue binds `Γ̂` itself, the `Θ` built from it,
  both, or neither;
- whatever the `Θ`/Kraus construction presupposes ((12) p. 6, (13) p. 7, (25)–(26) p. 10);
- anything else the construction actually needs.

**The contract is fixed by E3 and is not narrowed afterwards.** Act 7's frozen clause is carried
forward verbatim and governs here:

> The list is **not** limited to hypotheses §3.4 restates locally. It must include every upstream
> prerequisite the construction actually needs.

**And the symmetric error is forbidden too.** The contract may not be *widened* after seeing that a
construction succeeds. A hypothesis is in E3's list because Source A states or needs it, with a
coordinate — never because including it would change the outcome, in either direction.

### E4 — ROOTED or TWO-TIME? The question most likely to be narrowed silently

Source A's objects are written `Γ(t ← t₀)`: two-time. Act 6's and act 7's witness is rooted — a
one-parameter family `Γ_t`, which in Source A's notation is `Γ(t ← 0)` alone. E0's continuity clause,
`Γ̂(t) → 𝟙` as `t → 0`, is likewise rooted.

**So E4 asks, with coordinates: does Source A's contract require the full two-time family
`Γ̂(t ← t₀)`, or only the rooted `Γ̂(t ← 0)`?** Read the quantifier off p. 4 rather than assuming it.

**If two-time, three consequences are recorded, and none may be skipped.**

1. The extension obligation **includes constructing the two-time family**, not only the rooted one,
   and E0's positive answer covers only the rooted part.
2. **The two-time family is not determined by the rooted one for an indivisible process** — that
   non-composition is the defining feature of the class acts 1 and 2 are about — so the two-time
   family is a **further selection**, and the round says so.
3. The continuity condition then binds at **every** `t₀`, not only at `0`, and off-directness must
   still survive that.

**If rooted, that is the finding, and it is recorded with the coordinate that establishes it.** What
this freeze forbids is settling E4 by convenience, or leaving it unasked and letting E0's rooted form
stand in for the contract.

### E5 — WHERE off-directness must hold: three propositions, not one

The following are **distinct** and the freeze names them separately because they are easy to
conflate and because only a stated conjunction of them discharges the obligation:

| Label | Proposition |
| --- | --- |
| **`O-A`** | The continuous family is **somewhere** non-unistochastic: `∃ t` in the domain with `¬ IsUnistochastic ((Γ̂ t)ᵀ)`. |
| **`O-B`** | The **discrete restriction** is off-direct: `∃ n : ℕ` with `¬ IsUnistochastic ((Γ̂ (ι n))ᵀ)` — the property act 6 proved of its witness. |
| **`O-C`** | The **Source-A object the dilation consumes** is off-direct: the `Θ(t ← 0)` §3.4 takes as input is **not already unitary**, which is what triggers the dilation at all (act 7's D1). |

**These are not automatically equivalent.** `O-B` gives `O-A` only because an integer time is a time;
`O-A` does not give `O-B`, since a continuous family may leave the unistochastic set strictly between
integers and sit inside it at every integer. `O-C` is a statement about a **different object** — the
potential matrix, not the transition matrix — related to the others only through `Γ_ij = |Θ_ij|²`
((12) p. 6) and act 6's structural lemma. **Every entailment among `O-A`, `O-B` and `O-C` that this
round uses is proved in-round; none is assumed, and none is imported from the informal reading
above.**

**The required conjunction, frozen here: `CE1` requires `O-B` AND `O-C`.**

- **`O-B`**, because act 7's obligation says the discrete restriction must "remain the same lawful
  off-direct witness", and because a continuous family whose restriction is on the direct branch has
  extended a different object than the one acts 6 and 7 are about.
- **`O-C`**, because `O-C` is the condition under which §3.4's dilation is invoked at all. An
  extension satisfying `O-B` but not `O-C` would be off-direct in the visible data while the source's
  construction never enters its dilated branch, which does not discharge the obligation act 6
  identified.
- **`O-A` alone is never sufficient**, and a result stating only `O-A` is reported as `O-A` and
  labelled `CE5` or `CE2` as the rest of the record requires — never `CE1`.

### The preservation burden

**"A continuous extension exists" is insufficient.** The extension must carry the off-directness with
it, at the location E5 freezes. Specifically:

1. **The discrete restriction is a lawful `PPer` member** — root identity, row stochasticity at every
   `t`, positive finite period — **proved**, not asserted.
2. **That restriction is off-direct** (`O-B`) — proved, by act 6's route or another proved in-round.
3. **Either** the restriction is act 6's merged witness, **or** it is a different lawful off-direct
   witness **separately frozen in this document or in a merged append-only amendment** before it is
   used. Substituting a witness at execution time, after seeing which one makes the construction
   work, is exactly the move the split-PR protocol exists to prevent.
4. **`O-C` holds** for the object §3.4 consumes.

**A construction meeting 1–4 but failing E3's contract is not a `CE1`**, and a construction meeting
E3's contract but failing any of 1–4 is not a `CE1` either. The two halves are reported separately so
that a partial success is legible as one.

## Layer 2 — construction or impossibility (Track B, kernel)

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, `axiom` or `native_decide`.

### E6 — the fn. 11 negative control, RUN, not assumed

Act 7 recorded the hazard from the source's own text. Footnote 11, p. 12 gives Source A's
discrete-to-continuous interpolation: with `δt` the discrete time step and `Σ` a permutation matrix,
`Γ_ij(n δt + t ← n δt) ≡ |(Σ^{t/δt})_ij|²` "defines a **unistochastic** matrix that analytically
interpolates the original discrete, deterministic process to a smooth, unistochastic process".

**This is a mandatory negative control and it is NOT this round's construction.** The execution:

1. states whether the recipe **applies** to the frozen off-direct witness at all — act 6's odd slice
   `A = ![![1,0],![1,0]]` is rank one and is **not** a permutation matrix, so non-applicability is a
   live and reportable answer, and is itself the finding if that is what holds;
2. if it applies, **runs it** and **exhibits** the resulting family landing on the direct branch,
   rather than asserting that it would;
3. reports the control's outcome **whatever this round's own construction does**, including under
   `CE4` and `CE5`.

**Its purpose is to make a `CE1` falsifiable.** If the source's own interpolation destroys
off-directness and ours does not, the difference between the two is the content of the round and must
be stated explicitly: which clause of E3 ours satisfies that the source's recipe does not, or which
property of the witness ours exploits. A `CE1` that cannot say how it differs from fn. 11 has not
been shown to differ from it.

### E7 — the construction, or the impossibility theorem

**For `CE1`:** exhibit the extension, prove the layer-0 relation holds between it and a lawful `PPer`
witness, prove E3's transcribed admissibility predicate of it, and prove `O-B` and `O-C`. Existential,
one witness, and reported as existential.

**For `CE4`:** a theorem quantified over **all** extensions admissible in a **stated class**, proving
no member is off-direct at the frozen location. The class is named in the statement and the result is
never paraphrased beyond it. **`CE4` is never earned by an unsuccessful search**, and `CE2` and `CE5`
never upgrade to it.

**For `CE2`:** report each construction tested or derived, what it was, and where it landed on the
branch. `CE2` is a record of attempts, and **the quantifier is wrong for an impossibility claim** —
over constructions and over witnesses both.

## No hidden completion shortcut

**A continuous interpolation may not be introduced by appealing to the project's topological
completion machinery without discharging all three of the following, in the result note.**

1. **Name the exact theorem** being invoked — module and result name — rather than gesturing at "the
   completion".
2. **State whether the resulting points are executable/physical, or limiting objects only.** This
   distinction is already load-bearing in the merged corpus and is not introduced here:
   `DiscreteCompletion.lean`'s own header records that "dense availability is never identified with
   exact availability", and the quasilocal completion work (`QuasilocalAlgebra`, `RegionLimit`,
   `QuasilocalCharacterization`) records that it adds "no continuity or continuous-time law". A
   continuous family assembled out of limiting objects is a different claim from one assembled out of
   executable ones, and the result states which it has.
3. **State what the completion theorem actually quantifies over**, and whether the object produced is
   a transition family of the kind E1 defines or something the completion merely approximates.

**Density is not construction.** `DiscreteCompletion`'s `KrausDense`/`DenseFiniteQM` results, and any
`ChanWithin`-style approximation, establish that objects come **within `ε`** of a target. They do not
produce the target, and an `ε`-approximation to an off-direct family need not be off-direct — the
unistochastic set's closedness properties are not settled by anything merged here. **No `CE1` may
rest on a density statement.**

**`RegionLimit.continuous_extension_not_unique` is analogy and control only**, for the reason
recorded at E2: its two flows have identical visible shadows.

## Outcome grid — deliberately ASYMMETRIC

**`CE1` — an admissible off-direct continuous extension EXISTS.** A Source-A-admissible continuous
extension is **exhibited**, its discrete restriction is identified and proved a lawful `PPer` member,
and off-directness is preserved at the frozen location (`O-B` **and** `O-C`). **Existential**: one
witness, one extension. It does **not** say every off-direct `PPer` member has an admissible
continuous extension, and it is never paraphrased that way.

**`CE2` — extension exists, but every construction tested or derived lands on the DIRECT branch.**
Interesting, reported with the full list of what was tried and where each landed, and **explicitly
not an impossibility theorem**. `CE2` may not be paraphrased as "off-direct continuous extensions do
not exist", "the OI class cannot be continuized off the direct branch", or any equivalent. It
upgrades to `CE4` only by a theorem, never by accumulation.

**`CE3` — the extension relation itself cannot be defined from current OI structure without an extra
principle.** Layer 0's stop. Requires an argument **and** the named principle. This identifies a new
**Track I** missing structure and is reported as a Track I finding, with Source A carrying none of
its weight. Layers 1 and 2 recorded *not reached — the definitional layer stopped the round*.

**`CE4` — IMPOSSIBILITY THEOREM.** No admissible off-direct extension exists **in the stated class**,
proved, universally quantified over that class. The strongest outcome available here and the only one
that closes the obligation negatively. Reachable **only** by such a theorem.

**`CE5` — open.** No construction and no impossibility theorem. **`CE5` retires nothing**, is
reported as *unresolved* with what was tried and what would settle it, and may not be paraphrased as
evidence in either direction.

**Failure to prove `CE4` is not `CE1`, and failure to exhibit `CE1` is not `CE4`.** This is act 5's
`A1` discipline, act 6's `TI2`/`UB2` discipline and act 7's `DC3`/`DC4` discipline, stated a fourth
time because it is the error this programme has had to repair at every act where an existential met a
universal.

## The act-7 restart rule

**Only `CE1` reopens act 7.** On `CE1`, and only then, act 7 resumes at exactly the branch its layer-1
result fenced: **`D4a` positive / `D4b` negative**, which routes to the **readback-amendment path** at
**reduced strength** under act 7's frozen stop table — meaning layer 2 pauses for a merged append-only
amendment fixing the readback map before any layer-2 formalization or witness calculation.

**Nothing in this round promotes that counterfactual to an act 7 result.** Act 7's own note records
`D4a`/`D4b` as **not reached**, with the counterfactual reading explicitly non-outcome-bearing. This
round may **cite** that reading as the position act 7 would resume from; it may not report it as a
finding, restate it without its conditional, or treat `CE1` as having established anything about the
dilation. `CE1` establishes that a testable object exists — not what the test returns.

**Under `CE2`, `CE3`, `CE4` and `CE5`, act 7 stays closed at `DC2a`** and no part of its layer 2 is
run.

## Definition budget

The execution introduces **at most five** top-level definitions, and these are the five:

1. the continuous-time visible family datum (layer 0), if the relation cannot be stated without one;
2. the **extension/restriction relation** itself (layer 0, E1) — the embedding, the agreement
   condition and the restriction map, in whatever form E1 settles on;
3. the **Source-A admissibility predicate for a continuous-time family** (layer 1, E3) — transcribed,
   a separate object from 2, per the track-separation control;
4. the off-directness proposition at the frozen location (`O-B ∧ O-C`), if act 6's `IsUnistochastic`
   does not state it without a new name;
5. the `CE4` impossibility proposition, if reached.

**Witnesses are built inside the proofs that need them**, per act 3's lesson — no top-level witness
definitions. Merged definitions are consumed, never redefined: `PPer`, `PeriodicFamily`,
`IsRowStochastic`, `IsColStochastic`, `IsUnistochastic`, `RootedRealization` and act 6's structural
lemma are cited, not restated. If layer 0's or layer 1's findings require a sixth, that is an
**append-only amendment**, separately frozen and merged before the work it affects; it is not a
licence taken at execution time.

## Mandatory controls

1. **Kernel discipline.** No `sorry`, `axiom`, `native_decide`; `#print axioms` on **every** named
   result, at the tail of each module file; any new module registered in
   `verification/lean-manuscript-census.json` and imported in `OIBridge.lean`.
2. **Layer order is binding.** Layer 0 before layer 1 before layer 2. The extension relation is
   defined before the source is re-read; the contract is transcribed before any construction is
   attempted. A construction found first and a definition fitted to it afterwards is the failure mode
   this ordering exists to prevent.
3. **The extension relation is defined in Track I vocabulary** and mentions no Source A object and no
   Track B label (E1). Source-A admissibility is a **separate** predicate (E3). The two are never
   fused.
4. **No sourcing inference and no cross-track evidence**, in either direction, per Amendment 2. That
   Track B needs this definition is a motive and never evidence.
5. **The contract is transcribed, not invented, and not narrowed OR widened after construction**
   (E3). Act 7's inherited-prerequisites clause governs. Any condition the source leaves implicit is
   reported as a **finding** — a hypothesis the source does not state — and named in the result.
6. **E4 is answered with a coordinate.** Whether the contract is rooted or two-time is read off the
   source, and if two-time, the two-time family is constructed rather than assumed to follow from the
   rooted one.
7. **Off-directness is located, not assumed.** `O-A`, `O-B` and `O-C` are kept distinct; `CE1`
   requires `O-B ∧ O-C`; every entailment among them that is used is proved in-round.
8. **The witness is frozen before it is used.** Act 6's merged witness, or a separately frozen
   alternative — never one substituted at execution time after seeing which one works.
9. **A rooted continuous interpolation is not a `CE1`** (the triviality control). E0's answer is a
   screening result and is reported as one.
10. **The fn. 11 control is RUN and reported**, under every outcome, including non-applicability as a
    live answer; and a `CE1` states how it differs from fn. 11.
11. **No completion shortcut** without naming the exact theorem, stating whether its points are
    executable/physical or limiting objects only, and stating what it quantifies over. **No `CE1`
    rests on a density statement.**
12. **`RegionLimit.continuous_extension_not_unique` is analogy and control only**, never evidence of
    visible non-uniqueness; its visible shadows coincide, and that arithmetic is proved in-round if
    it is cited.
13. **`CE2` may not be paraphrased as impossibility**, and `CE5` may not be paraphrased as evidence
    in either direction.
14. **`CE4` is earned only by a theorem over a stated class**, never by an unsuccessful search;
    `CE3` is earned only with a named principle, never by an unsettled definition.
15. **Only `CE1` reopens act 7**, at `D4a` positive / `D4b` negative, reduced strength, via the
    readback amendment. Act 7's counterfactual is never promoted to a result.
16. **Source coordinates** follow act 1's frozen table and act 5's authoritative surface, and are
    never mixed across sources. Only Source A is adjudicated; Sources B and C are not compared with it
    on any axis.
17. **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2` and `DC2a` are cited and never
    revised.** Acts 1 through 7 are not reopened.
18. **No manuscript edit**, whatever is found.
19. **`UB2` is existential** and is never restated as a classification of the OI class; `CE1` is
    existential and is never restated as a statement about all off-direct members.

## Non-doings

Do not: adopt or propose a candidate-selection principle; run any part of act 7's layer 2; state or
rely on act 7's `D4a`/`D4b` counterfactual as a finding; adjudicate act 5's gauge-versus-empirical
tension; prove or claim anything about interference; decide `F1` versus `F2`; claim Source A is
inapplicable on any outcome; claim the external correspondence fails or succeeds; infer visible
unistochasticity from the existence of any representation; read `UB2` or `CE1` as a classification;
read `CE2` or `CE5` as impossibility; name or adopt `C5`; compare Source A with Source C on any axis;
begin the `BD3` follow-up, Arc D round 2 or Arc E; edit manuscripts.

## Prediction, recorded before executing

**The rooted screening question E0 is expected to come out positive, and that expectation is the
reason for the triviality control.** Convexity of the row-stochastic set makes continuous paths from
`𝟙` cheap, and concatenation makes matching a periodic discrete family at the integers cheap. This
freeze therefore predicts that the round's difficulty is **not** in E0 and records that in advance so
a positive E0 cannot be presented as the result.

**The live uncertainty is E3 and E4 — the contract, and whether it is two-time.** If Source A's
continuity condition binds at every `t₀`, the obligation grows a second construction (the two-time
family) which indivisibility guarantees is not determined by the first, and that is where this freeze
expects the round to become hard. Call the two-time reading roughly even money; it is asked with a
coordinate precisely because the temptation to read it as rooted — E0's own shape — is strong.

**Between the outcomes, the honest prior is tilted toward `CE1` or `CE5`, not toward `CE4`.** An
impossibility theorem would have to rule out every admissible extension in a stated class, and
nothing in the merged corpus currently supplies the tool for that; the fn. 11 hazard is a signpost,
not a proof, and it applies to one recipe that may not even apply to the frozen witness. `CE3` is
possible but is the outcome this freeze considers least likely, since E1's ingredients — a time
domain, an embedding, an agreement condition and a restriction — look statable without a new
principle.

**The prediction is recorded at that strength and no higher.** It is not a finding. `CE1` is earned
only by an exhibited admissible off-direct extension, `CE4` only by a universal theorem, `CE3` only by
a named principle, and if none is produced the answer is `CE5`.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **One amendment is anticipated by name.** If the preservation burden requires a witness other than
  act 6's merged one, that witness is fixed by an append-only amendment — written, reviewed and
  merged — **before** it is used, not chosen at execution time.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`.
- **No execution in the control-plane PR**: no witness search, no construction, no Lean, no probe
  guard, no roadmap edit.
- Final exact-head review after layers 0, 1 and 2, the result note and registry updates are complete.
- No merge without an explicit owner direction after exact-head review, naming the exact head SHA.

## Allowed final report

1. **E0** answered, stated as a **screening** result, with the triviality control applied explicitly;
2. **E1** — the extension relation, with (a)–(e) all returned, stated in Track I vocabulary, and the
   restriction map identified;
3. **E2** — determined or chosen, with every exhibited extension labelled a **selection** if plural,
   and `RegionLimit.continuous_extension_not_unique` used as analogy and control only;
4. **E3** — the transcribed contract with exact coordinates, listing **inherited** prerequisites as
   well as locally restated ones, with any source-implicit condition named as a finding;
5. **E4** — rooted or two-time, with the coordinate, and if two-time, the further selection recorded
   and the second construction either produced or recorded *not produced*;
6. **E5** — `O-A`, `O-B`, `O-C` stated separately, the required conjunction named, and every
   entailment used proved in-round;
7. **the preservation burden**, its four clauses answered individually, with the `PPer` membership and
   off-directness of the restriction **proved**;
8. **E6** — the fn. 11 control, run or reported non-applicable, with its outcome stated under every
   round outcome, and a `CE1` saying how it differs;
9. **E7** — the construction or the impossibility theorem;
10. the outcome — `CE1`, `CE2`, `CE3`, `CE4` or `CE5` — with the route to the label stated;
11. any completion theorem invoked, named exactly, with executable/physical versus limiting-object
    status stated, and confirmation that no `CE1` rests on a density statement;
12. the recorded predictions and whether each held;
13. the definition count and the `#print axioms` line for every named result;
14. what remains open and what would settle it;
15. explicitly: whether act 7 reopens, and under `CE1` that it reopens at `D4a` positive / `D4b`
    negative at **reduced strength** via the readback amendment, with act 7's counterfactual cited and
    not promoted; that `UB2` and `CE1` are existential and are not restated as classifications; that
    `CE2`/`CE5`, if reached, are unresolved and are not impossibility; that no candidate-selection
    principle has been adopted; that `BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2` and
    `DC2a` are unrevised; that no outcome says Source A is inapplicable or that the correspondence
    fails; and that nothing here is a sourcing claim in either track direction.
