"""
A5_OI_6_iterated_subtraction.py — Iterated-1-loop subtraction prescription.

Geometric-series expansion of a dressed propagator gives
    D_full = D_0 [1 + g² Σ_1L + g⁴(Σ_2L + Σ_1L²) + ...]
so the (g²·C_2)² coefficient in δ(1/α) extracted from the full propagator
contains both the genuine 2-loop 1PI piece and the iterated 1-loop piece
[Σ_1L]². To compare against the log-resum prediction
    A·ln(1 + B·g²·C_2) = A·B·(g²·C_2) - (A·B²/2)·(g²·C_2)² + ...
the iterated piece [Σ_1L]² must be subtracted.

Candidate prescription:
    c_2_subtracted(N) = c_2_raw(N) - [intercept_LO(N)]²
with structural factor 1.0. The intercept_LO(N) used is the std-QCD-equivalent
1-loop bubble + ghost result (which equals Π_T^(1L)_OI · Π_s² by the
induced-propagator identity at LO).
"""
import json
import numpy as np
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from qcd_crosscheck import bubble_standard_qcd, ghost_standard_qcd, compute_Pi_T_qcd

C_2_TARGET = -128.0
B0 = 11.0 / 3.0


def capture_at_N(N, m_reg):
    """Compute std-QCD capture(N, m_reg) at lambda=1 for any N."""
    Pi_T_lat, _, _ = compute_Pi_T_qcd(N, m_reg)
    Pi_T_exp = -B0 / (16 * np.pi ** 2) * np.log(np.pi ** 2 / m_reg ** 2)
    return Pi_T_lat / Pi_T_exp


def compute_Pi_T_std_at_lambda(N, m_reg, lam):
    """Compute std-QCD Π_T at p_ext = lam·κ·ê_0 for a given (N, m_reg, lam)."""
    kappa = 2 * np.pi / N
    p_ext = lam * kappa * np.array([1.0, 0.0, 0.0, 0.0])
    Sigma_b = bubble_standard_qcd(N, p_ext, m_reg=m_reg)
    Sigma_g = ghost_standard_qcd(N, p_ext, m_reg=m_reg)
    Sigma = Sigma_b + Sigma_g
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2)) ** 2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    Pi_T_b = (Sigma_b[1, 1] - Sigma_b[0, 0]) / p2_lat
    Pi_T_g = (Sigma_g[1, 1] - Sigma_g[0, 0]) / p2_lat
    return Pi_T, Pi_T_b, Pi_T_g, p2_lat


def lo_intercept_at_N(N, m_reg, lambdas=(1, 2, 3)):
    """LO substratum intercept (per Π_T·Π_s² convention).

    By the induced-propagator identity Π_T_OI·Π_s² = Π_T^std for the
    1-loop bubble (ghost handled separately as note in module docstring).

    Returns dict with extrapolated intercept and per-lambda data.
    """
    p2_lats = []
    Pi_T_vals = []
    per_lam = []
    for lam in lambdas:
        Pi_T, Pi_T_b, Pi_T_g, p2 = compute_Pi_T_std_at_lambda(N, m_reg, lam)
        p2_lats.append(p2)
        Pi_T_vals.append(Pi_T)
        per_lam.append({'lam': lam, 'p2_lat': p2,
                        'Pi_T': Pi_T, 'Pi_T_b': Pi_T_b, 'Pi_T_g': Pi_T_g})
    p2_arr = np.array(p2_lats)
    Pi_arr = np.array(Pi_T_vals)
    coef = np.polyfit(p2_arr, Pi_arr, 1)
    intercept_LO = float(coef[1])
    slope_LO = float(coef[0])
    return {
        'intercept_LO': intercept_LO,
        'slope_LO': slope_LO,
        'per_lam': per_lam,
    }


def main():
    print("=" * 78)
    print("Iterated-1-loop subtraction candidate")
    print("=" * 78)
    print()

    seq_path = os.path.join(DATA, 'c2_N_sequence.json')
    with open(seq_path) as f:
        seq = json.load(f)
    Ns = sorted(int(k) for k in seq.keys())

    cap_path = os.path.join(DATA, 'c2_N_capture_corrected.json')
    with open(cap_path) as f:
        cap_data = json.load(f)

    m_reg = 0.2
    print(f"Computing LO intercept_LO(N) = Π_T^(std)(N, m_reg={m_reg}) "
          f"with p²→0 extrapolation (lambda=1,2,3):")
    print()
    print(f"{'N':>4}  {'λ=1 Π_T':>11}  {'λ=2 Π_T':>11}  {'λ=3 Π_T':>11}  "
          f"{'intercept':>11}  {'[int]²':>11}")
    print("-" * 78)
    lo_data = {}
    for N in Ns:
        t0 = time.time()
        result = lo_intercept_at_N(N, m_reg)
        dt = time.time() - t0
        lo_data[N] = result
        per_lam = result['per_lam']
        Pi1, Pi2, Pi3 = per_lam[0]['Pi_T'], per_lam[1]['Pi_T'], per_lam[2]['Pi_T']
        intercept = result['intercept_LO']
        print(f"{N:>4}  {Pi1:+11.4e}  {Pi2:+11.4e}  {Pi3:+11.4e}  "
              f"{intercept:+11.4e}  {intercept**2:+11.4e}")
    print()

    print("Apply candidate subtraction:  c_2_sub(N) = c_2_raw(N) - [intercept_LO(N)]²")
    print()
    print(f"{'N':>4}  {'c_2 raw':>13}  {'[LO]²':>13}  {'c_2 - [LO]²':>13}  "
          f"{'capture':>8}  {'÷capture²':>13}  {'/(-128)':>10}")
    print("-" * 95)
    sub = {}
    sub_div_cap2 = {}
    for N in Ns:
        c2_raw = seq[str(N)]['intercept']
        intercept_LO_sq = lo_data[N]['intercept_LO'] ** 2
        c2_sub = c2_raw - intercept_LO_sq
        if str(N) in cap_data['capture_per_N']:
            cap = cap_data['capture_per_N'][str(N)]
        else:
            cap = capture_at_N(N, m_reg)
        c2_sub_cap2 = c2_sub / cap ** 2
        sub[N] = c2_sub
        sub_div_cap2[N] = c2_sub_cap2
        ratio = c2_sub_cap2 / C_2_TARGET
        print(f"{N:>4}  {c2_raw:+13.5e}  {intercept_LO_sq:+13.5e}  "
              f"{c2_sub:+13.5e}  {cap:>8.4f}  {c2_sub_cap2:+13.5e}  {ratio:+10.4e}")
    print()

    Ns_arr = np.array(Ns, dtype=float)
    print("1/N² extrapolations (3 points; not enough for Shanks-2 yet):")
    print()
    versions = [
        ('c_2 raw',                np.array([seq[str(N)]['intercept'] for N in Ns])),
        ('c_2 - [LO]²',            np.array([sub[N] for N in Ns])),
        ('c_2 / cap²',             np.array([cap_data['c2_div_capture_squared'][str(N)] for N in Ns])),
        ('(c_2 - [LO]²) / cap²',   np.array([sub_div_cap2[N] for N in Ns])),
    ]
    for label, vals in versions:
        coef = np.polyfit(1.0 / Ns_arr ** 2, vals, 1)
        ratio = coef[1] / C_2_TARGET
        print(f"  {label:<24}: c_2(∞) ≈ {coef[1]:+.5e}   "
              f"ratio to -128: {ratio:+.4e}")
    print()

    # Save
    out = {
        'm_reg': m_reg,
        'lambdas_used': [1, 2, 3],
        'intercept_LO_per_N':       {str(N): lo_data[N]['intercept_LO'] for N in Ns},
        'slope_LO_per_N':           {str(N): lo_data[N]['slope_LO']     for N in Ns},
        'intercept_LO_squared':     {str(N): lo_data[N]['intercept_LO']**2 for N in Ns},
        'c2_raw':                   {str(N): seq[str(N)]['intercept']   for N in Ns},
        'c2_subtracted':            {str(N): sub[N]                     for N in Ns},
        'c2_subtracted_div_cap2':   {str(N): sub_div_cap2[N]             for N in Ns},
    }
    out_path = os.path.join(DATA, 'c2_N_iterated_subtraction.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
