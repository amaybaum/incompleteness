#!/usr/bin/env python3
"""Coordinator's citation check for the round-2 documents of research/bridge, research/countermodels and
research/equivalence.  For each thread it takes the lines ADDED since the round-1 audited head (git diff r1..HEAD over
research/<thread>/**/*.md), extracts every `Name.lean:NNN` citation, resolves it against
verification/lean-mathlib/OIBridge/Name.lean at L = 9f9f8257 (git show from the repository), and checks that some
backticked identifier on the same document line occurs within the window [NNN-1, NNN+3] of the cited file.
Run: python3 -I -B cite_check_r2b.py <repo> <worktree> <thread> <r1head>
DECISION RULE (fixed before the first run): a citation is RESOLVED if the file exists at L and the line exists;
NAMED if in addition a backticked identifier of the citing line occurs in the window (or the line names none);
the thread passes iff every citation is RESOLVED and NAMED.  Prints per-citation lines and a summary.
"""
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
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++') and l[1:].lstrip().startswith(('#', '|', '-', '*', '`', '>', '[', '(', '"', "'")) or (l.startswith('+') and not l.startswith('+++'))]
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
cit_re = re.compile(r'\b([A-Z][A-Za-z0-9]+)\.lean:(\d+)')
id_re = re.compile(r'`([A-Za-z_][A-Za-z0-9_\'.]*)`')
seen = {}; order = []
for line in added:
    if '.md' in line and line.lstrip().startswith(('+++', 'diff')): continue
    ids = [i for i in id_re.findall(line) if not i.endswith('.lean') and not i.endswith('.py') and not i.endswith('.md')]
    for name, num in cit_re.findall(line):
        key = (name, int(num))
        if key not in seen: seen[key] = set(); order.append(key)
        seen[key].update(ids)
ok_all = True; n_res = n_named = n_unnamed = 0
for name, num in order:
    lines = file_at_L(name)
    if lines is None or num < 1 or num > len(lines):
        print(f'MISSING {name}.lean:{num}'); ok_all = False; continue
    n_res += 1
    window = '\n'.join(lines[max(0, num - 2): num + 3])
    ids = seen[(name, num)]
    hit = [i for i in ids if re.search(r'(?<![A-Za-z0-9_\'.])' + re.escape(i.split('.')[-1]) + r'(?![A-Za-z0-9_\'])', window)]
    if not ids:
        n_unnamed += 1; print(f'RESOLVED {name}.lean:{num} (no identifier named on the citing lines)')
    elif hit:
        n_named += 1; print(f'RESOLVED+NAMED {name}.lean:{num} {sorted(hit)[:4]}')
    else:
        ok_all = False; print(f'RESOLVED-UNNAMED {name}.lean:{num} names {sorted(ids)[:6]} not in window: {lines[num-1].strip()[:90]}')
print(f'SUMMARY {thread}: {len(order)} distinct citations in added lines since {r1}; resolved {n_res}; named-and-found {n_named}; unnamed {n_unnamed}')
print(f'CITATIONS-{thread.upper()}-' + ('RESOLVE' if ok_all else 'FAIL'))
