# QPHEN Phase 1, r7b → r7c: dispositions

This revision fixes the two failures found by the independent diff check of r7b (`review/CHECK-r7b-independent.md`, sha256 `2e355f09…`). Nothing else changes. r7b is kept under `r7b/`.

| Finding | Change |
| --- | --- |
| **F1** (check 3: O3 rewording at QX-4 R4.9, first occurrence) | "when the meter is supplied under SA-1(c)" becomes "when the meter is supplied under SA-1(c) with its conjugate slot `m′` unknown". SA-1(c) admits the known functional ℓ = m′. Under that law the reciprocal coupling has `K_null = id` at k = 0, and a known displacement x ↦ x+1 at k = 1 (CHECK-r7c). The second occurrence matches Q4-P20's hypothesis and is unchanged. |
| **F2** (check 4: O2 label understates the evidence) | In Q4-P20's label, "computation-supported by p15 (2g)–(2i) alone for the conclusion's first sentence there" becomes X, "including the conclusion's first sentence there". The reason: p14 (3b) counts constancy of `x∘M − x` on the `c = 0` support, and p14 (3a) matches it to constancy of `x′ − x` over all 81 translations. The statement in DISPOSITIONS-r7b that p14 (3) "tests only `K_null = id`" is wrong. DISPOSITIONS-r7b is kept unchanged as the record of r7b. |
| Housekeeping | Titles and §0 tags go from (r7b) to (r7c). The revision pointers name `r7b/` and DISPOSITIONS-r7c.md. |

No claim, proof, hypothesis, ledger status or count changes. §8 still has 81 entries: 44 proved, 12 disproved, 25 open.

Optional note N1 from CHECK-r7c (`ab7ae723…`) is not applied. p14 (3a) covers every part at q = 2, and the first 200 of the 648 location-preserving parts with four laws at q = 3. The label's phrase "over all 81 translations" is literally true. It should not be read as (3a) covering all 51,840 parts; that coverage is (3b)'s.
