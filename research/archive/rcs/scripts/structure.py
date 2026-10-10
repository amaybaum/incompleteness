import re, sys
p = sys.argv[1]
s = open(p, encoding="utf-8", newline="").read()
lines = s.split("\n")
print("chars:", len(s), "newlines:", s.count("\n"), "lines(split):", len(lines))
print("CR count:", s.count("\r"))
ts = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) ?")
first = next((l for l in lines if ts.match(l)), None)
last = next((l for l in reversed(lines) if ts.match(l)), None)
print("first line:", repr(lines[0][:200]))
print("last line:", repr(lines[-1][:300]))
print("first ts:", ts.match(first).group(1) if first else None)
print("last ts:", ts.match(last).group(1) if last else None)
nots = [i for i, l in enumerate(lines) if not ts.match(l)]
print("lines without timestamp prefix:", len(nots), nots[:10])
print("--- ##[ markers ---")
for i, l in enumerate(lines):
    body = ts.sub("", l, count=1)
    if body.startswith("##[") or "##[" in body:
        print(i + 1, repr(body[:220]))
