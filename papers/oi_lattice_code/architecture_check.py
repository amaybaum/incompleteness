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
    (r"[Tt]wo independent routes|either alone sufficient|Either route alone suffices",
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
    (r"T_\{ij\}(\(t\))?[^.\n]{0,12}=[^.\n]{0,12}\|U_\{ij\}(\(t\))?\|\^2"
     r"|\|\\langle j\|e\^\{-i\\hat\{H\}t\}\|i\\rangle\|\^2 = T_\{ij\}",
     "the bare visible-space form is unavailable in general; the representation is the ancilla-dilated one (Main §3.1)",
     [r"undilated equality", r"is itself unistochastic", r"not in general unistochastic",
      r"trivial-ancilla (special )?case", r"discards phase information", r"ancilla-marginal level"],
     "such that $T_{ij}(t) = |U_{ij}(t)|^2$ on the visible space"),
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
    (rf"(Input|Scope|input)[^|\n]{{0,25}}\|[^|\n]{{0,20}}P{E}indivisible process"
     rf"|[Aa]ny P{E}indivisible process(?![^.\n]{{0,40}}nontrivial)",
     "membership in the source's class is not gated by P-indivisibility; (T) admits the process",
     [],
     "| Input | P-indivisible process on $\\mathcal{C}_V$ |"),
    (rf"C1{E}[-–]{E}C4[^.\n]{{0,50}}(jointly necessary|jointly sufficient|exactly the joint specification)"
     rf"|combination of the four conditions[^.\n]{{0,40}}(produces|yields)",
     "the equivalence is a dilation theorem; C4 coincides with the non-Markovianity clause and C1/C3 follow from it",
     [],
     "C1–C4 as jointly necessary for accessible non-Markovianity"),
    (r"(Hamiltonian|dynamics) is uniquely (fixed|determined)"
     r"|Up to this freedom, the dynamics is uniquely determined",
     "phase-locking fixes H only up to shift, rephasing and the antiunitary conjugation",
     [r"antiunitary", r"twofold ambiguity", r"full gauge"],
     "The Hamiltonian is uniquely fixed by the observable transition data."),
    (r"independent second route|second independent route"
     r"|rejects? the Barandes[^.\n]{0,60}must also reject Stinespring",
     "Stinespring independently secures the generic dilation layer only; the two routes share that bedrock",
     [],
     "Stinespring dilation is an independent second route"),
    (r"reproduces all quantum[- ]mechanical predictions|reproduces all of quantum mechanics",
     "the operational instrument algebra is open; not all quantum predictions are delivered",
     [],
     "the framework reproduces all quantum-mechanical predictions"),
    (r"measurement[- ]independence preservation|preservation of measurement independence",
     "measurement independence is not imposed at the substratum level; it is an operational target",
     [],
     "the framework's measurement-independence preservation distinguishes it"),
    (rf"P{E}indivisibility required for (QM|quantum)|requires? P{E}indivisibility[^.\n]{{0,30}}for (QM|quantum)",
     "P-indivisibility is not required for a quantum representation (Main §3.4's diagonal-Hamiltonian counterexample)",
     [],
     "contradicting the P-indivisibility required for QM"),
    (rf"C1{E}[-–]{E}C4 imply quantum mechanics|C1{E}[-–]{E}C4[^.\n]{{0,30}}(imply|produce) (quantum mechanics|QM)",
     "C4's readback implies accessible non-Markovianity; the quantum representation is supplied separately under (T)",
     [],
     "C1–C4 imply quantum mechanics"),
    (r"not to be a permutation — equivalent to non-trivial coupling"
     r"|non-permutation[^.\n]{0,40}equivalent to[^.\n]{0,30}coupling",
     "the non-permutation witness is not equivalent to C1",
     [r"not equivalent to C1", r"does not by itself force"],   # negation-aware
     "requires $T$ not to be a permutation — equivalent to non-trivial coupling"),
    (r"non-Markovianity\}?\s*\\iff\s*\\text\{a per-horizon finite reversible deterministic realization exists"
     r"|accessible non-Markovianity[^.\n]{0,40}\\iff[^.\n]{0,60}realization exists(?![^.\n]{0,80}readback)",
     "the realization-exists form is FALSE without readback on the right-hand side: Markov laws have realizations too",
     [r"is \*\*false\*\*", r"does NOT license"],
     "accessible non-Markovianity \\iff \\text{a per-horizon finite reversible deterministic realization exists}"),
    (rf"P{E}indivisibility is mathematically equivalent to quantum mechanics",
     "P-indivisibility governs nontriviality of the representation, not its existence",
     [],
     "P-indivisibility is mathematically equivalent to quantum mechanics"),
    # ---- b119 families: encode the S ⟺ D ⟺ Q_fb architecture, not merely police old errors ----
    (rf"non{E}Markovianity[^.\n]{{0,80}}(finite{E}horizon{E})?reversible( deterministic)?{E}realizability",
     "bare reversible realizability is universal (the process dilation realizes Markov laws too); the licensed universal statement pairs non-Markovianity with unavoidable readout-relevant hidden memory",
     [r"is \*\*false\*\*", r"does NOT license", r"retired as false"],
     "the in-house equivalence between accessible non-Markovianity and finite-horizon reversible realizability"),
    (rf"QM is not merely{E}\*?compatible|[Qq]uantum mechanics is not merely{E}\*?compatible",
     "the equivalence is scoped: finite-horizon fixed-basis observable laws (S ⟺ D ⟺ Q_fb); unscoped QM-⟺-embedded-observation overstates the theorem",
     [r"finite-horizon fixed-basis", r"observable law"],
     "QM is not merely *compatible with* embedded observation — it is *equivalent to* it."),
    (rf"load{E}bearing for one result only|correspondence[^.\n]{{0,50}}load{E}bearing for[^.\n]{{0,50}}necessity|Barandes[^.\n]{{0,60}}load{E}bearing for the necessity",
     "the representation is internal (permutation unitary, §3.4); the import retains the compressed (≤ n³) form and its interpretive apparatus under (T), nothing gating existence or necessity",
     [],
     "The correspondence [11, 12] is load-bearing for one result only: the necessity direction"),
    (rf"P{E}indivisibility biconditional|QM[^.\n]{{0,25}}(\\Leftrightarrow|⇔|\\iff)[^.\n]{{0,25}}P{E}indivisib",
     "there is no QM ⇔ P-indivisibility biconditional in the architecture: membership and representation are P-indivisibility-free, and nontriviality is the M_t > 0 sector",
     [],
     "the QM $\\Leftrightarrow$ P-indivisibility biconditional powers (ii) $\\implies$ (i)"),
    (rf"frozen{E}bath[^.\n]{{0,60}}enables[^.\n]{{0,40}}quantum",
     "the representation is universal (S ⟺ D ⟺ Q_fb); the bath condition governs the accessible memory sector, and persistence — not frozenness — is the requirement (fastbath_probes.py)",
     [],
     "this frozen-bath condition is what enables quantum mechanics"),
    (rf"(failure|violating)[^.\n]{{0,60}}destroys the framework'?s emergent quantum|destroys the framework'?s emergent quantum mechanics",
     "under S ⟺ D ⟺ Q_fb the representation exists regardless; condition failure removes the memory-bearing sector (accessible non-Markovianity), not the representation",
     [],
     "violating the condition destroys the framework's emergent quantum mechanics"),
    (rf"(unitarily evolving |quantum |unitary )representation is imported|representation is supplied by an external theorem|quantum representation for processes in the correspondence'?s class",
     "existence of the representation is internal by the permutation unitary; only the compressed (≤ n³) form and interpretive apparatus are imported, under (T)",
     [r"compressed", r"no longer"],
     "The unitarily evolving representation is imported, applies across the correspondence's class"),
    (rf"C2 condition states that the hidden sector evolves much more slowly|C2[^.\n]{{0,50}}necessary for P{E}indivisibility",
     "(C2) is memory persistence with two named forms (Main §1.3): (C2-slow) is one mechanism, its necessity the conditional physical-memory theorem — not a P-indivisibility precondition",
     [],
     "The C2 condition states that the hidden sector evolves much more slowly than the visible sector"),
    (rf"P{E}indivisible members[^.\n]{{0,80}}admit the quantum representation",
     "the representation attaches to the whole class (S ⟺ D ⟺ Q_fb); P-indivisibility governs recurrence-scale nontriviality, and the discriminating sector is M_t > 0",
     [],
     "the P-indivisible members of that class, the empirically realized ones, admit the quantum representation"),
    (r"four conditions are exactly the joint specification",
     "C4 is primitive with C1/C3 its consequences and C2 a physical-regime premise; 'exactly the joint specification' overstates joint necessity",
     [],
     "The framework's four conditions are exactly the joint specification of \"embedded laboratory observer"),
    (r"only kind of observer whose dynamics is quantum",
     "the representation is universal at the observable-law level; what the observer kind selects is the memory-bearing (M_t > 0) sector",
     [],
     "the only kind of observer whose dynamics is quantum mechanics"),
    (r"\(C2\) as the retention required",
     "cite (C2-structural) for the retention clause; unqualified (C2) conflates structural retention with the τ_S ≪ τ_B form (Main §1.3)",
     [],
     "(C2) as the retention required by (b)"),
    # ---- b120 families: near-miss formulations of the retired dichotomy, found by sweep after b119 ----
    (r"structurally distinct from QM|violating the condition destroys QM",
     "P-divisible/Markovian laws lie inside Q_fb (S ⟺ D ⟺ Q_fb); condition failure removes the memory-bearing sector, not quantum representability",
     [],
     "violating C2 produces Markovian dynamics, which is structurally distinct from QM"),
    (rf"QM requires{E}(slow{E}bath|coupling|capacity|readback)",
     "state the necessity theorems in the memory currency (accessible non-Markovianity / physical memory), not as requirements of QM — the representation is universal",
     [],
     "QM requires slow bath"),
    (rf"P{E}indivisibility licenses",
     "(T) alone licenses the imported compressed representation; P-indivisibility gates neither membership nor representation (Main §3.4)",
     [],
     "P-indivisibility licenses the imported stochastic–quantum representation"),
    (rf"representation{E}(is{E})?supplied across the correspondence|attach\w*{E}to (its|the) correspondence['\u2019]s class",
     "existence of the representation is internal and universal; only the compressed (≤ n³) form is class-scoped under (T) — say 'compressed'",
     [r"compressed"],
     "the quantum representation is supplied across the correspondence's class under (T)"),
    (rf"QM for processes in the correspondence|correspondence['\u2019]s class \u2192{E}quantum representation",
     "the representation is universal (S ⟺ D ⟺ Q_fb); the class-scoped object is the compressed form",
     [],
     "QM for processes in the correspondence's class"),
    (rf"P{E}indivisibility requires[^.\n]{{0,25}}(τ_S|\\tau_S)",
     "the τ_S ≪ τ_B necessity is conditional on the mixing hypothesis (conditional physical-memory theorem); fast non-mixing baths retain records (fastbath_probes.py)",
     [r"mixing class", r"conditional"],
     "Contrapositive: P-indivisibility requires τ_S ≪ τ_B."),
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
            window = text[max(0, m.start()-160):m.start()+160]   # b114: qualifying language often sits a clause away
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
