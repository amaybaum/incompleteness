"""Extract the compact diagnostics of a Mathlib bridge job log saved by the MCP tool."""
import sys, re
t = open(sys.argv[1]).read()
t = t.replace('\\n', '\n') if t.count('\n') < 5 else t
lines = t.split('\n')
def sect(tag, n):
    idx = [i for i, l in enumerate(lines) if tag in l and 'echo' not in l]
    if not idx: return
    i = idx[0]
    for l in lines[i:i + n]:
        l = re.sub(r'^\S+ ', '', l)
        if l.startswith('===') and tag not in l: break
        print(l[:400])
print('--- ERRORS ---'); sect('=== ERRORS ===', 60)
print('--- CONTEXTS ---'); sect('=== ERROR CONTEXTS ===', int(sys.argv[2]) if len(sys.argv) > 2 else 400)
print('--- SORRY ---'); sect('=== SORRY ===', 30)
print('--- NONSTANDARD ---'); sect('=== NONSTANDARD AXIOMS ===', 30)
ps = [l for l in lines if 'ProductStratum.lean' in l and ('error' in l or 'warning' in l) and 'unused' not in l and 'not explicitly referenced' not in l]
print('--- PS error/warning lines:', len(ps))
for l in ps[:40]: print('  ', re.sub(r'^\S+ ', '', l)[:300])
