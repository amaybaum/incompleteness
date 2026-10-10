"""Exploratory pass over raw.log (counts and locations only).

Usage: python3 -I explore.py <raw.log>
"""
import re
import sys

with open(sys.argv[1], "r", encoding="utf-8", newline="") as fh:
    text = fh.read()

lines = text.split("\n")
print("chars:", len(text))
print("split('\\n') count:", len(lines), "| ends with newline:", text.endswith("\n"))
print("splitlines() count:", len(text.splitlines()), "| '\\r' count:", text.count("\r"))
print("BOM present:", "﻿" in text)

ts_re = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z)")
no_ts = [i for i, l in enumerate(lines, 1) if not ts_re.match(l)]
print("lines without leading timestamp:", len(no_ts), no_ts[:10])
print("first line:", repr(lines[0][:200]))
print("last line:", repr(lines[-1][:200]))

hits = [(i, l) for i, l in enumerate(lines, 1) if "CompositeDimension" in l]
print("\nlines mentioning 'CompositeDimension':", len(hits))
for i, l in hits[:80]:
    print(f"  L{i}: {l[:220]!r}")

# Lake progress lines (Built/Replayed/Building ...) for orientation
prog = [(i, l) for i, l in enumerate(lines, 1)
        if re.search(r"\[\d+/\d+\]", l)]
print("\nlake progress lines '[n/m]':", len(prog))
for i, l in prog[:60]:
    print(f"  L{i}: {l[:200]!r}")
if len(prog) > 60:
    print("  ...")
    for i, l in prog[-20:]:
        print(f"  L{i}: {l[:200]!r}")

# GitHub step group markers for orientation
grp = [(i, l) for i, l in enumerate(lines, 1) if "##[group]" in l or "##[endgroup]" in l]
print("\n##[group]/##[endgroup] lines:", len(grp))
for i, l in grp[:80]:
    print(f"  L{i}: {l[:200]!r}")
