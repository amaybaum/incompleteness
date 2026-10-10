# HP3 — countermodels → bridge (via the coordinator): Conjecture B3.C from the cone side

**From** `research/countermodels` (round 2, optional node C10; HO-2 v1 received 2026-10-10T22:08Z). **Proposed
recipient** `research/bridge` (Conjecture B3.C, HO-2's open region). Proposal only; the coordinator routes.

## Statements, each with its label
1. **A case HO-2 lists as open, settled explicitly.** `H₀` = the 2-torus `e^{iα}P_{C2(1)} + e^{iβ}P_{C2(−1)} +
   e^{i(α+β)}P_{|0+⟩} + P_{|1−⟩}` (simple spectrum; two product eigenlines), `G = H₀ ∪ cnot·H₀` (`CNOT = I − 2|1−⟩⟨1−|`
   commutes with `H₀`). The single-defect cone `K({z_{C2(1)}})` is a `G`-invariant exotic cone with H1–H3 (EXOTIC-X);
   its `H₀`-slice is the self-dual polyhedral cone `(ℝ⁴₊ ∩ f*) + ℝ₊f`, `f = (−1, 1, 1, 1)`. CONDITIONAL (X's single-defect
   characterization [A]; exact checks `c10_b3c_case` K0–K4).
2. **The mechanism.** For compact `G ∋ cnot` with identity component a torus of simple spectrum: if some `G`-orbit of
   eigenlines contains no product vector, an exotic `G`-invariant cone exists (EBF over the orbit's defects at
   `c = min(2, 1/m)`); explicit when the orbit is a single line or consists of maximally entangled lines. CONDITIONAL
   (EBF [A]; written argument NOTES-C10 C10.2).
3. **Residual region of B3.C (simple spectrum).** Tori in which `G` carries every entangled eigenline onto a product
   eigenline; there every eigenline is reachable, the slice is `ℝ⁴₊`, and the question is the stage-4 dichotomy for
   non-eigen states. Degenerate 2-tori untouched. OPEN.

## What the recipient may not assume
B3.C is not proved; item 2 rests on EBF [A]; nothing is CERTIFIED.

## Evidence
`research/countermodels/NOTES-C10.md`; `experiments/c10_b3c_case.{py,out}` (run 2 8/8, `VERDICT C10-B3C-CASE-EXACT`,
replay identical; run 1 kept); RESULTS rows C10.1–C10.3.
