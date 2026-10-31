"""Introduction-r11.md = r10 + the nits of the r10 re-check and the retained Lean evidence (papers/introduction_repro/).

Each edit is an exact, uniquely matching replacement on r10, so every unchanged sentence stays byte-identical to r10.
"""
import re
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


# --- 1. Revert T3 (RECHECK-r10 finding 1): the theorem pointer into [Main §3.4] is restored ---
rep("T3 reverted", "in the hidden register [Main §3.4; EGGH26, Prop. 13].",
    "in the hidden register [Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); "
    "EGGH26, Prop. 13].")

# --- 3. Weinberg marker: unambiguous wording (RECHECK-r10 finding 3, minor point); gating unchanged ---
rep("Weinberg marker wording", "it is cited for that sentence only once the source is read and checked. -->",
    "it is cited for that sentence only after the source is read and checked. -->")
rep("Weinberg landing gate (owner decision 2026-10-26)", "<!-- VERIFY: Weinberg 1989 (Rev. Mod. Phys. 61, 1)",
    "<!-- VERIFY: Landing gate (owner, 2026-10-26): the paper does not land until this source is read first-hand and "
    "checked. Weinberg 1989 (Rev. Mod. Phys. 61, 1)")

# --- 4. Lean evidence (papers/introduction_repro/, main 17b830bc) ---
rep("Conventions commit", "[dMU21; Mathlib20] at commit `687e885b` by the recipe",
    "[dMU21; Mathlib20] at commit `17b830bc` by the recipe")
pat = re.compile(r"\n<!-- OWNER: decision 2 / retention §A\.42\.[^\n]*-->\n")
assert len(pat.findall(t)) == 1
t = pat.sub("", t, count=1)
log.append("OWNER §A.42 marker (Conventions) removed")
pat = re.compile(r"<!-- OWNER: retention §A\.42\. The Lean-check sentence below[^\n]*-->\n")
assert len(pat.findall(t)) == 1
t = pat.sub("", t, count=1)
log.append("OWNER §A.42 marker (Code section) removed")
rep("Code-section evidence sentence",
    "The declarations in Appendix A were checked in Lean 4/Mathlib at commit 687e885b1cfd24d6f17eee439101afc8acf07015 "
    "by the recipe `python3 tools/lean_axiom_check.py --require-lake`, which builds the Lean project and requires "
    "every `#print axioms` report to lie within `propext`, `Classical.choice` and `Quot.sound`; the expected result "
    "is in [expected-result file path].",
    "The declarations in Appendix A were checked in Lean 4.33.0 with Mathlib v4.33.0 at commit "
    "17b830bcd0ecc36e10eff5b9eeca03bdd7198d86, by building the Lean project in `verification/lean-mathlib` "
    "(`lake exe cache get`, `lake --rehash build`) and running `python3 tools/release_gate.py`, whose "
    "`lean-axioms` step requires every `#print axioms` report to lie within `propext`, `Classical.choice` and "
    "`Quot.sound`. Each declaration in Appendix A reports exactly these three; the expected result and the "
    "comparison recipe are in `papers/introduction_repro/`.")

# --- one commit throughout: 17b830bc (Lean trees identical to 687e885b; #936's GR/BH text exists only from 17b830bc) ---
rep("Appendix A commit", "Modules of the `OIBridge` Lean library; line numbers at commit `687e885b`.",
    "Modules of the `OIBridge` Lean library; line numbers at commit `17b830bc`.")
rep("Corpus commit", "**Corpus** (repository commit `687e885b`,", "**Corpus** (repository commit `17b830bc`,")

open(dst, "w", encoding="utf-8").write(t)
print("applied", len(log), "edits:", "; ".join(log))
