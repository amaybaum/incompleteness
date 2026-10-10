"""Scratch: V3-13's changes to the V3 conformance corpus, generated from the corpus at D.

Usage: corpus_edits.py <corpus directory at D> <output directory>
Writes the added and replaced vectors (json, indent 1, trailing newline) into the output directory
and prints the vector ids to delete."""
import copy
import json
import os
import sys

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)


def load(name):
    return json.load(open(os.path.join(src, name + '.json'), encoding='utf-8'))


def dump(v):
    with open(os.path.join(out, v['id'] + '.json'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(v, indent=1) + '\n')


# G12, restated: a change to the legacy seal namespace is not a V3 predicate's concern
old = load('g12-reject-execution-changes-legacy-seal-namespace')
new = copy.deepcopy(old)
new['id'] = 'g12-admit-execution-changes-legacy-seal-namespace'
new['steps'][-1]['expect'] = {'verdict': 'HOLDS'}
dump(new)

# G13: a held round's records are those at its receipt commit
base = load('mc7-pass-sealing')
RD = 'verification/infrastructure/round-ex-2/'
land = {'commit': 'L', 'parents': ['D', 'Q'], 'from': 'Q'}


def g13(vid, change, verdict, family=None):
    v = copy.deepcopy(base)
    v['id'] = vid
    v['settlements'] = ['G13', 'S10']
    steps = v['steps'][:-1] + [land, {'check': 'receipts', 'args': ['L'],
                                       'expect': {'verdict': 'HOLDS'}}]
    steps.append(dict({'commit': 'X', 'parents': ['L'], 'from': 'L'}, **change))
    exp = {'verdict': verdict}
    if family:
        exp['family'] = family
    steps.append({'check': 'receipts', 'args': ['X'], 'expect': exp})
    v['steps'] = steps
    dump(v)


g13('g13-admit-records-unchanged-after-later-commit', {'set': {'README.md': 'r2\n'}}, 'HOLDS')
g13('g13-reject-record-file-modified-after-landing',
    {'set': {RD + 'preregistration.md': 'rewritten\n'}}, 'FAILS', 'g13')
g13('g13-reject-record-file-added-after-landing',
    {'set': {RD + 'result.md': 'a later note\n'}}, 'FAILS', 'g13')
g13('g13-reject-record-file-deleted-after-landing',
    {'del': [RD + 'preregistration.md']}, 'FAILS', 'g13')
g13('g13-reject-seal-record-changed-after-landing',
    {'set': {'verification/v3-seals/EX-2.json': 'another seal\n'}}, 'FAILS', 'g13')
print('delete g12-reject-execution-changes-legacy-seal-namespace')
