"""Scratch: the shallow-checkout control. Every Python file the probes job runs, with every
repository module it imports transitively, scanned for any way to reach repository history: a
subprocess or os.system/os.popen call, an import of subprocess, a git argument, a read of .git or
of the environment. Usage: histcontrol.py <repo root> <workflow> [<guard override>]"""
import ast, os, re, sys
root, wf = sys.argv[1], sys.argv[2]
override = sys.argv[3] if len(sys.argv) > 3 else None
text = open(os.path.join(root, wf), encoding='utf-8').read()
job = text[text.index('  probes:'):]
files = []
for wd, body in re.findall(r'working-directory: (\S+)\n\s+run: \|\n((?:\s{10}.*\n)+)', job):
    names = re.findall(r'[a-z0-9_]+', re.search(r'for p in (.*?); do', body, re.S).group(1).replace('\\', ' '))
    suffix = '_probe.py' if '${p}_probe.py' in body else '.py'
    files += [os.path.join(wd, n + suffix) for n in names]
GITCMD = {'rev-parse', 'rev-list', 'merge-base', 'ls-tree', 'cat-file', 'show', 'log', 'diff-tree',
          'fetch', 'for-each-ref', 'ls-remote', 'diff', 'blame', 'show-ref'}
def scan(path, src):
    hits = []
    t = ast.parse(src)
    for n in ast.walk(t):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mods = [a.name for a in n.names] if isinstance(n, ast.Import) else [n.module or '']
            if any(m.split('.')[0] in ('subprocess', 'pygit2', 'git', 'dulwich') for m in mods):
                hits.append(('import', n.lineno, ast.unparse(n)))
        if isinstance(n, ast.Call):
            f = ast.unparse(n.func)
            if f in ('os.system', 'os.popen') or f.split('.')[-1] in ('check_output', 'Popen', 'check_call') \
                    or f.startswith('subprocess.'):
                hits.append(('exec', n.lineno, f))
        if isinstance(n, ast.Attribute) and n.attr in ('environ', 'getenv'):
            hits.append(('env', n.lineno, ast.unparse(n)))
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            v = n.value
            if v in GITCMD or v == 'git' or re.search(r'(^|/)\.git(/|$)', v) or v.startswith('refs/'):
                hits.append(('git', n.lineno, v[:60]))
    return hits, t
def local_imports(path, t):
    out = []
    d = os.path.dirname(path)
    for n in ast.walk(t):
        mods = []
        if isinstance(n, ast.Import):
            mods = [a.name for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
            mods = [n.module]
        for m in mods:
            p = os.path.join(d, m.replace('.', '/') + '.py')
            if os.path.exists(os.path.join(root, p)):
                out.append(p)
    return out
seen, queue, total = set(), list(files), 0
while queue:
    p = queue.pop()
    if p in seen:
        continue
    seen.add(p)
    real = override if (override and p.endswith('edge_rigidity_probe.py')) else os.path.join(root, p)
    src = open(real, encoding='utf-8').read()
    hits, t = scan(p, src)
    for h in hits:
        print('HISTORY  %s:%d  %s  %s' % (p, h[1], h[0], h[2]))
    total += len(hits)
    queue += local_imports(p, t)
print('histcontrol: %d files run by the probes job (%d named), %d history site(s)' % (len(seen), len(files), total))
sys.exit(1 if total else 0)
