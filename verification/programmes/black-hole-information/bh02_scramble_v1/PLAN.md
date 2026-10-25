# BH-02 / BH-04 — permutation dynamics versus quantum scrambling; Page-time fraction

Status: preregistration for exploratory research under OI-BH-1 (`../PROGRAMME.md`, items BH-02,
BH-04, lane 3). Written before any computation. Not a manuscript amendment, theorem
designation or merge authorization. Drafting snapshot `D` = `809fac52` (branch
`research/oi-bh-information-audit`).

## 0. Question

Does classical reversible (permutation) dynamics generate the entanglement behaviour the
Page-curve argument of `book/ch07-gravity.md` §7.6 and `papers/GR.md` Appendix A.7
(Theorems A.7–A.9) needs, or must the condition H-scramble supply it? Separately (BH-04): on
which inputs does the fraction `t_P/t_evap = 1 − 2^{-3/2}` depend?

Owner safeguard. The quantum comparison must not assume the Page-curve behaviour it is used to
explain. Every quantum ensemble or circuit used below is labelled **SUPPLIED** (an input chosen
by the analyst: Haar measure, a seeded random two-qubit brickwork circuit, a superposition
initial state). None of them is an OI mechanism, and no result below derives H-scramble.

## 1. Definitions

- **Configurations.** `X = {0,…,q−1}^n` (here mostly `q = 2`, qubits; one exhaustive check at
  `q = 3`). Hilbert space `H = C^X` with computational (configuration) basis `|x⟩`.
- **Aligned bipartition.** A subset `R ⊆ {1,…,n}` of coordinates (radiation) and its complement
  `B` (black hole), so `H = H_R ⊗ H_B` with `d_R = q^{|R|}`, `d_B = q^{|B|}`. Emission is modelled
  by a nondecreasing schedule `r(t)`, `R_t = {1,…,r(t)}`, from `r = 0` to `r = n`.
- **Permutation unitary.** For a bijection `π: X → X`, `P_π|x⟩ = |π(x)⟩`. Dynamics
  `ψ_t = P_π^t ψ_0`. Because `π^t` is itself a bijection, the set of all states reachable from
  `ψ_0` by any power of any permutation equals `{P_σ ψ_0 : σ ∈ Sym(X)}`; an exhaustive sweep over
  `Sym(X)` therefore covers every time step of every permutation dynamics.
- **Reduced state and entropies.** `ρ_R = Tr_B |ψ⟩⟨ψ|`; Schmidt rank `= rank` of the
  `d_R × d_B` amplitude matrix `M`; purity `Tr ρ_R²`; Rényi-2 `S_2 = −ln Tr ρ_R²`; von Neumann
  `S = −Tr ρ_R ln ρ_R`. `p_0(x) = |⟨x|ψ_0⟩|²`, `H(p_0)` its Shannon entropy.
  `|+^n⟩ = q^{-n/2} Σ_x |x⟩`; `F(ψ) = |⟨+^n|ψ⟩|²`.
- **Page value (SUPPLIED Haar ensemble).** For `m ≤ k`, Page's exact Haar average
  `S_Page(m,k) = Σ_{j=k+1}^{mk} 1/j − (m−1)/(2k)` (Page 1993; proved by Foong–Kanno 1994,
  Sánchez-Ruiz 1995, Sen 1996), a rational number. Haar mean purity `(m+k)/(mk+1)` (Lubkin 1978).
  GR Theorem A.8 uses the approximation `ln m − m/(2k)`; both are reported.
- **Page-like (operational, preregistered).** A state at a cut `(m,k)` is *Page-like* iff
  `|S − S_Page(m,k)| ≤ 0.10` nats. A curve is Page-like iff every interior cut of it is.
  The tolerance is fixed here, before measurement.
- **Exactness.** Schmidt ranks, purities, overlaps, Page values and every claimed equality or
  inequality that admits it are computed in exact rational arithmetic (`fractions.Fraction`),
  in `Q(√2)`, or with rigorous rational interval bounds on logarithms (atanh series with explicit
  remainder). Von Neumann entropies of generic states are **NUMERICAL** (Jacobi eigenvalues in
  double precision) and are controlled against the exact purity: `|Σλ − 1|` and
  `|Σλ² − Tr ρ²_exact|` must each be `≤ 1e-10`, or the run is VOID.

## 2. Claims and preregistered decision rules

Verdict vocabulary: PROVED / CONDITIONAL / COUNTEREXAMPLE / OPEN; VOID if a required control
fails. Verdict text is generated from measurements by `checks.py`.

**C1 — non-scrambling control (the programme's named control).** For every bijection `π`, every
configuration initial state `|x_0⟩`, every `t` and every aligned bipartition, `ψ_t` is a
configuration basis state, Schmidt rank 1, `S(R) = 0` exactly.
- Proof obligation: `P_π` maps basis vectors to basis vectors (stated analytically in REPORT).
- Exhaustive check: all of `Sym(X)` for `(q,n) = (2,2)` (24), `(2,3)` (40 320), `(3,2)`
  (362 880): `P_σ` built as a matrix, verified to be a permutation matrix, applied to every basis
  vector; exact Schmidt rank at every aligned bipartition. Seeded sample of 500 permutations at
  `(2,4)`, full orbits.
- Rule: PROVED iff the proof holds, zero rank-`>1` states are found, and countercontrols CC1
  (Bell state, rank 2) and CC2 (non-permutation rational rotation followed by CNOT applied to a
  basis state, rank 2) are both detected. COUNTEREXAMPLE iff any rank-`>1` state arises under a
  permutation. VOID if a countercontrol is not detected or a sampled `σ` is not a bijection.

**C2 — entropy budget of permutation dynamics on any initial state.** For every `π`, pure
`ψ_0`, `t`, aligned bipartition:
(i) the amplitude multiset of `ψ_t` equals that of `ψ_0`; Schmidt rank `≤ |supp ψ_0|`, hence
`S(R) ≤ ln |supp ψ_0|`;
(ii) `S(R) ≤ min(H(p_R), H(p_B)) ≤ H(p_0)`, with `p_R, p_B` the configuration marginals at `t`;
(iii) `F(ψ_t) = F(ψ_0)` and `λ_max(ρ_R) ≥ F(ψ_0)`, hence `S_2(R) ≤ −2 ln F(ψ_0)` and
`S_∞(R) ≤ −ln F(ψ_0)`.
- Checks: (i), (iii) exactly, over all of `Sym(X)` at `(2,3)` for three rational-amplitude
  initial states (products of `(3/5, 4/5)` factors and one entangled rational state), all six
  aligned bipartitions; (ii) NUMERICAL on the same set with margin reported.
- Tightness witness (exact): a CNOT network (a permutation) maps `|+⟩^k|0⟩^{n−k}` to `k` Bell
  pairs across a cut; exact rank `2^k` and exact purity `2^{-k}` together certify a flat
  spectrum, so `S = k ln 2 = H(p_0)` exactly.
- Countercontrol CC3: a rational non-permutation rotation changes `F` and raises the Schmidt rank
  of a basis state above `|supp| = 1`.
- Rule: PROVED iff the analytic proofs hold, the exact sweeps find no violation, the tightness
  witness is exact and CC3 is detected; COUNTEREXAMPLE iff any exact violation; VOID otherwise.

**C3 — what permutations can do with a SUPPLIED superposition.** Initial state
`ψ_0 = |−⟩⊗|+⟩^{n−1}` (a product state in the conjugate basis, amplitudes `±2^{-n/2}`), seeded
uniformly random permutations; also a fixed permutation iterated with the emission schedule
`r(t) = t`. Measure exact purity at every cut and NUMERICAL `S`; compare with the exact
`S_Page`. Diagnostic variant: brickwork of seeded random three-bit reversible gates (local
permutations), depth sweep.
- Controls: CC4 (`|+^n⟩` is invariant under every permutation: `S = 0` at every cut, every step;
  the Page-like criterion must fail), CC5 (a low-`H(p_0)` product state must obey the C2 bound),
  CT1 (SUPPLIED Haar states at the same `n` must meet the Page-like criterion, showing it is
  attainable).
- Rule: report the fraction of sampled permutations whose half-cut state is Page-like and
  whether the iterated curve is Page-like. If Page-like states occur, the verdict is
  COUNTEREXAMPLE to "permutation dynamics cannot produce Page-like entanglement", scoped to
  supplied non-configuration initial states (equivalently, to a bipartition not aligned with the
  configuration basis); it is not a derivation of H-scramble. If none occur, report OPEN at the
  sizes tested.

**C4 — classical-ignorance analogue.** For a probability distribution `p_0` over configurations
evolved by `π` (a classical mixed state), the Shannon entropy of the radiation marginal obeys
`H(p_{R_t}) ≤ H(p_t) = H(p_0) = H(p_{R_final})`: the curve attains its maximum at full emission
and cannot turn over to zero. Proof analytic; NUMERICAL demonstration on a seeded example; the
pure-state curve (C3) is the countercontrol (returns to 0). Rule: PROVED iff proof holds and the
demonstration shows no violation beyond `1e-12`.

**C5 — SUPPLIED quantum comparison.** (a) Exact `S_Page(m,k)` and its GR approximation for all
`m ≤ k`, `mk ≤ 2^{10}` (powers of 2), including the GR Appendix A figure for `d_B = d_R = 4`
and the finite-size correction `−1/2` claimed at `n_R = n_B`. (b) Monte Carlo control: seeded
complex-Gaussian Haar sampling at `(m,k) ∈ {(2,2),(2,4),(4,4)}`, 4000 samples: sample means of
`S` and purity within 4 standard errors of the exact values. Countercontrol: a real-Gaussian
sampler must be rejected on purity (real mean `(m+k+1)/(mk+2)`). (c) A SUPPLIED circuit: brickwork
of seeded Haar two-qubit gates on `n = 8` from `|0⟩^n`, half-cut `S` versus depth, and the
emission curve at the final depth against `S_Page`. Rule: the comparison is reported as
measurements; it is VOID if the Monte Carlo control or the gate-unitarity control (`‖U†U − I‖
≤ 1e-12`) fails.

**C6 — H-scramble logical-dependency audit (GR Appendix A.7).** Quote the exact statement; name
its ensemble, measure and dynamical content; then test:
(a) *Satisfiability in OI's own setting.* GR Theorem A.7's proof takes the total state pure by
"deterministic evolution from a definite initial state". If the B/R factorization is aligned
with configurations, C1 implies the orbit of a definite configuration consists of product basis
states for every `φ`, so H-scramble fails for every bijection in that setting. Rule: PROVED
(exact) if C1 is PROVED.
(b) *Does H-scramble presuppose the Page value?* Trace the proof of Theorem A.8 step by step and
record which step supplies the number `S_Page`. Rule: report "the Page value enters through the
SUPPLIED Haar ensemble that H-scramble posits" iff no step of the proof other than the H-scramble
step produces a quantity depending on `d_B, d_R` beyond the trivial bound `ln d_min`.
(c) *Shell factorization.* Theorem A.8 posits equidistribution on an energy-shell subspace
`Σ_E ⊂ H_B ⊗ H_R` but states the Page value with the full factor dimensions. Exact witness: a
conserved Hamming weight `w` (a toy energy) in `n` qubits; by concavity the Haar-on-shell mean
entropy is at most `S(Tr_B Π_w / dim Π_w)`. Certify with rigorous log intervals whether this upper
bound lies strictly below the exact `S_Page(d_R, d_B)` for `(n,w,|R|) ∈ {(6,3,3), (8,4,4),
(10,5,5)}`, with a NUMERICAL Haar-on-shell diagnostic. Rule: CONDITIONAL (an unstated hypothesis
in A.8) iff the strict inequality is certified for at least one case; otherwise no finding.
(d) *Time average versus instantaneous value; moving partition.* Logical audit only: A.8 bounds
a cycle time-average at a fixed bipartition; A.9 applies it at each `t` with a changing
bipartition along one trajectory that starts from a definite (product) state. Rule: record as an
OPEN proof obligation (no computation is claimed to settle it).

**C7 — BH-04 Page-time fraction.** Exact checks:
(a) `dM/dt = −a/M²`, constant `a > 0` ⇒ `u = M³` obeys `du/dt = −3a`, `t_evap = M_0³/(3a)`,
`t/t_evap = 1 − (M/M_0)³` (exact rational checks of the ODE in `u`).
(b) Turnover at half the initial black-hole entropy with `S ∝ M²` ⇒ `M/M_0 = 2^{-1/2}`,
`t_P/t_evap = 1 − √2/4` in `Q(√2)`; certified decimal interval.
(c) A constant multiplicative greybody/species factor `a → Γa` leaves the fraction unchanged
(exact).
(d) Mass-dependent effective coefficient: power law `a ∝ M^{-p}` gives `1 − 2^{-(3+p)/2}`;
step model `a = a_1` above `M_*`, `a_2` below, exact fraction in `Q(√2)` for rational
`μ = M_*/M_0`, `a_2/a_1`, showing dependence on `M_0` through `μ`, and the size of the
correction as `μ → 0`.
(e) Turnover criterion: with radiation coarse-grained entropy `β` times the black-hole entropy
decrease, turnover at `β(S_0 − S) = S` gives `t_P/t_evap = 1 − (β/(1+β))^{3/2}`. External
control: with Page's literature value `β ≈ 1.4847` (photons and gravitons from a large
Schwarzschild hole; Page 1976 as used in Page 2013, arXiv:1301.4995), the formula must reproduce
Page 2013's quoted `0.5381` of the evaporation time and `40.25%` entropy loss to 4 decimal
places; otherwise C7(e) is VOID. Sensitivity for `β ∈ {1, 4/3, 1.4847, 3/2, 2}`.
- Rule: "independent of mass and greybody factor" is PROVED only for (c); it is CONDITIONAL on
constant `a` and on `β = 1` (equivalently `n_R(t) = n_B(0) − n_B(t)`); a computed change of the
fraction under (d) or (e) is reported as COUNTEREXAMPLE to the unconditional reading.

## 3. Controls, countercontrols and their mutants

Each control is shown able to fail by a mutant (`mutants.py`) that patches exactly one function
and names the control it targets; a mutant counts as caught only if its targeted control fails
and every other control passes.

| control | what it checks | mutant |
|---|---|---|
| K-bij | every sampled `σ` is a bijection; `P_σ` is a permutation matrix | sampler duplicates an element |
| K-rank | exact rank detects CC1, CC2 | rank function returns 1 |
| K-overlap | CC3 changes `F`; permutations conserve `F` | rotation replaced by identity |
| K-tight | CNOT-network witness gives rank `2^k`, purity `2^{-k}` | CNOT target misplaced |
| K-eig | eigenvalues reproduce exact purity, sum 1 | Jacobi rotation sign error |
| K-page-mc | Haar Monte Carlo matches exact Page and purity; real sampler rejected | real-Gaussian sampler |
| K-page-formula | harmonic sum bounds | off-by-one in sum |
| K-unitary | supplied two-qubit gates unitary | Gram–Schmidt without normalization |
| K-ln | rigorous log interval contains the value and is consistent (`ln 4 = 2 ln 2`) | series remainder dropped, few terms |
| K-plus | `|+^n⟩` invariant under permutations (CC4) | initial state built off by one sign |
| K-page2013 | β-formula reproduces 0.5381 / 40.25% | exponent 3/2 replaced by 1 |

## 4. Invariant → checkpoint table (§A.41)

| invariant asserted | checkpoint |
|---|---|
| determinism, byte-identical output | `checks.py` run twice under `-I -B` and once under `-I -B -O`; `cmp` against `result.json` |
| no `assert`-based check | grep of `checks.py`, `mutants.py` for `assert` returns nothing |
| fixed seeds | seeds printed in `result.json`; replay match |
| exact claims are exact | every exact field in `result.json` is a rational string or `Q(√2)` pair; interval bounds rational |
| numerics controlled | K-eig per diagonalization; VOID on breach |
| verdicts generated over green controls | `checks.py` prints VOID and exits 2 if any control fails; verdict strings built from measured fields |
| each control can fail | `mutants.py` output: every mutant caught, targeted control only |
| runtime budget | wall times printed to stderr only (not in `result.json`) |
| provenance | `PROVENANCE.json` names commit, interpreter, command; `SHA256SUMS` over the files |

## 5. What this would and would not establish

Would: exact statements about permutation unitaries acting on configuration-basis Hilbert spaces
with aligned bipartitions; exact limits on what such dynamics can do with any initial state; a
dependency map for H-scramble and for the 0.646 fraction; small-system numerical comparisons
with supplied quantum ensembles.

Would not: any statement about black holes as physical systems; any derivation or refutation of
H-scramble for an emergent Hilbert-space factorization that is not aligned with substratum
configurations (that factorization is not specified in the cited text and is named as the open
question); any statement about QES/island computations beyond identifying which radiation-entropy
accounting a Page-time comparison requires. Results are scoped to the constructions tested.
