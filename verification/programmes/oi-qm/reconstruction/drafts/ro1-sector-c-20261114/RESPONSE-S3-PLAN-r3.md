# Response to the focused review of S3-PLAN-r3

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-S3-PLAN-r3.md` (ACCEPT WITH CHANGES at
`9c65c22e`). The changes are in `S3-PLAN-r4.md`. They are local fixes only, and nothing else changes.
`S3-PLAN-r3.md` is left unchanged (SHA-256
`1213c3568ddf3b9c1c800f4f7d36b6da9bb44f2bd57db2099e26a0bdb9d8034b`).

Each finding was checked against the r3 text and its sources. No finding was found to be wrong.

| Finding | Check | Disposition | Where in r4 |
|---|---|---|---|
| **R3.** AC-1's per-unit wording blocks negative findings | Confirmed. r3 §9 read "no restriction excludes PR by disabling …", which conflicts with H-RR's refutation route in §4.1 ("failing AC-1") | **Applied.** The wording is now "no restriction is *proposed, or reported as passing*, if it excludes PR by disabling …". Added: a restriction found to do so is reported as failing AC-1, which is an admissible finding. AC-1 governs what a unit may propose or accept, not whether it may report a failure. §6's row is unchanged, as the review advised | §9, acceptance paragraph |
| **R4.** The reference-class sentence is written as settled | Confirmed. The reference class is "the reference vacuum/uniform state class" (Main:724 (x)), and its definition is OB-b0, open under #1234. The native marker's marginal is uniform (`MR-star.md`:642) | **Applied.** The sentence now reads that whether the marker lies in the reference class depends on OB-b0, and that if it does not, D-1 does not apply under the scoped reading | §8.4, check 1, (α) |
| **N1.** (β) and (δ) are coupled | Confirmed from S-L5's form (`MR-star.md`:584–594): the marker's content after coupling is `s_A + Φ_{AΣ} s_Σ` | **Applied** as an [A-inf] bullet. A native uniform marker masks its own record; the path information survives only jointly with whatever retains `s_A` (MR-1 GAP; OA-1 Gap 1); for the only sourced marker, (β) generically fails unless `s_A` is held elsewhere, and the native-marker miss branch may be empty. U4 decides (β) and (δ) together | §8.4, check 1 |
| **N2.** "At the rate" is a resource count; what a match falsifies | Confirmed | **Applied.** "At the rate" is removed from H-RR's support condition. A rate counts only where the limit is structural, that is, where it differs between PR and the quantum references on the shared interface. The falsification sentence now names both directions: a miss falsifies the K1 reading together with the identifications, and a match falsifies the reading that native K1 recording misses complementarity | §4.1; §8.4, check 1 |
