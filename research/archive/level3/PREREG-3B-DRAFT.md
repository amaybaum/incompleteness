# Level 3B — orthogonal substrate controls under a fixed interface (DRAFT preregistration; not frozen; nothing run)

Base `0f2687b7`. Read-only, off-repo. This draft is completed and frozen only after 3A has fixed the interface
class I₃ (its letter set, κ sweep and horizons) and only on owner direction. It records the design, its
predictions, and the decisions the owner must take before the freeze. Written before any Level-3 computation.

## 1. The question

With the interface I₃, the observer OBS-R, the measured effect r, the hidden-law class and the evidence rules
held identical across every cell, what in the substrate rule causes the rank behaviour: linearity (A5), the
absence of self-coupling (A4-S), both, or a property neither names?

## 1a. Owner decisions (2026-10-03)

- **D1** adopt R_5 — yes. **D2** all 143 κ per newly run cell; the OVER-RANK controls keep only the replay control.
- **D3** H₁ = stationary unbiased binary Markov chain with P(v_{i+1} = v_i) = 3/4; H₂ as the null control.
- **D4** H block at Stage A (3, 3) only, all 143 κ if feasible, with conservative semantics: certified rank > 4 is
  informative and terminal; rank ≤ 4 at this horizon means only "no OVER-RANK detected at Stage A" — never
  preservation of the ceiling, AT-RANK, or a null interaction.
- **Edge-permutivity is a named factor** of Block 1 (column of §2), not explanatory prose: the class forbids a
  full A5 × A4-S × permutivity factorial, and R_5 supplies the one extra comparison that decides whether the
  apparent A5 effect is a permutivity effect.

## 2. Block 1 — the rule matrix

All rules are second-order leaps v^{t+1} = F(v^t) + v^{t−1} mod 2 (bijective for every F, so A2 holds in every
cell), translation-invariant, radius 1, on the same lattice with the same product initial measure H₀.

| Cell | F | A5 | A4-S | Edge-permutive | Status under I₃ |
|---|---|---|---|---|---|
| R_LL | v_{i−1} + v_{i+1} | kept | kept | yes (both edges) | from 3A; not rerun |
| R_LS | v_{i−1} + v_i + v_{i+1} | kept | violated | yes | **run** |
| R_NL | v_{i−1} v_{i+1} | violated | kept | no (necessarily, §3) | **run** |
| R_NS-n | v_{i−1} v_{i+1} + v_i (RECORD's nonlinear) | violated | violated | centre-permutive only | OVER-RANK for every κ by monotonicity (iii) from Level 2; replay control only |
| R_NS-m | maj(v_{i−1}, v_i, v_{i+1}) (RECORD's majority) | violated | violated | no | OVER-RANK for every κ by monotonicity (iii); replay control only |
| **R_5** (proposed) | v_{i−1} + v_i v_{i+1} | violated | violated | yes (left edge) | **run** if adopted |

R_LL, R_LS, R_NL, R_NS are the owner's 2 × 2. R_NS needs no new run under I₃: G₂ ⊆ G₃ with the same κ, so the
Level-2 certified lower bounds > 4 already exclude R4(r; G₃) there; a small replay (three κ) is kept as a
positive control that the pipeline reproduces OVER-RANK.

## 3. Design finding before any run: the 2 × 2 is confounded with edge-permutivity

The mechanism predicted in PREREG-3A §8 for the linear rule's rank ceiling is **edge-permutivity**: F has
coefficient 1 in an edge variable v_{i±1}, so every leap adds a cone-edge initial variable that is independent of
everything observable, and all hidden correlation is masked. Linearity is sufficient for it but not what the
argument uses.

In the radius-1 binary class the cells are not independent of this property:

- A rule without the self variable is a Boolean function of two bits, F(v_{i−1}, v_{i+1}). If it is permutive in
  one argument it has the form x ⊕ h(y) with h a function of one bit, hence affine. **So (A5 violated, A4-S kept)
  forces non-permutive.** R_NL cannot be edge-permutive, whatever nonlinear F is chosen for it.
- A nonlinear edge-permutive rule must use the self variable: F = v_{i−1} ⊕ h(v_i, v_{i+1}) with h nonlinear,
  e.g. R_5 = v_{i−1} + v_i v_{i+1}. **So the only place edge-permutivity can be separated from A5 is the
  (A5 violated, A4-S violated) cell**, which the 2 × 2 fills with two non-edge-permutive rules.

Exact checks (design arithmetic, 2026-10-03): all four two-variable Boolean functions permutive in one argument
are affine; the permutivity column of §2 was verified by enumeration (R_LS is permutive in all three variables,
R_5 in the left edge only, R_NS-n in the centre only, R_NL and R_NS-m in none).

Consequence for attribution, fixed now as the decision table (criterion once frozen):

| Outcome pattern (all κ, Stage B) | Reading |
|---|---|
| R_LS ≤ 4, R_NL > 4, R_5 ≤ 4 | rank behaviour tracks edge-permutivity; neither A5 nor A4-S is the operative axis |
| R_LS ≤ 4, R_NL > 4, R_5 > 4 | A5 (linearity proper) or an A5 × A4-S interaction; permutivity alone insufficient |
| R_LS > 4 | A4-S matters even for a linear, edge-permutive rule; the masking lemma of 3A §8 is wrong in its stated generality |
| R_NL ≤ 4 | the masking mechanism is not necessary for a rank ceiling; new finding |

Predictions (not criteria): R_LS ≤ 4 and R_5 ≤ 4 (masking holds for both, left-edge permutivity suffices);
R_NL > 4 (no fresh variable; the product of the edges carries hidden correlation into every reading, as RECORD
found for the non-permutive controls). If these hold, the first row of the table is the reading, and the result
is that RECORD's A5-versus-A4-S question had a third answer.

**Owner decision D1:** adopt R_5 as a fifth cell (recommended: without it the 2 × 2 cannot distinguish "linear"
from "edge-permutive", and the predicted outcome of the 2 × 2 alone would be read as "A5 is operative").

## 4. Held identical across all cells (no exceptions)

Interface I₃ = IC (143 κ) × {f, s, c} as frozen by 3A; observer OBS-R; r = (o, outcome 1); H₀; preparation and
effect family rules; L_p, L_e per stage as 3A (A: 3, 3; B: 4, 4; C: 4, 5 on the same selection rule); rank
certification, WELLDEF guard, evidence classes, per-κ verdicts and the replay plan (one fixed κ per cell on the
reference simulator; the nine fixed Stage-A positions per cell). Cell labels: EXPOSED / NOT-EXPOSED / OVER /
INCONCLUSIVE as 3A §5.

**Owner decision D2:** κ sweep per cell — all 143 (recommended, ~3 × 25 min at Stage A; Stage B only for
advancing κ) or the 3A-AT-RANK set only.

## 5. Block 2 — the hidden-law factor H (after Block 1 is read)

Design (A5, A4-S [, permutivity]) × H, with the rule cells of Block 1 and H varied as a separate factor, so that
the three questions — what the rule does, what the hidden law does, whether they interact — are answered
separately.

Candidate classes:

| H | Initial measure | Predicted effect on edge-permutive cells | Role |
|---|---|---|---|
| H₀ | uniform product on (u_i, v_i) | ceiling 4 (3A) | baseline |
| H₁ | v^0 a translation-invariant two-state Markov chain along the lattice with P(v^0_{i+1} = v^0_i) = 3/4, u^0 uniform product independent | masking fails: the edge variable v^0_{t+1} is correlated with v^0_t, which lies inside the observed cone; rank may exceed 4 even for R_LL | the informative variation |
| H₂ | u^0_i = v^0_i (equal time slices), v^0 uniform product | masking holds: the edge variable still enters with coefficient 1 and is independent | control predicted not to matter |

Interaction prediction (not a criterion): the rule × H interaction is real for edge-permutive rules (H₁ lifts
their ceiling) and absent for non-permutive rules (already > 4 under H₀). This is the H-T1 point — correlated
hidden preparations change what the observer can see — in the only place in Level 3 where it can be tested.

Simulator constraint: the exact window simulator's correctness rests on the product measure (sites beyond the
window uniform and independent). H₁ and H₂ need exact full-cone enumeration with integer weights (3 : 1 for H₁),
feasible for total leaps ≤ 6, i.e. Stage A only (L_p = L_e = 3). The new enumerator must agree with the window
simulator on H₀ (built-in control) before any H₁/H₂ run.

**Owner decisions D3–D4:** the H classes and parameter (H₁ at 3/4 recommended; H₂ as the null control); the
horizon (Stage A only, given the enumerator cost).

## 6. Interpretation limits

As 3A §7, plus: Block 1 attributes rank behaviour to rule properties within the radius-1 binary second-order class
under I₃ and H₀ only; it establishes nothing about other interfaces, observers or hidden laws, and nothing about
QM. Block 2's negative results (an H class that does not matter) are stated for that class only.

## 7. To be filled at the freeze

I₃ as frozen by 3A (letter set, κ sweep, horizons); the Stage-C selection rule carried over; the decisions D1–D4;
code hashes before the first run; the 3A result's label, which this round does not reinterpret.
