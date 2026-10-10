# Wave 2 read-only threads N, O, P, R — common limits (owner direction, 2026-10-02)

Certified base: main = L = f7f5c3b0c621cc3e4b57e3709d11d9d580c81149 (OG-1 landed: OIBridge/OrbitGeneration.lean,
OIBridge/OrbitNormalization.lean). Each thread has its own detached worktree wave2/wt-<X>-*/ at exactly L.

1. Read-only against L. Inspect, compute and draft only. Write only inside wave2/<X>/ (outside the worktree).
2. No branches, PRs, commits, pushes, freezes, round records, receipts, ROADMAP or manuscript edits, GitHub writes.
3. No new axiom or premise to make a proof go through; every hypothesis is named and listed, never hidden.
4. A failed implication gets the smallest explicit countermodel (exact arithmetic where numeric) and the named
   missing premise.
5. Evidence levels are kept apart: kernel (a landed identifier, checked at L with file:line), exact (a script in the
   thread directory, exact arithmetic, replayed), written (an argument), citation (literature). "Proved" needs a
   landed kernel identifier. Written arguments are never presented as kernel results.
6. Do not run Lean/lake (the kernel runs in CI only). Python with exact arithmetic (fractions/sympy) only;
   PYTHONDONTWRITEBYTECODE=1.
7. Isolation: do not read the other wave-2 thread directories. Earlier threads (scratchpad/threads/F..M) may be read
   as background, but every claim used must be re-verified against the tree at L.
8. Gem-finding discipline (AGENTS.md §A.31): fix a productivity test before starting; walk the question depth-first;
   apply maximum skepticism to any branch whose outcome favours the framework; classify output NEW / POSITIVE /
   ELABORATING / CONFIRMING / BORDERLINE.
9. Deliverable (required before any preregistered round may be opened on the topic):
   (a) a candidate theorem statement, typed against the landed vocabulary (KInfFoundations, OrbitGeneration,
       OrbitNormalization), with every hypothesis named;
   (b) its dependency chain down to landed identifiers, named open premises, or genuinely missing implications;
   (c) a countermodel / circularity audit: for each hypothesis, a model where it fails and what breaks; and an
       explicit check that no step imports the conclusion (in particular, nothing may take dimension 3 from NB-1,
       and nothing may take the drive from elementaryDrivability_of_substratum-style routes already refuted).
   Write RESULT.md plus NOTES.md and scripts; if writing RESULT.md fails, put the full report in the final message.
10. Leave the worktree in place (the coordinator removes it).
