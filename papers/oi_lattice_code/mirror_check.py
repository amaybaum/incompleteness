#!/usr/bin/env python3
# mirror_check.py — b108 (2026-08-13)
# The book is maintained as chapter sources PLUS an assembled FULL.md mirror.
# Editing one and not the other leaves the corpus with two wordings for the same
# passage and no rule saying which governs — a defect that has now produced two
# partial-merge incidents and one review finding. This asserts the mirror rule:
# every nonblank line of every chapter must appear verbatim in FULL.md.
# Exclusions are structural, not convenience: book/README.md and bibliography.md
# are repository furniture, not assembled chapters.
import os, sys, glob

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
full_path = os.path.join(root, "book", "The-Incompleteness-of-Observation-FULL.md")
if not os.path.exists(full_path):
    print("mirror_check: FULL.md not found"); sys.exit(1)
full = set(l.strip() for l in open(full_path, encoding="utf-8").read().split("\n") if l.strip())

EXCLUDE = {"README.md", "bibliography.md", "The-Incompleteness-of-Observation-FULL.md"}
missing = []
for path in sorted(glob.glob(os.path.join(root, "book", "*.md"))):
    name = os.path.basename(path)
    if name in EXCLUDE: continue
    for i, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        s = line.strip()
        if s and s not in full:
            missing.append((name, i, s[:100]))

for n, i, s in missing[:20]:
    print(f"MIRROR DIVERGENCE  book/{n}:{i}\n    {s}")
if len(missing) > 20: print(f"    … and {len(missing)-20} more")
print(f"mirror_check: {len(missing)} chapter line(s) absent from FULL.md")
sys.exit(1 if missing else 0)
