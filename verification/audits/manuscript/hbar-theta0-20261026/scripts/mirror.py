"""Map pattern-matching lines between book chapters and the FULL mirror.

Usage: python3 -I mirror.py SNAPROOT PATTERN
For each chapter line matching PATTERN, print chapter:line -> FULL line(s) with identical text.
Then list FULL lines matching PATTERN that have no identical chapter line (divergences).
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1])
pat = re.compile(sys.argv[2], re.I)
book = root / "book"
full_name = "The-Incompleteness-of-Observation-FULL.md"
full = (book / full_name).read_text(encoding="utf-8").splitlines()
full_index = {}
for i, l in enumerate(full, 1):
    full_index.setdefault(l.strip(), []).append(i)

chap_lines = set()
for p in sorted(book.glob("*.md")):
    if p.name == full_name or p.name == "README.md":
        continue
    for n, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if pat.search(l):
            key = l.strip()
            chap_lines.add(key)
            print(f"{p.name}:{n} -> FULL {full_index.get(key, 'ABSENT')}")
print("--- FULL lines matching with no identical chapter line:")
for i, l in enumerate(full, 1):
    if pat.search(l) and l.strip() not in chap_lines:
        print(f"FULL:{i}: {l[:160]}")
