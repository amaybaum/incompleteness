# Introductory paper: preliminary audit records

Scope: `PLAN.md`. All sources were read at `main`
`c91bf5dd84b6415e1c59820ae0333f3b062d10b6`.

## Records

- `NOVELTY-AUDIT.md`: novelty and fidelity of the central correspondence
  `S ⟺ D ⟺ Q_fb` and of the black-hole application. **Status: unreviewed.**
  Its classification of each component against prior literature, and its
  recommendation to position the paper as a technical perspective, are
  provisional until an independent review compares the actual theorem
  statements and proofs. Its literature tags mark which references it could
  confirm and which it cites from memory. No full text could be opened.
  References cited from memory are unverified.
- `EXPLAINER-AUDIT.md`: what replacing `papers/Explainer.md` would lose,
  what is stale there, and what a replacement must change in the same commit.
  The search scripts it used are in `explainer-tools/`. **Status:
  unreviewed.** Its scratch-directory paths are replaced by relative
  descriptions; nothing else differs from the auditor's report.

## Findings carried forward for separate work

- `papers/Main.md:98` displays "finite-horizon non-Markovianity ⟺ ∃ finite
  reversible hidden-state realization" as the paper's core, while
  `papers/Main.md:596-598` states that this form is false because the
  process-dilation construction also realizes Markov laws. To be examined and
  corrected in a separate, narrowly scoped manuscript correction.
- The process-dilation theorem (`papers/Main.md:496-500`) cites `S_imp_D`,
  whose docstring (`verification/lean-mathlib/OIBridge/Equivalence.lean`)
  states that its class does not require a hidden prior independent of the
  visible initial state. This bears on the Lean-to-manuscript registry
  (§A.35).
- `papers/Explainer.md:120`: a dark-energy paragraph is spliced into the
  Liouville-measure sentence. To be repaired in a separate minimal
  correction.
- The D-gauge material of `papers/GR.md` §3.3 that the book does not carry,
  to be migrated to book Appendix B.7 and mirrored in the full text before
  any Explainer replacement.

None of these is a manuscript change made here.

## Open decisions

- Final positioning of the paper (research article or technical
  perspective), after the independent review of `NOVELTY-AUDIT.md`.
- Whether the appendix summary tables are rebuilt as navigation aids.
- The Explainer's retirement, after `papers/Introduction.md` is accepted,
  with its CI probe, census registry, coverage ledger and cross-references
  changed together.
