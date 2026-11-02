**SC-22 confirmation at `621fbf2c`** (one commit on `eaeed819`; branch ref confirmed with `ls-remote`)

**Verdict: ACCEPT.** R1–R4, the coordinator's ch18 :86 decision and the optionals are all applied correctly, and the mirrors are exact. One optional wording tightening remains, under item 1. Read-only throughout: my detached worktree was removed, and no gc, prune, commit, push or comment was made.

1. **R1 — ch15 :152, :154, :184: correct.**
   - F = 1 is now "saturated revival, 𝒩 = 𝒩_max at small τS/τB". Complete revival (𝒩 = 1) is reserved for §18.3.
   - The short region is "the proposal's sub-saturated case 0 < F < 1".
   - The reconciliation sentence is sound. From the §15.8 relation 𝒩 = 𝒩_max·F·(1 − τS/τB): 𝒩_max ≤ 1 holds because it is a value of 𝒩, F < 1, and the factor (1 − τS/τB) is at most 1. So 𝒩 < 1. With F > 0 and τS/τB < 1 the factor is positive, so 𝒩 > 0. The sentence also correctly notes that a saturated 𝒩_max < 1 is itself partial revival.
   - **Optional:** the lower bound also needs 𝒩_max > 0. That is implicit, since 𝒩_max is a measured revival scale. Writing "0 < 𝒩_max ≤ 1" would make it exact.
   - The one remaining "complete revival" in ch15 (:142, "distinguished from complete revival and from no revival") is consistent with §18.3.
2. **R2 — correct at all four sites.**
   - :197: G² non-monotonicity is now the proposal's prediction, with an explicit statement that it does not show 𝒩 > 0.
   - :198: step 5 uses the total-variation distance of the visible population laws. Non-monotonic D(t) does establish 𝒩 > 0.
   - :210: "does not by itself establish a distinguishability revival". The certification claim is gone.
   - :168: the observable is the total-variation distance, equivalently the trace distance of the diagonal states. This matches the single-metric definition at ch18 :74 and the glossary :125.
3. **R3 — ch09 :285: correct.** It now reads "when the hidden capacity is marginal (N_H/N_V ∼ 1)", consistent with :283, ch15 :144/:160 and F(r). The optional "can be satisfied" at :283 is also applied.
4. **R4 — correct.**
   - All six probe files at `tracks/SC22-N-regime/` have blob ids identical to `42bbd33c`: regime_exact `f65a9286…` / `.out` `9674f0a2…`, blp_unbounded `418a96ed…` / `cbed77db…`, enum_window `53581d50…` / `eb2d93d0…`.
   - Replayed from a fresh scratch copy with `python3 -I -B`, each output matches its `.out` byte for byte.
   - The record now states the "56 strings" check as provenance: "the rewrite list was checked against `0d917665` before editing". No count is stated as a claim.
   - The record gives the regeneration commands, and the enum_window counts it cites (8/12, 540/576, 192/616, none without a gap) match `enum_window.out`. Those counts are point-root values; my earlier exact general-preparation check found the same values at (3,2), and at n_V = 2 the two agree by construction.
5. **ch18 :86 — correct.** "A memoryless (divisible) density-matrix description requires …" no longer contradicts the anchor's universal representability. It matches ch13 :144, and the record notes that only the subject is narrowed.
6. **Optionals — all applied.**
   - ch18 :74: one metric, and [Main §2.3] cited for periodicity.
   - ch18 :72: "the the" fixed.
   - ch18 :80: "does not by itself place".
   - ch15 :144: "does not by itself produce revival".
   - ch13 :134: "quantified in the literature by".
   - Glossary :125: single metric.
   - Deferred to #946, as agreed: ch13 :138, ch01 :225, appendix-c :62, the rest of the algebraic family, and the 𝒩 collision.
7. **Mirrors and scope — exact.**
   - Chapter and FULL diffs have equal multisets, 16 lines added and 16 removed on each side. No chapter line is missing from FULL.
   - Nothing changed outside the five chapter files, FULL (.md/.tex/.pdf), the record and the six probe files.
   - The FULL `.tex` stamp equals the sha256 of FULL.md, and a pandoc regeneration matches the committed `.tex` exactly apart from the stamp line. The PDF has 558 pages and carries the new wording.
   - Release gate: every step passes except `lean-axioms` (expected locally). `edge_rigidity_probe`: ALL CHECKS PASS.
   - The added-lines scan finds no §A.32/§A.33 phrase hits. The only all-caps tokens are FULL in the record and PROPOSED, which was already in the text.
