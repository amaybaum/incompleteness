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

- `novelty-v5/`: revision 5 of the novelty and fidelity audit, now r4,
  read at `main` `83d1da1b`. **Status: work-in-progress evidence record.**
  - r1 was independently reviewed (BLOCK, on wording only), and r2 was
    re-checked (ACCEPT WITH NITS). r3 applied those nits.
  - r4 re-bases the audit after #925–#928 and adds a first-hand
    full-text literature reading. It has had no separate review.
  - For drafting it supersedes `NOVELTY-AUDIT.md`.
  - `novelty-v5/README.md` summarizes its source-coverage limits,
    attribution corrections and the manuscript defects it records.

## Findings carried forward for separate work

These were recorded at `c91bf5dd`. Their status at `main` `52e2db40` was
verified for this list; the fidelity notes are tracked in
`novelty-v5/AUDIT.md` §4.

- **Fixed by #922.**
  - `papers/Main.md:98` displayed "finite-horizon non-Markovianity ⟺ ∃
    finite reversible hidden-state realization" as the paper's core.
  - Main:98–99 now display {finite-horizon visible laws} = {visible
    marginals of finite reversible hidden-state systems}, "that is
    $S \iff D$, Markov laws included, so the existence of a realization
    does not distinguish non-Markovian laws" (novelty-v5 F1).
- **Resolved by #922.**
  - The issue: the process-dilation theorem (`papers/Main.md:496-500`)
    cited `S_imp_D`, whose class `RevReal` does not require a hidden
    prior independent of the visible initial state.
  - Main:500 now cites `S_imp_D` only for the realization from an initial
    law "that may correlate the hidden and visible coordinates". It states
    that the independence of $\mu_H$ "is not formalized".
  - The `RevReal` docstring and the comment at `Equivalence.lean:346–351`
    say the same (novelty-v5 F2, F2b).
- **Fixed by #919.** The dark-energy paragraph spliced into the
  Liouville-measure sentence at `papers/Explainer.md:120` is present at
  `a411bf46^1` and absent at `a411bf46`. The paragraph is now
  Explainer:115, "Where the Liouville measure comes from".
- **Done by #921.** The D-gauge material of `papers/GR.md` §3.3 is in book
  Appendix B.7 ("Bohr frequencies and the D-gauge classification",
  appendix-b:432; Theorem B.7.5c, :444).

None of these is a manuscript change made here.

## Unresolved literature and scope questions

These were recorded at `c91bf5dd`; current status as stated.

- **Classified.** The recurrence-plus-readback indivisibility result (C8)
  is KNOWN: Buscemi–Datta Prop. 1, and Rivas–Huelga–Plenio 2014 Thm 2.4
  (novelty-v5 C8).
  - Its step from history-level C4 is still argued in prose.
  - The open novelty question is now the rooted classification C8-R,
    novelty unverified (novelty-v5 C8-R, §5 P1).
- **Partly resolved.** References the original audit cited from memory.
  - The radiation-entropy factor is now stated at GR:863 and ch07:143 as
    "β ≈ 1.485 and t_P ≈ 0.538 t_evap", cited to Page [60]. novelty-v5
    classifies the Page-time formula and β > 1 on Page 2013 and 2005 in
    full text (C16a, C16b). The value 1.485 itself was not re-checked.
  - Hardy 2004 is still unread.
  - Vidyasagar 2011 is still unread, behind a paywall (novelty-v5 §0.2).
- **Resolved by #920.** The Page-time fraction (Page 2013's 0.5381
  against ch07's 0.646).
  - ch07:137–143 now gives $t_P/t_{\mathrm{evap}} = 1-(\beta/(1+\beta))^{3/2}$,
    "0.646 at β = 1", with Page 2013 cited (novelty-v5 C16a).
- **Still not examined.**
  - `papers/Main.md:308`.
  - The Bell bound at `papers/Main.md:22`. novelty-v5 cites :22 only as
    F4's context.
  - `papers/Main.md:624`. novelty-v5 cites it only as part of the
    interpretation (e).
- **F3–F8 on Main, and F9 on ch07 §7.6.** Current statuses, with fixing
  commits, are in `novelty-v5/AUDIT.md` §4.
  - F6 and F9 are fixed.
  - F3, F4, F5 and F8 are partly fixed.
  - F7 is open.

## Open decisions

- Final positioning of the paper (research article or technical
  perspective). `novelty-v5/AUDIT.md` §7 recommends a technical
  perspective or pedagogical review.
- Whether the appendix summary tables are rebuilt as navigation aids.
- The Explainer's retirement, after `papers/Introduction.md` is accepted,
  with its CI probe, census registry, coverage ledger and cross-references
  changed together.
