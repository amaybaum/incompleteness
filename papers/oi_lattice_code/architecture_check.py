#!/usr/bin/env python3
# architecture_check.py — b107 (2026-08-13)
# The analogue of citation_check.py for CLAIMS rather than files. Three rounds of
# review in a row found the same defect: a local correction to the manuscript's
# architecture did not propagate, because sweeps match wordings and the same claim
# recurs in unrelated phrasings. This encodes the load-bearing architectural
# invariants as mechanical assertions, so the next occurrence fails the battery
# rather than the next review.
#
# Each invariant is a forbidden pattern with an explanation of what it violates.
# Exceptions are explicit and few; add one only with a reason, not to silence a hit.
import os, re, sys, glob

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
targets = sorted(glob.glob(os.path.join(root, "papers", "*.md"))) \
        + sorted(glob.glob(os.path.join(root, "book", "*.md"))) \
        + [os.path.join(root, "README.md")]

INVARIANTS = [
    (r"P-indivisible subclass",
     "the imported representation applies across the correspondence's class, not to a P-indivisible subclass",
     [r'does not apply only to a "P-indivisible subclass"']),
    (r"picks out processes in that class",
     "(T) is tuple instantiation, not an identification of the framework's criterion with the source's class",
     []),
    (r"treated in this paper as structural hypotheses",
     "C1-C4 are diagnostics of a realization, not hypotheses of the characterization",
     []),
    (r"three structural conditions[^.\n]{0,60}C1, C2, C3, C4|four structural conditions[^.\n]{0,40}C1, C2, C3\b",
     "condition count and enumeration disagree",
     []),
    (r"C1, C2, C3, C4, and C4",
     "duplicated condition in an enumeration",
     []),
    (r"P-indivisibility is mathematically equivalent to quantum mechanics",
     "P-indivisibility governs nontriviality of the representation, not its existence",
     []),
    (r"two independent routes|either alone sufficient|Either route alone suffices",
     "both routes reach only the transition-statistics layer; neither supplies the operational instrument algebra",
     # narrow, referent-specific exceptions: SM's hypercharge identity is obtained
     # by two independent routes (a different claim), and Appendix C quotes the
     # phrase in order to reject it.
     [r"hypercharge assignment", r'so \"either alone suf']),
    (r"requires a \*frozen\* hidden sector|hidden sector to evolve much more slowly",
     "C2 is memory persistence, not slow evolution (fastbath_probes.py)",
     []),
]

violations = []
for path in targets:
    if not os.path.exists(path): continue
    text = open(path, encoding="utf-8").read()
    for pattern, why, exceptions in INVARIANTS:
        for m in re.finditer(pattern, text):
            window = text[max(0, m.start()-80):m.start()+80]
            if any(re.search(e, window) for e in exceptions): continue
            line = text[:m.start()].count("\n") + 1
            violations.append((os.path.relpath(path, root), line, m.group(0)[:48], why))

for f, ln, hit, why in violations:
    print(f"ARCHITECTURE VIOLATION  {f}:{ln}  '{hit}'\n    -> {why}")
print(f"architecture_check: {len(INVARIANTS)} invariant(s), {len(violations)} violation(s)")
sys.exit(1 if violations else 0)
