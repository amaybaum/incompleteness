"""
reproduce_AB_with_wilson_tadpole.py — A·B driver INCLUDING the derived
Wilson V_4g tadpole contribution.

Extends reproduce_AB.py by adding the tadpole's Π_T·Π_s² contribution
(from session n's derivation, V4G_STEP_2.md) to the bubble+ghost sum
before the A·B extraction.

The addition is a single analytical piece:
    ΔΠ_T·Π_s² from Wilson tadpole = -(Π_s/4) · J(N),    J = ⟨cos(k_μ)/k̂²⟩

This is simply ADDED to the intercept (since both are p=0 values of
Π_T·Π_s²).

Runs N ∈ {16, 20, 24, 28, 32} by default (faster than max-N=40 run).
"""
import numpy as np
import time
import os
import sys
import warnings

warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from paper_pi_s import compute_pi_s
from p_extrapolation import compute_sum_at_p, extract_PiT_times_pis2, small_p_fit
from qcd_crosscheck import compute_Pi_T_qcd
from tadpole_wilson_v4g import compute_PiT_tad_wilson


def shanks(values):
    out = []
    for i in range(1, len(values)-1):
        num = values[i+1]*values[i-1] - values[i]**2
        denom = values[i+1] - 2*values[i] + values[i-1]
        if abs(denom) > 1e-12:
            out.append(num/denom)
    return out


def main(N_list=None):
    m = 0.05
    if N_list is None:
        N_list = [16, 20, 24, 28, 32]

    b_0 = 11/3
    Pi_T_exp = -b_0 / (16*np.pi**2) * np.log((np.pi/m)**2)

    print("=" * 74)
    print("Per-N A·B with Wilson tadpole (derived in session n)")
    print("=" * 74)
    print()
    print(f"{'N':>3}  {'Π_s':>7}  {'Π·Π_s²(b+g)':>12}  {'Π_tad':>11}  "
          f"{'Π_sum':>12}  {'capture':>8}  {'A·B(b+g)':>9}  {'A·B(tot)':>9}")

    ABs_bg = {}   # bubble + ghost only
    ABs_tot = {}  # bubble + ghost + Wilson tadpole

    for N in N_list:
        t0 = time.time()
        kappa = 2*np.pi / N
        pi_s = compute_pi_s(N, m)

        # Bubble + ghost intercept via small-p fit
        p2_lats, Pi_vals = [], []
        for lam in [1, 2, 3]:
            p_ext = lam * kappa * np.array([1, 0, 0, 0])
            Sigma = compute_sum_at_p(N, m, p_ext, pi_s_val=pi_s, use_induced_ghost=True)
            pi_t = extract_PiT_times_pis2(Sigma, p_ext, pi_s)
            p2_lats.append((2*np.sin(p_ext[0]/2))**2)
            Pi_vals.append(pi_t)
        intercept_bg, _ = small_p_fit(np.array(p2_lats), np.array(Pi_vals))

        # Wilson tadpole contribution (analytical)
        PiT_tad, J = compute_PiT_tad_wilson(N, m, pi_s_val=pi_s)
        intercept_tot = intercept_bg + PiT_tad

        # QCD capture
        Pi_T_lat, _, _ = compute_Pi_T_qcd(N, m)
        capture = Pi_T_lat / Pi_T_exp

        # A·B(N) via direct conversion, two versions
        def AB_from_intercept(intercept):
            Pi_T_OI = abs(intercept) / pi_s**2
            delta = 4*np.pi * Pi_T_OI / capture
            g0_sq = 1/(6*pi_s)
            return delta / g0_sq

        AB_bg = AB_from_intercept(intercept_bg)
        AB_tot = AB_from_intercept(intercept_tot)
        ABs_bg[N] = AB_bg
        ABs_tot[N] = AB_tot

        dt = time.time() - t0
        print(f"{N:>3}  {pi_s:>7.4f}  {intercept_bg:>+12.5e}  "
              f"{PiT_tad:>+11.5e}  {intercept_tot:>+12.5e}  "
              f"{capture:>8.4f}  {AB_bg:>9.2f}  {AB_tot:>9.2f}  [{dt:.0f}s]", flush=True)

    print()
    print("=" * 74)
    print("Extrapolation to N→∞ (bubble+ghost only vs +Wilson tadpole)")
    print("=" * 74)

    for label, ABs in [("bubble+ghost only", ABs_bg),
                        ("b+g + Wilson tadpole", ABs_tot)]:
        print(f"\n--- {label} ---")
        Ns = sorted(ABs.keys())
        arr = np.array([ABs[n] for n in Ns])

        # 1/N² fits for last 3, 4, 5 subsets
        for k in [3, 4, 5]:
            if k > len(Ns): continue
            Ns_sub = np.array(Ns[-k:], dtype=float)
            ABs_sub = arr[-k:]
            coef = np.polyfit(1.0/Ns_sub**2, ABs_sub, 1)
            pred = coef[1] + coef[0]/Ns_sub**2
            print(f"  last {k} (N={list(Ns[-k:])}): A·B(∞) = {coef[1]:.2f}, "
                  f"residual std = {(ABs_sub-pred).std():.3f}")

        # Shanks
        s1 = shanks(arr)
        s2 = shanks(s1) if len(s1) >= 3 else []
        s3 = shanks(s2) if len(s2) >= 3 else []
        print(f"  A·B(N):   {[f'{v:.2f}' for v in arr]}")
        if s1: print(f"  Shanks-1: {[f'{v:.2f}' for v in s1]}")
        if s2: print(f"  Shanks-2: {[f'{v:.2f}' for v in s2]}")
        if s3: print(f"  Shanks-3: {[f'{v:.2f}' for v in s3]}")

    # Compare
    print()
    print("=" * 74)
    print("Summary: impact of Wilson tadpole on A·B(∞)")
    print("=" * 74)

    # Use 1/N² fit of last 3 points as the canonical estimator
    Ns = sorted(ABs_tot.keys())
    def last3_fit(abs_dict):
        Ns3 = np.array(sorted(abs_dict.keys())[-3:], dtype=float)
        arr3 = np.array([abs_dict[int(n)] for n in Ns3])
        return np.polyfit(1.0/Ns3**2, arr3, 1)[1]

    bg_inf = last3_fit(ABs_bg)
    tot_inf = last3_fit(ABs_tot)
    print()
    print(f"  A·B(∞) without tadpole (bubble+ghost only):  {bg_inf:.2f}")
    print(f"  A·B(∞) WITH Wilson tadpole:                  {tot_inf:.2f}")
    print(f"  Shift from tadpole:  {tot_inf - bg_inf:+.2f}  ({(tot_inf/bg_inf - 1)*100:+.1f}%)")
    print(f"  Paper target:         {46.4}")
    print(f"  Paper reported:       48.0 ± 1.5 (±3%)")
    print()
    print("Status: session n derivation, cross-check vs Capitani 2.84 pending")


if __name__ == "__main__":
    main()
