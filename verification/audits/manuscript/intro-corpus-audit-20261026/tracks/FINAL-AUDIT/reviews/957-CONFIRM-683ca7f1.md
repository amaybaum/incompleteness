CONFIRM: #957 at `683ca7f1` is correct, and no "T/map selects" claim without the premise survives in the corpus.

1. **Scope.** `683ca7f1` is a single-parent child of `9eff10d3`. The markdown diff touches only SM :134, SM :1418, ch19 :240 and :246, and FULL :5400 and :5406. The other files changed are the regenerated SM and FULL `.tex` and `.pdf`. Main and the ledger are untouched.

2. **Each change is correct.** In every site the selection of n is now attributed to the horizon partition, and the boost exclusion to the map under the premise:
   - SM :134: "the horizon partition defining the trace-out selects a rest frame and the trace-out yields…"
   - SM :1418: "the horizon partition defining the observation map selects … and that the map excludes boosts when it determines the horizon foliation"
   - ch19 :246 / FULL :5406: the same split as SM :1418.
   - ch19 :240 / FULL :5400: "the horizon partition defining it distinguishes a temporal direction". The sentence before it, "The observation map therefore makes contact with boost structure", is fine, because "makes contact" claims no invariance.

3. **The four sites left unchanged are right.**
   - Main :664: the subject is the partition, and the corollary now opens "Under the lemma's hypothesis".
   - Main :666: "$T$ selects a rest frame" is the consequence of the converse's own maximal-compact hypothesis.
   - SM :1414: "realized at a horizon that selects a rest frame, so it makes contact…" makes the horizon the selector.
   - ch19 :240: the selector is "that horizon".

4. **Mirrors.** ch19 :240, :242, :246 and :248 are byte-identical to FULL :5400, :5402, :5406 and :5408.

5. **Stamps.** The `.tex` source-sha256 stamps match their `.md` for Main, SM, Substratum and FULL. `staleness_check` reports OK, and so does `coverage_check` (128 statements).

6. **Residual sweep.** I grepped papers/*.md and book/*.md for map, $T$, trace-out and observation followed by selects, singles out, distinguishes or picks out. The only remaining hits involving T or the map are Main :664 and :666, both sound as above. Every other hit is an unrelated "observation selects / distinguishes" sentence (Complexity, Explainer, Main :588, Methodology, Structure, SM :336, ch03, appendix-c).

The worktree used for this check has been removed.
