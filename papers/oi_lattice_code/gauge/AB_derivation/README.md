# gamma3/ — Finite-lattice computation of A·B in OI induced gauge theory

This directory contains the finite-lattice perturbation theory calculation of the
`(A, B)` parameter product entering the SM gauge-coupling threshold. The integrals
are evaluated independently of the fitted SU(2)/SU(3) product; their extrapolation
to infinite volume depends on the assumed leading finite-size power.

## Headline result

**A·B ≈ 48–62 across finite-size models; comparison inconclusive.**
The fitted product is **A·B = 46.4**, from observed SU(2)/SU(3) couplings at M_Z.

The selected 1/N² fit and Shanks extrapolators give the estimate
**A·B = 48.0 ± 1.5**, where the quoted spread excludes leading-power uncertainty
and subleading systematics. A leading 1/N fit gives approximately 61 and fits
the six-point sequence better. The cross-check remains inconclusive pending
substantially larger lattices or a derivation of the leading finite-size power
(SM.md §6.2.1); the 48–62 range is a range of model estimates, not a confidence interval.

The model-conditional A·B calculation supplies a numerical threshold cross-check. The SU(2) and SU(3) entries in SM.md §6.3 remain
**retrodictions**: δ₀ and the full `C_2`-dependent threshold parameterization are
still empirical (δ₀ is treated as empirical input — see SM.md §6.2). Per SM.md §6.3,
deriving the `C_2`-dependent threshold parameters from first-principles lattice PT
is the open computational task that would upgrade the SU(2) and SU(3) couplings
from retrodictions to strict predictions. The finite-lattice calculation gives a few-percent comparison with the fit only
under the selected 1/N²/Shanks extrapolation; the comparison across finite-size
models remains inconclusive.

## Quick reproduction

```bash
# Fast run (~2 minutes, up to N=28; selected-model extrapolation):
python3 reproduce_AB.py --max-N 28

# Full run (~45 minutes, up to N=40; selected-model estimator spread):
python3 reproduce_AB.py --max-N 40
```

## The calculation in brief

The `C_2`-dependent threshold contributes to `1/α_i(M_Z)` via
`A·ln(1 + B·C_2·g_0²)`. At leading order in `C_2·g_0²`, this equals
`A·B·C_2·g_0²`. We compute this leading coefficient from 2-loop lattice PT
in the induced gauge theory:

1. **Ingredient**: Induced gauge propagator `D_ind(k) = 1/(k̂²·Π_s)`, with
   `Π_s(0)` the paper's 1-loop staggered VP (converges to 0.308).

2. **Diagrams**: Bubble (two Wilson 3-gluon vertices) + FP ghost (with
   induced propagator). Tadpole with continuum V_4g contributes only to
   the gauge-violating mass, not to the transverse `Π_T` — so can be
   neglected at leading order.

3. **Extraction**: At each lattice size N, compute `Σ^{μν}(p)` at small
   external momenta, extract `Π_T(p²=0)·Π_s²` via `(Σ^{11}-Σ^{00})/p̂²`,
   then compute A·B(N) using each N's own Π_s(N) and b_0 capture(N).

4. **Conversion formula** (validated by std QCD cross-check):
   `δ(1/α) = 4π · |Π_T| / b_0_capture`, where `b_0_capture` is the lattice's
   reproduction fraction of textbook `b_0 = 11/3`. Verified to reproduce
   textbook δ(1/α) to 100% at N=28.

5. **Model-dependent extrapolation**: Apply linear 1/N² fits and iterated
   Shanks acceleration to the stored `A·B(N)` sequence. Shanks-3/4 gives 47.9
   and the 1/N² fit on the largest three N gives 50.1. These estimates do not
   cover uncertainty in the leading finite-size power: a leading 1/N fit
   gives approximately 61 (SM.md §6.2.1).

## Per-N data (m=0.05, up to N=40)

| N | Π_s(N) | Π·Π_s²(N) | b_0 capture(N) | A·B(N) |
|---|---|---|---|---|
| 16 | 0.401 | −0.0485 | 0.651 | 14.0 |
| 20 | 0.345 | −0.0530 | 0.523 | 22.1 |
| 24 | 0.326 | −0.0567 | 0.460 | 28.5 |
| 28 | 0.317 | −0.0599 | 0.427 | 33.3 |
| 32 | 0.314 | −0.0626 | 0.408 | 36.9 |
| 36 | 0.311 | −0.0651 | 0.398 | 39.6 |
| 40 | 0.310 | −0.0673 | 0.392 | 41.7 |

Extrapolations to N→∞:
- 1/N² fit (N=32,36,40): **A·B = 50.1** (residual std 0.05)
- Shanks-2 last: 48.0
- Shanks-3 last: 47.9
- Shanks-4 last: **47.9** (fully stable)

Selected 1/N²/Shanks estimate: **A·B = 48.0 ± 1.5**. This is the spread
among the selected estimators, excluding leading-power and subleading uncertainties.

## File organization

### Primary files (for reproducing A·B)

| File | Purpose |
|------|---------|
| `reproduce_AB.py` | **End-to-end driver.** Runs all calculations. |
| `paper_pi_s.py` | Compute `Π_s(0)` (1-loop staggered VP) — reproduces paper's 0.308 |
| `yang_mills_lattice.py` | Wilson-action 3-gluon vertex `V_3g_ym` and continuum reference |
| `bubble_at_finite_p.py` | `Σ^{μν}_bubble(p)` via 2×V_3g + 2×D_ind |
| `ghost_self_energy.py` | FP ghost bubble (supports standard and induced propagators) |
| `tadpole_self_energy.py` | Tadpole with continuum V_4g (contributes to `Σ(0)` only) |
| `p_extrapolation.py` | Small-p fit at each N, cross-N extrapolation |
| `qcd_crosscheck.py` | Standard-QCD validation & `b_0` capture measurement |

### Support infrastructure

| File | Purpose |
|------|---------|
| `vertices.py` | Staggered Dirac operator `D` and its derivative vertices `D^(n)_μ` |
| `colors.py` | SU(3) structure constants `f^{abc}`, totally symmetric `d^{abc}` |
| `topologies.py` | Γ_3 diagram topologies (for induced 3-gluon vertex calc) |
| `gamma3.py` | Full induced Γ_3 vertex from fermion triangle (used in c_F3 work) |

## Conventions

- Brillouin zone: `(−π, π]`, not `[0, 2π)`. Critical for any expression
  involving `p̂_μ = 2·sin(p_μ/2)`.
- Units: lattice spacing `a = 1`; momenta are dimensionless.
- Propagator convention (induced): `D_ind(k) = 1/(k̂²·Π_s)` with
  `k̂² = Σ_μ(2·sin(k_μ/2))²`. This matches SM.md line 566.
- Wilson 3-gluon vertex: Wilson plaquette action expanded to 3rd order
  in `A`, standard `cos(p_μ/2)` factors.
- Color: stripped; SU(3) `f^{abc}f^{abc}` contraction absorbed as `C_2(adj)`.
- Feynman-like gauge for ghost computations (paper's framework has no
  formal gauge fixing; the effective Feynman gauge is consistent with
  D_ind being a scalar propagator).

## Key equations

From the standard-QCD cross-check, the relation between lattice-computed
`Π_T` (coupling-stripped) and the physical running of `1/α`:

```
δ(1/α) = 4π · |Π_T| / b_0_capture  (per C_2, at g=1 convention)
```

Validated at N=28, m=0.05 std QCD: `4π·0.0821/0.427 = 2.42` matches
textbook `(b_0/4π)·log(π²/m²) = 2.42` to 100%.

Applied to OI:
```
A·B = δ(1/α) / g_0² 
    = (4π·|Π_T_OI|/b_0_capture) / (1/(6·Π_s))
    = 24π·Π_s·|Π_T_OI|/b_0_capture
```

With `|Π_T_OI·Π_s²| = 0.079` (Shanks), `Π_s = 0.308`, `capture = 0.40`:
```
A·B = 24π · 0.308 · (0.079/0.308²) / 0.40 = 48.3
```

## Uncertainty budget

| Source | Contribution |
|--------|---|
| Selected Shanks/1/N² estimator spread | ~3%, conditional on those convergence models |
| Leading finite-size power | unresolved; model estimates ≈48–62 |
| F³ correction | ~0.24% for the stated continuum coefficient; ~1.4% for the conservative bound (SM.md §6.2.1) |
| Lattice V_4g correction | per-topology cosine placement selected; exact normalized shift pending |
| Convention alignment with paper | ~2% (bounded by std QCD cross-check) |
| **Overall comparison** | **Inconclusive across finite-size models** |

The ~3% spread at N=40 describes the selected extrapolators, not the total
uncertainty. It does not resolve the leading-power dependence. The F³ sensitivity
has been propagated under the coefficient and normalization assumptions stated in
SM.md §6.2.1. The lattice V_4g vertex comparison selects the per-topology cosine
placement; its exact contribution in the present Π_s-normalized scheme remains
to be evaluated. No combined ±3% or ±6% precision is established.

## Open work for higher precision

1. **Extend substantially beyond N=40 or derive the leading finite-size power**
   — distinguish the competing extrapolation models for the induced normalization
   and `b_0_capture` division.

2. **Evaluate the selected lattice V_4g contribution** — use the per-topology
   cosine placement identified from Capitani Eq. (5.28), and normalize its tadpole
   `p²` contribution in the present induced-propagator scheme. The exact shift
   remains open (SM.md §6.2.1).

3. **Separate A from B** — requires the next-order coefficient of
   `(C_2·g_0²)²` in the resummed gauge self-energy. In the OI induced
   theory, this coefficient is **structurally suppressed at strict 2-loop
   across all color channels**, because no tree-level gauge self-interactions
   exist in the induced theory and induced 3- and 4-gluon vertices first
   appear at 3-loop order. A clean separation therefore requires 3-loop
   lattice perturbation theory or non-perturbative methods, both beyond
   the current scope. See SM.md §6.2.1 (Open work paragraph) for the
   structural argument. The strict-2-loop 9-topology sum has been computed
   directly at N=6,8,10,12 as a quantitative consistency check on the
   structural-suppression claim — see "Strict 2-loop (C_2·g_0²)² check"
   below.

4. **Resolve the normalization of the raw lattice F³ coefficient** before
   applying it in the bubble integration. Sensitivity to the declared continuum
   coefficients has already been propagated (SM.md §6.2.1).

## Strict 2-loop (C_2·g_0²)² check

The 9-topology 1PI 2-loop sum in the induced gauge theory was computed
at N=6,8,10,12 (m_reg=0.2, m_f=0.05, p²→0 extrapolation via λ=1,2,3) to
provide a quantitative consistency check on the structural-suppression
claim of SM.md §6.2.1.

Topologies (T = gluon, G = ghost): T1a kite, T1b vertex correction,
T1c V_4g bubble, T1d V_4g tadpole, T1e V_4g triple-line, G_a ghost
square, G_b ghost vertex correction, G_c ghost triangle, G_d V_4g ghost
bubble.

**Result (std-QCD-equivalent sum, no extra Π_s rescaling):**

| N  | Π_s(m=0.05) | Σ_topologies Π_T_std (sum) |
|----|-------------|----------------------------|
|  6 | 5.226       | −0.274 |
|  8 | 1.853       | −0.101 |
| 10 | 0.935       | −0.061 |
| 12 | 0.607       | −0.044 |

The sequence is smooth, monotone-decreasing in magnitude, and converges
toward small values — quantitatively consistent with the paper's claim
that the strict-2-loop coefficient is structurally suppressed (the C_A²
ghost channel alone is estimated at ~0.2% of A·B = ~0.1 in §6.2.1; our
total is the same order of magnitude, decreasing further with N).

**This is NOT a test of the log-resum coefficient c_2 = −A·B²/2 = −128.**
That coefficient cannot be obtained from strict 2-loop in OI by the
framework's own structure: the geometric series 1/(1−Σ) that builds up
to the log-form requires gauge self-couplings to iterate, and these
only appear starting at 3-loop in the induced theory. The strict-2-loop
calculation shown here therefore confirms structural suppression at the
expected order of magnitude, and does not (and cannot) reproduce −128.

### Strict-2-loop infrastructure files

The 9-topology calculation lives in `../c2_strict_2loop/`:

| File | Purpose |
|------|---------|
| `T1a_kite.py` ... `T1e_V4g_triple_line.py` | The 5 gluon topologies, numpy implementations |
| `G_a_ghost_square.py` ... `G_d_V4g_ghost_bubble.py` | The 4 ghost topologies |
| `c_lib/kite_T1a.c`, `vertex_T1b.c`, `ghost_G[abc].c` | C+OpenMP single-call implementations |
| `c_lib/kite_T1a_chunked.c`, `vertex_T1b_chunked.c` | Chunked variants for N≥12 batch execution (bash-tool-timeout-resilient) |
| `c_topology_wrapper.py` | Python wrapper dispatching numpy or C per topology |
| `A5_OI_p_extrapolation.py` | p²→0 extrapolation (λ=1,2,3) at fixed N |
| `n12_driver.py` | Persistent-state task-graph runner. Survives bash-tool timeouts and container restarts. Reusable architecture for any future long-running N-scan. |

### Reproducing the strict-2-loop check

```bash
# Single N (e.g., N=10), single λ — fast smoke test:
python3 c_topology_wrapper.py  # smoke test
python3 -c "from A5_OI_p_extrapolation import run_N_scan; run_N_scan(N_list=[6,8,10], m_reg=0.2, m_f=0.05)"

# N=12 via persistent-state driver (~150 minutes wall-clock, survives interruption):
python3 n12_driver.py 99999  # drive to completion
python3 n12_driver.py status  # check progress
python3 n12_driver.py aggregate  # finalize when done
```

## Notes on the paper's text-vs-code convention

The paper's text (SM.md line 564) and code (`oi_lattice_code/gauge/two_loop_vp.py`)
define `Π_s` with different formulas:

- **Text**: `Π_s = ∫[cos²/D − cos²·sin²/D²]` → converges to 0.308
- **Code**: `Pi_1 = V2/D²` → gives ~40 at N=16, m=0.05

The calculation in `reproduce_AB.py` follows the TEXT convention (matching 1/α_0 = 23.25).
The code's `Pi_1` is internally used as `D_gauge = 1/(p²·Pi_1)` but
does NOT equal the Π_s that appears in 1/α_0 = 24π·Π_s.

The prior `two_loop_vp.py` "$\delta_0^{(2L)} = 8.0 \pm 2$" result (computed in the
`Pi_1` convention) has been superseded. The δ₀ calculation has since been rebuilt
from first principles in the TEXT convention (`Π_s`, with the conversion
`δ_0 = (1/α_0)·(δΠ_s^{(2L)}/Π_s)` tied to `1/α_0 = 24π·Π_s`) in
`../c2_strict_2loop/`. The rebuilt result: the dominant scalar-bubble piece falls
as `1/N^{3.09}` and vanishes in the continuum limit, so strict 2-loop lattice PT
does **not** reproduce the empirical `δ_0 ≈ 10`, which is accordingly treated as
empirical input fixed by the U(1) row. See SM.md §6.2 for the current statement.

## Dependencies

- Python 3.8+
- NumPy
- C compiler (gcc with OpenMP) for chunked binaries in `c_lib/`. Optional:
  the calculation can run in pure numpy at lower N (≤ 8) without compilation.

## Supporting code for §6.2.1 systematics

- **`tadpole_wilson_v4g.py`**, **`reproduce_AB_with_wilson_tadpole.py`** — selected Wilson-action $V_{4g}$ implementation and driver. Its extrapolated shift is conditional on that implementation and leading power; SM §6.2.1 records the verified per-topology cosine placement and the pending full shift in the present normalization.
- **`bubble_with_F3.py`** — Propagation of the $F^3$ Wilson coefficient correction through the bubble (informs the ±1.5% systematic bound in SM §6.2.1).
