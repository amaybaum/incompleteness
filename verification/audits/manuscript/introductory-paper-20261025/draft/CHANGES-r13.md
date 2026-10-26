# Changes r12 → r13

r13 applies the two nits of the independent confirmation of r12 (`review/scientific/CONFIRM-r12.md`: ACCEPT WITH
NITS, all ten findings of the final scientific review confirmed). It is generated from r12 by
`draft/scripts/build_r13.py`: two exact, uniquely matching replacements; every other sentence is byte-identical to r12.

| # | Finding | Old | New |
|---|---|---|---|
| W1 | Theorem 4's discard clause could be read as dropping the outcomes; the kernel keeps them (`prepAvail_discard`; the "if" direction uses `avail_iff_availExt_one`, LevelOneSeam:128) | "with the ancilla then discarded, is an available operation on the system [GR §3.3]." | "with the ancilla then discarded, is an available instrument on the system with the same outcomes [GR §3.3]." |
| W2 | The paper names two commits without saying why | "at commit 17b830bc…, by building" | "at commit 17b830bc…, whose Lean sources are identical at the corpus commit `c967d6a9`, by building" |

W1 states a hypothesis exactly; W2 is in the Code section, after the main text.

## Build and checks

- 17 pp; 0 overfull boxes; 0 missing glyphs. "Code, data and formal verification" starts at the top of p. 13, so the
  main text stays within 12 pp.
- `voice_check`, `claims_check` and `duplicate_check` are OK on a fresh `git archive c967d6a9` with r13 as
  `papers/Introduction.md`.
- No Lean identifier, citation, bibliography entry or marker changes; 0 OWNER and 4 VERIFY markers. Weinberg 1989
  remains the open landing gate (owner, 2026-10-26).
