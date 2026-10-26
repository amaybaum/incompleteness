"""Introduction-r14.md = r13 + the Weinberg 1989 landing gate cleared (G1, G2).

Weinberg 1989 was read first-hand and checked (review/references/WEI89.md). Each edit is an exact, uniquely matching
replacement on r13, so every unchanged sentence stays byte-identical to r13.
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


MARKER = (
    "<!-- VERIFY: Landing gate (owner, 2026-10-26): the paper does not land until this source is read first-hand and "
    "checked. Weinberg 1989 (Rev. Mod. Phys. 61, 1) is not read first-hand and is not treated as verified: the APS copy "
    "is paywalled, and the UT ScholarWorks copy (hdl 2152/61094) is blocked by its bot check from this environment; see "
    "draft/review/references/FINDINGS.md. No claim in the next sentence is attributed to Weinberg; it is cited for that "
    "sentence only after the source is read and checked. -->\n"
)

# --- G1: the gate sentence, cited to what Weinberg states (WEI89.md, Option A); the convention clause stays uncited ---
rep("G1",
    MARKER + "Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density "
    "some 120 orders of magnitude above the observed one (the mismatch), the exact power depending on the cutoff "
    "convention; if that density sources curvature, it must be cancelled to that accuracy.",
    "Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density "
    "some 120 orders of magnitude above the observational value [Wei89, §I; §III, Eqs. (3.4)–(3.6)] (the mismatch), "
    "the exact power depending on the cutoff convention; if that density sources curvature, it must be cancelled to "
    "that accuracy [Wei89, §III].")

# --- G2: bibliography entry, alphabetically after [Vol06] ---
rep("G2",
    "§5.2 (draft/review/references/FINDINGS.md, sha256 fa50caae…6ea1): SUPPORTED. -->\n",
    "§5.2 (draft/review/references/FINDINGS.md, sha256 fa50caae…6ea1): SUPPORTED. -->\n\n"
    "[Wei89] S. Weinberg, \"The cosmological constant problem,\" *Rev. Mod. Phys.* **61**, 1 (1989). "
    "<!-- Read first-hand: §I p. 1 and §III pp. 2–3, Eqs. (3.4)–(3.6); third-party scanned copy, not redistributed "
    "(draft/review/references/WEI89.md): SUPPORTED with qualifications. -->\n")

open(dst, "w", encoding="utf-8").write(t)
print("applied %d edits: %s" % (len(log), "; ".join(log)))
