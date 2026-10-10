#!/usr/bin/env python3
"""Scratch: render the V3-8 preregistration from prereg-template.md and edits38. Never landed.
Usage: render38.py <out>"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edits38 as e  # noqa

BLOBS = {'arch': 'db36dbd1ee4f779eff13525ffd3dc11d9041ab36', 'tool2': '0b3bd87fe52b269e9d7cf0fdb7f47653301ce8fd',
         'tool3': 'ccfbe813790e4855f408462449327f32e59d545b', 'readme': '55aba15ba3cf57a1fc35232534b6eed810abd920'}
LABEL = {'N1': 'the reconciliations in the objects table', 'N2': '`Q` in the objects table',
         'N3': 'the traceability row of `S10`', 'N4': '`S1`', 'N5': '`G8`', 'N6': '`G11`',
         'N7': '`S9`, the first parent', 'N8': '`S9`, the first reconciliation',
         'N9': '`K3`, consecutive reconciliations', 'N10': '`S10`', 'N11': '`K4`\'s first sentence',
         'N12': '`S11`', 'N13': '`S12`, the halted round', 'N14': '`S12`, reconciliation and receipt',
         'N15': '`S12`, the landed tree', 'N16': '`S12`, the execution commits', 'N17': '`G5`',
         'N18': 'the lifecycle states', 'N19': 'the lifecycle transitions', 'N20': 'the lifecycle\'s closing sentence',
         'N21': 'the worked example'}


def fence(t):
    return '```text\n' + t + '\n```'


spec = []
for nid, old, new in e.SPEC:
    spec.append('#### `%s` — %s\n\nThe located block:\n\n%s\n\nIts replacement:\n\n%s' % (nid, LABEL[nid], fence(old), fence(new)))


def sites(stage):
    return '\n\n'.join('#### Site `%s`\n\nThe site:\n\n%s\n\nThe drafting-time replacement (a prediction):\n\n%s'
                       % (sid, fence(old), fence(new)) for sid, st, old, new in e.SITES if st == stage)


t = open(os.path.join(HERE, 'prereg-template.md'), encoding='utf-8').read()
t = t.replace('{{SPEC}}', '\n\n'.join(spec)).replace('{{SITES:2}}', sites(2)).replace('{{SITES:3}}', sites(3))
t = t.replace('{{README_OLD}}', e.README_OLD).replace('{{README_NEW}}', e.README_NEW)
for k, v in BLOBS.items():
    t = t.replace('{{BLOB:%s}}' % k, v)
assert '{{' not in t
open(sys.argv[1], 'w', encoding='utf-8').write(t)
