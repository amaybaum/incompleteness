#!/usr/bin/env python3
"""staleness_check.py — is every built .tex still the build of its own source?

Every round of the b271-b277 audit hit the same failure: a .md was edited, the
.tex/.pdf were not rebuilt, and nothing recorded it. bundle_check, the mirror
check and the citation audit all pass in that state, because none of them
compares a source against its own build.

build.sh now appends `% source-sha256: <hash of the .md>` to each .tex it
generates. This compares that stamp against the current source. Exact: no
heuristics, no false positives. Artifacts built before the stamp existed report
UNSTAMPED and do not fail the run; they clear on the next build.

Usage:  python3 staleness_check.py [--root DIR]
Exit 1 only on a genuine mismatch.
"""
import hashlib, os, re, sys

STAMP = re.compile(r'^% source-sha256: ([0-9a-f]{64})\s*$', re.M)

def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()

def pairs(root):
    out = []
    pdir = os.path.join(root, 'papers')
    if os.path.isdir(pdir):
        for f in sorted(os.listdir(pdir)):
            if f.endswith('.md'):
                out.append((f[:-3], os.path.join(pdir, f),
                            os.path.join(pdir, f[:-3] + '.tex')))
    book = os.path.join(root, 'book', 'The-Incompleteness-of-Observation-FULL')
    if os.path.exists(book + '.md'):
        out.append(('book', book + '.md', book + '.tex'))
    return out

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    stale, unstamped, ok = [], [], 0
    for name, md, tex in pairs(root):
        if not os.path.exists(tex):
            unstamped.append((name, 'no .tex artifact'))
            continue
        m = STAMP.search(open(tex, encoding='utf-8', errors='replace').read())
        if not m:
            unstamped.append((name, 'built before stamping'))
            continue
        if m.group(1) != sha(md):
            stale.append(name)
            print(f"  STALE  {name:18s} .tex was built from a different source")
        else:
            ok += 1
            print(f"  ok     {name:18s} stamp matches source")
    for n, why in unstamped:
        print(f"  ----   {n:18s} UNSTAMPED ({why}); rebuild to enable")
    print()
    if stale:
        for n in stale:
            print(f"staleness_check: {n}.tex/.pdf do NOT match {n}.md "
                  f"— run ./build.sh {n}")
        print("staleness_check: FAILED")
        return 1
    print(f"staleness_check: OK ({ok} matched, {len(unstamped)} unstamped)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
