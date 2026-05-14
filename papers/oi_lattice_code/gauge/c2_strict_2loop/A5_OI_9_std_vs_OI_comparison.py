"""
A5_OI_9_std_vs_OI_comparison.py — Compute the std-QCD (no Π_s rescaling)
2-loop intercept at each N alongside the OI rescaled version.

The std-QCD result is the sum of all 9 topologies' Π_T_std without any
1/Π_s^n rescaling, then p²→0 extrapolated. This quantity is Π_s-independent
by construction — it's the bare 2-loop self-energy in standard QCD at the
same lattice with the same IR regulator.

The OI rescaled version multiplies each topology by 1/Π_s^n_induced before
summing, then × Π_s² overall.

For N=12 the per-topology breakdown is loaded from data/n12_aggregate.json;
for N=6,8,10 it is recomputed via the C wrappers and numpy O(N⁴) topologies
(<90s per λ at N≤10).
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

from paper_pi_s import compute_pi_s
from c_topology_wrapper import compute_all_sigmas_at_p_C

N_INDUCED = {
    'T1a': 5, 'T1b': 5, 'T1c': 4, 'T1d': 4, 'T1e': 3,
    'G_a': 5, 'G_b': 5, 'G_c': 5, 'G_d': 4,
}

m_reg = 0.2
m_f = 0.05


def piT(sigma, p_ext):
    p2 = (2 * np.sin(p_ext[0] / 2)) ** 2
    return (sigma[1, 1] - sigma[0, 0]) / p2


def per_top_at_N(N, lambdas=(1, 2, 3)):
    """Return list of dicts per λ with {'pi_T_std': {top: val}, 'pi_T_OI_total_times_pis2': val}."""
    pi_s = compute_pi_s(N, m_f)
    inv_pi_s = 1.0 / pi_s
    results = []
    for lam in lambdas:
        kappa = 2 * np.pi / N
        p_ext = np.array([lam * kappa, 0.0, 0.0, 0.0])
        sigmas, _ = compute_all_sigmas_at_p_C(N, p_ext, m_reg, verbose=False)
        per_top_std = {}
        for k, sigma in sigmas.items():
            per_top_std[k] = float(piT(sigma, p_ext))
        std_total = sum(per_top_std.values())
        OI_total = sum(per_top_std[k] * inv_pi_s ** N_INDUCED[k] for k in per_top_std)
        results.append({
            'lam': lam,
            'p2_lat': float((2 * np.sin(p_ext[0] / 2)) ** 2),
            'pi_T_std_per_top': per_top_std,
            'pi_T_std_total': float(std_total),
            'pi_T_OI_total': float(OI_total),
            'pi_T_OI_total_times_pis2': float(OI_total * pi_s ** 2),
        })
    return pi_s, results


def small_p_intercept(p2s, vals):
    """Linear fit val(p²) = a + b·p², return a."""
    coef = np.polyfit(np.array(p2s), np.array(vals), 1)
    return float(coef[1]), float(coef[0])


def main():
    # For N=12, just load from n12_aggregate.json
    n12 = json.load(open(os.path.join(DATA, 'n12_aggregate.json')))

    # Build all-N data
    all_data = {}

    # N=12 from saved
    all_data[12] = {
        'pi_s': n12['pi_s'],
        'per_lam': [
            {
                'lam': L['lam'],
                'p2_lat': L['p2_lat'],
                'pi_T_std_per_top': L['per_top_PiT_std'],
                'pi_T_std_total': sum(L['per_top_PiT_std'].values()),
                'pi_T_OI_total': sum(L['per_top_OI_contrib'].values()),
                'pi_T_OI_total_times_pis2': L['Pi_T_PiS2'],
            } for L in n12['per_lambda']
        ]
    }

    # N=6, 8, 10 by recomputation
    for N in [6, 8, 10]:
        print(f"Computing per-topology breakdown at N={N}...", flush=True)
        t0 = time.time()
        pi_s, per_lam = per_top_at_N(N)
        print(f"  done in {time.time()-t0:.1f}s")
        all_data[N] = {'pi_s': pi_s, 'per_lam': per_lam}

    # Now extract intercepts via p²→0 fit on each version
    print()
    print("=" * 90)
    print("Comparison of std-QCD vs OI-rescaled 2-loop intercepts at each N")
    print("=" * 90)
    print()
    print(f"{'N':>3} {'Π_s':>8} {'std c_2':>11} {'OI c_2 (× Π_s²)':>17}  {'std-OI ratio':>13}")
    print("-" * 60)

    for N in sorted(all_data.keys()):
        d = all_data[N]
        p2s_std = [L['p2_lat'] for L in d['per_lam']]
        std_vals = [L['pi_T_std_total'] for L in d['per_lam']]
        OI_vals = [L['pi_T_OI_total_times_pis2'] for L in d['per_lam']]
        std_intercept, _ = small_p_intercept(p2s_std, std_vals)
        OI_intercept, _ = small_p_intercept(p2s_std, OI_vals)
        ratio = std_intercept / OI_intercept if OI_intercept != 0 else float('nan')
        print(f" {N:>2} {d['pi_s']:>8.4f}  {std_intercept:+11.5e}  "
              f"{OI_intercept:+17.5e}  {ratio:>13.3f}")
    print()

    # Save
    out_path = os.path.join(DATA, 'std_vs_OI_per_N.json')
    summary = {N: {
        'pi_s': all_data[N]['pi_s'],
        'std_intercept': small_p_intercept(
            [L['p2_lat'] for L in all_data[N]['per_lam']],
            [L['pi_T_std_total'] for L in all_data[N]['per_lam']]
        )[0],
        'OI_intercept_times_pis2': small_p_intercept(
            [L['p2_lat'] for L in all_data[N]['per_lam']],
            [L['pi_T_OI_total_times_pis2'] for L in all_data[N]['per_lam']]
        )[0],
        'per_lam': all_data[N]['per_lam'],
    } for N in sorted(all_data.keys())}
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
