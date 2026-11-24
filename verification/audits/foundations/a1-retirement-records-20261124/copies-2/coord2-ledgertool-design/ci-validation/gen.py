"""Assembles the disposable workflow from src/template.yml: each `@@FILE name@@` line becomes the named file's lines
(helpers from src/, harness files from the local mutation harness), `@@CONFIG@@` the staged configuration as base64
of gzip -9n, `@@SUMS@@` the harness sha256 list; every inserted line is indented as the marker line."""
import base64, gzip, hashlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
IMPL = os.path.join(os.path.dirname(HERE), 'impl-v6.0e')
HARNESS = ['mutate_c2.py', 'mutants.py', 'mutants_c1.py', 'mutants_c2.py', 'mutants_cache.py']
CFG = os.path.join(IMPL, 'staging-4f4a9d58/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json')
def src(name):
    p = os.path.join(IMPL, 'mut', 'scripts', name) if name in HARNESS else os.path.join(HERE, 'src', name)
    return open(p, 'rb').read()
cfg = open(CFG, 'rb').read()
assert hashlib.sha256(cfg).hexdigest() == '5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0'
b64 = base64.b64encode(gzip.compress(cfg, 9, mtime=0)).decode()
cfg_lines = [b64[i:i + 76] for i in range(0, len(b64), 76)]
sums = ['%s  %s' % (hashlib.sha256(src(n)).hexdigest(), n) for n in HARNESS]
out = []
for line in open(os.path.join(HERE, 'src', 'template.yml')).read().split('\n'):
    m = re.fullmatch(r'( *)@@(FILE (\S+)|CONFIG|SUMS)@@', line)
    if not m:
        out.append(line); continue
    ind = m.group(1)
    if m.group(3):
        body = src(m.group(3)).decode('utf-8')
        assert body.endswith('\n') and '\r' not in body and '\t' not in body
        lines = body[:-1].split('\n')
    elif m.group(2) == 'CONFIG':
        lines = cfg_lines
    else:
        lines = sums
    out += [(ind + l) if l else '' for l in lines]
open(sys.argv[1], 'w').write('\n'.join(out))
