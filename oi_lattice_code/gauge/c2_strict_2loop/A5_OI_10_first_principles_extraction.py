"""
A5_OI_10_first_principles_extraction.py — c_2 extraction prescription analysis.

LO extraction (reproduce_AB.py):
  δ(1/α) = 4π · |Π_T_OI| / capture
  g₀² = 1/(6·Π_s)
  A·B = δ / g₀² = 24π · intercept / (Π_s · capture)
where intercept = Π_T·Π_s². Π_s appears in the denominator at LO.

NLO extraction by analogy (squared coupling):
  c_2 · g₀⁴ = δ_NLO   (with C_2 = C_A = 3)
  c_2 / C_A² = (4π · |Π_T_NLO| / capture^k) · 36·Π_s² / 9
             = 16π · Π_s² · |Π_T_NLO| / capture^k

with capture^k = capture² (one factor per loop integral) the natural choice.
This script applies the prescription to the saved N=6,8,10,12 data.
"""
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')

# Load data
n12 = json.load(open(os.path.join(DATA, 'n12_aggregate.json')))
std_per_N = json.load(open(os.path.join(DATA, 'std_vs_OI_per_N.json')))

# Constants
B0 = 11.0/3.0
C_A = 3.0
A_B_target = 48.0
c2_target_per_CA2 = -A_B_target**2 / 2 / C_A**2  # = -128
print(f"Target c_2/C_A² = {c2_target_per_CA2}")
print()

# Reconstruct the LO extraction logic to be sure
print("="*78)
print("Sanity check: LO extraction via reproduce_AB.py logic")
print("="*78)
print()
print("At LO, A·B = 4π · |Π_T_OI| / capture / g_0² = 4π·|Π_T_OI|·6·Π_s / capture")
print("Π_T_OI(LO) = bubble_OI = Π_T_std (the 1/Π_s² rescaling cancels Π_s² normalization)")
print()
print("In reproduce_AB.py form:")
print("  intercept_LO_substratum = Π_T_OI · Π_s² = Π_T_std (the std-QCD bubble)")
print("  Π_T_OI = intercept / Π_s²")
print("  A·B = 4π · |intercept|/Π_s² / capture / (1/(6·Π_s))")
print("      = 24π · |intercept| / (Π_s · capture)")
print()
print("So at LO, the DIMENSIONAL Π_s power is +1 in the denominator.")
print()

# Apply same logic to NLO
print("="*78)
print("First-principles extraction of c_2 at NLO")
print("="*78)
print()
print("By analogy:")
print("  δ_NLO (g²·C)² coeff = 4π · |Π_T_NLO_OI_total| / capture^?  (capture? capture²?)")
print("  g₀⁴ = 1/(36 · Π_s²)")
print("  c_2 / C_A² = δ_NLO / g₀⁴ / C_A²")
print("            = 4π · |Π_T_NLO_OI| · 36 · Π_s² / (capture^? · 9)")
print("            = 16π · Π_s² · |Π_T_NLO_OI| / capture^?")
print()
print("If capture^? = capture² (one per loop integral): RIGHT in spirit but check.")
print("If capture^? = capture (just LO): also possible.")
print()

# Use saved data
print("Applying to all available data (N=6,8,10,12):")
print()
print(f"{'N':>3}  {'Π_s':>7}  {'cap':>7}  {'OI×Π_s²':>10}  {'×24π/(Π_s·cap)':>14}  "
      f"{'×144π·Π_s²/cap':>14}  {'×144π·Π_s²/cap²':>15}")
print(f"{'':>3}  {'':>7}  {'':>7}  {'':>10}  {'(LO-style)':>14}  "
      f"{'(NLO,cap¹)':>14}  {'(NLO,cap²)':>15}")
print("-" * 90)

# Get capture at each N (from saved n12 + std_vs_OI; for N=6,8,10 we need to add)
# Capture data is in c2_N_capture_corrected.json
cap_data = json.load(open(os.path.join(DATA, 'c2_N_capture_corrected.json')))
captures = {int(k): v for k, v in cap_data['capture_per_N'].items()}
captures[12] = n12['capture_lambda1']

for N in [6, 8, 10, 12]:
    pi_s = std_per_N[str(N)]['pi_s']
    cap = captures[N]
    OI = std_per_N[str(N)]['OI_intercept_times_pis2']

    # The "LO-style" extraction (this is what reproduce_AB does, but for the NLO sum):
    # If we treat OI×Π_s² the same way we treated the LO Π_T·Π_s², we get:
    LO_style = 24*np.pi * OI / (pi_s * cap)
    # But this is a 1-loop-style extraction (c_1 / C_A) applied to the 2-loop number,
    # so it's just the wrong dimension.

    # NLO with capture^1:
    NLO_cap1 = 144 * np.pi * pi_s**2 * OI / cap
    # NLO with capture^2:
    NLO_cap2 = 144 * np.pi * pi_s**2 * OI / cap**2

    print(f"{N:>3}  {pi_s:>7.4f}  {cap:>7.4f}  {OI:+10.4e}  "
          f"{LO_style:+14.4e}  {NLO_cap1:+14.4e}  {NLO_cap2:+14.4e}")
print()
print(f"Target c_2/C_A² = {c2_target_per_CA2}")
print()

# Now do the same starting from std-QCD only
print("="*78)
print("Same extraction starting from std-QCD-only intercept (no OI rescaling)")
print("="*78)
print()
print(f"{'N':>3}  {'Π_s':>7}  {'cap':>7}  {'std_int':>11}  "
      f"{'×144π·Π_s²/cap²':>16}  {'×144π·1/cap²':>14}")
print("-" * 80)

for N in [6, 8, 10, 12]:
    pi_s = std_per_N[str(N)]['pi_s']
    cap = captures[N]
    std_int = std_per_N[str(N)]['std_intercept']

    NLO_cap2_pis2 = 144 * np.pi * pi_s**2 * std_int / cap**2
    NLO_cap2_only = 144 * np.pi * std_int / cap**2

    print(f"{N:>3}  {pi_s:>7.4f}  {cap:>7.4f}  {std_int:+11.4e}  "
          f"{NLO_cap2_pis2:+16.4e}  {NLO_cap2_only:+14.4e}")
print()
print(f"Target c_2/C_A² = {c2_target_per_CA2}")
