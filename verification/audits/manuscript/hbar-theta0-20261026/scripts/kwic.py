"""Keyword-in-context grep over the snapshot corpus.

Usage: python3 -I kwic.py ROOT PATTERN [WIDTH] [file-glob ...]
Prints file:line and a window of WIDTH chars around each regex match.
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1])
pat = re.compile(sys.argv[2], re.I)
width = int(sys.argv[3]) if len(sys.argv) > 3 else 220
globs = sys.argv[4:] or ["papers/*.md", "book/*.md"]
for g in globs:
    for p in sorted(root.glob(g)):
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for m in pat.finditer(line):
                a, b = max(0, m.start() - width), min(len(line), m.end() + width)
                print(f"{p.relative_to(root)}:{n}: ...{line[a:b]}...")
