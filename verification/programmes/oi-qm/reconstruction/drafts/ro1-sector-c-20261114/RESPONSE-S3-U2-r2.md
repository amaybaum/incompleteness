# Response to the confirmation review of S3-U2-r2

**Review.** `REVIEW-S3-U2-r2.md`, on PR #1294 at `0a4fb901`, returned ACCEPT WITH CHANGES. It
contains two required findings, N1 and N2, and two optional items, P1 and P2.

**Revision.** `S3-U2-r3.md` applies N1, N2, P1 and P2, and changes nothing else. No verdict moves. r2
(`S3-U2-r2.md`, blob `4642ff78f29ecabccbcd084aa96c6c612ba99c21`) is left unchanged.

| # | Finding | Disposition | Where in r3 |
|---|---|---|---|
| N1 | "only as a falsification condition (Substratum:481)" is a false negative corpus claim. E1 also carries the datum | **Accepted.** Checked at `75cc5100`: Substratum:76 is E1 ("described, to the precision tested, by quantum mechanics", in the empirical inputs), Substratum:475 heads Class A ("would falsify … if violated"), and Substratum:481 is the Bell/Tsirelson condition. The sentence now gives both sites with their status: E1 as an empirical input, implying the datum through the `2√2` bound [A-inf], and Substratum:481 as the matching falsification condition. The corpus states no measured CHSH value. M-PR5's miss is then conditional on `Θ`'s identification, given E1 | §6.2 (bullets and M-PR5 row); §11.2 |
| N2 | Residual of R4: "excluded by declaration" and "not in the circuit" are states U1 does not define | **Accepted.** In reading (c), each of CP-6, CP-7 and CP-8 is *not available* at the scope of the specified circuit, by its declared grammar (SEL-EXCL-1 ll. 91, 97, 150). Each carries the K-1 caveat that this rests on a declaration. Exhibiting a tuple that executes the operation is a *stop* (construction). CP-6 in reading (g) is *not available* at that tuple's scope, since the specified `φ_m` does not effect it. As a necessary consequence of the mapping, CP-8 joins CP-6 and CP-7 in §3's closing K-1 sentence and in §8.3's stop list. The outcome vocabulary now reads "No other state is used (R4, N2)" | §3 table and closing sentence; §8.3; §11.1; outcome vocabulary |
| P1 | §6.2 merges S5 with the wing geometry | **Applied.** "S8 and `Θ` (a), including the wing geometry; S5 is a separate condition", in §6.2 and §11.2 | §6.2; §11.2 |
| P2 | The CP-4 resource line | **Applied.** It lists one setting writer, the blank `B₀` and a budget of at least 2 for the same-register witness, plus one blank for the fresh-output variant | §11.2 |

**Checks.** All edits were made by exact-string replacement, each asserted to occur once. The diff
from r2 to r3 touches only the sites listed above and the header's revision note. The forbidden words
and local paths were checked with grep: the only matches are r2's withdrawn phrases, quoted in r3's
revision note. Nothing is computed, committed or pushed.
