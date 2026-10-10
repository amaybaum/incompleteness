"""Scratch: every history-executing site left in a guard file. Never landed."""
import ast, collections, sys
src = open(sys.argv[1]).read(); t = ast.parse(src)
hits = []
for n in ast.walk(t):
    if isinstance(n, ast.Call):
        f = ast.unparse(n.func)
        if f.split('.')[-1] in ('run', 'check_output', 'Popen', 'call', 'check_call'):
            hits.append(('subprocess', n.lineno, ast.unparse(n)[:100]))
    if isinstance(n, ast.Attribute) and n.attr == 'environ':
        hits.append(('env', n.lineno, ''))
    if isinstance(n, ast.Name) and n.id in ('_MANIFEST_PROSPECTIVE', '_MANIFEST_BASELINE'):
        hits.append(('state', n.lineno, n.id))
    if isinstance(n, ast.Constant) and isinstance(n.value, str) and (
            'verification/seals' in n.value or n.value in ('seals', 'seals/')):
        hits.append(('seals', n.lineno, n.value[:70]))
    if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value.split(' ')[0] in (
            'rev-parse', 'rev-list', 'merge-base', 'ls-tree', 'cat-file', 'show', 'log', 'diff-tree'):
        hits.append(('gitarg', n.lineno, n.value))
print(collections.Counter(h[0] for h in hits))
for h in hits:
    print(h)
