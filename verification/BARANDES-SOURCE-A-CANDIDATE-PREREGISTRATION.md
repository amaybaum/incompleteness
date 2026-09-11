# Track B act 5 — Source A's candidate selection: preregistration

Base: `main` at `ac10d48a1ed37ced3e6aaed6c2134f32f6b252c2` (post-PR #567, act 4 closed at `MP4`).

Presupposes act 1 (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560), act 2
(`BARANDES-TRANSPOSE-BRIDGE-RESULT.md`, PR #562), the scoping pass
(`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, PR #563), act 3
(`BARANDES-CANDIDATE-SELECTION-RESULT.md`, PR #565) and act 4
(`BARANDES-DILATION-MAPPING-RESULT.md`, PR #567).

**A source-to-formal audit round, the second in Track B to consult a primary source.** Act 4's
controls carry over, with the source of record changed and one control added.

Status: **draft; nothing here is frozen until the reviewer approves an exact commit and blob, and no
execution begins before the freeze is merged.**

## Source identities, inherited and not restated

Act 1's frozen table governs, and this round uses its letters:

| | Identity |
|---|---|
| **A** | *The Stochastic-Quantum Correspondence*, arXiv:2302.10778v3 |
| **B** | *Quantum Systems as Indivisible Stochastic Processes*, arXiv:2507.21192v1 |
| **C** | *The Stochastic-Quantum Theorem*, arXiv:2309.03085v2 |

**Equation numbers are never mixed across sources.** The same number means different things in A and
C — act 4's one pre-freeze blocker was exactly this conflation, in the reverse direction — and every
citation below names its source letter.

## Which source this round audits, and which it does not

**Source A, and that one only.** Source C was adjudicated by act 4 and is **not reopened**: its
`MP4` stands as merged, and nothing in this round revises, softens or re-reads it.

**This round does not compare the two sources.** It does not ask whether Source A's treatment is
better than Source C's, whether the two are equivalent, whether they agree on any induced candidate,
or whether either supersedes the other. Those are separate questions, recorded here as open and not
opened.

## Why this round is on the critical path, and why it displaced the tuple lemma

Act 3 proved that

    OI family  →  QfbData representation  →  candidate

is **not a function at our interface** (`CU1a`). A candidate-selection principle is therefore
required before "OI forces this interference discrepancy" is a well-defined family-level question.

Act 4 asked whether Source C's construction supplied the missing selection and returned `MP4`: every
object that construction builds is indexed `(t ← 0)` and its dilated conditioning-time set is
declared the singleton `{0}`, so it produces no intermediate propagator at all. Source C does not
supply the selection — not by supplying an ambiguous one, but by producing no candidate at that
layer.

The blocker is therefore still

    rooted stochastic family  →  selected external candidate  →  discrepancy/interference

and the `BarandesTuple` instantiation lemma, valuable as it is, does not address it: it would make
the first arrow kernel-checkable without determining what the second arrow's object is. Source A
carries relative-time machinery in its own development, so it is the one remaining place on this
route where the question can be asked of an existing construction rather than of a rule we invent.
**Act 5 therefore precedes the tuple lemma, which moves to second and is not abandoned.**

## Act 4's `MP4` is not amended, and no extraction rule is authorized

Act 4 closed cleanly **because** it respected Source C's actual interface and declined to form the
relative operator on that source's behalf. **That result is not reopened and no append-only
amendment authorizing a relative-operator extraction is made**, in this round or as a consequence of
it.

The point of asking Source A is precisely that it *already contains* relative-time machinery, so the
same question can be put without introducing an artificial rule of our own. **If Source A turns out
not to contain it in the load-bearing sense, the answer is `SA3` or `SA4` — not an amendment.**

## The authoritative numbering surface

**Equation and page coordinates are load-bearing in this audit, so the surface they are read off is
frozen here.**

**The authoritative surface is the PDF of arXiv:2302.10778v3**, which self-identifies by the stamp
`arXiv:2302.10778v3 [quant-ph] 30 Jul 2025` on p. 1. Every equation number and page number in this
file and in the result note is read off **that** document.

**arXiv's HTML rendering of the same version is not authoritative here**, and its equation numbering
is known to differ from the PDF's. A coordinate that does not resolve on the PDF is a **defect to be
repaired**, never reconciled by silently switching surfaces; if the result note ever needs to cite
the HTML rendering, it must say so at the citation.

This section exists because the first draft of this freeze pinned one site without checking whether
others carried the same machinery, and a reviewer reading a different surface found a different
number. Ambiguous coordinates are not frozen.

## Reachability: an existence and location check, and nothing more

Made **before** drafting, for one purpose: to confirm there is an object to audit, so the round
cannot fail for want of one.

**Relative-time machinery exists in Source A at four distinct sites**, all verified on the
authoritative PDF:

| Site | Location | What is there |
|---|---|---|
| **S1** | §3.5 "Interference", pp. 13–14 | relative time-evolution operator, eq (39) p. 13; composition law, eq (40) p. 14; a matrix written `Γ(t ← t′)`, eq (42) p. 14; a discrepancy formula, eq (43) p. 14 |
| **S2** | §3.7 "Division events and the Markov approximation", pp. 16–18 | a composite-system relative time-evolution operator and its tensor factorization, eq (46) p. 17 |
| **S3** | §3.9 "Entanglement", p. 21 | a relative transition matrix `Γ^AB(t ← t″)` and its tensor factorization, eqs (65)–(66) |
| **S4** | §4.2 "The measurement process", pp. 23–25 | a hybrid relative transition matrix, eqs (73)–(77) |

§3.4 "Unistochastic processes", pp. 10–12, is where the operator these are built from is introduced.

**That is the whole of the check, and nothing further is carried from it.** No claim is made here
about which site (if any) carries the object A1 is after, whether any of these is part of the
construction rather than exposition, what data it is computed from, whether it is invariant under
the freedoms Source A permits, or whether it is unique. Those are A1–A6 and they are adjudicated
only after the freeze.

**A1 is not pre-decided by this table.** Listing four sites rather than one is deliberate: an earlier
draft named S1 alone, which would have let the location check settle A1 by omission. **A1 must
determine which site or sites carry the intermediate/relative propagator role**, and may find that
more than one does, that they are instances of a common object, or that none plays the role in the
load-bearing sense.

In particular, **that an equation of candidate shape appears at a located page is not a finding that
Source A selects a candidate** — that inference is A2's business, and act 4 is the standing reminder
of what happens when a located object is promoted into a construction that does not contain it.

## The six frozen questions

Exactly these, in this order. Each is answered separately, with pinpoint Source A citation — or with
**not reached**, per the next section, when an earlier question has terminated the taxonomy.

**A1 — identification of the object.** What exact object in Source A plays the intermediate /
relative propagator role? Named by equation number and page, with its type stated: operator or
visible (stochastic) matrix, and indexed from which times.

**A2 — construction or post-processing.** Is that object part of Source A's own construction, or is
it something this round would be inventing on the source's behalf? Answered from the source's own
use of it — whether it is defined, carried forward, and relied on in the development — not from its
mere presence on a page. **This is the question act 4's first executed draft got wrong**, and the
burden is on the affirmative.

**A3 — provenance of the inputs.** From exactly which source data is the A1 object computed? Every
input listed, with its citation, **including any presupposition on the input process** that the
computation requires. Stated in Source A's own terms.

**A4 — invariance under the source's own freedoms.** Is the A1 object invariant under **all**
freedoms Source A itself permits on those inputs? Each permitted freedom named with its citation,
and the object's behaviour under it stated. A freedom the source permits but this round does not
examine is recorded as **not examined**, never as absent.

**A5 — uniqueness after the visible readout.** After taking the visible stochastic / Born readout,
is the resulting **candidate** unique? Answered at the level of the visible matrix, not the
operator. Three admissible answers: *unique*; *determinate given a named parameter or choice*, with
it named; or *unresolved*.

**A6 — identification in our vocabulary.** Can the resulting candidate be identified with one of our
frozen candidate rules — `initWeight`'s or `uniformWeight`'s — or is it a third rule? Three
admissible answers: *identified*, naming which; *a named third rule*, stated explicitly enough that
a later act could define it, **without defining it here**; or **unresolved**, when Source A does not
specify enough to place the visible rule among these — which routes to `SA4`.

**Under `SA2`, A6 names a parameterized rule or family**, not a single rule. A5 having already found
visible dependence on a choice, requiring A6 to produce one rule would be incoherent; the family and
its parameter are what A6 reports.

## *Not reached* versus *unresolved*, and which questions carry which

The questions are **sequentially dependent**: A3 asks for the A1 object's inputs, A4 for its
behaviour under freedoms on those inputs, A5 for the visible readout of that object, A6 for the
identification of that readout. When an earlier question terminates the taxonomy, the later ones are
**not logically live**, and reporting them as though they had been examined would misstate the
evidence. So two statuses are frozen, and they are not interchangeable:

- **Unresolved** — the question **was reached and examined**, and Source A does not settle it. This
  is an evidential finding. It is what routes A2, A5 and A6 to `SA4`.
- **Not reached** — an earlier question terminated the taxonomy, so this question is not live. It
  carries **no evidential weight whatever**: it is never a reason for `SA4`, never counts toward any
  outcome's conditions, and is never reported as a limitation of the source.

**Calling a not-reached question *unresolved* is an error**, because it would convert a structural
consequence of an earlier answer into a finding about Source A. Act 4 recorded its M2b and M3 this
way, and act 5 inherits the discipline explicitly rather than by analogy.

**What is not reached, per terminating answer:**

| Terminating answer | Outcome | Not reached |
|---|---|---|
| A2 *not part of the construction* | `SA3` | A3, A4, A5, A6 |
| A2 *undetermined* | `SA4` | A3, A4, A5, A6 |
| A3 cannot be completed | `SA4` | A4, A5, A6 |
| A4 leaves a bearing freedom unexamined | `SA4` | A5, A6 |
| A5 *unresolved* | `SA4` | A6 |
| A6 *unresolved* | `SA4` | — all reached |

**A6 under `SA3` is reported as *not reached — no candidate exists at this interface***, in those
terms. Not silently omitted, and not *unresolved*: under `SA3` the reason there is nothing to
identify is that Source A's development forms no visible intermediate candidate, which is `SA3`'s
own finding and not a further gap in the source.

**A1 is always reached**, since A2 presupposes an identified object; if A1 itself cannot name one,
that is an A2 *not part of the construction* answer and the round is an `SA3`.

## The control that act 4 earned: operator freedom is not candidate freedom

**Unitary or operator non-uniqueness does not count as candidate non-uniqueness without an explicit
visible counterexample.** To record the A1 object as choice-dependent at A5, the round must exhibit
**two admissible choices, permitted by Source A's own stated freedoms, whose visible readouts
differ** — two concrete matrices, not an argument that the operator is underdetermined.

This cuts both ways, and the second direction is the one to watch. Operator freedom that is **not**
shown to move the visible candidate is recorded as **representation freedom**, exactly as act 4
recorded Source C's Stinespring completion, and **is not named as a candidate-selection datum**.
Absent such a counterexample, A5 is *unique* or *unresolved* — never *determinate given a named
parameter* on the strength of operator freedom alone.

## What is deliberately not asked

**Whether our side's datum supplies the A3 inputs.** A3 reports what Source A's construction
consumes, in Source A's terms. Whether the merged `RootedRealization` read as a tuple determines
those inputs is the act 4-style containment question, and it is **recorded open, not adjudicated
here** — it is what the `BarandesTuple` instantiation lemma exists to make checkable, and answering
it by inspection now would be the plumbing becoming the headline. If A3 names a presupposition our
side plainly may not meet, that is **recorded as a named open question**, not resolved.

**Anything about the backward obligation.** Whether the Hilbert space and unitary Source A produces
coincide with the `QfbData` our side carries is a separate obligation, not attempted and not
assumed.

## Admissible outcomes

**`SA1` — canonical selection.** A2 is *part of the construction*, A3 lists inputs, A4 records
invariance under **every** permitted freedom examined with none outstanding, A5 is *unique*, and A6
is *identified* or *a named third rule*. The permitted sentence is *Source A's construction selects a
visible intermediate candidate, canonically from the data it names*. **Not** permitted: that this is
a theorem-level conclusion of Source A, which an audit of a construction does not earn; nor any
claim that our side's datum supplies those inputs.

**`SA2` — selection conditional on a named extra datum.** A2 is *part of the construction*, A5 is
*determinate given a named parameter or choice*, **exhibited by visible counterexample** per the
control above, and A6 names the parameterized rule or family. The round then names the datum. This
is the most valuable answer short of `SA1`: it locates the extra selection precisely rather than
leaving it as "something is missing".

**What `SA2`'s "extra datum" means, and what it does not.** It is **a choice not fixed by the
Source A data A3 lists** — a freedom internal to Source A's own construction. It is **not** a datum
missing from *our* side: containment against our `RootedRealization` is deliberately deferred (see
above), so no `SA2` finding says or implies anything about what our datum supplies.

**`SA3` — no candidate produced.** A2 is *not part of the construction*: Source A's development does
not itself form a visible intermediate candidate, and forming one would be post-processing this
round invents. A3 through A6 are then **not reached**, A6 with the reason stated. Reported at that
scope — a determination about **Source A's construction**, never a claim that no candidate exists or
that none could be defined.

**`SA4` — source or interface insufficient to decide.** Any of: A2 undetermined; A3 unable to list
the inputs; A4 leaving a permitted freedom unexamined that bears on A5; A5 unresolved; **A6
unresolved**. Reported as **open**, with exactly which question is open and what would settle it.
Not a negative result and not evidence for any other outcome.

**A6 unresolved is an `SA4`, not a downgrade of A5.** A construction can fix a unique visible
candidate that Source A does not specify well enough to place among our rules: A5 *unique* with A6
*unresolved* is a coherent state of the evidence, it belongs to no other outcome, and it is reported
as `SA4` with A5's finding stated in full rather than discarded.

**Exhaustiveness.** If A2 answers *not part of the construction* → `SA3`. Otherwise if A2 is
undetermined, or A3 cannot be completed, or A4 leaves a bearing freedom unexamined, or A5 is
unresolved, or A6 is unresolved → `SA4`. Otherwise A5 decides `SA1` against `SA2`. The cases are
disjoint and exhaust the possibilities.

**A6 is reported under every outcome**, with the status the table above assigns it: its answer under
`SA1` and `SA2`; *unresolved* in the `SA4` that its being unresolved produces; and **not reached**
under `SA3`, and under any `SA4` terminated before A6 — in the `SA3` case with the reason stated, *no
candidate exists at this interface*. The same holds for A3, A4 and A5: each appears in the report
with an answer or an explicit *not reached*, never absent.

## Prediction recorded before executing

**No prediction on `SA1` versus `SA2` versus `SA4`.** Each turns on A2, A4 and A5, which are what
this round exists to adjudicate, and act 4 is the standing lesson about leaning on a pre-freeze
reading.

**`SA3` is unlikely, on the location check and on that alone.** Equations of candidate shape were
located at four named sites. That is weaker than it sounds: every one of them could still fail A2 by
being expository rather than load-bearing in Source A's development, which is a live path to `SA3`
and is exactly what act 4 found one source over — there the located objects were real, correctly
cited, and still did not amount to a construction that selects. The prediction is recorded at that
strength and no higher.

## What this round produces, and what it does not

**An audit determination, not a theorem.** A reading of an external text sits at level 1 or 3 of act
1's frozen evidence hierarchy, never at level 2, and **no Lean module is written in this round**. If
`SA1` or `SA2` is reached, formalizing the named candidate and proving our datum instantiates the
construction is a **later act** with its own freeze — and the `BarandesTuple` instantiation lemma is
its natural first step.

## Mandatory controls

1. **Primary sources are consulted, and only for this question.** Source A's relative-time
   machinery and its stated freedoms, at pinpoint citation. No claim about any other part of the
   external framework.
2. **Source letters, pages and equation numbers follow act 1's frozen table**, and equation numbers
   are never mixed across sources. **Every coordinate resolves on the authoritative surface** — the
   PDF of arXiv:2302.10778v3, per the section above. A citation to any other rendering says so at
   the citation, and a coordinate that does not resolve is repaired, never reconciled by silently
   switching surfaces.
3. **Act 4's `MP4` is cited, never revised**, and no amendment authorizing a candidate-extraction
   rule is made. Source C is not re-adjudicated.
4. **Act 1's determinations are cited, never extended.** `BD3`, `BR3` and Q8 are neither reopened,
   softened nor re-derived.
5. **`RT1` and act 3's `CU1a` are consumed, not re-proved.** `CU1a` is a theorem about **our**
   bridge; no outcome here revises it, and the round states what its programme-level reading becomes.
6. **No this-side definition is introduced**, and no Lean module is written. `candidateOf`,
   `initWeight`, `uniformWeight` and `Admissible` are used as merged and are not reshaped.
7. **No candidate-selection principle is adopted or proposed**, on any outcome.
8. **Operator freedom is not candidate freedom** without an exhibited visible counterexample, per
   the control above; unexhibited freedom is recorded as representation freedom.
9. **Each of A1–A6 appears individually in the report** — with its citation when answered, or with
   an explicit **not reached** when an earlier question terminated the taxonomy, per the table above.
   None is silently omitted, a not-reached question is never called *unresolved*, and A4's freedoms
   are enumerated rather than summarized.
10. **Direction is stated, never assumed.** Every mapping claim says whether it establishes the
    forward or the backward obligation.
11. **No manuscript edit**, whatever is found.
12. **No sourcing inference.** Determining what an external construction fixes sources nothing about
    OI physics. **Track separation** both ways, per Amendment 2. **No fifth condition.** No deferred
    Arc D resource adjudicated, and §3.6 is not reopened.

## Non-doings

Do not: adopt or propose a candidate-selection principle; define a new extraction rule; amend act 4;
re-adjudicate Source C; compare Source A with Source C or claim either is better, equivalent or
superseded; adjudicate whether our datum supplies Source A's inputs; write Lean; mix equation
numbering across sources; treat operator non-uniqueness as candidate non-uniqueness without a
visible counterexample; claim the external framework requires an additional physical principle;
claim it does not; claim any finding is a theorem-level conclusion of Source A; identify
`candidateOf` with an external object except as A6's explicit determination and at that scope only;
establish the backward obligation by assumption; reopen `BD3`, `BR3`, Q8, `RT1`, `CU1a` or `MP4`;
begin the tuple-instantiation lemma, the BD3 follow-up, Arc D round 2 or Arc E; edit manuscripts.

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

1. A1–A6, each appearing individually — answered with its Source A citation, or marked **not
   reached** with the terminating answer named;
2. A4's permitted freedoms, enumerated, each with the object's behaviour under it or an explicit
   *not examined* — or A4 marked *not reached*;
3. A5's answer at the visible level, with any exhibited counterexample given as two concrete
   matrices, and any unexhibited operator freedom recorded as representation freedom — or A5 marked
   *not reached*;
4. the outcome label `SA1`–`SA4`, the recorded prediction, and whether it held;
5. A6's status — the identification in this side's vocabulary under `SA1`, the parameterized rule or
   family under `SA2`, *unresolved* with what Source A leaves unspecified in the `SA4` that produces,
   or **not reached** under `SA3` and under any `SA4` terminated before A6, in the `SA3` case reading
   *no candidate exists at this interface*;
6. which **obligation** — forward or backward — each claim establishes;
7. what act 3's `CU1a` licence retains and what its programme-level reading becomes;
8. what remains open and what would settle it, including whether our datum supplies Source A's
   inputs, and whether Source A and Source C agree;
9. explicitly: that this is an audit determination and not a theorem; that no theorem-level claim
   about Source A is made; that act 4's `MP4` is unrevised and no extraction rule has been
   authorized; that nothing here claims OI forces quantum structure; that nothing here is a sourcing
   claim; and that no candidate-selection principle has been adopted.
