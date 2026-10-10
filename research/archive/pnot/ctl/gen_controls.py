#!/usr/bin/env python3
"""Generate PARITY-NOT-1's controls.py from the reference module, the frozen family and D (frozen texts embedded
verbatim).  usage: gen_controls.py <module-file> <family.json> <D>   (run inside a checkout that has D)"""
import json, os, re, subprocess, sys
MODF, FAMF, DREF = sys.argv[1], sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'controls.py')
parts = [open(os.path.join(HERE, p), encoding='utf-8').read() for p in
         ('head.py', 'helpers.py', 'generic.py', 'body.py', 'mutators.py', 'selftest.py')]
template = '\n'.join(p.rstrip('\n') + '\n' for p in parts)
ns = {'D': DREF, 'LEAN': 'verification/lean-mathlib/OIBridge/', 'FAILS': [], 'COUNT': [0]}
src = template[template.index('DECL = re.compile'):template.index('\ndef must_fail')]
src = src.replace("FAILS, COUNT = [], [0]\n", '')
exec('import io, json, re, subprocess, sys\n' + src, ns)
mod = open(MODF, encoding='utf-8').read()
blob = subprocess.run(['git', 'hash-object', '-w', '--stdin'], input=mod, capture_output=True, text=True).stdout.strip()
decls = [[k, n] for k, n in ns['decls'](mod)]
texts = {n: c for n, (_, c, _) in ns['decl_chunks'](mod).items()}
assert len(texts) == len(decls), 'duplicate declaration names'
prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
landed = ns['landed_at_d']()
assert len(landed) == 8, sorted(landed)
fam = json.load(open(FAMF, encoding='utf-8'))
rep = {'@@D@@': DREF, '@@BLOB@@': blob,
       '@@CENSUS_FAMILY@@': json.dumps(fam, ensure_ascii=False, indent=1),
       '@@DECLS@@': json.dumps(decls, ensure_ascii=False, indent=1),
       '@@TEXTS@@': json.dumps(texts, ensure_ascii=False, indent=1),
       '@@PRINTS@@': json.dumps(prints, ensure_ascii=False, indent=1),
       '@@PREAMBLE@@': json.dumps(ns['preamble'](mod), ensure_ascii=False),
       '@@CONTEXT@@': json.dumps(ns['context_lines'](mod), ensure_ascii=False, indent=1),
       '@@LANDED@@': json.dumps(landed, ensure_ascii=False, indent=1),
       '@@NPRINTS@@': str(len(prints))}
out = template
for key, v in rep.items():
    assert out.count(key) == 1, key
    assert "'''" not in v, key
    out = out.replace(key, v)
open(OUT, 'w', encoding='utf-8').write(out)
print('blob', blob, 'decls', len(decls), 'prints', len(prints), 'landed', len(landed))
