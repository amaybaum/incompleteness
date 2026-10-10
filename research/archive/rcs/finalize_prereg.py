#!/usr/bin/env python3
"""Fill the predicted-tree section of the preregistration (template) and write the final revision.
usage: finalize_prereg.py <section.md>   -- section text replaces @@PREDICTED@@"""
import sys
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/rcs'
sec = open(sys.argv[1], encoding='utf-8').read().rstrip('\n')
t = open(S + '/preregistration.md', encoding='utf-8').read()
rep = {'@@CONTROLS@@': '8cafc140b519495d1687a5507846d320c3c3295f', '@@CONTROLS_LINES@@': '2400', '@@SELFTEST@@': '93',
       '@@B_PAR@@': '40cdd044094a5886d916c2c1a8847ff2066433d8', '@@B_BLK@@': '4db61452136745e536803f1d6f5789772db3fb50',
       '@@B_SQZ@@': 'ed994d18e322ef61015cba0e7dc3715316b009d6', '@@B_C5@@': '4ba97ee39c522faf6cc39ccca9f1c09dbcf0b9a6',
       '@@PREDICTED@@': sec}
for k, v in rep.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + '/preregistration.final.md', 'w', encoding='utf-8').write(t)
draft = open(S + '/preregistration.draft.md', encoding='utf-8').read()
a, b = draft.split('\n### The predicted execution tree\n'), t.split('\n### The predicted execution tree\n')
assert a[0] == b[0], 'the final revision differs from the drafting revision before the section'
assert a[1].split('\n## Stages\n')[1] == b[1].split('\n## Stages\n')[1], 'differs after the section'
long = [(i + 1, len(l)) for i, l in enumerate(t.split('\n')) if len(l) > 120 and not l.startswith('|') and i > 0]
print('final written; differs from the draft only in the predicted-tree section; long lines:', long)
