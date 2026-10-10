#!/usr/bin/env python3
"""Generate RELC-SELECT-1's controls.py from the four reference modules, the frozen family, the frozen earned reading
and non-inference rule, and D (frozen texts embedded verbatim).
usage: gen_controls.py <refdir> <family.json> <frozen.json> <D>   (run inside a checkout that has D)"""
import json, os, re, subprocess, sys
REFDIR, FAMF, FROZF, DREF = sys.argv[1:5]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'controls.py')
MODULES = ['RelcSelectParity', 'RelcSelectBlock', 'RelcSelectSqueeze', 'RelcSelectC5']
parts = [open(os.path.join(HERE, p), encoding='utf-8').read() for p in
         ('head.py', 'helpers.py', 'generic.py', 'body.py', 'mutators.py', 'selftest.py')]
template = '\n'.join(p.rstrip('\n') + '\n' for p in parts)
ns = {'D': DREF, 'LEAN': 'verification/lean-mathlib/OIBridge/', 'MODULES': MODULES, 'FAILS': [], 'COUNT': [0]}
src = template[template.index('DECL = re.compile'):template.index('\ndef must_fail')]
src = src.replace("FAILS, COUNT = [], [0]\n", '')
exec('import hashlib, io, json, re, subprocess, sys\n' + src, ns)
mods = {m: open(os.path.join(REFDIR, m + '.lean'), encoding='utf-8').read() for m in MODULES}
blobs, decls, texts, prints, pre, ctx = {}, {}, {}, {}, {}, {}
for m, mod in mods.items():
    blobs[m] = subprocess.run(['git', 'hash-object', '-w', '--stdin'], input=mod, capture_output=True,
                              text=True).stdout.strip()
    decls[m] = [[k, n] for k, n in ns['decls'](mod)]
    texts[m] = {n: c for n, (_, c, _) in ns['decl_chunks'](mod).items()}
    assert len(texts[m]) == len(decls[m]), 'duplicate declaration names in ' + m
    prints[m] = re.findall(r'^#print axioms (\S+)', mod, re.M)
    pre[m] = ns['preamble'](mod)
    ctx[m] = ns['context_lines'](mod)
landed = ns['landed_at_d']()
need = (['NativeGate#header', 'NativeGate#fields', 'IsNot', 'Entangling', 'GateRel#fields', 'nativeGate#names']
        + ['NativeGate#' + f for f in ns['GATE_FIELDS']] + ['GateRel#relT', 'GateRel#relC']
        + list(ns['LANDED_CD_THMS']) + list(ns['LANDED_PN_DEFS']) + list(ns['LANDED_PN_THMS'])
        + ['copy#' + o for o in ns['COPY_MAP']])
missing = [k for k in need if k not in landed]
assert not missing, missing
assert len(landed) == len(need), sorted(set(landed) - set(need))
fam = json.load(open(FAMF, encoding='utf-8'))
fro = json.load(open(FROZF, encoding='utf-8'))
rep = {'@@D@@': DREF,
       '@@BLOBS@@': json.dumps(blobs, ensure_ascii=False, indent=1),
       '@@CENSUS_FAMILY@@': json.dumps(fam, ensure_ascii=False, indent=1),
       '@@DECLS@@': json.dumps(decls, ensure_ascii=False, indent=1),
       '@@TEXTS@@': json.dumps(texts, ensure_ascii=False, indent=1),
       '@@PRINTS@@': json.dumps(prints, ensure_ascii=False, indent=1),
       '@@PREAMBLE@@': json.dumps(pre, ensure_ascii=False, indent=1),
       '@@CONTEXT@@': json.dumps(ctx, ensure_ascii=False, indent=1),
       '@@LANDED@@': json.dumps(landed, ensure_ascii=False, indent=1, sort_keys=True),
       '@@NPRINTS@@': json.dumps({m: len(prints[m]) for m in MODULES}),
       '@@EARNED@@': json.dumps(fro['earned'], ensure_ascii=False, indent=1),
       '@@NONINF@@': json.dumps(fro['non_inference'], ensure_ascii=False, indent=1)}
out = template
for key, v in rep.items():
    assert out.count(key) == 1, key
    assert "'''" not in v, key
    out = out.replace(key, v)
open(OUT, 'w', encoding='utf-8').write(out)
print('blobs', blobs)
print('decls', {m: len(decls[m]) for m in MODULES}, 'prints', {m: len(prints[m]) for m in MODULES},
      'landed', len(landed))
