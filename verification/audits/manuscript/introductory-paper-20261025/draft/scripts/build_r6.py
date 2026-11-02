"""Introduction-r6.md = r5 + the edits required or recommended by the r5 reviews (sci REVIEW-r5, ed REVIEW-r5).

Each edit is an exact, uniquely matching replacement on r5, so every unchanged sentence stays byte-identical to r5.
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
log = []


def rep(tag, old, new):
    global t
    n = t.count(old)
    assert n == 1, (tag, n, old[:80])
    t = t.replace(old, new)
    log.append(tag)


# --- abstract: RC2 / sci N3 ---
rep("RC2", "it is stated here as one theorem. The Born exponent is not selected.",
    "it is stated here as one theorem. Each class contains the Markov laws, so representability does not distinguish "
    "a law with memory from one without, and the Born exponent is not selected.")

# --- §1.2: RC1 + sci N2 ---
rep("RC1/N2", "The paper develops one idea, OI, and two of its consequences: the foundation and its quantum-emergence "
    "results (§§2–3), and two applications, the cosmological constant (§4) and black-hole information (§5).",
    "The paper develops one idea, OI: its foundation and quantum-emergence results (§§2–3), and two of its "
    "consequences, for the cosmological constant (§4) and for black-hole information (§5).")

# --- §2.2: Calvo moved to §3.1; 't Hooft sentence deleted (cited in §6.2 item 8) ---
calvo = ("Calvo states a proof of the six axioms of textbook quantum mechanics from the single axiom that every physical "
         "system evolves according to a generally indivisible stochastic law [Cal26]; Theorem 1 is a correspondence "
         "between classes of law and derives no such axioms.")
rep("flow: Calvo out of §2.2", calvo + "\n\n", "")
rep("flow: 't Hooft l.74 deleted", "'t Hooft has argued that quantum mechanics may serve as a tool for analysing a "
    "system that is classical at its core, and has discussed how such a view can be reconciled with Bell's theorem "
    "[tH14].\n\n", "")
rep("flow: Calvo into §3.1",
    "not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)].\n",
    "not why a physical system exhibits a law with memory [Main §3.4, Remark (representation, not explanation)]. "
    + calvo + "\n")

# --- §2.4: ed nit (F3 phrasing) ---
rep("ed nit F3", "The written proof is [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06].",
    "The written proof is in [Main §3.4, Theorem (unavoidable hidden predictive memory)]; see also [CT06].")

# --- §2.5: connective for the stochastic-inverse lemma ---
rep("flow: l.110 connective", "(machine-checked). On a fixed finite reversible substratum, history readback forces",
    "(machine-checked). With this lemma, on a fixed finite reversible substratum history readback forces")

# --- §3.5: trim T (l.150) and Bell split (l.152) ---
rep("trim T l.150", "The origin of the quadratic Born exponent is open: $p=|U|^2$ is part of the definition of "
    "$\\mathsf Q_K$ and is not selected by the correspondence (§2.3) [Main §3.4; Bar26, Thm 3.1].",
    "The origin of the quadratic Born exponent, which the correspondence does not select (§2.3), is open [Main §3.4; "
    "Bar26, Thm 3.1].")
rep("flow: Bell split", "must give up one of the two; the framework keeps measurement independence",
    "must give up one of the two. The framework keeps measurement independence")

# --- §4: RC3, bridge, C1 ---
rep("RC3 mismatch named", "gives a vacuum energy density some 120 orders of magnitude above the observed one, the "
    "exact power depending", "gives a vacuum energy density some 120 orders of magnitude above the observed one (the "
    "mismatch), the exact power depending")
rep("bridge §4 + RC3 proposal stated", "In OI the zero-point sum of the emergent quantum description and the "
    "effective cosmological constant are defined",
    "In OI (§1.1) the zero-point sum of the emergent quantum description (§§2–3) and the effective cosmological "
    "constant are defined")
rep("RC3 proposal before its content", "energy; the proposal's content lies in how the two levels couple to "
    "geometry.", "energy; OI's proposal is that the mismatch requires no cancellation, and its content lies in how "
    "the two levels couple to geometry.")
rep("RC3 symbols (completions)", "$\\mathcal G_{\\mu\\nu}=8\\pi G\\,(T^{\\rm cl}_{\\mu\\nu}-\\rho_C\\,g_{\\mu\\nu})$ "
    "[GR §6.2].", "$\\mathcal G_{\\mu\\nu}=8\\pi G\\,(T^{\\rm cl}_{\\mu\\nu}-\\rho_C\\,g_{\\mu\\nu})$, with "
    "$\\mathcal G_{\\mu\\nu}$ the Einstein tensor, $T^{\\rm cl}_{\\mu\\nu}$ the classical stress-energy of the "
    "substratum and $\\rho_C$ the energy density of the offset [GR §6.2].")
rep("RC3 symbols (target form)", "\\mathcal F[g,T]\\,g_{\\mu\\nu})$, with the classical stress-energy of the "
    "substratum as source,", "\\mathcal F[g,T]\\,g_{\\mu\\nu})$, with $E_{\\mu\\nu}[g,\\mathrm{OI}]$ the "
    "gravitational side still to be derived, $\\mathcal F[g,T]$ a scalar functional of the metric and the "
    "stress-energy, and the classical stress-energy of the substratum as source,")
rep("RC3 Hubble rate", "The scale $\\rho\\sim H^2/G$ is the Friedmann normalization of the total density",
    "The scale $\\rho\\sim H_{\\rm Hub}^2/G$, with $H_{\\rm Hub}$ the Hubble rate, is the Friedmann normalization of "
    "the total density")
rep("C1", "and of vacuum-energy sequestering, which extends to the vacuum energy of phase transitions [KP14]",
    "and of vacuum-energy sequestering, which also renders contributions from phase transitions small [KP14]")

# --- §5: bridge, RC4 ---
rep("bridge §5", "Under OI two questions separate: whether information is conserved",
    "Because the dynamics of OI is a bijection observed through a partition (§1.1), two questions separate: whether "
    "information is conserved")
rep("RC4 accessible advantage at first use", "exhibit bijections with no accessible advantage and non-injective "
    "maps with exact recovery [BHa].", "exhibit bijections with no accessible advantage, that is, no gain in success "
    "probability over a blind guess, and non-injective maps with exact recovery [BHa].")
rep("RC4 gloss removed at second use", "1,376 give zero accessible advantage, the gain in success probability over "
    "a blind guess, for a binary message", "1,376 give zero accessible advantage for a binary message")
rep("RC4 H-scramble defined at first use", "only through the scrambling hypothesis H-scramble, which no bijection "
    "satisfies from a definite configuration with configuration-aligned cuts [BHb, C1, C6(a)–(b)]. H-scramble "
    "posits equidistribution of the orbit on an energy shell. The mean entropy",
    "only through the scrambling hypothesis H-scramble, equidistribution of the orbit over pure states on an energy "
    "shell, which no bijection satisfies from a definite configuration with configuration-aligned cuts [BHb, C1, "
    "C6(a)–(b)]. The mean entropy")
rep("RC4 timescales", "since $t_{\\rm evap}/\\tau_B^D \\ge 10^{57}$ at 30 solar masses over the assumed parameter "
    "intervals [BHa, item F].", "since $t_{\\rm evap}/\\tau_B^D \\ge 10^{57}$ at 30 solar masses over the assumed "
    "parameter intervals, with $t_{\\rm evap}$ the evaporation time and $\\tau_B^D$ the $D$-sector timescale [GR App. "
    "A.5; BHa, item F].")

# --- §6 ---
rep("ed nit 'yet' (content-preserving form)", "no experiment yet distinguishes OI from standard quantum theory, and no "
    "memory-witness constraint is established", "no experiment distinguishing OI from standard quantum theory, and no "
    "memory-witness constraint, is established")
rep("trim T §6.2 item 4", "No resolution of the black-hole information problem: the Page curve of [GR App. A] needs "
    "H-scramble and the closure of the black hole and its radiation, in a pure joint state, over whole cycles; its "
    "stated value is established only for a full-product energy shell; and it gives a cycle average rather than a "
    "curve along one trajectory; the correspondence with islands is conjectural; the generalized second law is open; "
    "and the results of §5 concern finite toy models,",
    "No resolution of the black-hole information problem: the Page curve of [GR App. A] is not established (§5), and "
    "the results of §5 concern finite toy models,")
rep("C2 (settles ed RC5)", "The paper's results are the theorems and their scopes.",
    "What the paper states are the cited theorems and their scopes.")
rep("conclusion memory clause (from r4:249 s2)",
    "exactly the fixed-basis unitary Born laws. Exact operational quantum mechanics is reached only",
    "exactly the fixed-basis unitary Born laws; because the representation is universal, the discriminating content "
    "lies in memory, which every deterministic completion carries in its hidden state. Exact operational quantum "
    "mechanics is reached only")

rep("F1 reverted (outline: N-INT1 replaces the pointer)", "Exact operational quantum mechanics is reached only under "
    "conditions that OI alone does not imply (§3.2). The paper develops", "The paper develops")
# L1: drop the six *** rules inside the main text (editorial length variant L1)
head, sep, tail = t.partition("## Code, data and formal verification")
pre, sep0, body = head.partition("## Abstract")
n = body.count("\n***\n\n")
body = body.replace("\n***\n\n", "\n")
t = pre + sep0 + body + sep + tail
log.append(f"L1: {n} rules dropped")
open(dst, "w", encoding="utf-8").write(t)
print("applied", len(log), "edits:", "; ".join(log))
