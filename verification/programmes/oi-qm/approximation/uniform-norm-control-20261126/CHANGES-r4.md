# Uniform norm control: change map r3 → r4

r3 is `REPORT-r3.md` (commit `626628da47c75f045de32762ebb8e8443912959a`) and r4 is
`REPORT-r4.md`. Every earlier file is unchanged. The finding is the propagation finding of the
delta review of r3, posted on PR #1614 (verdict ACCEPT WITH NITS): the narrowed CC-p claim survived
in two places. The change is to text only; no result, proof or status changes.

| Where in r4 | r3 text | r4 text |
| --- | --- | --- |
| §5 CC-p heading | "CC-p (the coverage term is load-bearing)" | "CC-p (F1 alone does not bound the norms)" |
| §8 CC-p bullet | "It shows that the coverage term is load-bearing for Prop X1." | "It shows that law boundedness (F1) alone does not give Prop X1's norm conclusion; the soundness term alone is not tested." |
| Title and revision note | revision r3 | revision r4 |

A grep of r3 for "load-bearing" found only these two occurrences. A grep for "coverage hypothesis"
found none. In r4, "load-bearing" does not occur.
