# Changes r14 → r15

r15 applies the exact-commit landing review of r14 (`review/scientific/LANDING-REVIEW-r14.md`, REVISE minimal). It is
generated from r14 by `draft/scripts/build_r15.py`. The edits are exact replacements with stated counts; every other
sentence is byte-identical to r14.

| # | Finding | Old | New |
|---|---|---|---|
| L1 | §2.4's readback bound: the hypothesis as Main:167 states it at `b64919cd`, a common present state and joint probabilities | "If two visible histories of length $k$ with a common endpoint, each of probability at least $p_0$, induce" | "If two values of $X_{<k}$ followed by a common present state $X_k$, each of joint probability at least $p_0$, induce" |
| L2 | The corpus is repinned to `b64919cd`, where Main §2.3 carries the matching wording. Every other cited pointer reads as at `c967d6a9`, and the Lean sources are identical (2 sites: the Code section and the Corpus entry). | "`c967d6a9`" | "`b64919cd`" |
| L3 | The provenance comments use full repository paths, since the paper lands under `papers/` (7 sites; not typeset) | "(draft/review/references/" | "(verification/audits/manuscript/introductory-paper-20261025/draft/review/references/" |

## Build and checks

The landing tree is `papers/Introduction.md` = r15, together with the ledger rows, the README entry and the
`build.sh` count:
- 17 pp, main text through p. 12, with "Code, data and formal verification" at the top of p. 13. No dropped glyphs.
- `tools/release_gate.py`: every step passes except `lean-axioms`, which needs `lake` and runs in CI. That includes
  `coverage` with 133 statements, the five new Introduction rows among them, plus `legacy-records`, `v3-corpus`,
  `v3-receipts` and `citation-roles`.
- The proof census fingerprints of the five statements are unchanged from r14.
