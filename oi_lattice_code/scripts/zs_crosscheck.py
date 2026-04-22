#!/usr/bin/env python3
"""
zs_crosscheck.py — Compare Z_S extracted by three independent schemes.

Runs (or parses output of):
  - zs_measurements/rimom.c        (RI-MOM, momentum-space propagator)
  - zs_measurements/taste_irrep.c  (O(3) irrep decomposition)
  - zs_measurements/ward_chiral.c  (L/R sublattice parity)

Reports Z_S from each scheme at a common (L, m, beta), and highlights
the diagnostic channels identified from past production runs:

  - rimom:       report Z_S at |p|²=5 (24 momenta, away from zero and BZ corner)
  - taste_irrep: report Z_S(T1) (3 generations live here; A1 is Higgs)  
  - ward_chiral: report Z_S(L) (physical sector after trace-out)

The three values should agree within statistical errors when each code is
measuring the "physical" channel. Systematic disagreement points to
regulator dependence between schemes.

Usage:
    # Run all three codes and compare
    python3 zs_crosscheck.py --run -L 16 -m 0.20 -ncfg 50 -nthm 100 -beta 11.1

    # Parse existing output files
    python3 zs_crosscheck.py --parse rimom_out.txt taste_out.txt ward_out.txt
"""
import sys
import os
import re
import subprocess
import argparse


def find_binary(name):
    """Look for compiled binary in zs_measurements/ or ./"""
    for candidate in [
        f'./{name}',
        f'./zs_measurements/{name}',
        f'../zs_measurements/{name}',
        f'../../zs_measurements/{name}',
    ]:
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return None


def run_code(name, L, ncfg, nthm, beta, mass):
    """Run a zs_measurements code and return stdout."""
    binary = find_binary(name)
    if binary is None:
        print(f"  ERROR: binary '{name}' not found. Compile with:")
        print(f"    gcc -O3 -o {name} zs_measurements/{name}.c -lm")
        return None
    cmd = [binary, str(L), str(ncfg), str(nthm), f"{beta:.2f}", f"{mass:.3f}"]
    print(f"  Running: {' '.join(cmd)}")
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=3600)
        return out
    except subprocess.CalledProcessError as e:
        print(f"  ERROR running {name}: {e}")
        print(e.output[-500:] if e.output else "")
        return None


def parse_rimom(text):
    """Extract Z_S at |p|²=5 and all-|p| from rimom output."""
    # Table: |p|^2  n_mom  S_int/S0  Z_S  4.28*ratio
    zs_p2_5 = None
    zs_all = None
    for line in text.splitlines():
        m = re.match(r'\s*(\d+)\s+\d+\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)', line)
        if m and m.group(1) == '5':
            zs_p2_5 = float(m.group(3))
        m = re.search(r'All.*ratio\s+S_int/S_free\s*=\s*([\d.]+)', line)
        if m:
            # ratio = 1/Z_S, so Z_S = 1/ratio
            ratio = float(m.group(1))
            if ratio > 0:
                zs_all = 1.0 / ratio
    return {'p2=5': zs_p2_5, 'all-|p|': zs_all}


def parse_taste_irrep(text):
    """Extract Z_S per taste irrep from taste_irrep output."""
    results = {}
    labels = {
        'A1 (Higgs)': 'A1',
        'T1 (3 gen)': 'T1',
        'T2': 'T2',
        'A2': 'A2',
        'All': 'All',
    }
    # Format: A1 (Higgs)    0.7310       ±0.0275    2.983       ±0.112
    for line in text.splitlines():
        for pat, short in labels.items():
            if line.strip().startswith(pat):
                parts = line.split()
                # The 5th token should be S_int/S_free
                # Line: <label> <ratio> ±<err> <4.28*ratio> ±<err>
                # split with spaces... find first decimal
                nums = re.findall(r'[\d.]+', line.split(pat)[1] if pat in line else line)
                if nums:
                    try:
                        ratio = float(nums[0])
                        # Z_S = 1/ratio if ratio is S_int/S_free
                        # Z_S = ratio if ratio is Z_S directly
                        # The taste_irrep code prints "S_int/S_free" as the column header,
                        # which is the ratio pbp_int/pbp_free directly → Z_S itself
                        results[short] = ratio
                    except ValueError:
                        pass
    return results


def parse_ward_chiral(text):
    """Extract Z_S(L), Z_S(R), Z_S(full) from ward_chiral output."""
    results = {}
    for line in text.splitlines():
        m = re.search(r'L \(even, physical\):\s*([\d.]+)', line)
        if m: results['L (physical)'] = float(m.group(1))
        m = re.search(r'R \(odd, traced out\):\s*([\d.]+)', line)
        if m: results['R (hidden)'] = float(m.group(1))
        m = re.search(r'Full:\s+([\d.]+)', line)
        if m and 'full' not in results: results['full'] = float(m.group(1))
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', action='store_true', help='Run all three codes')
    parser.add_argument('--parse', nargs=3, metavar=('RIMOM','TASTE','WARD'),
                        help='Parse three existing output files')
    parser.add_argument('-L', type=int, default=16)
    parser.add_argument('-m', type=float, default=0.20)
    parser.add_argument('-ncfg', type=int, default=50)
    parser.add_argument('-nthm', type=int, default=100)
    parser.add_argument('-beta', type=float, default=11.1)
    args = parser.parse_args()
    
    if args.run:
        print("="*70)
        print(f"Z_S cross-check: L={args.L}, m={args.m}, β={args.beta}, {args.ncfg} configs")
        print("="*70)
        rimom_out = run_code('rimom', args.L, args.ncfg, args.nthm, args.beta, args.m)
        taste_out = run_code('taste_irrep', args.L, args.ncfg, args.nthm, args.beta, args.m)
        ward_out = run_code('ward_chiral', args.L, args.ncfg, args.nthm, args.beta, args.m)
    elif args.parse:
        rimom_out = open(args.parse[0]).read() if os.path.isfile(args.parse[0]) else None
        taste_out = open(args.parse[1]).read() if os.path.isfile(args.parse[1]) else None
        ward_out = open(args.parse[2]).read() if os.path.isfile(args.parse[2]) else None
    else:
        parser.print_help()
        sys.exit(1)
    
    rimom_Zs = parse_rimom(rimom_out) if rimom_out else {}
    taste_Zs = parse_taste_irrep(taste_out) if taste_out else {}
    ward_Zs = parse_ward_chiral(ward_out) if ward_out else {}
    
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print(f"\n{'Scheme':<20} {'Channel':<16} {'Z_S':>8} {'m_b/m_τ':>10}")
    print("-"*56)
    
    all_vals = []
    
    for ch, zs in rimom_Zs.items():
        if zs and zs > 0:
            mbt = 4.28 / zs
            is_diag = '  ← diagnostic' if ch == 'p2=5' else ''
            print(f"{'rimom':<20} {ch:<16} {zs:>8.4f} {mbt:>10.3f}{is_diag}")
            if ch == 'p2=5': all_vals.append(('rimom |p|²=5', zs))
    
    for ch, zs in taste_Zs.items():
        if zs and zs > 0:
            mbt = 4.28 / zs
            is_diag = '  ← diagnostic (3 generations)' if ch == 'T1' else ''
            print(f"{'taste_irrep':<20} {ch:<16} {zs:>8.4f} {mbt:>10.3f}{is_diag}")
            if ch == 'T1': all_vals.append(('taste_irrep T1', zs))
    
    for ch, zs in ward_Zs.items():
        if zs and zs > 0:
            mbt = 4.28 / zs
            is_diag = '  ← diagnostic (physical)' if ch == 'L (physical)' else ''
            print(f"{'ward_chiral':<20} {ch:<16} {zs:>8.4f} {mbt:>10.3f}{is_diag}")
            if ch == 'L (physical)': all_vals.append(('ward_chiral L', zs))
    
    if len(all_vals) >= 2:
        print("\n" + "="*70)
        print("Diagnostic-channel comparison")
        print("="*70)
        import statistics
        vals = [v for _, v in all_vals]
        mean = statistics.mean(vals)
        stdev = statistics.stdev(vals) if len(vals) > 1 else 0
        print(f"  Mean:    Z_S = {mean:.4f} ± {stdev:.4f} (stdev across schemes)")
        print(f"  m_b/m_τ = 4.28/{mean:.4f} = {4.28/mean:.3f}")
        print(f"  Observed: 2.352 ± 0.017")
        rel_scatter = stdev/mean * 100 if mean else 0
        print(f"  Cross-scheme scatter: {rel_scatter:.2f}%")
        if rel_scatter < 5:
            print(f"  → Schemes agree within systematics. Good cross-check.")
        else:
            print(f"  → {rel_scatter:.1f}% scatter exceeds typical statistics.")
            print(f"    Check for regulator/convention differences between schemes.")


if __name__ == '__main__':
    main()
