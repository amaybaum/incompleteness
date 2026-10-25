# Introductory paper: preliminary audit records

Scope: `PLAN.md`. Repository sources were read at `main`
`c91bf5dd84b6415e1c59820ae0333f3b062d10b6`, except PR #917, which was read at
its head `809fac52cdf207d24eccc63c734996bcb9d073a0` (not on `main`); only its
open status is drawn from it. Each audit file opens with a status block; no
verdict in either is an established result.

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
  The search scripts it used are in `explainer-tools/`; each takes one
  argument, a directory holding `Explainer.md` and `book/*.md` and
  `papers/*.md` taken at `c91bf5dd`. **Status: unreviewed.** Apart from its
  status block, it differs from the auditor's report (sha256
  `f2fedace546787037101196ebf4fd7152a7f84e00b28d857083a69c351a57685`) only in
  three scratch-directory phrases replaced by relative descriptions.
  Errata: its lines citing `tools/shingle.py` and `tools/eqs.py` mean
  `explainer-tools/`; and `papers/Explainer.md` has 41 displayed `$$…$$`
  equations, not 42 (`eqs.py` prints 41).

## Findings carried forward for separate work

- `papers/Main.md:98` displays "finite-horizon non-Markovianity ⟺ ∃ finite
  reversible hidden-state realization" as the paper's core, while
  `papers/Main.md:596-598` states that this form is false because the
  process-dilation construction also realizes Markov laws. To be examined
  and corrected in a separate, narrowly scoped manuscript correction.
- The process-dilation theorem (`papers/Main.md:496-500`) cites `S_imp_D`.
  The docstring of the class `RevReal` that `S_imp_D` targets
  (`verification/lean-mathlib/OIBridge/Equivalence.lean:150-156`) states
  that the class does not require a hidden prior independent of the visible
  initial state (`NOVELTY-AUDIT.md` attributes this docstring to `S_imp_D`).
  This bears on the Lean-to-manuscript registry (§A.35).
- `papers/Explainer.md:120`: a dark-energy paragraph is spliced into the
  Liouville-measure sentence. To be repaired in a separate minimal
  correction.
- The D-gauge material of `papers/GR.md` §3.3 that the book does not carry,
  to be migrated to book Appendix B.7 and mirrored in the full text before
  any Explainer replacement.

None of these is a manuscript change made here.

## Unresolved literature and scope questions

- Whether the recurrence-plus-readback indivisibility result (the audit's
  C8, kernel-checked in `RecurrenceHorizon.lean`) is already known.
- Every reference the novelty audit cites from memory, including the
  radiation-entropy factor β ≈ 1.48 and the bibliographic details of Hardy
  2004 and Vidyasagar 2011.
- The Page-time fraction: Page 2013's 0.5381 t_evap against
  `book/ch07-gravity.md:137-139`'s 0.646, a candidate book correction that
  stays open until its sources are checked (#917 bears on it).
- Components the audit did not examine: `papers/Main.md:624`,
  `papers/Main.md:308` and the Bell bound at `papers/Main.md:22`.
- The audit's further fidelity notes F3–F6 on `papers/Main.md`.

## Open decisions

- Final positioning of the paper (research article or technical
  perspective), after the independent review of `NOVELTY-AUDIT.md`.
- Whether the appendix summary tables are rebuilt as navigation aids.
- The Explainer's retirement, after `papers/Introduction.md` is accepted,
  with its CI probe, census registry, coverage ledger and cross-references
  changed together.
