#!/usr/bin/env python3
"""Coordinator's check of T6's row-by-row table (pt/T6/t4_rows.out, ROW lines) against the coordinator's own
recount of R6's Table A2 (r6_rows.tsv, written before T6 reported).  Reads both as data.
Run: python3 -I -B check_t6_rows.py from pt/audit/stage6-inputs/T-audit/.
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; CHECK-T6-ROWS-FIXED iff all CONFIRMED.
 R1 t4 carries exactly 199 ROW lines, ids = the 199 ids of r6_rows.tsv table A2, no duplicates.
 R2 the "R6 verdict" word T6 quotes per row equals my recount's A2 verdict for that id (SATISFIES / FAILS / NOT REACHED).
 R3 T6's own verdict per row: SATISFIES (incl. vacuous) or NOT REACHED on every row whose class is not dna/d4f/cand;
    FAILS exactly on the 13 hypothesis ids {I3.133, I3.135, I3.137, I3.142, I3.144, I3.150, I3.151, I3.152, I3.153,
    I3.155, I3.160, I3.161, I3.165}; T6's NOT REACHED set equals my recount's A2 NOT REACHED set.
 R4 tallies: T6 SATISFIES 115 + vacuous 3 = 118, NOT REACHED 68, FAILS 13 (amendment 2 A2.4: every item reaching the
    pair cone SATISFIES or NOT REACHED on every non-hypothesis row).
"""
import os, re
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
mine = {}
for ln in open(os.path.join(here, 'r6_rows.tsv'), encoding='utf-8').read().splitlines()[1:]:
    tb, i, cls, v = ln.split('\t')
    if tb == 'A2': mine[i] = (cls, v)
rows = {}
for ln in open(os.path.join(here, '..', '..', '..', 'T6', 't4_rows.out'), encoding='utf-8').read().splitlines():
    if not ln.startswith('ROW ') or ln.startswith('ROW id |'): continue
    f = [x.strip() for x in ln[4:].split(' | ')]
    rid, r6cls, r6v, t6v = f[0], f[1], f[2], f[3]
    if rid in rows: print('DUPLICATE', rid)
    rows[rid] = (r6cls, r6v, t6v)
def word(v):
    v = v.upper()
    for w in ('NOT REACHED', 'SATISFIES', 'FAILS', 'UNDECIDED'):
        if v.startswith(w): return w
    return v
rec('R1', len(rows) == 199 and set(rows) == set(mine), 't4 carries 199 ROW lines with exactly the A2 ids', 'rows %d, extra %s, missing %s' % (len(rows), sorted(set(rows) - set(mine))[:5], sorted(set(mine) - set(rows))[:5]))
bad2 = [(i, rows[i][1], mine[i][1]) for i in rows if i in mine and word(rows[i][1]) != mine[i][1]]
rec('R2', not bad2, "T6's quoted R6 verdict equals my recount's A2 verdict on every row", str(bad2[:6]))
hyp = {'I3.133', 'I3.135', 'I3.137', 'I3.142', 'I3.144', 'I3.150', 'I3.151', 'I3.152', 'I3.153', 'I3.155', 'I3.160', 'I3.161', 'I3.165'}
t6 = {i: word(rows[i][2]) for i in rows}
bad3 = [i for i in rows if mine.get(i, ('', ''))[0] not in ('dna', 'd4f', 'cand') and t6[i] not in ('SATISFIES', 'NOT REACHED')]
fails = {i for i in rows if t6[i] == 'FAILS'}
nr_t6 = {i for i in rows if t6[i] == 'NOT REACHED'}; nr_mine = {i for i in mine if mine[i][1] == 'NOT REACHED'}
rec('R3', not bad3 and fails == hyp and nr_t6 == nr_mine, "T6's verdicts: non-hypothesis rows SATISFIES/NOT REACHED; FAILS = the 13 hypothesis ids; NOT REACHED set = mine", 'bad %s; fails-diff %s; nr-diff %s' % (bad3[:6], sorted(fails ^ hyp), sorted(nr_t6 ^ nr_mine)[:6]))
tal = Counter(t6.values()); vac = sum(1 for i in rows if 'VACUOUS' in rows[i][2].upper())
rec('R4', tal['SATISFIES'] == 118 and tal['NOT REACHED'] == 68 and tal['FAILS'] == 13 and vac == 3, 'tallies SATISFIES 118 (3 vacuous), NOT REACHED 68, FAILS 13', '%s vacuous %d' % (dict(sorted(tal.items())), vac))
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('CHECK-T6-ROWS-FIXED' if all(R) else 'CHECK-T6-ROWS-MISMATCH')
