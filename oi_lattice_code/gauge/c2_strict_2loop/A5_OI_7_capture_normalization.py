"""
A5_OI_7_capture_normalization.py — Apply std-QCD capture-factor correction
to the c_2(N) sequence.

The capture factor is the lattice's reproduction fraction of the textbook
1-loop log term:
    capture(N, m_reg) = Π_T_lat(N, m_reg) / Π_T_textbook(m_reg)
    Π_T_textbook = -(11/3)/(16π²) · log(π²/m_reg²)

LO uses A·B = 4π·|Π_T_OI|/capture / g₀² with g₀² = 1/(6·Π_s). For NLO,
two natural choices are tested:
  (a) c_2(N) / capture(N)    — one capture factor (LO-style)
  (b) c_2(N) / capture(N)²   — squared (one per loop integral)

Run conditions: m_reg = 0.2, m_f = 0.05, λ ∈ {1,2,3} for p-extrapolation.
"""
import json
import numpy as np
import os
import sys
import time

# Paths

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from qcd_crosscheck import compute_Pi_T_qcd

C_2_TARGET = -128.0  # per C_A² (with A·B = 48 ⇒ -A·B²/2 / C_A² = -128)
B0 = 11.0 / 3.0


def capture_at_N(N, m_reg):
    """Compute std-QCD capture(N, m_reg) at smallest lattice p (lambda=1).

    Returns:
      Pi_T_lat, Pi_T_exp, capture = Pi_T_lat / Pi_T_exp
    """
    Pi_T_lat, Pi_T_bub, Pi_T_gh = compute_Pi_T_qcd(N, m_reg)
    Pi_T_exp = -B0 / (16 * np.pi ** 2) * np.log(np.pi ** 2 / m_reg ** 2)
    capture = Pi_T_lat / Pi_T_exp
    return {
        'Pi_T_lat': Pi_T_lat,
        'Pi_T_bub': Pi_T_bub,
        'Pi_T_gh': Pi_T_gh,
        'Pi_T_exp': Pi_T_exp,
        'capture': capture,
    }


def main():
    print("=" * 78)
    print("Capture-factor normalization of c_2(N) sequence")
    print("=" * 78)
    print()
    print(f"Log-resum reference (NOT reachable at strict 2-loop in OI): "
          f"c_2 / C_A² = {C_2_TARGET}")
    print(f"  (= -A·B²/2 / C_A² with A·B = 48; per SM.md §6.2.1, the strict")
    print(f"   2-loop value is structurally suppressed and ≪ this reference)")
    print()

    # Load existing c_2(N) sequence
    seq_path = os.path.join(DATA, 'c2_N_sequence.json')
    with open(seq_path) as f:
        seq = json.load(f)
    Ns = sorted(int(k) for k in seq.keys())
    print(f"Loaded c_2(N) sequence from c2_N_sequence.json:  N = {Ns}")
    print()

    # Compute capture at each N at the same m_reg=0.2 used for c_2 extraction
    m_reg = 0.2
    print(f"Computing std-QCD capture(N, m_reg={m_reg}) at lambda=1 (smallest p):")
    print()
    print(f"{'N':>4}  {'Π_T_bub':>11}  {'Π_T_gh':>11}  {'Π_T_sum':>11}  "
          f"{'Π_T_exp':>10}  {'capture':>9}  {'time':>7}")
    print("-" * 78)
    captures = {}
    for N in Ns:
        t0 = time.time()
        result = capture_at_N(N, m_reg)
        dt = time.time() - t0
        captures[N] = result['capture']
        print(f"{N:>4}  {result['Pi_T_bub']:+11.4e}  {result['Pi_T_gh']:+11.4e}  "
              f"{result['Pi_T_lat']:+11.4e}  {result['Pi_T_exp']:+10.4e}  "
              f"{result['capture']:>9.4f}  {dt:>6.1f}s",
              flush=True)
    print()

    # Apply capture corrections
    print("Applying capture correction to c_2(N):")
    print()
    print(f"{'N':>4}  {'c_2(N) raw':>13}  {'capture':>8}  "
          f"{'÷capture':>13}  {'÷capture²':>13}  "
          f"{'/(-128) raw':>11}  {'/(-128) /cap²':>13}")
    print("-" * 90)
    raw = {}
    div_cap = {}
    div_cap2 = {}
    for N in Ns:
        c2_raw = seq[str(N)]['intercept']
        cap = captures[N]
        c2_a = c2_raw / cap
        c2_b = c2_raw / cap ** 2
        raw[N] = c2_raw
        div_cap[N] = c2_a
        div_cap2[N] = c2_b
        print(f"{N:>4}  {c2_raw:+13.5e}  {cap:>8.4f}  "
              f"{c2_a:+13.5e}  {c2_b:+13.5e}  "
              f"{c2_raw / C_2_TARGET:>11.4e}  {c2_b / C_2_TARGET:>13.4e}")
    print()

    # Naive 1/N² extrapolation of each version
    print("1/N² extrapolation (3 points, cautious — only 3 N values, no Shanks possible):")
    print()
    Ns_arr = np.array(Ns, dtype=float)
    for label, vals_dict in [('c_2 raw', raw), ('c_2 / capture', div_cap),
                              ('c_2 / capture²', div_cap2)]:
        vals = np.array([vals_dict[N] for N in Ns])
        coef = np.polyfit(1.0 / Ns_arr ** 2, vals, 1)
        ratio = coef[1] / C_2_TARGET
        print(f"  {label:<20}: c_2(∞) ≈ {coef[1]:+.5e}   "
              f"(slope in 1/N² = {coef[0]:+.4e},  ratio to -128: {ratio:+.4e})")
    print()

    # Save results
    out = {
        'm_reg': m_reg,
        'm_f_for_intercepts': 0.05,
        'capture_per_N': {str(N): captures[N] for N in Ns},
        'c2_raw': {str(N): raw[N] for N in Ns},
        'c2_div_capture': {str(N): div_cap[N] for N in Ns},
        'c2_div_capture_squared': {str(N): div_cap2[N] for N in Ns},
        'C_2_target_per_CA2': C_2_TARGET,
    }
    out_path = os.path.join(DATA, 'c2_N_capture_corrected.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
