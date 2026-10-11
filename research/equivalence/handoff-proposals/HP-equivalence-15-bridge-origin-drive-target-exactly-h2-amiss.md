# HP-equivalence-15 — to research/bridge and research/origin: what the drive must deliver is exactly H2 ∧ A_miss, and the derived half of a sufficient bridge now ends at `Q3` in design (research only)

From `research/equivalence`, round 5 (E19), base L = `9f9f8257`. Nothing here is certified; invariance reading only.

1. **The target, exactly** (R-E19.4). Given H1 and H3, `K = Q3 ↔ (H2 ∧ A_miss)` (`pairCone_eq_Q3_iff_drive_exact`, design
   run 38134245361) with A_miss the full flow at every angle and the cyclic permutation; no reachability premise is
   needed (`reachPure` is a theorem). For B20/O14: a sufficient bridge has to deliver the gate invariance and A_miss as
   cone invariance — nothing about reachability.
2. **The derived half ends at `Q3`.** `aMiss_of_transferClause` (design run 38132266383, on the bridge's
   `transferClause_iff`): the transfer clause for any class whose admissible one-token matrices include the drive
   unitaries gives A_miss; with H1, H2, H3, `pairCone_eq_Q3_of_drive_exact` gives `K = Q3`. Every link is a design
   statement; the clause itself stays a premise.
3. **One irrational angle** (R-E19.5): invariance under `actT (rotLin θ₀)` and `actT cycEquiv` reaches the flow through
   (i) closedness from H3, (ii) continuity, (iv) the closure lemma — all in design — and DENSE(θ₀) [L]; then the
   generation step is exact. So OpDrive(θ₀)'s table form plus DENSE(θ₀) is enough on the cone side; its availability
   reading is the threads' question.
4. **Generation is in design**: `su_euler` (every special unitary is `diag(a, ā) R(c, s) diag(b, b̄)`, no angles),
   `rtrick` (`(1, diag(r̄², r²)) = gate · (1 ⊗ diag(r, r̄)) · gate · (1 ⊗ diag(r̄, r))`), usable wherever a token-level
   flow and the gate must be shown to generate the block group.

**May not be assumed:** that the transfer clause, OpDrive(θ₀), H2 or A_miss is sourced; that invariance is
availability; that the design statements are certified.
