# Parallel research threads — protocol (owner, 2026-10-01)

**Parallel research, serialized certification.** Threads A–E may inspect, compute, draft candidate statements and
find countermodels. They may NOT: freeze definitions, open or prepare governed rounds, create branches, push,
dispatch CI, comment on GitHub, or edit any authoritative state (ROADMAP, manuscripts, verification records).
Lean runs only in CI, so threads do no Lean builds; Lean text they draft is a candidate only.

- Base: landed main, read-only worktree `scratchpad/wt-threads` (detached). Never write inside it.
- Each thread writes only under `scratchpad/threads/<X>/`.
- Exact arithmetic only for any claimed identity, rank or sign (Fractions / Q(√3) / sympy exact). Floating point is
  allowed only as exploration and must be labelled so.
- Every favourable finding gets a countercontrol (AGENTS.md §A.31: maximum skepticism on favourable branches).

**Merge rule.** Each thread returns `scratchpad/threads/<X>/RESULT.md` with exactly these sections:
1. Finding — one paragraph.
2. Evidence level — written / exact computation (script + output) / literature, per claim.
3. Countermodels and controls — what was run against the finding, and what it showed.
4. Proposed next theorem — exact statement(s), with the layer each belongs to (Lean / exact / written).
5. Dependencies — on other threads, on corpus declarations (file:line), on unsourced premises.

Only after all five return does the owner decide what enters the successor foundations freeze.
