"""Introduction-r12.md = r11 + the findings of the final scientific review of r11 (B1, B2, N1-N8).

Each edit is an exact, uniquely matching replacement on r11, so every unchanged sentence stays byte-identical to r11.
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


# --- B1: Theorem 4's structural hypotheses (FiniteOperationalTheory, OperationalAssembly:594; GR:216) ---
rep("B1", "Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear "
    "maps are available on the system and at every ancilla level [GR §3.3].",
    "Fix a nonempty finite system and an operational theory specifying which finite outcome families of linear "
    "maps are available on the system and at every ancilla level. The theory contains the identity and is closed "
    "under coarse-graining of outcomes and, at every ancilla level, under outcome-conditioned composition; it has an "
    "available preparation of a uniformly mixed ancilla, which an available operation may follow, an available "
    "spectator-independent local readout of the ancilla, and ancilla discard: an available preparation followed by "
    "an available instrument, with the ancilla then discarded, is an available operation on the system [GR §3.3].")

# --- B2: corpus pin to main c967d6a9 (after #937); the Lean pins stay at 17b830bc (identical Lean tree) ---
rep("B2", "**Corpus** (repository commit `17b830bc`,", "**Corpus** (repository commit `c967d6a9`,")

# --- N1: the capacity bound carries Theorem 2's scope ---
rep("N1", "needs $|\\mathcal C_H|\\ge2^{I^*}$ (machine-checked).",
    "needs $|\\mathcal C_H|\\ge2^{I^*}$ (machine-checked in the same form as Theorem 2).")

# --- N2: the imported unboundedness is cited to the source [Main] imports it from ---
rep("N2 cite", "and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — "
    "classical-dimension form)].",
    "and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — "
    "classical-dimension form); HKLP24, Thm 4].")
rep("N2 bib", "[Haw76] S. W. Hawking, \"Breakdown of predictability in gravitational collapse,\" *Phys. Rev. D* **14**, "
    "2460 (1976).\n",
    "[Haw76] S. W. Hawking, \"Breakdown of predictability in gravitational collapse,\" *Phys. Rev. D* **14**, "
    "2460 (1976).\n\n"
    "[HKLP24] T. Heinosaari, O. Kerppo, L. Leppäjärvi, and M. Plávala, \"Simple information processing tasks with "
    "unbounded quantum advantage,\" *Phys. Rev. A* **109**, 032627 (2024); arXiv:2308.07727v4.\n")

# --- N3: the black-hole computations are in the repository, not in the release archive ---
rep("N3", "The probes and the black-hole computations [BHa; BHb] are released under the MIT License (concept DOI "
    "10.5281/zenodo.19060318), at these repository paths:\n\n"
    "- `papers/oi_lattice_code/foundations/` (probes);\n"
    "- `verification/programmes/black-hole-information/` (black-hole computations).",
    "The probes and the black-hole computations [BHa; BHb] are released under the MIT License, at these repository "
    "paths at the corpus commit:\n\n"
    "- `papers/oi_lattice_code/foundations/` (probes; also in the release archive, concept DOI "
    "10.5281/zenodo.19060318);\n"
    "- `verification/programmes/black-hole-information/` (black-hole computations; not part of the release "
    "archive).")

# --- N4: the abstract's open question names (iii)-(v), as the body does ---
rep("N4", "Open are which of these a physical substratum supplies,",
    "Open are which of conditions (iii)–(v) a physical substratum supplies,")

# --- N5: Theorem 3's object, as RootedRealization takes it ---
rep("N5", "*Let $\\varphi$ be a bijection of a finite set. If two rows",
    "*Let $\\varphi$ be a bijection of $\\mathcal C_V\\times\\mathcal C_H$ with a fixed hidden prior. If two rows")

# --- N6: "finite toy models" restricted to the [BHa; BHb] results ---
rep("N6", "and the results of §5 concern finite toy models,",
    "and the results of §5 reported from [BHa; BHb] concern finite toy models,")

# --- N7: the witness for (C4) <=> M_t>0 is the vanishing criterion ---
rep("N7", "In a faithful realization (C4) coincides with $M_t>0$, by the Corollary;",
    "In a faithful realization (C4) coincides with $M_t>0$ by the vanishing criterion [CT06], and the Corollary "
    "places it in the hidden state;")

# --- N8: the internal source comment is deleted ---
rep("N8", "<!-- Source of the decomposition below: ERRATUM-r4 (design record), by the Pauli-twirl identity; not a corpus "
    "derivation. -->\n", "")

# --- page budget (owner's rule: repetition, transitions, nonessential explanation only) ---
# P1: §6.1's closing sentence repeats §4 and §5 and the conclusion (§6.4) and the abstract
rep("P1 (repetition)", " Two long-standing problems would then change form: vacuum energy becomes a question about how two "
    "levels of description couple to geometry, and black-hole information separates into conservation and "
    "accessible recovery.", "")

open(dst, "w", encoding="utf-8").write(t)
print("applied", len(log), "edits:", "; ".join(log))
