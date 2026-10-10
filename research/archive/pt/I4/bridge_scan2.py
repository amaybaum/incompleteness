#!/usr/bin/env python3
"""I4 bridge scan 2 -- widened level-H token set: the passive hidden-dynamics modules in the import
closure of the pair-level modules.  (bridge_scan.py took H to be the substratum objects
substratumTheory/substratumClass only; PassiveQuotient.lean -- in I4's scope -- is a hidden deterministic
history object and lies in CompositeDimension.lean's import closure, so the H-P question is re-asked.)

Run from pt/I4/ as:  python3 -I -B bridge_scan2.py > bridge_scan2.out 2> bridge_scan2.err

DECISION RULE (fixed before the first run):
 E1 HMODS = PassiveQuotient, ControlledQuotient, ObservabilityQuotient (the three passive hidden-dynamics
    modules on the chain PassiveQuotient <- ControlledQuotient <- ... <- CompositeDimension; the chain
    is printed).  HNAMES = every name declared at column 0 in HMODS (def/abbrev/structure/class/
    inductive/theorem/lemma/instance), last dotted component, length >= 4.
 E2 PMODS = every OIBridge module that is, or transitively imports, CompositeDimension or K2Guard.
 E3 For each module in PMODS, every comment-stripped line containing a whole-word HNAME is listed.
    Lines in PMODS that use an HNAME are candidate H-P links; the verdict reports their count.
 E4 Controls: C1 'quotient_itinerarySeparating' is in HNAMES; C2 the scan finds the whole-word HNAME in
    a synthetic line 'theorem t := quotPerm x' and not in 'theorem t := quotPermX x'; C3 CompositeDimension
    is in PMODS; C4 PassiveQuotient is in the transitive closure of CompositeDimension.
 E5 Deterministic output.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.normpath(os.path.join(HERE, '..', 'base', 'verification', 'lean-mathlib', 'OIBridge'))
HMODS = ['PassiveQuotient', 'ControlledQuotient', 'ObservabilityQuotient']
DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe|nonrec)\s+)*'
                  r'(def|abbrev|structure|class|inductive|theorem|lemma|instance)\s+([^\s:({\[⦃]+)')


def strip(lines):
    out, depth = [], 0
    for line in lines:
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
    mods = sorted(f[:-5] for f in os.listdir(DIR) if f.endswith('.lean'))
    clean = {}
    for m in mods:
        with open(os.path.join(DIR, m + '.lean'), encoding='utf-8') as fh:
            clean[m] = strip(fh.read().split('\n'))
    imp = {m: sorted({mm.group(1) for s in clean[m] for mm in [re.match(r'^\s*import\s+OIBridge\.(\S+)\s*$', s)] if mm})
           for m in mods}
    clo = {}

    def close(m):
        if m in clo:
            return clo[m]
        clo[m] = set()
        acc = set()
        for d in imp.get(m, []):
            acc.add(d)
            acc |= close(d)
        clo[m] = acc
        return acc
    for m in mods:
        close(m)
    hnames = set()
    for h in HMODS:
        for s in clean[h]:
            mm = DECL.match(s)
            if mm:
                nm = mm.group(2).split('.')[-1]
                if len(nm) >= 4:
                    hnames.add(nm)
    pmods = sorted(m for m in mods if m in ('CompositeDimension', 'K2Guard')
                   or 'CompositeDimension' in clo[m] or 'K2Guard' in clo[m])
    pat = re.compile(r'(?<![\w.])(' + '|'.join(sorted(map(re.escape, hnames), key=lambda x: (-len(x), x))) + r')(?![\w])')
    c1 = 'quotient_itinerarySeparating' in hnames
    c2 = bool(pat.search('theorem t := quotPerm x')) and not pat.search('theorem t := quotPermX x')
    c3 = 'CompositeDimension' in pmods
    c4 = 'PassiveQuotient' in clo['CompositeDimension']
    print('## CONTROLS')
    for lab, ok in [('C1 quotient_itinerarySeparating in HNAMES', c1), ('C2 whole-word matcher', c2),
                    ('C3 CompositeDimension in PMODS', c3), ('C4 PassiveQuotient in closure(CompositeDimension)', c4)]:
        print('%s: %s' % ('PASS' if ok else 'FAIL', lab))
    print()
    print('HMODS: %s ; HNAMES: %d' % (' '.join(HMODS), len(hnames)))
    print('PMODS (%d): %s' % (len(pmods), ' '.join(pmods)))
    # chain from CompositeDimension down to PassiveQuotient (first-found path)
    path = None
    stack = [('CompositeDimension', ['CompositeDimension'])]
    seen = set()
    while stack:
        m, p = stack.pop()
        if m == 'PassiveQuotient':
            path = p
            break
        if m in seen:
            continue
        seen.add(m)
        for d in sorted(imp.get(m, []), reverse=True):
            stack.append((d, p + [d]))
    print('import chain CompositeDimension -> PassiveQuotient: %s' % (' -> '.join(path) if path else '(none)'))
    print()
    print('## HNAME USES IN PMODS (E3)')
    n = 0
    for m in pmods:
        for i, s in enumerate(clean[m]):
            hits = sorted(set(x.group(1) for x in pat.finditer(s)))
            if hits:
                n += 1
                print('%s.lean:%d | %s | %s' % (m, i + 1, ','.join(hits), s.strip()[:150]))
    print()
    print('candidate H-P link lines: %d' % n)
    ok = c1 and c2 and c3 and c4
    print('VERDICT: %s' % ('CONTROL FAILURE (scan void)' if not ok else
                           ('H NAMES USED IN PAIR-LEVEL MODULES (inspect)' if n else
                            'NO PAIR-LEVEL MODULE USES A NAME DECLARED IN THE PASSIVE HIDDEN-DYNAMICS MODULES')))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
