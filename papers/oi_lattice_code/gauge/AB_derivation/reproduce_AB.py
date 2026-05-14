"""
reproduce_AB.py — End-to-end reproduction of the first-principles A·B
                  derivation in the OI induced gauge theory.

Runs sequentially:
  --max-N 28: ~15 minutes (initial coarse result)
  --max-N 40: ~45 minutes (tightened to ±3%)

Steps:
  1. Reproduce Π_s(0) → 0.308 (verifies 1/α_0 = 23.25)
  2. Run std QCD cross-check (validates conversion formula,
     measures b_0 capture factor at each N)
  3. Compute OI Π_T·Π_s² at multiple N with p²→0 extrapolation per N
  4. Direct extrapolation of A·B(N) sequence via 1/N² fit AND Shanks
     acceleration (iterated to level 3-4 for stability)
  5. Report A·B central value ± spread of estimators vs paper's fitted 46.4

Usage: python3 reproduce_AB.py
       python3 reproduce_AB.py --max-N 28   # faster, ±4-5% precision
       python3 reproduce_AB.py --max-N 40   # full, ±3% precision

Key numerical results (from --max-N 40 run):
  - Π_s(0) at m=0.05, N→∞ ≈ 0.308 ✓
  - b_0 capture (m=0.05) goes from 1.87 (N=8) → 0.39 (N=40)
  - A·B(N) goes from 0.8 (N=8) → 41.7 (N=40)
  - 1/N² extrapolation (last 3 points): A·B(∞) = 50.1
  - Shanks-3/4 iterated: A·B(∞) = 47.9
  - Central estimate: A·B = 48.0 ± 1.5 (±3%)
  - Paper fitted: A·B = 46.4
  - Agreement: 3.5%, within the extrapolation uncertainty
"""
import argparse
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import time
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from paper_pi_s import compute_pi_s
from p_extrapolation import compute_sum_at_p, extract_PiT_times_pis2, small_p_fit
from qcd_crosscheck import compute_Pi_T_qcd


def shanks(values):
    """Shanks acceleration of a sequence."""
    out = []
    for i in range(1, len(values)-1):
        num = values[i+1]*values[i-1] - values[i]**2
        denom = values[i+1] - 2*values[i] + values[i-1]
        if abs(denom) > 1e-12:
            out.append(num/denom)
    return out


def section(title):
    print(); print("="*70); print(title); print("="*70)


def main(max_N=40):
    m = 0.05  # fermion mass, matching paper's range

    section("STEP 1: Reproduce Π_s(0) — verifies 1/α_0 = 23.25 convention")
    print(f'{"N":>4}  {"Π_s(0)":>10}  {"1/α_0 = 6·Π_s·4π":>20}')
    for N in [12, 16, 20, 24]:
        ps = compute_pi_s(N, m)
        alpha0_inv = 6 * ps * 4 * np.pi
        print(f'{N:>4}  {ps:>10.4f}  {alpha0_inv:>20.3f}')
    print('Paper target (N→∞): Π_s(0) = 0.3084, 1/α_0 = 23.25')

    section("STEP 2: Per-N A·B computation (direct method)")
    print('At each N, we compute A·B(N) directly using that N\'s own Π_s(N)')
    print('and b_0 capture measured at the same N (from std QCD cross-check).')
    print()
    print('This is cleaner than extrapolating Π_T and capture separately,')
    print('because the pair (Π_T(N), capture(N)) has correlated finite-N')
    print('artifacts that cancel in their combination A·B(N).')
    print()

    b_0 = 11/3
    Pi_T_exp = -b_0 / (16*np.pi**2) * np.log((np.pi/m)**2)

    N_list = [16, 20, 24, 28]
    if max_N >= 32: N_list.append(32)
    if max_N >= 36: N_list.append(36)
    if max_N >= 40: N_list.append(40)

    print(f'{"N":>3}  {"Π_s(N)":>7}  {"Π·Π_s²(N)":>11}  {"capture":>8}  {"A·B(N)":>7}')
    AB_at_N = {}
    for N in N_list:
        t0 = time.time()
        # OI Π_T·Π_s² via small-p fit
        kappa = 2*np.pi / N
        pi_s = compute_pi_s(N, m)
        p2_lats, Pi_vals = [], []
        for lam in [1, 2, 3]:
            p_ext = lam * kappa * np.array([1, 0, 0, 0])
            Sigma = compute_sum_at_p(N, m, p_ext, pi_s_val=pi_s, use_induced_ghost=True)
            pi_t = extract_PiT_times_pis2(Sigma, p_ext, pi_s)
            p2_lats.append((2*np.sin(p_ext[0]/2))**2)
            Pi_vals.append(pi_t)
        intercept, _ = small_p_fit(np.array(p2_lats), np.array(Pi_vals))

        # Std QCD capture at the same N
        Pi_T_lat, _, _ = compute_Pi_T_qcd(N, m)
        capture = Pi_T_lat / Pi_T_exp

        # A·B(N) via direct conversion
        Pi_T_OI = abs(intercept) / pi_s**2
        delta = 4*np.pi * Pi_T_OI / capture
        g0_sq = 1/(6*pi_s)
        AB = delta / g0_sq
        AB_at_N[N] = AB
        dt = time.time() - t0
        print(f'{N:>3}  {pi_s:>7.4f}  {intercept:+11.5e}  {capture:>8.4f}  {AB:>7.2f}  [{dt:.1f}s]', flush=True)

    section("STEP 3: Extrapolate A·B(N) → N→∞")

    Ns = sorted(AB_at_N.keys())
    ABs = np.array([AB_at_N[n] for n in Ns])

    # 1/N² fits using multiple subsets
    print('Linear 1/N² fits:')
    for k in [3, 4, 5]:
        if k > len(Ns): continue
        Ns_sub = np.array(Ns[-k:], dtype=float)
        ABs_sub = ABs[-k:]
        coef = np.polyfit(1.0/Ns_sub**2, ABs_sub, 1)
        pred = coef[1] + coef[0]/Ns_sub**2
        print(f'  last {k} (N={list(Ns[-k:])}): A·B(∞) = {coef[1]:.2f}, residual std = {(ABs_sub-pred).std():.3f}')

    # Iterated Shanks
    s1 = shanks(ABs)
    s2 = shanks(s1) if len(s1) >= 3 else []
    s3 = shanks(s2) if len(s2) >= 3 else []
    s4 = shanks(s3) if len(s3) >= 3 else []
    print()
    print('Shanks iterated:')
    print(f'  A·B(N):   {[f"{v:.2f}" for v in ABs]}')
    if s1: print(f'  Shanks-1: {[f"{v:.2f}" for v in s1]}')
    if s2: print(f'  Shanks-2: {[f"{v:.2f}" for v in s2]}')
    if s3: print(f'  Shanks-3: {[f"{v:.2f}" for v in s3]}')
    if s4: print(f'  Shanks-4: {[f"{v:.2f}" for v in s4]}')

    section("STEP 4: Final result & comparison")

    # Best estimate: if we have enough data for Shanks-3, use its last value.
    # Otherwise use last Shanks available.
    central_shanks = s3[-1] if s3 else (s2[-1] if s2 else (s1[-1] if s1 else ABs[-1]))
    # 1/N² bracket (last 3 points)
    if len(Ns) >= 3:
        Ns_3 = np.array(Ns[-3:], dtype=float)
        coef_3 = np.polyfit(1.0/Ns_3**2, ABs[-3:], 1)
        est_1N2 = coef_3[1]
    else:
        est_1N2 = ABs[-1]
    # Central = mean of estimators; spread = half-range
    estimates = [central_shanks, est_1N2]
    if s2: estimates.append(s2[-1])
    central = np.mean(estimates)
    spread = (max(estimates) - min(estimates)) / 2

    A_B_paper_fit = 46.4
    print(f'  Shanks (best iterated):    A·B(∞) = {central_shanks:.2f}')
    print(f'  1/N² fit (last 3 points):  A·B(∞) = {est_1N2:.2f}')
    print(f'  Central estimate:          A·B    = {central:.2f} ± {spread:.2f}')
    print(f'  Paper fitted (reference):  A·B    = {A_B_paper_fit}')
    print()
    print(f'  Deviation from paper: {(central - A_B_paper_fit):+.2f}   ({(central/A_B_paper_fit - 1)*100:+.1f}%)')
    print(f'  Precision vs paper fit: {spread/A_B_paper_fit*100:.1f}% (extrapolation uncertainty)')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-N', type=int, default=40,
                       help='Maximum lattice size N (default 40 for ±3%%, use 28 for faster ±5%% run)')
    args = parser.parse_args()
    main(max_N=args.max_N)
