#!/usr/bin/env python3
"""Coordinator's independent recount of R6's verdict tables from the markdown of pt/R6/REASSESSMENT.md (not from
R6's r4_tables.out).  Writes r6_rows.tsv (table, id, class, verdict) next to this script for the T6 audit, which
compares T6's row-by-row citations against these rows.  Read-only on pt/R6/.
Run: python3 -I -B r6_rows.py from pt/audit/stage6-inputs/T-audit/.
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; R6-ROWS-FIXED iff all CONFIRMED.
 T1 three tables A1, A2, A3 found, each with exactly 199 item rows, ids identical across the three tables.
 T2 tallies: A1 and A2 SATISFIES 118 / FAILS 13 / NOT REACHED 68; A3 SATISFIES 118 / FAILS 12 / UNDECIDED 1 /
    NOT REACHED 68 (R6 §2).
 T3 the FAILS ids of A1 equal those of A2 and equal the 13 ids {I3.133, I3.135, I3.137, I3.142, I3.144, I3.150,
    I3.151, I3.152, I3.153, I3.155, I3.160, I3.161, I3.165}; A3's FAILS = these minus I3.161, which is UNDECIDED.
 T4 every FAILS row carries class dna, d4f or cand (hypothesis classes), never def, thm, gate, kthm, inh, b1.
 T5 every row of class hmg or nr is NOT REACHED in all three tables.
"""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, '..', '..', '..', 'R6', 'REASSESSMENT.md'), encoding='utf-8').read()
R = []
def rec(cid, ok, text_, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text_}" + (f" -- {detail}" if detail else ""))
# split into sections at '### Table'
parts = re.split(r'\n### Table ', text)
tables = {}
for p in parts[1:]:
    title = p.split('\n', 1)[0]
    key = title.split(' ')[0]            # A1, A2, A3, A3-seeds
    rows = []
    for ln in p.split('\n'):
        m = re.match(r'^\| (I[1-4]\.\d+) \| (.*?) \| (\w+) \| ([A-Z ]+?)(?: \[[^\]]*\]| \(vacuous\))? \| (.*) \|$', ln)
        if m:
            rows.append((m.group(1), m.group(3), m.group(4).strip()))
    tables[key] = rows
ids = {k: [r[0] for r in v] for k, v in tables.items()}
rec('T1', all(k in tables for k in ('A1', 'A2', 'A3')) and all(len(tables[k]) == 199 for k in ('A1', 'A2', 'A3')) and ids['A1'] == ids['A2'] == ids['A3'],
    'tables A1, A2, A3 present with 199 item rows each, identical ids', 'rows %s' % {k: len(v) for k, v in tables.items()})
from collections import Counter
tal = {k: Counter(r[2] for r in tables[k]) for k in ('A1', 'A2', 'A3')}
rec('T2', tal['A1'] == Counter({'SATISFIES': 118, 'FAILS': 13, 'NOT REACHED': 68}) and tal['A2'] == tal['A1'] and tal['A3'] == Counter({'SATISFIES': 118, 'FAILS': 12, 'UNDECIDED': 1, 'NOT REACHED': 68}),
    'tallies 118/13/68 (A1, A2) and 118/12/1/68 (A3)', str({k: dict(sorted(v.items())) for k, v in tal.items()}))
F = {k: sorted(r[0] for r in tables[k] if r[2] == 'FAILS') for k in ('A1', 'A2', 'A3')}
exp13 = sorted(['I3.133', 'I3.135', 'I3.137', 'I3.142', 'I3.144', 'I3.150', 'I3.151', 'I3.152', 'I3.153', 'I3.155', 'I3.160', 'I3.161', 'I3.165'])
und3 = sorted(r[0] for r in tables['A3'] if r[2] == 'UNDECIDED')
rec('T3', F['A1'] == exp13 and F['A2'] == exp13 and F['A3'] == sorted(set(exp13) - {'I3.161'}) and und3 == ['I3.161'],
    'FAILS ids as listed; A3 UNDECIDED = I3.161', 'A1 %s; A3 undecided %s' % (F['A1'], und3))
badcls = [(k, r) for k in ('A1', 'A2', 'A3') for r in tables[k] if r[2] == 'FAILS' and r[1] not in ('dna', 'd4f', 'cand')]
rec('T4', not badcls, 'every FAILS row is of a hypothesis class (dna, d4f, cand)', str(badcls[:5]))
badnr = [(k, r) for k in ('A1', 'A2', 'A3') for r in tables[k] if r[1] in ('hmg', 'nr') and r[2] != 'NOT REACHED']
rec('T5', not badnr, 'every hmg/nr row is NOT REACHED', str(badnr[:5]))
with open(os.path.join(here, 'r6_rows.tsv'), 'w', encoding='utf-8') as f:
    f.write('table\tid\tclass\tverdict\n')
    for k in ('A1', 'A2', 'A3'):
        for r in tables[k]: f.write('%s\t%s\t%s\t%s\n' % (k, r[0], r[1], r[2]))
print('classes per table:', {k: dict(sorted(Counter(r[1] for r in tables[k]).items())) for k in ('A1', 'A2', 'A3')})
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('R6-ROWS-FIXED' if all(R) else 'R6-ROWS-MISMATCH')
