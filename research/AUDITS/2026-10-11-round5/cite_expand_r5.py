#!/usr/bin/env python3
"""Expand the shorthand kernel citations `File.lean:NNN, :MMM, ...` in a thread's round-5 added lines (inbox excluded)
and resolve every one at L = 9f9f8257: the cited line must exist, and the declaration whose header is at the cited line,
or nearest above it within 12 lines, is printed so the citation can be read against the prose that cites it.
Usage: python3 -I -B cite_expand_r5.py <repo> <worktree> <thread> <r4head>
Prints RESOLVED <File>:<line> -> <keyword> <name> (header line h) or MISSING; a final SUMMARY line.
"""
import re, subprocess, sys
repo, wt, thread, r4 = sys.argv[1:5]
L = '9f9f8257a980a1819fbbc1dc0019917cf8678626'
diff = subprocess.run(['git', '-C', wt, 'diff', f'{r4}..HEAD', '--', f'research/{thread}',
                       f':(exclude)research/{thread}/inbox'], capture_output=True, text=True).stdout
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
grp = re.compile(r'\b([A-Z][A-Za-z0-9]+)\.lean:(\d+)((?:\s*,\s*:\d+)*)')
cites = []
for line in added:
    for name, first, rest in grp.findall(line):
        nums = [int(first)] + [int(x) for x in re.findall(r':(\d+)', rest)]
        for n in nums:
            if (name, n) not in cites:
                cites.append((name, n))
cache = {}
def src(name):
    if name not in cache:
        p = subprocess.run(['git', '-C', repo, 'show', f'{L}:verification/lean-mathlib/OIBridge/{name}.lean'],
                           capture_output=True, text=True)
        cache[name] = p.stdout.splitlines() if p.returncode == 0 else None
    return cache[name]
hdr = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+)*'
                 r'(theorem|lemma|def|abbrev|structure|inductive|instance|class)\s+([^\s:({\[]+)')
ok = 0
for name, n in cites:
    s = src(name)
    if s is None or n > len(s):
        print(f'MISSING   {name}.lean:{n}' + (' (no such file at L)' if s is None else f' (file has {len(s)} lines)'))
        continue
    found = None
    for h in range(n, max(0, n - 13), -1):
        m = hdr.match(s[h - 1])
        if m:
            found = (h, m.group(1), m.group(2))
            break
    ok += 1
    print(f'RESOLVED  {name}.lean:{n} -> ' + (f'{found[1]} {found[2]} (header line {found[0]})' if found else
                                            f'no declaration header within 12 lines above: {s[n - 1].strip()[:90]!r}'))
print(f'SUMMARY {thread}: {len(cites)} expanded citations in added lines since {r4[:8]}; resolved at L {ok}; '
      f'missing {len(cites) - ok}')
