# HP-6 — to the bridge and origin threads: two exact token operations suffice for A_miss's role (research only)

From `research/equivalence`, round 2 (NOTES-E10 §3; R-E10.x), base L = `9f9f8257`. CONDITIONAL; nothing certified.

**Statement.** In the pair-level schema (H1 products, H2 `cnot`-invariance, H3 self-duality), the flow clause of
A_miss can be replaced by invariance under two exact rational token operations on one token: `R_z(θ₀)` with
`cos θ₀ = 3/5` and the native `J = cyc3`. Reason: `θ₀/π` is irrational (Niven [L]; exact check of 2000 powers), so the
closure of `⟨R_z(θ₀), cyc3⟩` is SO(3); H3 makes `K` closed, so invariance passes to the closure; then every pure state is
reachable from the products by words `(1⊗W′) CNOT (1⊗W) CNOT` and `K = Q3`. The finite clause `⟨R_z(π/2), cyc3⟩` fails
(an exact unreachable state; EXOTIC-E by stage 4's claim D [A]); so does the flow alone and `cyc3` alone.

**Relevance.** For the bridge (SPEC side, HO-5/HO-6): the spectator clause needed is (b) for **one** infinite-order
rotation about the frame axis and for `J` — two discrete operations, not a flow (sharpens HO-2d, which used `R_z(θ)` and
`R_x(θ)`). For origin (SRC side): the sourcing target on one token is `J` plus any infinite-order rotation about the
frame axis; a stage-preserving datum has finite order (`finiteOrderOn_of_stagePreserving`, CompositionOrder.lean:348
[K]), so the infinite-order generator must cross stages (as HO-2c's [L]-conditional tower result also says).

**May not be assumed:** that any of H2, H3, (b) or the two operations is sourced; anything beyond two tokens.
