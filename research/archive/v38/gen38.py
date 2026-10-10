#!/usr/bin/env python3
"""Scratch: generate the V3-8 corpus changes from the corpus at a ref. Never landed.

Usage: gen38.py <ref> <outdir>
Writes into <outdir>: the converted mc2-pass-base-drift.json and the three added reach-*.json.
The retired vector is mc2-counter-host-merge.json. Vectors are serialized as the corpus is
(json.dump, indent 1, ensure_ascii False, trailing newline), which the script checks first."""
import json
import os
import subprocess
import sys

REPO = '/home/user/incompleteness'
C = 'verification/infrastructure/v3/conformance/'
ref, out = sys.argv[1:3]


def show(path):
    return subprocess.run(['git', 'show', '%s:%s' % (ref, path)], cwd=REPO, capture_output=True,
                          check=True).stdout.decode('utf-8')


def dump(v):
    return json.dumps(v, indent=1, ensure_ascii=False) + '\n'


host = show(C + 'mc2-counter-host-merge.json')
drift = show(C + 'mc2-pass-base-drift.json')
assert dump(json.loads(host)) == host and dump(json.loads(drift)) == drift, 'corpus format'
hv, dv = json.loads(host), json.loads(drift)
labels = [s.get('commit') for s in hv['steps']]
assert labels[:8] == ['D', 'F', 'E1', 'E', 'R1', 'Q', 'M2', 'H'], labels
upto_q = hv['steps'][:6]
m2, h = hv['steps'][6], hv['steps'][7]

vectors = {}
# converted: the publication step becomes a reachability diagnostic, the superseded receipt commit
# Q being reachable from the final one
assert dv['steps'][-1] == {'check': 'publication', 'args': ['Q2', 'Q2'], 'expect': {'verdict': 'HOLDS'}}
dv['steps'][-1] = {'check': 'reachable', 'args': ['Q2', 'Q'], 'expect': {'reachable': 'true'}}
vectors['mc2-pass-base-drift'] = dv
vectors['reach-true-host-merge-contains-q'] = {
    'id': 'reach-true-host-merge-contains-q', 'settlements': ['S10'], 'kind': 'repo',
    'steps': upto_q + [m2, h, {'check': 'reachable', 'args': ['H', 'Q'], 'expect': {'reachable': 'true'}}]}
vectors['reach-false-moved-base-lacks-q'] = {
    'id': 'reach-false-moved-base-lacks-q', 'settlements': ['S10'], 'kind': 'repo',
    'steps': upto_q + [m2,
                       {'check': 'verify-round', 'args': ['Q'], 'expect': {'verdict': 'HOLDS'}},
                       {'check': 'reachable', 'args': ['M2', 'Q'], 'expect': {'reachable': 'false'}}]}
vectors['reach-undecidable-shallow-history'] = {
    'id': 'reach-undecidable-shallow-history', 'settlements': ['S10'], 'kind': 'repo',
    'steps': upto_q + [{'write': '.git/shallow', 'text': 'f' * 40 + '\n'},
                       {'check': 'reachable', 'args': ['Q', 'Q'],
                        'expect': {'reachable': 'undecidable', 'code': 'undecidable:shallow-repository'}}]}
os.makedirs(out, exist_ok=True)
for vid, v in vectors.items():
    assert v['id'] == vid
    open(os.path.join(out, vid + '.json'), 'w', encoding='utf-8').write(dump(v))
print('wrote', len(vectors), 'vectors')
