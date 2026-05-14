"""
A5_OI_8_pis_sweep.py — Verify the sign-flip diagnosis.

Hypothesis: at fixed std-QCD per-topology values, the OI-rescaled
total Π_T·Π_s² flips sign as a function of Π_s alone. The crossover
should occur where T1b (n=5) and T1d (n=4) amplifications balance,
i.e., somewhere near Π_s ≈ 1.

Method: use the saved per-topology std Π_T values from N=12 λ=1
(n12_aggregate.json), sweep Π_s ∈ [0.2, 5], plot the OI total.
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')

N_INDUCED = {
    'T1a': 5, 'T1b': 5, 'T1c': 4, 'T1d': 4, 'T1e': 3,
    'G_a': 5, 'G_b': 5, 'G_c': 5, 'G_d': 4,
}

d = json.load(open(os.path.join(DATA, 'n12_aggregate.json')))
# Use lam=1 std-QCD values
std_per_top = d['per_lambda'][0]['per_top_PiT_std']
lam = d['per_lambda'][0]['lam']

print(f"=== Π_s sweep at fixed N=12 std-QCD values, λ={lam} ===\n")
print(f"{'Π_s':>8}  {'1/Π_s':>8}  {'T1a*1/Π_s^5':>14}  {'T1b*1/Π_s^5':>14}  "
      f"{'T1c*1/Π_s^4':>14}  {'T1d*1/Π_s^4':>14}  {'tot':>13}  "
      f"{'tot·Π_s²':>13}")
print("-" * 110)

results = []
for pi_s in [5.0, 3.0, 2.0, 1.5, 1.2, 1.0, 0.85, 0.70, 0.607, 0.50, 0.40, 0.31, 0.25]:
    inv_pi_s = 1.0 / pi_s
    contribs = {}
    for top, std in std_per_top.items():
        contribs[top] = std * inv_pi_s ** N_INDUCED[top]
    total_OI = sum(contribs.values())
    total_OI_times_pis2 = total_OI * pi_s ** 2
    results.append((pi_s, total_OI_times_pis2))
    print(f"  {pi_s:>6.3f}  {inv_pi_s:>8.4f}  "
          f"{contribs['T1a']:>+14.4e}  {contribs['T1b']:>+14.4e}  "
          f"{contribs['T1c']:>+14.4e}  {contribs['T1d']:>+14.4e}  "
          f"{total_OI:>+13.4e}  {total_OI_times_pis2:>+13.4e}")
print()

# Find where total_OI_times_pis2 crosses zero (linear interp between bracketing points)
crossings = []
for i in range(len(results) - 1):
    pi_s1, t1 = results[i]; pi_s2, t2 = results[i+1]
    if t1 * t2 < 0:
        # linear interp
        f = -t1 / (t2 - t1)
        pi_s_cross = pi_s1 + f * (pi_s2 - pi_s1)
        crossings.append(pi_s_cross)

print(f"Sign-flip Π_s value(s) (lam=1, N=12 std data): {crossings}")
