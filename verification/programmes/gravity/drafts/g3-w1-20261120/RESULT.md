# G3-W1: conserved additive quantities of the d = 3 rounded rule

**Standing.** Author record of a paper-only research unit (AGENTS.md §A.29, §A.31 depth-first
form). WIP / UNVERIFIED: no independent non-author review yet. It adopts no premise and edits no
manuscript, Lean module or registry. The preregistration `PREREG.md` (commit `65e18750`) and
amendment `amendments/A01-3d-trivial-space.md` (commit `7bee0b1b`, before run D2) were pushed before
the runs they govern.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7033018172](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033018172),
  2026-11-20T07:12:08Z, row G3-W1, `execution` (quoted in PREREG). Scope:
  [#1169 c.7032429839](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7032429839).
- **Goal link (§A.47), from PREREG.** Serves G3 (#873): decides, for the stated classes, whether
  the published rounded rule carries a conserved additive real quantity, or which class is
  excluded.
- **Accountable Issues.** #873, #1169.
- **Snapshot `D`.** `main` at `b9168ef0408b5f55b935a4df17cb0841877e221a`. `SM:n`, `Sub:n` are line
  `n` of `papers/SM.md`, `papers/Substratum.md` there.
- **Inputs (§A.46 item 7).** UNIV-2 A2 (PR #1444, branch head `aecc64ef`; merged on `main` at
  `27187dc3`) is used only to choose classes that do not repeat it; no result below depends on it. UNIV-1 supplies the rule's
  definition; its background lemma is re-checked here (K1). G3-HOM is method provenance.

| Label | Meaning |
|---|---|
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact computation in `checks/g3w1_checks.py`: integer features, ranks mod a prime with the soundness argument of Lemma 5 |
| [XC] | cross-check in `checks/xcheck_rational.py` (not preregistered): independent code, ranks over ℚ |

***

## 0. Verdict (generated from `checks/results.json`)

`controls_green: true`. The script's verdict line:

> Decision (ii) met for 47 of 47 rounded classes (certified: every conserved additive quantity in
> the class is trivial on its periodic configurations): ax:Q(2,2,1), fd:Q(2,2,1), … ,
> ax:Q(5,0,2), fd:Q(5,0,2), 3D-RZ:P3(2), 3D-RZ:P3(3), 3D-RZ:P3r(2). No rounded class is
> uncertified. Decision (i) not met: no candidate conserved quantity in any rounded class.

(The ellipsis stands for the 44 plane-wave classes listed in full in `results.json` and in §3.)

In words, with the scope of §4:

1. **Direct 3D (amendment A01, run D2).** Every additive quantity of the rounded rule on `ℤ³` whose
   density is a polynomial of degree ≤ 3 in the 14 star values (site and six neighbours, both
   slices), or a polynomial of degree ≤ 2 in them with coefficients depending on the residues mod 3
   of `(S y)_n` and `(S p)_n`, and which is conserved on all periodic configurations, is trivial:
   `Φ(c) = λ·N(c)` on every periodic configuration. The linear-wave energy is in these classes, so
   no star-local polynomial correction of degree ≤ 3, and no rounding-aware quadratic correction,
   makes it conserved. [W + EC]
2. **Plane waves (preregistered runs A–C).** Every translation-invariant additive quantity of the
   3D rule conserved on all periodic configurations whose density restricts to plane waves along
   `(1,0,0)` or `(1,1,0)` inside one of 22 classes (polynomial up to degree 4; rounding-aware
   degree ≤ 4 with residues mod 3; arbitrary functions of the values mod μ, with μ ∈ {2,3,4,5,6,8,9}
   at extent 2, μ ∈ {2,3,4} at extent 3, μ ∈ {2,3} at extent 4 and μ = 2 at extent 5; density
   extent ≤ 5 cells along the wave vector as listed in §3, arbitrary transverse shape, values unbounded) is trivial
   on those plane waves. Uniform states are the period-1 plane waves, so each such quantity is
   constant on the homogeneous sector. [W + EC]
3. **The preregistered 3D run D** left the 3D classes uncertified (excess 24, 96, 24) because its
   trivial space omitted translation coboundaries (A01). Its excess examination took the first 50
   basis vectors of the mod-`p` kernel of `E` (kernel dimension 67, 199, 67, so these include
   directions of `T`); each lifted exactly, and a sampled witness search found no nontriviality
   witness for any of them. That search is not a proof. D's outcome stands as recorded; D2
   supersedes it for the 3D decision.
4. **No conserved real energy was found.** Decision (i) is not met.

***

## 1. Object and lemmas

Q is `x_{t+1}(n) = ⌊(Σ_{m∼n} x_t(m) + 1)/3⌋ − x_{t−1}(n) mod 2^16` on `ℤ³` (UNIV-1 §1; SM §4.2,
SM:294). RZ is the same rule over `ℤ`, `F(p, y) = (y, G(S y) − p)`, `G(s) = ⌊(s+1)/3⌋`, which is
nearest-integer rounding of `s/3` (K2).

**Lemma 1 (value shift) [W, EC K1].** `G(s + 6a) = G(s) + 2a`, so `F(p + a, y + a) = F(p, y) + a`.
On configurations with values in `[a − B, a + B]` whose image stays there, with
`B ≤ a ≤ 2^16 − 1 − B`, Q equals `a +` RZ, since no representative wraps. K1 checks this at
`a = 2^15` on 60 orbits of 30 steps.

**Lemma 2 (plane-wave reduction) [W, EC K1].** For primitive `v ∈ ℤ³` and `y(n) = u(v·n)`,
`(S y)(n) = Σ_j [u(v·n + v_j) + u(v·n − v_j)]`, so plane waves are invariant and evolve by
`u'_k = G(s_k) − p_k` with `s_k = u_{k±1} + 4u_k` (ax), `2(u_{k−1} + u_k + u_{k+1})` (fd),
`3(u_{k−1} + u_{k+1})` (bd). On bd, `s_k ≡ 0 mod 3`, so `G(s_k) = s_k/3` and the published rule is
exactly the linear rule `u' = u_{k−1} + u_{k+1} − p` on body-diagonal plane waves.

**Lemma 3 (restriction) [W].** Let `Φ(c) = Σ_{n ∈ Ω} h(c|_{n+O})` on periodic configurations
(`Ω` a fundamental domain of the period lattice; `O` the density's finite support in `ℤ³ × {t−1, t}`),
and let the values `v·o`, `o ∈ O`, lie in `[a, a + m − 1]`. On the plane wave of 1D period `L`,
the period lattice is `Λ_L = {n : v·n ≡ 0 mod L}` and `n ↦ v·n mod L` is a bijection
`ℤ³/Λ_L → ℤ/L` (`v` primitive), so `Φ(c) = Σ_{k mod L} h̃(u_{k+a}, …, u_{k+a+m−1})` with
`h̃` the value of `h` on the plane-wave pattern. With Lemma 2, `Φ` conserved on all periodic
configurations implies `Φ̃` conserved by the reduced rule on all `L`-periodic configurations, with
`N = L`. If `h` is a polynomial of degree ≤ D in its values with coefficients depending on their
residues mod μ, then `h̃ ∈ Q(m, D, μ)`.

**Lemma 4 (finite-support conservation implies periodic conservation) [W].** Let `h(0) = 0`
(subtracting a constant), so `Φ` is defined on finite-support configurations, and let it be
conserved there. RZ fixes the zero state. For periodic `c` with `NZ³` in its period lattice, let
`c_R` equal `c` on `[0, RN)³` and `0` elsewhere. Sites farther than `r + 1` (`r` the radius of `O`)
from the box boundary contribute to `Φ(F c_R) − Φ(c_R)` exactly as in `c`; there are
`R³N³ − O(R²)` of them. The remaining `O(R²)` terms take values in a finite set, since only
finitely many local patterns of `c` and `0` occur. So `0 = R³N³·ΔΦ_site(c) + O(R²)` for all `R`,
and `ΔΦ(c) = 0` on every period. The classes below may therefore be read with either definition
of conservation.

**Lemma 5 (certificate) [W].** `E` is the integer matrix of equations `Σ_windows f(Fc) − f(c)`,
one per configuration used. `T` (constants and coboundaries `b∘τ − b` inside the class) satisfies
`T ⊆ ker_ℚ E` for every rule: constants give `λN`, which `F` preserves, and a coboundary sums to
zero over every period. For an integer matrix, `rank_p ≤ rank_ℚ`. Hence if
`n − rank_p E = rank_p T`, then
`dim ker_ℚ E ≤ n − rank_p E = rank_p T ≤ rank_ℚ T ≤ dim ker_ℚ E`, so `ker_ℚ E = T`. Every conserved
quantity of the class satisfies every equation used, so it lies in `T` and is trivial on all
periodic configurations. Sampling equations only weakens `E`, so a certificate from a sample is a
proof. Float64 arithmetic is exact mod `p < 2^20`: in `mod_matmul` the block length is chosen so that
every partial sum stays below `2^53`, which is asserted; the other float64 operations (row scaling
and rank-one updates) involve single products of residues, bounded by `p² < 2^40` by inspection.

**Lemma 6 (transfer to Q) [W].** A certified class with recorded `max|value| = B` (§3) used only
configurations with values in `[−B, B]` before and after one step. Let `h_Q` be a density of Q,
conserved on Q's periodic configurations, that agrees on values in `[2^15 − B, 2^15 + B]`
(after subtracting `2^15`) with a member `h` of the class. By Lemma 1, `h` satisfies every equation
used, so `h ∈ T`, and `h_Q` is trivial on the configurations in that value window (plane-wave ones
for the 1D classes). The same holds at every background `a` with `B ≤ a ≤ 2^16 − 1 − B`.

***

## 2. Classes, method and controls

As preregistered (PREREG §2–§4), with amendment A01 for D2. Ranks are mod `p = 1048573`; a rounded
class left uncertified would be retried mod `1048571` and its excess examined (rational
reconstruction, 200 fresh exact equations, a nontriviality witness search).

**Deviations from PREREG.** (1) Amendment A01 (3D trivial space), committed after run D and before
run D2; D's outcome is reported unchanged. D2 uses the same seeds and equation sequence as D, and stops at a prefix of it once certified. (2) PREREG §7 names one output file; the script writes
one file per part (`results-A.json` … `results-D2.json`) and `--render` merges them into
`results.json`, which carries the verdict and the controls P1, P2, C1–C3 and coverage. (3) After the
preregistration `65e18750` and while the script was being tested, two single-class diagnostic runs
on the rounded rule (`ax:Q(2,2,1)`, `fd:Q(3,2,1)`, with an earlier seed scheme) preceded the
recorded runs; both certified, and the recorded runs replace them. `checks/g3w1_checks.py` was
first committed in `14c5ea2c`, after all runs, so the A01 code change (the `D2` part and
`Class3D.tgen_full`) cannot be dated from git; parts A–C and D ran on the earlier code, and the
replays of A and D2 on the committed code match them. (4) `xcheck_rational.py` and the replays are not
preregistered. (5) C1 for D = 0 classes uses only the bd invariant, since the linear energy is not
in a D = 0 class.

| Control | Status | Content |
|---|---|---|
| K1 | PASS | ax, fd, bd × 20 states × 30 steps: 3D RZ equals the reduced 1D rule; Q at `2^15` equals `2^15 +` RZ; `max|y| = 366` |
| K2 | PASS | `G` is nearest-integer rounding of `s/3` on `[−300, 300]`; the inverse undoes `F` (1D, 3D; 50 states) |
| P1 | PASS | bd reduction, all 22 classes: none certified; `Σ φ(u_{k+1} − p_k)` in `ker E` exactly and nontrivial in each |
| P2 | PASS | 3D linear rule `y' = S y − p` in P3(2): not certified (excess 16 in D2, 40 in D); `y·y + p·p − y·Sp` in `ker E` exactly and nontrivial |
| C1 | PASS | every rounded class: the bd invariant and the 1/3-coupling linear energy each have an exact witness with `ΔΦ ≠ 0`; e.g. 3D, torus `1×1×2`, `p = (−4,−4)`, `y = (−2,−4)`: `ΔE = 2/3` |
| C2 | PASS | a planted coboundary is classified trivial; the P1 invariant plus it stays nontrivial |
| C3 | PASS | every `T` generator annihilates every equation mod `p`, and 200 equations exactly |
| COVER | PASS | 70 of 70 preregistered classes present (22 × {bd, ax, fd} + 4 in D2) |
| XC | PASS | (not preregistered) independent ℚ-ranks for ax, fd, bd at (m, D) = (2,2), (3,2), (2,3), 400 equations each: excess 0, 0, 0 for ax and fd; 3, 5, 5 for bd (the first two equal to the main run; (2,3,1) is not in the grid) |
| replay | PASS | parts A and D2 rerun after the A01 code change: every rank and status identical |

***

## 3. Measurements

Plane-wave classes Q(m, D, μ) (`n` unknowns, `rank T`, `rank E` for ax / fd, excess for ax / fd and
for the bd control, largest absolute value in any configuration used or its image):

| Family | (m, D, μ) | n | rank T | rank E ax / fd | excess ax / fd | excess bd | max\|value\| |
|---|---|---|---|---|---|---|---|
| G1 | (2,2,1) | 15 | 6 | 9 / 9 | 0 / 0 | 3 | 18 |
| G1 | (3,2,1) | 28 | 15 | 13 / 13 | 0 / 0 | 5 | 17 |
| G1 | (4,2,1) | 45 | 28 | 17 / 17 | 0 / 0 | 7 | 18 |
| G1 | (2,4,1) | 70 | 15 | 55 / 55 | 0 / 0 | 7 | 18 |
| G1 | (3,4,1) | 210 | 70 | 140 / 140 | 0 / 0 | 19 | 18 |
| G1 | (4,4,1) | 495 | 210 | 285 / 285 | 0 / 0 | 39 | 18 |
| G2 | (2,2,3) | 1215 | 54 | 1161 / 1161 | 0 / 0 | 15 | 54 |
| G2 | (2,3,3) | 2835 | 90 | 2745 / 2745 | 0 / 0 | 21 | 54 |
| G2 | (2,4,3) | 5670 | 135 | 5535 / 5535 | 0 / 0 | 27 | 54 |
| G3 | (2,0,2) | 16 | 4 | 12 / 12 | 0 / 0 | 2 | 34 |
| G3 | (2,0,3) | 81 | 9 | 72 / 72 | 0 / 0 | 4 | 50 |
| G3 | (2,0,4) | 256 | 16 | 240 / 240 | 0 / 0 | 6 | 67 |
| G3 | (2,0,5) | 625 | 25 | 600 / 600 | 0 / 0 | 8 | 90 |
| G3 | (2,0,6) | 1296 | 36 | 1260 / 1260 | 0 / 0 | 10 | 102 |
| G3 | (2,0,8) | 4096 | 64 | 4032 / 4032 | 0 / 0 | 14 | 142 |
| G3 | (2,0,9) | 6561 | 81 | 6480 / 6480 | 0 / 0 | 16 | 160 |
| G3 | (3,0,2) | 64 | 16 | 48 / 48 | 0 / 0 | 4 | 35 |
| G3 | (3,0,3) | 729 | 81 | 648 / 648 | 0 / 0 | 12 | 51 |
| G3 | (3,0,4) | 4096 | 256 | 3840 / 3840 | 0 / 0 | 24 | 72 |
| G3 | (4,0,2) | 256 | 64 | 192 / 192 | 0 / 0 | 8 | 34 |
| G3 | (4,0,3) | 6561 | 729 | 5832 / 5832 | 0 / 0 | 36 | 54 |
| G3 | (5,0,2) | 1024 | 256 | 768 / 768 | 0 / 0 | 16 | 36 |

Direct 3D classes:

| Class | n | rank T (D / D2) | rank E | excess D / D2 | max\|value\| (run D) |
|---|---|---|---|---|---|
| 3D-LIN:P3(2) (control) | 120 | 43 / 67 | 37 | 40 / 16 | 42 |
| 3D-RZ:P3(2) | 120 | 43 / 67 | 53 | 24 / 0 | 18 |
| 3D-RZ:P3(3) | 680 | 103 / 199 | 481 | 96 / 0 | 18 |
| 3D-RZ:P3r(2) | 1080 | 43 / 67 | 1013 | 24 / 0 | 18 |

The last column is from run D; run D2, which stops at a prefix of the same equation sequence,
recorded 42, 17, 17, 18.

The bd excesses equal the counts of independent functions of the two transported fields
`a_k = u_{k+1} − p_k` (moving left) and `b_k = p_{k+1} − u_k` (moving right) that each class
contains; for D = 0 the excess is `2(μ − 1)`, the nonconstant indicators of `a_k` and of `b_k`
mod μ. The bd rule is the published rule on body-diagonal plane waves (Lemma 2), so these are
conserved quantities of the published rule on that invariant set. They are not restrictions of any
conserved 3D quantity in P3(2), P3(3) or P3r(2), all of which are trivial. (Non-conserved members
of these classes do restrict to them: `(y_{n+e1} − p_n)²` lies in P3(2) and restricts to the bd
invariant `(u_{k+1} − p_k)²`.)

CPU per part (`results.json`): A 472 s, B 610 s, C 698 s, D 123 s, D2 19 s.

***

## 4. Scope: what is and is not excluded

Excluded, for the rule on `ℤ³` (RZ, and Q through Lemma 6), with conservation on all periodic
configurations (or, by Lemma 4, on all finite-support ones):

- nontrivial translation-invariant additive quantities whose density is a star polynomial of
  degree ≤ 3, or a star quadratic with coefficients depending on the residues mod 3 of `(S y)_n`
  and `(S p)_n`;
- quantities nontrivial on axis or face-diagonal plane waves whose density restricts there to one
  of the 22 classes of §3. This covers densities of any transverse shape with extent ≤ 2 to 5 cells
  along the wave vector, as listed.

Not excluded:

- densities outside these classes: wider supports; higher degree; residues mod μ other than those
  run; functions of unbounded values that are neither polynomial nor periodic with a period run
  here (for example `|y|`, or functions with value-dependent structure beyond the windows);
- 3D quantities that are trivial on ax and fd plane waves but nontrivial elsewhere, for densities
  outside the three direct 3D classes;
- densities that are not translation invariant (for example parity-staggered), quantities with
  `E(t+1) = −E(t)`, and conserved quantities that are not additive (orbit labels of the bijection
  are conserved real functions and are not local);
- quantities conserved only modulo `q` (SM:292's quadratic is of that kind for the exact linear
  rule), and approximate or adiabatic invariants;
- Q-densities that do not agree with a class member on the value window `2^15 ± B` (Lemma 6), with
  `B ≤ 160` (1D) and `≤ 18` (3D).

UNIV-2 A2 reports excluding zero-flux star-local densities on value windows (UNIV-2 is merged on
`main` at `27187dc3`, PR #1444; cited here as provenance only); the classes
here allow flux, have unbounded values, and in the reductions have arbitrary transverse shape. They
do not contain A2's arbitrary-function star densities on `{−2,…,2}` in 3D; A2 is not re-derived.

***

## 5. Depth-first record (§A.31)

**Productivity test (fixed by the scope).** Gem iff (i) a conserved real energy with scope, or (ii)
an obstruction for a stated class.

- **Node 1. Plane-wave sector, ax and fd.** Branch: can a conserved quantity be nontrivial on the
  plane waves that the rounding acts on? Check: G1–G3 certificates. Verdict: no, in all 44 classes
  [EC]. Hidden assumption exposed: a quantity in these classes cannot distinguish homogeneous
  states, although the homogeneous dynamics `(a, b) ↦ (b, 2b − a)` conserves the drift `b − a`
  pointwise. The drift is an invariant of the uniform sector only, not the restriction of a
  conserved additive quantity of these classes.
- **Node 2. Direct 3D.** Branch: is the result an artefact of plane-wave restriction? Check: P3(2),
  P3(3), P3r(2) directly on 3D tori with sides 1–4. Run D: uncertified; no nontriviality witness was found
  for the 50 kernel vectors examined per class (a sampled search, not a proof). Diagnosis: incomplete trivial space (A01). Run D2: certified. Verdict: trivial in all
  three [EC]. Pressure test of the result: P2 shows that the same template finds the 3D linear
  energy when it exists, C1 shows that the equations reject the linear-wave energy under rounding,
  and XC reproduces the 1D ranks over ℚ with independent code.
- **Node 3. The body-diagonal sector.** On body-diagonal plane waves the rounding is exact and the
  published rule is the linear d'Alembert rule, with left- and right-moving fields whose additive
  functions are conserved (P1) [W, EC]. The rule therefore has invariant sectors with many
  conserved additive quantities, and they do not extend to the 3D classes of Node 2. [W, not
  checked] An energy built from these sector invariants alone would distinguish lattice directions,
  since the ax and fd plane-wave sectors carry no nontrivial invariant in the classes run.

**Classification.** NEW at this scope (author; awaiting review), negative: Nodes 1–2. ELABORATING:
Node 3. Fixed point: one pass; not reached.

**Consequence for G3 (stated, not adopted).** G3-HOM records the missing input as a native
conserved energy for the traced sector. On the present evidence the published rule supplies none in
the classes above. The manuscript statements that exact energy conservation is not shown for the
rounded rule (SM:294, Sub:459) are consistent with this record, which edits neither. SM:294 also
records, for the rounded rule at `q = 3` (d = 3, L = 2), no nonconstant polynomial invariant of
degree ≤ 2 over `𝔽₃`; that is a statement about invariants over a finite field at small `q`, and
the present classes (real-valued additive quantities, unbounded values, any torus) are a different
object. Routes not closed by this record:
the classes listed as not excluded in §4; a conserved quantity of a coarse-grained description; and
the exact linear member of the rule family, which has its conserved quadratic (modulo q) by SM §4.2.

***

## 6. Review must check

1. Lemma 3: the bijection `ℤ³/Λ_L → ℤ/L` for primitive `v`, the per-period equality, and that a
   3D quasi-polynomial density restricts into Q(m, D, μ) with the stated `m`.
2. Lemma 4: the boundary-layer bound for an unbounded alphabet (finitely many patterns occur).
3. Lemma 5: the inequality chain, in particular that `T ⊆ ker_ℚ E` holds for the generators as
   coded (`Class1D.tgen`, `Class3D.tgen_full`), and the float64 exactness bound in `mod_matmul`.
4. That the trivial space `T` is not too large: a `T` containing a nontrivial conserved quantity
   would make a certificate vacuous. Each generator is a constant or a difference of a monomial
   (times a residue indicator) and its translate; check `tgen_full`'s translation test and that
   residue patterns are carried uniformly in P3r.
5. Feature construction: windows, residue-pattern indexing (numpy `mod` is nonnegative), monomial
   exponents; `bd_invariant` and `lin_energy_1d` coefficients (P1, C1); `energy3d_density`.
6. Amendment A01: committed before D2 (`7bee0b1b`), D's outcome reported unchanged, and the D2
   decision labelled as governed by A01.
7. Lemma 6's window: the recorded `max|value|`, and that the statement is about Q-densities that
   agree with a class member on that window, not about every Q-density.
8. The scope list of §4, especially that "trivial on ax/fd plane waves" is not read as nonexistence
   for the plane-wave classes.
9. Reproduce: `python3 -I checks/g3w1_checks.py --part A` (≈ 8 min CPU), `--part B` (≈ 10 min),
   `--part C` (≈ 12 min), `--part D` (≈ 2 min), `--part D2` (< 1 min), then `--render`
   (exit 0, `controls_green: true`); `python3 -I checks/xcheck_rational.py` (seconds).
