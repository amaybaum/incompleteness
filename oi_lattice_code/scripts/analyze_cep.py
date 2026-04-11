#!/usr/bin/env python3
"""
analyze_cep.py — Analyze K=6 Constraint Effective Potential h-scan

Reads the summary file from run_cep_scan.sh and:
1. Plots dV/dh vs h (fermion, gauge, total)
2. Plots plaquettes vs h (SU(2) ordering diagnostic)
3. Integrates dV/dh to get V(h) - V(0)
4. Checks for sign change in dV/dh (= VEV exists)
5. Fits the functional form to extract effective λ

Usage: python3 analyze_cep.py cep_summary_L6_m100.dat
"""
import sys
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_cep.py <summary_file>")
        sys.exit(1)

    fname = sys.argv[1]
    data = []
    with open(fname) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            vals = line.split()
            if len(vals) >= 11:
                data.append([float(v) for v in vals])

    if not data:
        print(f"No data in {fname}")
        sys.exit(1)

    d = np.array(data)
    h = d[:,0]
    pbp = d[:,1]
    pbp_err = d[:,2]
    dvdh_f = d[:,3]
    dvdh_g = d[:,4]
    dvdh_tot = d[:,5]
    dvdh_err = d[:,6]
    P3 = d[:,7]
    P2 = d[:,8]
    P1 = d[:,9]

    print("="*65)
    print("CONSTRAINT EFFECTIVE POTENTIAL ANALYSIS")
    print("="*65)
    print()
    print(f"  {'h':>6s}  {'dV/dh_f':>10s}  {'dV/dh_g':>10s}  {'dV/dh_tot':>10s}  {'P2':>6s}  {'pbp':>8s}")
    print(f"  {'------':>6s}  {'----------':>10s}  {'----------':>10s}  {'----------':>10s}  {'------':>6s}  {'--------':>8s}")
    for i in range(len(h)):
        print(f"  {h[i]:6.3f}  {dvdh_f[i]:+10.4f}  {dvdh_g[i]:+10.4f}  {dvdh_tot[i]:+10.4f}  {P2[i]:6.4f}  {pbp[i]:8.4f}")

    print()

    # Check for sign change in dV/dh
    sign_changes = []
    for i in range(1, len(h)):
        if dvdh_tot[i-1] * dvdh_tot[i] < 0:
            # Linear interpolation for zero crossing
            h_cross = h[i-1] - dvdh_tot[i-1] * (h[i] - h[i-1]) / (dvdh_tot[i] - dvdh_tot[i-1])
            sign_changes.append(h_cross)

    if sign_changes:
        print(f"  *** SIGN CHANGE DETECTED in dV/dh at h ≈ {sign_changes[0]:.4f} ***")
        print(f"  This indicates a VEV: v = h* ≈ {sign_changes[0]:.4f} (lattice units)")
        print()
    else:
        print("  No sign change in dV/dh — no VEV at this resolution.")
        print()

    # Integrate dV/dh to get V(h) - V(0)
    V = np.zeros_like(h)
    for i in range(1, len(h)):
        V[i] = V[i-1] + 0.5*(dvdh_tot[i-1] + dvdh_tot[i]) * (h[i] - h[i-1])

    print("  V(h) - V(0) by trapezoidal integration:")
    for i in range(len(h)):
        print(f"    h={h[i]:6.3f}  V-V(0) = {V[i]:+10.4f}")
    print()

    # SU(2) ordering diagnostic
    print("  SU(2) ordering diagnostic (P2 vs h):")
    if len(h) > 1:
        dP2_dh = np.gradient(P2, h)
        print(f"    dP2/dh at h=0: {dP2_dh[0]:+.4f}")
        print(f"    dP2/dh at h=max: {dP2_dh[-1]:+.4f}")
        if P2[-1] > P2[0]:
            print(f"    P2 INCREASES with h: {P2[0]:.4f} → {P2[-1]:.4f}")
            print("    SU(2) is ordering → entropy cost exists → quartic stabilization present")
        else:
            print(f"    P2 does not increase: {P2[0]:.4f} → {P2[-1]:.4f}")
    print()

    # Decomposition analysis
    if len(h) > 2 and any(h > 0):
        mask = h > 0
        ratio = np.abs(dvdh_g[mask]) / np.abs(dvdh_f[mask])
        print(f"  |dV/dh_gauge| / |dV/dh_fermion| ratio:")
        for i in np.where(mask)[0]:
            r = abs(dvdh_g[i]) / abs(dvdh_f[i]) if abs(dvdh_f[i]) > 0 else 0
            print(f"    h={h[i]:6.3f}: ratio = {r:.4f}")
        print()
        print("  If this ratio increases with h and approaches 1,")
        print("  the gauge contribution CAN balance the fermion contribution")
        print("  at sufficiently large h — indicating a VEV exists in principle.")
    print()

    # Effective potential fit: V(h) = a*h² + b*h⁴
    if len(h) > 3 and any(V != 0):
        from numpy.polynomial import polynomial as P
        mask = h > 0
        hm, Vm = h[mask], V[mask]
        if len(hm) >= 3:
            # Fit V/h² = a + b*h² (linear in h²)
            Vh2 = Vm / hm**2
            h2 = hm**2
            if len(h2) >= 2:
                coeffs = np.polyfit(h2, Vh2, 1)
                b_eff, a_eff = coeffs
                print(f"  Effective potential fit: V(h) ≈ {a_eff:+.4f} h² + {b_eff:+.4f} h⁴")
                if a_eff < 0 and b_eff > 0:
                    v_pred = np.sqrt(-a_eff / (2*b_eff))
                    print(f"  → Minimum at h* = √(-a/2b) = {v_pred:.4f}")
                elif a_eff < 0 and b_eff <= 0:
                    print(f"  → a<0, b≤0: potential unbounded below — no stable minimum")
                else:
                    print(f"  → a≥0: minimum at h=0 — no symmetry breaking")
    print()
    print("="*65)

if __name__ == "__main__":
    main()
