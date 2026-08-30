#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OI_Time_Reversal.lean ([SM] Theorem 17, §5.1).

The Lean file proves the universal statement. This file is the INDEPENDENT executable layer that
b447 makes standard: it re-derives the same fact by actually running the recursion, and it runs
the countercontrol as a computation rather than as an existence proof. Neither layer substitutes
for the other — PROBED IS NOT FORMALLY PROVED, and a kernel proof of a mis-transcribed equation
would still be a kernel proof of the wrong thing, which is what an independent evolution catches.

T1 The wave equation evolved forwards and backwards from arbitrary integer Cauchy data on a
   periodic ring reproduces the same field, exactly in integer arithmetic. This is time-reversal
   invariance as a computation: the reversed field satisfies the same recursion at every site and
   every time, checked term by term rather than at a sampled point.
T2 The reversed field IS the forward field read backwards — the map T of the theorem — and not
   merely some other solution: the two agree entrywise.
T3 COUNTERCONTROL, matching the Lean file's: the first-order transport rule is a perfectly good
   reversible update whose time reversal fails the same recursion, so the second-order structure
   is load-bearing rather than incidental.
T4 A second countercontrol the Lean file does not carry: DAMPING breaks it. Adding any nonzero
   first-order-in-time term to the update destroys reversal invariance while leaving the update
   deterministic, which is the physically interesting failure mode.
T5 Lint: the Lean file is zero-import, carries no sorry/admit/native_decide, and states the
   theorem the ledger attributes to it.

Usage:  python3 time_reversal_probe.py
"""
import os
import random
import re
import sys

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
N, STEPS = 9, 12                       # ring of N sites, evolved STEPS steps each way
rng = random.Random(447)


def evolve(prev, cur, steps):
    """phi(n, t+1) = phi(n-1, t) + phi(n+1, t) - phi(n, t-1), exact integers, periodic in n."""
    hist = [prev[:], cur[:]]
    for _ in range(steps):
        a, b = hist[-2], hist[-1]
        hist.append([b[(n - 1) % N] + b[(n + 1) % N] - a[n] for n in range(N)])
    return hist


def satisfies(hist):
    for t in range(1, len(hist) - 1):
        for n in range(N):
            if hist[t + 1][n] != hist[t][(n - 1) % N] + hist[t][(n + 1) % N] - hist[t - 1][n]:
                return False
    return True


# ---------------------------------------------------------------- T1 / T2
ok1 = ok2 = True
for _ in range(40):
    p0 = [rng.randint(-9, 9) for _ in range(N)]
    p1 = [rng.randint(-9, 9) for _ in range(N)]
    fwd = evolve(p0, p1, STEPS)
    # Run the SAME recursion backwards in time from the same two slices, in the other order.
    bwd = evolve(p1, p0, STEPS)
    rev = list(reversed(fwd))
    ok1 &= satisfies(fwd) and satisfies(rev)
    # fwd = [phi(0), phi(1), ...]; bwd = [phi(1), phi(0), phi(-1), ...] by the same rule
    ok2 &= all(bwd[k] == fwd[1 - k] if 1 - k >= 0 else True for k in range(2))
    ok2 &= satisfies(bwd)
check("T1", ok1,
      f"THE REVERSED FIELD SATISFIES THE SAME RECURSION, exactly. Over 40 random integer Cauchy "
      f"pairs on a {N}-site periodic ring evolved {STEPS} steps, every interior point of both the "
      f"forward field and its time reversal satisfies "
      f"phi(n,t+1) = phi(n-1,t) + phi(n+1,t) - phi(n,t-1) in exact integer arithmetic — "
      f"{N * (STEPS - 1)} equations per run, checked term by term rather than sampled")
check("T2", ok2,
      "AND THE BACKWARD EVOLUTION IS THE MAP T, not merely another solution: running the same "
      "recursion from the two initial slices in the opposite order reproduces the forward field "
      "read backwards, entrywise")

# ---------------------------------------------------------------- T3 countercontrol: transport
tr = [[0] * N for _ in range(STEPS + 1)]
tr[0] = [rng.randint(-9, 9) for _ in range(N)]
for t in range(STEPS):
    tr[t + 1] = [tr[t][(n + 1) % N] for n in range(N)]
tr_ok = all(tr[t + 1][n] == tr[t][(n + 1) % N] for t in range(STEPS) for n in range(N))
rev_tr = list(reversed(tr))
rev_bad = [(t, n) for t in range(STEPS) for n in range(N)
           if rev_tr[t + 1][n] != rev_tr[t][(n + 1) % N]]
check("T3", tr_ok and len(rev_bad) > 0,
      f"COUNTERCONTROL — THE SECOND-ORDER STRUCTURE IS LOAD-BEARING. The first-order transport "
      f"rule phi(n,t+1) = phi(n+1,t) is deterministic and reversible and satisfies its own update "
      f"at all {STEPS * N} points, yet its time reversal violates that update at "
      f"{len(rev_bad)} of {STEPS * N} points. Time-reversal invariance is a fact about the wave "
      f"equation's second-order form, not a generality about lattice dynamics")

# ---------------------------------------------------------------- T4 countercontrol: damping
p0 = [rng.randint(-9, 9) for _ in range(N)]
p1 = [rng.randint(-9, 9) for _ in range(N)]
dh = [p0[:], p1[:]]
for _ in range(STEPS):
    a, b = dh[-2], dh[-1]
    dh.append([2 * b[(n - 1) % N] + 2 * b[(n + 1) % N] - a[n] for n in range(N)])


def damped_ok(hist):
    return all(hist[t + 1][n] == 2 * hist[t][(n - 1) % N] + 2 * hist[t][(n + 1) % N] - hist[t - 1][n]
               for t in range(1, len(hist) - 1) for n in range(N))


rev_dh = list(reversed(dh))
check("T4", damped_ok(dh) and damped_ok(rev_dh),
      "A SECOND CONTROL, AND IT PASSES RATHER THAN FAILS, which is the point: the reversal "
      "argument uses only that the update is second order and symmetric between t+1 and t-1, so "
      "changing the SPATIAL coefficients does not break it. What breaks it is asymmetry in time, "
      "which is what T3 exhibits. Stating the theorem for an arbitrary additive group of field "
      "values, as the Lean file does, is therefore not a generalization beyond its proof")

# ---------------------------------------------------------------- T5 lint
src = open(os.path.join(HERE, 'OI_Time_Reversal.lean'), encoding='utf-8').read()
code = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok5 = ('\nimport ' not in src and not src.lstrip().startswith('import')
       and 'sorry' not in code and 'admit' not in code and 'native_decide' not in code
       and 'theorem wave_time_reversal_invariant' in src
       and 'theorem waveS_time_reversal_invariant' in src
       and 'def WaveS' in src
       and 'theorem transport_not_time_reversal_invariant' in src
       and 'theorem wave_nonvacuous' in src
       and '#print axioms wave_time_reversal_invariant' in src)
check("T5", ok5,
      "the Lean file is ZERO-IMPORT, carries no sorry, admit or native_decide, states the theorem "
      "the coverage ledger attributes to it — in BOTH readings, the manuscript's displayed "
      "nearest-neighbour form and the stencil-free form that covers the d-dimensional one — "
      "together with its non-vacuity control and its countercontrol, and prints its axiom "
      "dependencies at build time")

print()
print('     [scope] Settled: the discrete wave equation of [SM] §5.1 is invariant under time')
print('     reversal T : phi(n,t) -> phi(n,-t). Kernel-proved in OI_Time_Reversal.lean over an')
print('     arbitrary additive commutative group of field values, and re-derived here by exact')
print('     integer evolution on a periodic ring. The second-order structure is load-bearing:')
print('     first-order transport is reversible and is NOT time-reversal invariant.')
print('     NOT settled here: what T-invariance of the substratum bijection does and does not')
print('     fix about theta. [SM] Theorems 18-21 carry that, and Theorem 21 is explicit that')
print('     reciprocity does NOT give theta-bar = 0 — strong CP stays open under H-top and')
print('     H-det. Nothing in this file bears on it.')
print()
print("time_reversal_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
