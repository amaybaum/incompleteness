# G3-W1 preregistration: conserved additive quantities of the d = 3 rounded rule

**Standing.** Preregistration of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form, §A.41, §A.44). Committed and pushed before any search on the rounded rule is run. It fixes
the classes searched, the exactness method, the controls, the stopping rule and the decision rule.
It states no expected result for the rounded rule. It adopts no premise and edits no manuscript,
Lean module or registry. WIP / UNVERIFIED.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7033018172](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033018172),
  2026-11-20T07:12:08Z, row G3-W1, `execution`: "Search for conserved quantities in the actual d=3
  rule. It builds on UNIV-2's conserved-density result (A2, #1444) as an input still under review,
  and extends the covered class or proves a stronger theorem rather than repeating the search."
  Scope, [#1169 c.7032429839](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7032429839),
  2026-11-20T06:37:08Z: "G3's first prerequisite: a conserved real energy for the d=3 rounded rule.
  Extend G3-HOM's exact conserved-quantity probe from d=1 to d=3. Either find the conserved additive
  quantities or prove that none exist in a bounded class." "None of these authorizes adopting a new
  physical assumption."
- **Decision rule (fixed by the scope, before any run).** "Counts as a gem only if (i) a conserved
  real energy is identified with its scope, or (ii) an obstruction is proved for a stated class."
  Otherwise the outcome is a scoped recorded negative.
- **Goal link (§A.47).** Serves G3 (#873, the vacuum-energy half of the target): it decides, for the
  classes below, whether the published rounded rule carries a conserved additive real quantity of
  the kind a native energy–momentum source would need, or which class is excluded. It does not
  decide the expansion history or any coupling.
- **Accountable Issues.** #873 (G3), #1169 (OI projection objective).
- **Inputs, with status (§A.46 item 7).** G3-HOM
  (`verification/programmes/gravity/drafts/g3-hom-20261119/RESULT.md`, PR #1430): exact probe of the
  exact linear rule in d = 1; used as method provenance only. UNIV-1
  (`verification/programmes/oi-qm/reconstruction/univ-1-20261119/RESULT.md`): definition of the rule
  Q and the background lemma (its Lemma 2.1); used for the definition only, and the lemma is
  re-checked here (K1). UNIV-2 A2 (PR #1444, branch `research/univ-2-20261120` at `aecc64ef`, under
  independent review): **unverified input**, used only to choose classes that do not repeat it; no
  result here depends on it.
- **Snapshot `D`.** `main` at `b9168ef0408b5f55b935a4df17cb0841877e221a` (the branch base).

***

## 1. Object

Q is the rounded rule `x_{t+1}(n) = ⌊(Σ_{m∼n} x_t(m) + 1)/3⌋ − x_{t−1}(n) mod 2^16` on `ℤ³`, on the
representatives `0, …, 2^16 − 1` (UNIV-1 §1, SM §4.2). RZ is the same update over `ℤ`, with
`G(s) = ⌊(s + 1)/3⌋`. A state is the pair of slices `(p, y) = (x_{t−1}, x_t)`; the map is
`F(p, y) = (y, G(S y) − p)`, with `S` the six-neighbour sum.

Facts used, each re-checked exactly (K1, K2):

- *Value shift.* For every integer `a`, `F(p + a, y + a) = F(p, y) + a` in RZ, since `G(s + 6a) =
  G(s) + 2a`. For the same reason, on configurations with values in `[a − B, a + B]` and
  `B ≤ a ≤ 2^16 − 1 − B` whose image stays in that range, Q coincides with RZ shifted by `a`.
- *Plane-wave reduction.* For a primitive `v ∈ ℤ³`, configurations `y(n) = u(v·n)` are invariant,
  and the reduced map is the one-dimensional rule
  `u'_k = G(Σ_j [u_{k+v_j} + u_{k−v_j}]) − p_k`. Three directions are used:
  `ax = (1,0,0)`: `s_k = u_{k−1} + u_{k+1} + 4u_k`;
  `fd = (1,1,0)`: `s_k = 2(u_{k−1} + u_k + u_{k+1})`;
  `bd = (1,1,1)`: `s_k = 3(u_{k−1} + u_{k+1})`, on which `G` is exact, so the bd reduction is the
  linear rule `u' = u_{k−1} + u_{k+1} − p` (the positive-control rule, §4).
- *Restriction.* A plane wave of 1D period `L` is a periodic configuration of `ℤ³` with `L` sites
  per period. A translation-invariant additive quantity `Φ = Σ_n h(window_n)` of `ℤ³` whose support
  has extent `m` along `v` (the values `v·o` over its support span `m` consecutive integers)
  restricts on these configurations to a 1D additive quantity with an `m`-cell density, with the
  same per-period value. If `Φ` is conserved on all periodic configurations of `ℤ³`, the
  restriction is conserved by the reduced rule on all periodic configurations. RESULT gives the
  proof [W], together with the argument that conservation on all finite-support configurations
  implies conservation on all periodic ones.

## 2. Classes searched

**Triviality.** A quantity is *trivial* on a set of periodic configurations if `Φ(c) = λ·N(c)` there
for one constant `λ`, with `N(c)` the number of sites per period. Constants and coboundaries
(`h = b∘τ − b`, with `τ` a lattice translation) are trivial and conserved by every rule. The
uniform configurations are the `L = 1` plane waves, so a quantity trivial on plane waves is
constant on the homogeneous sector.

**Class Q_v(m, D, μ)** (plane-wave reductions; values range over all of `ℤ`). Densities on `m`
consecutive cells (a cell is the pair `(p_k, u_k)`), each a polynomial of degree `≤ D` in the `2m`
window values whose coefficients are arbitrary rational functions of the residues of those values
mod `μ`. `μ = 1`: polynomial densities. `μ > 1`, `D ≥ 1`: rounding-aware densities. `D = 0`:
arbitrary densities periodic in value with period `μ` (functions of the window mod `μ`). Every
3D density of `v`-extent `≤ m` that is a polynomial of degree `≤ D` in its values, with coefficients
depending on residues mod `μ`, restricts into this class.

Grid, for each `v ∈ {ax, fd, bd}` (fixed; `n` is the number of unknowns
`μ^{2m}·C(2m + D, D)`):

| Family | `(m, D, μ)` |
|---|---|
| G1 polynomial | (2,2,1) (3,2,1) (4,2,1) (2,4,1) (3,4,1) (4,4,1) |
| G2 rounding-aware | (2,2,3) (2,3,3) (2,4,3) |
| G3 periodic in value | (2,0,2) (2,0,3) (2,0,4) (2,0,5) (2,0,6) (2,0,8) (2,0,9) (3,0,2) (3,0,3) (3,0,4) (4,0,2) (4,0,3) (5,0,2) |

**Class P3(D)** (direct 3D, no reduction; values over all of `ℤ`). Densities that are polynomials
of degree `≤ D` in the 14 values of the star (site `n` and its six neighbours, both slices), for
`D ∈ {2, 3}`. **Class P3r(2)**: degree `≤ 2` in the same 14 values, with coefficients depending on
the residues mod 3 of `(S y)_n` and `(S p)_n`, the two quantities whose residues the rounding at
`n` reads. The 3D linear-wave energy `y_n² + p_n² − (1/3) y_n (S p)_n` lies in P3(2).

What these classes add to UNIV-2 A2 (star-local densities, values in `{−1,0,1}` or `{−2,…,2}`,
zero flux): flux is allowed (conservation of the total, not of each star); values are unbounded;
in the reductions the support shape is arbitrary up to `v`-extent `m ≤ 5`; densities periodic in
value and rounding-aware densities are included.

## 3. Exactness method

**Equations.** For a class with `n` unknowns, each periodic integer configuration `c` (1D period
`L`, or a 3D torus) gives one linear equation `Σ_windows f(Fc) − f(c) = 0` on the coefficient
vector, with `f` the integer feature vector (residue pattern × monomial value). Every such equation
is a necessary condition for conservation. Configurations are drawn by a seeded generator: `L`
uniform in `{1, …, 12}` (1D), torus sides uniform in `{1, …, 4}` (3D), values uniform in `[−B, B]`
with `B = max(6, 6μ)`. Features and `F` are computed in integer arithmetic. The largest absolute
value in any configuration used and in its image is recorded (`max|value|`), which fixes the
window of the transfer to Q (§1, value shift, at `a = 2^15`).

**Certificate.** `T` is spanned by the constant and by the coboundaries of the class one cell
shorter (for 3D: the constant and `b(y at P + e_j) − b(y at P)` for monomials `b` on
`P ⊆ {0, −e_j}`). Ranks are computed mod a prime `p < 2^20` by elimination in float64 arithmetic
that is exact for these magnitudes (every product sum is below `2^53`, asserted in the code).
A class is **certified** when `n − rank_p(E) = rank_p(T)`. Soundness: `rank_p ≤ rank_ℚ` for every
integer matrix, and `T ⊆ ker E` over `ℚ`, so `dim ker_ℚ E ≤ n − rank_p E = rank_p T ≤ rank_ℚ T ≤
dim ker_ℚ E`; hence `ker_ℚ E = T`, and every conserved quantity in the class is trivial on all
periodic configurations of the reduced rule (respectively of `ℤ³`), uniform ones included. The
inclusion `T ⊆ ker E` is also checked on every equation mod `p` and on a sample exactly in integers
(control C3).

**Stopping rule.** Equations are added in chunks of `max(256, ⌈n/4⌉)` configurations until the class
is certified, or three consecutive chunks add no rank, or 40 chunks have been used. A class that
stops uncertified is reported as `not certified`, with its excess `n − rank_p(E) − rank_p(T)`. If a
rounded class stops uncertified, the excess space is extracted mod `p`, lifted by rational
reconstruction and checked exactly on 200 fresh configurations; a survivor is reported as a
candidate with its exact form and scope. A second prime (1048571) is used before reporting an
uncertified rounded class.

**Compute bound.** Each invocation is kept under about 30 minutes of CPU (§A.40); classes are run in
separate invocations if needed. Classes above `n = 6561` are not run.

## 4. Controls (each must be green before a verdict that relies on it)

| Id | Control | Pass condition |
|---|---|---|
| K1 | reduction and background exactness (§A.21) | for ax, fd, bd and 20 seeded random periodic 1D initial states, the 3D RZ orbit on an `L × 1 × 1` torus (ax), on the plane-wave configuration of an `L × L × 1` torus (fd) and of an `L × L × L` torus (bd) equals the reduced 1D orbit for 30 steps, elementwise; the same orbits run in Q mod `2^16` at background `2^15` equal background plus the RZ orbit |
| K2 | rounding and reversibility | `G(s) = ⌊(s+1)/3⌋` agrees with an exact `Fraction` rounding to nearest for `s ∈ [−300, 300]`; the inverse map `(p, y) ↦ (G(S p) − y, p)` undoes `F` on 50 seeded random 1D and 3D states |
| P1 | positive control, reductions | on the bd rule, for every class in the grid that contains `Σ_k φ(u_{k+1} − p_k)` (with `φ(a) = a²` for `D ≥ 2`, `φ = [a ≡ 1 mod μ]` for `D = 0`), the class is **not** certified, and that quantity is in `ker E` exactly (integer check on every equation used) and is nontrivial (two exact witnesses with different `Φ/N`) |
| P2 | positive control, 3D | the integer linear rule `y' = S y − p` in P3(2): not certified; `y·y + p·p − y·S p` is in `ker E` exactly and nontrivial |
| C1 | countercontrol: the equations bite | on ax and fd, the bd invariant `Σ (u_{k+1} − p_k)²` and the plane-wave linear energy (coupling 1/3) each have an exact witness configuration with `ΔΦ ≠ 0`; in 3D, the linear-wave energy has an exact RZ witness with `ΔΦ ≠ 0` |
| C2 | detector | a planted coboundary added to the P1 invariant leaves it nontrivial, and a planted coboundary alone is classified trivial by the exact witness test |
| C3 | `T ⊆ ker E` | every `T` generator annihilates every equation mod `p`, and 200 sampled equations exactly in integers |

## 5. Decision rule (applied mechanically by the script; verdict text generated from its output)

- A rounded class (ax or fd reduction, P3 or P3r) that is **certified**, with K1, K2, C1, C3 green
  and the positive control of its type (P1 or P2) green, is an obstruction for that stated class:
  every conserved additive quantity in it is trivial on the corresponding periodic configurations,
  uniform ones included. At least one such class meets decision (ii).
- Decision (i) is met only by a candidate that survives the exact check of §3 in a 3D class (P3,
  P3r), or in a reduction together with a proof [W] that it extends to a conserved quantity of the
  3D rule. A reduction-only candidate without such a proof is recorded as a finding at its scope,
  not as (i).
- If neither holds, the outcome is a scoped recorded negative, listing each class with its excess.
- A failed control voids every verdict that relies on it; the script exits non-zero and writes the
  failure to its JSON output.

## 6. Invariant → checkpoint table (§A.41)

| Asserted property | Checkpoint |
|---|---|
| reduced rules equal the 3D rule on plane waves; Q equals background + RZ | K1 |
| `G` is the published rounding; `F` is invertible as implemented | K2 |
| the method can find a conserved quantity when one exists in the class | P1, P2 |
| the equations exclude non-conserved candidates; rounding is seen | C1 |
| triviality is decided correctly | C2, and the certificate's `T ⊆ ker E` check C3 |
| ranks are exact | float64 sums asserted `< 2^53`; certificate uses only `rank_p ≤ rank_ℚ` |
| no verdict over a failed control | exit status and `results.json` field `controls_green`; verdict lines printed only from `results.json` |
| determinism | fixed seeds; a rerun reproduces every rank and status in `results.json` |
| transfer window to Q | `max|value|` recorded per class |

## 7. Outputs (§A.44)

`checks/g3w1_checks.py` writes `checks/results.json` (schema: `controls` list of
`{id, pass, info}`, `classes` list of `{rule, family, m, D, mu, n, rank_E, rank_T, excess,
certified, equations, max_abs_value, prime}`, `controls_green`, `verdict`) and exits 0 iff every
control passes. `RESULT.md` quotes the verdict generated from that file, with scope limits and a
"Review must check" section. Amendments, if any, are separate commits under `amendments/` before the
runs they affect.
