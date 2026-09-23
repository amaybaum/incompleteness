# Act 12 scope propagation — the two-sided invisible gauge, the fibre-Gram classification, and the two-part frontier: CONTROL PLANE

Owner-called, publication-only, written from `main` at
`aa4ac3a621a4967c1075fd129d49f88c724eecd0`, which carries the merged Track B act 12 execution
(#592, sealed head `85bb794febeab9251e0d9b3356ac6640e18bbee2`, merge `64fd89f22de0bb3db3c03627385a9b83b4ae9c75`).
This file is committed alone, in its own pull request, before any manuscript is touched, and the
execution pull request descends from the commit that merges it. **Blob identity is authoritative.**

The round propagates one already-settled classification and its consequence for the open frontier,
and does **no new mathematics**. The authoritative inputs are consumed, not re-adjudicated:

| | |
| --- | --- |
| Act 12's result | `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 12's module | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's propagation freeze and its amendment, both still authoritative for their own surfaces | `act11-scope-propagation-audit.md`, blob `cc6d5adb5682cd560d9342496fbaeeb957b760b9`; `act11-scope-propagation-open-frontier-amendment.md`, blob `50f74a0869789dd7188f850cf5ceee125596fb9b` |
| The surfaces this round edits, at the start state | `papers/Main.md` `deedef7a…`; `papers/Explainer.md` `79d1de2a…`; `book/ch01-observation.md` `1006dd68…`; `book/ch19-open-problems.md` `9f94b561…`; `book/glossary.md` `74a99799…`; `book/The-Incompleteness-of-Observation-FULL.md` `1b5499fc…`; `verification/lean-manuscript-census.json` `75dc27bd…` |

## What is being propagated, in the merged result's own terms

1. **The two-sided uniform gauge.** The uniformly invisible deformations of a lift come in two
   factors: act 11's right action by the maximal uniform anchored (weak) class, and act 12's left
   action by unitaries acting within each visible output's hidden fibre (`LeftFibreGroup`),
   invisible universally and maximal among uniform left actions considered alone
   (`left_preserves_admissible`, `left_of_preserves_every_admissible`). **Joint maximality of the
   two-sided action is neither asserted nor excluded**; the manuscript may say "each maximal among
   uniform actions of its kind" and "the two-sided action they generate", never "the maximal
   two-sided action".
2. **Act 11's open target is closed, positively, as right-only insufficiency** (`RO1`,
   `ro1_right_only_insufficient`): two coherent lifts of one visible family, **not** related by the
   right class, **differing in relating evolution**, with the relating element a **left** in-fibre
   move. So quotienting by the right class alone does not determine the relating evolution; the
   reading is exactly that, and not a statement about every gauge or connection description.
3. **The per-slice classification** (`TG2`, `twoSided_slice_iff`, `twoSidedRelated_iff`): at one
   time, two lifts are related by the two-sided action exactly when their fibre-Gram data — for
   each visible output, the Gram matrix of the hidden states into which the lift sends the visible
   inputs — agree up to the anchored phases. **Per slice only.**
4. **The shape** (`SH1`, `sh1_shape`): the visible law is exactly the diagonal of the fibre-Gram
   data, and every positive semidefinite, rank-at-most-`|A|`, identity-summing family with the
   prescribed diagonal is realized. Together: *the residual lift freedom, after the two-sided
   uniform gauge, is exactly the off-diagonal fibre-Gram data modulo the anchored phases — per
   time slice.*
5. **The quotient is not inert** (`TG3`, `hadamard_lifts_not_twoSided`): on a single visible law
   two coherent lifts can lie in different two-sided classes and differ in relating evolution.
6. **The frontier is two-part.** What remains open is (i) what selects or constrains the trajectory
   of fibre-Gram data (the orbit) across time, and (ii) what determines the relating evolution
   within a given trajectory — and the second is not fixed even by the complete trajectory, since
   a time-dependent invisible right deformation preserves every fibre-Gram matrix at every time
   and changes the relating evolution (act 11's `GL2`, read at act 12's exact-head review).
7. **The non-licences, verbatim from the merged result:** nothing here says embedded observation
   and quantum mechanics are inequivalent; the fibre-Gram data is a coordinate on the lift space,
   not a physical quantity; nothing here is a cross-time statement; no selection principle is named,
   endorsed or excluded, and nothing is said about connections or gauge fixings in either direction;
   overlap is not memory; `P0` is not closed.

The owner's summary of the message, which the manuscript must carry and not exceed: **the per-slice
freedom is classified by fibre-Gram data under the defined two-sided action, but even a complete
Gram trajectory does not determine the relative evolution.**

## The items, fixed in advance

Every replacement below is frozen as to content; the execution may adjust punctuation and
sentence order only where the surrounding paragraph requires it, and must report any such
adjustment. Manuscript voice throughout: no act numbers, theorem labels, kernel identifiers,
review history, branch or pull-request language, and no narration of what an earlier version said.

### Item 1 — Main: the scope remark, corrected forward

In `papers/Main.md`, in *Remark (scope: representability, not selection of the relating
evolution)*, the two sentences

> Invisibility does not exhaust the freedom either: two lifts of one visible family can fail to be
> related by any uniformly invisible deformation and still agree on every relating evolution, so
> lift freedom and freedom in the relating evolution are not the same freedom. Whether a pair
> exists that is outside the uniformly invisible class *and* differs in its relating evolution is
> open.

are replaced by the following, in this order and this content:

> The uniformly invisible deformations of a lift are two-sided: the time-dependent right action
> just described, by the anchored class, and a left action by unitaries acting within each visible
> output's hidden fibre; each is maximal among uniform actions of its kind, and neither is seen by
> the visible law. Invisibility does not exhaust the freedom: two lifts of one visible family can
> fail to be related by any uniformly invisible right deformation and still agree on every
> relating evolution, so lift freedom and freedom in the relating evolution are not the same
> freedom; and a pair outside that right class can differ in its relating evolution while being
> related by a left in-fibre move, so quotienting by the right class alone does not determine the
> relating evolution. At a single time the residue after the two-sided action is classified
> exactly: two lifts are related by it exactly when, for each visible output, the Gram matrix of
> the hidden states into which they send the visible inputs — the fibre-Gram data — agrees up to
> the anchored phases; the visible law is exactly the diagonal of that data, and every positive
> semidefinite, rank-bounded, identity-summing family with the prescribed diagonal is realized. So
> what the visible law leaves free at one time is exactly the off-diagonal fibre-Gram data modulo
> phases, and that freedom is neither empty nor inert: on a single visible law two lifts can lie in
> different two-sided classes and differ in their relating evolution. Across time the question is
> two-part, and both parts are open: what selects or constrains the trajectory of fibre-Gram data
> through time, and what fixes the relating evolution within a given trajectory — the second not
> fixed even by the complete trajectory, since a time-dependent invisible right deformation
> preserves every fibre-Gram matrix at every time and changes the relating evolution. The
> fibre-Gram data is a coordinate on the space of lifts, not a physical quantity, and nothing here
> says what selects it.

Every other sentence of the remark — ordinary coherence insufficient; a deformation constant in
time cancels; the selection condition unnamed; nothing alters `S ⇔ D ⇔ Q_fb`; nothing makes the
two inequivalent; the open frontier; the three statuses — is preserved verbatim. The three statuses
are unchanged: selection of a unique relating evolution from the coherent lifts of one visible
family is *open*.

### Item 2 — Explainer and Chapter 1: the same correction, at their level

In `papers/Explainer.md` (the paragraph **And it does not fix which unitary relates two times.**)
and `book/ch01-observation.md` (the paragraph beginning "A second boundary sits alongside it"),
the two sentences

> The freedom is also not simply the invisible freedom: two lifts of one visible family can fail
> to be related by any uniformly invisible deformation and still agree on every relating
> evolution. Whether a pair exists that is both outside the uniformly invisible class and
> different in relating evolution is open.

(Chapter 1: "Nor is the freedom simply the invisible freedom: … Whether a pair exists that is
outside the uniformly invisible class *and* differs in its relating evolution is open.") are
replaced by:

> The invisible freedom itself has two sides — a right action by the anchored class and a left
> action within each visible output's hidden fibre, each maximal among uniform actions of its kind
> — and it does not exhaust the freedom: two lifts can fail to be related by any uniformly
> invisible right deformation and still agree on every relating evolution, and a pair outside that
> right class can differ in relating evolution while being related by a left in-fibre move. At one
> time, what the visible law leaves free after both actions is known exactly: it is the
> off-diagonal part of the fibre-Gram data — for each visible output, the overlaps among the
> hidden states into which the lift sends the visible inputs — modulo phases, with the visible law
> as its diagonal; and that residue is not inert, since two lifts of one visible law can differ in
> it and differ in relating evolution. What remains open is two-part: what selects the trajectory
> of that data through time, and what fixes the relating evolution within a trajectory — the
> latter not fixed even by the complete trajectory. No selection principle is named or excluded.

The Explainer's **three statuses** paragraph is preserved verbatim. Chapter 1's closing sentence
("None of this weakens the finite observable-law equivalence, and none of it makes embedded
observation and quantum mechanics inequivalent.") is preserved verbatim.

### Item 3 — Chapter 19 §19.3.9: the frontier entry, sharpened

In `book/ch19-open-problems.md`, §19.3.9:

- **What is settled**, **What is open**, **What is claimed** (see below) and *Developed in* are
  preserved, except that the "What is open" paragraph gains its two-part form: after "…compatible
  with a single visible family." append: "The question is two-part: what selects or constrains,
  through time, the fibre-Gram data of the lift — for each visible output, the overlaps among the
  hidden states into which the lift sends the visible inputs — and what fixes the relating
  evolution within a given trajectory of that data."
- **What is proved about it** is extended, after its present content, by: "The invisible
  deformations are two-sided — a right action by the anchored class and a left action within each
  visible output's hidden fibre, each maximal among uniform actions of its kind — and at one time
  the residue after both is classified exactly: two lifts are related by the two-sided action
  exactly when their fibre-Gram data agree up to phases, the visible law is the diagonal of that
  data, and every positive semidefinite, rank-bounded, identity-summing family with the prescribed
  diagonal occurs. So the freedom the visible law leaves at one time is exactly the off-diagonal
  fibre-Gram data modulo phases."
- **What is not proved about it** is replaced, in place, by a paragraph headed **What is sharper,
  and what it does not settle.** with this content: "A pair of lifts of one visible family outside
  the maximal uniform right class and differing in relating evolution exists; every such pair
  exhibited is related by a left in-fibre move, so the right class alone is not the invisible
  freedom and quotienting by it alone does not determine the relating evolution. A pair outside the
  two-sided action and differing in relating evolution exists as well, on a single visible law. The
  complete trajectory of fibre-Gram data does not fix the relating evolution either: a
  time-dependent invisible right deformation preserves every fibre-Gram matrix at every time and
  changes the relating evolution. So the two-part question above is open in both parts."
- **What is not claimed** is preserved and gains one sentence: "The fibre-Gram data is a
  coordinate on the space of lifts, not a physical quantity, and no statement is made about which
  trajectory of it is selected."
- **Prospects** is corrected forward to: "The question is sharply posed at one time and the open
  part is cross-time: the data left free at each time is known exactly, so progress would come from
  a statement about what constrains that data across times, and about what fixes the relating
  evolution within a trajectory of it." (Nothing about connections, gauge fixings or a named
  mechanism.)
- The §19.4 table row *Relative-evolution selection (framework-specific)* is corrected forward to:
  "Open — representability settled and operational completion characterized conditionally; the
  freedom the visible law leaves at one time is classified exactly by the fibre-Gram data, but no
  theorem selects that data's trajectory or the relating evolution within it; ordinary coherence
  proved insufficient".
- §19.2.12's **Two frontiers, not one.** paragraph is preserved verbatim.

### Item 4 — Glossary and mirrors

- `book/glossary.md` gains one entry, **Fibre-Gram data**, defined in manuscript voice as: for a
  coherent lift of a visible law and each visible output, the Gram matrix of the hidden states into
  which the lift sends the visible inputs; its diagonal is the visible law; two lifts are related by
  the two-sided invisible action at one time exactly when their fibre-Gram data agree up to phases;
  it is a coordinate on the space of lifts, not a physical quantity.
- `book/The-Incompleteness-of-Observation-FULL.md` mirrors every changed book passage byte for
  byte.
- `papers/GR.md` and `papers/Methodology.md` are read, not edited: their sentences ("does not prove
  that bare OI selects a unique relative quantum evolution"; "Selection of a unique relative quantum
  evolution … is **open**") remain true and are re-pinned unchanged.
- `README.md` (root) is edited only if the re-grep finds a sentence that states the combined
  target as open or turns representability into selection; otherwise it is untouched.

### Item 5 — Verification, registry and generated surfaces, in the same execution commit

- Move the act 12 census family from `kernel-only` to `current`, with manuscript anchors actually
  created by this round (Main, Explainer, Chapter 1, Chapter 19, glossary); the theorem and
  evidence scope remain exactly those of the merged result.
- Add a propagation guard `R7-A12P` (name mechanically adjusted only on collision), placed
  immediately before `# ---- R7-A6D` in `verification/lean/edge_rigidity_probe.py`, that pins this
  audit by blob, pins every frozen sentence above where it lands, and mutation-tests the principal
  over-readings: the fibre-Gram data promoted to physics; joint maximality asserted; the trajectory
  said to determine the relating evolution; a selection principle or connection named or excluded;
  the two-part question collapsed to one part or declared closed; the boundary escalated into
  inequivalence; the two-sided action called "the maximal two-sided action".
- **Amend `R7-A11P` in exactly the contracts whose pinned sentences this round supersedes, and no
  others**, in the same execution commit, with the amendment recorded in the guard's own comment:
  - `_a11p_gi2_not_a_no_go` (E4): the pinned string "can fail to be related by any uniformly
    invisible deformation and still agree on every relating evolution" is re-pinned to the new
    string "can fail to be related by any uniformly invisible right deformation and still agree on
    every relating evolution"; its second string is unchanged; mutations `m1`, `m2` follow.
  - `_a11p_stronger_target_open` (E5) and mutation `m6`: the pinned pair "outside the uniformly
    invisible class" / "is open" in Main, Explainer and Chapter 1 is re-pinned to the presence of
    "related by a left in-fibre move" **and** the two-part openness sentence in each of the three,
    with the mutation writing the second part back as settled.
  - `_a11p_frontier_target_open` (E18) and mutation `m20`: the pinned Chapter 19 strings ("outside*
    the maximal uniform class of deformations the visible law cannot see", "agrees on every relating
    evolution, so it separates the space of lifts without separating the dynamics", "the combined
    target remains open") are re-pinned to the new **What is sharper, and what it does not
    settle.** paragraph, with the mutation declaring the two-part question closed.
  - The `check('R7-A11P', …)` message is corrected where it describes the stronger combined target
    as stated open.
  - `R7-A11P`'s two blob pins (`cc6d5adb…`, `50f74a08…`) and every other contract are untouched.
- Add the round to `verification/README.md` in the existing propagation-round style, immediately
  before the paragraph that begins "`.github/workflows/verify.yml` runs".
- Rebuild every affected `.tex` / `.pdf` and the book through the canonical `build.sh` route, or
  fail the round; no source/generated mismatch is admissible; the dropped-glyph and page-count
  checks are part of the build's acceptance.
- No frozen Track B control plane, result note, Lean file, or research `ROADMAP` status is edited.

## The chronology control

- This file is merged **alone**; the execution pull request is based on exactly the merge commit of
  this control-plane pull request and is never updated from later `main`.
- `R7-A12P` pins this file's blob **by content** and certifies the execution ancestry in act 10's
  strengthened form: the real `pull_request.head.sha` in PR CI, never the synthetic merge commit;
  the base an ancestor of the head **and** every commit of `git rev-list H ^B` a descendant of the
  base; recovery performed by the guard; fail-closed.
- **Archive mode** (the rule adopted on 2026-09-13, PR #599): once the execution pull request has
  merged, the guard re-runs the same strong check against the **sealed execution head pinned by
  SHA together with its merge commit**, both required reachable from the current target,
  fail-closed. The pins are added in a follow-up that records the sealed head after exact-head
  review and merge; until then the guard runs in execution mode.

## The constraints, fixed in advance

- **Publication-only.** No Lean theorem, definition, proof, probe result, source adjudication, or
  roadmap research status is added, changed, or removed.
- **No new `P0` answer.** Neither part of the two-part question is searched for or answered here.
- **No new physical interpretation.** No statement that a connection, gauge choice, channel
  selection, or any named mechanism is sufficient or insufficient is introduced; no selection
  principle is named in either direction.
- **Joint maximality is neither asserted nor excluded** anywhere in the corpus.
- **The fibre-Gram data is a coordinate, not physics**, wherever it is mentioned.
- **Manuscript voice only.** No act numbers, theorem labels, kernel identifiers, review history,
  branch or pull-request language, or verification process in manuscript prose.
- **Correct forward, do not narrate.** Superseded wording is replaced in place.
- **Whole-corpus propagation.** Changed book passages are mirrored in the full-book source;
  generated forms are rebuilt.

## Tests, fixed in advance

**E1 — the two-sided statement.** Main, Explainer and Chapter 1 each state that the invisible
freedom has a left and a right factor, each maximal among uniform actions of its kind, and none
calls the two-sided action maximal. Admissible outcome: all three agree.

**E2 — right-only insufficiency, bounded.** Each of the three states that a pair outside the right
class can differ in relating evolution and is related by a left in-fibre move, and none states that
every gauge or connection description is insufficient. Admissible outcome: zero over-readings.

**E3 — the per-slice classification.** Main states the classification (fibre-Gram data up to
phases; the visible law its diagonal; realizability as stated) and its "per time slice" scope;
Explainer, Chapter 1 and Chapter 19 state it at their level. Admissible outcome: all.

**E4 — the two-part frontier.** Main, Explainer, Chapter 1 and Chapter 19 state both parts as open
and state that the complete trajectory does not fix the relating evolution. Admissible outcome: all
four; no surface collapses the two parts or declares either closed.

**E5 — non-licences.** No surface promotes the fibre-Gram data to a physical quantity, names or
excludes a selection principle or connection, asserts joint maximality, or escalates into
inequivalence. Admissible outcome: zero.

**E6 — three statuses preserved.** Main, Explainer, GR, Methodology and Chapter 19 still agree:
representability established; operational completion characterized conditionally; selection open.
Admissible outcome: all, with `R7-A11P`'s three-status contract passing unchanged.

**E7 — `R7-A11P` amendment scope.** Exactly the three contracts named in Item 5 are re-pinned, their
mutations follow, both blob pins are unchanged, and every other `R7-A11P` contract passes without
edit. Admissible outcome: exactly that.

**E8 — mirrors and registry.** Changed markdown, generated TeX, PDFs, full-book source, census,
verification README and guards all agree; the act 12 census family is `current` with real anchors
and no stronger status than the merged theorem. Admissible outcome: all.

**E9 — re-grep.** The execution reports corpus-wide surviving counts for "uniformly invisible",
"relating evolution", "relative evolution", "fibre-Gram", "combined target", and "is open" in the
bridge context; every survivor is classified as intended or legitimate non-target use, and no
surface still states the combined target as open. Admissible outcome: no stale contradictory
surface.

**E10 — checks.** Release gate, foundations probes, manuscript and architecture guards, census,
canonical builds and dropped-glyph checks all green; no kernel count change attributable to this
publication round. Admissible outcome: all green.

## What the round does not do

It does not prove a new theorem, close either part of `P0`, name or exclude a connection, gauge
principle or selection mechanism, assert joint maximality, promote the fibre-Gram data to physics,
revise the finite observable-law equivalence, edit any Track B control plane or result note, change
any research status in the `ROADMAP`, touch act 11's three-notion vocabulary or the quantum-bridge
scope controls, or enter Bell, H-Bell, A6 or the substratum Lemma 24.1 round.

Status: preregistered; manuscript execution follows only after this file is merged alone.
