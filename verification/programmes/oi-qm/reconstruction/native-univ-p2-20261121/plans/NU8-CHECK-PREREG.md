# NU8-CHECK: exact comparison of the NU8 design with its target PCA (preregistration; not run)

**Standing.** Preregistration only. Running it is a computational experiment, which
[#1169 c.7064767045](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064767045)
does not authorize; it needs a separate owner authorization. NU8 is `NOTE.md` §3.

## Question

Does the rule `R_P` of NU8 satisfy `Φ³ ∘ E = E ∘ F_P`? Here `Φ` is its staggered component and
`P` a 16-state `2RPCA(4)`.

## Instances (frozen)

- **Local functions.** 20 seeded random bijections `f_P` of `{0,1}^4` with `f_P(0) = 0`, and the
  identity.
- **Configurations.** For each, 5 seeded random configurations on a `12 × 12` PCA torus, which is a
  `24 × 24` staggered torus. Every side is even, so NU1 applies.
- **Length.** 10 PCA steps, that is, 30 second-order steps.

## Decision rule (fixed now)

- **Pass:** for every instance and every PCA step `n ≤ 10`, the second-order run started at `E(c)`
  equals `E(F_P^n(c))` bitwise at step `3n`.
- **Report:** "consistent with exact runs on the sampled instances" on a pass, or the first failing
  instance otherwise. The verdict text is generated from the measurements.
- **Void:** if any control below is not green, no verdict is printed.

## Controls and countercontrols

| Id | Kind | Requirement |
|---|---|---|
| K1 | independent reference | `F_P` is implemented directly from Morita–Ueno Def. 2.1. That code imports nothing from the `R_P` implementation |
| K2 | countercontrol: wrong encoding | `E` with the sign of the edge data flipped (`+e` in place of `−e`) fails at `n = 1` on some instance |
| K3 | countercontrol: non-bijective `f` | a non-injective `f` (two inputs to one output) makes phase 3 fail to recover `X` on some instance. The comparison reports a failure; it does not pass silently |
| K4 | countercontrol: self-term | adding the site's own value to `F` (outside the narrow class) breaks the equality |
| K5 | invariant | the other component stays 0 at every tick |

## Invariant → checkpoint (§A.41)

| Invariant | Checkpoint |
|---|---|
| Preregistration before the run | this file's commit is an ancestor of the run's commit, and the run changes nothing in `plans/` |
| Exact arithmetic in `ℤ/8995` | integer arrays reduced mod 8995; the CRT fields are checked by reducing every value mod 5, 7 and 257 |
| `F` reads only the four neighbours | `F` is a function of the ordered neighbour tuple only; the code passes it no other argument |
| Determinism | a replay is byte-identical |

## Cost class

Bounded local: seconds. It is still a computation, and it is gated.

## What it would and would not establish

- **Would:** evidence that the NU8 construction is implemented as written, on the sampled
  instances.
- **Would not:**
  - NU8 itself: the proof is on paper, and a pass is evidence about the sampled instances only;
  - the universality of Model 1;
  - anything about `R_q`.
