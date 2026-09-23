# Act 11 scope propagation — append-only open-frontier amendment

Owner-directed scope expansion to the publication-only Act 11 propagation round. The original freeze
`verification/audits/foundations/act11-scope-propagation-audit.md` remains unchanged and authoritative
for its original surfaces. This amendment is append-only and is committed before any newly authorized
manuscript surface is edited.

## Why this amendment exists

The original round correctly propagates the representability-versus-selection distinction into Main,
the Explainer, Chapter 1, the glossary and the maintained summary surfaces. A subsequent owner review
identified one further publication-level requirement: the **remaining dynamical-selection gap must
also be named explicitly as an open frontier**, not only implied by local scope remarks.

This is not a new mathematical result. It is a status-propagation clarification of the already merged
Act 11 outcome:

- finite observable-law representability remains exact: `S ⇔ D ⇔ Q_fb`;
- ordinary coherent lifting does not uniquely select the relative unitary evolution;
- the operational completion theorem remains a conditional characterization of exact finite
  operational QM under explicit added principles;
- bare OI does not yet supply a theorem selecting the unique relative quantum evolution;
- the stronger combined target — same visible family, outside the maximal uniform weak class, and
  different relative evolution — remains open;
- nothing here says that a connection or gauge principle is sufficient or insufficient.

## Added manuscript surfaces

### A1 — Chapter 19: make the selection gap an explicit framework-specific open problem

Update `book/ch19-open-problems.md` and its FULL-book mirror so that the chapter inventory explicitly
records the OI–QM dynamical-selection frontier.

The clean placement is a framework-specific open-frontier entry in §19.3, so the standard external
open-problem tally is not altered. The entry must state:

1. the finite-law bridge is solved at the level of exact representability;
2. exact finite operational QM is already characterized conditionally by the explicit completion
   principles;
3. the still-open bare-OI question is whether and how one relative quantum evolution is selected from
   the coherent lifts compatible with one visible OI family;
4. Act 11 proves that ordinary coherence is not enough;
5. the current non-weak-gauge witness does not separate the relative evolutions, so the stronger
   combined target remains open;
6. no candidate selection mechanism is endorsed.

Cross-link §19.2.12 so its split-status Born/operational discussion does not leave the impression that
only the operational-instrument completion remains open. It should distinguish the two frontiers:
conditional operational completion versus bare-OI dynamical selection.

Update the §19.1 inventory prose and the §19.4 summary table only as needed to make the new
framework-specific item discoverable without changing the count of canonical standard open problems.

### A2 — Main: name the selection issue explicitly as an open frontier

The scope remark already says representability is not selection and that the stronger target is open.
Add only the publication-level status sentence needed to make this unmistakably an **open frontier of
the OI–QM bridge** rather than a local technical caveat. No new theorem or mechanism is introduced.

### A3 — Explainer: mirror the open-frontier status

At the explanatory OI–QM bridge summary, state in plain technical language that the remaining bare-OI
question is the selection/uniqueness of relative quantum evolution, while finite-law representability
is settled and finite operational QM is characterized conditionally by the added principles.

### A4 — GR: keep the completion theorem and the bare-OI selection frontier distinct

Where GR states the quantum-complete OI / operational-completion theorem, add the bounded sentence that
this theorem characterizes the completed theory but does not prove that bare OI selects a unique
relative evolution. The selection frontier remains the separate open question identified in Main.

### A5 — Methodology: update the project-status synthesis

Where Methodology summarizes what the OI–QM programme has established, distinguish:

- exact finite-law representability — established;
- finite operational completion under explicit added principles — characterized;
- unique relative-evolution selection from bare OI — open.

No other paper is edited merely for symmetry. `Substratum`, `Structure`, `Complexity`, and applied
papers change only if a re-grep finds a sentence that itself summarizes the OI–QM bridge in a way that
would contradict these three statuses.

## Generated and verification surfaces

The newly changed paper/book markdown must be mirrored into generated `.tex` and rebuilt `.pdf`
artifacts through the canonical build route. The full book source/PDF must be rebuilt.

Extend `R7-A11P` only as necessary to pin:

- Chapter 19's explicit dynamical-selection frontier;
- the paper-level three-status synthesis;
- the stronger combined target remaining open;
- absence of claims that the gap proves OI/QM inequivalence, requires non-gauge structure, or rules
  out a connection/gauge resolution.

The Act 11 census family remains `current`; add anchors only if required by the registry contract.
No kernel file, theorem, proof, probe result, Track B result, ROADMAP research status, D3/D5 status,
or Bell/locality result changes.

## Tests

**A-E1 — Chapter 19.** The chapter explicitly contains the framework-specific relative-evolution
selection frontier and preserves the canonical external open-problem tally.

**A-E2 — three statuses.** Main, Explainer, GR, Methodology and Chapter 19 all agree on:
`representability established / operational completion conditionally characterized / bare-OI relative
selection open`.

**A-E3 — stronger target.** The same-visible + outside-weak-class + different-relative-evolution
target remains explicitly open wherever the frontier is stated at full strength.

**A-E4 — forbidden inferences.** Zero manuscript claims that Act 11 proves OI and QM inequivalent,
that the missing structure must be non-gauge, that a connection cannot suffice, or that the current
GI2 witness changes relative evolution.

**A-E5 — mirrors/builds.** Markdown, generated TeX, PDFs and full-book mirrors agree; canonical builds
and dropped-glyph checks are green.

**A-E6 — publication-only.** Kernel named-result count and research ROADMAP status are unchanged.

## What this amendment does not do

It does not answer the selection problem, choose a physical principle, alter the completion theorem,
change `S ⇔ D ⇔ Q_fb`, claim uniqueness is impossible, or expand the research programme. It only makes
the already-settled boundary visible in the manuscript's open-frontier inventory and paper-level
status summaries.

Status: amended scope frozen; execution on these added surfaces follows only after this file exists as
its own commit.
