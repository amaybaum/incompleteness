#!/usr/bin/env python3
"""I4 census mapping -- maps every census (a) entry of census_kernel.out to an inventory record of
records.txt, or to the out-of-scope list below with an admissible reason.

Run from pt/I4/ as:  python3 -I -B census_map.py > census_map.out 2> census_map.err

DECISION RULE (fixed before the first run):
 M1 Census entries are the lines of census_kernel.out's section '## CENSUS (a) ENTRIES' (module.lean:line).
 M2 An entry is MAPPED iff some record of records.txt has src 'lean:<module>.lean:<line>' with the same
    module and line; it is OUT-OF-SCOPE iff listed in OUT below with a reason; otherwise UNMAPPED.
 M3 Admissible reasons only (PROTOCOL-STAGE6.md coverage control (a)): 'a definition with no hypothesis
    role', 'a theorem-internal auxiliary', 'belongs to thread Ik'. A listed reason outside these fails.
 M4 Controls: C1 the census section is non-empty and its count equals the TOTAL census count printed by
    census_kernel.out; C2 no entry is both mapped and out-of-scope; C3 a synthetic entry
    'ReferenceExtension.lean:1' is UNMAPPED (countercontrol).
 M5 VERDICT 'ALL ENTRIES ACCOUNTED' iff every entry is mapped or out-of-scope and C1-C3 pass.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {
    'MinimalRepertoire.lean:208': ('IsRealAntisym', 'a theorem-internal auxiliary (closure class of the colour-phase Lie algebra `colourAlg`, MinimalRepertoire.lean:250, used for the bipartite obstruction)'),
    'MinimalRepertoire.lean:311': ('ColourCompatible', 'a theorem-internal auxiliary (hypothesis of not_hControl_of_colourCompatible, MinimalRepertoire.lean:353, an obstruction lemma)'),
    'StructuralClosure.lean:98': ('IsSubmonomial', 'a definition with no hypothesis role (the elementwise form of IsMonomial; monomial_iff_submonomial, StructuralClosure.lean:169)'),
    'QuasilocalAlgebra.lean:104': ('AgreeOffG', 'a theorem-internal auxiliary (agreement off a finite set, used by agreeOffG_map, QuasilocalAlgebra.lean:942)'),
    'PassiveObservation.lean:288': ('IsDiagonal', 'a theorem-internal auxiliary (diagonal matrices, used by the pinching lemmas, PassiveObservation.lean:299-:342)'),
    'PassiveIndependence.lean:98': ('SuppAnc', 'a theorem-internal auxiliary (ancilla support predicate used by KeepsLabels and the label theory, PassiveIndependence.lean:103-:150)'),
}
ADMISSIBLE = ('a definition with no hypothesis role', 'a theorem-internal auxiliary', 'belongs to thread I')


def main():
    with open(os.path.join(HERE, 'census_kernel.out'), encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    entries, total, inside = [], None, False
    for ln in lines:
        if ln.startswith('## CENSUS (a) ENTRIES'):
            inside = True
            continue
        if inside and ln.startswith('## '):
            inside = False
        if inside and ln.strip():
            f = [x.strip() for x in ln.split('|')]
            entries.append((f[0], f[2], f[3]))
        if ln.startswith('TOTAL |'):
            total = int(ln.split('|')[1])
    srcs = {}
    with open(os.path.join(HERE, 'records.txt'), encoding='utf-8') as fh:
        for raw in fh.read().split('\n'):
            if not raw.strip() or raw.startswith('#'):
                continue
            f = [x.strip() for x in raw.split(' ¦ ')]
            if f[1].startswith('lean:'):
                key = f[1][5:]
                srcs.setdefault(key, []).append(f[0])
    mapped, oos, unmapped, both = [], [], [], []
    bad_reason = [k for k, (_, r) in OUT.items() if not r.startswith(ADMISSIBLE)]
    for (loc, kw, name) in entries:
        m = loc in srcs
        o = loc in OUT
        if m and o:
            both.append(loc)
        if m:
            mapped.append((loc, kw, name, ','.join(srcs[loc])))
        elif o:
            oos.append((loc, kw, name, OUT[loc][1]))
        else:
            unmapped.append((loc, kw, name))
    c1 = bool(entries) and total == len(entries)
    c2 = not both
    c3 = 'ReferenceExtension.lean:1' not in srcs and 'ReferenceExtension.lean:1' not in OUT
    print('## CENSUS (a) MAPPING (%d entries)' % len(entries))
    print('mapped: %d ; out-of-scope: %d ; unmapped: %d' % (len(mapped), len(oos), len(unmapped)))
    print()
    print('### mapped (entry | keyword | name | record ids)')
    for x in mapped:
        print('%s | %s | %s | %s' % x)
    print()
    print('### out of scope (entry | keyword | name | reason)')
    for x in oos:
        print('%s | %s | %s | %s' % x)
    print()
    print('### unmapped')
    for x in unmapped:
        print('%s | %s | %s' % x)
    print()
    for lab, ok in [('C1 census section count equals TOTAL (%s)' % total, c1), ('C2 no entry both mapped and out-of-scope', c2),
                    ('C3 synthetic entry is unmapped', c3), ('M3 reasons admissible', not bad_reason)]:
        print('%s: %s' % ('PASS' if ok else 'FAIL', lab))
    ok = c1 and c2 and c3 and not bad_reason and not unmapped
    print('VERDICT: %s' % ('ALL ENTRIES ACCOUNTED' if ok else ('CONTROL FAILURE' if not (c1 and c2 and c3 and not bad_reason) else 'UNMAPPED ENTRIES REMAIN')))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
