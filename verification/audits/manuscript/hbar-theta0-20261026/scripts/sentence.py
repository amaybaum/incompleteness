"""Print the sentence(s) of FILE:LINE that match PATTERN.

Usage: python3 -I sentence.py SNAPROOT PATTERN rel/path:LINE [rel/path:LINE ...]
Sentences are split naively on '. ' boundaries outside $...$ math.
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1])
pat = re.compile(sys.argv[2], re.I)


def sentences(line):
    out, buf, math = [], "", False
    i = 0
    while i < len(line):
        ch = line[i]
        buf += ch
        if ch == "$":
            math = not math
        if not math and ch == "." and (i + 1 == len(line) or line[i + 1] == " "):
            out.append(buf.strip())
            buf = ""
        i += 1
    if buf.strip():
        out.append(buf.strip())
    return out


for spec in sys.argv[3:]:
    path, n = spec.rsplit(":", 1)
    line = (root / path).read_text(encoding="utf-8").splitlines()[int(n) - 1]
    for s in sentences(line):
        if pat.search(s):
            print(f"{spec}: {s}\n")
