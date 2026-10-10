"""Derive A40's controls body from A39's frozen body by explicit, asserted replacements."""
import os
S = os.path.dirname(os.path.abspath(__file__))
b = open(os.path.join(S, '..', 'a39', '_body39.txt'), encoding='utf-8').read()
def rep(s, old, new, cnt=1):
    assert s.count(old) == cnt, (old, s.count(old))
    return s.replace(old, new)
b = rep(b, "PARTS = ('REAL',)\n\n\n", '')
i = b.index('SOURCE_TABLE = tuple('); j = b.index('def duality_ok')
b = b[:i] + '''SOURCE_TABLE = tuple(
    [(k, 'HEAD', 1) for k in PARTS + ('P_R', 'P_N')]
    + [(k, k, 1) for k in PARTS]
    + [(k, k2, 0) for k in PARTS for k2 in PARTS if k2 != k]
    + [('P_R', 'PKG', 1)] + [('P_R', k, 1) for k in PARTS] + [('P_N', k, 1) for k in PARTS])


''' + b[j:]
b = rep(b, '''    """P_R is the package statement over one head and P_N its negation, so each verdict is the
    other's negation; every other statement carries the one head; the head is act 38's frozen head
    followed by this round's objects."""''', '''    """P_R is the conjunction of the twenty-five kernel statements over one head and P_N the
    disjunction of their negations, so each verdict is the other's negation; every statement carries
    the one head, and each kernel statement its own part and no other; the head is act 39's frozen
    head followed by this round's objects."""''')
b = rep(b, "f.append('duality:PKG-is-not-the-package')", "f.append('duality:PKG-is-not-the-conjunction-of-the-twenty-five')")
b = rep(b, """    if comps['HEAD38'] != A38_HEAD or comps['HEAD'] != comps['HEAD38'] + comps['HEAD39']:
        f.append('source:head-is-not-act-38s-head-followed-by-this-rounds-objects')""", """    if comps['HEAD39'] != A39_HEAD or comps['HEAD'] != comps['HEAD39'] + comps['HEAD40']:
        f.append('source:head-is-not-act-39s-head-followed-by-this-rounds-objects')""")
# the module's proofs are not frozen: the result note names the reference implementation's blob and the module's blob at
# E, and states the departure whenever they differ
b = rep(b, "def note_ok(note, label):\n    f = []\n", """def note_ok(note, label, mb):
    f = []
    if '`%s`' % EXPECTED_MODULE_BLOB[0] not in note or '`%s`' % mb not in note:
        f.append('note:module-blobs-not-reported')
    if mb != EXPECTED_MODULE_BLOB[0] and DEPARTURE not in note:
        f.append('note:departure-from-the-reference-implementation-not-reported')
""")
b = rep(b, "    f += note_ok(files_e.get(RDIR + 'result.md', ''), label)\n",
        "    f += note_ok(files_e.get(RDIR + 'result.md', ''), label, blob_id(files_e.get(MODULE, '')))\n")
b = rep(b, "def _note(label):\n    parts = ['# result\\n\\n**Outcome:** `%s`\\n\\n' % label, '> ' + SENTENCES[label] + '\\n\\n']\n",
        """def _note(label, mb):
    parts = ['# result\\n\\n**Outcome:** `%s`\\n\\n' % label, '> ' + SENTENCES[label] + '\\n\\n']
    parts.append('The reference implementation is `%s`; the module at E is `%s`.%s\\n\\n' % (
        EXPECTED_MODULE_BLOB[0], mb, '' if mb == EXPECTED_MODULE_BLOB[0] else ' The ' + DEPARTURE + ' is proof-only.'))
""")
b = rep(b, "    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label),\n",
        "    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label, blob_id(_module(label))),\n")
b = rep(b, "EXPECTED_PROBE_BLOB = [PROBE_BLOB]\n", "EXPECTED_PROBE_BLOB = [PROBE_BLOB]\nEXPECTED_MODULE_BLOB = [MODULE_BLOB]\nDEPARTURE = 'departure from the reference implementation'\n")
b = rep(b, "'dita_torus_probe: OK' not in note", "'dita_torus_locus_probe: OK' not in note")
b = rep(b, "P0_STANDING_39 + ' |'", "P0_STANDING_40 + ' |'")
b = rep(b, "return [] if wf_e == w else ['workflow:not-D-with-the-probe-added']", "return [] if wf_e == w else ['workflow:not-D-with-the-shard-added']")
b = rep(b, "th('a39_shared_x', 'True')", "th('a40_shared_x', 'True')")
b = rep(b, "'\\n\\ndita_torus_probe: OK -- x\\n'", "'\\n\\ndita_torus_locus_probe: OK -- x\\n'")
b = rep(b, "WORKFLOW: 'jobs:\\n  a38:\\n    run: |\\n' + PROBE_ANCHOR + '\\n  foundations:\\n'}",
        "WORKFLOW: 'jobs:\\n' + SHARD_ANCHOR + ''.join(old for old, new in WORKFLOW_EDITS[1:])}")
b = rep(b, "c['families'].append({'name': 'act 39', ", "c['families'].append({'name': 'act 40', ")
assert 'a39_' not in b and 'A39-' not in b and 'dita_torus_probe' not in b and 'A38' not in b and 'HEAD38' not in b, \
    [l for l in b.split('\n') if 'a39_' in l or 'A39-' in l or 'A38' in l]
b = rep(b, '''def norm(t):
    t = ' '.join(t.split())''', '''_NORM = {}


def norm(t):
    if t in _NORM:
        return _NORM[t]
    r = _norm(t)
    _NORM[t] = r
    return r


def _norm(t):
    t = ' '.join(t.split())''')
open(os.path.join(S, '_body40.txt'), 'w', encoding='utf-8').write(b)
print('ok')
