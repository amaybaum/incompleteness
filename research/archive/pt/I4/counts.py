#!/usr/bin/env python3
"""I4 counts for RESULT.md section 0 -- counts by kind, status class and level; the bearing exceptions; the
bridge field classes; the do-not-assume list.

Run from pt/I4/ as:  python3 -I -B counts.py > counts.out 2> counts.err

DECISION RULE (fixed before the first run):
 K1 Input records.txt (same parsing as render_inventory.py: 12 fields separated by ' ¦ ').
 K2 kind class = the kind field up to the first ' (' or ' --' ; status class = 'proved [K]' if the field is 'K'
    or starts with 'proved [K]'; 'definition (no status)' if it starts with '-'; otherwise the first word of
    the field among assumed / open / conditional-on / refuted (first match, in that order, at the start).
 K3 bearing exception = bearing field not equal to 'none'.  bridge class = the code (NB-M, NB-H, NB-HP, NB-G)
    when the field starts with one, else 'other'.  do-not-assume = flag field starting with 'DNA'.
 K4 Controls: C1 every record has a status class among the five; C2 the total of each tally equals the number
    of records; C3 every bridge field is non-empty.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    recs = []
    with open(os.path.join(HERE, 'records.txt'), encoding='utf-8') as fh:
        for raw in fh.read().split('\n'):
            if not raw.strip() or raw.startswith('#'):
                continue
            recs.append([x.strip() for x in raw.split(' ¦ ')])
    kinds, stats, levels, bridges = {}, {}, {}, {}
    bad, exc, dna = [], [], []
    for f in recs:
        rid, src, name, kind, status, level, dep, yl, bridge, bearing, flag, note = f
        k = kind.split(' (')[0].split(' --')[0].strip()
        kinds[k] = kinds.get(k, 0) + 1
        if status == 'K' or status.startswith('proved [K]'):
            sc = 'proved [K]'
        elif status.startswith('-'):
            sc = 'definition (no status)'
        else:
            sc = None
            for w in ('assumed', 'open', 'conditional-on', 'refuted'):
                if status.startswith(w):
                    sc = w
                    break
        if sc is None:
            bad.append(rid)
            sc = 'UNCLASSIFIED'
        stats[sc] = stats.get(sc, 0) + 1
        levels[level] = levels.get(level, 0) + 1
        b = bridge.split(' ;; ')[0].strip()
        bc = b if b in ('NB-M', 'NB-H', 'NB-HP', 'NB-G') else 'other'
        bridges[bc] = bridges.get(bc, 0) + 1
        if bearing != 'none':
            exc.append((rid, name, level, bearing))
        if flag.startswith('DNA'):
            dna.append((rid, name, level))
        if not bridge:
            bad.append(rid + ':bridge')
    n = len(recs)
    print('records: %d' % n)
    for title, tally in (('kind', kinds), ('status class', stats), ('level', levels), ('bridge class', bridges)):
        print()
        print('## by %s (total %d)' % (title, sum(tally.values())))
        for key in sorted(tally):
            print('%s: %d' % (key, tally[key]))
    print()
    print('## bearing other than none at L: %d' % len(exc))
    for x in exc:
        print('%s | %s | level %s | %s' % x)
    print()
    print('## do-not-assume flags: %d' % len(dna))
    for x in dna:
        print('%s | %s | level %s' % x)
    c1 = not [b for b in bad if ':' not in b]
    c2 = all(sum(t.values()) == n for t in (kinds, stats, levels, bridges))
    c3 = not [b for b in bad if b.endswith(':bridge')]
    print()
    for lab, ok in (('C1 every status classified', c1), ('C2 tallies sum to the record count', c2), ('C3 bridge fields non-empty', c3)):
        print('%s: %s' % ('PASS' if ok else 'FAIL', lab))
    print('VERDICT: %s' % ('COUNTS VALID' if (c1 and c2 and c3) else 'CONTROL FAILURE'))
    return 0 if (c1 and c2 and c3) else 1


if __name__ == '__main__':
    sys.exit(main())
