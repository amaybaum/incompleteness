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

### S0 addendum (written 2026-10-11T10:18:06Z, after run 3 of `b21_torus.py`, before any run of `b21_ceq2.py`)

S0's design left the `c = 2` case OPEN ("no sufficiency engine decides a `c = 2` surgery on a product-free
`G`-orbit"). One written argument closes it on the side that matters for self-duality, and is checked here before
the outcome is written. **Claim G4.** Let `Z` be a `G`-invariant set of rank-one defects `d = I − cP_h` with H1
(I3.147: products in `K`). If `K(Z)` is self-dual (H3, I3.149), every defect pairs nonnegatively with every product
state (`d ∈ Z ⊆ K = K*` and the products lie in `K`), so `c · max_prod |⟨a ⊗ b|h⟩|² ≤ 1`; at `c = 2` every element of the
orbit is maximally entangled, `|D(gh)| = |h|²/2` with `D(h) = h₀₀h₁₁ − h₀₁h₁₀`. No `G`-orbit has this property:
`|D(U(u, v)h)|² = |h₀₀h₁₁|² + |h₀₁h₁₀|² − 2 Re(e^{2i(u−v)} h₀₀h₁₁ \overline{h₀₁h₁₀})` is constant in `u − v` only if
`h₀₀h₁₁ · \overline{h₀₁h₁₀} = 0`, and then `|D| = |h|²/2` forces (AM–GM) `h = (h₀₀, 0, 0, h₁₁)` with
`|h₀₀| = |h₁₁|` or `h = (0, h₀₁, h₁₀, 0)` with `|h₀₁| = |h₁₀|`, whose `CNOT` images `(h₀₀, 0, h₁₁, 0)`,
`(0, h₀₁, 0, h₁₀)` are products. So a self-dual `G`-invariant rank-one surgery with H1 has every `c < 2`, and with
G3 and Lemma C18-1 (HO-31 item 3(a), [W] at its label) none exists when the largest `c` is attained (finitely many
orbits, or `Z` compact): **the rank-one surgery route is closed for `G`**, CONDITIONAL on C18-1. Script
`experiments/b21_ceq2.py` (exact): (Q1) the two modulus identities, for `U(u, v)h` and for `CNOT U(u, v)h` (where
`u + v` replaces `u − v`), symbolically; (Q2) the case analysis on its algebraic core, exactly: for a normalized `h`
with `h₀₁h₁₀ = 0` and `|h₀₀h₁₁| = 1/2`, `|h₀₁|² + |h₁₀|² = 1 − (|h₀₀|² + |h₁₁|²) = −(|h₀₀| − |h₁₁|)² ≤ 0` (the same
with the roles exchanged), symbolically in the moduli; (Q3) the four Bell states: each `CNOT` image is an exact product
(`D = 0`) and its defect at `c = 2` pairs `−1` with that product; (Q4) countercontrol: without `CNOT` the orbit of
`Φ⁺` under `T² · ⟨X_B⟩` is maximally entangled at the 64 sampled torus points (`|D|² = 1/4` exactly), so `CNOT` is
load-bearing. Decision rule in the script's header.

Added predictions:

| id | prediction | check |
|---|---|---|
| S0-8 | G4: the modulus identities hold symbolically; the case analysis reduces to `−(|h₀₀| − |h₁₁|)² ≤ 0`; each Bell state's `CNOT` image is a product with pairing `−1`; the local countercontrol keeps `|D|² = 1/4` | Q1–Q4 |
| S0-9 | Outcome: the rank-one surgery route closed for `G` (CONDITIONAL on C18-1 [W]); existence of an exotic `G`-invariant cone stays at claim (D) [A]; the `c = 2` part of S0-6's "OPEN" withdrawn | §1 |

## 1. Outcome (written 2026-10-11T10:27:03Z)

**The runs.** `b21_torus.py`: run 1 (08:23:01Z) 4/5, VERDICT B21-FAILED T5, and run 2 (08:24:46Z), the same — both
failures of T5's identity sub-check on 8 of 256 samples were arithmetic artifacts (a float from Python integers; then
`nsimplify` returning a spurious radical for an exact rational), every pairing exact and `≥ 0`; kept as `.run1.*`,
`.run2.*`; run 3 (08:26:36Z) 5/5, VERDICT B21-EXACT, replay byte-identical (08:26:52Z). The header's rule stamp
"08:24:00Z" is wrong: the rule was written after the reading 08:22:02Z and before run 1 (LOG, timestamp corrections).
`b21_ceq2.py` (the S0 addendum): run 1 (10:19:44Z) 4/5, VERDICT B21-CEQ2-FAILED Q1 — the header and the code stated the
second modulus identity for `U(u, v) CNOT h`, where it is false with the phase `e^{2i(u+v)}`; the addendum, written
before run 1, specifies `CNOT U(u, v) h`; kept as `.run1.*`; post-run edit to the addendum's form (logged in the header;
the rule text of Q1 changed to the pre-registered statement, Q2–Q5 unchanged); run 2 (10:20:33Z) 5/5, VERDICT
B21-CEQ2-EXACT, replay byte-identical (10:20:35Z).

| id | outcome |
|---|---|
| S0-1 | confirmed [X] T1. The design paragraph's "`CNOT` swaps `u ↔ v`" holds in B10's coordinates `(a, b)` of `exp(i(aZ_B + bZ_AZ_B))` (`u = a + b`, `v = a − b`); in `(u, v)`, `CNOT U(u, v) CNOT = U(u, −v)`, as T1 checks |
| S0-2 | confirmed [X] T2: the identity symbolically; `⟨h | U X_B h⟩ = 0` at `h = (1, 1, 2, i)`, `U = U(π/2, 0)` and at `h = (1, 2, 3, 4)`, `U = U(π/2, π/2)` |
| S0-3 | confirmed [X] T3 |
| S0-4 | **FAILED as written.** The pairing of two defects is `4 − 2c + c²s`, which at `c = 2` is `4s ≥ 0`, not `4(s − 1) < 0` (T4; the header's law, corrected in the design before run 1). The inference S0 drew from it — Theorem S′ does not apply — survives for another reason: on a positively paired pair (CC) in inequality form reads `4 ≤ 4s` at `c = 2`, forcing `s = 1`, so S′ applies to a `c = 2` defect set only if its distinct rays are pairwise orthogonal |
| S0-5 | confirmed [X] T5: `λ = 1/98`, `⟨y, d_h⟩ = 0`, `h′†yh′/|h′|² = −1/4900 = λ(1 − c*)`, minimum sampled pairing `0`, C18-1's identity on all 256 samples |
| S0-6 | confirmed and sharpened: the obstruction, not a seed; the `c = 2` part of "OPEN" withdrawn by G4 (S0-9); the balanced route is not examined for `G`; existence stays at claim (D) [A] |
| S0-7 | **not confirmed as NEW**: G3's mechanism is the eigenline group (§3); the outcome is ELABORATING |
| S0-8 | confirmed [X] at `b21_ceq2.py` run 2: Q1–Q5; Q5: of the 390624 nonzero `h` with Gaussian-integer components in `{−2, …, 2} + i{−2, …, 2}`, none has a maximally entangled `G`-orbit, while 256 have a maximally entangled `T² · ⟨X_B⟩`-orbit (the countercontrol: `CNOT` is load-bearing) |
| S0-9 | confirmed (§2) |

## 2. What an explicit exotic `G`-invariant cone must satisfy

Reading: invariance throughout. `G` = B10-4's group, the closure of B10-5's tower, on the matrix side through HO-21's
conjugation formulas and the one dictionary [D].

- **G1, the group** (CONJECTURE: [X] T1 + [W]). `G = T² · {1, CNOT, X_B, CNOT X_B}` modulo scalars: identity component
  `T² = {U(u, v)}` (B10 T9), component group `ℤ/2 × ℤ/2`. On the four eigenlines of `T²` (the basis rays) `CNOT` acts as
  `(34)`, `X_B` as `(12)(34)`, `CNOT X_B` as `(12)`: the eigenline group of `G` is `Π = ⟨(12), (34)⟩`.
- **G2, products in an orbit** (CONJECTURE: [X] T3 + [W]). `U(u, v)h` is a product iff
  `e^{i(u−v)}h₀₀h₁₁ = e^{−i(u−v)}h₀₁h₁₀`, solvable iff `|h₀₀h₁₁| = |h₀₁h₁₀|`; the `G`-orbit of `h` is product-free iff
  `|h₀₀h₁₁| ≠ |h₀₁h₁₀|` and `|h₀₀h₁₀| ≠ |h₀₁h₁₁|`. The seed `(2, 1, 1, 0)` is product-free; `(1, 2, 2, −4)` reaches the
  exact product `(i, 2) ⊗ (1, −2)`. Every product-free orbit is infinite (a ray fixed by `T²` is a basis ray, a product).
- **G3, orthogonal pairs** (CONJECTURE: [X] T2 + [W]). `⟨h | U(u, v) X_B h⟩ = 2 Re(h̄₀₀h₀₁e^{iu}) + 2 Re(h̄₁₀h₁₁e^{iv})`;
  each term vanishes for a suitable angle, so every `G`-orbit contains an orthogonal pair `(h, U X_B h)`.
- **G4, no orbit at `c = 2`** (CONJECTURE: [X] Q1–Q5 + [W]). If a surgery `K(Z)` with H1 (I3.147) is self-dual (H3,
  I3.149), every defect pairs nonnegatively with every product (`d ∈ Z ⊆ K = K*`, products in `K`); at `c = 2` this makes
  every element of the orbit maximally entangled. Constancy of `|D(U(u, v)h)|` in `u − v` forces
  `h₀₀h₁₁ · \overline{h₀₁h₁₀} = 0`, normalization then forces `h = (h₀₀, 0, 0, h₁₁)` with `|h₀₀| = |h₁₁|` or
  `h = (0, h₀₁, h₁₀, 0)` with `|h₀₁| = |h₁₀|`, and `CNOT` carries each to a product. No `G`-orbit is admissible at `c = 2`.
- **The obstruction** (CONDITIONAL on Lemma C18-1, HO-31 item 3(a), at its label CONDITIONAL [W]): *let `Z` be a
  `G`-invariant set of rank-one defects `I − cP_h`, every `c ∈ (1, 2]`, with finitely many orbits or `Z` compact, and let
  `K(Z)` satisfy H1. Then `K(Z)` is not self-dual.* If it were, G4 would put every `c` in `(1, 2)`; the largest value is
  attained on one orbit, which carries an orthogonal pair (G3); C18-1 then makes `K(Z)` not self-dual. The exact instance
  of C18-1's witness for `G` is T5's.
- **Theorem S′ at `c = 2`** ([D] HO-30, through T4 [X]): in the inequality form of (CC), S′ applies to a `c = 2` defect
  set only if its distinct rays are pairwise orthogonal, which an infinite orbit in `ℂ⁴` cannot be.

So an explicit exotic `G`-invariant cone is not a rank-one surgery of this kind: it needs defects of rank two or more
(the balanced engine, C18-2(b): failed as a construction on case B's torus orbits in the countermodels thread, not
examined here for `G`), infinitely many orbits whose supremum of `c` is not attained, or a construction other than
surgery. Existence of an exotic `G`-invariant cone stays at claim (D) [A] (B7-2); this node moves the explicit status
by closing one route, not by a seed.

## 3. Gem classification (§A.31)

**ELABORATING.** The productivity test called G3 NEW only "with no eigenline group needed"; that clause fails — the
NOT of the tower, `X_B`, is the double transposition `(12)(34)` of the torus eigenlines, and `G`'s eigenline group is
case B's `Π = ⟨(12), (34)⟩` (NOTES-C18 R0, C13-Π). The node does yield more than "the orthogonal-pair obstruction applies
to this group too": with G4 (the counterpart for `G` of the countermodels thread's C16.2 for `G_B`), the rank-one surgery
route is closed for the tower's closure as a whole, the countermodels thread's corollary for `G_B` (NOTES-C18, after
Lemma C18-1) now holding for `G` by the same mechanism. Whether `G` is conjugate to a subgroup of `G_B` was not
examined. Cross-propagation: for countermodels C23 (this round, the same group), an explicit cone cannot be a rank-one
surgery with attained maximum `c`.
