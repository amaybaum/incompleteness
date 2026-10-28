"""SC-37 re-grep and diff checks.

Usage: python3 -I check.py <repo-root> [base-commit]

1. Stale: the superseded unconditional wordings occur nowhere in the corpus.
2. Mirror: each corrected book sentence occurs in its chapter and in the FULL book equally often.
3. Inventory: corpus sentences that pair a cosmological-constant term with a dissolution or
   gravitation verb, split into those carrying a conditional marker in the same sentence and
   those without one (the latter are listed for the dispositions in README.md).
4. Added lines: register (AGENTS.md section A.32/A.33), revision voice, caps emphasis,
   secret patterns and local filesystem paths.
"""
import pathlib
import re
import subprocess
import sys

root = pathlib.Path(sys.argv[1])
base = sys.argv[2] if len(sys.argv) > 2 else "0d917665"
FULL = "book/The-Incompleteness-of-Observation-FULL.md"
corpus = sorted(list(root.glob("papers/*.md")) + list(root.glob("book/*.md")))
corpus = [f for f in corpus if f.name != "Introduction.md"]
text = {str(f.relative_to(root)): f.read_text() for f in corpus}
fail = 0

STALE = [
    "the metric evolves via Einstein's equations *before* the trace-out",
    "The framework denies that the *absolute* zero-point sum gravitates",
    "The framework denies that $\\rho_{\\text{QFT}}$ gravitates",
    "The framework denies that the zero-point energy gravitates",
    "§8.3 denies that the emergent zero-point sum gravitates absolutely",
    "Section 7.7's dissolution denies",
    "The metric tensor evolves via Einstein's field equations",
    "it is not a source term in Einstein's equations, because",
    "the other predicts the observed value",
    "One predicts the observed vacuum energy",
    "the proofs are complete",
    "The emergent action scale is determined by the boundary geometry",
    "$\\hbar$ is determined by the boundary geometry",
    "Dissolution of the Cosmological Constant Problem",
    "## 7.7 Dissolution of the cosmological constant problem",
    "## 19.2 Problems resolved",
    "Derived (total budget",
    "The framework derives the total budget",
    "the dissolution of the cosmological constant problem at the descriptive level",
    "the $10^{122}$ ratio is a compression ratio, not a failure of cancellation",
    "geometry-first dissolution",
    "This is what makes the CC dissolution work",
    "turn out to be category errors (cosmological constant,",
    "But gravity is sourced by the classical Hamiltonian",
    "requires the geometry-first ordering established in §6.2",
    "*Under Lemmas 1–3 and conditions (C1)–(C4), the cosmological trace-out",
    "The total dark sector budget is established by §7.2",
    "\\Omega_\\Lambda \\approx 95\\%$ | consistent |",
    "predates the trace-out (does gravitate)",
    "the boundary entropy: gravitationally active",
    "This track record is itself evidence for the ordering",
    "it's existing evidence, not a future hope",
    "Because, on the framework's proposal, the spacetime metric",
    "the gauge status of the uniform vacuum offset",
    "(Chapter 7 §7.6, via the reconstruction theorem's energy-shift freedom)",
    "The uniform component is dark energy; the structured component",
    "concordance rather than puzzle — though the total fraction is partly definitional",
    "The remaining ~95% is boundary entropy — gravitationally active",
    "The dark sector of cosmological observation is the gravitational effect",
    "The dark sector is the gravitational weight of the unreadable storage",
    "The dark sector is the gravitational effect of the unreadable storage",
    "*by theorem*; its uniform component is dark energy",
    "so roughly ninety-five percent of the critical density is invisible to every embedded observer",
    "in the flagship case, its energetic content",
    "invisible to every embedded observer *by theorem*",
    "This is a theorem of Part I",
    "The paper proves that this entropy has no operator",
    "That doesn't prove the ordering is correct",
    "The contrast is conditional on that open step.",
    "the dark sector budget as a partly definitional concordance",
    "(information preservation, dark sector budget, no DM particle, no proton decay)",
    "Tier 1 has five entries",
    "Tier 2 has seven entries",
    "The seven Tier 2 entries",
    "\\Omega_{\\text{dark}} \\approx 95\\%$ | $\\Omega_{\\text{CDM}}",
    "The framework predicts that dark energy is the uniform component",
    "The dark-sector corollary predicts that ~95%",
    "The dark-sector corollary explains ~95%",
]
print("1. stale wordings (expect 0 each)")
for s in STALE:
    n = sum(t.count(s) for t in text.values())
    print(f"   {n}  {s}")
    fail += n != 0

MIRROR = {
    "book/ch07-gravity.md": [
        "## 7.7 The cosmological constant: descriptive distinction and conditional dissolution",
        "its covariant field equations and their source coupling are the open G3 step",
        "The emergent action scale depends only on the boundary geometry",
        "The framework's geometry-first proposal converges",
        "convergence with the framework's geometry-first proposal",
        "while on Section 7.7's proposal, conditional on the coupling step,",
        "Their gravitational reading is conditional on the open G3 coupling step ([GR §6.2])",
        "(on the same proposal, does gravitate)",
        "Conditional on the coupling step, the two are not commensurable as gravitational sources",
    ],
    "book/ch03-structural-realism.md": [
        "on the geometry-first proposal, the dark sector is the gravitational effect",
        "so, by the construction of the trace-out ([GR §7.2], step (ii-a)), it is invisible to the emergent quantum description; on the geometry-first proposal, conditional on the open coupling step (G3)",
        "a dimensional factor $1/6$ imported from Verlinde (Chapter 7 §§7.8–7.9)",
        "in the flagship case and conditional on the open coupling step, its energetic content",
    ],
    "book/ch00-introduction.md": [
        "the descriptive distinction behind a dissolution of the cosmological constant problem conditional on the open coupling step",
        "combining the conditional CC dissolution",
    ],
    "book/ch02-substratum.md": [
        "On the geometry-first proposal, the dark sector of cosmological observation","a reading on which the problem dissolves conditional on the open coupling step (G3)"],
    "book/ch09-universality.md": [
        "(conditional cosmological constant dissolution,",
        "levels (Chapter 7 §7.7), so that,",
        "([Main §3.4]; [GR §8.3]),",
        "another ([Main §3.4]; [GR §8.3]), which is why",
        "gauge outright for every quantum statistic and, conditional on the coupling step,",
        "the dark-sector budget only as a partly definitional count ($1-\\Omega_B$ by construction)",
        "is Tier 2 and conditional on the open G3 matter-to-boundary coupling (Chapter 7 §7.9)",
        "gravitational explanation conditional on the open G3 coupling | Ch 7 §7.9 |",
        "| No dark matter particle | XENON, LUX, etc. null; conditional dark-sector interpretation | Ch 7 §7.9 |",
    ],
    "book/ch18-beyond.md": [
        "**The first conditional dissolution: the cosmological constant.**",
        "On that reading, and conditional on the coupling step, the ratio is not a fine-tuning failure.",
        "is that, conditional on the coupling step, the two energy scales",
    ],
    "book/ch19-open-problems.md": [
        "## 19.2 Problems addressed",
        "Conditional on that step, the two energy scales",
        "**Framework status.** Partly definitional (the total fraction is $1-\\Omega_B$ by construction;",
        "The framework supplies the total budget, partly by definition;",
        "| Partly definitional ($1-\\Omega_B$ by construction); physical interpretation conditional on the coupling step | Ch 7 §7.9 |",
        "the physical interpretation is conditional on the coupling step.",
        "On the geometry-first proposal, the uniform component is dark energy",
        "The framework predicts, on the geometry-first proposal, that dark energy",
        "The conditional cosmological constant dissolution, the measurement problem",
    ],
    "book/appendix-c-objections.md": [
        "the status of each — proved, conditional or open — is recorded with it",
        "(the cosmological constant, conditional on the open coupling step;",
    ],
    "book/readers-guide.md": ["the conditional cosmological constant dissolution)"],
}
print("2. chapter/FULL mirror (counts must match and be >= 1)")
for ch, phrases in MIRROR.items():
    for s in phrases:
        a, b = text[ch].count(s), text[FULL].count(s)
        ok = a >= 1 and a == b
        print(f"   {'ok ' if ok else 'BAD'} {a}/{b}  {ch}: {s[:70]}")
        fail += not ok

PINS = {
    "papers/GR.md": [
        "By the construction of the trace-out, no hidden-sector degree of freedom maps to an operator on $\\mathcal{H}_V$, which is spanned by the visible configurations.",
        "$\\Omega_{\\text{dark}} \\approx 95\\%$ (conditional on the coupling step) |",
        "*Under Lemmas 1–3, conditions (C1)–(C4) and the geometry-first proposal of §6.2 (conditional on the open coupling step),",
        "the metric belongs to the substratum, prior to the trace-out, and its covariant field equations and their source coupling are the open G3 step.",
        "On the geometry-first proposal (§6.2), conditional on the open coupling step, the *absolute* zero-point sum does not gravitate",
    ],
    "papers/Explainer.md": [
        "By the construction of the trace-out, this entropy has no operator in the emergent QFT.",
        "reads the discrepancy as a derived quantity. (Note the division of labor",
        "the other, if the coupling step holds, carries the observed value as a normalization",
    ],
}
PINS["papers/GR.md"] += [
    "Their gravitational reading is conditional on the open G3 coupling step (§6.2)",
    "conditional on §3.2 and on the open coupling step of §6.2",
    "The dark-sector phenomenology is Tier 2 and conditional:",
]
PINS["papers/Structure.md"] = ["dark-sector phenomenology (its gravitational reading conditional on the open coupling step of [GR §6.2])"]
print("2b. paper pins (expect exactly 1 each)")
for pth, phrases in PINS.items():
    for ph in phrases:
        k = text[pth].count(ph)
        print(f"   {'ok ' if k == 1 else 'BAD'} {k}  {pth}: {ph[:70]}")
        fail += k != 1

# 2c. Tier counts in Chapter 9 are computed from the tables, not hard-coded: each stated count
# must equal the number of rows of its table, in the chapter and in FULL.
WORDS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve"
                                    " thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
def rows(t, header):
    i = t.index(header)
    n = 0
    for line in t[i:].splitlines()[2:]:
        if not line.startswith("|"):
            break
        n += 1
    return n
def num(w):
    return WORDS[w.lower()]
print("2c. Chapter 9 tier counts (stated vs table rows)")
for pth in ("book/ch09-universality.md", FULL):
    t = text[pth]
    n = {k: rows(t, f"| Tier {k} prediction |") for k in (1, 2, 3)}
    stated = [
        (1, re.search(r"Tier 1 has (\w+) entries", t)),
        (1, re.search(r"(\w+) universality-class entries tested", t)),
        (2, re.search(r"Tier 2 has (\w+) entries", t)),
        (2, re.search(r"The (\w+) Tier 2 entries", t)),
        (3, re.search(r"Tier 3 has (\w+) entries", t)),
        (3, re.search(r"The (\w+) Tier 3 entries", t)),
    ]
    for k, m in stated:
        v = num(m.group(1)) if m else None
        ok = v == n[k]
        print(f"   {'ok ' if ok else 'BAD'} {pth}: Tier {k} stated {v}, table {n[k]}  ({m.group(0) if m else 'missing'})")
        fail += not ok
    m = re.search(r"The three tiers contain (\w+) entries", t)
    v = num(m.group(1)) if m else None
    ok = v == sum(n.values())
    print(f"   {'ok ' if ok else 'BAD'} {pth}: total stated {v}, tables {sum(n.values())}")
    fail += not ok

CC = re.compile(r"cosmological[- ]constant|vacuum[- ]energy|zero[- ]point|10\^\{?122|\\Lambda|Λ|\bCC\b"
                r"|dark[- ]sector|boundary entropy|\\rho_s\b|energy scales|the two are", re.I)
DIS = re.compile(r"dissol|resolv|\bsolv|commensurable|is dark (?:energy|matter)|gravitational effect"
                 r"|gravitationally active|budget is", re.I)
GRAV = re.compile(r"gravitat|sourc\w* (?:of )?(?:gravity|curvature|geometry)|Einstein'?s (?:field )?equations|field equations never", re.I)
COND = re.compile(r"conditional|condition|proposal|propos|G3|coupling (?:step|theorem|obligation)|on (?:that|its|the framework's) reading|if the", re.I)
SPLIT = re.compile(r"(?<=[.;!?])\s+(?=[A-Z*(\[])")
marked, unmarked = 0, []
for p, t in text.items():
    if p == FULL:
        continue
    for n, line in enumerate(t.splitlines(), 1):
        for s in SPLIT.split(line):
            if CC.search(s) and (DIS.search(s) or GRAV.search(s)):
                if COND.search(s):
                    marked += 1
                else:
                    unmarked.append(f"{p}:{n}  {s[:150]}")
print(f"3. inventory (chapters and papers; FULL mirrors the chapters): {marked} sentences with a "
      f"conditional marker, {len(unmarked)} without")
for u in unmarked:
    print("   " + u)

diff = subprocess.run(["git", "-C", str(root), "diff", "-U0", base, "--", ".", ":(exclude)*.pdf",
                       ":(exclude)*.tex", ":(exclude)*/SC37-g3-conditional/check.out"], capture_output=True, text=True, check=True).stdout
added, removed, cur = [], {}, None
for l in diff.split("\n"):
    if l.startswith("+++ "):
        cur = l[6:]
    elif l.startswith("+") and not l.startswith("+++"):
        added.append((cur, l[1:]))
    elif l.startswith("-") and not l.startswith("---"):
        removed.setdefault(cur, []).append(l[1:])
REG = [r"discipline", r"honest", r"temptation", r"stated in that register", r"\bthroughout\b",
       r"should not be read", r"the reader should", r"should be read", r"neither borrows",
       r"\bis now\b", r"now settled", r"in its current form", r"the corrected form", r"as redefined",
       r"no longer", r"formerly", r"previously", r"earlier revision", r"withdrawn", r"is not listed",
       r"\bwe note\b", r"remarkabl", r"elegant", r"striking", r"impressive"]
WL = {"OI", "QM", "QFT", "CMB", "DESI", "JUNO", "PDF", "DOI", "GR", "SM", "FULL", "CON", "README"}
SEC = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_", r"AKIA[0-9A-Z]{16}", r"-----BEGIN", r"xox[baprs]-",
       r"sk-[A-Za-z0-9]{20,}", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}", r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
       r"https?://[^\s)]*[?&](sig|token|X-Amz)", r"(?i)(api[_-]?key|secret|password)\s*[:=]",
       r"/tmp/", r"/home/", r"/root/", r"scratchpad"]
reg = sec = 0
# Register and caps: a hit counts only where the edit adds an occurrence (count in the
# file's added lines above its count in the removed lines), so untouched wording on an
# edited line is not attributed to this change.
def caps(t):
    t = re.sub(r"`[^`]*`", "", t)
    t = re.sub(r"\$[^$]*\$", "", t)
    return [m.group(0) for m in re.finditer(r"(?<=[a-z,;] )[A-Z]{4,}\b", t) if m.group(0) not in WL]
files = sorted({f for f, _ in added})
for f in files:
    if not (f.endswith(".md") and (f.startswith("papers/") or f.startswith("book/"))):
        continue
    a = "\n".join(l for g, l in added if g == f)
    r_ = "\n".join(removed.get(f, []))
    for r in REG:
        if len(re.findall(r, a, re.I)) > len(re.findall(r, r_, re.I)):
            print("   REGISTER", f, r); reg += 1
    ca, cr = caps(a), caps(r_)
    for w in sorted(set(ca)):
        if ca.count(w) > cr.count(w):
            print("   CAPS", f, w); reg += 1
for f, l in added:
    for r in SEC:
        if f.endswith("SC37-g3-conditional/check.py"):
            continue  # this file holds the pattern list itself
        if re.search(r, l):
            print("   SECRET/PATH?", f, r); sec += 1
print(f"4. added lines: {len(added)}; register/caps hits: {reg}; secret/path hits: {sec}")
fail += reg + sec
print("RESULT", "PASS" if fail == 0 else f"FAIL ({fail})")
sys.exit(1 if fail else 0)
