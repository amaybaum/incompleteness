#!/usr/bin/env python3
"""Generate COMP-1's controls.py from the design module (frozen texts embedded verbatim).
usage: gen_controls_comp1.py <worktree> <D-commit-or-tree-with-ORD-1-family>"""
import json, re, subprocess, sys

WT = sys.argv[1].rstrip('/') + '/'
DREF = sys.argv[2]
OUT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/round2/controls_comp1.py'
MOD = 'verification/lean-mathlib/OIBridge/CompositeInterface.lean'
CENSUS = 'verification/lean-manuscript-census.json'

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and line.startswith('variable'):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


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
ctx = context_lines(mod)
pre = preamble(mod)
census = json.load(open(WT + CENSUS, encoding='utf-8'))
fam = [f for f in census['families'] if 'CompositeInterface' in f['modules']]
assert len(fam) == 1
family = fam[0]
dcen = json.loads(subprocess.run(['git', '-C', WT, 'show', DREF + ':' + CENSUS], capture_output=True,
                                 text=True).stdout)
prev = [f for f in dcen['families'] if 'CompositionOrder' in f['modules']]
assert len(prev) == 1
prev_prefix = prev[0]['name'][:60]
assert sum(1 for f in dcen['families'] if f['name'].startswith(prev_prefix)) == 1

template = open(OUT + '.template', encoding='utf-8').read()
rep = {
    '@@D@@': DREF if re.fullmatch(r'[0-9a-f]{40}', DREF) else '@@D@@',
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
