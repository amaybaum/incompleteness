"""Introduction-r8.md = r7 + the black-hole alignment pass to #936 as merged (main 17b830bc).

Each edit is an exact, uniquely matching replacement on r7, so every unchanged sentence stays byte-identical to r7.
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


def drop_marker(tag, prefix):
    """Remove one whole-line OWNER comment that starts with `prefix` (and its trailing newline)."""
    global t
    pat = re.compile(r"^" + re.escape(prefix) + r"[^\n]*-->\n", re.M)
    hits = pat.findall(t)
    assert len(hits) == 1, (tag, len(hits))
    t = pat.sub("", t, count=1)
    log.append(tag)


# --- R11 markers: every site they name is corrected on main 17b830bc (#936) ---
# abstract marker sits between two blank lines; remove it with one of them
pat = re.compile(r"\n<!-- OWNER: R11\. The abstract's black-hole sentence[^\n]*-->\n")
assert len(pat.findall(t)) == 1
t = pat.sub("", t, count=1)
log.append("R11 marker (abstract) removed")
drop_marker("R11 marker (claim A) removed", "<!-- OWNER: R11 (per the R11 review verdicts). The next paragraph's claim A")
drop_marker("R11 marker (Page paragraphs) removed", "<!-- OWNER: R11 (per the R11 review verdicts). The next two paragraphs")
drop_marker("R11 marker (closure / H-decouple label) removed", "<!-- OWNER: R11. The closure clause below")
rep("R11 marker (conclusion) removed", "<!-- OWNER: R11. Restates §5's claim A and H-scramble finding; it stands or "
    "falls with those paragraphs. -->\nApplied to vacuum energy", "Applied to vacuum energy")
rep("R11 marker (§6.2 item 4) removed", "4. <!-- OWNER: R11. Restates §5's claim A and H-scramble finding; it stands or "
    "falls with those paragraphs. --> No resolution", "4. No resolution")

# --- §5: the configuration-space paragraph moves into the Page-curve paragraph (setup of [GR App. A]) ---
rep("§5 config paragraph moved", "The configuration space is modelled as $\\mathcal C_V\\times\\mathcal C_B\\times"
    "\\mathcal C_D$, with $V$ the exterior visible region, $B$ the black-hole interior and $D$ the sector beyond the "
    "cosmological horizon; radiation is emitted from $B$ into $V$ [GR App. A.1].\n\n", "")

# --- §5: the two Page-curve paragraphs and the GSL/QES paragraph become one subordinate paragraph ---
old_start = "In the framework's nested-partition construction Page's mean-entropy value (below) enters only"
old_end = "the correspondence between islands and substratum cycles is conjectural [Book §7.6].\n"
i, j = t.index(old_start), t.index(old_end) + len(old_end)
assert t.count(old_start) == 1 and t.count(old_end) == 1
page = (
    "The Page-curve calculation of [GR App. A] addresses recovery under its own conditions and is a conditional "
    "result [Book §7.6, §18.5]. Its configuration space is $\\mathcal C_V\\times\\mathcal C_B\\times\\mathcal C_D$, with $V$ "
    "the exterior visible region, $B$ the black-hole interior and $D$ the sector beyond the cosmological horizon; the "
    "radiation $R$, a subsystem of $V$, is emitted from $B$ [GR App. A.1, A.7]. For all but an exponentially "
    "negligible fraction of initial conditions, the full-cycle time average of the radiation's entanglement entropy, "
    "at the bipartition of each stage held fixed, equals the Page value $S_{\\rm Page}(d_B,d_R)$ for factor "
    "dimensions $d_B,d_R$ [Pag93; GR, Thms A.8–A.9]. This holds under the scrambling hypothesis H-scramble, that "
    "the orbit ensemble equidistributes over quantum pure states on the shell; H-scramble fails for every bijection "
    "acting on a definite initial configuration with the bipartition aligned to the configuration coordinates and "
    "is not established [GR App. A.7; BHb, C1, C6(a)–(b)]. It also needs the decoupling condition H-decouple: "
    "$B\\cup R$ evolves with no coupling to $D$ or to the rest of the visible sector, $V\\setminus R$, and its joint "
    "state is pure, over whole cycles of the dynamics; timescale ordering does not supply it, and it is not "
    "established [GR App. A.7]. Theorem A.8 of [GR] takes the whole configuration space $\\mathcal C_B\\times"
    "\\mathcal C_R$ as a single energy shell. That requires the energy to be constant there, so that energy "
    "conservation places no constraint on the orbit, and it does not follow from the conservation of a Hamiltonian "
    "that takes more than one value there. An evaporating black hole whose radiation carries away its energy is in "
    "the proper-shell case, where the mean entropy depends on the shell and in general differs from the Page value; "
    "that case is open [GR App. A.7; BHb, C6(c)]. The result is a time average at a fixed bipartition, and whether "
    "the entropy along a single trajectory follows the same curve is open [GR App. A.7; BHb, C6(d)]. In the "
    "dependency ladder of [GR] the Page curve is also conditional on the covariant field equations. The generalized "
    "second law is not derived [GR App. A.6]; agreement with quantum-extremal-surface computations [Pen20] is not "
    "established; the correspondence between islands and substratum cycles is conjectural [Book §7.6]. The Page "
    "curve of [GR App. A] is therefore not established, and the black-hole information problem is not resolved "
    "here.\n"
)
t = t[:i] + page + t[j:]
log.append("§5 Page-curve material compressed to one paragraph (merged #936 wording)")

# --- §6.3: the closure condition by its name on main; the open shell and trajectory questions ---
rep("§6.3 H-decouple / proper shell", "whether H-scramble and the closure condition hold, the Page value on the "
    "relevant shell, and,", "whether H-scramble and H-decouple hold, the Page value on a proper energy shell and "
    "along a single trajectory, and,")

# --- references: arXiv identifier for [BBS24] (reference check, S/refs/FINDINGS.md) ---
rep("BBS24 arXiv", "*Phys. Rev. Lett.* **132**, 060402 (2024). <!-- VERIFY",
    "*Phys. Rev. Lett.* **132**, 060402 (2024); arXiv:2310.01205v2. <!-- VERIFY")

open(dst, "w", encoding="utf-8").write(t)
print("applied", len(log), "edits:", "; ".join(log))
