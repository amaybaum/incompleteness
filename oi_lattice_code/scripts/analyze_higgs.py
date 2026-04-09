#!/usr/bin/env python3
"""
analyze_higgs.py — Analyze K=6 dynamical Higgs kappa-scan

Uses gauge-invariant <hop> = <Re[Phi^dag W Phi']> as the order parameter
(Elitzur-safe — no gauge fixing needed).

Usage: python3 analyze_higgs.py summary_L6.dat [summary_L8.dat ...]
"""
import sys
import numpy as np

def parse(fname):
    data = []
    meta = {}
    with open(fname) as f:
        for line in f:
            if line.startswith('# Higgs'):
                for tok in line.split():
                    if '=' in tok:
                        k,v = tok.split('=')
                        try: meta[k] = float(v)
                        except: meta[k] = v
            if line.startswith('#') or not line.strip(): continue
            vals = line.split()
            if len(vals) >= 8:
                data.append([float(v) for v in vals])
    return np.array(data), meta

def analyze_one(fname):
    d, meta = parse(fname)
    if len(d) == 0:
        print(f"  No data in {fname}")
        return None
    L = int(meta.get('L', 0))
    V = L**3
    lam = meta.get('lambda', 0)

    kappa = d[:,0]
    phi_mod = d[:,1]
    hop = d[:,3]
    hop_err = d[:,4]
    chi_hop = d[:,5]
    P2 = d[:,6]

    print(f"  File: {fname}")
    print(f"  L={L}, V={V}, lambda={lam}")
    print()
    print(f"  {'k':>6s}  {'<hop>':>10s}  {'+-err':>8s}  {'chi_hop':>8s}  {'<|Phi|>':>8s}  {'P2':>6s}")
    print(f"  {'------':>6s}  {'----------':>10s}  {'--------':>8s}  {'--------':>8s}  {'--------':>8s}  {'------':>6s}")
    for i in range(len(kappa)):
        print(f"  {kappa[i]:6.3f}  {hop[i]:+10.6f}  {hop_err[i]:8.6f}  {chi_hop[i]:8.4f}  {phi_mod[i]:8.4f}  {P2[i]:6.4f}")

    ipeak = np.argmax(chi_hop)
    print()
    print(f"  chi_hop peak: {chi_hop[ipeak]:.4f} at kappa = {kappa[ipeak]:.3f}")
    print()

    for i in range(len(kappa)):
        if hop[i] > 3*hop_err[i] and hop[i] > 0.1:
            print(f"  kappa={kappa[i]:.3f}: <hop>={hop[i]:+.4f} > 0 at 3sigma -> BROKEN PHASE")
        elif hop[i] > 2*hop_err[i] and hop[i] > 0.05:
            print(f"  kappa={kappa[i]:.3f}: <hop>={hop[i]:+.4f} -> possible signal (2sigma)")

    return kappa, hop, hop_err, chi_hop, L

print("="*65)
print("DYNAMICAL HIGGS ANALYSIS (gauge-invariant)")
print("="*65)
print()

results = []
for fname in sys.argv[1:]:
    r = analyze_one(fname)
    if r: results.append(r)
    print()

if len(results) >= 2:
    print("="*65)
    print("VOLUME COMPARISON")
    print("="*65)
    print()
    k0, h0, _, _, L0 = results[0]
    k1, h1, _, _, L1 = results[1]
    print(f"  <hop> should be VOLUME-INDEPENDENT in both phases")
    print(f"  (unlike magnetization, which scales as 1/sqrt(V))")
    print()
    common = set(np.round(k0,3)) & set(np.round(k1,3))
    if common:
        print(f"  {'k':>6s}  {'hop(L=%d)'%L0:>12s}  {'hop(L=%d)'%L1:>12s}  {'agree?':>8s}")
        for kv in sorted(common):
            i0 = np.argmin(np.abs(k0-kv))
            i1 = np.argmin(np.abs(k1-kv))
            diff = abs(h0[i0]-h1[i1])
            agree = "YES" if diff < 0.05 else "no"
            print(f"  {kv:6.3f}  {h0[i0]:+12.6f}  {h1[i1]:+12.6f}  {agree:>8s}")

print()
print("="*65)
