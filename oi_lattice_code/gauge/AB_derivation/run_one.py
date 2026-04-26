"""
Driver: compute A·B(N) at user-specified N values using the
non-streaming (full-tensor) implementation. Caches each completed N
to ab_results.json so partial progress survives interruption.

Suitable for N ≲ 40 within ordinary memory budgets; for larger N use
run_streaming.py.

Usage:
    python3 run_one.py 32 36 40      # specific N values
    python3 run_one.py               # default sequence
"""
import time, sys, json, os
sys.path.insert(0, '.')
from paper_pi_s import compute_pi_s
from p_extrapolation import compute_sum_at_p, extract_PiT_times_pis2, small_p_fit
from qcd_crosscheck import compute_Pi_T_qcd
import numpy as np

m = 0.05
b_0 = 11/3
Pi_T_exp = -b_0 / (16*np.pi**2) * np.log((np.pi/m)**2)

# Persistent results store (so partial results survive interruption)
RESULTS_FILE = "ab_results.json"
if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE) as f:
        results = json.load(f)
    print(f"Loaded existing results: {sorted(int(k) for k in results.keys())}", flush=True)
else:
    results = {}


def run_one_N(N, m=0.05):
    t0 = time.time()
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
    Pi_T_lat, _, _ = compute_Pi_T_qcd(N, m)
    capture = Pi_T_lat / Pi_T_exp
    Pi_T_OI = abs(intercept) / pi_s**2
    delta = 4*np.pi * Pi_T_OI / capture
    g0_sq = 1/(6*pi_s)
    AB = delta / g0_sq
    dt = time.time() - t0
    return {
        "N": N, "m": m,
        "pi_s": float(pi_s),
        "intercept": float(intercept),
        "capture": float(capture),
        "AB": float(AB),
        "time_sec": float(dt),
    }


# Determine what N values to run based on argv (or default progression)
import sys
if len(sys.argv) > 1:
    Ns_to_run = [int(x) for x in sys.argv[1:]]
else:
    Ns_to_run = [32, 36, 40, 44, 48]

print(f"\nRunning N values: {Ns_to_run}")
print(f"{'N':>3} {'pi_s':>8} {'intercept':>14} {'capture':>10} {'A·B':>10} {'t(s)':>8}")
for N in Ns_to_run:
    if str(N) in results:
        r = results[str(N)]
        print(f"{r['N']:>3} {r['pi_s']:>8.4f} {r['intercept']:>+14.5e} {r['capture']:>10.4f} {r['AB']:>10.3f} {r['time_sec']:>8.1f} (cached)", flush=True)
        continue
    r = run_one_N(N, m)
    results[str(N)] = r
    print(f"{r['N']:>3} {r['pi_s']:>8.4f} {r['intercept']:>+14.5e} {r['capture']:>10.4f} {r['AB']:>10.3f} {r['time_sec']:>8.1f}", flush=True)
    # Save after every N so partial progress is preserved
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)

print(f"\nResults saved to {RESULTS_FILE}")
