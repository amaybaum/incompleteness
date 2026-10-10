# EQ threads A–E — research-only protocol (owner request, 2026-10-08)

Target, kept as two separately witnessed directions (AGENTS.md §A.34):

- **Forward:** OI + independently justified operational principles ⇒ finite-dimensional complex quantum theory.
- **Converse:** every finite-dimensional complex quantum model satisfies OI and every principle the forward direction
  uses, in the scope in which that principle is stated.

**Parallel research, serialized certification.** Threads may inspect, compute, draft candidate statements and find
countermodels. Nothing they produce is adopted, frozen or governed. A proposed formal round returns to the owner for
separate review.

## Limits (all threads)

1. **Base:** certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, extracted read-only at `scratchpad/eq/base/`
   (hash manifest `scratchpad/eq/base.manifest.sha256`). Never write inside it. History only through read-only git
   (`git -C /home/user/incompleteness show|log|cat-file|grep <rev> ...`); no git command that writes (checkout,
   worktree, branch, commit, stash, reset, fetch, push, gc, tag).
2. **Write only inside `scratchpad/eq/<X>/`.** Never modify `/home/user/incompleteness`, another thread's directory, or
   any earlier ledger in `scratchpad/`.
3. **No** branches, PRs, commits, pushes, CI dispatch, freezes, round records, receipts, ROADMAP or manuscript edits,
   GitHub writes or comments, artifact publishing, premise adoption. Do not spawn further agents.
4. **No Lean/lake.** There is no local toolchain; the kernel runs only in CI. Lean text drafted here is a candidate,
   labelled UNBUILT. "Kernel-proved" requires a landed identifier at `bcbc516f`, cited `file:line`.
5. **Exact arithmetic** (Fractions, sympy exact, exact algebraic numbers) for every claimed identity, rank, sign or
   inequality certificate. Floating point only as labelled exploration evidence; it certifies nothing.
6. **No hidden premises.** Every hypothesis is named. A failed implication is answered by the smallest explicit
   countermodel, checked exactly, and the named missing premise.
7. **Depth-first** (§A.12, §A.31): fix a productivity test before starting; walk one avenue to a result or a genuine
   wall before pivoting; number the branch nodes and record a verdict at each.
8. **Controls.** A computational verdict prints only over green controls. Every favourable branch gets maximum
   skepticism and a countercontrol (§A.31). A probe's sign can be an artifact (§A.21).
9. **The converse test.** Every proposed principle is checked against ordinary finite-dimensional complex quantum theory
   in its stated scope (it must hold there), and against at least one non-quantum foil (classical, real or quaternionic
   quantum theory, gbit/boxworld, polygon theories) to show what it excludes. A principle that fails in quantum theory
   is reported as incompatible, not repaired silently.
10. **Literature before closure** (Step 4 of the audit method): name the known results that bear on the question.
    Theorem numbers not checked against the source are labelled unverified.
11. **Prior work.** Read the listed earlier ledgers first (§A.19). They are off-repo research, not kernel results:
    reuse them, re-verify any claim you rely on, and do not redo settled work. Do not read other EQ threads'
    directories. The balanced-NOT question (whether frame, relT and two-sided positivity select the dimension for a
    NOT with equal eigenspaces) is owned by a separate thread; do not work on it.
12. `PYTHONDONTWRITEBYTECODE=1`; scripts and outputs stay in the thread directory and must replay deterministically.

## Deliverable

`scratchpad/eq/<X>/RESULT.md`, plus a running `NOTES.md` and the scripts, with exactly these sections:

1. **Finding** — one paragraph.
2. **Evidence level** — per claim: kernel (landed identifier) / exact computation (script + output) / written proof /
   literature (verified or unverified).
3. **Countermodels and controls** — what was run against each finding and what it showed.
4. **Proposed next theorem(s)** — exact statements, each with its layer (Lean / exact / written) and the direction
   (forward / converse) it serves.
5. **Dependencies** — on other threads' targets, on corpus declarations (`file:line` at `bcbc516f`), and on unsourced
   premises.
6. **Classification** — for each question the thread was given: THEOREM ROUTE / INDEPENDENT PREMISE (named, with the
   countermodel showing independence) / COUNTEREXAMPLE / OPEN (with the named wall).

If writing `RESULT.md` fails, put the full report in the final message.
