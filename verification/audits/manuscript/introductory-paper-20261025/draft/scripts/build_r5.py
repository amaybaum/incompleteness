"""Assemble Introduction-r5.md from r4's reviewed lines and design r7's permitted sentences.

Every r4 sentence is taken from the r4 file by line number and checked to be present verbatim, so that a carried
sentence cannot drift. New sentences are literal strings below, each tagged in CHANGES-r5.md.
"""
import sys

r4_path, out_path = sys.argv[1], sys.argv[2]
R4 = open(r4_path, encoding="utf-8").read().split("\n")


def L(n):
    return R4[n - 1]


def seg(n, start, end=None):
    """Substring of r4 line n from `start` (inclusive) up to `end` (exclusive, or end of line)."""
    line = L(n)
    i = line.index(start)
    j = line.index(end, i) if end else len(line)
    return line[i:j]


def sub(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


out = []
A = out.append

# Title block (r4:1-8)
for n in range(1, 9):
    A(L(n))
A("")
A("## Abstract")
A("")
ab = L(12)
s123 = seg(12, "Observational incompleteness (OI) is", " Each class contains")
s5 = seg(12, "The discriminating content concerns memory", " Exact finite operational")
s67 = seg(12, "Exact finite operational quantum mechanics", " In a bounded application")
NAB1 = ("Applied to the cosmological constant, OI places the zero-point sum and the effective cosmological constant at "
        "different levels of description; whether the zero-point sum sources curvature depends on covariant field "
        "equations that are not derived, so this is a proposal, not a resolution.")
NAB2 = ("Applied to black-hole information, finite computations separate the conservation of information under "
        "bijective dynamics from its recovery by an observer with restricted access; the framework's Page curve is not "
        "established, and the information problem is not resolved.")
A(" ".join([s123, "The Born exponent is not selected.", s5, s67, NAB1, NAB2]))
A("")
A("<!-- OWNER: R11. The abstract's black-hole sentence restates §5's claim A and H-scramble finding; it stands or "
  "falls with those paragraphs. -->")
A("")
A("***")
A("")

# 1. Introduction
A("## 1. Introduction: Observational Incompleteness and the emergence of quantum behaviour")
A("")
A("### 1.1 Embedded observation")
A("")
for n in (22, 24, 26):
    A(L(n)); A("")
A("### 1.2 The idea and its two consequences")
A("")
p30 = L(30)
p30 = sub(p30, "where the memory of a law must sit (§2.4) and what finite recurrence does with it (§3)",
          "where the memory of a law must sit (§2.4) and what finite recurrence does with it (§2.5)")
p30 = sub(p30, "that OI alone does not imply (§6).", "that OI alone does not imply (§3.2).")
NINT1 = ("The paper develops one idea, OI, and two of its consequences: the foundation and its quantum-emergence "
         "results (§§2–3), and two applications, the cosmological constant (§4) and black-hole information (§5). "
         "Neither application is a demonstrated resolution of its problem; §6 states what would decide each.")
p30 = sub(p30, " Proofs, the status ledger", " " + NINT1 + " Proofs, the status ledger")
A(p30); A("")
contrib_new = ("**Contributions.** The paper claims no new theorem or physical result; its contribution is expository. "
               "It presents the established mathematical results of OI together, separates the mathematical "
               "correspondence from its physical interpretation, and states two consequences with their conditions "
               "and limitations. The black-hole results of §5 are reported from unpublished repository research "
               "records [BHa; BHb], with written proofs and exact or exhaustive checks, whose novelty has not been "
               "established.")
rest32 = seg(32, "The components of Theorem 1 are known")
rest32 = sub(rest32, "The recurrence argument of §3 combines", "The recurrence argument of §2.5 combines")
rest32 = sub(rest32, "The results of §6.1–§6.2 are proved in", "The results of §3.2–§3.3 are proved in")
A(contrib_new + " " + rest32); A("")
A(L(34)); A("")
A(L(36)); A("")
A("***"); A("")

# 2. Theoretical foundation
A("## 2. Theoretical foundation: the established results and their assumptions")
A("")
A("This section defines three classes of finite-horizon law, shows that they coincide, identifies what the "
  "coincidence leaves (where a law's memory must sit), and states what finite recurrence does with that memory. Each "
  "result is stated with its reference; the proofs are in the cited papers.")
A("")
for n in range(44, 55):
    A(L(n))
A("")
A("### 2.2 The finite-horizon correspondence")
A("")
for n in range(58, 65):
    A(L(n))
A("")
A("**Realization.** For $\\mathsf S_K\\subseteq\\mathsf D_K$ the realization stores a sampled trajectory, with a "
  "clock, in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); "
  "EGGH26, Prop. 13]. For a law with rational probabilities, a realization whose hidden prior is independent of "
  "$x_0$ also exists [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper, with exact "
  "probes.")
A("")
A("**Quantum representation.** For $\\mathsf D_K\\subseteq\\mathsf Q_K$ the representation is the permutation "
  "unitary $U_\\varphi|x,h\\rangle=|\\varphi(x,h)\\rangle$, read out in the configuration basis at every step "
  "[Main §3.4]; $\\mathsf Q_K\\subseteq\\mathsf S_K$ is the Born rule.")
A("")
A(L(70)); A("")
A(L(72)); A("")
A("'t Hooft has argued that quantum mechanics may serve as a tool for analysing a system that is classical at its "
  "core, and has discussed how such a view can be reconciled with Bell's theorem [tH14].")
A("")
for n in range(74, 81):
    A(L(n))
A("")
for n in range(82, 91):
    A(L(n))
A("")
p92 = seg(92, "(a)–(c) are machine-checked", " The proof is the data-processing")
A(p92 + " The written proof is [Main §3.4, Theorem (unavoidable hidden predictive memory); CT06].")
A("")
A("**Corollary** (proved on paper [Main §1.5]). $M_t>0$ holds exactly when every faithful realization carries "
  "readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward "
  "direction rests on Theorem 2(a) in each realization; the converse on Theorem 2(a) in one realization, which "
  "Theorem 1 supplies (`S_imp_D`); both use the standard vanishing criterion for conditional mutual information "
  "[CT06], which, like the time-$t$ identification, is not machine-checked.")
A("")
p96 = sub(L(96), "\\ge p_0\\delta^2/\\ln2$, by Pinsker", "\\ge p_0\\delta^2/\\ln2$ (in bits), by Pinsker")
A(p96); A("")
A(L(98)); A("")
A("### 2.5 Recurrence and indivisibility")
A("")
A(L(108)); A("")
A(L(110)); A("")
A("Theorem 3 is machine-checked in its rooted form, and Doukas states the same overlap-and-return argument "
  "concurrently [Dou26, Prop. 1]. " + seg(112, "Monotone distance is necessary"))
A("")
s114_1 = sub(seg(114, "A stochastic matrix with", " On a fixed finite"), "A stochastic matrix", "A finite square stochastic matrix")
s114_last = seg(114, "The conclusion is machine-checked")
A(s114_1 + " On a fixed finite reversible substratum, history readback forces indivisibility somewhere in the "
  "recurrence cycle [Main §2.3, Theorem (history readback + finite recurrence implies indivisibility)]. " + s114_last)
A("")
A("Appendix B works a minimal model of Theorem 3 with six hidden states, a process with memory but no short-window "
  "indivisibility, and the smallest realization of Theorem 3, a two-card game, with its classical and quantum scope.")
A("")
A("***"); A("")

# 3. Quantum emergence
A("## 3. Quantum emergence: what is demonstrated, and what remains open for equivalence with quantum mechanics")
A("")
A("### 3.1 What is demonstrated")
A("")
A(sub(sub(L(118), "short-window indivisibility (§4.2).", "short-window indivisibility (Appendix B)."), "The indivisibility of §3.1 is global", "The indivisibility of §2.5 is global"))
A("")
A(L(120)); A("")
A(L(122)); A("")
A("### 3.2 From the correspondence to operational quantum mechanics")
A("")
for n in (212, 214, 216, 218, 220):
    A(L(n)); A("")
A("### 3.3 The evolution relating two times is not selected")
A("")
A(L(224)); A("")
A(L(226)); A("")
A("### 3.4 No fixed finite carrier reproduces a qubit")
A("")
A(L(230)); A("")
A("### 3.5 The Born exponent and Bell structure")
A("")
A("The origin of the quadratic Born exponent is open: $p=|U|^2$ is part of the definition of $\\mathsf Q_K$ and is "
  "not selected by the correspondence (§2.3) [Main §3.4; Bar26, Thm 3.1].")
A("")
bell = seg(234, "a deterministic completion that keeps pointwise causal cones")
A("A" + bell[1:])
A("")
A("***"); A("")

# 4. Cosmological constant
A("## 4. The cosmological constant: how OI might change the interpretation of vacuum energy")
A("")
A("<!-- OWNER: landing gate (r6 re-check O2). Weinberg 1989 (Rev. Mod. Phys. 61, 1) is to be read first-hand and "
  "cited for the number in the next sentence before the paper lands. -->")
A("Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density some "
  "120 orders of magnitude above the observed one, the exact power depending on the cutoff convention; if that "
  "density sources curvature, it must be cancelled to that accuracy.")
A("")
A("In OI the zero-point sum of the emergent quantum description and the effective cosmological constant are defined "
  "at different levels of description. A uniform shift of the emergent Hamiltonian changes no visible transition "
  "probability, so the offset has no content in the visible statistics of the quantum description [GR §6.2]. The "
  "invariance is the familiar statement that no non-gravitational measurement sees the absolute vacuum energy; the "
  "proposal's content lies in how the two levels couple to geometry.")
A("")
A("Whether the offset also fails to source curvature is a separate coupling question. Settling it requires covariant "
  "field equations derived from the substratum, with their coupling to sources (Level G3 of [GR]), which are open "
  "[GR §6.2]. The quantum description therefore does not decide between gravitational completions that differ by a "
  "term $\\rho_C\\,g_{\\mu\\nu}$, such as $\\mathcal G_{\\mu\\nu}=8\\pi G\\,T^{\\rm cl}_{\\mu\\nu}$ and "
  "$\\mathcal G_{\\mu\\nu}=8\\pi G\\,(T^{\\rm cl}_{\\mu\\nu}-\\rho_C\\,g_{\\mu\\nu})$ [GR §6.2]. The proposal that "
  "the mismatch requires no cancellation is therefore conditional on that open step.")
A("")
A("If the covariant field equations take the form [GR] targets, $E_{\\mu\\nu}[g,\\mathrm{OI}]=8\\pi G\\,(T_{\\mu\\nu}-"
  "\\mathcal F[g,T]\\,g_{\\mu\\nu})$, with the classical stress-energy of the substratum as source, the zero-point "
  "sum of the emergent description is not a source and needs no cancellation; the vacuum term that remains, from "
  "the substratum's classical energy density and from $\\mathcal F$, is not computed. It does not explain the "
  "observed value of Λ, which enters as a cosmological input. The scale $\\rho\\sim H^2/G$ is the Friedmann "
  "normalization of the total density, and the fraction carried by Λ is an input.")
A("")
A("With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff "
  "convention; this is a dimensional identity, not an independent prediction. How the energy of electroweak and QCD "
  "vacuum transitions couples to gravity is not fixed by the descriptive distinction and requires the same open "
  "coupling step.")
A("")
A("Removing the vacuum energy of matter as a source of curvature is also the aim of the trace-free Einstein "
  "equations, which leave the observed value of Λ unexplained [EvEMU11], and of vacuum-energy sequestering, which "
  "extends to the vacuum energy of phase transitions [KP14]; Volovik argues from the thermodynamics of quantum "
  "many-body ground states that the ultraviolet zero-point sum does not set the vacuum energy [Vol06]. The present "
  "proposal differs in locating the gravitational source in the substratum microstate, and its coupling step is open.")
A("")
A("A derivation of the covariant field equations, with their conservation and source coupling, from the substratum "
  "would turn the proposal into a theorem or refute it. Until then the proposal reinterprets the problem and does "
  "not resolve it.")
A("")
A("***"); A("")

# 5. Black-hole information
A("## 5. Black-hole information: preservation versus accessible recovery")
A("")
p172 = L(172)
s172_123 = seg(172, "The black-hole information problem asks", " The combinatorial results were checked")
s172_5 = seg(172, "They concern the framework's nested-partition construction")
A(s172_123 + " " + s172_5)
A("")
A(seg(176, "The configuration space is modelled as", " A bijection loses no information"))
A("")
A("<!-- OWNER: R11 (per the R11 review verdicts). The next paragraph's claim A is in tension with live text: ch07:110 / "
  "FULL:1987 and ch18:146 / FULL:4966 sentence 2 claim more than their support; ch18:158 / FULL:4978 contradicts it; "
  "the falsification framing at ch07:159–161 / FULL:2036–2038 is unfalsifiable as stated. The paper must not land "
  "until the owner corrects those sites (#936) or drops this paragraph and its restatements (§6.2 item 4, §6.4, "
  "abstract). -->")
A("Under OI, information is conserved in the global reversible dynamics because the dynamics is a bijection, which is "
  "a premise of the framework. Conservation neither implies nor is necessary for recovery from the records an "
  "observer can access: finite exhaustive computations exhibit bijections with no accessible advantage and "
  "non-injective maps with exact recovery [BHa].")
A("")
A("Let $\\mathcal U$ be the set of joint values of the registers left unread at the end and $\\mathcal M$ the message "
  "set. Of the 40,320 bijections of $\\{0,1\\}^3$, 1,376 give zero accessible advantage, the gain in success "
  "probability over a blind guess, for a binary message with one register unread after two emissions. For bijective "
  "dynamics, complete endpoint access gives exact recovery, and with $\\mathcal U$ inaccessible "
  "$P_{\\mathrm{succ}}\\ge1/|\\mathcal U|$, so zero advantage in a bijective instance requires "
  "$|\\mathcal U|\\ge|\\mathcal M|$; 32 non-injective maps of $\\{0,1\\}^2$ violate the bound on "
  "$P_{\\mathrm{succ}}$ [BHa]. These endpoint guarantees are sufficient, not necessary. "
  + seg(181, "The bound is the remnant-capacity form"))
A("")
A("<!-- OWNER: R11 (per the R11 review verdicts). The next two paragraphs are in tension with ch07:126 sentences 1–2 "
  "/ FULL:2003, GR:869, and the unconditional Page-curve statements at ch18:146 / FULL:4966 and ch19:334 / "
  "FULL:5510; GR Thm A.8's shell scope (#936 DIFF-REVIEW §6) is pending correction. -->")
A("In the framework's nested-partition construction the Page value enters only through the scrambling hypothesis "
  "H-scramble, which no bijection satisfies from a definite configuration with configuration-aligned cuts [BHb, C1, "
  "C6(a)–(b)]. H-scramble posits equidistribution of the orbit on an energy shell. The mean entropy of that ensemble "
  "is Page's average $S_{\\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$ [Pag93] when the shell is the full "
  "product space; on a smaller shell it differs in general, in a direction that depends on the shell [BHb, C6(c)].")
A("")
A("<!-- OWNER: R11. The closure clause below contradicts GR:811 (\"D is frozen on evaporation timescales\"), false "
  "by at least 57 orders of magnitude. The label \"H-decouple\" for the closure condition is used only once #936 "
  "lands and the owner adopts it with DIFF-REVIEW R1's definition. -->")
A("The Page curve of [GR App. A] is not established. Its stated hypothesis H-scramble is open. It also requires that "
  "the black hole and its radiation evolve as a closed system in a pure joint state, uncoupled from the sector beyond "
  "the cosmological horizon and from the rest of the visible sector, over whole cycles of the dynamics; timescale "
  "ordering does not supply this, since $t_{\\rm evap}/\\tau_B^D \\ge 10^{57}$ at 30 solar masses over the assumed "
  "parameter intervals [BHa, item F]. Its stated value is established only for a full-product shell, and what the "
  "cycle-typicality argument supplies is a time average at a fixed bipartition, so the curve along one trajectory is "
  "open [BHb, C6(c)–(d)]. In the dependency ladder of [GR] the Page curve is also conditional on the covariant field "
  "equations. The black-hole information problem is not resolved here.")
A("")
A("The generalized second law is not derived [GR App. A.6]; agreement with quantum-extremal-surface computations "
  "[Pen20] is not established; the correspondence between islands and substratum cycles is conjectural [Book §7.6].")
A("")
A("***"); A("")

# 6. Discussion and conclusion
A("## 6. Discussion and conclusion: implications, limitations and decisive open tests")
A("")
A("### 6.1 Implications")
A("")
A("If the hypothesis holds, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer, "
  "and their departures from Markov behaviour are memory carried in an inaccessible sector; whether the rest of "
  "operational quantum mechanics follows depends on completion conditions that OI does not imply (§3.2). Quantum "
  "Bell correlations are not accounted for by memory alone: with measurement independence kept, they need ontic "
  "parameter dependence, whose "
  "compatibility with operational no-signalling and the continuum limit is the open hypothesis H-Bell (§3.5). Two "
  "long-standing problems would then change form: vacuum energy becomes a question about how two levels of "
  "description couple to geometry, and black-hole information separates into conservation and accessible recovery.")
A("")
A("### 6.2 What is not claimed")
A("")
A(L(238))
A(L(239))
A(sub(L(240), "indivisibility on short windows (§3.2).", "indivisibility on short windows (§3.1)."))
A("4. <!-- OWNER: R11. Restates §5's claim A and H-scramble finding; it stands or falls with those paragraphs. --> "
  "No resolution of the black-hole information problem: the Page curve of [GR App. A] needs H-scramble and the "
  "closure of the black hole and its radiation, in a pure joint state, over whole cycles; its stated value is "
  "established only for a full-product energy shell; and it gives a cycle average rather than a curve along one "
  "trajectory; the correspondence with islands is conjectural; the generalized second law is open; and the results "
  "of §5 concern finite toy models, each proved on paper or checked exhaustively at small size or by exact "
  "arithmetic. No claim is made that information reaches $D$, that [GR, Thm A.7] fails within its stated scope, or "
  "that no other decoupling argument exists.")
A(L(242))
A(sub(L(243), "the card game (§4.3)", "the card game (Appendix B)"))
A("7. No prediction of the value of Λ or $\\Omega_\\Lambda$, and no resolution of the cosmological constant problem: "
  "§4 is conditional on the covariant field equations.")
A("8. No claim that the viewpoint is new: deterministic systems analysed with quantum methods have been studied "
  "before, for example in [tH14]. The paper's results are the theorems and their scopes.")
A("")
A("### 6.3 Decisive open tests")
A("")
A("For quantum emergence: whether a physical substratum supplies completion conditions (iii)–(v), and whether history "
  "readback (C4) holds at the cosmological partition [GR §2.2]; no experiment yet distinguishes OI from standard "
  "quantum theory, and no memory-witness constraint is established [Main §4.5]. For the cosmological constant: a "
  "derivation of the covariant field equations with their source coupling. For black-hole information: whether "
  "H-scramble and the closure condition hold, the Page value on the relevant shell, and, in [GR]'s ladder, the "
  "covariant field equations.")
A("")
items = seg(234, "(1) machine checks", " (5) Bell correlations")
items = sub(items, "the steps of §2.2, §2.4 and §3.1 that lack one", "the steps of §2.2, §2.4 and §2.5 that lack one")
items = items.rstrip(";")
A("Further open problems are: " + items + ".")
A("")
A("### 6.4 Conclusion")
A("")
A(seg(249, "At every finite horizon", " Because the representation") + " " + seg(249, "Exact operational quantum mechanics is reached"))
A("")
A("<!-- OWNER: R11. Restates §5's claim A and H-scramble finding; it stands or falls with those paragraphs. -->")
A("Applied to vacuum energy, OI proposes that the zero-point sum of the emergent description is not a gravitational "
  "source, conditional on covariant field equations that are not derived; applied to black-hole information, it "
  "separates conservation from accessible recovery, while the framework's Page curve is not established. Neither "
  "application is a demonstrated resolution of its problem.")
A("")

# Code, data and formal verification (r4:254-262)
for n in range(254, 263):
    A(L(n))
A("")
# Appendix A (r4:264-277), section pointers renumbered
appA = R4[263:277]
ren = [("**Theorem 2** (§2.4)", "**Theorem 2** (§2.4)"),
       ("**Stochastic-inverse lemma; Theorem 3** (§3.1)", "**Stochastic-inverse lemma; Theorem 3** (§2.5)"),
       ("**Readback forces indivisibility** (§3.1)", "**Readback forces indivisibility** (§2.5)"),
       ("**Relating evolution** (§6.2)", "**Relating evolution** (§3.3)"),
       ("**Theorem 4** (§6.1)", "**Theorem 4** (§3.2)"),
       ("**Independence; OI alone does not imply QM** (§6.1, qubit)", "**Independence; OI alone does not imply QM** (§3.2, qubit)")]
txtA = "\n".join(appA)
for a, b in ren:
    txtA = sub(txtA, a, b)
A(txtA)
A("")
# Appendix B
A("## Appendix B. Examples")
A("")
A("### B.1 A minimal model")
A("")
for n in range(132, 140):
    A(L(n))
A("")
A("### B.2 Memory without short-window indivisibility")
A("")
A(L(143)); A("")
A("### B.3 The card table")
A("")
for n in range(147, 162):
    A(L(n))
A(sub(L(162), "is notion (2) of §3.2.", "is notion (2) of §3.1."))
A("")
A("<!-- Source of the decomposition below: ERRATUM-r4 (design record), by the Pauli-twirl identity; not a corpus "
  "derivation. -->")
A(sub(L(164), "sums to the one-step map,",
      "sums to the one-step map by the identity $\\sum_o\\sigma_oX\\sigma_o=2\\operatorname{tr}(X)\\,I$,"))
A("")
A(L(166))
A("")
# References
refs = R4[278:]
txtR = "\n".join(refs)
pag05 = [l for l in refs if l.startswith("[Pag05]")][0]
txtR = sub(txtR, pag05 + "\n\n", "")
newrefs = {
 "[Cal26]": None,
}
def insert_before(txt, key, entry):
    i = txt.index("\n" + key)
    return txt[:i+1] + entry + "\n\n" + txt[i+1:]
txtR = insert_before(txtR, "[GH03]", "[EvEMU11] G. F. R. Ellis, H. van Elst, J. Murugan, and J.-P. Uzan, \"On the trace-free Einstein equations as a viable alternative to general relativity,\" *Class. Quantum Grav.* **28**, 225007 (2011); arXiv:1008.1196v2. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->")
txtR = insert_before(txtR, "[LP17]", "[KP14] N. Kaloper and A. Padilla, \"Sequestering the Standard Model vacuum energy,\" *Phys. Rev. Lett.* **112**, 091304 (2014); arXiv:1309.6562v2. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->")
i = txtR.index("\n\\endgroup")
txtR = (txtR[:i].rstrip("\n") + "\n\n"
        "[tH14] G. 't Hooft, \"The cellular automaton interpretation of quantum mechanics,\" arXiv:1405.1548v3 (2014). <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read; no priority is assigned -->\n\n"
        "[Vol06] G. E. Volovik, \"Vacuum energy: myths and reality,\" *Int. J. Mod. Phys. D* **15**, 1987 (2006); arXiv:gr-qc/0604062v4. <!-- VERIFY: abstract read first-hand (arXiv API, 2026-10-26); body not read -->\n"
        + txtR[i:])
A(txtR)
open(out_path, "w", encoding="utf-8").write("\n".join(out).rstrip("\n") + "\n")
print("written", out_path)
