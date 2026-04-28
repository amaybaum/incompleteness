# c2_strict_2loop/ — Strict 2-loop (C_2 g_0²)² coefficient in OI

NLO companion to `../AB_derivation/`. Computes the strict 2-loop 1PI
gauge self-energy in the OI induced theory via the 9-topology
decomposition (5 gluon + 4 ghost diagrams), with p²→0 extrapolation
and lattice sizes N=6,8,10,12.

## TL;DR

- **What this computes:** the strict-2-loop 1PI gauge self-energy in
  OI (9 topologies, p²→0 extrapolation).
- **What this confirms:** the structural-suppression claim of
  SM.md §6.2.1 line 633. The strict-2-loop (C_2·g_0²)² coefficient
  is small at all N, decreasing toward zero — quantitatively
  consistent with the paper's "≈ 0.2% of A·B" estimate for the
  C_A² ghost channel.
- **What this does NOT compute:** the log-resum-form coefficient
  c_2 = −A·B²/2 = −128. That coefficient cannot be obtained from
  strict 2-loop in OI by the framework's own structure: induced
  3- and 4-gluon vertices first appear at 3-loop, so the geometric
  series 1/(1−Σ) that builds up to the log cannot be assembled
  from 2-loop alone.

## Headline result

Per-N strict-2-loop sum (std-QCD-equivalent normalization, no
1/Π_s^n rescaling — see AB_derivation/README.md "Strict 2-loop
(C_2·g_0²)² check" for why this is the right quantity):

| N  | Π_s(m_f=0.05) | Σ_topologies Π_T_std (sum) |
|----|---------------|----------------------------|
|  6 | 5.226         | −0.274 |
|  8 | 1.853         | −0.101 |
| 10 | 0.935         | −0.061 |
| 12 | 0.607         | −0.044 |

Smooth, monotone-decreasing, consistent with structural suppression.
Compare to the C_A² ghost channel estimate of ~0.2% × A·B ≈ 0.1
cited in SM.md §6.2.1 — same order of magnitude, decreasing further
with N.

## Quick start

```bash
# Build C+OpenMP binaries (required for T1a, T1b, G_a, G_b, G_c)
make -C c_lib

# Smoke test (computes 9 Σ matrices at N=6, m_reg=0.2, ~30 sec)
python3 c_topology_wrapper.py

# Compute the std-QCD-equivalent sequence at all N (~10 min, N=10 bottleneck)
python3 A5_OI_9_std_vs_OI_comparison.py
```

The C binaries provide ~5-22× speedup over numpy for the five 1PI
topologies that need them. The other four (T1c-e, G_d) are O(N⁴) and
stay in pure numpy.

## File organization

### Topology implementations (the 9 1PI 2-loop diagrams)

| File | Topology | Loop type | Has C binary? |
|------|----------|-----------|----------------|
| `T1a_kite.py` | T1a kite | 2-loop with V_3g | Yes (chunked variant for N≥12) |
| `T1b_vertex_correction.py` | T1b vertex correction | 2-loop with V_3g | Yes (chunked variant for N≥12) |
| `T1c_V4g_bubble.py` | T1c V_4g bubble | bubble + V_4g | numpy O(N⁴) |
| `T1d_V4g_tadpole.py` | T1d V_4g tadpole | tadpole + V_4g | numpy O(N⁴) |
| `T1e_V4g_triple_line.py` | T1e V_4g triple line | triple + V_4g | numpy O(N⁴) |
| `G_a_ghost_square.py` | G_a ghost square | ghost loop | Yes |
| `G_b_ghost_vertex_correction.py` | G_b ghost vertex | ghost + V_3g | Yes |
| `G_c_ghost_triangle.py` | G_c ghost triangle | ghost triangle | Yes |
| `G_d_V4g_ghost_bubble.py` | G_d V_4g ghost | ghost + V_4g | numpy O(N⁴) |

All topologies are color C_A².

### Drivers and infrastructure

| File | Purpose |
|------|---------|
| `c_topology_wrapper.py` | Dispatches each topology to numpy or C binary |
| `A5_OI_p_extrapolation.py` | p²→0 extrapolation (λ=1,2,3) at fixed N |
| `A5_OI_p_extrapolation_C.py` | Same, optimized C-call path |
| `n12_driver.py` | Persistent-state task-graph runner. State per-task in `data/n12_state.json`. Survives interruption; resumes from saved state. |
| `validate_T1b_chunked.py` | Validates chunked T1b binary against unchunked at machine precision |

### Analysis scripts

| File | Role |
|------|------|
| `A5_OI_6_iterated_subtraction.py` | Iterated-1-loop subtraction prescription |
| `A5_OI_7_capture_normalization.py` | Capture-factor analysis |
| `A5_OI_8_pis_sweep.py` | Π_s sensitivity sweep at fixed N=12 std-QCD numbers |
| `A5_OI_9_std_vs_OI_comparison.py` | std-QCD-equivalent sum at all N |
| `A5_OI_10_first_principles_extraction.py` | NLO extraction prescription analysis |
| `A5_OI_substratum.py` | Substratum-side analysis driver |
| `A5_8_extract_b1.py` | Extract b_1 coefficient |

### C source files (in `c_lib/`)

| File | Topology | Variant |
|------|----------|---------|
| `kite_T1a.c` | T1a | single-call O(N⁸), O(N⁴) memory |
| `kite_T1a_chunked.c` | T1a | chunked variant for N≥12 |
| `vertex_T1b.c` | T1b | single-call |
| `vertex_T1b_chunked.c` | T1b | chunked variant for N≥12 |
| `ghost_Ga.c` | G_a | single-call |
| `ghost_Gb.c` | G_b | single-call |
| `ghost_Gc.c` | G_c | single-call |

The chunked binaries take `(chunk_idx, num_chunks)` arguments and
process only their assigned k_2 indices. Output partial Σ; caller
sums chunks then applies prefactors. Bit-equivalent to single-call
binaries (verified ≤ 1.7e-13).

### Data (in `data/`)

| File | Contents |
|------|----------|
| `c2_N_sequence.json` | c_2(N) sequence at N=6,8,10,12 |
| `n12_state.json` | Per-task results for the N=12 driver run (62 KB) |
| `n12_aggregate.json` | N=12 summary: per-λ totals, per-topology breakdown |
| `std_vs_OI_per_N.json` | std-QCD vs OI-rescaled comparison at all N |
| `c2_N_capture_corrected.json` | Capture-factor analysis output |
| `c2_N_iterated_subtraction.json` | Iterated subtraction analysis output |

## Path conventions

All Python files use this canonical path setup:

```python
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)
```

The directory is self-contained for compute but inherits the LO
infrastructure from `../AB_derivation/` for `paper_pi_s.py`,
`qcd_crosscheck.py`, `yang_mills_lattice.py`, `colors.py`,
`vertices.py`, etc.

## Conventions

- **m_reg = 0.2**: IR regulator on the gauge propagators.
- **m_f = 0.05**: fermion mass for Π_s computation (matches LO).
- **External momenta**: λ = 1, 2, 3 multiples of κ = 2π/N along the
  0-direction. Linear fit in p² for the p²→0 intercept.
- **Π_T extraction**: (Σ¹¹ − Σ⁰⁰) / p̂² for p along 0-direction.
- **Color**: stripped to per-C_A² coefficient.

## Reproducibility

- Python 3.8+, NumPy.
- gcc with OpenMP for the C+OpenMP binaries.
- All result files preserved in `data/` for direct comparison
  without re-running the calculation.
