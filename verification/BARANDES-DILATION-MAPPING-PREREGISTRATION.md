# Track B act 4 — the dilation mapping obligation: preregistration

Base: `main` at `ce3910e522c41b0d4aea2587044130fe8feef9be` (post-PR #565, act 3 closed at `CU1a`).

Presupposes act 1 (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560), act 2
(`BARANDES-TRANSPOSE-BRIDGE-RESULT.md`, PR #562), the scoping pass
(`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, PR #563) and act 3
(`BARANDES-CANDIDATE-SELECTION-RESULT.md`, PR #565).

**This is a source-to-formal audit round, and the first Track B act that consults a primary source
since act 1.** Acts 2 and 3 forbade it; this one requires it, and the controls below replace that
prohibition with a narrower one rather than dropping it.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no
execution begins before the freeze is merged.**

## Why this round is on the critical path

Act 3 proved that

    OI family  →  QfbData representation  →  candidate

is **not a function at our interface**: two independently admissible extraction rules give different
visible candidates on one lawful representation, with the representation held fixed. So a
candidate-selection principle is required before "OI forces this interference discrepancy" is a
well-defined family-level question.

Act 3 also fixed what may **not** be concluded from that, and this round is the reason the
restriction was written. Act 1 established that the external diagnostic uses a **particular**
candidate whereas our `PDivisible` quantifies existentially. That external construction may supply
the selection canonically from its own dilation. Until that is determined, we cannot tell whether
the missing selection is **already part of the external theorem** or is a genuinely additional
principle on our side — and that is the earliest unresolved dependency in the correspondence chain.

**No candidate-selection principle is adopted on our side in this round.** Doing so would pre-empt
exactly the question act 3 created.

## Reachability, recorded as orientation and not as determination

A five-page targeted read of Source C (`arXiv:2302.10778v3`, pp. 20–24) was made **before** drafting
this file, for one purpose only: to confirm that the construction this round is about exists in the
source, so that the round cannot fail for want of an object. Act 3's near-miss — a round nearly
frozen around a construction the corpus may not have contained — is why this check is done first and
recorded here.

What it establishes, and the round may cite it as orientation only:

- the correspondence is **unistochastic**: `Γ_ij(t ← 0) = |U_ij(t ← 0)|²`, Source C eq (44), p. 13,
  generalized to the composite at eq (72), p. 24;
- the object that factorizes is the **relative** time-evolution operator `U(t ← t′)`, eqs (46) and
  (74);
- footnote 21, p. 24, describes writing down "idealized examples of suitable unitary time-evolution
  operators… One choice is…", so **non-uniqueness of the unitary is live** rather than foreclosed.

**No determination is made here.** Whether those equations amount to a canonical selection for *our*
representation is target M2, and the third bullet is precisely why `MP1` and `MP2` are both
reachable rather than one being foreordained.

## The direction hazard, named before the targets

The two constructions run **opposite ways** and must not be silently composed.

- **Source C's direction.** Stochastic → quantum: given the process, build a Hilbert-space
  representation, with the transition matrix recovered as `|U|²`.
- **Ours.** Representation → candidate: given a `QfbData`, marginalize `bornPow` down to the visible
  carrier by a fibre weighting.

"Our representation instantiates his construction" is therefore **not** a single claim, and the
round states which of these it has established:

- **forward**: our `QfbData` is an instance of the data his construction takes as input, and his
  construction applied to it yields a determinate visible candidate;
- **backward**: the unitary his construction produces, applied to our rooted family, is the unitary
  our `QfbData` already carries.

The backward direction is **not** required for `MP1` and is not assumed by it. Conflating them is
the specific error this section exists to prevent.

## The four targets

**M1 — hypothesis check.** Against the construction's stated hypotheses, taken from the source and
listed by equation number, does our `QfbData` (with `IsLaw` and `PositiveRootMass`) satisfy each
one? Each hypothesis is recorded **individually** as satisfied, failed, or undetermined, with its
pinpoint citation. A hypothesis that our data satisfies only under an added assumption is recorded
as **failed at that scope**, with the assumption named.

**M2 — what the construction determines.** Does the construction fix a visible candidate
propagator, and is that candidate a function of data contained in `QfbData` alone? Two sub-questions,
answered separately:

- **M2a — determinacy.** Does the source's construction pick out one visible candidate, or a family?
- **M2b — containment.** If it picks one, is every datum it consumes present in `QfbData`, or does
  it consume something more?

**M3 — identification.** If M2 yields a determinate candidate, name it in this side's vocabulary:
is it `initWeight`'s candidate, `uniformWeight`'s, or a third rule? If a third, state it explicitly
enough that a later act could define it — **without defining it here**.

**M4 — what act 3's licence becomes.** Record, per the outcome reached, exactly what changes and
what does not in act 3's `CU1a` statement. Act 3's claim is about **our** bridge and stays true on
every outcome; what a determinate external selection would change is the programme-level reading,
not that claim. This target exists so the change is stated rather than absorbed.

## Admissible outcomes

The cases are exhaustive over the states of M1 and M2 and mutually exclusive.

**`MP1` — the construction canonically supplies one this-side candidate.** M1 closes with every
hypothesis satisfied, M2a gives determinacy, M2b gives containment, and M3 names the candidate.
The missing selection is then **part of the external theorem**, not an addition on our side.

**`MP2` — it maps, but consumes a datum `QfbData` does not contain.** M1 closes, M2a gives
determinacy, and M2b fails. The round then names **which datum**, which is the most valuable
possible answer short of `MP1`: it locates the extra selection precisely instead of leaving it as
"something is missing".

**`MP3` — our representation fails a stated hypothesis.** M1 records at least one hypothesis as
**failed**, exhibited against the source's own statement of it. This may bound the whole Track B
route and is therefore the outcome with the highest burden.

**`MP3` requires an exhibited failure and is never reached by non-verification.** A hypothesis we
could not check is recorded **undetermined**, and undetermined hypotheses give `MP4`. This is the
same discipline act 3 applied to `CU3`, one layer out: the absence of a verification is not a
finding of failure.

**`MP4` — undecidable from the available sources.** Any of: a hypothesis left undetermined; M2a
unresolved; M2b unresolved. Reported as **open**, with exactly which question is open and what would
settle it. Not a negative result and not evidence for any other outcome.

Exhaustiveness: if any hypothesis is exhibited failed, `MP3`; otherwise if any hypothesis is
undetermined or M2 is unresolved, `MP4`; otherwise M1 closes and M2a is determinate, and M2b decides
`MP1` against `MP2`.

## Prediction recorded before executing

**No confident prediction is recorded on `MP1` versus `MP2`, and that is deliberate rather than
evasive.** The orientation read found the unitary described through *chosen* idealized examples,
which is evidence toward non-uniqueness and so toward `MP2`; but it was five pages of a long paper,
looked at a composite measurement model rather than the subject system's own dilation, and is
exactly the kind of partial reading this programme does not let stand as a finding.

What is recorded: **`MP3` is unlikely**, because our `QfbData` is *built from* a unitary and its
Born weights are `‖U‖²` by construction, which is the shape the unistochastic condition asks for.
That is a reading of definitions, not a theorem, and M1 is where it is tested.

**`MP4` is materially live.** The construction's treatment spans several sections and the round is
bounded to the sources on hand.

## What this round produces, and what it does not

**It produces an audit determination, not a theorem.** A reading of an external text sits at level 1
or 3 of act 1's frozen evidence hierarchy, never at level 2, and **no Lean module is written in this
round**. If `MP1` is reached, formalizing the named candidate and proving our representation
instantiates the construction is a **later act** with its own freeze.

Stating it this way is what keeps a source reading from being cited later as though it were
kernel-checked.

## Mandatory controls

1. **Primary sources are consulted, and only for this question.** The three sources on hand, at
   pinpoint citation. No claim about any part of the external framework beyond the construction and
   its hypotheses.
2. **Act 1's determinations are cited, never extended.** `BD3` and `BR3` are neither reopened,
   softened nor re-derived, and this round adds nothing to what act 1 determined about the class or
   the theorem.
3. **`RT1` and act 3's results are consumed, not re-proved.** Act 3's `CU1a` stands; M4 records what
   the outcome changes about its *reading*, and no outcome here revises the theorem.
4. **No this-side definition is introduced**, and no Lean module is written. `candidateOf`,
   `initWeight`, `uniformWeight` and `Admissible` are used as merged and are not reshaped.
5. **No candidate-selection principle is adopted or proposed**, on any outcome.
6. **Direction is stated, never assumed.** Every mapping claim says which of the two directions of
   the section above it establishes.
7. **Each hypothesis is recorded individually** — satisfied, failed, or undetermined — with its
   citation. No aggregate "the hypotheses hold".
8. **No manuscript edit**, whatever is found.
9. **No sourcing inference.** Determining what an external construction fixes sources nothing about
   OI physics.
10. **Track separation** both ways, per Amendment 2. **No fifth condition.** No deferred Arc D
    resource adjudicated, and §3.6 is not reopened.

## Non-doings

Do not: adopt or propose a candidate-selection principle; define a new extraction rule; write Lean;
claim the external framework requires an additional physical principle; claim it does not; identify
`candidateOf` with an external object except as M3's explicit determination and at that scope only;
reopen `BD3`, `BR3`, `RT1` or `CU1a`; begin the tuple-instantiation lemma, Arc D round 2, or Arc E;
edit manuscripts.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any source adjudication. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen, committed before the work they affect.
- **Two PRs, in order.** Control-plane PR carrying **this file alone**, reviewed, frozen and merged
  before any execution; then exactly one execution/result PR from the resulting `main`.
- Final exact-head review after the result note and registry updates are complete.
- No merge without an explicit owner direction after exact-head review.

## Allowed final report

1. each hypothesis, individually, with its citation and its status;
2. M2a and M2b, answered separately;
3. if determinate: M3's identification, in this side's vocabulary;
4. the outcome label `MP1`–`MP4`, the recorded prediction, and whether it held;
5. which **direction** of the mapping section each claim establishes;
6. M4: what act 3's `CU1a` licence retains and what its programme-level reading becomes;
7. what remains open, and what would settle it;
8. explicitly: that this is an audit determination and not a theorem; that nothing here claims OI
   forces quantum structure; that nothing here is a sourcing claim; and that no candidate-selection
   principle has been adopted.
