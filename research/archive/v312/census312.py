#!/usr/bin/env python3
"""Scratch: assemble V3-12's census, one row per surface, from the guard extraction and the three
surveys. Never landed; its output, census.json, is the round's record of the measurement.

Usage: census312.py <D> <out census.json>"""
import collections
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
D, OUT = sys.argv[1], sys.argv[2]
G = 'verification/lean/edge_rigidity_probe.py'


def blob(rev, path):
    return subprocess.run(['git', 'rev-parse', '%s:%s' % (rev, path)], cwd=REPO, capture_output=True,
                          text=True).stdout.strip()


guard = json.load(open(os.path.join(HERE, 'guard.json')))
classes = json.load(open(os.path.join(HERE, 'guard_classes.json')))
OVERRIDES = {
    ('R7-GR1', 32031): 'infrastructure round: the guard-predicate text tests, not a record pin',
    ('R7-GR1', 32032): 'infrastructure round: the guard-predicate text tests, not a record pin',
    ('R7-GR1', 32034): 'infrastructure round: the guard-predicate text tests, not a record pin',
    ('R7-GR1', 32043): 'infrastructure round: the guard-predicate text tests, not a record pin',
    ('R7-GR1', 32046): 'infrastructure round: the guard-predicate text tests, not a record pin',
    ('R7-GR1', 32556): 'infrastructure round: the guard placement budget, not a record pin',
    ('R7-CV1', 35007): 'infrastructure round: couples the note to the V2 gate step being wired',
}
CLASSNAME = {'RS': 'retain-substantive', 'RH': 'retain-historical', 'RT': 'retire', 'STRUCT': 'structural'}
text_of = {(c['check'], p['line']): p['text'] for c in guard for p in c['predicates']}
preds = []
for r in classes:
    k = (r['check'], r['line'])
    cls, why = r['class'], r['why']
    if k in OVERRIDES:
        cls, why = 'RT', OVERRIDES[k]
    preds.append({'check': r['check'], 'line': r['line'], 'class': CLASSNAME[cls], 'reason': why,
                  'history_reads': r['hist'],
                  'text_sha256': hashlib.sha256(text_of[k].encode()).hexdigest()[:16],
                  'text': r['text']})
by = collections.defaultdict(collections.Counter)
for p in preds:
    by[p['check']][p['class']] += 1
checks = []
for c in guard:
    v = by[c['check']]
    n = sum(v.values()) - v['structural']
    if n == 0:
        disp = 'retain-substantive'   # checks whose verdict is a single computed accumulator
    elif v['retire'] == n:
        disp = 'retire'
    elif v['retire'] == 0:
        disp = 'retain-historical' if v['retain-historical'] and not v['retain-substantive'] else 'retain-substantive'
    else:
        disp = 'split'
    checks.append({'check': c['check'], 'line_at_D': c['line'], 'predicates': n,
                   'retain_substantive': v['retain-substantive'], 'retain_historical': v['retain-historical'],
                   'retire': v['retire'], 'disposition': disp})
v2 = json.load(open(os.path.join(HERE, 'agents', 'v2_census.json')))
infra = json.load(open(os.path.join(HERE, 'agents', 'infra_census.json')))
docs = json.load(open(os.path.join(HERE, 'agents', 'docs_census.json')))
out = {
    'schema': 'v3-12-retirement-census', 'version': 1, 'd': D,
    'blobs_at_d': {p: blob(D, p) for p in (G, 'tools/certificate_verifier.py', 'tools/release_gate.py',
                                           '.github/workflows/verify.yml', 'tools/control_plane_lint.py',
                                           'tools/control_plane_base_check.py', 'AGENTS.md',
                                           'verification/README.md', 'tools/v3_verifier.py')},
    'guard': {'checks': checks, 'predicates': preds,
              'totals': dict(collections.Counter(p['class'] for p in preds))},
    'v2': v2, 'infrastructure': infra, 'documentation': docs,
}
json.dump(out, open(OUT, 'w'), indent=1, ensure_ascii=False)
t = out['guard']['totals']
print('guard: %d checks, %d predicates: %s' % (len(checks), len(preds), t))
print('check dispositions:', dict(collections.Counter(c['disposition'] for c in checks)))
