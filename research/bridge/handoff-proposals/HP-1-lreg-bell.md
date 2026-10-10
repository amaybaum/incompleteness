# HP-1 — locality of registers is Bell-local and hosts no candidate pair

From `research/bridge`, node B1. Proposed for any thread that sources the composite from the hidden level, and for the
overview's manuscript-propagation list. The coordinator routes.

**Proposition HP-1.**
1. Every candidate cone `K ⊆ W 3`, i.e. one with H1 (products in `K`) and H2 (`cnot K ⊆ K`), contains
   `phiW = cnot (prodState xplus z3) = diag(1,1,−1,1)`. The identity is certified at L, CompositeDimension.lean:1220–1222;
   the membership step is [W].
2. `phiW` has valid statistics and CHSH value `14/5` for the sharp ball effects `a0 = e_x`, `a1 = e_z`,
   `b0 = (4/5, 0, 3/5)`, `b1 = (4/5, 0, −3/5)` [X `experiments/b1_hidden.py` H2a].
3. So no hidden model with the following four properties realizes the CHSH experiment on `phiW`:
   - product configuration space `Λ_A × Λ_B`;
   - local response functions for these four effects;
   - token operations acting as `π × id`;
   - measurement-independent preparations.

   Such a model has `|S| ≤ 2` (H2b; [W]). This holds for `Q3` and for every exotic cone alike.
4. With all hidden distributions available and ontic points in the ball, no hidden permutation realizes `cnot`: the
   hidden cone lies in `⟨w, ·⟩ ≥ 0` for `w = E00 − E11 + E22 − E33`, while `⟨w, phiW⟩ = −2` [X H1c].

**Consequence (assumption-watch marker).** Read operationally, GR.md:326 says "the tensor product structure follows from
the spatial product structure of the classical configuration space". So read, it is this locality of registers, and it
is Bell-local by the framework's own theorem (Main.md:360–371). The entangled sector of the composite requires the
branch-(a) nonlocal response (Main.md:392). As a level-M carrier statement, GR.md:326 is correct.

Manuscript propagation item: recorded, not applied (manuscript hold).

Evidence: `NOTES-B1.md` §3, §5; `experiments/b1_hidden.{py,out,replay.out}` (17/17, replay byte-identical).
