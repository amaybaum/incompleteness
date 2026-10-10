# HO-2 (v1) — bridge → equivalence, countermodels: finite and locally finite substrata cannot carry the sufficient composite actions

**From** `research/bridge` (node B3). **To** `research/equivalence` (the sourcing of K∞-Act / K∞-Drive; F-D3) and
`research/countermodels` (Conjecture B3.C). Also relevant to `research/origin` (O3-T5's stage-crossing datum), which
may receive it by the same receipt. Version 1, 2026-10-10.

## Statements and labels

**HO-2a (fixed finite pair substratum).** Hypotheses: `cnot` and the token operations in the pair context are realized
as readout-respecting permutations of a finite `Λ` with spanning readout `R : ℝ^Λ → W 3`. Conclusions: the realized
group on `W 3` is finite [W: a homomorphic image of a subgroup of `Sym(Λ)`]; if it consists of unitary or antiunitary
conjugations, claim D (stage-4 Z, audited [A]) gives an exotic self-dual invariant cone with H1–H3; so (b), granted for
every realized operation, does not force `Q3`. Native instance: `⟨cnot, local octahedral rotations⟩` has order 11520 [X].
Label: FAILED as a route to A_miss (kept with evidence); the obstruction itself CONDITIONAL on claim D [A] and [W].

**HO-2b (R1 and the gate).** `R1 = (1/9)[[8,1,4],[4,−4,−7],[1,8,−4]]`, the order-3 rotation about (5,1,1), forces `Q3`
together with `cnot` (stage 4 Y7 [A]) and is realized on an 18-point ontic token [X]; but `tr(cnot · actC R1) = 10/9 ∉ ℤ`
[X], so `⟨cnot, actC R1⟩` is infinite and `R1` and `cnot` are never realized together on a finite pair substratum.
Label: [X] exact (the trace), [W] (the algebraic-integer argument); FAILED as a finite-substratum route.

**HO-2c (directed towers).** The closure of a directed union of finite pair groups has abelian identity component;
hence no tower realizing `cnot` realizes an off-frame local circle (`[A_n, cnot A_n cnot] ≠ 0` for `n = (3/5, 0, 4/5)`
[X]), two non-commuting local circles (A_miss), or `R1`. On one token, an increasing chain of finite subgroups of
`SO(3)` ends cyclic or dihedral about one axis, so off-axis `ElementaryDrivability` (KInfFoundations.lean:264) is never
the closure of directed stage-preserving finite operations — the generator must cross stages (sharpens F-D3).
Label: CONDITIONAL on Jordan's theorem [L] and the classification of finite subgroups of `SO(3)` [L]; FAILED as a
tower route.

**HO-2d (A_miss as rational matrices).** By closure, A_miss ⟺ (b) for `{R_z(θ), R_x(θ)}` with `cos θ = 3/5` (`tr = 11/5`,
infinite order); K(Z_F) is moved out by each of `R_z(θ)` (witness `−1/10`), `S` (`−1/8`), `R1` (`−79/720`).
Label: CONDITIONAL (on `K` closed — part of the candidate setting; density of an irrational rotation [W]); witnesses [X].

**Open (Conjecture B3.C, for countermodels).** Does every compact pair group containing `cnot` with abelian identity
component leave an exotic invariant cone? Partial results in NOTES-B3 §2.1: `dim H₀ ≤ 1`; covered when `H₀` has simple
spectrum on an orthonormal product basis or with no product eigenline (local phase-flow tori, the monomial torus, stage-4
S2, the Bell-diagonal torus); OPEN for eigenbases with one to three product lines and for degenerate 2-tori.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5f4089a4500a59943c33ba13656b2530824068c5` |
| proposal | `research/bridge/handoff-proposals/HP-2-finite-substrata.md`, sha256 `ea94bb0b2aa81df10c3114731590c9a1daf7d45fcbb88ca7e4134fda893567ed` |
| results rows | `research/bridge/RESULTS.md` B3-1 … B3-6 (sha256 `eac88347fa62fec0…`) ; `NOTES-B3.md` |
| script, output | `research/bridge/experiments/b3_finite.py` (sha256 prefix `b45b38929770f99d`), `.out` (`c9b7265170ca1594`), 11/11, run 1 kept |
| coordinator audit | replay byte-identical; `indep_checkB.py` X1 (`tr(cnot · actC R1) = 10/9`, control `tr(cnot · actC cyc3)` integral; `cnot² = 1`, `R1³ = 1`) and X2 (order 11520 of `⟨cnot, actC O, actT O⟩`) CONFIRMED; X3 witnesses CONFIRMED |

## What the receiving threads may assume

The four statements at their labels. For `research/equivalence`: HO-2c's one-token clause as a CONDITIONAL [L]
constraint on any sourcing of K∞-Act / K∞-Drive through finite stage-preserving operations (the generator must cross
stages). For `research/countermodels`: B3.C as an OPEN conjecture with the partial results named.

## What they may not assume

- that "no locally finite H-level substratum forces `Q3`" is unconditional — that is exactly B3.C;
- that the literature inputs (Jordan; finite subgroups of `SO(3)`) have been checked in this programme: they are [L];
- any kernel status: nothing here is CERTIFIED.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-2 v1` and records in its `LOG.md`
whether and how it relies on it.
