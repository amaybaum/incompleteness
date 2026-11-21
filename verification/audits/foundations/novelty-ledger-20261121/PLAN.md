# NOVELTY-LEDGER — plan

Issue #1525; owner scope #1169 c.7067233614, start c.7067281228. Drafting snapshot `D` = `main` at
`df6da1c6`. Read-only with respect to the manuscripts; no computation is run.

## Units

1. **U1 — S ⇔ D ⇔ Q_fb** (Main:18, Main:80, Main:556–562) against random-mapping and functional
   representations, Egri–Gömöri–Gyenis–Hofer-Szabó (arXiv:2602.23491) and Barandes
   (arXiv:2302.10778, 2309.03085, 2608.04354).
2. **U2 — hidden memory, capacity, P-indivisibility** (Main §2.3, Main:514–534, Main:614–634) against
   data processing, Rivas–Huelga–Plenio, Buscemi–Datta, Milz et al., Doukas (arXiv:2602.22095) and
   computational mechanics.
3. **U3 — Theorem 23** (Substratum §3.1–§3.6, SM §4–§8.3) against dimension-selection arguments,
   lattice gauge theory, staggered fermions, anomaly-fixed hypercharges and emergent gravity.

## Method

Read the cited manuscript text and Lean statements at `D`; read each external source at its
arXiv or publisher page; record every citation with its locator and mark what was not read.
Classify each claim on five columns: mathematical priority, stronger assumptions, stronger
conclusions, formal verification, physical novelty. Use (N)/(I) only where the ledger restates an
existing classification; it introduces none.

## Productivity test (fixed before writing)

The ledger is productive iff, for at least one claim per unit, it identifies with a checkable
citation either (a) an earlier or concurrent source proving the same or a stronger statement, or
(b) a precise respect in which OI's statement is strictly stronger than the nearest source
(weaker hypotheses or a stronger conclusion). A unit where neither can be established with a
read source is recorded as INCONCLUSIVE for that unit. Restating the manuscripts' own
self-attribution without an independent check does not count.

## Invariant → checkpoint

| Invariant | Checkpoint |
|---|---|
| No manuscript file changes | `git diff --stat main -- papers book` empty at each commit |
| Every external citation has a locator and a read/unread mark | ledger §6 source table |
| Nothing is placed at the `verification/` root | path of this directory |
