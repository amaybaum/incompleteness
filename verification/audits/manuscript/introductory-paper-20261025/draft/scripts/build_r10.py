"""Introduction-r10.md = r9 + publication-readiness edits (owner decisions of 2026-10-26).

Each edit is an exact, uniquely matching replacement on r9, so every unchanged sentence stays byte-identical to r9.
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


# --- 1. Title: pandoc title block (no raw LaTeX; the # heading hyphenated "Determinis-tic") ---
rep("title block", "# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations\n\n"
    "**Author:** Alex Maybaum  \n**Date:** October 2026  \n",
    "% Observational Incompleteness: From Deterministic Dynamics to Quantum Observations\n% Alex Maybaum\n"
    "% October 2026\n\n")

# --- 3. Weinberg: owner gate becomes a VERIFY marker (not read first-hand); no claim attributed ---
rep("Weinberg VERIFY", "<!-- OWNER: landing gate (r6 re-check O2). Weinberg 1989 (Rev. Mod. Phys. 61, 1) is to be read "
    "first-hand and cited for the number in the next sentence before the paper lands. -->",
    "<!-- VERIFY: Weinberg 1989 (Rev. Mod. Phys. 61, 1) is not read first-hand and is not treated as verified: the APS "
    "copy is paywalled, and the UT ScholarWorks copy (hdl 2152/61094) is blocked by its bot check from this "
    "environment; see draft/review/references/FINDINGS.md. No claim in the next sentence is attributed to Weinberg; "
    "it is cited for that sentence only once the source is read and checked. -->")

# --- 2. Length: trims of repetition, transitions and nonessential explanation only ---
T = {}
T["T1"] = ("This section defines three classes of finite-horizon law, shows that they coincide, identifies what the "
           "coincidence leaves (where a law's memory must sit), and states what finite recurrence does with that "
           "memory. Each result is stated with its reference; the proofs are in the cited papers.\n\n", "")
T["T2"] = ("[Main] writes Theorem 1 as $S\\iff D\\iff Q_{\\mathrm{fb}}$. Theorem 1 is machine-checked",
           "Theorem 1 is machine-checked")
T["T3"] = ("in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); "
           "EGGH26, Prop. 13].", "in the hidden register [Main §3.4; EGGH26, Prop. 13].")
T["T4"] = ("(operational-completion characterization [GR §3.3, Theorem (operational-completion characterization)])",
           "(operational-completion characterization [GR §3.3])")
T["T5"] = ("Appendix B works a minimal model of Theorem 3 with six hidden states, a process with memory but no "
           "short-window indivisibility, and the smallest realization of Theorem 3, a two-card game, with its "
           "classical and quantum scope.",
           "Appendix B works examples: a minimal model of Theorem 3 with six hidden states, memory without "
           "short-window indivisibility, and a two-card game, the smallest realization of Theorem 3.")
only = sys.argv[3].split(",") if len(sys.argv) > 3 else sorted(T)
for k in only:
    rep(k, *T[k])

open(dst, "w", encoding="utf-8").write(t)
print("applied", len(log), "edits:", "; ".join(log))
