#!/usr/bin/env python3
"""Scratch: render V3-11's preregistration from the template and edits311.EDITS. Never landed.
Usage: render311.py <D> <out>"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edits311 as ed  # noqa: E402

D, OUT = sys.argv[1], sys.argv[2]
texts = {p: subprocess.run(['git', 'show', '%s:%s' % (D, p)], cwd=ed.REPO, capture_output=True,
                           check=True).stdout.decode() for p in sorted({e[0] for e in ed.EDITS})}
rows, cur = [], dict(texts)
for n in (1, 2, 3):
    cur = ed.apply(cur, n)
    for p in ed.STAGES[n]:
        rows.append('| %d | `%s` | `%s` | `%s` |' % (n, p, ed.blob(texts[p])[:8], ed.blob(cur[p])))
secs = []
for i, (p, st, old, new) in enumerate(ed.EDITS, 1):
    secs.append('### Edit %d — stage %d, `%s`\n\nThe text at the parent:\n\n```text\n%s```\n\n'
                'Its replacement:\n\n```text\n%s```' % (i, st, p, old, new))
t = open(os.path.join(HERE, 'prereg-template.md'), encoding='utf-8').read()
t = t.replace('{{BLOBS}}', '\n'.join(rows)).replace('{{EDITS}}', '\n\n'.join(secs))
assert '{{' not in t
open(OUT, 'w', encoding='utf-8').write(t)
print('rendered %d edits, %d blob rows' % (len(secs), len(rows)))
