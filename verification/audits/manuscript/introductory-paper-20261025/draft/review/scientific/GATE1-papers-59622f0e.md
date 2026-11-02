# Gate 1 (scientific accuracy): PR #918 r27 at `59622f0e`

**Verdict: ACCEPT.** All four points check out against `git diff 90705d41 59622f0e` and CHANGES-r27.md.

1. **No scope is lost.**
   - The only words removed are "It compares starting conditions under one fixed rule." (L130).
   - The paragraph split at L138/L140 is verbatim: joining the two new paragraphs reproduces r26's L138 exactly.
   - "Precisely:" became "Stated precisely:". The full-support scope clause after it is unchanged: "for the rooted family, with a hidden prior shared by every root and drawn independently of it and with a full-support visible prior, failure of P-divisibility on {0,…,L} is equivalent to M_k>0 at some order k<L".
   - Every exact statement is untouched.

2. **The fixed-rule point survives** in L130's merged sentence: "The comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain, and it means something only because the face-down card is dealt the same way whichever card is face up". The per-root deal remains the excluded contrast ("two different deals, not one rule started in two ways").

3. **The ledger lines match the census.**
   - T-3 moved 140→142, and Theorem 3 is at L142.
   - C-recurrence-cycle-indivisibility moved 146→148, and the Corollary is at L148.
   - T-4 moved 220→222, and Theorem 4 is at L222.
   - Only `line` fields changed, so no ID is retired.

4. **`coverage_check` reports OK** at `59622f0e` (134 canonical statements). I ran it in a detached worktree, which is now removed.

Nothing is weakened.