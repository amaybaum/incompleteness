# HP-2 — finite and locally finite substrata cannot carry the sufficient composite actions

From `research/bridge`, node B3. Proposed for the drive-sourcing thread (K∞-Act, K∞-Drive) and for the countermodels
thread. The coordinator routes.

**Proposition HP-2a (fixed finite pair substratum).**

*Hypotheses.* `cnot` and token operations in the pair context are realized as readout-respecting permutations of a
finite `Λ`, with spanning readout `R : ℝ^Λ → W 3`.

*Conclusions.*
- The realized group on `W 3` is finite [W: a homomorphic image of a subgroup of `Sym(Λ)`].
- If it consists of unitary or antiunitary conjugations, claim D (Z/RESULT.md §1.0 [A]) gives an exotic self-dual
  invariant cone with H1–H3.
- So (b), granted for every realized operation, does not force `Q3`.

*Native instance.* `⟨cnot, local octahedral rotations⟩` has order 11520 [X `experiments/b3_finite.py` X2].

**Proposition HP-2b (R1 and the gate).**
- `R1 = (1/9)[[8,1,4],[4,−4,−7],[1,8,−4]]` is the order-3 rotation about (5,1,1). Together with `cnot` it forces `Q3`
  (stage 4 Y7 [A]).
- It is realized on an 18-point ontic token [X3].
- But `tr(cnot · actC R1) = 10/9 ∉ ℤ` [X4], so `⟨cnot, actC R1⟩` is infinite. `R1` and `cnot` are therefore never
  realized together on a finite pair substratum.

**Proposition HP-2c (directed towers; CONDITIONAL on Jordan's theorem [L]).**
- The closure of a directed union of finite pair groups has abelian identity component.
- Hence no tower realizing `cnot` realizes any of:
  - an off-frame local circle: `[A_n, cnot A_n cnot] ≠ 0` for `n = (3/5, 0, 4/5)` [X6];
  - two non-commuting local circles (A_miss);
  - `R1`.
- On one token, an increasing chain of finite subgroups of `SO(3)` ends cyclic or dihedral about one axis. So off-axis
  `ElementaryDrivability` (KInfFoundations.lean:264) is never the closure of directed stage-preserving finite
  operations. This sharpens F-D3: the generator must cross stages.

**Proposition HP-2d (A_miss as rational matrices).**
- By closure, A_miss ⟺ (b) for `{R_z(θ), R_x(θ)}` with `cos θ = 3/5` (`tr = 11/5`, infinite order).
- K(Z_F) is moved out by each of the following, with certified witnesses [X5, X7]:
  - `R_z(θ)`: `−1/10`;
  - `S`: `−1/8`;
  - `R1`: `−79/720` (new; R6 recorded `−2383/5316` with another witness).

**Open (CONJECTURE B3.C).** Does every compact pair group containing `cnot` with abelian identity component leave an
exotic invariant cone?

Evidence: `NOTES-B3.md`; `experiments/b3_finite.{py,out,replay.out}` (11/11; run 1 kept).
