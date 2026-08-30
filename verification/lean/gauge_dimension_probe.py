#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/GaugeDimension.lean.

[SM] Theorem 16: the Yang-Mills coupling has mass dimension [g] = (3 - d)/2, dimensionless iff
d = 3.

The Lean file deliberately does NOT define [g] := (3 - d)/2 -- that would kernel-check the
notation. The physical content is the hypothesis: the action S = (1/4g^2) int d^{d+1}x F^2 is
dimensionless, so in mass dimensions

    -2[g] + 2[F] - (d + 1) = 0,

and with [F] = 2 the theorem is arithmetic from it. This probe mirrors that structure in exact
Fraction arithmetic and adds the two countercontrols the balance premise earns: the off-by-one
measure and the general-[F] formula.

  G1  the balance solved for g gives (3 - d)/2 for d = 0..12, and g = 0 exactly at d = 3.
  G2  COUNTERCONTROL for the measure exponent: balancing against d^d x gives (4 - d)/2, which
      agrees with the right answer at NO d -- the two differ identically by 1/2.
  G3  the general formula: leaving [F] arbitrary gives [g] = [F] - (d+1)/2 exactly, and [F] = 2
      is the one instantiation the theorem uses; a scalar-field check ([phi] = (d-1)/2 from the
      kinetic balance) confirms the identical bookkeeping reproduces the standard answer.
  G4  lint.

Usage:  python3 gauge_dimension_probe.py
"""
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


def solve_balance(d, F, measure_dim):
    """g from  -2 g + 2 F - measure_dim = 0."""
    return (2 * Fraction(F) - Fraction(measure_dim)) / 2


# ---------------------------------------------------------------- G1  the theorem
ok1 = True
for d in range(0, 13):
    g = solve_balance(d, 2, d + 1)
    ok1 &= g == Fraction(3 - d, 2)
    ok1 &= (g == 0) == (d == 3)
check("G1", ok1,
      "the balance -2g + 2*2 - (d+1) = 0 solved exactly for d = 0..12: g = (3 - d)/2 every time, "
      "and g = 0 precisely at d = 3. Lean's `theorem_16`, from the same premise")

# ---------------------------------------------------------------- G2  the off-by-one
ok2 = True
for d in range(0, 13):
    g_wrong = solve_balance(d, 2, d)
    ok2 &= g_wrong == Fraction(4 - d, 2)
    ok2 &= g_wrong != Fraction(3 - d, 2)
    ok2 &= g_wrong - Fraction(3 - d, 2) == Fraction(1, 2)
    ok2 &= (g_wrong == 0) == (d == 4)                 # the mistake would even move the threshold
check("G2", ok2,
      "COUNTERCONTROL for the measure exponent. Balancing against a d-dimensional measure gives "
      "(4 - d)/2 -- off by exactly 1/2 at every d, never agreeing with the right answer, and it "
      "would move the dimensionless point to d = 4. The (d+1) in the hypothesis is load-bearing; "
      "Lean's `off_by_one` and `off_by_one_never_agrees`")

# ---------------------------------------------------------------- G3  the general formula
ok3 = True
for d in range(0, 13):
    for F in (Fraction(0), Fraction(1), Fraction(2), Fraction(3, 2), Fraction(5, 2)):
        g = solve_balance(d, F, d + 1)
        ok3 &= g == F - Fraction(d + 1, 2)
# the same bookkeeping on the scalar kinetic term (1/2) int d^{d+1}x (d phi)^2:
# 2([phi] + 1) - (d + 1) = 0  =>  [phi] = (d - 1)/2 -- the standard answer, e.g. 1 at d = 3.
for d in range(0, 13):
    phi = (Fraction(d + 1) - 2) / 2
    ok3 &= phi == Fraction(d - 1, 2)
ok3 &= (Fraction(3 - 1, 2) == 1)
check("G3", ok3,
      "the general formula [g] = [F] - (d+1)/2 for five field-strength dimensions and d = 0..12 -- "
      "[F] = 2 is one instantiation, visible as such -- and the identical bookkeeping applied to "
      "the scalar kinetic term gives [phi] = (d-1)/2, the standard value, 1 at d = 3. Lean's "
      "`coupling_dim_general`")

# ---------------------------------------------------------------- G4  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'GaugeDimension.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('coupling_dim_general', 'theorem_16', 'off_by_one', 'off_by_one_never_agrees',
         'dimensionless_at_three', 'not_dimensionless_at_four')
ok4 = 'import OIBridge.GaugeDimension' in root
ok4 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok4 &= re.search(r'(?m)^axiom ', body) is None
ok4 &= all(f'theorem {n}' in src for n in NAMES)
ok4 &= all(f'#print axioms {n}' in src for n in NAMES)
ok4 &= 'native_decide' not in body
# the physical input must be a HYPOTHESIS, not a definition of [g]
ok4 &= 'def Balance' in src
ok4 &= '-2 * g + 2 * F - (d + 1) = 0' in src
tw = src[src.index('theorem theorem_16'):]
tsig = tw[:tw.index(':= by')]
ok4 &= 'h : Balance d g 2' in tsig
ok4 &= 'g = (3 - d) / 2' in tsig and '(g = 0 ↔ d = 3)' in tsig
# and no definition anywhere that hard-codes the answer
ok4 &= 'def' not in tsig
for line in src.split('\n'):
    if line.strip().startswith('def') and '(3 - ' in line:
        ok4 = False
check("G4", ok4,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The "
      f"physical input is the hypothesis `Balance d g 2` -- the dimensionless action with its "
      f"(d+1)-dimensional measure and [F] = 2 -- and no definition hard-codes (3 - d)/2, so the "
      f"kernel certifies the bookkeeping and not the notation")

print()
print('     [scope] Settled in Lean: [SM] Theorem 16 in full -- [g] = (3 - d)/2 and the')
print('     dimensionless-iff-d=3 clause -- derived from the dimension balance of the Yang-Mills')
print('     action rather than defined, with the general-[F] formula above it and the off-by-one')
print('     measure countercontrolled. NOT settled: the surrounding prose claims (renormalizability,')
print('     asymptotic freedom), which are cited results about d = 3 gauge theory, not statements')
print('     of this theorem.')
print()
print("gauge_dimension_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
