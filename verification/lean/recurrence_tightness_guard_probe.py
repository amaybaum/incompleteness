#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R7-RCH-T3: durable guard for the recurrence-tightness result note.

Pins the T3-A classification, exact full-period witness, controlling horizon, and the two
interpretive disclaimers that prevent the existential tightness result from being over-read as
physical inaccessibility or as an arbitrarily-large-horizon scaling theorem.

The guard includes three negative controls so it cannot pass vacuously: weakening the
inaccessibility disclaimer, replacing the no-scaling disclaimer by a positive scaling claim, or
changing the pinned horizon must each make validation fail.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFICATION = HERE.parent
RESULT = VERIFICATION / "RECURRENCE-TIGHTNESS-RESULT.md"
PROBE = HERE / "recurrence_tightness_probe.py"

text = RESULT.read_text(encoding="utf-8")
probe = PROBE.read_text(encoding="utf-8")

REQUIRED = (
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

PROBE_REQUIRED = (
    "MU = (Q(1, 2), Q(1, 5), Q(1, 10), Q(1, 5))",
    "B7 = B(Q(7, 10))",
    "B6 = B(Q(3, 5))",
    "B34 = B(Q(3, 4))",
    'checks.append(("N_CR=3", G[2] != I and G[3] == I))',
    'checks.append(("P-divisible for every K<3"',
    'checks.append(("P-indivisible at K=3"',
)

# The two anti-overclaim disclaimers necessarily name the vocabulary they disclaim, and both are
# REQUIRED verbatim above. Scanning them for forbidden substrings would make the guard
# unsatisfiable, since the only way to pass would be to delete the protection itself. The forbidden
# scan therefore runs over the note with exactly these sentences excised. They cannot conceal an
# overclaim: their presence, verbatim, is separately required, and the structural check below
# refuses any protected sentence that is not also a required one.
PROTECTED = (
    "It does **not** show that `N_CR` is always large or physically inaccessible; the exact witness here has `N_CR = 3`.",
    "No claim is made that arbitrarily large `N_CR` admits an analogous tight witness; that stronger scaling question was not preregistered in this round.",
)

FORBIDDEN = (
    "before recurrence",
    "accessible quantum",
    "nonclassicality is physically inaccessible",
    "`N_CR` is physically inaccessible",
    "`N_CR` is always large",
    "forces an obstruction on every shorter horizon",
    "forces P-indivisibility before the return",
)


def validate(note: str, witness_probe: str):
    checks = []
    for item in REQUIRED:
        checks.append(("required: " + item[:60], item in note))
    for item in PROBE_REQUIRED:
        checks.append(("probe witness: " + item[:60], item in witness_probe))

    # The vocabulary is allowed only in the explicit anti-overclaim sentences.
    for line in note.splitlines():
        low = line.lower()
        if "inaccessible" in low:
            checks.append(("inaccessible only in disclaimer",
                           "does **not** show" in line and "N_CR = 3" in line))
        if "arbitrarily large" in low:
            checks.append(("scaling only in no-claim disclaimer",
                           line.startswith("No claim is made that ") and "not preregistered" in line))

    # An exemption may never be widened into a hiding place: every protected sentence must itself
    # be required verbatim, so excising it cannot remove text the note is free to change.
    checks.append(("protected disclaimers are themselves required",
                   all(p in REQUIRED for p in PROTECTED)))

    scan = note
    for protected in PROTECTED:
        scan = scan.replace(protected, "")
    for bad in FORBIDDEN:
        checks.append(("forbidden: " + bad, bad.lower() not in scan.lower()))

    checks.append(("order/horizon distinction",
                   "happen to coincide" in note and "do not identify those notions in general" in note))
    checks.append(("publication boundary",
                   "No new condition is named or adopted" in note and "does not silently edit the manuscript" in note))
    return checks


def all_ok(checks):
    return all(ok for _, ok in checks)


checks = validate(text, probe)
for name, ok in checks:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")

# Non-vacuity controls: each deliberate regression must be rejected by the same validator.
weakened_accessibility = text.replace(
    "It does **not** show that `N_CR` is always large or physically inaccessible; the exact witness here has `N_CR = 3`.",
    "It shows that `N_CR` is physically inaccessible.",
)
positive_scaling = text.replace(
    "No claim is made that arbitrarily large `N_CR` admits an analogous tight witness; that stronger scaling question was not preregistered in this round.",
    "Arbitrarily large `N_CR` admits an analogous tight witness.",
)
wrong_horizon = text.replace("The controlling horizon is exactly N_CR = 3", "The controlling horizon is exactly N_CR = 4")

# The forbidden scan exempts the two protected disclaimers. These two controls prove that exemption
# is narrow: an overclaim placed anywhere else is still caught, and a disclaimer reworded so that it
# is no longer the protected sentence verbatim loses the exemption along with the protection.
smuggled_elsewhere = text.replace(
    "## Publication boundary",
    "## Publication boundary\n\nThis shows nonclassicality is physically inaccessible.\n",
)
reworded_disclaimer = text.replace(
    PROTECTED[0],
    "It does not really show that `N_CR` is always large.",
)

negative_controls = (
    ("negative control: accessibility overclaim fires", not all_ok(validate(weakened_accessibility, probe))),
    ("negative control: scaling overclaim fires", not all_ok(validate(positive_scaling, probe))),
    ("negative control: horizon mutation fires", not all_ok(validate(wrong_horizon, probe))),
    ("negative control: overclaim outside the exemption fires", not all_ok(validate(smuggled_elsewhere, probe))),
    ("negative control: reworded disclaimer loses the exemption", not all_ok(validate(reworded_disclaimer, probe))),
)
for name, ok in negative_controls:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")

ok = all_ok(checks) and all(x for _, x in negative_controls)
total = len(checks) + len(negative_controls)
passed = sum(1 for _, x in checks if x) + sum(1 for _, x in negative_controls if x)
print(f"\nR7-RCH-T3: {'PASS' if ok else 'FAIL'} ({passed}/{total})")
raise SystemExit(0 if ok else 1)
