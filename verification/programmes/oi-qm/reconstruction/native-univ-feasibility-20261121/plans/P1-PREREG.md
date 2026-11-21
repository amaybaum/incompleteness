# P1: narrow-class comparison census at q = 2, d = 2, and a paper design (preregistration)

**Standing.** Design and preregistration only, authorized by owner decision
[#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074)
item 3.4. Execution is not authorized: neither the census nor the P1-Q2 work beyond this design.
Item 3(b) places a paper design in step 1. This file is that design, and carrying out P1-Q2 (working
out the encoding and simulation argument) is P1 execution, gated with the census. P1 concerns comparison models only: no rule
found here replaces OI's native rule, and a universal member found here would not establish
universality of `R_q` (NOTE §4). A rule change would be a Layer-0 revision under §A.29.
Definitions (narrow class, staggered involution rule, NU1) are those of `NOTE.md` §3.1.

## 1. Question

**P1-Q1 (census).** In the narrow class at `q = 2`, `d = 2`, every rule is a staggered rule in which
a half-step flips `y(i)` iff `F(y_N, y_E, y_S, y_W) = 1` (NU1, consequence 2). Which `F` are
non-affine *and* carry (a) a moving localized pattern ("glider") on a background of spatial
period at most 2, and (b) at least one two-glider collision whose outcome is a set of gliders
different from the inputs? The search set is frozen in §2.

**P1-Q2 (paper design).** Is there a finite `q`, a narrow-class `F` on `ℤ²`, and an explicit
encoding under which the staggered rule simulates Morita–Ueno Model 1, the 16-state `2RPCA(4)`
of Def. 2.1 (p. 142), step for step with a constant slowdown? Model 1 reads, for each cell, its
four neighbours only (the facing part of each), as the narrow class reads its neighbours only. It differs in being
first-order and partitioned (`NOTE.md` §2). The deliverable is a written design and a list of
obstructions met. Building or testing the model needs step-2 authorization (decision 3(b)).

## 2. Search set (P1-Q1, frozen here)

- **Stage 1 (bounded):** the `2^6 = 64` neighbour functions invariant under the dihedral group
  `D4` of the four neighbours. The orbits of `{0,1}^4` under `D4` are `0000`, `1000`, `1100`
  (adjacent), `1010` (opposite), `1110` and `1111`. The 32 totalistic functions are among them.
- **Stage 2 (CI):** all `2^16` functions `F : {0,1}^4 → {0,1}`, reduced modulo the `D4` action
  and the conjugacy `y ↦ 1 − y`, under which `F(n)` becomes `F(1 − n)`. The reduction is computed and its orbit count checked by Burnside.
- **Backgrounds:** the uniform configurations `0` and `1`, and the four period-2 configurations
  (two checkerboards, two stripe directions). For each component, every background must first be
  verified to be an orbit of period dividing 4 under the staggered rule; one that is not is skipped
  and listed.
- **Gliders:** patterns differing from the background in a `w × w` window, `w ≤ 4`. A glider has
  period `p ≤ 16` half-step pairs and a nonzero displacement `s`. It is certified exactly: on a
  torus whose side exceeds `w + 4p + 2` (each half-step moves influence by one site), the state after `p` steps equals the initial state shifted
  by `s`. U1 §3 gives the induction argument that a torus certificate of this size holds on `ℤ²`.
- **Collisions:** for each certified glider pair (the same or two different types), every relative
  offset in a `6 × 6` window and every phase. The outcome is read at horizon `H = 64` steps after
  first contact.

## 3. Decision rule (fixed now)

- A rule is **affine** iff its algebraic normal form over `𝔽₂` has degree at most 1. This test is
  exact. Affine rules are excluded, since Theorem L covers them.
- A rule is a **candidate** iff it is non-affine, has at least one certified glider (§2), and has at
  least one collision whose outcome at `H` is a finite set of certified gliders and background,
  different from the inputs in number, type or direction.
- **Output:** the candidate list, with each rule's glider table and collision table, or "no
  candidate within the bounds of §2". The words "universal" and "not universal" are not used.
- **Void condition:** if any control in §4 is not green, no output is printed for the census.

## 4. Controls and countercontrols

| Id | Kind | Requirement |
|---|---|---|
| P1-K1 | exact count | the affinity test marks exactly 32 of the `2^16` functions affine (`2^5` affine Boolean functions of 4 variables) |
| P1-K2 | exact count | the Stage-1 set has exactly 64 members; the Stage-2 orbit count equals the Burnside value |
| P1-K3 | positive control, glider detector | the detector, run through the same generic interface on U1's billiard-ball block-rule implementation (U1 F1), certifies its diagonal glider |
| P1-K4 | countercontrol, glider detector | `F ≡ 0` (no flips) and `F ≡ 1` (all flips) yield no glider with `s ≠ 0` |
| P1-K5 | countercontrol, NU1 | on each candidate, a full second-order run equals the staggered run (re-run of C1's comparison) |
| P1-K6 | countercontrol, collision reader | a pair of gliders launched apart, never in contact before `H`, is read as "no collision" |

## 5. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint that measures it |
|---|---|
| The preregistration precedes the census | this file's commit is an ancestor of the first execution commit; the execution commit changes no file in `plans/` |
| The enumeration is complete | P1-K1 and P1-K2, asserted in the script |
| Every rule lies in the narrow class | `F` is built from its table, which takes only the four neighbour values; the script asserts the table length 16 |
| Glider certificates are exact | the torus side `> w + 4p + 2` is asserted for each certificate; equality is bitwise |
| Arithmetic is exact | `uint8` arrays, values asserted in `{0, 1}` at every step |
| Determinism | two runs give byte-identical output; the second is a replay |
| Controls precede verdicts | the script prints the census only after P1-K1 to P1-K6 hold |

## 6. Cost class (§A.40)

- **Stage 1** (64 rules): a bounded local run, minutes. It is still a census, so its execution
  needs authorization.
- **Stage 2** (`2^16` rules, collision tables): CI, sharded by rule orbit in a matrix, under an
  owner-approved dispatch (§A.43 item 4).
- **P1-Q2:** paper only, local.

## 7. What P1 would and would not establish

- **Would:** for `q = 2`, `d = 2`, the list of narrow-class rules with certified gliders and
  glider-producing collisions within the bounds of §2. This is evidence about the searched set only.
  P1-Q2 would give a written design or a named obstruction for simulating Morita–Ueno Model 1.
- **Would not:**
  - universality of any rule, since that needs an encoding, a construction and a correctness
    argument;
  - non-existence of a universal narrow-class rule, for a negative census;
  - anything about the native rule `R_q`, at `q = 2^16` or at other `q`, in `d = 3` or elsewhere.

## 8. Literature used

- Morita and Ueno, IEICE Trans. Inf. & Syst. E75-D(1) (1992) 141–147, read in full text: Def. 2.1
  and Lemmas 2.1–2.2 (p. 142); the 16-state model with `U = R = D = L = {0, 1}` (p. 143); the
  signal, stable block, mirror and I-gate of Model 1 (p. 144, Figs. 10–13).
- Margolus, Physica D 10 (1984) 81–95: the p. 84 footnote on decoupling; App. A.
- Kari, Math. Systems Theory 29 (1996) 47–61, and Durand-Lose, DMTCS (2001): block-permutation
  representations [abstract level]. They are a second route for P1-Q2.
- Q2R (Vichniac, Physica D 10 (1984) 96–116) [bibliographic record located; the Q2R definition is
  cited from memory]. The 2-D Q2R rule `F = [y_N + y_E + y_S + y_W = 2]` is a Stage-1 member.
