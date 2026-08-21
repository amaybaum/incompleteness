#!/usr/bin/env python3
"""toolchain_check.py - can this tree actually be rebuilt?

The other checks all compare artifacts to sources or documents to each other.
None of them notices if the BUILD ENTRY POINT is missing: a tree with no
build.sh passes staleness, voice, mirror, citation and architecture cleanly,
because every existing artifact still matches its existing source. It simply
cannot be regenerated. This check looks at the tooling itself.

  1. the build entry point exists and is non-empty
  2. every file path build.sh references resolves
  3. all copies of the shared header are byte-identical (a glyph fix applied
     to one copy and not the others silently drops glyphs from the others)
  4. every tools/*.py named in release_gate.py is present

Usage:  python3 tools/toolchain_check.py [--root DIR]
Exit 1 on any failure.
"""
import os, re, sys

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    bad = []

    build = os.path.join(root, 'build.sh')
    if not os.path.exists(build):
        bad.append("build.sh MISSING - the tree cannot be rebuilt")
    elif os.path.getsize(build) == 0:
        bad.append("build.sh is empty")
    else:
        s = open(build, encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'"([A-Za-z0-9_./-]+\.(?:tex|md))"', s):
            rel = m.group(1)
            if '$' in rel or '<' in rel:
                continue
            if not os.path.exists(os.path.join(root, rel)):
                bad.append(f"build.sh references a missing file: {rel}")

    # exactly one copy of the shared header
    copies = []
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f == 'unicode-fix.tex':
                copies.append(os.path.relpath(os.path.join(dp, f), root))
    if len(copies) == 0:
        bad.append("unicode-fix.tex missing entirely")
    elif len(copies) > 1:
        # Extra copies are inert -- build.sh reads only the shared one -- so
        # what matters is that they have not DRIFTED. A glyph mapping added to
        # one copy and not the others is the silent-drop failure this header
        # exists to prevent.
        import hashlib
        digests = {}
        for c in sorted(copies):
            h = hashlib.sha256(open(os.path.join(root, c), 'rb').read()).hexdigest()
            digests.setdefault(h, []).append(c)
        if len(digests) > 1:
            groups = " | ".join(", ".join(v) for v in digests.values())
            bad.append("unicode-fix.tex copies have DRIFTED apart: %s" % groups)
        else:
            print("  note: %d identical copies of unicode-fix.tex (%s); build.sh "
                  "reads only the shared one" % (len(copies), ", ".join(sorted(copies))))

    gate = os.path.join(root, 'tools', 'release_gate.py')
    if os.path.exists(gate):
        g = open(gate, encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'"(tools/[A-Za-z0-9_]+\.py)"', g):
            if not os.path.exists(os.path.join(root, m.group(1))):
                bad.append(f"release_gate.py names a missing check: {m.group(1)}")
        for m in re.finditer(r'"(papers/[A-Za-z0-9_/]+\.py)"', g):
            if not os.path.exists(os.path.join(root, m.group(1))):
                bad.append(f"release_gate.py names a missing check: {m.group(1)}")
    else:
        bad.append("tools/release_gate.py missing")

    for b in bad:
        print("  TOOLCHAIN " + b)
    if bad:
        print(f"\ntoolchain_check: FAILED ({len(bad)} problem(s))")
        return 1
    print(f"toolchain_check: OK (build entry present, unicode-fix.tex "
          f"consistent across {len(copies)} copy/copies, all named checks resolve)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
