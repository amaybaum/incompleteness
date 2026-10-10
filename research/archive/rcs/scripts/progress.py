import re, sys
s = open(sys.argv[1], encoding="utf-8", newline="").read()
lines = s.split("\n")
ts = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) ?")
prog = re.compile(r"\[(\d+)/(\d+)\]")
hits = [(i + 1, l) for i, l in enumerate(lines) if prog.search(ts.sub("", l, count=1))]
print("lines containing [k/n]:", len(hits))
for n, l in hits:
    print(n, repr(l))
print("--- lines containing 'Build completed' / 'Build failed' / 'jobs)' ---")
for i, l in enumerate(lines):
    b = ts.sub("", l, count=1)
    if re.search(r"Build (completed|failed)|\bjobs\)", b):
        print(i + 1, repr(l))
