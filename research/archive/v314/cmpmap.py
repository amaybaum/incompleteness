#!/usr/bin/env python3
"""Scratch: compare a rehearsal's guard verdict map with D's, from verdict dumps of the probes logs.
Usage: cmpmap.py <verdicts-D.txt> <verdicts-X.txt>...
The guard's block runs from the R1 just before R7-FWD through R9, plus the checks printed after R9
that D's source defines (the emptied ones print there at D)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EMPTIED = {'R7-ABR', 'R7-ARCH', 'R7-BRIDGE', 'R7-CV1', 'R7-DILCH', 'R7-DILMAP', 'R7-GR1', 'R7-GR2',
           'R7-RBR', 'R7-SI1', 'R7-SI2', 'R7-SI3', 'R7-SRCA', 'R7-VIS'}
st = json.load(open(os.path.join(HERE, 'static-tags.json')))
DSET = {x for x in st['D'] if not x.startswith('B')}
ESET = set(st['E'])


def guard(path, tagset):
    rows = [tuple(l.split(' ', 1)) for l in open(path).read().split('\n') if l and not l.startswith('LAST')]
    last = [l for l in open(path).read().split('\n') if l.startswith('LAST')]
    tags = [k for _v, k in rows]
    fwd = tags.index('R7-FWD')
    start = max(i for i in range(fwd) if tags[i] == 'R1')
    end = start + tags[start:].index('R9')
    while end + 1 < len(rows) and rows[end + 1][1] in tagset:
        end += 1
    return rows[start:end + 1], (last[0] if last else 'LAST: missing')


d, dl = guard(sys.argv[1], DSET)
ok_all = True
print('D: %d tags, set == source: %s, PASS %d, FAIL %d, %s' % (
    len(d), {k for _v, k in d} == DSET and len(d) == len(DSET), sum(v == 'PASS' for v, _k in d),
    sum(v == 'FAIL' for v, _k in d), dl))
want = [x for x in d if x[1] not in EMPTIED]
for p in sys.argv[2:]:
    g, gl = guard(p, ESET)
    ok = g == want and len(g) == 91 and all(v == 'PASS' for v, _k in g) and gl == 'LAST: edge_rigidity_probe: ALL CHECKS PASS'
    ok_all &= ok
    print('%s: %d tags, PASS %d, FAIL %d, map == D less the 14 in order: %s, %s -> %s' % (
        os.path.basename(p), len(g), sum(v == 'PASS' for v, _k in g), sum(v == 'FAIL' for v, _k in g),
        g == want, gl, 'OK' if ok else 'MISMATCH'))
sys.exit(0 if ok_all else 1)
