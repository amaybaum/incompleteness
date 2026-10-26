# Exact-commit landing review of Introduction r14

**Object.** `Introduction-r14.md` at `9925f683` (#918). The reviewer was the Introduction's final scientific referee. The
review was read-only, on a full extraction of the tree at that commit, with the landing simulated in scratch. The
coordinator wrote this record from the referee's report, because the referee's tool refused report files.

**Verdict: REVISE (minimal).** Line 84 needs one clause changed to match the readback lemma as Main:167 states it at
`b64919cd`. After that, the draft is ACCEPT FOR LANDING, provided the landing commit adds the five coverage-ledger
rows below.

## 1. r13 → r14

- `build_r14.py` applied to r13 reproduces `Introduction-r14.md` byte for byte. Its diff is exactly G1 and G2.
- G1 matches the Weinberg reviewer's Option A: the VERIFY marker is removed, the citations are placed as proposed,
  and the cutoff-convention clause is uncited. G2 places [Wei89] after [Vol06].
- `review/references/WEI89.md` records the reading accurately, with short quotations only.
- No PDF is in the audit tree: `git ls-tree -r 9925f683 -- verification/audits` lists 0 `.pdf` files.

## 2. Lean names at `9925f683`

- `git diff --stat 17b830bc 9925f683 -- verification/lean verification/lean-mathlib` is empty, so the Lean pin still
  holds.
- All 28 Appendix A declarations resolve. Each stated module:line holds a `theorem` or `def` of that name, declared
  once in that module, with 0 failures.
- `permMatrix_mem_unitaryGroup` is also declared elsewhere in `OIBridge`, but Appendix A names the module
  (EquivalenceChain:179), and that one is correct.
- The 9 identifiers cited in the text are a subset of the 28.
- No gate checks these names for this paper: `lean_manuscript_census.py` resolves only `(kernel: …)` spans, and the
  paper has none. This check is therefore the paper's Lean-name verification.

## 3. Landing simulation

Simulated with r14 as `papers/Introduction.md` and built with `sh ./build.sh Introduction`:
- 17 pages, 0 missing glyphs, 0 overfull boxes;
- the main text ends on p. 12, and "Code, data …" starts at the top of p. 13.

Every release-gate step that can run without git history or lake passes, except `coverage`. It fails on 5 statements
with no ledger row: `INTRODUCTION:T-1` (:48), `T-2` (:74), `C-unnamed-b596be8a` (:82), `T-3` (:92) and `T-4` (:116).

The landing commit must therefore:
- copy the final draft to `papers/Introduction.md`, byte-identical;
- build `.tex` and `.pdf` with `build.sh` only;
- add the five ledger rows on the Explainer precedent (`area: mirror`, `kernel: MIRROR`). T-3 restates the kernel's
  rooted form, not Main §2.3's printed theorem, and the Corollary mirrors Main §1.5, which has no row of its own; the
  notes name those sources.

It is recommended to:
- add a README index entry;
- update `build.sh`'s paper count;
- give the provenance comments full repository paths, because relative `draft/…` paths dangle under `papers/`.

The full release gate, with `lean-axioms`, `legacy-records`, `v3-receipts` and `citation-roles`, runs on the landing
head in CI.

## 4. Corpus pointers at `b64919cd`

#938 changed `papers/Main.md` (lines 167 and 170), `papers/Explainer.md`, `book/appendix-b-derivations.md` and their
FULL lines. Of these, the paper cites only Main.

**r14 line 84 (blocking).** "If two visible histories of length $k$ with a common endpoint, each of probability at
least $p_0$, …" reads literally with the endpoint inside the history, which shifts the index against $X_k$. It also
admits a marginal reading of the probability, and with a small joint probability the bound fails. Main:167 at
`b64919cd` states the hypothesis with values of $X_{<k}$ followed by a common present state $X_k=c$, each of joint
probability at least $p_0$.

**Minimal fix:** "If two values of $X_{<k}$ followed by a common present state $X_k$, each of joint probability at
least $p_0$, induce …". Optionally, repin the corpus to `b64919cd`; the Lean tree is identical.

Every other pointer the paper cites reads the same at `b64919cd`.
