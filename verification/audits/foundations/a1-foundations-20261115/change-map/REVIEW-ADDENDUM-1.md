# Review of Addendum 1 to change map A1C r6-min

**Reviewer.** The independent reviewer of the A1C map. Paper-only: no repository file was edited, nothing was committed, pushed or posted, and no tool beyond read-only searches and small read-only scripts was run. Base: the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. I also read the implementer's worktree (`wt-2a`, which holds the 126 applied entries, uncommitted), to check that the seven entries' lines are unchanged there and that nothing dangles.

## Verdict

**CONFIRMED WITH NITS.**

- All 21 primary pairs apply exactly: each old string occurs once on its stated line at the base, and every book line has a byte-identical FULL twin.
- Each new text carries the correction r6-min intended, in minimal form. None adds a claim, premise or prediction, A1 stays open, and no fragment is left.
- The three proposed drops are correct on the merits, but they shrink three reviewed entries. The one nit: under the authorization's clause "Any unexpected issue … must be reported separately", the drops must be reported to the owner, not just applied.

## 1. Mechanical checks

| Entry | Pairs | Old string: occurrences on the stated line | FULL twin | Line unchanged in `wt-2a` |
|---|---|---|---|---|
| N-U34 | (a) Sub:48, (b) Sub:171, (c), (d) Sub:467 | 1 each | — (paper) | yes |
| N-Y11 | (a) Meth:339, (b) :381, (c) :385, (d) :389, (e) :391 | 1 each | — (paper) | yes |
| N-K01-16 | (a), (b) ch01:16; fallback (c) ch01:183 | 1 each | FULL:351, :518, identical | yes |
| N-K03-40 | (a) ch03:40, (b) :162, (c) :180; fallback (d) :186 | 1 each | FULL:905, :1027, :1045, :1051, identical | yes |
| N-Kappc-32 | (a) appendix-c:32, (b) :34 | 1 each | FULL:6262, :6264, identical | yes |
| N-Kgl-19 | fallback (a) glossary:19 | 1 | FULL:6603, identical | yes |
| N-K18-186 | (a), (b) ch18:186; (c) line 188 and the blank 189; (d), (e) ch18:190 | 1 each; :188 begins "**Falsifiability.**"; :189 is blank | FULL:4992, :4994, :4996, identical | yes |

Applying by string, or bottom-up as the addendum says, handles the two-line FULL shift after (c).

## 2. Content of the 21 primary pairs

- **Bell rows that derive parameter independence from the cone get the scope.** These are the sentences where parameter independence follows from the readouts lying outside the other wing's graph cone, or from the coupling range not connecting the wings:
  - Sub:467 (d); Meth:381, :385, :389, :391; ch01:16 (b); ch03:162, :180; appendix-c:32, :34.
  - Each inserts the Bell scope of Main §3.3's Corollary, parts (1) and (2), in r6-min's N-M54 wording. That is the correction r6-min intended.
- **Sentences about the nearest-neighbour or reference cubic graph get only part (2)'s finite-region condition.** This is correct and minimal: the any-cardinality case is part (2), and on a finite site set the regions are finite anyway.
  - Sub:48, Sub:171, Meth:339, ch03:40.
  - Sub:171 is a no-go ("cannot itself realize M1-B"). Adding finite regions to its hypotheses narrows the claimed no-go to what Main:414 (2) proves, which is correct.
- **Cone sentences get "for finite-range couplings", as in the map:** Sub:467 (c), ch01:16 (a).
- **None of these pairs adds a premise or a claim.** The insertions repeat conditions already proved in Main §3.3, and no sentence says the site set is finite or infinite.
- **Wording.** The scope phrase is long. It is r6-min's reviewed wording, so it is kept unchanged. "On a finite site set …, if …" at the start of ch03:162, ch03:180 and appendix-c:32 reads correctly.

## 3. The three proposed drops

I read each sentence in context:

- **ch01:183:** "for a response-complete deterministic completion that records a $\pm1$ outcome in every run, measurement independence plus parameter independence would imply $|S_{\rm CHSH}|\le2$".
- **ch03:186:** "given deterministic dynamics and a $\pm1$ outcome in every run, a completion that keeps ontic parameter independence and measurement independence obeys $|S_{\mathrm{CHSH}}|\le2$".
- **glossary:19:** "measurement independence plus ontic parameter independence, with a $\pm1$ outcome in every run, gives Bell factorization and $|S_{\rm CHSH}|\le2$".

In each, parameter independence is **assumed**, not derived from the graph cone. The conclusion is Bell's theorem itself. Under determinism and $\pm1$ outcomes, each wing's response table takes one of sixteen values, and the table is measurable whenever the outcome probabilities $P(q,r\mid a,b)$ exist. With parameter independence and measurement independence assumed, the pointwise bound $q_0(r_0+r_1)+q_1(r_0-r_1)\in\{-2,2\}$ averages to $|S|\le2$ on any probability space. Neither a finite site set nor finite regions enters. The only step that needs either is the cone step that delivers parameter independence (Main:403–404: "(ii) and (iii), which with the cone lemma secure ontic parameter independence").

Main states the same assumed-independence form, unscoped, at Main:80 item (4). No version of the map touched that sentence. The three sentences therefore carry no claim that rests on A1, and leaving them unscoped leaves no unsupported assertion. Adding the scope would understate a result that holds unconditionally.

**Decision: drop all three.** The fallback pairs are not to be applied.

My r1 review (F5) listed these three sites among the Bell restatements needing scope. That listing over-included them.

## 4. N-K18-186

After the pairs, ch18:186–190 read: "The return itself is definite: a finite model returns to its exact initial state after $N$ substratum time steps, where $N$ is fixed by the cycle structure of $\varphi$. It is at most $g(|S|)$ for any bijection and below $|S|$ for the exactly linear rule. The framework bounds $N$ rather than computing it, and it supplies no lower bound on $N$." That is followed by "A finite model is periodic with period $N$, the least common multiple of the bijection's cycle lengths. …", with the cycle-structure mathematics kept.

- **Prediction removed completely (Q10 (c)).** Three passages go:
  - the physical-units and astronomical-period sentences at :186;
  - the Falsifiability paragraph at :188 ("The recurrence prediction is falsifiable only in the logical sense … any framework consistent with those commitments must predict exact recurrence");
  - the "predicts that the universe is cyclic" clause and the cyclicity-commitment sentence at :190.

  The return and the periodicity are stated of a finite model. The period bounds ($N\le g(|S|)$; $N<|S|$ for the exactly linear rule; the $\mathrm{lcm}$ and Landau bounds at :176–:184) stay as mathematics about finite models.
- **The deletion of :188 is within the entry's purpose.** r6-min's N-K18-186 names ":188 delete the Falsifiability paragraph", reviewed since r4. The paragraph's mathematical content, the bounds, survives at :186.
- **No fragment.** Deleting line 188 together with the blank line 189 leaves no doubled blank. The :190 sentence begins cleanly with "A finite model is periodic …". The remark that the observer's direction is fixed "on a stretch of the cycle" now sits inside the finite-model paragraph.
- **Nothing dangles in `wt-2a`.**
  - After this entry, no book or paper line mentions "cosmic recurrence", "F8", "recurrence prediction", "logical sense", "cyclic at the substratum" or "substratum cyclicity". The other occurrences were removed by applied entries: ch18:28 (N-K18-20), ch18:328 (N-K18-328), appendix-a:181 (N-Kappa-181), appendix-c:132 (N-Kappc-C6) and book README:90 (N-Kbk-90).
  - The remaining "§18.7" references (ch01:121, ch09:106, ch18:40) cite the bound or the recurrence route, which survive.
  - No text refers to the Falsifiability paragraph itself.

## 5. Scope

The addendum touches only the seven entries left unapplied: N-U34, N-Y11, N-K01-16, N-K03-40, N-Kappc-32, N-Kgl-19 and N-K18-186. It adds no site. Each pair implements a sub-edit already in the reviewed r6-min entry. Sub:171 belongs to N-U34 in r6-min. The only departure from the reviewed entries is the three drops, which reduce the edits. They are the nit to report to the owner.

## Final apply list

| Entry | Apply | Do not apply |
|---|---|---|
| N-U34 | (a) Sub:48, (b) Sub:171, (c) Sub:467, (d) Sub:467 | — |
| N-Y11 | (a) Meth:339, (b) :381, (c) :385, (d) :389, (e) :391 | — |
| N-K01-16 | (a) ch01:16, (b) ch01:16, with FULL:351 | (c) ch01:183: DROP; fallback not applied |
| N-K03-40 | (a) ch03:40, (b) :162, (c) :180, with FULL:905, :1027, :1045 | (d) ch03:186: DROP; fallback not applied |
| N-Kappc-32 | (a) appendix-c:32, (b) :34, with FULL:6262, :6264 (`wt-2a`: 6261, 6263) | — |
| N-Kgl-19 | — | (a) glossary:19: DROP; fallback not applied |
| N-K18-186 | (a), (b) ch18:186; (c) delete :188 and the blank :189; (d), (e) ch18:190; with FULL:4992, :4994, :4996, applied by string or bottom-up | — |

That is 21 pairs to apply and 3 sub-edits dropped. Report the three drops to the owner as the authorization requires.

## What I could not check

- No build, guard, census or coverage run.
- The post-application reading of ch18 comes from the base text with the pairs applied by reading, not from an executed dry run.
