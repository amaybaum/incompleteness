#!/usr/bin/env python3
"""Supplementary citation check (coordinator, bridge round 4): for every `Name.lean:NNN` citation in the lines added
since 7abe4da4, take ALL identifier-like tokens on the citing line (snake_case or dotted names with an underscore or
a capital, backticked or not), and test whether any occurs in the window [NNN-1, NNN+3] of the file at L.  Prints
the citations whose window names none of the line's identifiers, with the citing line and the cited line."""
import re, subprocess, sys
repo, wt, thread, r1 = sys.argv[1:5]
L = '9f9f8257a980a1819fbbc1dc0019917cf8678626'
cache = {}
def file_at_L(name):
    if name not in cache:
        p = subprocess.run(['git', '-C', repo, 'show', f'{L}:verification/lean-mathlib/OIBridge/{name}.lean'], capture_output=True, text=True)
        cache[name] = p.stdout.splitlines() if p.returncode == 0 else None
    return cache[name]
diff = subprocess.run(['git', '-C', wt, 'diff', f'{r1}..HEAD', '--', f'research/{thread}'], capture_output=True, text=True).stdout
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
cit_re = re.compile(r'\b([A-Z][A-Za-z0-9]+)\.lean:(\d+)')
tok_re = re.compile(r"[A-Za-z][A-Za-z0-9_'.]*")
hits = {}
for line in added:
    for name, num in cit_re.findall(line):
        ids = [t for t in tok_re.findall(line) if ('_' in t) and not t.endswith('.lean') and not t.endswith('.py')]
        hits.setdefault((name, int(num)), []).append((ids, line.strip()[:200]))
n_ok = n_bad = 0
for (name, num), lst in sorted(hits.items()):
    lines = file_at_L(name)
    if lines is None or num < 1 or num > len(lines):
        print('MISSING', name, num); n_bad += 1; continue
    window = '\n'.join(lines[max(0, num - 2): num + 3])
    allids = set(i for ids, _ in lst for i in ids)
    found = sorted(i for i in allids if re.search(r'(?<![A-Za-z0-9_\'.])' + re.escape(i.split('.')[-1]) + r'(?![A-Za-z0-9_\'])', window))
    if found:
        n_ok += 1
    else:
        n_bad += 1
        print(f'UNMATCHED {name}.lean:{num}  cited line: {lines[num-1].strip()[:110]}')
        for ids, l in lst[:2]:
            print(f'    citing: {l[:170]}')
print(f'SUMMARY supp: {len(hits)} citations; window names an identifier of the citing line: {n_ok}; unmatched: {n_bad}')
