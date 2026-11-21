#!/usr/bin/env python3
"""C14-AUDIT occurrence register for the foundational conditions C1-C4.

Read-only. Scans the manuscripts, the book (chapters and FULL.md), the glossary, the README files
and the Lean modules that name the conditions. register.tsv keeps one row per hand-classified match
(every class except `reference` and `unrelated`); --full prints every match to stdout instead:

    file  line  col  cond  class  ledger  mirror  note  text

`class` is the reviewed classification from REVIEWED below where one exists; every other match is
`reference` (an inline mention carrying no definition, classified by rule, not reviewed one by
one), or `unrelated` for labels that name a different object. FULL.md rows inherit the class of the
chapter line they mirror byte for byte. `ledger` marks lines that #1477's frozen edit ledger
(edits.json at 55544cc3) edits. The ledger is read from git and is not modified.

Usage (from the repository root):  python3 -I <this file> [--check | --full]
--check regenerates the register in memory and fails if it differs from the committed file.
--full prints the whole scan, rule-classified rows included, without writing anything.
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "register.tsv")
LEDGER_COMMIT = "55544cc3"
LEDGER_PATH = "verification/audits/foundations/a1exit-deletion-20261121/edits.json"
FULL = "book/The-Incompleteness-of-Observation-FULL.md"

MD = sorted(glob.glob("papers/*.md")) + sorted(glob.glob("book/*.md")) + ["README.md", "verification/README.md"]
LB = "verification/lean-mathlib/OIBridge/"
LEAN_OI = [LB + f + ".lean" for f in (
    "IndependenceCensus", "OIRealization", "PhysicalC4Discharge", "PhysicalC4StorageReadback",
    "MonoidalCompletion", "CompositionalIndependence", "PassiveQuotient", "ObservabilityQuotient",
    "RouteB", "ReadWriteControl", "CausalReadback", "C3Necessity", "TrajectoryMemory", "HiddenMemory",
    "AccessibleAlgebra", "SubstantiveCensus", "DiagonalTheory", "SubstratumInterfaceAudit")] + ["verification/lean-mathlib/OIBridge.lean"]
# Lean files whose C1..C4 labels name other objects (milestones, targets, sub-claims, a group element).
LEAN_OTHER = [LB + f + ".lean" for f in (
    "DerivedQ3", "CandidateSelection", "CoherentLift", "TwoSidedGauge", "GramTrajectorySelection",
    "IntermediateCrossTimeStructure", "LinkDecomposition")] + ["verification/lean/OI_Structural_Chain.lean"]

# Single lines outside the manuscripts added at review: guard strings that restate a condition.
EXTRA_SITES = [("papers/oi_lattice_code/architecture_check.py", 1086)]

PAT = re.compile(r"(?<![A-Za-z0-9_])[CС]([1-4])(?![0-9])")
PAT_LEAN_ID = re.compile(r"(?i)c([1-4])(?=_[a-z]|C[1-4]|Necessity)")

C = "canonical"; X = "exact"; E = "equivalent"; N = "name-only"; D = "different"; T = "theorem-ref"; U = "unrelated"
# Reviewed classifications: "file:line" -> (class, conditions it applies to or None for all, note).
REVIEWED = {
 # Canonical definitions, papers/Main.md section 1.3.
 "papers/Main.md:72": (C, "1", "(C1) Non-zero coupling"),
 "papers/Main.md:74": (C, "2", "(C2) Memory persistence; forms (C2-structural), (C2-slow)"),
 "papers/Main.md:76": (C, "3", "(C3) Sufficient memory capacity"),
 "papers/Main.md:78": (C, "4", "(C4) History readback"),
 # Book definitions (Chapter 1 section 1.3) and glossary.
 "book/ch01-observation.md:53": (E, None, "same name; same content, cites Main"),
 "book/ch01-observation.md:55": (E, None, "same name; structural form stated, slow bath one mechanism"),
 "book/ch01-observation.md:57": (E, None, "same name; same inequality"),
 "book/ch01-observation.md:59": (E, None, "same name; 'later visible steps' for 'future visible conditionals'"),
 "book/ch01-observation.md:251": (E, None, "table row; column 'What fails' (failure mode, not a name)"),
 "book/ch01-observation.md:252": (D, None, "column 'What fails', not a name; 'Markovian stochastic' outcome needs complete erasure / the uniform-erosion hypothesis (F1)"),
 "book/ch01-observation.md:253": (E, None, "column 'What fails', not a name; consistent with the ch01:229 limit model"),
 "book/glossary.md:25": (N, None, "named 'Coupling'; content equivalent"),
 "book/glossary.md:27": (E, None, "close paraphrase of Main:74 incl. both forms"),
 "book/glossary.md:29": (N, "3", "named 'Hidden-sector capacity'; content equivalent"),
 "book/glossary.md:31": (E, None, "adds positive probability; omits 'at some accessible order'"),
 # Paper restatements.
 "papers/Medicine.md:27": (N, None, "named 'Coupling'; first sentence matches Main:72"),
 "papers/Medicine.md:29": (E, None, "persistence to readback, slow bath one sufficient route"),
 "papers/Medicine.md:31": (N, None, "named 'Capacity'; first sentence matches Main:76"),
 "papers/Medicine.md:33": (E, None, "matches Main:78 operational clause"),
 "papers/Medicine.md:150": (E, None, "application list item"),
 "papers/Medicine.md:151": (E, None, "application list item (persistence time)"),
 "papers/Medicine.md:152": (E, None, "application list item (state count)"),
 "papers/Medicine.md:25": (T, "4", "C4 <=> M_t>0: matches Main section 3.4 Remark (diagnostics) within faithful realizations"),
 "papers/GR.md:46": (E, None, "application; restates accessible-conditional requirement"),
 "papers/GR.md:48": (E, None, "application of the slow-bath example (C2-slow), labelled as example"),
 "papers/GR.md:50": (E, None, "application (mode count)"),
 "papers/GR.md:52": (E, None, "application of the causal realization clause; not discharged"),
 "papers/GR.md:617": (D, None, "calls C1-C4 'structural conditions' (F2); C2 'slow bath ... the realization'"),
 "papers/GR.md:20": (E, None, "gloss list; memory-bearing sector characterized by C1, C3, C4"),
 "papers/Structure.md:110": (D, None, "'necessary for an embedded observer to exist', 'conditions on a substratum's bijection' (F3)"),
 "papers/Structure.md:112": (D, None, "'must be substantial' for H_int != 0 at an accessible step (F4)"),
 "papers/Structure.md:114": (N, None, "named 'Record persistence'; content equivalent"),
 "papers/Structure.md:116": (D, None, "'store the interaction history' for log2|C_H| >= I* (F7)"),
 "papers/Structure.md:118": (D, None, "'read back what was written' requires a causal write-read cycle (F5)"),
 "papers/Structure.md:528": (D, None, "'structural conditions for observer admission' (F2)"),
 "papers/Structure.md:530": (D, None, "'substantial coupling' (F4)"),
 "papers/Structure.md:532": (E, None, "persistence to readback, slow bath one realization"),
 "papers/Structure.md:534": (D, None, "'store the interaction history' (F7)"),
 "papers/Structure.md:536": (E, None, "C4 witness requirement stated operationally"),
 "papers/Structure.md:711": (D, None, "'structural conditions C1-C4' (F2)"),
 "papers/Structure.md:138": (D, "2", "'C2-mixing': sub-form not defined in Main section 1.3; scope differs from Theorem 23 (F9)"),
 "papers/Complexity.md:27": (N, None, "gloss list: coupling, record persistence, sufficient capacity, history readback"),
 "papers/Complexity.md:364": (E, None, "application (enzyme)"),
 "papers/Complexity.md:366": (E, None, "application of C2-slow, labelled 'slow-bath realization of persistence'"),
 "papers/Complexity.md:368": (E, None, "application; compares with visible state count (see F6 note)"),
 "papers/Complexity.md:370": (E, None, "matched-present operational form"),
 "papers/SM.md:22": (E, None, "gloss list; C4 operational, cosmological read-write cycle to be demonstrated"),
 "papers/SM.md:52": (E, None, "gloss list; conditions on the partition"),
 "papers/SM.md:1376": (T, None, "Theorem 22: C1 structural; C3 floor; C2, C4 hypotheses (see F8)"),
 "papers/SM.md:1378": (T, "1", "C1 proved as existence of a boundary coupling edge; preparation not addressed (F8)"),
 "papers/SM.md:1380": (T, "2", "C2 not established; hypothesis"),
 "papers/SM.md:1382": (T, "3", "C3 floor by data processing, consistent with Main Theorem (C3 necessity)"),
 "papers/SM.md:1384": (T, None, "remark on C2/C4 status, consistent"),
 "papers/Substratum.md:112": (T, None, "characterization theorem cited without its time-homogeneity hypothesis (F10)"),
 "papers/Substratum.md:127": (T, None, "equivalence attributed to the 'universal hidden-memory theorem'; it is the characterization theorem (F10)"),
 "papers/Substratum.md:129": (E, None, "two forms of C2 as in Main:74"),
 "papers/Substratum.md:24": (D, "2", "'C2-mixing' (F9)"),
 "papers/Substratum.md:195": (D, "2", "'C2-mixing condition' (F9)"),
 "papers/Substratum.md:367": (D, "2", "'C2-mixing' (F9)"),
 "papers/Substratum.md:407": (E, "2", "retention condition"),
 "papers/Methodology.md:108": (N, None, "gloss list: non-zero coupling, record persistence, sufficient capacity, history readback"),
 "papers/Methodology.md:162": (E, None, "role summary; consistent"),
 "papers/Introduction.md:85": (E, None, "non-technical paraphrase; 'feed the record back' reads C4 causally (low)"),
 "papers/Main.md:153": (N, "3", "'C3 (high-capacity hidden sector)' gloss inside the canonical paper"),
 "papers/Main.md:326": (D, None, "canonical paper: 'not an additional structural condition: (C1)-(C4) constrain coupling, timescales, and capacity' types all four structural, glosses C2 as timescales (F2b)"),
 "papers/Main.md:546": (T, None, "characterization theorem: (iii) lists C1, C3, C4; C2 deliberately absent"),
 "papers/Main.md:552": (T, None, "characterization theorem clause (iii)"),
 "papers/Main.md:628": (T, None, "Remark (the conditions are diagnostics, not hypotheses)"),
 "papers/Main.md:636": (T, None, "Remark (which condition is primitive): 'three structural conditions'"),
 # Book restatements.
 "book/ch07-gravity.md:24": (E, None, "mirror of GR:46 content; named 'coupling'"),
 "book/ch07-gravity.md:26": (E, None, "slow-bath example (C2-slow), as GR:48"),
 "book/ch07-gravity.md:28": (E, None, "as GR:50"),
 "book/ch07-gravity.md:30": (E, None, "as GR:52"),
 "book/ch09-universality.md:84": (D, None, "'C1-C4 specify the admission criterion'; the list that follows has no C4 entry (F11)"),
 "book/ch09-universality.md:112": (E, None, "non-trivial coupling; necessity for non-Markovian dynamics"),
 "book/ch09-universality.md:114": (E, None, "record survives to readback; slow bath one mechanism"),
 "book/ch09-universality.md:116": (E, None, "capacity >= I*; 'read-write cycle' phrasing (low)"),
 "book/ch11-origin-of-life.md:10": (D, None, "'structural conditions C1, C2, C3, C4' (F2)"),
 "book/ch11-origin-of-life.md:66": (N, None, "application names: catalytic feedback, template persistence, sequence capacity"),
 "book/ch11-origin-of-life.md:152": (D, "1", "C1 application requires two-way feedback; Main's C1 is one-way hidden-to-visible influence (F12)"),
 "book/ch11-origin-of-life.md:154": (N, "2", "named 'persistence'; content equivalent"),
 "book/ch11-origin-of-life.md:156": (N, "3", "named 'capacity'; application"),
 "book/ch11-origin-of-life.md:158": (E, "4", "matched-present operational form"),
 "book/ch12-evolution-intelligence.md:42": (E, None, "application"),
 "book/ch12-evolution-intelligence.md:44": (E, None, "records persist across the window"),
 "book/ch12-evolution-intelligence.md:46": (E, None, "distinguishable accessible record states"),
 "book/ch12-evolution-intelligence.md:48": (E, None, "matched-present operational form; bold where siblings are italic"),
 "book/ch13-quantum-biology.md:50": (D, "1", "named 'catalytic-conformational coupling'; asserts 'C1 is satisfied' without an accessible-conditional witness (F12)"),
 "book/ch13-quantum-biology.md:52": (D, "2", "named 'conformational timescale separation' (C2-slow only) (F1)"),
 "book/ch13-quantum-biology.md:54": (N, "3", "named 'conformational landscape capacity'"),
 "book/ch14-quantum-computing.md:107": (D, None, "'structural conditions C1-C4' (F2)"),
 "book/ch15-quantum-engineering.md:59": (E, None, "application"),
 "book/ch15-quantum-engineering.md:61": (E, None, "application of C2-slow (ratio only)"),
 "book/ch15-quantum-engineering.md:63": (N, "3", "named 'capacity'"),
 "book/ch15-quantum-engineering.md:65": (E, None, "matched-present operational form"),
 "book/ch16-medicine.md:196": (E, None, "application"),
 "book/ch16-medicine.md:198": (E, None, "application of C2-slow"),
 "book/ch16-medicine.md:210": (N, "3", "named 'capacity'"),
 "book/ch16-medicine.md:38": (E, "4", "matched-present operational form"),
 "book/ch16-medicine.md:194": (E, "4", "matched-present operational form"),
 "book/ch18-beyond.md:24": (D, None, "'necessary structural conditions' (F2, F3)"),
 "book/ch18-beyond.md:296": (D, None, "'necessary structural conditions' (F2, F3)"),
 "book/ch18-beyond.md:64": (E, None, "boundary by C1, C4 and the persistence form of C2"),
 "book/ch18-beyond.md:67": (E, None, "non-trivial interaction"),
 "book/ch18-beyond.md:68": (D, None, "states C2 as tau_B >> tau_S, then says slow dynamics is not the condition (F1)"),
 "book/ch18-beyond.md:69": (E, None, "capacity floor; N_H>>N_V regime not the condition"),
 "book/ch18-beyond.md:70": (E, None, "carry the visible past into future visible conditionals"),
 "book/ch18-beyond.md:268": (E, None, "gloss list with C2 'a physical-regime premise in [Main]'s typing'"),
 "book/ch18-beyond.md:276": (D, None, "'Any conscious system must implement ... substantial C1-C4 structure'; 'The C1-C4 architecture is necessary' (F3); C2 failure stated in timescale form"),
 "book/ch18-beyond.md:294": (E, None, "gloss list, application to IIT"),
 "book/ch02-substratum.md:20": (E, "2", "structural form of C2"),
 "book/ch02-substratum.md:88": (D, "2", "'C2-mixing' (F9)"),
 "book/ch02-substratum.md:192": (E, None, "C2 retention condition, slow-bath realization named"),
 "book/ch03-structural-realism.md:24": (E, None, "role summary as Methodology:162"),
 "book/appendix-b-derivations.md:22": (T, None, "characterization theorem cited without time-homogeneity (F10)"),
 "book/appendix-b-derivations.md:405": (T, None, "characterization theorem cited without time-homogeneity (F10)"),
 "book/appendix-b-derivations.md:90": (D, None, "mirror of Main:326 sentence (F2b)"),
 "book/ch09-universality.md:88": (D, None, "'the framework's structural conditions at its horizon' then C1-C4 (F2)"),
 "papers/Structure.md:734": (D, None, "'features required for C1-C4': necessity; C2 as slow-local-mixing, C3 as high-capacity (F3)"),
 "book/ch18-beyond.md:286": (D, None, "'C1-C4 architecture is necessary for non-Markovian information processing' (F3)"),
 "papers/oi_lattice_code/architecture_check.py:1086": (D, "2", "guard message string uses 'C2-mixing' (F9)"),
 LB + "DiagonalTheory.lean:359": (T, None, "uses core_isC1C4 (F14)"),
 LB + "SubstantiveCensus.lean:398": (T, None, "uses core_isC1C4 (F14)"),
 LB + "PhysicalC4Discharge.lean:148": (T, None, "cites CoreC1C4 (F14)"),
 LB + "SubstratumInterfaceAudit.lean:742": (T, None, "uses core_isC1C4 (F14)"),
 LB + "OIRealization.lean:254": (T, None, "uses core_isC1C4 (F14)"),
 LB + "RouteB.lean:85": (T, None, "core's C1-C4 is core_isC1C4 (F14)"),
 LB + "RouteB.lean:383": (T, None, "uses core_isC1C4 (F14)"),
 "book/appendix-b-derivations.md:417": (E, None, "C1 asserts non-zero coupling"),
 "book/appendix-b-derivations.md:419": (E, None, "gloss: history readback, memory persistence, sufficient capacity"),
 "book/appendix-c-objections.md:172": (D, None, "'C1-C4 structural conditions' (F2)"),
 "book/appendix-c-objections.md:291": (D, None, "'C1-C4 structural conditions' (F2)"),
 "book/README.md:74": (N, None, "application names (catalytic activity, template stability, sequence space, template-directed readback)"),
 "book/ch01-observation.md:61": (T, None, "SM Theorem 22 status: C1 'verified structurally' (F8)"),
 "book/ch01-observation.md:203": (E, "1", "C1 limit model"),
 "book/ch01-observation.md:215": (E, "2", "C2 limit model (persistence; slow bath mechanism)"),
 "book/ch01-observation.md:229": (E, "3", "C3 limit model; N_H>>N_V the comfortable regime"),
 "verification/README.md:680": (D, None, "README records 'C1 verified structurally, C2 and C3 verified with enormous margins' at the cosmological cut; GR:46-50 now say C1 not established and C2 assumption-based (F13)"),
 "verification/README.md:681": (D, None, "continuation of the README:680 status (F13)"),
 # Lean.
 LB + "IndependenceCensus.lean:25": (E, "1", "state-level instance: hidden bit drives next visible"),
 LB + "IndependenceCensus.lean:27": (D, "2", "C2 as visible period two, not hidden record persistence to readback (F14)"),
 LB + "IndependenceCensus.lean:29": (D, "3", "fibre count/saturation, no law or I* (F14)"),
 LB + "IndependenceCensus.lean:33": (E, "4", "deterministic instance of a readback gap"),
 LB + "IndependenceCensus.lean:135": (E, "1", "core_hidden_drives_visible"),
 LB + "IndependenceCensus.lean:141": (D, "2", "core_visible_period_two named C2 (F14)"),
 LB + "IndependenceCensus.lean:152": (D, "3", "core_capacity_saturates named C3 (F14)"),
 LB + "IndependenceCensus.lean:172": (E, "4", "core_history_readback"),
 LB + "IndependenceCensus.lean:182": (D, "2", "CoreC1C4 docstring: C2 'visible stream carries structural memory' (F14)"),
 LB + "IndependenceCensus.lean:183": (D, "2", "CoreC1C4 docstring continued (F14)"),
 LB + "C3Necessity.lean:2": (T, "3", "kernel C3 necessity; Realization has a bijective step (see F15)"),
 LB + "C3Necessity.lean:75": (T, "3", "c3_necessity; bijective realizations"),
 LB + "PhysicalC4Discharge.lean:15": (E, "4", "RoutedReadback explicitly not C4; consistent"),
}

def ledger_sites():
    raw = subprocess.run(["git", "show", f"{LEDGER_COMMIT}:{LEDGER_PATH}"], capture_output=True, text=True, check=True).stdout
    sites = set()
    for e in json.loads(raw)["edits"]:
        f, n = e["site"].rsplit(":", 1)
        sites.add((e["file"], f, int(n)))
    return sites

def rows():
    led = ledger_sites()
    led_chapter = {(f, n) for (_, f, n) in led}
    full_lines = open(FULL, encoding="utf8").read().split("\n")
    chapter_of = {}
    for f in MD:
        if not f.startswith("book/") or f == FULL or f.endswith("README.md"):
            continue
        for i, l in enumerate(open(f, encoding="utf8").read().split("\n"), 1):
            if PAT.search(l):
                chapter_of.setdefault(l, []).append((f, i))
    out = []
    def emit(f, i, l, matches, lean_other=False):
        mirror = ""
        src = (f, i)
        if f == FULL:
            srcs = chapter_of.get(l, [])
            mirror = ";".join(f"{a}:{b}" for a, b in srcs) or "NONE"
            src = srcs[0] if srcs else (f, i)
        rev = REVIEWED.get(f"{src[0]}:{src[1]}")
        ledger = "yes" if (src in led_chapter) else ""
        for col, cond in matches:
            if lean_other:
                cls, note = U, "label names a different object"
            elif f == "papers/GR.md" and "$'$" in l[col:col + 8]:
                cls, note = U, "(Cn$'$) labels of GR section 8, a different set"
            elif rev and (rev[1] is None or cond in rev[1]):
                cls, note = rev[0], rev[2]
            else:
                cls, note = "reference", "inline mention, rule-classified"
            a, b = max(0, col - 90), min(len(l), col + 140)
            text = l[a:b].replace("\t", " ").strip()
            out.append([f, str(i), str(col), "C" + cond, cls, ledger, mirror, note, text])
    for f in MD:
        for i, l in enumerate(open(f, encoding="utf8").read().split("\n"), 1):
            m = [(x.start(), x.group(1)) for x in PAT.finditer(l)]
            if m:
                emit(f, i, l, m)
    for f in LEAN_OI + LEAN_OTHER:
        for i, l in enumerate(open(f, encoding="utf8").read().split("\n"), 1):
            m = [(x.start(), x.group(1)) for x in PAT.finditer(l)]
            m += [(x.start(), x.group(1)) for x in PAT_LEAN_ID.finditer(l)]
            m = sorted(set(m))
            if m:
                emit(f, i, l, m, lean_other=f in LEAN_OTHER)
    for f, i in EXTRA_SITES:
        l = open(f, encoding="utf8").read().split("\n")[i - 1]
        m = [(x.start(), x.group(1)) for x in PAT.finditer(l)]
        if m:
            emit(f, i, l, m)
    return out

def render(rs):
    head = ["file", "line", "col", "cond", "class", "ledger", "mirror", "note", "text"]
    return "\n".join("\t".join(r) for r in [head] + rs) + "\n"

if __name__ == "__main__":
    allrows = rows()
    if "--full" in sys.argv:
        sys.stdout.write(render(allrows))
        sys.exit(0)
    text = render([r for r in allrows if r[4] not in ("reference", U)])
    if "--check" in sys.argv:
        ok = open(OUT, encoding="utf8").read() == text
        print("register matches" if ok else "register DRIFT")
        sys.exit(0 if ok else 1)
    open(OUT, "w", encoding="utf8").write(text)
    print(f"wrote {OUT}")
