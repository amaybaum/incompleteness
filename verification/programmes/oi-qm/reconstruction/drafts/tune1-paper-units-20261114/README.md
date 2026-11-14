# TUNE-1 paper-only units of 2026-11-14 (#1236)

Work in progress, published under AGENTS.md §A.43. Research drafts: paper-only, model-reviewed, not
independently verified, not adopted. They change no manuscript claim and no scientific status.

**Authorization.** The owner authorized two paper-only units on #1236 (comment 6874529744,
`amaybaum`, 2026-11-14): "I authorize steps 2 and 4 as paper-only work". Step 2 is a derivation on
gap L5.4; step 4 is the specification of one non-linear candidate. Paper-only means hand reasoning
and the repository's check scripts: no computation on OI rules was run.

## `nlcand/`: one non-linear candidate (step 4)

The candidate is the ring rule of `papers/SM.md` §3.1 as written, completed with a law, an observer,
labels and setting generators, and analysed by hand against three requirements: control, Bell
parameter dependence without signalling, and supply of known-value cells. The hypothesis that the
world's rule is this ring rule is written H-ring in r3 and is unadopted. It is not TUNE-1's H-nl,
which names the rounded rule of `papers/SM.md`:294.

| File | What it is |
| --- | --- |
| `SUMMARY-r3.md` | Plain-language summary of r3 |
| `NLCAND-r3.md` | The final text |
| `NLCAND-r2.md` | The revision the confirmation review read |
| `NLCAND-r1.md` | The first draft, which the review read |
| `NOTES-r1.md` | The writer's reading list and what was not checked |
| `REVIEW-r1.md` | Non-author review of r1: REVISE |
| `RESPONSE-r1.md` | Dispositions of the review's findings and of the confirmation review's edits |
| `CONFIRM-r2.md` | Confirmation review of r2: ACCEPT WITH CHANGES |

**Review status, exactly.**

- `REVIEW-r1.md` re-derived the rule quotation, bijectivity and the inverse, the directed cone and
  the signalling computations by hand and returned REVISE on verdict strength and scope. r2 applies
  its findings (`RESPONSE-r1.md`).
- `CONFIRM-r2.md` confirmed r2 and asked for five wording edits, N1–N5, with exact text and no
  change to any verdict.
- r3 applies all five edits as written; the verdicts of r2 are unchanged. Beyond N1–N5, r3 differs
  from r2 in the title and status paragraph, the review row of the reference table, one sentence in
  §8 and a closing "Not included" line. `diff NLCAND-r2.md NLCAND-r3.md` shows every change (13
  hunks).
- r3 itself has not been reviewed. Neither review is independent verification, a human review or an
  owner decision.

**Scope.** Every verdict is for the one candidate analysed. Nothing here is a statement about the
non-linear class, about H-ring or H-nl as hypotheses, or about H-Bell. Several results depend on the record convention
(complete-history records against the single-time readout of `papers/Main.md`:369–372); r3 states
which hold under which.

## Names used in the files

The reviews name the checkouts they read. They resolve as follows.

| Name in the files | Content |
| --- | --- |
| `wt-mainread` | `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` |
| `wt-3a` | branch `research/tune1-step3a-1236-20261113` at `8228b3c24e17a17f324b6779b53b04ad296b4308` (off `main`) |
| `wt-tune1plan` | branch `records/tune1-landing-plan-1236-20261114` at `ea9bff9c2f2f0f238db66690073868e281e43501` (off `main`) |
| `wt-bell` | branch `research/bell-ladder-868-20261113` at `d8e4f80e71b64972ee3e87a874544c8bd358d5c2` (off `main`) |

## To be added

The L5.4 unit (step 2) joins this directory as `l54/` when its confirmation review returns, with
its own review trail and scope.
