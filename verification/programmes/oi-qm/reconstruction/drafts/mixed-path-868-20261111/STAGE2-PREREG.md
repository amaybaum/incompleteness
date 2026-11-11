# MIXED-PATH-1 Stage 2 — preregistration of one exact computation on the native rule

**WIP / UNVERIFIED writer draft r1. Not yet independently checked. Nothing in it has been run.** No code for it
exists. No number about any OI rule was seen while it was written: Stage 1 (`MIXED-PATH-UNIT1.md`) used paper
arguments and generic mathematics only.

- **Accountable home:** #868. **Authorization:** #868 comment 6794392080, author `amaybaum`,
  2026-11-11T11:17:53Z: owner answer, verbatim, "I give full authorization"; recorded scope: "**Stage 2:** a small
  exact computation on the native rule, run only under a written preregistration that fixes the following before
  any number is seen (§A.29, §A.21, §A.41): the decision rule; the controls and countercontrols; the size bounds.
  The preregistration gets an independent check before the run." "**Not covered:** any merge; any F/E designation
  or dispatch; any manuscript change; any new physical premise; any other unit's gated run; the Q-C2-1 design
  run." "A result in either direction is reported as scoped evidence for this construction only."
- **This is not a native V3 round.** It has no `F`, no `E`, no receipt and no `check-run` attestation. It is a
  research-thread computation whose output is scoped evidence for the executor (§A.40). For any enduring claim to
  rest on it, the code, this file and the result file would have to land on `main` with a recipe (§A.42 item 1);
  that is not authorized here.
- **Corpus pin:** `cac5d26441dd33e9348151487e4df7b547195481`. Citations as in Stage 1.

***

## 1. The question

For the native rule on a small finite lattice, with a visible/hidden partition taken from the corpus: does a
generator-region setting at wing A change the record at wing B **inside the window** (graph-connected, spacelike
for the emergent wave speed)

- **(a)** pointwise: is there a hidden configuration at which changing the remote setting changes the record
  (a dependent pair)?
- **(b)** in law: under the uniform hidden prior, does the remote setting change the wing's complete record law
  (marginal signalling)?
- **(c)** jointly: with every run producing a record and the hidden prior the same for every setting, is the
  two-wing table over the setting menu outside the Bell-local polytope (CHSH > 2)?

The decision rule (§6) is fixed here. Its verdict text is generated from the measurements. §9 records what Stage 1
predicts on paper; those predictions are **not** inputs to the rule.

***

## 2. Objects, each with its source

### 2.1 Lattices

- **Thin torus** `𝕋(L) = Z/L × Z/2 × Z/2`, `L ∈ {6, 8, 10, 12}`, sites `(x,y,z)`, parity `ε = (x+y+z) mod 2`.
  The neighbour sum is the corpus's `np.roll` sum over the `2d = 6` shifts
  (`papers/main_repro/lyapunov_v3.py`:18), so on the two short axes a neighbour is counted twice:
  `Σ(u)(x,y,z) = u(x+1,y,z) + u(x−1,y,z) + 2u(x,y+1,z) + 2u(x,y,z+1)`.
  *Why this lattice.* A `d = 3` torus with side 2 is the corpus's own instance for exhaustive work on these rules
  (SM:294, SM:296: "at `d=3`, `L=2`"). The long axis is a lattice axis, where the window is widest. For modes
  uniform across the short axes the observer-level dispersion is `cos ω = (2 + cos ak)/3` (SM:126), with
  long-wavelength speed `1/√3`, and the graph cone along `x` advances one site per tick; so along `x` the window of
  Stage 1 §2 is unchanged: `D ≤ k < √3·D`. *Stated limitation:* this is a finite-size object; it is not the
  `L → ∞` cubic lattice, and the emergent speed is a property of the observer-level lift, whose relation to any
  finite rule is unproved (SM:232).
- **Unwrapped cubic patch**, for affine rules only: the torus `(Z/Λ)³` with `Λ = 24`, used by exact linear algebra
  on record functionals. For every instance of §2.6 no dependency path wraps (`2(k+‖n‖₁) < Λ`), so the result
  equals that on `Z³` (cone lemma, Main:364); control C13 measures this.

Side lengths are even everywhere, so the lattices are bipartite and Lemma P of Stage 1 applies.

### 2.2 Rules (the family is enumerated; the corpus names no single realized map, SM:298)

State at a site: `(u, v) = (x(t), x(t−1))`, values in `Z_q` represented by `0..q−1`. One step is
`(u, v) ↦ (F(u) − v mod q, u)` (ledger (xiii), Main:726).

| Label | `F(u)` at a site | `q` | Lattice | Source |
|---|---|---|---|---|
| **R-round** | `⌊(Σ(u) + 1)/3⌋`, `Σ` the integer neighbour sum of representatives | `2` on `𝕋(6..12)`; `3` on `𝕋(6)` | thin torus | SM:294; `lyapunov_v3.py`:19 |
| **R-lin** | `Σ(u) mod q` | `3` on `𝕋(6)`; `2, 3, 5` on the patch | both | `wave_eqn.c`:6–10; SM:298 |
| **R-norm** | `α·Σ(u) mod q`, `α = 3⁻¹ mod q` | `5` (`α = 2`) on the patch | patch | SM:296 |

Not included, with reason: R-lin at `q = 2` on `𝕋(L)` (the doubled transverse terms vanish modulo 2, leaving a
one-dimensional rule with no window); R-norm at `q = 2` (identical to R-lin); the state-dependent ring of SM:112
(`d = 1`, no emergent speed derived); prepared long edges (open point O1, a different unit); `q ≥ 4` for R-round
(over the size bound of §7).

### 2.3 Partitions (enumerated; Stage 1 finding C-1)

| Label | Hidden coordinates | Source |
|---|---|---|
| **Π_cb3** | both slices at odd sites | SM:537, SM:557 (3D sublattice grading) |
| **Π_reg** | both slices at every site that is not a generator or record site | Main:72 ("a laboratory apparatus"); the region form used by Main:366–393 |
| **Π_cb4** | the space-time parity class not containing the setting | SM:557 (`ε_4D`) |
| **Π_hor** | none inside the lattice (the horizon reading: SM:539, Main:28) | Main, SM |

The companion partition (current field visible, retarded register hidden; SM:252) is not listed separately: for a
current-slice setting its hidden coordinates in the setting's class are those of Π_cb3, and a retarded-slice
setting would be hidden under it.

**Law of the records** (Main:137, Main:131): the visible content at `t_s` is fixed (a visible root), the hidden
coordinates are drawn from the uniform measure, the same for every setting, and the rule is applied. Under Π_cb4
and Π_hor the setting's class has no hidden coordinate and every record law is a point mass.

### 2.4 Wings, generators, records

All sites lie on the line `y = z = 0`; positions are `x`-coordinates.

| Wing type | `g_A` | `r_A` | `r_B` | `g_B` | Allowed `D` |
|---|---|---|---|---|---|
| **S** (record at the generator site) | 0 | 0 | `D` | `D` | `D ≥ 2` |
| **I** (records inside) | 0 | 2 | `D` | `D+2` | `D ≥ 4` |
| **O** (records outside) | 2 | 0 | `D+2` | `D` | `D ≥ 4` |

In each type `d(g_B, r_A) = d(g_A, r_B) = D`. The corpus fixes none of these geometries, so all three are run.
A single-site receiver read passively at successive ticks is the corpus's declared receiver type
(`correlation-recombination-20261107/DESIGN.md` §1: "`R_t = (u_t(o), u_{t−1}(o))`", "Reads in this reference law are
passive projections of the evolving state"); a one-site intervention region is the smallest instance of Main's
theorem hypothesis (ii).

- **Setting slice** `s ∈ {u, v}`: the setting is the value of that slice at the generator site at `t_s`. Both are
  run. The other slice at that site lies in the other parity class and is set to `0` (it cannot matter: control C2).
- **Setting menu:** all `q` values at each wing. **Sub-menus for (c):** every pair `{a,a'} × {b,b'}` of distinct
  values: `C(q,2)²` (one for `q = 2`, nine for `q = 3`).
- **Record window `k`:** ticks `t_s+1 … t_s+k`. **Complete history of a wing:** its own setting together with
  `u_t(r)` for every tick `t ≤ k` at which `(r, t_s+t)` lies in the setting's parity class. Records in the other
  class are independent of both settings and of the setting class's hidden coordinates (Lemma P; measured by C2),
  so the two-class table is the product of this table with a setting-independent one, and its verdict for (a),
  (b), (c) is this table's.
- **Outcome maps for (c):** none is chosen. Locality is decided for the complete-history table, which covers every
  outcome map; in addition the exact maximum of `|CHSH|` over **all** pairs of `±1`-valued maps of the complete
  histories (maps may depend on the own setting) and all four placements of the minus sign is reported.

### 2.5 Visible content

The visible, non-generator coordinates of the setting's class are fixed, and the result is reported for each
member of:

- **F_const** (every instance): all such coordinates equal to `c`, for each `c ∈ Z_q`;
- **F_all** (where the count permits, §7): every assignment. This is run for `𝕋(6)`, `q = 2`, all partitions, and
  for Π_reg wherever the visible non-generator class coordinates number at most 4.

Coordinates of the other class are set to `0`.

### 2.6 Instances (frozen list)

**Window rule (integers).** `(D, k)` is a window instance on `𝕋(L)` iff `D` is even, `D ≥ 2`, `D ≤ k`,
`k² < 3D²`, and `L ≥ D + k + 1` (so that the path the other way round the long axis, of length `L − D`, is outside
the graph cone during the window). On the patch, `(n, k)` is a window instance iff `‖n‖₁ ≤ k` and `k² < 3 n·n`.

Odd `D` is not covered: with wings on sites of opposite parity, same-slice settings lie in different parity
classes, each class then carries one setting, and a table with one input is Bell-local whenever it is
no-signalling.

| Lattice | `(D, k)` window instances | Wing types |
|---|---|---|
| `𝕋(6)` | (2,2), (2,3) | S |
| `𝕋(8)` | (2,2), (2,3) | S |
| `𝕋(10)` | (2,2), (2,3), (4,4), (4,5) | S; I and O for `D = 4` |
| `𝕋(12)` | (2,2), (2,3), (4,4), (4,5), (4,6) | S; I and O for `D = 4` |

| Patch `n` (all `n_x ≥ n_y ≥ n_z ≥ 0`, `‖n‖₁` even, `≤ 4`) | Window ticks `k` |
|---|---|
| (2,0,0) | 2, 3 |
| (1,1,0) | 2 |
| (4,0,0) | 4, 5, 6 |
| (3,1,0) | 4, 5 |
| (2,2,0) | 4 |
| (2,1,1) | 4 |

Patch instances use wing type S along `n`, partitions Π_cb3 and Π_reg, both setting slices.

**Run matrix.**
- *Primary (the open case):* R-round, `q = 2`, every thin-torus row, partitions Π_cb3, Π_cb4, Π_hor; Π_reg on
  `𝕋(6)` only (size bound); both slices; every wing type listed; F_const, and F_all on `𝕋(6)`.
- *Primary, second alphabet:* R-round, `q = 3`, `𝕋(6)`, Π_cb3, both slices, F_const.
- *Affine, brute force:* R-lin, `q = 3`, `𝕋(6)`, Π_cb3 and Π_cb4, both slices, F_const.
- *Affine, linear algebra:* R-lin (`q = 2, 3, 5`) and R-norm (`q = 5`) on every patch row.

Every instance in the matrix is reported, whatever its token. No instance is added, dropped or reordered after the
independent check.

***

## 3. Measurements (exact)

For an instance, a window `k`, a visible content `c`, and settings `(a,b)`, let `H` be the set of hidden
configurations of the setting's class and `h_A(η; c,a,b)`, `h_B(η; c,a,b)` the complete histories for `η ∈ H`.

- `N[c][a][b]`: the table of integer counts of `(h_A, h_B)` over all `η ∈ H`; total `|H|` for every `(c,a,b)`.
- `dep_B[c]` = number of `(η, b, {a,a'})` with `h_B(η;c,a,b) ≠ h_B(η;c,a',b)`; `dep_A[c]` symmetrically. This
  compares the same `η` under two settings.
- `first_dep_tick`: the smallest tick at which a record entry differs in some such comparison, per wing.
- `sig_B[c]` = number of `(b, {a,a'})` for which the marginal count vectors of `h_B` under `(a,b)` and `(a',b)`
  differ; `sig_A[c]` symmetrically. Integer comparison of count vectors.
- For each `c` with `sig_A[c] = sig_B[c] = 0`, and each 2×2 sub-menu: `loc[c][sub] ∈ {LOCAL, NONLOCAL}`, decided by
  exact rational linear programming over the deterministic local strategies and returned **with a certificate**:
  for LOCAL, non-negative rational weights on deterministic strategies reproducing the table exactly; for
  NONLOCAL, a rational Bell functional `β` with `β·P > max_v β·v` over all deterministic strategies `v`. A
  separate routine verifies the certificate in exact arithmetic; only a verified certificate counts.
- `chsh_max[c][sub]`: exact maximum of `|CHSH|` over all pairs of binary maps of the histories (enumerate one
  wing's maps; the other wing's optimum is the sum of absolute values of the resulting linear coefficients), as a
  `Fraction`. Computed when each wing's history alphabet has at most 9 letters; otherwise recorded as `null`.

**Affine instances by linear algebra (patch).** Over the field `F_q`, the record functionals are rows of
`S_t(αA)` (Stage 1 §2.2). `dep` is "the remote setting's column in the wing's history is non-zero"; `sig` is "that
column is not in the span of the hidden columns" (exact Gaussian elimination over `F_q`); for locality the solver
returns the vectors `δ_a`, `δ'_b` of Theorem L and verifies `M_B δ_a = W_B(c_a − c_0)`, `M_A δ'_b = V'_A(c_b − c_0)`
exactly. Tokens from this path carry the suffix `-BY-THEOREM-L`: their locality rests on Stage 1's paper proof
plus an exact certificate of its hypotheses, not on enumeration.

**Arithmetic.** Integers and `fractions.Fraction` only on every path that feeds a control or a verdict. Fixed-width
integer arrays may be used for state enumeration and counting; counts are bounded by `|H| ≤ 4.4·10⁷ < 2⁶³`. No
floating-point number enters a comparison.

***

## 4. Controls and countercontrols

Every control must be green before any verdict is written. Each has a stated non-vacuity condition; a vacuous
control is red.

| # | Control | Green iff | Non-vacuity |
|---|---|---|---|
| **C1** | cone lemma: for every instance, records at ticks `t < d(g, r)` | zero pointwise differences under a change of the remote setting, over the whole enumeration | at least one such (tick, comparison) exists per instance with `D ≥ 2` |
| **C1′** | detector sensitivity (countercontrol): R-lin `q = 3`, `𝕋(6)`, Π_cb3, type S, slice `u`, tick `D = 2` | `u_2(r_B)` differs under a change of `a` for **every** hidden configuration and every `c` (the path count is 1, a unit) | count equals `|H|·q·C(q,2)·q` exactly |
| **C2** | parity decoupling (Lemma P; exactness and symmetry control of §A.21): on `𝕋(6)`, every rule and `q`, using a stepper for the full two-slice field (both classes together) | from each base state in the set `B` (the `q²` slice-constant states and 256 states from the fixed integer generator `s ← (1103515245·s + 12345) mod 2³¹`, `s₀ = 868`), changing any single coordinate of one class to any other value changes no value of the other class at any site through tick 6. **C2b:** the class-restricted stepper used for the enumeration equals the full-field stepper restricted to that class on every state of `B` and on every state reached in C3 | at least `260·24·(q−1)` comparisons per class, count reported. This control is not exhaustive over states; it tests an identity that Stage 1 proves |
| **C3** | bijection and measure: on `𝕋(6)`, each rule | step followed by the stated inverse step is the identity on every state of one class (`q = 2`: all `2²⁴`); the image of the enumeration is a permutation of it | exhaustive |
| **C4** | two code paths on the affine rule: R-lin `q = 3`, `𝕋(6)` | brute-force `dep`, `sig`, `loc` agree with the linear-algebra path on every instance, window and `c` | at least one instance with `dep > 0` and at least one with `sig = 0` occur in the comparison, else the control is vacuous and red |
| **C5** | slice shift (Lemma S): slice `u`, partitions Π_cb3 and Π_reg, every rule, windows `k ≤ D+1` | `sig_A = sig_B = 0` and every `loc = LOCAL` | applies to at least the instances (2,2), (2,3), (4,4), (4,5) |
| **C6** | native signalling is detected: R-lin `q = 3`, `𝕋(6)`, Π_cb4, slice `u`, type S, window (2,2) | `sig_B > 0` (no hidden coordinate in the class; C1′ gives the dependence) | — |
| **C7** | planted PR table (`h_A = r`, `h_B = r ⊕ ab`, `r` a fair bit) through the same pipeline | `sig = 0`, `loc = NONLOCAL` with verified certificate, `chsh_max = 4` exactly | — |
| **C8** | planted local tables: 200 seeded exact mixtures of deterministic strategies, including the uniform mixture of the eight `S = +2` strategies | every `loc = LOCAL` with verified certificate and `chsh_max ≤ 2`; the boundary case gives exactly `2` and is classified LOCAL | at least one table with `chsh_max = 2` exactly |
| **C9** | planted non-coset `Z₄` table of Stage 1 (probe X1) | `sig = 0`, `loc = NONLOCAL`, `chsh_max = 3` exactly | — |
| **C10** | symmetry (§A.21): the reflection `x ↦ g_A + g_B − x`, which exchanges the wings, and translation by 2 along `x`, on `𝕋(6)` and `𝕋(8)` | the count tables are equal after relabelling, exactly | applied to every instance on those lattices |
| **C11** | certificate verifier (countercontrol): one weight of a valid LOCAL certificate and one coefficient of a valid NONLOCAL certificate are perturbed | the verifier rejects both | — |
| **C12** | window arithmetic: the instance lists are regenerated from the integer inequalities of §2.6 | equal to the frozen lists in this file; body-diagonal vectors `(D,D,D)`, `D ≤ 6`, have empty windows | — |
| **C13** | no-wrap on the patch: affine results recomputed at `Λ = 28` | identical to `Λ = 24` | — |
| **C14** | planted signalling table (`h_B = a`) | `sig_B > 0` | — |

C5 and C4 are proof-backed. If either is red the run is VOID and the discrepancy is itself a finding to
investigate: either the code or the Stage 1 lemma is wrong. A red control is never repaired by changing the
control.

***

## 5. Invariants and their checkpoints (§A.41)

| Invariant asserted of the execution | Checkpoint that measures it |
|---|---|
| exact arithmetic on every control and verdict path | static check: no `float`, `math.` float function or true division on those paths; every reported probability is a `Fraction` serialized as `"p/q"`; the result schema rejects JSON numbers with a fractional part outside `timing` |
| every run produces a record (no post-selection) | for every `(c,a,b)`: `Σ N[c][a][b] = |H|`, asserted |
| the hidden prior is the same for every setting (measurement independence by construction) | one enumeration object of hidden configurations per instance; its digest is recorded once and re-checked before each `(a,b)` |
| hidden coordinates are exactly those of the stated partition | the coordinate lists are emitted in the result file and compared with a second, independent generator of the partition |
| the instance list is the frozen one | C12; the result file lists every frozen instance exactly once, with a token |
| cross-wing dependence is evaluated only inside the window | each record entry carries its tick; the window test `D ≤ t`, `t² < 3D²` is asserted for the last tick of each window; C1 covers `t < D` |
| the direct path is the only one inside the cone | `L − D > k` asserted per instance |
| no verdict over a red control | `verdicts` is written only if `controls_all_green` is true; otherwise it is `null` and the exit status is 2 |
| deterministic replay (§A.26) | the result file's `tables_digest` (SHA-256 over the canonical serialization of all count tables) is reproduced by a second full execution before the result is reported; a mismatch is exit status 4 |
| single process, bounded resources | wall-clock, peak memory and process count recorded in `timing`; caps enforced in the program (§7) |
| the code that ran is the code that was checked | SHA-256 of the program recorded on #868 before the registered run and written into the result file |
| no OI-rule number seen before the registered run | during development the program is executed only with `--selftest`, which runs C7, C8, C9, C11, C14 and nothing that steps a rule; the first execution without that flag is the registered run |

***

## 6. Decision rule

**Per (instance, window `k`)**, over the members `c` of the visible-content family run for that instance:

1. **`VOID`** if any control is red, an invariant checkpoint fails, or the instance did not complete.
2. **`NO-DEPENDENCE`** if `dep_A[c] = dep_B[c] = 0` for every `c`.
3. **`SIGNALLING`** if `sig_A[c] > 0` or `sig_B[c] > 0` for at least one `c`. The result records the number of such
   `c`, and separately the number of `c` that are no-signalling and NONLOCAL (flag
   `nonlocal_among_nonsignalling`); a non-zero flag is reported prominently and is not a Bell verdict.
4. **`BELL-VIOLATION-NO-SIGNALLING`** if `sig_A[c] = sig_B[c] = 0` for every `c`, and `loc[c][sub] = NONLOCAL` with
   a verified certificate for at least one `(c, sub)`. The result records `chsh_max`; if every `chsh_max ≤ 2` the
   token carries the suffix `-NON-CHSH`.
5. **`DEPENDENCE-MASKED-LOCAL`** if some `dep > 0`, every `sig = 0`, and every `loc[c][sub] = LOCAL` with a verified
   certificate. The token asserts locality of every 2×2 sub-menu table over complete histories, not of the full
   `q × q` menu.
6. **`LOCALITY-UNDECIDED`** if some `dep > 0`, every `sig = 0`, no NONLOCAL certificate was found, and at least one
   linear program did not finish within its bound.

For Π_cb4 and Π_hor, `|H| = 1`; rules 2 and 3 are the only ones that can apply, and the token `SIGNALLING` then
means deterministic visible-to-visible dependence.

**Headline for the unit**, generated from the instance tokens of the primary run matrix (R-round):

- `VOID` if any control is red;
- `INCOMPLETE` if any primary instance is `VOID` or `LOCALITY-UNDECIDED`;
- else `BELL-VIOLATION-NO-SIGNALLING-FOUND` if any primary instance under Π_cb3 or Π_reg has that token;
- else `SIGNALLING-FOUND` if any primary instance under Π_cb3 or Π_reg is `SIGNALLING`;
- else `DEPENDENCE-MASKED-LOCAL-ONLY` if any is `DEPENDENCE-MASKED-LOCAL`;
- else `NO-DEPENDENCE`.

The headline is accompanied by the full token table; Π_cb4 and Π_hor tokens are reported beside it and do not
enter it, because they have no hidden prior. No token is defined by a numerical threshold other than the exact
comparisons above, and none refers to an expected value.

***

## 7. Size and resource bounds

| Quantity | Bound |
|---|---|
| hidden configurations per (instance, `c`, setting pair) | `q^{2L}` under Π_cb3: at most `2²⁴ = 16,777,216` (`q = 2`, `L = 12`); `3¹² = 531,441` (`q = 3`, `L = 6`). Under Π_reg on `𝕋(6)`: at most `2²²` |
| visible contents per instance | F_const: `q`; F_all on `𝕋(6)`, `q = 2`: at most `2¹⁰` under Π_cb3, at most `2²²` class states under Π_cb4 and Π_hor |
| total trajectories, all instances | at most `4·10⁹` state evaluations of at most 6 ticks each |
| history alphabet per wing | at most 8 record letters for `q = 2` (three record ticks) and 9 for `q = 3` (two record ticks), times `q` for the own setting |
| linear program | at most `81 × 81` deterministic strategies and 324 equality rows; at most 10 minutes each |
| patch linear algebra | `Λ = 24` (13,824 sites), at most 6 record rows per wing |
| process | one process, one thread; no network; no GPU |
| memory | at most 6 GB resident; enumeration in blocks of at most `2²⁰` configurations |
| wall clock | at most 3 hours for the registered run, and the same for the replay |

**Order.** Self-test controls; then controls on `𝕋(6)`; then instances by increasing `L`, results written
atomically after each lattice.

**On reaching a bound.** The program stops, marks every unfinished instance `VOID` with reason `timeout` or
`memory`, writes the result file with `verdicts` for completed instances only if all controls are green, sets the
headline to `INCOMPLETE`, and exits with status 3. Nothing is rerun with smaller sizes, a different order or a
subset without an amendment to this file and a new independent check. If the run would exceed these bounds on the
executor's machine, the executor stops and reports the partial state (§A.40) and does not dispatch it elsewhere:
a workflow dispatch is outside the authorization.

***

## 8. Structured outputs and exit statuses (§A.44)

**Exit status.** `0` complete, all controls green, verdicts written. `2` a control is red: `verdicts` is `null`.
`3` a resource bound was reached: headline `INCOMPLETE`. `4` an invariant checkpoint or the replay digest failed.
`1` any other error. A consumer reads the exit status and `results.json`; printed output is diagnostic only.

**`results.json`** (one object; all integers are JSON integers, all probabilities strings `"p/q"`):

```json
{
  "schema": "mixed-path-1/stage2/v1",
  "prereg_sha256": "<sha256 of this file as checked>",
  "program_sha256": "<sha256>",
  "corpus_pin": "cac5d26441dd33e9348151487e4df7b547195481",
  "controls": [
    {"id": "C1", "green": true, "nonvacuous": true, "counts": {"comparisons": 0, "violations": 0}, "detail": "…"}
  ],
  "controls_all_green": true,
  "invariants": [{"name": "every-run", "ok": true, "measured": {"…": 0}}],
  "instances": [
    {
      "id": "R-round/q2/T12/cb3/S/D4/v",
      "rule": "R-round", "q": 2, "lattice": "T12", "partition": "cb3", "wing": "S", "D": 4, "slice": "v",
      "sites": {"gA": [0,0,0], "rA": [0,0,0], "gB": [4,0,0], "rB": [4,0,0]},
      "hidden_coordinates": ["u@(1,0,0)", "…"], "hidden_count": 16777216,
      "family": "F_const",
      "windows": [
        {
          "k": 5, "record_ticks": [1,3,5], "in_window": true,
          "per_content": [
            {"c": "0", "dep_A": 0, "dep_B": 0, "first_dep_tick": {"A": null, "B": null},
             "sig_A": 0, "sig_B": 0,
             "submenus": [{"a": [0,1], "b": [0,1], "loc": "LOCAL", "certificate_verified": true,
                           "chsh_max": "2/1"}],
             "table_digest": "<sha256>"}
          ],
          "nonlocal_among_nonsignalling": 0,
          "token": "…"
        }
      ]
    }
  ],
  "verdicts": {"headline": "…", "tokens": {"<instance id>/k<k>": "…"}},
  "tables_digest": "<sha256>",
  "replay": {"performed": true, "tables_digest_equal": true},
  "timing": {"wall_seconds": 0, "peak_rss_mb": 0, "processes": 1}
}
```

Count tables are written to `tables/<instance id>.json` beside it; certificates to `certificates/`. `token` and
`headline` take only the values defined in §6.

***

## 9. Paper predictions on record (not inputs to the rule)

From Stage 1, all unreviewed:

1. Lemma P: C2 is green for every rule.
2. Lemma S: C5 is green; for slice `u` the first law-level dependence can occur only at tick `D+2`, so the only
   slice-`u` instance not already fixed by the lemma is `(4,6)` on `𝕋(12)`.
3. Theorem L: no R-lin or R-norm instance receives `BELL-VIOLATION-NO-SIGNALLING`; C4 is green.
4. For slice `v` no dependence occurs before tick `D+1`, so windows `(2,2)` and `(4,4)` give `NO-DEPENDENCE`.
5. No prediction is made for R-round at slice `v`, windows `(2,3)`, `(4,5)`, `(4,6)`, or at slice `u`, window
   `(4,6)`. These are the instances the unit exists for.

A result contradicting 1–4 is reported as such. It does not void the run unless it arrives through a red control
(C2, C4, C5), in which case §4 applies.

***

## 10. What the result does and does not license

- **`NO-DEPENDENCE` or `DEPENDENCE-MASKED-LOCAL-ONLY`.** Scoped evidence that, for these rules, alphabets,
  lattices, partitions, wing geometries, slices and windows, the window carries no Bell-relevant dependence under
  the uniform hidden prior. It is **not** a no-go: it says nothing about larger separations, other alphabets, the
  full cubic lattice, multi-site records, structured or conditioned priors, state-dependent graphs, or other
  rules. It does not extend Theorem N or Main's Corollary.
- **`SIGNALLING-FOUND`.** Scoped evidence that at these sizes the uniform hidden prior does not mask the
  dependence. With `c` taken as the wave speed this would be controllable influence outside the emergent light
  cone at lattice scale on a thin torus. It does not show that the framework signals: `c` is not identified
  (Main:416), the emergent speed of the finite rule is not derived (SM:232), and a separation of two or four sites
  is not the long-wavelength regime.
- **`BELL-VIOLATION-NO-SIGNALLING-FOUND`.** A construction-scoped finding: one finite table, on one finite lattice,
  outside the local polytope with exact no-signalling. Before it is cited anywhere it requires (i) an independent
  re-derivation by a second implementation or by hand from the published count table and certificate, (ii) a
  check that it survives the next lattice size and the F_all family, (iii) the complete-history and reuse test of
  prepared-pair-source §4 beyond the window, and (iv) the confrontation of Stage 1 §5. It would not establish a
  native Bell mechanism, the Tsirelson bound, or agreement with quantum mechanics, and it would not select `c`.
- **Any outcome.** No manuscript statement, status or classification changes. Correctness bands are unchanged: this
  is internal work on the consistency axis (§A.23). The result is reported on #868 with its token table, including
  every `VOID`.

***

## 11. Requests to the independent checker

Before the run, the checker is asked to confirm or correct, in particular:

1. that the thin torus with the `np.roll` neighbour convention is an acceptable "small finite lattice" for the
   native rule, and that reading the window along its long axis is sound;
2. that fixing visible content (F_const everywhere, F_all on `𝕋(6)`) with a uniform hidden prior is the corpus's
   record law (Main:137), and that F_const is not a choice that favours any token;
3. the partition list, the exclusion of odd `D`, and the three wing types;
4. Lemma P, Lemma S and Theorem L, since C2, C5 and C4 lean on them;
5. the decision rule's precedence, in particular that a single signalling visible content makes the instance
   `SIGNALLING`;
6. that the bounds of §7 are small enough to run locally in one process, and the consequence if they are not.

Any change made in response is an amendment to this file, made before the program's hash is recorded.

***

## 12. References to content not on `main` (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md`, `papers/SM.md` @ cac5d264; `wave_eqn.c` (`c56e64ce…`); `lyapunov_v3.py` (`a25372b2…`); `correlation-recombination-20261107/DESIGN.md` (`b3907140…`); `oi-qm-ext-1/prepared-pair-source.md` (`9123157c…`) | object definitions, record law, receiver type | support on `main` |
| `MIXED-PATH-UNIT1.md` r1 (this directory, unreviewed) | Lemma P, Lemma S, Theorem L; window arithmetic; probe X1 table for C9 | **support off `main`: gap.** Controls C2, C4, C5 are valid as controls only if those arguments are; the checker is asked to verify them (§11 item 4) |
| `probes/generic_mixedpath_checks.py` (sha256 `3bb689f6…2fd4`) | C9's table and expected value | off `main`; gap if this record lands |
| Bell-scope unit 1 r2 (blob `5814e479…` at `e1534b08…`) | the question's origin (O2) | off `main`; provenance |
| #868 c.6794392080 | authority | planning record; provenance |

## 13. Not done

No program has been written. Nothing has been executed. The linear-programming method is specified by its
certificate, not by an algorithm. The checker's review is pending. No F/E designation, dispatch, merge or
manuscript change is requested or implied.
