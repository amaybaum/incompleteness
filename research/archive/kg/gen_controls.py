#!/usr/bin/env python3
"""Generate K2-GUARD-1's controls.py from the design tree (frozen texts embedded verbatim).
usage: gen_controls.py <worktree-or-ref> <D>"""
import json, os, re, subprocess, sys
SRC, DREF = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'controls.py')
MOD = 'verification/lean-mathlib/OIBridge/K2Guard.lean'
DIM1 = 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'
CENSUS = 'verification/lean-manuscript-census.json'
parts = [open(os.path.join(HERE, p), encoding='utf-8').read() for p in
         ('head.py', 'helpers.py', 'body.py', 'mutators.py', 'selftest.py')]
template = '\n'.join(p.rstrip('\n') + '\n' for p in parts)
open(os.path.join(HERE, 'controls.py.template'), 'w', encoding='utf-8').write(template)
ns = {}
exec('import io, json, re, subprocess, sys\n' + template[template.index('DECL = re.compile'):template.index('\nPREFIX = ')], ns)
def git(*a):
    r = subprocess.run(['git'] + list(a), capture_output=True, text=True); assert r.returncode == 0, (a, r.stderr); return r.stdout
def read(path):
    if os.path.isdir(SRC): return open(os.path.join(SRC, path), encoding='utf-8').read()
    return git('show', '%s:%s' % (SRC, path))
mod = read(MOD)
blob = subprocess.run(['git', 'hash-object', '--stdin'], input=mod, capture_output=True, text=True).stdout.strip()
decls = [[k, n] for k, n in ns['decls'](mod)]
texts = {n: c for n, (_, c, _) in ns['decl_chunks'](mod).items()}
assert len(texts) == len(decls), 'duplicate declaration names'
prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
census = json.loads(read(CENSUS))
fam = [f for f in census['families'] if f['modules'] == ['K2Guard']]
assert len(fam) == 1
dcen = json.loads(git('show', DREF + ':' + CENSUS))
k = [i for i, f in enumerate(dcen['families']) if f['modules'] == ['K1Bridge']]
assert len(k) == 1 and census['families'][k[0] + 1] == fam[0]
rep = {'@@D@@': DREF, '@@BLOB@@': blob,
       '@@CENSUS_FAMILY@@': json.dumps(fam[0], ensure_ascii=False, indent=1),
       '@@DECLS@@': json.dumps(decls, ensure_ascii=False, indent=1),
       '@@TEXTS@@': json.dumps(texts, ensure_ascii=False, indent=1),
       '@@PRINTS@@': json.dumps(prints, ensure_ascii=False, indent=1),
       '@@PREAMBLE@@': json.dumps(ns['preamble'](mod), ensure_ascii=False),
       '@@CONTEXT@@': json.dumps(ns['context_lines'](mod), ensure_ascii=False, indent=1),
       '@@NPRINTS@@': str(len(prints))}
out = template
for key, v in rep.items():
    assert out.count(key) == 1, key
    assert "'''" not in v, key
    out = out.replace(key, v)
open(OUT, 'w', encoding='utf-8').write(out)
print('blob', blob, 'decls', len(decls), 'prints', len(prints))
