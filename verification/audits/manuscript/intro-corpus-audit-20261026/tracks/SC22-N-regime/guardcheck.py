"""Load architecture_check.py INVARIANTS without running its scan, and test candidate replacement texts."""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
cut = src.index("# --- self-test")
ns = {"__file__": sys.argv[1]}
exec(compile(src[:cut], "architecture_check_head", "exec"), ns)
INV = ns["INVARIANTS"]
texts = open(sys.argv[2], encoding="utf-8").read().split("\n@@\n")
bad = 0
for i, t in enumerate(texts, 1):
    for pat, why, exc, ex in INV:
        for m in re.finditer(pat, t):
            w = t[max(0, m.start()-160):m.start()+160]
            if any(re.search(e, w) for e in exc): continue
            bad += 1; print(f"text {i}: HIT '{m.group(0)[:60]}' -> {why}")
    for m in re.finditer(r"(?<![A-Za-z{\\$])[A-Z]{4,}(?![A-Za-z])", t):
        print(f"text {i}: caps '{m.group(0)}'")
    for ph in ["formerly", "no longer", "is now", "in its current form", "corrected form", "as redefined", "should not be read", "the reader should"]:
        if ph in t: print(f"text {i}: history/reader phrase '{ph}'")
print(f"{len(INV)} invariants, {len(texts)} texts, {bad} hits")
