#!/usr/bin/env python3
# architecture_check.py — b107, strengthened at b110 (2026-08-13)
# The analogue of citation_check.py for CLAIMS. Encodes the manuscript's
# load-bearing architectural invariants as mechanical assertions.
#
# b110 lesson, recorded here because it cost a clean-but-false readout: the first
# version forbade the literal string "P-indivisible subclass" while the book wrote
# "*P-indivisible* subclass". Markdown emphasis defeated the regex and the guard
# reported zero violations while the corpus contradicted Main. A guard whose
# failure mode is SILENCE must be tested against the text it guards. Hence:
#   (a) patterns are emphasis- and hyphen-tolerant semantic families, not literals;
#   (b) every invariant carries a known-bad EXEMPLAR, and the guard fails if an
#       invariant does not match its own exemplar — a pattern that matches nothing
#       can no longer pass quietly.
import os, re, sys, glob

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
targets = sorted(glob.glob(os.path.join(root, "papers", "*.md"))) \
        + sorted(glob.glob(os.path.join(root, "book", "*.md"))) \
        + [os.path.join(root, "README.md")]

E = r"[*_`\s-]*"          # markdown emphasis / hyphen / space tolerance

INVARIANTS = [
    (rf"P{E}indivisib\w*{E}(subclass)",
     "the imported representation applies across the correspondence's class, not to a P-indivisible subclass",
     [r'does not apply only to a "P-indivisible subclass"', r"P-indivisible-subclass representation clause"],
     "the quantum representation attaches to the *P-indivisible* subclass"),
    (rf"P{E}indivisibility[^.\n]{{0,70}}(carries|produces|yields|gives|delivers)[^.\n]{{0,45}}quantum",
     "P-indivisibility governs nontriviality of the representation, not its existence",
     [],
     "P-indivisibility carries the quantum representation"),
    (r"picks out processes in that class",
     "(T) is tuple instantiation, not an identification of the framework's criterion with the source's class",
     [],
     "the criterion picks out processes in that class"),
    (rf"C1{E}[^.\n]{{0,60}}(implies|forces)[^.\n]{{0,45}}permutation"
     rf"|permutation[^.\n]{{0,60}}(follows from|because of|by){E}C1",
     "C1 is non-zero coupling; a non-permutation one-step matrix is a separate witness, not a consequence of C1",
     [],
     "T is not a permutation matrix (this follows from C1)"),
    (r"lack[s]?[^.\n]{0,90}(Stinespring|density-matrix|density matrix|Hilbert[- ]space unitary)",
     "every stochastic T admits the one-step ancilla dilation (Main §3.1); no process lacks a representation at that layer",
     [],
     "the partially-quantum process lacks the structure required for Stinespring dilation"),
    (r"treated in this paper as structural hypotheses",
     "C1-C4 are diagnostics of a realization, not hypotheses of the characterization",
     [],
     "the four conditions are treated in this paper as structural hypotheses"),
    (r"C1, C2, C3, C4, and C4",
     "duplicated condition in an enumeration",
     [],
     "C1, C2, C3, C4, and C4 therefore produce"),
    (r"two independent routes|either alone sufficient|Either route alone suffices",
     "both routes reach only the transition-statistics layer; neither supplies the operational instrument algebra",
     [r"hypercharge assignment", r'so \\?"either alone suf'],
     "the bridge is established by two independent routes"),
    (rf"requires a{E}\*?frozen\*?{E}hidden sector|hidden sector to evolve much more slowly",
     "C2 is memory persistence, not slow evolution (fastbath_probes.py)",
     [],
     "quantum mechanics requires a *frozen* hidden sector"),
    (rf"(?<!P-)(?<!P){E}\bindivisible{E}subclass",
     "the source's class has no distinguished subclass; use 'the source's finite-configuration class'",
     [],
     "representability following for the indivisible subclass"),
    (r"is no Hilbert space on which|lacks?[^.\n]{0,30}Hilbert space|does not have[^.\n]{0,40}density-matrix description|some but not all[^.\n]{0,40}Stinespring",
     "every stochastic T admits the one-step ancilla dilation; representability is not what is partial",
     [],
     "there is no Hilbert space on which the system's dynamics is unitary"),
    (rf"(finiteness|infinite substratum)[^.\n]{{0,80}}(required|necessary|not produce)[^.\n]{{0,45}}(quantum|P{E}indivisib)",
     "finiteness is load-bearing for the recurrence route only; readback has its own finite-horizon route",
     [],
     "finiteness is required for quantum mechanics"),
    (rf"C2[^.\n]{{0,50}}(must|necessary)[^.\n]{{0,50}}slow|C2[^.\n]{{0,40}}timescale[^.\n]{{0,40}}slower[^.\n]{{0,30}}necessary",
     "C2 is memory persistence; slow evolution is one sufficient mechanism, not the condition",
     [],
     "C2 requires that the hidden sector must have slow dynamics"),
    (rf"P{E}indivisibility is mathematically equivalent to quantum mechanics",
     "P-indivisibility governs nontriviality of the representation, not its existence",
     [],
     "P-indivisibility is mathematically equivalent to quantum mechanics"),
]

# --- self-test: every invariant must match its own known-bad exemplar ---
selftest_failures = [why for pat, why, _, ex in INVARIANTS if not re.search(pat, ex)]
for why in selftest_failures:
    print(f"SELF-TEST FAILURE: an invariant does not match its own exemplar -> {why}")

violations = []
for path in targets:
    if not os.path.exists(path): continue
    text = open(path, encoding="utf-8").read()
    for pattern, why, exceptions, _ in INVARIANTS:
        for m in re.finditer(pattern, text):
            window = text[max(0, m.start()-90):m.start()+90]
            if any(re.search(e, window) for e in exceptions): continue
            line = text[:m.start()].count("\n") + 1
            violations.append((os.path.relpath(path, root), line, re.sub(r"\s+", " ", m.group(0))[:60], why))

for f, ln, hit, why in violations[:25]:
    print(f"ARCHITECTURE VIOLATION  {f}:{ln}  '{hit}'\n    -> {why}")
if len(violations) > 25: print(f"    … and {len(violations)-25} more")
print(f"architecture_check: {len(INVARIANTS)} invariant(s), {len(violations)} violation(s), "
      f"{len(selftest_failures)} self-test failure(s)")
sys.exit(1 if (violations or selftest_failures) else 0)
