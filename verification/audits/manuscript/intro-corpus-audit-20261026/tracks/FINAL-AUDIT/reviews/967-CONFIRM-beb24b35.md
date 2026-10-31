## SC-31 confirmation at `beb24b351f2832aff0f60d6ee32db5bda0d08fa6`: ACCEPT, with one small record fix

All six items in the brief hold. The one thing left is a miscount in the record: it says 11 controls, but the script runs 10. `beb24b35` is one commit on `2430948d`, and `git ls-remote` confirms it is the branch head.

1. **R1 holds.** No manuscript site uses e^{10^122} as an upper bound on |S| or N.
   - ch18:186 now says |S| is not fixed by visible data. It cites [Substratum §4] (the bound at :263 sits under §4, which starts at :247) for |C_V×C_B| ≤ e^{10^122}, and says the deep sector is gauge.
   - The e^{e^{10^122}}, 10^61·e^{5×10^121} and 5×10^243 figures survive only after "For illustration only, if |S| were of order e^{10^122}".
   - The linear display now reads N ≤ q^D − 1 = |S| − 1, with no number attached.
   - ch01:121 and Explainer:175 say that n is not fixed by visible data.
   - The remaining `e^{10^{122}}` hits are ch18:186–187, which are illustrative, plus Main:218 and Substratum:263. Those two are holographic bounds that were already there and are correct.
2. **R2 holds.** ch18:196 states all three required points:
   - for a given |S| and φ, failing to recur within g(|S|) steps contradicts a finite S with bijection dynamics;
   - failing within |S| − 1 steps contradicts only exact linearity (A5);
   - for any finite T an |S| > T+1 is admissible, so no finite observation falsifies the framework as a whole.

   The added sentence, "An embedded observer's records are, moreover, part of S and return with it", is correct. The close at :336 matches, quoting g(|S|) and the same framework-level conclusion.
3. **R3 holds.**
   - Every summary site quotes g(|S|) with |S| not fixed: ch18:20, ch18:28, App A F8, App C:132, book/README:90.
   - "< |S|" appears only for "the exactly linear rule on a fixed coupling graph" under A5. That covers ch18:190, :194 and :196, ch01:121 ("exactly linear update rule (A5)") and Explainer:175 ("only an exactly linear update rule").
   - ch18:192 names both maps as not covered, the state-dependent-geometry map of [SM §3.1] and the rounded bijection of [SM §4.2]. For them it says only N ≤ g(|S|) and N | lcm hold.
4. **R4 and O1 hold.** App B:420 (and FULL) now reads "can be astronomically large". ch18:194 adds "it supplies no lower bound on N", and the proton-lifetime sentence is now conditioned on "A period of astronomical size". O3 holds too: record row (R) reads "for the exactly linear rule only".
5. **References hold.** Rosser–Schoenfeld and 1.03883 are gone from the papers, the book, FULL and the bibliography. Both strings survive only in the record README's list of zero-hit grep patterns (:109). The citation check passes with 112 citations, 0 broken. The script now prints max ψ(n)/n only as an observation, with no check attached.
6. **Scope holds.**
   - The diff touches only the SC-31 sites, App B:420, the bibliography, the record, and the regenerated Explainer and book files.
   - The FULL mirror is exact: all 14 added chapter/appendix lines are present in FULL, FULL adds exactly 14, and no removed line survives.
   - The `.tex` stamps equal the `.md` sha256 for both Explainer and FULL, and a regenerated Explainer `.tex` is identical apart from the stamp.
   - The PDFs carry the new text; Explainer is 70 pages and the book 559.

**Checks.** The release gate passes every step except lean-axioms, which fails locally as expected (including mirror, citation, voice and claims). `period_growth_check.py`, re-run from a scratch copy under `python3 -I -B`, replays byte-identical with 10 PASS and 0 FAIL ("ALL CHECKS PASS").

**Required (record only, trivial):** the record README's Numerical-check section (line 64, "all 11 controls pass") should say 10. The script has 10 `check()` calls; the eleventh `check(` match is the function's own definition, and the earlier "13" for 12 calls was off by one the same way.

No manuscript changes are needed. The detached worktree was removed, with no gc or prune.
