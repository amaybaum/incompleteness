"""Scratch: apply (old, new) edit lists to files; refuse unless each old text occurs exactly once."""
import sys
def apply(path, edits):
    t = open(path, encoding='utf-8').read()
    for i, e in enumerate(edits):
        old, new = e[0], e[1]
        n = t.count(old)
        if n != 1:
            raise SystemExit('%s: edit %d occurs %d times: %r' % (path, i, n, old[:80]))
        t = t.replace(old, new)
    open(path, 'w', encoding='utf-8', newline='\n').write(t)
