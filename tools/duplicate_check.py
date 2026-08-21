#!/usr/bin/env python3
"""duplicate_check.py - is a paragraph repeated inside a single document?

A blanket scope note was pasted at the head of nearly every file, which put 16
identical copies inside the assembled book. No other check sees this:
mirror_check verifies chapter text is PRESENT in FULL, not that it appears
once; staleness and claims are per-claim, not per-repetition.

Chapter-to-FULL repetition is by design and is not counted. What is counted is
repetition WITHIN one file.

Usage:  python3 tools/duplicate_check.py [--root DIR] [--min-chars N]
Exit 1 if any file repeats a substantial paragraph.
"""
import os, sys, collections

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    minc = 200
    if '--min-chars' in sys.argv:
        minc = int(sys.argv[sys.argv.index('--min-chars') + 1])
    bad = 0
    # Headings first. A section duplicated with SMALL edits shares few whole
    # paragraphs and can slip past paragraph matching entirely, while still
    # being a duplicated section. Report the heading and BOTH offsets so the
    # two copies can be diffed before anything is deleted -- never delete on
    # heading match alone.
    import re as _re
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith('.md'):
                continue
            p2 = os.path.join(dp, f)
            t2 = open(p2, encoding='utf-8', errors='replace').read()
            pos = {}
            for m in _re.finditer(r'^#{2,4} .+$', t2, _re.M):
                pos.setdefault(m.group(0).strip(), []).append(m.start())
            for h, offs in pos.items():
                if len(offs) > 1:
                    lines = [t2.count('\n', 0, o) + 1 for o in offs]
                    print(f"  DUP-HEADING {p2}  x{len(offs)} at lines "
                          f"{', '.join(map(str, lines))}")
                    print(f"              {h[:80]}")
                    print(f"              diff the copies before removing either")
                    bad += 1

    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            text = open(p, encoding='utf-8', errors='replace').read()
            c = collections.Counter(
                para.strip() for para in text.split('\n\n')
                if len(para.strip()) >= minc)
            for para, n in c.items():
                if n > 1:
                    print(f"  DUPLICATE {p}  x{n}")
                    print(f"            {para[:90]}...")
                    bad += 1
    if bad:
        print(f"\nduplicate_check: FAILED ({bad} paragraph(s) repeated within "
              f"a single file)")
        return 1
    print("duplicate_check: OK (no paragraph repeated within a file)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
