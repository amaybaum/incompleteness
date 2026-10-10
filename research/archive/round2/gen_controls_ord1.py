#!/usr/bin/env python3
"""Generate TRB-1's controls.py from the design module (frozen texts embedded verbatim)."""
import json, re, subprocess, sys

WT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/wt-ord1b/'
OUT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/round2/controls_ord1.py'
D = 'afa66d16d7adaffe94fb9bac391e6039c51dad8a'
MOD = 'verification/lean-mathlib/OIBridge/CompositionOrder.lean'
CENSUS = 'verification/lean-manuscript-census.json'

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def decl_texts(text):
    out = {}
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            chunk = chunk[:j] if j != -1 else chunk
        out[m.group(2)] = chunk
    return out


mod = open(WT + MOD, encoding='utf-8').read()
blob = subprocess.run(['git', '-C', WT, 'hash-object', MOD], capture_output=True, text=True).stdout.strip()
decls = [[m.group(1), m.group(2)] for m in DECL.finditer(mod)]
texts = decl_texts(mod)
prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
ctx = [m.group(0) for m in CTX.finditer(mod)]
pre = preamble(mod)
census = json.load(open(WT + CENSUS, encoding='utf-8'))
fam = [f for f in census['families'] if 'CompositionOrder' in f['modules']]
assert len(fam) == 1
family = fam[0]
idx = census['families'].index(family)
prev_prefix = census['families'][idx - 1]['name'][:60]

template = open(OUT + '.template', encoding='utf-8').read()
rep = {
    '@@BLOB@@': blob,
    '@@PREV_FAMILY_PREFIX@@': prev_prefix,
    '@@CENSUS_FAMILY@@': json.dumps(family, ensure_ascii=False, indent=1),
    '@@DECLS@@': json.dumps(decls, ensure_ascii=False, indent=1),
    '@@TEXTS@@': json.dumps(texts, ensure_ascii=False, indent=1),
    '@@PRINTS@@': json.dumps(prints, ensure_ascii=False, indent=1),
    '@@PREAMBLE@@': json.dumps(pre, ensure_ascii=False),
    '@@CONTEXT@@': json.dumps(ctx, ensure_ascii=False, indent=1),
}
for k, v in rep.items():
    assert template.count(k) == 1, k
    assert "'''" not in v, k
    template = template.replace(k, v)
open(OUT, 'w', encoding='utf-8').write(template)
print('blob', blob, 'decls', len(decls), 'prints', len(prints), 'ctx', len(ctx), 'prev', repr(prev_prefix))
for n in ('finiteOrderOn_of_stagePreserving', 'not_ordInf_of_finite_of_mulClosed', 'OrdInf', 'iterAfter'):
    print('---', n); print(texts[n])
