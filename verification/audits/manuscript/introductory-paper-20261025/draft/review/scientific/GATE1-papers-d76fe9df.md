# Gate 1 (scientific accuracy): PR #918 r29 at `d76fe9df`

**Verdict: ACCEPT.** I checked `git diff 4feca97b d76fe9df` against CHANGES-r29.md. The only paper changes are the two non-statement sentences at L140 and L152. The ledger is unchanged, so no ID is retired.

1. **"rather than of any accessible record" (L152) is correct.**
   - The failure of P-divisibility on {0,…,L} is a property of the rooted family, which is fixed by the dynamics and the shared hidden preparation.
   - Accessible records are restrictions to windows short compared with L, so they do not carry it (Main §2.3, Scope: "an observer's statistics are its restriction to accessible windows").
   - The new ending, "it constrains how such a world can be described, not what accessible data will show [Main §2.3, Scope]", is at the same scope.

2. **Yes, the earlier "rather than of any record" overstated, and I missed it at r28.**
   - Under a full-support visible prior, the failure is equivalent to M_k > 0 at some order k < L (the Corollary).
   - That is a property of the visible law over the whole cycle, so the full-cycle record does carry it.
   - Gate 3's correction is right.

3. **Dropping the clause that restated the hypotheses leaves no claim without them.**
   - The new sentence starts "The failure of chaining …". That refers to the failure named in the sentence just before it, "the failure of chaining it implies across the cycle … under the theorem's hypotheses".
   - The hypotheses are stated in full at L148 (the Corollary) and L150. They are also stated at L134, which is what CHANGES-r29 cites.
   - The sentence asserts nothing beyond what the Corollary covers.

4. **Nothing else is lost.**
   - The dropped clause "although one may hold on every accessible window" is still covered by the four-bit example at L154: "its forecasts from the start chain step by step there … it shows no failure of chaining inside it".
   - At L140, the reason ("a result about a rule has to cover every start the rule can be given, not only the starts a particular sample contains") and the mechanism are both kept.
   - "it can happen that the only rows keeping the table from being a permutation belong to starts that never happen" still carries Main §2.3's "possibly only through" sense, and the citation is kept, now at the end: "as in the different-deck example [Main §2.3]".
   - Removing "dropping those rows would then describe the sample rather than the rule" takes out a restatement only.

Nothing is weakened.