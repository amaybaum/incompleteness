#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R7-RCH-T3: durable guard for the recurrence-tightness result note.

Pins the T3-A classification, exact full-period witness, controlling horizon, and the two
interpretive disclaimers that prevent the existential tightness result from being over-read as
physical inaccessibility or as an arbitrarily-large-horizon scaling theorem.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFICATION = HERE.parent
RESULT = VERIFICATION / "RECURRENCE-TIGHTNESS-RESULT.md"
PROBE = HERE / "recurrence_tightness_probe.py"

text = RESULT.read_text(encoding="utf-8")
probe = PROBE.read_text(encoding="utf-8")
flat = " ".join(text.split())

checks = []

def check(name, ok):
    checks.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")

required = (
    "**Target 3 — T3-A, tightness construction succeeds.**",
    "`mu_H = (1/2, 1/5, 1/10, 1/5)`",
    "`Gamma_0 = I`",
    "`Gamma_1 = B_(7/10)`",
    "`Gamma_2 = B_(3/5)`",
    "`Gamma_3 = I`",
    "`B_(7/10) * B_(3/4) = B_(3/5)`",
    "`Lambda = [[3,-2],[-2,3]]`",
    "The controlling horizon is exactly N_CR = 3",
    "`N_CR = 3`",
    "the frozen parent does not force a P-divisibility obstruction on some strictly shorter horizon `K < N_CR` in every realization",
    "It does **not** show that `N_CR` is always large or physically inaccessible; the exact witness here has `N_CR = 3`.",
    "No claim is made that arbitrarily large `N_CR` admits an analogous tight witness; that stronger scaling question was not preregistered in this round.",
    "that return-horizon statement is tight: all shorter horizons can remain P-divisible.",
)
for item in required:
    check("required: " + item[:56], item in text)

# Pin the exact witness in the independent arithmetic probe too, rather than guarding prose alone.
for item in ("Fraction(1, 2)", "Fraction(1, 5)", "Fraction(1, 10)",
             "Fraction(7, 10)", "Fraction(3, 5)", "Fraction(3, 4)"):
    check("probe witness: " + item, item in probe)

# Guard the interpretation rather than merely the vocabulary: the words "inaccessible" and
# "arbitrarily large" are allowed only inside the explicit disclaimers above.
for line in text.splitlines():
    low = line.lower()
    if "inaccessible" in low:
        check("inaccessible only in disclaimer", "does **not** show" in line and "N_CR = 3" in line)
    if "arbitrarily large" in low:
        check("scaling only in no-claim disclaimer", line.startswith("No claim is made that ") and "not preregistered" in line)

for bad in (
    "before recurrence",
    "accessible quantum",
    "nonclassicality is physically inaccessible",
    "`N_CR` is physically inaccessible",
    "`N_CR` is always large",
    "forces an obstruction on every shorter horizon",
    "forces P-indivisibility before the return",
):
    check("forbidden: " + bad, bad.lower() not in text.lower())

# The result must continue to distinguish microscopic order from the controlling visible return.
check("order/horizon distinction", "happen to coincide" in text and "do not identify those notions in general" in text)
check("publication boundary", "No new condition is named or adopted" in text and "does not silently edit the manuscript" in text)

ok = all(checks)
print(f"\nR7-RCH-T3: {'PASS' if ok else 'FAIL'} ({sum(checks)}/{len(checks)})")
raise SystemExit(0 if ok else 1)
