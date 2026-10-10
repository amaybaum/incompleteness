"""Scratch: the caller census for the verifier's projection mode. Lists the module-level names the
edit removes from tools/v3_verifier.py and every reference to them, or to the removed modes, in the
tracked files of a tree. Usage: callers.py <verifier at D> <verifier edited> <tree root>"""
import ast, os, re, subprocess, sys
def names(p):
    t = ast.parse(open(p, encoding='utf-8').read())
    out = set()
    for n in t.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out.add(n.name)
        elif isinstance(n, ast.Assign):
            out |= {x.id for x in n.targets if isinstance(x, ast.Name)}
    return out
gone = sorted(names(sys.argv[1]) - names(sys.argv[2]))
root = sys.argv[3]
files = subprocess.run(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=root, capture_output=True).stdout.split(b'\0')
pats = [re.compile(r'\b(v3|v3_verifier)\.%s\b' % g) for g in gone] + [
    re.compile(r'v3_verifier\.py[^\n]*--(project|mode)\b')]
print('removed names:', ', '.join(gone))
hits = 0
for f in files:
    f = f.decode()
    if not f or not os.path.isfile(os.path.join(root, f)) or f.startswith('verification/infrastructure/round-') \
            or f.startswith('verification/receipts/'):
        continue
    try:
        text = open(os.path.join(root, f), encoding='utf-8').read()
    except (UnicodeDecodeError, IsADirectoryError):
        continue
    for i, line in enumerate(text.split('\n'), 1):
        if any(p.search(line) for p in pats):
            print('CALLER  %s:%d  %s' % (f, i, line.strip()[:100]))
            hits += 1
print('callers: %d' % hits)
