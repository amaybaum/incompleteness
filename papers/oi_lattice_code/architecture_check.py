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
    (r"(does not admit|lacks?|has no|is no)[^.\n]{0,45}(density[- ]matrix|Stinespring|Hilbert space)"
     r"|some but not all[^.\n]{0,45}Stinespring",
     "every stochastic T admits the one-step ancilla dilation; representability is not what is partial",
     [r"no probability calculus", r"requires no Hilbert space, no Born rule",
      r"routed through the uniqueness clause", r"is not distinguished by lacking",
      r"Stinespring uniqueness"],
     "a partially-quantum process does not admit a density-matrix description"),
    (r"Markov chains are excluded|memoryless Markov chains are excluded|excludes? (ordinary )?Markov chains",
     "the source's class explicitly includes Markov chains as special cases",
     [],
     "ordinary memoryless Markov chains are excluded"),
    (r"(L\\u00fcders|Luders|Lüders)[^.\n]{0,60}(derived|delivered|follows)"
     r"|instrument algebra[^.\n]{0,40}(derived|delivered)"
     r"|multi-time predictions[^.\n]{0,40}(derived|delivered|are all)",
     "the operational instrument algebra is open; only the transition-statistics layer is delivered",
     # negation-aware: the corrected form states the NEGATIVE and must not self-trigger
     [r"are NOT all delivered", r"remains open"],
     "the Lüders update and multi-time predictions are derived"),
    (rf"(would not produce|cannot produce|no)[^.\n]{{0,45}}quantum[^.\n]{{0,45}}infinite substratum"
     rf"|infinite substratum[^.\n]{{0,60}}(would not produce|no longer produces|cannot produce)[^.\n]{{0,30}}quantum"
     rf"|finiteness[^.\n]{{0,60}}(makes|required for)[^.\n]{{0,40}}(account of )?quantum",
     "finiteness is load-bearing for the recurrence route only",
     [],
     "the framework would not produce quantum mechanics on an infinite substratum"),
    (r"the (four|4) structural conditions|four structural conditions",
     "C1, C3, C4 are the structural conditions; C2 is a physical-regime premise",
     [r"Juno", r"A_1 is fixed by", r"cubic geometric input"],
     "the framework's four structural conditions"),
    (rf"C2 \(slow bath\)|C2[^.\n]{{0,30}}slow bath\)",
     "C2 is memory persistence; slow bath is one realization",
     [],
     "C2 (slow bath) requires timescale separation"),
    (r"T_\{ij\}[^.\n]{0,12}=[^.\n]{0,12}\|U_\{ij\}\|\^2|Unitary with \$T_\{ij\} = \|U_\{ij\}\|\^2\$",
     "the bare visible-space form is unavailable in general; the representation is the ancilla-dilated one (Main §3.1)",
     [r"undilated equality", r"is itself unistochastic", r"not in general unistochastic"],
     "Output | Unitary with $T_{ij} = |U_{ij}|^2$"),
    (r"(follow|derived|delivered)[^.\n]{0,60}without independent postulates"
     r"|L\u00fcders rule[^.\n]{0,60}(quantum transcription|follows|is derived)",
     "the operational instrument algebra is open; the Lüders rule is not delivered by the characterization",
     [],
     "the further structures of operational quantum mechanics follow without independent postulates"),
    (r"exactly one self-consistent algorithm|the unique self-consistent algorithm",
     "the stochastic-to-quantum representation is explicitly non-unique (Main §3.1)",
     [],
     "there is exactly one self-consistent algorithm for making predictions"),
    (rf"frozen bath[^.\n]{{0,40}}(enables|is required|makes)|only[^.\n]{{0,40}}slow bath[^.\n]{{0,40}}(see|observe)[^.\n]{{0,30}}quantum",
     "C2 is record persistence with timely readback; fast conserved dynamics qualify (fastbath_probes.py)",
     [],
     "the frozen bath enables quantum mechanics"),
    (rf"P{E}indivisibility[^.\n]{{0,70}}(produces|yields|gives)[^.\n]{{0,40}}(quantum correlations|Tsirelson|Bell)"
     rf"|Tsirelson[^.\n]{{0,60}}from[^.\n]{{0,30}}P{E}indivisibility",
     "the Tsirelson value is imported for the causally local indivisible construction, not generic P-indivisibility",
     [],
     "P-indivisibility produces quantum correlations up to Tsirelson"),
    (r"(framework|it) (preserves|satisfies) measurement independence",
     "measurement independence is not imposed at the substratum level; it is an operational target",
     [r"does not impose", r"not imposed"],
     "the framework preserves measurement independence"),
    (rf"phase[- ]lock\w*[^.\n]{{0,70}}unique\w*",
     "phase-locking fixes H only up to shift, rephasing and the antiunitary conjugation H -> -H*",
     [r"antiunitary", r"-\\hat\{H\}\^\*", r"twofold ambiguity"],
     "phase-locking determines the Hamiltonian uniquely"),
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

LIMIT = len(violations) if os.environ.get("OI_ARCH_FULL") else 25
for f, ln, hit, why in violations[:LIMIT]:
    print(f"ARCHITECTURE VIOLATION  {f}:{ln}  '{hit}'\n    -> {why}")
if len(violations) > LIMIT: print(f"    … and {len(violations)-LIMIT} more (set OI_ARCH_FULL=1 for all)")
print(f"architecture_check: {len(INVARIANTS)} invariant(s), {len(violations)} violation(s), "
      f"{len(selftest_failures)} self-test failure(s)")
sys.exit(1 if (violations or selftest_failures) else 0)
