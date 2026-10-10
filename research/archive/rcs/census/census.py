#!/usr/bin/env python3
"""Statement census for the RELC-SELECT-1 design batch.
  census.py snapshot <out.json> <module.lean>...   record kind, name, statement (theorem/lemma: header up to `:=`;
                                                    def/structure/abbrev/instance: whole text) and sha256 per declaration
  census.py compare <frozen.json> <module.lean>... statements frozen: every frozen declaration present with an identical
                                                    statement; new declarations listed for review (helpers)"""
import hashlib, json, re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'odd', 'ctl'))
import io, subprocess
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'odd', 'ctl', 'helpers.py')).read()
ns = {'re': re, 'subprocess': subprocess, 'io': io, 'json': json}
exec(src, ns)
def census(paths):
    out = {}
    for p in paths:
        text = open(p, encoding='utf-8').read()
        mod = os.path.basename(p)
        for name, (kind, stmt, _proof) in ns['decl_chunks'](text).items():
            s = ns['norm'](stmt)
            out[mod + '::' + name] = {'kind': kind, 'stmt': s, 'sha256': hashlib.sha256(s.encode()).hexdigest()}
        out[mod + '::@file'] = {'sha256': hashlib.sha256(text.encode()).hexdigest(),
                                'prints': re.findall(r'^#print axioms (\S+)', text, re.M),
                                'sorry': bool(re.search(r'\bsorry\b', ns['code_only'](text))),
                                'axiom': bool(re.search(r'^\s*axiom\b', ns['code_only'](text), re.M))}
    return out
if sys.argv[1] == 'snapshot':
    c = census(sys.argv[3:]); json.dump(c, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
    decls = [k for k in c if not k.endswith('::@file')]
    print('declarations', len(decls)); [print(k, c[k]['sha256'][:12]) for k in c if k.endswith('::@file')]
else:
    f = json.load(open(sys.argv[2])); c = census(sys.argv[3:])
    changed = [k for k in f if not k.endswith('::@file') and (k not in c or c[k]['stmt'] != f[k]['stmt'] or c[k]['kind'] != f[k]['kind'])]
    new = [k for k in c if k not in f and not k.endswith('::@file')]
    bad = [k for k in c if k.endswith('::@file') and (c[k]['sorry'] or c[k]['axiom'])]
    print('frozen declarations', sum(1 for k in f if not k.endswith('::@file')))
    print('CHANGED/MISSING:', changed); print('NEW (review as helpers):', new); print('sorry/axiom:', bad)
    sys.exit(1 if changed or bad else 0)
