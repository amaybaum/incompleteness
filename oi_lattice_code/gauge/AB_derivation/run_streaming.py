"""
Streaming version of run_one.py — uses streaming_bubble + streaming_ghost +
streaming_qcd to compute A·B at large N within memory constraints.
"""
import time, sys, json, os
sys.path.insert(0, '.')
from paper_pi_s import compute_pi_s
from p_extrapolation import extract_PiT_times_pis2, small_p_fit
from streaming_bubble import compute_bubble_at_p_streaming
from streaming_ghost import compute_ghost_sigma_streaming
from streaming_qcd import compute_Pi_T_qcd_streaming
import numpy as np

m = 0.05
b_0 = 11/3
Pi_T_exp = -b_0 / (16*np.pi**2) * np.log((np.pi/m)**2)

RESULTS_FILE = "ab_results.json"
if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE) as f:
        results = json.load(f)
    print(f"Loaded existing results: {sorted(int(k) for k in results.keys())}", flush=True)
else:
    results = {}


def run_one_N_streaming(N, m=0.05, batch_size=None):
    t0 = time.time()
    kappa = 2*np.pi / N
    pi_s = compute_pi_s(N, m)
    p2_lats, Pi_vals = [], []
    for lam in [1, 2, 3]:
        p_ext = lam * kappa * np.array([1, 0, 0, 0])
        # OI bubble + ghost (induced)
        Sig_bub, _ = compute_bubble_at_p_streaming(N, m, p_ext, pi_s_val=pi_s, batch_size=batch_size)
        Sig_gh = compute_ghost_sigma_streaming(N, p_ext, use_induced=True, pi_s_val=pi_s, m=m, batch_size=batch_size)
        Sigma = Sig_bub + Sig_gh
        pi_t = extract_PiT_times_pis2(Sigma, p_ext, pi_s)
        p2_lats.append((2*np.sin(p_ext[0]/2))**2)
        Pi_vals.append(pi_t)
    intercept, _ = small_p_fit(np.array(p2_lats), np.array(Pi_vals))
    
    # Std QCD capture (streaming)
    Pi_T_lat, _, _ = compute_Pi_T_qcd_streaming(N, m, batch_size=batch_size)
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


if len(sys.argv) > 1:
    Ns_to_run = [int(x) for x in sys.argv[1:]]
else:
    Ns_to_run = [44]

# At N=44, batch_size=20000 gives peak memory ~80MB which is safe
# At N=48, use batch_size=15000
default_batch = {44: 20000, 48: 15000}

print(f"\nRunning N values (streaming): {Ns_to_run}")
for N in Ns_to_run:
    if str(N) in results:
        r = results[str(N)]
        print(f"N={N}: AB={r['AB']:.3f} (cached, t={r['time_sec']:.1f}s)", flush=True)
        continue
    bs = default_batch.get(N, 30000)
    print(f"N={N}: starting (batch_size={bs})...", flush=True)
    r = run_one_N_streaming(N, m, batch_size=bs)
    results[str(N)] = r
    print(f"N={N}: AB={r['AB']:.3f}, t={r['time_sec']:.1f}s", flush=True)
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=2)

print(f"Saved to {RESULTS_FILE}")
