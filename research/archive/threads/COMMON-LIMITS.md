# Common limits for Threads I–L (owner direction, 2026-10-01)
1. Read-only against certified main = 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a (own detached worktree under the thread's dir).
2. Inspect, compute and draft only. Write only inside the thread's own directory threads/<X>/ (outside wt/).
3. No branches, PRs, commits, pushes, freezes, round records, receipts, ROADMAP or manuscript edits, GitHub writes.
4. No new axiom or premise to make a proof go through; hypotheses are named and listed, never hidden.
5. Failed implication ⇒ smallest explicit countermodel (exact arithmetic) and the named missing premise.
6. Written arguments are never presented as kernel results; "proved" needs a landed kernel identifier.
7. Do not run Lean/lake (kernel runs in CI only). Python with exact arithmetic only; PYTHONDONTWRITEBYTECODE=1.
8. ISOLATION: do not read other threads' I/J/K/L directories. Threads F, G, H outputs (threads/F, G, H) may be read
   as background, but every claim used must be re-verified against the tree.
9. Deliverable file RESULT.md plus running NOTES.md and scripts; if writing RESULT.md fails, put the full report in
   the final message.
10. Remove the worktree at the end: git -C /home/user/incompleteness worktree remove --force <path>.
