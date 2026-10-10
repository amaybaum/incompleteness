# RESULTS — research/bridge

Every claim carries one label: CERTIFIED [K at L, file:line] / CONDITIONAL (on named items at their status) / CONJECTURE / FAILED / OPEN; evidence level [K]/[D]/[W]/[X]/[A]/[U]; and a pointer to its script, output and replay.

Base L = `9f9f8257`; kernel paths under `verification/lean-mathlib/OIBridge/` (CD = CompositeDimension.lean). Scripts under `experiments/`; every `.out` has a byte-identical `.replay.out`.

| id | statement | label | evidence | where |
|---|---|---|---|---|
| B1-0 | `cnot (prodState xplus z3) = phiW = diag(1,1,−1,1)`; hence `phiW` lies in every candidate cone (H1 + H2) | CERTIFIED [K at L, CD:1220–1222] (the membership step [W]) | [K]; recomputed [X] b1 K0a | NOTES-B1 §3 |
| B1-1 | Under locality of registers (product registers, local readout `R_A ⊗ R_B`, token operation `π × id`), the hidden idle extension of a readout-respecting permutation induces `actC N_π` / `actT N_π` on the pair readout | CONDITIONAL (on L-REG and RESPECT of `π`; L-REG is a hypothesis, not at L) | [W] NOTES-B1 §2; [X] b1 H1a–H1b (48 octahedral permutations, exact) | NOTES-B1 §2; b1_hidden.out |
| B1-2 | (b_H) for `O` holds when RESPECT (W), availability in context (A) and product behaviour (P) hold, with local tomography | CONDITIONAL (on (A), the H-level spectator clause of OI⁺-1: assumed, not at L; (W), (P) hold operationally in branch (a); LT is the premise field `lt`, CompositeInterface.lean:245) | [W] Theorem B1.1; [X] b1 H3 (rank 16) | NOTES-B1 §2, §4 |
| B1-3 | Locality of registers as the bridge from embedded observation to (b) | FAILED (kept with evidence): with measurement-independent preparations it bounds `|S_CHSH| ≤ 2`, while `phiW` and each defect `z_s` reach `S = 14/5` with valid statistics. It therefore excludes every candidate cone, `Q3` included. With all hidden distributions available, no hidden permutation realizes `cnot`, since `⟨w, phiW⟩ = −2` against `min = 0` on the hidden cone | [W] Theorem B1.2; [X] b1 H1c, H2a–H2d, CC2–CC3 | NOTES-B1 §3, §7 |
| B1-4 | GR.md:326 ("tensor product structure follows from the spatial product structure of the classical configuration space") read as an operational-composite statement is L-REG, and is Bell-local by the framework's own Main.md:360–371 | CONDITIONAL (on reading GR.md:326 operationally; as a level-M carrier statement it is correct) — assumption-watch marker, manuscript hold | [W] | NOTES-B1 §5 |
