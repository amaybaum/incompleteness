#!/usr/bin/env python3
"""Generate DIM-1's controls.py from the design tree (frozen texts embedded verbatim).
usage: gen_controls_dim1.py <worktree-or-ref> <D>

<worktree-or-ref> is a directory holding the design tree, or a commit whose files are read with `git show`.
<D> is the drafting snapshot; the census, ROADMAP and NativeGateBall texts at D fix the frozen edits."""
import difflib, json, os, re, subprocess, sys

SRC = sys.argv[1]
DREF = sys.argv[2]
OUT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/round2/controls_dim1.py'
MOD = 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
NGB = 'verification/lean-mathlib/OIBridge/NativeGateBall.lean'

template = open(OUT + '.template', encoding='utf-8').read()
# The extraction functions are the template's own, so the generator and the frozen checks cannot disagree.
ns = {}
src_funcs = template[template.index('DECL = re.compile'):template.index('\nPREFIX = ')]
exec('import io, json, re, subprocess, sys\n' + src_funcs, ns)


def git(*a):
    r = subprocess.run(['git'] + list(a), capture_output=True, text=True)
    assert r.returncode == 0, (a, r.stderr)
    return r.stdout


def read(path):
    if os.path.isdir(SRC):
        return open(os.path.join(SRC, path), encoding='utf-8').read()
    return git('show', '%s:%s' % (SRC, path))


mod = read(MOD)
blob = subprocess.run(['git', 'hash-object', '--stdin'], input=mod, capture_output=True, text=True).stdout.strip()
decls = [[k, n] for k, n in ns['decls'](mod)]
texts = {n: c for n, (_, c, _) in ns['decl_chunks'](mod).items()}
assert len(texts) == len(decls), 'duplicate declaration names'
prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
assert len(prints) == 87, len(prints)
ctx = ns['context_lines'](mod)
pre = ns['preamble'](mod)

# census: the DIM-1 family and the NB-1 sentence
census = json.loads(read(CENSUS))
fam = [f for f in census['families'] if f['modules'] == ['CompositeDimension']]
assert len(fam) == 1
dcen = json.loads(git('show', DREF + ':' + CENSUS))
k = [i for i, f in enumerate(dcen['families']) if f['modules'] == ['CompositeInterface']]
assert len(k) == 1
assert census['families'][k[0] + 1] == fam[0]
nb_d = [f for f in dcen['families'] if f['modules'] == ['NativeGateBall']]
nb_e = [f for f in census['families'] if f['modules'] == ['NativeGateBall']]
assert len(nb_d) == 1 and len(nb_e) == 1
na, nb = nb_d[0]['note'], nb_e[0]['note']
i = 0
while na[i] == nb[i]:
    i += 1
j = 0
while na[-1 - j] == nb[-1 - j]:
    j += 1
s = na.rfind('; ', 0, i) + 2
e_a = na.index('.', len(na) - j) + 1
e_b = nb.index('.', len(nb) - j) + 1
nb1_old, nb1_new = na[s:e_a], nb[s:e_b]
assert na.count(nb1_old) == 1 and na.replace(nb1_old, nb1_new, 1) == nb, (nb1_old, nb1_new)

# ROADMAP: the P1 parenthetical and the K1 bullet
ra, rb = git('show', DREF + ':' + ROADMAP), read(ROADMAP)
al, bl = ra.splitlines(True), rb.splitlines(True)
ops = [o for o in difflib.SequenceMatcher(None, al, bl, autojunk=False).get_opcodes() if o[0] != 'equal']
assert len(ops) == 2 and all(o[0] == 'replace' for o in ops), ops
pat = r'K1 \*\*CONDITIONAL\*\* \([^)]*\)'
p_old, p_new = re.findall(pat, ''.join(al[ops[0][1]:ops[0][2]])), re.findall(pat, ''.join(bl[ops[0][3]:ops[0][4]]))
assert len(p_old) == 1 and len(p_new) == 1
b_old, b_new = ''.join(al[ops[1][1]:ops[1][2]]), ''.join(bl[ops[1][3]:ops[1][4]])
edits = [[p_old[0], p_new[0]], [b_old, b_new]]
want = ra
for o, n in edits:
    assert ra.count(o) == 1, o
    want = want.replace(o, n, 1)
assert want == rb

# NativeGateBall's declaration names at D
ngb = git('show', DREF + ':' + NGB)
ngb_names = sorted({n for _, n in ns['decls'](ngb)})

rep = {
    '@@D@@': DREF if re.fullmatch(r'[0-9a-f]{40}', DREF) else '@@D@@',
    '@@BLOB@@': blob,
    '@@CENSUS_FAMILY@@': json.dumps(fam[0], ensure_ascii=False, indent=1),
    '@@NB1_OLD@@': json.dumps(nb1_old, ensure_ascii=False),
    '@@NB1_NEW@@': json.dumps(nb1_new, ensure_ascii=False),
    '@@ROADMAP_EDITS@@': json.dumps(edits, ensure_ascii=False, indent=1),
    '@@NGB_NAMES@@': json.dumps(ngb_names, ensure_ascii=False),
    '@@DECLS@@': json.dumps(decls, ensure_ascii=False, indent=1),
    '@@TEXTS@@': json.dumps(texts, ensure_ascii=False, indent=1),
    '@@PRINTS@@': json.dumps(prints, ensure_ascii=False, indent=1),
    '@@PREAMBLE@@': json.dumps(pre, ensure_ascii=False),
    '@@CONTEXT@@': json.dumps(ctx, ensure_ascii=False, indent=1),
}
out = template
for key, v in rep.items():
    assert out.count(key) == 1, key
    assert "'''" not in v, key
    out = out.replace(key, v)
open(OUT, 'w', encoding='utf-8').write(out)
print('blob', blob, 'decls', len(decls), 'prints', len(prints), 'ctx', len(ctx), 'ngb', len(ngb_names))
print('nb1', repr(nb1_old), '->', repr(nb1_new))
