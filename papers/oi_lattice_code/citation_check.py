#!/usr/bin/env python3
# citation_check.py — b94 (2026-08-13)
# Guard against the recurring defect class: a corpus sentence citing a probe
# file that does not exist in the repository (the p35a packaging gap, and the
# lg_comb.py rename caught by the p50 audit). Scans every paper, book chapter
# and README for `something.py` citations and verifies each names a real file
# under papers/oi_lattice_code/. Exit 0 iff every citation resolves.
import os, re, sys, glob

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
have = {}
for dirpath, _, files in os.walk(os.path.join(root, "papers", "oi_lattice_code")):
    for fn in files:
        if fn.endswith(".py"):
            have[fn] = os.path.relpath(os.path.join(dirpath, fn), root)

targets = sorted(glob.glob(os.path.join(root, "papers", "*.md"))) \
        + sorted(glob.glob(os.path.join(root, "book", "*.md"))) \
        + [os.path.join(root, "README.md")]

cited, broken = 0, []
for path in targets:
    if not os.path.exists(path): continue
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"`([A-Za-z0-9_]+\.py)`", text):
        name = m.group(1); cited += 1
        if name not in have:
            line = text[:m.start()].count("\n") + 1
            broken.append((os.path.relpath(path, root), line, name))

for f, ln, n in broken:
    print(f"BROKEN CITATION  {f}:{ln}  ->  {n} (no such file under papers/oi_lattice_code/)")
print(f"citation_check: {cited} citation(s), {len(broken)} broken")
sys.exit(1 if broken else 0)
