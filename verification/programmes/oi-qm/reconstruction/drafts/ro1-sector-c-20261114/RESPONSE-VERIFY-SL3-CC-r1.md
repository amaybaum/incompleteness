# Response to the review of VERIFY-SL3-CC-r1

**Review.** `REVIEW-VERIFY-SL3-CC-r1.md` (ACCEPT WITH CHANGES; PR #1294 at `c2da5530`; reviewed blob
`4baa0283`). **Revision.** `VERIFY-SL3-CC-r2.md`. r1 is unchanged. Every finding is accepted and
applied; none is rejected. Each was checked by hand against the sources at `origin/main` =
`75cc5100` before it was applied. Paper verification only; no computation; nothing committed. All
four items stay named premises until r2 is reviewed and accepted.

| Finding | Check made before applying | Change in r2 |
|---|---|---|
| **F1** (required) block swap; marginal reading | Re-derived the one-site case: over `ℤ/2`, `a = 1`, `X = {i}`, one tick maps `(x_i, y_i)` to `(y_i, (A y)_i − x_i)`, which is `(y_i, x_i)` when the neighbours' current slice is `0`. Confirmed that the r1 S-C1(a) sentence omitted the case `Φ^n_{XX} = σ_X`. | §1.2 (L3c) now checks only MR★'s stated support, with the corrected sentence "the map on `s_X` is `Φ^t_{XX}`, fixed by `(t, X)` and selectable by no region". The block-swap argument moved to a new §1.3, labelled as this record's supplement Sup-1, "global block-form reading". The word "unconditional" is dropped. The marginal reading and the `ℤ/2` one-site case are added as Sup-3, recorded as outside S-L3 and Sup-1, contradicting no S-L3 bullet and giving no erasure. |
| **F2** (required) verdict split; credit; MR★'s own uses | Confirmed r1 §1.4's own "only in the sense" wording, and the MR★ uses at MR★:648, 856, 1396, 1485. | §1.5 has two rows: S-L3 as stated, VERIFIED; the gloss "erasure unavailable on K1", VERIFIED AT NARROWER SCOPE. §6 credits Sup-1 and Sup-2 to this record, not to S-L3. §1.5 adds the narrowing for MR★'s four uses, without correcting them (MR★ is frozen). The T3 non-coverage cites PREREG:485–487. |
| **F3** side-2 case | Confirmed: SM:224–226 sums `2d` neighbouring values; `A = 0` needs `2a = 0` on `𝐑`, which among `ℤ/q`, `ℤ_p` (torsion-free) and `ℝ/ℤ` with `a` injective is only `ℤ/2`; any axis of side `≥ 3` gives `A ≠ 0`; MR★:358–359 and PC★:102–106 define K1's `A` as the relation sum. | §1.2: "side 2 in every axis" and "`𝐑 = ℤ/2`"; "outside the native lattice" removed. The native scope is unaffected because frozen K1 uses PC★2a's relation sum, which counts each neighbour once. The `A ≠ 0` remark is restricted to the multiset reading. |
| **F4** (required) CC5's T7 separation | Confirmed MR★:1145–1147 (stage 2 halts before any T7 step if the Eqs. (10)–(11) check fails). | §4.2 splits the T7 separation: law level as written (same protocol; PREREG:552's reading); verdict level conditional on PC-Q's W1 and the pending check. §4.4 states the condition. CC7's T7 carries the same condition (§5.2), noting that its named test is §3.5. |
| **F5** CC7 and the law of `f` | Confirmed `V` is signed (MR★:972): `V(π/2) = 1 − 2q`. (ii) needs `0 < q < 1` under a contrast reading. | §5.2, §5.3 (G-CC7-2) and §5.4: `V = 0` needs `q = ½`; (ii) and the dephasing classification need `0 < q < 1`; the T8 row as signed needs only `q > 0` (narrower than the review's `0 < q < 1`, since `q = 1` gives `V(π/2) = −1 < 1`). The §3.5 separation is moved from "as written" to "conditional on nondegenerate `f`". Only the `D` part stays as written. |
| **F6** `separated` gap | Confirmed PREREG:552 ("from PC-Q's law"), MR★:1122, MR★:1233, Row 0 at MR★:1243–1248 with no separation clause, and frozen 0(i) at PREREG:592–593. | §2 states both facts. §3.2 and §3.4 say CC4's T7 separation is not computable under the law reading and holds only under a reading that does not compare laws (the W1 verdict or the derived `(P, V)`). §6's repair list adds the rule for `separated` and the Row 0 clause. |
| **F7** minor | Each item checked. | `DP`'s validity for CC4 needs uniform `f` (§3.2, G-CC4-2). G-CC4-1 now names the undefined CC4 settings: `P_bal`, the strength map (MR★:1051), T6's `B₀`, `B₁` (MR★:1056), and `z_s`, `x_s`. CC5's T5 `p₀ = ½` needs uniform `e`, while order independence and `ϕ₁ + ϕ₂` dependence hold for any law (§4.2, G-CC5-2). LIT-1-C7 is cited at LOG:433–435, and LIT-1-C4 at LOG:67–70. CC4's three T2 laws are now shown (§3.2) and match B-T2. |

**Optional item taken.** The review's optional note on off-`main` references is applied: §0 of r2
classifies S3-PLAN-r9/S3-U1-r5 (provenance), PR #1023 c.6554399670 (support on `main`, quoted in MR★
§K★.F) and the relayed `fc68d333` review (provenance only).

**Verdicts after revision.**
- S-L3 as stated: VERIFIED.
- The gloss "erasure unavailable on K1": VERIFIED AT NARROWER SCOPE.
- CC4, CC5, CC7: each VERIFIED AT NARROWER SCOPE. Their scopes change as listed above.
