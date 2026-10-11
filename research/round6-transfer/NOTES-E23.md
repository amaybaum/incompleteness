# NOTES-E23 — the sources of H2, H3 and A_miss (short source table; narrowed)

Started 2026-10-11 15:37:17 UTC (S0-b item 3; owner's narrowing: a source table, no new computation). Base L = `9f9f8257`;
inventory `research/archive` @ `4dc0321c` (I3 §I–§J; I4); E19's design forms (`EqvK2Generation.lean:535`, run
38134245361 [D]); HO-43 item 6 at its label. No assumed item is upgraded to an observer-native consequence.

**Productivity test (§A.31).** A gem only if some premise is found to have a source at L stronger than its recorded
status; otherwise CONFIRMING. Expectation at the start: CONFIRMING (every source is assumed, open or introduced).

The premises in E19's exact form (EqvK2Generation.lean:535–539, [D]): H2 `∀ ω ∈ K, cnot ω ∈ K`; H3 `K = dualW K`;
A_miss `∀ t, ∀ ω ∈ K, actT (rotLin t) ω ∈ K ∧ actT cycEquiv ω ∈ K`; given H1 and H3, `K = Q3 ↔ H2 ∧ A_miss`.

| premise | inventory source (id, status at L) | reading of the source | remaining hypotheses for a derivation |
|---|---|---|---|
| H2 | I3.148 (PT-record: assumed; "the certified native gate; hgate", PROTOCOL-STAGE3.md:46; relative to L `hgate` INDEPENDENT, INTEGRATION-REVIEW.md:102). The gate itself is a kernel map on `W 3` (`cnot`, CompositeDimension.lean:775 [K]); DIM-1's native-gate hypotheses (I3.35 `NativeGateOf`, assumed) bound positivity on `maxCone`, not `K` | invariance | an operation datum and a transfer: the matrix `cnotMat` is a permutation of configurations, so the stated access makes its conjugation available [W]; carrying that to `K` needs a two-token transfer clause (the pair analogue of (T); introduced, OPEN — B22's gap) with the intertwining `dict_cnot` [D] |
| H3 | I3.149 (PT-record: assumed, unsourced at L; `dualW` only in a design module, I3.143); stage-2 CSD2, "every pair effect is a pair state", a conjunct of SDC whose observer-native source is UNRESOLVED (INTEGRATION-ADDENDUM-STAGE2.md:45–51); one ball's self-duality (the Lorentz effect cone, I3.124, I3.127) has no bridge to the pair | neither invariance nor availability of an operation: a duality of pair states and pair effects (tests) | an observer-native source for CSD2, or a one-ball → pair bridge for self-duality; none at L. `K = Q3` implies H3 — the target, excluded |
| A_miss | I3.165's clause "local actions compatible with the composite cone" (open, ROADMAP.md:1001; do not assume) with I3.150 (b_S4) and I3.153 (b_DJ) (PT-record: open; INDEPENDENT of H1–H3 at L; do not assume); the single-token K∞-Drive (I3.169, OPEN obligation; `ball3Drive`'s flow about the third axis, KInfFoundations.lean:449) has no bridge to the pair (I3.66) | invariance (each source states cone invariance under one token's actions) | in the availability reading, design routes only: {OpDrive(θ₀), J-datum, (T)_𝓘} ⇒ the two one-angle invariances (`bridge_derived_half` [D]); {J-datum, (T^ch)_𝓘, `K` closed, the repeat-until-success witness [W] + [X]} ⇒ the same (`bridge_channel_half`, [D] pending run 38151796092); from one angle to the flow: H3 (closedness), continuity [D], DENSE(θ₀) [L] (R-E19.5); or `aMiss_of_transferClause` (EqvOneDictionary.lean:121 [D]) for a class whose admissible one-token matrices include the drive at every angle. OpDrive(θ₀), the J-datum, (T)_𝓘 and (T^ch)_𝓘 are introduced, not OI premises; I4.60 (assumed, level H, outside Table A2) implies OpDrive(θ₀) (HO-33 v2) |

**Outcome.** No source stronger than its recorded status: H2 and H3 are PT-record assumptions (H2's `hgate`
INDEPENDENT relative to L); A_miss's sources are open and do not assume, and its availability routes all pass through
an introduced transfer clause (B22: OPEN in both forms). CONFIRMING; not a gem. The one structural note: H2's operation
is already available in the stated access ([W]), so H2's open content is the two-token transfer alone, the same gap as
B22's.

**Update after run 38151796092.** `bridge_channel_half` is [W], not [D] pending: the module's build failed on another
theorem (B23-1); the route's status in the A_miss row is unchanged otherwise.
