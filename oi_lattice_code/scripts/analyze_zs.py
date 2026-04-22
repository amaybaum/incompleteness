#!/usr/bin/env python3
"""
analyze_zs.py — Extract Z_S(m) from k6_hmc.c output files

Takes a set of k6_hmc.c output files covering a mass scan at fixed L, 
computes the free-theory ⟨ψ̄ψ⟩ at each mass, and extracts

    Z_S(m) = ⟨ψ̄ψ⟩_int(m) / ⟨ψ̄ψ⟩_free(m)

Then cubic-interpolates to get Z_S at a target mass (default 0.122,
which reproduces the paper's Z_S(0.122) = 1.813 claim).

The free-theory ⟨ψ̄ψ⟩ is computed analytically on the same lattice:

    ⟨ψ̄ψ⟩_free(m) = (1/V) Σ_{k≠0} N_K × m / (Σ_μ sin²(k_μ) + m²)

where N_K = 6 is the number of staggered components in K=6. Sum is
over lattice momenta k_μ = 2π n_μ / L excluding the staggered zero modes
(which contribute unphysically). This matches the regulator the HMC code
uses implicitly (the CG solver converges on the non-zero-mode subspace).

Usage:
    python3 analyze_zs.py [-L 32] [-m 0.122] [-beta 11.1] file1.dat file2.dat ...

Output:
    Per-file: mass, <pbp> ± err, <pbp>_free, Z_S ± err
    Final:    cubic-interpolated Z_S(m_target) ± err

Input files: output of k6_hmc.c, containing lines like
    # k6_hmc_v2 L=32 mass=0.122000 beta=(11.1,7.4,3.7) nstep=1 tau=0.01
    # traj  acc  dH         pbp         P3      P2      P1
        0  1  -0.0543       1.813400  0.7512  0.8564  0.0312
        1  1  +0.1234       1.815100  0.7511  0.8563  0.0311
    ...
    # RESULT: <pbp>=1.813123 +/- 0.000987 acc=87%

Prints a cubic-interpolation table in Z_S vs m, plus the target value.
"""
import sys
import os
import re
import argparse
import numpy as np

def parse_k6_hmc_output(filename):
    """Parse a k6_hmc.c output file. Returns (L, mass, pbp_mean, pbp_err, ntraj)."""
    L = None
    mass = None
    pbp_mean = None
    pbp_err = None
    pbp_values = []
    
    with open(filename) as f:
        for line in f:
            m = re.search(r'L=(\d+).*mass=([\d.]+)', line)
            if m:
                L = int(m.group(1))
                mass = float(m.group(2))
            m = re.search(r'<pbp>=([\d.eE+-]+)\s*\+/-\s*([\d.eE+-]+)', line)
            if m:
                pbp_mean = float(m.group(1))
                pbp_err = float(m.group(2))
                continue
            if line.startswith('#') or not line.strip():
                continue
            # Data line: traj acc dH pbp P3 P2 P1
            parts = line.split()
            if len(parts) >= 4:
                try:
                    pbp_values.append(float(parts[3]))
                except ValueError:
                    pass
    
    # If no RESULT line, compute from data (skip first 20% as thermalization)
    if pbp_mean is None and pbp_values:
        n = len(pbp_values)
        nkeep = max(1, int(0.8 * n))
        arr = np.array(pbp_values[-nkeep:])
        pbp_mean = np.mean(arr)
        pbp_err = np.std(arr, ddof=1) / np.sqrt(len(arr)) if len(arr) > 1 else 0.0
    
    return L, mass, pbp_mean, pbp_err, len(pbp_values)


def pbp_free(m, L, NK=6, DIM=3):
    """
    Free-theory ⟨ψ̄ψ⟩ on an L^DIM lattice with NK staggered components.
    
    Formula (3D spatial lattice, matches k6_hmc.c's DIM=3):
        ⟨ψ̄ψ⟩_free = NK × (1/V) Σ_{k≠0} m / (Σ_μ sin²(k_μ) + m²)
    
    Excludes the staggered zero mode at k=(0,0,0) and k=(π,π,π) (in index form
    k = 0 and k = L/2 respectively when L is even), which are regulator-dependent.
    """
    L3 = L**DIM
    # Build all lattice momenta
    ks = 2 * np.pi * np.arange(L) / L
    # 3D momentum grid
    if DIM == 3:
        KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
        D = np.sin(KX)**2 + np.sin(KY)**2 + np.sin(KZ)**2 + m**2
    elif DIM == 4:
        K = np.meshgrid(*[ks]*4, indexing='ij')
        D = sum(np.sin(k)**2 for k in K) + m**2
    else:
        raise ValueError(f"Unsupported DIM={DIM}")
    
    # Exclude staggered zero modes: k_μ ∈ {0, π} for all μ
    # In L-index form: k_μ = 0 or k_μ = L/2
    zero_mask = np.ones_like(D, dtype=bool)
    # Only mask if L is even (so L/2 is exact)
    if L % 2 == 0:
        half = L // 2
        # Build the mask: exclude points where ALL indices are in {0, L/2}
        idxs = [0, half]
        if DIM == 3:
            for i in idxs:
                for j in idxs:
                    for k in idxs:
                        zero_mask[i, j, k] = False
    
    integrand = m / D
    return NK * np.sum(integrand[zero_mask]) / L3


def main():
    parser = argparse.ArgumentParser(description="Extract Z_S(m) from k6_hmc output files")
    parser.add_argument('-L', type=int, default=None, 
                        help='Override lattice size (auto-detected otherwise)')
    parser.add_argument('-m', '--target', type=float, default=0.122,
                        help='Target mass for cubic interpolation (default: 0.122)')
    parser.add_argument('-beta', type=float, default=11.1,
                        help='Beta (for labeling, not used in calculation)')
    parser.add_argument('files', nargs='+', help='k6_hmc output files')
    args = parser.parse_args()
    
    rows = []
    for fname in args.files:
        if not os.path.isfile(fname):
            print(f"  SKIP: {fname} not found", file=sys.stderr)
            continue
        L, mass, pbp_mean, pbp_err, n = parse_k6_hmc_output(fname)
        if L is None or mass is None or pbp_mean is None:
            print(f"  SKIP: {fname} could not be parsed", file=sys.stderr)
            continue
        if args.L is not None:
            L = args.L
        pbp_f = pbp_free(mass, L)
        Z_S = pbp_mean / pbp_f if pbp_f != 0 else 0.0
        Z_S_err = pbp_err / pbp_f if pbp_f != 0 else 0.0
        rows.append((mass, pbp_mean, pbp_err, pbp_f, Z_S, Z_S_err, L, n, fname))
    
    if not rows:
        print("No valid data files found.", file=sys.stderr)
        sys.exit(1)
    
    # Sort by mass
    rows.sort(key=lambda r: r[0])
    
    # Check all same L
    Ls = set(r[6] for r in rows)
    if len(Ls) > 1:
        print(f"WARNING: mixed lattice sizes {Ls} — Z_S(m) is L-dependent!", file=sys.stderr)
    L_label = list(Ls)[0] if len(Ls) == 1 else "mixed"
    
    print("=" * 78)
    print(f"Z_S(m) extraction from k6_hmc output  —  L={L_label}, β={args.beta}")
    print("=" * 78)
    print(f"  {'mass':>8}  {'⟨ψ̄ψ⟩_int':>10} {'±err':>8}   {'⟨ψ̄ψ⟩_free':>11}   {'Z_S':>7} {'±':>7}   {'N_traj':>7}")
    for mass, pbp_m, pbp_e, pbp_f, Z, Z_e, L, n, fname in rows:
        print(f"  {mass:8.5f}  {pbp_m:10.5f} {pbp_e:8.5f}   {pbp_f:11.5f}   {Z:7.4f} {Z_e:7.4f}   {n:7d}")
    
    # Cubic interpolation to target mass
    masses = np.array([r[0] for r in rows])
    ZS_vals = np.array([r[4] for r in rows])
    ZS_errs = np.array([r[5] for r in rows])
    
    m_target = args.target
    
    if len(masses) < 4:
        print(f"\n  Cubic interpolation requires ≥ 4 mass points; have {len(masses)}. Skipping.")
        return
    
    if m_target < masses.min() or m_target > masses.max():
        print(f"\n  Target m={m_target} is outside data range [{masses.min()}, {masses.max()}];")
        print(f"  extrapolation may be unreliable.")
    
    # Fit cubic (in the volume-converged region m·L ≳ 3 per SM.md)
    mL_min = 3.0 / L if len(Ls) == 1 else 0
    in_range = masses >= mL_min
    if np.sum(in_range) < 4:
        print(f"\n  Fewer than 4 points in volume-converged region (mL ≥ {mL_min:.3f}).")
        print(f"  Using all points; result may be volume-biased.")
        in_range = np.ones_like(masses, dtype=bool)
    
    try:
        from scipy.interpolate import CubicSpline
        cs = CubicSpline(masses[in_range], ZS_vals[in_range])
        ZS_interp = float(cs(m_target))
        # Error estimate: use the error at the nearest data point
        i_near = np.argmin(np.abs(masses - m_target))
        ZS_interp_err = ZS_errs[i_near]
    except ImportError:
        # Fallback: linear interpolation
        ZS_interp = np.interp(m_target, masses, ZS_vals)
        i_near = np.argmin(np.abs(masses - m_target))
        ZS_interp_err = ZS_errs[i_near]
    
    print("\n" + "=" * 78)
    print(f"Cubic interpolation to target mass")
    print("=" * 78)
    print(f"  m_target = {m_target}")
    print(f"  Z_S(m_target) = {ZS_interp:.4f} ± {ZS_interp_err:.4f}")
    print(f"  Using {np.sum(in_range)}/{len(masses)} points (volume-converged region)")
    print()
    print(f"  → m_b/m_τ = 4.28 / Z_S(m_target) = {4.28/ZS_interp:.3f}")
    print(f"  Observed: 2.352 ± 0.017")
    sigma = abs(4.28/ZS_interp - 2.352) / 0.017 if ZS_interp > 0 else 0
    print(f"  Deviation: {sigma:.2f}σ")


if __name__ == '__main__':
    main()
