"""
c_F3 F³ refinement: extract sensitivity dA·B / dc_F3 in continuum limit.

Sweeps c_F3 ∈ {-0.1, -0.034, 0, +0.034, +0.1} at N ∈ {16, 24, 32, 40, 48}
and extracts the slope of Π_T·Π_s² vs c_F3, then propagates the
±0.034 uncertainty in c_F3 (the conservative bound from the framework's
analytical estimate) to a systematic on A·B.

The README's current bound is ±1.5%; this session aims for ±0.5%.
"""
import time, json, os, sys
import numpy as np
import warnings
warnings.filterwarnings('ignore')

sys.path.insert(0, '.')
from paper_pi_s import compute_pi_s
from streaming_F3 import compute_PiT_Pi_s2_at_N_streaming
from streaming_qcd import compute_Pi_T_qcd_streaming


m = 0.05
b_0 = 11/3
Pi_T_exp = -b_0 / (16*np.pi**2) * np.log((np.pi/m)**2)

# Cache file
RESULTS_FILE = "f3_sweep_results.json"
if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE) as f:
        results = json.load(f)
    print(f"Loaded existing: {sorted(results.keys())}", flush=True)
else:
    results = {}

c_F3_values = [-0.1, -0.034, 0.0, +0.034, +0.1]
N_values = [16, 24, 32, 40, 48]

# Convert intercept (Π_T·Π_s²) to A·B at each (N, c_F3) using the same formula 
# as in run_streaming.py:
#   A·B(N) = 4π · |intercept|/Π_s² / capture / (1/(6·Π_s)) = 24π · |intercept| / (Π_s · capture)
# capture is c_F3-independent (it's from std QCD, not the OI bubble), so we 
# compute it once per N from session 11's cache or recompute with streaming_qcd.

def compute_AB(intercept, pi_s, capture):
    Pi_T_OI = abs(intercept) / pi_s**2
    delta = 4*np.pi * Pi_T_OI / capture
    g0_sq = 1/(6*pi_s)
    return delta / g0_sq


# Reuse session 11's capture values where available
ab_results_path = "ab_results.json"
ab_baseline = {}
if os.path.exists(ab_results_path):
    with open(ab_results_path) as f:
        ab = json.load(f)
    for k, v in ab.items():
        ab_baseline[int(k)] = v


# Run sweep
print("\n=== c_F3 sweep ===")
print(f"{'N':>3} {'c_F3':>8} {'PiT*Pi_s^2':>14} {'pi_s':>8} {'capture':>10} {'A·B':>9} {'t(s)':>7}")
for N in N_values:
    pi_s = compute_pi_s(N, m)
    if N in ab_baseline:
        capture = ab_baseline[N]['capture']
        cap_src = "cached"
    else:
        Pi_T_lat, _, _ = compute_Pi_T_qcd_streaming(N, m, batch_size=20000)
        capture = Pi_T_lat / Pi_T_exp
        cap_src = "fresh"
    
    for c_F3 in c_F3_values:
        key = f"{N}_{c_F3:+.3f}"
        if key in results:
            r = results[key]
            print(f"{r['N']:>3} {r['c_F3']:>+8.3f} {r['intercept']:>+14.6e} {r['pi_s']:>8.4f} {r['capture']:>10.4f} {r['AB']:>9.3f} {r['time_sec']:>7.1f} (cached)", flush=True)
            continue
        
        t0 = time.time()
        intercept = compute_PiT_Pi_s2_at_N_streaming(N, m, c_F3, pi_s, batch_size=20000)
        AB = compute_AB(intercept, pi_s, capture)
        dt = time.time() - t0
        results[key] = {
            "N": N, "c_F3": c_F3, "m": m,
            "pi_s": float(pi_s), "capture": float(capture),
            "intercept": float(intercept), "AB": float(AB),
            "time_sec": float(dt),
        }
        print(f"{N:>3} {c_F3:>+8.3f} {intercept:>+14.6e} {pi_s:>8.4f} {capture:>10.4f} {AB:>9.3f} {dt:>7.1f}", flush=True)
        with open(RESULTS_FILE, 'w') as f:
            json.dump(results, f, indent=2)

print(f"\nSaved to {RESULTS_FILE}")

# Analysis: at each N, extract dA·B / dc_F3 by linear fit to the 5-point sweep
print("\n=== dA·B / dc_F3 at each N (via linear fit) ===")
print(f"{'N':>3} {'A·B(0)':>9} {'dA·B/dc_F3':>13} {'A·B(c=-0.034)':>16} {'shift @ c=-0.034':>18}")
slopes = {}
for N in N_values:
    cs = []
    abs_ = []
    for c_F3 in c_F3_values:
        key = f"{N}_{c_F3:+.3f}"
        if key not in results: continue
        cs.append(c_F3)
        abs_.append(results[key]['AB'])
    cs = np.array(cs); abs_ = np.array(abs_)
    if len(cs) < 3: continue
    coef = np.polyfit(cs, abs_, 1)  # AB = slope * c_F3 + intercept
    AB0 = coef[1]
    slope = coef[0]
    shift_at_pm = abs(slope) * 0.034
    rel_shift = shift_at_pm / AB0 * 100
    slopes[N] = (slope, AB0)
    print(f"{N:>3} {AB0:>9.3f} {slope:>+13.4f} {AB0 + slope*(-0.034):>16.3f} {rel_shift:>+17.2f}%")

# Continuum extrapolation of dA·B / dc_F3
print("\n=== Extrapolation of dA·B/dc_F3 to N→∞ ===")
Ns_with_slopes = sorted(slopes.keys())
slope_vals = [slopes[N][0] for N in Ns_with_slopes]
print(f"  Sequence: {[f'{s:.3f}' for s in slope_vals]}")

# 1/N² fit
if len(Ns_with_slopes) >= 3:
    Ns_arr = np.array(Ns_with_slopes, dtype=float)
    slopes_arr = np.array(slope_vals)
    for k in [3, 4, 5]:
        if k > len(Ns_arr): continue
        coef = np.polyfit(1/Ns_arr[-k:]**2, slopes_arr[-k:], 1)
        print(f"  1/N² fit (last {k}): dA·B/dc_F3 (∞) = {coef[1]:.3f}")

# Continuum slope estimate
if len(Ns_with_slopes) >= 3:
    Ns_arr = np.array(Ns_with_slopes, dtype=float)
    slopes_arr = np.array(slope_vals)
    coef = np.polyfit(1/Ns_arr[-3:]**2, slopes_arr[-3:], 1)
    slope_inf = coef[1]
    print(f"\n  → Continuum slope: dA·B/dc_F3 ≈ {slope_inf:.3f}")
    
    # Continuum A·B baseline (Shanks-3 from session 11/12 was 47.5-48.0, with V_4g 48.9 ± 0.3)
    AB_central = 48.0  # paper's value
    # Conservative c_F3 bound from analytical: ±0.034
    c_F3_bound = 0.034
    delta_AB = abs(slope_inf) * c_F3_bound
    rel_systematic = delta_AB / AB_central * 100
    print(f"  c_F3 bound (analytical): ±{c_F3_bound}")
    print(f"  ΔA·B at c_F3 = ±{c_F3_bound}: ±{delta_AB:.3f}")
    print(f"  Relative systematic on A·B: ±{rel_systematic:.2f}%")
    print(f"\n  README's current systematic: ±1.5%")
    print(f"  Achieved this session:        ±{rel_systematic:.2f}%")
