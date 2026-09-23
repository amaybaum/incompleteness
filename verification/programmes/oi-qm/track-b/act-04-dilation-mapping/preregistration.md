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

## Source identities, inherited and not restated

Act 1's frozen table governs, and this round uses its letters:

| | Identity |
|---|---|
| **A** | *The Stochastic-Quantum Correspondence*, arXiv:2302.10778v3 |
| **B** | *Quantum Systems as Indivisible Stochastic Processes*, arXiv:2507.21192v1 |
| **C** | *The Stochastic-Quantum Theorem*, arXiv:2309.03085v2 |

**Equation numbers are never mixed across sources.** The same number means different things in A
and C, and every citation below names its source letter.

## Which construction this round audits

**Source C's theorem construction, and that one only.** It is the theorem-bearing source; it is the
construction act 1 audited for `BR3`; and it is the one that terminates in a quantum system, which
is what could supply a candidate.

**Source A's earlier correspondence construction is out of scope.** Whether the two constructions
agree on the induced candidate is a separate question, recorded here as open and not opened.

## Why this round is on the critical path

Act 3 proved that

    OI family  →  QfbData representation  →  candidate

is **not a function at our interface**. So a candidate-selection principle is required before "OI
forces this interference discrepancy" is a well-defined family-level question.

Act 3 also fixed what may **not** be concluded from that, and this round is the reason the
restriction was written. Act 1 established that the external diagnostic uses a **particular**
candidate whereas our `PDivisible` quantifies existentially. Until it is determined whether the
external construction supplies that candidate, we cannot tell whether the missing selection is
**already supplied by the correspondence** or is a genuinely additional principle on our side.

**No candidate-selection principle is adopted on our side in this round.** Doing so would pre-empt
exactly the question act 3 created.

## Reachability: an existence and location check, and nothing more

Made **before** drafting, for one purpose: to confirm the construction exists and to locate it, so
the round cannot fail for want of an object. Act 3's near-miss is why this is done first.

**It exists, in Source C §5.7–5.9.** The construction is a **Stinespring dilation** producing a
dilated tuple `(C̃, T̃, T̃₀, Γ̃, p̃, Ã)` at eqs (106)–(110), p. 27, closing with "*This conclusion
completes the proof of the stochastic-quantum theorem (69). QED*"; §5.9, p. 28, then gives "The
Corresponding Quantum System" — a Hilbert space `H̃` of dimension `Ñ ≤ N³` with unitary
`Ũ(t ← 0)`.

**That is the whole of the check, and nothing further is carried from it.** No claim is made here
about what the construction determines, what it consumes, or whether it is unique. Those are M1 and
M2 and they are adjudicated only after the freeze. In particular **no prediction is grounded on any
reading of the source**, which is the defect this section was rewritten to remove.

## The typing of the two obligations, named before the targets

The constructions run **opposite ways** and must not be silently composed. The forward obligation
starts from **stochastic-process/tuple data**, not from `QfbData`, and act 1's Q8 already fixed that
boundary.

- **Forward (this round's obligation).**

      our source-side stochastic datum  →  Source C's construction  →  external candidate

  The source-side datum is the merged `RootedRealization V H` read as a tuple, inheriting Q8's
  component ledger: `C`, `T`, `Γ` and `A` supplied; `T₀` and `p` **not carried** and to be
  **declared**. M1 checks the construction's hypotheses against **that** object, with its
  declarations stated.

- **Backward (a separate obligation, not this round's).** Whether the Hilbert space and unitary the
  construction produces coincide with the `QfbData` our side already carries. **Not required for
  `MP1` and not assumed by it.**

Conflating the two is the specific error this section exists to prevent, and every mapping claim in
the result must say which direction it establishes.

## The four targets

**M1 — hypothesis check against the correctly typed source-side object.** Against Source C's stated
hypotheses for the construction, listed by equation number, does our source-side datum — with its
`T₀` and `p` declarations — satisfy each one? Each hypothesis is recorded **individually** as
**satisfied**, **incompatible**, or **undetermined**, with its pinpoint citation. No aggregate "the
hypotheses hold".

Act 1's Q8 is **inherited, not re-derived**: it already determined which tuple components our datum
supplies. M1 extends that from tuple membership to the **construction's** hypotheses, which Q8 did
not examine.

**M2 — what the construction determines.** Two sub-questions, answered separately.

- **M2a — determinacy.** Does the construction fix one visible candidate, or fix it only **up to a
  named parameter or choice**? Three admissible answers: *unique*; *determinate given a named
  parameter*, with the parameter named; or *unresolved*.
- **M2b — containment.** Taking M2a's answer, is **every** datum the construction consumes —
  including any parameter M2a names — determined by our source-side datum and its declarations?

**M3 — identification.** If M2 yields a determinate candidate, name it in this side's vocabulary:
`initWeight`'s, `uniformWeight`'s, or a third. If a third, state it explicitly enough that a later
act could define it — **without defining it here**.

**M4 — what act 3's licence becomes.** Record, per the outcome, exactly what changes and what does
not in act 3's `CU1a` statement. Act 3's claim is about **our** bridge and stays true on every
outcome; what a determinate external selection would change is the programme-level reading, not that
claim. This target exists so the change is stated rather than absorbed.

## Admissible outcomes

**`MP1` — the external correspondence supplies the selection.** M1 records every hypothesis
satisfied, M2a is *unique* or *determinate given a named parameter*, M2b is **yes**, and M3 names
the candidate.

The permitted sentence is *the external correspondence supplies the candidate selection*. **Not**
permitted from this round: that the selection is a theorem-level conclusion of the external theory —
that is stronger than an audit of the construction earns, and would need the theorem's own statement
to say so.

**`MP2` — it maps, but consumes a datum our side does not determine.** M1 records every hypothesis
satisfied, M2a is answered, and **M2b fails**. The round then names **which datum or choice**. This
is the most valuable answer short of `MP1`: it locates the extra selection precisely instead of
leaving it as "something is missing".

**A named parameter is `MP2`, never `MP3` and never `MP4`.** Needing an extra datum is not a
violation of a hypothesis, and a construction determinate only up to a named choice is exactly what
`MP2` exists to capture — not an unresolved reading.

**`MP3` — direct incompatibility.** M1 records at least one hypothesis as **incompatible**:
**no admissible completion** of our source-side datum — over the `T₀` and `p` declarations left open
by Q8 — satisfies the hypothesis as Source C states it. Exhibited against the source's own
statement. This may bound the whole Track B route and carries the highest burden.

**`MP3` is never reached by non-verification, and never by a needed datum.** A hypothesis we could
not check is **undetermined**, which gives `MP4`; a hypothesis satisfiable under a named additional
datum is **satisfied for `MP3` purposes** and the datum is `MP2`'s business. This is act 3's `CU3`
discipline, one layer out.

**`MP4` — undecidable from the available sources.** Any of: a hypothesis left undetermined; M2a
unresolved; M2b unresolved. Reported as **open**, with exactly which question is open and what would
settle it. Not a negative result and not evidence for any other outcome.

**Exhaustiveness.** If any hypothesis is exhibited incompatible → `MP3`. Otherwise if any hypothesis
is undetermined, or M2a is unresolved, or M2b is unresolved → `MP4`. Otherwise M1 closes and M2a is
answered, and M2b decides `MP1` against `MP2`. The cases are disjoint.

## Prediction recorded before executing

**No prediction is recorded on `MP1` versus `MP2` versus `MP4`.** An earlier draft of this file
leaned toward `MP2` on a reading of the source; that lean rested on a footnote in the wrong paper
about a composite measurement unitary, which bears on the freedom in *that* operator and not on
whether the induced **visible candidate** is unique — a step that needs the very M2 mapping this
round exists to adjudicate. The lean is withdrawn and nothing replaces it.

What is recorded: **`MP3` is unlikely**, on a ground that does not read the construction. Act 1's Q8
determined that our datum supplies four of the six tuple components and that the remaining two are
declarable rather than unavailable — `T₀ = {0}` being the natural declaration, and `p` free by
Source C's own account of it. A direct incompatibility would therefore have to arise from a
hypothesis of the **construction** that Q8 did not examine, which is possible but is not what Q8's
ledger suggests. That is a reading of a merged determination, not of the source, and M1 is where it
is tested.

**`MP4` is materially live.** The construction spans several subsections and the round is bounded to
the sources on hand.

## What this round produces, and what it does not

**An audit determination, not a theorem.** A reading of an external text sits at level 1 or 3 of act
1's frozen evidence hierarchy, never at level 2, and **no Lean module is written in this round**. If
`MP1` is reached, formalizing the named candidate and proving our datum instantiates the
construction is a **later act** with its own freeze.

Stating it this way is what keeps a source reading from being cited later as though it were
kernel-checked.

## Mandatory controls

1. **Primary sources are consulted, and only for this question.** Source C's construction and its
   hypotheses, at pinpoint citation. No claim about any other part of the external framework.
2. **Source letters, pages and equation numbers follow act 1's frozen table**, and equation numbers
   are never mixed across sources.
3. **Act 1's determinations are cited, never extended.** `BD3`, `BR3` and Q8 are neither reopened,
   softened nor re-derived; Q8's ledger is inherited as given.
4. **`RT1` and act 3's results are consumed, not re-proved.** Act 3's `CU1a` stands; M4 records what
   the outcome changes about its *reading*, and no outcome here revises the theorem.
5. **No this-side definition is introduced**, and no Lean module is written. `candidateOf`,
   `initWeight`, `uniformWeight` and `Admissible` are used as merged and are not reshaped.
6. **No candidate-selection principle is adopted or proposed**, on any outcome.
7. **Direction is stated, never assumed.** Every mapping claim says whether it establishes the
   forward or the backward obligation.
8. **Each hypothesis is recorded individually** — satisfied, incompatible, or undetermined — with
   its citation.
9. **No manuscript edit**, whatever is found.
10. **No sourcing inference.** Determining what an external construction fixes sources nothing about
    OI physics. **Track separation** both ways, per Amendment 2. **No fifth condition.** No deferred
    Arc D resource adjudicated, and §3.6 is not reopened.

## Non-doings

Do not: adopt or propose a candidate-selection principle; define a new extraction rule; write Lean;
audit Source A's earlier construction; mix equation numbering across sources; claim the external
framework requires an additional physical principle; claim it does not; claim the selection is a
theorem-level conclusion; identify `candidateOf` with an external object except as M3's explicit
determination and at that scope only; establish the backward obligation by assumption; reopen `BD3`,
`BR3`, Q8, `RT1` or `CU1a`; begin the tuple-instantiation lemma, Arc D round 2, or Arc E; edit
manuscripts.

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

1. each hypothesis, individually, with its source-C citation and its status;
2. M2a and M2b, answered separately, with any parameter named;
3. if determinate: M3's identification, in this side's vocabulary;
4. the outcome label `MP1`–`MP4`, the recorded prediction, and whether it held;
5. which **obligation** — forward or backward — each claim establishes;
6. M4: what act 3's `CU1a` licence retains and what its programme-level reading becomes;
7. what remains open, and what would settle it, including whether Source A's construction agrees;
8. explicitly: that this is an audit determination and not a theorem; that under `MP1` the
   correspondence *supplies* the selection and no theorem-level claim is made; that nothing here
   claims OI forces quantum structure; that nothing here is a sourcing claim; and that no
   candidate-selection principle has been adopted.
