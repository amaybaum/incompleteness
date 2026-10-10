#!/usr/bin/env python3
"""I4 dictionary scan -- does a kernel module at L define a dictionary between the pair carrier W 3 and
complex matrices (the Pauli map `pauliW`, the cone `Q3`), and where does the dictionary the PT stages
use live?

Run from pt/I4/ as:  python3 -I -B dictionary_scan.py > dictionary_scan.out 2> dictionary_scan.err

DECISION RULE (fixed before the first run):
 P1 Trees: (L) every .lean file under ../base/verification (both Lean projects); (D) every .lean file under
    ../inputs/fourcopy (design modules exported from ff9c3a35, not certified).
 P2 A DEFINITION of the dictionary is a comment-stripped line matching
    '^(noncomputable )?(def|abbrev) (pauliW|pauli1|Q3|twin)\\b'.  A USE is any comment-stripped
    whole-word occurrence of pauliW or Q3.
 P3 Report definitions and use counts per tree; for (D), report whether the defining file contains
    'sorry' (comment-stripped).
 P4 Controls: C1 the (D) tree must contain the definition 'def pauliW' (known from FourCopyPackage.lean:176,
    read before this script was written); C2 the matcher must reject 'def pauliWX' and accept
    'def pauliW (ω : W 3)'.  Any control failure voids the scan.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TREES = {'L': os.path.normpath(os.path.join(HERE, '..', 'base', 'verification')),
         'D': os.path.normpath(os.path.join(HERE, '..', 'inputs', 'fourcopy'))}
DEF = re.compile(r'^(?:noncomputable )?(?:def|abbrev) (pauliW|pauli1|Q3|twin)(?![\w])')
USE = re.compile(r'(?<![\w.])(pauliW|Q3)(?![\w])')


def strip(text):
    out, depth = [], 0
    for line in text.split('\n'):
        buf, i = [], 0
        while i < len(line):
            two = line[i:i + 2]
            if depth > 0:
                if two == '-/':
                    depth -= 1; i += 2; continue
                if two == '/-':
                    depth += 1; i += 2; continue
                i += 1; continue
            if two == '--':
                break
            if two == '/-':
                depth += 1; i += 2; continue
            buf.append(line[i]); i += 1
        out.append(''.join(buf))
    return out


def main():
    res = {}
    for t, root in TREES.items():
        defs, uses, files = [], 0, 0
        for dp, dn, fn in sorted(os.walk(root)):
            dn.sort()
            for f in sorted(fn):
                if not f.endswith('.lean'):
                    continue
                files += 1
                path = os.path.join(dp, f)
                with open(path, encoding='utf-8') as fh:
                    cl = strip(fh.read())
                rel = os.path.relpath(path, root)
                has_sorry = any(re.search(r'(?<![\w])sorry(?![\w])', s) for s in cl)
                for i, s in enumerate(cl):
                    m = DEF.match(s)
                    if m:
                        defs.append((rel, i + 1, m.group(1), has_sorry))
                    uses += len(USE.findall(s))
        res[t] = (files, defs, uses)
    c1 = any(d[2] == 'pauliW' for d in res['D'][1])
    c2 = (not DEF.match('def pauliWX (x : W 3)')) and bool(DEF.match('def pauliW (ω : W 3)'))
    for t in ('L', 'D'):
        files, defs, uses = res[t]
        print('## tree %s (%s): .lean files %d ; dictionary definitions %d ; whole-word uses of pauliW/Q3 %d'
              % (t, 'certified base at L' if t == 'L' else 'design modules ff9c3a35, not certified', files, len(defs), uses))
        for (rel, ln, nm, hs) in defs:
            print('  DEF %s:%d %s%s' % (rel, ln, nm, '  (file contains sorry)' if hs else ''))
    print()
    print('PASS: C1 design tree defines pauliW' if c1 else 'FAIL: C1 design tree defines pauliW')
    print('PASS: C2 matcher' if c2 else 'FAIL: C2 matcher')
    if not (c1 and c2):
        print('VERDICT: CONTROL FAILURE')
        return 1
    print('VERDICT: %s' % ('NO DICTIONARY DEFINITION AT L' if not res['L'][1] else 'DICTIONARY DEFINED AT L (inspect)'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
