# P2: periodic orbits with excursions in small finite configurations of Q (preregistration)

**Standing.** Design and preregistration only, authorized by owner decision
[#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074)
item 3.4. Execution (an exhaustive search) is not authorized. The object is the native rule's
working reference implementation, Q = `R_{2^16}` on `ℤ³` (decision 3.2), at the uniform background
`c = 2^15`. Notation: MQ = MEAS-Q `RESULT.md` §2 (closed set, `cl₂`, boundary layer `∂D`, MQ1,
MQ2); NU2 = `NOTE.md` §3.2.

## 1. Question

Among the finite configurations of §2, are there orbits that are **periodic with an excursion**?
Such an orbit has bounded support (so it is periodic, by NU2), and at some tick `t` the instantaneous
closed hull `D_t = cl₂(supp(x_{t−1}) ∪ supp(x_t))` has a boundary-layer site whose *current-slice*
value `x_t` lies outside `[c−1, c+1]`. This is MQ2's hypothesis, which restricts only the current
slice; out-of-range previous-slice values alone are not an excursion.

**Why it matters.** By NU2, a finite configuration cannot breach and then stay confined in a set it
had escaped, so "bounded breach" for a finite gadget means exactly this. A periodic orbit with an
excursion would be a breach that does not spread: a candidate ingredient for U1's missing block.
It would also refute P3's Conjecture S for that configuration. Using such an ingredient in a turn
is step-2 work.

## 2. Search set (frozen here)

- **Shapes.** Every set of `k ≤ 3` sites with ℓ∞-diameter at most 2, taken up to translation and
  the cubic group `O_h`. The script enumerates them and checks their number against a Burnside
  count.
- **Values.** Each of the `2k` slots (previous and current slice) takes a value `y = x − c` in
  `{−2, −1, 0, 1, 2}`. At least one slot is nonzero, and the configuration is not identically
  ternary at both slices. The ternary sector is MQ's confined case, already covered by MQ S-A.
- **Run.** Q itself, mod `2^16`, on a torus of side `2 R_max + 5` with `R_max = 12`, to at most
  `T_max = 4096` ticks.

## 3. Decision rule (fixed now)

Each configuration receives exactly one class:
- **P (periodic):** the two-slice state returns exactly to its initial state at some tick
  `t ≤ T_max`, and the support stays within ℓ∞-radius `R_max` of the shape's centre throughout.
  The class carries the flag **exc** iff some tick `t < P` has an excursion (§1).
- **G (growing):** the support reaches ℓ∞-radius `R_max + 1` at some tick `t ≤ T_max`, before any
  return. This is evidence of spreading, not a proof that the support is unbounded.
- **U (undetermined):** neither by `T_max`.

**Output:** the counts of P, P-exc, G and U per shape, and the full list of P-exc configurations
with their periods. If the P-exc count is zero, the output is "no periodic orbit with an excursion
in the search set of §2", and nothing beyond that set is stated. The verdict text is generated
from the counts. If any control in §4 is not green, no verdict is printed.

## 4. Controls and countercontrols

| Id | Kind | Requirement |
|---|---|---|
| P2-K1 | sharpness of the breach test | MQ1's converse re-run exhaustively (all `q` values of the one perturbed neighbour) at `c = 2^15` |
| P2-K2 | known P without excursion | a ternary singleton `(a, b) ∈ {−1,0,1}² ∖ {(0,0)}` is P, period 4, no excursion (U1 E3, MQ5) |
| P2-K3 | known breach | a singleton with current value `c + 2` (MQ CC5) has an excursion at tick 0, and is classified G or U, never P without the flag |
| P2-K4 | countercontrol for G | the linear member `L_{2^16, 3^{−1}}` from the singleton seed `(0, 1)` on the uniform background `0` (a fixed point of the linear rule) is G (it spreads at once, U2 N4); this shows the G test fires |
| P2-K5 | countercontrol, background | the seed `(0, 1)` on the vacuum `c = 0` is G (U1 C2: support radius `t − 2` for `3 ≤ t ≤ 20`) |
| P2-K6 | excursion detector | synthetic histories with and without an excursion are classified correctly. This calibrates the implementation only: no in-rule periodic orbit with an excursion is known in advance, so a zero P-exc count is calibrated only by K6 and K3 |
| P2-K7 | no wrap-around | a seeded sample of 200 configurations, re-run on a torus four sites larger, gets the same class and the same first-event tick |

## 5. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint that measures it |
|---|---|
| The preregistration precedes the search | this file's commit is an ancestor of the first execution commit, which changes nothing in `plans/` |
| The enumeration is complete | shape count equals the Burnside count; the value count equals `5^{2k}` minus the excluded cases, asserted per shape |
| Updates are exact on `ℤ³` | G fires at the first tick the support reaches radius `R_max + 1`; before that, every nonzero site lies within `R_max`, and the torus side `2 R_max + 5` keeps every neighbour unwrapped. K7 checks this on a sample |
| Periodicity certificates are exact | P requires bitwise equality of both slices with the initial state |
| Arithmetic is exact | integer arrays; values reduced mod `2^16` on representatives `0,…,q−1`, as in `papers/main_repro/lyapunov_v3.py:19` |
| Determinism | a full replay gives byte-identical output |
| Controls precede verdicts | the verdict is printed only after K1–K7 hold |

## 6. Cost class (§A.40)

CI. There are on the order of `10^5` configurations, each up to 4096 ticks on a `29³` torus, so
the cost lies beyond a bounded local check. Shard by shape in a matrix, under an owner-approved
dispatch (§A.43 item 4).

## 7. What P2 would and would not establish

- **Would:**
  - exact periodicity certificates for the P configurations;
  - the list of periodic orbits with excursions in the search set, or their absence from it;
  - evidence, not proof, of spreading for the G configurations.
- **Would not:**
  - unbounded growth of any configuration;
  - anything outside §2, such as larger shapes, wider value ranges, other backgrounds,
    configurations with infinite components, or other `q`;
  - a turn, a gate or universality of Q.
