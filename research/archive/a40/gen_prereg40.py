"""Assemble A40's preregistration from the single source (props40.json, texts40.json) and the frozen facts.
usage: python3 gen_prereg40.py  -> rec/preregistration.md (fills every @@TOKEN@@; refuses to write if one is left)"""
import hashlib, importlib.util, json, os, re
S = os.path.dirname(os.path.abspath(__file__)) + '/'
P = json.load(open(S + 'props40.json'))
T = json.load(open(S + 'texts40.json'))
C_ = P['COMPONENTS']; PR = P['PROPS']
HEAD = C_['HEAD']
def body(k):
    assert PR[k].startswith(HEAD)
    return PR[k][len(HEAD):]
def blob_of(path):
    b = open(path, 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
def lean(t):
    return '```lean\n' + t.rstrip('\n') + '\n```\n'
def quote(t):
    return '> ' + t + '\n'
spec = importlib.util.spec_from_file_location('c40', S + 'rec/controls.py'); CT = importlib.util.module_from_spec(spec); spec.loader.exec_module(CT)
PROBE_BLOB = blob_of(S + 'dita_torus_locus_probe.py')
MODULE_BLOB = blob_of(S + 'mod40F.lean')
assert CT.PROBE_BLOB == PROBE_BLOB and CT.MODULE_BLOB == MODULE_BLOB, (CT.PROBE_BLOB, PROBE_BLOB, CT.MODULE_BLOB, MODULE_BLOB)
CONTROLS_BLOB = blob_of(S + 'rec/controls.py')
log = open(S + 'probe40b.log', encoding='utf-8').read()
NPASS = len(re.findall(r'(?m)^\s+PASS\s', log)); assert NPASS == 22 and 'FAIL' not in log and 'dita_torus_locus_probe: OK' in log
ROAD = {lab: blob_of(S + 'roadmap-%s.md' % lab) for lab in ('A40-LOCUS-CLASSIFIED', 'A40-LOCUS-FAILS')}
NAMES = {'1': 'u₁', '2': 'u₂', '3': 'u₃'}
MAPS = {'k1': 'ditak1', 'k2': 'ditak2', 'k3': 'ditak3', 'k4': 'ditak4', 'e1': 'ditae1', 'e2': 'ditae2',
        't1': 'dita28', 't2': 'ditat2', 't3': 'ditat3', 'mc': 'ditamc', 'mr': 'ditamr'}
ORIG = {'k1': "act 37's class `k1`", 'k2': "act 37's class `k2`", 'k3': "act 37's class `k3`", 'k4': "act 37's class `k4`",
        'e1': "act 37's class `e1`", 'e2': "act 37's class `e2`", 't1': "act 36's frozen `2 × 8` class",
        't2': "act 37's class `t2`", 't3': "act 37's class `t3`", 'mc': "act 38's `M_COL`", 'mr': "act 38's `M_ROW`"}

excl_rows = []
for k, eqs in P['EQS'].items():
    nm, o = k.split('_')
    form = ('`%s X Y D`' if o == 'c' else '`(%s X Y D)ᵀ`') % MAPS[nm]
    excl_rows.append('| `a40_shared_excl_%s` | %s | %s | %s |' % (k, ORIG[nm], form, ' ∧ '.join('`%s = %s`' % (NAMES[str(c)], x) for c, x in eqs)))

props_md = []
props_md.append('### `P_R` — the kernel layer\n\nThe head, then:\n\n' + lean(body('P_R')))
props_md.append('### `P_N` — its negation\n\nThe head, then:\n\n' + lean(body('P_N'))
                + '\n`P_N` is `P_R`\'s negation: the conjunction of the twenty-five kernel statements becomes the disjunction of\ntheir negations. `controls.py` rebuilds both from the shared components and rejects any drift.\n')
FACE_TXT = {'FACE_1p': ('u₁ = 1', '`H3` is a strict Diţă product `ditat2 X Y D`', "act 37's class `t2`, column form"),
            'FACE_1m': ('u₁ = −1', '`H3` is a strict Diţă product `ditamc X Y D`', "act 38's `M_COL`, column form"),
            'FACE_2p': ('u₂ = 1', '`H3` is a strict Diţă product `dita28 X Y D`', "act 36's frozen `2 × 8` class, column form"),
            'FACE_3p': ('u₃ = 1', '`H3` is the transpose `(dita28 X Y D)ᵀ` of a strict Diţă product', "act 36's frozen `2 × 8` class, row form"),
            'FACE_3m': ('u₃ = −1', '`H3` is the transpose `(ditamr X Y D)ᵀ` of a strict Diţă product', "act 38's `M_ROW`, row form")}
s = '### `A40-1` — the five faces, required under `A40-LOCUS-CLASSIFIED`\n\n'
for k, (face, form, what) in FACE_TXT.items():
    s += '`%s`, `a40_shared_%s` — at every point of the face `%s`, %s (%s), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:\n\n%s\n' % (
        k, k.lower(), face, form, what, lean(body(k)))
props_md.append(s)
s = '### `A40-2` — the twenty named exclusions, required under `A40-LOCUS-CLASSIFIED`\n\n'
s += ('| theorem | index map | strict Diţă form | forces |\n| --- | --- | --- | --- |\n' + '\n'.join(excl_rows) + '\n\n')
for k in P['PARTS'][5:]:
    s += '`%s`, `a40_shared_%s`. The head, then:\n\n%s\n' % (k, k.lower(), lean(body(k)))
props_md.append(s)
PROPS_MD = '\n'.join(props_md)

REP = {
 '@@CLAUSE@@': '\n'.join('> ' + l for l in T['CLAUSE'].split('\n')),
 '@@HEAD@@': lean(HEAD),
 '@@HEAD40@@': lean(C_['HEAD40']),
 '@@OPEN@@': lean(P['OPEN']),
 '@@PROPS@@': PROPS_MD,
 '@@SENT_PV@@': quote(T['SENTENCES']['A40-LOCUS-CLASSIFIED']),
 '@@SENT_FL@@': quote(T['SENTENCES']['A40-LOCUS-FAILS']),
 '@@SENT_UD@@': quote(T['SENTENCES']['A40-UNDECIDED']),
 '@@P0_END_D@@': quote(T['P0_END_D']),
 '@@P0_PV@@': '  ' + quote(T['P0_CASE']['A40-LOCUS-CLASSIFIED']),
 '@@P0_FL@@': '  ' + quote(T['P0_CASE']['A40-LOCUS-FAILS']),
 '@@P0_STANDING@@': '  ' + quote(T['P0_STANDING_40']),
 '@@PROBE_BLOB@@': PROBE_BLOB, '@@MODULE_BLOB@@': MODULE_BLOB, '@@CONTROLS_BLOB@@': CONTROLS_BLOB,
 '@@ROAD_PV@@': ROAD['A40-LOCUS-CLASSIFIED'], '@@ROAD_FL@@': ROAD['A40-LOCUS-FAILS'],
 '@@NPASS@@': str(NPASS),
}
t = open(S + 'preregistration.draft.md', encoding='utf-8').read()
for k, v in REP.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
left = re.findall(r'@@[A-Z0-9_]+@@', t)
os.makedirs(S + 'rec', exist_ok=True)
open(S + 'rec/preregistration.md', 'w', encoding='utf-8').write(t)
print('preregistration.md written, %d bytes; probe %s module %s controls %s; unfilled: %s' % (len(t.encode()), PROBE_BLOB, MODULE_BLOB, CONTROLS_BLOB, left))
