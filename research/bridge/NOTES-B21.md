# NOTES-B21 — an explicit exotic cone for the tower's closure: what a seed must satisfy

Node B21 of `research/bridge` (round 5, last in priority: "if time remains"). Base L = `9f9f8257`. Evidence levels as
in NOTES-B14. Reading: every statement of this node is an invariance statement (which cones a group of conjugations
preserves); none is about operational availability. Received handoffs used at their labels (LOG, round 5): HO-31 items
1–3 (Theorem C19-1; the Clifford chain; Lemmas C18-1 … C18-3 and the two assumption-watch markers); HO-30 item 1
(Theorem S′, finite form, [D]); HO-32 items 1–4 (the explicit cones against Table A2). Authorized cross-branch reads
(LOG, 08:11:09Z): `research/countermodels` @ `644bf0a1` — NOTES-C18, NOTES-C19, `c18_attempts.py`, `c19_groups.py`,
read for Lemma C18-1's exact statement and witness, the product and orthogonal-pair tests of C19, and the balanced
engine's conditions; nothing is copied.

## 0. Question

B10-4's group `G = closure ⟨cnot, actT nflip, actT R_z(t) for all t⟩` is the closure of the locally finite tower of
B10-5 (B17-1), with identity component the abelian 2-torus `T² = {exp(i(a Z_B + b Z_A Z_B))}` (B10 T9 [X]). B7-2 says
it leaves an exotic cone, CONDITIONAL on claim (D) [A] — "a group of identity-component dimension two". The directive:
state exactly what an explicit invariant exotic cone must satisfy — the orbit structure of a candidate seed under the
torus, the orthogonal-pair obstruction (HO-31 item 3, Lemma C18-1), the balanced engine (C18-2(b)) — and either give a
seed meeting the obstruction's conditions with exact checks, or the obstruction, to move claim (D) towards explicit.

## S0. Design, productivity test and predictions (written 2026-10-11T08:15:54Z, before any run; no dispatch)

**Design.**
- **The group, explicitly.** On the matrix side (HO-21's conjugation formulas, one dictionary [D]): `CNOT`,
  `X_B = 1 ⊗ X`, `1 ⊗ diag(1, e^{it})`. Written claim G1: `1 ⊗ diag(1, e^{it}) = e^{it/2} · diag(e^{−it/2}, e^{it/2},
  e^{−it/2}, e^{it/2})` lies in `T² = {U(u, v) = diag(e^{iu}, e^{−iu}, e^{iv}, e^{−iv})}` modulo a scalar (`u = v =
  −t/2`), its `CNOT`-conjugate too (`u = −t/2, v = t/2`), and `CNOT`, `X_B` normalize `T²` (`CNOT` swaps `u ↔ v`,
  `X_B` negates both), commute and square to `1`; so `G = T² · {1, CNOT, X_B, CNOT·X_B}` modulo scalars: four
  components, the identity component `T²` of dimension two (B10-4's statement, now with the component group).
- **Orbit structure of a seed `h` under `G`**: four torus orbits, `T²·h`, `T²·CNOT h`, `T²·X_B h`, `T²·CNOT X_B h`.
  Products in the orbit (written claim G2): `U(u, v) h` is a product iff `e^{i(u−v)} h₀₀h₁₁ − e^{i(v−u)} h₀₁h₁₀ = 0`,
  which has a solution iff `|h₀₀h₁₁| = |h₀₁h₁₀|`; with the `CNOT` image (`h₁₀ ↔ h₁₁`) the `G`-orbit is product-free iff
  `|h₀₀h₁₁| ≠ |h₀₁h₁₀|` and `|h₀₀h₁₀| ≠ |h₀₁h₁₁|` (the `X_B` images give the same two conditions).
- **The orthogonal-pair obstruction is universal for `G`** (written claim G3, the candidate NEW): for every unit `h`,
  `⟨h | U(u, v) X_B h⟩ = 2 Re(h̄₀₀ h₀₁ e^{iu}) + 2 Re(h̄₁₀ h₁₁ e^{iv})`, and `u`, `v` can be chosen to make each term
  vanish; so every `G`-orbit contains an orthogonal pair `(h, g h)`. With Lemma C18-1 (HO-31 item 3(a), [W] at its
  label: a set of rank-one defects with values in `(1, 2)` whose orbit of largest `c` contains an orthogonal pair
  has a non-self-dual surgery; the values are constant on orbits), no rank-one surgery `K(Z)` with `c ∈ (1, 2)` on a
  `G`-invariant defect set is self-dual — for every seed, every weighting, finite or compact. The exact instance is
  built here with C18-1's own witness `y = P_h + λ d_{h′}`, `λ = (c* − 1)/(4 − 2c*)`.
- **`c = 2`.** Pairwise pairings of distinct rays are `⟨d_j, d_k⟩ = 4(s_{jk} − 1) < 0` at `c = 2`, so Theorem S′ (finite
  or compact form) does not apply, and C18-1 does not apply either (`c* < 2` is its hypothesis); K(Z_F) is the
  model of a `c = 2` surgery whose self-duality was established by other means [A]. For `G` a product-free orbit at
  `c = 2` exists (G2 with the seed `(2, 1, 1, 0)`), and the Bell circles are excluded (`CNOT` carries a Bell state to
  a product). No sufficiency engine decides a `c = 2` surgery on a product-free `G`-orbit: OPEN.
- **The balanced engine** (C18-2(b)): zero pairing on every orthogonal pair and strict room at cap boundaries at once;
  on a torus continuum the countermodels thread found the local condition broken by nearby pairs (A2b-near). Not
  re-derived here; the conditions are listed, and G3 says the orthogonal pairs are present for every seed.
- **Script** `experiments/b21_torus.py` (sympy, exact; torus points at Gaussian-rational points of the circle
  `{±1, ±i, (3 ± 4i)/5, (4 ± 3i)/5}`): (T1) G1 symbolically in `t, u, v`; (T2) G3 symbolically (real and imaginary
  parts of `h` as symbols) and the exact instance `h = (1, 1, 2, i)`, `U = diag(i, −i, 1, 1) ∈ T²`,
  `⟨h | U X_B h⟩ = 0`; (T3) G2 symbolically; the product-free seed `(2, 1, 1, 0)` (both inequalities, on all four
  components) and the countercontrol `(1, 2, 2, −4)` (`|h₀₀h₁₁| = |h₀₁h₁₀| = 4`, an exact product reached at
  `U = diag(i, −i, 1, 1)`); (T4) the `c = 2` pairing law symbolically; (T5) C18-1's witness at `c* = 51/50` on the
  seed of T2: `⟨y, d_h⟩ = 0`, `h′† y h′ < 0`, and `⟨y, d⟩ ≥ 0` for every sampled orbit defect (the four components at
  the 64 Gaussian-rational torus points), the sampled form of the lemma's identity.
- **Decision rule**: `VERDICT B21-EXACT` iff T1–T5 pass; then G1–G3 are recorded as CONJECTURE (exact computation and
  written proof), the obstruction as CONDITIONAL on Lemma C18-1 [W] at its label, the `c = 2` and balanced routes as
  OPEN, and existence of an exotic cone for `G` stays at claim (D) [A]. A failure of T2 withdraws G3.

**Productivity test (§A.31), fixed now.** B21 is a gem iff it yields more than "the orthogonal-pair obstruction applies
to this group too": G3's universality — every seed, through the NOT of the tower itself, with no eigenline group
needed — would be NEW (it constrains every surgery-type construction for the tower's closure at once); otherwise
CONFIRMING.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | G1: the generators lie in `T² · {1, CNOT, X_B, CNOT X_B}` modulo scalars; `CNOT` and `X_B` normalize `T²`, commute, square to `1` | T1 |
| S0-2 | G3: the orthogonality identity holds symbolically; the exact instance gives `0` | T2 |
| S0-3 | G2: the product criterion; `(2, 1, 1, 0)` product-free on all four components; `(1, 2, 2, −4)` reaches an exact product | T3 |
| S0-4 | at `c = 2` the pairing of distinct rays is `4(s − 1) < 0` | T4 |
| S0-5 | C18-1's witness: `⟨y, d_h⟩ = 0`, `h′† y h′ = λ(1 − c*)|h′|² < 0`, `⟨y, d⟩ ≥ 0` on all 256 sampled defects | T5 |
| S0-6 | Outcome: the obstruction, not a seed — no rank-one surgery with `c < 2` is self-dual for `G`; `c = 2` and balanced routes OPEN; existence at claim (D) | §2 |
| S0-7 | Gem: NEW for G3's universality, otherwise CONFIRMING | §3 |
