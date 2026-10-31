# Introductory paper: preliminary audits

Working title of the proposed paper: *Observational Incompleteness: From
Deterministic Dynamics to Quantum Observations*. Its intended form is a
12–15 page introduction for physicists and mathematicians, built on the
finite observable-law correspondence of `papers/Main.md` and illustrated by a
bounded black-hole information application.

This directory holds the preliminary audits that precede any drafting. No
paper, Explainer replacement or manuscript edit is part of this stage.

## Audits

1. **Planning scope.** A planning Issue text for the paper: the question,
   scope, success criteria, dependencies and activation condition.
2. **Novelty and fidelity.** For each claim of `papers/Main.md` the paper
   would carry, in particular the correspondence `S ⟺ D ⟺ Q_fb`: the exact
   theorem, proof and retained evidence it rests on; which parts are proved
   in this repository and which apply established results (stochastic
   processes, hidden-state realizations, dilation and quantum-representation
   theorems); and the closest prior literature. The same separation for the
   black-hole application: information recovery from restricted subsystems
   and radiation, Page typicality and its assumptions. The outcome decides
   whether the paper is positioned as a research article or a technical
   perspective.
3. **Explainer content.** Whether the two items `papers/Explainer.md` names as
   not yet carried by the book (the D-gauge walkthrough and the mathematical
   summary tables of its appendix) are now present in the book, and what
   would have to be migrated before the Explainer is replaced.

## Inputs and boundaries

- Sources are read at `main` `c91bf5dd84b6415e1c59820ae0333f3b062d10b6`
  unless an audit states otherwise.
- The black-hole application uses only independently reviewed findings of
  #917 as established results; unreviewed findings are cited as open.
- An audit records what it checked and at what commit. A claim it cannot
  trace to a theorem, proof or retained evidence is listed as untraced.

## Outputs

Each audit adds its report to this directory. A later stage, separately
authorized, drafts the paper from the authoritative `papers/Main.md` and
checks it against that source for any strengthened claim.
